# scientific reports 

## OPEN A probability prediction method for the classification of surrounding rock quality of tunnels with incomplete data using Bayesian networks

Junjie Ma ${ }^{1,2}$, Tianbin Li ${ }^{1,2,2}$, Xiang Li ${ }^{1,2}$, Shuanglong Zhou ${ }^{1,2}$, Chunchi Ma ${ }^{1,2}$, Daqiang Wei ${ }^{1,2}$ \& Kunkun Dai ${ }^{1,2}$

The classification of surrounding rock quality is critical for the dynamic construction and design of tunnels. However, obtaining complete parameters for predicting the surrounding rock grades is always challenging in complex tunnel geological environment. In this study, a new method based on Bayesian networks is proposed to predict the probability for the classification of surrounding rock quality of tunnel with incomplete data. A database is collected with 286 cases in 10 tunnels, involving nine parameters: rock hardness, weathering degree, rock mass integrity, rock mass structure, structural plane integrity, in-situ stress, groundwater, rock basic quality, and surrounding rock level. Moreover, the Bayesian network structure is built using the collected database and quantitatively verified by strength analysis. Then, the accuracy, precision, recall, F-measure and receiver operating characteristic (ROC) curves are utilized for model evaluation. The average values of accuracy, precision, recall, F-measure, and area under the curve (AUC) are approximately $89.2 \%, 91 \%, 92 \%$, $91 \%$, and 0.98 , respectively. These results indicate that the established classification model has high accuracy, even with small sample size and imbalanced samples. Ten additional sets of tunnel cases (incomplete data) are also used for verification. The results reveal that compared with the traditional Q-system (Q) and rock mass rating (RMR) classification methods, the proposed classification model has the lowest error rate and is capable of using incomplete data to predict sample results. Finally, sensitivity analysis suggests that the rock hardness and rock mass integrity have the strongest impact on the quality of tunnel surrounding rock. Overall, the findings of this study can serve as a useful reference for future rock mass quality evaluation in tunnels, underground powerhouses, slopes, etc.

## List of symbols

$R_{c} \quad$ Saturated uniaxial compressive strength
$k_{c} \quad$ Wave velocity ratio
$k_{f} \quad$ Weathering coefficient of rock
$K_{v} \quad$ Rock mass integrity coefficient
$V_{p m} \quad$ Elastic longitudinal wave velocity of rock mass
$V_{p r} \quad$ Elastic longitudinal wave velocity of rock (block)
$J_{v} \quad$ Volume joint number of rock mass
$\sigma_{\max } \quad$ Maximum initial stress perpendicular to the hole axis
$p \quad$ Water pressure of surrounding rock fissures
$q \quad$ Water output per 10 m hole length
W Weathering degree
$D \quad$ Structural plane integrity
$S \quad$ Rock mass structure

[^0]
[^0]:    ${ }^{1}$ College of Environment and Civil Engineering, Chengdu University of Technology, Chengdu 610059, China. ${ }^{2}$ State Key Laboratory of Geohazard Prevention and Geoenvironment Protection, Chengdu University of Technology, Chengdu 610059, China. ${ }^{22}$ email: ltb@cdut.edu.cn


Rock mass classification is widely used for assessing rock quality and performance based on the inherent structural parameters. According to the nature and requirements of engineering applications, the mechanical and geological properties of the rock mass are comprehensively considered in the classification of its quality ${ }^{1}$. In tunnel engineering, this process is called the classification of tunnel surrounding rock quality, which is one of the most important methods to evaluate the stability of surrounding rocks of tunnels, and it also plays a crucial role in the optimization of tunnel construction plan and design parameters. Since the 1920s, rock mass quality classification has received considerable research attention, and numerous classification methods have been proposed ${ }^{2-9}$. Table 1 lists several internationally recognized classification methods. Since the twenty-first century has witnessed a rapid development of underground engineering, especially the construction of a large number of deep-buried and ultra-long tunnels, the challenges encountered in the classification of tunnel surrounding rock quality must be urgently resolved. Therefore, it is necessary to further test the applicability of commonly used methods in tunnel construction and to develop new interdisciplinary methods for predicting the quality of surrounding rocks in tunnels and other underground projects.

The predictive classification of tunnel surrounding rock quality can be divided into long-term and short-term prediction. The long-term prediction aims to assess the quality of surrounding rock in the initial tunnel design stage and provide a reference for the preliminary design of tunnel ${ }^{14}$. It is generally used to provide a preliminary assessment of the basic quality $(B Q)$ of rock mass based on its strength and integrity. The short-term prediction aims to evaluate the quality of surrounding rock in real-time based on various geological information revealed by tunnel excavation, which can serve as a reference for the dynamic design of tunnel support ${ }^{14}$. This study focuses on short-term classification prediction of tunnel surrounding rock quality, and it also utilizes long-term prediction.

Artificial intelligence (AI) was proposed at the Dartmouth Conference in 1956. Since then, it has been widely used in civil engineering applications, such as the prediction of pile bearing capacities ${ }^{15}$, peak particle velocity ${ }^{16}$, tunnel boring machine (TBM) penetration rate ${ }^{17}$, safety factor ${ }^{18}$, rock tensile strength ${ }^{19}$, Schmidt hammer rebound numbers ${ }^{20}$, and compressive strength of mortars ${ }^{21}$. Further, different AI algorithms have been employed for the prediction of rock mass classification, such as fuzzy mathematics ${ }^{22,23}$, neural networks ${ }^{24,25}$, support vector machines ${ }^{26,27}$, and random forest ${ }^{28}$. However, most of the existing intelligent rock mass classification methods focus on the construction stage (short-term prediction of rock mass quality), while the design stage is often ignored (long-term prediction of rock mass quality). More importantly, these existing methods require complete rock mass parameters to predict the rock mass quality. Due to the complex geological environment at the tunnel construction site, it is difficult to obtain the complete surrounding rock parameters. Therefore, it is imperative to further verify the applicability of the existing intelligent classification methods for surrounding rock quality.

The main problem in using the existing methods to predict the quality of tunnel surrounding rock is the difficulty in obtaining the indicators and missing data. Further, the geological information revealed by underground engineering excavation has great uncertainty. To solve this problem, Bayesian networks (BNs) have been introduced in intelligent surrounding rock classification (SRC). The advantage of BNs is that they can handle the conditional dependence between observed or unobserved random variables in the statistical model and can provide accurate probabilistic predictions based on a limited dataset. Therefore, BNs are widely used in pattern recognition, classification, and decision-making problems ${ }^{29}$. Furthermore, they are becoming increasingly popular in environmental science ${ }^{29}$, medicine ${ }^{30,31}$, agriculture ${ }^{32}$, and industrial fields ${ }^{33,34}$, and they are also being used in rock mechanics and rock engineering ${ }^{35-38}$. Notably, to establish a BN model, it is crucial to determine a reasonable BN structure. However, in the existing studies on BNs, the network structure is automatically generated by software or established by qualitative analysis. Therefore, it is necessary to quantitatively analyze the rationality of the network structure in future research.

For our analysis, we have compiled a case database containing 286 sets of data from 10 different tunnels with nine parameters: rock hardness, weathering degree, rock mass integrity, rock mass structure, structural plane integrity, in-situ stress, groundwater, rock basic quality, and surrounding rock level. Then, Bayesian search and expectation--maximization (EM) algorithms are used to learn the (SRC-BN) structure and parameters, respectively. Moreover, strength analysis is utilized to quantify the rationality of the learned SRC-BN structure. In addition, we examine and revise the learned conditional probability tables (CPTs) based on the expert experience, thereby improving the performance of the SRC-BN model in the case of small sample size and imbalanced


Table 1. Rock mass quality classification methods.
![img-0.jpeg](img-0.jpeg)

Figure 1. Workflow of the SRC-BN model.
samples. Finally, ten-fold cross-validation method and confusion matrix (including accuracy, precision, recall, F-measure, and receiver operating characteristic (ROC) curves) are used to evaluate the performance of the model. Furthermore, ten sets of other underground engineering cases are used to verify the feasibility of proposed SRC-BN model, and sensitivity analysis is employed to evaluate the importance of each input parameter in the model. The specific workflow of this study is shown in Fig. 1. The SRC-BN model can probabilistically predict the quality grade of tunnel surrounding rock with incomplete data. Moreover, the SRC-BN model overcomes the influence of small and unbalanced samples on the accuracy of SRC. In general, this probabilistic method for predicting rock mass quality grades is of immense significance for tunnel and underground engineering applications under the condition of large buried depth and high in-situ stress.

# Predictive analysis and data set description 

Inputs of SRC-BN. Since 1920, numerous methods have been proposed for rock mass classification ${ }^{29}$. The internationally acceptable methods for evaluating the rock mass quality include rock structure rating (RSR), rock mass rating (RMR), Q-system (Q), geological strength index (GSI), and modified basic quality ([BQ]) classification methods, etc. The indicators of these classification methods are shown in Table 1. According to the

![img-1.jpeg](img-1.jpeg)

Figure 2. Classification of factors affecting rock mass quality.


Table 2. Qualitative and quantitative categorization of rock hardness.

Existing studies on rock mass quality classification, the main influencing factors can be divided into physical and mechanical properties of rock, rock mass structural states, and other geological environment factors, as shown in Fig. 2.

Tunnel excavation is a dynamic process, and the changes in underground geological conditions are also uncertain. Therefore, the quality evaluation of tunnel surrounding rock is a dynamic probabilistic problem. BN is a powerful method to dynamically deal with datasets containing multiple variables and missing data as well as with conditional dependencies among the variables. It can also be used to quickly calculate the posterior probability of each state of the target node. It can be seen from Table 1 and Fig. 2 that the main factors affecting the surrounding rock quality of tunnels are rock hardness, rock integrity, in-situ stress, and groundwater. Hence, based on previous work^{14}, we consider seven parameters that have a direct or indirect impact on the tunnel surrounding rock quality evaluation: weathering degree, rock hardness, structural plane integrity, rock mass structure, rock mass integrity, in-situ stress, and groundwater. Another parameter called *BQ* is used as an intermediate variable or as a categorical variable in the network. A brief description of these parameters and their acquisition methods are presented in the following subsections.

### Rock hardness

Rock hardness is an important indicator to measure the quality of rock mass. The harder the rock, the better the rock quality^{40}. The rock hardness can be measured by qualitative or quantitative methods, as shown in Table 2. The qualitative assessment is mainly based on the sound and rebound of geological hammer hitting the rock and the rock condition after immersion. The quantitative measurement of rock hardness is based on the saturated uniaxial compressive strength (*R*_{s}) of rock. *R*_{s} can be obtained by uniaxial compressive


Table 3. Qualitative and quantitative classification of rock weathering degree.


Table 4. Quantitative classification of rock mass integrity.
strength test. The point load strength or rebound value of the rock can also be measured on site, and finally $R_{s}$ is calculated by using empirical formula ${ }^{41,42}$. We recommend using on-site point load test or rebound test to obtain the $R_{s}$ value indirectly and quantitatively.

Weathering degree. The weathering degree refers to the degree of damage to the rock by weathering. The higher the weathering degree, the lower the rock strength. The weathering degree is also often used to classify the surrounding rock quality of tunnels ${ }^{43}$. The qualitative and quantitative classification criteria of rock weathering degree are shown in Table 3. Qualitative classification is a comprehensive judgment based on the characteristics of rock structure, mineral composition, degree of fragmentation, etc. Quantitative classification is based on the wave velocity ratio $\left(k_{r}\right)$ or weathering coefficient $\left(k_{f}\right)$ of the rock ${ }^{44}$. $k_{r}$ refers to the ratio of compressional wave velocity between weathered rock and fresh rock. $k_{f}$ refers to the ratio of the saturated uniaxial compressive strength between weathered rock and fresh rock.

Rock mass integrity. The rock mass integrity is one of the most important parameters that affect the tunnel surrounding rock quality ${ }^{45}$. The rock mass integrity reflects the development of structural planes, including the number of joint sets, joint spacing, and the degree of combination of main structural planes that affect the stability of the surrounding rock. The quantitative classification of rock mass integrity is shown in Table 4. This classification is based on the rock mass integrity coefficient $\left(K_{s}\right) . K_{s}$ is the square of the ratio of elastic longitudinal wave velocity $\left(V_{y m}\right)$ of rock mass to the elastic longitudinal wave velocity $\left(V_{y n}\right)$ of rock (block) ${ }^{44}$. In actual engineering, it is more common to measure the volume joint number $\left(J_{v}\right)$ of the rock mass to obtain the $K_{s}$ value and finally obtain the rock mass integrity. It is worth noting that the unit of $J_{v}$ is number of joints per $\mathrm{m}^{3}$.

Rock mass structure. The rock mass structure is composed of structural plane and structural body, which reflects the development degree of structural plane and the fragmentation of rock mass. The structural plane is divided into weak plane surface and hard structural plane. The structural body is divided into block shape and plate shape according to the mechanical action. Structural plane and body are combined and arranged differently in the rock mass to form different types of structures. The rock mass structure can be comprehensively judged according to the rock mass integrity, characteristics of rock mass, and development of structural plane. Determination of the type of rock mass structure plays an important role in evaluating the stability of the rock mass under engineering loads. The Chinese hydropower industry has proposed the classification and semiquantitative identification methods of rock mass structure (see Table 5) ${ }^{44}$.

Structural plane integrity. Structural plane integrity is comprehensively assessed according to the opening degree, roughness, and filling of the structural plane. It reflects the characteristics of the structural surface, including the degree of opening and filling, and it is closely related to the rock mass integrity. Rock mass with good integrity usually has a better degree of structural plane integration. The Ministry of Water Resources of the People's Republic of China (2014) proposed a semi-quantitative classification standard for the structural plane integrity ${ }^{44}$, as shown in Table 6.

In-situ stress. In-situ stress is the stress confined in a rock formation before excavations or other perturbations. It is an important mechanical property, which affects the bearing capacity of rock mass. For rock mass existing in a certain in-situ stress environment, the greater the confining pressure formed by in-situ stress, the greater the bearing capacity of rock mass ${ }^{46}$. At the same time, under high in-situ stress conditions, hard rocks are prone to


Table 5. Classification of rock mass structure.


Table 6. Classification and characteristics of the structural plane integrity.


Table 7. Classification of in-situ stress.
rockburst disasters, while soft rocks are prone to large deformation disasters ${ }^{47,48}$. Therefore, the in-situ stress has a significant influence on the quality of tunnel surrounding rock. The internationally popular $Q$ and $[B Q]$ methods consider the correction of in-situ stress to evaluate the surrounding rock quality. The quantitative classification of in-situ stress is shown Table 7. Here, $\sigma_{\max }$ is the maximum initial stress perpendicular to the hole axis.

Groundwater. As an important environmental factor, groundwater affects the deformation and destruction of rock mass, thereby influencing its stability. Expansive soft rock is a disaster for underground engineering, and its mechanical properties depend on the degree of interaction between soft rock and water. It can be seen from Table 1 that the methods such as $Q, R M R$, and $[B Q]$ also consider the impact of groundwater on the surrounding rock quality. However, in most methods, the impact of groundwater on the surrounding rock quality is evaluated by quantifying the water pressure, which is often impossible in actual engineering applications. Therefore, based on engineering experience, a qualitative description of different water emergence conditions from the tunnel excavation surface is presented in Table 8, where $p$ is the water pressure of surrounding rock fissures (MPa), and $q$ is the water output per 10 m hole length $(\mathrm{L} / \mathrm{min} \cdot 10 \mathrm{~m})$.


Table 8. Classification of water outflow from tunnel excavation face.


Table 9. Classification of $B Q$.

Rock mass basic quality. The $[B Q]$ method uses the hardness and the integrity of rock mass to make a preliminary assessment of its quality. The classification of $B Q$ is shown in Table 9. The $[B Q]$ method is widely used in China, where the determination of $B Q$ value is the basis for the final quality assessment of tunnel surrounding rock. $B Q$ is also crucial for the preliminary design of the initial support structure of tunnel. Generally, due to the urgency of tunnel construction, the strength and integrity of rock mass are not determined early enough at the construction site. In the tunnel design stage, the quality grade of tunnel surrounding rock is often judged preliminarily. When the strength and integrity of rock mass are not measured, the surrounding rock quality grade obtained from the tunnel design stage can be input as the $B Q$ value into the model. In this way, more parameters can be input in the SRC-BN model to improve its reliability. Similarly, in the tunnel planning stage, the strength and integrity of rock mass can be approximated based on the geological information revealed by the borehole, and then the $B Q$ value can be preliminary assessed using the proposed SRC-BN model.

Description of database. We have collected a tunnel surrounding rock quality evaluation database containing nine parameters: rock hardness, weathering degree, rock mass integrity, rock mass structure, structural plane integrity, in-situ stress, groundwater, $B Q$ and surrounding rock level. In this database, $B Q$ are expressed in terms of the quality grade and not the quality score of the surrounding rock. Surrounding rock level is the quality grade of surrounding rock referenced by the actual support at the tunnel construction site. In the construction of traffic tunnels in China, surrounding rock level is mainly determined by $[B Q]$ method (see Appendix A for $[B Q]$ method). The parameter $B Q$ can be used as an intermediate or categorical parameter in the established SRC-BN structure. Most of tunnel surrounding rock quality evaluation cases have been collected from $\mathrm{Niu}^{14}$, and a few cases are from unpublished scientific reports. These data enabled us to compile a new database of tunnel surrounding rock quality, which is used in our analysis. The database has a total of 286 cases, which are from ten typical tunnels in China (Niba mountain tunnel, Zhegu mountain tunnel, Erlang mountain tunnel, Wangiangling tunnel, Zaozilin tunnel, Longxi tunnel, Futang tunnel, Miyaluo \#3 tunnel, Shiziping tunnel, and Micang mountain tunnel). Figure 3 shows the distribution of nine parameters in the 286 cases. Our database covers a wide range of values for these nine parameters. Therefore, in principle, it has a good applicability within the scope of considered cases. With the emergence and addition of new data in the future, this method is expected to become more generalized and practical.

Parameters excluded in the SRC-BN model. Except the parameters mentioned in "Inputs of SRC-BN", other parameters can also be used to predict the surrounding rock quality level of tunnels. However, we do not consider them in the SRC-BN model due to the following reasons:
$R Q D . \quad R Q D$ was proposed by Deere et al. ${ }^{4}$ to quantify the rock quality. The internationally used $Q$ and $R M R$ methods for the surrounding rock quality classification use $R Q D$ indicator. However, $R Q D$ has certain limitations. Firstly, a specific size of drill bit and coring equipment must be used to obtain the standard $R Q D$ value. Because cores are considered in weak and unintegrated rock masses, the $R Q D$ values obtained by using different drill bits and coring equipment vary greatly ${ }^{49-51}$. Secondly, $R Q D$ roughly counts cores with lengths greater than 10 cm and less than $10 \mathrm{~cm}^{52}$. Finally, since we have selected the index of rock mass integrity, the impact of rock mass completeness on the tunnel surrounding rock quality is considered. Therefore, $R Q D$ is not considered in the established SRC-BN model.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** Histograms of the eight parameters considered to predict the quality of tunnel surrounding rock. The numbers on the X-axis represent the characteristic of different parameters. (1) The numbers 1, 2, 3, 4, and 5 for rock hardness represent hard, slightly hard, slightly soft, soft, and extremely soft, respectively. (2) 1, 2, 3, 4, and 5 for rock mass integrity represent complete, slightly complete, slightly broken, broken, and extremely broken, respectively. (3) 1, 2, 3, 4, and 5 for rock mass structure represent integral/extremely-thick layered, block/thick layered, fractured block/medium-thick layered/interlayer/thin layered/mosaic, fragmented, and granular, respectively. (4) 1, 2, 3, 4, and 5 for weathering degree represent fresh, slight, medium, severe, and extreme, respectively. (5) 1, 2, 3, and 4 for structural plane integrity represent good, ordinary, bad, and very bad, respectively. (6) 1, 2, 3, and 4 for groundwater represent dry/wet, moist/dripping, rain-like dripping/linear water, and tubular water/gushing water, respectively. (7) 1, 2, 3, and 4 for in-situ stress represent low, medium, high, and extremely high, respectively.

*Occurrence of main weak structural plane.* The relationship between the occurrence of main weak structural plane and the tunnel axis has a certain influence on the surrounding rock stability^{53,54}. This parameter is a crucial indicator in the design of tunnel in the active area of neotectonic movement. This parameter is considered in the [*BQ*], *HC*, and *RMR* methods, but it is not considered in *Q*, *GSI*, and *RMI* methods. Since this parameter is also missing in the collected data samples, we did not consider it in the established SRC-BN model. In future research, we will consider including this parameter in the SRC-BN model.

*Joint features.* The joint characteristics include joint set number, joint spacing, joint length, joint roughness, and joint filling. Some joint features are considered in both *Q* and *RMR* methods. The five main joint features essentially reflect the structural characteristics and integrity of rock mass. In particular, the structure and integrity of rock mass have been considered in the established SRC-BN model. Joint roughness and joint filling basically reflect the completeness of structural plane. They are also indirectly considered in the established SRC-BN model. Hence, the five joint features are not employed in the SRC-BN model.

Other parameters. Traffic tunnels passing through areas with special geological structures may encounter distinct problems such as high ground temperature and karst. These geological issues should also be considered in the quality evaluation of tunnel surrounding rock. However, there is no case with such issues in the collected surrounding rock samples. Thus, these issues cannot be considered in the established SRC-BN model. Fortunately, we have collected some samples under high in-situ stress environment, so our model considers the impact of high in-situ stress on the tunnel surrounding rock quality. In subsequent studies, we will further consider the effect of special geological issues on the tunnel surrounding rock quality.

## Establishment of SRC-BN structure and parameter learning

SRC-BN structure definition. BN model is probabilistic graphical model, which was proposed by Judea Pearl in 1986^{55}. BN is a directed acyclic graph composed of nodes and arrows connecting nodes. The nodes in BN indicate random variables, and the arrows connecting nodes represent the relationship between two variables. This relationship is quantitatively expressed by conditional probability distributions. Therefore, there is no arrow between two conditionally independent variables^{56}.

In the BN model, the network structure must be defined first to carefully consider the conditional independence and independent relations among the input variables. BN structure can be defined through structural learning^{56} or experience. After the BN structure is defined, the conditional probability between the variables must be defined. The CPTs can be used to represent the quantitative dependence among the discrete variables. When new evidence (observed variable) is introduced into the BN or the existing evidence is updated, the Bayesian method is used to calculate the changes in CPTs of unobserved variables. This process is called “belief updating,” which is described in “Belief updating”.

BN can be used to solve an uncertain problem, such as classification of tunnel surrounding rock quality. Here, Y is used to represent the class variable, which is divided into five levels (Y = 1, 2, 3, 4, 5). X is used as an input vector, which includes n observed or unobserved input variables that affect the class variable Y (X = (X_{1}, X_{2}, ..., X_{n})). In this work, X is given by the seven input variables mentioned in “Inputs of SRC-BN”. In addition, the variable BQ can be used as an intermediate variable or a categorical variable. Subsequently, the collected 286 cases (mentioned in “Description of database”) are used to train the SRC-BN model.

A structural learning algorithm, called Bayesian Search, is used to establish the BN structure^{56,57}. Before examining the BN structure, we are allowed to increase the professional background knowledge to obtain a reasonable network structure. Since the input parameters are qualitative indicators or discretized continuous indicators, the calculation of the statistical correlation between the input parameters has little reference value. Fig. 4 illustrates the SRC-BN structure for predictive classification of tunnel surrounding rock quality, given seven input parameters: weathering degree, rock hardness, structural plane integrity, rock mass structure, rock mass integrity, in-situ stress, and groundwater. In addition, BQ can be used as an intermediate parameter. It is especially useful when the rock hardness or rock mass integrity input parameters are missing.

Discretization of parameters. Among the eight parameters, rock mass structure, structural plane integrity, and groundwater are the qualitative indicators (discrete variables), while the remaining five parameters are continuous variables. To use the continuous variables in BN, it is necessary to discretize them or specify a density function for them^{58}. Under limited sample conditions, it is difficult to specify an accurate density function for the input parameters. Therefore, the discretization method is used to deal with continuous variables. The discretization method divides the continuous value into several ranges. In this article, we adopt the parameter division range recommended by the industry guide “Standard for Engineering Classification of Rock Mass.” The eight parameters have been discussed in “Inputs of SRC-BN”. The interval range and possible states of each node in SRC-BN are shown in Table 10.

Learning parameters. Based on the model structure defined in Fig. 4, the SRC-BN model can learn parameters from dataset. In other words, the CPTs of each node in the SRC-BN model can be obtained through training and learning. Generally, the expectation--maximization (EM) algorithm is used to estimate the CPTs of each node in the BN^{59}. The EM algorithm can find the maximum likelihood estimate of a set of parameters even when some variables in the dataset are missing^{58,60}. The workflow of the EM algorithm is show as Fig. 5.

The standard calculation framework of EM algorithm is composed of expectation-step (E-step) and maximization-step (M-step). E-step mainly estimates the parameters by observing data and existing models, and then this estimated parameter value is used to calculate the expected value of the likelihood function. M-Step is to find the corresponding parameter when the likelihood function is maximized. Further details about the EM algorithm can be found in Jensen and Nielsen^{58}.

Belief updating. After obtaining SRC-BN parameters by using EM algorithm, belief updating is the next step. Belief updating is also called probabilistic inference, and it is used to calculate the posterior probability of a given evidence (observations)^{60}. In particular, for predictive analysis of the tunnel surrounding rock quality, this method is used to compute the posterior probability of a given evidence, where the evidence may be a set of incomplete observations about the input parameter vector. Generally, the junction tree (JT) algorithm is used to calculate the posterior probability^{61}. The workflow of the JT algorithm is show as Fig. 6.

The calculation steps of the JT algorithm in belief updating are summarized as follows: (1) a junction tree is constructed based on the existing BN; (2) a message passing algorithm is used to convey messages along the junction tree; (3) response to queries are provided when introducing evidence. Further details of the JT algorithm can be found in Jensen and Nielsen^{58} and Korb and Nicholson^{60}.

![img-3.jpeg](img-3.jpeg)

Figure 4. SRC-BN structure of tunnel surrounding rock quality.


Table 10. Intervals of the input parameters of SRC-BN.

![img-4.jpeg](img-4.jpeg)

Figure 5. Workflow of the EM algorithm.

![img-5.jpeg](img-5.jpeg)

Figure 6. Workflow of the JT algorithm.

Strength analysis. The established SRC-BN structure is a tree structure. Therefore, we need to analyze the influence strength of parent node on the child node in this tree structure. Then, the result can be used to quantitatively judge the rationality of the SRC-BN structure (the relationship between the input parameters of SRC-BN are analyzed from a qualitative perspective in "Inputs of SRC-BN", which is the expert background knowledge before the establishment of the SRC-BN structure). The influence strength is calculated based on the CPT of child node, which essentially expresses the distance between various conditional probability distributions over the child node conditional on the states of the parent node[62]. We use the Euclidean distance in GeNIe to calculate the influence strength[63]. Suppose A and T are two points in n-dimensional space, and their discrete probability distributions are shown in Eq. (1).

$$
\left\{\begin{array}{l}
A \in\left\{\left(a_{1}, a_{2}, \ldots, a_{n}\right) \mid a_{i}>0, \sum_{i=0}^{n} a_{i}=1\right\}, n>1 \\
T \in\left\{\left(t_{1}, t_{2}, \ldots, t_{n}\right) \mid t_{i}>0, \sum_{i=0}^{n} t_{i}=1\right\}, n>1
\end{array}\right.
$$

The calculation of spatial distance (normalized) between two points is shown in Eq. (2).

$$
E_{\text {norm }}(A, T)=\frac{\sqrt{\sum_{i=1}^{n}\left(a_{i}-t_{i}\right)^{2}}}{\sqrt{2}}
$$

![img-6.jpeg](img-6.jpeg)

**Figure 7.** Results of strength analysis of the SRC-BN model.

Figure 7 shows the strength analysis results obtained using GeNIe. Average indicates the average value of the distance. Maximum is the largest distance from the distribution. Weighted is the edge probability of the parent node to measure the distance. We usually only focus on the average and maximum values. The larger the calculated value, the stronger the influence. According to Fig. 7, the following conclusions can be drawn: (1) the average value of node *H* (rock hardness) and node *C* (rock mass integrity) on node *B* (*BQ*) exceeds 0.6, and the maximum value is also above 0.9. From the description in "Inputs of SRC-BN", it can be seen that *BQ* is mainly judged based on the hardness and integrity of rock mass. Therefore, the qualitative and quantitative assessments of the structure are consistent. (2) The average value of node *B* to node *L* (classification of tunnel surrounding rock quality) exceeds 0.5, and the maximum value also reaches above 0.9. According to the description in "Inputs of SRC-BN", *BQ* is a preliminary judgment of the surrounding rock quality. In addition, the maximum value of node *G* (groundwater) and node *I* (in-situ stress) to node *L* are both above 0.8. Consequently, the qualitative (in "Inputs of SRC-BN") and quantitative judgment results of the structure are coincident. (3) The quantitative calculation results of the tree structure at *D* → *C* (gomphosis → rock mass integrity), *S* → *C* (rock mass structure → rock mass integrity), and *W* → *H* (weathering → rock hardness) are also consistent with the expert background knowledge. Therefore, the established SRC-BN structure is reasonable from both qualitative and quantitative perspectives.

## Results and discussion

### Learned SRC-BN model

Based on the collected 286 cases for the classification of tunnel surrounding rock quality cases, we use the GeNIe software to train the SRC-BN model. The SRC-BN structure is established by combining expert background knowledge and Bayesian search algorithm. The EM algorithm is used to learn the network parameters, and the JT algorithm is used to update beliefs to convey the uncertainty (before parameter learning, we assume that there is no prior knowledge, so the prior probability of each state of the node is the same). In addition, the learned CPTs in the SRC-BN model are also evaluated and revised based on the expert experience, which improves the model performance in the case of small and imbalanced samples. The trained SRC-BN model is shown in Fig. 8. Due to the complex SRC-BN structure, the CPTs of each node are listed in Appendix B.

After learning the structure and parameters of SRC-BN model, when a set of new observation values for the input variables are given, JT algorithm can be used for probabilistic inference to obtain the probability distribution of the target node state. For instance, let us assume that we obtain the following set of input data regarding the tunnel surrounding rock parameters: *W* = Medium, *R*<sup>*c*</sup> = 25 MPa (*H* = Slightly soft), *D* = Ordinary, *S* = Medium-thick layered structure (State 3), *K*<sup>*c*</sup> = 0.40 (*C* = Slightly broken), *G* = Wet, *R*<sup>*c*</sup>/*σ*max = 3 (*I* = Low). Using these variable values for the predictive classification of tunnel surrounding rock quality with the trained SRC-BN model, the probability of nodes *B* and *L* are updated, and we obtain that *P* (*B* = 4|*W* = Medium, *H* = Slightly soft, *D* = Ordinary, *S* = State 3, *C* = Slightly broken) = 97.6%, and *P* (*L* = IV|*W* = Medium, *H* = Slightly soft, *D* = Ordinary, *S* = State 3, *C* = Slightly broken, *G* = Wet, *I* = Low) = 86.5%. This implies that IV is the most likely grade for such tunnel surrounding rock. SRC-BN model can also make prediction with incomplete input data. For example, *H*, *C*, *B*, and *I* are not known in the previous example, and we can recalculate the probability of the target node under the given input parameters as *P* (*L* = IV|*W* = Medium, *D* = Ordinary, *S* = State 3, *G* = Wet) = 42.9% (the probability of IV is also the largest among all states of the node). The estimated change in the probability of tunnel surrounding rock quality grade has practical significance for tunnel support and design. In addition, the results of probability of tunnel surrounding rock quality grade vary with our knowledge of the input parameters.

The predicted probability can also be manually calculated using CPTs (Appendix B) of each node variable in SRC-BN model. The posterior probability of *L* = IV given **X**, i.e., *P*(L = IV|**X**), is expressed as follows:

![img-7.jpeg](img-7.jpeg)

**Figure 8.** SRC-BN model after parameter learning using EM algorithm. State1, state2, state3, state4, and state5 of rock mass structure represent integral/extremely-thick layered, block/thick layered, fractured block/medium-thick layered/interlayer/thin layered/mosaic, fragmented, and granular, respectively.

$$P(L = \text{IV}|\mathbf{X}) = \frac{P(\mathbf{X}|L = \text{IV})P(L = \text{IV})}{P(\mathbf{X})} = \frac{\prod_{i=1}^{n} P(x_i | L = \text{IV})}{\sum_{j = \text{I,II,III,IV,V}} \prod_{i=1}^{n} P(x_i | L = j)}$$

where **X** = (*x*₁, *x*₂, ..., *x*ₙ) is the input vector, which represents the input variables (*n*max = 8 in this study); *j* is the state of target node *L*, and *j* = I, II, III, IV, V.

Now, we illustrate how to use Eq. (3) to classify the quality of tunnel surrounding rock. The above example is used as the input data, i.e., **X** = (*W* = Medium, *H* = Slightly soft, *D* = Ordinary, *S* = State 3, *C* = Slightly broken, *G* = Wet, *I* = Low). Combining CPTs in Appendix B and Eq. (3), the posterior probability of *B* = 4 under given **X** is calculated as follows:

$$P(B = 4|\mathbf{X}) = \frac{0.405 \cdot 0.309 \cdot 0.635 \cdot 0.502 \cdot 0.42 \cdot 0.976}{0.405 \cdot 0.309 \cdot 0.635 \cdot 0.502 \cdot 0.42 \cdot 1} = 0.976$$

The posterior probability of *L* = IV under given **X** is calculated as follows:

$$P(L = \text{IV}|\mathbf{X}) = \frac{0.405 \cdot 0.309 \cdot 0.635 \cdot 0.502 \cdot 0.42 \cdot 0.266 \cdot 0.443}{0.405 \cdot 0.309 \cdot 0.635 \cdot 0.502 \cdot 0.42 \cdot 0.266 \cdot 0.443 \cdot 1} \cdot \frac{0.006 \cdot (0.025 + 0.015 + 0.029 + 0.029) + 0.976 \cdot 0.886}{0.006 \cdot 4 + 0.976} = 0.865$$

The result of manual calculation is the same as that of GeNIe. Thus, based on Eq. (3) and CPTs in Appendix B, the classification-probability of tunnel surrounding rock quality can be easily predicted without any software.

**SRC-BN model validation.** *Ten-fold cross-validation.* According to the influencing factors of surrounding rock quality, it can be known that the corresponding samples are inherently imbalanced. Therefore, the ten-fold cross-validation method is used to validate the proposed model, and the accuracy, precision, recall, F-measure, and ROC curves are used to evaluate the performance of the model. The details of model evaluation methods and indicators are provided in Appendix C. Firstly, all the data (286 sets) are randomly divided into 10 groups. Then, nine groups are used as training sets, and the remaining one group is used as the verification set. Finally, the process is repeated 10 times to maximize the use of each set of data to train and validate the model. The average accuracy of the 10 validation sets is used as the performance measure of the model. In the established SRC-BN model, *B* and *L* are used as the classification variables, so the average accuracy of the established

![img-8.jpeg](img-8.jpeg)

**Figure 9.** Confusion matrix of ten-fold cross-validation.

![img-9.jpeg](img-9.jpeg)

**Figure 10.** Precision, recall, and F-measure for classification variable *L*.

Model for these variables is measured in the model test. The results of ten-fold cross-validation are shown in Fig. 9. The values on the diagonal of the heatmap in Fig. 9 indicate the number of correct predictions. It is clear that the average accuracies of the model for classification variables *B* and *L* are 100% and 89.2%, respectively. Since the accuracy of variable *B* is 100%, only the prediction of the learned model for variable *L* is analyzed in detail. It can be seen in Fig. 10 that the prediction precision and recall of the learned model for each sub-state of the variable *L* are both above 85%, except the state IV, whose prediction precision is approximately 78%. Then, the learned model's F-measure for each sub-state of the variable *L* is greater than 90%, except that for the state IV is nearly 82%. The average values of precision, recall, and F-measure are approximately 91%, 92%, and 91%, respectively. Generally, the closer the precision, recall, and F-measure to 100%, the better the learned model. In addition, Fig. 11 shows that the area under the curve (AUC) of the learned model for each sub-state of the variable *L* is close to 1. The average value of AUC is 0.98. This verifies the feasibility of the proposed model for predicting the classification-probability of surrounding rock quality, even under a small and imbalanced database.

*Validation with new samples.* To further verify the effectiveness of the learned SRC-BN model, the *Q* and *RMR* methods are used to test 10 cases from three underground engineering projects, including hydropower and railway tunnel projects. Because the *Q* and *RMR* methods are inconsistent with the grading standards used in this article, according to previous studies^{64–67}, the *Q* and *RMR* grades are standardized (see Table 11). The input parameters and quality classification results of surrounding rock related to the proposed SRC-BN model are shown in Table 12. It is worth noting that the *Q* and *RMR* value scoring in Table 12 are based on the existing literature, and not on this study. In addition, all the 10 test cases do not include the rock mass integrity parameter, and some test cases lack the groundwater and in-situ stress parameters. The above learned SRC-BN model is capable of handling incomplete data.

![img-10.jpeg](img-10.jpeg)

**Figure 11.** ROC curves for classification variable *L*.


**Table 11.** Relationship between [BQ], *Q*, and *RMR* rock mass classification methods.


**Table 12.** Verification results of the new tunnel cases. The "Actual" in the last column of the table is the quality grade of surrounding rock referenced by the actual support at the tunnel construction site.

The classification no. 1 in Table 12 is taken as an example to calculate the posterior probability of variable nodes through GeNle (see Fig. 12). The nodes with a probability of 100% in Fig. 12 are known evidence, and the posterior probability distribution of nodes with unknown evidence can be obtained by calculation. As shown in Fig. 12, the probability of a slightly complete rock mass is approximately 98.7%, and that of grade III surrounding rock is nearly 84.0%.

It can be seen from Table 12 that the BN method predicts one case (case 9) incorrectly, which has more missing data, so the prediction results are conservative. In addition, the *Q* and *RMR* methods predict three error cases. According to the surrounding rock quality classification results in Table 12, although the accuracy of the established SRC-BN model is not much different from the internationally popular *Q* and *RMR* methods, it has a wider application scope (especially with incomplete data).

![img-11.jpeg](img-11.jpeg)

Figure 12. Posterior probability of target nodes in GeNIe.

![img-12.jpeg](img-12.jpeg)

Figure 13. Results of sensitivity analysis based on the SRC-BN model.

**Sensitivity analysis.** Since the SRC-BN structure is a tree structure, it is not a radial structure that conforms to the naive Bayesian theory (the input variables are independent of each other and are only related to the target node). Therefore, sensitivity analysis is used to determine which variables contribute the most to the prediction of surrounding rock quality levels. Mutual information (MI) and variance reduction (VR) are employed to measure the parametric sensitivity. The specific measurement indicators can be found in Shannon^{70} and Pearl^{71}. Fig. 13 shows the sensitivity analysis results calculated by Netica, including the influence of five input parameters on *BQ* (*B*) and the influence of eight input parameters on the classification of surrounding rock quality (*L*). Percent represents the contribution of each input variable to the target node. Here, nodes *B* and *L* are set as the target node. It is observed that the rock mass integrity (*C*) and rock hardness (*H*) have the highest contribution to the *BQ* (*B*). The *B* has the highest contribution to the *L*. Therefore, the hardness and integrity of rock mass have a greater impact on the final judgment of the surrounding rock quality. These results and parameter description in "Inputs of SRC-BN" are consistent with the strength analysis in "Strength analysis". Of course, other parameters (*W*, *D*, *S*, *G*, and *I*) are also important for predicting the classification of surrounding rock

quality. Since the SRC-BN model has a tree structure (non-naive Bayesian structure), the calculated sensitivity value of the node that is not directly connected to the target node is small. Although the mutual information and variance reduction in Fig. 13 are relatively small, their influence on the classification of surrounding rock quality should also be taken into account.

## Conclusion

In this study, we proposed a new method based on BNs to predict the classification-probability of tunnel surrounding rock quality with incomplete information. The intelligent SRC model that can handle incomplete data is of great significance for the dynamic design and construction of tunnels. The main findings of this study can be summarized as follows.
(1) A probabilistic prediction model of surrounding rock quality grades was established through structural learning and parameter learning based on 286 sets of cases. Strength analysis was utilized to quantitatively verify the rationality of the learned SRC-BN structure.
(2) The ten-fold cross-validation results showed that the accuracy of categorical variables $B$ and $L$ was $100 \%$ and $89.2 \%$, respectively. The average precision, recall, and F-measure values for variable $L$ were over $91 \%$. The AUC for each sub-state of variable $L$ exceeded 0.96 . The evaluation results verified the stable and good performance of the learned model for predicting the classification-probability of surrounding rock quality, even with a small and imbalanced database.
(3) The validation results with ten samples suggested that the error rate of the learned SRC-BN model was lower than that $Q$ and $R M R$ methods. The results indicated that the learned SRC-BN model could identify the surrounding rock grade more accurately and intelligently, even when the original information was incomplete.
(4) The sensitivity analysis results showed that the hardness and integrity of the rock mass were the main parameters that affected the quality of tunnel surrounding rock. Obviously, other parameters affected the quality of tunnel surrounding rock to a certain extent, among which the weathering degree had the lowest impact.

Overall, the proposed SRC-BN model can probabilistically predict the quality grade of tunnel surrounding rocks with incomplete data, which has great application value in the tunnel and underground engineering. Moreover, the results also have certain reference value for other rock mass engineering applications related to rock mass quality, such as slope engineering. However, since the training samples and verification projects of the SRC-BN model are mainly tunnels and underground projects in Southwest China, validating the applicability of the model for tunnels and underground projects in other regions needs further study. Therefore, in the future, we will collect more samples to improve the model's performance. In addition, cloud technology may be integrated to establish a cloud platform for tunnel information management.

## Data availability

The datasets generated or analyzed during the current study are available from the corresponding author upon reasonable request.

Received: 18 April 2022; Accepted: 26 August 2022
Published online: 18 November 2022

# Acknowledgements 

This work was supported by the Science \& Technology Department of Sichuan Province, China [Grant no. 2021YFS0317]; and the National Natural Science Foundation of China (NSFC) [Grant No. U19A20111]; and the Science \& Technology Department of Sichuan Province, China [Grant No. 2021YJ0041].

## Author contributions

J.M. conceived the idea and wrote the manuscript; T.L. supervised the project as well as reviewed and provided the train datasets; X.L. and S.Z. completed the model evaluation and validation; C.M., D.W. and K.D. handled all the figures and tables. All the authors have discussed/verified the results and contributed to the final manuscript.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary Information The online version contains supplementary material available at https://doi.org/ 10.1038/s41598-022-19301-6.

Correspondence and requests for materials should be addressed to T.L.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
(c) The Author(s) 2022