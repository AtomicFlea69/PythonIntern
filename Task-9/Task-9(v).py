import random
randomlist = []
for i in range(0,20):
    n = random.randint(1,500)
    randomlist.append(n)
list1 = list(filter(lambda even_numbers:(even_numbers % 2 == 0),randomlist))
print("The even numbers in the list is:",list1)