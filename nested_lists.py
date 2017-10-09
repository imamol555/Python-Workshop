mylist = [5,7,8,"heloo"]

print(mylist[3])


newlist = [[5,4,3,2,1],['amol','patil']]

print(newlist[1][1])

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:   print(each_item)
        '''-->
        5
        4
        3
        2
        1
        amol
        patil'''

        ''' print(each_item)  -->
                [5, 4, 3, 2, 1]
                ['amol', 'patil'] '''
print_lol(newlist)