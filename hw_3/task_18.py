text=[["Lorem ipsum dolor sit amet, consectetur adipiscing elit."],
        ["Integer egestas velit iaculis fermentum posuere."],
        ["Curabitur venenatis ante quis elit elementum commodo."],
        ["Maecenas varius dolor nisl."],
        ["Aenean imperdiet metus non neque eleifend, vitae tincidunt purus lobortis."],
        ["Vestibulum sit amet mi velit. Fusce porta imperdiet massa, id blandit lacus tincidunt vel."]
]
for paragraph in text:
    for sentence in paragraph:
        for char in sentence:
            if char.isupper():
                print(char)