newdict = {"name":'amol', 'age':20, 'gf':"python"}

print(newdict["name"])
'''
list1 = ["name",'age','gf',"lucky_no"]
list2 = ["amol",20,'python',555]

newlist = list(zip(list1,list2))
print(newlist)

mydict = dict(newlist)
print(mydict)
'''
print(newdict.keys())
print(newdict.values())

print(newdict.items())

mydict = newdict.copy()
print(mydict)
