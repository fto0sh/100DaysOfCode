Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=5
>>> print(x > 3 or x < 4)
True
>>> x = ["apple", "banana"]
>>> y = ["apple", "banana"]
>>> z = x
>>> print(x is z)

# returns True because z is the same object as x
True
>>> print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
SyntaxError: multiple statements found while compiling a single statement
>>> print(x is y)

# returns False because x is not the same object as y, even if they have thew same content
False
>>> print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
True
>>> print(x is not z)
False
>>> x = ["apple", "banana"]
>>> print("banana" in x)
True
>>> 
