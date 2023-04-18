
#这个程序用来做实验数据的一次方程线形拟合以及数据间的相关性判断
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
# 准备数据,将(x,y)坐标点进行输入
x = np.array([0.5,1,1.5,2,2.5,3])  
y = np.array([14.3,28.8,42.6,57,74.4,82.5])
pc = pearsonr(x, y)
print("相关系数：", pc[0])
print("显著性水平：", pc[1])
# 使用polyfit方法来拟合,并选择多项式,这里先使用1次方程
z1 = np.polyfit(x, y, 1)
# 使用poly1d方法获得多项式系数,按照阶数由高到低排列
p1 = np.poly1d(z1)
# 在屏幕上打印拟合多项式
print(p1)
# 求对应x的各项拟合函数值
fx = p1(x)
# 绘制坐标系散点数据及拟合曲线图
plot1 = plt.plot(x, y, '*', label='F/N')#自变量名称x
plot2 = plt.plot(x, fx, 'r', label='U/mV')#因变量名称y
plt.xlabel('F/N')#自变量
plt.ylabel('U/mV')#因变量
plt.legend(loc=4)  # 指定legend的位置,类似象限的位置
plt.title('U-F')#图像标题
plt.show()
plt.savefig('拟合结果')#文件名称
