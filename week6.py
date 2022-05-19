import urllib.request,urllib.parse,urllib.error
import json

hand=urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_1526808.json')
file=hand.read()

info = json.loads(file)
sum=0
for item in info['comments']:
    sum=sum+item['count']
print(sum)