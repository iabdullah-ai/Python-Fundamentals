def calculator():
    print("-"*50)
    print("CALCULATOR")
    print("-"*50)
    a=int(input("enter first number:\n"))
    b=int(input("enter second number:\n"))
    c=int(input('''enetr a vaid operation\n
                \n1-addition \n 2-substraction \n 3- multiplication \n 4- division\n'''))
    if(c==1):
        print(a+b)
    elif(c==2):
        print(a-b)
    elif(c==3):
        print(a*b)
    elif(c==4):
        print(a/b)
    else:print("enter a valid operation")
calculator()
input("\nPress Enter to exit...")

        
