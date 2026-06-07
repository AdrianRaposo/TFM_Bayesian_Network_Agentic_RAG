# Tracking the Visual Focus of Attention for a Varying Number of Wandering People

Kevin Smith, Member, IEEE, Sileye Ba, Jean-Marc Odobez, Member, IEEE, and Daniel Gatica-Perez, Member, IEEE

**Abstract**— In this article, we define and address the problem of finding the visual focus of attention for a varying number of wandering people (VFOA-W)—determining where a person is looking when their movement is unconstrained. VFOA-W estimation is a new and important problem with implications in behavior understanding and cognitive science, as well as real-world applications. One such application, presented in this article, monitors the attention passers-by pay to an outdoor advertisement using a single video camera. In our approach to the VFOA-W problem, we propose a multi-person tracking solution based on a dynamic Bayesian network that simultaneously infers the number of people in a scene, their body locations, their head locations, and their head pose. For efficient inference in the resulting variable-dimensional state-space we propose a Reversible Jump Markov Chain Monte Carlo (RJMCMC) sampling scheme, as well as a novel global observation model which determines the number of people in the scene and their locations. To determine if a person is looking at the advertisement or not, we propose Gaussian Mixture Model (GMM) and Hidden Markov Model (HMM)-based VFOA-W models which use head pose and location information. Our models are evaluated for tracking performance and ability to recognize people looking at an outdoor advertisement, with results indicating good performance on sequences where up to three mobile observers pass in front of an advertisement.

**Index Terms**— Computer vision, tracking, video analysis, consumer products.

## I. INTRODUCTION

As motivation for this work, we consider the following hypothetical question: "An advertising firm has been asked to produce an outdoor display ad campaign for use in shopping malls and train stations. Internally, the firm has developed several competing designs, one of which must be chosen to present to the client. Is there some way to empirically judge the best placement and content of these advertisements?" Currently, the advertising industry relies on recall surveys or traffic studies to measure the effectiveness of outdoor advertisements. However, these hand-tabulated approaches are often impractical or too expensive to be commercially viable, and yield small samples of data. A tool that automatically measures the effectiveness of printed outdoor advertisements would be extremely valuable, but does not currently exist.

However, in the television industry, such a tool does exist. The Nielsen ratings measure media effectiveness by estimating the size of the net cumulative audience of a program via surveys and Nielsen Boxes. If one were to design a similar system for outdoor advertisements, it might automatically determine the number of people who have actually viewed an advertisement as a percentage of the total number of people exposed to it. This is an example of an important extension of the visual focus of attention (VFOA) problem, in which there exists a varying number of wandering people. We denote this as the VFOA-W problem, whose tasks are:

1. to automatically detect and track a varying number of mobile observers,
2. and to estimate their VFOA with respect to one or more fixed targets.

Solutions to the VFOA-W problem have implications for other fields (e.g. human behavior, HCI) as well as real-life applications. In our example of the outdoor advertisement application, the goal is to identify each person exposed to the advertisement and determine if and when they looked at it. We can also collect other useful statistics such as the amount of time they spent looking at the advertisement.

The VFOA-W problem represents an extension of traditional VFOA problems studied in computer vision (e.g. [38]) in two respects. First, for VFOA-W, the VFOA must be estimated for an unknown, varying number of subjects instead of a fixed number of static subjects. Second, in VFOA-W, mobility is unconstrained. By unconstrained motion, we mean that the subjects are free to walk about the scene (or wander): they are not forced to remain seated or otherwise restrained. This complicates the task, as the subject's appearance will change as he moves about the scene and keeps his attention focused on the target.

Camera placement and the unconstrained motion of the subjects can limit the video resolution of the subjects, making VFOA estimation from eye gaze difficult, as illustrated in Figure 1. To address this problem, we follow the work of Stiefelhagen et al., who showed that VFOA can be deduced from head pose when the resolution is insufficient to determine eye gaze [38].

In this article, we propose a principled probabilistic framework for estimating VFOA-W, and apply our method to the advertising example to demonstrate its usefulness in a real-life application. Our method consists of two components: a dynamic Bayesian network, which simultaneously tracks people in the scene and

Manuscript received August 11, 2006; revised March 05, 2007.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Determining VFOA from eye gaze. In the VFOA-W problem, allowing an unknown number of people to move about the scene (and enter/exit the scene) complicates the task of estimating each subject's visual focus of attention (VFOA). Because a large field of view is necessary, the resolution is often too low to estimate the VFOA using eye gaze (as seen above). In our work, VFOA is inferred from a person's location and head pose.

estimates their head pose, and two VFOA-W models based on Gaussian mixture models (GMM) and hidden Markov models (HMM) which infer a subject's VFOA from their location and head pose. We assume a fixed uncalibrated camera which can be placed arbitrarily, with the condition that subjects appear vertical with their face in view of the camera when they look at the target, as in Fig. 1.

Besides defining the VFOA-W problem itself, which to our knowledge is a previously unaddressed problem in the literature, we also make several contributions towards a solution. First, we propose a probabilistic framework for solving the VFOA-W problem by designing a mixed-state dynamic Bayesian network that jointly represents the people in the scene and their various parameters. The state-space is formulated in a true multi-person fashion, consisting of size and location parameters for the head and body, as well as head pose parameters for each person in the scene. This type of framework facilitates defining interactions between people.

Second, because the dimension of the state representing a single person is sizable, the multi-object state-space can grow to be quite large when several people appear together in the scene. The dimension of the state-space also changes as people enter or leave the scene. Efficiently inferring a solution in a large variable-dimensional space is a challenging problem. To address this issue, we designed a Reversible Jump Markov Chain Monte Carlo (RJMCMC) sampling method to do inference in this large variable dimensional space.

Third, in order to localize, identify, and determine the correct number of people present, we propose a novel global observation model. This model uses color and binary measurements taken from a background subtraction model and allows for the direct comparison of observations containing different numbers of objects.

Finally, we demonstrate the applicability of our model by applying it to the outdoor advertisement problem. We show that we are able to gather useful statistics such as the number of people who looked at the advertisement and the total number of people exposed to it on a set of video sequences in which people walk past a simulated advertisement. We provide an evaluation of our approach on this data using a comprehensive set of objective performance measures.

The remainder of the article is organized as follows. In Section II we discuss related works. In Section III we describe our joint multi-person head-pose tracking model. In Section IV we propose the GMM and HMM methods for modeling VFOA-W. In Section V we describe our parameter setting procedure. In Section VI we evaluate our models on captured video sequences of people passing by an outdoor advertisement. Some limitations of our approach are discussed in Section VII. Finally, Section VIII contains some concluding remarks.

## II. Related Work

To our knowledge, our work is the first attempt to estimate the VFOA-W. However, there is an abundance of literature concerning the three component tasks of the VFOA-W problem: multi-person tracking, head pose tracking, and VFOA estimation.

## A. Multi-Person Tracking

Multi-person tracking is the process of locating a variable number of moving people or objects in a video over time. Multi-
person tracking is a well studied topic with a variety of different approaches. We restrict our discussion to probabilistic tracking methods which use a particle filter (PF) formulation [20], [39], [15], [23]. Some computationally inexpensive methods use a single-object state-space model [23], but suffer from the inability to resolve the identities of different objects or model interactions between objects. As a result, much work has been focused on adopting a rigorous Bayesian joint state-space formulation to the problem, where object interactions can be explicitly defined [20], [39], [15], [17], [44], [32]. However, sampling from a joint statespace can quickly become inefficient as the dimension of the space increases when more people are added [20]. Recent work has concentrated on using MCMC sampling to track multiple people more efficiently [17], [44]. In a previous work [32], we proposed to generalize this model to handle a varying number of people using RJMCMC, which allows for a formal definition of object appearance (births) and disappearances (deaths) from the scene through the definition of a set of reversible move types (see Section III-D). In this work, we extend the model of [32] to handle a more complex object model and a larger statespace, necessitating the design of new move types and proposal distributions, a new observation model, and inter- and intra-person interactions.

## B. Head-Pose Tracking

Head-pose tracking is the process of locating a person's head and estimating its orientation in space. Existing methods can be categorized in two of the following ways: feature-based vs. appearance-based approaches and parallel vs. serial approaches. In feature-based approaches, a set of facial features such as the eyes, nose, and mouth are tracked. Making use of anthropometric measurements on these features, the relative positions of the tracked features can be used to estimate the head-pose [10], [13], [37]. A feature-based approach employing stereo vision was proposed in [42]. The major drawback of the feature-based approach is that it requires high resolution head images, which is impractical in many situations. Occlusions and other ambiguities present difficult challenges to this approach as well.

In the appearance-based approach, instead of concentrating on specific facial features the appearance of the entire head is modeled and learned from training data. Due to its robustness, there is an abundance of literature on appearance-based approaches. Several authors have proposed using neural networks [28], [19], principal component analysis [8], and multi-dimensional Gaussian distributions [41] as modeling tools.

In the serial approach to head-pose tracking, the tasks of head tracking and pose estimation are performed sequentially. This is also known as a "head tracking then pose estimation" framework, where head tracking is accomplished through some tracking algorithm, and features are extracted from the tracking results to perform pose estimation. This methodology has been used by several authors [37], [28], [19], [43], [41], [7]. In approaches relying on state-space models, the serial approach may have a lower computational cost over the parallel approach as a result of a smaller configuration space, but head-pose estimation depends on the tracking quality.

In the parallel approach, the tasks of head tracking and pose estimation are performed jointly. In this approach, knowledge of the head-pose can be used to improve localization accuracy, and vice-versa. Though the configuration space may be larger

in the parallel approach, the computational cost of the two approaches may ultimately be comparable as a result of the parallel approach's improved accuracy through joint tracking and pose estimation. Benefits of this method can be seen in [42] and [3]. In this work, we adopt an appearance-based parallel approach to head-pose tracking, where we jointly track the bodies, the heads, and estimate the poses of the heads of multiple people within a single framework.

### *C. Visual Focus of Attention*

Estimating VFOA is of interest to several domains as a person's VFOA is often strongly correlated with his behavior or activity. Strictly speaking, a person's VFOA is determined by his eye gaze. However, measuring the VFOA using eye gaze is often difficult or impossible as it can require either the movement of the subject to be constrained, or high-resolution images of the eyes, which may not be practical ([34], [22]).

In [38], Stiefelhagen et al. made the important observation that visual focus of attention can be reasonably derived by head-pose in many cases. We rely on this assumption to simultaneously estimate the VFOA for multiple people without restricting their motion. Others have followed this work, such as Danninger et al. [9] (where VFOA is estimated using head-pose in an office setting), Stiefelhagen [36] (where VFOA for multiple people and multiple targets is estimated through head pose), and Katzenmaier et al. [16] (where the head pose is used to determine the addressee in human-human-robot interaction). Note that in these related works the VFOA is modeled for a fixed number of seated people using an unsupervised learning process.

### *D. Other Related Work*

While we believe that this work is the first attempt to estimate VFOA-W, there exist several previous works in a similar vein. The 2002 Performance Evaluation of Tracking and Surveillance Workshop (PETS) defined a number of estimation tasks on videos depicting people passing in front of a shop window, including 1) determining the number of people in the scene, 2) determining the number of people in front of the window, and 3) determining the number of people looking at the window. Several methods attempted to accomplish these tasks through various means, including [21], [25]. However, among these works there were no attempts to use head-pose or eye gaze to detect when people were looking at the window; all estimations were done using only body location, assuming that a person pausing in front of the window is looking at it. A preliminary version of this article appeared in [30].

### III. JOINT MULTI-PERSON AND HEAD-POSE TRACKING

In a Bayesian approach to multi-person tracking, the goal is to estimate the posterior distribution for a target state Xt, taking into account a sequence of observations Zt:t = (Zt, ..., Zt), p(Xt|Zt:t). The state, or joint multi-person configuration, is the union of the set of individual states describing each person in the scene. The observations consist of information extracted from an image sequence. The posterior distribution is expressed recursively by

$$p(\mathbf{X}_t|\mathbf{Z}_{1:t}) = C^{-1} p(\mathbf{Z}_t|\mathbf{X}_t) \times \tag{1}$$

$$\int_{\mathbf{X}_{t-1}} p(\mathbf{X}_t|\mathbf{X}_{t-1})p(\mathbf{X}_{t-1}|\mathbf{Z}_{1:t-1})d\mathbf{X}_{t-1},$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. **State model for varying numbers of people and their head-pose.** The joint multi-person state, Xt, consists of an arbitrary number of single-person states Xt,t, each of which contains a body Xt,t and head Xt,t component. The body is modeled as a bounding box with parameters for the location (xh,yh), height scale xh, and eccentricity eh. The head location Lh has similar parameters for location (xh,yh), height xh, and eccentricity eh, as well as in-plane rotation yh. The head also has an associated *exemplar* 0h, which models the out-of-plane head rotation.

where the dynamic model, p(Xt|Xt-1), governs the temporal evolution of Xt given the previous state Xt-1, and the observation likelihood, p(Zt|Xt), expresses how well the observed features Zt fit the predicted estimation of the state Xt. Here C is a normalization constant.

In practice, the estimation of the filtering distribution in Eq. 1 is often intractable. However, it can be approximated by applying the Monte Carlo method, where the target distribution (Eq. 1) is represented by a set of N samples {Xt(n), n = 1, ..., N}, where Xt(n) denotes the n-th sample. In this work we use RJMCMC, where a set of uniformly-weighted samples form a so-called Markov chain. Given the sample set approximation of the posterior at time t-1, p(Xt-1|Z1:t-1) ≈ ∑n δ(Xt-1 - Xt(n)), the Monte Carlo approximation of Eq. 1 is written

$$p(\mathbf{X}_t|\mathbf{Z}_{1:t}) \approx C^{-1} p(\mathbf{Z}_t|\mathbf{X}_t) \sum_{n} p(\mathbf{X}_t|\mathbf{X}_{t-1}^n). \tag{2}$$

In the following sub-sections we describe the joint multi-person and head tracking model, the dynamic model, the observation model, and how RJMCMC sampling is used to do inference.

### *A. State-Space Definition for a Varying Number of People*

The state at time t describes the joint configuration of people in the scene. Because the amount of people in the scene may vary, we define a state model designed to accommodate changes in dimension [32]. The joint state vector Xt is defined by Xt = {Xt,t|i ∈ I_t}, where Xt,t is the state vector for person i, and I_t is the set of all person indexes at time t. The total number of people present in the scene is mt = |I_t|, where | · | indicates set cardinality. A special case exists when there are no people present in the scene, denoted by Xt = ∅ (the empty set).

Each person is represented by two components: body Xt,t, and head Xt,t, Xt,t = (Xt,t,Xt,t) as seen in Figure 2. The body component is represented by a bounding box, whose state vector contains four parameters, Xh = (xh,yh,xh, eh) (we drop the i, t subindices to simplify notation). The point (xh,yh) is the continuous 2D location of the center of the bounding box, xh is the height scale factor of the bounding box relative to a reference height, and eh is the eccentricity defined by the ratio of the width of the bounding box to its height.

The head component is represented by a bounding box which may rotate in the image plane, along with an associated discrete

exemplar used to represent the head-pose (see Fig. 4). The state vector for the head is defined by $\mathbf{X}^{h}=\left(L^{h}, \theta^{h}\right)$ where $L^{h}=$ $\left(x^{h}, y^{h}, s^{h}, e^{h}, \gamma^{h}\right)$ denotes the continuous 2D configuration of the head, including the continuous 2D location $\left(x^{h}, y^{h}\right)$, the height scale factor $s^{h}$, the eccentricity $e^{h}$, and the in-plane rotation $\gamma^{h}$. The discrete variable, $\theta^{h}$ represents the head-pose exemplar which models the out-of-plane head rotation. Note that the head pose is completely defined by the couple $\left(\gamma^{h}, \theta^{h}\right)$.

## B. Dynamic and Interaction Model

The dynamic model governs the evolution of the state between time steps. It is responsible for predicting the motion of people (and their heads) as well as governing transitions between the head-pose exemplars. It is also responsible for modeling interperson interactions between the various people, as well as intraperson interactions between the body and the head. We define the dynamic model for a variable number of objects as

$$
p\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}\right) \propto p_{V}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}\right) p_{0}\left(\mathbf{X}_{t}\right)
$$

where $p_{V}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}\right)$ is the multi-object transition model and $p_{0}\left(\mathbf{X}_{t}\right)$ is an interaction term. The multi-person transition model is defined more specifically as

$$
p_{V}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}\right)= \begin{cases}\prod_{i \in \mathcal{I}_{t}} p\left(\mathbf{X}_{i, t} \mid \mathbf{X}_{t-1}\right) & \text { if } \mathcal{I}_{t} \neq \emptyset \\ k & \text { if } \mathcal{I}_{t}=\emptyset\end{cases}
$$

where $k$ is a constant. The single-person transition model is given by

$$
\begin{gathered}
p\left(\mathbf{X}_{i, t} \mid \mathbf{X}_{t-1}\right)= \\
\left\{\begin{array}{lll}
p\left(\mathbf{X}_{i, t} \mid \mathbf{X}_{i, t-1}\right) \text { if } & i \text { previously existed, } i \in \mathcal{I}_{1: t-1} \\
p\left(\mathbf{X}_{i, t}\right) & \text { if } & i \text { is a previously unused index, } i \notin \mathcal{I}_{1: t-1}
\end{array}\right.
\end{gathered}
$$

where $p\left(\mathbf{X}_{i, t}\right)$ is a mixture which selects parameters from either a previously dead tracked object or a new proposal (see Section III-E, birth move). The first term, $p\left(\mathbf{X}_{i, t} \mid \mathbf{X}_{i, t-1}\right)$ is given by

$$
p\left(\mathbf{X}_{i, t} \mid \mathbf{X}_{i, t-1}\right)=p\left(\mathbf{X}_{i, t}^{b} \mid \mathbf{X}_{i, t-1}^{b}\right) p\left(L_{i, t}^{b} \mid L_{i, t-1}^{b}\right) p\left(\theta_{i, t}^{b} \mid \theta_{i, t-1}^{b}\right)
$$

where the dynamics of the body state $\mathbf{X}_{i}^{b}$ and the head spatial state component $L_{i}^{b}$ are modeled as $2^{\text {nd }}$-order auto-regressive (AR) processes. This model applies for dead objects as well as live objects, as it is necessary for the positions of dead objects to be propagated for a certain duration in order to allow them to possibly be reborn. The head-pose exemplars, $\theta_{i}^{h}$, are modeled by a discrete $1^{\text {st }}$-order AR process represented by a transition probability table.

The interaction model $p_{0}\left(\mathbf{X}_{t}\right)$ handles two types of interactions, inter-person $p_{0_{1}}$ and intra-person $p_{0_{2}}: p_{0}\left(\mathbf{X}_{t}\right)=p_{0_{1}}\left(\mathbf{X}_{t}\right) p_{0_{2}}\left(\mathbf{X}_{t}\right)$. For modeling inter-person interactions we follow the method proposed in [17], in which the inter-person interaction model $p_{0_{1}}\left(\mathbf{X}_{t}\right)$ serves the purpose of restraining multiple trackers from fitting the same person by penalizing overlap. It accomplishes this by exploiting a pairwise Markov Random Field (MRF) whose graph nodes are defined by the people present at each time step. The links in the graph are defined by the set $\mathcal{C}$ of pairs of proximate people. By defining an appropriate potential function $\phi\left(\mathbf{X}_{i, t}, \mathbf{X}_{j, t}\right) \propto \exp \left(-\varrho\left(\mathbf{X}_{i, t}, \mathbf{X}_{j, t}\right)\right)$, the interaction model $p_{0_{1}}\left(\mathbf{X}_{t}\right)=\prod_{i j \in \mathcal{C}} \phi\left(\mathbf{X}_{i, t}, \mathbf{X}_{j, t}\right)$ enforces a constraint in the multi-person dynamic model, based on the locations of a person's neighbors. This constraint is defined by a non-negative penalty function, $g=\frac{\left\langle\rho\left(X_{i}, X_{j}\right) \nu\left(X_{i}, X_{j}\right)\right.}{\varrho\left(X_{i}, X_{j}\right) \nu\left(\left(X_{i}, X_{j}\right)\right.}$, which penalizes configurations which contain overlapping pairs of people, where $S^{X_{i}}$ is the
spatial support of $X_{i, t}, \rho\left(X_{i}, X_{j}\right)=\frac{S^{X_{i} \nu} S^{X_{j}}}{S^{X_{i}}}$ is the recall, and $\nu\left(X_{i}, X_{j}\right)=\frac{S^{X_{i} \nu} S^{X_{j}}}{S^{X_{i}}}$ is the precision, so that $g=0$ for no overlap, and increased overlap increases the penalization term $g$.

We also introduce intra-person interactions to the overall motion model. The intra-person interaction model is meant to constrain the head model w.r.t. the body model, so that they are configured in a physically plausible way (e.g. the head is not detached from the body). The intra-person interaction model $p_{0_{2}}\left(\mathbf{X}_{t}\right)$ is defined as $p_{0_{2}}\left(\mathbf{X}_{t}\right)=\prod_{k \in \mathcal{I}_{t}} p\left(L_{k, t}^{b} \mid \mathbf{X}_{k, t}^{b}\right)$, where $p\left(L_{k, t}^{b} \mid \mathbf{X}_{k, t}^{b}\right) \propto \exp \left(-\lambda d^{2}\left(L_{k, t}^{b}, \mathbf{X}_{k, t}^{b}\right)\right)$, and the distance function $d(\cdot)$ is equal to zero when the head center is within a predefined region relative to the body (i.e. the area defined by the top third of the body bounding box), and equal to the Euclidean distance between the head and nearest edge of the predefined region otherwise. This term penalizes head configurations which fall outside an acceptable range of the body, increasing as the distance between the head and body increases. With these terms defined, the Monte Carlo approximation of Eq. 2 can now be expressed as

$$
\begin{aligned}
p\left(\mathbf{X}_{t} \mid \mathbf{Z}_{1: t}\right) \approx & C^{-1} p\left(\mathbf{Z}_{t} \mid \mathbf{X}_{t}\right) p_{0}\left(\mathbf{X}_{t}\right) \sum_{n} p_{V}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}^{(n)}\right) \\
= & C^{-1} p\left(\mathbf{Z}_{t} \mid \mathbf{X}_{t}\right) \prod_{i j \in \mathcal{C}} \phi\left(\mathbf{X}_{i, t}, \mathbf{X}_{j, t}\right) \times \\
& \prod_{k \in \mathcal{I}_{t}} p\left(L_{k, t}^{b} \mid \mathbf{X}_{k, t}^{b}\right) \sum_{n} p_{V}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}^{(n)}\right)
\end{aligned}
$$

## C. Observation Model

The observation model estimates the likelihood of a proposed configuration, or how well the proposed configuration is supported by evidence from the observed features. Our observation model consists of a body model and a head model, formed from a set of five features. The body model consists of binary and color features, which are global in that they are defined pixel-wise over the entire image. The binary features $\left(\mathbf{Z}_{t}^{b i n}\right)$ make use of a foreground segmented image, while the color features $\left(\mathbf{Z}_{t}^{c o l}\right)$ exploit histograms in hue-saturation (HS) space. The head model is local in that its features $\left(\mathbf{Z}^{h}\right)$ are gathered independently for each person from an area around the head. They are responsible for the localization of the head and estimation of the head-pose, and include texture $\mathbf{Z}_{t}^{t e x}$, skin color $\mathbf{Z}_{t}^{s k}$, and silhouette $\mathbf{Z}_{t}^{s i l}$ features. For the remainder of this section, the time index $(t)$ has been omitted to simplify notation. Assuming conditional independence of body and head observations, the overall likelihood is given by

$$
p\left(\mathbf{Z}^{l} \mid \mathbf{X}\right) \stackrel{\text { def }}{=} p\left(\mathbf{Z}^{c o l}\right)\left(\mathbf{Z}^{b i n}, \mathbf{X}\right) p\left(\mathbf{Z}^{b i n} \mid \mathbf{X}\right) p\left(\mathbf{Z}^{h} \mid \mathbf{X}\right)
$$

The first two terms constitute the body model and the third term represents the head model.

1) Body Model: An issue arises when defining an observation likelihood for a variable number of objects. Fairly comparing the likelihoods, a task essential to the filtering process, is more complicated when the number of objects may vary. For a fixed number of objects, the comparison of two observation likelihoods can be relatively straightforward. Given an observation likelihood for a single object, the joint multi-object observation likelihood can be defined as the product of the individual object likelihoods [17], [18], [44]. For a static number of objects, the observation likelihoods are directly comparable because the number of objects, and thus the number of factors in the likelihood, is fixed. Fairly comparing two likelihoods defined in this manner when

![img-2.jpeg](img-2.jpeg)

Fig. 3. The binary observation model determines the number of objects and localizes the objects. In (a)-(c), two ground truth people appear in the scene segmented from the background (shown in green). The binary foreground model consists of K<sub>bf</sub> = 1 Gaussian, the black contour in (d). The background model consists of three GMMs of K<sub>bb</sub> = 4 mixture components each in (e) (m = 1: red contour, m = 2: blue contour, and m = 3: green contour). The square data points in (d) and (e) represent measured precision/recall observations from the hypotheses in (a)-(c). The red square indicates the (ν, ρ) values for the hypothesis containing only 1 object in (a), the blue square indicates the two-object hypothesis in (b), and the green square indicates the three-object hypothesis in (c). Clearly, the two-object hypothesis, which agrees with the ground truth, fits the model better than the others. The binary observation model will associate the highest likelihood to the hypothesis matching the actual number of objects (m = 2).

The number of objects may vary is problematic, as the number of factors in the likelihood terms we wish to compare may be different. This can eventually lead to observation likelihoods of different magnitude orders reflecting a variation in number of factors rather than an actual difference in the likelihood level.

To address this issue, we propose a global body observation model which allows for a direct comparison of observations containing different numbers of objects. Our model detects, tracks, and maintains consistent identities of people, adding and removing them from the scene when necessary. It is comprised of a binary feature and a color feature.

### Body Binary Feature

We introduced the binary feature in a previous work [32], which relies on an adaptive foreground segmentation technique described in [35]. At each time step, the image is segmented into sets of foreground pixels F and background pixels B from the images (I = F ∪ B), which form the foreground and background observations (Z<sup>bin,F</sup> and Z<sup>bin,B</sup>).

For a given multi-person configuration and foreground segmentation, the binary feature computes the distance between the observed overlap (between the spatial support of the multi-person configuration S<sup>X</sup> obtained by projecting X onto the image plane and the segmented image) and a learned value. Qualitatively, we are following the intuition of a statement such as: "We have observed that two well-placed trackers (tracking two people) should contain approximately 65% foreground and 35% background." The overlap is measured for F and B in terms of precision and recall: ν<sup>F</sup> = S<sup>X</sup> ∪ F, ρ<sup>F</sup> = S<sup>X</sup> ∪ F, ν<sup>B</sup> = S<sup>X</sup> ∪ B, and ρ<sup>B</sup> = S<sup>X</sup> ∪ B. An incorrect location or person count will result in ν and ρ values that do not match the learned values well, resulting in a lower likelihood and encouraging the model to choose better multi-person configurations.

The binary likelihood is computed for the foreground and background case p(Z<sup>bin</sup> | X) ≺ p(Z<sup>bin,F</sup> | X) p(Z<sup>bin,B</sup> | X) where the definition of the binary foreground term, p(Z<sup>bin,F</sup> | X), for all non-zero person counts (m ≠ 0) is a single Gaussian distribution in precision-recall space (ν<sup>F</sup>, ρ<sup>F</sup>). The binary background term, p(Z<sup>bin,B</sup> | X), on the other hand, is defined as a set of Gaussian mixture models (GMM) learned for each possible person count (m ∈ M). For example, if the multi-person state hypothesizes that two people are present in the scene, the binary background likelihood term is the GMM density of the observed ν<sup>B</sup> and ρ<sup>B</sup> values learned for m = 2. For details on the learning procedure, see Section V.

In Figure 3, an example of the binary observation model trained to recognize M = {1, 2, 3} objects is shown. Learning of the GMM parameters was done using the Expectation Maximization (EM) algorithm on 948 labeled images from the data set described in Section V-B. As shown in Figures 3(a)-(c), two ground truth people appear in the scene. The binary feature also encourages the tracker to propose hypotheses with good spatial fitting in a similar manner. For example, a poorly placed object might only cover a small fraction of the foreground blob corresponding to a person appearing in the image. In this case, the foreground ν and ρ measurements will not match the learned values well, as the learning has been done using tightly-fitting example data.

### Body Color Feature

The color feature is responsible for maintaining the identities of people over time, as well as assisting the binary feature in localization of the body. The color feature uses HS color observations from the segmented foreground and background regions (Z<sup>col,F</sup> and Z<sup>col,B</sup>). Assuming conditional independence

between foreground and background, the color likelihood is written $p\left(\mathbf{Z}^{col} \mid \mathbf{Z}^{b i n}, \mathbf{X}\right)=p\left(\mathbf{Z}^{c o l}, F \mid \mathbf{Z}^{b i n}, F, \mathbf{X}\right) p\left(\mathbf{Z}^{c o l}, B \mid \mathbf{Z}^{b i n}, B, \mathbf{X}\right)$.

The color foreground likelihood compares an adaptive 4-D spatial-color model histogram, $H C$, with a 4-D spatial-color observed histogram, $H\left(X_{t}\right)$. The observation likelihood measures the similarity of the 4-D histograms by $p\left(\mathbf{Z}^{c o l}, F \mid \mathbf{Z}^{b i n}, F, \mathbf{X}\right) \propto$ $\exp \left(-\lambda_{F} d_{F}^{2}\left(H C, H\left(X_{t}\right)\right)\right)$, where $d_{F}\left(H C, H\left(X_{t}\right)\right)$ is the Bhattacharya distance [6] between the histograms. The 4-D histograms $H(i, b p, h, s)$ are collected as follows. The first dimension corresponds to the object $i$, and the remaining dimensions correspond to an object color model proposed by Pérez et al. [26]. For the object color model, the histogram is defined over 3 body parts $b p$ corresponding to the head, torso, and legs. For each bodypart region, a 2-D HS+V histogram is computed using the Hue-Saturation-Value elements from the corresponding location in the training image. The HS+V histogram is constructed by populating an $B_{H} \times B_{S}$ HS histogram (where $B_{H}=8$ and $B_{S}=8$ are the number of H and S bins) using only the pixels with H and S greater than 0.15 . The +V portion of the HS+V histogram contains a $B_{V} \times 1\left(B_{V}=8\right)$ Value histogram comprised of the pixels with Hue or Saturation lower or equal to $0.15^{1}$.

The 4-D adaptive color model $H C$ is selected from a set of competing adaptive color models every frame. When an object first appears, pixel values extracted from the initial frame are used to initialize each competing color model. At the end of each subsequent frame, the point estimate solution for the objects' locations is used to extract a 4-D multi-person color histogram, which is compared to each model. The nearest matching competing model receives a vote, and is updated with the extracted data by a running mean. When computing the foreground color likelihood in the following frame, the model with the most votes is used.

The background color likelihood helps reject configurations containing untracked people by penalizing unexpected colors. The background model is a static 2D HS color histogram, learned from empty training images. The background color likelihood is defined as $p\left(\mathbf{Z}_{t}^{c o l}, B \mid \mathbf{Z}_{t}^{b i n}, B, \mathbf{X}_{t}\right) \propto e^{\lambda_{B} d_{B}^{2}}$, where $\lambda_{B}$ and $d_{B}^{2}$ are defined as in the foreground case but using the background images to compute the histogram.
2) Head Model: The head model is responsible for localizing the head and estimating the head-pose. The head likelihood is defined as

$$
p\left(\mathbf{Z}^{h} \mid \mathbf{X}\right)=\left[\prod_{i \in \mathcal{I}} p\left(\mathbf{Z}_{t}^{t e x} \mid \mathbf{X}_{i}\right) p\left(\mathbf{Z}_{t}^{s k} \mid \mathbf{X}_{i}\right) p\left(\mathbf{Z}_{t}^{e l} \mid \mathbf{X}_{i}\right) .\right]^{\frac{1}{m}}
$$

The overall head likelihood is composed of the geometric mean of the individual head likelihood terms. The geometric mean provides a pragmatic solution to the problem of comparing likelihoods with a variable number of factors (corresponding to varying numbers of people). However, note that it is not justifiable in a probabilistic sense.

The head model consists of three features: texture $\mathbf{Z}_{t}^{t e x}$, skin color $\mathbf{Z}_{t}^{s k}$, and silhouette $\mathbf{Z}_{t}^{e l}$. The silhouette feature, proposed in this work, helps localize the head using foreground segmentation. The texture and skin color features, which have appeared in previous works including our own [3], [41], use appearance-dependent observations to determine the head-pose of the subject.

[^0]![img-3.jpeg](img-3.jpeg)

Fig. 4. The head-pose model. (a) The head pose represented by the angles resulting from the Euler decomposition of the head rotation w.r.t. the head frame, known as pan, tilt, and roll. (b) Left: set of discrete poses $\theta^{h}$ used to represent out-of-plane rotation exemplars from the Prima-Pointing database. Right: pointing vector $z^{h}$ (note $z^{h}$ only depends on the pan and tilt angles when using the representation on the left).

## Head-Pose Texture Feature

The head-pose texture feature reports how well the texture of an extracted image patch matches the texture of the discrete headpose hypothesized by the tracker. Texture is represented using responses from three filters: a coarse scale Gaussian filter, a fine Gabor filter, and a coarse Gabor filter, as seen in Figure 5.

Texture models were learned for each discrete head-pose $\theta^{h}$. Training was done using several $64 \times 64$ images for each head-pose taken from the Prima Pointing Database. Histogram equalization was applied to the training images to reduce variation in lighting, the filters were applied on a subsampled grid to reduce computation, and the filter responses concatenated into a single feature vector. Then, for each head-pose $\theta$ ( $\theta=\theta^{h}$ here, for simplicity), the mean $e^{\theta}=\left(e_{j}^{\theta}\right)$ and diagonal covariance matrix $\sigma_{\theta}=\left(\sigma_{j}^{\theta}\right), j=1, \ldots, N_{t e x}$ of the corresponding training feature vectors were computed and used to define the person texture likelihood model from Eq. 10 as

$$
p\left(\mathbf{Z}_{t}^{t e x} \mid \mathbf{X}_{i}\right)=\frac{1}{Z_{\theta}} \exp -\lambda_{\theta}^{t e x} d_{\theta}\left(\mathbf{Z}_{t}^{t e x}, e^{\theta_{i}}\right)
$$

where $\theta_{i}$ is the head pose associated with person $i$ and $d_{\theta}$ is the normalized truncated Mahalanobis distance defined as:

$$
d_{\theta}(u, v)=\frac{1}{N_{t e x}} \sum_{j=1}^{N_{t e x}} \max \left(\left(\frac{u_{j}-v_{j}}{\sigma_{j}^{\theta}}\right)^{2}, T_{t e x}^{2}\right)
$$

where $T_{t e x}=3$ is a threshold set to make the distance more robust to outlier components. The normalization constant $Z_{\theta}$ and the parameter $\lambda_{\theta}^{t e x}$ are learned from the training data using a procedure proposed in [40].

## Head-Pose Skin Feature

The texture feature is a powerful tool for modeling the headpose, but prone to confusion due to background clutter. To help make our head model more robust, we have defined a skin color binary model (or mask), $M^{\theta}$, for each head-pose, $\theta$, in which the value at a given location indicates a skin pixel (1), or a nonskin pixel (0). An example of a skin color mask can be seen in Figure 5. The skin color binary models were learned from skin color masks extracted from the same training images used in the


[^0]:    ${ }^{1}$ This extra 1D V histogram is appended as one extra row in the HS histogram, resulting in a " 2 D " HS+V histogram.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Head-pose observation features. (a) Texture is used to estimate the head-pose by applying three filters to the original image (upper left). These filters include a coarse scale Gaussian filter (upper right), a fine scale Gabor filter (lower left), and a coarse scale Gabor filter (lower right). (b) Skin color models help to keep the head-pose robust in presence of background clutter. (c) A silhouette model is responsible for localizing the head.

Texture model using a Gaussian skin-color distribution modeled in normalized RG space [2].

The head-pose skin color likelihood compares the learned model with a measurement extracted from the image **Z<sup>th</sup><sub>i</sub>** (skin color pixels are extracted from the image using a temporally adaptive person-dependent skin color distribution model which is updated with a MAP adaptation to the current person using skin color pixels in the estimated head location). The skin color likelihood of a measurement **Z<sup>th</sup><sub>i</sub>** belonging to the head of person *i* is defined as

$$p(\mathbf{Z}_i^{sk} \mid \mathbf{X}_i) \propto \exp{-\lambda_{sk} ||\mathbf{Z}_i^{sk} - M^{\theta_i} ||_1},\tag{13}$$

where ||.||<sub>1</sub> denotes the *L*<sub>1</sub> norm and *λ*<sub>sk</sub> is a parameter tuned on training data.

### Head-Pose Silhouette Feature

In addition to the pose-dependent head model, we propose to use a head silhouette likelihood model to aid in localizing the head by taking advantage of foreground segmentation information. A head silhouette model is *H*<sup>sil</sup> (see Figure 5) is constructed by averaging head silhouette patches extracted from binary foreground segmentation images re-sized to 64 × 64 (see Section V-B, note that a single model is used unlike the pose-dependent models for texture and skin color).

The silhouette likelihood works by comparing the model *H*<sup>sil</sup> to an extracted binary image patch (from the foreground segmentation) corresponding to the hypothesized location of the head, **Z<sup>sil</sup><sub>i</sub>**. A poor match indicates foreground pixels in unexpected locations, probably due to poor placement of the head model. The head silhouette likelihood term is defined as:

$$p(\mathbf{Z}_i^{sil} \mid \mathbf{X}_i) \propto \exp{-\lambda_{sil} ||\mathbf{Z}_i^{sil} - H^{sil} ||_1},\tag{14}$$

where *λ*<sub>sil</sub> is an parameter tuned on training data.

In practice, we found that introducing this term (not defined in our previous work [3] or in others' like [41]) greatly improved the head localization in the combined body-head optimization process. Further details on the head-pose model can be found in [2].

### D. Component-wise Reversible-Jump MCMC

Having defined the components of Eq. 2 (state-space, dynamic model, and observation model) we now define an RJMCMC sampling scheme to efficiently generate a Markov Chain representing the posterior distribution in Eq. 9.

As the state vector for a single person is ten-dimensional, the multi-person state-space can quickly become very large when allowing for an arbitrary number of people. Traditional Sequential Importance Resampling (SIR) particle filters are known to be inefficient in such high-dimensional spaces [1]. The classic Metropolis-Hastings (MH) based MCMC particle filter is more efficient [17], but does not allow for the dimensionality of the state-space to vary (the number of people must remain static). To solve this problem, we have defined a type of RJMCMC sampling scheme [11] based on a method we proposed previously [32] which includes a set of reversible move types (or *jumps*) which can change the dimension of the state-space (note that a different RJMCMC model was originally used for tracking in [44]).

The RJMCMC algorithm starts in an arbitrary configuration **X<sup>0</sup>** sampled from the Markov chain belonging to the previous time step, *t* − 1. The first step is to select a *move type v* from the set of *reversible moves* **T** by sampling from a prior distribution on the move types *v* ∼ *p(v)*. The next step is to choose a target object *i<sup>*</sup>* (or two objects *i<sup>*</sup>* and *k<sup>*</sup>* in the case of a *swap* move), and apply the selected move type to form a proposal configuration **X**<sup>*</sup>. The proposal is evaluated in an *acceptance test*, and based on this test either the previous state **X<sup>(n−1)</sup>** or the proposed state **X**<sup>*</sup> is accepted and added to the Markov chain for time *t*.

A reversible move defines a transition from the current state **X** and a proposed state **X**<sup>*</sup> via a deterministic function *h<sub>v</sub>*, and, when necessary, a generated random auxiliary variable **U** [11]. This transition can involve changing the dimension between **X** and **X**<sup>*</sup>. The transition function *h<sub>v</sub>* is a *diffeomorphism*, or an invertible function that maps one space to another. There is flexibility in defining the transition *h<sub>v</sub>*, so long as it meets the following criteria: 1. it is a *bijection*, i.e. if *h<sub>v</sub>* defines a one-to-one correspondence between sets; 2. its derivative is invertible, i.e. it has a non-zero Jacobian determinant; 3. it has a corresponding *reverse move h<sub>v</sub><sup>0</sup>*, which can be applied to recover the original state of the system. The reverse move must also meet the first two criteria. For move types that do not involve a dimension change the reverse move is often the move type itself, in which case it is possible to recover the original multi-object configuration by reapplying the same move. Move types that involve a change in dimension usually cannot revert to the previous state, and are defined in *reversible move pairs*, where one move is the reverse of the other.

Following [1], the general expression for the acceptance ratio for a transition defined by *h<sub>v</sub>* from the current state **X<sup>t</sup>** to a proposed state **X**<sup>*</sup><sub>t</sub> (allowing for jumps in dimension) is given

$$\begin{array}{c}
\alpha(\mathbf{X}_t, \mathbf{X}^*_t) = \min\left\{ 1, \frac{p(\mathbf{X}^*_t | \mathbf{Z}_{1:t})}{p(\mathbf{X}_t | \mathbf{X}_{1:t})} \times \frac{p(v^R)}{p(v)} \times \right. \\
\frac{q^R_{t}(\mathbf{X}_t, \mathbf{U}|\mathbf{X}^*_{t}, \mathbf{U}^*)}{q_v(\mathbf{X}^*_{t}, \mathbf{U}^*)(\mathbf{X}_t, \mathbf{U})} \times \left| \frac{\partial h_v(\mathbf{X}_t, \mathbf{U})}{\partial(\mathbf{X}_t, \mathbf{U})} \right| \right\},
\end{array} \tag{15}$$

where **U** is an auxiliary dimension-matching variable and **U**<sup>*</sup> is its reverse move counterpart, *p*(**X**<sup>*</sup><sub>t</sub>|**Z**<sub>1:t</sub>) is the target distribution evaluated at the proposed configuration **X**<sup>*</sup><sub>t</sub>, *p*(**X**<sub>t</sub>|**Z**<sub>1:t</sub>) is the target distribution evaluated at the current configuration **X**<sup>*</sup><sub>t</sub>, *p(v)* is the probability of choosing move type *v*, *p(v<sup>R</sup>)* is the probability of choosing the reverse move type *v<sup>R</sup>*, *q<sub>v</sub>*(**X**<sup>*</sup><sub>t</sub>, **U**<sup>*</sup>|**X**<sup>t</sup>, **U**) is the proposal for a move from (**X**<sup>t</sup>, **U**) → (**X**<sup>*</sup><sub>t</sub>, **U**<sup>*</sup>), *q<sub>v</sub><sup>R</sup>*(**X**<sup>t</sup>, **U**|**X**<sup>*</sup><sub>t</sub>, **U**<sup>*</sup>) is the proposal distribution for the reverse move from (**X**<sup>*</sup><sub>t</sub>, **U**<sup>*</sup>) → (**X**<sup>t</sup>, **U**), and *q<sub>v</sub><sup>R</sup>*(**X**<sup>t</sup>, **U**) is the Jacobian determinant of the diffeomorphism from (**X**<sup>t</sup>, **U**) → (**X**<sup>*</sup><sub>t</sub>, **U**<sup>*</sup>). The Jacobian determinant is the matrix of all first-order partial derivatives of a vector-valued function, which reduces to one for our selected moves (see [29] for further details).

Instead of updating the whole of an object **X**<sup>i</sup> in a single move as in [44] and [32], we propose to split **X**<sup>i</sup> into components

of differing dimension $\left\{\mathbf{X}_{i}^{b}, L_{i}, \theta_{i}\right\}$ for some move types, and update these components one-by-one to increase the efficiency of the sampling process. Haario et al. [12] showed that such MCMC methods (which define proposal distributions that split the dimension of the state-space) are often more efficient and less sensitive to increasing dimension than those proposing moves over the full dimension for high-dimensional spaces [12]. In previous works using RJMCMC ([32] and [18]), a single update move was defined in which all the parameters of a person were updated simultaneously. This was sufficient for simple object models, but we found it to be inefficient for our complex model representing the body, head, and head pose.

## E. Reversible Move Type Definitions

In this work, we define a set of six reversible move types below, $\Upsilon=\{$ birth, death, swap, body update, head update, pose update $\}$. The traditional update move is split into three component moves for efficiency. The split was made such that the set of parameters modified for each of the update move types only affect a few terms in the observation likelihood: body update modifies the location and size of the body $\left(\mathbf{X}_{i}^{b}\right)$, head update modifies the location and size of the head $\left(L_{i}\right)$, and pose update updates the head pose $\left(\theta_{i}\right)$. (1) Birth. Birth adds a new object $\mathbf{X}^{*}{ }_{i^{*}}$ with index $i^{*}$ to the multiobject configuration $\mathbf{X}_{t}$, while keeping all other objects fixed, forming a proposed state $\mathbf{X}^{*}{ }_{t}$. This move implies a dimension change from $m \Gamma \rightarrow m \Gamma+\Gamma$, where $\Gamma$ denotes the dimension of a single object within the multi-object configuration. The birth move proposes the new multi-object configuration $\mathbf{X}^{*}{ }_{t}$, generated from the birth proposal distribution, $\mathbf{X}^{*}{ }_{t} \sim q_{b}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}, \mathbf{U}\right)$, by applying the transition function $h_{b}$ and sampling a dimensionmatching auxiliary variable $\mathbf{U}, \mathbf{U} \sim q(\mathbf{U})$. The birth move transition is given by $\mathbf{X}^{*}{ }_{t}=h_{b}\left(\mathbf{X}_{t}, \mathbf{U}\right)$ where the specific objects are defined as

$$
\mathbf{X}_{i, t}^{*}=\left\{\begin{array}{cc}
\mathbf{X}_{i, t}, & i \neq i^{*} \\
\mathbf{U}, & i=i^{*}
\end{array}\right.
$$

The auxiliary variable $\mathbf{U}$ is responsible for dimension matching in the transition $\left(\mathbf{X}_{t}, \mathbf{U}\right) \rightarrow\left(\mathbf{X}^{*}{ }_{t}\right)$ (i.e., $\mathbf{U}$ acts as a placeholder for the missing dimension in $\mathbf{X}_{t}$ ). The proposal for the birth move, $q_{b}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}, \mathbf{U}\right)$ is given by

$$
q_{b}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}, \mathbf{U}\right)=\sum_{i \in \mathcal{D}_{t} \cup\left\{i^{+}\right\}} q_{b}(i) q_{b}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}, \mathbf{U}, i\right)
$$

where $q_{b}(i)$ selects the object to be added, $i^{+}$is the next available unused object index and $\mathcal{D}_{t}$ is the set of currently dead objects. The target object index sampled from $q_{b}(i)$ is denoted as $i^{*}$, making the proposed set of objects indices a union of the current set $\mathcal{I}_{t}$ and the target object index $i^{*}, \mathcal{I}^{*}{ }_{t}=\mathcal{I}_{t} \cup\left\{i^{+}\right\}$. The objectspecific proposal distribution for a birth move is given by
where in the case of $i=i^{*}$, the proposal can be rewritten as

$$
\begin{aligned}
q_{b}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}, \mathbf{U}, i^{*}\right) & =\frac{1}{C\left(\mathbf{X}_{t}\right)}\left(\frac{1}{N} \sum_{n=1}^{N} \omega_{n} p\left(\mathbf{X}^{*}{ }_{i^{*}, t} \mid \mathbf{X}_{t-1}^{(n)}\right)\right) \times \\
& \prod_{j \in \mathcal{I}_{t}} p\left(\mathbf{X}_{j, t} \mid \mathbf{X}_{t-1}^{(n)}\right) \times \\
& \delta\left(\mathbf{X}^{*}{ }_{j, t}-\mathbf{X}_{j, t}\right) \\
& 0
\end{aligned}
$$

where

$$
\begin{gathered}
\omega_{n}=\prod_{j \in \mathcal{I}_{t}} p\left(\mathbf{X}_{j, t} \mid \mathbf{X}_{t-1}^{(n)}\right) \\
C\left(\mathbf{X}_{t}\right)=\frac{1}{N} \sum_{n=1}^{N} \omega_{n}=\frac{1}{N} \sum_{n=1}^{N} p_{V}\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}^{(n)}\right)
\end{gathered}
$$

When $i^{*}=i^{+}$a previously unused object index is chosen and $p\left(\mathbf{X}^{*}{ }_{i^{*}, t} \mid \mathbf{X}_{t-1}^{(n)}\right)$ reduces to $p\left(\mathbf{X}^{*}{ }_{i^{*}, t}\right)$ (Eq. 5). In this case, initial size parameters of a new object are sampled from learned Gaussian distributions. Location parameters are selected using cluster sampling for efficiency (a hierarchical process in which the image is broken into smaller regions, a region is randomly selected based on the probability of selecting its contents, and a point is sampled from the selected region) on a smoothed foreground segmented image. If a previously dead object is chosen to be reborn ( $i^{*} \neq i^{+}$), the new object parameters are taken from the dead object. Initial head and pose parameters are chosen to maximize the head likelihood in both cases. Refer to [29] for further details. After simplification, it can be shown that $\alpha_{b}$ reduces to

$$
\alpha_{b}=\min \left(1, \frac{p\left(\mathbf{Z}_{i} \mid \mathbf{X}^{*}{ }_{t}\right)}{p\left(\mathbf{Z}_{i} \mid \mathbf{X}_{t}\right)} \times \frac{\prod_{j \in \mathcal{C}_{i^{*}}} \phi\left(\mathbf{X}^{*}{ }_{i^{*}, t}, \mathbf{X}^{*}{ }_{j, t}\right)}{1} \times\right.
$$

(2) Death. The reverse of a birth move, $h_{b}^{B}=h_{d}$, the death move is designed so that it may revert the state back to the initial configuration after a birth, or $\left(\mathbf{X}_{t}, \mathbf{U}\right)=h_{d}\left(h_{b}\left(\mathbf{X}_{t}, \mathbf{U}\right)\right)$. The death move removes an existing object $\mathbf{X}_{i^{*}, t}$ with index $i^{*}$ from the state $\mathbf{X}_{t}$, keeping all other objects fixed. This move implies a dimension change from $m \Gamma \rightarrow m \Gamma-\Gamma$. It proposes a new state $\mathbf{X}^{*}$ and an auxiliary variable $\mathbf{U}^{*}$, generated from the death proposal distribution, $\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*}\right) \sim q_{d}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}\right)$, by applying the transition function $h_{\text {death }}$. The transition is given by $\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*}\right)=h_{d}\left(\mathbf{X}_{t}\right)$, where the specific objects are defined as

$$
\mathbf{X}^{*}{ }_{i, t}=\mathbf{X}_{i, t}, \quad i \neq i^{*} \quad, \quad \mathbf{U}^{*}=\mathbf{X}_{i, t}, \quad i=i^{*}
$$

The proposal for the death move $q_{d}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}\right)$ is given by

$$
q_{d}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}\right)=\sum_{i \in \mathcal{I}_{t}} q_{d}(i) q_{d}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, i\right)
$$

where $q_{d}(i)$ selects the object index $i^{*}$ to be removed and placed in the set of dead objects $\mathcal{D}_{t}$, and the object-specific proposal distribution is
$q_{d}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, i\right)=\left\{\begin{array}{ll}\prod_{j \in \mathcal{I}_{t}, j \neq i^{*}} \delta\left(\mathbf{X}^{*}{ }_{j, t}-\mathbf{X}_{j, t}\right) & \text { if } i=i^{*} \\ 0 & \text { otherwise }\end{array}\right.$.
In practice, the death move selects an object according to $q_{d}(i)$ (which is uniform over the set of existing objects in our model) and removes that object from the state-space. Refer to [29] for further details. After simplification $\alpha_{d}$ is expressed as

$$
\alpha_{d}=\min \left(1, \frac{p\left(\mathbf{Z}_{i} \mid \mathbf{X}^{*}{ }_{t}\right)}{p\left(\mathbf{Z}_{i} \mid \mathbf{X}_{t}\right)} \times \frac{1}{\prod_{j \in \mathcal{C}_{i^{*}}} \phi\left(\mathbf{X}_{i^{*}, t}, \mathbf{X}_{j, t}\right)} \times\right.
$$

(3) Swap. Exchanges the parameters of a pair of objects with indexes $i^{*}$ and $k^{*}$, allowing the tracker to recover from events in which the identity of two people become confused (e.g. in occlusion). The transition is given by $\mathbf{X}^{*}{ }_{t}=h_{s}\left(\mathbf{X}_{t}\right)$, where specific objects are defined

$$
\mathbf{X}^{*}{ }_{i, t}= \begin{cases}\mathbf{X}_{i, t}, & i \neq i^{*}, i \neq k^{*} \\ \mathbf{X}_{k^{*}, t}, & i=i^{*} \\ \mathbf{X}_{i^{*}, t}, & i=k^{*}\end{cases}
$$

The proposal for the swap move $q_{s}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}\right)$ is defined as

$$
q_{s}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}\right) \triangleq \sum_{i, k \in \mathcal{I}_{t}} q_{s}(i, k) q_{s}\left(\mathbf{X}^{*}{ }_{t} \mid \mathbf{X}_{t}, i, k\right)
$$

where the target object indices $i^{*}$ and $k^{*}$ are randomly sampled from $q_{s}(i, k)$. The object-specific proposal distribution exchanges the state values and histories (past state values) of objects $i^{*}$ and $k^{*}$. It can be shown [29] that the expression for the $\alpha_{s}$ reduces to

$$
\alpha_{s}=\min \left(1, \frac{p\left(\mathbf{X}^{*}{ }_{i} \mid \mathbf{Z}_{i: t}\right)}{p\left(\mathbf{X}_{t} \mid \mathbf{Z}_{1: t}\right)}\right)
$$

(4) Body update. Modifies the body parameters of a current object $\mathbf{X}^{*}{ }_{i, t}^{b}$ with index $i=i^{*}$ keeping the head of person $i=i^{*}$ and all other people fixed. The update move transition is given by $\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*}\right)=h_{\text {body }}\left(\mathbf{X}_{t}, \mathbf{U}\right)$, where the specific objects are defined as

$$
\left(\mathbf{X}_{i, t}^{* b}, \mathbf{X}_{i, t}^{* b}\right)= \begin{cases}\left(\mathbf{X}_{i, t}^{b}, \mathbf{X}_{i, t}^{b}\right) & i \neq i^{*} \\ \left(\mathbf{U}, \mathbf{X}_{i, t}^{b}\right) & i=i^{*}\end{cases}, \quad \mathbf{U}^{*}=\mathbf{X}_{i^{*}, t}^{b}
$$

The body update move proposal is defined as

$$
q_{\text {body }}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}\right)=\sum_{i \in \mathcal{I}_{t}} q_{\text {body }}(i) q_{\text {body }}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}, i\right)
$$

The object-specific proposal distribution is defined as

$$
\begin{gathered}
q_{\text {body }}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}, i\right)= \\
\frac{1}{N} \sum_{n} p\left(\mathbf{X}_{i^{*}, t}^{* b}, \mathbf{X}_{t-1}^{b,(n)}\right) p\left(\overline{\mathbf{X}_{i^{*}, t}^{*}} \mid \mathbf{X}_{t-1}^{b,(n)}\right) \delta\left(\overline{\mathbf{X}_{i}^{*}} \overline{ }_{i, t}-\overline{\mathbf{X}_{i^{*}, t}^{b}}\right) \\
\prod_{j \neq i^{*}} p\left(\mathbf{X}_{j, t} \mid \mathbf{X}_{t-1}^{(n)}\right) \delta\left(\mathbf{X}^{*}{ }_{j, t}-\mathbf{X}_{j, t}\right)
\end{gathered}
$$

where $\overline{\mathbf{X}_{i^{*}, t}^{*}}$ denotes all state parameters except $\mathbf{X}_{i^{*}, t}^{* b}$, and $\mathbf{X}_{i, t}^{* b}$ denotes the proposed body configuration for target $i^{*}$. This implies randomly selecting a person $i^{*}$ and sampling a new body configuration for this person from $p\left(\mathbf{X}_{i^{*}, t}^{* b} \mid \mathbf{X}_{t-1}^{b,(n^{*})}\right)$, using an appropriate sample $n^{*}$ from $t-1$, leaving the other parameters unchanged. Thus, $\alpha_{\text {body }}$ can then be shown to reduce to [29]:

$$
\alpha_{\text {body }}=\min \left(1, \frac{p\left(\mathbf{Z}_{t}^{b} \mid \mathbf{X}_{i^{*}, t}^{* b}\right.}{p\left(\mathbf{X}_{t}^{*}, \mathbf{U}, \mathbf{V}_{i^{*}, t}^{*}\right.}, \frac{\phi\left(\mathbf{X}^{*}{ }_{i^{*}, t}, \mathbf{X}_{i, t}^{*}\right)}{\left.p\left(\mathbf{Z}_{t}^{b} \mid \mathbf{X}_{i^{*}, t}^{b}\right)\right]_{\left.t \in \mathcal{C}_{i^{*}} \phi\left(\mathbf{X}_{i^{*}, t}, \mathbf{X}_{t, t}\right)\right.}}\right)
$$

(5) Head update. Modifies the head parameters of a current object $L_{i^{*}, t}^{* b}$ with index $i^{*}$. The transition is given by $\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*}\right)=$ $h_{\text {head }}\left(\mathbf{X}_{t}, \mathbf{U}\right)$, where the specific objects are defined as

$$
\left(\mathbf{X}_{i}^{* b}, L^{*}{ }_{i}, \theta_{i}^{*}\right)= \begin{cases}\left(\mathbf{X}_{i, t}^{b}, L_{i, t}, \theta_{i, t}\right) & i \neq i^{*} \\ \left(\mathbf{X}_{i, t}^{b}, \mathbf{U}, \theta_{i, t}\right) & i=i^{*}\end{cases}, \quad \mathbf{U}^{*}=L_{i, t}
$$

The head update move proposal is defined as

$$
q_{\text {head }}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}\right)=\sum_{i \in \mathcal{I}_{t}} q_{\text {head }}(i) q_{\text {head }}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}, i\right)
$$

where the object-specific proposal distribution is defined as

$$
\begin{gathered}
q_{\text {head }}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}, i\right)= \\
\frac{1}{N} \sum_{n} p\left(L^{*}{ }_{i^{*}, t} \mid \mathbf{X}_{t-1}^{(n)}\right) p\left(\overline{L^{*}}{ }_{i^{*}, t} \mid \mathbf{X}_{t-1}^{(n)}\right) \delta\left(\overline{L^{*}}{ }_{i^{*}, t}-\overline{L_{i^{*}, t}}\right) \times \\
\prod_{j \neq i^{*}} p\left(\mathbf{X}_{j, t} \mid \mathbf{X}_{t-1}^{(n)}\right) \delta\left(\mathbf{X}_{j, t}^{*}-\mathbf{X}_{j, t}\right)
\end{gathered}
$$

where $\overline{L^{*}}{ }_{i^{*}, t}$ denotes all state parameters except $L^{*}{ }_{i^{*}, t}$. This implies selecting a person $i^{*}$ and sampling a new head configuration for this person from $p\left(\mathbf{X}_{i^{*}, t}^{*} \mid \mathbf{X}_{t-1}^{h,(n^{*})}\right)$, using an appropriate
sample $n^{*}$ from the previous time leaving the other parameters unchanged. $\alpha_{\text {head }}$ can then be shown to reduce to [29]:

$$
\alpha_{\text {head }}=\min \left(1, \frac{p\left(\mathbf{Z}_{t}^{b} \mid L^{*}{ }_{i^{*}, t}\right)}{p\left(\mathbf{Z}_{t}^{b} \mid L_{i^{*}, t}\right)} \times \frac{p\left(L^{*}{ }_{i^{*}, t} \mid \mathbf{X}_{i^{*}, t}^{* b}\right)}{p\left(L_{i^{*}, t} \mid \mathbf{X}_{i^{*}, t}^{b}\right)}\right)
$$

(6) Pose update. Modifies the pose parameter $\theta_{t, i^{*}}$ of a person with index $i^{*}$. Like the previous update moves it is self-reversible and does not change the dimension of the state. The move transition is given by $\left(\mathbf{X}^{*}, \mathbf{U}^{*}\right)=h_{\theta}(\mathbf{X}, \mathbf{U})$, where

$$
\left(\mathbf{X}_{i}^{*}{ }_{i^{*}, t}^{*}, \theta_{i}^{*}\right)= \begin{cases}\left(\mathbf{X}_{i}^{b}, L_{i}, \theta_{i}\right) & i \neq i^{*} \\ \left(\mathbf{X}_{i}^{b}, L_{i}, \mathbf{U}\right) & i=i^{*}, \quad, \quad \mathbf{U}^{*}=\theta_{i^{*}}\end{cases}
$$

The head-pose update move proposal is defined as

$$
q_{\theta}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}\right)=\sum_{i \in \mathcal{I}_{t}} q_{\theta}(i) q_{\theta}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}, i\right)
$$

where the object-specific proposal distribution is defined as

$$
\begin{gathered}
q_{\theta}\left(\mathbf{X}^{*}{ }_{t}, \mathbf{U}^{*} \mid \mathbf{X}_{t}, \mathbf{U}, i\right)=\frac{1}{N} \sum_{n} p\left(\theta^{*}{ }_{i^{*}, t} \mid \theta_{t-1}^{(n)}\right) p\left(\overline{\theta^{*}}{ }_{i^{*}, t} \mid \overline{\theta^{*}}_{t-1}^{(n)}\right) \times \\
\delta\left(\overline{\theta^{*}}{ }_{i^{*}, t}-\bar{\theta}_{i^{*}, t}\right) \prod_{j \neq i^{*}} p\left(\mathbf{X}_{j, t} \mid \mathbf{X}_{t-1}^{(n)}\right) \delta\left(\mathbf{X}_{j, t}^{*}-\mathbf{X}_{j, t}\right)
\end{gathered}
$$

where $\theta^{*}{ }_{i^{*}, t}$ denotes the proposed head-pose configuration for target $i^{*}$ and $\overline{\theta^{*}}{ }_{i^{*}, t}$ denotes all state parameters except $\theta^{*}{ }_{i^{*}, t}$. This implies selecting a person index, $i^{*}$, and sampling a new head-pose for this person from $p\left(\theta^{*}{ }_{i^{*}, t} \mid \theta_{t-1}^{(n^{*})}\right)$, using an appropriate sample $n^{*}$ from the previous time step, leaving the other parameters unchanged. $\alpha_{\theta}$ can then be shown [29] to reduce to

$$
\alpha_{\theta}=\min \left(1, \frac{p\left(\mathbf{Z}_{t}^{b} \mid \mathbf{X}_{i^{*}, t}^{* b}\right)}{p\left(\mathbf{Z}_{t}^{b} \mid \mathbf{X}_{i^{*}, t}^{b}\right)}\right)
$$

## F Inferring a Solution

The first $N_{b}$ samples added to the Markov Chain are part of the burn-in period, which allows the Markov Chain to reach the target density. The chain after this point approximates the filtering distribution, which represents a belief distribution of the current state of the objects given the observations. It does not, however, provide a single answer to the tracking problem. To find this, we compute a point estimate solution, which is a single state computed from the filtering distribution which serves as the tracking output. To determine the set of objects in the scene, we compute the mode of the object configurations in the Markov Chain (each sample contains a set of object indices; we select the set that is repeated most often accounting for identity changes resulting from swap moves). Using these samples, we find the mean configuration of each of the body and head spatial configuration parameters $\left(\mathbf{X}_{i, t}^{b}, L_{i, t}^{b}\right)$. For the out-of-plane head rotations represented by the discrete exemplar $\theta_{i}$, we compute the mean of the corresponding Euler angles for pan and tilt. The detailed steps of our joint multi-person body-head tracking and VFOA-W estimation model are summarized in Figure 6.

## IV. Modeling the VFOA for a Varying Number of WANDERING PEOPLE

The VFOA-W task is to automatically detect and track a varying number of people able to move about freely, and to estimate their VFOA. The VFOA-W problem is significantly more complex than the traditional VFOA problem because it allows for the number of people in the video to vary and it allows for the

At each time step, $t$, the posterior distribution of Eq. 9 for the previous time step is represented by a set of $N$ unweighted samples $p\left(\mathbf{X}_{t-1} \mid \mathbf{Z}_{1: t-1}\right) \approx\left\{\mathbf{X}_{t-1}^{(n)}\right\}_{n=1}^{N}$. The approximation of the current distribution $p\left(\mathbf{X}_{t} \mid \mathbf{Z}_{1: t}\right)$ is constructed according to steps 1 and 2, from which a point estimate solution for head and body parameters is determined in step 3. The values of these parameters are used in step 4 to determine if a person's attention is directed at the advertisement (focused) or not (unfocused).

1) Initialize the Markov Chain by choosing a sample from the $t-1$ Markov Chain with the mode configuration $\left(m_{t-1}^{\text {mode }}\right)$. Apply the motion model to each object, $\prod_{i \in Z_{t}} p\left(\mathbf{X}_{t, i} \mid \mathbf{X}_{t-1, i}^{(n)}\right)$, and accept as sample $n=0$.
2) RJMCMC Sampling. Draw $N+N_{B}$ samples according to the following schedule.

- Begin with the state of the previous sample $X_{t}^{(n)}=X_{t}^{i^{n-11}}$.
- Choose Move Type by sampling from the set of moves $\Upsilon=$ \{birth, death, swap, body update, head update, pose update $\}$ with prior probability $p_{i^{*}}$.
- Select a Target $i^{*}$ ( or set of targets $i^{*}, k^{*}$ for swap) according to the target proposal $q_{v}(i)$ for chosen move type.
- Sample New Configuration $\mathbf{X}^{*}$ : from the move-specific proposal distribution $q_{v^{*}}$. For move type $v$, this implies:
- Birth - add a new person $i^{*}$ according to Eq. 17, $m_{t}^{(n) *}=m_{t}^{(n)}+1$.
- Death - remove an existing person $i^{*}$ according to Eq. 23, $m_{t}^{(n) *}=m_{t}^{(n)}-1$.
- Swap - swap the parameters of two existing people $i^{*}, k^{*} \mathbf{X}_{i, t}^{(n)} \rightarrow \mathbf{X}_{k, t}^{(n) *}, \mathbf{X}_{k, t}^{(n)} \rightarrow \mathbf{X}_{i, t}^{(n) *}$.
- Body Update - update the body parameters $L_{i, t}^{k,(n) *}$ of an existing person $i^{*}$ (Eq. 30).
- Head Update - update the head parameters $L_{i, t}^{k,(n) *}$ of an existing person $i^{*}$.
- Pose Update - update the pose parameter $\theta_{i, t}^{(n) *}$ of an existing person $i^{*}$.
- Compute Acceptance Ratio $\alpha$ according to Equation 21, 25, 28, 32, 36, or 40.
- Accept/Reject. Accept the proposal $\mathbf{X}^{*}$ : if $\alpha \geq 1$, otherwise accept with probability $\alpha$. If accepted, add it to the Markov Chain $\mathbf{X}_{t}^{(n)}=\mathbf{X}^{*}_{t}^{(n)}$. If rejected, add the previous sample in the Markov Chain to the current position $\mathbf{X}_{t}^{(n)}=\mathbf{X}_{t}^{(n-1)}$.

3) Compute a Point Estimate Solution from the Markov Chain (as in Section III-F):

- to avoid bias in the Markov Chain, discard the first $N_{B}$ burn-in samples. The sample set $\left\{\mathbf{X}_{t}^{(n)}\right\}_{n=N_{B}+1}^{N_{B}+N}$ represents an approximation of the filtering distribution.
- form a sample set $W$ from the mode configuration $\hat{X}_{t}$ as described in Section III-F. Compute the point estimate body $\hat{X}_{t}^{b}$ and head $\hat{X}_{t}^{b}$ parameters from their mean value in $W$.

4) Determine the VFOA-W for each person in the scene according to Section IV.

Fig. 6. Algorithm for joint multi-person body and head tracking and VFOA-W estimation with RJMCMC.
people in the video to freely walk about the scene, whereas in previous works [36] the number of people appearing in a single video was fixed and they were constrained to remain seated (for their VFOA to be estimated). The advertising application chosen as an introduction to VFOA-W represents a relatively simple instance of the problem as we only attempt to measure VFOA for a single target, though it is straightforward to extend this model for multiple targets.

At each time $t$ a person's VFOA-W is defined as being in one of two states $f_{t}$ :

- focused: $f_{t}=1$, looking at the advertisement, or
- unfocused: $f_{t}=0$, not looking at the advertisement.

Note that this is just one of many ways in which the VFOA-W can be represented, but it is sufficient to solve the tasks set forth in Section I. A person's state of focus depends both on their location and on their head-pose as seen in Figure 7. For head location and head-pose information, we rely on the output of the RJMCMC tracker described in Section III.
VFOA-W Modeling with a Gaussian mixture Model (GMM) Estimating the VFOA-W can be posed in a probabilistic framework as finding the focus state maximizing the a posteriori probability $\hat{f}=\arg \max _{f} p\left(f \mid z^{h}\right) \propto p\left(z^{h} \mid f\right) p(f)$, where $z^{h}=($ pan,tilt $)$ is the head pointing vector of the person parametrized by a pan and tilt angle (see Fig. 4). We assume the prior on the VFOA-W state $p(f)$ to be uniform thus, it has no effect on the VFOA-W estimation. To model the probability of being in a focused state we consider the horizontal head position $x^{h}$ and head pointing vector (see Figure 7). Because the target is stationary, the ranges of $z^{h}$ corresponding to the focused state are directly dependent on the location of the head in the image.

For this reason, we chose to split the image into $K_{v f o n-w}=5$ horizontal regions $I_{k}, k=\{1, \ldots, 5\}$, and modeled the probability of a focused state as

$$
\begin{aligned}
p\left(z^{h} \mid f=1\right) & =\sum_{k=1}^{K} p\left(x^{h} \in I_{k}, z^{h} \mid f=1\right) \\
& =\sum_{k=1}^{K} p\left(x^{h} \in I_{k}\right) p\left(z^{h} \mid x^{h} \in I_{k}, f=1\right)
\end{aligned}
$$

where the first term $p\left(x^{h} \in I_{k}\right)$ models the probability of a person's head location belonging to region $I_{k}$, and the second term $p\left(z^{h} \mid x^{h} \in I_{k}, f=1\right)$ models the probability of focused head-pose given the region the head belongs to. The inclusion of the head location in modeling the VFOA-W allowed us to solve an issue not previously addressed in [24], [34], [38]: resolving the VFOA-W of a person whose focus state depends on their location.

The terms of the VFOA-W model in Equation 41 are defined as follows. Each region is defined by its center and width, denoted by $x_{I_{k}}$ and $\sigma_{I_{k}}$, resp. The probability of a head location $x^{h}$ belonging to region $I_{k}$ is modeled by a Gaussian distribution $p\left(x^{h} \in\right.$ $\left.I_{k}\right)=\mathcal{N}\left(x^{h}, x_{I_{k}}, \sigma_{I_{k}}\right)$. For each region, the distribution of pointing vectors representing a focused state was modeled using a Gaussian distribution $p\left(z^{h} \mid x^{k} \in I_{k}, f=1\right)=\mathcal{N}\left(z^{h} ; z_{I_{k}}^{h}, \Sigma_{I_{k}}^{z}\right)$ where $z_{I_{k}}^{h}$ are the mean pointing vectors and $\Sigma_{I_{k}}^{z}$ is the full covariance matrix learned from training data. 2D projections of typical pointing vectors for each region are seen in Figure 7. The probability of being unfocused is modeled as a uniform distribution $p\left(z^{h} \mid f=0\right)=T_{v f o n-w}$.
The parameters of the VFOA-W model (Gaussian mean and covariance matrix) and the uniform distribution modeling the unfocused state distribution were learned from training data described in Section V. Though our VFOA-W model does not make use of the vertical head location, it is straightforward

![img-5.jpeg](img-5.jpeg)

Fig. 7. VFOA-W modeling. Top: VFOA-W is determined by head-pose and horizontal position in the image. The horizontal axis is split into $K_{v f o a-w}=$ 5 regions $\left(I_{1}, \ldots, I_{5}\right)$, and a VFOA-W model is defined for each of these regions. Yellow, green, cyan, black, and blue data points represent focused head locations used for training and red arrows represent 2D projections of typical samples of focused pointing vectors $z^{h}$. Note that the advertisement is affixed to a window and appears just above the image frame. Bottom: over 9400 training points representing a person in a focused state (also seen in the left pane) were split into the $K_{v f o a-w}$ regions and used to train a model for each region.
to generalize the model to do this. To reduce noisy VFOA-W estimations, a smoothing filter with an 10 -frame window was applied to the GMM output.

## VFOA-W Modeling with a hidden Markov model (HMM)

The VFOA-W GMM does not take into account the temporal dependencies between the focus states. Such dependencies can be modeled using an HMM. If we denote a sequence of focus states by $f_{1: T}$ and a sequence of head pose observations as $z_{1: T}^{h}$, the joint posterior probability of the observation and the states can be written as:

$$
p\left(f_{1: T}, z_{1: T}^{h}\right)=p\left(f_{0}\right) \prod_{t=1}^{T} p\left(z_{t}^{h} \mid f_{t}\right) p\left(f_{t} \mid f_{t-1}\right)
$$

In this equation, the emission probabilities $p\left(z_{t}^{h} \mid f_{t}\right)$ are modeled as before (GMM for focused and uniform for unfocused). But, in the HMM case, a transition matrix is used to model the temporal VFOA-W state transition $p\left(f_{t} \mid f_{t-1}\right)$. Given $z_{1: T}^{h}$, VFOA-W recognition is done by finding the optimal sequence maximizing $p\left(f_{1: T} \mid z_{1: T}^{h}\right)$ using the Viterbi algorithm [27].

TABLE I
SYMBOLS, VALUES, AND DESCRIPTIONS FOR KEY PARAMETERS.


## V. TRAINING AND PARAMETER SELECTION

## A. Experimental Setup

To simulate the advertising application described in the introduction, a home-made advertisement was placed in an exposed window with a camera set behind. Several actors were instructed to pass in front of the window and allowed to look at the advertisement (or not) as they would naturally (actors were used due to privacy concerns for actual passers-by). A recording of 10minute duration ( $360 \times 288$ resolution, 25 fps ) was made in which a maximum of three people appear in the scene simultaneously. The recorded data includes challenging events such as people occluding each other and people entering/exiting the scene.

## B. Training and Parameter Selection

The recorded video data was organized into a disjoint training and test set of equal size. The training set, consisting of nine sequences (for a total of 1929 frames), was manually annotated for body location, head location, and focused/unfocused state.

Table I provides a list of the key parameters of our model. Parameters were either learned automatically from training data (learned), tuned by hand (hand-tuned), or selected without exhaustive tuning (untuned). The parameters for the foreground segmentation were hand-tuned by observing results on the training set. The binary body model was trained using background subtraction and training set annotations. Using this information, GMMs were trained for the foreground and background models (parameters were selected through cross-validation). Head annotations were used to learn the parameters of the Gaussian skincolor distribution in the head-pose skin feature. The silhouette mask was also trained using the head annotations by averaging the binary patches corresponding to head annotations. Parameters for the VFOA-W model, including $T_{v f o a-w}$, were optimized on the training data (bootstrapped to 9400 training points, see Figure 7) to achieve the highest VFOA-W event recognition performance (see Section VI for details). The transition probability of the HMM $p\left(f \mid f_{t-1}\right)$ is defined as a 0.8 for a transition to the same state and 0.2 to change state. The training set was also used to learn prior size models (scale and eccentricity) for the person models. Texture models and the skin color masks were learned from the Prima-Pointing Database, which consists of 30 sets of

TABLE II
TEST SET DATA SUMMARY.


images of 15 people, each containing 93 frontal images of the same person in a different pose ranging from -90 degrees to 90 degrees (see Figure 4). The texture parameters $Z_{\theta}$ and $\lambda_{0}^{t e x}$ were learned according to the method described in [40].

## VI. Evaluation

In order to evaluate the performance of our application, the test set was annotated similarly to the training set. The test set consists of ten sequences summarized in Table II. Sequences $a$ $d$ contain three people (appearing sequentially) passing in front of the window. Sequences $e-i$ contain two people; sequence $j$ contains three people appearing simultaneously. We compared our results with the ground truth over 200 experiments on the 10 test sequences (corresponding to 20 full runs of the DBN model per sequence). The length of the Markov Chain was chosen such that there was a sufficient number of samples for good quality tracking (see Table I). Experimental results are illustrated in Figure 9 and fully shown in companion videos [14].

## A. Multi-Person Body and Head Tracking Performance

To evaluate the tracking performance we adopt a set of measures proposed in [31], with some minor changes to names and notation. These measures evaluate three tracking qualities: the ability to estimate the number and placement of people in the scene (detection), how tightly the estimated bounding boxes fit the ground truth (spatial fit), and the ability to persistently track a particular person over time (tracking). Overall results are given in Table III, with illustrations for sequences $b, e, h$, and $i$ in Fig. 9 and further details available at [14].

To evaluate detection, we rely on the rates of False Positive and False Negative errors (normalized per person, per frame) denoted by $\overline{F P}$ and $\overline{F N}$. As indicated in Tab. III, for a given person in a given frame there is a $1.8 \%$ chance of our method producing a false positive error and $1.1 \%$ chance of producing a false negative error. The Counting Distance $\overline{C D}$ measures how close the estimated number of people is to the actual number (normalized per person per frame). A $\overline{C D}$ value of zero indicates a perfect match. As shown in Tab. III, the $\overline{C D}$ is near zero, indicating good performance.

Spatial fitting between the ground truth region and the tracker output is measured for the body and the head using the $f$-measure $F=\frac{\partial F P}{\partial\left\langle f_{i}\right\rangle}$, where $\rho$ is recall and $\nu$ is precision. A perfect fit is indicated by $F=1$, no overlap by $F=0$. Tab. III indicates that the spatial fitting for both the head and body were quite good, above $80 \%$.

To evaluate tracking performance we rely on the purity measure, which estimates the degree of consistency with which the estimates and ground truths were properly identified ( $\bar{P}$ near 1 indicates well maintained identity and $\overline{\bar{P}}$ near 0 indicates poor performance, see [31] for details) Tab. III shows that our model had good tracking quality (.93), though it dropped to .81 in sequence $h$ where two people occlude one another as they cross paths.

TABLE III
MULTI-PERSON TRACKING RESULTS AVERAGED OVER THE ENTIRE TEST


## B. Advertisement Application Performance

To evaluate the performance of the advertisement application, the results from our model were compared with ground truth annotations. Results appear in Fig. 8 (summarized in Tab. IV) and the companion videos [14]. For evaluation, we considered six criteria defined below, and report results for the GMM and HMM models for each. To reduce errors caused by people partially appearing in the image, VFOA-W results are computed on a region-of-interest defined from 8 frames after a person appears until 8 frames before they exit the scene.

1. The number of people exposed to the advertisement. Over the entire test set, 25 people passed the advertisement, while our RJMCMC tracking model estimated 25.15 people appeared, on average (over 20 runs, std dev $=.17$ ) which results in $3.4 \%$ error for both models. In Figure 8a we can see that the number of people was correctly estimated for every sequence except $a, c$, and $i$.
2. The number of people who looked the advertisement. 20 of the 25 people actually focused on the advertisement at some point. The GMM model estimated 22.95 people looked at the ad, while 21.2 did so for the HMM resulting in $6.0 \%$ (HMM) and $14.75 \%$ (GMM) error rates.
3. The number of events where someone looked the advertisement. The VFOA-W recognition sequences were broken into continuous segments, or events, where a look-event is a focused state for $t \geq 3$ frames. 21 look-events actually occurred over the test set. The GMM model estimated 28.5 look-events occurred while the HMM model estimated 21.45 giving error rates of $2.14 \%$ (HMM) and $35.45 \%$ (GMM). These results were determined through a standard symbol-matching technique.
4. Time spent looking at the advertisement. Over the entire test set, people spent 37.28 s looking at the advertisement. The GMM model estimated that people looked at the ad for 38.59 s while the HMM estimated 37.89 s , yielding $1.63 \%$ (HMM) and $3.51 \%$ (GMM) error rates.
5 and 6. VFOA-W recognition rate estimation. The VFOA-W recognition rate is computed with respect to frames as well as events (continuous segments of frames with a similar VFOA-W state). The frame-based recognition rate is computed directly as the number of frames in which the estimate and ground truth agree over the number of frames. The overall frame-based recognition rates are $83.90 \%$ (mean GMM) and $92.53 \%$ (mean HMM). The aforementioned $F$-measure, $F=\frac{\partial p_{i t}}{\partial\left\langle f_{i}\right\rangle}$, is used to compute the event-base recognition rate [16] where $\rho$ is the event-based recall (the number of segments where the ground truth and estimate agree, normalized by the number of segments in the ground truth) and $\nu$ is the precision (the number of segments where the ground truth and estimate agree, normalized by the number of segments in the estimate). The overall event-based recognition rates are $90.37 \%$ (GMM) and $93.85 \%$ (HMM). Results for each sequence appear in Fig. 8(e) and $(f)$.

TABLE IV
VFOA-W ESTIMATION SUMMARY FOR GMM AND HMM MODELS. error rates (in \%) | | \# people | \# people looked | \# look events | time focused | | :--: | :--: | :--: | :--: | :--: | | hmm | 3.40 | 6.00 | 2.14 | 1.63 | | gmm | 3.40 | 14.75 | 35.45 | 3.51 | | | VFOA-W recognition rates | | | | | | | | | event-based | frame-based | | | | hmm | 93.95 | 92.53 | | | gmm | 90.37 | 83.90 | | | | | | | | | |

## C. Varying the Number of Particles

To study the model's dependency on the number of samples, we conducted a series of experiments on sequence $i$ which is omitted for space reasons. In summary, $N=600$ samples were required for good performance in Matlab between $<1$ and 5 seconds processing time per frame on an Intel Pentium IV 3.2 GHz processor. We refer the reader to [14] for details.

## VII. DISCUSSION AND LIMITATIONS

While our proposed model yielded convincing results on the preceding experiments, there exist some limitations to the models and data set. In this section we discuss some of these limitations and how they might be addressed in future work.

## 1. Multi-Person Tracking.

Separability of classes in the binary background observation model limits the number of people that the model can track simultaneously. As the number of people increases, the learned background model loses ability to discriminate between different numbers of objects (i.e. the fewer objects in the scene, the more confident our estimation). In independent experiments, the binary observation model was found to be robust for up to five simultaneous objects, though this limitation depends on the typical size of the objects with respect to the scene and the variability of object size. An alternative approach to the binary observation model proposed in [33] addresses this limitation.

Our observation model is also limited in its ability to handle occlusion. Though it performs well for full occlusion in our experiments (with a relatively small number of people), our approach would be less robust in situations where a monocular camera view is insufficient to resolve the occlusion due to the camera placement or multiple occlusions This is a common problem to monocular tracking algorithms. A multi-view approach such as that proposed by in [5] may better address these types of situations, which can occur in realistic environments.

Finally, because it models relative size and overlap of the foreground and background, the binary observation model is not robust in situations where the typical size of a person varies dramatically (e.g. if a person appears much smaller in the background than in the foreground).

## 2. Head Tracking and Pose Estimation.

The head pose estimation is principally limited by performance of the texture and skin color models. The performance of these models is dependent on the resolution of the head in the image. Lower resolution leads to greater error in the head pose estimation (and thus the VFOA-W estimation). In our experiments, the head was typically approximately $40 \times 60$ pixels. In [4], the head pose model presented in this work was shown to yield good tracking results for head sizes of $20 \times 30$ pixels, though data from multiple cameras were used.

The performance of the texture and skin color models also depends on the placement of the camera relative to the head.

Experiments in [3] show that our head pose model performs better for near frontal faces ( $12^{\circ}$ mean error) than for faces near profile poses $\left(18^{\circ}\right.$ mean error).

## 3. VFOA-W Modeling.

The relatively simple $x$-axis positional model used for VFOAW is sufficient to yield good results to estimate VFOA for moving people. A more complex scenario may require a more geometrically complex VFOA-W model which takes into account the observed head pose and the locations of the advertisement, person and camera.

## 4. Data Set.

Although the designed data set was useful to demonstrate the ability of our VFOA-W algorithm to perform in a realistic situation, it does contain some limitations. First, only four actors appeared throughout the data set. Second, the actors did not walk into the far background, and thus their size did not vary appreciably. Third, the maximum number of actors appearing simultaneously did not exceed three, and the actors only crossed paths in one test sequence and one training sequence (causing an occlusion). Finally, though tested outdoors, the lighting conditions were relatively stable. The design of a future VFOA-W data set should take these issues into account.

## VIII. CONCLUSION

In this article, we have introduced the problem of estimating the visual focus of attention for a varying number of wandering people and presented a principled probabilistic approach to solving it. Our approach expands on state-of-the-art RJMCMC tracking models, with novel contributions to object modeling, observation modeling, and inference through sampling. It is a general model that can be easily adapted to similar tasks. We applied our model to a realistic advertising application and provided a rigorous objective evaluation of its performance in this context. We compared two VFOA-W models (GMMs and HMMs) and found the temporal dependencies of the HMM to yield superior performance. From these results we have shown that our proposed model is able to track a varying number of moving people and determine their VFOA-W with good quality (exhibiting only a $6 \%$ error rate in determining the number of people who looked at the ad). Finally, through the detailed evaluation of the current strengths and limitations of our approach, we have identified several lines of research for future work.

## Acknowledgments

This work was funded by the Swiss National Science Foundation (SNSF) through the National Center for Competence in Research (NCCR) on Interactive Multimodal Information Management (IM2), by the European IST Project 'Augmented Multiparty Interaction with Distant Access' (AMIDA, FP6-033812, pub. AMIDA-35), and by the European IST Project 'Content Analysis and Retrieval Technologies Applied to Knowledge Extraction from massive Recordings' (CARETAKER). We also thank our colleagues at IDIAP who contributed their time for recording the data set.
