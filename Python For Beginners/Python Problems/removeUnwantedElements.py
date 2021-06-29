list1 = []   
num = int(input("Enter number of elements: "))  
for i in range(1, num + 1):  
    ele = int(input("Enter elements: "))  
    list1.append(ele)  
print("Elements in the list are as follows: ", list1)
unwanted = []
x = int(input("Enter numbers of elements: "))  
for i in range(1, x + 1): 
    item = int(input("Enter elements: "))  
    unwanted.append(item)  
for ele in list1:  
    if ele in unwanted:  
        list1.remove(ele)    
print("New list after removing unwanted elements: ", list1) 