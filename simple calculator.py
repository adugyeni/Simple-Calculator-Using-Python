# A SIMPLE CALCULATOR

def Addition(a, b):
    return (a + b)
def Subtraction(a, b):
    return(a - b)
def Multiplication(a, b):
    return (a * b)
def Division(a, b):
    if b != 0:
        return(a/b)
    else:
        return("Oops!!! 🫠: Division by zero! Error")

while True:
    print("Welcome, This is Benjamin's Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    arithmetic_choice = input("Enter any operation(1-5): ")

    if arithmetic_choice in ["1", "2", "3", "4"]:
        value = input("Enter two separated values(a, b): ").split()
        a, b = map(float, value)
    
        if arithmetic_choice == "1":
            print(f"{a} + {b} = {Addition(a, b)}")
        elif arithmetic_choice == "2":
            print(f"{a} - {b} = {Subtraction(a, b)}")
        elif arithmetic_choice == "3":
            print(f"{a} * {b} = {Multiplication(a, b)}")
        elif arithmetic_choice == "4":
            print(f"{a} / {b} = {Division(a, b)}")

        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again == 'yes':
            continue
        else:
            print("Thank you for using my simple calculator! Goodbye👋.")
            break

    elif arithmetic_choice == "5":
        print("Goodbye👋")
        break

    else:
        print("Oops!Incorrect input 🤔. Please choose from the Calculator menu")




    

