# Risk Assessment on Robotic Surgery Using Bayesian Network 

Teh Raihana Nazirah Roslan ${ }^{1 *}$ and Chee Keong Ch'ng ${ }^{2}$<br>${ }^{1}$ Othman Yeop Abdullah Graduate School of Business, Universiti Utara Malaysia, 50300 Kuala Lumpur, Malaysia<br>${ }^{2}$ Department of Decision Sciences, School of Quantitative Sciences, Universiti Utara Malaysia, 06010 UUM<br>Sintok, Kedah, Malaysia


#### Abstract

In moving towards Industrial Revolution 4.0, healthcare and medicine are one of the biggest areas of concern which is beneficial to maintaining healthy living. This study seeks to identify the potential problems and risks related to high-technology medical approaches, namely the da Vinci robotic surgical systems, specifically used for thyroidectomy surgery. In particular, the risks embedded in robotic surgeries in terms of health and economy are investigated. Furthermore, a probabilistic risk analysis was conducted to assess the risk among surgeons of the da Vinci robotic surgery using event tree analysis and Bayesian network. This research revealed that the probability of success for surgeons without prior robotic surgery experience was 0.10 . It highlights the importance of proper training for medical practitioners in handling advanced medical equipment by considering the related risk involved in patients.


Keywords: Bayes' theorem, event tree analysis, healthcare, high technology medical, probabilistic risk analysis, robotic surgery, thyroid surgery

## ARTICLE INFO

## Article history:

Received: 21 November 2021
Accepted: 11 March 2022
Published: 23 September 2022

## DOI: https://doi.org/10.47836/pjst.30.4.27

E-mail addresess:
raihana@uum.edu.my (Teh Raihana Nazirah Roslan) chee@uum.edu.my (Chee Keong Ch'ng)
*Corresponding author

## INTRODUCTION

Healthcare and medicine are among the priority areas affected by the current wave of Industrial Revolution 4.0. Some applications in these areas involve surgical instruments, clinical devices, implants, and healthcare equipment such as telemedicine and robotic surgery. Consequently, conventional surgery methods often produce traumatic effects in patients posed a high risk in a large wound,

and longer recovery time will be improved. The robotics application implemented in the medical field assisted the human in terms of helping doctors to perform the complicated task such as conducting surgery on the patient in the operation theatre, which required a long duration of time, deep focus, accuracy, and other activities that the doctors' ability cannot do. The robotic surgery system in healthcare is an advanced development in the surgical area. This great system has been approved to be applied and implemented in treating diseases requiring surgeries.

The most pronounced development is in robotic surgery (Talib, 2017). The only robotic system that is most widely used in procedures of surgical, especially for application in laparoscopic procedures, urological procedures, and mitral valve repair surgery, that has been approved by the Food and Drug Administration (FDA), is the robotic system of da Vinci Surgical System (Ng \& Tam, 2014). This type of surgery can reduce pain and discomfort, and among the popular ones is the thyroidectomy surgery conducted through the da Vinci robotic surgical system (Park et al., 2015). The da Vinci System has been widely used worldwide for robotic colorectal surgeries since then (Zakaria et al., 2018).

The da Vinci surgical system refers to the surgery system of the thyroid gland, which involves teleoperating, as shown in Figure 1. The doctors would control a surgical robot comfortably, where the robot's arms would follow da Vinci motions with tools and an endoscope for surgery (Olanrewaju et al., 2013). This system involves three components: a surgeon's console, a patient-side robotic cart including four robotic arms handled by the surgeon, and a 3D high-dimensional vision system ( Ng \& Tam, 2014). This procedure was safer and feasible compared to traditional open surgery. The duration of such surgery would also be shortened (Park et al., 2015). Moreover, compared robotic versus conventional laparoscopic colorectal surgery, it was found that the robotic approach was as safe and feasible as a conventional one, although it involved higher costs ( Ng \& Tam, 2014). DeSouza et al. (2010) also claimed that robotic procedure took longer surgery times and greater costs but was found safer and feasible. Ng and Tam (2014) highlighted that robotic surgery improved visualization and enhancement of the images involved with the shorter learning curve and improved musculoskeletal strain to surgeons. Therefore, the application of robotic surgery in thyroidectomy can overcome the traditional thyroid surgery approach's flaws in shortening the learning curve. Here, the learning curve refers to analyzing an individual's stage and total operation time (Park et al., 2015).

Before undergoing robotic thyroidectomy surgery, surgeons must completely understand the thyroid gland's anatomy and the lymph node compartments. Next, surgeons must know how to describe the overall process of thyroidectomy in detail. Then, surgeons will be trained in robotic thyroidectomy for 6 to 12 months. Finally, they can conduct robotic thyroidectomy independently monitored by supervising consultants (Park et al., 2015).

![img-0.jpeg](img-0.jpeg)

Figure 1. The da Vinci robotic surgery system

In this article, we will assess the risks involved among surgeons when using robotic thyroidectomy surgery using probabilistic risk analysis through the Bayesian network. Zoullouti et al. (2019) successfully utilized a Bayesian approach to healthcare management to investigate the probability of success for surgeons based on previous surgery experiences.

# METHODOLOGY 

## Risk Management in Healthcare

Risk management for healthcare can be defined as identifying, assessing, and mitigating the possible risks to health institutions' visitors, staff, and assets that require organization. Risk management in its best form may be proactive in identifying and managing the risks. However, if an incident happens after the event handling, it should still be tackled in line with the risk management principles outlined in Figure 2 (Alam, 2016).
![img-1.jpeg](img-1.jpeg)

Figure 2. Steps of risk management in healthcare

Five steps are involved in the risk management process, starting by establishing the context. In healthcare risk management, context is crucial. There are many high-priority areas in the hospital, such as ICU (Intensive care unit), O.R. (Operation room), and E.R. (Emergency room), together with other miscellaneous functions related to patients' care. The second step is the identification of risk. This process involves awareness among healthcare professionals and staff on health care services. The third step is analyzing the risks involved. The need to analyze the risk was to develop and understand the risk when it is identified. The fourth step involves evaluating the risk, where underlying causes of the risk, emergency arrangements, and healthcare training are brainstormed and evaluated. The evaluation of risk is divided into two; to accept the risk or to treat the risk. The final step involves treating risk, normally consisting of three methods: controlling, transferring, and avoiding risk. The risk treatment plan should be able to propose actions, mobilizes resources, and establish a timeframe for undertaken actions (Agency for Healthcare Research and Quality, 2013).

The risk management of healthcare was very important to determine and eliminate all the risks. Because predominantly, the underlying causes of medical errors are recognized as communication problems, inadequate information flow, human-related problems, organizational transfer of knowledge, staffing patterns and workflow, inadequate policies and procedures, and technical failures (Agency for Healthcare Research and Quality, 2013).

# Sources of Data 

Park et al. (2015) obtained the data from a secondary source. This data consists of 125 patients who went for robotic thyroid surgery by two trained surgeons. Before the robotic thyroidectomy, Surgeon 1 had experienced 47 open conventional thyroidectomy surgeries but no experience in endoscopic thyroidectomy or robotic surgery. Meanwhile, Surgeon 2 had more than 200 experiences in open conventional thyroidectomy surgery and five experiences in endoscopic thyroidectomy surgery or robotic surgery. Table 1 illustrates the data that will be used in this project. For this study, data for Surgeon 2 is only for display purposes since our target is Surgeon 1 without former robotic surgery experiences.

From Table 1, 5 variables (age, sex, body mass index (BMI), the extent of surgery, and operation time) were considered. Total operation time was defined as from the first incision to completion of skin closure, which includes docking and undocking robots. Besides that, the learning curve was analyzed by individual-level time and overall operation time. The learning curve was described as the increased performance and experience with time, increasing productivity. The extent of surgery was divided into three groups of surgery. The first surgery group was less than total thyroidectomy, meaning that the surgery group did not involve thyroid patients. Total thyroidectomy was the second surgery group involving only thyroid patients. The third surgery group, total thyroidectomy + MRND, was the

Table 1
Data of patient demographics, extent of surgery, and operation time


Source. The robotic thyroidectomy learning curve for beginning surgeons with little or no experience of endoscopic surgery (Park et al., 2015)
surgery of patients with thyroid disease and other diseases or symptoms found during the surgery. Here, MRND means Modified Radical Neck Dissection. The operation time was defined in minutes. We calculate the total time of each operation using Equation 1:

$$
\sum x=\mu \times n
$$

where $\mu$ represents the mean value, $x$ is the total operation time, and $n$ is the sample size.
The mean value for less than total thyroidectomy was 100.8 , and the sample $n$ was 113 . These values gave us Equation 2:

$$
\begin{aligned}
& \frac{\sum x}{113}=100.8 \\
& \sum x=11390.4
\end{aligned}
$$

The total operation time for 113 patients was 11390.4 minutes. Besides that, for total thyroidectomy with the mean value of 134.2 and $n=9$, we obtain Equation 3 :

$$
\begin{aligned}
& \frac{\sum x}{9}=134.2 \\
& \sum x=1207.8
\end{aligned}
$$

Thus, the total operation time for nine patients was 1207.8 minutes. Besides, the calculation for total thyroidectomy $+M R N D$ was repeated as above, using the mean of 284.7 and $n=3$ in Equation 4:

$$
\begin{aligned}
& \frac{\sum x}{3}=284.7 \\
& \sum x=854.1
\end{aligned}
$$

Here, the total operation time for three patients was 854.1 minutes.
Appendix A shows the framework of robotic healthcare, where successful robotic surgery requires details of operation time and extent of surgery. The surgery was considered successful when the robotic surgery's operation time was less than the history data or the duration of the surgery without using robots. It also means that robotic surgery is more advantageous than conventional surgery. For example, robotic thyroidectomy eliminated the need for anterior neck incision for patients, resulting in reduced pain and swallowing discomfort compared to conventional thyroidectomy (Lee et al., 2010). Perez and Schwautzberg (2019) mentioned that the increased cost of robotic surgery was partly due to the high cost of fixed equipment. Robotic surgery could be cost-effective if these fixed costs were spread to a higher volume. Weaver and Steele (2016) stated that the learning curve, particularly for trained laparoscopic surgeons, is expected to be shorter than conventional laparoscopic surgery as robots are meant to be more intuitive than laparoscopy, although the curve is still lengthy and profound. Besides that, Mattos (2016) said that robots would enable more accurate and safer operations by increasing surgeons' agility, control, and accuracy.

# Event Tree Analysis 

Spouge (1999) proposed event tree analysis (ETA) as an inductive procedure that shows all possible outcomes of an accident, normally based on two major assumptions. First, the likelihood of events or basic events is assumed to be exact and precisely known. Second, interdependencies of events or basic events are assumed, independent. These assumptions are understandably not always true. There were situations when some inherent uncertainties were available in data collection and defining the relationships of events or basic events (Sadiq et al., 2008). Sometimes, the events surrounding trees may depend on one another (Ferson, 2004). In this article, a predictive approach was applied where the number of

accidental events $X$ in some specified operations was focused. A link $g$ between $X$ and observables on a more detailed system level was established and denoted in $Z=\left(Z_{1}, Z_{2}, \ldots\right.$ $\left.Z_{\mathrm{m}}\right)$. The number of hazardous situations of a certain type occurring during some operations was indicated as $Z_{\mathrm{i}} .1$ was denoted as specific safety barrier fails, while 0 otherwise-for example, the model given in Figure 3 consists of $Z_{1}, Z_{2}$, and $Z_{3}$. The number of hazardous situations to occur refers to $Z_{1}$, while $Z_{2}$ indicates 1 if the first safety barrier fails and 0 otherwise. Next, $Z_{3}$ is equal to 1 if the second safety barrier fails and 0 otherwise (Aven \& Eidesen, 2007).
![img-2.jpeg](img-2.jpeg)

Figure 3. An event tree

$$
X=\mathrm{g}(Z)=Z_{1} \cdot Z_{2} \cdot Z_{3}, \text { as } X \text { is given by }
$$

the number of hazardous situations where both safety barriers fail.

# Bayesian Network 

The applications of Bayesian are already found in a wide range of activities, including in sciences, engineering, medicine, sport, and others. Lately, a Bayesian network strategy has started to be utilized in designing applications. A Bayesian network is a graphical induction method to communicate the causal connections among factors. Bayesian networks are utilized either to anticipate the likelihood of obscure factors or to refresh the likelihood of realized factors given the specific condition of different factors through the course of likelihood spread or thinking. The modeling depends on Bayes' theorem. Because of this capacity, Bayesian networks have given a promising structure to a framework for security investigation and hazard the executives. Bayesian networks are progressively utilized for the development of framework unwavering quality models, hazard the executives, and wellbeing examination considering probabilistic and dubious information. Like fault trees, Bayesian networks comprise both subjective and quantitative parts.

Many researchers have examined various methods in mishap situation examination, not many of whom have involved Bayesian networks. Sklet (2004) subjectively looked at a few ordinarily utilized techniques, for example, fault tree examination, occasion tree investigation, and hindrance examination for mishap investigation. The examination was made in view of standards, for example, graphical portrayal and the capacity to help security boundaries. Nivolianitou et al. (2004) utilized fault tree, occasion tree, and Petri nets for a subjective mishap situation examination in an alkali stockpiling plant, reasoning that Petri nets can fuse the proof through situation investigation and consequently are more fitting for dynamic mishap investigation. Zheng and Liu (2009) made a correlation

among a few broadly involved strategies for mishap anticipating. Although fault tree as a situation examination strategy and Bayesian networks were momentarily talked about, the principal center in their exploration was given to techniques, for example, relapse models, time-series techniques, and neural organizations.

Additionally, Simon et al. (2007) gave a comprehensive factual survey of Bayesian network application in various regions like gambling and upkeep investigation, in which Bayesian network was subjectively contrasted and different techniques, for example, fault trees, Markov chains, and Petri nets. The current work is pointed toward showing the equals among fault trees and Bayesian networks in the particular area of mishap displaying and process security examination, which has not been concentrated on so far. The paper additionally examines the demonstrating potential presented by Bayesian networks, making them a better technique looked at than fault trees for dynamic security investigation.

According to Oppermann (2018), in finance, the Bayes' theorem can be used to rate the risk of lending money to potential borrowers. In the healthcare field, the Bayesian network can be used to determine the accuracy of medical test results by taking into consideration how likely any given person is to have a disease and the general accuracy of the test. In this work, we will find the probability of total thyroidectomy $+M R N D$ occurring, given that the event of total thyroidectomy $+M R N D$ for Surgeon 1 had occurred. The general formula for Bayes' theorem is as Equation 5:

$$
P(A \mid B)=\frac{P(B \mid A) P(A)}{P(B)}
$$

where
$P(A \mid B)=$ the probabilty of event A occuring, given event B has occured
$P(B \mid A)=$ the probabilty of event $B$ occuring, given event $A$ has occured
$P(A)=$ the probabilty of event A
$P(B)=$ the probabilty of event $B$

# RESULTS AND DISCUSSION 

In assessing the risks, all aspects of the event need to be identified to improve the field of robotic thyroidectomy surgery. Therefore, we begin with the posed risks, followed by the assessment through event tree analysis and the Bayesian network for probabilistic risk analysis. In this era of globalization, the government has introduced many new technologies in the field of healthcare to provide greater efficiency in services.

## Health Risk

The health risk is the health consequence of a specific disease or condition. The robotic surgery impacted the precise dissection in a confined space and reduced in blood loss of the

patients. The other complications after surgery, like lower transfusion rates and death rates in the hospital, can be reduced through the robotic surgery approach. Moreover, a shorter learning curve can be achieved ( $\mathrm{Ng} \&$ Tam, 2014). This approach's noticeable drawback is the speed of transferring information from the operator to the robot and the lag time from operator to execution involving surgeon and patient in a different location (Olanrewaju, 2013). The difficult robotic surgery procedures can be done quickly as in open surgery by competent surgeons and nurses. The operating time was sped up with the help of a regular assistant-the surgical training for robotic surgery using VR simulators in the operating room limit the operative time. However, the acceleration of the learning curve in real robotic surgery does not directly imply the improvement of da Vinci's performance. Using the VR simulation of the robotic surgery tasks performed by the trainee, less psychomotor stress and actively manipulated clutch and camera pedals of the robotic system were improved (Cho et al., 2013). However, this surgery could be smoothly conducted when surgery team members became familiar and comfortable with the procedures (Sahabudin, 2006).

# Economic Risk 

The economic risk involved is the high cost of the da Vinci robotic thyroidectomy apparatus, but this risk could become cost-effective when the employability rate of such an approach is high (Park et al., 2015). Even though the current costs are high, the wider dissemination of this technology and the increase in competition from manufacturers may drive the costs down ( $\mathrm{Ng} \&$ Tam, 2014). This issue is also related to the training needed for surgeons in the operating room (Cho et al., 2013). Training for the trainees to conduct robotic surgery is essential, specifically in suturing techniques. A short course is insufficient for those who do not have laparoscopic experience (Sahabudin, 2006).

Moreover, financial limitations are found in applying the da Vinci robotic surgery system. The cost involved in using robotic surgery is a higher burden in terms of limited availability, cost, and the learning curve of robotic surgery. Since the da Vinci robotic surgery system applied proprietary software, which physicians cannot modify, there is no freedom for users to modify the standard operating system. The jobs that relate to intellectual capitalism, creativity, imagination, leadership, analysis, humor, common sense, screen or script-writing, and scientific endeavors will be volatile against the technological revolution. Another risk of this technology is that it might be able to replace labor tasks and roles, reducing human function that may leading to unemployment (Zakaria, 2018).

## Event Tree Analysis

In this section, we establish the links between the parameters used based on the operation time in surgery using robotic thyroidectomy. Event tree analysis is a model used to show

logical numbers for failure and success from a population or individual (Freeman, 2022). The general event tree in this study is as follows:
![img-3.jpeg](img-3.jpeg)

Figure 4. The general event tree

Figure 4 portrays the possible pathways of this study. We assess the total thyroidectomy + MRND as $Y=2$ when both events succeed, total thyroidectomy as $Y=1$ when one event gains success and the other does not occur, and less than total thyroidectomy as $Y=0$, which is a failure or does not achieve their total operation time. To perform the event tree analysis, we need to perform the following steps:

Step 1: The system needs to be defined by stating the variables involved.

Total thyroidectomy + MRND, total thyroidectomy, and less than total thyroidectomy

Step 2: The accident scenarios were identified by performing a system assessment for each event.
$\mathrm{Y}=2$ (total thyroidectomy occurs, and MRND occurs)
$\mathrm{Y}=1$ (total thyroidectomy occurs, and MRND does not occur
$\mathrm{Y}=0$ (less than total thyroidectomy)

Step 3: Define the initiating event by using the main sources of events.
Operation time of robotic thyroidectomy surgeries for population

Step 4: Identify Events A and B, either failure or success.
Event $\mathrm{A}=$ total thyroidectomy
Event B $=$ MRND

Step 5: Calculate the overall probability for each path.

Based on the data in Table 1, the total operation time of the overall event was 13452.3 minutes. It was obtained by summing up the operation time for total thyroidectomy + MRND, which was 854.1 minutes, total thyroidectomy, which was 1207.80 minutes, and less than total thyroidectomy was 11390.40 minutes, respectively. Therefore, to calculate the probability of each event occurring, we need to use every event's minute, then divide by overall minute by a population of all events, as shown in Equation 6.

$$
\begin{aligned}
& P(\text { Total Thyroidectomy }+M R N D)=\frac{854.1 \text { minutes }}{13452.3 \text { minutes }}=0.0635 \\
& P(\text { Total Thyroidectomy })=\frac{1207.80 \text { minutes }}{13452.3 \text { minutes }}=0.0897 \\
& P(\text { Less than Total Thyroidectomy })=\frac{11390.40 \text { minutes }}{13452.3 \text { minutes }}=0.8467
\end{aligned}
$$

![img-4.jpeg](img-4.jpeg)

Figure 5. Event tree analysis in robotic thyroidectomy

When Events A and B succeed or take place, we choose $\theta=2$. Meanwhile, when one event occurs, and the other event does not occur, we state $\theta=1$. Finally, if Events A and B did not occur, we set $\theta=0$.

From Figure 5, it can be observed that the condition for total thyroidectomy occurring in Event A and MRND occurring in Event B implies that Event A and Event B also took place. Here, the value is 0.0635 for $\theta=2$. For the case when Event A did not occur, it would be considered $\theta=0$ and recognized as less than total thyroidectomy with a value of 0.8467 . The last event was when Event A occurred, but Event B did not occur; here, $\theta$ was denoted as 1 . This event was for the surgery population in robotic thyroidectomy if total thyroidectomy occurred, in which the surgery was just for thyroid but not for MRND. The value calculated was 0.0897 .

# Bayesian Network 

The Bayesian network allows combining prior information about population parameters with evidence from the information contained in the sample to guide the statistical inference process (Gleason \& Harris, 2019). This method allows us to integrate information from historical data and the parameters of the population undergoing thyroid surgery. The information from the past population is defined as the prior distribution for thyroidectomy surgery using robotics. We call the information from the past population the prior distribution for Thyroidectomy Surgery using Robotic for IR 4.0. In this study, all surgeons showed success in handling robotic surgery. Therefore, we assumed that the experience from Surgeon 1 would give a positive response mean a positive result to a person who undergoes thyroidectomy surgery. We later look at the angle from which operation time for a surgeon that successfully performed this operation using the same steps as the previous history.

Based on Table 1, when Surgeon 1 performs total thyroidectomy for Event A but at the same time Event B, which is MRND occurred, the value for this situation was 468.2

times. On the other hand, if Surgeon 1 performs only Event A (total thyroidectomy), and the patient was not required to undergo surgery for MRND (Event B), the value obtained was 193. Lastly, when Surgeon 1 was performing the less than total thyroidectomy surgery, the value was 6912 operation time. All these values can be written using conditional probabilities as Equations 7 and 8:
(MRND (by surgeon 1) $\cap$ Total Thyroidectomy $)=468.2$
(Surgeon $1 \cap$ Total Thyroidectomy $)=193$
(Surgeon $1 \cap$ Less than Total Thyroidectomy) $=6912$
We used the results for each event as follows:

$$
P(B \mid A)=\frac{P(B \cap A)}{P(A)}
$$

(MRND (by surgeon 1) $\cap$ Total Thyroidectomy $)=468.2$
(MRND (by surgeon 1) $\cap$ Total Thyroidectomy $)=468.2$

$$
\begin{aligned}
& P(\text { MRND Operation time By surgeon } 1 \mid \text { Total Thyroidectomy }+ \text { MRND })=\frac{468.2}{854.1}=0.54818 \\
& P(\text { Operation time By surgeon } 1 \mid \text { Total Thyroidectomy })=\frac{193}{1207.80}=0.1598 \\
& P(\text { Operation time By surgeon } 1 \mid \text { Less than Total Thyroidectomy })=\frac{6912}{11390.40}=0.6068
\end{aligned}
$$

By using the
$P($ MRND Operation time By surgeon $1 \mid$ Total Thyroidectomy + MRND $)=$
$P(X=1 \mid \theta=2)=0.54818$
$P($ Operation time By surgeon $1 \mid$ Total Thyroidectomy $)=P(X=1 \mid \theta=1)=0.1598$
$P($ Operation time By surgeon 1|Less than Total Thyroidectomy $)=$
$P(X=1 \mid \theta=1)=0.6068$
By combining data on the history and experience of Surgeon 1 (Equation 9), we can compute the posterior probability for the probability of patients having Total Thyroidectomy $+M R N D$ undergoing surgery by Surgeon 1, denoted as $P(\theta=2 \mid X=1)$.
To achieve this, first, we calculate $P(X=1)$ in Equation 10:

$$
\begin{aligned}
& P(X=1)=P(X=1 \mid \theta=2) P(\theta=2)+P(X=1 \mid \theta=1) P(\theta=1) \\
& P(X=1 \mid \theta=0) P(\theta=0) \\
& P(X=1)=0.54818(0.0635)+(0.1598)(0.0898)+(0.6068)(0.8467) \\
& =(0.03481)+(0.01435)+(0.51378)=0.56294
\end{aligned}
$$

Here, $P(X=1)$ means the operation time performed by Surgeon 1. By using historical data $P(X=1 \mid \theta=2)=0.54818$.

$$
P(\theta=2 \mid X=1)=\frac{P(X=1 \mid \theta=2) P(\theta=2)}{P(X=1)}=\frac{(0.54818)(0.0635)}{0.56294}=0.10
$$

The result for posterior distribution when using the Bayes' Theorem Analysis was 0.10 (Equation 11). This result shows that the probability of success by Surgeon 1 when performing Total Thyroidectomy + MRND surgery was 0.10 . Therefore, based on the history data in Park et al. (2015), Surgeon 1 did not have experience handling robotic surgery, and his success probability in this operation was 0.10 .

# CONCLUSION 

In this study, we used event tree analysis and the Bayesian network to show probability of the learning curve (operation time) for Surgeon 1 handling the Total Thyroidectomy + MRND surgery. This approach can be applied to other robotic or technological equipment that requires large funding for a better understanding of the said innovation. Although expensive, the government should consider investing in this technology as it reflects more advantages, such as reducing the potential of unnecessary risk of injuries in normal surgery. Furthermore, constructive strategies should be developed to provide necessary training tools for surgeons with minimal training costs. This type of technology will be potential in the future, where its adoption will produce safe and efficient procedures with minimal damage. Patients will also reduce hospitalization; thus, the bed occupancy in major hospitals can be reduced to cater to more emergency matters.

## ACKNOWLEDGEMENT

This research was self-supported by the authors.
