# list comprehension (we can create a list in one line)
# creating a list of squares
# normal
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)
# by list comprehension
squares1 = [i**2 for i in range(1,11)]
print(squares1)

# list of negative numbers
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

negative1 = [-i for i in range(1,11)]
print(negative1)

# separate first letter of names
names = ['divya','karan', 'rahul']
name = []
for i in names:
    name.append(i[0])
print(name)

name = [i[0] for i in names]
print(name)

# rev of string inside the list
name1 = ['abc', 'def', 'ghi']
def func(l):
    return [i[::-1] for i in l]
print(func(name1))

# list comprehension with if statement
nums = list(range(1,11))
# even = []
# for i in nums:
#     if i%2 == 0:
#         even.append(i)
# print(even)

even = [i for i in nums if i%2 == 0]
print(even)
even1 = [i for i in range(1,11) if i%2 == 0]
odd1 = [i for i in range(11,21) if i%2 != 0]
print(even1)
print(odd1)

# convering all the datatypes of list into string
def strs(l):
    new = []
    for i in l:
        if type(i) != str:
            new.append(str(i))
        else:
            new.append(i)
    return new
lst = [1,'divi',1.2,[2,3.4,'abc'],(2,4,5)]
print(strs(lst))

# it will return only int or float by converting them into string and ignore other datatype
def str2(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]
lst2 = [1,1.3,4,'abc']
print(str2(lst2))

# list comprehension with if-else
# negative of odd and twice of even numbers
num = [1,2,3,4,5,6,7,8,9,10]
new1 = []
for i in num:
    if i%2 == 0:
        new1.append(i*2)
    else:
        new1.append(-i)
print(new1)

new2 = [i*2 if (i%2 == 0) else -i for i in num]
print(new2)

# nested list comprehension
# eg. = [[1,2,3],[1,2,3],[1,2,3]]
l1 = []
for i in range(3):
    l1.append([1,2,3])
print(l1)
nest = [[i for i in range(1,4)] for j in range(1,4)]
print(nest)

# dictionary comprehension
square = {num: num**2 for num in range(1,11)}
print(square)
# or
sqr =  {f"square of {num} is" : num**2 for num in range(1,11)}
print(sqr)
for k,v in sqr.items():
    print(f"{k} : {v}")

# to count no. of character in string by dict comprehension
string = "divya"
word = {c: string.count(c) for c in string}
print(word)

# dict comprehension with if else
# d = {1: 'odd', 2: 'even'...}
d = {i:('odd' if i%2 != 0 else 'even') for i in range(1,11)}
print(d)

# sets comprehension
s = {k**2 for k in range(1,11)}
print(s)

names = ['divi','karan','rahul']
first = {name[0] for name in names}
print(first)