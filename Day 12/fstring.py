'''
f-string사용법

(문법) f"----"
변수는 {중괄호 안에}

age=13
name="뉴진스"
string=f"내 나이는 {age}이고, 이름은 {name}이야."
animal="고양이"
job="초등학생"
string=f"나는 {animal}를 좋아하는 {job}입니다"

print(string)
print(string)

---------------------------------
입력 input <-> 출력 print

for i in range(3):
    입력한거=input("나이를 입력하세요:")
    ddd=f"당신의 나이는 {입력한거}이군요!"
    print(ddd)

for i in range(3):
    gender=input("성별을 입력해 주세요:")
    name=input("성함을 입력해 주세요:")
    print(f"당신의 {gender}이고 이름은 {name}이네요. 환영해요!")
'''
for i in range(5):
    num1=input("첫 번쨰 숫자를 넣어주세요:")
    num2=input("두번쨰 숫자를 넣어주세요:")
    print(f"두 수를 합치면 {int(num1)+int(num2)}가 됩니다.")