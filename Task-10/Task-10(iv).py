import re
num = 0
txt = str(num)
if (len(txt) >= 1) & (len(txt) <= 3):
    x = re.search("[0-9]",txt)
    if x:
        print("Match found")
    else:
        print("Match not found")
else:
    print("Enter a valid number")