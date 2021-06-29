def calculation(num1,num2):
    addition = num1+num2
    difference = num1-num2
    return [addition,difference]

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lst = calculation(num1,num2)
print("Addtion is: ",lst[0],"Subtraction is: ",lst[1])