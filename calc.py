def calc():
    # Take input from the user
    #choice = input("Enter choice(1/2/3/4/5):")


    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if choice == '1':
       print(x,"+",y,"=", x + y)

    elif choice == '2':
       print(x,"-",y,"=", x-y)

    elif choice == '3':
       print(x,"*",y,"=", x*y)

    elif choice == '4':
       print(x,"/",y,"=", x/y)

    # elif choice == '5':
    #    print("Exiting")


    else:
       print("Invalid input")

    operations()


def operations():
    print("\n")
    print("----------------------------------")
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.EXIT")
    global choice
    choice = input("Enter choice(1/2/3/4/5):")
    if choice == '5':
        print("Exiting")
    else:
        calc()

    x = False
    if choice != '5':
        x = True
    while x:
        operations()
    else:
        return

operations()
