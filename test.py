han= open('actual.txt')
import re
lst=list()
for line in han:
    line=line.rstrip()
    y=re.findall("[0-9]+",line)
    if(len(y) == 0):
       continue
    for i in range(len(y)):
        lst.append(float(y[i]))

print(len(lst))
print(sum(lst))