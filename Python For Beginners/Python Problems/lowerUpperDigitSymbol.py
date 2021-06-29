str2 = input("Enter a string: ")
lower,upper,digit,specialSymbol = (0,0,0,0)
for i in range(len(str2)):
    if(str2[i].islower()):
        lower += 1
    elif(str2[i].isupper()):
        upper += 1
    elif(str2[i].isdigit()):
        digit += 1
    else:
        specialSymbol += 1
print("Count of lower case letters: ",lower)
print("Count of upper case letters: ",upper)
print("Count of digits: ",digit)
print("Count of special symbols: ",specialSymbol)