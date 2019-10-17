import day53 as c 
print("1+8=",c.add(1,8))
print("4-2=" ,c.subtract(4,2))
print("6*6=",c.multiply(6,6))
print("8/2=",c.divide(8,2))

import datetime
date =datetime.datetime.now()
print(date.strftime("%c"))
t=datetime.date.today()
print(t)

x=int(t.strftime("%d"))
print(x-1)
print(x+1)


