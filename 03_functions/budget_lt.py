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
# Initialize dictionaries to store income and expenses for different categories
income_categories = {}
expenses_categories = {}

# Function to add income to a specific category
def add_income(category, amount):
    income_categories[category] = income_categories.get(category, 0) + amount

# Function to add expense to a specific category
def add_expense(category, amount):
    expenses_categories[category] = expenses_categories.get(category, 0) + amount

# Function to calculate balance for a specific category
def calculate_balance(category):
    income = income_categories.get(category, 0)
    expenses = expenses_categories.get(category, 0)
    balance = income - expenses
    print(f"\nCurrent Balance for '{category}': Eur{balance}")

# Function to print statement summary for all categories
def statement_summary():
    print("\nStatement Summary:")
    for category in set(income_categories.keys()).union(expenses_categories.keys()):
        income = income_categories.get(category, 0)
        expenses = expenses_categories.get(category, 0)
        balance = income - expenses
        print(f"\nCategory: '{category}'")
        print(f"Income: Eur{income}")
        print(f"Expenses: Eur{expenses}")
        print(f"Balance: Eur{balance}")

# Main loop
def main(budgeter: list):
    while True:
        print("\nBudget Holes:")
        print("0. Exit")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Balance")
        print("4. Statement Summary")

        choice = input("Enter your choice (0-4): ")

        if choice == '0':
            print("Exiting the budget calculator. Goodbye!")
            break
        elif choice == '1':
            category = input("Enter the income category: ")
            amount = float(input("Enter the income amount: "))
            add_income(category, amount)
        elif choice == '2':
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            add_expense(category, amount)
        elif choice == '3':
            category = input("Enter the category to calculate balance: ")
            calculate_balance(category)
        elif choice == '4':
            statement_summary()
    



"""def main(budget_list: list) -> None:
    while True:
        print(">>> Budget Holes System <<<")
        print("0: Exit")
        print("1: Add Cash")
        print("2: Cashout")
        print("3: Trasactions")
        print("4: Cash Flow Balance")
        
        choice = input("Choice: ")
        if choice == "0":
            break
        elif choice == "1":
            budget_list = add_cash(budget_list, input('Amount of money to add: '))
        elif choice == "2":
            budget_list = cash_out(budget_list, input('Amount of money spent: '))


main([])"""