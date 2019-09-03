thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["Ahmad", "omer", "khalid"]
mylist = thislist.copy()
thislist.pop(0)
print(mylist)
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
