# Article 

## Causal Reasoning: Towards Dynamic Predictive Models for Runoff Temporal Behavior of High Dependence Rivers

José-Luis Molina ${ }^{1, *}$ (D), Santiago Zazo ${ }^{2}$ (D) and Ana-María Martín ${ }^{3}$<br>1 Ávila. Area of Hydraulic Engineering, High Polytechnic School of Engineering, Salamanca University, Av. de los Hornos Caleros 50, 05003 Ávila, Spain<br>2 TIDOP Research Group, Salamanca University, Avda. de los Hornos Caleros, 50, 05003 Ávila, Spain; szazo@usal.es<br>3 Ávila. Department of Statistics, High Polytechnic School of Engineering, Salamanca University, Avda. de los Hornos Caleros, 50, 05003 Ávila, Spain; ammc@usal.es<br>* Correspondence: jlmolina@usal.es; Tel.: +34-920-353-500

Received: 28 March 2019; Accepted: 23 April 2019; Published: 26 April 2019


#### Abstract

Nowadays, a noteworthy temporal alteration of traditional hydrological patterns is being observed, producing a higher variability and more unpredictable extreme events worldwide. This is largely due to global warming, which is generating a growing uncertainty over water system behavior, especially river runoff. Understanding these modifications is a crucial and not trivial challenge that requires new analytical strategies like Causality, addressed by Causal Reasoning. Through Causality over runoff series, the hydrological memory and its logical time-dependency structure have been dynamically/stochastically discovered and characterized. This is done in terms of the runoff dependence strength over time. This has allowed determining and quantifying two opposite temporal-fractions within runoff: Temporally Conditioned/Non-conditioned Runoff (TCR/TNCR). Finally, a successful predictive model is proposed and applied to an unregulated stretch, Mijares river catchment (Jucar river basin, Spain), with a very high time-dependency behavior. This research may have important implications over the knowledge of historical rivers' behavior and their adaptation. Furthermore, it lays the foundations for reaching an optimum reservoir dimensioning through the building of predictive models of runoff behavior. Regarding reservoir capacity, this research would imply substantial economic/environmental savings. Also, a more sustainable management of river basins through more reliable control reservoirs' operation is expected to be achieved.


Keywords: Causality; causal reasoning; runoff fractions; hydrological time series; dynamic temporal dependence propagation; predictive models

## 1. Introduction

In recent decades, the alteration of traditional hydrological patterns has been increasingly more evident both worldwide and over a particular territory [1-3]. This is essentially materialized by more frequent and therefore less anomalous extreme events such as floods and droughts [4-7]. This is mainly due to global warming phenomenon [8-10], which is highly intensified by anthropogenic actions [11-13]. Consequently, the stationarity in hydrological time series is not strictly kept [14-17], and therefore, non-stationarity has become a common feature to deal with [18].

Not all the reasons that explain this increasing variability are brand new. Because of that, there is a consequently strong need to have powerful and reliable analytical methods to build accurate models that reproduce and forecast the future hydrological behavior of a river system [19-25]. Also, there is a growing necessity to design analytical strategies that allow: (a) an increase of knowledge on temporal

behavior of the hydrological series [26,27], and (b) the ability to extract the logical and non-trivial time-dependency structure that underlies them [18,28,29,30].

This dual challenge, between powerful-reliable methods and new analytical strategies, is jointly addressed through the scientific approaches shown in Molina et al. [28], Zazo [30], Molina and Zazo [18,29] and Molina, et al [31], among others. This novel and active research line, focused on Causality, is characterized by increasing the knowledge of temporal behavior of water resources. This is done through the coupling among stochastic hydrological parametric models, such as Autoregressive Moving Average (ARMA) models, and innovative methodologies based on Artificial Intelligence (AI), such as Causal Reasoning (CR) supported by Bayesian modelling. In this sense, recent research suggests that this union amongst "traditional-novel approaches" provides more accurate results in the modelling of complex natural processes like hydrological behavior [22,32,33,34]. In addition, this opens new perspectives for building stochastic hydrological predictive models, able to incorporate the inherent uncertainty of the hydrological processes [29,35].

This work aims to develop a new methodological framework that will enable us to advance on the knowledge over historical adaptive behavior of river runoffs. This was addressed through Causality (Causal Reasoning, temporal dependence/independence), a powerful stochastic approach to extract the hidden logical time-dependency structure that inherently underlies into hydrological series. This approach ultimately comprises a new predictive method for the runofft temporal behavior.

In relation to previous works that integrate this research line, this paper represents a breakthrough in the characterization of the temporally runoff fractions in a high dependence rivers context. These fractions were first highlighted in Molina and Zazo [18] and referred to as Temporally Conditioned Runoff (TCR, or fraction due to time) and Non-Conditioned Runoff (TNCR, or uninfluenced by time). Now, both fractions have been determined and quantified based on dependence strength over time. Furthermore, different dynamic management scenarios (time-step by time-step) were generated according to the temporal dependence (time-lags) propagation, from which time series were obtained for each fraction. In addition, a preliminary implementation of a dynamic predictive runoff model was addressed based on the observed temporal behavior trends of both fractions in the different generated scenarios. Finally, the reliability of the predictive model was assessed from a probabilistic perspective, proposing two alternatives; the first one general and the second one detailed where the TNCR fraction adds uncertainty to the prediction because it does not depend on time.

Given that this work implies a step forward over previous ones, it is not considered appropriate to re-emphasize aspects such as the State of Art and theoretical and mathematical frameworks. To read a comprehensive and in-depth review of them, the reader is referred to the aforementioned cited works (please see $[28,29,31]$ ).

Furthermore, the application of this new analytical strategy over annual runoff series applied to reservoirs, dams, and their control operation seems quite straightforward. In this sense, the better knowledge and prediction on temporal behavior of TCR and TNCR fractions will lead to a reconsidering of the capacity of the storage reservoirs, especially convenient in the current context of global warming and for high temporal dependent river basins. This might also help for reaching an optimal dimensioning of dams, what would imply significant economic and environmental savings.

After this initial section, this work is organized as follows: a description of case study, hydrological data, and applied methodology are shown in Section 2. Section 3 provides the main experimental results from the research. In Section 4, the results are discussed in detail. Finally, Section 5 addresses the general conclusions drawn from the study.

# 2. Materials and Methods 

### 2.1. Case Study

Variability and randomness are the main characteristics of water resources in Spain [29,36], which is essentially attributable to an uneven spatial and temporal distribution of the precipitations [18,37].

Indeed, the annual average rainfall in Spain presents a latitudinal decrease pattern, from wet north-west (around 2000 mm), to dry south-east with less than 200 mm [28,38]. This is aggravated by low capacity of retention of Spanish soils; on average a $9 \%$ \& $34 \%$ in the rest of Europe [39].

The selected case study was Mijares river (belonging to Jucar river basin, the second largest basin on the Mediterranean side of the Iberian Peninsula). This river is situated in Eastern Spain, traditionally known as "dry Spain". This zone regularly suffers noteworthy drought conditions [40]. In particular, an unregulated stretch, characterized by a very high time-dependency behavior and by the existence of important water springs at its headwater was selected [41] (Figure 1a). This case study was defined by gauging station "El Terde", code number 8030 (Figure 1b).

Morphometrically, the sub-basin covers a medium-sized extension of $665 \mathrm{~km}^{2}$ [42], with a main stream of 47.462 km in length, an average slope of 0.018 meter/meter. Therefore, it has a time of concentration of 12.13 h , according to Spanish regulations [43].

In lithological terms, there are important formations of loams and clays with alternation of gypsum and conglomerates or limestones and gypsums, being that these areas are generally of low permeability. However, these areas may contain deeper aquifers with greater permeability and productivity. In addition, there are small areas of limestones and dolomites where very permeable aquifers are located, generally large and productive [44].

Annual runoff time series (Figure 1c) were supplied through the network of gauging stations belonging to the Jucar River Basin Authority [45]. Regarding the historical runoff, it is well known in Hydrology, at least in Spain (South Europe), that the " 80 effect" which comprises a drastic reduction in Rainfall and Runoff from the year 80. In this particular basin, this effect is clearly shown in that Figure, where there is also an isolated rise for the period 1988-1991. Most of the authors and experts impute this consequence to Climate Change.
![img-0.jpeg](img-0.jpeg)

Figure 1. (a) Situation map; (b) Jucar River Basin map and case study situation; (c) Historical annual series of runoff (time period: 1945/46 to 2013/14). Note: Time series are referred according to water year in Spain where the first month is October and the last is September of following year.

# 2.2. Methodololy 

This research was articulated in four sequential stages. Firstly, in order to characterize the basin behavior, the memory and temporal behavior indicators of the historical time series were obtained, as well as its main statistical parameters. After that, equiprobable synthetic runoff series were generated through a parsimonious and unconditioned ARMA (1,1) model (Stage-1). Next, synthetic series were applied to populate the Causal Reasoning, supported by Bayesian modelling. This stage was crucial because it comprises the discovery and characterization of the logical and non-trivial time-dependency structure that inherently underlies the hydrological series (Stage-2). Then in Stage-3, based on dependence strength over the time, different dynamic management scenarios (time-step by time-step) were generated. Each temporal dependence scenario contains the dynamic and stochastic identification and quantification of the runoff temporal-fractions, TCR and TNCR. Afterward, an in-depth analysis of each of them was done. Finally, in Stage-4, a preliminary implementation of a dynamic predictive runoff model was performed and its reliability was assessed from a probabilistic perspective (Figure 2).
![img-1.jpeg](img-1.jpeg)

Figure 2. General methodology.

### 2.2.1. Stage-1. Historical Series. Memory and Temporal Behavior Indicators

In order to preliminarily assess the temporal nature of the basin, the memory and temporal behavior indicators of the historical time series were calculated. This was done through Hurst coefficient (H) and correlogram, respectively, based on the general framework exposed in Salas et al. [46] (pp. 41-44 and p. 49 respectively), and which are well established in the scientific community. Given that the determination of H is not a matter of this research, the reader is referred to Tyralis and Koutsoyiannis [47] where a full discussion about its accuracy is done through three different approaches. After that, main statistical parameters of the historical time series were determined. This essentially comprises getting the basic statistics parameters of the ARMA model, such as mean, standard deviation, and variation and skewness coefficients.

Secondly, a set of equiprobable synthetic runoffs were generated through a parsimonious and unconditioned ARMA (1,1) according to Molina et al. [28] and Molina and Zazo [18,29], based on the classical framework to generate ARMA models as shown by Salas et al. [46] (Chapter 5). A 20 years warm-up period was defined for achieving a "non-conditioned" synthetic series generation process without "boundary effects".

In the context of this work, it is worth mentioning that an ARMA $(p, q)$ model is formed by adding a moving average (MA) component to the Autoregressive (AR) component to model the temporal correlation in time series [46]. AR component (" $p$ " part) represents the temporal dependence delay within a series; the MA component uses delays of the forecast errors to improve the process [28]. In this sense, a generic ARMA model is expressed as [48]:

$$
X_{t}=a_{t}+\sum_{j=1}^{p}\left(\varnothing_{j} \cdot X_{t-j}\right)-\sum_{j=1}^{q}\left(\theta_{j} \cdot a_{t-j}\right)
$$

where $X t$ is the value of the variable at a certain time-step $t, p$ is the number of autoregressive parameters, $q$ is the number of moving average parameters, $\varnothing_{j}$ and $\theta_{j}$ are the coefficient of autoregressive and moving average model respectively and $a_{t}$ is a random variable that represents the historical residuals (error term).

# 2.2.2. Stage-2. Causal Reasoning 

Causality was addressed from the perspective of Causal Reasoning, which is characterized by searching reasoning patterns focused on the cause, and where the objective comprises the prediction of the effect [49]. As an analytical strategy, Bayesian modelling was selected, supported by software HUGIN Expert version 7.3 [50]. It should be noted that Bayesian modelling is a powerful AI technique based on a Probabilistic Graphical Model (PGM; [51,52,53,54]) that has significant advantages such as no need for priori information of the process and use of raw data [55,56], its usefulness for analyzing non-linear physical systems [57], or the ease of defining relationships in complex systems and offering a compact representation of the joint probability distribution over sets of random variables [21].

Causal Reasoning is carried out over a set of random decision variables called "nodes" (water years in this case), which are consecutively interconnected through "links" and a set of conditional probability tables between decision variables [21,53,54]. Furthermore, the quantification of the variables' relationship strength is performed by Bayes' theorem, which is propagated over time by the conditional probability; in this way the probability distributions are calculated for each decision variable as [58]:

$$
P(A \mid B)=\frac{P(A, B)}{P(B)}=\frac{P(A \cap B)}{P(B)}
$$

where $P(A \mid B)$ is a probability on event $A$, assuming that event $B$ is true; $P(A, B)$ is the joint probability of events $A$ and $B$; and $P(B)$ is the probability of $B$.

The propagation of the Bayes' Theorem allows, on one hand, dynamically analyze (time-step by time-step) the mitigation (evolution) of temporal dependence over time, through the relative percentage of runoff change that a time-step dynamically produces on the following ones. On the other hand, it allows for generating the yearly interactions among one target year and the previous ones through graphing of marginal dependencies in which each detected connection represents a time-dependency relationship [29].

Hydrological memory of the basin was characterized in terms of the runoff dependence strength over time. This was dynamically performed through interactions over the target year according to the time-horizon defined by the propagation of temporal dependence. The strength of each yearly interaction was evaluated by Dependence Rate ( $D R$; from 0 to 1 ), expressed as [29]:

$$
D R=1-(p \text {-value })
$$

where $p$-value is the measure of the strength of evidence against the independence relationship [28,30]. Therefore, a $D R$ value equal to 1 expresses a lot of evidence of a total dependence, while in contrast 0 represents little evidence against the independence. $D R$ values were arranged in matrix form and classified in two classes and grouped in 5 intervals (Table 1).

Table 1. Dependence Rate $(D R)$. Definition of classes and intervals.


This approach, based on a parsimonious and unconditioned ARMA (1,1) combined with the analytical power of Bayesian modeling, confers a high degree of freedom to the Causal Reasoning that overcoming the temporal imposition of the ARMA model [30]. This makes it possible to discover non-trivial relationships (time lag $>1$ ) among decision variables, initially consecutively connected. In addition it allows us to discover the hidden logical time-dependency structure, which inherently underlies hydrological series [18,28,29].

For a complete definition of these processes, the reader is invited to refer to Molina et al. [28] and Molina and Zazo [29].

# 2.2.3. Stage-3. Temporal Runoff Fractions 

Once the dependence relationships among variables and propagation of the temporal dependence were discovered through Causality, different management scenarios were dynamically/stochastically generated based on methodological framework shown in Molina and Zazo [18], and a detailed analysis of the temporal behavior was done.

In each time-step (time-lag) of the dependence propagation, both temporal-fractions, TCR (fraction due to time) and TNCR (uninfluenced by time) were determined and quantified. In this sense, the sum of both of them represents the total runoff for each water year. Both fractions are expressed as:

$$
\begin{gathered}
T C R_{i}=\frac{\sum_{j=0}^{i-1} w_{j} \cdot Y_{j}}{\sum_{j=0}^{i-1} w_{j}}, \quad i=1, \ldots, T D \\
T N C R_{i}=\left(R_{i}-T C R_{i}\right), \quad i=1, \ldots, T D
\end{gathered}
$$

where $T C R_{i}$ is the weighted average conditioned runoff of the Target Year (i); $w_{j}$ expresses in weight form the dependence of year $j$ on Target Year ( $i$; please see Figure 7b); $Y_{j}$ is the conditioned runoff for the year $j ; T D$ is the temporal interval, expressed in years, of the propagation of dependence from $\operatorname{lag}=0([0,1]$ when the relative percentage change is maximum) to maximum lag (when the relative percentage change is minimum and equal to zero; please see Figure 5); $R_{i}$ is the runoff of the time series in the target year; and $T N C R_{i}$ is the uninfluenced by time fraction for the target year.

Furthermore, in order to highlight the analytical capacity and discovery potential that this methodological framework offers for the basin water resources management, for each time-lag, two different time series were obtained, one for each temporal fraction. Next, the main statistical parameters and the coefficients of different ARMA models for each time series were determined. Consequently, the differences in the parameters and the coefficients will be exclusively due to "discovered nuances" into the temporal behavior. This was done supported by software TRASERO version 2.3.0 [48]. Akaike Information Criterion (AIC; [59]) was applied as criterion of models' selection. This was done by maximizing the expected log-likelihood of a particular model through the maximum likelihood method. The optimal model will be the one with the lowest AIC value [60].

# 2.2.4. Stage-4. Post-Process. 

This represents the last stage of the research. It comprises, on one side, a preliminary design of the predictive model from a probabilistic perspective, and, on the other, the assessment of the prediction reliability. The predictive model was based on the hidden temporal conditionality that inherently underlies of the historical series and that has been discovered through Causality (Stage-3).

Additionally, some studies have demonstrated the validity of stationary assumptions and stochastic parametric models applied to the generation of hydrological predictive models, such as references [61,62]. Recently, Papacharalampous et al. [61] presented an exhaustive study in which large-scale results versus traditional approaches focused on cases studies are provided. Its main conclusion is that stochastic and machine learning methods provide similar forecasts. Earlier, Tyralis and Koutsoyiannis [62] justified the validity of the stationarity hypothesis applied to stochastic methods in a context of prediction of hydroclimatic variables.

In agreement with the above conclusions, the predictive model was performed through stochastic hydrological parametric ARMA models. This was generated by parsimonious ARMA models, one for each temporal fraction (TCR and TNCR). They were developed from a time series obtained in Stage-3, according to temporal horizons of dependence mitigation.

Given that the availability of water resources in Spain is characterized by a high seasonal and annual variability [63-65], the predictive model was generated by a time-horizon of one (1) year (Dep-1). For that reason, the training dataset was 69 years (time period: 1945/46 to 2013/14) and the prediction was done over water year 2014/15. The obtained value of this final year was used to assess the predictive reliability based on the resulting probability.

Finally, the reliability of the predictive model was assessed from a probabilistic perspective, by suggesting two alternatives. The first one general and the second one detailed. The second approach is based on the fact that the TNCR fraction does not depend on time, and, consequently, adds uncertainty to the prediction. For that, two Monte Carlo simulations from ARMA models with 5000 data were done. The probabilistic approach was based on Gringorten probability expressed as [66]:

$$
F_{\left(y_{i}\right)}=\frac{i-0.44}{n+0.12}
$$

where $F_{\left(y_{i}\right)}$ is the value is the value of the data distribution function $y_{i}, i$ the occupied position by the data in the series ordered from lowest to highest, and $n$ the total number of data in the series.

## 3. Results

### 3.1. Statistical Analysis

Figure 3 shows both the main results drawn from the traditional statistical analysis performed (Figure 3a) and the temporal correlation through correlogram (Figure 3b). Please note that the Anderson limits of a correlogram define the temporal non-dependent region; in this way, if the correlation coefficient for a certain time-lag is located inside this region, this time-step is temporally non-dependent. In addition, regarding Hurst coefficient, the resulting value was 0.84 , which indicates that analyzed runoff series has a high long-term memory. This is in agreement with the observed temporal behavior shown by the correlogram. In Figure 3b it can be clearly observed that the zone of the highest dependency is mainly located in the time-lag interval $[0,7]$.

An in-depth analysis of the correlogram reveals isolated points that may provide uncertainty on time dependence (see time-lags 4,7 and 8 ). In these points, the correlation coefficient $(r k)$ is very close to the Anderson limits, $r k_{4}=0.225[-0.257,0.226], r k_{7}=0.216[-0.263,0.231]$ and $r k_{8}=0.231$ versus $[-0.265,0.232]$. In addition, from $r k_{8}$ to $r k_{10}$ a slight trend toward an independent area of the correlogram is also observed. This is due to the average and static behavior that a correlogram offers. However, these doubts on the dependent nature of runoff series and its time-horizon will be solved by means of the dynamic analysis through the Causality.

![img-2.jpeg](img-2.jpeg)

Figure 3. (a) Main statistical parameters of runoff series. (b) Correlogram and Anderson probability limits for an independent series ( 95 percent probability level).

Synthetic series, obtained through a parsimonious and unconditioned ARMA (1,1) model, maintain the main statistical parameters of the runoff series (Table 2). In this sense, Figure 4 shows the spectrum of generated synthetic series to populate and train the Causal Reasoning through Bayesian modelling.

Table 2. Main statistical parameters. Historical series versus set of synthetic series from Autoregressive Moving Average (ARMA) $(1,1)$.


${ }^{1}$ Classic skewness coefficient. $\square$
![img-3.jpeg](img-3.jpeg)

Figure 4. Spectrum of synthetic series to populate the Causal Reasoning versus historical runoff.

# 3.2. Analysis of the Temporal Conditionality through Causal Reasoning 

The temporal dependence propagation (mitigation) for the period 1945/46 to 2013/14 was evaluated by means of a dynamic analysis of the relative percentage of change evolution over the whole time period. Figure 5 shows the discovered dependence through the maximum (MAX or positive) and minimum (MIN or negative) wrap-around shapes and fourth-order functions, which describe the temporal behavior, these last ones with high determination coefficients $\left(R^{2}=0.99\right.$ in both cases).
![img-4.jpeg](img-4.jpeg)

Figure 5. Causal modelling of the mitigation/propagation of temporal dependence by an analysis of the evolution of the relative percentage of change over the time period 1945/46 to 2013/14.

It is also worthy highlighting the lack of symmetry in the Figure 5, with a positive (MAX) wrap-around evidently dominant over the negative one (practically null). This reveals a clear dependence behavior which coincides with that observed in the correlogram (see Figure 3b). However, the dynamic propagation of dependence by Causal Reasoning encompasses a time-horizon of exclusively 7 years (from maximum value of relative percentage change (time-lag $=0[0,1]$ ) to minimum value ( $y$-axis equal zero; time-lag $=7[6,7]$ ), versus 10 years shown by the average and static behavior that the correlogram offers (Figure 3b). Furthermore, uncertain points on time dependence shown in the correlogram ( $r k_{4}$ and $r k_{7}$ ) have been eliminated by Causal Reasoning. This is shown by the dominant positive wrap-around that reveals that dependence exists but with less force. In this sense, both indeterminacies $\left(r k_{4}\right.$ and $\left.r k_{7}\right)$ might be due to the same aforementioned reasons for the observed difference in the time horizon.

A detailed analysis of the graph of dependence propagation highlights a double dependence behavior. The first one, between interval $[0,4]$, of greater dependence, presents a rapid mitigation of dependence from a relative percentage of change of $4,612.7$ (time-lag $=0$ ) to 167.7 (time-lag $=4$ ), and where the maximum dependence is observed in the interval $[0,1]$. In contrast, the second one, in the interval $[4,7]$ and with a reduced relevance, shows a smooth mitigation and a non-significant increase in the final interval $[6,7]$. These discovered, different and continuous behaviors might indicate a temporal behavior both in the short ( $[0,4]$ ) and medium ( $[4,7]$ ) term that is not detected by the correlogram.

Additionally, the analytical power and suitability of Causal Reasoning applied to complex natural systems are clearly revealed in Figure 6, in which a large number of non-trivial dependency relationships (time-lag $>1$ ) amongst water years (decision variables) are revealed. Every detected connection shows an independent relationship that is measured by its $p$-value.

Finally, from the graph of marginal dependencies and for a $100 \%$ independence level threshold and Equation (3), Figure 7 presents, in matrix form, the hydrological memory of the basin in terms of the runoff independence/dependence strength, over time.

![img-5.jpeg](img-5.jpeg)

**Figure 6.** Graph of Marginal Dependencies. Note: The displayed threshold of level of independence is 0.05 (up to 95% of dependency relationships are shown amongst water years or decision variables).


**(a)**


**Figure 7.** (**a**) Matrix of independence. The cell value is *p-value*. (**b**) Matrix of dependence. The cells show dependence rate (DR) value of each relationship. Row values indicate year interactions with respect to target year (main diagonal cell). Note: In order to achieve a better knowledge about the results obtained a part of the matrixes is only shown (1945/46 to 1958/59), nevertheless the results encompass the whole time period of the runoff series. For the color code please see Table 1.

Water 2019, 11, 877 11 of 18

3.3. Management Scenarios Applying Equations (4) and (5) over runoff series, the two temporal fractions (TCR and TNCR) were determined and quantified in agreement with the graph of mitigation/propagation of temporal dependence (see Figure 5).

Figure 8 shows the different generated dynamic management scenarios. In addition, Table 3 summarizes the evolution of both temporal fractions with respect to the mean value of runoff. In each time-lag, it can be clearly seen, as the percentages of TCR exhibit high values (always above 65% and up to mean value of 86.1%), what agrees with the Hurst coefficient (0.84). Furthermore, the dual pattern of revealed behavior by Figure 5 in two intervals [0,4] and [4,7] is also observed.

Table 3. Temporally Conditioned Runoff (TCR) and Temporally Non-conditioned Runoff (TNCR) Fractions. Analysis of temporal behavior for a reference threshold 2.


2 Reference threshold: Mean value of the runoff.

The discovery potential that this methodological framework offers for the management of the water resources of a basin is shown in the Tables 4 and 5.

Table 4. TCR Fraction. Evolution of the main statistical parameters according to time dependence.


¹ Classic skewness coefficient.

Regarding the ARMA models coefficients of the TCR fraction, their range does not show a significant variability. However, slight nuances are evident in their behavior because of the propagation of time dependence. Classical analysis does not detect this because the coefficients are unique and fixed in each model. In contrast, the TNCR fraction variability is greater, especially in the $\varnothing_{1}$ coefficient (from 0.9979 to 0.9993) versus the fixed coefficients of the historical series (0.9985 and 0.9992). This would allow for a better characterization of this uninfluenced by time fraction, and therefore, the uncertainty of temporal behavior would be reduced.

![img-6.jpeg](img-6.jpeg)

Figure 8. Dynamic management scenarios. Please note Dependence Propagation (3 year) is referred time-lag equal to 3 .

Table 5. ARMA model selection. parameters and the coefficients.


![img-7.jpeg](img-7.jpeg)

Figure 9. Preliminary implementation of the predictive model for a Dependence Propagation one year (Dep-1).

On the other hand, the reliability of the predictive model is shown in Table 6, both a general approach and a detailed one developed through a definition of TNCR intervals which is an uninfluenced fraction of the time. From this approach, this adds an uncertainty component to the prediction because this fraction does not depend on time. The recorded value of target water year to assess the predictive reliability, $28.4 \mathrm{Hm}^{3}$ was supplied by the Jucar River Basin Authority (please, see Reference [41]).

Table 6. Prediction Analysis for a Dependence Propagation one year (Dep-1).


${ }^{3}$ TNCR: Fraction uninfluenced by time.

# 4. Discussion

This methodology allows knowing, in detail and jointly, the behavior of water resources in the short and medium term (Figure 5; [0.4] and [4.7]), as well as their time-horizon ( 7 years versus 10 of the correlogram; Figures 3b and 5). In this sense, it is worth highlighting the coherence between the Hurst coefficient ( 0.84 ) and the results obtained (asymmetry in Figure 5). It is also remarkable the existing agreement between the dual pattern of behavior presented in Figure 5 (intervals [0,4] and [4,7]) and the analysis of the TCR and TNCR fractions' temporal behavior evolution shown in Table 3 (time-lags 1 to $4 ; 84.8 \%$ to $70.1 \%$ ).

Furthermore, the potential of this methodological framework for the basin water resources management largely became clear when the temporal behavior nuances of each fraction series (Tables 4 and 5) were discovered. It is important to mention that these nuances cannot be detected by the classical approaches. This was revealed by the variability of the ARMA model coefficients, especially noteworthy in the case of TNCR Fraction (Table 5).

Regarding the predictive model, it shows a high level of reliability, $82.4 \%$ in general perspective, and within $85 \%$ to $90 \%$ through a detailed approach ([20.11, 30.23] and [22.26, 34.50] for a time-dependency of one-year; see Table 6).

Moreover, detailed analysis over the temporal fractions presents crucial and convenient implications over dimensioning, and control operations of reservoirs and dams. This is clearly shown on the uncertainty that TNCR fraction adds to the predictive model. In a sense, for a runoff of $28.4 \mathrm{Hm}^{3}$ in the target water year, there is an uncertainty among 5.06 and $6.12 \mathrm{Hm}^{2}$ due to the fraction not influenced by time, approximately 17.8 or $21.5 \%$ of the total runoff, respectively. Therefore, in a management context, that volume should be jointly provided by the reservoir-dam and its control operations in the previous year. In this way, the failure capacity of the infrastructure is reduced or minimized.

Although reservoir dimensioning involves knowing multiple key aspects such as capacity-areaelevation curves, downstream impacts and sediments inflow, among others, this methodological framework might effectively contribute to achieving a better dimensioning of reservoirs and dams. This will necessarily improve service guarantees through detailed knowledge of the runoff temporal-fractions (TCR and TNCR), especially TNCR fraction, which it is not temporally dependent.

Furthermore, this methodology opens new perspectives for building dynamic and stochastic hydrological predictive models. Also, more river basins sustainable management approaches are expected to be designed. This may be produced through more reliable control operation of reservoirs within the current context of global warming, and for high temporal dependent river basins.

Future research will incorporate the analysis of spatial dimension behavior in the design of causal models.

# 5. Conclusions 

This research supposes a breakthrough in the temporal characterization of runoff series. Here, Causality has discovered a hidden and logical structure of temporal interdependence that inherently underlie the hydrological series. This represents a latent behavior pattern that was waiting to be discovered and that the classical approaches had not been able to reveal. This was performed by means of the coupling of a stochastic hydrological parametric, parsimonious and unconditioned ARMA model, and Causal Reasoning. The latest was supported by Bayesian modelling, which is a powerful AI technique based on probabilistic graphical model.

The methodological framework makes possible to generate dynamic management scenarios according to the propagation (mitigation/evolution) of the dependence (time-lags), taking into account the runoff dependence strength over time. In that sense, two opposite temporal-fractions, the Temporally Conditioned Runoff (TCR) fraction, and Temporally Non-Conditioned Runoff (TNCR) fraction were determined and quantified within the runoff series. Furthermore, the observed behavior trends of TCR/TNCR fractions made it possible to build a predictive runoff model with a high level of reliability.

The application of this new analytical strategy over annual runoff series applied to dimensioning of reservoirs, dams, and control operation of reservoirs seems quite straightforward. In this sense, a design more adjusted to the real needs of reservoirs-dams through a better knowledge and prediction on temporal behavior of TCR and TNCR fractions is expected to be achieved. This will lead to a reconsideration of the capacity of the storage reservoirs, especially their convenience in the current context of global warming and for high temporal dependent river basins. This would imply substantial economic and environmental savings in the future.

This research has demonstrated that past information provides prior knowledge of the future with a high degree of reliability. Furthermore, this research reinforces the suitability of Causality (Causal Reasoning) in modelling the temporal behavior of the water resources of a highly dependent basin from a dynamic and stochastic perspective.

Author Contributions: J.-L.M. and S.Z. conceived, designed and led the experiments. J.-L.M. and S.Z. have performed the experiments. J.-L.M., S.Z. and A.-M.M. analyzed the data. J.-L.M., S.Z. and A.-M.M. contributed reagents/materials/analysis tools. All authors wrote the paper.

Acknowledgments: Authors especially appreciate the suggestions in this work of Marta Molina (Salamanca University, Spain). Authors sincerely thank the reviewers 'effort who greatly help us to provide a much higher quality paper.
Conflicts of Interest: The authors declare no conflict of interest.
