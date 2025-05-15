nums = [3, 7, 2, 9, 5]
total=0
for num in nums:
  total+=num
mid=total/(len(nums))
print(mid)



nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]
unique_nums=set(nums)
my_lst=list(unique_nums)
even=my_lst[0::2]
final=even[::-1]
print(final)



grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]
mid_grade_list=[]
for i in grades:
  mid_grade=sum(i)/len(i)
  mid_grade_list.append(round(mid_grade,2))
max_value=max(mid_grade_list)
for index, grade in enumerate(mid_grade_list):
  #print(f"{index}:{grade}")
  if grade==max_value:
    student_index=index
print(student_index)
print(max_value)
print(grades[student_index])



prices = {
    "apple": 12,
    "banana": 8,
    "milk": 25,
    "bread": 20
}
price_value=list(prices.values())
print(sum(price_value))



people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}
cities=list(set(people.values()))
names=list(people.keys())
new_dict={}
for i in cities:
  new_dict[i]=[]
for key, value in people.items():
  new_dict[value].append(key)
print(new_dict)