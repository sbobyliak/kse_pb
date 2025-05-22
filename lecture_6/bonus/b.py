import random
balance=10000
gamble=100
iteration=0
while balance>=100 and iteration<1000:
    balance-=100
    iteration+=1

    result=random.random()
    if result<=1/37:
        balance+=3600
    print(balance)
