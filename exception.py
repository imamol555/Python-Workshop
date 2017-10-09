try:
    data = open("sample.txt")
    for each_line in data:
       try:
            str1, str2 = each_line.split(":",maxsplit=1)
            print(str1)
            print(str2)
       except:
           pass

except:
    print("file not present")

