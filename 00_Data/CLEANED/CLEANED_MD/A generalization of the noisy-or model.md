# A Generalization of the Noisy-Or Model 

Sampath Srinivas*<br>Knowledge Systems Laboratory<br>Computer Science Department<br>Stanford University, CA 94305<br>srinivas@cs.stanford.edu


#### Abstract

The Noisy-Or model is convenient for describing a class of uncertain relationships in Bayesian networks [Pearl 1988]. Pearl describes the Noisy-Or model for Boolean variables. Here we generalize the model to nary input and output variables and to arbitrary functions other than the Boolean OR function. This generalization is a useful modeling aid for construction of Bayesian networks. We illustrate with some examples including digital circuit diagnosis and network reliability analysis.


## 1 INTRODUCTION

The Boolean Noisy-Or structure serves as a useful model for capturing non-deterministic disjunctive interactions between the causes of an effect [Pearl 1988] .

The Boolean Noisy-Or can be explained as follows. Consider a Boolean OR gate with multiple inputs $U_{1}, U_{2}, \ldots, U_{n}$ and an output $X$. Now consider some non-determinism associated with each input defined as follows: On each input line $U_{i}$ a nondeterministic line failure function $\mathcal{N}_{i}$ is introduced (see Fig 1, considering $F$ to be a Boolean OR gate). The line failure function $\mathcal{N}_{i}$ takes $U_{i}$ as input and has a Boolean output $U_{i}^{\prime}$. Instead of $U_{i}$ being connected to the OR gate we now have $U_{i}^{\prime}$ connected to the OR gate instead.

The line failure function can be conceptualized as a non-deterministic device - there is a probability $q_{i}$ (called the inhibitor probability) that the line failure function causes a 'line failure'. When a line failure occurs on line $i$, the output of the device is $f$ (i.e., false) irrespective of what the input is, i.e.,

[^0]$U_{i}^{\prime}=f$. When a line failure does not occur on line $i$ the device just transmits its input to its output, i.e., $U_{i}{ }^{\prime}=U_{i}$. This non-failure event occurs with probability $1-q_{i}$.

This overall structure induces a probability distribution $P\left(X \mid U_{1}, U_{2} \ldots, U_{n}\right)$ which is easily computable[Pearl 1988].

When each $U_{i}$ is interpreted as a "cause" of the "effect" $X$, the Boolean Noisy-Or models disjunctive interaction of the causes. Each cause is "inhibited" with probability $q_{i}$, i.e., there is a probability $q_{i}$ that even when the cause $U_{i}$ is active, it will not affect $X$.

In a Bayesian network interpretation, each of the variables $U_{i}$ can be considered as a predecessor node of the variable $X$. The conditional probability distribution $P\left(X \mid U_{1}, U_{2} \ldots, U_{n}\right)$ is computed from the probabilities $q_{i}$. In domains where such disjunctive interactions occur, instead of fully specifying opaque conditional probability distributions, the Noisy-Or model can be used instead. The inhibitor probabilities are few in number (one associated with each predecessor $U_{i}$ of $X$ ) and would be intuitively easier to specify because of their direct relation to the underlying mechanism of causation.

This paper generalizes the Noisy-Or model to the case where both the 'cause' variables $U_{i}$ and 'effect' variable $X$ need not be Boolean. Instead, they can be discrete variables with any number of states. Furthermore, the underlying deterministic function is not restricted to be the Boolean OR function, it can be any discrete function. In other words, in Fig $1, F$ can be any discrete function.

Seen as a modeling tool, this generalization provides a framework to move from an underlying approximate deterministic model (the function $F$ ) to a more realistic probabilistic model (the distribution $P\left(X \mid U_{1}, U_{2} \ldots, U_{n}\right)$ ) with the specification of only a few probabilistic parameters (the inhibitor probabilities).


[^0]:    *Also with Rockwell International Science Center, Palo Alto Laboratory, Palo Alto, CA 94301.

![img-0.jpeg](img-0.jpeg)

Figure 1: The generalized Noisy-Or model.

In domains where the generalized Noisy-Or is applicable, it makes the modeling task much easier when compared to the alternative of direct specification of the probabilistic model $P\left(X \mid U_{1}, U_{2} \ldots U_{n}\right)$. In such domains, the task of creating a Bayesian network would proceed as follows:

- Variables and deterministic functions that relate them and approximate the non-deterministic behaviour of the domain are identified.
- A network is created with this information with a node for each variable, and a link from each of $U_{1}, U_{2}, \ldots, U_{n}$ to $X$ for each relation of form $X=F\left(U_{1}, U_{2}, \ldots, U_{n}\right)$. (The network is assumed to be acyclic).
- Inhibitor probabilities for each link in the network are elicited.
- The generalized Noisy-Or model is used to automatically 'lift' the network from the previous step into a fully specified Bayesian network which has the same topology as the network.


## 2 THE GENERALIZED MODEL

The generalized Noisy-Or model is illustrated in Fig 1 .

Each $U_{i}$ is a discrete random variable. Each $U_{i}^{\prime}$ is a discrete random variable with the same number of states as $U_{i}$.

We will refer to the number of states of $U_{i}$ and $U_{i}^{\prime}$ as $m_{i}$. We will refer to the $j$ th state of $U_{i}$ as $u_{i}(j)$ where $0 \leq j<m_{i}$. We call $j$ the index of state $u_{i}(j)$. We will use $u_{i}$ to denote "any state of $U_{i}$ ". As an example of the use of $u_{i}$, consider the statement, "Every state $u_{i}$ of $U_{i}$ has a unique index associated with it".

We define $I_{i}$ to be the function that returns the index of a state $u_{i}$ of $U_{i}$, i.e., $I_{i}\left(u_{i}\right)=j$ where $j$ is the index of state $u_{i}$ of variable $U_{i}$. We also have
similarly defined quantities $u_{i}^{\prime}(j), u_{i}^{\prime}, I_{i}^{\prime}$ associated with the variable $U_{i}^{\prime}$.

The line failure function $\mathcal{N}_{i}$ associates a probability value $P_{i}^{i n h}(j)$ with every index $0 \leq j<m_{i}$. This quantity can be read as the inhibitor probability for the $j$ th state of input $U_{i}$.

The line failure function can be conceptualized as a non-deterministic device that takes the value of $U_{i}$ as the input and outputs a value for $U_{i}^{\prime}$. This device fails with probability $P_{i}^{i n h}(j)$ in state $j$. When a failure in state $j$ occurs, the output of the device is $u_{i}^{\prime}(j)$ regardless of the input. When no failure occurs, if the input is $u_{i}(j)$ the output is $u_{i}^{\prime}(j)$ - this can be viewed as "passing the input through to the output" (note that the index $j$ of the output state and the input state are same in this case). The probability of no failure occuring is denoted by $P_{i}^{\text {n ofail }}$. We see that:

$$
P_{i}^{\text {n ofail }}=1-\sum_{0 \leq j<m_{i}} P_{i}^{i n h}(j)
$$

The output $X$ is a discrete random variable with $m_{x}$ states. We will refer to the $j$ th state of $X$ as $x(j)$ and use $x$ to refer to "any state of $X$ ".
$F$ (see Fig 1) can be conceptualized as a deterministic device that outputs some value $x$ of $X$ for each possible joint state $u_{1}^{\prime}, u_{2}^{\prime}, \ldots, u_{n}^{\prime}$ of the inputs $U_{1}^{\prime}, U_{2}^{\prime}, \ldots, U_{n}^{\prime}$. In other words $F$ is a discrete function that maps the space of joint states of $U_{1}^{\prime} \times U_{2}^{\prime} \times \ldots \times U_{n}^{\prime}$ into the set of states of $X$.

We note that the model described above induces an uncertain relationship between the output $X$ and the variables $U_{i}$. This relationship is captured by the conditional distribution $P\left(X \mid U_{1}, U_{2}, \ldots, U_{n}\right)$.

In the next section we proceed to show how this conditional distribution is computed from the function $F$ and the inhibitor probabilities. We will use the notation $\mathbf{U}$ to denote the vector of variables $\left[U_{1}, U_{2}, \ldots, U_{n}\right]$. Similarly, we will use $\mathbf{u}$ to denote any joint state $\left[u_{1}, u_{2}, \ldots, u_{n}\right]$ of $\mathbf{U} . \mathbf{U}^{\prime}$ and $\mathbf{u}^{\prime}$ are defined similarly with respect to the variables $U_{i}^{\prime}$. Note that $P\left(X \mid U_{1}, U_{2}, \ldots, U_{n}\right)$ abbreviates to $P(X \mid \mathbf{U})$.

In the special case where every inhibitor probability is zero each variable $U_{i}^{\prime}$ always has the "same" value as $U_{i}$ (i.e., the state of $U_{i}^{\prime}$ has the same index as the state of $U_{i}$ ). In this special case the variables $U_{i}^{\prime}$ become superfluous, we could just as well remove the line failure functions and connect the each input $U_{i}$ directly through to $F$.

In this special case, the overall model degenerates to a deterministic function where the value of output $X$ is determined from the values of the input variables $U_{i}$ by the function $F$. Thus the general-

ized Noisy-Or model can be viewed as starting with a deterministic model (the function $F$ ) and then introducing failures in the inputs, viz, the inhibitor probabilities, resulting finally in a non-deterministic model.

## 3 CHARACTERIZING $P(X \mid \mathbf{U})$

Each line failure function $\mathcal{N}_{i}$ defines a probability distribution $P_{i}\left(U_{i}^{\prime} \mid U_{i}\right)$ relating $U_{i}^{\prime}$ and $U_{i}$. From the model for $\mathcal{N}_{i}$ we see that the distribution $P_{i}$ is calculated as:
$P_{i}\left(u_{i}^{\prime} \mid u_{i}\right)=\left\{\begin{array}{ll}P_{i}^{\text {nefail }}+P_{i}^{\text {inh }}\left(I_{i}^{\prime}\left(u_{i}^{\prime}\right)\right) & \text { if } I_{i}^{\prime}\left(u_{i}^{\prime}\right)=I_{i}\left(u_{i}\right) P_{i}^{\text {inh }}\left(I_{i}^{\prime}\left(u_{i}^{\prime}\right)\right) \\ P_{i}^{\text {inh }}\left(I_{i}^{\prime}\left(u_{i}^{\prime}\right)\right) & \text { otherwise }\end{array}\right.$
The equation above summarizes the following facts: if the the output $u_{i}^{\prime}$ of $\mathcal{N}_{i}$ is the "same" as the input $u_{i}$ (i.e., the indices of both are the same), then either the device $\mathcal{N}_{i}$ is working normally or it has failed in the state $u_{i}^{\prime}$. If the output $u_{i}^{\prime}$ is not the "same" as input $u_{i}$, then the device has failed in state $u_{i}^{\prime}$.

We now characterize the distribution $P(X \mid \mathbf{U})$ in terms of the inhibitor probabilities for each $U_{i}$ and the function $F$.

We note that:

$$
P(x \mid \mathbf{u})=\sum_{\mathbf{u}^{\prime}} P\left(x \mid \mathbf{u}^{\prime}, \mathbf{u}\right) P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right)
$$

We note that once we know the state $\mathbf{u}^{\prime}$ of $\mathbf{U}^{\prime}$, we know the value $x$ of $X$, since $x=F\left(\mathbf{u}^{\prime}\right)$. In other words, $X$ is independent of $\mathbf{U}$ once $\mathbf{U}^{\prime}$ is known. The above equation therefore simplifies to:

$$
P(x \mid \mathbf{u})=\sum_{\mathbf{u}^{\prime}} P\left(x \mid \mathbf{u}^{\prime}\right) P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right)
$$

We note that $P\left(x \mid \mathbf{u}^{\prime}\right)=1$ when $x=F\left(\mathbf{u}^{\prime}\right)$ and $P\left(x \mid \mathbf{u}^{\prime}\right)=0$ when $x \neq F\left(\mathbf{u}^{\prime}\right)$. This simplifies the defining equation to:

$$
P(x \mid \mathbf{u})=\sum_{\left\{\mathbf{u}^{\prime} \mid x=F\left(\mathbf{u}^{\prime}\right)\right\}} P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right)
$$

Now we note that the dependence of $\mathbf{u}^{\prime}=$ $\left[u_{1}, u_{2}, \ldots, u_{n}\right]$ on $\mathbf{u}=\left[u_{1}, u_{2}, \ldots, u_{n}\right]$ can be split into $n$ pairwise dependences of $u_{i}^{\prime}$ on $u_{i}$. This is because the value of a variable $U_{i}{ }^{\prime}$ depends solely on $U_{i}$ and not on any other variable $U_{j}$ where $i \neq j$.

Thus we can simplify the equation to:

$$
\begin{aligned}
P(x \mid \mathbf{u}) & =\sum_{\left\{\mathbf{u}^{\prime} \mid x=F\left(\mathbf{u}^{\prime}\right)\right\}} P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right) \\
& =\sum_{\left\{\mathbf{u}^{\prime} \mid x=F\left(\mathbf{u}^{\prime}\right)\right\}} \prod_{\mathbf{u}^{\prime}} P_{i}\left(u_{i}^{\prime} \mid u_{i}\right)
\end{aligned}
$$

We note that we have already defined $P\left(u_{i}^{\prime} \mid u_{i}\right)$ in terms of the inhibitor probabilities.

The above equation is easily converted to an algorithm (described later) to generate a conditional probability table given the inhibitor probabilities and the function $F$.

### 3.1 BOOLEAN NOISY-OR AS A SPECIAL CASE

The generalized Noisy-Or collapses to be the Boolean Noisy-Or [Pearl 1988] when all the variables are Boolean ${ }^{1}$, the function $F$ is the Boolean OR, $0)=q_{i}$ and $P_{i}^{i n h}(1)=0$. In other words, $\mathcal{N}_{i}$ can fail with probability $q_{i}$ with the output being "false" but it cannot fail with output being "true".

Let $f_{i}$ and $t_{i}$ denote the "true" and "false" states of variable $U_{i}$. Similarly we have $f_{x}$ and $t_{x}$ for variable $X$. The following can be shown easily from equation 2 above:

$$
\begin{aligned}
& P\left(f_{x} \mid \mathbf{u}\right)=\prod_{\left\{i \mid u_{i}=t_{i}\right\}} q_{i} \\
& P\left(t_{x} \mid \mathbf{u}\right)=1-\prod_{\left\{i \mid u_{i}=t_{i}\right\}} q_{i}
\end{aligned}
$$

## 4 INTERESTING SPECIAL CASES

### 4.1 CHOICE OF A FUNCTION $F$

The generalized model described above allows the use of any discrete function $F$ relating $\mathbf{U}$ to $X$. We now suggest a particular form of $F$ that is 'compatible' with the Boolean Noisy-Or, i.e., $F$ degenerates to the Boolean OR function when the inputs and outputs are Boolean ${ }^{23}$ :

$$
F\left(\mathbf{u}^{\prime}\right)=x\left(\left\lceil\left(m_{x}-1\right)\left(\frac{1}{n} \sum_{i} \frac{l_{i}^{\prime}\left(u_{i}^{\prime}\right)}{\left(m_{i}-1\right)}\right)\right\rceil\right)
$$

In essence, this function is a weighted average - we are finding the fraction of each input's state's index over the maximum possible index of that input, averaging these fractions, scaling this quantity to the maximum index of the output, and mapping back to an actual state of the output after converting the scaled result to an integer.

[^0]
[^0]:    ${ }^{1}$ For Boolean variables we define the index of the "false" state to be 0 and the index of the "true" state to be 1 .
    ${ }^{2}$ We use the syntax [] for the Ceiling function. For a real number $x,|x|$ is the smallest integer $i$ that satisfies $i \geq x$.
    ${ }^{3}$ In the following equation, note again that $x(j)$ denotes the $j$ th state of $X$.

This additive function will have the characteristic that as any input goes 'higher' it will tend to drive the output 'higher'. Further, the inputs are 'equally weighted' regardless of their arity. So, for example, a change from state 0 to state 1 in a Boolean input will have just the same effect as a change from 0 to 5 in an input with 6 states. Finally, the output is 0 if and only if all the inputs are 0 .

We note that this function reduces to the Boolean OR function in the case where all inputs are Boolean and the output is Boolean.

### 4.2 CASE OF BOOLEAN OUTPUT AND $n$ ARY INPUTS

Consider the case where $X$ is a Boolean variable and the inputs $U_{i}$ are nary. The function $F$ is defined as in the previous section. Further, we define $P_{i}^{i n h}(0)=q_{i}$ and $P_{i}^{i n h}(j)=0$ for $j \neq 0$. We see that we have a restricted generalization of the Boolean Noisy-Or.

This special case of nary inputs and Boolean output is interesting since it has better computational properties than the general case while being more general than the Boolean Noisy-Or (see Sec 5.2).

### 4.3 OBTAINING STRICTLY POSITIVE DISTRIBUTIONS

In some situations it is desirable for the conditional distribution of a Bayesian network node $X$ with predecessors $\mathbf{U}$ to be strictly positive, i.e., $\forall x \forall \mathbf{u} P(x \mid \mathbf{u})>0$.

For the generalized Noisy-Or model, the definition of $P(x \mid \mathbf{u})$ is in Equation 2. From this definition we note that the following condition is necessary to ensure a strictly positive distribution:

For all states $x$ of $X$, the set $\left\{\mathbf{u}^{\prime} \mid x=\right.$ $\left.F\left(\mathbf{u}^{\prime}\right)\right\}$ is not empty. In other words, $F$ should be a function that maps onto $X$.

This condition is a natural restriction - if $F$ does not satisfy this condition, the variable $X$, in effect, has superfluous states. For example, the function defined in Section 4.1 satisfies this restriction.

Assuming that the above condition is satisfied, the following condition is sufficient (though not necessary) to ensure a strictly positive distribution:

For any $\mathbf{u}^{\prime}$ and $\mathbf{u}, P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right)>0$, i.e., $\prod_{\mathbf{u}^{\prime}} P_{i}\left(u_{i}^{\prime} \mid u_{i}\right)>0$.
This second condition is a stronger restriction. From Equation 1 we note that this restriction is equivalent to requiring that all inhibitor probabilities be strictly positive, i.e., that $P_{i}^{i n h}(j)>0$ for all $0 \leq j<m_{i}$.

Finally, we note that the Boolean Noisy-Or formulation of [Pearl 1988] and its generalization to nary inputs described in Section 4.2 always result in a distribution which is not strictly positive since $P\left(t_{x} \mid \mathbf{f}\right)=0$.

## 5 COMPUTING $P(X \mid \mathbf{U})$

We consider the complexity of generating the probabilities in the table $P(X \mid \mathbf{U})$.

Let $S=\prod_{i} m_{i}$ be the size of the joint state space of all the inputs $U_{i}$. We first note that $P_{i}\left(u_{i}^{\prime} \mid u_{i}\right)$ can be computed in $\Theta(1)$ time from the inhibitor probabilities. This leads to:

$$
P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right)=\prod_{i} P_{i}\left(u_{i}^{\prime} \mid u_{i}\right)=\Theta(n)
$$

Therefore:

$$
P(x \mid \mathbf{u})=\sum_{\{x \mid x=F\left(\mathbf{u}^{\prime}\right)\}} P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right)=\Theta(S n)
$$

This is because, for a given $x$ and $\mathbf{u}$ we have to traverse the entire state space of $\mathbf{U}^{\prime}$ to check which $\mathbf{u}^{\prime}$ satisfy $x=F\left(\mathbf{u}^{\prime}\right)$.

To compute the entire table we can naively compute each entry independently in which case we have:

$$
P(X \mid \mathbf{U})=m_{x} S \Theta(S n)=\Theta\left(m_{x} n S^{2}\right)
$$

However the following algorithm computes the table in $\Theta\left(n S^{2}\right)$ :

## Begin Algorithm

For each state $\mathbf{u}$ of $\mathbf{U}$ :

- For all states $x$ of $X$ set $P(x \mid \mathbf{u})$ to 0 .
- For each state $\mathbf{u}^{\prime}$ of $\mathbf{U}^{\prime}$ :
- Set $x=F\left(\mathbf{u}^{\prime}\right)$.
- Increment $P(x \mid \mathbf{u})$ by $P\left(\mathbf{u}^{\prime} \mid \mathbf{u}\right)$.


## End Algorithm

### 5.1 BOOLEAN NOISY-OR

In the case of the Boolean Noisy-Or, all $U_{i}$ and $X$ are Boolean variables. We see from Sec 3.1 that:

$$
P\left(f_{x} \mid \mathbf{u}\right)=\prod_{\left\{i \mid u_{i}=t_{i}\right\}} q_{i}=\Theta(n)
$$

For computing the table, we see that since $P\left(t_{x} \mid \mathbf{u}\right)=1-P\left(f_{x} \mid \mathbf{u}\right)$, we can compute both probabilities for a particular $\mathbf{u}$ in $\Theta(n)$ time. So the time required to calculate the entire table $P(X \mid \mathbf{U})$ is $\Theta(S n)$.

We see that in the case of the Boolean Noisy-Or there is a substantial saving over the general case in computing probabilities. This saving is achieved by taking into account the special characteristics of the Boolean OR function and the inhibitor probabilities when computing the distribution.

### 5.2 BOOLEAN OUTPUT AND $n$ ARY INPUTS

From an analysis similar to the previous section we note that computation of $P(X \mid \mathbf{U})$ takes $\Theta(S n)$ time in this case too.

### 5.3 STORAGE COMPLEXITY

For the general case we need to store $m_{i}$ inhibitor probabilities per predecessor. Therefore in this case $O\left(n m_{\max }\right)$ storage is required where $m_{\max }=$ $\max _{i}\left(m_{i}\right)$. This contrasts with $O\left(m_{x} m_{\max }^{n}\right)$ for storing the whole probability table.

For the Boolean Noisy-Or we need to store one inhibitor probability per predecessor and this is $\Theta(n)$. Using tables instead would cost $\Theta\left(2 \times 2^{n}\right)=$ $\Theta\left(2^{n}\right)$.

In the case of nary inputs and Boolean output (as described above) one inhibitor probability per predecessor is stored. Thus storage requirement is $\Theta(n)$. Using a table would cost $O\left(m_{\max }^{n}\right)$.

### 5.4 REDUCING COMPUTATION COMPLEXITY

In general, one could reduce the complexity of computing $P(x \mid \mathbf{u})$ if one could take advantage of special properties of the function $F$ to efficiently generate those $\mathbf{u}^{\prime}$ that satisfy $x=F\left(\mathbf{u}^{\prime}\right)$ for a particular $x$.

Given a function $F$, we thus need an efficient algorithm Invert such that Invert $(x)=\{\mathbf{u} \mid x=$ $F(\mathbf{u})\}$. By choosing $F$ carefully one can devise efficient Invert algorithms. However, to be useful as a modeling device, the choice of $F$ has also to be guided by the more important criterion of whether $F$ does indeed model a frequently occurring class of phenomena.

This Noisy-Or generalization has high complexity for computing probability tables from the inhibitor probabilities ${ }^{4}$. If the generalization is seen mostly as a useful modeling paradigm, then this complexity is not a problem, since the inhibitor probabilities can be pre-compiled into probability tables before inference takes place. Inference can be then performed with standard Bayesian network propagation algorithms.

If this generalization, however, is seen as a method of saving storage by restricting the models to a specific kind of interaction, the cost of computing the probabilities on the fly may outweigh the gains of saving space.

[^0]![img-1.jpeg](img-1.jpeg)

Each line has the probability of failure marked on it.
Figure 2: A digital circuit
![img-2.jpeg](img-2.jpeg)

For every link the failure function $N$ has the following inhibitor probabilities (where $X$ is the predecessor variable of the link):
$P_{N}^{l n h}(f)=0.01$ and $P_{N}^{l n h}(t)=0$
Figure 3: A generalized Noisy or model of the circuit

## 6 EXAMPLES

### 6.1 DIGITAL CIRCUIT DIAGNOSIS

The generalized Noisy-Or provides a straightforward method for doing digital circuit diagnosis. Consider the circuit in Fig 2. Let us assume that each line (i.e., wire) in the circuit has a probability of failure of 0.01 and that when a line fails, the input to the devices downstream of the line is false.

Each of the inputs to the devices in the circuit is now modeled with a state variable in a Noisy-Or model (see Fig 3). The function $F$ for the generalized Noisy-Or which is associated with each node is the truth table of the digital device whose output the node represents. We have an inhibitor probability of 0.01 associated with the false state along each link and an inhibitor probability of 0 associated with the true state (since the lines cannot fail in the true state in our fault model).

A Bayesian network is now constructed from the Noisy-Or model (see Fig 4) using the algorithm described in Section 5. Note that to complete the Bayesian network one needs the marginal distributions on the inputs to the circuit. Here we have made a choice of uniform distributions for these


[^0]:    ${ }^{4}$ However, the Boolean Noisy Or does not suffer from this problem since the special structure of the $F$ function and the fact that the inputs and outputs are Boolean reduce the complexity dramatically by a factor of $S$.

![img-3.jpeg](img-3.jpeg)

Figure 4: Bayesian network for digital circuit example.
marginals. ${ }^{5}$
As an example of the use of the resulting Bayesian network, consider the diagnostic question "What is the distribution of $D$ given $F$ is false and $B$ is true ?". The evidence $B=t$ and $F=f$ is declared in the Bayesian network and any standard update algorithm like the Jensen-Spiegelhalter [Jensen 1989, Lauritzen 1988] algorithm is used to yield the distribution $P(D=t \mid F=f, B=t)=$ 0.984 and $P(D=f \mid F=f, B=t)=0.016$.

Note that this example does not include a model for device failure - only line failures are considered. However the method can be extended easily to handle device failure by replacing every device $G$ in the circuit with the 'extended' device $G^{\prime}$ as shown in Fig 5. In this figure, the input (variable) $G_{f}$ has a marginal distribution which reflects the probability of failure of the device. All the inhibitor probabilities on the line $G_{f}$ are set to 0 . Note that the particular fault model illustrated here is a 'failed at false' model, i.e., when the device is broken, its output is false. One nice feature of the method described above is that it is incremental. If a device is added or removed from the underlying circuit a corresponding node can be added or removed from the Bayesian

[^0]![img-4.jpeg](img-4.jpeg)

Figure 5: Modeling device failure with an 'extended' device.
![img-5.jpeg](img-5.jpeg)

Each link has the probability of failure marked on it.
Figure 6: A network with unreliable links.
network - there is no need to construct a complete diagnostic model from scratch.

This method relates very well to the model based reasoning approach in this particular domain [deKleer 1987, deKleer 1989, Geffner 1987]. We describe a probabilistic approach to modelbased diagnosis using Bayesian networks in detail in [Srinivas 1993b, Srinivas 1993a].

### 6.2 NETWORK CONNECTIVITY

The following example uses the Boolean Noisy-Or and the following example generalizes it to use the generalized Noisy-Or.

Consider the network shown in Fig 6. Say each link is unreliable - when the link is 'down' the link is not traversable. The reliability of each link $L$ is quantified by a probability of failure $l$ (marked on the link in the network). Now consider the question "What is the probability that a path exists from $A$ to $G$ ?".

Consider the subset of the network consisting of $A$ and its descendants (in our example, for simplicity, this is the whole network). We first associate each node with the Boolean OR as the $F$ function. Each of the link failure probabilities translates directly into the inhibitor probability for the false state along each link. The inhibitor probability for the true state is 0 .

This network is now used to create a Bayesian network using the algorithm of Sec 5. The Bayesian


[^0]:    ${ }^{5}$ These marginals can be seen as the distribution over the inputs provided by the environment outside the circuit. Such a distribution is not usually available. But when the distribution is not available, all diagnosis is perforce carried out with the assumption that all inputs are known. Furthermore, when all the inputs are known, it is to be noted that the answer to any diagnostic question is not affected by the actual choice of marginal as long as the marginal is any strictly positive distribution.

network has the same topology as the network in Fig 6. To complete the distribution of the Bayesian network the root node $A$ has to be assigned a marginal distribution. We assign an arbitrary strictly positive distribution to the root node $A$ (since evidence is going to be declared for the root node, the actual distribution is irrelevant).

The answer to the question asked originally is now obtained as follows: Declare the evidence $A=t$ (and no other evidence), do evidence propagation and look at the updated belief of $G$. In this example, we get $\operatorname{Bel}(G=t)=0.7874$ and $\operatorname{Bel}(G=f)=$ $0.2126 .{ }^{6}$ These beliefs are precisely the probabilities that a path exists or does not exist respectively from $A$ to $G$.

To see why, consider the case where link failures cannot happen (i.e., link failure probability is zero). Then if any variable in the network is declared to be true then every downstream variable to which it has some path will also be true due to the nature of the Boolean OR function. Once the failure probabilities are introduced, belief propagation gives us, in essence, the probability that a connected set of links existed between $A$ and $G$ forcing the OR gate at $G$ to have the output true.

Furthermore, it is to be noted that because belief propagation updates beliefs at every node, the probability of a path existing from $A$ to any node $X$ downstream of it is available as $\operatorname{Bel}(X=t)$.

This method can be extended with some minor variations to answer more general questions of the form "What is the probability that there exists a path from any node in a set of nodes $S$ to a target node $T$ ?".

### 6.3 NETWORK CONNECTIVITY EXTENDED

Consider the exact same network as in the previous example. The question now asked is "What is the probability distribution over the number of paths existing from $A$ to $G$ ?".

Consider the subset of the network consisting of $A$ and its descendants. For every node $U$ we make the number of states be $n_{U}+1$ where $n_{U}$ is the number of paths from root node $A$ to the node $U$. The states of $U$ are numbered from 0 through $n_{U}$. We will refer to the $i$ th state of node $U$ as $u(i)$.

The number $n_{U}$ can be obtained for each node in the network through the following simple graph traversal algorithm:

## Begin Algorithm

[^0]- For root node $A$, set $n_{A}=1 .^{7}$
- For every non root node $U$ in the graph considered in graph order (with ancestors before descendants):
$n_{U}=\sum_{p \in \text { Parents }(U)} n_{p}$


## End Algorithm

To build the Noisy-Or model, we now associate integer addition as the function $F$ associated with each node. For example, if $R$ and $S$ are parents of $T$ and the state of $R$ is known to be $r_{3}$ and the state of $S$ is known to be $s_{3}$, then the function maps this state of the parents to state $t_{(2+3)}=t_{5}$ of the child $T$.

We now set the inhibitor probabilities as follows: Say the predecessor node of some link $L$ in the graph is a node $U$. We set the inhibitor probability for state $u(0)$ to be the link failure probability $l$ and all other inhibitor probabilities to be 0 . That is $P_{U}^{i n h}(0)=l$, where $l$ is the link failure probability and $P_{U}^{i n h}(i)=0$ for $i=1,2 \ldots, n_{U}$.

We now construct the Bayesian network from the network described above. The marginal probability for the root node is again set arbitrarily to any strictly positive distribution since it has no effect on the result.

The answer to the question posed above is obtained by declaring the evidence $A=1$ and then doing belief propagation to get the updated beliefs for $G$. The updated belief distribution obtained for $G$ is precisely the distribution over the number of paths from $A$ to $G$.

To see why, consider the case where there are no link failures. Then when $A$ is declared to have the value 1 , the addition function at each downstream nodes counts exactly the number of paths from $A$ to itself. Once the failures are introduced the exact count becomes a distribution over the number of active paths.

In this example, we get the distribution: $\operatorname{Bel}(G=0)=0.2126, \operatorname{Bel}(G=1)=0.3466$, $\operatorname{Bel}(G=2)=0.2576, \operatorname{Bel}(G=3)=0.1326$ and $\operatorname{Bel}(G=4)=0.0506$. We see that $\operatorname{Bel}(G=0)$ is the same probability as $\operatorname{Bel}(G=f)$ in the previous example, viz, the probability that no path exists from $A$ to $G$.

Note that after belief updating, the distribution of number of paths from $A$ to any node $X$ downstream of it is available as the distribution $\operatorname{Bel}(X)$ after belief propagation.

This method can be extended with to answer more general questions of the form "What is the distribution over the number of paths that originate

[^1]
[^0]:    ${ }^{6}$ The updated belief $\operatorname{Bel}(X=x)$ of a variable $X$ is the conditional probability $P(X=x \mid E)$ where $E$ is all the available evidence.

[^1]:    ${ }^{7}$ We define the root node to have a single path to itself.

in any node in a set of nodes $S$ and terminate in a target node $T$ ?".

Another interesting example which can be solved using the generalized Noisy-Or is the probabilistic minimum cost path problem: Given a set of possible (positive) costs on each link of the network and a probability distribution over the costs, the problem is to determine the probability distribution over minimum cost paths between a specified pair of nodes.

The generalized Noisy-Or, in fact, can be used to solve an entire class of network problems [Srinivas 1993c]. The general approach is as in the examples above - the problem is modeled using the generalized Noisy-Or and then Bayesian propagation is used in the resulting Bayesian network to find the answer.

All the examples described above use the NoisyOr model at every node in the network. However, this is not necessary. Some sections of a Bayesian network can be constructed 'conventionally', i.e., by direct elicitation of topology and input of probability tables while other sections where the Noisy-Or model is applicable, can use the Noisy-Or formalism.

## 7 IMPLEMENTATION

This generalized Noisy-Or model has been implemented in the IDEAL [Srinivas 1990] system. When creating a Noisy-Or node, the user provides the inhibitor probabilities and the deterministic function $F$.

IDEAL ensures that all implemented inference algorithms work with Bayesian networks that contain Noisy-Or nodes. This is achieved by 'compiling' the Noisy-Or information of each node into a conditional probability distribution for the node. The distribution is available for all inference algorithms to use.

## Acknowledgements

I thank Richard Fikes, Eric Horvitz, Jack Breese and Ken Fertig for invaluable discussions and suggestions.
