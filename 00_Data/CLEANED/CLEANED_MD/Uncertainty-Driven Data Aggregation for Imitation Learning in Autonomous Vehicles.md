# Article 

## Uncertainty-Driven Data Aggregation for Imitation Learning in Autonomous Vehicles

Changquan Wang ${ }^{1,2}$ (D) and Yun Wang ${ }^{1,2, *}$ (D)<br>check for updates<br>Citation: Wang, C.; Wang, Y.<br>Uncertainty-Driven Data Aggregation for Imitation Learning in Autonomous Vehicles. Information 2024, 15, 336. https://doi.org/10.3390/info15060336

Academic Editors: Antonio Comi, Jianbo Li and Junjie Pang

Received: 20 April 2024
Revised: 27 May 2024
Accepted: 3 June 2024
Published: 6 June 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https: / / creativecommons.org/licenses/by/ $4.0 /$ ).

1 Institute of Microelectronics of the Chinese Academy of Sciences, Beijing 100029, China; wangchangquan@ime.ac.cn
2 University of Chinese Academy of Sciences, Beijing 101408, China

* Correspondence: wangyun@ime.ac.cn

Abstract: Imitation learning has shown promise for autonomous driving, but suffers from covariate shift, where the policy performs poorly in unseen environments. DAgger is a popular approach that addresses this by leveraging expert demonstrations. However, DAgger's frequent visits to sub-optimal states can lead to several challenges. This paper proposes a novel DAgger framework that integrates Bayesian uncertainty estimation via mean field variational inference (MFVI) to address this issue. MFVI provides better-calibrated uncertainty estimates compared to prior methods. During training, the framework identifies both uncertain and critical states, querying the expert only for these states. This targeted data collection reduces the burden on the expert and improves data efficiency. Evaluations on the CARLA simulator demonstrate that our approach outperforms existing methods, highlighting the effectiveness of Bayesian uncertainty estimation and targeted data aggregation for imitation learning in autonomous driving.

Keywords: DAgger; Bayesian uncertainty estimation; Bayesian network; autonomous driving; critical scenes

## 1. Introduction

In recent years, end-to-end imitation learning has demonstrated significant potential for autonomous driving by learning a driving policy that directly maps sensory observations to control commands [1-5]. However, a primary challenge in imitation learning is the issue of covariate shift [6,7], which refers to the variation in the state distribution encountered by the policy. As shown in Figure 1a, policies quickly accumulate errors, leading to poor performance in new environments, a phenomenon known as the compounding error problem. Therefore, researchers have proposed data aggregation techniques for training robust policies. One such technique is DAgger [8], which iteratively improves a policy by combining the learner's experience with expert corrections. It is compared with imitation learning, as shown in Figure 1a. This approach has demonstrated its effectiveness in various robotic tasks. Several DAgger variants have been proposed: Q-DAgger [9] accelerates the learning process by incorporating a Q -function to estimate the value of each stateaction pair, guiding the algorithm to focus on more informative samples. AggreVaTe [10] introduces a reinforcement learning approach that learns a value function to minimize the cost incurred by the expert, reducing the burden on the expert during training. AggreVaTeD [11] extends AggreVaTe by employing a deep neural network to represent the value function, enabling the algorithm to handle high-dimensional state spaces and improve performance. MinDAgger [12] proposes an asynchronous variant of DAgger that allows for parallel data collection and aggregation, significantly reducing the sample complexity and training time. These DAgger variants aim to enhance the efficiency and practicality of imitation learning by addressing key challenges such as sample complexity [12], expert cost minimization [10], and policy performance optimization [9]. In the field of autonomous driving, one notable approach is DARB (DAgger with replay buffer) [13], which focuses

on critical states and incorporates a replay buffer, thereby achieving significant improvements in generalization performance for autonomous driving scenarios. Additionally, The Roach [14] algorithm propose a novel reinforcement learning agent as an "automated expert" for autonomous driving, outperforming existing methods and enabling effective DAgger to achieve expert-level performance.
![img-0.jpeg](img-0.jpeg)

Figure 1. (a) Imitation learning, an off-policy method, propagates errors early in the trajectory. In contrast, DAgger is an on-policy approach that integrates the expert's and the agent's control, requiring the expert to label unfavorable states visited by the agent's policy. The agent leverages this data iteratively to refine its own policy through multiple training iterations, progressively approaching the expert's policy. (b) We propose a modified version of DAgger with uncertainty estimate and critical scenes for improved driving in dense urban scenarios. In contrast to traditional DAgger algorithms, we employ a deep Bayesian uncertainty estimation method to determine whether a scene is extracted for retraining.

However, the DAgger algorithm's propensity to frequently visit suboptimal states can lead to several challenges, including increased expert burden, reduced data efficiency, degraded policy performance, and instability in the learning process. To address these issues, researchers have proposed various improvements to the algorithm. SafeDAgger introduces a safety policy that selectively queries expert labels, thereby reducing the reliance on experts and enhancing the efficiency and safety of data aggregation [15]. In contrast, DART injects noise during the data collection phase to generate perturbed trajectories that simulate the errors of the learning policy [16]. This data augmentation technique improves the robustness of the learning policy in suboptimal states. Both approaches alleviate the problem of frequent visitation to suboptimal states in the DAgger algorithm from different perspectives, ultimately enhancing the performance and efficiency of imitation learning. These algorithmic advancements demonstrate the ongoing efforts in the research community to address the limitations of the original DAgger algorithm and push the boundaries of imitation learning for real-world applications.

Furthermore, a growing number of researchers are utilizing Bayesian learning methodologies to tackle this problem. Bayesian approaches to the DAgger algorithm, such as EnsembleDAgger [17], DropoutDAgger [18], address the critical issue of quantifying uncertainty in the decision-making process of imitation learning. These Bayesian variants of DAgger aim to improve upon the original algorithm by providing a more nuanced understanding of the learning agent's confidence in its actions. EnsembleDAgger [17] leverages a collection of diverse models to form a committee that votes on the best action, integrating model variance as an implicit measure of uncertainty. DropoutDAgger [18] utilizes Monte Carlo dropout (MC-dropout) [19] within neural networks to approximate Bayesian inference, thus offering a practical way to estimate uncertainty by capturing the predictive variance in the network's output. BAgger [20], or Bayesian aggregation, incorporates explicit Bayesian methods to model the uncertainty of the policy's actions, often through probabilistic modeling techniques. By integrating these Bayesian concepts,

these algorithms enable the learning agent to make more informed decisions about when to defer to the expert, thereby potentially reducing the number of suboptimal actions taken and improving the overall performance of the system.

Closely related to our work, UAIL (uncertainty aware imitation learning) [21] proposed a DAgger-based learning algorithm that utilizes MC-dropout to estimate uncertainty in autonomous driving actions. This algorithm leverages uncertainty estimates during onpolicy data collection, allowing the learning agent to switch control at uncertain states and collect data targeted at corrective behaviors at the boundary of optimal and suboptimal states. However, MC-dropout often exhibits inaccurate predictions and high computational costs on large-scale datasets [22,23]. Furthermore, UAIL's implementation of DAgger lacks critical states and replay buffer techniques [13], which limits its overall effectiveness.

Imitation learning has shown promise for autonomous driving but suffers from covariate shift, where the policy performs poorly in unseen environments. DAgger is a popular approach that addresses this by leveraging expert demonstrations. However, DAgger's frequent visits to suboptimal states can lead to several challenges, such as increased expert burden, reduced data efficiency, degraded policy performance, and instability in the learning process.

To address these limitations, we propose a novel DAgger framework that integrates Bayesian uncertainty estimation via MFVI [24,25]. The architecture of the method is shown in Figure 1b. MFVI provides better-calibrated uncertainty estimates compared to prior methods, such as MC-dropout used in UAIL. The proposed algorithm consists of several key components: an uncertainty estimation module, a critical state identification process, and an expert querying mechanism. During training, the framework first uses MFVI to estimate the uncertainty of the agent's predictions. It then identifies both uncertain and critical statesthose states where the policy's performance is most uncertain or potentially suboptimal. The expert is queried only for these specific states, enabling a targeted data collection strategy. This approach not only reduces the burden on the expert but also improves data efficiency by focusing on the most informative samples. Evaluations on the CARLA simulator demonstrate that our approach outperforms existing methods, highlighting the effectiveness of Bayesian uncertainty estimation and targeted data aggregation for imitation learning in autonomous driving.

The key contributions of our work are as follows:

- We introduce a novel DAgger framework that synergistically integrates Bayesian uncertainty estimation via MFVI and critical state identification for improved imitation learning in autonomous driving.
- We demonstrate that MFVI provides better-calibrated uncertainty estimates compared to MC-dropout, leading to more effective data collection and improved driving performance.
- We conduct extensive evaluations on the CARLA simulator [26] using the NoCrash [27] and CARLA Leaderboard benchmarks [28], showing that our approach outperforms existing methods, such as CILRS (conditional imitation learning with ResNet and speed prediction) [27], DARB, and UAIL.

Our work advances imitation learning for autonomous driving by demonstrating the effectiveness of integrating Bayesian uncertainty estimation and targeted data aggregation. This makes it a direction with valuable insights for future work in this domain.

# 2. Background 

### 2.1. Imitation Learning

Imitation learning [29], also known as learning from demonstrations, is a form of machine learning in which an agent learns a policy $\pi$ from observed state-action pairs $\left(s_{i}, a_{i}\right)$, where the actions $a_{i}$ are provided by an expert policy $\pi_{E}$. The goal of the agent is to learn a policy that can imitate the expert policy, either by minimizing the difference between their actions or by maximizing the likelihood of actions taken by the expert. The learned policy can then be used to make decisions in new, unseen environments.

Formally, let $\mathcal{S}$ and $\mathcal{A}$ denote the state and action spaces, respectively. The expert policy $\pi_{E}: \mathcal{S} \rightarrow \mathcal{A}$ maps states to actions. The agent's goal is to learn a policy $\pi_{\theta}$ : $\mathcal{S} \rightarrow \mathcal{A}$, parameterized by $\theta$, that mimics the expert's behavior. Given a dataset of expert demonstrations $\mathcal{D}=\left(s_{i}, a_{i}\right)_{i=1}^{N}$, where $s_{i} \in \mathcal{S}$ and $a_{i} \in \mathcal{A}$, the objective of imitation learning can be formulated as:

$$
\min _{\theta} \mathbb{E}_{s \sim d_{\pi_{E}}}\left[L\left(\pi_{\theta}(s), \pi_{E}(s)\right)\right]
$$

where $d_{\pi_{E}}$ is the state distribution induced by the expert policy, and $L$ is a loss function that measures the dissimilarity between the actions taken by the learned policy and the expert policy.

# 2.2. DAgger 

DAgger stands for "Dataset Aggregation" and is a combination of supervised and reinforcement learning. It involves collecting a dataset of expert demonstrations and using this data to train a supervised learning model. The model is then used to perform the task, and the expert provides feedback to the model by correcting its errors. This feedback is then used to update the model, making it more accurate and better able to perform the task.

The key idea behind DAgger is to iteratively collect additional data from the states visited by the learned policy and have the expert provide labels for those states. By aggregating the new data with the existing dataset and retraining the policy, DAgger helps mitigate the distribution shift problem and improves the policy's performance. The overall workflow of the Dagger algorithm is outlined in Algorithm 1.

```
Algorithm 1 DAgger
    Collect initial dataset \(D_{0}\) using expert policy \(\pi^{*}\)
    Initialize dataset \(D \leftarrow D_{0}\)
    Train initial policy \(\hat{\pi}_{0}=\operatorname{argmin}_{\pi} \mathcal{L}\left(\pi, \pi^{*}, D_{0}\right)\)
    for \(i=1 N\) do
        Generate on-policy dataset \(D_{i}\) using \(\hat{\pi}_{i-1}\)
        Ask the expert \(\pi^{*}\) for labels for \(D_{i}\) to get \(D_{i}^{\prime}\)
        Aggregate datasets: \(D \leftarrow D \cup D_{i}^{\prime}\)
        Train policy \(\hat{\pi}_{i}=\operatorname{argmin}_{\pi} \mathcal{L}\left(\pi, \pi^{*}, D\right)\)
    end for
    return \(\hat{\pi}_{N}\)
```

In this formulation, $\mathcal{L}\left(\pi, \pi^{*}, D\right)$ represents the loss function that measures the difference between the actions predicted by the policy $\pi$ and the expert's actions $\pi$ on the dataset $D$. The specific choice of loss function depends on the problem domain and the type of actions being predicted (e.g., mean squared error for continuous actions, cross-entropy loss for discrete actions).

By iteratively collecting data from the learned policy, getting expert labels, and retraining the policy, DAgger effectively combines supervised learning and reinforcement learning to improve the policy's performance and generalization ability. The algorithm has been successfully applied in various domains, including robotics, autonomous driving, and game playing.

### 2.3. Bayesian Neural Networks and Inference

Deep Bayesian algorithms are a class of methods that combine Bayesian inference with deep learning to probabilistically model the weights of deep neural networks, thereby enabling the estimation of model uncertainty.

Let $f_{\theta}(x)$ denote a deep neural network, where $\theta$ represents the network weights and $x$ is the input. In the Bayesian framework, we treat the weights $\theta$ as random variables and model them with a prior distribution $p(\theta)$. Given a training dataset $\mathcal{D}=\left(x_{i}, y_{i}\right)_{i=1}^{N}$, our goal is to compute the posterior distribution $p(\theta \mid \mathcal{D})$. According to Bayes' theorem:

$$
p(\theta \mid \mathcal{D})=\frac{p(\mathcal{D} \mid \theta) p(\theta)}{p(\mathcal{D})} \propto p(\mathcal{D} \mid \theta) p(\theta)
$$

However, for deep neural networks, the posterior distribution $p(\theta \mid \mathcal{D})$ is often intractable. Therefore, we typically resort to approximate inference methods, such as variational inference (VI) [24] or Markov chain Monte Carlo (MCMC) [30], to approximate the posterior distribution.

Mean field variational inference (MFVI) [31]: MFVI approximates the true posterior distribution $p(\theta \mid \mathcal{D})$ with a simpler variational distribution $q_{\phi}(\theta)$, parameterized by $\phi$. The objective is to minimize the Kullback-Leibler (KL) divergence between $q_{\phi}(\theta)$ and $p(\theta \mid \mathcal{D})$, which is equivalent to maximizing the evidence lower bound (ELBO). The optimal variational parameters $\phi^{*}$ are obtained through optimization techniques such as gradient descent. Figure 2c illustrates the optimization process.

Monte Carlo dropout (MC-dropout) [19]: MC-dropout is a practical approach that interprets dropout regularization as an approximate Bayesian inference method. By enabling dropout during both training and testing phases, MC-dropout approximates the posterior distribution over the weights. Multiple forward passes with different dropout masks allow for the estimation of predictive uncertainty.

Deep Bayesian learning plays a pivotal role in enhancing the safety and reliability of autonomous vehicles by providing a probabilistic framework that can effectively handle uncertainty in perception [32,33,34], prediction [35], and decision-making tasks [36,37,38]. The integration of Bayesian inference with deep learning models allows for the quantification and propagation of uncertainty through various layers of the system, which is crucial for developing robust AVs that can operate in dynamic and unpredictable environments.
![img-1.jpeg](img-1.jpeg)

Figure 2. (a) The schematic representation of our imitation learning network and deep Bayesian network. They have the same latent space. In our imitation learning network, we employ the CILRS framework. Initially, an input image undergoes processing by a ResNet perception module, resulting in a latent space representation. Subsequently, two prediction heads are employed: one for controls and the other for speed. In our deep Bayesian network, the latent space serves as input for predicting the uncertainty associated with controls. This network comprises interconnected Bayesian neurons organized in layers, each potentially varying in activation functions, weight distributions, and bias distributions. (b) A Bayesian neuron, the mathematical operation involves an activation function, a distribution of weights w, and a distribution of biases b specific to that neuron. When processing inputs $x$, the network samples one instance of weights and biases from their respective distributions and applies the activation function accordingly. This approach allows for uncertainty estimation and robust modeling in neural networks. (c) The variational inference for analyzing the optimal posterior distribution $p(\theta \mid \mathcal{D})$ by estimating a relatively simpler distribution $q(\theta)$.

# 3. Method 

### 3.1. Imitation Learning for Autonomous Vehicles

Our proposed framework employs CILRS [27] as the imitation learning algorithm. CILRS is an end-to-end architecture specifically designed for autonomous driving. It extends the traditional behavior cloning approach by incorporating conditional imitation learning (CIL) [1], enabling it to effectively handle complex urban driving scenarios that demand nuanced navigational decisions.

As show in Figure 2a CILRS employs a CIL framework, which extends imitation learning cloning by incorporating high-level navigational commands to disambiguate actions in complex driving scenarios. The network structure consists of an input module that processes sensory observations, including single RGB images and ego vehicle speed, to capture the dynamic driving environment. This input is then fed into a deep neural network that simultaneously learns perception and control tasks. The architecture includes convolutional layers for feature extraction from the image data, followed by fully connected layers that integrate the high-level commands with the visual features to predict the vehicle's control parameters. This design allows the network to learn end-to-end policies capable of handling intricate driving maneuvers.

Consider a dataset of observation-action pairs $D\left(o_{i}, a_{i}\right)_{i=1}^{N}$, collected from expert policy. The goal of imitation learning is to learn a policy $\pi\left(o_{t}\right): O \rightarrow A$, which maps observations $o_{t}$ to actions $a_{t}$ at at every time step and imitates the behavior of an expert action:

$$
\text { IL : } \min _{\pi} \sum_{i}\left[\left(a_{t}, \pi\left(o_{i}\right)\right)\right]
$$

The policy is optimized by minimizing a distance L between the predicted action and the expert action, In our autonomous driving model, the output of the policy is a three-dimensional continuous action vector (steer, throttle, and brake). Specifically, we use a mean squared error (MSE) loss for training, which measures the average squared difference between the predicted actions and the expert actions. By minimizing this loss, the policy is trained to produce actions that closely match the expert's actions, thus effectively imitating the expert's behavior.

CIL add some high-level command c that can convey the planning module intent at test time. This command can guide the car's driving direction, thus avoiding multimodality behavior. For example, when the car is at the intersection, whether the car should turn left or right, or go straight. If tell the car a planning command c helps resolving the ambiguity. The training dataset becomes $D\left\{\left(o_{i}, c_{i}, a_{i}\right)\right\}_{i=1}^{N}$, High-level commands include three: turn left, turn right, and go straight. The command-conditional imitation learning objective can be written as

$$
\text { CIL : } \min _{\pi} \sum_{i}\left[\left(a_{t}, \pi\left(o_{i}, c_{i}\right)\right)\right]
$$

Imitation learning assumes that the data distribution is independently identically distributed, and imitation cannot accurately replicate the expert action. And because autonomous driving is a sequential decision-making problem, each errors will gradually accumulate. This causes the probability of accident to increase over time while the car is running. Another problem is that it is easy for the car to make mistakes if it encounters states that are not present in the expert data distribution. This problems can be solved using iterative on-policy algorithms such as DAgger, which we discuss next.

### 3.2. Mean Field Variational Inference

We constructed a deep Bayesian network to evaluate the uncertainty in end-to-end autonomous driving systems. As show in Figure 2a, the network's input is the feature output layer from the CILRS backbone network, while the output comprises the control actions along with their associated uncertainties. Mirroring the latter half of the CILRS architecture, each driving command module corresponds to a deep Bayesian network.

The network structure consists of six fully connected layers. The prior parameters for the Bayesian neural network (BNN) are initialized with a mean of 0.0 and a standard deviation of 1.0.

MFVI operates on the principle of approximating the complex posterior distribution $p(w \mid \mathcal{D})$ of the model parameters $w$, given the dataset $\mathcal{D}$, with a simpler variational distribution $q_{\lambda}(w)$. This variational distribution is typically factorized across the dimensions of $w$ to ease computations:

$$
q_{\lambda}(w)=\prod_{i=1}^{D} q_{\lambda_{i}}\left(w_{i}\right)
$$

where $D$ represents the dimensionality of $w$, and $\lambda=\left\{\lambda_{1}, \ldots, \lambda_{D}\right\}$ are the variational parameters we aim to optimize.

Within the framework of MFVI, the optimization objective is to approximate the intractable true posterior distribution $p(w \mid \mathcal{D})$ with a variational distribution $q_{\lambda}(w)$ that is more computationally feasible to handle. This approximation is achieved by minimizing the Kullback-Leibler (KL) divergence from $q_{\lambda}(w)$ to $p(w)$, which is a measure of the loss of information when $q_{\lambda}(w)$ is used to approximate $p(w)$. The KL divergence is given by the integral

$$
\mathrm{KL}\left[q_{\lambda}(w) \| p(w)\right]=\int q_{\lambda}(w) \log \frac{q_{\lambda}(w)}{p(w)} d w
$$

which quantifies the expected value of the logarithmic difference between $q_{\lambda}(w)$ and $p(w)$, calculated with respect to $q_{\lambda}(w)$.

The evidence lower bound (ELBO), which is formulated as:

$$
\mathcal{L}(\lambda)=\mathbb{E}_{q_{\lambda}(w)}[\log p(\mathcal{D} \mid w)]-\mathrm{KL}\left[q_{\lambda}(w) \| p(w)\right]
$$

here, the first term is the expected log-likelihood of the data given the parameters, indicating how well the model fits the data. The second term is the KL divergence, which provides regularization.

The loss function to be minimized is then defined as the negative ELBO:

$$
\mathcal{J}(\lambda)=-\mathcal{L}(\lambda)
$$

During inference, we employ Monte Carlo sampling to approximate the predictive distribution. Forward passes are performed through the network T times, each time sampling different weights $w \sim p(w \mid D)$ from the posterior distribution. The model output $a^{t}$ is computed for each sample $t$ as $a^{t}=f\left(x, w^{t}\right)$, where $f$ is the neural network mapping inputs $x$ to outputs $y$ given weights $w^{t}$. The outputs from the T samples are averaged to obtain the final prediction:

$$
a_{\text {pred }}=\frac{1}{T} \sum_{t=1}^{T} a^{(t)}
$$

by sampling multiple times with varying weights, we derive a robust prediction encompassing the full posterior $p(a \mid x, D)$.

Predictive uncertainty is quantified by calculating the predictive entropy of the output distribution over control actions $a$. The predictive entropy is then calculated as

$$
\sigma(a \mid x, D)=-\int p(a \mid x, D) \log p(a \mid x, D) d a
$$

where $a$ is the output (driving action), $x$ is the input, and $D$ is the training data. Predictive uncertainty captures the inherent noise and variability in the data.

Model uncertainty is quantified using mutual information. Mutual information captures the dependence between the output $a$ and the model parameters $\omega$ by measuring the reduction in uncertainty of $a$ when $\omega$ is known:

$$
\sigma(a, \omega \mid x, D)=H(a \mid x, D)-\mathbb{E}_{p(\omega \mid D)}[H(a \mid x, \omega)]
$$

A higher mutual information indicates the model is more uncertain about its own predictions.

Uncertainty quantification in BNNs provides valuable insights into the reliability of the model's predictions. By distinguishing between data uncertainty and model uncertainty, we can make safer and more informed decisions in the context of autonomous driving. Model uncertainty, which can be mitigated by incorporating sufficient data, is often quantified through stochastic forward passes using dropout. However, this approach is computationally expensive and not suitable for real-time applications. In this paper, we primarily focus on data uncertainty, which arises from the inherent noise or ambiguity present in the input data.

We leverage the data uncertainty present in the prediction of the driving policy to identify safe states. Consequently, the set of critical states, denoted as $\mathcal{S}_{\text {unsafe }}$, can be determined as a result of this process.

$$
\mathcal{S}_{\text {unsafe }}=\{s \in \mathcal{S} \mid \sigma(\mathrm{s})>\tau\}
$$

The selection of the safety threshold parameter $\tau$ is crucial in achieving a harmonious trade-off between ensuring safety and optimizing query efficiency.

# 3.3. Critical Scenes 

The DAgger algorithm appends the entire generated on policy trajectory to the training dataset for the current iteration. However, not all states present the same utility for the driving policy. Specifically, states that correspond to failure cases have maximum utility for accelerate the convergence of DAgger algorithm. On this basis, according to the characteristics of automatic driving tasks, the definition of key frames is introduced, so that the training strategy can be more focused on the driving task.

Scene-based: In the context of dense urban driving, tasks such as navigating intersections are deemed more critical than traveling straight on an empty road, as most collisions occur at intersections and during turning maneuvers. Additionally, collisions are prone to happen when pedestrians unexpectedly cross the road. Therefore, we define the following key scenarios: (1) intersection, (2) a turning scenario, and (3) pedestrians on the road. Consequently, we prioritize sampling these scenarios, where scenarios (1) and (2) align with the definitions provided by DAgger.

Safe time-based: The level of risk is mainly reflected by the interaction between the autonomous vehicle and objects in the scenario, which can be naturally described by the distance-a small distance means the risk of collision is high. This intuition can also be converted to other metrics such as time to collision (TTC) [39,40]. The TTC of a vehicledriver combination $i$ at instant $t$ with respect to a leading vehicle ${ }_{i-1}$ can be calculated with

$$
T T C_{i}=\frac{x_{i-1}(t)-x_{i}(t)-l_{i}}{\widehat{x}_{i}(t)-\hat{x}_{i-1}(t)}, \forall \widehat{x}_{i}(t)>\hat{x}_{i-1}(t)
$$

In this formula, $x_{i-1}(t)$ represents the position of the leading vehicle (vehicle ${ }_{i-1}$ ) at time $t$. Similarly, $x_{i}(t)$ denotes the position of the following vehicle (vehicle ${ }_{i}$ ) at the same time. The term $l_{i}$ specifies the length of the following vehicle (vehicle ${ }_{i}$ ). Additionally, $\widehat{x}_{i}(t)$ indicates the speed (or velocity) of the following vehicle (vehicle ${ }_{i}$ ) at time $t$, while $\hat{x}_{i-1}(t)$ represents the speed of the leading vehicle (vehicle ${ }_{i-1}$ ) at the same instant.

The TTC represents the time remaining before a collision occurs if both vehicles continue at their current speeds. The numerator, $x_{i-1}(t)-x_{i}(t)-l_{i}$, represents the gap

distance between the following vehicle and the leading vehicle, adjusted for the length of the following vehicle. The denominator, $\tilde{x}_{i}(t)-\hat{x}_{i-1}(t)$, represents the relative speed between the two vehicles. The condition $\tilde{x}_{i}(t)>\hat{x}_{i-1}(t)$ ensures that the following vehicle is moving faster than the leading vehicle, which is necessary for a potential collision to occur.

According to international test practices and industry research [39,41], the TTC threshold for household vehicles is set to 2.4 s . Below this value, vehicles are prone to collision. This threshold is based on extensive experimental data and real-world testing, ensuring enough reaction time for drivers or automated systems to take evasive action and avoid accidents. Specifically, the 2.4 s threshold accounts for average human reaction times combined with the mechanical response times of vehicles, providing a safe margin to prevent collisions.

We can obtain the safety factor of the vehicle according to the TTC value, which is defined as follows:

$$
\mathcal{S}_{c}=\left\{s_{c} \in \mathcal{S} \mid T T C_{i}<2.4\right\}
$$

Overall, scene-based and safe time-based sampling play a significant role in enhancing the focus and effectiveness of the training strategy within the context of autonomous driving tasks.

# 3.4. DAgger with Uncertainty Estimates and Critical States 

DAgger is an iterative training algorithm that collects on-policy data at each iteration under the current policy and trains the next policy under the aggregate of all collected data. This iteration continues until the supervised cost on a validation set stops improving.

Our proposed DAgger algorithm synergistically combines uncertainty estimation with the identification of critical states, with the detailed procedure depicted in Algorithm 2. In any given scenario $s$, for every action $a$ executed under the agent policy $\hat{\pi}$, we commence by utilizing a Bayesian neural network to conduct an uncertainty prediction. Should the resulting uncertainty surpass a predefined threshold $\tau$, we defer control to the expert policy $\pi^{*}$, thereby preventing the traversal of a sequence of suboptimal states. The algorithm leverages uncertainty estimation to orchestrate the data collection process, focusing on acquiring data that are most instrumental in enhancing model performance. specifically, correction behaviors at the boundary between optimal and suboptimal states. The selection of the policy at each sampling instance is shown in Equation (15), where $V I$ is the uncertainty prediction network. Concurrently, for each scenario, we extract critical frames using both scene-based and safe time-based methods.

$$
\pi=\left\{\begin{array}{l}
\pi^{*}, V I(s)>\tau \\
\hat{\pi}, \text { otherwise }
\end{array}\right.
$$

The determination of the threshold $\tau$ is a significant element within our computational framework. The threshold is computed iteratively by aggregating the uncertainty estimates, represented by $\sigma(a \mid s)$, for all scenarios within a given iteration to obtain their mean $\mu$ and standard deviation $\sigma^{*}$. We then define the threshold $\tau$ as $\tau=\mu+\sigma^{*}$.

The theoretical justification for adopting the threshold $\tau=\mu+\sigma^{*}$ is rooted in the properties of the normal distribution. In a normal distribution, approximately $68 \%$ of the data lies within one standard deviation of the mean. Thus, by setting the threshold to $\mu+\sigma^{*}$, our algorithm targets scenarios that exhibit a level of uncertainty above what is typical for $68 \%$ of the scenarios observed. This method ensures that the scenarios selected for sampling present a higher degree of uncertainty, which is pivotal for the algorithm to identify and learn from more challenging and less certain states.

We also employed the replay buffer method proposed by the authors. The fixed size of the replay buffer meticulously controls the blend of expert and on-policy data, enabling the learning algorithm to successively refine and augment the policy's capabilities, especially in its areas of deficiency, culminating in a more adept and flexible driving policy.

```
Algorithm 2 DAgger with Uncertainty Estimate and Critical States
    Collect \(D_{0}\) using expert policy \(\pi^{*}\)
    \(\hat{\pi}_{0}=\operatorname{argmin}_{\pi} \mathcal{L}\left(\pi, \pi^{*}, D_{0}\right)\)
    Initialize variational inference network \(\mathrm{VI}_{0}\left(D_{0}\right)\)
    Initialize uncertainty threshold \(\tau_{0}\)
    Initialize replay buffer \(D \leftarrow D_{0}\)
    Let \(m=\left|D_{0}\right|\)
    for \(i=1\) to \(N\) do
        Generate on-policy datasets \(D_{i}\) using \(\pi\left(\pi=\pi^{*}, V I(s)>\tau ; \pi=\hat{\pi}\right.\), otherwise \()\)
        sampling critical states \(s_{c}\) from \(D_{i}\)
        sampling unsafe states :
```

$$
\mathcal{S}_{\mathrm{u}} \leftarrow\left\{s \in D_{i} \mid \mathrm{VI}_{i-1}(\mathrm{~s})>\tau_{i-1}\right\}
$$

Get $D_{i}^{\prime} \leftarrow\left\{s \in s_{c} \cup s_{u} \mid\left(s, \pi^{*}(s)\right)\right\}$ of visited states by expert $\hat{\pi}^{*}$
Combine datasets: $D \leftarrow D \cup D_{i}^{\prime}$
while $|D|>m$ do
Sample $\left(s, \pi^{*}(s)\right)$ randomly from $D \cap D_{0}$
$D \leftarrow D-\left\{\left(s, \pi^{*}(s)\right)\right\}$
end while
Train $\hat{\pi}_{i}=\operatorname{argmin}_{\pi} \mathcal{L}\left(\pi, \pi^{*}, D\right)$ with policy initialized from $\hat{\pi}_{i-1}$
Training $\mathrm{VI}_{i}(D)$.
Update $\tau_{i}$.
end for
return $\hat{\pi}_{N}$

# 4. Experiments and Evaluation 

### 4.1. Environment

We utilize the CARLA simulator as the environment for training and evaluation of our autonomous driving models. The NoCrash benchmark serves as our primary assessment tool. Each NoCrash scenario defines specific training conditions, including the virtual towns (Town 1 for training and Town 2 for testing) and weather settings, for data collection [26,27]. Subsequently, the agent's performance is evaluated in novel towns and weather conditions not encountered during training.

The NoCrash benchmark examines the agent's ability to generalize from Town 1, meticulously designed as a training environment, to Town 2, designed as a testing environment. Figure 3 shows maps of these towns and representative views. Town 1 features an intricate network of 2.9 km of drivable roads, meticulously designed to replicate real-world urban landscapes, featuring diverse urban structures (buildings, vegetation), traffic signage, and infrastructure. The inclusion of intricate intersections, pedestrian crossings, and a variety of weather and lighting conditions makes Town 1 ideal for training robust ADS models. The extensive and varied layout challenges these models with diverse scenarios, fostering the development of robust perception, planning, and control modules.

Town 2, a scaled-down version of Town 1, presents a more compact environment ( 1.4 km of drivable roads) with an equally detailed level of fidelity. This environment features a distinct urban layout with unique textures and 3D models, including a mix of single-lane and multi-lane roads, as well as more complex junctions compared to Town 1. Town 2 serves primarily as a testing ground, offering an unseen environment to assess the adaptability and robustness of models trained in Town 1. By encountering novel road layouts, building structures, and environmental textures, this approach verifies the generalization capabilities of the models, ensuring they can handle variations within a similar urban style.

![img-2.jpeg](img-2.jpeg)

Figure 3. The two CARLA towns. (a) The map of Town 1 and two example scenes. (b) The map of Town 2 and two example scenes.

Consistent with the NoCrash benchmark, our driving policy is developed using datasets collected in Town 1 under four distinct weather conditions. The policy's robustness is then assessed across various scenarios: Training, New Weather (NW), New Town (NT), and the combined New Town and Weather (NTW) conditions. The NoCrash benchmark categorizes traffic density into three distinct levels: empty, regular, and dense. These classifications determine the quantity of pedestrians and vehicles populating each map. For the evaluations conducted on the CARLA Leaderboard, the traffic density of each map has been calibrated to correspond with the established busy traffic parameters.

# 4.2. Uncertainty Estimation 

### 4.2.1. Mean and Standard Deviation of Uncertainty Estimates

The imitation agent and our uncertainty estimation system were tested in a novel environment, Town 2, which is part of the CARLA benchmark. This town features a smaller and more varied layout compared to Town 1 and includes both old and new weather conditions, using a subset of test cases provided in the benchmark. The network outputs three control signals: steering angle, throttle value, and brake. Uncertainties for the control signals were computed independently. The tested uncertainty estimation signals include steer standard error, throttle standard error, and brake standard error. We present several specific examples of uncertainty estimation. Figure 4a demonstrates the effect of different lighting and weather conditions on uncertainty estimation within the same scene. Specifically, it includes three images, each corresponding to different lighting and weather scenarios. These variations significantly affect the uncertainty estimates, highlighting the importance of accurate uncertainty estimation under diverse environmental conditions. Figure 4b presents additional scenarios where the estimated uncertainty exceeds a predefined threshold. This part of the figure emphasizes challenging situations such as changes in road surface illumination, traffic lights, sharp turns, and other novel or complex conditions. The high uncertainty estimates in these scenarios underscore the potential of our proposed DAgger framework to handle complex driving environments effectively.

To evaluate the sensitivity of uncertainty estimation to novel scenarios. We collected four distinct datasets, each comprising 10,000 frames, under varied scenario conditions. under each high-level command, we independently calculated the mean value $u$ and standard deviation $\sigma$ of the uncertainty for each action. These statistics serve as the main basis for calculating the uncertainty threshold in the subsequent steps. Table 1 presents the corresponding statistical values of action uncertainty obtained from testing in

different environments. The results demonstrate that the uncertainty of the agent's actions increases in new environments, which aligns with the expected behavior of uncertainty estimation principles.
![img-3.jpeg](img-3.jpeg)

Figure 4. (a) The three images illustrate the influence of varying lighting and weather conditions on the estimated uncertainty within the same scene. (b) Additional examples where the uncertainty of the estimate exceeds the threshold. For instance, this can occur when the agent encounters changes in road surface illumination, traffic lights, sharp turns, or other novel or complex situations.

Table 1. Mean and standard deviation of uncertainty estimates in different scenarios.


During the iterative training process of DAgger, we analyzed the changes in $u$ and $\sigma$ after each training loop. As show in Table 2, the number of iterations increases, the parameters of the deep Bayesian network gradually stabilize, leading to more precise uncertainty estimations. Consequently, $u$ and $\sigma$ tend to decrease with the increasing number of loops, reflecting the growing confidence in action selection through imitation learning. This variation necessitates dynamic adjustments when selecting the uncertainty threshold $\tau$ to adapt to the changes in each iteration.

Table 2. Mean and standard deviation of uncertainty estimates in Iter.


# 4.2.2. Monte Carlo Sample Size 

Deep Bayesian algorithms require multiple forward inferences to quantify the uncertainty of the data; this called Monte Carlo sampling. There exists a trade-off between the sample size and the accuracy of uncertainty computation. Generally, more sample size can achieve better accuracy but at the cost of higher computational complexity. However, the computed uncertainty value tends to stabilize as the number of sample size increases. Therefore, it is crucial to select an appropriate number of sample size to balance accuracy and computational complexity.

We evaluated the changes in the mean of all uncertainty in the training set. As shown in Figure 5a, we analyzed the relationship between the sample size and the mean of uncertainty. We also compared our results with the MC-dropout algorithm used in UAIL. The figure demonstrates that the mean of our MFVI algorithm stabilizes after size $=10$, while MC-dropout still exhibits significant fluctuations. This indicates that MC-dropout requires more computation to obtain reliable uncertainty estimates. This is theoretically justified because MFVI approximates the posterior distribution by maximizing the evidence lower bound, which can be computed analytically via the log-likelihood term and the KL divergence term, leading to reduced computational complexity.
![img-4.jpeg](img-4.jpeg)

Figure 5. A comparison of variational inference and Monte Carlo dropout on uncertainty prediction, based on our test set. (a) The mean uncertainty of actions varies with changes in sample size. (b) ROC curves for predicting infractions in test environment, the total uncertainty under different commands. (c) The average ratio of consultations by the expert policy. Algorithms eventually transfer control to the novice policy.

# 4.2.3. Infraction Prediction 

We evaluated the predictive performance of our proposed candidate uncertainty functions for infraction detection using receiver operating characteristic (ROC) curves. Since there is no public dataset for uncertainty evaluation, we followed the UAIL approach and considered the following events as infractions: collisions, crossing into the opposite lane, and driving onto the curb. Due to the branched structure of the network, ROC curves for different commands are plotted in Figure 5b. In this experiment, we utilize the joint uncertainty as described by UAIL, where the total uncertainty is defined as $U_{\text {total }}=U_{\text {streee }}+\alpha U_{\text {throttle }},(\alpha=0.6)$. The different shapes of the ROC curves indicate that different threshold values should be used to achieve similar true-positive ratios across different commands. As can be seen from the figure, the Area Under the curve (AUC) value for the straight command is low. This is because straight driving is relatively simple and does not involve complex steering operations, resulting in lower uncertainty values and reduced sensitivity to dangerous scenarios.

Compared to MC-dropout, our algorithm achieved better AUC values for all commands. This demonstrates that our algorithm can better estimate the uncertainty of the scene. Theoretically, MC-dropout has been shown to be more accurate for small data sets [19]. However, variational inference outperforms MC-dropout in large-scale data sets [22] and when the data distribution is shifted [42]. Since our autonomous driving task involves large-scale data with frequent distribution changes, MFVI is more suitable for uncertainty estimation in the autonomous driving scenario.

### 4.2.4. Expert Ratio

The performance of uncertainty prediction is also reflected in the ratio of expert queries. As shown in Figure 5c, it can be observed that the algorithm initially relies heavily on expert queries. However, as the number of training iterations increases, the number of expert queries decreases. We can also see that variational inference can reduce the expert ratio faster than MC-dropout. This indicates that the variational inference algorithm can better select uncertain data and help the imitation learning model to train better.

### 4.3. Driving Performance

### 4.3.1. Metrics

We present our results using two key performance indicators: the success rate, as proposed by the NoCrash benchmark, and the driving score, an innovative metric introduced by the CARLA leaderboard. The success rate quantifies the proportion of routes completed without incurring any collisions or impasses. The driving score, on the other hand, is calculated as the product of two factors: route completion, which is the percentage of the route distance successfully navigated; and the infraction penalty, which is a cumulative discount applied for each infraction incurred during the drive. For instance, if an agent were to run two red lights during a single route, with a penalty coefficient of 0.7 for each infraction, the overall infraction penalty would be $(0.7 \times 0.7=0.49)$. The driving score offers a more nuanced assessment than the success rate, accounting for a broader spectrum of infractions, making it particularly advantageous for evaluating performance over longer routes.

### 4.3.2. Baseline and Alternatives

To analyze the driving performance, we compare our method against several algorithms: CILRS [27], DARB [13], UAIL [21], DA_UE (DAgger with uncertainty estimate using Variational Inference), DA_CS (DAgger with critical scenes), DA_UE+CS (our proposed, DAgger with uncertainty estimate and critical scenes), and UAIL+ (UAIL incorporates advanced DAgger architecture).

CILRS is a seminal end-to-end imitation learning algorithm in the autonomous driving domain, widely used as a control network, including in our own system. DARB represents an extension of the original DAgger algorithm that leverages critical state and replay buffer technology. Notably, DARB incorporates extensive data preprocessing tailored to

autonomous driving tasks. This algorithm has demonstrated promising performance on the NoCrash benchmark, establishing itself as a valuable baseline for research on DAgger algorithms in the context of autonomous driving.

UAIL also employs the DAgger framework and utilizes Monte Carlo dropout for uncertainty estimation. However, UAIL suffers from poor performance due to its outdated DAgger implementation. To compare the impact of different deep Bayesian algorithms on performance, we ported the UAIL algorithm to DARB to obtain UAIL+. Therefore, the only difference between UAIL+ and our approach lies in the choice of the deep Bayesian algorithm.

Due to DARB's use of an advanced DAgger architecture, all of our proposed algorithms are developed based on DARB. Our proposed DA_UE builds upon DARB by using uncertainty estimation via MFVI to extract key frames, providing a more robust approach to handling uncertain and replacing traditional methods. DA_CS is an extension of DARB that focuses on incorporating our defined critical scenes during the training process, thereby improving the policy's ability to respond to high-risk scenarios. DA_UE+CS, our complete algorithm, combines the features of DA_UE and DA_CS, leveraging uncertainty estimation to extract key frames and identifying critical safety scenes, aiming to utilize the strengths of both approaches for enhanced performance.

We compare our approach against the aforementioned algorithms for performance evaluation. For our infraction analysis, we focus on DARB since it significantly outperforms other approaches and serves as a strong baseline.

# 4.3.3. Performance and Ablation Study 

The performance of the models on the NoCrash benchmark at each DAgger iteration is shown in Figure 6. As expected, all models improved after iterative training with the DAgger mechanism. While the backbone networks of all models were the same, based on CILRS, the algorithms differed mainly in data selection and training methods. Our algorithm, which combines MFVI with safe critical states, achieved good results in all scenarios. Our autopilot can achieve a driving score of $30 \%$ and a success rate of $40 \%$.
![img-5.jpeg](img-5.jpeg)

Figure 6. Success rate of different methods across conditions. experimental environments: NW (New Weather), NT (New Town), NTW (New Town and Weather). Algorithms used in our experiments: DARB [13], CILRS [27], DA_UE (DAgger with uncertainty estimate use variational inference), DA_C S(DAgger with critical scenes), DA_UE+CS (our proposed, DAgger with uncertainty estimate and critical scenes), UAIL [21], UAIL+ (UAIL with critical scenes).

We examined whether on-policy data help to improve our driving performance. We mainly used two techniques to improve the agent's performance: critical state and uncertainty estimation. As shown in the figure, both methods improved performance. However, the effects and principles of these two methods are different.

Critical scenes slightly improved performance, thereby affirming that the sampled critical states contain useful information that facilitates improved driving behavior. However, on the new weather condition, the performance of critical scenes starts to decline. This indicates that the scenario selection method of critical scenes does not include weather changes, so it is not good at handling such scenarios.

Uncertainty estimation significantly improved performance in all scenarios. This indicates that calculating the uncertainty of scenarios and selecting suboptimal data does improve the performance of the model. This is consistent with previous research.

# 4.3.4. Comparison against DARB 

DARB is a notable approach in imitation learning for autonomous driving, focusing on aggregating data from critical and high-uncertainty states. This method employs a replay buffer mechanism to prioritize these states, aiming to enhance the generalization performance of the driving policy. However, it is essentially still the traditional DAgger algorithm, which requires frequent access to the expert policy when collecting trajectories and may also collect a lot of suboptimal data. Our proposed DAgger framework with MFVI shares a similar goal but offers distinct advantages over DARB.

We employ an uncertainty-based prediction method combined with active learning, which differs significantly from traditional DAgger algorithms such as DARB in the way training trajectory is collected. As shown in Figure 7, we illustrate the differences in data collection methods through specific experimental examples. The DARB method, particularly during the early stages of training when the performance of the learned policy is suboptimal, tends to collect a large amount of poor and unnecessary suboptimal data. Figure 7b demonstrates such an example, where the vehicle driven by the learned policy ends up on the sidewalk. Learning how to drive on the sidewalk is not useful, and once in this suboptimal state, even the expert policy has difficulty recovering, let alone providing guidance to the learned policy. In our experiments, when scenarios such as driving onto the sidewalk or colliding with a lamppost occur, the expert policy often fails to recover. Collecting such trajectory data results in poor guidance and labeling by the expert policy, which degrades the quality of the training data and subsequently the training effectiveness of the learned policy.

The uncertainty-based prediction method combined with active learning helps to some extent in avoiding the collection of suboptimal data. As shown in Figure 7c, when the uncertainty of the learned policy exceeds the threshold, control is immediately handed over to the expert, who gradually recovers to a normal state before returning control to the learned policy. This approach prevents the continuous collection of suboptimal data, thereby improving the quality of the training data and the effectiveness of the learned policy's training.

To validate the effectiveness of the uncertainty-based prediction method for dataset collection, we modified the data collection approach of DARB to incorporate uncertainty prediction and active learning, naming the algorithm DA_UE. As shown in Figure 6, DA_UE's success rate surpasses that of DARB from the initial training stages and eventually approaches expert-level performance. Furthermore, DA_UE demonstrates superior generalization on the test set, particularly under NT and NW conditions where DARB's generalization capability significantly declines, yet DA_UE maintains strong performance. Using the Carla leaderboard testing methodology, as shown in Table 3, DA_UE achieved a driving score of 27.9 , representing a $32 \%$ improvement over DARB. Evaluating the individual test components, we also observe enhanced safety with DA_UE. This indicates that leveraging uncertainty prediction combined with active learning for data collection effectively avoids the accumulation of suboptimal data, thereby improving the quality and

diversity of the dataset annotations and significantly enhancing the performance of the learned policy.
![img-6.jpeg](img-6.jpeg)

Figure 7. Trajectory data for different control methods. In the diagrams, circles represent expert trajectories, while triangles indicate trajectories generated by the learned policy. Green signifies that uncertainty remains below the threshold, indicating a safe state. Conversely, red signifies that uncertainty exceeds the threshold, indicating an unsafe state. (a) The vehicle is entirely driven by the expert $\pi^{*}$. (b) The vehicle is driven entirely by the learned policy $\hat{\pi}$, reflecting the traditional DAgger algorithm, such as DARB, for collecting training trajectories. This approach tends to collect a significant amount of suboptimal data. (c) The uncertainty-based prediction method, where the expert policy $\pi^{*}$ takes over driving when the learned policy's uncertainty exceeds the threshold, thereby avoiding the collection of excessive suboptimal data.

Table 3. Driving performance and infraction analysis of IL agents on NoCrash-busy.


New Town and New Weather. Mean and standard deviation over 3 evaluation seeds. DS: driving score. RC: route completion. IS: infraction score. CP: collisions with pedestrians. CV: collisions with vehicles. CO: collisions with others. RI: red light infraction. AB: agent blocked.

# 4.3.5. Comparison against UAIL and UAIL+ 

As shown in Figure 6, UAIL also improved the performance of the model and had some generalization ability to new scenarios. UAIL also used uncertainty prediction, but it used the traditional DAgger structure without data preprocessing or replay buffer, so the final performance improvement was limited. UAIL+ used the MC-dropout algorithm to perform uncertainty prediction in our algorithm structure. The performance was indeed better than UAIL, which also indicates that the improved techniques proposed by researchers in the DAgger algorithm do improve performance. However, the performance of UAIL+ was still not as good as that of DA_UE. As we analyzed before, in the autonomous driving scenario, the MC-dropout method is not as good as the MFVI method for uncertainty prediction, which ultimately leads to poor driving performance of the agent. This also shows that choosing different deep Bayesian algorithms has an impact on the performance of Bayesian DAgger-like algorithms.

# 4.3.6. Infraction Analysis 

Table 3 shows that DA_UE underperforms DARB in the traffic light scenario. Through analyzing the specific data, we found that the Bayesian network is unstable for predicting traffic scenes with traffic lights and cannot make good uncertainty predictions. This indicates that the network's perception of small targets is not good, which leads to insufficient training data extraction for the Bayesian network in this aspect. However, the subsequent critical scenses makes up for this defect and improves the training samples for traffic lights. Finally, the overall performance of the DA_UE+CS algorithm exceeds that of DARB, demonstrating the effectiveness of the proposed method.

## 5. Conclusions

This study presents a novel DAgger framework that synergistically integrates Bayesian uncertainty estimation via mean field variational inference and critical state identification to improve imitation learning for autonomous driving. The proposed method efficiently approximates the posterior distribution over the policy's parameters and provides wellcalibrated uncertainty estimates. During training, the framework identifies both uncertain and critical states, querying the expert only for these states, thereby reducing the burden on the expert and improving data efficiency.

Evaluations on the CARLA simulator using the NoCrash and CARLA leaderboard benchmarks demonstrate that the proposed method outperforms existing imitation learning approaches, such as CILRS, DARB, and UAIL. The results highlight the effectiveness of integrating Bayesian uncertainty estimation and targeted data aggregation in imitation learning for autonomous driving. The proposed approach achieves a higher success rate and lower infraction rate compared to the traditional DAgger algorithm, indicating that uncertainty prediction methods are more purposeful in the data collection process by focusing on states where the learning agent needs improvement.

In conclusion, this study presents a novel and effective approach to imitation learning for autonomous driving by leveraging Bayesian uncertainty estimation and critical state identification. The proposed method improves driving performance, generalization ability, and data efficiency, making it a promising direction for future research in autonomous driving.

Author Contributions: Conceptualization: C.W. and Y.W.; Methodology: C.W.; Software: C.W.; Validation: C.W. and Y.W.; Formal analysis: C.W.; Investigation: C.W.; Resources: C.W.; Data curation: C.W.; Writing-original draft preparation: C.W.; Writing-review \& editing: Y.W.; Visualization: C.W.; Supervision: Y.W.; Project administration: Y.W.; Funding acquisition: Y.W.; All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the National Key Research and Development Program of China (2021YFB2501403).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data in this study are available from the first author upon request.
Conflicts of Interest: The authors declare no conflict of interest.
