# Article 

## Risk Reasoning from Factor Correlation of Maritime Traffic under Arctic Sea Ice Status Association with a Bayesian Belief Network

Zhuang Li ${ }^{1}$, Shenping Hu ${ }^{2, * *}$, Guoping Gao ${ }^{3}$, Yongtao $\mathrm{Xi}^{2}$, Shanshan $\mathrm{Fu}^{4}$ and Chenyang Yao ${ }^{2}$ (D)<br>check for updates

Citation: Li, Z.; Hu, S.; Gao, G.; Xi, Y.; Fu, S.; Yao, C. Risk Reasoning from Factor Correlation of Maritime Traffic under Arctic Sea Ice Status Association with a Bayesian Belief Network. Sustainability 2021, 13, 147. https://dx.doi.org/10.3390/su1301 0147

Received: 16 November 2020
Accepted: 23 December 2020
Published: 25 December 2020

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (C) 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/ licenses/by/4.0/).

1 College of Ocean Science and Engineering, Shanghai Maritime University, Shanghai 201306, China; shmtu_lizhuang@163.com
2 Merchant Marine College, Shanghai Maritime University, Shanghai 201306, China; ytxi@shmtu.edu.cn (Y.X.); yaochenyang@stu.shmtu.edu.cn (C.Y.)
3 College of Marine Ecology and Environment, Shanghai Ocean University, Shanghai 201306, China; gpgao@shou.edu.cn
4 College of Transportation and Communication, Shanghai Maritime University, Shanghai 201306, China; ssfu@shmtu.edu.cn

* Correspondence: sphu@shmtu.edu.cn

Abstract: Sustainable growth should not only be beneficial to the shipping industry in the future, but is also an urgent need to respond to resource and environmental crises and strengthen shipping governance. Maritime traffic in Arctic waters is prone to encounter dangerous ice conditions, and it is essential to study the mechanism of ice collision risk formation in relation to ice conditions. Taking the ship-ice collision risk in Arctic waters as the research object, we propose a dynamic assessment model of ship-ice collision risk under sea ice status dynamic association (SDA) effect. By constructing the standard paradigm of risk factor dynamic association (DA) effect, taking SDA as the key association factor. Combing with other risk factors that affect ship-ice collision accidents, the coupling relationship between risk factors were analyzed. Then, using the Bayesian network method to build a ship-ice collision accident dynamic risk assessment model and combing with the ice monitoring data in summer Arctic waters, we screen five ships' position information on the trans-Arctic route in August. The risk behavior of ship-ice collision accidents on the selected route under SDA is analyzed by model simulation. The research reveal that the degree of SDA is a key related factor for the serious ice condition and the possibility of human error during ship's navigation, which significantly affects the ship-ice collision risk. The traffic in Arctic waters requires extra vigilance of the SDA effect from no ice threat to ice threat, and continuous ice threat. According to the ship-ice collision risk analysis under the SDA effect and without SDA effect, the difference in risk reasoning results on the five stations of the selected route are $32.69 \%,-32.33 \%,-27.64 \%$, $-10.26 \%$, and $-30.13 \%$ respectively. The DA effect can optimize ship-ice collision risk inference problem in Arctic waters.

Keywords: maritime traffic risk; ship-ice collision; Bayesian network; Dempster-Shafer theory; Arctic waters; dynamic association

## 1. Introduction

In the past few years, the shipping industry has been introducing necessary measures to improve safety and environmental performance. For example, 30 years ago, oil leakage and personal injuries were a very serious problem [1,2]. About 300,000 tons of oil leaked every year while thousands of human-beings were injured, but today, the number of leakage incidents per year is only about 5000 tons and 900 people died in ship accidents worldwide [3]. Affected by the increasingly extreme climate, for example, the storms that occur in China's coastal areas have caused great disasters [4], which will inevitably affect the safety of maritime traffic activities. The number of ship damages, casualties and direct

economic losses have increased year by year, and the cost of supporting safe operations in the shipping industry has suddenly increased. The more than 50,000 ships sailing on global routes consume nearly 500 million tons of fuel per year, and the amount of greenhouse gases such as carbon dioxide emitted by them is astronomical, causing environmental pollution to surrounding oceans, ports and cities [5].

However, there are still many major challenges ahead. First, in the face of the current resource and environmental crisis, neither the traditional passages nor the minor adjustments should be made. Traditions should be overturned and a sustainable future growth model will be constructed [6]. Second, technology is always the key to the transformation of human society, and also the main means for the sustainable development of shipping [7,8]. A thorough and long-term solution nowadays requires the use of technological innovation to achieve transformation and upgrading more than ever. In view of the opening of Arctic routes, the shipping industry will make full use of Arctic routes for ship transportation to become an inevitable demand and an essential choice [9]. Not only is it conducive to the energy-saving and efficient development of shipping, but it also increases the options for global shipping routes. At the same time, the restrictions on sea ice also have a certain impact on the safety of ship Arctic navigation. Floating ice at sea has a very prominent impact on the safety of ship navigation, and easily causes ship-ice collision accidents [10]. In the vast high-latitude waters, the state of floating ice is interrelated, and this association will form a coupling effect on the navigation risks of Arctic ships during long-distance voyages [11].

The Arctic route has become a new-period waterway connecting eastern Asia/west America to Europe, the normalization of the route selection has received more and more attention, and the maritime traffic in the Arctic waters is becoming more and more common [12]. For commercial ships, navigation in the Arctic northeast route is close to the continental shelf, and has a low probability of the ship encountering sea ice during the voyage, but has a long voyage time relative to the trans-Arctic route. With the melting of Arctic sea ice [13], it is the future trend to sail near the edge of the ice shelf in the center Arctic [14,15]. Ships moving towards the central area of the Arctic waters will encounter continuous changing sea ice condition. Ship-ice collisions will be a serious threaten to the safety of maritime traffic [16,17]. The dynamic risk of maritime traffic in the Arctic under ice conditions is currently a more urgent issue.

When conducting risk reasoning of maritime traffic accidents under the influence of sea ice. Huang simulated the impact of ship-wave-ice interaction on ship-ice collision accident, and predicted the ice impact that ship may encounter when sailing in Arctic waters [18]. By proposing a new method of numerical simulation, the damage of sea ice to propagation was analyzed in [19]. Chai provided a reference for ship structure design through statistics of the characteristics of on year ice in Arctic waters [20,21]. Such studies focus on the impact of the interaction between sea ice and ship's structure, leading to ship-ice accidents.

In addition, some scholars have analyzed the ship-ice accident risk mechanism to find the main reason for accidents. When analyzing the risk of maritime traffic in the Gulf of Finland in winter, Valdez Banda analyzed the causes of sea ice formation and found the most common ice conditions that affect maritime traffic safety [22]. In view of the risk of ship ice besetting accident, Montewka believes that sea ice affects the speed of ship on the one hand, and on the other hand becomes an obstacle on the channel, leading to ice besetting accidents [23]. Afenyo held the opinion that the failure of sea ice detection technology and the obstruction of sea ice on the channel will lead to ship-ice collision accidents, and analyzed the main reasons leading to ship-ice collision accidents in Arctic waters [24]. When analyzing the collision accident of maritime traffic in the Arctic ice region, Zhang believes that sea ice would mainly damage the structure of ships [25]. Fu thought that whether a ship ice besetting accident occurs depends on the effectiveness of a series of technical operations under sea ice conditions, by establishing a ship ice besetting accident event tree model, the severity of the consequences of ice besetting accident in

multiple scenarios is analyzed [26]. Goerlandt [27] used the ship maneuvering data and environmental data, analyzed the safe distance and safe speed between ships and escort ships in Finnish sea under ice condition. In addition, some scholars analyze the main causes of collision accident through analyze accident reports [28,29]. It can be seen that ice conditions have a major impact on ship operation safety, and studies on maritime traffic safety under the influence of ice condition have been carried out in depth from multiple perspectives.

In the current analysis of ship-ice accident risk reasoning, relevant scholars pay a lot of attention to finding key risk factors and their relationship, but, a key issue is overlooked, maritime traffic in the Arctic waters is a typical dynamic process, the association effects of risk factor proposed in research [30] should also exist in the study of maritime traffic risk assessment. Thus, we propose the dynamic association (DA) effect of risk factor. Focusing on the impact of sea ice on ship Arctic navigation risk, we analyze the ship-ice collision accident risk under sea ice status dynamic association (SDA), which is of positive significance for advancing maritime traffic risk research in Arctic waters.

In the field of maritime traffic risk research, the commonly used analysis methods include fault tree [31,32], event tree [33,34], analytical hierarchy process method [35,36], and Bayesian analysis methods [37,38]. Among them, Bayesian analysis methods can effectively combine subjective and objective information and are widely used in ship Arctic navigation risk analysis. Fu established a Bayesian prediction model to predict and analyze the risk of ship ice besetting accidents in Arctic waters [39]. BAKSH established a Bayesian risk assessment model for three types of maritime traffic accidents: collisions, grounding and founding in Arctic waters [40]. Khan constructed an object-oriented Bayesian network risk assessment model to analyze the ship-ice collision risk in Arctic waters, and determined the root cause of the collision accident to support ship operation decision-making [41]. Khan used the dynamic Bayesian analysis method to analyze the main risk factors of the Arctic ship-ice collision accidents [42]. These studies have proved the advantages of Bayesian networks in the analysis of evidence information. The risk assessment of ship navigation under the SDA effect contains a lot of uncertainty analysis. Therefore, it is suitable to use the mature method of Bayesian analysis to carry out this research.

In the following parts of this study, we plan to establish a ship-ice collision risk analysis model under the SDA effect. The Bayesian network is used to analyze the dynamic change of maritime traffic risk in the Arctic waters. Besides, sea ice monitoring data in the Arctic waters are used to explore the influence of ice conditions on the risk of ship-ice collisions. In Section 2, we introduce how to perform Bayesian network risk reasoning under SDA. The obtain of relevant data and the calculate of prior probability distribution (PPD) and conditional probability distribution (CPD) in Bayesian risk assessment network are discussed in Section 3. Section 4 discusses the changes that SDA effect brings to ship Arctic navigation risk analysis. Section 5 provides the conclusions of this research effort.

# 2. Materials and Methods 

### 2.1. Risk Definition of Maritime Traffic under Status Association

The dynamic association effect of one risk factor refers to that the risk factor's impact on maritime traffic risk is not only related to the risk factor's current state, but also related to the risk factor's state in the past time. The DA effect of one risk factor can be expressed by Equation (1). Under the DA effect, a cumulative effect will occur in the risk factor, thereby forming a dynamically associated risk factor $T$. Among them, $S_{n}$ refers to the $n$-th risk factor, $S^{i}{ }_{n}$ refers to the $i$-th state of the $n$-th risk factor, t refers to the occurrences of DA effects of risk factor $S_{n}$, and the number of states of $T$ is $i^{t}$.

$$
T=\sum_{t=1}^{m}\left(S_{n}^{i}\right)_{t}
$$

Risk refers to the occurrence probability of accident [43]. The ship-ice collision in Arctic waters is caused by a series of risk factors. Under the DA effect of one risk factor, the maritime traffic risk in Arctic waters can be expressed by Equation (2):

$$
R=P\left(f\left(S_{1}, S_{2}, \ldots, S_{n-1}, T\right)\right)
$$

Among them, $R$ is the risk value of a risk factor in a ship-ice collision accident, and its value is equal to the probability of occurrence of the risk factor $S$ is the sub-factor that affects the risk factor, $T$ represents the DA effect of one risk factor, and $f$ is the coupling relationship between the risk factor to be assessed and its sub-factors.

# 2.2. Risk Factors Network Structure on Ship-Ice Collision 

The accident causation theory can explain why and how accidents happen [44], and risk analysis is often based on this. In the causation analysis of ship collision accidents, part of the research is based on the large number of ship traffic accidents reports that have occurred [45,46]. In the causation analysis of accidents, ship traffic accident reports are often a small proportion. It is an effective way to infer the logical relationship of risk factors through the subjective judgment of experts [47]. And it is often encouraged by the International Maritime Organization [48].

Combining the analysis of the main causes of maritime traffic accidents in Arctic waters from 1993 to 2001 in [17], and the risk reasoning of ship-ice collision accidents in Arctic waters in [24]. We analyzed the risk factors that influence ship-ice collision accidents based on expert knowledge. Detail information about risk factors is refereed as Table 1. The risk factors that influence the occurrence of ship-ice collision accidents are divided into three types: initial events (X), intermediate events (M) and target event (N).

Table 1. Basic factors nodes in risk reasoning network.


Refer to the risk factors and relationships of ship-ice collision accident risk assessment in [22-24], the relationship between the risk factors is logically analyzed. Regarding the influence of ice condition, it is believed that SDA determines the degree of threat by sea ice, and the cumulative effect it produces may affect human. Based on this, the logical

relationship of the risk factors cause ship-ice collision accident in the Arctic waters is analyzed, and the Bayesian network of ship-ice collision risk assessment for ship Arctic navigation is constructed, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Bayesian network structure of maritime traffic risk in Arctic waters.
In the ship-ice collision accident risk assessment Bayesian network, N represents the ship-ice collision accident, according to whether the accident occurs, its status is divided into yes or no. M represents the intermediate process in which N is triggered by X , and divides its state into increase, constant, or decrease, which means that the probability of occurrence of M increases, constant, or decreases after X occurs.

# 2.3. Status Dynamic Association on Ship-Ice Collision 

According to the influence of ice condition on the safety of maritime traffic, the influence of ice condition is expressed by No Adverse Impact (NAI) and Have Adverse Impact (HAI), respectively. NAI means that the influence of ice condition on the navigation safety of ship can be ignored, and HAI means the ice encountered by ship will have an impact on the safety of maritime traffic. With reference to the International Code for Ships Operating in Polar Waters (polar code) for maritime traffic in the Arctic waters [49], it is assumed that when the sea ice concentration (SIC) is below $48 \%$, the impact of SIC is NAI, and the SIC is above $48 \%$, the impact of SIC is HAI. This study assumes that the human's response to ice condition during ship's voyage is only affected by ice conditions for two consecutive days (the current day and the previous day). Therefore, $I=2, t=2$, the state of SDA can be expressed by Equation (3). In the set of $X$, the state of initial events except $X 1$ are divided into "yes" or "no", according to whether the event occurs:

$$
X_{1}^{e}=\{N A I-N A I, N A I-H A I, H A I-N A I, H A I-H A I\}
$$

### 2.4. Reasoning Method of Node Parameter in Factors Correlation Network

2.4.1. Bayesian Inference Method of Ship-Ice Collision Risk

According to Equation (2), we can know that in ship-ice collision accident, the risk of a factor is caused by other risk factors. The Bayesian inference process of risk can be expressed by Equation (4):

$$
P\left(S_{n}, \operatorname{parents}\left(S_{n}\right)\right)=\sum P\left(S_{n} \mid \operatorname{parents}\left(S_{n}\right)\right) p\left(\operatorname{parents}\left(S_{n}\right)\right)
$$

Among them, $P\left(\right.$ parents $\left.\left(S_{n}\right)\right)$ called PPD, $P\left(S_{n} \mid\right.$ parents $\left(S_{n}\right)$ ) refers to the probability of $S_{n}$ obtained under certain evidence information parents $\left(S_{n}\right)$, called CPD, which is used to describe the process of generating data $S_{n}$.

From Figure 1, we can know that the occurrence of the ship-ice collision accident (N1) is directly caused by the risk event $M 1, M 4$, and $M 9$. According to Equation (4), the Bayesian inference process of N1can be represented by Equation (5):

$$
\begin{aligned}
R(N 1) & =P(N 1, \operatorname{parents}(N 1))=P(N 1, M)=\sum_{M} P(N 1 \mid M) P(M) \\
& =P(N 1 \mid M 1) P(M 1)+P(N 1 \mid M 4) P(M 4)+P(N 1 \mid M 9) P(M 9)
\end{aligned}
$$

In the process of solving Equation (5), since the event M is an intermediate event, its PPD cannot be directly obtained. It is necessary to find all the parent nodes that affect the occurrence of $M$, in turn until the initial event $X$ appears, and then use Equation (4) to perform joint inference. In order to simplify this calculation process, the chain rule of CPD is introduced to solve it. The solution to the joint probability of risk events $\left\{S_{1}, S_{2}, \ldots, S_{n}\right\}$ can be calculated by Equation (6):

$$
\begin{aligned}
P\left(S_{1}, S_{2}, \ldots, S_{n}\right) & =P\left(S_{n} \mid S_{n-1}, \ldots, S_{1}\right) P\left(S_{n-1}, \ldots, S_{1}\right) \\
& =P\left(S_{n} \mid S_{n-1}, \ldots, S_{1}\right) P\left(S_{n-1} \mid S_{n-2}, \ldots, S_{1}\right) P\left(S_{n-2}, \ldots, S_{1}\right) \\
& =P\left(S_{n} \mid S_{n-1}, \ldots, S_{1}\right) P\left(S_{n-1} \mid S_{n-2}, \ldots, S_{1}\right) \ldots P\left(S_{2} \mid S_{1}\right) P\left(S_{1}\right) \\
& =P\left(S_{1}\right) \prod_{j=2}^{n} P\left(S_{j} \mid \operatorname{parents}\left(S_{j}\right)\right)
\end{aligned}
$$

According to Equations (4)-(6), the Bayesian risk inference process of N1 can be expressed by Equation (7):

$$
\begin{aligned}
R(N 1) & =P(N 1, M, X)=P(N 1 \mid M, X) P(M, X) \\
& =P(N 1 \mid M, X) P(M \mid X) P(X) \\
& =\sum_{k=1}^{14} P\left(X_{k}\right) \Pi P(N 1 \mid \text { parents }(N 1))
\end{aligned}
$$

# 2.4.2. Bayesian Method of Risk Inference under Evidence Information 

In risk analysis, it is often necessary to perform reverse reasoning, that is, according to the evidence information of the child node, reverse the probability change of the parent node. The Bayesian reasoning method of this process is expressed by Equation (8):

$$
P\left(\operatorname{parents}\left(S_{n}\right) \mid S_{n}\right)=\frac{P\left(S_{n} \mid \operatorname{parents}\left(S_{n}\right)\right)}{p\left(S_{n}\right)} P\left(\operatorname{parents}\left(S_{n}\right)\right)
$$

Among them, $P\left(\right.$ parents $\left.\left(S_{n}\right) \mid S_{n}\right)$ is called posterior probability distribution (PoD), which represents the probability of occurrence of risk event parents $\left(S_{n}\right)$ after the evidence update, which is the required event probability. $P\left(S_{n}\right)$ represents the probability of event $S_{n}$ under any hypothesis, which called standardized constant.

In the Bayesian network structure of Figure 1, the occurrence of X1 will directly affect M1, and then indirectly lead to the occurrence of N1. Take the Bayesian inference of this process as an example. The main purpose of this reasoning process is to analyze the degree of change in each state of $X 1$ when $N_{1}^{\text {ivyes }}$, so as to find the state that has a greater impact on the collision accident. Since N1 and X1 are indirect relationships in the Bayesian network structure and cannot be solved directly, they need to be solved jointly with the Equation (6) on the basis of Equation (8). The calculation process is shown in Equation (9), where the solution of $P(N 1)$ is referred to Equation (7):

$$
P\left(X 1 \mid N_{1}^{i=\text { yes }}\right)=P(X 1) \frac{P\left(N_{1}^{i=\text { yes }} \mid X 1\right)}{p\left(N_{1}^{i=\text { yes }}\right)}=\frac{P\left(N_{1}^{i=\text { yes }} \mid X 1, M 1\right) P(M 1 \mid X 1) P(X 1)}{\sum_{k=1}^{14} P\left(X_{k}\right) \Pi P\left(N_{1}^{i=\text { yes }} \mid \text { parents }(N 1)\right)}
$$

# 2.4.3. The Calculation Approach of Factors Network Parameters 

The necessary parameters for Bayesian network inference include PPD $P\left(S_{n}\right)$ and likelihood $P\left(S_{n-1} \mid S_{n}\right)$. Other parameters can be calculated after these two parameters are known. In addition to the method of mathematical statistics, the solution of $S_{n}$ needs to be solved by subjective judgment in most cases. Among them, the calculation of mathematical statistics method is shown in Equation (10):

$$
P\left(S_{n}^{i=h}\right)=\frac{A\left(S_{n}^{i=h}\right)}{\sum A\left(S_{n}^{i}\right)}
$$

Among them, $\sum A\left(S_{n}^{i}\right)$ represents the frequency of occurrence of all states in risk factor $S_{n}$, and $i=h$ represents the $h$-th state among all $i$ states of the risk factor $S$.
$P\left(S_{n-1} \mid S_{n}\right)$ is the CPD calculation under certain information. In Bayesian analysis, it is usually judged based on experience. Since experts often come from different fields, they are different in age, experience, and knowledge reserves, and judgments on the results are also different. The Dempster-Shafer (D-S) theory has great advantages in dealing with the joint solution of multi-source information fusion, so, a CPD calculation method based on the D-S theory is proposed. First, define the universe of discourse in the form of a combination of CPD between the states of two directly related nodes in the Bayesian network, as shown in Equation (11), $\alpha$ represents the CPD function between two states of two nodes:

$$
\Theta=\left\{\alpha_{1}, \alpha_{2}, \ldots \alpha_{n}\right\}
$$

On this basis, define the mass function on the universe, and each mass function represents an expert's scoring of CPD. In a mass function, $m(\phi)=0, \sum_{\alpha \subseteq \Theta} m(\alpha)=1$ needs to be satisfied. For the scoring opinions of multiple experts, that means multiple mass functions, represented by $m_{1}, m_{2}, \ldots, m_{n}$ and their synthesis rules are denoted by Equation (12). By combining the opinions of multiple experts, a CPD between two nodes with mutual dependence is obtained:

$$
\begin{gathered}
m_{1} \oplus m_{2} \cdots \oplus m_{n}(\alpha)=K \sum_{\alpha_{1} \cap \alpha_{2} \cap \ldots \cap \alpha_{n}=\alpha} m_{1}\left(\alpha_{1}\right) \cdot m_{2}\left(\alpha_{2}\right) \ldots m_{n}\left(\alpha_{n}\right) \\
K^{-1}=\sum_{\alpha_{1} \cap \alpha_{2} \cap \ldots \cap \alpha_{n} \neq \phi} m_{1}\left(\alpha_{1}\right) \cdot m_{2}\left(\alpha_{2}\right) \ldots m_{n}\left(\alpha_{n}\right) \\
=1-\sum_{\alpha_{1} \cap \alpha_{2} \cap \ldots \cap \alpha_{n}=\phi} m_{1}\left(\alpha_{1}\right) \cdot m_{2}\left(\alpha_{2}\right) \ldots m_{n}\left(\alpha_{n}\right)
\end{gathered}
$$

### 2.5. Data Collection

Maritime traffic in Arctic waters will tend to the central area [14,50], so we select a hypothetical trans-Arctic route and take maritime traffic risk on this route as the assessment object, which is provided by [51], as shown in Figure 2. Based on the maritime traffic information for five consecutive days on this route, the ship-ice collision risk on this route is analyzed.

![img-1.jpeg](img-1.jpeg)

Figure 2. The selected route and ship's position change information.

# 2.5.1. Prior Probability Distribution of Factors Network Parameters 

The database of the National Snow \& Ice Data Center (NSIDC) contains a variety of physical data information in the Arctic waters. According to the needs of this research, satellite platforms DMSP 5D-3/F17 and DMSP 5D-3/F18 are selected and the "Near-RealTime DMSP SSMIS Daily Polar Gridded Sea Ice Concentrations, Version 1" data product is obtained, and the relevant information is shown in Table 2. The data set divides the Arctic sea ice data into a grid of 448 rows $\times 304$ columns, and the value is the daily average change of SIC within a $25 \mathrm{~km} \times 25 \mathrm{~km}$ spatial coverage area. During data processing, the ship's position information is the point coordinates, and the SIC data is the regional average. The average SIC data of the grid to which the ship's position coordinates belong is used as the SIC data of the ship's location.

Table 2. Basic information of sea ice data.


According to the position coordinate information of the five points and starting point on the selected route, a total of 186 pieces of data on the daily change of SIC in August 2018 for these six positions in the database are extracted, as shown in Figure 3. By analyzing the influence of SIC on the maritime traffic risk, with the SIC value of $48 \%$ as the limit, the original data of SIC is changed into two state discrete data (NAI or HAI). On the basis of the four states of X 1 given in Equation (3), the discrete data of two states is changed to the distribution of four states, and then the PPD of the four states of X 1 is calculated in combination with Equation (10), as shown in Table 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. The daily change of ship's position and dynamic ice condition.

Table 3. Prior probability distribution of ice condition(X1).


The PPDs of other root nodes in the model are obtained by combining other literature (OL) and expert judgment (EJ), as shown in Table 4. EJ relies on five professionals who have rick experience in the shipping industry and are familiar with polar navigation practice. Among them, two experts are captains from the China Polar Research Center, with more than 15 years of ship driving experience, and have long been engaged in the driving operations of the Chinese polar scientific research mission. One expert is a professor from Shanghai Maritime University, he has been engaged in maritime traffic risk research for more than 20 years, and has devoted himself to ship navigation risk research in Arctic waters for the past five years. Another two experts are captains from COSCO Special Transport Group, which is actively engaged in the commercial operation of Arctic routes. The two captains have many experience in Arctic routes. Use the five experts to judge the probability of risk factors, and take the average value of their judgments as actual probability.

Table 4. Prior probability distribution of other root nodes.


# 2.5.2. Conditional Probability Distribution of Factors Network Parameters 

In Bayesian network reasoning, the calculation of CPD mainly relies on expert experience. In Section 2.4.3, the CPD calculation method based on D-S theory is introduced. Since ice condition will directly affect human error, take the calculation of the CPD of SDA's state NAI-HAI on human error as an example. Table 5 shows the scores of the five experts on the human error status of increase, constant, and decrease under the influence of state NAI-HAI.

Table 5. Five experts' scoring opinions on human error under the influence of state NAI-HAI.


In the calculation of CPD in the above situation, according to Equation (9), the universe of discourse is $\Theta=\{$ increase, constant, increase $\}$. According to Equation (13), the consistency coefficient K of five expert opinions is calculated, and on this basis, by utilizing Equation (12), the CPD of the influence of NAI-HAI on human error after the combined opinions of five experts is obtained. In other cases, the calculation methods of CPD are in the same pattern, and finally the CPD of human error under SDA is obtained, as shown in Table 6 .

$$
\begin{aligned}
& K^{-1}=\sum_{\alpha_{1} \cap \alpha_{2} \cap \ldots \cap \alpha_{n} \neq \phi} m_{1}\left(\alpha_{1}\right) \cdot m_{2}\left(\alpha_{2}\right) \ldots m_{n}\left(\alpha_{n}\right) \\
& =m_{1}(\text { increase }) \cdot m_{2}(\text { increase }) \cdot m_{3}(\text { increase }) \cdot m_{4}(\text { increase }) \cdot m_{5}(\text { increase }) \\
& +m_{1}(\text { constant }) \cdot m_{2}(\text { constant }) \cdot m_{3}(\text { constant }) \cdot m_{4}(\text { constant }) \cdot m_{5}(\text { constant }) \\
& +m_{1}(\text { decrease }) \cdot m_{2}(\text { decrease }) \cdot m_{3}(\text { decrease }) \cdot m_{4}(\text { decrease }) \cdot m_{5}(\text { decrease }) \\
& =0.69 * 0.64 * 0.72 * 0.85 * 0.91+0.28 * 0.33 * 0.28 * 0.13 * 0.08 \\
& +0.03 * 0.03 * 0.04 * 0.02 * 0.01=0.246 \\
& K^{-1}=\sum_{\alpha_{1} \cap \alpha_{2} \cap \ldots \cap \alpha_{n} \neq \phi} m_{1}\left(\alpha_{1}\right) \cdot m_{2}\left(\alpha_{2}\right) \ldots m_{n}\left(\alpha_{n}\right) \\
& =m_{1}(\text { increase }) \cdot m_{2}(\text { increase }) \cdot m_{3}(\text { increase }) \cdot m_{4}(\text { increase }) \cdot m_{5}(\text { increase }) \\
& +m_{1}(\text { constant }) \cdot m_{2}(\text { constant }) \cdot m_{3}(\text { constant }) \cdot m_{4}(\text { constant }) \cdot m_{5}(\text { constant }) \\
& +m_{1}(\text { decrease }) \cdot m_{2}(\text { decrease }) \cdot m_{3}(\text { decrease }) \cdot m_{4}(\text { decrease }) \cdot m_{5}(\text { decrease }) \\
& =0.69 * 0.64 * 0.72 * 0.85 * 0.91+0.28 * 0.33 * 0.28 * 0.13 * 0.08 \\
& +0.03 * 0.03 * 0.04 * 0.02 * 0.01=0.246
\end{aligned}
$$

Table 6. Conditional probability distribution of serious ice condition (M1).


## 3. Result

### 3.1. Comparative Analysis of Maritime Traffic Risk

The ship-ice collision accident risk Bayesian network assessment model (AM) in Figure 1 is used to analyze the impact of SDA on ship-ice collision risk. Besides, the node X1 in AM is deleted, and the node M1 and M2 will change to root node. By giving the PPD of node M1 and M2 to establish a sea ice non-associated control model (CM). Figure 4 shows the SDA information at the five positions, and the Bayesian network reasoning result of the ship-ice collision risk through running the AM and the CM, respectively.

![img-3.jpeg](img-3.jpeg)

Figure 4. Risk with or without SDA.
The probability of ship-ice collision on the selected route is around 0.15 . Through the CM, the risk of ship-ice collision accident along the route are $0.16,0.13,0.12,0.16$, and 0.16 . By using the AM, the risk of ship-ice collision accident are $0.2,0.09,0.09,0.14$, and 0.11 . The risk change trends calculated by the two models are basically the same, but at the same location, the model analysis results under the SDA are more sensitive to ice condition. At station A, the risk assessment result of the AM is $32.69 \%$ higher than that of the CM. At station B, C, D, and E, the risk assessment results of the CM are higher than that of the AM, which are $32.33 \%, 27.64 \%, 10.26 \%$, and $30.13 \%$, respectively.

# 3.2. The Impact of Ice Condition on Maritime Traffic Risk 

To further explore the difference of risk assessment results between the AM and the CM, the evidence information of SDA in the AM are set as $\mathrm{P}(\mathrm{NAI}-\mathrm{NAI})=1, \mathrm{P}(\mathrm{NAI}-\mathrm{HAI})=$ $1, \mathrm{P}(\mathrm{HAI}-\mathrm{NAI})=1$, and $\mathrm{P}(\mathrm{HAI}-\mathrm{HAI})=1$, the evidence information in the corresponding CM are $\mathrm{P}(\mathrm{NAI})=1, \mathrm{P}(\mathrm{HAI})=1, \mathrm{P}(\mathrm{NAI})=1$, and $\mathrm{P}(\mathrm{HAI})=1$, respectively. Figure 5 shows the ship-ice collision risk assessment result by updating the model information.
![img-4.jpeg](img-4.jpeg)

Figure 5. Risk assessment results under evidence information of the AM and CM.

According to the risk assessment results of the AM and CM under the evidence information of SDA's each state, with or without SDA effect, maritime traffic risk show obvious differences:
(a) When the evidence information in AM and CM are $\mathrm{P}(\mathrm{NAI}-\mathrm{NAI})=1$ and $\mathrm{P}(\mathrm{NAI})=1$, the risk assessment results are basically the same, and the risk assessment result in the AM is slightly higher than those in the CM.
(b) When the evidence information in AM and CM are $\mathrm{P}(\mathrm{NAI}-\mathrm{HAI})=1$ and $\mathrm{P}(\mathrm{HAI})=1$, the risk assessment result in the AM is significantly higher than that in the CM.
(c) When the evidence information in AM and CM are $\mathrm{P}(\mathrm{HAI}-\mathrm{NAI})=1$ and $\mathrm{P}(\mathrm{NAI})=1$, $\mathrm{P}(\mathrm{HAI}-\mathrm{HAI})=1$ and $\mathrm{P}(\mathrm{HAI})=1$ respectively, the risk assessment results in the AM are lower than those in the CM.
Recalling the ship-ice collision risk assessment results in Figure 4:

- When the ship at station A, the state with a higher probability of SDA is NAI-HAI, which is close to the state of scenario b), so the risk assessment result of the AM is significantly higher than that of the CM.
- When the ship is at station B, C, D, and E respectively, the state with a higher probability of SDA is HAI-HAI, which is close to the state of scenario c), so the risk assessment result in the CM is higher than AM.


# 3.3. Model Validation 

Through increasing the state occurrence probability of SDA's every state in the AM by $10 \%$ and $30 \%$ respectively, observe the changes of PoD for each state in M1 and M2 to analyze the impact of SDA on the ship-ice collision risk, the results of PoDs are shown in Figure 6a-d and Figure 6e-h respectively.
![img-5.jpeg](img-5.jpeg)

Figure 6. The change of PoD in M1 and M2 under the variation of SDA. Among them, (a-d) means that the SDA states of NAI-NAI, NAI-HAI, HAI-NAI, and HAI-HAI increase by $10 \%$ respectively, (e-h) means that the SDA states of NAI-NAI, NAI-HAI, HAI-NAI, and HAI-HAI increase by $30 \%$ respectively.

With the increase in the occurrence probability of NAI-NAI, the occurrence probability of M2 is likely to increase, while the occurrence probability of M1 remains stable, indicating that the vigilance of ship operators will decrease under the continuous state of no ice threat, resulting in a slightly higher navigation risk, but the navigation risk is still far lower than in other states. The increase in the occurrence probability of NAI-HAI will cause

the occurrence probability of M1 and M2 to increase at the same time, indicating that the sudden sea ice threat affects navigation safety at the same time on M1 and M2, and ship operators are insufficiently prepared to respond to sudden sea ice threats. When the occurrence probability of state HAI-NAI increases, the occurrence probability of M1 and M2 will decrease instead, indicating that the sudden disappearance of sea ice threat will have a negative effect on M1 and M2, and ship operators are still on sea ice threat alert status. Under the increase in the occurrence probability of HAI-HAI, the occurrence probability of M1 remains unchanged, but the occurrence probability of M2 is likely to decrease, indicating that when the sea ice threat continues to exist, ship operators will maintain the sea ice threat alert state, which will reduce the maritime traffic risk. However, the overall navigation risk under HAI-HAI of is still high.

The ship-ice collision risk analysis under the SDA can reflect the influence of the status change of human on the navigation risk under the change of SIC. During the navigation, it needs to be extra vigilant of the SDA status of NAI-HAI and HAI-HAI.

# 4. Discussion 

In relevant studies, researchers often pay attention to risk factors' relationships and analyze risk factors' comprehensive effects through different methods and models to assess maritime traffic risk [52,53], but maritime traffic is a dynamic process, and humans on board continuously adapt to various maritime traffic environments during the navigation process, so, their adaptability to the state of risk factors will also change accordingly. This means that even the same risk factor status, under different association modes, will have different effects on maritime traffic risks. Therefore, we propose a DA effect of risk factor's state, in which we pay attention to the impact of risk factor's state changes with time on maritime traffic risk. To assess the maritime traffic risk in Arctic waters under DA effect, based on the ship-ice collision risk behavior under the influence of dynamic sea ice, we establish a Bayesian network model of ship-ice collision risk with multi-factor coupling to explore the Impact of SDA to ship-ice collision accident risk. Combined with the SIC sample data of the trans-Arctic route in Arctic waters, the proposed model reveals the general regulation of the dynamic risk for ship Arctic navigation under SIC. Under the DA effect of risk factor's state, the perception of maritime traffic risk has also changed. Results show that the AM's response to different SDA effects is robust, and the SDA effect has a positive impact on the manifestations of human error and serious ice condition. The ship-ice collision risk under SIC is formed through SDA.

The impact of association effects on driving is more in road traffic safety research. Because in-vehicle information systems (IVIS) are widely used in vehicles, drivers continuous use the IVIS during driving will form behavioral adaptation effects [54]. Some drivers perform risky driving because of excessive participation in IVIS during driving, but, some drivers respond positively to the safety assistance in IVIS to improve driving safety. Relevant research found that under an advanced driver assistance system (ADAS), drivers would stop at intersections less frequently, and the speed would increase, which is not conducive to driving safety [55]. These studies all show that drivers will display behavioral adaptation for consecutive events, which will have a positive or negative impact on driving safety. According to the phenomenon that the drivers appear in the driving process, we propose the influence of the risk factor's DA effect on the maritime traffic risk, which means that the navigation risk is not only affected by the risk factors of its current state, but also formed by the cumulative effect of the risk factors in the time series.

Based on this, we analyzed the impact of SDA effect on ship-ice collision accidents in Arctic waters through the Bayesian risk assessment model. In related research, the conclusion generally believes that SIC is the main factor affecting navigation risk [35,56]. In the maritime traffic risk assessment results of CM in Figure 5 also verify the rationality of this statement. However, through the further in-depth study of this research, we found that the impact of SIC on maritime traffic risk is not as simple as the presence of sea ice threat cause the high navigation risk, and the absence of sea ice threat lead the low navigation

risk. Through the influence of SDA status on the ship-ice collision accident risk in Figure 5, and the influence of SDA status on human error in Figure 6, we can find that the SDA effect of NAI-NAI and HAI-NAI both indicate that the current state of the ship is no sea ice threat, but the risk assessment result of the ship-ice collision accident under the association state NAI-NAI is higher than the association state HAI-NAI. This is mainly due to the fact that in the NAI-NAI state, ship operators have adapted to the navigation environment without sea ice threats, thereby increasing the probability of human error and leading to the increase of navigation risk. The SDA effect NAI-HAI and HAI-HAI both indicate that the current state of the ship is threatened by sea ice, but the risk assessment result of ship-ice collision accident in the association state NAI-HAI is significantly higher than that in the association state HAI-HAI. The main reason is that in the state of NAI-HAI, ship operators have adapted to the navigation environment without sea ice threats, and are insufficiently prepared for sudden sea ice threats, which leads to a high growth in navigation risk.

In this study, we calculated the occurrence probability of risk nodes X 1 and M 1 in the ship-ice collision accident risk Bayesian network assessment model based on the sea ice concentration data monitored by satellites. Limited by the availability of data related to maritime traffic in Arctic waters, the conditional probability of node M2 is obtained through expert knowledge, and the prior probability of other nodes is obtained through reference to other researches and expert knowledge judgments, which may have a certain impact on the objectivity of the model assessment results. However, through model testing, we found that the constructed ship-ice collision accident assessment model for maritime traffic in Arctic waters is highly sensitive. With the addition of more monitoring data, the constructed model can be well applied to guide ships navigate in Arctic waters under ice conditions.

Through this research, we apply the proposed DA effect of risk factors to maritime traffic risk assessment in Arctic waters. With the risk analysis of ship-ice collision accidents in Arctic waters under the influence of DA effect, we recognize that in a ship-ice collision accident, the threat of SIC will affect the ship, and the DA effect produced by SIC will affect the adaptation of ship operators. Therefore, maritime traffic risks in Arctic waters are complex and volatile. The SDA effect has a positive effect on our further understanding of the causes of ship-ice collisions in Arctic waters. In order to effectively reduce the risk of ships navigate in Arctic waters, the ship management department can focus on training crews to maintain a good mental state in conducting crew training for Arctic navigation, so as to overcome the adaptability that occurs during maritime traffic practice.

# 5. Conclusions 

This paper has argued that maritime traffic risk is caused by the dynamic association (DA) effect of the risk factor's state in the time series. Bayesian networks can obtain the inference model of risk forming factors through parameter learning and structure learning, and the risk decision-making can be optimized through the new state design of risk factor nodes. Based on the Bayesian network analysis method, the logical relationship between factors can be reflected, and the impact of DA effect can be expressed. The establishment of the Bayesian network model for the risk assessment of ship-ice collision accidents in Arctic waters is under the influence of sea ice status dynamic association (SDA) effect. Through Bayesian network reasoning, different forms of SDA have different threats to the occurrence possibility of human error and serious ice condition. The SDA is more obvious in the form of "No Adverse Impact (NAI)-Have Adverse Impact (HAI)" and "Have Adverse Impact (HAI)-Have Adverse Impact (HAI)".

Objectively understanding risks and analyzing their causes are an important part of realizing risk prevention. This study has shown that on the basis of analyzing the logical relationship between risk factors of the ship-ice collision accident, and introducing the DA effect into the maritime traffic risk assessment model, we have a deeper understanding of the cause of the ship-ice collision accident risk, which will promote the discovery of the objective regulations of maritime traffic risk changes in Arctic waters. Through the

new understanding of maritime traffic risks in Arctic waters, when carrying out relevant crew safety operation training, the crew can be targeted to realize that they will have adaptability during Arctic navigation operations, and then they can actively overcome them psychologically to achieve the improve of maritime traffic safety.

A limitation of this study is that the SDA effect of sea ice concentration (SIC) considered in this study are only two consecutive days in the discrete state (SIC state of the previous day on the current day) and only the impact of SDA on maritime traffic risk was considered. maritime traffic is a continuous process and there will be multiple risk factors that have DA effects, so the DA effect in maritime traffic risk assessment model should also be continuous repeated in multiple times and risk factors. In the next study, it is necessary to consider the impact of the cumulative association effect produced by the continuous changes of multiple risk factors in the time series on the maritime traffic risk.

Author Contributions: Conceptualization, G.G. and S.H.; methodology, S.H. and Z.L.; software, Z.L.; original draft preparation, Z.L.; validation, S.H., Z.L. and C.Y.; data curation, G.G. and C.Y. and Z.L.; review and editing, Y.X., S.F., G.G., and S.H.; funding acquisition, S.F. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by National Science Foundation of China (NSFC), grant number 51709168.

Institutional Review Board Statement: "Not applicable" for studies not involving humans or animals.
Informed Consent Statement: "Not applicable" for studies not involving humans.
Data Availability Statement: The data presented in this study are available on request from the corresponding author.
Acknowledgments: The authors express thanks to the NSIDC for their sea ice data. We would also like to acknowledge the insight contributions from anonymous reviewers whose thoughtful comments have helped to improve an earlier version of this paper.
Conflicts of Interest: The authors declare no conflict of interest.
