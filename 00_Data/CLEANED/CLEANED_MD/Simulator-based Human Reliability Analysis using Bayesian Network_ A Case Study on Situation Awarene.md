# Simulator-based Human Reliability Analysis using Bayesian Network: A Case Study on Situation Awareness in Engine Resources Management 

A.M. Nizar, T. Miwa \& M. Uchida<br>Kobe University, Kobe, Japan


#### Abstract

Situational awareness (SA) is regarded as one of the important non-technical skills in constructing the seafarers' ability in daily decision-making and performing tasks, especially in Engine Resources Management (ERM). In maritime accidents that are mainly human error, insufficient SA is the specific factor that contributes to most of incidents. To quantitatively assess SA reliability, a Bayesian network of seafarers' performance in attaining SA in engine supervisory control is constructed. The adaptation of simulator data helped as combination along using subject matter expert input, which is a common practice in constructing human reliability analysis. Additionally, the simulator data can serve as the updating function when new data is observed. The result shows that the model can provide promising results as compared with expert expectation. Such kind of model can support the evaluation of the engine operation onboard, and mitigation can be provided to reduce the probability of human error.


## 1 INTRODUCTION

Regardless on doubt of the famous statement that said $80 \%$ of maritime incident are caused by the human error, the issue of human contribution to accidents is still remain important to study in the maritime safety area [1]. Departing from the traditional approach of studying human error for finding the lack of human limitation and blaming them, human factors study needs to be seen as the area where the human limitation is studied to improve working conditions. Thus, paradigm shift is needed to enhance the understanding of human capabilities, further, to facilitate the development of countermeasure and preventive strategy.

For the specific human performance factors that caused the most incident, situation awareness (SA) is prominent substituent that often mentioned. Human error in SA is labeled as "loss of SA". Incident analysis
report that was conducted by Grech et. al revealed $71 \%$ of incidents in maritime operator are due to loss of SA [2]. Loss of SA will result in the operator failure to understand the operation condition and leading to the failure to take appropriate action. For thus, as the well concept that not only researcher and management define but also seafarer well understand and relate its importance, IMO already included it in crew resources management as one of the nontechnical skill for seafarer to have [3,4].

### 1.1 Human Reliability Analysis in Maritime Operation

Practice to quantify human error through the process of human reliability analysis (HRA) has become the practice in other industry, from nuclear power plant through the air traffic control [5]. To uniform it, IMO with the formal safety assessment (FSA) guideline has also mentioned the HRA and various method of it in

maritime operation [6]. The HRA is not only useful in academic activity, but it was found to be benefit for stakeholders such ship owners and safety inspectors to identify and minimize the potential risk. The concept of hardware reliability analysis was also implemented in the HRA methods, including the hazard analysis and risk control stage. Seeing the HRA as similar with hardware analysis, it is also believed similar two combination of method can be fit to each other and combined to measure system reliability. Various HRA methods have been developed, also demonstrated in maritime operation cases. Cognitive reliability and error analysis (CREAM) is already applicated to derived the marine engineers performance reliability by combining Bayesian inference and fuzzy methods [7]. In seeing future projection, fuzzy methods also used combine with success likelihood index methods (SLIM) to demonstrate the autonomous operation regarding the human-machine interface [8]. Beyond onboard, the SLIM methods combined with system theoretic process analysis (STPA) are also used to analysis human-machine interaction in ship-to-ship LNG bunkering [9].

Most HRA aims to measure human error probability (HEP), that defined as an index to show the likeliness the human will conduct an error during the specific event. IMO defines it as the ratio of number of human error that have occurred, with the number of opportunities for human error [6]. In general, denominator for HEP is the number of chances the human conduct the error, compared to the hardware reliability where the denominator is the running time of equipment. This led to quantifying it by bottom-up approach to predict HEP by retrieving various data, mostly accident or incident report. The pitfall of employing only the failure database is the information only contain the number of failure event, without number of successful performance, where it is more close to assess the failure probability with empiric way [10]. Deciding the human error data from the accident report also has limitation since the number of accident reports is considered small compared to hardware failure data. This limitation often counters by including the expert judgement as the input, or the simulator experiment data.

In the lower factors, HRA can be included, combine, and consist of several performance shaping factors (PSF)[6]. PSF is often treated independently from one to the other. Several agree that PSF can be overlap, or its influence to each other should be considered [11]. The countermeasure of the dependency issue between PSF is by utilizing Bayesian network. The utilization of Bayesian network in HRA is increasing recently [5]. The Bayesian network allows us to analyze the likelihood of human error and identify the dependencies for complex modelling. It also came with the advantage of the ability to combine various data.

Bayesian network utilization in maritime operation is steadily increasing, either for HRA purpose or system reliability. It has wide application range from operator safety assessment to the evacuation training, including its application in offshore operation [12,13], ship collision [14], emergency situation [15], and ship engine operation [7]. The Bayesian network suggest PSF interaction and integrating different sources of
information into the model, once the new information or data is exist, it can be updated easily to the model [11]. In the context of HRA, the Bayesian network provides the ability to contain and combine multiple types of information and data, including cognitive literature, operation events, statistical data, and expert judgment.

SA concept in human factors field is already applied in various work environments, include in maritime operation. In this study, loss in SA is considered as one of the factors that contribute to the human error event. HRA as the methods in quantifying human error is applied with adapting the engine plan simulator data combine with the subject matter experts. Further, Bayesian concept is employed to accommodate the dependency between the factors in contributing the human error.

## 2 MODEL CONSTRUCTION AND UPDATING

There are two terms involved in model construction and updating. In model construction, Bayesian network is applied to construct the model and calculate the probability of SA failure in the first place. While in model updating, the concept of Bayesian inference is used to recalculate the probability of SA failure by considering the new data from the simulator. The difference between the two methods is Bayesian network with its graphical methods does not necessarily imply the theoretical Bayesian inference. However, the Bayesian network in this study is called Bayesian since it employed similar rules for inferring the probability.

### 2.1 Model construction

The flow process of model construction and updating are shown in Figure 1. The Bayesian network in calculating human error mostly employed subject matter experts input as weighting factors, in this flow is to calculate nodes distance. Beyond that, subject matter experts also use variable control input to calculate condition probability distribution. Within this study, the role of subject matter expert is not removed, but instead reduced by substituting it with the result from simulator data, specifically in the stage of calculating the condition probability distribution. Bayesian network causal model uses directed acyclic graphs consisting of nodes and arcs. The node plays as the variable in the model, and the arcs denote the causal relationship between these variables. The nodes that the arcs point to are called child nodes, while the reference nodes are called parents nodes. A node with child node and no parent node is called root node. As shown in Figure 1, this part refers to the first and second stage. For nodes that are discrete, their effect on the child node can be quantitively expressed through a conditional probability distribution (CPD) that shows the influence of parent nodes. This part takes the three processes on the last section of model construction.

![img-0.jpeg](img-0.jpeg)

Figure 1. Flow of model construction and updating.
![img-1.jpeg](img-1.jpeg)

Figure 2. Bayesian network general construction

### 2.1.1 Identify nodes and causal relationship

The Bayesian network model has several advantages, such as the ability to clearly define causal factors. Figure 2 illustrates the causal factor mapping for the proposed model, which focuses on estimating the likelihood of human failure event (HFE) as the general objective of human factor analysis. Based on the simulator data, this study focuses on the Bayesian network depicted in Figure 2 in general and Figure 3 as the proposed model, which include three level of stages: failure mode, cognitive function, and performance shaping factors.
![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian network based on the simulator experiment

Failure Mode (FM). HFE can be described as many types as possible of activity or process during the work. Following the same term in hardware reliability, FM is constructed below the HFE to explain various types of supporting events that lead to the human error itself. This can range from processing information process, decision making process and taking an action process. In this study, SA loss is assigned as one of the FM that construct the HFE.

Cognitive Function (CF). FM are supported by various human mechanisms explained by CF nodes. CF is determined as a variable that can be examined and observed during the controllable environment such as simulator, but it is difficult to observe in work environment. As the simulator experiment design, CF is assigned as one or multiple dependent variables. As shown on the Figure 3, there are two CF nodes called perception and comprehension, that support the SA loss. Perception, as situation awareness definition, is the process consuming the cues from the environment, while the comprehension is the stage where this information from the cues combined with the working and long-term memory to create meaningful information for the work goal.

Performance Shaping Factors (PSF). The PSF are the lowest, or the root nodes of the modes, as other HRA methods also described. In relation to the simulator data, the PSF represents the independent variable, in this case task-load, expertise, and familiarity. Taskload refers to the complexity of the performed work, the expertise is determined by the skill and knowledge of the operator, and familiarity refers to experience with specific work environment hardware and scenario. These PSF nodes contribute to the SA loss by influencing the operator perception and comprehension.

### 2.1.2 Distance between nodes

The relative importance of each parent node in influencing the child nodes are established by considering the relative importance of one parent node compared to others. Røed suggested that this can be done using a weight $w_{i}$ for each parent node $i$ [12]. In this study, we employed analytical hierarchy process to conduct pairwise comparisons and determine the weight. We invited four experts from academia who have professional experience on board in engine department as described on Table 1. The experts provided their weighting answers individually.

Table 1 Profile of the expert as subject matter experts


The weighting process resulted in the construction of perception as cognitive function, where the taskload has a relative importance of $w_{1}=0.26$, expertise with $w_{0}=0.41$, and familiarity with $w_{r}=0.33$. Similarly, in the construction of comprehension, task-load had a relative importance of $w_{l}=0.13$, expertise with $w_{k}=0.55$, and familiarity with $w_{r}=0.32$. Lastly, the weight is also applied to determine the importance of each CF in construction FM. In this case, perception had $w_{0}=0.14$, while compression has $w_{c}=0.86$, in constructing the SA loss as the main goal HRA in this study.

$$
D_{j}=\left|\sum_{i=1}^{n} D_{i j} W_{i}\right| \quad D_{j} \in[0,1]
$$

The relative importance result is used to define the distance between the child node and its parent nodes. The probability of the child node in certain states should be assigned smaller if the parent nodes are in different states. Take the example of CF perception node, if its PSF task-load node is in the easy state, PSF expertise node in high state and PSF familiarity node in good state, the PSF node perception should have higher probability of being in the high state compared to medium and low states. Røed suggested the conditional probability can be measured using this distant methods [12]. Considering the direction of change its parent nodes, we applied the Li method that modified the equation into the absolute value, as mention in the equation above, to distribute the probability of the child node [16].

### 2.1.3 Conditional probability for child nodes

$P_{j}=\frac{e^{-R D_{j}}}{\sum_{j=a}^{c} e^{-R D_{j}}} \quad P_{j} \in[0,1]$
To assign the probability distribution to each state on child nodes, the formula from Røed is used [12]. In the equation, the numerator is used to determine the probability of each state of the child node in the focus, while the denominator is normalization factor that all state of the child sum up to 1 . The higher $R$ index will make lower probability where the node in focus is state distant from the parent's states. While Røed uses the expert input to decide the R index, this study demonstrates how to reduce the uncertainty by using the simulator result. Approach using simulator data to decide R index has been demonstrated by Li in the nuclear power plant analysis [16]. In this study, we apply different approaches to decide the R index.

Table 2. Perception and comprehension sensitivity from simulator experiment


The simulator result is explained in Table 2. The simulator experiment is designated with two taskload states: easy where the simulation is under ocean going scenario, and complex for entering-port scenario where stand-by engine procedure must be conducted. Familiarity has a bad state where the first measurement is taken, and good when the repeated
measurement is taken. The sensitivity of perception and comprehension level of situation awareness measured by freeze-probe methods under signal detection theory (SDT) [17,18]. The higher number on it means the ability of each participant to discriminate between the false alarm and correct rejection of the questioned parameter is better. The participants P1 until P8 are categorized with expertise state high, and P9 until P16 categorized with expertise state low. Within this data, two thresholds are applied to categorize the measurement result into three states: low, mediate, and high. Important to note that the average mediate state should have the larger number of distributions.

Table 3. Simulator result distribution for perception


Table 4. Simulator result distribution for comprehension


The assigned conditional probability retrieved from the simulator result was then compared with the conditional probability from the Bayesian network with R value varied from 0 to 5 . We simply assign RMSE function as stated below to decide the comparison between probability from simulator data e and the probability from Bayesian model $f$ with scenario $i$ and the state $j$. The $m$ and $n$ explains the numbers of scenario and number states respectively. The R value was then decided based on the comparison which has the lower RMSE. In this case, $R=3.15$ and $R=1.22$ are assigned for calculating with Equation 2 to calculate the CPD for perception and comprehension nodes. The result of each CPD is shown in Table 5 and Table 6 for the perception node and comprehension node, respectively.
$R M S E=\sqrt{\frac{1}{m n} \sum_{i}^{m} \sum_{j=1}^{n}\left(e_{i j}-f_{i j}\right)^{2}}$
Table 5. Perception CPD


Table 6. Comprehension CPD


### 2.1.4 Calculating target node probability

The SA loss as the failure mode in the proposed Bayesian model in this study is binary state; means either the condition meets the true or false state. While the node in the cognitive function and performance shaping factor level is constructed by three states, the following step is necessary to align it with the failure mode level. The condition probability distribution in the cognitive function is assigned as equation below.
$P_{f}=P_{\text {basic }} \sum_{i=1}^{n} w_{i} \sum_{k=a}^{f} P_{i k} Q_{i k}$
The conditional probability of failure mode node $P_{f}$ is calculated based on the probability of each parent cognitive function node $P_{i k}$ with states $k=a, b, c$. The weighted value $w_{i}$ is retrieved from subject-matter experts like the previous step in weighting the PSF nodes. $Q_{i k}$ is the corresponding adjustment for the $P_{\text {basic. }}$ We follow the practice by Li to use $P_{\text {basic }}=0.01$ as the basic probability of error in SA, and 100 -fold as the number of compromise adjustment. This configuration will made the adjustment factor for parent nodes state to have $Q_{i k}=0.01, Q_{i k}=1, Q_{i k}=100$ for parent node high, mediate, and low respectively.

Given the example, when the Task-load is Complex, Experience is high, and familiarity is bad, the probability distribution of perception is 0.13 , 0.64 , and 0.23 from Table 5, and the probability distribution comprehension is $0.29,0.46$, and 0.25 . Where the weighting can be retrieved from the previous explanation of subject matter experts. The probability of SA loss given this condition can be calculated as follow:
$P_{\text {loss }}=P_{\text {basic }}\left(0.14+(0.13 \times 0.01 \times 0.64 \times 1+0.23 \times 100)+0.86+(0.29 \times 0.01 \times 0.46 \times 1+0.25 \times 100)\right)=$ $=0.253$
![img-3.jpeg](img-3.jpeg)

Figure 4. SA loss probability comparison from Bayesian network and expert expectation

The result from the Bayesian network modelling is shown in Figure 4. The comparison includes the expert expectation that was measured using the free scale on the paper. The expert given the condition of simulator result and asked how likely the participant will fail in attaining the SA in each scenario. The validation is not with an aim to validate until the level of unit, but the tendency of the pattern comparison. It can be accepted the Bayesian network result is follow the expert expectation pattern at the most, except in interception of scenario familiarity is good and expertise is low, the Bayesian network result have tendency to have higher probability in these scenarios.

### 2.2 Model updating

$$
P(H \mid D)=P(H) \frac{P(D \mid H)}{P(D)}
$$

In this model updating method, the calculated probability for each combination of performanceshaping factor, cognitive function, and failure mode will be re-calculated given the condition if the new simulator data exists. The method is based on the Bayesian inference as explained in the equation below. The aim is to update the posterior distribution $P(H \mid D)$ with the prior known information distribution $P(H)$ with collected data from likelihood model $P(D \mid H)$ that normalized with probability of distribution $P(D)$ The Bayesian inference able to use every time the new data exists, means the posterior data from one modelling process became prior data for the next modelling study or stage.

### 2.2.1 Prior distribution construction

Regarding SA loss as the one factor for human error event, it can be explained using the binomial distribution explained by equation below. The distribution expresses the uncertainty about the number of failures $x$ occurred in the given condition of demands $n$ with the parameter probability of failure $p$. This parameter $p$ is uncertain that sometimes derived from expert judgment or data. Groth et al suggest the p can be retrieved by using the Bayesian inference [19].

$$
f(x \mid p)=\binom{n}{x} p^{x}(1-p)^{n-x}
$$

We used the same approach as the previous method in deciding the $p$ by using the beta distribution. Probability density function as shown in below equation express the beta function $B(\alpha, \beta)$ with function to normalize the distribution. From with explanation from Groth et al, the distribution can be conjugated with binomial distribution, where posterior distribution parameters $\alpha_{\text {post }}$ and $\beta_{\text {post }}$ are assigned using equation below [19]. The next step in using Bayesian inference is with assigning the value of $\alpha$ and $\beta$.

$f(p ; \alpha, \beta)=\frac{p^{\alpha-1}(1-p)^{\beta-1}}{B(\alpha, \beta)}$
$\alpha_{\text {post }}=\alpha_{\text {prior }}+x$
$\beta_{\text {post }}=\beta_{\text {prior }}+n-x$
To specify the prior distribution $p_{0}$, we applied the constrained non-information (CNI) distribution [19] As shown in the following equation, the a is estimated as the number of failure contained in the prior distribution, and the denominator $(\alpha+\beta)$ is considered as the number of demands. The beta distribution is constructed by $\alpha=0.5$ and $\beta$ derived from the equation constraint. The extract prior distribution $p_{0}$ from the new existing simulator data is shown in Table 7.
$E(\operatorname{Beta}(\alpha, \beta))=\frac{\alpha}{\alpha+\beta}=E\left(p_{0}\right)$

Table 7. Prior distribution $(p 0)$


### 2.2.2 Posterior distribution updating

Table 8. Simulator result distribution


The process updating the prior distribution with new simulator data can be obtained by utilizing Equation 8. The aims is calculating the posterior distribution $p_{1}$ based on the prior distribution $p_{0}$ and the new distribution parameters $\alpha_{\text {post }}$ and $\beta_{\text {post }}$. For thus, number of failures $x$ occurred in the given condition of demands $n$ need to be defined. Table 8 illustrates the additional simulator result from eight participants with expertise level assumed to be high. In this step, a different approach is used to highlight the participant who has perception or comprehension equal or below 0 are categorized as loss in SA. Based on the categorization, as also shown on Table 9, there are eight trials for each scenario combination, then number of opportunities can be assigned $n=8$, and the number of failure $x$ is assigned in each scenario combination. The $\alpha_{\text {post }}$ and $\beta_{\text {post }}$ is retrieved using Equation 8, and the updated SA loss for selected scenario.

Table 9. Posterior distribution for (p_1)


## 3 DISCUSSION

HRA methods to measure and predict human error in maritime operation are already developed with various methods. The Bayesian network and Bayesian inference is used in this study to demonstrate method which use the simulator data for the probability distribution calculation. The Bayesian network has the advantage of treating the dependencies of PSF, which often treat independent of each other in recent HRA methods. Further, Bayesian inference concept in the second stage demonstrated another possibility to update the probability distribution of human error if the new data from the simulator exists. This has an advantage since there is no necessity to reconstruct the model.

In the first stage of model construction, the threenoode level is introduced. FM were introduced as the possible process or activity that support event led to the human error. Situation awareness is introduced as single FM in this study. CF is introducing as human mechanism in construct the activity, its assigned as dependent variable in simulator experiment. Perception and comprehension were introduced in constructing situation awareness. Last, PSF is introduced as the lowest node in the model. In relation to the simulator experiment, the PSF represents the independent variable. Three PSF are assigned in the model: task-load, expertise, and familiarity. The proposed methods to replace the expert judgment in deciding R-value are demonstrated to reduce the subjective expert judgment uncertainty. However, the input from expert judgment is still mandatory to put the weighting factors between the nodes in the same level node. The second stage demonstrates updating the prior distribution with the Bayesian inference methods. Here the additional simulator data is used to recalculate it into posterior distribution.

The human error probability as the output from the model was compared to the expert expectation for each scenario combination. It is observed that Bayesian network results follow the same pattern as the expert expectation input. However, several comparisons such the scenario with familiarity is good and expertise is low, is have higher evaluation from the Bayesian Network. Thus, the Bayesian network in this model still lacks sensitivity, especially in the scenario which has close result of human error probability.

The general construction of HRA with Bayesian network offers the flexibility to cover more PSF into the model. However, considering the PSF that can be observed in the simulator will limit to detect all PSF exist in other studies. This is the coming limitation of the Bayesian network in HRA context. Thus, the incomplete representation cannot explain the complex

relationship between variables. The second limitation from employing simulator data is, during the session, the participant is well now their performance is being observed. This implies the participants put more effort during the simulation. This must be noted since human error calculation is aimed to measure the error during the normal condition.

Work onboard a ship is divided into big portions of navigation and engine operation work. Defining general PSF that includes the two areas is the future challenge that must be considered. The remaining challenge in HRA is the various definition of the denominator in probability, the number of opportunities for human error which remain wide interpretation for each method. An approach to combine the result of HRA needs an adjustment method to tackle this challenge. Similar to the reliability in hardware, such study may become reference under the IMO guideline to include in the formal safety assessment.
