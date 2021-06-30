# set(data type) unordered collection(no indexing) of unique items(one item single time)
# we cannot store list,dict or tuple in sets
s = {1,2,3,1.1,4,1.0,3}
# 1 and 1.0 are same
print(s)
# to convert list into set and remove duplicate item
l = [1,2,3,2,4,5,4,5,6,7]
s1 = set(l)
print(s1)
# to convert set into list
s2 = list(s1)
print(s2)
# or
# s2 = list(set(s1)) if s1 is a list

# some methods with sets
s.add(5)
print(s)
# below if 3 not in set we get error
s.remove(3)
print(s)
# for error handling use discard
s.discard(6)
print(s)
# copy method
s3 = s.copy
print(s3)
# clear method
s.clear()
print(s)

# in keyword in set
s = {'a', 'b', 'c'}
if 'a' in s:
    print('present')
else:
    print('not present')

# for loop in set(unordered elements are printed)
for item in s:
    print(item)

# union and intersection
s1 = {1,2,3,4}
s2 = {3,4,5,6}
union_set = s1|s2
print(union_set)
intersetion_set = s1 & s2
print(intersetion_set)