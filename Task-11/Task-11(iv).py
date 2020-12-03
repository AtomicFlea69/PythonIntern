import random
def odd_numbers(num):
    if(num%2 != 0):
        return True
    else:
        return False
list1 = []
for i in range(0,10):
    x = random.randint(1,100)
    list1.append(x)
print("The list before filtering",list1)
filtered_list = filter(odd_numbers,list1)
list2 = []
for num in filtered_list:
    list2.append(num)
print("The list after filtering is:",list2)