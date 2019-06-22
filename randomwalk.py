#encoding:utf-8
"""
随机生成数据，进行matplotlib可视化操作
"""
#author cfx
from random import choice
class RandomWalk():
    def __init__(self,numpoints=5000):
        self.numpoints=numpoints
        self.x_values=[0]
        self.y_values=[0]
    def fill_walk(self):
        #计算随机漫步包含的所有点
        while len(self.x_values)<self.numpoints:
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            if x_step==0 and y_step==0:
                continue
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
while True:
    rw=RandomWalk()
    rw.fill_walk()
    point_nums=list(range(rw.numpoints))
    import matplotlib.pyplot as plt
    plt.scatter(rw.x_values,rw.y_values,c=point_nums,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.show()
    ins=raw_input('yes/no')
    if ins=='no':
        break