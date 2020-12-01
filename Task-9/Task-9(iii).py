nums = [1,2,3,4,5]
n = 2
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))