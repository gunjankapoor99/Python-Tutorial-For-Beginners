# tuples are data structures can store any data type are faster than list
# tuples are  immutable used when data is not going to change
# eg = ('one', 'two', 'three')
# count, index, len, slicing can be used with tuple

# loops with tuple
mixed = (1,2,3,4,5)
for i in mixed:
    print(i)
print(len(mixed))
# tuple with one element
# written below is int
nums = (1)
# it is string
words = ('words')
print(type(nums))
print(type(words))
# , is required to create one element tuple
num = (1,)
print(type(num))
# this is also tuple below
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))

# tuple unpacking (variables must be equal to elements)
colors = ('blue', 'black', 'purple')
color1, color2, color3 = (colors)
print(color2)

# list inside tuple (we can use pop, append etc with list inside tuple also)
favorites = ('south magnolia', ['tokyo', 'landscape'])
favorites[1].pop()
favorites[1].append('yoyo')
print(favorites)

# functions that can be used with tuple (min, max, sum)
print(min(mixed))
print(sum(mixed))

# function returning two values
# when two values are returned it give tuple
def func(int1,int2):
    add = int1 + int2
    mul = int1 * int2
    return add, mul
print(func(2,4))
# to get separate values store them in variables
add1, mul1 = func(2,4)
print(add1)
print(mul1)

# more on tuple, list and str
num1 = tuple(range(1,11))
print(num1)
# convert tuple into list
num2 = list((1,2,3,4,5))
print(num2)
# convert tuple into string
num3 = str((1,2,3,4))
print(num3)
print(type(num3))
# convert list into string
num_list = str([1,2,3,4,5])
print(num_list)
print(type(num_list))

# dictionaries unordered collection of data in key : value pair. Inside dictionary we can have string , list , number, other dictionary
user = {'name' : 'Divya', 'age' : 16}
print(user)
print(type(user))
# other method to create dictionary , keys without ''
user1 = dict(name = 'Divya', age =16)
print(user1)

# accessing data in dictionaries (there are no indexing in dictionaries), write keys to access data in square braces and quotes
print(user['name'])
print(user['age'])

user_info = {
    'name' : 'divya',
    'age' : 16,
    'fav_movies' : ['abc', 'def', 'ghi'],
    'fav_tunes' : ['jkl', 'mno', 'pqr']
}
print(user_info)
print(user_info['fav_movies'])

# dictionary inside dictionary
# users = {
#     user1 :  {
#         'name' : 'divya',
#     'age' : 16,
#     },
#     'user2' : 5,
#     'user3' : 'six'
# }
# print(users)

# add data inside an empty dictionary
user2 = {}
user2['name'] = 'divya'
user2['age'] = 16
print(user2)

# in keyword (used only with keys)
if 'name' in user_info:
    print('present')

# for values
if 'divya' in user_info.values():
    print('present')
else:
    print('not present')
# for list
if ['abc', 'def', 'ghi'] in user_info.values():
    print('present')
else:
    print('not present')

# loops in dictionaries
# for keys
for i in user_info:
    print(i)
# for values
for i in user_info.values():
    print(i)
# or
for i in user_info:
    print(user_info[i])

# values method (in form of list)
user_values = user_info.values()
print(user_values)
print(type(user_values))

# keys method (in form of list)
user_keys = user_info.keys()
print(user_keys)
print(type(user_keys))

# items method(important) give key , value in tuple
dict_items = user_info.items()
print(dict_items)
print(type(dict_items))

for key, value in user_info.items():
    print(f"key is {key} value is {value}")

# add and delete data from dictionary
user_info['fav_songs'] = ['song1', 'song2']
print(user_info)

# pop metthod
# error if no argument in pop
pop_item = user_info.pop('fav_tunes')
print(f"pop item value is {pop_item}")
print(user_info)
print(type(pop_item))

# popitem for deleting any random key value pair
pop1 = user_info.popitem()
print(user_info)
print(pop1)
print(type(pop1))

# update method
# if both dict have same key than it get updated
user_info = {
    'name' : 'divya',
    'age' : 16,
    'fav_movies' : ['abc', 'def', 'ghi'],
    'fav_tunes' : ['jkl', 'mno', 'pqr']
}
more_info = {'name': 'divya kapoor', 'state' : 'up', 'hobbies' : ['coding','reading','dancing']}
user_info.update(more_info)
print(user_info)
# updating new empty dictionary has no impact
user_info.update({})
print(user_info)

# fromkeys method
# when we need same values for more than one key
d = dict.fromkeys(['name','age','heigth'], 'unknown')
print(d)
d1 = dict.fromkeys(('name', 'age', 'height'), 'unknown')
print(d1)
d2 = dict.fromkeys("abc", 'unknown')
print(d2)
d3 = dict.fromkeys(range(1,11), 'unknown')
print(d3)
d4 = dict.fromkeys(['name','age'], ['unknown', 'unknown'])
print(d4)

# get method
d = {'name' : 'unknown', 'age' : 'unknown'}
print(d['name'])
# but names give error to handle these errors we use get method which give none if key is not present
print(d.get('name'))
print(d.get('names'))

# if 'name' in d: and if d.get('name'): are same as None is evaluated as False

# clear method
d.clear()
print(d)

# copy method
d = {'name' : 'unknown', 'age' : 'unknown'}
# di and d are different dictionaries
d1 = d.copy()
print(d1)
d1.popitem()
print(d1)
print(d)
print(d1 is d)
# if we write d1 = d then they are same dictionary

# more on get method 
# we can overwrite None in get method if a key is not found
user = {'name' : 'divya', 'age' : 16}
print(user.get('names', 'not found'))

# more than one same key is present second one will overright
user = {'name' : 'divya', 'age': 16, 'age': 15}
print(user)

def cube(num):
    dict1 = {}
    for i in range(1,num+1):
        dict1[i] = i*i*i
    return dict1
print(cube(8))

# word counter
# in dictionary if alphabet occurs again in a name then it overwrites previous so no need to check if alphabet is already present or not
def word(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word('divya khurana'))

# exercise
user = {}
name = input("name")
age = input('age')
fav = input("fav movies separated by commas").split(',')
fav_songs = input('fav songs').split(',')
user['name'] = name
user['age'] = age
user['fav_movies'] = fav
user['fav_songs'] = fav_songs
print(user)
for key,value in user.items():
    print(f'{key} : {value}')