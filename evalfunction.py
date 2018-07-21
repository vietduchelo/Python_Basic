
from math import *
s= "(5+8)-(7/4)+4" # string
x= eval(s)
print (x)

#  ======
s= "(7*6)-(7/3)+8+sin(1)+pow(2,3)"
x= eval(s)
print(x)

# =====

x1,x2 = eval(input("input x1, x2: "))
print ("x1=",x1," x2=",x2)