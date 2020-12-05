import re
txt = "HELLO"
for i in txt:
    x = re.findall("[A-Z]",i)
if x:
    print("Only uppercase,Match Found")
else:
    print("Lowercase is present,No match found")