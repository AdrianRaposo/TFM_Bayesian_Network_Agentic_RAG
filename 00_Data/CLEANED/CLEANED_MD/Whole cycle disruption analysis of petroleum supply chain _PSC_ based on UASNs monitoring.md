# Whole cycle disruption analysis of petroleum supply chain (PSC) based on UASNs monitoring 

Hui Hu, Keqi Chen*, Jing He and Lingbo Du


#### Abstract

This paper proposes a whole cycle analysis method of supply chain disruption based on underwater acoustic sensor networks (UASNs). Firstly, the UASNs are deployed to monitor offshore disruptions (such as oil leakage), and the monitoring data of underwater disruptions can be obtained. Based on the monitoring data, scenario inference and Bayesian network forecasting are applied to reversely infer the upstream causes and probabilities of the disruption, which will provide decision-making basis for the effective prevention of such disruptions in the future. At the same time, based on the monitoring data via UASNs, the DA-NET model of the petroleum supply chain (PSC) system is built and the impact of the disruption on PSC operation is analyzed quantitatively, such as cost increase or time delay. The results show that with disruption monitoring via UASNs, the proposed method can not only infer the causes of a disruption, but also quantitatively determine the impact of the disruption on the operation of PSC, which has certain guiding significance for the enterprise managers of the PSC to prevent such disruptions in advance and to deal with them afterwards.


Keywords: Petroleum supply chain (PSC), Disruption, Underwater acoustic sensor networks (UASNs), Bayesian network, Forecast

## 1 Introduction

Underwater acoustic sensor networks (UASNs) consist of a variable number of sensors and vehicles that are deployed to perform collaborative monitoring tasks over a given sea area. UASNs have become more and more important in ocean exploration applications, such as ocean monitoring, pollution detection, ocean resource management, and underwater device maintenance [1]. As a kind of strategic material, petroleum is significant for the industrial economy and national defense of a country. The uncertain nature and high economic incentives of the petroleum business are driving forces for improvements in the supply chain management. At present, about $80 \%$ petroleum is transported by sea. Inevitably, oil leakage can result in serious contamination of the ocean and shoreline environment and bring huge loss to the enterprises of petroleum supply chain (PSC). Recently, UASNs have

[^0]been used to detect pipeline oil leakage, which is especially significant for the security of PSC. In research area, the existed papers focused on the applications, communication protocols, deployment analysis, and energy management, etc. [2-4]. Modeling and analysis of PSC based on marine disruption monitoring via UASNs is not involved, which is a new research and application area. Therefore, with the function of detecting disruption, UASNs are utilized to infer the causes and probabilities of the disruption and analyze the impact of disruptions on the downstream operation of PSC quantitatively, which is significant for the members of PSC to prevent and cope with the disruption.

When obtaining the monitoring data of the disruption via UASNs, the proposed method can analyze the PSC disruption from a whole cycle perspective, which includes reversely inferring the causes and their probabilities of the disruption, and determine the impact of the disruption on the operation of PSC

[^1]
[^0]:    * Correspondence: 2017222097@chd.edu.cn

    School of Automobile, Chang'an University, Xi'an, China

[^1]:    (c) The Author(s). 2019 Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

members. Thus, we can accumulate experiences of such disruptions and prevent them effectively. On the other hand, known its impact on PSC enterprises, the managers can deal with the disruption more efficiently and decrease the loss after the disruption occurs. To analyze the impact of the disruption, a Petri net-based method called DA-NET is applied, which can illustrate the propagation of disruption and determine the impact of a disruption on the PSC.

## 2 Literature review

UASNs can be used to remotely monitor pipelines, natural gas leaks, equipment condition, and real-time reservoir status. Data gathered by such devices enables new insights into plant operation and innovative solutions that aid the oil, gas, and resources industries in improving platform safety and optimizing operations [5]. Pipeline transportation is the main mode of undersea petroleum transportation, so pipeline leakage is generally detected by negative pressure wave, mass balance, and pressure gradient methods [6, 7]. Compared with the WSNs, the harsh and unpredictable underwater environment is a challenge to UASNs. In addition, UASNs should provide more reliable and stable data transmission over a long period of time. Some problems, such as data collection, trust model, and privacy, have been studied by [8-11]. Nadeem et al. [12] presented an autonomous underwater vehicle-aided efficient data-gathering routing protocol for reliable data delivery in underwater sensor networks. The limited battery resources of UASNs present a challenge for the deployment of such long-term sensor networks. Akyildiz et al. [1] mainly focused on various underwater applications, underwater acoustic communication, and architecture for UASNs. Ribeiro et al. [13] proposed an underwater monitoring system built with sensors distributed over a subsea infrastructure, which was responsible for the operation and transportation of oil production. Besides, the use of the currently available equipment was considered. Data is transmitted by underwater acoustic modems installed on the sensors, platforms, and vessels used for logistic support of the petroleum exploration.

The PSC is very important to the national economic development. Sear [14] constructed a linear programming network model of the PSC and proposed the adjustment strategy of the existing distribution network and production plan under the fluctuation of demand and price. Fernandes et al. [15] presented a stochastic mixed integer linear program (MILP) for PSC design and planning under the demand uncertainty that maximized the expected net present value of a multi-entity multi-product PSC network.

In recent years, disruptions have brought huge loss to supply chain [16-18]. Disruptions are caused by natural disasters (earthquakes, flood, fire, etc.) or human factors (such as terrorist attacks and cyberattacks) [19, 20]. Moreover, supply chains are also affected by their own uncertainties, such as demand fluctuations, supply changes, lead time variability, and exchange rate fluctuations [21]. Fahimnia et al. [22] systematically analyzed and summarized the research on disruption management of global supply chain since 1975. Snyder et al. [23] reviewed the OR/MS literature on supply chain disruptions, organized into six categories: evaluating supply disruptions, strategic decisions, sourcing decisions, contracts and incentives, inventory, and facility location. Regarding the impact of disruptions, Hendricks [24] investigated and calculated 827 supply chain disruptions between 1989 and 2000 and studied the impact of disruptions on enterprises. Tang et al. [25] developed a cascading failure model of risk propagation based on production capability loss. In the model, the network robustness levels under different disruption scenarios were compared. Bandaly et al. [26] studied the impact of lead time variability on the performance of supply chain risk management in the beer industry using operational methods and financial derivatives. At the same time, commodity price risk and demand uncertainty were considered. Hu et al. [27] studied the stability of a supply chain with switched system modeling based on disruption classification. Wu and Blackhurst [28] presented a network-based modeling methodology to determine how disruptions propagated in supply chains and how disruptions affected the supply chain. However, this method only makes a general assumption about whether a node will be interrupted or not and does not consider the probability of node interruption based on the actual situation.

Bayesian network, an uncertain knowledge representation model proposed by Pearl [29] in 1986 to solve uncertainties and incompleteness, has great advantages in solving complex problems caused by uncertainties and correlations. Qiu et al. [30] proposed the merging method of single event Bayesian network with correlation and constructed the Bayesian network model of emergency chain. Barua et al. [31] demonstrated a methodology for mapping the fault tree gates into the Bayesian network and the dynamic Bayesian network. In other areas, Bayesian networks can also make good predictions. Okutan and Yıldız [32] used Bayesian networks to determine the probabilistic influential relationships among software metrics and defect proneness. Didelot et al. [33] inferred a time-labeled phylogeny using Bayesian evolutionary analysis by sampling trees (BEAST), and

then inferred a transmission network via a Monte Carlo Markov chain.

At present, the research mainly focuses on the evolution and evaluation of supply chain disruptions, supply chain contract, network planning, etc., and there is still a lack of research on the interaction mechanism between disruptions and supply chain. For PSC, there is no related research on the causes and impacts of disruption on the system operation. Therefore, this paper combines the Bayesian network forecasting with the DA-NET modeling to analyze the causes and impact of disruptions quantitatively.

## 3 Methodology

By exploring the causal relation between risk factors, a disruption and its impact, a disruption can be analyzed [34]. Accordingly, we construct the causal model of the disruption chain of PSC, as shown in Fig. 1. The input layer is a collection of risk factors, which is composed of all causes and factors of a disruption. The state layer is the disruption, which analyzes the evolution process of the disruption factors. The output layer is the impact layer, which shows the damage of the disruption on the PSC.

The methodology of the paper is shown in Fig. 2. This method consists of three sections: deploying UASNs to obtain disruption monitoring data, inferring the causes and probabilities of the disruption, and analyzing the impact of disruption using the

DA-NET model. Based on the monitoring data via UASNs, the disruption chain is analyzed in the whole cycle. Firstly, the monitoring data of underwater disruptions (such as oil leakage volume and leakage speed) can be obtained by the UASNs. Then, based on the monitoring data of the disruption, the upstream causes and probabilities of the disruption can be inferred by scenario inference and Bayesian network forecasting. Finally, the impact of the disruption on the operation of downstream enterprises can be determined by using the DA-NET modeling method.

### 3.1 Deployment of UASNs and disruption monitoring

UASNs refer to a distributed intelligent network system which consists of many sensors with communication and computing capabilities in the underwater area by self-organizing and completing assigned tasks independently according to the environment. The nodes of the network monitor collect monitoring information with sensors in the distribution area of the network in real time. After data fusion and information processing, the real-time monitoring information is sent to the base station through the underwater nodes with long-distance transmission capability, and then the real-time information is transmitted to the users through the nearshore base station or satellite. The system layout for monitoring oil leakage using the UASNs is shown in Fig. 3.
![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

As shown in Fig. 3, UASNs are composed of underwater nodes, floating nodes in the water, self-moving nodes, and surface transmission nodes. Each node is both a data collecting and a data transferring agent in the network. The UASN protocol consists of the physical layer, data link layer, and network layer.

## 1. Physical layer

In the leak detection system, the negative pressure wave method, pressure gradient method, and other methods combined with the leak detection and positioning technology will be utilized to monitor the real-time data of pipeline. Once
![img-2.jpeg](img-2.jpeg)

the oil leakage occurs, the system will alarm immediately, and the location and volume of the leakage and other related parameters will be recorded.

## 2. Data link layer

It is mainly responsible for transmitting data accurately between two adjacent nodes to ensure point-to-point and point-to-multiple points connections within the sensor network. The designing objective is to enable each underwater node to share bandwidth resources fairly and efficiently while minimizing the time delay and energy consumed.

## 3. Network layer

The task of the network layer is to design an appropriate routing protocol between the source and destination nodes. The node energy of UASNs is very limited, and the communication bandwidth is also limited. Therefore, the design of the routing protocol has a great influence on the network usage time.

Based on the leakage volume detected by the UASNs, the severity of the leakage can be evaluated. Scenario inference is used to determine the causes of the disruption. According to the location of the interruption in the PSC, the Bayesian network is used to forecast the probability of each cause of the disruption, so as to prepare for future prevention and response to such disruptions. At the same time, the monitoring data is input into the DA-NET model to analyze the impact on the downstream supply chain enterprises.

### 3.2 Bayesian network forecasting

Bayesian network, one of the most effective theoretical models in the area of complexity and uncertainty, is a kind of graph model that uses directed acyclic graphs to represent the probability dependencies between variables. Through bottom-up hierarchical analysis, the probability of the causal node is deduced according to the posterior probability of the oil leakage according to the causal chain.

Suppose $x$ is the cause set of causal relation in Bayesian network, and $y$ is the result set of causal relation, then there is $x \rightarrow y$. Each of the set $x$ is $x_{i}$, and $x_{i} \in x(i=1,2, \cdots, n)$.
When a disruption has occurred, we can determine the probability of its cause, as shown in (1).

$$
P\left(x_{i} \mid y\right)=\frac{P\left(x_{i} y\right)}{P(y)}=\frac{P\left(x_{i}\right) P\left(y \mid x_{i}\right)}{\sum_{j=1}^{n} p\left(x_{j}\right) P\left(y \mid x_{i}\right)}
$$

Bayesian network inference implies a premise of conditional independence, that is, for a given node's set of parent nodes, the node is independent to all its
non-descendant nodes. Therefore, the joint probability of all nodes represented by the Bayesian network can be expressed as the product of the conditional probability of each node, then

$$
\begin{aligned}
P\left(x_{1}, x_{2}, \cdots, x_{n}\right) & =\prod_{i=1}^{n} P\left(x_{i} \mid x_{1}, x_{2}, \cdots, x_{i-1}\right) \\
& =\prod_{i=1}^{n} P\left(x_{i} \mid P_{\alpha}\left(x_{i}\right)\right)
\end{aligned}
$$

where $P_{\alpha}\left(x_{i}\right)$ is the parent node set of $x_{i}$.
Dynamic Bayesian network adds time on the basis of static Bayesian network to make reasoning consistent and continuous with the development of events; thus, it is more in line with the reality. A dynamic Bayesian network can be seen as an expansion of a static Bayesian network along the time axis. Suppose that there are $T$ periods, $n$ hidden nodes, and $m$ observation nodes and $x_{i j}$ represents the state of the $i$ th hidden node of the $j$ th period, then there are:

$$
\begin{aligned}
& P\left(x_{11}, x_{12}, \cdots, x_{T 1}, x_{T 2}, \cdots, x_{T n} \mid y_{11}, y_{12}, \cdots, y_{1 m}, \cdots, y_{T 1}, y_{T 2}, \cdots, y_{T m}\right) \\
& =\frac{\prod_{i} P\left(y_{i j} \mid P_{\alpha}\left(y_{i j}\right)\right) \prod_{i, k} P\left(y_{i k} \mid P_{\alpha}\left(y_{i k}\right)\right)}{\sum_{i} \prod_{i, j} P\left(y_{i j} \mid P_{\alpha}\left(y_{i j}\right)\right) \prod_{i, k} P\left(y_{i k} \mid P_{\alpha}\left(y_{i k}\right)\right)}, i \in[1, T], j \in[1, m], k \in[1, n]
\end{aligned}
$$

where $y_{i j}$ is an observation value and $P_{\alpha} y_{i j}$ is the set of parent nodes of $Y_{i j}$.
The dynamic Bayesian network for the disruption evolution is shown as Fig. 4.
The dynamic Bayesian network modeling includes the following steps:

Step 1: Determine the key node variables. Firstly, the nodes are determined by causal analysis, and then according to the historical cases or expert experiences, determine the node variables based on the key elements Step 2: Construct a dynamic and continuous evolution process according to Fig. 4
Step 3: Calculate the probabilities of the node variables in the time-based dynamic Bayesian network from the disruption back to the upstream causes of the disruption

### 3.3 DA-NET modeling

Firstly, the explanation of parameters about the DA-NET is shown in Table 1.
The process of DA-NET modeling is as follows:

![img-3.jpeg](img-3.jpeg)

Step 1: Obtain the input matrix *I* and the output matrix *O*. The input matrix *I* is an input matrix mapping *A* × *M* → {0, 1}, which corresponds to a set of directed arcs from *A* to *M*. The output matrix *O* is an output matrix mapping, which corresponds to a set of directed arcs from *M* to *A*. Step 2: Assume the premise of *E*^{1} is true, that is, *c*_{1}^{1} < accepted cost, then, with a token in *m*_{1}, *a*_{1} is triggered. Therefore, *H*^{1} = [1 0 0]. Also assume the algorithm set *F*^{i} = {*f*_{1}^{i}} is a simple sum operation to calculate the cost. Step 3: Consider a DA-NET with *m* place nodes and *n* transition nodes, given *T*^{i} the current marking vector, *G* the incidence matrix, and *H*^{i} the current transition fire vector, a new marking vector is given by

$$(T^{i+1})^{\prime} = (T^{i})^{\prime} + G(H^{i+1})^{\prime} \tag{4}$$

We use (4) to add *T*^{i} to *R*(*T*^{i}).

Step 4: The attribute is updated with (5)

$$[C^{1}, C^{2}, \dots, C^{m}]\left(T^{i+1}\right)^{\prime} = F\left{\left[C^{1}, C^{2}, \dots, C^{m}\right]\left(T^{i}\right)^{\prime},\left[D^{1}, D^{2}, \dots, D^{n}\right]\left(H^{i+1}\right)^{\prime}\right} \tag{5}$$

Step 5: The DA-NET is a loop network, so if there is an enable transition node, we will go back to step 1

### 4 Case study

The PSC includes crude oil exploration, oil field development, crude oil extraction, pipeline transportation, petrochemical industry, transportation, distributor, and customers. The PSC is easily affected by the changes of world oil reserves, production, and prices. In addition, unlike the traditional supply chain, in which the production enterprise is regarded as the core enterprise


and the production as the core process, the pipeline transportation after oil exploitation is the core process in the PSC. After pipeline transportation, oil is eventually distributed to different customers for subsequent re-production and processing. Therefore, if oil leakage occurs in the pipeline transportation, it will certainly affect the operation of downstream enterprises. The PSC model is shown in Fig. 5.

### 4.1 Causal analysis with Bayesian network forecasting

On April 20, 2010, the oil leakage in the Gulf of Mexico has caused great concerns in the world. The fire and explosion resulted in the damage of offshore oil wells and finally led to the oil leakage. The underwater detectors showed that the volume of daily oil leakage of the drilling riser and drilling pipe was about 1000 barrels.

The Gulf of Mexico, situated in the southeastern coastal waters of the North American continent, connects with the Atlantic Ocean through the Florida Strait and its geological structure is relatively stable, so geological factors are not considered. According to the process of on-site rescue, the scenario elements of the disruption can be analyzed and shown in Table 2. The whole disruption is divided into six periods according to the evolution state of the disruption, which are represented by scenario states, including operational errors, fire and explosion, abnormal oil pressure, aging facilities, pipeline break and adjacent pipeline break, and end of disruption, which are also the causes of the disruption.

The evolution path of the Mexico Gulf oil leakage is shown in Fig. 6.

The conditional probability is determined according to the expert experiences for the variable with the parent node. When an event occurs, its node probability for each period is shown in Fig. 7. Netica (version 5.22.0.0) is used to calculate the Bayesian probabilities.

Then, scenario inference and probability calculation are carried out for each stage of the disruption. It is inferred that, due to operational error, methane isokinetic breaks through the safety barrier in the oil well, and then explosion occurs. After the explosion, the oil pressure in oil wells and pipelines is abnormal, and the equipments are aging. These factors finally result in oil leakage due to pipeline break. Based on the historical data and the experiences of experts, the probabilities of Bayesian network are deduced. The process is shown in Fig. 7. The probabilities of causes (scenario states) are shown in Table 3, in which the probability of S_{3} and S_{6} is 100% and 85.9% respectively. The calculation results are basically in line with the actual situation of the disruption, that is, the abnormal pressure of the pipeline and the rupture of

![img-4.jpeg](img-4.jpeg)

Table 2 Scenario elements of the Gulf of Mexico oil leakage


the adjacent pipelines led to the eventual occurrence of the oil spill.

### 4.2 Impact analysis with DA-NET modeling

This section mainly studies the impact of the oil spill on the PSC. The oil of the Gulf of Mexico has always been an important source of raw materials for W; since the disruption, the underwater sensor has detected that the amount of oil leaked every day is about 5000 barrels, which has led to a shortage of raw materials for the company and seriously affects its normal manufacturing operation. Then, the DA-NET model is used to analyze the disruption on the PSC in which W Company belongs to. The assumptions are as follows.

1. W is a chemical enterprise engaged in the production of synthetic fibers. It mainly manufactures synthetic fibers of three types of chemical products
2. W can find new suppliers of crude oil on the third day of the accident
3. W does not have enough emergency stock

According to the disruption in PSC and process of DA-NET modeling, the DA-NET model of the PSC is shown in Fig. 8.

In Fig. 8, we can see three kinds of raw materials for chemical fiber products that are used and assembled. Then, oil is processed, followed by the impact nodes, including impurity removal and de-sulfurization, atmospheric distillation, catalytic cracking, and processing of petroleum. To understand the impact of the *p*_{8} disruption on the PSC, a token is provided for *p*_{8}. The reachable set *R*(*M*) of *p*_{8} is (*p*_{10}, *p*_{11}, *p*_{12}, *p*_{13}), and these points are nodes affected by the disruption. *t*_{9}, *t*_{10}, *t*_{11}, *t*_{12}

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

**Fig. 7** Probability inference of the Gulf of Mexico oil leakage

related are respectively de-sulfurization, atmospheric distillation, catalytic cracking, and processing of petroleum. Within 3 days, the disruption leads to higher costs and affects the efficiency of the PSC. Therefore, cost and delivery time are chosen as the key performance indicators to illustrate the impact. Decision sets are used to determine the fire of transition sets, and algorithmic sets are used to update the cost and delivery time.

Assuming that the customers need 20 units of chemical product from W, the disruption analysis of W is as follows:

**Step 1:** According to the flow of the Petri net, we obtain

$$I = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}, \ O = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{bmatrix}, \text{ and} $$

**Table 3** Probabilities of the causes (scenario state)


$$G = \begin{bmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 1 & -1 & 1 \end{bmatrix}.$$

Then, we assume, $$C = [5 \begin{array}{cccc} 6 & 13 & 2 \end{array}]$$ and $$H^{1}$$

Then, we assume, $$C = [5 \begin{array}{cccc} 6 & 13 & 2 \end{array}]$$ and $$H^{1}$$

Step 2: Assume that the condition of decision set $$E_{1}$$ is correct, $$c_{1}^{1} = 8$$ is less than the acceptable price, the transition fire vector $$H^{1} = [1 \begin{array}{cccc} 0 & 0 & 0 \end{array}]$$, and the algorithm set $$F^{l}$$ is a sum set, which is used to calculate the cost.

Step 3: We obtain $$T^{1} = [2 \begin{array}{cccc} -1 & 1 & 0 \end{array}]^T$$ and then add it to $$R(T^{l})$$. That is, $$c_{1}^{1} = c_{1}^{2} + d_{1}^{1} = 6 + 20 = 26$$,

$$d_{1}^{1} = d_{1}^{2} + c_{1}^{1} = 30 + 26 = 56,$$ which iterates until no transition nodes are fired. Through iteration calculation, it can be concluded that the updated $$C$$ = [26 20 12 10], $$D$$ = [56 40 22 10]. Within 3 days of oil disruption in W, the cost increases and delivery is delayed. For 1 unit product, the total cost increases by 42 and the time delay is 58 h.

### 5 Results and discussion

As the main aim of our research was to address two related questions, we discuss hereafter the implications of the research findings in order to explicitly explain each question.

![img-7.jpeg](img-7.jpeg)

### 5.1 Causal analysis

As described before, scenario inference and probability calculation are carried out to analyze the causes of the disruption. Scenario inference is utilized to identify the causes qualitatively, based on the causal relation model of the disruption chain in PSC. Then, we need more detailed information about the cause-effect relation of the disruption chain. Based on the historical data and the experiences of experts, the probabilities of Bayesian network are deduced. Finally, we not only get the causes of the disruption, but also identify their probabilities, which is especially hard and significant for the decision-maker to cope with the disruption. As shown in [25-27], most research focused on the impact of disruptions. Although some researchers addressed the causes, they used the qualitative method to explain what factors led to disruptions. Especially for the oil leakage, it does not often occur, so we do not have sufficient information and data to infer the causes. Thus, with the help of Bayesian forecasting, we can tackle the problem.

### 5.2 Impact analysis

The other issue we address is the impact of the PSC disruption. After oil leakage happened, we need to know what are the causes and what the disruption will lead to. If we know the impact of the disruption, we can prepare in advance and reduce the loss. So it is important for the managers of the PSC and downstream members to make decisions. We combine the practical technology with the theoretical method to solve the problem. Here, UASNs are designed to detect pipeline oil leakage, and then, the DA-NET model is built to analyze the disruption on the PSC.

Oil leakage is a special kind of disruption, which happens in the sea and difficult to collect disruption data. Thus, identifying its impact accurately is basically impossible. With the input data via UASNs, the DA-NET model is applied and we can infer the accurate impact on the PSC, for example, time delay and cost increase. When we get the result, the managers can plan the delivery and ordering in advance, and the fluctuation of the supply chain will be controlled.

The method proposed in the paper can be applied to analyze other kinds of disruptions. The causal analysis with Bayesian network forecasting and impact analysis with DA-NET modeling also can be separated to use.

### 5.3 Limitations and future research directions

The paper proposes a whole cycle analysis method of supply chain disruption based on UASNs. Although the method can provide causes and impact of oil leakage simultaneously, there exist some limitations. Because of the particularity of oil leakage, we lack sufficient data and experience. So the causal relation model of the disruption chain is not accurate. Perhaps some causes are missing. In the future, we should accumulate more cases and data to improve the model. Moreover, DA-NET modeling is a method based on Petri net and analysis of disruption evolution. The reasonable inference of disruption evolution path is the key factor to obtain the accurate impact on PSC operation. So how to analyze the evolution and development of a disruption is essential to solve in the future.

## 6 Conclusion

UASNs present a golden opportunity for marine disruption analysis. In the paper, we proposed a whole cycle disruption analysis approach for the PSC. When we obtained the monitoring data of a disruption via the UASNs, we can infer the causes of the disruption and also determine the impact of the disruption. In detail, scenario inference and Bayesian network are applied to reversely infer the upstream causes and probabilities of the disruption, the DA-NET model of the PSC is developed, and the impact of the disruption (cost and time delay) is analyzed quantitatively. For the oil leakage in PSC, operational errors, fire and explosion, abnormal oil pressure, aging facilities, and pipeline break are usually the causes of the disruption. With the proposed method, we can infer the causes and their probabilities after analyzing the evolution path of the disruption. Moreover, with the DA-NET model, the cost increase and time delay of a supply chain caused by the disruption can be calculated.

## Abbreviations

BEAST: Bayesian evolutionary analysis by sampling trees; DA-NET: Disruption analysis-Petri net; MILP: Mixed integer linear program; PSC: Petroleum supply chain; UASNs: Underwater acoustic sensor networks

## Acknowledgements

The research presented in this paper was supported by the China National Natural Science Foundation.

## Funding

The authors acknowledge the National Natural Science Foundation of China (Grant U1664264), the China Fundamental Research Funds for the Central Universities (Grant: 300102228402 and 3100102229103), and the China Postdoctoral Science Foundation (Grant: 2014 M552401).

## Availability of data and materials

Not applicable.

## Authors' contributions

HH is the main author of this article. The idea of applying DA-NET modeling and Bayesian forecasting to analyze the disruptions of petroleum supply chain was put forward by her. Then, she also constructed the main structure of this paper and was responsible for DA-NET modeling. KC introduced the Bayesian network to analyze the causes of disruption. Relevant data were collected by JH. LD verified the validity of the model. All the authors read and approved the final manuscript.

## Competing interests

The authors declare that they have no competing interests.

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Received: 21 February 2019 Accepted: 10 April 2019
Published online: 10 May 2019

## Submit your manuscript to a SpringerOpen ${ }^{\circledR}$ journal and benefit from:

- Convenient online submission
- Rigorous peer review
- Open access: articles freely available online
- High visibility within the field
- Retaining the copyright to your article

Submit your next manuscript at $\rightarrow$ springeropen.com