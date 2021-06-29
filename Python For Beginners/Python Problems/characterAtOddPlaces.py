str1 = input("Enter a string: ")
for i in range(len(str1)):
    if(i%2==0):
        print(str(str1[i]),",",end=" ")
