import random
import  sys
import os

str= "I am Amol Patil. I m doing my engineering in Computer Science"

#char operaions
print(str[0:15])
print(str[-7:])
print(str[:-7])

#str operations

#capitalizing the first letter of str
print(str.capitalize())

#getting the index of a substr
print(str.find('Amol'))

#if all are char in str
print(str.isalpha())
str2='amol'
print(str2.isalpha())

#if the str is alphanumeric
print('\"%s\" is alphanumeric ' % str ,end="\t->" )
print(str.isalnum())
#length of str
print(len(str))
print(len(str2))

#replacing the substr by another str

print(str.replace('Amol',"Aakash"))

#splitting the str into list of words sepaerated by space
str_list=str.split(" ")
print(str_list)

#splitting the str into list of words sepaerated by letter a
str_list=str.split("a")
print(str_list)