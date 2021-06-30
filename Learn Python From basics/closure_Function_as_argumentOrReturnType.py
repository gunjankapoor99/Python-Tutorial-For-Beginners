# we can indicate a function by variable(of same memory location)
def square(a):
    return a**2
s= square
print(s(7))
print(s.__name__)
print(square.__name__)
print(s)
print(square)

# function as an argument
l = [1,2,3,4]
def my_map(func, l):
    new = []
    for item in l:
        new.append(func(item))
    return new
print(my_map(square, l))
print(my_map(lambda a: a**3, l))

# or
def my_map2(func, l):
    return [func(item) for item in l]
print(my_map2(square, l))

# function returning function(closure)
def outer_func():
    def inner():
        print("inside function")
    return inner
    # or
    # return inner()         
var = outer_func()
var()
# or outer_func()

def outer2(msg):
    def inner2():
        print(f"message is {msg}")
    return inner2
var = outer2("hello!")
var()

def to_power(x):
    def call_power(n):
        return n**x
    return call_power
cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))