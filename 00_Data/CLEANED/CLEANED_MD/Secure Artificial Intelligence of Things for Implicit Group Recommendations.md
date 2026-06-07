# Secure Artificial Intelligence of Things for Implicit Group Recommendations 

Keping Yu, Member, IEEE, Zhiwei Guo, Member, IEEE, Yu Shen, Wei Wang, Jerry Chun-Wei<br>Lin, Senior Member, IEEE, Takuro Sato, Life Fellow, IEEE


#### Abstract

The emergence of Artificial Intelligence of Things (AIoT) has provided novel insights for many social computing applications such as group recommender systems. As distance among people has been greatly shortened, it has been a more general demand to provide personalized services to groups instead of individuals. In order to capture group-level preference features from individuals, existing methods were mostly established via aggregation and face two aspects of challenges: secure data management workflow is absent, and implicit preference feedbacks is ignored. To tackle current difficulties, this paper proposes secure Artificial Intelligence of Things for implicit Group Recommendations (SAIoT-GR). As for hardware module, a secure IoT structure is developed as the bottom support platform. As for software module, collaborative Bayesian network model and non-cooperative game are can be introduced as algorithms. Such a secure AIoT architecture is able to maximize the advantages of the two modules. In addition, a large number of experiments are carried out to evaluate the performance of the SAIoT-GR in terms of efficiency and robustness.


Index Terms-Secure data analytics, group recommender systems, Bayesian network, non-cooperative game.

## I. INTRODUCTION

THE constant prevalence of the Internet of Things (IoT) makes it possible to construct a world in which all things are interconnected [1]. At the same time, the emergence of artificial intelligence (AI) has also brought novel vitality to multiple fields [2], [3]. The fusion of them yields an innovative conception named Artificial Intelligence of Things

This work was supported in part by the State Language Commission Research Program of China under grant YB135-121, in part by the Science and Technology Research Program of Chongqing Municipal Education Commission under Grant KJQN202000805, in part by the Chongqing Natural Science Foundation of China under grant cstc2019jcyj-msxmX0747, in part by the Japan Society for the Promotion of Science (JSPS) Grants-in-Aid for Scientific Research (KAKENHI) under Grant JP18K18044, and in part by the Key Research Project of Chongqing Technology and Business University under grant ZDPTTD201917 and grant KFJJ2018071. (Corresponding author: Yu Shen)

Keping Yu is with Global Information and Telecommunication Institute, Waseda University, Tokyo 169-8555, Japan (e-mail: keping.yu@aoni.waseda.jp).

Zhiwei Guo is with School of Artificial Intelligence, Chongqing Technology and Business University, Chongqing 400067, China (e-mail: zwguo@ctbu.edu.cn).

Yu Shen is with National Research Base of Intelligent Manufacturing Service, Chongqing Technology and Business University, Chongqing 400067, China (e-mail: shenyu@ctbu.edu.cn).

Wei Wang is with School of Intelligent Systems Engineering, Sun Yat-Sen University, Shenzhen, China. (email: ehomewang@ieee.org)

Jerry Chun-Wei Lin is with the Department of Computer Science, Electrical Engineering and Mathematical Sciences, Western Norway University of Applied Sciences, 5063, Bergen, Norway (e-mail: jerrylin@ieee.org).

Takuro Sato is with Research Institute for Science and Engineering, Waseda University, Tokyo 169-8555, Japan (e-mail: t-sato@waseda.jp).
(AIoT), a potentially promising technology mode in the future [4]. Predictably, the AIoT may be adopted to improve many ordinary industrial or commercial applications [5], in which the recommender systems (RSs) acts as a most typical one [6], [7]. In the context of IoT, the continuous development of communication quality has substantially boosted information transmission and exchange, yet also leading to remarkable information overload issue [8]. Especially in the era of upcoming 5G, such problem is likely to become more prominent in terms of IoT environment [9], [37]. Nowadays, the RSs have been regarded as effective tools to deal with such issue, and have gained considerable attention for some years [12]. The RSs managed to provide personalized services to users, so that suitable items that satisfy their preferences can be suggested to them [38]. But existing RSs were mostly developed towards individual users [14]. But due to many conveniences brought by information techniques, more and more social activities tend to be arranged in the form of groups. As a result, recommending items to groups instead of individuals has also become a meaningful demand, yielding the application of group recommender systems (GRSs).

Despite great progress has been obtained with respect to GRSs [15]-[31], two aspects of challenges are still faced. For one thing, They were generally constructed with the use of offline data, and lacked the ability to be adaptive to changeable situations in real time. This is because the online sample training highly depends on the reliable management of security guarantee and data integration. In fact, real-time online management for data integration and security guarantee is important under IoT environment that is filled with time-varying characteristics. For another, existing GRSs were developed by investigating how to effectively aggregate members into a group. However, almost all of these methods just considered explicit preference feedbacks and failed to handle the scenarios of implicit preference feedbacks. The explicit feedbacks refer to those that are able to directly reflect preference degree towards items, such as ratings. In contrast, the implicit feedbacks refer to interactions between users and items such as click records and purchase records, so that preference degree is indirectly expressed. Undoubtedly, the explicit ones are much more intuitive and favourable for knowledge discovery. But data with the form of implicit feedbacks is quite common in real-world scenarios, as it usually remains difficult to acquire ideal data samples.

The aforementioned challenges can be tackled by designing a secure AIoT architecture that contains two parts: hardware module and software module two parts. As for the hardware

![img-0.jpeg](img-0.jpeg)

Fig. 1: Architecture for platform framework of the SAIoT-GR.

module, an IoT structure is developed as the bottom support platform. Its strong ability of data management and security guarantee will contribute a lot to the software module that is embedded into the hard module so that models for group recommendations can be re-optimized online. As for the software module, the collaborative Bayesian network (CBN) model can be introduced to simultaneously infer unknown preference features hidden inside implicit feedbacks. In other words, implicit feedbacks can be transformed into explicit ones through joint probabilistic inference. And then non-cooperative game theory can be utilized to search for optimal results for all the group members. Thus, this paper proposes Secure Artificial Intelligence of Things for Group Recommendations, which is named SAIoT-GR for short. The fusion of secure IoT bottom framework and AI algorithms is able to maximize their own advantages of the two modules, and improves recommendation efficiency to the most extent. This work firstly considers formulating online data management mechanism to establish an efficient GRS. In addition, it also firstly investigates the group recommendation problem from the perspective of implicit feedback. Major highlights of this paper are summed up as:

- It is recognized that existing researches concerning GRSs still face two aspects of challenges. One is absence of real-time online management, and the other is ignorance of situations of implicit feedbacks.
- SAIoT-GR, composed of two main modules, is proposed to solve the above two aspects of challenges, respectively. It well fuses a secure IoT framework and AI algorithms.
- Enough experiments on real-world datasets are carried out to prove efficiency of the proposed SAIoT-GR.

Except introduction, this paper contains four main sections. Section II, entitled system model, gives macroscopic design for both IoT architecture and the embedded recommendation model. Among, the microscopic workflow of the recommen-
dation algorithm is described in Section III. The Section IV presents a series of experiments which evaluate performance of the proposed SAIoT-GR. In Section V, the paper is concluded.

## II. SYSTEM MODEL

This research manages to put forward SAIoT-GR to build up a novel GRS under the situations of implicit feedbacks. This section firstly describes platform framework of the designed SAIoT-GR, and then describes the specifically developed CBN model that is embedded into the platform.

## A. Hardware Architecture

Architecture of the designed SAIoT is illustrated in Fig. 1, which is actually the combination of a secure IoT platform and an embedded AI algorithm. From the view of structural composition, it is composed of two main modules: hardware module and software module. The former mainly refers to the IoT bottom framework that offers data integration, and is endowed with a four-layer working structure: data layer, security layer, processing layer and application layer. Among, the processing layer directly implements group recommendations by carrying the software module which is exactly the developed AI algorithm CBN model. All parts of SAIoT-GR work jointly to constitute the newly proposed GRS. Three main modules are described as the following contents:

- The data layer collects the original data and connecting them to the SAIoT-GR. It contains several types of entities: user profiles, item attributes, business records, and group information. And all types of data related to group recommendations can be acquired and updated in real-time under the environment of IoT.
- The security layer is mainly responsible for some physical security management of source data. Firstly, it provides links to transmit data from the data layer to the following

![img-1.jpeg](img-1.jpeg)

Fig. 2: Algorithmic workflow of the SAIoT-GR.

working layers. Secondly, it put forward unified authentication mechanisms for multi-source heterogeneous data to ensure online information security. Thirdly, it gives distributed storage space for source data.

- The processing layer mainly implements the two-stage AI algorithm that is embedded into SAIoT-GR. For one thing, it employs the CBN model to model the generative process of interaction results between users and items, so that collaborative inference of unknown preference feedbacks can be realized. For another, a non-cooperative game is adopted to output recommendation results for groups of users to satisfy their interests.

### *B. Workflow of SAIoT-GR*

Enumerating *i* from 1 to |*G*| and *j* from 1 to *Q*, *u<sub>i</sub>* denotes user set of group *G* and *v<sub>j</sub>* denotes the item set. When user *u<sub>i</sub>* selects or consumes item *v<sub>j</sub>*, there exists an interaction record *B(i, j)* between them. Hence, *u<sub>i</sub>*, *v<sub>j</sub>* and *B(i, j)* are actually the initial training data. To better classify contents of different items, each item is assigned a topic indicator *g<sub>j</sub>* = *d*, where *d* ranges from 1 to *D*. It should be noted that the topics here never have specific meanings and are latent forms. The main task of this work is to select appropriate items from another candidate item set, so that demand of most users can be satisfied. The demand of user *u<sub>i</sub>* towards item *v<sub>j</sub>* is determined by two aspects of factors: inherent interest and social influence. The former is defined as the initial preference feedback of users towards items, not being influenced by social factors. The latter is defined as the influence brought by social friends and independent from inherent interest.

Algorithmic workflow of the SAIoT-GR is demonstrated in Fig. 2, which contains two main components: collaborative inference module and recommendation module. The former models forward decision processes of users as CBN model and infers preference features via Gibbs sampling. The latter models the generation of recommendation results as the non-cooperative game among group members, and calculates results that maximizes utility of whole groups. Before them, the prevalent short text classification algorithm Twitter-LDA is utilized to endow each item with a topic indicator to each item based upon associated textual contents.

### III. METHODOLOGY

#### *A. Collaborative Bayesian Network*

*B(i, j)*, the interaction record between user *u<sub>i</sub>* and item *v<sub>j</sub>*, is mainly determined by four aspects of factors:

- *g<sub>j</sub>*, the topic indicator of the item;
- *I(i, d)*, inherent interest of user *u<sub>i</sub>* about topic *d*;
- *π(i, d)*, contribution rate of topic *d* towards user *u<sub>i</sub>*;
- *S(i, d)*, social influence of user *u<sub>i</sub>* about item *d*.

It is assumed that inherent interest *I(k, i)* is drawn from the first Gaussian distribution *I(k, i)* ∼ *Gau*(μ<sub>1</sub>, σ<sub>2</sub><sup>2</sup>), where μ<sub>1</sub> is mean and σ<sub>2</sub><sup>2</sup> is variance. Similarly, it is also assumed that social confidence *S(k, i)* is drawn from another Gaussian distribution *S(k, i)* ∼ *Gau*(μ<sub>2</sub>, σ<sub>2</sub><sup>2</sup>), where μ<sub>2</sub> is mean and σ<sub>2</sub><sup>2</sup> is variance. Selection result of user *u<sub>i</sub>* on item *v<sub>j</sub>* is denoted as:

$$
B(i, j) = \begin{cases}
1, & \text{selection} \\
0, & \text{no selection}
\end{cases} \tag{1}
$$

For scenes where *B(i, j)* = 1, their generative processes can be deduced as conditional probability with the use of logistic function:

$$
\begin{aligned}
\mathcal{P}[B(i, j) &= 1 | g_j = d, \pi(i, d), I(i, d), S(i, d)] \\
&= \frac{1}{1 + \exp[-\pi(i, d) \cdot I(i, d) - S(i, d)]} \tag{2}
\end{aligned} \tag{2}
$$

where π(*i, d*) acts as the aforementioned contribution rate between topic *d* and user *u<sub>i</sub>*. It is calculated as:

$$
\pi(i, d) = \frac{m_i^{(d)}}{m_i} \tag{3}
$$

where *m<sub>i</sub>* is the amount of interactions of user *u<sub>i</sub>*, and *m<sub>i</sub><sup>(d)</sup>* is the number of his interactions related to topic *d*. For scenes where *d<sub>j,i</sub>* = 0, generative process is expressed as:

$$
\begin{aligned}
\mathcal{P}[B(i, j) &= 0 | g_j = d, \pi(i, d), I(i, d), S(i, d)] \\
&= 1 - \frac{1}{1 + \exp[-\pi(i, d) \cdot I(i, d) - S(i, d)]} \tag{4}
\end{aligned} \tag{4}
$$

Joint probability of all the generative processes is expressed as:

$$
\begin{aligned}
& \mathcal{P}[B(i, j) \mid g_{j}=d, \pi(i, d), I(i, d), S(i, d)] \\
= & \left\{\frac{1}{1+\exp [-\pi(i, d) \cdot I(i, d)-S(i, d)]}\right\}^{\delta\left(d_{j, i}, 1\right)} \\
& \cdot\left\{1-\frac{1}{1+\exp [-\pi(i, d) \cdot I(i, d)-S(i, d)]}\right\}^{\left[1-\delta\left(d_{j, i}, 1\right)\right]}
\end{aligned}
$$

where $\delta(a, b)$ is Kronecker delta represented as:

$$
\delta(a, b)= \begin{cases}1, & a=b \\ 0, & a \neq b\end{cases}
$$

Therefore, given the topic indicator $k$ and prior distributions, the following formula can be deduced:

$$
\begin{aligned}
& \mathcal{P}\left[B(i, j), \pi(i, d), I(i, d), S(i, d) \mid g_{j}=d, \mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}\right] \\
= & \mathcal{P}\left[I(i, d) \mid \mu_{1}, \sigma_{1}^{2}\right] \cdot \mathcal{P}\left[S(i, d) \mid \mu_{2}, \sigma_{2}^{2}\right] \\
& \cdot \mathcal{P}\left[B(i, j) \mid g_{j}=d, \pi(i, d), I(i, d), S(i, d)\right]
\end{aligned}
$$

Based on the above formula, learning goal for interactions can be summarized as searching for minimization of the following objective function:

$$
J_{j, i}=-\log \mathcal{P}\left(d_{j, i}, \pi_{k, i}, I_{k, i}, S_{k, i} \mid z_{j}=k, \mu_{1}, \mu_{2}, \sigma_{1}^{2}, \sigma_{2}^{2}\right)
$$

Integrating the above two formulas leads to a new objective function:

$$
\begin{aligned}
J_{j, i}= & -\log \mathcal{P}\left[I(i, d) \mid \mu_{1}, \sigma_{1}^{2}\right]-\log \mathcal{P}\left[S(i, d) \mid \mu_{2}, \sigma_{2}^{2}\right] \\
& -\log \mathcal{P}\left[B(i, j) \mid g_{j}=d, \pi(i, d), I(i, d), S(i, d)\right]
\end{aligned}
$$

And the formula can be rewritten as:

$$
\begin{aligned}
J_{j, i} \propto & -\log \mathcal{P}\left[B(i, j) \mid g_{j}=d, \pi(i, d), I(i, d), S(i, d)\right] \\
& -\frac{\left[I(i, d)-\mu_{1}\right]^{2}}{2 \sigma_{1}^{2}}-\frac{\left[S(i, d)-\mu_{2}\right]^{2}}{2 \sigma_{2}^{2}}
\end{aligned}
$$

The unknown variables $I(i, d)$ and $S(i, d)$ can be inferred through stochastic gradient descent method.

To solve the learning objective established above, the most ordinary optimization approach named stochastic gradient descent (SGD) is adopted here. Finally, the obtained process variables are two vectors as the following forms:

$$
\begin{aligned}
& I(i, d)=\left[I(i, 1), I(i, 2), \cdots, I(i, D)\right]\left|{ }_{i \in[1,|G|]}\right. \\
& S(i, d)=\left.[S(i, 1), S(i, 2), \cdots, S(i, D)]\right|_{i \in[1,|G|]}
\end{aligned}
$$

## B. Recommendation

When making group recommendations, intuitively, it is expected to analyze the cooperation relations and competition intention of group members. And naturally, recommendation results to a group need to be item sets rather than single items. Thus, the idea of non-cooperative game is introduced here to allocate recommended item sets to the whole group. When the equilibrium state is reached, corresponding item sets can be viewed as the optimal allocation for the whole group.


Fig. 3: Architecture for platform framework of the SAIoT-GR.

As for the construction of game process, three elements are included: player set, strategy set and utility set. Generalized to a group $G$, all of its members are regarded to take part in the game process. Therefore, all of its members are actually players of the game. In other words, the player set is the set of group members whose size is $|G|$. During the game process, each player will be asked to select one topic indicator as his strategy $t_{i}$. The strategies of all the group members constitute the strategy set. The size of strategy set is $|G|$. It is assumed that there exists a utility value $H_{i}$ for user $u_{i}$ to benefit from his selected strategy. Similarly, the size of utility set also equals to $|G|$.

In order to unify the range of all the utility values in the utility set, it is supposed to normalized all the $I(i, d)$ and $S(i, d)$ into values with range $[0,1]$. Let $I_{N}(i, d)$ and $S_{N}(i, d)$ denote transformed forms of $I(i, d)$ and $S(i, d)$. Given this, the final profit of user $u_{i}$ can be computed as:

$$
X_{i}=\frac{E X P\left[s_{i} \cdot I_{N}(i, d)\right]}{\operatorname{Count}\left(s_{i}\right)}
$$

where $E X P(\cdot)$ denotes the expectation operator, and $\operatorname{Count}\left(s_{i}\right)$ counts the number of players whose strategies are $s_{i}$. At the same time, the cost of user $u_{i}$ born from $s_{i}$ is represented as:

$$
M_{i}=\eta_{1} \cdot\left[S_{N}(i, d)+1-I_{N}(i, d)\right]^{n}
$$

where $n$ is a model parameter. Offset by cost, utility finally acquired by $u_{i}$ is computed as:

$$
H_{i}=\eta_{2} \cdot\left(X_{i}-M_{i}\right)
$$

where $\eta_{1}$ and $\eta_{2}$ are trade-off parameters.
Let $\Omega^{*}=\left\{s_{1}^{*}, s_{2}^{*}, \cdots, s_{|G|}^{*}\right\}$ denote the strategy set under the status where Nash equilibrium is reached. From the perspective of game theory, all of the players cannot obtain larger utility by changing their strategies. At such state, the following condition can be satisfied:

$$
H_{i}\left(s_{i}^{*}, s_{-i}^{*}\right) \leq H_{i}\left(s_{i}, s_{-i}^{*}\right)
$$

where $s_{-i}$ denotes strategy set from players except player $u_{i}$, and $s_{-i}^{*}$ denotes denotes such strategy set under status of Nash equilibrium. When all the elements of $\Omega^{*}$ are inferred, the contents that are recommended to group $G$ are denoted as:

$$
R_{G}=\left\{A_{1}, A_{2}, \cdots, A_{K}\right\}
$$

where $A_{k}$ is the ratio of items with topic indicator $k$. In stead of specific items, recommendation results here take the form of ratios of each topic indicator.

## IV. EXPERIMENTS AND ANALYSIS

## A. Datasets

The performance of recommender systems is generally evaluated on benchmark datasets. However, specific datasets for situations of group recommendations are not publicly available since now. Relevant researches universally artificially constructed experimental datasets from those for situations of individual recommendations. Here, two prevalent datasets that are commonly used for individual recommendations, are selected for this purpose. As for group construction, it is expected to randomly select some users to constitute some groups according to group size. Their statistical values can be found in Fig. 3, and they are briefly described as:

1) Last.fm dataset: Last.fm ${ }^{1}$ is an online music community with online social function, in which users can join social communities and tag things they are interested in. The dataset was collected by the team of Millennium song dataset through APIs provided by the website.
2) Delicious dataset: Delicious ${ }^{2}$ is the largest bookmark sharing community of the Internet and also an online social platform. Similar to Last.fm, users are allowed to release tags and participate social communities. And the dataset is also a part of the Millennium song dataset.

To reduce the effect brought by data sparsity, inactive users with their interaction records inside the two datasets are required to be filtered out, especially the users whose number of interactions is small. Besides, some social density is also required to ensure the richness of data. It is assumed that the minimum social density inside a group must not be below 0.25 . The social density is calculated as $\left(2 E_{G}\right) /(|G| \cdot|G-1|)$, where $E_{G}$ is the number of social relations that can be observed in group $G$.

## B. Experimental Settings

All the experiments can be divided into two parts: efficiency assessment and stability assessment. The former part measures precision of recommendation results by comparing predicted results with real ones. For the latter, a combination of parameters are changed into multiple groups to measure robustness of the SAIoT-GR. Specifically, recommendation precision is determined by the distance between real proportion distributions of topics and predicted ones. To measure such distance, six different distances are selected as metrics: Euclidean distance (EucDist), Manhattan distance (ManDist), Chebyshev distance (CheDist), Correlation distance (CorDist), mean absolute error (MAEDist), and Mean-square error (MSEDist). The detailed definitions of the six distances can be found in one of our previously published work [36].

And five implicit feedbacks-based recommendation methods are selected as baselines, and are briefly introduced as follows:

[^0]1) Frequency: It measures the preference features of group members by counting the frequency of different topics. And preferences of members are aggregated into group preferences.
2) ConfiMF: The preference confidence is regarded as explicit preference feedback score which can be calculated through interaction frequency. Then, group preference feedback is obtained through preference aggregation [33].
3) ContextMF: It is assumed that decision process of a user towards an item depends on two contextual information: user context and item context [34].
4) RanGroup: It is a graph theory-based group recommender system and produces recommendation results through idea of random work [35].
5) FreGroup: It is a self-defined recommendation method that aggregates interactions of members into interactions of groups. The, the Frequency method is utilized to generate recommendation results for groups of users.

And some key parameters are required to be specially set with respect to two datasets. For the Last.fm dataset, mean values of two Gaussian distributions are set to 45 and 12 separately, variance values of two Gaussian distributions are set to 70 and 30 separately. For the Delicious dataset, two mean values are set to 45 and 10 separately, and two variance values are set to 75 and 25 separately. Learning rate and the convergence threshold of SAIoT-GR in experiments are set to 0.01 and 0.001 , respectively. In the game process used for generating, two trade-off parameters $\eta_{1}$ and $\eta_{2}$ in Eq. (14) and (15), are set to 0.6 and 0.4 . And for the proportion of training data, it is set to $70 \%$ by default and can be changed during experimental processes. The total number of topic indicators in Last.fm and Delicious is set to 6 and 10, respectively.

## C. Results and Analysis

Comparisons between predicted topic distributions and real ones on the Last.fm dataset and the Delicious dataset, are visualized on Fig. 4 and Fig. 5, separately. Naturally, the total number of topic indicators on two datasets equals to 6 and 10. The Fig. 4 and Fig. 5 are both made up of six subfigures, in which each one corresponds to an experimental method. In six subfigures of Fig. 4, the curves in red color denote real values of topic distributions ranging from topic 1 to topic 6 , and the curves in blue color denote predicted values of topic distributions ranging from topic 1 to topic 6 . In six subfigures of Fig. 5, the curves in green color denote real values of topic distributions ranging from topic 1 to topic 6 , and the curves in pink color denote predicted values of topic distributions ranging from topic 1 to topic 6 . It is revealed that distance measurement in terms of SAIoT-GR is the smallest inside all the six methods. This reflects the fact that performance of the SAIoT-GR is superior to ConfiMF and Frequency. The ConfiMF is a popularity-based method that investigates preference features from the perspective of statistics, yet ignores complex group-level features inside social networks. But these subfigures are not able to reveal the comparisions between SAIoT-GR and the other several methods. Thus the metrics are quantified to further compare performance of SAIoT-GR and others.


[^0]:    ${ }^{1}$ https://www.last.fm/
    ${ }^{2}$ https://www.delicious.com

![img-2.jpeg](img-2.jpeg)

Fig. 4: Comparison between predicted topic distributions and real ones on the Last.fm.

TABLE I and TABLE II illustrate specific values of six obtained evaluation metrics as experimental results. They both have six columns that correspond to six distance measurement, as well as six lines that correspond to six experimental methods. Overall, the proposed SAIoT-GR is about 4% better than RandGroup, 6% better than FreGroup, 7% better than ContextMF, 12% better than ConfiMF and 15% better than Frequency. Although social information and contextual information are also considered in ContextMF and RandGroup, the two methods never deeply mining influential factors as the SAIoT-GR. Differently, the SAIoT-GR tries to fuse information come from multiple sources, and forms strong feature extraction for the level of groups. At the same time, it can be also observed that SAIoT-GR cannot acquire the best experimental results all the time, such as results of Chebyshev distance on Last.fm dataset. Two possible reasons can be speculated to explain this phenomenon. On the one hand, some difference exists among computational methods of different distance measurement criteria, so that it is difficult to guarantee that similar results can be obtained by diverse criteria. On the other hand, SAIoT-GR is an unsupervised learning method, which may bring about some uncertainty.

During previous experiments, prior parameters µ<sup>1</sup>, σ<sup>2</sup><sub>1</sub>, µ<sup>2</sup> and σ<sup>2</sup><sub>2</sub> were set up empirically. As some unsupervised

![img-3.jpeg](img-3.jpeg)

Fig. 5: Comparison between predicted topic distributions and real ones on the Delicious.

Methods are susceptible to initial value settings, an additional group of experiments are conducted to testify stability for the proposed SAIoT-GR. It should be noted that this group of experiments set no comparisons between object method and baseline methods, just performance of SAIoT-GR is singly evaluated. It is not required to use all of the six distances in this group of experiments, and just the most typical Euclidean distance is employed. Fig. 6 and Fig. 7 illustrate the results of parameter sensitivity testing on two datasets. Inside these figures, most of the areas are in color of blue, and no sharp change of colors is reflected. It can be concluded from this group of experiments that the SAIoT-GR is not only stable, but also robust.

## V. CONCLUSION

Nowadays, recommender systems oriented to groups rather than individuals have received wide attention in academia. Existing technical approaches mostly utilized explicit feedbacks to develop GRSs. However, situations about implicit feedbacks which are common in the real-world are not well considered. Besides, the absence of online data management also acts as an obstacle to improve recommendation performance. To this end, this paper proposes SAIoT-GR, a CBN-based AIoT, to carry out group recommendations. As for the hardware module, an

TABLE I: Comparisons between SAIoT-GR and baselines with respect to six distances (Last.fm dataset).


TABLE II: Comparisons between SAIoT-GR and baselines with respect to six distances (Delicious dataset).


![img-4.jpeg](img-4.jpeg)

Fig. 6: Stability results of SAIoT-GR on Last.fm dataset.
exclusive IoT structure is developed as the bottom support platform. As for the software module, CBN model and noncooperative game are can be introduced as algorithms. Such an AIoT architecture is able to maximize the advantages of the two modules. In addition, a large number of experiments are carried out to evaluate the performance of the SAIoT-GR in terms of efficiency and robustness. In the future, we are going to extend our SAIoT-GR to more complex scenarios,
where the group's preferences are not clear given the not enough explicit ratings or implicit feedback. Anoloty to coldstart users, such groups can be named as the cold-start groups. This is a also long-standing challenge in conventional RSs. We find a promising solution in [36], [37], [38], which incorporates conversational interactions in RSs and demonstrates its efficiency and explainability over state-of-the-art methods. We hope that our SAIoT-GR will be able to make an explainable

![img-5.jpeg](img-5.jpeg)
(a) $\mu_{1}$ and $\sigma_{1}^{2}$
![img-6.jpeg](img-6.jpeg)
(b) $\mu_{2}$ and $\sigma_{2}^{2}$

Fig. 7: Stability results of SAIoT-GR on Delicious dataset.
recommendations for cold-start groups by using conversational recommender strategies.
