lst_1=[1,3,5,7,9]
lst_2=[2,4,6,8,10]
comb=[]
for a,b in zip(lst_1, lst_2):
    comb.append(a)
    comb.append(b)
print(comb)