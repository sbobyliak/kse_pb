data={"rollerskates": 10, "bicycle": 6, "skateboard": 2, "skies": 0}
for key,value in data.items():
    if value==0:
        data[key]="out of stock"
    elif value<5:
        data[key]="low"
    elif value<10:
        data[key]="medium"
    else:
        data[key]="high"
print(data)
