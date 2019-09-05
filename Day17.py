Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> thistuple = ("apple", "banana", "cherry")
>>> if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

  
Yes, 'apple' is in the fruits tuple
>>> thistuple=("python,")*3
>>> print(thistuple)
python,python,python,
>>> thistuple1=(1,2,3,4)
>>> thistuple2=(5,6)
>>> thistuple=thistuple1+thistuple2
>>> print(thistuple)
(1, 2, 3, 4, 5, 6)
>>> thistuple = ("apple", "banana", "cherry")
>>> print(len(thistuple))
3
>>> thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thislist=[3,4,5,6,"A","B"]
>>> thistuple=tuple(thislist)
>>> print(thistuple)
(3, 4, 5, 6, 'A', 'B')
>>> 
