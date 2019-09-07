Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Mylist=["Fatimah","Sara", 30,69.7 ,55]
>>> print(Mylist)
['Fatimah', 'Sara', 30, 69.7, 55]
>>> Mylist.append("fto0sh")
>>> print(Mylist)
['Fatimah', 'Sara', 30, 69.7, 55, 'fto0sh']
>>> Mylist.remove(3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Mylist.remove(3)
ValueError: list.remove(x): x not in list
>>> Mylist.remove(30)
>>> print(Mylist)
['Fatimah', 'Sara', 69.7, 55, 'fto0sh']
>>> Mylist.clear()
>>> print(Mylist)
[]
>>> Mylist=["Fatimah","Sara", 30,69.7 ,55]
>>> print(Mylist)
['Fatimah', 'Sara', 30, 69.7, 55]
>>> welist=Mylist.copy()
>>> print(welist)
['Fatimah', 'Sara', 30, 69.7, 55]
>>> Mylist.count(3)
0
>>> Mylist.count(55)
1
>>> lists=["Ahmed",12,34]
>>> Mylist.extend(lists)
>>> print(Mylist)
['Fatimah', 'Sara', 30, 69.7, 55, 'Ahmed', 12, 34]
>>> x=Mylist.index(12)
>>> print(x)
6
>>> Mylist.insert(5,"maha")
>>> print(Mylist)
['Fatimah', 'Sara', 30, 69.7, 55, 'maha', 'Ahmed', 12, 34]
>>> Mylist.pop(4)
55
>>> print(Mylist)
['Fatimah', 'Sara', 30, 69.7, 'maha', 'Ahmed', 12, 34]
>>> Mylist.reverse()
>>> print(Mylist)
[34, 12, 'Ahmed', 'maha', 69.7, 30, 'Sara', 'Fatimah']
>>> Mylist.sort()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Mylist.sort()
TypeError: unorderable types: str() < int()
>>> def s(i)
SyntaxError: invalid syntax
>>> def s(i):
	return len(i)
Mylist=["Fatimah","Sara", 30,69.7 ,55]
SyntaxError: invalid syntax
>>> 
