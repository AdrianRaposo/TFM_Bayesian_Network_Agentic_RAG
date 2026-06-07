# Context-Based Path Prediction for Targets with Switching Dynamics 

Julian F. P. Kooij ${ }^{1}$ (D) $\cdot$ Fabian Flohr ${ }^{3}$ (D) $\cdot$ Ewoud A. I. Pool ${ }^{2}$ (D) $\cdot$ Dariu M. Gavrila ${ }^{1,2}$ (D)<br>Received: 18 December 2017 / Accepted: 21 June 2018 / Published online: 2 July 2018<br>(c) The Author(s) 2018


#### Abstract

Anticipating future situations from streaming sensor data is a key perception challenge for mobile robotics and automated vehicles. We address the problem of predicting the path of objects with multiple dynamic modes. The dynamics of such targets can be described by a Switching Linear Dynamical System (SLDS). However, predictions from this probabilistic model cannot anticipate when a change in dynamic mode will occur. We propose to extract various types of cues with computer vision to provide context on the target's behavior, and incorporate these in a Dynamic Bayesian Network (DBN). The DBN extends the SLDS by conditioning the mode transition probabilities on additional context states. We describe efficient online inference in this DBN for probabilistic path prediction, accounting for uncertainty in both measurements and target behavior. Our approach is illustrated on two scenarios in the Intelligent Vehicles domain concerning pedestrians and cyclists, so-called Vulnerable Road Users (VRUs). Here, context cues include the static environment of the VRU, its dynamic environment, and its observed actions. Experiments using stereo vision data from a moving vehicle demonstrate that the proposed approach results in more accurate path prediction than SLDS at the relevant short time horizon ( 1 s ). It slightly outperforms a computationally more demanding state-of-the-art method.


Keywords Intelligent vehicles $\cdot$ Path prediction $\cdot$ Situational awareness $\cdot$ Vulnerable road users $\cdot$ Intention estimation $\cdot$ Dynamic Bayesian Network $\cdot$ Probabilistic inference

## 1 Introduction

Anticipating how nearby objects will behave is a key challenge in various application domains, such as intelligent vehicles, social robotics, and surveillance. These domains concern systems that navigate trough crowded environments,

[^0]that interact with their surroundings, or which detect potentially anomalous events. Predicting future situations requires understanding what the nearby objects are, and knowledge on how they typically behave. Object detection and tracking are therefore common first steps for situation assessment, and the past decade has seen significant progress in these fields. Still, accurately predicting the paths of targets with multiple motion dynamics remains challenging, since a switch in dynamics can result in a significantly different trajectory. People are an important example of such target. For instance, a pedestrian can quickly change between walking and standing.

To improve path prediction of objects with switching dynamics, we propose to exploit context cues that can be extracted from sensor data. Especially vision can provide measurements for a diverse set of relevant cues. But incorporating more observations in the prediction process also increases sensitivity to measurement uncertainty. In fact, uncertainty is an inherent property of any prediction on future events. To deal with uncertainties, we leverage existing probabilistic filters for switching dynamics, which are common for tracking maneuvering targets (Bar-Shalom


[^0]:    Communicated by Larry Davis.
    D Dariu M. Gavrila
    d.m.gavrila@tudelft.nl
    Julian F. P. Kooij
    j.f.p.kooij@tudelft.nl
    Fabian Flohr
    fabian.flohr@daimler.com
    Ewoud A. I. Pool
    e.a.i.pool@uva.nl
    1 Delft University of Technology, Mekelweg 2, 2628 CD Delft, The Netherlands

    2 AMLab, University of Amsterdam, Science Park 904, 1098 XH Amsterdam, The Netherlands

    3 Department of Environment Perception, Daimler AG, Wilhelm-Runge-Str. 11, 89081 Ulm, Germany

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Path prediction of vulnerable road users with switching dynamics. **a** The pedestrian can cross, or stop. Context for a crossing pedestrian's path includes vehicle trajectory, the pedestrian's awareness of the approaching vehicle, and pedestrian's position w.r.t. the curbside. **b** The cyclist approaching an intersection can cycle straight or turn left. Context includes the vehicle trajectory, the cyclist's expressed intent by raising an arm, and distance to the intersection

![img-1.jpeg](img-1.jpeg)

**et al. 2001).** Our proposed method therefore extends a Switching Linear Dynamical System (SLDS) with dynamic latent states that represent context. The resulting model is a Dynamic Bayesian Network (DBN) (Murphy 2002), where the latent states control the switching probabilities between the dynamic modes. We can utilize existing theory for approximate posterior inference in DBNs to efficiently compute predictive distributions on the future state of the target.

In this paper, we focus on applications in the Intelligent Vehicle (IV) domain. More specifically, we demonstrate our method on path prediction of pedestrians and cyclists, i.e. the so-called Vulnerable Road Users (VRUs). For automated vehicles, forecasting the future locations of traffic participants is a crucial input to plan safe, comfortable and efficient paths through traffic (Althoff et al. 2009; Paden et al. 2016). However, the current active pedestrian systems are designed conservatively in their warning and control strategy, emphasizing the current pedestrian state (i.e. position) rather than prediction, in order to avoid false system activations. Small deviations in the prediction of, say, 30 cm in the estimated lateral position of VRUs can make all the difference, as this might place them just inside or outside the driving corridor. Better predictions can therefore warn the driver further ahead of time at the same false alarm rate, and more reliably initiate automatic braking and evasive steering (Keller et al. 2011; Köhler et al. 2013).

We evaluate our approach on two scenarios. The first scenario that we target considers a pedestrian intending to laterally cross the street, as observed by a stereo camera onboard an approaching vehicle, see Fig. 1a. Accident analysis shows that this scenario accounts for a majority of all pedestrian fatalities in traffic (Meinecke et al. 2003). We argue that the pedestrian's decision to stop can be predicted to a large degree from three cues: the existence of an approaching vehicle on collision course, the pedestrian's awareness thereof, and the spatial layout of the static environment. Likewise, the second scenario considers a cyclist driving on the same lane as the ego-vehicle, who may turn left at an upcoming crossing in front of the vehicle, see Fig. 1b. This scenario also has three predictive cues, namely the cyclist raising an arm to indicate intent to turn at the crossing, the cyclist's proximity to the crossing, and the existence of an approaching vehicle.

Our approach is general though, and can be extended with additional motion types (e.g. pedestrian crossing the road in a curved path), or to other application domains, such as robot navigation in human-inhabited environments. Our method also does not prohibit the use of other sensors or computer vision methods than the ones considered here.

# 2 Related Work

In this section we discuss existing work on state estimation and path prediction, especially for pedestrians and cyclists. We also present different context cues from vision that have been explored to improve behavior prediction.

## 2.1 Detection and Tracking

*Object Detection* The classical object detection pipeline first applies a sliding window on the input image to extract image features at candidate regions, and classify each region as containing the target object. In recent years, state-of-the-art detection and classification performance is instead achieved by deep ConvNets trained on large datasets. For online applications, ConvNet architectures are now also achieving real-time performance by combining detection and classification in a single forward pass, e.g. Single Shot Multibox Detector (Liu et al. 2016) or YOLO (Redmon et al. 2016).

There are many datasets for pedestrian detection, e.g. those presented in Enzweiler and Gavrila (2009), and Dollár et al. (2012). For an overview on vision-based pedestrian detection, see surveys from Enzweiler and Gavrila (2009), Dollár et al. (2012) and Ohn-Bar and Trivedi (2016). For cyclists, there is the Tsinghua-Daimler Cyclist Benchmark from Li et al. (2016). These datasets make it possible to create sophisticated models that require large amounts of

training data, for instance for unified pedestrian and cyclist detection (Li et al. 2017), or recovering the 3D pose of vehicles and VRUs (Braun et al. 2016). Indeed, the IV domain is used in many challenging Computer Vision benchmarks, e.g. KITTI (Geiger et al. 2012; Menze and Geiger 2015) and ADE20K (Zhou et al. 2017), hence we expect VRU detection to improve even further in the near future.

State Estimation In the IV domain, state estimation is typically done in a 3D world coordinate system, where also information from other sensors (e.g. lidar, radar) is fused. Image detections can be projected to this world coordinates through depth estimation from monocular or stereo-camera setup (Hirschmüller 2008).

The per-frame spatial position of detections can then be incorporated in a tracking framework where the measurements are assigned to tracks, and temporally filtered. Filtering provides estimates and uncertainty bounds on the objects' true position and dynamical states. State estimation often models the state and measurements as a Linear Dynamical System (LDS), which assumes that the model is linear and that noise is Gaussian. In this case, the Kalman filter (KF) (Blackman and Popoli 1999) is an optimal filtering algorithm. In the intelligent vehicle domain, the KF is the most popular choice for pedestrian tracking (see Schneider and Gavrila 2013 for an overview). The Extended and Unscented KF (Meuter et al. 2008) can, to a certain degree, account for non-linear dynamical or measurement models, but multiple motion models are needed for maneuvering targets that alternate various dynamics.

The SLDS is a type of DBN which can model multiple possible dynamics. It extends the LDS with a top-level discrete Markov chain. At each time step, the state of this chain determines which of the various possible motion dynamics is applied to the underlying LDS, allowing to 'switch' the dynamics through discrete state transitions. Unfortunately, exact inference and learning in an SLDS becomes intractable, as the number of modes in the posterior distribution grows exponential over time in the number of the switching states (Pavlovic et al. 2000). There is however a large body of literature on approximate inference in such DBNs. One solution is to approximate the posterior by samples using some Markov Chain Monte Carlo method (Oh et al. 2008; Rosti and Gales 2004; Kooij et al. 2016). However, sampling is impractical for online real-time inference as convergence can be slow. Instead, Assumed Density Filtering (ADF) (Bishop 2006; Minka 2001) approximates the posterior at every time step with a simpler distribution. It has generally been applied to mixed discrete-continuous state spaces with conditional Gaussian posterior (Lauritzen 1992), and to discrete state DBNs, where it is also known as BoyenKoller inference (Boyen and Koller 1998). ADF will be further discussed in Sect. 3.2.

The Interacting Multiple Model (IMM) KF (Blackman and Popoli 1999) is another popular algorithm to track a maneuvering target, mixes the states of several KF filters running in parallel. It has been applied for path prediction in the intelligent vehicle domain for pedestrian (Keller and Gavrila 2014; Schneider and Gavrila 2013), and cyclists (Cho et al. 2011) tracking. IMM can be seen as doing an alternative form of approximate inference in a SLDS (Murphy 2002).

### 2.2 Context Cues for VRU Behaviors

Even though SLDSs can account for changes in dynamics, a switch in dynamics will only be acknowledged after sufficient observations contradict the currently active dynamic model. If we wish to anticipate instead of reacting to changes in dynamics, a model should include possible causes for change.

Various papers provide naturalistic studies on pedestrians behavior, e.g. during encounters at unsignalized crossing (Chen et al. 2017), to predict when a pedestrian will cross (Völz et al. 2016), or to categorizing danger in vehiclepedestrian encounters (Otsuka et al. 2017). Similar studies are also being performed for cyclists. Zernetsch et al. (2016) collected data at a single intersection for path prediction of a starting cyclists, and Hubert et al. (2017) used the same data to find indicators of cyclist starting behavior. Some studies have used naturalistic data to detect and classify critical vehicle-cyclist interactions at intersections (Sayed et al. 2013; Vanparijs et al. 2015; Cara and de Gelder 2015), while others use simulations to study bicycle motion at intersections (Huang et al. 2017; Zhang et al. 2017).

For online prediction of VRU behavior, cues must be extracted from sensor data. Especially computer vision provides many types of context cues, as the following subsections will discuss. From the extract features, behavior predicting can then be treated as a classification problem (Bonnin et al. 2014; Köhler et al. 2013). However, probabilistic methods integrate the inherent detection uncertainty directly into path prediction (Schulz and Stiefelhagen 2015a, b; Keller and Gavrila 2014; Kooij et al. 2014a).

Static Environment Cues The relation between spatial regions of an environment and typical behavior has been extensively researched in visual surveillance, where the viewpoint is static. For instance, different motion dynamics may frequently occur at specific space coordinates (Morris and Trivedi 2011; Kooij et al. 2016; Robicquet et al. 2016; Yi et al. 2016; Jacobs et al. 2017). Another approach is to interpret the environment, e.g. detect semantic regions and learn how these affect agent behavior (Kitani et al. 2012; Rehder and Kloeden 2015). Such semantics enable knowledge transfer to new scenes too (Ballan et al. 2016). In surveillance, agent models are also used to reason about intent (Bandyopadhyay et al. 2013), i.e. where the pedestrian intends to go.

In the IV domain, behavior is typically tied to road infrastructure (Oniga et al. 2008; Geiger et al. 2014; Kooij et al. 2014b; Sattarov et al. 2014; Pool et al. 2017). Road layout can be obtained from localization using GPS and INS sensors (Schreiber et al. 2013) to retrieve information map data on the surrounding infrastructure. SLAM techniques provide another means for accurate self-localization in a world coordinate frame, and are also used in automotive research (Geiger et al. 2012; Mur-Artal and Tardós 2017). Another approach is to infer local road layout directly from sensor data (Geiger et al. 2014; Yi et al. 2017). Here, too, semantic scene segmentation with ConvNets can be used to identify static and dynamic objects, and drivable road [c.f. Cityscapes benchmark (Cordts et al. 2016)].

Dynamic Environment Cues VRU behavior may also be influenced by other dynamic objects in their surrounding. For instance, social force models (Antonini et al. 2006; Helbing and Molnár 1995; Huang et al. 2017) expect agents to avoid collisions with other agents. Tamura et al. (2012) extended social force towards group behavior by introducing sub-goals such as "following a person". The related Linear Trajectory Avoidance model (Pellegrini et al. 2009) for short-term path prediction uses the expected point of closest approach to foreshadow and avoid possible collisions.

Neural nets can also learn how multiple agents move in each others presence (Alahi et al. 2016; Yi et al. 2016), even from a vehicle perspective (Karasev et al. 2016; Lee et al. 2017). In the IV domain, interaction of road users with the ego-vehicle is especially important. An often used indicator is the Time-To-Collision (TTC) which is the time that remains until a collision between two objects occurs if their course and speeds are maintained (Sayed et al. 2013). A related indicator is the minimum future distance between two agents, which like TTC assumes both travel with fixed velocity (Pellegrini et al. 2009; Cara and de Gelder 2015).

Beyond accounting for the presence of other road users, traffic participants also negotiate right of way to coordinate their actions. Rasouli et al. (2017) presents a study of such interactions between drivers and pedestrians.

Object Cues People may not always be fully aware of their surroundings, and inattentive pedestrians are an important safety case in the IV context. A study on pedestrian behavior prediction by Schmidt and Färber (2009) found that human drivers look for body cues, such as head movement and motion dynamics, though exactly determining the pedestrian's gaze is not necessary. Hamaoka et al. (2013) presents a study on head turning behaviors at pedestrian crosswalks regarding the best point of warning for inattentive pedestrians. They use gyro sensors to record head turning and let pedestrians press a button when they recognize an approaching vehicle. Continuous head estimation can be obtained by interpolating the results of multiple discrete orientation clas-
sifiers, adding physical constraints and temporal filtering to improve robustness (Enzweiler and Gavrila 2010; Flohr et al. 2015). Benfold and Reid (2009) uses a Histogram of Oriented Gradients (HOG) based head detector to determine pedestrian attention for automated surveillance. Ba and Odobez (2011) combines context cues in a DBN to model the influence of group interaction on focus of attention. Recent work uses ConvNets for real-time 2D estimation of the full body skeleton (Cao et al. 2017).

The full body appearance can also be informative for path prediction, e.g. to classify the object and predict a class-specific path (Klostermann et al. 2016), or to identify predictive poses. Köhler et al. (2013) rely on infrastructurebased sensors to classify whether a pedestrian standing at the curbside will start to walk. Keller and Gavrila (2014) estimates whether a crossing pedestrian will stop at the curbside using dense optical flow features in the pedestrian bounding box. They propose two non-linear, higher order Markov models, one using Gaussian Process Dynamical Models (GPDM), and one using Probabilistic Hierarchical Trajectory Matching (PHTM). Both approaches are shown to perform similar, and outperform the first-order Markov LDS and SLDS models, albeit at a large computational cost.

## 3 Proposed Approach

We are interested in predicting the path of an object with switching motion dynamics. We consider that nonmaneuvering movement (i.e. where the type of motion is not changing) is well captured by a LDS with a basic motion model [e.g. constant position, constant velocity, constant turn rate (Blackman and Popoli 1999)]. An SLDS combines multiple of such motion models into a single model, using an additional switching state to indicate which of the basic motion model is in use at any moment. These probabilistic models can express the state probability given all past position measurements (i.e. online filtering), or given all past and future measurements (i.e. offline smoothing). Similarly, it is also possible to infer future state probability given only the current past measurements (i.e. prediction). Details on inference will be presented in Sect. 3.2.

While the SLDS can provide good predictions overall, we shall demonstrate that this unfortunately comes at the cost of bad predictions when a switch in dynamics occurs between the current time step and the predicted time step. To tackle the shortcomings of the SLDS, we propose an online filtering and prediction method that exploits context information on factors that may influence the target's motion dynamics. More specifically, for VRU path prediction we consider three types of context, namely interaction with the dynamic environment, the relation of the VRU to the static environment, and the VRU's observed behavior.

The presented work offers several contributions:

1. We present a generic approach to exploit context cues to improve predictions with a SLDS. The cues are represented as discrete latent nodes in a DBN that extends the SLDS. These nodes influence the switching probabilities between dynamic modes of the SLDS. An algorithm for approximate online inference and path prediction is provided.
2. We apply our approach to VRU path prediction. Various context cues are extracted with computer vision. The context includes the dynamic environment, the static environment, and the target's behavior. The proposed approach goes beyond existing work in this domain that has considered no or limited context. We show the influence of different types of context cues on path prediction, and the importance of combining them.
3. Our work targets online applications in real-world environments. We use stereo vision data collected from a moving vehicle, and compare computational performance to a state-of-the-art method in the IV domain.

We shall now formalize the SLDS, and demonstrate with a simple example how context can improve prediction quality when an actual switch in dynamics occurs. Afterwards, we discuss approximate inference, and specify how our general approach can be applied to VRU path prediction.

### 3.1 Contextual Extension of SLDS

Given noisy positional measurements $Y_{t}$ of a moving target, the target's true dynamics can be modeled as a Linear Dynamical System (LDS) with a latent continuous state $X_{t}$. The process defines the next state as a linear transformation $A$ of the previous state, with process noise $\epsilon_{t} \sim \mathcal{N}(0, Q)$ added through linear transformation $B$. Observation $Y_{t}$ results from a linear transformation $C$ of the true state $X_{t}$ with also Gaussian noise $\eta_{t} \sim \mathcal{N}(0, R)$ added, referred to as the measurement noise.

A Switching LDS (SLDS) conditions the dynamics on a discrete switching state $M_{t}$. We shall consider that the switching state $M_{t}$ selects the appropriate state transformation matrix $A^{\left(M_{t}\right)}$ for the process model, though generally other LDS terms could also be conditioned on $M_{t}$, if needed. Accordingly, the SLDS process is here defined as

$$
\begin{gathered}
X_{t}=A^{\left(M_{t}\right)} X_{t-1}+B \epsilon_{t} \quad \epsilon_{t} \sim \mathcal{N}(0, Q) \\
Y_{t}=C X_{t}+\eta_{t} \quad \eta_{t} \sim \mathcal{N}(0, R)
\end{gathered}
$$

These equations can be reformulated as conditional distributions, i.e. $P\left(X_{t} \mid X_{t-1}, M_{t}\right)=\mathcal{N}\left(X_{t} \mid A^{\left(M_{t}\right)} X_{t-1}, B Q B^{\top}\right)$ and $P\left(Y_{t} \mid X_{t}\right)=\mathcal{N}\left(Y_{t} \mid C X_{t}, R\right)$. The first time step is defined
![img-2.jpeg](img-2.jpeg)

Fig. 2 Best viewed in color. Toy example of path prediction for a target (moving left to right) with two motion types. Four models are considered: a LDS with 1st- and 2nd-order state space, a SLDS, and the proposed Context-based SLDS (C-SLDS). Each model extrapolates the filtered dynamics three time steps ahead, resulting in a Gaussian distribution over the future state. Top: Spatial view where gray dots show the target's actual path. The noisy measurements are omitted for clarity. Black circles mark the target's position $t=5,10$ and 15 . Stars mark its corresponding future position. Colored lines and uncertainty ellipses show the predicted path, and the distribution at the prediction horizon of each model. Middle: Log likelihood over time of the true future position under the predictive distributions. Bottom: The evidence from the spatial context over time, used by the C-SLDS. If this context is 'activated' (white) the state transition probabilities are high and the C-SLDS acts like the 1st-order LDS, otherwise (black) it acts like the SLDS
by initial distributions $P\left(X_{0} \mid M_{0}\right)$ and and $P\left(M_{0}\right)$. The former expresses our prior knowledge about the position and movement of a new target for each switching state, the latter expresses the prior on the switching state itself. Note that the SLDS describes a joint probability distribution over sequences of observations and latent states. It is therefore a particular instance of a DBN.

As an example, consider predicting the future position of a moving target which exhibits two types of motion, namely, moving in positive $x$ direction (type A), and moving in positive $x$ and $y$ direction (type B). The target performs motion type A for 10 time steps, and then type B for another 10 time steps. The target's motion dynamics are known, and a LDS is selected to filter and predict its future position for three steps ahead. An LDS with a 1st-order state space only includes position in its state, $X_{t}=\left[x_{t}\right]$. The target velocity is assumed to be fixed. Each time step, this LDS adds the fixed velocity and random Gaussian noise to the position. For the considered target, the optimal fixed velocity of the LDS is an

![img-3.jpeg](img-3.jpeg)

Fig. 3 Context-based SLDS as directed graph, unrolled for two time slices. Discrete/continuous/observed nodes are rectangular/circular/shaded

average of the two possible motion directions. Figure 2 illustrates this example, and shows predictions made using this LDS in blue. The LDS provides poor predictive distribution which do not adapt to the target motion.

An LDS with a 2nd-order state space also includes the velocity in the state, $X_t = [x_t, \dot{x}_t]^T$. Through process noise on the velocity, this LDS can account for changes in the target direction. However, its spatial uncertainty grows rapidly when predicting ahead as the velocity uncertainty increases without bounds. The figure shows its predictions in purple.

An SLDS can instead combine multiple LDS instances, each specialized for one motion type. This example considers an SLDS combining two 1st-order LDSs, one with fixed horizontal, and one with fixed diagonal velocity. Less process noise is needed compared to the single LDS. The switching state is to 1/20 chance of changing motion types. The predictions of this SLDS, shown in red in the figure are better during each mode. It exploits that changes between modes are rare, and the prediction uncertainty is therefore smaller. However, this notion leads to bad results when half-way the rare switch does occur, as the log-likelihood plots shows. The SLDS thus delivers good predictions for typical time steps where the dynamics do not change, at the cost of inaccurate predictions for rare moments where the dynamics switch. But a switch could be part of expected behavior for maneuvering targets. Preferably, the model should deliver good predictions for typical or 'normal' tracks, even if these switch, at the cost of inaccurate predictions during rare tracks with anomalous behavior.

We make a simple observation to tackle the poor SLDS performance during a switch. Consider having information that the target approaches a region with higher probability of switching than usual, i.e. spatial context. Outside this region the SLDS behaves as before. But inside, the switching probability is set to 1/2, which makes every dynamic mode equally likely in the future such. The SLDS then behaves as the original 1st-order LDS. By selectively adapting the transition probabilities based on the spatial context, this model can ideally take best of both worlds, as the yellow log-likelihood plot in Fig. 2 confirms.

To obtain this behavior, the transition probability of the SLDS switching state is conditioned on additional discrete latent context variables (which will be specified in more detail later). These different context states can collectively be represented by a single discrete node $Z_t$. Each contextual configuration $Z_t = z$ defines a different motion model transition probability,

$$P(M_t = m_t | M_{t-1} = m_{t-1}, Z_t = z_t) = \mathcal{P}(M_t | M_{t-1}, Z_t) \tag{3}$$

$$P(Z_t = z_t | Z_{t-1} = z_{t-1}) = \mathcal{P}(Z_t | Z_{t-1}) \tag{4}$$

Here we use $\mathcal{P}(\cdot)$ to denote probability tables.

We also introduce a set of measurements $E_t$, which provide evidence for the latent context variables through conditional probability $P(E_t | Z_t)$. The bottom plot in Fig. 2 demonstrates this likelihood for the example. Even though the context $Z_t$ is discrete, during inference the uncertainty propagates from the observables to these variables, resulting in posterior distributions that assign real-valued probabilities to the possible contextual configurations.

Like the SLDS, this extended model is also a DBN. Figure 3 shows all variables as nodes in a graphical representation of the DBN. The arrows indicate that child nodes are conditionally dependent on their parents. The dashed arrows show conditional dependency on the nodes in the previous time step.

### 3.2 Online Inference

The DBN is used in a forward filtering procedure to incorporate all available observations of new time instances directly when they are received. We have a mixed discrete-continuous DBN where the exact posterior includes a mixture of $|M|^T$ Gaussian modes after $T$ time steps, hence exact online inference is intractable (Pavlovic et al. 2000). We therefore resort to Assumed Density Filtering (ADF) (Bishop 2006; Minka 2001) as an approximate inference technique. The filtering procedure consists of executing the three steps for each time instance: predict, update, and collapse. These steps will also be used for predicting the target's future path for a given prediction horizon, as described later in Sect. 3.4.

We will let $P_t(\cdot) \equiv P(\cdot | Y_{1:t-1}, E_{1:t-1})$ denote a prediction for time $t$ (i.e. before receiving observations $Y_t$ and $E_t$), and $P_t(\cdot) \equiv P(\cdot | Y_{1:t}, E_{1:t})$ denote an updated estimate for time $t$ (i.e. after observing $Y_t$ and $E_t$). Finally, $P_t(\cdot)$ is the collapsed or approximated updated distribution that will be carried over to the predict step of the next time instance $t+1$. Figure 4 shows a flowchart of the computational performed in the steps, which will now be explained in more detail.

![img-4.jpeg](img-4.jpeg)

Fig. 4 Flowchart of the three ADF steps in a single time instance. For simplicity, two motion models and three context states are assumed, and no example numbers are shown in the probability tables, except for the likelihoods of the context evidence $E_{t}$ and observed position $Y_{t}$. Table rows correspond to the model $M$ and/or context state $Z$ of the previous time step $t-1$, columns correspond to the model $M$ and/or context state $Z$ of the time step $t$. Within each probability table, cell blocks with thick lines correspond to a single $Z$ value, cell blocks with solid lines are normalized and therefore sum to one

### 3.2.1 Predict

To predict time $t$ we use the posterior distribution of $t-1$, which is factorized into the joint distribution over the latent discrete nodes $\widehat{P}_{t-1}\left(M_{t-1}, Z_{t-1}\right)$, and into the conditional distribution and the dynamical state, $\widehat{P}_{t-1}\left(X_{t-1} \mid M_{t-1}\right)=$ $\mathcal{N}\left(X_{t-1} \mid \widehat{\mu}_{t-1}^{\left(M_{t-1}\right)}, \widehat{\Sigma}_{t-1}^{\left(M_{t-1}\right)}\right)$.

First, the joint probability of the discrete nodes in the previous and current time steps is computed using the factorized transition tables of Eqs. (3) and (4),

$$
\begin{aligned}
& \bar{P}_{t}\left(M_{t}, M_{t-1}, Z_{t}, Z_{t-1}\right)=P\left(M_{t} \mid M_{t-1}, Z_{t}\right) \\
& \quad \times P\left(Z_{t} \mid Z_{t-1}\right) \times \widehat{P}_{t-1}\left(M_{t-1}, Z_{t-1}\right)
\end{aligned}
$$

Then for the continuous latent state $X_{t}$ we predict the effect of the linear dynamics of all possible models $M_{t}$ on the conditional Normal distribution of each $M_{t-1}$,

$$
\begin{aligned}
& \bar{P}_{t}\left(X_{t} \mid M_{t}, M_{t-1}\right)=\int P\left(X_{t} \mid X_{t-1}, M_{t}\right) \\
& \quad \times \widetilde{P}_{t-1}\left(X_{t-1} \mid M_{t-1}\right) \quad d X_{t-1}
\end{aligned}
$$

With the dynamics of Eq. (1), we find that the parametric form of (6) is the Kalman prediction step, i.e.

$$
\begin{aligned}
\bar{P}_{t}\left(X_{t} \mid M_{t}, M_{t-1}\right) & =\mathcal{N}\left(X_{t} \mid \widehat{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)}, \bar{\Sigma}_{t}^{\left(M_{t}, M_{t-1}\right)}\right) \\
\bar{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)} & =A^{\left(M_{t}\right)} \widehat{\mu}_{t-1}^{\left(M_{t-1}\right)}
\end{aligned}
$$

### 3.2.2 Update

The update step incorporates the observations of the current time step to obtain the joint posterior. For each joint assignment $\left(M_{t}, M_{t-1}\right)$, the LDS likelihood term is

$$
\begin{aligned}
P\left(Y_{t} \mid M_{t}, M_{t-1}\right) & =\int P\left(Y_{t} \mid X_{t}\right) \times \bar{P}_{t}\left(X_{t} \mid M_{t}, M_{t-1}\right) d X_{t} \\
& =\mathcal{N}\left(Y_{t} \mid C \bar{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)}, \bar{\Sigma}_{t}^{\left(M_{t}, M_{t-1}\right)}+R\right)
\end{aligned}
$$

where we make use of Eq. (2). Combining this with the prediction [Eq. (5)] and context likelihood $P\left(E_{t} \mid Z_{t}\right)$, we obtain the posterior as one joint probability table

$$
\begin{aligned}
\widehat{P}_{t} & \left(M_{t}, M_{t-1}, Z_{t}, Z_{t-1}\right) \propto P\left(Y_{t} \mid M_{t}, M_{t-1}\right) \\
& \times P\left(E_{t} \mid Z_{t}\right) \times \bar{P}_{t}\left(M_{t}, M_{t-1}, Z_{t}, Z_{t-1}\right)
\end{aligned}
$$

Here we normalized the r.h.s. over all possible assignments of $\left(M_{t}, Z_{t}, M_{t-1} Z_{t-1}\right)$ to obtain the distribution on the l.h.s. The posterior distribution over the continuous state,

$$
\begin{aligned}
\widehat{P}_{t}\left(X_{t} \mid M_{t}, M_{t-1}\right) & \propto P\left(Y_{t} \mid X_{t}\right) \times \bar{P}_{t}\left(X_{t} \mid M_{t}, M_{t-1}\right) \\
& =\mathcal{N}\left(X_{t} \mid \widehat{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)}, \widehat{\Sigma}_{t}^{\left(M_{t}, M_{t-1}\right)}\right)
\end{aligned}
$$

has parameters ( $\tilde{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)}, \tilde{\Sigma}_{t}^{\left(M_{t}, M_{t-1}\right)}$ ) for the $|M|^{2}$ possible transition conditions, which are obtained using the standard Kalman update equations.

In case there is no observation for a given time step, there is no difference between the predicted and updated probabilities, which means both Eqs. 11 and 12 simplify to $\widetilde{P}_{t}(\cdot)=\widetilde{P}_{t}(\cdot)$.

### 3.2.3 Collapse

In the third step, the state of the previous time step is marginalized out from the joint posterior distribution, such that we only keep the joint distribution of variables of the current time instance, which will be used in the predict step of the next iteration.
$\widetilde{P}_{t}\left(M_{t}, Z_{t}\right)=\sum_{M_{t-1}} \sum_{Z_{t-1}} \widehat{P}_{t}\left(M_{t}, M_{t-1}, Z_{t}, Z_{t-1}\right)$
Similarly, $\widetilde{P}\left(M_{t-1} \mid M_{t}\right)$ is straightforward to obtain,
$\widetilde{P}\left(M_{t-1}, M_{t}\right) \propto \sum_{Z_{t}} \sum_{Z_{t-1}} \widehat{P}_{t}\left(M_{t}, M_{t-1}, Z_{t}, Z_{t-1}\right)$
$\widetilde{P}\left(M_{t-1} \mid M_{t}\right)=\widetilde{P}\left(M_{t-1}, M_{t}\right) / \sum_{M_{t-1}} \widetilde{P}\left(M_{t-1}, M_{t}\right)$.
We approximate the $|M|^{2}$ Gaussian distributions from Eq. (12) by just $|M|$ distributions,

$$
\begin{aligned}
\widetilde{P}_{t}\left(X_{t} \mid M_{t}\right) & =\sum_{M_{t-1}} \widehat{P}_{t}\left(X_{t} \mid M_{t}, M_{t-1}\right) \times P\left(M_{t-1} \mid M_{t}\right) \\
& =\mathcal{N}\left(X_{t} \mid \widetilde{\mu}_{t}^{\left(M_{t}\right)}, \widetilde{\Sigma}_{t}^{\left(M_{t}\right)}\right)
\end{aligned}
$$

Here, the parameters $\left(\widetilde{\mu}_{t}^{\left(M_{t}\right)}, \widetilde{\Sigma}_{t}^{\left(M_{t}\right)}\right)$ are found by Gaussian moment matching (Lauritzen 1992; Minka 2001),

$$
\begin{aligned}
\widetilde{\mu}_{t}^{\left(M_{t}\right)}= & \sum_{M_{t-1}} P\left(M_{t-1} \mid M_{t}\right) \times \widetilde{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)} \\
\widetilde{\Sigma}_{t}^{\left(M_{t}\right)}= & \sum_{M_{t-1}} P\left(M_{t-1} \mid M_{t}\right) \times\left[\widetilde{\Sigma}_{t}^{\left(M_{t}, M_{t-1}\right)}\right. \\
& \left.+\left(\widetilde{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)}-\widetilde{\mu}_{t}^{\left(M_{t}\right)}\right) \cdot\left(\widetilde{\mu}_{t}^{\left(M_{t}, M_{t-1}\right)}-\widetilde{\mu}_{t}^{\left(M_{t}\right)}\right)^{\top}\right]
\end{aligned}
$$

### 3.3 Context for VRU Motion

Until now the use of context in a SLDS has been described in general terms, but for VRU path prediction we distinguish a four binary context cues, $Z_{t}=\left\{Z_{t}^{\mathrm{DYN}}, Z_{t}^{\mathrm{STAT}}, Z_{t}^{\mathrm{ACT}}\right.$, $\left.Z_{t}^{\mathrm{ACTED}}\right\}$, which affect the probability of switching dynamics:
![img-5.jpeg](img-5.jpeg)

Fig. 5 DBN with context cues for VRU path prediction, unrolled for two time slices. Discrete/continuous/observed nodes are rectangular/circular/shaded. The binary context nodes represent interaction with the dynamic environment $Z_{t}^{\mathrm{DYN}}$, relation to the static environment $Z_{t}^{\mathrm{STAT}}$, and object behavior (i.e. how VRU acts, $Z_{t}^{\mathrm{ACT}}$, or has acted, $\left.Z_{t}^{\text {ACTED }}\right)$

- Dynamic environment context: the presence of other traffic participants can deter the VRU to move too closely. In our experiments we only consider the presence of the egovehicle. Context indicator $Z_{t}^{\mathrm{DYN}}$ thus refers to a possible collision course, and therefore if the situation is potentially critical.
- Static environment context: the location of the VRU in the scene relative to the main infrastructure. $Z_{t}^{\text {STAT }}$ is true iff the VRU is at the location where change typically occurs.
- Object context: $Z_{t}^{\text {ACT }}$ indicates if the VRU's current actions provide insight in the VRU's intention (e.g. signaling direction), or awareness (e.g. line of gaze). The related context $Z_{t}^{\text {ACTED }}$ captures whether the VRU performed the relevant actions in the past.

These cues are present in both the pedestrian and the cyclist scenario. The temporal transition of the context in $Z$ is now factorized in several discrete transition probabilities,

$$
\begin{aligned}
& P\left(Z_{t} \mid Z_{t-1}\right)=\mathcal{P}\left(Z_{t}^{\mathrm{STAT}} \mid Z_{t-1}^{\mathrm{STAT}}\right) \times \mathcal{P}\left(Z_{t}^{\mathrm{DYN}} \mid Z_{t-1}^{\mathrm{DYN}}\right) \\
& \quad \times \mathcal{P}\left(Z_{t}^{\mathrm{ACTED}} \mid Z_{t-1}^{\mathrm{ACTED}}, Z_{t}^{\mathrm{ACT}}\right) \times \mathcal{P}\left(Z_{t}^{\mathrm{ACT}} \mid Z_{t-1}^{\mathrm{ACT}}\right)
\end{aligned}
$$

The graphical model of the DBN obtained through this context factorization is shown in Fig. 5.

The latent object behavior variable, $Z^{\mathrm{ACT}}$, indicates whether the VRU is currently exhibiting behavior that signals a future change in dynamics. The related object context $Z^{\text {ACTED }}$ acts as a memory, and indicates whether the behavior has occurred in the past. For instance, the behavior of a

crossing pedestrian is affected by the pedestrian's awareness, i.e. whether the pedestrian has seen the vehicle approach at any moment in the past, $Z_{t}^{\mathrm{ACT}}=$ true for some $t^{\prime} \leq t$. The transition probability of $Z_{t}^{\text {ACTED }}$ encodes simply a logical OR between the Boolean $Z_{t-1}^{\text {ACTED }}$ and $Z_{t}^{\text {ACT }}$ nodes:
$\mathcal{P}\left(Z_{t}^{\text {ACTED }} \mid Z_{t-1}^{\text {ACTED }}, Z_{t}^{\text {ACT }}\right)=\left\{\begin{array}{ll}\text { true } & \text { iff }\left(Z_{t-1}^{\text {ACTED }} \vee Z_{t}^{\text {ACT }}\right) \\ \text { false } & \text { otherwise. }\end{array}\right.$

The context states have observables associated to them, except $Z^{\text {ACTED }}$ which is conditioned on the $Z^{\text {ACT }}$ state only. Hence, there are only three types of context observables, $E=\left\{E^{\mathrm{DYN}}, E^{\mathrm{STAT}}, E^{\mathrm{ACT}}\right\}$, which are assumed to be conditionally independent distributed given the context states. This yields the following factorization,

$$
\begin{aligned}
P\left(E_{t} \mid Z_{t}\right) & =P\left(E_{t}^{\mathrm{DYN}} \mid Z_{t}^{\mathrm{DYN}}\right) \times P\left(E_{t}^{\mathrm{STAT}} \mid Z_{t}^{\mathrm{STAT}}\right) \\
& \times P\left(E_{t}^{\mathrm{ACT}} \mid Z_{t}^{\mathrm{ACT}}\right)
\end{aligned}
$$

### 3.4 VRU Path Prediction

The goal of probabilistic path prediction is to provide a useful distribution $\bar{P}_{t_{p} \mid t}$ on the future target position,
$\bar{P}_{t_{p} \mid t}\left(X_{t+t_{p}}\right) \equiv \bar{P}\left(X_{t+t_{p}} \mid Y_{1: t}\right)$.
Here $t_{p}$ is the prediction horizon, which defines how many time steps are predicted ahead from the current time $t$. This formulation can reuse the steps from approximate online inference of Sect. 3.2, treating the unknown observations of the future time steps as 'missing' observations. Iterative application of these steps creates a predictive distribution of each moment in the future path, until the desired prediction horizon is reached.

However, the static environment context $Z^{\text {STAT }}$ exploits the relation between VRU's position and the static environment. Since the expected position is readily available during path prediction, we can estimate the future influence of the static environment on the predicted continuous state of the VRU. For instance, while predicting a walking pedestrian's path, we can also predict the decreasing distance of the pedestrian to the static curbside.

Accordingly, to obtain prediction $\bar{P}\left(X_{t+t_{p}} \mid Y_{1: t}\right)$ at time $t$ for $t_{p}$ time steps in the future, we use the current filtered state distribution and iteratively apply the Predict, Update and Collapse steps as before. However, the Update step now only includes measurements for the future static environment context using the expected VRU position. It does not have measurements for the object and dynamic environment indicators, thereby effectively skipping these context cues. Thus, to predicting future time steps, we replace Eq. (11) by
$\widehat{P}_{t}\left(M_{t}, M_{t-1}, Z_{t}, Z_{t-1}\right) \propto$

$$
P\left(E_{t}^{\mathrm{STAT}} \mid Z_{t}^{\mathrm{STAT}}\right) \times \bar{P}_{t}\left(M_{t}, M_{t-1}, Z_{t}, Z_{t-1}\right)
$$

This enables the method to predict when the change in dynamics will occur, if the VRU is inclined to do so.

## 4 VRU Scenarios

The previous section explained the general approach of using a DBN to incorporate context cues, infer current and future use of dynamics, and ultimately perform future path prediction. This section now specifies the dynamics and context used for the two VRU scenarios of interest.

### 4.1 Crossing Pedestrian

The first scenario concerns the pedestrian wanting to cross the road, and approaching the curb from the right, as illustrated in Fig. 1a.

Motion Dynamics In this scenario, we consider that the pedestrian can exhibit at any moment one of two motion types, walking $\left(M_{t}=m_{w}\right)$ and standing $\left(M_{t}=m_{s}\right)$. While the velocity of any standing person is zero, different people can have different walking velocities, i.e. some people move faster than others. Let $x_{t}$ denote a person's lateral position at time $t$ (after vehicle ego-motion compensation) and $\dot{x}_{t}$ the corresponding velocity. Furthermore, $\dot{x}^{m_{w}}$ is the preferred walking speed of this particular pedestrian. The motion dynamics over a period $\Delta t$ can then be described as,
$x_{t}=x_{t-\Delta t}+\dot{x}_{t} \Delta t+\epsilon_{t} \Delta t \quad \dot{x}_{t}=\left\{\begin{array}{ll}0 & \text { iff } M_{t}=m_{s} \\ \dot{x}^{m_{w}} & \text { iff } M_{t}=m_{w}\end{array}\right.$
Here $\epsilon_{t} \sim \mathcal{N}(0, Q)$ is zero-mean process noise that allows for deviations of the fixed velocity assumption. We will assume fixed time-intervals, and from here on set $\Delta t=1$.

Since the latent $\dot{x}^{m_{w}}$ is constant over the duration of a single track, $\dot{x}_{t}^{m_{w}}=\dot{x}_{t-1}^{m_{w}}$. Still, it varies between pedestrians. We include the velocity $\dot{x}^{m_{w}}$ in the state of an SLDS together with the position $x_{t}$ such that we can filter both. The prior on $\dot{x}_{0}^{m_{w}}$ represent walking speed variations between pedestrians. By filtering, the posterior on $\dot{x}_{t}^{m_{w}}$ converges to the preferred walking speed of the current track.

The switching state $M_{t}$ selects the appropriate linear state transformation $A^{\left(M_{t}\right)}$, and the matrices from Eq. (1) become
$X_{t}=\left[\begin{array}{c}x_{t} \\ \dot{x}_{t}^{m_{w}}\end{array}\right], A^{\left(m_{s}\right)}=\left[\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right], A^{\left(m_{w}\right)}=\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right], B=\left[\begin{array}{l}1 \\ 0\end{array}\right]$.

![img-6.jpeg](img-6.jpeg)

Fig. 6 Context observables used in the crossing pedestrian scenario. a The closest distance between pedestrian and the ego-vehicle. b The pedestrian head orientation. c The distance to the curb

The observations $Y_{t} \in \mathbb{R}$ from Eq. (2) are the observed lateral position. The observation matrix is defined as $C=\left[\begin{array}{lll}1 & 0\end{array}\right]$. The initial distribution on the state $X_{0}$ and both the process and measurements noise are estimated from the training data (see Sec. 5.4).

Context Following the study on driver perception (Schmidt and Färber 2009), the context cues in the pedestrian scenario are collision risk, pedestrian head orientation, and where the pedestrian is relative to the curb. The context observations $E_{t}$ for this scenario are illustrated in Fig. 6. The related Fig. 7 shows the empirical distributions of the context observations estimated on annotated training data from a pedestrian dataset. The dataset will be discussed in more detail in Sect. 5.1.

The dynamic environment context $Z^{\mathrm{DYN}}$ indicates whether the current trajectories of the ego-vehicle and pedestrian creates a critical situation. Namely, if there is a possible collision when both pedestrian and vehicle continue with their current velocities. For the interaction cue, we consider the minimum distance $D^{\min }$ between the pedestrian and vehicle if their paths would be extrapolated in time with fixed velocity (Pellegrini et al. 2009), see Fig. 6a. While this indicator makes naive assumptions about the vehicle and pedestrian motion, it is still informative as a measure of how critical the situation is. As part of our model, will thereby assist to make path prediction more accurate. We define a Gamma distribution over $D^{\min }$ conditioned on the latent interaction state $Z^{\mathrm{DYN}}$, parametrized by shape $a$ and scale $b$,
$P\left(E_{t}^{\mathrm{DYN}} \mid Z_{t}^{\mathrm{DYN}}=z\right)=\Gamma\left(D_{t}^{m i n} \mid a_{z}, b_{z}\right)$.
This distribution is illustrated in Fig. 7a.
The object behavior context $Z^{\mathrm{ACT}}$ describes if the pedestrian is seeing the approaching vehicle. $Z^{\text {ACTED }}$ indicates whether this was the case at any moment in the past, i.e. if the pedestrian did see the vehicle. It therefore indicates the pedestrian's awareness: a pedestrian will likely stop when he is aware of the fact that it is dangerous to cross. The HeadOrientation observable $H O_{t}$ serves as evidence $E_{t}^{\mathrm{ACT}}$ for the behavior. A head orientation estimator is applied to the head image region. It consists of multiple classifiers, each trained
to detect the head in a particular looking direction, and $H O_{t}$ is then a vector with the classifier responses, see Fig. 6b. The values in this vector form different unnormalized distributions over the classes, depending on whether the pedestrian is looking at the vehicle or not, see Fig. 7b. However, if the head is not clearly observed (e.g. it is too far, or in the shadow), all values are typically low, and the observed class distribution provides little evidence of the true head orientation. We therefore model $H O_{t}$ as a sample from a Multinomial distribution conditioned on $Z_{t}^{\mathrm{ACT}}$, thus with parameter vectors $p_{\text {true }}$ and $p_{\text {false }}$ for $Z^{\mathrm{ACT}}=$ true and $Z^{\mathrm{ACT}}=$ false respectively,
$P\left(E_{t}^{\mathrm{ACT}} \mid Z_{t}^{\mathrm{ACT}}=z\right)=\operatorname{Mult}\left(H O_{t} \mid p_{z}\right)$.

As such, higher classifier outputs count as stronger evidence for the presence of that class in the observation. In the other limit of all zero classifier outputs, $H O_{t}$ will have equal likelihood for any value of $Z_{t}^{\mathrm{ACT}}$.

The static environment context $Z^{\text {STAT }}$ indicates if the pedestrian is currently at the position next to the curb where a person would normally stop if they wait for traffic before crossing the road. The relative position of the pedestrian with respect to the curbside therefore serves as observable for this cue. As shown in Fig. 6c, we detect the curb ridge in the image. It is then projected to world coordinates with the stereo disparity to measure its lateral position near the pedestrian. These noisy measurements are filtered with a constant position Kalman filter with zero process noise, such that we obtain an accurate estimate of the expected curb position, $x_{t}^{\text {curb }}$. Distance-To-Curb, $D T C_{t}$, is then calculated as the difference between the expected filtered position of the pedestrian, $\mathbf{E}\left[x_{t}\right]$, and of the curb, $\mathbf{E}\left[x_{t}^{\text {curb }}\right]$. Note that for path prediction we can estimate $D T C$ even at future time steps, using predicted pedestrian positions. The distribution over $D T C_{t}$ given $Z^{\text {STAT }}$ is modeled as a Normal distribution, see Fig. 7c,
$P\left(E_{t}^{\text {STAT }} \mid Z_{t}^{\text {STAT }}=z\right)=\mathcal{N}\left(D T C_{t} \mid \mu_{z}, \sigma_{z}\right)$.

![img-7.jpeg](img-7.jpeg)

Fig. 7 Histograms and the fitted distributions of the context observations $E_{I}$ for the pedestrian scenario, conditioned on their GT context states $Z_{I}$ : a the minimum future distance between pedestrian and egovehicle, conditioned on $Z_{I}^{\mathrm{DYN}}$ (critical vs non-critical situation). b The
head orientation conditioned on $Z_{I}^{\mathrm{ACT}}$ (pedestrians sees vs does not see the ego-vehicle). c The pedestrian's distance to the curb, conditioned on conditioned on $Z_{I}^{\mathrm{STAT}}$ (not at curb vs at the curb)
![img-8.jpeg](img-8.jpeg)
(a) Time to approach, $T^{\min }$
![img-9.jpeg](img-9.jpeg)
(b) Arm Detection, $A D$
![img-10.jpeg](img-10.jpeg)
(c) Cyclist tracks relative to intersection center, DTI

The map's coordinate system is aligned with the intersection center. By projecting tracked cyclist positions to this coordinate system, their longitudinal distance to the intersection is obtained
![img-11.jpeg](img-11.jpeg)

Fig. 9 Histograms and the fitted distributions of the context observations $E_{I}$ for the cyclist scenario, conditioned on their GT context states $Z_{I}$ : a the time until the ego-vehicle would approach the cyclist, if both kept moving at the same speed, conditioned on $Z^{\mathrm{DYN}}$ (critical vs non-

### 4.2 Cyclist Approaching Intersection

The second scenario concerns the ego-vehicle driving behind a cyclist, and approaching an intersection. As illustrated in Fig. 1b, the cyclist may or may not turn left at the intersection, but can indicate intent to turn by raising an arm in advance. In our training data, the cyclist always does this when turning in a critical situation where the ego-vehicle is quickly approaching. But in non-critical situations, cyclists may turn even without raising an arm. The context observables of this scenario are illustrated in Figs. 8, and 9 shows the empirical
critical). b The arm detector's confidence conditioned on $Z^{\mathrm{ACT}}$ (cyclists has arm up vs arm down). c The cyclists' longitudinal position conditioned on $Z^{\mathrm{STAT}}$ (cyclist not at intersection vs at intersection)
distributions of the observables on the cyclist dataset that will be presented later in Sect. 5.2.

Motion Dynamics The cyclist can switch between the motion types cycling straight, $m_{s t}$, and turning left, $m_{l u}$. Since a turning cyclist changes velocity in both lateral $x$ and longitudinal $y$ direction, we now include both spatial dimensions in the cyclist's dynamic state. While the pedestrian model included only a latent velocity for the preferred walking speed, our cyclist models includes latent velocities for both

motion types. The matrices from Eq. (1) are as follows:
$X_{t}=\left[\begin{array}{lll}x_{t} & y_{t} & \dot{x}_{t}^{m_{t u}} & \dot{y}_{t}^{m_{t u}} & \dot{x}_{t}^{m_{s t}} & \dot{y}_{t}^{m_{s t}}\end{array}\right]^{\top}$
$A^{\left(m_{t u}\right)}=\left[\begin{array}{lll}I & I & 0 \\ 0 & I & 0 \\ 0 & 0 & I\end{array}\right] A^{\left(m_{s t}\right)}=\left[\begin{array}{lll}I & 0 & I \\ 0 & I & 0 \\ 0 & 0 & I\end{array}\right] B=\left[\begin{array}{l}I \\ 0 \\ 0\end{array}\right]$.

Here, $I$ defines as a $2 \times 2$ identity matrix, and 0 represents a $2 \times 2$ matrix of zeros. The observations $Y_{t} \in \mathbb{R}^{2}$ from Eq. (2) are the observed lateral and longitudinal position with observation matrix $C=\left[\begin{array}{lll}I & 0 & 0\end{array}\right]$.

Context In this scenario, the dynamic environment context $Z^{\mathrm{DYN}}$ indicates whether a situation would be critical if the cyclist would decide to turn left at that moment. Here we consider time $T^{\min }$ it would take for the vehicle to reach the cyclist, if both the vehicle and the cyclist would keep moving at the same speed. This is represented schematically in Fig. 8a. This is not a perfect prediction of the criticality of the situation, because the speed of the cyclist is not constant when turning left. But, similar as the pedestrian case, it still conveys useful information and will therefore improve the prediction. Figure 9a shows that the empirical distribution over $T^{\min }$ has multiple modes. We therefore define a mixture of $m$ Gaussians over $T^{\min }$, conditioned the dynamic context state $Z^{\mathrm{DYN}}$. From the data we find that $m=3$ for $Z^{\mathrm{DYN}}=$ true (the situation is critical), and that $m=2$ for $Z^{\mathrm{DYN}}=$ false. The Gaussian mixture is parametrized by means $\mu_{z d y n}^{(k)}$, covariances $\sigma_{z d y n}^{(k)}$ and the mixture weights $\phi_{z d y n}^{(k)}$,
$P\left(E_{t}^{\mathrm{DYN}} \mid Z_{t}^{\mathrm{DYN}}=z\right)=\sum_{k=1}^{m} \phi_{z d y n}^{(k)} \mathcal{N}\left(T_{t}^{m i n} \mid \mu_{z d y n}^{(k)}, \sigma_{z d y n}^{(k)}\right)$.

The object context $Z^{\mathrm{ACT}}$ captures whether the cyclist raises an arm to indicate intent to turn left, or not (see Fig. 8b). Accordingly, $Z^{\text {ACTED }}$ represents whether the cyclist did raise an arm in the past. For evidence $E^{\text {ACT }}$, an Arm-Detector provides a classification score $A D_{t}$ in the $[0,1]$ range, where a high score is indicative of a raised arm. The Beta distribution is a suitable likelihood function for this domain, see Fig. 9b. The distribution is parameterized by $\alpha_{z}$ and $\beta_{z}$,
$P\left(E_{t}^{\mathrm{ACT}} \mid Z_{t}^{\mathrm{ACT}}=z\right)=\operatorname{Beta}\left(A D_{t} \mid \alpha_{z}, \beta_{z}\right)$.
The static environment context $Z^{\text {STAT }}$ represents if the cyclist has reached the region around the intersection where turning becomes possible. Figure 8c shows that cyclist tracks have some variance in their turn angle and the location of onset. Rather than an exact spot, this region is a bounded range on the relative longitudinal distance of the cyclist to the
center of the intersection. The dashed lines in the figure mark this region. We rely on map information and ego-vehicle localization to estimate the longitudinal distance of the cyclist to the next intersection, the Distance-To-Intersection, $D T I_{t}$. As shown in Fig. 9c, the distribution over $D T I_{t}$ given $Z^{\text {STAT }}$ is also modeled as a mixture of $m$ Gaussians, using $m=1$ for $Z^{\text {STAT }}=$ true, and $m=2$ for $Z^{\text {STAT }}=$ false:
$P\left(E_{t}^{\text {STAT }} \mid Z_{t}^{\text {STAT }}=z\right)=\sum_{k=1}^{m} \phi_{z s t a t}^{(k)} \mathcal{N}\left(D T I_{t} \mid \mu_{z s t a t}^{(k)}, \sigma_{z s t a t}^{(k)}\right)$.

For path prediction we can estimate $D T I_{t}$ using the predicted cyclist positions and static map information.

## 5 Datasets and Feature Extraction

The experiments in this paper used two stereo-camera datasets of VRU encounters recorded from a moving vehicle, one for the crossing pedestrian and one for the cyclist at intersection scenario. Due to the focus on potentially critical situations, both driver and pedestrian/cyclist were instructed during recording sessions. A sufficient safety distance between vehicle and VRU was applied in all scenarios recorded. In the following sections, 'critical situation' thus refers to a theoretic outcome where both the approaching vehicle and pedestrian would not stop.

### 5.1 Pedestrian Dataset

For pedestrian path prediction, we use a dataset (c.f. Kooij et al. 2014a) consisting of 58 sequences recorded using a stereo camera mounted behind the windshield of a vehicle (baseline $22 \mathrm{~cm}, 16 \mathrm{fps}, 1176 \times 64012$-bit color images). All sequences involve single pedestrians with the intention to cross the street, but feature different interactions (Critical vs. Non-critical), pedestrian situational awareness (Vehicle seen vs. Vehicle not seen) and pedestrian behavior (Stopping at the curbside vs. Crossing). The dataset contains four different male pedestrians and eight different locations. Each sequence lasts several seconds (min / max / mean: $2.5 \mathrm{~s} / 13.3 \mathrm{~s} / 7.2 \mathrm{~s}$ ), and pedestrians are generally unoccluded, though brief occlusions by poles or trees occur in three sequences.

Positional ground truth (GT) is obtained by manual labeling of the pedestrian bounding boxes and computing the median disparity over the upper pedestrian body area using dense stereo (Hirschmüller 2008). These positions are then corrected for vehicle ego-motion provided by GPS and IMU, and projected to world coordinates. From this correction we obtain the pedestrian's GT lateral position, and use the temporal difference as the GT lateral speed.

Table 1 Breakdown of the number of tracks in the pedestrian dataset (c.f. Kooij et al. 2014a) for the four normal sub-scenarios (above the line), and in the anomalous one (below the line)


Table 2 Breakdown of the number of tracks in the cyclist dataset for the normal (above the line) and anomalous (below the line) sub-scenarios


The GT for context observations is obtained by labeling the head orientation of each pedestrian. The 16 labeled discrete orientation classes were reduced to 8 GT orientation bins by merging three neighbored orientation classes (c.f. Flohr et al. 2015) together.

This dataset is divided into five sub-scenarios, listed in Table 1. Four sub-scenarios represent 'normal' pedestrian behaviors (e.g. the pedestrian stops if he is aware of a critical situation and crosses otherwise). The fifth sub-scenario is 'anomalous' with respect to the normal sub-scenarios, since the pedestrian crosses even though he is aware of the critical situation.

### 5.2 Cyclist Dataset

A new dataset was collected for the cyclist scenario, in a similar fashion to the pedestrian dataset. This new dataset contains 42 sequences with another stereo camera setup in the vehicle (baseline $21 \mathrm{~cm}, 16 \mathrm{fps}, 2048 \times 102412$-bit color images). The cyclist and vehicle are driving on the same road, such that the cyclist is observed from the back, and they approach an intersection with an opportunity for the cyclist to turn left.

The cyclist GT positions are obtained similarly to the pedestrian scenario from stereo vision. To obtain information about the road layout further ahead, intelligent vehicles can rely on map information and self-localization. Since the cyclist scenario was collected in a confined road area, we use Stereo ORB-SLAM2 (Mur-Artal and Tardós 2017) on all collected stereo video to build a 3D map of the environment for our experiments. This results in a fixed world coordinate system shared by all tracks. The spatial layout of the crossing (road width and intersection point) is expressed in these world coordinates, and the detected cyclist positions can be projected to this global coordinate system too. In a pre-processing step GT cyclist tracks are smoothed to compensate for the estimation noise for stereo vision, which especially affects the longitudinal position. The aligned road layout and cyclist tracks are shown in Fig. 8c.

This dataset is also divided into several sub-scenarios, with the number of recordings for each sub-scenario listed in Table 2. We consider that initially the cyclist intent is unknown, i.e. whether he will turn or go straight at the intersection. By raising an arm, he can give a visual indication of the intent to turn left. However, the cyclist might not always properly raise an arm in non-critical situations. Therefore, in non-critical situations without raising an arm, our data contains an equal number of tracks with turning and going straight. In summary, the normal sub-scenarios reflect situations where the cyclist must indicate intent in critical situations with the approaching ego-vehicle, but could neglect to do this in non-critical cases. The additional anomalous sub-scenario contains a turning cyclist in a critical situation, without having raised an arm.

### 5.3 Feature Extraction

Both cyclist and pedestrian are detected by using neural networks with local receptive fields (Wöhler and Anlauf 1999), given region-of-interests supplied by an obstacle detection component using dense stereo data. The resulting bounding boxes are used to calculate a median disparity over the upper pedestrian body area. The vehicle ego-motion compensated position in world coordinates is then used as positional observation $Y_{t}$.

For an estimation of the pedestrian head orientation $H O_{t}$, the method described in Flohr et al. (2015) is used. The angular domain of $\left[0^{\circ}, 360^{\circ}\right)$ is split into eight discrete orientation classes of $0^{\circ}, 45^{\circ}, \cdots, 315^{\circ}$. We trained a detector for each class, i.e. $f_{0}, \cdots, f_{315}$, using again neural networks with local receptive fields. The detector response $f_{o}\left(I_{t}\right)$ is the strength for the evidence that the observed image region $I_{t}$ contains the head in orientation class $o$. We used a separate training set with 9300 manually contour labeled head samples from 6389 gray-value images with a min./max./mean pedestrian height of 69/344/122 pixels (c.f. Flohr et al. 2015). For additional training data, head samples were mirrored and shifted, and 22109 nonhead samples were generated in areas around heads and from false positive pedestrian detections. For detection, we generate candidate head regions in the upper pedes-

trian detection bounding box from disparity based image segmentation. The most likely head image region $I^{*}$ is selected from all candidates based on disparity information and detector responses. Before classification, head image patches are rescaled to $16 \times 16 p x$. The head observation $H O_{t}=\left[f_{0}\left(I_{t}^{*}\right), \cdots, f_{315}\left(I_{t}^{*}\right)\right]$ contains the orientation confidences of the selected region.

The expected minimum distance $D^{\min }$ between pedestrian and vehicle is calculated as in Pellegrini et al. (2009) for each time step based on current position and velocity. Vehicle speed is provided by on-board sensors, for pedestrians the first order derivative is used and averaged over the last 10 frames. For DTC, the curbside is detected with a basic Hough transform (Duda and Hart 1972). Though other approaches are available, e.g. stereo (Oniga et al. 2008) or scene segmentation (Cordts et al. 2016), this simple approach was already sufficient for our experiments. The image region of interest is determined by the specified accuracy of the vehicle localization using typical on-board sensors (GPS+INS) and map data (Schreiber et al. 2013). $Y_{t}^{\text {curb }}$ is then the mean lateral position of the detected line back-projected to world coordinates.

To determine whether the cyclist raises an arm $\left(A D_{t}=1\right)$, or not $\left(A D_{t}=0\right)$, we apply the chamfer matching approach from Gavrila and Giebel (2002). First, a binary foreground segmentation of the cyclist is generated from the disparity values in the tracked cyclist bounding box $r$. The foreground consists of all pixels with a disparity in the range of $\left[\bar{d}_{r}-\epsilon, \bar{d}_{r}+\epsilon\right]$. Here $\bar{d}_{r}$ is the median disparity value in region $r$. We set $\epsilon_{D}=1.5$ to account for disparity errors. The binary segmentation is then matched against multiple rectangular contour templates near the expected shoulder location in the bounding box. These arm templates vary in length, width and angle. The arm detector $A D_{t}$ is the output of a Naive Bayesian Classifier which integrates several likelihood terms over all templates: a Gamma distribution for the chamfer matching score, and a Gaussian mixture for both the intensity and disparity values in the segmented foreground. This classifier uses a uniform prior.

### 5.4 Parameter Estimation

Estimating the parameters of the conditional distributions is straightforward, if the values of the latent variables are known. We have therefore annotated the dataset with ground truth (GT) labels for all latent variables in the sequences. During training, the distributions are then fitted on the training data using maximum likelihood estimation. The ExpectationMaximization (Dempster et al. 1977) algorithm is used to fit the Gaussian mixtures. We now explain for both scenarios how the GT labels were obtained.

### 5.4.1 Pedestrian Scenario

Sequences where potentially critical situations occur, i.e. when either pedestrian or vehicle should stop to avoid a collision, have been labeled as critical. Sequences are further labeled with event tags and time-to-event (TTE, in frames) values. For stopping pedestrians, $\mathrm{TTE}=0$ is when the last foot is placed on the ground at the curbside, and for crossing pedestrians at the closest point to the curbside (before entering the roadway). Frames before/after an event have negative/positive TTE values. For stopping sequences, the GT switching state is defined as $M_{t}=m_{s}$ at moments with $\mathrm{TTE} \geq 0$, and as $M_{t}=m_{w}$ at all other moments, crossing sequences always have $M_{t}=m_{w}$.

Considering head observation $H O$, we assume pedestrians recognize an approaching vehicle (GT label $Z_{t}^{\mathrm{ACT}}=$ true) when the GT head direction is in a range of $\pm 45^{\circ}$ around angle $0^{\circ}$ (head is pointing towards the camera), and do not see the vehicle $\left(Z_{t}^{\mathrm{ACT}}=\right.$ false) for angles outside this range (future human studies could allow a more precise threshold, or provide an angle distribution, the study in Hamaoka et al. (2013) only reported the frequency of head turning). For each ground truth label $s v$, we estimate the orientation class distributions $p_{s v}$ by averaging the class weights in the corresponding head measurements.

For the observation $D^{\min }$, we define per trajectory one value for all $Z_{t}^{\mathrm{DYN}}$ labels ( $\forall_{t} Z_{t}^{\mathrm{DYN}}=$ true for trajectories with critical situations, $\forall_{t} Z_{t}^{\mathrm{DYN}}=$ false otherwise), and fit the distributions $\Gamma\left(D^{\min } \mid \mu_{s c}, b_{s c}\right)$.

The distributions $\mathcal{N}\left(D T C_{t} \mid \mu_{a c}, \sigma_{a c}\right)$ are estimated from GT curb positions and the spacial $Z_{t}^{\text {STAT }}$ labels, where $Z_{t}^{\text {STAT }}=$ true only at time instances where $-1 \leq \mathrm{TTE} \leq 1$ when crossing, and $\mathrm{TTE} \geq-1$ when stopping.

The histogram of the GT distributions and the estimated fits can be seen in Fig. 7.

### 5.4.2 Cyclist Scenario

The turning cyclists have $\mathrm{TTE}=0$ defined at the frame where it is first visible that they are turning. For the cyclists going straight, $\mathrm{TTE}=0$ is defined as the first frame where they pass the point at which $25 \%$ of all turning cyclists have passed their $\mathrm{TTE}=0$. For all turning cases, the GT switching state is defined as $M_{t}=m_{t u}$ at moments with $\mathrm{TTE} \geq 0$. All other moments, and all straight cases have their GT state defined as $M_{t}=m_{s t}$ These average turning velocity of a track is estimated on its frames where $M_{t}=m_{t u}$. The prior for the speed of the turning cyclist is estimated on these average turning velocities.

The GT for $Z_{t}^{\mathrm{ACT}}$ is taken from annotated GT arm angles. When the arm is raised further than $30^{\circ}, Z_{t}^{\mathrm{ACT}}=$ true. Below $30^{\circ}$, the arm is considered down, or $Z_{t}^{\mathrm{ACT}}=$ false.

We define one value for all $Z_{t}^{\mathrm{DYN}}$ labels of a specific track. It is set as true if the ego-vehicle would overtake the cyclist in two seconds at TTE $=0$, assuming the cyclist has no more longitudinal speed. This can be interpreted as the worst-case scenario, where a cyclist would make an instant 90-degree turn.

Finally, the spatial extent of the turning region is determined from smallest and largest longitudinal position of all turning cyclists at $\mathrm{TTE}=0$. The GT label for $Z^{\mathrm{STAT}}$ is set to true whenever the cyclist is in this region.

### 5.4.3 Both Scenarios

In both scenarios, we compute maximum likelihood estimates of the parameters for the priors and noise distributions using the GT position and speed profiles. For each pedestrian track, we take the average speed during the walking motion type as GT preferred walking speed $\bar{x}^{m_{w}}$. Similarly, for each cyclist track we take averages of their GT speeds during each motion type as GT of the preferred speeds $\bar{x}_{t}^{m_{t u}}, \bar{y}_{t}^{m_{t u}}, \bar{x}_{t}^{m_{s t}}$ and $\bar{y}_{t}^{m_{s t}}$.

With all continuous states $X_{t}$ fully defined for all tracks, we can compute the $\epsilon_{t}$ using Eq. (1), i.e. $B \epsilon_{t}=X_{t}-$ $A^{\left(M_{t}\right)} X_{t-1}$. From these $\epsilon_{t}$ the process noise covariance $Q$ is estimated. Likewise, observation noise covariance $R$ is estimated from the differences between GT and measured positions, since $\eta_{t}=Y_{t}-C X_{t}$ from Equation(2). Finally, the mean and covariance parameters of the state priors can be estimated from the $X_{0}$ of all training tracks.

The prior and transition probability tables for the discrete context states $Z^{\mathrm{ACT}}, Z^{\mathrm{STAT}}$ are obtained by counting and normalizing the occurrences in the GT labels. The same applies to the dynamic switching state $M$, conditioned on $Z^{\text {ACTED }}$, $Z^{\mathrm{DYN}}$ and $Z^{\mathrm{STAT}}$. The transition probability for $Z^{\text {ACTED }}$ is a logical OR, as described in Sect. 3.3. Since we only got one $Z^{\mathrm{DYN}}$ label per track, we fix the $Z^{\mathrm{DYN}}$ transition probability to $1 / 100$ for changing state.

## 6 Experiments

In the experiments, we compare the proposed DBNs using all context cues to variants using less cues, and to baseline approaches. We also compare the use of visual detections to using GT annotations as measurements, and we investigate computational performance.

In all experiments, leave-one-out cross-validation is used to separate training and test sequences. Sequences from anomalous sub-scenarios are always excluded from the training data. For each time $t$ with state $X_{t}$, we create a predictive distribution $\widetilde{P}_{t_{p} \mid t}\left(X_{t+t_{p}}\right)$ for prediction horizon $t_{p}$. Two performance metrics are used to evaluate a sequence, namely the Euclidean distance between predicted expected position
$Y_{t+t_{p}}$ and GT position $G_{t+t_{p}}$, and the log likelihood of $G$ under the predictive distribution:

$$
\begin{aligned}
\operatorname{error}\left(t_{p} \mid t\right) & =\left|\mathbb{E}\left[\widetilde{P}_{t_{p} \mid t}\left(Y_{t+t_{p}}\right)\right]-G_{t+t_{p}}\right| \\
\operatorname{predll}\left(t_{p} \mid t\right) & =\log \left[\widetilde{P}_{t_{p} \mid t}\left(G_{t+t_{p}}\right)\right]
\end{aligned}
$$

### 6.1 Pedestrian Scenario

We first investigate the influence of context on the pedestrian scenario. The proposed DBN with full context is compared to model variants that only uses the head orientation, to one that only uses the minimal distance to the pedestrian, and to one that combines these two contexts. We refer to these variants after the used measurements: $E^{\mathrm{ACT}}, E^{\mathrm{DYN}}$ and $E^{\mathrm{DYN}}+E^{\mathrm{ACT}}$ respectively. We also include a common 2nd-order LDS as additional baseline. The dynamic process of this LDS for the lateral pedestrian position can be described as
$\left[\begin{array}{l}x_{t} \\ \dot{x}_{t}\end{array}\right]=\left[\begin{array}{ll}1 & 1 \\ 0 & 1\end{array}\right],\left[\begin{array}{l}x_{t-1} \\ \dot{x}_{t-1}\end{array}\right]+\epsilon_{t} \quad \epsilon_{t} \sim \mathcal{N}\left(\left[\begin{array}{l}0 \\ 0\end{array}\right], Q\right)$.
where the process noise covariance is also estimated from the GT position and speed.

### 6.1.1 Comparison of Model Variations

The results in Table 3 show the predictive log likelihood predll for $t_{p}=16$ time steps ( $\sim 1 \mathrm{~s}$ ) in the future, averaged over the second up to TTE $=0$ when the pedestrian reaches the curb. In the first three normal sub-scenarios, all five SLDSbased models perform similarly, clearly outperforming the LDS (which has similar low likelihoods across the board, i.e. it is unspecific for any sub-scenario). However, in the fourth sub-scenario (pedestrian sees the vehicle in a critical situation and stops), the simpler DBNs have low predictive likelihoods, except for our proposed model. Without the full context, the other models are not capable to predict if, where and when the pedestrian will stop.

For the anomalous sub-scenario, only the proposed model results in lower likelihood than for normal behavior, which is a useful property for anomaly detection as mentioned in Sect. 3.1. A future driver warning strategy could benefit from the more accurate path prediction of our full model in high likelihood situations, whereas falling back to simpler models/strategies when anomalies are detected.

### 6.1.2 Detailed Analysis on a Single Track

Fig. 10 illustrates a sequence from the stopping sub-scenario (fourth row in Table 3), with a snapshot just before (TTE $=$ $-20)$ and after $(\mathrm{TTE}=-9)$ the pedestrian becomes aware of the critical situation. At TTE $=-20$, the predicted distributions of all models are close together and indicate that

Table 3 Prediction log likelihood of the GT pedestrian position for t_{p} = 16 frames (~ 1 s) ahead, for different sub-scenarios (rows) and models (columns), for TTE ∈ [-15, 0]


The first four sub-scenarios contain "normal" pedestrian behavior. The fifth case is anomalous (lower likelihood is better). Model variations (best SLDS variant marked in bold): full context, no curb (E^{DYN}+E^{ACT}), only head (E^{ACT}), only criticality (E^{DYN}), no context (SLDS), KF (LDS)

The pedestrian continues walking (the LDS does so with high uncertainty). At TTE = -9, the mean position predictions of the LDS are furthest away from the GT (still within one std. dev. because of high uncertainty). The SLDS-only prediction shows a comparatively low uncertainty, but the predicted means have a high distance to the GT (not within one std. dev.). Predictions of the E^{DYN}+E^{ACT} model are closer to the true positions, since it captures the situational awareness of the pedestrian and therefore assigns a higher probability, compared to SLDS, to switch to the standing model m_{s}. The

![img-12.jpeg](img-12.jpeg)

Fig. 10 Best viewed in color. Example of a pedestrian stopping at the curb after becoming aware of a critical situation, see also the marginal distributions in e. Predictions are made t_{p} = 16 (~ 1 s) time steps ahead from different times t. a Pedestrian with head detection bounding box (white), tracking bounding box (green), collapsed predicted distribution of the full model (blue ellipses show one and two std. dev.) and curb detection (blue line). b The pedestrian became aware of the critical situation. c Predictions [mean and std. dev. (shaded)] made at t = 12 (green diamond) for the lateral position at time t + t_{p} (red diamond indicates the GT at t + t_{p}). Vertical black line denotes the event. Black dots indicate position measurements, the black line the GT positions. Colored lines are predicted positions by different models. d Predictions of the lateral position at t + t_{p} made from t = 23. e Marginal distributions of the full model latent variables over time [probabilities range from 0 (black) to 1 (white)]. The dotted green lines are set on the time of the two snapshots, t = 12 and t = 23. Variable labels are True and False, and walking and standing

![img-13.jpeg](img-13.jpeg)

Fig. 11 Best viewed in color. Pedestrian scenario: stopping probability (left) and lateral prediction error (right) when predicting 16 time steps ( $\sim 1 \mathrm{~s}$ ) ahead in the two critical sub-scenarios. a, b Pedestrian is not aware of the critical situation and crosses. c, d Pedestrian is aware of the critical situation and stops. Shown are mean and standard devia-
tion (shaded) of each measure over all corresponding sequences, for our proposed full model, an intermediate model without spatial layout information $\left(E^{\mathrm{DVN}}+E^{\mathrm{ACT}}\right)$, the baseline SLDS model without context cues, and a LDS
![img-14.jpeg](img-14.jpeg)

Fig. 12 Best viewed in color. Pedestrian scenario: the plots show the lateral prediction error of our proposed model and the PHTM model in various sub-scenarios. The lines show the avg. error over all sequences in a sub-scenario, after aligning the results by their TTE values, and
the shaded region shows the std. dev. of the error. a Non-critical, vehicle seen, crossing. b Critical, vehicle not seen, crossing. c Non-critical, vehicle not seen, crossing. d Critical, vehicle seen, stopping

full model makes the best predictions as it also anticipates where the pedestrian will stop, namely at the curbside.

For instance, at $t=23, Z_{t}^{\text {ACTED }}$ starts to change as it becomes more probable that the pedestrian has seen the vehicle, and indeed around $t=29$ the pedestrian stops at the curb.

### 6.1.3 Comparison Over Time

In the context of action classification, Fig. 11 shows for various model variations, the standing probability $\hat{P}_{t}\left(M_{t}=m_{s}\right)$, and the error $\left(t_{p} \mid t\right)$ for predictions made $t_{p}=16$ frames ahead, plotted against the TTE. In the first sub-scenario (top row), the pedestrian crosses in a critical situation without seeing the approaching vehicle. All models have a very low stopping probability (Fig. 11a), but since a few sequences have ambiguous head observations, our proposed model does not exclude the possibility that the vehicle has been seen. This translates to a higher stopping probability near the curb, and to a higher error of the average prediction (Fig. 11b) for a short while. Still, the model recuperates as the pedestrian approaches the curb and shows no sign of slowing down, which informs the model that the pedestrian did not see the vehicle (i.e. joint inference also means that observed motion dynamics can disambiguate low-level head orientation estimation). In the second sub-scenario (bottom row), the pedestrian is aware of the critical situation and stops at the curb. Now, all models show an increasing stopping probability (Fig. 11c) towards the event point. In a few scenarios, the SLDS switches too early to the standing state, reacting to perceived de-acceleration (noise) of the pedestrian walking, hence the high std. dev. of the SLDS over all sequences early on. However, on average the SLDS assigns a higher probability to standing $(>0.5)$ than walking after the pedestrian has already reached the curb (TTE $>0$ ). It can only react to changing dynamics, but not anticipate it. Our proposed model, on the other hand, gives the best action classification (highest stopping probability at $\mathrm{TTE}=0$ ). It anticipates the change in motion dynamics a few frames earlier as the SLDS, benefiting from the combined knowledge about pedestrian awareness, interaction, and spatial layout. Further, the knowledge about the spatial layout helps to keep the standing probability low while the pedestrian is still far away from the curb. The model with limited context information ends up in between proposed model and SLDS. Accordingly, our proposed model has the lowest prediction error (Fig. 11d). Averaged over the sequences, it outperforms the baseline SLDS model by up to 0.39 m (at $\mathrm{TTE}=1$ ) and the $E^{\mathrm{DYN}}+E^{\mathrm{ACT}}$ model by up to 0.16 m (at $\mathrm{TTE}=-10$ ).

### 6.1.4 Idealized Vision Measurements

To investigate how the vision components affect performance, we train and test using GT as idealized measurements

Table 4 Pedestrian scenario. Computational costs for the different models per frame (avg. per frame, in $m s$ )


for pedestrian location, curb location, and head orientation. We find that the lateral pedestrian and curb measurements are sufficiently accurate: the use of GT as measurements does not notably improve the results. Ideal head measurements alter the five sub-scenario scores of the full model w.r.t. Table 3 to $-0.57,-1.08,-0.32,-0.12$ ("normal" cases), and to -3.67 (anomalous case). Predictions became more accurate for critical sub-scenarios. However the second sub-scenario (Non-critical, Vehicle seen, Crossing) became less accurate, as some moments were deemed critical, and seeing the vehicle implied stopping, Still, the likelihood of the anomalous fifth sub-scenario is much lower than all other sub-scenarios.

### 6.1.5 Comparison with PHTM and Computational Cost

Fig. 12 shows a comparison of the mean prediction error of our proposed model with the state-of-the-art PHTM model (Keller and Gavrila 2014) which uses optical flow features and an exemplar database, on the four "normal" sub-scenarios. On two of these sub-scenarios (Fig. 12a, b) the proposed model outperforms PHTM slightly, both in terms of mean and variance, in particular on the arguably most important sub-scenario for a pedestrian safety application: Critical, Vehicle not seen, Crossing. On the other two sub-scenarios (Fig. 12c, d) PHTM performs slightly better.

The computational costs of the various approaches were assessed on standard PC hardware (Intel Core i7 X990 CPU at 3.47 GHz ), see Table 4. We differentiate between the computational cost for obtaining the observables and that for performing state estimation and prediction. In terms of observables, all approaches used positional information derived from a dense stereo-based pedestrian detector (about 60 ms ). The additional observables used in our proposed full model (e.g. head orientation and curb detection) cost an extra 100 ms to compute. PHTM on the other hand requires computing dense optical flow within the pedestrian bounding box (about 10 ms ). But, as seen in Table 4, the proposed model is one order of magnitude more efficient than PHTM when considering only the state estimation and prediction component [this even though PHTM implements its trajectory matching by an efficient hierarchical technique (Keller and Gavrila 2014)], and it is three times more efficient in total.

### 6.2 Cyclist Scenario

To demonstrate that our approach is not specific for the crossing pedestrian scenario, we compare the full model to SLDS and LDS baselines on the cyclist scenario. Like the pedestrian scenario, we use an LDS baseline with the dynamic model from Eq. (35), except that the state is extended to $\left[x_{t}, \dot{x}_{t}, y_{t}, \dot{y}_{t}\right]$.

### 6.2.1 Comparison with Baselines

Unlike stopping pedestrians, turning cyclists remain in the vehicle's view and driving corridor for a longer time. Also, the path during a turn slowly diverges from the straight path. Therefore, we extend the duration over which we summarize predictions with 15 time steps (frames). Another difference between the cyclist and pedestrian scenario is that cyclist's predictive distributions are 2D multivariate Gaussians for lateral and longitudinal position, instead of 1D Gaussians on the lateral position only. Hence, the reported likelihood values cannot be compared directly between scenarios, as the underlying domains have different dimensions.

The log likelihoods of the one-second-ahead prediction (16 time steps) are shown in Table 5, averaged over TTE $\in$ $[-15,15]$, i.e. starting with prediction for the moment when the cyclist either starts to turn, or keeps moving straight.

Since the cyclist tracks are long, and mostly consist of moving straight, the LDS predictions reflect the common behavior of straight motion with little variance. As a result, its predictions are accurate when the cyclist indeed does not turn. As expected, this comes at the cost of inaccurate predictions in normal and anomalous sub-scenarios where the cyclist does turn.

Compared to the LDS, the switching models demonstrate the benefit of having separate dynamics for straight and turning motion, as the predictions for turning sub-scenarios are considerably more accurate. Furthermore, our model outperforms the SLDS in almost all but one normal sub-scenarios. On the non-critical sub-scenario where there is ambiguity on whether the cyclist will turn or go straight, the SLDS performs best. Still, the proposed method performs best overall on all normal sub-scenarios, demonstrating that context does improve prediction accuracy generally compared to the LDS and SLDS baselines.

We also note that all models obtain lower predictive likelihood for turning than for moving straight. We find that this is a result from the large variance in how cyclists execute the turn. The data shows the cyclists vary in when they initiate the turn, and in used turning speed and angle. This variance is also reflected in the predictive distributions, which show larger uncertainty for turning than for moving straight.

During the evaluation period of Table 5 around $T T E=0$, the cyclist is always near to the intersection. We note that our model outperforms the baselines in all sub-scenarios when including all earlier predictions $(T T E<-15)$. When the cyclists are still far from the intersection, our full model benefits from the static environment context which predicts that turning is not feasible yet.

The final row of the table illustrates the predictive likelihood for the anomalous sub-scenario where the cyclist turns in a critical situation without raising an arm. Here, our model performs more similar to the LDS, as both expect the cyclist to continue moving straight. The next session will show a more detailed analysis of all sub-scenarios.

### 6.2.2 Comparison Over Time

Figure 13 compares the prediction error over time around $T T E=0$ for all normal sub-scenarios. For the critical sub-scenario where the cyclist maintains its straight path, Fig. 13a, all models demonstrate low prediction errors. The LDS shows lowest Euclidean error, but it has larger prediction uncertainty as Table 5 showed. In the critical and non-critical sub-scenarios where the cyclist raises an arm, our model anticipates the turn, and predicts some lateral motion to the left as soon as the cyclist is near the intersection. As a result, the model has slightly larger prediction error than the baselines before the turn is initiated, but yields lower errors as soon as turnings starts, see Fig. 13b, c. It keeps an advantage over SLDS for almost a full second after the turn started, until approximately $T T E=13$. On the critical subscenario, the largest difference in average error of 0.41 m occurs at $T T E=5$. On the non-critical sub-scenario without the cyclist raising an arm, Fig. 13d, the context cannot uniquely distinguish if the cyclist will turn or continue moving straight. Indeed, here the SLDS and our model also show similar performance.

Figure 14 shows the prediction log likelihood for two subscenarios where the cyclist turns in critical situations, namely the normal sub-scenario where the turn happens after raising an arm (Fig. 14a), and the anomalous sub-scenario where the turn happens without raising an arm (Fig. 14b). In both cases, the LDS likelihood drops fast, as it predicts continuation of the past motion instead of turning. Our full model also expects moving straight in case the arm was not raised, therefore its predictive likelihood declines too for the anomaly. Interestingly, the model does adapt after $T T E=0$ when the turning behavior becomes apparent. Later, at $T T E=10$, the predictive log likelihood of all models drops due to the variation in turning behavior.

Finally, we note that the LDS shows larger errors for the non-critical sub-scenarios. We observe that in these cases, where the vehicle is generally further away, the longitudinal estimates from stereo-vision are more unstable. The LDS is more sensitive to such noise as it adapts to all observed speed changes.

Table 5 Cyclist scenario


Log likelihood at 16 time steps ( $\sim 1 \mathrm{~s}$ ) into the future for TTE $\in[-15,15]$. Below sub-scenarios indicate the expected behavior of a cyclist. Best model performance are given in bold
![img-15.jpeg](img-15.jpeg)

Fig. 13 Cyclist scenario. Prediction error on the normal sub-scenarios when predicting 16 time steps ( $\sim 1 \mathrm{~s}$ ) ahead. a Critical, arm not raised, straight. b Critical, arm raised, turn. c Non-critical, arm raised, turn. d Non-critical, arm not raised, straight/turn
![img-16.jpeg](img-16.jpeg)

Fig. 14 Best viewed in color. Cyclist scenario: Prediction likelihood when predicting 16 time steps ( $\sim 1 \mathrm{~s}$ ) ahead on critical sub-scenarios where the cyclist turns. a Normal sub-scenario where the arm was raised. b Anomalous sub-scenario where the cyclist did not raise an arm to express intent

![img-17.jpeg](img-17.jpeg)

Fig. 15 Best viewed in color. Example of a cyclist turning in after holding his arm up, in a non-critical situation. Predictions are made sixteen time steps ( $\sim 1 \mathrm{~s}$ ) into the future. a Cyclist with tracking bounding box (red), arm detection (red line), collapsed predicted distribution of the full model (green ellipsoid shows one standard deviation), and "at intersection" region (white dotted line). b the cyclist enters the intersection region, which results in a wider predictive distribution shifted

### 6.2.3 Detailed Analysis on a Single Track

Figure 15 shows two snapshots of the prediction over time for a cyclist who is turning at the intersection after holding his arm up while the situation is not critical. Before the cyclist arrives at the intersection, at $t=67$, the prediction of the full model is very specific. Even though it was already detected that the cyclist raised his arm, he is expected to keep moving straight as he is not yet close enough to the intersection to turn. This prediction is done with less uncertainty than the baseline LDS because the process noise on the LDS must also account for the parts where the cyclist is turning left. At $t=132$, when the cyclist is at the intersection, there is an increased probability that he could turn left. As a result, the expected future position also shifts left, and the uncertainty region of the prediction increases. The one standard deviation area of the prediction reflects the possibility that the cyclist may still move straight before turning.
to the left. c Predictions (mean, and shaded std. dev.) made at $t=67$ (green diamond) for the lateral position up to 16 time steps into the future. The red diamond indicates the corresponding future GT position. d Predictions made at $t=132$, the moment where the cyclist starts turning. e Marginal posterior distributions of the latent variables in our full model over time. Probabilities range from 0 (black) to 1 (white). Variable labels are True and False, and straight and turning

## 7 Discussion

Our DBN provides predictive distributions of the future position of the tracked objects, reflecting uncertainty on possible trajectories. But as our results show, different scenarios give rise to different sources of uncertainty. For instance, if the system anticipates a change in dynamics, the future stopping position near the curb can be determined quite accurately for the pedestrian scenario. However, in the cyclist scenario there is more variance in turning behavior than in moving straight ahead, making accurate path predictions for the anticipated switch in dynamics more challenging. The available context may also be insufficient to unambiguously predict the behavior, as was seen in a cyclist sub-scenario. Here, our model's performance approximated that of the SLDS baseline.

Another property of our model is that it is not a black box, but explicitly defines the relation between context observables, states, motion modes, and their dynamics. This ensures that a designer can inspect the system, investigate how it assesses the context, and determine causes for failure or success. The explicit formulation also facilitates adding addi-

tional cues, or improve individual parts (e.g. using different dynamical models) while keeping existing parts unchanged. The generic formulation also ensures that many forms of information can be included, from up-to-date map data, to past image classification results. Accordingly, our method and the PHTM approach do not stand directly in competition, as they use different sources of information that could conceivably be combined.

Anomalous sub-scenarios contain situations not represented by the training data. In anomalous sub-scenarios, our method predicts position with lower likelihood than for the normal sub-scenarios. Therefore, low-likelihood predictions can be used to detect anomalous behavior, for instance to switch to an emergency control strategy of the vehicle. Of course, anomalous situations are expected to be rare, since the training data is expected to be representative of 'normal' behavior. Larger realistic datasets should therefore provide better estimates of 'normal' behavior, though the principle demonstrated on our example scenarios should remain the same.

Future work involves the incorporation of additional scene context (e.g. traffic light, pedestrian crossing) and the extension of the basic motion types of the SLDS (e.g. turning in different directions). Indeed, initial work has already begun on extending our earlier conference (Kooij et al. 2014a) submission, which only considered the pedestrian crossing scenario. For instance, (Roth et al. 2016) incorporated driver attention in the same framework, and (Hashimoto et al. 2016) tackled additional pedestrian scenarios with similar DBNs.

## 8 Conclusions

This paper investigated the use of DBNs for path prediction of maneuvering objects. As a toy example illustrated, SLDSs can make good overall predictions, but prediction accuracy suffers when an actual change in dynamics occurs. We therefore proposed to condition the switching probability on dynamic context variables. Measurements of various visual cues inform the model if and when changes in dynamics are likely to occur. An efficient approximate inference method was presented for online path prediction. Parameters are estimated on annotated training data.

We validated our approach on two use cases of VRU path prediction in the IV domain, a pedestrian and a cyclist scenario. Combining several context cues proved to improve overall prediction accuracy, namely the VRU's interaction with the ego-vehicle as dynamic environment context, the VRU's location in the static environment, and the VRU behavior indicating awareness or intent. The experiments demonstrate that the expected benefits of the context also occur with real-world vehicle measurements, and when using features extracted from vision. Compared to the SLDS, when predicting up to $\sim 1 \mathrm{~s}$ ahead, our method improved up to 0.39 m for the pedestrian scenario, and up to 0.41 m for the cyclist scenario. It also slightly outperforms the PHTM approach at less than a third of computational cost.

We are encouraged that the presented context-based models can play an important role in saving lives for the future intelligent vehicles.

Acknowledgements The research leading to the results of this work has received funding from the European Communitys Eighth Framework Program (Horizon2020) under Grant Agreement No. 634149, the PROSPECT project.

Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecomm ons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.
