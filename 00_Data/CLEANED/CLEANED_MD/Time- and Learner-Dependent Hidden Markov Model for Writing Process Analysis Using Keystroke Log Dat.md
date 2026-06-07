# Time- and Learner-Dependent Hidden Markov Model for Writing Process Analysis Using Keystroke Log Data 

## Masaki Uto ${ }^{1}$ (D) $\cdot$ Yoshimitsu Miyazawa ${ }^{2} \cdot$ Yoshihiro Kato ${ }^{3} \cdot$ Koji Nakajima ${ }^{3} \cdot$ Hajime Kuwata ${ }^{3}$

Published online: 12 March 2020
(c) International Artificial Intelligence in Education Society 2020


#### Abstract

Teaching writing strategies based on writing processes has attracted wide attention as a method for developing writing skills. The writing process can be generally defined as a sequence of subtasks, such as planning, formulation, and revision. Therefore, instructor feedback is often given based on sequence patterns of those subtasks. For such feedback, instructors need to analyze sequence patterns for all learners, which becomes problematic as the number of learners increases. To resolve this problem, this study proposes a new machine-learning method that estimates sequence patterns from keystroke log data. Specifically, we propose an extension of the Gaussian hidden Markov model that incorporates parameters representing temporal change in a subtask appearance distribution for each learner. Furthermore, we propose a collapsed Gibbs sampling algorithm as the parameter estimation method for the proposed model. We demonstrate effectiveness of the proposed model by applying it to actual keystroke log datasets.


Keywords Writing skills $\cdot$ Writing process $\cdot$ Keystroke log $\cdot$ Hidden Markov model $\cdot$ Markov chain Monte Carlo method

[^0]
[^0]:    Masaki Uto
    uto@ai.lab.uec.ac.jp

    1 The University of Electro-Communications, 1-5-1 Chofugaoka, Chofu, Tokyo 182-8585, Japan
    2 The National Center for University Entrance Examinations, 2-19-23 Komaba, Meguro, Tokyo 153-8501, Japan
    3 Benesse Educational Research and Development Institute, 1-34 Ochiai, Tama, Tokyo 206-8686, Japan

# Introduction 

Recently, the importance of nurturing writing skills in higher education has been widely acknowledged (Uto and Ueno 2015). A typical instruction method for writing is an instructor providing feedback on a completed text. As another approach, instruction methods that focus on the writing process have attracted attention in recent years (Deane and Zhang 2015; Leijten and Waes 2013; Seow 2002; Zhang et al. 2016; Bayat 2014; Conijn et al. 2018).

The writing process can be generally regarded as a sequence of subtasks, such as planning, formulation, and revision (Flower and Hayes 1981; Seow 2002; Bayat 2014; Southavilay et al. 2010b). These processes are known to be dependent on writing skills (Stevenson et al. 2006; Hayes and Flower 1980; Sasaki 2000, 2002; Larios et al. 2008; Chan 2017). For example, learners with advanced skills tend to formulate faster but spend more time on revisions, as compared with those with lower skills (Sasaki 2000, 2002; Larios et al. 2008). In addition, learners with advanced skills tend to make major edits in logical structures and main arguments, while those with lesser skills primarily perform superficial corrections such as expressions and typographical errors (Sasaki 2000; 2002; Lester and Witte 1981; Barkaoui 2016). Because there is a relation between writing skills and writing processes, instruction based on the writing process can be an effective approach toward improving writing skills (Bayat 2014; Conijn et al. 2018).

Instructions focused on the writing process are often based on the appearance pattern of the above-described subtasks (Bayat 2014; Conijn et al. 2018). As a method for analyzing appearance patterns of these subtasks, the think-aloud technique and video playback stimulation method have been long used (Stevenson et al. 2006; de Larios et al. 2008). In the think-aloud technique, learners sequentially utter their thoughts during the writing process. The playback stimulation method presents learners with videos of their writing process and has learners discuss their thoughts. However, these methods require considerable time for analysis, so they are impractical when there are many learners.

To address this issue, writing process analysis methods using keystroke log data recorded during composition on a computer have been recently proposed (Deane and Zhang 2015; Leijten and Waes 2013; Zhang et al. 2016; Chan 2017; Conijn et al. 2018). For example, Zhang et al. (2016) proposed a method in which the writing process is categorized based on the distribution of intervals between word inputs. However, while existing methods can categorize stages in the writing processes, there is no method for estimating subtask appearance patterns by learner.

We therefore propose a method for estimating subtask appearance patterns by learner from keystroke log data. Specifically, we propose a method for converting keystroke log data of each learner to time-series data with multiple features that express writing characteristics for applying an unsupervised machine learning method. Feature extraction is based on a sliding window approach, which divides keystroke log data into analytical frames with a small time-width and extracts features from each frame. The Gaussian hidden Markov model (GHMM) is well-known as a typical unsupervised machine learning method for such time-series data. GHMM assumes that observational data at an arbitrary point in time arise depending on a

latent variable called the state, and that the state sequence can be estimated from the data. Therefore, by applying GHMM under an assumption of latent state for each analytical frame as a subtask, a sequence of subtasks for each learner can be estimated from keystroke log data. However, because this approach estimates a subtask for each analytical frame with a small time-width, the variety of subtask sequences becomes extremely large, hindering interpretation of the writing process for each learner. For educational application, knowing the subtask to be performed each moment is not necessarily important. What we need, instead, is to know the subtask appearance patterns by learner, as discussed earlier. The information required to understand the patterns is the appearance ratios for subtasks in a time interval with a certain time span and the temporal changes in the ratios. For example, we wish to know the extent to which each learner performs subtasks such as formulation, major edits, and superficial corrections in every quarter of writing time. Information on temporal changes in the subtask appearance ratios will be helpful by allowing learners and instructors to characterize the writing patterns of each learner quantitatively. Furthermore, it will also be beneficial for instructors by allowing them to give appropriate feedback and instruction toward improving learners' writing activities.

For the above reasons, this paper proposes an extension of GHMM that incorporates parameters representing temporal change in the subtask appearance distribution for each learner. For the model, we first divide feature vector sequences obtained from each learner's keystroke data into a few time intervals. We then incorporate parameters that express state appearance probabilities for each learner in each time interval in the GHMM. The characteristics of the proposed model are as follows:

1. Because the incorporated parameters represent temporal change in subtask appearance patterns for each learner, by interpreting the parameters we can understand the writing process of each learner.
2. By comparing differences in state appearance distributions between learners, we can quantitatively analyze between-learner differences in the writing process.
3. The writing processes of learners can be categorized by applying typical cluster analyses, taking differences in state appearance distributions between learners as the distance function.

As a method for estimating parameters for the proposed model, we propose a collapsed Gibbs sampling algorithm, which is a type of Markov-chain Monte Carlo method. This paper demonstrates the effectiveness of the proposed method through evaluation testing applied to actual keystroke log data.

# Related Works 

This section describes related works on keystroke data applications.
The most common application of keystroke data is user authentication in the security domain. Many user authentication methods that use keystroke data have been proposed (Karnan et al. 2011; Teh et al. 2013; Quraishi and Bedi 2018). In these methods, users are identified by using supervised classifiers trained on keystroke features. Various statistical and probabilistic models and machine learning methods

have been used for classification (Karnan et al. 2011; Teh et al. 2013; Quraishi and Bedi 2018). Hidden Markov models (HMMs), which are used in this study, have also been used for user authentication (Chen and Chang 2004; Rodrigues et al. 2005; Ali et al. 2016). In HMM-based authentication methods, an HMM is trained for each user from sequences of keystroke timing features such as the durations of key presses and the time elapsed between key presses. User authentication is performed by checking how well a set of keystroke data from an authentication attempt fits the pre-trained HMMs.

Another application of keystroke data is emotion recognition (Epp et al. 2011; Salmeron-Majadas et al. 2018). Emotion-estimation methods classify user emotion by applying a supervised machine learning classifier trained from keystroke features for each emotion class.

As approaches for general pattern recognition tasks including writing-pattern recognition, temporal interval Bayesian networks (Zhang et al. 2013) and a generative probabilistic model with Allen's interval-based relations (Liu et al. 2016, 2018) have recently been proposed. These methods can capture complex temporal relations among the occurrences of observable features (so-called atomic/primitive actions) by using Allen's interval algebra (Allen 1983) and Bayesian networks. Such approaches have been used for classification of sequential data, achieving state-of-the-art accuracy for applications such as classifications of sports videos (Zhang et al. 2013; Liu et al. 2016), human actions (Liu et al. 2018), and facial expression (Wang et al. 2013).

It is important to note that the above-mentioned approaches focus on classification. The approaches are not suitable for our research objective because the purpose of this study is to estimate the hidden processes underlying observable keystroke activities, not to classify the datasets.

For a method focused on estimation of the writing process, Southavilay et al. (2010a) proposed a method for estimating the process of collaborative writing activities by using an HMM. The proposed method collects the versions of a document produced during collaborative writing and estimates changes in semantic meaning for the next two versions according to predefined heuristics (Southavilay et al. 2010b). The process of collaborative writing is then analyzed by an HMM trained on the sequences of semantic meanings. The purpose and approaches are similar to those of our study, but that method does not use keystroke data. Moreover, that study analyzes the writing process by interpreting the parameters of an HMM trained for each collaborative group. In this approach, we cannot compare writing processes among groups because the means of the latent states will differ among the groups. Although this approach might be extendable to writing process analysis for each learner, the interpretation of each process would be infeasible.

# Keystroke Logging System and Log Data 

This study assumes that writing tasks are presented to learners, and that keystroke log data are collected as learners compose their responses. To collect keystroke log data, we developed a keystroke logging system similar to those in previous studies (Deane and Zhang 2015; Leijten and Waes 2013; Salmeron-Majadas et al. 2018). Figure 1

![img-0.jpeg](img-0.jpeg)

Fig. 1 Interface of keystroke logging system (the writing task on the left side is hidden for copyright reasons)
shows the interface of the developed system. The system presents learners with a writing task in the left panel and a text input area in the right panel. The system records information on typed characters, cursor position, and timestamps for each learner input made to the text area using the keyboard or mouse. The time at which learners access the system is recorded as the response start time. Therefore, keystroke log datasets for each learner consist of a sequence of tuples in the format 〈written text, cursor position, timestamp〉, with the number of tuples being the number of keyboard operations plus one. The keystroke logging function is implemented in Javascript and works on our e-testing platform, developed in Java. The system stores obtained keystroke log data in an SQL database.

In this study, we use keystroke log data obtained in this manner to analyze the writing process.

# Feature Extraction 

Previous studies on analyses of keystroke log data analyzed the writing process based on multiple features, such as the number of characters and keystroke interval times as extracted from each learner's keystroke series (Deane and Zhang 2015; Leijten and Waes 2013; Zhang et al. 2016; Chan 2017). As described in "Introduction", previous studies extracted one set of feature values for each learner, and used those features to categorize writing patterns. In contrast, the present study aims to estimate temporal change in the subtasks of each learner. Thus, keystroke log data for each learner must be defined as time-series feature data.

To extract feature sequences, we use a sliding window approach like that widely used for image processing and speech recognition (Leijten and Waes 2013). The sliding window approach extracts features with analytical frame units by building

frames with a small time-width from time-series data. The width of each analytical frame $W$ is called the frame width, and the movement width of adjacent frames $H$ is called the step width. If $H<W$, overlapping of adjacent frames is permitted. Figure 2 shows the sliding window approach.

In this study, we apply the sliding window approach to keystroke log data for each learner. We extract the seven features listed in Table 1 from each analytic frame (those features are designated as writing features). These features are commonly used in similar studies (Deane and Zhang 2015; Leijten and Waes 2013; Zhang et al. 2016).

By extracting these features for each analytical frame, we can define keystroke log data as series data for seven dimensions of writing features. Specifically, letting $X_{i j f} \in \mathbb{R}$ be feature $f \in \mathcal{F}=\{1, \cdots, F=7\}$ for the $j \in \mathcal{J}=\{1, \cdots, J\}$-th analytical frame of learner $i \in \mathcal{I}=\{1, \cdots, I\}$, series data for writing features of learner $i$ are defined as $\boldsymbol{X}_{i}=\left\{\boldsymbol{X}_{i 1}, \cdots, \boldsymbol{X}_{i J}\right\}$ (where $\boldsymbol{X}_{i j}=\left\{X_{i j 1}, \cdots, X_{i j F}\right\}$ ).

We expect that by applying a machine learning method to dataset $\boldsymbol{X}=$ $\left\{\boldsymbol{X}_{1}, \cdots, \boldsymbol{X}_{I}\right\}$, the subtask for each analytical frame of each learner can be estimated. We use an unsupervised machine learning method for this estimation, because it is unclear what subtask types exist within the analytical frame.

# Gaussian Hidden Markov Model-based Writing Process Analysis 

As discussed in "Feature Extraction", data $\boldsymbol{X}_{i}$ are time-series data, and there likely is a dependency of subtasks between adjacent analytical frames. A typical unsupervised classifier for such time-series data is the hidden Markov model (HMM). Especially in the case where observed data have continuous values, as in the present study, GHMM
![img-1.jpeg](img-1.jpeg)

Fig. 2 Feature extraction based on the sliding window approach

Table 1 Writing features


is generally used. The following provides details of GHMM assuming application to our dataset $\boldsymbol{X}$.

GHMM assumes a latent variable $S_{i j} \in \mathcal{S}=\{1, \cdots, S\}$, called the state, for each feature $\boldsymbol{X}_{i j}$. Each state $S_{i j}$ is obtained according to a transition probability that is dependent on the state immediately before $S_{i, j-1}$. Specifically, letting the transition probability from state $s$ to state $s^{\prime}$ be $A_{s s^{\prime}}\left(\right.$ where $\left.0 \leq A_{s s^{\prime}} \leq 1, \sum_{s^{\prime}=1}^{S} A_{s s^{\prime}}=1\right)$ and letting $\boldsymbol{A}_{s}$ be $S$-dimensional multinomial distribution $\left\{A_{s 1}, \cdots, A_{s S}\right\}$, the probability of state $S_{i j}$ being dependent on state $S_{i, j-1}=s$ can be written as $P\left(S_{i j} \mid S_{i, j-1}=\right.$ $\left.s, \boldsymbol{A}_{s}\right)=A_{s, S_{i j}}$. The initial state $S_{i 1}$ is obtained following $p\left(S_{n 1} \mid \boldsymbol{\pi}\right)=\pi_{S_{n 1}}$ in accordance with the initial probabilities, which are defined as the $S$-dimensional multinomial distribution $\boldsymbol{\pi}=\left\{\pi_{1}, \cdots, \pi_{S}\right\}$ (where $\left.0 \leq \pi_{s} \leq 1, \sum_{s=1}^{S} \pi_{s}=1\right)$.

The features for each analytic frame $\boldsymbol{X}_{i j}$ follow a normal distribution dependent on state $S_{i j}$. In this study, given state $S_{i j}=s$, we assume that the $f$-th feature $X_{i j f}$ follows a normal distribution with values of mean $\mu_{s f}$ and variance $\sigma_{s f}^{2}$ : $p\left(X_{i j f} \mid \mu_{s f}, \sigma_{s f}^{2}\right)=N\left(\mu_{s f}, \sigma_{s f}^{2}\right)$. Therefore, the emission probability for features $\boldsymbol{X}_{i j}$ can be obtained from the following equation when state $S_{i j}=s$ :

$$
p\left(\boldsymbol{X}_{i j} \mid S_{i j}=s, \boldsymbol{\mu}, \boldsymbol{\sigma}\right)=\prod_{f=1}^{F} p\left(X_{i j f} \mid \mu_{s f}, \sigma_{s f}^{2}\right)
$$

where $\boldsymbol{\mu}=\left\{\mu_{11}, \cdots, \mu_{S F}\right\}$ and $\boldsymbol{\sigma}=\left\{\sigma_{11}, \cdots, \sigma_{S F}\right\}$.
By applying GHMM under the assumption of latent states for each analytical frame as subtasks, a sequence of subtasks for each learner is expected to be estimated. In this approach, however, a subtask is estimated for each analytical frame, which is defined with a small time-width and which overlaps adjacent multiple frames. Therefore, subtask sequence patterns become significantly large, making it difficult to grasp temporal changes in subtasks for each learner.

# Proposed Model 

To address this issue, this study proposes an expanded GHMM model that incorporates parameters representing temporal change in subtasks for each learner. In this

study, we divided series data for each learner into a small number of time intervals, and incorporated into the GHMM a parameter representing the subtask appearance probability for each time interval for each learner. Specifically, time-series data are divided into $T$ time intervals $\mathcal{T}=\{1, \cdots, T\}$ with a constant time span. We then incorporate a state appearance probability $\phi_{i t s}$ that learner $i$ is in state (subtask) $s$ in time interval $t \in \mathcal{T}$, as shown in Fig. 3. In this figure, $\boldsymbol{\phi}_{i t}$ represents a state appearance distribution of learner $i$ in time interval $t$ that is defined as $S$-dimensional multinomial distribution $\left\{\phi_{i t 1}, \cdots, \phi_{i t S}\right\}$.

In the proposed model, state probabilities for individual analytical frames are assumed to follow the product of the transition probability and the state appearance probability, as

$$
P\left(S_{i j} \mid S_{i, j-1}=s, \boldsymbol{A}_{s}, \boldsymbol{\phi}_{i}\right) \propto A_{s, S_{i j}} \cdot \phi_{i, t_{i j}, S_{i j}}
$$

where $\boldsymbol{\phi}_{i}=\left\{\phi_{i 11} \cdots, \phi_{i T S}\right\}$ and $t_{i j} \in \mathcal{T}$ is the time interval to which data $\boldsymbol{X}_{i j}$ belong.

Similarly, we assume that the initial probability is defined as

$$
P\left(S_{i 1} \mid \boldsymbol{\pi}, \boldsymbol{\phi}_{i}\right) \propto \pi_{S_{i 1}} \cdot \phi_{i, 1, S_{i 1}}
$$

The features are obtained using (1) in the same manner as in GHMM.
In the proposed model, the subtask appearance distribution $\boldsymbol{\phi}_{i t}$ can be estimated in an arbitrary time interval for each learner. Thus, by interpreting temporal change in the distribution, writing pattern trends of each learner can be quantitatively grasped. Furthermore, by measuring differences in the subtask appearance distributions $\boldsymbol{\phi}_{i}$ between learners, using for example the Kullback-Leibler divergence or the Jensen-Shannon divergence, differences in the writing process between learners can be quantitatively evaluated. In addition, categorizing writing processes becomes possible using typical cluster methods with those divergence functions.
![img-2.jpeg](img-2.jpeg)

Fig. 3 State appearance distributions for each time interval

# Parameter Estimation Algorithm 

Representative parameter estimation methods for GHMM are maximum likelihood estimation using the Baum-Welch algorithm and Bayesian estimation using Markov chain Monte Carlo (MCMC) (Bishop 2006). For complex models, Bayesian estimation by MCMC would provide higher accuracy (Bishop 2006; Brooks et al. 2011). This method estimates the posterior distribution of each parameter and uses expected or maximum values as a point estimate for parameters. MCMC approximates posterior distributions via sampling. This study proposes a collapsed Gibbs sampling (CGS) algorithm for the proposed model. CGS has been widely used for learningtopic modeling and HMM as a method to improve the efficiency of MCMC by marginalizing out a part of the parameter set (Griffiths and Steyvers 2004; Griffiths et al. 2004; Paisley and Carin 2009).

CGS repeatedly samples parameter values from the conditional posterior distribution for each parameter, approximating the posterior distribution of parameters using the obtained samples. Conditional posterior distribution is defined as a distribution in which all parameters other than those of interest are given, after marginalizing a specific parameter set from the joint distribution. In this study, we marginalize the initial probability $\boldsymbol{\pi}$, transition probability $\boldsymbol{A}$, and state appearance probability $\boldsymbol{\phi}$, and sample the latent state $\boldsymbol{S}=\left\{S_{11}, \cdots, S_{I L}\right\}$ and emission distribution parameters $\boldsymbol{\xi}=\{\boldsymbol{\mu}, \boldsymbol{\sigma}\}$.

The remainder of this subsection presents the details of this algorithm. Figure 4 shows a graphical representation of the proposed model for the following derivation. In the figure, $\alpha, \beta$, and $\gamma$ represent hyperparameters for the distributions of $\boldsymbol{A}, \boldsymbol{\phi}$, and $\boldsymbol{\pi}$, respectively, while $\mu_{0}, n_{0}, g_{1}$, and $g_{2}$ are hyperparameters for the emission distribution.

## Conditional Posterior Distribution for Sampling State $S_{i j}$ for $j>1$

We first derive the conditional posterior distribution of state $S_{i j}$ for $j>1$.
Letting $\boldsymbol{X}^{\backslash i j}=\boldsymbol{X} \backslash\left\{\boldsymbol{X}_{i j}\right\}$ and $\boldsymbol{S}^{\backslash i j}=\boldsymbol{S} \backslash\left\{S_{i j}\right\}$, the conditional posterior distribution where $S_{i j}=s$ is obtained for $j>1$ can be written as

$$
p\left(S_{i j}=s \mid \boldsymbol{X}_{i j}, \boldsymbol{X}^{\backslash i j}, \boldsymbol{S}^{\backslash i j}, \boldsymbol{\xi}\right) \propto p\left(\boldsymbol{X}_{i j} \mid S_{i j}=s, \boldsymbol{\xi}\right) \cdot p\left(S_{i j}=s \mid \boldsymbol{S}^{\backslash i j}\right)
$$

The first term on the right side of (4) is obtained using (1). Furthermore, by omitting constant terms, the second term can be written as

$$
\begin{aligned}
p\left(S_{i j}=s \mid \boldsymbol{S}^{\backslash i j}\right) & \propto p\left(S_{i j}=s, S_{i, j+1} \mid \boldsymbol{S}^{\backslash i, j, j+1}\right) \\
& \propto p\left(S_{i, j+1} \mid S_{i j}=s, \boldsymbol{S}^{\backslash i, j, j+1}\right) \cdot p\left(S_{i j}=s \mid S_{i, j-1}, \boldsymbol{S}^{\backslash i, j-1, j, j+1}\right)
\end{aligned}
$$

where $\boldsymbol{S}^{\backslash i, j, j+1}=\boldsymbol{S} \backslash\left\{S_{i j}, S_{i, j+1}\right\}$ and $\boldsymbol{S}^{\backslash i, j-1, j, j+1}=\boldsymbol{S} \backslash\left\{S_{i, j-1}, S_{i j}, S_{i, j+1}\right\}$.
If Dirichlet priors with hyperparameters $\alpha$ and $\beta$ are respectively used for the transition probabilities $\mathbf{A}_{\mathbf{s}}$ and the state appearance probabilities $\boldsymbol{\phi}_{i t}$, then by omitting

![img-3.jpeg](img-3.jpeg)

Fig. 4 Graphical representation of time- and learner-dependent GHMM
constant terms, the first term on the right side of (5) can be reorganized as

$$
\begin{aligned}
p\left(S_{i, j+1} \mid S_{i j}=\right. & s, \boldsymbol{S}^{\backslash i, j, j+1} \\
\propto & \int p\left(S_{i, j+1} \mid \boldsymbol{A}_{s}\right) \cdot p\left(\boldsymbol{A}_{s} \mid \boldsymbol{S}^{\backslash i, j, j+1}\right) d \boldsymbol{A}_{s} \\
& \cdot \int p\left(S_{i, j+1} \mid \boldsymbol{\phi}_{i, t_{i, j+1}}\right) \cdot p\left(\boldsymbol{\phi}_{i, t_{i, j+1}} \mid \boldsymbol{S}^{\backslash i, j, j+1}\right) d \boldsymbol{\phi}_{i, t_{i j+1}} \\
= & \frac{n_{s, S_{i, j+1}}^{\backslash i, j, j+1}+\alpha}{\sum_{s^{\prime}=1}^{S}\left(n_{s, s^{\prime}}^{\backslash i, j, j+1}+\alpha\right)}
\end{aligned}
$$

where $n_{s, s^{\prime}}^{\backslash i, j, j+1}$ represents the frequency at which state $s$ transitioned to state $s^{\prime}$ among $\boldsymbol{S}^{\backslash i, j, j+1}$.

The second term on the right side of (5) is similarly rewritten as

$$
\begin{aligned}
p\left(S_{i j}=\right. & s\left|S_{i, j-1}, \boldsymbol{S}^{\backslash i, j-1, j, j+1}\right) \\
& \propto \int p\left(S_{i j}=s \mid \boldsymbol{A}_{S_{i, j-1}}\right) \cdot p\left(\boldsymbol{A}_{S_{i, j-1}} \mid \boldsymbol{S}^{\backslash i, j-1, j, j+1}\right) d \boldsymbol{A}_{S_{i, j-1}} \\
& \cdot \int p\left(S_{i j}=s \mid \boldsymbol{\phi}_{i, t_{i j}}\right) \cdot p\left(\boldsymbol{\phi}_{i, t_{i j}} \mid \boldsymbol{S}^{\backslash i, j-1, j, j+1}\right) d \boldsymbol{\phi}_{i, t_{i j}} \\
& =\frac{n_{S_{i, j-1}, s}^{\backslash i, j-1, j, j+1}+\alpha}{\sum_{s^{\prime}=1}^{S}\left(n_{S_{i, j-1}, s^{\prime}}^{\backslash i, j-1, j, j+1}+\alpha\right)} \cdot \frac{n_{i, t_{i j}, s}^{\backslash i, j-1, j, j+1}+\beta}{\sum_{s^{\prime}=1}^{S}\left(n_{i, t_{i j}, s^{\prime}}^{\backslash i, j-1, j, j+1}+\beta\right)} \\
& \propto\left(n_{S_{i, j-1}, s}^{\backslash i, j-1, j, j+1}+\alpha\right) \cdot\left(n_{i, t_{i j}, s}^{\backslash i, j-1, j, j+1}+\beta\right)
\end{aligned}
$$

In these equations, $n_{s, s^{\prime}}^{\backslash i, j-1, j, j+1}$ represents the appearance frequency at which state $s$ transitioned to state $s^{\prime}$ among $\boldsymbol{S}^{\backslash i, j-1, j, j+1}$. Furthermore, $n_{i, t, s}^{\backslash i, j-1, j, j+1}$ represents the appearance frequency of state $s$ in a state set $\left\{S_{i j} \in \boldsymbol{S}^{\backslash i, j-1, j, j+1} \mid t_{i j}=t\right\}$ for learner $i$.

From the above, the conditional posterior distribution of $S_{i j}$ for $j>1$ can be described as

$$
\begin{aligned}
p\left(S_{i j}=s \mid \boldsymbol{X}_{i j}, \boldsymbol{X}^{\backslash i j}, \boldsymbol{S}^{\backslash i j}, \boldsymbol{\xi}\right) & \\
& \propto\left[\prod_{f=1}^{F} p\left(X_{i j f} \mid \mu_{s f}, \sigma_{s f}^{2}\right)\right] \cdot \frac{n_{s, S_{i, j+1}}^{\backslash i, j, j+1}+\alpha}{\sum_{s^{\prime}=1}^{S}\left(n_{s, s^{\prime}}^{\backslash i, j, j+1}+\alpha\right)} \\
& \cdot\left(n_{S_{i, j-1}, s}^{\backslash i, j-1, j, j+1}+\alpha\right) \cdot\left(n_{i, t_{i j}, s}^{\backslash i, j-1, j, j+1}+\beta\right)
\end{aligned}
$$

# Conditional Posterior Distribution for Sampling Initial States 

The conditional posterior distribution of initial state $S_{i 1}$ can be written as

$$
p\left(S_{i 1}=s \mid \boldsymbol{X}_{i 1}, \boldsymbol{X}^{\backslash i 1}, \boldsymbol{S}^{\backslash i 1}, \boldsymbol{\xi}\right) \propto p\left(\boldsymbol{X}_{i 1} \mid S_{i 1}=s, \boldsymbol{\xi}\right) \cdot p\left(S_{i 1}=s \mid \boldsymbol{S}^{\backslash i 1}\right)
$$

Here, the first term on the right side of (9) is obtained using (1), while the second term can be written as

$$
p\left(S_{i 1}=s \mid \boldsymbol{S}^{\backslash i 1}\right) \propto p\left(S_{i 2} \mid S_{i 1}=s, \boldsymbol{S}^{\backslash i, 1,2}\right) \cdot p\left(S_{i 1}=s \mid \boldsymbol{S}^{\backslash i, 1,2}\right)
$$

The first term on the left side of the above equation is calculable from (6). When the Dirichlet prior with hyperparameter $\gamma$ is used for the initial distribution $\boldsymbol{\pi}$, the second term can be expressed by omitting constant terms as

$$
\begin{aligned}
p\left(S_{i 1}\right. & =s \mid \boldsymbol{S}^{\backslash i, 1,2}\right) \\
& \propto \int p\left(S_{i 1}=s \mid \boldsymbol{\pi}\right) \cdot p\left(\boldsymbol{\pi} \mid \boldsymbol{S}^{\backslash i, 1,2}\right) d \boldsymbol{\pi} \cdot \int p\left(S_{i 1}=s \mid \boldsymbol{\phi}_{i}\right) \cdot p\left(\boldsymbol{\phi}_{i} \mid \boldsymbol{S}^{\backslash i, 1,2}\right) d \boldsymbol{\phi} \\
& =\frac{n_{s}^{\backslash i, 1,2}+\gamma}{\sum_{s^{\prime}=1}^{S}\left(n_{s^{\prime}}^{\backslash i, 1,2}+\gamma\right)} \cdot \frac{n_{i, 1, s}^{\backslash i, 1,2}+\beta}{\sum_{s^{\prime}=1}^{S}\left(n_{i, 1, s^{\prime}}^{\backslash i, 1,2}+\beta\right)} \\
& \propto\left(n_{s}^{\backslash i, 1,2}+\gamma\right) \cdot\left(n_{i, 1, s}^{\backslash i, 1,2}+\beta\right)
\end{aligned}
$$

where $n_{s}^{\backslash i, 1,2}$ represents the appearance frequency of $S_{i 1}$ among $\boldsymbol{S}^{\backslash i, 1,2}$ becoming state $s$, while $n_{i, 1, s}^{\backslash i, 1,2}$ represents the appearance frequency of state $s$ in the state set $\left\{S_{i j} \in \boldsymbol{S}^{\backslash i, 1,2} \mid t_{i j}=1\right\}$ for learner $i$.

Thus, the sampling distribution of $S_{i 1}$ is obtained as

$$
\begin{aligned}
& p\left(S_{i 1}=s \mid \boldsymbol{X}_{i 1}, \boldsymbol{X}^{\backslash i 1}, \boldsymbol{S}^{\backslash i 1}, \boldsymbol{\xi}\right) \\
& \propto\left[\prod_{f=1}^{F} p\left(X_{i j f} \mid \mu_{s f}, \sigma_{s f}^{2}\right)\right] \cdot \frac{n_{s, S_{i 2}}^{\backslash i, 1,2}+\alpha}{\sum_{s^{\prime}=1}^{S}\left(n_{s, s^{\prime}}^{\backslash i, 1,2}+\alpha\right)} \cdot\left(n_{s}^{\backslash i, 1,2}+\gamma\right) \cdot\left(n_{i, 1, s}^{\backslash i, 1,2}+\beta\right)
\end{aligned}
$$

# Conditional Posterior Distribution of Emission Probability Parameters 

The conditional posterior distributions of emission probability parameters $\mu_{s f}$ and $\sigma_{s f}^{2}$ for feature $f$ can be expressed as

$$
\begin{aligned}
p\left(\mu_{s f} \mid \boldsymbol{X}, \boldsymbol{S}, \boldsymbol{\xi}^{\backslash s, f}, \sigma_{s f}^{2}\right) & \propto p\left(\mu_{s f} \mid \boldsymbol{X}_{f}^{s}, \sigma_{s f}^{2}\right) \\
p\left(\sigma_{s f}^{2} \mid \boldsymbol{X}, \boldsymbol{S}, \boldsymbol{\xi}^{\backslash s, f}, \mu_{s f}\right) & \propto p\left(\sigma_{s f}^{2} \mid \boldsymbol{X}_{f}^{s}, \mu_{s f}\right)
\end{aligned}
$$

where $\boldsymbol{\xi}^{\backslash s, f}=\boldsymbol{\xi} \backslash\left\{\mu_{s f}, \sigma_{s f}^{2}\right\}$ and $\boldsymbol{X}_{f}^{s}=\left\{X_{i j f} \in \boldsymbol{X} \mid S_{i j}=s, i \in \mathcal{I}, j \in \mathcal{J}\right\}$. These equations are consistent with the conditional posterior distributions of a typical normal distribution for a sample set $\boldsymbol{X}_{f}^{s}$. The normal distribution $N\left(\mu_{0}, \sigma_{s f}^{2} / n_{0}\right)$ is generally used as the conjugate prior of the mean parameter $\mu_{s f}$, where $\mu_{0}$ and $n_{0}$ are hyperparameters. Concretely, the conditional posterior probability of $\mu_{s f}$ is written as Uto and Ueno (2016) and Fox (2010)

$$
p\left(\mu_{s f} \mid \boldsymbol{X}_{f}^{s}, \sigma_{s f}^{2}\right)=N\left(\frac{n_{0} \mu_{0}+\left|\boldsymbol{X}_{f}^{s}\right| \cdot \hat{X}_{f}^{s}}{n_{0}+\left|\boldsymbol{X}_{f}^{s}\right|}, \frac{\sigma_{s f}^{2}}{n_{0}+\left|\boldsymbol{X}_{f}^{s}\right|}\right)
$$

where $\hat{X}_{f}^{s}=\sum_{x \in \boldsymbol{X}_{f}^{s}} \frac{x}{\left|\boldsymbol{X}_{f}^{s}\right|}$ and $\left|\boldsymbol{X}_{f}^{s}\right|$ indicates the number of data points in $\boldsymbol{X}_{f}^{s}$.
The inverse gamma distribution $I G\left(g_{1} / 2, g_{2} / 2\right)$, a type of conjugate prior, is often used as the prior distribution of normal distribution variance $\sigma_{s f}^{2}$ (Gelman 2006), where $g_{1}$ and $g_{2}$ are hyperparameters and are generally small positive real numbers, such as $g_{1}=g_{2}=0.01$. Specifically, the conditional posterior distribution of variance $\sigma_{s f}^{2}$ can be expressed as Uto and Ueno (2016) and Fox (2010)

$$
p\left(\sigma_{s f}^{2} \mid \boldsymbol{X}_{f}^{s}, \mu_{s f}\right)=I G\left(\frac{g_{1}+\left|\boldsymbol{X}_{f}^{s}\right|}{2}, \frac{\sigma_{0}^{2}}{2}\right)
$$

where

$$
\sigma_{0}=g_{2}+\sum_{x \in \boldsymbol{X}_{f}^{s}}\left(x-\hat{X}_{f}^{s}\right)^{2}+\frac{\left|\boldsymbol{X}_{f}^{s}\right| \cdot n_{0}}{\left|\boldsymbol{X}_{f}^{s}\right|+n_{0}} \cdot\left(\hat{X}_{f}^{s}-\mu_{0}\right)
$$

The algorithm proposed by Tanizaki (2008) is useful for obtaining random samples from an inverse gamma distribution.

## Estimation of Marginalized Parameters

Given the obtained state samples, we can estimate the initial probabilities $\boldsymbol{\pi}$, transition probabilities $\boldsymbol{A}$, and state appearance probabilities $\boldsymbol{\phi}$ as follows:

$$
\begin{aligned}
\pi_{s} & =\frac{n_{s}+\gamma}{\sum_{s^{\prime}=1}^{S}\left(n_{s^{\prime}}+\gamma\right)} \\
A_{s s^{\prime}} & =\frac{n_{s s^{\prime}}+\alpha}{\sum_{s^{\prime}=1}^{S}\left(n_{s s^{\prime}}+\alpha\right)} \\
\phi_{i t s} & =\frac{n_{i t s}+\beta}{\sum_{s^{\prime}=1}^{S}\left(n_{i t s^{\prime}}+\beta\right)}
\end{aligned}
$$

In these equations, $n_{s}$ is the frequency at which initial state $S_{i 1}$ becomes state $s, n_{s s^{\prime}}$ is the frequency at which the state transitioned from $s$ to $s^{\prime}$, and $n_{i t s}$ is the frequency of the state becoming $s$ among a state set with time interval $t$ for learner $i$.

# Algorithm 

CGS of the proposed model repeatedly samples states $\boldsymbol{S}$ and the parameters of the emission probability distribution $\boldsymbol{\xi}=\{\boldsymbol{\mu}, \boldsymbol{\sigma}\}$ according to the equations introduced in the previous subsection. Specifically, (8) is used to sample $\left\{S_{i j} \in \boldsymbol{S} \mid j>1, i \in \mathcal{I}\right\}$, and (12) is used for $\left\{S_{i 1} \in \boldsymbol{S} \mid i \in \mathcal{I}\right\}$. Equations (15) and (16) are used to sample $\boldsymbol{\mu}$ and $\sigma$, respectively. Additionally, in the CGS algorithm, the initial probability $\boldsymbol{\pi}$, transition probability $\boldsymbol{A}$, and state appearance probability $\boldsymbol{\phi}$ are calculated from the obtained state samples using (18), (19), and (20), respectively. Finally, the expected values for the obtained parameters are calculated. Algorithm 1 shows pseudocode for the algorithm. A burn-in period is required to remove the effect of initial values.

Algorithm 1 CGS for the proposed model.
Initialize $S, \mu, \sigma$.
for loop $=1$ to $M$ do
for $i=1$ to $I$ do
Sample $S_{i 1}$ from (12)
for $j=2$ to $J$ do
Sample $S_{i j}$ from (8)
end for
end for
for $f=1$ to $F$ do
for $s=1$ to $S$ do
Sample $\mu_{s f}$ from (15)
Sample $\sigma_{s f}^{2}$ from (16)
end for
end for
if loop $>$ burn-in period then
Calculate $\pi, A$, and $\phi$ using (18),(19),(20)
Store $\pi, A, \phi, \mu$ and $\sigma$
end if
end for
return Average values of $\pi, A, \phi, \mu$ and $\sigma$

## Application and Evaluation

In this section, we evaluate the effectiveness of the proposed model using actual keystroke log data collected using the keystroke logging system introduced in

"Keystroke Logging System and Log Data". In this experiment, we collected actual keystroke log data as follows.

We assigned a writing task to 72 subjects and collected keystroke log data while the subjects composed their responses. The task was a reading-to-write task in which the subjects read a short text and related material, then wrote their opinion. This task required no prior knowledge. The subjects were 37 boys/men and 35 girls/women. The range of ages was 16-23, and the median age was 19 years. Of the subjects, 34 were high school students and 38 were university students. Among the university students, 18 were studying arts/humanities and 20 were studying science of some kind. All subjects had experience using a keyboard to create documents. We provided 45 min to respond, and subjects were not allowed to finish before 45 min had elapsed. The total number of keystroke operations obtained in the experiment was 184,916. The mean and standard deviation of the number of keystroke operations by learners were 2568.28 and 852.53 , respectively. The mean and standard deviation values for the final number of characters by learner were 608.92 and 168.30.

Keystroke log data were transformed to writing feature vectors using the sliding window approach, with frame width $W=30 \mathrm{~s}$ and step width $H=10 \mathrm{~s} . W$ and $H$ are the hyperparameters, as described in "Feature Extraction". $W$ controls the granularity of subtask estimation. A small $W$ value enables the capture of more detailed subtasks, although extremely small values of $W$ increase the number of frames with no or only a few keystroke operations, which makes the subtask estimation unstable. A small $H$ value increases the smoothness of the temporal change in the state appearance probabilities, although overlap among the frames is increased by using a small $H$. Excessive overlap is not desirable because the computational cost increases rapidly with overlap. Based on the above-mentioned factors, $W=30$ and $H=10$ were selected by empirical observation. As a result of this feature extraction, features $\boldsymbol{X}_{i}$ for learner $i$ were obtained as the seven previously described dimensional features at 268 timepoints. In the remainder of this section, we evaluate the proposed model through application to this dataset $\boldsymbol{X}$.

# Model Selection Using Information Criteria 

Writing process analysis using the proposed model depends on the number of states $S$ and the number of time intervals $T$. To select the state number in GHMM, the Akaike information criterion (AIC) (Akaike 1974) and the Bayesian information criterion (BIC) (Schwarz 1978) have been widely used. AIC and BIC assume asymptotic normality of maximum likelihood estimates (Watanabe 2010, 2013). However, GHMM does not satisfy this assumption, so these information criteria are not theoretically appropriate. When MCMC is used, a log-marginal likelihood (log-ML) that does not assume asymptotic normality is approximately calculable (Newton and Raftery 1994). In recent years, various studies have used the log-ML calculated using MCMC for model selection (Uto et al. 2017; Griffiths and Steyvers 2004; Wallach et al. 2009; Taddy 2012; Uto and Ueno 2018). Therefore, in this study, we use the log-ML to select $S$ and $T$. Specifically, we calculate the log-ML while changing the number of states $S=\{2, \cdots, 10\}$ and the number of time intervals $T=\{1, \cdots, 12\}$. Note that $S=1$ is meaningless for writing process analysis because the same writing

process will be estimated for all learners. Thus, $S=1$ was ignored in this experiment. Furthermore, the upper limit values of $S=10$ and $T=12$ were selected because extremely large values make the interpretation of the estimated writing process difficult. We discuss the appropriateness of the upper limit values later, using data for justification. For comparison, we also calculated the log-ML for each state number with GHMM.

Table 2 shows the experimental results, where a larger value for log-ML indicates increased appropriateness of the model. Table 2 shows that the proposed model tends to produce higher values than does the GHMM when the state number increases. This suggests that trends in subtask appearance differ among learners and among time intervals, and that the proposed model represents them appropriately. Here, to confirm the appropriateness of the upper limits for $S$ and $T$, Figs. 5 and 6 show, respectively, the average $\log$-ML for each $S \in\{1, \cdots, 10\}$ and for each $T \in\{1, \cdots, 12\}$. Figure 5 shows that the log-ML values rapidly increase until around $S=7$, and the increase rate is slow for $S>7$. Furthermore, the value with $S=10$ is smaller than that with $S=9$. Figure 6 shows that the log-ML values tend to increase until $T=11$. When $T=12$, however, the value is sharply reduced. These results suggest that the optimal values probably lie within $S=\{2, \cdots, 10\}$ and $T=\{1, \cdots, 12\}$. In these ranges, the proposed model with $S=9$ and $T=10$ had the highest indicator value, so we used those values for $S$ and $T$ in the following experiments.

Table 2 Log-marginal likelihood values for each number of states and time interval


![img-4.jpeg](img-4.jpeg)

Fig. 5 Average $\log$-ML value for each $S$

# States Interpretation 

To analyze the writing patterns of each learner based on the proposed model, we first need to interpret the characteristics of each state. For this interpretation, Table 3 presents the mean and standard deviation parameters of the emission distribution for each feature in each state. Furthermore, for ease of interpretation, Fig. 7 shows the mean feature values for each state, which are normalized so that the maximum is 1 and the minimum is 0 . From these results, the characteristics of each state can be interpreted as follows:

State 1 can be interpreted as a waiting stage, because the number of stops is the highest and there are no addition or subtraction operations.
![img-5.jpeg](img-5.jpeg)

Fig. 6 Average $\log$-ML value for each $T$

Table 3 Mean and standard deviation parameters of emission distributions for each state


States 2, 3, 7, and 9 can be interpreted as formulation stages, because the cursor is at the end of the text, and some number of addition and subtraction operations can be seen. Here, the numbers of bursts, addition operations, and subtraction operations exhibit the following relation: state $7<$ state $3<$ state $9<$ state 2. In other words, these four states can be differentiated by keystroke speed.
![img-6.jpeg](img-6.jpeg)

Fig. 7 Normalized mean values of emission distributions for each state

States $4,5,6$, and 8 can be interpreted as a revision stage, because the cursor positions are relatively toward the beginning of the text, the numbers of characters are relatively high, and there are a certain number of bursts, addition operations, and subtraction operations. A characteristic of state 5 is that the cursor moves often, while characteristics of state 6 are that the cursor is positioned relatively toward the beginning of the text and there are few cursor moves. Moreover, a characteristic of state 4 is that there are extremely few addition and subtraction operations. Conversely, there are many addition and subtraction operations in state 8 . From these analyses, we can interpret state 4 as a revision state involving few edits, state 5 as a revision state involving overall edits, state 6 as a revision state involving edits of specific parts in the beginning and middle parts of the text, and state 8 as a revision state with many edits.

Table 4 summarizes the characteristics based on the above analyses.
It is worth noting that we might be able to evaluate the appropriateness of our state interpretation by comparing the interpretations with the subjects' intentions. Subjects' intentions can be investigated via traditional writing process analysis methods, such as the video playback stimulation method. For this analysis, however, we must create the subtask labels summarized in Table 4 in advance by estimating the proposed model parameters using data from all subjects. Due to our experimental constraints, we could not gather the same subjects after all the data had been collected. The evaluation of appropriateness by comparison with subjects' intentions remains for future work.

# Interpretation of State Appearance Distribution 

This section discusses interpretation of the state appearance distribution for each learner based on the above interpretation of states. To that end, Figs. 8 and 9 show the state appearance distribution $\boldsymbol{\phi}_{i}$ for two learners. The horizontal axes in these figures show the time interval, while vertical axes show the appearance probability of each state. Line types show individual states. The figures lead to the following interpretations of the writing process for each learner.

Writer 1 (Fig. 8) has a high ratio of waiting states in the first time interval, which we interpret as the learner reading the task and planning. As time progresses, the

Table 4 Interpretation of each state


![img-7.jpeg](img-7.jpeg)

Fig. 8 State appearance distribution of learner 1
appearance ratio increases in the order of state 9 (formulation stage with fast writing), state 8 (revision stage with many edits), and state 5 (revision of overall text). The learner returns to the waiting state in later time intervals, suggesting that this learner has an ideal writing process.

In contrast, learner 2 (Fig. 9) shows high appearance ratios for states 3 and 7, representing slow writing formulation stages across all time intervals. The appearance
![img-8.jpeg](img-8.jpeg)

Fig. 9 State appearance distribution of learner 2

ratio of revision states is low. This learner might not have been spending enough time on revisions.

The above analysis shows that the proposed model allows quantitative analysis of temporal changes in subtask appearance patterns for each learner.

# Validity Evaluation of State Appearance Distributions 

This subsection evaluates the validity of subtask appearance distribution estimations by the proposed method.

For this experiment, we randomly selected ten learners from among the subjects. Then we showed a replay of their keystrokes to two experts (evaluators A and B, below). We asked the evaluators to assess the appearance ratio of nine states for each time interval for each learner. However, it might be difficult for humans to directly differentiate between the nine states. Therefore, we first asked the evaluators to assess ratios of waiting, formulation, and revision, which are presented as major divisions for the nine states for individual time intervals of each learner using five categories: 5. appears very often, 4. appears often, 3. appears relatively often, 2. appears somewhat, and 1. does not appear. If revision was scored 2 or higher in this assessment, the range and amount of revision were evaluated as 2. wide or 1. narrow, and 2. large amount or 1. small amount. Furthermore, keystroke speed was scored as 2. fast or 1. slow for all learners.

In this experiment, we calculated subtask distributions for each learner from these evaluation data (hereinafter called the correct distribution). To create the correct distribution, we calculated scores for each subtask subdivision in Table 4, based on each evaluator's assessment data. Concretely, for each time interval for each learner, the scores for the seven subtask subdivisions were calculated as follows:

Waiting: Use the evaluation score for waiting.
Formulation (Fast writing): If input speed is 2. fast, use the evaluation score for formulation. If not, use half of the score.
Formulation (Slow writing): If input speed is 1. slow, use the evaluation score for formulation. If not, use half of the score.
Revision (Many edits): If the number of edits is 2. large amount, use the evaluation score for revision. If not, use half of the score.
Revision (Few edits): If the number of edits is 1. small amount, use the evaluation score for revision. If not, use half of the score.
Revision (Overall edits): When edit range is 2. wide, use the evaluation score for revision. If not, use half of the score.
Revision (Individual edits): When edit range is 1. narrow, use the evaluation score for revision. If not, use half of the score.

The correct distribution was created by normalizing those scores for each evaluator. Note that this experiment did not distinguish between states 2 and 9 or between states 3 and 7, because those pairs are difficult for humans to differentiate.

We evaluated the validity of the proposed model by comparing the correct distribution with state appearance distributions from the proposed model. To evaluate these differences, we used the Jensen-Shannon (JS) divergence, which is widely used to

evaluate differences in probability distributions. The JS divergence is zero when the distributions are completely consistent and increases with increasing differences. To discuss the degree of differences between correct distributions and state appearance distributions from the proposed model, we also calculated JS divergence between the uniform distribution and each distribution. Here, because the correct distribution combined states 2 and 9 and states 3 and 7 as described above, the JS divergence was calculated after the state appearance probabilities for those state pairs were summed.

Table 5 shows the mean and standard deviation for the JS divergence calculated between each distribution. These results demonstrate that the difference between the state appearance distribution from the proposed model and each correct distribution is smaller than differences between the uniform distribution and each correct distribution. We performed paired multiple comparison using the Bonferroni method to evaluate whether significant differences are confirmed for those JS divergence means. Table 6 shows the results. In that table, $A$ (or $B$ ) indicates evaluator A (or B), $X / Y$ refers to the JS divergence between distributions of methods X and Y , and values in each cell are the $p$-value for the mean difference of the JS divergences. For example, the cell in the first row and first column shows the $p$-value of the mean difference between the JS divergences of $A / B$ and those of $A /$ Proposed. The results show that JS divergences between state appearance distributions from the proposed model and the correct distributions as calculated by both evaluators present no significant differences, while those between uniform and correct distributions reveal significant differences.

These results indicate that state appearance distributions from the proposed model have trends similar to the interpretations by the expert evaluators. This suggests that using the proposed model to analyze subtask appearance patterns for each learner is appropriate.

# Analysis of the Relation Between Skills and the Writing Process 

As discussed in "Introduction", the writing process and writing skills are known to be related. Therefore, if analyses of this relation based on the proposed model are consistent with findings from existing studies, the validity of analyses using the proposed model can be confirmed.

For this evaluation, we classified learners with similar processes and analyzed relations between these clusters and writing skills. Specifically, we performed hierarchical clustering using the JS divergence of the state appearance distribution between learners as the distance function. We used the pseudo-F criterion to determine the

Table 5 JS divergence between methods


Table 6 Results of statistical tests


optimum cluster number, and two clusters were supported. Therefore, in this experiment we classified learners into two clusters, with 26 learners in one group and 46 learners in another. Figures 10 and 11 show mean values of state appearance probabilities for learners belonging to each cluster. Those figures show the following characteristics for each cluster.

Writers in cluster 1 wait for a certain amount of time, followed by a fast-writing formulation stage (states 9 and 2) and then, in the latter half, transition to the waiting state with a certain ratio of overall revision (state 5) and minor edits (state 4). This can be considered as a good writing process, because there is good balance between planning, formulation, and revision, and writing is completed with time to spare.

Writers in cluster 2 are relatively slow to start writing, and the start of writing is was followed by slow-writing formulation (states 7 and 3) for a long time, with minor edits (state 4) and edits at specific locations (state 6) conducted just before the end of the writing period. This can be seen as a cluster of learners who formulate slowly and cannot secure sufficient time for revisions.
![img-9.jpeg](img-9.jpeg)

Fig. 10 Average state appearance probabilities of cluster 1

![img-10.jpeg](img-10.jpeg)

Fig. 11 Average state appearance probabilities of cluster 2

Learners who write fast and spend more time performing revisions are generally known to have high writing skills (Sasaki 2000, 2002; Larios et al. 2008). Therefore, if the product quality in cluster 1 is high, analyses based on the proposed model are validated.

To evaluate the quality of writing products, we had two experts score the writing of each learner by two perspectives: 1) organization, and 2) readability. Organization was evaluated using five scores: 1. extremely poor, 2. poor, 3. neither poor nor skilled, 4. skilled, and 5. extremely skilled. Readability was evaluated using four categories: 1. very difficult to read and understand, 2. difficult to read and understand, 3. somewhat difficult to read and understand, and 4. no problem with readability. Evaluators were not informed of which cluster learners belonged to. The average of the scores by the two experts was used as the final score. We conducted the Wilcoxon rank-sum test to examine differences in mean score between clusters for each evaluation point. We also performed the same calculation for the total score of the two evaluation points.

Table 7 shows the results. The experimental result shows that the score for cluster 1 is higher than that for cluster 2 for each evaluation point. In addition, the readability and total scores are significantly different. Here, we also confirmed the

Table 7 Scores for each cluster


Table 8 Scores for each attribute of subjects


relations between the attributes of the subjects and their scores. Concretely, Table 8 shows the averaged total scores (standard deviations) and $p$-values of the Wilcoxon rank-sum test for different genders and different backgrounds. These tests found no significant difference for gender or background. In addition, the correlation between age and total score was 0.17 , with no significance $(p=0.15)$. These results show that the effects of subjects' attributes did not significantly affect the outcome of this experiment.

From the experimental results, we can confirm that the product quality in cluster 1 was higher than that in cluster 2, as expected. This suggests that writing process analyses based on the proposed model derive findings consistent with those of previous studies (e.g., Sasaki 2000, 2002; Larios et al. 2008), suggesting that such analyses are appropriate.

Finally, to show some examples of the writing process of subjects with advanced skills and those with lesser skills, Figs. 12 and 13 depict the state appearance probabilities of the subjects with the top 3 and bottom 3 scores, respectively. Figure 12 shows that high-performing subjects have high ratios of formulation stages (State 2, $3,7,9)$ in the first half of the total writing time. In the second half, the ratios of waiting (State 1) and revision actions (States 4, 5, 6, 8) increase. Although the time allocated to each stage differs among the subjects, they tend to divide the formulation and revision phases consciously. In contrast, Fig. 13 shows that low-performing subjects have a low ratio of waiting (State1) across all time intervals, meaning that they continued to write until just before the end of the writing period. Concretely, the subject shown in the center of Fig. 13 has high ratios of formulation stages (State 3, 7,9 ) overall, and the subjects shown in the left and right of Fig. 13 have high ratios of editing/revision actions (State 4, 5, 6, 8) across all time intervals. These results suggest that the common characteristics of good writers are that (1) the formulation
![img-11.jpeg](img-11.jpeg)

Fig. 12 State appearance probabilities of subjects with top 3 scores

![img-12.jpeg](img-12.jpeg)

Fig. 13 State appearance probabilities of subjects with bottom 3 scores
and revision phases are divided, and (2) time management is practiced. In addition, the figures show that the temporal changes in subtasks differ between the subjects, although good (and bad) writers share roughly similar trends. The interpretation of the detailed temporal changes would help learners and instructors grasp the writing characteristics of each learner quantitatively, as we discussed in "Introduction". Furthermore, such data also provide useful information for instructors to use in providing feedback and instruction based on the writing patterns of each learner.

# Conclusion 

In this study, we proposed a method for machine learning from keystroke log data to estimate temporal change in learners' subtask appearance patterns. Specifically, we defined keystroke log data as series data of writing features, and developed an expanded GHMM model that estimates the subtask appearance distribution from these data. The proposed model considered latent states in GHMM as subtasks, and incorporated parameters that express state appearance probabilities for each time interval for each learner. Furthermore, we proposed a Bayesian estimation method via collapsed Gibbs sampling as a method for estimating parameters for the proposed model.

We used actual data to show that the proposed model produces higher fit than does GHMM. Furthermore, we demonstrated that the writing process of each learner could be quantitatively interpreted based on the state appearance distribution from the proposed model, and that the distribution was valid and similar to interpretations by expert evaluators. We also showed that differences in learner writing processes can be measured based on JS divergence in state appearance distributions, and that clustering of writing processes can be conducted using that measure. We also demonstrated the validity of writing process analysis based on the clustering.

In the future, we would like to examine generalizability of the proposed method through applications to various actual data. We will also examine an extension of the proposed method to deal with reports that writing activity depends on emotion (Epp et al. 2011; Salmeron-Majadas et al. 2018). In the proposed method, the state appearance probabilities for each learner $\boldsymbol{\phi}_{i}$ will reflect the effects of emotion. The effects of emotion and writing characteristics cannot be differentiated, but the effects might be explicitly captured by incorporating emotion parameters. This extension will be

explored in future work. We also aim to develop a writing learning support system that visualizes estimated results as feedback to learners.
Acknowledgements This work was supported by JSPS KAKENHI Grant Numbers 17H04726 and 17K20024. Data collection was performed with the support of the Assessment Research and Development Office, Benesse Educational Research and Development Institute.
