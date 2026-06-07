# Article 

## Optimizing Construction Engineering Management Using Metaheuristic Methods and Bayesian Networks

Anna Jakubczyk-Gałczyńska ${ }^{1, * *}$, Agata Siemaszko ${ }^{1}$ and Maryna Poltavets ${ }^{2}$

## check for updates

Citation: Jakubczyk-Gałczyńska, A.; Siemaszko, A.; Poltavets, M. Optimizing Construction Engineering Management Using Metaheuristic Methods and Bayesian Networks. Appl. Sci. 2024, 14, 4871. https:// doi.org/10.3390/app14114871

Received: 7 May 2024
Revised: 28 May 2024
Accepted: 31 May 2024
Published: 4 June 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Faculty of Civil and Environmental Engineering, Gdansk University of Technology, 80-233 Gdansk, Poland; agasiema@pg.edu.pl
2 Department of Industrial and Civil Construction, Zaporizhzhia National University, 69600 Zaporizhzhia, Ukraine; poltavmar@ukr.net

* Correspondence: annjakub@pg.edu.pl


#### Abstract

The construction of buildings invariably involves time and costs, and disruptions impact ongoing construction projects. Crisis situations in management strategies, structural confusion, and financial miscalculations often arise due to misguided decision-making. This article proposes a method that combines the learning of Bayesian Networks and heuristic techniques to optimize decision-making processes in construction scheduling. As an innovative approach in order to enhance construction management, the functioning of biological, molecular, and physical objects and nervous systems is considered, applying bionic features to mimic their efficiency and precision, thereby optimizing construction processes and improving coordination and decision-making. Bayesian Networks are used for probabilistic analysis, and heuristic methods guide quick decision-making. The results demonstrate the effectiveness of Bayesian Networks and heuristic methods in data analysis and decision-making in construction engineering. The developed algorithm can be successfully applied to both erecting and planning construction projects.


Keywords: civil engineering; project management; metaheuristic methods; golden ratio; Bayesian networks

## 1. Introduction

Optimization in construction management is crucial, enabling efficient resource utilization, cost minimization, and project-duration reduction. Despite its significance, the construction sector often grapples with the issue of delays and disruptions in the construction process. Accidental destabilizing situations in the management strategy, structural confusion in the production system, and economic and financial failures can result from misguided objectives in a separate department, enterprise, or business. These unforeseen obstacles can lead to substantial financial losses and can negatively impact a company's reputation. While various risk management and optimization methods exist, there is a lack of modern algorithms that could effectively support the construction process. Many of these methods are either too slow or imprecise, hindering their practical application in a dynamic construction environment.

At the moment, we can note that the latest optimization methods are becoming relevant in science and production, which are conceptually different from the traditional ones and are based on the characteristics of the functioning of biological, molecular, physical, and nervous systems. In this context, this paper aims to propose new heuristic methods that utilize Bayesian Networks to assess the probability of disruptions. Bayesian Networks, being graphical probabilistic models, allow complex dependencies between various factors influencing the construction process to be modeled. In the aforementioned conditions, there is an opportunity to achieve an effective balance between the whole and its elements (parts) between performers (departments, units), considering the qualification level, experience, and degree of responsibility [1,2]. It is believed that the application of such a method

can bring a range of benefits to construction management. Firstly, it can lead to a better understanding and prediction of potential disruptions, which in turn can assist in their avoidance or minimization. Secondly, it can enable more efficient resource utilization, leading to cost savings. Finally, it can contribute to improving the quality and timeliness of construction projects, which is crucial for maintaining competitiveness in the market.

# A Review of Knowledge of Metaheuristics in Engineering 

It is important to determine the state of knowledge in the presented problem of delay management. In paper [3], a detailed analysis of delays in construction projects has been conducted. The authors noted that delays are one of the main areas of scientific research due to the impact of delays on the time and cost of implementing construction projects. In publication [4], the risk of delays in construction projects has been discussed. The authors have identified several main causes of delays, such as order changes, the owner's financial problems, and slow decision-making by stakeholders. It has been suggested that these risks should be analyzed during the planning stage, which could reduce the risk during project implementation. An interesting approach has been used in [5]. In this article, models and methods of managing the risk of supply chains and delays in construction projects have been examined. Mainly, quantitative analysis has been used to identify disruptions in the supply chains in construction. An interesting position is presented in [6]. In this work, a literature review on risk management in construction projects in Nigeria has been conducted. The aim of this research was to assess and understand the current situation of risk management practices in the Nigerian construction sector, with a particular focus on common risk factors that significantly impact project outcomes, and to examine the opinions of project managers and other stakeholders on the effectiveness of risk management.

The authors of this study have repeatedly attempted to assess disruptions during construction work. The first example is [7]. The publication stated that the organization and management of the investment process are key aspects of modern construction. It was pointed out that the success of a project depends on skillful risk management in logistics processes. Many risk factors affect the timeliness of construction work, which are often not taken into account at the planning stage. The aim of the research was to present the thesis that the project documentation for a given investment should be expanded to include a risk management plan. The authors argue that planning the execution of works while taking into account disruptions is a very good solution for scheduling work, as this method reduces the probability of shifting the deadlines for completing individual stages of construction, and thus also contributes to cost reduction. The authors emphasize that random events that can interrupt or prolong work are not easy to determine. Therefore, it is important to introduce a risk management plan for disruptions at the stage of designing logistics activities. Another article by the co-authors [8] deals with problems related to the implementation of construction works in difficult weather conditions. It was noted that construction contractors are forced to optimize the amount of labor during the implementation of construction works. Many risk factors affect the timeliness of construction work, which are often not taken into account at the planning stage. The aim of the article was to present a proposal for determining the costs and labor of construction works performed in unfavorable weather conditions. It was found that planning the execution of works while taking into account disruptions is a very good solution for scheduling work, as this method reduces the probability of shifting the deadlines for completing individual stages of construction, and thus also contributes to cost reduction. The authors emphasize that random events that can interrupt or prolong work are not easy to determine. Therefore, it is important to introduce a risk management plan for disruptions at the stage of designing logistics activities.

Another article [9] presented risk assessment and management in urban construction projects. The authors have been looking for new methods to improve the efficiency of investments related to the maintenance and operation of existing engineering structures. Research has suggested that risk management can be more effectively handled by using a

statistical inference process based on Bayesian theory, taking into account new information from monitoring. The authors of this paper have also carried out research on the use of Bayesian Networks; an example is article [10]. It concerns the use of Bayesian Networks to forecast the impact of traffic-induced vibrations transmitted through the ground on residential buildings. The authors have shown how monitoring data, combined with knowledge about the elements of the construction and operation phase and their relations, can be used to assess the impact of traffic-induced vibrations. In [2], the authors have developed the concept of the effective management of production systems in construction, taking into account the harmonious formation of organizational structures. The authors of the study revealed the effectiveness of the harmonization approach in improving the interaction of structural elements of production and accelerating their functional sensitivity to changes in the environment. It has been proved that harmonious production more effectively adapts to the diversity of interests, goals, and actions at all levels of management of various subsystems in any environment. In [11], the study resulted in the development of a structural and information model for managing production systems in the construction industry based on the general laws and principles of systemology, system engineering, and logic. The proposed integrated model provides the logical interconnection of information modules, complete control functions, and expected states of the production system in achieving the goal of optimization and reliability.

In [12], the expediency of using the quasilinear optimization model, which considers a triad of construction processes in the form of organizational and technological measures, characterized by a set of basic parameters, is shown; in addition, each directly implemented organizational and technological event can be modified by the introduction of logistics measures in the form of additional parameters. This will optimize the construction process and contributes to the saving of production costs of construction and installation works, reducing the complexity of building production and obtaining economic benefits.

The need to develop metaheuristics methods can be seen in article [13]. The authors focus on the fact that there is a growing number of approaches to solutions based on metaheuristics in global optimization research. Since the introduction of the first metaheuristic algorithms, such as genetics, particle swarm optimization, and other such similar algorithms, there has been an exponential increase in novel proposals. The article emphasizes that these algorithms are evaluated not only on the basis of their performance, but also on the novelty of the processes they model. A comprehensive review of the knowledge and use of metaheuristics can be found in [14]. The authors provide a summary of the methods' capabilities in various fields: scheduling, transportation, combinatorial optimization, structural and civil engineering, energy and electrical engineering, and the military. This shows how effective metaheuristics-based methods are.

In the present day, a variety of innovative optimization methods are on offer, which solve the issue of practical application in determining the optimistic indicator, searching for the best (optimal) value of the objective function among a set of admissible real values. Possibilities of solving the actual organizational and technological tasks of construction production are oriented to the complex of logical-structural relationships between its functional subsystems. Global destabilization processes and the violation of the system methodology in production management led to the disconnection of logical and informational approaches to functioning, a lack of unity of the modeling space, and cross-cutting information support when making effective organizational and technological decisions. Analyzing the state of knowledge in the field of project optimization management, it can be concluded that there is a need to look for new optimization solutions. The purpose of this research is the development of algorithmic support for the processes of the organization and management of production systems of construction in the circle of the harmonious guidance of metaheuristic methods during improvement and optimization. Therefore, the subject of this work is an algorithm supporting the decision to extend or shorten the planned times of construction processes.

# 2. Materials and Methods 

### 2.1. Justification of the Research Field

The combination of metaheuristic methods with Bayesian Networks creates new possibilities in the field of optimization, especially in the construction sector. Metaheuristics, akin to genetic and swarm algorithms, are optimization procedures inspired by natural processes. They utilize principles like the golden ratio and genetic evolution to create systems with self-similarity. Used in optimizing fuzzy systems linked to Bayesian probability, they guide towards effective solutions. The blend of the golden ratio method and Bayesian modeling emulates natural mechanisms, showcasing the metaheuristic essence of the research. Metaheuristic methods are commonly used to solve complex optimization problems [12-14]. Thanks to their ability to explore the global solution space, these methods are particularly useful in situations where the solution space is irregular or contains multiple local extremes. On the other hand, Bayesian Networks are a powerful tool for modeling uncertainty and complex dependencies between variables. In the context of optimization, they can be used to model and quantify uncertainty associated with various aspects of the optimization problem. The combination of these two approaches can lead to the creation of more advanced and effective optimization algorithms. For example, metaheuristic methods can be used for the global exploration of the solution space, while Bayesian Networks can be used for local exploration and to evaluate the quality of individual solutions [10]. In this particular situation, such a combination can be used to optimize various aspects of the construction process, such as schedule planning, resource management, or building structure design. As a result, it is possible to achieve better effects, such as shorter construction times, lower costs, or better quality of construction [4,10].

Furthermore, the properties of production systems in construction are described by non-linear dependencies and are improved with the help of complex modeling algorithms [15-21]. This causes high computational complexity when solving optimization problems; therefore, the use of classical numerical methods to find the extrema of multiextremal functions with complex surface relief of the level is very difficult [22,23]. This highlights the importance and potential benefits of using advanced optimization methods such as metaheuristics and Bayesian Networks in the construction sector.

The use of metaheuristic methods accompanies the execution of global optimization and allows one to find a high-quality solution in a relatively reasonable time, as well as to use a physical phenomenon with a minimum amount of initial information about the properties of the function. We will coordinate the strategy of finding local extrema and perform a full study of the set of admissible solutions, considering the calculation costs as an essential factor of feasibility. The structure of production systems, their functional integrity, and the stability of unity with the external environment form the basis of harmonious management, which is a guarantor of orderliness and consistency of all constituent parts of production system both internally among themselves and with external functions. The ordered composition and coordination of components into a single harmonious structure provides "immunity" to the system in relation to external and internal destructive (destabilizing) factors. The probability of negative consequences drops sharply [15]. Modern business structures use the technology of harmonious management, which prevents crises in activity and the choice of a promising development strategy. The implementation of harmonious management technology contributes to the sustainable operation of all construction processes. The main condition of the process of the sustainable evolutionary (harmonious) development of systems is the existence of the ratio of the golden section in their structure [0.62:0.38], which ensures a stable balance of development and a reduction in costs for the maintenance of a stable state of the production system [13-15]. The golden section combines dynamics and statics, the variable and the unchangeable, because it contains at its core the principle of structural dynamic symmetry (invariance of structural transformations) and the phenomenon of self-similarity-the whole relates to the larger part as the larger to the smaller. The functioning of production processes according to the laws of the golden ratio (GR) ensures the property of structural self-similarity, that is, energy-informational

conditioning of development. The symmetry of structural self-similarity in conditions of dynamism creates the progression of the golden section in combination with the fractals of the algorithms of the functioning of complex production systems. In the focus of understanding the amazing properties of the golden section, there is an opportunity to apply unique optimization techniques in the management, planning, and organization of production processes of construction.

# 2.2. Selection of Optimization Methods 

Construction production has its own peculiarities and specifics: the instability of production, its discrete nature, mobility, the number of participants in the construction process, a long production cycle compared to industry, the stationary nature of the use of construction products, and the influence of random factors (weather, geographical conditions, etc.). The management of construction production occurs through optimization. The golden section method emerges as one of the most promising, achieving the highest accuracy with a limited number of target function $f(x)$ calculations [11,14].

According to the concept of the golden ratio method, the optimization of any management decision is performed by the practical tools of dividing the initial interval $[a \ldots b]$ of possible alternative construction options of length $(\tau=1)$ into two parts in such a way that the ratio of the whole to the larger part is equal to the ratio of the larger part to the smaller part. This unusual division principle creates two points, $x_{\tau 1}$ and $x_{\tau 2}$, on the research interval, which realize the optimization principle of the golden section.

To ensure the symmetry of the search optimal solution, the distance $(1-\tau)$ should be $\tau$-th of the length of the total interval. Under such conditions of choosing the value of $\tau$, the next test point is placed at a distance equal to the $\tau$-th part of the length of the interval from the right limit point of the segment boundary [19]. When choosing $\tau$ in accordance with the condition $1-\tau=\tau^{2}$, the search solution is preserved when moving to a reduced interval (see Figures 1-4). Next, the following quadratic equation is solved:

$$
\tau=\frac{-1 \pm \sqrt{5}}{2}
$$

The positive value of the equation is obtained: $\tau=0.61803 \approx 0.62$.
![img-0.jpeg](img-0.jpeg)

Figure 1. Geometric scheme of the golden section method in optimization problems of construction production (source: own findings based on [1,19]).
![img-1.jpeg](img-1.jpeg)

Figure 2. The search for the symmetry of the golden section in the optimization tasks of construction production in production systems (source: own findings based on [1,19]).

![img-2.jpeg](img-2.jpeg)

Figure 3. The formation of "golden intervals" in the work of the golden section method of optimizing construction production in production systems (source: own findings based on [1,19]).
![img-3.jpeg](img-3.jpeg)

Figure 4. Symmetry of the golden section in optimization tasks of construction production (source own based on $[1,19])$.

The mathematical model of the proportion is formed as follows:

$$
\frac{\tau}{y_{2}}=\frac{y_{2}}{y_{1}}
$$

or

$$
\frac{\tau}{y-y_{1}}=\frac{\tau-y_{1}}{y_{1}}
$$

The following notation is introduced into the mathematical calculations:

$$
\frac{y_{1}}{\tau}=z
$$

the formalization of which obtains the following:

$$
\frac{1}{1-z}=\frac{1-z}{1}
$$

and the following result was obtained: $z=\frac{3-\sqrt{5}}{2} \approx 0.382$.
We performed a further search for the harmonic accompaniment of the optimal solution using the method of the golden section, which is based on dividing the segment of a set of possible options by trial points into intervals in the golden ratio. The management decision optimization function $f(x)$ is unimodal on the interval $[a \ldots b]$. Under these conditions, the position of the optimal point of the function (min) is found in the two inner points of the golden ratio (see Table 1). The mutual location of the optimal solution points should be considered in the following two cases:

$$
\begin{aligned}
& f\left(x_{\tau 1}\right)<f\left(x_{\tau 2}\right) \\
& f\left(x_{\tau 1}\right) \geq f\left(x_{\tau 2}\right)
\end{aligned}
$$

Table 1. Operation of the optimization procedure by the method of the golden section.


The first case (6) realizes the minimum of the optimality function in the segment $\left[a \ldots x_{\tau 2}\right]$. The second condition (7) provides the implementation of the optimal function in the segment $\left[x_{\tau 1} \ldots b\right]$.

Considering the levels of symmetry of the intervals of segments in the proportions of the golden section, the implementation of the working scheme of the golden section method was discovered, which proves that the length of the uncertainty interval $l_{o p t}$ at each stage (the symmetry levels of the golden section $S$ ) is compressed by a factor of 0.62 . In the first stage, you need to perform two calculations of the optimal function, and in each subsequent stage, it is enough to calculate one value (see Figure 5). The length of the uncertainty optimization interval after $S$ calculations of the values of the objective function $f(x)$ will be as follows:

$$
l_{o p t}=0.62^{S-1} \cdot(b-a)
$$

It is reasonable to use the principle of the golden section as a management factor of the enterprise's organizational and economic potential. The purpose of complex research and transformations is to bring them to an unexpectedly or expectedly simple conclusion and to discover the natural laws of the relation between the whole and its parts, the variety of recurrent sequences, essentially identical relationships, and inversion models that allow us to make harmonics, or the theory of harmony, which is the future.
![img-4.jpeg](img-4.jpeg)

Figure 5. Graph of the optimization function of the golden section method with the mutual location (a) of points $f\left(x_{\tau 1}\right)<f\left(x_{\tau 2}\right)$; (b) of points $f\left(x_{\tau 1}\right) \geq f\left(x_{\tau 2}\right)$ (source: own findings based on [1,19]).

# 2.3. Possibilities of Using Bayesian Networks 

A harmonious production system is a complex of component parts (subsystems) interconnected according to the rule of the golden ratio. The management and organization of such a system should be based on the concepts of harmonious management [11,18]. Under these circumstances, the application of Bayesian Networks can be seen as a natural extension of the principle of harmonious management. By modeling the probabilistic dependencies between different variables in the system, Bayesian Networks can help to

capture the complex dynamics of the system and thus contribute to the achievement of a more harmonious state [23].

Bayesian Networks (BNs) are powerful tools in the field of construction, offering a probabilistic graphical model that represents a set of variables and their conditional dependencies via a directed acyclic graph [24,25,26]. The nodes in this graph represent the variables, and the edges between nodes represent the probabilistic dependencies between the variables. By integrating Bayesian Networks into the management process, it is possible to make more informed decisions and thus further enhance the harmony of the system. Bayesian Networks are a type of probabilistic graphical model that uses Bayesian inference for probability computations. Bayesian Networks aim to model conditional dependence, and therefore causation, by representing conditional dependence by edges in a directed graph. Through these relationships, one can efficiently conduct the inference of the random variables in the graph using the Bayesian Network [27].

Mathematically, a Bayesian Network is defined by two components: a directed acyclic graph (DAG), G, where each node represents a variable, and the absence of an edge represents a conditional independence statement, and a set of conditional probability distributions (CPDs). Each node, $X_{i}$, in the graph has an associated CPD, $P\left(X_{i} \mid\right.$ Parents $\left(X_{i}\right)$ ), where Parents $\left(X_{i}\right)$ denotes the parents of $X_{i}$ in G.

The joint probability distribution over all variables $X_{1}, X_{2}, \ldots, X_{n}$ in the Bayesian Network can be expressed as a product of the CPDs in the network [28,29]:

$$
P\left(X_{1}, X_{2}, \ldots, X_{n} \prod_{i=1}^{n} P\left(X_{1} \mid\right.\right. \text { Parents }\left(X_{1}\right))
$$

This factorization allows for the efficient computation of the joint distribution and is the key feature of Bayesian Networks that makes them useful for modeling complex systems. The structure of the graph can also provide valuable insight into the conditional independence relationships in the modeled system. In the context of construction, these variables could represent different aspects of a construction project, such as cost, time, quality, and safety. The dependencies between these variables can help in understanding how changes in one aspect of the project can affect others. For instance, an increase in cost might lead to an increase in quality but might also lead to an extension in the project timeline. The strength of BNs lies in their ability to handle uncertainty and complexity, which are inherent in construction projects. They allow for the calculation of the probability of different outcomes, given the current state of knowledge about the variables. This is particularly useful in construction, where projects often face unforeseen challenges and changes.

One application of BNs in construction is in risk management. Construction projects often face various risks, such as delays, cost overruns, and safety incidents. BNs can be used to model these risks and their interdependencies, allowing for a more comprehensive and accurate assessment of the overall project risk. This can help in making informed decisions about risk mitigation strategies.

# 3. Results 

### 3.1. Experience and Preliminary Research

Efficient construction project management relies on optimizing construction schedules. The choice of technique depends on project-specific details and the available data. Experimentation and adaptation of approaches tailored to specific needs are essential for achieving optimal results. In this article, we delve into various optimization techniques, drawing from our extensive experience.

In recent studies, metaheuristic methods have demonstrated their ability to approach optimal solutions within a short timeframe. These methods, such as simulated annealing, tabu searches, and swarm optimization, efficiently explore solution spaces. By iteratively refining schedules, metaheuristics significantly improve project timelines and resource allocation. In the range of these studies, among others, there is also the method of the golden ratio.

Beyond traditional optimization approaches, the golden ratio offers unique insights. Combining dynamic and static elements, the golden ratio principles of dynamic symmetry, self-similarity, and adaptation contribute to structurally advantageous designs. Objects based on the golden ratio exhibit structural self-similarity and evolutionary benefits. Algorithms inspired by the golden division maintain consistent features throughout an object's life cycle, mirroring natural systems' evolutionary and genetic properties.

In recent years, machine learning also has gained prominence for optimizing construction processes. Bayesian networks, in particular, predict optimal schedules based on historical data. While each method-metaheuristics and Bayesian networks-has shown promise independently, their simultaneous application represents a novel approach. Researchers have achieved excellent results by combining these methods, as demonstrated in this work.

# 3.2. Modeling Metaheuristic Methods 

It is reasonable to use the principle of the golden section as a management factor of an enterprise's organizational and economic potential. The purpose of complex research and transformations is to bring them to an unexpectedly or expectedly simple conclusion and to discover the natural laws of the relation between the whole and its parts, the variety of recurrent sequences, essentially identical relationships, and inversion models that allow us to make harmonics, or the theory of harmony, which is the future. A harmonious production system is a complex of component parts (subsystems) interconnected according to the rule of the golden ratio. The management and organization of such a system should be based on the concepts of harmonious management [11,19].

To evaluate the effectiveness of the uncertainty interval reduction algorithm used by us for a given number of calculations of the optimization function $N$, we offer an additional auxiliary characteristic-the criterion for the relative reduction in the initial uncertainty interval $R(N)$. The physical essence of this criterion reflects the ratio of the length of the interval, which is obtained as a result of some number of $N$ calculations of the optimization function, to the length of the initial uncertainty interval:

$$
R(N)=\frac{\left|\tau_{N}\right|}{\left|\tau_{(0)}\right|}
$$

To perform optimization using the method of the golden section, the characteristic of the relative reduction in the initial uncertainty interval is determined by the following formula:

$$
R(N)=(0.618)^{N-1}
$$

where $N$ is the number of function calculations.
The current uncertainty intervals are as follows: $\tau_{0}, \tau_{2}, \tau_{3}, \tau_{4}, \ldots$. They reflect the fact that two function calculations are performed on the first iteration, $\tau_{0}$ and $\tau_{1}$, and on the following ones-one each for $\tau_{2}, \tau_{3}, \tau_{4}$, etc. The reduction in the length of the uncertainty interval is constant and is equal to the following:

$$
\frac{\left|\tau_{0}\right|}{\left|\tau_{2}\right|}=\frac{\left|\tau_{2}\right|}{\left|\tau_{3}\right|}=\frac{\left|\tau_{3}\right|}{\left|\tau_{4}\right|}=\ldots=\frac{1+\sqrt{5}}{2}=\cong 1.618
$$

If the value of $R(N)$ is given, then the number of computations of the optimization function that is required to achieve the desired accuracy is defined as the smallest integer that must satisfy the following condition:

$$
N \geq 1+\frac{\ln R(N)}{\ln 0.618}
$$

We offer a basic algorithm for optimizing the functioning of the construction production system based on the concept of the golden section method in optimization procedures. We form a sequence of stages of the optimization algorithm, which works according to the harmonic principle of the golden section (see Figure 6). The search for the optimal solution is most often reflected in the processes of saving material resources and assessing the level of optimality, which developers operate; therefore, we will develop the stages of the optimization algorithm using the method of the golden section to minimize the function $f(x)$ (Table 2).
![img-5.jpeg](img-5.jpeg)

Figure 6. The basic algorithm for optimizing the functioning of the construction production system based on the concept of the golden section method.

Table 2. The formulation of the algorithmic stages of the optimization algorithm based on the principle of the golden ratio in the improvement in production systems in construction.


The general harmonic $M S_{\text {harm }}$ model of the production system in the construction industry $S$ uses harmonic parameters $\theta$ as follows:

- The parameter of harmony of the development $\theta_{1}\left(\theta_{\text {dev }}\right)$;
- The parameter of harmony in production $\theta_{2}\left(\theta_{\text {prod }}\right)$;
- The parameter of harmony of the price system in the construction industry $\theta_{3}\left(\theta_{\text {price }}\right)$;
- The parameter of harmony of interests and motivations of labor resources of construction production $\theta_{4}\left(\theta_{\text {mot }}\right)$;
- The parameter of harmony of social inter-relations between construction organization and a consumer $\theta_{5}\left(\theta_{\text {social }}\right)$;
- The parameter of harmony of logistic chains $\theta_{6}\left(\theta_{\text {log }}\right)$;
- The parameter of harmony of the stability of the construction complex $\theta_{7}\left(\theta_{\text {stab }}\right)$.

These parameters coordinate the information characteristics for the operation of the harmony criteria $K_{\text {crit }}$ subsystem $S S_{\text {crit }}$ according to the golden division method. The procedure for analyzing the harmony criterion is carried out using the golden interval method, that is, the closeness of its coordinates to the value of the golden interval $K_{\text {crit }}$ $[x ; y] \approx[0.68 ; 0.32]$. If the value of the harmony criterion coordinate is not close to the golden division, then a selection of regulatory optimization influences (membranes) is carried out $\lambda_{\text {reg }}$ (membran). If the coordinate values of the harmony criterion are close to the golden division, then the production system continues to operate in the previous mode $S_{\text {prev.mode. }}$. During this time, the harmony control and accounting subsystem monitors the performance of the algorithm $S S_{\text {control }}$. After all these analytical procedures for making management decisions are followed, a state of harmonious functioning of the $F_{\text {harm }}$ production system of construction production $S$ follows.

The above study showed that construction production systems undergo an optimization platform in the process of their development and acquire a new progressive quality. When performing functions, system fluctuations determine the level of organization, which corresponds to harmonious (sustainable) development. The use of the "golden ratio" in the management of construction production in combination with information technologies contributes to the evolution and development of the structural diversity of production systems in a changing environment [2,20].

3.3. Modeling Bayesian Networks

The Bayesian Network depicted in Figure 7 is a probabilistic graphical model used to represent a set of variables and their conditional dependencies via a directed acyclic graph [30-32]. This specific network is designed to evaluate the design of a construction schedule and the potential disruptions affecting it [33-37]. In examining the harmonization of construction production management, the duration of construction processes was taken into account. A method of the harmonic management of the level of time in construction production is proposed. When determining the most probable date of completion of a construction investment, a harmonic approach can be applied.

![img-6.jpeg](img-6.jpeg)

Figure 7. A Bayesian Network diagram representing the dependencies between various factors in a construction schedule (own source in the Netica program, https://norsys.com/netica.html, accessed on 30 May 2024).

Applying the metaheuristic principle of the "golden ratio" to determine the expected time of completion of work, the following indicators are proposed:

- Estimated (according to the project) production process time $=1$;
- Harmonized production process execution time $=y$;
- Additional time reserve is $(1-y)$.

The ratio of harmonic proportions takes the following form: $y=0.38 ; 0.62-y=0.24$. It was determined that the work time reserve will be $24 \%$. Elements of harmonization of time reserves z were defined. From this, it follows that $z=0.24 ; 0.38-z=0.14$.

The network is for the assessment of whether a construction schedule is well designed, with probabilities assigned to 'YES' ( $47 \%$ ) and 'NO' (53\%). This initial assessment leads to an estimation of how likely the duration of construction activities was correctly estimated. There is a main node in the network, estimated time of the production process, and a mitigating node, additional time reserve, in proportion to the golden ratio. It was determined that the work time reserve would be $24 \%$. The elements of harmonization of time reserves $z$ are $0.24 ; 0.38-z=0.14$.

The following two disruptions affecting the process were also considered:

- D1: Probability of $46.5 \%$ if 'YES' and $53.5 \%$ if 'NO'.
- D2: Probability of $47.9 \%$ if 'YES' and $52.1 \%$ if 'NO'.

The probability indicates potential underestimation in project timing. Disruptions are more likely to occur than not, requiring contingency planning.

If one disturbance occurs, the analysis Figure 8 suggests that only $20 \%$ of construction schedules are well designed, while almost $80 \%$ do not meet expectations.

![img-7.jpeg](img-7.jpeg)

Figure 8. Diagram of a Bayesian Network with one disturbance (own source in the Netica program).
If two disturbances occur, the network is depicted as shown in Figure 9. The analysis suggests that only $15.5 \%$ of construction schedules are well designed, while a significant majority of $84.5 \%$ do not meet the necessary standards.
![img-8.jpeg](img-8.jpeg)

Figure 9. Diagram of a Bayesian Network with two disturbances (own source in the Netica program).
Both disruptions D1 and D2 have effects, indicating a high level of vulnerability in the construction process to these disruptions. For additional time reserve (Figure 10), the probability of correct estimation is more than $70 \%$, while almost $30 \%$ do not meet the necessary standards.

The practical application of the proposed method can be effectively demonstrated through the example of leveling a $5400 \mathrm{~m}^{2}$ plot of land using a bulldozer. The soil in this case falls under category II, with a total volume of $2600 \mathrm{~m}^{3}$. The conventional approach estimates that this process will require 8 days of work, assuming an 8-h working day. However, to optimize the process, we can reduce the duration to 6 days of harmonized working time, reserving an additional 2 days as a time buffer. This reduction represents approximately $24 \%$ of the total estimated time. Achieving this efficiency involves considering the following two distinct management approaches:

1. Balanced approach:

- A $38 \%$ emphasis on modern management practices (innovation);
- A $62 \%$ reliance on constant management experience.

2. Innovative approach:

- A $62 \%$ emphasis on modern management practices (innovation);
- A $38 \%$ reliance on constant management experience.
![img-9.jpeg](img-9.jpeg)

Figure 10. Diagram of a Bayesian Network with two disturbances. (Own source in the Netica program).
To determine the optimal solution, we employed Bayesian Networks. Expert assessments played a crucial role in this process, leading to a satisfactory outcome for the second option. Specifically, conditional probability tables were completed by five experts from Poland and Ukraine. These experts evaluated various factors related to the land leveling task. Their opinions were ranked and analyzed for consistency using Kendall's concordance coefficient. Remarkably, the study revealed a high level of agreement among the experts, as indicated by a coefficient value of $\mathrm{W}=0.9$.

In summary, the flowchart presents a complex process of time management in construction production, taking into account various factors and disruptions. It underscores the importance of a well-designed construction schedule and the accurate estimation of construction activity duration. Furthermore, it highlights the significant impact of disruptions on the construction process. This analysis can be used to improve the efficiency and effectiveness of construction project management.

# 4. Discussion 

The relevance of the search for the harmonious support of optimization procedures in construction in the direction of sustainable and logical development is justified. The use of metaheuristic techniques and a bionic approach has been shown to positively shape risk management systems. By mimicking the efficiency and precision of biological, molecular, and physical objects and nervous systems, construction processes can be optimized, and decision-making can be improved. This approach has been found to result in more efficient outcomes, providing crucial information on how to manage time harmoniously while considering the risk of disruptions. The components of harmonious production are revealed in improving the interaction of various departments and accelerating the response to unexpected changes, which will improve the level of successful work of any organization and improve the functioning of production systems.

The Bayesian Networks have been programmed based on the golden ratio, i.e., harmonized proportions have been introduced into the Bayesian Networks, making the results more effective. The golden ratio, a mathematical concept found in nature and art, was used to harmonize the proportions within the Bayesian Networks. This resulted in a more effective and efficient system, demonstrating the potential of integrating mathematical concepts into reasoning under uncertainty. This approach is not only a theoretical proposition but also shows promising practical applications. The preliminary research presented in this paper demonstrates that the approach is well founded and opens up broader possibilities. Based on the degree of orderliness of the optimization flow, a basic algorithm for optimiz-

ing the functioning of the construction production is presented. The production system is based on the concept of the golden section method and adapts to divergent interests, goals, and actions at all levels of management of various conditions. The developed algorithm could be successfully applied to both ongoing and planned construction projects, showing its practicality and effectiveness. The algorithmic stages of the golden section introduce harmonious (sustainable) development in the construction industry in achieving an optimization platform and acquiring progressive qualities.

In the results, it is shown that the integration of Bayesian Networks and heuristic techniques presents a promising approach to improve construction management. By mimicking the efficiency and precision of natural systems and using harmonized proportions, this approach can optimize construction processes and improve decision-making, potentially leading to more successful construction projects. The golden ratio was used in the process of modeling production systems in the Bayesian Network, which resulted in an increase in the stability of the production system, its functionality, and adaptive characteristics.

# 5. Conclusions 

The research presented in this paper underscores the potential of a bionic approach in the construction industry. The use of Bayesian Networks, programmed based on the golden ratio, has proven to be an effective tool for managing the construction process and its associated disruptions, the result of which is the creation of all conditions for the harmonious interaction of performers and equipment at all levels of construction management, which confirms the need for the development of modern production approaches based on the principles of harmony.

This research serves as a stepping stone towards a more efficient and resilient construction industry.

However, it is important to note that this paper presents an initial exploration into this innovative approach. Further research is needed to develop potential and limitations. Future work could focus on refining the algorithm, exploring its application in different types of construction projects, and investigating how it could be integrated into existing construction management systems. The aim of further research is to develop an algorithm that can predict the impact of disruptions during construction processes. This algorithm will leverage both the techniques developed in this paper and artificial intelligence. The aim is to create a tool that can not only manage but also anticipate potential challenges, thereby further optimizing construction processes. Further research and development will undoubtedly uncover more opportunities for improvement and innovation.

Author Contributions: Conceptualization, M.P.; methodology, M.P., A.S. and A.J.-G.; software, A.S. and A.J.-G.; validation, A.J.-G.; formal analysis, M.P. and A.S.; investigation, M.P., A.S. and A.J.-G.; writing-original draft preparation, M.P.; writing-review and editing, A.J.-G. and A.S. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by Gdansk University of Technology, grant ARGENTUM number 28/1/2022/IDUB/I3b/Ag.
Data Availability Statement: The datasets generated and analyzed during the current study are available on request.

Conflicts of Interest: The authors declare no conflicts of interest.
