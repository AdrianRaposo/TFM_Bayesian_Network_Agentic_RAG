# Low-carbon economic multi-objective dispatch of integrated energy system considering the price fluctuation of natural gas and carbon emission accounting 

Minglei Qin ${ }^{1}$, Yongbiao Yang ${ }^{1,2}$, Xianqiu Zhao ${ }^{1}$, Qingshan Xu ${ }^{1,2 *}$ and Li Yuan ${ }^{3}$


#### Abstract

Natural gas is the main energy source and carbon emission source of integrated energy systems (IES). In existing studies, the price of natural gas is generally fixed, and the impact of price fluctuation which may be brought by future liberalization of the terminal side of the natural gas market on the IES is rarely considered. This paper constructs a natural gas price fluctuation model based on particle swarm optimization (PSO) and Dynamic Bayesian networks (DBN) algorithms. It uses the improved epsilon constraint method and fuzzy multi-weight technology to solve the Pareto frontier set considering the system operation cost and carbon emission. The system operation cost is described using Latin Hypercube Sampling (LHS) to predict the stochastic output of the renewable energy source, and a penalty function based on the Predicted Mean Vote (PMV) model to describe the thermal comfort of the user. This is analyzed using the Grey Wolf Optimization (GWO) algorithm. Carbon emissions are calculated using the carbon accounting method, and a ladder penalty mechanism is introduced to define the carbon trading price. Results of the comparison illustrate that the Pareto optimal solution tends to choose less carbon emission, electricity is more economical, and gas is less carbon-intensive in a small IES for end-users when the price of natural gas fluctuates. The impacts of various extents of natural gas price fluctuation for the same load are also discussed.


Keywords Low carbon integrated energy systems, Natural gas price fluctuation, Carbon emission accounting, Multiobjective optimization, GWO

## 1 Introduction

In the energy industry, carbon neutrality has emerged as a prominent research topic of significant interest. China, in particular, has made a commitment to implementing robust measures aimed at achieving a carbon peak by the year 2030, followed by the ambitious goal of

[^0]carbon neutrality by 2060 [1]. Among electricity, buildings, transportation, and fossil fuels, the electricity industry has the largest carbon emission and is the key to achieving carbon neutrality [2]. In the existing research on the low-carbon transformation of the electricity industry, the concept of the Integrated Energy System (IES) enables the coordinated planning and adaptable dispatch of diverse energy systems, leading to substantial enhancements in energy utilization efficiency [3], promoting the consumption of renewable energy [4], and minimizing operational expenses plays a crucial role as a facilitator in the transition towards a low-carbon transformation process [5].

[^1]
[^0]:    *Correspondence:

    Qingshan Xu
    xuqingshan@seu.edu.cn
    ${ }^{1}$ School of Electrical Engineering, Southeast University, Nanjing, China
    ${ }^{2}$ Nanjing Center for Applied Mathematics, Nanjing, China
    ${ }^{3}$ Changzhou Power Supply Company, State Jiangsu Electric Power Co., Ltd, Changzhou, China

[^1]:    (c) The Author(s) 2023. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

IES was first put forward in [6]. It has been widely studied, taking advantage of energy coupling [7], multi-energy complementarity [8], and improved storage conversion flexibility. Heat pumps, boilers, and combined heat and power (CHP) plants are introduced in [9] to realize the coupling of electricity, thermal energy, natural gas, and other energy forms, and has been widely implemented at different scales, including the district [10], and regional levels [11] and industrial parks [12]. Early studies have demonstrated the utility of the Integrated Energy System (IES) in reducing operational costs and enhancing the integration of renewable energy sources, particularly in scenarios where processes exhibit a degree of homogeneity in [13] in which processes are relatively homogeneous.

In subsequent investigations, a two-level optimization algorithm was employed to address the lower-level objectives, aiming to minimize repetition of the original content, such as the thermal comfort of the user [14], the cost of energy storage equipment [15], and the profitability of secondary users [16]. These are combined to form a two-level model while ensuring the upper-level objectives, resulting in more comprehensive results and greater reference significance for realistic operation. On the other hand, a multi-objective model can also be constructed, encompassing various aspects such as energy cost, energy efficiency level [17], and demand response [18]. The optimization of this multi-objective model is accomplished using either Pareto optimal or heuristic algorithms, allowing for considerations of multiple objectives simultaneously.

From the viewpoint of carbon emission management in an IES, reference [19] analyzes the multi-objective functions of minimum cost and carbon emission using the Pareto frontier. The same multi-objective optimization is used in [20, 24] by using the mixed-integer programming and weight sum technique to achieve the appropriate balance between operating and emission costs.

As for the uncertainty of the volatility of energy prices, previous research has focused mainly on electricity market coupling the energy hub [21] or IES system [22], with few studies on the fluctuation of the natural gas prices. As an important energy component in IES, the purchase price of natural gas is generally fixed in past research [23, 24], while further opening of its electricity trading market in China will also liberalize the future terminal side of the natural gas market trading. Reference [25] studies the multi-objective optimization of the natural gas price fluctuation range in a distribution network and discusses the relationship between user energy cost and a flexible distribution network. Reference [25] discusses the integrated energy distribution system model to increase the robustness of the system, and considered gas price fluctuation. In [26], the PSO-ALS-optimized GRU network is used to build a long-term prediction model of natural gas price, whereas [27] uses a DBN model to build a short-term natural gas price fluctuation model and two-level optimization model to examine the relationship between user thermal comfort and energy use economy.

However, both [25, 27] only consider the economy of energy use, without considering carbon emission in the optimization results. This is not appropriate for the current situation in China. Currently, with the concept of carbon neutrality, China is setting up carbon trading centers at seven provincial levels [28], and the prices of natural gas and electricity, which are the main carriers of carbon, will be the first to affect the carbon emission and the price of carbon trading.

To provide a viable operating model for future system operators to participate in the natural gas market and carbon emission market trading, this paper develops a low-carbon economic multi-objective dispatch model of IES considering the price fluctuation of natural gas and carbon emission accounting. This explores system economic and environmental options in the light of fluctuating natural gas prices. The main contributions of this work are:A multi-objective model of IES based on natural gas price fluctuation is built, one which guarantees thermal comfort and reduces carbon emissions.A dynamic Bayesian network model (DBN) improved by particle swarm optimization (PSO) is used to study the fluctuation mechanism of natural gas price and to avoid network redundancy.An improved epsilon constraint method and fuzzy multi-weight technology are used to solve the Pareto frontier set considering system operation cost and carbon emissions, while the robustness of natural gas price fluctuation is also studied.

## 2 Framework of the integrated energy system with price fluctuation

### 2.1 Steady-state matrix of the energy hub

The IES studied in this paper, as shown in Fig. 1, contains three types of energy: electricity, heat and gas. From the user perspective, it can include the upper power grid, energy dealers, and end users. The system can include distributed energy (DG), energy hub (EH), upper power grid, upper gas network, and energy storage equipment. The distributed energy can include photovoltaic power generation (PV), wind power generation (Wind), biogas, and battery energy storage systems (BESS). Energy storage equipment can include BESS, thermal energy storage (TES), and the gas tank. Energy hub can include combined CHP units, heat pumps (HP), renewable energy sources (RES), BESS, and TES. From the perspective of

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Dispatch structure of the IES considering the price fluctuation of natural gas

energy use, the electricity demand can be met by the upper power grid, CHP, electric energy storage systems, and renewable generation equipment. The heat demand can be met by both electric boiler and electric HP, whereas the gas demand can be met by the upper gas network and gas tanks. The system adds the natural gas market component compared to the previous IES, and the impact of natural gas price fluctuation on the operating cost and carbon emission of the IES is explored.

Various converters and storage are integrated into the process of building equipment models, and equipment can be combined or coupled to meet the various energy demands of end users. This can greatly increase the flexibility and synergies in the whole system. The energy hub is a connected matrix that depicts the interaction of input and output energy [21]. The steady-state matrix of the energy hub, in which various energy carriers, storages, and converters can be divided into electricity, thermal, and gas aspects, is shown as:

$$
\left[\begin{array}{l}
L_{\mathrm{E}} \\
L_{\mathrm{H}} \\
L_{\mathrm{G}}
\end{array}\right] = \begin{bmatrix}
C_{11} & C_{12} & C_{13} \\
C_{21} & C_{22} & C_{23} \\
C_{31} & C_{32} & C_{33}
\end{bmatrix}
\begin{bmatrix}
S_{\mathrm{E}} \\
S_{\mathrm{H}} \\
S_{\mathrm{G}}
\end{bmatrix}
$$

where *L*E, *L*H, and *L*G are the electricity, thermal, and gas loads, respectively. *S*E, *S*H, and *S*G are the energy of the electricity, heat, and gas, respectively.

### 2.2 Price fluctuation model based on PSO-DBN

At present, the electricity and carbon trading markets have been opened in some provinces in China. It is expected that the natural gas price will gradually become market-oriented. Thus the price fluctuation of natural gas appears to be an inseparable part of considerations in future IES. From the existing North American and European natural gas markets, natural gas prices are related to the price of refined oil products [29]. The demand relationship, stock market fluctuation, and seasonal changes have also been proven to be vital to price fluctuation [30].

Considering the characteristics of uncertainty, nonlinearity, and 'infinite' factors, this paper uses a Bayesian network (BN) [31] to carry out various data to obtain a price fluctuation model of natural gas. Bayesian networks can be divided into Static (SBN) and Dynamic (DBN) [31]. For the SBN model, all the causality in the network structure is seen at the same time with only the value of the nodes changing, whereas the causality in the DBN model can occur between two different time points. The SBN network can be expressed as:

$$P(X_1, X_1, \dots, X_n) = \prod_{i=1}^n P(X_i|\text{parents}(X_i)) \tag{2}$$

where *parents(Xi)* is the upper node of *Xi*, parameter collection *θ* = *i*θ1, *θ2*, ..., *θn* is the conditional probability distribution, and *θi* = *P(Xi|parents(Xi)* is the conditional probability distribution of *Xi*.

In this section, the discrete Bayesian network model is built. It is suited for discrete data (polynomial function), and the joint probability distribution function of each BN is:

$$P(X[1], X[2], \dots, X[T]) = P_{Bn}(X[1]) \prod_{t=1}^{T} P_{B \to (X[t+1])|X[t])} \tag{3}$$

The transmission network between adjacent BNs is:

$$P(X[t]|X[t - 1]) = \prod_{i=1}^{N} P(X_i^l|\text{parents}(X_i^l)) \tag{4}$$

By introducing multiple influencing factors into the BN network, temporal factors can be introduced into the stationary BN network. The drivers are divided into instantaneous impact and lag factors [32], such as financial markets, sudden disasters, and hidden variables. The hidden variables here are the hidden factors that are not considered or studied in the current literature, but can have great influence on natural gas prices [32]. By introducing hidden variables, the established DBN of natural gas is closer to actual market operation. The topological structure of the DBN model and the variable names in the DBN model can be seen in [27].

When building a DBN model, the number of nodes in the hidden layer of the DBN model is usually determined by experience or experiment. It is easy to cause redundancy in the network structure. Considering that DBN uses the greedy unsupervised algorithm to train each RBM network layer by step during training, this paper uses the PSO algorithm to optimize the number of neurons in each hidden layer, so that the model can map the original signals to different feature spaces and minimize

the loss of feature information. The PSO optimization of a DBN network can be divided into the following three steps: (1) Set the basic parameters of the PSO-DBN network (including the number of particle groups, evolution times, the number of DBN network layers, etc.), and initialize the number of nodes of the hidden layer using the PSO algorithm. (2) The PSO updates the number of hidden nodes according to its particle update rules and the objective function. Once the optimal number of hidden nodes satisfying the target is found, the final network structure is determined. (3) The samples are used to train the PSO-optimized DBN network, and the greedy supervision algorithm is used to train each RBM network layer by layer to obtain the final network structure and weight parameters.

After building the PSO-DBN model, the price fluctuation probability of natural gas is calculated and shown in Table 1.

## 3 Multi-objective optimization model

This paper focuses on the two aspects of economy and carbon emission in an IES. To explore the choices, the minimum operating cost and minimum carbon emission cost are modeled as the optimization functions.

### 3.1 Minimum integrated operating costs

### 3.1.1 Latin hypercube sampling

The IES, which considers the gas market as Fig. 1 shows, contains solar energy and wind energy whose output power uncertainties have been studied extensively in recent years [33]. Meanwhile, the correlation between different distributed energy sources also needs to be considered. Therefore, a Latin hypercube sampling method is used to study the uncertain characteristics of wind power and PV output:

$$r_{\mathrm{m}, \mathrm{l}}=F_{\mathrm{Z}_{\mathrm{m}}}^{-1}\left(\frac{l-a}{L}\right) \quad m=1,2 \ldots, M, \quad l=1,2, \ldots, L$$

where $r_{\mathrm{m}, \mathrm{l}}$ is the sampling value in the $m$ th variable's $l$ th section, and $F_{\mathrm{zm}}{ }^{-1}$ is the corresponding inverse function of the cumulative distribution function (CDF). As the number of samples in LHS increases, the matrix becomes unstable when considering a symmetric positive definite matrix. This paper uses the modified alternating projections technique to locate a nearest matrix [34], and the nearest matrix can be managed to assure symmetry and positive definiteness. Equation (6) summarizes the alternate projections approach. When the number of iterations approaches infinity, the output $X$ is proven to be the desired correlation matrix represented by $P$.

$$ \begin{aligned} X & =P_{\mathrm{U}}\left(P_{\mathrm{S}}\left(P_{\mathrm{U}}\left(\ldots P_{\mathrm{S}}(P)\right)\right)\right) \rightarrow P \ P_{\mathrm{U}}(P) & =P-\operatorname{diag}\left(\operatorname{diag}(P-I)\right) \ P_{\mathrm{S}}(P) & =Z \times \operatorname{diag}\left(\max \left(v_{\mathrm{i}}, 0\right)\right) \times Z^{\mathrm{T}} \ P & =Z A Z^{\mathrm{T}} \ A & =\operatorname{diag}\left(v_{\mathrm{i}}\right) \end{aligned} $$

After using the LHS method to consider the correlation between different PV devices and wind generators, typical scenes are generated after using the backward scene reduction method [35]. Figure 2 shows the predicted output of wind and PV, in which the upper and lower district of the curves are the 2000 initial scenes of renewable energy, and the curves are the practical scenes after the backward scene reduction method.

### 3.1.2 Thermal comfort of customers

Different from the user electric load demand, the thermal load, because of its obsoleteness characteristics, means that any temperature increases or falls in the room at a certain time will not be perceived by the human body. In this paper, the interval estimation method is used to quantize the thermal comfort degree of the human body. Firstly, Predicted Mean Vote (PMV) indicators are built to estimate the thermal comfort degree, and the relation between PMV degree and the temperature is shown in Fig. 3 [36]. The equation can be expressed as:

Table 1 Conditional probability results


![img-1.jpeg](img-1.jpeg)

**Fig. 2** Output of new energy equipment

![img-2.jpeg](img-2.jpeg)

**Fig. 3** PMV degree

$$
D_{PMV} = \begin{cases}
0.9895(T - 26), & T \ge 26 \\
0.4065(-T + 26), & T < 26
\end{cases}
\tag{7}
$$

From (7), the user thermal comfort temperature is 26 °C, and according to China's ISO7730, the user thermal comfort interval is [−2.5, 2.5], indicating a temperature interval of [23.5–28.5] which the users cannot perceive. Therefore, adjusting the temperature in the room can reduce the heating capacity in the room, and the energy cost of the system and the carbon emission of the system [14], as:

$$
\text{Min}\sum_{t \in T} \text{price}_e^t \cdot (P_B^t + P_{CHP.e}^t) + \sigma \cdot (T_{\text{in}}^t + 1 - T_{\text{opt}})^2
\tag{8}
$$

where σ is a penalty factor, which can be determined from [37]. *T*<sub>in</sub><sup>t+1</sup> is the indoor temperature at the (*t* + *I*)th time slot, and *T*<sub>opt</sub> is the most comfortable temperature according to PMV.

In this paper, the heating equipment of the user is set as a CHP unit and an electric boiler. When calculating the user heat load, the thermodynamic difference of the user room is not considered, and the time domain differential thermodynamic model in [14] is uniformly adopted.

### 3.1.3 Minimum costs objective function

For the system proposed in this paper, total operating costs can be expressed by the following equation, which contains six parts, as:

$$
\min F_1 = \sum_{t=1}^{T} (F_{\text{u,t}} + F_{\text{re,t}} + F_{\text{chp,t}} + F_{\text{lo,t}} + F_{\text{con,t}} + F_{\text{o,t}}) \cdot \Delta t
$$

where *F*<sub>u,t</sub> is the cost of purchasing the electricity and the gas energy, *F*<sub>re,t</sub> is the penalty cost of wind or PV abandonment, *F*<sub>chp,t</sub> is the operating cost of the CHP unit, *F*<sub>lo,t</sub> is the cost of energy charging and discharging losses, *F*<sub>con,t</sub> is the equipment operation and maintenance cost, and *F*<sub>o,t</sub> is the heating cost penalty function for considering user thermal comfort. The above six costs are further described in (10)–(15) below, respectively.

$$
F_{\text{u,t}} = \sum_{t=1}^{T} \left[ \text{price}_e^t \cdot P_{\text{grid,t}} + \text{price}_{\text{gas}}^t \cdot V_{\text{grid,t}} \right] \cdot \Delta t
$$

where *price*<sub>g</sub><sup>t</sup> is the electricity price at the *t*th period, *price*<sub>gas</sub><sup>t</sup> is the gas price at the *t*th period, *P*<sub>grid,t</sub> is the electricity purchased from the upper grid at the *t*th period, and *V*<sub>grid,t</sub> is the gas quantity purchased from the upper network at the *t*th period.

$$
F_{\text{re,t}} = \sum_{t=1}^{T} \left[ \lambda_w \cdot (P_{\text{w,t}}^t - P_{\text{w,t}}^{\text{act}}) \right] \cdot \Delta t
$$

where *λ*<sub>w</sub> is the unit penalty of abandoning wind power, while *P*<sub>wind,t</sub><sup>t</sup> and *P*<sub>wind</sub><sup>t</sup> are the forecast and actually used power of wind generators at the *t*th time slot, respectively. *λ*<sub>p</sub> is the unit penalty of abandoning PV power, while *P*<sub>pv,t</sub><sup>t</sup> and *P*<sub>pv</sub><sup>t</sup> are the forecast and actually used PV power at the *t*th time slot, respectively.

$$
F_{\text{chp,t}} = \sum_{t=1}^{T} \left[ \lambda_{\text{on}}^{\text{chp}} \cdot u_t \cdot (1 - u_{t-1}) + \lambda_{\text{off}}^{\text{chp}} \cdot u_{t-1} \cdot (1 - u_t) \right] \cdot \Delta t
\tag{12}
$$

where *λ*<sub>on</sub><sup>CHP</sup> and *λ*<sub>off</sub><sup>CHP</sup> are the start-up/ shut-down costs of the CHP unit, *u*<sub>t</sub> is the binary variable of 1 or 0 representing on or off state of the CHP at the *t*<sup>th</sup> time slot.

$$
\begin{aligned}
F_{\text {lo,t }}=\sum_{t=1}^{T} \lambda_{\text {loss }} \cdot\left[P_{\mathrm{ch}, \mathrm{t}} \cdot\left(1-\eta_{\mathrm{e}}^{\mathrm{ch}}\right)+P_{\mathrm{dis}, \mathrm{t}} \cdot\left(1-\eta_{\mathrm{e}}^{\mathrm{dis}}\right)\right] \cdot \Delta t \\
+\sum_{t=1}^{T} \lambda_{\text {loss }} \cdot\left[V_{\mathrm{ch}, \mathrm{t}} \cdot\left(1-\eta_{\text {tank }}^{\mathrm{ch}}\right)+V_{\mathrm{dis}, \mathrm{t}} \cdot\left(1-\eta_{\text {tank }}^{\mathrm{dis}}\right)\right] \cdot \Delta t
\end{aligned}
$$

where $\lambda_{\text {loss }}$ is the cost of the energy loss, $P_{\mathrm{ch}, \mathrm{t}}$ and $P_{\text {dis,t }}$ are the charging and discharging power of the BESS at the $t$ th time slot, respectively. $\eta_{\mathrm{e}}^{\text {ch }}$ and $\eta_{\mathrm{e}}^{\text {dis }}$ are the charging and discharging efficiencies of the BESS, respectively.

$$
\begin{aligned}
& E_{\text {grid,co }_{2}}^{\star}=\beta_{\mathrm{e}}^{\star} \cdot \sum_{t=1}^{T} P_{\text {grid,t }} \cdot \Delta t \\
& E_{\text {gas,co }_{2}}^{\star}=\beta_{\mathrm{h}}^{\star} \cdot \sum_{t=1}^{T} V_{\text {grid,t }} \cdot \Delta t \\
& E_{\text {co }_{2}}=E_{\text {grid,co }_{2}}+E_{\text {gas,co }_{2}}
\end{aligned}
$$

$$
F_{\text {con,t }}=\sum_{t=1}^{T}\left[\alpha_{\mathrm{chp}} \cdot P_{\mathrm{chp}, \mathrm{t}}+\alpha_{\mathrm{eb}} \cdot P_{\mathrm{eh}, \mathrm{t}}+\alpha_{\mathrm{pv}} \cdot P_{\mathrm{pv}, \mathrm{t}}^{\mathrm{f}}+\alpha_{\text {wind }} \cdot P_{\mathrm{w}, \mathrm{t}}^{\mathrm{f}}+\alpha_{\text {BESS }} \cdot\left(P_{\mathrm{ch}, \mathrm{t}}+P_{\mathrm{dis}, \mathrm{t}}\right)+\alpha_{\text {tank }} \cdot\left(V_{\mathrm{ch}, \mathrm{t}}+V_{\mathrm{dis}, \mathrm{t}}\right)\right] \cdot \Delta t
$$

where $\alpha_{\text {chp }}, \alpha_{\text {eb }}, \alpha_{\text {wind }}, \alpha_{\text {BESS }}, \alpha_{\text {tank }}$, and $\alpha_{\mathrm{pv}}$ are the maintenance charges of the CHP unit, electric boiler, wind power unit, BESS, gas tank, and PV power unit, respectively.

$$
F_{\sigma, \mathrm{t}}=\sum_{t=1}^{T} \sigma \cdot\left(T_{\mathrm{in}}^{\mathrm{t}+1}-T_{\mathrm{opt}}\right)^{2} \cdot \Delta t
$$

where $\sigma$ is the penalty factor, $T_{\mathrm{in}}{ }^{\mathrm{t}+1}$ is the indoor temperature at the $(t+I)$ th time slot, and $T_{\text {opt }}$ is the most comfortable temperature people feel indoors.

### 3.1.4 Minimum carbon emissions

In China, carbon credits are generally distributed by the government. For producers and operators, carbon credit surplus or deficit can be traded in carbon trading markets. In this paper, the electricity purchased from the upper grid comes from thermal power, and the reference line method is adopted to determine the free carbon emission of the system. By reducing the actual carbon emission minus the free carbon emission obtained from the market purchase, the carbon emission generated by the actual operation of each piece of equipment in the system is obtained.

$$
\min F_{2}=\sum_{t=1}^{T} C_{\mathrm{em}} \cdot \Delta t
$$

where $F_{2}$ is carbon emission and $C_{\mathrm{em}}$ is the amount of actual carbon emission.

$$
C_{\mathrm{em}}=E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{\star}
$$

where $E_{\text {co2 }}$ is the amount of total carbon emission and $E_{\text {co2 }}{ }^{\prime}$ is the amount of free carbon emission.

$$
E_{\mathrm{co}_{2}}^{\star}=E_{\text {grid,co }_{2}}^{\star}+E_{\text {gas,co }_{2}}^{\star}
$$

$$
E_{\text {grid,co }_{2}}=\beta_{\mathrm{e}} \cdot \sum_{t=1}^{T} P_{\text {grid,t }} \cdot \Delta t
$$

$$
E_{\text {gas,co }_{2}}=\beta_{\mathrm{h}} \cdot \sum_{t=1}^{T} V_{\text {grid,t }} \cdot \Delta t
$$

where $E_{\text {grid,co2 }}$ and $E_{\text {grid,co2 }}{ }^{\prime}$ are the amounts of total carbon emission and free carbon emission coming from the upper grid purchased, respectively. $E_{\text {gas,co2 }}$ and $E_{\text {gas,co2 }}{ }^{\prime}$ are the amounts of total carbon emission and free carbon emission coming from the gas purchased, respectively. $\beta_{\mathrm{e}}$ and $\beta_{\mathrm{h}}$ are the respective carbon emissions per unit electricity and heat, while $\beta_{\mathrm{e}}{ }^{\prime}$ and $\beta_{\mathrm{h}}{ }^{\prime}$ are the free carbon emissions per unit electricity and heat, respectively.
There are currently seven provincial carbon trading centers in China, and carbon trading prices fluctuate with the number of transactions and trading hours per day. There is no specific literature on carbon trading prices. In future research, a detailed study of the carbon trading price will be conducted to more accurately describe the cost of carbon trading for users. This paper adopts the ladder penalty mechanism to define the carbon trading price [38], and the specific carbon trading price is expressed in (24) [39].
As expressed in (24), if the actual carbon emission of the operator is less than the rated carbon emission, the operator can make a profit from selling the extra rated carbon emission to others, while the price of carbon emission quota is inversely proportional to the amount of selling carbon emission. On the contrary, the operator needs to enter the carbon trading market to buy a missing carbon emission quota. When the actual carbon emission of the operator is greater than the sum of the rated carbon emission and the carbon emission amount allowed to trade from the market, the operator also needs to pay a penalty for the excess amount,

with the penalty increasing proportionally as the excess amount increases.

$$
\operatorname{price}_{\mathrm{co}_{2}, \mathrm{t}}=\left\{\begin{array}{l}
-c h-c(1+\partial)\left(E_{\mathrm{co}_{2}}^{*}-E_{\mathrm{co}_{2}}-h\right) \\
-c\left(E_{\mathrm{co}_{2}}^{*}-E_{\mathrm{co}_{2}}\right) \\
c\left(E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*}\right) \\
c h+c(1+\partial)\left(E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*}-h\right) \\
c(2+\partial) h+c(1+2 \partial)\left(E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*}-2 h\right) \\
c(3+3 \partial) h+c(1+3 \partial)\left(E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*}-3 h\right) \\
c(4+6 \partial) h+c(1+4 \partial)\left(E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*}-4 h\right)
\end{array} \begin{array}{l}
E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq-h \\
-h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 0 \\
0<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq h \\
h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 2 h \\
2 h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 3 h \\
3 h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 4 h \\
4 h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*}
\end{array}\right.
$$

where $c$ is the benchmark price of carbon emission, $h$ is the carbon credits at different stages, and $a$ is the penalty increase factor.

### 3.1.5 Network constraint

As well as the multi-objective functions, the typical constraints of the proposed IES can be divided into five parts. A nonlinear quadratic model appears in CHP unit constraints and constraints of natural gas pipelines. For quadratic problem solving, it is necessary to ensure the convexity of the problem, so piecewise linear functions have been used to ensure the determined size and the specific method [40].
3.1.5.1 Equipment output and input constraints All the equipment in this paper works within the normal range of equipment output, i.e., the maximum output does not exceed the rated maximum output, the minimum output is not lower than the rated minimum output, the maximum input does not exceed the rated maximum input, and the minimum input is not lower than the rated minimum input.

$$
\begin{aligned}
P_{\text {out }}(t) & =\eta \cdot P_{\text {in }}(t) \\
P_{\text {in }}^{\min } & \leq P_{\text {in }}(t) \leq P_{\text {in }}^{\max }
\end{aligned}
$$

where $P_{\text {out }}(\mathrm{t})$ and $P_{\text {in }}(\mathrm{t})$ are the output and input power of the equipment at the $t$ th time slot, respectively. $\eta$ is the conversion efficiency of the equipment. $P_{\text {in }}{ }^{\text {min }}$ and $P_{\text {in }}{ }^{\text {max }}$ are the minimum and maximum inputs of the equipment, respectively.
3.1.5.2 Battery constraints State of charge (SOC) indicates the battery's remaining capacity, and (26) prevents the overcharging and over-discharging of battery, as:
$S O C_{\mathrm{BES}, \mathrm{t}}=S O C_{\mathrm{BES}, \mathrm{t}-\Delta t}+\frac{\eta_{\mathrm{e}}^{\mathrm{ch}} P_{\mathrm{ch}, \mathrm{t}-\Delta t} \Delta t}{E_{\mathrm{e}}}-\frac{P_{\mathrm{dis}, \mathrm{t}-\Delta t} \Delta t}{\eta_{\mathrm{e}}^{\mathrm{dis}} E_{\mathrm{e}}}$
where $E_{\mathrm{e}}$ is the electric quantity of the battery energy system.

The real-time charging and discharge of battery storage meet the constraints of maximum charging power and

$$
\begin{aligned}
& E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq-h \\
& -h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 0 \\
& 0<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq h \\
& h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 2 h \\
& 2 h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 3 h \\
& 3 h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*} \leq 4 h \\
& 4 h<E_{\mathrm{co}_{2}}-E_{\mathrm{co}_{2}}^{*}
\end{aligned}
$$

maximum discharge power, and the dual variable is used to restrict the battery storage to only charge or discharge at the same time.

$$
\begin{aligned}
& P_{\mathrm{ch}, \mathrm{t}} \leq P_{\mathrm{ch}, \max } \cdot k_{\mathrm{t}} \\
& P_{\mathrm{dis}, \mathrm{t}} \leq P_{\mathrm{dis}, \max } \cdot r_{\mathrm{t}} \\
& k_{\mathrm{t}}+r_{\mathrm{t}} \leq 1
\end{aligned}
$$

where $P_{\mathrm{ch}, \max }$ and $P_{\mathrm{dis}, \max }$ are the maximum allowed charging and discharging power, respectively, while $k_{\mathrm{t}}$ and $r_{\mathrm{t}}$ are all binary variables.
3.1.5.3 Natural gas storage constraints The SOC of a natural gas storage tank should be limited to the abovementioned battery constraints [14], as:

$$
\begin{aligned}
& V_{\text {bio,t }}=V_{\text {bio,t }-\Delta \mathrm{t}}+V_{\mathrm{GCS}, \mathrm{t}-\Delta \mathrm{t}}-V_{\mathrm{GDS}, \mathrm{t}-\Delta t} \\
& V_{\text {bio,min }} \leq V_{\text {bio,t }} \leq V_{\text {bio,max }} \\
& 0 \leq V_{\mathrm{GCS}, \mathrm{t}} \leq f_{\text {gas.t }} \cdot V_{\mathrm{GCS}, \max } f_{\text {gas.t }} \\
& \quad \in\{0,1\} \\
& 0 \leq V_{\mathrm{GDS}, \mathrm{t}} \leq\left(1-f_{\text {gas.t }}\right) V_{\mathrm{GDS}, \max } f_{\text {gas.t }} \\
& \quad \in\{0,1\}
\end{aligned}
$$

where $V_{\text {bio,t }}$ is the SOC of biogas tank at the $t$ th time slot, while $V_{\text {bio,min }}$ and $V_{\text {bio,max }}$ are the minimum and maximum storage of the biogas tank, respectively. $V_{\mathrm{GDS}, \mathrm{t}}$ and $V_{\mathrm{GCS}, \mathrm{t}}$ are the amounts of gas tank provided and purchased at the $t$ th time slot, respectively. $V_{\mathrm{GDS}, \min }$, $V_{\mathrm{GCS}, \min }$, and $V_{\mathrm{GDS}, \max }, V_{\mathrm{GCS}, \max }$ are the lower and upper speeds of the gas tank charge or discharge, respectively. $f_{\text {gas,t }}=0$ means the gas tank at the discharging state, while $f_{\text {gas,t }}=1$ indicates the gas tank at the charging state.
3.1.5.4 CHP unit constraints In this paper, the output characteristics of CHP unit are considered. The power change of CHP unit per unit of time should meet certain

constraints, and the secondary nonlinear convex function is used to describe the output characteristics of the CHP unit [41], as:

$$
\begin{aligned}
Q_{\mathrm{CHP}, \min } & \leq P_{\mathrm{CHP}, \mathrm{t}} \eta_{\mathrm{h}}^{\mathrm{CHP}} / \eta_{\mathrm{e}}^{\mathrm{CHP}} \\
& \leq Q_{\mathrm{CHP}, \max } \\
\left|P_{\mathrm{CHP}, \mathrm{t}}-P_{\mathrm{CHP}, \mathrm{t}-\Delta \mathrm{t}}\right| & \leq \text { ramp } \\
G L_{\mathrm{t}} & =a_{1}+b_{1} \cdot P_{\mathrm{CHP}, \mathrm{t}}+c_{1} \cdot\left(P_{\mathrm{CHP}, \mathrm{t}}\right)^{2}
\end{aligned}
$$

where ramp is the ramp rate of the CHP unit. $Q_{\mathrm{CHP}, \min }$ and $Q_{\mathrm{CHP}, \max }$ are the lower and upper limits of the thermal output of the CHP unit, respectively. $G L_{\mathrm{t}}$ is the gas consumption of the CHP unit at the $t^{\text {th }}$ time slot, and $a_{1}$, $b_{1}$, and $c_{1}$ are the gas consumption coefficients.
3.1.5.5 The constraints of a natural gas pipeline The natural gas pipeline model is partially simplified before modeling in [14], e.g., excluding the temperature change of natural gas during pipeline transmission, the friction of natural gas between pipeline and pipe wall, and the variation of compression ratio of a natural gas compression station. After simplification, the transmission model of natural gas in the pipeline can be derived from the law of conservation of energy and flow conservation, as:

$$
\begin{aligned}
& \omega_{\mathrm{j}, \mathrm{t}}+\sum_{i j \in Z(j)} \omega_{\mathrm{ij}, \mathrm{t}}=\sum_{j k \in v(j)} \omega_{\mathrm{jk}, \mathrm{t}} \\
& \omega_{\mathrm{ij}, \mathrm{t}}+\omega_{\mathrm{jk}, \mathrm{t}}=0 \\
& \omega_{\mathrm{j}, \mathrm{t}}=\omega_{\mathrm{j}, \mathrm{t}}^{\text {well }}-\omega_{\mathrm{j}, \mathrm{t}}^{\mathrm{CHP}}-\omega_{\mathrm{j}, \mathrm{t}}^{\text {load }} \\
& \omega_{\mathrm{ij}, \mathrm{t}}=C_{\mathrm{ij}} \sqrt{\left|\psi_{\mathrm{t}, \mathrm{t}}^{2}-\psi_{\mathrm{j}, \mathrm{t}}^{2}\right|} \\
& \psi_{\min } \leq \psi_{\mathrm{i}, \mathrm{t}} \leq \psi_{\max } \\
& \omega_{\mathrm{ij}, \min } \leq \omega_{\mathrm{ij}, \mathrm{t}} \leq \omega_{\mathrm{ij}, \max } \\
& 0 \leq \omega_{\mathrm{j}, \mathrm{t}}^{\text {loadcut }} \leq \omega_{\mathrm{j}, \mathrm{t}}^{\text {load }}
\end{aligned}
$$

where $\omega_{\mathrm{ij}, \mathrm{t}}$ is the gas flow from node $i$ to node $j$ in the gas network at the $t$ th time slot, and $\omega^{\text {well }}{ }_{\mathrm{j}, \mathrm{t}}$ is the gas flow of node $j$ from the gas source at the $t$ th time slot. $\omega^{\text {chp }}{ }_{\mathrm{j}, \mathrm{t}}$ and $\omega^{\text {load }}{ }_{\mathrm{j}, \mathrm{t}}$ are the gas consumption of the CHP unit and gas load of the node $j$ at the $t$ th time slot, respectively. $Z(j)$ is the set of gas pipelines which set the node $j$ as the end node, while $v(j)$ is the set of gas pipelines which set the
node $j$ as the start node. $\psi_{\mathrm{i}, \mathrm{t}}$ is the gas pressure of the node $i$ at the $t$ th time slot, while $\psi_{\min }$ and $\psi_{\max }$ are the minimum and maximum gas pressures of the node at the $t$ th time slot, respectively. $\omega_{\mathrm{ij}, \min }$ and $\omega_{\mathrm{ij}, \max }$ are the respective minimum and maximum gas flows of the gas pipeline from node $i$ to node $j$, and $C_{\mathrm{ij}}$ is the pipeline constraint of a gas pipeline from node $i$ to node $j$.

## 4 Solution method

Based on the multi-objective model built in the previous section, the Grey Wolf Optimization (GWO) algorithm is used first. This considers the quadratic form of the objective function. The multi-objective solution method based on the improved epsilon constraint is then used to examine the Pareto frontier sets, and finally, fuzzy multiweight technology is used to determine the optimal result.

### 4.1 The grey wolf algorithm

The GWO algorithm is a neoteric bio-intelligence algorithm proposed by Mirjalili [42], which is based on wolf pack group intelligence. It simulates the wolf wandering, summoning, and sieging behaviors, and the head wolf generation rules. This algorithm can integrate the genetic algorithm (GA) and basic PSO algorithm with all their advantages, and use a nonlinear control parameter to guarantee a more rapid convergence rate of late iteration.

In this paper, GWO is used to solve the minimum integrated operating cost in (25), which contains a quadratic form. Assuming the spatial dimension of the optimal solution of integrated operating cost is $d$ and the number of the wolves is $N$, the location of $i$ th wolf is given as:

$$
X_{\mathrm{i}}=\left\{X_{\mathrm{i}}^{1}, X_{\mathrm{i}}^{2}, \ldots, X_{\mathrm{i}}^{\mathrm{d}}\right\}, i=1,2, \ldots, N
$$

Using $a, b$ and $c$ to represent the first, second, and third optimal solutions of the whole wolf pack, respectively, the range of the target solution can be expressed as [42]:

$$
X(t+1)=X_{\mathrm{p}}(t)-A \cdot\left|c \cdot X_{\mathrm{p}}(t)-X(t)\right|
$$

where $t$ is the iteration number, $X \mathrm{p}(\mathrm{t})$ is the location of the optimal solution, while $X(t)$ and $X(\mathrm{t}+1)$ express the location changes between the adjacent location of the optimal solution. $A$ is convergence factor, $c$ is a swing factor, and the computational formulas are:

$$
\begin{aligned}
& A=2 a \cdot r_{1}-a \\
& c=2 \cdot r_{2}
\end{aligned}
$$

where $r_{1}$ and $r_{2}$ are random numbers between $[0,1] . a$ is a distance controlling parameter, given as:

where T_{max} is the maximum number of iterations. a_{ini} and a_{fin} are the initial and end values, respectively.

Using (46) and (47) to get the locations of a, b, and c as:

$$
\begin{aligned}
& \left\{\begin{array}{l}
X_{1}(t+1)=X_{\mathrm{a}}(t)-A_{1} \cdot \mid c_{1} \cdot X_{\mathrm{a}}(t)-X(t) \mid \\
X_{2}(t+1)=X_{\mathrm{b}}(t)-A_{2} \cdot \mid c_{2} \cdot X_{\mathrm{b}}(t)-X(t) \mid \\
X_{3}(t+1)=X_{\mathrm{c}}(t)-A_{3} \cdot \mid c_{3} \cdot X_{\mathrm{c}}(t)-X(t) \mid
\end{array}\right. \\
& X_{\text {next }}(t+1)=\frac{X_{1}(t+1)+X_{2}(t+1)+X_{3}(t+1)}{3}
\end{aligned}
$$

where X_{next}(t+1) is the location for the next iteration, and X_{a} is the optimal solution of GWO.

### 4.2 Multi-objective optimization with epsilon constraint

Given that the two optimization models proposed in Sect. 3 are minimized objective functions, the intrinsic connection between the minimum operating cost and the minimum carbon emission is difficult to determine. Therefore, this paper uses the improved epsilon constraint method to solve multi-objective models. This helps to examine the choice between economy and low-carbon in different Pareto frontier sets [25]. As the basal epsilon constraint method tends to maldistributed Pareto frontier sets [43], the improved epsilon method adopted in this paper uses the utopia line [44] to improve the uniformity of the Pareto frontier set distribution. To reduce the influence of the order of magnitude and dimension of the objective functions on the final result, the formal optimization results are normalized as:

$$
\begin{aligned}
& F_{1}(x)=\frac{F_{1}^{\prime}(x)-F_{1}^{*}\left(x_{1}^{*}\right)}{F_{1}^{*}\left(x_{2}^{*}\right)-F_{1}^{*}\left(x_{1}^{*}\right)} \\
& F_{2}(x)=\frac{F_{2}^{\prime}(x)-F_{2}^{*}\left(x_{2}^{*}\right)}{F_{2}^{*}\left(x_{1}^{*}\right)-F_{2}^{*}\left(x_{2}^{*}\right)}
\end{aligned}
$$

where F_{1}' is defined as the minimum integrated operating cost, and F_{2}' is defined as the minimum carbon emission. x_{1}* and x_{2}* represent the optimal results of F_{1}' and F_{2}', respectively.

The Pareto frontier can be obtained by optimizing (50) and (51), and iteratively adjusting the essential parameters ε2,k.

After determining the Pareto frontier, we use fuzzy multi-weight technology to determine the score of each solution belonging to the optimal target level of membership and then the optimal solution. The detailed calculations are:

$$
\begin{aligned}
& F U Z Z Y_{\mathrm{i}, \mathrm{k}}=\alpha_{\mathrm{i}} \vartheta_{\mathrm{i}, \mathrm{k}}^{\mathrm{u}}+\beta_{\mathrm{i}} \vartheta_{\mathrm{i}, \mathrm{k}}^{\mathrm{m}}+\gamma_{\mathrm{l}} \vartheta_{\mathrm{i}, \mathrm{k}}^{\mathrm{l}} \\
& \vartheta_{\mathrm{i}, \mathrm{k}}^{\mathrm{u}}=\frac{F_{\mathrm{i}, \text { pumax }}-F_{\mathrm{i}, \mathrm{pu}, \mathrm{k}}}{F_{\mathrm{i}, \text { pumax }}-F_{\mathrm{i}, \text { pumin }}} \\
& \vartheta_{\mathrm{i}, \mathrm{k}}^{\mathrm{m}}=\left\{\begin{array}{l}
\frac{F_{\mathrm{i}, \text { pumax }}-F_{\mathrm{i}, \mathrm{pu}, \mathrm{k}}}{F_{\mathrm{i}, \text { pumax }}-F_{\mathrm{i}, \text { pumear }}}, F_{\mathrm{i}, \mathrm{pu}, \mathrm{k}} \geq F_{\mathrm{i}, \text { pumearn }} \\
\frac{F_{\mathrm{i}, \mathrm{pu}, \mathrm{k}}-F_{\mathrm{i}, \text { pumin }}}{F_{\mathrm{i}, \text { pumearn }}-F_{\mathrm{i}, \text { pumin }}}, F_{\mathrm{i}, \mathrm{pu}, \mathrm{k}} \leq F_{\mathrm{i}, \text { pumearn }}
\end{array}\right. \\
& \vartheta_{i, k}^{l}=\frac{F_{\mathrm{i}, \mathrm{pu}, \mathrm{k}}-F_{\mathrm{i}, \text { pumin }}}{F_{\mathrm{i}, \text { pumax }}-F_{\mathrm{i}, \text { pumin }}}
\end{aligned}
$$

Equations (53)–(55) are the values of the objective function's upper, middle, and lower membership degrees at the kth iteration, respectively. F_{i,pumearn} represents the objective function's average, and the final solution of each objective function can obtain the final objective result, as:

$$
\begin{aligned}
\mathrm{OBJ}^{*} & =\left[F_{1}, \mathrm{pu}^{*}, F_{2}, \mathrm{pu}^{*}, \ldots . . F_{\mathrm{i}, \mathrm{pu}}^{*}\right] \\
F_{\mathrm{i}, \mathrm{pu}}^{*} & =\max \left(F U Z Z Y_{\mathrm{i}, \mathrm{k}}\right)
\end{aligned}
$$

### 4.3 Flowchart of solution process

The flowchart of the solving process is shown in Fig. 4 and can be divided into 3 parts. The left part is the GWO optimization, which is used to solve the quadratic convex function (8). The middle part and the right part are the processes of multi-objective optimization with epsilon constraint. Compared with previous research, the right part shows the fuzzy multi-weight technology which is used to determine the score of each solution belonging to the optimal target level of membership. All the equations can be seen in Fig. 4.

## 5 Case studies

### 5.1 Basic configurations

The system architecture for the case studies is shown in Fig. 5, in which the power grid connects a 1200 kWh BESS, PV equipment, and wind turbine. The network encompasses four nodes, namely the upper gas field, gas tank, Combined Heat and Power (CHP) unit, and residential consumers, which collectively facilitate gas utilization. To meet the thermal load demands, two potential sources are available: an electric boiler with an installed capacity of 800 kW and a CHP unit with an installed capacity of 3300 kW . Detailed specifications of the remaining units are provided in Table 2, while Fig. 6 graphically represents the 24-h profiles of electric load and gas load for a typical winter's day. Pertinent information regarding predicted temperature and electricity price can be found in Fig. 7. The baseline

![img-3.jpeg](img-3.jpeg)

**Fig. 4** Flowchart of the multi-objective optimization method

![img-4.jpeg](img-4.jpeg)

**Fig. 5** Structure of the IES network

gas price is fixed at 2.73 m³/¥, while its fluctuation adheres to the model presented in Sect. 2. For additional insight, the intricate parameters governing the natural gas networks can be found in [14]. This case is implemented in MATLAB R2020b and the commercial optimization solver Gurobi (Version 9.1.2).

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

**Fig. 6** Predicted gas load and power load

### 5.2 Analysis of multi-objective optimization

#### 5.2.1 Energy consumption

Figure 8a and b show the electrical output and gas output of the IES when the system operating strategy is to minimize operating cost (MOC). In comparison, Fig. 9a and b show the electricity and gas outputs when the system operating strategy is to minimize carbon emission (MEC). As can be seen in Figs. 8a and 9a, when the system operating strategy is MEC, the output of the electric boiler is reduced, and the CHP unit is used as the main heat source. Upper trading with the grid also decreases as the system reduces carbon emission. As can be seen in Figs. 8b and 9b, the system will correspondingly increase its purchases to the upper gas grid when in MEC.

From Table 3, it can be seen more intuitively that in MEC, the operating cost of the system will increase. In terms of energy purchase, the purchases from the upper grid and gas network are increased, and the dependence on external energy sources is greater. In terms of renewable energy sources, because of the increased dependence on external energy sources, the consumption of new energy sources is reduced to a certain extent, and

![img-7.jpeg](img-7.jpeg)

**Fig. 8** Electrical and gas outputs of MOC

The amount of wind and PV abandoned is expanded. In terms of energy transmission, electrical energy storage and gas tank are used more frequently. For heating, the penalty cost for misjudging the thermal comfort of users becomes greater, the carbon emission of the system is reduced, but the thermal comfort of the system is also reduced.

### 5.2.2 Carbon emission

Table 4 presents the carbon emissions data for the system in two different operational modes, namely the Mode of Electricity Consumption (MEC) and the Mode of Gas Consumption (MOC). Additionally, Fig. 10 illustrates the specific carbon emissions associated with electricity and gas purchases on each occasion. A notable finding in MEC is the substantial reduction in electricity purchased from the upper tier, resulting in a decrease in carbon emissions. This reduction in electricity purchase can be effectively compensated for by the thermoelectric coupling of the CHP unit, enabling it to meet the reduced electrical load demand while simultaneously fulfilling the heat supply requirements that would have otherwise relied on the electric boiler's output. Consequently, the economic viability of directly purchasing electricity at the terminal is found to surpass that of purchasing gas directly at the terminal. Moreover, the direct terminal purchase of electricity exhibits lower carbon emissions than the direct terminal purchase of gas.

The MEC mode can also increase the frequency of gas tank use and the independence of the gas system. In summary, electricity is more economical, and gas is less carbon-intensive in a small integrated energy system for end-users.

Table 3 Operating costs of MOC and MEC


5.2.3 Storage equipment

The IES built in this paper contains two types of energy

Table 4 Carbon emissions of MOC And MEC


![img-8.jpeg](img-8.jpeg)

Fig. 10 Carbon emissions of MOC and MEC
storage device, i.e., BESS and gas tank. As can be seen in Table 5, MEC increases the energy transfer cost of the system, which is the frequency of use of the energy storage devices. Figure 11a and b show specifically the usages of the two different energy storage devices for the different modes of operation. It can be seen that BESS varies more during the period of $3 \mathrm{am}-10 \mathrm{am}$, during which the MEC mode gives priority to the use of batteries to meet the electricity demand of the users. For the gas tank, also during the $3-10$ am period, the MEC mode increases the amount of gas saved in the upper gas layer, while during the peak gas consumption period of $2-7 \mathrm{pm}$, because of the capacity of the gas pipeline transmission, it gives priority to the use of storage tanks to meet the gas demand. This analysis shows that the reduction in carbon emission reduces the dependence of the system on the upper grid, while it uses CHP equipment and electric storage to meet the electricity demand of customers, with CHP equipment being used mainly during daytime hours and BESS late at night when the electricity price is low.

### 5.3 Performance of Pareto optimal solution

The study presents the optimal results of MOC and MEC using the proposed multi-objective optimization algorithm based on the improved epsilon constraint method. This algorithm is applied to determine the optimal objective N in MOC and the optimal objective M in MEC. Additionally, fuzzy multi-weight technology is employed to obtain a compromise solution P that gives priority to both objectives M and N . The

![img-9.jpeg](img-9.jpeg)

**Fig. 11** BESS and gas tank of MOC and MEC

Pareto frontier is constructed using twenty optimal solutions lying between M and N, and the results are illustrated in Fig. 12, with a subset of these solutions presented in Table 6. The analysis of Table 6 reveals that the optimal solution N achieves a cost reduction of 1.8% compared to the compromise solution P, but it comes with a trade-off of 4.6% higher carbon emissions. On the other hand, the optimal solution M exhibits a noteworthy reduction of 7% in carbon emissions; however, it incurs an 8% higher cost when compared to the compromise solution P. These findings highlight the trade-offs between cost and environmental impact, underscoring the importance of the proposed multi-objective optimization approach in decision-making processes. Table 7 shows the specific results of the compromise solution P. To balance the minimum operating cost with minimum carbon emission, the operator of this IES can select the appropriate operating mode from the Pareto frontier in Fig. 12 according to the actual demand for economy and environmental friendliness by policy or actual energy use, while the compromise solution P in this section is more biased towards the minimum carbon emission in the selection of the operating mode.

### 5.4 Robustness of natural gas price fluctuation

In Fig. 12, the red and black curves represent the Pareto curve of the system for fluctuating and constant

![img-10.jpeg](img-10.jpeg)

**Fig. 12** Pareto frontier of the two cases

Table 6 Results of Oareto Froniter of the two cases


Table 7 Results of compromise solution P


Table 8 Results of compromise solution P without gas price fluctuation


natural gas prices, respectively. It can be seen from the above analysis that, when the price of natural gas fluctuates, because the price of natural gas in the next stage is easily affected by the purchase volume of the previous stage while it is difficult to maintain in a small range, the price of natural gas in the system is higher than the initial value. Therefore, in MOC, the operating cost of the IES under the fluctuating natural gas price will be greater than that of the IES under constant natural gas price, while the carbon emission under the condition of natural gas price fluctuation is also greater than that under constant natural gas price. For MEC, the system carbon emission under natural gas price fluctuation is greater than that when the natural gas price is constant. Unit gas carbon emission is less than unit electricity carbon emission, and therefore, the system in MEC will greatly increase the use of natural gas and reduce the system for the upper grid purchase under natural gas price fluctuation, resulting in higher system carbon emission. However, for the operating cost of the system, when the gas price is constant, the system operating cost is lower. The results of compromise solution P without gas price fluctuation can be seen in Table 8.
![img-11.jpeg](img-11.jpeg)

Fig. 13 Gas prices of MOC and MEC

### 5.5 Impact of natural gas price fluctuation

The DBN model is used here to predict price fluctuation in the natural gas market. Figure 13 shows the natural gas price fluctuation curves when the system is run

![img-12.jpeg](img-12.jpeg)

**Fig. 14** Pareto frontier with different price fluctuation extents

with MOC and MEC. It can be seen for the day-ahead gas trading market that the magnitude of gas price fluctuation is not very large. With MEC, the system has a smoother gas trading price between 2 and 8 pm, and the trading price is lower than with MOC. When the system gas load reaches its peak, the system tends to purchase gas on a large scale to meet the multiple energy needs of its customers, while the presence of the gas tank reduces the variation of adjacent gas purchases. In contrast, a system with MOC procures electrical energy to meet the electrical and thermal energy needs of customers, so natural gas purchases are mainly influenced by fluctuation in gas load and cannot reduce the volatility of natural gas in adjacent periods in the same way as MEC reduces the volatility of natural gas through the coordination of multiple energy coupling devices. Reducing carbon emission will, to a certain extent, reduce the system's gas purchase cost and price fluctuation of the gas market.

The extent of natural gas price fluctuation in the short-term market is also discussed in this section. Figure 14 shows the Pareto frontier set of system operating costs and carbon emissions for natural gas price fluctuations, based on the DBN prediction model presented in Sect. 2, with the fluctuations reduced to 0.8 times, held constant, and increased to 1.2 times. The analysis of the graph shows that the fluctuation of the natural gas price affects the economy and environmental friendliness of the system to a certain extent, and that the lower the fluctuation of the natural gas price, the smaller the system operating cost and carbon emission for the same load. In the future, price fluctuation in the natural gas market will become increasingly important in the operation of integrated energy systems, especially as electricity trading is now generally on a time-of-use basis, and the market price of natural gas will be an important factor in the carbon emissions of customers. The size of a customer's carbon emission also determines the amount of carbon emission and the price at which the customer can participate in the carbon trading market, so the prices of natural gas and carbon trading will become increasingly linked in the future energy market.

## 6 Conclusion

This paper has used the improved epsilon constraint method and fuzzy multi-weight technology to solve the Pareto frontier set considering system operation cost and carbon emission. The results show that: (1) The Pareto solution is more biased towards the minimum carbon emission in the selection of the operating mode as the operating cost is 43,902 ¥ and carbon emission is 15,425 kg, respectively; (2) Electricity is more economical, while gas is less carbon-intensive in a small IES for end-users; (3) Reducing carbon emission will, to a certain extent, reduce the system's gas purchase cost and price fluctuation of the gas market, and the lower the fluctuation of the natural gas price, the smaller the system operating cost and carbon emission for the same load.

This paper provides a guiding role for operators in dealing with the price uncertainty factors of the fully open domestic natural gas market in the future and has significance in comparing economic and environmental aspects. However, the DBN model for natural gas price fluctuation for medium to long-term market is not discussed and the carbon trading price based on a ladder penalty mechanism is not suitable for just-in-time clearing carbon trading market. These are the main limitations of this research.

This work was supported by the Science and Technology Project of State Grid Corporation of China (NO. 5400-202218162A-1-1-ZN) and the Key Program of National Natural Science Foundation of China (Grant No. 51936003).

### Author contributions

MQ: Conceptualization (equal), data curation (equal), investigation (equal), methodology (equal), software (equal), writing—original draft (equal). YY: Project administration (equal), supervision (equal), writing—review and editing (equal). XZ: Data curation (equal), funding acquisition (equal), software (equal), validation (equal), visualization (equal). QX: Investigation (equal), project administration (lead), writing—review and editing (lead). LY: resources (equal), validation (equal).

### Funding

The Science and Technology Project of State Grid Corporation of China (NO. 5400-202218162A-1-1-ZN). The Key Program of National Natural Science Foundation of China (Grant No. 51936003).

### Availability of data and materials

The datasets used or analysed during the current study are available from the corresponding author on reasonable request.

## Declarations

## Competing interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper" for the section Competing interests.

## Received: 25 February 2023 Accepted: 23 October 2023 Published online: 23 November 2023

## Submit your manuscript to a SpringerOpen ${ }^{\circledR}$ journal and benefit from:

- Convenient online submission
- Rigorous peer review
- Open access: articles freely available online
- High visibility within the field
- Retaining the copyright to your article

Submit your next manuscript at $\rightarrow$ springeropen.com