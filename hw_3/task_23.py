strings = [
    "bike",
    "rollerskates",
    "skate",
    "ski",
    "board"
]
x=4
count=0
for s in strings:
    if len(s)>x:
        count+=1
print(count)