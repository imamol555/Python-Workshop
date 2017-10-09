import random
import  sys
import os

test_file=open("test.txt","ab+")
print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Hello, I am Amol. This is my first file I/O in Python","UTF-8"))

test_file.close()

test_file=open("test.txt","r+")
txt=test_file.read()
print(txt)
test_file.close()
if (os.remove("test.txt")):
    print("successfull")