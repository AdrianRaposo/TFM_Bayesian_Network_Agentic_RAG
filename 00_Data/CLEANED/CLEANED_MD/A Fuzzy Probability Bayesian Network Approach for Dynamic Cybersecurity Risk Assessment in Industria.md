# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Zhang, Qi, Zhou, Chunjie, Tian, Glen, Xiong, Naixue, Qin, Yuanqing, \& Hu, Bowen
(2018)

A fuzzy probability Bayesian network approach for dynamic cybersecurity risk assessment in industrial control systems.
IEEE Transactions on Industrial Informatics, 14(6), pp. 2497-2506.
This file was downloaded from: https://eprints.qut.edu.au/223265/

## (c) Consult author(s) regarding copyright matters

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.1109/TII.2017.2768998

# A Fuzzy Probability Bayesian Network Approach for Dynamic Cybersecurity Risk Assessment in Industrial Control Systems 

Qi Zhang, Chunjie Zhou, Yu-Chu Tian, Naixue Xiong, Yuanqin Qin, Bowen Hu


#### Abstract

With the increasing deployment of data network technologies in industrial control systems (ICSs), cybersecurity becomes a challenging problem in ICSs. Dynamic cybersecurity risk assessment plays a vital role in ICS cybersecurity protection. However, it is difficult to build a risk propagation model for ICSs due to the lack of sufficient historical data. In this paper, a fuzzy probability Bayesian network (FPBN) approach is presented for dynamic risk assessment. Firstly, an FPBN is established for analysis and prediction of the propagation of cybersecurity risks. To overcome the difficulty of limited historical data, the crisp probabilities used in standard Bayesian networks (BNs) are replaced in our approach by fuzzy probabilities. Then, an approximate dynamic inference algorithm is developed for dynamic assessment of ICS cybersecurity risk. It is embedded with a noise evidence filter in order to reduce the impact from noise evidence caused by system faults. Experiments are conducted on a simplified chemical reactor control system to demonstrate the effectiveness of the presented approach.


Index Terms-cybersecurity, risk assessment, Bayesian network, fuzzy probability, industrial control systems.

## I. INTRODUCTION

IDUSTRIAL control systems (ICSs) are implemented worldwide in critical infrastructures [1]. They are integrated with computation, communication, and control theories [2], [3]. With the increasing deployment of data networks in ICSs, cybersecurity becomes a challenging ICS problem [4]-[8]. The number of cyberattacks to ICSs increases year by year [9]. This demands systematic research on cybersecurity risk analysis and cybersecurity protection for ICSs.

Cyberattacks to ICSs may lead to damage to, and losses of, physical infrastructure systems [10]. Cybersecurity risk of ICSs includes casualties, environment pollution, and asset losses. Cybersecurity protection in ICSs aims to minimize cybersecurity risk through implementing security strategies. Thus, risk-based dynamic cybersecurity protection is widely accepted in ICSs [11]. It generally consists of a number of components, e.g., intrusion detection, dynamic risk assessment, risk-based decision-making, and security strategy enforcement. A dynamic risk assessment system calculates ICS cybersecurity risk dynamically through analysis of real-time ICS data [12]. The risk value derived from the risk assessment provides important information for security decision-making. Thus, dynamic risk assessment plays an important role in cybersecurity protection of ICSs.

However, the calculation of ICS cybersecurity risk is difficult. One of the difficulties is the existence of various processes from launching a malicious attack to causing losses. Example processes are network penetration, privilege escalation, system anomaly, and hazardous incidents. Another
difficulty is the limited cyberattack data in a large amount of real-time data such as sensing data control commands. It is reported that 290 ICS cybersecurity incidents happened in 2016 [9]. This number is far less than that of cybersecurity incidents in general information technology (IT) systems. Thus, acquiring sufficient knowledge about cyberattacks and establishing a cybersecurity risk propagation model from the limited historical data become challenging.

Efforts have been made on modelling of cybersecurity risk. An example is the Bayesian attack graph method employed in risk assessment for prediction of potential malicious attacks [13]. The method calculates the probability of attacks by supervising the actions of attackers. Another example is the bow-tie model for assessment of industrial accidental risk [14]. However, both methods require a large amount of prior knowledge about attacks in their cybersecurity risk propagation models. They do not work in the presence of limited cyberattack data.

To address this issue, an FPBN approach is presented in this paper for dynamic risk assessment in ICSs. It consists of an FPBN model and a fuzzy approximate dynamic inference algorithm. The model is designed for analysis and prediction of cybersecurity risk. It uses fuzzy probabilities in our approach to replace the crisp probabilities required in a standard BN model. The inference algorithm is for dynamic assessment of ICS cybersecurity risk. It is integrated with a confidence index based noise evidence filter for elimination of noise evidence, thus improving the convergence of the algorithm.

This paper is organized as follows. Section II gives some background and preliminaries. Section III presents the architecture of our approach for dynamic assessment of cybersecurity risk in ICSs. This is followed by FPBN modelling in Section IV for cybersecurity risk propagation. In Section V, a fuzzy probability Bayesian inference algorithm is designed for dynamic risk assessment. Experiments are conducted in Section VI to demonstrate our approach. Finally, Section VII concludes the paper.

## II. BACKGROUND AND PRELIMINARIES

## A. Cybersecurity Risk Propagation in ICSs

As an ICS is a cyber-physical system [15], the process of cybersecurity risk propagation in ICSs is different from that in general network systems. Most ICS attacks aim to vandalize ICS assets, which include humans, environment, and equipment. To achieve a destructive purpose, attacks generally behave with part or all of the following five characteristics: 1) infiltrating the field network; 2) elevating the attacker's

privilege; 3) launching attacks to invalidate system functions; 4) causing hazardous incidents; and 5) leading to casualties, environment pollution, and other damages.

Modelling of cybersecurity risk propagation is critical for dynamic cybersecurity risk assessment in ICSs. Various models have been proposed for this purpose in recent years. Examples are BN, Petri net, fault tree, attack graph, and attack tree. However, most of these models are developed for cybersecurity analysis in general IT systems or for system safety analysis in ICSs. They do not cover all the above-mentioned five characteristics of ICS attacks.

To predict the propagation of cybersecurity risk for ICSs, a multi-level BN is proposed in literature [16]. It is equipped with multiple domain knowledge about attacks, system functions, hazardous incidents, and system assets. Therefore, a multi-level BN can be used to describe the whole cybersecurity risk propagation. It is effective for dynamical assessment of cybersecurity risks in ICSs.

### II-B A Brief Review of BN

A BN is a probabilistic graphical model to describe a set of random variables and their conditional dependencies via a directed acyclic graph (DAG) [17]. It is widely used in probabilistic estimation [18], fault diagnosis [19], system prediction [20], and pattern recognition [21]. A BN is defined as:

$$
\mathscr{B} \stackrel{\text { def }}{=}\left\langle\boldsymbol{x}, \boldsymbol{g}^{x \mapsto x}, \boldsymbol{p}\right\rangle,
$$

where

- $\boldsymbol{x}=\left(x_{1}, x_{2}, \cdots, x_{\ell(x)}\right)$ is a set of $\ell(x)$ nodes in total.
- $\boldsymbol{g}^{x \mapsto x}$ is an $\ell(x) \times \ell(x)$ incidence matrix that describes the relationship between the nodes, it is expressed as:

$$
\boldsymbol{g}^{x \mapsto x}=\left(\begin{array}{cccc}
x_{1} & x_{2} & \cdots & x_{\ell(x)} \\
g_{1,1} & g_{1,2} & \cdots & g_{1, \ell(x)} \\
g_{2,1} & g_{2,2} & \cdots & g_{2, \ell(x)} \\
\vdots & \vdots & \ddots & \vdots \\
g_{\ell(x), 1} & g_{\ell(x), 2} & \cdots & g_{\ell(x), \ell(x)}
\end{array}\right) x_{1}
$$

The definition of incidence matrix element $g_{i, j}$ is:

$$
g_{i, j}=\left\{\begin{array}{ll}
1, & \text { node } x_{i} \text { is the parent of node } m_{j} \\
0, & \text { otherwise. }
\end{array}\right.
$$

- $\boldsymbol{p}=\left(\boldsymbol{p}_{1}, \boldsymbol{p}_{2}, \cdots, \boldsymbol{p}_{\ell(x)}\right)$ is a set of conditional probability tables, $\boldsymbol{p}_{i}$ is the conditional probability table of node $x_{i}$.
Common methods for exact inference in BN are: variable elimination [22], clique tree propagation [23], and recursive conditioning and AND/OR search [24]. The complexity of these methods increases exponentially with the tree width of the network. The most commonly used approximate inference algorithms are importance sampling [25], stochastic Markov $\cdot$ chain Monte Carlo (MCMC) simulation [26], mini-bucket elimination [27], and loopy belief propagation [28].

The set $\boldsymbol{p}$ is generally obtained from statistics and analysis of big historical data [23], [29]. But for ICSs, the amount
of historical data about cyberattacks is too small to be used for estimation of conditional probability table. In this paper, a fuzzy conditional probability table is employed, which is easy to obtain from a group of experts.

## III. Architecture of our Fuzzy Approach for Dynamic Cybersecurity Risk Assessment

The architecture of our FPBN approach for dynamic cybersecurity risk assessment in ICSs is shown in Fig. 1.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Architecture of our FPBN approach for dynamic cybersecurity risk assessment in ICSs

In the architecture of our approach, there are two types of input data: attack evidence and anomaly evidence. The attack evidence data are from intrusion detection system, while the anomaly evidence data are from anomaly detection system. Cyberattacks and system faults can both generate anomaly evidence. System faults can lead to the error of risk assessment. Therefore, to ensure that there is no noise evidence caused by system faults, attack evidence and the anomaly evidence should be filtered first.

The FPBN is designed with multi-domain knowledge about attacks, system functions, hazardous incidents, and system assets. In our FPBN, crisp conditional probabilities, which are difficult to obtain, are replaced by fuzzy conditional probabilities. When the FPBN inference engine receives evidence, it calculates posterior probabilities that assets are damaged with the FPBN. Then, it assesses the dynamic cybersecurity risk with the losses of assets. The symbol " $\times$ " means that cyber security risk value is equal to the product of asset losses and the corresponding probabilities. Detailed system modelling and risk assessment will be developed in the next two sections.

## IV. Fuzzy Probability Bayesian Network

## A. Modelling of FPBN

As an extension to BN, a multi-level BN is an effective tool for risk assessment of ICSs [12], It is defined as:

$$
\mathscr{B} \stackrel{\text { def }}{=}\left\langle\boldsymbol{x}, \boldsymbol{g}^{x \mapsto x}, \boldsymbol{p}, \boldsymbol{v}\right\rangle
$$

where
$\boldsymbol{x}=\left(x_{1}, x_{2}, \cdots, x_{\ell(x)}\right)$ is a set of nodes, $x_{i}$ represents an ICS event with three states T (true), F (false) and U (unknown):

$$
x_{i}= \begin{cases}\mathrm{T}, & \text { event of node } x_{i} \text { happens } \\ \mathrm{F}, & \text { event of node } x_{i} \text { does not happen } \\ \mathrm{U}, & \text { unknown. }\end{cases}
$$

There are four types of nodes in the BN $\mathscr{B}$ : attack node $a$, function node $f$, incident node $e$, and asset node $z$. The event of an attack node means that an attacker launches an attack $a$. The event of a function node indicates that the system function $f$ fails. The event of an incident node implies a that a hazardous incident $e$ happens. The event of an asset node marks a damage of the asset $z$.

- $\boldsymbol{g}^{x \mapsto x}$ is an $\ell(x) \times \ell(x)$ incidence matrix. It describes the relationship between the nodes.
- $\boldsymbol{p}=\left(\boldsymbol{p}_{1}, \boldsymbol{p}_{2}, \cdots, \boldsymbol{p}_{\ell(x)}\right)$ is a set of conditional probability tables.
- $\boldsymbol{v}=\left(v_{1}, v_{2}, \cdots, v_{\ell(x)}\right)$ is a set of loss, $v_{i}$ is the loss of node $x_{i}$. If $x_{i}$ is an asset node, the loss $v_{i}$ is the value of that asset; otherwise $v_{i}=0$. There are three types of assets in ICSs: humans, environment, and properties. The quantification of these assets is introduced in literature [12].

As mentioned earlier, the crisp conditional probability table is difficult to estimate from limited historical data. To deal with this problem, this paper introduces an FPBN as follows:

$$
\tilde{\mathscr{B}} \stackrel{\text { def }}{=}\left\langle\boldsymbol{x}, \boldsymbol{g}^{x \mapsto x}, \tilde{\boldsymbol{p}}, \boldsymbol{v}\right\rangle
$$

where $\tilde{\boldsymbol{p}}=\left(\tilde{p}_{1}, \tilde{p}_{2}, \cdots, \tilde{p}_{\ell(x)}\right)$ is a set of conditional probability tables, and $\tilde{p}_{i}$ is the fuzzy conditional probability table of node $x_{i}$.

Our modelling of an FPBN is similar to that of a traditional BN. However, we estimate the fuzzy conditional probability table differently. Our method consists of three steps as described below.

Step 1: Establish a group of linguistic probabilities. Linguistic probabilities are words to describe the probabilities, such as "certain", "more probable", "less probable" and "impossible" [30], [31]. Each linguistic probability corresponds to a fuzzy number $\in[0,1]$. Fig. 2 shows fuzzy numbers of some linguistic probabilities.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Some fuzzy numbers of linguistic probabilities.
Step 2: Build an expert team. The experts are chosen from the cybersecurity or control engineering field. They define the meanings of the nodes and the fuzzy probabilities in the FPBN. With consideration of time resource and cost, a team of not less than 10 is suggested.

Step 3: Obtain the conditional probability from a constrained optimization. Assume that there are $\ell(p)$ linguistic probabilities $\tilde{p}_{1}, \tilde{p}_{2}, \cdots, \tilde{p}_{\ell(p)}$, and an experts team. If there are $\kappa_{i}$ experts select linguistic probability $\tilde{p}_{i}$ to describe the conditional probability $\tilde{p}(u)$, then $\tilde{p}(u)$ can be calculated by:

$$
\begin{gathered}
\tilde{p}(u)=\sup \min \left(\tilde{p}_{1}\left(u_{1}\right), \tilde{p}_{2}\left(u_{2}\right), \cdots, \tilde{p}_{\ell(p)}\left(u_{\ell(p)}\right)\right) \\
\text { s.t. } \quad \sum_{i=i}^{\ell(p)} \kappa_{i} u_{i}=\sum_{i=1}^{\ell(p)} \kappa_{i} u, \quad \sum_{i=i}^{\ell(p)} u_{i}=1
\end{gathered}
$$

where $\sup (\cdot)$ refers to the least upper bound of a partially ordered set. In Equation (7), the fuzzy probability $\tilde{p}_{i}\left(u_{i}\right)$ is
expressed as a function of $u_{i}$. When $u$ is confirmed, $\tilde{p}(u)$ can be obtained from an optimization problem subject to $\sum_{i=i}^{\ell(p)} \kappa_{i} u_{i}=\sum_{i=1}^{\ell(p)} \kappa_{i} u$ and $\sum_{i=i}^{\ell(p)} u_{i}=1$. When $u \in[0,1]$ changes, the solution of this optimization $\tilde{p}(u)$ varies.

## B. Inference of FPBN

Let $x$ denote a node in FPBN $\tilde{\mathscr{B}}$. Its parent node set is " $\boldsymbol{x}=\left\{" x_{1}, " x_{2}, \cdots, " x_{m}\right\}$. Its child node set is $\boldsymbol{x}^{*}=$ $\left\{x_{1}^{*}, x_{2}^{*}, \cdots, x_{n}^{*}\right\}$. At the $(t+1)$ th iteration, the message that $x$ passes to its parent node " $x_{i}$ is:

$$
\left(\begin{array}{c}
\lambda_{i}^{(t+1)}\left(" x_{i}=\mathbb{F}\right) \\
\lambda_{i}^{(t+1)}\left(" x_{i}=\mathbb{T}\right)
\end{array}\right)=\beta\left(\begin{array}{c}
\sum_{x} \lambda_{x}(x) \prod_{j} \lambda_{x_{j}^{(1)}}^{(\mathrm{t})}(x) \sum_{\boldsymbol{x}_{i}} p(x) " \boldsymbol{x}_{i}, " x_{i}=\mathbb{F}) \prod_{k \neq i} \pi_{i}^{(t)}\left(" x_{k}\right) \\
\sum_{x} \lambda_{x}(x) \prod_{j} \lambda_{x_{j}^{(1)}}^{(\mathrm{t})}(x) \sum_{\boldsymbol{x}_{i}} p(x) " \boldsymbol{x}_{i}, " x_{i}=\mathbb{T}) \prod_{k \neq i} \pi_{i}^{(t)}\left(" x_{k}\right)
\end{array}\right)
$$

where " $\boldsymbol{x}_{i}={ }^{*} \boldsymbol{x} \backslash\{" x_{i}\}$, and the operator " $\backslash$ " refers to set subtraction. The message that $x$ sends to its child node $x_{j}^{*}$ is:

$$
\left(\begin{array}{c}
\lambda_{x_{j}^{(t+1)}}^{(\mathrm{t}+1)}(x=\mathbb{F}) \\
\pi_{x_{j}^{(t+1)}}^{(\mathrm{t}+1)}(x=\mathbb{T})
\end{array}\right)=\beta\left(\begin{array}{c}
\lambda_{x}(x=\mathbb{F}) \prod_{k \neq j} \lambda_{x_{k}^{(1)}}^{(\mathrm{t})}(x=\mathbb{F}) \sum_{\boldsymbol{x}} p(x=\mathbb{F}) " \boldsymbol{x}) \prod_{k} \pi_{x}^{(t)}\left(" x_{k}\right) \\
\lambda_{x}(x=\mathbb{T}) \prod_{k \neq j} \lambda_{x_{k}^{(1)}}^{(\mathrm{t})}(x=\mathbb{T}) \sum_{\boldsymbol{x}} p(x=\mathbb{T}) " \boldsymbol{x}) \prod_{k} \pi_{x}^{(t)}\left(" x_{k}\right)
\end{array}\right)
$$

Equations (8) and (9) are derived from literature [28]. The symbol " $\sum_{\boldsymbol{x}}$ " is a summation operator over all possible states of " $\boldsymbol{x}$. For example,

$$
\begin{aligned}
\sum_{x_{1} x_{2}} p\left(x_{1}\right) p\left(x_{2}\right) & =p\left(x_{1}=\mathbb{F}\right) p\left(x_{2}=\mathbb{F}\right)+p\left(x_{1}=\mathbb{F}\right) p\left(x_{2}=\mathbb{T}\right) \\
& +p\left(x_{1}=\mathbb{T}\right) p\left(x_{2}=\mathbb{F}\right)+p\left(x_{1}=\mathbb{T}\right) p\left(x_{2}=\mathbb{T}\right)
\end{aligned}
$$

In Equations (8) and (9), $\beta$ is a normalization operator. For two fuzzy possibilities $\tilde{p}_{1}$ and $\tilde{p}_{2}, \beta\left(\tilde{p}_{1}, \tilde{p}_{2}\right)^{\top}$ is defined as:

$$
\beta\binom{\tilde{p}_{1}}{\tilde{p}_{2}}=\left(\begin{array}{c}
\bigcup_{\alpha \in[0,1]} \alpha\left(\left[\frac{\tilde{L}_{1}^{-1}(\alpha)}{L_{1}^{-1}(\alpha)+R_{2}^{-1}(\alpha)} \cdot \frac{\tilde{R}_{1}^{-1}(\alpha)}{R_{1}^{-1}(\alpha)+L_{2}^{-1}(\alpha)}\right]\right) \\
\bigcup_{\alpha \in[0,1]} \alpha\left(\left[\frac{\tilde{L}_{2}^{-1}(\alpha)}{L_{2}^{-1}(\alpha)+R_{1}^{-1}(\alpha)} \cdot \frac{\tilde{R}_{2}^{-1}(\alpha)}{R_{2}^{-1}(\alpha)+L_{1}^{-1}(\alpha)}\right]\right)
\end{array}\right)
$$

where $\alpha=\tilde{L}(u)$ is a monotonically increasing function, its inverse function is $\tilde{L}^{-1}(u), \alpha=\tilde{R}(u)$ is a monotonically decreasing function, its inverse function is $\tilde{R}^{-1}(u)$. They form the membership function of fuzzy probability $\tilde{p}$, which is shown in equation (11).

$$
\tilde{p}(u)= \begin{cases}\tilde{L}(u), & u \in[0, \underline{u}) \\ 1, & u \in[\underline{u}, \tilde{u}] \\ \tilde{R}(u), & u \in(\tilde{u}, 1]\end{cases}
$$

In Equation (10), the $\alpha$-cuts is another expression method of fuzzy probability. For example,

$$
\bigcup_{\alpha \in[0,1]} \alpha\left(\left[\frac{3 \alpha+2}{10}, \frac{8-3 \alpha}{10}\right]\right)= \begin{cases}\frac{10 u-2}{3}, & 0.2<u \leq 0.5 \\ \frac{8-10 u}{3}, & 0.5<u \leq 0.8 \\ 0, & \text { otherwise }\end{cases}
$$

The relationship between these two kinds of expression methods is shown in Fig. 3.

In Equations (8) and (9), the function $\lambda_{x}(\cdot)$ is the message that the node $x$ sends to itself. It is expressed as:

$$
\begin{aligned}
& \lambda_{x}(x=\mathbb{F})= \begin{cases}0, & \text { when } x \in \boldsymbol{E}, \text { and its observed value is } \mathbb{T}, \\
1, & \text { otherwise. }\end{cases} \\
& \lambda_{x}(x=\mathbb{T})= \begin{cases}0, & \text { when } x \in \boldsymbol{E}, \text { and its observed value is } \mathbb{F}, \\
1, & \text { otherwise. }\end{cases}
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3. The relationship between two expression methods.

where $\boldsymbol{E}$ is the evidence set of the ICS:

$$
\boldsymbol{E} \stackrel{\text { def }}{=} \{\boldsymbol{x} \mid \boldsymbol{x} \in \boldsymbol{x}, x \neq \mathbb{U}\}
$$

$\boldsymbol{E}$ can be obtained by analyzing the result of intrusion detection system and anomaly detection system.

After $t$ th iteration, the fuzzy belief of node $x$ becomes:

$$
\left(\begin{array}{c}
\operatorname{Bel}^{(t)}(x=\mathbb{F}) \\
\operatorname{Bel}^{(t)}(x=\mathbb{T})
\end{array}\right)=\beta\left(\begin{array}{c}
\lambda^{(t)}(x=\mathbb{F}) \cdot \pi^{(t)}(x=\mathbb{F}) \\
\lambda^{(t)}(x=\mathbb{T}) \cdot \pi^{(t)}(x=\mathbb{T})
\end{array}\right)
$$

where

$$
\left(\begin{array}{c}
\lambda^{(t)}(x=\mathbb{F}) \\
\lambda^{(t)}(x=\mathbb{T})
\end{array}\right)=\left(\begin{array}{c}
\lambda_{x}(x=\mathbb{F}) \prod_{i} \lambda_{x_{i}^{(t)}}^{(t)}(x=\mathbb{F}) \\
\lambda_{x}(x=\mathbb{T}) \prod_{i} \lambda_{x_{i}^{(t)}}^{(t)}(x=\mathbb{T})
\end{array}\right)
$$

and

$$
\left(\begin{array}{c}
\pi^{(t)}(x=\mathbb{F}) \\
\pi^{(t)}(x=\mathbb{T})
\end{array}\right)=\left(\begin{array}{c}
\sum_{x} P\left(x=\mathbb{F} \mid^{*} \boldsymbol{x}\right) \prod_{k} \pi_{x}^{(t)}\left({ }^{*} x_{k}\right) \\
\sum_{x} P\left(x=\mathbb{T} \mid^{*} \boldsymbol{x}\right) \prod_{k} \pi_{x}^{(t)}\left({ }^{*} x_{k}\right)
\end{array}\right)
$$

The iteration will terminate when it reaches the pre-specified iteration limit $t_{\max }$, i.e.,

$$
t \geq t_{\max }
$$

or achieves the pre-defined accuracy threshold $D_{\min }$, i.e.,

$$
\forall x \in \mathscr{B}, \quad\left|\operatorname{Bel}^{(t)}(x=\mathbb{T})-\operatorname{Bel}^{(t-1)}(x=\mathbb{T})\right| \leq D_{\min }
$$

It is worth mentioning that, for the BN with fuzzy probabilities, the beliefs $\operatorname{Bel}^{(t)}(x=\mathbb{T})$ and $\operatorname{Bel}^{(t-1)}(x=\mathbb{T})$ are fuzzy numbers. The distance between $\operatorname{Bel}^{(t)}(x=\mathbb{T})$ and $\operatorname{Bel}^{(t-1)}(x=\mathbb{T})$ can be calculated by [32], [33]:

$$
\begin{aligned}
& \left|\operatorname{Bel}^{(t)}(x=\mathbb{T})-\operatorname{Bel}^{(t-1)}(x=\mathbb{T})\right| \\
= & \int_{0}^{1}\left|\operatorname{Bel}^{(t)}(x=\mathbb{T})(u)-\operatorname{Bel}^{(t-1)}(x=\mathbb{T})(u)\right| \mathrm{d} u
\end{aligned}
$$

When the iteration terminates, $\operatorname{Bel}^{(t)}(x)$ is considered to be an approximation of the posterior fuzzy probability of node $x$ under the evidence set $\boldsymbol{E}$, i.e.,

$$
\tilde{p}(x=T \mid \boldsymbol{E}) \approx \operatorname{Bel}^{(t)}(x=T)
$$

For tree-structured FPBNs, this iteration process can be used to efficiently perform exact marginalization in a finite number of iterations. However, for loopy FPBNs, the sequence of messages defined by equations (8) and (9) is not guaranteed to converge to a fixed point after some iterations [34]. Therefore, Equation (18) is used as a time-out termination condition.

## V. DYNAMIC RISK ASSESSMENT

Cybersecurity risk of an ICS is calculated from the evidence set $\boldsymbol{E}$. A successful detection of an intrusion or anomaly leads to a change in the evidence set $\boldsymbol{E}$. Therefore, dynamic risk assessment is required for cybersecurity protection.

As mentioned earlier, noise evidence caused by system faults will lead to incorrect cybersecurity risk assessment. Therefore, the first step of risk assessment is to filter out the noise evidence from the evidence set $\boldsymbol{E}$.

For evidence set $\boldsymbol{E}$ and $\operatorname{FPBN} \mathscr{B}=\left\langle\boldsymbol{x}, \boldsymbol{g}^{x \mapsto x}, \hat{\boldsymbol{p}}, \boldsymbol{v}\right\rangle$, a confidence index $C(x=\mathbb{T})$ is proposed in this paper to describe the confidence degree of node $x \in \boldsymbol{x}$. It refers to a function node or incident node. The confidence index $C(x=\mathbb{T})$ is defined as:

$$
C(x=\mathbb{T})=\max _{\bar{a} \in \bar{\alpha}}\left(\prod_{a_{i} \in \bar{a}, a_{i}=\mathbb{T}} \eta_{i}\right)
$$

where $\bar{a}$ is an attack path of node $x, \bar{\alpha}$ is the attack path set of node $x, a_{i}$ is an attack node, $\eta_{i}$ is the false negative rate of intrusion detection system for attack $a_{i}$. Algorithm 1 shows how to get the attack path set $\bar{\alpha}$ of node $x$.

```
Algorithm 1: \(\operatorname{GetPathSet}(x, \mathscr{B})\) ). Output: attack path set \(\bar{\alpha}\)
1 Initialization: \(\bar{\alpha} \leftarrow \varnothing\) (empty);
2 if \(* \boldsymbol{x}\) is not empty then
3 foreach \(* x \in * \boldsymbol{x}\) do
4 \(\quad \bar{\alpha}^{\prime} \leftarrow \operatorname{GetPathSet}\left({ }^{*} x, \mathscr{B}\right)\);
5 foreach \(\hat{a} \in \hat{\alpha}^{\prime}\) do
6
7 else
8 \(\leftarrow\) Add \(\{x\}\) into \(\bar{\alpha}\);
```

If the value of the confidence index of evidence $x=\mathbb{T}$ is smaller the threshold $C_{\min }$, this evidence is considered to be caused by system faults, and thus should be removed from the evidence set $\boldsymbol{E}$. After noise evidence is filtered out from $\boldsymbol{E}$, the evidence set becomes $\boldsymbol{E}^{\prime}$. $\boldsymbol{E}^{\prime}$ is sent to the FPBN inference engine. The probabilities of all nodes in the FPBN are calculated accordingly. Then, the cybersecurity risk is assessed from:

$$
\hat{\mathscr{R}}=\sum_{i=1}^{\ell(x)} \tilde{p}\left(x_{i} \mid \boldsymbol{E}^{\prime}\right) \cdot v_{i}
$$

where $x_{i}$ is a node in theBN of ICSs, $\tilde{p}\left(z \mid \boldsymbol{E}^{\prime}\right)$ is the probability that node $x$ happens under the observed evidence set $\boldsymbol{E}^{\prime}$, and $v_{i}$ is the loss of the node $x_{i}$.

## VI. SIMULATION EXPERIMENTS

This section conducts simulation studies to demonstrate our approach [resented in this paper. The simulated control system is for control of a chemical reactor. Chemical reactors are widely used in process industries. Their safe operations are significant. Hazardous incidents of chemical reactors, such as explosion and toxic substance leaks, may cause casualties and environmental pollution, and thus must be avoided.

### V-A Experiment Setup

Fig. 4 shows a continuous stirred-tank reactor and its control system. The control system consists of supervisory control in an Ethernet network environment and PLC control in two CANBUS subnets. The Ethernet network interconnects the control system with the enterprise network via a commercial gateway. In this network, there are two hosts: a data server (DS) and an engineer station (ES). The DS is used for collecting the real-time control data and providing data service for the enterprise network. The ES is employed to program and configure the six PLCs.

The six PLCs are separated into two CANBUS subnets. PLC1 is the controller of feeding valves V1 and V2. PLC2 is exploited for collecting data from pressure, liquid level, and temperature sensors. PLC3 and PLC4 control the impeller and heater, respectively. The relief valve V4 is controlled by PLC5. PLC6 is responsible for control of discharging valve V3.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Networked control of continuous stirred-tank reactor.

An FPBN of this chemical reactor control system is shown in Fig. 5. This BN model and our fuzzy probability Bayesian inference engine are implemented with C++ language programmed in Microsoft Visual Studio 2015.

Four case studies are carried out: 1) the effectiveness of our risk assessment approach; 2) the effectiveness of our noise filter; 3) the execution time performance of our approach; and 4) the scalability of our approach with respect to the problem size characterized by the number of nodes.

![img-4.jpeg](img-4.jpeg)

### Legend


Fig. 5. FPBN for the reactor control system.

### V-B Case Study 1: Effectiveness of our Risk Assessment

To demonstrate the ability of our approach in dynamic risk assessment, multi-step attacks to the control system are

simulated. From 49 min to 81 min , the attacker scans the Ethernet network. From 90 min to 142 min , the attacker scans the vulnerabilities of the devices in the Ethernet. From 163 min to 204 min , the attacker launches a DoS attack to the DS. A full list of attacks and system faults are shown in Table I.

TABLE I
EVIDENCE EVENTS


Fig. 6 shows the curve of dynamic cybersecurity risk from the 1 st minute to the 498th minute. The $y$-coordinate is the value of risk, which is a fuzzy number with unit of U.S. dollar. The color is used to describe the degree of confidence. Blue indicates that the degree of confidence is 0 , while red means that the degree of confidence is 1 . The curve in black is the most likely risk whose degree of confidence is equal to 1 .

It is seen from Fig. 6 that the cybersecurity risk increases as the attacker gradually launches those attacks. When an attack is suspended or the invalid function is recovered, the cybersecurity risk decreases. The key values of cybersecurity risk are shown in Fig. 7.

## C. Case Study 2: Effectiveness of our Noise Filter

Noise evidence will lead to an increase in the number of iterations of the inference algorithm if no noise filter is employed. In the BN shown in Fig. 8, the nodes in red are observed pieces of evidence. If each of the other nodes is a new evidence, then judge whether the new evidence is a noise evidence. If Yes, draw it with black; otherwise draw it with green. The parameter $\tau$ in each evidence is the number of iterations of the inference algorithm if no noise filter is applied. Our simulation shows that the numbers of iterations in the presence of noise evidence are mostly larger than those in the absence of noise evidence.

To demonstrate the effectiveness of our noise filtering, a scenario shown in Fig. 9 is simulated. In Fig. 9, $\boldsymbol{E}$ is the evidence sequence shown in Table I. $\boldsymbol{E}^{\prime}$ is the evidence sequence $\boldsymbol{E}$ together with added noise evidence. The symbol $\boldsymbol{E}^{\prime \prime}$ is the evidence sequence derived from the noise filter. The noise invalidation of functions caused by system faults is designed as following. From the 45th minute to the 56th minute, the system function $f_{10}$ fails. From the 340th minute to the 361 st minute, the system function $f_{6}$ fails.

Other simulation settings are as follows. The maximum number of iterations is $t_{\max }=100$. The accuracy $D_{\min }=$ $1 \times 10^{-4}$. The inference process is repeated 5,000 times. For each inference of BN, a stochastic evidence set is generated and sent to the fuzzy probability Bayesian inference engine.

All simulations are conducted on computer with Intel Pentium processor G3220 (3M Cache, 3.00GHz) and 4GB DDR3 memory.

In our simulation, the fuzzy probability Bayesian inference engine receives evidence sequences $\boldsymbol{E}, \boldsymbol{E}^{\prime}$ and $\boldsymbol{E}^{\prime \prime}$. Then, it generates three risk curves $\mathscr{R}, \mathscr{R}^{\prime}$ and $\mathscr{R}^{\prime \prime}$ with these evidence sequences $\boldsymbol{E}, \boldsymbol{E}^{\prime}$, and $\boldsymbol{E}^{\prime \prime}$, respectively. After that, two Hamming distances $D(\mathscr{R}^{\prime}, \mathscr{R})$ and $D(\mathscr{R}^{\prime \prime}, \mathscr{R})$ are recorded as shown in Fig. 10.

Filtering out noises, the noise filter helps improve the convergence of the fuzzy probability Bayesian inference algorithm. This is due to the noise-induced increase in the number of iterations in the inference algorithm if the noise is not filtered out. To demonstrate this claim, 5,000 attack scenarios are generated stochastically according to the BN shown in Fig. 5. Then, stochastic noises are added to each evidence sequence. These 5,000 evidence sequences without noise and 5,000 evidence sequences with noise are sent to the fuzzy probability Bayesian inference engine. Simulation results show that in the presence of noise, the number of nonconvergence is 493 if the noise is not filtered out. In comparison, in the absence of noise, the number of nonconvergence is reduced to 269 , indicating a $45 \%$ drop.

The effectiveness of our noise filter is shown in the plot of Hamming Distances in Fig. 10. It is seen from Fig. 10 that $D(\mathscr{R}^{\prime}, \mathscr{R})$ has two disturbances: one from the 45 th minute to the 56 th minute, and the other from the 340 th minute to the 361 st minute. The maximum distance between $\mathscr{R}^{\prime}$ and $\mathscr{R}$ is $1.660 \cdot 10^{6}$. This means that if the noise filter is not applied, the value of the cybersecurity risk will be disturbed by the noises caused by system faults. It is also observed that the curve of the Hamming distance $D\left(\mathscr{R}^{\prime \prime}, \mathscr{R}\right)$ is always 0 . This confirms that with the noise filter, the risk error caused by noise evidence events is eliminated.

It is worth mentioning that a noise filter should be used with caution as it may filter out useful information. Assume that an attacker utilizes a zero-day vulnerability to launch a new attack, and the attack is missed out by the intrusion detection system. The result is that the anomaly evidence caused by this attack may be filtered out by the noise filter. Being too sensitive may cause some false actions, while being too robust may reduce its functionality as a noise filter. Therefore, a tradeoff is required between the sensitivity and robustness to noises by adjusting the parameter $C_{\min }$.

## D. Case Study 3: Execution Time of our Approach

To demonstrate the execution time performance of our approach, all execution times of the 5,000 simulation runs are recorded. Their distribution is shown in the histogram plot in Fig. 11. A quantitative analysis is carried out for Fig. 11. It shows that the minimum, maximum and average execution times are $0.242 \mathrm{~s}, 3.074 \mathrm{~s}$ and 0.648 s , respectively. The execution time performance is acceptable to a wide range of industrial process control systems. It can be well controlled by two parameters: the maximum number $t_{\max }$ of iterations, and the accuracy threshold $D_{\min }$.

![img-5.jpeg](img-5.jpeg)

Fig. 6. The Curve of dynamic cybersecurity risk.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Key values of dynamic cybersecurity risk.

### *E. Case Study 4: Scalability of our Approach*

To show the scalability of our approach, simulations are carried out to measure possible lower and upper bounds of the execution time performance under different problem sizes, which are characterized by the number of nodes. For this purpose, 25 FPBNs are simulated. The minimum and maximum problem sizes are 10 and 490, respectively. For each FPBN, the risk assessment is repeated for 200 runs. Fig. 12

![img-7.jpeg](img-7.jpeg)

Fig. 8. The number of iterations when the noise filter is not used.

shows the measured upper and lower bounds together with the best fitting line of average execution time performance.

In Fig. 12, the best fitting line has the form *t* = 0.0080201× *ℓ*(*m*) + 0.01467 with the correlation coefficient *r* = 0.99968.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Simulation of our noise filter.

![img-9.jpeg](img-9.jpeg)

Fig. 10. The curves of Hamming distances.

![img-10.jpeg](img-10.jpeg)

Fig. 11. The distribution of execution times from 5,000 runs.

This means that the average execution time increases linearly with the increase of the problem size, indicating good scalability of our risk assessment approach. For 490 nodes, the maximum execution time of the FPBN is 4.90s in our simulation environment.

![img-11.jpeg](img-11.jpeg)

Fig. 12. Execution time performance of our approach under different problem sizes each with 200 runs.

### *F. A Comparison of Various Approaches*

Requirements for cybersecurity risk assessment change from a system to another, or from a scenario to another. Therefore, a variety of risk assessment approaches have been developed for different scenarios or applications. A direct comparison of these approaches is unfair for a particular scenario. Instead, a comparison of the differences among these approaches will give some insights into the functionality and features of the approaches. Table II provides such a comparison of our approach and existing approaches. It is seen from Table II that our approach has more features than any other existing approaches from literature.

**TABLE II: A COMPARISON OF OUR APPROACH AND EXISTING APPROACHES.**


### VII. CONCLUSION

Dynamic assessment of cybersecurity risks plays a vital role in cybersecurity protection of ICSs. Due to the lack of historical data in ICSs, building a risk propagation model is difficult for risk assessment. To address this issue, an FPBN approach has been presented in this paper for dynamic assessment of cybersecurity risks in ICSs. It starts with establishment of an FPBN. To overcome the difficulty of limited historical data, fuzzy probabilities have been used in our approach to replace crisp probabilities used in standard BN. Then, an approximate dynamic inference algorithm has been designed for dynamic assessment of cybersecurity risks based on the established FPBN. It has been integrated with a noise evidence filter for removal of noise evidence caused by system faults. To demonstrate the effectiveness of our presented approach, experiments have been conducted on a simulation platform of a simplified chemical reactor. Our simulations of 5,000 runs for each scenario have shown a computation time of about 3 s for risk evaluation, indicating satisfaction of soft real-time control requirements of ICSs.
