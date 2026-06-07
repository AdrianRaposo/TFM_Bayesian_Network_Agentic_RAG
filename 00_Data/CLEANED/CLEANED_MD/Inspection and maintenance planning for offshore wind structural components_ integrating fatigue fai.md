# Inspection and maintenance planning of offshore wind structural components: Integrating fatigue failure criteria with Bayesian networks and Markov decision processes 

Nandar Hlaing ${ }^{\mathrm{a}^{*}}$, Pablo G. Morato ${ }^{\mathrm{a}}$, Jannie S. Nielsen ${ }^{\mathrm{c}}$, Peyman Amirafshari ${ }^{\mathrm{b}}$, Athanasios Kolios $^{\mathrm{b}}$ and Philippe Rigo ${ }^{\mathrm{a}}$<br>${ }^{a}$ Naval \& Offshore Engineering, ArGEnCo, University of Liege, Liege, Belgium; ${ }^{\mathrm{b}}$ Department of Naval Architecture, University of Strathclyde, Glasgow, United Kingdom; ${ }^{\text {c }}$ Department of the Built Environment, Aalborg University, Aalborg, Denmark

## ARTICLE HISTORY

Compiled January 28, 2022


#### Abstract

Exposed to the cyclic action of wind and waves, offshore wind structures are subject to fatigue deterioration processes throughout their operational life, therefore constituting a structural failure risk. In order to control the risk of adverse events, physics-based deterioration models, which often contain significant uncertainties, can be updated with information collected from inspections, thus enabling decision-makers to dictate more optimal and informed maintenance interventions. The identified decision rules are, however, influenced by the deterioration model and failure criterion specified in the formulation of the pre-posterior decisionmaking problem. In this paper, fatigue failure criteria are integrated with Bayesian networks and Markov decision processes. The proposed methodology is implemented in the numerical experiments, specified with various crack growth models and failure criteria, for the optimal management of an offshore wind structural detail under fatigue deterioration. Within the experiments, the crack propagation, structural reliability estimates, and the optimal policies derived through heuristics and partially observable Markov decision processes (POMDPs) are thoroughly analysed, demonstrating the capability of failure assessment diagram to model the structural redundancy in offshore wind substructures, as well as the adaptability of POMDP policies.


## KEYWORDS

Offshore wind turbines; Inspection and maintenance planning; Fracture mechanics; Failure criteria; Failure assessment diagram; Partially observable Markov decision processes

## 1. Introduction

An optimal and rational management of offshore wind substructures is becoming increasingly important due to the growth of offshore wind installations, with a trend towards larger wind turbines, often located far offshore. Exposed to harsh marine environmental conditions, the degradation of offshore wind substructures is accentuated, thus inducing a risk of structural failure. Additionally, inspection and maintenance interventions may become more complex and expensive far offshore. In this context, inspection and maintenance (I\&M) planning methods offer a framework for minimising life-cycle costs, controlling structural failure risks by optimally allocating inspections and maintenance actions.

Already in the 1990s, early I\&M planning methods address the decision-making problem by exploiting Bayesian decision analysis with the objective to identify optimal strategies for structures subjected to fatigue deterioration (Fujita, Schall, \& Rackwitz, 1989; Madsen, Sørensen, \&

[^0]
[^0]:    ${ }^{a}$ CONTACT Nandar Hlaing Email: nandar.hlaing@uliege.be

Olesen, 1990), with many applications focused on I\&M planning for offshore structures (Faber, Sørensen, \& Kroon, 1992; Goyet, Maroini, Faber, \& Paygnard, 1994). By defining the I\&M policies based on a set of predefined decision rules, the computational complications associated with solving an extensive pre-posterior analysis were alleviated, enabling the identification of rational strategies within a reasonable computational time (Straub, 2004; Straub \& Faber, 2006). Heuristic-based I\&M planning methods have been widely applied to the management of fatiguesensitive structures, planning inspections at periodic intervals or immediately after a specified failure probability threshold is exceeded (Moan, 2005; Straub \& Faber, 2005). More recently, the integration of discrete dynamic Bayesian networks (DBNs) into I\&M methodologies has enabled the efficient evaluation of more sophisticated heuristic decision rules (Nielsen \& Sørensen, 2018). For instance, Luque and Straub (2019) has proposed an I\&M planning approach for structural systems, evaluating system-level heuristic decision rules in a DBN simulation environment. Other existing I\&M research works consider multiple conflicting objectives within the policy optimisation (Frangopol \& Kim, 2019; Soliman, Frangopol, \& Mondoro, 2016), planning maintenance actions, in some cases, based on specified thresholds (Kim, Ge, \& Frangopol, 2019). Relying also on dynamic Bayesian networks, single- and multi-objective optimisation methods provide robust Bayesian inference and enable the evaluation of advanced decision rules, e.g. adaptive repair thresholds (Yang \& Frangopol, 2018). Through multi-objective policy optimisation methods, decision-makers can operate under budget constraints and/or control maintenance delays.

Even if heuristic decision rules alleviate the computational complexity of the I\&M decisionmaking problem, as mentioned before, the obtained I\&M strategies are constrained by the number of evaluated pre-defined rules out of the vast available policy space. Instead, I\&M planning methods that rely on Markov decision processes determine adaptive policies, providing a mapping from the dynamically updated deterioration state to the optimal actions. Various I\&M planning applications for deteriorating structures modelled the decision-making problem via Markov decision processes, e.g. (Corotis, Ellis, \& Jiang, 2005; Memarzadeh \& Pozzi, 2016; Robelin \& Madanat, 2007). The benefits offered by adaptive I\&M policies are substantiated by Yang and Frangopol (2022), and Morato, Papakonstantinou, Andriotis, Nielsen, and Rigo (2022) have demonstrated that partially observable Markov decision process (POMDP) solved via point-based algorithms can efficiently determine optimal I\&M policies. An overview of state-of-the-art point-based solvers and their applicability to infrastructure management can be found in Papakonstantinou, Andriotis, and Shinozuka (2017).

As explained before, I\&M planning methods aim at controlling arising structural failure risks by timely allocating inspection and maintenance actions. Essentially, the failure risk of a structural component represents both the probability of a failure event and its associated economic, societal, and environmental consequences. The estimation of the failure probability is governed by a failure criterion, which is specified by the decision-maker. Within the context of fatigue deteriorating structures, a through-thickness failure criterion is normally prescribed, e.g. asset management of offshore pipelines and containers. This conventional criterion might be over-conservative for redundant structures such as the tubular joints of jacket-type offshore wind turbines (OWTs), as tubular connections have the capacity to sustain through-thickness cracks until the loading exceeds the resistance of the cracked structure. In such applications, the fatigue failure limit state can be, instead, formulated via a failure assessment diagram (FAD).

The failure assessment diagram, originally proposed by Dowling and Townley (1975) and Harrison, Milne, and Gray (1981), describes the interaction between brittle fracture and plastic failure through a two-parameter failure criterion. The specification of FAD as the governing failure criterion has recently gained attention in offshore wind applications. Among them, Fajuyigbe and Brennan (2021) and Mai, Sørensen, and Rigo (2016) showcased the evaluation of flaw acceptability in offshore wind support structures using a failure assessment diagram of BS7910 (British Standards, 2015). In parallel with the reported FAD research work, several probabilistic fatigue studies and I\&M planning methods for offshore wind substructures have still specified fatigue limit states based on the conventional through-thickness failure criterion, potentially drawing over-conservative conclusions.

In the reported I\&M planning methods that formulate the fatigue failure limit state via a failure assessment diagram (Amirafshari, Brennan, \& Kolios, 2021; Hlaing et al., 2020), the identified I\&M policies are, however, based on heuristic decision rules. In this paper, we originally integrate the modelling of stochastic fatigue deterioration processes and the specification of FAD-based limit states via dynamic Bayesian networks, and we introduce the necessary formulation for modelling the overarching I\&M decision-making problem as a partially observable Markov decision process (POMDP). The proposed method is flexible and can be easily adopted by other applications whose limiting failure criterion is also defined as a function of multiple failure parameters. The applicability and efficacy of the proposed approach is verified through numerical experiments, in which optimal I\&M strategies are determined for the specific case of an offshore wind tubular joint. Within the numerical experiments, the fatigue deterioration of offshore wind structural details is modelled by one-dimensional and two-dimensional fracture mechanics methods as well as various failure criteria, thoroughly investigating the effect of model selection on the identified I\&M strategies. The results reveal that the choice of failure criteria and the optimality of the implemented I\&M planning methods significantly affect the resulting I\&M policies. In particular, the benefits of adopting FAD criteria for offshore wind substructures and the cost savings provided by POMDP-based policies are both meticulously discussed.

# 2. Background: Risk-based inspection and maintenance planning 

Risk-based inspection and maintenance planning is based on pre-posterior decision analysis integrated with deterioration modelling, inspection and repair modelling, and cost modelling. This section presents deterioration modelling including failure criteria and inspection modelling. Cost modelling along with policy optimisation methods is discussed in Section 4. The probabilistic fatigue deterioration model is used as reference and fracture mechanics models are calibrated to the fatigue model. The through-thickness failure criterion has been commonly used in the I\&M planning of offshore wind structures (Luque \& Straub, 2016; Morato, 2021). In this paper, the failure assessment diagram criterion is also addressed and integrated into I\&M planning. Procedures to obtain a FAD and failure assessment points are also presented.

### 2.1. Deterioration modelling

### 2.1.1. Probabilistic SN model

Offshore wind turbine support structures are subjected to a large number of environmental load cycles (e.g. waves) and other operational loading in their lifetime. For such structures, the long-term stress range distribution can be represented by a Weibull distribution, described by a scale parameter $q$ and a shape parameter $h$. The shape parameter $h$ for offshore wind (OW) substructures as recommended by DNV standards (DNV, 2019) is 0.8 and the scale parameter $q$ is computed such that the cumulative lifetime damage of the structural component designed for $T_{d}$ years is equivalent to the damage limit corrected by the fatigue design factor $(F D F)$, i.e. $D_{S N}\left(t=T_{d}\right)=1 / F D F$ where the temporal fatigue evolution $D_{S N}$ is defined as:

$$
D_{S N}(t)=n t\left[\frac{q^{m_{1}}}{k_{1}} \gamma_{1}\left(1+\frac{m_{1}}{h} ;\left(\frac{S_{1}}{q}\right)^{h}\right)+\frac{q^{m_{2}}}{k_{2}} \gamma_{2}\left(1+\frac{m_{2}}{h} ;\left(\frac{S_{1}}{q}\right)^{h}\right)\right], t=0,1, \ldots T_{d}
$$

$m_{1}, m_{2}, k_{1}, k_{2}, S_{1}$ are parameters of the bi-linear SN curve. $n$ is the number of stress cycles per year. $\gamma_{1}$ and $\gamma_{2}$ are the upper and lower incomplete gamma functions.

Probabilistic fatigue analysis can then be based on Palmgren-Miner's rule with the long-term

stress range distribution. The limit state function applied in the fatigue deterioration model is:

$$
g_{S N}(t)=\Delta-D_{S N}(t)
$$

where $\Delta$ is the fatigue limit beyond which failure happens and is considered as a random variable owing to the uncertainty of Palmgren-Miner's rule. $D_{S N}(t)$ is the accumulated fatigue damage at year $t$ calculated as in Equation (1).

The design of offshore structures is based on SN curves but the inspection information, i.e. the presence of crack or the crack size measurement, cannot be directly used to update the SN-based reliability. Inspection and maintenance planning therefore demands the use of fracture mechanics (FM) models. Different FM models are described in Section 2.1.2. It becomes necessary to relate the two deterioration models and such a relation can be attained by calibrating the FM models to the SN model which includes all the information from the design stage. The calibration is performed such that a similar fatigue life is calculated by fracture mechanics models as that of S-N test data. Whereas the FM models compute the crack growth, the only information that contains in the SN model is the failure or survival of the hotspot through fatigue damage. Therefore, the calibration between SN and FM models has been based on the probability of failure along the lifetime (DNV, 2019). Typically, FM parameters with the largest influence on the crack growth and/or with the least available information are calibrated (Straub, 2004).

# 2.1.2. Fracture mechanics models 

Two-dimensional crack growth model
![img-0.jpeg](img-0.jpeg)

Figure 1.: Illustration of fatigue crack initiation.
In offshore wind support structures, fatigue cracks initiate from manufacturing imperfections and welding defects as illustrated in Figure 1. The severity increases over the time as the cracks grow under the cyclic loading of wind and waves. Paris-Erdogan's law has been widely used in linear elastic fracture mechanics (LEFM) to model the crack growth (Paris \& Erdogan, 1963):

$$
\begin{aligned}
& \frac{d}{d n} d=C_{d}\left(\Delta K_{d}\right)^{m} \\
& \frac{d}{d n} c=C_{c}\left(\Delta K_{c}\right)^{m}
\end{aligned}
$$

where $d$ is the crack depth growing through the thickness of the structural member and $c$ is the crack length growing along the surface. $n$ corresponds to the number of stress cycles. $C_{d}, C_{c}$ and $m$ are Paris law parameters, also called crack growth parameters and $\Delta K$ is the stress intensity

factor range at the crack tip calculated as:

$$
\begin{aligned}
& \Delta K_{d}=\Delta \sigma Y_{d}(d, c) \sqrt{\pi d} \\
& \Delta K_{c}=\Delta \sigma Y_{c}(d, c) \sqrt{\pi d}
\end{aligned}
$$

$Y_{d}$ and $Y_{c}$ are stress intensity correction factors and theoretically, are dependent on the geometry of the component, welded joint detail and time-varying two-dimensional crack size. The applied stress range $\Delta \sigma$ is assumed to be composed of membrane and bending stress components. The two components are quantified by the ratio of bending stress to total stress, denoted as the degree of bending $D_{b}$. Stress concentration due to weld geometry is also incorporated as the stress magnification factor $M_{k}$. The stress intensity factor ranges can then be described as:

$$
\begin{aligned}
& \Delta K_{d}=\Delta \sigma\left[Y_{m d} M_{k m d}\left(1-D_{b}\right)+Y_{b d} M_{k b d} D_{b}\right] \sqrt{\pi d} \\
& \Delta K_{c}=\Delta \sigma\left[Y_{m c} M_{k m c}\left(1-D_{b}\right)+Y_{b c} M_{k b c} D_{b}\right] \sqrt{\pi d}
\end{aligned}
$$

The subscripts $d, c$ refer to crack depth and crack length and $m, b$ refer to membrane and bending stress components respectively. Geometry functions $Y_{m d}, Y_{b d}, Y_{m c}, Y_{b c}$ and stress magnification factors $M_{k m d}, M_{k b d}, M_{k m c}, M_{k b c}$ can be solved by using parametric equations, for instance, as in BS7910 (British Standards, 2019). Alternatively, one can perform finite element analysis of the cracked structure and directly compute the stress intensity factors $K_{d}$ or $K_{c}$ at each stress cycle (Fajuyigbe \& Brennan, 2021).

# One-dimensional crack growth model 

In the one-dimensional fracture mechanics model, the crack propagation is considered only in the direction of the member's thickness. Therefore, the stress intensity correction factor $Y_{d}$ simply becomes a function of crack depth only. Additionally, if it is further simplified such that the stress intensity correction factor $Y_{d}$ does not depend on the time-varying crack depth and is approximated as a constant value over the lifetime, an explicit solution of the crack growth can then be obtained as follows:

$$
d(t)=\left[\left(1-\frac{m}{2}\right) C_{d} Y_{d}^{m} \pi^{m / 2}(\Delta \sigma)^{m} n+d_{t-1}^{1-m / 2}\right]^{(1-m / 2)^{-1}}
$$

Through this simplification, the crack propagation can be analytically computed attenuating the computation associated to solving the coupled equations. For small cracks situated far away from the boundaries of the structural member, $Y_{d}$ can be taken as 1 with sufficient accuracy (Ditlevsen \& Madsen, 2007). In probabilistic deterioration modelling, $Y_{d}$ is assigned as a timeinvariant random variable to introduce the model uncertainties associated to the simplifications of the stress intensity correction factor (JCSS, 2011).

### 2.1.3. Failure criteria

## Through-thickness failure criterion

As illustrated in Figure 1, a crack grows both through the thickness and along the surface of the structural component taking a semi-elliptical shape. Assuming that the thickness is smaller than the length and the width of the member, the crack is likely to penetrate the whole thickness first. The failure criterion can be formulated depending on the capacity of the structure to further resist the applied load after through-thickness penetration.

In the through-thickness criterion, the failure happens when the crack depth reaches the thickness of the structural member which is also denoted as the critical crack size $d_{\text {crit }}$. This common criterion is particularly adopted for structures containing pressurised containment, e.g. pipelines, pressure vessels, etc. and is conservative for redundant structures such as OW jacket foundations. The following limit state function is employed for the through-thickness failure:

$$
g_{F M}(t)=d_{\text {crit }}-d(t)
$$

in which $d(t)$ is the crack propagation over time. The probability of failure $P_{F}(t)$ is then the probability of the limit state function being negative such that $P_{F}(t)=P\left(g_{F M}(t) \leq 0\right)$.

# Failure assessment diagram 

When a crack propagates through a structural member, ultimately the crack size may reach a critical size which corresponds to a critical stress intensity factor, usually taken as the characteristic value of the fracture toughness $K_{\text {mat }}$ at which brittle fracture happens. Alternatively, if the applied load is substantially high compared to the material tensile strength, the member may reach its tensile capacity and fail by plastic collapse. In between brittle fracture and plastic collapse is an elastoplastic failure mode, where the failure occurs before reaching the plastic capacity or fracture toughness. The failure assessment diagram was therefore introduced to combine the two failure modes (Dowling \& Townley, 1975).

The most rigorous method to obtain a FAD for a particular application is to perform an elastic-plastic J-integral analysis (Anderson, 2005). Since it can be cumbersome, simplified approximations are available. For instance, BS7910 (British Standards, 2019) provide three alternative FAD options which have been frequently used in offshore wind applications (Fajuyigbe \& Brennan, 2021; Mai et al., 2016). They are of increasing complexity in terms of the required material properties and stress analysis data but also provide results of increasing accuracy with less conservatism. An example of the FAD is plotted in Figure 2.

In a FAD, the ordinate plots the fracture ratio $K_{r}$, also called the crack-driving parameter which represents the structure's susceptibility to brittle fracture. The abscissa plots the load ratio $L_{r}$ which measures how close the structure containing the crack is to plastic collapse. The load ratio $L_{r}$ is equal to 1 at the yield limit, however plastic collapse happens at a higher value which is equal to $L_{r, \max }$. The failure of a structural component is then defined by means of a failure assessment line (FAL). If an assessment point lies inside the envelope below the assessment line, the component is assumed to be safe. If it falls on or outside the FAL, it is assumed to be failed. The failure assessment line (FAL) is in fact a plot of the critical values of fracture ratio $K_{r, \text { crit }}$ for a range of load ratio, i.e. $0 \leq L_{r} \leq L_{r, \text { max }}$. The cut-off value for plastic collapse $L_{r, \text { max }}$ according to BS7910 (British Standards, 2019) is:

$$
L_{r, \max }=\frac{\sigma_{Y}+\sigma_{U}}{2 \sigma_{Y}}
$$

where $\sigma_{Y}$ and $\sigma_{U}$ are the design yield strength and ultimate strength of the material used. $K_{r, \text { crit }}$ is equal to 1 for fully brittle fracture and declines as the load ratio increases towards the collapse load as in Figure 2. In addition, as it is illustrated, the FAD can be partitioned into three different zones: Zone I is the fracture dominant zone, Zone II is the elastoplastic zone and Zone III is the plastic collapse dominant zone (Hlaing et al., 2020).

When the FAD is used as a limit state function, the failure occurs when the applied load exceeds the reduced capacity of the cracked structure. It becomes necessary to consider the combined influence of applied loads and non-monotonic strength deterioration of the cracked structure. Therefore, evaluation of the failure probability with a FAD requires to apply timevariant reliability methods which are extremely time-consuming. Instead, a simplified criterion proposed by JCSS (2011) has been used in this work as an alternative to FAD. In this case, the failure is expected if the interaction of the crack-driving parameter $K_{r}$ and the load ratio

![img-1.jpeg](img-1.jpeg)

Figure 2.: Failure assessment diagram (British Standards, 2019) and the simplified criterion (JCSS, 2011).

L<sup>r</sup> exceeds a normalised resistance parameter R<sup>f</sup>, see Figure 2. The concept of the normalised resistance parameter and the recommended values are described in Dijkstra (1991) and JCSS (2011). Then, the limit state equation and assessment points K<sup>r</sup> and L<sup>r</sup> are reformulated as:

$$g_{FM}(t) = R_f - \sqrt{K_r^2(t) + L_r^2(t)}\tag{12}$$

$$K_r = \frac{K_I}{K_{mat}} + \rho, \qquad L_r = \frac{\sigma_{ref}}{\sigma_Y} \tag{13}$$

where R<sup>f</sup> is the normalised resistance parameter. K<sub>mat</sub> is the fracture toughness of the material. K<sup>I</sup> is the stress intensity factor at the crack tip and can be computed for a particular crack size as follows:

$$K_I = \sigma Y_d(d, c) \sqrt{\pi d} \tag{14}$$

where σ is the maximum applied stress. The plasticity correction factor ρ ≥ 0 reflects the interaction between the applied primary loads and the secondary loads, e.g. residual stress R<sub>s</sub>. Plasticity correction is important when the secondary loads are high which, for example, is the case of welded joints. In such case, ρ increases as the crack size becomes larger, representing the reduced load carrying capacity of the deteriorated structure driven by plasticity interaction effects. The plasticity correction can be evaluated according to the procedures in JCSS (2011) or British Standards (2019). σ<sub>Y</sub> is the material's yield stress and σ<sub>ref</sub> is the net section stress or reference stress of the cracked structure. For a surface crack at the weld toe, σ<sub>ref</sub> can be evaluated as in the following equation (British Standards, 2019).

$$
\begin{aligned}
& \sigma_{\text {ref }}=\frac{\left(D_{b} \cdot \sigma\right)+\left(\left(D_{b} \cdot \sigma\right)^{2}+9\left(\left(1-D_{b}\right) \cdot \sigma\right)^{2}\left(1-\mu^{\prime \prime}\right)^{2}\right)^{0,5}}{3\left(1-\mu^{\prime \prime}\right)^{2}} \\
& \text { where } \mu^{\prime \prime}= \begin{cases}\frac{(d / t)}{1+(t / c)}, & \text { if } W \geq 2(c+t) \\
\frac{2 d}{t} \frac{c}{W}, & \text { if } W<2(c+t)\end{cases}
\end{aligned}
$$

where W and t are the width and the thickness of the structural member.

# 2.2. Inspection modelling 

![img-2.jpeg](img-2.jpeg)

Figure 3.: Probability of detection, adapted from signal response method (Chung et al., 2006). The mean values of the signal response fall on a regression line with the regression parameters $\beta_{0}$ and $\beta_{1} . \varepsilon$ is associated with variability of imperfect inspection and is assumed normally distributed with a zero mean and a standard deviation $\sigma_{\varepsilon}$.

The information gathered during the operational lifetime can be used to update the uncertainties in the deterioration model. For instance, the probability distribution of the crack size can be updated after an inspection is performed. However, it is necessary to take into account the measurement quality of the observation model. The probability of detection $(P O D)$ curves have been adopted to characterise the quality of several non-destructive inspection techniques such as ultrasonic testing (UT), magnetic particle inspection (MPI) and Eddy current (EC) inspection (Berens \& Hovey, 1981). The $P O D$ depends on the crack size and the detection threshold, as illustrated in Figure 3. A signal response above the detection threshold will give an inspection outcome of crack detection and below the threshold results in a no-detection outcome. Accordingly, the $P O D$ is defined in detection theory (Macmillan \& Creelman, 2004) as

follows:

$$
P O D(d)=\int_{\hat{d}_{s, t h}}^{+\infty} f_{\text {signal }}\left(\hat{d}_{s} \mid d\right) d \hat{d}_{s}
$$

where $d$ is the true crack size. $\hat{d}_{s, t h}$ is the detection threshold and $f_{\text {signal }}$ is the probability density function of the signal response $\hat{d}_{s}$. Given the regression parameters $\beta_{0}, \beta_{1}$ and the variability $\sigma_{\varepsilon}$ of an inspection technique, Equation (16) can be derived as:

$$
P O D(d)=1-\Phi\left(\frac{\hat{d}_{s, t h}-\left(\beta_{0}+\beta_{1} \cdot \ln (d)\right)}{\sigma_{\varepsilon}}\right)
$$

where $\Phi$ is the cumulative distribution function of the standard normal distribution. For a particular detection threshold $\hat{d}_{s, t h}$, the theoretical probability of detection curve according to Equation (17) is a monotonically increasing function of the crack size. Adjusting the detection threshold $\hat{d}_{s, t h}$, the shape of a $P O D$ curve can be changed so that $P O D=1$ when $\hat{d}_{s, t h} \rightarrow-\infty$ and $P O D=0$ when $\hat{d}_{s, t h} \rightarrow \infty$ for any crack size. Based on Hong (1997) and Straub (2004), the following limit state function is used for the event of crack detection at time $t$ :

$$
g_{D}(t)=u-P O D(d(t))
$$

where $u$ is a uniformly distributed random variable in the interval $[0,1]$. The $P O D$ of the crack depth at time $t$ is computed according to Equation (17).

The additional information obtained from inspections can be used to update the reliability through conditional failure probability (Lotsberg, Sigurdsson, Fjeldstad, \& Moan, 2016). For instance, given no-detection outcome of inspection at year $t_{\text {ins }}$, the updated failure probability for $t \geq t_{\text {ins }}$ is:

$$
P_{F}(t)=P\left(g_{F M}(t) \leq 0 \mid g_{D}\left(t_{\text {ins }}\right)>0\right)=\frac{P\left(g_{F M}(t) \leq 0 \cap g_{D}\left(t_{\text {ins }}\right)>0\right)}{P\left(g_{D}\left(t_{\text {ins }}\right)>0\right)}
$$

# 3. Stochastic deterioration modelling through dynamic Bayesian networks 

Bayesian networks (BN), introduced by (Pearl, 1988), is a graphical formalism to represent joint probability distributions of a set of random variables. Dynamic Bayesian networks (DBNs) are temporal repetitions of BNs which have been increasingly used in engineering structural reliability and risk analysis (Nielsen \& Sørensen, 2018; Straub, 2009; Zhu \& Collette, 2015). To implement DBNs in I\&M planning, the continuous random variables involved in the deterioration model need to be discretised for prediction and exact inference tasks. This step is crucial since the accuracy of the results and the computational efficiency are influenced by the number of intervals and the discretised boundaries. Theoretically, the discretisation error tends to 0 as the size of the intervals approaches 0 . In practical applications, the discretisation scheme is preferred to provide sufficient accuracy with maximum computational efficiency.

The state space $\mathcal{S}$ in DBNs is the domain of the discretised variables. In a stochastic deterioration process, the belief which is the probability distribution over the state space $P\left(s_{t}\right)$ transitions from one time step to the next one according the conditional probability $P\left(s_{t+1} \mid s_{t}\right)$, also denoted as the transition matrix. Markovian property is assumed here, i.e. the state at time $t+1$ depends only on the state at $t$ and not on the past ones. Additionally, the transition matrix is time-invariant meaning that $P\left(s_{t+1} \mid s_{t}\right)$ is the same for any two consecutive time steps. Evidence from observations (e.g. inspections) can also be incorporated through Bayes' rule such

that:

$$
P\left(s_{t+1} \mid \boldsymbol{o}_{\boldsymbol{t}+\mathbf{1}}\right) \propto P\left(\boldsymbol{o}_{\boldsymbol{t}+\mathbf{1}} \mid s_{t+1}\right) P\left(s_{t+1}\right)
$$

whereas the likelihood $P\left(\boldsymbol{o}_{\boldsymbol{t}+\mathbf{1}} \mid s_{t+1}\right)$ quantifies the quality of the observation.

# 3.1. Deterioration rate DBNs adopting a through-thickness criterion 

Dynamic Bayesian networks (DBNs) have been frequently used to model engineering deterioration processes in risk analysis, often through combination of random variables to reduce the dimension of the state space and the computation time (Straub, 2009). When more complex deterioration model and failure criterion are used, the state space becomes high-dimensional and non-combinative, e.g. the Weibull scale parameter $q$ cannot be combined with other variables since the crack size is conditional on it (through $\Delta \sigma$ ) and so are the failure assessment points $K_{r}$ and $L_{r}$ (through $\sigma$ ). In addition, the necessity of high-dimensional conditional probabilities for propagating the belief and computing the failure probability, such as $P\left(d_{t+1} \mid d_{t}, c_{t}, q, C_{a}\right)$, $P\left(c_{t+1} \mid d_{t}, c_{t}, q, C_{c}\right), P\left(K_{r, t} \mid d_{t}, c_{t}, q, K_{\text {mat }}, R_{s}\right), P\left(L_{r, t} \mid d_{t}, c_{t}, q, \sigma_{Y}\right), P\left(g_{F M} \mid L_{r}, K_{r}, R_{f}\right)$ increases computational complexity.

Another DBN representation, denoted here as "deterioration rate" DBN, represents a stochastic deterioration process as a function of the deterioration rate. The graphical representation of such DBNs adopting a through-thickness criterion is shown in Figure 4. The crack evolution is traced by the nodes $d_{t}$ and is dependent on the deterioration rate $\tau_{t}$. The node $\tau_{t}$ is a one-hot (one-zero) vector indicating the current deterioration rate. Unless any maintenance action is taken, it transitions one deterioration rate, i.e. $\tau_{i}$ to $\tau_{i+1}$, at every time step. Note that the component may have the same deterioration rate for different time steps in the lifetime. For example, the crack may return to its initial deterioration rate $\tau_{0}$ after a perfect repair or jump a number of deterioration rate back after an imperfect repair. The inspection model is considered within the observation nodes $\boldsymbol{o}_{\boldsymbol{t}}$. The nodes $F_{t}$ indicate the probability of failure. In the through-thickness failure criterion, $F_{t}$ is dependent only on the crack size $d_{t}$. The failure subspace $\mathcal{S}_{F} \subseteq \mathcal{S}$ is therefore defined based on the discretisation scheme of $d_{t}$ to compute the failure probability.
![img-3.jpeg](img-3.jpeg)

Figure 4.: Deterioration rate DBNs adopting a through-thickness criterion. The nodes $d_{t}$ describe the crack evolution dependent on the deterioration rate $\tau_{t}$. The nodes $\boldsymbol{o}_{\boldsymbol{t}}$ represent the imperfect observations (inspections) conditional on $d_{t}$, and $F_{t}$ indicates the probability of a failure event.

The initial belief $\mathbf{b}_{\mathbf{0}}(s)$ corresponds to a joint probability distribution of the initial crack size and deterioration rate $P\left(d_{0}, \tau_{0}\right)$. The belief transitions from each time step $t$ to the next

$t+1$ according to the predefined conditional matrix as follows:

$$
P\left(d_{t+1}, \tau_{t+1} \mid \boldsymbol{o}_{\mathbf{0}}, \ldots, \boldsymbol{o}_{\boldsymbol{t}}\right)=\sum_{d_{t}} \sum_{\tau_{t}} P\left(d_{t+1}, \tau_{t+1} \mid d_{t}, \tau_{t}\right) P\left(d_{t}, \tau_{t} \mid \boldsymbol{o}_{\mathbf{0}}, \ldots, \boldsymbol{o}_{\boldsymbol{t}}\right)
$$

When the evidence is available, the estimation of the updated belief can be done through the normalisation of:

$$
P\left(d_{t+1}, \tau_{t+1} \mid \boldsymbol{o}_{\mathbf{0}}, \ldots, \boldsymbol{o}_{\boldsymbol{t}+\mathbf{1}}\right) \propto P\left(\boldsymbol{o}_{\boldsymbol{t}+\mathbf{1}} \mid d_{t+1}\right) P\left(d_{t+1}, \tau_{t+1} \mid \boldsymbol{o}_{\mathbf{0}}, \ldots, \boldsymbol{o}_{\boldsymbol{t}}\right)
$$

# 3.2. Deterioration rate DBNs adopting a FAD criterion 

![img-4.jpeg](img-4.jpeg)

Figure 5.: Deterioration rate DBNs adopting a FAD criterion. The nodes $d_{t}$ describe the crack evolution dependent on the deterioration rate $\tau_{t}$. The nodes $\boldsymbol{o}_{\boldsymbol{t}}$ represent the imperfect observations (inspections) conditional on $d_{t}$, and $F_{t}$ indicates the probability of a failure event through the nodes $g_{F M t}$.

A method to implement a FAD criterion in deterioration rate DBNs is presented here. The DBN model with the FAD criterion is illustrated in Figure 5. In this case, the probability of a failure event cannot be obtained only from the nodes $d_{t}$ since it requires the crack length as well as other time-invariant variables $\sigma_{Y}, K_{\text {mat }}, R_{s}, R_{f}$ to evaluate the failure. Alternatively, one can include additional nodes $g_{F M t}$, denoted here as the limit state variable and computed from Equations (12-15) in the DBNs to allow the direct estimation of the failure probability $F_{t}$. In this I\&M planning problem, the observation nodes $\boldsymbol{o}_{\boldsymbol{t}}$ are conditional on the crack depth and the nodes $d_{t}$ still need to be tracked. Therefore, the belief space $\mathbf{b}_{\mathbf{0}}(s)$ becomes a joint distribution of the deterioration rate, the crack size and the limit state variable $P\left(d_{t}, \tau_{t}, g_{F M t}\right)$.

The deterioration evolution over the subsequent time steps can be computed through transition and estimation steps. However, the computational complexity significantly increases due to the larger state space size with this failure criterion. The transition of the crack length has been implicitly considered in the DBNs through the nodes $g_{F M t}$. If the component returns to its initial belief $P\left(\tau_{0}, d_{0}, g_{F M 0}\right)$ after the perfect repair, both the crack depth and the crack length consistently return to the initial condition.

# 4. Policy optimisation methods 

### 4.1. IEM planning through heuristics

The objective of I\&M planning is to identify the optimal inspection strategy which provides the minimum total expected cost $\mathbb{E}\left[C_{T}\right]$. It is theoretically feasible to obtain optimal inspection and maintenance plans by means of the pre-posterior decision theory, however it becomes computationally intractable as the branches of the decision tree exponentially increase with time. One approach to circumvent this problem is to impose predefined decision rules in order to reduce the policies which have to be evaluated. Some of the decision rules that have been frequently applied in risk-based inspection planning of offshore structures are:
(i) Inspections are planned either periodically or before an annual failure probability threshold $\Delta P_{F}$ is reached. The optimal interval and optimal annual failure probability threshold are then identified.
(ii) A perfect repair action is immediately performed if the inspection gives an outcome of crack detection $\left(g_{D}\left(t_{\text {ins }}\right) \leq 0\right)$.
(iii) After the perfect repair, it is assumed that the component goes back to its initial state thus forming a new decision tree with a lifetime equal to $T_{N}-t_{\text {ins }}$.

I\&M strategies are evaluated through Monte Carlo simulations to compute the total expected $\operatorname{cost} \mathbb{E}\left[C_{T}\right]$. The expected failure cost $\mathbb{E}\left[C_{F}\right]$ is the sum of annual failure probabilities multiplied by the failure cost $C_{F}$. The expected cost of inspection $\mathbb{E}\left[C_{I}\right]$ is the product of inspection cost $C_{I}$ and the number of inspections. The expected cost of repair $\mathbb{E}\left[C_{R}\right]$ is the product of the repair $\operatorname{cost} C_{R}$ and the number of repairs performed. All the costs are discounted by a factor $\gamma \in[0,1]$ to take into account the time value of money. The total expected cost $\mathbb{E}\left[C_{T}\right]$ is the sum of the failure, inspection and repair costs over $N_{\text {sim }}$ simulations.

$$
\mathbb{E}\left[C_{T}\right]=\frac{1}{N_{\text {sim }}} \sum_{n=1}^{N_{\text {sim }}}\left[\sum_{t=1}^{T_{N}} C_{F} \Delta P_{F}(t) \gamma^{t}+\sum_{t=t_{\text {ins }, 1}}^{t_{\text {ins }, N}} C_{I} \gamma^{t}+\sum_{t=t_{\text {rep }, 1}}^{t_{\text {rep }, N}} C_{R} \gamma^{t}\right]
$$

where $T_{N}$ is the planned lifetime of the structure. $\Delta P_{F}(t)$ is the annual failure probability for year $t . t_{\text {ins }, N}$ and $t_{\text {rep }, N}$ represent the number of inspections and repairs performed in each simulation.

### 4.2. IEM planning through POMDPs

In the following section, a brief description of partially observable Markov decision processes (POMDPs) is presented with its particular implementation in offshore wind I\&M planning problem. A POMDP is a generalisation of a Markov decision process (MDP) in which the agent takes probabilistic actions in a stochastic environment and imperfect observations. In the 7 tuple $\langle\mathcal{S}, \mathcal{A}, \mathcal{O}, T, Z, R, \gamma\rangle$ process, the agent takes an action $a \in \mathcal{A}$ thereby transitioning the belief state $\mathbf{b}(s)$ according to the transition model $T\left(s^{\prime}, a, s\right)=P\left(s^{\prime} \mid s, a\right)$. The agent then receives an imperfect observation $o \in \mathcal{O}$ with the probability $Z\left(o, s^{\prime}, a\right)=P\left(o \mid s^{\prime}, a\right)$ and also collects the reward $R(\mathbf{b}, a)$ for taking the action $a$.

An inspection and maintenance planning problem can be formulated as a POMDP through proper definition of its elements $\langle\mathcal{S}, \mathcal{A}, \mathcal{O}, T, Z, R, \gamma\rangle$. A concise explanation is provided below, and more details can be found in Morato et al. (2022), Papakonstantinou and Shinozuka (2014a, 2014b).

- States: As already described before, the implementation of DBNs/POMDPs requires efficient and effective discretisation of continuous random variables. The first element of POMDP tuple $\mathcal{S}$ can be directly defined from the domain of the discretised intervals. For example, the through-thickness criterion POMDP consists of $|S|=\left|S_{d}\right| \cdot\left|S_{\tau}\right|$ states and

that of FAD criterion POMDP is $|S|=\left|S_{d}\right| \cdot\left|S_{\tau}\right| \cdot\left|S_{g_{F M}}\right|$. The initial belief $\mathbf{b}_{\mathbf{0}}(s)$ is the joint probability distribution of those random variables at $t=0$.

- Action-Observation: Several maintenance actions $a \in \mathcal{A}$ can be defined herein such as "perfect-repair", "imperfect-repair" or "do-nothing". Observations $o \in \mathcal{O}$ refer to different types of inspection techniques described in Section 2.2. Note that monitoring can also be modelled as an observation through systematic post-processing of continuous data stream into discrete observations.
- Transition probabilities: A transition matrix $T\left(s^{\prime}, a, s\right)$ for each maintenance action $a \in \mathcal{A}$ is defined as the probability of the component changing from the state $s \in \mathcal{S}$ to the state $s^{\prime} \in \mathcal{S}$.

For the action "do-nothing", the transition matrix $T\left(s^{\prime}, a_{D N}, s\right)$ follows the stochastic deterioration process since no maintenance action is performed. Therefore, $P\left(d_{t+1}, \tau_{t+1}\right.$ $\left.d_{t}, \tau_{t}\right)$ and $P\left(d_{t+1}, \tau_{t+1}, g_{F M t+1} \mid d_{t}, \tau_{t}, g_{F M t}\right)$ become the transition models for POMDPs with different failure criteria.

The transition model for a "perfect-repair" action $T\left(s^{\prime}, a_{P R}, s\right)$ is constructed such that the component holding any belief $\mathbf{b}(s)$ returns to its initial condition $\mathbf{b}_{\mathbf{0}}(s)$ (Morato et al., 2022). Despite being briefed to only two actions in this paper, other repair transition matrices can also be defined for different types of maintenance actions (Papakonstantinou \& Shinozuka, 2014a).

- Observation probabilities: An observation matrix $Z\left(o, s^{\prime}, a\right)$ defines the probability of collecting an observation $o \in \mathcal{O}$ for the component being in state $s^{\prime} \in \mathcal{S}$ after taking the action $a$. Frequently used ones in offshore I\&M planning are "no-inspection", "binary-indication" and "continuous-indication", etc.
- Rewards: After taking an action $a \in \mathcal{A}$ every time step, the agent collects the reward $R(\mathbf{b}, a)$ which is a weighted sum of the belief $\mathbf{b}(s)$ and the state reward $R(s, a)$. One needs to define the state reward $R(s, a)$ for each action-observation combination of RBI planning.

The reward of "do-nothing/no-inspection" is the failure risk computed from the failure $\operatorname{cost}-C_{F}$ assigned to the failure states within $\bar{R}\left(s, a_{D N-N I}\right)$ and the transition probability as follows:

$$
R\left(s, a_{D N-N I}\right)=P\left(s^{\prime} \mid s, a\right) \bar{R}\left(s^{\prime}, a_{D N-N I}\right)-\bar{R}\left(s, a_{D N-N I}\right)
$$

The reward of "do-nothing/inspection" is one inspection cost $-C_{I}$ additional to the reward of "Do-nothing/no-inspection" such that:

$$
R\left(s, a_{D N-I}\right)=R\left(s, a_{D N-N I}\right)-C_{I}
$$

The reward of "perfect-repair/no-inspection" is simply equal to the repair cost $-C_{R}$ for any state:

$$
R\left(s, a_{P R-N I}\right)=-C_{R}
$$

The objective of I\&M planning being to identify the optimal policy which minimises the total expected cost can be rephrased, within the POMDP framework, as to obtain a sequence of actions that maximises the total expected reward. In an MDP policy $(\pi: \mathcal{S} \rightarrow \mathcal{A})$, the current state can prescribe which action to be taken. Since the agent cannot fully observe the current state in POMDPs, action decisions are planned based on the belief. A POMDP policy $(\pi: \mathbf{B} \rightarrow \mathcal{A})$ therefore maps a belief $\mathbf{b}$ to the prescribed action and the objective is to identify the optimal policy $\pi^{*}(\mathbf{b})$ which maximises the expected sum of the rewards. The value of the

optimal policy $\pi^{*}$ is described by the value function:

$$
V^{*}(\mathbf{b})=\max _{a \in \mathcal{A}}\left[\sum_{s \in \mathcal{S}} b(s) R(s, a)+\gamma \sum_{o \in \mathcal{O}} P(o \mid \mathbf{b}, a) V^{*}\left(\mathbf{b}^{\prime}\right)\right]
$$

Recently, efficient point-based solvers have been developed which solve high-dimensional state space POMDPs based on a representative set of belief points (Kurniawati, Hsu, \& Lee, 2008; Spaan \& Vlassis, 2004). In the point-based solvers, the value function in Equation (27) is parametrised by a set of $\alpha$-vectors each of which is associated to an action. For a certain belief $\mathbf{b}(s)$, the optimal action is the one corresponding to the $\alpha$-vector which maximises the value function:

$$
V^{*}(\mathbf{b})=\max _{\alpha \in \Gamma} \sum_{s \in \mathcal{S}} \alpha(s) b(s)
$$

Since the belief is updated after every action and observation, as in Equations (21) and (22), the value function is therefore recomputed to choose sequential optimal actions over time.

# 5. Numerical experiments: Application to a tubular joint 

With the objectives of implementing the presented I\&M planning methods integrated with various failure criteria, as well as exploring the effects of failure criteria, deterioration and inspection models on the identified I\&M strategies, a set of numerical experiments are conducted here for the particular case of an offshore tubular joint subjected to fatigue deterioration. Table 1 lists all the conducted experiments, classified by the implemented failure criterion and fracture mechanics model.

Table 1.: List of analysed cases for RBI planning.


First, the I\&M planning is performed with an inspection model in which the detection threshold $\hat{d}_{s, t h}$ (Section 2.2) is fixed. The effects of fracture mechanics models and failure criteria on the crack propagation, reliability updating and optimal I\&M plan are thoroughly analysed. The optimal I\&M strategies identified by different optimisation methods for each case are also compared. Afterwards in Experiment 2, only one combination of 2-D FM model and FAD criterion is considered while the detection threshold $\hat{d}_{s, t h}$ of the inspection technique is varied within a range to demonstrate how the I\&M policies adapt with different inspection models. Detailed explanation of the deterioration models, inspection and cost models is provided in the following sections.

# 5.1. Deterioration models 

### 5.1.1. SN Model

The fatigue deterioration is first estimated by computing the cumulative fatigue damage following the design recommendations provided by DNV standards (DNV, 2016, 2018, 2019). Considering that the tubular joint is located just above the mean waterline, which is an accessible area for inspections, a fatigue design factor $F D F$ of 2 is assigned in this case. Assuming the structural component is designed to the limit for a lifetime of 20 years, the scale parameter of the Weibull stress range distribution is found to be $q=6.4839$ from Equation (1). The variables used in the SN approach are listed in Table 2. The reliability over the lifetime according to SN-Miner's rule is computed by crude Monte Carlo simulations with one million samples.

Table 2.: Variables used in SN model.


Determ. $=$ Deterministic
${ }^{*} \log _{10}\left(k_{1}\right)$ and $\log _{10}\left(k_{2}\right)$ are fully correlated.

### 5.1.2. FM models

For each considered setting, the initial crack size $d_{0}$ and crack growth parameter $C_{d}$ are calibrated to render a similar reliability in both SN and FM models. Calibration is performed by the least-square fitting of the normalised failure probability. In Option 3 cases, the throughthickness failure criterion is still used for the calibration since it is assumed that the cracks fail when they penetrate the thickness during SN tests. The FAD criterion is only used for reliability analysis and I\&M planning. Figure 6 shows the goodness-of-fit of the calibrations. The calibration for the 2-D FM model shows some discrepancies in the high reliability region. Yet the probabilities of failure in this region are very small so that they are assumed not to affect the optimal decision. The calibrated parameters together with all other parameters used in FM models are listed in Table 3. The normalised resistance parameter $R_{f}$ for the FAD criterion is taken as recommended by JCSS (2011).

## Incorporation of residual stress

When the failure assessment diagram criterion is used for the case of welded joints, it is necessary to take into account the residual stress as a consequence of weld metal contraction being restrained by the base material (Anderson, 2005). The presence of residual stress in welded joints contributes as secondary stress component in the stress intensity factor such that $K_{I}=K_{I}^{P}+K_{I}^{S}$. However, secondary stress does not contribute in the plastic collapse since it has no significant effect on the tensile strength (British Standards, 2019).

Realistic estimates of the residual stress are possible by finite element simulations of the considered welded detail. Alternatively, the residual stress can be conservatively assumed to be uniform. In the experiments, the values recommended in JCSS (2011) are used for lognormal

![img-5.jpeg](img-5.jpeg)

Figure 6.: Calibration between SN and FM approaches. The reliability index is the normal inverse cumulative distribution function of the failure probability $\beta(t)=-\Phi^{-1}\left(P_{F}(t)\right)$.
distribution of uniform residual stress $R_{s}$, see Table 3. The applied primary stress is considered to be fully reversed, i.e. the primary mean stress is zero and therefore, the value of stress amplitude is used when the primary stress intensity factor $K_{I}^{P}$ and the load ratio $L_{r}$ are computed.

# Tensile strength and fracture toughness 

Material properties are usually considered as uncertain variables due to production variability. The tensile strength of a structural material is often described by a lognormal distribution. Fracture toughness is a quantitative description of material's resistance to fracture failure beyond which the crack propagation becomes unstable. A three-parameter Weibull distribution is proposed to describe the fracture toughness $K_{\text {mat }}$ as in the following equation:

$$
F_{K m a t}(k)=1-\exp \left[-\left(\frac{k-K_{0}}{A_{k}}\right)^{B_{k}}\right]
$$

The shape parameter $B_{k}$ is 4 and the recommended value of the threshold parameter $K_{0}$ is 20 $\mathrm{MPa} \sqrt{m}$ (JCSS, 2011). The scale parameter $A_{k}$ is computed according to the following equation (British Standards, 2019). The resulting fracture toughness is in $\mathrm{MPa} \sqrt{m}$.

$$
A_{k}=\left[11+77 \exp \left(\frac{T-T_{0}-T_{K}}{52}\right)\right]\left(\frac{25}{t}\right)^{0.25}\left[\ln \left(\frac{1}{1-p}\right)\right]^{0.25}
$$

where $T$ is the temperature at which $K_{\text {mat }}$ is to be determined (in ${ }^{\circ} \mathrm{C}$ ). $T_{0}$ is the temperature for a median toughness of $100 \mathrm{MPa} \sqrt{m}$ in 25 mm thick specimens and calculated as $T_{0}=$ $T_{27 J}-18^{\circ} \mathrm{C} . T_{27 J}$ is the temperature for 27 J measured in a standard Charpy V specimen. $T_{K}$ is the temperature term that describes the scatter in the Charpy versus fracture toughness correlation. For $S t d=15^{\circ} \mathrm{C}$ and $90 \%$ confidence, $T_{K}$ is $+25^{\circ} \mathrm{C} . t$ is the thickness of the material for which an estimate of $K_{\text {mat }}$ is required (in mm), and $p$ is the probability of $K_{\text {mat }}$ being less than estimated and $5 \%$ is recommended without experimental evidence (Wallin, 2011). In this paper, the tubular joint is considered to be made of $E N 10025-S 355-J R$ structural steel and the required values for material properties are obtained as follows: $T=10^{\circ} \mathrm{C}, T_{27 J}=20^{\circ} \mathrm{C}$ and $\sigma_{Y}=355 \mathrm{MPa}$ (Igwemezie, Mehmanparast, \& Kolios, 2018).

Table 3.: Variables used in FM models.


Determ. $=$ Deterministic; 3P-W $=$ Three-parameter Weibull distribution

# 5.2. Inspection models 

$P O D$ curves of different inspection methods frequently used for OWTs are provided in DNV (2019). Eddy current (EC) inspection has become a common inspection method for offshore wind structures as it can be used to detect fatigue cracks without removing coating. The EC inspection in the normal working conditions is used as a reference inspection model in Experiment 1 Fixed detection threshold. The parameters of signal response method $\beta_{0}, \beta_{1}, \sigma_{\varepsilon}$ and $\hat{d}_{s, t h}$ as in Equation (17), are therefore calibrated to provide an equivalent $P O D$ curve as the chosen inspection technique, see Figure 7a.

In Experiment 2, the risk-based I\&M planning is conducted for a range of detection thresholds. The parameters of the inspection models used in the RBI experiments are shown in Table 4. The shape of the $P O D$ curve changing with the detection threshold is illustrated in Figure 7 b .

Table 4.: Parameters of inspection models.


### 5.3. Modelling I\&M planning in POMDPs

The I\&M planning experiments are formulated as POMDPs through the deterioration rate DBNs. As discussed in Section 3, the continuous random variables need to be discretised to implement the DBNs and the discretisation scheme should be an optimal compromise between the accuracy of the results and the computational performance. Since the discretisation is arbitrary and case-specific, several attempts are made on the selection of the number of intervals and boundary values, and the discretisation schemes shown in Table 5 with the number of

![img-6.jpeg](img-6.jpeg)
(a) Experiment 1 inspection model, $\hat{d}_{s, t h}=$ 5.4898 .
![img-7.jpeg](img-7.jpeg)
(b) Experiment 2 inspection model, $\hat{d}_{s, t h} \in$ $[0,10]$.

Figure 7.: Illustration of inspection models.
states $\left|S_{d}\right|=40,\left|S_{\tau}\right|=21,\left|S_{g_{F M}}\right|=30$, are selected as the relevant ones. Accordingly, the deterioration rate DBNs with the through-thickness criterion has overall 840 states and that of the FAD criterion has 25,200 states with the additional limit state variable $g_{F M}$. Following the discretisation schemes, the initial belief $\mathbf{b}_{\mathbf{0}}$ and transition matrices $T\left(s^{\prime}, a, s\right)$ for each case are defined from one million simulations of crack size and FAD assessment points.

Table 5.: Discretisation schemes utilised in the numerical experiments.


Since the existing point-based solvers are set up for the solution of infinite horizon POMDPs and the I\&M planning is desired for 20 years (finite horizon), the state space of deterioration rate DBNs is augmented by encoding the time in the state space and adding a terminal state. For the detailed explanation about state augmentation, the reader is referred to Papakonstantinou and Shinozuka (2014a, 2014b). Finally, the state space of finite horizon POMDP with the throughthickness criterion has 9240 states and that of the FAD criterion has 277,200 states.

For all case studies, three action-observation pairs are considered: (1) do-nothing/noinspection (DN-NI) (2) do-nothing/inspection (DN-I) and (3) perfect-repair/no-inspection (PRNI). The consequence of a failure event is associated with a cost $C_{F}$ of $10^{6}$ monetary units. The cost of corrective repair and the risk of system failure conditional on component failure are taken into account in the failure cost $C_{F}$ of the joint. The cost of inspection $C_{I}$ independent of

the detection threshold is $10^{3}$ monetary units and the repair cost $C_{R}$ is $1.2 \cdot 10^{4}$ monetary units. The discount factor $\gamma=0.94$ is considered. SARSOP point-based solver is used for solving the POMDPs to obtain optimal I\&M policies (Kurniawati et al., 2008).
![img-8.jpeg](img-8.jpeg)
(a) Mean crack depth and crack length.
![img-9.jpeg](img-9.jpeg)
(b) Mean $K_{r}$ and $L_{r}(2-\mathrm{D}$ FM).

Figure 8.: Illustration of crack deterioration.

# 5.4. Results and discussion: Experiment 1 - Fixed detection threshold 

## Crack growth

As mentioned in the previous sections, both 1-D and 2-D fracture mechanics models are applied to estimate the crack deterioration. In both models, the crack propagation rate is influenced by the Paris law parameters and the stress intensity correction factor. To represent one-dimensional crack growth, Equation (9) is used where the stress intensity correction factor $Y_{d}$ is assigned as a time-invariant random variable, see Table 3. In two-dimensional crack growth, the stress intensity correction factors $Y_{d}$ and $Y_{c}$ become functions of time-varying crack size and are recomputed at every time step. The geometry functions $Y_{m d}, Y_{b d}, Y_{m c}, Y_{b c}$ and stress magnification factors $M_{k m d}, M_{k b d}, M_{k m c}, M_{k b c}$ are evaluated by parametric equations following the procedures of Newman and Raju (1981) and DNV (2019).

A crude Monte Carlo Simulation (MCS) containing 1 million samples was run to estimate the stochastic crack evolution. The comparison of mean crack propagation between 1-D and 2-D FM models can be seen in Figure 8a. The crack length is not comparable between the two models as the 1-D model only measures the crack depth. The crack depth grows faster in the 2-D model than in the 1-D model. In fact, this is due to different initial crack depths $d_{0}$ and crack growth parameters $C_{d}$ of the two models since they are calibrated to the same target reliability, see Table 3. However, it successively implies different crack propagation by the two

![img-10.jpeg](img-10.jpeg)
(a) Crack distribution by 1-D FM model.
![img-11.jpeg](img-11.jpeg)
(b) Crack distribution by 2-D FM model.

Figure 9.: Crack propagation by 1-D and 2-D FM models. To illustrate the difference between the two models, the same initial crack size $d_{0} \sim \operatorname{Exp}(0.1603)$ and crack growth parameter $\log \left(C_{d}\right) \sim \mathcal{N}(-27.6302,0.4599)$ are used.
models. To examine this, crack propagation is computed by the two models using the same initial crack size $d_{0} \sim \operatorname{Exp}(0.1603)$ and the crack growth parameter $\log \left(C_{d}\right) \sim \mathcal{N}(-27.6302,0.4599)$. The mean crack depth over the lifetime and $95 \%$ reference interval (between $2.5 \%$ and $97.5 \%$ quantiles) are plotted in Figure 9. Note that a cut-off point is considered at $d_{\text {crit }}=16 \mathrm{~mm}$ and all bigger cracks remain at 16 mm in Monte Carlo simulations. It is observed that the two models give different variability in the crack distribution. The variability of the 1-D FM model rapidly increases compared to 2-D model. This effect is important in the structural reliability aspect such that the 1-D FM model with higher model uncertainty gives higher probability of failure than the 2-D FM model. And therefore, when calibrated to have the same reliability, the 2-D FM model results in a higher mean and standard deviation of $C_{d}$.

Using the 2-D FM model, the deterioration of the tubular joint can also be described by the fracture ratio $K_{r}$ and the load ratio $L_{r}$ computed from Equations (13-15). The mean values of $K_{r}$ and $L_{r}$ are plotted in Figure 8b. Before year 10, the FAD assessment point mainly increases in the $K_{r}$ axis and the load ratio $L_{r}$ is initially less sensitive to the crack size. With small values of crack size, the tubular joint has a sufficient intact area and therefore it is not subjected to high net section stress $\sigma_{r e f}$. However, the load ratio starts increasing as the crack depth and crack length rapidly grow after year 10 .

# Updating reliability 

The effect of failure criteria and FM models on the updated failure probability after an inspection is examined here. Assuming an inspection is performed at year $t=11$ and no crack is detected during the inspection, the reliability is updated for different cases using Equation (19) through Monte Carlo simulations. In the deterioration rate DBNs, the updated failure probability is the probability of being in the failure states after performing the transition and estimation steps. As shown in Figure 10, consistent $P_{F}$ values are obtained by the MCS and the DBNs, which verifies the proper discretisation of the state space variables. On the other hand, the updated failure probabilities after the inspection are different among the analyzed cases. The 2D-FADFixed case gives the smallest failure probabilities in all years. This is expected simply due to the assumption of the capacity to hold the through-thickness cracks when the FAD criterion is used.

The effect of fracture mechanics models on reliability updating can be analysed through comparison of 1D-Thick-Fixed and 2D-Thick-Fixed cases. As discussed before, the two FM

![img-12.jpeg](img-12.jpeg)

Figure 10.: The updated cumulative failure probability given no-detection in the inspection at year 11 .
models provide different initial crack sizes $d_{0}$ and crack growth parameters $C_{d}$ when calibrated to the SN failure probabilities. Consequently, the crack depth belongs to different probability distributions with respect to each FM model, as illustrated with the crack size histograms in Figure 11a. Firstly, the variation in prior distributions influences the updated failure probability given no crack detection. However, this is not obvious just after the no-detection event, in Figure 11b. Since the probability of no-detection and probability of crack distribution are very low in the failure bin, i.e. $d \geq d_{\text {crit }}$, the difference in the updated $P_{F}$ is extremely small when normalised by the overall no-detection probability according to Equation (19). As the posterior distribution further propagates accumulating and increasing the probability in the failure bin, the difference in the updated $P_{F}$ can then be clearly observed as in Figure 11c and 11d. The more-detailed 2-D FM finally achieves higher reliability at the end of the lifetime. And vice versa, the decisionmaker may use simple models with higher uncertainty, e.g. 1-D FM but may take a higher risk than using more precise ones or perform more inspections to remain at the same reliability and risk.

Secondly, the overall probability of detection with the same inspection model is different between the two cases. The 2-D FM model with its higher crack growth parameters results in a higher probability of detection. In heuristic-based inspection planning, maintenance decision rules are often prescribed based on inspection outcomes, e.g. repair is performed if a crack is detected. In this case, using the 2-D FM will result in higher maintenance costs than the 1-D FM for the same inspection strategy.

# Optimal IEM strategies 

I\&M planning is performed through traditional heuristic-based methods as well as through the formulation as POMDPs. The SARSOP point-based POMDP solver is used for the computation of the optimal I\&M policies (Kurniawati et al., 2008). Two sets of heuristic decision rules equidistant inspections (EQ-INS) and inspections planned before an annual failure probability threshold is exceeded (THR-INS) - have been evaluated in the simulation environment through DBNs. If the inspection indicates the presence of crack, a perfect repair is immediately performed and after, the component goes back to its initial condition. The identified optimal I\&M strategies

![img-13.jpeg](img-13.jpeg)
(a) Prior distribution of crack depth $(\mathrm{t}=11)$.
![img-14.jpeg](img-14.jpeg)
(c) Posterior distribution of crack depth $(\mathrm{t}=15)$.
![img-15.jpeg](img-15.jpeg)
(b) Posterior distribution of crack depth $(\mathrm{t}=11)$.
![img-16.jpeg](img-16.jpeg)
(d) Posterior distribution of crack depth $(\mathrm{t}=19)$.

Figure 11.: Propagation of crack distribution. (a) The prior crack distribution at year $t=11$ is estimated by the two FM models. (b) The posterior $P_{F}$ at the year of inspection is almost equal for 1-D and 2-D models whereas the overall detection probability is different. (c, d) The updated $P_{F}$ w.r.t the two models becomes different as the posterior crack distribution propagates.
from heuristics and POMDPs are evaluated in a simulation environment. The resulting total expected costs $\mathbb{E}\left[C_{T}\right]$ as well as the numerical confidence intervals over $10^{5}$ simulations are reported in Table 6 .

In all combinations of deterioration models and failure criteria, POMDP policies outperform traditional heuristics with significant differences in the total expected cost. Comparing among different options, 2D-FAD-Fixed case results in less expected cost than the other two options which rely on the through-thickness criterion. When the FAD criterion is used, it is assumed that the through-thickness cracks can grow further in the length until the critical value of the stress intensity factor is reached. It is also worth mentioning that the fracture toughness of the material considered for the tubular joint is high enough so that the component does not fail before the crack reaches the thickness and can hold the through-thickness crack. Therefore, the failure probabilities over the lifetime with the FAD criterion are smaller than the other cases, as already discussed before. It results in a significant reduction of failure risk as well as less observations and maintenance actions can be generally expected. Random realisations are presented to visualise the policies prescribed by different approaches. Figure 12a, 12c and

Table 6.: Experiment 1 - Fixed detection threshold: Comparison of the total expected cost.


12e represent the finite horizon POMDP policy realisations and Figure 12b, 12d and 12f show the realisations of the equidistant heuristic. As manifested in the POMDP policies, only one inspection is required in the 2D-FAD-Fixed case if the first inspection outcome is no-detection thanks to the low failure risk. Contrarily, more inspections are conducted in a number of years in the cases in which the through-thickness criterion is used.

In the heuristic-based policies, an immediate repair action is prescribed after detection, but the POMDP policies may opt to perform subsequent inspections in case of detection. A repair action is planned only if the subsequent inspections also give detection outcomes. In Figure 12a, POMDP policies plan one more inspection after a detection event and a repair is performed as the second inspection also gives detection. However, POMDP policies also consider more subsequent inspections when the deterioration model has lower uncertainty. For the 2D-ThickFixed case, POMDP plans up to three consecutive inspections as in Figure 12c. Since the last inspection declares no-detection, no maintenance action is taken. Therefore, POMDP solutions can provide adaptive policies for different scenarios such that, as in this example, it is plausible to take advantage of the more precise 2-D model to avoid an expensive repair.

In contrast, traditional heuristic approaches which only follow the predefined decision rules are not able to capture such aspects. Utilising the 2-D FM instead of the 1-D FM affects the optimal heuristic policies such that the number of inspections is reduced, which opposes the pattern in the POMDP policies. In the equidistant inspection approach, two inspections $\left(\Delta_{\text {ins }}=7\right)$ are performed in the 1D-Thick-Fixed whereas only one inspection $\left(\Delta_{\text {ins }}=11\right)$ is conducted in the 2D-Thick-Fixed. As discussed before, using the 2-D FM model is a matter of reducing the risk but on the other hand increasing the maintenance cost. And in this case, the increased maintenance cost is more than the reduced risk, therefore one inspection has been reduced to adjust the optimal policy.

# 5.5. Results and discussion: Experiment 2 - Varied detection threshold 

## Optimal IEM strategies

Hereafter, only one combination with 2-D FM model and FAD criterion is considered. The optimisation is performed only through POMDPs as it has been demonstrated in the previous experiment that POMDP outperforms traditional heuristic approaches for any combination of deterioration model and failure criteria. In this experiment, the RBI planning is repeatedly performed for several values of detection thresholds $0 \leq \hat{d}_{s, t h} \leq 10$. The transition models and the rewards models of the POMDP remain the same as the 2D-FAD-Fixed case from the previous experiment. Only the observation model $Z\left(o, s^{\prime}, s\right)$ is modified for each threshold value.

The breakdown of the total expected cost evaluated over $10^{5}$ simulations are reported in

![img-17.jpeg](img-17.jpeg)
(a) 1D-Thick-Fixed (FH-POMDP).
![img-18.jpeg](img-18.jpeg)
(c) 2D-Thick-Fixed (FH-POMDP).
![img-19.jpeg](img-19.jpeg)
(e) 2D-FAD-Fixed (FH-POMDP).
![img-20.jpeg](img-20.jpeg)
(b) 1D-Thick-Fixed (Heuristic EQ-INS).
![img-21.jpeg](img-21.jpeg)
(d) 2D-Thick-Fixed (Heuristic EQ-INS).
![img-22.jpeg](img-22.jpeg)
(f) 2D-FAD-Fixed (Heuristic EQ-INS).

Figure 12.: Policy realisations of Experiment 1 - Fixed detection threshold. Inspection outcomes are represented by a circle (for no-detection) or a five-pointed star (for detection). A red bar denotes that a perfect repair is performed.

Figure 13. In general, moderate to high detection thresholds $5 \leq \hat{d}_{s, t h} \leq 10$ provide the lowest expected costs. The policy realisations of some representative cases are also presented. Figure 14a
![img-23.jpeg](img-23.jpeg)

Figure 13.: Experiment 2 - Varied detection threshold: Comparison and breakdown of the total expected cost.
and 14 b show random realisations of inspection planning with low detection threshold $\hat{d}_{s, t h}=0$ and Figure 14c and 14d show the realisations with high threshold $\hat{d}_{s, t h}=10$. An interesting pattern of inspection planning can be discovered in the POMDP prescribed policies. When the inspection model has a lower threshold, POMDP tends to plan several subsequent inspections in case of detection. The shape of the $P O D$ curve plateaus earlier with lower detection threshold, e.g. $P O D$ curve of $\hat{d}_{s, t h}=0$ becomes flat at around $d=5 \mathrm{~mm}$ in Figure 7b. If a detection outcome is obtained, one may not simply presume bigger crack size and/or higher probability failure, noting that even the small cracks which do not cause failure may also be detected. Therefore, the probability of failure is only slightly increased and successive inspections are planned instead of taking an expensive repair action, see Figure 14a. In the case of no-detection from the low threshold inspection, a small crack can be assured since bigger cracks $d>5$ mm have almost zero probability of no-detection in the $P O D$ curve. The probability of failure therefore drops drastically, see Figure 14b.

On the other hand, the $P O D$ curve with a high detection threshold slants up with the crack size, see $\hat{d}_{s, t h}=10$ in Figure 7b. Bigger cracks are more likely to be detected than smaller ones. If this inspection model gives a detection outcome, a severe crack can be expected with a higher confidence, thus resulting in a high jump of failure probability as in Figure 14c. The repair action is also performed immediately after one detection. Nevertheless, detection events are less frequent in this case and the expected repair cost is still remarkably lower compared to the low threshold inspection.

# 6. Conclusions 

In this paper, the effects of failure criteria, deterioration and inspection models on the optimal inspection and maintenance (I\&M) strategies are examined. Two-dimensional fracture mechanics model and failure assessment diagram (FAD) criterion have been successfully integrated with dynamic Bayesian networks (DBNs), therefore allowing the formulation and optimisation of I\&M planning via partially observable Markov decision processes (POMDPs). Various deterioration, inspection and failure criteria settings were tested for the optimal management of a structural detail subjected to fatigue deterioration, revealing the following findings:

![img-24.jpeg](img-24.jpeg)

Figure 14.: Policy realisations of Experiment2 - Varied detection threshold. Inspection outcomes are represented by a circle (for no-detection) or a five-pointed star (for detection). A red bar denotes that a perfect repair is taken.

- The failure assessment diagram might be preferred as the failure criterion to model redundant structures with capacity to sustain through-thickness cracks since it offers significant savings in the total expected cost, especially through advanced optimisation methods such as POMDPs. However, one needs the knowledge of material properties, compulsorily yield strength and fracture toughness to implement the FAD criterion.
- 2-D fracture mechanics models are more robust than 1-D models since the effects of timedependent crack size, geometry of the structure and welded detail are inherently considered in the stress intensity correction factors $Y_{d}$ and $Y_{c}$. The shortcoming is that it requires FEM analysis or the use of parametric equations, both of which demand computational resources.
- The observation model, specified often through probability of detection (POD) curves, can be adjusted by varying the detection threshold of the inspection technique. Generally, very low detection thresholds are not recommended due to its flat and high $P O D$ curve, causing frequent detections, inspections and/or repairs.

Throughout the experiments, it is demonstrated that I\&M polices provided by finite horizon POMDPs outperform heuristic-based polices for any combination of deterioration models and failure criteria. POMDPs also reveal adaptability in the policy patterns depending on the models

specified in the I\&M planning. The main limitation associated with implementing the 2-D fracture mechanics model and FAD criterion in discrete DBNs/POMDPs is the high-dimensional state space. Computational intractability becomes a constraint to apply such complex models and failure criterion for the case of multiple components or longer horizon lengths. To overcome this curse of dimensionality, further research efforts are suggested towards the integration of the FAD criterion with POMDP-based deep reinforcement learning (DRL) approaches. The capability of POMDP-based DRL approaches to efficiently provide optimal I\&M strategies for large state space problems has been demonstrated in Andriotis and Papakonstantinou (2021).

# Acknowledgments 

This research has been developed at the University of Liège, Belgium, in collaboration with the University of Strathclyde, UK, and Aalborg University, Denmark. The financial support provided by the Belgian Energy Transition Fund (FPS Economy) through the projects PhairywinD and MaxWind is greatly appreciated. Dr. Morato would further like to acknowledge the support granted by the National Fund for Scientific Research in Belgium F.R.I.A. - F.N.R.S.
