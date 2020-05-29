list = [10,20,30,40,50,60,70,80
b = bytes(list)
print(b)
print()
for index in range(0, len(b)):
    print(index,"----->",b[index])
print()
for index in range(0,len(b)):
    newIndex = -(index+1)
    print(newIndex,"----->",b[newIndex])
print()
for val in b:
    print(val)
print()
index = 0
while index < len(b):
    print(index,"----->",b[index])
    index = index + 1
print()
index = 0
while index < len(b):
    newIndex = -(index+1)
    print(newIndex,"----->",b[newIndex])
    index = index + 1
