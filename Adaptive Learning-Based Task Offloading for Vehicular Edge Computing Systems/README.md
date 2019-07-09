# Mobile-Edge-Computing

## Adaptive Learning-Based Task Offloading for Vehicular Edge Computing Systems 车辆边缘计算系统中基于自适应学习的任务卸载

[文章链接](https://ieeexplore.ieee.org/document/8627987)

### Abstract
车辆边缘计算(VEC)系统集成了车辆的计算资源，为其他车辆和行人提供任务卸载的计算服务。然而，车辆任务卸载环境是动态的、不确定的，网络拓扑结构、无线信道状态和计算工作量变化很快。这些不确定性给任务卸载带来了额外的挑战。在本工作中，我们考虑了车辆间的任务卸载问题，并提出了一种解决方案，使车辆在卸载计算任务时能够学习相邻车辆的卸载延迟性能。我们设计了一种基于multi-armed bandit（MAB）理论的基于自适应学习的任务卸载（ALTO）算法，以最小化平均卸载延迟。ALTO以分布式方式工作，不需要频繁的状态交换，并通过输入感知和事件感知进行增强，以适应动态环境。结果表明，该算法具有sublinear learning regret。在synthetic scenario和realistic highway scenario下进行了大量的仿真，结果表明，与现有的基于upper confidence bound的学习算法相比，该算法具有较低的时延性能，平均时延降低了30%。

### Introduction
每个任务可能被多个SeVs处理，而一个关键的挑战是在动态VEC环境中缺少SeVs的准确状态信息。由于车辆的运动，网络拓扑结构和无线信道状态变化很快，SeVs的计算工作量随时间波动。这些因素很难建模或预测，因此TaV事先不知道哪个SeV在延迟性能方面表现得最好。

我们的解决方案是边学习边卸载，TaV能够在卸载任务时学习延迟性能。具体来说，我们采用了multi-armed bandit(MAB)框架来设计我们的任务卸载算法。经典MAB问题旨在平衡学习过程中的探索和利用权衡:探索不同的候选行为，从而很好地估计它们的回报分布，同时利用学到的信息来选择经验上最优的行为。基于upper confidence bound(UCB)如UCB1和UCB2被提出具有较强的性能保证。

然而，在我们的任务卸载问题中，车辆的运动导致了一个动态的候选SeV集，每个任务的工作量都是时变的，导致探索次优行为的成本是变化的。这些因素还没有被现有的MAB方案所解决，这促使我们在车辆任务卸载场景中特别适应MAB框架。我们的主要贡献包括:

* 我们提出了一种基于MAB理论的基于自适应学习的任务卸载（ALTO）算法，以指导TaV的任务卸载并最小化平均卸载延迟。 ALTO算法以分布式方式工作，使TaV能够在卸载任务时学习候选SeV的延迟性能。 该算法计算复杂度低，不需要交换准确的状态信息，如信道状态和车辆间的计算工作量，因此易于在真实的VEC系统中实现。

* 通过提出的ALTO算法增强了两种自适应性：input-awareness和occurrence-awareness，通过根据任务的工作量和SeV的出现时间调整探索权重。证明ALTO能够有效地平衡动态车辆环境下的探索和利用，并具有sublinear learning regret。

* 在synthetic scenario和realistic highway scenario下进行了大量的仿真。结果表明，该算法具有较低的时延性能，为关键设计参数的设置提供了指导。