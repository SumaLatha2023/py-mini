print("*****SIMPLE CALCULATOR*****")
print()
print("Select the operation to be performed :")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

while(True):
    print()
    choice = int(input("Enter choice from 1 to 4 : "))

    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    if(choice == 1):
        print(f"Result of {a} + {b} = {a+b}")
    elif(choice == 2):
        print(f"Result of {a} - {b} = {a-b}")
    elif(choice == 3):
        print(f"Result of {a} x {b} = {a*b}")
    elif(choice == 4):
        print(f"Result of {a} / {b} = {a/b}")
    else:
        print("Wrong Choice")
        continue

    click = (input("Enter 'ac' to end or 'go' to continue : "))
    if(click == 'ac'):
        break
    elif(click == 'go'):
        continue
    else:
        print("Wrong entry")






