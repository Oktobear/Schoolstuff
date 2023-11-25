# Project Name

Bank Assignment

## Description

Bank, BankAccount and Person class combined to perform banking tasks in accordance with Sensei Lambda's orders.


## Table of Contents

- [Project Name](#project-name)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Features

Key features include:
1.Individual account holder for banks and persons
2.Add an existing bank account to another bank
3.Password protected withdrawals/deposits and accounts
4.Transaction history showing precise time and date and type of transaction
5.Merge accounts through authentication
ETC

## Getting Started

### Prerequisites

Python
pip
Pytest

### Installation


```
To run in a python venv follow instructions from the official python documentation or below
> sudo mkdir .venv
> cd .venv/
> python -m venv .
> source ./bin/activate
> pip install pytest
```

## Usage

```
Create a person etc
> P = Person("first_name", "last_name", "YYMMDD")
> P.add_bank_account("password") # create new account
> P.account_holder[account_id].deposit(amount, account_id, "password")
> P.account_holder[account_id].withdraw(amount, acccount_id, "password")
> P.get_all_bank_accounts()
> P.transaction_history[account_id]

Create a bank etc
B = Bank(owner) ## Could be a person object or "Bank of America"
B.create_bank_account("password") # Create new account
B.add_bank_account(account_id) # add existing account to bank
B.close_bank_account(account_id, "password", transfer_id) ## account_id to close, password of account to close, and transfer_id for transferring remaining funds(if there are)
B.generate_accounts_report() # Generate .csv account report
B.get_accounts_for_person(person_id, "first_name", "last_name")
B.merge_account(account_id, "password", transfer_id) ## Same here, account_id to merge, password of account to merge, transfer_id of account to put remaining funds
```





## License

Example License

## Acknowledgements

Credits to the creators of modules and programming language. Hail internet.

