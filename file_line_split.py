try:
    data = open("sample.txt")

    for each_line in data:
        try:
            (str1,str2) = each_line.split("a",maxsplit=1)
            print("str1 = %s "%str1,end='\n' )
            print("str2 = ", str2, end='\n')
        except:
            pass
    data.close()
except:
    print("THe data file is  missing !")
