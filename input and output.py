import random
import  sys
import os

# getting input from user
print('Hi, may I knw your gud name plz')

name = sys.stdin.readline()

print('hi',name)

print("hey %s what is ur lucky no" % name )
num=sys.stdin.readline()



print("%s , ur fav no is %s and that is %.3f  correct" % (name,num,100) )