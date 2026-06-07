# A Model-Predictive Switching Approach To Efficient Intention Recognition 

Peter Krauthausen and Uwe D. Hanebeck


#### Abstract

Estimating a user's intention is central to close human-robot cooperation. In this paper, the problem of performing intention recognition with tree-structured Dynamic Bayesian Networks for large environments with many features is addressed. The proposed approach reduces the computational complexity of inference $O\left(b^{s}\right)$ for tree-structured measurement models with an average branching factor $b$ and tree height $s$ to $O\left(\hat{b}^{s}\right)$, where $\hat{b} \ll b$. The key idea is to switch between a finite set of reduced system and measurement models in order to restrict inference to the most important features. A model predictive approach to online switching between the reduced models is proposed that exploits an upper bound of the distances of the reduced models to the full model. The effectiveness of the proposed algorithm is validated in the intention recognition for a humanoid robot using a telepresent household scenario.


## I. INTRODUCTION

Recognizing a user's intentions, plans, or actions based on the observation of his interactive behavior is crucial for the success of every-day close human-robot cooperation. From a methodological standpoint, intention recognition is the process of estimating the force driving a human's actions [1]. For example, in a kitchen setting, this corresponds to estimating whether the user wishes to drink, cook, wash, clean, etc., based on his location, manipulations, and object interactions [2], cf. Fig. 1 (a). Two categories of approaches may be distinguished: probabilistic and symbolic intention recognition. In the former, a probability distribution over the set of intentions is inferred [2]-[4]. In contrast, in symbolic intention recognition, no account for the probability, but rather the possibility of a plan is considered. Mixture forms of both approaches exist, too. In this paper, a probabilistic recognition is proposed as typically performed by using Dynamic Bayesian Networks (DBN) [5] or a special case thereof, Hidden Markov Models (HMM) [6]. The main challenges for these techniques are model construction, model learning/adaption, and efficient online inference for nontrivial tasks. In this paper, the problem of reducing a high model complexity, due the usage of an increasing number of features, i.e., DBN with tree-structured measurement models, is addressed. The top left of Fig. 1 (b) shows such a DBN for the kitchen setting with a large tree-structured measurement model. In order to allow for natural reactive interaction with

[^0]a robot, approximate inference is required. This problem gains importance as with increasing levels of model detail, the number of states and possible features, e.g., objects, will inevitably grow.

## II. Related Work

Efficient online inference for intention recognition with DBN corresponds to handling large Bayesian Networks (BN). This problem is related to three main research areas: modeling and inference for structured BN, switching systems, and active sensing. The most prominent approach to handling large scale BN are Object-Oriented BN [7] and Situation-specific BN [8], [9]. The former facilitates modeling BN by introducing reusable object and class structures as well as relations between them. In [10], a first approach to dynamic querying based on first-order logic is presented. Situation-specific BN allow for constructing minimal querycomplete networks based on a knowledge base of network fragments. None of these approaches addresses the case, where the size of the deducible model is large and, e.g., a likelihood-based model reduction is sought.

In [11], Multinets are introduced that dynamically switch the network's structure based on a state estimate. Yet, the approach is not aimed at reducing the underlying state space model's complexity, but at increasing classification performance for automated speech recognition. In [11], the future development is ignored when changing the network. The approach is counterproductive if a network reduction is desired, as it introduces an additional Markov chain for guiding the model switch.

Regarding active sensing, the presented work may be understood as a blend of a sensor selection problem for large BN measurements systems [12] and model predictive sensor scheduling/control, which is a well-understood problem for smaller models [13]-[16]. Yet, the latter differs from the considered problem as no decentral computation under energy constraints, but a complex model's reductions needs to be managed. In [12], an approach for selecting a sensor subset based on an sensor synergy graph maximizing the mutual information between the state and sensor subsets is proposed. Note, that the specific difficulty for the intention recognition lies in the complexity of the measurement system and the consideration of too many sensor set combinations will render this approach infeasible for large problems.

In this paper, a model switching approach is proposed to reduce the computational burden of inference for DBN with large tree-structured measurement models. The approach switches models by selecting one model from a given finite


[^0]:    Peter Krauthausen and Uwe D. Hanebeck are with the Intelligent Sensor-Actuator-Systems Laboratory (ISAS), Institute for Anthropomatics, Karlsruhe Institute of Technology (KIT), Karlsruhe, Germany, Peter.Krauthausen@kit.edu, uwe.hanebeck@ieee.org. This work was partially supported by the German Research Foundation (DFG) within the Collaborative Research Center SFB 588 on "Humanoid Robots - Learning and Cooperating Multimodal Robots."

![img-0.jpeg](img-0.jpeg)

Fig. 1. In (a), features corresponding to measurements of the leaf nodes of the reduced models' BN in (b) are depicted. In (b), a coarse illustration of a full model (left) and two detailed reduced models (red, blue) is given. The correspondence between both models are marked by boxes. The red arrows show the course of this paper: starting from a large full model, it is decomposed and the small canonical models are derived and used for inference.

set of models online at each time step. Fig. 1 (b, right) shows how a large DBN for intention recognition may be understood as a composition of reduced models. The proposed approach is *model predictive* as it takes the future state evolution into account. Based on the current state as well as the system and measurement models, it predicts subsequent states for a fixed horizon. The model selection problem for the next time step is solved, using a reward function based on the predicted states, encoding the requirement of little loss in estimation quality due to the model reduction, and accounting for the computational savings by a reduced model. To this end, a novel approximate upper bound [17] of the difference in posterior estimates is employed. The rest of this paper is structured as follows. First, state estimation for the full model, when collapsed into an HMM, is presented in Sec. III, and a detailed problem definition is given in Sec. IV. The model selection problem is formalized based on the reduced models, in Sec. V-VIII. In the following sections the exact and approximate model selection based on a novel upper bound are presented and evaluated in Sec. IX.

## III. STATE ESTIMATION

In this paper, dynamic systems with discrete-valued hidden state $x_k \in \mathcal{X} := \{1, \ldots, M\}$ and measurements $\hat{y}_k \in \mathcal{Y} := \{1, \ldots, L\}$ for discrete time steps $k \in \mathbb{N} \cup \{0\}$ are considered. This is a simple DBN and equivalent to an HMM [5]. Each measurement corresponds to a fixed combination of features $y_{i,k}$, e.g., (distances × velocities × object × ...). State estimation in such a model (cf. [5]) corresponds to calculating the predicted probability distributions, i.e., the distributions for state $x_k$ given all measurements $\hat{y}_{1:k-1}$,

$$
\underline{\xi}_{k|1:k-1} = [P(x_k = 1|\hat{y}_{1:k-1}) \cdots P(x_k = M|\hat{y}_{1:k-1})]^T \tag{1}
$$

and the posterior probability distribution after measuring $\hat{y}_k$,

$$
\underline{\xi}_{k|1:k} = [P(x_k = 1|\hat{y}_{1:k}) \cdots P(x_k = M|\hat{y}_{1:k})]^T \tag{2}
$$

Using (2) and a state transition matrix $A_k \in \mathbb{R}^{M \times M}$

$$
A_k := ((P(x_{k+1} = j | x_k = i)))_{ij},
$$

where the transition probabilities depend on a specific model, the predicted density $\underline{\xi}_{k+1}$ is calculated by

$$
\underline{\xi}_{k+1|1:k} = A_k^T \cdot \underline{\xi}_{k|1:k}. \tag{3}
$$

In the filter step, $\underline{\xi}_{k+1|1:k}$ is fused with $\hat{y}_{k+1}$ according to

$$
\underline{\xi}_{k+1|1:k+1} = c \cdot \text{diag}(H_k(:, \hat{y}_{k+1})) \cdot \underline{\xi}_{k+1|1:k}, \tag{4}
$$

with $c := 1/(1_M \cdot \text{diag}((H_k(:, \hat{y}_k)) \cdot \underline{\xi}_{k+1|1:k})$ a normalization factor, asserting that $\xi_{k+1|1:k+1}$ is a valid probability distribution. In (4), $H_k := ((P(y_k = j | x_k = i)))_{ij}$, $H_k \in \mathbb{R}^{M \times L}$ denotes the matrix of observation probabilities given the state. Note, that (4) needs to be slightly changed to include continuous measurements. With an output vector $\underline{\xi}_k^0$, the model is then given by $M = \{\underline{\xi}_k, \underline{\xi}_k^0, A_k, H_k\}$. Inference in this type of DBN/HMM corresponds to alternating prediction (3) and filter steps (4).

## IV. PROBLEM DEFINITION

In many realistic settings, hundreds of features ought to be fused to obtain a state estimate, i.e., an intention estimate. Following Sec. III, a linear growth in the number of features yields an exponential growth in the size of the measurement matrix $H_k$, rendering online inference intractable.

Most applications allow for a hierarchical fusion of features as shown in Fig. 1. Exploiting conditional independencies between the features and introducing additional non-measurable random variables enables a decomposition of the measurement matrix $H_k$. The resulting graphical model, e.g., in Fig. 1 (b, right), is a Bayesian Network (BN) with the features' variables as leaf nodes. The computational complexity of inference for discrete BN depends on the nodes' state size and the number of nodes. The dependency on the state size is less relevant, as a growth in $x_k$ can be reduced by state compression, i.e., aggregation of states into so-called superstates [18], and if state transitions allow a decomposition, sparse matrix operations may reduce the computational effort drastically.

The problem is the growth in the number of features, i.e., nodes. The measurement systems considered here correspond

to trees rooted at $x_{k}$. For simplicity, it is assumed that they are $b$-ary trees of average height $s$ and average branching factor $b$. If the computation for the model selection is negligible and the $b$-ary tree can be decomposed into $r$ subtrees of identical size rooted at $x_{k}$. Only one subtree is used at a time, yielding a model with $(b / r)^{s} \ll b^{s}$ leaf nodes.

## V. REDUCED MODELS

In order to obtain the aforementioned computational savings, a finite set of $M$ reduced models $\left\{\mathcal{M}^{i}\right\}_{i=1, \ldots, M}$ is assumed to be given. Each $\mathcal{M}_{k}^{i}$ is defined by

$$
\mathcal{M}_{k}^{i}=\left\{\underline{\xi}_{k}^{i}, \underline{\xi}_{k}^{y, i}, \mathbf{A}_{k}^{i}, \mathbf{H}_{k}^{i}\right\}
$$

with $k$ the time index, $x_{k}^{i} \in \mathcal{X}^{i} \subset \mathcal{X},\left|\mathcal{X}^{i}\right| \ll|\mathcal{X}|$ and measurements $\hat{y}_{k} \in \mathcal{Y}^{i} \subset \mathcal{Y},\left|\mathcal{Y}^{i}\right| \ll|\mathcal{Y}|$. This implies $\mathbf{A}_{k}^{i} \in \mathbb{R}^{\left|\mathcal{X}^{i}\right| \times\left|\mathcal{X}^{i}\right|}, \mathbf{H}_{k}^{i} \in \mathbb{R}^{\left|\mathcal{X}^{i}\right| \times\left|\mathcal{Y}^{i}\right|}$ and a definition of $x_{k}^{i}$ w.r.t. $\underline{\xi}_{k}^{i}$. These sets may be determined manually, based on domain knowledge, or automatically by using algorithms for detecting lumps or decompositions in the transition or measurement matrix, cf. [18], [19]. Depending on the model choice $u_{k}=i$ at time $k$, the respective model $\mathcal{M}_{k}^{i}$ is used for the state estimation. As an example, in Fig. 1 the full system would be replaced, e.g., by the given blue and red $\mathcal{M}_{k}^{j}$ depending on $u_{k}$.

Regarding the implementation, the state spaces that do not align due to the omission of some part of the $\mathcal{X}$ may be zero-padded. Using sparse operations and proper indexing will still save the computation.

## VI. MODEL SELECTION

The key idea of the proposed approach is to choose $\mathcal{M}_{k}^{i}$ most similar to the full model $\mathcal{M}$. The corresponding distance is determined by the difference in the posterior density $\xi_{k+1 \mid 1: k+1}$ based on the common prior estimate $\xi_{k \mid 1: k}$. Selecting the model online corresponds to solving the following optimization problem

$$
u_{k}^{*}=\arg \max _{u_{k}, 0} \underbrace{\max _{u_{k}, 1: n} \sum_{n=1}^{N} g_{n}\left(\underline{\xi}_{k, 1: n}, \mu_{k, n}\left(\underline{\xi}_{k, 1: n}\right)\right)}_{J\left(\underline{\xi}_{k, 1}\right)}
$$

Here, $\underline{\xi}_{k, 1: n}$ denotes the predicted state estimate for $n$ steps into the future based on the estimate at time step $k$. For the sake of brevity, $\underline{\xi}_{k, n}:=\underline{\xi}_{k, 1: n}$ is defined. In (5), $J\left(\underline{\xi}_{k, 1}\right)$ is the default cumulative reward function and $g_{n}\left(\underline{\xi}_{k, n}, \mu_{k, n}\left(\underline{\xi}_{k, n}\right)\right)$ is a one-step objective function mapping to scalar reward values. The variable $\mu_{k, n}$ corresponds to the selection policy, i.e., $\mu_{k, n}\left(\underline{\xi}_{k, n}\right)$ maps the state distributions $\underline{\xi}_{k, n}$ to the model choice $u_{k, n}^{*}$. The outcome of (5) is the model choice $u_{k}^{*}=u_{k, 0}^{*}\left(\underline{\xi}_{k, 0}\right)$ to be applied to the system. After solving (5), inference using the selected model $\mathcal{M}_{k}^{i} \sim u_{k}^{*}$ is performed as described in Sec. III and the selection problem is solved for the next time step $k+1$. In the next section, a reward function for the reduction problem will be proposed and the efficient solution of this problem for a finite $N$ step horizon in each time step $k$ will be addressed.

## VII. ONE-STEP OBJECTIVE FUNCTION

In order to solve (5), a one-step objective function has to be chosen for determining in each time step one reduced model $\mathcal{M}_{k}^{i}$. Note, that there is a wealth of cost functions starting from information-theoretic criteria [20] to arbitrary cost functions in form of Gaussian mixtures [13], [15]. As the aim of this paper is to approximate $\mathcal{M}$ by $\mathcal{M}_{k}^{i}$, the most obvious cost function is the distance between $\mathcal{M}$ and $\mathcal{M}_{k}^{i}$. In [17], a distance measure for HMM was derived, which may be used to determine the difference in predicted posterior $\xi_{k, n+1}^{i}$ given the common prior estimate $\xi_{k, n}$ for the considered $\mathcal{M}_{k}^{i}$. The following norms defined for $\mathbf{S}=$ $\left(\left(s_{i j}\right)\right) \in \mathbb{R}^{M \times L}$ and $\underline{t}=\left[t_{1} \ldots t_{M}\right]^{\mathrm{T}}$ are used for obtaining these results

$$
\|\underline{t}\|_{1}=\sum_{o}\left|t_{o}\right|, \quad\|\mathbf{S}\|_{1}=\max _{p} \sum_{o}\left|s_{o p}\right|
$$

The triangle inequality and $\|\mathbf{S} \underline{t}\| \mid_{1} \leq\|\mathbf{S}\|_{1} \cdot\|\underline{t}\|_{1}$ hold.
a) Upper Bound of the Filter-Step: Given a predicted density, the difference between the posterior density $\xi_{k, n}$ obtained from using $\mathcal{M}$ and $\mathcal{M}_{k}^{i}$ may be upper-bounded. To bound the effect of the filter steps [17],

$$
F\left(\mathbf{H}_{k}^{i}\right)_{\hat{y}_{k}}:=\operatorname{diag}\left(\mathbf{H}_{k}^{i}\right)\left(:, \hat{y}_{k}\right))
$$

is defined in accordance with the notation in (4) and

$$
\mathbf{F}\left(\mathbf{H}_{k}^{i}\right):=\left[F\left(\mathbf{H}_{k}^{i}\right)_{1} ; \quad \ldots ; F\left(\mathbf{H}_{k}^{i}\right)_{L}\right]
$$

The matrices (6) are the likelihoods, as used in (4), for a specific measurement $\hat{y}_{k}$. Using (6), all likelihoods, i.e., the likelihoods for all $L$ possible observations, are collected into (7). In the following, the abbreviation $\mathbf{F}^{F}=\mathbf{F}\left(\mathbf{H}_{k}\right)$ for $\mathcal{M}$ and $\mathbf{F}^{i}=\mathbf{F}\left(\mathbf{H}_{k}^{i}\right)$ for $\mathcal{M}_{k}^{i}$ are used. The above description allows for upper-bounding the difference in the impact of the filter step (4) for $\mathcal{M}$ and $\mathcal{M}_{k}^{i}$ and w.r.t. to all measurements

$$
\begin{aligned}
& \left\|\underline{\xi}_{k, n}-\underline{\xi}_{k, n}^{i}\right\|_{1} \\
& \leq c_{1} \underbrace{\left\|\underline{\xi}_{k, n-1}-\underline{\xi}_{k, n-1}^{i}\right\|_{1}+c_{2}\left\|\mathbf{F}^{F}-\mathbf{F}^{i}\right\|_{1}}_{=d\left(\underline{\xi}_{k, n}, \underline{\xi}_{k, n}^{i}\right)},
\end{aligned}
$$

with $c_{i} \geq 1$ constants. The proof for (8) can be found in Sec. XI. The intuitive meaning of this upper bound is that the difference in posterior distributions can be bounded by the difference of the prediction results and a term considering the differences in the measurement models. A nice property of (8) is that the expensive computation $\left\|\mathbf{F}^{F}-\mathbf{F}^{i}\right\|_{1}$ may be performed a priori offline and only $\left\|\underline{\xi}_{k, n-1}-\underline{\xi}_{k, n-1}^{i}\right\|_{1}$ needs to be calculated online during the solution of (5). As the measurement impact is accounted for in the bound, $\underline{\xi}_{k, n}$ is approximated by predicting $\underline{\xi}_{k, n-1}$ only. The $c_{i}$ may be used to alleviate for overly different measurement models.
b) Approximate Upper Bound of Filter-Step: As mentioned earlier, the matrices $\mathbf{F}^{i}$ often cannot be used due to its mere size $|L| \cdot|N|$. For discrete feature combinations, e.g., for 4 binary features, one obtains $|L|=2^{4}$ combinations. This number will grow exponentially with the number of distinct

![img-1.jpeg](img-1.jpeg)

Fig. 2. Entire search tree for horizon $t=3$. Using Alg. 1 all but the red nodes are pruned and not calculated. The used selections and resulting densities correspond to nodes and edges of the tree.

observations, thereby rendering any approach to determine any $\mathbf{F}^{F}$ or $\mathbf{F}^{i}$ intractable for large problems.

As can be seen in Fig. 1 (b, right), there exist intermediate fusion results obtained during the hierarchical fusion of measurements, e.g., *Take Plate*. These intermediate estimates combine semantically coupled sets of observations. As (5) depends on predicted future measurements and the prediction according to the models will correlate semantically coupled measurements, an approximate measurement model is proposed by using the structure of $\mathbf{H}_{k}$ and $\mathbf{H}_{k}^{i}$, respectively. This approximation drastically reduces the number of nodes, as it corresponds to reducing the tree height. In Fig. 1, the proposed approximation corresponds to approximating the measurement model by removing all nodes up to a certain level of information fusion, e.g., a certain tree height or aggregation level, as the $a_{j,k}$ in Fig. 1 (b, right/lower left).

The upper bound is then calculated w.r.t. the reduced measurement matrices $\tilde{\mathbf{H}}_{k}$ and $\tilde{\mathbf{F}}^{i}=F(\tilde{\mathbf{H}}_{k}^{i})$. Here, $\tilde{\mathbf{H}}_{k}$ corresponds to an approximate measurement tree consisting of intermediate nodes only. To account for the approximation loss and complexity of the measurement system, an additional cost function is introduced into (5)

$$p(\xi_{k,n}) = p_{k,n} \in \mathbb{R}.$$

The entries of the cost vector $p_{k,n}$ reflect the size of the respective reduced model, e.g., for the experiments in Sec. IX a normalized number of nodes was used.

*c) Summarized Step Objective function:* The one-step objective function for the model selection problem is

$$g_n(\xi_{k,n}, \mu_{k,n}(\xi_{k,n})) = \alpha \, d(\xi_{k,n}, \xi_{k,n}^{i}) + p(\xi_{k,n}^{i}) + \beta. \qquad(9)$$

Here, $\alpha$ and $\beta$ are suitable constants guaranteeing that the cost function is negative, which will be used in the implementation, described in Sec. VIII.

## VIII. EFFICIENT SOLUTION

The optimization problem (5) may be solved by calculating the reward function (9) recursively for a fixed horizon

$$N.\text{ Defining } \mu_{k,n}(\xi_{k,n}) = u_{k,n}, \text{ the recursion starts with}$$

$$J(\xi_{kmN}) = g_n(\xi_{k,N}, u_{k,N}))\tag{10}$$

For $n<N$, the reward function is computed by

$$J(\xi_{k,n})$$

$$= g_n(\xi_{k,n}, u_{k,n}) + \max_{u_{k,n+1}} \left\{ J(\xi_{k,n+1}, u_{k,n+1}) \right\}.\tag{11}$$

Solving this recursive optimization problem in its most naive form consists of searching the tree of all possible model sequences of length $N$, see Fig. 2 (all nodes). Since it is possible to bound the quality of a path by the reward function, the solution to the above problem may be found by applying a *modified* version of Probabilistic Branch and Bound (MPAB) [13]. The MPAB is listed in Alg. 1. Similar to [13], it is assumed that $g < 0$. In Alg. 1, initially several flags need to be initialized per node $\mathcal{N}$. For example, the upper bound $J$ needs to be set to 0. The flag indicating whether the upper bound $J$ may be improved, i.e., is the search path exhausted, needs to be set to FALSE, and the flag for storing, if the node was visited, needs to be set to FALSE, too. During the execution of the algorithm, the cumulative reward as calculated by Alg. 1, needs to be stored. Expanding the children corresponds to instantiating the consecutive child nodes for $u_{k}$ in the search tree. Their prior density is obtained by using the estimate of the parent node and the $\mathcal{M}_{k}^{i}$ corresponding to the chosen $u_{k}$. After determining the posterior density, the reward $J$ is calculated for each child and the rewards of the parent nodes are updated. This means that (3) needs to be calculated for $\mathcal{M}$ and $\mathcal{M}_{k}^{i}$.

Using Alg. 1, the search through the entire search tree is avoided and fewer nodes need to be expanded, Fig. 2 (red nodes only). In the best case, the number of nodes in the search that ought to be expanded is only $M \cdot N$.

Algorithm 1 Modified Probabilistic Branch-and-Bound [13]

while not ( $\mathcal{N}$.exhausted ) do

while ( $\mathcal{N}$.visited ) do

$\mathcal{C} \leftarrow$ Non-leaf child of $\mathcal{N}$ with max.J
Recurse with $\mathcal{N} \leftarrow \mathcal{C}$

end while

// Expand best search path

if recursion level < horizon then
$\mathcal{C} \leftarrow$ Instantiate child nodes of $\mathcal{N}$
for all Children of $\mathcal{C}$ of $\mathcal{N}$ do
$\mathcal{C} \cdot J \leftarrow g(\mathcal{C})$
$\mathcal{C}$.exhausted $\leftarrow$ FALSE
end for
Update $\mathcal{N} \cdot J$
else
$\mathcal{C}$.exhausted $\leftarrow$ TRUE
Update parent( $\mathcal{N}$ ).J
end if

end while
$\mathcal{N}$.visited $\leftarrow$ TRUE

![img-2.jpeg](img-2.jpeg)

Fig. 3. Left: Human with head and hand tracking devices and data glove. Right: example impressions of the 1st person view of the virtual environment.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Mean *l*<sub>1</sub>-difference between the estimates using the full model and the proposed approach for a typical every day activity sequence.

## IX. EXPERIMENTS

The proposed approach shall be used for recognizing the user's intentions, plans, or actions based on the observation of his interactive behavior in a household setting by a humanoid robot assisting the user. In Sec. IX-A, a telepresent virtual household setting will be introduced and in Sec. IX-B, the experiments are described and analyzed.

### A. Telepresent Virtual Household Setting

In the experiments, an *extended range telepresence system* [21] was used. The specific system enables the user to move in a virtual 1:1-scale kitchen model of the original household. While moving, head and hand positions are tracked by an acoustic tracking system. The noise characteristics are similar to what the vision system of a real robot may achieve. Besides the position data, the user's grasping activity is measured by means of a cyber-glove device. The user in the real world and example impression of the *first-person* view of the kitchen inside the household setting can be seen in Fig. 3. This test environment has several advantages: (a) the test person naturally moves in the virtual kitchen just like in the real kitchen, (b) interaction with objects (dishes, glasses, pots etc.) and appliances is natural, e.g., cupboard doors may be opened by grasping and pulling the handle.

### B. Experimental Task

For the experiments, a test person performed an everyday sequence: *lay table*, *prepare a meal*, and *clean dishes*. In detail, the test person moves to the other side of the room, picks up some dinner ware, and brings it to the table in the kitchen. Then, cooking ingredients are fetched in order to put them into a cooking pot. The pot is put onto the stove. Later, the dinner ware on the table is picked up and carried over to the sink basin and put into the dishwasher.

In order to validate the proposed approach for varying model sizes, two full models *M*<sub>*A*−*B*</sub> of different size were created with **small** and **large** number of nodes. The models are structurally similar to Fig. 1, but consist of different numbers of fragments, cf. Tab. II. For example, in Fig. 1 two *action* fragments- (*take dinnerware* and *bring dinnerware to dishwasher*) are shown. Each fragment is associated with a set of objects, e.g., dishes, cups, pots, etc., and planes that play a role in the manipulation of these objects, e.g., putting a pot onto the stove. All *M*<sub>*k*</sub><sup>*i*</sup> used more than 100 features to obtain an estimate for 10 and 15 intentions.

For each full model *M*<sub>*A*−*B*</sub>, sets four of reduced models *M*<sub>*k*</sub><sup>*i*</sup> were created. The respective numbers of nodes are given in Tab. I. The results in terms of computational savings and approximation quality for all model pairs are given in Tab. II. The results using *M*<sub>*A*−*B*</sub> is denoted by **default** and the results using *M*<sub>*k*</sub><sup>*i*</sup> for look ahead horizons *h* = 2 and *h* = 3 are denoted by **MP**. For the two horizons, the average number of nodes, the approximation error as the average *l*<sub>1</sub>-distance between the full model's posterior density and the approximation, as well as the average time per step are given. This time corresponds to the DBN inference only and excludes the time for calculating the switch.

For the small experiment, the error distribution over time is depicted in Fig. 4. Over the entire trajectory the error remains modest, i.e., the intention is estimated as using full model. The error is noteworthy only after the initialization and when repeated switching occurs, e.g., around *t* = 100.

The statistics in Tab. II show that the proposed approach even with the shorter horizon already speeds up inference. This holds even though for the small experiment, each reduced model *M*<sub>*k*</sub><sup>*i*</sup> contains more than 50% of the full model, cf. Tab. I. For the large model—the actual field of application of the proposed approach—the switched approach is one order of magnitude faster than if the default full *M* was used. For the investigated application, i.e., intention recognition in close human-robot-cooperation, interactive cooperation can be achieved with this speed-up.

## X. CONCLUSIONS

In this paper, an approach for efficient estimation of the user's intention with tree-structured Dynamic Bayesian Networks for large environments with many features is addressed. The approach is shown to yield large speed-ups that allow for integrating large-scale intention, plan, and action recognition into close human-robot-cooperation and the consideration of drastically larger environments. The

TABLE I

NUMBER OF NODES FOR *M*<sub>*A*−*B*</sub> AND RESPECTIVE *M*<sub>*k*</sub><sup>*i*</sup>


TABLE II
MODEL SIZE OF THE UNDERLYING DBN IN THE NUMBER OF NODES, AVERAGE RUNTIME, AND ERROR WITH STANDARD DEVIATION.


effectiveness of the proposed algorithm is validated in the intention recognition for a humanoid robot by using a telepresent virtual household scenario. As future work, it remains to be investigated whether the model predictive approach may yield benefits for online adaption of Object-Oriented $B N$ or Situation-specific $B N$, how the model decomposition and parameter identification may be automated, as well as how models with a decomposition into a large number of reduced models may be handled.

## XI. Proof

Let $\mathbf{F}^{i}:=\mathbf{F}\left(\mathbf{H}_{k}^{i}\right), i=1,2$, be given. The altered result from in [17] in (8) holds as

$$
\left\|\xi_{k, n}^{1}-\xi_{k, n}^{2}\right\|_{1} \leq\left\|\mathbf{F}^{1} \xi_{k, n-1}^{1}-\mathbf{F}^{2} \xi_{k, n-1}^{2}\right\|_{1}
$$

and due to $\mathbf{F}^{1} \xi_{k, n-1}^{2}-\mathbf{F}^{1} \xi_{k, n-1}^{2}=0$, simple rearrangement, as well as the application of the triangle inequality

$$
\begin{aligned}
& \left\|\left(\mathbf{F}^{1} \xi_{k, n-1}^{1}-\mathbf{F}^{1} \xi_{k, n-1}^{2}\right)+\left(\mathbf{F}^{1} \xi_{k, n-1}^{2}-\mathbf{F}^{2} \xi_{k, n-1}^{2}\right)\right\|_{1} \\
& \leq\left\|\mathbf{F}^{1} \xi_{k, n-1}^{1}-\mathbf{F}^{1} \xi_{k, n-1}^{2}\right\|_{1}+\left\|\mathbf{F}^{1} \xi_{k, n-1}^{2}-\mathbf{F}^{2} \xi_{k, n-1}^{2}\right\|_{1} \\
& \leq L \cdot\left\|\left(\xi_{k, n-1}^{1}-\xi_{k, n-1}^{2}\right)\right\|_{1}+\left\|\mathbf{F}^{1}-\mathbf{F}^{2}\right\|_{1}
\end{aligned}
$$

because $\left\|\mathbf{F}^{1}\right\|_{1} \leq L$ for the maximum number of observations and $\left\|\xi_{k, n-1}^{2}\right\|_{1}=1$ and $\xi_{k, n-1}^{2}$ is a normalized density.
