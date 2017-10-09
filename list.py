newlist = [1,2,
            ["a",'b','c'],
            [4,
                ["x",'y','z']
             ]
           ]
def print_list(mylist):
    for item in mylist:
        if isinstance(item,list):
            print_list(item)
        else:
            print(item)
print_list(newlist)
