# Article 

## A Stochastic Model Approach for Copper Heap Leaching through Bayesian Networks

Manuel Saldaña ${ }^{1, *}$ (D), Javier González ${ }^{2}$, Ricardo I. Jeldres ${ }^{3}$ (D), Ángelo Villegas ${ }^{2}$, Jonathan Castillo ${ }^{4}$ (D), Gonzalo Quezada ${ }^{5}$ (D) and Norman Toro ${ }^{2,6, *}$<br>1 Departamento de Ingeniería de Sistemas y Computación, Facultad de Ingeniería y Ciencias Geológicas, Universidad Católica del Norte, 1270709 Antofagasta, Chile<br>2 Departamento de Ingeniería Metalúrgica y Minas, Facultad de Ingeniería y Ciencias Geológicas, Universidad Católica del Norte, 1270709 Antofagasta, Chile; javier.gonzalez@ucn.cl (J.G.); avf009@alumnos.ucn.cl (Á.V.)<br>3 Departamento de Ingeniería Química y Procesos de Minerales, Facultad de Ingeniería, Universidad de Antofagasta, 1270300 Antofagasta, Chile; ricardo.jeldres@uantof.cl<br>4 Departamento de Ingeniería en Metalurgia, Universidad de Atacama, 1531772 Copiapó, Chile; jonathan.castillo@uda.cl<br>5 Water Research Center for Agriculture and Mining (CRHIAM), University of Concepción, 4030000 Concepción, Chile; gonzaloqe@gmail.com<br>6 Department of Mining and Civil Engineering, Polytechnic University of Cartagena, 30203 Cartagena, Spain<br>* Correspondence: manuel.saldana@ucn.cl (M.S.); ntoro@ucn.cl (N.T.)

Received: 14 October 2019; Accepted: 4 November 2019; Published: 7 November 2019


#### Abstract

Multivariate analytical models are quite successful in explaining one or more response variables, based on one or more independent variables. However, they do not reflect the connections of conditional dependence between the variables that explain the model. Otherwise, due to their qualitative and quantitative nature, Bayesian networks allow us to easily visualize the probabilistic relationships between variables of interest, as well as make inferences as a prediction of specific evidence (partial or impartial), diagnosis and decision-making. The current work develops stochastic modeling of the leaching phase in piles by generating a Bayesian network that describes the ore recovery with independent variables, after analyzing the uncertainty of the response to the sensitization of the input variables. These models allow us to recognize the relations of dependence and causality between the sampled variables and can estimate the output against the lack of evidence. The network setting shows that the variables that have the most significant impact on recovery are the time, the heap height and the superficial velocity of the leaching flow, while the validation is given by the low measurements of the error statistics and the normality test of residuals. Finally, probabilistic networks are unique tools to determine and internalize the risk or uncertainty present in the input variables, due to their ability to generate estimates of recovery based upon partial knowledge of the operational variables.


Keywords: Bayesian networks; uncertainty analysis; stochastic process modelling; heap leaching

## 1. Introduction

Copper mining is a constantly growing industry [1], and in countries like Chile, this industry represents $10 \%$ of the gross national product (GNP) [2], while approximately 19.7 million tons are produced annually worldwide [3]. Among the copper ores on the planet, the vast majority correspond to sulfured minerals, and a smaller amount to oxidized minerals [4], which is why flotation techniques and smelting processes are used to process these minerals, and to a lesser extent hydrometallurgical techniques [5]. However, flotation techniques generate a large amount of waste, resulting in tailings and the generation of acid drainage by the oxidation of minerals with a high presence of pyrite [4,6].

On the other hand, pyrometallurgical processes produce high emissions of sulfur dioxide $\left(\mathrm{SO}_{2}\right)$, which together with $\mathrm{NO}_{\mathrm{x}}$ and $\mathrm{CO}_{2}$, can cause major problems, such as acid rain and increased local pollution [5]. So, hydrometallurgy is a good alternative to process both oxidized minerals and sulfurized minerals, since it is more environmentally friendly [5,7,8].

During the last 50 years, heap leaching processes were a very attractive technological option for the treatment of low grade minerals, allowing the economic exploitation of marginal deposits, often in remote locations in many parts of the world [9]. They are applied to previously crushed minerals in crushers, where the copper $(\mathrm{Cu})$ present in the mineralized rock is extracted by the mixture between water and leaching agents [10]. This process is performed in leaching piles, where its typical height is between 4 to 10 m , although in some cases they can reach 18 m [11]. It can be applied for oxidized copper ores of low to medium grades $(0.3-0.7 \%)$ as well as secondary copper sulfides. In heap leaching, larger sizes generally range between 10 and 40 mm , where sizes less than 6 mm are unacceptable, because they affect the permeability of the pile, especially if there are clayey minerals that result in a greater obstruction of heaps over time, due to swelling and gradual decrepitation. The leaching solution is distributed on top of the heap by sprinklers or drip emitters and then flows down through the heap under gravity. The volumetric flows of the typical solution vary between 4 and $20 \mathrm{~L} /\left(\mathrm{h} \times \mathrm{m}^{2}\right)$ [9]. Finally, cupric ions $\left(\mathrm{Cu}^{2+}\right)$ are obtained together with other ions of elements dissolved in the pregnant liquid solution (PLS), which ions all advance to the subsequent stage of solvent extraction [12].

In the present investigation, the modeling of the copper heap leaching process is proposed using a stochastic approach through bayesian networks (BN), which considers both the distributions of the independent variables and the conditioned distributions of the response variable to the independent variables, in addition to the conditional relationships between the independent variables. The generation of this type of model allows investigation of the effects of the variables or input factors on one or more output variables through intentional changes, which are used to identify the conditions of the process and its components that affect the extraction behavior, in order to identify the configuration of factors that have a greater conditional dependence on the response variable. On the other hand, the modeling of this type of processes, in addition to being efficient in predicting the response variable, is robust to the lack of evidence; that is, they have the capacity to estimate recovery under conditions of lack of evidence or lack of knowledge, or more independent variables.

# 2. Materials and Methods 

### 2.1. Machine Learning

Machine Learning is related to the creation of computer programs or algorithms which automatically improve and/or adapt their performance through experience. Machine learning has many things in common with other domains, such as statistics and probability theory (understanding of the phenomena that have generated the data), data mining (finding patterns in data that are understandable to people) and cognitive sciences (human learning aims to understand the mechanisms that underlie the various learning behaviors exhibited by people, such as concept learning, skill acquisition, strategy change, etc.) [13]. The objective of machine learning is to devise learning algorithms that automatically learn without human intervention or assistance, generating methods by which the computer creates its own program based on the examples we provide [14].

As part of the exploration and understanding of a process, ways of quantifying the events associated with its variables are sought. Depending on their complexity, these events could be associated with a single variable or multiple of them, and often follow an orderly, sequential evolution that could converge in one or more patterns that reflect, and sometimes determine, their behavior.

# 2.2. Data-Based Modeling in Mineral Processing 

Machine learning and artificial intelligence techniques have a growing presence and impact in a wide variety of research fields. McCoy and Auret [15] develop a review of the state of machine learning applications in mineral processing. Data-based modeling methods in the mineral processing literature are frequently applied as "soft sensors" for the prediction of variables measured infrequently (or difficult to measure), based on variables measured frequently [16,17,18]. Some applications include the prediction of indicators of the grinding phase, determining the chemical properties that have a greater impact on the milling capacity indices by configuring an artificial neural network [19,20] or a regression of support vectors [21], Martin et al. [22]. On the other hand, they apply Random Forest (RF) for the prediction of the Hardgrove Grindability Index (HGI) based on a wide range of Kentucky coal samples.

Modeling applications to predict mill performance indicators based on process measurements, include the use of multivariate statistical methods such as partial least squares (PLS) and radial-based neural networks (RBF), demonstrating that the density of mill pulp and ball loading volume can be estimated reliably from different operational characteristics [23]. Ahmadzadeh and Lundberg [24], on the other hand, developed a method that predicts the remaining lifespan of a mill's lining without stopping it, by modeling an artificial neural network capable of recognizing the complex relationships between inputs and departures. The results obtained by Ahmadzadeh and Lundberg [24] show a remarkably high degree of correlation between the input and output variables. The performance of the neural network model is very consistent for the data used for training and testing.

Other studies show the application of machine learning techniques to the prediction of flotation performance indicators based on process measurements. Jahedsaravani et al. [25] analyzed and modeled the relationship between flotation process conditions and foam characteristics through the use of neural networks. Similar to the study developed by Jahedsaravani et al., Massinaei and Doostmohammadi [26] studied the relationship between gas dispersion in a flotation cell and flotation speed using artificial neural network (ANN) techniques and statistics (nonlinear regression). Nakhaei et al. [27], investigates the prognosis of metallurgical performance (grade and recovery) of the flotation column of the pilot plant using artificial neural networks (ANN) and multivariable nonlinear regression (MNLR).

However, most of these neural networks applied to the modeling of mineral processes have to be relatively small, often with only a hidden layer due to computer or data limitations. Recent developments in the design and training of deep and complex neural networks have not been demonstrated in the literature on mineral processing. Comparisons between neural networks and methods such as linear or nonlinear regression have not confirmed a significant benefit of neural networks compared to simpler methods [26,27].

Wang et al. [28], developed another work that implements an interesting adaptive modeling application, where multiple neural networks are used to predict foam properties based on the measurements of input or feed parameters. As machine learning techniques become increasingly accessible as part of software packages, data-based modeling applications are likely to become more common and make use of more advanced techniques and analysis. In particular, techniques for modeling the dynamics of complex processes may be of interest, since most applications currently assume that observations are independent [15].

### 2.3. Bayesian Networks

The Bayesian networks model is a phenomenon through a set of variables with dependency relationships between them. In this model, Bayesian inference can estimate the subsequent probability of the unknown variables based on the known variables. These models can have different applications for classification, prediction, diagnosis, etc. In addition, they can give interesting information, as to how the domain variables are related, which can sometimes be interpreted as cause-effect relationships. A Bayesian network is therefore a device of representation destined to organize knowledge about a

particular situation in a coherent whole. The Bayesian network is a graphical modeling tool to specify probability distributions [29].

Bayesian networks provide a graphical representation for a set of random variables and for the relationships between them. The structure of the network makes it possible to specify the joint probability function of these variables as the product of conditional probability functions, usually simpler ones. BN are probabilistic, multivariate models that relate a set of random variables through a directed graph that explicitly indicates causal influence and this is thanks to its probability update engine, Bayes' Theorem [30]. Bayesian networks are an extremely useful tool in estimating probabilities to new evidence. A Bayesian network is, therefore, a type of causal network.

Then, defining the fundamentals of Bayesian networks, given a vector of random variables $X:\left(x_{1}, \ldots, x_{n}\right)$, a joint probability measure is defined (Equation (1)):

$$
\operatorname{Pr}: \operatorname{dom}(X) \rightarrow[0,1]
$$

where $\operatorname{dom}(X)=\operatorname{dom}\left(x_{1}\right) \times \ldots \times \operatorname{dom}\left(x_{n}\right)$. If the joint probability is known, it is possible to calculate any probability on the variables $x_{1}, \ldots, x_{n}$. Then the following propositions are defined: Rule of total probability (Equation (2)) and rule of marginalization (Equation (3)).

$$
\begin{gathered}
\operatorname{Pr}(X \mid Y)=\frac{\operatorname{Pr}(X, Y)}{\operatorname{Pr}(Y)} \\
\operatorname{Pr}(A)=\sum_{i \in I} \operatorname{Pr}\left(A, B_{i}\right), B_{i} \text { disjoint, } \bigcup_{i \in I} B_{i}=\Omega
\end{gathered}
$$

Then the theorem shown in Equation (2) shows a simple but powerful relationship between conditional probabilities, which will be the basis of Bayesian network theory.

$$
\operatorname{Pr}(C=c \mid X=x)=\frac{\operatorname{Pr}(X=x \mid C=c) \times \operatorname{Pr}(C=c)}{\operatorname{Pr}(X=x)}
$$

where,

$$
\begin{gathered}
\operatorname{Pr}(C=c \mid X=x): \text { Later } \\
\operatorname{Pr}(X=x \mid C=c): \text { verisimilitude } \\
\operatorname{Pr}(C=c): \text { Prior } \\
\operatorname{Pr}(X=x): \text { Evidence }
\end{gathered}
$$

Now, considering the independence between the factors, the two random variables are independent if and only if the conditions of Equation (9) are met, or the condition of Equation (10) is met if the existence of evidence is considered.

$$
\begin{gathered}
\forall x, y \operatorname{Pr}(X=x, Y=y)=\operatorname{Pr}(X=x) \times \operatorname{Pr}(Y=y) \\
\operatorname{Pr}(X, Y \mid E)=\operatorname{Pr}(X \mid E) \times \operatorname{Pr}(Y \mid E)
\end{gathered}
$$

If, on the contrary, $X$ and $Y$ are independent, $\operatorname{Pr}(X \mid Y)=\operatorname{Pr}(X)$ o $\operatorname{Pr}(X \mid Y, E)=\operatorname{Pr}(X \mid E)$. The independence between variables allows a reduction in the complexity of the joint probability function, and instead of modeling a single function, we separate them into simpler parts.

Then, assuming that you have the data of the form $\left(X_{1}, \ldots, X_{2}, C\right)$, where $C$ is the class variable, and you are looking to predict the value of the class $\left(x_{1}, \ldots, x_{2}\right)$, a probabilistic approach will assign the most probable class (Equation (11)), which is:

$$
\tilde{c}=\arg \max _{c} \operatorname{Pr}\left(C=c \mid X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)
$$

Then, if Bayes' Theorem is applied, the following is obtained (Equation (12)):

$$
\tilde{c}=\arg \max _{c} \frac{\operatorname{Pr}\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n} \mid C=c\right) \times \operatorname{Pr}(C=c)}{\operatorname{Pr}\left(X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)}
$$

However, for the purpose of estimating the output, the expected value of mineral recovery through the product between the outputs and their conditional probabilities is considered, as shown in Equation (13).

$$
E[Y(t) \mid X]=\sum_{i=1}^{n} y_{i}(t) \times P\left(y_{i}(t) \mid X\right), \forall t
$$

where $X$ represents the set of independent variables influencing the response variable in different degrees, and $y_{i}$ corresponds to a possible state of recovery in a given time $t$.

If the existence of certain independent variables is unknown, the expected value of the probability of each value of the response variable is considered conditional on the evidence of the $\mathrm{n}-\mathrm{k}$ independent variables known and the conditional distributions of the $k$ independent variables unknown, as shown in Equation (14).

$$
E[Y(t)] X_{n-k}]=\sum_{i=1}^{n} y_{i}(t) \times P\left(y_{i} \mid X_{n-k} \wedge E\left[x_{1}, x_{2}, \ldots, x_{k}\right]\right), \forall t
$$

It should be noted that the expected value of the k variables whose evidence is unknown may or may not be conditioned on the other $n-1$ independent variables, which is the $n_{k}$ variables whose evidence is known and the conditional distributions of the $k-1$ variables whose evidence is unknown.

# 2.4. Uncertainty Analysis 

The uncertainty analysis (UA) corresponds to determine the uncertainty in the output variables as a result of the uncertainty in the input variables [31]. The UA is generally performed using the probability theory [32], where uncertainty is represented by the probability distribution functions (PDFs), and which can be done in four steps. First, the type of PDF and the magnitude of the uncertainty for each input variable is determined. In other words, the uncertainty of entry is characterized. Then, for each input variable, a sample of the PDF is generated. Third, the values of the output variables are determined for each element of the sample. Finally, the results are analyzed using graphs, descriptive statistics and statistical tests to characterize the behavior of the output variables.

When the input variables have epistemic uncertainties, the uncertainty can be represented by a uniform distribution. Design and operation variables present this type of uncertainty. When the input variables have stochastic uncertainties, the normal distribution is generally used to represent this type of uncertainty [33].

## 3. Results and Discussion

The results are ordered into three subsections: The results of the UA, which address the UA in the response variable at 30, 60 and 90 days of leaching; the modeling results of the copper recovery from the heap leaching process through the Bayesian networks, in addition to the conditional relationships between the independent variables and the recovery, and the conditional dependence between the independent variables, together with the degree of strength of the dependencies (reflected in the arcs that connect the nodes of the network). Finally, the effectiveness of the Bayesian network is studied as a tool to model the productive process of heap leaching, by calculating the indicators of goodness of adjustment mean absolute deviation (MAD), mean squared error (MSE) and mean absolute percentage error (MAPE), together with tests of the normality of the residues when evaluating the value expected response to changes in input variables and ignorance of one or more independent variables.

# 3.1. Analysis of Uncertainty 

Equation (14) indicates that copper recovery depends on the operational variables' sampled time, particle radius, pile height, particle porosity, surface velocity of the leaching flow and effective diffusivity of the solute through the pores of the particle.

A good distribution function to represent epistemic uncertainties is the uniform PDF, taking the values of $x_{1}, x_{2}, \ldots, x_{n}$ as the central tendency values of the parameters $p_{1}, p_{2}, \ldots, p_{n}$, respectively. The sensitivity analysis was analyzed three times for the occasions of 30,60 and 90 days of leaching. The results are shown in Figures 1-3, respectively.

Figures 1-3 show that the leaching time affects the kinetic uncertainty of the battery leaching phase. Histograms show that uncertainty in the input variables produces greater uncertainty in recovery after 30 days compared to uncertainty after 60 days, in addition to greater uncertainty after 60 days compared to sampling after 90 days leaching.

The normal probability plot (Figure 1b) indicates that when the leaching time is equal to 30 days, the recovery presents a normal PDF with a standard deviation of 1.75 and an average of $54.89 \%$ recovery, while when the leaching time is 60 days (Figure 2b), the recovery presents a normal PDF with an average of $57.53 \%$ and a deviation of 1.03 .
![img-0.jpeg](img-0.jpeg)

Figure 1. Uncertainly analysis at 30 days of leaching, copper recovery distribution (a) and normal probability plot (b).
![img-1.jpeg](img-1.jpeg)

Figure 2. Uncertainly analysis at 60 days of leaching, copper recovery distribution (a) and normal probability plot (b).

![img-2.jpeg](img-2.jpeg)

Figure 3. Uncertainly analysis at 90 days of leaching, copper recovery distribution (a) and normal probability plot (b).

On the other hand, the normal probability plot indicates that when the leaching time is equal to 90 days, the recovery has a tail that moves away from normal behavior. These results show that the Bayesian network can estimate the expected recovery of copper from heap leaching, considering a wide range of the uncertainties of independent variables. The change in the recovery behavior as a function of the time factor is because the recovery tends to present asymptotic behavior at high values of the time factor. It is evident that regardless of the value of the other independent variables, the deviation of the long-term recovery is less than at lower levels of the time factor.

# 3.2. Bayesian Network Modeling 

The analysis of the behavior or dynamics of battery leaching involves a complex and multidimensional system in an environment, in which there is regularly uncertainty and the lack or absence of certain risk factors involved in the problem. The modeling made possible through probability distributions amid uncertainties, provided by the BN-based models, becomes appropriate to model the recovery of copper, considering that it allows one to deduce hypotheses and establish the relationships between the explanatory factors of the response variable. However, risk is a changing fact when it comes to time (among other aspects), and modeling through BNs satisfies this logic, since it stimulates stochastic processes [34].

The parameters' leaching time, pile height, particle size, surface velocity of the leaching flow through the bed, effective diffusivity of the solute within the pores of the particle and the porosity of particle, were considered for the generation of the Bayesian network, information obtained from operational data from a mine in the Antofagasta region, Chile (data provided by the national mining company, Antofagasta, Chile, ENAMI, by its acronym in Spanish). The minimum, maximum and average values of the variables considered are presented in Table 1.

Table 1. Summary of minimum, average and maximum values of the operational data.


Developing the Bayesian network in GeNIe software (version 2.3) [35], the a priori structure of the network is given by Figure 4, where it is possible to appreciate that copper recovery is conditionally

dependent upon all the variables considered in the sampling. Looking at the arches of the Bayesian network of Figure 4, they have a different thickness, indicating the force of influence between the nodes of the network. Strength of influence is always calculated from the total conditional probability (TCP) of the child node, and essentially expresses some form of distance between the various conditional probability distributions over the child node conditional on the states of the parent node; that is, the greater the thickness of the arc, the greater the conditional dependence between the nodes. The distance function that is used for the generation of the Bayesian network is the Euclidean function.
![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network for copper heap leaching process.
Once the network structure is identified, the probabilistic and computational calculations make the inference of the quantitative parameters of the model, with a possible interaction of the theoretical knowledge of the experts on the risk scenario that involves a specific problem, with the establishment of relationships that theoretically influence the response variable. Therefore, for the construction of analytical models using BN, prior subjective knowledge is required, which is also associated with the fact that the algebra of Bayesian analysis is more complex than classical analysis, especially in multidimensional problems.

Analyzing the network of Figure 4, it is necessary that the class variable "Copper recovery" is conditionally dependent on the independent variables considered in the sampling. However, for the set of sampled values, there is no conditional dependence between the variables that explains the answer. Then, incorporating a priori knowledge of the dynamics of the process handled by the authors (dependence relationships), the expected recovery following a stochastic approach should be modeled as shown in Figure 5.

Developing an analysis of influences of the nodes that show conditional dependence, prior to the establishment of relationships generated based on a priori knowledge managed by the system, the arcs that have a greater conditional dependence are time-copper recovery, heap height-recovery and superficial velocity of the leaching flow-recovery. Analyzing the Bayesian network outputs, the increase in the height and size of the typical commercial heap has not occurred simply as a result of economic efficiency but is also a function of the available surface area [9]. One of the factors that most influences the kinetics of the process is the percolation rate, which is directly related to the height of the pile and the permeability of the pile [12]. While time is a factor that greatly influences in copper recovery percentage from conventional leaching stacks, the current laws have made other technologies not profitable, since they require greater comminution or temperature [12].

For this reason, it works with long operating times, which may vary depending on the material to be worked and the recovery standards that the mining company is looking for.

![img-4.jpeg](img-4.jpeg)

Figure 5. Bayesian network for copper heap leaching process incorporating a priori knowledge.
On the other hand, the factors that have a marginal effect are the effective diffusivity of the solute within the pores of the particle and the size and porosity of particle. The influence force is always calculated from the total conditional probability (TCP) of the secondary node and essentially expresses some form of distance between the various distributions of conditional probability over the secondary node, conditioned on the states of the primary node.

The total probability distributions identified by the Bayesian network are presented in Figure 6, where it can be seen that the stack height and particle size factors tend to be distributed normally (Figure 6a,b), while the surface velocity of the leaching flow (Figure 6c), the effective diffusivity of the solute through the pores of the particle (Figure 6d) and the porosity of the particle (Figure 6e) can be adjusted to a uniform continuous distribution. It is assumed that the time factor, as it is an operational sampling data, is uniform discrete, with a priori known values.
![img-5.jpeg](img-5.jpeg)

Figure 6. Cont.

![img-6.jpeg](img-6.jpeg)
(e)

Figure 6. Distributions of independent variables high pile (a), particle size (b), surface velocity of the leaching flow through the bed (c), effective diffusivity of the solute within the pores of the particle (d) y porosity of the particle (e).

Then, the effectiveness of the Bayesian network is evaluated to estimate copper recovery considering a priori knowledge of the sampled parameters. The ability to predict the recovery is based on the knowledge of the n variables of interest, or the expected value of the response variable is calculated based on the underlying distributions of the independent variables unknown, while the dynamics of the recovery based on each of the independent variables is presented in Figure 7.
![img-7.jpeg](img-7.jpeg)

Figure 7. Cont.

![img-8.jpeg](img-8.jpeg)

Figure 7. Copper recovery based on leaching time (a), particle size (b), pile high (c), superficial velocity of lixiviant flow (d), effective diffusivity of the solute within particle pores (e) and porosity of particle (f).

# 3.3. Bayesian Network Validation 

Finally, the effectiveness of the Bayesian network is evaluated to estimate copper recovery considering a priori knowledge of the parameters considered in its generation. The ability to predict recovery is based upon the knowledge of the n variables of interest, otherwise the expected value of the response variable is calculated conditioned on the underlying distributions of the independent variables, which in turn are conditioned on the evidence of the other independent variables already known. Then, the independent variables are sensitized, in order to estimate the expected recovery of ore, according to the stochastic model shown in Equation (14).

Estimating the recovery of copper through the Bayesian network adjusted with operational data from a copper mine considering as evidence the n independent variables, and analyzing the contrast between the outputs of the network and the operational results, as shown in Figure 8a, The Bayesian network presents a good fit to the operational data, and the goodness of fit statistics shown in Table 2 validate it.
![img-9.jpeg](img-9.jpeg)

Figure 8. Operational fit curve versus Bayesian networks outputs (a) and Normal Probability Graph $E[Y(t)] X_{n} \mid(\mathbf{b})$

Table 2. Statistics of the analytical model of leaching of marine nodules.


On the other hand, Figure 8b shows that the assumption of the normality of the residues obtained from the contrast between the expected value of the network output and the operational data is reached, making the p -value of the test greater than the level of significance ( $\mathrm{p}>0.05$ ), which indicates that the mathematical model is relatively accurate in representing the experimental design, although some points away from the line imply a distribution with outliers.

Analyzing the outputs of Bayesian networks over time and the variables defined by the nodes that represent the other independent variables, the expected value of the response is based on the evidence and the conditional distribution of the variable whose evidence is unknown. The expected recovery value obtained by the network is adjusted to the operational data, which is validated with the statistic p ( $\mathrm{p}>0.05$ ), as shown in Figure 9.
![img-10.jpeg](img-10.jpeg)

Figure 9. Normal Probability Graph $E\left[Y(t) \mid X_{n-1} \wedge E[x]\right], x$ : particle porosity (a), velocity of lixiviant flow (b), particle size (c), effective diffusivity of solute within particle pores (d) and porosity of particle (e).

The analysis of the residues between the experimental values and the expected recovery values generated by the network that excludes the knowledge of the porosity variables (Figure 9a) and the superficial velocity of the leaching flow (Figure 9b) do not present a normal adjustment, which together

with high values of the goodness of fit indicators presented in Table 3 ratify the importance of both variables in the response.

Table 3. Statistics of the analytical model of leaching of marine nodules.


In the opposite case, the residuals of the variables particle size (Figure 9c), effective diffusivity of the solute within the pores of the particle (Figure 9d) and porosity of the particle (Figure 9e) tend to have a normal adjustment ( $p=0.05$ ), indicating that these variables do not have a significant impact on recovery.

Following the example of Saldaña et al. [10], the generated stochastic model can be incorporated into a simulation framework that can quantify the benefits derived from the incorporation of probabilistic models in estimating the expected value of mineral recovery, or it could have the potential to include it in a system of support for decision making in the mining industry, as presented in Saldaña et al. [36].

# 4. Conclusions and Future Works 

### 4.1. Conclusions

Probabilistic networks have become unique tools to determine and internalize the risk or uncertainty present in the input variables, and the importance of these is due to the ability to provide data for monitoring, as new information is added or removed from its structure, and also, for incorporate various hypotheses. Therefore, one of the main benefits of the Bayesian approach is the ability to incorporate prior information to quantify uncertainties and verify the legitimacy of the propositions.

Based on the above, it can be concluded that the behavior of the classification algorithms based on Bayesian networks presents satisfactory results in general terms, since the error obtained in the classification is minimal, which is validated by the normalization statistics of adjustment and the normality of the residuals distribution.

The construction of the Bayesian network model to analyze the dynamics of the leaching process has the potential to contribute to:

1. Identifying the dependency relationships between independent variables and the response variable, in addition to dependency relationships between independent variables.
2. Determining the variables that contribute most to explain the variability of the response.
3. Assimilating quantitative knowledge in terms of the frequency of the occurrence of a given event (or level of recovery), using the parameters obtained by the BN, which will allow the identification of recurrent scenarios.
4. The generation of copper recovery estimates based on partial knowledge of the operational variables considered in the study.

Finally, the variables that have a greater conditional dependence on the response variable are the time (mainly), the height of the stack and the superficial velocity of the leaching flow, while the variables that have a less significant impact are particle size, the porosity of the particle and the effective diffusivity of the solute within the pores of the particle.

# 4.2. Future Works 

To further advance the operational investigation of leaching processes through a stochastic approach, sensitization of the variables of interest through a global sensitivity analysis are being considered. In addition, there is the incorporation into the stochastic model of the variability of the feeding of the productive process, and this will be through the generation of geostatistical models that relate the mineralogical content of the mine with the planning of extraction.

Author Contributions: M.S. and N.T. contributed in the methodology, conceptualization and modeling; J.G. and Á.V. investigation, writing review and editing; J.C. data curation and formal analysis and R.I.J. and G.Q. contributed with supervision and validation.
Funding: This research received no external funding.
Acknowledgments: Gonzalo Quezada and Ricardo Jeldres thank the Centro CRHIAM Project Conicyt/Fondap/15130015.
Conflicts of Interest: The authors declare no conflict of interest.
