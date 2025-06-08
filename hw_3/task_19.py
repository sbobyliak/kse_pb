from collections import Counter
lst=[2,9,34,26,123,643,34,78,43,9,0,76,323,123,57,43,6,9,6,3,123,45,34,2,1,5,6,34]
lst.sort()
print(lst)
freq = Counter(lst)
sorted_lst = sorted(lst, key=lambda x: (-freq[x], x))
print(sorted_lst)