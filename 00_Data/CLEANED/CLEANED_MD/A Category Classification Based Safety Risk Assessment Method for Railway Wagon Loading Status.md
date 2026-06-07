# A Category Classification Based Safety Risk Assessment Method for Railway Wagon Loading Status 

Fei YE, Qigang LIU, Jing JIN*, Tiegang ZHANG, Wenqiao SUN, Yue GE


#### Abstract

The identification and control of safety risks in the loading state of goods wagon is one of the important tasks to ensure the safety of goods in transit. In view of the problem that the current risk assessment of transportation schemes is mainly based on manual experience and cannot be quantified, which makes it difficult to accurately determine the safety risk of transportation on the way, a risk assessment method for loading status of goods wagon based on scenario classification was proposed. Firstly, based on a detailed analysis of the safety risk points in various stages of railway freight operations, a SHEL influencing factor model based on scenario classification was constructed. Then, considering the characteristics of railway freight transportation, a fuzzy accident tree model (FTA) of goods wagon loading state risk was constructed, and the fault tree was transformed into a Bayesian network structure according to the mapping algorithm of fuzzy fault tree and Bayesian. Furthermore, a triangular fuzzy membership function was introduced to describe the fault probability of nodes, and a BN based fuzzy fault tree inference algorithm was proposed. Finally, taking a railway station and route transporting coil steel goods in China as an example, this paper explained how to integrate expert knowledge through fault tree and Bayesian network to support railway freight scheme designers in conducting risk quantification assessment of freight wagon loading status


Keywords: check of railway wagon loading status; fuzzy fault tree-BN model; railway freight transport; safety risk evaluation; SHEL; traffic safety

## 1 INTRODUCTION

The safety of railway wagon loading status is the key of railway freight safety management, which consists of three parts: railway cargo safety, railway wagon safety, and cargo loading safety. Ensuring the loading status of railway wagons not only ensures the safety of railway freight transportation, but also paves an important foundation for ensuring the safety of railway traffic and passenger transport. For a long time, railway enterprises have focused on strengthening the risk identification ability of railway wagon loading status by means of metrological safety, video monitoring, and etc., and have made clear management rules and regulations such as Management Rules for Railway Freight Inspection, Rules for Railway Cargo Loading and Reinforcement, and Management Rules for Wagon Tarpaulins. The main contents are:
(1) Management Rules for Railway Freight Inspection specify the scope of cargo inspection operations, including: the loading and reinforcement status of goods in freight trains, wagon tarpaulin and tarpaulin rope net covering and binding status, sealing (except for sealing at the end doors of tank cars, containers, SQ or JSQ vehicles), the closing conditions of the doors, windows, covers, and valves of wagons, as well as the closing conditions of the covers and valves of tank containers, and other matters stipulated by China State Railway Group Co., Ltd.
(2) Railway Cargo Loading and Reinforcement Rules are important single technical regulations to strengthen the loading and reinforcement of railway cargo and ensure the safety of railway transportation by fully-loaded wagons. This regulation indicated many requirements for loading and reinforcement, here are examples for illustration. If the following errors are found, train should be stopped immediately for treatment: firstly, the coil is horizontally loaded and rolling occurs; secondly, the moving parts of the goods rotate and open, which may scratch the operation equipment or affect the locomotives and vehicles on the adjacent lines.
(3) Management Rules for Wagon Tarpaulins is a single technical regulation that standardizes the
management of wagon tarpaulins, improves utilization efficiency, and ensures railway transportation and cargo safety. This regulation clarifies the requirement for the loading quality of tarpaulin before and after covering. Quality inspection before covering consists of the integrity of the cloth body, no damage, intact eye rims, complete and clear marks and numbers, complete ropes, no joints, firm insertion, and correct connection to the tarpaulin. Quality inspection after covering should make sure: firstly, the tarpaulin is flat, the goods are not exposed, the corners at both ends are tightly pasted, and the lines on both sides are smooth. Each part shall not exceed the limit. Secondly, the position of the rope hitch and binding is correct, the knot is firm, and there is no looseness or falling off. The rope tied to the rope bolt is in a butterfly shaped knot, with a length of $100-300 \mathrm{~mm}$ at the end and tail.
(4) Railway Container Transport Rules is a single technical regulation to standardize the management of container transport, ensure the safety of railway transport, and accelerate the development of container transport. There are clear requirements for the loading status of railway containers, including: firstly, before loading containers, the vehicle floor must be cleaned to ensure that there are no debris on the container and vehicle body. Secondly, when transporting empty containers on special flat cars or shared flat cars that are not equipped with F-TR locks, they must be securely bound with 4 or more strands of 8\# galvanized iron wire. Thirdly, containers should be shipped through special flat cars or shared flat cars for containers, and it is prohibited to use ordinary flat cars for shipping.

Railway rules and regulations stipulated risk types and disposal measures; however, the determination of the safety risk level of railway wagon loading conditions mainly depends on the operational experience and subjective understanding of on-site operators, and there is a lack of reliable and quantitative risk assessment methods for railway wagon loading conditions. The risk assessment of railway freight safety has always been a hot topic in academic research. The main focus of the in-depth discussion was on the factors affecting the safety risks of

railway freight transportation. Based on lierature review, scholars [1, 2] analyse the causes of accidents on railway lines with statistical data, and determine the probability of occurrence of a given cause, and use the risk matrix [3], risk control process [4] to assess and control railway freight risk. However, owing to many catogories of railway transport goods, complex loading and unloading processes, and diverse transport environments and scenarios, the expert assessment results might be greatly disturbed in accessing the risk of goods wagon loading status without considering the operation scenario, resulting in insufficient reliability, pertinence, and operability of the risk assessment.

The main contributions can be summarized as follows: 1) Considering significant differences in risk importance between different management or operational categories, a SHEL influencing factor model based on category classification was constructed (Section 3.1). 2) Considering the fuzziness of the risks of railway freight car loading state, a fuzzy accident tree model (FTA) of railway freight car loading state risk is constructed (Section 3.2.13.2.2). 3) A triangular fuzzy membership function is introduced to describe the fault probability of nodes, and a fuzzy fault tree inference algorithm based on BN is proposed (Section 3.2.3-3.2.4). 4) Taking a railway station and line transporting coil steel goods in China as an example, this paper explains how to integrate expert knowledge through fault tree and Bayesian network (Section 4).

## 2 LITERATURE REVIEW

The problem of risk assessment in railway transport is presented next to risk analysis and risk evaluation as one of the stages of risk management in the whole railway system. Research studies largely focused on risk assessment of rail freight transport system, risk assessment of a certain operation, risk assessment of rail freight facilities [5].

In terms of risk assessment of rail freight transport system, some researchers take the railway freight system as the object based on statistical data, mostly focus on rail transport of hazardous material [9-12]. Turla Tejashree et al. [6] proposed two alternative risk measures, namely the expected consequence and conditional value at risk were used to evaluate the freight train collision risk on main tracks, accounting for both the average and worst-case scenarios. Jiang Hui et al. [7] proposed railway freight transportation measurement safety monitoring system, to collect and manage the data from detection sites, and integrate the data with the consistent information of railway transportation management information system to achieve the real-time monitoring of freight loading and alarm management. Fourie Cornelius Jacobus et al. [8] presented a model of railway accident occurrence and the use of fault tree analysis method. A breakdown of studies of reliability and safety of the railway transport system in four areas is presented. Zelenko Yuliia et al. [9] presented the interrelation of the functional strategy of ensuring the reliability of the transportation process with other strategies, proposed a new functional strategy and a schematic diagram of the environmental management system for making management decisions to optimize environmental management in railway transport. Kang Di
et al. [10] proposed five illustrative scenarios used to analyze the best or worst cases and compare the transportation risk differences between service options using unit trains and manifest trains.

In terms of risk assessment of a certain operation, researchers mostly focus on the loading and reinforcement technology for different types of goods and wagons. Liu Jinchao [13] established a simulation model for the frictional resistance performance of the railway flat car floor by using dynamic simulation software. Compared with the impact test of vertical loading of steel coils on wooden floors conducted at the Baotou field test line, the simulation data were compared with field test data to verify the reliability of the simulation model. Qian Runhua et al. [14] in addition, many scholars have studied and discussed the safety of loading special cargo on flat car [15-17]. Lei Dingyou et al. [18] comprehensively considered the constraints such as load balancing, loading location and placement methods, and took light and heavy mixed goods as objects to build a balanced loading model and designed algorithms to solve it. Zhang Yinggui et al. [19] established an optimization model for the balanced loading layout of railway container mixed goods with the optimization goal of maximizing the comprehensive utilization rate of containers, proposed a cargo block unit construction method based on the classification method of mixed goods and the judgment index of the structure of goods to be loaded, and designed a set of cargo block unit selection and placement methods and remaining space update rules. An optimization algorithm for balanced loading layout of railway container mixed goods is proposed. Lang Maoxiang et al. [20] develop a multi-objective optimization model that focuses on a number of practical requirements including the center-of-gravity height of a loaded car and load balance considerations. Jiang Jianzheng et al. [21] established a dynamic model for a certain type of high-speed freight EMU based on multibody dynamics theory using the safety indicators of wheel load reduction rate and derailment coefficient as evaluation criteria, and used the model to study the impact of cargo centroid deviation on driving safety. In terms of inspection of wagon loading status, Du Lunping et al. [22] proposed a method of gauge-exceeding detection of freight train based on monocular visual 3D reconstruction, to meet the requirements of railway freight train gauge-exceeding detection.

In terms of risk assessment of rail freight facilities, some researches concern research related to risk assessment with multiple facilities and their interrelationships. Grenčík Juraj et al. [23] presented methods of risks assessment and possibilities of their reduction in design, operation and maintenance of railway vehicles. Baranovskyi, D. et al. [24] obtained the dependences of the probability of failure-free operation of freight wagons on the operating life, proposed the centers of gravity of the areas that are used to characterize and assess the risk. Under this classification, scholars mainly optimize the application management and process design of rail freight facilities through the research of security risk identification and control [25-27].

It can be seen that there is currently less research on risk assessment of railway wagon loading conditions. The risk assessment of the loading status of railway wagons is

an important task in railway freight scheme design. To meet the needs of providing technical support for railway freight scheme design, it is necessary to develop scientific potential risk assessment techniques for the loading status of railway freight trains, predict the degree of safety risks existing in the loading status of freight trains in advance, improve the efficiency of freight operation organization, and reduce labor intensity.

## 3 RESEARCH METHODOLOGY

### 3.1 SHEL Factor Model Based on Category Classification

The SHEL model was proposed by Professor Elwyn Edwards in 1972. In this model, personnel are at the core, and the interrelationships among other personnel (L-Liveware), hardware (H-Hardware), software (S-Software), and environment (E-Environment) constitute the four interfaces of the model, namely, L-L, L-S, L-H, and L-E [28]. According to the SHEL model theory, the main reason for errors is the insufficient coordination between personnel at the central location and other interfaces. To reduce errors, corresponding measures must be taken to increase the matching degree between personnel and the four interfaces. Traditional SHEL factory models do not distinguish between management or operational scenarios, but are classified according to personnel, hardware, software, and environmental factors, and are directly used for risk assessment. In actual management activities, there are significant differences in the risk importance of different management or operation scenarios, resulting in differences in the weight of risk factors under different scenarios, leading to a significant gap between the risk assessment results and actual risks. Based on this, a SHEL factor model based on railway freight operation scenario classification is proposed.

### 3.1.1 Railway Freight Operation Scenario

The railway freight operation process includes many links and involves many factors, and the influencing factors involved in different links vary. If the condition verification process is handled, only personnel risks and software risks are involved. The weight inspection process involves personnel risks, software risks, environmental risks, and equipment risks. Safety incidents and accidents related to the loading status of railway wagons mainly occur at freight yards and dedicated lines handling loading operations, as well as at railway freight inspection stations. Therefore, it is necessary to focus on analyzing the main business processes of freight operations from handling conditions verification to vehicle pickup and delivery operations at the arrival end without centering on the aspects that do not affect the safety of the loading status of railway freight vehicles, such as ticket preparation, charging, price insurance, claim settlement, and arrival loading and unloading.

This paper analyses the main processes of railway freight operations based on the handling of industrial sidings and freight stations.

The goods handled at the railway freight station shall go through the main operation steps of condition verification, weight inspection, pre-loading inspection, loading operation, post loading inspection, vehicle pickup and delivery operation (delivery), freight inspection, vehicle pickup and delivery operation (arrival), etc. Verification of processing conditions refers to the verification and confirmation of conditions such as the identity of the shipper, delivery requirements, and processing conditions of the station. Weight inspection refers to the inspection and confirmation of the type, weight, and number of pieces of goods, mainly including safety inspection of mixed loading goods, cargo inventory, and weight inspection of goods. Pre-loading inspection and post loading inspection refer to the status inspection of wagons, goods, and loading and unloading equipment before and after loading. The pickup and delivery operation (sending) and the pickup and delivery operation (arrival) are the confirmation and verification of the train formation. Freight inspection refers to the use of technical means such as metrological safety equipment, video monitoring equipment, etc. to inspect and confirm the loading of goods, wagon bodies, and the status of goods during transportation [29].

![img-0.jpeg](img-0.jpeg)

Figure 1 Main processes of railway freight operations that affect the loading status of railway wagons

The goods handled on the industrial siding shall go through the operations such as handling condition verification, wagon handover (empty wagon), loading operation on the industrial siding, wagon handover (loaded wagon), wagon pickup and delivery operation (dispatch), freight inspection, wagon pickup and delivery operation (arrival), etc. Among them, wagon handover (empty wagon) and wagon handover (loaded wagon) refer to the inspection and confirmation of wagon condition, cargo condition, and cargo loading status.

### 3.1.2 Improved SHEL Factor Model

Due to factors such as the type of goods, type of wagons, and loading and reinforcement technology, there are significant differences in the level of safety risks associated with railway freight transportation in different operational stages. It is difficult to accurately diagnose and locate high-risk links and scenarios not conducive to risk

control or risk transfer after risk assessment without distinguishing between scenarios and links. Therefore, it is necessary to systematically analyze the key risk points of each link using the SHEL model based on the systematic sorting of railway freight operation processes, in order to accurately locate and prevent risks.

The traditional SHEL factor analysis model does not distinguish scenarios, making it difficult to accurately locate risk sources, resulting in differences between risk assessment and actual risks. From the main links of railway freight operations, it can be seen that the risk items in each link have a direct impact on the loading status of freight trains, starting from the cargo acceptance link, while the impact of management rules and regulations on operational safety risks will be directly reflected in the standardization and standardization of operations. According to the basic factor model framework of L-L, L-S, L-H, and L-E, combined with the main links of railway freight operations that affect the loading status of railway wagons, a SHEL factor model based on scenario classification is formed. Taking L-H as an example, railway freight facilities and equipment include weighing and inspection equipment, loading and unloading equipment, storage facilities, measurement safety detection equipment, and video monitoring equipment. According to the requirements of railway rules and regulations and experts' expertise, they include the loss or failure of weighing equipment in the weighing and inspection process, the failure of loading and unloading equipment or storage facilities in the loading operation process, the loss or failure of measurement safety equipment in the freight inspection process, missing or malfunctioning of metering safety equipment during wagon handover, missing or malfunctioning of video monitoring equipment, as shown in Fig. 2.

![img-1.jpeg](img-1.jpeg)

**Figure 2** The basic factor model framework of L-H

Based on the above method, the main risk item components of L-L, L-S, and L-E are processed, and the results are shown as follows:

In terms of L-L, risk items mainly arise from the professional quality and work status of personnel, mainly represented as unintentional behavior and intentional behavior [30]. In the category of railway freight operations, unintentional behavior is manifested as operational errors or inadequate operations in freight operations, and intentional behavior is manifested as illegal operations. Therefore, the main risk of L-L includes information verification errors, inadequate inspection, illegal loading and unloading, illegal acceleration and deceleration, and other risk points in the process of handling condition verification, wagon handover, dedicated line loading operations, weight inspection, preloading inspection, loading operations, post loading inspection, and freight inspection [31, 32]. Major risk items include: verification of processing conditions - error in processing conditions verification by acceptance personnel (*X*<sub>1</sub>), verification of processing conditions - the acceptance personnel makes an error in verifying the type or quantity of goods (*X*<sub>2</sub>), wagon handover - the status inspection of the wagon body by the freight forwarder is insufficient (*X*<sub>3</sub>), wagon handover - the freight forwarder fails to inspect the goods loaded on the wagon (*X*<sub>4</sub>), wagon handover - the inspection on the loading and reinforcement status of the wagon by the freight forwarder is not in place (*X*<sub>5</sub>), industrial siding loading operation - errors in cargo inventory made by loading and unloading personnel (*X*<sub>6</sub>), loading operations on industrial sidings - uneven loading by loading and unloading personnel or loading not in accordance with the loading reinforcement plan (*X*<sub>7</sub>), industrial siding loading operation - poor closing of doors and windows for loading and unloading personnel (*X*<sub>8</sub>), weight inspection - inventory error made by freight forwarder (*X*<sub>9</sub>), weight inspection - the safety inspection by the freight forwarder is not in place (*X*<sub>10</sub>), weight inspection - the reading of weight inspection made by freight forwarder is incorrect (*X*<sub>11</sub>), inspection before loading - the freight forwarder does not thoroughly check the status of the wagon body (*X*<sub>12</sub>), inspection before loading - the freight forwarder does not properly inspect the goods loaded on the wagon (*X*<sub>13</sub>), inspection before loading - the loading and reinforcement status of the wagon is not thoroughly checked by the freight forwarder (*X*<sub>14</sub>), loading operations - inventory errors made by loading and unloading personnel (*X*<sub>15</sub>), loading operations - uneven loading by loading and unloading personnel or failure to follow the loading reinforcement plan (*X*<sub>16</sub>), loading operation - doors and windows of loading and unloading personnel are closed or poorly sealed (*X*<sub>17</sub>), inspection after loading - the freight forwarder does not thoroughly check the status of the wagon body (*X*<sub>18</sub>), inspection after loading - the freight forwarder does not properly inspect the goods loaded on the wagon (*X*<sub>19</sub>), inspection after loading - the loading and reinforcement status of the wagon is not thoroughly checked by the freight forwarder (*X*<sub>20</sub>), pickup and delivery operations - illegal acceleration, deceleration, or sliding of operators (*X*<sub>21</sub>), freight inspection - the freight forwarder does not thoroughly check the status of the wagon body (*X*<sub>22</sub>), freight inspection - the freight forwarder does not properly inspect the goods loaded on the wagon (*X*<sub>23</sub>), freight inspection - the loading and reinforcement status of the wagon is not thoroughly checked by the freight forwarder (*X*<sub>24</sub>), freight inspection - the cargo inspector reads the measurement and detection data incorrectly (*X*<sub>25</sub>).

In terms of L-S, risks mainly refer to information inaccuracy caused by poor software status, including the risk of information inaccuracy caused by processing conditions verification, wagon handover, dedicated line loading operations, weight inspection, preloading inspection, loading operations, post loading inspection, vehicle pickup and delivery operations, and cargo inspection operations. Major risk items include:

verification of processing conditions - inaccurate information on processing conditions at freight terminals $\left(X_{26}\right)$, wagon handover - incorrect train formation or cargo loading information $\left(X_{27}\right)$, industrial siding loading operation - inaccurate loading information $\left(X_{28}\right)$, weight inspection - inaccurate cargo weight information $\left(X_{29}\right)$, inspection before loading - inaccurate loading status check information $\left(X_{30}\right)$, loading operation - inaccurate loading information $\left(X_{31}\right)$., inspection after loading - inaccurate loading status check information $\left(X_{32}\right)$, pickup and delivery operations - incorrect train formation or cargo loading information $\left(X_{33}\right)$, cargo inspection - inaccurate loading status check information $\left(X_{34}\right)$.

In terms of L-E, risks are generated by the operational environment such as management, norms, and values, as well as the natural environment of the work scenario. In the Category of on-site operation of railway freight transportation, various rules, regulations, standards, etc. are represented in the standardization of the operation process, that is, the risk is the lack of standardization of the operation process in each link. The natural environment risks refer to the safety risks of operations in severe natural weather such as wind, frost, rain, and snow. Major risk items include: verification of processing conditions insufficient standardization of operation procedures $\left(X_{35}\right)$, wagon handover - severe weather $\left(X_{36}\right)$, industrial siding loading operation - insufficient standardization of operation process $\left(X_{37}\right)$, weight inspection - inadequate standardization of the operation process $\left(X_{38}\right)$, inspection before loading- severe weather $\left(X_{39}\right)$, inspection before loading - inadequate standardization of operation processes $\left(X_{40}\right)$, loading operations - severe weather $\left(X_{44}\right)$, loading operations - insufficient standardization of operation process $\left(X_{42}\right)$, inspection after loading - severe weather $\left(X_{43}\right)$, inspection after loading - inadequate standardization of operation processes $\left(X_{44}\right)$, pickup and delivery operations - insufficient standardization of operation process $\left(X_{45}\right)$, cargo inspection operations - severe weather $\left(X_{46}\right)$, goods inspection operations - insufficient standardization of operation process $\left(X_{47}\right)$.

Major risk items of L-H include: weight inspection missing or faulty weight inspection equipment $\left(X_{48}\right)$, loading operations - handling equipment failure $\left(X_{49}\right)$, loading operations - storage facilities failure $\left(X_{50}\right)$, freight inspection - missing or malfunctioning metering safety equipment $\left(X_{51}\right)$, freight inspection - missing or malfunctioning video surveillance equipment $\left(X_{52}\right)$, wagon handover - missing or malfunctioning metering safety equipment $\left(X_{53}\right)$, wagon handover - missing or malfunctioning video surveillance equipment $\left(X_{54}\right)$.

### 3.2 Evaluation Model Based on Fuzzy FTA Bayesian 3.2.1 Bayesian Network Construction Based on Fuzzy Fault Tree

In traditional fault tree analysis (FTA) methods, whether the research object is a device fault or a system fault, there must be some ambiguity in its state. The fault manifestations in the same bottom event element are diverse, and there are similarities between different manifestations, making it difficult to quantitatively analyze with certain values. Fuzzy set theory is suitable for solving problems with complexity, uncertainty and fuzziness [33].

Considering obvious uncertainty in the risk degree of each subject, each link and each Category of rail freight transport, fuzzy number is introduced. Compared with traditional fault trees, fuzzy fault trees can better express fuzziness and the uncertainty of fault logic. Fuzzy fault trees are easy to construct, without updating the data of the models. The fault tree can clearly reflect the logical relationship between risk factors, but the fault tree itself can only be reasoned in top-down order, and the reasoning efficiency is not high [34]. In order to effectively evaluate the risk and accurately simulate the uncertainty of causality in the process of logical reasoning, the fault tree is transformed into Bayesian network. Bayesian network (BN), as an uncertainty risk analysis model, can use Bayesian theorem to achieve real-time update of probability when new information needs to be input. However, when using Bayesian network directly for causal analysis of accidents, it is easy to cause confusion in the causal relationship between various nodes, and modelling is relatively complex. Therefore, studying the transformation method from fuzzy fault tree to BN can effectively solve the shortcomings of fuzzy fault tree and BN.

The process of mapping a fuzzy fault tree to BN mainly includes graphical mapping and numerical mapping. This method utilizes the bidirectional reasoning ability of Bayesian networks to perform reliability analysis on complex systems. It utilizes the top-down logical deduction of a fault tree (FTA). The process of converting a fuzzy fault tree to BN is shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Figure 3 Flow chart of transforming fuzzy fault tree to Bayesian network model
When mapping FTA to BN , the corresponding algorithms are mainly as follows: (1) The top event, intermediate event, and basic event of FTA are mapped to the parent node, intermediate node, and child node in the BN; (2) If there are multiple identical basic events in the FTA, they can only be expressed as one basic event in the BN; (3) The prior probabilities of each basic event in FTA are directly assigned to the root node in BN as a prior probability; (4) The logical relationship of logic gates in FTA is mapped to a deterministic conditional probability table (CPT) in BN. Based on the above algorithm, the fault tree can be transformed into a Bayesian network model.

### 3.2.2 Fuzzy Fault Tree Model (FTA) for Loading State Risk of Railway Wagons

The occurrence of railway freight transportation accidents is essentially a change in the loading status of railway wagons. Therefore, taking the railway freight accident as the top event, the main accident as the intermediate event, and the key risk as the basic event, the FTA model is constructed, further mapped to the BN


model. Based on public data and triangular fuzzy numbers, the probability of child node occurrence can be calculated. Through studying the characteristics of railway freight transportation, it can be found that railway freight transportation accidents include not only scrape accidents, derailment accidents, and overturning accidents, but also combustion and explosion accidents [33, 36]. Among them, scrape accidents during freight transportation include situations where goods scrape equipment, buildings, or adjacent trains along the line during transportation, such as the scratching of the inbound signal caused by the opening of the door of a box car; cargo transportation overturning accident refers to the abnormal loading conditions such as partial loading and partial weight of wagons during cargo transportation, resulting in derailment and overturning of wagons. Combustion and explosion accidents during cargo transportation refer to spontaneous combustion of goods and combustion of wagon bodies due to physical and chemical reactions between different goods, friction between goods and vehicle bodies, and high ambient temperature during cargo transportation. Therefore, based on the publicly available railway freight accident information, this paper uses the analysis results of improved SHEL railway wagon loading status risk impact factor, and establishes a fault tree model, which is shown in Fig. 4. Intermediate events are designed in Tab. 1.

By analysing the causal relationship between system faults and basic failure events, a mapping algorithm is used to transform the fault tree into a Bayesian network, with nodes in the BN corresponding to corresponding times in the fuzzy fault tree one by one. The BN network model can be obtained as shown in Fig. 5.

![img-3.jpeg](img-3.jpeg)

**Figure 4** Risk fuzzy fault tree model of railway wagon loading state

**Table 1** Intermediate events

**Figure 5** Bayesian network model

### 3.2.3 Determination and Calculation of Fuzzy Membership Function

Fuzzy logic is a multi-valued logic in which the true value of a variable is considered fuzzy and can be any real number within the unit interval [0, 1]. It is an effective method for designing decision systems, which can be used to solve the problem of inaccurate and uncertain data [37-39]. Aiming at the problem of excessive dependence on the precise failure probability of the root node in probabilistic analysis of BN network models, fuzzy membership functions are used to convert linguistic estimates into fuzzy numbers for quantitative evaluation. In this paper,

triangular fuzzy numbers are used to describe the failure probability of nodes, and the triangular fuzzy membership function diagram is shown in Fig. 6.
![img-4.jpeg](img-4.jpeg)

Figure 6 Triangular fuzzy membership function
Let the root node and intermediate node in a Bayesian network be $x_{i}(i=1,2, \ldots, n)$, and the leaf node be $T$. When state of the node $x_{i}$ is $x_{i}^{p}=1$, it indicates node failure, while the state $x_{i}^{p}=0$ indicates that the node has no failure. When the state of the leaf node $T$ is $T_{q}=1$, it indicates that the leaf node has no failure, and the state $T_{q}$ $=0$ indicates that the leaf node has no failure. Then the membership function of the fuzzy set $A$ on the $U$ satisfies the following requirements, as shown in Eq. (1); then
$U_{A}\left(x_{i}\right): U \rightarrow[0,1], x \in U$
where $U$ is a domain composed of object factors, and $A$ is a fuzzy set on the domain $U$.

The membership function expression of triangular fuzzy numbers is shown in Eq. (2):
$U_{A}(x)=\left\{\begin{array}{lr}0, & x \leq m_{i}-\alpha_{i} \text { or } x \geq m_{i}+\beta_{i} \\ \frac{x-m_{i}+\alpha}{\alpha_{i}}, & m_{i}-\alpha_{i}<x \leq m_{i} \\ \frac{m_{i}+\beta_{i}-x}{\beta_{i}}, & m_{i} \leq x<m_{i}+\beta_{i}\end{array}\right.$
when the root node fails, the fuzzy subset of the failure probability is as shown in Eq. (3):
$P_{x_{i}}=\left(m_{i}-\alpha_{i}, m_{i}, m_{i}+\beta_{i}\right), 0<\alpha_{i} \leq m_{i} \leq \beta_{i}$
where $\alpha_{i}, \beta_{i}$ are the upper and lower confidence limits of $P_{x_{i}}$. When the value of $\alpha_{i}$ is smaller and the value of $\beta_{i}$ is larger, the probability of the root node becomes more ambiguous. When the value is 0 , the probability of the root node is an accurate probability value; $m_{i}$ is the median of root node probability.

Traditional FTA calculates the failure probability of the top event by logically calculating the failure probability of the bottom event through its Boolean operation. When the failure probability of the bottom event is represented by a subset of fuzzy probabilities, the fuzzy operator uses the logical OR gate and AND gate operators, and the fuzzy operator calculation formula is as follows [40]:

The OR gate fuzzy operator is as shown in Eq. (4).

$$
\begin{aligned}
& P_{o r}=1-\prod_{i=1}^{n}\left(1-P_{x_{i}}\right)=1-\prod_{i=1}^{n}\left(1-\left(m_{i}-\alpha_{i}, m_{i}, m_{i}+\beta_{i}\right)\right) \\
& =\left\{1-\prod_{i=1}^{n}\left[1-\left(m_{i}-\alpha_{i}\right)\right], 1-\prod_{i=1}^{n}\left(1-m_{i}\right), 1-\prod_{i=1}^{n}\left[1-\left(m_{i}+\beta_{i}\right)\right]\right\}
\end{aligned}
$$

The AND gate fuzzy operator is as shown in Eq. (5).

$$
\begin{aligned}
& P_{\text {and }}=\prod_{i=1}^{n} P_{x_{i}}=P_{x_{1}} \cdot P_{x_{2}} \cdot \ldots \cdot P_{x_{n}}=\left(m_{1}-\alpha_{1}, m_{1}, m_{1}+\beta_{1}\right) \\
& \cdot\left(m_{2}-\alpha_{2}, m_{2}, m_{2}+\beta_{2}\right) \cdot\left(m_{n}-\alpha_{n}, m_{n}, m_{n}+\beta_{n}\right) \\
& =\left[\prod_{i=1}^{n}\left(m_{i}-\alpha_{i}\right), \prod_{i=1}^{n} m_{i}, \prod_{i=1}^{n}\left(m_{i}+\beta_{i}\right)\right]
\end{aligned}
$$

### 3.2.4 Fuzzy Fault Tree Reasoning Algorithm Based on BN

(1) Leaf node probabilistic reasoning

BN networks can derive the probability of occurrence of leaf nodes through forward reasoning, and can also derive the probability of occurrence of root nodes through reverse reasoning. According to BN's joint probability distribution algorithm and BN's fault diagnosis algorithm, the occurrence probability of the root node can be directly calculated when the occurrence probability of the leaf node is known. Assuming that the leaf node $T$ intersects the node $x_{i}$ and satisfying $\exists i \in[1, n]$, and then $T \cap x_{i}=\varnothing$, it can be obtained from the total probability formula - Eq. (6):

$$
P(T)=\sum_{i=1}^{n} P\left(x_{i}\right) P\left(T / x_{i}\right)
$$

When the fault state of leaf node $T$ is $T_{p}$, the probability of occurrence is shown in Eq. (7).

$$
\begin{aligned}
& P\left(T=T_{p}\right)=\sum_{x_{1}, x_{2}, \ldots, x_{n}} P\left(x_{1}, x_{2}, \ldots, x_{i}=x_{i}^{p}, \ldots, T=T_{p}\right) \\
& =\sum_{x_{1}, x_{2}, \ldots, x_{n}} P\left(T=T_{p} / x_{1}, \ldots, x_{i}=x_{i}^{p}, \ldots, x_{n}\right) P\left(x_{1}\right) \ldots P\left(x_{n}\right)
\end{aligned}
$$

In addition, it is known that the root node state is $x_{i}^{p}$, and according to the BN principle, the conditional probability of the leaf node $T$ state being $T_{p}$ is shown in Eq. (8).

$$
\begin{aligned}
& P\left(T=T_{p} / x_{i}=x_{i}^{p}\right)=\frac{P\left(x_{i}=x_{i}^{p}, T=T_{p}\right)}{P\left(x_{i}=x_{i}^{p}\right)} \\
& =\frac{\sum_{x_{1}, x_{2}, \ldots, x_{n}} P\left(x_{1}, \ldots, x_{i}=x_{i}^{p}, \ldots, x_{n}, T=T_{p}\right)}{P\left(x_{i}=x_{i}^{p}\right)} \\
& =\frac{\sum_{x_{1}, x_{2}, \ldots, x_{n}} P\left(T=T_{p} / x_{1}, \ldots, x_{i}=x_{i}^{p}, \ldots, x_{n}\right) P\left(x_{1}\right) P\left(x_{2}\right) \ldots P\left(x_{n}\right)}{P\left(x_{i}=x_{i}^{p}\right)}
\end{aligned}
$$

where $P\left(x_{i}=x_{i}^{p}\right)$ is the probability that the state of root node $x_{i}$ is $x_{i}^{p}$, and $P\left(x_{i}=x_{i}^{p}, T=T_{p}\right)$ is the joint probability that state of the root node $x_{i}$ is $x_{i}^{p}$ and the state of the leaf node $T$ state is $T_{p}$.
(2) Root node fuzzy importance

Importance describes the degree of influence on the leaf node during the evolution of the fault state from 0 to 1 when the root node fails. Using BN inference algorithm, the importance calculation formula can be given.

Under separate conditions when the state of node $x_{i}$ is $x_{i}^{p}=1$, the fuzzy probability importance of the leaf node $T$ under the state of $T_{p}=1$ is shown in Eq. (9).

$$
\begin{aligned}
I_{T}^{1}\left(x_{i}\right. & =1)=E_{T}^{1}=P\left(T=1 / x_{i}^{p}=1\right)-P\left(T=1 / x_{i}^{p}=0\right) \\
& =\frac{P\left(T=1, x_{i}^{p}=1\right)}{P\left(x_{i}^{p}=1\right)}-\frac{P\left(T=1, x_{i}^{p}=0\right)}{P\left(x_{i}^{p}=0\right)}
\end{aligned}
$$

Under separate conditions when the state of node $x_{i}$ is $x_{i}^{p}=1$, the fuzzy probability importance of the leaf node $T$ under the state of $T_{p}=0$ is shown in Eq. (10).

$$
\begin{aligned}
I_{T}^{0}\left(x_{i}\right. & =1)=E_{T}^{0}=P\left(T=0 / x_{i}^{p}=1\right)-P\left(T=0 / x_{i}^{p}=0\right) \\
& =\frac{P\left(T=0, x_{i}^{p}=1\right)}{P\left(x_{i}^{p}=1\right)}-\frac{P\left(T=0, x_{i}^{p}=0\right)}{P\left(x_{i}^{p}=0\right)}
\end{aligned}
$$

The fuzzy probability importance of the root node $x_{i}$ for the leaf node $T$ under fault state of $T_{p}$ is shown in Eq. (11).
$I_{T}^{T_{p}}\left(x_{i}\right)=\frac{1}{K-1} \sum_{i=1}^{K} E_{T}^{T_{p}}$
Then the two fuzzy probability importance degrees for the leaf node $T$ under fault state of $T_{p}$ are shown in Eqs. (12) to (13).
$I_{T}^{1}\left(x_{i}\right)=\frac{1}{K-1} \sum_{p=1}^{K} E_{T}^{1}$
$=\sum_{p=1}^{2} \frac{P\left(T=1, x_{i}^{p}=1\right)}{P\left(x_{i}^{p}=1\right)}-\frac{P\left(T=1, x_{i}^{p}=0\right)}{P\left(x_{i}^{p}=0\right)}$
$I_{T}^{0}\left(x_{i}\right)=\frac{1}{K-1} \sum_{p=1}^{K} E_{T}^{0}$
$=\sum_{p=1}^{2} \frac{P\left(T=0, x_{i}^{p}=1\right)}{P\left(x_{i}^{p}=1\right)}-\frac{P\left(T=0, x_{i}^{p}=0\right)}{P\left(x_{i}^{p}=0\right)}$
where $K$ is the number of failure states for root node $x_{i}$. Since there are only two node failure states discussed in this article, $K=2$ is taken.
(3) Root node critical importance

Under separate conditions when the state of node $x_{i}$ is $x_{i}^{p}$, the critical importance of a leaf node $T$ under fault state of $T_{p}$ is shown in Eq. (14).
$I_{T}^{k}\left(x_{i}=x_{i}^{p}\right)=\frac{P\left(x_{i}=x_{i}^{p}\right) I_{T}^{T_{p}}\left(x_{i}=x_{i}^{p}\right)}{P\left(T=T_{p}\right)}$
The critical importance of the root node $x_{i}$ to the leaf node $T$ under fault state of $T_{p}$ is shown in Eq. (15).
$I_{T}^{k}\left(x_{i}\right)=\frac{1}{K-1} \sum_{p=1}^{K} I_{T}^{k}\left(x_{i}=x_{i}^{p}\right)=\sum_{p=1}^{2} I_{T}^{k}\left(x_{i}=x_{i}^{p}\right)$
(4) Root node posterior probability

If the occurrence probability of the leaf node is known, the posterior probabilities of the intermediate node and the root node of the BN network can be obtained using the reverse inference algorithm of the BN network. If the failure probability of leaf node $T$ in the BN network is known, the posterior probability of the root node $x_{i}$ with the failure state being $x_{i}^{p}$ is shown in Eq. (16).

$$
\begin{aligned}
& P\left(x_{i}=x_{i}^{p} / T=T_{p}\right)=\frac{P\left(x_{i}=x_{i}^{p}, T=T_{p}\right)}{P\left(T=T_{p}\right)} \\
& =\frac{\sum_{x_{1}, x_{2}, \ldots, x_{p}} P\left(x_{1}, x_{2}, \ldots x_{n}, T=T_{p}\right)}{P\left(T=T_{p}\right)}
\end{aligned}
$$

The above formula utilizes the fault diagnosis ability of the BN network, which can be beneficial to system troubleshooting.

## 4 RESULTS AND DISCUSSION

### 4.1 Results Calculation

Taking a railway station and line carrying coil steel goods on a Chinese railway as an example, the calculation is carried out. On this line, coil steel is shipped from industrial siding A through two cargo inspection stations B and C, and transported to freight yard D for unloading. Based on the above conditions, relevant influencing factors such as weight inspection, pre-loading inspection, loading operation, and inspection after loading can be deleted, namely $X_{9} \sim X_{20}, X_{29} \sim X_{32}, X_{38} \sim X_{44}, X_{48} \sim X_{50}$. Based on the fault BN network model, it is necessary to determine the fault fuzzy probability of the root node. The expert survey weight method is used to determine the probability of the root node. The specific process is as follows: 4 railway transportation experts from different fields are selected, and different weights are assigned to experts from different fields. The weights of domain experts are shown in Tab. 2.

Table 2 Domain expert weight


Based on personal experience, with reference to the risk occurrence probability level criteria defined in Tab. 3, the risk factors of railway wagon loading status are evaluated.


The 5 semantic values in Tab. 4 are defined to represent different fuzzy numbers.

Table 4 Risk probability rating standard


The linguistic values judged by experts are represented by triangular fuzzy numbers, and a comprehensive evaluation fuzzy set of the weights of various influencing factors is established. The weighted average method is used to weighted average the weights assigned to experts in the expert data set, and the final probability median is calculated using Eq. (17).

$$
P\left(x_{i}\right)=\frac{\sum_{k=1}^{4} W_{k} Q_{k i}}{\sum_{k=1}^{4} W_{k}}
$$

where $P\left(x_{i}\right)$ represents the final estimated value of the occurrence probability of the root node $i, W_{k}$ is the weight of the No. $k$ evaluator, and $Q_{k i}$ is the initial fuzzy probability value given by the No. $k$ evaluator. By fuzzifying $m_{i}$ and through expert consultation and consulting relevant literature, the fuzzification parameters are finally determined as $\alpha_{i}=\beta_{i}=0.12 m$ and the fuzzy prior probability subset of the root node is finally determined. The fuzzy prior probability subset of the root node is shown in Tab. 5.

Table 5 Fuzzy failure probability subset of root node


Combining the conditional probability table CPT derived from the logical relationship of the fault tree, using

Eq. (7) to Eq. (8), the failure probability of a leaf node is obtained in Eq. (18).

$$
\begin{aligned}
& P\left(T=T_{q}\right)=\sum_{x_{1}, x_{2}, \ldots, x_{m}} P\left(x_{1}, x_{2}, \ldots, x_{n}, T=T_{q}\right) \\
& =\sum_{x_{1}, x_{2}, \ldots, x_{m}} P\left(T=1 / x_{1}, x_{2}, \ldots, x_{n}\right) P\left(x_{1}\right) P\left(x_{2}\right) \ldots P\left(x_{n}\right) \\
& =\sum_{x_{1}, x_{2}, \ldots, x_{54}} P\left(T=1 / x_{1}, x_{2}, \ldots, x_{54}\right) P\left(x_{1}\right) P\left(x_{2}\right) \ldots P\left(x_{54}\right)= \\
& =3.43 \times 10^{-2}
\end{aligned}
$$

By fuzzifying the probability of accidents occurring at leaf nodes in the loading state of railway wagons, $\alpha_{i}=\beta_{i}=$ $0.12 m_{i}$ the fuzzy subset of the probability of failure occurring at leaf nodes in the loading state of railway wagons is as follow:

$$
P\left(T=T_{q}\right)=\left\{3.02 \times 10^{-2}, 3.43 \times 10^{-2}, 3.84 \times 10^{-2}\right\}
$$

Referring to the risk classification in Tab. 3, the probability of failure of the wagon loading state on this line is located at the fourth level of the risk occurrence probability level standard, indicating a high probability of accident occurrence, which is basically consistent with the results of the probability assessment conducted by experts.

### 4.2 Sensitivity Analysis

In practical applications, managers pay more attention to the factors that play an important role in the entire system and the control sequence of various risk factors. Taking the goods inspection operation as an example, where no defective loading of wagons is found, using Eq. (12), the fuzzy importance of root node to leaf node $T$ in the event of failure is obtained. The fuzzy importance curve is shown in Fig. 7.
![img-5.jpeg](img-5.jpeg)

Figure 7 Fuzzy importance curve
As can be seen from the above figure, given the fuzzy subset of root node failures, $X_{1}, X_{2}, X_{21}, X_{27}, X_{28}, X_{33}, X_{31}$, and $X_{53}$ are significantly larger than other root nodes. After discussion with experts, it is found that during railway freight transportation, operational errors by personnel such as acceptance personnel and cargo inspection personnel have resulted in a high frequency of accidents. This is due to the monotonous environment and lack of concentration of personnel during long-term on-site operations. In addition, the cargo inspection operation is highly dependent on measuring equipment, and the failure or inability to use measuring equipment may bring the failure

in cargo inspection operation. In summary, the actual situation is basically consistent with the calculation results in this article.

The key links of railway wagon loading status risk based on the critical importance of nodes are analyzed, which is conducive to improving the ability to control the risks of railway wagon loading status. Based on Eq. (14) and Eq. (15), the critical importance of the root nodes is calculated and the node critical importance curve is shown in Fig. 8. It can be seen that *X*21, *X*25, *X*31, and *X*33 are of high importance. Through configuring and optimizing metering security equipment the security risks of *X*51 and *X*53 can be reduced, but *X*21 and *X*25 with personnel as the core are difficult to improve.

![img-6.jpeg](img-6.jpeg)

**Figure 8** Critical importance curve

When an accident occurs at node *T*, the prior probability is modified using the reverse reasoning ability of the BN network, and the posterior probability under the condition of *x*1 ∼ *x*53 is obtained using Eq. (16) under *T* faults. The posterior probability of the node is shown in Tab. 6.


**Table 6** A posteriori probability subset of node fuzzy failures

![img-7.jpeg](img-7.jpeg)

**Figure 9** Ratio curve of node posterior probability to prior probability

In order to evaluate the sensitivity of the root node to accidents when a safety accident occurs in the loading state of a railway wagon, the ratio of a posterior probability to a prior probability is used to express the sensitivity of the root node to a safety accident in the loading state of a wagon. The ratio change curve of the root node is shown in Fig. 9. It can be seen that the possibility of system accidents caused by illegal acceleration, deceleration, or sliding of operators is much higher than other factors.

Discussion on the results:

(1) Risk Level is IV, whose linguistic estimation is high. It is basically consistent with the overall safety situation of railway coil steel transportation in recent years, which is necessary to take risk control or risk transfer measures.

(2) *X*47, *X*52, *X*53, *X*24, *X*31, *X*5, *X*7, *X*23, *X*25, *X*46 are the 10 risk factors with high prior probability, mainly involving the human, equipment and environmental factors in the process of truck handover and freight inspection. Risk control measures for key risk factors in the above scenarios can effectively reduce the overall risk level.

(3) Through sensitivity analysis, it can be seen that the importance of *X*21, *X*25, *X*31, *X*53 is high, and the security risk of *X*31, *X*53 can be reduced by configuring and optimizing measurement safety equipment, but it is difficult to reduce *X*21, *X*25 which are the human-centered items. Through reverse reasoning, it can be found that the possibility of accidents caused by *X*21 is much higher than other factors, so in addition to configuring and optimizing the measurement safety equipment in the cargo inspection link and the handover link, it is necessary to strengthen the training, management and assessment of cargo inspection personnel and vehicle delivery personnel.

The risk assessment of railway wagon loading status for the transportation scheme under the example scenario can effectively identify the key links and key factors affecting the safety state of railway wagon loading status, so as to accurately take risk prevention and control measures. Further, it provides reliable technical support for the design of railway freight service scheme to ensure the safety of the whole process of cargo transportation.

# **5 CONCLUSION**

This article proposes a scenario of classification-based risk assessment method for railway wagon loading conditions. SHEL model is used to systematically analyze the factors affecting the loading status of railway wagons under various operating scenarios, which can expand the same type of factors into different scenarios and is conducive to accurate identification and positioning of risk items under different scenarios. The fuzzy fault tree and BN are complemented and fused, which is expanded and improved on the basis of traditional fault tree and BN network fusion. This method can effectively solve the problems of traditional fault tree operations that are complex and cannot be reasoned in both directions, which is conducive to the development of fault tree and Bayesian network analysis methods.

Using SHEL model, accident tree model, and Bayesian network model comprehensively, a risk assessment method for railway wagon loading status based on scenario classification is proposed, which can accurately diagnose and locate risk scenarios and risk factors compared to traditional railway freight safety risk assessment, and increase the operability of this method. At the same time, through the forward reasoning algorithm of BN network, it

can not only directly obtain the top event failure probability from the bottom event failure probability, but also calculate the fuzzy probability importance and critical importance of the bottom event, so as to troubleshoot accidents and simplify the calculation process.

The proposed method is calculated in the form of a numerical example, and the conclusions obtained are basically consistent with the results of expert discussions in the actual situation, which verifies the feasibility of the method and can be used as a decision-making tool for safety management of railway wagon loading conditions.

## Acknowledgements

This research was funded by Research and development plan of China State Railway Group Co., Ltd., grant number K2023X006, and scientific research project of China Academy of Railway Sciences Corporation Limited, grant number 2022YJ011.

## Contact information:

Fei YE, Doctoral Candidate, Associate Researcher Graduate Department, China Academy of Railway Sciences, Transportation \& Economics Research Institute, China Academy of Railway Sciences Corporation Limited, No. 2 Daliushu Road, Haidian District, Beijing, China E-mail: yfhl2011@126.com

Qigang LIU, Researcher
Transportation \& Economics Research Institute, China Academy of Railway Sciences Corporation Limited, No. 2 Daliushu Road, Haidian District, Beijing, China E-mail: liuqigang@rails.cn

Jing JIN, Associate Researcher
(Corresponding author)
Transportation \& Economics Research Institute, China Academy of Railway Sciences Corporation Limited, No. 2 Daliushu Road, Haidian District, Beijing, China E-mail: 65254631@qq.com

Tiegang ZHANG, Senior Engineer
Freight Transport Department, China State Railway Group Co., Ltd., No. 10, Fuxing Road, Haidian District, Beijing, China E-mail: 313072951@qq.com

Wenqiao SUN, Associate Researcher
Graduate Department, China Academy of Railway Sciences, Transportation \& Economics Research Institute, China Academy of Railway Sciences Corporation Limited, No. 2 Daliushu Road, Haidian District, Beijing, China E-mail: sunwenqiao@rails.cn

Yue GE, Research Assistant
Transportation \& Economics Research Institute, China Academy of Railway Sciences Corporation Limited, No. 2 Daliushu Road, Haidian District, Beijing, China E-mail: julia1412@163.com