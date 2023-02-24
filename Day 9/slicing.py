'''
범위 지정(slice)
    a:b -> a이상 b미만
생략 가능한 slice
    처음부터 시작 할때 0 생략가능 맨마지막 생략 가능

a=[]
b=["watermelon","banana","cherry","apple"]
c=[]
for i in range(1,11):
    a.append(i)
print(i)
print(a[1:4])
print(a.index(2))
print(a[a.index(2):a.index(5)])
print(a[:4])
print(a[8:])
print(b[:1]+b[2:])
b.sort()
print(b[1:3])
b.append("orange")
b.reverse()
print(b[:3])
for i in range(1,21):
    if i%2==0:
        c.append(i)
print(c[5:])
print(c[:4])
print(c[2:7])
하율생일=[1,1,1,0,1,7]
유래생일=[1,1,0,5,0,2]
서현생일=[1,1,0,1,1,6]
print(하율생일[2:4]+유래생일[2:4]+서현생일[2:4])
print(하율생일[4:]+유래생일[4:]+서현생일[4:])
print(하율생일[:2]+유래생일[:2]+서현생일[:2])
'''
리스트=[]
for i in range(1,31):
    if i%7==0:
        리스트.append(i)
print(리스트[:2])
print(리스트[:])