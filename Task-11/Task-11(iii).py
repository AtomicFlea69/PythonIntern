import random
list1 = []
for i in range(1,10):
    x = random.randint(1,50)
    list1.append(x)
print("The unsorted list is:",list1)
list_sort = sorted(list1)
print("The sorted list is:",list_sort)
