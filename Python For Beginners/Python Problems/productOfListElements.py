def mul(lst):
    multiply=1
    for i in range(len(lst)):
        multiply *= lst[i]
    return multiply

lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    element = int(input())  
    lst.append(element)
print("Multiply af all items is: ",mul(lst))