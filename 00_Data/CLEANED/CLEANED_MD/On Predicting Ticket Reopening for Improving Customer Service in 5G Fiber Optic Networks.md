# Article 

## On Predicting Ticket Reopening for Improving Customer Service in 5G Fiber Optic Networks

Lorenzo Ricciardi Celsi ${ }^{1,2, *}$ (D), Andrea Caliciotti ${ }^{2,3}$ (D), Matteo D'Onorio ${ }^{4}$ (D), Eugenio Scocchi ${ }^{5}$ (D), Nour Alhuda Sulieman ${ }^{6}$ and Massimo Villari ${ }^{6}$

check for updates

Citation: Ricciardi Celsi, L.; Caliciotti, A.; D'Onorio, M.; Scocchi, E.; Sulieman, N.A; Villari, M. On Predicting Ticket Reopening for Improving Customer Service in 5G Fiber Optic Networks. Future Internet 2021, 13, 259. https://doi.org/ 10.3390/f13100259

Academic Editor: Michael Mackay

Received: 17 September 2021
Accepted: 4 October 2021
Published: 9 October 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0) 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 ELIS Innovation Hub, Via Sandro Sandri 81, 00159 Roma, Italy
2 Department of Computer, Control, and Management Engineering Antonio Ruberti, Sapienza Università di Roma, Via Ariosto 25, 00185 Roma, Italy; andrea.caliciotti@enel.com
3 Enel Green Power S.p.A., Viale Regina Margherita 125, 00198 Roma, Italy
4 DIAEE, Sapienza Università di Roma, Corso Vittorio Emanuele II 244, 00186 Roma, Italy; matteo.donorio@uniroma1.it
5 ERG S.p.A., Via Bissolati 76, 00187 Roma, Italy; escocchi@erg.eu
6 Dipartimento di Scienze Matematiche e Informatiche, Scienze Fisiche e Scienze della Terra, Università di Messina, Piazza Pugliatti 1, 98122 Messina, Italy; nosulieman@unime.it (N.A.S.); mvillari@unime.it (M.V.)

- Correspondence: 1.ricciardicelsi@elis.org

Abstract: The paper proposes a data-driven strategy for predicting technical ticket reopening in the context of customer service for telecommunications companies providing 5G fiber optic networks. Namely, the main aim is to ensure that, between end user and service provider, the Service Level Agreement in terms of perceived Quality of Service is satisfied. The activity has been carried out within the framework of an extensive joint research initiative focused on Next Generation Networks between ELIS Innovation Hub and a major network service provider in Italy over the years 2018-2021. The authors make a detailed comparison among the performance of different approaches to classification-ranging from decision trees to Artificial Neural Networks and Support Vector Machines-and claim that a Bayesian network classifier is the most accurate at predicting whether a monitored ticket will be reopened or not. Moreover, the authors propose an approach to dimensionality reduction that proves to be successful at increasing the computational efficiency, namely by reducing the size of the relevant training dataset by two orders of magnitude with respect to the original dataset. Numerical simulations end the paper, proving that the proposed approach can be a very useful tool for service providers in order to identify the customers that are most at risk of reopening a ticket due to an unsolved technical issue.

Keywords: 5G fiber optic networks; data-driven service assurance; next generation networks; predictive analytics

## 1. Introduction

Effective customer care and data-driven service assurance have become a vital need for telecommunication companies, especially as regards the progression towards automating the management of technical tickets: in addition, this enables a thorough and objective evaluation of the performance of the service assurance functions, based on generated reports and prescribed Key Performance Indicators (KPIs), which implies increased productivity, improved quality of service and, in some cases, even personalized satisfaction of the end user.

More in detail, designing a successful data-driven service assurance system requires:

- in-house design and development in order to offer a solution that is at the same time cheap and adaptable to all service needs;
- tight integration with the customer portal in order to allow the access to all relevant online services with the same login credentials;

- support to all activities that are characteristic of an incident management process, such as opening, classifying, assigning, solving, closing and archiving an IT incident;
- enabling the exchange of files and comments regarding an IT incident, as this makes the served customers satisfied by allowing them to interact with IT agents in order to clarify the problem or understand the solution;
- provision of email notifications that allow for keeping all involved parties informed on any ticket update;
- automatic classification and ticket rerouting to the relevant IT agents, which is expected to significantly minimize resolution time of each ticket and consequently enhance user satisfaction;
- generation of reports to measure the KPIs that are chosen to evaluate the success of the customer care service.
For detailed references, the advantages and challenges of using data-driven service assurance in an organization have already been explored in the Information Technology Infrastructure Library (ITIL) framework of best practices for delivering IT services (see [1-8]). Moreover, the positive influence of ticketing services on the implementation of the incident management process is stressed in [1-10]. Indeed, being able to automate several key activities such as identification, prioritization, assignment, diagnosis and closure of technical tickets plays a relevant role in enhancing the said process. In addition, data-driven service assurance (see [4-6]) facilitates the measurement and improvement of several important KPIs for the IT business processes, such as the percentage of incidents detected and solved in the first attempt, the mean number of incidents that occurred per day and the average lifetime of an incident. In particular, in [8], it is clearly stated that automatic incident classification proves to be extremely effective at minimizing ticket resolution time. Providing an automated solution to the challenge of ticket classification is a relevant emerging task also according to [10].

Some related additional features that are in part beyond the scope of this work but testify the interest of the scientific and industrial community are the multimedia chat service architecture introduced in [11], as well as rule-based reasoning for fault diagnosis and visual dashboards for helping desk tickets monitoring, which is illustrated in [12,13]. In addition, a probabilistic framework for IT ticket annotation and search based on natural language processing is introduced in [14-17]. In [15], a predictive model based on Support Vector Machines (SVMs) and K-Nearest Neighbours (KNN) is discussed with the aim to automate incident categorization with the specific help of ticket description and other relevant ticket attributes. In a similar way, in [18], the dispatch of a ticket to the correct resolution group is successfully automated by means of a tool that combines SVMs and discriminative term-based classification techniques. Alternatively, Multinomial Naive Bayes (MNB) and Softmax Regression Neural Network (SNN) are used in [19] for text classification purposes aimed at categorizing user tickets. Finally, several methods to detect duplicate tickets/bugs are proposed in [20-22].

In particular, this paper, with respect to the emerging need for preventing customers from issuing a request for technical ticket reopening on customer service platforms of telecommunication companies, provides the following contributions:

- the identification of relevant correlations between the reopening of a technical customer service ticket, on the one hand, and Quality of Service (QoS) parameters of the 5G fiber optic networks, on the other hand, based on the actual use the customer is currently making of the fixed network itself;
- based on such correlations, the design of a data-driven model capable of predicting whether a customer will call the assistance service once again even though his/her technical ticket has already been closed.
Incidentally, reopened tickets are to be considered as those tickets that were formerly solved and have been reopened [23].

The proposed approach may prove particularly useful in the domain of 5G enabling technologies. Indeed, even with the advent of 5G, optical fiber is the most suitable means

for wireless backhaul networks. Indeed, even in networks where this is not the case, the wireless backhaul actually has to be connected into a fiber backhaul. For this reason, fiber technology is increasingly being preferred for the so-called fronthaul, especially when it comes to connecting the dense mesh of 5G small cells. There are several benefits, such as increased speeds matched with lower attenuation, significant immunity with respect to electromagnetic interference, relatively small size, and practically unlimited potential in terms of bandwidth. Hence, customer service in order to address any technical issue relative to the Quality of Service (QoS) perceived in 5G fiber optic networks has a critical role, especially with the advent of the emerging Fixed Wireless Access (FWA) paradigm [24].

The paper contribution lies in the fact that the effectiveness of the proposed approach is evaluated on the customer complaints that arise in conditions of intensive usage of the fixed network of a major Italian network operator. Indeed, according to IBM analyses in [25] and to [26], by automating up to $85 \%$ of the customer service process thanks to the usage of predictive tools such as the one presented in this work, an increase in efficiency up to $90 \%$ can be obtained, together with a reduction in the operating costs between $25 \%$ and $30 \%$.

Similar machine learning methods have already been used in order to solve resource allocation problems in order to improve the perceived QoS in [27-29]. In more detail, Pietrabissa et al. have already focused on distributed load balancing in Software Defined Networking relying on Lyapunov-based decision-making algorithms in [27], on optimal buffer allocation for guaranteeing QoS in multimedia Internet broadcasting for mobile networks in [28], and on predictor-based control design for improving Quality of Experience in delay-sensitive Future Internet frameworks in [29]. In contrast with the cited works, this paper specifically focuses on the prediction of the ticket reopening phenomena that characterize fixed networks and therefore also 5G fiber optic networks. To this aim, we exploited several machine learning approaches and compared the obtained performance results.

The paper is organized as follows: Section 2 introduces the so-called Analytical Base Table (ABT), namely the dataset to be given as an input to the predictive model for training and test purposes, as well as the data collection and preparation activity that has been carried out to assemble said ABT. Section 3 presents the performance achieved by different machine learning based classifiers, comparing the results obtained on the original dataset against those obtained on the reduced dataset. Section 4 discusses a further dimensionality reduction effort before introducing the Bayesian network classifier whose performance is the best in class. Concluding remarks end the paper.

# 2. Data Collection, Data Preparation and Analytical Base Table 

With the aim of effectively predicting ticket reopening relative to the QoS perceived in 5G fiber optic networks-namely, according to the emerging FWA paradigm-the methodological approach inspiring this work can be structured as follows.

- A first data collection and data preparation effort were made, by collecting, aggregating, cleaning and preparing the relevant data for the subsequent processing phase, resulting in a homogeneous ABT to be fed to the predictive analytics/classification engine that was subsequently designed and developed. This first activity was carried out in the framework of an extensive joint research initiative on Next Generation Networks between ELIS Innovation Hub and Vodafone over the years 2018-2021.
- Then, the KPI definition was necessary, that is, the identification of the relevant KPIs that allows for quantifying the benefits that are ultimately yielded by the adoption of the proposed predictive analytics engine. In this respect, we chose to evaluate the performance of the proposed predictive analytics engine in terms of accuracy, Gini coefficient, Youden index, and Area Under the ROC Curve (AUC).
- The design and training of the predictive analytics engine followed, together with the evaluation of the performance obtained on a suitable test dataset.

In more detail, the relevant input data are collected from two heterogeneous data sources,

1. the former related to the Virtual Unbundled Local Access (VULA) technology-VULA offers a means to any licensed network operator to effectively join the ultrabroadband network infrastructure of the backbone provider by virtually accessing the last mile only;
2. the latter related to the Sub-Loop Unbundling (SLU) technology-SLU is alternative to VULA, yet it joins the network infrastructure of the backbone provider only at the copper section, thus exhibiting lower performance than VULA.
The original dataset $X$ is therefore represented by an $m \times n \times t$ matrix aggregating the inputs from both VULA and SLU technologies. After being suitably cleaned, it reports $n=307$ network QoS parameters collected over a period of $t=30$ days of intensive usage for a group of $m=600,000$ users.

The $i$-th row of $X$ (for $i=1, \ldots, m$ ),

$$
x_{i}=\left(x_{u, v}^{i}\right)_{\substack{u=1, \ldots, n \\ v=1, \ldots, t}}
$$

associated with a user $i$ that the customer service has already closed a ticket for (since the aim of the paper is to predict ticket reopening), accounts for the values of the $n$ network QoS parameters perceived by user $i$ on day $v$. Among the $m$ users, in the considered period, $25 \%$ reopened a ticket due to a technical issue that is still unsolved even though a ticket in that respect had already been closed. In particular, data collection was carried out with a specific data matching criterion: namely, in the case of a reopened ticket, only the last data point-i.e., the last values of the $n$ features-that is, the temporally closest to ticket reopening for the considered user is collected and stored in the dataset $X$, whereas, for all other tickets-that have already been closed and have not been reopened yet-all data in the time interval between ticket closing and the last possible sampling instant are collected and stored in the dataset $X$.

In order to obtain a smaller dataset, with reduced dimensionality $(p<n=307)$ but with very similar information content, we first performed feature reduction on the original dataset $X$ by removing all features with very low variance, i.e., proving to be redundant when it comes to estimating the probability of ticket reopening.

Then, we carried out a linear correlation analysis among the features which, however, did not yield any relevant results; this is why we chose to resort to hierarchical clustering in order to shed light on any existing nonlinear correlations.

The result of hierarchical clustering, performed on the portion of $X$ accounting for the VULA and SLU inputs alternatively, is represented by the dendrograms shown in Figures 1 and 2, which represent the resulting hierarchies of clusters, by reporting:

- along the $x$-axis the logical distance between clusters according to the Manhattan metric;
- along the $y$-axis the hierarchical level of aggregation (denoted with 'Height' in Figures 1 and 2) measured in integer positive values.
In both dendrograms, important correlations emerged-which had not been as evident from linear correlation analysis at all-between ticket reopening (accounted for by the 'Repeated ticket' variable) and some network parameters. The most relevant evidence is related to the correlations of the Repeated ticket variable with the following:
- Percentage of 3G data availability for backup;
- Alarm tag;
- Number of connected hosts (WiFi);
- Total number of connected hosts.

![img-0.jpeg](img-0.jpeg)

Figure 1. Dendrogram showing the results of hierarchical clustering on the VULA portion of the original dataset $X$.

![img-1.jpeg](img-1.jpeg)

Figure 2. Dendrogram showing the result of hierarchical clustering on the SLU portion of the original dataset $X$.

As regards the last two, it is reasonable that the higher the number of connected devices, the higher the performance degradation.

A specific remark has to be made relative to the tight correlation of the Repeated ticket variable with the Alarm tag. Indeed, the Alarm tag parameter is a boolean variable which is valued 1 if the so-called customer-premises equipment parameter hits the alarm and 0 otherwise according to two alarm-triggering rules:

- if in almost 4 out of 8 measurements, the SAC parameter goes below threshold;
- if in 3 consecutive measurements, the SAC parameter goes below the threshold.

The SAC variable, which specifically accounts for attenuation-related QoS, can have values in the range from 1 to 6 (where 1 accounts for 'bad' and 6 for 'good') and is obtained by comparing other two parameters, namely signal-to-noise ratio (downstream) and attenuation (downstream), respectively.

The correlation between Repeated ticket and Alarm tag can be considered as primary since it is the tightest one. Therefore, in addition to the primary correlations highlighted by the dendrograms, starting from the tight correlation between Repeated ticket and Alarm tag, other secondary correlations also emerge between the Repeated ticket variable, on the one hand, and SAC, signal-to-noise ratio (downstream) and attenuation (downstream), on the other hand. In particular, by observing the relationship among these variables, we can notice the following high degrees of correlation:

- $\quad-47 \%$ correlation between Alarm tag and SAC for both VULA and SLU technologies;
- $\quad+65 \%$ correlation between SAC and signal-to-noise ratio for the SLU technology and $+68 \%$ correlation between the same variables for the VULA technology;
- $\quad-55 \%$ correlation between SAC and attenuation (downstream) for the SLU technology and $-45 \%$ between the same variables for the VULA technology.
It is also possible to evaluate the similarity degree between the two dendrograms by computing the so-called entanglement parameter-ranging from 0 , which accounts for no entanglement-to 1-which accounts for full entanglement. A low entanglement score implies a good alignment degree between the QoS performance of the two technologies with respect to the time period and set of users observed. In the considered case, the entanglement parameter is evaluated to be equal to 0.175 , thus allowing us to consider as ABT a reduced dataset $X^{\text {red }}$ extracted from the original one $X$. In particular, the Repeated ticket variable occupies very similar positions in both dendrograms. In light of this, it is reasonable to adopt the same predictive algorithm to predict ticket reopening for both VULA and SLU technologies.

As a result, the following lessons can be learned from the data preparation activity carried out in this section:

- no relevant linear correlations emerge between the Repeated ticket variable and QoS parameters;
- the variables exhibiting primary nonlinear correlations with the Repeated ticket variable are the percentage of 3G data availability for backup and the Alarm tag;
- the variables exhibiting secondary nonlinear correlations with the Repeated ticket variable are SAC, signal-to-noise ratio, and attenuation in downstream;
- the datasets related to the VULA and SLU technologies are very much correlated with each other due to the 0.175 entanglement coefficient computed between the two dendrograms in Figures 1 and 2.
Hence, the reduced dataset $X_{\text {red }}$ we are going to resort to hereinafter can be regarded as a $p \times n \times t$ matrix reporting the following $p=15$ network QoS parameters for the same group of $m$ users at time $t$ : (i) SAC, (ii) signal-to-noise ratio (downstream), (iii) attenuation (downstream), (iv) constant bitrate (downstream), (v) downstream maximum rate, (vi) Ethernet bytes (LAN data), (vii) percentage of Ethernet bytes (LAN), (viii) percentage of WiFi primary data Ethernet bytes (LAN), (ix) attenuation (upstream), (x) current bitrate (upstream), (xi) upstream maximum rate, (xii) power (upstream), (xiii) UPBO (upstream power back-off) loop length (dB), (xiv) ticket close code, and (xv) repeated ticket.

The ticket close code has not been mentioned so far but was already also present in the original dataset $X$ : it testifies that the network operator has acknowledged the causes that are attributable to the variations in the QoS parameters for which the user is complaining. The ticket close code variable may take one of the following values: (a) activity on the OCA protocol, (b) existence of a known problem that is pending for resolution, (c) line/device problem needing for device reboot, (d) line/device problem

needing for device reset, (e) unexploited link/GNP (Geographic Number Portability), (f) LNI-minimum bitrate, (g) maximum obtainable performance, (h) no trouble found, (i) OLO2OLO problem-OLO2OLO is the Italian platform allowing the migration of access lines between different network operators insisting on the same network infrastructure-, (j) performance degradation resulting from monitoring, (k) macroproblem due to the network infrastructure, (l) known network outage, (m) network outage detected as a result of monitoring, (n) access degradation of the network infrastructure resulting from monitoring, (o) access network degradation relative to the backbone provider, (p) access network degradation relative to the network operator, and (q) wrong assignment of the network service to a user. For the sake of completeness, in Table 1, we show the relative frequency of each ticket close code in the considered dataset.

Table 1. Relative frequencies of the values exhibited by the ticket close code variable.


We now present our predictive model. In more detail, we are going to address the following classification problem: is a user at risk of reopening a ticket that was previously closed even though the related technical issue (in terms of perceived QoS) was still not solved?

# 3. Classification for Predicting Ticket Reopening 

In this section, we show the performance achieved by different machine learning based classifiers trained both on the original dataset $X$ and on the reduced dataset $X_{\text {red }}$ in order to predict if a monitored ticket will be reopened or not. This allows us to evaluate the effectiveness of the dimensionality reduction activity discussed in the previous section.

### 3.1. Different Approaches to Classification

Machine learning is a branch of artificial intelligence based on the idea that systems can learn from data and make reasonable decisions with minimal human intervention. In contrast with many statistical modeling approaches, which generally value inference over prediction, the focus of machine learning is predictive accuracy (see [30]). High predictive accuracy is usually achieved by training complex predictive models, often involving advanced numerical optimization routines, on a very large number of training examples.

According to the survey provided in [31], in this paper, the following supervised classification techniques are considered: decision tree, random forest, boosting, logistic regression, Artificial Neural Network (ANN) and SVM.

The chosen architecture for the decision tree based classifier is inspired by [32]. The random forest based approach to classification follows [33]. The setup for boosting resembles [34], whereas the logistic regression one is inspired by [35].

Instead, in the case of the ANN, we consider a two-layer fully connected network. For the hidden layer, we resort to ReLU nonlinearity, whereas, for the output layer, we have a Softmax loss function. The size of the neural network for the input and output layers is dependent on the input dataset ( $X$ and $X_{\text {red }}$, alternatively) and classes respectively, while the hidden layer is arbitrarily set.

Finally, the SVM classifier follows the classical approach from [36].

# 3.2. Numerical Simulations and Results 

In this subsection, we compare the different classification approaches (described in Section 3.1) in order to predict ticket reopening via supervised learning. According to Section 2, we consider both datasets: the first one $(X)$ in the original form and the second one in the reduced form $X_{\text {red }}$ (through feature selection analysis).

Given a month (i.e., 30 days) of data collected according to the format discussed in Section 2, we reordered the dataset by picking six groups of four days as training sets $(k \in\{1,6,11,16,21,26\})$, denoting them, with a slight abuse of notation, with $X_{\text {training }}[k]$ in the case of the original dataset and with $X_{\text {training }}^{\text {red }}[k]$ in the case of the reduced dataset, that is,

$$
X_{\text {training }}[k]:=\left[\begin{array}{c}
x_{u,(v=k)}^{i} \\
x_{u,(v=k+1)}^{i} \\
x_{u,(v=k+2)}^{i} \\
x_{u,(v=k+3)}^{i}
\end{array}\right], \quad \forall u, \quad k \in\{1,6,11,16,21,26\}, \quad i=1, \ldots, m
$$

and analogously for $X_{\text {training }}^{\text {red }}[k]$.
We then considered the dataset portion relative to each of the remaining six days of the considered month $(q=k+4)$ as a one-day subset of the ABT providing a suitable test set, denoted with

$$
X_{\text {test }}[q]:=\left[x_{u,(v=q)}^{i}\right], \quad \forall u, \quad k \in\{1,6,11,16,21,26\}, \quad i=1, \ldots, m
$$

in the case of the original dataset, and with $X_{\text {test }}^{\text {red }}[q]$ defined analogously, in the case of the reduced dataset.

In order to ensure the statistical robustness of the learned models, we proceeded in the following way. We first trained each classification algorithm on $X_{\text {training }}[k]$ and $X_{\text {training }}^{\text {red }}[k]$ alternatively, in order to obtain the learned models for each iteration $k$ (training phase). Then, we tested each model learned at iteration $k$ on the one-day test set $X_{\text {test }}[q]$ in the case of the original dataset, and on the one-day test set $X_{\text {test }}^{\text {red }}[q]$ in the case of the reduced dataset (test phase).

Eventually, we measured the KPIs listed below for each couple $(k, q)$ of training and test sets and we reported in Tables 2 and 3 the average KPI values over all $(k, q)$ couples.

For both data preparation and supervised leaning algorithms, all codes are written in R. All the simulation runs were performed on a dual-core Intel Core i7-7500U 2.70GHz (up to 3.50 GHz ) processor equipped with 16 GB RAM and running Ubuntu 18.04.

Numerical results are provided in terms of Accuracy, Gini coefficient, Youden index and $A U C$.

- Accuracy [37]: the accuracy measure tells how well a machine learner, which learned the hypothesis $h$ as the approximation of the target classification function $V$, performs in terms of classifying a novel unseen example correctly. The true error of hypothesis $h$ is the probability that it will misclassify a randomly drawn example $x$, that is,

$$
\operatorname{error}(h)=\operatorname{Pr}[V(x) \neq h(x)]
$$

With this in mind, accuracy has the following definition:

$$
\text { Accuracy }=\frac{\text { number of correct predictions }}{\text { total number of predictions }} .
$$

For binary classification, as in the considered case, accuracy can also be calculated in terms of positives and negatives as follows:

$$
\text { Accuracy }=\frac{T P+T N}{T P+T N+F P+F N}
$$

where $T P, T N, F P$ and $F N$ are the number of true positives, true negatives, false positives and false negatives, respectively.

- Gini coefficient [37]: It provides a measure of the degree or probability of the target variable being wrongly classified. It has values between -1 and 1 . The closer it is to 1 the better.
- Youden index [37]: it is a goodness-of-fit index that represents the maximum separation between the model Receiver Operating Characteristic (ROC) curve and the baseline ROC curve.
- AUC [37]: an ROC curve shows the probability distribution just for the events, the positive class. It compares the events predicted correctly (true positives) against the events predicted incorrectly (false positives). The higher the sensitivity (true positive rate close to 1) and the lower the false negative rate (specificity close to 1), the better the model. The AUC gives us the area under the ROC curve: the greater the area, the higher the index.

Table 2. Numerical results for the dataset $X$.


Table 3. Numerical results for the dataset $X_{\text {red }}$.


The best one in the first case is the random forest algorithm. In the second case, the most accurate is the logistic regression algorithm, but the best performing one in general remains the random forest algorithm.

# 4. A Bayesian Network Classifier Trained on a Further Reduced Dataset 

We now propose another data-driven classification model, namely based on a Bayesian network, aimed at improving the performance already obtained on the dataset $X_{\text {red }}$ by means of a further dimensionality reduction, namely resorting to the further reduced dataset $X_{\text {red }}^{\prime}$.

4.1. Bayesian Network Classifier

Based on the reduced dataset, we trained a classifier resorting to a Bayesian network.

A Bayesian network is a probabilistic graphical model that, by representing a set of variables and their conditional dependencies via a directed acyclic graph **G**, allows for predicting the likelihood that one of several possible known causes is the contributing factor behind the occurrence of a specific event. In the considered case, the aim is that of predicting if a combination of network QoS parameters belongs to the discrete class variable Repeated ticket.

In more detail, we learned a Naive Bayes network structure **G** as in Figure 3, revolving around the following input variables, which therefore compose the new reduced dataset **X**′_{*r**e**d*} as a **p** × *n* matrix, with **p** = 7:

- Repeated ticket;
- Ticket close code;
- Signal-to-noise ratio (downstream);
- SAC;
- Constant bitrate (downstream);
- Power (upstream);
- Attenuation (upstream).

We set the Upstream Attenuation node as root node and the SAC and Repeated ticket nodes as leaf nodes.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** Naive Bayes network structure **G** behind the chosen Bayesian network classifier.

The variables' alarm tag and percentage of 3G data availability for backup have been preliminarily excluded from the ABT because, from a statistical viewpoint, they were not suitable for the algorithm procedure that is behind training a Bayesian network classifier.

In addition, before training the classifier, we chose to perform discretization-referred to as the process of grouping values into intervals in order to limit the number of possible states-on the input data according to the type and distribution of each variable, in order to optimize the performance in the creation of the Bayesian network graph. The following two methods were applied onto the continuous variables of the ABT: namely, quantile (subdivision by frequency) and uniform (subdivision into a suitable number of groups of the same size) discretization.

Quantile discretization was performed onto the constant bitrate (downstream), signal-to-noise ratio (downstream), attenuation (upstream) and power (upstream) variables, by grouping the values of each variable into four same size bins, split based on percentiles.

Uniform discretization, instead, was performed onto the ticket close code and SAC, grouping the values of each variable into four same-width discrete bins depending on the span of possible values for each considered variable.

The Repeated ticket variable was discretized into two disjoint bins, of which $15 \%$ are repeated tickets and the rest are non-repeated.

Table 4 shows the characteristics of the Bayesian network in detail. The value of the Pearson correlation coefficient (denoted with 'Strength' in the table) indicates the existing degree of correlation between the variables considered: the closer this value is to 1 , the greater the correlation between the variables. On the other hand, the 'Direction' column indicates the degree of reliability of the links that introduce a hierarchy between the variables: in this case, too, the closer the value is to 1 , the more the direction of the link accounting for the existing relationship between the considered variables is reliable.

Table 4. Pearson correlation coefficient between the variables in $X_{\text {red }}^{\prime}$ and degree of reliability of the links characterizing the learned Naive Bayes network structure $\mathcal{G}$.


It is clear from Figure 3 and Table 4 that the correlation coefficient with the variables closest to the Repeated ticket variable is always greater than 0.93 , which implies that the proposed tree structure can be considered as highly reliable for our classification purpose.

The combinations of conditional probabilities calculated by the Bayesian network as a result of discretization generate a number of scenarios to which it is possible to associate the probability of occurrence of the event of ticket reopening. For the considered reduced dataset $X_{\text {red }}^{\prime}$, more than one thousand different simulation scenarios were generated. Namely, the 13 intervals shown in Table 5 are combined with the 17 possible causes identified within the ticket close code variable. Constant bitrate in downstream is measured in bits per second. Attenuation in upstream is measured in dB and power in upstream is measured in dBmV .

Table 5. Relevant distributions of the variables of $X_{\text {red }}^{\prime}$ into suitable bins as a result of discretization.


Remark 1. The number of relevant scenarios may vary depending on the discretization type and the number of tickets associated with the different combinations. This has proven to be the best choice, given the characteristics of the considered dataset.

# 4.2. Model Performance Evaluation and Discussion on the Results 

For the purpose of evaluating the model performance, we adopted the same approach as discussed at the beginning of Section 3.2. However, in order to further test the robustness of the Bayesian network classifier, we also carried out the experiment of creating 1000 random pairs of training/test sets according to the $70 / 30$ rule, i.e., $70 \%$ of the $X_{\text {red }}^{\prime}$ dataset was used for training purposes and the rest for testing. The measured KPIs were very similar, thus testifying the effectiveness of the Bayesian network classifier as well as its robustness. The average values of the KPIs measured throughout these tests are reported below in Table 6 in order to compare them with the results of the different classifiers trained in Section 3.

The validation process was completed by comparing the accuracy measure achieved by the Bayesian network classifier against the performance of the other classifiers.

From Table 6, it is clear that the Bayesian Network classifier trained on $X_{\text {red }}^{\prime}$ outperforms the classifiers introduced in Section 3.

Table 6. Numerical results for the second dataset.


Among the trained classifiers, according to the accuracy and AUC measures, the Bayesian Network classifier proves to be the most effective at minimizing the error (8).

From the results obtained, we also infer the combinations of features in $X_{\text {red }}^{\prime}$ that are most probably the reason for ticket reopening: namely, they are the events listed below:
(1) Ticket close code (d) AND Constant bitrate (downstream) in bin 2 AND Power (upstream) in bin 4 AND Attenuation (upstream) in bin 3;
(2) Ticket close code (k) AND Constant bitrate (downstream) in bin 1 AND Power (upstream) in bin 1 AND Attenuation (downstream) in bin 3;
(3) Ticket close code (i) AND Constant bitrate (downstream) in bin 4 AND Power (upstream) in bin 3 AND Attenuation (upstream) in bin 3;
(4) Ticket close code (i) AND Constant bitrate (downstream) in bin 3 AND Power (upstream) in bin 3 AND Attenuation (upstream) in bin 4;
(5) Ticket close code (i) AND Constant bitrate (downstream) in bin 2 AND Power (upstream) in bin 2 AND Attenuation (upstream) in bin 3;
(6) Ticket close code (i) AND Constant bitrate (downstream) in bin 3 AND Power (upstream) in bin 2 AND Attenuation (upstream) in bin 1;
(7) Ticket close code (p) AND Constant bitrate (downstream) in bin 2 AND Power (upstream) in bin 3 AND Attenuation (upstream) in bin 3;

(8) Ticket close code (p) AND Constant bitrate (downstream) in bin 3 and Power (upstream) in bin 4 AND Attenuation (upstream) in bin 4;
(9) Ticket close code (p) AND Constant bitrate (downstream) in bin 4 AND Power (upstream) in bin 1 AND Attenuation (upstream) in bin 2.
Table 7 reports them with the corresponding number of occurrences of such combinations of QoS parameters.

Table 7. Combinations of features in $X_{\text {red }}^{\prime}$ that are most probably the reason for ticket reopening according to the predictions of the Bayesian Network classifier.


In general, as can be seen from Table 7, the trained classifier provides the customer service of a network operator with a reliable tool for effectively monitoring customer tickets that, despite being already closed, are at risk of being reopened due to unsolved technical issues related to the perceived QoS.

The complexity of the Bayesian Network classifier, namely the most successful one, is linear in the number of training examples and in the number of features characterizing each training example. Instead, almost all other methods exhibit increased runtime complexity: more precisely, the Decision Tree, Random Forest and Gradient Boosting approaches are such that their complexity is logarithmic in the number of training examples, whereas the complexity of the SVM approach is quadratic in the number of training examples. Only the ANN and the Logistic Regression techniques have comparable computational complexity with respect to the Bayesian Network classifier, but with lower predictive performance (as shown in Table 6).

# 5. Conclusions 

The paper proposes a data-driven approach based on machine learning for predicting technical ticket reopening in customer service platforms of telecommunications companies providing 5G fiber optic networks, namely with respect to ensuring that, between end user and service provider, the Service Level Agreement in terms of perceived Quality of Service is satisfied.

The activity was carried out within the framework of an extensive joint research initiative on Next Generation Networks between ELIS Innovation Hub and a major network service provider in Italy over the years 2018-2021.

The authors compare the performance of different approaches to classificationranging from decision trees to Artificial Neural Networks and Support Vector Machinesand establish that a Bayesian network classifier is the most accurate at predicting whether a monitored ticket will be reopened or not.

In addition, the authors propose a suitable dimensionality reduction strategy that proves to be successful at increasing the computational efficiency by reducing the size of the relevant training dataset by two orders of magnitude with respect to the original dataset.

Numerical simulations show the effectiveness of the proposed approach, proving it can be a very useful tool for service providers in order to identify the customers that are most at risk of reopening a ticket due to an unsolved technical issue.

As future work, the authors look forward to testing the proposed method on Quality of Service datasets coming from additional sources and/or related to other 5G networks, as well as to testing the same method on even larger datasets in orders to further assess its scalability properties.

Author Contributions: Investigation, M.V.; Methodology, L.R.C., A.C., M.D., E.S. and M.V.; Software, A.C., M.D. and E.S.; Writing—original draft, L.R.C. and N.A.S.; Writing—review \& editing, L.R.C. and N.A.S. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by ELIS Innovation Hub within a collaboration with Vodafone, grant number Joint Research Project within the framework of the Mindset Revolution Semester.
Data Availability Statement: Not Applicable, the study does not report any data.
Conflicts of Interest: The work presented in this paper was carried out while Caliciotti and Scocchi were with ELIS Innovation Hub and does not reflect the results of any activity carried out at Enel Green Power S.p.A. and ERG S.p.A., to which these two authors are currently affiliated, respectively.
