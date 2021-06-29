def showEmployee(name,salary=9000):
    print("Employee name is: ",name," and salary is: ",salary)

name = input("Enter employee's name: ")
salary = int(input("Enter salary: "))
showEmployee(name,salary)
showEmployee(name)