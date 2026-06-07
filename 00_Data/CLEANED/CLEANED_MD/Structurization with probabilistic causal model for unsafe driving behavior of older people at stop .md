# Advance Publication by J-STAGE 

## Mechanical Engineering Journal

DOI: 10.1299/mej. 24-00151

Received date : 10 April, 2024
Accepted date : 22 August, 2024
J-STAGE Advance Publication date : 1 September, 2024

# Structurization with probabilistic causal model for unsafe driving behavior of older people at stop sign intersections 

Byung hyun KIM*, Kakeru TAKAHASHI*, Hiroshi YOSHITAKE**,<br>Tomoya MURAKI***, Yoshiro EGAMI**** and Motoki SHINO**<br>*The University of Tokyo<br>5-1-5 Kashiwanoha, Kashiwa, Chiba, 277-8563, Japan<br>E-mail: bkim@s.h.k.u-tokyo.ac.jp<br>**Tokyo Institute of technology<br>2-12-1 Ookayama, Meguro, Tokyo, 152-0033, Japan<br>***TIER IV, Inc.<br>1-12-10 Kitashinagawa, Shinagawa, Tokyo, 140-0001, Japan<br>****Minami Holdings Co., Ltd.<br>3-2-20 Shimoori, Onojo, Fukuoka, 816-0952, Japan


#### Abstract

To reduce unsafe driving among older drivers, clarifying the process and factors leading to such behaviors is essential. In this study, we proposed a method to express the process and factors leading to unsafe driving using Bayesian networks. In the proposed method, the flow leading to unsafe driving is divided into three stages: driver characteristics, driving behavior, and driving unsafeness. Driver age, various driving behaviors, traffic violation and collision risk were selected as indices of driver characteristics, driving behavior, and driving unsafeness. By organizing and layering these indices in the order of cause, behavior and result, the indices were set to align with the timeline. With the proposed structuring method, we constructed models of deceleration and intersectionpassing behaviors based on the driving data of older drivers at stop-sign intersections. The results revealed that driving characteristics and environmental factors influence indices related to the position and speed at intersection entry, capturing relationships leading to violations at stop lines and collision risk with crossing vehicles at intersections. Moreover, it was confirmed through probability inference that the association shown in the structured results was identical to the known driving characteristics of older drivers. According to this result of probability inference, the validity of the proposed structuring method was confirmed.


Keywords: Driving behavior, Older people, Bayesian networks(BN), Unsafe driving, Driving evaluation

## 1. Introduction

In recent years, traffic accidents involving older drivers have become a significant issue in Japan. The number of traffic accidents per 100,000 drivers aged 75 and above is more than 2.5 times higher than the number for drivers under 75 (Tokyo Metropolitan Police Department, 2022). Additionally, the number of drivers aged 75 and above has increased by approximately 1.8 times compared to a decade ago, and those aged 80 and above have increased by about 1.9 times, indicating a predicted further increase in the number of older drivers (Cabinet Office, 2022).

Various initiatives have been implemented to reduce traffic accidents involving older drivers, with one example surrender of driver's license. However, the car serves as a crucial means of transportation for the older, and a decrease in mobility is suggested to have implications for health, such as a decline in autonomy and an increase in depressive tendencies (Chihuri et al., 2016; Ragland et al., 2005). For these reasons, supporting the continued driving of older drivers is crucial. Means have been conducted, such as interventions through automatic braking systems in vehicles (Tsugawa, 2006) and the application of user-friendly automobile controls (Kim et al., 2011), to reduce the risk of accidents involving older drivers and enable them to continue driving.

Understanding the characteristics of older drivers associated with unsafe driving is essential to consider means for promoting safe driving among older drivers. According to Suzuki's study (2007), the characteristics of older drivers can be categorized into four perspectives: physical, psychological, driving, and social. These characteristics vary among individuals based on their innate qualities, driving environments, and experiences, and these are reported to interact with each other. Therefore, there is individual variation in the driving characteristics of older drivers and individual differences in the causes leading to unsafe driving. Moreover, driving behavior follows a series of human behaviors, such as cognition, judgment, and operation, involving the simultaneous execution of multiple tasks in response to the surrounding environment. Hence, the causes and the process leading to unsafe driving are diverse. It is necessary to understand how the characteristics of older drivers, influenced by aging, impact their behaviors and how these behaviors may lead to unsafe driving with structurization of driving behavior to develop means that enable older drivers to continue driving safely.

# 2. Related works 

### 2.1 Unsafe driving by older drivers

Existing studies have analyzed driving data obtained in simulated urban environments and real roads to understand the unsafe driving behaviors of older drivers. In the study by Choi et al.(2017), real-world driving data was used to confirm that the trajectory and behavior of older drivers during intersection turns lack consistency and exhibit a wider range compared to non-elderly drivers. Romoser et al.'s study (2013) utilized a driving simulator to observe that older drivers have less confirmation behavior towards potential collision objects during intersection turns than non-elderly drivers. They explored improving older drivers' surrounding awareness through active feedback training. Yonekawa et al.(2014) conducted a study using a driving simulator to compare non-elderly and older drivers, finding that older drivers often exhibit inappropriate deceleration and insufficient safety confirmation behaviors, especially at stop lines. Sato et al.'s study (2014) on the passing behavior at stop-sign intersections, which are prone to accidents among older drivers, proposed driving behavior indices based on comparing expert drivers exhibiting model driving and older drivers. Using these indices, they aimed to understand the characteristics of unsafe driving behaviors in older drivers.

Previous research has focused on capturing the characteristics of older drivers' driving behaviors and examining the relationship between driving behaviors and driver characteristics. In contrast, to understand unsafe driving by older drivers, this study aims to elucidate the process leading to unsafe driving behaviors by revealing how unsafe driving behaviors are connected to the characteristics of driving behaviors and other driving behaviors.

### 2.2 Structurization of driving behavior

Studies understanding the relationship between driving characteristics and behaviors based on collected driving data and constructing mathematical models from these relationships often employ multivariate analysis and machine learning. For instance, in the research of Zafian et al. (2021), machine learning was applied to the SHRP2 NDS dataset to investigate the causes of accidents among older drivers. The study revealed that older drivers have a higher collision risk during left turns at signal intersections than non-elderly drivers. The study extracted factors such as health and cognitive function of older drivers individuals as potential causes. In another study by Lucidi et al. (2014), structural equation modeling was conducted using interview survey data to examine the relationship between driver characteristics, such as personality of older drivers, and driving unsafeness. The findings reported that positive personality and attitudes among older drivers are associated with a reduction in risky driving behaviors.

The probabilistic causal model is one example of a machine-learning model that can express such relationships. The probabilistic causal model estimates causes and predicts structures based on the features and frequency biases present in the data. Hidden Markov models and Bayesian networks are examples of probabilistic causal models. Among them, Bayesian networks stand out as they do not require explicit objective functions and prior information can be set as restraints on the model. These features make them easily interpretable in a semantic sense. In the field of driving, Bayesian networks are used for applications such as driver-state identification (Sato et al., 2018).

Furthermore, some studies utilize Bayesian networks to visualize the flow and relationships of driving behaviors. In the research by Hassan and Abdel-Aty (2013), conditional probabilities were employed to explore a broad range of

relationships between collision conditions (e.g., collision location, method, road conditions, vehicle speed) and driver age. The study indicated that young and older drivers are the primary generations involved in collision accidents. It revealed that young drivers drive in situations and conditions that increase collision risk, while older drivers avoid driving in unfavorable conditions.

Kumagai and Akamatsu(2006) constructed a driving behavior model for behavioral prediction using Bayesian networks based on a driving behavior database, specifically focusing on the behaviors leading from deceleration to stopping at stop-sign intersections. In this model, the timing of each behavior, the relationship with leading vehicles and passing vehicles, and factors influencing driving behavior, such as intersection geometry, were represented using Bayesian networks. The interactions among these factors and their influence on driving behavior were modeled.

In evaluating driving behavior, Zhu et al.(2017) organized information on road types, slopes, speed limits, and other traffic conditions. They focused on driver acceleration and deceleration in traffic conditions and proposed a method to evaluate the relationship between driving behavior and driving risk using Bayesian networks. This study leverages the advantages of Bayesian networks to visualize the relationships between various pieces of information and driving behavior.

While these previous studies demonstrate information related to driving behavior, they do not explicitly represent the sequential flow of cognitive process, decision-making, and operations over time. Additionally, understanding the factors contributing to unsafe driving and the timing of their occurrence in the driving behavior flow is crucial to practice safe driving. Therefore, it is necessary to visualize the flow of unsafe driving behavior over time.

# 3. Research objective 

According to the previous section, this study adopts the Bayesian networks to structure and visualize various information influencing driving, including their relationships, to depict the flow of driving characteristics, driving behavior, and the progress to accidents or violations for older drivers. This approach allows the interpretation of this information in a chronological sequence. Therefore, the research objective is to propose a structuring method that allows the visualization of the relationships between the driving characteristics, driving behavior, and unsafe driving behavior of older drivers. The steps to achieve this objective are outlined below:
I. Organize essential factors and restraints for structuring.
II. Propose a method for structuring driving behavior.
III. Evaluate the validity and reliability of the proposed structuring method.

In this paper, the essential factors and restraints for structuring are organized, and a structuring method is proposed in Section 4. Section 5 describes the application results of the proposed method to a certain driving scenario. The validity and reliability of the proposed method is evaluated in Section 6. Section 7 discusses the proposed method. Finally, Section 8 shows the conclusions of this paper.

## 4. Structuring method of driving behavior

To propose a structuring method, we considered functional requirements and restraints for structuring and set essential factors and their requirements for structuring.

### 4.1 Unsafe driving by older drivers

The requirements of the structuring method are set as follows to achieve the research objective.

- Visualize the relationship between driver characteristics, driving behavior, and driving unsafeness.
- Express the characteristics of driving behavior of drivers with different driver characteristics.

To satisfy the abovementioned requirements and consider that human behavior is based on a series of steps of recognition, judgment, and operation, we set the following restraints when structuring a Bayesian network.

- The structure follows a chronology based on the time the events happened.
- No influence between driving characteristics and other vehicle factors.


# 4.2 Essential factors and its requirements 4.2.1 Essential factors 

It is necessary to set factors that follow the requirements and restraints to meet the requirements and restraints of the structuring method. The set-up of factors involves the index setting, which quantifies their concepts and incorporates them into the structure. Indices serve as benchmarks for quantifying the concept of factors, and the requirements for these indices are set based on insights revealed in existing studies related to driving behavior. As mentioned above, structuring driving behavior requires visualizing the relationship between driver characteristics, driving behavior, and driving unsafeness, such as accidents or violations. Therefore, it is necessary to set indices representing driver characteristics, driving behavior, and driving unsafeness to meet the requirement.
Like any other behavior, driving behavior is influenced by the external environment. Stanton and Salmon(2009) classified external influences affecting driver behavior and leading to driver errors into categories such as road infrastructure, vehicles, drivers, other traffic participants, and the external environment. These numerous external factors may make understanding their interactions and influences challenging. Thus, external factors must be considered to understand the cause and process of driving behavior. Therefore, the indices for structuring in this paper are limited to driving behavior, driving unsafeness, driver characteristics, and external influences.

### 4.2.2 Requirements of each factor for structuring driving behavior

Each essential factor for structuring needs to be defined and limited clearly with indices setting for structuring driving behavior. For the structurization of driving behavior, the essential factors are represented with indices, and each index is represented as a component of the structure.

Firstly, regarding driving behavior indices, this study considers instructors as people who practice safe driving behavior and uses their driving behavior as an index. The standard of indices for structuring aims to evaluate based on the instructor's reference whether the driver is performing the necessary actions and whether the timing and degree of driving actions (e.g., level of manipulation) are appropriate.

Secondly, the requirements for indices evaluating driving unsafeness include the ability to express states where violations or high accident risks occur numerically. In this study, driving unsafeness is defined as violations or accidents, and "high unsafeness" is defined as states with violation occurrence or high accident risks. Therefore, the objective indices for unsafeness are set based on criteria that can objectively judge driving unsafeness, such as indices quantifying the possibility of accidents or instructor evaluations.

Thirdly, the requirements for indices related to driver characteristics involve the ability to express unique characteristics the drivers possess. Therefore, these indices are set based on characteristics that can influence operational behaviors in the driving process, particularly those related to mental and physical characteristics.

### 4.3 Proposal of structuring method

We proposed a structuring method for driving behavior with the factors mentioned in the previous sections. The steps of the proposed method are set as follows.
(1) Select a target scenario.
(2) Set indices for the target scenario that meet the requirements mentioned in Section 4.2.
(3) Acquire driving data to calculate the indices.
(4) Calculate the indices with the acquired data.
(5) Build a Bayesian network using the calculated indices with restraints mentioned in Section 4.1.

# 5. Application of structuring method 

### 5.1 Selection of target driving scenario

According to accident statistics categorized by age group and accident type (Tokyo Metropolitan Police Department, 2022), older drivers are more involved in head-on, rear-end, and right/left turn collisions than non-elderly drivers. Among these, accidents at unsignalized intersections are prevalent. Therefore, this paper focuses on head-on collisions, which have a high occurrence rate among older drivers. Thus, passing through an unsignalized intersection with a stop sign while proceeding straight is selected as the target driving scenario.

In this scenario, the vehicle must stop before the stop line and pass through the intersection. Hence, in this paper, the process of violating the stop at a stop-sign intersection is referred to as "deceleration behavior," and the entry into the intersection from the stop line to the point of contact with crossing vehicles is defined as the "intersection passing behavior," which represents the process leading to the potential occurrence of head-on collisions.

### 5.2 Setting indices of target driving scenario

### 5.2.1 Driver characteristics and external factors

Driver's unique characteristics, such as the driver's physical or psychological characteristics, can be used as indices of driver characteristics. In this study, the driver's age was selected as an index because the purpose was to extract the characteristics of driving behavior exhibited by older drivers using indices of driving characteristics. The driver's age can represent multiple driver characteristics because increased age affects the driver's cognition, judgment, and behavior, and many countries are re-examining the driver's ability based on age.

This study limits the driving environment to a driving school and only considers the impact on traffic participants as external influences to reduce the impact of external influences. For the details of external factors in driving school, other traffic participants are only vehicles. Other vehicles may appear in front, behind, left, or right based on their direction of travel. In the deceleration behavior, if there was a front vehicle, the drivers might follow the front vehicle or stop behind it, affecting driving behavior. This indicates that the behavioral effect from the front vehicle is considerable compared to the case from other directions. Therefore, the presence of a front vehicle was adopted as an index.

### 5.2.2 Driving behavior

The characteristics of driving behavior exhibited by older drivers revealed in existing research were organized to set the indices of driving behavior that can represent the process leading to unsafe driving behavior in the selected target scenario. Previous studies have identified specific driving behavior characteristics of older drivers at stop-sign intersections, such as delayed initiation of deceleration, rolling stops, frequently violating stop lines, and insufficient safety checks beyond the stop line (Yonekawa et al., 2014). Moreover, unsafe driving behaviors of older drivers have been reported, including sudden acceleration when entering the intersection after stopping at the stop line, insufficient checking of blind spots, and prematurely concluding safety checks (Sato et al., 2014).

Considering the reported tendencies of older drivers to accelerate abruptly and lack confirmation of blind spots when entering the intersection after stopping at the stop line, indices of driving behavior were selected as illustrated in Fig. 1. As shown in the figure, the intersection passing behavior was categorized into Sections 1 and 2 to understand the characteristics of older drivers regarding the blind spots. Section 1 is the interval from the stop line to the position where the vehicle front enters the intersection. Section 2 is set as the interval from the end of Section 1 to the position where the driver enters the intersection.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Driving behavior indices of the target driving scenario.

# 5.2.3 Driving unsafeness 

Unsafe driving may result in violations of traffic laws or traffic accidents. For example involving violations, drivers must follow the stop-sign regulations in the target scenario. If the regulations are not followed, it is considered a violation, and the presence of a violation can be used as an index showing driving unsafeness.

To objectively evaluate the unsafe driving leading to accidents at intersections, the focus is on assessing collision risk as an index. Oya's study (2019) adopted the probability of collision with virtual vehicles hidden in blind spots as an evaluation index of collision risk. This index assesses the probability of collision accidents with vehicles emerging from blind spots based on the driver's driving data.

Based on the index in Oya's study, the initial scene for risk assessment in this paper is illustrated in Fig. 2. The distance from the front end of the vehicle to the collision area is $X$, and the vehicle speed is $V_{\text {ego }}$. When the driver detects a crossing vehicle traveling at a constant speed $V_{c r s}$, the vehicle decelerates at a constant rate $\&$ after a brake reaction time $T_{r}$. Here, the speed of the collision target, the crossing vehicle, is assumed to follow a normal distribution (Tamura et al., 1987). Thus, the collision risk index $S_{d}$, can be expressed by integrating the probability density of the collision target's speed distribution to determine the presence of collisions for all possible collision target speeds. Therefore, the collision risk index $S_{d}$ can be expressed by the Eq. 1.

$$
S_{d}=\int G\left(X, y, V_{e g o}, V_{c r s}\right) p\left(V_{c r s}\right) d V_{c r s}
$$

Here, $y$ represents the distance from the front end of the crossing vehicle to the collision area, and $p$ is the probability density function representing the crossing vehicle speed. $G$ is the decision function for collision occurrence when the crossing vehicle is detected.

The driver's field of view is set as a constant range $\theta$, and with the driver's face direction, the detection of the crossing vehicle is identified as the time when the driver's field of view overlaps the crossing vehicle. Figure 3 shows the flow of detection of a crossing vehicle and deceleration at a stop-sign intersection.

In this study, as an objective index for evaluating the unsafeness of passing through stop-sign intersections, the collision risk index $S_{d}$ after the stop line is adopted. To calculate the collision risk index in the target scenario, a bicycle approaching from behind an obstacle was assumed as the crossing vehicle.

![img-1.jpeg](img-1.jpeg)

Fig. 2 Initial scene for collision risk assessment with parameters related to the collision risk index.
![img-2.jpeg](img-2.jpeg)

Fig. 3 Flow of crossing vehicle detection and deceleration.

# 5.3 Acquisition of driving data 

Data acquisition of the selected target scenario was done within a controlled environment at a driving school. A course within the driving school premises, including a poorly visible stop-sign intersection, was set up, as shown in Fig. 4. A driving experiment was conducted with 33 individuals, 19 older drivers aged 75 and above, and 14 non-elderly drivers. Before the experiment, participants were provided with an explanation of the content, informed consent was obtained, and the experiment was conducted. This experiment was approved by the Ethics Review Board of the University of Tokyo Life Sciences Committee.

The experiment utilized a vehicle equipped with cameras and a LiDAR (Light Detection and Ranging) sensor, as illustrated in Fig. 5. The recorded information included video data of the vehicle's front and the driver's face, vehicle data such as speed and acceleration, driver's operational data from the accelerator pedal, brake pedal, and steering wheel, and accurate vehicle position. The self-position of the vehicle was calculated based on the point cloud data obtained with the LiDAR sensor mounted on the vehicle's top and a pre-generated 3D map of the driving school course. Table 1 shows each equipment and each sampling rate, and for driving behavior analysis, the time axis was synchronized based on

LiDAR information. Additionally, the participants were administered a questionnaire to obtain basic personal information such as age, driving history, and cognitive test results in the license renewal process for older drivers.
![img-3.jpeg](img-3.jpeg)

Fig. 4 The front view of stop sign intersection.
![img-4.jpeg](img-4.jpeg)

Fig. 5 Experimental vehicle.

Table 1 Equipment and its sampling rate


![img-5.jpeg](img-5.jpeg)

Fig. 6 Sample result of acquired data through the intersection with the stop sign.

The experiment successfully obtained driving data from older and non-elderly drivers at a stop-sign intersection. Figure 5 illustrates an example of the driving data at the stop-sign intersection. The driving data in Fig. 6 represents the data of a participant whose speed was closest to the overall average speed. As depicted in the figure, the driver decelerates as they approach the stop-sign intersection, makes a stop, and then departs slowly.

# 5.4 Building a Bayesian network 

### 5.4.1 Index layering and discretization

Based on the driving experiment data, the timeline layering along the timeline was performed to incorporate the

driving behavior indices set in Section 5.2 into the model. Following the driving behavior procedure illustrated in Fig. 6, the indices were categorized as shown in Fig. 7. On constructing the model, the indices were organized with labels in order of cause, behavior, and result. Specifically, for the process leading to unsafe behavior, inherent human cognition characteristics were considered the cause, and violation and collision risk were considered the result. The behavior at a stop-sign intersection was set in sequence as deceleration, stop, confirmation, and acceleration. In driving, multiple actions can occur simultaneously in this process. Thus, the indices were set to align with the timeline.
Discretization of indices in deceleration and intersection passing behaviors were conducted, respectively. Speed was discretized into three levels: low, middle, and high, and position-related indices were discretized based on the distance from the stop line into three levels: near, medium, and far. For discretization of driver characteristic indices, age was classified into two groups: older drivers and non-elderly drivers, based on age 65.
![img-6.jpeg](img-6.jpeg)

Fig. 7 Layers of indices along the timeline.

# 5.4.2 Structural learning conditions 

Structural learning was performed using BayoLinkS (NTT DATA Mathematical Systems Inc, 2022) to construct a Bayesian network. The maximum likelihood method was employed for structurization. The relationship between nodes was set according to the indices layering mentioned in the previous section. Additionally, the maximum number of new nodes was limited to two. This condition, which limits the number of arrows, facilitates a clearer understanding of the structure.

### 5.4.3 Results of structurization

- The scenario with deceleration behavior : The results represented by the Bayesian network using the collected data are shown in Fig. 8. The presence of violation at the stop line was directly related to the position and speed at the minimum speed. The start of deceleration behavior influenced these parameters at the minimum speed. Furthermore, this deceleration start behavior was influenced by age. This result visualized the process leading to the violation at the stop line.

- The scenario with intersection passing behavior : Using the proposed structuring method, we visualized the intersection-passing behavior. From Fig. 9, the acceleration start position and the percentage of confirmation time in Section 1 indicated a direct dependency on collision risk. Additionally, the age index influenced the end position of the confirmation behavior, meaning that it affects the termination of the confirmation behavior, and the flow from driving characteristics to unsafeness can be expressed.

Therefore, the proposed method made it possible to visualize the factors leading to unsafe driving behaviors indicating violations and collision risk.
![img-7.jpeg](img-7.jpeg)

Fig. 8 Structuring results of deceleration behavior.
![img-8.jpeg](img-8.jpeg)

Fig. 9 Structuring results of intersection passing behavior.

# 6. Evaluation of structuring method 

In this section, the validity and reliability of the structuring method are assessed. We evaluated the validity and reliability of the structuring method based on the relationship between the known characteristics of older drivers and the characteristics obtained through the structuring results.

### 6.1 Method

To evaluate the validity of the structured model, we focused on whether known characteristics of older drivers driving behavior were represented. We performed probability inference to calculate driving behavior indices based on age. Probability inference is a method that estimates the distribution of probability variables for other nodes when the probability distribution for some nodes is given on the Bayesian network. For example, Zou and Yue's study (2017) constructed a Bayesian network model to analyze traffic accident causes using data on vehicles, collision situations, and road environments. The study used probability inference to represent that the collision angle is more likely to be a right angle in the case of a signal violation. Therefore, in the context of a probabilistic causal model, probability inference allows us to confirm the impact of the desired indices by inducing changes in those indices. Using this method, we examined the changes in driving behavior indices based on the age index, which categorizes non-elderly and older drivers.

In order to evaluate the reliability of a structured model, the reliability of the structured model must be defined. This study proposes a method to structure the process leading to unsafe driving. In other words, since the relationship expressed through structuring indicates a flow toward unsafe driving, the reliability of the structured model is defined as the ability to continuously represent the relationship between indices expressed through the proposed method.

To calculate the reliability of the structured model, cross-validation was performed on the obtained data sets. As a method of cross-validation, the K-fold cross validation can be used, but considering the small number of data sets available for this model, the leave-one-out validation was adopted. Collision risk was set as an objective variable to be confirmed through cross-validation.

### 6.2 Results

### 6.2.1 Deceleration behavior

Previous research (Yonekawa et al., 2014) has highlighted characteristics of older drivers during deceleration, such as delayed deceleration timing and failure to stop. Figure 10 shows the probability inference results for the required deceleration, the minimum speed, and its position concerning intersection entry.

Comparing the posterior probabilities of older drivers with the prior probabilities, the probability of "high" required deceleration during intersection entry increased significantly from 0.34 to 0.45 . This probability inference result indicates that older drivers require greater deceleration during entry into stop-sign intersections compared to non-elderly drivers. This result implies a tendency for delayed deceleration timing.

Additionally, as a characteristic of minimum speed during intersection entry, the probability of failure to stop increased from 0.34 to 0.46 . As a characteristic of the position of minimum speed concerning the intersection, the probability of crossing the stop line increased from 0.39 to 0.48 . Therefore, older drivers tend to engage in unsafe driving near the stop line and violations such as rolling stops compared to non-elderly drivers. Thus, the results of probability inference using the model based on the collected data demonstrate that the characteristics of older drivers' driving behavior can be represented, validating the probabilistic causal model structured with the proposed method.

![img-9.jpeg](img-9.jpeg)

Fig. 10 Probabilistic inference results in deceleration behavior.

# 6.2.2 Intersection passing behavior 

Previous research (Yonekawa et al., 2014) has highlighted older drivers' characteristics during passing intersections, such as a lack of safety confirmation due to rapid acceleration after stopping. Figure 11 illustrates the results of probabilistic inference for the acceleration start position and collision risk during intersection crossing. From this figure, it can be observed that when the acceleration start position during intersection crossing is near the stop line, meaning the acceleration starts just before entering the intersection, the probability of collision risk increases. Moreover, if the confirmation behavior in Section 1, from the stop line to the entry point of the intersection, is insufficient, the acceleration start position becomes just before entering the intersection, leading to higher collision risk. This result indicates that unsafe driving behavior due to rapid acceleration immediately after stopping and inadequate safety checks for blind spots increase the collision risk during intersection entry.

The probabilistic causal model for deceleration behavior and intersection-passing behavior structured by the proposed method, along with the results of probabilistic inference, allowed the extraction of relationships between factors of driver characteristics and factors of driving behaviors leading to violations and collision risk among older drivers. Specifically, the characteristics identified for older drivers leading to unsafe behavior and violations included delayed deceleration start position, high deceleration during entry into the intersections, failure to stop at stop lines, and insufficient confirmation behaviors. These features align with the trends reported in existing studies on older drivers driving behavior (Yonekawa et al., 2014; Sato et al., 2014). Therefore, it can be concluded that the proposed method is valid for understanding factors and behaviors leading to unsafe driving and violations among drivers.

![img-10.jpeg](img-10.jpeg)

Fig. 11 Probabilistic inference result related to collision risk in intersection passing behavior.

# 6.2.3 Reliability assessment of the structured model 

For the reliability assessment of the structured model, collision risk representing unsafe driving was set as the target variable, and the model was validated using leave-one-out cross-validation, resulting in an $84 \%$ accuracy rate. Compared to Amata's study(Amata et al., 2010) modeling exemplary driving behavior at non-signalized intersections and predicting pedal operation patterns with about $75 \%$ accuracy, the result indicates a comparable outcome to existing research.

## 7. Discussion

### 7.1 Necessity of restraints for structurization

The proposed method demonstrates the relationships between indices by structurally employing a probabilistic causal model under the specified restraints. We examined the case without the restraints to clarify the necessity of the set restraints. The proposed method is designed to illustrate the process when older drivers get engaged in unsafe driving behaviors, and it sets the restraint of "following the time at which events occur." With the assumption that human behavior arises from a sequence of cognition, judgment, and operation, the observed driving behaviors in the driving data were organized according to the index classification shown in Fig. 7. Consequently, the index classification in Fig. 7 is arranged in the order of causes, actions, and results. To assess the necessity of the restraints in index layering we conducted structurization without classifying the factors and verified whether the relationships between indices could be sequentially represented through structural learning.

The results of the structurization without index classification are presented in Fig. 12. The comparison between the results obtained with restraints in the proposed method (Figs. 8 and 9) and without restraints (Fig. 12) revealed differences between the two cases.

Firstly, unsafeness and driving behaviors were found to be parent nodes of driver characteristics in the absence of restraints. This implies that unsafe driving behaviors and driving behaviors are causes of driver characteristics. However, since performed behaviors and their outcomes cannot alter the nature of the driver, the results without restraints demonstrated relationships that are not achievable. In contrast, in the proposed method with restraints, driver characteristics, driving behaviors, and unsafe driving behaviors are visualized in that order. This indicates the necessity of classifying indices in the order of causes, behaviors, and results.

Furthermore, in the results without restraints for driving behavior indices, the order of deceleration and stopping was reversed. In comparison, the proposed method with classification restraints allows the representation of driving behaviors in the sequence of deceleration, stopping, and acceleration. This highlights the need for restraints on the order of behaviors to represent driving behaviors.

Therefore, the examination results suggest that in a probabilistic causal model, it is necessary to classify indices in the order of causes, behaviors, and results to illustrate the indices in the process leading to unsafe driving behaviors.
![img-11.jpeg](img-11.jpeg)

Fig. 12 Structuring results without restraint

# 7.2 Expandability of driver characteristics 

The structuring method allows extracting features of older drivers' driving behavior through probabilistic inference using conditional probabilities between indices. In this study, the age index was considered a driver characteristic, and the relationship with driving behavior was extracted through probabilistic inference. Older drivers, in addition to aging, undergo changes in physical and mental characteristics that influence driving behavior (Suzuki, 2007). The extensibility of driver characteristic indices in the proposed method is investigated to examine whether the proposed method can visualize the relationship between various physical and mental characteristics of older drivers and driving behavior. Specifically, indices related to driver characteristics other than age are added, and the results are analyzed.

Driver characteristics of older drivers include a decline in physical abilities and functional impairments such as memory loss. Recently, the relationship between cognitive function in older drivers and safe driving has been highlighted (Karthaus and Falkenstein, 2016; Tokyo Metropolitan Police Department, 2023). To prevent traffic accidents caused by older drivers, cognitive function tests are mandated for older drivers when renewing their licenses in Japan. Therefore, cognitive function is added as a new index of driver characteristics, and the results are discussed using a probabilistic causal model.

In this study, cognitive function information is derived from the classification results of cognitive function tests conducted during the license renewal of older drivers. Cognitive function was categorized into two groups based on the presence of problems in the cognitive function test results conducted at the time of the driver's license renewal. Subsequently, cognitive function is incorporated into the model as an index of driver characteristics, and the structured results are analyzed. The results reveal that, as shown in Fig. 13, the cognitive function index influences the deceleration

start position at the intersection entry.
Probabilistic inference was used to calculate the relationship between the deceleration start position and cognitive function to understand the impact and characteristics of the added cognitive function. The results are shown in Fig. 14. From the figure, it is evident that cognitive function associated with aging influences the deceleration start point, indicating a higher probability of deceleration initiation near the stop line. This implies that older drivers individuals with impaired cognitive function delay the deceleration start point for intersection entry compared to drivers without cognitive issues. This characteristic aligns with existing research (Lodha et al., 2021) highlighting delays in deceleration behavior in older drivers with cognitive impairments. Therefore, it is concluded that expanding driver characteristic indices in the proposed method is feasible.

As driver characteristics can be expanded, the proposed method can be expected to apply various driver characteristics. In particular, the proposed method utilizes Bayesian networks, it is possible to employ various categorizable driver evaluation index, for example the Driver Style Questionnaire (DSQ), as driver characteristics.
![img-12.jpeg](img-12.jpeg)

Fig. 13 Structuring results of deceleration behavior with cognitive function index.

![img-13.jpeg](img-13.jpeg)

Fig. 14 Probabilistic inference result of deceleration start position in deceleration behavior with cognitive function index.

# 7.3 Limitations 

The structuring method proposed in this study captures driver characteristics and the lead vehicle as factors in the process leading to unsafe driving behavior in older drivers. However, three points need consideration in the proposed method based on the following perspectives.

First, when interpreting structured results, it is necessary to review the environmental influence from which the driving data was obtained. In this study, we examined the validity of the proposed method using driving data obtained in a driving school. Due to the environmental difference, the driving behavior observed in this study may be different from driving behavior on real roads. However, drivers who were observed to drive unsafely in a driving school are likely to continue driving that way on actual roads, thus many countries, including Japan, implemented graduated driver licensing systems(Mayhew et al., 1998) that can provide correction through sufficient education and evaluation (McKnight and Raymond, 2002) at driving schools. Therefore, the model results based on the driving experiment data in this study cannot completely explain the occurrence of unsafe driving in actual driving situations but can provide evidence about the cause and process of unsafe driving on actual roads.

Secondly, an examination is necessary regarding the influence of different driver characteristics. Driver characteristics exist in multiple aspects, and it is conceivable that these characteristics may influence each other. Adjusting restraint conditions by considering their relationships is necessary when considering indices for multiple driver characteristics to figure out the dominant characteristics for unsafe driving.

Thirdly, an examination is needed for external factors. In the proposed method, external factors related to other vehicles are only considered for the lead vehicle in the structurization of driving behavior. Regarding other vehicles as external factors in relation to the position of the own vehicle, vehicles crossing in front or from the sides and vehicles in the rear can be considered. Therefore, to better account for the influence of other vehicles, it is necessary to set external factors that consider the impact of traffic participants and other vehicles on driving behavior throughout the entire duration from the start to the end of the driving.

## 8. Conclusions

This paper aimed to extract factors and processes that lead older drivers to unsafe driving. We proposed a structuring method to visualize the process leading to unsafe driving behavior and applied the method to a scenario passing through the intersections with stop sign, where accidents involving older drivers are common. The following insights were

obtained:

- By using driving behavior indices, indices representing unsafeness, and indices representing driver characteristics and constructing a probabilistic causal model, the process leading to unsafe driving could be visualized along the timeline.
- The model obtained through the proposed method allowed to extract the characteristics of known older drivers driving behavior, demonstrating the validity of the proposed method to understand the factors and behaviors leading to unsafe actions and violations.
- By adopting cognitive function as a driver characteristic within the structure indices related to driving behavior and applying the proposed method, the ability to expand the driver characteristics in the proposed method was confirmed.

This study visualized the process leading to unsafe driving over time using the proposed method. The visualized results are expected to provide clues about not only the unsafe driving behavior by older drivers but also the process leading to such behavior, allowing researchers and engineers to understand the process leading to unsafe driving and attempt behavioral correction at various behavioral points.

To provide such clues in driving on actual roads, as a future task, it is first necessary to investigate the influence of other vehicles on driving behavior. The presence of other vehicles influences the driving behavior depending on the vehicle's location and driving situation. The method proposed in this study uses only the presence of the vehicle in front as an index to visualize its influence. It is thought that it is necessary to consider the influence of traffic participants, such as other vehicles and pedestrians, not just those in front, from the start to the end of driving, and to consider the setting of factors for the proposed method. In addition, it is necessary to investigate not only behavior when passing through a stop sign intersection, but also other driving scenarios, and we plan to extract factors of other driving behavior and examine the applicability of the proposed method.
