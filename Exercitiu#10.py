import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list1 = random.sample(range(1, 12), 8)
list2 = random.sample(range(1, 13), 6)

print(list1)
print(list2)

list4 = [i for i in set(list1) if i in list2]
result = print([i for i in list4 if list4.count(i) == 1])
