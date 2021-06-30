print("hello \"world\" world")
print('hello "world"')
# \\ for backslash
# \t for tab
#\b for backspace
#\\\\ for double backslash
print("name\tgunjan")
print("name \\")
print("hell\bo")
# for output : LineA \n LineB OR lineA \t lineB
print("lineA \\n lineB")
# ouput: \" \'
print("\\\" \\\'")
# output:this is \\ double backslash
# this is /\/\/\/\/\ mountain
# he is     awesome(use escape sequence)
# \" \n \t \' 
print("this is \\\\ double backslash")
print("this is /\\/\\/\\/\\ mountain")
print("Divya is \t awesome")
print("\\\" \\n \\t \\\'")
# shortcut
# to use any escape sequence as normal text we can use r
print(r"lineA \n lineB")
# for printing emojis
# print("\unicode od emoji and + removed with 000")
print("\U0001F609")
# / float division
# // integer division
# ** exponent
print(2/4)
print(4/2)
print(4//2)
print(2//4)
# for square root
print(2**0.5)
print(round(2**0.5,4))

def sum(a,b):
    return a+b
print(sum(10,23))

print(2**3/2*6-4*(3.4/2))
# associativity of exponent is right to left
print(2**3**2)
name = "Divya"
print(name)
name = 123
print(name)
# only _ can be used in python variable name
# file_name_1 snake case naming mainly used in python

# strings
first_name = "Divya"
last_name = " Kapoor"
full_name = first_name + last_name
print(full_name)
print(first_name + "3")
print(first_name + str(3))
print(first_name*3)

# user input
name = input("enter your name: ")
print("hello! " + name)
age = input("enter your age: ")
# age is already a string as input is always string but we can still use str function with no error
print("your age is " + str(age))
print(age)

num1 = input("enter fisrt num: ")
num2 = input("enter second num: ")
total = num1 + num2
print(total)
total1 = int(num1) + int(num2)
print("total is " + str(total1))
# int and float can be added but output will be a float
# assign more than one values in their variables in a line
name, age = "Divya" , 16
print("hello " + name + "." + "Your age is " + str(age))
x=y=z=1
print(x+y+z)

# two or more input in one line
# but there should be (default) space between two input while running
# name, age = input("enter your name and age").split()
# to saperate with comma while running
name, age = input("enter your name and age").split(",")
print(name)
print(age)
# print("hello " + name + "." + "Your age is " + str(age)) ugly syntax
# so we use string formatting which is of 3 types python2,python3,python 3.6
# python3 no need to convert int into string
print("hello {} your age is {} ".format(name, age))
# python3.6
print(f"hello {name} your age is {age}")
print(f"hello {name} your age is {int(age) + 3}")

# exercise
num1, num2, num3 = input("enter num1,num2 and num3: ").split()
total = int(num1) + int(num2) + int(num3)
avg= total/3
print(f"average of three numbers is {avg}")
# or
print(f"average is : {(int(num1) + int(num2) + int(num3))/3}")

# string indexing
language = "python"
print(language[3])
print(language[-1])
# slicing/selecting sub sequence
print(language[2:5])
print(language[-3:6])
print(language[:])
print(language[1:])
print(language[:5])
# important
print("Divya"[1:5])
# step argument
print("Divya"[0:5:2])
print("Gunjan"[0::3])
# for reverse 
print("Divya"[5::-1])
# or
print("Divya"[::-1])

# exercise
name = input("enter your name: ")
print(f"name in reverse order is {name[-1::-1]}")

# string methods
name = "DiVya KaPoor"
# len is a function
print(len(name))
# lower and upper are methods
print(name.lower())
print(name.upper())
# tile method one capatalise first letter of name and sirname
print(name.title())
# count method count the times of character in string
print(name.count("a"))

# exercise
name, char = input("enter your name and a character to count it's occuring: ").split(",")
# character = char.lower()
# count = name.lower().count(character)
print(f"length of your name is {len(name)} \nthe number of character {char} is {name.lower().count(char.lower())}")
# in above exercise while running if we write divya, a than count of a will ne 0 due to space before a  so strip method is used

# strip method
name = "   Divy  a    "
dots = "...."
print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
# but ir does not remove between spaces
# for that use replace
print(name.replace(" ",""))

name, char = input("enter your name and a character to count it's occuring: ").split(",")
print(f"length of your name is {len(name)} \nthe number of character {char} is {name.strip().lower().count(char.strip().lower())}")

# replace() and find() method
string = "she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was",1))
print(string.replace("is","was",2))

print(string.find("is"))
# find is after 4th position
print(string.find("is",5))
# if we don't know the position of second is
is_pos = string.find("is")
is_pos2 = string.find("is",is_pos + 1)
print(is_pos2)

# center method
# to add space/characters on left and right side
name = "Divya"
# to add 2 stars on both sides
print(name.center(9,"*"))
# if we write 6 instead of 9 then a star will print on right side
# to print 4 stars on both side of user input name
name = input("enter your name: ")
print(name.center(len(name) + 8, "*"))

# strings are immutable
string = "string"
print(string[1])
# string[1]='u' is not allowed
# string.replace('t','T') is allowed and can be stored in new variable but original string remains unchanged

# we can change variable but string cannot be changed by methods
name = "div"
name += "ya"
print(name)
age = 16
age += 1
print(age)