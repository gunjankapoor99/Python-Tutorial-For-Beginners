# functions
def add(a, b):
    return a+b

a= int(input("enter a number: "))
b= int(input("enter a number: "))
print(add(a,b))

name1= input("enter first name: ")
name2= input("enter last name: ")
print(add(name1,name2))

# return and print
def add(a,b):
    print(a+b)
add(4,5)

# last character of name
def last_char(name):
    return name[len(name)-1]
name = input("enter your name")
print(last_char(name))

# odd or even
# def odd_even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"

def odd_even(num):
      if num%2==0:
          return "even"
      return "odd"
num = int(input("enter a number: "))
print(odd_even(num))

# or
def is_even(num):
    if num%2==0:
        return True
    return False
print(is_even(9))

# or
def is_even(num):
    return num%2==0
print(is_even(12))
# above num is parameter and 12 is argument

def song():
    return "abc song"
print(song())

# exercise
def greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
num1 = int(input("enter first num: "))
num2 = int(input("enter second num: "))
print(greater(num1,num2))

def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(greatest(4,6,2))

# function inside function
def new_greatest(num1,num2,num3):
    # bigger = greater(a,b)
    # return greater(bigger,c)
    return greater(greater(num1,num2),num3)
print(new_greatest(12,32,35))

# exercise
# palindrome number
def is_palindrome(text):
    reverse = text[::-1]
    if text == reverse:
        return True
    else:
        return False
print(is_palindrome("noon"))

# or
# def is_palindrome(word):
#    return word == word[::-1]

# default parameter
# here age is default parameter
# if we write age while calling it will overwrrite the parameter
# default parameter can be made only at last not middle
# we can also write age = None
def user(first_name, last_name, age=16):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
user("Divya", "Kapoor")

# scope of variable
# it will give error
# def func():
#     x=7
#     return x
# def func2():
#     print(x)
# func2()

# below x=5 is global and x inside func is different to use same x we use keyword global
x=5
def func():
    x=7
    return x
print(func())
print(x)

# fisrt x=5 then function call then x become 7
x=5
def func():
    global x
    x=7
    return x
print(x)
print(func())
print(x)

# fibonacci series

def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a, b, end = " ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b , end = " ")
print(fibonacci(6))