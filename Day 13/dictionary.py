'''
딕셔너리(dictionary)
-파이썬에서 사용하는 자료 구조중 하나
-key 와 value 쌍으로 이루어져 잉ㅆ음
-중괄호를 이용함 {}
-indexing 가능함 key값을 이용해서
-indexing method 이용 가능(클래스 함수)

height={"서현":160, "하율":140, "유래":153}

print(height["서현"])
print(height.get("서현"))
print(height.keys())
print(height.values())
height.update({"하율":165})
height["하율"]=130
print(height)
height.update({"선생님":180})
height["아인"]=170
del height["선생님"]
del height["아인"]

print("선생님" in height)
print("하율" in height)
'''

fruits={"오렌지":30, "바나나":20, "사과":50}
fruit=input("과일 상점 입니다. 어떤 과일을 원하시나요?:")
if fruit in fruits:
    print(f"{fruit}는 {fruits[fruit]}개 있어요")
else:
    print(f"저희 상점에는 {fruit}가 없습니다.")