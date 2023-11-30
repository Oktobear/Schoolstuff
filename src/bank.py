import datetime
from src.bank_account import BankAccount


class Bank(BankAccount):
    bank_id = int()
    bank_account_ledger = dict()
    bank_ledger = list()
    person_ledger = list()

    def __init__(self, owner):
        self.owner = owner
        Bank.add_id()
        self.id = Bank.bank_id
        Bank.bank_ledger.append(self)
        self.account_keeper = dict()

    @classmethod
    def add_id(cls):
        cls.bank_id += 1

    def create_bank_account(self, password: str, owner):
        bank_account = BankAccount(password, owner)
        if not bank_account.id in Bank.bank_account_ledger.keys() and not bank_account.id in self.account_keeper.keys():
            self.account_keeper[bank_account.id] = bank_account
            Bank.bank_account_ledger[bank_account.id] = bank_account
            return bank_account
        else:
            return f'Try again'

    def add_bank_account(self, id_input: int, password: str) -> None:
        """
        id_input == id of the bank account to add
        password == password of the bank account you would like to add
        """
        for account in Bank.bank_account_ledger.values():
            if id_input == account.id and password == account.password and not id_input in self.account_keeper.keys():
                self.account_keeper[account.id] = account
                for instance in Bank.bank_ledger:
                    if account in instance.account_keeper and instance.id != self.id:
                        del instance.account_keeper[account.id]
                        return f'Success {self.account_keeper}'

    def close_bank_account(self, id_input: int, password: str, transfer_id: int):

        """
        id_input == id of account to close
        password == password of account to close
        transfer_id == id of account to transfer remaining balance to
        """
        for accounts in self.account_keeper.values():
            if accounts.id == id_input and accounts.password == password:
                if accounts.balance >= 0:
                    self.account_keeper[transfer_id].balance += accounts.balance
                    accounts.balance -= accounts.balance
                    del self.account_keeper[id_input]
                    del Bank.bank_account_ledger[id_input]
                    return f'Success'
                elif accounts.balance < 0:
                    return f'This client is in debt'

            else:
                return f'Something went wrong, try again'

    def generate_accounts_report(self):
        try:

            with open('accounts_report.csv', 'w', encoding='UTF8', newline='') as csvfile:

                writer = csv.writer(csvfile)
                writer.writerow([self.owner, self.id])

                for account in self.account_keeper.values():
                    headers = [key for key in account.__dict__.keys()]
                    values = [value for value in account.__dict__.values()]
                    writer.writerow(headers)
                    writer.writerow(values)
            return csvfile
        except Exception as e:
            return f'{e}'


        except FileNotFoundError as fnfe:
            return f'File does not exist {fnfe}'
        except PermissionError as pe:
            return f'Permission error {pe}'

    @staticmethod
    def get_accounts_for_person(id_input: int, first_name: str, last_name: str):
        for persons in Bank.person_ledger:
            if persons.id == id_input and first_name == persons.first_name and last_name == persons.last_name:
                temp_list = [accounts for accounts in persons.account_keeper.values()]
                return_dict = {}
                for account in temp_list:
                    set_to_append = (account.owner, account.password, account.balance, account.transaction_history)
                    return_dict[account.id] = set_to_append
            return return_dict

    def merge_account(self, id_to_close, password_to_close, transfer_id):
        """
        id_to_close == ACCOUNT ID OF OTHER ACCOUNT
        password_to_close == PASSWORD OF OTHER ACCOUNT
        transfer_id == ID OF ACCOUNT TO PUT REMAINING FUNDS

        """
        date_and_time = datetime.datetime.now()
        string_date_time = date_and_time.strftime("%Y-%b-%d-%X")
        for accounts in self.account_keeper.values():
            if id_to_close == accounts.id and password_to_close == accounts.password and transfer_id in self.account_keeper.keys():
                for accounts_ in self.account_keeper.values():
                    if accounts_.id == transfer_id and not transfer_id == id_to_close:
                        accounts_.balance += accounts.balance
                        accounts.balance = 0
                        accounts.transaction_history.clear()
                        accounts_.transaction_history["Merges"].append({string_date_time: "Success"})
                        del self.account_keeper[id_to_close]
                        del Bank.bank_account_ledger[id_to_close]
                        return f'Success'
        return f'Account not found or invalid credentials for merge operation'
