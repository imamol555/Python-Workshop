import random
import  sys
import os

my_tuple=(1,2,3,4,5)
print(my_tuple)

# u cannot change tupole items but u can change list items
# so if u eant u can convrt tuple into list
new_list=list(my_tuple)
print(new_list)

#list to tuple
new_tuple=tuple(new_list)
print(new_tuple)

#min max length of tuple

print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))