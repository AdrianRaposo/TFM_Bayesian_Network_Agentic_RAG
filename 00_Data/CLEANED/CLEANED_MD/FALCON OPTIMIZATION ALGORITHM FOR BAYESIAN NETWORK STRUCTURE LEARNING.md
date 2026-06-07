# Shahab Wahhab Kareem <br> Mehmet Cudi Okur 

## FALCON OPTIMIZATION ALGORITHM FOR BAYESIAN NETWORK STRUCTURE LEARNING


#### Abstract

In machine-learning, some of the helpful scientific models during the production of a structure of knowledge are Bayesian networks. They can draw the relationships of probabilistic dependency among many variables. The score and search method is a tool that is used as a strategy for learning the structure of a Bayesian network. The authors apply the falcon optimization algorithm (FOA) to the learning structure of a Bayesian network. This paper has employed reversing, deleting, moving, and inserting to obtain the FOA for approaching the optimal solution of a structure. Essentially, the falcon prey search strategy is used in the FOA algorithm. The result of the proposed technique is associated with pigeon-inspired optimization, greedy search, and simulated annealing that apply the BDeu score function. The authors have also examined the performances of the confusion matrix of these techniques by utilizing several benchmark data sets. As shown by the experimental evaluations, the proposed method has a more reliable performance than other algorithms (including the production of excellent scores and accuracy values).


Keywords Bayesian network, global search, falcon optimization algorithm, structure learning, search and score

Citation Computer Science 22(4) 2021: 553-569

Copyright (C) 2021 Author(s). This is an open access publication, which can be used, distributed and reproduced in any medium according to the Creative Commons CC-BY 4.0 License.

# 1. Introduction 

One of the simplified analytical models for constructing the probabilistic structure of knowledge in machine-learning is a Bayesian network (BN) [13]. Such a model can be applied as a learning method for combining knowledge, arguments, and inference [8]. The structure of a Bayesian network is a directed acyclic graph (DAG) that is composed of two significant parts; the parameters, and the structure of the network. The conditional probabilities are represented as parameters, and the dependencies among the variables are displayed as the structure. It is difficult to solve a Bayesian network's structure learning without a proper search method. The difficulties for learning from a data set for the structure of a Bayesian network to achieve the optimal is NP-hard class [20]; however, a comprehensive investigation becomes conducted to improve the approximate approaches for the learning structure of the network. Usually, there are two types of structural learning procedures for Bayesian networks. The first type is a constraint-based procedure, and the second is a classification and search procedure [22]. The score and search method is applied to examine the range that concerns the structures of a BN, which include continuously estimating all candidate network structures until an actual metric score is obtained. Score-based methods depend on a function to evaluate the network and accessible data and constantly look for a structure that improves the score (which is the ultimate goal) [7]. The score function method is implemented by using two primary criteria: a Bayesian score, and an information-theoretic score. A Bayesian score is performed in some other techniques like K2, BD (Bayesian Dirichlet), BDe (Bayesian Dirichlet [the "e" stands for likelihood-equivalence]), and BDeu (Bayesian Dirichlet equivalent uniform [the "u" stands for uniform joint distribution]). The information-theoretic score is implemented in techniques such as the Akaike information criterion (AIC), log-likelihood (LL), minimum description length (MDL), Bayesian information criterion (BIC), mutual information test (MIT), and normalized minimum likelihood (NML) [3]. There are various techniques of a research strategy that are intended to improve the problem of structural learning; these include particle swarm intelligence [4], the ant colony optimization algorithm [27], bee colony [13], the hybrid algorithm ( $[11,15,21]$ ), the simulated annealing algorithm [26], bacterial foraging optimization [33], genetic algorithms [19], the gene-pool optimal mixing evolutionary algorithm (GOMEA) [24], the breeding swarm algorithm [18], the binary encoding water cycle [32], pigeon-inspired optimization [16], tightening bounds [6], A* search algorithms [34], scatter search documents [5], the cuckoo optimization algorithm [1], quasi-determinism screening [25], and the minimum spanning tree algorithm [28]. Another additional metaheuristic technique that can be applied to learn the structure of Bayesian networks is falcon optimization. Here, this article proposes and presents a relative evaluation of this approach as a new method for solving the learning problem of a Bayesian network structure. The models of BN integrate with the administration for decision networks, the fundamental formulation of causal systems, mixed continuous and discrete variables, quantum probability, Bayesian neural networks, state-and-transition

standards, object-oriented and agent-based standards, geographic information systems, and other fields. BNs are becoming valuable mechanisms in risk management, risk analysis, and decision science for resource planning and environmental management. BNs are natural and compact graphical descriptions that can be utilized to manage causal reasoning and risk evaluation examination and allow many benefits beyond regression-based approaches [14]. A Bayesian network is used to present a short description of the relationship among the appearance of many chronic diseases and patient-level risk circumstances over time $[14,17]$. A structure-learning challenge can be viewed as an inference problem where the variables define a selection of parents for any node within a graph. The major combinatorial problem arises from the global constraint that the graph structure must be acyclic. We called the structure learning problem a linear program over the polytope represented by valid acyclic structures. In decreasing this problem, the authors maintain an outer bound approximation to the polytope and imperatively stretch it by searching for a new kind of validity constraint. If a full solution is found, it is proven to be an optimal Bayesian network.

The arrangement of this article is as follows. Following the introduction, Section 2 presents the approach of Bayesian network structure learning in general. The short introduction of the falcon optimization algorithm is presented in Section 3. In Section 4, the authors present the methodology in detail and show the experimental results. The final section concludes the article.

# 2. Bayesian network structure learning 

Essentially, one can express a Bayesian network utilizing two elements $-G ; P$. The first element $G(V ; E)$ is the DAG, which include the predictable group of nodes (or vertices), $V$, which is interconnected across identified links (or edges), and $E$. The second elements $-P=P\left(X_{i} \mid P a\left(X_{i}\right)\right)$ - describe the combination of conditional probabilistic distributions (CPD) that are specific to every variable $X_{i}$ (vertices from a graph). Furthermore, $P a\left(X_{i}\right)$ denotes the group of parents of node $X_{i}$ in $G$ [14]. Based on this model, a simple possibility group of a network $(G ; P)$ can be described by the following:

$$
P\left(X_{i}, \ldots X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)]
$$

On the other hand, a score function is based on different principles (which include information and entropy), Bayesian approaches, and minimum description length [17]. According to the rules of Bayesian inference, the posterior probability of a Bayesian network can be expressed as follows:

$$
P(G \mid D)=\frac{P(D \mid G) \cdot P(G)}{\sum_{G^{\prime}} P\left(D \mid G^{\prime}\right) \cdot P\left(G^{\prime}\right)}
$$

In (2), $P(D \mid G)$ is a finite probability, which is determined by using the normalization constant $P(D)$ as

$$
P(D \mid G)=\int P(D \mid G, x) \cdot P(x \mid G) \cdot d x
$$

$P(D)$ is assumed to be independent of Bayesian network structure $G ; x$ represents the model parameter, and $P\left(G^{\prime}\right)$ is the prior probability. Therefore, as long as the limited probability of all potential structures is calculated, the posterior distribution of the network structure can be determined [4]. The methods of structural learning apply class-based procedures by analyzing past and current structure results. The final expression of the result is as follows [2]:

$$
\operatorname{Score}(G, D)=\sum \operatorname{Score}\left(X_{i}, P a\left(X_{i}\right), D\left(X_{i}, p a\left(X_{i}\right)\right)\right)
$$

# 3. Falcon optimization algorithm 

Metaheuristics are nature-inspired algorithms for obtaining comparative solutions to any computationally difficult optimization problems. The swarming behaviors of animals (including firefly-BAT [35], cuckoo [9], ant, pigeon, fish, bee, etc.) have been used in metaheuristics [10]. The amazing characteristics behind the metaheuristics hold identity, illation-free tools, adaptability, and local optima eschewal ability [23].

In [31], the proposed metaheuristic algorithm depends on the falcon's behavior of hunting. The falcon optimization algorithm (FOA) is the reliable and robust algorithm of stochastic population-based problems that requires arrangements from several parameters to its three-stage action settlement.

The motivation of the proposed method was the chase style of falcons while they are seeking their prey during flight. Falcons are recluses, and their tactics for hunting depends on their requirements. However, specific tactics arise, and amazing models hold the fundamental precepts about the flight. Based on many products of Tucker [29,30], Among birds, high-performance flyers are falcons. In various states of elevated hunting, the fitting objectives are checked for the limits of flying achievement [30]. The implementation technique of flight in the framework include determining a standardized power about the flight, the flight average velocities, and adaptive responses to the wind [30]. One of the quickest animals in the world is a falcon; stoops have been shown to approach velocities that are faster than $300 \mathrm{~km} / \mathrm{h}$. Small thin tubercules in their beaks lead the air through high-speed stoops, allowing falcons to breath easily. The primary hunting is done throughout the day (including morning and night). They primarily feed on small and medium-sized birds, but their diets also include insects like cicadas, moths, and locusts (although such prey is rare) [12].

During flight, falcons take different routes to reach their prey. Each route has two parts: the first part is a logarithmic spiral on which a falcon continually keeps its head straight while peering at the prey with the highest visible acuity; and the second is when the falcon flies toward the prey in a straight segment - when the prey

is within the falcon's field of vision, the falcon dives. Therefore, a falcon's achieve locomotion can be classified into three steps: the initial step (first stage) - exploring for prey; the second step (second stage) - improving its dive through a logarithmic spiral; and the third step (third stage) - the dive itself (which can result in success; i.e., acquisition of prey). Otherwise, a falcon quickly reverses its action depending on it is experience.

The quick procedure, which includes five steps for the implementation of the FOA, is given below [31].
Step 1: Start the algorithm by adjusting the parameters for the optimization problem, including the number of falcons $(N P)$, highest speed $(V \max$ ), cognitive rate $(c c)$, social $(s c)$ constant, following $(f c)$ constant, dive probability $(D P)$, and awareness probability $(A P)$.
Step 2: Set the velocity and position of the falcons randomly in a D-dimensional space based on the boundary conditions, where the position of each falcon is defined in consideration of the number of $N P$ applicants within all of its D dimensions. The speeds are arbitrarily produced among the $V \max$ and $V \min$ limitations, where both are respectively determined as follows:

$$
\begin{aligned}
& V \max =0.1 \cdot u b \\
& V \min =-V \max
\end{aligned}
$$

where $u b$ denotes the upper bound (the boundary area concerning each dimension). In the beginning, generate the pairs of numbers randomly $(p A P, p D P)$ for each falcon for correspondence among the dive and awareness probabilities.
Step 3: Calculate the fitness value and select the best ( $x$ best) and global ( $g$ best) sites. The selected positions will be used to produce new positions considering the logic that rules the move behind the dive and awareness probabilities.
Step 4: New locations are produced, including updating the location of the falcon. Then, compare pAP with the probability of awareness $A P$; if $A P$ is bigger than $p A P$, the falcon moves from seeking for prey based on its activity (including some different experiences of the other falcons):

$$
X_{i t e r+1}=X_{i t e r}+V_{i t e r}+c c\left(X_{b e s t}, X_{i t e r}+s c\left(g_{b e s t}, X_{i t e r}\right)\right.
$$

where $V_{i t e r}$ is the current velocity and $X_{i t e r}$ is the current position of the falcon. If $p A P$ is bigger than $A P$, formerly compare a dive likelihood $D P$ among $p D P$. If $D P$ is less than $p D P$, then one of the targets is chosen as prey by the falcon ( $X_{\text {chosen }}$ ), and it completes its fundamental step toward hunting. A logarithmic spiral is provided through

$$
x_{i t e r+1}=X_{i t e r}+\left|X_{\text {chosen }}-x_{i t e r}\right| \cdot \exp ^{b t} \cos (2 \pi t)
$$

where $b$ is a fixed number that determines the state of the spiral logarithm (equal to 1), and $t$ is an arbitrary number within range $(-1,1)$ that determines

the next location of the falcon with respect to its exact destination [31]. If $A D$ is bigger than $p A P$, formerly compare the score function of the preferred prey and the score function of the falcon. Wherever the prey is most appropriate, it will be followed through by the falcon related to a dive step:

$$
X_{\text {iter }+1}=X_{\text {iter }}+V_{\text {iter }+1}+f c \cdot \operatorname{rand}\left(X_{\text {chosen }}-X_{\text {iter }}\right)
$$

otherwise, falcon continues to fly based in its best position:

$$
X_{\text {iter }+1}=X_{\text {iter }}+V_{\text {iter }+1}+c c \cdot \operatorname{rand}\left(X_{\text {best }}, X_{\text {iter }}\right)
$$

The new location that is evaluated later concerns the velocities and location boundaries. Next, its new score function is computed, and the new values of $X_{\text {best }}$ and gbest are determined.
Step 5: Last, subsequent evaluations of Step 4 are continued until the highest number of iterations (itermax) is reached.

Algorithm: Structure Learning of Bayesian Network Based on
Falcon Optimization Algorithm
INPUT: - datasets Population size, $N P$; Maximum speed, $V \max$; Values of cognitive Cc , social, $S c$ and following $F c$, constant. Value of awareness Probability $(A P)$ and Dive probability $(D P)$; tmax: maximum iteration number; Xmax: upper boundary, and Xmin: lower boundary.

OUTPUT: - learning Bayesian network.

1. Initialized empty structure and initialize parameters of FOA algorithm (dimension space $D$, size of population $N P$, constant values of $C c, S c$, and $F c$, Awareness $A P$ and Dive $D P$ probability, number of iterations, upper boundary, and lower boundary, $\left(G_{\text {best }, i, d}^{t}\right)$.
2. Set velocity and position for all falcons randomly, Compare each falcon by BDe score function and find best in current position $\left(P_{\text {best }, i, d}^{t}\right)$.
3. For loop to maximum iteration number.
4. For loop to size of population.
5. Generate random value $p A P, p D P$. Select new best position by comparing BDe score function of each falcon.
6. if $p A P<A P$, update falcon velocity $\left(V_{i}, d\right)$ using Equation (7); else, if $p D P>$ $D P$, update falcon velocity using Equation (8). else, compare score function of current and previous one. If this one is better, update falcon velocity using Equation (9); otherwise, use Equation (10).
7. Update position $X_{i}$.

8. Evaluate BDeu score function of new position $\left(X_{i, d}^{t}\right)$.
(a) If current position $\left(X_{i, d}^{t}\right)$ is better than best position $\left(P_{\text {best }, i, d}^{t}\right)$, then update best position by $\left(P_{\text {best }, i, d}^{t}\right)=\left(X_{i, d}^{t}\right)$.
(b) If $\left(G_{\text {best }, i, d}^{t}\right)<\left(X_{i, d}^{t}\right)$ greater than current position, then update best solution for global by $\left(G_{\text {best }, i, d}^{t}\right)<\left(X_{i, d}^{t}\right)$.
(c) Best score value and solution are saved.
(d) If $\left(X_{\min }\right) \geq\left(X_{\max }\right)$, stop iteration process; results are presented. If not, move to Step 5.
9. Return maximum BDe score.

# 4. Structure learning of Bayesian network using FOA 

The FOA is a proposed algorithm that can be applied for the structure learning of a Bayesian network. It uses the BDeu score function as a score metric for evaluating the structure of the Bayesian network. The FOA algorithm is an effective iterative method that depends on a society of individuals where each falcon encodes a possible location and velocity in a specific area. This area is held to be the search area. The proposed method is based on different procedures. The initial procedure utilizes Equation (7), which concerns exploration within the essential process if $(A P<p A P)$; otherwise, the secondary procedure uses Equation (8). If $D P<p D P$ then the falcon target one chosen prey ( $X_{\text {chosen }}$ ), and performs its initial movement for hunting, otherwise comparing the BDeu score function of both steps during choosing the most suitable location that is considered under Equations (9, 10). The algorithm above presents the pseudo-code of this procedure. The solution to the FOA's structure appropriates various neighborhoods in the exploration area. The expectation is powerful for updating a solution that is developed for a local search through the group of the fan falcon. The solution area of the Bayesian network structure learning is made for each possible DAG. Each falcon begins a potential solution, which is described as a DAG with empty arcs. A falcon next explores some examination space to obtain the approaching optimal or near-optimal solution, which is essentially recognized as the BDeu score. Applying Equation (4) determines the BDeu score as the goal function of the optimization. Achieving a higher (or the best) BDeu score for the structure of the Bayesian network is the goal of the search process. Each of the initial solutions is provided by iterative processes. Beginning by a clear graph $(G 0)$ with no arcs at the initial states, the arcs are added one after another (provided that they are not covered in the popular graph solution). The process for appending performs if and only if the new solution's score function is more powerful than the current score and the new solution satisfies the DAG constraint. This procedure continue until the number of arcs is equal to the number that is defined in the progress. During the design, the solution begins to select a population for each iteration, including selecting a candidate solution that has a more powerful score function. The falcon proceeds

according to the chosen operative until the method has achieved the highest number of iterations or the BDeu score does not grow anymore. In general, the processes contain four separate operations in the optimization: addition, deletion, movement, and reversion. Addition, deletion, and reversion are simple actions inside this region, including merely replacing an original edge each time from a competitor solution. This enables the inclusion of a relatively small region that is near the solution. On the other hand, the actual edges adjust the set of parents with each movement action, which can make a moderately important change for the current solution. Accordingly, if the solution is not modified after applying simple actions, the move action may update it. Diving is the principal force that uses the preferred procedure within the local optimization, which expands more comprehensively while a falcon approaches the acceptable solution. Diving is a driving force utilizing the same local optimization operator, which grows more widespread as a falcon approaches a desirable solution. Flying directions, the switch with various local optimization operators, which grows extra widespread as a falcon moves continuously from a solution to search for a better one.

Accordingly, the current velocity update by both falcon's best local or best global solutions depend on the values of $(D P$ and $A P)$. The speed of the FOA is updated depending on the current most suitable location of the falcon in the search area. Figure 1 shows Falcon G0, which represents a DAG that includes arcs, tries addition, reversion, move, and deletion, and sequentially approaches new solutions G1, G2, G3, and G4. Considering that the highest score is in G3, it will be chose; then, the falcon will continue to experiment on some comparable process to essentially get $\mathrm{G}+3$ as the new solution. If the BDeu score of $\mathrm{G}+3$ is more powerful than that of $\mathrm{G}+1$, the falcon will proceed to complete a similar operative. The procedures will iterate until the BDeu score stabilizes or the repetition loop equals the maximum. In the full procedure, the falcon chooses among the directions that utilize deletion, movement, reversion, and addition.
![img-0.jpeg](img-0.jpeg)

Figure 1. Searching steps for one falcon

# 5. Experimental evaluation 

To assess the FOA's performance, a standard evaluation technique is used by employing probability datasets obtained from the Bayesian network common criteria. The test platform includes a computer that has the following characteristics: Core i3, 2.1 GHz CPU, 4GB RAM, Ubuntu 14.04, and using Java to implement the algorithms. The authors studied the characteristics of the proposed method in several static datasets, including Lucap02 (143 variables and 10,000 instances), Andes (223 variables, 338 arcs, and 500 instances), win95pts ( 76 variables, 112 arcs, and 574 instances), Hepar ( 70 variables, 123 arcs, and 350 instances), Hailfinder ( 56 variables, 66 arcs, and 2,656 instances), Alarm ( 37 variables, 46 arcs, and 10,000 instances), Soybean ( 35 variables and 307 instances), Hepatitis ( 35 variables and 137 instances), Static Banjo ( 33 variables and 320 instances), Water ( 32 variables, 66 arcs, and 10,083 instances), Epigenetics ( 30 variable and 72,228 instances), Insurance ( 27 variables, 52 arcs, and 3,000 instances), Sensors ( 25 variables and 5,456 instances), Mushroom (23 variables and 1,000 instances), Parkinsons ( 23 variables and 195 instances), Heart (22 variables and 267 instances), Imports ( 22 variables and 205 instances), Child ( 20 variables, 25 arcs, and 230 instances), Letter ( 17 variables and 20,000 instances), Adult ( 16 variables and 30,162 instances), Lucas01 (10 variables and 10,000 instances), WDBC ( 9 variables and 1,000 instances), and Asia ( 8 variables, 8 arcs, and 3,000 instances) $[12]$.

In the paper, this work is dependent on an assumption of static data, and the learning data sets that the authors examined are stationery sets. Enlarging the FOA to sensor data sets or different forms of online current data sets is a challenging task and could be attempted after assessing its review over stationary data sets.

In this paper, the authors compared the results with pigeon-inspired optimization (PIO) [16], greedy search (GS) methods, and simulated annealing (SA) by using similar metrics for the data sets. Next, to define the parameters of the FOA, they estimated whole algorithms under identical conditions. In the FOA, the following values were employed for the experiments: population size $N=25$, and $t \max =1,000$. The constant parameters of the FOA's optimization are $C c=2, S c=3, F c=4$, $A P=0.3, V \max =0.1 u b(u b$ is 100 , and $V \max$ is 10$),(t)$ is a random number within a range of $[-1,1]$, and $D P$ is 0.85 . The parameters of the greedy search are as follows: the minimum number of recommended networks after the highest score $=1,000$, the recommended minimum networks before reboot $=3,000$, the maximum parent count for operations reboot $=5$, the maximum recommended networks before reboot $=5,000$, and restart by random network $=$ yes. The parameters of the simulated annealing algorithms are as follows: the temperature of re-annealing $=500$, the cooling factor $=0.8$, and the initial temperature $=1,000$. The algorithms were performed for three distinct execution times: 2,5 , and 60 minutes.

Tables 1, 2, and 3 show the score function values for the algorithms in the abovementioned data sets (including the different times). It can be noted from the results that the proposed method provides more reliable score values than PIO, the simulated

annealing algorithms, and the default greedy search during most comparison states. This means that the FOA obtains the best score with the minimum necessary time.

Table 1
Calculation results of score function values for FOA, simulated annealing, and greedy for 2 minutes of execution time


Table 2
Calculation results of score function values for FOA, simulated annealing, and greedy for 5 minutes of execution time


Table 3
Calculation results for score function values for FOA, simulated annealing, and greedy for 60 minutes of execution time


To assess the success of the discovery of the structure, the confusion matrix was calculated for each data set and its known network structure. The $T P, T N, F N$, and $F P$ metrics were calculated for each network for each algorithm to additionally obtain the following criteria: sensitivity (SE), F1 score, accuracy (Acc), and AHD, which are defined as follows:

$$
\begin{gathered}
\text { sensitivity }=\frac{T P}{T P+F N} \\
F 1_{s} \text { core }=\frac{2 \cdot T P}{2 \cdot T P+F P+F N} \\
\text { accuracy }=\frac{T P+T N}{T P+F P+T N+F N} \\
H D=\frac{F N+F P}{T P+T N+F P+F N}
\end{gathered}
$$

The meanings of these metrics are as follows: TN is an arc (vertex or edge) that is inside neither the learning network nor the natural network. $T P$ is the arc in the correct place inside the learning network. $F N$ is an arc in the natural network but not in the learning network. $F P$ is an arc inside the learning network but not in the natural network. The sensitivity results for simulated annealing, the FOA, PIO, and greedy are shown in Figure 2. The proposed method produces better values than simulated annealing, PIO, and greedy in most datasets.

![img-1.jpeg](img-1.jpeg)

Figure 2. Sensitivity for FOA, PIO, SA, and GS
Furthermore, the proposed method had greater accuracy values than the simulated annealing, PIO, and greedy algorithms in most datasets (as shown in Figure 3).
![img-2.jpeg](img-2.jpeg)

Figure 3. Accuracy for FOA, PIO, SA, and GS

The learning algorithm that was proposed works well in obtaining a suitable structure. As a result, the iterative FOA algorithm is the most suitable algorithm when compared to the other algorithms in most datasets from the point of view of

prediction accuracy. The FOA is also better than the other algorithms from the point of view of construction times. For the performance metrics, we used F1 as a metric of the model's accuracy in addition to the best score in the Bayesian results.

The F1-score, precision, and recall are used to evaluate the performance of the proposed algorithm. Under these circumstances, precision is the number of directed edges that are found to be correctly divided by the number of all of the edges in the expected BN. recall represents the division of the number of directed edges that are found by the number of edges in the actual BN. It does know that F1 is the harmonic average of accuracy and recall. Figure 4 presents the comparison of the FOA, PIO, simulated annealing, and greedy search.
![img-3.jpeg](img-3.jpeg)

Figure 4. F1 Score for FOA, PIO, SA, and GS

As presented in Figure 4, the proposed methods are more successful than the PIO, greedy search, and simulated annealing methods. Furthermore, the ultimate purpose of the model is to present a convenient representation of the real world, so accuracy is a useful measure of model performance evaluation. The proposed algorithm is also preferable regarding Hamming distances, which are always considerably lower than those that are obtained by using the DAG space.

Hamming distances is one of the most widely used evaluation metrics for BN structure learning, which directly matches the structure of learners and local networks and are also directed entirely toward exploration rather than inference. Figure 5 shows the average Hamming distances for the mentioned algorithms. The results demonstrate that the proposed method produces better performance values than the other methods that we considered.

![img-4.jpeg](img-4.jpeg)

Figure 5. AHD for FOA, PIO, SA, and GS

# 6. Conclusion 

The authors concentrated on the structure learning of a Bayesian network problem and utilized the falcon-inspired optimization procedure for Bayesian network structure learning. The authors applied the score and search technique, appropriating the FOA method as the search and BDeu as the score function. The FOA can be expressed as a stochastic search technique that is dependent on the navigational habits of falcons. In particular, the FOA is a common approach for exploring a discrete solution space; as such, it can be customized to suit any application domain. The concentration control in the FOA presents a quickened concentration to global extremum through providing a falcon to fly following a logarithmic spiral to the shortest useful solution space. The proposed method has a higher ability for searching, which indicates it can discover a more useful structure solution, measure better score function values, and best approximate to a network structure; in addition, the results are accurate. The global search enhances through the steps of the algorithm and immediately drives to global convergence. The authors are planning to further evaluate other essential properties of the FOA, such as resource consumption, analyses of run times, overall performance when utilizing further data sets, and experimental setups.

# Affiliations 

## Shahab Wahhab Kareem

(1) Erbil Polytechnic University, Department of Technical Information Systems Engineering, Erbil Technical Engineering College, Erbil-Iraq, shahab.kareem@epu.edu.iq
(2) Lebanese French University, Department of Information Technology, College of Engineering and Computer Science, Erbil-Iraq

## Mehmet Cudi Okur

Yasar University, Software Engineering Department, Faculty of Engineering, Izmir-Turkey, mehmet.okur@yasar.edu.tr

Received: 27.04 .2020
Revised: 22.06 .2020
Accepted: 05.08 .2020