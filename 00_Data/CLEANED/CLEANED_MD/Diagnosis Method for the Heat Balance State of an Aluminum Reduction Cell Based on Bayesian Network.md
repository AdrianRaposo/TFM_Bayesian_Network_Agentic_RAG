# Chapter 1 <br> Diagnosis Method for the Heat Balance State of an Aluminum Reduction Cell Based on Bayesian Network 

Jiaming Zhu * and Jie Li<br>School of Metallurgy and Environment, Central South University, Changsha 410012, China; lijieyejin@csu.edu.cn<br>* Correspondence: csujiaming_zhu@163.com; Tel.: +86-024-2325-3041

Received: 29 March 2020; Accepted: 5 May 2020; Published: 7 May 2020
check for updates


#### Abstract

The superheat of an electrolyte is an important indicator of the heat balance state of aluminum reduction cells. In industrial practice, it costs too much to accurately measure the superheat in every cell every day. A common alternative is to calculate the superheat based on additive concentrations in the electrolyte, which has problems of high error and long delay. In this paper, a method to diagnose the heat balance state of an aluminum reduction cell based on Bayesian network is presented, a Bayesian network structure and CPT (conditional probability distribution) were built, and the continuous diagnosis process is presented. This diagnosis method takes important symptoms and factors into account, taking advantage of more useful information instead of only calculated superheat. The application examples show that this method is effective in diagnosing the heat balance state for uncertain and incomplete superheat information.


Keywords: aluminum reduction cell; Bayesian network; heat balance state; superheat

## 1. Introduction

Maintaining a proper heat balance state is of great importance for the highly efficient and stable operation of aluminum reduction cells. Technically, it is necessary to evaluate the heat balance state through a comprehensive index of electrolyte superheat and ledge thickness. Literature studies [1-5] show that the superheat and ledge thickness are mutually coupled, which can achieve automatic balance to some extent. When the superheat is too low, the thickness of the ledge thickness increases, which causes the superheat to rise again. When the superheat is too high, the thickness of the ledge decreases, which causes the superheat to decrease again. When the heat balance changes, superheat responds very fast, while the ledge thickness responds much slower. In most cases, representing heat balance state only through the superheat does not cause big errors.

Although many researchers and companies have developed instruments to measure superheat, they are not yet widely used in practical production due to the high price and complex operation requirements. Technicians in most aluminum smelters make indirect estimates of superheat by applying the following methods: sampling electrolyte and making the electrolyte composition analysis in the laboratory, then calculating the liquidus temperature according to the empirical formula, and then subtracting the liquidus temperature from the electrolyte temperature to obtain the superheat. This method is not good in time-effectiveness, and has large errors in analyzing electrolyte composition. In order to compensate, the technician also judges the heat balance state with the aid of some signs. There are several heat balance states, including low superheat cell, normal cell, and high superheat cell. When the superheat is too low, the cell is regarded as a low superheat cell, presenting decreasing cell temperature, poor alumina dissolution, more precipitation and anode effects, amongst others. When the superheat is too high, the cell is regarded as a high superheat cell, presenting increasing temperature, sidewall redness, decreasing current efficiency, among other effects.

The development of the machine learning model in recent years has led many scholars to apply it to the prediction of the superheat, electrolyte temperature, and control system in aluminum reduction cells. Guo [6] proposed a time granularity-based superheat prediction model, with feature sets and training sets built on different time series. Based on the Restreken formula, Cao [7] proposed making corrections to the composition by using recent historical measurements in compliance with the relevant law of volatile composition consumption, and improved the empirical prediction formula of the liquidus temperature, which can be used to estimate the superheat in the non-sampling period. Long [8], Ding [9], Li [10], and Boadu [11], amongst others, improved the alumina feeding control system by using the BP neural network or fuzzy neural network. Frost and Karri [12,13] studied the method to predict and control the electrolyte temperature through BP neural network. In Zheng's research [14,15], neural network was applied in aluminum fluoride addition and cell status diagnosis. Li [16,17], and Li [18], amongst others, combined wavelet theory with neural network to establish a reduction cell state prediction model.

Although artificial neural network has received much attention from many researchers, there are many limits of application in predicting heat balance state due to the high technicality and complexity of artificial neural network. Compared with artificial neural network, another machine learning model, the Bayesian network, has been used very successfully in many industries and fields, particularly in the medical industry. Bayesian network is a probability network model based on the causality among variables, which has unique advantages in describing the complex causality between cause and signs. The technique mentioned above uses the various signs to judge low or high superheat cells by experience, whose basic idea is consistent with the principle of the Bayesian network. This paper analyzes the causality between the related variables of the heat balance state, on the basis of which the Bayesian network is established, calculating the conditional probability distribution from the manual measurement and online measurement data, thus proposing the specific continuous diagnosis procedures.

# 2. Bayesian Network 

Bayesian network is a type of probabilistic graphical model based on Bayesian theorem, which is a directed acyclic graph containing nodes and directed edges. The directed edge represents the causality or association among nodes. The association strength is determined by the conditional probability table. Generally speaking, Bayesian theorem is that you can predict the probability of an event relying on the probability of other events related to the nature of the event when you can't determine the probability of an event occurrence. As mathematicians say, the more events supporting an attribute occur, the greater the likelihood that it will occur [19].

### 2.1. Selection of Network Node

There are many variables during aluminum reduction. It is necessary to select variables with obvious causality with heat balance state as nodes of Bayesian network. Through state discretization of 500 kA cell production data in a Chinese smelter according to the actual situation and variable characteristics, the specific nodes and state discretization are listed in Table 1.

Table 1. Selected nodes and state discretization (State with * is default choice).


(1) "Heat_state"

This node indicates the heat balance state of the cell based on its superheat value.
(2) "Often_AE"

When the superheat decreases, alumina is not easily dissolved and more anode effects will occur, which can be acquired in the cell control system in real time.
(3) "Block"

When superheat decreases, undissolved alumina will accumulate near the feeding hole and cause blockage. If the blocked hole is not cleaned, the block is only counted once. After cleanup, if the block occurs on this hole again, another block event can be counted. An intelligent breaking and feeding system was applied to monitor the block state of each feeding hole, the method of which is in [20].
(4) "Bath_level"

This node represents the height of the bath level.
(5) "Metal_level"

This node represents the height of the metal level.
(6) "Superheat"
"Superheat" is calculated based on electrolyte temperature and liquidus temperature. The empirical formula for liquidus temperature calculation is given in the literature [21].
(7) "Heat_long"

Firstly, the current efficiency for a longer period of time (the latest week in general) is approximately current efficiency $\eta$ according to tapping amount, so electrochemical reaction consumption and energy for heating materials [22] is $W_{R}=(0.48+1.644 \times C E / 100) \times I(\mathrm{~kW})$.

The energy input is equal to voltage times current: $W_{i n}=U \times I(\mathrm{~kW})$.
In the above two formulas, $U$ refers to cell voltage and $I$ refers to potline current, both of which can be acquired from the cell control system in real time.

In accordance with the law of energy balance, the heat loss from a cell surface equals $W_{i n}-W_{R}$, which is also the heat for maintaining cell temperature and electrolyte superheat. This heat value is estimated based on average current efficiency for a longer period of time, so it is called "Heat_long". For easy understanding, voltage is used to express "Heat_long", i.e., $U-(0.48+1.644 \times C E / 100)$.
(8) "MHD" (Magnetohydrodynamic)

The MHD fluctuation index can be acquired from anode current monitoring system. The higher the index, the more fluctuations occur between the molten metal and electrolyte interface.
(9) "CVD"

Both cathode block quality and proper heating-up process can influence cathode voltage drop (CVD), but those influence are long and stable. The value of "CVD" must be determined based on the actual conditions of each cell. After verifying that there is no hard precipitation on the cathode and that the heat balance state remains normal, $\operatorname{CVD}(V 0)$ is measured as baseline.
(10) "Spike"

All anode currents were measured by an online anode current measuring system [23,24]. Anode current can obviously reflect the anode spike. As for the anodes with higher current and lower noise, the anode spike can be inspected on the monitor by operators.
(11) "Temp_change"

This variable represents the variation trend of bath temperature.
The temperature measurement precision of thermocouple is $0.1^{\circ} \mathrm{C}$. The three latest values of electrolyte temperatures (in chronological order T2, T1, and T0; T0 represents the temperature measured that day) are used to conduct trend analysis.
(12) "Heat_xstate"

The variable is not an observed variable but a known variable, which is a historical value of previous "Heat_state". It is based on the manual measurement of superheat. Its classification is consistent with "Heat_state".
(13) "Wall_temp"

This node refers to the temperature of the side wall surface.
(14) "Sludge"

The sludge on the cathode surface can be judged by operators.
(15) "Heat_present"
"Heat_present" is jointly determined by "Spike" and "Heat_long". "Heat_present" refers to the current heat loss considering anode spikes, which is the correction of "Heat long", so its state classification is consistent with "Heat long".

# 2.2. Analysis of Causality among Nodes 

### 2.2.1. Variables Influencing "Heat_State"

The "Heat_state" of an aluminum reduction cell is determined by two key factors: the heat loss (i.e., "Heat_present") and thermal insulation performance. When the thermal insulation performance remains unchanged, the higher the "Heat present" is, the hotter the cell could be. When "Heat_present" remains unchanged, the better the thermal insulation is, the hotter the cell could be.

Thermal insulation is mainly influenced by the type and thickness of insulation material in the lining of the aluminum reduction cell, the thickness of the cover material on the upper part of the cell, the ventilation conditions of the external surface of the cell, the "Metal_level", the ledge thickness,

and other factors. The type and thickness of the insulation material are usually determined during the engineering stage and cannot be changed during cell operation. It is necessary to take a very long time to effectively adjust the cover material thickness of upper part of the cell. The ventilation conditions on the external surface of the cell also change very slowly unless forced ventilation is used in the event of an emergency. "Metal_level" is an important means to influence and regulate the heat balance in the normal operation of cells. Although it is not recommended that heat balance is adjusted by "Metal_level" too often, "Metal_level" is one of the available important means for smelters when there are heat balance problems. The ledge thickness is the result of the heat balance state, which is variable along with the changing of the heat balance state.

Therefore, "Heat_present" and "Metal_level" are those variables influencing "Heat_state" of aluminum reduction cells.

# 2.2.2. Variables Affected by "Heat_State" 

(1) "Often AE"

As mentioned above, some alumina cannot be dissolved when the superheat is low, and it can easily lead to the occurrence of anode effects.

In addition, the variable "Bath level" influences "Often_AE". When the "Bath_level" is low, i.e., insufficient electrolyte to dissolve the amount of alumina, this results in more anode effects.

As the electrolyte ratio (concentration ratio of $\mathrm{NaF} / \mathrm{AlF}_{3}$ ) decreases, the saturated solubility of alumina decreases, and the alumina dissolution rate decreases as well. The current alumina concentration can generally be controlled below $3 \%$, and the appropriately low electrolyte ratio will not cause an anode effect [25]. In addition, many aluminum smelters target achieving a low electrolyte ratio. The anode effect will occur frequently (i.e., $1 \mathrm{AE} /$ pot$\cdot$day) only when the electrolyte ratio is very low. In this paper, it is assumed that the electrolyte ratio can be controlled within a reasonable range.
(2) "Superheat"

Although "Superheat" has an error in calculation, unable to exactly substitute the actual superheat, it has a certain relation with the actual superheat.
(3) "Wall_temp"

When the cell maintains high superheat, "Wall temp" will become very high.
(4) "Block"

When the cell maintains low superheat, alumina is not easily dissolved and the feeding hole is easily blocked.
(5) "Sludge"

When the cell retains low superheat for a long time, the alumina easily precipitates on the cathode surface and hard precipitation forms and, therefore, "Sludge" becomes worse.
(6) "Temp_change"
"Heat_xstate" and "Heat state" have joint influence on "Temp_change". If the cell changes from low to high superheat, "Temp_change" presents an upward trend (i.e., state of "increase"); if the cell changes from high to low superheat, "Temp_change" presents a downward trend (i.e., state of "decrease").

In addition, "Heat_state" can also influence "Bath level", but such influence is ignored since the operators often tap or add electrolyte, giving rise to great disturbance on the "Bath level".

### 2.2.3. Influencing of Other Variables

(1) Influence of "Sludge" on "CVD"

As "Sludge" worsens, hard precipitation increases, and area of current passing the cathode surface decreases, so the "CVD" becomes higher.
(2) Influence of "Metal_level" and "Sludge" on "MHD"

As "Metal_level" becomes lower or there is much hard precipitation on the cathode, the horizontal current in the molten metal becomes higher, which makes "MHD" more likely to be worse.

(3) Influence of "Spike" and "Heat_long" on "Heat_present"

When "Spike" occurs, a current passes through the conducting spike under the anode, which causes molten metal short circuit and no electrochemical reaction happens, so the energy consumed decreases and the corresponding "Heat present" becomes higher.

# 2.3. Configuration of Bayesian Network 

### 2.3.1. Structure of Bayesian Network

Based on the above analysis of causality among different nodes, the Bayesian network can be configured as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Bayesian network for diagnosis of "Heat_state".
"Heat_present" and "Metal_level" are the parent nodes of "Heat_state". Other factors, such as lining structure, ventilation, and anode cover thickness, are not incorporated into the Bayesian network, since these factors are more stable and are seldom used to adjust the heat balance of the cell.

The child nodes of "Heat_state" are "Temp_change", "Often_AE", "Superheat", "Wall_temp", "Block", and "Sludge", which give signs that are easily seen when the cell becomes low or high superheat.

### 2.3.2. Conditional Probability Tables

After finalizing Bayesian network structure, it is necessary to establish a conditional probability table based on known data. The data is from production reports and actual measurements (including online and manual measurements) of 500 kA cell during a three-month period in a potroom.

As mentioned above, if the equipment is used to measure the superheat of each cell on site every day, it a lot of time and costs will be spent. Setting superheat as the target variable in this model can realize timely understanding of the superheat variation at lower cost without requiring frequent daily measurement of superheat. However, if there are no measured superheat data at all, the parameter learning in the model cannot be carried out, so a small amount of superheat measurement data is required to complete the parameter learning.

By means of the automatic calculation function of GeNIe 2.3 Academic software (BayesFusion, LLC, Pittsburgh, PA, USA), the conditional probability table for each node is calculated after the original data are input. Table 2 shows a list of probability distributions of "Heat_present" and "Metal_level" to "Heat_state" conditions. The conditional probability tables of other nodes are not shown here due to space limitations.

Table 2. Conditional probability distribution of "Heat_present" and "Metal_level" to "Heat_state".


# 3. Diagnosis and Analysis of Heat Balance 

Bayesian network takes evidence as input variables. Evidence refers to the state value of a known variable which shall be input to the model to solve the probability distribution of other variables. It is unnecessary to treat all measurement variables as known conditions every time; instead, any part of them may be used.

### 3.1. Inference and Calculation Method of Bayesian Network

As for networks with $n$ nodes such as $x_{1}, x_{2}, \ldots, x_{n}$, the joint probability distribution of Bayesian network is

$$
P\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \operatorname{parents}\left(x_{i}\right)\right)
$$

The conditional probability of a node is related to the parent node, and ignores the nodes without a connection.

Setting $A_{1}, A_{2}, \ldots, A_{n}$ as a complete group of incompatible events for $E$, and $P\left(A_{i}\right)>0, B$ represents any event of $E$, according to the Bayesian formula:

$$
P\left(A_{i} \mid B\right)=\frac{P(A) P\left(B \mid A_{i}\right)}{\sum_{j=1}^{n} P\left(A_{j}\right) P\left(B \mid A_{j}\right)}
$$

The probability distribution of other variables can be calculated based on the selected evidence variables as known conditions in accordance with Equations (1) and (2). Some mature commercial software or toolkits can be applied to the inference and calculation of Bayesian network. The author wrote code and conducted automatic data input and calculation based on Bayesian network Toolbox (BNT) of MATLAB 7.12.0.635 software (The MathWorks, Inc., Natick, MA, USA).

### 3.2. Single Diagnosis

Except for those variables not frequently measured (such as "Wall_temp" and "Sludge"), there are ten variables commonly used as evidence, which can constitute more than twenty thousand combinations, so it is impossible to list them all. Table 3 lists the diagnosis results of some typical evidence combinations.

Table 3. "Heat_state" results under some evidence combinations.


Notes: Blank means not used as evidence. The states of other nodes are default.

# 3.3. Continuous Diagnosis 

The "Superheat" is calculated based on the electrolyte composition, assuming the measurement frequency of the electrolyte composition is once every 7 days. The longer the time from the electrolyte sampling time, the greater the difference between the analytical value and the real measured value. The specific requirements of the model for the "Superheat": If electrolyte is sampled on Day 1, the analysis results will be obtained on Day 2, which will work as evidence of the model operation on Day 2. At the same time, the probability of "Superheat" and "Heat_state" of the model are updated on Day 1, and "Superheat" is no longer used as evidence after Day 3, until the loop to the next electrolyte composition measurement date.
(1) Conditions of Continuous Diagnosis

Assuming the states of "Heat_present" and "Metal_level" are known and remain the same all the time, the continuous calculation method can be used: regarding the conditional probability of the "Heat_state" under known "Heat_present" and "Metal_level" as prior probability; regarding the probability result of "Heat_state" after calculation as posterior probability, which can be an update of the prior probability of the "Heat_state" for the next calculation.
(2) Application Cases of Continuous Diagnosis

There are three continuous calculation cases (Cases A-C) as shown in Tables 3-5. The specific calculation process is as follows: make electrolyte sample on Day 1, conduct analysis of the electrolyte composition on Day 2. On Day 2, calculate the "Heat_state" on Day 1 and Day 2 at the same time (using the same composition). From Day 3, the actual composition has a big difference with the value at the time of sampling, so the "Superheat" is not set as evidence. On Day N $(\mathrm{N} \geq 3)$, the "Heat_state" result of Day $\mathrm{N}-2$ is assigned to the current "Heat_xstate" as a prior probability, and the "Heat_state" result of Day $\mathrm{N}-1$ is assigned to the current "Heat_state" as a prior probability (provided that the "Heat_state" and "Metal_level" remain unchanged; if there is a change, use the original condition probability), calculate the "Heat_state" result of Day N, and until the loop to the next composition results.

In Case A, from Day 4, evidence of "Bath_temp" presents an upward trend. On Day 4, the probability of "High" in "Heat_state" increases from $0.8 \%$ on the previous day to $11.5 \%$, and reaches up to $68.3 \%$ and $97.2 \%$ on Day 5 and Day 6 , respectively.

Table 4. Evidence and results of continuous calculation for Case A.


Notes: Blank means not used as evidence. The states of other nodes are default.

Table 5. Evidence and results of continuous calculation for Case B.


Notes: Blank means not used as evidence. The states of other nodes are default.
Case B can be obtained through modifying the evidence of "Bath_temp" in Case A from upward into downward. In Case B, the probability of "Normal" of "Heat_state" is maintained above $98 \%$ all the time, and the probability of "Low" only slightly increases. The phenomenon of the electrolyte temperature decreases and neither anode effect nor block occur, indicating that the electrolyte superheat can meet the requirements for alumina dissolving and the cell does not become low in superheat.

In Case C, when the electrolyte temperature decreases, and both anode effect and block occur, the probability of "Low" of "Heat_state" will go up from $0.1 \%$ on Day 3 to $97.7 \%$ on Day 6, as shown in Table 6.

Table 6. Evidence and results of continuous calculation for Case C.


Notes: Blank means not used as evidence. The states of other nodes are default.

# 3.4. Application Effect 

The Bayesian network model has been used in testing mode in the 500 kA potroom for 3 months with very good performance. When selecting the appropriate probability threshold, there are hardly any missing alarms and false alarms of low and high superheat cells. In the potroom with 184 pots, 12 pots were diagnosed as low or high superheat pots in the 3-month testing period. The measured

degree of superheat of these pots has verified that all diagnoses are correct. Such application results show that the model can effectively judge the trend of heat balance, which can help the technician concentrate on dealing with the cells with more serious problems, saving labor time and costs.

# 4. Conclusions 

Bayesian network modeling possesses a strict theoretical basis, and its result is a quantitative probability value, which is different from the qualitative analysis by experience. Bayesian network has no strict restrictions on input conditional variables and output result variables and can accept any combination of input variables as evidence with very high flexibility. Therefore, it is quite suitable for diagnosing the heat balance state of aluminum reduction cell with uncertain input variables.

In this paper, a heat balance state diagnosis method based on Bayesian network is proposed. At first, the causality analysis of the variables associated with the heat balance was conducted. Then, the GeNIe software was used to process measurement data and statistical report data to obtain the conditional probability table. Consequently, the automatic inference and calculation program of Bayesian network was conducted with the aid of MATLAB software. Since the inference results are consistent with actual state, and are quite convincing, the Bayesian network model is thus demonstrated to have obvious advantages over the superheat measuring instrument with high cost and complicated structure.

Author Contributions: J.Z. has done study design and data analysis, developed the model and written the manuscript. J.L. has provided valuable guidance. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
