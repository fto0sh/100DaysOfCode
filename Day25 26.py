Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> set1={1,3,5,7,8}
>>> print(set1)
{8, 1, 3, 5, 7}
>>> set1.add({4,8,12})
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    set1.add({4,8,12})
TypeError: unhashable type: 'set'
>>> set1.add(4,8,12)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    set1.add(4,8,12)
TypeError: add() takes exactly one argument (3 given)
>>> set1.add([4,8,12])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    set1.add([4,8,12])
TypeError: unhashable type: 'list'
>>> set1.update([4,8,12])
>>> print(set1)
{1, 3, 4, 5, 7, 8, 12}
>>> set1.remove(8)
>>> print(set1)
{1, 3, 4, 5, 7, 12}
>>> set1.clear()
>>> print(set1)
set()
>>> thisdict={'name':'pigon','type':'bird','skin cover':'feather'}
>>> print(thisdict)
{'name': 'pigon', 'skin cover': 'feather', 'type': 'bird'}
>>> s=thisdict['type']
>>> print(s)
bird
>>> thisdict['skin cover']='hair'
>>> print(thisdict)
{'name': 'pigon', 'skin cover': 'hair', 'type': 'bird'}
>>> 
