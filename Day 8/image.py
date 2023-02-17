import numpy as np
'''
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

c=[1,2,3]
d=[4,5,6]
print(c+d)
'''

import matplotlib.pyplot as plt
import matplotlib.image as img
# my_image=img.imread("./Phython_Haseul/Day 8/인우.jpg")
# plt.imshow(my_image)
my_matrix=np.array([
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
    [[255,0,0],[255,0,0],[255,255,255],[255,0,0],[255,0,0]],
    [[255,0,0],[255,255,255],[255,255,255],[255,255,255],[255,0,0]],
    [[255,0,0],[255,0,0],[255,255,255],[255,0,0],[255,0,0]],
    [[255,0,0],[255,0,0],[255,0,0],[255,0,0],[255,0,0]],
])
plt.imshow(my_matrix)
plt.show()