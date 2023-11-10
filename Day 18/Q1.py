starbucks=0
twosome=0
megacoffee=0

for i in range(1,1000):
    if i%3==0:
        starbucks+=i
for y in range(1,1000):
    if y%5==0:
        twosome+=y
for t in range(1,1000):
    if t%3==0:
        if t%5==0:
            megacoffee+=t
print(starbucks+twosome-megacoffee)





sum=0

for i in range(10,1001):
    a=str(i)
    결과=1
    for j in a:
        결과*=int(j)
    sum+=결과
print(sum)





a=[1,-2,3,-1]
b=[]
c=[]
for i in a:
    if i>0:
        b.append(i)
    else:
        c.append(i)
print(c+b)