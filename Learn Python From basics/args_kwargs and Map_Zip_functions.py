# make flexible functions
# * operator, *args
# below code will give erroe
def total(a, b):
    return a+b
# print(total(1,2,3))
# below * operator takes arguments in form of tuple 
def all_total(*args):
    print(args)
all_total(1,2,3,4,5)

def total1(*args):
    total = 0
    for num in args:
        total += num
    return total
print(total1(1,2,3,4))

# *args with normal parameter
# num can always written before *args
def multiply(num, *args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply
# here first 2 is not a part of *args
print(multiply(2,2,3))
# if only *args is the parameter than we can write print(multiply()) but when num and *args both are parameters then one argument must be passed

# args as a argument(while calling)
def mul(*args):
    mul = 1
    print(args)
    for i in args:
        mul *= i
    return mul
nums = [2,3,4]  # list or tuple
print(mul(nums))
print(mul(*nums))

# exercise
def lst(num , *args):
    # lst1 = []
    # for i in args:
    #     lst1.append(i**num)
    if args:
        return [i**num for i in args]
    else:
        return "no argument is passed"
    
num2 = [1,2,3,4]
print(lst(3,*num2))

# kwargs (keyword arguments) **kwargs(double star operator)
# kwargs as a parameter(output as dictionary)
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k} : {v}")
func(first_name = 'divya', last_name = 'kapoor')
# dictionary unpacking
d = {'name': 'div', 'age' : 24}
func(**d)

def func1(name, **kwargs):
    print(kwargs)
    print(name)
    for k,v in kwargs.items():
        print(f"{k} : {v}")
func1('divi',first_name = 'divya', last_name = 'kapoor')

# fuctions with all parameters
# padk (parameter,*args,default parameters,**kwargs)
def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('divya', 1, 2, 3, a= 1, b= 2)

# exercise
def rev(names,**kwargs):
    if kwargs.get('rev_str') == True:
        return [name[::-1].title() for name in names]
    else:
        return[name.title() for name in names]
print(rev(['divi','gunjan'], rev_str = True))

# lambda expression (anonymous function)
# lambda expression is used with built in functions like map,reduce,filter
add2 = lambda a,b : a+b
print(add2(3,4))
# these functions do not have names so while print(add2,variable name) we get lambda as output while in normal functions we get name of function
print(add2)

# odd even function
def even(a):
    return a%2 == 0
print(even(5))

iseven = lambda a : a%2 == 0
print(iseven(6))

last_char = lambda s : s[-1]
print(last_char("divya"))

# lambda function with if-else
func = lambda s : True if len(s) > 5 else False
print(func("abcde"))

# we use enumerate function with for loop to track position of out items 
# normal method
names = ['abc', 'abcde', 'abcdefg']
for name in names:
    pos = 0
    print(f"{pos} ---> {name}")
    pos += 1
# by enumerate function
for pos,name in enumerate(names):
    print(f"{pos} ---> {name}")

# exercise (finding index of string if present in the list)
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1
names = ['abc', 'divi', 'divya']
print(find_pos(names,'div'))

# map function
num1 = [1,2,3,4,5]
def sqr(a):
    return a**2
sqrs = list(map(sqr, num1))
print(sqrs)
# or
sqrs1 = list(map(lambda s: s**2, num1))
print(sqrs1)
# by list comprehension
square = [i**2 for i in num1]
print(square)

# we can iterate in map object
name1 = ['divi', 'divya', 'karan']
length = map(len,name1)
# loop will run only one time on map and filter function
for i in length:
    print(i)
for j in length:
    print(j)
lens = list(map(len, name1))
print(lens)

# filter function
numbers = [3,4,2,1,5,6,9,8]
def even(a):
    return a%2 == 0
evens = tuple(filter(even, numbers))
print(evens)
# or
even = tuple(filter(lambda a: a%2 == 0, numbers))
for i in even:
    print(i)
print(" ")

# iterator and iterables
# how loop works on list/tuple/string and map object
numbers = [1,2,3,4] # iterables
squares = map(lambda a:a**2, numbers) # iterator

for i in numbers:
    print(i)
print(" ")
# how for loop actually works(first it call iter function)(iter function convert list into iterator)
num2 = iter(numbers)
# then next function get called
print(next(num2))
print(next(num2))
print(next(num2))
print(next(num2))
print(iter(numbers))  # it is a object
# print(next(numbers)) will give error
# but we can do it directly with iterators
print(next(squares))
print(next(squares))
print(next(squares))

# zip function
user_id = ['user1', 'user2', 'user3']
names = ['harshit', 'mohit', 'rohit']
# ('user1', 'harshit'), ('user2', 'mohit')
# print(zip(user_id, names)) does not give anything
print(list(zip(user_id, names)))
print(dict(zip(user_id, names)))

# list having tuples and two values in each can be converted into dictionary directly
example = [('a',1), ('b',2)]
print(dict(example))

# zip can also work with more than two list
last_name = ['verma','sharma', 'singh']
print(list(zip(user_id, names, last_name)))

# * operator with zip (reverse of previous example)
l = [(1,2), (3,4), (5,6), (7,8)]
l1, l2 = list(zip(*l))
print(list(l1))
print(l2)

l1 = [1,3,5,7]
l2 = [2,4,6,8]
new = []
# check which corresponding number is bigger by zip
for pair in zip(l1,l2):
    new.append(max(pair))
print(new)

# exercise (return average of corresponding numbers of lists)
def average(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(average([1,2,3], [4,5,6], [7,8,9]))

# or
average1 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average1([1,2,3], [4,5,6], [7,8,9]))

# any(true), all(true) function
number1 = [2,4,6,8,10]
number2 = [1,2,3,5,4,6]

print(all([num%2 == 0 for num in number1]))
print(any([num%2 == 0 for num in number1]))

# exercise
def fun(*args):
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "wrong input"
print(fun(1,2,3,4,5,'divi'))

# advanced min() and max() function
def func2(item):
    return len(item)
names = ['harshit', 'mohit', 'ab']
print(max(names, key = func2))
# or
print(max(names, key= lambda item: len(item)))

student = [
    {'name': 'harshit', 'score': 90, 'age': 24},
    {'name': 'mohit', 'score': 60, 'age': 23},
    {'name': 'rohit', 'score': 70, 'age': 20},
]
print(max(student, key = lambda item:item.get('score')))
print(max(student, key = lambda item:item.get('score'))['name'])

student2 = {
    'harshit': {'score':70, 'age': 24},
    'mohit' : {'score':90, 'age': 20},
    'rohit' : {'score': 80, 'age': 25}
}
print(max(student2, key = lambda item: student2[item]['score']))

# advance sorted function
# we can sort list directly by list.sort() but we can't do it with tuple(same with sets)
fruit = ('grapes', 'apple', 'peach')
print(sorted(fruit))
print(fruit)

guitar = [
    {'model': 'yamaha', 'price': 8400},
    {'model': 'naptune', 'price': 50000},
    {'model': 'venus', 'price': 35000}
]

print(sorted(guitar, key = lambda d: d.get('price')))
print(sorted(guitar, key = lambda d: d.get('price'), reverse = True))

# doc strings(we can write and see doc strings)
def add(a,b):
    ''' this function takes 2 numbers and return their sum '''
    return a+b
print(add.__doc__)
print(len.__doc__)

# help function
print(help(sum))
print(help(sorted))