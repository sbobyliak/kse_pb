a=int(input("Введіть ціле число "))
if a%2==0:
  print("Парне")



score=float(input("Введіть середній бал "))
if score>=90:
  print("Відмінник")
elif score>=75:
  print("Молодець")
else:
  print("Старайся більше")



for price in range(10,101,5):
  print(f"Ціна без ПДВ {price}, - Ціна з ПДВ {price*1.2}")



a=int(input("Введіть число "))
b=int(input("Введіть число "))
c=int(input("Введіть число "))
if a>b and a>c:
  print(f"{a}")
elif b>a and b>c:
  print(f"{b}")
elif c>b and c>a:
  print(f"{c}")



x=1000
m=0
while x<=5300:
  print(f"номер місяця {m} - сума {x}")
  x+=300
  m+=1



year=int(input("Введіть рік "))
if year%4==0 and year%100!=0 or year%400==0:
  print("Високосний")
else:
  print("Звичайний рік")



for i in range(0,21):
  if i%4==0:
    continue
  print (f"{i}")



amount_left=10000
month=0
while amount_left>0:
  print(f"Місяць: {month} - Залишок боргу: {round(amount_left,2)}")
  amount_left-=1200
  amount_left*=1.02
  month+=1
print(f"Щоб повністю погасити кредит знадобиться {month} місяців")



total=0
while True:
  guestion=float(input("Введіть ваш місячний дохід або '0' для виходу "))
  if guestion==0:
    break
  elif guestion<0:
    print("Дохід не може бути від'ємним")
    if guestion<0:
      continue
  else:
    print ("Ваш дохід збережено:")
    total+=guestion
    print(f"Загальна сума {total}")