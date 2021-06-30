# list
numbers = [1, 2, 3, 4]
print(numbers)
mixed = [1, 2, 3, 4, "five", "six", 2.3, None]
print(mixed)
print(mixed[2])
print(mixed[:4])
mixed[1] = "two"
print(mixed)
mixed[2:] = ["three", "four"]
print(mixed)

# adding items to the list
fruits = ["grapes", "apple"]
fruits.append("mango")
print(fruits)

# more methods to add item
fruits1 = ["mango", "apple"]
fruits1.insert(1, "grapes")
print(fruits1)
fruits2 = ['grapes', 'apple']
fruits3 = fruits1+fruits2
print(fruits3)
fruits1.extend(fruits2)
print(fruits1)

# appending a list inside list
fruits1.append(fruits2)
print(fruits1)
# if we append a list inside a list it will appears in the form of list but on extend an list in a list it appears as different elements in that list

# deleting data from list
fruit = ['orange', 'apple', 'pear', 'banana', 'kiwi']
# pop method
# used to delete last element
fruit.pop()
print(fruit)
# if argument is passed than that element is deleted
fruit.pop(1)
print(fruit)

# del operator
del fruit[1]
print(fruit)
fruit.remove("banana")
print(fruit)
# if there are two same items then remove method remove the first item only

# to check if a element is present in the list or not use in keyword
fruit4 = ['banana', 'mango', 'apple']
if 'apple' in fruit4:
    print("apple is present")
else:
    print("not present")

# count method
print(fruit4.count('apple'))
# sort method can be used with string or numbers
# we can not directly print sorted list , so write in separate lines
fruit4.sort()
print(fruit4)

# sorted function used to sort list and print it but it does not actually sort the original list
number = [1, 4, 2, 8, 5]
print(sorted(number))
print(number)

# clear method
number.clear()
print(number)

# copy method
numbers = [4, 6, 2, 9, 5]
num2 = numbers.copy()
print(num2)

# is vs equals
# is check the same position in memory
fruit1 = ['orange', 'banana', 'apple']
fruit2 = ['banana', 'apple', 'kiwi']
fruit3 = ['orange', 'banana', 'apple']
print(fruit1 == fruit2)
print(fruit1 == fruit3)
print(fruit1 is fruit3)

# split method converts string to list
user_info = "Divya,16".split(",")
print(user_info)
name, age = "Divya,16".split(",")
print(name)
print(age)

# join method converts list to string
# both divya and 16 should be of same data type
user = ["divya", '16']
print(','.join(user))

# list and array
# array has same datatype values but list has more than one datatype
# python has a array module which store single data
# javascript array is similar to python list can store any datatype

# list and string
# list are mutable and string are immutable
# string can be mutable in other languages like RUBY

# loops inside list
# for loop
fruits4 = ['orange', 'apple', 'banana', 'kiwi']
for fruit in fruits4:
    print(fruit)

# while loop
i = 0
while i < len(fruits4):
    print(fruits4[i])
    i += 1

# list inside list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
for i in matrix:
    for j in i:
        print(j)

print(matrix[1][1])

# type function
s = 'string'
print(type(s))
print(type(matrix))

# more on list
# generate list with range functions
nums = list(range(1,11))
print(nums)

# pop method
# pop also return the last removed value
print(nums.pop())
print(nums)

# index method
nums1 = [1, 2, 3, 1]
print(nums1.index(1))
# 4 is the end index number
print(nums1.index(1,1,4))

# pass list into a function
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(nums1))

# exercise
nums2 = list(range(1,11))
def sqr(l):
    square = []
    # we can write nums2 below in place of l
    for i in l:
        square.append(i*i)
    return square
print(sqr(nums2))

# exercise
# def reverse_list(l):
#     l.reverse()
#     return l
# print(reverse_list(nums2))

# or
def rev(l):
    return l[::-1]
print(rev(nums2))

def reverse(l):
    emptylist = []
    for i in range(1,len(l) + 1):
        a = l.pop()
        emptylist.append(a)
    return emptylist
print(reverse(nums2))

# exercise
list1 = ['abc', 'tuv', 'xyz']
def rlist(l):
    empty = []
    for sub in l:
        empty.append(sub[::-1])
    return empty
print(rlist(list1))

# filter odd even exercise
lis = [1,2,3,4,5,6,7]
def oddeven(l):
    empty = []
    empty1 = []
    for num in l:
        if num % 2 == 0:
            empty.append(num)
        else:
            empty1.append(num)
    output = [empty, empty1]
    return output
print(oddeven(lis))

# common elements exercise
c1 = [1,3,4,7,2]
c2 = [3,6,8,5,2]
def common(l1, l2):
    empty = []
    for i in l1:
        if i in l2:
        # for j in l2:
        #     if i == j:
                empty.append(i)
    return empty
print(common(c1, c2))

# min and max fuction
b = [4,6,8]
print(min(b))
print(max(b))

def greatest_diff(l):
    return max(l) - min(l)
print(greatest_diff(b))

# no of list inside list exercise
c = [1,[4,5],3,[7,8],[4,9],6]
def no_of_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
print(no_of_list(c))