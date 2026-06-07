Nat. Hazards Earth Syst. Sci., 13, 439-454, 2013
www.nat-hazards-earth-syst-sci.net/13/439/2013/
doi:10.5194/nhess-13-439-2013
(c) Author(s) 2013. CC Attribution 3.0 License.

Natural Hazards and Earth System Sciences

# Dynamic decision making for dam-break emergency management - Part 2: Application to Tangjiashan landslide dam failure 

M. Peng ${ }^{1,2}$ and L. M. Zhang ${ }^{1}$<br>${ }^{1}$ Department of Civil and Environmental Engineering, The Hong Kong University of Science and Technology, Hong Kong<br>${ }^{2}$ Key Laboratory of Geotechnical and Underground Engineering of Ministry of Education, Department of Geotechnical Engineering, Tongji University, Shanghai, China

Correspondence to: L. M. Zhang (cezhangl@ust.hk)
Received: 26 March 2012 - Published in Nat. Hazards Earth Syst. Sci. Discuss.: -
Revised: 12 January 2013 - Accepted: 23 January 2013 - Published: 18 February 2013


#### Abstract

Tangjiashan landslide dam, which was triggered by the $M_{\mathrm{s}}=8.0$ Wenchuan earthquake in 2008 in China, threatened 1.2 million people downstream of the dam. All people in Beichuan Town 3.5 km downstream of the dam and 197 thousand people in Mianyang City 85 km downstream of the dam were evacuated 10 days before the breaching of the dam. Making such an important decision under uncertainty was difficult. This paper applied a dynamic decisionmaking framework for dam-break emergency management (DYDEM) to help rational decision in the emergency management of the Tangjiashan landslide dam. Three stages are identified with different levels of hydrological, geological and social-economic information along the timeline of the landslide dam failure event. The probability of dam failure is taken as a time series. The dam breaching parameters are predicted with a set of empirical models in stage 1 when no soil property information is known, and a physical model in stages 2 and 3 when knowledge of soil properties has been obtained. The flood routing downstream of the dam in these three stages is analyzed to evaluate the population at risk (PAR). The flood consequences, including evacuation costs, flood damage and monetized loss of life, are evaluated as functions of warning time using a human risk analysis model based on Bayesian networks. Finally, dynamic decision analysis is conducted to find the optimal time to evacuate the population at risk with minimum total loss in each of these three stages.


## 1 Introduction

Triggered by the $M_{\mathrm{s}}=8.0$ Wenchuan earthquake on 12 May 2008 in Sichuan China, a slope of Tangjiashan hill failed, which blocked the Jianjiang River and formed a large landslide dam as shown in Fig. 1. The dam was found on 14 May through an aerial investigation (CCTV News, 2008). From the analysis of aerial photos, the dam was estimated to have a height of 82 m , width of 802 m , length of 611 m , dam volume of 20.4 million $\mathrm{m}^{3}$ and lake capacity of 316 million $\mathrm{m}^{3}$ (Cui et al., 2009; Hu et al., 2009; Liu et al., 2010) as shown in Table 1. The landslide dam was located at 3.5 km upstream of Beichuan Town with 30000 residents, and 85 km upstream of Mianyang City with 1127000 residents (Fig. 2). Note the population in Beichuan Town (i.e. 30000 ) refers to that before the earthquake (Liu, 2008), in which the casualties during the Wenchuan earthquake and the relocated people are not excluded.

The landslide dam could not be accessed due to blockage of roads by landslides until 21 May when experts managed to arrive in the dam by helicopter. The geological conditions of the dam were obtained two days later through in situ investigations. The dam mainly consists of three layers (Fig. 3): the upper layer of gravely soils with a thickness of $5-15 \mathrm{~m}$; the middle layer of strongly weathered cataclasite with a thickness of $10-15 \mathrm{~m}$; and the bottom layer of weakly weathered cataclasite with a thickness of $50-80 \mathrm{~m}$ (Hu et al., 2009; Liu et al., 2009, 2010). The coefficient of erodibility of the dam varies from $120 \mathrm{~mm}^{3}(\mathrm{~N}-\mathrm{s})^{-1}$ for the top layer to $10 \mathrm{~mm}^{3}(\mathrm{~N}-$ s) ${ }^{-1}$ for the bottom layer (Chang and Zhang, 2010; Chang et al., 2011). Three possible dam-failure scenarios with a small,

Table 1. Parameters of Tangjiashan landslide dam.


![img-0.jpeg](img-0.jpeg)

Fig. 1. Satellite image of the Tangjiashan landslide triggered by the 2008 Wenchuan earthquake (modified from Liu, 2008).
medium and large breach were assumed for evacuation decision at that time; the corresponding estimated peak outflow rates at the dam site being $33771,47252$ and $69577 \mathrm{~m}^{3} \mathrm{~s}^{-1}$, respectively (Huang et al., 2008). The corresponding estimated populations at risk (PARs) downstream are approximately $0.2,1.0$ and 1.2 million, respectively. The predicted floods were very large. The government decided to reduce the dam-break risks by excavating a diversion channel. The channel was completed by 1 June with great efforts, as all the excavation equipment had to be shipped by heavy-duty helicopters. As shown in Table 1, the diversion channel has a length of 475 m , a width of 25 m and a depth of 12 m . The channel lowered the crest elevation from 752.2 m to 740.4 m , and reduced the lake capacity from 316 million $\mathrm{m}^{3}$ to 247 million $\mathrm{m}^{3}$ (Liu et al., 2010).

A series of problems arose when making decisions on evacuating the people downstream. What was the damfailure probability? When would the dam fail? How large would the peak outflow rate be? How effective is a diversion channel to reduce the risks? How many people should be evacuated? When would be the proper time to evacuate the PAR? A late decision could lead to loss of lives and properties, whereas a very early evacuation would incur unnecessary expenses. There was little information about the
landslide dam when it was just found. How could one progressively reach the best decision as relevant information on the hydrological, geological and social-economic conditions becomes available gradually? A framework for decisionmaking based on dynamic risk analysis is needed to scientifically answer these questions.

A dynamic decision-making framework for dam-break emergency management (DYDEM) under uncertainty has been presented in the companion paper (Peng and Zhang, 2013). In this paper, the DYDEM is applied to the dynamic decision analysis for the Tangjiashan landslide dam failure. The optimal time to evacuate the PAR for achieving a minimum expected total risk will be studied in different stages with different available hydrological, geological and socialeconomic information.

## 2 The framework and stages of dynamic decision making

### 2.1 The framework

The framework of dynamic decision making is intended to make a decision whether to evacuate the population at risk or to delay the decision; to predict the optimal time to evacuate the PAR with the minimum expected total loss (MTC); and to update the decision-making with new information when delayed decision is chosen.

DYDEM is a dynamic decision framework for dam-break emergency management that is introduced in the companion paper (Peng and Zhang, 2013). In this framework, the probability of dam failure is taken as a stochastic process and estimated using a time-series analysis method. The flood consequences are taken as functions of warning time and evaluated with a human risk analysis model (HURAM) based on Bayesian networks (Peng and Zhang, 2012a, b). A decision criterion is suggested to decide whether to evacuate the PAR or to delay the decision. The optimum time for evacuating the PAR is obtained by minimizing the expected total loss, which integrates the time-related probabilities and flood consequences. When a delayed decision is chosen, the decision making can be updated with available new information.

The decision process starting at a certain time $\left(t_{0}\right)$ with different available information is defined as a stage. A dynamic decision should be a multi-stage decision process. In each

Table 2. Available information in the three stages of decision making for Tangjiashan landslide dam.


![img-1.jpeg](img-1.jpeg)

Fig. 2. Locations of the dam, Beichuan Town and Mianyang City.
stage, both the predicted dam-break probabilities and flood consequences can be updated. In the case study of Tangjiashan landslide dam, three stages with significant changes in information are identified for evacuation decision making.

### 2.2 The timeline and stages for decision making for the Tangjiashan landslide dam failure

Figure 4 summarizes the main issues along the timeline of the Tangjiashan landslide dam failure event. Three stages can be distinguished for evacuation decision-making in Table 2:

1. Stage 1 starts on 15 May, when the landslide dam was identified and the geometric parameters of the dam were estimated as shown in Table 1. As the soil conditions of the dam remained unknown, an empirical model (Peng and Zhang, 2012c) based on statistical data was used to predict the breaching parameters.
2. Stage 2 starts on 23 May, when the soil conditions of the dam were investigated as shown in Fig. 3. Both geometric parameters and soil conditions are available. Thus,
![img-2.jpeg](img-2.jpeg)

Fig. 3. Cross sections of Tangjiashan landslide dam: (a) across the river; (b) along the river.
a physical model for dam breaching analysis, DABA (Chang and Zhang, 2010), was applied to improve the prediction of the breaching parameters. In stages 1 and 2, the elevation of the dam crest was 752.2 m .
3. Stage 3 starts on 1 June, when the diversion channel had been constructed. With the channel, the dam crest was lowered by 12 m (i.e. the elevation of the dam crest became 740.4 m ) and the lake capacity was reduced by 69 million $\mathrm{m}^{3}$. Moreover, a large part of the top soil layer with high erodibility (Chang and Zhang, 2010) was removed. Therefore, the peak outflow rate during breaching was significantly reduced in stage 3.

In the following sections, the analysis of the dam-break probability and flood consequences and the dynamic decision making in each of these three stages will be demonstrated.

Table 3. A recorded time series of inflow rate into the Tangjiashan landslide lake (Data from Zhang, 2009).


Note: The average inflow rate is $94.18 \mathrm{~m}^{3} \mathrm{~s}^{-1}$, and the standard deviation is $21.64 \mathrm{~m}^{3} \mathrm{~s}^{-1}$.

![img-3.jpeg](img-3.jpeg)

Fig. 4. The timeline and three stages of decision making.

## 3 Prediction of dam-break probability with time series analysis

As $92 \%$ of past landslide dam failures were due to overtopping (Peng and Zhang, 2012c), only overtopping failure is considered in this study. A dam is overtopped at time $t$ when the reservoir volume $\left(V_{t}\right)$ exceeds its capacity $\left(V_{\text {cr }}\right)$, or $V_{t}>V_{\text {cr }}$.

### 3.1 Forecasting lake volume

Based on conservation of mass as introduced in the companion paper (Peng and Zhang, 2013), the reservoir volume at time $t, V_{t}$, is given by $V_{t}=V_{t-\Delta t}+\left(Q_{t}-Q_{o t}-Q_{\mathrm{ct}}\right) \Delta t$, where $\Delta t$ is a time interval; $Q_{t}$ is the inflow rate at time $t ; Q_{\mathrm{ct}}$ is the evaporation rate which could be ignored for a short time during the emergency management; $Q_{\text {ot }}$ is the outflow rate at time $t$. In the Tangjiashan landslide dam case, the seepage flow rate was very small $\left(<1 \mathrm{~m}^{3} \mathrm{~s}^{-1}\right)$, which can be ignored $\left(Q_{\text {ot }}=0\right)$. Therefore, the main task of predicting the dam-break probability is to forecast the inflow rate at time $t$, $Q_{t}$.

According to the records at a hydrological station 4 km upstream of the Tangjiashan landslide dam and the records at the dam site, the average daily inflow rates from 12 May to 13 June 2008 were estimated as shown in Table 3 (Zhang, 2009). The authors have to use the limited data to build a time series model for inflow forecasting. Actually, part of the data may not be available when making decisions in the three stages. Let us set $x_{t}=Q_{t}-\bar{Q}$, where $\bar{Q}=94.2 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ (Table 3) is the average value of the records of $Q_{t}$. According to the time series theory in Appendix A, a time series model of $\operatorname{AR}(2)$ is suitable to fit the records in Table 3, and $x_{t}$ is expressed as $x_{t}=0.463 x_{t-1}-0.181 x_{t-2}+a_{t}$.

Both the means and standard deviations of $x_{t}$ are obtained according to Appendix A. Taking stage 1 for example, Fig. 5 shows the predicted inflow rates into the Tangjiashan landslide lake in stage 1 based on the records before 15 May. Generally, the records are within the $95 \%$ confidence interval in the stage. The first several predicted values are relatively close to the records. The predicted values with lead times larger than five days $(l>5)$ gradually approach a constant value of $94.2 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ and the corresponding standard deviations approach a constant value of $21.6 \mathrm{~m}^{3} \mathrm{~s}^{-1}$, which are the estimated average value and standard deviation based on the statistical data, respectively as shown in Table 3. One reason for this is that the dependence between two variables of the time series at a large time interval is very small. In other words, the variables at large time intervals appear to be independent. The predictions in stage 2 and stage 3 are updated by using the records during 12-22 May and during 12-31 May, respectively.

As the $\Delta t$ in Eq. (1) is one day, the reservoir volume at day $t\left(V_{t}\right)$ is given by $V_{t}-V_{t-1}=3600 \times 24 \times Q_{t}=3600 \times 24 \times\left(x_{t}+\bar{Q}\right)$ where $\bar{Q}=94.18 \mathrm{~m}^{3} \mathrm{~s}^{-1}$. By setting $v_{t}=V_{t} /(3600 \times 24)$, then $x_{t}=v_{t}-v_{t-1}-\bar{Q}$.

Substituting the expressions for $x_{t}, x_{t-1}$ and $x_{t-2}$ into Eq. (2) yields $v_{t}=1.463 v_{t-1}-0.644 v_{t-2}+0.181 v_{t-3}+0.717 \bar{Q}+a_{t}$.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Predicted inflow rate in stage 1 based on the records before 15 May using the time series method.

Therefore, the forecasting equations for $v_{t}$ are given by

$$
\begin{aligned}
v_{t}^{*}(1)= & 1.463 v_{t}-0.644 v_{t-1}+0.181 v_{t-2}+67.53 \\
v_{t}^{*}(2)= & 1.463 v_{t}^{*}(1)-0.644 v_{t}+0.181 v_{t-1}+67.53 \\
v_{t}^{*}(3)= & 1.463 v_{t}^{*}(2)-0.644 v_{t}^{*}(1)+0.181 v_{t}+67.53 \\
v_{t}^{*}(l)= & 1.463 v_{t}^{*}(l-1)-0.644 v_{t}^{*}(l-2)+0.181 v_{t}^{*}(l-3) \\
& +67.53, l=4,5, \ldots
\end{aligned}
$$

Similar to $x_{t}$ in Appendix A, $v_{t}$ can also be expressed in a random shock form of an infinite series:

$$
\begin{aligned}
v_{t} & =a_{t}+\psi_{1} a_{t-1}+\psi_{2} a_{t-2}+\psi_{3} a_{t-3} \cdots \\
& =a_{t}+\sum_{j=1}^{\infty} \psi_{j} a_{j}
\end{aligned}
$$

where the coefficients of $\psi_{j}$ can be obtained by substituting Eq. (7) into Eq. (5) and comparing the coefficients of $a_{t}$ on both sides (Box et al., 2008). Table 4 shows the $\psi$ weights $\left(\psi_{l}\right)$ for $v_{t}$. As $a_{t}$ is an independently and identically distributed stochastic process with a normal distribution of $N\left(0, \sigma_{a}^{2}\right)$, the standard deviation of $x_{t}$ is calculated as (Box et al., 2008)
$\sigma^{2}\left[v_{t}(l)\right]=\left(1+\psi_{1}^{2}+\psi_{2}^{2}+\ldots+\psi_{l-1}^{2}\right) \sigma_{a}^{2}$.
Figure 6 shows the records, predictions, and the upper and lower $95 \%$ confidence intervals of the lake volume. The predictions are generally within the $95 \%$ confidence interval. The predictions are closer to the records at small lead times. The variance of the predicted lake volume increases with time, as the prediction for the future is less supported by the existing data.

### 3.2 Prediction of dam failure probability

Since $v_{t}$ can be expressed as a weighted average of several normal variates as shown in Eq. (7), $v_{t}$ is also a normal distribution. With the predicted mean and variance of the lake volume, the probability of dam failure before time $t\left[P_{\mathrm{O}}(t)\right]$ is calculated as

$$
P_{\mathrm{O}}(t)=P\left(V_{t}>V_{\mathrm{cr}}\right)=1-P\left(V_{t} \leq V_{\mathrm{cr}}\right)=1-\Phi\left(\frac{V_{\mathrm{cr}}-M_{V_{t}}}{\sigma_{V_{t}}}\right)
$$

![img-5.jpeg](img-5.jpeg)

Fig. 6. Predicted lake volume in stage 1 using the time series analysis method.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Dam-break probability as a discrete time series at an interval of one day in stage 1 .
where $V_{t}$ is calculated using Eq. (6); $M_{V_{t}}$ and $\sigma_{V_{t}}$ are the mean and standard deviation of $V_{t}$. The probability of overtopping in the period between $t-\Delta t$ and $t, P_{D}(t)$, is calculated as the probability that the predicted $V_{t}$ is larger than $V_{\text {cr }}$ and the predicted lake volumes before time $t$ are smaller than or equal to $V_{\mathrm{cr}}$ :
$P_{D}(t)=P\left(V_{t}>V_{\mathrm{cr}}, V_{t-1} \leq V_{\mathrm{cr}}, \ldots, V_{1} \leq V_{\mathrm{cr}}\right)$.
As the inflow rate is greater than the outflow rate, the lake volume always increases. According to the analysis in the companion paper, $P_{D}$ is expressed as

$$
\begin{aligned}
P_{D}(t) & =P\left(V_{t}>V_{\mathrm{cr}}, V_{t-1} \leq V_{c r}, \ldots, V_{1} \leq V_{\mathrm{cr}}\right) \\
& =P_{\mathrm{O}}(t)-P_{\mathrm{O}}(t-1)
\end{aligned}
$$

For example, $V_{\text {cr }}$ in stage 1 is 316 million $\mathrm{m}^{3}$; the predicted probabilities of $P_{\mathrm{O}}$ and $P_{D}$ in stage 1 as two discrete time series are shown in Fig. 7.

The time interval of the predicted hydraulic parameters is in days, because the inflow rates in Table 3 were recorded in days. However, more precise warning time is needed in DYDEM, because the flood consequences are sensitive to the warning time. Therefore, in this study, interpolations are conducted for predicted means and variances of lake volume

Table 4. The $\psi$ weights for time series $v_{t}$ in stage 1.


Note: * The $\psi$ weights are close to a constant value of 1.394 when $l>9$.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Discrete probability of dam failure in three stages with a time interval of one hour.
with a time interval of one hour. This is reasonable as the predicted mean values and variances of the lake volume increase nearly linearly at large lead times $(l \geq 5)$.

Figure 8 shows the discrete probability of dam failure in an interval of one hour in all three stages. Note $V_{\mathrm{cr}}$ is 316 million $\mathrm{m}^{3}$ in stages 1 and 2 , and 224 million $\mathrm{m}^{3}$ in stage 3 , because the diversion channel was completed in stage 3. The dam-break probabilities in discrete time series in the three stages will be used to conduct dynamic decision analysis. In stage 3, the dam may fail much earlier than in stages 1 and 2 because of the smaller lake capacity. Moreover, the estimated times of dam break in stage 3 become less scattered than in stages 1 and 2, since more information is available in stage 3 such as the geometric conditions, a constructed diversion channel, the decreased crest elevation, and the removal of a soil layer with high erodibility.

## 4 Simulation of dam breaching and flood routing

The estimation of dam-break probability answers the question of whether and when the dam would fail. In this section the questions of how it would fail and who would be affected by the dam-break flood will be answered. The dam breaching process, significantly influences the flood consequences downstream. The peak outflow rate affects the flood area and the corresponding PAR. The breach formation time, which is the duration from the lake water level reaching the dam crest to the start of breaching (i.e. the breach reaches the upstream bound of the dam crest), is part of the available warning time. The breach development time or breaching time, which is the
duration from the start to the completion of the breaching process, significantly influences the flood rise time.

### 4.1 Simulation of dam breaching and flood routing in stage 1

In stage 1, when only the geometric parameters of the Tangjiashan landslide dam are available, an empirical model for landslide dams (Peng and Zhang, 2012c) is applied to predict the breaching parameters. The empirical model was developed based on 52 landslide dam failure cases from all over the world. These cases are divided into three groups with different dam erodibility (high, medium or low erodibility) according to the dam type, rock and soil properties and factors such as triggers (Knapen et al., 2007; Briaud et al., 2008). The equations with medium erodibility are used to simulate the Tangjiashan landslide dam since the dam is assumed to be of medium erodibility based on Peng and Zhang (2012c). The inputs of the model include dam height ( 82 m ), dam width ( 802 m ), dam volume ( 20.4 million $\mathrm{m}^{3}$ ), lake volume ( 316 million $\mathrm{m}^{3}$ ) and dam erodibility (medium). As no information about the dam erodibility is available at that time, the uncertainty of this parameter is estimated according to statistics. Out of the 52 cases with breaching-parameter records, 6 cases are of low erodibility, 31 cases of medium erodibility and 15 cases of high erodibility. Thus, the probabilities of low, medium and high erodibility are $0.116,0.596$ and 0.288 , respectively (Peng and Zhang, 2012c). The outflow rates with high, medium and low erodibility are shown in Fig. 9. Table 5 shows the predicted peak outflow rates and breaching times. The peak outflow rate in the high erodibility case is 5 times that in the medium erodibility case and 16 times that in the low erodibility case. Note that the empirical model differs from the one for man-made dams by Xu and Zhang (2009).

After obtaining the breaching parameters, a river analysis program, HEC-RAS 4.0 (Hydrologic Engineering Center, 2008), is used to simulate the flood routing process. This is a one-dimensional hydraulic analysis program developed by US Army Corps of Engineers. The main physical laws for the program are the conservation of energy for steady flows and the conservation of mass and momentum for unsteady flows (Hydrologic Engineering Center, 2008). Details of the simulations are reported by Peng (2012). The highest water depth, maximum flow velocity and PAR in Beichuan Town and Mianyang City are shown in Table 5. The flood risks vary significantly from low to high erodibility. Mianyang City would not be flooded in the low and medium erodibility

Table 5. Dam-break floods in Beichuan Town and Mianyang City in stage 1.


Note * The design flood for the levee system in Mianyang City is $14500 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ with a $100-\mathrm{yr}$ return period.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Outflow rates in the three scenarios of stage 1.
cases. However, the flood in the high erodibility case would put 0.21 million people at risk. The highest water depth in Mianyang City would be 3.68 m .

### 4.2 Simulation of dam breaching and flood routing in stage 2

In stage 2, after the geological conditions of the dam have been investigated, a physical model named DABA (Chang and Zhang, 2010) is used to improve the dam breaching simulation. The water-soil interactions in this model are simulated with theory of erosion and shallow water flow. The soil erodibility is described by the coefficient of erodibility (i.e. how fast the soil erodes) and the critical erosive shear stress (i.e. when the erosion starts and ends), which are obtained based on empirical relations with basic soil parameters. Chang et al. (2011) derived two empirical equations for estimating the coefficient of erodibility of landslide dams based on results of field erodibility tests. Chang and Zhang (2010) measured the basic properties of soil samples taken from the Tangjiashan landslide dam at different depths
$(10 \mathrm{~m}, 20 \mathrm{~m}, 21 \mathrm{~m}$ and 50 m$)$. The coefficients of erodibility of the soils at these depths are estimated as $120,65,62$ and $10 \mathrm{~mm}^{3}(\mathrm{~N}-\mathrm{s})^{-1}$, respectively using the two empirical equations.

The inputs for the model include both the geometric information and soil parameters of the dam. The outputs are the breaching parameters (e.g. instantaneous breach size, breaching time, water level, and outflow rate) during the breaching process. The peak outflow rate and the breaching time in stage 2 are predicted as $14700 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ and 14.5 h , respectively. Peng and Zhang (2012c) showed that the predicted peak outflow rate $\left(Q_{\mathrm{p}}\right)$ and breaching time $\left(T_{\mathrm{b}}\right)$ can be simulated as lognormal distributions. The standard deviations of $\ln \left(Q_{\mathrm{p}}\right)$ and $\ln \left(T_{\mathrm{b}}\right)$ are 0.53 and 0.40 , respectively. Therefore, in stage $2, \ln \left(Q_{\mathrm{p}}\right)$ and $\ln \left(T_{\mathrm{b}}\right)$ are assumed as normal distributions of $N[\ln (14700), 0.53)]$ and $N[\ln (14.5), 0.40]$. It is very tedious to consider $\ln \left(Q_{\mathrm{p}}\right)$ and $\ln \left(T_{\mathrm{b}}\right)$ at infinite continuous states. In this study, $\ln \left(Q_{\mathrm{p}}\right)$ and $\ln \left(T_{\mathrm{b}}\right)$ are discretized into five ranges, corresponding to five scenarios in Table 6. For example, scenario 1 is from $-\infty$ to $(\mu-1.5 \sigma)$, where $\mu=\ln (14700)$ and $\sigma=0.53$. The probability of this range is 0.067 for a normal variate. The median $\left[P\left(Q_{P}<\right.\right.$ median $)=$ 0.5 ] of this range is $e^{(\mu-1.83 \sigma)}=5570 \mathrm{~m}^{3} \mathrm{~s}^{-1}$, which is used as a representative value for this range. Similarly, the corresponding values of the other ranges are shown in Table 6. Figure 10 shows the outflow rate curves for the five scenarios.

HEC-RAS 4.0 is used to simulate the flood routing process in stage 2, and the results are shown in Table 6. Without the construction of the diversion channel in stage 2, Beichuan would be seriously flooded in all five scenarios. The predicted flood of $14700 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ in scenario 3 would inundate the entire Beichuan Town with a maximum water depth of 12.1 m . Mianyang would not be flooded in scenarios $1-3$. However, the floods in scenarios 4 and 5, especially scenario

Table 6. Dam-break floods in Beichuan Town and Mianyang City in stage 2.


Note: $\mu$ is the predicted mean; $\sigma$ is the predicted standard deviation.

Table 7. Dam-break floods in Beichuan Town and Mianyang City in stage 3.


![img-9.jpeg](img-9.jpeg)

Fig. 10. Outflow rates in the five scenarios of stage 2.

5 , would put a large number of people at risk. The highest water depth in these two scenarios would be 1.8 m and 4.0 m , respectively. The PAR in scenario 5 in stage 2 in Mianyang would be 0.23 million.

### 4.3 Simulation of dam breaching and flood routing in stage 3

Stage 3 starts when the diversion channel has been completed. The diversion channel largely reduced the peak outflow rate during the breaching of Tangjiashan landslide dam. Similar to stage 2, stage 3 is also divided into five scenarios. Table 7 shows the peak outflow rate and breaching time in each scenario. The predicted mean peak outflow rate and

![img-10.jpeg](img-10.jpeg)

Fig. 11. Outflow rates in the five scenarios of stage 3.
mean breaching time are $6540 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ and 16.3 h , respectively, which are close to the recorded values of $6500 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ and 14 h , respectively (Cui et al., 2009; Liu et al., 2010). Figure 11 shows the dam-break outflow rate curves for the five scenarios.

The flood parameters and populations at risk in both Beichuan and Mianyang are shown in Table 7. The PAR in Beichuan increases significantly from scenario 1 to scenario 5. With the predicted mean peak outflow rate, Beichuan would be flooded with a maximum water depth of 6.1 m , which is in good agreement with the observation that the river water level rose to the third storey of many buildings according to the wet marks observed by the authors. Mianyang City would not be flooded in any of the scenarios in stage 3, as the maximum flow rate, $13690 \mathrm{~m}^{3} \mathrm{~s}^{-1}$, is smaller than the design flow rate of $14500 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ for the city (Liu, 2008).

## 5 Evaluation of flood consequences

The flood consequences include evacuation costs, flood damage and loss of life. The flood consequences are closely related to the evacuation rate, sheltering rate and loss of life, which are estimated using a human risk analysis model (HURAM) based on Bayesian networks (Peng and Zhang, 2012a, b). The methodology of evaluating flood consequences, which is coded in Microsoft Excel, has been introduced in the companion paper (Peng and Zhang, 2013). A human life is monetized according to macro-economic contributions. In this section the consequences of the Tangjiashan landslide dam failure will be evaluated.

### 5.1 Methodology

The evaluation of flood consequences in Beichuan in stage 1 is taken as an example to illustrate the analysis methodology. In the medium erodibility case with a peak outflow rate of $7100 \mathrm{~m}^{3} \mathrm{~s}^{-1}$, the inputs for HURAM (Peng and Zhang, 2012a, b) are listed in Fig. 12 for five subareas (S1-S5). In this case, the maximum water depth of 6.13 m occurs in subarea 5 . The probabilities of evacuation, sheltering and loss of
![img-11.jpeg](img-11.jpeg)

Fig. 12. Evaluation of flood consequences in Beichuan Town in the medium erodibility case in stage 1 .
life at a warning time of zero, calculated with HURAM, are shown in Fig. 12. For example, the evacuation rate is 0.208 in subarea 1. As the buildings in this subarea are all threestorey brick structures, they are just slightly damaged and can serve as shelters. The ratios of the people unsheltered, on the second floor and on the third floor are $19.3 \%, 11.1 \%$ and $69.6 \%$, respectively. Since the water depth is $0-1.5 \mathrm{~m}$ in this subarea, the people on the second and third floors are in the safe zone. The fatality ratio in this subarea is $0.02 \%$ and the expected loss of life is 1.12 if without any warning.

Given the sheltering rate, evacuation rate and fatality rate, the flood consequences can be estimated based on the methods presented in the companion paper. The evacuation costs include arrangement fees $\left(C_{t}\right)$ and GDP interruption $\left(C_{\mathrm{GDP}}\right)$. The flood damage $(D)$ is limited to the moveable properties in this study. The moveable properties are generally proportional to the number of people who have neither evacuated nor sheltered in safe zones. The monetized loss of life is calculated as
$V_{\mathrm{L}}=(\mathrm{LOL})\left(\mathrm{GDP}_{\mathrm{p}}\right) L$,
where LOL is the predicted loss of life; $\mathrm{GDP}_{\mathrm{p}}$ is the annual gross domestic product per person; and $L$ is the average longevity ( 75 yr ). LOL is 1.12 in subarea 1 in Fig. 12; hence $V_{\mathrm{L}}$ for subarea 1 is calculated in RMB as $V_{\mathrm{L}}=1.12 \times$ $13745 \times 75=1154580$.

In addition to the medium erodibility scenario, two other scenarios (low erodibility and high erodibility) are also involved in stage 1 . The probabilities of low, medium and high erodibility are $0.116,0.596$ and 0.288 , respectively as shown in Table 5. Therefore, the flood consequence (FC) in stage 1

![img-12.jpeg](img-12.jpeg)

Fig. 13. Flood consequences in Beichuan Town: (a) stage 1; (b) stage 2; (c) stage 3.
is the weighted sum of those of the three scenarios:
$\mathrm{FC}_{1}=0.116 \mathrm{FC}_{\mathrm{L}}+0.596 \mathrm{FC}_{\mathrm{M}}+0.288 \mathrm{FC}_{\mathrm{H}}$.
where $\mathrm{FC}_{\mathrm{L}}, \mathrm{FC}_{\mathrm{M}}$ and $\mathrm{FC}_{\mathrm{H}}$ are the flood consequences in the low, medium and high erodibility cases, respectively.

Similarly, the flood consequences in stages 2 and 3 are also the weighted sum of those of the five scenarios and given by

$$
\begin{aligned}
\mathrm{FC}_{i} & =0.067 \mathrm{FC}_{i 1}+0.242 \mathrm{FC}_{i 2}+0.382 \mathrm{FC}_{i 3} \\
& +0.242 \mathrm{FC}_{i 4}+0.067 \mathrm{FC}_{i 5}, \quad i=2,3
\end{aligned}
$$

in which the five coefficients are the probabilities of the five scenarios in Tables 6 and 7.

### 5.2 Calculated dam-break flood consequences

With the methods introduced above, the flood consequences as functions of warning time in Beichuan Town and Mianyang City are presented in Figs. 13 and 14, respectively. In Beichuan Town (Fig. 13), the flood severities in the three
![img-13.jpeg](img-13.jpeg)

Fig. 14. Flood consequences in Mianyang City: (a) stage 1; (b) stage 2. No flooding is predicted in stage 3.
stages are very high. The monetized loss of life dominates when the warning time is short. This is reasonable as human life is the first concern upon a serious dam-failure. However, if the warning time is relatively long, the evacuation costs would be the largest expenditure. Compared to stage 1, the estimated flood consequences in stage 2 are much larger. In stage 2 , the erodibility of the top soil layer of the dam is very high $\left(120 \mathrm{~mm}^{3}(\mathrm{~N}-\mathrm{s})^{-1}\right)$. The rapid erosion of this soil layer would cause a larger peak outflow rate and a shorter breaching time. With the diversion channel built in stage 3, the flood consequences would be smaller. The monetized potential loss of life with zero warning time is RMB 3674 million ( 3564 fatalities) in stage 3, compared to RMB 4928 million ( 4780 fatalities) in stage 1 and RMB 14904 million ( 14458 fatalities) in stage 2. The larger number of fatalities in stage 2 is due to two reasons: the higher flood severity (water depth and flow velocity) and the shorter flood rise time. The flood rise time is closely related to the breaching time and flood water depth as shown in Tables 5-7.

In Mianyang City (Fig. 14), no flooding is predicted in stage 3 and no evacuation is needed. In stages 1 and 2, the flood damage and evacuation costs are much larger, but the monetized loss of life is much smaller than that of Beichuan Town with the same warning time. The reason is that the number of PAR in Mianyang City is much larger, but the flood severity is much lower than that in Beichuan Town. The larger number of PAR would cause more evacuation costs and flood damage. However, as the values of the maximum

![img-14.jpeg](img-14.jpeg)

Fig. 15. The probability of dam-break flood in Beichuan as a discrete time series at an interval of one hour in stage 1 (with a breach formation time of three days).
water depth and flow velocity in Mianyang City are much smaller than those in Beichuan as shown in Tables 5 and 6, the fatality rates in Mianyang City are much lower. In fact, the maximum water depth is much lower than the brick structures with three and more storeys, the people in Mianyang can take refuge in the buildings, which is simulated as sheltering in HURAM.

## 6 Dynamic decision making

### 6.1 Methodology

In this study, the decision for the Tangjiashan landslide dam break is divided into three stages with different levels of information. Figure 8 shows the probabilities of dam failure in the three stages. There is still quite some time from the moment of $V_{t}$ reaching $V_{\mathrm{cr}}$ to the start of breaching, which is called the breach initiation time. As few data are available to predict the breaching initiation time and the corresponding uncertainties, a constant value of 72 h is selected based on the records of the breaching process (Chang and Zhang, 2010; Peng and Zhang, 2012a, b). This means that the dam starts to breach three days after the water level reaches the dam crest.

In order to demonstrate the method of decision making, the flood in Beichuan Town in stage 1 is taken as an example. Figure 15 shows the probability of dam break in Beichuan as a discrete time series with an interval of one hour. The studied time range is set between $t_{0}$ of 00:00 on 14 May and $t_{\text {end }}$ or $t_{360}$ of 00:00 on 29 May. The predicted dam-failure probability outside of this range is very small $\left(3.2 \times 10^{-5}\right)$. Theoretically, a dam would fail at any time in this range. Let us assume that the dam-break flood arrives at $t_{\mathrm{f}}$ and the warning is issued at $t_{\mathrm{w}}$. The flood consequences with any $t_{\mathrm{w}}$ in this range can be obtained with the method presented in the companion paper (Peng and Zhang, 2013). For example, assuming $t_{\mathrm{w}}$ is at 00:00 on 17 May, then $t_{\mathrm{w}}=t_{72}$. The total
flood consequence is given by

$$
\begin{aligned}
E\left(L_{t}\right) & =\sum_{j=0}^{360} L\left(t_{j}\right) P_{D}\left(t_{j}\right) \\
& =\sum_{j=0}^{360}\left[C\left(W_{t}\right)+D\left(W_{t}\right)+L\left(W_{t}\right)\right] P_{D}\left(t_{j}\right) \\
& =\sum_{j=0}^{360} C\left(W_{t}\right) P_{D}\left(t_{j}\right)+\sum_{j=0}^{360}\left[D\left(W_{t}\right)+L\left(W_{t}\right)\right] P_{D}\left(t_{j}\right)
\end{aligned}
$$

where $C\left(W_{t}\right), D\left(W_{t}\right)$ and $L\left(W_{t}\right)$ are the evacuation costs, flood damage and monetized loss of life as functions of warning time $\left(W_{t}\right)$, which can be found in Fig. 13; $P_{D}\left(t_{j}\right)$ is the flood probability in the duration of $t_{j-1}$ to $t_{j}$, which is expressed in Fig. 15. Therefore, the optimal time to evacuate the PAR is the time to achieve the minimum total loss $\left[\operatorname{Min}\left(E\left(L_{t}\right)\right)\right]$ in Eq. (15).

### 6.2 Dynamic decision making in the three stages

Figures 13 and 14 show the expected flood consequences as functions of the time to evacuate the PAR in Beichuan Town and Mianyang City, respectively. The evacuation costs decrease, but the flood damage and monetized loss of life increase with delayed time for evacuation. The expected total consequence decreases first and then increases. Therefore, an optimum decision time can be obtained corresponding to the minimum expected total loss (MTC).

In Beichuan Town, the optimal decision and flood consequences are shown in Table 8. The optimum evacuation time is at 08:00 on 16 June in stage 1, when the MTC is RMB 41.93 million. The optimum time is brought forward 14 h in stage 2 with an MTC of RMB 41.60 million. In stage 3 , as the diversion channel has been constructed, the dam crest elevation is reduced by 12 m . The optimum time to evacuate the PAR is at 00:00 on 7 June, when the MTC is RMB 36.20 million. The 8-9 day difference between stage 3 and stages 1 and 2 is due to the reduced reservoir capacity ( 69 million $\mathrm{m}^{3}$ ) in stage 3 . It takes $8-9$ days to fill this part of lake. As shown in Fig. 16, the expected total loss increases rapidly about a half-day after the optimum time because of the increase of monetized loss of life with later warning. Generally, an evacuation is not avoidable in all three stages for Beichuan. The optimum times for evacuating the PAR, as shown in Fig. 16, may be brought forward a certain period for convenience (e.g. at daytime) since the sensitivity is not high.

In Mianyang City, the optimal decision and flood consequences are shown in Table 8. Since there is no predicted flooding in stage 3, which is a fact, no evacuation is needed. In stage 1 as shown in Fig. 17, the optimum time for evacuating the PAR is set at 10:00 on 19 June with an expected minimum total consequence of RMB 370 million. Like in Beichuan, the optimum time is brought forward 16 h in stage 2

Table 8. The optimal decision and flood consequences in Beichuan Town.


Note*: The crest elevation in stages 1 and 2 was the natural crest elevation before the excavation of the diversion channel.

Table 9. The optimal decision and flood consequences in Mianyang City.


Note*: The crest elevation in stages 1 and 2 was the natural crest elevation before the excavation of the diversion channel.
with an MTC of RMB 381 million. The MTC is more sensitive to the time for evacuating the PAR than that in Beichuan. The optimum times for evacuating the PAR in Mianyang are $2-3$ days later than those in Beichuan. There are three reasons for this: (1) the probabilities of the floods in both stages 1 and 2 in Beichuan are very large, but the probabilities of the floods in Mianyang are much smaller (i.e. 0.12 in stage 1 and 0.31 in stage 2 ); (2) the higher flood severity in Beichuan needs more warning time for evacuation, while the people in Mianyang can take refuge in high-rise buildings instead; (3) the flood rise time in Mianyang is much longer, and a certain time is needed for the flood to travel 85 km from Beichuan to Mianyang. There is a trend of convergence of the monetized loss of life, flood damage and total consequences in both stages in Mianyang City. This is because there are limits in the maximum loss of life, flood damage and total consequence even when no evacuation is implemented.

According to Sina News (2008a, b) and Gov.cn (2008), the government organized evacuation exercises in areas downstream of the dam on 27 May 2008. The formal evacuation instruction was issued at 16:00 on 30 May 2008. More than 0.2 million people were evacuated from Mianyang City, Beichuan and other towns by 20:00 on 31 May, 10 days before the start of the breaching. The evacuated people were not allowed to go back to home until 11 June when the flow rate at the dam site was smaller than $300 \mathrm{~m}^{3} \mathrm{~s}^{-1}$. The people in both Beichuan and Mianyang were evacuated earlier than the optimal times suggested in this study. In Beichuan, the earlier evacuation would not incur much expense since a serious flood was not avoidable and the population at risk
was relatively small. In Mianyang, nearly 200000 people had been evacuated for 12 days, but no extraordinary flood actually occurred in this city. An early evacuation decision was made for two main reasons: (1) the government considered possible political and societal impacts of the flood and put human life at the highest priority; (2) a higher flood severity with a peak discharge of $33770 \mathrm{~m}^{3} \mathrm{~s}^{-1}$ was predicted based on experiences of man-made soil and rockfill dams (Huang et al., 2008). The study of Peng and Zhang (2012c) shows that direct application of empirical models for man-made earth and rockfill dams to landslide dams would, on average, overestimate the breach size by more than $60 \%$ and the peak outflow rate by approximately $200 \%$, and underestimate the breaching duration by approximately $50 \%$. DYDEM helps on a rational decision in the Tangjiashan landslide case. However, DYDEM may offer little help on the decision with a short-lived landslide dam (Dong et al., 2011). In such a case, an immediate decision is needed on evacuation of the PAR.

## 7 Discussions

### 7.1 The influence of the value of a human life

In this study, a value of the macro-economic contribution of a person is used to monetize a human life. One may argue that the value is too low or too high for decision making. Therefore, the influence of value of life to the final decision making is discussed here. If the value of life becomes higher, the minimum expected total consequences (MTC) in Figs. 16 and 17 would be larger than the present values. The curve

![img-15.jpeg](img-15.jpeg)

Fig. 16. Optimal decision making for Beichuan Town: (a) stage 1; (b) stage 2; (c) stage 3.
of the monetized loss of life would increase more rapidly and meet the evacuation costs earlier. Therefore, an earlier evacuation with a higher MTC is needed if the value of life is higher, and vice versa. If political or societal influences are involved, which puts saving a life on the highest priority, new criteria should be used. In this case, the human risk should be first reduced to a certain degree before considering money issues.

### 7.2 The influence of failure modes

Only overtopping failure is considered in this study as most failed landslide dams ( $92 \%$ ) were overtopped. Other failure modes such as slope failure and piping may influence the final decision. Slope failures are mass soil movements on either upstream or downstream side of a dam. A slope failure reduces the soil thickness and, in some cases, the crest height of the dam. A slope failure by itself may not result in flooding, but it can affect the future ability of a dam to perform as intended. An earlier dam breaching with a higher
![img-16.jpeg](img-16.jpeg)

Fig. 17. Optimal decision making for Mianyang City: (a) stage 1; (b) stage 2 (No flooding is predicted in stage 3).
peak outflow rate would happen if a slope failure occurs, and hence an earlier evacuation warning should be issued with more MTC. However, as landslide dams are caused by rapid deposition of landslide debris materials, the slopes on both upstream and downstream sides are relatively gentle and the secondary slope failure is less likely. Statistical data show that only 2 landslide dams ( $1 \%$ ) are recorded with slope failures. Like the slope failure, piping failure may lead to an earlier failure and hence an earlier evacuation warning as it may occur before the water level reaches the dam crest. Few landslide dams failed in piping ( 12 cases, $7 \%$ of all failures) as a large ratio of dam width and dam height often leads to a small hydraulic gradient.

### 7.3 The sensitivity of the minimum expected total consequence

In this study, the MTC is not very sensitive to the warning time before the optimal time in Beichuan and the evacuation may be brought forward for safety. However, in Mianyang the MTC is much more sensitive to the warning time than that in Beichuan and should be considered carefully. Several factors influence the sensitivity. The number of the PAR is a main factor since the evacuation cost, which is related to the

PAR, dominates the MTC before the optimal time of evacuation. The flood severity is another factor as it directly influences the flood damage and loss of life. If the flood severity in Beichuan were not so high, the MTC would not increase so fast over time. Then the time of evacuation could be delayed from the optimal time since it would not cost much more. The probability of flood is also a very important factor as it is also highly related to the expected flood damage and loss of life. Other factors (e.g. dam parameters, hydraulic parameters, city size, and building characteristics) that affect the PAR, the flood severity or the flood probability also indirectly influence the sensitivity of MTC.

## 8 Conclusions

Dynamic decision making for the emergency management of Tangjiashan landslide dam is analyzed with DYDEM. The following conclusions can be drawn:

1. The timeline of the Tangjiashan landslide dam failure event is presented in three stages with different levels of hydrological, geological and social-economic information. Only geometric data are available in stage 1; geometric, geologic and hydrological parameters are obtained in stages 2 and 3; a diversion channel has been constructed in stage 3.
2. The hydraulic parameters, such as inflow rate and lake volume, are forecasted using a time series analysis method. The results are checked through a $\chi^{2}$ goodness-of-fit test. The probability of dam failure is obtained with the predicted means and standard deviations of the lake volume as a time series.
3. The dam breaching parameters, such as peak outflow rate and breaching time, are predicted with a set of empirical models in stage 1 without soil property information, and a physical model (DABA) in stages 2 and 3 when more geotechnical information is available. The uncertainties of the breaching parameters are studied based on statistical data. The flood routing in these three stages is simulated with HEC-RAS, from which the hydraulic parameters and the PAR in Beichuan Town and Mianyang City are obtained. Beichuan suffers serious flooding in all three stages. Mianyang is not flooded in stage 3, but the maximum PARs in stages 1 and 2 are 0.21 and 0.23 million, respectively.
4. The flood consequences, including evacuation costs, flood damage and monetized loss of life, are evaluated with HURAM. The evacuation costs increase and the flood damage and monetized loss of life decrease with the increase of warning time. The monetized loss of life dominates when the warning time is short, which reduces rapidly with more available warning time. In Mianyang City, the evacuation costs and flood damage are
larger, but the monetized loss of life is less than that in Beichuan. The reason is that the PAR in Mianyang is much larger but the flood severity is much lower.
5. Dynamic decision making analysis is conducted to find the optimal time for evacuating the PAR with minimum total loss and update the decision with new information. In Beichuan Town, the optimal time for evacuating the PAR is brought forward 8-9 days because of the construction of the diversion channel. The minimum expected total consequences in these three stages do not vary significantly, as they are dominated by the evacuation costs. In Mianyang, no evacuation is needed in stage 3 as no flooding is predicted. The optimum times for evacuating the PAR in stage 1 and 2 in Mianyang are 2-3 days behind those for Beichuan. The expected minimum total consequence in Mianyang is much larger than that in Beichuan due to the larger number of PAR.
6. The framework of dynamic decision making takes the dam-failure probability as a time series and flood consequences as functions of warning time. It sets a criterion for making an evacuation decision and updates the decision with new information when delayed decision is chosen. The application of DYDEM is not limited to dam-break floods; it may be applicable to emergency management of other disasters with a certain lead time, such as levee breaks, flash floods, hurricanes, tsunamis and landslides.

## Appendix A

According to the method introduced in the companion paper (Peng and Zhang, 2013), autocorrelation function $\rho_{k}$ and partial autocorrelation function $\varphi_{k k}$ of time series $x_{t}$ are shown in Table A1. Since $\rho_{k}$ does not fall off slowly with the increase of $k$ and the dataset in Fig. 5 shows a stationary trend, a stationary model is suggested (Box et al., 2008). As the current daily inflow into the reservoir is closely related to the inflow values on the previous days according to the river confluence theory (Nash, 1957), an autoregressive model $\operatorname{AR}(p)$ or $\operatorname{ARMA}(p, q)$ is suggested, in which the current daily inflow is expressed as the weighted sum of the previous daily inflow values. Since the partial autocorrelation function, $\varphi_{k k}$, has a cutoff after lag 2 as shown in Table A1, the time series is identified to follow an autoregressive model $\operatorname{AR}(2)$ according to the rules in the companion paper (Peng and Zhang, 2013):
$x_{t}=\varphi_{1} x_{t-1}+\varphi_{2} x_{t-2}+a_{t}$,
where $\varphi_{1}$ and $\varphi_{2}$ are coefficients; the random shock $a_{t}$ is an independent and identical time series with a mean of zero, which is often set as a normal distribution $N\left(0, \sigma^{2}\right)$. The assumption of $\operatorname{AR}(2)$ will be tested later.

Table A1. The autocorrelation function and partial autocorrelation function for time series $Q_{t}$.


Table A2. The autocorrelation function for $a_{t}$ in time series $Q_{t}$.


Table A3. The $\psi$ weights for time series $Q_{t}$ in stage 1.


Note:* The $\psi$ weights are neglected as they are too small.

The error of time series $\operatorname{AR}(2)$ is given by
$a_{t}=x_{t}-\varphi_{1} x_{t-1}-\varphi_{2} x_{t-2}$.
The least squares method is used to find parameters $\varphi_{i}$ and $\theta_{i}$ for achieving the least sum of the squares of $a_{t}$ :
$\operatorname{Min}\left[\sum_{t=1}^{n} a_{t}^{2}\left(\varphi_{i}, \theta_{i}\right)\right], \quad i=1,2, \ldots, n)$.
By using the solver in Microsoft Excel with the data in Table 3 , we find $\varphi_{1}=0.463$ and $\varphi_{2}=-0.181$. Therefore, time series $x_{t}$ is expressed as
$x_{t}=0.463 x_{t-1}-0.181 x_{t-2}+a_{t}$.
According to Box et al. (2008), the assumption of $\operatorname{AR}(2)$ for inflow rate $x_{t}$ is tested by checking whether $33 \sum_{k=1}^{7}\left[\rho_{k}^{*}(a)\right]^{2}$ follows a $\chi^{2}(5)$ distribution. Here $\rho_{k}^{*}(a)$ is the estimated autocorrelation function of $a_{t}$. The $10 \%$ and $5 \%$ quantile points for $\chi^{2}(5)$ are 9.24 and 11.1 , respectively. As 4.46 in Table A2 is smaller than either 9.24 or 11.1, the model of $\operatorname{AR}(2)$ as Eq. (A4) cannot be refused.

As the expected value of $a_{t}$ is zero, the inflow rate with a lead time $l$ at time $t$ can be calculated by
$x_{t}^{*}(1)=0.463 x_{t}-0.181 x_{t-1}$
$x_{t}^{*}(2)=0.463 x_{t}^{*}(1)-0.181 x_{t-1}$
$x_{t}^{*}(l)=0.463 x_{t}^{*}(l-1)-0.181 x_{t}^{*}(l-2), l=3,4, \ldots$
where $x_{t}$ is the recorded value; $x_{t}^{*}(l)$ is the predicted mean value of the inflow rate with a lead time of $l, x_{t+l}$.

In order to obtain the standard deviation of the predicted value $x_{t}^{*}(l)$, we express Eq. (A1) in a random shock form of
an infinite series:

$$
\begin{aligned}
x_{t} & =a_{t}+\psi_{1} a_{t-1}+\psi_{2} a_{t-2}+\psi_{3} a_{t-3} \cdots \\
& =a_{t}+\sum_{j=1}^{\infty} \psi_{j} a_{j}
\end{aligned}
$$

where the coefficients can be obtained by substituting Eq. (A6) into Eq. (A2) and comparing the coefficients of $a_{t}$ (Box et al., 2008). As $a_{t}$ is an identically distributed stochastic process of $N\left(0, \sigma_{a}^{2}\right)$, the standard deviation of $x_{t}$ is calculated as (Box et al., 2008)
$\sigma^{2}\left[x_{t}(l)\right]=\left(1+\psi_{1}^{2}+\psi_{2}^{2}+\ldots+\psi_{l-1}^{2}\right) \sigma_{a}^{2}$
where the $\psi$ weights $\left(\psi_{l}\right)$ are shown in Table A3 according to the methods in the companion paper (Peng and Zhang, 2013), and $\sigma_{a}$ is estimated as
$\sigma_{a}^{2}=\frac{1}{33-1} \sum_{1}^{33} a_{t}^{2}=312.5$
in which $a_{t}$ is calculated using Eq. (A2).

Acknowledgements. The research reported in this paper was substantially supported by the Natural Science Foundation of China (No. 51129902) and the National Basic Research Program (973 Program) (No. 2011CB013506). The authors are grateful to David Keefer of the US Geological Survey and Jia-Jyun Dong of National Central University in Taiwan for their valuable suggestions during the preparation of this paper.

Edited by: D. Keefer
Reviewed by: J.-J. Dong and one anonymous referee
