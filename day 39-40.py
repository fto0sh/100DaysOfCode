def expower(powr,num):
        if powr <1:
                return 1
        else :
                return num*expower(powr-1,num)
print(expower(3,5))

print()
print()


mylist = [-4, -6, -5, -1, 2, 3, 7, 9, 88]
print(mylist)
for i in mylist:
    x = lambda a: print(a) if a > 0 else None
    x(i)

