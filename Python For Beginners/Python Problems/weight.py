weight=input("weight: ")
unit=input("(L)bs or (K)bs: ")
if unit.lower()=='L':
    converted=int(weight)*0.45
    print(f"you are {converted} kilos")
else:
    converted=int(weight)/0.45
    print(f"you are {converted} pounds")
