import json
import os

def addIncome(desc, amount, incomeRecordPath):

    newExpense = {
        "description": desc,
        "amount": amount  
    }

    existingData = []

    if os.path.exists(incomeRecordPath):
        with open(incomeRecordPath, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
            except json.JSONDecodeError:
                existingData = []
    else:
        existingData = []

    existingData.append(newExpense)

    with open(incomeRecordPath, 'w') as file:
        json.dump(existingData, file, indent=4)

    print(f"Added Income: {desc}, Amount: {amount}\n")

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

def showIncome(incomeRecordPath):
    print("Income : ")

    existingData = []

    if os.path.exists(incomeRecordPath):
        with open(incomeRecordPath, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
            except json.JSONDecodeError:
                existingData = []
    else:
        existingData = []
    
    for expense in existingData:
        print(f" - {expense['description']} : {expense['amount']}")
    print(f"\nTotal Income : {getTotalIncome(incomeRecordPath)}\n")

def getTotalIncome(incomeRecordPath):
    sum = 0
    existingData = []

    if os.path.exists(incomeRecordPath):
        with open(incomeRecordPath, 'r') as file:
            try:
                existingData = json.load(file)
                if not isinstance(existingData, list):
                    existingData = []
            except json.JSONDecodeError:
                existingData = []
    else:
        existingData = []

    for expense in existingData:
        sum += expense['amount']
    return sum

def showExpense(expenseRecordPath):
    print("Expense : ")

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
    
    for expense in existingData:
        print(f" - {expense['description']} : {expense['amount']}")
    print(f"\nTotal Expense : {getTotalExpense(expenseRecordPath)}\n")

def getTotalExpense(expenseRecordPath):
    sum = 0
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

    for expense in existingData:
        sum += expense['amount']
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
    incomeRecordPath = 'income.json'
    expenseRecordPath = 'expenses.json'
    initial_budget = loadBurgetData(filepath)
    expenses = []

    while True:
        try:
            print("What would you like to do ?")
            print("1) Add Income")
            print("2) Add an Expense")
            print("3) Show Income details")
            print("4) Show Expense details")
            print("5) Exit\n")
            choice = int(input("Enter Your choice (1/2/3) : "))
            if(choice == 1):
                desc = input("\nEnter Income description : ")
                amount = float(input("Enter Income amount : "))
                addIncome(desc, amount, incomeRecordPath)
                continue
            elif(choice == 2):
                desc = input("\nEnter expense description : ")
                amount = float(input("Enter expense amount : "))
                addExpense(expenses, desc, amount, expenseRecordPath)
                continue
            elif(choice == 3):
                showIncome(incomeRecordPath)
                continue
            elif(choice == 4):
                showExpense(expenseRecordPath)
                continue
            elif(choice == 5):
                print("3 Exit" )
            else:
                print(f"Invalid input... Please enter a valid number.")
        except ValueError:
            print(f"Invalid input... Please enter a valid number.")

main()