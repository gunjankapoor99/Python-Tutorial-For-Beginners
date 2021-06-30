import random

age = int(input("enter your age: "))
if age >= 14:
    print("you are above 14")

# pass statement
x=12
if(x>12):
    pass
  
# if-else
age = int(input("enter your age: "))
if age >= 14:
    print("you are above 14")
else:
    print("you can't play")

# exercise
win_num = 8
user_num = int(input("guess a number: "))
if user_num == win_num:
    print("you win!")
else:
    if(user_num < win_num):
        print("number is too low")
    else:
        print("number is too high")

# check two condition at same time
# and, or
name = 'abc'
age = 14
if name == 'abc' and age == 12:
    print("true")
else:
    print("false")
# similarly or

# exercise
name, age = input("enter your name and age: ").split(",")
# we can also use lower method
if int(age) > 10 and (name[0]=='a' or name[0]=='A'):
    print("you can watch coco")
else:
    print("you can not watch coco")

# if elif else statement
age = int(input("enter your age"))

if age==0 and age<0:
    print("you can't watch")
elif  age>0 and age<=3:
    print("ticket price is free")
elif  age>3 and age<=10:
    print("ticket price is 150")
elif  age>10 and age<=60:
    print("ticket price is 250")
else:
    print("ticket price is 200")

# in keyword
# if with in
name = "Divya"
# in place of name(variable) we can also use string
if 'a' in name:
    print("a is present in name")
else:
    print("not present")

# check empty or not
name = input("enter your name")
# it checks whether name is empty or not
if name:
    print("string is not empty")
else:
    print("string is empty")

# loops
i = 1
while i<=10:
    print("hello Divya!")
    i += 1

# exercise
total = 0
i = 1
while i<=10:
    total = total+i
    i += 1
print(f"total sum is {total}")

# exercise
total = 0
i = 1
n = int(input("enter a natural number: "))
while i<=n:
    total = total+i
    i += 1
print(f"total sum is {total}")

# exercise
# to print sum of digits of a number
num = input("enter a number of more than 1 digit: ")
sum = 0
digit = len(num)-1
while digit>=0:
    sum += int(num[digit])
    digit -= 1
print(sum)

# exercise
# count the occurance of an alphabet in name
name = input("enter your full name: ")
# name.coount("d"), name.count(name[0]) = 1
# name.count("a"), name.count(name[1])= 2
# output
# d : 1

i = 0
while i<len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1
# but it repeats the output of same alphabet
name = input("enter your full name: ")
i = 0
temp_var = ""
while i<len(name):
    if name[i] not in temp_var:
         temp_var += name[i]
         print(f"{name[i]} : {name.count(name[i])}")
    i += 1

#infinite loop
# i=0
# while i<= 10:
#     print("hello world")
# control + c to stop infinite loop
# intentional infinite loop
# while True:
#     print("hello world")      

# for loop
# i = 0 to 9
for i in range(10):
    print(f"hello world {i}")

for i in range(1,11):
    print(i)

sum = 0        
for i in range(1,11):
    sum += i
print(sum)

# exercise
sum = 0
num = input("enter a number: ")
for i in range(0, len(num)):
    sum += int(num[i])
print(sum)

# exercise
name = input("enter your name: ")
temp_var = ""
for i in range(0, len(name)):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")

# break and continue keywards
for i in range(0,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)

# modified guessing game
win_num = random.randint(1,100)
guess = 1
user_num = int(input("guess a number: "))
game_over = False
while not game_over:
    if user_num == win_num:
        print(f"you win, and you guess this num in {guess} times")
        game_over = True
    else:
        if user_num < win_num:
            print("too low")
            guess += 1
            user_num = int(input("guess again"))
        else: 
            print("too high")
            guess += 1
            user_num = int(input("guess again"))

# DRY(don't repeat yourself) principle of coading
# while True:
#     user_num = int(input("guess a number: "))
#     if user_num == win_num:
#         print(f"you win, and you guess this num in {guess} times")
#         break
#     else:
#         if user_num < win_num:
#             print("too low")
#         else: 
#             print("too high")
#     guess += 1
#     continue


# step argument in range function
for i in range(1,11,2):
    print(i)
# output 10,9,8
for i in range(10,0,-1):
    print(i)

for i in range(1,-11,-1):
    print(i)

# for loop with string
# used in any language
name = "divya"
for i in range(len(name)):
    print(name[i])
# only in python
name = "divya"
for i in name:
    print(i)
for i in "divya":
    print(i)

num = input("enter a number: ")
sum = 0
for i in num:
    sum += int(i)
print(total)
