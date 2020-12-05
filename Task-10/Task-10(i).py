import re
txt = "@-="
x = re.search("[a-z,A-Z,0-9]",txt)
if x:
    print("The given letters are present")
else:
    print("Match not found")


