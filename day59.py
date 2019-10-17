import re

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)

import re

str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)
import re

str = "The rain in Spain"
x = re.search("ai", str)
print(x) #this will print an object

import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

import re

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)

import re

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())
