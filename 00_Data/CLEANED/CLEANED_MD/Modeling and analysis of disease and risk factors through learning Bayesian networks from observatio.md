# Modeling and Analysis of Disease and Risk Factors through Learning Bayesian Networks from ObservationalData 

Jing Li ${ }^{1, *, \dagger}$, Jianjun Shi ${ }^{2}$ and Devin Satz ${ }^{3}$<br>${ }^{1}$ Department of Industrial Engineering, Arizona State University, Tempe, AZ 85287-5906, U.S.A.<br>${ }^{2}$ Department of Industrial and Operations Engineering, University of Michigan, Ann Arbor, MI 48109-2117, U.S.A.<br>${ }^{3}$ Synchronous Knowledge Inc., Falls Church, VA 22041, U.S.A.

This paper focuses on identification of the relationships between a disease and its potential risk factors using Bayesian networks in an epidemiologic study, with the emphasis on integrating medical domain knowledge and statistical data analysis. An integrated approach is developed to identify the risk factors associated with patients' occupational histories and is demonstrated using real-world data. This approach includes several steps. First, raw data are preprocessed into a format that is acceptable to the learning algorithms of Bayesian networks. Some important considerations are discussed to address the uniqueness of the data and the challenges of the learning. Second, a Bayesian network is learned from the preprocessed data set by integrating medical domain knowledge and generic learning algorithms. Third, the relationships revealed by the Bayesian network are used for risk factor analysis, including identification of a group of people who share certain common characteristics and have a relatively high probability of developing the disease, and prediction of a person's risk of developing the disease given information on his/her occupational history. Copyright (c) 2007 John Wiley \& Sons, Ltd.

Received 23 September 2007; Accepted 26 September 2007
KEY WORDS: case-control study; causal inference; Bayesian network; epidemiology

## 1. INTRODUCTION

Modeling and analysis of the relationships between a disease and its potential risk factors is important for effective disease diagnosis, control, and prevention in epidemiology. General studies under this objective can be classified into two categories: those based on experiments and those based on observational data. Compared with experimental studies in which the factors of interest are controlled and

[^0]
[^0]:    *Correspondence to: Jing Li, Department of Industrial Engineering, Arizona State University, Tempe, AZ 85287-5906, U.S.A.
    ${ }^{\dagger}$ E-mail: jinglz@asu.edu

their impacts on disease occurrences are evaluated, observational studies are performed based on population sampling, where the investigator has no control over the data collection but utilizes the existing record information. Observational studies are especially advantageous in situations such as when (i) the target disease may result in severe health damage; (ii) risk factor control is inconvenient or even infeasible; and (iii) a large number of potential risk factors need to be studied simultaneously. In all of these cases, it is almost impossible to conduct experiments.

Meanwhile, due to the advancement of computer technologies, a large amount of real-world data can now be collected and warehoused, including patients' clinical records regarding disease diagnoses and treatments; demographic attributes such as gender, age, and race; and behavioral information such as occupational histories (i.e. job type, job location, and time period for performing the job). This data-rich environment creates new opportunities for observational epidemiology. However, there is a lack of effective tools for analyzing the data, discovering the relationships, and making intelligent decisions.

Traditionally, the assessment of the relationship between a disease and a potential risk factor in an observational study was achieved using a variety of association measures ${ }^{1}$. Also, there were statistical methods, such as logistic regression ${ }^{2}$, to quantify both the association and the uncertainty surrounding the estimation of the association. However, these measures and methods paid little attention to the nature of the risk factor and the disease; that is, they did not distinguish between the cause and the effect. Furthermore, the apparent association could even be non-causal due to the confounding effects of other variables. Although the confounding effects can be eliminated by certain data-separation techniques such as stratification ${ }^{1}$, the success of the elimination has to be based on pre-identification of the confounding variables. A complicated scenario arises when the problem is data mining in nature. In this case, most of these traditional approaches may not be effective. Data mining is not targeted at studying the association between the disease and one risk factor, but searches for interesting relationships between the disease and all potential risk factors simultaneously. Without any a priori knowledge about what variables confound which associations, these traditional approaches may not be able to distinguish among different associations (i.e. causal or non-causal) in an effective and efficient manner.

The problem formulation for discovering the relationships between a disease and its potential risk factors in epidemiology is similar to that for data-driven modeling and analysis of the relationships between process variables and product quality variables in quality engineering. In the latter case, Bayesian networks based on massive observational data have been identified as effective tools for studying dependent, independent, and causal relationships ${ }^{3,4}$. Recent years have witnessed the application of quality engineering methods in non-traditional domains such as health care ${ }^{5,6}$ and computer networks ${ }^{7,8}$. As a similar effort, this paper adopts the concepts and methods of Bayesian networks, and combines them with the uniqueness of epidemiologic studies to model and analyze the relationships between a disease and its potential risk factors.

A Bayesian network is an explicit representation of the dependent and independent relationships among variables. Depending on the interpretation, it can also represent causalities ${ }^{9}$. Previous research in epidemiology has focused on using a developed Bayesian network, usually constructed by a priori knowledge, to infer the presence of confounding factors and to compute the strength of the associations ${ }^{1}$. Little has been found on how to develop a Bayesian network from observational data. A Bayesian network developed from observational data provides a way to simultaneously study the causal relationships between the disease and all the potential risk factors of interest. Another important advantage of a Bayesian network is that a priori knowledge from the specific application domain can be incorporated into the learning algorithms of the Bayesian network to improve the learning accuracy and efficiency.

This paper presents an application of Bayesian networks in an epidemiologic study with the objective of identifying the causal relationships between disease occurrences and patients' occupational histories. The proposed approach emphasizes the integration of medical domain knowledge with data preparation and analysis. The focus is on studying the following issues of the disease through the learning and inference

of a Bayesian network:

- Occupational distribution, i.e. whether and how disease occurrences are associated with certain occupations.
- Geographical distribution, i.e. whether and how disease occurrences are associated with certain locations (i.e. geographical location of a job conducted).
- Time-sensitive occupational distribution, i.e. whether and how the association with an occupation varies over time.
- Time-sensitive geographical distribution, i.e. whether and how the association with a location (i.e. geographical location of a job conducted) varies over time.
- Role of demographic attributes, i.e. whether the association with an occupation or a location is due to the confounding effects of other demographic attributes such as gender and age, and what the confounding factors are.

A thorough understanding of the aforementioned issues of the disease helps identify 'who,' 'where,' and 'when,' i.e. what demographic attributes increase the likelihood of developing the disease, in which location was the disease developed, and when was the disease developed. All these provide supporting information to discover the 'what,' i.e. the cause of the disease.

The remainder of this paper is organized as follows. Section 2 describes the data. Section 3 introduces important considerations in data preprocessing. Section 4 demonstrates the use of a Bayesian network to learn the relationships between disease occurrences and potential risk factors. Section 5 discusses how to make inferences based on the Bayesian network. Section 6 provides case studies based on real-world data. Finally, conclusions are given in Section 7.

# 2. DESCRIPTION OF THE DATA 

This research utilizes two data sets. One contains the clinical records of patients (clinical data set), and the other contains information on the patients' occupational histories (occupational data set). In the clinical data set, each row corresponds to one medical appointment and each column corresponds to one clinical or demographic attribute of the patient, including the patient's ID, appointment date, the diagnostic result, age, gender, race, marital status, etc. In the occupational data set, each row corresponds to one patient identified by the patient's ID; and contains the jobs he/she had, the locations of the jobs in chronological order up to the time when the data set was created, and the time period (i.e. the starting and ending dates) of each job. To link the diagnostic result (i.e. the disease) with a patient's occupational history, the clinical and occupational data sets are merged using patient ID as the common variable, and a combined data set is created. This research is based on the combined data set. The data sets, their contents, and their relationships are described in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Description of the data

# 3. DATA PREPROCESSING 

To obtain a meaningful Bayesian network, data preprocessing is critical. During preprocessing, medical domain knowledge can be utilized to transform the variable, de-noise the data, and remove redundant information, in order to facilitate the developing of a Bayesian network. Several important issues are discussed in this section.

### 3.1. Hierarchical grouping of the diagnostic results

The variable 'diagnostic result' contains the disease that a patient was diagnosed with. Different diagnostic results can be grouped together if they are subtypes of a more general type of disease. For example, both yellow fever and mosquito-borne viral encephala belong to arthropod-borne viral diseases. The grouping can be further refined, resulting in a three-level disease hierarchy. The diseases at different levels may have different relationships with the occupational history. For example, the geographical distribution for the occurrences of yellow fever may be different from that of arthropod-borne viral diseases. To obtain a complete understanding of how the occupational history may impact disease occurrences, diseases on all three levels have been studied in this research.

### 3.2. Handling multiple appointment records

In the combined data set, a patient may have more than one appointment record (i.e. multiple rows) with identical diagnostic results. These appointments may all correspond to one occurrence of the disease, where the first appointment in chronological order was the one when the diagnosis was made, and subsequent appointments were made for continuous treatments of the disease. Because the induction of the disease must occur prior to the time of the first appointment, the patient's occupational history after the first appointment is uninformative for identifying the cause of the disease. Thus, there is no need to keep all the appointment records after the first one.

In some cases, multiple appointment records of one patient could also be generated due to disease recurrences or re-infections. Therefore, efforts need to be made to distinguish between the multiple appointments associated with a single disease occurrence and those associated with multiple disease occurrences. By assuming that the successive appointments in the situation of a single disease occurrence have smaller time intervals than those in the situation of multiple disease occurrences, the following criterion is implemented: $t_{A_{i}}$ and $t_{A_{i+1}}$ denote the time of two successive appointments $A_{i}$ and $A_{i+1}$, respectively, and $\Delta t_{M}$ can be obtained from medical awareness on the treatment cycle of the disease.

If $t_{A_{i+1}}-t_{A_{i}}<\Delta t_{M}$, then both $A_{i}$ and $A_{i+1}$ correspond to one single disease occurrence. Otherwise, each of them corresponds to a different disease occurrence.

### 3.3. Estimating the induction time of disease

The combined data set contains a patient's occupational history spanning from the first day his/her information was recorded to the time when the data analysis was initiated. Not all parts of this occupational history are relevant to the disease occurrence. For example, the occupation he/she held after the medical appointment is non-informative. Even for the occupations prior to the appointment, only those during a certain time period could possibly impact the disease occurrence. This period, denoted by $\left[t_{I}^{L}, t_{I}^{U}\right]$, is an estimate of the induction time of the disease based on medical domain knowledge, where $t_{I}^{L}$ and $t_{I}^{U}$ are the estimated lower and upper bounds of the induction time, respectively. The estimation procedure is shown in Figure 2. For a given appointment time, $t_{A}$, an estimate of the time when the symptom of the disease appears $t_{S}$, is first obtained. This can be done either through the medical awareness of how long the symptom can be tolerated by the patient after it appears, or by retrieving more detailed diagnostic information from additional data sets containing the patient's description of his/her disease development. Furthermore, for most diseases in epidemiology, there is a defined incubation period, which is the time between the contraction of a disease and the first appearance of

![img-1.jpeg](img-1.jpeg)

Figure 2. Estimation of the induction time
a symptom. Based on the incubation period, an interval estimate of the induction time $\left[t_{I}^{L}, t_{I}^{U}\right]$ can be achieved.

Because the length of the time interval $\left[t_{I}^{L}, t_{I}^{U}\right]$ is generally much smaller than the time period of a patient staying in one occupation at one location, it is reasonable to assume that his/her occupation and the location of the occupation remain unchanged within $\left[t_{I}^{L}, t_{I}^{U}\right]$. Therefore, although the patient's entire occupational history may contain a series of changes in occupations and locations, only one occupation and one location are kept for each record.

# 3.4. Selecting a control group 

The observational research presented in this paper is a case-control study. Selecting an appropriate control group is important to avoid reaching biased conclusions regarding the relationships between the disease and risk factors. One distinct feature of this study is that there are records only for the people who were sick and hospitalized, but not for the healthy population. Therefore, the subjects in the control group have to be selected from the same source of subjects in the case group, i.e. the patients with diseases different from the disease of the case group in the combined data set. The following principles are used to find such a 'diseased' control group.
(i) If a patient is diagnosed with a disease that is associated with any of the risk factors of interest, he/she cannot be selected as a subject in the control group.

Wacholder et al. ${ }^{10}$ pointed out that the best strategy regarding the selection of the diseases in forming a control group is to exclude all conditions likely to be related to the risk factors of interest. This is based on the consideration that if the disease of the subjects in the control group is related to the risk factors, the association between the disease of the case group and the risk factors may be masked or twisted. Although theoretically attractive, in practice this principle is difficult to implement, as it requires a prior knowledge about the relationship between the disease of a control group candidate and the risk factors. Thus, a second principle is proposed as a supplement.
(ii) If a patient is diagnosed with the disease of the case group or is diagnosed with a disease sharing a common ancestor with the disease of the case group in the disease hierarchy, he/she is not selected as a subject in the control group.

It is reasonable to believe that the diseases belonging to the same disease family are more likely related to the risk factors in the same way as those in different families. Although applying this principle cannot completely exclude the unqualified subjects from the control group defined by principle (i), it narrows the scope of the investigation and helps find the qualified subjects.
(iii) Multiple control groups are preferable to a single control group, with each control group corresponding to a different disease.

The data analysis can be conducted based on each individual control group and then the results are compared. If a certain relationship is found to be concordant across the control groups, a high confidence in the existence of this relationship can be achieved. However, when the results are discordant, additional efforts have to be made to determine which result is correct. Multiple control groups may also be helpful when each group serves a different purpose. For example, if the disease (other than

the disease of the case group) of a control group is known to have little association with location, this control group can be used to study the relationship between the disease of the case group and location. Another control group may be used to study the relationship between the disease of the case group and occupation if the disease of this control group is known to be independent of occupation. The patients from different control groups can also be pooled together to form one control group. The data analysis based on this pooled control group can effectively avoid bias when an individual control group is used.

# 3.5. Data visualization 

Data visualization is important for achieving an initial understanding of data distributions and variable relationships. In this section, several graphical techniques are presented which target the visualization of the time-sensitive geographical and occupational distribution of the disease.

### 3.5.1. Multi-location temporal distribution (MLTD) graph and multi-occupation temporal distribution (MOTD) graph

For each disease occurrence $i$, let $\left(t_{I}^{L}\right)_{i}$ and $\left(t_{I}^{U}\right)_{i}$ denote the starting and ending dates of the estimated induction period of the disease, and $z_{i}$ denote the location, i.e. the location of the patient during this period. The MLTD graph is constructed with the $x$ - and $y$-axes representing the locations and the calendar time, respectively. If the calendar time is in units of days, there will be $\left(t_{I}^{U}\right)_{i}-\left(t_{I}^{L}\right)_{i}+1$ points plotted in the graph for the disease occurrence $i$, with the $x$-coordinates all being $z_{i}$ and $y$-coordinates being $\left(t_{I}^{L}\right)_{i},\left(t_{I}^{L}\right)_{i}+$ $1, \ldots,\left(t_{I}^{U}\right)_{i}$. To avoid the overlap of the points from different disease instances, two random numbers, $U_{1}$ and $U_{2}$, are generated and added to the $x$ - and $y$-coordinates of each point, respectively. Thus, the resulting points plotted in the graph have the coordinates $z_{i}+U_{1}$ and $\left(t_{I}^{L}\right)_{i}+k+U_{2}, k=0, \ldots,\left(t_{I}^{U}\right)_{i}-\left(t_{I}^{L}\right)_{i}$, where $U_{j}, j=1,2$, follows a uniform distribution with the range $\left[-a_{j}, a_{j}\right], 0<a_{j}<0.5$, and $a_{j}$ can be adjusted so as to achieve the clearest graph possible.

Under certain circumstances, it may be more favorable to use larger units for the calendar time such as weeks or months, especially when the data are collected continuously over a long time span. Thus, using days as the units will result in a graph that is extremely lengthy in the vertical direction. As the units become coarser, fewer points will be produced from each disease instance. The $y$-coordinates of the points can be inferred from the induction period.
![img-2.jpeg](img-2.jpeg)

Figure 3. (a) MLTD graph and (b) ULTD graph

The MOTD graph can be developed in a similar manner. The MLTD/MOTD graph displays the temporal distribution of the disease at each location/occupation and also tells how the temporal distribution varies across different locations/occupations. For example, in Figure 3(a), the distribution of the particular disease has a cyclic fluctuation, that is, most instances cluster around certain months of a year. This pattern is consistent across different locations.

It should be pointed out that inspections on the temporal distribution of the disease in the MLTD/MOTD graph should be focused on the pattern or trend of each location/occupation and the contrast between locations/occupations, and any interpretations based on the absolute number of points should be avoided. For example, the number of points on a MLTD/MOTD graph does not reflect disease prevalence because more points could result from a long induction period.
3.5.2. Uni-location temporal distribution (ULTD) graph and uni-occupation temporal distribution graph After certain patterns have been identified from the MLTD/MOTD graph, it may be desirable to further examine the parameters of the patterns. Examples of these parameters include the slope of an increasing trend and the period of a cyclic fluctuation. To achieve this objective, a graph that plots the number of disease instances vs time for each individual location (or occupation) can be constructed. For example, Figure 3(b) displays such a graph for location 5 in Figure 3(a). It shows that the disease is prevalent in three months of a year, i.e. December, January, and February.

# 4. LEARNING THE RELATIONSHIPS BETWEEN A DISEASE AND POTENTIAL RISK FACTORS USING A BAYESIAN NETWORK 

A Bayesian network provides an explicit representation of the dependent and independent relationships among the variables in a problem. Depending on the interpretation, it can also represent causalities. Bayesian networks have been extensively used in genetics ${ }^{11}$, ecology ${ }^{12}$, social science ${ }^{13}$, and physical science ${ }^{14}$.

A Bayesian network is a directed acyclic graph (DAG), as shown in Figure 4. Each variable defines a node. An arc with an arrow points from $X_{j}$ to $X_{i}$ if $X_{j}$ is a parent (i.e. direct cause) of $X_{i}$. For each node $X_{i}$, there is a conditional probability distribution $P\left(X_{i} \mid\right.$ Parents $\left.\left(X_{i}\right)\right)$ quantifying the dependence between $X_{i}$ and its parents.

The process of developing a Bayesian network from observational data includes learning the structure (i.e. the DAG) and learning the parameters (i.e. the conditional probability distributions) given a structure. The existing algorithms for learning the structure can be divided into two categories: constraint-based approaches and score-based approaches. This paper focuses on the first category. Within this category, the algorithms can be further classified depending on whether the variables are discrete or continuous. Since the disease and most of the potential risk factors are measured at discrete scales, the learning algorithm for discrete variables is adopted in this research, which follows two basic principles ${ }^{15}$. Let $\mathbf{V}$ denote the set of variables, $\mathbf{V}=\left\{X_{1}, \ldots, X_{n}\right\}$. Any subset of $\mathbf{V}$ is denoted by $\mathbf{T} . X_{i} \bigsqcup X_{j} \mid \mathbf{T}$ means $X_{i}$ is independent of $X_{j}$ given $\mathbf{T}$.
![img-3.jpeg](img-3.jpeg)

Figure 4. A Bayesian network

$\neg A$ means that statement $A$ does not hold. The principles are as follows:
Principle I: Let $X_{i}, X_{j} \in \mathbf{V}$. Then $X_{i}$ and $X_{j}$ are adjacent if and only if for every $\mathbf{T} \subset \mathbf{V}$ such that $X_{i}, X_{j} \notin \mathbf{T}, \neg X_{i} \coprod X_{j} \mid \mathbf{T}$.

Principle II: If $X_{i}$ and $X_{k}$ are adjacent, $X_{j}$ and $X_{k}$ are adjacent, but $X_{i}$ and $X_{j}$ are not, then orient the arcs among such triplets as $X_{i} \rightarrow X_{k} \leftarrow X_{j}$ if and only if for every $\mathbf{T} \subset \mathbf{V}$ such that $X_{i}, X_{j} \notin \mathbf{T}$ and $X_{k} \in \mathbf{T}$, $\neg X_{i} \coprod X_{j} \mid \mathbf{T}$.

The first principle discovers all arc connections among variables and the second identifies arc directions. These two principles have been implemented in a computational algorithm called PC (Peter and Clark) ${ }^{16}$. Taking the BN structure in Figure 4 as an example, the PC algorithm is briefly introduced here.

- Start with a fully connected undirected graph in which each variable is linked with all other variables by undirected arcs.
- The undirected arc between one pair of variables is removed when conditional independence is found. For example, in Figure 4, the arc between $X_{3}$ and $X_{4}$ is removed because $X_{3}$ is independent of $X_{4}$ given their common cause $X_{2}$, and the arc between $X_{3}$ and $X_{1}$ is removed because $X_{3}$ is independent of $X_{1}$ given $X_{3}$ 's parent $X_{2}$. Other undirected arcs can be removed similarly.
- For the undirected arcs that cannot be removed in the previous step, the following rule is used to orient the arcs: each triple of variables $X_{i}-X_{j}-X_{k}$ is oriented as $X_{i} \rightarrow X_{j} \leftarrow X_{k}$, if $X_{i}$ and $X_{k}$ are found to be independent given a set of variables which do not contain $X_{j}$. Aside from this major rule in orientation, Meek ${ }^{17}$ introduced some supplementary rules such as orienting the remaining undirected arcs in a way that no cycles are created in the BN. In addition, some orientations may be achieved through knowledge or first principles.

PC can be improved by incorporating a partial or complete temporal order of the variables, which is readily available in most epidemiologic studies. For example, gender and age are naturally determined and thus they are always the earliest variables; moreover, the disease is always later than the risk factors. The basic idea for incorporating the temporal order into the learning is that if $X_{i}$ occurs after $X_{j}$, it cannot be a cause of $X_{j}$.

After the structure is obtained, the parameters can be learned based on the structure and the data. Learning parameters can be achieved by the EM algorithm in the cases of complete data sets and the data sets with missing data ${ }^{18}$.

# 5. INFERENCE BASED ON A BAYESIAN NETWORK 

### 5.1. Qualitative inference

After a Bayesian network is obtained, the DAG can be used to qualitatively interpret the association between the disease and a risk factor in the following ways.
(i) The association is causal, i.e. the risk factor is a cause of the disease if and only if there is directed path from the risk factor to the disease. A directed path from $X_{i}$ to $X_{j}$ is a sequence of variables beginning with $X_{i}$ and ending with $X_{j}$ such that for every pair of variables $X_{k}$ and $X_{l}$, adjacent in this sequence and occurring in that order, there is an arc pointing from $X_{k}$ to $X_{l}$. For example, age $\left(X_{1}\right)$ and smoking $\left(X_{2}\right)$ affect the development of lung cancer $\left(X_{4}\right)$ in Figure 4, while yellow fingers $\left(X_{3}\right)$ is not a cause of lung cancer $\left(X_{4}\right)$.
(ii) A variable is independent of its non-descendants given its parents. This statement is called the causal Markov condition ${ }^{16} . X_{i}$ is a descendant of $X_{j}$ if there is a directed path from $X_{j}$ to $X_{i}$. The causal Markov condition can be used to infer (conditional) independence relationships between variables. For example, in Figure 4, $X_{3}$ is independent of $X_{1}$ given $X_{2}$. An interpretation of this independence is that knowing whether a person smokes $\left(X_{2}\right)$ is sufficient to assess his/her risk of having yellow fingers $\left(X_{3}\right)$, regardless of his/her age $\left(X_{1}\right)$.

(iii) To determine whether confounding factors exist, a two-step procedure is followed ${ }^{1}$ : (a) Delete all arcs from the risk factor that points to any other nodes. (b) In the reduced graph, determine whether there is any unblocked backdoor path from the risk factor to the disease. If such a path exists, the association between the disease and the risk factor is due to the confounding effect of other variables. Otherwise, there is no confounding effect.

An unblocked backdoor path is defined as follows. A backdoor path from $X_{i}$ to $X_{j}$ is a path that begins by leaving $X_{i}$ along an arc whose arrow points into $X_{i}$, and then continues to $X_{j}$ regardless of the arc directions. A path is blocked if it contains at least one collider. A node $X_{i}$ on a path is called a collider if the arcs of the path entering and leaving $X_{i}$ both have arrows pointing into $X_{i}$.

For example, the association between yellow fingers $X_{3}$ and lung cancer $X_{4}$ is due to the confounding effect of smoking $X_{2}$ because $X_{3} \leftarrow X_{2} \rightarrow X_{4}$ is an unblocked backdoor path from $X_{3}$ to $X_{4} . X_{3} \leftarrow X_{2} \rightarrow X_{4}$ is an unblocked backdoor path because it does not contain a collider.

# 5.2. Quantitative inference 

Quantitative inference can be achieved based on the parameters of the Bayesian network. A joint distribution over all the variables can be computed as a function of the parameters, i.e. $P\left(X_{1}, \ldots, X_{n}\right)=$ $\prod_{i=1}^{n} P\left(X_{i} \mid\right.$ Parents $\left.\left(X_{i}\right)\right)^{19}$. Based on the joint distribution, any conditional probability $P(\mathbf{U} \mid \mathbf{W}),(\mathbf{U}, \mathbf{W} \subset \mathbf{V})$ can be computed. One conditional probability, $P(D=1 \mid \mathbf{R}=\mathbf{r})$, is of particular interest, where $D=1$ represents 'having the disease' and $\mathbf{R}$ is a set of risk factors, as it provides an assessment of a person's risk of developing the disease. In addition, computing $\hat{\mathbf{R}}=\arg \max _{\mathbf{r}} P(D=1 \mid \mathbf{R}=\mathbf{r})$ provides a way to identify the group of people who share some common characteristics and have the highest probability of developing the disease.

## 6. CASE STUDY

Two case studies are presented in this section, each corresponding to one particular disease of interest. The data used in the case studies are collected from a real-world data warehouse, which has synchronized occupational data and clinical data for more than 100000 data records. There are five potential risk factors. The variables in the case studies include disease $X_{4}\left(X_{4}=1\right.$ : case; $X_{4}=2$ : control), gender $X_{1}\left(X_{1}=1\right.$ : male; $X_{1}=2$ : female), age group $X_{2}\left(X_{2}=1: 18 \leq\right.$ age $\left.<25 ; X_{2}=2: 25 \leq\right.$ age $\left.<35 ; X_{2}=3: 35 \leq\right.$ age $\left.<45\right)$, occupation $X_{3}\left(X_{3}=1-8\right)$, location $X_{5}\left(X_{5}=1-6\right)$, and estimated induction time $X_{6}$. Note that the ages of patients are aggregated into three age groups (i.e. $X_{2}$ ) according to medical definitions. The estimated induction time $\left(X_{6}\right)$ is transformed depending on the objective of the study. For example, if the seasonal fluctuation of the disease prevalence is of interest, $X_{6}$ should be aggregated into 12 months or four quarters of a year; if the trend of the disease prevalence is of interest, the entire time axis can be divided into several intervals using discretization approaches such as equal bin size or equal frequency ${ }^{20}$. Visualization of the data, i.e. the MLTD/MOTD graph, gives a hint on how to transform $X_{6}$. For example, Figure 3(a) plots partial instances of the disease in the first case study, and it is obvious that the disease prevalence has seasonal fluctuation. Thus, $X_{6}$ is grouped into four quarters of a year. In the second case study, $X_{6}$ is divided into four intervals by the equal-frequency approach, that is, $X_{6}=1$ : [6/2001-1/2002], $X_{6}=2$ : [2/2002-7/2002], $X_{6}=3$ : [8/2002-3/2003], $X_{6}=4$ : [4/2003-8/2003].

A partial temporal order of the variables is specified as follows and further utilized by the PC algorithm to improve the learning. The variables belong to three temporal layers, with gender and age on the earliest layer, time, location, and occupation on the second earliest layer, and disease on the latest layer.

### 6.1. Case study 1

Figure 5 shows the structure and partial parameters $\left(P\left(X_{4} \mid X_{2}, X_{6}\right)\right)$ of the Bayesian network for this particular disease. The following conclusions can be reached.

(i) Age and quarter affect disease occurrences. Location and occupation are associated with the disease but do not affect disease occurrences, because the associations are due to the confounding effect of age. Gender is not associated with the disease.
(ii) $P\left(X_{4}=1 \mid X_{2}=x_{2}, X_{6}=x_{6}\right)$ is computed and shown in the table of Figure 5, which can be used to predict a person's risk of developing the disease given his/her age and the time (i.e. quarter) for performing his/her job. In addition, $\arg \max _{x_{2}, x_{6}} P\left(X_{4}=1 \mid X_{2}=x_{2}, X_{6}=x_{6}\right)=(1,1)$, which means people in the youngest age group (i.e. $X_{2}=1: 18 \leq$ age $<25$ ) in the first quarter of a year $\left(X_{6}=1\right)$ have the highest probability to develop this disease.

# 6.2. Case study 2 

The structure of the Bayesian network for this particular disease is shown in Figure 6. (The parameters are not shown here.) The following conclusions can be inferred:
![img-4.jpeg](img-4.jpeg)


Figure 5. The structure and partial parameters of the Bayesian network in case study 1
![img-5.jpeg](img-5.jpeg)

Figure 6. The structure of the Bayesian network in case study 2
![img-6.jpeg](img-6.jpeg)

Figure 7. Prediction of a person's risk of developing the disease given locations in case study 2

(i) Age, time, and location affect disease occurrences. Occupation is associated with the disease but does not affect disease occurrences, because the association is due to the confounding effect of age and location. Gender is not associated with the disease.
(ii) $P\left(X_{4}=1 \mid X_{5}=x_{5}\right)$ is computed and plotted in Figure 7, which can be used to predict a person's risk of developing the disease given the location of his/her job. In addition, $\arg \max _{x_{2}, x_{5}, x_{6}}\left(X_{4}=1 \mid X_{2}=x_{2}\right.$, $\left.X_{5}=x_{5}, X_{6}=x_{6} \mid\right)=(1,6,4)$, which means people in the youngest age group (i.e. $X_{2}=1: 18 \leq$ age $<25$ ) at location 6 (i.e. $X_{5}=6$ ) during the time interval 4/2003-8/2003 (i.e. $X_{6}=4$ ) have the highest probability of developing this disease.

# 7. CONCLUSION 

This paper presents a systematic approach to discovering the relationships between disease occurrences and patients' occupational histories based on real-world data. A Bayesian network is employed to learn the relationships. Data pre-processing is discussed as an important step in supporting the Bayesian network learning and ensuring meaningful results. The proposed approach addresses the integration of medical domain knowledge with the data preparation and analysis.

Based on the Bayesian networks, qualitative inferences can be made to distinguish among different types of associations (causal or non-causal) between the disease and risk factors. Quantitatively, given a person's demographic and occupational attributes, such as gender, age, and occupation, his/her risk of developing the disease can be predicted; in addition, it is possible to identify a group of people who share some common descriptive characteristics (e.g. a certain gender or/and occupation) and have the highest probability of developing the disease, which is important for disease control and prevention in epidemiology.

The proposed approach requires that sufficient data are collected for the variables, which is a challenging issue in some cases, such as when (i) the data set contains many missing values and (ii) the disease to be studied is not prevalent so that only a few cases are gathered. Further work will focus on studying how to derive meaningful dependent, independent, and causal relationships with missing values and small sample size.

## Acknowledgements

The authors would like to thank the researchers and analysts at Synchronous Knowledge Inc., specifically Wesley Watkins, Rick Reichard, Corey Ritchie, Stavros Kalamatianos, Olga Brazhnik, and Rick Reichard, for their invaluable support and contribution to this research.

# Authors' biographies 

Jing Li is an Assistant Professor in the Department of Industrial Engineering at Arizona State University. She received her PhD in industrial and operations engineering from the University of Michigan. Her primary research interests are applied statistics, data mining, and causal modeling and inference for process control, especially modeling and analyzing massive high-dimensional data sets in complex systems for improving the quality of products and processes. Her work has been applied to manufacturing and health-care problems.

Jianjun Shi is a Professor in the Department of Industrial and Operations Engineering at the University of Michigan. He received his PhD in mechanical engineering from the University of Michigan. His research interests focus on the fusion of advance statistics and domain knowledge to develop methodologies for modeling, monitoring, diagnosis, and control of complex manufacturing systems. His research has been funded by the National Science Foundation, National Institute of Standards and Technology, Advanced Technology Program, General Motors, Daimler-Chrysler, Ford, Lockheed-Martin, Honeywell, and various other industrial companies and funding agencies.

Devin Satz was the former President of Synchronous Knowledge Inc. (SKI), currently known as IMS Government Solutions, a wholly owned subsidiary of IMS Health Incorporated since May 2005. He was formerly a Major in the U.S. Air Force and the Administrator and Chief Information Officer for the Air Force Medical Operations Agency.