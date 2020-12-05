import re
txt = "ab de villers"
x = re.findall("^ab",txt)
if x:
    print("Match found")
else:
    print("Match not found")