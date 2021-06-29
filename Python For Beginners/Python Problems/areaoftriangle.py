side1 = int(input("Enter first side of triangle: ")) 
side2 = int(input("Enter second side of triangle: ")) 
side3 = int(input("Enter third side of triangle: ")) 
s = (side1+side2+side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
print("The area of triangle is: %0.2f" %area)