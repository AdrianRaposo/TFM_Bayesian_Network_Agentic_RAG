# A Bayesian belief network-based analytics methodology for early-stage risk detection of novel diseases 

Kazim Topuz ${ }^{1}$ (D) $\cdot$ Behrooz Davazdahemami ${ }^{2}$ (D) $\cdot$ Dursun Delen ${ }^{3,4}$ (D)<br>Accepted: 1 May 2023 / Published online: 17 May 2023<br>(c) The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2023


#### Abstract

During a pandemic, medical specialists have substantial challenges in discovering and validating new disease risk factors and designing effective treatment strategies. Traditionally, this approach entails several clinical studies and trials that might last several years, during which strict preventive measures are enforced to manage the outbreak and limit the death toll. Advanced data analytics technologies, on the other hand, could be utilized to monitor and expedite the procedure. This research integrates evolutionary search algorithms, Bayesian belief networks, and innovative interpretation techniques to provide a comprehensive exploratory-descriptive-explanatory machine learning methodology to assist clinical decision-makers in responding promptly to pandemic scenarios. The proposed approach is illustrated through a case study in which the survival of COVID-19 patients is determined using inpatient and emergency department (ED) encounters from a real-world electronic health record database. Following an exploratory phase in which genetic algorithms are used to identify a set of the most critical chronic risk factors and their validation using descriptive tools based on the concept of Bayesian Belief Nets, the framework develops and trains a probabilistic graphical model to explain and predict patient survival (with an AUC of 0.92). Finally, a publicly available online, probabilistic decision support inference simulator was constructed to facilitate what-if analysis and aid general users and healthcare professionals in interpreting model findings. The results widely corroborate intensive and expensive clinical trial research assessments.


[^0]
[^0]:    园 Behrooz Davazdahemami
    davazdab@uww.edu
    Kazim Topuz
    kat0141@utulsa.edu
    Dursun Delen
    dursun.delen@okstate.edu
    1 Collins College of Business, School of Finance and Operations Management, The University of Tulsa, Tulsa, USA
    2 Department of IT and Supply Chain Management, University of Wisconsin-Whitewater, 809 W. Starin Rd., Hyland Hall 1222, Whitewater, USA
    3 Center for Health Systems Innovation, Spears School of Business, Oklahoma State University, Stillwater, USA
    4 Faculty of Engineering and Natural Sciences, Istinye University, Istanbul, Turkey

Keywords Pandemic $\cdot$ Risk assessment $\cdot$ Bayesian network $\cdot$ Explainable machine learning $\cdot$ Comorbidity

# 1 Introduction 

Timely decision-making for efficient allocation of scarce healthcare resources during national or worldwide public health emergencies is critical (Lee et al., 2009). Notably, in the case of novel contagious diseases with mysterious aspects, gaining knowledge of potential demographic and chronic risk factors on time can significantly help the medical experts in designing and optimizing treatment and prevention protocols and bringing the outbreak under control (Davazdahemami et al., 2022; Li et al., 2020).

In the case of such novel diseases, while traditionally experimental clinical studies can identify the major risk factors over time, they are deemed inefficient in several aspects. First, most of these studies utilize small samples of patients and typically are limited to testing the validity of one or a few potential risk factors. Second, they are usually focused on specific patient groups (e.g., diabetic patients, pregnant women, senior adults, etc.) and this puts the generalizability of their finding under question. Third, such studies are more focused on descriptive aspects and less concerned with comparing the identified risk factors in terms of their relative importance. Fourth, given that their focus is typically limited to a few risk factors, the risk associated with interaction of multiple comorbid conditions is neglected in their analyses. Lastly, the settings of these past studies are exclusive to a certain disease; they do not lead to developing a comprehensive generalizable framework applicable in future health emergencies.

The current study attempts to address these shortcomings by presenting a universally applicable Exploratory-Descriptive-Explanatory (EDE) structure that can be utilized as a decision-making tool for identifying important chronic risk factors early in the course of the novel, complicated infectious diseases. The exploratory aspect of our framework employs a combination of the evolutionary heuristic search methods with predictive analytics techniques to perform a feature selection and identify an optimal subset of the most relevant chronic and demographic risk factors associated with a given novel disease. In the descriptive phase, we use the network and visual analytics tools to understand the patterns and relationships among the risk factors identified in the exploratory phase. In the explanatory phase of the framework, the selected features are used to develop a Bayesian Belief Network through which we assess the probability of survival for individual patients given their specific combination of demographics and chronic conditions. This is particularly crucial given the limitation of resources at the time of outbreaks and the importance of accurately identifying patients at high risk to allocate healthcare resources optimally. Additionally, this article introduces a decision support simulator, a web-based Bayesian inference tool, to assist decision-makers in exploring multidimensional interactions. The decision-support tool analyzes the effect of a specific combination of conditions based on patient-specific values/updates and is publicly accessible.

We use the COVID-19 pandemic as a case study to validate our proposed framework. We use a dataset of early COVID-19 cases in the United States. Despite using COVID-19 data for showcasing the proposed framework, we argue that it is a disease-agnostic framework and is meant to work for any similar health crisis.

The remainder of this article is organized as follows. In Sect. 2, the related studies from the literature are reviewed. Next, we describe the proposed framework and the specific data used

to validate it. Following that, the feature selection and the Bayesian analyses are demonstrated. Finally, we discuss our findings and limitations, as well as future research directions.

# 2 Background 

With the onset of the COVID-19 pandemic in early 2020, many research efforts began worldwide to understand the mechanism and risk factors of the novel mysterious virus and consequently to design and adjust prevention and treatment protocols. While several key risk factors of the disease were identified and reported through these studies, they generally suffer from one (or both) of the two main limitations as follows.

First, they primarily are focused on a single or a few risk factors. They do not account for the possible complications caused by the interaction of multiple health factors on the severity of the outcome. Such studies typically rely on standard statistical tests to find out a statistically significant difference between two different samples in terms of a given potential risk factor. For example, Peckham et al. (2020), using a sample of more than 3 million global COVID-19 cases, showed that the odds of intensive care needs and death in male patients are significantly higher than in females. Similar results were reported by Galbadage et al. (2020) in another meta-analysis study on the effect of gender on the severity of the disease. Also, using a similar approach, other studies identified several other risk factors for the disease, including age, obesity, hypertension, cardiovascular diseases, diabetes, pulmonary diseases, and cancer (Du et al., 2021; Földi et al., 2020; Hussain et al., 2020; Javanmardi et al., 2020; Mantovani et al., 2020; Parohan et al., 2020; Romero Starke et al., 2020). The risk factors investigated in these studies were all considered individually and in isolation from other possible confounders (e.g., demographics, comorbidities, medications, or public health factors).

Second, even those studies that account for interrelationships among various factors are mostly focused on employing such patterns for improving the predictability of the outcome (e.g., patients' survivability, hospital length of stay, intensive care need, among others) and are less concerned with the explanation of those relationships and their business and/or medical implications. For instance, Bekker et al. (2022) propose a new approach based on linear programming for predicting COVID-19 occupancy using only aggregated data as opposed to individual health records. In another predictive analytics study, Nikolopoulos et al. (2021) provide tools for forecasting the country-level COVID-19 growth rates to plan supply chain demand for related products and services. Similarly, Eryarsoy et al. (2020) propose a novel approach (based on the well-established marketing diffusion models) for estimating the number of cases, hospitalizations, ICU admissions, and fatalities with minimal data requirements for application in the public health policy development at the early stages of pandemics where not enough data is yet accumulated to estimate the common epidemiology indices. Several other studies have employed various machine learning, time series, and simulation techniques to predict hospitalization demands (Alakus \& Turkoglu, 2020; Deschepper et al., 2021; Huang et al., 2020), mortality (Cui et al., 2021; Davazdahemami et al., 2022; Taylor \& Taylor, 2021), and vaccination supply chain requirements (Currie et al., 2020; Nagurney, 2021; Sinha et al., 2021).

However, the mentioned shortcomings are not limited to the recent pandemic studies only. A review of research conducted on the three other major pandemics and epidemics in the past decade, namely the H1N1 Swine Flu pandemic in 2009, the Ebola virus disease epidemic in 2014, and the Zika virus disease epidemic in 2015, confirms that they were also mainly

focused on either investigating single risk factors or interrelation of risk factors with emphasis on improving the predictability of outcomes. In a study of the risk factors of the H1N1 flu pandemic, O'Riordan et al. (2010) have compared the charts of 58 children with H1N1 with those of children with seasonal influenza A using standard statistical tests and showed that factors such as age and underlying conditions were significantly different among the two groups. Similarly, using a case-control approach Ribeiro et al. (2015) showed that age, obesity, and immunosuppression increase the odds of death due to H1N1 flu. Several other studies have employed similar bivariate statistical approaches to look into the risk factors of that disease (Baumeister et al., 2003; Campbell et al., 2010; Gilca et al., 2011; Hanslik et al., 2010; Lenzi et al., 2012) as well as Ebola virus disease (Hartley et al., 2017; Wing et al., 2018; Wirth et al., 2016; Xu et al., 2016) and Zika virus disease (de Araújo et al., 2018; Goodman et al., 2016; Smith \& Mackenzie, 2016; Ventura et al., 2016).

In the predictive analytics realm also, several studies sought to perform early detection of these diseases (Akhtar et al., 2019; Kakulapati et al., 2021; Mahalakshmi \& Suseendran, 2019; Thakkar et al., 2010), predict mortality or severity (Colubri et al., 2019; Pandey \& Subbiah, 2018), and modeling the spread of diseases (Jiang et al., 2018; Zhang et al., 2015). The number of data-driven machine learning studies for the past pandemics/epidemics are considerably smaller than those of the COVID-19, most probably due to their relatively limited outbreak and advances in the data collection and analysis infrastructures and methods in methods recent years. Nevertheless, what seems to be missing in the literature on data-driven studies of pandemics is a comprehensive methodology for early detection of the chronic risk factors considering the confounding roles of comorbid conditions in estimating the severity and mortality of novel viral diseases. Bayesian networks (BNs) are advantageous since they provide researchers with a causally correct method for exploring the domain with input from subject matter experts and disengaging statistical correlation and causal effects (Pearl, 2009, 2014). BNs have gained popularity among machine learning models because of their use of graph and probability theory principles, enabling non-technical subject matter experts to analyze big data. (Topuz et al., 2021b).

The present study contributes to the extant literature by proposing a holistic framework for both identifications of chronic comorbidity risk factors (increasing the odds of mortality) through an evolutionary search process as well as an explanation of the relative risk of those factors either individually or in combination with each other by creating BNs and presenting it on a publicly available web simulator. BNs actively use graph and probability theory concepts, making data science intuitive for non-technical subject matter experts. To be realistic and applicable, our framework is particularly designed with two key assumptions in mind, namely:1) novelty of the disease and no prior knowledge about its risk factors; and 2) limitation of data availability in the early stages of an epidemic/pandemic and the need for quick and accurate decision support tools for planning the limited resources and adjust treatment protocols.

# 3 Methods and materials 

### 3.1 Data

We used early US pandemic data from the Cerner HealthFacts data warehouse, one of the most comprehensive EHR platforms in the United States with clinical records from more than 63 million unique patients collected since 2000. The data warehouse structure involves

Table 1 Summary of the predictive features


a fact table containing general visit (a.k.a. encounter) and patients' features with several dimensions containing details on diagnoses, medications, lab test, medical facilities, and operations, just to name a few. The COVID-19 related visits (both inpatient and emergency) between December 2019 and June 2020 were extracted. We eliminated visits from patients who were not adults (above 18). The patients in the sample had all been diagnosed with COVID-19 using one or more diagnostic lab tests.

Next, we performed a one-hot-encoding of the patients' historical chronic conditions (the corresponding ICD-10 identifier for each condition was used for consistency). Chronic conditions were identified using the Chronic Condition Indicator (CCI) list for ICD-10CM provided by the Agency for Healthcare Research and Quality. ${ }^{1}$ Acute conditions were excluded from the scope of this study since they could be resulted from the COVID-19 (i.e., as a consequence or symptom) as opposed to being risk factors. This resulted in 1047 binary features, each indicating the existence of a chronic condition in the health records of a patient. Additionally, the final dataset includes patients' demographics and encounter-specific data (i.e., patient age at the encounter, admission type, and payer type) to be examined for their prospective risk level. We also included two numeric features showing the total number of diagnoses at the admission and the total number of unique historical diagnoses in each patient's records as two proxies of their general health condition. Table 1 shows a summary of the features extracted from the patients' records by category.

Finally, a binary target variable was derived to show if a given patient survived COVID19 (i.e., survived $=0$; deceased $=1$ ). Our data revealed a 9.6 percent mortality rate ( 982 out of 10,189 ) for COVID-19, which is significantly greater than the average rate (2-3 percent) reported by the Johns Hopkins Coronavirus Resource Center (2021). We believe that although this discrepancy may be partially explained by the absence of asymptomatic patients (or those who self-quarantined at home) in our data, it may also be explained by the disease's novelty and insufficient resources to control the epidemic during the early phases of the pandemic. Table 2 summarizes the demographics of the patients. Also, in Fig. 1, we

[^0]
[^0]:    ${ }^{1}$ https://www.hcup-us.ahrq.gov/toolssoftware/chronic_icd10/chronic_icd10.jsp.

Table 2 Summary of the patients' demographics


![img-0.jpeg](img-0.jpeg)

Fig. 1 Proportions of comorbidities by patient outcome
have demonstrated the proportion contrasts of different conditions (by category) among the two classes of patients.

# 3.2 Methodology 

Exploratory, descriptive, and explanatory research are incorporated into the proposed system's conceptual design, using a genetic algorithm and a Bayesian belief network. Seven steps (three phases) of development are followed in order to create an efficient framework for developing comorbidity analysis, which includes (1) combining datasets from multiple data sources, (2) dealing with data issues like missing values and multicollinearity, (3) feature engineering with genetic algorithm, (4) understanding patterns, and inter-relationships and graphical representation of data, (5) developing a probabilistic model to estimate survival joint probability, (6) designing a publicly available decision inference tool to perform whatif scenarios, (7) interpreting explanatory results and updating exploratory phase knowledge. Figure 2 illustrates the proposed methodology graphically. The following sections detail each of these phases.

![img-1.jpeg](img-1.jpeg)

Fig. 2 Graphical representation of the methodology

# 3.3 Exploratory phase: feature selection 

Considering the primary goal of the proposed framework (i.e., risk identification early in epidemics or pandemics), we made the assumption that none of the COVID-19 risk elevators were known before conducting this study. In other words, we initially assumed each chronic condition as an equally important potential risk factor contributing to the likelihood of death by COVID-19, resulting in a high-dimensional data set (i.e., a binary flag feature representing each condition). This large number of features is known as a major challenge in bioinformatics studies (Alexe et al., 2006). It is shown in the literature that evolutionary search algorithms are efficient approaches for finding an optimal, reasonably small subset of features with minimal harm to the distinctive power and informativeness of the data (Fan \& Chaovalitwongse, 2010; Mehmanchi et al., 2021; Şeref et al., 2018).

In line with the literature, to address the high dimensionality issue of our dataset, we employed an evolutionary heuristic search approach, namely the Genetic Algorithm (GA) (Holland, 1992), to find a nearly optimal subset of variables. GA uses a chromosome-like string to represent each potential solution in an optimization problem (i.e., a set of features in this paper); it then uses a set of rules to randomly generate a population of feasible chromosomes. Through several generations (iterations), the top chromosomes of each population (based on their fitness function score) are maintained for the following generation, and new chromosomes replace the rest. The process of generating new child chromosomes is partially random, and the rest through the mating of the top parent chromosomes from the previous generation (i.e., crossover of two chromosome strings or mutating a single chromosome). The procedure of developing additional generations is repeated until the variations in the best fitness value are minimal across several successive generations (i.e., the convergence of the algorithm).

GA forward selection approach was used with a population size of 1000 solutions in each generation to refine the feature set. The data was split on a chronological basis, with the data

of COVID patients identified before April 22, 2020 (around 79.5\% of the sample) being used for training and the rest of the data used for validation purposes. Each initial population's solution of the GA contained an arbitrary subset of 50 out of the 1407 chronic conditions of the data set. The chromosome length was determined after running the algorithm multiple times with different lengths (between 30 and 200) and observing no major improvement for those longer than 50 features. In each generation, the features selected by the algorithm were employed to train a random forest (RF) classification model with basic settings using the training subset of data. We noted the model performance on the validation subset. RF was chosen for feature selection given having too many binary features in the data; prior research has shown that tree-based methods are powerful algorithms in the existence of several binary categorical features (Davazdahemami et al., 2022).

The area under the receiver operating characteristic curve (AUC) was employed as the fitness function to select the top feature sets in each generation. AUC was chosen (among other evaluation metrics) since it indicates the distinctive capability of each selected feature set in identifying the two classes of patients. We utilized a tournament strategy as the selection process of the algorithm; the survival rate, elitism rate, crossover rate, and mutation rate were set to $20 \%, 30 \%, 30 \%$, and $10 \%$, respectively. We let the algorithm train for a maximum of 100 generations with an early stop possibility in case of convergence and showing no improvements in 10 consecutive iterations. Finally, for descriptive analysis, the best feature set associated with the greatest AUC was retained (phase 2), and subsequently developing the Bayesian Belief Network model for explaining the relative individual and combined risk of each identified factor.

The GA procedure pursued for feature selection is summarized in the pseudo-code shown in Fig. 3.

# 3.4 Descriptive phase: understanding patterns and inter-relationships 

In the second phase of our framework, we take advantage of descriptive analytics tools to dig into the details to obtain some initial insights into the relationship patterns among the selected features with the target variable.

Specifically, we first look into the relative survival and death rates for patients suffering from each single selected chronic condition. Given the feature selection criteria explained above, we expect to observe relatively high diagnostic power for each feature, reflected as a significant difference between their corresponding survival and death rates. Hence, in addition to getting insights at the bivariate level, this can be considered a validation mechanism for the feature selection step.

Second, we use descriptive tools to investigate the conditions' pairwise comorbid relationships with the survival factor. For each pair of the selected chronic conditions, we look into the frequency of cases diagnosed with the novel disease as well as the relative death rate. This can provide us with insights into patients' vulnerability with a history of each comorbid pair in terms of contracting the disease and mortality.

### 3.5 Explanatory phase: probabilistic prediction model and inference simulator

### 3.5.1 Probabilistic models and Bayesian belief networks

Since its origin (Wright, 1934), probabilistic graphical models built from DAG (Directed Acyclic Graphs) have come long. Its variations have found use in a wide variety of fields.

Input: instance $\pi$,
Size of population $(\alpha)$,
Rate of elitism $(\beta)$,
Rate of mutation $(\gamma)$,
Maximum Number of generations $(\delta)$
Number of generations to terminate in case of no improvement $(\mu)$
Output: solution $X$
// initialization
Generate $\alpha$ feasible solutions (feature sets) randomly;
Save them in the population $p o p$;
Initiate a placeholder variable for the highest area under the curve $\mathrm{AUC}^{*}=0$;
Initiate a counter variable to count the number of consecutive generations with no improvement $\mathrm{g}=0$;
// loop until the max number of generations
for $i=1$ to $\delta$;
// elitism-based selection
Train a Random Forest (RF) model using pop as predictor features set;
Evaluate the RF model using AUC criterion;
Save the AUC of the best pop solution as $\mathrm{AUC}_{\text {pop }}$;
if $\mathrm{AUC}_{\text {pop }}>\mathrm{AUC}^{*}$ :
$\mathrm{AUC}^{*}=\mathrm{AUC}_{\text {pop }}$;
$\mathrm{g}=0$
else:
$\mathrm{g}=\mathrm{g}+1$;
if $\mathrm{g}>=$ $\mu$ then break
Number of elitism $n e=\alpha^{*} \beta$;
Select the best $n e$ solutions (based on AUC) in pop and save them in pops;
// crossover
Number of crossover $n c=(a-n e) / 2$;
for $j=1$ to $n c$ :
randomly select two solutions $\mathrm{X}_{\mathrm{A}}$ and $\mathrm{X}_{\mathrm{B}}$ from pop;
generate $\mathrm{X}_{\mathrm{C}}$ and $\mathrm{X}_{\mathrm{D}}$ by one-point crossover to $\mathrm{X}_{\mathrm{A}}$ and $\mathrm{X}_{\mathrm{B}}$;
save $\mathrm{X}_{\mathrm{C}}$ and $\mathrm{X}_{\mathrm{D}}$ to pops;
end crossover loop;
// mutation
for $j=1$ to $n c$ :
select a solution $\mathrm{X}_{j}$ from pops;
mutate each bit of $\mathrm{X}_{j}$ under the rate $\gamma$ and generate a new solution $\mathrm{X}_{i}^{\prime}$;
if $\mathrm{X}_{i}^{\prime}$ is infeasible:
update $\mathrm{X}_{i}^{\prime}$ with a feasible solution by repairing $\mathrm{X}_{i}^{\prime}$;
replace $\mathrm{X}_{j}$ with $\mathrm{X}_{i}^{\prime}$ in pops;
end mutation loop;
// updating population
pop $=$ pop $_{1}+$ pop $_{2} ;$
end generations loop;
// Returning the best solution
Return the best solution $X$ in pop ;
Fig. 3 Summary of the feature selection GA algorithm

Bayesian Networks (BNs) are used to solve various issues in machine learning and cognitive science. While BNs may be used to investigate the domain in a causally accurate manner, they can also be used for the explanatory purpose to disentangle statistical correlation from causal effects. Essentially, the BN model is a directed acyclic graph (DAG). The nodes correspond to the relevant variables (e.g., whether the patient has dementia with behavioral disturbance and/or unspecified atrial fibrillation). The conditional dependence between variables is symbolized by arcs (Pearl, 1988). The arc directions illustrate the dynamics between a parent and child-an arrow connecting A and B , where A is the parent node of B , indicates that the probabilities of B are conditionally tied to the values of A . Another valuable method to conceptualize the Bayesian model is via the lens of hypothetical events. Each arc represents a statement about the outcome of a hypothetical event; if we could wiggle A, we would expect to notice a change in the probability of B. Assuming no other variables exist, Fig. 4 illustrates a simple DAG reflecting the relationship between $\times 1$ : the patients' age, $\times 2$ : their status of dementia with behavioral disturbance, and $\times 3$ : their status of unspecified atrial fibrillation.

![img-2.jpeg](img-2.jpeg)

Fig. 4 Example of a DAG diagram

Three distinct patterns may be considered in this context: Since age is a prevalent cause or confounding variable of dementia with behavioral disturbance (1) and unspecified atrial fibrillation (2), individuals with dementia with behavioral disturbance often have unspecified atrial fibrillation. However, the association is not causal—giving a patient with dementia with behavioral disturbance does not automatically result in unspecified atrial fibrillation; instead, both conditions are described by a third factor (3), the patient's age.

We are interested in two types of probabilities. The marginal probability is the probability that it will occur regardless of the result of another variable, a node that has no parents. The conditional probability is one event happening in the presence of another event, a node that has parent(s). Conditional probability tables (CPTs) link parent and child node states and have entries for all possible child and parent node states compositions. Following the conditional dependencies among these variables, BN offers a simple way to assess the joint distribution of a set of random states; hence one can calculate the conditional probabilities of any subset of factors. Furthermore, the graphical aspect of Bayesian networks is helpful since it allows users to receive a visual perspective of the subject at hand. To simplify complex joint probabilities, the BN chain rule is used (Koller \& Friedman, 2009):

$$
P\left(x, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid Y_{x_{i}}\right)
$$

where each $x_{i}$ denotes child variables, and $Y_{x_{i}}$ represents parent(s). Figure 4 illustrates this in action: $\mathrm{P}(\times 3 \times 2, \times 1)$ is the probability of unspecified atrial fibrillation given the value of the patient's age (it is independent of dementia with behavioral disturbance when conditioning age).

In order to develop a BBN model, there are two options: (1) a manual approach, more subjective based on expert opinion (2) a data-driven analytical approach, which induces the structure utilizing advanced mathematical models (Koller \& Friedman, 2009). Since CPTs are calculated for all states of the parent nodes to those of a child node, their size increases exponentially. Consider a single child node that has $m$ parents and both child and parents have n states; the total number of entries in the CPT becomes $n^{m+1}$. For example, a simple CPT with $\mathrm{m}=2$ and $\mathrm{n}=5$, the CPT requires 625 entries. Thus, eliciting a simple-sized network requires a set of domain experts to study for many hours, which would be expensive

and time-consuming (Korb \& Nicholson, 2010). Furthermore, expert reasoning may elicit biased and doubtful outcomes due to differing viewpoints.

Numerous earlier research works have shown a variety of approaches for inducing the structure using data. The Naive Bayes method is a simple technique that uses the Bayes rule and requires computing the probability of the class/target number for each input value. Naïve Bayes limits the structure with an assumption that all variables are independent. The TAN model, an upgraded version of the naive Bayes, implements a tree-structure model (Friedman et al., 1997). The TAN model builds on the Naive Bayes model by adding a degree of interaction between the system's characteristics. Each attribute in the TAN model relies on its class and one additional variable from the variable set (see Fig. 4). Since this model integrates attribute dependencies, it is more realistic than a Naive mode and outperforms other data-driven structural learning techniques such as Naive Bayes and Markov blanket (MB). Korb and Nicholson's paper has further examinations and specifics on comparing BN structures- naïve Bayes, TAN, and MB (Korb \& Nicholson, 2010).

In our context, we evaluated several structural learning algorithms and chose the TAN model due to its superior performance. After constructing the structure, BN may act as an inference simulator, allowing for the extraction of all domain relations via simulation. Using CPTs, the reasoning would be more effective despite multiple unknowns, and one can conduct Omni-directional inference using the BN decision support simulator. Eliciting inference from simulation inside a BN is time-consuming and requires many resources (Topuz et al., 2018b). However, technologies have been applied that are capable of doing the necessary tasks in the background, and these algorithms are all capable of being implemented successfully in the inference simulator. For this purpose, we present the findings using a web-based inference simulator (see results and discussion session).

# 3.5.2 Understanding uncertainty in probabilistic modeling- mutual information and entropy concepts 

Shannon's mathematical theory of communication shows us entropy could be used to quantify information content (Shannon, 1948). In information theory, entropy provides a mathematical way of quantifying uncertainty. A greater entropy value suggests a greater degree of informational uncertainty; or, more practically, a greater number of potential outputs of a function. We would want thorough information about a patient to generate a credible risk assessment in our case. However, would we be absolutely unsure of its worth if we did not have all the patient-specific knowledge, say missing information about the heart condition! Even if we did not know anything about the patient's specific heart condition, we might have the patient's "age_at_encounter," "payer_information," and other chronic conditions. The risk of being deceased can be updated with the given information. Knowing "age_at_encounter" leads to an information gain, and the "average information gain" would allow you to reveal the predictive significance of observing these variables. We can calculate the target variable's conditional entropy given the predictive variable as follows:

$$
H\left(\text { Deceased } \mid \text { Age_at_encounter }\right)=\sum_{i} P\left(\text { Deceased } \left.) H\left(\text { Deceased }_{i}\right| \text { Age_at_encounter }_{i}\right)
$$

where H denotes the entropy, the difference between the marginal and the conditional entropy, given that the predictive variable is formally known as Mutual Information (MI). In our context, the MI is the marginal entropy of "Deceased" minus the conditional entropy of "Deceased" given "Age at encounter" it can be formally defined as:

$$
\text { MI(Deceased, Age_at_encounter) }=H(\text { Deceased })-H(\text { Deceased } \mid \text { Age_at_encounter })
$$

In general form, MI is:

$$
M I(A, B)=H(A)-H(A \mid B)
$$

which translates as:

$$
\operatorname{MI}(\mathrm{A}, \mathrm{~B})=\sum_{a \in A} P(a) \sum_{b \in B} P(b \mid a) \log _{2} \frac{P(b \mid a)}{P(b)}
$$

The above enables us to measure the MI among any variables. In other words, we may identify which variable generates the most information gain and so has the most predictive significance.

# 3.5.3 Validation framework and performance evaluation 

Several measures for "true performance" of dependent variables models (Sokolova \& Lapalme, 2009) and "true understanding" of complicated relationships (Gonzalez-Lopez et al., 2019; Topuz et al., 2018a) have been developed in the literature. A full extent of the performance is essential, as is an insight into the problem's complicated structure. Thus, this article offers (a) measures for assessing overall performance (including AUC, accuracy, and dependability), as well as (b) measures for illustrating interrelationships and conditional interdependence (reporting MI and entropy).

One of the most often used estimation techniques for classification-type data mining models is to split the data into training and testing sets, a process known as training-testing split (Delen et al., 2020). Cross-validation and bootstrap resampling are two popular implementations of this possible method presently (Benbasat \& Nault, 1990; Delen, 2010). The stratified k -fold cross-validation procedure randomizes the entire dataset (all samples/rows) and then divides it into k distinct subsets, each with a nearly equal number of samples/rows and roughly similar dependent variable classes (Fig. 5a). The model is trained on the first $\mathrm{k}-1$ subsets of the given dataset and then evaluated on the last subset. This experimental technique is repeated k times (i.e., training preceded by testing). Each iteration includes a new fold as the test dataset and the remaining folds as the training dataset, repeating this process until the desired conclusion is reached. The classifier's overall performance is then computed by taking a simple average of the performance measurements obtained from each
![img-3.jpeg](img-3.jpeg)

Fig. 5 a Stratified k-fold cross validation. b. Bootstrap method

k individual test sample. A bootstrap sample is formed by resampling n cases using replacement and then resampling the sample again. Therefore, duplicate instances may appear in a bootstrap sample (Fig. 5b). After n samples, the likelihood of any given case not being taken can be estimated: $(1-1 / n)^{n} \approx 1 / e \approx 0.368$. In test sets, the anticipated number of unique occurrences from the initial dataset can be computed: 0.632 n .

Kim (2009) demonstrates how the bootstrap estimator suffers from bias when using a small sample size. In order to reduce the impact of bias imposed by random sampling, k -fold cross-validation can be employed. However, when the sample size is not big enough, Kohavi (1995) explains how the k -fold cross-validation method suffers from variance. To present a complete picture of a credible estimate, this study includes both resampling procedures, k -fold stratified cross-validation, and bootstrap.

# 3.5.4 WebSimulator- inference generator 

This study provides a web-based inference calculator (WebSimulator) that links data, analysis, and computing. Specifically, instead of using single-point predictions, we develop a BN model that explicitly accounts for uncertainty in all assumptions. The inference engine that powers the WebSimulator output is this BN and the objective is to build a model from data and predict Covid death probability. WebSimulator has grown into a decision aid that allows the user to access and share data within the BN via visualization, modeling, and interactive analytical approaches that enhance interpretation and decision-making. By using the WebSimulator as a platform for broadcasting inter-active models over the internet, this research allows end-users to engage with scenarios and get a better grasp of the model's underlying dynamics, so making it more accessible to a broader audience. Importantly, any such "machine-learned solutions" may be readily duplicated by stakeholders, who can use the WebSimulator to test out different alternative assumptions and policy scenarios.

## 4 Results and discussion

### 4.1 Summary of exploratory analysis

### 4.1.1 Feature selection

The feature selection algorithm was executed on a PC with a 2.90 GHz processor and 64 GB of main memory. The model convergence was obtained after 29 generations which took roughly 4 h of processing time. Table 3 indicates a summary of the 50 selected conditions by category (some conditions belonged to multiple categories).

Generally, we identified the same groups of risk factors as those noted in meta-analytic studies of the literature. Nevertheless, those studies were mostly conducted months after the onset of COVID-19 in the US. Moreover, we noticed some chronic diseases (categorized as "other") that are typically prevalent among senior patients (e.g., arthritis, dementia, and cognitive impairment), which suggests that their inclusion among the selected features by the genetic algorithm could be attributed to patients' age instead of the disease itself. This has been pointed out by MacLeod and Hunter (2021), who maintain that in the studies of COVID-19, its age-dependent effects must be taken into account.

Table 3 Selected chronic risk factors by category


# 4.2 Summary of descriptive analysis 

First, we assess the bivariate relationships among each individual chronic condition with the COVID-19 survivability of the patients suffering from that. Figure 6 shows the proportion of survived vs. dead COVID patients who suffered from each of the chronic features (ICD-10 codes) selected through the GA process.

As shown, a majority of the selected features are remarkably different in terms of the COVID-19 survival rate. This indicates the relatively high diagnostic power of the selected feature set that, considering the AUC criterion (with emphasis on maximizing diagnostic power of the prediction model) for the GA feature selection, suggests the efficacy of the feature selection approach.

At the individual condition level, the chart suggests that amyloidosis (ICD-10: E58.5), postprocedural hypopituitarism (ICD-10: E89.3), nonautoimmune hemolytic anemias (ICD10: D59.4), and cardiac arrest (ICD-10: I46.9) are the top fatal risk factors.

While studying risk factors at the individual level could be insightful, many complications arise when two or more conditions develop at the same time. Figure 7 indicates the COVID-19 mortality rate of comorbid conditions resulting from pairing up the selected chronic features. The heatmap suggests interesting potential complications at the pair level of comorbidity. For instance, whereas the occlusion and stenosis of cerebral arteries (ICD-10: I66.0) at the individual level do not seem to be diagnostic-aiding at all (i.e., $50 \%$ survived, $50 \%$ deceased), at the pair level, $100 \%$ of patients who had that condition along with vitamin D deficiency (ICD-10: E55.9) have died. Similarly, while gout (ICD-10: M10.9) and hypertensive heart and renal disease (ICD-10: I13.0) individually involved mortality rates of $16.4 \%$ and $38.1 \%$, respectively, patients who developed both conditions turned to have a mortality rate of $83 \%$. As another example, thrombocytopenia (ICD-10: D69.6) has an individual death rate of $25.6 \%$, whereas its comorbidity with no-insulin-dependent diabetes mellitus (ICD-10: E11.1) and hypertensive heart and renal disease (ICD-10: I13.0) increase its corresponding death rate to $100 \%$ and $78 \%$, respectively.

![img-4.jpeg](img-4.jpeg)

Fig. 6 Survival and death rate in COVID-19 patients by their chronic conditions

Whereas complications associated with pairwise comorbidities are insightful, in the next stage employing the Naïve Bayes Network approach, we step up and look into more complicated confounding patterns resulting from multiple comorbid conditions.

# 4.3 Summary of explanatory analysis 

BNs can be used in a wide range of real-world situations because they can help with analyses when there is a high degree of uncertainty. This study includes both resampling procedures, k -fold stratified cross-validation, and bootstrap to present a comprehensive picture of a credible estimate. In other words, we produced twenty different probabilistic inference models: ten for k -fold and ten for bootstrapping. Table 4 shows the average of ten folds predictive performance. Overall, the bootstrap results did better than the k-fold results (Mean ROC: 90.8 percent vs. 85.8 percent).

Typically, in traditional statistical analysis, the correlation and covariance are explored to understand their relative significance, specifically for the target variable. The current study offers an alternative technique, based on information theory (Ehsani et al., 2010; Topuz et al., 2021a), for determining how observing a variable improves the uncertainty of the probability of a novel disease (see Sect. 3.5). Here we employed the information gain concept -using

![img-5.jpeg](img-5.jpeg)

Fig. 7 The mortality rate of COVID-19 patients by pairwise comorbid conditions

Table 4 Cross-validated classification performance


K-Fold (10)—Stratified


entropy and MI- to measure the uncertainty and determine which variable has the most predictive power. The BN shown in Fig. 8 illustrates how the states on nodes represent MI with the dependent variable, representing the maximum information gain between nodes.

Patient's age (Age at encounter- 0.078) is the most significant predictor, followed by number of diagnoses the patient has (numDiagnosis- 0.056) and type of patient's encounter (encounter_type- 0.052). Among the comorbidities, the patient's cardiac arrest (unspecified)

![img-6.jpeg](img-6.jpeg)

Fig. 8 Bayesian Network for risk factors (node volume symbolizes MI with the dependent variable; values on arcs specify MI between nodes)
status has the most information gain (I46.9- 0.003), followed by the patient's encephalopathy status (G93.4- 0.002), and the patient's unspecified dementia without behavioral disturbance (F03.9- 0.001). A comprehensive list of all comorbidities and factors can be found in Appendix A with their relative significance.

# 4.3.1 Omnidirectional inference with web simulator 

We created an example using omnidirectional inference and ran several simulations on various network components to show how to interpret the conditional dependencies. The marginal probabilities are depicted in Fig. 9 as horizontal bars, along with the amount of information received by observing the age variable (second row), cardiac arrest (I46.9) (third row), and encephalopathy (G93.4) (the bottom row). Mortality has marginal probabilities of $90.5 \%$ ( $=0$ - not deceased) and $9.5 \%$ ( $=1$ - deceased). Updating the information on variable age (age $>78$ ), the probability of being deceased increases to $29.9 \%$ compared to the marginal probability of $9.5 \%$. Similarly, if we have information that the patient has a cardiac arrest, the probability of being deceased increases to $84.7 \%$. On the other hand, observing cardiac arrest changes the distribution of age mean from 54 to 70 . Updating the belief on both ages ( $>78$ ) and cardiac arrest $(=1)$ increases the probability of being decreased to $93 \%$. In addition, the probability of encephalopathy increases by $15 \%$. Indeed, all the probabilities in the graphical model's other components have been changed (even those not shown in Fig. 9).

Through WebSimulator, a list of all interactions in the domain can be revealed. Most importantly, despite several unknowns, reasoning can be done effectively regarding the application domain (Topuz et al., 2018a, 2021). Since the model is published online, users may play

![img-7.jpeg](img-7.jpeg)

Fig. 9 Example of omnidirectional inference
around with various scenarios and examine the model's dynamics and explore the omnidirectional inference. The simulator has evolved through visualization, modeling, and analysis into an instructional tool capable of efficiently extracting and disseminating knowledge inside the PGM, acting as a gateway connecting human and artificial intelligence. To interact with the model and analyze risk factors for a novel, contagious disease in a specific patient with knowledge of demographic and chronic factors, a healthcare provider can use the WebSimulator, an adapted version of the predictive analyzer, which is publicly accessible at https:// simulator.bayesialab.com/\#!simulator/59628240012.

# 5 Conclusion 

Understanding the main chronic risk factors, which allows for more effective allocation of scarce resources and improving treatments, is among the top public health management priorities during the outbreak of a novel viral disease. Whereas clinical studies in a controlled environment are considered the most reliable technique in detecting such risk factors, their

considerable time requirements may result in the loss of many lives, apart from the negative social and economic impacts which may arise from long-term lockdowns required to bring the outbreak in control. When there are epidemics or pandemics, predictive and prescriptive analytics can help medical experts and policymakers figure out which chronic risk factors are most important to keep an eye on. This is critical both in adjusting proper preventive measures as well as in identifying patient groups at high risk of mortality to be prioritized for the limited available health resources.

The three-phased -exploratory, descriptive, and explanatory (EDE)- methodology proposed in this study combines various data analytics tools. In this study, we used genetic algorithms, Bayesian networks, and innovative model interpretation approaches to create a complete EDE methodological approach that may benefit clinical decision-makers in responding quickly to a pandemic. We showcased the effectiveness of the proposed approach by implementing it on early COVID-19 data obtained from a large EHR repository in the United States.

Even though risk factors discovered by our proposed technique have already been mentioned in the past studies, what distinguishes the current study is the capacity introduced by the proposed approach to acquire highly similar findings within a considerably shorter period. For example, while the earliest published clinical studies discussing the role of Diabetes mellitus type II and Thrombocytopenia in increasing the mortality odds of COVID-19 patients are dated back to May (Bloomgarden, 2020) and April of 2020 (Yang et al., 2020), we could not find studies mentioning the increased risk of mortality in patients having both conditions together, published earlier than late July 2020 (Zhang et al., 2020). That is, using our proposed approach, the risk associated with that comorbidity combination could have been discovered around a month earlier than it was. Additionally, for some comorbid pairs of chronic conditions like Diabetes and Mitral insufficiency we could not find any studies indicating the increased mortality rate associated with them in COVID-19 patients, even until mid-2022, although they both have been identified as independent risk factors by around mid-June of 2020.

These timelines could have been shortened even further if international institutions responsible for global health policies develop proper monitoring and information governance techniques for future pandemics and effectively use social networks for crowdsourcing potential risk factors and symptoms from the general population (Zolbanin et al., 2021). For example, while we were able to reliably establish the risk variables using data from early US cases, highly comparable results could have been acquired sooner provided that there existed an efficient international health data exchange infrastructure allowing for a faster flow of valid information. There are two primary ways in which we believe that earlier detection of risk variables would have resulted in lower total mortality. To begin, more accurate information could have been supplied earlier in the epidemic to high-risk patients. Second, better outcomes may have been achieved by more efficiently prioritizing and administering scarce healthcare resources. The majority of COVID-19 chronic risk factors might have been spotted as early as the third week of March 2020 (considering the earlier $80 \%$ of COVID-19 cases in our data chronologically for training the prediction model), about the time the World Health Organization labeled the infection a global pandemic. That is significantly earlier than when risk elements were identified and reported in peer-reviewed journals. Studies including this one show how machine learning methods can save time when looking for early signs of illness; we think that major health agencies around the world should collaborate and establish the infrastructure and skills needed to do data analysis early on in future similar situations.

In fact, the primary contribution of this study is proposing a framework to discover risk factors of novel diseases (and the role of comorbid risk factors) while requires minimal prior

knowledge about those diseases. Even though most (and not all) of the risk factors were discovered within 6-12 months after the onset of the pandemic, we argue that using our proposed framework they could have been discovered several months earlier. This could have led to saving thousands of lives across the world just by taking more informed medical decisions. Particularly given the limited amount of resources during outbreaks a more accurate list of risk factors (and their potential comorbidity interrelationships) can considerably help the healthcare authorities in adjusting their resource allocation priorities accordingly.

While our study sheds light on the benefits of the machine learning models in the early detection of chronic risk factors, there are several limits to our study and thus opportunities for additional future research. For instance, the utilization of data obtained from a single data source may raise concerns about the generalizability of findings. Hence, we encourage future researchers to validate our proposed framework using data from other EHR repositories and/or possibly from a combination of different repositories and perform a comparative assessment of the identified risk factors thereof.

Funding No funding sources to declare.

# Declarations 

Conflict of interest All authors declare that they have no conflict of interest.

## Appendix A. Comprehensive list of comorbidities in overall analysis with "deceased"




The variables are arranged according to their Relative Significance (Ri) to the Target Node. ${ }^{*} R_{i}=I\left(M_{i}, F\right) / \max _{i} I\left(M_{i}, F\right)$ where Mi denotes the ith manifest variable, while F denotes the ith factor variable and $\mathrm{I}($.$) returns the Mutual Information.$
