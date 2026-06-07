# Discovery of Perception Performance Limiting Triggering Conditions in Automated Driving 

Ahmad Adee<br>Corporate Research, Robert Bosch GmbH, Renningen, Germany<br>Ahmad.Adee@de.bosch.com Roman.Gansch@de.bosch.com

Peter Liggesmeyer<br>Software Engineering Institute<br>University of Kaiserslautern,<br>Kaiserslautern, Germany<br>liggesmeyer@cs.uni-kl.de<br>Claudius Glaeser<br>Corporate Research, Robert Bosch GmbH, Renningen, Germany<br>Claudius.Glaeser@de.bosch.com

Florian Drews<br>Corporate Research, Robert Bosch GmbH, Renningen, Germany<br>Florian.Drews@de.bosch.com


#### Abstract

Highly automated driving (HAD) vehicles are complex systems operating in an open context. Performance limitations originating from sensing and understanding the open context under triggering conditions may result in unsafe behavior, thus, need to be identified and modeled. This aspect of safety is also discussed in standardization activities such as ISO 21448, safety of the intended functionality (SOTIF). Although SOTIF provides a non-exhaustive list of scenario factors to identify and analyze performance limitations under triggering conditions, no concrete methodology is yet provided to identify novel triggering conditions.

We propose a methodology to identify and model novel triggering conditions in a scene in order to assess SOTIF using Bayesian network (BN) and p-value hypothesis testing. The experts provide the initial BN structure while the conditional belief tables (CBTs) are learned using dataset. P-value hypothesis testing is used to identify the relevant subset of scenes. These scenes are then analyzed by experts who provide potential triggering conditions present in the scenes. The novel triggering conditions are modeled in the BN and retested. As a case study, we provide p-value hypothesis testing of BN of LIDAR using real world data.

Index Terms-SOTIF, triggering conditions, safety of the intended functionality, Bayesian networks, parameter learning, hypothesis testing


## I. INTRODUCTION

Highly automated driving (HAD) vehicles are safety critical systems deployed in an open context. Their deployment in open context may ensue unsafe and uncertain behavior originating from limitations in perceiving and understanding the open context [1]. As open context brings in a multitude of scenarios, due consideration should be given to model all possible scenario factors that may induce performance limitations, eventually affecting the HAD vehicle performance [2].

Open context also impacts a perception system's (sensor and the associated processing algorithm) capabilities causing

[^0]limitations and/or uncertainties in the performance. Characterization of a perception system in terms of safety requirements or key performance indicators (KPIs) is challenging because their performance is dependent on many external scenario factors. For example, functional performance of a LIDAR based perception system may be influenced by traffic density, occlusion and/or weather conditions [3].

The international organization for standardization (ISO) published the standard, ISO 21448 road vehicles safety of the intended functionality (SOTIF) [2]. SOTIF provides guidelines for the analysis of the performance limitations under the influence of potential triggering conditions that in turn can lead to hazardous behavior. The standard provides a scene centric scenario factor list as a starting point. Moreover, it also includes deductive e.g., cause tree analysis (CTA) and exploratory analysis e.g., system theoretic process analysis (STPA) [4] as tools to model such scenario factors. ISO 21448 [2] advocates the use of exploratory analysis e.g., STPA in cases where the understanding of interaction between system and its context is insufficient. While STPA may provide a good modeling representation, it cannot substantiate the interactions by quantification, to the best knowledge of the authors. In our previous publications [3], [5], we have proposed BN as an alternate modeling tool in this regard.

The BN [6] is a directed acyclic graph (DAG) that consists of nodes and edges. Every node is a random variable $\left(X_{1}, \ldots, X_{n}\right)$. The edges represent a directed relationship between two nodes and run from the parent node $(p a)$ towards the child node $(c h)$. Together, nodes and edges represent the structure of the probabilistic network. The strength of these dependencies is governed by conditional probability distributions $\operatorname{Pr}(c h \mid p a)$ [7]. Mathematically, the BN can be written as follows.

$$
\operatorname{Pr}\left(X_{1}, \ldots, X_{n}\right)=\prod_{i}^{n} \operatorname{Pr}\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

BN is effective in modeling uncertainty and probabilistic


[^0]:    The research leading to these results has received funding from the European Unions Horizon 2020 research and innovation program under the Marie Skoldowska-Curie grant agreement No 812.788 (MSCA-ETN SAS). This publication reflects only the authors view, exempting the European Union from any liability. Project website: http://etn-sas.eu/.

reasoning of a system. It exploits the dependence relationship through the local conditions in the model to perform uncertainty analysis for prediction, classification and causal inference of scenario factors. We provide a methodology to model perception’s performance limitations under triggering conditions in a given scene to assess SOTIF in our previous work [3]. Modeling of the scene into a BN structure is solely based on expert knowledge. The resulting BN structure is fixed and assumed as the best representation of the scene for the given dataset [3]. However, this assumption may not always be true. Due to the open context and a general lack of knowledge about the context and system, modeling all the triggering conditions becomes a very challenging task. Identification of novel triggering conditions becomes specifically important in case of the HAD vehicles deployed in the open context. Moreover, the open context may evolve over time and new phenomena may emerge, even if the initial triggering conditions set was sufficient. For example, the initial guess of an expert about the triggering conditions for the LIDAR performance in terms of false negative (FN) rate can be truncation, reflection and occlusion [3], however, it is also entirely possible that the FN rate is also influenced by the additional triggering conditions such as traffic density.

In this publication, we introduce a methodology to identify and model novel triggering conditions in BN using p-value hypothesis testing. The expert elicited initial BN structure [3] and learned conditional belief tables (CBTs) are subjected to p-value hypothesis testing. This testing results in a small number of relevant scenes that correspond to test dataset, which are deemed inconsistent to the initial BN structure and CBTs, thus serving as a quality metric for the initial BN. Experts then analyze the scenes in order to identify novel triggering conditions. These new expert opinions (in terms of novel triggering conditions) are modeled and validated through p-value hypothesis testing on the new BN structure and the learned CBTs. Summarizing, we test the assumption of best representation of the scene through p-value hypothesis testing. We provide the following contributions.

- We introduce a methodology to model novel triggering conditions in a scene to assess SOTIF by using p-value hypothesis testing on BN structure and learned CBTs.
- We introduce a scene-based definition of local neighborhood and hypothesis testing.
- We implement the methodology on a LIDAR case study in which we use real world dataset to accept or reject novel triggering conditions.

The publication is structured as follows: sec. II presents the proposed methodology. Sec. III briefly describes the setup used for data acquisition. Sec. IV provides the application of proposed methodology on LIDAR perception. In sec. V, results of the implementation are evaluated. Sec. VI provides limitations of the methodology while sec. VII presents an overview of the state of the art. Finally, in sec. VIII we discuss conclusion and future work.

![img-0.jpeg](img-0.jpeg)

Fig. 1: Flowchart describing the flow of the proposed methodology. SOTIF relevant scenario factors and expert knowledge are encoded into scene model defined by the BN structure. The shaded steps are part of previous publication [3]. Established CBTs (after parameter learning) are tested with p-value hypothesis and relevant scenarios are extracted, refinement steps are introduced and retested till a sufficiently accurate BN is achieved.

## II. PROPOSED METHODOLOGY

Fig. 1 shows the flowchart of the methodology we adopt in this publication. We introduce a methodology to discover novel triggering conditions and the dependence relationship in a scene with respect to the initially proposed BN. We then model, quantify and verify the potential triggering conditions. The experts provide the initial structure of BN while the conditional belief tables (CBTs) are learned from the training dataset. We then perform hypothesis tests on the learned BN using p-values statistics [8]–[10], which result in subset of relevant scenes. These scenes are then analyzed by the experts, and they provide refinement strategies, accordingly. Since this publication is focused on the SOTIF, we provide SOTIF relevant triggering conditions as input to model the causal relations [3]. However, the underlying methodology is generic and can be applied to diverse domains.

### A. Model of the Causal Relation

Modeling the initial set of the causal relations is an important step of the methodology. We utilize the step described in our previous work [3] to model the causal relation and summarize it as follows.

SOTIF related undesired behavior (e.g., braking when it is not required and vice versa) may originate from performance limitations e.g., higher FP and FN rate [2]. Apart from FP

![img-1.jpeg](img-1.jpeg)

Fig. 2: BN based on the SOTIF relevant scenario factors and expert knowledge describing the causal structure used in our implementation.

and FN, positional error, contour matching, classification as well as regression quality can also be modeled as performance limitations.

We utilize the scenario factors from ISO 21448 [2] as well as expert opinion, previous data and existing setup (constraint on data acquisition and/or data labels) to model the scene in our methodology (Fig. 1). The work uses BN structure modeling for this purpose. Traditionally, the BN structure modeling is based either on the expert knowledge [11] or on the learning from data (structure learning) [12]. However, in structure learning from data the number of graph candidates grow exponentially with the number of variables in the data [13]. Modeling causal relations is also challenging using the structure learning techniques. Due to this, we opt for the former technique in this work.

Scene description which includes SOTIF relevant triggering conditions and corresponding performance limitations constitute the nodes of the BN structure. As a first step towards derivation of the structure, the experts establish hierarchical dependencies between performance limitations and triggering conditions of the scene. They then provide propositions based on these hierarchical dependencies e.g., the proposition p1: high occlusion may result in higher FNs. We then construct BN from these propositions e.g., the proposition p1 is modeled as an explicit node (Fig. 2).

### *B. Parameter Learning*

Dataset **D** obtained and used in this work consists of fully observed instances of the BN variables.

$$
\mathcal{D} = \xi[1], \dots, \xi[M] \tag{2}
$$

Where **ξ[.]** represents a data instance and **M** represents the number of instances in **D**. We use *train* and *test* subscripts to refer *train* and *test datasets*, respectively.

We execute ad-hoc steps to calculate any missing variables of the BN in the dataset. For example, data instances may not be labeled with FNs. With BN structure (Sec. II-A) determined and corresponding data acquired, the CBTs can be learned. We determine the CBTs and thus the strength of the dependencies by utilizing the maximum likelihood estimator (MLE) [7]. Given a variable **X** with parents **U**, we will have a parameter **θ**<sub>x|u</sub> for each combination of **x ∈ Val(X)** and **u ∈ Val(U)** for a CBT. The likelihood function is as follows.

$$
\begin{split}
L_X(\theta_{X|U} : \mathcal{D}_{train}) &= \prod_{m} \theta_{x[m|u|m]} \\
&= \prod_{u \in Val(\mathbf{U})} \prod_{x \in Val(X)} \theta_{x|u}^{M_{train}[u, x]}
\end{split} \tag{3}
$$

Here **θ**<sub>x|u</sub> represents the parameter to be learned and **m** represents the m<sup>th</sup> data instance in the dataset. Maximizing the likelihood function from Eq. 3 results in the learned parameter.

$$
\theta_{x|\mathbf{u}} = \frac{M_{train}[\mathbf{u}, x]}{M_{train}[\mathbf{u}]} \tag{4}
$$

Where **M**<sub>train</sub>[**u**, **x]** represents the combined occurrence of **u** and **x**. Eq. 4 defines the MLE. It is important to note that this learning scheme is implemented on the train dataset.

### *C. Conditional Belief Likelihood Assignment*

Given the BN structure (Sec. II-A) and learned CBTs (Sec. II-B), we calculate the conditional belief likelihood.

$$
CBL_{x|\mathbf{u}}^{j} = \xi[j]_{x|\mathbf{u}} = \theta_{x|\mathbf{u}} \tag{5}
$$

In the above equation, **j ∈ M**, **CBL**<sub>x|u</sub> **i** or **ξ[j]x|u** corresponds to realization of attribute **x** given realization of its parents **u** in the jth data instance. For example, if **x : FN(Yes)** given its parents nodes **u** : **Truncation (Yes)**, **Reflection (Yes)**, **Occlusion (Largely Occluded)** corresponds to jth row, then **CBL**<sub>x|u</sub> **i** assignment corresponds to **θx|u**. The CBL assignment is performed for both train and test datasets.

### *D. P-values Calculation*

P-values calculation have been used for null hypothesis testing in BN [8]–[10]. The p-value can be defined as the probability of obtaining test results that are at least equally rare or rarer than observed results. Ranges in the p-values have been defined to handle ties in the conditional probabilities (CBLs in our case) [9], [10]. The calculation of p-value ranges for the test dataset estimates relative frequency of equally rare or rarer CBL in the train dataset.

$$
\begin{aligned}
M_{lower}^{CBL_{x|\mathbf{u}}^{j}} &= \sum_{k \in \mathcal{D}_{train}} I(CBL_{x|\mathbf{u}}^{k} < CBL_{x|\mathbf{u}}^{j}) \\
M_{equal}^{CBL_{x|\mathbf{u}}^{j}} &= \sum_{k \in \mathcal{D}_{train}} I(CBL_{x|\mathbf{u}}^{k} = CBL_{x|\mathbf{u}}^{j})
\end{aligned} \tag{6}
$$

Consequently, the p-value ranges can be defined as.

$$
\begin{split}
p_{x|\mathbf{u}}^{j} &= [p_{min}(p_{x|\mathbf{u}}^{j}), p_{max}(p_{x|\mathbf{u}}^{j})] \\
&= \left[\frac{M_{lower}^{CBL_{x|\mathbf{u}}^{j}}}{M_{train} + 1}, \frac{M_{lower}^{CBL_{x|\mathbf{u}}^{j}} + M_{equal}^{CBL_{x|\mathbf{u}}^{j}}}{M_{train} + 1}\right]
\end{split} \tag{7}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3: Scene representing the causal relations "cars loaded on a trailer", "ground truth labeling errors" and "vehicle activity".

Where $M_{train}$ corresponds to number of training data instances.

### *E. Significance Calculation*

We quantify significance by statistical hypothesis testing of the calculated p-values (Sec. II-D). For a single p-value an indicator quantifying the significance at level $\alpha$ can be mathematically written as follows [9].

$$n_{\alpha}(p) = I(p \leq \alpha) \tag{9}$$

This definition can be extended to p-value ranges. Eq. 9 for p-value ranges can be written as follows.

$$n_{\alpha}(p_{x|u}^{j}) = \begin{cases} 0 & \text{if } p_{min}(p_{x|u}^{j}) > \alpha \\ 1 & \text{if } p_{max}(p_{x|u}^{j}) < \alpha \\ \frac{\alpha - p_{min}(p_{x|u}^{j})}{p_{max}(p_{x|u}^{j}) - p_{min}(p_{x|u}^{j})} & \text{otherwise} \end{cases} \tag{10}$$

### *F. Local Neighborhood Definition*

We believe that data instances produced by the same scene or process follow a similarity constraint, constituting a local neighborhood. Local neighborhood in the dataset can be defined by the traditional distance-based method [9] e.g., Euclidean distance for continuous and Jaccard index for categorical data instances. However, we introduce a scene level local neighborhood by combining the scene data instances into a distinct neighborhood. An image equivalent to one such scene is shown in Fig. 3. The red annotated bounding boxes represent ground truth data instances while the blue annotated bounding boxes represent detection data instances of LIDAR datasets. This definition of local neighborhood emphasizes that scenes in the test dataset can be as different as the significance level $\alpha$.

### *G. Relevant Scene Identification*

Once we establish the local neighborhood, we calculate the relevant scenes to be analyzed, by using the following mathematical notations for a local neighborhood $S$ defined by a scene.

$$N_{\alpha}(S) = \sum n_{\alpha}(p_{x|u}^{j}) \tag{11}$$

$$N(S) = \sum I \tag{12}$$

Scenes that satisfy the inequality $N_{\alpha}(S) > \alpha N(S)$ are considered relevant scenes and further analyzed. Specifically, the relevant scenes define rarer p-values in the obtained test results.

This step can be provided for any number of nodes in the initial BN structure i.e., this step can be performed for any node/combination of nodes in the BN shown in Fig. 2. However, in this work we confine to a single node of the initial BN within a given iteration/implementation of the methodology.

### *H. Relevant Scene Causal Relation*

Every scene identified in the previous section is subject to expert analysis. In our proposed methodology, the experts assess the scene under two probable explanations, which are discussed as follows.

*1) Acceptable Random Occurrences:* Experts may find scenes in which no novel triggering condition is identifiable. These scenes are considered as acceptable random occurrences. This means that no novel triggering condition can be identified by the expert through the analysis of this scene.

*2) Novel Triggering Condition Identifiable:* Experts may find scenes in which novel triggering conditions are identifiable i.e., they define relevant triggering conditions that should be taken into account in the BN structure to assess SOTIF. For example, the experts may observe traffic density as a triggering condition in the extracted scenes, that needs to be modeled in the BN.

### *I. Refinement*

Triggering conditions identified by the experts (Sec. II-H2) are then modeled into the BN structure through the refinement step. Koller et al. [7] define four possible edge trails to model a variable into a BN. We only consider direct causal edge trail and confounding causal edge trail for the novel triggering conditions (Fig. 4). Apart from this, we also test the initial BN structure by removing a triggering condition.

*1) Direct Causal Edge Trail (DCET):* This is the simplest case, in which the novel triggering condition directly effects a node in the existing BN (Fig. 4(a)).

*2) Confounding Causal Edge Trail (CCET):* A confounding variable is a variable that influences both the dependent variable and independent variable, causing a spurious association (Fig. 4(b)). This occurs when the novel triggering condition controls two nodes in the existing BN simultaneously.

Mathematically, CCET will produce a similar number of relevant scenes as DCET for a given variable in a hypothesis test, since the CCET does not change the parents of the variable. However, if the p-value hypothesis testing is performed for both independent (parent node) and dependent variable (child node) and a DCET is established for both variables, the validation results can be indicative of confounding phenomena. For example, suppose FN has a parent node occlusion while the human expert identifies traffic density as the novel triggering condition. In order to establish a CCET, we have to validate the DCET of traffic density for both FN and occlusion.

![img-3.jpeg](img-3.jpeg)

Fig. 4: Refinement steps considered in this publication (a) Direct causal edge trail (DCET) (b) Confounding causal edge trail (CCET)
3) Triggering Condition Removal: This refinement step challenges the initial BN structure proposed by the experts (Sec. II-A). Some nodes introduced in the initial BN structure may not validate the hypothesis test. For example, truncation, while included initially by the experts (Fig. 2), may not be a relevant triggering condition given the dataset.

## J. Validation

Once the refinement step is taken, the BN can be tested for the relevant scene score (RSS) before and after the adjustment performed in the refinement step. This step of the implementation requires labeled data for the identified triggering conditions in order to learn the CBTs, which we consider to be made available in an iterative development approach. The validation process includes defining a valid proposition $N T C$ for a novel triggering condition from an algorithmic standpoint and final conclusion from the expert's standpoint as described in Algorithm 1.

```
Algorithm 1 Validation Algorithm Flow
    if \(\left(R S S_{\text {initial }}^{\text {node }}>R S S_{\text {after }}^{\text {node }}\right)\) then
        proposition \(_{N T C}=\) valid
        Expert Conclusion \(=\)
        Accepted Proposition or Inconclusive Evidence
    else if \(\left(R S S_{\text {initial }}^{\text {node }}<R S S_{\text {after }}^{\text {node }}\right)\) then
        proposition \(_{N T C}=\) invalid
        Expert Conclusion \(=\)
        Rejected Proposition or Inconclusive Evidence
    end if
```

Where $N T C$ is the novel triggering condition, $R S S_{\text {initial }}^{\text {node }}$ is the relevant scene score before the modification in the BN and $R S S_{\text {after }}^{\text {node }}$ is the relevant scene score after the modification in the BN, relative to existing BN node. It is worth noticing that a valid proposition for a novel triggering condition proposition $N T C$ may or may not be accepted by the experts. The experts may accept a proposition based on the difference between $R S S_{\text {initial }}^{\text {node }}$ and $R S S_{\text {after }}^{\text {node }}$, representatives of data, past experience and knowledge etc. Novel triggering
conditions that are accepted by the experts are finally included in the modified BN. This decision criteria differs significantly from purely data driven approaches, where the decision is generally based on the results of an algorithm.

## III. EXPERIMENTAL SETUP

The experimental setup consists of two Hesai Pandar 64 and two Velodyne Ultra Puck VLP-32C LIDAR sensors installed on the roof corners of a car. The recorded data consists of different labels including bounding boxes, pose, visibility state and vehicle activity among others surrounding $360^{\circ}$ of the HAD vehicle. Two separate datasets are available that correspond to detection and ground truth. Every detection and ground truth are labeled as a blue and red bounding box (Fig. 3). Most of the data was collected on different highways of Europe. However, part of the collected data also belongs to urban roads. The data consists of around twenty thousand instances. A deep neural network (DNN) was trained and used as the processing algorithm. Two experts provided their opinions on LIDAR insufficiencies, triggering conditions and limitations.

## IV. IMPLEMENTATION

In this section, we demonstrate the application of our methodology on the LIDAR sensing dataset discussed in the previous section. We do not discuss Sec. II-C and Sec. II-D as they are purely mathematical calculations. Moreover, we discuss Sec. II-G, Sec. II-H, Sec. II-I and Sec. II-J as part of the result section (Sec. V).

## A. Model of the Causal Relation

The experts provide the list that constitutes the triggering conditions that may initiate the performance limitation of LIDAR perception system (Sec. II-A). Based on the available data labels, scenario factors and experts' inputs, we conclude seven variables as SOTIF relevant performance limitation and triggering conditions. The leaf node, FN defines the performance limitation while the rest of the causal structure describes how the triggering conditions may impact the performance limitation (Fig. 2). Occlusion and truncation are both defined analogously to the KITTI benchmark [14] and both represent the visibility state of an object.

We use the BN structure from a previous publication [3]. The experts provide the following initial propositions for SOTIF relevant scenario factors.
a) Proposition 1: Truncation and occlusion in detection may influence $F N$ rate.
b) Proposition 2: Weather conditions may effect road conditions and scene illumination, which in turn can effect the $F N$ rate.
c) Proposition 3: Road condition and scene illumination can effect reflection in the scene, which in turn can effect the $F N$ rate.
The resulting BN structure is shown in Fig. 2.

### B. Parameter Learning

The dataset has all the labels of our initial BN structure (Fig. 2) except FN. We calculate FN using mean squared error (MSE) for each data instance.

$MSE=\frac{1}{n}\sum_{i=0}^{n}(Y_{i}-\hat{Y}_{i})^{2}$ (13)

Where $n$ represents number of samples, $Y_{i}$ represents the ground truth and $\hat{Y}_{i}$ represents the detection. We execute Eq. 13 using $x$ and $y$ values of individual detection and ground truth data instance to find a correspondence between them. All those data instance from ground truth that has no correspondence from detection using MSE are considered to be FN. We consider data instances with $|x|<140$ meters and $|y|<50$ meters as the DNN was trained for this range. We perform random division of train and test datasets (80$\%$ and 20$\%$) in order to perform parameter learning using Eq. 4.

### C. Significance Calculation

In order to perform significance calculation, we choose significance level $\alpha$ at $5\%$. We make this choice purely on the premise that p-value hypothesis testing is also performed at the same level of $\alpha$ in the state of the art [9].

### D. Local Neighborhood Definition

We define local neighborhood of test datasets based on the scenes they represent. This selection of local neighborhood equips us to identify the relevant scenes which are subject to refinement (Sec. V-A) rather than identification of distance-based subsets of data instances. One such scene is shown in Fig. 3.

## V. Results

In this section, we present the results obtained by the application of our methodology. For simplicity and completeness, we adopt the following patterns in the results.

- We provide the hypothesis testing and relevant scene identification for FN, truncation, occlusion and reflection nodes from the initial BN (Fig. 5).
- We select traffic density, vehicle activity and context from the relevant scene causal relation step for refinement and validation (Fig. 6(a)). Moreover, we perform the refinement step for all three selected casual relations with respect to FN only.
- We perform CCET refinement and corresponding validation on traffic density with FN and its two parent nodes i.e., reflection and occlusion (Fig. 6(b)).
- We perform triggering condition removal step on the truncation node (Fig. 6(a)).

### A. Relevant Scene Identification

We identify varying number of relevant scenes depending upon the randomization on the train and test dataset selection as well as the relevant nodes for which the relevant scene identification is performed. The $RSS_{\text{initial}}^{\text{node}}$ for node: FN, occlusion and reflection is shown in Fig. 5. There is a general decrease in the number of identified scenes (3.68% of the test dataset scenes on average). A relatively small number of relevant scenes indicate that the test dataset is similar to train dataset.

![img-4.jpeg](img-4.jpeg)

Fig. 5: Relevant Scene Score (RSS) for hypothesis testing of FN, occlusion and reflection RSS here represents the numbers of scenes rarer at significance level $\alpha$ before any modification in the BN structure.

### B. Relevant Scene Causal Relations

We believe that the higher number of RSS provides the best opportunity to experts to identify relevant scene causal relations. Thus, we take the cases in which the RSS is the highest.

TABLE I: Relevant scene causal relations and the respective acceptable random occurrences and identifiable novel triggering conditions cases. Identification of the triggering conditions is based on the expert opinion.


1) Acceptable Random Occurrences: The expert analysis of the identified relevant scenes results in 29, 56 and 10 scenes from FN, occlusion and reflection tests in which no novel triggering condition can be identified (Tab. I). We believe that the results do not assert that no novel triggering condition is present in these scenes. We merely believe that the experts cannot provide a probable explanation of relevancy from the novel triggering conditions standpoint. 2) Novel Triggering Condition Identifiable: The expert analysis of the identified relevant scenes results in 33, 65 and 13 scenes from FN, occlusion and reflection tests in which some novel triggering conditions can be identified (Tab. I). The identified novel triggering conditions for FN hypothesis testing are listed in Tab. II. A representative scene containing three novel triggering condition from the expert guess "cars loaded on a trailer", "ground truth labeling errors" and "vehicle activity" is shown in Fig. 3.

TABLE II: Identified novel triggering conditions by FN's p-value hypothesis testing. Expert analyzes the relevant scenes identified through hypothesis testing. Triggering conditions are then provided by the experts.


### C. Refinement

Among the potentially novel triggering conditions mentioned (Tab. II), we only discuss traffic density, context and vehicle activity in detail in the refinement step. We make this selection for the following reasons.

- The selected causal relations have relatively high number of occurrences.
- The selected causal relations have labeled data available. This selection is specific to the scope of this publication. Data labels must be made available for any selection of causal relation, if required.

The experts provide the following propositions.

- Traffic density, vehicle activity and context may effect the defined performance limitation i.e., FN (Fig.4(a)).
- Traffic density may effect FN, occlusion and reflection. This proposition specifically focuses on the CCET case (Fig.4(b)).
- Truncation may not have any effect on the defined performance limitation i.e., FN.

By combining the results of the first two propositions and establishing DCET, the expert can establish CCET e.g., DCET of FN and occlusion with the traffic density may result in a CCET. We implement DCET and CCET (Sec. II-I1) for traffic density only. The propositions can be supported by the intuition of the causal relations proposed by the experts i.e., apart from the SOTIF related measure (FN), vehicle activity and context of driving are not the cause or effect of any other node in our BN.

### D. Validation

We provide validation of expert analysis by using Algorithm 1.

1) Traffic Density: We define 4 states of the traffic density; from “low” to “very high”. Traffic density as a triggering condition may not be very intuitive for a data instance, however, it defines the class of scenes the data instance belongs to. The validation results of the DCET (Sec. II-I1) are shown

![img-5.jpeg](img-5.jpeg)

Fig. 6: (a) Relative relevant scene score of refinement of DCET for FN using traffic density, vehicle activity, context and without truncation as identified novel triggering conditions. Lower value after the DCET refinement indicates a more suitable BN structure than the structure considered before. (b) Relative relevant scene score of refinement of traffic density as DCET of FN, occlusion and reflection. The circles in the plot refer to the outlier relative RSS among the iterations.

in Fig. 6(a) and Fig. 6(b). The following validation results can be extracted using Algorithm. 1.

$$
\begin{aligned}
\text { proposition }_{TD \rightarrow FN} & =\text { valid } \Longleftarrow R S S_{\text {initial }}^{FN}>R S S_{\text {after }}^{FN} \\
\text { proposition }_{TD \rightarrow O c c} & =\text { valid } \Longleftarrow R S S_{\text {initial }}^{O c c}>R S S_{\text {after }}^{O c c} \\
\text { proposition }_{TD \rightarrow R e f} & =\text { invalid } \Longleftarrow R S S_{\text {initial }}^{R e f}<R S S_{\text {after }}^{R e f}
\end{aligned}
$$

where:
$T D=$ traffic density
$O c c=$ occlusion
$R e f=$ reflection
The experts draw the following conclusions.

- Traffic density impacts the FN rate and occlusion.
- CCET trail is the most suitable construction for traffic density with occlusion and reflection.
- Traffic density is not a triggering condition for reflection.

2) Context: Two driving contexts are available in the data.

- Highway: Represented by 199645 points
- Urban: Represented by 863 points

The validation results of the DCET from context to FN is shown in Fig. 6(a). We observe a general decrease in the relevant scenes after the adjustment in the BN structure. Algorithm 1 provides the validity of the proposition.
proposition $_{C o n \rightarrow F N}=$ valid $\Longleftarrow R S S_{\text {initial }}^{F N}>R S S_{\text {after }}^{F N}$
where:
Con $=$ context
However, the decrease in the RSS is not substantial, primarily due to lack of representation of the urban context in

the data from the experts’ standpoint. The experts draw the following conclusions.

- Context of driving may impact FN rate, however, more data is required to substantiate this claim.
3) Vehicle Activity: Vehicle activity consists of “parked”, “stopped”, “moving” and “other” states. The validation results of the DCET for vehicle activity as a triggering condition is shown in (Fig. 6(a)). We observe an increase in the RSS after the adjustment in the BN structure. Algorithm 1 provides the validity of the proposition.

$$
\text { proposition }_{V A \rightarrow F N}=\text { invalid } \Longleftarrow R S S_{\text {initial }}^{F N}<R S S_{\text {after }}^{F N}
$$

where:
$V A=$ vehicle activity
The experts draw the following conclusions.

- The proposition is not valid. Vehicle activity cannot be taken as a triggering condition for FN at this point.

4) Truncation Removal: The validation results of the DCET for truncation removal as a triggering condition is shown in (Fig. 6(a)). We observe a slight increase in the RSS when truncation is not taken as a triggering condition. Algorithm 1 provides the validity of the proposition.
proposition $_{\text {Trun } \rightarrow F N}=$ valid $\Longleftarrow R S S_{\text {initial }}^{F N}<R S S_{\text {after }}^{F N}$
where:
Trun $=$ truncation
The experts draw the following conclusions.

- Truncation removal has inconclusive evidence. More data is required to substantiate further claim.
Tab. III summarizes the results of our implementation. The results validated and analyzed by the experts to provide final conclusions using Algorithm 1.

TABLE III: Summary of the results produced by the implementation of the methodology. Different initial nodes, systematic factors and refinements are considered in the implementation. Abbreviations : Al. - Algorithm, Pro ${ }_{N T C}-$ proposition $_{N T C}$


The resulting BN structure is shown in Fig. 7. We make adjustments in the BN structure by adding traffic density as CCET for FN and occlusion. With more data, the decision about driving context and truncation can also be made. In this way, novel triggering conditions can be identified, refinements can be generated and validation of those refinements can be performed in iterations to acquire more knowledge and perform a robust SOTIF analysis.
![img-6.jpeg](img-6.jpeg)

Fig. 7: BN structure from Fig. 2 updated with novel triggering condition traffic density as SOTIF relevant scenario factor for false negative and occlusion.

## VI. Limitation of the Methodology

We perform validation of our methodology by introducing prescribed nodes in the BN structure and calculating the new RSS. We observe a substantial decrease in the RSS after modeling traffic density as a triggering condition. However, finding all the underlying triggering conditions is a challenging task. The algorithm presented in this work substantiates the triggering conditions of rare events in its true sense. We also presume that there are certain assumptions taken that are worth discussing to understand the limitation of the methodology.

## A. Training and Test Data

The most important assumptions we take are related to train and test datasets.

- Train dataset does not contain any scenes that belong to rare scene family.
- Test dataset contains scenes that belong to rare scene family.
However, this may not always be the case. Generally, test datasets are segregated from the training datasets and they are highly correlated. We believe that randomizing the selection of datasets (e.g., Monte Carlo) can help us optimize the best solutions [15].


## B. Resemblance to Structure Learning

A potential objection to the methodology presented can be its resemblance with the structure learning technique. Though our methodology enhances the structure by identifying novel triggering conditions, yet our methodology has the following distinct features.

- We believe that a human expert plays a key role in the construction of safety analysis models. This is reflected in our methodology and is a missing feature in any structure learning technique.
- A human expert may identify potential triggering conditions that may not be the part of labeled data. This implies that the new BN structure may acquire causal relation not present in the initial dataset (after performing new labels). Structure learning is only confined to what is available in the form of data.

## C. Availability of the Labeled Data

Availability of labeled data is very important for the proposed methodology. It may happen that the data is not available for some of the prescribed scene causal relation. For example, labels are not available for "cars loaded on a trailer", "ground truth labeling error", "construction activity" and "other lane height". We believe that the unavailability of labeled data can be addressed by the following methods.
a) Labeling Automation: Manual data labeling is a labor intensive and expensive task. However, part of the labeling process can be automated.
b) Label Ranks: If limited resources hinder the labeling process, a ranking of labels based on some structured method e.g. Phenomena Identification and Ranking Table (PIRT) [16] can be used.

## D. Argumentation on Completeness

Providing argumentation on the completeness of the safety model produced by our methodology to assess SOTIF is still a challenging task, despite the methods itself help in knowledge acquisition process (and thus improving completeness concerns). Even after multiple iterations of restructuring the BN, the resulting BN might not be complete. Though a conventional solution to the problem can be an expert conclusion and a sufficiency criterion defined on the RSS benchmarking, the resulting BN may not be a robust representation. Consider the following hypothetical scenario.

After restructuring the BN with the inclusion of traffic density as novel triggering condition, the expert conclusion and RSS satisfy the benchmark. However, it is possible that traffic density may not be a confounding variable and its effect on FN may be governed by a third missing variable. Such challenges can be partially solved by understanding the intuition of causal relations about real-world phenomena.

## E. Randomness and Lack of Knowledge Decoupling

A general conception in the hypothesis testing is the acceptance of randomness of results to a certain significance level $\alpha$. Any value below or above the $\alpha$ (depending upon which tail of the distribution is being tested) results in unacceptable randomness and rejection of the hypothesis. In this work, we go further and instead of rejecting the hypothesis, model it with novel triggering condition. In its essence, this step corresponds to modeling lack of knowledge concepts [17]. The decoupling between randomness and lack of knowledge at some significance level $\alpha$ works with the underlying assumption i.e., any scene relation $N_{\alpha}(S)>\alpha N(S)$ is due to some triggering condition. However, it is also possible that the rarer scene occurrence is purely governed by randomness in the data. We attempt to solve this problem by allowing experts to define scenes as random occurrences (Sec. II-H1).

## VII. Related Work

Recent research indicates an ever-growing interest in SOTIF and scenario-based safety of HAD vehicles as a topic [18]. However, to the best of the authors' knowledge, existing approaches do not contribute to the knowledge acquisition process of identification, modeling, quantification and validation of novel SOTIF relevant scenario factors. Formalization of the reliability-based validation of the environment perception for safe automated driving [19], probabilistic framework for incrementally bounding the residual risk associated with autonomous drivers and its quantification [20] and integrated method for safety assessment of automated driving functions [21] are some of the salient literature studies in this regard. Berk et al. [19] emphasizes on the failure rates of perception as well as quantification of false negative (FN) and false positive (FP) as uncertainties. Edward Schwalb [20] focuses on continuous monitoring of SOTIF for imminent hazard by autonomous driver in order to maximize the time to materialization (TTM) by appropriate selection of actions. Finally, two publications [21], [22] provide identification and quantification of SOTIF related hazardous scenarios by using causal chain analysis techniques. However, the work provides a more theoretical view of the problem.

In the most recent publications [23], [24], the major focus has been on formalization of scenario-based verification and validation. Zhang et al. [23] provide a test framework that consist of test scenarios, different types of testing and allocation of tests, generation of test cases, data collection as well as analysis and correlation of obtained results. Scholtes et al. [24] focuses on structured modeling of urban road environment and traffic using a six-layer model approach.

Finally, Adee et al. [3], propose a novel methodology to model triggering conditions and performance limitations in a scene to assess SOTIF using BN in this regard. The experts provide the BN structure and conditional belief tables are learned using the maximum likelihood estimator. However, the publication takes the underlying assumption that expert provided BN structure are complete and provide the best representation of the scene.

The conceptual usage of BN and p-values hypothesis testing is performed by Mc. Flowland et al. [9], [10] for anomaly pattern detection. The implementation can be distinguished from our work in the following aspects.

- While Mc. Flowland et al. [9], [10] use a structure learning technique for BN structure, we believe the initial BN structure should be provided by the safety experts as discussed in other literature [3].
- In our work, the local neighborhood definition is scene based rather than a more common distance-based defi-

nition. This selection changes the entire rationale of the implementation and is a salient feature of our implementation.

- We close the loop by expert oriented reasoning of anomalies and provision of new BN structure that better suits our world knowledge.
- Moreover, the overall theme of the work by Mc. Flowland et al. [9], [10] is to provide an inference algorithm for pattern detection, while we focus on the SOTIF oriented triggering condition discovery.


## VIII. CONCLUSION AND Future Work

We presented a methodology to discover novel triggering conditions under the scene model to argue safety of the intended functionality (SOTIF) analysis. The methodology encodes parameter learning for Bayesian network (BN) and p-value testing of the learned BN.

This methodology particularly assists in the identification of novel SOTIF related triggering conditions under manageable effort. The identified novel triggering conditions are then modeled in the BN and validated through testing. This assists the experts to establish SOTIF modification plan for the identified performance limitation under the novel triggering conditions.

We believe that the contribution we make with this publication is very valuable from the SOTIF standpoint. Analyzing thousands of scenes to identify potentially novel triggering conditions is not feasible. Our approach curtails the number of scenes to a very small number (around $\mathbf{3 \%}$ of the total in test dataset), making the analysis feasible.

In order to argue the adequacy of the approach, LIDAR performance was studied given a scene. The scene was modeled using a BN structure and parameter learning was performed using real world data to elicit conditional belief tables (CBTs). P-value testing was performed on the learned BN and relevant scenes were extracted. These scenes were then analyzed by experts to identify the triggering conditions.

We also evaluated the decrease in the number of identified scenes and observed roughly a $\mathbf{2 5 \%}$ decrease in case of traffic density as newly modeled triggering condition for $F N$ and roughly $\mathbf{5 0 \%}$ for occlusion. We then discussed the limitations of the methodology.

In future, we intend to explore other hypothesis testing techniques against BN models. We also intend to provide a general framework which covers novel triggering condition identification based on rare events.
