from src.bank import Bank
from src.bank_account import BankAccount

"""
Bra grejer att du kör OOP
Några kommentarer att hålla koll på här dock, när man använder sig av arv så är det en form av "is-a" relation

Så Person(BankAccount) betyder att "Person är en typ av BankAccount".

Rimligare hade förmodligen varit att BankAccount(Account), då är BankAccount typ av Account. 
I ditt fall kanske en AccountHolder class kunde ha hålla de olika fälten first_name, last_name, etc. 

* Jag hade nog kanske döpt om classen till AccountHolder
* AccountHolder hade ärvt från Person, för man kan ju säga att AccountHolder är en typ av Person
* I AccountHolder classen hade man sedan haft en dict som håller varje BankAccount, kanske med id som nyckel
"""

class Person(BankAccount):
    person_id = int() # Kan sättas till 0

    @classmethod
    def add_id(cls):
        cls.person_id += 1

    def __init__(self, first_name: str, last_name: str, birth_date: str = "YYMMDD"):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        Person.add_id()
        self.id = Person.person_id
        self.account_keeper = dict()
        Bank.person_ledger.append(self)

    def add_bank_account(self, password):
        bank_account = BankAccount(password, self)
        if bank_account.id not in Bank.bank_account_ledger.keys():
            Bank.bank_account_ledger[bank_account.id] = bank_account
            self.account_keeper[bank_account.id] = bank_account
            return bank_account
        else:
            del bank_account
            return f'Something went wrong, try again'

    def get_all_bank_accounts(self):
        temp_dict = {}
        """
        Du kan använda dig av dictionary comprehension, en mer pythonic approach än att använda for loop
        
        temp_dict = {accounts.id: (accounts.balance, accounts.password, accounts.transaction_history) for accounts in self.account_keeper.values()}
        
        """
        for accounts in self.account_keeper.values():
            temp_dict[accounts.id] = ((accounts.balance, accounts.password, accounts.transaction_history))
        return f'{temp_dict}'

    def get_total_balance(self):
        total_balance = 0
        for accounts in self.account_keeper.values():
            total_balance += accounts.balance
        return f'Total balance: {total_balance}'