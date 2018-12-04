# Mobile-Edge-Computing

## Cooperative Task Scheduling for Computation Offloading in Vehicular Cloud

[文章链接](https://ieeexplore.ieee.org/document/8451923)

### Abstract
汽车工业中的技术演变，尤其是连接和自动车辆的发展，已经赋予车辆更多的计算，存储和传感资源。有效利用这些资源的必要性导致车载云计算（VCC）的愿景，其可以从边缘或远程云卸载计算任务以提高整体效率。在本文中，我们研究了通过车载云（VC）计算卸载的问题，其中来自边缘云的计算任务可以被卸载并由VC中的车辆协同执行。具体而言，计算任务进一步划分为具有相互依赖性的计算任务，并在VC中的不同车辆中执行以最小化总体响应时间。为了表征由高车辆移动性导致的计算资源的不稳定性，利用了关注车辆停留时间的移动性模型。考虑到车载计算能力的异构性和计算任务的相互依赖性，我们制定了一个NP难的任务调度优化问题。对于低复杂度，设计了基于改进遗传算法的调度方案，其中使用整数编码而不是二进制编码，并且定义和使用亲属以避免不可行解。此外，针对VC内的一些车辆离线的情况，提出了基于任务负载的VCC系统稳定性分析。数值结果表明，该方案可以显着提高计算资源的利用率，同时保证低延迟和系统稳定性。

### I. INTRODUCTION
#### B. Main Contributions
我们通过联合考虑资源的不稳定性，车辆计算能力的异构性以及计算任务的相互依赖性，提出了一种有效的VC任务调度方案。 我们的主要贡献总结如下。

* 针对VC的独特特征，如计算任务的不稳定性，异构性和相互依赖性，提出了VC中计算卸载的协同任务调度方案，该方案被制定为NP-hard调度问题。

* 为了表征车载计算资源的不稳定性，开发了一种关注停留时间的车辆移动模型，其中停留时间可以直接用于卸载决策。

* 我们设计并实现了一种基于遗传的启发式算法来解决所述的NP难调度问题，从而降低了问题的复杂性，同时提高了车载资源的利用率。

### System Model and Problem Formulation
我们考虑蜂窝网络中的VC辅助计算卸载方案，其中${N}$ vehicles $\mathcal{V}=\left\lbrace{{v_1},\ldots,{v_N}}\right\rbrace$

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