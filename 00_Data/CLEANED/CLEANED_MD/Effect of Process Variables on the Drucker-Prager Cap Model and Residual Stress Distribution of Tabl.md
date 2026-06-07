# Effect of Process Variables on the Drucker-Prager Cap Model and Residual Stress Distribution of Tablets Estimated by the Finite Element Method 

Yoshihiro Hayashi, ${ }^{a}$ Saori Otoguro, ${ }^{a}$ Takahiro Miura, ${ }^{b}$ Yoshinori Onuki, ${ }^{a}$ Yasuko Obata, ${ }^{a}$ and Kozo Takayama*<br>${ }^{a}$ Department of Pharmaceutics, Hoshi University; 2-4-41 Ebara, Shinagawa-ku, Tokyo 142-8501, Japan: and ${ }^{b}$ Mechanical CAE Division, Cybernet Systems Co., Ltd.; Fujisofi Bldg.3, Kanda-neribeicho, Chiyoda-ku, Tokyo 101-0022, Japan. Received February 27, 2014; accepted July 31, 2014; advance publication released online August 9, 2014


#### Abstract

A multivariate statistical technique was applied to clarify the causal correlation between variables in the manufacturing process and the residual stress distribution of tablets. Theophylline tablets were prepared according to a Box-Behnken design using the wet granulation method. Water amounts $\left(X_{1}\right)$, kneading time $\left(X_{2}\right)$, lubricant-mixing time $\left(X_{3}\right)$, and compression force $\left(X_{4}\right)$ were selected as design variables. The DruckerPrager cap (DPC) model was selected as the method for modeling the mechanical behavior of pharmaceutical powders. Simulation parameters, such as Young's modulus, Poisson rate, internal friction angle, plastic deformation parameters, and initial density of the powder, were measured. Multiple regression analysis demonstrated that the simulation parameters were significantly affected by process variables. The constructed DPC models were fed into the analysis using the finite element method (FEM), and the mechanical behavior of pharmaceutical powders during the tableting process was analyzed using the FEM. The results of this analysis revealed that the residual stress distribution of tablets increased with increasing $X_{4}$. Moreover, an interaction between $X_{2}$ and $X_{3}$ also had an effect on shear and the $x$-axial residual stress of tablets. Bayesian network analysis revealed causal relationships between the process variables, simulation parameters, residual stress distribution, and pharmaceutical responses of tablets. These results demonstrated the potential of the FEM as a tool to help improve our understanding of the residual stress of tablets and to optimize process variables, which not only affect tablet characteristics, but also are risks of causing tableting problems.


Key words tablet; simulation; mathematical model; residual stress; processing; Bayesian network

Various stresses, such as shear and axial stress, remain in tablets after the tableting process, because of the induction of elastic recovery. This type of stress, which is termed the residual stress distribution of the tablet, affects tablet characteristics and causes tableting problems. For instance, tablet failure, in particular capping, is more likely to be associated with an intensive shear band formed during the decompression stage. ${ }^{1,2)}$ Therefore, controlling the residual stress distribution of tablets is crucial in pharmaceutical design.

However, it is difficult to measure the residual stress distribution of tablets using analytical instruments. For this reason, the finite element method (FEM), in which the powder is modeled using the Drucker-Prager cap (DPC) model, is used to estimate the residual stress distribution of tablets. ${ }^{3,4)}$ The FEM is a numerical analytical method that is well established for the modeling of the deformation of powders in various industries, such as compaction in ceramic industries, and for the analysis of pharmaceutical-powder compaction. ${ }^{3,6)}$ In the FEM, powders are modeled as continuum media and the compaction behavior is analyzed by solving boundary value problems.

The DPC model is one of the continuum mechanical models, in which the powder is considered as a porous medium. The DPC model can represent the densification and hardening of the powder, as well as the interparticle friction. ${ }^{7,8)}$ This model can also reasonably represent both the shear failure and the plastic yielding of the powder, and can be readily characterized via experiments on real powders. Therefore, the DPC

[^0]model is used frequently to analyze the strain, relative-density changes, and stress distribution of tablets during the tableting process. Finally, the DPC model is characterized by parameters that are mainly related to the internal friction angle, elastic modules, and plastic deformation, among others.

In general, the full calibration of the DPC model requires triaxial, hydrostatic compression, and proportional loading tests. These tests are used commonly for metallurgical powders. ${ }^{9,10)}$ Because pharmaceutical powders are very soft and loosely packed, the application of triaxial cells in pharmaceutical materials is difficult. To solve this problem, a novel method adapted for pharmaceutical powders was proposed. ${ }^{1)}$ In this method, DPC model parameters are obtained by measuring axial upper/lower punch forces and displacements, as well as the radial die-wall pressure, during the tableting process.

Several studies have reported the calculation of the residual stress distribution of tablets using the FEM, in which the powder is modeled using the DPC model. ${ }^{11-13)}$ For instance, Kadiri and Michrafy reported that the stress distribution of tablets was affected by punch geometry. ${ }^{14)}$ It has been shown that the density distribution patterns are comparable with the experimental results of others. ${ }^{15-18)}$ Conversely, improvement of the DPC model was also studied. ${ }^{19)}$ In those studies, the DPC model parameters were considered as a function of the relative density of powders.

We have demonstrated that the residual stress distribution of tablets was affected by formulation and was closely related to the characteristics of the tablets, such as tensile strength and disintegration time. ${ }^{20)}$ However, a few issues remained unclear. The first was that a placebo powder and one other type


[^0]:    The authors declare no conflict of interest.

of powder (such as microcrystal cellulose or lactose) were used to model formulation in many studies, ${ }^{1,5,10)}$ even though the actual pharmaceutical products included one or more active pharmaceutical ingredients and many different excipients. Second, the effect of variables of the manufacturing process on DPC model parameters and residual stress distribution remains obscure, although the impact of the compression force has been well reported. Finally, the relationships between the DPC model parameters and pharmaceutical responses have not been elucidated. As the DPC model parameters express the physical characteristics of tablets, pharmaceutical characteristics, such as disintegration time, and dissolution property, may be predicted based on those parameters.

Therefore, the purpose of this paper was to investigate the problems described above. To achieve this purpose, we prepared 27 types of theophylline tablets according to the experimental design and measured the DPC model parameters of each tablet. Subsequently, we estimated the residual stress distribution of tablets using FEM and measured pharmaceutical characteristics of the tablets. Finally, we analyzed the data obtained using statistical methods such as multiple linear regression analysis (MRA) and Bayesian network (BN) analysis, to clarify the relationships between the process variables, DPC model parameters, residual stress distribution, and pharmaceutical characteristics of the tablets.

## Experimental

Materials Theophylline (JP grade) was purchased from Hachidai Pharmaceutical Co., Ltd. (Osaka, Japan). Lactose (LAC; Tablettose 80, Meggle Japan Co., Ltd., Tokyo, Japan), cornstarch (CS; Graflow M, Nippon Starch Chemical Co., Ltd., Osaka, Japan), and microcrystalline cellulose (MCC; Ceolus PH-101, Asahi Kasei Chemicals Co., Ltd., Tokyo, Japan) were purchased. Magnesium stearate (Mg-St) was purchased from Wako Pure Chemical Industries, Ltd. (Osaka, Japan). Polyvinylpyrrolidone K30 (PVP; Kollidon K30, BASF, Ludwigshafen, Germany) was a gift from the Nippon Shokubai Company, Ltd. (Osaka, Japan).

Experimental Design To develop systematic model formulations, 27 types of tablets containing theophylline, LAC, CS, MCC, PVP, and Mg-St were prepared according to a Box-Behnken design (Table 1). Water amount $\left(X_{1}\right)$, kneading
time $\left(X_{2}\right)$, lubricant-mixing time $\left(X_{3}\right)$, and compression force $\left(X_{4}\right)$ were selected as the process variables. Process conditions were fixed according to the flow chart presented in Table 2. All ingredients were dried at $75^{\circ} \mathrm{C}$ for 12 h . The ingredients were accurately weighed according to the experimental formulations, and all ingredients, with the exception of Mg-St, were blended using a mixer (KM4005; De'Longhi, Treviso, Italy) for 1 min . Distilled water was added as a granulation liquid and the mixture was kneaded (impeller speed, 470 rpm ; processing time, $1-9 \mathrm{~min}$ ). After the granulation process, the

Table 1. Box-Behnken Design of the Four Process Variables


Table 2. Flow Chart of the Granulation Process, Simulation Parameters ( $\alpha^{x}, E, v, W_{1}^{i}, D_{1}^{i}, D_{2}^{i}$, and $D_{1}$ ), Process Variables ( $X_{1}, X_{2}, X_{3}$, and $X_{4}$ ), and Pharmaceutical Responses (TS, DT, and $\mathrm{D}_{10}$ )


[^0]
[^0]:    The simulation parameters were measured via direct shear test and analysis of compaction behavior.

![img-0.jpeg](img-0.jpeg)

Fig. 1. A Typical Finite Element Model for Modeling the Compaction of Flat-Faced Tablets
The powder was modeled using the DPC model. An axisymmetric two-dimensional model (right half) was used.
granules were sieved through a 5.8 mm mesh. The granules were dried at $75^{\circ} \mathrm{C}$ for 50 min and forcibly sieved through a 1.4 mm mesh. Mg-St was added to the granules and the mixture was blended using a V blender (S-3; Tsutsui Rikagaku Kikai, Tokyo, Japan) for 5-55 min at 50 rpm . The final blended product was compressed into flat-faced tablets ( $200 \mathrm{mg}, 8 \mathrm{~mm}$ in diameter) using a tableting machine (AUTOTAB-500; Ichi-hashi-Seiki Company, Ltd., Kyoto, Japan). All the formulations were composed of 40 mg of theophylline, 86 mg of LAC, 37 mg of $\mathrm{CS}, 31 \mathrm{mg}$ of MCC, 4 mg of PVP, and 2 mg of Mg-St.

Simulated Conditions of the Tableting Process Using FEM Because the compaction of cylindrical tablets is carried out in an axisymmetric case, it can be analyzed using a two-dimensional FEM. Figure 1 shows the scheme of the FEM. The powder was considered as a DPC model. The die wall and upper punches were modeled as rigid bodies. The interaction between the powder, die wall, and upper punch was modeled, and the friction in the contacts was set to 0.1 . The nodes on the symmetry axis were restricted to move only horizontally, and the nodes at the bottom boundaries were allowed to move only vertically. The upper punch could move vertically with compression.

DPC Model The DPC model is one of the yield surface models and can represent the plastic deformation, elastic deformation, and internal friction of powders. The constitutive equations of the model are not listed here, as they can be found in a previous paper. ${ }^{20)}$ The DPC model parameters that have to be measured from the experiments are mainly Young's modulus $(E)$, Poisson rate $(v)$, internal friction angle $\left(\alpha^{s}\right)$, and three plastic deformation parameters $\left(W_{1}^{s}, D_{1}^{e}\right.$, and $\left.D_{2}^{s}\right)$. The methods for measuring each parameter are described in the following sections.

Measurement of the Failure Envelope Using the Direct Shear Test A direct shear tester (NS-V100; Nanoseeds Corporation, Gifu, Japan) was used to measure the failure envelope and estimate the internal friction angle $\left(\alpha^{s}\right)$. Before measurement, all ingredients were dried at $75^{\circ} \mathrm{C}$ for 12 h . The powder $(2.5 \mathrm{~g})$ was added into the shear cell. Shear stresses were then measured when the powder bed was compressed at 20,40 , and 60 N , respectively. The data observed were plotted in the axial shear ( $\sigma$ )-stress ( $\tau$ ) plane. The linear approximation method was used to estimate the failure envelope. The failure envelope was measured for three powders of each formulation. The details of the failure envelope are given in a
previous paper. ${ }^{20)}$

## Measurement of Elastic Modules, Plastic Deformation

Parameters, and Initial Density Using Analysis of Compaction Behavior Elastic modules (Young's modulus (E) and Poisson rate ( $v$ )) and plastic deformation parameters ( $W_{1}^{e}$, $D_{1}^{e}$, and $D_{2}^{e}$ ) were estimated based on references. ${ }^{1,20)}$ Powder compaction tests were conducted using an instrumented hydraulic press (TK-TB20KN; TOKUSHU KEISOKU Co., Ltd., Kanagawa, Japan). The axial upper/lower punch forces and displacements, and the radial die-wall pressure were measured during compaction. To obtain accurate measurements of the parameters, compression and decompression speeds were set at a relatively low speed (compression speed, $1 \mathrm{~mm} / \mathrm{s}$; decompression speed, $1 \mathrm{~mm} / \mathrm{s}$ ) and a large amount of sample powder was used (approximately 350 mg ). The relative packing density at 2 MPa was measured based on the volume of the gap between the upper and lower punches. Moreover, the initial density $\left(D_{i}\right)$ of the powder bed was calculated from this result. The $E, v$, and $D_{i}$ values were obtained from an average of three tablets, respectively.

A statistical method was applied to estimate the three DPC model parameters $\left(W_{1}^{e}, D_{1}^{e}\right.$, and $\left.D_{2}^{e}\right)$ using volume change as an indicator. The $W_{1}^{e}, D_{1}^{e}$, and $D_{2}^{e}$ were assigned to a Box-Behnken design, and 13 kinds of DPC models were constructed. The range of these parameters was determined using a preliminary test. The $\alpha^{s}$ value was obtained from the direct shear test measurements. $R_{i}^{s}=0.6, R_{i}^{e}=10, X_{i}=10, \sigma_{i}=0.91$, and $\varphi=1$ were set as arbitrary values that do not cause divergence problems in FEM analysis. The tableting process was simulated using the FEM and the thickness of tablets during compaction was measured at $1,2,3,4,5,6,7,8,9$, and 10 kN . The data observed were modeled by RSM-S, and DPC model parameters that were correlated with the experiment were estimated.

Evaluation of the Pharmaceutical Responses of Tablets The hardness of the tablets was determined using a tablethardness tester (Portable checker PC-30; Okada Seiko, Tokyo, Japan). TS was calculated as:

$$
\mathrm{TS}=\frac{2 F}{\pi d t}
$$

where $F$ is the maximal diametrical crushing force and $d$ and $t$ are the diameter and thickness of the tablet, respectively. TS values were measured for three tablets of each formulation.

The disintegration test was performed according to the JP16 disintegration test for tablets using a disintegration tester (NT20H; Toyama Sangyo Co., Ltd., Osaka, Japan) and water (as a test medium) at $37^{\circ} \mathrm{C}$. The DT was defined as the interval that was required for the complete disappearance of a tablet or its particles from the tester net. The DT was measured for three tablets of each formulation.

The dissolution test was performed according to the JP16 dissolution test No. 2 (the paddle method) at 50 rpm (NTR6100A; Toyama Sangyo Co., Ltd.). The dissolution medium used was 900 mL of distilled water at $37 \pm 0.5^{\circ} \mathrm{C}$. The samples were collected and filtered after $1,4,10,20,30,45$, and 60 min . The concentration of theophylline was measured spectrophotometrically at 271 nm using a Jasco Ubest-30 spectrophotometer (Japan Spectroscopic Co., Ltd., Tokyo, Japan). The dissolution rates of three tablets of each formulation were measured.

Evaluation of the Homogeneity of Residual Stress Distri-

bution The standard deviation (S.D.) was used as an indicator of homogeneity. S.D. is defined as:

$$
\text { S.D. }=\sqrt{\frac{\sum_{i=1}^{n}\left(\bar{x}-x_{i}\right)^{2}}{n-1}}
$$

where $\bar{x}, x_{i}$, and $n$ indicate the average of the stress distribution of each formulation, each stress point obtained by FEM, and the number of stress points obtained by FEM, respectively. Because $n$ was determined by the number of meshes used in the FEM, $n=333$ was used in this study.

Modeling of the Causal Relationships between Factors To evaluate the causal relationships between factors, we applied a nonlinear response surface method that incorporated a thin plate spline interpolation (RSM-S), which has been used to determine acceptable formulations of pharmaceutical compounds. Using RSM-S, we can easily understand the nonlinear relationships between causal factors and response variables and estimate a robust optimal solution. ${ }^{21)}$

MRA was performed to clarify the impact of process variables on the simulation parameters or residual stress distribution of tablets. A forward selection method based on stepwise selection was applied to the selection of causal factors, and factors with $p$ values $>0.25$ were successively excluded from the analysis. In general, $p>0.25$ is used as a judging standard for excluding factors. Lowering the criterion is increasing the risk of involving meaningless factors, meanwhile significant factors are possibly eliminated with tightening the criterion.

Bayesian networks (BN) were used to construct the
probabilistic graphical model among the variables of the manufacturing process, DPC model parameters, residual stress distribution of tablets, and tablet properties, and to estimate conditional independencies. BN are popular in statistics, machine learning, and artificial intelligence, and are mathematically strict and intuitively understandable. They represent the probabilistic relationships between random variables by using a directed acyclic graph and a set of conditional probability distributions. ${ }^{22)}$ The construction of BNs requires candidates for the parent node (explanatory variable). In this study, a three-layered BN model was constructed, i.e., the process variables were assigned as the parent nodes of the DPC model parameters, and the DPC model parameters were assigned as the parent nodes of the stress distribution of tablets and of the pharmaceutical responses of tablets. The factors were discretized into three categories (low, medium, and high) using the K-means method.

Computer Programs The FEM analysis of the tableting process was performed using ANSYS ${ }^{\circledR} 14.5$ (ANSYS Inc., Canonsburg, PA, U.S.A.). The RSM-S was performed using dataNESIA ${ }^{\circledR}$ version 3.2 (Azbil Corporation, Tokyo, Japan). The MRA was performed using JMP version 8 (SAS Institute Inc., Cary, NC, U.S.A.). The BN model was constructed using BayoNet System software, version 6.0 (Mathematical Systems Inc., Tokyo, Japan).

## Results and Discussion

Evaluation of the Pharmaceutical Responses of Tablets Measured data, such as tensile strength (TS), disintegration

Table 3. Pharmaceutical Responses of All Formulations


[^0]
[^0]:    Each data point is the mean $\pm$ S.D. $(n=3)$.

time (DT), and dissolution property, are summarized in Table 3. Percent dissolved at $10 \mathrm{~min}\left(\mathrm{D}_{10}\right)$ was selected as a typical dissolution property of tablets at the early stage, because the results of a dissolution test revealed the presence of a great difference in each sampling point at 10 min . Although percent dissolved at $30 \mathrm{~min}\left(\mathrm{D}_{30}\right)$ was selected as a late-stage dissolution property, $\mathrm{D}_{10}$ was only used in BN analysis.

The response surfaces for TS, DT, and $\mathrm{D}_{10}$ were estimated using RSM-S based on the original data set. The accuracy of the response surfaces was evaluated via leave-one-out cross-validation (LOOCV), which revealed that the correlation coefficients for TS, DT, and $\mathrm{D}_{10}$ were sufficiently high ( $0.934,0.959$, and 0.888 , respectively). Multiple regression analysis was also performed. The coefficient of determination, which was adjusted using degrees of freedom $\left(R^{* * 1}\right)$ and is an indicator of the fit of each linear regression equation, was estimated. The $R^{* * 2}$ values for TS, DT, and $\mathrm{D}_{10}$ were $0.827,0.765$, and 0.714 , respectively, resulting in poor estimations.

As shown in Fig. 2, the results regarding response surfaces revealed that the TS increased as the kneading time $\left(X_{2}\right)$ and lubricant-mixing time $\left(X_{3}\right)$ decreased and the compression force $\left(X_{4}\right)$ increased. The DT increased with increasing water amount $\left(X_{1}\right), X_{3}$, and $X_{4}$, and decreasing $X_{2}$. The $\mathrm{D}_{10}$ was strongly affected by $X_{1}$ and $X_{3}$, and increased as $X_{1}$ and $X_{3}$ decreased.

Granule properties, such as mean particle size, porosity, and specific surface area, are responsible for tablet characteristics.

For instance, Ohno et al. reported that both the $50 \%$ pore diameter and the $50 \%$ particle diameter have a strong influence on the dissolution property. ${ }^{23)}$ Moreover, the $50 \%$ pore diameter decreases with increasing water amount. Consequently, a greater $X_{1}$ decreased DT and $\mathrm{D}_{10}$ because excessive water induced a decrease of $50 \%$ in pore diameter in this study. Mg-St reduces the interparticle binding strength, DT, and dissolution property, because Mg -St has hydrophobic and flatting characteristics. Therefore, excessive mixing induces a delaying effect regarding the reduction of the hardness of the tablet and the release rate of the drug.

Effect of Process Variables on Simulation Parameters The results of the measurement of Young's modulus ( $E$ ), Poisson rate ( $v$ ), internal friction angle $\left(\alpha^{v}\right)$, plastic deformation $\left(W_{1}^{v}, D_{1}^{v}\right.$, and $\left.D_{2}^{v}\right)$, and initial density $\left(D_{1}\right)$ of each formulation are summarized in Table 4. To understand visually the effect of process variables on simulation parameters, response surfaces for $E$ and $v$ were estimated using RSM-S, as shown in Fig. 3. The accuracy of the response surfaces was evaluated via LOOCV, which revealed that the correlation coefficients for $E$ and $v$ were sufficiently high ( 0.710 and 0.729 , respectively). To evaluate the contribution of each factor to simulation parameters, multiple regression analysis (MRA) was also performed. The results are summarized in Table 5.
$E$ was significantly affected by $X_{4}, X_{2}^{2}, X_{1} \times X_{2}, X_{1} \times X_{3}$, and $X_{2} \times X_{3}$, as shown in Table 4. In particular, the effects of $X_{4}$ and $X_{2} \times X_{3}$ were strong. The analysis of response sur-

Table 4. Simulation Parameters of All Formulations


Each data point (Young's modulus, Poisson rate, internal friction angle, and initial density) is the mean $\pm$ S.D. $(\mathrm{n}=3)$.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Response Surfaces for Tensile Strength (a), Disintegration Time (b), and Percent Dissolved at 10 min (c) as a Function of Water Amount, Kneading Time, Blending Time, and Compression Force

Eighty-one data points obtained by experimental design were analyzed based on RSM-S. LOOCV results showed high prediction ability in all models (more than at least 0.88).

![img-2.jpeg](img-2.jpeg)

Fig. 3. Response Surfaces for Simulation Parameters: Young's Modulus (a and b) and Poisson Rate (c and d)

Eighty-one data points obtained by experimental design were modeled as a function of water amount, kneading time, lubricant-mixing time, and compression force using RSM-S. Background factors were set to intermediate values in all cases.

Table 5. Prediction Accuracy and *p* Value of Multiple Regression Analysis


Each simulation parameter was predicted based on the four process variables. A forward selection method based on stepwise selection was applied to the selection of causal factors, and factors with *p* values >0.25 were successively excluded from the analysis.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison of FEM and Experimental Results: (a) Variation of Axial Stress with Axial Strain during Compaction; (b) Axial Strain of Each Tablet (Rp. 1-27)

In all cases, the experimental values obtained were in good agreement with the FEM results.

Table 6. Correlation Coefficient, Gradient, and Intercept of a Straight Line That Represents the Relationship between the Axial Strain of FEM and Experimental Results at Each Compression Force


![img-4.jpeg](img-4.jpeg)

Fig. 5. Two-Dimensional Maps for the Residual Shear and $x$-Axial and $y$-Axial Stress Distribution of Tablets Estimated Using the FEM
As typical examples, the most homogeneous and inhomogeneous formulations are shown here. The process variables of each formulation are shown in Table 2.
faces showed that a higher $X_{4}$ led to an increased $E . E$ was slightly decreased with decreasing $X_{3}$ (Fig. 3b). Although $E$ increased as $X_{2}$ decreased when $X_{1}$ was high, $E$ increased as $X_{2}$ increased when $X_{1}$ was low (Fig. 3a). A higher $E$ indicates tablets that are more resistant to elastic deformation, because the $E$ of materials represents the stress that is required to produce a corresponding unit of strain. The results of the MRA showed the $v$ was driven by $X_{1}, X_{4}, X_{1}^{2}, X_{3}^{2}$, and $X_{1} \times X_{2}$. The effect of $X_{1}$ on $v$ was comparable to that of $X_{4}$. Response surfaces showed that $v$ increased with decreasing $X_{1}$ and increasing $X_{4}$ (Figs. 3c, d). The impact of compression force on $E$ and $v$ observed here was consistent with the findings of a previous report. ${ }^{1)}$

The $\alpha^{s}$ was affected by $X_{1}, X_{2}, X_{1}^{2}$, and $X_{1} \times X_{3}$ (Table 5), with the impact of $X_{2}$ and $X_{1} \times X_{3}$ being particularly strong. Rp. 1 showed the highest value among the 27 kinds of test formulations (Table 4). Because Rp. 1 was set to have a small
$X_{1}$ and short $X_{2}$, granulation might not have progressed much. This difference might affect the experimental results. $D_{1}$ was affected by $X_{1}, X_{2}, X_{3}, X_{1}^{2}, X_{1} \times X_{2}, X_{1} \times X_{3}$, and $X_{2} \times X_{3}$. More importantly, $X_{1}, X_{1} \times X_{3}$, and $X_{2} \times X_{3}$ contributed strongly to changes in $D_{1}$. In general, a higher granule size yields greater bulk, and granule size is affected by $X_{1}$ and $X_{2}$. Conversely, as $X_{3}$ affects interparticle friction and agglomeration, this effect might contribute to $D_{1}$. The model of $W_{1}^{c}, D_{1}^{c}$, and $D_{2}^{c}$ based on MRA yielded poor estimation value and the effect of factors could not be evaluated well. A possible explanation for this low prediction ability is strong nonlinearity, because plastic deformation of the DPC model was correlated with experimental values and could be modeled by a BN, as shown in the following section.

Comparison of the FEM with Experimental Results The material properties that were obtained from experiments were fed into the ANSYS software, in which the DPC model

![img-5.jpeg](img-5.jpeg)

Fig. 6. Response Surfaces for Simulation Parameters: S.D. of Shear Stress (a and b), S.D. of $\sigma_{y}$ Stress (c and d), and S.D. of $\sigma_{c}$ Stress (e and f), as a Function of Water Amount, Kneading Time, Blending Time, and Compression Force

Twenty-seven data points obtained by FEM were analyzed based on RSM-S. LOOCV results showed high prediction ability in all models. Background factors were set to intermediate values in all cases.
was implemented. The mean values obtained in experiments were used as the DPC model parameters, as shown in Table 4. In this study, appropriate values of the parameters $R_{x}^{\prime}, R_{t}^{\prime \prime}, X_{t}$, $\sigma_{b}$ and $\varphi$ were sought in an arbitrary manner when they could not be measured based on the data, because these parameters have little effect on plastic deformation and stress distribution. ${ }^{20)}$

In many cases, the volume change of the powder during the tableting process was used to compare FEM with experimental results, because there is no concise procedure that enables the simple visualization of the residual stress distribution of tablets. ${ }^{1,11)}$ Figure 4a shows a typical example of the variation of axial stress with axial strain during compaction. This result showed that the FEM and experimental curves were very close. To evaluate all formulations, the axial strain of the com-
pact obtained by FEM was plotted as a function of the axial strain of tablets obtained based on experimental results, and the linear approximation method was applied. Subsequently, correlation coefficient, gradient, and intercept of liner were calculated. The results of tablets and compacts for each compression force are shown in Fig. 4b and Table 6, respectively. This result showed high correlation coefficients in many cases, although a slightly poor estimation was observed at a low compression force ( 1 and 2 kN ). Moreover, the values of gradient and intercept were relatively close to one and zero, respectively, indicating good correlations. These results suggest that FEM results corresponded well to experimental findings.

Impact of Process Variables on Residual Stress Distribution of Tablets The typical residual stress distributions of tablets that showed the most homogeneous and inhomogeneous formulations are shown in Fig. 5. We evaluated the effect only of $X_{1}, X_{2}$, and $X_{3}$, because it is well known that the residual stress increases with increasing $X_{4}$. Consequently, tablets compressed at 8 kN were used for the comparison of residual stress distribution.

The results of the FEM analysis revealed that the trend of the residual stress distribution was similar among model formulations. An intensive shear region was recognized from the top edge to the mid center. In this shear region, the shear stress changed from positive to negative, indicating a change in the direction of the shear stress. Regarding $x$-axial stress $\left(\sigma_{y}\right)$, the top corner exhibited the highest value, whereas the bottom corner exhibited the lowest value. It was clear that the absolute value of $y$-axial stress $\left(\sigma_{y}\right)$ at the top was generally lower than that observed at the bottom. Moreover, the $\sigma_{y}$ value at the top had the stress extending upward, whereas the one at the bottom had the stress extending downward. The overall trend was similar to that reported previously. ${ }^{21)}$

Although the residual stress distribution was similar among model formulations, the ranges of stress values were significantly different. The MRA revealed that the residual stress distribution of tablets was significantly affected by $X_{4}$, as it increased with increasing $X_{4}$. Moreover, an interaction between $X_{2}$ and $X_{3}$ also affected shear and the $x$-axial residual stress of tablets significantly. To evaluate the impact of process variables on residual stress distribution, response surfaces for S.D. of each stress distribution as a function of four process variables were estimated using RSM-S (Fig. 6). A high $X_{1}$ and short $X_{2}$ resulted in low S.D. values, indicating a uniform stress distribution (Figs. 6a, c, e). Conversely, higher $X_{3}$ and $X_{4}$ yielded a more inhomogeneous stress distribution in many cases (Figs. 6b, d, f). There was an optimum blending time of the lubricant, because overblending led to agglomeration and a decrease of interparticle bonding. This phenomenon might cause higher residual stress.

We performed a successful quantitative prediction of tablet characteristics, as well as residual stress distribution, using FEM and RSM-S. Consequently, we were able to seek optimum process variables that were considered not only as tablet characteristics, but also as a risk of having tableting problems.

Construction of a BN Model BNs efficiently implement the probabilistic inference algorithm, which estimates the probability distribution of arbitrary random variables in a model. ${ }^{24,25)}$ To analyze the latent structure among the process variables, FEM parameters, residual stress distribution, and pharmaceutical responses of tablets, BN models were con-

![img-6.jpeg](img-6.jpeg)

Fig. 7. Bayesian Network Model of the Latent Structure among Process Parameters, Simulation Parameters, S.D. of Residual Stress Distribution, and Responses of Tablets Estimated Using the K2 Algorithm

Table 7. Four Standard Measures of Bayesian Network Models Based on Each Measurement Criterion


structed using Akaike's information criteria (AIC), the K2 algorithm, and minimum description length (MDL) as the judging criteria. The distinctive probabilistic model was estimated by the edges, which represent conditional dependencies, and between the nodes, which represent the variables.

The internal structures of BN models differed slightly depending on the judging criteria used. Therefore, the optimal BN model was estimated using the indices of accuracy rate, precision, recall, and $F$-measure. In general, there is a trade-off between precision and recall, as greater precision decreases recall and vice versa. The $F$-measure is the harmonic mean of precision and recall and takes both measures into consideration. When simulation parameters, the S.D. of each stress, and the pharmaceutical responses of tablets were predicted based on process variables, all measures estimated using the model based on the K2 algorithm were greater than 0.77 , indicating that the prediction ability of the probabilistic model is sufficiently high. In contrast, all measures estimated using the model based on AIC and MDL were lower than 0.66 (Table 7). These results led us to conclude that the BN model based on the K2 algorithm has an optimal structure and represents a significant latent structure.

The selection of simulation parameters as input values allowed the calculation of the accuracy rate of the other parameters. This result showed that the accuracy rate of pharmaceutical responses ranged from 0.852 to 0.864 , indicating a high prediction ability. This finding suggests that the simulation parameters are closely related to pharmaceutical responses, such as TS, DT, $\mathrm{D}*{10}$, and $\mathrm{D}*{30}$. However, it might be difficult to predict pharmaceutical responses quantitatively based on simulation factors, because prediction ability decreased drastically when the factors were discretized into five categories. In addition, acceptable results were not obtained based on MRA.

Evaluation of the Relationships between Process Variables, Simulation Parameters, Stress Distribution, and Pharmaceutical Responses Based on the BN Model The BN model constructed here is shown in Fig. 7. The use of a BN model allowed the thorough understanding of the relationships between the variables of the manufacturing process, DPC model parameters, residual stress distribution, and pharmaceutical responses of tablets. The BN model obtained clarified the causal relationships among factors. For instance, Young's modulus $(E)$ was affected by all process variables, and affected TS, DT, and S.D. of $\tau$. The water amount $\left(X_{1}\right)$ and compression force $\left(X_{4}\right)$ had an impact on the Poisson rate $(\nu)$, and $v$ was correlated with TS, DT, and S.D. of $\tau$ and $\sigma_{u}$. $X_{1}$, kneading time $\left(X_{2}\right)$, and blending time $\left(X_{3}\right)$ had an effect on the $\alpha^{y}$. Finally, $\alpha^{y}$ was associated with TS, DT, $\mathrm{D}*{10}, \mathrm{D}*{30}$, and S.D. of $\sigma_{u}$. These results were similar to the MRA results (Table 5).

To evaluate semi-quantitative dependence, the posterior probability of the causal factors was predicted based on the BN model constructed here. Four typical examples of the results obtained are shown in Fig. 8. First, the effect of elastic modules was evaluated. The $X_{4}$ and S.D. of $\tau$ were relatively low at a high $\alpha^{y}$, small $E$, and small $v$. Conversely, a high $\alpha^{y}$, high $E$, and high $v$ yielded a low $X_{1}$ and a high $X_{4}$ and S.D. of $\tau$ (Fig. 8a). This result indicates that $E$ and $v$ increased with de-

![img-7.jpeg](img-7.jpeg)

Fig. 8. Typical Example of the Conditional Probability Distributions (CPDs) of Causal Factors Inferred Using a Bayesian Network Model
(a) CPDs of $X_{1}, X_{4}$, and S.D. of $\tau$ predicted from $\alpha^{x}, E$, and $v$; (b) CPDs of $X_{1}, \mathrm{TS}, \mathrm{D}_{10}$, and S.D. of $\sigma_{x}$ predicted from $\alpha^{x}, E$, and $v$; (c) CPDs of $X_{1}$ and S.D. of $\tau, \sigma_{x}$, and $\sigma_{y}$ predicted from $D_{1}, D_{2}$, and $D_{2}^{c}$; (d) CPDs of $X_{1}, X_{3}$, and S.D. of $\tau$ and $\sigma_{y}$ predicted from $\alpha^{x}, D_{1}, W_{1}^{c}, D_{2}^{c}$, and $D_{2}^{c}$.
creasing $X_{1}$, increasing $X_{4}$, and increasing S.D. of $\tau$. Therefore, we focused on the variation of $\alpha^{x}$. The BN model inferred factors with low $\alpha^{x}$, intermediate $E$, and intermediate $v$ for intermediate $X_{1}$, TS, and $\mathrm{D}_{10}$ tablet values. Conversely, there was no remarkable difference in CPDs at high $\alpha^{x}$, intermediate $E$, and intermediate $v$ (Fig. 8b). This result indicates that $\alpha^{x}$ is a governing factor in this condition. Third, we focused on the variation of $D_{i}$. The BN model inferred factors with low $D_{i}$, intermediate $D_{1}^{c}$, and intermediate $D_{2}^{c}$ for tablet intermediate $X_{3}$, intermediate S.D. of $\tau$, and intermediate S.D. of $\sigma^{x}$. However, there was no remarkable difference in CPDs at high $D_{i}$, intermediate $D_{1}^{c}$, and intermediate $D_{2}^{c}$ (Fig. 8c). Finally, we estimated the critical factors of $\mathrm{D}_{10}$. When tablets had a small $\alpha^{x}$, high $D_{i}$, small $W_{\mathrm{c} 1}$, intermediate $D_{1}^{c}$, and intermediate $D_{2}^{c}$, the BN model inferred parameters with intermediate $X_{2}$, high $X_{3}$, low $\mathrm{D}_{10}$, and high S.D. of $\sigma_{x}$, in contrast, when tablets had small $\alpha^{x}$, intermediate $D_{i}$, intermediate $W_{i}^{1}$, high $D_{1}^{c}$, and intermediate $D_{2}^{c}$, the BN model inferred parameters with low $X_{2}$, intermediate $X_{3}$, high $\mathrm{D}_{10}$, and low S.D. of $\sigma_{x}$ (Fig. 8d). Although a higher $W_{i}^{1}$ resulted in an increase of volume change at all compression forces, a higher $D_{c}^{1}$ indicated a higher volume change at low compression forces. These results suggest that $\mathrm{D}_{10}$ is closely related to plastic deformation and bulkiness, because the $\mathrm{D}_{10}$ value was dramatically changed when $D_{1}, W_{c}^{1}$, and $D_{c}^{1}$ were selected as input values.

## Conclusion

In this study, we investigated the relationships between process variables, residual stress distribution of tablets, and pharmaceutical responses. A direct shear test and instrumented die were used to model the mechanical behavior of pharmaceutical powders. The FEM was used to simulate the compaction behavior of the powders and estimate the residual stress distribution of each formulation. Simulation parameters, such as $E$, $v, \alpha^{x}$, and $D_{i}$, were expressed as a function of the four process variables using MRA, and the impact of process variables on simulation parameters was evaluated. The FEM revealed that the residual stress distribution of tablets was affected by the four process variables. The BN model clarified the causal relationships between process variables, simulation parameters, pharmaceutical responses, and residual stress distribution of tablets. These results demonstrated that FEM is a useful tool to help improve our understanding of residual stress and optimize process variables that are considered not only as tablet characteristics, but also as a risk of having tableting problems.

Acknowledgments This study was supported by a Grant-in-Aid for Scientific Research from the Ministry of Education, Culture, Sports, Science and Technology of Japan. The authors thank Mr. Yuuki Ishida, Department of Pharmaceutics, Hoshi University, for performing the dissolution test.
