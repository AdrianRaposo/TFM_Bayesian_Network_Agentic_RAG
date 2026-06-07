# Dynamic risk assessment in healthcare based on Bayesian approach 

Li Mei ${ }^{\mathrm{a}, *}$, Liu Zixian ${ }^{\mathrm{a}}$, Li Xiaopeng ${ }^{\mathrm{a}}$, Liu Yiliu ${ }^{\mathrm{b}}$<br>${ }^{a}$ College of Management and Economics, Tianjin University, Tianjin, China<br>${ }^{\mathrm{b}}$ Department of Mechanical and Industrial Engineering, Norwegian University of<br>Science and Technology, Trondheim, Norway<br>*Corresponding author e-mail address: $\operatorname{lm} 314835237 @ 163 . \mathrm{com}$


#### Abstract

Risks related with healthcare are always dynamic, and they are affected by situations of patients, human errors in treatment and even the states of medical devices. This paper proposes a dynamic medical risk assessment model, for capturing the impacts of factors on the occurrence of adverse events. In this model, a static fault tree is established to show risk scenarios. Dynamic Bayesian network and Bayesian inference are introduced to analyze the operations of medical devices, in consideration of their failures, repairs, and human errors over time. Hemodialysis infection is taken as the case to verify that the proposed method is helpful to demonstrate the changes of medical risks with time, and to identify the critical events contributing to the occurrence of the adverse event at different moments. These findings can act as the basis to assign and adjust safety measures.


Keywords: Medical risk; Dynamic risk assessment; Dynamic Bayesian network; Bayesian inference; Probability updating

## 1. Introduction

Medical risks refer to the probability of an adverse event during a particular treatment process, and they impact on patient safety and overall healthcare system, in

considering possible high medical costs, and wastage of medical resources. Medical risks can come from biological properties of patients, like age, gender and comorbidity, and they can be from those iatrogenic factors, such as device failures and human errors. Medical risks have received more attentions recently, after the publication of the report titled "To err is human: building a safer health system" by the Institute of Medicine (IOM) in 1999. The report has indicated that identification and control of iatrogenic factors are the most effective way of reducing medical risks [1]. When such iatrogenic risks can be revealed proactively, the critical events in a healthcare system are determined, safety measures can be implemented effectively.

# 1.1. Risk assessment in healthcare 

Probabilistic risk analysis (PRA) has been introduced to assess medical risks. Among them, fault tree analysis (FTA) has been a common-accepted approach due to its ability for modeling risk scenario by illustrating relationships between an adverse event and the possible causes. Ekaette et al. have applied FTA in radiation treatment risk assessment [2], as well as Komal has evaluated risk of medication delivery and inpatient transfers with fuzzy FTA [3].

However, fault tree models have long been in the debate because of their weakness in representing the dependencies of events explicitly, analyzing multi-state variables, updating probabilities, and coping with uncertainties [4,5]. Bayesian network (BN) has gained more focuses recently, because it can release aforementioned limitations to some extent $[6,7]$, with the strong capability in predictive and diagnostic analysis. Maglogiannis et al have introduced BN in healthcare to assess the risk of medical

information system [8]. Nevertheless, conventional BN can only represent relationships between variables at a particular time point or during a specific period of time, and it does not reflect temporal relationships between different times.

# 1.2. The dynamic nature of medical risk 

It is noticeable that medical risks always evolve with time due to the dynamic natures of their impact factors in a healthcare process [9]. Here we consider medical workers and medical devices:

Behaviors of humans are full of uncertainties, and the probabilities of human errors are changing due to the ever-changing environment. It is reported, however, that probabilities of human errors are usually quantified as constant values while keeping same at different times $[10,11]$. However, it is possible to know the number of occurrences of a human error during a certain period of time, which can be used to conduct probability updating by Bayesian inference. Bayesian inference provides a mathematical framework for updating prior knowledge by integrating new data and information.

On the other hand, the performance of a medical device, affected by its age and usage intensity, can degrade over time. Compared with human errors, medical devices are of high reliability and failures seldom occur [12]. Therefore, Bayesian inference is not suitable for probability updating of device failures. When the device has a failure, a repair is needed to restore the failure. To model such behaviors, dynamic Bayesian network (DBN) can be introduced. This method is able to demonstrate the changes over time and relationships between the current state of a device and its past or future states

[13]. To our knowledge, there have been no specific studies of dynamic Bayesian network and Bayesian inference in risk assessment for device failures and human errors in healthcare.

Based on a fault tree to model medical risk scenario, the purpose of this study is to embed Bayesian approaches into the fault tree for dynamic medical risk assessment. Hemodialysis infection is involved as a case study due to its high incidence, and it is the main cause leading to the death of hemodialysis patients [14,15]. The proposed method includes two parts: (1) the qualitative and static analysis where risk identification of hemodialysis infection is carried out with the help of conventional FTA, (2) the quantitative and dynamic analysis in which probability updating is conducted using the dynamic Bayesian network and Bayesian inference to demonstrate risk profile over time. Additionally, critical events contributing to the occurrence of hemodialysis infection are identified using the ratio of variation (RoV). The rest of the paper is structured as follows: section 2 gives a brief introduction to dynamic Bayesian network and Bayesian inference; section 3 demonstrates the dynamic risk assessment model; section 4 is the case study followed by conclusions in section 5 .

# 2. Dynamic Bayesian network 

A Bayesian network consists of qualitative and quantitative parts. The qualitative part is a directed acyclic graph, including a set of nodes representing the system variables and a set of directed arcs representing the dependencies or the cause-effect relationships among the variables. The quantitative part is conditional probability tables (CPTs), which stand for conditional dependencies between nodes and their parents [16].

![img-0.jpeg](img-0.jpeg)

Fig. 1 A simple dynamic Bayesian network

As an extension of ordinary BN, DBN facilitates explicit modeling of temporal evolution for a set of random variables over a discretized timeline [13]. Assume that a timeline T is divided into several time-slices and the time interval is $\Delta t$. Each timeslice stands for a unit time which can be one day, one month or one year. So, a DBN can be defined as a pair $\left(B^{1}, B^{\rightarrow}\right)$ over the timeline, where $B^{1}$ is a static BN at $t=0$, and $B^{\rightarrow}$ is a two-slice temporal BN which defines:

$$
P\left(X^{t+\Delta t} \mid X^{t}\right)=\prod_{i=1}^{n} P\left(X_{i}^{t+\Delta t} \mid P a\left(X_{i}^{t+\Delta t}\right)\right)
$$

Then, the joint probability distribution of the variables at time $t$ can be represented as:

$$
P\left(U^{t+\Delta t}\right)=P\left(X_{1}^{t+\Delta t}, X_{2}^{t+\Delta t}, \cdots, X_{n}^{t+\Delta t}\right)=\prod_{i=1}^{n} P\left(X_{i}^{t+\Delta t} \mid X_{i}^{t}, P a\left(X_{i}^{t}\right), P a\left(X_{i}^{t+\Delta t}\right)\right)
$$

where $X_{i}^{t}$ and $X_{i}^{t+\Delta t}$ are different states of $X_{i}$ in two consecutive time-slices, $P a\left(X_{i}^{t}\right)$ and $P a\left(X_{i}^{t+\Delta t}\right)$ are parent sets of $X_{i}$ at these two time-slices, respectively.

A simple DBN is shown in Fig. 1, where a similar BN is duplicated twice with variables of different values. Moreover, the two types of arcs show the relationships between variables, including intra-slice arcs which represent the relationships in a timeslice (denoted by solid arrows) and inter-slice arcs, representing the relationships between successive time-slices (denoted by dotted arrows).

DBNs can update the values of probability with Bayesian inference, which is a

key element to dynamic risk assessment [17]. Considering $\theta$ as a parameter, and $\pi_{0}(\theta)$ as the probability distribution function (prior distribution) of $\theta$. New data about $\theta$ is used to form the likelihood function $f(x \mid \theta)$. Then, Bayesian inference can be employed to yield the posterior distribution $\pi_{1}(\theta \mid x)$ as shown in the following equation $[18]:$

$$
\pi_{1}(\theta \mid x) \propto f(x \mid \theta) \pi_{0}(\theta)
$$

# 3. Dynamic risk assessment model for hemodialysis infection 

In this section, the qualitative part of our proposed model is described first, in which an adverse event and its possible causes are identified using conventional FTA. Then, the quantitative part introduces dynamic Bayesian network and Bayesian inference for probability updating of device failures and human errors, respectively. After that, the occurrence probability of the adverse event can be evaluated and the critical events will be identified. We take the hemodialysis infection as a case here to describe how the analysis should be conducted for healthcare activities.

Hemodialysis removes metabolic wastes and supplements bases through diffusion between blood and dialysate. With the continuous development and extensive applications of the technology, hemodialysis has been proved to be one of the most effective treatments for patients with end-stage renal disease (ESRD), which can increase the life span of patients. Even so, hemodialysis has a high level of risk due to a variety of influencing factors in the process. The process of hemodialysis is illustrated in Fig. 2 [19,20]. Specifically, nurses cannulate the vascular access, and connect them to electronically controlled dialysis machines. Sophisticated equipment purifies the

water for blending dialysate. Dialyzers are reprocessed and sterilized before they are delivered to the nurse for setting up the dialysis equipment. Nurses should take care of patients responsibly during the hemodialysis, but hazardous events are inclined to occur in so many interactions between dialysis staff, machines, and the environment [21]. Recently, the number of ESRD patients who receive hemodialysis is rapidly increasing because of the aging population and prevalence of diabetes and hypertension [22,23]. Due to sharing of dialysis machines and close contact among patients in dialysis units, the rate of infections acquisition of hemodialysis patients is significantly higher than general population [15,24]. Consequently, risk assessment for hemodialysis infection is to be urgently settled before serving the patients.

# 3.1. Fault tree analysis for hemodialysis infection 

Fault tree analysis is a diagram which connect potential adverse event (that is a top event) with its possible causes (intermediate events and basic events) using Boolean logic where "AND" and "OR" are two basic types. Here we describe the "hemodialysis infection" as the top event (TOP) and causes of the top event mainly come from three stages of hemodialysis as shown in Fig. 2. Thus, "infection in preparation $\left(G_{1}\right)$ ", "infection during hemodialysis $\left(G_{2}\right)$ " and "infection after hemodialysis $\left(G_{3}\right)$ " are connected with "hemodialysis infection (TOP)" using an "OR" gate. According to expert suggestions and related literature, 23 possible basic events in the hemodialysis process are identified. The whole fault tree is constructed accordingly and shown in Fig. $3[25,26,27]$. The descriptions of symbols in the fault tree are listed in Table 1.

![img-1.jpeg](img-1.jpeg)

**Fig. 2** The process of hemodialysis

![img-2.jpeg](img-2.jpeg)

**Fig. 3** Fault tree for hemodialysis infection

Table 1 Descriptions of events in fault tree for hemodialysis


# 3.2. Device failure probability updating with DBN 

DBN is employed to show the state transition of a device at different times, and to calculate its corresponding failure probability. For a device $i, X_{i}^{t}$ represents the failure probability at time $t$. The dynamic Bayesian network for $i$ is depicted in Fig. 4.
![img-3.jpeg](img-3.jpeg)

Fig. 4 Dynamic Bayesian network for medical device $i$

FTA assumes two states for each event, meaning that a device is either in its perfect functioning state $\left(X_{i}=0\right)$ or failed state $\left(X_{i}=1\right)$. In fact, it is a gradual process from $X_{i}=0$ to $X_{i}=1$ where many intermediate states exist between these two extreme states. For example, dialyzer can still normally operate for a period, even if it is a little wear out. The current paper assumes that for device failure events, each basic event has three states, namely $X_{i}=1, X_{i}=0.5$, and $X_{i}=0$, whereas every intermediate event still has two states in order to simplify calculation. The state $X_{i}=0.5$ refers to a degraded state between state $X_{i}=0$ and $X_{i}=1$.

At the beginning of a timeline $(t=0)$, each device is in its state $X_{i}=0$. With the passage of time, it can either go to the degraded state $\left(X_{i}=0.5\right)$ or the failed state $\left(X_{i}=1\right)$, while all failure rates are assumed to be exponentially distributed. When a failure occurs $\left(X_{i}=1\right)$, the device will no longer function continually, and repair is required. The state after the repair depends on the degree of repair that can be a perfect repair or an imperfect repair. The device can go to state " 0 " with perfect repair, or it can go to state " 0.5 " as well as " 0 " when performing imperfect repair. The repair rates also follow exponential distribution. The state transition of a device in dynamic Bayesian network

is shown in Fig. 5. The above symbols of the arcs are indicated as failure rates $\lambda_{i}(i=$ $1,2,3)$ and repair rates $\mu_{j}(j=1,2)$ between states, respectively.
![img-4.jpeg](img-4.jpeg)

Fig. 5 State transition diagram for medical device

Assume that the current time is $t$, and the time interval is $\Delta t$, then the transition relationships of medical devices between two consecutive time-slices without repairs, with imperfect repairs, and with perfect repairs are given in Table 2-4, respectively [28]. Notably, the selection of $\Delta t$ deserves consideration. For a given time period, risk variations may not be apparent under short $\Delta t$ while a long $\Delta t$ is prone to overlook some crucial information. Thus, a reasonable $\Delta t$ should be determined carefully considering factors such as assessment cycle, observation period etc.

Table 2 Transition relationships between consecutive time-slices without repairs


Table 3 Transition relationships between consecutive time-slices with imperfect repairs


Table 4 Transition relationships between consecutive time-slices with perfect repairs


# 3.3. Human error probability updating with Bayesian inference 

Bayesian inference is adopted to handle the dynamics of human errors. All human error events, both basic and intermediate, are assumed to involve two states since a human error just occurs or not. The difficulty of Bayesian inference is forming the likelihood function $f(x \mid \theta)$ using new data. Accident precursor data (APD) has been widely used to construct likelihood function which in turn updates the prior knowledge to yield the posterior distribution. APD is defined as the number of occurrences of the events which are not characterized as adverse events but indicate the increasing occurrence probability of an adverse event [29,30]. In healthcare, the number of occurrences of a human error can be regarded as APD. Considering $P_{i}$ as the prior probability of a human error $X_{i}$, which needs to be updated, $f$ is the number of occurrences of $X_{i}$ in $n$ patients during a time interval, then $f$ follows a binomial distribution as follows [31]:

$$
P\left(X_{i}=f\right)=f\left(A P D \mid P_{i}\right)=P_{i}^{f}\left(1-P_{i}\right)^{n-f}
$$

To simplify calculation, it is common to choose a prior distribution and its corresponding likelihood function from the well-known conjugate families that in turn result in a posterior distribution from the same family [32]. Actually, the conjugate

distribution of binomial distribution is Beta distribution, thus this paper assumes that the $P_{i}$ of $X_{i}$ follows the $\operatorname{Beta}(\alpha, \beta)$ distribution $[18,31]$ :

$$
f\left(P_{i}\right) \propto P_{i}^{\alpha-1}\left(1-P_{i}\right)^{\beta-1}
$$

where $\alpha$ and $\beta$ are parameters of Beta distribution. In practice, $\alpha$ and $\beta$ can be regarded as the numbers of occurrences and non-occurrences of $X_{i}$, respectively. Apparently, $\alpha+\beta$ is the number of served patients in the hospital in a time interval. Then, the posterior distribution of $P_{i}$ can be obtained based on equation (3):

$$
\begin{gathered}
f\left(P_{i} \mid A P D\right) \propto f\left(A P D \mid P_{i}\right) f\left(P_{i}\right) \propto P_{i}^{f}\left(1-P_{i}\right)^{n-f} P_{i}^{\alpha-1}\left(1-P_{i}\right)^{\beta-1} \\
\propto P_{i}^{\alpha+f-1}\left(1-P_{i}\right)^{\beta+n-f-1}
\end{gathered}
$$

Obviously, the posterior distribution of $P_{i}$ is also a Beta distribution and the updated parameters are $\alpha+f$ and $\beta+n-f$, respectively.

In this paper, the value of $P_{i}$ is considered as the mean value of Beta distribution. So, the prior probability of $X_{i}$ can be presented as:

$$
P_{i}=\frac{\alpha}{\alpha+\beta}
$$

and the posterior probability of $X_{i}$ is adapted as:

$$
P\left(X_{i} \mid A P D\right)=\frac{\alpha+f}{(\alpha+f)+(\beta+n-f)}=\frac{\alpha+f}{\alpha+\beta+n}
$$

3.4. Dynamic risk profile for hemodialysis infection

When involving three-state device failures, conventional minimal cut sets methods in FTA to compute the probability of the top event become ineffective. Noisy OR-gate and AND-gate models can be introduced to handle corresponding "OR" gate and "AND" gate in FTA, and help to assign conditional probabilities for those intermediated events [33]. Let $Y$ be an intermediate event, and $X_{1}, X_{2}, \cdots, X_{n}(i=$

$1,2, \cdots, n$ ) be the lower events of $Y$. Each $X_{i}$ with three states is associated with a weight $w_{i}$ which means $X_{i}$ can cause $Y$ with the probability of $w_{i}$. For noisy ORgate, the conditional probabilities can be:

$$
\mathrm{P}\left(Y \mid X_{1}, X_{2}, \cdots, X_{n}\right)=1-\prod_{1 \leq i \leq n}\left(1-w_{i}\right)
$$

For noisy AND-gate, the conditional probabilities can be:

$$
\mathrm{P}\left(Y \mid X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{1 \leq i \leq n} w_{i}
$$

Then, the probability of $Y$ is obtained using the following equation:

$$
\mathrm{P}_{\text {noisy }}=\prod_{i=1}^{n} P\left(X_{i}\right) P\left(Y \mid X_{i}\right)
$$

The weights for device failures are listed in Table 5. These values are estimated according to the expert suggestions, and the weights for state " 0.5 " are assigned as half of the values for state " 1 ". For example, $G_{10}$ in Fig. 3 is regarded as a noisy OR-gate and the conditional probabilities for $G_{10}$ is computed using equation (9) (see Table 6).

Table 5 Weights for device failures


Table 6 Conditional probabilities for $G_{10}$



For other intermediate events with only two-state lower events, their probabilities can be computed as:

$$
\begin{gathered}
P_{A N D}=\prod_{i=1}^{n} P\left(X_{i}\right) \\
P_{O R}=1-\prod_{i=1}^{n}\left(1-P\left(X_{i}\right)\right)
\end{gathered}
$$

Based on equation (11)-(13), the probability of the top event considering three-state events can be obtained by computing the probabilities of each logic gate from the bottom to the top.

Device failures and human errors can be prevented, or at least their occurrence probabilities can be reduced by adopting suitable safety measures. Considering the resources limitations, it is reasonable for healthcare to identify events with high criticalities, and assign corresponding measures onto these events. This paper measures the criticality of an event based on the ratio of variation (RoV), which takes both prior and posterior probabilities of an event into account and thus evaluates the criticality from a holistic perspective [34,35]. For a given basic event $X_{i}$, the posterior probability $\pi\left(X_{i}\right)$ can be computed as:

$$
\pi\left(X_{i}\right)=\mathrm{P}\left(X_{i} \mid T O P\right)=\frac{\mathrm{P}\left(T O P \mid X_{i}\right)}{\mathrm{P}(T O P)}
$$

and RoV can be represented as:

$$
\operatorname{RoV}=\frac{\pi\left(X_{i}\right)-\theta\left(X_{i}\right)}{\theta\left(X_{i}\right)}
$$

where $\theta\left(X_{i}\right)$ denotes the prior probability of $X_{i}$.

# 4. Case study 

In the case study, data is collected from a large general hospital in Tianjin, China and used to estimate the prior parameters. Failure rates $\lambda$ and repair rates $\mu$ of device failures following exponential distribution are listed in Table 7. Parameters $\alpha$ and $\beta$ of human errors following Beta distribution are listed in Table 8. During data collection, we are allowed to go to the unit once a week for almost three months, so $\Delta t$ in this study is selected as one week and all the results are within 10 weeks. More detailed data analysis and computational procedures can be found in the Appendix.

Table 7 Device failures in fault tree for hemodialysis infection

$\left(\lambda, 10^{-5} / \mathrm{h}\right)$ | Repair rate
$(\mu, / \mathrm{h})$ | Prior probability
$\left(5^{\text {th }}\right.$ week) | Posterior probability
$\left(10^{-3}, 5^{\text {th }}\right.$ week) | Ratio of Variation
(RoV, $5^{\text {th }}$ week)  |

Table 8 Human errors in fault tree for hemodialysis infection

$\left(5^{\text {th }}\right.$ week) | Posterior probability
$\left(10^{-2}, 5^{\text {th }}\right.$ week) | Ratio of Variation
(RoV, $5^{\text {th }}$ week)  |

# 4.1. Dynamic risk profile for hemodialysis infection 

In order to compute the probability of the top event "hemodialysis infection", the occurrence probabilities of 23 basic events in Fig. 3 should be determined first. For each device failure in Table 7, to simplify calculation, failure rates $\lambda_{i}(i=1,2,3)$ and repair rates $\mu_{j}(j=1,2)$ between states are assumed to be:

$$
\begin{gathered}
\lambda_{1}=\lambda_{2} \\
\lambda_{1}+\lambda_{3}=\lambda \\
\lambda_{1} / \lambda_{3}=3 \\
\mu_{1}+\mu_{2}=\mu \\
\mu_{1} / \mu_{2}=1 / 2
\end{gathered}
$$

Based on the above equations, $\lambda_{i}(i=1,2,3)$ and $\mu_{j}(j=1,2)$ of each device can be computed and further, failure probabilities at different times can be obtained according to Table 2-4. $X_{5}$ (Multi-media filter failure) is taken as an example. The failure probabilities at different time points without repairs, with imperfect repairs, and with perfect repairs, are shown in Fig. 6. As shown in Fig. 6, the probability of $X_{5}$ in state " 0 " is decreasing while that of $X_{5}$ in state " 0.5 " and " 1 " continues to increase, under all repair degrees. Repair modes make a difference in the slopes of different states. The results are consistent with the degrading process in reality, verifying the effectiveness and practicality of the proposed method. In addition, the failure probabilities are increasing slightly, demonstrating the high reliability of medical devices [12].

![img-5.jpeg](img-5.jpeg)
(a)Probability of $X_{5}$ without repairs within 10 weeks
![img-6.jpeg](img-6.jpeg)
(b)Probability of $X_{5}$ with imperfect repairs within 10 weeks
![img-7.jpeg](img-7.jpeg)
(c)Probability of $X_{5}$ with perfect repairs within 10 weeks

Fig. 6 Occurrence probability of $X_{5}$ within 10 weeks

For each human error (Table 8), Table 9 lists the accident precursor data during 10 weeks. According to equation (8), probability updating can be conducted using these data. $X_{2}$ (Error in puncture) is taken as an example to illustrate the proposed method and the result is shown in Fig. 7. As shown in Fig. 7, different from the probability of device failures, that of human errors fluctuates rather than increases continuously. Specifically, human error probability goes up when an error occurs in the current week and goes down when there is no error. It can be attributed to the uncertainty and complexity of human behaviors, which are influenced by various aspects, such as psychological factors, circumstances, etc. [36].

Table 9 Accident precursor data of human errors within 10 weeks


![img-8.jpeg](img-8.jpeg)

Fig. 7 Occurrence probability of $X_{2}$ within 10 weeks
So far, probabilities of basic events per week are obtained, and the probability of hemodialysis infection can be calculated. Fig. 8 shows the occurrence probability of hemodialysis infection without repairs, with imperfect repairs, and with perfect repairs within 10 weeks. In Fig. 8, the occurrence probability of hemodialysis infection increases over time due to the joint impact of device failures and human errors. Especially, the increasing rates of the probability are decreasing when considering no repairs, imperfect and perfect repairs.

Criticality analysis is conducted using the concept of RoV and the results are shown in Table 7 and 8 (the $5^{\text {th }}$ week under imperfect repairs). As illustrated from Table 7, $X_{4}$ (catheter contamination), $X_{5}$ (multi-media filter failure), $X_{6}$ (carbon filter failure), $X_{7}$ (demineralizer failure) have the highest RoV, since most hemodialysis patients rely on the catheters that are associated with high infection rates [37]. Besides, hemodialysis patients usually are exposed to a large amount of water that contains a lot of chemicals and bacteria [38]. In addition, almost all the human errors show high RoV of 10.52 (Table 8). In a dialysis unit, limited number of nurses, whose compliances are easily

influenced by such a high-stress circumstance, take care many patients [39]. When the workloads of nurses cannot be alleviated in an effective way, staff training, personal protective equipment and other means are necessary for healthcare to reduce human errors [40].
![img-9.jpeg](img-9.jpeg)

Fig. 8 Occurrence probability of hemodialysis infection within 10 weeks

# 4.2. Validation of the model 

Validation is to demonstrate that the model is a reasonable representation of the actual healthcare system. Due to the operability and intelligibility, a validation method introduced by Jones B et al [41], is adopted. The method requires that the results of the sensitivity analysis should satisfy the following three axioms:

Axiom 1. A slight increase/decrease in the prior probabilities of each basic event should certainly result in a relatively increase/decrease of the posterior probabilities of the top event.

Axiom 2. Given the variation of probability distributions of each basic event, its influence magnitude to the top event values should keep consistency.

Axiom 3. The total influence magnitudes of the combination of the probability

variations from $x$ attributes on the values should be always greater than the one from the set $x-y(y \in x)$ attributes.

Take the basic events $X_{1}-X_{4}$ with imperfect repairs at the $5^{\text {th }}$ week as an example. When $X_{1}$ is set to $100 \%$, the probability of the top event "hemodialysis infection" increases to $44.99 \%$ from $8.68 \%$. When both $X_{1}$ and $X_{2}$ are set to $100 \%$, the probability increases to $49.55 \%$. Besides, when $X_{3}$ is also set to $100 \%$, the probability increases to $79.71 \%$. When all these four basic events occur, the probability of the top event increases to $95.88 \%$. The sensitivity analysis satisfies all the axioms above, therefore providing a partial validation to the model. In order to conduct a full validation, parameters monitoring and data collecting for a long period are required, but it is impractical in practices in terms of the confidentiality in healthcare, as well as involved time and cost.

# 5. Conclusions and perspectives 

Dynamic risk assessment model for hemodialysis infection is constructed and validated in this paper. Considering unique features of different risk factors, device failures and human errors are handled separately, with the help of dynamic Bayesian network and Bayesian inference, respectively. FTA serves as a modular framework to integrate these factors and evaluate the medical risk as a whole.

The proposed method is applied in a case study of hemodialysis infection from a hospital. The results show that by introducing Bayesian approaches, the probability variations of device failures, human errors and hemodialysis infection during 10 weeks can be obtained. The failure probabilities of devices are increasing slightly, verifying

the high reliability of medical devices. In contrast, the occurrence probabilities of human errors exhibit irregularity as they fluctuate within the 10 weeks, due to their uncertainty and complexity. In addition, the occurrence probability of hemodialysis infection increases over time due to the joint impact of device failures and human errors. Especially, the increasing rates of the probability are decreasing when considering no repairs, imperfect and perfect repairs. Also, catheter contamination, multi-media filter failure, carbon filter failure and demineralizer failure, are identified as the most critical device failures at the $5^{\text {th }}$ week under imperfect repairs. Besides, most of the human errors have high criticalities. Critical events at different times can be identified in the similar way. This offers healthcare the basis for assigning and adapting safety measures. Although this paper uses a specific example of hemodialysis infection, the developed model can also be applied to other healthcare domains, since device failure and human error are common risk factors in healthcare [9].

There are also some limitations in using Bayesian based model. Firstly, the prior probabilities and assumptions, e.g. failure and repair times of device failures follow exponential distributions, influence the accuracy of the model parameters and posterior distributions. Therefore, reliable and abundant input data is necessary to build more accurate models. Secondly, healthcare is much more complex due to the diversity of medical processes, the heterogeneity of patients, the wide range of providers, among others [9]. When those factors and their interactions need to be considered, Bayesian methods become ineffective. In addition, when involving more states, the size of the model explodes, which will consume computational time and cost. To release the

aforementioned limitations, simulation methods, such as Monte Carlo simulation and Petri net, can be helpful tools to supplement the Bayesian approaches [42,43].

# Acknowledgements 

This research is supported by the National Natural Science Foundation of China (No. 91746205 and No. 71871158).

## A. Appendix

This appendix demonstrates how the input data in the case study is collected and obtained. Besides, some examples are given to demonstrate the specific computational procedures of the proposed model.

## A.1. Data collection

In the case study, the occurrence probability of hemodialysis infection is computed using the proposed model. According to the proposed method, the required input parameters include: failure rates $\lambda_{i}(i=1,2,3)$ and repair rates $\mu_{j}(j=1,2)$ between the states of the medical devices following exponential distribution, as well as $\alpha$ and $\beta$ of human errors following $\operatorname{Beta}(\alpha, \beta)$ distribution. In order to obtain these data, we investigated a dialysis unit in a hospital from Tianjin, China.

For device failures (Table 7), the unit has the data of average failure rates $\lambda$ and repair times provided by the devices manufacturers. Then, the repair rates $\mu$ are set as the inverse of the repair times. However, the manufacturers didn't provide the more detailed data, such as the failure rates $\lambda_{i}(i=1,2,3)$ and repair rates $\mu_{j}(j=1,2)$ between states, since that is relevant to the quality of their products. Therefore, to

simplify calculation, we estimate these parameters by making assumptions between their values (Equation (16)-(20)).

For human errors (Table 8), $\alpha$ and $\beta$ can be assigned as the number of occurrence and non-occurrence of the human error. However, we couldn't find required data to estimate the values of parameters, since the unit does not have an established medical error reporting mechanism. In addition, infections usually do not occur immediately, creating difficulties in identifying causes and estimating infection rate. Only serious infections had been recorded, but the detailed data is not available due to confidentiality. There are about 1460 cases in the unit last year and the rate of serious infections is around $1.68 \%$ ( 24.53 serious infections per year). Therefore, we assume the number of infections is 24.53 and assign it as the sum of $\alpha$ for all human errors. Then, $\alpha$ of each human error is obtained using random number generation and $\beta$ is the difference between $\alpha$ and 1460. This method had negative impact on the accuracy of the model at the beginning, which would be compensated by repeating Bayesian inference-based updating.
A.2. Calculation of the occurrence probabilities of $X_{5}$
$X_{5}$ is taken as an example to demonstrate the computation procedures of the occurrence probabilities of device failures. The failure rate $\lambda$ and repair rate $\mu$ of $X_{5}$ are $3.835 \times 10^{-5}$ and 0.67 per hour, respectively. Based on equation (16)-(20), $\lambda_{1}-\lambda_{3}$, and $\mu_{1}-\mu_{2}$ of $X_{5}$ can be computed as: $2.876 \times 10^{-5}, 2.876 \times 10^{-5}, 9.59 \times 10^{-6}, 0.2233$ and 0.4467 , respectively. At week $0(\mathrm{~T}=0), X_{5}$ is assumed to at state " 0 ", meaning the probabilities of $X_{5}$ are as follows: $\mathrm{P}\left(X_{5}^{T=0}=1\right)=\mathrm{P}\left(X_{5}^{T=0}=0.5\right)=0, \mathrm{P}\left(X_{5}^{T=0}=\right.$

$0)=1$, under all repair degrees. At $\mathrm{T}=1$, according to Table 2 , the transition probabilities between $\mathrm{T}=0$ and $\mathrm{T}=1$ without repairs are computed as:

Supplementary table 1 transition probabilities of $X_{5}$ between $\mathrm{T}=0$ and $\mathrm{T}=1$ (without repairs)


According to the total probability formula, the probabilities of $X_{5}$ at $\mathrm{T}=1$ without repairs can be obtained as follows:

$$
\begin{aligned}
& \mathrm{P}\left(X_{5}^{T=1}=1\right)=\mathrm{P}\left(X_{5}^{T=1}=1 \mid X_{5}^{T=0}=0\right) \mathrm{P}\left(X_{5}^{T=0}=0\right) \\
& +\mathrm{P}\left(X_{5}^{T=1}=1 \mid X_{5}^{T=0}=0.5\right) \mathrm{P}\left(X_{5}^{T=0}=0.5\right) \\
& +\mathrm{P}\left(X_{5}^{T=1}=1 \mid X_{5}^{T=0}=1\right) \mathrm{P}\left(X_{5}^{T=0}=1\right)=0.0016 \\
& \mathrm{P}\left(X_{5}^{T=1}=0.5\right) \\
& =\mathrm{P}\left(X_{5}^{T=1}=0.5 \mid X_{5}^{T=0}=0\right) \mathrm{P}\left(X_{5}^{T=0}=0\right) \\
& +\mathrm{P}\left(X_{5}^{T=1}=0.5 \mid X_{5}^{T=0}=0.5\right) \mathrm{P}\left(X_{5}^{T=0}=0.5\right) \\
& +\mathrm{P}\left(X_{5}^{T=1}=0.5 \mid X_{5}^{T=0}=1\right) \mathrm{P}\left(X_{5}^{T=0}=1\right)=0.0048 \\
& \mathrm{P}\left(X_{5}^{T=1}=0\right)=1-\mathrm{P}\left(X_{5}^{T=1}=0.5\right)-\mathrm{P}\left(X_{5}^{T=1}=1\right)=0.9936
\end{aligned}
$$

Similarly, the probabilities of $X_{5}$ at different times and under different repair degrees can be obtained as shown in Fig. 6.
A.3. Calculation of the occurrence probabilities of $X_{2}$
$X_{2}$ is taken as an example to demonstrate the computation procedures of the occurrence probabilities of human errors. At $\mathrm{T}=0$, the parameters of $X_{2}$ are $\alpha_{2}^{T=0}=$ 2.987 and $\beta_{2}^{T=0}=1457.013$. Then, the probability of $X_{2}$ is computed based on

equation (7) as follows:

$$
\mathrm{P}\left(X_{2}^{T=0}\right)=\frac{2.987}{2.987+2457.013}=0.00205
$$

At $\mathrm{T}=1, X_{2}$ didn't occur and 20 patients received hemodialysis this week, thus the probability can be updated based on equation (8) as follows:

$$
P\left(X_{2}^{T=1}\right)=\frac{2.987+0}{1457.013+20}=2.02 \times 10^{-3}
$$

Similarly, the probabilities of $X_{2}$ at different times can be obtained as shown in Fig. 7.
A.4. Calculation of the occurrence probabilities of hemodialysis infection

The probability of hemodialysis infection at $5^{\text {th }}$ week with imperfect repairs is taken as an example to demonstrate the computation procedures. The probabilities of basic events are computed using aforementioned procedures and shown as follows:

Supplementary table 2 probabilities of device failures ( $5^{\text {th }}$ week, with imperfect repairs)


Supplementary table 3 probabilities of human errors ( $5^{\text {th }}$ week, with imperfect repairs)


Examples of computation procedures for different gates in FTA are as follows:
Noisy OR-gate: $\mathrm{P}\left(G_{10}\right)=\prod_{i=0}^{9} P\left(X_{i}\right) P\left(Y \mid X_{i}\right)=0.0137$.
Noisy AND-gate: $\mathrm{P}\left(G_{7}\right)=\prod_{i=16}^{17} P\left(X_{i}\right) P\left(Y \mid X_{i}\right)=0.00276$.
OR gate: $\mathrm{P}\left(G_{12}\right)=1-\prod_{i=20}^{21}\left(1-P\left(X_{i}\right)\right)=0.00427$.
Similarly, the probabilities of hemodialysis infection at different times can be obtained, as shown in Fig. 8, by calculating the probabilities of each logic gate from the bottom to the top.
