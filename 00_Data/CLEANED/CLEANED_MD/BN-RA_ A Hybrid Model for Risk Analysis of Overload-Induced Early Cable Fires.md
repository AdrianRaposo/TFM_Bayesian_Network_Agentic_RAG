# Article 

## BN-RA: A Hybrid Model for Risk Analysis of Overload-Induced Early Cable Fires

Xiaolong Chen ${ }^{1}$, Guozhong Huang ${ }^{1}$, Xuehong Gao ${ }^{1, *}$, Shengnan Ou ${ }^{1}$, Yatao $\mathrm{Li}^{2}$ and Ibrahim M. Hezam ${ }^{3}$ (D)<br>check for updates

Citation: Chen, X.; Huang, G.; Gao, X.; Ou, S.; Li, Y.; Hezam, I.M. BN-RA: A Hybrid Model for Risk Analysis of Overload-Induced Early Cable Fires. Appl. Sci. 2021, 11, 8922. https:// doi.org/10.3390/app11198922

Academic Editor: Alfio Dario Grasso

Received: 3 September 2021
Accepted: 22 September 2021
Published: 24 September 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0) 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Research Institute of Macro-Safety Science, School of Civil \& Resource Engineering, University of Science and Technology Beijing, Beijing 100083, China; g20198124@xs.ustb.edu.cn (X.C.); hjxhuanggz@ustb.edu.cn (G.H.); osn@ustb.edu.cn (S.O.)
2 Department of Civil and Earth Resources Engineering, Graduate School of Engineering, Katsura Campus, Kyoto University, Kyoto 615-8540, Japan; li.yatao@b.mbox.nagoya-u.ac.jp
3 Department of Statistics \& Operations Research, College of Sciences, King Saud University, Riyadh 4545, Saudi Arabia; ialmishnanah@ksu.edu.sa

* Correspondence: gaoxh2020@ustb.edu.cn

Abstract: Cable overload is one of the most critical contributors to early cable fires. This study proposes a hybrid Bayesian network (BN)-based fire risk analysis model, to investigate the evolution of overload-induced early cable fire risks. In particular, the fire risk transmission paths caused by cable overload are reported, considering the critical factors that likely lead to fires. A BN with a specific structure was considered using the fire risk transmission paths. Later, given the risk index system, a hybrid fire risk assessment model caused by cable overload was developed based on the entropy weight method. Subsequently, the corresponding risk levels were evaluated based on the evolution of the fire risk, using numerical simulations. Finally, a case study was conducted to validate the proposed methods, and the results indicated that the proposed methods can effectively evaluate the state of the cable and explain the causes of fire risk, which can be used for early fire warnings.

Keywords: Bayesian network; cable overload; fire; risk transmission; risk assessment

## 1. Introduction

Electrical wires and cables are important power conduits, supporting the rapidly evolving energy needs of modern societies. Facing the explosive growth of the urban population, electrical wires and cables carry more power than before, which results in faster wire aging and corrosion. At the same time, the numbers of fires, victims, and property damage cases caused by wire- and cable-related disasters were the highest among all types of electrical products [1]. In the United States alone, it was reported that half of the domestic fire incidents from 2012 to 2016 were caused by various cable factors (i.e., power distribution and/or lighting) [2]. Compared with the United States, China is confronted with a more serious situation. There are 587,000 electrical fire-related disasters that occurred in China from 2015 to 2020, accounting for a large proportion of all incidents. In this sense, to prevent the serious consequences of cable fires, the mechanisms underlying cable fires should be explored, and fire risk analysis models should be developed for providing early fire warnings.

It is widely acknowledged that cable fires usually result in secondary hazards with much more damage, such as smoke, poison gas, dust explosion, and gas explosion. Accordingly, many researchers have paid attention to experimental, monitoring, risk analysis, investigative, and other aspects of cable fires, because these often result in great loss of life and property [3]. However, most of the existing studies have only focused on the mechanisms of cable fires, applications to prevention and early warnings, and analysis of consequences. Compared with the studies of the effects of cable fires after their occurrence, research on the early evolution of cable fires has not received sufficient attention. Conse-

quently, this study focuses on analyzing the risk of overload-induced early fires from the perspective of cable fire risk transmission paths based on a Bayesian network (BN).

To estimate the risk level of overload-induced early cable fires, this study proposes a novel BN-based hybrid fire risk assessment model. First, the evolution of the cable overload fire risk is studied; then, a BN with a specific structure is proposed for presenting the evolution process. Subsequently, the prior probabilities of basic factors are explored, and the conditional probabilities of network nodes are determined based on cable-temperaturerise experiments. In addition, given the risk index system and combined with the entropy weighting method, the risk assessment model of overload-induced early cable fires is established, and the risk level is estimated based on the numerical simulations of risk evolution. The results show that the proposed model can evaluate the overload fire risk states of cables and infer the causes of the risk states. To address the aforementioned concerns and research gaps, this study focuses on the overload-induced early cable fire risk analysis, based on the proposed BN and considering the effects of mechanical damage, cable aging, and other factors.

The remainder of this paper is organized as follows. Section 2 reviews and discusses previous studies and the main concerns of this study, where the existing research gaps are identified. Section 3 constructs the cable overload-induced early cable fire BN, based on the risk transmission of early cable fires. To formulate the cable fire risk using the BN, a cable overload coupling experiment was conducted for investigating the causes of the cable temperature in the case of the cable overload. To assess the early cable fire risk, a risk index system combined with the entropy weighting method is developed in Section 4. Furthermore, to validate the effectiveness of the proposed method, a case study and its computational results are presented in Section 5. Finally, Section 6 concludes the paper by providing valuable insights and by highlighting future directions.

# 2. Literature Review 

Regarding the main concerns associated with the cable fire risk assessment, we position this study within the following main streams of the literature.

### 2.1. Cable Fire Mechanisms

Many studies have addressed the ignition and combustion mechanisms of cable fires, by a large number of experimental analyses. For instance, Babrauskas [4,5] and Zhang [6], investigated the mechanisms of cable fires caused by arc faults, overheating of cable cores, and external heating. Courty [7] and Fisher [8], revealed the ignition mechanisms and failure criteria of cable fires by performing cable fire characterization experiments. Shea [9] investigated cable fires caused by cable looseness or corrosion, high resistance connection, and wire insulation moisture absorption. Xie [10], Shu [11], and Zhang [12], studied the influence of polyvinyl chloride (PVC) cable aging on the fire risk. The above studies revealed that the mechanisms of cable fires were associated with intrinsic factors. However, the occurrence of cable fires is generally attributed to a complex combination of factors. Moreover, conventional methods cannot simultaneously predict the occurrence probability and the consequences of cable fires. In this sense, a cable risk analysis model should be implemented, for incorporating the impact of multi-factor coupling and for quantifying the occurrence probability and the severity of fire consequences.

### 2.2. Impact of Cable Overload on Cable Fires

It is known that cable overload increases the risk of cable fires, and many studies have addressed this issue. For instance, Yu [13], studied the microstructure of a copper wire arc bead with an overcurrent fault. Gao [14], investigated the fire risk for copper wires under overcurrent fault conditions. He [15], investigated the dripping behavior of the molten thermoplastic insulation of copper wires induced by the flame spreading, for overload currents. Zhang [16], studied the thermal and fire behavior of a polyethylene-insulated

wire under an overload current. Shimizu [17], focused on the ignition of electric wires after a long-term excess current supply under microgravity.

Previous studies have mainly focused on wires ignited by external heat sources, and only a few studies have investigated the characteristics of cable fires induced by current overloads. However, in most realistic fire scenarios, cable fires are expected to start with short-circuiting or a current overload. Fires for cables subjected to strong currents are more common and dangerous. To the best of our knowledge, the study of early cable fire risk analysis for overcurrent energized wires remains nascent.

# 2.3. Methods for Preventing Cable Fires 

To prevent the occurrence of cable fires, detection equipment (i.e., monitors and devices) that provides early warnings should be used. In particular, Parise [18], designed a residual current protector for the active and passive protection of cables. Huang [19], developed a ZigBee monitoring and protection system for electrical safety in buildings. Ping [20], investigated methods for real-time monitoring of temperature elevation episodes in energized transformer cores with distributed optical fiber sensors. Tvs [21], proposed a framework for cable-condition monitoring and for estimating the remaining service life, based on an artificial neural network and the Weibull theory.

In addition to the usage of specialized detection equipment, risk analysis offers an effective way to address the main concerns associated with the appearance of cable fires. He [22], proposed a method for quantitative assessment of cable fire risks in utility tunnels, by combining weighted fuzzy Petri nets and event trees. Worrell [23], explored the use of machine learning methods for generating meta-model approximations of a physics-based fire hazard model. Khan [24], proposed a framework for bridge fire risk assessment based on the Analytic hierarchy process. Manan [25], presented a building fire risk analysis model based on scenario clusters. Ding [26], proposed a framework combining two methods (i.e., uncertainty reasoning approach and deterministic modeling approach), to assess the probability of fire accidents. Vanweyenberge [27], described a bow-tie-based risk assessment methodology for tunnel fires involving smoke spread, evacuation, and consequences. Yang [28], proposed a model that combines a Bayesian network (BN) with stochastic Petri nets (SPN), for analyzing the probability of fire accidents in congested and complex processing areas. Chen [29], developed a model that combined quantitative and qualitative methods, for evaluating the risks that accompany fires and pipeline explosions.

### 2.4. Summary

Previous experimental research, which aimed to elucidate the mechanisms underlying the emergence of cable fires, found that cable fires are caused by a complex combination of critical factors. To investigate the underlying processes, risk analysis should be conducted to quantitatively assess the risk level of cable fires. Compared with neural network-based models [30], bow-ties [31], and Petri nets [32], BNs have the advantages of flexible inference and are good at dealing with uncertain relations, not requiring large amounts of data. They are widely used in accident probability analysis [33], accident scenario deduction [34], fault diagnosis [35], and risk assessment [36]. BNs can be used for quantitative analysis using forward and reverse methods [37,38]. Accordingly, to analyze the early risk of cable fires from the risk transmission perspective, the forward and reverse analyses of BNs are applied for risk assessment and risk cause reasoning, respectively. Combined with multi-factor coupling experiments of cable overload fires, the theory of risk transformation, and the BN-based risk assessment, this study proposes a composite early cable fire risk analysis method for investigating the fire risk in energized cables before cable fires, and for inferring the critical factors leading to cable fires.

# 3. Construction of a BN 

### 3.1. Risk Transmission for Overload-Induced Early Cable Fires

In general, the process of risk transmission occurs in four phases: (i) risk incubation, (ii) diffusion, (iii) outbreak, and (iv) extinction [39]. This study focuses on the processes before fire spreading, namely risk incubation and diffusion phases, which correspond to the early evolution and formation stages of fire elements.

The evolution of overload-induced cable fires needs to be explored to prevent risk generation and transmission, which is of great significance for cable fire prevention and early warning. To investigate the overload-induced cable fires' evolution characteristics, three categories of factors are usually considered: (i) basic factors, (ii) intermediate factors, and (iii) fire risk factors. The basic factors are the root causes of cable overheating, which usually include electric currents, cable damage, aging, and environment temperature. These factors directly or indirectly affect the overload fire risk factors through the second category of intermediate factors. The intermediate factor considered in this study, the cable temperature rise, is the bridge connecting the basic factors and the third category of the fire risk factors, which consists of the insulation breakdown, cable heat resource, and material pyrolysis risks.

During the early fire risk evolution, regardless of external factors, the overcurrent is the main culprit of overheating, increasing the cable temperature. In addition, cable aging, mechanical damage, and high ambient temperature are also important factors that increase the cable temperature. In particular, the cable insulation material, PVC, suffers from thermal aging, which irreversibly increases the cable insulation breakdown risk [40]. In addition, the loss of the plasticizer causes the formation of voids in the material, which reduces the insulation breakdown strength [41]. Based on the above considerations, the risk transmission process of overload-induced cable fires in this study is presented in Figure 1. In the cable fire formation stage, electric sparks, high-temperature heat sources, and flammable substances are caused by three risk factors, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Risk transmission paths of overload-induced cable fires.

### 3.2. Risk BN for Overload-Induced Early Cable Fires

BNs were introduced by Dr. Judea Pearl. A BN captures conditional probability relationships based on the Bayesian theorem, and connects the uncertainty relationships

among different events by a directed acyclic graph, thus yielding a causal probability network that contains the transmission paths of events. In Figure 2, a sample BN is shown, where three layers of nodes are connected with directed acyclic arrows. The nodes are considered the model variables, and relationships between variables are represented by directed acyclic arrows. Any sub-node of a given node is called a child node, and the given node is the parent node. Root nodes have no links directed toward them (i.e., they do not have parent nodes), and represent basic events whose probabilities are assigned as prior probabilities. These probabilities are obtained from standard sources of failure data or based on expert elicitation in the case of unavailable failure data. Nodes with no child nodes are called leaf nodes, and are quantified using a conditional probability table (CPT). Both intermediate and leaf nodes are quantified using a CPT, considering the causal dependence between them [42].
![img-1.jpeg](img-1.jpeg)

Figure 2. Basic structure of a BN.
In a BN, according to the inference principle of Bayesian decision theory, the conditional probability of random events $X$ and $Y$ is given by:

$$
P(X \mid Y)=\frac{P(Y \mid X) P(X)}{P(Y)}
$$

where $P(X \mid Y)$ is the probability of occurrence of $X$ when $Y$ occurs.
If event $X_{i}$ leads to event $Y, Y$ is regarded as a child node. After the evidence associated with the child node $Y$ is updated, the posterior probability of the parent node $X_{i}$ is written as:

$$
P\left(X_{i} \mid Y\right)=\frac{P\left(Y \mid X_{i}\right) P\left(X_{i}\right)}{\sum_{i=1}^{n} P\left(Y \mid X_{i}\right) P\left(X_{i}\right)}, i=1,2,3, \ldots, n
$$

If $X_{i}(i=1,2, \ldots, n), n$ events occur, then the occurrence probability of these events is given by the joint probability

$$
P(Y)=P\left(Y \mid X_{1}\right) P\left(X_{1}\right)+P\left(Y \mid X_{2}\right) P\left(X_{2}\right)+\cdots+P\left(Y \mid X_{n}\right) P\left(X_{n}\right)
$$

A BN can be used as a risk analysis model for complex systems [43]. Risk factors are represented as nodes in the BN, and risk transmission is encoded in the directed acyclic graph, yielding a causal probability network that represents the risk evolution process. By calculating conditional probability, the probability of event occurrence and possible consequences can be measured quantitatively. At the same time, a BN can integrate quantitative information from different channels, can deal with continuity and multi-state variables, and can carry out prediction and diagnostic analyses.

To establish an overload-induced early cable fire risk BN model, it is necessary to determine the network structure and parameters. Then, the model BN can be established

according to the early evolution stage of the fire risk transmission paths, as shown in Figure 1. The established BN structure with node states is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Structure of the BN for overload-induced early cable fire risk.

# 3.3. Determination of the BN Parameters 

After constructing a BN, it is necessary to determine the prior probabilities of the root nodes and the conditional probabilities for all pairs of connected nodes in order to specify the relationship between the BN's child and parent nodes.

### 3.3.1. Prior Probabilities of Root Nodes

Root nodes with no parent nodes are the most basic nodes in a BN. The initial state of these root nodes must be determined through empirical decision-making and historical data. In this study, the prior probabilities of root nodes were obtained from the monitoring records of a tobacco distribution center and the historical data of electrical inspection (Table 1). Establishing a CPT relies on the following five rules:
(I) Because of the different properties of the nodes, these nodes are divided into discrete and continuous nodes. To unify the construction of a BN, continuous variables should be discretized and divided into different discrete intervals, where each discrete interval represents the state of the corresponding node.
(II) Cable current node reflects the current through the $0.75 \mathrm{~mm}^{2}$ cross-sectional area of the cable. According to an experimental study on the cable temperature rise, the rated current for this type of cable during normal operation is approximately 7 A .
(III) The degree of mechanical damage indicates the original damage of the cable, that is, the mechanical damage caused by wiring, operation, or animals' gnawing.
(IV) Cable aging is quantified by the aging time. In the temperature rise experiment, the cables aged according to the Arrhenius high-temperature aging model [44], yielding cables with different aging degrees.
(V) Cable working environment temperature is derived from historical records of a tobacco storage and distribution center.

Table 1. Prior probabilities of root nodes.


# 3.3.2. CPT

In a BN, each node has a different state, where each state corresponds to a certain probability. At the same time, a combination of different states of each parent node leading to different states of child nodes also has a certain probability. Accordingly, a CPT based on the nodes' states can be constructed between child nodes and parent nodes with polymorphic uncertainty. In general, conditional probability is determined by the corresponding functional relation, statistical probability, and subjective decision. To obtain the conditional probability relationship of the temperature rise, this study utilized the temperature rise theory and evidence from coupling experiments. (i) Conductor heating theory

When a cable is connected to a constant-current circuit, its inner core conductor generates heat. Owing to the heat transfer, the temperature of the insulation layer will gradually increase with time, and the conductor insulation layer will dissipate heat into the environment around it. The dynamic process of heat dissipation is shown in Figure 4, where the circle indicates the cross-section of a cable.

Heat radiation

Figure 4. Heat generation and dissipation by the cable. In Figure 4, the basic process of heat generation and dissipation by a conductor is presented, where the temperatures of the inner core and ambient are denoted by $T_{c}$ and $T_{0}$, respectively. The physical processes of heat generation and heat dissipation by a conductor follow the law of energy conservation. The temperature rise of the conductor

can be regarded as the difference between heat generation and dissipation, which can be expressed as:

$$
m C \frac{\mathrm{~d} T}{\mathrm{~d} t}=I^{2} R-K_{z h} A\left(T-T_{0}\right)
$$

where $t$ is the time during which the current is applied, $m$ is the linear density of the conductor, $C$ denotes the specific heat capacity of the conductor, $R$ is the core resistance per unit length, $K_{z h}$ is the total heat transfer coefficient between the conductor insulation layer and external environment, $A$ is the surface area of the conductor per unit length.

The temperature rise function can be obtained by solving the first-order differential Equation (4), and the temperature difference, denoted by $\Delta T$, is given by:

$$
\Delta T=\left(T-T_{0}\right)=\frac{I^{2} R}{K_{z h} A}\left[1-\exp \left(-\frac{K_{z h} A t}{m C}\right)\right]+\left(T_{c}-T_{0}\right) \exp \left(-\frac{K_{z h} A t}{m C}\right)
$$

With $T_{P}=\frac{I^{2} R}{K_{z h} A}, T_{n}=\left(T_{c}-T_{0}\right), T_{m}=\frac{m C}{K_{z h} A}$, the above Equation (5) can be written as follows:

$$
\Delta T=T_{P}\left[1-\exp \left(-\frac{t}{T_{m}}\right)\right]+T_{n} \exp \left(-\frac{t}{T_{m}}\right)
$$

Equation (6) gives the conductor temperature rise as a function of time, assuming ideal conditions, and given a certain current. There are three coefficient terms in the temperature rise function: temperature rise equilibrium coefficient $T_{P}$, temperature difference coefficient $T_{n}$, and time coefficient $T_{m}$. In the limit of $t \rightarrow \infty$ in Equation (6), the expression for the temperature difference is given by:

$$
\Delta T=T_{P}=\frac{I^{2} R}{K_{z h} A}
$$

When the heat generation rate of the inner core of the conductor equals the heat dissipation rate of the outer surface of the conductor insulation layer, the conductor is in a balanced state of heat generation and heat dissipation, and its temperature rise is the temperature rise balance coefficient $T_{P}$, where the current $I$ and the total heat transfer coefficient $K_{z h}$ are two important factors. The total heat transfer coefficient for the conductor surface is affected by heat conduction, heat convection, and heat radiation on the conductor surface and environment. Therefore, changing the heat dissipation on the conductor surface, for example, owing to the conductor damage and/or aging, affects the total heat transfer coefficient on the conductor surface.

According to Equation (7), after a sufficiently long time the conductor temperature will eventually stabilize at a certain value, which is called the equilibrium temperature for the specific current. The equilibrium temperature of a conductor can be determined in terms of the equilibrium temperature rise and ambient temperature, as follows:

$$
\begin{gathered}
T_{\text {balance }}-T_{0}=\frac{I^{2} R}{K_{z h} A} \\
T_{\text {balance }}=\frac{I^{2} R}{K_{z h} A}+T_{0}=T_{B}+T_{0}
\end{gathered}
$$

(ii) Coupling experiment of conductor temperature rise

To explore the influence of mechanical damage, aging, and current on the cable temperature increase, an experiment was conducted to test the internal wiring single-core flexible conductor unshielded cable ( 60227 iec 05 BV ) with a cross-sectional area of $0.75 \mathrm{~mm}^{2}$. The equipment used in this experiment is shown in Figure 5. In particular, a grounding resistance tester, TSO6210 (Figure 5a), was used for providing a stable and large constant current. The temperature of the cable surface was measured using a 0.32 mm T-type thermocouple and recorded using an LR8431-30 data acquisition instrument (Figure 5b). A

thermal aging test chamber (Figure 5c) provided a constant-temperature aging environment for aging cable samples.
![img-3.jpeg](img-3.jpeg)
(a) Grounding resistance tester
![img-4.jpeg](img-4.jpeg)
(b) Data acquisition instrument
![img-5.jpeg](img-5.jpeg)
(c) Aging test chamber

Figure 5. Equipment used in this study.
In this study, cables were tested for six currents (i.e., $6,10,13,15,18$, and 20 A ), three levels of mechanical damage (i.e., $50 \%, 75 \%$, and $100 \%$ ), and four aging states (i.e., $6,12,36$, and 60 months). Meanwhile, cables under different damage degrees and aging time are tested under different loading currents, where the cable temperature rise is recorded. To accurately measure the cable temperature and calculate the cable temperature rise, three thermocouple measuring points (i.e., inlet, outlet, and middle end points) are fixed on the conductor, and another measuring point is arranged in the surrounding to record the ambient temperature nearby. For the damaged cable test group, it is necessary to add a temperature measurement point at the damaged conductor edge to monitor its temperature change. Finally, the temperature rise of the cable is obtained by calculating the difference value of cable equilibrium temperature and ambient temperature.

Mechanical damage was modeled as partial insulation that affected heat dissipation, directly exposing the high-temperature core and causing cable overheating. Cable damage was quantified by the angle of the cable local damage; five examples that illustrate different exposed ratios are shown in Figure 6.
![img-6.jpeg](img-6.jpeg)

Figure 6. Illustration of cable damage degrees.
In addition to the mechanical damage, aging affects the structure of the cable insulation layer and its insulation ability and resistance to high temperatures; aging causes cables to overheat easier. In aged cables, overload induces a sharp temperature rise. In this study, an aging model developed by Arrhenius [45], was used for modeling cables with different aging degrees. Regarding the same chemical reaction, the activation energy did not change and the component service life under different temperatures shows an inversely proportional relationship to the exponent of temperature, which is given by:

$$
V=A e^{-\frac{E_{a}}{K T}}
$$

where $V$ : reaction rate, $\mathrm{mol} /\left(\mathrm{m}^{3} \mathrm{~s}\right) ; A$ : constant, known as frequency factor; $E_{a}$ : Activation energy, $0.3-1.2 \mathrm{eV}(1.01 \mathrm{eV}$ for PVC); $T$ : Kelvin temperature, k; $K$ : Boltzmann constant, $K=8.617385 \times 10^{-5}$.

Given a certain product, if the life degradation reaction follows Arrhenius law, the failure rate of the product $\lambda(T)$ is directly proportional to the reaction rate; and the average life $L(T)$ is inversely proportional to the reaction rate $V$, see Equation (11). The acceler-

ation factor, denoted by $A F$, is defined as the ratio of average life under two different temperatures, shown in Equation (12):

$$
\begin{gathered}
\lambda(T)=\frac{1}{L(T)}=A e^{-\frac{T_{u}}{E T}} \\
A F=\frac{L\left(T_{u}\right)}{L\left(T_{t}\right)}=e^{\frac{E_{u}}{R}\left(\frac{T}{T_{u}}-\frac{1}{T_{t}}\right)}
\end{gathered}
$$

where $T_{u}$ : temperature during normal use; $T_{t}$ : accelerated aging temperature; $L\left(T_{u}\right)$ : average life at operating temperature; $L\left(T_{t}\right)$ : average life at accelerated aging temperature.

Regarding the experimental environment, this study followed the recommendations of 60,227 IEC 06 (BV) wires in the PVC wire test standard CB/T5023-2008, where the aging temperature was $80^{\circ} \mathrm{C}$ and the treatment scheme of the test scenario could be obtained (Table 2).

Table 2. Design of accelerated aging time.


The nodes with conditional probability in the BN included the cable temperature rise, insulation breakdown risk, cable heat source risk, and insulation pyrolysis risk. The parent nodes of the cable temperature rise were the current, the damage degree, and the aging time. Based on the experimental data, the fits to the cable temperature dependence on current-damage and current-aging are shown in Figure 7, where the corresponding threedimensional (3D) illustrative diagrams are also shown. In particular, the cable temperature rise caused by currents and damage is shown in Figure 7a, and the cable temperature rise caused by currents and aging is shown in Figure 7b.
![img-7.jpeg](img-7.jpeg)

Figure 7. Fitted relationships: (a) current-damage; (b) current-aging.
It is known that cable aging and mechanical damage involve two independent processes, and the temperature rise function for the coupled model of current, damage, and aging effects is given by:

$$
T_{B}(I, s, a)=\left(p_{1} a^{4}+p_{2} a^{3}+p_{3} a^{2}+p_{4} a+p_{5} s+p_{6}\right) I^{2}+p_{7}
$$

where $T_{B}(I, s, a)$ is the balanced temperature rise under specific current, damage, and aging conditions; $I$ is the current, $s$ is the damage degree, $s \in[0,1]$; and $a$ is the aging time (in months).

Using the least-squares method, the Python data analysis toolkit StatsModels was used for fitting the experimental data, which are available at https://github.com/cxiaolong/ experiments/. The fit results are listed in Table 3.

Table 3. Fit results for $T_{B}(I, s, a)$.


Then, the conditional probability of the cable temperature rise node was calculated using Equation (13), and the cable heat source temperature was determined as the sum of the cable equilibrium temperature rise and the ambient temperature:

$$
T=T_{B}+T_{e}
$$

Because the nodes of the insulation breakdown risk and the material pyrolysis risk are difficult to calculate, the conditional probability remains unknown, although the equation and the relationships are given. In this sense, this study first evaluated the breakdown and pyrolysis of insulating materials based on the phenomena of cable melting, damage, smoke, and peculiar smell during the experiment, and analyzed multiple groups of experimental data to obtain the needed conditional probabilities (Table 4).

Table 4. Conditional probabilities of insulation breakdown risk and material pyrolysis risk.


# 4. Numerical Analysis of the Fire Risk Assessment 

In this study, risk is represented as $f(s, p)$ [46], which is a function of the probability and severity of the consequences of a certain hazardous event. In particular, $R$ represents the total fire risk of the overload-induced early cable fires, $R_{i}$ is the risk index of the $i$-th risk factor, $S_{i j}$ represents the quantitative value of the $j$-th severity in the $i$-th risk factor, and $w_{i}$ represents the weight of the $i$-th risk factor. Then, the cable overload fire risk is:

$$
\begin{gathered}
R_{i}=f_{i}(s, p)=\sum_{j=1}^{n} S_{i j} P_{i j},(i=1,2,3) \\
R=\sum_{i=1}^{m} w_{i} R_{i},(m=3)
\end{gathered}
$$

Based on the risk-establishing BN, the probabilities of different risk factors corresponding to each risk state were obtained. Then, the risk indices of risk factors were obtained from Equation (15), and the overall risk index was computed using Equation (16).

# 4.1. Classification of Risk Factors 

In this study, the overload-induced early cable fires were divided into three risk-factor categories. The severity classes and quantitative rules for the three categories are listed in Table 5.

Table 5. Classification of risk factors with severities.


### 4.2. Determination of the Risk-Factor Weights

Because different categories of risk factors contribute unevenly to the overall fire risk, different priorities (i.e., weights) of these risk factors need to be considered. To determine the weights, three popular methods are usually used: (1) difference-driven, (2) function-driven, and (3) comprehensive set assignment methods [47]. The differencedriven weight determination method was used in this study because it not only retains the data characteristics perfectly but also adapts to the data changes automatically. At the same time, this method can avoid subjectivity in determining the weights, which makes it more scientific and reasonable. Consequently, the entropy weight method based on the difference-driven approach was used for weight analysis. The steps of the entropy weight method are described below.
(i) Data evaluation matrix

The weight judgment of the entropy weight was based on the input data. Before evaluating the data, an evaluation matrix $X_{m \times n}$ must be constructed, consisting of $m$ cases and $n$ indicators, as in:

$$
X_{m \times n}=\left[\begin{array}{ccc}
x_{11} & \cdots & x_{1 n} \\
\vdots & \ddots & \vdots \\
x_{m 1} & \cdots & x_{m n}
\end{array}\right]
$$

(ii) Standardization of the evaluation matrix

Firstly, indicators in the matrix need to be standardized using the following equation:

$$
y_{i j}^{\prime}=\frac{x_{i j}-\min \left(x_{i j}\right)}{\max \left(x_{i j}\right)-\min \left(x_{i j}\right)},(i=1,2, \ldots, m ; j=1,2 \ldots, n)
$$

Then, each element is normalized by:

$$
y_{i j}=\frac{y_{i j}^{\prime}}{\sum_{i=1}^{m} y_{i j}^{\prime}}
$$

The standardized evaluation matrix $Y_{m \times n}$ is given by:

$$
Y_{m \times n}=\left[\begin{array}{ccc}
y_{11} & \cdots & y_{1 n} \\
\vdots & \ddots & \vdots \\
y_{m 1} & \cdots & y_{m n}
\end{array}\right]
$$

(iii) Computation of the information entropy

Given the evaluation matrix $Y_{m \times n}$, the information entropy of each evaluation factor is calculated as:

$$
H_{j}=-k \sum_{i=1}^{m} y_{i j} \log y_{i j}, \quad(i=1,2, \ldots, m ; j=1,2 \ldots, n)
$$

where $H_{j}$ represents the information entropy of factor $j$, and $0<H<1, k=1 / \log m$. It should be noted that the index value of the logarithmic function is not zero; thus, $y_{i j} \log y_{i j}=$ zero when $y_{i j}=0$.
(iv) Calculation of weights

The weight of each factor is calculated according to the information entropy of each index, and is given by:

$$
w_{j}=\frac{1-H_{j}}{n-\sum_{j=1}^{n} H_{j}}
$$

# 4.3. Simulation 

### 4.3.1. Weight Determination of Fire Risk Factors

To determine the weights of risk factors, a numerical dataset was generated using the Netica software based on the constructed BN with its probability relationships. In this study, 70 groups of cases were generated (Table 6).

Table 6. Node states and risk factors generated by Netica.


Using the entropy weight method to calculate the generated node data, the information entropy and weight vectors of three factors were obtained: $H=[0.5962,0.6492,0.8673]$, $w=[0.455,0.395,0.1495]$.

### 4.3.2. Risk-Level Classification Based on the Risk Evolution

By virtue of the flexible inference of the BN and the ability to update the node evidence data, the probability of each root node in the BN was updated, to simulate the change in risk. The probabilities of the sub-node states were obtained by Bayesian reasoning based on the simulated root node states, and then the risk indices were obtained using Equation (4). Figure 8 shows the evolution curve of the risk indices based on the current, aging time, mechanical damage degree, and environment temperature.

![img-8.jpeg](img-8.jpeg)

Figure 8. Risk evolution.
The division of the overall risk level depends on the risk evolution of the risk factors. The change trends of the risk indices for the different factors can be seen as follows:
(i) When the total risk index is below 0.35 , the risks of the three factors are relatively small, and the current indicator is in the state of normal or slight overload; the overload fire risk is relatively low.
(ii) When the total risk index is in the $0.35-0.5$ range, the factors in this range are often in the state of intermediate risk. For example, for currents in the 15-20 A range, the risk index of the cable heat source risk is $R_{1}=0.4342$. According to the explanation of the current overload degrees in Table 4, the current is in the medium-overload state.
(iii) When the total risk index is in the $0.5-0.65$ range, the factors are often in a high-risk state. For example, for 20-25 A currents, the risk index of the cable heat source is $R_{1}=0.6128$, and when the damage rate of mechanical damage is in the $50-75 \%$ range, the risk index of insulation breakdown is $R_{2}=0.694$.
(iv) When the total risk factor is above 0.65 , the basic node states, such as the overcurrent, cable damage, and aging, are close to the edge of fire, the states of all the risk factors are above high risk, and the fire risk of the cable overload is extremely high.
Based on the above rules of risk evolution, the risk index can be categorized into the following four categories, as shown in Table 7.

Table 7. Risk classification table.


# 5. Case Study 

An electrical anomaly record of a tobacco logistics center in Chongqing was selected for BN reasoning and risk assessment. On a certain day, an inspector opened the door of the transformer room during daily inspection, and immediately felt a heatwave gushing out. A wall-mounted thermometer showed that the ambient temperature reached $45^{\circ} \mathrm{C}$, and the temperature inside the transformer equipment, displayed on an LCD panel, was as high as $90^{\circ} \mathrm{C}$. The inspector immediately contacted the equipment control center with the request to reduce the power consumption and turned on the transformer indoor refrigeration and air conditioning for cooling.

### 5.1. BN-Based Reasoning

Based on the description of the case, the following evidence-related information was extracted: when the ambient temperature was $45^{\circ} \mathrm{C}$, the state of the environmental node in the BN was $P\left(35-45^{\circ} \mathrm{C}\right)=1$. The transformer panel showed that the internal temperature was $90^{\circ} \mathrm{C}$; thus, it was assumed that the temperature of the internal line cable was approximately $90^{\circ} \mathrm{C}$, and the state of the temperature node in the BN was $P\left(70-90^{\circ} \mathrm{C}\right)=1$.

These two pieces of information could be obtained directly based on daily inspection, but other information remained unavailable. Because the BN has a strong reasoning function, it can be used for inferring the probability of unknown information based on the known information. Therefore, based on the above two pieces of evidence, the updated state of the BN is shown in Figure 9.
![img-9.jpeg](img-9.jpeg)

Figure 9. Bayesian network reasoning analysis.
According to the inference of the BN posterior probability, some additional information was obtained about that dangerous situation.
(1) The event was mostly owing to a high current. The node of the current changed, and the probability of a normal current (under 10 A ) was 0 , indicating that there must have been an overcurrent in this accident. The likelihood of a serious overload at $20-25$ A could reach $44.5 \%$.
(2) The temperature rise of the cable was obvious. The cable temperature rise node also changed significantly. The probability of the cable temperature rising to less than $25^{\circ} \mathrm{C}$ was 0 . The probability of the cable temperature rising to the $25-40^{\circ} \mathrm{C}$ range was $68.1 \%$, indicating that cable heating was extremely serious, and the risk probability of

insulation breakdown and pyrolysis significantly increased when the cable was in the state of a high-temperature heat source for a long time. The main reason for the risk of overheating is the heating of the cable line rather than the high air temperature.
(3) The cable exhibited the risk of insulation breakdown, and the main cause was cable overheating. The node of the cable mechanical damage changed only weakly, and the probability of no mechanical damage was $94 \%$, indicating that the main cause of the insulation breakdown risk was overheating rather than mechanical damage.

# 5.2. Risk Assessment 

The state probabilities of the three risk factors were determined by the BN-based reasoning and taken as the corresponding risk probabilities, where the corresponding risk indices were obtained by substituting them into Equations (15) and (16). The cable heat source risk was $R_{1}=0.75$, the insulation breakdown risk was $R_{2}=0.5009$, the material pyrolysis risk was $R_{3}=0.4671$, and the total fire risk index was $R=0.6089$, as shown in Figure 10.
![img-10.jpeg](img-10.jpeg)

Figure 10. Risk indices and risk levels for the case study.
According to the above risk index levels, the high-temperature heat source risk level of the overload accident was in the high-risk category, the cable insulation breakdown risk was in the high-risk category, the material pyrolysis risk was in the medium-risk category, and the overall risk level was in the high-risk category. These results were in agreement with the facts of the case.

## 6. Conclusions

To investigate the early fire risk caused by cable overloads, this study proposed a hybrid risk analysis model called BN-RA. Specifically, we investigated the risk transmission paths in overload-induced early cable fires, where the influence of overcurrent, damage, aging, and environment temperature on the risks of early cable fires was mainly considered. A BN was established for estimating the risk transmission paths for overload-induced

early cable fires. The parameters of this risk BN were determined based on the cable overload coupling experiment and data analysis. Combined with the entropy weight method, a risk index-based risk assessment model was proposed for assessing the risk state of overload-induced early cable fires. A numerical simulation was performed for quantifying the associated risk levels. Finally, a case study was implemented for validating the proposed method, and the results indicated that the proposed method can effectively evaluate the state of the cable and elucidate the underlying fire risk mechanisms.

From the established risk transmission paths for overload-induced early cable fires, we determined that the occurrence of overload-induced cable fires is characterized by stages; the early evolution stage is crucial for cable fire prevention and early warning. Overcurrent, mechanical damage, aging, and temperature were the basic factors associated with the cable overload-induced fire risk. From the numerical simulation and entropy weight method analysis, we found that overcurrent is the main factor causing fires, which shows the importance of reducing circuit load and configuring circuit-monitoring devices for cable fire prevention and control. In addition, cable damage can be prevented, cable barriers should be set, and new cables should be replaced regularly to reduce the likelihood of fires caused by cable damage and aging.

Despite these novelties and contributions, there are several potential directions that can be further investigated. This study explored the cable fire risk owing to the cable overload, and proposed a hybrid risk analysis model (i.e., BN-RA). However, there are more dangerous situations that may result in cable fires, such as short circuits, leakage discharges, and poor contacts. Besides, this study only investigates the widely used single core low-voltage PVC cables. However, it is interesting to explore the influence of multi-core cables with different insulation thickness, different installation methods, and high-voltage cables on fire risk in future. At the same time, in this sense, a more comprehensive early risk analysis of cables still requires in-depth studies. In addition, dynamical BNs are expected to be useful for cable fire studies.

Author Contributions: Conceptualization, X.C. and X.G.; methodology, X.C. and X.G.; writingoriginal draft preparation, X.C. and X.G.; writing-review and editing, X.C., X.G., G.H., S.O., Y.L., and I.M.H. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by National Natural Science Foundation of China Grant No. 72104020, and by Researchers Supporting Project number (RSP-2021/389), King Saud University, Riyadh, Saudi Arabia.

Institutional Review Board Statement: No applicable.
Informed Consent Statement: No applicable.
Data Availability Statement: Data are available at my GitHub https://github.com/cxiaolong/ experiments/.

Conflicts of Interest: The authors declare no conflict of interest.
