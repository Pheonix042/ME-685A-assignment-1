name=str(input('Enter expression of x:'))
from romil import differential_1
a,s,d=differential_1(name)
print('1st Derivative is',a)
print('2nd Derivative is',s)
print('3rd Derivative is',d)
