# TUDelft 

Delft University of Technology

## System level reliability assessment for high power light-emitting diode lamp based on a Bayesian network method

Ibrahim, Mesfin Seid; Fan, Jiajie ; Yung, Winco K.C. ; Jing, Zhou; Fan, Xuejun; van Driel, Willem; Zhang, Guoqi
DOI
10.1016/j.measurement.2021.109191

Publication date
2021
Document Version
Final published version
Published in
Measurement: Journal of the International Measurement Confederation

## Citation (APA)

Ibrahim, M. S., Fan, J., Yung, W. K. C., Jing, Z., Fan, X., van Driel, W., \& Zhang, G. (2021). System level reliability assessment for high power light-emitting diode lamp based on a Bayesian network method. Measurement: Journal of the International Measurement Confederation, 176, 1-13. Article 109191. https://doi.org/10.1016/j.measurement.2021.109191

## Important note

To cite this publication, please use the final published version (if applicable).
Please check the document version above.

## Copyright

Other than for strictly personal use, it is not permitted to download, forward or distribute the text or part of it, without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license such as Creative Commons.

## Takedown policy

Please contact us and provide details if you believe this document breaches copyrights.
We will remove access to the work immediately and investigate your claim.

# Green Open Access added to TU Delft Institutional Repository 

'You share, we take care!' - Taverne project
https://www.openaccess.nl/en/you-share-we-take-care

Otherwise as indicated in the copyright section: the publisher is the copyright holder of this work and the author uses the Dutch legislation to make this work public.

# System level reliability assessment for high power light-emitting diode lamp based on a Bayesian network method 

Mesfin Seid Ibrahim ${ }^{\mathrm{a}, \mathrm{b}}$, Jiajie Fan ${ }^{\mathrm{c}, \mathrm{e}, \mathrm{b}, *}$, Winco K.C. Yung ${ }^{\mathrm{a}}$, Zhou Jing ${ }^{\mathrm{d}}$, Xuejun Fan ${ }^{\mathrm{f}}$, Willem van Driel ${ }^{\mathrm{g}, \mathrm{h}}$, Guoqi Zhang ${ }^{\mathrm{h}}$<br>${ }^{a}$ Department of Industrial and System Engineering, The Hong Kong Polytechnic University, Hung Hom, Hong Kong<br>${ }^{\mathrm{b}}$ College of Engineering, Kombolcha Institute of Technology, Wollo University, Kombolcha 208, Ethiopia<br>${ }^{c}$ Institute of Future Lighting, Academy for Engineering and Technology, Fudan University, Shanghai 200433, China<br>${ }^{d}$ College of Mechanical and Electrical Engineering, Hohai University, Changshou 213022, China<br>${ }^{e}$ Changshou Institute of Technology Research for Solid State Lighting, Changshou 213161, China<br>${ }^{f}$ Department of Mechanical Engineering, Lamar University, Beaumont, TX, USA<br>${ }^{g}$ Signify, Eindhoven 5656 AE, the Netherlands<br>${ }^{h}$ EEMCS Faculty, Delft University of Technology, Delft 2628, the Netherlands

## A R T I C L E I N F O

Keywords:
Light-emitting diodes (LEDs)
Bayesian networks (BN)
Junction tree algorithm (JTA)
Reliability assessment
System level lifetime prediction

## A B S T R A C T

The increased system complexity in electronic products brings challenges in a system level reliability assessment and lifetime estimation. Traditionally, the graph model-based reliability block diagrams (RBD) and fault tree analysis (FTA) have been used to assess the reliability of products and systems. However, these methods are based on deterministic relationships between components that introduce prediction inaccuracy. To fill the gap, a Bayesian Network (BN) method is introduced that considers the intricacies of the high-power light-emitting diode (LED) lamp system and the functional interaction among components for reliability assessment and lifetime prediction. An accelerated degradation test was conducted to analyze the evolution of the degradation and failure of components that influence the system level lifetime and performance of LED lamps. The Gamma process and Weibull distribution are used for component level lifetime prediction. The junction tree algorithm was deployed in the BN structure to estimate the joint probability distributions of the lifetime states. The degradation and prediction results showed that LED modules contribute a major part for lumen degradation of LED lamps followed by drivers and the least effect is from diffuser and reflector. The BN based lifetime estimation results also exhibited an accurate prediction as validated with the Gamma process and such improved reliability assessment outcomes are beneficial to LED manufacturers and customers. Thus, the proposed approach is effective to evaluate and address the long-term reliability assessment concerns of high-reliability LED lamps and fulfill the guarantee of high prediction accuracy in less time and cost-effective manner.

## 1. Introduction

The introduction of Light-emitting diodes (LEDs)-based solid state lighting (SSL) marked the third revolution in the lighting industry after traditional incandescent and fluorescent light sources. They are emerging as the future sources of lighting, with multiple benefits, and have attracted a wide range of applications. Nowadays, LEDs are widely used in different sectors including street lighting, traffic lighting, advertising display backlights, aviation lighting, indoor lighting, communication devices, automotive lighting, and medical equipment [1,2]. LED-based SSL is known for its benefit in providing lower energy
consumption, higher reliability, longer lifetime, compactness in size, and eco-friendliness compared to their traditional counterparts [3]. Low energy consumption, which ultimately helps in energy-saving programs, is one of the benefits of high-power white LEDs. The world electrical energy consumption for lighting was estimated to be about $20 \%$ of the global energy production as of 2014. The replacement of traditional lighting sources with LED-based SSL is anticipated to reduce the electrical energy usage for lighting applications by $15 \%$ in 2020 , by $40 \%$ in 2030, and up to $75 \%$ in 2035 in the U.S according to forecast by the United States Department of Energy (US-DOE) [4].

The high-power LED lamp is a complex optoelectronic system

[^0]
[^0]:    * Corresponding author at: Fudan University, China.

    E-mail address: jiajie_fan@fudan.edu.cn (J. Fan).
    https://doi.org/10.1016/j.measurement.2021.109191
    Received 14 July 2020; Received in revised form 12 February 2021; Accepted 15 February 2021
    Available online 20 February 2021
    0263-2241/© 2021 Elsevier Ltd. All rights reserved.

assembled from several components (such as LED chips, electrical drivers, substrate materials, packaging material including bonding wires/die attaches, encapsulant materials such as silicon, phosphor, optical parts, thermal heat-sink components and so on) [5]. Because of the interaction of the different components, a high-power LED lamp is also known to have a large number of failure modes and failure mechanisms. Besides, there are also technological and technical gaps for describing the different failure mechanisms in a high-power LED lamp system. This makes the system level reliability assessment and lifetime prediction of high-power LED lamp challenging [6]. A failure in electronic systems, such as high-power white LEDs, could be either a catastrophic or degradation failure. A catastrophic failure is usually caused by overstressing where single stress exceeds a certain threshold and can be attributed to improper operation or external factors. It is often the case that a catastrophic failure is fatal to the whole system or product. With proper operation and close follow-up, catastrophic failures can be reduced if not avoided. On the other hand, degradation failure which occurs as a result of cumulative stresses (loads) over time, is inevitable and results in a gradual degradation of the performance characteristics [7].

Traditionally, accelerated lifetime tests (ALT) are widely used to estimate the lifetime of highly reliable, expensive as well as safe-ty-critical products, such as aircraft parts, batteries, and LEDs. However, ALT is found to be expensive for estimating the lifetime of such products in a short time as it needs a longer time to collect sufficient time-tofailure data [8]. Nowadays, accelerated degradation tests (ADT) have become a promising alternative in capturing the degradation paths for the performance characteristics of products [9]. Thus, ADT based on high-stress conditions enables the gathering of appropriate lumen degradation, color shift, and catastrophic failure results efficiently and in a relatively short time for LEDs [10]. Using degradation data, many research studies have been conducted to address lifetime estimation and reliability assessment issues of LED light sources. Fan et al. [11] proposed a degradation data-driven method to predict the lumen maintenance lifetime of high-power white LEDs using degradation data. Similarly, other degradation modelling approaches proposed to assess the reliability of LED light sources include Wiener process [12], [13], Gamma process [14], [15], [16], Kalman filter (KF), extended KF [17], [18], [19], unscented KF [17], [20], Particle filter [21], Lévy process [22] and Recurrent Neural Network [23]. Ibrahim et al. [13] applied the Wiener Process to predict the lumen maintenance lifetime of LEDs and Bayesian inference based on Gibbs sampling used to estimate unknown model parameters. Huang et al. [12] applied a modified Wiener process method to model the lumen maintenance and color shift of mid-power white LEDs. Most of these studies focus on lifetime prediction based on degradation data obtained from a component, mainly an LED package/module. However, the lifetime of a LED lamp is not only affected by the lifetime status of a single component but all its components, including the LED driver, LED module, diffuser, and reflector and interconnects. That is why the system and/or product level reliability prediction approaches need to consider the failure modes and mechanisms at the component levels.

In a high power LED lamp system, the LED driver serves as the constant current source and optimizes the power to drive high-power LEDs [24]. Usually, LED drivers are considered the weakest part among all the components in an LED lighting product. A report from the US DOE [25] claimed that the LED driver (power supply) is the weakest part among an LED outdoor luminaire, constituting 52% failure, LED package (10%), housing (31%) and control circuit - driver (7%). On the other hand, van Driel et al. [26] reported that solder interconnects account for dominant failures followed by LED emitters and drivers. The results among the few studies based on subsystems and components for system level lifetime studies are inconsistent. The Illuminating Engineering Society of North America (IESNA) used IES-TM-21 [27] standard to rate lifetime are mainly based on the LED packages, and recently the IES-TM-28-14 standard was introduced to project the lifetime for LED-based SSL lamps and luminaires [28].

Although the rapid growth in the engineering design and manufacturing technology enabled the advancement of engineering systems, it also introduced challenges in the system level reliability assessment. This is because of the increased complexity of products/systems that leads to unexpected failures with interdependent behavior [29]. Traditionally, graph model-based reliability block diagrams (RBD) and fault tree analysis (FTA) have been used to assess the reliability of products and systems. The FTA is a deductive approach that helps mainly to identify critical failure causes of a product/system. Furthermore, these methods are based on deterministic relationships between components/subsystems that make it difficult to model systems with uncertainties and dependent events. In this study, we make use of inputs from FTA results and expert knowledge for LED structural and functional analysis. Despite the shortcoming of traditional approaches, Bayesian Network (BN) is found to be a suitable method for complex system reliability analysis [30], [31], [32], due to its advantages in handling uncertainties, correlations, and the conditional relationship between components/subsystems [31]. As one of the popular modelling and reasoning tools, the BN model has been employed in the fields of machine learning, artificial intelligence, and uncertainty management [33]. The BN model has also been applied in the field of reliability engineering including software reliability [34], modelling maintenance [35], and fault diagnosis in systems [36], [37]. Recently, the BN model was found to be effective in estimating the system/product reliability of complex systems, such as high-speed trains [37], solar-powered unmanned aerial vehicles [38] and pitting degradation structural steel in marine systems [39]. Zheng et al. [40] presented an improved compression inference algorithm in multilevel BN to analyze the reliability of complex multistate satellite systems. A dynamic BN was also proposed to assess and update the reliability of timber structures exposed to deterioration processes based on inspection data [41]. Therefore, system level lifetime prediction based on a BN is very important to achieve a reasonable integration of performance data from constituting components for a complex system/product.

In order to address the long-term reliability assessment concerns of highly reliable products and fulfill the guarantee of increased prediction accuracy in less time and cost-effective manner, developing a system level lifetime prediction method based on the BN model is highly demanded. In this study, an accelerated degradation test based on thermal stress was designed, conducted, and analyzed the evolution of degradation and failures from components that influence the lifetime and performance of the LED-based lighting products. This paper proposed a BN method that considers the intricacy of a high-power LED lamp system and functional interaction among components for a novel application on system level reliability assessment and lifetime prediction.

The remaining parts of this paper are organized as follows: Section 2 describes the methodology and theoretical analysis of the research. Section 3 presents the experimental design and setup for gathering the required data. In Section 4, the results and detailed discussions based on the experimental results and proposed methodology are presented. Finally, concluding remarks are drawn in Section 5.

## 2. Theory and methodology

In this section, the proposed models and algorithms for modelling the degradation of high-power LED lamps and the system level reliability assessment and lifetime prediction are introduced. The Gamma process, Weibull distribution and IES-TM-28 exponential based empirical models for performance degradation of component/subsystem and the BN model applied to integrate the reliability information at the system level are presented.

### 2.1. Degradation analysis based on empirical models

Compared to traditional lighting sources (i.e., incandescent and

fluorescent), a high-power LED lamp is a more complex product and possesses additional components that enable it to provide the required light output. The main components in the high-power LED lamp used in this study include a LED module (light engine), the LED driver, diffuser and reflector, and so on. Similarly, the light output degradation of the LED lamp can be due to the LED module, the driver, the diffuser, and reflector components depreciation as well as degradation due to geometric or form factors. Equation (1) expresses the luminous flux degradation of a high-power LED lamp.
$\Phi_{L o m p}=\Phi_{0}-\Phi_{t}=\Phi_{m d}+\Phi_{d v}+\Phi_{d f}+\Phi_{s r}$
where $\Phi_{0}$ is the initial luminous flux, $\Phi_{t}$ is the luminous flux after operating time $t$ and $\Phi_{\text {md }}, \Phi_{\text {div }}, \Phi_{d f}$ and $\Phi_{s r}$ are the lumen degradation caused by the LED module, LED driver and diffuser and reflector, and form factor respectively in the process of the thermal stress ageing process.

The degradation of each component/subsystem is designed based on the ageing of one component while keeping the complementary parts unaged (fresh). The degradation of each component/subsystem is evaluated based on the variation in the lumen degradation of each component, namely the LED driver, LED module, and diffuser and reflector.

$$
\begin{aligned}
& \Phi_{m d}=\Phi_{0 m d}-\Phi_{m d} ; \Phi_{d v}=\Phi_{0 d v}-\Phi_{s d v} \\
& \Phi_{d f}=\Phi_{0 d f}-\Phi_{s d f}
\end{aligned}
$$

Here $\Phi_{0 m d}$ and $\Phi_{0 m d}, \Phi_{0 d v}$ and $\Phi_{s d v}, \Phi_{0 d f}$ and $\Phi_{s d f}$ are the luminous fluxes of the LED module, LED driver and diffuser and reflector under the rated power supply, before and after operating time $t$. In this study, the degradation modelling is employed based on the Gamma process model and the exponential model along with the Weibull lifetime distribution after extrapolation of degradation path. For LED light sources, lumen degradation is considered as the main failure mode according to IESNA [42], and the lumen maintenance lifetime is defined as the operating time that $70 \%$ of the luminous flux maintained L70 from its initial light output for general applications and 50\% (L50) for decorative lighting. The luminous flux degradation for high power LED lamp can be modeled using the widely applied empirical model based on the exponential decay equation [43], [44] given as equation (3).
$\Phi_{t}=\beta^{*} \exp (-\alpha t)$
where $\Phi_{t}$ is the luminous flux after ageing for $t$ hours, $\beta$ is the projected initial constant (i.e. initial luminous flux) of the test samples, $\alpha$ is the lumen degradation rate or decay rate, $t$ is operation time in the ageing process. Here, parameters $\alpha$ and $\beta$ are estimated from historical (or experimental data) using the least-squares regression method.

In addition, the Weibull distribution is a flexible lifetime distribution that can go through the choice of two or three of the parameters, known as scale (characteristic life) $\eta$, shape (slope) $\kappa$ and location $\gamma$ parameter [45], [46]. The Weibull distribution is the most widely used lifetime distribution due to its versatile nature, taking the characteristics of other types of distributions based on a value of the shape parameter $\kappa$. For the common two-parameter Weibull lifetime distribution, the reliability function $R(t)$, probability density function $\mathrm{f}(t)$, cumulative density function $F(t)$, and failure rate function $\lambda(t)$ are given as:

$$
\begin{gathered}
R(t)=e^{-|t / \eta|^{k}} ; f(t)=\frac{\kappa}{\eta}\left(\frac{t}{\eta}\right)^{k-1} * e^{-|t / \eta|^{k}} \\
F(t)=1-e^{-|t / \eta|^{k}} ; \lambda(t)=\frac{\kappa}{\eta}\left(\frac{t}{\eta}\right)^{k-1} ; M T T F=\bar{T}=\eta . \Gamma\left(\frac{1}{\kappa}+1\right)
\end{gathered}
$$

For a lifetime analysis based on degradation data with a defined level of failure threshold, basic mathematical models are implemented for parameter estimation and reliability assessment. Accordingly, the procedure includes: (i) model parameters were estimated for each sample from recorded degradation data based on the exponential model and
least squares method; (ii) degradation data was extrapolated to predict time to failure; (iii) estimated failure data were fitted to the Weibull probability distribution to estimate the shape $\kappa$ and scale $\eta$ parameters and assess the reliability.

As discussed in the previous section, the performance characteristics of a high-power LED lamp can also be modeled based on a stochastic degradation model, the Gamma Process [14], where the degradation has a monotonic pattern and the probability density function and the reliability function for the failure distribution function are given as:

$$
\begin{aligned}
& f_{X(t)}(x \mid \mu(t), \lambda)=\left\{\begin{array}{c}
\frac{1}{\Gamma(\mu(1)) \lambda^{\mu(t)}} e^{\mu(t)-1} \exp (-x / \lambda) I_{(0, \alpha s)}(x), x \geq 0 \\
0, x<0
\end{array}\right. \\
& R(t)=1-F_{T}(t)=1-P(X(t) \geq D)=1-F_{T}(t)=\frac{\Gamma(\mu t, D / \lambda)}{\Gamma(\mu t)}
\end{aligned}
$$

where $\lambda$ is the scale parameter, $\mu$ is the shape parameter and $D$ is the failure threshold. Details of the Gamma process degradation model on LEDs are given in our previous study by Ibrahim et al. [14].

### 2.2. An overview on Bayesian Network model

Bayesian Networks (BNs), also known as belief networks or simply Bayes nets, provide a compact graphical representation of multivariate statistical distribution functions [47]. A typical BN has a set of nodes that represent random variables $X=\left\{X_{1}, X_{2}, X_{3}, \cdots, X_{n}\right\}$ and the nodes are connected by directional arcs/edges that specify conditional dependence and independence relations of the nodes. A directional cycle is not permitted among nodes in a BN based DAG. The complete structure of the nodes and arcs is called a directed acyclic graph (DAG) and it illustrates the qualitative relations among the variables.

On the other hand, the quantitative relationship among variables in BN models is determined by the conditional probability table (CPT). These conditional probabilities are used to define the joint probability function of all the nodes in the BN model graph. The joint probability density function is given as the product of all the conditional probability density functions of all nodes, given its predecessors or parent nodes [30].
$P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i} P\left(X_{i} \mid \operatorname{Pre}\left(X_{i}\right)\right)$
where $\operatorname{Pre}\left(X_{i}\right)$ denotes predecessor variables of node $X_{i}$ and $P\left(X_{i} \mid \operatorname{Pre}\left(X_{i}\right)\right)$ denotes the conditional probability function of variables $X_{i}$ given its predecessors.

The parameter estimation for the joint distribution from data is not computationally or statistically efficient as the number of model parameters grows exponentially with the number of random variables (nodes). In these cases, the conditional independence relationships help to reduce the number of distribution parameters [33]. In general, the BN models enable us to visually illustrate and work with conditional probabilistic dependencies among model variables in a particular problem. A simple BN DAG is shown in Fig. 1 to demonstrate conditional dependencies, independence, and joint distribution among random variables. According to Bayes conditional independence, "each variable is conditionally independent of its non-descendants in the graph given the value of its parents". In this example, node C is conditionally independent of nodes D and E given node values A and B, and similarly node F is conditionally independent of $\mathrm{A}, \mathrm{B}$ and D given its parent nodes C and E. Also, node C is independent of other variables (in this case node D) given its Markov blanket as shown in Fig. 1 (a) to (c).

BN uses the advantages of the Bayes theorem to update the prior failure probability given the observation of another set of variable evidence. Based on Bayes theorem, the different types of inference algorithms, such as junction tree [48] and variable elimination [49], are used to estimate the posterior probability distribution of a particular

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** Simple BN Model for conditional independence and Markov Blanket.

variable. While variable elimination inference is suitable for singly connected graphs, the junction tree algorithm is used to multiply connected graphs to perform exact inference by transforming multiply connected cases to single connected structures [48]. The conditional distribution of a node given its predecessors can be described, based on Bayes' theorem.

$$P(A|B) = \frac{P(B|A)^*P(A)}{P(B)} = \frac{P(A, B)}{\sum_A P(B, A)}$$

where *P(A|B)* is the posterior, *P(A)* is the prior, *P(B|A)* is the likelihood function and *P(B)* is the scaling factor.

In this study, the junction tree algorithm is implemented due to the additional benefits of performing exact inferences efficiently, transforming the DAG to the appropriate data structure, and ensuring consistent marginal and joint probability estimates. The joint tree inference structure of the BN model can be created based on a four-step process, (i) build initial DAG graph; (ii) construct the moral graph; (iii) triangulate the graph; and (iv) create a clique of the graph [31]. A simple demonstration of building a joint tree inference algorithm for a simple BN model with six random nodes A to F is shown in Fig. 1(d). An overview of the proposed BN based methodology for the high-power LED lamp system level reliability assessment is shown in Fig. 2.

### 2.3. Bayesian networks modelling and reliability assessment for a LED lamp system

In system level reliability assessment, the BN has a significant advantage over the traditional reliability analysis tools, such as fault tree analysis (FTA) and the reliability block diagram (RBD). While the RBD and FTA are based on a deterministic relationship between the random variables, the BN model provides probabilistic relationships. Thus, the fault trees and corresponding failure probability relationships between components can be described through the BN model DAG, where each random variable is represented with circles/nodes, and connections are made through arcs. The construction of a fault tree system focuses on the interconnections between the LED lamp components, mainly including the LED module (set of packages/engine), LED driver, and optical parts (reflector and diffuser). This helps to analyze the impact of each component on the LED lamp (system level) failure or survival.

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** An overview of the BN based methodology for reliability assessment.

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** DAG for product level LED light sources (left), 3D model exploded and assembly view (right).

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** Test sample and main components.

conditions.

To construct a DAG for a BN model, the functional and structural relationship analysis between components and failure mode and effect analysis (FMEA) are considered [1]. In the BN model constructed in Fig. 3 (left), the variables which have no parents, such as LED_CAT, LED_DEP, Driver_CAT, Driver_DEP, Solder_CAT, DifRef_DEP and DifRef_CAT, are referred as root nodes. On the other hand, the variable with no children is the leaf node (LED_Lamp), while the remaining variables are the intermediate nodes (LED_Module, LED_Diffuser, and LED_DifRef). Here, the abbreviations CAT and DEP represent catastrophic failure and performance depreciation respectively for corresponding components LED module (LED), Driver (Driver), Solder interconnect (Solder), as well as diffuser and reflector (DifRef). The root nodes have unconditional probabilities, represented here as a reliability state function of node *X*<sub>i</sub> at time *t* *R*<sub>*X**i*</sub>(*t*), i = 1,...,p, the intermediate nodes as *R*<sub>*M**i*</sub>(*t*), j = 1,...,k, and the leaf node as *R*<sub>*L*</sub>(*t*). The BN model DAG analysis is based on the construction of test sample as shown 3D model with an exploded and assembled view Fig. 3 (right).

The reliability status of each root node or component is assessed based on the corresponding prediction model at a future time *t*<sub>*o*</sub> and the reliability state prediction matrix can be represented as follows:

$$R_{pn} = \begin{bmatrix}
R_{11} & R_{12} & \cdots & R_{1o} \\
R_{21} & R_{22} & \cdots & R_{2o} \\
\vdots & \vdots & \ddots & \vdots \\
R_{p1} & R_{p2} & \cdots & R_{pn}
\end{bmatrix} \tag{9}$$

The reliability state of the intermediate nodes can also be predicted based on the prediction models of the root nodes *U* = {*R*<sub>*L*</sub>, *R*<sub>*Z**i*</sub>, ..., *R*<sub>*p*</sub>} and the assumption of conditional independence:

$$P(R_{Mi}(t)) = \sum_{U} P(R_{Mj}(t), R_{Xi}(t)) \tag{10}$$

Similarly, the reliability state of the leaf node can be predicted based on the probability of the intermediate and root nodes as follows and the junction tree algorithm synchronizes the DAG of the BN model for product level lifetime prediction.

$$\begin{aligned}
P(R_{L}(t)) &= \sum_{Pn} P(R_{X1}(t), \dots, R_{Xp}(t), R_{M1}(t), \dots, R_{ML}(t), R_{L}(t)) \\
&= \sum_{Pn|L|} P(R_{L}(t)|Pa(R_{L}(t)), \sum_{Pn|Mj|} P(R_{M1}(t)|Pa(R_{M1}(t)), \dots \\
&\sum_{Pn|Mk|} P(R_{Mk}(t)|Pa(R_{Mk}(t)), \dots, P(R_{X1}(t)), P(R_{Xp}(t))
\end{aligned} \tag{11}$$

Here *Pa*(*L*), *Pa*(*M**j*) and *Pa*(*Mk*) are the parent nodes for leaf node L,

Table 1 The basic parameters of test samples and components.


intermediate nodes $M_{j}$ and $M_{k}$ respectively.

## 3. Experimental setup and data collection

### 3.1. Test samples

The test sample in this study was a 12 W high power phosphorconverted white LED spot lamp. The LED package is a commonly used 2835 type which consists of an InGaN based blue chip covered with a yellow phosphor [50]. The LED module in a lamp consists of 54 LED packages with a minimum of 0.19 W power, as well as an LED driver, diffuser, reflector, and housing. The test sample and its components are shown in Fig. 4.

The lumen efficacy of the high-power LED spot lamps (test samples) is $>60 \mathrm{~lm} / \mathrm{W}$ while the luminous flux is around 730 lm . The technical description and specification of the test samples are shown in Table 1.

### 3.2. Accelerated degradation test for LEDs

In this study, a high temperature accelerated degradation test was conducted on high power LED spot lamps, aimed at assessing the lifetime of LED lamps at the system level by investigating the impact of component degradation on product level performance degradation. In addition, the interconnections between subsystems, such as drivers, LED packages, diffusers, and other auxiliary components, were also analyzed. The experiment further enables exploration of additional reliability information, such as failure modes, mechanisms, mean time to failure (MTTF), and estimation of remaining useful life (RUL) of the

LED lamp system at the accelerated test situation, as designed.
In this experiment, twenty test samples of LED spot lamps from the same batch were prepared in four groups. Each group consisted of five test samples, where the first group was for the product level degradation test, while the second, third, and fourth groups were for component level degradation tests, namely LED module, LED driver and LED diffuser, and reflector respectively. The test samples in all groups were aged under an elevated temperature of $55^{\circ} \mathrm{C}$ for a total of 2160 h . The colorimetric and photometric parameters were collected every 240 h , for about ten cycles including the initial test. In general, the experiment had three phases; ageing, cooling, and testing, which continued until sufficient degradation data were obtained. The overall experimental setup and data collection procedure are shown in Fig. 5.

### 3.2.1. System level ageing and data collection

The LED lamp system level ageing test was conducted according to the experimental setup and procedure are shown in Fig. 6 and described as follows: first, the test samples were placed inside a thermal chamber set at $55^{\circ} \mathrm{C}$ and supplied with an AC power source. Then the samples were kept for 240 h and cooled down for about 2 h to prepare for colorimetric and photometric parameter measurement in an integrating sphere (EVERFiNE SPEKTRON Coating, Model YF1000 lamp complete analysis system). An Infrared (IR) camera (Model Fluke Ti55FT) was used to measure the temperature distribution of the lamps at the surface of each component, including the driver, LED module, reflector, diffuser, and housing. Thermocouples were connected to the samples to measure the case temperature of the LED package, and driver while a multiparameter electronic tester was used to in-situ detect the electrical parameters (such as current, voltage, input power) for each LED lamp test sample. After that, the samples were placed back in the thermal chamber and the tests were conducted repeatedly. After 240 h of ageing, the samples were taken out to cool down for about 2 h and continued optical tests one by one to gather direct performance data, including luminous flux, chromaticity coordinates, SPD, CRI, and CCT. The cycles continue until failure occurred or sufficient degradation data were obtained.

### 3.2.2. Component level ageing and data collection

The component level ageing test experimental setup and procedure is shown in Fig. 6. Firstly, the accelerated degradation test procedure for

Product and Component Level Thermal Degradation Test

![img-4.jpeg](img-4.jpeg)

Fig. 5. Experimental setup and data collections.

![img-5.jpeg](img-5.jpeg)

**Fig. 6.** Experimental setup for thermal ageing and optical measurement (a) system level (b) LED module component (c) LED driver component (d) LED diffuser and reflector.

The LED module is presented as depicted in Fig. 6 (a). The electrical configuration of packages in the LED modules was as follows: 54 LEDs are arranged in six groups of LEDs connected in parallel and each group had nine LEDs connected in series. Each LED is rated with 40 mA current and thus 240 mA is the rated current of the LED module (DC power) in a thermal chamber set at 55 °C.

Similarly, the samples were taken out of the thermal chamber after 240 h and cooled for about 2 h to room temperature for further optical testing in an integrating sphere. Secondly, the LED driver is a subsystem or component in the LED lamp comprised of resistors, MOSFET, and capacitors designed to supply and regulate the power to another component. In this study, the driver was treated as a black-box and supplied with an AC power loaded with an equal power LED module. Similarly, it underwent thermal ageing for the specified time and tested for optical performance after assembling with a fresh LED package, as shown in Fig. 6 (b) and (c). Thirdly, the degradation test on diffusers and reflectors relies mainly on the material degradation test. The commonly used materials for a diffuser is Polymethyl Methacrylate (PMMA) also known as acrylic glass or simply acrylic and reflector materials are Microcellular PET [51]. The thermal ageing test of these components relatively easier as it doesn't require a power supply or load to it while in the thermal chamber. After ageing at 55 °C for 240 h, it was cooled down for about 2 h to an ambient temperature of 25 °C and assembled with fresh LED driver and package subassembly for an optical test to gather lumen depreciation, chromaticity shift and SPD data as shown in Fig. 6 (d). The test cycle continues until it was terminated when the component shows significant degradation or failure as per the experiment design.

### 4. Results and discussion

#### 4.1. Lumen degradation analysis for LED lamp and components

First, the lumen degradation measured for the LED lamp test samples under thermal ageing is shown in Fig. 7 (a). It can be noted that the total lumen maintenance (LM) at the termination of the experiment for the five samples was 71.23%, 74.37%, 73.71%, 72.18%, and 71.85% respectively. Similarly, the color shift showed a significant degradation for the test samples with du'v' 0.00877, 0.00769, 0.00763, 0.00885, and 0.00856 respectively.

Secondly, the influence of LED module degradation Φ*vul* on the LED lamp lifetime is described based on the experimental results, as shown in Fig. 7 (b). The LED module lumen degradation caused lumen maintenance of respectively 70.7%, 77.7%, 70.9%, 67.7%, and 73.6% for the five test sample LED lamps with a 28% average lumen depreciation. It can be noted from the results that the LED modules contribute significantly to the degradation of the LED lamp, and test sample 4 was below the lumen maintenance threshold (failed), while the other samples were close to the threshold.

Thirdly, the influence of the LED driver degradation Φ*dr* on the LED

![img-6.jpeg](img-6.jpeg)

**Fig. 7.** (a) Lumen maintenance for LED lamps, (b) Lumen maintenance of LED lamp due to LED modules, (c) Lumen maintenance of LED lamp due to LED driver, (d) Lumen maintenance of LED lamp due to LED diffuser and reflector.

### **Table 2**


### **Table 3**


![img-7.jpeg](img-7.jpeg)

**Fig. 8.** Lumen maintenance reliability prediction of LED module, LED driver, LED diffuser and reflector.

![img-8.jpeg](img-8.jpeg)

**Fig. 9.** Lumen maintenance based lifetime prediction for LED module, driver and diffuser and LED lamp based on BN method.

![img-9.jpeg](img-9.jpeg)

**Fig. 10.** Lifetime prediction based on lumen maintenance data for LED lamp using the Gamma Process.

lamp lifetime is based on the experimental results shown in Fig. 7 (c). The total lumen depreciation due to the LED driver caused an average of 6.97% lumen degradation to the LED lamp with each sample 2.8%, 8.2%, 7.3%, 5.5%, and 11.1% respectively. Finally, the influence of the diffuser and reflector degradation ΦdF on the LED lamp lifetime is shown in Fig. 7(d). The total lumen depreciation due to the LED diffuser and reflector degradation, caused 2.58% lumen degradation to the LED lamp after 2160 h of ageing time. The lumen maintenance degradation of the test samples due to optical part ageing was not significant according to the experimental results.

Under the designed ageing condition, the overall influence of LED components/subsystems on the LED lamp level degradation is summarized in Table 2. The main cause of degradation for the LED lamp was due to the degradation of the LED module, secondly, driver degradation and the least degradation was due to diffuser and reflector.

$$
P(R_I(t)) = \sum_{A} P(R_A(t), R_B(t), R_C(t), R_D(t), R_E(t), R_F(t), R_G(t), R_H(t), R_I(t), R_J(t)) = \sum_{A,B} P(R_C(t) | R_A(t), R_B(t)) \cdot \sum_{F,G} P(R_F(t) | R_D(t), R_E(t)) \cdot \sum_{C,D, E} P(R_F(t) | R_C(t), R_H(t), R_E(t)) \cdot \sum_{G,H} P(R_I(t) | P(R_G(t), R_H(t)) \cdot \sum_{F,G,H} P(R_I(t) | R_F(t), R_G(t), R_H(t)) \cdot P(R_A(t)) P(R_B(t)) (R_H(t)) P(R_E(t)) (R_G(t)) P(R_H(t))
$$

### 4.2. BN based lifetime prediction at component and product level

According to the experimental design and setup, degradation ageing tests at the system level and component level were conducted. The experimental results for both component and system levels degradation were presented in the previous section. Here, the reliability state prediction based on the degradation models proposed is presented in Table 3. All the prediction models at the component and product level used 45% (960 h) of the degradation data. The degradation model for the root nodes (i.e. component level) used in this study, along with the model parameters and descriptions, is presented here:

Based on the product architecture and functionality of the high-power LED lamp, the BN was constructed and the reliability assessment of the components and LED lamps was accomplished. In the experiment, no catastrophic failures were observed which allows us to consider the degradation of the LED lamp and its components, mainly the LED Module, LED Driver and LED diffuser and reflector. Based on the degradation models and parameters estimated (in Table 3), the reliability curves are shown Fig. 8.

For ease of algebraic representation, let A = LED_DEP, B = LED_CAT, C = LED_Module, D = Driver_DEP, E = Driver_CAT, F = LED_Driver, G = DifRef_DEP, H = DifRef_CAT, I = LED_DifRef and J = LED_Lamp. The reliability state probability of the LED lamp (node J) and intermediate nodes LED module (node C), LED driver (node F) and diffuser and reflector (node I) can be expressed as follows:

This BN model can be solved by using the Junction tree algorithm based on the Bayes Net Toolbox (BNT) for MATLAB developed by Murphy [52], and the results are plotted in Fig. 9. This equation (12), can be further simplified by setting P(RB(t)) = P(RB(t)) = P(RH(t)) = 1, when catastrophic failures are not observed in the experimental results and given as:

$$
P(R_I(t)) = \sum_{A} P(R_C(t) | R_A(t)) \cdot \sum_{D} P(R_F(t) | R_D(t)) \cdot \sum_{C,D} P(R_F(t) | R_C(t), R_D(t)) \cdot \sum_{G} P(R_I(t) | P(R_G(t)) \cdot \sum_{F,G} P(R_I(t) | R_F(t), R_G(t)) \cdot P(R_A(t)) (R_H(t)) (R_G(t))
$$

![img-10.jpeg](img-10.jpeg)

**Fig. 11.** Comparison of reliability prediction for LED Lamp (system level) based on BN and GP.

The reliability prediction plot exhibits the impact of component's degradation (intermediate nodes LED_DEP, Driver_DEP, and DifRef_DEP) on the lifetime of the high power white LED lamp (leaf node LED_Lamp), as shown in Fig. 9. It is also worth noting that the degradation of the LED module has more influence than the LED driver, diffuser, and reflector for the product level lifetime status. The absence of a catastrophic failure mode for the components, as well as the product, is displayed as a straight line in all the reliability function plots. Furthermore, the reliability plot trace for LED module due to depreciation and predicted values coincide, and this applies to the case of LED drivers and optical parts (diffuser and reflector).

On the otherhand, the lifetime estimation of LED lamp based on the BN model (shown in Fig. 9) is validated by a counterpart system level (LED lamp) degradation analysis. The Gamma process model is employed to model the lumen degradation of LED lamp test samples. The Gamma process is selected due to a monotonic degradation pattern recorded in the experiment. The lifetime prediction of LED lamp is shown by the reliability trace plot and CDF in Fig. 10.

In this BN model, the reliability prediction result indicated that the LED module has a significant impact on the degradation of the LED lamp followed by LED drivers and optical components (diffuser and reflector). In fact, the BN based model results also illustrated that the system level reliability estimation highly depends on the component level reliability prediction methods. In our study, the Gamma process and exponential decay were chosen to model components degradation path due to its suitability for the nature of the data observed. Therefore, appropriate use of lifetime prediction methods at the component level, with proper experimental setup and data acquisition provides a better capability for lifetime assessment of more complex products and systems. As can be seen from the analysis results, the BN model integrated the lifetime data from components based on the specified prediction model to estimate the degradation status at the LED lamp (i.e. system) level.

### 4.3. Discussion based on analysis results

The degradation data from LED components were analyzed using the BN model while system level lumen degradation data was examined using the Gamma process model. Based on the analysis of the component level and system level degradation data, a comparison of lifetime prediction using lumen maintenance data is shown in Fig. 11.

It can be verified from the reliability trace plots that the BN enables to achieve integration of LED component degradation data to reasonably predict the system level lifetime of a LED lamp. The expected lumen maintenance lifetime L70 for the LED lamp based on the BN method is estimated as 2360 h , while the Gamma process gives a more conservative result of about 2000 h . Using the exponential decay model, the lifetime prediction for the LED lamps showed 2492.6 h with model parameters estimated using the nonlinear least-squares (NLS) regression approach, as $\alpha=1.52 \mathrm{E}-04, \beta=1.023328$. When the prediction results are compared with the experimental findings, it had shown good compatibility, even though the experimental failure times exceeding the threshold were not obtained to estimate prediction error.

The prediction results for LED lamps based on the BN model showed steady nature compared to the Gamma process model. This can be seen from the reliability plots that the BN curve was slower in the first 2000 h while the GP trace was slowed in the first 1500 h and both curves started to drop faster thereafter. This is because the BN model was influenced by the slow degradation of the LED module until it reaches a certain threshold and the degradation process was quicker in the later degradation phases.

In general, the BN method with a systematically designed ADT enables to achieve the long term lifetime estimation of LED lamps based on component degradation data. The prediction models at component and system level used $45 \%$ ( 960 h ) of overall degradation data, which
benefits in shortening longer testing time for highly reliable high-power LED products. The lifetime prediction for the LED lamps based on the BN model was also validated with the analysis of LED lamp reliability using the Gamma process method. Thus, it can be concluded that the BN model offers a comprehensive and effective approach for lifetime prediction and reliability assessment of LED lamp products/systems and can be beneficial for LED manufacturers and customers as well as this method could be employed to assess the reliability of other complex products.

## 5. Conclusions

In this study, an accelerated degradation test based on thermal stress was implemented to evaluate the reliability of a high-power LED lamp system. A Bayesian Network (BN) method was proposed to predict the lifetime of a high-power LED lamp system by considering its intricacy, functional interaction among components, and degradation of subsystems on system level reliability. The component level lifetime prediction was carried out based on the Gamma process model and the Weibull distribution method. The junction tree algorithm was used in the BN structure to estimate the joint probability distributions of system level lifetime states. This was validated based on system level LED lamp degradation tests and system level reliability predictions based on the Gamma process and exponential LSR methods. The proposed BN model shows highly accurate lifetime prediction results and improves the reliability assessment outcomes for LED manufacturers and end-users. The BN prediction results were also compared with the experimental findings and showed good compatibility even though the failure times were not obtained for numerical quantification. Many of the SSL manufacturers obtain components from different suppliers and they have to test the product for a long time after the components are assembled. As many of the component supplier companies test their products before releasing to the market or supply to customers, the assembly companies can use the BN to get a close estimation of the system reliability based on the data from their suppliers. This reduces much of the cost and long testing time with a proper understanding of the physics of failure scenarios. Thus, it can be concluded that the BN model offers a promising approach for lifetime prediction and reliability assessment based on component failure modes and mechanisms for LED lamp systems/systems and could be employed to other complex systems.

## CRediT authorship contribution statement

Mesfin Seid Ibrahim: Data curation, Software, Formal analysis, Writing - original draft. Jiajie Fan: Conceptualization, Methodology, Formal analysis, Writing - review \& editing, Project administration, Funding acquisition. Winco K.C. Yung: Project administration, Funding acquisition. Zhou Jing: Data curation, Software. Xuejun Fan: Supervision. Willem Driel: Supervision. Guoqi Zhang: Supervision.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgment

The work described in this paper was partially supported by the National Natural Science Foundation of China (Grant No. 51805147, 61673037) and partially supported by a grant from the Research Committee of The Hong Kong Polytechnic University under student account code RK21.

# Appendix A 

## A.1. Abbreviations

