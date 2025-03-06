def main():
    print("Welcome to Budget app")

    while True:
        print("What would you like to do ?")
        print("1) Add an Expense")
        print("2) Show budget details")
        print("3) Exit\n")

        choice = int(input("Enter Your choice (1/2/3) : "))

        if(choice == 1):
            print("1) Add an Expense")
        elif(choice == 2):
            print("2) Show budget details")
        elif(choice == 3):
            print("3) Exit")
        else:
            print(f"Invalid input... Please enter a valid number.")


main()