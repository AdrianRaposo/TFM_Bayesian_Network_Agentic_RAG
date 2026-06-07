# Article 

## Probabilistic Forecasting of Drought Events Using Markov Chain- and Bayesian Network-Based Models: A Case Study of an Andean Regulated River Basin

Alex Avilés ${ }^{1, *}$, Rolando Célleri ${ }^{2}$, Abel Solera ${ }^{3}$ and Javier Paredes ${ }^{3}$<br>1 Departamento de Recursos Hídricos y Ciencias Ambientales \& Facultad de Ciencias Químicas, Universidad de Cuenca, Víctor Manuel Albornoz y los Cerezos, Campus Balzay, Cuenca 10207, Ecuador<br>2 Departamento de Recursos Hídricos y Ciencias Ambientales \& Facultad de Ciencias Agropecuarias, Universidad de Cuenca, Víctor Manuel Albornoz y los Cerezos, Campus Balzay, Cuenca 10207, Ecuador; rcelleri@gmail.com<br>3 Institute of Water and Environmental Engineering, Universitat Politècnica de València, Camino de Vera s/n, Valencia 46022, Spain; asolera@upvnet.upv.es (A.S.); iparedea@hma.upv.es (J.P.)<br>* Correspondence: alex.aviles@ucuenca.edu.ec; Tel.: +593-74-051-000 (ext. 4494)<br>Academic Editors: Paolo Reggiani and Ezio Todini<br>Received: 3 October 2015; Accepted: 11 January 2016; Published: 23 January 2016


#### Abstract

The scarcity of water resources in mountain areas can distort normal water application patterns with among other effects, a negative impact on water supply and river ecosystems. Knowing the probability of droughts might help to optimize a priori the planning and management of the water resources in general and of the Andean watersheds in particular. This study compares Markov chain- (MC) and Bayesian network- (BN) based models in drought forecasting using a recently developed drought index with respect to their capability to characterize different drought severity states. The copula functions were used to solve the BNs and the ranked probability skill score (RPSS) to evaluate the performance of the models. Monthly rainfall and streamflow data of the Chulco River basin, located in Southern Ecuador, were used to assess the performance of both approaches. Global evaluation results revealed that the MC-based models predict better wet and dry periods, and BN-based models generate slightly more accurately forecasts of the most severe droughts. However, evaluation of monthly results reveals that, for each month of the hydrological year, either the MC- or BN-based model provides better forecasts. The presented approach could be of assistance to water managers to ensure that timely decision-making on drought response is undertaken.


Keywords: probabilistic drought forecasting; drought index; Markov chains; Bayesian networks; copulas; Andean watersheds

## 1. Introduction

Droughts are recognized as an environmental disaster, the consequence of a reduction in precipitation over an extended period of time [1], negatively affecting agriculture, domestic water supply and economic growth [2], and in some cases even altering the functioning of natural ecosystems [3]. Droughts are especially important in regions where economic activities are highly dependent on water resources [4], such as in mountain regions which traditionally provide water resources and services to local communities and lowland residents [5]. For example, the Andean basins, which have been identified as excellent providers of water for multiple uses [6,7], could be affected by droughts and climate change, putting the water supply at risk and augmenting the vulnerability of the basin's water resources systems and eco-services [8-11]. The increasing tendency

of water shortage is a concern of water managers [11], wrestling with questions such as which drought indicator [12] and threshold of the indicators should be used to qualify the drought status. In fact, drought characterization requires indicators that are generally applicable, but specific enough to capture the type of drought relevant to the region and the variables of interest [10]. Droughts may occur at different moments in the hydrological year, with the consequence that hydrologic variables might experience quite different levels of drought, complicating the overall assessment of the drought status [13]. Furthermore, droughts can be the result of a succession of water shortages over different periods of time [14]. Consequently, there is a need to assess the drought status using indices based on multiple variables monitored during different time windows. The present study uses the drought index (DI) developed by Avilés et al. [15], which is based on water-related variables of different window-sizes in the hydrologic year, enabling the capturing of the drought status for short, medium and long periods. The main advantages of this index are its flexibility in aggregating basin water-related variables and capability of selectively using variables depending on the available hydro-meteorological data.

The characterization of droughts and its reliable prediction would help water managers to make the decisions that make water supplies safe and reliable, and that are risk-adverse. To this end water managers need the instruments that enable them to mimic the water supply and demand systems using adequate models that also address uncertainties and vulnerabilities, and help to prioritize risks [16]. A major restriction in the formulation of strategies addressing the availability of water is the forecast of droughts [17]. It is generally accepted that the reliable forecast of drought events plays an important role in the development of adequate strategies for the planning and distribution of water resources [13,18]. Several methodologies to forecast drought saw daylight in recent years, and Mishra and Singh [19] describe some of these approaches. Regression analysis [20,21,22] is a commonly used method; however, it has the limitation of assuming linearity between predictor and predictand, which makes the technique less suitable for long-lead forecasting [19]. Time series models [23,24,25,26,27] are advantageous since they provide a framework for the identification, estimation and the diagnostic check for model development [23], but they are also, as the regression models, linear. Neural networks [28,29,30] are nonlinear models having the capacity to discover patterns from data and estimate any complex functional relationship with high accuracy. However, major disadvantages of neural networks are their black-box nature and computational burden [19]. The above-listed models provide a deterministic prediction of the drought status, and does not consider the uncertainty associated with the forecast [31]. This aspect can be handled by probabilistic models, which forecast in a quantitative way droughts and the associated uncertainty [32]. A variety of probabilistic models for drought forecasting has been developed [13,15,18,31,33,34,35,36,37,38,39,40,41], but not that many calculate the conditional probability if there are multiple events, such as the Markov chains and Bayesian networks. Those approaches generate probabilistic forecasts of future droughts in function of earlier drought conditions. According to the probability conditional theory are the models based on MC most common for drought forecasting [15,33,34,35,36], while the BN-based models are more sophisticated. The latter have not been widely used for the probabilistic forecasting of drought events, notwithstanding they seem to have the ability of better forecasting droughts [13,18].

A BN is a graphical model that encodes the joint probability for a large set of random variables. They offer a natural way of describing the conditional dependencies of dependent variables in time, such as drought indices (DIs) with probabilities [42]. Since droughts are slowly evolving phenomena, strong temporal autocorrelation among DIs is expected [14], and, therefore, they can be expressed within a BN [18,43]. A considerable effort is required to solve BNs, a task that can be simplified using copula functions. Those functions are capable of combining several variables with different levels of correlation and dependence structures [13]. The two most frequently used copulas families are Elliptic and Archimedean copulas [44]; a commonly used list of copulas families can be found in the literature [45,46,47]. In this study, two types of each family, Elliptic and Archimedean are tested. To enhance the confidentiality of the forecasts, we used the RPSS for the verification of forecasts, which provides a measure of the accuracy of the forecast in terms of assigned probabilities [48,49].

This study uses the Drought Index (DI) developed on the basis of rainfall and streamflow data of the Chulco River basin in Southern Ecuador, as described in Aviles et al. [15]. In this study, the first-order Markov chain and the second-order Markov chain stochastic models were used to predict the frequency of monthly droughts. The aim of the present study is to compare MC-based models, a more classical approach, with BN-based models, a novel technique, for forecasting future droughts given knowledge of earlier droughts, and to assess the benefits of BNs over the first and second order MCs. Section 2 of the manuscript describes the methodology, including a brief description of the developed DI, the forecast models and the method used to verify forecasts. The third section of the paper gives a snapshot of the study area, while the fourth and fifth sections respectively present the results and conclusions.

# 2. Materials and Methods 

### 2.1. Case Study

Data of the Andean Chulco mountain basin, which is situated in Southern Ecuador at an altitude of 3200-4300 m.a.s.l (Figure 1), were used to examine the performance of the MC and BN model approaches. Most of the basin area is covered by páramo (tussock grass). The Andean hilly páramo region consists of glacier-formed valleys and plains with a large variety of lakes, peat bogs and wet grasslands, intermingled with shrubland and low-statured montane forest patches [7]. The study basin is one of the few regulated basins in the region, with the El Labrado reservoir situated at the basin outlet. The reservoir stores water for urban, agricultural and industrial uses, and power generation. The basin is strategic because it is one of the few multi-purpose water resources systems in Southern Ecuador that benefits local and regional ecology and economies. From this point of view, research results might be useful for water managers working in similar environmental conditions.
![img-0.jpeg](img-0.jpeg)

Figure 1. Location of the Chulco river basin in the Paute river basin.

For development of the DI, monthly time series of basin average rainfall and stored volume in the El Labrado reservoir, for the period 1971 to 2010 were collected from the National Institute of Meteorology and Hydrology of Ecuador (INAMHI) and the Council Basin River Machangara (CBRM). Figure 2 shows the variation of the monthly average of rainfall and water volume, two time series

of the variables. Similar to the study by Avilés et al. [15], to capture short, medium and large term droughts, time windows of $1,3,6,9$ and 12 months were selected for the generation of ten time series with varying time scales, respectively five time series of the total rainfall (PR1, PR3, PR6, PR9 and PR12) in mm, and five time series of the water volume entering the reservoir (VS1, VS3, VS6, VS9 and VS12) in $\mathrm{hm}^{3}$. The monthly seasonality is accounted by the division of the ten time series for each month. All data was standardized to jointly considered variables with different units.
![img-1.jpeg](img-1.jpeg)

Figure 2. Monthly average of the time series of rainfall and water volume for the period 1971-2010.

# 2.2. Drought Index 

The DI used herein is derived subjecting available water-related variables of the study area to Principal Components Analysis (PCA), calculating the correlation matrices between time series of $r$ available hydro-meteorological datasets, yielding the eigenvalues and eigenvectors. The eigenvectors establish the relationship between the principal components (PCs) and the original information, as expressed by Avilés et al. [15]:

$$
\mathrm{Z}=\mathrm{D} \times \mathrm{E}
$$

where $Z$ is the $o \times r$ matrix of PCs, o the number of observations, $D$ the $o \times r$ matrix of the standardized original information, and E the $\mathrm{r} \times \mathrm{r}$ matrix of eigenvectors. DI is the first principal component (PC1), normalized by its standard deviation. Hence we have:

$$
\mathrm{DI}_{\mathrm{i}, \mathrm{k}}=\frac{\mathrm{Z}_{\mathrm{i}, 1, \mathrm{k}}}{\sigma_{\mathrm{k}}}
$$

where $\mathrm{DI}_{\mathrm{i}, \mathrm{k}}$ is the DI value for the kth month in the ith year, $\mathrm{Z}_{\mathrm{i}, 1, \mathrm{k}}$ the PC1 for the kth month in the ith year, and $\sigma_{\mathrm{k}}$ the sample standard deviation of $\mathrm{Z}_{\mathrm{i}, 1, \mathrm{k}}$ of all years. Once the DI values for each month and year were calculated, they were chronological rearranged into a single time series.

DI is a standardized index (SI) capable of capturing the anomalies from the average moisture condition of a basin as a function of the available information of water-related variables [13,14]. Any phenomenon that can be quantified continuously, such as the drought index, is likely treated as a discrete variable by categorizing the time series considering thresholds for each state of drought. Hence, DI, being a normal score satisfying the null hypothesis of the Kolmogorov-Smirnov test [50] for normality, was divided into categories to characterize the state of drought, using the same thresholds as the World Meteorological Organization [51]. Based on that, the following drought categories were derived: DI $>0=$ category 0 (no drought); $-1<\mathrm{DI} \leqslant 0=$ category 1 (mild drought); $\mathrm{DI} \leqslant-1=$ category 2 (moderate, severe and extreme drought). The three states of category 2 were taken as a single state called drought. This new time series of categorical values (variable Y) are the inputs of the Markov

chain models, and the time series of cumulative normal distribution function of the DI values are the inputs of the Bayesian network models. The calibration and validation of the models was performed applying the leave-one-out cross-validation procedure.

# 2.3. Markov Chain Models 

The behavior of a Markov chain (MC) is governed by a set of probabilities of transitions that specify probabilities for the system being in each of its possible states during the next time period [52]. A mth order Markov chain is one where the transition probabilities depend on the states in the previous $m$ time periods. The Markovian property to the $m^{\text {th }}$ order Markov chain is (for more details see Wilks [52]):

$$
P\left(Y_{t n} \mid Y_{t n-1}, Y_{t n-2}, Y_{t n-3}, \ldots, Y_{1}\right)=P\left(Y_{t n} \mid Y_{t n-1}, Y_{t n-2}, \ldots, Y_{t n-m}\right)
$$

Considering a first-order Markov chain (MCFO), i.e., $\mathrm{m}=1$, the transition probabilities provide the probabilistic forecast for the status of the next step based on the current status, applying the following equation:

$$
\mathrm{p}_{\mathrm{ij}}=\mathrm{P}\left(\mathrm{Y}_{\mathrm{tn}}=\mathrm{j} \mid \mathrm{Y}_{\mathrm{tn}-1}=\mathrm{i}\right)
$$

where $\mathrm{p}_{\mathrm{ij}}$ represents the transition probability that $\mathrm{Y}_{\mathrm{tn}}$ is equal to category j given $\mathrm{Y}_{\mathrm{tn}-1}$ is equal to category i. The estimate of the transition probabilities $\left(\hat{\mathrm{p}}_{\mathrm{ij}}\right)$ can be calculated to account for the conditional relative frequencies of transitions $\left(\mathrm{f}_{\mathrm{ij}}\right)$ :

$$
\hat{\mathrm{p}}_{\mathrm{ij}}=\frac{\mathrm{f}_{\mathrm{ij}}}{\sum_{\mathrm{j}} \mathrm{f}_{\mathrm{ij}}} \mathrm{i}, \mathrm{j}=1, \ldots, \mathrm{~s}
$$

where $f_{i j}$ is the frequency that $Y$ is equal to the category $i$ at time $t_{n-1}$ and equal to category $j$ at the time $t_{n}$. The value of $s$ is the number of states of the system. The numerator represents the number of transitions of category i to category j , and the denominator stands for the sum of the number of transitions of category i to any other category.

If $\mathrm{m}=2$, we would have a second-order Markov chain (MCSO), where the transition probabilities depend on the states of the current and the previous time period, providing the probabilistic forecast of the status of the next time step. The transition probabilities are calculated as follows:

$$
\mathrm{p}_{\mathrm{hij}}=\operatorname{Pr}\left\{\mathrm{Y}_{\mathrm{tn}}=\mathrm{j} \mid \mathrm{Y}_{\mathrm{tn}-1}=\mathrm{i}, \mathrm{Y}_{\mathrm{tn}-2}=\mathrm{h}\right\}
$$

where $\mathrm{p}_{\mathrm{hij}}$ represent the transition probability that $\mathrm{Y}_{\mathrm{tn}}$ is equal to category j , given that $\mathrm{Y}_{\mathrm{tn}-1}$ is equal to the category i and $\mathrm{Y}_{\mathrm{tn}-2}$ equal to the category h . The transition probability estimates $\left(\hat{\mathrm{p}}_{\mathrm{hij}}\right)$ are obtained from conditional relative frequencies of transition counts $\left(\mathrm{f}_{\mathrm{hij}}\right)$ :

$$
\hat{\mathrm{p}}_{\mathrm{hij}}=\frac{\mathrm{f}_{\mathrm{hij}}}{\sum_{\mathrm{j}} \mathrm{f}_{\mathrm{hij}}} \mathrm{~h}, \mathrm{i}, \mathrm{j}=1, \ldots, \mathrm{~s}
$$

where the numerator is the number of transitions of category $h$ at time $t_{n-2}$, category $i$ at time $t_{n-1}$, and category $j$ at the time $t_{n}$, and the denominator is the sum of the number of transitions categories $h, i$ to any other category. For this condition, the probability of the drought status of the next time period depends on the status of the two previous time periods.

### 2.4. Bayesian Network Models

Heckerman [42] claims that a Bayesian network for a set of variables $X=\{X 1, \ldots, X n\}$ consists of: (1) a network structure (NS) that encodes a set of conditional independence assertions about variables in X; and (2) a set P of local probability distributions associated with each variable. Together, these components define the joint probability distribution for X . The NS is a directed acyclic graph (DAG),

consisting of the sequence of events or random variables with direct ordering, such as time evolving events [18,53]. Given the NS, the joint probability distribution for $X$, is given by:

$$
P(X)=\prod_{i=1}^{n} P(X i \mid P a i)
$$

where Xi is both the variable and its corresponding node, and Pai are the parents of node Xi in NS. The probabilistic information on the nodes stands for the influence of their parents in the graph on the node. For further details, the reader is referred to Heckerman [42].

Following a similar mathematical formulation as in Madadgar and Moradkhani [13,18], and given the set of variables $X$ is a unique time-evolving random variable (e.g., drought index), $X=\left\{X_{t 1}, \ldots, X_{t n}\right\}$, where the dependency ordering follows the temporal sequence and the parents of $X_{t i}$ is the set of all prior variables $\left(X_{t 1}, \ldots, X_{t i-1}\right)$, then Equation (8) can be expressed as:

$$
P\left(X_{t 1}, \ldots, X_{t n}\right)=\prod_{i=1}^{n} P\left(X_{t i} \mid X_{t 1}, \ldots ., X_{t i-1}\right)
$$

Equation (9) represents the chain rule in probability theory, which can be solved as:

$$
P\left(X_{t 1}, \ldots, X_{t n}\right)=P\left(X_{t n} \mid X_{t 1}, \ldots ., X_{t n-1}\right) P\left(X_{t 1}, \ldots ., X_{t n-1}\right)
$$

Reordering Equation (10), we obtain:

$$
P\left(X_{t n} \mid X_{t 1}, \ldots ., X_{t n-1}\right)=\frac{P\left(X_{t 1}, \ldots, X_{t n}\right)}{P\left(X_{t 1}, \ldots ., X_{t n-1}\right)}
$$

Equation (11) represents a BN-based model, where the conditional probabilities of the forecast variable $\left(\mathrm{X}_{\mathrm{tn}}\right)$ are calculated given the predictor variables $\left(\mathrm{X}_{\mathrm{t} 1}, \ldots, \mathrm{X}_{\mathrm{tn}-1}\right)$. The calculation of the joint probability distributions in the right-hand side of Equation (11) is a relatively cumbersome task, which can be considerably simplified using copula functions.

# 2.5. Copulas 

Copulas are functions that join multivariate distribution functions whose one-dimensional margins are uniform on the interval $[0,1][46]$. Accepting the mathematical definition of copulas in Yan [45], one obtains a random vector $\left(\mathrm{U}_{1}, \ldots, \mathrm{U}_{\mathrm{n}}\right)^{\mathrm{T}}$, where each margin $\mathrm{U}_{\mathrm{i}}, \mathrm{i}=1, \ldots, \mathrm{n}$, is a uniform random variable over the unit interval. Suppose the joint cumulative distribution function (CDF) of $\left(U_{1}, \ldots, U_{n}\right)^{\mathrm{T}}$, is as follows:

$$
C\left(U_{1}, \ldots, U_{n}\right)=P\left(U_{1} \leqslant u_{1}, \ldots, U_{n} \leqslant u_{n}\right)
$$

where the function $C$ is called a n-dimensional copula and CDF specifies the probabilities that the random quantity $X$ will not exceed particular values [52], i.e., $U(X)=U(X \leqslant x)$. On the other hand, Sklar's theorem [54] explains the role that copulas play in the relationship between multivariate distribution functions and their univariate margins [46]. The theorem states that a joint multivariate distribution functions $F\left(X_{1}, \ldots, X_{n}\right)$, for all $x$ in the domain of $F$, can be expressed by a $n$-dimensional copula, as follows $[13,44]$ :

$$
F\left(X_{1}, \ldots, X_{n}\right)=C\left\{U_{1}\left(X_{1}\right), \ldots, U_{n}\left(X_{n}\right)\right\}
$$

where $U_{i}\left(X_{i}\right)$ represents the ith univariate marginal distribution on the unit interval $[0,1]$ and $C$ is the cumulative copula distribution function that represents the multivariate dependence structure [55]. If $\mathrm{U}_{1}, \ldots, \mathrm{U}_{\mathrm{n}}$ are all continuous and C is unique [45], Equation (11) can be expressed as:

$$
P\left(X_{i n} \mid X_{t 1}, \ldots . ., X_{i n-1}\right)=\frac{C\left(U_{t 1}, \ldots, U_{i n}\right)}{C\left(U_{t 1}, \ldots, U_{i n-1}\right)}
$$

If $\mathrm{n}=2$ (dependence of first order), the conditional probabilities of the forecast variable $\left(\mathrm{X}_{\mathrm{t} 2}\right)$ are calculated given the predictor variable ( $\mathrm{X}_{\mathrm{t} 1}$ ), i.e., the next drought status is conditional to the current status. Similarly, if $n=3$ (dependence of second order), the conditional probabilities of the forecast variable $\left(X_{t 3}\right)$ are calculated given the predictor variables $\left(X_{t 1}, X_{t 2}\right)$, i.e., the next drought status is conditional to the current status and the status of a previous step. These cases could be called Bayesian networks of the first order (BNFO) and second order (BNSO), respectively. Thus, replacing $n=2$ and $n=3$ in Equation (14) leads to the following expressions:

$$
\begin{aligned}
P\left(X_{t 2} \mid X_{t 1}\right) & =\frac{C\left(U_{t 1}, U_{t 2}\right)}{U_{t 1}} \\
P\left(X_{t 3} \mid X_{t 1}, X_{t 2}\right) & =\frac{C\left(U_{t 1}, U_{t 2}, U_{t 3}\right)}{C\left(U_{t 1}, U_{t 2}\right)}
\end{aligned}
$$

To calculate the probability that DI in the next time step does not exceed the thresholds defined in Section 2.2, in which drought states are categorized as drought, mild drought, and non-drought, given the availability of the information for the current status for the BNFO model and the states of the current and previous time steps for the BNSO model, Equations (15) and (16) can be rewritten as:

$$
\begin{gathered}
P\left(X_{t 2} \leqslant x d_{s} \mid X_{t 1}\right)=\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2} \leqslant x d_{s}\right)\right]}{U\left(X_{t 1}\right)} \\
P\left(X_{t 3} \leqslant x d_{s} \mid X_{t 1}, X_{t 2}\right)=\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right), U\left(X_{t 3} \leqslant x d_{s}\right)\right]}{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right)\right]}
\end{gathered}
$$

where $x d_{s}$ is the drought index that causes a drought status according to the threshold defined in Section $2.2\left(\mathrm{xd}_{0}=0\right.$ and $\left.\mathrm{xd}_{1}=-1\right)$. Applying Equations (17) and (18), the probabilities of having a category 0 (no drought), i.e., $\mathrm{DI}>0$, will be equal to:

$$
\begin{gathered}
P\left(X_{t 2}>x d_{0} \mid X_{t 1}\right)=1-\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2} \leqslant 0\right)\right]}{U\left(X_{t 1}\right)} \\
P\left(X_{t 3}>x d_{0} \mid X_{t 1}, X_{t 2}\right)=1-\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right), U\left(X_{t 3} \leqslant 0\right)\right]}{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right)\right]}
\end{gathered}
$$

Analogously, the probabilities of having a category 1 (mild drought), i.e., $-1<\mathrm{DI} \leqslant 0$, can be formulated as:

$$
\begin{gathered}
P\left(x d_{1}<X_{t 2} \leqslant x d_{0} \mid X_{t 1}\right)=\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2} \leqslant 0\right)\right]}{U\left(X_{t 1}\right)}-\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2} \leqslant-1\right)\right]}{U\left(X_{t 1}\right)} \\
P\left(x d_{1}<X_{t 3} \leqslant x d_{0} \mid X_{t 1}, X_{t 2}\right)=\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right), U\left(X_{t 3} \leqslant 0\right)\right]}{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right)\right]}-\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right), U\left(X_{t 3} \leqslant-1\right)\right]}{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right)\right]}
\end{gathered}
$$

Finally, the probabilities of having a category 2 (drought), i.e., $\mathrm{DI} \leqslant-1$, can be expressed as:

$$
\begin{gathered}
P\left(X_{t 2} \leqslant x d_{1} \mid X_{t 1}\right)=\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2} \leqslant-1\right)\right]}{U\left(X_{t 1}\right)} \\
P\left(X_{t 3} \leqslant x d_{1} \mid X_{t 1}, X_{t 2}\right)=\frac{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right), U\left(X_{t 3} \leqslant-1\right)\right]}{C\left[U\left(X_{t 1}\right), U\left(X_{t 2}\right)\right]}
\end{gathered}
$$

# 2.6. Copulas Fitting 

The procedure for constructing joint distributions includes: (1) identifying marginal distributions on the unit interval $[0,1] ;(2)$ selecting suitable dependence structures; and (3) forming joint distributions [14]. The marginal distributions $\left(U_{i}\right)$ of step 1 can be derived when the DI values are transformed to a cumulative normal distribution function, in accordance with Section 2.2. Since droughts are slowly evolving phenomena, strong temporal autocorrelation among DI is expected [14]. Steps 2 and 3 consist in modeling the temporal dependence structure by fitting the copula functions given the marginal distribution.

Two elliptical copulas (normal and t) and two Archimedean copulas (Clayton and Frank) were tested in this study, as to define the most appropriate function for the joint distributions. The canonical maximum likelihood (CML) [56] method was applied for the estimation of the parameters in the copula functions, using the empirical cumulative distribution function of each marginal distribution (Ui) to transform the observations into pseudo-observations on the unit interval [0,1] [44]. The best fitted copula function was identified by the parametric bootstrap-based goodness-of-fit test [57], which consists in comparing a distance $(\Delta C)$ between the empirical copula $\left(C_{E}\right)$ and the estimated parametric copula $\left(C_{\theta}\right)$ function under the null hypothesis that $C_{E} \in C_{\theta}$. The latter is evaluated by the $p$ value; if the p value is greater than the significance level $\alpha$ the null hypothesis is accepted, conversely, the null hypothesis is rejected. $P$ values can be obtained via the Monte Carlo method embedded in a parametric bootstrapping procedure.

The Cramér-von-Mises statistic (S) [58] was applied on the group of copulas that are in agreement with the null hypothesis, as to derive the best alternative among the fitted copulas. In the group of copulas that are greater than the significance level, the smallest $S$ is chosen as the best copula function [13]. The expression of the statistic is as follows, where d is the sample size:

$$
S=\int \Delta C(U)^{2} d C(U)=\sum_{i=1}^{d}\left\{C_{E}\left(U_{i}\right)-C_{\theta}\left(U_{i}\right)\right\}^{2}
$$

### 2.7. Forecast Verification

The quality of the forecasts was assessed using the cross-validation procedure, whereby RPSS, despite being a skill score appropriate for the evaluation of probabilistic forecasts of categorical variables, was applied to verify the overall quality of the forecasts of both models. It is noticed here that the results of the Bayesian network model were divided by the categories before the forecast verification.

The ranked probability score (RPS) is a skill measurement that penalizes forecast errors in terms of the probability assigned to the events [59], and is based on the square error between the cumulative probabilities of forecasts and observations. This score is sensitive to distance, i.e., it includes a penalty for the forecasts that are further away of the observations. According to Wilks [52], RPS is defined as:

$$
\mathrm{RPS}=\sum_{\mathrm{m}=1}^{\mathrm{s}}(\mathrm{Ym}-\mathrm{Om})^{2}
$$

where Ym is the cumulative probabilities of forecasts, Om is the cumulative probabilities of observations $(\mathrm{Om})$ and s the number of event categories or states of the system. As RPS is seen as the probabilistic extension of the square error, a perfect forecast would have an RPS value equal to 0 and the worst forecasts would be very much different from zero.

For the assessment of the usefulness of forecasts, RPSS could be used, which refers to the relative accuracy of a set of forecasts with respect to some set of reference forecasts. In fact, RPSS can be interpreted as the percentage improvement over the reference forecast [52], and is computed as:

$$
\operatorname{RPSS}=1-\frac{\langle\mathrm{RPS}\rangle}{\left\langle\mathrm{RPS}_{\mathrm{Clim}}\right\rangle}
$$

where $\langle\mathrm{RPS}\rangle$ is the average of the RPS values for each forecast-observation record and $\left\langle\mathrm{RPS}_{\text {Clim }}\right\rangle$ the average of the RPS values computed with respectively the reference forecasts and observations. In this study, the reference forecast is the climatological relative frequencies of the predictand. $\mathrm{RPSS}=1$ means a $100 \%$ improvement over the reference forecasts, while, if RPSS is equal to 0 or less, there is no improvement over the reference forecast.

# 3. Results and Discussion 

### 3.1. Drought Index

Applying PCA for each month of the year, using information of the correlation matrices of the ten time series (PR1, PR3, PR6, PR9, PR12, VS1, VS3, VS6, VS9 and VS12), the eigenvalues and eigenvectors were obtained. Table 1 shows the eigenvalues and the explained variance of the PC1 for each month.

Table 1. Eigenvalues and explained variance of the PC1.


By means of Equations (1) and (2), and using information from the eigenvectors and the standardized original data, the DI values were derived for each month and rearranged in chronological order, forming the DI time series for the period 1971 to 2010. The DI values were converted into a cumulative normal distribution function that served as input for the Bayesian network models, while the Markov chain models require categorized time series of the DI according to the thresholds listed in Section 2.2. Table 2 lists the frequencies of each category (drought states) for the 480 months of the categorical time series, Figure 3 shows the time series of the DI, and Figure 4 depicts an example of the correlation between the time series of the DI of the months of July, August and September. The models were fitted using leave-one-out cross-validation, a procedure allowing an assessment of the accuracy of the forecast with respect to all events in the period 1971-2010.

Table 2. Frequency of drought state categories.


![img-2.jpeg](img-2.jpeg)

Figure 3. Time series of the DI (1971-2010).
![img-3.jpeg](img-3.jpeg)

Figure 4. Scatter plots of DI respectively between the months July-August, August-September and July-September for the period 1971-2010.

# 3.2. Markov Chain Models 

To take seasonality into account, the non-homogeneous model version of MC was used, i.e., transition probabilities were calculated for each month of the year, yielding twelve matrices of transition probabilities estimates for each model (MCFO and MCSO). These matrices enabled the derivation of probabilistic forecasts of the status of next month j, given the current status in month i by applying the MCFO model, and given the states in the current month i and previous month h applying the MCSO model. The transition probability matrix leaving the third year out in the cross-validation procedure for August (month with least rain) using the MCFO model is shown in Table 3, and the transition probability matrix for July-August applying the MCSO model is listed in Table 4. For example, if in August the drought status corresponds to category 1 (mild drought), then according to Table 3 the drought forecasting probabilities for the month of September are: $7 \%$ for category 0 (no drought), $86 \%$ for category 1 (mild drought) and $7 \%$ for category 2 (drought), the adding to $100 \%$. Similarly, the drought forecasting probabilities for September using the information in Table 4 when the states of July and August are category 0 (no-drought) are: $75 \%$ for category 0 (no drought), $25 \%$ for category 1 (mild drought), and $0 \%$ for category 2 (drought), adding to $100 \%$. In the absence of transitions between states, the transition probability for each state is likely equal to one divided by the number of categories, e.g., the states $0-2$ and $2-0$ in Table 4 have a probability of $33.33 \%$ for each category.

Table 3. Transition probability matrix of the MCFO model leaving the third year out in cross-validation for the month August.


Table 4. Transition probability matrix of the MCSO model leaving the third year out in cross-validation for the period July-August.


# 3.3. Bayesian Network Models 

The BN models consider seasonality, and copula fittings were developed for each month. For testing the null hypothesis, the significance level $\alpha$ was made equal to 0.05 , and the number of the bootstrap in the Monte Carlo method equal to 1000. For example, Tables 5 and 6 depict the $p$ values and the S-statistic of the BNFO and BNSO models for each month and the four types of copulas (normal, t, Clayton and Frank), leaving the third year out in the cross-validation. The four copula types were tested because of the symmetrical dependence between most monthly DI time series and the stronger dependence in the lower tail between few monthly time series of DI, as shown in Figure 4.

Table 5. $p$ value and S-statistic leaving the third year out in cross-validation for the BNFO model.


Table 6. $p$ value and S-statistic leaving the third year out in cross-validation for the BNSO model.


The shaded $p$ values represent the copulas that reject the null hypothesis and the shaded S-statistics highlight the copulas with the best fit for each month. The latter copulas were chosen to calculate the conditional probabilities of the drought status for next month given the drought status of the current month for the BNFO model and the current and previous drought states for the BNSO model, applying Equations (19)-(24). Equations (18), (20), (22) and (24) have bivariate copulas as a denominator; these are the same copulas with the best fit shown in Table 5. Figure 5 shows the probability distributions of the drought forecasting for the month of September given the drought index of the month of August for the BNFO model, leaving the third year out in the cross-validation. For example, if there is a DI of -1.65 in August corresponding to category 2 (drought), the probabilities drought forecasting for the month of September are: $0 \%$ for category 0 (no drought), $5 \%$ for category 1 (mild drought) and $95 \%$ for category 2 (drought). In a similar way, if there is a DI of 2.68 in August corresponding to a category 0 (no drought), the probabilities drought forecasting for the month September are: $50 \%$ for category 0 (no drought), $34 \%$ for category 1 (mild drought), and $16 \%$ for category 2 (drought). In brief, a low DI value in August leads to higher probabilities of severe droughts in September; conversely, high values of DI in August lead to low probabilities of drought in September. 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

# 3.4. Forecast Verification 

Cross-validation was used to evaluate the probabilistic forecasts. Forty RPS values were derived for each month, and each model applying the leave-one-out procedure and $\mathrm{RPS}_{\text {Clim }}$ was calculated on the basis of reference forecasts equal to climatological relative frequencies of the time series of categorical values of the DI. Considering the average of the RPS and $\mathrm{RPS}_{\text {Clim }}$ values for the entire time series, i.e., taking into account all states of drought (drought, mild drought and no-drought) and all months, and, using Equation (27) to calculate the RPSS values, the MCFO model performed better compared to the other models with the greatest value of improvement over the reference forecast equal to 0.29 , followed by the MCSO and BNFO models with values of RPSS equal to 0.21 and -0.05 (negative RPSS values mean that the reference forecasts are better that the tested model). Considering only the observed drought states (drought and mild drought), the BNFO model performed better with the greatest values of RPSS equal to 0.40 , followed by the BNSO and MCFO models with RPSS values equal to 0.33 and 0.19 , respectively. Even considering only the most severe drought status, the BNFO model yielded better results, with the greatest RPSS value equal to 0.44 , followed by the MCSO and BNSO models with RPSS values equal to 0.37 and 0.35 . These results indicate that, for the given case study, the MCFO model performed better for the probabilistic forecast of dry and wet periods, while, for the probabilistic forecast of dry periods, the BN-based models are a better option.

Table 7 depicts the assessment of the monthly drought forecasts, with, in the top section of the table, (a) the RPSS values of all observed states (drought, mild drought and no-drought), and, in the bottom section, (b) the RPSS values for mild drought and drought states. On the basis of the RPSS values in the top section (a) of Table 7, it can be concluded that the MCFO model produces better forecasts than the reference forecasts in the months January, February, March, May, June, September, October and November, while in the months of April, July and August the MCSO performed better. The RPSS values in the bottom section (b) of Table 7 reveal that the BNFO model produces better forecasts than the reference forecasts in the months January, February, April, May, June, October, November and December; the MCFO model performed better in March and September; and the MCSO model performs best in July and August.

Table 7. RPSS values of the monthly assessment of drought forecasts.


Whereas global assessment of drought forecasts permits evaluation of the overall performance of the models, the assessment of drought forecasts on a monthly basis might reveal which of the models perform best for a given month of the hydrologic year. For example, our study disclosed that the MC-based models perform better in predicting dry periods in specific months. Although a monthly scale was used for drought forecasting, findings are in agreement with the results obtained by Madadgar and Moradkhani [13]; drought forecasts using the BN-based models did not significantly differ from the forecast generated of other models. Those authors [18] also stated that the BN model in combination with copula functions is a useful procedure in the probabilistic forecasting of drought events.

# 4. Conclusions 

The performance of the MC- and BN-based models in drought forecasting was tested. Both conditional-based approaches offer the ability to derive probabilistic forecasts based on information of previous droughts. Copula functions were used to simplify the solution of the mathematical formulation of the Bayesian network, enabling the derivation of joint distribution functions. Employing a recently developed drought index, both modeling approaches were applied and tested using 40-year rainfall and streamflow data of the Chulco River basin, an Andean regulated river basin in Southern Ecuador. The leave-one-out cross-validation procedure was used for forecast verification. Results revealed that BN-based models were slightly better in forecasting severe drought events than the MC-based models; however, the monthly verification of forecasts suggests that the four models distinctively perform better for given drought categories in given months of the hydrological year. The tested approaches can be applied to other spatial and temporal scales, and serve other purposes such as simulation, characterization, classification and evaluation of drought events for decision-making. It is evident that monthly probabilistic forecasting will be instructive water managers in the development of appropriate mitigation measures.

Acknowledgments: This research was financially supported by the University of Cuenca through its Dirección de Investigación (DIUC) and the Empresa pública municipal de telecomunicaciones, agua potable, alcantarillado y saneamiento de Cuenca (ETAPA-Parque Nacional Cajas) via the projects "Meteorological Cycles and Evapotranspiration along the Altitudinal Gradient of the Cajas National Park" and "Identification of hydro-meteorological processes that trigger extreme floods in the city of Cuenca using precipitation radar". The authors are grateful to INAMHI and CBRM for providing the data. Thanks are due to Jan Feyen for his valuable comments and suggestions, and the revision of the manuscript. We are grateful to Lenin Campozano, who programmed the cross-validation procedure. The helpful comments of two anonymous reviewers are specially acknowledged.
Author Contributions: Alex Avilés conceived the initial idea of the study, constructed the models and prepared the manuscript. Rolando Célleri participated in the design of the study, and provided a critical revision of manuscript. Abel Solera and Javier Paredes provided many useful suggestions to improve the analysis of the results and supervised the research.
Conflicts of Interest: The authors declare no conflict of interest.
