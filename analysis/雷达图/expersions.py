import numpy as np
import matplotlib.pyplot as plt

#=======自己设置开始============
#标签
labels = np.array(['1-3年','10年以上','1年以内','3-5年','5-10年 ','应届生','经验不限'])
#数据个数
dataLenth = 7
#数据
data = np.array([22,47,19,28,35,9,23])
#========自己设置结束============

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)# polar参数！！
ax.plot(angles, data, 'bo-', linewidth=2)# 画线
ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
ax.set_title("经验对工资影响的雷达图", va='bottom', fontproperties="SimHei")
ax.set_rlim(0,50)
ax.grid(True)
plt.savefig("../../tmp/雷达图/expersionPlot.png")
plt.show()