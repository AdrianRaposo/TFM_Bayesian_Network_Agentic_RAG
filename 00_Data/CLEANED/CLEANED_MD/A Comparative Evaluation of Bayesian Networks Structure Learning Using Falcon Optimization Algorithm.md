# A Comparative Evaluation of Bayesian Networks Structure Learning Using Falcon Optimization Algorithm 

Hoshang Qasim Awla ${ }^{1 *}$, Shahab Wahhab Kareem ${ }^{2,3}$, Amin Salih Mohammed ${ }^{3,4}$<br>${ }^{1}$ Department of Computer Science, Faculty of Science, Soran University, Erbil (Iraq)<br>${ }^{2}$ Department of technical information system Engineering, Erbil Technical Engineering College, Erbil Polytechnic University, Erbil (Iraq)<br>${ }^{3}$ Department of Information technology, College of Engineering and computer science, Lebanese French University, Erbil (Iraq)<br>${ }^{4}$ Department of Software and Informatics, College of Engineering, Salahaddin University-Erbil (Iraq)

Received 16 January 2020 | Accepted 16 September 2022 | Published 19 January 2023

## ABSTRACT

Bayesian networks are analytical models that may represent probabilistic dependent connections among variables and are useful in machine learning for generating knowledge structure. Due to the vastness of the solution space, learning Bayesian network (BN) structures from data is an NP-hard problem. The score and search technique is one Bayesian Network structure learning strategy. In Bayesian network structure learning the Falcon Optimization Algorithm (FOA) is presented and evaluated by the authors. Inserting, Reversing, Moving, and Deleting, are used in the method to create the FOA for finding the best structural solution. The FOA algorithm is based on the falcon's searching technique during drought conditions. The suggested technique is compared to the score metric function of Pigeon Inspired search algorithm, Greedy Search, and Antlion optimization search algorithm. The performance of these techniques in terms of confusion matrices was further evaluated by the authors using a variety of benchmark data sets. The Falcon optimization algorithm outperforms the previous algorithms and generates higher scores and accuracy values, as evidenced by the results of our experiments.

## Keywords

Bayesian Network, Falcon Optimization Search Algorithm, Global Search, Local Search, Score And Search, Structure Learning.

DOI: 10.9781/ijimal.2023.01.004

## I. INTRODUCTION

In machine learning, Bayesian networks (BN) are one of the main analytical models for developing the probabilistic structure of knowledge [1]. They may be used in a variety of contexts, including knowledge design, argumentation, and inference [2]. There are two stages to learning a Bayesian network: parameter learning and structure learning. The focus of this paper is on Bayesian network structure learning. In structure learning, three procedure is needed such as strategies on the conditional independence, calculating score for optimization technique, and combining different approaches [3]. In Bayesian network, directed acyclic graph (DAG) is the main structure, and this structure contain two components key: parameters and network structure. The structure displays interrelationships between variables, whereas the parameters represent conditional probabilities. Without a great search technique, it's hard to solve the Bayesian network's learning structure. Meanwhile, although learning the Bayesian network structure from a dataset to produce the best

[^0]result is NP-hard [4] a lot of work has gone into developing estimate methods for learning the network structure. Generally, constraint based approach and score-and-search strategy are two different mechanism in structure learning of Bayesian network [5]. The main mechanism for searching on the Bayesian network space is score and search mechanism, and continuously evaluate each potential network structure until the correct metric value is found.

Score-based methods utilize a metric to quantify the network and data available before looking for a structure that maximizes the score [6]. The scoring function method was implemented using two key criteria: one of them is Bayesian score, and the second is Information-theoretic score. Information-theoretic score has been used by the Normalized Minimum Likelihood (NML), BDeu (Bayesian Dirichlet equivalent uniform ("u" for uniform joint distribution), Bayesian Information Criterion (BIC) and log-likelihood (LL), Minimum Description Length (MDL), and Akaike Information Criterion (AIC) [7]. The Bayesian score is used in K2, BDe (Bayesian Dirichlet ("e" for likelihoodequivalence), BD (Bayesian Dirichlet), and Mutual Information Tests, (MIT) [8]. There are several sorts of search strategies for discovering the optimal solution to the structure learning issue. Simulated Annealing Algorithm [7], Particle Swarm optimization [9], Ant Colony Algorithm [10], Antlion optimization [3], Hybrid Algorithms


[^0]:    * Corresponding author.

    E-mail address: hoshang.awla@soran.edu.iq

([11], [12], [13], [14], [15] [16]), Bacterial Foraging Optimization [17]., Breeding Swarm Algorithm (20), Genetic Algorithms (GOMEA) [18][19], Falcon optimization is another reducing met heuristic for Bayesian network structure learning. These findings suggest and examines this method for addressing the Bayesian network structure learning difficulty. BNs are increasingly useful mechanisms for risk assessment, risk evaluation, resource planning for data science and environmental management.

BNs is simple and straightforward graphical presentation that is used to manage causal inference and risk monitoring, so they have a lot of benefits over regression-based methods. The Bayesian network is frequently used this to clearly visualize the connection between the emergence of several major illnesses and patient related variables during the time [22]. The rest of this paper will be arranged as follows. The notion of structure learning in Bayesian networks is introduced in Section II. The Falcon Optimization Search Algorithm in Section III, is briefly introduced. In section IV, we go through the approach in depth and show the results of the experiment. Section V contains the conclusions.

## II. Structure Learning of Bayesian Networks

The Bayesian network is essentially made up of two parts: (G, P).
The DAG G(V; E) denotes a collection of conditional probable distributions (CPD) that includes all variables Xi. $\mathrm{P}=\mathrm{P}$ (Xi | Pa (Xi) denotes a set of conditional probability distributions (CPD) that includes all parameters Xi (vertices from a graph). Pa(Xi) commonly denotes the parents of the node Xi in G [29]. Probabilistic as a simple pairing for a $(\mathrm{G} ; \mathrm{P})$ network may be outlined to apply this equation (1):

$$
P\left(X_{i}, \ldots X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P \alpha\left(X_{i}\right)\right)
$$

A scoring function, is based on a number of factors, including Bayesian techniques, information and entropy, and the length of the minimal description [30]. Bayesian network posterior probability may be stated as follows using Bayesian inference rules:

$$
P(G \mid D)=P(D \mid G) \cdot P(G) / \sum_{G^{\prime}} P\left(D \mid G^{\prime}\right) P\left(G^{\prime}\right)
$$

$\mathrm{P}\left(\mathrm{G}^{\prime}\right)$ is the posterior probability and reflects the parameters of the model in equation (2). As a result, as long as the minimum probability of all potential structures is known, It is possible to establish the prior probability of the network structure. [31]. P(D|G) stands for marginal likelihood and is defined: $\mathrm{P}(\mathrm{D})$ is used as a normalizing constant:

$$
P(D \mid G)=\int P(D \mid G, \theta) P(\theta \mid G) d \theta
$$

$\mathrm{P}(\mathrm{D})$ in Byesian network structure is supposed to be independent of network G. Structure learning methods compare the present and prior scores of the structure using score-based methods. [32] is the final representation of the score:

$$
\begin{aligned}
& \operatorname{BDe}(G, D)=\prod_{i=1}^{n} B D e(X i, \\
& \Pi \mathrm{Xi})=\prod_{i=1}^{p} \prod_{j=1}^{q i}\left\{\frac{\Gamma(\alpha \mathrm{ij})}{\Gamma(\alpha \mathrm{ij}+\mathrm{nii})} \prod_{k=1}^{r r} \frac{\Gamma(\alpha \mathrm{ij}+\mathrm{nii} \mathrm{k})}{\Gamma(\alpha \mathrm{ijk})}\right\}
\end{aligned}
$$

where:

- p is the number of nodes in G ;
- ri is the number of classes regarding node Xi ;
- qi is the number of preparations from the groups of Xi's parents;
- nijk denotes the amount of participants who might have node Xi's jth class and its parents' kth arrangement.


## III. Falcon Optimization Algorithm

Metaheuristics are algorithms that are inspired by nature and are used to find approximate solutions to computationally difficult optimization problems. Metaheuristics have been used to exploit swarming characteristics of animals such as the Firefly-BAT [33], Cuckoo [34],GWO [35], Deep multi-model fusion [36]antlion, pigeon, fish, bee, and others. Homogeneity, adaptability, illation-free tools, and the capacity to avoid local optima are all characteristics of metaheuristics [37]. The suggested metaheuristic algorithm in [38] was inspired by the falcon's hunting activity. The For probabilistic inhabitants' tasks, the Falcon optimization search algorithm is a dependable and stable process that encourages parameter values for its three item resolution.

The proposed strategy was inspired by the chasing style of falcons when on the hunt for prey while in flight. Falcons strategy foe hunting is determined by their needs. However, specific strategies emerge.

Based on several studies [39], [40]. Falcons are high-performance fliers among birds. The suitable targets are examined for the boundaries of flying achievement in distinct stages of heightened hunting [41]. Determining the physical power of flight, calculating average flight velocities, and responding to wind are some of the flight implementation strategies in the framework. [41]. Falcons are one of the fastest animals on the planet, with stoops reaching speeds of above $300 \mathrm{~km} / \mathrm{h}$. Falcons can breathe freely due to little thin tubercles in their noses that direct air via high-speed stoops. The majority of the hunting will be done in the morning and at night. The predominant source of food is small-medium-sized birds, with insects such as cicadas, moths, and locusts arriving only occasionally [42].

Falcons approach their prey in a number of ways while flying. The route is divided into two sections: the first section is logarithmic curve in which the falcon keeps it's own head straight whereas peering slantingly the prey in the outcomes acuity, the second one is a straight segment in which the falcon wants to fly to a prey if in the vision and dives when it becomes close to it. As a result, the falcons mainly obtain a movement which can be separated into three phases: the First Phase, which involves prey exploration; the Second Phase, which involves improving the look into the logarithmic curve; and Third Stage, which involves the dive itself, which can lead to the success outcome, like as picking a prey. Instead, depending on its prior experiences, the falcon immediately changes its behavior. The five steps of a quick method to adopting FOA are shown below [38].

Step 1: Determine the parameters of the optimization task, such as falcons number (NP), limit of speed (Vmax), rate of (cc) cognitive rate, the social constant (sc), the following constant (fc), probability of dive (DP), and the alertness probability (AP) (AP).

Step 2: Based on the boundary conditions where each falcon's position is established, assign the falcons' velocity and location in a D-dimensional space at random, while keeping the number of NP candidates in all D dimensions in mind. Between the Vmax and Vmin limitations, which are established as follows, the velocities are generated at random:

$$
\begin{aligned}
& \text { Vmax }=0.1^{*} \text { ub } \\
& \text { Vmin }=-\text { Vmax }
\end{aligned}
$$

Where ub denotes the upper border of each dimension's boundary region. Create the pairings of values ( $\mathrm{pAP}, \mathrm{pDP}$ ) for each falcon at random to compare with the awareness and dive probability.

Step 3: Find the best (xbest) and global (gbest) locations by calculating the fitness value. This fitness value, of, is calculated for each bird. The chosen positions will be utilized to create new locations based on the logic that governs the dive's movement and the probabilities of awareness.

# Algorithm: Structure Learning of Bayesian Network based on falcon optimization algorithm 

## INPUT: - datasets

Population size, NP;
Maximum speed, Vmax;
Values of cognitive Cc, social, Sc and following Fc, constant.
Value of awareness Probability (AP) and Dive probability (DP);
$t_{\text {max }}:$ maximum number of iteration number: $X_{\text {max }}:$ upper boundary, and $X_{\text {min }}:-$ lower boundary

## OUTPUT: - learning Bayesian Network

1. The initialized empty structure and initialize parameters of FOA algorithm (dimension space D_"s " size of population NP, the constant value ofCc, Sc and Fc, Awareness AP and Dive DP probability, the number of iteration number, upper boundary and lower boundary, $\left(G_{\text {best }, i t}^{l}\right)$.
2. Set the velocity and position for all Falcon randomly. Comparing each falcon by BDe score function, and find the best in the current position $\left(P_{\text {best }, i, d}^{l}\right)$.
3. For loop to maximum iteration number
4. For loop to size of population
5. Generate the random value $p A P, p D P$. Select a new best position by comparing the BDe score function of each falcon.
6. if $p A P<A P$, update falcon velocity $\left(V_{t}, d\right)$ using equation 7 .
else if $p D P>D P$ update faicon velocity using Equation 8 .
else compare the score function of the current and previous one if its better update falcon velocity using Equation 9 otherwise use equation 10.
7. Update the position $X$.
8. Evaluate BDeu score function of new position $\left(X_{t, d}^{l}\right)$
a. If current position $\left(X_{t, d}^{l}\right)$ is better than the best position $\left(P_{\text {best }, i, d}^{l}\right)$ then update the best position by $\left(\left(P_{\text {best }, i, d}^{l}\right)=\left(X_{t, d}^{l}\right)\right)$
b. If $\left(G_{\text {best }, i, d}^{l}\right)<$ current position then update the best solution for global by $\left(G_{\text {best, id }}^{l}=\left(X_{1}, \beta\right)\right)$
c. The best score value and solution are saved.
d. If $X_{\text {min }} \geq X_{\text {max }}$, stop the iteration process, and the results are present. If not, move into Step 5.
9. Return the maximum BDe score.

## Fig. 1. FOA for Bayesian Network Structure learning.

Step 4: Make new locations, repositioning the falcon as required. Based on its own and other falcons' experiences, the falcon examines the pAP to the aware probability AP, and if the attention probability AP is greater than the pAP, the falcon avoids pursuing preys:

$$
\text { Xiter }+1=\text { Xiter }+ \text { Viter }+ \text { cc (Xbest, Xiter) }+ \text { sc (gbest, Xiter) }
$$

where Viter represents existing velocity and Xiter represents the falcon's current location.

Compare the probability of dive DP with pDP if AP is smaller than pAP. If DP is smaller than pDP, the falcon (Xchosen) selects one of the targets as prey and completes the first phase in the hunting process. The logarithmic spiral is calculated as follows:

$$
X_{\text {iter }+1}=X_{\text {iter }}+\left|X_{\text {chosen }}-X_{\text {iter }}\right| \exp (b t) \cos (2 \pi t)
$$

where a fixed number is $b$ and takes the position of the logarithmic spiral that matches 1, and number as a random will be $t$ in the range $(-1,1)$ that defines the falcon's next exact location [38].

While AD is more than pAP, compare the preferred prey's score function to the falcon's scoring function, and the falcon will follow the preferred prey wherever it is most suitable, like in a dive step:

$$
\text { Xiter }+1=\text { Xiter }+ \text { Viter } 1+f c * \text { rand (Xchosen }- \text { xiter) }
$$

The falcon, on the other hand, continues to fly around the optimal position:

$$
\text { Xiter }+1=\text { Xiter }+ \text { Viter } 1+c c \wedge * \text { rand (Xbest, Xiter) }
$$

Later, new location is assessed in terms of velocities and location bounds. The new scoring function is then computed, as well as the updated values of gbest and Xbest.

Step 5: After that, the assessments from step 4 are repeated until the iterations of maximum number (itermax) is obtained. Fig. 1 shows the falcon optimization method for structure learning Bayesian networks as a proposed technique. Falcon G0, which illustrates a DAG using arcs in Fig. 2, tries addition, move, reversal, and deletion, going to new solutions G1, G2, G3, and G4.G3 will be chosen since it has the greatest score; the falcon will then continue to investigate using a similar strategy to arrive at $\mathrm{G}+3$ as the next alternative. If the $\mathrm{G}+3$ BDeu score is higher than the G+1 BDeu score, the G+3 BDeu score is used, the falcon will do a similar operation. The methods iterate while the score of BDeu is fix or repetition loop reaches its maximum length. During the whole operation, the falcon must pick between deletion, movement, reversal, and addition.
![img-0.jpeg](img-0.jpeg)

Fig. 2. Searching steps for one Falcon [12].

TABLE I. Score Function Calculation for PIO, ALO, FOA, and Greedy Within Execution Times of 2, 5, and 60 Minutes


## IV. EXPERIMENTAL Evaluation

A common assessment approach is used to evaluate the performance of FOA, which employs probabilistic datasets collected from prominent Bayesian networks benchmarks. A PC with the following characteristics serves as the experimental platform: The method is implemented in Java and runs on a 4GB RAM, 2.1GHz CPU, Core i3, operating system (Ubuntu 14.04). We looked examined the suggested algorithm's characteristics in a number of static datasets, including: Asia ( 8 variables, 8 arcs, and 3000 instance), Static Banjo ( 33 variables and 320 instance), Letter ( 17 variables and 20000 instance), Heart(22 variables and 267 instance), Epigenetics ( 30 variable and 72228 instance), Alarm ( 37 variables, 46 arcs, and 10000 instance ), Hailfinder ( 56 variables, 66 arcs, and 2656 instance), WDBC ( 9 variables and 1000 instance), Hepar ( 70 variables, 123 arcs, and 350 instance), Water (32 variables, 66 arcs, and 10083 instance), Child ( 20 variables, 25 arcs, and 230 instance), Imports( 22 variables and 205 instance), Sensors( 25 variables and 5456 instance), Insurance ( 27 variables, 52 arcs, and 3000 instance), win95pts ( 76 variables, 112 arcs, and 574 instance), Andes ( 223 variables, 338 arcs, and 500 instance), Hepatitis( 35 variables and 137 instance), Soybean ( 35 variables and 307 instance), Lucas01(10 variables and 10000 instance), Adult ( 16 variables and 30162 instance), Parkinsons ( 23 variables and 195 instance), Mushroom ( 23 variables, 1000 instance), and Lucap02 (143 variables and 10000 instance) [43].

The learning datasets we looked at stationary sets, and this study is built on the assumption of stationary data. Extending the FOA technique to Andes and sensor benchmarks or other types of stream data sets in online is a hard task that may attempted after a thorough evaluation of its effectiveness on stationary data sets.

The authors used relevant metrics for the datasets to compare the outcomes with Pigeon optimization algorithm (PIO). Greedy Search (GS), and Antlion optimization algorithm (ALO). We assessed all techniques under the identical settings after determining the parameters of the FOA algorithm. For the experiments in the FOA, the following values were used: N is the population size, $\mathrm{AP}=0.3$, and tmax is $1,000 . \mathrm{Sc}=3, \mathrm{Cc}=2, \mathrm{Fc}=4$, (t) is a random value within the range of $[-1,1], \mathrm{Vmax}=0.1 \mathrm{ub}$ (ub is 100 , and Vmax is 10 ), and DP is 0.85 are fixed value of the FOA's optimization. Pigeon Inspired algorithms have parameters such as dimension space D, population size Np, factor $R$ for map and compass, number of iterations Nc1 max and Nc2 max for two operators, and Nc2 max $>$ Nc1 max.The Antlion optimization algorithm parameters are: dimension space D, population size NE, number of iterations, upper and lower boundaries (Xmax and Xmin), and Xmax $>$ Xmin. The algorithms were implemented in three distinct time frames: two minutes, five minutes, and 60 minutes.

Table I displays the scores for those algorithms which is known
in this paper in the specified datasets, as well as time values. In all circumstances, the recommended approach outperforms the default Greedy Search, Antlion Algorithms, as indicated in the table. This illustrate that FOA obtain the best score in the quickest time possible.

Confusion matrix implemented for all data sets and network structure to assess the efficacy of structure identification. The metrics FN, TP, TN, and FP, the criteria Sensitivity (SE), F1 Score, Average Hamming Distance (AHD), and Accuracy (Acc), have been computed for each network per method.

$$
\begin{aligned}
& \text { sensitivity }=\frac{T P}{T P+F N} \\
& \text { accuracy }=\frac{T P+T N}{T P+F P+T N+F N} \\
& \text { F1 Score }=\frac{2 * T P}{2 T P+F P+F N} \\
& \mathrm{AHD}=\frac{F N+F P}{T P+T N+F P+F N}
\end{aligned}
$$

Defining these metrics illustrated as: A TP is a learning network arc (vertex or edge) that is located in the correct location. The arc that travels through neither the learning nor the regular networks is known as TN. The arc of the learning network, not the arc of a regular network, is FP. The FN is the arc in a conventional network, but not in a learning network. PIO, FOA, ALO, and Greedy Sensitivity Results, are illustrate in Fig. 3. The FOA produces best values than the PIO, Antlion, and Greedy search in diffrent datasets.

As demonstrated in Fig. 4, the suggested technique has higher accuracy values in the most dataset than the PIO, ALO, and Greedy methods. The suggested FOA Learning Algorithm is effective in determining the correct structure. As a consequence, in most datasets, the Iterative FOA method outperforms other algorithms in terms of prediction accuracy, and the FOA also outperforms other algorithms findings, we utilized F1 as a metric of the model's accuracy for performance metrics.

The Falcon optimization algorithm's performance is evaluated using the Precision, Recall, F1-score. In these cases, Precision is the The number of total network edges in anticipated BN splited with the number of successfully identified directed edges. Recall is achived by dividing the directed edges number identified by total number for edges in the BN. It recognizes that the harmonic average of accuracy and recall is F1. The scenario is depicted in Fig. 5. FOA, ALO, PIO, and Greedy searches are compared. As demonstrated in Fig. 5, the suggested approaches outperform the ALO, Greedy search, and PIO methods. Furthermore, accuracy is an important criterion for measuring model performance since the model's ultimate purpose is to provide a

![img-1.jpeg](img-1.jpeg)

Fig. 3. Sensitivity for SA, GS, FOA, and PIO.
![img-2.jpeg](img-2.jpeg)

Fig. 4. Accuracy for SA, GS, FOA, and PIO.
![img-3.jpeg](img-3.jpeg)

Fig. 5. F1_Score for SA, GS, FOA, and PIO.

![img-4.jpeg](img-4.jpeg)

Fig. 6 AHD for SA, GS, FOA, and PIO.
useable illustration of the real world. In terms of Hamming distances, the proposed approach beats the DAG space algorithm, which is always much smaller. Because local networks are entirely focused on exploration rather than inference, main assessment measures for BN structure learning is hamming distances because it directly suits the structure of learners. The Average Hamming Distances for the methods presented are shown in Figure 6. The findings show that the proposed strategy delivers higher performance values than the other strategies we looked at.

## V. CONCLUSION

The authors have focused on Bayesian network structure learning and used Falcon Inspired Optimization method to tackle the problem. We employed the search and score strategy using the FOA algorithm as search function and BDeu as the scoring function. FOA is a stochastic optimization technique based on falcon navigational behavior.

FOA is a method for locating a discrete solution search space that may be applied to any task. The falcon can employ FOA to lead a logarithmic spiral to the lowest usable solution space, which allows for quicker concentration to the global extremum. The proposed technique has a greater search capability, which implies it can find better structure solutions, calculate THE VALUE score function, and properly measure network structure. The strategies help to speed up global convergence and improve global search efficiency. We want to investigate other important aspects of the FOA, such as efficiency, resource use, and run time analytics, BY using THE BEST data sets and experimental configurations.

## Amin Salih Mohammed

Dr. Amin Salih Mohammed is the President of the Lebanese French University in Erbil, Iraq's Kurdistan region. He was the university's Vice President for Scientific Affairs before being promoted to President. He has more than 15 years of expertise in both teaching and research. Amin is a dedicated scholar who has served as a resource for a variety of seminars and faculty development programs hosted by various schools. He earned his undergraduate, postgraduate, and doctoral degrees in computer engineering from the Kharkiv National University of Radio Electronics in Kharkiv, Ukraine. Computer networks, wireless networks, and cloud computing are among his research interests.
![img-7.jpeg](img-7.jpeg)

Hoshang Qasim Awla
Hoshang Qasim received his BSc in Computer Science/ Soran University /Iraq in 2012 and his MSc in Computer Engineering from Hassan Kalyouneu University/ Turkey in 2016, and a Ph.D student in data science from Soran University. Assistant lecturer at the computer science department/ faculty of science at Soran University, email address: hoshang.awla@soran.edu.iq