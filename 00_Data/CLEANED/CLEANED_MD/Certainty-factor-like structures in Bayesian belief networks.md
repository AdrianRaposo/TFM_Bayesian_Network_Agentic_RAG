# Certainty-factor-like Structures in Bayesian Belief Networks 

Peter Lucas<br>Department of Computer Science, Utrecht University<br>Padualaan 14, 3584 CH Utrecht, The Netherlands<br>E-mail: lucas@cs.uu.nl


#### Abstract

The certainty-factor model was one of the most popular models for the representation and manipulation of uncertain knowledge in the early rule-based expert systems of the 1980s. After the model was criticised by researchers in artificial intelligence and statistics as being ad-hoc in nature, researchers and developers have stopped looking at the model. Nowadays, it is often stated that the model is merely interesting from a historical point of view. Its place has been taken over by more expressive formalisms for the representation and manipulation of uncertain knowledge, in particular by the formalism of Bayesian belief networks. In this paper, it is shown that this view underestimates the importance of the principles underlying the certainty-factor model. In particular, it is shown that certainty-factor-like structures occur frequently in practical Bayesian network models as causal independence assumptions. In fact, the noisy-OR and noisy-AND models, two probabilistic models frequently employed, appear to be reinventions of combination functions previously introduced as part of the certainty-factor model. This insight may lead to a reappraisal of the certainty-factor model.


Keywords: Bayesian networks, certainty-factor model, causal independence, noisy-OR model, noisy-AND model.

## 1 Introduction

In the early rule-based expert systems as developed in the 1980s, the representation and manipulation of uncertain knowledge was accomplished by various ad-hoc schemes. Typical examples of such schemes are the certainty-factor calculus of Shortliffe and Buchanan [4, 20] and the subjective Bayesian method [7]. At the time in particular the certainty-factor model enjoyed much popularity, possibly due to its mathematical and computational simplicity.

After the introduction of more expressive, and mathematically sound, probabilistic methods for the representation and manipulation of uncertainty the early methods have been criticised, sometimes severely, by researchers. Examples of such criticism are easily found in the literature; a selection is shown below (explanations added for the purpose of this paper are written in parentheses). For example, Heckerman states ([9], page 309):
". . . it is recommended that those who intend to build a system incorporating the certainty factor model consider these more general techniques (i.e. Bayesian belief networks)."

whereas Neapolitan states ([17], pages 70-71):
"The calculus for combining certainty factors ... is of interest primarily for its historical significance."

Jensen's opinion is even stronger ([14], page 3):
"... it is not possible to capture reasoning with uncertainty with inference rules for production rules."

In contrast, the criticism of Pearl is more moderate ([18], page 6):
"The price attached to extensional systems (e.g. rule-based systems) is that they often yield updating that is incoherent, i.e. subject to surprise and counterintuitive conclusions."

Nowadays, the majority of AI and uncertainty in AI researchers probably agrees with the opinions summarised above. They believe that the framework of Bayesian belief networks offers a coherent, expressive, and flexible formalism for the representation and manipulation of uncertain knowledge, and there seems to be little reason to revert to the use of the early models of uncertainty. The author of this paper shares this opinion. Yet, the situation is not as clear-cut as it appears, and researchers should be aware of this.

In this paper it is shown that the certainty-factor model has in fact been reintroduced by Bayesian network theoreticians without knowing, and is used as an essential ingredient of many practical network models. It even appears that fragments of the certainty-factor model are currently very popular for the representation and manipulation of uncertainty. We think the results of this study to be important, because it shows that particular probabilistic models have been introduced by various research traditions independently, indicating their general significance. Furthermore, this study also sheds some light on current Bayesian belief network modelling practice. As we have not been able to find similar results in the literature, we believe this result to be new.

The structure of the remainder of this paper is as follows. In the next section, the certaintyfactor model is introduced. Next, we study various probabilistic models that seem good candidates for their mapping to fragments of the certainty-factor model. To what extent such mappings are possible is also investigated. The practical significance of the various probabilistic models selected is next illustrated by a number of real-life applications as found in the literature. The paper is rounded off by a discussion of the practical consequences of the results achieved in this paper.

# 2 The certainty-factor model 

In this section, the basic principles of the certainty-factor model, so far as needed for the reading of this paper, are briefly reviewed.

### 2.1 Certainty factors

The certainty-factor model was introduced by Shortliffe and Buchanan as a method for the representation and manipulation of uncertain knowledge in the rule-based expert system

MYCIN [20, 4], and later incorporated, in slightly modified form, in the prototypical rulebased expert-system shell EMYCIN [4]. The basic idea underlying the method is that when representing knowledge as production rules of the form if $e$ then $h_{x} \mathbf{f i}$, a measure of uncertainty $x$ is associated with the hypothesis $h$, expressing the degree to which the observation of evidence $e$ influences the confidence in $h$. In developing the certainty-factor model Shortliffe and Buchanan have chosen two basic measures of uncertainty: the measure of belief $\mathrm{MB}(h, e)$ expressing the degree to which an observed piece of evidence $e$ increases the belief in a hypothesis $h$, and the measure of disbelief $\mathrm{MD}(h, e)$, expressing the degree to which an observed piece of evidence $e$ decreases the belief in a hypothesis $h$. Each of these measures lie in the closed interval $[0,1]$.

The measure of belief $\mathrm{MB}(h, e)$ and the measure of disbelief $\mathrm{MD}(h, e)$ are defined in terms of probability theory as relative changes with respect to the prior probability $\operatorname{Pr}(h)$, based on available evidence $e$. Although intuitively attractive at first sight, Heckerman [9] and Van der Gaag [22] showed that this choice renders the certainty-factor model inconsistent with the basic axioms of probability theory. Heckerman, however, has been able to find alternative definitions for these measures in terms of likelihood ratios, yielding mathematically sound probabilistic interpretations of the model [9].

A certainty factor $\mathrm{CF}(h, e)$ is just a numerical measure between -1 and +1 , defined in terms of measures of belief and disbelief. The actual definition is not relevant for this paper (cf. [15]). A negative certainty factor indicates that the hypothesis $h$ is disconfirmed by the evidence $e$; a positive certainty factor indicates that the hypothesis $h$ is confirmed by the evidence $e$. A certainty factor equal to zero indicates that the evidence $e$ does not influence the belief in the hypothesis $h$. In most implementations of the certainty factor model, the measures of belief $\mathrm{MB}(h, e)$ and disbelief $\mathrm{MD}(h, e)$ are no longer used; only the certainty factor is employed. Consequently, with each production rule if $e$ then $h$ fi is now associated a certainty factor $\mathrm{CF}(h, e)$; this can also be depicted as a directed graph, as shown below:

# 2.2 Combination functions 

For the manipulation of certainty factors, Shortliffe and Buchanan have defined a number of combination functions, expressed in terms of certainty factors. For an extensive motivation underlying their design, the reader is referred to [4].

The combination function for the propagation of uncertain evidence from the antecedent of a production rule to its consequences, as shown in the following directed graph

$$
e^{\prime} \quad \frac{\mathrm{CF}\left(e, e^{\prime}\right)}{e} e \quad \frac{\mathrm{CF}(h, e)}{h}
$$

is the following:

$$
\mathrm{CF}\left(h, e^{\prime}\right)=\mathrm{CF}(h, e) \cdot \max \left\{0, \mathrm{CF}\left(e, e^{\prime}\right)\right\}
$$

Here, $\mathrm{CF}(h, e)$ is the certainty factor associated with the hypothesis $h$ by the production rule if $e$ then $h$ fi if the evidence $e$ has been observed with absolute certainty; $\mathrm{CF}\left(e, e^{\prime}\right)$ indicates the actual confidence in $e$ based on some prior evidence $e^{\prime}$, and acts as a weighting factor to

$\mathrm{CF}(h, e)$. If the rule's antecedent is false, the resulting weighting factor will be 0 , as indicated in formula (1).

The function for combining two certainty factors $\mathrm{CF}\left(e_{1}, e^{\prime}\right)$ and $\mathrm{CF}\left(e_{2}, e^{\prime}\right)$ of two constituting pieces of evidence $e_{1}$ and $e_{2}$ to obtain a certainty factor for the conjunction $e_{1}$ and $e_{2}$ of these pieces of evidence, as shown in the directed graph below
![img-0.jpeg](img-0.jpeg)
is the following:

$$
\mathrm{CF}\left(e_{1} \text { and } e_{2}, e^{\prime}\right)=\min \left\{\mathrm{CF}\left(e_{1}, e^{\prime}\right), \mathrm{CF}\left(e_{2}, e^{\prime}\right)\right\}
$$

For the disjunction of two pieces of evidence, we have the following formula:

$$
\mathrm{CF}\left(e_{1} \text { or } e_{2}, e^{\prime}\right)=\max \left\{\mathrm{CF}\left(e_{1}, e^{\prime}\right), \mathrm{CF}\left(e_{2}, e^{\prime}\right)\right\}
$$

The combination functions (2) and (3) are commutative and associative in their first argument; so the order in which conjunctions and disjunctions are evaluated has no effect on the resulting certainty factor.

Finally, the combination function for combining two certainty factors $\mathrm{CF}\left(h, e_{1}^{\prime}\right)$ and $\mathrm{CF}\left(h, e_{2}^{\prime}\right)$ which have been derived from two co-concluding production rules if $e_{i}$ then $h$ $\mathbf{f i}, i=1,2$, as shown in the following directed graph
![img-1.jpeg](img-1.jpeg)
is as follows:

$$
\mathrm{CF}\left(h, e_{1}^{\prime} \text { co } e_{2}^{\prime}\right)= \begin{cases}x+y(1-x) & \text { if } x, y>0 \\ \frac{x+y}{1-\min \{|x|,|y|\}} & \text { if }-1<x y \leq 0 \\ x+y(1+x) & \text { if } x, y<0\end{cases}
$$

where $\mathrm{CF}\left(h, e_{1}^{\prime}\right)=x$ and $\mathrm{CF}\left(h, e_{2}^{\prime}\right)=y$. Combination function (4) is commutative and associative in its second argument; so, the order in which production rules are applied has no effect on the final result.

As mentioned above, Heckerman has proposed a number of suitable transformations of the certainty-factor model to probability theory [9]; it is therefore known that the model, with slightly altered definitions, permits a probabilistic interpretation. Although important as a result, this work is still in line with the basic ideas of Shortliffe and Buchanan, in the sense that the original model was the central focus of the study; the meaning of certainty factors as changes to belief states was left unchanged. Our goals are different, because we employ the certainty-factor model as a tool in the analysis of Bayesian belief network models. Thus,

![img-2.jpeg](img-2.jpeg)

Figure 1: Causal independence model.
we are actually interested in the inverse problem. Taking solving the inverse problem as our aim, it seems unnecessary complicated to maintain the idea of certainty factors as modelling belief changes, and we shall therefore abandon this idea. In facts, although certainty factors were originally defined in terms of probability theory, they have never been used in this way, not even in the MYCIN system for which the model was originally developed.

Below, it is investigated under which conditions Bayesian belief network models correspond to ingredients of the certainty-factor model.

# 3 Certainty-factor interpretation of Bayesian belief networks 

Above, we have summarised the principles of the certainty-factor model. In this section, we trace probabilistic models that correspond to fragments of the certainty-factor model.

### 3.1 Employed notation

Stochastic variables will be denoted by upper-case letter, e.g. $X$; values of variables will be denoted by lower-case letters, e.g. $x$. In the case of binary variables, the value $X=$ true will be denoted by $X=x$, or simply $x$; the value $X=$ false is denoted by $X=\neg x$, or simply $\neg x$. All variables are assumed to be discrete. By an expression like

$$
\sum_{f\left(X_{1}, \ldots, X_{n}\right)=c} \psi\left(X_{1}, \ldots, X_{n}\right)
$$

is indicated a summation of function values of a function $\psi$, ranging over all possible values of the variables $X_{1}, \ldots, X_{n}$ satisfying the functional constraint $f\left(X_{1}, \ldots, X_{n}\right)=c$. A probability distribution will be denoted by Pr.

### 3.2 Causal independence

In building Bayesian belief networks for practical purposes it has been argued by several researchers that considering the assumption of causal independence may be very fruitful [8, 10, $11,12]$. The global structure of a causal-independence model is shown in Figure 1; it expresses the idea that causes $C_{1}, \ldots, C_{n}$ influence a given common effect $E$ through intermediate variables $I_{1}, \ldots, I_{n}$ and a deterministic function $f$. The influence of each cause $C_{k}$ on the common effect $E$ is independent of each cause $C_{j}, j \neq k$. The function $f$ represents in which way the intermediate effects $I_{k}$, and indirectly also the causes $C_{k}$, interact to yield a final effect $E$. Hence, this function $f$ is defined in such way that when a relationship as modelled

by the function $f$ between $I_{k}=i_{k}, k=1, \ldots, n$, and $E=e$ is satisfied, then it holds that $e=f\left(i_{1}, \ldots, i_{n}\right)$.

In terms of probability theory, the notion of causal independence can be formalised for a distinguished value $e$ of $E$ as follows:

$$
\operatorname{Pr}\left(e \mid C_{1}, \ldots, C_{n}\right)=\sum_{f\left(I_{1}, \ldots, I_{n}\right)=e} \operatorname{Pr}\left(e \mid I_{1}, \ldots, I_{n}\right) \operatorname{Pr}\left(I_{1}, \ldots, I_{n} \mid C_{1}, \ldots, C_{n}\right)
$$

meaning that the causes $C_{1}, \ldots, C_{n}$ influence the common effect $E$ through the intermediate effects $I_{1}, \ldots, I_{n}$ only when $e=f\left(I_{1}, \ldots, I_{n}\right)$ for certain values $I_{k}=i_{k}, k=1, \ldots, n$. Under this condition, it is assumed that $\operatorname{Pr}\left(e \mid i_{1}, \ldots, i_{n}\right)=1$; otherwise, when $f\left(i_{1}, \ldots, i_{n}\right)=e^{\prime} \neq e$, it holds that $\operatorname{Pr}\left(e \mid i_{1}, \ldots, i_{n}\right)=0$. Note that the effect variable $E$ is conditionally independent of $C_{1}, \ldots, C_{n}$ given the intermediate variables $I_{1}, \ldots, I_{n}$, and that each variable $I_{k}$ is only dependent on its associated variable $C_{k}$; hence, it holds that

$$
\operatorname{Pr}\left(e \mid I_{1}, \ldots, I_{n}, C_{1}, \ldots, C_{n}\right)=\operatorname{Pr}\left(e \mid I_{1}, \ldots, I_{n}\right)
$$

and

$$
\operatorname{Pr}\left(I_{1}, \ldots, I_{n} \mid C_{1}, \ldots, C_{n}\right)=\prod_{k=1}^{n} \operatorname{Pr}\left(I_{k} \mid C_{k}\right)
$$

The formula above can now be simplified to:

$$
\operatorname{Pr}\left(e \mid C_{1}, \ldots, C_{n}\right)=\sum_{f\left(I_{1}, \ldots, I_{n}\right)=e} \prod_{k=1}^{n} \operatorname{Pr}\left(I_{k} \mid C_{k}\right)
$$

Based on the assumptions above, it also holds that

$$
\operatorname{Pr}\left(e \mid C_{1}, \ldots, C_{n}\right)=\sum_{I_{1}, \ldots, I_{n}} \operatorname{Pr}\left(e \mid I_{1}, \ldots, I_{n}\right) \prod_{k=1}^{n} \operatorname{Pr}\left(I_{k} \mid C_{k}\right)
$$

Formula (5) above is practically spoken not very useful, because the size of the specification of the function $f$ is exponential in the number of its arguments. The resulting probability distribution is therefore in general computationally intractable, both in terms of space and time requirements. An important subclass of causal independence models, however, is formed by models in which the deterministic function $f$ can be defined in terms of separate binary functions $g_{k}$, also denoted by $g_{k}\left(I_{k}, I_{k+1}\right)$. Such causal independence models have been called decomposable causal independence models [11]; these models are of significant practical importance. Usually, all functions $g_{k}\left(I_{k}, I_{k+1}\right)$ are identical for each $k$; a function $g_{k}\left(I_{k}, I_{k+1}\right)$ may therefore be simply denoted by $g\left(I, I^{\prime}\right)$. Typical examples of decomposable causal independence models are the noisy-OR $[5,8,13,18,21]$ and noisy-MAX $[5,12,21]$ models. Other popular causal independence models are the noisy-AND and noisy-MIN models. These models will be studied below.

# 3.3 Noisy-OR model 

As shown above, it is the precise definition of the function $f$ of a causal independence model that distinguishes one model from the other. Hence, for simplicity's sake, it is allowed to discard intermediate variables. Also, since only the use of decomposable causal independence

![img-3.jpeg](img-3.jpeg)

Figure 2: Three-node model.
models is practically feasible, it seems justified to merely consider three-node models as shown in Figure 2, without loss of generality.

Now, suppose that the three variables $A, B$ and $C$ are binary variables, and assume that node $C$ represents a logical OR, i.e.:

$$
\operatorname{Pr}(c \mid A, B)=\left\{\begin{array}{ll}
0 & \text { if } A=\neg a \text { and } B=\neg b \\
1 & \text { otherwise }
\end{array}\right.
$$

The binary functions $g_{k}$ as defined above all correspond to a logical OR, i.e. $g\left(i, i^{\prime}\right)=g_{k}\left(i, i^{\prime}\right)=$ $\left(i \vee i^{\prime}\right)$, for each $k$. The marginal probability $\operatorname{Pr}(C)$ is now obtained as follows:

$$
\begin{aligned}
\operatorname{Pr}(c) & =\sum_{A, B} \operatorname{Pr}(c \mid A, B) \operatorname{Pr}(A, B) \\
& =\operatorname{Pr}(a) \operatorname{Pr}(b)+\operatorname{Pr}(\neg a) \operatorname{Pr}(b)+\operatorname{Pr}(a) \operatorname{Pr}(\neg b)
\end{aligned}
$$

since the variables $A$ and $B$ are independent. We can rewrite this result in two different ways:

1. $\operatorname{Pr}(a) \operatorname{Pr}(b)+\operatorname{Pr}(\neg a) \operatorname{Pr}(b)+\operatorname{Pr}(a) \operatorname{Pr}(\neg b)=\operatorname{Pr}(a)+\operatorname{Pr}(b)(1-\operatorname{Pr}(a))$, which corresponds to the combination function for co-concluding production rule (4) in the certainty-factor model for positive certainty factors;
2. $\operatorname{Pr}(a) \operatorname{Pr}(b)+\operatorname{Pr}(\neg a) \operatorname{Pr}(b)+\operatorname{Pr}(a) \operatorname{Pr}(\neg b)=1-\operatorname{Pr}(\neg a, \neg b)=1-\operatorname{Pr}(\neg a) \operatorname{Pr}(\neg b)$ (because, $\operatorname{Pr}(\neg a, \neg b)$ was discarded in the sum above), which is a well-known formula used to define the noisy-OR model [18].

Note that $\operatorname{Pr}(\neg c)=1-\operatorname{Pr}(c)=\operatorname{Pr}(\neg a) \operatorname{Pr}(\neg b)$ is unspecified in the certainty-factor model, because certainty factors only concern positive literals. In principle, however, it might be dealt with by the method discussed below in Section 3.5. Actually, this limitation is not too important, because we take probability theory as our starting point. Hence, it appears that the noisy-OR model has exactly the same mathematical structure as combination function (4) for co-concluding production rules of the certainty-factor model for binary variables.

# 3.4 Noisy-MAX model 

When we drop the restriction that the variables in the three-node model must be binary, the probabilistic interpretation changes. Without loss of generality, let us assume that $A, B$ and $C$ are ternary variables. Furthermore, assume that the values of the given variables satisfy the following linear order: $a_{1}>a_{2}>a_{3} ; a_{1}=b_{1}=c_{1}, a_{2}=b_{2}=c_{2} ; a_{3}=b_{3}=c_{3}$. Also assume that the function $g(A, B)=C$ that underlies a particular causal independence model


Figure 3: Enumeration of elements from which is selected for the computation of the probability distribution $\operatorname{Pr}(C)$.
defines a MAX function in accordance with the given linear order. The function $g$ is thus defined as follows:

$$
g(A, B)=\left\{\begin{array}{cl}
c_{1} & \text { if } A=a_{1} \text { or } B=b_{1} \\
c_{2} & \text { if } A=a_{2} \text { or } B=b_{2}, \text { and } \\
& A \neq a_{1} \text { and } B \neq b_{1} \\
c_{3} & \text { otherwise }
\end{array}\right.
$$

The resulting probabilistic model is known as the noisy-MAX model $[5,12]$.
Using this definition of $g$, it holds that

$$
\begin{aligned}
\operatorname{Pr}\left(c_{1}\right) & =\sum_{g(A, B)=c_{1}} \operatorname{Pr}(A) \operatorname{Pr}(B) \\
& =\sum_{A=a_{1} \vee B=b_{1}} \operatorname{Pr}(A) \operatorname{Pr}(B)
\end{aligned}
$$

Now, since

$$
\sum_{A, B} \operatorname{Pr}(A) \operatorname{Pr}(B)=1
$$

it follows that

$$
\begin{aligned}
\operatorname{Pr}\left(c_{1}\right) & =1-\sum_{A \neq a_{1}, B \neq b_{1}} \operatorname{Pr}(A) \operatorname{Pr}(B) \\
& =1-\operatorname{Pr}\left(\neg a_{1}\right) \operatorname{Pr}\left(\neg b_{1}\right)
\end{aligned}
$$

The last expression can be rewritten to $\operatorname{Pr}\left(c_{1}\right)=\operatorname{Pr}\left(a_{1}\right)+\operatorname{Pr}\left(b_{1}\right)\left(1-\operatorname{Pr}\left(a_{1}\right)\right)$, which corresponds to the combination function for co-concluding production rules for positive certainty factors. Similarly, applying the definition of the noisy-MAX model to $\operatorname{Pr}\left(c_{2}\right)$ yields: $\operatorname{Pr}\left(c_{2}\right)=\operatorname{Pr}\left(a_{2}\right)\left(\operatorname{Pr}\left(b_{2}\right)+\operatorname{Pr}\left(b_{3}\right)\right)+\operatorname{Pr}\left(b_{2}\right) \operatorname{Pr}\left(a_{3}\right)$. However, according to the combination function for co-concluding production rules, we should have obtained: $\operatorname{Pr}^{\prime}\left(c_{2}\right)=\operatorname{Pr}\left(a_{2}\right)+$ $\operatorname{Pr}\left(b_{2}\right)\left(1-\operatorname{Pr}\left(a_{2}\right)\right)=\operatorname{Pr}\left(c_{2}\right)+\operatorname{Pr}\left(a_{1}\right) \operatorname{Pr}\left(b_{2}\right)+\operatorname{Pr}\left(a_{2}\right) \operatorname{Pr}\left(b_{1}\right)$; the two results differ.

The difference between the two results can be explained in terms of the matrix shown in Figure 3. Using the noisy-MAX model, the probability $\operatorname{Pr}\left(c_{i}\right)$ is defined as the sum of the probability $\operatorname{Pr}\left(a_{i}, b_{i}\right)$ on the diagonal of the matrix, supplemented with elements below and to the right of the element $\left(a_{i}, b_{i}\right)$, i.e.

$$
\operatorname{Pr}\left(c_{i}\right)=\operatorname{Pr}\left(a_{i}, b_{i}\right)+\sum_{j=i+1}^{n}\left(\operatorname{Pr}\left(a_{i}, b_{j}\right)+\operatorname{Pr}\left(a_{j}, b_{i}\right)\right)
$$

In the case of the combination function for co-concluding production rules, all elements on the $i$ th row and column are added, with the diagonal element $\operatorname{Pr}\left(a_{i}, b_{i}\right)$ just added once, resulting in:

$$
\operatorname{Pr}^{\prime}\left(c_{i}\right)=\sum_{j=1}^{n}\left(\operatorname{Pr}\left(a_{i}, b_{j}\right)+\operatorname{Pr}\left(a_{j}, b_{i}\right)\right)-\operatorname{Pr}\left(a_{i}, b_{i}\right)
$$

As a consequence, particular numbers $\operatorname{Pr}\left(a_{i}, b_{j}\right)$ will not only contribute to $\operatorname{Pr}^{\prime}\left(c_{i}\right)$, but also to $\operatorname{Pr}^{\prime}\left(c_{j}\right), i \neq j$, i.e. they are counted twice as part of the probability distribution $\operatorname{Pr}^{\prime}(C)$. The resulting probability distribution $\operatorname{Pr}^{\prime}$ is therefore inconsistent.

An interesting question is whether the probability distribution $\operatorname{Pr}^{\prime}$ can be made consistent, and, if so, in which way. The causal independence model that corresponds to the certaintyfactor model appears to be defined by the following function $g^{\prime}$ :

$$
g^{\prime}(A, B)=\left\{\begin{array}{ll}
c_{1} & \text { if } A=a_{1} \text { or } B=b_{1} \\
c_{2} & \text { if } A=a_{2} \text { or } B=b_{2} \\
c_{3} & \text { if } A=a_{3} \text { or } B=b_{3}
\end{array}\right.
$$

which is only identical to $g$ when $g^{\prime}(A, B)=c_{1}$. Although the function $g^{\prime}$ does not take the order of the values of the variables $C, B$ and $A$ into account, it is still very much alike the noisy-MAX model.

The probability distribution $\operatorname{Pr}^{\prime}$ can be rendered consistent by uniformly distributing the contribution of probabilities $\operatorname{Pr}\left(a_{i}, b_{j}\right)$ among $\operatorname{Pr}^{\prime}\left(c_{i}\right)$ and $\operatorname{Pr}^{\prime}\left(c_{j}\right), i \neq j$. This manipulation results in:

$$
\operatorname{Pr}^{\prime}\left(c_{i}\right)=\operatorname{Pr}\left(a_{i}\right) \operatorname{Pr}\left(b_{i}\right)+\frac{1}{2} \sum_{A=a_{i} \oplus B=b_{i}} \operatorname{Pr}(A) \operatorname{Pr}(B)
$$

where $\oplus$ denotes the exclusive OR operator. This equation is equal to $\frac{1}{2}\left(\operatorname{Pr}\left(a_{i}\right)+\operatorname{Pr}\left(b_{i}\right)\right)$, but not in general equal to $\frac{1}{2}\left(\operatorname{Pr}\left(a_{i}\right)+\operatorname{Pr}\left(b_{i}\right)\left(1-\operatorname{Pr}\left(a_{i}\right)\right)\right)$. Note that it holds that

$$
\begin{aligned}
\sum_{i=1}^{n} \operatorname{Pr}^{\prime}\left(c_{i}\right) & =\frac{1}{2} \sum_{i=1}^{n}\left(\operatorname{Pr}\left(a_{i}\right)+\operatorname{Pr}\left(b_{i}\right)\right) \\
& =1
\end{aligned}
$$

Hence, $\operatorname{Pr}^{\prime}$ is now consistent. We thus have shown that it is in general not possible to map the noisy-MAX model for non-binary variables to the combination functions of the certaintyfactor model by a similarity transformation, i.e. a transformation $T: U \rightarrow V$, such that $T(u)=c v+b, b, c \in \mathbb{R}$.

It appears that the causal independence model for non-binary variables using combination function (4) for co-concluding production rules is related to the noisy-MAX model, but nevertheless different for all but the probability of the value of the variable $C$ that is highest in the given linear order. The resulting model was shown to be probabilistically inconsistent. It is not difficult to resolve the inconsistency, yielding a model that is still related to the noisy-MAX model. However, the resulting probabilistic model cannot be represented in terms of the certainty-factor model.

# 3.5 Noisy-AND model 

The noisy-OR appears to be one of the most popular probabilistic models used in building practical Bayesian belief networks. However, this model is not suitable when one is primarily interested in modelling the conjunctive effect of particular causes. This idea naturally leads to the concept of the noisy-AND model. Using again the topology of the graph depicted in Figure 2, the noisy-AND model can be defined in terms of a probabilistic representation of the logical AND:

$$
\operatorname{Pr}(c \mid A, B)=\left\{\begin{array}{ll}
1 & \text { if } A=a \text { and } B=b \\
0 & \text { otherwise }
\end{array}\right.
$$

where $A, B$ and $C$ are binary stochastic variables. It now follows that:

$$
\begin{aligned}
\operatorname{Pr}(c) & =\sum_{A, B} \operatorname{Pr}(c \mid A, B) \operatorname{Pr}(A, B) \\
& =\operatorname{Pr}(a) \operatorname{Pr}(b)
\end{aligned}
$$

because $A$ and $B$ are independent. This result does not correspond to the combination function for co-concluding production rules (4). However, it is possible to represent the noisy-AND model in terms of the combination function for the propagation of evidence (1), using two production rules as follows:

$$
\begin{aligned}
& \text { if } a \text { then } b_{\operatorname{Pr}(b)} \mathbf{f i} \\
& \text { if } b \text { then } c_{1.0} \mathbf{f i}
\end{aligned}
$$

given the probability distributions $\operatorname{Pr}(A)$ and $\operatorname{Pr}(B)$, and assuming that the subscript 1.0 attached to $c$ represents a certainty factor. Using combination function (1) twice yields the required result for $C$.

### 3.5.1 Noisy-MIN model

As with the noisy-OR model, it is possible to generalise the noisy-AND model for non-binary variables; the result is known as the noisy-MIN model. Assume that the stochastic variables $A, B$ and $C$ are ternary variables, with values ordered as in Section 3.4. Also assume that the functions $g(A, B)=C$ underlying the causal independence model respects the linear order of values, yielding the minimum of its arguments as a result:

$$
g(A, B)=\left\{\begin{array}{cl}
c_{3} & \text { if } A=a_{3} \text { or } B=b_{3} \\
c_{2} & \text { if } A=a_{2} \text { or } B=b_{2}, \text { and } \\
& A \neq a_{3} \text { and } B \neq b_{3} \\
c_{1} & \text { otherwise }
\end{array}\right.
$$

Using this definition of $g$ yields the following result for $\operatorname{Pr}\left(c_{1}\right)$ :

$$
\begin{aligned}
\operatorname{Pr}\left(c_{1}\right) & =\sum_{g(A, B)=c_{1}} \operatorname{Pr}(A) \operatorname{Pr}(B) \\
& =\sum_{A=a_{1} \wedge B=b_{1}} \operatorname{Pr}(A) \operatorname{Pr}(B) \\
& =\operatorname{Pr}\left(a_{1}\right) \operatorname{Pr}\left(b_{1}\right)
\end{aligned}
$$

![img-4.jpeg](img-4.jpeg)

Figure 4: Propagation of evidence.

This probability can be mapped to the certainty-factor model in the same way as done for the noisy-AND model discussed above.

In general we have that

$$
\operatorname{Pr}\left(c_{i}\right)=\operatorname{Pr}\left(a_{i}, b_{i}\right)+\sum_{j=1}^{i-1}\left(\operatorname{Pr}\left(a_{i}, b_{j}\right)+\operatorname{Pr}\left(a_{j}, b_{i}\right)\right)
$$

which expresses that $\operatorname{Pr}\left(c_{i}\right)$ is obtained as the sum of $\operatorname{Pr}\left(a_{i}, b_{i}\right)$ on the diagonal of Figure 3, supplemented with elements $\operatorname{Pr}\left(a_{i}, b_{j}\right)$ on the $i$ th row to the left of element $\left(a_{i}, b_{i}\right)$ and elements $\operatorname{Pr}\left(a_{j}, b_{i}\right)$ on the $i$ th column above element $\left(a_{i}, b_{i}\right)$ of Figure 3.

For $\operatorname{Pr}\left(c_{2}\right)$ we thus get:

$$
\operatorname{Pr}\left(c_{2}\right)=\operatorname{Pr}\left(a_{2}\right) \operatorname{Pr}\left(b_{2}\right)+\operatorname{Pr}\left(a_{2}\right) \operatorname{Pr}\left(b_{1}\right)+\operatorname{Pr}\left(a_{1}\right) \operatorname{Pr}\left(b_{2}\right)
$$

No mapping exists in this case, and the same is true for $\operatorname{Pr}\left(c_{3}\right)$.
Similar to the noisy-MAX model, a mapping of the full noisy-MIN model to the certaintyfactor model is only possible for binary variables, in which case the noisy-MIN model and the noisy-AND model are identical.

# 3.6 Propagation of evidence 

Consider the probabilistic network shown in Figure 4; it is identical to the network model in Figure 2, except that a node $D$ is added. Let us assume that the corresponding variable $D$ only influences the uncertainty with respect to $A$ for the distinguished value $d$ ( $D$ is present); if $D$ is absent, i.e. $\neg d$, it holds that $A$ cannot occur, formally: $\operatorname{Pr}(a \mid \neg d)=0$. We only consider the noisy-OR probabilistic model of causal independence in this section.

Now, when assuming that evidence with respect to $D$ has been observed with certainty, it holds that:

$$
\begin{aligned}
\operatorname{Pr}(C \mid D) & =\sum_{A, B} \operatorname{Pr}(C, A, B \mid D) \\
& =\sum_{A, B} \operatorname{Pr}(C \mid A, B) \operatorname{Pr}(A \mid B, D) \operatorname{Pr}(B \mid D) \\
& =\sum_{A, B} \operatorname{Pr}(C \mid A, B) \operatorname{Pr}(A \mid D) \operatorname{Pr}(B)
\end{aligned}
$$

by the (conditional) independence information represented in the network. Let node $C$ again model a logical OR, as defined in Section 3.3. Under this condition, it holds that when $D=d$ :

$$
\operatorname{Pr}(c \mid d)=\operatorname{Pr}(a \mid d) \operatorname{Pr}(b)+\operatorname{Pr}(a \mid d) \operatorname{Pr}(\neg b)+\operatorname{Pr}(\neg a \mid d) \operatorname{Pr}(b)
$$

which is equal to $\operatorname{Pr}(a \mid d)+\operatorname{Pr}(b)(1-\operatorname{Pr}(a \mid d))$. This equation combines the effects of combination function (1), the propagation of evidence from $D$ to $A$, and combination function (4) for co-concluding production rules. Note that $\operatorname{Pr}(c \mid \neg d)=\operatorname{Pr}(\neg a \mid \neg d) \operatorname{Pr}(b)=\operatorname{Pr}(b)$, which result corresponds to the situation when the rule if $d$ then $a$ fi fails; only $B$ contributes to $C$. This result is again in accordance with the certainty-factor model.

Next, assume that $D$ is not known with certainty. We then get:

$$
\begin{aligned}
\operatorname{Pr}(C) & =\sum_{A, B, D} \operatorname{Pr}(C, A, B, D) \\
& =\sum_{A, B, D} \operatorname{Pr}(C, A, B \mid D) \operatorname{Pr}(D)
\end{aligned}
$$

Substituting results from the derivation of $\operatorname{Pr}(C \mid D)$ above in this equality, we obtain:

$$
\operatorname{Pr}(C)=\sum_{A, B, D} \operatorname{Pr}(C \mid A, B) \operatorname{Pr}(A \mid D) \operatorname{Pr}(B) \operatorname{Pr}(D)
$$

Again, using the causal independence assumption of the logical OR, the following result is obtained:

$$
\begin{aligned}
\operatorname{Pr}(c) & =\operatorname{Pr}(c \mid d) \operatorname{Pr}(d)+\operatorname{Pr}(c \mid \neg d) \operatorname{Pr}(\neg d) \\
& =(\operatorname{Pr}(a \mid d)+\operatorname{Pr}(b)(1-\operatorname{Pr}(a \mid d)) \operatorname{Pr}(d)+\operatorname{Pr}(b) \operatorname{Pr}(\neg d) \\
& =\operatorname{Pr}(a \mid d) \operatorname{Pr}(d)+\operatorname{Pr}(b)(1-\operatorname{Pr}(a \mid d) \operatorname{Pr}(d))
\end{aligned}
$$

This result corresponds again to the successive application of combination functions (1) and (4) in the certainty-factor model.

# 4 Practical significance 

Above we have seen that important Bayesian belief-network models, or parts of such models, can be mapped to fragments of the certainty-factor model. However, the results of this paper would have little significance, when in almost all practical belief-network models the assumptions underlying decomposable, causal independence would not be satisfied. But the opposite seems to be the case: in many practical Bayesian belief network models, a lot of causal independence assumptions are made. This is to be expected, because the technology of Bayesian belief networks is only practically useful when a large amount of information concerning independence, with causal independence as a special case, is available in a domain. A number of actual network models, as described in the literature, is briefly discussed to illustrate the point.

Heckerman and colleagues have described a probabilistic network for printer trouble shooting [12]. The structure of this network seems quite typical for networks used for detecting hardware faults. Assumptions of causal independence are rather essential ingredients of the network, and the arguments developed in this paper seems to fully apply to this network.

Díez and colleagues [6] have developed a Bayesian belief network for the diagnosis of heart disease, in which both the noisy-OR and noisy-MAX models are used to represent interactions among causes. Another, well-known example, is the probabilistic reformulation of Internist1/QMR, often referred to as QMR-DT (Decision-Theoretic reformulation of QMR), which uses the same assumptions [16].

Another interesting consequence of the results of this paper is that it at least partially explains the similarity in the conclusions of the assessment of the sensitivity of the MYCIN system to changes in certainty factors that was carried out in the 1970s [4], and a recent major study of the sensitivity of Bayesian belief networks to changes in their underlying probability distribution [19]. In both studies, it was concluded that the advice produced by the systems was rather insensitive to changes in the underlying numbers. However, the Bayesian belief networks that were studied incorporated noisy-OR and noisy-MAX models for the representation of interactions. Hence, the structural assumptions of these two studies were quite similar, which has not been recognised before.

Of course, causal independence does not play such an important role in all Bayesian belief networks. However, even in networks in which the notions of causal independence has not been adopted as a central modelling paradigm, e.g. the MUNIN network [2], such assumptions appear to underly a large part of the probabilistic assessments.

Although many Bayesian belief networks heavily rely on the assumption of causal independence, this does not mean that the certainty-factor calculus would be sufficient to manipulate such networks. This only holds when it is prevented that stochastic dependencies are introduced due to the entering of evidence. In networks purely used for diagnosis, and not for prediction purposes, causes of problems usually reside in the upper part of the network; findings that may be observed for a given case reside in the lower part of the network. When particular findings concerning a problem case are entered into the lower part of the network, new probabilistic dependencies would be induced. This could be handled by dynamically adapting the structure of the network, in such way that it explicitly reflects the new dependencies. Although this conclusion limits the practical usefulness of the certainty-factor calculus for such applications, it still holds that the underlying probabilistic model would be similar or even identical to fragments of the certainty-factor model.

In applications of prediction and planning it is in principle possible to use the certaintyfactor calculus as a method for probabilistic inference if the structure of the network follows the principles discussed in this paper. An example of such a network, meant to assist medical specialists in the treatment of infectious diseases, is described in [3]. This observation is interesting from the perspective of the design of efficient algorithms for probabilistic inference $[1,5,23,24]$.

# 5 Discussion 

As has been said at the beginning of this paper, it is not our intention to promote renewed popularity of the use of the certainty-factor model. Given the current state of research, this would be absurd. Still, the conclusion that the certainty-factor model is more important than most researcher would think possible seems inescapable. There can be learnt something from the early models of uncertainty in terms of probabilistic structures that have general significance.

We have studied the mapping of probabilistic structures to fragments of the certainty-

factor model. As was to be expected, only very specific probabilistic models can be dealt with in this way. For some probabilistic models a mapping was shown to exist; for other models, the mapping was only partial. Nevertheless, these structures appear to be of major practical importance to developers of Bayesian belief networks for specific problem domains. This explains why we believe that the results of this paper ought to be common knowledge to artificial-intelligence researchers.

We finally would like to plea for a more balanced view of the certainty-factor model: much too often researchers have expressed opinions about the model that are not supported by scientific facts.
