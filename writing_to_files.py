import os
myfile = open("sample1.txt", "w+")

print(myfile.mode)
print(myfile.name)

myfile.write("hello python")
print(myfile.read())

myfile.close()

#deleting the created file------
#if (os.remove("sample.txt")):
 #   print("successfull")
