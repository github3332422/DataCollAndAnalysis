import numpy as np
import matplotlib.pyplot as plt

#=======自己设置开始============
#标签
labels = np.array(['大专','本科','硕士','博士','学历不限'])
#数据个数
dataLenth = 5
#数据
data = np.array([17,27,30,48,29])
#========自己设置结束============

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)# polar参数
ax.plot(angles, data, 'bo-', linewidth=2)# 画线
ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
ax.set_title("学历对工资影响的雷达图", va='bottom', fontproperties="SimHei")
ax.set_rlim(0,50)
ax.grid(True)
plt.savefig("../../tmp/雷达图/educationPlot.png")
plt.show()