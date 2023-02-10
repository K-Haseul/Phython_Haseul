'''
막대그래프 그리기
-모듈 설치필요
-python에서 모듈을 설치할 때는 pip명령어를 쓴다
-터미널 창에서 "pip install matplotlib"을 입력

PYTHON
 -API
 -Library
'''
import matplotlib.pyplot as plt

fruits=["apple","blueberry","cherry","orange"]
counts=[5,10,7,12]
bar_color=["#FF6C6C","#BFABFF","#9F3F48","#FFC070"]
창,내용=plt.subplots(1,3)
# 내용.barh(fruits,counts,color=bar_color)
내용[0].bar(fruits,counts,color=bar_color)
내용[1].barh(fruits,counts,color=bar_color)
내용[2].bar(fruits,counts,color=bar_color)
plt.show()