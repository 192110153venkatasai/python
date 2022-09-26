try:
    a=int(input("enter a year"))
    if(a%4==0):
        print(a+4)
    elif(a==0):
        print("it is a leap year:")
    elif(a<0):
        print("it is leap year")
    else:
        b=a%4
        c=a-b
        print(c)
except ValueError:
    print("invalid input")
