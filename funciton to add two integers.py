def add():
    n1=int(input("enter first integer:"))
    n2=int(input("enter second integer:"))
    total=n1+n2
    print ("total of given integers=",total)
   
   
while True:
        add()
        choice=input("do you want to take new integers (Y/N):")
        if choice.lower() != "y":
            break