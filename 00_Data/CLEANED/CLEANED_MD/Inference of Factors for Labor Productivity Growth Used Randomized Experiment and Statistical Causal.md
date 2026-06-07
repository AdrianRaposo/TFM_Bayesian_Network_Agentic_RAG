# Article 

## Inference of Factors for Labor Productivity Growth Used Randomized Experiment and Statistical Causality

Ekaterina V. Orlova (D)<br>check for<br>updates

Citation: Orlova, E.V. Inference of Factors for Labor Productivity Growth Used Randomized Experiment and Statistical Causality. Mathematics 2023, 11, 863. https://doi.org/10.3390/ math11040863

Academic Editor: Anatoliy
Swishchuk
Received: 26 December 2022
Revised: 2 February 2023
Accepted: 6 February 2023
Published: 8 February 2023

## (0)

Copyright: (c) 2023 by the author. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Department of Economics and Management, Ufa University of Science and Technology, 450000 Ufa, Russia; ekorl@mail.ru


#### Abstract

The study of causal dependencies in economics is fraught with great difficulties, that it is required to consider not only the object structure, but also take into account a huge number of factors acting on the object, about which nothing is either known or difficult to measure. In this paper, we attempt to overcome this problem and apply the theory of statistical causality for labor productivity management. We suggest new technology that provides the inference of causal relations between the special programs implemented in the company's and employee's labor productivity. The novelty of the proposed technology is that it is based on a hybrid object model, combines two models: 1-the structural object model about its functioning and development to provide a causal inference and prediction the effect of explicit factors; 2-the model based on observed data to clarify causality and to test it empirically. The technology provides integration of the theory of causal Bayesian networks, methods of randomized controlled experiments and statistical methods, allows under nonlinearity, dynamism, stochasticity and non-stationarity of the initial data, to evaluate the effect of programs on the labor effeciency. The difference between the proposed technology and others is that it ensures determination the synergistic effect of the action of the cause (program) on the effect-labor productivity in condition of hidden factors. The practical significance of the research is the results of its testing the proposed theoretical provisions, methods and technologies on actual data about food service company. The results obtained could contribute to the labor productivity growth over uncertainty of the external and internal factors and provide the companies sustainable development and its profitability growth.


Keywords: causal relations; causal inference; randomized controlled experiments; causal Bayesian network; resource efficiency of companies; labor productivity growth

MSC: 62P20

## 1. Introduction

The study of causal relations in economic and social systems is connected with significant difficulties, consisting in the fact that, together with the object (system) under consideration, it is necessary to take into account a huge number of factors about the object. These factors are either unknown, or it is impossible or difficult to measure. So, the results of data observations and understanding of the substantive (essential) foundations of the studied object are required. If the set of factors that directly affect the object is known, then the determination of the impact effects on the object characteristics can be reduced to finding the regression coefficients of the dependent variable and the independent factors. If the impact of factors on the object is complex, changing, or the composition of these factors is unknown, or there is a certain group of hidden, implicit factors, then the impact effect is difficult to determine.

The features of data describing economic and social processes limit an application of classical methods of statistical modeling, approximation and forecasting, are the following.

1. Different data scales. Economic data use binary, nominal or ordinal scale.

2. Samples heterogeneous, distribution of data attribute values may differ from the normal distribution law. Known statistical approximation methods such as maximum likelihood or least squares are extremely sensitive to inhomogeneities in such data.
3. Fuzziness, incompleteness of data or gaps in the original data. The struggle with overcoming this is the removal of redundant data, but this also has a negative side, as it leads to loss of information.
4. Stochastic data. The prerequisites of statistical parametric methods for identifying models presuppose the determinism of the characteristics of the object under study. But determinism can occur more often in the case of planned experiments, when exogenous variables are clearly controlled. If the data is stochastic in nature, then other approaches and methods are required-machine learning, methods of the theory of random processes, etc.
5. Data correlation and data heteroscedasticity. Correlations in the data often occur between the studied parameters of the object, the cause of which is incorrectly chosen factors, errors in the models specification. Multicollinearity and heteroscedasticity significantly distort the model results obtained on the basis of classical statistical parametric methods.

All of the above requires a fundamentally new methodological approach for modeling causal relations and solving the forecasting problem, based on methods and algorithms that are not sensitive to these features, which can be used in various applications of the economy.

The purpose of the investigation is to develop a technology that provides with a high reliability the establishment of a causal relation between the implementation of alternative management decisions (programs) and the productivity of the company's employees, and is designed to select decisions (programs) based on the their effect on labor productivity.

The article is organized as follows. The second section discusses the existing methods and approaches to the study of causality and causal relations, and provides a comparative analysis of causality models. The third chapter considers in detail the proposed technology for evaluating the effectiveness of alternative managerial impacts on labor productivity, describes the methods and analysis tools used. The fourth section describes an experiment conducted in a large catering company and discusses the results of its analysis.

The research logic is as follows. In order for the methods and algorithms to give reliable results, it is necessary that the experiment results are determined solely by programs and do not depend on other factors (age, gender, etc.). For this, a randomization procedure is used. Randomization allows to neutralize the individual differences of employees and identify the program efficiency. With this approach, each employee has an equal chance to become a participant of the experiment.

The initial data for the study is obtained on the basis of a randomized controlled experiment, in which management decisions (programs) M1, M2, M3 are tested on the treatment and control samples, the purpose of which is to increase the productivity of the company's employees.

The first program is M1 "partial remote work". The target group of this program consists of service departments employees, as well as employees who providing purchases. The expected effect of this program is a decrease in the incidence of employees, a decrease in staff turnover, and a decrease in labor costs.

The second program is M2 "rating system for employees and using bonuses". The target group of this program is employees working in the production departments. The program involves the introduction of a rating system between individual production departments of the enterprise; identifying the best department for a certain period according to various criteria; introduction of a checklist for daily employee surveys and employee bonuses implementation. The expected effect of this program is a reduction in high staff turnover, a reduction in personnel management costs, and an increase in employee motivation.

The third program is M3 "internships in leading companies". For this program, a system for improving the skills of employees will be implemented by sending them to internships in leading companies. The expected effect is to improve the quality of products, increase sales volumes, and increase the company's revenue.

As a result of the experiment, panel data is generated reflecting the results of observations of 40 employees (for each tested program, a total of 120 employees took part in the experiment), 20 of which were included in the treatment group, the other 20 is in the control group for 8 months (during 4 months, the treatment group is not affected, and the next 4 months-the impact is carried out).

Primary data analysis is carried out on the basis of exploratory analysis and the "difference-in-differences" method, which assess the cumulative expected effect of the programs to the labor productivity. However, these method has a number of significant drawbacks associated with not taking into account the impact on labor productivity of the other (indirect, latent) factors.

To overcome this shortcoming and solve the problem of determining direct and indirect factors affecting labor productivity, we use a statistical approach to test causal dependencies in conditions of non-reproducibility of observations, based on the concept of Markovian properties of a set of variables. It is proposed to use Bayesian networks representing a directed acyclic graph on random variables with Markov properties. Here we use the concept of intervention by J. Pearl [1,2] to assess the full effect of competing programs on labor productivity arising in the Bayesian network architecture.

For a practical solution of the problem of causal relation identification between the use of an program and its impact on labor productivity, the results of the author's previous research [3,4], associated with human potential and social capital, the Bayesian network includes the factors "innovation", "motivation" and "social capital".

# 2. Literature Review 

### 2.1. Labor Productivity Growth as a Factor of National Security

The growth of labor productivity, along with the problems of modernizing priority sectors of the economy, is integral factors in economic development and key elements of the national security of any state. Labor productivity reflects the level of economic development of the country and forms the level and quality of life of population. In Russia, the national project "Improving Labor Productivity and Supporting Employment" [5] is being implemented, which is aimed at increasing companies' labor productivity.

Labor productivity is not only an economic characteristic of labor efficiency, but it also characterizes the efficiency of production activities of enterprises. It shows the cost of labor required to produce a unit of output. Known factors for labor productivity growth can be grouped into the following groups:

- material and technical factors, ensuring the innovativeness of production technologies, as well as the creation of highly productive jobs;
- factors that determine the degree of production specialization and concentration, ensuring lean production, optimization of the production structure and its volume, employees qualifications growth;
- socio-economic factors that determine the level of wages and working conditions.

In conditions of significant technological changes, the nature and conditions of work are changing. The economic and social characteristics of workers are becoming more diverse and are associated with digital transformation and the expansion of human activities. Consumer preferences, management models changes. Over the fourth industrial revolution, data, information, and knowledge become the main object of management. The nature of work changes under the influence of the digitalization of business processes. This contributes to the emergence of new and changing professions, leads to the disappearance of retired professions, and causes an increase in unemployment. In this regard, the problem associated with improving the quality of human capital, which provides one of the main productive resources of an enterprise, is important and relevant, providing social and economic effects.

It is possible to consider human capital both in a broad and in a narrow sense. In the first case, human capital reflects an intensive productive factor of economic development, the development of society and the family. It includes the labor force, knowledge, intellect,

labor of a person, providing his labor activity. In the second case, human capital integrates the health, intelligence of a person, his high-quality and productive work, as well as the quality of his life.

The human capital of companies can include organizational (structural) capital [6], social and consumer capital [7] as a component of intellectual capital in the form of skills and knowledge accumulated by the company, as well as a non-physical resource for creating added value [8,9]. In [10], much attention is paid to the institutional components of a company's human capital.

Social capital as a structural component of human capital affects the ability of a person in his work to form innovative solutions, which is extremely important in the context of globalization and digital transformation of economic systems and ESG-oriented business in the global scientific community. The main purpose of social capital is to reproduce certain values from the social structure and turn them into a productive resource that ensures the achievement of the goals of an individual or team. Human behavior is determined not only by rational goals, but is also subject to a number of irrational factors associated with emotional activity, moral and value restrictions, trust and social obligations. When managing social capital, it is important to take into account these behavioral factors and promote more effective interaction between employees, develop trust between colleagues, and ensure the highest quality of teamwork.

In $[3,11]$ proposes a methodology for assessing the social capital of employees and the company, taking into account the factors of interpersonal and institutional trust, involvement in social networks and labor values, based on statistical processing of data representing objective information about the employee, and subjective information obtained as a result of a survey, allowing a comparative analysis of employees from the standpoint of their social capital. It also provides not only empirical confirmation of the influence of social capital and its factors on the individual innovativeness of an employee, but also provides an essential (economic) explanation and interpretation of this influence.

# 2.2. Analysis of Methods for Causal Relations Modeling 

### 2.2.1. The Concept of Causality, Causal Relations and Causal Inference

One of the defining goals of knowledge in any field is the recognition, explanation of the principles of functioning and development of any system, taking into account the cause-and-effect relations of processes and phenomena. The adequacy and possibility of using approaches to describe processes and phenomena depend on how correctly these causal relations are identified.

Causality characterizes such an influence of one event (process, phenomenon)—a cause on another event-a consequence, through which the event-effect occurs and without the event-cause it would not have arisen. The concepts of cause and effect are formed at the intersection of the principles of universal connection and development. From the standpoint of the principle of universal connection, causality is defined as one of the main types of connection in which the cause, under certain conditions, generates the effect. From the standpoint of the principle of development, causality is defined as any change and development, that is, a change towards the emergence of a new quality. Causal inference is the process of establishing the actual process-effect as a result of observing the process-cause and its change, which gave rise to the change in the process-effect.

It should be noted that not every relation is causal. The correlation between the factors characterizing the system and/or its external environment does not yet guarantee the existence of a causal relation between these factors. This is explained as follows:

1. The presence of an omitted variable. If two factors $x$ and $y$ correlate with each other, then the third factor $z$ can be the cause of their changes, the impact of which on the first two changes them simultaneously and unidirectionally. If a managerial impact on the factor $y$ is required, then a change in the factor $x$ will not be able to provide this, since a change in $y$ is facilitated by a change in the factor $z$. This phenomenon is known as the spurious correlation.

2. The presence of reverse causality. The proven correlation between factors $x$ and $y$ does not mean that factor $x$ affects factor $y$, since such a relationship may be different when $y$ affects $x$.
3. Non-representativeness of the sample and selection bias. As a result of the nonrepresentativeness of the sample, in which the sample does not fully and adequately reflect the general population. This could be due to the incomplete inclusion of all groups of respondents in the sample, incorrect determination of the sample size, which biases the results of estimates obtained from the sample and gives inaccurate results.
4. The presence of measurement errors. During the data collection phase of an experimental study or observation, systematic errors could occur due to intentional or accidental distortion of measurement data. Such errors lead to incorrect conclusions about the presence of causal relations.

# 2.2.2. Comparative Analysis of Causality Models 

One of the goals of mathematical modeling is to identify relations between the parameters of the system being modeled. It is important not only to determine these relations, but also to identify the factors-causes and factors-effects, as well as to reveal the effects that are caused by the influence of the factor-cause on the factor-consequence.

A causal model can be built in three ways:

1. Analytically based on the conclusion based on expert knowledge of the physical (technical, economic, social, etc.) laws that determine the functioning of the simulated system. This modeling method includes the construction of systems of differential equations [12], cognitive modeling [3,4,13,14], modeling based on operations research methods [15,16], simulation modeling [17-19].
2. Experimentally based on the processing of empirical data from observation or measurement (experiment) and the selection of approximating dependencies. This modeling method includes statistical modeling [20-22], modeling based on artificial intelligence and machine learning methods [23-26], data mining methods based on neural networks [26-29], graph models (structural equation modeling) [30-32], modeling based on a directed acyclic graph—Bayesian networks [1,33-37].
3. Hybrid causality model [11,18,19] combining the strengths of the two previous approaches and leveling their shortcomings.
The presented generalization of existing approaches to modeling causality within certain characteristics allows, on the one hand, to systematize the methods and models used to build models of such systems, taking into account the requirements for the control system, describing the uncertainty of the system parameters, the stage of its life cycle and other essential properties, and on the other hand, to carry out the choice of modeling tools adequate to the control object and its features, Table 1.

Integration of mathematical modeling with data-driven models provides higher predictive capabilities than models based only on statistical analysis or machine learning. At the same time, data-based models can be applied at the stage of the life cycle "operation" and systematically receive feedback from the object (process). Mathematical models based on physical processes are more appropriate in situational tasks and for decision-making under "what-if?" conditions. Hybrid models combine the strengths of the two previous modeling approaches and can be used in non-recurring situations or when there is insufficient data. The hybrid model at the stage of the life cycle "operation" makes it possible to increase the adequacy of the representation of the object and provide prediction probable deviations of the object's functioning from the normal modes [22].

Using a well-interpreted statistical model with a high level of adequacy, it is not possible to use it to prove causal relations between the object characteristics since established correlation does not yet mean causality. Therefore, causal relations cannot be substantiated only on the basis of a statistical approach and require the use of theoretical knowledge about causes and effects and the use of analytical (structural, causal) models.

Table 1. Comparative analysis of causality models (designed on the basis of the author's research [19]).


Modeling and establishing causal relations that determine the functioning and development of an object should be based on the combination of models based on data and physical models. Such a symbiosis will make it possible to increase the transparency of models, ensure their explainability, and enhance their generalizing and predictive ability.

Such a hybrid causality model should be presented in the form of a modular architecture, where various modules can be individually configured and adapted to solve new problems. This approach will allow using the experts knowledge and experiencen and at the same time the results of empirical findings. Like analytical (physical) models, the hybrid model will provide a causal understanding of the object and will be able to predict the effect of factors. At the same time, the justification of causal relationships and learning should be based on data-based models, replacing expert knowledge and judgments (often with weak and general assumptions) about the modeled object.

The hybrid causal model, having a high level of adequacy, combines both physical (mathematical) models and data-driven models.

# 3. Research Methodology 

For the considered problem of the company's employees productivity management, three different programs is developed, which effeciciency is evaluated on the basis of prove its causal relations with labor productivity growth: (1) partial remote work; (2) rating system for employees and using bonuses; (3) internships in leading companies. The best program should provide the maximum increase in labor productivity at minimum cost. It is necessary to test these programs in terms of their impact on labor productivity. After the research, the programs are ranked depending on the degree of their impact on the labor productivity.

We test the hypothesis: implementation of the program (each of the three separately) affects labor productivity (there is a causal relationship between the program implementation and labor productivity growth) under the influence of explicit and hidden factors of the labor productivity efficiency.

The methodological basis of the study is the developed concept and technology for modeling and management, designed to assess the impact of the tested program on the labor productivity growth, and used to support decision-making in the field of the personnel policy of a company, aimed at reducing the risks of human capital. The conceptual scheme of the technology is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Technology for labor productivity (LP) modeling and management based on the causal relations.
Let's consider the developed technology step by step.
Stage 1. At the first preparatory stage of the technology, a representative sample of employees is formed to conduct tests for each program. The sample of employees is carried out randomly from different departments of the company. Before the tests, all

candidates are instructed, voluntary consents are collected from all candidates to participate in experimental studies.

Stage 2. Conduct randomized controlled experiment. We use randomized distribution of participants in the experiments into treatment and control groups. Randomization is designed to divide a sample of employees into treatment and control groups so that it is impossible to predict in advance which of the two groups the individual will belong to. The most important step in a randomized controlled trial is the use of a masking method based on a double-blind study of the experiments results. This means that information about the participants in the treatent and control groups, including the participants themselves and the researchers who carried out the experiments, is closed. All information is available only to the person responsible for the testing. The double-blind survey method prevents systematic errors that can affect the experiment results. In each of the three of the treatment groups, one of the three programs is implemented, no intervention is performed in the control group. Observation is carried out for the treatment and control groups for 8 months.

Stage 3. Process of the results of randomized controlled experiments. Processing of the results is carried out on the basis of statistical analysis methods: descriptive analysis, correlation and regression analysis, the difference-difference method. Evaluation of the private prorgams effect on labor productivity is carried our. At this stage, the effect of the binary impact of the intervention (partial effect of the intervention) on labor productivity is estimated under the assumption that the difference between the treatment and control groups is due solely to the effect of the intervention itself, while the influence of other variables is leveled (in this case by randomization). Then the comparison of the results of the two groups can be interpreted from admitting causal relations between the programs impact on the controlled indicator-labor productivity.

Stage 4. Evaluation of the programs effeciency and conclusions about the choice one the program as the best management decision. Estimation of the total effect of the intervention on labor productivity based on a causal Bayesian network.

The developed technology is able to provide with a high degree of reliability the establishment of a causal relations between the implementation of alternative management decisions and the productivity of the company's employees, and is designed to select solutions (programs) based on the effect on labor productivity. The novelty of the proposed technology is that it is based on a hybrid causality model, combines two models: (a) the structural model built on the basis of a priori knowledge of about functioning and development and providing a causal understanding of the object and capable of predicting the effect of factors (explicit and indirect); (b) the model based on data, which is adapted taking into account empirical data obtained as a result of object observation. This technology has a high level of adequacy, uses heterogeneous research methods-the method of a randomized controlled experiment to obtain information about the tested programs, methods of statistical data analysis-the method of descriptive data analysis, the method of correlation and regression analysis, the difference-in-difference method to establish a causal relations between the implemented program and labor productivity growth, a Bayesian network of causality for building and analyzing a structural model of an object and explaining the causal relations of explicit and hidden factors affecting labor productivity in the context of the programs implementation.

The developed technology provides system integration of the theory of causal Bayesian networks, methods of statistical randomized tests and difference-in-differences and allows, under conditions of nonlinearity, dynamism, stochasticity and non-stationarity of the initial data, to evaluate the management decisions effect and choose the most effective solution. The difference between the proposed technology and others is that it allows to determine the synergistic cause effect the intervantion (program) on labor productivity under hidden factors affecting it.

# 4. Empirical Results and Discussion 

### 4.1. Evaluation of Partial Effect of the Programs

Design of the experiment for the first technology stage. A sample of 120 employees of a public catering organization, differentiated by the use/non-use of program, is being studied. Each program employs 40 people, 20 of whom is included into the treatment group, the remaining 20-into the control group. The division into subgroups is carried out by randomization. The experiment is carried out for 8 months, in the first four months the intervantion on the treatment group is not carried out, the second four months the treatment group is being under intervantion (program implementation). In the control group throughout the entire period of the experiment, no effects are provided. The characteristics of the individual labor productivity of employees are monitored before the start of the programs and during their implementation. In addition, based on the methodology described in [22], a survey of employees is carried out and an assessment of social capital, the level of motivation and innovativeness of company employees is carried out.

The problem is to evaluate the program effeciency in terms of the impact on labor productivity. In other words, it is necessary to test the hypothesis that there is a causal relations between theprogram implementation and the labor productivity growth.

Based on the experiments results, data sets are formed on the following employees' characteristics: individual labor productivity, labor productivity growth rate. At the second technology stage, we conduct the analysis of experiments results for each programs separately based on the following methods:

1. method of descriptive analysis for comparison of average levels of labor productivity in the treatment and control groups before and after the programs implementation;
2. "difference-in-differences" method [38-40] for evaluation of the programs impact on labor productivity in the medium term, based on the obtained parameters estimation of econometric models.

### 4.1.1. Descriptive Analysis of Experimental Results

For the correct application of the methods of descriptive data analysis (calculation of the average value, standard deviation), the initial data about individual labor productivity are converted into growth rates. The results of the descriptive analysis are presented in Table 2. for individual programs: (1) partial remote work; (2) rating system for employees and using bonuses; (3) internships in leading companies.

An analysis results of the average growth rates of labor productivity in the test sample before and after program 1 implementation indicates an increase in labor productivity by more than $6.8 \%$ (from 0.9686 to 1.0373 ). At the same time, the range of variation in labor productivity growth rates in the test sample is noticeably lower than in the control sample. Before the implementation of program 1 in the test sample, the range of variation was at the level of $13.9 \%$, and after the implementation it is $11.5 \%$. In the control sample, the range of variation also became lower and at the end of the experimental period amounted to $11.9 \%$. At the same time, the statistical homogeneity of the sample increases; in the test sample after the implementation of program 1, the coefficient of variation is about $3 \%$. It should be noted that in the control group before and after the experiment, there is a slight decrease in labor productivity- $0.5 \%$. At the same time, the range of variation of labor productivity for this group decreased comparable in the control group and amounted to about $11.9 \%$. This situation is developed due to this sample include more or less the same levels of labor productivity-about 200 rubles per person and not include employees who took sick leave during the test period.

Regarding the second program 2, the situation is similar, since labor productivity in the test group is growing, the average growth rate after the implementation of the program 2 is $3.7 \%$ per month, and in the control group before the implementation of the program, the growth in labor productivity was $2.5 \%$, and after implementation of the program, labor productivity decreased by $0.5 \%$. It should also be noted that in the control group, before the program implementation, the sample is characterized as statistically heterogeneous, since

Table 2. Descriptive statistics for the labor productivity growth rates (\%) by the programs 1-3.


The results of the data analysis about changes in labor productivity as a result of the program 3 showed the following. Before the program implementation, the test group is characterized by a decrease in the growth rate of labor productivity by an average of $2.5 \%$ per month; after the program implementation, the rate of decline slowed down to $0.5 \%$ per month. The control group was also characterized by a decrease in labor productivity by $1.1 \%$ per month before the implementation of the measure, but after the program implementation, employees in the control group showed a steady increase in labor productivity on average by $1.7 \%$ per month. Note that this control group is statistically heterogeneous in terms of labor productivity, the variation rate before the program implementation is about $40 \%$, that is, the sample included employees with a significant spread in labor efficiency values, and their dynamics is reflected by high volatility.

Based on the study, it is not possible to confirm or refute the hypothesis about causal relations between the program implementation and a change in labor productivity for several reasons.

First, as a result of descriptive analysis, it is shown that the labor productivity in test samples that have implemented program is growing, but labor productivity is also growing for some control samples of employees for whom no program have been implemented. For program 3, the growth rates of labor productivity in the test and control samples are comparable and approximately the same before and after the program implementation, the growth was about $2 \%$ in both samples. Based on this, a false conclusion can be made about the ineffectiveness of the tested programs.

Secondly, the acceptance or refutation of this hypothesis would be erroneous, since the initial sample have a significant range of variation, and some employees in the test group during the program were forced to take a sick leave for health reasons. Therefore, in its

current form, the employees sample could not be relevant, and the data for calculating labor efficiency are not comparable due to the difference in the starting point for the program implementation for individual employees.

Thirdly, the growth (decrease) in labor productivity as a result of the program implementation could be due to other factors of an economic, social, political and other nature, and it is not possible to estimate the net contribution of the factor of the program taken to this growth. The method of descriptive analysis does not allow isolating the share of variation in labor productivity due to motivation factors as a result of ongoing program.

Since the samples of employees before and after programs implementation have the same composition, they are dependent, related. Let's test the hypothesis about the equality of the means for two dependent samples based on the paired $t$-test:

$$
t=|\bar{m}| \sqrt{\frac{n \cdot d f}{\sum_{i} m_{i}^{2}-n \bar{m}^{2}}}
$$

where $m_{i}$-difference between pairs of compared values of two data samples ( $m_{i}=x_{i}-y_{i}$, $x_{i}$-value of the growth rate for labor productivity before the implementation of the program, $y_{i}$-value of the growth rate for labor productivity after the program implementation); $n$ is the sample size; $d f=n-1$-degrees of freedom for the $t$-test.

That is we test the hypotheses about a statistically significant difference (at the significance level $\alpha=0.05$ ) in the growth rate of labor productivity before and after the programs implementation for the treatment and control samples. The results of evaluating of the observed $t$-values are shown in Table 3.

Table 3. Observed $t$-values.


${ }^{*}$ statistically significant difference between samples before and after the program implementation at the significance level $\alpha=0.05$.

The results showed a significant difference between the average growth rates of labor productivity (hence, the samples of employees) only in the treatment groups for the first and second interventions. The other samples differ slightly. Statistical tests for a significant difference between the employees sample as a result of the programs implementation do not allow determine of their effectiveness.

Therefore, to test the initial hypothesis, we further use other methods.

# 4.1.2. Results of Difference-in-Difference Method Application 

We apply the difference-in-differences method by estimating the parameters of Equation (1) from [41]. We assess six samples of employees: treatment and control groups to test three programs.

First, we build tables for the average values of labor productivity rates for different programs to evaluate the partial expected effect from their implementation, using the difference-in-difference method, Table 4.

To model the true partial impact of the program on the labor productivity level, we build an econometric model with a dummy variable that takes into account employees who apply the program and do not apply. For each of the three programs, we construct econometric models of changes in labor productivity in different subsamples (treatment and control) of the following type:

$$
Y_{\text {after }}-Y_{\text {before }}=l_{0}+l_{1} D+e
$$

where $Y_{\text {after }}$-value of the labor productivity growth rate after the program implementation; $Y_{\text {before }}$-value of the labor productivity growth rate before the program implementation; $D$-dummy variable, takes the value 1 if the employee belongs to the treatment sample; $I_{0}$-a free regression coefficient, reflects the change in labor productivity for employees for whom the program is not implemented:

$$
I_{0}=Y_{\text {control, after }}-Y_{\text {control, before }}
$$

where $Y_{\text {control }}$-values of the labor productivity growth rate for employees for which the program is not implemented; $I_{1}$-regression coefficient, shows the expected partial effect of the program for employees for whom the program is implemented and not implemented:

$$
I_{1}=\left(Y_{\text {treatment,after }}-Y_{\text {treatment, before }}\right)-\left(Y_{\text {control, after }}-Y_{\text {control, before }}\right)
$$

$Y_{\text {treatment }}$-values of the labor productivity growth rate for employees for which the program is implemented.

The identification of models is carried out on the basis of the classical LSM, the simulation results are presented in Table 5.

Table 4. Difference-in-difference calculations for programs 1-3 (indicators are measured in \%).


Table 5. Estimated parameters for model (1).


[^0]
[^0]:    * statistically significant parameter for $p<0.05$.

An analysis of the simulation results shows that in the model for sample 1, the parameter with a dummy variable is statistically significant and its value coincides with the value obtained in Table 2, and reflects the possible effect of labor productivity growth for the entire given sample in the context of the total use of program 1. At the same time, in the model for sample 1, the free regression coefficient is statistically insignificant. Model 2 as a whole cannot be the basis for justifying the decision on program 2, since this model is generally inadequate, that is, for a group of employees in the second sample, the causal relations between the program implementation and the labor productivity growth is not justified. Model 3 has a statistically insignificant parameter with a dummy variable and, in general, does not reflect the positive effect of the implementation of program 3 on labor productivity growth.

At the same time, it is necessary to note the nature of the constructed models. They are descriptive of the program implementation and their impact in the medium term, but all of them have a rather weak predictive ability and the description of changes in the level of labor productivity as a result of program implementation can hardly be explained by these models. Their main disadvantage is that the variable $Y_{\text {before }}$ can be correlated with the variable $D$, which biases the parameters estimates in the model (1) and makes it inapplicable for analysis.

On the other hand, the program implementation is more economically attractive for employees with low labor productivity values. For such employees, labor efficiency indicators grow faster than for employees with higher initial levels of labor productivity. This also depends in part on time factors. Therefore, in model (1) regression to the mean, there may be problems with the interpretation of the results for such samples.

Thus, based on the results of the analysis of the constructed models, it is impossible to unambiguously judge the effectiveness of the tested program.

In order to neutralize model (1) errors, we form a model in the following specification:

$$
Y_{\text {after }}-Y_{\text {before }}=l_{0}+l_{1} D+l_{2} Y_{\text {before }}+e
$$

This model includes a control variable for regression to the mean [41]. The coefficient of the dummy variable in this model shows whether the program affects the change in the labor productivity for given initial indicators. If the parameter is statistically significant, then with the program implementation with low initial values of the growth rate, labor productivity improves more than without an program with the same low initial values of the growth rate of labor productivity. This difference implies the true effect of the program implementation.

The results of numerical experiments with model (2) are presented in Table 6.
Table 6. Estimated parameters for model (2).


* statistically significant parameter for $p<0.05$.

Analysis of the identification results of model (2) shows that all models have a high level of explanatory power, so the coefficients of determination for all samples are quite

high. In all models, the parameters at the variable $Y_{\text {before }}$ are statistically significant and actually explain the following.

If the parameter at the variable $D$ were statistically significant, then the following assumption could be made regarding the hypothesis being tested. The true effect of the intervention (in this case, intervention 1 to introduce a partial remote work) in the sample 1 is quite effective, since in the test subsample there are employees with low initial labor productivity values that are very different from the average labor productivity values for the control subsample. Therefore, the effect of the program implementation for such employees would be higher than the effect of refusing to use this program. Thus, for a sample 1, the hypothesis of causal relations between the program 1 use and the increase in labor productivity could be accepted as correct. And the use of this program in teams with low values of labor efficiency would be economically feasible. In addition, in model (2), built on subsample 1, the parameter with a dummy variable is statistically significant. Therefore, the conclusion about the advisability of introducing program to switch to a partial remote work is logical.

In models (2) built on samples 2 and 3, the parameter with a dummy variable is not statistically significant. Therefore, such considerations would be premature. The test and control subgroups in these samples are more statistically homogeneous and are characterized by average values of labor productivity growth, as well as small variations in this indicator both before and after the implementation of measures. The effect of the introduction of activities 2 and 3 in samples of workers is less noticeable in the control subgroups of workers. In general, for samples 2 and 3, program 2 and 3 do not bring the required results and do not contribute to the growth of labor productivity in the whole sample. In addition, in model (2) for sample 3, the regression coefficient with a dummy variable is below zero, which means the opposite effect from the program implementation under conditions of its total application.

In a model (2), we made an attempt to neutralize the shortcomings of a model (1) by introducing a variable on the right side of the equation as a control variable for regression to the mean that is, taking into account the differences in employees in the initial levels of labor productivity. As a result of evaluating the models for different samples of employees, it was found that the regression coefficients for the variable have negative and rather large statistically significant values, and the coefficients for the variable for samples 2 and 3 do not differ significantly from zero. This means that after taking into account the average level of initial labor productivity, the dummy variable introducing interventions 2 and 3 in the whole sample of 2 and 3 employees (including the experimental and control groups) has no explanatory power. This result, in turn, can be interpreted as the fact that the implementation of program 2 and program 3 in general does not have a significant impact on labor productivity.

However, when choosing program 1 as a management decision aimed at increasing the productivity of personnel, it must be borne in mind that, being generally effective, this program will give the greatest effect to those employees who have rather low initial levels of productivity labor. Thus, the partial impact of the program 1 is empirically substantiated.

# 4.2. Assessment of the Total Effect of the Programs, Bayesian Network Design 

At the third stage of the technology, the design and study of the Bayesian network is carried out. Bayesian networks are directed acyclic graphs on random variables with Markovian properties. The importance of Bayesian networks is that one can trace the influence of one variable over another through causal chains.

Consider the problem of determining direct and indirect factors that affect labor productivity. Based on the theory of the firm, we a priori compose the following architecture of the Bayesian network, Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Bayesian network of factors influencing on labor productivity. Network variable notation: $x_{1}$-tested program M1, $\ldots$, M3; $x_{2}$-social capital (an index); $x_{3}$-motiation (an index); $x_{4}$-innovativeness (an index); $x_{5}$-individual labor productivity.

This network architecture is a causal relationship between a set of factors that characterize human and social capital, employee motivation, innovativeness, management decisions (tested programs) and labor efficiency. A meaningful analysis of the influencing mechanisms is presented in [11], and a study related to experimental studies and assessment of the impact of social capital and innovation is discussed in detail in the work [3].
$x_{5}$-labor productivity. The Markovian property is that direct causes for We will be interested in how the program (managerial decision) M1, ..., M3 implementation-the factor $x_{1}$ will affect the factor a factor $x_{5}$ informationally block all other vertices of the graph, except for those that are direct or indirect consequences of $x_{5}$. That is, all information about the factor contained in the network variables, except for the consequence vertices of $x_{5}$, is completely contained in its direct vertices.

We will use the concept of intervention (do operator) introduced by J. Pearl [1] in order to obtain a joint probability distribution of network variables when fixing, assigning to a variable a certain value corresponding to one of the three programs $d o\left(x_{1}=x_{0}\right)$, where $x_{0}= \begin{cases}1, & \text { if program implemented, } \\ 0, & \text { otherwise. }\end{cases}$
It is required to find out how the distribution of the variable will change depending on the implemented management decision (program). Based on the concept of the do operator, we formulate a definition of causality $[2,28]$.

Definition 1. A vertex $x_{i}$ is a reason for $x_{j}$, if there are at least two values of $a, b, a \neq b$, so:

$$
p\left(x_{j} \mid d o\left(x_{i}=a\right)\right) \neq p\left(x_{j} \mid d o\left(x_{i}=b\right)\right)
$$

That is, the factor $x_{i}$ is the reason for $x_{j}$, if during the implementation of interventions $x_{i}$ (perhaps virtually) the probabilistic nature of $x_{j}$.

Using the concept of intervention will determine the overall effect of the the intervention $x_{1}$ on labor productivity $x_{5}$. To do this, we represent the Bayesian network analytically as a system of structural equations, when each vertex (except for exogenous ones) is associated with the regression equation of this vertex over all its direct vertices. Next, we determine the coefficient of the total action $x_{1}$ on $x_{5}$ based on the following theorem [42-44].

Theorem 1. The coefficient of the total effect of the action $x_{i}$ on $x_{j}$ is equal to the sum of the products of the regression coefficients along all paths leading from $x_{i}$ to $x_{j}$ :

$$
k_{x_{i}, x_{j}}=\sum_{x_{i_{1}}, \ldots, x_{i_{j}}} k_{x_{i_{1}}, x_{i_{2}}} \cdot \ldots \cdot k_{x_{i_{j-1}}, x_{i_{j}}}
$$

Consider the paths (sequences) of arrows leading from $x_{1}$ to $x_{5}$. Each cause-and-effect pair in the diagram determines the coefficient for the corresponding arrow-the effect of the direct cause. We have five paths from vertex $x_{1}$ to vertex $x_{5}$ :

- $\mathrm{I}-x_{1} \rightarrow x_{2} \rightarrow x_{4} \rightarrow x_{5}$;
- II— $x_{1} \rightarrow x_{2} \rightarrow x_{3} \rightarrow x_{5}$;
- III— $x_{1} \rightarrow x_{2} \rightarrow x_{3} \rightarrow x_{4} \rightarrow x_{5}$;
- IV— $x_{1} \rightarrow x_{3} \rightarrow x_{5}$;
- $\mathrm{V}-x_{1} \rightarrow x_{3} \rightarrow x_{4} \rightarrow x_{5}$.

We introduce the notation for the coefficients $k$ as shown in Figure 2. Let's write the Bayesian network as a system of equations:

$$
\begin{gathered}
x_{2}=a_{1} x_{1}+\varepsilon_{2} \\
x_{3}=b_{1} x_{1}+b_{2} x_{2}+\varepsilon_{3} \\
x_{4}=c_{1} x_{2}+c_{2} x_{3}+\varepsilon_{4} \\
x_{5}=d_{1} x_{3}+d_{2} x_{4}+\varepsilon_{5}
\end{gathered}
$$

Let's do the transformations. Substitute (5) into (6):

$$
x_{3}=b x_{1}+b_{2}\left(a_{1} x_{1}+\varepsilon_{2}\right)+\varepsilon_{3}=b_{1} x_{1}+a_{1} b_{2} x_{1}+\varepsilon^{\prime}{ }_{3}
$$

Next, we substitute (10) and (5) into (8):

$$
x_{4}=c_{1}\left(a_{1} x_{1}+\varepsilon_{2}\right)+c_{2}\left(b_{1} x_{1}+a_{1} b_{2} x_{1}+\varepsilon^{\prime}{ }_{3}\right)+\varepsilon_{4}=a_{1} c_{1} x_{1}+b_{2} c_{2} x_{1}+a_{1} b_{2} c_{2} x_{1}+\varepsilon^{\prime}{ }_{4}
$$

The final substitution of (11) and (10) in (9) is as:

$$
\begin{aligned}
& x_{5}=d_{1}\left(b_{1} x_{1}+a_{1} b_{2} x_{1}+\varepsilon^{\prime}\right)+d_{2}\left(a_{1} c_{1} x_{1}+b_{2} c_{2} x_{1}+a_{1} b_{2} c_{2} x_{1}+\varepsilon^{\prime}\right)+\varepsilon_{5}= \\
& =b_{1} d_{1} x_{1}+a_{1} b_{2} d_{1} x_{1}+a_{1} c_{1} d_{2} x_{1}+b_{1} c_{2} d_{2} x_{1}+a_{1} b_{2} c_{2} d_{2} x_{1}+\varepsilon^{\prime}
\end{aligned}
$$

where $\varepsilon^{\prime}$ is a linear combination of errors $\varepsilon_{1}, \ldots, \varepsilon_{5}$.
The coefficient of the total effect of the action on is equal to the sum of the products of the regression coefficients along all five paths $\mathrm{I}-\mathrm{V}$ leading from vertex $x_{1}$ to vertex $x_{5}$ :

$$
k=b_{1} d_{1}+a_{1} b_{2} d_{1}+a_{1} c_{1} d_{2}+b_{1} c_{2} d_{2}+a_{1} b_{2} c_{2} d_{2}
$$

Causal chains in the Bayesian network represent the transmission mechanism from the factor $x_{1}$ to $x_{5}$, and the coefficient $k$ is a quantitative expression of this mechanism. The coefficient of the total effect of the action evaluates the result of the impact on the labor productivity of the tested management decision (programs M1, ..., M3), analyzing the chains from $x_{1}$ to $x_{5}$. That is, from the inclusion (application) of the program, we have a clear understanding of the process of formation of cause-and-effect relations leading from $x_{1}$ to $x_{5}$. Based on this analysis, the following conclusions are formed:

- different management decisions M1, ..., M3 are compared according to their total effect of the action on labor productivity and the one that has the greatest effect is identified;
- within network, based on the ranking of chains according to the contribution of their influence on the total effect coefficient, and within each chain, the exact contribution of each of the variables to the resulting indicator $x_{5}$ is determined.
Based on the initial data on control factors-the programs implementation, the data obtained from the results of the survey, for an additional assessment of social capital, innovation and motivation of employees, as well as an objective calculation of individual labor productivity over experimental and control samples (details of the methods and algorithms of this study are given in [3,4,24]), estimates of the parameters of models (5)-(8) were calculated, Table 7.

Table 7. Model (5)-(8) parameter estimates for different programs.


${ }^{\text {a }}$ significant parameterfor $p<0.05$.
The results of the assessment of the total effect of the programs M1, $\ldots$, M3 action as well as the effects of the action along all paths leading from $x_{1}$ to $x_{5}$, are presented in Table 8.

Table 8. Assessing the total effect of interventions on labor productivity for different programs.


The obtained results demonstrate that the highest total effect under the conditions of many factors (under their control) affecting labor productivity is the program associated with the rating system for employees and using bonuses, the second largest effect is the program aimed at employee training, the program about partial remote mode of employees has the lowest effect. These results are different from the results of comparing programs obtained on the basis of an assessment of their partial effect on labor productivity (Section 3). To understand the reasons for this discrepancy, we visualize the joint distributions of factors in the form of 3d-diagrams, Figures 3 and 4, and also compare the individual chains (paths) of the network according to the degree of their contribution to the total program effect.

Chain I $\left(x_{1} \rightarrow x_{2} \rightarrow x_{4} \rightarrow x_{5}\right)$ of the network during the program M2 implementation makes the greatest contribution to the total effect on labor productivity. This path includes social capital and employee innovation. At the same time, it is obvious that the employees in the experimental group under the conditions of the implementation of the program, labor productivity and its growth depend on the levels of social capital and innovation. Figure 3b shows that the program M2 implementation (M2:1) contributes to the growth of social capital and innovation, and through them affects labor productivity. Employees with high social capital indices and innovation have higher labor productivity. At the same time, this relation is less noticeable among employees in the control group. This can be explained not by the direct, but by the indirect impact of thisprogram on labor productivity, that is, the rating of employees and their bonuses depending on their place in the rating helps to stimulate employees to develop new ideas, increase institutional trust (to the company's management) and, as a result, increase the effectiveness of their activities. It should also be noted that this chain of connections in the network works for workers with high initial levels of labor productivity (Figure 3a-c). Thus, the introduction of this program M2 into practice is more appropriate for more efficient employees.

![img-2.jpeg](img-2.jpeg)

Figure 3. 3d maps of the dependence of labor productivity (LP) on social capital (SC) and innovativeness (In): (a) under the conditions of the program M1 implementation, for the treatment group (M1:1) and the control group (M1:0); (b) under the conditions of the program M2 implementation, for the treatment group (M2:1) and the control group (M2:0); (c) under the conditions of the program M3 implementation, for the treatment group (M3:1) and the control group (M3:0).

The first program M1, aimed at introducing a partial remote mode of operation, has two chains—II $\left(x_{1} \rightarrow x_{2} \rightarrow x_{3} \rightarrow x_{5}\right)$ and III $\left(x_{1} \rightarrow x_{2} \rightarrow x_{3} \rightarrow x_{4} \rightarrow x_{5}\right)$ with the greatest contribution to the total effect. These chains involve motivation as a factor that has an indirect influence between the implementation of this program and the growth of labor productivity. This is also confirmed by the diagrams in Figure 4.

So for employees from the control group (M1:1), Figure 4a, those with the highest social capital and motivation indices have the highest values of labor productivity. For them, it is important to obtain a certain freedom in planning and implementing their labor functions, which contributes to the intensification of their work, and therefore their effectiveness. The program M1 implementation is advisable for employees with average levels of labor productivity.

When implementing the program M3, the chain of the network passing through the top-social capital, has the greatest contribution. This program-internships in leading companies is most appropriate to implement with a group of employees who have high communication skills (Figures 3c and 4c), are creative and can transplant the experience of other companies who are ready to take certain risks when implementing their new projects.

The identification of such employees is an additional task that can be solved on the basis of additional expert information.
![img-3.jpeg](img-3.jpeg)

Figure 4. 3d-maps of the dependence of labor productivity (LP) on social capital (SC) and motivation (M): (a) under the program M1 implementation, for the treatment group (M1:1) and the control group (M1:0); (b) under the program M2 implementation, for the treatment group (M2:1) and the control group (M2:0); (c) under the program M3 implementation of the activity M3, for the treatment group (M3:1) and the control group (M3:0).

We point out that for the final choice of programs implemented, the criterion of its effectiveness when compared with competing ones is the possibility of complete and sustainable achievement of the final goals-the growth of resource efficiency, in this case, labor productivity at minimal cost for its implementation.

The problem set in this paper to substantiate the causal relations between the program implementation and the labor productivity growth has been completed. It is shown that there is such causality, but the program implementation should be differentiated depending on the initial levels of employee efficiency, their innovativeness, motivation and social capital.

# 5. Conclusions 

The problem of labor productivity management of the company's employees has been considered. A meaningful analysis of approaches, methods and tools for analyzing projects aimed at increasing resource efficiency (including labor productivity), expanding sales markets, and increasing the efficiency of companies' operating activities has been carried out. We have tested the hypothesis that implementation of the special program affects labor

productivity that is there is a causal relations between the program implementation and labor productivity growth under the influence of explicit and hidden factors of the labor productivity efficiency.

The new research technology has been developed based on the integration of the theory of causal Bayesian networks, method of statistical randomized experiments and the difference-in-difference method for evaluating the effeciency of competing programs and its effect on the labor productivity growth. The difference between the proposed technology and others is that it ensures determination the synergistic effect of the action of the cause (program) on the effect-labor productivity in condition of hidden factors.

The causal Bayesian network helps to calculate the consequences of various programs aimed at increasing labor productivity. On the example of a simple Bayesian network consisting of five vertices, it has been shown that the total effect of the program is due to both the mutual arrangement of factors and their impact on each other. This can be used to select and implement a management decision with the highest effect of action.

We have evaluated three programs: (1) partial remote work; (2) rating system for employees and using bonuses; (3) internships in leading companies, which intended for labor productivity growth and increase company efficiency.

We conducted a randomized controlled experiment in which its results were determined solely by the action of the program and did not depend on other factors. For this, we used a randomization procedure. Based on the difference-in-difference method, we have shown that the first program focused on the partial remote work of the company's employees has a causal relations with the labor productivity growth. At the same time, it was noted that these program give the greatest effect to those employees who have rather low initial values of labor productivity.

Then we formed a structural model of the object based on the Bayesian network to take into account the hidden factors that affect labor productivity, including innovation, motivation and social capital as important determinants of labor productivity. As a result of the Bayesian network analysis we have revealed that the highest total effect under hidden factors (under their control) affecting labor productivity is the program associated with the ratings for employees and introduction employee bonuses. It was also noted that the program implementation should be differentiated depending on the initial levels of employees' efficiency, their innovativeness, motivation and social capital.

The proposed research technology was tested in catering company. However, the technology is universal and can be implemented by other companies, regardless of their size and type of economic activity. The practical significance of the investigation is that it results could contribute to the labor productivity growth over uncertainty of the external and internal factors and provide the companies sustainable development and its profitability growth.

Funding: This research received no external funding.
Data Availability Statement: Data sharing not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
