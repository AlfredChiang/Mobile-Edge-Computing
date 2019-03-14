import random
import math
import logging
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='w',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
class Car():
    def __init__(self,index, speed, location, moving_direction, occurrence_time, disappearance_time, frequency):
        self.index = index #车辆index
        self.speed = speed #车辆速度
        self.location = location #车辆位置
        self.moving_direction = moving_direction #移动方向
        self.occurrence_time = occurrence_time #进入系统时间
        self.disappearance_time = disappearance_time #离开系统时间
        self.frequency = frequency #车辆CPU频率 GHz
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
        return self.frequency*1000*1000*1000
def cal(key1, k_n):
    total = 0
    for key in N_t:
        if key == key1:
            continue
        else:
            if abs(k_n[key].getLocation() - k_n[key1].getLocation())>=10:
                total += 1/math.pow(abs(k_n[key].getLocation()-k_n[key1].getLocation()),4)
    return total



def one():
    car = Car("car", 60.0, 100, 1, 1, 3000, 0)
    car1 = Car("car1", 60.0, 10, 1, 1, 2000, 3.5)
    car2 = Car("car2", 60.0, 50, 1, 1, 3000, 4.5)
    car3 = Car("car3", 60.0, 80, 1, 1, 3000, 5)
    car4 = Car("car4", 60.0, 60, 1, 1, 3000, 5.5)
    car5 = Car("car5", 60.0, 150, 1, 1, 1000, 3)
    car6 = Car("car6", 60.0, 10020, 1, 1001, 2000, 6.5)
    car7 = Car("car7", 60.0, 10010, 1, 1001, 3000, 6)
    car8 = Car("car8", 60.0, 20000, 1, 2001, 3000, 4)

    w_0 = 1000 #Cycles/bit
    A_0 = 10**-1.78#-17.8 #dB
    P = 0.1 #W
    W = 0.1 #MHz
    sigma_2 = 10**-13 #W
    beta_0 = 0.5
    alpha_0 = 0.1

    cardict = {"car1":car1, "car2":car2, "car3":car3, "car4":car4, "car5":car5, "car6":car6, "car7":car7, "car8":car8}
    carnum = {"car1":0, "car2":0, "car3":0, "car4":0, "car5":0, "car6":0, "car7":0, "car8":0}
    TIME = []
    N_t = {}
    x_t = []
    x_ba_t = []
    k_n = {}
    u_ba_n = {}
    t_n = {}

    for i in range(3000):
        #logging.info('--------------------------Periods '+str(i+1)+'--------------------------')
        # x_t 为t时刻数据的大小，均匀分布在[0.2,1]Mbits
        rand = random.uniform(0.2, 1.0)
        x_t.append(rand)
        # x_ba_t 将x_t标准化到[0,1]之间
        if rand<=0.24:  #x+ = x- and x- = 0.24
            x_ba_t.append(0)
        else:
            x_ba_t.append(1)
        #logging.info('x_t '+str(rand)+'        x_ba_t '+str(x_ba_t[i]))
        if (i+1) >= car.getOccurrence_time() and (i+1) <= car.getDisappearance_time():
            speed = car.getSpeed()
            location = car.getLocation()
            location = location + speed*1000/3600.0*0.6
            car.setLocation(location)
            #logging.info(str(car.getIndex())+' location: '+str(car.getLocation()))
        
        for key in cardict:
            c = cardict[key]
            if (i+1) >= c.getOccurrence_time() and (i+1) <= c.getDisappearance_time():
                speed = c.getSpeed()
                location = c.getLocation()
                location = location + speed*1000/3600.0*0.6
                c.setLocation(location)
                if abs(car.getLocation() - c.getLocation()) <= 200 and car.getMoving_direction() == c.getMoving_direction():
                    if key not in N_t.keys():#N_t.has_key(key):
                        N_t[key]=c
            if (i+1) < c.getOccurrence_time() or (i+1) > c.getDisappearance_time() or abs(car.getLocation() - c.getLocation()) >= 200:
                if key in N_t.keys():
                    N_t.pop(key)
        #for key in N_t:
        #    logging.info(str(N_t[key].getIndex())+' location: '+str(N_t[key].getLocation()))
        
        f_t_n = {}
        h_t_n = {}
        
        # 遍历候选集
        for key in N_t:
            f_t_n[key] = N_t[key].getFrequency()*random.uniform(0.5, 0.5)
            h_t_n[key] = A_0/(math.pow(N_t[key].getLocation()-car.getLocation(),2))
            #logging.info(str(N_t[key].getIndex())+' location: '+str(N_t[key].getLocation())+'  frequency: '+str(f_t_n[key])+'  zengyi '+str(h_t_n[key]))

        flag = 0
        for key in N_t:
            if key not in k_n.keys():
                flag = 1
                k_t_n = []
                u_ba_t_n = []
                k_t_n.append(1)
                k_n[key] = k_t_n
                
                #r_u_t_n = W*math.log(1+(P*h_t_n[key])/(sigma_2+P*A_0*cal(key,N_t)),2)*1000000
                r_u_t_n = W*math.log(1+(P*h_t_n[key])/(sigma_2),2)*1000000

                r_d_t_n = r_u_t_n
                print(h_t_n[key],A_0,P*h_t_n[key]/(sigma_2),math.log(1+(P*h_t_n[key])/(sigma_2),2))
                print(key,'总延迟',x_t[i]*1024*1024*(1/r_u_t_n+alpha_0/r_d_t_n+w_0/f_t_n[key]),'s     传输速率',r_u_t_n/1024/1024,'Mb/s')
                print(key,'传输延迟',x_t[i]*1024*1024*(1/r_u_t_n+alpha_0/r_d_t_n),'    执行延迟',x_t[i]*1024*1024*w_0/f_t_n[key])
                u_ba_t_n.append(1/r_u_t_n+alpha_0/r_d_t_n+w_0/f_t_n[key])
                u_ba_n[key] = u_ba_t_n
                t_n[key] = i+1

        u_jian_n = {}
        if flag == 1:
            continue
        else:
            u_ba_n_max = 0
            for key in N_t:
                if u_ba_n_max < u_ba_n[key][-1]:
                    u_ba_n_max = u_ba_n[key][-1]
            for key in N_t:
                u_jian_n[key] = u_ba_n[key][-1]/u_ba_n_max - math.sqrt(beta_0*(1-x_ba_t[i])*math.log(i+1-t_n[key])/k_n[key][-1])
                # print(u_ba_n[key][-1]/u_ba_n_max - math.sqrt(beta_0*(1-x_ba_t[i])*math.log(i+1-t_n[key])/k_n[key][-1]))
                # print(u_ba_n[key][-1]/u_ba_n_max,math.sqrt(beta_0*(1-x_ba_t[i])*math.log(i+1-t_n[key])/k_n[key][-1]))

        a_t = min(u_jian_n,key=u_jian_n.get)
        # print(a_t,x_ba_t[i],math.sqrt(beta_0*(1-x_ba_t[i])*math.log(i+1-t_n[key])/k_n[key][-1]),i+1-t_n[key],math.log(i+1-t_n[key]))
        
        #r_u_t_at = W*math.log(1+(P*h_t_n[a_t])/(sigma_2+P*A_0*cal(a_t,N_t)),2)*1000000
        r_u_t_at = W*math.log(1+(P*h_t_n[a_t])/(sigma_2),2)*1000000
        # print('dddddddddd',r_u_t_at,f_t_n[a_t],N_t[a_t].getLocation(),car3.getLocation(),(P*h_t_n[a_t])/(sigma_2+P*A_0*cal(a_t,N_t)),P*h_t_n[a_t],cal(a_t,N_t))
        d_sum = (1/r_u_t_at+alpha_0/r_u_t_at+w_0/f_t_n[a_t]) * x_t[i]*1024*1024
        #logging.info('Optimal '+a_t+'   time '+str(d_sum))
        carnum[a_t] += 1
        TIME.append(d_sum)
        u_ba_n[a_t].append((u_ba_n[a_t][-1]*k_n[a_t][-1]+d_sum/(x_t[i]*1024*1024))/(k_n[a_t][-1]+1))
        k_n[a_t].append(k_n[a_t][-1]+1)

    return TIME

        
if __name__ == "__main__":
	#one()
	
	TIME = []
	for i in range(2997):
		TIME.append(0)
	for i in range(100):
		print(i)
		Time = one()
		for j in range(len(Time)):
			TIME[j] += Time[j]
	for j in range(len(Time)):
		TIME[j] = TIME[j] /100
	x = np.arange(0,2997)
	l1=plt.plot(x,TIME,'r--',label='time')
	plt.title('Time Delay')
	plt.xlabel('Average time /s')
	plt.ylabel('Time Period t')
	plt.legend()
	plt.show()
	
