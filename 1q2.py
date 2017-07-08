a=float(input('Enter cooefficient of x^2:'))
b=float(input('Enter cooefficient of x:'))
c=float(input('Enter cooefficient of x^0:'))
from romil import quad
x1,x2=quad(a,b,c)
print('first root:',x1)
print('Second root',x2)
