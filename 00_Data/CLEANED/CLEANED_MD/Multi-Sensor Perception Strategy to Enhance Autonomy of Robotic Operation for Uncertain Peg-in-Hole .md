# Article 

## Multi-Sensor Perception Strategy to Enhance Autonomy of Robotic Operation for Uncertain Peg-in-Hole Task

Li Qin *, Hongyu Wang, Yazhou Yuan and Shufan Qin

## check for updates

Citation: Qin, L.; Wang, H.; Yuan, Y.; Qin, S. Multi-Sensor Perception Strategy to Enhance Autonomy of Robotic Operation for Uncertain Peg-in-Hole Task. Sensors 2021, 21, 3818. https://doi.org/10.3390/ s21113818

Academic Editors: Pawel Strumillo and Piotr Samczynski

Received: 9 May 2021
Accepted: 28 May 2021
Published: 31 May 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

School of Electrical Engineering, Yanshan University, Qinhuangdao 066012, China; 972472486@stumail.ysu.edu.cn (H.W.); yzyuan@ysu.edu.cn (Y.Y.); 1736941343@stumail.ysu.edu.cn (S.Q.)<br>* Correspondence: ql@ysu.edu.cn; Tel.: +86-186-3038-4419


#### Abstract

The peg-in-hole task with object feature uncertain is a typical case of robotic operation in the real-world unstructured environment. It is nontrivial to realize object perception and operational decisions autonomously, under the usual visual occlusion and real-time constraints of such tasks. In this paper, a Bayesian networks-based strategy is presented in order to seamlessly combine multiple heterogeneous senses data like humans. In the proposed strategy, an interactive exploration method implemented by hybrid Monte Carlo sampling algorithms and particle filtering is designed to identify the features' estimated starting value, and the memory adjustment method and the inertial thinking method are introduced to correct the target position and shape features of the object respectively. Based on the Dempster-Shafer evidence theory (D-S theory), a fusion decision strategy is designed using probabilistic models of forces and positions, which guided the robot motion after each acquisition of the estimated features of the object. It also enables the robot to judge whether the desired operation target is achieved or the feature estimate needs to be updated. Meanwhile, the pliability model is introduced into repeatedly perform exploration, planning and execution steps to reduce interaction forces, the number of exploration. The effectiveness of the strategy is validated in simulations and in a physical robot task.


Keywords: robot; multi-sensor perception; Bayesian probability; fusion decision; autonomy operation

## 1. Introduction

Several recent studies have demonstrated that robotic operations may no longer be targeted at specific objects and structured tasks. For example, in the medical field, robots autonomously perform large-scale pharyngeal swab sampling to reduce the risk of COVID-19 (Coronavirus Disease 2019) in health care workers [1]. In industry, robots can replace humans in the autonomous assembly of circuit breaker components and ensure a compact assembly [2]. Similar robotic operations can also extend to the robotic refueling and charging of vehicles. A critical step that exists in the above tasks is the robotic peg-inhole operation with an uncertain object. This type of operation usually has to meet force and position accuracy requirements under the constraints of narrow spaces and uncertain objects. It is essential to obtain feature information of uncertain objects for the performance of frequent interaction operational tasks in narrow spaces.

Visual sensors are considered to be the most common and direct method, which are used to perceive important features of the uncertain object. In [3,4] they perceived the hole posture by a single vision or multi-level vision for axial hole assembly and rivet-in-hole Insertion. However, narrow uncertain objects often cause visual occlusion. For example, during refueling for public service, the end of the fuel gun is not available to the tank well through the vision sensor under the condition of uncertain object features, due to the physical occlusion of the robot itself and the tank housing. Occlusion can lead to sensors not being able to acquire the needed information [5] and force task termination. To solve this problem, some methods have been proposed, such as introducing a heuristic approach [6], which compensates for the residual visual information by a priori knowledge. Nevertheless,

the process of demonstration and retrieving data is difficult to experiment in the real world unstructured environment, such as space, deep sea and disaster scene. For frequent interaction operational tasks, tactile sensors can provide richer local information than visual sensors, such as shape, position and friction. Many researches are concerned with predicting grasp stability [7] or re-grasp [8] by the information from tactile feedback. Others use tactile sensors to estimate target position [9] and local surface texture [10,11]. Although the tactile sensor avoids to some extent the shortcomings of the visual absence, it is dependent on the contact state between the robot and operating object. In other words, tactile sensors cannot provide the necessary information when the robot is not in contact with the operating object. Humans instinctively have the ability to seamlessly combine the visual and tactile senses to perceive their surroundings accurately and evaluate the operations being performed [12]. Vision sensors can provide global information for accurate reach. Tactile sensors can estimate local information during operation in the presence of visual errors and missing data due to occlusion [10]. It is a feasible solution idea to achieve the complementarity and concurrency of these two sensors in the robotic autonomy operation.

Some methods based on various learning algorithms that fuse visual and tactile information are proposed, for example, in-depth researches on grasping stability prediction [13,14] and shape estimation [15]. When operating in narrow spaces, Lv et al. [16] fused visual and tactile information using the SVM (support vector machine) algorithm, which enabled the robot to open the cover and insert the charging plug into the charging port autonomously. Shaidah Jusoh et al. [17] proposed a multimodal information fusion method for robots to recognize actions and generate tasks in industrial assembly environments. Nevertheless, multimodal information fusion requires prior knowledge of the task to obtain realistic performance. When this prior knowledge is not available, in [18], a multi-modal representation learning approach with self-supervised functionality, which incorporated visual, force, and robot motion information, was employed to complement the absence caused by visual occlusion in a frequent interaction task. However, the implementation of these methods, whether offline or online learning, requires a large amount of data as the basis. Therefore, these methods are not applicable to operating objects where it is difficult to obtain feature datasets for uncertain objects in advance.

Compared to the above methods, the approach based on Bayesian probabilistic techniques has a clear advantage that a large amount of training data is not required in fusing multi-sensor information. The results in [19] also demonstrated that approaches based on Bayesian probabilistic techniques are significantly superior to neural network-based approaches. In [20], a Bayesian filtering framework was proposed to fuse the residual visual information with the tactile information from the GelSight contact sensor to track the objects operated by the robot in hand. Although using tactile sensors are an effective solution to the problem of visual occlusion, it has high requirements for the working environment as a precision instrument. For special operating environments or special tasks, it may be inconvenient to install dedicated tactile sensors or impossible to collect information. In order to reduce the reliance on dedicated tactile sensors, they are replaced by force/torque sensors. For instance, Fan Zhang et al. [21] used a probabilistic tracking method using a Bayesian network that integrated multimodal information (force information and position information) to estimate the posture of the human body in real-time to dress for disabled people without a camera, even when the person has a sudden unexpected movement. However, a pre-constructed object model is required, which is difficult for the previously mentioned operating object. In the field of robotic assembly, Korbinian et al. [22] presented a framework for tracking visual and tactile information assembly to perform assembly operations for multiple hole types. Besides, some researchers have fused haptic and visual information using a Bayesian framework to achieve the estimation of target positions of assembled objects in industrial assembly [23,24]. In addition to estimating the target position, the estimation of shape and other features and the decision capability, which

empowers the robot to evaluate the quality of the task (how well the task was completed), can further improve autonomy.

To achieve robotic autonomy operation without human intervention and without making any provisions for an uncertain object, the designed solution scheme in this paper is shown in Figure 1. Considered the possibility of visual deficits, contact force information from the force/torque sensor and position information from the robot joint encoder are introduced. The information from the three sensors is used in a multi-sensor perception strategy (MSP) to obtain accurate features of the operating object and guide the operation. The strategy performs an exploration-correction-decision-correction process, as shown in the orange box in Figure 1. In the strategy, the interactive exploration method (IE) is first presented to obtain the features of the uncertain object without a priori knowledge. It integrates the Bayesian posterior probabilities obtained from multimodal information (visual, contact force and position) to features estimated starting value, i.e., the target position and shape of the uncertain object. Then, considered that the dynamic interaction process may increase the uncertainty of the operating object, memory adjustment and inertial thinking are introduced as correction methods to improve the accuracy of the estimates further.
![img-0.jpeg](img-0.jpeg)

Figure 1. The solution scheme for robotic operating.
To achieve the function of the robot deciding the next operation by relying on its own judgement, a fusion decision strategy (FD) is designed which is adapted to fine-

grained operations with multiple requirements, such as operating accuracy and preload. The purpose of this is to avoid the errors that can arise from single-evidence decisions, for example, when evidenced by position only, substandard quality of operation may occur (i.e., the operating tool reaches the target position but is not installed solidly in the peg-in-hole task). When evidence by contact force only, it can be incorrectly judged as satisfying the task requirements, because an interaction during operation creates a contact force similar to the expected one. The fusion decision strategy is used after each exploration of operating object features. Unlike existed research works that only used position accuracy as an indicator, the designed fusion decision strategy fuses both position and force evidence information in the D-S theoretical framework and includes their uncertainties to guide the subsequent operations.

Finally, command information, such as the features of the uncertain object and the evaluation results of the operation, from the MSP is sent to the robot to guide the operation. As shown in the pink box in Figure 1, the flexibility model is introduced to further optimize the robotic interaction behavior with the operating object.

This paper includes the following contents. In Section 2, There are major problems that robots need to face for autonomous operation under uncertain objects. In Section 3, the proposed multi-sensor perception strategy is presented in detail. In Section 4, the control system is proposed. In Section 5, simulations based on the robot model established are performed to verify the feasibility of the proposed method and provided parameter references for the experiments. Then, physical robot operation experiments with dynamic objects are conducted to further verify the effectiveness of the proposed method faced with more uncertain objects. In Section 6, conclusions are given.

# 2. Problem Description 

Based on the above analysis, the following issues will be investigated in this paper:
(1) how to perceive the features of the uncertain operating object,
(2) how to achieve make an automatic decision for the robotic operation,
(3) how to achieve safety interaction between the robot and the uncertain operating object.

For the critical step of the pen-in-hole task, a mathematical description of the above problem was presented. As shown in Figure 1, an internal equivalent model of the operation object is drawn on the right side. The cross-section where the robot interacts with the uncertain operation object is extracted to establish an equivalent model of the uncertain operation object. The inner shape and the target position are selected as the features of the uncertain operation object. It is worth noting that the shape mentioned here is the overall shape of the proposed uncertain operation object. The irregular interior surface has no significant effect on the features to be perceived, so it can be ignored. In addition, for perception algorithms, since the robotic end is simplified to a point with no width and the inner wall is inclined, the uncertain operating object is simplified to a triangle, as shown in Figure 1. Finally, the shape and position can be expressed by three vertices:

$$
X_{\mathrm{d}}=\left[\begin{array}{ll}
\boldsymbol{P}^{\mathrm{a}} & \boldsymbol{P}^{\mathrm{b}} & \boldsymbol{P}^{\mathrm{c}}
\end{array}\right]
$$

where $\boldsymbol{P}^{\mathrm{a}} \in \mathbb{R}^{\mathrm{D}}, \boldsymbol{P}^{\mathrm{b}} \in \mathbb{R}^{\mathrm{D}}, \boldsymbol{P}^{\mathrm{c}} \in \mathbb{R}^{\mathrm{D}}$ are the positions of vertex A , vertex B and vertex C of the triangle, respectively. D denotes the space dimension where the robot is located. The position $\boldsymbol{P}^{\mathrm{b}}$ of vertex B is utilized to represent the target position $\boldsymbol{X}_{\mathrm{e}}$ of the uncertain operating object.

Besides visual error and occlusion, the operating object may generate continuous dynamic effects due to the interaction process, which can increase uncertainty. The uncertainty can be expressed as $\omega_{\mathrm{e}}$. The estimated position of the uncertain object by vision sensors can be expressed as:

$$
\boldsymbol{X}_{\mathrm{e}, \text { vision }}=\boldsymbol{X}_{\mathrm{e}, \text { reality }}+\omega_{\mathrm{e}}
$$

where $\omega_{\mathrm{e}}$ contains visual errors, which are usually non-linear and uncertain. It is also very expensive to recognize and predict for $\omega_{\mathrm{e}}$. Therefore, the target position of the uncertain operating object $\boldsymbol{X}_{\mathrm{e}}$ can be obtained by estimating the local features of the uncertain operating object $\boldsymbol{X}_{\mathrm{d}}$. When the estimate is accurate enough, $\boldsymbol{X}_{\mathrm{e}}$ is $\boldsymbol{X}_{\mathrm{e}, \text { reality }}$.

Moreover, in practical application, the operation task performed by the robot is usually composed of several continuous nail hole operations. Each contact behavior induces dynamic interactions at the operational object connections, resulting in coupling effects of robot operational errors and system stability. This coupling effect accumulates and increases over the course of the task. From the above description and analysis, it is clear that for each peg-in-hole operation, the robot must perform with high operational accuracy and apply appropriate forces to the operational object during continuous and large task volumes. That is, the contact force needs to satisfy:

$$
F_{\mathrm{e}} \in\left(\mathrm{~F}_{\text {preload }}, \mathrm{F}_{\max }\right)
$$

where $F_{\mathrm{e}}$ is the contact force at the robotic end, $\mathrm{F}_{\text {preload }}$ is the preload force in accordance with the operational requirements, $\mathrm{F}_{\max }$ is the maximum contact force allowed. On the one hand, a very high force is not allowed due to the safety of the whole system. On the other hand, a tiny force is also not qualified because there should be enough preload to ensure that each step of the operation is stable, ensuring that the whole structure is stable and reliable [25].

If the robot can make timely autonomy decisions based on the collected limited information to guide the subsequent movements, the number of contacts can be effectively reduced and thus the dynamic effects are reduced. In addition, it also reduces human involvement, which effectively avoids human errors and workload. Therefore, a variable $\xi$, which represents the result of the decision, is needed to evaluate the quality of the task and guide subsequent operations.

# 3. Design of Multi-Sensor Perception Strategy 

The multi-sensor perception strategy is divided into two parts, i.e., interactive exploration and fusion decision, which are shown in Figure 2. Firstly, in the interactive exploration part, the information from the three sensors is seamlessly combined to obtain features estimated starting value $\hat{\boldsymbol{X}}_{\mathrm{d} 0}^{\prime}$. The correction component is used to adjust the $\hat{\boldsymbol{X}}_{\mathrm{d} 0}^{\prime}$, which will obtain accurate operating object features $\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor2 }}^{\prime}$. Then, the information in $\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor2 }}^{\prime}$ is sent to the fusion decision part and the pliability model part, respectively. The fusion decision part will provide the robot controller and exploration part with $\xi$ to guide subsequent movements. Finally, $\xi$ and the commanded position $\boldsymbol{X}_{\mathrm{c}}$ provided by the pliable model will together guide the subsequent robot movements.

### 3.1. Interactive Exploration

In the case of imperfect vision sensors, the features of the uncertain operating object are explored by integrating three sources of information. Given the position of the robotic end (i.e., $\boldsymbol{X}_{\text {end }}^{\prime}$ in (3.1.3)), the force information between the robot and the uncertain operating object (i.e., $\boldsymbol{F}_{\mathrm{e}}{ }^{\prime}$ in (3.1.4)) and estimated operating object features by vision (i.e., $\hat{\boldsymbol{X}}_{\mathrm{e}, \text { vision }}^{\prime}$ in (3.1.5)), particles (each particle $\hat{\boldsymbol{z}}_{i}^{\prime}$ corresponds to a set of features of the uncertain operating object $\boldsymbol{X}_{\mathrm{d}}$ ) are weighted integrated to estimate the features of the uncertain operating object. The coordinate transformation between the three sensors can be achieved by the transformation matrix $T_{X}^{\mathrm{E}}$ and $T_{X}^{\mathrm{F}}$. Furthermore, memory adjustment and inertial thinking methods are introduced to correct the shape feature and target position feature of the uncertain operating object, respectively, to improve the estimation accuracy.

![img-1.jpeg](img-1.jpeg)

Figure 2. Multi-sensor perception strategy.

# 3.1.1. Initialization 

It is assumed that the features of the uncertain operating object at each moment obey the Gaussian distribution and include the dynamics of operating object prediction.

$$
P=N\left(\boldsymbol{\mu}_{z}^{t}, \boldsymbol{\Sigma}_{z}^{t}\right)
$$

where $\boldsymbol{\mu}_{z}^{t}$ represents the mean vector of the Gaussian distribution, $\boldsymbol{\Sigma}_{z}^{t}$ represents the covariance matrix of Gaussian distribution. $\boldsymbol{\mu}_{z}^{t}$ is the features of the uncertain operating object at the current moment. For initialization, $\boldsymbol{\mu}_{z}^{0}$ is the initial features of the uncertain operating object collected by the depth camera and $\boldsymbol{\Sigma}_{z}^{0}$ is the error of the depth camera. When $t>0$, the definition of $\boldsymbol{\mu}_{z}^{t}$ and $\boldsymbol{\Sigma}_{z}^{t}$ will be introduced in detail in Section 3.1.6.

### 3.1.2. Random Wandering of Sampled Particles

The particle random walk is realized by adding a constant diagonal matrix to the covariance matrix of the Gaussian distribution. The purpose is to introduce dynamic effects in the uncertain operating object between two moments in the model. Hybrid Monte Carlo sampling (HMC sampling) according to the new Gaussian distribution is performed to obtain the particles:

$$
\hat{\boldsymbol{Z}}^{t}=\left[\hat{\boldsymbol{z}}_{1}^{t}, \hat{\boldsymbol{z}}_{2}^{t}, \cdots, \hat{\boldsymbol{z}}_{N}^{t}\right]^{\mathrm{T}}
$$

where $t$ is the current moment and $N$ is the number of sampled particles. $\hat{\boldsymbol{Z}}_{i}^{t}$ is a sixdimensional vector due to the representation of $\boldsymbol{X}_{\mathrm{d}}$.

The random walk of particles is defined as:

$$
p\left(\hat{\boldsymbol{z}}_{i}^{t}\right)=N\left(\hat{\boldsymbol{z}}_{i}^{t} \mid \boldsymbol{\mu}_{z}^{t-1}, \boldsymbol{\Sigma}_{z}^{t-1}+\boldsymbol{\Sigma}_{\triangle}\right)
$$

where $\boldsymbol{\Sigma}_{\triangle}$ is a constant diagonal matrix, which contains the dynamics of the predicted uncertain operating object between two moments.

In the following section, based on the position information and force information of the robotic end and visual estimated operating object features at the current moment, probability calculations are performed on each sampled particle to recursively design a Gaussian distribution so that the features of the uncertain operating object at each moment can be estimated.

3.1.3. Estimating the Probability of the Features of the Uncertain Object Based on Position Information

The robotic end position $\boldsymbol{X}_{\text {end }}^{t}$ is used to estimate the probability of the features of the uncertain operating object, as shown in Figure 3. $d_{i}^{t}$ is defined as the distance between the position of the current robotic end and the estimated uncertain operating object $\hat{\boldsymbol{Z}}_{i}^{t}$. Each $d_{i}^{t}$ is obtained by calculating $d_{i, \text { up }}^{t}$ and $d_{i, \text { down }}^{t}$, where $d_{i, \text { up }}^{t}$ is the sum of $d_{\mathrm{a}}$ and $d_{\mathrm{b}}$ and $d_{i, \text { down }}^{t}$ is the sum of $d_{\mathrm{c}}$ and $d_{\mathrm{b}}$, respectively. Among them, $d_{\mathrm{a}}$ is the distance between the robotic end and the vertex $\mathrm{A}, d_{\mathrm{b}}$ is the distance between the robotic end and the vertex $\mathrm{B}, d_{\mathrm{c}}$ is the distance between the robotic end and the vertex C . Note that whether $d_{i, \text { up }}^{t}$ or $d_{i, \text { down }}^{t}$ is used depends on the current position of the robotic end in the uncertain operating object. In other words, if the end of the robot collides with $\overrightarrow{\boldsymbol{A B}}, d_{i, \text { up }}^{t}$ is used, otherwise, $d_{i, \text { down }}^{t}$ is used. Assumed that the robotic end is on the boundary (i.e., $d_{i}^{t}=\mathrm{d}_{\overrightarrow{\boldsymbol{A B}}}$ or $d_{i}^{t}=\mathrm{d}_{\overrightarrow{\boldsymbol{C B}}}$ ) when the robot happens to collide with the uncertain operating object. Therefore, under the conditions of a given uncertain operating object, the probability of the current robot end position colliding with the uncertain operating object can be expressed as:

$$
p\left(\boldsymbol{X}_{\text {end }}^{t} \mid \hat{\boldsymbol{z}}_{i}^{t}\right)=N\left(d_{i}^{t} \mid \mu_{d}, \sigma_{d}^{2}\right)
$$

where $\sigma_{d}^{2}$ is the covariance matrix of the Gaussian distribution function, $\mu_{\mathrm{d}}$ can be defined as:

$$
\mu_{\mathrm{d}}=d_{\mathrm{o}}=\left\{\begin{array}{l}
\mathrm{d}_{\overrightarrow{\boldsymbol{A B}}}, \text { the end of the robot collides with } \overrightarrow{\boldsymbol{A B}} \\
\mathrm{~d}_{\overrightarrow{\boldsymbol{C B}}}, \text { the end of the robot collides with } \overrightarrow{\boldsymbol{C B}}
\end{array}\right.
$$

where $d_{\mathrm{o}}$ is the mean of the Gaussian distribution. When the end of the robot collides with $\overrightarrow{\boldsymbol{A B}}$, the mean is set as $d_{\mathrm{o}}=\mathrm{d}_{\overrightarrow{\boldsymbol{A B}}}$. When the end of the robot collides with $\overrightarrow{\boldsymbol{C B}}$, the mean is set as $d_{\mathrm{o}}=\mathrm{d}_{\overrightarrow{\boldsymbol{C B}}}$.
![img-2.jpeg](img-2.jpeg)

Figure 3. Probabilistic model based on the position information. The solid black line indicates the uncertain operating object and the red circle indicates the end of the robot.

# 3.1.4. Estimating the Probability of the Features of the Uncertain Object Based on Force Information 

The contact force $\boldsymbol{F}_{\mathrm{e}}{ }^{t}$ of the robotic end collected by the six-dimensional force sensor (by the contact model in the simulation) is used to calculate the probability of each particle. The normal collision position $\hat{\boldsymbol{n}}_{i}^{t}$ is obtained based on each particle $\hat{\boldsymbol{Z}}_{i}^{t}$ corresponding to the uncertain operating object and the current position of the robotic end $\boldsymbol{X}_{\text {end }}^{t}$. The friction cone $\hat{\boldsymbol{c}}_{i}^{t}$ is defined with the normal $\hat{\boldsymbol{n}}_{i}^{t}$ as the axis.

When the direction of the end contact force is inside the friction cone, the particle corresponds to the uncertain operating object with the highest probability, as shown in Figure 4. In other words, the angle $\theta_{i}^{t}$ between the end contact force $\boldsymbol{F}_{\mathrm{e}}{ }^{t}$ and the normal $\hat{\boldsymbol{n}}^{t}{ }_{i}$ should be less than the angle $\theta_{i}$ of the defined friction cone. The probability model based on force information can be defined as follows. When the end contact force $\boldsymbol{F}_{\mathrm{e}}{ }^{t}$ is inside the friction cone $\hat{\boldsymbol{c}}_{i}^{t}$, the probability of the particle $\hat{\boldsymbol{Z}}_{i}^{t}$ is defined as 1 . When the end contact force $\boldsymbol{F}_{\mathrm{e}}{ }^{t}$ is outside the friction cone $\hat{\boldsymbol{c}}_{i}^{t}$, the probability of the particle $\hat{\boldsymbol{Z}}_{i}^{t}$ is defined as a Gaussian

distribution function. Therefore, the probability of the force for each particle sampled is defined as:

$$
p\left(\boldsymbol{F}_{\mathrm{e}}{ }^{t} \mid \hat{\mathbf{z}}_{i}^{t}\right)=\left\{\begin{array}{cc}
1, & \theta_{i}^{t} \leq \theta_{\mathrm{f}} \\
N\left(\theta_{i}^{t} \mid \theta_{\mathrm{f}}, \sigma_{\mathrm{f}}^{2}\right), & \theta_{i}^{t}>\theta_{\mathrm{f}}
\end{array}\right.
$$

where $\sigma_{\mathrm{f}}^{2}$ is the covariance matrix of the Gaussian distribution function.
![img-3.jpeg](img-3.jpeg)

Figure 4. Probabilistic model based on force information. The solid black line indicates the uncertain operating object and the solid gray line indicates the end of the robot.

# 3.1.5. Estimating the Probability of the Features of the Uncertain Object Based on Visual Information 

When the robot starts to move toward the operation object, vision can easily provide feature information of the object. The current moment object features can be estimated by the Euclidean distance between $\boldsymbol{X}_{\mathrm{e}, \text { vision }}^{t}$ from the visual information and $\boldsymbol{Z}_{i}^{t}$. After the robot moves near the operation object, visual occlusion occurs. Therefore, the probability of the visual information for each particle sampled is defined as:

$$
p\left(\boldsymbol{X}_{\mathrm{e}, \text { vision }}^{t} \mid \hat{\mathbf{z}}_{i}^{t}\right)=\left\{\begin{array}{cc}
N\left(\hat{\mathbf{z}}_{i}^{t} \mid \boldsymbol{X}_{\mathrm{e}, \text { vision }}^{t}, \sigma_{\mathrm{v}}^{2}\right), & d_{\mathrm{r}}>\mathrm{d}_{\mathrm{v}} \\
0, & d_{\mathrm{r}} \leq \mathrm{d}_{\mathrm{v}}
\end{array}\right.
$$

where $\sigma_{\mathrm{v}}^{2}$ is the covariance matrix of the Gaussian distribution function, $d_{\mathrm{r}}$ is the distance between the robot and the target position of the uncertain object at the previous moment, $d_{v}$ is the minimum distance between the robot and the uncertain object without occlusion.

### 3.1.6. Weighted Integration

To improve the accuracy of the estimation, the posterior probabilities obtained from these two information sources are integrated to obtain the weighting coefficient of the particles. At a certain moment, given the end position and robotic contact force, the weight of the particle can be expressed as:

$$
p\left(\hat{\mathbf{z}}_{i}^{t} \mid \boldsymbol{X}_{\mathrm{end}}^{t}, \boldsymbol{F}_{\mathrm{e}}{ }^{t}, \boldsymbol{X}_{\mathrm{e}, \text { vision }}^{t}\right) \propto \frac{p\left(\hat{\mathbf{z}}_{i}^{t} \mid \boldsymbol{X}_{\mathrm{end}}^{t}\right) \cdot p\left(\hat{\mathbf{z}}_{i}^{t} \mid \boldsymbol{X}_{\mathrm{end}}^{t}, \boldsymbol{F}_{\mathrm{e}}{ }^{t}\right)+p\left(\boldsymbol{X}_{\mathrm{e}, \text { vision }}^{t} \mid \hat{\mathbf{z}}_{i}^{t}\right)}{L_{\mathrm{m}}} p\left(\hat{\mathbf{z}}_{i}^{t}\right)=w_{i}^{t} \cdot p\left(\hat{\mathbf{z}}_{i}^{t}\right)
$$

where $L_{\mathrm{m}}$ is the normalization factor.
Redefine the Gaussian distribution of particles as:

$$
P=N\left(\boldsymbol{\mu}_{z}^{t}, \boldsymbol{\Sigma}_{z}^{t}\right)
$$

where $\boldsymbol{\mu}_{z}^{t}$ is the mean vector and $\boldsymbol{\Sigma}_{z}^{t}$ is the covariance matrix.

$$
\begin{gathered}
\boldsymbol{\mu}_{z 0}^{t}=\sum_{i=1}^{N} w_{i}^{t} \hat{\mathbf{z}}_{i}^{t} \\
\boldsymbol{\Sigma}_{z}^{t}=\boldsymbol{A} \boldsymbol{A}^{\mathrm{T}} \\
\boldsymbol{A}=\left[\left(w_{i}^{t}\right)^{\frac{1}{2}}\left(\hat{\mathbf{z}}_{i}^{t}-\boldsymbol{\mu}_{z}^{t}\right), \cdots,\left(w_{\mathrm{N}}^{t}\right)^{\frac{1}{2}}\left(\hat{\mathbf{z}}_{\mathrm{N}}^{t}-\boldsymbol{\mu}_{z}^{t}\right)\right]
\end{gathered}
$$

where $\boldsymbol{\mu}_{z 0}^{t}$ is features estimated starting value $\hat{\boldsymbol{X}}_{\mathrm{d} 0}^{t}$ of the uncertain object.

3.1.7. Correcting the Estimated Features of the Uncertain Object

Since there may be errors in the shape and position of the uncertain object after sampling and estimation, historical information and rules of inertia thinking are used to correct the estimated value of the features of the uncertain object to improve the accuracy of the estimation, as shown in Figure 5. In this section, the memory adjustment correction method (MAC) and the Inertia thinking correction method (ITC) will be introduced in detail.
![img-4.jpeg](img-4.jpeg)

Figure 5. Schematic diagram of correction method. (a) Schematic diagram of memory adjustment correction method (left) and (b) schematic diagram of Inertia thinking correction method (right).
(1) Memory adjustment correction method

The shape features of the uncertain object are calculated based on the estimated value, after completing the sampling estimation. According to the uncertain object proposed in Section 2, the shape is defined as the angle and the depth of the triangle, as shown in Figure 6. It is an accepted fact that dynamic effects do not change the shape of the uncertain object. Referring to the iterative update process of memory and operation during continuous human exploration, the fuzzy Naive Bayes principle is used to process real-time estimation and historical information.
![img-5.jpeg](img-5.jpeg)

Figure 6. Shape features of the uncertain object.
According to the estimated value $\hat{\boldsymbol{X}}_{\mathrm{d}}$, the angle $\delta_{\mathrm{e}, i}$ is calculated,

$$
\begin{gathered}
\delta_{\mathrm{e} 1}=\tan ^{-1}\left[\left(\boldsymbol{P}_{2}^{\mathrm{b}}-\boldsymbol{P}_{2}^{\mathrm{e}}\right) /\left(\boldsymbol{P}_{1}^{\mathrm{b}}-\boldsymbol{P}_{1}^{\mathrm{e}}\right)\right] \\
\delta_{\mathrm{e} 2}=\tan ^{-1}\left[\left(\boldsymbol{P}_{2}^{\mathrm{b}}-\boldsymbol{P}_{2}^{\mathrm{c}}\right) /\left(\boldsymbol{P}_{1}^{\mathrm{b}}-\boldsymbol{P}_{1}^{\mathrm{c}}\right)\right] \\
\delta_{\mathrm{e}}=\left[\begin{array}{ll}
\delta_{\mathrm{e} 1} & \delta_{\mathrm{e} 2}
\end{array}\right]
\end{gathered}
$$

where $\delta_{\mathrm{e}}$ is the angle vector. $\boldsymbol{P}_{n}^{\mathrm{b}}$ denotes the $n$-th element in $\boldsymbol{P}^{\mathrm{b}}$. In the later sections, similar representations are used for this purpose.

To obtain the most suitable correction angle, historical information is introduced to participate in the correction calculation. The history information collection of angle is

defined as $\boldsymbol{H}_{\delta}=\left\{\boldsymbol{H}_{\delta, 1}, \boldsymbol{H}_{\delta, 2}, \cdots \boldsymbol{H}_{\delta, t-1}\right\}$, and the reference angle $\delta_{\mathrm{r}}$ is calculated through the history information collection $\boldsymbol{H}_{\delta}$.

The angle error $e_{\delta}$ is expressed as:

$$
e_{\delta, i}=\delta_{\mathrm{r}}-\delta_{\mathrm{e}, i}
$$

The posterior probability of the angle based on the angle error $\delta_{\mathrm{e}}$ is defined as:

$$
p_{i}^{j}\left(\delta_{\mathrm{e}, i} \mid e_{\delta, i}\right)=\mu_{i}\left(e_{\delta, i}\right)=\max \left(\mu_{i}^{j}\left(e_{\delta, i}\right)\right),(j=1,2)
$$

where $\mu_{i}^{j}\left(e_{\delta, i}\right)$ is the fuzzy membership function, $j$ is the labeled value, 1 is true and 2 is false.

A simple fuzzy system with two fuzzy rules is established, and the fuzzy membership function is:

$$
\begin{aligned}
\mu_{i}^{1}\left(e_{\delta, i}\right) & =\left\{\begin{array}{ll}
1, & e_{\delta, i} \leq v_{\delta, 1} \\
\frac{e_{\delta, i}-v_{\delta, 2}}{v_{\delta, 1}-v_{\delta, 2}}, & v_{\delta, 1}<e_{\delta, i} \leq v_{\delta, 2} \\
0, & e_{\delta, i}>v_{\delta, 2}
\end{array}\right. \\
\mu_{i}^{2}\left(e_{\delta, i}\right) & =\left\{\begin{array}{ll}
0, & e_{\delta, i} \leq v_{\delta, 1} \\
\frac{e_{\delta, i}-v_{\delta, 1}}{v_{\delta, 2}-v_{\delta, 1}}, & v_{\delta, 1}<e_{\delta, i} \leq v_{\delta, 2} \\
1 & e_{\delta, i}>v_{\delta, 2}
\end{array}\right.
\end{aligned}
$$

where $v_{\delta, 1}$ and $v_{\delta, 2}$ are the membership function parameters.
$\delta_{\text {cor }}$ is introduced to express the correction angle. When $j$ is 11 (i.e., the labels corresponding to both $\delta_{\mathrm{e} 1}$ and $\delta_{\mathrm{e} 2}$ are 1 ), $\delta_{\text {cor }}$ is $\delta_{\mathrm{e}}$ corresponding to the maximum value of $p_{i}^{j=1}\left(\delta_{\mathrm{e}, i} \mid e_{\delta, i}\right)$, and the credibility is recorded as the maximum value of $p_{i}^{j=1}\left(\delta_{\mathrm{e}, i} \mid e_{\delta, i}\right)$. When $j$ is 12 (i.e., only the label corresponding to $\delta_{\mathrm{e} 1}$ is 1 ), $\delta_{\text {cor }}$ is $\delta_{\mathrm{e} 1}$, and the credibility is recorded as $p_{i=1}^{j=1}\left(\delta_{\mathrm{e}, i} \mid e_{\delta, i}\right)$. When $j$ is 21 (i.e., only the label corresponding to $\delta_{\mathrm{e} 2}$ is 1 ), $\delta_{\text {cor }}$ is $\delta_{\mathrm{e} 2}$, and the credibility is recorded as $p_{i=2}^{j=1}\left(\delta_{\mathrm{e}, i} \mid e_{\delta, i}\right)$. When $j$ is 22 (i.e., the labels corresponding to both $\delta_{\mathrm{e} 1}$ and $\delta_{\mathrm{e} 2}$ are 2 ), $\delta_{\text {cor }}$ is $\delta_{\mathrm{r}}$, and the credibility is recorded as the maximum value of $p(\bullet)=0.9$.

The history information at the current moment is defined as $\boldsymbol{H}_{\delta, t}=\left[\delta_{\text {cor }}, p(\bullet)\right]^{\mathrm{T}}$. The historical information collection is regenerated as $\boldsymbol{H}_{\delta} \leftarrow \boldsymbol{H}_{\delta} \cup\left\{\boldsymbol{H}_{\delta, t}\right\}$. The reference angle $\delta_{\mathrm{r}}$ is expressed as:

$$
\delta_{\mathrm{r}}=\sum_{t=0}^{t=t-1} \frac{\boldsymbol{H}_{\delta, t, 1} \cdot \boldsymbol{H}_{\delta, t, 2}}{\sum \boldsymbol{H}_{\delta, t, 2}}
$$

The depth $l_{\mathrm{e}, i}$ is calculated based on the estimated value $\hat{\boldsymbol{X}}_{\mathrm{d} 0}$,

$$
\begin{gathered}
l_{\mathrm{e} 1}=\left|\boldsymbol{P}_{1}^{\mathrm{b}}-\boldsymbol{P}_{1}^{\mathrm{a}}\right| \\
l_{\mathrm{e} 2}=\left|\boldsymbol{P}_{1}^{\mathrm{b}}-\boldsymbol{P}_{1}^{\mathrm{c}}\right| \\
\boldsymbol{l}_{\mathrm{e}}=\left[\begin{array}{ll}
l_{\mathrm{e} 1} & l_{\mathrm{e} 2}
\end{array}\right]
\end{gathered}
$$

where $\boldsymbol{l}_{\mathrm{e}}$ is the depth vector.
In order to obtain the most suitable correction depth, historical information is introduced to participate in the correction calculation. The history information collection of depth is defined as $\boldsymbol{H}_{\mathrm{l}}=\left\{\boldsymbol{H}_{\mathrm{l}, 1}, \boldsymbol{H}_{\mathrm{l}, 2}, \cdots \boldsymbol{H}_{\mathrm{l}, t-1}\right\}$, and the reference depth $l_{\mathrm{r}}$ is calculated through the history information collection $\boldsymbol{H}_{\mathrm{l}}$.

The depth error $e_{l}$ is expressed as:

$$
e_{l, i}=l_{\mathrm{r}}-l_{\mathrm{e}, i}
$$

The posterior probability of the depth based on the depth error $I_{\mathrm{e}}$ is defined as:

$$
p_{i}^{j}\left(l_{\mathrm{e}, i} \mid e_{\mathrm{l}, i}\right)=\mu_{i}\left(e_{\mathrm{l}, i}\right)=\max \left(\mu_{i}^{j}\left(e_{\mathrm{l}, i}\right)\right),(j=1,2)
$$

where $\mu_{i}^{j}\left(e_{\mathrm{l}, i}\right)$ is the fuzzy membership function, $j$ is the labeled value, 1 is true and 2 is false. The calculation method and the same calculation method described above are omitted.
$l_{\text {cor }}$ is introduced to express the correction depth. When $j$ is 11 (i.e., the labels corresponding to both $l_{\mathrm{e} 1}$ and $l_{\mathrm{e} 2}$ are 1 ), $l_{\text {cor }}$ is $l_{\mathrm{e}, i}$ corresponding to the maximum value of $p_{i}^{j=1}\left(l_{\mathrm{e}, i} \mid e_{\mathrm{l}, i}\right)$, and the credibility is recorded as the maximum value of $p_{i}^{j=1}\left(l_{\mathrm{e}, i} \mid e_{\mathrm{l}, i}\right)$. When $j$ is 12 (i.e., only the label corresponding to $l_{\mathrm{e} 1}$ is 1 ), $l_{\text {cor }}$ is $l_{\mathrm{e} 1}$, and the credibility is recorded as $p_{i=1}^{j=1}\left(l_{\mathrm{e}, i} \mid e_{\mathrm{l}, i}\right)$. When $j$ is 21 (i.e., only the label corresponding to $l_{\mathrm{e} 2}$ is 1 ), $l_{\text {cor }}$ is $l_{\mathrm{e} 2}$, and the credibility is recorded as $p_{i=2}^{j=1}\left(l_{\mathrm{e}, i} \mid e_{\mathrm{l}, i}\right)$. When $j$ is 22 (i.e., the labels corresponding to both $l_{\mathrm{e} 1}$ and $l_{\mathrm{e} 2}$ are 2 ), $l_{\text {cor }}$ is $l_{\mathrm{r}}$, and the credibility is recorded as the maximum value of $p(\bullet)=0.9$.

The history information at the current moment is defined as $\boldsymbol{H}_{\mathrm{l}, \mathrm{r}}=\left[l_{\text {cor }}, p(\bullet)\right]^{\mathrm{T}}$. The historical information collection is regenerated as $\boldsymbol{H}_{\mathrm{l}} \leftarrow \boldsymbol{H}_{\mathrm{l}} \cup\left\{\boldsymbol{H}_{\mathrm{l}, \mathrm{r}}\right\}$. The reference depth $l_{\mathrm{r}}$ is expressed as:

$$
l_{\mathrm{r}}=\sum_{t=0}^{t=t-1} \frac{\boldsymbol{H}_{\mathrm{l}, t, 1} \cdot \boldsymbol{H}_{\mathrm{l}, t, 2}}{\sum \boldsymbol{H}_{\mathrm{l}, t, 2}}
$$

After obtaining the correction angle and correction depth, the initial correction value $\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor }}^{t}$ of the features of the uncertain object is calculated:

$$
\begin{gathered}
\boldsymbol{P}_{\mathrm{cor}, 1}^{\mathrm{a}}=\boldsymbol{P}_{1}^{\mathrm{b}}-l_{\mathrm{cor}} \\
\boldsymbol{P}_{\mathrm{cor}, 2}^{\mathrm{a}}=\tan \left(\delta_{\mathrm{cor}}\right) \cdot l_{\mathrm{cor}}+\boldsymbol{P}_{2}^{\mathrm{b}} \\
\boldsymbol{P}_{\mathrm{cor}}^{\mathrm{b}}=\boldsymbol{P}^{\mathrm{b}} \\
\boldsymbol{P}_{\mathrm{cor}, 1}^{\mathrm{c}}=\boldsymbol{P}_{1}^{\mathrm{b}}-l_{\mathrm{cor}} \\
\boldsymbol{P}_{\mathrm{cor}, 2}^{\mathrm{c}}=-\tan \left(\delta_{\mathrm{cor}}\right) \cdot l_{\mathrm{cor}}+\boldsymbol{P}_{2}^{\mathrm{c}} \\
\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor }}^{t}=\left[\begin{array}{lll}
\boldsymbol{P}_{\mathrm{cor}}^{\mathrm{a}} & \boldsymbol{P}_{\mathrm{cor}}^{\mathrm{b}} & \boldsymbol{P}_{\mathrm{cor}}^{\mathrm{c}}
\end{array}\right]
\end{gathered}
$$

(2) Inertia thinking correction method

Human tactile perception is an iterative process of recognition-decision-correction. In this part, the features of the uncertain object will be corrected based on the result of the fused decision and the sensor information. For the sake of correcting the estimated features of the uncertain object, a novel method is proposed based on inertial thinking in the following.

Rule 1: When the robot moves towards the target position, the end of the robot should gradually approach the target position,

$$
\left\{\begin{array}{l}
\gamma=\left(\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor }, 3}^{t}-\boldsymbol{X}_{\text {end }, 1}^{t}\right)-\left(\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}-\boldsymbol{X}_{\text {end }, 1}^{t}\right) \leq 0 \\
\hat{\boldsymbol{X}}_{\text {end }, 1}^{t} \geq 0
\end{array}\right.
$$

If $\gamma \geq 0 \cup \hat{\boldsymbol{X}}_{\text {end }, 1}^{t} \geq 0$, it is necessary to correct the target position of the uncertain object based on rules of inertial thinking and the estimated target position at the current moment should be the target position at the previous moment, that is $\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor2,3 }}^{t}=\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}$. Otherwise, there is no need to correct again, that is, $\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor2,3 }}^{t}=\hat{\boldsymbol{X}}_{\mathrm{d}, \text { cor,3 }}^{t}$. However, when the end of the robot reaches the target position but still has not completed the task (Equation (51), the

judgment method is given in the next section), the estimated target position of the uncertain object will shift toward the forward direction of the robot, that is, add a positive parameter.

$$
\left\{\begin{array}{l}
\text { unfinish } \\
\boldsymbol{e}_{\mathrm{end}, \mathrm{I}}^{\mathrm{t}} \leq \varsigma
\end{array}\right.
$$

where $\boldsymbol{e}_{\text {end }}^{\mathrm{t}}$ is the distance between the end position of the robot and the estimated target position. $\varsigma$ is the threshold.

In the process of exploration, if humans perceive a collision, they will explore in the opposite direction.

Rule 2: If the end of the robot collides with $\overrightarrow{A B}$, the robot is expected to move away from $\overrightarrow{A B}$; if the end of the robot collides with $\overrightarrow{C D}$, the robot is expected to move away from $\overrightarrow{C D}$.

The end of the robot collides with $\overrightarrow{A B}$,

$$
\begin{cases}\boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{b}}=\tan \left(\delta_{\mathrm{cor}}\right) \cdot\left(\hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t}-\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}\right)+\boldsymbol{P}_{\mathrm{cor}, 2}^{\mathrm{b}}-\varepsilon, & \hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t}<\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1} \\ \boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{b}}=-\tan \left(\delta_{\mathrm{cor}}\right) \cdot\left(\hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t}-\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}\right)+\boldsymbol{P}_{\mathrm{cor}, 2}^{\mathrm{b}}, & \hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t} \geq \hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}\end{cases}
$$

The end of the robot collides with $\overrightarrow{C D}$,

$$
\begin{cases}\boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{b}}=-\tan \left(\delta_{\mathrm{cor}}\right) \cdot\left(\hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t}-\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}\right)+\boldsymbol{P}_{\mathrm{cor}, 2}^{\mathrm{b}}+\varepsilon, & \hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t}>\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1} \\ \boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{b}}=\tan \left(\delta_{\mathrm{cor}}\right) \cdot\left(\hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t}-\hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}\right)+\boldsymbol{P}_{\mathrm{cor}, 2}^{\mathrm{b}}, & \hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor}, 3}^{t} \leq \hat{\boldsymbol{X}}_{\mathrm{d}, 3}^{t-1}\end{cases}
$$

where $\varepsilon$ is a constant positive parameter added to strictly ensure that the requirements of Rule 2 are met.

$$
\begin{gathered}
\boldsymbol{P}_{\mathrm{cor} 2,1}^{\mathrm{a}}=\boldsymbol{P}_{\mathrm{cor} 2,1}^{\mathrm{b}}-l_{\mathrm{cor}} \\
\boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{a}}=\tan \left(\delta_{\mathrm{cor}}\right) \cdot l_{\mathrm{cor}}+\boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{b}} \\
\boldsymbol{P}_{\mathrm{cor} 2,1}^{\mathrm{c}}=\boldsymbol{P}_{\mathrm{cor} 2,1}^{\mathrm{b}}-l_{\mathrm{cor}} \\
\boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{c}}=-\tan \left(\delta_{\mathrm{cor}}\right) \cdot l_{\mathrm{cor}}+\boldsymbol{P}_{\mathrm{cor} 2,2}^{\mathrm{c}} \\
\boldsymbol{\mu}_{z}^{t}=\hat{\boldsymbol{X}}_{\mathrm{d}, \mathrm{cor} 2}^{t}=\left[\begin{array}{ll}
\boldsymbol{P}_{\mathrm{cor} 2}^{\mathrm{a}} & \boldsymbol{P}_{\mathrm{cor} 2}^{\mathrm{b}} \quad \boldsymbol{P}_{\mathrm{cor} 2}^{\mathrm{c}}
\end{array}\right] \\
\boldsymbol{X}_{\mathrm{e}}^{t}=\boldsymbol{P}_{\mathrm{cor} 2}^{\mathrm{b}}
\end{gathered}
$$

After the correction is completed, $\boldsymbol{\mu}_{z}^{t}$ and $\boldsymbol{X}_{\mathrm{e}}^{t}$ are sent to the multi-sensor perception strategy part and the robot, respectively, $\boldsymbol{\mu}_{z}^{t}$ is used to estimate the features of the uncertain object next time and $\boldsymbol{X}_{\mathrm{e}}^{t}$ is used to update the desired target position of the control section.

# 3.2. Fusion Decision Based on D-S Theory 

As shown in Figure 7, the information of position and force is used to jointly decide the subsequent operation of the robot, based on the different information of position and force generated in different task progress stages. For example, the contact force during the task is lower than the one after the task is completed in general. In addition, the direction of the contact force is also different. The contact force during the task should be directed to the internal friction of the cone $\hat{\boldsymbol{c}}_{i}^{t}$, while the task is completed on the contrary. Ideally, the direction of the contact force should coincide with the end direction.

![img-6.jpeg](img-6.jpeg)

Figure 7. The force of the robot generated in different task progress stages.
The D-S theory is used to analyze the position information provided by the robot and the force information provided by the force sensor. This fusion decision strategy provides a mechanism to represent and process the uncertainty from robots and force sensors. Moreover, Dempster's combination rules [26] are used to fuse information from different sources.

First, the recognition framework $\Theta$ is defined as:

$$
\Theta=\{\text { Finish, Unfinish }\}
$$

The main elements of the recognition framework, $2^{\Theta}$, are defined as:

$$
\Omega=\{\{\text { Finish }\},\{\text { Unfinish }\},\{\text { Finish, Unfinish }\}\}
$$

where $\{$ Finish, Unfinish $\}$ represents the uncertain assumption in D-S theory. $\{$ Finish $\}$ and \{Unfinish\} represent the thresholds of the two hypotheses, respectively.

Next, the basic probability assignment (BPA) of different categories to which different information sources belong is calculated. In the method in this paper, the fuzzy naive Bayes method is used to generate BPA for each category and assign it to D-S theory. Let $V_{i}{ }^{j}$ be the eigenvalue vector collected by each information source, where $i$ represents the $i$-dimensional independent feature variable and $j$ represents different information sources. For the position information source, $V_{i}$ is the position error in each direction. For the force information source, $V_{i}$ is the magnitude and direction of the contact force. $\mathrm{W} \in \boldsymbol{C}=\left\{C_{1}, C_{2}, \cdots, C_{N}\right\}$ is defined as the classification label corresponding to $V_{i}$. In order to determine the BPA, the fuzzy naive Bayes method is used to determine the conditional probability and assign it to the basic probability used in the D-S theory,

$$
\mathrm{m}\left(C_{i}\right)=\mu_{C_{i}}\left(V^{j}\right)
$$

where $C_{i} \in\{\{$ Finish $\},\{$ Unfinish $\}\}$.
According to D-S theory, there is a compound hypothesis that an object may belong to both $\{$ Finish $\}$ and $\{$ Unfinish $\}$. Therefore, the operator $\wedge$ is used to assign the basic probability of $\{$ Finish, Unfinish $\}$,

$$
\mathrm{m}(\{\text { Finish, Unfinish }\})=\mu_{\{\text {Finish,Unfinish }\}}\left(V^{j}\right)=\mu_{\{\text {Finish }\}}\left(V^{j}\right) \wedge \mu_{\{\text {Unfinish }\}}\left(V^{j}\right)
$$

where $\wedge$ is the minimum t-norm operation. Moreover, the purpose of normalizing the BPA solved above is to ensure the effectiveness of BPA,

$$
\begin{gathered}
m\left(C_{i}\right)=\frac{\mu_{C_{i}}\left(V^{j}\right)}{L} \\
m(\{\text { Finish, Unfinish }\})=\frac{\mu_{\{\text {Finish,Unfinish }\}}\left(V^{j}\right)}{L} \\
L=\mathrm{m}\left(C_{i}\right)+\mathrm{m}(\{\text { Finish, Unfinish }\})
\end{gathered}
$$

where $L$ is the normalization factor. BPA generated by different information sources can be obtained through the above methods. Then, Dempster's combination rule is used to integrate the above BPA to obtain the overall BPA. Let $m_{1}$ and $m_{2}$ be the evidence provided by two independent information sources. In the framework of evidence theory, Dempster's combination rule is expressed as $m=m_{1} \oplus m_{2}$. The calculation method is as follows:

$$
m(A)=m_{1} \oplus m_{2}(A)=\frac{1}{1-\kappa} m_{\wedge}(A)
$$

where $A \in \Omega, A \neq \varnothing, m_{\wedge}(A)$ represents the sum of BPA products whose intersection with the subset is not an empty set,

$$
m_{\wedge}(A)=\sum_{A_{1} \cap A_{2}=A} m_{1}\left(A_{1}\right) m_{2}\left(A_{2}\right)
$$

where $\kappa$ is the degree of conflict between evidence. The greater the degree of inconsistency between the information, the closer $\kappa$ will be to 1 . The sum of BPA products whose intersection is an empty set.

$$
\kappa=\sum_{A_{1} \cap A_{2}=\varnothing} m_{1}\left(A_{1}\right) m_{2}\left(A_{2}\right)
$$

where $1-\kappa$ can be understood as a normalization factor.
For systems with multiple information sources, the overall BPA, $m_{\text {all }}$, can be expressed as:

$$
m_{\mathrm{all}}=m_{1} \oplus m_{2} \oplus \cdots \oplus m_{j}
$$

After the fusion is completed, the entire decision-making process has changed from multiple information sources to single information source decision-making. Choose the hypothesis with the greatest probability as the predicted category of the sample in the test data. Finally, the result of the task assessment $\xi$ and its BPA are obtained, where $\xi$ is 0 or 1 . 1 represents $\{$ Finish $\}, 0$ represents $\{$ Unfinish $\}$.

# 4. Design of Control System 

### 4.1. Dynamics Model

The n-degree-of-freedom robot dynamics are:

$$
\boldsymbol{M}(\boldsymbol{q}) \ddot{\boldsymbol{q}}+\boldsymbol{C}(\boldsymbol{q}, \dot{\boldsymbol{q}}) \dot{\boldsymbol{q}}+\boldsymbol{G}(\boldsymbol{q})+\boldsymbol{D}(\boldsymbol{q})+\boldsymbol{J}^{\mathrm{T}} \boldsymbol{F}_{\mathrm{e}}=\boldsymbol{\tau}
$$

where $\boldsymbol{M}(\boldsymbol{q}) \in \mathbf{R}^{\mathrm{n} \times \mathrm{n}}$ is a symmetric positive definite inertia matrix, $\boldsymbol{C}(\boldsymbol{q}, \dot{\boldsymbol{q}}) \in \mathbf{R}^{\mathrm{n} \times \mathrm{n}}$ is the Coriolis force and centrifugal force matrix, $\boldsymbol{G}(\boldsymbol{q}) \in \mathbf{R}^{\mathrm{n}}$ is the gravity vector, $\boldsymbol{D}(\boldsymbol{q}) \in \mathbf{R}^{\mathrm{n}}$ is the friction torque matrix generated by the clearance. $\boldsymbol{q} \in \mathbf{R}^{\mathrm{n}}, \dot{\boldsymbol{q}} \in \mathbf{R}^{\mathrm{n}}$ and $\ddot{\boldsymbol{q}} \in \mathbf{R}^{\mathrm{n}}$ is the position, velocity and acceleration of the robot in the joint space, respectively, obtained by the robot joint encoder. $\boldsymbol{J} \in \mathbf{R}^{\mathrm{n} \times \mathrm{m}}$ is the Jacobian matrix. $\boldsymbol{F}_{\mathrm{e}} \in \mathbf{R}^{\mathrm{m}}$ is the contact force vector at the end of the robot, which is collected by the six-dimensional force/torque sensor at the robotic end. $\boldsymbol{\tau} \in \mathbf{R}^{\mathrm{n}}$ is the joint torque. It is worth noting that, $\boldsymbol{M}(\boldsymbol{q}), \boldsymbol{C}(\boldsymbol{q}, \dot{\boldsymbol{q}})$ and $\boldsymbol{G}(\boldsymbol{q})$ are all unknown.

The above formula is rewritten into Cartesian coordinate form as:

$$
\boldsymbol{M}(\dot{q}) \boldsymbol{J}^{\mathrm{T}}\left(\ddot{\boldsymbol{X}}_{\mathrm{end}}-\ddot{\boldsymbol{J}} \dot{\boldsymbol{q}}\right)+\boldsymbol{C}(\boldsymbol{q}, \dot{\boldsymbol{q}}) \boldsymbol{J}^{\mathrm{T}} \dot{\boldsymbol{X}}_{\mathrm{end}}+\boldsymbol{G}(\boldsymbol{q})+\boldsymbol{D}(\boldsymbol{q})+\boldsymbol{J}^{\mathrm{T}} \boldsymbol{F}_{\mathrm{e}}=\boldsymbol{\tau}
$$

where $\boldsymbol{J}^{\mathrm{T}}=\boldsymbol{J}^{\mathrm{T}}\left(\boldsymbol{J J}^{\mathrm{T}}\right)^{-1}$ is the pseudo-inverse matrix of the Jacobian matrix. $\boldsymbol{X}_{\text {end }} \in \mathbf{R}^{\mathrm{m}}$, $\boldsymbol{X}_{\text {end }} \in \mathbf{R}^{\mathrm{m}}$ and $\dot{\boldsymbol{X}}_{\text {end }} \in \mathbf{R}^{\mathrm{m}}$ are the end position, velocity and acceleration of the Cartesian space robot, respectively. It is particularly noted that the robot and the operating tool are considered as a whole and thus the robotic end is defined as the end of the operating tool.

Rewrite the above formula further:

$$
\stackrel{-}{M} \boldsymbol{J}^{\dagger}\left(\hat{\boldsymbol{X}}_{\text {end }}+\Delta f\right)+\boldsymbol{J}^{\dagger} \boldsymbol{F}_{\mathrm{e}}=\boldsymbol{\tau}
$$

where $\stackrel{-}{M}$ is the estimated value of the inertia matrix $M(q) . \Delta f$ is uncertain terms, which can be expressed as:

$$
\Delta f=\boldsymbol{J} \stackrel{-\dagger}{M}\left((M(q)-\stackrel{-}{M}) \boldsymbol{J}^{\dagger} \hat{\boldsymbol{X}}_{\text {end }}-M(q) \hat{\boldsymbol{J}} \ddot{\boldsymbol{q}}+\boldsymbol{C}(\boldsymbol{q}, \ddot{\boldsymbol{q}}) \boldsymbol{J}^{\dagger} \hat{\boldsymbol{X}}_{\text {end }}+\boldsymbol{G}(\boldsymbol{q})+\boldsymbol{D}(\boldsymbol{q})\right)
$$

# 4.2. Control System Designed with MSP 

In this part, the uncertain of the robot model and the uncertain of the object are considered in the design of the robot controller. In the outer loop, the pliability model is introduced and combined with a multi-sensor perception strategy to perceive the object and provide a command position $X_{c}$ for the inner loop. In the inner loop, sliding mode control is used to solve the influence of robot model errors (only used in simulation). The control system diagram is shown in Figure 8. It is worth noting that the sliding mode compensation term (yellow box in Figure 8) is only used in the simulation, while in the experiments the robot receives the command positions provided by the flexibility model directly. The sliding mode compensation term is introduced to reduce the impact of errors of the robot model established in Section 4.1 on the strategy validation.
![img-7.jpeg](img-7.jpeg)

Figure 8. Control system designed with MSP.
The pliability model is:

$$
M_{\mathrm{d}}\left(\hat{X}_{\mathrm{e}}-\hat{X}_{\mathrm{c}}\right)+B_{\mathrm{d}}\left(\hat{X}_{\mathrm{e}}-\hat{X}_{\mathrm{c}}\right)+K_{\mathrm{d}}\left(X_{\mathrm{e}}-X_{\mathrm{c}}\right)=F_{\mathrm{d}}-F_{\mathrm{e}}
$$

where $M_{\mathrm{d}}, B_{\mathrm{d}}$ and $K_{\mathrm{d}}$ are the inertia matrix, damping matrix and stiffness matrix required by the impedance model, respectively, and they are positive definite diagonal matrices. $X_{e}$ is the desired target position in Cartesian space, which is given by the perception strategy in the previous Section 3. $\hat{X}_{e}$ and $\hat{X}_{e}$ are the desired velocity and acceleration in Cartesian space, respectively, which can be calculated by $\boldsymbol{X}_{\mathrm{e}} \cdot \boldsymbol{F}_{\mathrm{d}}$ is the desired contact force. Rewrite the above formula:

$$
M_{\mathrm{d}} \hat{X}_{\mathrm{c}}+B_{\mathrm{d}} \hat{X}_{\mathrm{c}}+K_{\mathrm{d}} X_{\mathrm{c}}=\boldsymbol{F}_{\mathrm{e}}-\boldsymbol{F}_{\mathrm{d}}+M_{\mathrm{d}} \hat{X}_{\mathrm{e}}+B_{\mathrm{d}} \hat{X}_{\mathrm{e}}+K_{\mathrm{d}} X_{\mathrm{e}}
$$

among them, $X_{\mathrm{e}}(0)=X_{\mathrm{c}}(0)$ and $\dot{X}_{\mathrm{e}}(0)=\dot{X}_{\mathrm{c}}(0)$. The command position and command acceleration can be obtained from the command speed.

The position error is defined as:

$$
e=X_{\mathrm{c}}-X_{\text {end }}
$$

Sliding mode is defined as:

$$
\boldsymbol{S}=\dot{\boldsymbol{e}}+\lambda \boldsymbol{e}
$$

where $\lambda$ is a positive definite constant matrix.
The robot reference state is defined as:

$$
\ddot{\boldsymbol{X}}_{\mathrm{r}}=\ddot{\boldsymbol{X}}_{\mathrm{c}}+\lambda \dot{\boldsymbol{e}}
$$

The controller can be designed as:

$$
\boldsymbol{\tau}=\overline{\boldsymbol{M}} \boldsymbol{J}^{\dagger}\left(\ddot{\boldsymbol{X}}_{\mathrm{r}}+\mathrm{A} \boldsymbol{S}+\mathrm{K}^{\prime} \operatorname{sign}(\boldsymbol{S})\right)+\boldsymbol{J}^{\dagger} \boldsymbol{F}_{\mathrm{e}}
$$

# 5. Simulation and Experimental Results 

Simulation and physical robot task experiments are designed for the narrow uncertain object. The proposed whole solution scheme is evaluated in terms of intelligence, autonomy and safety. (1) accuracy of interactive exploration for the features of the uncertain object $X_{\mathrm{d}}$ (intelligence); (2) correctness of fusion decision for task completion judgments (autonomy) and (3) comparative experiments to assess the safety of the entire solution scheme for robotic autonomy operations (safety).

### 5.1. Simulation Studies

### 5.1.1. Simulation Settings

Let $\mathrm{n}=4$ in Equation (57). The complete simulation model is established based on the robot dynamics model and control system in Section 4. In the simulation, the basic parameters used in the control system are as follows.

Impedance coefficient:

$$
\begin{gathered}
M_{\mathrm{d}}=\operatorname{diag}([0.0000001,0.0000001]) \\
\boldsymbol{B}_{\mathrm{d}}=\operatorname{diag}([5.05,5.05]) \\
\boldsymbol{K}_{\mathrm{d}}=\operatorname{diag}([1500,1500])
\end{gathered}
$$

Sliding mode parameters:

$$
\begin{gathered}
\lambda=\operatorname{diag}([50000,50000]) \\
\mathrm{A}=\operatorname{diag}([20,20]) \\
\hat{\mathrm{K}}=7000
\end{gathered}
$$

Inertial matrix estimates:

$$
\bar{M}=\operatorname{diag}([0.005,0.0015,0.0015,0.01])
$$

In the simulation, the initial position of the robot is set near the operation object (i.e., there is visual occlusion). The initial features of the uncertain object are given and are in error with the expected value. Since the estimates of our method are based on the previous moment's ones each time, the range of applicability of interactive exploration can be tested by adjusting the initial error. Considering that the entire operating object should be stabilized after the task is completed, the preload force is introduced and was set to 5 N .

### 5.1.2. Intelligibility Evaluation

We give the initial features of the uncertain object, and the errors of these features (target position) from the expected values are $-0.8 \mathrm{~mm},-3 \mathrm{~mm}, 0,3 \mathrm{~mm}$ and 10 mm , respectively. As can be seen from Figure 9, the accuracy of estimated values improves with the increasing number of explorations. The final error is less than 1 mm . Therefore, it can be concluded that force-tactile exploration can estimate the target position of the uncertain object.

![img-8.jpeg](img-8.jpeg)

Figure 9. Estimation error of the target position of the uncertain object.
In addition, to verify the advantages of the proposed method in terms of estimation accuracy, we also evaluate the MAC and ITC methods. The simulation results of MAC are represented in Figure 10, where Figure 10a shows the simulation results of MAC (angle) and Figure 10b shows the simulation results of MAC (depth). Since features of the true object are uncertain, we consider the reference eigenvalues as the baseline. When one of the original estimated angle features is close to the reference angle, the original estimated angle feature is corrected to the closer one by MAC, as shown in Figure 10a. When none of the original estimated depth features is close to the reference eigenvalue, the original estimated depth feature is corrected for the reference depth by MAC, as shown in Figure 10b. We can arrive at a conclusion that the MAC method keeps the estimated shape features (depth and angle) of the uncertain object more accurately by historical data.
![img-9.jpeg](img-9.jpeg)

Figure 10. Simulation results of MAC. (a) simulation results of MAC (angle) and (b) simulation results of MAC (depth).
In Figure 11, the robot collides with BC at this time. In Figure 11a, the feature (target position) of the uncertain object at the current moment estimated by the MAC is located at

the lower right of the estimated target position of the uncertain object at the last moment. After the ITC, the target position of the uncertain object, which is corrected by the MAC, at the current moment slides along the direction $\overrightarrow{B A}$ to near the inertial position. In Figure 11b, The target position feature of the uncertain object at the current moment estimated by the MAC is located at the upper right of the estimated target position of the uncertain object at the last moment. After the ITC, the target position of the uncertain object, which is corrected by the MAC, at the current moment slides along the direction $\overrightarrow{B C}$ to near the inertial target position, due to the presence of $\varepsilon$, which aims to make the robot conform to the collision-avoidance inertial response.
![img-10.jpeg](img-10.jpeg)

Figure 11. Simulation results of ITC. (a) result 1 and (b) result 2.
During the ITC design stage, we consider four possible scenarios that can cause inaccurate estimation (only three scenarios have appeared in the results of many simulations so far). Moreover, with the introduction of the ITC, the estimation results of the interactive exploration method are more accurate. Therefore, the validity of the design in this paper was verified.

# 5.1.3. Autonomy Evaluation 

The fusion decision results can be viewed as a classification of the current task progress (finished and unfinished). Therefore, the confusion matrix is proposed to evaluate the performance of the fusion decision strategy. As shown in Figure 12, each row of the confusion matrix represents a real result (finished and unfinished) and each column represents the result of the fusion decision. Six simulation studies are selected for analysis, containing the results of 86 decisions. In 86 results, the number of finished is 6 and the number of unfinished is 80 . The number on the box indicates the percentage of the result of all decisions. Since each task can have only one result of finished, we count the results of 86 decisions and calculate the percentages according to completion and unfinished, respectively, to represent all results in the range $[0,1]$. As expected, the diagonal values of the confusion matrix are high, which indicates that the strategy has a high truth rate.

![img-11.jpeg](img-11.jpeg)

Figure 12. Confusion matrix for fusing decision results.

# 5.1.4. Safety Evaluation 

Figure 13 shows that the contact force between the robot and the object under the control of the designed solution scheme is less than 10 N , which satisfies the requirement of pliability and safety. In addition, the preload force of the robot in completing the task meets the design requirements (red marker), which proves that the task is qualified. In overview, the control system meets the requirements for contact forces presented in Section 2.
![img-12.jpeg](img-12.jpeg)

Figure 13. Contact force at the end of the robot.
The result in Figure 14 shows that the proposed system can control the robot to reach the target position of the task with an error of less than 0.5 mm . We can also observe that the robot undergoes an abrupt displacement (represented as a circle in the $y$-direction), which is caused by the large change in the target position of the uncertain object estimated twice. Sudden displacement is within 1 mm due to the combined efforts of fusion decision results and impedance control. The later motion trajectory is smoother because the change in position between two adjacent estimates became smaller.

![img-13.jpeg](img-13.jpeg)

Figure 14. Robot position tracking error.

# 5.2. Experimental Studies 

### 5.2.1. Experimental Settings

To further validate the performance of the proposed strategy in more complex and uncertain objects, a peg-in-hole experiment with dynamic effects is designed, and the experimental equipment is shown in Figure 15a. The experimental system consists of the UR3 robot, operating tools, simulation components (operating objects), a six-degree-of-freedom parallel movement platform, and a console. Among them, the six-degree-of-freedom parallel movement platform, which introduces uncertainty for the operating object, is used to increase the difficulty of the task position. The simulation component is fixed on the movement platform. The amplitude and frequency of the movement platform are set according to the simulation parameters and results. An omnidirectional depth camera Kinect2 is utilized to collect the features of the simulated component. The experimental code is written in python. The conversion of the coordinate system between each experimental equipment was determined before the experiment and unify with the model. The movement platform parameters are set as follows, $x=A \sin (, 2 \pi f t), A=1 \sim 3 \mathrm{~mm}$, $f=1 \sim 5 \mathrm{~Hz}$. The direction of motion of the platform is x -direction. A total of 75 insertion experiments are tested in the experiment. The preload force is set to 5 N .
![img-14.jpeg](img-14.jpeg)

Figure 15. Experimental equipment. (a) Experimental equipment, (b) Operation tool 1 and operation object 1, (c) Operation tool 2 and operation object 2.

Two sets of workpieces (operating tools and simulation components) are used in the experiment to verify the versatility of the proposed method for different workpieces. As shown in Figure 15b,c, there is a greater dimensional difference in the tools and objects of workpiece 2 compared to workpiece 1. Their basic sizes are as follows.

Operation tool 1: full length is 176 mm , diameter of bottom end is 20 mm , diameter of top end is 40 mm , tilt angle $\delta_{\mathrm{e}}$ is 0.12 rad .

Operation object 1: hole deep is 80 mm , hole diameter of bottom end is 20 mm , hole diameter of top end is 40 mm , and tilt angle $\delta_{\mathrm{e}}$ is 0.12 rad .

Operation tool 2: full length is 197 mm , diameter of bottom end is 19 mm , diameter of top end is 13 mm , tilt angle $\delta_{\mathrm{e}}$ is 0.1 rad .

Operation object 2: hole deep is 32 mm , hole diameter of bottom end is 13 mm , hole diameter of top end is 20 mm , and tilt angle $\delta_{\mathrm{e}}$ is 0.11 rad .

In the experiment, the basic parameters used in the control system are as follows.
Impedance coefficient:

$$
\begin{gathered}
M_{\mathrm{d}}=\operatorname{diag}([0.2,0.2,0.2]) \\
B_{\mathrm{d}}=\operatorname{diag}([101,101,101]) \\
K_{\mathrm{d}}=\operatorname{diag}([300,300])
\end{gathered}
$$

Figure 16 illustrates an example of a robot performing a peg-in-hole task in the uncertain object. The example shows the adaptation of the robotic motion during the dynamic effects of the uncertain object in operation and the update of the target position of the uncertain object. The green dashed line indicates the robotic operation trajectory. In Figure 16a, the perception strategy guides the robot to start the assembly. At this time, the visual information (blue dashed line) is weighted higher due to the non-existence of visual occlusion (the distance between the robot and the simulated component is greater than $d_{v}$ ). In Figure 16b, the perception strategy guides the robot to assemble inside the operating object. At this time, the tactile information is weighted higher while the visual information is weighted lower, due to the visual occlusion (the distance between the robot and the simulated component is less than $d_{v}$ ). The simulation component is in dynamic effects and the robot adjusted its motion accordingly, updating the target position by interactive exploration. In Figure 16c fusion decision is triggered and the result is Unfinish. In Figure 16d fusion decision is triggered and the result is Finish.
![img-15.jpeg](img-15.jpeg)

Figure 16. Snapshot of the robot peg-in-hole operation in the uncertain object with dynamic effects. (a) starting assembly without visual occlusion, (b) assemble with visual occlusion, (c) decision: Unfinish and (d) decision: Finish.

# 5.2.2. Autonomy Evaluation 

We first show the result of the fusion decision by the position and force on the end of the robot with the finished and unfinished operation, as shown in Figure 16c,d. Due to visual occlusion, the interior is not known. It is obvious that the right side operating tool has fully entered the simulation component from the outside, while the left side has only partially entered. From the collected position data, the distance between the robotic end position and the simulation component on the left side is 18 mm , while the right side is less than 1 mm . In addition, according to the data collected through the force/torque sensor, the direction of the contact force when the operation is finished is significantly different from that when the operation is unfinished. Combining the external observations with the collected data, we can find that the fusion decision turns out to be correct. It is indicated that the model we propose in the design of the fusion decision is correct. Moreover, the robot will continue to perform the task when the decision result is unfinished, and vice versa, it will stop the movement.

Some details are shown in Figure 17 to evaluate the quality of the operation. We observe from the front and side, respectively, that the operating tool is very tightly fitted to the simulation component (red circles). At the end of the experiment, we try to pull the operating tool out of the simulated component, which requires a force of approximately more than 10 N . It further indicates that the fusion decision is correct. Comparing Figure 17a,b, when using workpiece 2 for the experiment, there is a large clearance after the task is completed. It is caused by the difference in the size of operation tool 2 and operation object 2 . Nevertheless, the proposed method can still guide the robot to complete the task. It also demonstrates the versatility of the method for different workpieces and reduces the workload of the operator which does not require the operator to modify the parameters after each workpiece change.
![img-16.jpeg](img-16.jpeg)

Figure 17. Detail at finished operation. (a) operation tool 1 and operation object 1, (b) operation tool 2 and operation object 2 .

As shown in Figure 18, we count the results of 55 decisions and calculate the percentages according to finished and unfinished, respectively, to represent all results in the range $[0,1]$. For the incorrect results, we find the reason for the decision error, one source of information with evidence showing a high probability of finished and the other showing a low probability of finished, which ultimately yields a low probability of finished. The problem can be solved by a threshold value of a higher probability of finished is set. The application of this strategy eliminates the need for the operator to check that the workpiece is securely mounted, which helps to reduce the workload.

![img-17.jpeg](img-17.jpeg)

Figure 18. Confusion matrix for fusing decision results. (a) operation tool 1 and operation object 1, (b) operation tool 2 and operation object 2.

### 5.2.3. Safety Evaluation

In this section, we conduct experiments on the proposed system under the dynamic effects conditions of *A* = 1 mm & *f* = 1 Hz, *A* = 2 mm & *f* = 1 Hz, *A* = 3 mm & *f* = 1 Hz and *A* = 1 mm & *f* = 5 Hz, as shown in Figure 19. In the experiments, we filter the contact force less than 2 N to counter the effect of measurement noise. The black dots in the figure represent the contact force generated by each collision, and the red dots represent the average value of the contact force for each experiment. As a whole, two workpieces of the mean contact forces are low, between 5 and 10 N, and the number of collisions is low, no more than 15 per experiment. It indicates that our solution scheme meets the requirement for safe operation for multiple types of dynamic effects. In Figure 19a, comparing orange, blue and yellow, we find that an increase in the amplitude of the dynamic effects causes a slight increase in the contact force, which also proves that the dynamic effects of the uncertain object affect the robot end operation.

![img-18.jpeg](img-18.jpeg)

Figure 19. Results of operation of robots with different dynamic effects. (a) operation tool 1 and operation object 1, (b) operation tool 2 and operation object 2.

In the previous experiment, we illustrated the generality of the proposed system in terms of safety. To verify the safety attributed to the proposed method, we compare the proposed system with two benchmark experiments: (1) guide operation by MSP only, without impedance control, and (2) variable impedance control only, without MSP. For each method, experiments are performed sequentially at three types of dynamic effects. As shown in Figure 20, we show the comparison results from the same dynamic effects, with one experiment for each method.

![img-19.jpeg](img-19.jpeg)

**Figure 20.** Results of operation of robots with different control methods.

(1) The maximum contact force (orange) is demonstrated using only MSP-guided operation without impedance control. This result is expected and indicates that a pliability model is needed to accomplish the operation task to minimize the contact force between the robot and the uncertain object. Although the target position is updated by MSP, it leads to large contact forces when guiding the robot movement, which is undesirable since the robot–object interaction is not considered.

(2) Variable impedance control is a classical approach to deal with the problem of robot interaction with an uncertain object, which adjusts the impedance parameters online by contact forces to accommodate the uncertain object with dynamic effects. The approach using variable impedance control only without MSP (green) presents multiple peaks, which means that the robot guided only by variable impedance without MSP may lead to frequent collisions and possibly even divergence during operation. Frequent collisions can also exacerbate dynamic effects.

(3) In summary, the proposed method (blue) demonstrates minimal contact forces and no multiple collisions. It indicates that the method proposed in this paper is effective.

### 6. Conclusions

In this paper, we focused on the issue of robotic autonomy operations in the real-world unstructured environment. Missing or inaccurate visual information was also considered due to confined space limitations and interference from complex environments. In order to satisfy the three requirements of intelligence, autonomy and safety, a multi-sensor perception strategy for the robot was proposed to achieve a humanoid autonomy operation process integrating exploration, decision and guidance with uncertain objects. In terms of intelligence, it was our goal to obtain information about the features of the uncertain object. An interactive exploration method using Bayesian networks was proposed to integrate multimodal information and accurately estimate the features of the uncertain object, which can comprehensively perceive the features of the uncertain object even in the presence of visual occlusion. The exploration approach was general for static objects and multiple dynamic objects. In terms of safety, the proposed system was capable of performing tasks under the uncertain object and minimizing the forces of interaction between the robot and the uncertain object. In terms of autonomy, the proposed fusion

decision strategy has enabled autonomous start-stop and guided subsequent operations of the robot, which could reduce the workload of the operators. Based on the D-S theory, the evidence information provided by multiple information sources was fused to judge the task progress, which gives the robot human-like decision-making capability. Moreover, the pliability model was combined with an MSP to reduce the interaction forces during operation. In general, the multi-sensor-based solution scheme showed fine performance for robotic operation tasks with both position and force requirements.

There is one more area where the proposed method could be improved. The inclusion of a pose adjustment strategy before the MSP will improve the generality of the method for pegs and holes with multiple angles. This attitude adjustment strategy performs a tilt-right-rotate-alignment process to bring the robotic end into an ideal attitude for operation.

Author Contributions: Conceptualization, L.Q.; writing—original draft preparation, L.Q. and H.W.; writing-review and editing, L.Q., H.W., Y.Y. and S.Q.; supervision, L.Q.; project administration, L.Q. and Y.Y.; funding acquisition, L.Q. and Y.Y. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the National Natural Science Foundation of China (51605415) and Natural Science Foundation of Hebei Province (F2016203494, F2015203362).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank the anonymous reviewers for their valuable suggestions.

Conflicts of Interest: The authors declare no conflict of interest.
