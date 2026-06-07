# Generation Expansion Planning Based on Dynamic Bayesian Network Considering the Uncertainty of Renewable Energy Resources 

Xiangyu Kong ${ }^{1, *}$, Jingtao Yao ${ }^{1}$, Zhijun E ${ }^{2}$ and Xin Wang ${ }^{2}$<br>1 Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin 300072, China<br>2 State Grid Tianjin Electric Power Company, Tianjin 300010, China<br>* Correspondence: eekongxy@tju.edu.cn

Received: 22 May 2019; Accepted: 24 June 2019; Published: 28 June 2019


#### Abstract

In generation expansion planning, sustainable generation expansion planning is gaining more and more attention. Based on the comprehensive consideration of generation expansion planning economics, technology, environment, and other fields, this paper analyzes the sustainable development of power supply planning evaluation indicators and builds a multi-objective generation expansion planning decision model considering sustainable development. According to the target variables in the model, the variables such as attribute variables are divided into different subsets, and the logical relationship analysis method between different nodes is obtained based on Dynamic Bayesian network theory, which reduces the complexity of the planning model problem. The application examples show the feasibility and effectiveness of the proposed model and the solution method.


Keywords: generation expansion planning; sustainable development; Dynamic Bayesian Network; decision model

## 1. Introduction

With the increasingly serious environmental pollution and the gradual exhaustion of petrochemical energy, the development of renewable clean energy is receiving more and more attention. As the most important secondary energy, electric power plays an important role in China's energy consumption and production. Power development and planning usually involve many factors such as economy, resources, environment, science, and technology. Therefore, in essence, generation expansion planning (GEP) is a complex, multi-variable, multi-constraint, multi-objective, multi-stage nonlinear dynamic optimization problem [1-6].

In 2003, the British government published its national energy white paper, which first proposed the concept of "low-carbon economy" [7]; At the world climate conference held in Copenhagen, Denmark, in 2009, the Chinese government also set two ambitious goals of "reducing $\mathrm{CO}_{2}$ emissions per unit of GDP by $40 \%$ to $45 \%$ compared with 2005" and "non-fossil energy accounts for $15 \%$ of total primary energy consumption" by 2020. This not only puts forward a clear goal for China's carbon emission reduction work but also will bring severe challenges to the relevant energy sector. The electrical industry is an important industry of fossil energy consumption in China. According to BP's report [8], nearly two-thirds of the world's new energy consumption will be used to generate electricity by 2035, while the share of energy used to generate electricity is expected to rise from $42 \%$ in 2015 to $47 \%$ by 2035. Emissions from energy use will rise by about $13 \%$ by 2035, far outpacing the IEA's 450 scenario, which calls for a roughly $30 \%$ reduction in global emissions by 2035 in order to meet emissions reduction targets set out in the Paris agreement. The specific situation is shown in Figure 1.

![img-0.jpeg](img-0.jpeg)

Figure 1. Global carbon emissions projections compared to 450 deployment scenarios.
According to BP's report [8], it is not hard to see that with the rapid development of the national economy the demand for electricity is growing and, in the process of electricity production, so is the need to consume large amounts of coal resources, thus causing excessive emissions of greenhouse gases. This is contrary to the concept of a low-carbon economy. In order to change this situation, it is particularly important to study GEP to adapt to the development of the low-carbon economy.

Comprehensive consideration of the economic and environmental costs of sustainable development and the effective use of wind power, solar energy, and other renewable energies has become the focus of GEP and scientific development of power supply structure in various countries. There have been many studies on the GEP of sustainable development. For example, in [9], renewable resources (wind and solar energy) were included in the GEP and the coordinated planning of power system reliability, economy, and long-term operation was studied. The multiple objectives including economic, social, and environmental objectives were analyzed and the uncertain multi-objective GEP model was studied, in [10]. In [11], the interval mixed integer linear programming method was introduced for the generation mode with coal and gas power generation as the main source and new energy and renewable energy power generation as the supplement, and the uncertainty problem existing in the GEP model and the installation expansion problem of the generator set were analyzed. In [12], the objective function of GEP is modified by considering incentive systems such as tariff, emission trade, and carbon tax; the GEP model is obtained with environmental protection restrictions, and the model is solved based on the generalized Benders decomposition method. The above research mainly focuses on the description of the relationship between power and environment, economy and energy technology. However, for the multi-objective decision-making of sustainable development of power structure, the evaluation of indicators and the establishment of models still need to be further improved.

On the other hand, current common GEP models including linear programming, nonlinear programming, multi-objective programming, integer programming, multilevel programming, and dynamic programming [13,14,15,16,17,18] are based on some important assumptions. One of the assumptions is that the three elements in decision analysis-alternative scheme, constraint space, and utility function-can be expressed with absolute accuracy and good mathematics, so the solution space is clear and the result of the solution also strives towards "optimal". However, many criteria and considerations are involved in GEP, making it difficult to describe and evaluate the single-objective method. At the same time, sustainable GEP not only needs to adapt to the current situation of the power system, the development of society, technology, and economy but also needs to be combined with future development, involving a lot of information, data, but a lot of information and data cannot be obtained, so the GEP process has strong uncertainty factors.

At present, there are mainly three kinds of methods for solving multi-target GEP problems in an uncertain environment. The first type of method is to adopt a fuzzy set, rough set, evidence

theory, gray theory, and other methods on the basis of definite analysis to deal with incomplete and inaccurate information [19-22]. However, in the actual decision-making process, considering that the sustainable development planning of generation expansion has to face many data, choices, risks and other factors, the mutual influence among various decision variables is difficult to determine, so the method mentioned above cannot be directly used to guide the decision-making. The second method is to use the robust optimization method to solve the uncertain environment GEP problem [23,24]. This method uses the robust duality theorem to transform the model with uncertain variables into a completely determined model and then use the relevant optimization method to solve the model solution. This method has good robustness, but its solution also has the characteristics of conservatism, and the stronger the uncertainty, the stronger the conservation of the solution. Therefore, this method is suitable for small-scale GEP; for the determination of the total installed capacity of various types of power sources in a certain area, its solution is too conservative due to the large uncertainty range, and the economy is poor. The second method is the stochastic programming method based on probability theory, which needs to collect a large number of scene samples to obtain the relatively reliable probability distribution of renewable energy output so that the complexity of solution increases rapidly [25].

Dynamic Bayesian network (DBN) is a probability graph model used to represent the dependence between variables, which provides a concise and effective method for the expression and inference of causality. This method has been applied in power system reliability analysis and fault diagnosis because it can represent the preference, probability estimation, and information state of decision-makers through nodes and directed edges, and at the same time, it can make use of the conditional independence between variables and provide decision-makers with intuitive and accurate logical relations. For example, reference [26] established a component-based DBN fault diagnosis model for the application of a genetic algorithm in the power system fault diagnosis. Based on certain inference rules, the objective function of the genetic algorithm was formed according to the DBN, and the genetic algorithm was used for optimization and solution. In [27], for the problem that the analytical method is difficult to analyze the reliability of the distribution system when the scale of the distribution system increases, a distribution system reliability evaluation reasoning algorithm was proposed based on DBN timing simulation, which can intuitively find out the weak links of the system.

A reasonable and effective GEP method is the premise to ensure the development of the power industry and a powerful means to achieve low carbon on the basis of ensuring the safe and stable operation. In this paper, an evaluation index of sustainable GEP is provided, and the decision-making model for multi-objective GEP considering sustainable development is established. Based on DBN, a GEP method considering renewable energy resources uncertainty and multi-objective is proposed that provides a way for the sustainable development of power supply. The main contributions of this paper include:
(1) Through comprehensive analysis of sustainable development in the economic, scientific, environmental, and other aspects of GEP requirements, the sustainable development of GEP evaluation indicators and the development of a multi-objective GEP decision model considering sustainable development.
(2) This paper analyzes the uncertainties in power supply planning considering sustainable development and determines the probability distribution and variation interval of uncertain variables. By dividing the uncertainty variable interval into several sub-intervals and taking the most unfavorable state on these sub-intervals as the overall state of the sub-interval, the uncertain variables are discretized into several discrete states, which greatly reduces the calculation amount and ensures solution set robustness and economy.
(3) This paper proposes a model solving method based on DBN theory for the problem that multi-objective multi-stage power planning model with uncertain variables is difficult to solve, which divides model variables into decision environment variables, decision choice variables, decision transmission variables, decision target variables, and decision value variables according to their attributes and represents them as a network structure according to their causal relationship.

Based on this network, the final utility of each decision scheme is deduced. Since the uncertainty model draws on the conditional independence assumption of DBN, the decision maker only needs to consider the relationship between the current node and its parent node when building the model, which greatly reduces the complexity of the decision maker's thinking problem and improves the effective decision making.

The structure of the paper is as follows. Section 2 comprehensively introduces the requirements of sustainable development for GEP. Section 3 introduces the objective function and constraint conditions of GEP, constructs a multi-objective GEP model, and introduces how to deal with the multi-objective optimization problem. Section 4 introduces in detail the uncertain factors in GEP (uncertainty of renewable energy output and load). Section 5 gives the method of obtaining robust feasible solutions. In Section 6, the DBN theory and the model solving algorithm of GEP model using DBN are introduced in detail. Section 7 verifies the proposed model and the model solving algorithm. Finally, Section 8 draws conclusions by discussing the potential, shortcomings, and potential for improvement of the methods presented in this article.

# 2. Sustainable Generation Expansion Planning Requirements 

### 2.1. Characteristics of Generation Expansion Planning under Low Carbon Economy

The power plan is generally based on the source and load conditions to make a power plan when the grid structure and parameters are determined [28,29]. Since the user's electricity behavior is not regulated by the power system, the load is quite random. In the traditional GEP, the power supply side uses conventional energy for power supply, which can provide continuous and stable power supply. Therefore, only load uncertainty is considered in the conventional GEP. In a low-carbon economy, the power supply side will be transformed from a single energy structure into a multi-energy structure in which new energy such as wind, light, and conventional energy are developed in concert. Because wind energy and solar energy are greatly affected by the climate, and the climatic conditions are uncontrollable and random, this results in the random uncertainty of photovoltaic and wind power output [30-35]. This feature makes the source-network-load model of the power system transform from load uncertainty to source load uncertainty, and the GEP problem becomes more complicated. The source-network-load model in a low carbon economy is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Generation expansion planning diagram under low carbon economy.

The uncertainty of the user's power consumption makes it difficult to determine the load growth, and the uncertainty of the load growth makes the unbalanced power uncertain. Unbalanced power is an important basis for GEP. Its uncertainty makes it difficult to make decisions about power supply capacity. This is a difficult problem in traditional GEP. In a low-carbon economy, the uncertainty of renewable energy makes the output of renewable energy uncertain, and this uncertainty will make the determination of unbalanced electricity more difficult. At the same time, the random nature of renewable energy makes it necessary for conventional power supplies to provide spare capacity, which affects the decision of conventional power supply capacity. Therefore, solving the uncertainty of load and the uncertainty of renewable power supply is the difficulty of GEP decision in a low-carbon economy. This paper makes GEP decision by establishing load and power model and using Bayesian network theory to deal with this difficulty.

# 2.2. Voltage Planning Evaluation Index Considering Low Carbon Emission 

The sustainable development plan of the power supply is to incorporate the power supply's environmental impact, economic and social satisfaction, and scientific and technological content and resource constraints into GEP and development and use multi-objective decision-making methods to seek future power supply goals. Interval optimization process. To conduct research on a sustainable GEP model, it is first necessary to determine the GEP evaluation indicators. The established indicators should reflect the relevant multi-objective factors and the essential characteristics of the sustainable development of the power supply, and the number should be as small as possible and can be analyzed and calculated according to the data. Based on the relationship between power development and planning and economic, environmental, technological, and energy aspects, this paper establishes a sustainable development GEP evaluation index, as shown in Table 1. Among them, $f_{1}$ and $f_{2}$ reflect the relationship between sustainable development of GEP and economic and electrical production; $f_{3}$ reflects the relationship with the environment. Indicators in other areas can also be added in the same way.

Table 1. Evaluation index of the sustainable power structure.


## 3. Planning Model Considering Low Carbon Emission

### 3.1. Objective Function

Due to the characteristics of the power system, from the perspective of meeting the national economy and life, there are economic and reliability requirements in the GEP objectives; from the perspective of the impact on the social environment, it is necessary to make full use of renewable energy and emit emissions to thermal power plants. Exhaust gas, wastewater, waste residue, etc. have strong constraints. In this paper, only the total installed capacity, reliability power loss, and total pollutant emissions such as exhaust gas and carbon dioxide emission indicators are selected to construct a multi-objective function model. Other factors such as national policies and technological developments can also be added in the same way.
(1) System investment operation and maintenance cost indicator

The economic costs in GEP include the investment and construction costs of new power plants that are considered at one time and the operating costs of power plant generator sets that are considered annually in subsequent planning periods. The system investment and operation and maintenance costs of many different types of power supply installations during the planning year can be expressed as follows:

$$
\min f_{1}=\sum_{t=1}^{T} \sum_{i=1}^{N} u_{i}^{t} B_{T}^{*}\left(\Delta Q_{i}^{t}\right)+\sum_{t=1}^{T} \sum_{i=1}^{N} H_{t}^{t} C_{i}\left(Q_{i}^{t}\right)+\sum_{t=1}^{T} M_{t} P_{g}
$$

where $T$ indicates the total length of the planning period; $N$ indicates the number of power types, including wind, solar, thermal, hydro, nuclear, and other new energy types; $u_{i}^{t} \Delta Q_{i}^{t}$ is new installed capacity for the $i$-th power supply in year $t ; u_{i}^{t}$ is $0-1$ variable. It indicates the existence of new installed capacity only when $u_{i}^{t}=1 ; B_{T}^{*}\left(\Delta Q_{i}^{t}\right)$ indicates the unit installation cost of the $i$-th power source; $H_{i}^{t}$ is the expected hours of utilization for the $i$-th power plant in year $t ; C_{i}\left(Q_{i}^{t}\right)$ indicates the unit operating unit cost of the $i$-th power source, where the coal-fired power unit includes fuel costs and operation and maintenance costs, and the remaining units only include operation and maintenance costs. $M_{t}$ is the linkage power of the t-year in the region. When it is greater than 0 , it indicates that the region needs foreign power imports to make up the gap. When it is less than 0 , it means that the remaining electricity in the region can be sold to the field; $P_{g}$ is the average transaction price in power linkage.
(2) Comprehensive energy efficiency indicator

The comprehensive energy efficiency refers to the average utilization rate of the generator set. The unit utilization rate can be expressed by the ratio of the actual power generation amount to the theoretical maximum power generation amount, that is, the ratio of the power generation utilization hours to the full year hours, which can reflect the utilization level of power generation. Due to the intermittent and uncontrollable nature of renewable energy such as wind energy and photovoltaic, the reliability of power supply to the load is worse than that of the traditional power supply, and traditional thermal power, hydropower, etc. are required for adjustment. In order to evaluate the utilization efficiency of different types of power supplies, this paper uses the maximum number of planned power utilization hours, which can be expressed by the following formula:

$$
\max f_{2}=\frac{1}{N} \sum_{i=1}^{N}\left(\frac{1}{T_{i}} \sum_{t=1}^{T_{i}} \frac{H_{i}^{t}}{8760}\right)
$$

# (3) Environmental impact indicators 

The environmental indicator refers to the environmental impact of waste pollutants and greenhouse gas $\mathrm{CO}_{2}$ emissions during the production of electric energy. The total indicator of pollutant discharge in a given period can be minimized. Since thermal power is the main factor of environmental pollution, the pollutant emissions of coal-fired units mainly consider $\mathrm{SO}_{2}$, nitrogen oxides, and soot emissions. In the current social background of building low-carbon electricity, people are paying more and more attention to $\mathrm{CO}_{2}$ emissions. According to the emission intensity of $\mathrm{CO}_{2}$, power sources can be divided into high-carbon power sources and low-carbon power sources. High-carbon power sources are mainly traditional thermal power plants. In addition to hydropower and nuclear power, low-carbon power supplies include new energy sources such as wind power and solar energy. China's wind power and solar energy resources are abundant, and its proportion in GEP should be greatly improved. The calculation of important indicators in sustainable GEP can be expressed as:

$$
\min f_{3}=\sum_{t=1}^{T} \sum_{i=1}^{N} O_{i}^{t}=\sum_{t=1}^{T} \sum_{i=1}^{N} Q_{i}^{t} H_{i}^{t} E_{i}
$$

where $O_{i}^{k}$ refers to the $\mathrm{CO}_{2}$ emission from the $i$-th power source in the $t$-th year. For clean renewable energy, $O_{i}^{k}=0 ; E_{i}$ is the $\mathrm{CO}_{2}$ emission per unit of electricity produced by the $i$-th power source, which is related to the power generation efficiency, varying from power plant to power plant. $E_{i}$ is generally averaged, taking China's current thermal power generation as an example, $E_{i}=0.785 \mathrm{~kg} /(\mathrm{kw} \cdot \mathrm{h})$.

Since the country or society usually has a constraint on the total amount of waste emissions, it can also adopt the method that the pollutant emissions within a certain period equal to a given amount of emissions, and then this target can be transferred to the constraint conditions.

# 3.2. Constraints 

Depending on the model adopted, the constraints considered in the GEP model may include spare capacity or reliability constraints, power supply construction constraints, system operation constraints, line transmission capacity constraints, minimum start-up capacity constraints, and new energy generator set constraints, etc. Because the problem of GEP is quite complex, a simplified method is inevitably adopted in all kinds of optimization models. This paper focuses on the sustainable development of power supply and only considers the system balance power and power balance constraints. In the specific implementation process, other constraints can also be added.
(1) System power balance constraint conditions

$$
\sum_{i=1}^{N} p_{i}^{t} \alpha_{i}^{t} s^{t} \geq D_{D}^{k x}\left(1+e_{D}^{t}\right)
$$

where, $D_{D}^{k \pm}$is the maximum possible load for the $k$-th stage system; $e_{D}^{k}$ is system capacity reserve factor of the k -stage; it is worth noting that as the system's wide range of networking and intermittent renewable energy ratios increase, the system's reserve factor will change.
(2) Constraint conditions of system electric quantity balance

$$
\sum_{i=1}^{N} p_{i}^{t} H_{i}^{t} s^{t} \geq E_{D}^{t \pm}\left(1+e_{E}^{t}\right)
$$

where $E_{D}^{t \pm}$is the number of electricity demand forecasts for the system in the $t$-th planning year and is an uncertain value; $e_{E}^{t}$ is the $t$-planning year system power reserve factor and is the same as $e_{D}^{t}$, and each phase is different with system networking and power supply structure changes.
(3) Non-water renewable energy generation constraint

In order to achieve energy conservation and emission reduction, countries have established the proportion of non-water renewable energy generation, and the corresponding constraints can be expressed as:

$$
\sum_{i=1}^{N_{r e}} H_{i}^{t} Q_{i}^{t} \geq \sum_{i=1}^{N} H_{i}^{t} Q_{i}^{t} \eta^{t}
$$

where $N_{r e}$ is the number of sets of non-hydro renewable energy types; $\eta^{t}$ is the planned proportion of non-renewable energy requirements for the system in the t-plan year.
(4) Peaking power reserve capacity constraint

Due to the intermittent and uncontrollable nature of non-water renewable energy sources, it is necessary to use power sources such as thermal power or hydropower as peaking units. In addition, there is a certain reserve capacity constraint, specifically:

$$
\sum_{i=1}^{N_{r e}} Q_{i}^{t} \geq R_{r e} D_{D}^{t \pm}\left(1+e_{D}^{t}\right)
$$

where $R_{m}$ is the spare capacity factor.

# 3.3. Acquisition and Normalization of Uncertain Indicator Decision Matrix 

For the sake of generality, let the generation expansion focus on $m$ objective functions and record the set of indicators as $V=\left\{V_{1}, V_{2}, \cdots, V_{m}\right\}$. Corresponding to the above model, there are:

$$
V_{i}=f_{i}=\sum_{k=1}^{T} v_{i}^{k}
$$

In the $k$-stage of the GEP, there are $q^{k}$ non-inferior solutions, which form a feasible solution set $x_{i}=\left\{x_{1}^{k}, x_{2}^{k} \cdots, x_{q^{k}}^{k}\right\}$ and constitute a feasible decision-making solution set $\mathrm{X}=\left\{x_{1}, x_{2} \cdots, x_{n}\right\}$. If the state set of the $k$-stage decision is represented by $\Theta^{k}=\left\{\theta_{1}^{k}, \theta_{1}^{k}, \cdots \theta_{r}^{k}\right\}$, the probability that state $\theta_{j}^{k}$ occurs is $p_{j}^{k}$, satisfying $0 \leq p_{j}^{k} \leq 1$ and $\sum_{j=1}^{q^{k}} p_{j}^{k}=1$. In the uncertain environment, the influence of the $i$-th scheme $x_{i}^{k}$ of the $k$-th stage on the $j$-th decision indicator under the uncertainty state $\theta_{j}^{k}$, that is, after the execution of the $i$-th scheme, the probability that the decision target $V_{j}$ takes the $j$-th value $V_{i j}$ is $p_{i j}^{k}$, forming an uncertainty indicator decision matrix $P=\left(p_{i j}^{k}\right)_{\alpha \times r \times T}$.

For the incommensurability between operation and maintenance cost indicator, comprehensive energy efficiency indicator and environmental indicator, according to the method of [18], the indicators can be normalized by means of relative state eigenvalues. The formula is as follows:

$$
\begin{aligned}
& v_{\max }=\max \left\{v_{i j}^{k}: 1 \leq i \leq n, 1 \leq j \leq r\right\} \\
& v_{\min }=\min \left\{v_{i j}^{k}: 1 \leq i \leq n, 1 \leq j \leq r\right\}
\end{aligned}
$$

For the maximum benefit indicator such as energy efficiency, the indicator is normalized as shown in Formula (10).

$$
\begin{aligned}
r_{i j}^{k}= & \left(v_{i j}^{k}-v_{\min }\right) /\left(v_{\max }-v_{\min }\right) \\
& (1 \leq i \leq n, 1 \leq j \leq r)
\end{aligned}
$$

For the minimum benefit indicator such as operation and maintenance cost or environmental indicator, the indicator is normalized as shown in Formula (11).

$$
\begin{aligned}
r_{i j}^{k}= & \left(v_{\max }-v_{i j}^{k}\right) /\left(v_{\max }-v_{\min }\right) \\
& (1 \leq i \leq n, 1 \leq j \leq r)
\end{aligned}
$$

Through the calculation of the above formula, the relative state eigenvalues under the unified dimension of each type of indicator can be obtained. Due to the existence of multiple states of decision target variables, when the situation is different, the proportional weight of each target will change. For example, when the local environmental requirements are high, the environmental indicator weights will increase, and the weight of class $j$ decision indicator can be set as $W_{j}=\left\{w_{j}^{1}, w_{j}^{2}, \cdots, w_{j}^{n}\right\}$. The determination of the weight needs to include the knowledge and experience, preferences, and other information of the decision makers and experts. It is assumed that the $L$ decision makers evaluate the importance of the $m$ planning objectives, and the weight vectors are given $w_{l}=\left(w_{l 1}, w_{l 2}, \ldots, w_{l m}\right)^{T}$, and $\sum_{k=1}^{m} w_{l k}=1,0 \leqslant w_{l k} \leqslant 1(k=1,2, \cdots m ; l=1,2, \cdots L)$. If each decision maker's weight is $\lambda_{l}\left(0 \leq \lambda_{l} \leq 1\right)$ and $\sum_{l=1}^{L} \lambda_{l}=1$, the expression of $w_{k}$, which is the k -th element of $w=\left(w_{1}, w_{2}, \ldots, w_{m}\right)^{T}$, is as in Formula (12).

$$
w_{k}=\frac{\sum_{l=1}^{L} \lambda_{l} w_{l k}}{\sum_{k=1}^{m} \sum_{l=1}^{L} \lambda_{l} w_{l k}}
$$

In this case, the multi-objective decision-making problem under uncertain conditions is to use Equation (13) to determine the decision-making choices in each stage successively when the decision-making conditions are known or partially known, and evaluate each decision-making scheme with a unified dimension, and then choose the optimal one in the decision-making scheme or give the priority order.

$$
\gamma\left(X_{i}\right)=\sum_{k=1}^{T} \sum_{j=1}^{n} w_{j}^{k} p_{i j}^{k} v_{i j}^{k} i \in \mathbf{X}
$$

# 4. Uncertainty Analysis 

### 4.1. Load Model

Medium or long term load probability models are generally considered to be normal distribution models.

$$
f_{P}(P)=\frac{1}{\sqrt{2 \pi} \delta_{L}} e^{-\frac{\left(P-\beta_{L}\right)^{2}}{2}}
$$

where $P$ is the actual load power; $\beta_{L}$ and $\delta_{L}$ are the load power expectation and variance, respectively. Since the accuracy of load prediction is high (the error does not exceed $5 \%$ ), $\beta_{L}$ takes the load prediction value, and $\delta_{L}$ is given by experts and relevant staff based on experience.

### 4.2. Renewable Energy Power Generation Model

The auto-regressive moving average (ARMA) model in the time series method is used to simulate the wind speed curve of the wind farm throughout the year. The general expression of the ARMA model is as in Formula (15).

$$
y_{t}=\phi_{1} y_{t-1}+\phi_{2} y_{t-2}+\cdots+\phi_{n} y_{t-n}+\alpha_{t}-\theta_{1} \alpha_{t-1}-\theta_{2} \alpha_{t-2}-\cdots-\theta_{m} \alpha_{t-m}
$$

where $y_{t}$ is the value of the sequence of time $t, \varphi_{1} \ldots \varphi_{n}$ are the autoregressive parameters; $\theta_{1}, \theta_{2}, \cdots, \theta_{n}$ are the moving average parameters; $\alpha_{t}$ is a normal white noise process with a mean of 0 and a variance of $\sigma_{\alpha}^{2}$, such as $\alpha_{i} \in N I D\left(0, \sigma_{\alpha}^{2}\right), \alpha_{i} \in N I D\left(0, \sigma_{\alpha}^{2}\right)$ for a normal distribution.

The wind speed at time $t$ is:

$$
v_{t}=\mu+\sigma y_{t}
$$

where, $\mu$ is the average wind speed and $\sigma$ is the standard deviation of wind speed.
The wind turbine output is nonlinearly related to the wind speed and mainly determined by cut-in wind speed, cut-out wind speed, and rated wind speed of the turbine. The piecewise function is:

$$
P_{g}(v)= \begin{cases}0 & 0 \leq v \leq v_{c i} \\ \left(a+b v+c v^{2}\right) P_{r} & v_{c i} \leq v \leq v_{r} \\ P_{r} & v_{r} \leq v \leq v_{c o} \\ 0 & v_{c o} \leq v\end{cases}
$$

where $v_{c i}, v_{r}$, and $v_{c o}$ are cut-in wind speed, rated wind speed, and cut-out wind speed, respectively; $P_{r}$ is the rated power; $a, b, c$ are the coefficients.

The output power of a photovoltaic power station is determined by factors such as luminous intensity, photovoltaic array area, and photoelectric conversion efficiency. The specific calculation formula is as Formula (18).

$$
P^{e g}=E S \eta
$$

where $E$ is illumination intensity, $S$ is the photovoltaic array area, and $\eta$ is photoelectric conversion efficiency.

The illumination intensity is random, and Beta probability distribution is usually selected as the probability distribution of the illumination intensity, which is as in Formula (19).

$$
f(E)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \Gamma(\beta)}\left(\frac{E}{E_{\max }}\right)^{\alpha-1}\left(1-\frac{E}{E_{\max }}\right)^{\beta-1}
$$

where $E$ and $E_{\max }$ are the actual illumination intensity and maximum illumination intensity for the current time period, respectively; $\alpha$ and $\beta$ are the shape parameters of the Beta distribution, and $\Gamma$ is the Gamma function.

# 5. Acquisition of Feasible Solutions 

### 5.1. Uncertain Subinterval Division

The fluctuation range of the total load power of a certain area and the fluctuation range of the total output of the $j$-th renewable energy power station of this area are shown as follows:

$$
\begin{gathered}
p_{i}^{t} \leq p^{t} \leq p_{h}^{t} \forall t \\
p_{g j t}^{t} \leq p_{g j}^{t} \leq P_{g j h}^{t} \forall j, \forall t
\end{gathered}
$$

where $p^{t}$ is the load power of $t$ period; $p_{i}^{t}$ and $p_{h}^{t}$ are the upper and lower bounds of the fluctuation range of load power in $t$ period, respectively, which can be obtained according to historical data; $p_{g j}^{t}$ is the output of the $j$-th renewable energy power station in $t$ period; $p_{i}^{t}$ and $p_{h}^{t}$ is the upper and lower bounds of the fluctuation range of the output of the renewable energy power station in $t$ period, respectively, and can be obtained based on historical data and weather forecast.

According to the robust optimization theory, load prediction error variation range and the $j$-th renewable energy power station output fluctuation variation range are defined as:

$$
\begin{gathered}
p^{t}=\left\{p^{t} \mid p^{t}=\bar{p}^{t}+\delta^{t},\left|\delta^{t}\right| \leq \bar{p}^{t}, \bar{p}^{t}=\frac{p_{f}^{t}+p_{h}^{t}}{2}, \bar{p}^{t}=\frac{p_{h}^{t}-p_{f}^{t}}{2}, t=1,2, \cdots T\right\} \\
p_{g j}^{t}=\left\{p_{g j}^{t} \mid p_{g j}^{t}=\bar{p}_{g j}^{t}+\delta^{t},\left|\delta_{g j}{ }^{t}\right| \leq \bar{p}_{g j}{ }^{t}, \bar{p}_{g j}{ }^{t}=\frac{p_{g j t}^{t}+p_{g j h}^{t}}{2}, \bar{p}_{g j}{ }^{t}=\frac{p_{g j h}^{t}-p_{g j t}^{t}}{2}, t=1,2, \cdots T\right\}
\end{gathered}
$$

Although the robust optimization method is an effective method for solving the uncertainty problem, the effectiveness of the solution is closely related to the uncertainty interval of the variable. When the uncertainty interval is large, the solution is conservative. The uncertainty range of a single load or a renewable energy source may be small, but for GEP of an area, the total load power and the total output of all renewable energy plants will be relatively indeterminate, which makes GEP conservative, resulting in a waste of resources. In order to solve this problem, this paper divides the whole uncertain interval $R$ into several subintervals $R_{1}, R_{2} \cdots R_{n}\left(\bigcup_{i=1}^{n} R_{i}=R, \bigcap_{i=1}^{n} R_{i}=R\right)$ and uses the robust optimization method to obtain the optimal schemes in these sub-intervals. Then, these schemes are evaluated by using the DBN theory to select the global optimal scheme.

The probability that the variable is in a sub-interval $R_{i}$ is:

$$
P\left(p \in R_{i}\right)=\int_{R_{i}} f(p) d p i=1,2 \cdots n
$$

where $p$ is the uncertain variable; it refers to the load power or the output of the renewable energy power station; $f()$ is the probability density function of the uncertain variable.

Constraints containing uncertain parameters in the power planning model include system power balance constraint. In a subinterval $R_{i}(i \in\{1,2, \cdots n\})$, the original constraint (4) is added to the indeterminate parameter, and the constraint is transformed into:

$$
\sum_{j=1}^{N_{r e}}\left(\Delta Q_{j}+Q_{j}\right)\left(p_{g j}^{t}+\delta_{g j}^{t}\right)+\sum_{i=1}^{N_{r}} \alpha_{i}^{t}\left(\Delta Q_{i}^{t}+Q_{i}^{t}\right) \geq\left(p^{t}+\delta^{t}\right)\left(1+e_{D}^{t}\right)
$$

where $N_{r e}$ is the number of renewable energy types; $N_{c}$ is the number of conventional power sources. In summary, the robust model of GEP can be expressed as:

$$
\left\{\begin{array}{c}
(8) \\
\text { s.t. }(5)-(7)
\end{array}\right.
$$

According to the robust duality theorem, Formula (25) can be expressed as Formula (27).

$$
\left\{\begin{array}{c}
\sum_{j=1}^{N_{r e}} p_{g j}^{t}\left(\Delta Q_{j}+Q_{j}\right)-\sum_{j=1}^{N_{r e}} \bar{p}_{g j}^{t}\left(\Delta Q_{j}+Q_{j}\right) y_{j}+\sum_{i=1}^{N_{c}} \alpha_{i}^{t}\left(\Delta Q_{i}^{t}+Q_{i}^{t}\right) \geq\left(p^{t}+\bar{p}^{t}\right)\left(1+e_{D}^{t}\right) \\
-y_{j} \leq \Delta Q_{j}+Q_{j} \leq y_{j}
\end{array}\right.
$$

Formula (26) can be converted to Formula (28).

$$
\left\{\begin{array}{c}
(8) \\
\text { s.t. }(5)-(7)
\end{array}\right.
$$

Since the GEP model shown by Formula (28) is already a completely determined model, there are already quite mature research results for solving this model [7,36-38] and will not be repeated here.

# 5.2. Target Utility Value Discretization 

Although the above gives a finite number of feasible schemes, when the uncertain variables are continuous variables, the target utility value of these schemes is in a continuously changing interval and changes with the uncertain variables; the decision workload is large and complex, which is very unfavorable for making decisions using DBN theory. When making decisions in an uncertain environment, with the decision-making scheme used, it is often difficult to achieve a certain target utility value, and it only needs to reach a certain target state. In order to facilitate the selection of feasible solutions, the target utility value is discretized into several discrete states by the fuzzy set method according to the actual needs. The membership function of the fuzzy set adopts the most common trapezoidal membership function. If the target utility value is discretized into three states, high, medium, and low, the membership functions of the three states are:

$$
\begin{aligned}
& \mu_{H}\left(P_{L}\right)= \begin{cases}1, & V<a \\
\frac{a-V}{b-a}, & a \leq V \leq b \\
0, & V>b\end{cases} \\
& \mu_{M}\left(P_{L}\right)= \begin{cases}\frac{d-V}{d-c}, & V<d \\
1, & b \leq V \leq c \\
\frac{V-a}{b-a}, & V>a\end{cases} \\
& \mu_{L}\left(P_{L}\right)= \begin{cases}0, & V<c \\
\frac{V-d}{d-c}, & c \leq V \leq d \\
1, & V>d\end{cases}
\end{aligned}
$$

where: $a, b, c$ and $d$ are the parameters of the membership functions, obtained from historical data and expert evaluation. The diagram of its membership function is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. The diagram of its membership function.

# 6. Model Solving based on DBN Method 

Based on the DBN method, this paper puts forward an applicable analysis method for the generation expansion model. By analyzing the properties of each variable in the decision problem, each variable is divided into different sets, and the network is constructed according to its logical relationship. Moreover, the DBN theory is used to solve the network, and the utility of the decision scheme is obtained.

### 6.1. Division of Model Nodes

The decision model is divided into different subsets according to the characteristics of variables, as follows:
(1) The decision-making base node, $C=\left\{C_{1}, C_{2}, \cdots\right\}$, indicates the external condition information that can be collected before the decision is made, such as renewable energy resources, installed capacity, and power generation forecast. The information may be determined or uncertain.
(2) Decision-making node, $D=\left\{D_{1}, D_{2}, \cdots\right\}$, indicates the variables that need to be decided during the entire GEP process, including building capacity and power structure. For the $k$-th stage, the decision variables need to be obtained from the decision set.
(3) Decision-making transfer nodes, $E=\left\{E_{1}, E_{2}, \cdots\right\}$. In the multi-stage decision-making problem, each decision result will affect subsequent decision-making choices. For example, the decision of the power supply structure will affect the environmental protection constraints, and the decision-making transfer node is introduced to indicate the situation after the decision-making of the previous stage. The analysis provides more information or constraints for subsequent decision making.
(4) Decision target node, $O=\left\{O_{1}, O_{2}, \cdots\right\}$, which represents the set of evaluation indicators that need to be measured in the decision-making process, which embodies the objective function that GEP needs to consider.
(5) The decision value node, $V=\left\{V_{1}, V_{2}, \cdots\right\}$, indicates the value brought by each decision target. It is the quantitative representation of the decision target under the same unified dimension and is calculated according to the state combination probability and the corresponding weight.

According to the division of the above node set, the GEP model can be expressed as Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4. Schematic diagram of the model in network form.

# 6.2. Dynamic Bayesian Network 

Dynamic Bayesian networks (DBN) are developed on the basis of static Bayesian networks. At each point in time, each factor of the environment is represented by a random variable. The DBN based on GEP is shown in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. Three-phase generation expansion planning network representation.
It can be seen from Figure 5 that the role of $E$ in this phase is to provide a decision-making environment, which has the same effect as $C$ and can be regarded as the decision-making environment node determined by the previous stage. According to the definition of DBN, $E$ and $D$ are hidden variables, and $O$ and $V$ are observed variables. Therefore, $E$ and $D$ can be merged into node $X$, and $O$ and $V$ are merged into node $Y$ to form a Markov chain. As shown in Figure 6.

![img-5.jpeg](img-5.jpeg)

Figure 6. Hidden Markov model.
The state transition matrix is $\mathbf{A}=\left(a_{i j}\right)_{n \times n}$, where $a_{i j}=P\left(X_{t}+1=j \mid X_{t}=i\right)$. According to Bayesian network independence and Bayes' theorem, $Y_{t}$ can be solved by prior probability and state transition matrix.

$$
P\left(Y_{t}\right)=P\left(Y_{t} \mid X_{t}\right) P\left(X_{t}\right)=P\left(Y_{t} \mid X_{t}\right) P\left(X_{1}\right) P\left(X_{2} \mid X_{1}\right) \cdots P\left(X_{t}=x_{t} \mid X_{t-1}=x_{t-1}\right)
$$

# 6.3. Model Solution 

(1) Using the theory of Section 5, discretize the uncertain variables and solve the probabilities in various decision environments.
(2) The attributes are merged with the nodes with the same function, and the network is simplified to the hidden Markov model.
(3) Determine the true state of the decision base node and determine the conditional probability and state transition matrix.
(4) Calculate the value of the obtained decision value node in the current state and go to step (3) until the planning is completed.

$$
\begin{aligned}
& P\left(v_{j}=v_{j}^{k} \mid x_{i}, C_{\text {now }}\right) \\
& =P\left(v_{j}=v_{j}^{k} \mid E\left(v_{j}\right)\right) \times P\left(E\left(v_{j}\right) \mid x_{i}, C_{\text {now }}\right)
\end{aligned}
$$

(5) According to the above posterior probability, use $P\left(v_{j}=v_{j}^{k} \mid x_{i}, C_{\text {now }}\right)$ to denote $p_{i j}^{k}$ and calculate the sum of the values of all decision value nodes, that is, the utility of the scheme, as shown in Equation (34).

$$
r\left(x_{i}\right)=\sum_{i=1}^{m} P(i) \sum_{k=1}^{T} \sum_{j=1}^{n} w_{j}^{k} p\left(v_{j}=v_{j}^{k} \mid E\left(v_{j}\right)\right) \times P\left(v_{j}=v_{j}^{k} \mid x_{i}, C_{\text {now }}\right) v_{i j}^{k}
$$

where $P(i)$ denotes the probability of occurrence of the decision environment in the $i$ th; $m$ denotes $m$ kinds of decision environments.
(6) Continuously change the state of the value combination of the decision-making nodes at each stage and repeat steps (3) and (4) to obtain various feasible decision-making combinations $X=\left\{x_{1}, x_{2} \cdots, x_{n}\right\}$ for each power plan of each stage.
(7) Calculate the respective utility $\left[\gamma\left(x_{1}\right), \gamma\left(x_{2}\right), \cdots, \gamma\left(x_{n}\right)\right]$ of each decision-making scheme; select the optimal scheme; or sort the scheme for decision-makers to choose the reference.

The model solving algorithm is shown in Figure 7.

![img-6.jpeg](img-6.jpeg)

Figure 7. Schematic diagram of the model in network form.

# 7. Case Analysis 

### 7.1. Case Description and Model Establishment

The load fluctuation range of a certain region is 2769.0 MW-3936.4 MW; the existing installed thermal power capacity is 2600 MW ; the minimum technical output is 0.75 ; the existing renewable energy power plants are wind power plants; the installed capacity is 300 MW ; the output fluctuation rate is $0 \%$ to $25 \%$. The operating cost of a wind farm is $80 \mathrm{RMB} / \mathrm{MWH}$; the operating cost of a photovoltaic power station is $120 \mathrm{RMB} / \mathrm{MWH}$; and the volatility is $0 \%$ to $20 \%$. The service life of thermal power units is 30 years. In the future planning period, 10 thermal power units and 5 wind farms can be added, each thermal power unit with an installed capacity of 100 MW , and each wind farm with an installed capacity of 100 MW .

In the GEP process, determining the installed capacity of renewable energy and the installed capacity of conventional energy is an important part of GEP. The installed capacity of renewable energy is affected by the uncertainty of the output of renewable energy sources. Conventional energy as a power source that stabilizes the random output of renewable energy is affected by the output of renewable energy and local load. The installed capacity of these two types of power supplies will directly affect the various indicators of GEP.

### 7.2. Case Network Model Structure

First, each uncertainty interval is divided into two uncertain subintervals, and then the robust optimization algorithm is used to solve the robust optimization schemes of these sub-intervals, whose solution is shown in Table 2:

Table 2. Feasible solution set.


Then, the state values of each node are obtained by using the division method of uncertain stator interval, the discrete method of target utility value and the expert evaluation method, as shown in Table 3.

Table 3. Influencing factors node descriptions for sustainable generation expansion planning.


Last, based on the causal relationship, the relationship between these nodes is established, and the multi-stage multi-objective network structure model of GEP is shown in Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. Network structure analysis chart for the decision-making process.

# 7.3. Case Model Probability Parameter 

The model probability parameters are not controlled by the decision makers. The main information comes from probabilistic analysis of many aspects such as direct observation, mathematical estimation, or expert evaluation. Assume that the probability of impact on the various indicators of GEP due to the constraints of environmental protection and renewable energy construction is shown in Tables 4-7.

Table 4. The probability distribution of each target in the first stage of decision making.


Table 5. The probability distribution of transition state in the first stage of decision making.


Table 6. The target probability distribution in the second stage of decision making under high load fluctuation.


Table 7. The target probability distribution in the second stage of decision making under low load fluctuation.


### 7.4. The Solution of Model Cases

The sum of the target utility is the final quantitative standard of the GEP model. The goal of the model solution is to provide such a GEP scheme to maximize $\sum_{1}^{3} V_{i}$. Calculate the GEP decision indicators according to Equation (35) as shown. The final benefit indicators for calculating each program are shown in Table 8.

$$
\begin{aligned}
\gamma\left(S_{1}\right)= & \sum_{j=1}^{3} \sum_{k=1}^{q^{j}} W_{j}^{k} V_{i j}^{k} \times P\left(O_{j}=O_{j}^{k} \mid S_{i}, C_{1}=\text { High }\right)+\sum_{j=1}^{3} \sum_{k=1}^{q^{j}} W_{j}^{k} \times P\left(O_{j}=O_{j}^{k} \mid S_{i}, C_{1}=\text { High }\right) \\
= & \sum_{j=1}^{3} \sum_{k=1}^{q^{j}} W_{j}^{k} V_{i j}^{k} \times P\left(O_{j}=O_{j}^{k} \mid E\left(O_{j}\right)\right) \times P\left(\pi\left(O_{j}\right) \mid S_{1}, C_{2}=\text { High }\right) \\
& +\sum_{j=1}^{3} \sum_{k=1}^{q^{j}} W_{j}^{k} V_{i j}^{k} \times P\left(O_{j}=O_{j}^{k} \mid E\left(O_{j}\right)\right) \times P\left(E\left(O_{j}\right) \mid S_{1}, C_{2}=\text { High }\right)=2.9901
\end{aligned}
$$

Table 8. Standardized indicators matrix for generation expansion planning decision-making.


According to the analysis in Section 4.2, the probability of fluctuations in load and renewable energy can be obtained. The decision environment probability matrix is shown in Table 9:

Table 9. Standardized indicators matrix for generation expansion planning decision-making.


In this uncertain environment, the indicators for various decision-making options are shown in Table 10. It can be seen that in this uncertain environment, the best benefit is adopted in No. 3.

Table 10. Standardized indicators matrix for generation expansion planning decision-making.


# 8. Conclusions 

From the perspective of sustainable social development in the future, the planning of the power system will pay more attention to the proportion of renewable new energy. Taking environmental factors as one of the multiple objectives, this paper constructs a multi-objective sustainable development GEP model with uncertainty. According to the characteristics of target variables, attribute variables and other factor variables in the model, the model is divided into different subsets, and the logical relationship analysis method among different nodes is obtained based on the DBN theory, which reduces the complexity of the planning model problem. This method focuses on the constraints of economic and environmental factors in GEP and provides an idea and method for the sustainable development of GEP under the multi-objective situation in China.

Author Contributions: Conceptualization, X.K. and J.Y.; methodology, X.W. and X.K.; software, X.W. and J.Y.; validation, X.K.; formal analysis, X.K., and J.Y.; investigation, X.K.; resources, X.W. and Z.E.; data curation, X.K. and Z.E.; writing-original draft preparation, X.K.; writing-review and editing, J.Y.; supervision, X.W. and Z.E.; project administration, X.W., and Z.E.
Funding: This work was funded by the State Key Laboratory of HVDC, Electric Power Research Institute, China Southern Power Grid (SKLHVDC-2019-KF-16).
Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.

# Abbreviations 

DBN Dynamic Bayesian network
IEA International Energy Agency
GEP Generation expansion planning
