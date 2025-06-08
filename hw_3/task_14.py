lst=["статуя","ротатор","механізм","тон","радар","навушники","око","зараз","інженер","пісня"]
for word in lst:
    if word!=word[::-1]:
        lst.remove(word)
print(lst)