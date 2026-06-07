# Article 

## Study on the Reliability Evaluation Method and Diagnosis of Bridges in Cold Regions Based on the Theory of MCS and Bayesian Networks

Zhonglong Li ${ }^{1, *}$, Wei Ji ${ }^{2, *}$, Yao Zhang ${ }^{1,3}$, Sijia Ge ${ }^{1}$, Haonan Bing ${ }^{1}$, Mingjun Zhang ${ }^{4}$, Zhifeng Ye ${ }^{5}$ and Baowei $\mathrm{Lv}^{5}$

## check for updates

Citation: Li, Z.; Ji, W.; Zhang, Y.; Ge, S.; Bing, H.; Zhang, M.; Ye, Z.; Lv, B. Study on the Reliability Evaluation Method and Diagnosis of Bridges in Cold Regions Based on the Theory of MCS and Bayesian Networks. Sustainability 2022, 14, 13786. https://doi.org/10.3390/ su142113786

Academic Editor: Gianluca Mazzucco

Received: 27 September 2022
Accepted: 18 October 2022
Published: 24 October 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Transportation Science and Engineering, Harbin Institute of Technology, Harbin 150090, China
2 CCCC Infrastructure Maintenance Group Co., Ltd., Beijing 100020, China
3 Henan Provincial Communications Planning \& Design Institute Co., Ltd., Zhengzhou 450018, China
4 Heilongjiang Communications Investment Group Co., Ltd., Harbin 150001, China
5 Heilongjiang Highway Development Center, Harbin 150001, China

* Correspondence: lizhonglong@hit.edu.cn (Z.L.); 18745059800@126.com (W.J.);
Tel.: +86-451-86282121 (Z.L.); +86-135-81612687 (W.J.)

Abstract: The safety assessment of bridges in cold areas under the special environmental effects of extremely low temperatures, frequent freezing and thawing, and chloride ion erosion from snow removal with deicing salt, presents challenges that requiring solving. Thus, this paper proposes a new method of safety assessment based on a combination of Monte Carlo simulation (MCS) and Bayesian theory that achieves the reliability evaluation and reverse diagnosis of the overall safety performance of reinforced concrete bridges in cold areas. Additionally, the new method accomplishes the intelligent grading of various safety performance aspects of the bridge, which provides substantial references for the maintenance and reinforcement of in-service bridges.

Keywords: bridge evaluation in cold regions; MCS; Bayesian network; reliability evaluation

## 1. Introduction

With the completion of the "13th Five-Year Plan", China's economy has entered a period of rapid development. Additionally, transportation construction is developing rapidly. Bridge engineering is an indispensable part of the transportation industry and has become the foundation of our national economy. According to the "Statistical Bulletin of the Development of the Transportation Industry in 2020", as of the end of 2020, the total number of bridges in China reached 912,800, including 6444 extra-large bridges and 119,935 bridges [1]. With the increase in the number of bridges and their years in service, some in-service bridges have gradually deteriorated. Moreover, these issues have resulted in significant safety hazards and have even led to extremely serious traffic accidents.

The daily inspection, monitoring, and evaluation of bridge structures are particularly important and can effectively ensure the long-term service safety of bridge structures. To date, assessment methods for the safety of bridge structures are mainly divided into two categories: comprehensive assessment methods based on expert experience and artificial intelligence assessment methods based on computer technology. Cold regions are the most ecologically and environmentally sensitive areas, and changes to these areas comprehensively affect the dynamic Earth system, impacting populations globally. To address certain limitations in existing evaluation methods regarding the evaluation of bridges in special environments, we consider various unfavorable environmental factors in cold regions. We achieve this by using reliability indicators and failure probability as quantitative indicators to establish a reliability evaluation method of reinforced concrete bridges in cold regions based on the combination of Monte Carlo simulation (MCS) and tests. This method can be used to evaluate and classify various safety aspects of concrete beam bridges in cold

regions. Thus, the rapid evaluation and classification of various safety aspects concerning bridges can be realized for bridge maintenance, which can direct maintenance work and guarantee structural safety of the bridge.

# 2. The Construction of the Bridge Evaluation Network and the Determination of the Node Statistical Parameters 

When the safety performance of an engineering structure is evaluated, the structure is usually required to meet safety, applicability and durability requirements. The safety evaluation of a bridge usually considers the resistance function of the main girder; the applicability is usually evaluated by the deflection limit of the main girder; and the durability is usually evaluated by the limit of the crack width of the main girder.

For reinforced concrete bridges in cold regions, the main factors affecting safety are the frequent freezing and thawing effects produced by the special environment in the area and natural or human factors such as the presence of deicing salt from artificial-snow removal from roads. These factors directly lead to the deterioration of concrete materials. With the frequent action of various variable loads, cracks in the main beam gradually develop. When water produced by frequent freezing and thawing and chloride ions in the deicing salt diffuse to the location of a steel bar, the steel bar undergoes galvanic corrosion and rusts. As a result, the bearing capacity of the structure is reduced, and the safety of the bridge is reduced. Hence, there are six main factors that affect the corrosion of steel bars and the reduction in loadbearing capacity of the structure's main reinforcement in cold environments: the yield strength of the steel bars, the initial diameter of the steel bars, the initial chloride ion concentration of the concrete, the chloride ion concentration on the surface of the concrete, the critical chloride ion concentration of steel corrosion and the depth of concrete carbonization. There are three main factors that affect the deterioration of concrete materials: the compressive strength of concrete cubes, the number of freeze-thaw cycles, and the depth of concrete carbonization.

A hierarchical evaluation model for constructing an overall safety evaluation network for reinforced concrete bridges in cold areas including these factors is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Overall safety evaluation network for reinforced concrete bridges in cold areas.
For the evaluation network model shown in Figure 1, all root nodes are continuous random variables. Assuming that any two random variables are independent of each other, each random variable obeys its own known distribution type. Their respective first-order moment information, namely, the mean and variance, are determined by experiments and literature research methods and provide data support for subsequent MCSs.

2.1. Determination of the Distribution of the Strength of the Reinforcement and the Corresponding Statistical Parameters by Testing

The strength of steel bars in reinforced concrete members is determined by the tensile testing of steel bars. The design of this test is based on "Steel for reinforced concrete Part 2: Hot rolled ribbed steel bars" (GB/T 1499.2-2018) [2] and "Test methods of steel for reinforced concrete" (GB/T 28900-2012) [3].

The steel bar sample in this test is the same material as that of the low-temperature bending test beam. The steel bar sample is an HRB335 steel bar with a nominal diameter of 12 mm . The basic parameters of the steel bar sample are shown in Table 1. The steel bar tensile test is carried out on a universal testing machine.

Table 1. Parameters of steel bar specimens.


The test data results of the steel bar tensile test are summarized, and the test data are plotted as a histogram, as shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Frequency histogram of the reinforcement strength.
Based on the basic theory of hypothesis testing, it can be concluded that at a significance level of 0.05 , the yield strength of steel bars obeys a normal distribution with a mean value of 436.7 MPa and a coefficient of variation of 0.102 .

# 2.2. Determination of the Distribution of the Concrete Strength and the Corresponding Statistical Parameters by Testing 

The concrete compressive strength test measures the axial compressive strength of concrete. The formed test piece and the low-temperature bending test beam are made from the same batch of concrete. The test is designed according to the specification "Standard for Test Methods for Physical and Mechanical Properties of Concrete" (GBT 50081-2019) [4], and the basic parameters of the formed concrete specimens are shown in Table 2.

Table 2. Parameters of the concrete specimens.


The schematic diagram of concrete compressive strength test is shown in Figure 3. The statistical test data are drawn as a histogram, as shown in Figure 4. According to the fitting

curve of the histogram, the hypothesis that the compressive strength of concrete obeys the normal distribution is proposed. After hypothesis testing on the test data, it is concluded that at the significance level of 0.05 , the axial compressive strength of concrete obeys a normal distribution with a mean value of 25.4 MPa and a coefficient of variation of 0.103 .
![img-2.jpeg](img-2.jpeg)

Figure 3. Concrete compressive strength test.
![img-3.jpeg](img-3.jpeg)

Figure 4. Frequency histogram of the concrete compressive strength.

# 2.3. Determination of the Distribution of the Concrete Carbonation Depth and the Corresponding Statistical Parameters by Testing 

The carbonization of concrete has a significant impact on the properties of concrete materials and reinforcement materials. The determination of the depth of concrete carbonation is carried out in accordance with the "Technical Regulations for Testing the Compressive Strength of Concrete by the Rebound Method" (JGJT 23-2011) [5]. The test material is from the same batch of concrete as that of the bending test beam. We plot the concrete carbonization data as a histogram, as shown in Figure 5.

The distribution curve fitted in Figure 5 puts forward the hypothesis that the concrete carbonation depth obeys a log-normal distribution. Hypothesis testing theory is applied to verify this hypothesis, and it is concluded that under a significance level of 0.05 , the concrete carbonization depth obeys a log-normal distribution with a mean value of 1.5 mm and a coefficient of variation of 0.163 .

![img-4.jpeg](img-4.jpeg)

Figure 5. Frequency histogram of the concrete carbonation depth.

# 2.4. Determination and Summary of Other Root Node Statistics 

The other six root nodes in the network cannot be determined by experimental means due to time and equipment factors. Therefore, by consulting relevant domestic and foreign documents [6-8], we obtain the distribution information and first-order information of these six root nodes. The moment information, distribution and first-order moment information are as follows:

The initial diameter of the steel bar obeys a normal distribution, where the average value is 12 mm and the coefficient of variation is 0.15 .

The thickness of the concrete cover obeys a normal distribution, with an average value of 30 mm and a coefficient of variation of 0.03 .

The chloride ion concentration (mass fraction) on the concrete surface obeys the logarithmic normal distribution, with a mean value of $0.145 \%$ and a coefficient of variation of 0.10 ;

The initial chloride concentration (mass fraction) of concrete follows the logarithmic normal distribution, with a mean value of $0.006 \%$ and a coefficient of variation of 0.30 ;

The critical chloride concentration (mass fraction) obeys the logarithmic normal distribution, with a mean value of $0.04 \%$ and a coefficient of variation of 0.12 ;

The number of freeze-thaw cycles follows the lognormal distribution, with the mean of 98.17 cycles/year and the coefficient of variation of 0.154 .

The chloride ion concentration (mass fraction) on the surface of concrete obeys a log-normal distribution, with an average value of $0.145 \%$ and a coefficient of variation of 0.10 .

The initial chloride ion concentration (mass fraction) of concrete obeys a log-normal distribution, with an average value of $0.006 \%$ and a coefficient of variation of 0.30 .

The critical chloride ion concentration (mass fraction) obeys a log-normal distribution, with an average value of $0.04 \%$ and a coefficient of variation of 0.12 .

The number of freeze-thaw cycles obeys a log-normal distribution, with an average value of 98.17 times/year and a coefficient of variation of 0.154 .

The distribution information and statistical parameters of the abovementioned nodes are summarized as follows, as shown in Table 3. In the table, N represents a normal distribution, and LN represents a log-normal distribution.

Table 3. The distribution information and statistical parameters of the network root node.


# 3. Reliability Assessment of Bridge Safety Performance 

### 3.1. MCS Method and Fuzzy Reliability Theory

MCS is a method of applying basic random variable distribution information, generating random arrays that conform to the distribution, performing numerical test simulations, and statistically analyzing a large number of simulation results to approximate the failure probability of structures. MCS includes the MCS method of direct sampling, the MCS method of importance sampling, and so on. The main application employed in this article is the MCS method of direct sampling. The principle of this method is briefly described below $[9-11]$.

Assume that the joint probability density function of the basic random vector of the structure is $f_{\mathrm{x}}(\mathrm{x})$. The limit state equation is:

$$
Z=g(\mathrm{X})
$$

The failure probability of the structure is:

$$
\begin{aligned}
p_{f} & =P[g(\mathrm{X}) \leq 0] \\
& =\int_{\Omega: g(\mathrm{x}) \leq 0} f_{\mathrm{x}}(\mathrm{x}) d \mathrm{x}
\end{aligned}
$$

The indicative function is:

$$
I(\mathrm{x})= \begin{cases}1 & \mathrm{x} \in \Omega \\ 0 & \mathrm{x} \notin \Omega\end{cases}
$$

Introducing the indicative function into Equation (2), we can extend the integral area to the global integral, namely:

$$
\begin{gathered}
p_{f}=\int_{\mathrm{R}_{n}} I(\mathrm{x}) f(\mathrm{x}) d \mathrm{x} \\
\Omega:\{\mathrm{X} \mid g(\mathrm{X}) \leq 0\} \subseteq \mathrm{R}_{n}
\end{gathered}
$$

According to the definition of mathematical expectation in probability theory, Formula (4) can be transformed into:

$$
p_{f}=E[I(\mathrm{x})]
$$

According to the known distribution information and mean variance information of each basic random variable, a random vector array conforming to the distribution can be generated. If the generated random vector falls into $\Omega$ space, the indicator function value is 1 ; otherwise, it is 0 . We calculate the value of the indicator function in a large number of numerical simulation tests and estimate the mathematical expectation of the indicator function with the statistical average value of the indicator function to obtain the failure probability of the structure:

$$
p_{f}=\frac{1}{N} \sum_{i=1}^{N} I\left(\mathrm{x}_{i}\right)
$$

According to the failure probability, the size of the reliability index can be obtained:

$$
\beta=-\Phi^{-1}\left(p_{f}\right)
$$

Regarding the definition of deflection and crack failure in the normal service limit state of the bridge, although the specification stipulates the limit of the deflection deformation and crack width of the bridge, in actual engineering situations, when the crack and deflection do not exceed the limit, the bridge performance and durability may not be guaranteed. For the same reason, even if the two exceed the limits, it is difficult to conclude that the bridge does not meet the applicability and durability requirements. This requires blurring the boundary between the failure domain and the safety domain. Fuzzy reliability theory can solve such problems by making the failure criterion fuzzy [12-15].

Assume the limit state equation determined by the basic random vector $\mathrm{x}=\left[\mathrm{x}_{1}, \mathrm{x}_{2}, \ldots, \mathrm{x}_{n}\right]^{T}$ is $Z=g(\mathrm{X})$. The joint probability density of X is $f_{\mathrm{x}}(\mathrm{x})$. The probability density of the function $Z$ is $f_{Z}(z)$. The membership function of the fuzzy random event in the service limit state of the bridge is $\mu(Z)$, so the fuzzy failure probability of this fuzzy event is:

$$
\begin{aligned}
p_{f} & =\int_{-\infty}^{+\infty} \mu(z) f_{Z}(z) d z \\
& =\int_{\mathrm{R}_{0}} \mu[g(\mathrm{X})] f_{\mathrm{x}}(\mathrm{x}) d \mathrm{x}
\end{aligned}
$$

Our expectation for the function $Z$ of the service limit state of the bridge is that the larger the value of the function, the smaller the failure degree of the bridge. Therefore, the corresponding membership function should be a decreasing function, and thus the half-ladder membership function is chosen. According to the characteristics of the reduced-half-ladder membership function, its complementary function is:

$$
\bar{\mu}(z)=1-\mu(z)
$$

Hence, it meets the definition of the distribution function of random variables, so we define a new random variable $x_{n+1}$. The limit state equation after the failure criterion is fuzzed is:

$$
\bar{Z}=g(\mathrm{X})-X_{n+1}
$$

Its failure domain is $\Omega:\left\{\mathrm{X} \mid g(\mathrm{X}) \leq x_{n+1}\right\}$, and the reliability index and failure probability of the limit state equation after the fuzzification of the failure criterion can be obtained according to the MCS method.

# 3.2. Structural Safety Classification Based on the Reliability Index 

According to the abovementioned basic theory of structural reliability, after appropriate limit state equations and failure criteria are defined, the reliability index for evaluating the performance of the structure can be obtained. In the current structural safety performance evaluation method, the various performance aspects of the structure are usually graded according to the size of the reliability index. This paper also uses this method for the evaluation and grading of the various performance aspects of bridges.

According to the classification method in ISO 2394-2015 [16] General principles on reliability for structures [17], the performance classification of bridge structures is shown in Table 4.

Table 4. Reliability index classification table.


# 3.3. Material Degradation Model Selection 

(1) Deterioration model of concrete materials

To evaluate the reduction in concrete compressive strength, domestic and foreign researchers have proposed a variety of concrete strength degradation models. This paper applies the Jeda Yoshikuan model proposed by Japanese scholar Yoshihiro Jeda et al. [18], where distribution information of the concrete's compressive strength does not change with time and always obeys a normal distribution but the statistical parameters of the distribution that the random variable obeys change over time, namely:

$$
\left\{\begin{array}{c}
f_{c}(t) \sim N\left(\mu_{f_{c}}(t), \sigma_{f_{c}}^{2}(t)\right) \\
\mu_{f_{c}}(t)=1.4529 \exp \left(-0.0246(\ln t-1.7154)^{2}\right) \mu_{f_{c 0}} \\
\sigma_{f_{c}}(t)=(0.0305 t+1.2368) \sigma_{f_{c 0}}
\end{array}\right.
$$

where $t$-Concrete service time.
$\mu_{f_{c 0}}$-Average strength of concrete cured for 28 days.
$\sigma_{f_{c 0}}$-Standard deviation of strength of concrete cured for 28 days.
$\mu_{f_{c}}(t)$-Average strength of concrete after $t$ years of service.
$\sigma_{f_{c}}(t)$-Standard deviation of concrete strength after $t$ years of service.
The method proposed in this paper is a method for determining the reliability of reinforced concrete bridges in cold areas, mainly characterized by frequent freezing and thawing. Therefore, the concrete deterioration model expressed in Equation (12) is modified to consider frequent freezing and thawing in cold areas. The modified model [19] of the influence of intensity is as follows:

$$
f_{c E T}=k_{w / c} k_{F A} k_{a} \exp (-0.001 n) f_{c N F T}
$$

where $n$-Number of freeze-thaw cycles in the area (times/year).
$f_{c N F T}$-Axial compressive strength of the concrete before freezing and thawing.
$f_{c E T}$-Axial compressive strength of concrete after freeze-thaw cycle.
$k_{w / c}$-Concrete water-cement ratio correction coefficient.
$k_{F A}$-Correction coefficient for concrete fly ash content.
$k_{a}$-Concrete air content correction factor.
(2) Rebar corrosion model based on Fick's second law

The formation of galvanic cells is an important factor that causes corrosion of steel bars. To quantify the degree of the galvanic effect on steel bars, we determine the formation time of galvanic cells and its influence on the corrosion rate of steel bars based on Fick's second diffusion law $[20,21]$.

It is assumed that the direction of chloride ions in the environment into the concrete is one-dimensional; that is, the ions gradually diffuse only vertically inward along the edge of the concrete to the position of the steel bars, as shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. Schematic diagram of chloride ion attack on concrete.

According to Fick's second law of one-dimensional diffusion and the known initial conditions, the analytical solution of the chloride ion concentration with respect to time and diffusion depth can be obtained:

$$
C_{C t^{-}}=C_{0}+\left(C_{s}-C_{0}\right)\left[1-\operatorname{erf}\left(\frac{x}{\sqrt{4 D t}}\right)\right]
$$

where $\operatorname{erf}(\bullet)$ —Error function.
When the chloride ion concentration at the steel bar reaches the critical chloride ion concentration, the steel bar starts to corrode. By substituting the critical chloride ion concentration into Formula (13), we can obtain the time when the steel bar starts to corrode:

$$
T_{i}=\frac{C^{2}}{4 D}\left[\operatorname{erf}^{-1}\left(\frac{C_{s}-C_{c r}}{C_{s}-C_{0}}\right)\right]^{-2}
$$

where $\operatorname{erf}^{-1}(\bullet)$ —Inverse function of the error function.
$T_{i}$-Time at which the rebar begins to corrode.
The chloride ion diffusion coefficient of concrete is calculated using the Japan Society of Civil Engineers (JSCE) model [22] in the Japanese Concrete Structure Design Standard. In this model, the unit of the chloride ion diffusion coefficient of concrete is $\mathrm{cm}^{2} /$ year:

$$
\lg D=-3.9(w / c)^{2}+7.2(w / c)-2.5
$$

When the steel bars in the reinforced concrete members begin to corrode, the corrosion rate is related to the current density of the galvanic cell. The steel corrosion rate model is obtained by consulting related literature [18,19]:

$$
r(t)=\alpha i_{c 0} \times 0.85\left(t-T_{i}\right)^{-0.29}
$$

where $\alpha$-Correction factor.
$r(t)$-Rebar corrosion rate.
$i_{c 0}$-Rust initial current density.

$$
i_{c 0}=\frac{37.8(1-w / c)^{-1.64}}{C}
$$

Due to corrosion of the steel bar, the tensile bearing capacity of the steel bar is reduced. The calculation of the bearing capacity reduction of the steel bar employs the area loss rate of the steel bar to characterize the corrosion degree of the steel bar. The definition of the area loss rate of the steel bar is as follows:

$$
\rho(t)=\frac{A_{0}-A_{c}(t)}{A_{0}} \times 100 \%
$$

where $A_{0}$-Initial area of reinforcement.
$A_{c}(t)$-Remaining area of rebar at time $t$.
The corrosion of steel bars is generally divided into uniform corrosion and local corrosion. The two different forms and characteristics of corrosion are shown in Figure 7. The corrosion depths of the two different corrosion methods are:

$$
\begin{gathered}
p(t)=\int_{T_{i}}^{t} r(u) d u \\
p(t)=R \int_{T_{i}}^{t} r(u) d u
\end{gathered}
$$

where $R$-Nonuniformity coefficient of local corrosion.

![img-6.jpeg](img-6.jpeg)

Figure 7. Low-temperature bending beam test.
In the actual situation, the corrosion of steel bars usually occurs through these two types of corrosion concurrently, so the two types of corrosion areas are added when calculating the remaining area after corrosion of the steel bars to obtain the final remaining area of the steel bars.

# 3.4. Evaluation Method for Bridge Safety Performance Reliability 

(1) Low-temperature bending beam test

A total of 12 reinforced concrete test beams sized $b \times h \times L=150 \mathrm{~mm} \times 200 \mathrm{~mm} \times$ 2500 mm are poured for this test. After the test beams are made, they are placed outside in the cold environment of Harbin City at the same time as the test blocks for the concrete compressive strength test, and they are degraded in the natural environment for one year. After the degradation is complete, a low-temperature bending beam test is conducted. The size information of the test beams and the layout of the reinforcement are shown in Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. Test beam size and reinforcement.
The test beam is a simply supported beam with a rectangular single-reinforced section, and the calculated length is $L_{0}=2.2 \mathrm{~m}$. The loading method is two-point loading at the mid-span position, as shown in Figure 9. The test beam loading method uses hierarchical loading. The magnitude of the load applied at each level, the resulting deflection and the width of the crack are recorded separately. The test termination mark is the beam body. The crack width exceeds the limit of 0.2 mm . The concrete in some of the test beams is damaged during demolding and transportation. In the end, a total of 9 beams are tested for bending. The test data are summarized in Table 5. According to the data in the table and hypothesis test theory, the load data are analyzed, and it is concluded that at the end of the test, the load obeys a normal distribution with a mean value of $13,440.16 \mathrm{~N}$ and a

coefficient of variation of 0.113 . In addition, it is known by consulting the literature that the concrete density obeys a normal distribution with a mean of $2462 \mathrm{~kg} / \mathrm{m}^{3}$ and coefficient of variation of 0.105 . The above data are used as the statistical parameters for evaluating the random variables of the second-layer node load in the network, and the performance of the bridge is evaluated.
![img-8.jpeg](img-8.jpeg)

Figure 9. Test beam loading device and sensor layout diagram.

Table 5. Summary table containing test data of the low-temperature bending beams.


# (2) Safety assessment 

Figure 1 shows that the limit state equation for evaluating bridge safety is determined by the resistance function. Therefore, it is necessary to determine the internal force of the test beam due to the load and the bearing capacity of the test beam. The test beam is simplified into a simply supported beam structure calculation model. According to the basic theory of structural mechanics, the maximum bending moment of the test beam section can be calculated as:

$$
M_{d}=\frac{1}{8} \rho_{m} g b h L_{0}^{2}+\frac{1}{2} F L_{1}
$$

where $L_{1}$-Distance between the fulcrum of the test beam and the loading point close to the fulcrum, 1000 mm

According to the theory of reinforced concrete single-reinforced section beams, the compression zone height and maximum bearing capacity of the test beam section are:

$$
\begin{gathered}
x=\frac{(1-\rho) \pi f_{v} d^{2}}{2 f_{c} b} \\
M_{u}=f_{c} b x\left(h_{0}-\frac{\mathrm{x}}{2}\right)
\end{gathered}
$$

where $h_{0}$-Effective height of beam, 160 mm

According to Equations (20) and (22), the resistance function for evaluating the safety of reinforced concrete beams, that is, the limit state equation, is:

$$
Z_{1}=M_{u}-M_{d}
$$

When $Z_{1}<0$, the structure does not meet the safety requirements and is recorded as status 0 . When $Z_{1}>0$, the structure meets the safety requirements and is recorded as status 1 . According to the statistical distribution information of each random variable, the limit state equation of Formula (23) is simulated based on the MCS method, with 1-million simulations. The simulation results are recorded, and the safety failure probability and reliability index of the test beam are solved. The safety of the test beam is evaluated; the simulation results show that the safety failure probability of the test beam is 0.0236 , and the reliability index is 1.9845 . Referencing Table 4 , we can conclude that the safety level of the test beam is five, which is consistent with the actual test results.

# (3) Applicability evaluation 

According to the bridge evaluation network in Figure 1, the applicability of the bridge is evaluated by the deflection. The test beam is simplified into a simply supported beam structure model, and the deflection of the simply supported beam can be solved by using the virtual work principle in structural mechanics. According to the load form of the test beam, the deflection of the mid-span section of the test beam can be calculated by:

$$
f=\frac{1}{B}\left(\frac{5}{66} F L_{1}^{2} L_{0}+\frac{21}{176} L_{0} L_{1} L_{2}\right)
$$

where $L_{2}$-Distance between the two loading points of the test beam, 200 mm .
$B$-Flexural rigidity of the reinforced concrete beam section.
In this paper, the method of calculating the bending stiffness of the beam section employs the concept of the effective moment of inertia of the section from the American standard ACI 318-11 Building Code Requirements for Structural Concrete and Commentary [23]. The effective moment of inertia of the section is defined as:

$$
I_{e}=\left(\frac{M_{c r}}{M_{a}}\right)^{3} I_{g}+\left[1-\left(\frac{M_{c r}}{M_{a}}\right)^{3}\right] I_{c r}
$$

where $I_{e}$-Effective bending moment of inertia of the section.
$I_{g}$-Conversion of the full section moment of inertia.
$I_{c r}$-Conversion of the cracked section to the moment of inertia of the section.
$M_{a}$-Maximum bending moment of the section, that is, the above load.
$M_{d}$-bending moment.
$M_{c r}$-Cracking moment.
After the steel bars are corroded, the effective section moment of inertia of the concrete beam inevitably decreases. To consider the loss of this moment of inertia, scholars at home and abroad have proposed many theories about the section stiffness degeneration of corroded bridges. This article uses a reduction factor method that considers the degradation of the effective section moment of inertia [24], namely:

$$
I_{c e}=\gamma(\rho) I_{e}
$$

$\gamma(\rho)$ is a function of the corrosion area rate of steel bars, and the expression is as follows:

$$
\gamma(\rho)= \begin{cases}1 & \rho \leq 0.05 \\ 1.22+12.88 \rho^{2}-5.05 \rho & \rho>0.05\end{cases}
$$

Therefore, the flexural rigidity of the test beam section is:

$$
B=E_{c} I_{c e}
$$

According to the above theory, the MCS method is used to simulate the deflection of reinforced concrete beams 1-million times, the deflection data obtained by the simulation are recorded, and the mean value of the simulated deflection data is calculated to be 2.72 mm . The test record data results in Table 5 show that the test deflection has an average value of 2.83 mm , and the relative error between the two is:

$$
\delta=\frac{2.83-2.72}{2.83} \times 100 \%=3.9 \%
$$

Within the allowable range of error, the calculated data are basically consistent with the experimental data, which proves the correctness of the simulation results.

According to provisions of the "JTG3362-2018 Code" [25], the deflection of a simply supported beam bridge should not be greater than $1 / 600$ of the calculated span length, so the limit state equation for evaluating applicability can be defined as:

$$
Z_{2}=\frac{L_{0}}{600}-f
$$

According to fuzzy reliability theory, the failure criterion is fuzzified, and the reduced half trapezoidal membership function is selected. The membership function to evaluate the applicability is:

$$
\mu(\mathrm{x})=\left\{\begin{array}{cc}
1 & \mathrm{x} \leq-0.183 \\
\frac{0.183-\mathrm{x}}{0.366} & -0.183<\mathrm{x} \leq 0.183 \\
0 & \mathrm{x}>0.183
\end{array}\right.
$$

The failure criterion after the fuzzy membership function is:

$$
\widetilde{Z}_{2}=Z_{2}-X^{\prime}
$$

When $\widetilde{Z}_{2}<0$, the structure does not meet the applicability requirements and is recorded as status 0 . When $\widetilde{Z}_{2}>0$, the structure meets the applicability requirements and is recorded as status 1 . According to the statistical parameters of the aforementioned random variables, the MCS method is used to perform 1-million simulations to obtain the failure probability and reliability indicators of the test beam's applicability.

According to the simulation results, the applicability failure probability of the test beam is 0.0450 , and the reliability index is 1.6959 . Compared with Table 4 , it can be concluded that the applicability level of the test beam is five, which is similar to the actual test results.

# (4) Durability evaluation 

According to the bridge evaluation network in Figure 1, the crack width is used to evaluate the durability of the bridge. In this section, we use the large-scale general finite element software Ansys to numerically simulate the crack width of the test beam. The reinforced concrete beam model established in this paper is a separate model; that is, different element types are selected to simulate the steel and concrete to simulate the maximum size of the test beam. For the crack width, the bond slip between the steel bar and concrete should also be considered in the model, and the bond element is used to simulate this effect.

In Ansys, the Solid65 element is usually used to simulate the nonlinear properties of concrete. This element can simulate the nonlinear behavior of concrete by setting the element attribute parameters and defining the real constants of the material; the reinforcement is simulated by the Link180 element, and the real constants are also used for simulation [26]. To describe the nonlinear constitutive structure of the steel bar material, the bond and slip between the steel bar and concrete is simulated by the spring element Combin39, which is a nonlinear spring element whose spring characteristics are defined by the load-displacement

curve. Therefore, by converting the bond-slip model of the steel bar and concrete into a load-displacement function, we can use the spring to simulate the bond-slip effect by defining the real constant. The nonlinear constitutive model of concrete is the multilinear follow-up strengthening model in the Chinese code. The elastic modulus of concrete is taken as the initial elastic modulus in the strengthening model, Poisson's ratio is 0.2 , the uniaxial tensile strength of concrete is taken as one tenth of the compressive strength, the shear transfer reduction coefficient of open cracks is taken as 0.4 , and the shear transfer reduction coefficient of closed cracks is taken as 0.9 . In order to make the structural model converge quickly, the crushing of concrete elements is closed; The nonlinear constitutive model of reinforcement applies the strengthening model of two broken lines. The elastic modulus of reinforcement is $20,000 \mathrm{MPa}$ and Poisson's ratio is 0.3 . After entering the strengthening stage, the strengthening elastic modulus is $10 \%$ of the initial elastic modulus, namely 2000 MPa . The nonlinear constitutive models of concrete and steel bars are:

$$
\begin{aligned}
& \sigma_{c}=\left\{\begin{array}{lc}
f_{c}\left[1-\left(1-\frac{\varepsilon_{c}}{0.0021}\right)^{2}\right] & \varepsilon_{c} \leq 0.0021 \\
f_{c} & 0.0021<\varepsilon_{c} \leq 0.0033
\end{array}\right. \\
& \sigma_{s}=\left\{\begin{array}{cc}
20000 \varepsilon_{s} & \sigma_{s} \leq f_{s} \\
f_{s}+2000\left(\varepsilon_{s}-\frac{f_{c}}{20000}\right) & \sigma_{s}>f_{s}
\end{array}\right.
\end{aligned}
$$

The bond between concrete and steel bars can be used to derive the load-displacement curve required by the Conbin39 element by applying the fourth-order polynomial function between the bond stress and slip, which was fitted by Houde through experiments in 1965:

$$
F=\left(5.3 \times 10^{2} D-2.52 \times 10^{4} D^{2}+5.87 \times 10^{5} D^{3}-5.47 \times 10^{6} D^{4}\right) \sqrt{\frac{f_{c}}{40.7}} \times \pi d l
$$

The finite element model is established according to the abovementioned material constitutive relationship and the size of the test beam. Since the structure is symmetrical with symmetrical loads, to simplify the calculation and to reduce the calculation error, a semi-structured finite element model is established. The established finite element model is shown in Figure 10.
![img-9.jpeg](img-9.jpeg)

Figure 10. Semi-structure-separated finite element model.
This paper uses the Ansys method proposed by Tian Shuangzhu et al. to calculate the maximum crack width of reinforced concrete members under load. This theory states that after concrete cracks under load, the crack width can represent the difference between the strain of steel and the strain of concrete. Compared with the strain of the steel bar, the strain

of the concrete can be ignored, and thus the following formula is proposed to calculate the crack width with the aid of finite element software:

$$
\omega_{m}=0.85 \varphi \sum_{i=1}^{m} \varepsilon_{s i} \Delta L_{i}
$$

where $\omega_{m}$-Average crack width.
$m$-Number of units in the average crack spacing.
$\varepsilon_{s i}$-Rebar strain of the $i$-th element in the crack spacing.
$\Delta L_{i}$-Length of the $i$-th unit in the crack spacing.
$\varphi$-Nonuniformity coefficient of the steel bar strain.
In the end, the maximum crack width of reinforced concrete members under load can be twice the average crack width, namely:

$$
\omega_{\max }=2 \omega_{m}
$$

The calculation results of the Ansys nonlinear model are used to extract the corresponding element length, steel-bar stress and strain, and the maximum crack width of the test beam can be simulated according to the above formula. Figure 11 shows the model strain cloud diagram and the crack width calculated by the test data.
![img-10.jpeg](img-10.jpeg)

Figure 11. Strain cloud diagram of the test data and calculation result of crack width.

According to the modeling process of the abovementioned finite element model, a simulation system for the crack width of reinforced concrete beams is established based on the MCS method. The cross-sectional area of the steel bar $A_{s}$, compressive strength of concrete $f_{c}$, yield strength of the steel bar $f_{s}$ and load $F$ are used as system input, and the APDL language of Ansys is used to establish a finite element crack width calculation model. Finally, the maximum crack width of a reinforced concrete beam calculated by the finite element model is used as the system output, and a crack simulation system is constructed with the help of macro commands. The total number of simulated cracks is 500,000.

According to data processing, the average crack width obtained by finite element calculation and simulation is 0.2474 mm , and the average crack width measured by the low-temperature bending beam test is 0.2433 mm . The error between the two is:

$$
\delta=\frac{0.2474-0.2433}{0.2433} \times 100 \%=1.7 \%
$$

Within the allowable range of error, the finite element simulation data and the experimental data are basically consistent, which proves the correctness of the simulation results.

According to provisions of the "JTG3362-2018 Code" [25], when reinforced concrete beams are used in a freeze-thaw environment, the width of cracks generated by the beam body should not be greater than 0.2 mm , so the limit state equation that defines the applicability of the evaluation is:

$$
Z_{3}=0.2-\omega_{\max }
$$

The membership function for evaluating the durability of bridges is:

$$
\mu(\mathrm{x})=\left\{\begin{array}{cc}
1 & \mathrm{x} \leq-0.01 \\
\frac{0.01-\mathrm{x}}{0.02} & -0.01<\mathrm{x} \leq 0.01 \\
0 & \mathrm{x}>0.01
\end{array}\right.
$$

The limit state equation after the failure criterion is fuzzified is:

$$
\overline{Z}_{3}=Z_{3}-X^{\prime \prime}
$$

When $\bar{Z}_{3}<0$, the structure does not meet the durability requirements, and it is recorded as status 0 . When $\bar{Z}_{3}>0$, the structure meets the durability requirements and is recorded as status 1 .

According to the crack simulation results, the fuzzy limit state equation is simulated by the MCS method 500,000 times, and the failure probability and reliability index of the durability of the test beam are obtained.

According to the calculation results, the reliability index of the test beam durability is -1.0 , the grade evaluation is five, and the failure probability reaches $84.13 \%$. In the test, the load termination condition is that the reinforced concrete beam crack exceeds the limit. The measured value only has two test beam cracks that have not exceeded the limit, and the simulation results are in good agreement with the actual conditions, again verifying the scientific veracity of the evaluation method.

# 4. Reverse Diagnosis Based on Bayesian theory 

Bayesian network theory is derived from the combination of probability theory and graph theory. Its main advantage is that it decouples complex factors that affect the outcome of events according to whether they are independent of each other. A network is built based on the causal relationship between various factors based on graph theory and the relationship between various factors is reflected in the form of a conditional probability table to realize the reverse diagnosis of the main factors that induce the event.

According to the overall safety assessment network of reinforced concrete bridges in cold areas constructed in Section 2.1, a three-layer and 14-node Bayesian network is constructed. To simplify the calculation, the frequency distribution histogram is drawn

based on the data generated by the first-level nodes of the network using the MCS method, and the continuous random variables of the first-level nodes are transformed into threestate discrete random variables according to the grouping in the histogram as the prior probability of these nine root node factors. The software Netica is used to build a Bayesian network that evaluates the overall safety performance of the bridge.

The prior probability and likelihood of all root nodes is input into the Bayesian network of the overall safety performance evaluation of the bridge, the parameter setting is completed, and the Bayesian network is activated. In Section 3, the results of the evaluation of performance and durability applied to the safety of the test beams are all five levels, so the status of the three leaf nodes in the network is set to 0 ; that is, the safety, applicability and durability of the test beam are all in a failed state. Therefore, the test beams are used to diagnose the main risk factors for the failure and to solve the posterior probability of the second-layer nodes of the network; after determining the main risk factors for the second layer of the network, we adjust the risk factors to the most unfavorable state and solve the first layer of the network again. The posterior probabilities of the nodes can be used to determine the main risk factors. The posterior probabilities of the most unfavorable states of all nodes in the network are summarized in Table 6.

Table 6. Summary of the posterior probability of nodes in the Bayesian network.


From the posterior probability calculated by the Bayesian network, it can be concluded that the main risk factor for failure of the test beam is insufficient concrete strength. The posterior probability of this node in the first layer of the network is the largest at $2.80 \%$. The actual conditions of the test beams using C25-labeled concrete are consistent, followed by the number of annual freeze-thaw cycles with a posterior probability of $2.14 \%$, which is the most important environmental factor in causing failure of the test beam; the largest posterior probability in the second layer of the network, the probability of the steel bar strength reduction node is $95.5 \%$. From this, it can be inferred that the concrete strength of the test beam becoming too low and the steel bars corroding due to frequent freezing and thawing result in decreased safety performance of the test beam. This makes it difficult to meet the structural safety requirements.

# 5. Conclusions 

In this paper, a network model for evaluating the safety performance of reinforced concrete bridges in cold regions was constructed, and the statistical information of the root nodes of the network was determined through experiments and literature research. Furthermore, based on low-temperature bending beam tests and the MCS method, the safety and applicability of the bridge structure were evaluated. Relying on the methods of calculating the failure criterion and durability and reliability indexes, in addition to performing bending beam tests to measure the test beam reliability index and according to the specifications, we grade the safety, applicability and durability of the structure according to the reliability indexes and verify the results with experiments. The evaluation

method is highly consistent with real engineering conditions and can provide technical support for the safe operation and maintenance of bridge structures. Finally, based on the Bayesian network theory, a Bayesian network model for bridge assessment was constructed to realize reverse diagnosis of the main risk factors for the bridge, and the correctness of the assessment method and diagnosis method was verified via low-temperature bending beam tests.

Author Contributions: Conceptualization, Z.L., H.B., M.Z. and Z.Y.; software, W.J., Y.Z. and Z.Y.; validation, Z.L. and W.J.; formal analysis, Z.L. and H.B.; investigation, Y.Z.; resources, Z.L., W.J., S.G. and M.Z.; data curation, Y.Z. and B.L.; writing—original draft, Y.Z. and H.B.; writing-review \& editing, Z.L. and S.G.; visualization, Z.L. and H.B.; supervision, Z.L., W.J. and M.Z.; project administration, S.G., M.Z., Z.Y. and B.L.; funding acquisition, W.J. and B.L.. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
