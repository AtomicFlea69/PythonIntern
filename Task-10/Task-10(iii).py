import re
txt = "atomicflea"
x = re.search("[0-9]$",txt)
if x:
    print("Match found")
else:
    print("Match not found")