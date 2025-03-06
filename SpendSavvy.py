def addExpense(expenses, desc, amount):
    expenses.append({"description": desc, "amont":amount})
    print(f"Added expenses: {desc}, Amount {amount}")

def showExpense(expenses):
    print("Expense : ")
    for expense in expenses:
        print(f" - {expense['description']} : {expense['amont']}")
    print(f"\nTotal Expense : {getTotalExpense(expenses)}")

def getTotalExpense(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amont']
    return 

def main():
    print("Welcome to Budget app")
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
                    addExpense(expenses, desc,amount)
                elif(choice == 2):
                    showExpense(expenses)
                elif(choice == 3):
                    print("3) Exit")
                else:
                    print(f"Invalid input... Please enter a valid number.")
            except ValueError:
                print(f"Invalid input... Please enter a valid number.")

main()