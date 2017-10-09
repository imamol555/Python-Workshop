import random
import  sys
import os

# for loop

for x in range(0,10):
    print(x,end=' ')

#for loop for traversing thr list
mylist=['amol','aakash','nirmal','swapnil','pankaj']

for x in mylist:
    print(x)
#for loop for traversing thr 2D list

new_list=[[1,2,3,4,5],[11,22,33,44,55],[111,222,333,444,555]]

for x in range(0,3):
    for y in range(0,5):
        print(new_list[x][y],end='\t')
    print('\n')