import json
import os

def addExpense(expenses, desc, amount, expenseRecordPath):

    newExpense = {
        "description": desc,
        "amount": amount  
    }

    existingData = []

    if os.path.exists(expenseRecordPath):
        with open(expenseRecordPath, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
            except json.JSONDecodeError:
                existingData = []
    else:
        existingData = []

    existingData.append(newExpense)

    with open(expenseRecordPath, 'w') as file:
        json.dump(existingData, file, indent=4)

    print(f"Added expense: {desc}, Amount: {amount}")

def showExpense(expenses):
    print("Expense : ")
    for expense in expenses:
        print(f" - {expense['description']} : {expense['amont']}")
    print(f"\nTotal Expense : {getTotalExpense(expenses)}")

def getTotalExpense(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amont']
    return sum

def loadBurgetData(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.loads(file)
            return data['initial_budget'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def main():
    print("Welcome to Budget app")
    filepath = 'budget_data.json'
    expenseRecordPath = 'expenses.json'
    initial_budget = loadBurgetData(filepath)
    expenses = []

    while True:
        print("What would you like to do ?")
        print("1) Add an Expense")
        print("2) Show budget details")
        print("3) Exit\n")

        while True:
            try:
                choice = int(input("Enter Your choice (1/2/3) : "))
                if(choice == 1):
                    desc = input("\nEnter expense description : ")
                    amount = float(input("Enter expense amount : "))
                    addExpense(expenses, desc, amount, expenseRecordPath)
                elif(choice == 2):
                    showExpense(expenses)
                elif(choice == 3):
                    print("3 Exit" )
                else:
                    print(f"Invalid input... Please enter a valid number.")
            except ValueError:
                print(f"Invalid input... Please enter a valid number.")

main()