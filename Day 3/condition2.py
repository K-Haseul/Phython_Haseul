'''
조건문

1. while 조건:
  ㄴ 실행할 코드작성
1.조건이 참이면 아래 코드가 실행됨
2.조건이 거짓이면 While이 끝남
3.for 조건문은 while조건문으로 바꿀수있다

2. for을 While로 바꾸기
for i in range(3):
    print("hi")

i=0
while i<3:
    print("hi")
    i+=1

3. while이 참일떄, 거짓일때
while True:
    print("왜이래")
while False:
    print("왜이래")

#1
i=1
while i<11:
    print(i)
    i+=1

#2
i=1
while i<11:
    if i%2==0:
        print(i)

#3
sum=0
i=1
while i<11:
    if i%3==0:
        sum+=i
    i+=1
print(sum)

#4
i=50
while i<101:
    if i%3==0:
        if i%7==0:
            print(i)
    i+=1

#5
i=1
sum=1
while i<21:
    if i%2==0:
        sum*=i
    i+=1
print(sum)
'''