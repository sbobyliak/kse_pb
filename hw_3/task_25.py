lst=[1, 5, 8, 3, 10, 2]
x=3
y=8
result=[]
for num in lst:
    if num>x:
        result.append(num*y)
    else:
        result.append(num)
print(result)