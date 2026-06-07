# Article 

## Bayesian-Based Traffic Safety Evaluation Study for Driverless Infiltration

Yinhao Wang, Junyou Zhang * and Guansheng Wu

## check for updates

Citation: Wang, Y.; Zhang, J.; Wu, G. Bayesian-Based Traffic Safety Evaluation Study for Driverless Infiltration. Appl. Sci. 2023, 13, 12291. https://doi.org/10.3390/ app132212291

Academic Editors: Huazhou Hou, Guilin Qi and He Wang

Received: 24 October 2023
Revised: 7 November 2023
Accepted: 10 November 2023
Published: 14 November 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

579 Qianwangang Road Economic \& Technical Development, Shandong University of Science and Technology, Qingdao 266590, China; 15621406165@163.com (Y.W.); wgs03708@163.com (G.W.)

* Correspondence: junyouzhang@sdust.edu.cn; Tel.: +86-13905323314

Abstract: Although driverless technology belongs to the frontier of science and technology, there is no sufficient actual data. From the lack of a comprehensive systematic evaluation method of traffic safety under driverless penetration, considering the impact of the three core systems of driverless perception, decision-making, control, and the complex road factors on the safety of driving, we review the main risk causal factors through the analysis of the accident causal model STAMP and put forward the fusion of the Leaky Noisy-OR Gate and Bayesian network model. The Bayesian network professional analysis tool GeNle 2.0 was used to simulate, analyze, and evaluate the driverless traffic risk Bayesian network model, which accurately assessed the traffic safety risk under driverless penetration and diagnosed and identified the sensitive risk factors. The results of this study concluded that, in order to effectively deal with the future traffic safety risks of driverless vehicles, vehicle enterprises, research institutions, software and hardware suppliers in the field of driverless driving should strengthen the research and development and manufacturing of key components such as perception, and enhance the depth of research and development of AI decision-making software, which provides a new way of thinking about the management of the safety risk of driverless traffic and a theoretical basis for the development and implementation of risk control measures.

Keywords: driverless vehicles; safety evaluation; STAMP; Bayesian networks; Leaky Noisy-OR gate model; GeNle; sensitivity analysis

## 1. Introduction

With the arrival of the 5G era and the rapid development of the internet and communication technology, the internet of vehicles and intelligent transport systems gradually in the vehicle has been widely used. Although the road to fully realizing autonomous driving is long, winding, and full of danger, with the development of artificial intelligence, control technology, and the support of government policies, driverless technology will usher in a prosperous development. Driverless technology can not only save human energy spent on driving and improve the quality of life and efficiency, but its ultimate goal is to establish a smart city with intelligent transportation planning [1]. At present, domestic and foreign research institutions, universities, and automobile enterprises are committed to research, with a view to breaking through technical barriers and realizing the commercial operation of driverless vehicles, and the development of driverless vehicles has become an important symbol for measuring a country's scientific and technological innovation. The U.S. IEEE predicts that by $2040,75 \%$ of the total number of cars on the road in the world will be driverless vehicles [2]; according to the world-renowned market research agency 39IHS Automotive predicts that by 2035, North America's share of the driverless car market will reach $29 \%$, China's is $24 \%$, and Western Europe's is $20 \%$ [3], which lays a solid foundation for the development of the smart city in the future. However, since 2018, Uber, Google, Ford, Tesla, General Motors, Alphabet, and other driverless vehicles have been involved in traffic accidents such as traffic jams, tailgating, rollovers, collisions, and other traffic

accidents when traveling, and have even caused injuries and deaths, which has sounded a safety alarm for the whole driverless technology industry, and road traffic safety under driverless infiltration has become a hotspot of concern both at home and abroad.

In road traffic safety under driverless penetration, it is especially important to carry out a risk assessment of the key parts of the driverless vehicle and the surrounding environment, to find out the higher risk of influencing factors and then put forward rectification proposals and improve them, to reduce the occurrence of traffic accidents, reduce the loss of life and property brought about by traffic accidents, and accurate risk assessment can ensure that the vehicle drives smoothly and safely so that passengers can enjoy a fast, safe and efficient traveling experience.

Traffic safety accident causation is complex and diverse, combined with the characteristics of autonomous perception, control, and decision-making of the AI system of driverless vehicles. Firstly, the driving environment includes characterizing the impact of stationary objects and moving targets on the road on driving safety. Secondly, the risk of AI driving includes the impact of perception, decision-making, and control on driving safety. The classic road traffic safety management model, traffic accident causation analysis is to view the human-vehicle-road-environment as a whole, and common analysis methods and theories include fuzzy hierarchical analysis, neural networks, Bayesian networks, fault tree analysis, etc. Sun Xianglong et al. [4] in the three-dimensional evaluation model of traffic safety risk of general trunk highways, the weight determination method based on the relevance of indicators (CRITIC) and fuzzy hierarchical analysis (Fuzzy-AHP) are combined to establish a comprehensive evaluation model of traffic safety risk, and different improvement measures should be taken according to different risk levels of road sections, in order to effectively improve the level of traffic safety of general trunk highways. Yue Long [5] in the analysis of factors affecting traffic accidents on highways based on radial basis neural network, radial basis neural network is used to predict traffic accidents with high feasibility and accuracy ( $91.6 \%$ ). Cheng Wei et al. [6] in highway traffic accident severity prediction and causation analysis based on the Bayesian network, the data fusion method is used to construct an accident severity prediction model based on tree augmentation and generalized Bayesian network, and the model's accuracy in predicting the severity of highway accidents can reach $84.27 \%$. Peng Gu [7] in the pattern recognition and causation analysis of mega road traffic accidents, a T-S fuzzy fault tree mega traffic accident causation analysis map is constructed, and targeted suggested measures are proposed to reduce the occurrence of such accidents. Each of these evaluation methods has its own advantages and disadvantages, such as the neural network evaluation method, the advantage of selflearning ability, and adaptive ability, but the disadvantage is that it requires a large amount of sample data and low precision. The hierarchical analysis method has the advantage of simple calculation, flexibility, and convenience, but the disadvantage is that it is difficult to solve the problem of more risk indicators.

Currently, there is no abundant research on driverless safety risk, but the perception, decision-making, and control of driverless risk occupy a pivotal position in overall risk management. Most of the existing studies calculated the probability of safety risk for a certain type of accident, and less deeply dig into the causation of accidents and risk inference analyses. In this study, the classical Leaky Noisy-OR-Gate model [8] and the Bayesian network [9] risk analysis model are used in a perfect fusion, which can project the safety risk value of driverless highway traffic in a forward direction as well as find out the sensitive factors by inverse reasoning. The results of this study can provide an important reference basis for the prevention of traffic accidents and the development of key software and hardware technologies for driverless vehicles.

# 2. Materials and Methods 

In order to prevent traffic accidents and the research and development of key software and hardware technologies of driverless vehicles, this paper analyzed the key factors of highway traffic safety under the penetration of driverless vehicles and then established the

evaluation system of driverless highway safety risk indicators. In this section, we obtained relevant data for expert scoring and constructed the Bayesian network model of causal risk, and the Leaky Noisy-OR Gate model for the data.

# 2.1. Analysis of Key Factors for Road Traffic Safety Evaluation under Driverless Penetration Identification of Key Risk Factors 

A total of 24 cases of driverless accidents at home and abroad from 2016 to 2022 were collected. The content mainly includeed automobile companies, the time of the accident, the brief description of the accident, and the damage caused by the casualties and vehicles. After collation, some text data are shown in Table 1.

Common accident causation models include 24 Model [10], HFACS [11], Dominoes [12], STAMP [13,14], etc. Each model has its characteristics and is applied to different accident analysis situations [15]. STAMP (Systems Theoretic Accident Model and Process) is the most influential system accident model in contemporary times, which has shown its unique charm in accident investigation and analysis. STAMP was proposed by Leveson, which identifies the causes of accidents at the system level, explores the potential factors that have not been reflected in the accident investigation report, pays attention to the emergence of the system as a whole and treats the safety problem as a kind of control problem. It is the concurrent complex dynamic processes and unsafe interactions that are the causal factors of the security problem. The specific STAMP analysis framework for road traffic accidents is divided into five levels, namely unsafe behavior, prerequisites for unsafe behavior, unsafe supervision, organizational influence, and external factors, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. STAMP analysis framework for road traffic accidents.

Table 1. Selected textual data.


According to the STAMP analysis framework and the actual situation of driverless research, when the factors of people and organizations at the three and four levels were eliminated, and appropriate amendments were made, the implied accident causation

was inferred, the causal relationship was analyzed, and the causal factors present in the accident cases were mined, and finally, 18 driverless accident causal factors were identified. Considering the influence of the key aspects of perception [16-19], decision [20-22], and control [23,24] on driving safety, the 18 causal factors were divided into 5 categories, such as perception risk factor, decision risk factor, control risk factor, road risk factor, and other risk factors, in which P1-P3 are the perception risk factors, D1-D4 are the decision risk factors, C1-C4 are the control risk factors, R1-R4 are the road risk factors and E1-E3 are other risk factors. The obtained risk factors were mapped to the STAMP analysis framework for coding, as shown in Table 2.

Table 2. Classification and coding of factors causing driverless accidents.


A driverless vehicle is the product of the efficient integration of automotive AI technology and information and communication technology (ICT), which effectively improves the efficiency of transport and its safety. The accident cases and the key technologies of environment perception, positioning and navigation, path planning, motion control, and other key technologies of driverless vehicles were analyzed, and it was found that the driverless safety risks mainly come from five aspects, namely, perception risk, decision-making risk, control risk, road risk, and other objective risks, and the evaluation system of the driverless highway traffic safety indicators was established based on the above analyzed 18 causative factors, as shown in Figure 2.

# 2.2. Bayesian Network Modelling of Causal Risk 

### 2.2.1. Bayesian Network

A basic feature of the Bayesian analysis is the prediction. It utilizes prior existing knowledge and data, updates the probability model through the Bayesian theorem, and obtains predictions for future events or unknown quantities. It plays an important role in many practical applications, helping people make wise decisions and plans.

![img-1.jpeg](img-1.jpeg)

Figure 2. Evaluation system for traffic safety risk indicators of driverless highway.

The Bayesian Network (BN), also known as the belief network or directed acyclic graphical model (DAG), is a probabilistic graphical model, according to the topology of the probability graph, to examine a set of random variables $\left\{X_{p}, x \ldots X_{r}\right\}$ and its $n$ sets of Conditional Probability Distributions (CPDs). The nodes in the directed acyclic graph of a Bayesian network represent random variables, which can be observable variables, or hidden variables, unknown parameters, and so on. An arrow connecting two nodes represents that the two random variables are causally (or non-conditionally) independent. If two nodes are connected by a single arrow, meaning that one node is the "parents" and the other is the "children", the two nodes will produce a conditional probability value. In summary, the Bayesian network consists of a directed acyclic graph (DAG) and a conditional probability table (CPT). The BN expression is Equation (1).

$$
\mathrm{A}=\{(\mathrm{M} \cdot \mathrm{~K}), \mathrm{P}\}
$$

where $M$ is the structural network node, $K$ is the directed acyclic graph, and $P$ is the conditional probability distribution of the node.

Bayesian networks mainly use local distributions (conditional probability distributions) to describe joint distributions. That is, by integrating local interactive relationships between described variables to obtain global variable relationships. This makes Bayesian networks suitable for research on problems dealing with ambiguity and uncertainty. The full probability expression is shown in Equation (2).

$$
\mathrm{P}(\mathrm{Y})=\sum_{i=1}^{n} \mathrm{P}\left(X_{i}\right) \mathrm{P}\left(\mathrm{Y} \mid X_{i}\right)
$$

The set of discrete node variables is $\mathrm{M}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}, X_{n}$ denotes the node variables of BN, and the CPT of each node includes all the conditional probabilities P of the parent node inside it, which can be computed by Bayesian formulae, expressed as shown in Equation (3).

$$
\mathrm{P}\left(X_{i} \mid \mathrm{Y}\right)=\frac{\mathrm{P}\left(\mathrm{Y} \mid X_{i}\right) \mathrm{P}\left(X_{i}\right)}{\mathrm{P}(\mathrm{Y})}
$$

In the formula: $i=1,2, \ldots, n ; \mathrm{P}\left(X_{i}\right)$ is the a priori probability, which can be obtained through statistical data or empirical knowledge, $\mathrm{P}\left(X_{i} \mid \mathrm{Y}\right)$ is the a posteriori probability, i.e., the probability of $X_{i}$ occurring under the condition of Y occurring, and $\mathrm{P}\left(\mathrm{Y} \mid X_{i}\right)$ are all conditional probabilities [25].

# 2.2.2. Modelling Bayesian Networks 

In the analysis of the Bayesian network-based model, the construction of the Bayesian network structure was the basis of this study of driverless traffic risk. After the expert group decision-making on the driverless highway traffic safety risk indicator evaluation system for logical reasoning, a Bayesian network model of driverless traffic risk was constructed, see Figure 3.

### 2.3. Determining Bayesian Network Parameters

### 2.3.1. Leaky Noisy-OR Gate Extended Model

When applying a Bayesian network, how to obtain the network parameters corresponding to the risk of driverless driving is an important problem that needs to be solved urgently. If there is a large number of complete datasets, you can directly build a BN model to obtain network parameters from the data set. For example, the Stochastic Approximate Monte Carlo method (SAMC), Maximum Likelihood Estimation (MLE), etc., are used. However, these methods require a large number of data samples, and the research mainly focuses on $\beta$ distribution and binomial distribution, which have certain limitations. Due to the late start of China's artificial intelligence technology, the exploration of driverless technology is still in the primary stage, and there is not a complete risk case base. At

present, it is still necessary to rely on expert knowledge and historical experience to obtain the Bayesian network parameters, and the Leaky Noisy-OR-Gate model is a method to solve this kind of problem. The method in the knowledge of the network structure, and the expert knowledge, can approximate the conditional parameters of Bayesian network by Leaky Noisy-OR Gate model.
![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian network structure for driverless risk indicators.
The Noisy-OR Gate model can be used to describe the internal relationship between n variables $X_{1}, X_{2}, \ldots, X_{n}$ and the result $Y$ they influence. The Bayesian network based on the Leaky Noisy-or Gate model also needs to meet the following three conditions:

- Each node in the network is a binary discrete variable with 2 states, assuming they are true value (1) and false value ( 0 ).
- The parent node of any node Y is $X_{1}, X_{2}, \ldots, X_{n}$, then $X_{1}, X_{2}, \ldots, X_{n}$ should be independent of each other.
- Each variable is enough to cause the result Y to occur when other variables are false ( 0 ). At this time, only $X_{i}(i=1,2, \ldots, n)$ is 1 , while other parent nodes are 0 . The probability that Y takes the value 1 is $P_{i}$, as shown in Equation (4).

$$
P_{i}=\mathrm{P}\left(\mathrm{Y} \mid \overline{X_{1}}, \overline{X_{2}}, X_{i}, \ldots, \overline{X_{n}}\right)
$$

Then $P_{1}, \ldots, P_{i}, \ldots, P_{n}$ determine the other terms $X$ in the conditional probability table for node Y, as shown in Equation (5).

$$
\mathrm{P}\left(\mathrm{Y} \mid X_{n}\right)=1-\prod_{i: X_{i \in} X_{p}}\left(1-P_{i}\right)
$$

where $X_{n}$ is the set of Y parent node values, $X_{p}$ is a subset of $X_{n}$, and the subset consists of parent nodes whose values are true.

As there will be some other unknown factors that will affect node Y in the actual driverless risk, Henrion proposed the concept of leaky probability. The conditional probability modification model of the parent nodes n variables $X_{1}, X_{2}, \ldots, X_{n}$ with the same influence factor child node Y produced by them, which is the Leaky Noisy-OR-Gate extension model, assuming that Y (child node) has 2 mutually independent parent nodes: $X_{i}$ and $X_{\text {all }}$ (i.e.,

factors other than $X_{i}$ are merged into $X_{\text {all }}$ ), $P_{i}$ and $P_{\text {all }}$ are the connection probabilities of $X_{i}$ and $X_{\text {all }}$, as shown in Equations (6) and (7).

$$
\begin{gathered}
\mathrm{P}\left(\mathrm{Y} \mid X_{i}\right)=P_{i}+P_{\text {all }}-P_{i} P_{\text {all }} \\
\mathrm{P}\left(\mathrm{Y} \mid \overline{X_{i}}\right)=P_{\text {all }}
\end{gathered}
$$

From this, Equation (8) can be derived:

$$
P_{i}=\frac{\mathrm{P}\left(\mathrm{Y} \mid X_{i}\right)-\mathrm{P}\left(\mathrm{Y} \mid \overline{X_{i}}\right)}{1-\mathrm{P}\left(\mathrm{Y} \mid \overline{X_{i}}\right)}
$$

After obtaining the parent node connection probability $P_{i}$ according to Equation (8), all the hazardous factors we may have missed were combined into a single variable $X_{L}$, and $P_{L}$ is the connection probability of $X_{L}$, the conditional probability of node Y is obtained by combining the uncertainty factor $X_{L}$ and its connection probability $P_{L}$ (which can be determined by the risk history distribution function), and thus the conditional probability of node Y, as shown in Equation (9).

$$
P_{i}(\mathrm{Y})=1-\left(1-P_{L}\right) \prod_{i: X_{i} \in X_{p}}\left(1-P_{i}\right)
$$

In summary, for a given sample data, under the premise of node topology and conditional probability distribution determined by the Bayesian network, the conditional probability or a posterior probability was calculated for unknown data for diagnosis, prediction, or classification purposes.

# 2.3.2. Calculation of Conditional Probabilities for Each Node 

In order to achieve the quantitative analysis of causal factors in the evaluation system of driverless road traffic safety risk indicators, it was necessary to obtain the a priori probability of the underlying nodes and the probability value of the initial conditions of each node. However, it is very difficult to obtain accurate data for driverless road traffic safety risk indicators in real scenarios, and the probability statistics of these underlying nodes are currently lacking, so experts with rich experience in the field of driverless vehicles were used to make judgments and assign values, and finally, data analysis statistics and quantification were carried out to determine the required probability values. This method of obtaining data was more scientific, effective, and accurate.

After each node and scenario was determined, one senior manager with rich experience in the field of driverless vehicles was selected along with four experts (Hereinafter collectively referred to as experts). In order to ensure the validity and accuracy of the data, the experience differences of each expert were taken into account, and errors caused by personal subjective factors were reduced through weight distribution. This article selected three indicators, educational background, length of service, and professional title, as the key influencing factors of experience differences, and assigned values of 1 to 3 points respectively. The weight distribution of each factor is shown in Figure 4.

Scores were assigned to experts based on their academic qualifications, length of service, and professional titles. The sum of the three was the total weighted score of the expert. The ratio of each expert's weighted score to the total score of all experts was the weight factor of each expert. Table 3 lists the weighting factors of the five invited experts.

![img-3.jpeg](img-3.jpeg)

Figure 4. Weight coefficient distribution of expert experience influencing factors.

Table 3. Experts and their weight.

|  Serial
Number | Educational
Qualifications | Length
of Service | Job
Title | Weighted
Score | Weight
Factor  |

Each risk factor was scored according to the risk probability level evaluation criteria. The results of the partial scoring and the weighting factors of the expert scores corresponding to the total score are shown in Table 4.

Table 4. The weighting factors corresponding to partial scoring results and expert scores in the total score value.


According to the causal factors of the driverless road traffic safety risk indicator evaluation system, a questionnaire was issued to two senior managers and six experts in the field of driverless driving, and the probability level of the risk was classified into five levels by the expert group, as shown in Table 5.

Table 5. Risk probability level.


Each risk factor was scored according to the risk probability level evaluation criteria. Based on the valid sample data, the statistics were analyzed and quantified to obtain the a priori probability of the bottom node of each risk factor (see Table 6) and the initial condition probability table of each node, see Appendix A.

Table 6. Prior probabilities of each risk factor.


# 2.3.3. Calculation of Conditional Probabilities for Each Node 

The connection probability between each child node and its parent node was determined from the initial conditional probability table and Leaky Noisy-OR Gate model, Equation (8) in Appendix A, and then the modified CPT was obtained by using the Leaky Noisy-OR Gate model in Equation (9). Due to the large number of nodes and the space limitation, the conditional probability calculation of each node of $\mathrm{C} 1, \mathrm{C} 2, \mathrm{C} 3$, and C 4 was carried out by taking the control risk C11 as an example.

According to Equation (8), the connection probabilities of $\mathrm{C} 1, \mathrm{C} 2, \mathrm{C} 3$, and C 4 were calculated to be $0.5641,0.2698,0.6463$, and 0.4737 , respectively. In this paper, given that the connection probability of the unknown factor (Leak probability) was 0.1 , and then, according to Equation (9), we computed the node control risk C11 modified conditional probability, and the results are shown in Table 7.

Table 7. CPT for controlling risks at node C11. (1: Yes; 0: No).


Table 7. Cont.


The CPT results of other nodes P11, D11, R11, and E11 are shown in Tables 8-11.
Table 8. CPT for Perceived risks at node P11 (1: Yes; 0: No).


Table 9. CPT for Decision risks at node D11 (1: Yes; 0: No).


Table 10. CPT for Road risks at node R11 (1: Yes; 0: No).


Table 10. Cont.


Table 11. CPT for Other risks at node E11 (1: Yes; 0: No).


# 3. Results 

### 3.1. Analysis of Driverless Risk Assessment Based on Bayesian Network Models

Commonly used tools for BN analysis are GeNIe [26], MATLAB's BNT toolbox [27], Netica [28], and others.

GeNIe is a very powerful visualization tool, a professional and efficient Bayesian network construction and simulation analysis tool, with a good user interface, intuitive and transparent, which can calculate the prior probability by automatically learning the sample data. It is also able to calculate the posterior probability of other nodes based on the known target nodes of the network model [29]. So, GeNIe was used for simulation and analysis to achieve effective prediction and diagnosis of driverless risk events.

### 3.2. Risk Assessment Based on Bayesian Modelling

This article used the Bayesian analysis software GeNIe to provide a detailed description of the modeling data simulation analysis and calculation process. Taking the C11 node as an example, GeNIe was run, a new network1 file was created, a new opportunity node in the graphical view was created and renamed it C 1 , the node button was double-clicked, and the 'Definition' tab was selected, At this point, the following dialog box popped up, referenced and standardized collected data (initial prior probability), and inputted the status of node C 1 and the prior probability value of $\mathrm{Y}, \mathrm{N}, 0.12,0.88$ in sequence. The success of nodes in the network was described by the prior probability distribution of their two results ( Y and T ), as shown in Figure 5.

Using the same method, nodes $\mathrm{C} 2, \mathrm{C} 3$, and C 4 were established in sequence and entered their respective states and prior probability values. Then, the prediction node C11 was created. To represent that Bayesian prediction depended on the actual occurrence prospect, four arcs were drawn from nodes $\mathrm{C} 1, \mathrm{C} 2, \mathrm{C} 3, \mathrm{C} 4$ to C 11 . The arc between two nodes meant that the probability distribution of risk occurrence had an impact. as shown in Figure 6.

![img-4.jpeg](img-4.jpeg)

Figure 5. C1 node Prior probability input.
![img-5.jpeg](img-5.jpeg)

Figure 6. C11 node Bayesian network.
The two states of node C11 were renamed to Y and T. The CPT of each node was entered, taking node C11 as an example, see Figure 7.

The Update tool was clicked, updating the probability distributions in light of observed evidence. The posterior probability distribution of control risk C11 nodes was simultaneously displayed, as shown in Figure 8.

According to the above method, other nodes were established and finally formed a complete Bayesian network. After updating the network, the complete probability of risk occurrence was $47 \%$, as shown in Figure 9.

![img-6.jpeg](img-6.jpeg)

Figure 7. C11 node CPT input.

![img-7.jpeg](img-7.jpeg)

Figure 8. Risk assessment results of C11 nodes based on Bayesian network.
The known data was substituted into the joint probability Formula (2) to obtain the full probability of A, as shown in Equation (10).

$$
P(A)=\sum_{X_{i}=P 11, D 11, C 11, R 11, E 11} P\left(X_{i}\right) P\left(A \mid X_{i}\right)=0.47
$$

The calculation results were consistent with the software simulation results, indicating that GeNIe was reasonable for Bayesian network traffic safety risk prediction.

In terms of the total risk probability, the probability of occurrence was $47 \%$. According to Table 5, it was judged that the driverless risk was a medium level 3, which is generally controllable and in line with the actual situation of driverless traffic safety.

In terms of decision risk, the probability was $39 \%$, the highest share of the five risk factors. It showed that the expert group believes that the decision-making risk occupied the primary position in the whole risk factor, in which the GPS positioning, navigation map, and dynamic planning accounted for $25 \%$, and the AI learning decision-making software accounted for $20 \%$, and the two accounted for nearly half of the decision-making risk. If the perception system was compared to human eyes, then the decision-making system was equivalent to the brain of the driverless driving system, through the perception system to obtain all the peripheral environmental information data transmission to the decision-

making system, planning the optimal travel route, such as the encounter of obstacles or traffic congestion. The decision-making system can quickly re-plan the driving route, and reasonably avoid roadblocks or congested sections, to ensure that the vehicle can be in the shortest time to safely reach the destination and safely arrive at the destination in the shortest time.
![img-8.jpeg](img-8.jpeg)

Figure 9. Risk assessment results based on Bayesian networks.
In the case of road risk, the probability was $36 \%$, the second highest of the five risk factors. This indicated that the expert group believed that road risk, although an objective factor, still occupied a secondary position in the overall driverless risk factors. Visibility, due to the influence of harsh environments such as rain, snow, fog, and haze, had the highest share of road environment factors, with a $19 \%$ share.

In the case of control risk, the probability was $33 \%$, the third highest of the five risk factors. It showed that the expert group believed that control risk was the last link in the whole driverless system, and was the executor that puts the conclusions of perception and decision-making into practice, which is an important factor in determining the safety and comfort of driverless driving. Emergency braking had the highest percentage of control risk at $25 \%$ and was the last important control output to deal with emergency situations to ensure safety.

As far as the perception system is concerned, the probability was $26 \%$, which was the fourth of the five major risk factors. The illustration family group thought that the perception risk was in the first ring of the whole driverless driving system, and its advantages and disadvantages would affect the safety and stability of the whole driving process. Sensors and cameras accounted for the highest proportion of perceived risk, $23 \%$, and occupied a very important position in the whole perception system, equivalent to the eyes of the driverless vehicle, providing accurate and error-free basic data information for the decision-making system.

# 4. Discussion 

### 4.1. Sensitivity Analysis Based on Bayesian Modelling

Sensitivity analysis is the process of analyzing the sensitivity of the probability of query nodes in a Bayesian network to changes in the probability of evidence nodes [28], which can be used to determine which factors have the greatest impact on the occurrence of target nodes. Sensitivity analysis is the process of calculating the risk factors that have a

significant impact on the safety of driverless traffic based on backward reasoning and then making targeted recommendations or improvements based on the results.

Assuming a driverless risk accident, so that A = 1, using the Bayesian network analysis tool, GeNIe calculated the posterior probability of each node and inversely inferred the sensitivity key risk factors. The results of the calculation are shown in Figure 10.

![img-9.jpeg](img-9.jpeg)

**Figure 10.** Results of sensitivity analysis based on Bayesian network.

From the figure, it can be seen that nodes P1, P3, D1, D2, C4, and R4 were more sensitive and the posterior probability of each sensitive factor is shown in Figure 11.

![img-10.jpeg](img-10.jpeg)

**Figure 11.** Posterior probability of each sensitivity factor for A = 1.

### 4.2. Targeted Recommendations

#### 4.2.1. The Shortcomings of Driverless

Based on the above computational study, the shortcomings of driverless vehicles were specifically in the following areas:

- The long-tail problem of sensors, cameras, and sensing technology in perceived risk (P1, P3). The reality was that there was a problem of poor sensing ability and low

robustness in complex traffic environments. For example, sensors such as LiDAR were basically unable to accurately measure the distance during heavy rain and foggy weather. Sensors such as millimeter waves can only recognize angles and distances and are unable to sense height. Cameras use visual perception, which requires a large amount of training data and a long period of algorithmic arithmetic support, and are unable to identify untrained non-standard obstacles. In addition, the long-tailed problem of perception technology is that it can never be guaranteed to exhaust all the training scenarios, and it needs to continue to be updated and improved.

- GPS positioning, navigation maps, dynamic planning, and AI learning decisionmaking software in decision-making risk (D1, D2). The current foreign civil GPS positioning accuracy is m-level, which is not up to the driverless high-precision cmlevel requirements. The daily real-time update of the traffic network also poses a challenge to accurate navigation map mapping. The reliability and security of the AI learning decision-making software are still to be improved.
- Emergency braking problem for risk control (C4). Driverless vehicles still occasionally have little or no braking output in the event of an emergency, and it is the last barrier to avoiding traffic safety accidents.
- The visibility problem of road risk (R4). Reduced visibility due to inclement weather, leading to misidentification or difficulty in identification by the perceptual system, is also an important factor in the overall system risk.


# 4.2.2. Presentation of Recommendations 

In view of the critical risks of the above six nodes and the existing deficiencies of the driverless, the following recommendations are made to the research institutes, software and hardware suppliers, and vehicle companies in the driverless field:

1. While improving the sensor accuracy, a multi-sensor fusion sensing system is adopted to achieve sensing redundancy to cover the whole scene sensing. A road sensing network based on multi-task learning is adopted to ensure the accuracy and robustness of the environment sensing system in complex traffic environments.
2. With the help of China's high-precision Beidou satellite navigation system and the development of Telematics based on the network's high-speed transmission of 5G technology, there is a need for real-time updating of high-precision maps and improvement of the software functions of the AI Learning Decision System, to ensure the timeliness, flexibility, and accuracy of the decision system.
3. For the occurrence of emergencies, the driverless vehicle should quickly make security decisions, and through adaptive control strategies for emergency risk avoidance operations, automatically stop the vehicle operation to ensure the timeliness and stability of the control system, and effectively ensure the absolute personal safety of the vehicle personnel.

## 5. Summary and Prospect

### 5.1. Research Results and Conclusions

This article conducted statistical analyses through accident cases and expert questionnaires, and the weight of each expert's scoring was calculated for validation to ensure the validity of the data. For the first time, the evaluation system of driverless highway traffic safety risk indicators was established, and the driverless traffic risk assessment model fused with Leaky Noisy-OR-Gate and Bayesian network was innovatively constructed, and the simulation inference analysis was carried out by using the GeNIe visualization tool, which effectively predicted the probability of the occurrence of the target node, and comprehensively evaluated the traffic safety risk under the penetration of driverless driving. By analyzing the driverless risk, it was obtained that the overall risk was in a controllable state, which coincided with the actual traffic risk. The key factors with high sensitivity were further identified. Specifically, they included the long-tail problem of sensors, cameras, and sensing technology in perception risk, the GPS positioning, navigation maps, dynamic

planning, and AI learning decision-making software problem in decision-making risk, the emergency braking problem in control risk, and the visibility problem in road risk. Meanwhile, three suggestions were put forward for scientific research institutions in the field of autonomous driving. The three suggestions are hardware and software suppliers, and vehicle companies.

Policymakers should improve the policies and regulations of the internet of vehicles industry based on the research results and promote cross-industry integration of the internet of vehicles industry. According to the safety evaluation index system in this article, investment in unmanned vehicle manufacturing enterprises, single-point technology solutions, overall solutions, sensors, artificial intelligence software, and hardware should be increased, and policy support should be provided. The regulatory authorities focus on managing the key units of perception, decision-making, and risk control, requiring autonomous driving production enterprises to actively control the source, strengthen industry self-discipline, actively participate in policy formulation and implementation processes, and ensure effective management and safe operation supervision of autonomous driving. With the improvement of autonomous driving policies and regulations, the effective management of regulatory authorities, and the supervision of safe operation, several major technology giants have begun to lay out autonomous vehicles. Unmanned new energy-sharing vehicles are about to enter commercial pilot operation, which will have a profound impact on the broader transportation industry.

In the coming period, efforts should be made to break through the bottleneck of perception, decision-making, and control technology of driverless vehicles, with a view to reasonably and effectively controlling the traffic safety risks under the penetration of driverless vehicles in a targeted manner, avoiding the escalation of the degree of risk or the expansion of the risk loss. This should be done by formulating the corresponding control measures and improving the level of safety preventive and control measures, providing a new idea for the management of driverless traffic safety risks, and providing a theoretical basis for the risk control measures to be the formulation and implementation of the theoretical basis. It is believed that in the near future, driverless vehicles will fundamentally change the human traveling mode, which will largely improve traveling safety and open up new solutions for reducing traffic congestion.

# 5.2. Innovation Points 

- The proposed fusion of the Leaky Noisy-OR Gate and Bayesian network model for assessing traffic safety risk is a novel approach.
- The integration of GeNIe for Bayesian network analysis adds depth to the research methodology.
- The call for action in terms of strengthening research and development in key components and AI decision-marking software offers practical insights for industry stakeholders. Clearly emphasizing the profound impact of the research findings on policymakers, regulatory agencies, and the transportation industry.


### 5.3. Research Prospect

This article analyzed the causal model STAMP of unmanned vehicle accidents and identified the main risk causal factors. The Bayesian network model of unmanned traffic risk was used to accurately evaluate traffic safety risks under unmanned driving penetration, diagnose and identify sensitive risk factors, and achieve rich research results. In the future, research is needed in the following two aspects.

At present, the research on driverless traffic safety analysis based on Bayesian networks is very few in China, and a lot of work needs to be carried out in-depth by continuing to study the contributing factors of driverless traffic accidents in depth. This paper did not correlate the impact of time factors on traffic accidents, which will be included in future research.

For traffic safety evaluation under the penetration of unmanned driving, this article constructed the Leaky Noisy OR Gate and Bayesian network model. Due to the limited sample data, all quantitative data of the model came from expert ratings, which had a certain degree of subjectivity. In the future, we will further expand the sample size and consider exploring more advanced learning algorithms, such as Bayesian deep learning, to link machine learning with probability theory, thereby promoting in-depth research on probability theory in machine learning and increasing the depth of traffic safety evaluation research under the penetration of unmanned driving.

Author Contributions: Conceptualization, J.Z.; methodology, Y.W. and J.Z.; data curation, Y.W. and G.W.; writing-original draft preparation, Y.W.; visualization, J.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This work was funded in part by the Natural Science Foundation of Shandong Province under Grant ZR2019MF056.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available in Appendix A.
Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A 

Initial condition probability Table for Bayesian network nodes for driverless traffic risks.

Table A1. Initial conditional probability of occurrence of $P$ risk.


Table A2. Initial conditional probability of occurrence of D risk.


Table A3. Initial conditional probability of occurrence of $C$ risk.


Table A4. Initial conditional probability of occurrence of R risk.


Table A5. Initial conditional probability of occurrence of E risk.

