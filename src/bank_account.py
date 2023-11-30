import secrets
import datetime

from src.bank import Bank
from src.person import Person
"""
Här skulle kanske du nog skulle vilja att owner är en typ av Person så slipper du ärva från den här klassen i Person classen (har kommenterat där)
"""
class BankAccount:
    account_id = int(0)

    def __init__(self, password: str, owner: Person, balance: float = 0):
        self.owner = owner
        self.password = password
        self.account_number = BankAccount.account_number_generator()
        BankAccount.add_id()
        self.id = BankAccount.account_id
        self.balance = balance
        self.transaction_history = {"Deposits": [], "Withdrawals": [], "Merges": []}

    @classmethod
    def add_id(cls):
        cls.account_id += 1

    @classmethod
    def account_number_generator(cls):
        """
        Method that generates a 10 byte hexadecimal "unique" value used as account number
        """
        account_number = secrets.token_hex(10)
        return account_number
    
    """
    Inte helt med på varför du vill ha dessa som statiska metoder men inte heller fel
    Men tror nog att sånna statiska metoder nog hade varit mer lämpliga i en annan typ av klass som sedan anropar bank_account's deposit metod osv. 
    """
    @staticmethod
    def deposit(amount, id_input, password):
        date_and_time = datetime.datetime.now()
        string_date_time = date_and_time.strftime("%Y-%b-%d-%X")
        for accounts in Bank.bank_account_ledger.values():
            if password == accounts.password and id_input == accounts.id:
                accounts.balance += amount
                accounts.transaction_history["Deposits"].append({string_date_time: amount})
                return f"Deposited amount: {amount}"

        return f"Please check your input parameters"
    @staticmethod
    def withdraw(amount, id_input, password):
        date_and_time = datetime.datetime.now()
        string_date_time = date_and_time.strftime("%Y-%b-%d-%X")
        """
        Det här är inte jätteeffektivt. Om du tänker dig att en bank har miljontals konton, i värsta fall behöver du
        loopa igenom alla dessa innan du kommer till kontot. Typiskt sett skulle det räcka med att du vet id_input och kan slå upp kontot
        direkt från en dictionary. Det är mycket snabbare
        
        """
        
        for accounts in Bank.bank_account_ledger.values():
            if password == accounts.password and id_input == accounts.id:
                if accounts.balance >= amount:
                    accounts.balance -= amount
                    accounts.transaction_history["Withdrawals"].append({string_date_time: amount})
                    return f"Withdrawn amount: {amount}"
                else:
                    return f"Insufficient funds. Current balance: {accounts.balance}"
        return f"Wrong ID or PASSWORD"

    def get_balance(self, id_input: int, password: str):
        for accounts in self.account_keeper.values():
            if id_input == accounts.id and password == accounts.password:
                return f'Current balance: {accounts.balance}'