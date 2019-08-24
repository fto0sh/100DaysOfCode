Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x, y, z = "apple", "orange", "limon"
>>> basket=x+y+z
>>> print(basket)
appleorangelimon
>>> n=5
[basket[i:i+n]for i in range(0,len(basket),n)]

 
