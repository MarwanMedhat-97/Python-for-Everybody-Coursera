a=int(input("Enter number: "))
temp=a
n=0
x=list()
y=list()
while temp>0:
    n+=1
    x.append((temp%10))
    temp=temp//10
for i in range(len(x)):
    y.append(x[i]**n)

print(sum(y),a)
if(sum(y)==a):
    print('Armstrong')
else:
    print('Not Armstrong')