lst=["муза","темп","музичний","тон","ритм","музика","музикальний","голос","мелодія","пісня"]
with_prefix=[]
for word in lst:
    if word.startswith("муз"):
        with_prefix.append(word)
print(with_prefix)