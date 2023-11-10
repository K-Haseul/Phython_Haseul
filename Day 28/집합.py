'''
집합의 특징
1- 순서가 없음
2- 중복이 없음

집합에서의 연산

교집합 &
    - 겹치는 것만
    예) 
    A={1,2,3} B={3,4,5}
    A와 B의 교집합 => 3

합집합 |
    - 중복뺴고 다
    예)
    A={1,2,3} B={3,4,5}
    A와 B의 합집합 => 1,2,3,4,5

차집합 -
    - A-B , B-A
    예)
    A={1,2,3} B={3,4,5}
    A-B => 1,2
    B-A => 4,5

GCD - 최대공약수
LCM - 최소공배수


a={1}
print(a)
print(type(a))

b=[2]
print(b)
print(type(b))

c=(3,4)
print(c)
print(type(c))

d={4:"a",5:"b"}
print(d)
print(type(d))

e=[100,200,300]
f=[500,600,700]
print(e[2])
print(f[1])
print(e[1:])
print(f[:1])

A={1,2,3}
B={3,3,4,4,4,5,5}
print(A)
print(B)
print(A-B)
print(B-A)
print(A&B)
print(A|B)

fruit={"lemon","apple","banana","cherry"}
red={"fire","tomato","apple","cherry"}

print(fruit&red)
print(fruit|red)
print(fruit-red)
print(red-fruit)

A={1,2,3,4,6,8,12,24}
B={1,2,3,4,6,9,12,18,36}
CD=A&B
GCD=max(CD)

LCM=GCD*(24/GCD)*(36/GCD)

print(GCD)
print(LCM)
'''

A={1,2,4,7,14,28}
B={1,2,3,6,7,14,21,42}
CD=A&B
GCD=max(CD)

LCM=GCD*(28/GCD)*(42/GCD)

print(CD)
print(GCD)
print(LCM)