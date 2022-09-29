m=int(input("enter the starting number range"))
n=int(input("enter the ending number range"))
k=int(input("enter the range of the number to be skipped"))
if(m>n or m<0 or n<0 or k<0 or m==n):
   print("invalid input")
else:
      for i in range(m,n+1,k+1):
         print(i)
