a = 'Durga Software Solutions'
b = "Durga Software Solutions"
c = '''Durga 
Software 
Solutions'''
print(a)
print(b)
print(c)
print()
a = "Durga "
b = a + "Software "
c = b + "Solutions"
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
print()
str = "Durga"
print(str)
print(str[2])
print(str[4])
print(str[-2])
print(str[-4])
#print(str[5]) --> IndexError
print(str[-5])
#print(str[-6]) --> IndexError
print()
str = "Durga Software Solutions"
print(str)
print(len(str))
print()
str = "Durga Software Solutions"
for x in range(0, len(str)):
    print(x,"--->",str[x])
print()
for x in range(0, len(str)):
    index = -(x+1)
    print(index,"--->",str[index])
print()
str ="Durga Software Solutions"
print(str)
print()
index = 0
while index < len(str):
    print(index,"---->",str[index])
    index = index + 1
print()
index = -1
while index >= -len(str):
    print(index, "---->",str[index])
    index = index - 1
print()
str1 = '\'Durga\' "Software" \'''Solutions\''''
print(str1)
str2 = "'Durga' \"Software\" '''Solutions'''"
print(str2)
str3 = ''''Durga' "Software" \'''Solutions\''' '''
print(str3)
print()
str = "Durga Software Solutions"
for x in range(0,len(str)):
    print(str[x],end="  ")
print()
for x in str:
    print(x,end="  ")
print()
a = 0
while a < len(str):
    print(str[a],end="  ")
    a = a + 1
print()
print()
str = "Durga Software Solutions"
print("Forward Direction : ", end="")
for x in range(0, len(str)):
    print(str[x], end=" ")
print()
print("Backward Direction : ", end="")
for x in range(0,len(str)):
    print(str[-(x+1)], end=" ")