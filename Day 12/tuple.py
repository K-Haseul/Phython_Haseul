'''
튜플(tuple)

(문법)
[](x) ()(o)

immutable(변경 불가능한)
indexing 가능 -> [] -> 읽기 가능 -> 값은 변경 불가
slicing 가능
list 메소드 사용 불가
'''

a=[1,2,3]
b=(1,2,3)
c=tuple(a)
a[2]=100

print(a[:2])
print(b[:2])
print(c)