'''
클래스(class)
-객체를 생성하기 위한 설계도
-생성된 객체는 인스턴스(instance)라고 함
-클래스의 멤버 변수를 프로퍼티(property)라고 함
  ㄴ 클래스 안에 있는 변수들 
-클래스의 멤버함수를 메소드(method)라고 함
  ㄴ 클래스 안에 있는 함수
-객체들을 만들어서 프로그래밍 하는 방식을 OOP(객체지향 프로그래밍)
  ㄴ C언어는 함수형 프로그래밍
-문법
  ㄴ class 클래스이름:
        프로퍼티
          or
        메소드
'''

class 수학:
    원주율=3.14
    홀수=[1,2,3]
# 초등수학=수학()
# print(초등수학.홀수)

# 중등수학=수학()
# print(중등수학.원주율)

    def 삼각형넓이(self,가로,세로):
        넓이=가로*세로/2
        return 넓이
    def 사각형넓이(self,가로,세로):
        넓이=가로*세로
        return 넓이
    def 사다리꼴넓이(self,가로,세로,높이):
        넓이=(가로+세로)*높이/2
        return 넓이
대학수학=수학()
print(대학수학.삼각형넓이(3,4))
print(대학수학.사각형넓이(5,6))
고등수학=수학()
print(고등수학.사다리꼴넓이(2,3,4))