def count(str2):
    lower,upper = (0,0)
    for i in range(len(str2)):
        if(str2[i].islower()):
            lower += 1
        elif(str2[i].isupper()):
            upper += 1
    return [lower,upper]

str2 = input("Enter a string: ")
cnt = count(str2)       
print("Count of lower case letters: ",cnt[0])
print("Count of upper case letters: ",cnt[1])
