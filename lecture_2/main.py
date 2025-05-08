name="Sofiia"
surname="Bobyliak"
country="Ukraine"
date=8
height=1.58
is_happy=True
has_deadlines=False
weigth=5.8
want_to_study=True
year=2025

a=8
b=6
a,b=b,a
print(a)
print(b)

x=3
y=9
task_1=2*x+3*y
task_2=x**2+2*x*y+y**2
task_3=2/8*x-13/7*y
task_4=y**((4*x-2*y)**0.5)
task_5=x%y
task_6=(y//x)**2
task_7=x>y
task_8=(x**2)!=y

product_name="rollerskates"
product_price=15000
outcome=("{} is {} grivnas".format(product_name,product_price))


x1=7
x2=5
x3=8
x4=2
is_true=((x1>x3)or(x2>x4)and not(x2!=x3)or(x1==x4))

height=float(input("Введіть ваш зріст в метрах"))
weight=float(input("Введіть вашу вагу в кілограмах"))
bmi=(height**2)/weight
print("При вазі {} кг і рості {} метрів, Ваш BMI складає {}".format(height,weight,bmi))

r1=30
r2=36
size1=3.14*r1**2
size2=3.14*r2**2
diff=(size2-size1)/size1*100
x="{:.2f}".format(diff)
print("Друга піца на {}% більша за першу".format(x))