import matplotlib.pyplot as plt
plt.figure()

x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
for i in range(-10,11):
    x1.append(i)
    x2.append(i)
    x3.append(i)

    y1.append(i)
    y2.append(i**2)
    y3.append(i**3)
    # y1.append(2*i**3+4*i+2)
    # y1.append(-4*i**4+3*i**3+2*i**2-5*i+7)

# x1=[1,2,3]
# y1=[3,5,7]
# x2=[1,2,3]
# y2=[0.25,0.5,0.75]
# plt.plot(x1,y1,'r',x2,y2,'ko')
# plt.plot(x1,y1,'o')
# plt.plot([1,2,3],[1,2,3],[1,2,3],[2,4,6],[1,2,3],[0.5,1,1.5])
plt.plot(x1,y1,x2,y2,x3,y3)
plt.show()