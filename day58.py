import re

#Return a list containing every occurrence of "ai":

str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

import re

str = "The rain in Spain"
x = re.findall("Portugal", str)
print(x)

import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())
import re

str = "The rain in Spain"
x = re.split("\s", str)
print(x)
