'''
리스트(aka. array)
 -데이터응 저장하는 방식 중 하나
 -규칙은 대괄호와 쉼표로 구분

 -출력 시 모두 나타남
 -특징1) :순서로 안에 있는 내용을 선택 할 수 있음
        :순서는 0부터 시작
        :선택 할 때도 대괄호 사용함
        :마지막 순서는 -1해도 무방
 -특징2):append를 사용해 추가할 수 있음
        :pop을 이용해 삭제할 수 있음
          ㄴ*맨 마지막이 사라짐
 -특징3):선택한 값을 지우고 싶을때 remove 사용
 -특징4):정렬(오름차순)할 때 sort 사용
 -특징5):정렬(내림차순)할 때 reverse 사용

- 특징1 예시)
a="하율"
b=10
c=["사과","배","바나나"]
d=[10,20,30]
e=["축구",2,"야구",3]


print(a)
print(b)
print(c)
print(d)
print(e)

print(d[0]+d[1])
print(d[2]//d[0])
print(d[-1]-d[1])

- 특징2,3 예시)
요일=["일요일","월요일"]
print(요일)

요일.append("화요일")
print(요일)

요일.pop()
print(요일)

요일.remove("일요일")
print(요일)

- 특징4 예시)
fruit=["orange","watermelon","banana","apple"]

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

list=[]
for i in range(10,21):
  if i%3==0:
    list.append(i)
list.reverse()
print(list)
'''

# 1
lis=[]
for i in range(1,21):
  if i%2==1:
    lis.append(i)
lis.reverse()
print(lis)

# 2
list=[]
for i in range(50,101):
  if i%3==0:
    if i%4==0:
        list.append(i)
list.reverse()
print(list)

# 3
print(lis[0]*list[-1])