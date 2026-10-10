# CREATE A CALCULATOR
#Pralay Mahala
while True:

    print("\n===============================================")
    print("                  Calculator")
    print("===============================================")

    print("Do you want to add? Press = 1")
    print("Do you want to subtract? Press = 2")
    print("Do you want to multiply? Press = 3")
    print("Do you want to divide? Press = 4")

    num = int(input("Enter any one Number (1, 2, 3, 4): "))
    print("\n")

    if(num == 1):
        a = float(input("Enter your First Number: "))
        b = float(input("Enter your Second Number: "))
        c = a + b
        print(" ", a, "+", b, "=", " ", c)

    elif(num == 2):
        a = float(input("Enter your First Number: "))
        b = float(input("Enter your Second Number: "))
        c = a - b
        print(" ", a, "-", b, "=", " ", c)

    elif(num == 3):
        a = float(input("Enter your First Number: "))
        b = float(input("Enter your Second Number: "))
        c = a * b
        print(" ", a, "*", b, "=", " ", c)

    elif(num == 4):
        a = float(input("Enter your First Number: "))
        b = float(input("Enter your Second Number: "))

        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            c = a / b
            print(" ", a, "/", b, "=", " ", c)

    else:
        print("You entered a wrong number")

    while True:
        again = input("\nDo you want to calculate again? (Y/Yes or N/No): ")

        if again.lower() in ["y", "yes"]:
            break

        elif again.lower() in ["n", "no"]:
            print("\n===============================================")
            print("Thank you for using my Calculator!")
            print("This is my Calculator, made by Pralay Mahala.")
            print("===============================================")

            input("\nDo you want to exit? Press Enter to exit: ")
            exit()

        else:
            print("Please enter Y/Yes or N/No.")

print("\n===============================================")
print("             Made by Pralay Mahala")
print("===============================================")
