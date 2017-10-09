data = open("sample.txt")

print(data.readline(),end='')

print(data.seek(2))
print(data.readline(),end='')
print(data.tell())

data.close()