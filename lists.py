import random
import sys
import os

mylist = [5, 'amol', 555, 5555, 55555]

print('I am ', mylist[1])
print("my lucky no is", mylist[2])

amol_list = mylist[1:3]
print(amol_list)

# matrix list
new_list = [mylist, amol_list]
print(new_list)
print(new_list[1][1])

# appending
amol_list.append('patil')
print(amol_list)

# inserting at apecified index
mylist.insert(0, 'love')
print(mylist)

# removing an item from list
mylist.remove(5555)
print(mylist)

# deleitng an item by index
del  mylist[4]
print(mylist)

#sorting the list
sort_list=[2,5,4,7,6,9,8]
sort_list.sort()
print(sort_list)

#reverse
sort_list.reverse()
print(sort_list)

#combini9ng the lists
l1=[11,21,31,41,51]
l2=[5,15,25,35,45,55]

l3 = l1 + l2
print(l3)

#operations on list
print(len(l3))
print(max(l3))
print(min(l3))
