Nat. Hazards Earth Syst. Sci., 13, 425-437, 2013
www.nat-hazards-earth-syst-sci.net/13/425/2013/
doi:10.5194/nhess-13-425-2013
(c) Author(s) 2013. CC Attribution 3.0 License.

Natural Hazards and Earth System Sciences

# Dynamic decision making for dam-break emergency management - Part 1: Theoretical framework 

M. Peng ${ }^{1,2}$ and L. M. Zhang ${ }^{1}$<br>${ }^{1}$ Department of Civil and Environmental Engineering, The Hong Kong University of Science and Technology, Hong Kong<br>${ }^{2}$ Key Laboratory of Geotechnical and Underground Engineering of Ministry of Education, Department of Geotechnical Engineering, Tongji University, Shanghai, China

Correspondence to: L. M. Zhang (cezhangl@ust.hk)
Received: 26 March 2012 - Published in Nat. Hazards Earth Syst. Sci. Discuss.: -
Revised: 10 December 2012 - Accepted: 15 December 2012 - Published: 18 February 2013


#### Abstract

An evacuation decision for dam breaks is a very serious issue. A late decision may lead to loss of lives and properties, but a very early evacuation will incur unnecessary expenses. This paper presents a risk-based framework of dynamic decision making for dam-break emergency management (DYDEM). The dam-break emergency management in both time scale and space scale is introduced first to define the dynamic decision problem. The probability of dam failure is taken as a stochastic process and estimated using a time-series analysis method. The flood consequences are taken as functions of warning time and evaluated with a human risk analysis model (HURAM) based on Bayesian networks. A decision criterion is suggested to decide whether to evacuate the population at risk (PAR) or to delay the decision. The optimum time for evacuating the PAR is obtained by minimizing the expected total loss, which integrates the time-related probabilities and flood consequences. When a delayed decision is chosen, the decision making can be updated with available new information. A specific dam-break case study is presented in a companion paper to illustrate the application of this framework to complex dam-breaching problems.


## 1 Introduction

Dam breaks can cause catastrophic consequences to human beings. Past dam failure disasters have shown that flood risks are directly related to the available warning time (the period from issuing evacuation warning to the arrival moment of a flood) for evacuation. Despite the benefits of saving human
life and properties, an evacuation decision should be treated as a very serious issue since it often incurs a large amount of economic expense at the same time (Frieser, 2004). Before making an evacuation decision, two problems need to be considered. Is it necessary to evacuate the population at risk (PAR)? If yes, then when is the optimal time to evacuate the PAR? The answers to these problems raise the need for proper decision-making based on dynamic risk analysis that considers time effects.

Generally, there are two categories of methods of decision making for emergency management: deterministic methods and probabilistic methods. Deterministic methods are those based on deterministic analysis, experiences and judgment without explicit consideration of uncertainties. In deterministic methods, some critical values (e.g. water level, period return flood) are often suggested as indices for evacuation decision-making (Nielsen et al., 1994; Frieser, 2004). Some guidelines also offer recommendations for decision-making based on judgments (Urbina and Wolshon, 2003; FEMA, 2004). Deterministic methods are simple to apply. However, they may not be reasonable as the uncertainties are not studied.

There are many uncertainties in both the occurrence and consequences of dam breaks, especially for landslide dam failures. Landslide dams are formed by rapid deposition of massive rocks and soils, in which both the geometrical and mechanical parameters are uncertain. Therefore, probabilistic decision methods are more realistic. BC Hydro (1993), USBR (1997) and ANCOLD (1998) published life-safety criteria for dam safety decision making by considering the relationship of dam failure probability and fatality. Decision

Table 1. Flood consequences


trees have been frequently used to conduct quantitatively risk-based decision making in mitigation of various disasters (Frieser, 2004; Smith et al., 2006; Lindell et al., 2007; Woo, 2008; Liu, 2009). Frieser (2004) and Smith et al. (2006) commented that the evacuation decision for floods can be delayed in cases with long prediction lead time and large uncertainties. Figure 1 shows a delayed decision tree for a flood disaster. The flood consequences include evacuation costs $(C)$, flood damage $(D)$, and loss of life $(L)$ as shown in Table 1. Evacuation costs include initial costs (e.g. costs of transport, accommodation, food supply, organization and service), interruption of gross domestic product (GDP) due to evacuation, and indirect influences (e.g. influence of the market in the affected areas). The evacuation costs increase with the warning time. The indirect influences are difficult to evaluate and not included in this study. Flood damages include all the consequences caused by flooding except those to human life. Some moveable properties such as cars and portable items can be saved by evacuation. However, immoveable properties such as houses, GDP interruption and environmental damage cannot be reduced by evacuation. Therefore, those are not involved in this study. Loss of life is the fatality caused by flooding. Historical data show that the fatality rate can be largely reduced by allowing more warning time (DeKay and McClelland, 1993; Graham, 1999).

The evacuation may be delayed (e.g. $t_{\mathrm{w}}$ in Fig. 1) to obtain information with less uncertainty and to reduce the evacuation costs $\left(C_{1}<C_{2}\right)$, as shown in Fig. 1. As more information is collected, the uncertainty in the dam failure probability, $P_{1}$, with a delayed decision is smaller than that in $P_{2}$ in Fig. 1. However, such delayed evacuation runs the risk of losing more lives $\left(L_{1}>l_{1}>l_{2}\right)$ and properties $\left(D_{1}>\right.$ $d_{1}>d_{2}$ ) given less available time for evacuation. A good decision should try to attain a minimum expected total loss. Time-dependent evacuation decision can be analyzed using a multi-phase decision tree (Frieser, 2004; Smith et al., 2006). The probabilistic methods using decision trees are superior to deterministic methods due to the inclusion of uncertainties.

A premise of using a decision tree in the existing methods is to assume a predicted time of flooding, $t_{\mathrm{f}}$, as shown in
![img-0.jpeg](img-0.jpeg)

Fig. 1. Decision tree for dam-break emergency management (modified from Frieser, 2004).

Fig. 1. Normally, $t_{\mathrm{f}}$ is set as a target time (e.g. with enough lead time to evacuate the people) or the time of the worst predicted situation (e.g. the highest water level or largest flood flow rate). This may not be reasonable due to the fact that a dam-break flood may occur at any future time. Therefore, decision trees may not be sufficient for dynamic decision making, since the predicted flood probability should be a stochastic process instead. The loss of life and properties could be underestimated if the flood occurs before the predicted time, and vice versa.

This paper presents a new framework of dynamic decision making for dam-break emergency management (DYDEM) in both time scale and space scale. The probability of dam failure is taken as a stochastic process and estimated using a time-series analysis method. The consequences are taken as functions of warning time and evaluated with a human risk analysis model (HURAM) using Bayesian networks (Peng and Zhang, 2012a, b). A decision criterion is suggested to decide whether to evacuate the population at risk (PAR) or to delay the decision. The optimum time for evacuating the PAR is obtained by minimizing the expected total loss. Finally, a comparison between two existing methods and the new framework is made to show the features of this framework. A specific dam-break case study is presented in a companion paper (Peng and Zhang, 2013) to illustrate the application

![img-1.jpeg](img-1.jpeg)

Fig. 2. Schematic of the dam breaching and warning time.
of this framework to complex dam-breaching problems. HURAM simulates the evacuation, sheltering and loss of life in a flood event, which are closely related to the evacuation cost, flood damage and number of fatalities in this paper. DYDEM in this paper focuses on dynamic decision making for dambreak emergency management.

## 2 Dam-break emergency management

Dam-break emergency management is aimed to minimize the possible dam-break consequences using primarily nonstructural measures, such as warning, sheltering and evacuation. This section presents the dam-break emergency management in both time and space scale to define the dynamic decision making problems.

### 2.1 In time scale

The prediction lead time (i.e. the duration between the prediction moment and the predicted failure time) of a dambreak flood is usually on the order of hours or days. During this period emergency management can possibly be implemented to save human lives and properties. The studied time includes available time and demand time. The available time is influenced by the dam breaching and flood routing processes. The concepts of breaching and warning time are shown in Fig. 2. The demand time for emergency management can be divided into four phases: (1) hydrological forecasting, risk assessment and decision making; (2) warning; (3) response; and (4) evacuation and sheltering (Frieser, 2004), as shown in Fig. 3.

Emergency management starts from the identification of signs of dam break (e.g. the water level rises to the crest or cracks in the dam) (Fig. 3). Risk assessment, based on the hydrological forecasting, must be conducted before the evacuation decision making in phase 1. The government must decide the optimal time to evacuate the population at risk (PAR) if evacuation is finally chosen. It takes time to transmit warning messages in phase 2. An S-curve for the PAR warned and the progress of warning is shown in Fig. 3. The warning transmitting time is defined as the duration between issuing the warning and the receipt of it. Phase 3 starts at the receipt
![img-2.jpeg](img-2.jpeg)

Fig. 3. Emergency management of dam breaks in time scale (modified from Frieser, 2004).
of warning messages by the PAR. The PAR needs time to confirm the warning messages, prepare for evacuation and wait for family members. A part of the PAR may evacuate to safe places as shown in phase 4 of Fig. 3. The rest, either refusing to evacuate or having insufficient time, may try to shelter themselves in relatively safe places (e.g. high rise buildings) in the flooded areas. After the possible occurrence of the disaster, people may flee for safe havens. Some of these might lose their lives, however.

The dam-break emergency management in time scale displays the sequence of human activities and the population distributions with time before the flood occurrence. A good decision should consider not only the available time before the predicted arrival of the flood, but also the demand time for each phase and the corresponding population distribution.

### 2.2 In space scale

The risk analysis of a dam-break event covers a large area along the river from the catchment upstream of the dam to the potential flood areas downstream of the dam. In space scale (Fig. 4), the dam-break emergency management includes five steps: hydraulic parameter forecasting, dam-break probability evaluation, dam breaching simulation, flood routing simulation and flood consequence evaluation.

Hydraulic parameters such as reservoir volume, inflow rate and water elevation directly influence the dam safety conditions. These parameters should be treated as stochastic processes instead of independent random variables due to the correlations in time scale.

Failure mode is a key parameter for dam-break probability analysis. Most dam failures are caused by either overtopping or piping, with corresponding percentages of $56.0 \%$ and $35.7 \%$, respectively for man-made earth and rockfill dams (Xu and Zhang, 2009; Zhang et al., 2009), and $91 \%$ and $8 \%$, respectively for landslide dams (Peng and Zhang, 2012c). Since this study focuses on decision making, only the overtopping failure mode is considered, which usually suffices for breached landslide dams. Overtopping occurs when the

![img-3.jpeg](img-3.jpeg)

Fig. 4. Emergency management of dam breaks in space scale.
reservoir water elevation exceeds the elevation of the dam crest. The probability of dam failure is closely related to hydrological parameters.

The next two components are to simulate the dam breaching process and flood routing downstream of the dam. The breaching parameters significantly affect the flood consequence downstream. In this study, an empirical model (Peng and Zhang, 2012c) based on statistical data is used to simulate the breaching process when only geometrical parameters are available, while a physical model, DABA (Chang and Zhang, 2010), is used when more soil properties are available (e.g. cohesion and friction angle). The outputs of the breaching simulation are peak outflow rate, breaching time and breach size. With the breaching parameters predicted, a river analysis program, HEC-RAS 4.0, developed by Hydrologic Engineering Center (2008), is used to simulate the flood routing in the river downstream of the dam. Detailed simulations in a specific case will be introduced in the companion paper (Peng and Zhang, 2013).

The flood consequences, including evacuation costs, flood damage and loss of life as shown in Fig. 1, are highly related to the warning time. Generally, evacuation costs increase and flood damage and loss of life decrease with more warning time. The dam-break emergency management should cover the evolution of the dam-break event in space scale. A proper decision should take the dam-break probability as a time series and the consequences as functions of warning time.

## 3 Framework of dynamic decision making

The framework of dynamic decision making is intended to make a decision whether to evacuate the population at risk or to delay the decision; to predict the optimal time to evacuate the PAR with the minimum expected total loss; and to update the decision-making with new information when delayed decision is chosen.

Assume a continuous stochastic process of dam-break probability as shown in Fig. 5. The studied period ranges from $t_{0}$ (e.g. the current time) to $t_{\text {end }}$ (e.g. the moment after which the risk is not considered). The probability of dam failure in a short period $\mathrm{d} t$ is calculated as
![img-4.jpeg](img-4.jpeg)

Fig. 5. Probability of dam-break flood as a continuous stochastic process of time.
$P(t)=f(t) \mathrm{d} t$
where $f(t)$ is a continuous stochastic process of dam failure probability. Given the time of issuing evacuation warning ( $t_{0} \leq t_{\mathrm{w}} \leq t_{\text {end }}$ ) as shown in Fig. 5, the period between $t_{\mathrm{w}}$ and possible flood arrival time $\left(t_{\mathrm{f}}\right)$ is called the warning time $\left(W_{t}\right)$, which is critical for the people at risk to evacuate to safe places. Warning time equals zero if the possible flood occurs before the time for evacuating the PAR. Thus, $W_{t}$ is a non-negative parameter and given by
$W_{t}=0$, when $t_{\mathrm{f}}<t_{\mathrm{w}}$
$W_{t}=t_{\mathrm{f}}-t_{\mathrm{w}}$, when $t_{\mathrm{f}} \geq t_{\mathrm{w}}$
$W_{t}=t_{\text {end }}-t_{\mathrm{w}}$, when $t_{\mathrm{f}} \geq t_{\text {end }}$.
The flood risk, or expected total loss, $E\left(L_{\mathrm{t}}\right)$, is the sum of the expected evacuation costs, flood damage and loss of life, which are obtained by integrating the product of these three categories of consequences and their corresponding probabilities along time:

$$
\begin{aligned}
E\left(L_{\mathrm{t}}\right) & =\int L(t) f(t) \mathrm{d} t \\
& =\int_{t_{0}}^{+\infty}\left[C\left(W_{t}\right)+D\left(W_{t}\right)+L\left(W_{t}\right)\right] f(t) \mathrm{d} t \\
& =\int_{t_{0}}^{+\infty} C\left(W_{t}\right) f(t) \mathrm{d} t+\int_{t_{0}}^{+\infty}\left[D\left(W_{t}\right)+L\left(W_{t}\right)\right] f(t) \mathrm{d} t
\end{aligned}
$$

where $L(t)$ is the flood consequences or total loss; $C\left(W_{t}\right)$, $D\left(W_{t}\right)$ and $L\left(W_{t}\right)$ are the evacuation cost, flood damage, and loss of life as functions of warning time, respectively, which will be presented later in this paper. Considering the definition of $W_{t}$ in Eqs. (2) to (4), Eq. (5) can be separated into two equations:

![img-5.jpeg](img-5.jpeg)

Fig. 6. Probability of dam-break flood as a discrete stochastic process of time.

$$
\begin{aligned}
& \int_{t_{0}}^{+\infty} C\left(W_{t}\right) f(t) \mathrm{d} t=\int_{t_{0}}^{t_{\mathrm{w}}} C(0) f(t) \mathrm{d} t \\
& \quad+\int_{t_{\mathrm{w}}}^{t_{\mathrm{end}}} C\left(t-t_{\mathrm{w}}\right) f(t) \mathrm{d} t+C\left(t_{\mathrm{end}}-t_{\mathrm{w}}\right)\left[1-\int_{t_{0}}^{t_{\mathrm{end}}} f(t) \mathrm{d} t\right] \\
& \int_{t_{0}}^{+\infty}\left[D\left(W_{t}\right)+L\left(W_{t}\right)\right] f(t) \mathrm{d} t=\int_{0}^{t_{\mathrm{w}}}[D(0)+L(0)] f(t) \mathrm{d} t \\
& \quad+\int_{t_{\mathrm{w}}}^{t_{\mathrm{end}}}\left[D\left(t-t_{\mathrm{w}}\right)+L\left(t-t_{\mathrm{w}}\right)\right] f(t) \mathrm{d} t+0
\end{aligned}
$$

The last part of Eq. (6) denotes that evacuation costs incur even if there is no dam failure or if the failure time is beyond the studied period. The last part of Eq. (7) denotes that the flood damage and loss of life are not considered if there is no dam failure in the studied period.

The optimal time to evacuate the PAR is the time to attain the minimum total loss or the time at which the derivative of the following function is zero:
$\operatorname{Min}\left[E\left(L_{\mathrm{t}}\right)\right]$ or $\frac{d E\left(L_{\mathrm{t}}\right)}{\mathrm{d} t_{\mathrm{w}}}=0$

For a discrete time series as shown in Fig. 6, the probability of flooding in the period from $t_{j-1}$ to $t_{j}$ is given by $P\left(t_{j}\right)$. The expected total loss is given by

$$
\begin{aligned}
E\left(L_{\mathrm{t}}\right)= & \sum_{j=1}^{+\infty} L\left(t_{j}\right) P\left(t_{j}\right) \\
& =\sum_{j=1}^{+\infty}\left[C\left(W_{t}\right)+D\left(W_{t}\right)+L\left(W_{t}\right)\right] P\left(t_{j}\right)
\end{aligned}
$$

![img-6.jpeg](img-6.jpeg)

Fig. 7. Flood consequences as functions of time for evacuating the PAR.

$$
\begin{aligned}
= & \sum_{j=1}^{+\infty} C\left(W_{t}\right) P\left(t_{j}\right) \\
& +\sum_{j=1}^{+\infty}\left[D\left(W_{t}\right)+L\left(W_{t}\right)\right] P\left(t_{j}\right)
\end{aligned}
$$

Similarly, considering the definition of $W_{t}$ in Eqs. (2)-(4), Eq. (9) can be separated into two equations:

$$
\begin{aligned}
& \sum_{j=1}^{+\infty} C\left(W_{t}\right) P\left(t_{j}\right)=\sum_{j=1}^{w} C(0) P\left(t_{j}\right) \\
& \quad+\sum_{j=w+1}^{N} C\left(t_{j}-t_{\mathrm{w}}\right) P\left(t_{j}\right)+C\left(t_{\mathrm{end}}-t_{\mathrm{w}}\right)\left[1-\sum_{j=0}^{N} P\left(t_{j}\right)\right] \\
& \sum_{j=1}^{+\infty}\left[D\left(W_{t}\right)+L\left(W_{t}\right)\right] P\left(t_{j}\right)=\sum_{j=1}^{w}[D(0)+L(0)] P\left(t_{j}\right) \\
& \quad+\sum_{j=w+1}^{N}\left[D\left(t_{j}-t_{\mathrm{w}}\right)+L\left(t_{j}-t_{\mathrm{w}}\right)\right] P\left(t_{j}\right)+0
\end{aligned}
$$

where $t_{N}=t_{\text {end }}$. The optimal time to issue the evacuation warning is the time to attain the minimum total loss $\left[\operatorname{Min}\left(E\left(L_{\mathrm{t}}\right)\right]\right.$.

Figure 7 shows the flood consequences as functions of the time for issuing warning $\left(t_{\mathrm{w}}\right)$. The flood damage and loss of life increase and the evacuation costs decrease with $t_{\mathrm{w}}$. Therefore, there is an optimal point $\left(t_{\mathrm{op}}\right)$ for evacuating the PAR to achieve the minimum expected total loss. The parameter, $t_{\mathrm{op}}$, is very important in decision making. If $t_{\mathrm{op}}$ is close to $t_{0}$, the PAR should be evacuated immediately; if $t_{\mathrm{op}}=t_{\text {end }}$, no evacuation is decided; if $t_{0}>t_{\mathrm{op}}<t_{\text {end }}$, the PAR should be evacuated at $t_{\mathrm{op}}$. If it is not in an urgent case, namely $t_{\mathrm{op}}$ is much larger than $t_{0}$, we may delay the decision to gain more information to reduce the uncertainties.

As time goes on, more information for decision will be available. The decision with a different initial time $\left(t_{0}\right)$ is defined as a stage in which the available information and the

evaluated results may be different. Thus, a dynamic decision should be a multi-stage decision process, the details of which will be introduced in the companion paper (Peng and Zhang, 2013). In each stage, as the information gathered and its condition of uncertainty is different, the predicted dambreak probabilities and flood consequences could be different. It would be unnecessary to consider the decision making as a continuous process of $t_{0}$ since the changes in information may be small in a short period. In this framework, the multi-stage decisions are limited to stages with significant changes in information, such as a predicted storm, changes in knowledge on the properties of the dam materials, and implementing major flood control measures. In the multi-stage decision framework, both the predicted dam-break probabilities and consequences should be updated in each new stage. This will be illustrated with a specific dam-break case study in the companion paper (Peng and Zhang, 2013).

It may be debatable to put a price on human life and make a decision with a minimal expected total loss. However, as the actual expenditures on risk reduction are finite, it may be rational to set a value of a life to help rational decision making. In this study, a value of the macroeconomic contribution of a person is used to monetize a human life, which will be introduced later. From the overview of the dynamic decision framework, two important components of the framework are critical: prediction of dam-break probability as a stochastic process and evaluation of flood consequences as functions of warning time. These two components will be presented in the next two sections.

## 4 Prediction of dam-break probability with time series

### 4.1 Dam-break probability analysis

As introduced above, only the overtopping failure mode is discussed in this paper. A dam is assumed to be overtopped once the reservoir volume exceeds its capacity $\left(V_{\mathrm{cr}}\right)$ :
$V_{t}>V_{\mathrm{cr}}$
where $V_{t}$ is the reservoir volume at time $t$. If $V_{t}$ is a normal variate with a mean of $M_{V t}$ and a standard deviation of $\sigma_{V t}$, the probability of overtopping failure before time $t\left(P_{\mathrm{O}}\right)$ is given by

$$
\begin{aligned}
P_{\mathrm{O}}(t) & =P\left(V_{t}>V_{\mathrm{cr}}\right)=1-P\left(V_{t} \leq V_{\mathrm{cr}}\right) \\
& =1-\Phi\left(\frac{V_{\mathrm{cr}}-M_{V t}}{\sigma_{V t}}\right)
\end{aligned}
$$

where $\Phi()$ is the probability function of a standard normal distribution.

For a discrete variable situation, the probability of overtopping in the period between $t-\Delta t$ and $t, P_{D}(t)$, is the probability that the predicted lake volume at time $t$ is larger than $V_{\mathrm{cr}}$ and the predicted lake volumes before time $t\left(V_{t-k \Delta t}\right.$,
$k \geq 1$ ) are smaller than or equal to $V_{\mathrm{cr}}$ :
$P_{D}(t)=P\left(V_{t}>V_{\mathrm{cr}}, V_{t-\Delta t} \leq V_{\mathrm{cr}}, \ldots, V_{t-k \Delta t} \leq V_{\mathrm{cr}}, \ldots\right)$
where $V_{t-k \Delta t}$ denotes all the predicted lake volumes before time $t$.

Based on mass conservation, the reservoir volume at time $t, V_{t}$, is given by
$V_{t}=V_{t-\Delta t}+\left(Q_{t}-Q_{o t}-Q_{\mathrm{er}}\right) \Delta t$,
where $\Delta t$ is a time interval, and $Q_{t}, Q_{o t}$, and $Q_{\mathrm{er}}$ are the inflow rate, outflow rate, and evaporation rate of the reservoir at time $t$, respectively. For a specific dam before overtopping, the outflow rate $Q_{o t}$ can be treated as a deterministic variable. The evaporation rate $\left(Q_{\mathrm{er}}\right)$ in a short time during the emergency management could be ignored. If the inflow rate is greater than the outflow rate, then $V_{t}$ always increases monotonically with time; namely, $V_{t}>V_{t-\Delta t}$ and $V_{t-\Delta t}>V_{t}-V_{t-k \Delta t}, k>1 . P_{D}(t)$ can now be expressed as

$$
\begin{aligned}
P_{D}(t) & = \\
& P\left(V_{t}>V_{\mathrm{cr}}, V_{t-\Delta t} \leq V_{\mathrm{cr}}, \ldots, V_{t-k \Delta t} \leq V_{\mathrm{cr}}, \ldots\right) \\
& =P\left(V_{t}>V_{\mathrm{cr}}, V_{t-\Delta t} \leq V_{\mathrm{cr}}\right) \\
& =P\left(V_{t-\Delta t} \leq V_{\mathrm{cr}}\right)-P\left(V_{t} \leq V_{\mathrm{cr}}, V_{t-\Delta t} \leq V_{\mathrm{cr}}\right) \\
& =P\left(V_{t-\Delta t} \leq V_{\mathrm{cr}}\right)-P\left(V_{t} \leq V_{\mathrm{cr}}\right) \\
& =\left[1-P_{\mathrm{O}}(t-1)\right]-\left[1-P_{\mathrm{O}}(t)\right] \\
& =P_{\mathrm{O}}(t)-P_{\mathrm{O}}(t-1)
\end{aligned}
$$

From the analysis, $Q_{t}$ is the only stochastic process in estimating the reservoir volume at time $t$, which can be forecasted using time series analysis methods. A time series is a sequence of observations taken sequentially in time. An intrinsic feature of a time series is that adjacent observations are dependent (Box et al., 2008). Considering these time-related dependences is essential for dynamic decision analysis. The purpose of the time series analysis is to forecast the future values of a time series based on the available observations. The analysis in this paper is divided into four steps: model identification, model estimation, model diagnostic checking and forecasting following Brockwell and Davis (1996) and Box et al. (2008). Several frequently used time-series models, model estimation, model diagnostic checking and forecasting are introduced in the appendices.

### 4.2 Forecasting dynamic inflow rates and lake volumes

After a time-series model and its model parameters have been identified as described in the appendices, forecasts of reservoir inflow rate can be obtained from the following difference equation:

$$
\begin{aligned}
x_{t} & =\varphi_{1} x_{t-1}+\varphi_{2} x_{t-2}+\cdots+\varphi_{p} x_{t-p} \\
& +a_{t}-\theta_{1} a_{t-1}-\theta_{2} a_{t-2}-\cdots-\theta_{q} a_{t-q}
\end{aligned}
$$

For example, an $\operatorname{AR}(2)$ time series can be forecasted as

$$
\begin{aligned}
& x_{t}^{*}(1)=\varphi_{1} x_{t}+\varphi_{2} x_{t-1} \\
& x_{t}^{*}(2)=\varphi_{1} x_{t}^{*}(1)+\varphi_{2} x_{t-1} \\
& x_{t}^{*}(l)=\varphi_{1} x_{t}^{*}(l-1)+\varphi_{2} x_{t}^{*}(l-2), l=3,4, \ldots
\end{aligned}
$$

where $x_{t}$ is the recorded value and $x_{t}^{*}(l)$ is the predicted value with lead time $l$. Note the expected value of $a_{t}$ is zero as $a_{t}$ follows a normal distribution of $N\left(0, \sigma_{a}^{2}\right)$.

A time series can also be expressed in a random-shock form of an infinite series (Box et al., 2008):

$$
\begin{aligned}
x_{t} & =a_{t}+\psi_{1} a_{t-1}+\psi_{2} a_{t-2}+\psi_{3} a_{t-3} \cdots \\
& =a_{t}+\sum_{j=1}^{\infty} \psi_{j} a_{j}
\end{aligned}
$$

where the coefficients $\psi_{j} \mathrm{~s}$ can be obtained by substituting Eq. (19) into Eq. (17) and comparing the coefficients of $a_{t}$ in both sides.

As $a_{t}$ is an identically distributed stochastic process, $N\left(0, \sigma_{a}^{2}\right)$, the standard deviation of $x_{t}$, is calculated as
$\sigma^{2}\left[x_{t}(l)\right]=\left(1+\psi_{1}^{2}+\psi_{2}^{2}+\ldots+\psi_{l-1}^{2}\right) \sigma_{a}^{2}$
where $\sigma_{a}$ is estimated as
$\sigma_{a}^{2}=\frac{1}{n-1} \sum_{1}^{n} a_{t}^{2}$
in which $a_{t}$ can be obtained using Eq. (A11).
According to Eq. (15), the reservoir volume $V_{t}$ can be expressed as a function of the inflow rate, $x_{t}$ :
$V_{t}-V_{t-\Delta t}=\left(x_{t}+\mu_{Q}-Q_{\text {or }}\right) \Delta t$,
where $Q_{t}=x_{t}+\mu_{Q}$, and $\mu_{Q}$ is the mean value of $Q_{t}$. Let us set
$v_{t}=\frac{V_{t}}{\Delta t}$ and $v_{t-i}=\frac{V_{t-i \Delta t}}{\Delta t}$.
Then $v_{t}$ is given by
$x_{t}=v_{t}-v_{t-1}-\left(\mu_{Q}-Q_{\text {or }}\right)$.
Take $x_{t}$ as a $\mathrm{AP}(2)$ model for example again; namely
$x_{t}=\varphi_{1} x_{t-1}+\varphi_{2} x_{t-2}+a_{t}$.
Writing Eq. (24) at times $t, t-1$ and $t-2$ and substituting these equations for $x_{t}, x_{t-1}$ and $x_{t-2}$ into Eq. (25), $v_{t}$ can be expressed as

$$
\begin{aligned}
v_{t} & =\left(1+\varphi_{1}\right) v_{t-1}-\left(\varphi_{1}-\varphi_{2}\right) v_{t-2}-\varphi_{2} v_{t-3} \\
& +\left(1-\varphi_{1}-\varphi_{2}\right) \mu_{Q}-\left(Q_{\mathrm{O}_{t}}-\varphi_{1} Q_{\mathrm{O}_{t-1}}-\varphi_{2} Q_{\mathrm{O}_{t-2}}\right)+a_{t}
\end{aligned}
$$

Set
$C_{Q}=\left(1-\varphi_{1}-\varphi_{2}\right) \mu_{Q}-\left(Q_{\mathrm{O}_{t}}-\varphi_{1} Q_{\mathrm{O}_{t-1}}-\varphi_{2} Q_{\mathrm{O}_{t-2}}\right)$.

Then the means of $v_{t}$ can be forecasted as

$$
\begin{aligned}
v_{t}^{*}(1)= & \left(1+\varphi_{1}\right) v_{t}-\left(\varphi_{1}-\varphi_{2}\right) v_{t-1}-\varphi_{2} v_{t-2}+C_{Q} \\
v_{t}^{*}(2)= & \left(1+\varphi_{1}\right) v_{t}^{*}(1)-\left(\varphi_{1}-\varphi_{2}\right) v_{t}-\varphi_{2} v_{t-1}+C_{Q} \\
v_{t}^{*}(3)= & \left(1+\varphi_{1}\right) v_{t}^{*}(2)\left(\varphi_{1}-\varphi_{2}\right) v_{t}^{*}(1)-\varphi_{2} v_{t}+C_{Q} \\
v_{t}^{*}(l)= & \left(1+\varphi_{1}\right) v_{t}^{*}(l-1)\left(\varphi_{1}-\varphi_{2}\right) v_{t}^{*}(l-2) \\
& -\varphi_{2} v_{t}^{*}(l-2)+C_{Q} l=4,5, \ldots
\end{aligned}
$$

where $v_{t}$ is the recorded value and $v_{t}^{*}(l)$ is the predicted value with lead time $l$.

The standard deviation of $v_{t}$ and $V_{t}$ can be obtained following the method as shown in Eqs. (20) and (21). With the means and standard deviations of $V_{t}$, the probabilities of dam failure as a time series can be predicted with Eqs. (14) and (16). The details of the method will be demonstrated with a dam-break case study in the companion paper (Peng and Zhang, 2013).

## 5 Evaluation of the consequences of dam breaks

The flood consequences are closely related to evacuation, sheltering, and loss of life. Before evaluating the consequences, HURAM (Peng and Zhang, 2012a, b) is used to simulate these three processes.

### 5.1 Human risk analysis

HURAM incorporates 14 parameters (e.g. time of a day, warning time, water depth, building damage, evacuation, and sheltering) and their inter-relationships in a systematic structure by using Bayesian networks. Figure 8 shows the framework of HURAM, which can be divided into four components: evacuation, sheltering, flood severity, and loss of life.

An evacuation is assumed successful when the available time is larger than the demand time:
$W_{t}+R_{t}>T_{t}+S_{t}+E_{t}$
where $W_{t}=$ warning time, which is the sum of lead time (the duration between issuing warning and the start of the breaching) and flood routing time (the time for the flood routing from the dam site to the studied area); $R_{t}=$ flood rise time, which is the time for the flood water level to rise to the peak level $\left(D_{\mathrm{p}}\right)$ when $D_{\mathrm{p}}<1.5 \mathrm{~m}$ or to 1.5 m when $D_{\mathrm{p}} \geq 1.5 \mathrm{~m} ; T_{t}=$ warning transmitting time, which is the duration from issuing the warning to the receipt by the people at risk; $S_{t}=$ response time, which is the time for people to confirm the warning, prepare for evacuation and wait for family members; $E_{t}=$ evacuation time, which is the time for people to move to safe places (Frieser, 2004; Jonkman, 2007). The fatality rate of the evacuated people is set as zero. The people who have not evacuated are called exposed population. The details of determining each parameter are described by Peng and Zhang (2012a, b).

![img-7.jpeg](img-7.jpeg)

Note: $\mathrm{Fr}=$ fatality rate; $\log N(\mu, \sigma)=$ a lognormal distribution with a variable of water depth $(h)$ in meter; $\mu=$ mean of $\ln (h)$; and $\sigma=$ standard deviation of $\ln (h)$.
Fig. 8. The framework of HURAM.

The exposed people are assumed to take shelter at the top of buildings. A successful sheltering also requires that the available time is longer than the demand time ( $W_{t}+R_{t}>T_{t}+$ $S_{t}$ ). $E_{t}$ is not needed in Eq. (29) for sheltering. The people who have sheltered in the buildings are not absolutely safe, depending on building damage and building inundation as shown in Fig. 8.

Flood severity is a parameter to evaluate the flood strength and the resistance of the buildings. Flood severity is divided into four levels: safe, low, medium and high, depending on the building damage and building inundation. Building damage is determined according to the criteria of RESCDAM (2000) as shown in Table 2. The whole building is fully inundated if the water depth is greater than the height of the building. Based on the concepts of building damage and building inundation, the flood severity in this study is defined in a matrix form in Table 3.

The loss of life in each flood severity zone is obtained with separate methods. In a safe zone, where no flood has arrived and the buildings are stable, the fatality rate is set as zero. In a high severity zone, as the buildings are either fully inundated or totally damaged, the fatality is very high. Historical records show that the average fatality rate in high severity zones is 0.91 (Peng and Zhang, 2012a). Jonkman (2007) found that a logarithmic function fits the relationship between fatality rate and water depth well. Thus, the fatality rates in medium and low severity zones are assumed to follow lognormal functions of water depth $(h)$. Based on results of regression analysis, the means and standard deviations of $\ln (h)$ are 1.65 and 0.56 for medium flood severity and 3.38 and 1.19 for low flood severity, respectively (Peng and Zhang, 2012a). For example, the fatality rate of
the non-evacuated people in a low flood severity area (the buildings are neither seriously damaged nor fully inundated) is $10 \%$ if the water depth is 6.4 m .

### 5.2 Modifications to HURAM

HURAM is implemented in Hugin Lite (Hugin Expert A/S, 2004), which is a program for the analysis of Bayesian networks. Hugin Lite is powerful for the analysis of Bayesian networks involving discrete variables or continuous normal variates. However, in the dynamic decision making framework (DYDEM), the parameters are not limited to these two types. Thus, the calculations for flood consequence in DYDEM are coded in Visual Basic in Microsoft Excel with Monte Carlo simulations instead of in Hugin Lite. The modifications are summarized as follows, and details of the HURAM model are described by Peng and Zhang (2012a, b):

1. In HURAM, the parameter of time of day, with the states of $08: 00-17: 00,17: 00-22: 00$ and $22: 00-08: 00$, is considered in the evacuation and sheltering components. In each state of time of day, the distributions of warning transmitting time $\left(T_{t}\right)$, response time $\left(S_{t}\right)$ and evacuation time $\left(E_{t}\right)$ are different. These can be handled as the lead time in HURAM is on the order of minutes to hours (the lead time is often in one state of time of a day). However, in DYDEM, the lead time for decision making is often on the order of days. The distributions of $T_{t}, S_{t}$ and $E_{t}$ would be complicated if the time of day is considered. Thus, the effect of time of day is not considered in DYDEM.
2. In HURAM, the warning transmitting distributions are $W(3.5,0.6), W(2.0,0.5)$, and $W(1.3,0.7)$ for times of a day of $08: 00-17: 00,17: 00-22: 00$ and $22: 00-08: 00$, respectively. Here $W(a, b)$ denotes a Weibull distribution with coefficients $a$ and $b$ :
$P_{t}=1-\exp \left(-a t^{b}\right)$.
In DYDEM, we use $W(1.3,0.7)$ only for convenience and safety. $W(1.3,0.7)$ is suggested for moderately rapid warning by Lindell et al. (2002).
3. The response time distribution is assumed as $W(4,1)$ for emergent dam break situations in HURAM, with a mean value of 15 min and a standard deviation of 15 min . However, for decision making in DYDEM, the response time should be much longer as people need time to evacuate properties and prepare to live outside of their homes for several days. A distribution of $W(0.085$, 2.55) is used according to practices of hurricane evacuation (Lindell et al., 2004).

### 5.3 Estimation of the flood consequences

The evacuation cost consists of initial costs and GDP interruption. The initial costs $\left(C_{\mathrm{i}}\right)$ are the expenses for evacuating

Table 2. Recommended damage parameters for building structures (after RESCDAM, 2000).


Table 3. Flood severity matrix.


and arranging the people at risk and necessary services (e.g. security and medical care). The initial costs are generally proportional to the number of people to be evacuated and the time interrupted (warning time):
$C_{\mathrm{i}}=c P_{\text {eva }}(\mathrm{PAR})\left(W_{t}+3\right)$
where $c$ is the expense per person per day (e.g. RMB 60 or US $\$ 9.5$ per person per day); $P_{\text {eva }}$ is the proportion of the people evacuated, which is estimated using the modified HURAM; $W_{t}$ is the warning time in days. The 3-day time is taken as the minimal period of time between the predicted moment of flooding and the return of the residents (Frieser, 2004). The GDP interruption $\left(C_{\mathrm{GDP}}\right)$ is calculated as
$C_{\mathrm{GDP}}=\frac{\mathrm{GDP}_{\mathrm{P}}}{365}(\mathrm{PAR})\left(W_{t}+4\right)$
where GDP $_{\mathrm{P}}$ is the average GDP per person in the flood area. It is expected that economic sectors need time to restart their business (Frieser, 2004). Therefore, a duration of 4 days is added to the warning time. Thus the evacuation costs $(C)$ are given by
$C=C_{\mathrm{i}}+C_{\mathrm{GDP}}$.
The flood damage $(D)$ is limited to the moveable properties in this study. The moveable properties are generally proportional to the number of people who have neither evacuated nor sheltered in safe zones:
$D=\left(1-P_{\text {eva }}\right)\left(1-P_{\text {safe }}\right)(\mathrm{PAR}) \alpha I_{\mathrm{p}}$
where $P_{\text {safe }}$ is the ratio of the people taking shelter in safe zones; $\alpha$ is the proportion of properties that can be transferred ( 0.1 is assumed); $I_{\mathrm{p}}$ is the property of each person, which is taken as the cumulative net income (i.e. income minus spending) per person:
$I_{\mathrm{p}}=(I-S) n$
where $I$ and $S$ are the average income and spending per person; $n$ is the average working period per person (e.g. 20 yr ).
Despite ethical considerations, a human life has to be measured for evacuation decision making. Jonkman (2007) reviewed approaches of evaluating the human life. A method with macroeconomic considerations is chosen in this study (Van Manen and Vrijling, 1996, quoted by Jonkman, 2007). In this method, the value of a human life $\left(V_{\mathrm{L}}\right)$ is given as the product of GDP per person $\left(\mathrm{GDP}_{\mathrm{P}}\right)$ and the average longevity $(L)$ :
$V_{\mathrm{L}}=\left(\mathrm{GDP}_{\mathrm{p}}\right) L$.
For example, the GDP $_{\mathrm{P}}$ and $L$ in Mianyang, China, are RMB 13745 and 75 yr in 2008 (Mianyang Bureau of Statistics, 2009). Thus, the value of one person in 2010 in China is RMB 1.03 million. The monetized loss of life $\left(M_{\mathrm{L}}\right)$ is then calculated as
$M_{\mathrm{L}}=V_{\mathrm{L}}(\mathrm{LOL})$
where LOL is the loss of life predicted with HURAM as a function of warning time. As $P_{\text {eva }}, P_{\text {safe }}$ and LOL can be predicted as functions of warning time with HURAM, the three categories of flood consequences are expressed as functions of warning time.

## 6 Dynamic decision making and comparison with existing methods

With the predicted dam-break probabilities as a time series and the flood consequences as functions of warning time, the expected total loss can be calculated with Eq. (5) for continuous time series and Eq. (9) for discrete time series. The optimal time to evacuate the PAR is obtained by attaining the minimum expected total loss as shown in Fig. 7. The decision can be updated when additional information is available

Table 4. Comparison of decision-making methods for dam break floods.


to reduce the uncertainties in the model parameters. These will be presented with a specific dam-break case study in the companion paper (Peng and Zhang, 2013).

Frieser (2004) and Smith et al. (2006) published decisionmaking methods for floods with multi-phase decision trees, which are extended from the two-phase decision tree shown in Fig. 1. The time of possible flood occurrence is set as a target time (e.g. with enough lead time to evacuate the people) or the time achieving the worst predicted situation (e.g. highest water level or largest flood flow rate). The minimum expected total loss in each phase is obtained by comparing those in all alternatives. The optimal time to evacuate the PAR is the time achieving the minimum expected total loss.

Table 4 shows a comparison of these two methods and DYDEM. Compared to the existing methods with decision trees, the dynamic decision framework suggested in this paper has several distinct features:

1. The framework takes the dam-failure probability as a time series and the flood consequences as functions of warning time. The time effects on both dam-break probability and consequence are sufficiently considered.
2. Decision trees have a premise of a fixed occurrence time, which may not be reasonable, as the probability of disaster occurrence is a stochastic process. The loss of life and properties may be underestimated if the flood occurs before the predicted moment, and vice versa. The dam-failure probability is simulated as a time series in DYDEM, in which the dam may break at any future time with a certain probability.
3. A successful evacuation can be attained when the available time (i.e. the sum of warning time and flood rise time) is more than the demanded time (i.e. the sum of warning transmitting time, response time and evacuation time). The parameter distributions are based on excising models and statistical data. Monte Carlo simulation is used to simulate the evacuation process with these parameter distributions.
4. The human risk or loss of life, which is complex and often assumed as constant values in the existing methods,
is simulated with HURAM based on Bayesian networks. Fourteen uncertain parameters and their interrelationships are considered in this model.
5. Flood consequences, including evacuation cost, flood damage and loss of life, are closely related to evacuation rate (the proportion of the people evacuated), sheltering rate (the proportion of the people sheltered) and fatality rate (the proportion of the people who die). The processes of evacuation, sheltering and loss of life are simulated in HURAM with a Bayesian network.

## 7 Conclusions

Evacuation can save human life and properties but incurs costs at the same time. This paper presents a new framework of dynamic decision making for dam-break emergency management. The following conclusions can be drawn:

1. The new framework presented in this paper takes the dam-failure probability as a time series and the flood consequences as functions of warning time. The assumption of a fixed flood occurrence time in a traditional decision tree can be relaxed.
2. Overtopping failure occurs when the reservoir water volume exceeds the capacity. The inflow rates and reservoir volumes are considered as stochastic processes and forecasted using time series in four steps: model identification, model estimation, model diagnostic checking and forecasting. The probability of overtopping failure is predicted using the forecasted mean values and standard deviations of the reservoir volume.
3. The consequences of dam-break floods include evacuation costs, flood damage and loss of life. The three categories of flood consequences can be calculated as functions of evacuation rate, sheltering rate and loss of life. These three parameters can be predicted with HURAM, which is a model for simulating human-flood interactions using Bayesian networks. A program is coded in Visual Basic in Microsoft Excel for this purpose.

4. The total risk given a warning time is calculated considering the probability of dam failure, evacuation costs, flood damage and loss of life, and the optimal warning time to achieve a minimum total loss can be determined. The PAR needs to be evacuated immediately if the calculated optimal warning time is close to the initial time $\left(t_{0}\right)$; no warning is needed if the calculated optimal warning time is equal to the end of the study period ( $t_{\text {end }}$ ); the PAR should be evacuated at the optimal time $\left(t_{\text {op }}\right)$ with the minimum expected total loss if $t_{\text {op }}$ is between $t_{0}$ and $t_{\text {end }}$. The decision can be delayed to collect more information and reduce the uncertainties in the information. A delayed decision analysis can be performed with the updated information in this framework. A specific dam-break case study will be presented in the companion paper.

## Appendix A

## Time series models for forecasting inflow rate

A stationary time series, which is one with its mean and variance independent of time, can usually be simulated as a mixed autoregressive-moving average (ARMA) model. In an ARMA model, a time-related variable $x_{t}$ can be expressed as a finite, linear aggregate of previous values of the time series and random shocks, $a_{t}, a_{t-1}, \ldots, a_{t-q}$.

$$
\begin{aligned}
x_{t} & =\varphi_{1} x_{t-1}+\varphi_{2} x_{t-2}+\cdots+\varphi_{p} x_{t-p}+a_{t} \\
& -\theta_{1} a_{t-1}-\theta_{2} a_{t-2}-\cdots-\theta_{q} a_{t-q}
\end{aligned}
$$

in which $\varphi_{\mathrm{i}}$ and $\theta_{\mathrm{i}}$ are the coefficients of the $\operatorname{ARMA}(p, q)$ model to be quantified. A random shock, $a_{t}$, is an independently and identically distributed (IID) stochastic process. Normally $a_{t}$ can be assumed as a normal distribution with a mean value of zero, $N\left(0, \sigma_{a}^{2}\right)$.

If a time series is not a stationary model, it can often be transferred to a stationary one by differentiating it (Box et al., 2008). A difference equation $\Delta x_{t}$ is defined as
$\Delta x_{t}=x_{t}-x_{t-1}$
and $\Delta^{d} x_{t}$ as
$\Delta^{d} x_{t}=\Delta^{d-1} x_{t}-\Delta^{d-1} x_{t-1}$
If $x_{t}$ can be transferred to a stationary time series $\omega_{t}$ with difference equation, namely,

$$
\begin{aligned}
& \omega_{t}=\Delta^{d} x_{t}=\varphi_{1} \omega_{t-1}+\varphi_{2} \omega_{t-2}+\cdots+ \\
& \quad \varphi_{p} \omega_{t-p}+a_{t}-\theta_{1} a_{t-1}-\theta_{2} a_{t-2}-\cdots-\theta_{q} a_{t-q}
\end{aligned}
$$

then $x_{t}$ is called an autoregressive integrated moving average time series, or ARIMA $(p, d, q)$. Actually, ARMA $(p, q)$ is a special case of $\operatorname{ARIMA}(p, d, q)$ with $d=0$.

For an $\operatorname{ARMA}(p, q)$ model as shown in Eq. (A1), if $q=0$, then
$x_{t}=\varphi_{1} x_{t-1}+\varphi_{2} x_{t-2}+\cdots+\varphi_{p} x_{t-p}+a_{t}$
is called an autoregressive model of order $p$, or $\operatorname{AR}(p)$ for short. If the $p=0$ in an $\operatorname{ARMA}(p, q)$ model, then $x_{t}$ can be expressed as a finite weighted sum of $a_{t}, a_{t-1}, \ldots, a_{t-q}$ :
$x_{t}=a_{t}-\theta_{1} a_{t-1}-\theta_{2} a_{t-2}-\cdots-\theta_{q} a_{t-q}$,
and is called a moving average model of order $q$, or $\operatorname{MA}(q)$ for short.

## A1 Model identification

The objective of model identification is to find a suitable time series model with orders $(p, d, q)$ to simulate the observations of a time series. For a given observed time series, the first step is to check whether it is stationary or not. If it is non-stationary, we need to transform it using Eq. (A3) until it becomes a stationary time series. The symptom of a nonstationary time series is that the autocorrelation function $\rho_{k}$ at time lag $k$ will not die out quickly and will fall off slowly and nearly linearly with the increase of $k$ (Box et al., 2008). The autocorrelation function, $\rho_{k}$, is given by
$\rho_{k}=\frac{\gamma_{k}}{\gamma_{0}}$
where $\gamma$ is called a autocovariance at time lag $k$ and given by
$\gamma_{k}=\operatorname{cov}\left[x_{t}, x_{t+k}\right]=E\left[\left(x_{t}-\mu\right)\left(x_{t+k}-\mu\right)\right]$.
For a given time series of inflow rate, $x_{1}, x_{2}, \ldots x_{N}$, the estimate of $\gamma_{k}$ is given by
$\gamma_{k}^{*}=\frac{1}{N} \sum_{t=1}^{N-k}\left[\left(x_{t}-\bar{x}\right)\left(x_{t+k}-\bar{x}\right)\right] k=0,1, \ldots, N-1$,
where $\bar{x}$ is the average value of the observations of $x_{t}$.
Another important parameter for a time series is its partial autocorrelation function $\varphi_{k k}$. The $j$-th autocorrelation function $\rho_{j}$ can be described as an autoregressive function as

$$
\begin{aligned}
\rho_{j} & =\varphi_{k 1} \rho_{j-1}+\varphi_{k 2} \rho_{j-2}+\cdots \varphi_{k(k-1)} \rho_{j-k+1} \\
& +\varphi_{k k} \rho_{j-k} \quad j=1,2, \ldots, k
\end{aligned}
$$

where the last coefficient $\varphi_{k k}$ is called a "partial autocorrelation function". $\varphi_{k k}$ can be estimated using a recursive formulas (Durbin, 1960; Box et al., 2008).

The model identification for a stationary time series is to find the model type $[\operatorname{AR}(p), \operatorname{MA}(q)$ or $\operatorname{ARMA}(p, q)]$ and the corresponding order (i.e. $p$ and $q$ ). According to Box et al. (2008), one feature of $\operatorname{AR}(p)$ is that the autocorrelation function $\rho_{k}$ tails off, while its partial autocorrelation function

Table A1. Identification of time series.


![img-8.jpeg](img-8.jpeg)

Fig. A1. Parameters of an assumed time series: (a) autocorrelation function, (b) partial autocorrelation function.
$\varphi_{k k}$ has a cutoff after lag $p$. Conversely, for $\operatorname{MA}(q)$, the autocorrelation function $\rho_{k}$ cuts off after lag $p$, while its autocorrelation function $\varphi_{k k}$ tails off. If both $\rho_{k}$ and $\varphi_{k k}$ tail off, then a mixed process is suggested as shown in Table A1. For example, the autocorrelation function $\left(\rho_{k}\right)$ and partial autocorrelation function $\left(\varphi_{k k}\right)$ of an assumed time series are shown in Fig. A1. As $\rho_{k}$ has a cutoff after lag 1 and $\varphi_{k k}$ tails off, the time series can be assumed as $\mathrm{Ma}(1)$. The assumption needs to be tested, which will be introduced later.

## A2 Model estimation and diagnostic checking

An $\operatorname{ARMA}(p, q)$ time series, shown in Eq. (A1), has $(p+$ $q+1)$ parameters, namely, $\varphi_{1}, \ldots, \varphi_{p}, \theta_{1}, \ldots, \theta_{q}$, and $\sigma_{a}$. The objective of model estimation is to find proper parameters to fit the observations of the time series. The error of a ARMA $(p, q)$ time series at time $t$ is expressed as

$$
\begin{aligned}
a_{t} & =x_{t}-\varphi_{1} x_{t-1}-\varphi_{2} x_{t-2}-\cdots-\varphi_{p} x_{t-p} \\
& +\theta_{1} a_{t-1}+\theta_{2} a_{t-2}+\cdots+\theta_{q} a_{t-q}
\end{aligned}
$$

The least squares method is used to find parameters $\varphi_{\mathrm{i}}$ and $\theta_{\mathrm{i}}$ for achieving the least sum of the squares of $a_{t}$ :
$\operatorname{Min}\left[\sum_{i=1}^{n} a_{i}^{2}\left(\varphi_{\mathrm{i}}, \theta_{\mathrm{i}}\right)\right], \quad i=1,2, \ldots, n$.
This can be implemented using a solver in Microsoft Excel.

After obtaining the parameters, the next step is to conduct model diagnostic checking to make sure the assumed model is suitable. Box et al. (2008) show that the equation
$n \sum_{k=1}^{K}\left[\rho_{k}^{*}(a)\right]^{2}$
approximately follows a $\chi^{2}(K-p-q)$ distribution, where $\rho_{k}^{*}(a)$ is the estimated autocorrelation function of $a_{t}$, which is defined in Eqs. (A7) and (A8). The model can be checked through a $\chi^{2}$ goodness-of-fit test at a confidence level (e.g. $5 \%$ or $10 \%$ ).

Acknowledgements. The research reported in this paper was substantially supported by the Natural Science Foundation of China (No. 51129902) and the National Basic Research Program (973 Program) (No. 2011CB013506).

Edited by: D. Keefer
Reviewed by: J.-J. Dong and H. Huang
