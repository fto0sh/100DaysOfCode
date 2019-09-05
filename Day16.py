Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple=(3,)
>>> print(thistuple)
(3,)
>>> thistuple=(3,1,3,4,1,7)
>>> print(thistuple)
(3, 1, 3, 4, 1, 7)
>>> thistuple=("Ahmed",1.1,4,"بايثون")
>>> print(thistuple)
('Ahmed', 1.1, 4, 'بايثون')
>>> thistuple = ("apple", "banana", "cherry")
>>> print(thistuple[1])
banana
>>> thistuple = ("apple", "banana", "cherry")
>>> for x in thistuple:
	print(x)

	
apple
banana
cherry
>>> thistuple = ("apple", "banana", "cherry")
>>> thistuple[3] = "orange" # This will raise an error
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    thistuple[3] = "orange" # This will raise an error
TypeError: 'tuple' object does not support item assignment
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thistuple = ("apple", "banana", "cherry")
>>> del thistuple
>>> print(thistuple) #this will raise an error because the tuple no longer exists
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(thistuple) #this will raise an error because the tuple no longer exists
NameError: name 'thistuple' is not defined
>>> thistuple=("apple", "banana", "cherry","orang")
>>> print(thistuple[0:3])
('apple', 'banana', 'cherry')
>>> 
