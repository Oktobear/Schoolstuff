import pytest
from solution import (Bank, BankAccount, Person)

@pytest.fixture
def sample_bank():
    return Bank(owner="Test Owner")
@pytest.fixture
def sample_bank2():
    return Bank(owner="Test Owner")
@pytest.fixture
def sample_person():
    return Person(first_name="John", last_name="the Baptist", birth_date="911023")
@pytest.fixture
def sample_person2():
    return Person(first_name="Seneca", last_name="the Stoic", birth_date="010101")

def test_create_bank_account(sample_bank):
    password = "test_password"
    account = sample_bank.create_bank_account(password, sample_bank)

    assert isinstance(account, BankAccount)
    assert account.password == password
    assert account.id in sample_bank.account_keeper.keys()  # Assuming this is the first account created in the test

def test_close_bank_account(sample_bank):
    password = "test_password"
    account1 = sample_bank.create_bank_account(password, sample_bank)
    account2 = sample_bank.create_bank_account(password, sample_bank)

    # Assuming some balance in the account to be closed
    sample_bank.account_keeper[account1.id].balance = 100

    result = sample_bank.close_bank_account(account1.id, account1.password, account2.id)

    assert result == 'Success'
    assert account1 not in sample_bank.account_keeper.values()
    assert sample_bank.account_keeper[account2.id].balance == 100


def test_merge_account(sample_bank):
    password = "test_password"
    account1 = sample_bank.create_bank_account(password, sample_bank)
    account2 = sample_bank.create_bank_account(password, sample_bank)

    # Assuming some balance in the account to be closed
    account1.balance = 100

    result = sample_bank.merge_account(account1.id, account1.password, account2.id)

    assert result == 'Success'
    assert account1 not in sample_bank.account_keeper.values()
    assert account2.balance == 100
    assert not account1.transaction_history
    assert account2.transaction_history["Merges"]


def test_deposit_bank(sample_bank):
    password = "test_password"
    account1 = sample_bank.create_bank_account(password, sample_bank)

    result = sample_bank.deposit(23480234, account1.id, password)

    assert result == 'Deposited amount: 23480234'
    assert account1.balance == 23480234

def test_withdraw_bank(sample_bank):
    password = "test_password"
    account1 = sample_bank.create_bank_account(password, sample_bank)


    sample_bank.deposit(23480234, account1.id, password)
    result = sample_bank.withdraw(23480233, account1.id, password)

    assert result == 'Withdrawn amount: 23480233'
    assert account1.balance == 1
