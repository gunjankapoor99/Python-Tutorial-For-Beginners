dict1 = {'num1':30,'num2':24,'num3':45,'num4':16}
print("Sorted dictionary by value is: ")
sorted_x = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
print(sorted_x)