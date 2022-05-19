import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

hand=urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_1526807.xml')
file=hand.read()
print(file)
stuff=ET.fromstring(file)
counts = stuff.findall('comments/comment')
lst=list()
for item in counts:
    lst.append(int(item.find('count').text))

print(sum(lst))
#print(sum(counts))