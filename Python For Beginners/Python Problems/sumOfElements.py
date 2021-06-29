def sum(lst):
    add=0
    for i in range(len(lst)):
        add += lst[i]
    return add

lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    element = int(input())  
    lst.append(element)
print("Sum af all numbers is: ",sum(lst))