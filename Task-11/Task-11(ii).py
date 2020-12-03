import random
list1 = []
list2 = []
for i in range(1,8):
    x = random.randint(1,8)
    y = random.randint(1,8)
    list1.append(x)
    list2.append(y)
list_zip = zip(list1,list2)
list_tup = tuple(list_zip)
print(list_tup)