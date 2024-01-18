""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą
"""

"""def add_cash(budget_list: list, input_str: str) -> list:
    try:
        name, amount_str = input_str.split(':')
        amount = float(amount_str)
        budget_list.append((name.strip(), amount))
        print(f"${amount} added to the budget from '{name.strip()}'.")
    except ValueError:
        print("Invalid input. Please enter a valid transaction in the format 'Name: Amount'.")
    return budget_list

def cash_out(budget_list: list, input_str: str) -> list:
    try:
        name, amount_str = input_str.split(':')
        amount = float(amount_str)
        
        # Extract only the amounts from the budget_list for sum calculation
        current_balance = sum(transaction[1] for transaction in budget_list)
        
        if current_balance >= amount:
            budget_list.append((name.strip(), -amount))
            print(f"${amount} spent from the budget for '{name.strip()}'.")
        else:
            print("Insufficient funds.")
    except ValueError:
        print("Invalid input. Please enter a valid transaction in the format 'Name: Amount'.")
    return budget_list

def transactions(budget_list: list) -> None:
    print(">>> Transaction History <<<")
    for transaction in budget_list:
        name, amount = transaction
        if amount > 0:
            print(f"Added: Eur {amount} from '{name}'")
        else:
            print(f"Spent: Eur {-amount} for '{name}'")

def cash_flow_balance(budget_list: list) -> None:
    balance = sum(transaction[1] for transaction in budget_list)
    print(f"Current Cash Flow Balance: ${balance}")

def main(budget_list: list) -> None:
    while True:
        print(">>> Budget Holes System <<<")
        print("0: Exit")
        print("1: Add Cash")
        print("2: Cashout")
        print("3: Transactions")
        print("4: Cash Flow Balance")
        
        choice = input("Choice: ")
        if choice == "0":
            break
        elif choice == "1":
            input_str = input('Enter transaction (e.g., Salary: 2000): ')
            budget_list = add_cash(budget_list, input_str)
        elif choice == "2":
            input_str = input('Enter transaction (e.g., Grocery: 50): ')
            budget_list = cash_out(budget_list, input_str)
        elif choice == "3":
            transactions(budget_list)
        elif choice == "4":
            cash_flow_balance(budget_list)

main([])"""

# BUDGET MASCHINE#2
import pickle
import os

BUDGET_FILE = 'Budget program/budget_file.pkl'

if os.path.exists(BUDGET_FILE):
    with open(BUDGET_FILE, "rb") as budget_file:
        transfers = pickle.load(budget_file)
        transfers.append(transfer)
else:
    transfers = [transfer]
with open(BUDGET_FILE, "wb") as budget_file:
    

def income(money_in, amount, budget_main):
    budget_main[money_in] = +abs(float(amount))
    print(f'Eur {amount} amount was added.')
    return budget_main

def expense(money_out, amount, budget_main):
    budget_main[money_out] = -abs(float(amount))
    print(f'Eur {amount} amount was deducted.')
    return budget_main

def statment(budget_main):
    for key, value in budget_main.items():
        print(f'{key}  {value}')
    return budget_main

def balance(budget_main):
    whole_budget = sum(budget_main.values())
    print(f'{whole_budget:.2f}')
    return budget_main

budget_main = {}

while True:
    print(">>>> Budget Holes Checker <<<<")
    print("0: Exit")
    print("1: Add Income")
    print("2: Add Expense")
    print("3: Print Transactions List")
    print("4: Current Balance")
    choice = input("Choose your task: ")
    if choice == "0":
        print('Bye bye :)')
        break
    elif choice == "1":
        money_in = input("Enter transaction name: ")
        amount = input('Enter the amount to add: ')
        budget_main = income(money_in, amount, budget_main)
    elif choice == "2":
        money_out = input("Enter deduction transaction name: ")
        amount = input("Enter deduction amount: ")
        budget_main = expense(money_out, amount, budget_main)
    elif choice == "3":
        statment(budget_main)
    elif choice == "4":
        balance(budget_main)
    else:
        print("Bad input check your numbers!")
        pass