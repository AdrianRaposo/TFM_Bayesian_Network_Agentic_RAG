# Body Schema Learning for Robotic Manipulators from Visual Self-Perception 

Jürgen Sturm ${ }^{a, a}$, Christian Plagemann ${ }^{b}$, Wolfram Burgard ${ }^{a}$<br>${ }^{a}$ University of Freiburg, Department of Computer Science, Georges-Köhler-Allee 79, 79110 Freiburg, Germany<br>\{sturm, burgard\}@informatik. uni-freiburg. de<br>${ }^{b}$ Stanford University, AI Lab, 353 Serra Mall, Stanford, CA 94305-9010, USA<br>plagemann@stanford. edu


#### Abstract

We present an approach to learning the kinematic model of a robotic manipulator arm from scratch using self-observation via a single monocular camera. We introduce a flexible model based on Bayesian networks that allows a robot to simultaneously identify its kinematic structure and to learn the geometrical relationships between its body parts as a function of the joint angles. Further, we show how the robot can monitor the prediction quality of its internal kinematic model and how to adapt it when its body changes - for example due to failure, repair, or material fatigue. In experiments carried out both on real and simulated robotic manipulators, we verified the validity of our approach for real-world problems such as end-effector pose prediction and end-effector pose control.


Key words: robotics, machine learning, self-perception, sensor-motor learning, body schema

[^0]
[^0]:    ${ }^{\text {a }}$ Corresponding author
    URL: http://www.informatik.uni-freiburg.de/ sturm (Jürgen Sturm)

# 1. Introduction 

Kinematic models are widely used in robotics, especially in the context of robotic manipulation (Craig, 1989; Choset et al., 2005). Such models are typically derived in an analytic way (Rosales and Gan, 2004), which relies heavily on prior knowledge about the geometry of the robot. When a model is then used on a real robotic manipulator, its geometrical parameters have to be calibrated carefully. In practice, this is done by the robot manufacturer using a highly accurate calibration chamber.

As robotic systems become more complex and versatile, especially when they are delivered in a completely reconfigurable way, there is a growing demand for techniques allowing a robot to automatically learn kinematic models with no or only minimal human intervention and without the need for costly calibration equipment. Clearly, such a capability would not only facilitate the deployment and calibration of new robotic systems but also allow for autonomous re-adaptation when the kinematic model changes, e.g., due to deformations of robot parts or due to material fatigue. Additionally, components of the robot might get exchanged or replaced by newer parts such that the system model no longer complies with the originally engineered one. Finally, to make intelligent use of tools, a robot would need to learn the kinematic properties of unknown tools to use them appropriately (Nabeshima et al., 2006).

In this article, we investigate how to equip robots with the ability to learn their kinematic models from scratch and how to adapt them over time using exploratory actions and self-perception. Figure 7 depicts the robotic manipulation system used to develop and test our approach and Fig. 7 shows

a visualization of its simulated counter-part. We propose to learn a Bayesian network for the kinematic structure of the robot including the forward and inverse models relating action commands and body pose. In contrast to prior work in this area, we jointly address (a) the combinatorial problem of assigning action signals and percepts to body parts and (b) the calibration problem for all the individual kinematic transformations. Figure 3 gives an overview of the proposed approach. We start with a fully connected network containing all perceivable body parts and the available action signals, perform random "motor babbling" and iteratively reduce the network complexity by analyzing the perceived body motion. At the same time, we learn Gaussian process regression models for all individual dependencies in the network, which can later be used to predict the body pose when no perception is available or to allow for gradient-based posture control.

Our approach addresses all of the following practical problems that frequently arise in robotic manipulation tasks in a single Bayesian framework:

- Pose prediction: Given the current joint configuration (i.e., the joint angles), compute the pose of the end-effector.
- Pose control: Conversely, given a target pose (a 6D configuration of the end-effector), compute the required joint angles that lead to that position.
- Model selection: Given a history of observed configuration-pose pairs, infer the structure of the kinematic function. In particular, this includes discovering the (in-)dependencies between the individual body parts and the joint signals.

- Model learning: After the kinematic structure of the robot has been identified, the geometrical relationships between the body parts of the robot can be learned from the history of observed configuration-pose pairs. If parametrized models are used, this corresponds to parameter optimization given the observed data.
- Model testing: Given both a pose prediction and a pose observation, the robot estimates the quality of its internal model.
- Failure detection and model adaptation: When the kinematics of the robot change, e.g., when a joint gets blocked or is deformed, the robot detects such a change by model testing. Our approach can localize the mismatch within the kinematic function and trigger relearning only for the affected parts of the kinematic function.

The article is structured as follows. We start with a brief introduction of kinematic and inverse kinematic functions in robotics in Section 2. We will then introduce our Bayesian framework for representing robotic body schemas in Section 3, discuss failure awareness and life-long adaptation in Section 4, and present experimental results obtained with real and simulated manipulator arms in Section 5, which demonstrate that our approach is able to quickly learn compact and accurate models and to robustly deal with noisy observations. We finish the article with a discussion of related work.

# 2. The Kinematic Function and the Body Schema 

The kinematic model describes the relationship between the configuration of the robot, i.e., the joint angles, and the body posture, i.e., the positions

of the body parts in space. Figure 4 shows an example of a simple 2-DOF robotic manipulator. The robot consists of two rotary joints $a_{1}$ and $a_{2}$, and five body parts $\mathbf{X}_{1}, \ldots, \mathbf{X}_{5}$. The first two body parts are connected rigidly. This means that the geometric transformation $\boldsymbol{\Delta}_{1 \rightarrow 2}$ from the trunk $\mathbf{X}_{1}$ to the shoulder $\mathbf{X}_{2}$ is independent of the positions of the joints. The shoulder $\mathbf{X}_{2}$ and the upper arm $\mathbf{X}_{3}$ are connected by the shoulder joint $a_{1}$, and thus their geometric transformation $\boldsymbol{\Delta}_{2 \rightarrow 3}\left(a_{1}\right)$ depends on the joint angle of $a_{1}$. The same holds for the following parts, as the joint angle of the elbow joint $a_{2}$ has direct influence on the geometrical transformation $\boldsymbol{\Delta}_{3 \rightarrow 4}\left(a_{2}\right)$ between the upper arm $\mathbf{X}_{3}$ and the lower arm $\mathbf{X}_{4}$. The gripper $\mathbf{X}_{5}$ is attached rigidly to the lower arm $\mathbf{X}_{4}$, such that $\boldsymbol{\Delta}_{4 \rightarrow 5}$ is a fixed transformation. The kinematic function of this manipulator is defined by the concatenation of these individual transforms, i.e.,

$$
f\left(a_{1}, a_{2}\right):=\boldsymbol{\Delta}_{1 \rightarrow 2} \circ \boldsymbol{\Delta}_{2 \rightarrow 3}\left(a_{1}\right) \circ \boldsymbol{\Delta}_{3 \rightarrow 4}\left(a_{2}\right) \circ \boldsymbol{\Delta}_{4 \rightarrow 5}
$$

The kinematic function $f\left(a_{1}, a_{2}\right)$ describes the full geometrical transformation from the coordinate frame of the trunk to the coordinate frame of the gripper. In engineering, the kinematic function of a robotic manipulator is often constructed of the individual transformations by the specification of the Denavit-Hartenberg (DH) parameters (Sciavicco and Siciliano, 2000). For many robotic applications, it is necessary to compute the required joint angles $a_{1}, a_{2}$ given a target position in the workspace, requiring the inverse kinematic function $f^{-1}$. Note that as the algebraic inversion of a kinematic function $f$ is only possible for simple manipulators, a solution to the inverse kinematic problem is in practice often computed using an iterative numerical method, such as pseudo-inverse inverse kinematics (IK) or damped-least

squares IK (Buss and su Kim, 2005).
Probabilistic graphical models, like Bayesian networks, are an appealing tool to represent the dependencies between random variables in an intuitive way (Pearl, 1988; Jensen, 2001). A Bayesian network is a directed, acyclic graph consisting of nodes and edges. The nodes in the network correspond to the observed or latent random variables, and the edges (or lack of edges) between nodes stand for the conditional dependencies (or independencies, respectively) between two nodes. Note how the kinematic function of Eq. 1 has been translated into the Bayesian network depicted in Fig. 7: the poses of the body parts $\mathbf{X}_{1}, \ldots, \mathbf{X}_{5}$ and the actions $a_{1}, a_{2}$ appear as nodes in the network, and the kinematic structure is encoded as the topology of the network. Consider for example the pose of body part $\mathbf{X}_{2}$, that has only a single incoming edge originating from pose $\mathbf{X}_{1}$, meaning that the pose of $\mathbf{X}_{2}$ is fully defined after $\mathbf{X}_{1}$ has been observed. In contrast, the pose of $\mathbf{X}_{3}$ has incoming edges both from $\mathbf{X}_{2}$ and $a_{1}$, expressing its probabilistic dependency of both of its so-called parents. Bayesian networks can be used to infer the probability distributions of particular nodes in a variety of ways (Sudderth et al., 2003). In particular, it is possible with Bayesian networks to answer queries similar to those listed at the end of Section 1, for example predicting the pose of the end-effector (given $a_{1}, \ldots, a_{m}$, infer $\mathbf{X}_{n}$ ) or controlling the pose of the end-effector (given $\mathbf{X}_{n}$, infer $a_{1}, \ldots, a_{m}$ ).

# 3. A Bayesian Framework for Kinematic Chains 

We define a robotic body schema as the joint probability distribution of the available action signals $\left\langle a_{1}, \ldots, a_{m}\right\rangle$, the self-observations $\left\langle\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{n}\right\rangle$,

and the true poses of the body parts $\left\langle\mathbf{X}_{1}, \ldots, \mathbf{X}_{n}\right\rangle$. In our concrete scenario, in which we consider the body schema of a robotic manipulator arm in conjunction with a stationary, monocular camera, the action signals $a_{i} \in \mathbb{R}$ are real-valued variables corresponding to the latest joint angle request. Whereas the $\mathbf{X}_{i} \in \mathbb{R}^{6}$ encode the 6 -dimensional poses ( 3 D Cartesian position and 3 D orientation) of the body parts w.r.t. a reference coordinate frame, the $\mathbf{Y}_{i} \in \mathbb{R}^{6}$ are observations of the body parts-generally noisy and potentially missing. Throughout this article, we use capital, bold letters to denote the pose variables to highlight that these also uniquely define homogeneous transformation matrices, which can be concatenated and inverted.

Note that our approach does not require proprioception telling the robot how well joint $i$ has approached the requested target angle $a_{i}$. At first sight, it seems that with proprioception one could learn the kinematic function passively from visual and proprioceptive observations only. However, one would then lack the mapping from motor commands to proprioception, such that the learned model would not suffice for manipulator control. One would either need to assume that motors and proprioceptive sensors are calibrated precisely, or one would need to additionally learn the motor-proprioception mapping for each joint. Therefore, we propose to learn the mapping from motor commands to body pose observations directly using active exploration. In this way, our approach closes the action-perception-loop, as visualized in Fig. 3, and it obviates the need for additional calibration of the motor encoders.

Formally, we seek to learn the probability distribution

$$
p\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{n}, \mathbf{Y}_{1}, \ldots, \mathbf{Y}_{n} \mid a_{1}, \ldots, a_{m}\right)
$$

which in this form is intractable for all but the simplest scenarios. It is therefore typically assumed that each observation variable $\mathbf{Y}_{i}$ is independent from all other variables given the true configuration $\mathbf{X}_{i}$ of the corresponding body part and that they can thus be fully characterized by an observation model $p\left(\mathbf{Y}_{i} \mid \mathbf{X}_{i}\right)$. Furthermore, if the kinematic structure of the robot was known, a large number of pair-wise independencies between body parts and action signals could be assumed, which in turn would lead to the much simpler, factorized model

$$
p\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{n} \mid a_{1}, \ldots, a_{m}\right)=\prod_{i} p\left(\mathbf{X}_{i} \mid \operatorname{parents}\left(\mathbf{X}_{i}\right)\right)
$$

Here, parents $\left(\mathbf{X}_{i}\right)$ comprises all body parts and action variables that directly influence $\mathbf{X}_{i}$. Note, that the actions are given and, thus, do not depend on other variables in this model. We now make the factorized structure of the problem explicit by introducing (hidden) transformation variables $\boldsymbol{\Delta}_{i \rightarrow j}:=\mathbf{X}_{i}^{-1} \mathbf{X}_{j}$ for all pairs $\left\langle\mathbf{X}_{i}, \mathbf{X}_{j}\right\rangle$ of body parts. We represent the 6 D pose vectors $\mathbf{X}$ as their equivalent homogeneous transformation matrices, which means that $\boldsymbol{\Delta}_{i \rightarrow j}$ reflects the (deterministic) relative transformation between $\mathbf{X}_{i}$ and $\mathbf{X}_{j}$. Note that various parameterizations of such transformation matrices are possible (e.g., by means of the Euler angles, quaternions, or over-parametrized as the full 12D matrices) and that we thus assume a $d$-dimensional parametrization of $\boldsymbol{\Delta}_{i \rightarrow j}$.

Denoting with $\mathbf{Z}_{i \rightarrow j}:=\mathbf{Y}_{i}^{-1} \mathbf{Y}_{j}$ the transformation relating the observations $\mathbf{Y}_{i}$ and $\mathbf{Y}_{j}$ that correspond to $\mathbf{X}_{i}$ and $\mathbf{X}_{j}$, we define as a local model the subgraph of our network that defines the relationship between any two body parts $\mathbf{X}_{i}$ and $\mathbf{X}_{j}$ and their dependent variables, if all other body parts are ignored. Figure 7 shows a prototypical local model. Here, we denote

with $\mathcal{A}_{i \rightarrow j}$ the set of action variables that have a direct influence on $\boldsymbol{\Delta}_{i \rightarrow j}$. Any set of $(n-1)$ local models which forms a spanning tree over all $n$ body parts defines a model for the whole kinematic structure.

In the following, we explain (a) how to learn local models from data and (b) how to find the best spanning tree built from these local models that explains the whole robot. We consider the single best solution only and do not perform model averaging over possible alternative structures. Note that in theory, it would be straight-forward to keep multiple structure hypotheses and to average over them for prediction using Bayes' rule. Control under structure uncertainty, however, is a slightly more difficult problem. One would have to consider all possible structures and assess the individual risks and gains for alternative actions. Then, the one action sequence would be selected that maximizes the overall gain while keeping all possible risks low (Stachniss et al., 2005). In practice, we found that considering the mostlikely structure only is sufficient for most of the relevant tasks. Our approach is conservative in this respect since it requires a certain minimal accuracy from all parts of the body schema before the model is considered complete.

# 3.1. Local Models 

The local kinematic models are the central concept in our body schema framework. A local model $\mathcal{M}$ (see Fig. 7) describes the geometric relationship between two body parts $i$ and $j$ given a set of action signals $\mathcal{A}_{i \rightarrow j}$. We propose to learn this relationship from data samples acquired while performing random actions and observing their effects. As the learning framework for solving this supervised regression problem, we apply Gaussian processes for regression (Rasmussen and Williams, 2006). On the real robotic plat-

form used in our experiments, the action $a_{i}$ correspond to the target angle requested from joint $i$. The observations $\mathbf{Y}_{i}$ of part locations $\mathbf{X}_{i}$ are obtained by tracking visual markers in 6D space (including their 3D pose and 3D orientation (Fiala, 2004), see Fig. 7). Note that the $\mathbf{Y}_{i}$ 's are inherently noisy and that missing observations are common-for example in the case of (self-)occlusion.

Formally, the task is to learn the local transformations $\boldsymbol{\Delta}_{i \rightarrow j}$, each linking two body parts $\mathbf{X}_{i}$ and $\mathbf{X}_{j}$. Considering Fig. 7, a straight-forward approach would be to infer the true poses $\mathbf{X}_{i}$ and $\mathbf{X}_{j}$ from the noisy observations $\mathbf{Y}_{i}$ and $\mathbf{Y}_{j}$, for instance assuming Gaussian white noise on the observations, $\mathbf{Y}_{i} \sim \mathcal{N}\left(\mathbf{X}_{i}, \sigma_{\text {sensor }}^{2} \cdot \mathbf{I}_{d}\right)$. With $\mathbf{I}_{d}$ we denote the $d$-dimensional identity matrix and remind that $d$ denotes the chosen dimensionality of the parametrization of transformation matrices. In other terms, one would be following the full Bayesian pathway $\mathbf{Y}_{i} \leftarrow \mathbf{X}_{i} \rightarrow \boldsymbol{\Delta}_{i \rightarrow j} \rightarrow \mathbf{X}_{j} \rightarrow \mathbf{Y}_{j}$ to reason about $\boldsymbol{\Delta}_{i \rightarrow j}$.

However, since the absolute positions $\mathbf{X}_{i}$ are irrelevant for describing the relative transformations, we take a slightly different approach by concentrating on the transformations $\mathbf{Z}_{i \rightarrow j}$ between observations $\mathbf{Y}_{i}$ and $\mathbf{Y}_{j}$. We model $\mathbf{Z}_{i \rightarrow j} \sim \mathcal{N}\left(\boldsymbol{\Delta}_{i \rightarrow j}, \sigma_{\text {sensor-rel }}^{2} \cdot \mathbf{I}_{d}\right)$, and thus follow the shorter path $\left\{\mathbf{Y}_{i}, \mathbf{Y}_{j}\right\} \leftarrow \mathbf{Z}_{i \rightarrow j} \leftarrow \boldsymbol{\Delta}_{i \rightarrow j}$, which does not include the $\mathbf{X}_{i}$ explicitly. The problem of learning a single local model now has the form of the noisy regression problem, that is, learning the function

$$
\begin{aligned}
f_{\mathcal{M}}: \quad \mathbb{R}^{\left|\mathcal{A}_{i \rightarrow j}\right|} & \rightarrow \mathbb{R}^{d} \\
\mathcal{A}_{i \rightarrow j} & \mapsto \Delta_{i \rightarrow j}
\end{aligned}
$$

from noisy observations $\mathbf{Z}_{i \rightarrow j}$.

For simplicity, we consider over-parametrized transformation matrices in the following with $d=12$ independent components and learn the functional mapping for each component separately. Due to this simplification, we cannot guarantee that all predictions correspond to valid, homogeneous transformation matrices. In practice, however, they lie close to valid transformations, such that a normalization step (orthonormalizing the rotation part using singular value decomposition) resolves the problem. In the future, we might consider more efficient parameterizations that come closer to the actual 6DOF of the transformations.

For solving the regression problem as stated in Eq. 4, we place individual Gaussian process priors (Rasmussen and Williams, 2006) on the 12 variables of the transformation functions $f_{\mathcal{M}}$ for all local models $\mathcal{M}$ and choose the squared exponential covariance function to parametrize the process. Figures 8 and 9 shows the $x, y$, and $z$ components of two different local models learned from real data using the Gaussian process (GP) model. In the situation shown in Fig. 8, the action variable (x-axis) physically corresponds to the transformation being measured (y-axis). Thus, the data set is selfconsistent and accurate functions with low noise levels can be learned. The higher noise level for the $z$-component is due to larger measurement error in this direction (i.e. the camera's line of vision). In the situation depicted in Fig. 9, a local model has been learned for variables that do not have a direct physical relationship. As a result, the model shows high noise levels and it does not explain the data well. Such a local model is likely to be discarded during the search for the full body model, which is described in the following.

# 3.2. Learning a Factorized Full Body Model 

We seek to find a factorized model for the whole kinematic structure (see Eq. 3) that explains the observed data well and that is not overly complex-such that it can be learned and evaluated online. To limit complexity, we first discard all local models that are overly inconsistent with the observed data. We define a local model $\mathcal{M}$ to be valid given a set of observations $\mathcal{D}$, if and only if its prediction error is below some threshold $\theta$, i.e., $\epsilon_{\text {pred }}(\mathcal{D})<\theta$ that we will denote with the Boolean predicate $\operatorname{valid}_{\mathcal{M}}(\mathcal{D})$. Our experiments revealed that a good value for $\theta$ is $3 \sigma$, where $\sigma$ is the standard deviation of the sensor model. The prediction error $\epsilon_{\text {pred }}(\mathcal{D} \mid \mathcal{M})$ is defined as

$$
\epsilon_{\text {pred }}(\mathcal{D} \mid \mathcal{M}):=\frac{1}{|\mathcal{D}|} \sum_{\left(\mathbf{Z}_{i \rightarrow j}, \mathcal{A}_{i \rightarrow j}\right) \in \mathcal{D}} \epsilon_{\text {pred }}\left(\mathbf{Z}_{i \rightarrow j} \mid \mathcal{A}_{i \rightarrow j}, \mathcal{M}\right)
$$

with

$$
\epsilon_{\text {pred }}\left(\mathbf{Z}_{i \rightarrow j} \mid \mathcal{A}_{i \rightarrow j}, \mathcal{M}\right):=\frac{1}{d} \sqrt{\sum_{z \in \mathbf{Z}_{i \rightarrow j}}\left(z-\mu_{z}^{*}\right)^{2}}
$$

Here, $\mu_{z}^{*}$ is the mean prediction of component $z$ of transformation $\mathbf{Z}_{i \rightarrow j}$. Denoting with $C(\mathcal{M}) \in \mathbb{N}$ the dimensionality of model $\mathcal{M}$, that is, the number $\left|\mathcal{A}_{i \rightarrow j}\right|$ of action signals that the model depends on, we define a model quality measure $q(\mathcal{D} \mid \mathcal{M})$,

$$
\log q(\mathcal{D} \mid \mathcal{M})=\underbrace{\log \left[1 / \epsilon_{\text {pred }}(\mathcal{D} \mid \mathcal{M})\right]}_{\text {accuracy }}-\underbrace{C(\mathcal{M}) \log 1 / \theta}_{\text {complexity }}
$$

which is proportional to both the model accuracy and to a penalty term for model complexity. Note that quality measures such as the Bayesian information criterion (BIC) are not directly applicable here since Gaussian process

regression is a nonparametric method and, thus, there is no obvious number of parameters for representing the data sets. Note that the marginal data likelihood $p(\mathcal{D} \mid \mathcal{M})$, which is used to learn the parameters of the covariance function, might serve as an alternative model quality measure. However, since $q(\mathcal{D} \mid \mathcal{M})$ includes the model dimensionality explicitly-which makes it easy to order the search for local models by this criterion-we have used this measure in our experiments.

# 3.2.1. Finding the Network Topology 

If no prior knowledge about the body structure of the robot exists, we initialize a fully connected network model containing a total of $\sum_{k=0}^{m}\binom{n}{2}\binom{m}{k}$ local models (linking $m$ actions to $n$ transformations). Given a set of self observations, the robot can first eliminate those local models that are highly inconsistent with the data by evaluating $\operatorname{valid}_{\mathcal{M}}(\mathcal{D})$ as described above. The remaining set of valid models is typically still large (e.g., see Fig. 10). Certain ambiguities will, for instance, remain even after infinitely many training samples. If, for example, $p_{\mathcal{M}_{1}}\left(\mathbf{Z}_{1 \rightarrow 2} \mid a_{1}\right)$ has been determined to be a valid local model, then $p_{\mathcal{M}_{2}}\left(\mathbf{Z}_{1 \rightarrow 2} \mid a_{1}, a_{2}\right)$ will also be. Although these alternative models might not be distinguishable regarding prediction accuracy for $\mathbf{Z}_{1 \rightarrow 2}$, they differ significantly in their complexity and therefore in their model quality $q(\mathcal{D} \mid \mathcal{M})$.

To resolve such locally ambiguous situations and to also find the best topology on a global level, we seek to select the minimal subset $\mathbb{M} \subset \mathbb{M}_{\text {valid }}$ from the superset of all valid local models $\mathbb{M}_{\text {valid }}=\left\{\mathcal{M}_{1}, \ldots\right\}$ that covers all body part variables and simultaneously maximizes the overall model fit $q(\mathcal{D} \mid \mathbb{M}):=\prod_{\mathcal{M} \in \mathbb{M}} q(\mathcal{D} \mid \mathcal{M}) . \quad \mathbb{M}$ can be found efficiently by computing

the minimal spanning tree of $\mathbb{M}_{\text {valid }}$ taking the model quality measure of the individual local models as the cost function. For our purposes, the spanning tree needs to cover all body parts but not necessarily all action variables, since some of them might not have an influence on the robot.

To connect all $n$ body poses in the Bayesian network, exactly $|\mathbb{M}|=(n-1)$ local models need to be selected. This yields $\binom{\left|\mathbb{M}_{\text {valid }}\right|}{|\mathbb{M}|}$ possible network structures to be considered. In the typical case, where the robot is composed of 1-DOF joints (arbitrarily connected), this number reduces to the order of $O\left(n^{3}\right)$. Regarding the scalability to higher degrees of freedom and longer kinematic chains, the growth of the search space is of less practical importance than other factors like the observability of local transformations (from a given camera view point). In practice, straight-forward search heuristics allow us to strongly focus the search on the relevant parts of the structure space, further reducing this number. In our experiments, for instance, we searched by processing the lower dimensional models first. Recall that the quality measure $q(\mathcal{D} \mid \mathcal{M})$ for a local model is composed of the (data-dependent) prediction accuracy and a (data-independent) complexity penalty. If we consider two valid local models, i.e., with $\epsilon_{\text {pred }}\left(\mathcal{D} \mid \mathcal{M}_{1 \mid 2}\right)<\theta$, then by the definition of $q(\mathcal{D} \mid \mathcal{M})$, the quality of a model with lower complexity is always higher compared to a local model with higher complexity for any $\mathcal{D}$, i.e.,

$$
C\left(\mathcal{M}_{1}\right)<C\left(\mathcal{M}_{2}\right) \Longleftrightarrow \forall \mathcal{D}: q\left(\mathcal{D} \mid \mathcal{M}_{1}\right)>q\left(\mathcal{D} \mid \mathcal{M}_{2}\right)
$$

This is due to the fact that $C(\mathcal{M})$ contains the error threshold $\theta$ and that this is also the upper bound of all prediction errors $\epsilon_{\text {pred }}$ (see Eq. 6)-all models above this threshold are invalid and thus discarded. Due to Eq. 8, it

is sufficient to evaluate only the first $k$ complexity layers of local models in $\mathbb{M}_{\text {valid }}$ until a minimal spanning tree is found for the first time. This spanning tree then corresponds to the global maximum of overall model quality.

# 3.3. Prediction and Control 

Having discussed the learning of local models and the selection of the network structure, we now show how the resulting model can be used to predict the configuration of the robot for a given action signal (forward modeling) and how to select actions to achieve a given configuration (inverse modeling).

The kinematic forward model can be constructed directly from the local models contained in $\mathbb{M}$, since these form a tree over all body part variables $\mathbf{X}_{i}$. We can write

$$
\begin{aligned}
& p\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{n} \mid a_{1}, \ldots, a_{m}\right)=\prod_{i} p\left(\mathbf{X}_{i} \mid \operatorname{parents}\left(\mathbf{X}_{i}\right)\right) \\
& \quad=p\left(\mathbf{X}_{\text {root }}\right) \prod_{\mathcal{M}_{i \rightarrow j} \in \mathbb{M}} p_{\mathcal{M}_{i \rightarrow j}}\left(\Delta_{i \rightarrow j} \mid \mathcal{A}_{i \rightarrow j}\right) \\
& \quad=p\left(\mathbf{X}_{\text {root }}\right) \prod_{\mathcal{M}_{i \rightarrow j} \in \mathbb{M}} p_{\mathcal{M}_{i \rightarrow j}}\left(\mathbf{X}_{i}^{-1} \mathbf{X}_{j} \mid \mathcal{A}_{i \rightarrow j}\right)
\end{aligned}
$$

where $\mathbf{X}_{\text {root }}$ is the position of the robot trunk, which serves as the reference frame for all other body parts. We denoted with $\mathcal{M}_{i \rightarrow j}$ the local model of $\mathbb{M}$ which describes the transformation between $\mathbf{X}_{i}$ and $\mathbf{X}_{j}$. From $p\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{n} \mid a_{1}, \ldots, a_{m}\right)$ in the factorized form, we can now approximate the maximum likelihood (ML) estimate of the resulting body posture given an action signal by concatenating the geometric transformations of the individual geometric transformations. We may refer the interested reader to (Ware and Lad, 2003) how products of Gaussians can be approximated by a single Gaussian.

Although the inverse kinematic model can be derived by applying Bayes' rule in principle,

$$
\begin{aligned}
& p\left(a_{1}, \ldots, a_{m} \mid \mathbf{X}_{1}, \ldots, \mathbf{X}_{n}\right) \\
& \quad=\frac{p\left(a_{1}, \ldots, a_{m}\right)}{p\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{n}\right)} p\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{n} \mid a_{1}, \ldots, a_{m}\right)
\end{aligned}
$$

it is difficult in practice to determine the maximum likelihood (ML) solution for the action signal $a_{1}, \ldots, a_{m}$. This is due to the fact that the goal configuration is typically not fully specified for all body parts, but rather for the root part and the end-effector only. Thus, the Bayesian network is constrained at both "ends" only, which results in a high-dimensional optimization problem.

For this reason, we resort to a well-known iterative approach (termed differential kinematics in the literature) which applies small changes to the current action signal such that the body posture $\mathbf{X}_{1}, \ldots, \mathbf{X}_{n}$ approaches the target configuration. Since all individual functions $f_{\mathcal{M}_{i}}$ are continuous, and so is the ML posture estimate $f$ of the forward kinematic model, we can compute the Jacobian of the forward model as

$$
J_{f}(\mathbf{a})=\left[\frac{\partial f(\mathbf{a})}{\partial a_{1}}, \ldots, \frac{\partial f(\mathbf{a})}{\partial a_{m}}\right]^{T}
$$

Given $J_{f}(\mathbf{a})$, it is straight-forward to implement a gradient descent-based algorithm that continuously minimizes the distance function and, thus, controls the manipulator towards the target configuration. While such a "greedy" controller may get trapped in local minima of the distance function and fails to plan around obstacles in general, it nevertheless solves many important control tasks and it builds the basis for higher-level path-planning algorithms, such as probabilistic road-maps.

# 4. Failure Awareness and Life-Long Adaptation 

So far, we have assumed that the kinematics of the robot remain unchanged during its whole life-time. It is clear, however, that in real-world applications, the robot will change in the course of time. This requires that the robot revises parts of its internal model over time, allowing it to discriminate between earlier and more recent observations. We would like the robot to detect changes to its body by testing the validity of its local models at different points in time and at different temporal scales. It might even be useful for the robot to maintain multiple body schemas at different time scales. Consider, for example, a robot that uses an accurate pre-programmed model over a long period of time, but which is also able to create and use a new models that takes over as soon as the body structure of the robot changes (which could be as little as the displacement of one visual marker). Such a situation is depicted in Fig. 11. In this experiment, we changed the end-effector body part without notifying the system. The task then was, to automatically detect the change and to learn a replacement for the mismatching local model.

For dealing with model changes over time, we consider temporal local models $\mathcal{M}^{T}$ that describe the geometric relationship $p_{\mathcal{M}}^{T}\left(\mathbf{Z}_{i \rightarrow j} \mid \mathcal{A}_{i \rightarrow j}, T\right)$ between two observed body parts $\mathbf{Y}_{i}$ and $\mathbf{Y}_{j}$ given a subset of the action signal $\mathcal{A}_{i \rightarrow j} \subset\left\{a_{1}, \ldots, a_{n}\right\}$ and a particular time interval $T$. However, the size of the learning problem now also grows exponentially in time yielding the immense upper bound of $\sum_{k=0}^{m}\binom{n}{2}\binom{m}{k} 2^{|T|}$ local models to be considered. As it would be practically infeasible to evaluate all of these local models even for small periods of time, three additional assumptions can be made such that

an efficient algorithm for online application can be implemented:

1. Changes to the kinematic structure and/or body geometry are relatively rare events.
2. Changes to the robot's body happen incrementally.
3. Whatever local models were useful in the past, it is likely that similaror even the same-local models will be useful in the future.

Due to Assumption 1, we do not have to re-learn the local models continuously and re-optimize the network, but rather it is sufficient to monitor the prediction accuracies of the models until one of them is not evaluated as being valid any more. In this case, Assumption 2 states that the network cannot change completely at a given time step, but that we can recover the new structure by exchanging non-valid local models by re-learned ones individually. Furthermore, according to Assumption 3, it is reasonable to begin the search for new models with those that are similar to previously useful models, i.e., to keep a history of successful local models and to start searching within this history before learning new models from scratch.

These rules were incorporated into an integrated system, that is able to learn a body schema from scratch and to exchange local models at a later stage, whenever a misfit is detected. For rating and ordering alternative local models, we consider the structural proximity $C\left(\mathcal{M}_{2} \mid \mathcal{M}_{1}\right)$ of two local models which we define as the ratio of shared nodes in the Bayesian network. This way, models that depend on a similar set of variables are given preference in the search. We now present an experimental evaluation of the integrated system in simulation and on two real robotic manipulators.

# 5. Experimental Results 

We tested our approach in a series of experiments both on a real robot and in simulation. The goal of our experiments was to verify that

1. the robot is able to learn its kinematic structure and individual transformation functions,
2. subsequent changes to the robot's body are detected confidently (blocked joints / deformations),
3. the body schema is updated automatically without human intervention,
4. and the resulting model allows for accurate prediction and control.

The two real robots used to carry out the experiments were equipped with a 2-DOF and with a 6-DOF manipulator, respectively, composed of Schunk PowerCube modules (see Fig. 7). As the ground-truth kinematic model to compare against, we consider a carefully hand-tuned model and the joint encoder measurements-which are not used for learning and prediction in our approach. Visual perception was implemented using a Sony DFW-SX900 FireWire camera at a resolution of 1280x960 pixels. Seven black-and-white markers were attached to the joints of the robot and the ARToolkit vision module (Fiala, 2004) was used to continuously estimate their 6D poses. The standard deviation of the camera noise was measured to $\sigma_{\text {markers }}=44 \mathrm{~mm}$ in 3D space, which is acceptable considering that the camera was located two meters apart from the robot. The prediction errors and errorbars reported in the following were estimated on an independent test set of $\left|\mathcal{D}_{\text {testing }}\right|=15$ data samples.

# Evaluation of Model Accuracy 

To quantitatively evaluate the accuracy of the kinematic models learned from scratch as well as the convergence behavior of our learning approach, we generated random action sequences and analyzed the intermediate models using the 2-DOF robot of which the kinematic model is perfectly known. Figure 15 gives the absolute errors of prediction and control after certain numbers of observations have been processed. For a reference, we also give the average observation noise, i.e. the absolute localization errors of the visual markers. As can be seen from the diagram, the body schema converges robustly within the first 10 observations. After about 15 training samples, the accuracy of the predicted body part positions becomes even higher than the accuracy of the direct observations. The latter is a remarkable result as it means that, although all local models are learned from noisy observations, the system is able to "blindly" estimate its configuration more accurately than immediate perception. The figure also gives the accuracy of the gradientbased control algorithm. Here, we used an additional marker for defining a target location for the end effector. We learned the full body schema model from scratch as in the previous experiment and used the gradient-based control algorithm to bring the end effector to the desired target location. The average positioning error is in the order of the perception noise (approx. 50 mm , see Fig. 15), which is slightly higher than the prediction error alone.

## Scenario 1: Blocked Joint

In a second experiment we used the 6-DOF robot (see Fig. 7) to evaluated how well the proposed system can detect a stuck joint and repair its model accordingly. To this aim, we initialized the body schema with an accurate,

manually calibrated model. Upon detection of a model mismatch, new local models were trained from $\left|\mathcal{D}_{\text {training }}\right|=30$ consecutive training samples recorded after the model was instantiated. In order for a local model to be valid, its translational and rotational error on the test set was required to be below a threshold of $\theta_{\text {trans }}=3 \sigma_{\text {trans }}=150 \mathrm{~mm}$ and $\theta_{\text {rot }}=3 \sigma_{\text {rot }}=45^{\circ}$, with $\sigma_{\text {trans }}$ and $\sigma_{\text {rot }}$ the standard deviations of the translational and rotational observation noise, respectively. New local models were only sampled when no valid spanning tree could be constructed for $\left|\mathcal{D}_{\text {testing }}\right|$ consecutive time steps, as this is the time it takes to replace most if not all data samples of the test set.

We generated a large sequence of random motor commands $\left\langle a_{1}, \ldots, a_{m}\right\rangle$. Before accepting a pose, we checked that the configuration would not cause any (self-)collisions and that the markers of interest would potentially be visible on the camera image. This sequence was sent to the robot and after each motion command, the observed marker positions $\left\langle\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{n}\right\rangle$ were recorded. We allowed for arbitrary motion patterns (just constrained by the geometry of the manipulator) and thus do not assume full visibility of the markers. In the rare case of an anticipated or actual (self-)collision during execution, the robot stopped and the sample was rejected. Analysis of the recorded data revealed that, on average, the individual markers were visible only in $86.8 \%$ of the time with the initial body layout. In a second run, we blocked the end-effector joint $a_{4}$, so that it could not move, and again recorded a log-file. An automated test procedure was then used to evaluate the performance and robustness of our approach. For each of 20 recorded runs, a data sequence was sampled from the log-files, consisting of 4 blocks

with $N=100$ data samples each. The first and the third block were sampled from the initial body shape, while the second and the fourth block were sampled from the log-file where the joint got blocked.

Fig. 16 shows the absolute errors of the local models predicting the endeffector pose. As expected, the prediction error of the engineered local model increases significantly after the end-effector joint gets blocked at $t=100$. After a few samples, the robot detects a mismatch in its internal model and starts to learn a new dynamic model (around $t=130$ ), which quickly reaches the same accuracy as the original, engineered local model. At $t=200$, the joint gets repaired (unblocked). Now the estimated error of the newly learned local model quickly increases while the estimated error of the engineered local model decreases rapidly towards its initial accuracy. Later, at $t=300$, the joint gets blocked again in the same position, the accuracy of the previously learned local model increases significantly, and thus the robot can re-use this local model instead of having to learn a new one.

The precision of the combined model-i.e. the engineered one fused with the one learned after having detected the failure-are given in Fig. 17 and Fig. 18 for 20 re-runs of the experiment. The hand-tuned initial geometrical model evaluates to an averaged error at the end-effector of approx. 37 mm . After the joint gets blocked at $t=100$, the error in prediction increases rapidly. After $t=115$, a single new local models gets sampled, which already is enough to bring down the overall error of the combined kinematic model to approximately 51 mm . Training of the new local model is completed at around $t=135$.

Later, at $t=200$, when the joint gets un-blocked, the error estimate of the

combined kinematic model increases slightly, but returns much faster to its typical accuracy: Switching back to an already known local model requires less data samples than learning a new model (see Tab. 1). At $t=300$, the same quick adaption can be observed when the joint gets blocked again.

# Scenario 2: Deformed limb 

In a third experiment ${ }^{1}$, we changed the end-effector limb length and orientation and applied the same evaluation procedure as in the previous subsection. This was accomplished by placing a tool with an attached marker in the gripper and changing its configuration during the experiment (see Fig. 11ff). The quantitative results for 20 runs are given in Fig. 20 and Fig. 21. After the tool gets displaced at $t=100$, two local models have to be sampled on average to repair the kinematic model. The prediction accuracy of the whole system closely resembles the levels that were obtained in the case of the blocked joint: On average, we measured an accuracy of 47 mm after recovery. In Tab. 1, we summarize the recovery times for this and the previous experiment. As can be seen from the results, the system adapts to a blocked joint quicker than to a deformed limb, and recalling a previously successful model-i.e. the engineered one after "repair" or the newly learned one after "same failure"-is significantly faster than learning from scratch (after "failure").

[^0]
[^0]:    ${ }^{1} \mathrm{~A}$ demonstration video of this experiment can be found on the Internet at http://www.informatik.uni-freiburg.de/ sturm

# Controlling a Deformed Robot 

Finally, we ran a series of experiments to verify that dynamically maintained body schemas can be used for accurate positioning and control. The experiments were performed on a simulated 4-DOF manipulator. We defined a trajectory consisting of 30 way-points (in 3D space) that the manipulator should approach using the inverse kinematics derived from its current body schema, see Fig. 22 and Fig. 23. When the initial geometric model was used to follow the trajectory by using the undamaged manipulator, a positioning accuracy of 7.03 mm was measured. When the middle limb was deformed by $45^{\circ}$, the manipulator with a static body schema was significantly off course, leading to an average positioning accuracy of 189.35 mm . With dynamic adaptation enabled, the precision settled at 15.24 mm . These results are also summarized in Tab. 2 including the two standard deviations of the errors obtained on 20 runs. The results show that dynamic model adaption enables a robot to maintain a high positioning accuracy even after substantial changes to its body.

## 6. Related Work

The concept of kinematic functions and inverse kinematic functions in robotics is closely related to the concept of body image and body schema in cognitive neuroscience (Stamenov, 2005; Gallagher, 2005). Evidence from studies of both humans and higher primates indicates regions of the higherlevel visual cortex that are specialized for the visual perception of the body (Peelen and Downing, 2007). Mirror neurons, as found in brain area F5, map proprioceptive sensations to tactile and visual ones and thereby seem

to serve as a neurological representation of the body schema (Holmes and Spence, 2004), suggesting that the body schema serves as a spatio-temporally integrated image of various modalities, such as auditory and visual perceptions and somatic including tactile sensations as well (Sawa et al., 2007). Neuro-physiological evidence indicates that humans as well as higher primates are able to learn and adapt their body schema continuously and autonomously (Meltzoff and Moore, 1997). Brain scan studies of monkeys that have been trained to use tools revealed that the tool itself even gets integrated into their body schemas over time (Maravita and Iriki, 2004).

The problem of learning kinematics of robots has been investigated heavily in the past. Recently, Kolter and Ng (2007) enabled a quadruped robot to follow omnidirectional paths using dimensionality reduction techniques. Their key idea is to use a simulator for identifying a suitable subspace for policies and then to learn with the real robot only in this low-dimensional space. A similar direction has been explored by Dearden and Demiris (2005), who applied dimensionality reduction techniques to unveil the underlying structure of the body schema. Similar to this work, their approach is formulated as a model selection problem between different Bayesian networks. Another instance of approaches based on dimensionality reduction is the work by Grimes et al. (2006) who applied the principal component analysis (PCA) in conjunction with Gaussian process regression for learning walking gaits on a humanoid robot.

Yoshikawa et al. (2004a) used Hebbian networks to discover the body schema from self-occlusion or self-touching sensations. and learned classifiers for body/non-body discrimination from visual data (Yoshikawa et al.,

2004b). Other approaches used nearest-neighbor interpolation (Morasso and Sanguineti, 1995) or neural networks (Natale, 2004), for example for handeye coordination (Gaskett and Cheng, 2003) using self-organizing maps. By combining the body images of multiple modalities, e.g., both a motor and a tactile body image, it becomes possible to infer the motor Jacobians even for invisible hand positions (Sawa et al., 2007). As the required number of training samples increases exponentially with the degrees of freedom of the robot, Lopes and Santos-Victor (2005) propose to learn the kinematic function incrementally, first by moving only the shoulder/elbow joints, and later for the hand. A similar approach was formulated by de Angulo and Torras $(2002,2005)$ for learning the inverse kinematic function in two parts, which speeds up learning but requires an additional search step during evaluation of the function. For redundant kinematic chains, no global inverse kinematic function exists. Therefore, D'Souza et al. (2001) used Locally Weighted Projection Regression (LWPR) to estimate the inverse kinematic function locally at the current configuration from observed data. Recently, Ting et al. (2006) developed a Bayesian parameter identification method for non-linear dynamic systems, such as a robotic arm or a 7-DOF robotic head.

The approach presented in this article is also related to the problem of self-calibration which can be understood as a subproblem of body schema learning. When the kinematic model is given in a parametric form, the parameters can be estimated efficiently, in certain cases, by optimizing the parameters directly (Hersch et al., 2008) or by maximizing the likelihood of the model given the data (Roy and Thrun, 1999). Genetic algorithms have been used for parameter optimization when no closed form is available

(Bongard et al., 2006b). To a certain extent, such methods can also be used to calibrate a robot that is temporarily using a tool (Nabeshima et al., 2005). In contrast to the work presented here, such approaches require a parametrized kinematic model of the robot.

To achieve continuous self-modeling, Bongard et al. (2006a) recently described a robotic system that continuously learns its own structure from actuation-sensation relationships. In three alternating phases (modeling, testing, prediction), their system generates new structure hypotheses using stochastic optimization, which are validated by generating actions and by analyzing the following sensory input. In a more general context, structure learning was studied in arbitrary non-linear systems using similar mechanisms by Bongard and Lipson (2007).

In contrast to all the approaches described above, we propose an algorithm that learns both the structure as well as functional mappings for the individual building blocks. Furthermore, our model is able to revise its structure and component models on-the-fly. This paper presents a complete view on our previous works (Sturm et al., 2008b,a), the first of which introduced the probabilistic kinematic model as well as the basic algorithm for structure search. The latter work extended the model towards life-long adaptation and self-monitoring and gave more experimental results in complex and realistic scenarios.

# 7. Conclusion 

In this article, we presented a novel approach to body schema learning and life-long body adaptation for a robotic manipulation system. Our central

idea is to continuously learn a large set of local kinematic models using nonparametric regression and to search for the best arrangement of these models to represent the full system. To the best of our knowledge, this is the first time that such complex kinematic structures have been learned from scratch using visual self-observation only.

Our work follows the general idea of learning by explanation. The search for the kinematic structure (including its dimensionality and connectivity) as well as the calibration of the local models is guided by how well the set of observations can be explained by the model.

In experiments carried out with a real robot and in simulation, we demonstrated that our system is able to deal with missing and noisy observations, operates in full 3D space, and is able to perform relevant tasks like prediction, control, and online adaptation after failures.

# Acknowledgments 

This work has partly been supported by the EU under FP6-IST-004250 (COSY), FP6-IST-045388 (INDIGO), and by the German Ministry for Education and Research (BMBF) through the DESIRE project.
