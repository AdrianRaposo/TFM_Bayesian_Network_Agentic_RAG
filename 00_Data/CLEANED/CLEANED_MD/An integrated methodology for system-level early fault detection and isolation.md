# 1 An Integrated Methodology for System-Level Early Fault Detection 

## 2 and Isolation

3 Jinxin Wang ${ }^{\mathrm{a}, \mathrm{b}, *}$; Xiuquan Sun ${ }^{\mathrm{c}}$; Chi Zhang ${ }^{\mathrm{b}}$; Xiuzhen $\mathrm{Ma}^{\mathrm{b}}$
$4{ }^{a}$ School of Safety Engineering, China University of Mining and Technology, Xuzhou 221116,
5 China
$6{ }^{b}$ College of Power and Energy Engineering, Harbin Engineering University, Harbin 150001,
7 China.
$8{ }^{c}$ Centre for Efficiency and Performance Engineering, University of Huddersfield, Huddersfield
9 HD1 3DH, UK.

[^0]
[^0]:    *Corresponding author.
    E-mail addresses: wangjinxin@cumt.edu.cn (J. Wang). xiuquan.sun@hud.ac.uk (X. Sun). zhangchi2018@hrbeu.edu.cn (C. Zhang). maxiuzhen@hrbeu.edu.cn (X. Ma).


A high-performance and reliable mechanical system is an ever-constant objective in all mechanical technological innovations. Fault diagnosis is an indispensable technique to ensure the high-performance and safe operation of a mechanical system during its life-cycle. Currently, single component diagnostics has already received considerable attention from researchers, while the diagnostics of a whole system is found limited. In practice, a large-scale system usually consists of plenty of components. Single fault diagnostic method is often found inefficient and error-prone to find out the real root causes. Whereas, a system-level fault diagnosis strategy takes all the potential faults into consideration in the process of troubleshooting, which therefore can give a more reasonable result compared with single component diagnostics.

Some works have devoted to develop the system-level fault diagnostic methodology from different aspects. For example, researchers believe that optimal sensor placement is the precondition for multiple fault diagnosis (Gangsar, \& Tiwari, 2020; Duan, Lin, \& Feng, 2018; Sahoo, Yin, \& Liu, 2019; Chen, Chen, Ding, \& Wu, 2018; Perelman, Abbas, Koutsoukos, \& Amin, 2016; Sen, Narasimhan, \& Deb, 1998). Travé-Massuyès et al (2006) presented an analytical redundancy relations (ARRs)-based approach for optimising sensor placement. Krysander et al. (2008), Khemliche et al. (2006), Rosich et al. (2012) and Chi et al. (2015)

presented different improvements via different methods. In terms of fault isolation, various pattern recognition algorithms have been successfully applied to pinpoint the real root cause for an abnormality (Jang, Park, \& Baek, 2017; Yu et al., 2021; Pulido, Zamarreño, Merino, \& Bregon, 2019; Taktak, Triki, \& Kamoun, 2017; Lopez, \& Sarigul-Klijn, 2010). Cai et al (2021) proposed a Bayesian network-based approach for large-scale system multiple fault diagnosis by taking uncertainties into consideration. Despite new technologies keep falling into the category of system-level fault diagnosis, existing approaches only focus on one aspect (dynamics modeling, fault feature extraction, fault isolation and decision-making, etc.), which makes the proposed methods difficult to be combined with other technologies and successfully implemented in the practice of an engineering system. Little research provides a comprehensive as well as general diagnostic procedure at a system level, based on which a complete fault diagnosis system can be developed.

This paper gives an integrated methodology for system-level fault detection and isolation based on fault behaviour analysis, optimal sensor placement and intelligent data analytics for multiple fault detection and isolation. Particular considerations are given to the system response characteristics analysis under various faults and early fault detection and abnormal parameter separation. In terms of fault behaviour analysis, correlation analysis and fault tree are known as two primary methods to

82 characterise the system failures using a set of observable parameters. 83 Correlation analysis evaluates whether there exists a relationship between 84 the two parameters and how strong it is according to statistical theory. 85 This method has already been successfully used in different mechanical 86 systems and facilities, e.g. rolling bearing (Chen, Toyota, \& He, 2001) 87 and crankshaft (Sekhar, 2008). Although being well-accepted, this 88 approach usually calls for a great quantity of sample data, which is not 89 always available in practice, especially when it comes to the major faults 90 with heavy losses. Fault tree is another method for fault behaviour analysis. Different from correlation analysis, this method takes the most 92 undesired fault as Top Event, and then describes the propagation path and 93 manifestation on observable parameters according to the working 94 principles of the system (Khakzad, Khan, \& Amyotte, 2011; Knezevic, 95 Orovic, Stazic, \& Culin, 2020). The multi-dimensional causal 96 relationships of interested faults and observable parameters are attained 97 by exploring the fault tree. Despite sample data is not needed in the 98 process of fault behaviour analysis, the fault tree model is constructed in 99 light of experts' knowledge, which makes that different or even 100 conflicting diagnostic results may be derived. Mathematical model-based 101 approach is an alternative approach to obtain the causal relationships of 102 faults and parameters. This approach takes advantage of a set of analytic 103 equations to depict the behaviour characteristics of the mechanical system.

The causal relationships among faults and parameters are then derived via transforming these equations. Mathematical model-based approach gets rid of the dependency on sample data and experts' experience, and provides an objective approach for fault behaviour analysis. Nevertheless, constructing a higher-fidelity mathematical model is known as a time-consuming and fault-prone work, which limits this method being widely applied in real-world situations. Mosterman et al. (1999) proposed the concept of Temporal Causal Graph (TCG) and exploited the approach to analyse the transient behavior of a system. The TCG is a signal flow diagram, in which the vertices represent the system variables, and a labeled directed edge is added if there exists a functional relationship between the two vertices. The causal relationships of system variables are obtained via traversing the signal flow paths in a TCG model. The TCG makes the analysis of causality between faults and parameters free from construct elaborate analytic equations, which provides an effective solution to solve the problem of modelling complexity for fault behaviour analysis.

As for fault detection, hypothesis testing and limits checking are two commonly used approaches in practice. Hypothesis testing views fault detection task as a hypothesis-testing problem, and two hypotheses: a null hypothesis $H_{0}$ and an alternative hypothesis $H_{1}$ are posed to affirm different conditions of the system. The likelihood ratio is calculated to

support a reasonable decision if the system is undergoing a fault or not. Currently, hypothesis testing has been widely used in the fault diagnosis of various mechanical and control systems (Frosini, 2020; Lv et al., 2021; Schmid, Gebauer, Hanzl, \& Endisch, 2021), the sensor fault detection system for an unclear power plant, developed by the Argonne National Laboratory being one of the most famous applications. However, hypothesis testing procedure is carrying out with a potential purpose of rejecting the null hypothesis (normally asserts that the fault is present). Consequently, this approach tends to believe that the system is currently working at a healthy condition (Type I error), which may lead to the missed diagnosis for a fault. Limit checking detects an abnormality via comparing the system working parameters with the Upper Control Limit (UCL) or Lower Control Limit (LCL), or both. An alarm is reported if any parameter drifting exceeding its UCL or LCL. Limit checking ensures a rational decision be made in the process of fault detection, avoiding a false or miss warning. Nevertheless, the precondition for the well performance of limit checking is the large fluctuation of system working parameters. For an early fault, the system parameters may still fluctuate within normal limits, which makes this approach unsatisfied for early fault diagnosis.

In this paper, an integrated methodology for fault detection and isolation is proposed at a system level. A dynamical model of a


170 presents a methodology of mechanical system fault behaviour analysis based on TCG. Section 3 gives a sensor placement approach to describe the system behaviour using the least quantity of sensors. Section 4 provides an early fault detection method for the fault with weak signatures and the abnormal parameters are separated at the same time. The multiple abnormal parameters are fused using Bayesian network and real root cause of the current breakdown is located in Section 5. Finally, Section 6 summaries the paper.

# 2. Fault Behaviour Analysis Based on Temporal Causal Graph 

The causal relationship between systems faults and symptoms is the first step for the fault detection and isolation (Luo et al., 2021; Singh, Howard, Hansen, \& Kopke, 2018). In this section, a temporal causal graph-based approach is presented to analyse the response characteristics of observable parameters under different faults. An engine lubrication system is used to illustrate the approach.

### 2.1 System Modelling Using Bond Graph

Bond graph is a graphical and universal dynamics modelling method which describes dynamic behaviour in different domains (hydraulic, mechanics, electrics, etc.) via a unified approach (Kazemi, \& Montazeri, 2019). This method is developed based on the fact that the physical concepts of basic variables in different domains are analogous, e.g,

electric voltage and hydraulic pressure, electric current and volume flow rate, and so on. Consequently, Bond graph depicts the behaviour of a system involving different domains using just 4 generalised variables: effort $e(t)$, flow $f(t)$, momentum $p(t)$ and displacement $q(t)$. The components in various domain systems can be represented by 6 Bond graph elements. A power bond (drawn as a half arrow) is added if there exists an energy flow from one element to the other. Figure 1 shows these basic Bond graph elements. The physical concepts of the generalised variables in different energy domains and the instantiation of Bond graph elements are given in Appendix A.

$$
\begin{aligned}
& S_{e} \xrightarrow[\substack{\frac{e_{1}}{f_{1}} \\
S_{f} \\
\hdashline f_{2}}]{e_{1} \rightarrow} \\
& \frac{e_{3}}{f_{3}} \rightarrow R \\
& \frac{e_{4}}{f_{4}} \rightarrow C \\
& \frac{e_{5}}{f_{5}} \rightarrow I
\end{aligned}
$$

(a) Sources
(b) Passive elements
(c) Transformer
(d) Gyrator

$$
\begin{aligned}
& e_{11} \mid f_{11} \\
& \xrightarrow[\substack{e_{10} \\
f_{10}}]{e_{11}} 0 \xrightarrow[\substack{e_{12} \\
f_{12}}]{e_{12}} \quad \frac{e_{13}}{f_{13}} 1 \frac{e_{13}}{f_{13}}
\end{aligned}
$$

(e) 0-junction
(f) 1-junction

Figure 1. Basic elements of Bond graphs

Bond graph, i.e. pseudo Bond graph, is used to model the thermodynamic systems. Temperature $T$ and heat flow rate $\dot{E}$ are utilised as effort variable and flow variable respectively. The heat conduction, convection and radiation of the fluid with environment are described using one-port R-element, in which $R$ represents the thermal resistance in the thermal transmission. A two-port R-element is introduced to depict the energy change in a control volume with fluid flowing in and out, see Figure 2. According to thermodynamic theories, the energy flow from one control volume to another is not only the function of temperature $T$ and heat flow rate $\dot{E}$, but also the function of mass flow $\dot{m}$ (or volume flow $Q$ for an incompressible fluid). Thus, another port is introduced to the two-port R-element, and this additional port is connected with the hydraulic Bond graph model to capture the mass flow or volume flow of the fluid. The constitutive relation of the two-port R-element is shown as Eq. (1), where $\dot{E}_{\text {in }}, \dot{E}_{\text {out }}$ are the input and output heat flow rate respectively, $\rho$ denotes the density of the fluid, and $c$ represents the specific heat.

$$
\begin{aligned}
& \text { if } Q>0, \dot{E}_{\text {in }}=\dot{E}_{\text {out }}=\rho c Q T_{\text {in }} \\
& \text { if } Q<0, \dot{E}_{\text {in }}=\dot{E}_{\text {out }}=\rho c Q T_{\text {out }}
\end{aligned}
$$

Figure 2. The two-port R-element in pseudo Bond graph

The marine diesel engine lubrication system is taken as an example to illustrate the approach. This example will be used throughout the paper because it is critical systems for most of machines and operates based on the coherent links between different domains. A typical marine diesel engine lubrication system is shown in Figure 3. The working of engine lubrication system involves three common domains: mechanical, hydraulic and thermodynamic principles. This section aims to obtain the causal relationships of faults and parameters, therefore qualitative modelling method is applied here. The Bond graph of a marine engine lubrication system is constructed as Figure 4 (this can be done by the graphical user interface of the $20-\mathrm{sim}^{\mathrm{TM}}$ modelling and simulation software environment). Detailed modeling process can be found in Appendix B.
![img-0.jpeg](img-0.jpeg)

1-relief valve of gear pump, 2-gear pump, 3-oil cooler, 4- thermostatic valve, 5-oil filter, 6-bypass valve, 7-pressure regulating valve, 8 -supercharger, 9 -oil pressure gauge, 10-piston, 11-air valve, 12-rocker arm, 13-camshaft, 14-fuel injection pump, 15 -main oil gallery, 16 -crankshaft, 17 - oil sump

Figure 3. A marine diesel engine lubrication system

two-port R-element to assure a power consistent graph. Auxiliary node + is introduced to qualitatively represent the positive correlation of the two variables. Element $R_{\text {leak }}$ represents the leak oil through pipe. It can be viewed as an infinite quantity at healthy condition and a finite value if a leakage exists. The admissible causal patterns of the Bond graph elements are arranged using Sequential Causality Assignment Procedure (SCAP) (Mosterman, \& Biswas, 1999).
![img-1.jpeg](img-1.jpeg)

Figure 4. Bond graph of a marine engine lubrication system

### 2.2 Steady-State Fault Behaviour Analysis via Temporal Causal Graph

The steady-state fault behaviour can be obtained by deriving the

analytic equations according to the constitutive relations of bond elements. However, this work is thought time-consuming. Alternatively, one can analyse steady-state fault behaviour with the help of temporal causal graph.

Definition 2.1 A TCG is a 3-tuple $\langle V, L, D\rangle$, in which $V$ is a set of vertices, or called variables for an engineering system; $L=\{1,-1,=, \lambda, 1 / \lambda, \lambda \mathrm{d} t, 1 / \lambda \mathrm{d} t\}$ is the label set of the signal flow diagram which is used to represent the function relationships of the variables, where $1, \lambda$ and $1 / \lambda$ denotes the positive correlation with coefficient 1 , $\lambda$ and $1 / \lambda$ respectively, -1 depicts the negative correlation, $=$ represents the two variables are equal in number, $\lambda \mathrm{d} t$ and $1 / \lambda \mathrm{d} t$ represent the integral relationships; $D \subseteq V \times L \times V$ is the directed edges of the model.

The TCG describes the function relationships of the system variables using a directed graph. The TCG can be directly constructed from the Bond graph model detailed in (Mosterman, \& Biswas, 1999). Figure 5 shows the TCG model of engine lubrication system converted from the Bond graph. According to the analytic model-based fault diagnosis community, a failure can be manifested as the abnormal change of the system structure parameters or observable parameters (Travé-Massuyès, Escobet, \& Olive, 2006; Mosterman, \& Biswas, 1999). Therefore, the faults of a mechanical system can be introduced as the deviation of system variables. For the example above, in total 11 faults of marine

engine lubrication are studied in this paper. The corresponding system variables and the deviation form are presented in Table 1, in which symbols $T, \downarrow$ label the direction of the deviation; $R_{1} \rightarrow R_{2}$ implies an abrupt change from $R_{1}$ to $R_{2}$ when the fault occurs. For example, fault filter blocking is represented as the increases of the flow resistance $R_{\text {filter }} \uparrow$; pipe leakage is manifested as the abrupt change of the resistance from $+\infty$ (no crack exists) to a finite value $R$. The response characteristics of 8 observable parameters are analysed according to the TCG. These parameters can be directly detected via pressure or temperature transducers. Table 2 shows the parameters and the corresponding variables in TCG.

Table 1
Common faults of a marine engine lubrication system



Table 2
TCG of common faults of a marine engine lubrication system


Algorithm 1 shows the methodology of fault behaviour analysis.
The algorithm obtains the qualitative deviation for observable parameters according to the functional relationships represented by TCG. The fault propagation analysis starts from the zeroth order deviation for a variable, i.e. magnitude changes, and the order keeps unchanged if the effects of the two variables are instantaneous, i.e. labels $1,-1,=, \lambda$, and $1 / \lambda$. Specifier $\mathrm{d} t$ indicates an integrating relation, which implies that a node

affects the derivative of its successor node. The order increases when an integrating edge is traversed to represent the time delay for the effect. Loops (closed causal path) in the TCG indicate a natural negative feedback mechanism in the system. The effects of a fault on its successor node are fed back via the loop with a certain transfer function to subtract the deviation. A steady-state of the system is achieved due to the existence of the loops. By taking the propagation of filter blocking $f_{1}$ as an example, the increase of resistor $R_{\text {filter }}$ will decrease the oil flow through the filter, i.e. $Q_{24} \downarrow$. A propagation path $Q_{24} \downarrow \rightarrow Q_{23} \downarrow \rightarrow Q_{27} \downarrow$ is generated since they have a positive correlation or take on equal values. As for the algebraic loop $Q_{27} \rightarrow p_{27} \rightarrow p_{25} \rightarrow Q_{25} \rightarrow Q_{27}$, the effect of $Q_{27} \downarrow$ propagates along the temporal edge and leads to a first derivative change in $p_{27}\left(p_{27}^{\prime} \downarrow\right)$. The propagation continues to decrease the change rate of $Q_{25}\left(Q_{25}^{\prime} \downarrow\right)$. A negative correlation exists between $Q_{25}$ and $Q_{27}$. Thus, the deviation $Q_{25}^{\prime} \downarrow$ will increase the change rate of $Q_{27}$, i.e $Q_{27}^{\prime} \uparrow$, and a new balance is achieved. Figure 6 shows the forward propagation of filter blocking on all parameters. The response characteristics of observable parameters for the faults presented in Table 1 are shown in Table 3, in which +1 represents the occurrence of fault would increase the parameter, while -1 indicates the opposite change.

Algorithm 1: Analyse the behaviour for a fault in steady-state
Input: failure modes
Output: response characteristics of all variables
Steps:
manifest the fault as the deviation of system variables:
mark the of magnitude change of its successor node, and add the node to list $v_{\text {list }}$;
while $v_{\text {list }} \neq \varnothing$ do
$v_{\text {parent }} \leftarrow$ the last node in $v_{\text {list }}$
if the successor $v_{\text {child }}$ of $v_{\text {parent }}$ is not traversed then
if successor relation is equal or positive correlation then
$v_{\text {child }}$ has the same deviation with $v_{\text {parent }}$
else if successor relation is negative correlation then
$v_{\text {child }}$ has the opposite deviation with $v_{\text {parent }}$
else if successor relation includes a time integral effect then
increase $v_{\text {child }}$ derivative order and assign the same qualitative value
end if
end if
delete $v_{\text {parent }}$ from $v_{\text {list }}$
$v_{\text {list }} \leftarrow v_{\text {child }}$
end while

![img-2.jpeg](img-2.jpeg)

Figure 5. Temporal causal graph of an engine lubrication system

![img-3.jpeg](img-3.jpeg)

Figure 6. Failure behaviour analysis of filter blocking

Table 3
Response characteristics of observable parameters for different faults



Experiments were carried out based on an in-line 2 cylinders, water-cooled marine diesel engine, see Figure 7. Detailed specifications of the engine are shown in Table 4. Seven common faults are introduced to test rig. The experiments are carried out under four different load rates: $25 \%, 50 \%, 75 \%, 100 \%$, respectively at the speed of $2000 \mathrm{r} / \mathrm{min}$. Typical values of parameters at $75 \%$ load are presented in Table 5.

Table 4
Technical details of the Beta 14 marine diesel engine


![img-4.jpeg](img-4.jpeg)

Figure 7. Test rig of a Beta 14 marine engine power train

Table 5
Operating parameters of the Beta 14 engine lubrication system under healthy and various fault conditions


The actual response characteristics of the observable parameters when a fault presents can be obtained from the data in Table 5.

Comparing the Table 3 with Table 5 found that the deviations of parameters derived from the TCG are consistent with the ones presented from the experiment data. For example, the response of the parameters $\left\{s_{1}, \cdots, s_{8}\right\}$ for filter blocking $f_{1}$ can be listed as $[+1,+1,-1,-1,+1,+1,+1,+1]$, i.e. the lubrication oil pressures decrease at the measurement points $s_{3}$ and $s_{4}$, while the other parameter increase when the filter is blocked. From Table 5, it shows that the lubrication oil pressure after pump and the pressure before filter increase about 0.1 bar compared with healthy ones; while the pressure after filter and pressure before engine decrease about 0.5 bar when the filter is blocked. Meanwhile, the temperature at different position all increase compared with normal values. The abnormal changes from experiment data agree well with the predictions in Table 3, which shows the validity of TCG for fault behaviour analysis.

# 3. Optimal Sensor Placement Using Set Partitioning Theory 

The system behaviour can be effectively characterised using the observable parameters derived in Section 2. However, for a large-scale mechanical system, it is almost an infeasible work to monitor all observable parameters given the various limitations of installation space and cost. This section gives an optimal sensor placement approach to achieve a desired fault isolatability using the minimum quantity of

sensors. Comparison to a graphical approach is presented to illustrate the advantages.

# 3.1 Problem Formulation 

Key concepts are firstly overviewed to formulate this problem (Wang et al., 2020).

Definition 3.1 Let a complex mechanical system be a 2-tuple $\sum=\langle F, S\rangle$, in which $F=\left\{f_{1}, \cdots, f_{n}\right\}$ represents the set of interested faults and $S=\left\{s_{1}, \cdots, s_{k}\right\}$ denotes the set of observable parameters or said sensors (we do not differentiate observable parameters from sensors in this section). A fault signature matrix is defined as $\mathbf{M}(\Sigma)=\left(m_{i j}\right)_{n \times k}$, in which

$$
m_{i j}=\left\{\begin{array}{l}
1, \quad s_{j} \text { increases if } f_{i} \text { presents } \\
0, \quad s_{j}, f_{i} \text { have no causal relation } \\
-1, s_{j} \text { decreases if } f_{i} \text { presents }
\end{array}\right.
$$

According to the definition of fault signature matrix, any observable parameters with non-zero value in a row vector $\mathbf{r}_{i}$ of $\mathbf{M}(\Sigma)$ is enough to indicate the presence of fault $f_{i}$. Accordingly, the column vector $\mathbf{c}_{j}$ denotes the faults that can be detected using sensor $s_{j}$. Two faults $f_{a}$ and $f_{b}$ are distinguishable if there exist at least one observable parameter that shows different response characteristics for the two faults, i.e. $\mathbf{r}_{a} \neq \mathbf{r}_{b}$. It should be note that the isolatability of the concerned faults is essentially determined by the properties of the system. Some faults are inherently indistinguishable due to the similar failure mechanisms and

symptoms. Besides, some faults can be easily distinguished from each other by simple artificial observations, and an advanced, high-accuracy sensor network is not necessary isolation these faults. Therefore, the purpose of sensor placement is not to pursue the completely isolation of pairs of faults, but find a quantity-optimum set of sensors that has the same fault isolation ability with the complete set of potential sensors. Set partitioning theory is exploited for this purpose.

# 3.2 Selecting A Minimal Sensor Set for Fault Isolation 

The faults and potential sensors can be viewed as two sets. Specifically, the faults are thought as the decision attribute set, while the sensors are treat as conditional attribute set. The causal relationships between faults and parameters represent the mapping from a conditional attribute set to a decision attribute set. The problem of optimal sensor placement can be then viewed as partitioning the decision attribute set using the minimum set of conditional attributes.

As for a mechanical system $\sum=\langle F, S\rangle$ with fault signature matrix $\mathbf{M}(\Sigma)=\left(m_{i j}\right)_{n \times k}$, a discernibility matrix $\mathbf{D}(\Sigma)$ is defined as a $n \times n$ symmetric matrix. The discernibility matrix crosses fault modes in both rows and columns. The matrix element $\alpha_{i j}$ is defined as follows.

$$
\alpha_{i j}=\left\{s \mid s \in S \wedge s\left(f_{i}\right) \neq s\left(f_{j}\right)\right\}
$$

where $s\left(f_{i}\right)$ denotes the qualitative value of fault $f_{i}$ on $s$ according

to Eq. (2).
The matrix element $\alpha_{i j}$ represents the set of sensors that have different response characteristics for faults $f_{i}$ and $f_{j}$. Therefore, any sensor of matrix element $\alpha_{i j}$ is adequate to discern faults $f_{i}$ from $f_{j}$. Obviously, elements of the main leading diagonal are all empty sets since no sensors can distinguish a fault from itself. After generating the discernibility matrix of a mechanical system, the minimal sensor set to distinguished pairs of faults can be derived by combining the non-empty elements using Boolean logic, see Eq. (4). The procedure for design a quantity-optimal sensor network for fault isolation is presented as Algorithm 2. It should be note that an additional row vector $\mathbf{r}_{n+1}=\mathbf{0}_{1 \times k}$ is added to $\mathbf{M}(\Sigma)$. The purpose of this step is to ensure the observability of a fault, i.e. there is no zero vector in the fault signature matrix regarding $F$ and $S^{*}$.

$$
f(\Sigma)=\wedge\left\{\vee s \mid s \in \alpha_{i j}, \alpha_{i j} \neq \varnothing\right\}
$$

Algorithm 2: Design A Quantity-Optimal Sensor Network for FDI
Input: the set of all potential sensors $S$;
Output: all alternative optimal configurations of sensors for a desired FDI $S^{*}$; Steps:

Step 1 construct the fault signature matrix $\mathbf{M}(\Sigma)$ of the system according to the causal relationships between faults and symptoms;

Step 2 add $\mathbf{r}_{n+1}=\mathbf{0}_{1 \times k}$ as the additional row vector of $\mathbf{M}(\Sigma)$;
Step 3 calculate the discernibility matrix $\mathbf{D}(\Sigma)$ from $\mathbf{M}(\Sigma)$ according to Eq. (8);
Step 4 calculate the discernibility function $f(\Sigma)$ using Eq. (9);
Step 5 derive the minimal disjunctive normal form of $f(\Sigma)$;
Step 6 output each conjunctive form of $f(\Sigma)$ as the alternative configuration of sensors $\left(S^{*}\right)$ for FDI.

# 3.3 Illustration Example: Engine Lubrication System 

By revisiting the example of engine lubrication system aforementioned, Table 3 shows the causal relationships of faults and symptoms, which can be considered as the fault signature matrix $\mathbf{M}(\Sigma)$. The partition of $F=\left\{f_{1}, \cdots, f_{11}\right\}$ by the complete set of sensors $S=\left\{s_{1}, \cdots, s_{8}\right\}$ is written as

$$
F / S=\left\{\left\{f_{1}\right\},\left\{f_{2}, f_{4}, f_{8}\right\},\left\{f_{3}\right\},\left\{f_{5}\right\},\left\{f_{6}\right\},\left\{f_{7}\right\},\left\{f_{9}\right\},\left\{f_{10}\right\},\left\{f_{11}\right\}\right\}
$$

Faults pipe leakage $f_{2}$, lubrication oil shortage $f_{4}$, relief valve of pump leakage $f_{8}$ have similar failure behaviour, which cannot be isolated using the online condition monitoring system $S=\left\{s_{1}, \cdots, s_{8}\right\}$. In engineering practice, these three can be easily distinguished by simple artificial checking, e.g. pipe leakage can be easily identified by a quick visual inspection; lubrication oil shortage would reflect in the liquid level of dipstick; relief valve of pump leakage can be determined using exclusive method. The discernibility matrix $\mathbf{D}(\Sigma)$ of engine lubrication system is calculated as follows.

$$
\mathbf{D}(\Sigma)=\left[\begin{array}{ll}
\mathbf{D}_{11}(\Sigma) & \mathbf{D}_{12}(\Sigma) \\
\mathbf{D}_{21}(\Sigma) & \mathbf{D}_{22}(\Sigma)
\end{array}\right]
$$

where

462
$\mathbf{D}_{x 1}(\Sigma)=\left[\begin{array}{cccc}\phi & \left\{s_{1}, s_{2}\right\} & \left\{s_{2}, s_{3}, s_{6}, s_{7}, s_{8}\right\} & \left\{s_{1}, s_{2}\right\} & S & \left\{s_{1}, s_{3}, s_{4}\right\} \\ \phi & \left\{s_{1}, s_{5}, s_{6}, s_{7}, s_{8}\right\} & \phi & S \backslash\left\{s_{1}, s_{2}\right\} & \left\{s_{2}, s_{3}, s_{4}\right\} \\ & \phi & \left\{s_{1}, s_{5}, s_{6}, s_{7}, s_{8}\right\} & \left\{s_{1}, s_{3}, s_{4}\right\} & S \\ & \phi & S \backslash\left\{s_{1}, s_{2}\right\} & \left\{s_{2}, s_{3}, s_{4}\right\} \\ & & \phi & \left\{s_{2}, s_{5}, s_{6}, s_{7}, s_{8}\right\} \\ & & & \phi\end{array}\right]$

$$
\mathbf{D}_{12}(\Sigma)=\left[\begin{array}{cccc}
\left\{s_{2}\right\} & \left\{s_{1}, s_{2}\right\} & S \backslash\left\{s_{1}, s_{2}\right\} & \left\{s_{3}, s_{4}\right\} & S \backslash\left\{s_{3}, s_{4}\right\} & S \\
\left\{s_{1}\right\} & \phi & S & \left\{s_{1}, s_{2}, s_{3}, s_{4}\right\} & \left\{s_{5}, s_{6}, s_{7}, s_{8}\right\} & S \\
\left\{s_{5}, s_{6}, s_{7}, s_{8}\right\} & \left\{s_{1}, s_{5}, s_{6}, s_{7}, s_{8}\right\} & \left\{s_{2}, s_{3}, s_{4}\right\} & S \backslash\left\{s_{1}\right\} & \left\{s_{1}\right\} & S \\
\left\{s_{1}\right\} & \phi & S & \left\{s_{1}, s_{2}, s_{3}, s_{4}\right\} & \left\{s_{5}, s_{6}, s_{7}, s_{8}\right\} & S \\
S \backslash\left\{s_{2}\right\} & S \backslash\left\{s_{1}, s_{2}\right\} & \left\{s_{1}, s_{2}\right\} & S \backslash\left\{s_{3}, s_{4}\right\} & \left\{s_{3}, s_{4}\right\} & S \\
\left\{s_{1}, s_{2}, s_{3}, s_{4}\right\} & \left\{s_{2}, s_{3}, s_{4}\right\} & \left\{s_{1}, s_{5}, s_{6}, s_{7}, s_{8}\right\} & \left\{s_{1}\right\} & S \backslash\left\{s_{1}\right\} & S\end{array}\right]
$$

464
$\mathbf{D}_{21}(\Sigma)=[]_{6=6}$
465
$\mathbf{D}_{22}(\Sigma)=\left[\begin{array}{cccc}\phi & \left\{s_{1}\right\} & S \backslash\left\{s_{1}\right\} & \left\{s_{2}, s_{3}, s_{4}\right\} & \left\{s_{1}, s_{5}, s_{6}, s_{7}, s_{8}\right\} & S \\ \phi & S & \left\{s_{1}, s_{2}, s_{3}, s_{4}\right\} & \left\{s_{3}, s_{6}, s_{7}, s_{8}\right\} & S \\ & \phi & \left\{s_{5}, s_{6}, s_{7}, s_{8}\right\} & \left\{s_{1}, s_{2}, s_{3}, s_{4}\right\} & S \\ & & \phi & S & S \\ & & & \phi & S \\ & & & & \phi\end{array}\right]$

The discernibility function $f(\Sigma)$ can be derived from $\mathbf{D}(\Sigma)$ by combining the non-empty elements using Eq. (4). The minimal disjunctive normal form of $f(\Sigma)$ is shown below.

$$
f(\Sigma)=s_{1} s_{2} s_{3} s_{5}+s_{1} s_{2} s_{3} s_{6}+s_{1} s_{2} s_{3} s_{7}+s_{1} s_{2} s_{3} s_{8}+s_{1} s_{2} s_{4} s_{5}+s_{1} s_{2} s_{4} s_{6}+s_{1} s_{2} s_{4} s_{7}+s_{1} s_{2} s_{4} s_{8}
$$

Each conjunctive form in $f(\Sigma)$ is an alternative sensor placement plan for FDI. In total 8 possible sensor networks are given using the proposed approach.

$$
\begin{aligned}
& S_{1}^{*}=\left\{s_{1}, s_{2}, s_{3}, s_{5}\right\}, \quad S_{2}^{*}=\left\{s_{1}, s_{2}, s_{3}, s_{6}\right\}, \quad S_{3}^{*}=\left\{s_{1}, s_{2}, s_{3}, s_{7}\right\}, \quad S_{4}^{*}=\left\{s_{1}, s_{2}, s_{3}, s_{8}\right\} \\
& S_{5}^{*}=\left\{s_{1}, s_{2}, s_{4}, s_{5}\right\}, \quad S_{6}^{*}=\left\{s_{1}, s_{2}, s_{4}, s_{6}\right\}, \quad S_{7}^{*}=\left\{s_{1}, s_{2}, s_{4}, s_{7}\right\}, \quad S_{8}^{*}=\left\{s_{1}, s_{2}, s_{4}, s_{8}\right\}
\end{aligned}
$$

According to set partitioning theory, the partition of faults using the 8 derived sensor configuration solutions can be calculated as follows.

$$
F / S_{i}^{*}=\left\{\left\{f_{1}\right\},\left\{f_{2}, f_{4}, f_{8}\right\},\left\{f_{3}\right\},\left\{f_{5}\right\},\left\{f_{6}\right\},\left\{f_{7}\right\},\left\{f_{9}\right\},\left\{f_{10}\right\},\left\{f_{11}\right\}\right\}=F / S(i=1, \cdots, 8)
$$

It shows that the partition of faults remains unchanged using the optimal sensor networks, which means that any of derived sensor configuration solution has the same capability to classify pairs of faults as the complete sensor network. Compared with the original sensor placement plan, the quantity of sensors for the fault detection and isolation of engine lubrication system are reduced from 8 to 4 , which considerably decreases the complexity and cost for engine condition monitoring. Meanwhile, the reduced sensor installation helps to minimise the interfering of auxiliary equipment for the working performance of a mechanical system. Table 6 compares the sensor placement results using the proposed approach with a classical graphical method presented in (Raghuraj, Bhushan, \& Rengaswamy, 1999). Algorithm 2 derives all possible combinations of sensors for a desired performance of fault isolation, which provides various options to design a sensor network for fault isolation of an engine lubrication system.

Table 6
Comparisons of the proposed approach with a classical sensor placement approach.


$$
\begin{aligned}
& \left\{s_{1}, s_{2}, s_{3}, s_{5}\right\},\left\{s_{1}, s_{2}, s_{3}, s_{6}\right\} \\
& \left\{s_{1}, s_{2}, s_{3}, s_{7}\right\},\left\{s_{1}, s_{2}, s_{3}, s_{8}\right\} \\
& \left\{s_{1}, s_{2}, s_{4}, s_{5}\right\},\left\{s_{1}, s_{2}, s_{4}, s_{6}\right\} \\
& \left\{s_{1}, s_{2}, s_{4}, s_{7}\right\},\left\{s_{1}, s_{2}, s_{4}, s_{8}\right\}
\end{aligned}
$$

Indistinguishable faults $\left\{f_{2}, f_{4}, f_{8}\right\}$
$\left\{f_{2}, f_{4}, f_{8}\right\}$

# 4. Early Fault Detection and Abnormal Parameter Separation 

In this section, we propose a multivariate statistics-based approach for early fault detection with the sensor networks designed in Section 3. The abnormal parameters are also separated according to the contributions of the parameters for the deviated multivariate statistic.

### 4.1 Multivariate Statistics Indices for Early Fault Detection

As for a mechanical system with $k$ observable parameters, the measurements can be arranged as a data matrix:

$$
\mathbf{X}=[\mathbf{x}(1) \mathbf{x}(2) \cdots \mathbf{x}(m)]^{\mathrm{T}}
$$

where $\mathrm{x} \in \mathfrak{R}^{\mathrm{k}}$ is a column vector for a measurement, i.e. $\mathrm{x} \in \mathfrak{R}^{\mathrm{k}}$ and $m$ is the number of samples.

The covariance matrix of data set can be obtained by

$$
\mathbf{S}=\frac{1}{m} \mathbf{X}^{\mathrm{T}} \mathbf{X}
$$

To model this dataset $\mathbf{S}$ for better diagnostics, it then is decomposed according to PCA using Eq. (6).

$$
\mathbf{S}=\left[\begin{array}{ll}
\overline{\mathbf{p}} & \tilde{\mathbf{p}}
\end{array}\right]\left[\begin{array}{ll}
\overline{\mathbf{A}} & \mathbf{0} \\
\mathbf{0} & \tilde{\mathbf{A}}
\end{array}\right]\left[\begin{array}{ll}
\overline{\mathbf{p}} & \tilde{\mathbf{p}}
\end{array}\right]^{\mathrm{T}}
$$

where $\overline{\mathbf{p}} \in \mathfrak{R}^{k \times l}$ and $\tilde{\mathbf{p}} \in \mathfrak{R}^{k \times(k-l)}$ are the principal loadings and residual loadings; $\tilde{\mathbf{A}} \in \mathfrak{R}^{l \times l}$ and $\tilde{\mathbf{A}} \in \mathfrak{R}^{(k-l) \times(k-l)}$ represent the corresponding eigenvalues of $\mathbf{S}$ respectively; $l$ denotes the quantity of principal components (PCs).

Equation (6) shows the projection of the data matrix $\mathbf{X}$ to two orthogonal linear spaces. The linear spaces $S_{p}$ and $S_{r}$ spanned by $\overline{\mathbf{p}}$ and $\tilde{\mathbf{p}}$ are called principal component subspace (PCS) and residual subspace (RS) respectively. In the two linear spaces, two multivariate statistics, i.e. Hotelling's $T^{2}$ and $Q$, can be obtained to depict the variations of the measurable parameters, see Eqs. (7) and (8) (Zhang, Yu, \& Ye, 2021; Li, Ding, \& Tsung, 2021).

$$
\begin{aligned}
& T^{2}=\mathbf{x}^{\mathrm{T}} \overline{\mathbf{P}} \overline{\mathbf{A}}^{-1} \overline{\mathbf{P}}^{\mathrm{T}} \mathbf{x} \\
& Q=\mathbf{x}^{\mathrm{T}} \overline{\mathbf{P}} \overline{\mathbf{P}}^{\mathrm{T}} \mathbf{x}
\end{aligned}
$$

Most of the researchers assign Hotelling's $T^{2}$ and $Q$ residual control limits by assuming the operation parameters in a mechanical system based on the assumption of Gaussian distribution. Nevertheless, an operation parameter hardly follows such an ideal probability distribution model completely in practice because the measurement noise often varies with working conditions. In order to develop accurate control limits for fault detection, Adaptive Kernel Density Estimation (AKDE) (Abramson, 1982) is used to obtain the probability density function (PDF)

more accurately, allowing a more realistic limit to be estimated.
Let $\left\{x_{1}, x_{2}, \cdots, x_{t}\right\}$ be the samples of random variable $X$, the PDF of the random variable is firstly estimated using a fixed-width KDE, where $h$ denotes bandwidth of the KDE; $K(\cdot)$ represents the kernel probability density function.

$$
\hat{f}_{p}(x)=\frac{1}{t h_{0}} \sum_{i=1}^{t} K\left(\frac{x-x_{i}}{h_{0}}\right)
$$

In this paper, the Gaussian kernel function is used to estimate the PDF of Hotelling's $T^{2}$ and $Q$. The Gaussian kernel function is shown as Eq. (10).

$$
K(x)=\frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} x^{2}}
$$

The initial bandwidth $h_{0}$ is assigned using the rules-of-thumb (ROT).

$$
h_{0}=\left(\frac{4 \hat{\sigma}^{5}}{3 t}\right)^{1 / 5}
$$

where $\hat{\sigma}$ is the standard deviation of the samples, which can be calculated using Eq. (12).

$$
\hat{\sigma}=\frac{R}{1.34}
$$

In Eq. (12), $R$ denotes the interquartile range of the sample set, i.e. $R=X[0.75]-X[0.25]$.

The data set $\left\{x_{1}, x_{2}, \cdots, x_{t}\right\}$ may be a non-uniform sampling of the random variable $X$. Consequently, a fixed bandwidth $h_{0}$ has limited

ability to describe the local probability distribution characteristic of the random variable $X$ on every data points. The AKDE exploits local bandwidth factor $\tau_{i}$ to evaluate the estimation result of fixed-width KDE method.

$$
\tau_{i}=\left\{\left[\prod_{j=1}^{i} \hat{f}_{p}\left(x_{j}\right)\right]_{i}^{1} / \hat{f}_{p}\left(x_{i}\right)\right\}^{\rho}
$$

where $\rho$ represents the sensitivity factor of AKDE.
The bandwidths on every data points are then modified to $\tau_{i} h_{0}$, and a more accurate estimation of the PDF is obtained using Eq. (14).

$$
\hat{f}(x)=\frac{1}{t} \sum_{i=1}^{t} \frac{1}{\tau_{i} h_{0}} K\left(\frac{x-x_{i}}{\tau_{i} h_{0}}\right)
$$

The AKDE provides a variable bandwidth for different data points, thereby avoiding the over-smoothing and under-smoothing of the conventional fixed-width KDE. The control limit of $T^{2}$ and $Q$ can thus be calculated according to the estimated probability density function.

$$
P\left(x<x_{U C L}\right)=\int_{-\infty}^{x_{U C L}} \hat{f}(x) \mathrm{d} x=\alpha
$$

where $\alpha$ denotes the confidence coefficient for the detection.
The multivariate statistics $T^{2}$ and $Q$ depict the parameters correlation in principal component subspace and residual subspace, respectively. Any statistic exceeding its control limit implies the system degraded from the healthy condition. The decision rule can be written as

$$
\left(T^{2}>T_{U C L}^{2}\right) \vee\left(Q>Q_{U C L}\right)
$$

to implement fault or abnormality detection.

When a fault is reported, it is desired to know which parameter is deviated from the normal value for the purpose of fault isolation and localisation. To this end, the contribution analysis is needed to be implemented.

The multivariate statistics Hotelling's $T^{2}$ and $Q$ are defined as the products of the column vector of measurable parameters and transformational matrix. The statistics can be defined as a unified form

$$
\text { Index }=\mathbf{x}^{\mathrm{T}} \mathbf{M x}
$$

where Index represents the statistics $T^{2}$ or $Q ; \mathbf{M}$ denotes the transformational matrix, $\quad \mathbf{M}=\overline{\mathbf{P}} \overline{\mathbf{A}}^{-1} \overline{\mathbf{P}}^{\mathrm{T}} \quad$ for Hotelling's $\quad T^{2}$ and $\mathbf{M}=\overline{\mathbf{P}} \overline{\mathbf{P}}^{\mathrm{T}}$ as for $Q$ residuals.

Decomposing the indices according to matrices multiplication, the statistics can be further written as

$$
\text { Index }=\mathbf{x}^{\mathrm{T}} \mathbf{M} \mathbf{x}=\left\|\mathbf{M}^{\frac{1}{2}} \mathbf{x}\right\|^{2}=\sum_{i=1}^{k}\left(\xi_{i}^{\mathrm{T}} \mathbf{M}^{\frac{1}{2}} \mathbf{x}\right)^{2}=\sum_{i=1}^{k} c_{i}^{\text {Index }}
$$

In Eq. (18), the value of a multivariate statistic is viewed as the superposition of $k$ component $c_{i}^{\text {Index }}$. Each component $c_{i}^{\text {Index }}$ represents the contribution of $i^{\text {-th }}$ measurable parameter to the deviation of the statistic. The contribution can be deduced as a more computable form

$$
c_{i}^{J n d e x}=\left(\xi_{i}^{\mathrm{T}} \mathbf{M}^{\frac{1}{2}} \mathbf{x}\right)^{2}
$$

where $\xi_{i}$ is the $i$-th column of the identity matrix, i.e. $\xi_{i}=\left[\begin{array}{lll}0 & 0 \cdots 1 \cdots 0\end{array}\right]^{\mathrm{T}}$.

For Hotelling's $T^{2}$, the contribution of each observable parameter is calculated as

$$
c_{i}^{T^{2}}=\left[\xi_{i}^{\mathrm{T}}\left(\overline{\mathbf{P}} \overline{\mathbf{A}}^{-1} \overline{\mathbf{P}}^{\mathrm{T}}\right)^{\frac{1}{2}} \mathbf{x}\right]^{2}
$$

For statistic $Q$, Eq. (19) can be rewritten as

$$
c_{i}^{Q}=\left[\xi_{i}^{\mathrm{T}}\left(\overline{\mathbf{P}} \overline{\mathbf{P}}^{\mathrm{T}}\right)^{\frac{1}{2}} \mathbf{x}\right]^{2}
$$

# 4.3 Experimental Evaluation 

A high-power marine diesel engine test system is employed to verify the proposed approach. The test rig has an 8-cylinder, water-cooled, high-speed marine diesel engine (MTU8V396SE84) with 500 kW output power at the rated speed of $1800 \mathrm{r} / \mathrm{min}$. The schematic of the engine test rig is shown as Figure 8. One of the optimal sensor network obtained in Section 3, i.e. lubrication oil pressure after pump $s_{1}$, lubrication oil pressure before filter $s_{2}$, lubrication oil pressure before engine $s_{4}$, lubrication oil temperature after cooler $s_{6}$, is commonly used as the parameters to describe the working condition of the engine lubrication system which operates based on a cooperation of multiple physical processes.

617 valve leakage $f_{5}$ which are common in diesel engines were introduced
618 to the lubrication system with minor magnitude of defects that affect little
619 on engine performance during the short period of tests. The data were
620 recorded at $25 \%, 50 \%, 75 \%$ full load at the speed of $1800 \mathrm{r} / \mathrm{min}$ for
621 examining the performance of the proposed method.
![img-5.jpeg](img-5.jpeg)

Figure 8. Schematic of the MTU8V396SE84 marine diesel engine test rig

In order to illustrate the advantages of proposed approach for early fault detection, the monitoring charts of pipe leakage at $25 \%$ full load using Pauta criterion (Shen et al., 2017) is shown in Figure 9 for comparison. The red dash lines represent the UCLs and LCLs of the parameters; the blue sample points are the engine parameters with healthy working condition while the red sample points denote the parameter with engine faults.

![img-6.jpeg](img-6.jpeg)

Figure 9. Detecting pipe leakage of MTU8V396 engine lubrication system using Pauta criterion ( $25 \%$ full load, $1800 \mathrm{r} / \mathrm{min}$ )

It can be seen that quite a number of samples still fluctuate between the acceptable range (the area determined via UCL and LCL of Pauta criterion) when the engine initially suffers from a fault. Some samples exceed the control limits, but the deviation is slight so that these samples are often mistaken as sampling errors and therefore ignored in engineering practice. Fault detection rate (FDR) (Samuel, \& Cao, 2014) is defined to quantitatively describe the performance of the fault detection result, see Eq. (22), where $N$ represents the total quantity of data

samples, and $n_{c}$ denotes the number of fault samples correctly identified. The FDRs of the three faults at different engine working conditions are shown as column 3 of Table 7. It can be seen that the conventional method has an unsatisfactory performance on early fault detection.

$$
F D R=\frac{n_{c}}{N} \times 100 \%
$$

Table 7
The FDRs of the three engine faults using different fault detection method


Multivariate statistics-based approach proposed in this study is then applied to the datasets for fault detection. The data samples under healthy condition are firstly exploited as the training data to obtain the baseline vectors of PCS and the RS and to assign the control limits of Hotelling's $T^{2}$ and $Q$ using AKDE. The test data are then used to evaluate the performance of the multivariate statistics-based approach. The monitoring

![img-7.jpeg](img-7.jpeg)

Figure 10. Detecting pipe leakage of engine lubrication system using multivariate statistics-based approach ( $25 \%$ full load, $1800 \mathrm{r} / \mathrm{min}$ )

The multivariate statistics of normal data (samples 1-100) fluctuate within the control limits, which are represented using red dash lines. Once a fault is introduced (sample 101), the multivariate statistics increase remarkably, particularly most $T^{2}$ values exceed the threshold. A fault alarm is then reported according to the fault decision rule Eq. (16). Compared with Pauta criterion, the FDR of pipe leakage under $25 \%$ load of $1800 \mathrm{r} / \mathrm{min}$ increases to $91.50 \%$ from $73.00 \%$ after using the proposed approach. Table 7 column 4 also shows significant increases in the FDRs for filter blocking $f_{1}$, pipe leakage $f_{2}$, bypass valve leakage $f_{5}$ under different engine working conditions. This demonstrates the improved performance for early faults detection by using the multivariate method.

The abnormal parameters are then separated for fault isolation in

680 next step. Figure 11 shows the contributions of the 4 measurable 681 parameters for the Hotelling's $T^{2}$ statistic when fault pipe leakage $f_{2}$, 682 is presented. Comparatively, parameters $s_{2}$ and $s_{1}$ show obviously 683 higher contributes, which are 8.035 and 5.331 respectively. During the 684 experiment, the pipe leakage was simulated by installing a manually 685 operated valve on the filter seat and releasing the oil out from the pipe. 686 The sensors for lubrication oil pressure after pump $s_{1}$ and lubrication 687 oil pressure before filter $s_{2}$ are structurally closed to the filter seat, so 688 the fault pipe leakage has the most influence on $s_{1}$ and $s_{2}$. The 689 lubrication oil temperature after cooler $s_{6}$ has the least contribution 690 because the small leakage has little impact on the thermal balance of the 691 system. The contribution plot effectively pinpoints the abnormal 692 parameters and quantifies the deviation. A fault isolation module can then 693 be performed to further investigate the root causes.

![img-8.jpeg](img-8.jpeg)

Figure 11. Contributions of parameters for the Hotelling's $T^{2}$ (pipe leakage, $25 \%$ full load, $1800 \mathrm{r} / \mathrm{min})$

# 5. Fault Isolation by Fusing Multi-Information 

In the previous, section 2 obtains the response characteristics of observable parameters under different faults, and section 3 simplifies the observable parameters needed to be detected. In this section, the causal relationships between faults and detected parameters are used to construct Bayesian network model. Once an abnormality is reported (Section 4), the root cause is identified using Bayesian network by blending the separated abnormal parameters with fault diagnosis rules.

### 5.1 Bayesian Network-Based Fault Isolation Approach

A Bayesian network is a directed acyclic graph (DAG). The faults are represented as parent nodes and the children nodes are instantiated as

the parameters. A directed edge is added from parent node to child node if a fault is perceived to be a cause of the abnormality. The causal relationship is quantified via conditional probability, which can effectively represent the uncertainties of the causality between faults and symptoms.

A Bayesian network with noisy-OR/MAX semantics is shown as Figure 12. Let $f_{1}, f_{2}, \cdots, f_{n}$ be the direct cause of an abnormality, $P_{i, a}^{b_{i}}$ be the probability that a mode of a fault $f_{i}$ is sufficient to cause a certain state of abnormality, i.e.
![img-9.jpeg](img-9.jpeg)

Figure 12. A Bayesian network with noisy-OR/MAX semantics

$$
\begin{array}{ll}
P_{i, a}^{b_{i}}=P\left(s=a \mid f_{i}=b_{i}, f_{j}=0_{\left[\forall j, j \neq i\right]}\right) & i=1 ; \cdots n \\
& a=0 ; \cdots d_{s}-1 \\
& b_{i}=1 ; \cdots d_{f_{i}}-1
\end{array}
$$

where $b_{i}$ is the current mode of fault $f_{i}$, i.e. $f_{i}=b_{i} ; a$ denotes the state of parameter $s$, i.e. $s=a ; d_{s}$ and $d_{f_{i}}$ depict the domain sizes of the parameter $s$ and the fault $f_{i}$, respectively; the finite integer sets

$727\left\{0,1, \cdots, d_{s}-1\right\}$ and $\left\{0,1, \cdots, d_{f_{i}}-1\right\}$ represent the domains of the parameter $s$ and the fault $f_{i}$.

The combined effect of multiple faults on the parameter $s$ can be generated according to the arithmetic relationship noisy-MAX.

$$
P(s=a \mid p a(s))=\left\{\begin{array}{lr}
P(s \leq 0 \mid p a(s)) & \text { if } a=0 \\
P(s \leq a \mid p a(s))-P(s \leq a-1 \mid p a(s)) & \text { if } a>0
\end{array}\right.
$$

where $p a(s)$ represents the parent nodes of parameter $s$; and $P(s \leq a \mid p a(s))$ can be calculated by

$$
P(s \leq a \mid p a(s))=\prod_{\substack{i=1 \\ b_{i} \neq 0}}^{n} \sum_{a^{\prime}=0}^{n} P_{i, a^{\prime}}^{b_{i}}
$$

In fault diagnosis, the faults and symptoms usually have Boolean-valued domains, i.e. present (denoted as T) or absent (denoted as F). In this cases, Eq. (25) can be converted into

$$
\left\{\begin{array}{l}
P(s=\mathrm{F} \mid p a(s))=\prod_{i: f_{i} \in p a(s)^{+}}\left(1-P_{i}\right) \\
P(s=\mathrm{T} \mid p a(s))=1-\prod_{i: f_{i} \in p a(s)^{+}}\left(1-P_{i}\right)
\end{array}\right.
$$

in which $p a(s)^{+}$denotes the present faults; $P_{i}$ represents the probability that a symptom is caused by the fault $f_{i}$ while other faults are absent, i.e.

$$
P_{i}=P\left(s=\mathrm{T} \mid f_{i}=\mathrm{T}, f_{j}=\mathrm{F}_{\left[\forall j, j \neq i\right]}\right)
$$

In addition to depicting the fault diagnosis rules qualitatively and quantitatively, a Bayesian network is used to characterise the occurrence

frequency of all system faults, which takes into account prior probabilities and provides more realistic guidance to investigate the root cause for the current breakdown. In practice, the prior probabilities of faults are usually assigned via expert's knowledge or experiences due to the limited quantity of statistical data. To control the bias of expert opinions and improve the accuracy of the diagnosis, an auxiliary node expert is introduced to fuse the various opinions on the proneness of a fault. The modified Bayesian network is shown in Figure 13. The auxiliary node expert assigns a state to each of experts who are invited to give their opinions to the prior occurrence probabilities of the faults to be examined based on their own knowledge. The belief $P_{i}$ of the state $\exp i$ represents the reliability of the $i^{\text {-th }}$ expert. Prior probability $P r_{i}=P(f=\mathrm{T} \mid \exp i)$ denotes the evaluation of the $i^{\text {-th }}$ expert on the occurrence probability of the modelled fault. The directed edges from expert to the fault nodes represent the analytic relationships in BN syntax. Therefore, the prior occurrence probability of a modelled fault is the weighted average of different experts' opinions.

![img-10.jpeg](img-10.jpeg)

Figure 13. Modified Bayesian network for prior probability assignment

The prior probability is updated given some new observations to show the likelihood that a fault is responsible for the presented abnormity. The fault reasoning is carried out based on Bayes theorem. Details can be seen in (Cai et al., 2021).

# 5.2 Experimental Evaluation 

The topological structure of the Bayesian network model for the engine lubrication system is shown in Figure 14. The directed edges are assigned according to the fault behaviour analysis results achieved in Section 2. An optimal sensor placement solution $\left\{s_{1}, s_{2}, s_{4}, s_{6}\right\}$ derived in Section 3 is used as the child nodes to describe the system behaviour. Two experts are invited to assign the quantitative parameters of the Bayesian network model. The reliabilities of experts are set as 0.6 and 0.4 respectively according to their experiences working in the field. An abnormality has a certain probability to present due to the influence of

measurement error and some unknown faults even though all modelled faults are absent. Accordingly, a base rate probability $P(s \mid$ Leak $)=0.05$ is introduced in this model to describe the influence from the possible causes missed. The probabilities of the model are configured as Table 8. Due to space limitation, only the probabilities regarding with $s_{1}$ and $s_{2}$ are presented here.
![img-11.jpeg](img-11.jpeg)

Figure 14. Bayesian network model of engine lubrication system

Table 8
Prior and conditional probabilities of the Bayesian network model



In Section 4, the abnormal parameters are separated according to the contributions to the multivariate statistics. The abnormalities are then input into the Bayesian network model as the evidence to locate the root cause. One of the graph theory-based inference algorithms: junction tree propagation algorithm is used for fault reasoning. The inference is realised by taking the advantage of GeNIe software. Table 9 presents diagnostic results using Bayesian network model.

Table 9
Diagnostic results using Bayesian network



The pipe leakage $f_{2}$ has the maximum posterior occurrence probability according to the Bayesian network model, which is $45.80 \%$. Therefore, pipe leakage $f_{2}$ is identified as the root cause for the abnormality. The fault lubrication oil shortage $f_{4}$ and relief valve of pump leakage $f_{8}$ also have high occurrence probabilities, which are $41.33 \%$ and $29.20 \%$ respectively. This is because fault $f_{2}, f_{4}$ and $f_{8}$ share the same symptoms according to the fault behaviour analysis in Section 2. In fact, these three faults can be easily distinguished from each other via a further checking in practice. The diagnostic result is consistent well with the experiment, which shows the Bayesian network-based approach can effectively fuse information from multiple sensors to localise the fault.

# 6. Conclusions 

In this paper, an integrated methodology for system-level fault

diagnosis is proposed based on fault behaviour analysis and optimal sensor placement, to achieve early fault detection and fault isolation, which provides a feasible technical route to design the fault diagnosis system for a complex mechanical system. The fault behaviour analysis outputs the causality of faults and parameters, which is the essential information for fault detection and isolation; an optimal sensor placement method is then presented to design a condition monitoring system for a complete description of system conditions with minimum quantity of sensors; the observed parameters are then analysed via a multivariate statistics-based approach to detect an abnormality at the early stage, and the abnormal parameters is separated at the same time; the abnormal parameters are finally input to a Bayesian network model, and the root cause is determined by fusing the observations with diagnostic rules. This approach is realised based on an engine lubrication system. The successful diagnosis achieved has demonstrated superior performance of the approach and provided an effective approach to the diagnostics of complex mechanical systems that operates based on interactions between multiple physical domains.

# Acknowledgements 

This work was supported by the Fundamental Research Funds for the Central Universities (Grant No: 2021QN1089).

# Appendix A. Bond Graph for Dynamics Modelling 

In Bond graph modeling, the physical concepts of the generalised variables in different energy domains are unified according to Table A.1.

Table A.1.
Generalised variables in different domains


The instantiation of the basic bond graph elements are presented as follows.
$s_{e}, s_{f}$ sources, indicating the energy sources and the interaction with environment, e.g. voltage source, hydraulic pump.
$R$ resistors, representing energy dissipation units, e.g. electric resistor, fluidic resistor.
$C, l$ storing free energy by accumulating the net flow $f$ (for $C$ ) or net effort $e$ (for $l$ ), e.g. electric capacitor, spring (for $C$ ) and


$$
\left\{\begin{array}{l}
e_{10}=e_{11}=e_{12} \\
f_{10}-f_{11}-f_{12}=0
\end{array}\right.
$$

$$
\left\{\begin{array}{l}
e_{13}-e_{14}-e_{15}=0 \\
f_{13}=f_{14}=f_{12}
\end{array}\right.
$$

# Appendix B. The Modelling Method of Engine Lubrication System 

The mechanism of engine lubrication system refers to the transmission mechanism from engine crankshaft to oil pump. The crankshaft provides free energy for the whole system, which is denoted via a flow source $S_{f}$. Oil pump is connected with the crankshaft through a gear set or a belt, and the energy transfer process can be modelled by a transformer TF in which parameter $i$ represents the transmission ratio of gear set/belt. A part of energy would be dissipated in the process due to the friction and sliding etc. A dissipation element $R_{\text {effic }}$ is used to depict this energy loss. The rotating oil pump stores some free energy as mass moment of inertia. This physical behaviour is described using an I-element, i.e. $I_{\text {pump }}$ in Bond graph semantic, and connected with $R_{\text {effic }}$ via a 1-junction since they share the same angular speed.

For the hydraulic domain, the oil is expelled out by the rotating oil pump and the angular moment of oil pump is converted into hydraulic pressure in this process. The energy conversion is described by a transformer TF with transformer ratio $1 / k$, in which parameter $k$ denotes the pump delivery capacity per radian. A part of oil will leak back

to the oil sump due to the existence of end clearance, back lash and backlash in circular tooth. The resistor of oil leakage is modelled by a resistor $R_{\text {pleak }} . C_{\text {pcavity }}$ is used to model the internal chamber of the pump. From the oil pump, the lubricating oil flow through cooler and filter before entering the main oil gallery. The physical effects of cooler and filter mainly includes two parts: fluidic resistor and capacitor (the lubricating oil works at a low pressure so the liquid inductance can be ignored). The effects are modelled by C-element ( $C_{\text {cooler }}$ and $C_{\text {filter }}$ ) and R-element ( $R_{\text {cooler }}$ and $R_{\text {filter }}$ ) respectively. Besides the oil cooler and filter, a variety of valves is also configured on the system with different function. The resistor of the valve is modelled through an R-element in Bond graph, e.g. $R_{\text {preliej }}, R_{\text {thermo }}, R_{\text {bypass }}$ and $R_{\text {mreliej }}$. Resistor $R_{\text {block }}$ represents the fluidic resistor of the engine body.

For the thermodynamic domain, the working engine consistently generates heat owing to fuel combustion. The heat production is constant when the engine working at a stable condition. Thus, the combustion chamber is viewed as a constant heat source and represented using a flow source $S_{f}$. The heat production can be also a time-dependent quantity if the engine works at a time-varying condition (fuel-injection quantity changes with time). In this case, a sub-model should be added in the Bond graph model to describe the detailed analytic relationship between heat production (flow source $S_{f}$ ) and fuel-injection quantity for accurate

modelling of oil thermodynamic behavior. The main thermal storage elements include the main oil gallery, oil cooler, oil filter, and the oil sump. Heat transfers to these components when the oil flows through. The stored heat can be modelled as a capacitor, i.e. $C_{\text {Tgallery }}, C_{\text {Tsump }}$, $C_{\text {Tcooler }}$, and $C_{\text {Tfilter }}$. Besides the storage effect, the heat will also dissipate to the ambient air through oil sump. According to thermodynamic theories, thermal resistance in this heat convection can be modelled as $R_{\text {Tsump }}$. The environment temperature $T_{\text {atm }}$ can be viewed as a constant value and an effort source $S_{e}$ is used to model the physical effect. Oil cooler is another heat dissipation link of the lubrication system. Since the heat transfer is proportional to the temperature difference of the coolant and oil, and inversely proportional to the heat transfer resistance $R_{\text {conv }}$, a modulated flow source $M S_{f}$ is utilised here to model the heat transferring. The inversely proportional is captured via an auxiliary node inv.
