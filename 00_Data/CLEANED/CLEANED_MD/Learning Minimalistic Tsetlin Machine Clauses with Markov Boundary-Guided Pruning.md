# Learning Minimalistic Tsetlin Machine Clauses with Markov Boundary-Guided Pruning 

Ole-Christoffer Granmo<br>Centre for AI Research<br>University of Agder<br>Grimstad, Norway<br>0000-0002-7287-030X

Christian Blakely
Machine Learning and AI
PwC Switzerland
Zurich, Switzerland
christian.blakely@pwc.ch

Per-Arne Andersen
Centre for AI Research
University of Agder
Grimstad, Norway
0000-0002-5490-6436

Geir Thore Berge
Technology and Innovation
Sørlandet Hospital
Kristiansand, Norway
0000-0002-7631-8045

Lei Jiao
Centre for AI Research
University of Agder
Grimstad, Norway
0000-0002-5490-6436

Xuan Zhang
Energy and Technology NORCE
Grimstad, Norway
xuzh@norceresearch.no

Tor Tveit
Technology and Innovation
Sørlandet Hospital
Kristiansand, Norway
tor.tveit@sshf.no


#### Abstract

A set of variables is the Markov blanket of a random variable if it contains all the information needed for predicting the variable. If the blanket cannot be reduced without losing useful information, it is called a Markov boundary. Identifying the Markov boundary of a random variable is advantageous because all variables outside the boundary are superfluous. Hence, the Markov boundary provides an optimal feature set. However, learning the Markov boundary from data is challenging for two reasons. If one or more variables are removed from the Markov boundary, variables outside the boundary may start providing information. Conversely, variables within the boundary may stop providing information. The true role of each candidate variable is only manifesting when the Markov boundary has been identified. In this paper, we propose a new Tsetlin Machine (TM) feedback scheme that supplements Type I and Type II feedback. The scheme introduces a novel Finite State Automaton - a ContextSpecific Independence Automaton. The automaton learns which features are outside the Markov boundary of the target, allowing them to be pruned from the TM during learning. We investigate the new scheme empirically, showing how it is capable of exploiting context-specific independence to find Markov boundaries. Further, we provide a theoretical analysis of convergence. Our approach thus connects the field of Bayesian networks (BN) with TMs, potentially opening up for synergies when it comes to inference and learning, including TM-produced Bayesian knowledge bases and TM-based Bayesian inference.


Index Terms—Tsetlin Machine, Bayesian Networks, Context-Specific Independence, Context-Specific Markov Blankets, Markov Boundaries

## I. INTRODUCTION

The power of state-of-the-art machine learning comes from encoding enormous amounts of historical data using millions (and lately, trillions) of parameters. However, the historical data makes the trained models carry on biases, discrimination, and prejudices [1], while the

[^0]number of parameters makes them incomprehensible to humans [2].

Researchers are further accumulating evidence that models based on correlation are brittle. Even state-of-the-art deep learning models, with their high computational cost and carbon footprint [3], tend to learn simple correlations instead of capturing the underlying causal dynamics of the data [4], [5]. Relying on such correlations is problematic when they are spurious or accurate only in limited contexts due to data bias.

Recently, the emerging paradigm of TMs [6] has made a fundamental shift from arithmetic-based to logic-based machine learning. Seen from a logical engineering [7] perspective, a TM produces propositional/relational clauses in Horn form (logical ANDrules) [8]. However, the logical expressions are robustly learnt using finite state machines, so-called Tsetlin automata [9]. TMs handle uncertainty despite being based on logic, using multiple clauses to signify confidence [10]. In this way, TMs introduce the concept of logically interpretable learning, where both the learned model and the process of learning are easy to follow and explain.

Two different feedback types interact to make the TM learn patterns: Type I and Type II Feedback. Type I Feedback produces frequent patterns, leading to descriptive conjunctive clauses. To increase discrimination power, the TM simultaneously uses Type II Feedback to introduce discriminative literals into the clauses. However, while effective in pattern recognition, the clauses sometimes include more context than needed, reducing efficiency and potentially interpretability.

To increase the efficiency and interpretability of TMs, we here propose a new kind of TM feedback - Type III Feedback. Type III Feedback interacts with Type I and Type II Feedback, with the goal of isolating the mechanism that governs the target variable. That is, Type III Feedback prunes the clauses of literals so that only the literals that directly govern the target variable remain.

To reach the above goal, our strategy is to view the TM clauses from a BN [11] perspective, introducing the concepts of Markov blankets and Markov boundaries [12] into TM learning.

Markov Blanket. In BNs, the Markov blanket of a target variable is a subset of the other variables. When we know the value of the variables in this subset, the remaining variables become superfluous. That is, the variables outside the Markov blanket are conditionally independent of the target given the variables in the Markov blanket.

Markov Boundary. The Markov boundary is the smallest possible Markov blanket. In other words, none of its subsets are Markov blankets. As proven by Pellet and Elisseeff, the Markov boundary of a target is the theoretically optimal set of features for predicting that target [13].

Context-Specific Independence. Context-specific independence is independence that holds in certain contexts [14]. In brief, the independence holds only for specific variable values. Such a refinement allows us to distil the mechanism governing the target value in more detail, leading to context-specific Markov blankets.

Context-Specific Markov Blankets. Context-specific Markov blankets exploit context-specific independence. The purpose is to reduce the number of parameters needed to specify the factors deciding the target variable [15].

Paper Contributions. This paper introduces a novel feedback scheme that exploits context-specific independence to prune clauses of literals outside their contextspecific Markov boundary. The feedback scheme is based on a novel Context-Specific Independence Automaton (CS-IA) that works alongside the Tsetlin automata of the TM. As soon as an IA uncovers contextspecific independence in a clause, it starts pruning any independent literals from the clause. We show empirically and prove formally that the CS-IA is capable of uncovering context-specific independence through online learning. We also show that CS-IA can robustly reduce the number of literals used on MNIST.

## II. CONTEXT-SPECIFIC MARKOV BOUNDARY-GUIDED PRUNING

## A. Tsetlin Machine Clauses and Bayesian Networks

1) Bayesian Networks: A BN is a directed acyclic graph (DAG) where the nodes of the graph are random variables while the directed edges represent dependencies among the variables. The entire graph is a compact representation of a joint probability distribution over the set of random variables, where each node and its parents are associated with a conditional probability

![img-0.jpeg](img-0.jpeg)

Fig. 1: Markov boundary of $Y$ in grey.

distribution (CPD). In this manner, the CPD gives a probabilistic formulation of the relationship between two or more variables. For example, Table V contains the CPD for variable $X_{1}$ of the BN in Fig. 1. In this example, the parent node of $X_{1}$ is $Y$. The table therefore specify a probability distribution over $X_{1}$, conditioned on the values of $Y$. When $Y=0$, $X_{1}$ takes the value 0 with probability 0.9 . Conversely, it takes value 1 with probability 0.1 . Note that the variables of a BN can also be continuous, with relationships modelled by conditional density functions.

Learning a BN from data is conducted in two phases. The first phase creates the structure of the network and the second phase estimates the probabilities of the CPDs, given the network structure from phase one. While parameter estimation is a well-studied problem, structure learning is still considered challenging. Vanilla BN structure learning usually involves two strategies: 1) constraint-based search for conditional independencies (CIs) in the data, from which one builds a DAG that is consistent with these; and 2) score-based search which poses structure learning as an optimization problem. One then seeks to maximize the score over the space of possible DAGs. Finding an optimal structure, however, has been shown to be NP-hard.
2) Tsetlin Machine Clauses: A TM learns conjunctive clauses to represent patterns in the data. A TM clause is simply an AND-rule for predicting a target value. For instance, a TM could represent the relationship between $X_{1}$ and the target $Y$ with the two clauses:

$$
\begin{aligned}
C^{+}(\mathbf{X}) & =X_{1} \\
C^{-}(\mathbf{X}) & =\neg X_{1}
\end{aligned}
$$

Each clause takes a vector $\mathbf{X}=\left[X_{1}, X_{2}, \ldots, X_{8}\right]$ as input. Half of the TM clauses get positive polarity, predicting when the target is 1 . The clause $C^{+}$above has positive polarity (signified by the upper index), and predicts $Y=1$ when $X_{1}=1$. Relating the clause to the CPD, it has precision 0.9 when it comes to predicting when $Y=1$. The negative polarity clauses, on the other hand, predicts when $Y=0$. For instance, the clause $C^{-}$above predicts $Y=0$ when $X_{1}=0$, again giving precision 0.9 according to the CPD.

A detailed description of how the TM uses teams of clauses to learn patterns from data can be found in [6]. The focus here is on the new learning automaton that we introduce to learn context-specific Markov boundaries.
3) Context-Specific Independence and Clauses: By way of example, two variables $X_{5}$ and $X_{7}$ are independent if we have $P\left(X_{5}, X_{7}\right)=P\left(X_{5}\right) P\left(X_{7}\right)$. Further, the variables $X_{1}$ and $X_{2}$ are conditionally independent given $Y$ if we have $P\left(X_{1}, X_{2} \mid Y\right)=$ $P\left(X_{1} \mid Y\right) P\left(X_{2} \mid Y\right)$. Context-specific independence refines conditional independence by saying that two variables $X_{1}$ and $X_{2}$ are independent when another variable $Y$ takes a specific value, for instance 0 , but not necessarily for other $Y$-values. That would be the case if we have $P\left(X_{1}, X_{2} \mid Y=0\right)=P\left(X_{1} \mid Y=0\right) P\left(X_{2} \mid Y=0\right)$. In the latter sense, one can say that a TM clause defines a specific context. For instance, the clause $C^{+}$in Eqn. 1 specifies a context where $X_{1}=0$.
4) Context-Specific Markov Boundaries and Clauses: A Markov blanket of a target variable $Y$ is a subset $\mathcal{X}^{\prime} \subseteq\left\{X_{1}, X_{2}, \ldots, X_{8}\right\}$ of the remaining variables $\mathcal{X}=\left\{X_{1}, X_{2}, \ldots, X_{8}\right\}$ where all the variables outside $\mathcal{X}$ are conditionally independent of the target $Y$ : $P\left(Y \mid \mathcal{X}^{\prime}, \mathcal{X} \backslash \mathcal{X}^{\prime}\right)=P\left(Y \mid \mathcal{X}^{\prime}\right)$. The Markov boundary of the target $Y$ is a Markov blanket that does not contain any smaller Markov blankets. As such, the Markov boundary of the target contains all the information needed for predicting the target. It is the theoretically optimal feature set [13]. So-called $d$-separation from [11] gives that the Markov boundary of $Y$ in Fig. 6 is $X_{1}, X_{2}, \ldots, X_{7}$, rendering $X_{8}$ conditionally independent of $Y$. When the Markov boundary only applies for specific values of $X_{1}, X_{2}, \ldots, X_{7}$, we say that the Markov boundary is context-specific. Again, a TM clause specifies a particular context by assigning values to the variables in the clause. For instance, the clause $C^{+}=X_{1} \wedge \neg X_{3}$ specifies the context where we have both $X_{1}=1$ and $X_{3}=0$.

## B. Context-Specific Independence Automaton (CS-IA)

Looking at TM clauses from the viewpoint of contextspecific Markov blankets, we hypothesize that Type I and Type II Feedback sometimes may include superfluous variable assignments. E.g., they may potentially include $X_{8}$ in Fig. 1 in clauses predicting $Y=1$ even though $X_{8}$ is conditionally independent of $Y$ given $X_{1}, X_{2}, \ldots, X_{7}$. The conditionally independence means that $P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}, X_{8}\right)=$ $P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}\right)$, rendering $X_{8}$ superfluous for predicting $Y$. By allowing the TM to discover that $X_{8}$ is superfluous, it can create shorter clauses that more concisely capture the underlying dynamics in the data.

To this end, we introduce the Context-Specific Independence Automaton (CS-IA), illustrated in Fig. 2 and detailed below. The CS-IA is based on the Tsetlin automaton [9], being a finite state automaton with two
actions. In brief, like with standard Type I and Type II Feedback, each clause literal gets its own automaton.

1) CS-IA Actions: Action Prune means that the CSIA decides to remove its literal from its clause because it has discovered that the literal is conditionally independent of the target given the remaining literals in the clause (the context).
2) CS-IA State Initialization and Updating: By way of example, we exploit the fact that $P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}, X_{8}\right)=P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}\right)$ when $X_{8}$ is outside the Markov boundary of $Y$. In brief, our CS-IA is to learn to Prune the literal if it is confident that $P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}, X_{8}\right)=$ $P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}\right)$. To avoid premature pruning of literals, the CS-IA starts in state $2 N$ (extreme right in the figure), signifying high confidence in dependence.

After initialization, the CS-IA swaps between examining two scenarios to learn context-specific independence for its clause $C$ from data:

1) The clause $C$ evaluates to 1 and $X_{8}$ takes part in $C$.
2) The clause $C$ evaluates to 1 and $X_{8}$ takes part in $C$, however, we pretend that $X_{8}$ is not there.
This means that the CS-IA waits for Scenario 1 to happen, then for Scenario 2, and then for Scenario 1 again, and so on. Fig. 3 illustrates this waiting strategy, where the dotted line refers to Scenario 1 and the solid red line to Scenario 2. Only Event 2, Event 5, Event 3, and Event 8 are used for updating. Using the above procedure, it will be possible for the CS-IA to gradually uncover whether $P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}, X_{8}\right)=$ $P\left(Y \mid X_{1}, X_{2}, \ldots, X_{7}\right)$, because if they are equal, Scenario 1 and Scenario 2 will look the same when it comes to predicting $Y$.

The pseudo-code for updating the state and taking actions for a general variable $X_{i}$ with Independence Automaton $I A_{i}$ is found below (see the next two sections for an empirical study and a rigorous theoretical convergence analysis of the scheme):

1) Wait for $X_{i}=1$ and $C=1$ :
a) If $Y=1$ then increase the state of $I A_{i}$.
b) If $Y=0$ then decrease the state of $I A_{i}$.
c) Decrease the state of $I A_{i}$ with a small probability $1.0 / d$ ( $d$ is a hyperparameter that controls how conservative the pruning should be).
2) Wait for the remaining variables of $C$ being 1 , ignoring the value of $X_{i}$ (simulating that $X_{i}$ is not present in the clause).
a) If $Y=1$ then decrease the state of $I A_{i}$.
b) If $Y=0$ then increase the state of $I A_{i}$.
c) Decrease the state of $I A_{i}$ with probability $1.0 / d$.
d) If state is below or equal to $N$, prune the variable $X_{i}$ from the clause $C$.
3) Repeat.

![img-1.jpeg](img-1.jpeg)

Fig. 2: The Context-Specific Independence Automaton (CS-IA) with 2N states.

![img-2.jpeg](img-2.jpeg)

Fig. 3: Illustration of the meaning of "Wait" in the learning loop.

We coin the new feedback type Type III Feedback, working alongside Type I and Type II Feedback.

## III. EMPIRICAL STUDY

To examine Markov boundary-guided pruning empirically, we use the toy BN from Fig. 1 and Tables I-VIII.

### A. Hyperparameters and experiment scope

We conduct a hyperparameter search over T ∈ {5, . . . , 20}, s ∈ {2, . . . , 100}, and d ∈ {20, . . . , 400}. Furthermore, we explore number of Tsetlin automaton and CS-IA states, N ∈ {25, . . . , 219}. Performance is assessed over 10 million epochs, incorporating 96 concurrent experiments sampled from the defined parameter space. For each epoch, the TM is trained using 100 samples from the toy BN illustrated in Fig. 1.1

We report the best found hyperparameters in Table IX. Our main conclusion is that the CS-IA exhibits robustness towards varying hyperparameters, as demonstrated in Fig. 6 where best and worst performance is plotted across epochs over all the experiments.

### B. Literal occurrence with Markov boundary pruning

We now investigate how accurately the Markov boundary is identified by examining how frequently the various literals appear within the TM clauses. As illustrated in Fig. 4, Markov boundary-guided pruning effectively diminishes the presence of literals that do not exhibit causal relationships with the target variable Y. In particular, X8 distinguishes itself from the other literals by being left out of more clauses.

Also notice how the entropy of the CPDs (Table IVII) is reflected in the plot. Variables with high entropy (high uncertainty) are included in correspondingly fewer clauses. Variable X1 meets two criteria: (1) it displays minimal entropy (Table V), and (2) it constitutes an essential element of the Markov boundary. Consequently, this variable is expected to have a significant presence across all clauses of the TM. In contrast, variable X4 is (1) included within the Markov boundary, but exhibits (2) substantial entropy. As a result, the presence of X4 is considerably reduced following the training process. These findings indicate that the TM learning process produces a distribution of clauses that reflects the entropy of the underlying BN.

### C. Markov-boundary clause distribution

We next explore how the clauses evolve during training, focusing on two aspects: (1) clauses containing the complete Markov boundary and (2) clauses with a partial Markov boundary, and their relationship to noisy variables. Our findings are illustrated in Fig. 6.

Notice first in Fig. 6c that the clauses containing independent literals first increase, but then drops again after 100,000 epochs. This is due to the CS-IA getting sufficient confidence to start pruning literals. Eventually, 100 out of 200 clauses contain Markov boundary variables only, as shown in Fig. 6d.

The TM's capacity to form clauses with the complete Markov boundary is investigated in Fig. 6b, where approximately 40 out of 200 clauses are identified as complete Markov boundary clauses. Very few of these clauses contain non-boundary variables, as seen in Fig. 6a. Indeed, the Markov boundary-guided pruning achieves 140 out of 200 noise-free clauses, paving the way for a TM that learns causal relationships instead of correlations.

### D. Analysis of clause pruning for MNIST

We finally study the effect of Markov boundary-based pruning on the more complex MNIST dataset by contrasting clause size against accuracy during learning. If Type III Feedback successfully prunes literals outside

<sup>1</sup>The code for conducting the experiments is publicly accessible at <https://github.com/cair/tmu>


TABLE I: CPD of X5 TABLE II: CPD of X6


TABLE III: CPD of X7 TABLE IV: CPD of X8


TABLE V: CPD of X1 TABLE VI: CPD of X2


TABLE VII: CPD of X4


TABLE VIII: CPD of Y


TABLE IX: Hyperparameters corresponding to the most effective and least effective runs of the toy experiment. The evaluation criteria is the number of clauses that have successfully pruned variables situated outside the Markov boundary. The best discovered configuration is in bold. The OR columns signify the timestep at which clauses containing a partial Markov Boundary jointly find the complete boundary by ORing the partial ones.
![img-3.jpeg](img-3.jpeg)

Fig. 4: Each line represents the frequency at which a literal is present in a clause. Literals which occur less frequently are either not part of the Markov boundary or have substantial uncertainty bound to their outcome.
the Markov boundary, we expect reduced clause size without significantly affecting accuracy. Fig. 5 supports our hypothesis. The left figure shows behaviour without Type III Feedback, with average literals per clause growing to around 40 . In the right figure, Type III Feedback starts pruning literals around epoch 30, reducing the
average number of literals per clause to below 5 , while maintaining accuracy. This indicates that superfluous parts of the clauses are being pruned.

## IV. THEORETICAL ANALYSIS

To analyze the proposed strategy, we study a toy-like example analytically. In more detail, we consider three variables, target variable $Y$, and two input variables $X_{1}$ and $X_{2}$. The Markov blanket of $Y$ is $X_{1}$, i.e., $P\left(Y \mid X_{1}, X_{2}\right)=P\left(Y \mid X_{1}\right)$. However, without knowing $X_{1}, X_{2}$ becomes informative: $P\left(Y \mid X_{2}\right) \neq P(Y)$. We assume that the clause of the TM $C$, after a period of training, becomes $C=X_{1} \wedge X_{2}$ for predicting $Y=1$. We want to show that the Type III Feedback can eventually guide the clause to become $C=X_{1}$.

## A. Probability of the steps being triggered

Before we analyzing the convergence, we explain the meaning of "Wait" in the learning loop as described in Sub-section II-B. In the learning loop, there are mainly two steps, namely, Step 1) and Step 2). Those two steps are controlled by the program and occurs in sequence, taking turns. For example, the events of Step 1) are depicted as blacked dash lines in Fig. 3, index as 1, 2, 3, and 4. In the above example, when we study $X_{1}$, the event probability is described by $P\left(C=1, X_{1}=1\right)$. Following the same concept, the events of Step 2)

![img-4.jpeg](img-4.jpeg)

Fig. 5: Accuracy (blue) and literals (green) without (a) and with (b) pruning.
![img-5.jpeg](img-5.jpeg)

Fig. 6: Distribution of Markov boundary among clauses. (a) Complete Markov boundary with supplementary noisy variables, (b) Complete Markov boundary without noisy variables, (c) Incomplete Markov boundary incorporating noisy variables, (d) Incomplete Markov boundary devoid of noise. The blue curve signifies the average of the top 5 performing trials, the orange curve represents the average of the bottom 5 trials, and the grey curve illustrates the mean value obtained from all 96 experimental runs.

are presented by red solid lines, index as $5,6,7,8$. In the above example, when $X_{1}$ is studied, the event probability is described by $P\left(X_{2}=1\right)$. In the training process, without any control, those two types of events will not always take turn to happen, as shown in Fig. 3. When consecutive events from the same step occurs, the program only processes the first time when it happens and ignore latter consecutive ones, until an event from another step happens. In this concrete example shown in Fig. 3, the Event 1 is trigger for Step 1), but not Event 2. Similarly, Event 5 will be triggered, but not Event 6. This applying to all previous and future events. Following the concept of taking turns, in Fig 3, Event 1, Event 3 and Event 4 will be triggered for Step 1). Similarly, Event 5 and Event 7 will be triggered for Step 2).

Now let us study the probability of the events that will trigger Step 1) and Step 2) in turn, as described in Sub-section II-B. Clearly, Step 1) and Step 2) will be triggered with equal probability as they take turns to happen. However, to calculate the concrete probability in a closed form is difficult. Here, instead of calculating the event probability, we try to bound it.

For $X_{1}$, let us define $P(\phi)$ the probability of Step 1) is triggered by the program. As Step 1) and Step 2) take turn to happen, the probability of Step 2) is also $P(\phi)$. Clearly, $P(\phi) \leq \min \left\{P\left(C=1, X_{1}=1\right), P\left(X_{2}=1\right)\right\}$. This is because when the two events take turn to be triggered, the event that has the minimum probability to be triggered determines the overall probability. In addition, for the case with the minimum probability, it is not all events that can trigger the program because the consecutive following ones are ignored. To simplify $\min \left\{P\left(C=1, X_{1}=1\right), P\left(X_{2}=1\right)\right\}$, we look at $P\left(C=1, X_{1}=1\right)=P\left(C=X_{1} \wedge X_{2}=\right.$ $\left.1, X_{1}=1\right)=P\left(X_{2}=1, X_{1}=1\right)=P\left(X_{2}=\right.$ 1) $P\left(X_{1}=1 \mid X_{2}=1\right) \leq P\left(X_{2}=1\right)$. Therefore, $P(\phi) \leq \min \left\{P\left(C=1, X_{1}=1\right), P\left(X_{2}=1\right)\right\}=$ $P\left(C=1, X_{1}=1\right)=P\left(X_{2}=1, X_{1}=1\right)$.

Similarly, for $X_{2}$, let us define $P\left(\phi^{\prime}\right)$ the probability of Step 1) is triggered by the program. As Step 1) and Step 2) take turn to happen, the probability of Step 2) is also $P\left(\phi^{\prime}\right)$. Clearly, $P\left(\phi^{\prime}\right) \leq \min \left\{P\left(C=1, X_{2}=\right.\right.$ 1), $P\left(X_{1}=1\right)\}$. Here $P\left(C=1, X_{2}=1\right)=P(C=$ $\left.\left.X_{1} \wedge X_{2}=1, X_{2}=1\right)=P\left(X_{2}=1, X_{1}=1\right)=\right.$ $\left.P\left(X_{1}=1\right) P\left(X_{2}=1 \mid X_{1}=1\right) \leq P\left(X_{1}=1\right)\right.$. Therefore, $P\left(\phi^{\prime}\right) \leq \min \left\{P\left(C=1, X_{2}=1\right), P\left(X_{1}=\right.\right.$ 1) $\}=P\left(C=1, X_{2}=1\right)=P\left(X_{2}=1, X_{1}=1\right)$. Note that although $P\left(\phi^{\prime}\right)$ and $P(\phi)$ have the same bounds, the actual values may be quite different.

## B. The convergence of $X_{1}$

We start the analysis of $X_{1}$ in different steps. For Step 1 (a), for $X_{1}$, the transition probability is $P(Y=1 \mid C=$ $\left.\left.1, X_{1}=1\right)=P\left(Y=1 \mid C=X_{1} \wedge X_{2}=1, X_{1}=1\right)=\right.$ $\left.P\left(Y=1 \mid X_{2}=1, X_{1}=1\right)=P\left(Y=1 \mid X_{1}=1\right)\right.$, which is increasing. For step 1 (b), for $X_{1}, P(Y=$
$\left.0 \mid C=1, X_{1}=1\right)=P(Y=0 \mid C=X_{1} \wedge X_{2}=1, X_{1}=$ $1)=P\left(Y=0 \mid X_{2}=1, X_{1}=1\right)=P(Y=0 \mid X_{1}=1)$, which is decreasing. For step 1 (c), we have a decreasing probability, which is $d$. Those events are all conditioned by $P(\phi)$.

We now study $X_{1}$ in Step 2. For Step 2, when we study $X_{1}$, we need to "Wait for the remaining variables of $C$ being 1 ". In this step, we need to wait until $X_{2}$ is 1 . Then, we need to ignore the value of $X_{1}$. In this step, the value of $C$ is useless in the calculation. It only depends on the remaining variable, i.e., $X_{2}$ and the value $Y$. For Step 2 (a), namely when $Y=1$, the probability of decrease is $P(Y=1 \mid X_{2}=1)$. For step 2 (b), namely, when $Y=0$, the probability of increase is $P(Y=$ $\left.0 \mid X_{2}=1\right)$. Those events are all conditioned by $P(\phi)$ as well.

Based on the above analysis, we can determine the probability of increase and the probability of decrease. For increase, we have 1 (a) and 2 (b). Therefore, the overall probability of increase, defined by $P_{\text {inc } X_{1}}$, is $P_{\text {inc } X_{1}}=P(Y=1 \mid X_{1}=1) P(\phi)+P(Y=0 \mid X_{2}=$ 1) $P(\phi)$. For decrease, we have 1 (b), 1 (c) and 2 (a). Therefore, the overall decreasing probability, defined by $P_{\text {dec } X_{1}}$ becomes $P_{\text {dec } X_{1}}=P(Y=0 \mid X_{1}=1) P(\phi)+$ $d P(\phi)+P\left(Y=1 \mid X_{2}=1\right) P(\phi)$. Fig. 2 illustrates the transitions of the states. Here $P_{\text {inc } X_{1}}$ is represented by the dashed arrow while $P_{\text {dec } X_{1}}$ is presented by the solid arrow. Note here that $P_{\text {dec } X_{1}} \leq 1$ and $P_{\text {inc } X_{1}} \leq 1$ must fulfill and the self-loop is not depicted. This condition is not difficult to fulfill as long as the dateset is balanced and the value $d$ is very small.

Now let us study the infinite time horizon with infinite states in the TA. As shown by Lemma 1 in [16], $X_{1}$ is to be included if $P_{\text {dec } X_{1}}<P_{\text {inc } X_{1}}$ holds in probability 1. To full fill this requirement, we need

$$
\begin{aligned}
& P\left(Y=1 \mid X_{1}=1\right)+P\left(Y=0 \mid X_{2}=1\right) \\
& >P\left(Y=0 \mid X_{1}=1\right)+d+P\left(Y=1 \mid X_{2}=1\right)
\end{aligned}
$$

which can be re-written as:

$$
\begin{aligned}
& P\left(Y=1 \mid X_{1}=1\right)-P\left(Y=0 \mid X_{1}=1\right) \\
& -\left(P\left(Y=1 \mid X_{2}=1\right)-P\left(Y=0 \mid X_{2}=1\right)\right)>d
\end{aligned}
$$

Eq. (4) can be interpreted in this way. Given $X_{1}=1$, the probability difference between $Y$ being 1 and 0 is $P(Y=1 \mid X_{1}=1)-P(Y=0 \mid X_{1}=1)$. Similarly, for $X_{2}=1$, the probability difference between $Y$ being 1 and 0 is $P\left(Y=1 \mid X_{2}=1\right)-P(Y=0 \mid X_{2}=1)$. When $X_{1}$ is not pruned, meaning that $X_{1}$ can be used to predict $Y$ by itself (without information from $X_{2}$ ), i.e., $C=X_{1}$, we expect that given $X_{1}=1$, the probability of $Y$ being 1 is greater than that of being 0 . In addition, the difference given $X_{1}$ must be greater than that given $X_{2}$, meaning that the information of $X_{2}$ is redundant. A margin $d$ is given to ensure that the above mentioned differences are sufficient.

## C. The convergence of $X_{2}$

In this subsection, we analyze the behavior of $X_{2}$. For Step 1) (a), the transition probability is $P(Y=1 \mid C=$ $\left.1, X_{2}=1\right)=P(Y=1 \mid C=X_{1} \wedge X_{2}=1, X_{2}=1)=$ $P(Y=1 \mid X_{2}=1, X_{1}=1)=P(Y=1 \mid X_{1}=1)$, which is increasing. For step 1 (b), for $X_{2}, P(Y=$ $0 \mid C=1, X_{1}=1)=P(Y=0 \mid C=X_{1} \wedge X_{2}=1, X_{2}=$ $1)=P(Y=0 \mid X_{2}=1, X_{1}=1)=P(Y=0 \mid X_{1}=1)$, which is decreasing. For step 1 (c), we have a decreasing probability, which is $d$. Those events are all conditioned by $P\left(\phi^{\prime}\right)$.

We now study $X_{2}$ in Step 2. For Step 2, when we study $X_{2}$, we need to "Wait for the remaining variables of $C$ being 1 ". In this step, we need to wait until $X_{1}$ is 1 . Then, we need to ignore the value of $X_{2}$. In this step, the value of $C$ is useless in the calculation. It only depends on the remaining variable, i.e., $X_{1}$ and the value $Y$. For Step 2 (a), namely when $Y=1$, the probability of decrease is $P(Y=1 \mid X_{1}=1)$. For step 2 (b), namely, when $Y=0$, the probability of increase is $P(Y=$ $0 \mid X_{1}=1)$. Those events are all conditioned by $P\left(\phi^{\prime}\right)$ as well.

Based on the above analysis, we can determine the probability of increase and the probability of decrease. For increase, we have 1 (a) and 2 (b). Therefore, the overall probability of increase, defined by $P_{\text {tnc } X_{2}}$, is $P_{\text {tnc } X_{2}}=P(Y=1 \mid X_{1}=1) P\left(\phi^{\prime}\right)+P(Y=0 \mid X_{1}=$ 1) $P\left(\phi^{\prime}\right)$. For decrease, we have 1 (b), 1 (c) and 2 (a). Therefore, the overall decreasing probability, defined by $P_{\text {dee } X_{2}}$ becomes $P_{\text {dee } X_{2}}=P(Y=0 \mid X_{1}=1) P\left(\phi^{\prime}\right)+$ $d P\left(\phi^{\prime}\right)+P(Y=1 \mid X_{1}=1) P\left(\phi^{\prime}\right)$. Fig. 2 illustrates the transitions of the states. Here $P_{\text {tnc } X_{2}}$ is represented by the dashed arrow while $P_{\text {dee } X_{2}}$ is presented by the solid arrow. Note here that $P_{\text {dee } X_{2}} \leq 1$ and $P_{\text {tnc } X_{2}} \leq 1$ must fulfill and the self-loop is not depicted. This condition is not difficult to fulfill as long as the dateset is balanced and the value $d$ is very small.

In infinite time horizon, given infinite length of Markov chain, to make sure that $X_{2}$ is to be pruned, we have to grantee that $P_{\text {dee } X_{2}}>P_{\text {tnc } X_{2}}$. This is always true as long as $d>0$ holds.

To conclude, based on the above analysis, we can see that for this toy-like example, if the system configuration is correct, i.e., $P(Y=1 \mid X_{1}=1)-P(Y=0 \mid X_{1}=1)-$ $\left(P(Y=1 \mid X_{2}=1)-P(Y=0 \mid X_{2}=1)\right)>d>0$, the system will almost surely converge to the correct clause with proper pruning and keeping, i.e., arriving $C=X_{1}$, given infinite time and states.

## V. CONCLUSION and FURTHER WORK

In this paper, we proposed a novel TM feedback scheme that supplements Type I and Type II Feedback. The new Type III Feedback exploits context-specific independence analysis, manifested as a Context-Specific Independence Automaton. The automaton evaluates independence hypotheses on-line, allowing it to uncover
literals that are independent of the prediction target, given the remaining literals of the clause (the context).

Our empirical and theoretical analysis shows that the scheme is effective, opening up for further synergy between the fields of BNs and TMs. In our future work, we intend to investigate how TMs can enable learning of Bayesian knowledge bases [17] and efficient probabilistic inference by composing Markov-boundary pruned TM clauses into, e.g., a Moral Graph [18].
