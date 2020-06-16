from matplotlib import pyplot as plt
x=[1,6,10,4,7]
y=[5,4,3,2,1]

plt.subplot(2,1,1)
plt.plot(x,y,'--',color='g')
plt.title("Demo1")
plt.subplot(2,1,2)
plt.bar(x,y)
plt.title("Demo2")
plt.show()