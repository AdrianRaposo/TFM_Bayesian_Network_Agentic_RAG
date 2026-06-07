# Generic Bayesian Network Models for Making Maintenance Decisions from Available Data and Expert Knowledge 

Haoyuan Zhang, D. William R. Marsh<br>School of Electronic Engineering and Computer Science, Queen Mary University of London, UK

Corresponding Author: Haoyuan Zhang

Contact Address: School of Electronic Engineering and Computer Science, Queen Mary University of London, UK

Email: haoyuan.zhang@qmul.ac.uk

This is the submitted version of the paper:
Haoyuan Zhang, D. William R. Marsh. Generic Bayesian Network Models for Making Maintenance Decisions from Available Data and Expert Knowledge. Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability.

#### Abstract

To maximize asset reliability cost-effectively, maintenance should be scheduled based on the likely deterioration of an asset. Various statistical models have been proposed for predicting this but they have important practical limitations. We present a Bayesian network model that can be used for maintenance decision support to overcome these limitations. The model extends an existing statistical model of asset deterioration, but shows how i) data on the condition of assets available from their periodic inspection can be used ii) failure data from related groups of asset can be combined using judgement from experts iii) expert knowledge of the causes deterioration can be combined with statistical data to adjust predictions. A case study of bridges on the GB rail network is presented, showing how the model could be used for the maintenance decision problem, given typical data likely to be available in practice.


# Keywords 

Bayesian network, Available data, Expert knowledge, Maintenance modelling, Deterioration, GB rail bridges

# 1 Introduction 

Maintenance consists of a set of activities required to ensure assets are in a reliable operating condition. According to Dhillon, ${ }^{1}$ maintenance strategies can be of three types: i) corrective maintenance, where maintenance follows failure ii) preventive maintenance, where inspections and maintenance follow a fixed schedule and iii) predictive maintenance, where the schedule depends on the condition of assets. Predictive maintenance requires a way to predict the future condition of an asset by estimating how fast it will deteriorate from its current condition.

A range of different modelling techniques has been proposed to implement predictive maintenance strategy. However, in many situations these do not provide practical decision tools as the assumed data is unavailable and relevant knowledge that could be used to distinguish between different individuals in the same asset class is unused:

- We may only have data such as a history of repairs, from which the condition of assets has to be inferred with considerable uncertainty.
- Conventionally, separate deterioration models are created from failure data of each different type of asset, which is a difficulty for an organisation with many different asset types but only little failure data for each. We would therefore like to be able to pool failure data where we have evidence that different but related asset types have related deterioration processes.
- Decisions about maintenance can be made for specific structure, whereas deterioration models cover all asset of the same type. It should be possible to use experience (e.g. among maintainers) about the effect of factors such as environmental conditions, loading and design differences on the rates of deterioration in combination with models derived from failure data in a population where these factors vary.

This paper proposes an asset deterioration model building on an existing statistical model that can be adapted to pool related data and incorporate expert knowledge about factors that affect the likely deterioration rates. Section 2 describes the typical modelling techniques for maintenance problems, and discusses the advantages of Bayesian networks (BNs) to meet the challenges of unused data and expert knowledge. Section 3 introduces the way generic BN models can be built to learn from available data and expert knowledge in asset maintenance problems. We assemble the models and show how to use the model for practical decisionmaking for GB rail bridges maintenance planning in Section 4. The paper ends with conclusions in Section 5.

# 2 Background 

Markov models, Petri nets and Bayesian networks are three commonly used modelling techniques that have been developed to predict asset performance for maintenance purpose. Section 2.1 reviews the work on Markov models and Petri nets, and their limitations for reliability modelling. Section 2.2 gives a brief introduction to BNs. The application of BNs to reliability modelling is described in Section 2.3.

### 2.1 Modelling using Markov models and Petri nets

In a Markov model, deterioration is modelled by a sequence of states representing the condition of an asset system over time (e.g. condition rating from 0 to 7 in Agrawal et al. ${ }^{2}$ ). Simple models have a fixed transition probability from one state to the next; typically these probabilities have to be estimated from data. Jiang et al. ${ }^{3}$ and Cesare et al. ${ }^{4}$ apply Markov models to predict future state of bridges, and Shafahi and Hakhamaneshi ${ }^{5}$ used it for track maintenance prediction.

Deterioration models that combine several repair states with non-fixed transition probabilities have been implemented using Petri nets and Monte-Carlo simulation. Audley and Andrews ${ }^{6}$ used this approach to model the degradation of track, developing an optimum inspection and maintenance policy. A hierarchical Petri net model for rail track maintenance is presented by Rama and Andrews ${ }^{7}$, but the data needed to parameterise the model is not described in detail. Though Markov models and Petri nets are popular in reliability modelling, they require sufficient failure data, which is impractical in many maintenance problems since assets may have little failure data. Also, an easy way to integrate expert knowledge in these models is still uncommon.

# 2.2 Bayesian networks overview 

A Bayesian network is a flexible modelling technique. A BN represents the joint probability of a set of random variables; causal or influential relationships between variables are specified by a directed graph with the variables as nodes. The joint probability distributions are calculated using the following equation:

$$
p(X)=\prod_{i=1}^{n} p\left(X_{i} \mid \operatorname{parents}\left(X_{i}\right)\right)
$$

Here, $p(X)$ is the joint probability of the variables in the model, given by the product of the conditional probability of each variable $X_{i}$ given its parents. The example Bayesian network in Figure 1 models the dependencies among four random variables $\mathrm{X}=\left[\mathrm{X}_{1}, \ldots, \mathrm{X}_{4}\right] . \mathrm{X}_{2}$ is depends on $\mathrm{X}_{1}$ and $\mathrm{X}_{4}$ depends on variables $\mathrm{X}_{2}$ and $\mathrm{X}_{3}$ so that we say $\mathrm{X}_{1}$ is the parent of $\mathrm{X}_{2}$, while $\mathrm{X}_{2}$ and $\mathrm{X}_{3}$ are the parents of $\mathrm{X}_{4} ; \mathrm{X}_{1}$ and $\mathrm{X}_{3}$ have no parents and $\mathrm{X}_{4}$ has no children. The joint distribution of this example is $p\left(X_{1}, X_{2}, X_{3}, X_{4}\right)=p\left(X_{4} \mid X_{2}, X_{3}\right) p\left(X_{2} \mid X_{1}\right) p\left(X_{1}\right) p\left(X_{3}\right)$.

# [insert Figure 1.] 

The BN therefore has two components: the first is the graph of the chosen variables and their dependency; the second is the conditional probability distribution of each variable, given the states of its parents, which form the parameters of the BN. When some variables have a known state, an inference algorithm can update the probability distribution of the remaining variables, using Bayes' theorem. Many early BN inference algorithms worked primarily with discrete variables, allowing continuous variables only by discretisation. This was a barrier for the use of BNs in reliability analysis where both discrete and continuous variables are needed.

### 2.2.1 Hybrid BN

A BN that contains both discrete and continuous variables is called a hybrid BN. Local exact inference in hybrid BN can be executed only under the assumption of conditional Gaussian distributions. ${ }^{8}$ However, it is impractical for models with mixture of discrete variables and non-standard distributions. Static discretisation allows approximate inference in a hybrid BN but states of a continuous variable are mapped into pre-defined finite set of discrete states, with a trade-off between accuracy and efficiency. ${ }^{9}$ Although many other approaches to inference have been proposed, it remains challenging to support various types of distributions in hybrid BNs.

Inspired by the work on using non-uniform discretisation in a hybrid BN from Kozlov and Koller, ${ }^{10}$ Marquez et al. ${ }^{11}$ use dynamic discretisation in an exact inference algorithm. Continuous variables are dynamically discretised, with narrower intervals where the probability distributions are changing most. This algorithm is implemented in the BN tool AgenaRisk, ${ }^{12}$ which is used in our paper for its flexibility and efficiency.

# 2.2.2 Hyper parameters in a hierarchical BN model 

A hierarchical BN model is a standard BN model extended with additional variables; the variables are called hyper-parameters as they represent statistical parameters (such as mean and variance in a Normal distribution) used elsewhere in the model; the result is that we can model the uncertainty about the parameters themselves. To construct a hierarchical BN model, prior probability distributions of hyper-parameters, need to be assigned. When hyperparameters have conjugate priors, choosing a prior from that list can simplify posterior distribution calculation, so these distributions are often used (Fink ${ }^{13}$ contains a list of conjugate priors); however, any distribution can be used in the numerical approach we are using. When no additional information about the hyper-parameters is available, uninformative prior distributions can be assigned. ${ }^{9}$ Another way is to elicit priors from past information, such as past experiments or expert knowledge. ${ }^{14}$ Experts play an important role when less data is available. An example of how to explicit knowledge from experts are presented in Cooke. ${ }^{15}$ The process of knowledge elicitation is further discussed in Section 5.2.

### 2.3 Applications of BN to reliability

In system reliability, a range of studies has shown the benefits of BNs over conventional approaches for reliability modelling and analysis. In particular, modelling features of BNs, such as flexibility in modelling common cause ${ }^{11}$ and sequential failures and multi-state variables, ${ }^{16}$ capability in modelling an extensive ranges of failure distributions, ${ }^{17}$ and diagnostic reasoning ${ }^{18}$ are valuable in reliability problems.

### 2.3.1 Discrete BN

Early work of the applications of BN to reliability modelling mostly used discrete BN. Kang and Golay ${ }^{19}$ estimated the state of a system after a selected maintenance action using a discrete BN model. A discrete BN model that allows diagnosis and prognosis for manufacturing processes is developed in Weber et al., ${ }^{18}$ including a maintenance model. Celeux et al. ${ }^{20}$ proposed a BN for preventive maintenance using experts, with a set of rules for choosing the most reliable of different probabilities elicited from experts. Its reliability is secured by a feedback procedure to eliminate inconsistent probabilities of the parameters. Factors, such as maintenance complexity, expertise of professionals, that could induce uncertainty during the maintenance process are considered in de Melo and Sanchez. ${ }^{21}$ They present a discrete BN model to predict delays of a software maintenance project based on project features and experts experience. However, in system reliability, asset deterioration should be modelled using continuous variables ${ }^{22}$ and statistical distributions, with parameters fitted from data.

# 2.3.2 Hybrid BNs and models with hyper-parameters 

With the development of inference algorithms for hybrid BN as discussed in Section 2.2.1, applications of hybrid BN to reliability have been given more attention recently. Langseth and Portinale ${ }^{23}$ discuss the properties of the modelling framework for hybrid BN and its applicability for reliability analysis. Some applications have been proposed. For example, failure distribution of system components are fitted by continuous-time variables in the BN model proposed in Boudali and Dugan, ${ }^{17}$ and an electrical power system is modelled by Mengshoel et al. ${ }^{24}$ using a hybrid BN for its sensor validation and diagnosis. Some applications using BN models with hyper parameters are proposed, such as Kuo and Yang ${ }^{25}$ applied a hierarchical BN in software reliability, but all the hyper-parameters are

assumed known. Coolen ${ }^{26}$ presented a Bayesian reliability analysis with informative priors extracting from experts.

Marquez et al. ${ }^{11}$ presented a hierarchical BN to model continuous failure times of components and overall system reliability. In its parameter learning BN model for a system supervision component, failure data followed a Weibull distribution with parameters governed by hyper-parameters shape and scale. Each hyper-parameter has a prior modelled by a triangular distribution given by experts. The posterior distributions on the hyperparameters are updated from data on actual failures and the model can then predict reliability using the learned parameters.

Given the situation that failure data is insufficient and expert knowledge is unused in practical maintenance problems discussed in Section 1, BNs are attractive for reliability modelling because they can combine expert knowledge with data and can therefore be applied in situations when there is insufficient failure data for a purely statistical approach. Furthermore, with more recent inference algorithms, BNs models can use both discrete and continuous variables. The parameter learning BN model proposed in Marquez et al. ${ }^{11}$ provides a flexible framework combining these features and is adopted as the basis of our study. This model is introduced in more detail in Section 3.1.

# 3 Generic Bayesian networks models of asset condition 

In this section we present several generic hybrid BN models to support maintenance decision making, where assets deteriorate through multiple states, with each failure time (after which it move to the next state) following a Weibull distribution. Section 3.1 presents the basic hyper-parameter learning BN model, following Marquez et al. ${ }^{11}$. Section 3.2 extends this with multiple states, each representing a further state of deterioration, and Section 3.3 shows how

to pool data from different asset types with similar deterioration rate. Section 3.4 demonstrates the capability of the model to use more realistic types of failure data. Section 3.5 extends the fragment to include expert knowledge to customize the prediction for a particular asset. Section 3.6 shows how future condition can be predicted and a summary is presented in Section 3.7.

# 3.1 A simple hyper-parameter BN model of asset deterioration 

The expected lifetime of an asset is derived from its likely time to failure. The time to failure follows a statistical model, with parameters determined by gathering a set of failure time data and fitting it to the chosen distribution. In a hierarchical model, the parameters (or hyperparameters) become part of the model; data on known failure times is entered, updating the distribution over the parameters. We introduce these features of a hyper-parameter model in the following sections.

### 3.1.1 Selecting a time-to-failure distribution

Any distribution can be used in a hyper-parameter model - which is best? He et al. ${ }^{27}$ use exponential distributions to estimate degradation of railway track while the gamma distribution, in the form of gamma processes, is used by Edirisinghe et al. ${ }^{28}$ to study the deterioration of building components. Studies of bridges ${ }^{2}$ and railways ${ }^{29}$ provide two examples showing the use of Weibull distributions to model a range of asset deterioration behaviours.

In $\mathrm{Le}^{30}$, lifetime data of bridge components from the same type and material are grouped together to fit with a series of distributions. The closeness of fit of Normal, Exponential, Lognormal and Weibull distributions is compared using their probability plots and AndersonDarling tests. Weibull distributions have the closets fit in most cases. Given this results and

its versatility in describing a range of deterioration behaviours, we selected the Weibull distribution, with probability density over time $t$ shown in Equation (2), for our study. The two parameters of the distribution are shape $\beta$ and scale $\eta$.

$$
f(t)=\frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} e^{-\left(\frac{t}{\eta}\right)^{\beta}}, f(t) \geq 0, \beta \geq 0, \eta \geq 0
$$

# 3.1.2 Prior probabilities for the Weibull's shape and scale 

To construct the hierarchical failure model, prior probability distributions of hyperparameters, such as the Weibull's shape and scale, need to be assigned. It is difficult for nonstatisticians to evaluate the values of shape and scale but can be made easier by understanding the characteristics of the distribution. In Weibull distribution, the effect of the shape parameter on the failure rate is shown in Figure 2, with shape $<1$ describing early degradation leading to decreasing failure rate and shape $>1$ describing wear-out failure, giving an increasing failure rate. Also, for a given shape, increasing the scale increases the mean failure time.
[insert Figure 2.]
By observing the plots of the hyper-parameters, experts can justify whether a type of asset has a decreasing, constant or increasing failure rate, leading to a range of possible values for the shape parameter. Similarly, it is also possible to evaluate the range of the scale parameter from the typical age of asset failure. Different distributions, such as normal distribution or uniform distribution, could be used to express uncertainty over the range of each parameter. Some experts find it easier not to specify their opinion with absolute precision but providing value intervals. ${ }^{31}$ Following Marquez et al., ${ }^{11}$ triangular distributions (Equation (3)) are used

in our model for its advantage in extracting value ranges from experts based on past experience:

$$
P(x)=\left\{\begin{array}{c}
\frac{2(x-a)}{(b-a)(c-a)}, a \leq x \leq c \\
\frac{2(b-x)}{(b-a)(c-a)}, c<x \leq b
\end{array}\right.
$$

where $P(x)$ is the probability function of triangular distribution, $a$ is its lower limit, $b$ is its median and $c$ is its upper limit. Experts assign values of $a, b$ and $c$ for each parameter, based on their pass experience.

# 3.1.3 The hyper-parameter BN 

Figure 3 presents a BN model constructed on these principles, and Table 1 lists its NPTs. The time each asset transits from a normal to a failed state follows a Weibull distribution, which can be inferred when data on the past transition of the assets of the same class are entered as evidence. Take Asset 1 as an example, the entered data 15 representing it takes 15 months for Asset 1 to transit from a normal state to a failed state. Because we consider assets 1 to 6 to be of the same type, we assume that they deteriorate following the same Weibull distribution, meaning that they share the same shape and scale. The posterior distribution of transition time from one state to another state, which predicts future failure for the asset in the same class, is shown for the variable Transition Distribution, derived from the hyper-parameters learnt from data.
[insert Figure 3.]
[insert Table 1.]

We only show failure data for six assets in this example. However, increasing the size of the dataset causes the parameters of the Weibull distribution to start to converge and with sufficient failure data, it is possible to overcome the prior probabilities estimated by experts.

# 3.2 Assets with multiple states 

Statistical models can model the different aging processes of assets but directly distinguish only working from (hard) failure; this is not sufficient for using inspection data and making decisions about a variety of maintenance actions, for which models with multiple states of repair are more suited. One way to combine statistical models with this requirement is using a Markov model based condition rating system (see Section 2.1).

To model the deterioration of assets through several states of repair, we can extend the model in Section 3.1 with multiple states (Figure 4).
[insert Figure 4.]
To illustrate the idea, three states are modelled., with transition time from State 1 to State 2 (Transition 1), State 2 to State 3 (Transition 2). Each transition is modelled by a separate parameters learning model. In this example, Transition 1 follows a Weibull distribution with parameters shape 1 and scale 1, while Transition 2 with parameters shape 2 and scale 2. When decision makers enter the operating time (time interval between a specified time and the time of its last repair), the asset condition will be calculated using the following Boolean logic expression (this expression is supported in AgenaRisk):
if (Operating time < Transition 1, "State 1", if (Operating time < Transition 2, "State 2", "State 3"))

In Figure 4, a 15-months operating time was entered as an example data, representing that it has been 15 months since the last repair of an asset. Learnt from the past data of assets in the

same class, we can capture the condition distribution of the asset for this operating time: the probability that the asset stays in its original state (State 1) is around $48 \%$, transits to State 2 is around $39 \%$ and State 3 is $13 \%$. A maintenance planner can use this prediction to evaluate if an inspection needs to be carried out.

# 3.3 Assets with similar deterioration rate 

In practice, we may have several groups of assets of different types, which we believe deteriorate with similar behaviour. We propose to extend the model in Section 3.2 for the situation where there is a lot of failure data for some types of assets in the group, but much less for others. In this case, since the failure times are determined by hyper-parameters shapes and scales, we assume the distribution hyper-parameters learnt for one type of asset approximate those of the other similar type, with uncertainty.
[insert Figure 5.]
Assume assets in Group A (assets 1 to 6 in this example) and Group B (asset 7 and 8) have similar deterioration rates resulting from some shared characteristics (such as similar designs with different materials). Group A has more failure data than Group B. Figure 5 shows a parameters learning model for these two groups of assets. Shapes (node Group A: shape and Group B: shape) and scales (node Group A: scale and Group B: scale) of these assets were governed by the typical shape (node Typical shape) and scale (node Typical scale) variables, whose prior probability distributions are using triangular distributions as in Section 3.1. Experienced experts are possible to have knowledge about how similar two groups of assets are. For example, experts know about the deterioration of a stone-based structure is more similar to a concrete-based structure compares to a timber-based structure, which leads to a higher similarity degree (lower variance) between stone-based and concrete-based structure. Hence, a truncated normal (TNormal) distribution (its expression can be found in Fenton and

$\mathrm{Neil}^{9}$ ), a normal distribution bounded by lower and upper limits, is used to model the relationship between the related shape and scale of each asset type and the typical ones. The mean $\mu$ of this distribution is the typical shape or scale, and variance $\sigma^{2}$ representing the degree of similarity of the two assets, which is given by experts. The lower bound $L$ and upper bound $U$ of the distributions are also evaluated by experts about their knowledge of extreme values. In the TNormal distribution, the normal distribution is used to group singular parameters to approximate the overall parameters, while the bounds are used to prevent extreme values. Also, since their hyper-parameters shape and scale are bounded by triangular distributions, if we use an unbounded distribution, like normal distribution, on a node with a bounded range, the model may throw away values that outside the range. ${ }^{9}$

Take node Group A: shape as an example: it may have a conditional probability distribution given by TNormal (typical shape, 0.5, 1, 3). Its mean is given by the distribution of node typical shape, which inherits the typical behaviour of the shape between these two groups of assets. Its variance is 0.5 - a smaller variance means a higher similarity, representing a high degree of similarity between these two groups. The distribution is restricted to the region between 1 and 3, indicating it has an increasing failure rate (because the shape value is higher than 1 as discussed in Section 3.1) with values between 1 and 3. By extracting information from experienced experts about the degree of similarity of different assets and possible trending of the plots, the model can reason the transition time of an asset for which there is only a little data (group B) using data from other group of assets (group A) that are judged to share a similar deterioration rate.

# 3.4 Modelling of available data types 

Often, the ideal data on the failure times of assets is not available. This section explores various limitations on the data likely to be available, showing how it can be used.

The transition time is the time, since the previous transition, when an asset transitions from one state to another state. However, it is often hard to obtain this data: in practice, we are more likely to have data from periodic examinations (and perhaps repairs) rather than data on the exact transition time. To exploit the examination history data, four types of transition time data can be inferred with uncertainty as follows (for convenience, we assume inspection interval is 12 months, and the transition are between State 1 to State 2, that is Transition 1):

- Left-censored data: the asset failed at some point before we started to inspect. For example, an asset failed in its first inspection after it was built, that means the transition time is less than 12 months: Transition $1<12$.
- Interval-censored data: failures happened sometime between two inspection times. For example, in the first inspection, the asset didn't show any signs of deterioration, but we found out it failed in the second inspection. Therefore, we can conclude that the asset transitioned between 12 and 24 months: $12<$ Transition $1 \leq 24$.
- Right-censored data: for those cases where the asset survived longer than the time available for observation. Suppose an asset has been inspected twice and has survived for more than 24 months, hence Transition $1>24$.
- Exact-time data: this type of data may be available when an issue is reported. For example, at 8 months, the asset failed suddenly and inspection confirms this transition: Transition $1=8$.

To use these data, we introduce a Boolean variable to express a constraint on an asset's transition time. To represent left censored data, the variable is true when Transition $<\mathrm{t}_{\text {inspection }}$, and the true state is observed. Similar constraints are used for interval and right censored data. Furthermore, there is a possibility that a component deteriorates faster than our inspection intervals. For example, suppose that at the 12-month inspection, a component remained at

State 1, while in the 24 -month inspection, the component was found in the State 3. To use this type of information, we can enter observations for right censored data that its first transition time is greater than 12 months, and left censored data that its second is smaller than 24 months, as well as an additional constraint that the first transition time is smaller than the second one, as following:
$($ Transition $1>12) \wedge($ Transition $2<24) \wedge($ Transition $1<$ Transition 2$)$

# 3.5 Introducing experts to distinguish individual asset deterioration 

In practice, the deterioration rate may be affected by heavy use and aggressive environment conditions (see for example Yianni et al. ${ }^{32}$ ). Ideally, the maintainers' knowledge of these effects could be combined with statistical failure data gathered from a population where use and environment vary. From a decision support perspective, this will allow specific assets to be distinguished. For example, Marsh et al. ${ }^{33}$ outline a BN architecture to integrate multiple factors, such as loading and environmental stress, to support maintenance decision but do not show failure data could be included.

To distinguish individual members of a group of assets, we model the effect of environmental conditions and loading on deterioration by adjusting the scale parameter of the BN developed in previous sections. A known shape parameter is often assumed due to its relatively stable value. ${ }^{34}$
[insert Figure 6.]
As shown in Figure 6, we use two ranked nodes to express the degree of influence of factors (here, for example, loading and environment). Each factor has three states: low, medium and high. An example of how to estimate their states can be adopted from Yianni et al. ${ }^{32}$ Take loading of railways bridges as an example, track data of Equivalent Million Gross Tonnes Per

Annum (EMGTPA) passes over the bridge can be used to estimate the level of loadings. For loadings less than 3.5 EMGTPA, they are grouped as low, between 3.5 and 12 EMGTPA are classified as medium, and over 12 EMGTPA are defined as high. In Figure 6, a medium loading is observed because the EMGTPA of the line passes over asset 1 is between 3.5 EMGTPA and 12 EMGTPA.

Different factors may have different degrees in influencing the deterioration of assets, such as a well-designed metal bridge may deteriorate faster affected by its environmental stress than its loading. Experts could have knowledge about the weights of these influence factors. The degree of influence factors (node Asset 1: Influence degree) is modelled by a TNormal distribution combined using a weighted mean (wmean, equivalent to a linear model) of the influence factors (node Loading and node Environmental stress), and variances are given by experts regarding to their certainty of the weights: Influence degree $\sim$ TNormal (wmean, $\sigma^{2}, 0$, 1).

In Figure 6 shows an example, assuming the weight of loading is 0.3 and environmental stress is 0.7 , so that the combined influence of these factors is slightly closer to the high environmental stress than the medium loading.

While the parameter scale (variable Typical scale) is modelled by three TNormal distributions (since there are three states in this example: Low, Medium, High, each state is modelled by a TNormal distribution), with mean adjusted from the typical scale hyperparameter (see Section 3.3), and the bounds are given by experts (same as Section 3.3). The only differences are the variances based on the states of Influence degree: a low influence degree has a lower variance, while a high influence degree has a higher variance. The evaluation of variances is given by experts regarding to how easy the assets can be influenced by external factors.

# 3.6 Condition prediction 

The BN models of the previous sections cover the distributions of transition time between different conditions and can therefore evaluate the current condition of an asset based on its operating time, allowing decisions about, for example, the interval to the next inspection. We now extend the model further to predict its future condition, supporting a wider range of decisions. The extended model shown in Figure 7, provides the following predictions:
[insert Figure 7.]

- Current condition: the asset's condition based on its operating time (see section 3.2);
- Future condition: the future condition of the asset, taking into account both current condition and further deterioration.

The prediction of future condition works with the following logic:
if (Operating time + Next scheduled inspection time $<$ Transition 1, "State 1",
if (Operating time + Next scheduled inspection time $<$ Transition 2, "State 2", "State 3"))

Consequently, this node predicts an asset's condition distribution within different periods. In the example in Figure 7, since the last effective repair, the operating time is 5 months, therefore, the current condition has a probability of around $86 \%$ in state 1 . While the next scheduled inspection time is 7 months later, and the predicted result is quite optimistic with a probability of $62 \%$ in state 1 . We might therefore suggest that a longer inspection interval could be used for this asset to reduce costs.

### 3.7 Summary

This section has presented generic BN models to learn assets deterioration behaviour and then use this to predict the future condition of a particular asset. Each model represents a

situation that may exist in real-life maintenance problems. The models combine the use of the available data with expert knowledge; we summarise this below:

# 1. Available data: 

- Section 3.3: some assets (e.g. new asset types) may have only a little failure data. Therefore, we pool failure data with related asset types that are different but have related aging processes (e.g. an older version of the new components).
- Section 3.4: the exact time an asset transitions from one state to another state is not always available. We introduce censored data in our models so that data from periodic examinations can be used in place of exact transition times.


## 2. Expert knowledge:

- Section 3.1 and Section 3.3: it is possible for experts to propose priors for the parameters of the Weibull distribution by understanding the characteristics of each parameter. Triangular and TNormal distributions are used in our models to estimate ranges for the Weibull's shapes and scales.
- Section 3.3: knowledge that, for example, a concrete structure deteriorates more slowly than a timber structure is well-known by experts. An experienced engineer can estimate the degree to which two groups of assets will have similar deterioration.
- Section 3.5: experts may know that assets deteriorate faster when near the coast or more heavily loaded. This type of knowledge can be used to distinguish individual assets by modelling the influence of these factors in the deterioration rate.


## 4 Case study: strength assessment of GB railway bridges

In this section, we present a case study based on the processes used to maintain overbridges (a bridge crossing over the railway) on the GB rail network. Section 4.1 introduces the activities to plan maintenance work for GB railway bridges, and Section 4.2 summaries its challenges. Section 4.3 applies models from Section 3 to estimate the strength of bridges from their condition. Section 4.4 shows two examples of the use of the model.

# 4.1 Maintenance in the GB railway bridges 

There are 23981 bridges owned by Network Rail, brick and masonry bridge takes up around $47 \%$ of the number, while stone bridge only takes up $0.15 \% .{ }^{35}$ Given the number and variety of bridges, the burden of maintenance on railway bridges is high.

Bridges can be decomposed into major elements, such as deck, superstructure, substructure, and be further subdivided the major elements into minor elements, such as abutment, wing walls. Table 2 shows an example of elements of a masonry arch bridge presented in Rafiq et al., ${ }^{36}$ which is later used in our case study. Different types of bridges have different major and minor elements, and even when two bridges are of the same type the number of elements may vary.
[insert Table 2.]

Two types of activity are carried out to understand the state of GB rail bridges and prioritise maintenance works. Bridge examination is used to evaluate the condition of bridges. Bridge assessment is used to evaluate the bridge strength.

### 4.1.1 Bridge examination

The condition of bridges is periodically examined: the focus of examination is to determine the maintenance work needed to maintain the condition of the bridges. Two examination regimes are applied in the GB:

1) Visual examination is carried out every year to look for changes in the condition of the structure as a whole since the last examination. The condition of the structure is rated as Good, Fair or Poor. The examination also makes recommendations for maintenance work.
2) Detailed examination is carried out every 6 years and looks at all parts of the structure to determine their conditions and the extent of deterioration. This examination recommends remedial works and also the need for any additional examination of the structure. Additional examination is normally performed for hidden critical element (HCE, a structural member that cannot be observed during the examination), using a range of intrusive and non-intrusive examination methods. The condition of each part is recorded using a marking index called Structures Condition Marking Index (SCMI) ${ }^{37}$ (recently named as Bridge Condition Marking Index (BCMI)). A BCMI score ranges from 0 to 100, where ' 0 ' represents an element in extremely poor condition and ' 100 ' shows the element in perfect condition.

The uncertainty of the examination - caused by the difference between actual condition and the condition reported by an examination - varies for different types of structures and different examination regimes. Visual examination is conducted from a position of safety to report any major defects or to verify that defects already seen have been repaired. Though there is more available data from visual examination compared to detailed examination, as the former are more frequent, a visual examination determines the true condition with less certainty:

1) Defects may not be visible as it may take some time for a defect to reach a size that is observable. Another situation is some elements, such as HCE, which may have developed defects, but the visual examination did not reveal it because these elements are unobservable. The uncertainty depends on the defect types and examination quality for defects (e.g. examination procedures and engineers training). ${ }^{38}$
2) Bridge elements may have a shorter life than the overall bridge. For example, a concrete bridge may have a life of 120 years while its bearing may only have a life of 20 years as discussed in Arshad and Cook. ${ }^{39}$ Therefore, in a visual examination, it is possible that the bridge is marked as good condition even though some elements of the bridge are in poor condition when these elements do not make a visible contribution to the condition of the bridge as a whole.

# 4.1.2 Bridge assessment 

Every 18 years, following a structural inspection, an assessment of the safe load capacity (strength) of bridges is required. Three levels of structural assessment exist with increasing complexity and accuracy:

1) Level 0 reviews historical drawings of the structure and examination reports to produce an estimate of the load capability. Level 0 assessments are required to have a higher safety threshold than other levels as the assessment is the least accurate.
2) Level 1 uses static analysis to identify the load capacity of a structure, which can be used to prioritise the next assessment.

3) Level 2, as the most complex and accurate assessment, is an advanced structural analysis, uses finite element analysis based on design information and onsite inspections, estimating both static and dynamic load capacity.

# 4.1.3 Connecting bridge condition to strength 

The condition of a bridge is an indication of its strength, but with uncertainty that varies for different types of structure. Since there is data about the condition of bridges, it could be attractive to be able to use condition data to estimate strength, for example, to know when a full strength assessment was needed.

Previous studies have been proposed to estimated strength from condition. AASHTO ${ }^{40}$ used a reliability-based, load and resistance factor rating method for evaluating the strength limit states and service limit states of bridges based on condition of the bridges, bridge types and other factors. Tapan and Aboutaha ${ }^{41}$ proposed a bridge condition-rating method, which provides a good estimate of the bridge pier column strength that cannot be obtained by normal visual examination. Additionally, Wang et al. ${ }^{42}$ analysed the load-carrying capacity of a girder based on the deterioration levels of its cracks depending on the structure type and their effects on the structural integrity.

Rafiq et al., ${ }^{36}$ show that a bridge level strength can also be inferred from information about its major elements and minor elements. Experts give each minor element a factor using the BCMI system to indicate its contribution to the strength of the related major element. Then the condition of major element can be generated based on its corresponding weighted minor elements' condition. Factors are assigned in the same way to major elements for their contribution to the overall bridge strength.

### 4.2 Challenges of GB railway bridges maintenance

We have summarised the data available to plan maintenance: every year there is a visual inspection; every 6 years a detailed examination and every 18 years an assessment. How can the different types of data be combined?

1) The number of bridges of each type varies widely: as a result, some groups of assets may have lots of data, while the other have much less. The first challenge is therefore to pool data between bridges of different types.
2) The visual examination is more frequent but less accurate: the visual examination looks only at the bridge as a whole while the less frequent detailed examination looks at individual elements. The second challenge is therefore how to combine the element-level condition data with the whole structure condition data.

Condition does not inform the strength assessment: when a detailed structural assessment is available, it is clear that this provides the most accurate assessment of the structure's strength but an estimate of deterioration in strength from the condition data might allow assessment work to be prioritised. The third challenge is therefore to estimate the strength of the structure from the condition of its elements.

# 4.3 Applying BN models to estimate bridge strength from condition 

Facing these challenges, we propose a BN model framework as showed in Figure 8, assembled from the generic models from Section 3, to estimate the loss of strength of a bridge from its condition seen at examination. In the figure, the oval-shaped nodes represent variables in the BN models, the square-shaped nodes are labels: solid square labels show what type of data the nodes are using, dashed square labels indicate which section is referring to. The framework is developed with the following steps:

1) Section 4.3.1: The future condition of each element of the bridge is predicted by modelling element deterioration rates, as transitions between from Good condition to Fair condition and from Fair to Poor. The data is inferred from the detail examination, grouping data for bridges of the same class. The transition probabilities are assumed to follows a Weibull distribution. Models from Section 3.1, 3.2, 3.4 and 3.6 are used.
2) Section 4.3.2: This section examines how smaller groups of bridge, for which less data will be available, could be handled by using detailed examination data from related situations. Models from Section 3.3 and 3.5 are used.
3) Section 4.3.3: Visual examination data is added in this section: the overall condition is assumed to be indicative of the condition the elements but with varying uncertainty. Models developed from Section 3.3 and 3.6 are used.
4) Section 4.3.4: A bridge condition can be estimated by combining by the conditions of its elements, with weights representing each element's contribution on the bridge strength. Strength changes of a bridge can be inferred from its condition.

Since we are describing a model framework, the actual model will depend on the type of bridges and their elements. As an example, we consider a masonry arch bridges, for which little failure data is available.

# 4.3.1 Condition of bridge elements 

Generally, a BCMI score above 80 is considered to be in good state, below 45 is in a poor condition. Hence, we can model each element condition as a three-state variable, namely: Poor (BCMI range from 0 to 45), Fair (BCMI range from 46 to 80), and Good (BCMI range from 81 to 100). ${ }^{36}$

Two failure transitions, from Good to Fair, Fair to Poor, are modelled with an assumption that the time to failure of each transition follows a Weibull distribution. The parameters of the distribution are learnt from data, using the modelling approaches described in Section 3.1 and 3.2.

An example of the condition of one element - a wing wall - is shown in Figure 9, based the model in Section 3.6. Here wing walls asset 1, 2, 3 and the target wing walls are from different bridges that have similar designs and are constructed from the same materials, they are grouped in the same class that share the same deterioration rate. In this example, it took 62, 48 and 72 months for asset 1, 2 and 3 respectively to transit from Good to Fair and 110, 130 and 70 months more from Fair to Poor. The last examination shows this wing wall was in Good condition. Here, the variable Examination type is similar to the variable Next scheduled inspection time in Figure 7, and variable Condition of Wing Wall corresponds to the Future condition variable. In our example, the predicted probability that this wing wall stays in Good condition in its next detailed examination will be $31 \%$.
[insert Figure 9.]

# 4.3.2 Learning from different groups of assets 

Element of the same type but of different materials may share similar deterioration rate. Another situation is where the same element exposed to different environmental condition may deteriorate differently. Hence, we propose to use our models to learn deterioration rates from different groups of assets that are judged to share similar deterioration.
[insert Figure 10.]
By combining the models proposed in Section 3.3 and 3.5, for illustration purpose, two groups of assets with two types of learning for transition time from Good to Fair are presented in Figure 10. In practice, the number of group pooled may be more than 2. The

model contains typical shape and scale parameters shared between the groups and separate parameters for each group. The parameters for a group are related to the shared parameters using a TNormal distribution, allowing both changes in means and variances to be modelled. Group A and Group B, represent the same element built with different materials under the same external environment. Group A (built with masonry) has a more stable deterioration rate, while Group B (e.g. built with timber) has a more variable deterioration rate. We model this with a TNormal distribution with different variances - Group A has a smaller variance than Group B. We can also apply the same principle for their environment condition: if the bridge located in a more critical environment, it has a faster deterioration rate.

# 4.3.3 Updating from visual examination failure data 

In this section, we propose to use visual examination data as an additional data source to update the condition of each minor element that was learnt from detailed examination. As discussed in Section 4.1.2 and 4.1.3, failure data from visual examination contain more uncertainty than detailed examination, but there is more data available. To use this, we must elicit information on how accurately the visual examination result reflects the condition of each minor element using expert knowledge.

Figure 11 shows the model we use to update the condition of each element from the visual examination data. The variable Condition of bridge from visual examination is modelled using the same method we used in Section 4.2 for bridge element condition. It is learnt from visual examination data, and used to update the condition of the elements of the bridge using probability tables given by experts considering the uncertainty of visual examination and the relationship between the condition of bridge as a whole and each element. Examples of minor elements abutment and parapets are also showed in the figure, with a fragment of the

probability table in Table 3, showing how the element condition is adjusted when it is originally good.
[insert Figure 11.]
Since during the visual examination, examiners pay more attention to abutments than to parapets, so the condition of the bridge from visual examination has more influence on the abutment condition than the parapets condition. For example, when the condition of bridge from visual examination is Poor condition, the probability of abutment in Good condition will be updated from $100 \%$ to $70 \%$, while Parapets will be updated from $100 \%$ to $90 \%$ only. These are example values, which we plan to refine by interviewing examiners and reviewing the examination guideline to assess the confidence they have that the visual examination reflects the condition of each element.
[insert Table 3.]

# 4.3.4 Strength of a bridge 

A typical masonry arch bridge based on Table 2 is presented in Figure 12. Element factors (see Section 4.1.3) and their relative weighting are gathered from Rafiq et al. ${ }^{36}$ One of the major elements is 'condition of support', with minor elements abutment and wing walls. Their element factors are 10 and 5 respectively, giving relative weighting of 0.67 and 0.33 . They are combined using a weighted mean as discussed in Section 3.5, and the 'condition of support' is modelled by a truncated normal distribution with the weighted mean of abutment and wing walls, and a variance given by the experts regarding to the certainty about the element factors.
[insert Figure 12.]
The bridge strength is then calculated based on a weighted combination of its major elements and its bridge type. The conditional probability table reflects the experts' understanding of

the contribution of each element to the overall strength. By using this model, we can provide a preliminary evaluation of the bridge strength to prioritise assessment.

# 4.3.5 Assembling the models 

For our case study, a complete BN model is assembled from six minor elements, learnt from two groups of assets; the resulting model has 126 variables in total. To build such a model in general, we first need to determine the elements of the bridge type (e.g. information from Table 2) and model each as described in Section 4.3.1. Then, if the target group lacks sufficient failure data, we can look for similar groups and pool the failure data using the model of Section 4.3.2. Visual examination data is used using model from Section 4.3.3 if the detailed examination is not sufficient on its own. Finally, the model from Section 4.3.5 is applied to assemble the element condition models to assess the strength of the target bridge.

### 4.4 Examples of scenario analyses

We have shown how models built using BNs allow a variety of data to be combined. Here, we have combined BCMI data from detailed examination with overall condition data from visual examination. We can use this to estimate the future strength of the bridge and so provide practical decision support for decision makers to evaluate the effect of different examination intervals.

For example, suppose that from the latest detailed examination, the BCMI data indicates that all the elements of a masonry arch bridge are in good condition, except the parapet which is in fair condition. The model predicts with probability of $84 \%$ that the bridge will have no loss of strength in one year, at the time of the next visual examination. However, a prediction for the next detailed examination, after a further 6 years, gives a probability of $22 \%$ for good strength, and $66 \%$ for fair strength.

[insert Figure 13.]

We can use these predictions to evaluate the effects of different examination regime and to modify examination intervals. We can also use the model to estimate if an intervention is needed in order to ensure the strength of a bridge is maintained above a certain level. Figure 13 shows an example of strength limit (black line), representing a probability of at least $40 \%$ that this bridge is in good strength; below this intervention is needed. In this example, we would suggest that detailed examination after a 5-year interval is safer than the full 6-year interval in order to avoid falling below the threshold probability of good strength. Another advantage of using BN models is that we can reason backwards to evaluate intervention plans given a target. For example, we can set the bridge's strength to the limit and analyse the element conditions that result. When an element is already close to this condition, we can prioritise it for maintenance.

# 5 Conclusions 

We have proposed generic BN models that can be combined to reason about the deterioration of assets from data likely to be available and from and expert knowledge in practical maintenance planning. These models can be selected and assembled according to what kind of data is available, guided by expert knowledge in a particular case. An example tailored for GB railway bridges maintenance is presented to estimate bridge strength from condition.

### 5.1 Summary

This paper presents an asset deterioration model for maintenance planning using BN models. The core of the model uses a Weibull distribution to model asset deterioration in a

hierarchical BN. The transition times between a small number of conditions are assumed to be drawn from Weibull distributions, whose parameters are learned using historical data. To complete the hierarchical model, prior probabilities need to be assigned to the hyperparameters. The shape parameter can model an increasing, constant or decreasing failure rate, while the scale parameter stretches out the probability density function. By understanding the characteristics of these two parameters, we argue that reasonable priors could be determined in discussion with experts.

We may have a group of related asset types that deteriorate with similar behaviour, with a lot of data for some types, while others have little. We extend the model to learn from related assets. Further expert judgement of the degree of similarity between the groups is needed at this stage. We also extend the model to make the most use of available data, which do not necessary include the exact times that each asset transitioned from one state to another. Then, to distinguish individual assets within a broad class of similar assets, we allow experts to quantify the effect of factors such as loadings and environmental conditions to adjust the predicted deterioration of a specific asset. This expert knowledge could be replaced by parameters learned from data if it were available.

Finally, we show how the different generic BN models can be combined and used for GB rail bridges maintenance planning. A case study is presented using realistic types of data and knowledge that can be exploited from experts. Examples of how to use the proposed models for maintenance planning were discussed.

# 5.2 Future Work 

Further work is needed to validate the approach using real datasets and for real maintenance scenarios. We wish to extend the model further to incorporate costs, including disruption, of

different maintenance actions, so that we can schedule an optimum hierarchy of maintenance actions.

Though our models provide the feasibility and structures of how to include expert knowledge to improve the models, the procedure for knowledge elicitation needs further investigation. Process of how to acquire knowledge from experts for decision analysis have been proposed by many researchers, such as Cooke's classical method. ${ }^{15}$ Another challenge is how to incorporate opinions when multiple experts are involved, which could be handled in two ways: combine the assessment of each expert into a single one, or hold a workshop for experts to come to a consensus. ${ }^{43}$

We also plan to study the computational performance of the model, especially for significant quantities of data. Experience to date shows that it is adequate and some optimisations to the model structure are likely to yield improvements. Fortunately, maintenance decision making does not require instant answers and there are a great variety of BN inference algorithms offering different trade-offs between speed and accuracy.

As we have shown in Section 4, the way that the different modelling stages are combined reflects the needs of a particular scenario. To make this practical, we plan to develop a higher-level interface in which the maintenance-related information (such as the number of conditions, the maintenance actions etc.) could be described and from which the necessary BN could be generated automatically.

# Acknowledgements 

We would like to thank the anonymous reviewers and the editor for their insightful comments. This work is supported by the European Research Council (ERC-2013-AdG339182-BAYES-

KNOWLEDGE) for funding, and Agena Ltd for software support. The first author is supported by China Scholarship Council (CSC)/Queen Mary Joint PhD scholarships.
