'''
함수
-반복적인 일을 할 때 유용하게 사용되는 기법
-한 번 만들어 놓으면, 여러번 사용 가능
-ex) 쿠킹틀

1. 함수 만들기
2. 함수 부르기(여러번 가능)

<1번>
def 함수이름():
    실행할 코드 작성

<2번>
def 함수이름(입력):
    실행할 코드 작성

<3번>
def 함수이름(입력):
    실행할 코드 작성
    return 출력

def 하율():
    print("하율이")
하율()
하율()
하율()

def 유래(몇번):
    for i in range(몇번):
        print("나는 유래")
유래(3)
유래(7)

def 서현(입력):
    for i in range(입력):
        print("나는 서현")
    return i

서현(5)
print(서현(5))
결과=서현(7)
print(결과)
'''
#1
def 함수(몇번):
    for i in range(몇번):
        print("파이썬 함수 배움")
함수(5)

#2
def 곱하기(a,b):
    print(a*b)
    return a*b
곱하기(2,3)
곱하기(10,20)

#2-1
def 삼각형넓이(a,b):
    print(a*b/2)
    return a*b/2
삼각형넓이(10,5)
삼각형넓이(6,8)

#2-2
def 구구단(a):
    for i in range(1,10):
        print(a*i)
구구단(3)
구구단(7)

#2-3
def 홀수(a):
    for i in range(a*2):
        if i%2==1:
            print(i)
홀수(5)
홀수(6)