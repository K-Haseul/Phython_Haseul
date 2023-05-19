'''
클래스
1. 생성자(constructor)
 :객체를 생성할 때 자동으로 호출되는 메소드

문법
class 이름:
   def __init__(self):
      작성
   
'''
# class 수학:
#     def 더하기(self,a,b):
#         결과=a+b
#         return 결과
# 초등수학=수학()
# print(초등수학.더하기(10,20)) 

# class 강아지:
#     def __init__(self,강아지눈,강아지털,강아지이름):
#         self.강아지눈=강아지눈
#         self.강아지털=강아지털
#         self.강아지이름=강아지이름
#     def 소개하기(self):
#         print(f"강아지눈은 {self.강아지눈}개 이고 강아지털은 {self.강아지털}이며 강아지 이름은 {self.강아지이름}입니다.")
# 우리집강아지=강아지(2,"검은색","검둥이")
# 친구네강아지=강아지(2,"하얀색","멍멍이")
# 하율네강아지=강아지(3,"사람색","이승욱")
# 하율네강아지.소개하기()

# print(우리집강아지.강아지눈)
# print(우리집강아지.강아지털)
# print(우리집강아지.강아지이름)

# print(친구네강아지.강아지눈)
# print(친구네강아지.강아지털)
# print(친구네강아지.강아지이름)

class 연산:
    def __init__(self,첫번째수,두번째수):
        self.첫번째수=첫번째수
        self.두번째수=두번째수
    def 더하기(self):
        결과=self.첫번째수+self.두번째수
        return 결과
    def 뺴기(self):
        결과=self.첫번째수-self.두번째수
        return 결과
    def 곱하기(self):
        결과=self.첫번째수*self.두번째수
        return 결과
    def 나누기(self):
        결과=self.첫번째수/self.두번째수
        return 결과
사칙연산=연산(3,5)
print(사칙연산.더하기())
print(사칙연산.뺴기())
print(사칙연산.곱하기())
print(사칙연산.나누기())