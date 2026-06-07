# OPEN Data-driven automated job shop scheduling optimization considering AGV obstacle avoidance 

Qi Tang \& Huan Wang ${ }^{1 / 2}$

The production stage of an automated job shop is closely linked to the automated guided vehicle (AGV), which needs to be planned in an integrated manner to achieve overall optimization. In order to improve the collaboration between the production stages and the AGV operation system, a two-layer scheduling optimization model is proposed for simultaneous decision making of batching problems, job sequences and AGV obstacle avoidance. Under the AGV automatic path seeking mode, this paper adopts a data-driven Bayesian network method to portray the transportation time of AGVs based on the historical operation data to control the uncertainty of the transportation time of AGVs. Meanwhile, a time window is established to control the risk of AGV delay, and a data-driven Bayesian network is constructed to optimize the two-layer scheduling model of automated job shop and AGV. To solve the model, we design an improved particle swarm algorithm combining genetic operators, crossover operators and elite retention operator. The results show that the model in this paper can effectively improve the collaboration between the production stage and AGV operation system within the shop floor, and successfully solve the actual operation scale case to enhance the effectiveness of the production and transportation system.

Keywords Automated job shop, Production scheduling, Obstacle avoidance, Data-driven
With the development of intelligent manufacturing, automated job shop has become a research topic for job shop scheduling problems. AGV is the main horizontal transportation equipment in the job shop under various environments. Its reasonable decision-making transportation route and obstacle avoidance play a crucial role in improving the overall transportation efficiency of the job shop and reducing the energy consumption of horizontal transportation operations. During a production run, we are faced with a wide variety of products, each with different production times and quantities. The proper scheduling of products directly affects the completion time and transportation time of the production. Therefore, considering AGV decision making and job shop scheduling optimization problems with energy savings is an important issue for research in manufacturing industries. Scholars have conducted a great deal of research on AGVs, mainly focusing on the areas of task assignment and path planning for AGVs. In the research of task assignment of AGVs, the main focus is to match AGVs for materials or semi-finished products to be transported, and to solve the problem by building mathematical planning models ${ }^{3}$, which sometimes may also consider equipment failures and safety performance ${ }^{2}$. In the field of path planning for AGVs, the vehicle path problem is mainly studied to generate transportation paths. Mostly, mathematical planning models, behavioral models and reinforcement learning are applied to solve the problem and plan the transportation paths of AGVs in advance. Zhang, LX et al. consider both the scheduling problem and the energy consumption problem of AGVs, and propose a new approach using deep learning to solve the problem ${ }^{5}$; Zhou, PF et al. designed a reinforcement learning algorithm for AGV path selection based on the selection of action strategies ${ }^{4} ; \mathrm{Wu}, \mathrm{MP}$ et al. designed a path planning model for three operation modes based on the A -star $\left(\mathrm{A}^{*}\right)$ algorithm to solve AGV path planning and real-time random obstacle avoidance ${ }^{5}$; Zhou, PF et al. found the shortest route for AGVs in a guided path network based on the realtime state of the AGVs. And they designed a reinforcement learning path algorithm based on selection action strategy ${ }^{6}$. With the landing reference of automatic driving technology, AGV can dynamically find the optimal path with high autonomy, which further enriches the path planning method and improves the applicability of AGV in multiple fields.

School of Management, Shenyang University of Technology, Shenyang 110870, China. ${ }^{1 / 2}$ email: huanwang0221@163.com

The job shop scheduling problem is mainly considered as a batching and scheduling problem in the context of operations research optimization. Initially, production scheduling research mainly addressed job assignment and production sequencing problems, and these were mostly deterministic problems that were studied^{7}. However, uncertain variables occur, such as processing times, transportation times, and jams, which become a range or even change in real time. The problem of dynamic production scheduling arises and it can be more flexible to cope with changes and unexpected events^{8}.Considering the situation, the transportation time of materials and semi-finished products is a part of the production that cannot be ignored. The widespread use of mobile robots plays a key role in supporting equipment processing and material transportation, which directly affects the completion time^{9}.AGVs have been widely used as material transportation equipment to support many production environments, automated storage, retrieval systems and port terminals. Similarly, pharmaceutical plants generally use automated guided vehicles for this transportation purpose. AGV decision-making considerations add a new layer of complexity to the job shop scheduling problem^{10}. The loading and unloading times of the AGVs need to be accurately matched to the production start and end times of the production equipment, which makes the production equipment and the AGVs strongly coupled. As a result, job shop coscheduling with AGVs has attracted a lot of attention. Job shop scheduling primarily involves decision-making on production batch and production sequencing. For example, Wang, ZC et al. established a constrained hybrid flow shop scheduling model by considering a real-world scenario. And a discrete artificial ant colony algorithm is designed to solve the model, and the effectiveness of the algorithm is verified by comparing the job scheduling results of the experimental cases^{11}; Brandimarte, P et al. dealt with a just-in-time scheduling job shop problem in which setup times and completion times related to timing sequence are handled. The authors developed new destroy and repair operators that take advantage of the problem itself^{12}. AGV decision-making mainly studies the path selection problem. When dealing with the AGV decision-making and job shop scheduling synergy problem, most of the research essentially combines the vehicle path and shop scheduling problems mechanically or the research focuses on the task assignment of AGVs^{13}. Some of the commonly used methods are mixed integer programming and Markov decision making. Guan, T et al. constructed a multi-objective rescheduling model by taking buffer capacity and AGV as resource constraints^{14,15}. When AGVs are equipped with driverless technology, they have a certain degree of autonomy. Driving flexibility is greatly improved and driving uncertainty is further increased. Most of the previous studies could not judge the uncertainty. And the mathematical methods of uncertainty used are difficult to capture the exact distribution of AGV transportation time. Yang, Y et al. proposed a two-layer model for handling equipment coordination and integrated scheduling of AGV routes^{16}; Castilla-Rodríguez, I et al. investigated the AGV logistics transportation and scheduling problem using an uncertainty model^{17}. Although some scholars have considered the transportation time uncertainty of AGVs, they mostly solve the stochastic problem by adding environmental constraints, mathematical probability and triangular fuzzy sets. Du, BG et al. proposed a similarity coefficient mutation operator based on probability matrix to improve the algorithm's solution performance^{18}; Cai, L et al. improved the algorithm using a new congestion distance operator with cosine distance to improve the diversity of problem solutions^{19}. These do not satisfy the need for AGVs to learn from real-time data in order to achieve AGV autonomy. AGV path decisions for job shop autonomy are not equivalent to variants of vehicle paths. Because job shop scheduling events occur in closed production halls where collisions and congestion are inevitable, the problem of decision processing for job shop AGVs focuses on obstacle avoidance or prediction^{20}.

In a recent study, there are various research efforts on job shop scheduling and related problems. For example, Han, XQ et al. designed a two-population genetic algorithm to solve the FJSP-AGV problem, in which two different decoding methods were proposed^{21}. Amirteimoori, A et al. investigated the job shop problem considering AGV eligibility and conflict-free AGV path selection and proposed a new parallel two-step decomposition heuristic and a hybrid linear programming algorithm^{22}. Amirteimoori, A et al. investigated the simultaneous scheduling problem of job scheduling and AGVs in a flexible job shop system with a mixed integer planning model. The authors focused on the effectiveness of parallel computing in order to reduce computation time^{23}. Chaudhry, IA et al. considered the problem of transportation between equipment and showed a Microsoft Excel(R) spreadsheet-based solution for the problem^{24}. Homayouni, SM et al. proposed novel solutions to study the extension of the flexible job shop problem and the transportation job shop problem. Considering the flexible dynamic problem and transportation together, a modular structure is designed that can be quickly adapted to solve similar scheduling problems^{25}. Fontes, DBMM et al. studied the job shop problem with a transportation problem and designed a novel hybrid particle swarm algorithm to solve the small-scale problem^{26}.There are many kinds of methods to solve the integrated scheduling problem, but most of the theoretical methods do not consider the AGV obstacle avoidance problem in the scheduling process. Adding the AGV obstacle avoidance problem on top of the complex job shop scheduling will greatly increase the difficulty of the algorithm and the computational cost. And transforming the AGV obstacle avoidance problem into a Bayesian network prediction problem can reduce the complexity of the integration problem. When unexpected obstacle events occur during production, most studies choose to pause production for rescheduling, which does not allow for learning from historical empirical data and does not allow for just-in-time production control. However, the production of some products is a continuous process and emergency stops in the production process are not allowed, otherwise the purity of the product will be affected or defective products will appear. Therefore, we use an automated job shop scheduling model based on Bayesian networks to predict the occurrence of uncertain events in advance and minimize the risk of job planning.

Based on this, this paper constructs a data-driven two-layer optimization model for automated job shop scheduling and AGV decision-making with Bayesian network inference. It considers the simultaneous decision making of job scheduling and AGV obstacle avoidance problem under the uncertainty of transportation time. At the same time, the delay time of AGVs is controlled and the collaboration of the system is improved. In this case, the decision-making sequence of operations belongs to the upper level problem, where the transportation

decision environment is determined and it needs to be solved before the delayed exposure of the AGV transportation time; while the AGV decision-making belongs to the lower layer problem, where it is solved under the production scheduling results and after the delayed exposure of the uncertain transportation time. In this paper, we portray the impact of AGV uncertainty on the production system through a data-driven Bayesian network, and then pass the second-layer uncertainty to the first-layer problem to solve the data-driven two-layer optimization model. In addition, there are not many studies that consider the job shop scheduling problem with AGV decision making while developing sustainable development with reduced energy consumption^{27}. Previous research on energy consumption has mainly focused on equipment design concepts, and fewer articles have been written from the perspective of optimizing scheduling schemes to reduce energy consumption^{28}. So, we also study the multidimensional objective problem with its simultaneous minimization of completion time and minimization of energy consumption. Compared to previous studies, this paper has the following academic and practical contributions:In this paper, a data-driven two- layer automated job shop scheduling model is developed. Based on Bayesian network inference theory, it minimizes the obstacle encounter probability of the lower layer AGV path nodes, thus assisting the total objective of the production system to be optimal.Mathematical methods such as Beta distribution are used to obtain the prior probability of the data and to train the parameters so as to infer the probability of the network nodes encountering obstacles.Use job shop scheduling models for batching and job sequencing of production products to minimize production completion time and energy consumption.An Improved Multi-Objective Particle Swarm Algorithm (IMMOPSO) is designed for the model developed in this paper. The model in this paper is solved using the improved algorithm and the IMMOPSO algorithm is compared with the NSGA-II algorithm to demonstrate the reliability of the IMMOPSO algorithm solution.Completing the experimental simulation comparisons, this paper provides accurate production completion time and time connection between stages for manufacturing companies.

The rest of this article is arranged as follows. Sect. Problem description presents the core problem and assumptions of job shop considering transportation time to be studied in this paper. Sect. Mathematical model presents the construction and main parts of the mathematical model. Sect. Applying IMMOPSO to Solve Data-Driven Automated JSP presents the model solution, evaluation and result analysis. Sect. Conclusions presents the conclusions and possible further developments.

## Problem description

There is a current demand in the market for product p ∈ P, each product p ∈ P goes through stages s ∈ S of production. Among them, P = {1, 2, ... p}, S = {1, 2, ... s}. Each production stage is equipped with an AGV for the transportation of each batch, and this transportation time is not negligible. During transportation, AGVs need to avoid obstacles, and obstacle avoidance can lead to uncertainty in the AGV's transportation time. The problem rationalizes the batching of all products and determines the processing sequence for each batch. Optimization is performed with the objectives of minimizing the maximum completion time and total energy cost. Figure 1 illustrates the production process for job shop.

Fig. 1. Production processes in the job shop. I, II---XIII represents a set of equipment, which includes multiple production equipment. Product p is passed into this set. It selects an equipment for production and transfers it out after production. The red dotted boxes s_{1}, s_{2}, ... , s_{6} represent a production stage, which is the range of services required by a AGV, and includes all the equipment of a stage. p1 - p4 for four raw materials, the four raw materials pass in turn through a particular piece of equipment from different stages.

The probability set Ω of an AGV meeting an obstacle at each production stage is predicted by a Bayesian network. The predicted data numbers are passed into an optimization model to establish a data-driven automated job shop scheduling system based on Bayesian network inference. Figure 2 illustrates the data flow and material flow of the system.

## Mathematical model

### Multi-objective function

The objective function of the model consists of two objective functions of minimizing the maximum completion time and total energy cost (TEC). They are represented as equation (1)- equation (2), respectively.

Among them, *ms* ≤ *τ*<sub>*i**k*</sub> + *e*<sub>*i**k*</sub> + *c*<sub>*i**k*</sub>, *i* ∈ *I*<sub>*j*</sub>, *k* ∈ *K*. *τ*<sub>*i**k*</sub> represents the start time of product *i* at event point *k*; *e*<sub>*i**k*</sub> represents the processing time of product *i* at event point *k*; *c*<sub>*i**k*</sub> represents the adjustment time of product *i* at event point *k*.

During the execution period of product production, project schedule inconsistencies with the scheduling plan may result in extra costs. The uncertainty in this paper mainly comes from the deviation of material transportation time. When handling materials, AGVs may encounter obstacles. In this paper, the AGV chooses to wait for the obstacle to leave after encountering the obstacle, therefore, a time delay is generated. We describe the energy loss due to this uncertainty as the energy consumption deviation cost. Minimizing the energy deviation cost is the second objective function. The functions can be illustrated as equation (3) and equation (4).

Among them, *F*<sub>*p*</sub><sup>*e*</sup> represents the total completion time after the delay; *F*<sub>*p*</sub> represents an unobstructed time of completion; *E* represents the unit energy consumption, which includes two parts. They are the full state unit energy consumption *E*<sub>*f*</sub> and the idle state unit energy consumption *E*<sub>*i*</sub>, which has the unit *w*/*s*; *g*(*t*) represents the price function, which is related to the total completion time; *P̂*(·) represents the delay probability, which can determine the size of the delay and belongs to a probability range.

Generally, AGVs have three states of energy consumption. *fc*, *ic* and *bc* represent the energy consumption of AGVs in full state, idle state and braking state respectively. The full state and idle state belong to the transportation time part, and braking state belongs to the processing time part. In this paper, the delay in completion time is mainly caused by transportation. Therefore, only the energy consumption of transportation time is considered and not the braking state. The energy consumption is related to the unit energy consumption and the current state of the AGV. The functions can be illustrated as Eq. (5) and Eq. (6).

![img-0.jpeg](img-0.jpeg)

**Fig. 2.** Automated production scheduling system based on Bayesian network inference.

$$
\begin{aligned}
f c & =\sum_{a g v s=1}^{A} \sum_{t=s_{i}}^{e_{i}} u f^{a g v s} \varepsilon_{a g v s}^{t} g(t) \\
i c & =\sum_{a g v s=1}^{A} \sum_{t=s_{i}}^{e_{i}} u i^{a g v s} \eta_{a g v s}^{t} g(t)
\end{aligned}
$$

Among them, $u f^{a g v s}$ represents the energy consumption per unit time of the AGV under full state; $u i^{a g v s}$ represents the energy consumption per unit time of the AGV under idle state; $\varepsilon_{a g v s}^{t}$ and $\eta_{a g v s}^{t}$ represent the full state variable and the idle state variable at time $t$, respectively; $s_{i}$ and $e_{i}$ represent the start time and end time of the different state parts of product $i$, respectively.

# Batch model 

Batch model is the first part of the upper layer job shop scheduling model. There is a limit to the capacity of the production equipment as well as the capacity of the inventory, but the market demand is uncertain. When the market demand is greater than the capacity of the production equipment, it is necessary to produce in batches. The batch model is illustrated Eq. (7)-Eq. (14). Among them, $i$ represents the products; $I_{j}$ represents the set of products produced in stage $j ; k$ represents the event point, $k \in K=\{1,2, \cdots, k m\} ; x_{i k}$ represents whether product $i$ is produced at the $k$ event point; $O$ represents the production process; $O_{i j}^{k}$ represents the production process of product $i$ at event point $k$ in stage $j ; Q$ represents a production batch at one time; $Q_{j}^{\text {min }}, Q_{j}^{\max }$ represent the minimum and maximum production batch, respectively; $\partial_{a g v s}^{t}$ represents the decision variable for the braking state; $D_{i}$ represents the market demand for product $i ; P_{i j}^{k k \prime}$ represents the intermediate inventory of product $i$ between event point $k$ in stage $j$ and event point $k \prime$ in stage $j-1 ; P_{i j}^{\max }$ represents the maximum inventory.

$$
\begin{gathered}
\sum_{i \in I_{j}} x_{i k} \leq 1, \forall k \in K \\
Q_{j}^{\min } \leq Q\left(O_{i j}^{k}\right) \leq Q_{j}^{\max }, \forall i \in I_{j}, j \in J_{i}, k \in K \\
x_{i k}= \begin{cases}0, & \text { 定 } \\
1, & \text { 定 }
\end{cases}, \quad \forall i \in I_{j}, k \in K \\
\sum_{i \in I_{j}} x_{i k} \geq \sum_{i \in I_{j}} x_{i, k+1}, \forall j \in S, k \in K, k+1 \in K, k \neq k m \\
\varepsilon_{a g v s}^{t}+\eta_{a g v s}^{t}+\partial_{a g v s}^{t}=1 \\
\sum_{k \in\{1,2, \cdots, k m\}} Q\left(O_{i j}^{k}\right)=D_{i}, \forall i \in P, j \in S \\
P_{i j}^{k k \prime}=P_{i, j-1}^{k k \prime}+\sum_{0 \leq k k \leq k} Q\left(O_{i j}^{k k}\right)-\sum_{0 \leq k k \leq k \prime} Q\left(O_{i, j+1}^{k k}\right), \forall i \in P, j \in S, j \neq j m, k, k \prime \in K \\
P_{i j}^{k k \prime} \leq P_{i j}^{\max }, \forall i \in P, j \in S, j \neq j m, k, k \prime \in K
\end{gathered}
$$

Equation (7) represents that a process can only process one product at any moment, and similarly, a product can only be processed by one process; equation 8 represents the upper and lower limits for each batch; equation (9) represents that the set values of the decision variables and the uniqueness of the product batch corresponding to the event point; equation (10) represents that the actual event point is prior to the virtual event point; equation (11) represents that each AGV can only maintain one state for a fixed period of time; equation (12) represents that the total output of each process of each product is consistent with the market demand; equation (13) represents the calculation of intermediate inventory; equation (14) represents that the intermediate inventory cannot exceed the maximum value of the inventory.

## A time scheduling model based on Bayesian network inference prediction

Time scheduling model is the second part of the upper layer job shop scheduling model. Bayesian network inference identifies causal and coupling relationships of event occurrences and analyzes and models the events ${ }^{28}$. Considering the transportation uncertainty in the scheduling plan, the time scheduling model based on Bayesian network inference is established as Eq. (15)-Eq. (20). The scheduling sub problem determines the processing sequence and times for each batch of each process. There are two dimensions in the process immediately preceding the process, namely, product and equipment dimensions. Therefore, the start time of a process is affected by the availability of equipment in the current stage and the production status of the previous stage. When there is a product waiting between processes and there is availability on the equipment,

$\tau\left(O_{i j}^{k}\right)>\tau\left(O_{i-, j}^{k-}\right)+T\left(O_{i-, j}^{k-}\right), \tau\left(O_{i j}^{k}\right)>\tau\left(O_{i, j-1}^{k-}\right)+T\left(O_{i, j-1}^{k-}\right)$; When there is a product waiting between processes and there is no availability on the equipment, $\tau\left(O_{i j}^{k}\right)>\tau\left(O_{i-, j}^{k-}\right)+T\left(O_{i-, j}^{k-}\right)$ $, \tau\left(O_{i j}^{k}\right)=\tau\left(O_{i-, j-1}^{k-}\right)+T\left(O_{i-, j-1}^{\text {s, } k-}\right)$; When there is no product waiting between processes and there is availability on the equipment, $\tau\left(O_{i j}^{k}\right)=\tau\left(O_{i-, j}^{k-}\right)+T\left(O_{i-, j}^{k-}\right), \tau\left(O_{i j}^{k}\right)>\tau\left(O_{i, j-1}^{k-}\right)+T\left(O_{i, j-1}^{k-}\right)$ ; When there is no product waiting between processes and there is no availability on the equipment, $\tau\left(O_{i j}^{k}\right)=\tau\left(O_{i-, j}^{k-}\right)+T\left(O_{i-, j}^{k-}\right), \tau\left(O_{i j}^{k}\right)=\tau\left(O_{i-, j}^{k-}\right)+T\left(O_{i-, j}^{k-}\right)$.

Among them, process $O_{i j}^{k}$ represents the $k$-th position of the $j$-th stage of product $i$ to be processed; the markers below $O$ represent the product dimension and equipment dimension information; the markers above $O$ represent the event point information; $O_{i-, j}^{k-}$ represents the immediate preceding process of equipment dimensioning for process $O_{i j}^{k} ; O_{i, j-1}^{k-}$ represents the immediate preceding process of product dimensioning for process $O_{i j}^{k} ; T\left(O_{-,-}^{-}\right)$represents the sum of the processing and adjustment time of the process; $\tau\left(O_{i}^{k}\right)$ represents the start of production time of product $i$ on the process at the event point $k ; \lambda_{i}$ represents the production coefficient of product $i$ at different stages; $\gamma_{i}$ represents the conversion rate of product $i$ at different stages; $\beta_{i i}$ represents the inference probability derived from Bayesian network inference; $C_{i}^{k}$ represents the rated time for production of product $i$; Decision variable $\phi_{i i i}^{\text {change }}$ represents whether or not a product switches at the same stage of the process, if $i t=i$, then $\phi_{i i i}^{\text {change }}=0$, otherwise, $\phi_{i i i}^{\text {change }}=1 ; X\left(O_{i}^{k}\right)$ represents whether product $i$ is produced at the $k$ event point in this process; $W$ represents the outlook period.

$$
\begin{gathered}
\tau\left(O_{i}^{k+1}\right) \geq \tau\left(O_{i}^{k}\right)+\lambda_{i} \cdot \gamma_{i} \cdot Q\left(O_{i}^{k}\right)+\beta_{i i} \cdot C_{i}^{k} \cdot X\left(O_{i}^{k}\right), \forall i, i^{\prime} \in I_{j}, j \in S, k \in N, k \neq k m \\
\tau\left(O_{i}^{k+1}\right) \geq \tau\left(O_{i t}^{k}\right)+\lambda_{i^{\prime}} \cdot \gamma_{i t} \cdot Q\left(O_{i t}^{k}\right)+\beta_{i i t} \cdot C_{i t}^{k} \cdot X\left(O_{i t}^{k}\right)-W\left[1-X\left(O_{i t}^{k}\right)\right]+C_{i t i}^{k} \cdot \phi_{i t i}^{\text {change }} \\
\forall i, i t \in I_{j}, j \in S, k \in N, k \neq k m \\
\tau\left(O_{i t}^{k t}\right)+W \cdot\left[1-X\left(O_{i t}^{k t}\right)\right] \geq \tau\left(O_{i}^{k}\right)+\lambda_{i} \cdot \gamma_{i} \cdot Q\left(O_{i}^{k}\right)+\beta_{i i t} \cdot C_{i}^{k} \cdot X\left(O_{i}^{k}\right)-W \cdot\left[1-X\left(O_{i}^{k}\right)\right] \\
\forall i \in I_{j}, i t \in I_{j+1}, j \in S, k \in N, k \neq k m \\
\tau\left(O_{i}^{k}\right) \leq W, \forall i \in I_{j}, k \in K \\
\tau\left(O_{i}^{k}\right)+\lambda_{i} \cdot \gamma_{i} \cdot Q\left(O_{i}^{k}\right)+\beta_{i i t} \cdot C_{i}^{k} \cdot X\left(O_{i}^{k}\right) \leq W, \forall i \in I_{j}, j \in S, k \in K, k \neq k m \\
\sum_{k \in K} \sum_{i \in I_{j}}\left(\lambda_{i} \cdot \gamma_{i} \cdot Q\left(O_{i}^{k}\right)+\beta_{i i t} C_{i}^{k} \cdot X\left(O_{i}^{k}\right)\right) \leq W, \forall j \in S
\end{gathered}
$$

equation (15) represents that when the same product is produced in the same stage, the end time of the former event point cannot be greater than the start time of the latter event point; equation (16) represents that when different products are produced in the same stage, the end time of the former event point cannot be greater than the start time of the latter event point, and there is a switch of products; equation (17) represents that when the same product is produced in different stages, the end time of the former event point cannot be greater than the start time; equation (18) represents that the batch start time of the event point is less than the look-ahead period; equation (19) represents that the end time of the last product in each stage is less than the look-ahead period; equation (20) represents that the total processing time of each stage is less than the look-ahead period.

# Data-driven Bayesian network inference model 

The Bayesian network inference model is the lower layer model. During transportation between equipment, AGVs have multiple paths to choose and the occurrence of obstacles is uncertain for each path. In this paper, Bayes theorem is used to obtain the probability of occurrence of each path obstacle, and the objective function of the lower layer model is to minimize the occurrence of path obstacles. Equation. (21) illustrates the objective function.

$$
\beta_{i i t}=\min \left\{\frac{p\left(c_{s}\right) \cdot p\left(A / c_{s}\right)}{p(A=1)}\right\}, \forall i, i^{\prime} \in I_{j}, s \in\{1,2, \cdots 7\}, A \in\{0,1\}
$$

Among them, $A$ represents whether the AGV encounters obstacles during transportation; $c_{s}$ represents the $s$ -th node in the Bayesian network; $p(\cdot), p(\cdot / \cdot)$ represent the prior probability and conditional probability, respectively.

There are two scenarios in the AGV transportation path, passing and not passing. Assuming that the node data obeys the Beta prior distribution as in equation. (22), the Beta posterior distribution is obtained by updating the hyper-parameters through learning from the historical experience database as in equation. (23).

$$
\begin{gathered}
\pi\left(\theta_{p q}\right)=B e t a\left(\theta_{p q} ; a_{p q}, b_{p q}\right), 0 \leq \theta_{p q} \leq 1, p, q=1,2, \cdots, n \\
\pi\left(\theta_{p q} / X\right) \propto \operatorname{Beta}\left(\theta_{p q} ; a_{p q}+m ; b_{p q}+N-m\right)
\end{gathered}
$$

Among them, $\theta_{p q}$ represents the conditional probability that node $p$ occurs in the $q$-th combinatorial state of the parent node; $a_{p q}$ and $b_{p q}$ represent the hyper parameters in the $\operatorname{Beta}\left(\theta_{p q} ; a_{p q}, b_{p q}\right) ; m$ represents the times of $p$-th node occurring under the condition that the $q$-th combinatorial state of the parent node of the $p$-th node occurs $N$ times.

# Applying IMMOPSO to solve data-driven automated JSP 

To solve the job shop scheduling problem (JSP) considering AGV transportation time, a data-driven improved multi-objective particle swarm algorithm (IMMOPSO) is designed. The algorithm avoids to a great extent the problem of premature stabilization of statistical positions $x_{j}(t-1), p b_{j}(t-1)$, and $g b(t-1)$ of the standard multi-objective particle swarm. The quality of the solution is greatly improved. In the standard PSO algorithm, each particle evolution depends on the latest evolutionary rate $v_{j}(t-1)$, the update position $x_{j}(t-1)$ , the optimal individual position $p b_{j}(t-1)$ and the global optimal position $g b(t-1)$. Add more dynamic information and update the evolution scheme for each particle ${ }^{30}$. Therefore, the $j$-th particle evolves at $t$ iterations as Eq. (24)-Eq. (25)

$$
\begin{gathered}
v_{j}(t)=\omega v_{j}(t-1)+c_{1} r_{1}\left(p b_{j}(t-1)-x_{j}(t-1)\right)+c_{2} r_{2}(g b(t-1)-x_{j}(t-1))+\rho\left(c_{1} r_{1}+c_{2} r_{2}\right)\left(x_{j}(t-1)-v_{j}(t-1)\right) \\
x_{j}(t)=x_{j}(t-1)+v_{j}(t)
\end{gathered}
$$

Among them, $\rho$ represents a non-negative coefficient in the range $[0,1]$ Additionally, for the job shop scheduling problem considering AGVs, this problem is also solved using a non-dominated genetic algorithm(NSGA-II). Its comparison is made with the improved multi-objective particle swarm algorithm(IMMOPSO).

## IMMOPSO algorithm improvement strategy analysis

Based on the improved update formula, this paper also adds the crossover operator and genetic operator. It further prevents the multi-objective particle swarm algorithm from falling into local optimal solutions.

## $(\cdots)$ Crossover operator

The gene segments of two particles were randomly selected to interchange their positions to produce offspring. Among the $\mathrm{A} 1\left(1_{x_{11}}-2_{x_{12}}-\cdots-(K-1)_{x_{i,(K-1)}}-K_{x_{i, K}}\right)$ and $\mathrm{A} 2\left(2_{x_{12}}-1_{x_{11}}-\cdots-K_{x_{i, K}}-(K-1)_{x_{i,(K-1)}}\right)$ particles, the production variable interval segments are chosen randomly. Taking $\left(x_{i K}\right)$ and $\left(x_{i K}\right)$ as the beginning and the end, respectively, and placing them at the end of the gene yields $\mathrm{A} 1(1-2-3-4-[5]-[6]-[7]-8-[9]-10-11-12-[5-6-7-9])$ and $\mathrm{A} 2(4-2-11-1-[5]-[6]-[7]-9-[8]-10-3-12-[5-6-7-8])$. Two particles B1 (1-2-3-4-8-9-10-11-12-5-6-7-9) and B2 (4-2-11-1-8-10-3-12-5-6-7-8) after crossover were obtained by eliminating the repeated gene fragments. Thus, the crossover operation is complete.

## $(\square)$ Mutation Operators

Designing mutation operators can similarly improve the global search capability of multi-objective particle swarm algorithms. The production variable interval segments of the particles are randomly selected and the genes are updated. For example, the particle $\mathrm{C}(1-2-3-4-5-6-7-8-9-10-11-12$ ) is selected, from which the two production variables 9 and 10 are chosen to obtain $\mathrm{C} 1(1-2-3-4-5-6-7-8-10 t-9 t-11-12)$ by a mutation operation. If the mutated gene is out of the variable's defined range, the mutated gene is corrected; if the mutated gene meets the variable's defined range, the mutation operation is complete.

## Encode and decode

Consider the job shop scheduling problem (JSP) for AGVs which solves two main problems, the scheduling problem and the path decision problem. The entire problem is solved in two ways, corresponding to the start of production time and transportation time of each batch on each stage. In order to ensure that the particle corresponds to the solution space of the problem, a two-dimensional continuous variable is created to represent the search space of the particle. Table 1 illustrates the two-dimensional variable space. Among them, $j m$ and $u m$ represent the product type and the number of stages, respectively. Algorithm 1 illustrates the pseudo-code for the encoding of the improved particle swarm algorithm.


Table 1. Two-dimensional continuous variable.


Algorithm 1. Coding procedure

Converting the algorithm into a problem solution requires a corresponding decoding operation. Algorithm 2 illustrates the decoding pseudo-code for the IMMOPSO algorithm.


Algorithm 2. Decoding procedure

# Algorithm steps 

The most basic Multi-Objective Particle Swarm (MOPSO) is prone to fall into local optimization during the iteration process. Therefore, in this section, the MOPSO algorithm will be improved. Combining the above coding and decoding principles, the MOPSO algorithm is improved based on the idea of cross mutation and named as IMMOPSO algorithm. The specific details are denoted as Step 1 to Step 13.

Step 1 Define the population size pop and the number of iterations $N$ and set the set of algorithm parameters $\Omega$.

Step 2 Initialize particle population phest, fitness value Fitness.
Step 3 Perform a no-dominated sort to obtain the no-dominated solution set rep.
Step 4 Initialize adaptive grid.

Step 5 Perform an elite choice strategy to select the globally optimal solution Gbest.
Step 6 Update the velocity and position of all particles, randomize mutations and crossovers, and update Pbest again.

Step 7 If the iteration number reaches $N-t=10$ times, $t$ represents the current iteration number. Store the global optimal solution set for the current iteration number into the rep set, otherwise, directly skip to Step 8.

Step 8 Update the no-dominated solution set rep.
Step 9 Update the adaptive grid again.
Step 10 Check if the rep set is overflowed.
Step 11 If rep overflows, truncate; if it doesn't overflow, continue to Step12.
Step 12 Repeat Step3- Step11 until the number of iterations is reached and stop;
Step 13 Output the particles in the set of Pareto optimal solutions.

# Data-driven Bayesian network algorithms 

The combination of states of Bayesian network nodes affects the prediction results. Reasonable algorithm solving can get better solution. A large amount of historical empirical data is input, and Newton's method and second-order moment function, etc. are introduced to solve the mean of the posterior distribution. According to Bayesian theorem and event independence, the posterior probability is calculated. Algorithm 3 is the pseu-do-code of data-driven Bayesian network algorithm.

```
Begin
    Num1 given the number of state combinations of Bayesian network nodes;
    Num2 given the number of child nodes;
1.int \(i\);
2. double \(r[N u m 1] \leftarrow[]\);
3.for \((i=0 ; i<N u m 1 ; i++\) )
4. \(\{\)
5. Randomly generate a mean, \(\mathrm{r}[i]=r \operatorname{rand}(\) Min, Max);
6. output \(r[i]\);
7. \(\}\)
8. double \(x_{0}[N u m 1] \leftarrow[]\);
9. double \(u[N u m 1] \leftarrow[]\);
10. double \(D[N u m 1] \leftarrow[]\);
11. double \(A[N u m 1] \leftarrow[], B[N u m 1] \leftarrow[]\);
12. double \(T[N u m 1] \leftarrow[]\);
13. initialization approximation \(x_{0}\);
14. setting the accuracy requirements and maximum number of iterations for Newton's method;
15. for \((j=0 ; j<N u m 1 ; j++\) )
16. \(\{\)
17. setting up Newton's iterative equations \(f(x)=0\), computing \(u[j]\);
18. setting the second-order moment function \(g(x)\), computing \(D[j]\);
19. setting coefficient functions \(v 1(x), v 2(x)\), computing \(A[j], B[j]\);
20. setting the first-order function \(h(x)\), calculate the a posteriori mean \(T[j]\);
21. \(\}\)
22. double \(p[N u m 2] \leftarrow[]\);
23. for \((k=0 ; k<5 ; k++\) )
24. \(\{\)
25. computing the set of posterior probabilities for the parent node \(p[k]\);
26. \(\}\)
27. selecting maximum and minimum values, \(\max \{p[k]\}, \min \{p[k]\}\);
28. output range, \(\mathrm{r}\left(p\left(k_{s}\right), p\left(k_{s}\right)\right)\);
29. End
```

Algorithm 3. Bayesian network prediction algorithm


Table 2. Input parameters and level values.
![img-1.jpeg](img-1.jpeg)

Fig. 3. Parameter Mean Response.

# Experimental simulation and analysis 

## Parameter testing

The parameter settings also have a great impact on the optimization performance of the improved IMMOPSO algorithm. It consists of six main parameters, which are the perturbation factor $(\rho)$, update coefficients ( $c 1$ and $c 2$ ), crossover probability ( $p c$ ), mutation probability ( $p m$ ), grid expansion ( $\alpha$ ), and leader election pressure ( $\beta$ ). Generally, $c 1=c 2$. In this section, Taguchi's design of experiments method is used to analyze the effects of different settings of the six parameters on the optimization results and to find out the better parameter setting scheme ${ }^{31}$. Table 2 illustrates that each of the six parameters has three level values. Ultimately an orthogonal matrix is produced to represent the parameter combinations The function that builds the model itself is used as the objective function of the test function. Since there exists more than one objective function and the results obtained are non-inferior solution sets, there are two response values for the experiment.

The parameter combinations are imported into MINTAB18 software for processing, and the mean response plots under different parameter combinations are obtained, as shown in Fig. 3. From Fig. 3, it can be seen that the algorithm performs better when the disturbance factor and update coefficient are at high level; the algorithm performs best when the mutation probability is at low level; the algorithm operates less well when the grid expansion, the leader selection pressure and the crossover probability are too large and too small.

The mean response illustrated in Fig. 3 shows that the IMMOPSO algorithm achieves optimal results when using combinations of $\rho=1.0, c_{1}=c_{2}=2.1, \alpha=0.25, \beta=5, p c=0.6$ and $p m=0.05$. Therefore, this combination of parameters will continue to be used in subsequent experiments.

## Data-driven Bayesian network inference

Network nodes exist in both passable and failed states, with the failed state indicating the occurrence of an external obstacle. Therefore, Beta distribution is chosen as the conditional probability of the action between nodes. Through the data-driven Bayesian network inference, this chapter obtains the coefficient table of Beta distribution as Table 3.

During the historical production process, data was recorded for each project. Among them, a large amount of AGV transportation path selection and obstacle avoidance information was accumulated. By organizing the data, a period of historical time can be selected for analysis. The historical information is illustrated in Table 4.


Table 3. Coefficients of Beta distribution.


Table 4. Sample information on AGV transportation path selection.

of conditional
probabilities of
nodes | $\operatorname{Beta}\left(\theta_{c_{1}} ; 3.3451 ; 57.3897\right)$ | $\operatorname{Beta}\left(\theta_{c_{2}} ; 1.1385 ; 59.1717\right)$  |
of conditional
probabilities of
nodes | $\operatorname{Beta}\left(\theta_{c_{3}} ; 5.3451 ; 55.3897\right)$ | $\operatorname{Beta}\left(\theta_{c_{4}} ; 2.2627 ; 58.3059\right)$  |
of conditional
probabilities of
nodes | $\operatorname{Beta}\left(\theta_{c_{5}} ; 3.027 ; 57.0365\right)$ |   |

Table 5. Posterior distribution of each parent node.

Table 4 shows the information of 60 historical production transportation paths, in which transportation barriers appeared 10 times in 5 random combinations. It is assumed that none of the nodes outside of the obstacle combinations are obstructed.

Finally, the mean of the posterior distribution is taken as the conditional probability of the node. Tables 5, 6, 7 demonstrates the posterior distribution of each node. Table 8 demonstrates the conditional probability of the node and the range of efficiency values.

From Table 8, the minimum and maximum values are taken as the range of transportation time efficiency values for the optimization model, i.e., $[0.05091660,0.331437]$.


Table 6. Posterior distribution of each child node.

of conditional
probabilities of root
nodes | $\operatorname{Beta}\left(\theta_{A 00} ; 0.2311 ; 50.2729\right)$ | $\operatorname{Beta}\left(\theta_{A 01} ; 0.4933 ; 0.5344\right)$ |  |  |   |

Table 7. Posterior distribution of root nodes.


Table 8. Calculated values and ranges of a posteriori probabilities.

![img-2.jpeg](img-2.jpeg)

Fig. 4. Pharmaceutical process.

# Instance testing

In order to verify the performance of the proposed IMMOPSO, the algorithm is programmed and implemented using VS 2019. The simulation platform is configured with Intel(R) Core(TM) i7-8550U(CPU), 8 GB (RAM) and Windows 10 .

Based on the production data in a pharmaceutical company ${ }^{32}$, this section analyzes the effectiveness of the proposed IMMOPSO through test cases. The process of pharmaceutical production is illustrated in Fig. 4.


Table 9. Production data.
![img-3.jpeg](img-3.jpeg)

Fig. 5. Comparison of algorithms under different combinations of sizes.

The manufacturing process of a pharmaceutical company in Shenyang has multi-species production lines, each of which contains multiple production stages. The total production capacity of the equipment at each stage fluctuates within a certain range, which is mainly related to the type of tablet. The processing time of tablets is determined by the production quantity and processing coefficient. The transportation time of AGV is related to the layout of the equipment in the corresponding stage. At the same time, based on the pharmaceutical industry tablet production process industry, AGV main action energy acquisition is electrical energy. The amount of electrical energy it consumes depends on several factors such as workload, working time, route and environment, type and capacity of battery. In this paper, AGV belongs to high energy consumption equipment, the size of consumed power energy is probably between tens of kilowatts and hundreds of kilowatts per day, and the specific data will be related to the AGV's state ${ }^{33}$. Table 9 illustrates the detailed production data.

The performance of IMMOPSO algorithm proposed in this is compared with NSGA-II algorithm. Each algorithm is run 70 times randomly. Figure 5 illustrates a comparison of the optimal solutions resulting from the two algorithms, with the horizontal axis indicating the value of objective function 1 and the vertical axis indicating the value of objective function 2. Figure 5. (a) illustrates a population size of 20 with 50 iterations; (b) illustrates a population size of 50 with 50 iterations; (c) illustrates a population size of 100 with 100 iterations. When the algorithm combinations are $50 * 50$ and $100^{*} 100$, the IMMOPSO algorithm runs significantly better than the NSGA-II algorithm. When the particle population size becomes larger ( $125^{*} 100$ ), the results of IMMOPSO runs are comparable to the NSGA-II algorithm and can still be worth referring to for applications. In summary, from Fig. 5, it can be seen that the pareto fronts computed by the IMMOPSO algorithm outperform the pareto fronts of the NSGA-II algorithm.

# Experimental evaluation 

The IMMOPSO is compared with the solution set of the NSGA-II to analyze the dispersion degree of IMMOPSO ${ }^{34}$. When the dispersion of the solution set of the IMMOPSO algorithm can be comparable or even higher than that of the NSGA-II, it indicates that the algorithm is able to seek the optimal solution in a larger


Table 10. Comparison of the dispersion of each algorithm under different combinations.
![img-4.jpeg](img-4.jpeg)

Fig. 6. Boxplots of the IMMOPSO and NSGA-II algorithm.
range. Table 10 illustrates the results of the degree of dispersion of the IMMOPSO algorithm and the NSGA-II algorithm.

Through the dispersion of particle populations demonstrated in Table 10, the dispersion of IMMOPSO algorithm is less different from that of NSGA-II algorithm, and in some combinations the dispersion of IMMOPSO algorithm exceeds that of NSGAII algorithm. The dispersion of the IMMOPSO algorithm gradually increases as the population and the number of iterations increase. The IMMOPSO algorithm is very stable when the population size reaches 125 . However, the NSGA-II algorithm is less stable.

In addition to this, setting the population size to 100 and the number of iterations to 100, Fig. 6(a) and (b) show the boxplots of the two algorithms, respectively. It can be concluded that from the perspective of time span, IMMOPSO algorithm searches for the solution with better quality than NSGA-II algorithm, which can prove that our strategy and algorithm are effective. The mean value of the results of the IMMOPSO algorithm is smaller than the mean value of the results of the NSGA-II algorithm, demonstrating a better range aggregation range for its solution. From the point of view of power consumption, IMMOPSO algorithm searches for a larger range of solutions, but with higher mean values. It shows that our strategy plays a positive role and it also shows that the algorithm choice of particle swarm algorithm is more appropriate.

In summary, the improved IMMOPSO algorithm converges much better than the NSGA-II algorithm. Its dispersion is comparable to that of the NSGA-II-II, and it does not fall into local optimality. Thereby, the improved IMMOPSO algorithm in this paper is effective.

# Data-driven multi-scenario analysis of a job shop scheduling problem based on Bayesian inference 

The probabilistic inference method designed in this paper for lower tier transportation delays has important implications for the on-time performance of upper tier scheduling plans. Continue to use case data from the literature [26] to design simulation experiments. There exists an on-time standard completion time set for this simulation case. Its completion time is near-optimal. The AGV transportation obstacle avoidance problem is not considered and therefore there is no time extension problem. For example, one of the sets of completion time sets is $\{11288.1,11483.34,12455.93,10467.13,11525.56,12996.33\}$. Based on the Bayesian network inference, this paper predicts the probability of encountering obstacles when AGVs transport materials. The delay probability is restricted to a certain range, and the delay probability is randomly selected from the interval $\{0.050916608,0.331437\}$. Comparison of the completion time under different scenarios is done to obtain the feasibility of the optimization scheme. In order to compare the experimental results more visually, for the same scheduling plan, four different scenarios will be illustrated in this paper. Scenario 1 represents the maximum completion time without considering delays; Scenario 2 represents the maximum completion time of the datadriven AGV based on Bayesian inference with predicted delay period; Scenario 3 and Scenario 4 represent the maximum completion time of the AGV without predicted delay period. Figure 7 represents the transportation

![img-5.jpeg](img-5.jpeg)

Fig. 7. Multi-scenario optimization model for solving scheduling schemes.

Path transformation graphs and time span graphs of AGVs for the optimal scheduling scenarios under the four scenarios.

In Fig. 7, the start time for this production schedule is set to zero. The completion time of the last process in scenario 1 is 12,209.64 s. Therefore, the maximum completion time minimization for this production schedule is 12,209.64 s, subject to various realistic constraints. The maximum completion time always occurs at the time when the production of the second batch ends. The three lines represent the transportation time and conversion time points of the AGVs, respectively. The vertical axis values represent stages and products. Among them, 1–5 represent are five products in the first stage; 6–10 represent are five products in the second stage; 11–15 represent are five products in the third stage. Horizontally, the end time of the first stage of different batches of the same product is less than the start time of the next stage. Vertically, the start of the next stage is greater than the end of the previous stage for the same batch of the same product. From a different perspective, Fig. 7(a) reflects that the model's calculated before and after time connection is reasonable. The completion time for the last process in Scenario 2 is 12,397.74. Scenario 2 is the one that takes the least amount of time after considering uncertainties, indicating that the Bayesian network predicts well. Both scenarios 3 and 4 also consider uncertainty, but the transportation path of the AGV is chosen randomly. Data-driven Bayesian inference prediction applied to the job shop AGV decision-making problem can improve productivity by 4.4% and 8.4% over scenarios 3 and 4, respectively, which proves its optimization effect.

### Conclusions

For the job shop scheduling problem considering AGV transportation between equipment, this paper establishes a data-driven two-layer automated shop scheduling model based on Bayesian network inference prediction. This section analyzes the main findings and implications of the study from an upper-layer production scheduling model perspective and a lower-layer predictive model perspective. From the perspective of upper-layer production scheduling, the case study shows that the model in this paper greatly reduces the uncertainty of the completion time. At the same time, in case of random obstacles, the model greatly reduces the transportation time of the AGVs between equipment by at least 4.4% of the time span. From the perspective of lower-level

predictive modeling, Bayes' theorem is able to reason about the posterior distribution of network nodes. Based on this, this paper finds that each node in the AGV action trajectory network has different probabilities of obstacle occurrence, and the node with the lowest probability is selected as the AGV passing node. The method transforms the complex obstacle avoidance problem into a Bayesian network historical data learning problem, which significantly reduces the computational cost of the algorithm and better applies to job shop manufacturing. In addition, there exists a certain practical significance of this research. The combination of job shop scheduling and Bayesian network prediction techniques can greatly help manufacturing companies to predict the scheduling process of manufacturing resources and make optimal resource scheduling decisions. For future research, it can be considered that the job shop scheduling problem for AGV transportation between equipment can be approached from the following aspects.

Real-time scheduling. By making production planning fully responsive and making immediate plans at any time based on real-time information, the production system becomes more responsive and the timing of the production and transportation stages more precise.
Deep learning algorithms. With the rapid development of deep learning algorithms, this paper can also use some more advanced algorithms to solve the problem. By performing several algorithm comparisons, the speed of the solution is improved and the reliability of the solution is enhanced

# Data availability 

All data generated during and/or analyzed in the current study are not openly accessible but are available from the corresponding author upon reasonable request.

Received: 25 August 2024; Accepted: 9 December 2024
Published online: 02 January 2025

# Author contributions 

Q. T. and H. W. conceptualized and designed the study; H. W. drafted the initial manuscript; Q. T. reviewed and revised the manuscript; Q.T. and H.W. collected the research data and analyzed the results; all authors approved the final manuscript as submitted and agree to be accountable for all aspects of the work.

## Funding

This work was supported by the National Natural Science Foundation of China (grant number 71801160); Liaoning Provincial Department of Education Fundamental Scientific Research Project. (grant number LJ112410142009); Liaoning Provincial Education Science General Subject. (grant number JG20DB342);

## Declarations

## Competing interests

The authors declare no competing interests.

## Additional information

Correspondence and requests for materials should be addressed to H.W.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommo ns.org/licenses/by-nc-nd/4.0/.
(c) The Author(s) 2025