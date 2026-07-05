balance = 10000
pin = "1234"

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance is:", balance)

        elif choice == "2":
            amount = float(input("Enter Deposit Amount: "))
            balance += amount
            print("Amount Deposited Successfully.")
            print("Current Balance:", balance)

        elif choice == "3":
            amount = float(input("Enter Withdraw Amount: "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Current Balance:", balance)
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")
