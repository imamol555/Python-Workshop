def print_list(newlist):
    for each_item in newlist:
        if isinstance(each_item,list):
            print_list(each_item)
        else:
            #print(end='\t')
            print(each_item)

