# Mobile-Edge-Computing

## Cooperative Task Scheduling for Computation Offloading in Vehicular Cloud

[文章链接](https://ieeexplore.ieee.org/document/8451923)

### Abstract


### I. INTRODUCTION


### V. SIMULATION RESULTS

#### A. Vehicle and Mission Simulation
为了说明车载云中的计算卸载过程，我们从模拟中随机选择一个场景，其中15个车辆组合在一起作为VC来卸载附近EC的计算任务。图3示出了这些车辆在36 tu的持续时间内的移动（即，15个连续的调度时隙St）。  
观察到BS的覆盖范围内的每个车辆的接触间隔是不同的，这反映了VC中这些车载计算资源的不稳定性。为了保证卸载任务完成后，任务应该在处理车辆的接触的时间间隔内完成。图4显示了卸载计算任务的逻辑拓扑，到达时间和计算工作量。据观察，在模拟期间有5个任务被卸载到VC。第一个任务是在2tu卸载，并且有2个任务分别在3tu和4tu卸载到VC。 每个任务分为4个具有不同计算工作量的任务。这些任务的结构由第II-C节中提到的三种基本逻辑拓扑组成。任务m1和m5是单输入结构，而其他三个任务是多输入结构。资源的不稳定性（图3）和任务的相互依赖性（图4）都将影响卸载决策。在下面的小节中，我们将在卸载决策，响应时间和系统稳定性方面展示所提出的基于MGA的方案的性能。
![image](https://github.com/qpointwang/Mobile-Edge-Computing/blob/master/Cooperative-Task-Scheduling-for-Computation-Offloading-in-Vehicular-Cloud/f3.png)
![image](https://github.com/qpointwang/Mobile-Edge-Computing/blob/master/Cooperative-Task-Scheduling-for-Computation-Offloading-in-Vehicular-Cloud/f4.png)

#### B. Offloading Decisions
图5显示了基于贪婪和MGA的方案所做的卸载决策。从图5（a）可以看出，通过Greedy方案，VC系统总是分配最早的调度时隙，以实现每个任务的最短响应时间。然而，贪婪计划缺乏全球概念，这可能导致局部最优。与图5（b）中的MGA方案相比，从两种方案获得的任务m1和m3的响应时间是相同的，而MGA方案的m2的响应时间大于贪婪方案的响应时间。 对于任务m4和m5，MGA方案的结果优于贪婪方案的结果。从图5（a）可以看出，即使贪婪方案的m2的响应时间短于MGA方案的响应时间，m2的资源分配使得资源不可用于m4和m5，这导致这两个任务的排队时间更长。
![image](https://github.com/qpointwang/Mobile-Edge-Computing/blob/master/Cooperative-Task-Scheduling-for-Computation-Offloading-in-Vehicular-Cloud/f5.png)

图6（a）示出了所提出的基于MGA的调度方案的效率。 贪婪方案获得的平均响应时间为16tu，而基于MGA的方案的结果为14tu，减少了12.5％。为了进一步证明所提出的基于MGA的方案的效率，图6（b）显示了m4中任务的排队，通信和处理时间，这是与其他任务相比最复杂的任务（图4）。对于基于MGA的方案，第一任务b41被分配给第四调度时隙S4中的车辆v10。
![image](https://github.com/qpointwang/Mobile-Edge-Computing/blob/master/Cooperative-Task-Scheduling-for-Computation-Offloading-in-Vehicular-Cloud/f6.png)


$$a + b$$

# 机器学习-如何在github上写数学公式

居中格式: $$xxx$$
$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
靠左格式: $\(xxx\)$

$\(x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\)$
测试
$$\frac{7x+5}{1+y^2}$$
$$\(l(x_i) = - \log_2 P(x_i)\)$$

$${D_n}=\left[{\sum\limits_{k=1,b_i^k\in{\mathcal{B}^k}}^K{\sum\limits_{h=1}^H{\left({{c_{i,n,h}}+{p_{i,n,h}}}\right){x_{i,n,h}}}}}\right]{\left({{\mu_n}-{\delta_n}}\right)^{-1}}\tag{25}$$


![](http://latex.codecogs.com/gif.latex?\\frac{1}{1+sin(x)})


![](http://latex.codecogs.com/gif.latex?\\x=frac{1}{1+sin(x)})


![](http://latex.codecogs.com/gif.latex?\\frac{\\partialJ}{\\partial\\theta_k^{(j)}}=\\sum_{i:r(i,j)=1}{\\big((\\theta^{(j)})^Tx^{(i)}-y^{(i,j)}\\big)x_k^{(i)}}+\\lambda \\xtheta_k^{(j)})

![](http://latex.codecogs.com/gif.latex?\\{D_n}=\left[{\sum\limits_{k=1,b_i^k\in{\mathcal{B}^k}}^K{\sum\limits_{h=1}^H{\left({{c_{i,n,h}}+{p_{i,n,h}}}\right){x_{i,n,h}}}}}\right]{\left({{\mu_n}-{\delta_n}}\right)^{-1}}\tag{25})