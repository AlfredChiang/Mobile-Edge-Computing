#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import math
import logging
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='new1.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class Car():
    def __init__(self, index, speed, location, moving_direction, occurrence_time, disappearance_time, frequency):
        self.index = index  # 车辆index
        self.speed = speed  # 车辆速度
        self.location = location  # 车辆位置
        self.moving_direction = moving_direction  # 移动方向
        self.occurrence_time = occurrence_time  # 进入系统时间
        self.disappearance_time = disappearance_time  # 离开系统时间
        self.frequency = frequency  # 车辆CPU频率 GHz

    def getIndex(self):
        return self.index

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def getOccurrence_time(self):
        return self.occurrence_time

    def getDisappearance_time(self):
        return self.disappearance_time

    def getMoving_direction(self):
        return self.moving_direction

    def getFrequency(self):
        return self.frequency * 1000 * 1000 * 1000


def cal(key1, k_n):
    total = 0
    for key in N_t:
        if key == key1:
            continue
        else:
            if abs(k_n[key].getLocation() - k_n[key1].getLocation()) >= 10:
                total += 1 / math.pow(abs(k_n[key].getLocation() - k_n[key1].getLocation()), 4)
    return total


def one():
    car = Car("car", 60.0, 100, 1, 1, 3000, 0)
    car1 = Car("car1", 60.0, 70, 1, 1, 2000, 4.5)
    car2 = Car("car2", 60.0, 50, 1, 1, 3000, 4.5)
    car3 = Car("car3", 60.0, 80, 1, 1, 3000, 5)
    car4 = Car("car4", 60.0, 60, 1, 1, 3000, 5.5)
    car5 = Car("car5", 60.0, 150, 1, 1, 1000, 3)
    car6 = Car("car6", 60.0, 10070, 1, 1001, 2000, 6.5)
    car7 = Car("car7", 60.0, 10115, 1, 1001, 3000, 5)
    car8 = Car("car8", 60.0, 20080, 1, 2001, 3000, 4)

    w_0 = 1000  # Cycles/bit
    A_0 = 10 ** -1.78  # -17.8 #dB
    P = 0.1  # W
    W = 10  # MHz
    sigma_2 = 10 ** -6  # W
    beta_0 = 0.5
    alpha_0 = 0.1

    cardict = {"car1": car1, "car2": car2, "car3": car3, "car4": car4, "car5": car5, "car6": car6, "car7": car7,
               "car8": car8}
    carnum = {"car1": 0, "car2": 0, "car3": 0, "car4": 0, "car5": 0, "car6": 0, "car7": 0, "car8": 0}
    TIME = []
    carnum_UBC = {"car1": 0, "car2": 0, "car3": 0, "car4": 0, "car5": 0, "car6": 0, "car7": 0, "car8": 0}
    TIME_UBC = []
    carnum_VUBC = {"car1": 0, "car2": 0, "car3": 0, "car4": 0, "car5": 0, "car6": 0, "car7": 0, "car8": 0}
    TIME_VUBC = []
    carnum_AdaUBC = {"car1": 0, "car2": 0, "car3": 0, "car4": 0, "car5": 0, "car6": 0, "car7": 0, "car8": 0}
    TIME_AdaUBC = []
    N_t = {}  # t时刻TaV的SeV候选集
    x_t = []
    x_ba_t = []
    k_n = {}
    u_ba_n = {}
    k_n_UBC = {}
    u_ba_n_UBC = {}
    k_n_VUBC = {}
    u_ba_n_VUBC = {}
    k_n_AdaUBC = {}
    u_ba_n_AdaUBC = {}
    t_n = {}

    for i in range(3000):
        #logging.info('--------------------------Periods '+str(i+1)+'--------------------------')
        # x_t 为t时刻数据的大小，均匀分布在[0.2,1]Mbits
        rand = random.uniform(0.2, 1.0)
        x_t.append(rand)
        # x_ba_t 将x_t标准化到[0,1]之间
        if rand <= 0.24:  # x+ = x- and x- = 0.24
            x_ba_t.append(0)
        else:
            x_ba_t.append(1)
        # TaV在系统调度时间范围内时，更新TaV的位置
        if (i + 1) >= car.getOccurrence_time() and (i + 1) <= car.getDisappearance_time():
            speed = car.getSpeed()
            location = car.getLocation()
            location = location + speed * 1000 / 3600.0 * 0.6
            car.setLocation(location)
        # 对于在系统调度时间范围内的SeV，也更新位置
        for key in cardict:
            c = cardict[key]
            if (i + 1) >= c.getOccurrence_time() and (i + 1) <= c.getDisappearance_time():
                speed = c.getSpeed()
                location = c.getLocation()
                location = location + speed * 1000 / 3600.0 * 0.6# + random.uniform(-5,5)
                c.setLocation(location)
                # 判断SeV和TaV的相对位置关系，相对位置要在[10, 200]米的通信范围内，否则无法进行通信。并且车辆的运行方向要相等
                if abs(car.getLocation() - c.getLocation()) >= 10 and abs(car.getLocation() - c.getLocation()) <= 200 and car.getMoving_direction() == c.getMoving_direction():
                    if key not in N_t.keys():  # 如果车辆不在t-1的候选集内，则加入N_t
                        N_t[key] = c
            # 将不符合条件的车辆移除出N_t
            if (i + 1) < c.getOccurrence_time() or (i + 1) > c.getDisappearance_time() or abs(car.getLocation() - c.getLocation()) > 200 or abs(car.getLocation() - c.getLocation()) < 10:
                if key in N_t.keys():
                    N_t.pop(key)
        #for key in N_t:
        #    print(key+' ',end='')
        #print()
            #logging.info(str(N_t[key].getIndex())+' location: '+str(N_t[key].getLocation())+' Speed difference: '+str(abs(N_t[key].getLocation()-car.getLocation())))

        f_t_n = {}
        h_t_n = {}

        # 遍历SeV候选集
        for key in N_t:
            f_t_n[key] = N_t[key].getFrequency() * random.uniform(0.2, 0.5)  #SeV CPU Frequency is randomly distributed from 0.2Fn to 0.5Fn
            h_t_n[key] = A_0 / (math.pow(N_t[key].getLocation() - car.getLocation(), 2)) # wireless channel state
            #logging.info(str(N_t[key].getIndex())+' location: '+str(N_t[key].getLocation())+'  frequency: '+str(f_t_n[key]/1000000)+'  zengyi '+str(h_t_n[key]))

        flag = 0
        time_max = 0
        for key in N_t:
            # 对于新的SeV，先卸载一次，如果某时刻同时有多个新SeV，则全部试探一次。
            if key not in k_n.keys():
                flag = 1
                k_t_n = []
                u_ba_t_n = []
                k_t_n.append(1)
                k_n[key] = k_t_n
                k_n_UBC[key] = k_t_n
                k_n_VUBC[key] = k_t_n
                k_n_AdaUBC[key] = k_t_n
                # 计算上行和下行的传输速率  这里计算还有问题
                r_u_t_n = W * math.log(1 + (P * h_t_n[key]) / (sigma_2), 2) * 1000000
                r_d_t_n = r_u_t_n
                u_ba_t_n.append(1 / r_u_t_n + alpha_0 / r_d_t_n + w_0 / f_t_n[key])
                u_ba_n[key] = u_ba_t_n
                u_ba_n_UBC[key] = u_ba_t_n
                u_ba_n_VUBC[key] = u_ba_t_n
                u_ba_n_AdaUBC[key] = u_ba_t_n
                t_n[key] = i + 1
                if time_max<(1 / r_u_t_n + alpha_0 / r_d_t_n + w_0 / f_t_n[key])*x_t[i]*1024*1024:
                    time_max = (1 / r_u_t_n + alpha_0 / r_d_t_n + w_0 / f_t_n[key])*x_t[i]*1024*1024
                #logging.info(str(key) + ' ' + str(u_ba_n[key][-1]) + ' k_n: ' + str(k_n[key][-1])+' t_n: '+str(t_n[key])+' t t'+str(1 / r_u_t_n + alpha_0 / r_d_t_n)+' z t'+str(w_0 / f_t_n[key]))
        u_jian_n = {}
        u_jian_n_UBC = {}
        u_jian_n_VUBC = {}
        u_jian_n_AdaUBC = {}
        if flag == 1:# 如果已经卸载过一次，则无需再卸载，否则，会执行学习算法，选择一个SeV进行卸载
            #print(time_max)
            TIME.append(time_max)
            TIME_UBC.append(time_max)
            TIME_VUBC.append(time_max)
            TIME_AdaUBC.append(time_max)
            continue
        else:
            # u_ba_n_max = 0
            # for key in N_t:
            #     if u_ba_n_max < u_ba_n[key][-1]:
            #         u_ba_n_max = u_ba_n[key][-1]
            for key in N_t:
            	
            	u_jian_n[key] = u_ba_n[key][-1] - math.sqrt(beta_0 * (1 - x_ba_t[i]) * math.log(i + 1 - t_n[key]) / k_n[key][-1])/1000000
            	u_jian_n_UBC[key] = u_ba_n[key][-1] - math.sqrt(beta_0 * math.log(i + 1) / k_n[key][-1])/1000000
            	u_jian_n_VUBC[key] = u_ba_n[key][-1] - math.sqrt(beta_0 * math.log(i + 1 - t_n[key]) / k_n[key][-1])/1000000
            	u_jian_n_AdaUBC[key] = u_ba_n[key][-1] - math.sqrt(beta_0 * (1 - x_ba_t[i]) * math.log(i + 1) / k_n[key][-1])/1000000

        a_t = min(u_jian_n, key=u_jian_n.get)
        r_u_t_at = W * math.log(1 + (P * h_t_n[a_t]) / (sigma_2), 2) * 1000000
        d_sum = (1 / r_u_t_at + alpha_0 / r_u_t_at + w_0 / f_t_n[a_t]) * x_t[i] * 1024 * 1024

        a_t_UBC = min(u_jian_n_UBC, key=u_jian_n_UBC.get)
        r_u_t_at_UBC = W * math.log(1 + (P * h_t_n[a_t_UBC]) / (sigma_2), 2) * 1000000
        d_sum_UBC = (1 / r_u_t_at_UBC + alpha_0 / r_u_t_at_UBC + w_0 / f_t_n[a_t_UBC]) * x_t[i] * 1024 * 1024
        
        a_t_VUBC = min(u_jian_n_VUBC, key=u_jian_n_VUBC.get)
        r_u_t_at_VUBC = W * math.log(1 + (P * h_t_n[a_t_VUBC]) / (sigma_2), 2) * 1000000
        d_sum_VUBC = (1 / r_u_t_at_VUBC + alpha_0 / r_u_t_at_VUBC + w_0 / f_t_n[a_t_VUBC]) * x_t[i] * 1024 * 1024

        a_t_AdaUBC = min(u_jian_n_AdaUBC, key=u_jian_n_AdaUBC.get)
        r_u_t_at_AdaUBC = W * math.log(1 + (P * h_t_n[a_t_AdaUBC]) / (sigma_2), 2) * 1000000
        d_sum_AdaUBC = (1 / r_u_t_at_AdaUBC + alpha_0 / r_u_t_at_AdaUBC + w_0 / f_t_n[a_t_AdaUBC]) * x_t[i] * 1024 * 1024

        carnum[a_t] += 1
        TIME.append(d_sum)
        
        carnum_UBC[a_t_UBC] += 1
        TIME_UBC.append(d_sum_UBC)

        carnum_VUBC[a_t] += 1
        TIME_VUBC.append(d_sum_VUBC)

        carnum_AdaUBC[a_t] += 1
        TIME_AdaUBC.append(d_sum_AdaUBC)

        u_ba_n[a_t].append((u_ba_n[a_t][-1] * k_n[a_t][-1] + d_sum / (x_t[i] * 1024 * 1024)) / (k_n[a_t][-1] + 1))
        k_n[a_t].append(k_n[a_t][-1] + 1)

        u_ba_n_UBC[a_t_UBC].append((u_ba_n_UBC[a_t_UBC][-1] * k_n_UBC[a_t_UBC][-1] + d_sum_UBC / (x_t[i] * 1024 * 1024)) / (k_n_UBC[a_t_UBC][-1] + 1))
        k_n_UBC[a_t_UBC].append(k_n_UBC[a_t_UBC][-1] + 1)

        u_ba_n_VUBC[a_t_VUBC].append((u_ba_n_VUBC[a_t_VUBC][-1] * k_n_VUBC[a_t_VUBC][-1] + d_sum_VUBC / (x_t[i] * 1024 * 1024)) / (k_n_VUBC[a_t_VUBC][-1] + 1))
        k_n_VUBC[a_t_VUBC].append(k_n_VUBC[a_t_VUBC][-1] + 1)

        u_ba_n_AdaUBC[a_t_AdaUBC].append((u_ba_n_AdaUBC[a_t_AdaUBC][-1] * k_n_AdaUBC[a_t_AdaUBC][-1] + d_sum_AdaUBC / (x_t[i] * 1024 * 1024)) / (k_n_AdaUBC[a_t_AdaUBC][-1] + 1))
        k_n_AdaUBC[a_t_AdaUBC].append(k_n_AdaUBC[a_t_AdaUBC][-1] + 1)
        #for key in N_t:
        #    logging.info(str(key)+' '+str(u_jian_n[key])+' k_n: '+str(k_n[key][-1])+' t_n: '+str(t_n[key])+'   '+str(math.sqrt(beta_0 * (1 - x_ba_t[i]) * math.log(i + 1 - t_n[key]) / k_n[key][-1])))
    return TIME,TIME_UBC,TIME_VUBC,TIME_AdaUBC

# if __name__ == "__main__":
#     carnum, TIME = one()
#     print(carnum)

if __name__ == "__main__":

    TIME = []
    TIME_UBC = []
    TIME_VUBC = []
    TIME_AdaUBC = []

    n = 10000

    for i in range(3000):
        TIME.append(0)
        TIME_UBC.append(0)
        TIME_VUBC.append(0)
        TIME_AdaUBC.append(0)
    for i in range(n):
        print(i)
        Time,Time_UBC,Time_VUBC,Time_AdaUBC = one()
        #print(carnum)
        for j in range(len(Time)):
            TIME[j] += Time[j]
            TIME_UBC[j] += Time_UBC[j]
            TIME_VUBC[j] += Time_VUBC[j]
            TIME_AdaUBC[j] += Time_AdaUBC[j]

    for j in range(len(Time)):
        TIME[j] = TIME[j] / n
        TIME_UBC[j] = TIME_UBC[j] / n
        TIME_VUBC[j] = TIME_VUBC[j] / n
        TIME_AdaUBC[j] = TIME_AdaUBC[j] / n
    x = np.arange(0, 3000)
    l1 = plt.plot(x, TIME, 'r--', label='time',linewidth = '1')
    l2 = plt.plot(x, TIME_UBC, 'go-', label='time_UBC',linewidth = '1')
    l3 = plt.plot(x, TIME_VUBC, 'b^-', label='time_VUBC',linewidth = '1')
    l4 = plt.plot(x, TIME_AdaUBC, 'y+-', label='time_AdaUBC',linewidth = '1')
    plt.title('Time Delay')
    plt.xlabel('Average time /s')
    plt.ylabel('Time Period t')
    plt.legend()
    plt.savefig('t.png')
    plt.show()




