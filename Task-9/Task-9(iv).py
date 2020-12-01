list1 = [1,9,12,35,45,56,72,84,90]
a = list(filter(lambda filter_list:(filter_list % 9 == 0),list1))
print("The numbers divisible in the list are:",a)