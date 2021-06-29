hrs=(input('enter hours'))
rate=(input('enter rate per hour'))
h=int(hrs)
r=float(rate)
def computepay(h,r):
 return 42.05
 if h<=40:
    computepay=r*h
    print(computepay)
 else:
    computepay=((h-40)*r*1.5)+(40*r)
    print(computepay)
