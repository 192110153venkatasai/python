str=input("Please enter a string: ")
upper, lower, num, special=0,0,0,0;
for i in range(len(str)):
  if(str[i]>='A' and str[i]<='Z'):
     upper+=1
  elif(str[i]>='a' and str[i]<='z'):
     lower+=1
  elif(str[i]>='1' and str[i]<='9'):
      num+=1
  else:
      special+=1
print("Upper case letters: ",upper)
print("\nLower case letters: ",lower)
print("\nnumbers: ",num)
print("\nSpecial characters: ",special)
