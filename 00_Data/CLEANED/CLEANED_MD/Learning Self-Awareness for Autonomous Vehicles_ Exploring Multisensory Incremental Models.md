# Learning Self-Awareness for Autonomous Vehicles: Exploring Multisensory Incremental Models 

Mahdyar Ravanbakhsh, Mohamad Baydoun, Damian Campo, Pablo Marin, David Martin, Lucio Marcenaro, and Carlo Regazzoni


#### Abstract

The technology for autonomous vehicles is close to replacing human drivers by artificial systems endowed with high-level decision-making capabilities. In this regard, systems must learn about the usual vehicle's behavior to predict imminent difficulties before they happen. An autonomous agent should be capable of continuously interacting with multi-modal dynamic environments while learning unseen novel concepts. Such environments are not often available to train the agent on it, so the agent should have an understanding of its own capacities and limitations. This understanding is usually called self-awareness. This paper proposes a multi-modal self-awareness modeling of signals coming from different sources. This paper shows how different machine learning techniques can be used under a generic framework to learn single modality models by using Dynamic Bayesian Networks. In the presented case, a probabilistic switching model and a bank of generative adversarial networks are employed to model a vehicle's positional and visual information respectively. Our results include experiments performed on a real vehicle, highlighting the potentiality of the proposed approach at detecting abnormalities in real scenarios.


Index Terms-self-awareness, dynamic Bayesian networks, multi-modality, deep generative models.

## ACRONYMS

DBN dynamical Bayesian network
GAN generative adversarial networks
KF Kalman filter
MJPF Markov jump particle filter
MKF motivated Kalman filter
PF particle filter
PL private layer
SA self-awareness
SDS switching dynamical system
SL shared layer
SOM self-organizing map
U-KF unmotivated-agent Kalman filter

## I. INTRODUCTION

Autonomous vehicles are designed to take human error out of driving actions, which should help make self-driving vehicles safer, thus dramatically reducing the number of road

[^0]accidents. Nowadays, methods based on machine learning techniques together with signal processing are playing an increasingly substantial role in this domain and contributing to general topics such as monitoring driver distraction [1], Smart Driver Monitoring [2], [3], vehicle infrastructure support and planning/monitoring [4], [5], and detecting abnormalities automatically from multi-sensory data [6-8].

Systems with a single modality generally lack the robustness and reliability required in real-word applications [9]. To tackle this issue, we propose a cross-modality structure using an agent's internal and external sensory data. Our approach is motivated by the process of problem-solving in humans, where information from various modalities, e.g., vision and language [10], [11], or different domains, e.g., brain and environment [12], is combined to improve the decision-making.

SA refers to the system's capability to recognize and predict its own states, possible actions, and the result of these actions on the system itself and its surroundings [13]. By using SA models, the agent gains the ability to both predict the future evolution of a situation and detect situations potentially unmanageable. This "sense of the limit" is considered as a level of SA that allows an agent to predict potential changes concerning its previous experiences to involve a human operator for support in due time. In this sense, the capability of detecting novel situations is an essential feature of SA models as it allows autonomous systems to anticipate their situational/contextual states and improve the effectiveness of the decision-making sub-modules [7], [14], [15]. Our model is not a fully autonomous driving system; however, it is an aware system that can provide suggestions, predictions, and detect the possible deviation from previously learned tasks/situations.

The work in [7] introduces an SA model consisting of two layers: SL and PL. The analysis of observed moving agents for learning normal/abnormal dynamics in a given scene represents an emerging research field [16-30]. An agent's planned activity can be modeled as a sequence of organized state changes (actions) performed to achieve a task under a particular context. This set of actions can be learned from observations that, in turn, can be clustered into sequential discrete patterns. The availability of a plan that associates the current state with an action model facilitates the detection of normal/abnormal situations in future repetitions of the same task. This paper complies with the definition of abnormality offered by, [31], which defines it as a behavior (set of observations) that has not been seen before.

An active SA action plan can be seen as a dynamical filter that predicts state behaviors using dynamic and observation


[^0]:    Mahdyar Ravanbakhsh, Mohamad Baydoun, Damian Campo, Lucio Marcenaro, Carlo Regazzoni, are with the Department of Electrical, Electronics and Telecommunication Engineering and Naval Architecture, University of Genoa, Genoa 16145, Italy. (e-mail: mahdyar.ravan@ginevra.dibe.unige.it; mohamad.baydoun@ginevra.dibe.unige.it; damian.campo@ginevra.dibe.unige.it; lucio.marcenaro@unige.it; carlo.regazzoni@unige.it).
    Pablo Marin and David Martin are with the Intelligent Systems Laboratory, Department of Systems Engineering and Automation, Universidad Carlos III de Madrid, 28911 Leganes, Spain (e-mail: pamarinp@ing.uc3m.es; dmgomez@ing.uc3m.es).

![img-0.jpeg](img-0.jpeg)

Fig. 1: Block Diagram of Learning Process: the DBN learning starts with an initial general model. New experiences that deviate from the general model (abnormalities) are detected. Identified abnormalities are stored and they can be used to learn a new model. Once the new learned model is available, the process can be iterated.

models. SDSs [32] are well-known probabilistic graphical models [33] capable of managing discrete and continuous variables jointly in dynamical filters. Probabilistic models have demonstrated their usefulness at the moment of modeling dependencies between different variables [34]. In [35], a probabilistic approach is taken for tracking random irregularities that evolve through time in vehicles/tracks.

This paper proposes a switching DBN that dynamically estimates future and present states at continuous and discrete levels. In [16], SDSs have been used successfully to improve decision making and tracking capabilities. Moreover, the ability of probabilistic models to manage discrete representations enables the incorporation of semantic concepts in autonomous systems [36–38], which is a useful feature for communicating/cooperating with humans. In [39], [40], authors propose probabilistic approaches that encode high-level semantics, e.g., drivers' intention, to model traffic vehicle data.

The MJPF [41] is one of the most used algorithms that takes advantage of learned hierarchical probabilistic models in the online SDS phase. MJPF uses a combination of KF and PF to predict and update jointly continuous and discrete state space posterior probabilities. This paper employs an MJPF to exploit learned knowledge from the SL that includes the capability to self-detect abnormality situations.

An agent can infer dynamic models through internal variables, which represent private information only accessible by the agent itself. Detecting abnormalities is possible by training a SA model on private (first person) multisensorial data. Such a model can be defined as the PL of SA [7]. Most of the previous works rely on high-level supervision to learn SA models for the PL [7], [15], [31]. However, this work proposes a weakly-supervised method based on a hierarchy of cross-modal GANs [42], [43]. In this work, PL data consists of the first-person visual information taken by an operative agent. This visual information, coupled with the corresponding optical-flow data, is used to learn GAN models.

Our major contributions are *(i)* proposing SDSs for learning several tasks incrementally in a semi-supervised fashion.

*(ii)* Introducing a multi-modal probabilistic model that can increase the capability of self-understanding and situational awareness in autonomous systems. Our model finds deviations (abnormalities) in human driving behaviors that may lead to detecting a new task, undesired situations, and even threats to the drivers' safety.

The proposed method includes two major phases: *(i)* an incremental offline learning process and *(ii)* an online testing procedure for detecting the possible abnormalities. The proposed offline incremental learning process for both SL and PL is described in Sec II, and the online abnormality detection phase is presented in Sec. III. Sec. IV introduces the employed dataset and shows the experimental results of training/testing phases. Sec. V discusses the different components of our proposed method and Sec. VI concludes the article.

## II. MULTI-MODAL SELF-AWARENESS MODELING

This work focuses on the incremental learning of dynamic models from data acquired through the agent's experiences, facilitating the building of SA models. This paper considers the actions of a human driver while performing different tasks observed from the vehicle's "First Person" viewpoint. We propose an incremental adaptive process that allows the agent (vehicle) to learn switching DBN models from video and positional data. These models can predict (i.e., to generate) new observed situations and adaptively estimate the current states by filtering data based on the most fitting model (i.e., to discriminate). In other words, DBN models facilitate the prediction of situations different from the dynamic reference equilibrium (i.e., previously learned models).

Our SA model consists of two levels: PL and SL. For both of them, a unified learning procedure is designed, see Fig. 1. The proposed incremental process (see Tab. I) adds generative and discriminative knowledge to already known experiences. Statistically significant deviations from such known situations are recognized as abnormal situations whose characteristics are captured by the newly learned models.

In our experiments, PL and SL are learned based on visual perception (first-person vision data only available to the


TABLE I: Phases/components of the proposed method concerning the SA modalities. See Fig. 2 for corresponding blocks.
agent) and localization (third-person vision), respectively. A probabilistic framework based on a set of switching dynamical models [41], [44], [45] is used to learn the SL's models incrementally. On the other hand, a bank of cross-modal GANs is employed for learning PL models. The rest of this section introduces a general procedure to learn dynamic models from a set of observed experiences and also presents a detailed explanation of learning processes for each level of SA.

## A. Learning SL and PL: an off-line process

Fig. 1 shows a flow chart describing our proposed adaptive learning process that enables the incremental learning of additional knowledge necessary to describe new observed situations. By encoding new knowledge into the agent's conditions of equilibrium trough probabilistic switching models, it is possible to increase the SA level of the agent.

The incremental learning of new models starts by observing dynamic data series related to a given experience (Fig. 1-b). Such a data is filtered by using an initial reference model (Fig. 1-a) and by keeping track of deviations w.r.t it. The initial reference model consists of a simple filter whose dynamic model describes a basic dynamic condition of equilibrium. In the case of SL, where low dimensional data, i.e., 2D-locations and velocities, are considered, the initial filter corresponds to a KF that assumes the agent remains static. This filter makes reasonable predictions when there are no forces affecting the state of the agent, i.e., in case the agent does not interact with its surroundings, suggesting that agent motions can be approximated by small random noise oscillations of the state. In the SL, noises can be produced either by the agent or external entities, producing noisy data series of sparse measurements. Accordingly, we define it as the U-KF. Such a reference filter is illustrated in Fig. 2-a.1. U-KF assumes $\dot{x}=\omega$, where $\dot{x}$ is the agent's velocity and $\omega$ is the perturbation error.

When the U-KF is applied to a motivated experience, it produces a set of errors due to the fact that the agent follows certain motivations modeled as surroundings' forces acting on it. In the PL, a pre-trained reference GAN is used as an initial general model (see Fig. 2-a.2), which encodes an experience where the agent moves linearly on a clear path. Similar to the U-KF model, the reference GAN assumes a dynamic equilibrium exists between the environment and the agent but on a different modality, i.e., first-person video data). In this case, the condition of equilibrium corresponds to the agent's visual data supporting linear motion towards a point in the environment. Such a point can be seen as a stationary center of force that attracts the agent linearly. In case other forces
interact with the agent, the dynamics of visual data would vary from the linear movement, producing a set of prediction mismatches (errors) between the GAN filter estimations and the new observations. By considering the set of errors (here defined as innovations, using terminology from KFs) obtained from U-KF and the reference GAN, cumulative probabilistic tests can be designed for both SL and PL to evaluate whether a data series corresponds to an abnormal experience.

Collected innovations can be used to decide when to store data to learn a new filter. Each new filter represents a new equilibrium condition encoding a set of stationary forces, see Fig. 1-c. The abnormality measurement process block ranks innovations and computes abnormality signals, enabling the selection of the most probable model among those learned from previous experiences. The most fittest models represent an SDS in case of SL and a couple of cross-modal GANs for PL. Abnormality signals can drive soft decision processes [46] and are used to learn new models, see Fig. 1-d.

The abnormality detection procedure enables defining an incremental process similar to Dirichlet [47] (stick-breaking processes [48], Chinese restaurant [49]). The proposed abnormality measurements determine the choice about whether new observations can be described by already available experiences (learned equilibrium conditions) embedded into DBN (Fig. 1e) or there is a need to learn a new one (Fig. 1-d). Data from new experiences can be structured into multiple partitions of the state-innovation, where the correlations between states and innovations facilitate clustering the new data into classes that define a new learned model. Fig. 1-d shows the procedure of learning new models from state-innovation pairs. Such a data couple establishes a relationship between the states and error measurements obtained through the initial models. In the case of SL, the new learning model process generates a set of regions that segment the state space motion depending on innovations (See Fig. 2-d.1). For the PL's case, it is considered a clustering of consecutive images and their corresponding optical flows based on a similarity measurement (i.e., local innovation), see Fig. 2-d.2. Detected regions can form an explicit (in SDS) or implicit (in GANs) vocabulary of switching variables employed by learned model to describe new experiences. Note that, in the case of PL, there is a need for accessing dynamic visual information to train a new set of GANs. Hence, as shown in Fig. 2-d.2, for detected new clusters based on state-innovation pairs, the original data is used directly for training the new GANs. Accordingly, PL's models are all related to different effects of forces distinct from the one producing a linear motion in a video sequence, e.g., a curving motion will generate a new GAN model.

![img-1.jpeg](img-1.jpeg)

Fig. 2: Learning Process in SL and PL: for each experience, SL and PL use respectively positional and video data and as inputs. The structure of both layers is based on a generic incremental adaptive training process that allows them to increase their self-awareness capabilities by learning new experiences observed from multi-sensory sources.

### *B. Mathematical modeling of spatial activities for SL layer*

In SL, the main idea consists of learning a switching DBN for tracking and predicting the dynamical system over time, see Fig. 3 (b). Hence, arrows represent conditional probabilities between the involved variables. Vertical arrows facilitate describing causalities between both continuous and discrete levels of inference and observed measurements.

**Dynamic modeling.** The SL level of SA focuses on the analysis of agents' positional information for understanding their dynamics in a given scene through a set of SL's models \( M = {m}_{m=1,\ldots,M} \). As it is well known, the dynamics of an agent can be described by hierarchical probabilistic models consisting of continuous and discrete random variables. Accordingly, an agent's dynamic model can be written as:

$$X_{k+1} = AX_k + BU_{S_k^m + w_k},\tag{1}$$

where \( X_k \) represents the agent's state composed of its coordinate positions and velocities at a time instant \( k \), such that \( X_k = [\boldsymbol{x} \boldsymbol{\dot{x}}]^T \). \( \boldsymbol{x} \in \mathbb{R}^d \) and \( \boldsymbol{\dot{x}} \in \mathbb{R}^d \). \( d \) represents the dimensionality of the environment. \( A = [A_1 \quad A_2] \) is a dynamic model matrix: \( A_1 = [I_d \quad 0_{d,d}]^T \) and \( A_2 = 0_{2d,d} \). \( I_n \) represents a square identity matrix of size \( n \) and \( 0_{l,g} \) is a \( l \times g \) null matrix. \( w_k \) represents the prediction noise which is here assumed to be zero-mean Gaussian for all variables in \( X_k \) with a covariance matrix \( Q \), such that \( w_k \sim \mathcal{N}(0, Q) \).

In Eq.(1), \( B = [I_2 \Delta k \quad I_2]^T \) is a control input model and \( \Delta k \) is the sampling time. \( U_{S_k^m} = [\dot{x}_k, \dot{y}_k]^T \) is a control vector that encodes the expected agent's velocity when its state belongs to a discrete region \( S_k^m \in \mathcal{S}^m \). Discrete regions associated with a model \( m \) can be represented as:

$$S^m = \{S^{m,l^m}\}_{l^m=1,\ldots,L^m},\tag{2}$$

where \( l^m \) and \( L^m \) represent the index and the maximum number of super-states respectively. Additionally, a threshold value is defined where linear continuous models of super-states \( S^m \) are valid. Such a threshold is defined as:

$$\psi_{S^m} = E(d_{S^m}) + 3\sqrt{V(d_{S^m})},\tag{3}$$

where \( d_{S^m} \) is a vector containing all distances between neighboring super-states, \( E(\cdot) \) receives a vector of data and calculates its mean and \( V(\cdot) \) its variance. The threshold value in Eq.(3) defines a certainty boundary that determines where the model is valid, determining the extent of the *knowledge* captured by the model.

Let \( Z_k \) be the observed agent's position at the instant \( k \) while executing a given experience, see Fig. 2-b.1. It is assumed a linear relationship between measurements and agent's states, such that:

$$Z_k = HX_k + \nu_k,\tag{4}$$

where \( H = [I_d \quad 0_{d,d}] \) is an observation matrix that maps states onto observations and \( \nu_k \) represents the measurement noise produced by the sensor device which is here assumed to be zero-mean Gaussian with a covariance matrix \( R \), such that, \( v_k^m \sim \mathcal{N}(0, R) \). By considering the dynamical filter in Eq.(1), it is possible to estimate the agents' velocity by using the KFs' innovations produced by a model \( m \), such that:

$$v_k^m = \frac{Z_k - H \hat{X}_{k+1|k}^m}{\Delta k},\tag{5}$$

where \( \hat{X}_{k+1|k}^m \) is the state space estimation under the model \( m \) at the time \( k+1 \) given observations until time \( k \). \( \Delta k \) is the sampling time. By considering a 2-dimensional space, i.e., \( d = 2 \), the agent's state can be written as: \( X_k = [x_k, y_k, \dot{x}_k, \dot{y}_k]^T \).

Initial model. The initial model $m=0$ is a situation where the agent keeps the same position over time. A KF based on an “unmotivated model” in Fig. 2-a.1 is used to tracking agents.

The model $m=0$ contains only one super-state $\boldsymbol{S}^{\mathbf{0}}=\{S_{1}^{0}\}$, leading to $U_{S_{1}^{0}}\sim 0$. By relaxing $BU_{S_{k}^{m}}$ in Eq.(1), we obtain: $X_{k+1}=AX_{k}+w_{k}$, where the agent is assumed to move only under random noisy fluctuations $w_{k}$. By applying Eq.(5), innovations obtained from the initial model $m=0$ can be collected and used to create new models incrementally.

Creating models incrementally. As shown in Fig. 1-c, during the inference, there are two different possible situations.
i) Normality: the observation can be fitted and predicted with the current learned model(s). In this case, there is no need to learn new models and Eq. (1) is used to infer future states.
ii) Abnormality: the current observation does not fit in the existing model(s), which means it is out of the boundary defined in Eq.(3), where a random filter $U_{S_{k}^{m}}=0_{2,1}$ is applied. In this case, the abnormal data is used to learning a new model $m+1$. For SL, this corresponds to learning a MKF in Fig. 2-d.1, where the agent’s dynamics can be described by quasi-constant velocity models, i.e., $U_{S_{k}^{m}}\neq 0$ in Eq.(1).

The state information of instances detected as abnormal is collected to learning new models. We employ a SOM [50] that receives stored abnormal states $X_{k}$ and generates a set of neurons encoding similar information (quasi-constant velocities). Consequently, the set of super-states will be updated, such that:

$$
\boldsymbol{S}^{m+1}=\left\{S^{m+1, l^{m+1}}\right\}_{l^{m+1}=1, \ldots, L^{m+1}}
$$

The clustering process prioritizes similar velocities (actions) based on a weighted distance. Consequently, Eq. (7) shows a distance function that uses the weights $\beta$ and $\alpha$ employed to train the SOM, where $\beta+\alpha=1$ and $\alpha>\beta$ to favor clustering of patterns with small differences in velocity, such that:

$$
d(\tilde{X}, \tilde{Y})=\sqrt{(\tilde{X}-\tilde{Y})^{\top} D(\tilde{X}-\tilde{Y})}
$$

where $D=\left[\begin{array}{ll}\mathcal{B} & \mathcal{A}\end{array}\right] \cdot \mathcal{B}=\left[\begin{array}{lll}\beta I_{2} & 0_{2,2}\end{array}\right]^{\top}, \mathcal{A}=\left[\begin{array}{lll}0_{2,2} & \alpha I_{2}\end{array}\right]^{\top} \cdot \tilde{X}$ and $\tilde{Y}$ are both 4-dimensional vectors of the form $[x \quad y \quad \dot{x} \quad \dot{y}]^{\top}$.

By analyzing the activated super-states over time while executing a certain activity, it is possible to obtain a set of temporal transition matrices $T_{t}^{m}$. Those matrices encode the probabilities of passing or staying between super-states depending on the time $t$ that the agent has spent in a superstate while model $m$ is applied. Transition matrices facilitate the inference of next super-states given the current one, i.e., $p\left(S_{k}^{m} \mid S_{k-1}^{m}, t\right)$.

Each new model is identified in an unsupervised fashion and added to the model set $\boldsymbol{M}=\{m\}_{m=1, \ldots, M}$. While the agent perform a task, all transition matrices $T_{t}^{m}$ apply in parallel and the model with minimum error $m_{k,(m i n)}$ is selected as the correct one, such that:

$$
m_{k,(m i n)}=\underset{m}{\arg \min }\left(v_{k}^{m}\right)
$$

In case $v_{k}^{m_{k,(m i n)}}>\psi_{\boldsymbol{S}^{m}}$, the selected model $m_{k,(m i n)}$ is not valid and a new model must be added to the available ones, see Eq.(16). Similarly, a new set of temporal transition matrices $T_{t}^{m+1}$ are calculated for the new detected model.
![img-2.jpeg](img-2.jpeg)

Fig. 3: Proposed DBN switching models for (a) private layer, (b) shared layer

## C. Mathematical modeling of PL layer

Cross-modal GAN representation. Unlike the SL, the PL deals with high-dimensional visual information observed by the agent. Namely, a sequence of images (frames) $\mathcal{I}$, and their corresponding optical-flow maps (motion) $\mathcal{O}$. To model the PL of SA, a set of cross-modal GANs [42] is trained to learn the normality from a set of visual data. Generative models try to maximize likelihood by minimizing the Kullback-Leibler distance between a given data distribution and the generator’s distribution [51]. GANs learn such a minimization during the training phase by an adversarial game between two networks: a generator $(G)$ and a discriminator $(D)$.

As mentioned before, a SA model has to be generative (predict multi-level, temporal data series based on previously learned knowledge) and discriminative (provide measurements to evaluate or select best-fitting models in new observations). In the case of GANs, Generative networks learn to predict. In particular, our predictions include the generation of the next image (frame) and optical-flow (motion map). This could be seen as a hidden state $\mathcal{X}_{k}^{P}$ (see Fig. 3). The update task includes having the likelihood and prediction. In GANs, the likelihood is learned and approximated by the Discriminators. The outputs of the Discriminators are the encoded version of optical-flow $\mathcal{D}^{\mathcal{O}}$ and image $\mathcal{D}^{\mathcal{I}}$. In our approach, Discriminators' scores are used to approximate the distance between the likelihood and the prediction.

Intuitively, the encoded version of an image can be seen as the state in SL, while the encoded version of opticalflow represents its motion. The error $\mathcal{E}$ can be seen as the distances between the encoded versions of prediction and the observation. Following the same intuition applied in SL, we cluster the encoded version of images, motion and errors into a set of super-states. In light of the above, the states here can be defined as a function of image, motion, and error $f\left(\left[\mathcal{D}^{\mathcal{I}}, \mathcal{D}^{\mathcal{O}}, \mathcal{E}\right]\right)$ for any model (super-state).
Dynamic modeling. GANs are commonly used to generate data (e.g., images) and trained using only unsupervised data. Supervisory information in a GAN is indirectly provided by an adversarial game between two independent networks: a

generator $(G)$ and a discriminator $(D)$. During training, $G$ generates new data and $D$ tries to distinguish whether its input is real (i.e., a training image) or it was generated by $G$. The competition between $G$ and $D$ helps to boost the ability of both $G$ and $D$. For learning conditions of equilibrium, two channels are used as observations: appearance (rawpixels) and motion (optical-flow images) for two different cross-channel tasks. In the first task, optical-flow images are generated from the original frames. In the second task, appearance information is estimated from an optical flow image. Specifically, let $\mathcal{I}_{k}$ be the $k$-th frame of a training video and $\mathcal{O}_{k}$ the optical-flow obtained through $\mathcal{I}_{k}$ and $\mathcal{I}_{k+1}$. $\mathcal{O}_{k}$ is computed using [52]. For any given model $m^{\prime} \in \boldsymbol{M}^{\prime}$, where $\boldsymbol{M}^{\prime}=\left\{m^{\prime}\right\}_{m^{\prime}=1, \ldots, M^{\prime}}$, two networks are trained: $\mathcal{N}^{m^{\prime}: \mathcal{I} \rightarrow \mathcal{O}}$, which generates optical-flow from frames (task 1) and $\mathcal{N}^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}$, which outputs frames from optical-flow (task 2). In both cases, inspired by [43], [53], our architecture is composed of two fully-convolutional networks: the conditional generator $G$ and discriminator $D . G$ is the U-Net architecture [53], which is an encoder-decoder following with skip connections helping to preserve relevant local information. $D$ is the PatchGAN discriminator [53], which is based on a "small" fully-convolutional discriminator. $G$ and $D$ are trained using both a conditional GAN loss $\mathcal{L}_{c G A N}$ and a reconstruction loss $\mathcal{L}_{L 1}$. In case of $\mathcal{N}^{m^{\prime}: \mathcal{I} \rightarrow \mathcal{O}}$, the training set is composed of pairs of frame-optical flow images $\mathcal{X}=\left\{\left(F_{t}, O_{t}\right)\right\}_{t=1, \ldots, N}$. $\mathcal{L}_{L 1}$ is given by: $\mathcal{L}_{L 1}(x, y)=\|y-G(x, z)\|_{1}$,

$$
\mathcal{L}_{L 1}(x, y)=\|y-G(x, z)\|_{1}
$$

where $x=F_{t}$ and $y=O_{t}$, while the conditional adversarial loss $\mathcal{L}_{c G A N}$ is:

$$
\begin{gathered}
\mathcal{L}_{c G A N}(G, D)=\mathbb{E}_{(x, y) \in \mathcal{X}}[\log D(x, y)]+ \\
\mathbb{E}_{x \in\left\{F_{t}\right\}, z \in \mathcal{Z}}[\log (1-D(x, G(x, z)))] .
\end{gathered}
$$

In case of $\mathcal{N}^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}$, we define $\mathcal{X}=\left\{\left(O_{t}, F_{t}\right)\right\}_{t=1, \ldots, N}$. Additional details about the training can be found in [53]. In the GANs' training phase, networks $\mathcal{N}^{m^{\prime}: \mathcal{I} \rightarrow \mathcal{O}}$ and $\mathcal{N}^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}$ learn a dynamic model for the continuous space.

The discrete level uses an encoded vector $C_{k}^{m^{\prime}}=$ $\left[D^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}\left(\mathcal{I}_{k}, \mathcal{O}_{k}\right), D^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}\left(\mathcal{I}_{k}, \mathcal{O}_{k}\right)\right]$, where $D^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}$ and $D^{m^{\prime}: \mathcal{I} \rightarrow \mathcal{O}}$ are the discriminator networks of $\mathcal{N}^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}$ and $\mathcal{N}^{m^{\prime}: \mathcal{I} \rightarrow \mathcal{O}}$, respectively. Encoded vectors represent the expected entity's motion when its state belongs to a region $C_{k}^{m^{\prime}}$, where $m^{\prime}$ is a given model. Discrete regions of a given model $m^{\prime}$ are written as:

$$
\boldsymbol{C}^{\boldsymbol{m}^{\prime}}=\left\{C^{m^{\prime}, l^{m^{\prime}}}\right\}_{l^{m^{\prime}}=1, \ldots, L^{m^{\prime}}}
$$

where $C_{k}^{m^{\prime}} \in \boldsymbol{C}^{\boldsymbol{m}^{\prime}}$ and $L^{m^{\prime}}$ is the total number of super-states in a task $m^{\prime}$. Additionally, a threshold is employed to define where linear continuous models of super-states $\boldsymbol{C}^{m^{\prime}}$ are valid. The threshold can be written as:

$$
\psi_{\boldsymbol{C}^{m^{\prime}}}=E\left(\mathcal{D}_{\boldsymbol{C}^{m^{\prime}}}\right)+3 \sqrt{V\left(\mathcal{D}_{\boldsymbol{C}^{m^{\prime}}}\right)}
$$

where $\mathcal{D}_{\boldsymbol{C}^{m^{\prime}}}$ contains all cross-modal discriminators likelihoods over the super-states, $E(\cdot)$ and $V(\cdot)$ are defined in Eq.(3). Note that Eq.(3) determines the extend of the knowledge captured by GANs.

Initial model. GANs are trained in a weakly-supervised manner, their only supervision consists of a subset of normal data to train the first level of the hierarchy that we name reference GANs, which corresponds to U-KF in case of SL for low-dimensional data. The reference GANs is trained to model an initial equilibrium condition where the agent moves linearly towards a fixed motivation point. The reference GANs provide a baseline for the next levels of the models, in which all of them are trained in a self-supervised way.

Similar to the SL initial model, the PL initial model $m^{\prime}=0$ contains a single super-state $\boldsymbol{C}^{\mathbf{0}}=\left\{C_{1}^{0}\right\}$, containing the reference GANs. Details of the training are shown in Alg. 1. The inputs of the procedure are represented by two sets: $\mathcal{Z}$ represents an observation vector including all normal observations from the training data and $\mathcal{V}_{m^{\prime}}$, which is a subset of $\mathcal{Z}$. In case of the reference GANs, the initial set $\mathcal{V}_{0}$ is used to train two cross-modal networks $\mathcal{N}^{0: \mathcal{I} \rightarrow \mathcal{O}}$, and $\mathcal{N}^{0: \mathcal{O} \rightarrow \mathcal{I}}$. Note that the only supervision consists of training the first model (reference GANs) on the initial set $\mathcal{V}_{0}$. the next models are built from the supervision provided by the reference GANs.

Moreover, the mismatches between the reference GANs estimation and new observations lead to errors that, in turn, are used to detect new conditions of equilibrium.
Creating models incrementally. As described in Sec.I, our method assumes that the distribution of the normality patterns has a high degree of diversity. To learn such a distribution, we suggest a hierarchical strategy for high-diversity areas by encoding the different distributions into the different levels, in which each subset of train data is used to train a different GAN. A recursive procedure is adopted to construct the proposed hierarchy of GANs. As shown in Alg. 1, the input set $\mathcal{Z}$ includes a set of coupled Frame-Motion maps, where $\mathcal{Z}=\left\{\left[\mathcal{I}_{k}, \mathcal{O}_{k}\right]\right\}_{k=1, \ldots, N}$, and $N$ is the number of total train samples. Besides, the input $\mathcal{V}_{m^{\prime}}$ is a subset of $\mathcal{Z}$, provided to train GANs for each model.

After training $\mathcal{N}^{0: \mathcal{I} \rightarrow \mathcal{O}}$, and $\mathcal{N}^{0: \mathcal{O} \rightarrow \mathcal{I}}$, we input $G^{0: \mathcal{I} \rightarrow \mathcal{O}}$ and $G^{0: \mathcal{O} \rightarrow \mathcal{I}}$ using each frame $\mathcal{I}$ of the entire set $\mathcal{Z}$ and its corresponding optical-flow image $\mathcal{O}$, respectively. The generators predict Frame-Motion couples as:

$$
\begin{aligned}
& \mathcal{X}^{0: \mathcal{P}}=\left\{\left[\mathcal{P}_{k}^{0: \mathcal{I}}, \mathcal{P}_{k}^{0: \mathcal{O}}\right]\right\}_{k=1, \ldots, N} \\
& \mathcal{P}_{k}^{0: \mathcal{I}}=G^{0: \mathcal{O} \rightarrow \mathcal{I}}\left(\mathcal{O}_{k}\right), \quad \mathcal{P}_{k}^{0: \mathcal{O}}=G^{0: \mathcal{I} \rightarrow \mathcal{O}}\left(\mathcal{I}_{k}\right)
\end{aligned}
$$

where $\mathcal{P}_{k}^{0: \mathcal{I}}$ and $\mathcal{P}_{k}^{0: \mathcal{O}}$ are the $k$-th predicted image and opticalflow, respectively. The encoded versions of observations $\mathcal{Z}$ are computed by the discriminator networks $D^{0}$ :

$$
\begin{gathered}
\mathcal{D}^{0: \mathcal{I}}=\left\{D^{0: \mathcal{O} \rightarrow \mathcal{I}}\left(\mathcal{I}_{k}, \mathcal{O}_{k}\right)\right\}_{k=1, \ldots, N} \\
\mathcal{D}^{0: \mathcal{O}}=\left\{D^{0: \mathcal{I} \rightarrow \mathcal{O}}\left(\mathcal{O}_{k}, \mathcal{I}_{k}\right)\right\}_{k=1, \ldots, N}
\end{gathered}
$$

where $\mathcal{D}^{0: \mathcal{I}}$ and $\mathcal{D}^{0: \mathcal{O}}$ are the encoded version (from initial model $m^{\prime}=0$ ) of the observed image and optical-flow, respectively. Encoded distance maps $\mathcal{E}^{0}$ between observations $\mathcal{Z}$ and predictions $\mathcal{P}$ for both channels are computed as:

$$
\begin{aligned}
& \boldsymbol{\mathcal { E } _ { k } ^ { 0 }}=\left\{\left[\boldsymbol{\mathcal { E }}_{k}^{0: \mathcal{I}}, \mathcal{E}_{k}^{0: \mathcal{O}}\right]\right\}_{k=1, \ldots, N} \\
& \mathcal{E}_{k}^{0: \mathcal{I}}=D^{0: \mathcal{O} \rightarrow \mathcal{I}}\left(\mathcal{I}_{k}, \mathcal{O}_{k}\right)-D^{0: \mathcal{O} \rightarrow \mathcal{I}}\left(\mathcal{P}^{\mathcal{I}}, \mathcal{O}_{k}\right) \\
& \mathcal{E}_{k}^{0: \mathcal{O}}=D^{0: \mathcal{I} \rightarrow \mathcal{O}}\left(\mathcal{O}_{k}, \mathcal{I}_{k}\right)-D^{0: \mathcal{I} \rightarrow \mathcal{O}}\left(\mathcal{P}_{k}^{\mathcal{O}}, \mathcal{I}_{k}\right)
\end{aligned}
$$

The distance maps $\boldsymbol{\mathcal { E } ^ { 0 }}$ represent a set of errors in the coupled image-motion states representation, The joint states

$\left\{\left[\mathcal{D}_{k}^{0: \mathcal{I}}, \mathcal{D}_{k}^{0: \mathcal{O}}, \mathcal{E}_{k}\right]\right\}_{k=1, \ldots, N}$ input to a SOM that clusters similar appearance-motion information. Similar to clustering position-velocity information in the shared layer, the proposed clustering groups the appearance-motion representations into a set of super-states. Specifically, the SOM's output is a set of neurons encoding the state information into a set of prototypes. Detected prototypes (clusters) provide the means of discretization for representing a set of super-states, and consequently, the set of super-states will be updated, such that:

$$
\boldsymbol{C}^{m^{\prime}+1}=\left\{C^{m^{\prime}+1, l^{m^{\prime}+1}}\right\}_{l^{m^{\prime}+1}=1, \ldots, L^{m^{\prime}+1}}
$$

where $L^{m^{\prime}+1}$ is the number of detected clusters (super-states) for the new model(s).

It is expected that the clusters containing the training data present a low distance score due to low innovations between predictions and observations. This is the criteria to detect the new distributions for learning new GANs, in which the clusters with high average scores are considered as new distributions. The new detected distributions forming the new subsets $\mathcal{V}_{l}$ to train new networks $\mathcal{N}^{C^{m^{\prime}}: \mathcal{I} \rightarrow \mathcal{O}}$, and $\mathcal{N}^{C^{m^{\prime}}: \mathcal{O} \rightarrow \mathcal{I}}$ for the new GAN models. New identified models add to the model set $\boldsymbol{M}^{\prime}=\left\{m^{\prime}\right\}_{m^{\prime}=1, \ldots, M^{\prime}}$. During a task performing by the agent, all the transition matrices $T_{l}^{m^{\prime}}$ apply in parallel. The selected model (best-fitted model) will be selected based on the minimum error $m^{\prime}{ }_{k,(m i n)}$, such that:

$$
m_{k,(m i n)}^{\prime}=\underset{m^{\prime}}{\arg \min }\left(\mathcal{E}_{k}^{m^{\prime}}\right)
$$

In case $\mathcal{E}_{k}^{m^{\prime}{ }_{k,(m i n)}}>\psi_{\boldsymbol{C}^{m^{\prime}}}$, the selected model $m^{\prime}{ }_{k,(m i n)}$ is not valid and a new model must be added to the available ones, see Eq.(16). Similarly, a new set of temporal transition matrices $T_{l}^{m+1}$ are calculated for the new detected model.

This procedure continues until no new distribution is detected. GANs and detected super-states in each level are stacked incrementally for constructing the entire GAN model set $\mathcal{H}_{C^{m^{\prime}}}$. The incremental nature of the proposed method makes it capable of learning complex distributions of data in a self-supervised manner.

## III. AbNORMALITY DETECTION: AN ONLINE APPLICATION

## A. Shared layer: on-line testing MJPF

As mentioned before, the SL model can be learned using a SDS, see Fig. 3 (b). Such a model includes a discrete set of state regions subspaces corresponding to the switching variables. The quasi-constant velocity model described before in Eq. (1), is employed in each region to describe the relation between consecutive states in time. A further learning step facilitates to obtain the temporal transition matrices between super-states. An MJPF is used to infer posterior probabilities on discrete and continuous states iteratively, see Fig. 4. Our MJPF uses a PF at the discrete level, embedding in each particle KF. In other words, each particle in the PF uses a KF, which depends on the super-state $S_{K}^{m}$; see Eq. (1). Such a filter predicts the continuous state associated with a super-state $S_{k}^{m}$, where $p\left(X_{k} \mid X_{k-1}, S_{k-1}^{m}\right)$; and the posterior probability $p\left(X_{k}, S_{k}^{m} \mid Z_{k}\right)$ is estimated using the current observation $Z_{k}$.

Algorithm 1 Incremental training: Hierarchy of GANs
Input:

1: $\psi_{\mathcal{C}^{m^{\prime}}}$ : Threshold parameter for train a new GAN
2: $\boldsymbol{C}^{m^{\prime}}=\left\{C^{0}\right\}$
3: $\mathcal{Z}$ : Entire training sequences $\mathcal{Z}=\left\{\left(\mathcal{I}_{k}, \mathcal{O}_{k}\right)\right\}_{k=1, \ldots, N}$
4: $\mathcal{V}_{0}$ : Subset of $\mathcal{Z}$
5: $m^{\prime}=0$ : Counter of models
Output:
6: $\left\{\mathcal{H}_{\mathcal{C}^{m^{\prime}}}\right\}$ Hierarchy of GANs
7: procedure TRAINING OF CROSS-MODAL GANs
8: train:
9: $\quad$ Train networks $\mathcal{N}^{m^{\prime}: \mathcal{I} \rightarrow \mathcal{O}}, \mathcal{N}^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}$, with $\mathcal{V}_{m^{\prime}}$
10: $\left\{\mathcal{H}_{\mathcal{C}^{m^{\prime}}}\right\} \leftarrow$ Trained networks $\mathcal{N}^{m^{\prime}: \mathcal{I} \rightarrow \mathcal{O}}, \mathcal{N}^{m^{\prime}: \mathcal{O} \rightarrow \mathcal{I}}$
11: $\mathcal{X}^{m^{\prime}: \mathcal{P}} \leftarrow G^{m^{\prime}}(\mathcal{Z})$ : predictions
12: $\mathcal{D}^{m^{\prime}} \leftarrow D^{m^{\prime}}(\mathcal{Z})$ : encoded observation
13: $\mathcal{E}^{m^{\prime}} \leftarrow\left\|D^{m^{\prime}}(\mathcal{Z})-D^{m^{\prime}}\left(\mathcal{X}^{m^{\prime}: \mathcal{P}}\right)\right\|_{1}$ : error
14: $\mathcal{X} \leftarrow\left[\mathcal{D}_{m^{\prime}}, \mathcal{E}_{m^{\prime}}\right]$ : states
15: Clustering states: $S O M(\mathcal{X})$ : super-states $\boldsymbol{C}^{m^{\prime}}$
16: for each identified cluster do
17: $\mu \leftarrow$ Average score maps in this cluster
18: if $\mu \geq \psi_{\boldsymbol{C}^{m^{\prime}}}$ then
19: $\quad m^{\prime}=m^{\prime}+1$
20: $\mathcal{V}_{m^{\prime}} \leftarrow$ Samples from cluster $C^{m^{\prime}}$ in $\mathcal{Z}$
21: go to train
22: return $\left\{\mathcal{H}_{\mathcal{C}^{m^{\prime}}}\right\}$

Abnormalities can be seen as deviations between MJPF's predictions and the actual observed trajectories. As a probabilistic filtering approach is considered, two main moments can be distinguished: $i)$ Prediction: estimation of future states at a given time $k$. ii) Update: computation of the state's posterior probability based on the comparison between predicted states and new measurements. Accordingly, abnormality behaviors can be measured in the update phase, i.e., when predicted probabilities are far from observations. As it is well known, innovations in KFs are defined as:

$$
\epsilon_{k}^{m}=Z_{k}-H \hat{X}_{k \mid k-1}^{m}
$$

where $\epsilon_{k}^{m}$ is the innovation generated in the zone $m$ where the agent is located at a time $k . Z_{k}$ represents observed spatial data and $\hat{X}_{k \mid k-1}^{m}$ is the KF estimation of the agent's location at the future time instant $k$ calculated at the time $k-1$ by using Eq. (1). Additionally, $H$ is the observation model that maps measurements into states, such that $Z_{k}=H X_{k}+v$ where $v \sim \mathcal{N}(0, R)$ and $R$ is the covariance observation noise.

Abnormalities are moments when a tracking system fails to predict subsequent observations. Consequently, we propose a weighted norm of innovations for detecting them, such that:

$$
\mathcal{Y}_{k}^{m}=\mathbf{d}\left(Z_{k}, H \hat{X}_{k \mid k-1}^{m}\right)
$$

In the MJPF, the expression shown in Eq. (19) is computed for each particle and the median of such values is used as a global anomaly measurement of the filter. Further details about the implemented method can be found in [44].

![img-3.jpeg](img-3.jpeg)

Fig. 4: Online phase: An MJPF makes inferences on the DBN

### *B. Private Layer: On-line testing GANs*

Once the GANs hierarchy {*H<sub>Cm</sub><sup>i</sup>*} is trained, it can be used for online prediction and anomaly detection purposes. This section describes the testing phase for state/label estimation and the proposed method for the detection of abnormalities.

*Label estimation*: At testing time, we aim at estimating the state and detect possible abnormalities from the training set. More specifically, let *D<sup>0:ℤ→Ơ</sup>* and *D<sup>0:Ơ→ℤ</sup>* be the patch-based discriminators trained using the two channel-transformation tasks. Given a test frame *I<sub>k</sub>* and its corresponding optical-flow image *O<sub>k</sub>*, we first produce the reconstructed *P<sup>0:Ơ</sup><sub>k</sub>* and *P<sup>0:ℤ</sup><sub>k</sub>* using the first level generators *G<sup>0:ℤ→Ơ</sup>* and *G<sup>0:Ơ→ℤ</sup>*, respectively. Then, the pairs of patch-based discriminators *D<sup>0:ℤ→Ơ</sup>* and *D<sup>0:Ơ→ℤ</sup>*, are applied for the first and the second task, respectively. This operation results in two score maps for the observation: *D<sup>0:ℤ→Ơ</sup>*(O<sub>k</sub>, I<sub>k</sub>) and *D<sup>0:Ơ→ℤ</sup>*(I<sub>k</sub>, O<sub>k</sub>), and two score maps for the prediction (the reconstructed data): *D<sup>0:ℤ→Ơ</sup>*(P<sup>0:Ơ</sup><sub>k</sub>, I<sub>k</sub>) and *D<sup>0:Ơ→ℤ</sup>*(P<sup>0:ℤ</sup><sub>k</sub>, O<sub>k</sub>). In order to estimate the state, we used Eq. (15) to generate the joint representation *X<sub>k</sub>* = [*X<sub>k</sub><sup>T</sup>*, *X<sub>k</sub><sup>O</sup>*], where:

$$
\begin{aligned}
& \mathcal{X}_k^{\mathcal{T}} = D^{0:Ơ \rightarrow \mathcal{I}} (\mathcal{I}_k, \mathcal{O}_k) - D^{0:Ơ \rightarrow \mathcal{I}} (\mathcal{P}^{\mathcal{I}}, \mathcal{O}_k), \\
& \mathcal{X}_k^{\mathcal{O}} = D^{0:I \rightarrow O} (\mathcal{O}_k, \mathcal{I}_k) - D^{0:I \rightarrow O} (\mathcal{P}_k^{\mathcal{O}}, \mathcal{I}_k)
\end{aligned} \tag{20}
$$

For estimating the current super-state, we use *X<sub>k</sub>* to find the closest SOM's detected prototypes. This procedure is repeated for all the models in the hierarchy [*H<sub>Cm</sub><sup>i</sup>*]. This model can be seen as a switching model (see Fig. 3), where a hierarchy of GANs estimates the continuous space of the states whereas a hidden Markov model predicts the discrete space of the states. *Anomaly detection*: Note that, a possible abnormality in the observation (e.g., an unusual object or an uncommon movement) corresponds to an outlier with respect to the data distribution learned by *N<sup>m</sup><sub>I</sub>*:I→O and *N<sup>m</sup><sub>O</sub>*:O→I during training. The presence of the anomaly, results in a low value of prediction score maps: *D<sup>m</sup><sub>O</sub>*:O→I(P<sup>I</sup>, O<sub>k</sub>) and *D<sup>m</sup><sub>I</sub>*:I→O(P<sup>O</sup><sub>k</sub>, I<sub>k</sub>), but a high value of observation score maps: *D<sup>m</sup><sub>I</sub>*:O→I(I<sub>k</sub>, O<sub>k</sub>) and *D<sup>m</sup><sub>I</sub>*:I→O(O<sub>k</sub>, I<sub>k</sub>). Hence, to decide whether an observation is normal or abnormal, we calculate the average value of the *innovations maps* introduced in Eq. (20) from both modalities. Therefore, the final abnormality measurement is defined as:

$$
\theta_k = \overline{\mathcal{X}_k^{\mathcal{T}}} + \overline{\mathcal{X}_k^{\mathcal{O}}}
$$

The final representation of PL for an observation *Z<sub>k</sub>* = (I<sub>k</sub>, O<sub>k</sub>) consists of the computed *θ<sub>k</sub>* and estimated super-state *C<sup>m</sup><sub>k</sub><sup>I</sup>*. We define an error threshold *θ<sub>t</sub><sup>h</sup>* = *ψ<sub>Cm</sub><sup>i</sup>* to detect the abnormal events: when all the levels in the hierarchy of GANs classify a sample as abnormal (e.g., dummy super-state) and the measurement *θ<sub>k</sub>* is higher than *θ<sub>t</sub><sup>h</sup>*, the current measurement is considered as an abnormality. Note that the process is aligned to the one in the SL layer, with the advantage that GANs deal with high multi-dimensional inputs and non-linear dynamic models at the continuous level. This complexity is required to analyze video data involved in PL.

### IV. EXPERIMENTAL RESULTS

In this section, first, we introduce our collected dataset, then present the off-line training process for each layer of the self-awareness model, and finally, we demonstrate the results of online abnormality detection for the proposed test scenarios.

#### *A. Experimental Dataset*

In our experiments, an iCab vehicle [54] driven by a human operator is used to collect the dataset. We obtain the vehicle's positions mapped into Cartesian coordinates from the odometry manager [54], as well as captured video footage from a first-person vision acquired by a built-in camera of the vehicle. For the SL, measurements of the iCab's positions and its flow components are considered. Furthermore, for the cross-modal GANs in the PL, we input the captured video frames and their corresponding optical-flow maps.

Accordingly, this work considers three situations (experiments): *Scenario I)* or normal perimeter monitoring, where the vehicle follows a rectangular trajectory around a building (see Fig. 14-a). *Scenario II)* or U-turn, where the vehicle performs a perimeter monitoring and faces a pedestrian, so it makes a U-turn to continue the task in the opposite direction (see Fig. 14-b). *Scenario III)* or emergency stop, where the vehicle encounters pedestrians crossing its path and stops until the pedestrian leaves its field of view (see Fig. 14-c).

Situations II and III contain deviations from the perimeter monitoring task. When an observation falls outside the super-state, as the learned models are not valid, a *dummy neuron* is used to represent the new experience, and random filter where *U* = 0<sub>2,1</sub> in Eq. (1) is employed for prediction purposes.

#### *B. Training SL and PL*

The two layers of the proposed self-awareness model, including the SL (modeled by a MJPF) and the PL (modeled as a hierarchy of GANs), are able to learn the normality. In our experiments, normal behaviors are performed as Scenario I (Fig. 14-a). Such a scenario is used as a training set to learn both models (SL and PL). For each layer, we use different observations. Accordingly, SL uses positional information while PL utilizes first-person visual data. In the rest of this section, we show the training process and output of each layer.

![img-4.jpeg](img-4.jpeg)

Fig. 5: U-KF's estimations

![img-5.jpeg](img-5.jpeg)

Fig. 7: U-KF's innovations

![img-6.jpeg](img-6.jpeg)

Fig. 6: Learned filter's estimations

![img-7.jpeg](img-7.jpeg)

Fig. 8: Learned filter's innovations

Fig. 9: SL state estimation: (a) and (b) correspond to the estimations made by the U-KF and the learned filter respectively. Abnormality signals in SL: (c) and (d) show the innovations generated by the U-KF and the learned filter respectively.

Fig. 10: PL state estimation: (a) and (b) are the estimated video frame and optical-flow motion map from the *reference GAN* while the vehicle moves toward a linear path. (c) and (d) are the estimations from the *reference GAN* while the vehicle curving, (e) and (f) are the same samples predicted by the hierarchy of GANs after training. Each triplet image contains the ground truth observation (left), the predicted frame (center), and the difference between prediction optical-flow map and the ground truth where black pixels indicate a high accuracy at the prediction stage.

**Initial model in SL.** As we discussed in Sec. II, the reference filter for the shared layer is a U-KF; see Fig. 2-(a.1), which assumes the simple condition of equilibrium in which the agent is not moving. A sequence of state estimation samples of U-KF is shown in Fig. 5. In this figure, U-KF always predicts the agent will stay in a still position, including a negligible perturbation error; see small velocity vectors in red. However, this assumption is not true in the observed data; see large velocity vectors in blue in Fig. 5 and leads to large innovation values such as shown in Fig. 7.

**Training incremental models in SL.** By applying the reference filter U-KF over the training data, a set of innovation values can be obtained. This set of innovations is plotted in Fig. 7, and it is used in the next training iteration to learn new filters incrementally as described in Sec. II-B (see Fig. 2-(d.1)). The new set of MKFs encode models that describe new conditions of equilibrium and whose estimations are more accurate estimations than the ones produced by the U-KF when dealing again with similar abnormal situations, compare blue and red arrows in 6. It can be seen that predictions are close to the observations, producing low errors, i.e., low innovation values, as shown in Fig. 8.

**Initial model in PL.** As mentioned in Sec. II-C, constructing the GAN hierarchical model is done based on the distance of discriminators scores between the predictions and the real observations. The first level of GANs (*reference GANs*) is trained on a selected subset of normal samples from *perimeter monitoring* sequence. This subset represents the captured sequences while the vehicle moves on a linear path in a normal situation, i.e., when the road is empty and the vehicle moves linearly. The hypothesis is that this subset only represents one of the motion distributions and appearance in a highly diverse data condition. As a result, when the pair of *reference GANs* detects an abnormality in the corresponding set on which is trained, the corresponding observations can be considered as outliers. This hypothesis is confirmed by testing the *reference GANs* over the entire sequences of *perimeter monitoring*, and observing the discriminators' scores distances between the prediction and the observation. Fig. 11 shows the results of training *reference GANs*. Our hypothesis concerning the complexity of distributions is confirmed in Fig. 11 (a), where the test is performed using only the *reference GANs*.

**Training incremental models in PL.** As shown in Fig. 11, *reference GANs* can predict/detect the linear path (white background area) perfectly. On the other hand, when the vehicle curves (green bars), the system fails and recognizes curving as an abnormal event. This means, the *reference GAN* discriminators' scores distances between the prediction and the observation (abnormality signal) are higher over the curving areas, which was expected. However, after collecting this set of abnormal data and training the second level of GANs, the newly learned models facilitate recognizing the entire training sequence as normal.

The estimation of optical-flow and frame for each level (iteration) of the training process is shown in Fig. 10. For each case, an image triplet is shown, where the left image

is the ground truth observed frame, the central image shows the predicted frame, and the right image is the difference between the observed optical-flow motion map and the predicted optical-flow. The lower the distance between predicted motion and observation, the blacker (values are near to " 0 ") the right image. In this figure, (a), (b), (c), and (d) show the output estimation for the initial GANs. As can be seen, straight motions displayed in (a) and (b) are correctly estimated; see the low error, i.e., black pixels, in the right frames of their triplets. Nonetheless, the initial model is unable to predict curve motions shown in (c) and (d), see the high error, i.e., colorful pixels, in the right frames of their triplets. Fig. 10 (e) and (f) show the estimation from the hierarchy of GANs after a full training phase in case of curving. It can be observed this time how the GANs estimate the curving motion with high accuracy, see the number of black pixels in the triplet's right frames.

As the reference GANs are trained on the reference situation which is the linear movements (see Fig. 2-(a.2)), therefore is it expected to having a good estimation while the vehicle moving linearly (Fig. 10-a-b). However, this filter fails to estimate curves (Fig. 10-c and d). The incremental nature of the proposed method is demonstrated in Fig. 2-(d.2), where low estimation errors are obtained by using the second level GANs for predicting curve motions, see 10-e-f.
![img-8.jpeg](img-8.jpeg)

Fig. 11: Training hierarchy of GANs: (a) ground truth labels, the green background means the vehicle moves on a linear path, while the blue bars indicate curving. (b) and (c) show the signal of the averaged score distance values between prediction and observation (innovation) for the first level of GANs and the hierarchy of GANs, respectively. Horizontal and vertical axes encode time and innovation values correspondingly.

## C. Representation of normality in SL and PL

After training SL and PL over the training sequence, to evaluate the final learned models, we select a period of the normal perimeter monitoring task (see Fig. 14-a) as a test scenario. As reviewed in Sec. II both SL and PL, represent their situation awareness by a set of super-states following and abnormality signals. This set of results for PL and SL is shown in Fig. 13, which simply visualizes the learned normality representations. The ground truth label is shown in Fig. 13-a, and the color-coded detected super states from PL $\left\{C^{m^{\prime}}\right\}$ and SL $\left\{S^{m}\right\}$ are illustrated in Fig. 13-b and Fig. 13-c, respectively. It clearly shows that the pattern of super-states is repetitive and highly-correlated with the ground truth. It also
![img-9.jpeg](img-9.jpeg)

Fig. 12: Color-coded zones from SL and PL.
![img-10.jpeg](img-10.jpeg)

Fig. 13: Normality representations of PL and SL: (a) shows the ground truth labels, green and blue bars represent linear and curve motions respectively. (b) and (c) show color-coded super-states sequences $\left\{C_{k}^{m^{\prime}}\right\}$ and $\left\{S_{k}^{m}\right\}$ respectively. They are highly correlated with the agent's real status (a). Images (d) and (e) show the abnormality signals from PL and SL, respectively. The horizontal axes in (d) and (e) are the sample numbers, and the vertical axes show the abnormality signals.
shows a strong correlation between the sequence of PL and SL super-states.

The study of the cross-correlation between the SL and PL is beyond the scope of this paper. Nonetheless, it is also interesting to demonstrate such a relation. For showing the correlation of both learned models (SL and PL), we divided the environment into eight meaningful zones, including curves and linear paths. This semantic partitioning of state-space is shown in Fig. 12. For the training scenario (normal situation), the color-coded super-states of SL and PL are visualized over the environment plane. As shown in Table. II, for the SL we detect 115 super-states, each of them corresponding to an individual filter. For PL, we have detected seven different super-states, corresponding to trained cross-modal GANs.

Note that in Fig. 13 (d) and (e), abnormality signals are stable for both PL and SL due to the presence of normal data. In the case of abnormalities, peaks (high local values) are expected over the signals. To study such abnormal situations, we apply the trained models over unseen test sequences. Two different scenarios are selected where the agent performs new maneuver actions in order to solve the abnormal situation.


TABLE II: List of corresponding detected super-states from PL and SL for the normal scenario: for each zone, the number of color-coded super-states sequences from PL $\left(\left\{C_{k}^{m^{\prime}}\right\}\right)$ and SL $\left(\left\{S_{k}^{m}\right\}\right)$ are shown.

## D. Abnormality detection in dynamic data series

In this phase, we perform an online testing setup to evaluate the performance of our models. This procedure for the SL is shown in Fig. 2-(b.1), (c.1) and (d.1). For the PL, it is shown in Fig. 2-(b.1), (c.1) and (d.1).
Avoiding a pedestrian by a U-turn action: In this scenario, which is illustrated in Fig. 14-b, the vehicle performs a Uturn avoidance maneuver when encounters a static pedestrian and then continues the standard monitoring in the opposite sense. The goal is to detect the abnormality, consisting of the pedestrian presence, which leads to unexpected agent's actions when compared to the learned normality during the perimeter monitoring. Fig. 15 shows the result of anomaly detection from PL and SL. The results are related to the highlighted time slice of the testing scenario II (Fig. 14-b).

In Fig. 15-a, the green background represents a vehicle's linear path, the blue bars indicate curving, and red bars show the presence of an abnormal situation (which corresponds to the static pedestrian). The abnormality area starts at first sight of the pedestrian, and it continues until the avoiding maneuver finishes (end of U-turn). Similarly, the sequences of states $\left\{C_{k}^{m^{\prime}}\right\}$ and $\left\{S_{k}^{m}\right\}$ in Fig. 15-(b,c), follow the same pattern. While the situation is normal, the super-states repeat the expected normal pattern, but as soon as the abnormality begins, the super-state patterns change in both PL and SL (e.g., dummy super-states). Furthermore, in the abnormal superstates, the abnormality signals present higher values. The abnormality signal (innovations)generated by SL is shown in Fig. 15-e. The abnormality produced by the vehicle is higher while it moves through the path, which is indicated by red arrows in Fig. 14-b. This is caused by the observations that are outside the domain where super-states are trained. Namely, during the training phase, such a state-space configuration is never observed. Additionally, KF's innovations become higher in the same time interval due to the opposite velocity compared with the normal behavior of the model.

The abnormality signal generated by PL, Fig. 15-d, is computed by averaging over the distance maps between prediction and observation score maps: when an abnormality arises, the proposed measure does not undergo large changes since a local abnormality (see Fig. 17-c) can not change the average value significantly. However, as soon as it is observed a full sight of the pedestrian, and the vehicle starts performing the avoidance maneuver, the abnormality signal becomes higher since both observed appearance and action represent unknown situations. This situation is shown in Fig. 17-(d,e). As soon as the agent back to the known situation (e.g., curving), the abnormality signal becomes lower.
Emergency stop maneuver: This scenario is shown in Fig. 14-c, where the agent performs an emergency stop for a pedestrian to cross. Accordingly, Fig. 16 displays the results of abnormality detection for the highlighted time slice shown in Fig. 14-c. In Fig. 16-a, the red bars indicate the abnormality areas, i.e., where the vehicle stops and waits until the pedestrian crosses. Such anomaly areas are represented as dummy super states from PL (light-blue color in Fig. 16-b) with high scores in the abnormality signal (see Fig. 16-d). The generated abnormality signal from PL increases smoothly as the agent gets a better visual of the pedestrian and reaches the peak when the agent (vehicle) stops and has a full visual of the walker. Once the pedestrian passes and the agent starts to continue its linear path, the signal drops sharply. Similarly, the abnormality signal from the SL representation model, see Fig. 16-e, shows two peaks corresponding to high innovation values. Those peaks represent the abnormality patterns associated with the emergency stop maneuver. In contrast with the PL signal, the SL signal reaches a sharp peak and then smoothly goes back to the normal level. Such a pattern indicates that the vehicle stops immediately and waits for a while, then it increases the velocity to start moving again under the normal conditions. As a consequence, different motion patterns with respect to those predicted are detected using the innovation values. The color-coded super-states also confirm this; see Fig. 16-c, where the green and dark-blue states are continued longer than what expected with respect to the normal pattern that learned from the previous observations.

## V. Discussion

The cross-modal representation: One of the novelties in our paper is using GANs for a multi-channel data representation. Specifically, we use appearance and motion (optical-flow) information: a two-channel approach that has been proved to be empirically significant in previous works. Moreover, we propose to use a cross-channel strategy, where we train two networks that transform raw-pixel images into opticalflow representations and vice-versa. The reasoning behind this relies on the architecture of our conditional generators $G$, which are based on an encoder-decoder (see Sec. II-C). Such a channel-transformation task prevents $G$ from learning a trivial identity function by forcing $G$ and $D$ to construct sufficiently informative internal representations.
Private layer and shared layer cross-correlation: The PL and SL levels are providing complementary information regarding the situation awareness. As an instance, it has been observed that PL's super-states are invariant to the agent's location, while SL's super-states representation is sensitive to such spatial information. In other words, PL representation can be seen as the semantic feature of the agent's situation awareness (e.g., moving linearly, curving) regardless of its current location. Hence, the pattern of super-states sequences

![img-11.jpeg](img-11.jpeg)

Fig. 14: Sub-sequence examples from testing scenarios reported in the experimental results.

![img-12.jpeg](img-12.jpeg)

Fig. 15: Abnormality in the U-turn avoiding scenario: (a) ground truth labels. (b) and (c) color-coded transition of states {C<sup>m</sup><sub>k</sub>} and {S<sup>m</sup><sub>k</sub>}, respectively. (d) and (e) generated abnormality signal (innovation) from PL and SL, respectively. The horizontal axis represents the sample number, and the vertical axis shows the innovation values (abnormality signal).

![img-13.jpeg](img-13.jpeg)

Fig. 16: Abnormality in the emergency stop scenario: (a) ground truth labels. (b) and (c) color-coded transition of states from PL and SL, respectively. (d) and (e) generated abnormality signal (innovation) {C<sup>m</sup><sub>k</sub>} and {S<sup>m</sup><sub>k</sub>}, respectively. The horizontal axis represents the sample number, and the vertical axis shows the innovation values (abnormality signal).

is repetitive; see how PL's super-states are repeated in Table II, e.g., Zone 1, 3, 5 are 4 correspond to the same super-states. In contrast, the SL representation includes spatial information, which generates more specific super-states for describing each

![img-14.jpeg](img-14.jpeg)

Fig. 17: Visualization of abnormality: the first column shows the localization over the original frame, the second column is the predicted frame, and the last column shows the pixel-by-pixel distance over the optical-flow maps. (a) moving linear, (b) curving, (c) first observation of the pedestrian, (d) and (e) performing the avoiding action.

zone, see table II. In light of the above, these two representations carry complementary information and define a cross-correlation between PL and SL situations. A coupled Bayesian network could represent such cross-correlation, enabling a potential improvement on the detection of abnormality and consequently boost the entire self-awareness model.

Performance of the method: Time and accuracy performances of the proposed method are shown in Table III.


TABLE III: Computational time and accuracy of the proposed method. $A U C_{1}$ and $A U C_{2}$ are the area under the curve of the ROC in the U-turn and emergency stop respectively.

The computational time in Table III refers to the time required to analyze, predict, and detect abnormalities in an instance of position and visual data. Increasing the number of particles in the SL improves the accuracy of the method while requiring more time. Since sampling times of positional are video data are 110 ms and 50 ms respectively. SL's computational time with 50 particles $(\sim 65 \mathrm{~ms})$ can handle realtime processing of positions. Nonetheless, PL's computational time $(\sim 190 \mathrm{~ms})$ cannot handle real-time video processing in multiple GANs, however, this can be improved significantly using only a single model which either is capable to expand itself gradually [55], or learn the new concepts through a curriculum learning regime [56]. All the experimental results reported in this work are obtained through a MJPF that uses 50 particles.

## VI. CONCLUSION AND FUTURE WORK

This work has presented a multi-modal approach to detect abnormalities in a moving vehicle. The proposed models consider two levels (SL and PL) that handle different types of information. SL uses a state-space representation from an external observer, whereas PL employs a state-space representation from the analyzed agent. SL self-awareness employs a set of MKFs coupled with a PF to perform predictions. Innovations from filters are employed to build more complete models. On the other hand, PL self-awareness is modeled as a hierarchy of cross-modal GANs that learn complex data distributions in a weakly-supervised manner. Scores of the Discriminator network are used to approximate the complexity of data. Namely, a set of distance maps between prediction and observation scores is used as a criterion for creating new hierarchical levels in the proposed GAN structure. Our approach facilitates incrementally learning complex data distributions. Experimental results on a ground vehicle show the capability of our methodology to recognize anomalies using multiple viewpoints, namely PL and SL. This work opens some future research paths, such as (i) combining outputs from different sensorial sources that can lead to a more robust and unified SA decision-making. (ii) Optimizing of algorithms such that they can run on-device in a real-time fashion by using robotics middleware. (iii) considering more complex scenarios that include the interaction with other artificial agents, e.g., another ground vehicle or a drone, to accomplish cooperative tasks.
