# Latent Structure Analysis of the Process Variables and Pharmaceutical Responses of an Orally Disintegrating Tablet 

Yoshihiro Hayashi, ${ }^{a}$ Etsuko Oshima, ${ }^{a}$ Jin Maeda, ${ }^{b}$ Yoshinori Onuki, ${ }^{a}$ Yasuko Obata, ${ }^{a}$ and Kozo Takayama*, ${ }^{a}$<br>${ }^{a}$ Department of Pharmaceutics, Hoshi University; 2-4-41 Ebara, Shinagawa-ku, Tokyo 142-8501, Japan: and<br>${ }^{b}$ Formulation Technology Research Laboratories, Daiichi Sankyo Co., Ltd.; 1-12-1 Shinomiya, Hiratsuka, Kanagawa 254-0014, Japan.

Received June 13, 2012; accepted July 31, 2012; advance publication released online August 10, 2012


#### Abstract

A multivariate statistical technique was applied to the design of an orally disintegrating tablet and to clarify the causal correlation among variables of the manufacturing process and pharmaceutical responses. Orally disintegrating tablets (ODTs) composed mainly of mannitol were prepared via the wet-granulation method using crystal transition from the $\boldsymbol{\delta}$ to the $\boldsymbol{\beta}$ form of mannitol. Process parameters (water amounts $\left(X_{1}\right)$, kneading time $\left(X_{2}\right)$, compression force $\left(X_{3}\right)$, and amounts of magnesium stearate $\left(X_{4}\right)$ ) were optimized using a nonlinear response surface method (RSM) incorporating a thin plate spline interpolation (RSM-S). The results of a verification study revealed that the experimental responses, such as tensile strength and disintegration time, coincided well with the predictions. A latent structure analysis of the pharmaceutical formulations of the tablet performed using a Bayesian network led to the clear visualization of a causal connection among variables of the manufacturing process and tablet characteristics. The quantity of $\beta$-mannitol in the granules $\left(Q_{\beta}\right)$ was affected by $X_{1}$ and influenced all granule properties. The specific surface area of the granules was affected by $X_{1}$ and $Q_{\beta}$ and had an effect on all tablet characteristics. Moreover, the causal relationships among the variables were clarified by inferring conditional probability distributions. These techniques provide a better understanding of the complicated latent structure among variables of the manufacturing process and tablet characteristics.


Key words multivariate analysis; orally disintegrating tablet; response surface method; optimization; process variable; Bayesian network

In recent years, orally disintegrating tablets (ODTs) have become popular worldwide. ODTs are preferred by an increasing number of patients, especially children and the elderly, but also adults who like to have their medication readily available at any time. Various compositions and manufacturing methods of orally disintegrating or dissolving tablets have been reported. ${ }^{1-3)}$ However, ODTs have several disadvantages: they are generally brittle and a special apparatus is needed for their manufacture. Therefore, ODTs are difficult to prepare in their final dosage form.

The relationships among the variables, quality attributes of in-process materials, and pharmaceutical characteristics involved in the design of pharmaceutical products are intricate. Therefore, the expertise and experience of formulators are essential for the design of an acceptable product formulation and of a manufacturing process. The empirical approach requires a long development time and significant resources. In recent years, the application of statistical methods to pharmaceutical development has been implemented, to allow International Conference on Harmonisation (ICH) Q trio guidance (Q8, Q9, and Q10). ${ }^{4-6)}$ This requires the use of a combination of chemometric treatments, including the design of experiments (DoEs), the response surface method (RSM), and multivariate analyses. ${ }^{7)}$

DoE is a rational and well-organized technique that is used to determine the critical attributes that may influence a product or process. DoE overcomes the problems associated with one-component-at-a-time experiments, in which interactive effects between factors cannot be clarified. DoE also
helps understand how typical fluctuations around mean input values can influence the properties of the final product. The RSM is used for DoE analysis and for resolving optimization problems. ${ }^{8-10)}$ The RSM is also used for the wide visualization of the relationships between causal factors and responses. We have developed a nonlinear RSM incorporating thin plate spline interpolation (RSM-S), which has been used to determine acceptable formulations of pharmaceutical compounds. Using RSM-S, we can easily understand the nonlinear relationships between causal factors and response variables and estimate a robust optimal solution. ${ }^{11,12)}$

A Bayesian network (BN) is potentially useful to understand the causal relationships among the variables of input, internal, and output elements. BN is a directed acyclic graphical approach that expresses the probabilistic causal relationships among attributes and in which probabilistic relationships are expressed by nodes and by the links connecting the nodes. ${ }^{13)}$ BN offers many advantages over a sample of all possible observations. Recently, BN has been used widely in various fields, including applied statistics, medicine, and bioinformatics. ${ }^{14-17)}$

In this study, we optimized the process parameters using RSM-S and determined the granule properties that are closely associated with process variables and responses of ODTs. We applied a BN to analyze the causal correlations among variables of the manufacturing process, granules, and tablet properties. A BN was used to construct a probabilistic graphical model of the latent structure of ODTs and to reveal the latent structure in the manufacture of these tablets.

[^0]
[^0]:    The authors declare no conflict of interest.

## Experimental

Materials Indomethacin (IMC), which was used as a model drug and magnesium stearate (Mg-St) were purchased from Hachidai Pharmaceutical Company, Ltd. (Osaka, Japan) and Wako Pure Chemical Industries, Ltd. (Osaka, Japan), respectively. The $\delta$ form of mannitol (Parteck ${ }^{\circledR}$ Delta M) was purchased from Merck KGaA (Darmstadt, Germany). Microcrystalline cellulose (MCC; Ceolus PH-101, Asahi Kasei Chemicals Co., Ltd., Tokyo, Japan) was a gift from Daiichi Sankyo Co., Ltd. (Tokyo, Japan). Cross povidone (Cross-PVP; Polyplasdone ${ }^{\circledR}$ XL, ISP Co., Ltd., NJ, U.S.A.) was a gift from Nippon Shokubai Company, Ltd. (Osaka, Japan).

Preparation of ODTs Process conditions were fixed according to the flow chart presented in Fig. 1. The ingredients were accurately weighed according to the experimental formulations and all ingredients, with the exception of Mg-St, were blended using a mixer (KM4005, De'Longhi, Italy) for 1 min . Distilled water was added as a granulation liquid and the mixture was kneaded (impeller speed, 470 rpm ; processing time, $1-9 \mathrm{~min}$ ). After the granulation process, the granules were sieved through a 5.8 mm mesh. The granules were dried at $75^{\circ} \mathrm{C}$ for 30 min and sieved through a $850 \mu \mathrm{~m}$ mesh. Mg -St was added to the granules and the mixture was blended in a polyethylene bag for 1 min . The final blend was compressed into round-faced tablets ( $200 \mathrm{mg}, 8 \mathrm{~mm}$ in diameter, with a 12 mm radius of curvature) using a tableting machine (Handtab-100, Ichihashi-Seiki Co., Ltd., Kyoto, Japan). All the formulations were composed of 25 mg of IMC, 145 mg of $\delta$-mannitol, 20 mg of Cross-PVP, and 10 mg of MCC.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Flow Chart of the Granulation Process

Experimental Design To develop systematic model formulations, 27 kinds of tablets containing indomethacin, $\delta$-mannitol, Cross-PVP, MCC, and Mg-St were prepared according to a Box-Behnken design (Table 1). Water amount $\left(X_{1}\right)$, kneading time $\left(X_{2}\right)$, compression force $\left(X_{3}\right)$, and amount of $\mathrm{Mg}-\mathrm{St}\left(X_{4}\right)$ were selected as the design variables.

Evaluation of Tablet Properties The hardness of the tablets was determined using a tablet hardness tester (Ogawa Seiki Co., Tokyo, Japan). Tensile strength (TS) was calculated as:

Table 1. Box-Behnken Experimental Design of Four Design Variables and Response Variables


![img-1.jpeg](img-1.jpeg)

Fig. 2. Response Surfaces of Orally Disintegrating Tablets Estimated Using RSM-S Based on Water Amount, Kneading Time, Compression Force, and Quantity of Mg-St

Panels (a) and (b) indicate tensile strength and disintegrating time, respectively.

$$
T S=\frac{2 F}{\pi d t}
$$

where $F$ is the maximal diametrical crushing force and $d$ and $t$ are the diameter and thickness of the tablet, respectively. The TSs of three tablets of each formulation were measured. The disintegration test was performed according to the JP16 disintegration test for tablets using a disintegration tester (NT-20H; Toyama Sangyo Co., Ltd., Osaka, Japan) and water (as a solvent) at $37^{\circ} \mathrm{C}$. Disintegration time (DT) was defined as the interval required for the complete disappearance of a tablet or its particles from the tester net. DT was measured for three tablets of each formulation. The dissolution test was performed according to the JP16 dissolution test No. 2 (the paddle method) at 100 rpm (NTR-6100A, Toyama Sangyo Co., Ltd.). The dissolution medium used was 900 mL of mixture of 1 volume of 0.05 m phosphate buffer ( pH 7.2 ) and 4 volumes of distilled water at $37 \pm 0.5^{\circ} \mathrm{C}$. The samples were collected and filtered after $5,10,15,20,25,30,40$, and 50 min . The concentration of indomethacin was measured spectrophotometrically at 320 nm using a Jasco Ubest-30 spectrophotometer (Japan Spectroscopic Company, Ltd., Tokyo, Japan). The dissolution rates of three tablets of each formulation were measured.

Physicochemical Properties of Granules Quantities of $\beta$-mannitol $\left(Q_{\beta}\right)$, specific surface area $\left(S_{w}\right)$, and mean size $\left(d_{50}\right)$ and relative width $\left(R_{w}=\left(d_{10}-d_{10}\right) / d_{50}\right)$ of particles were measured. The $Q_{\beta}$ of granules was determined via a combination technique using a X-ray powder diffractometer (XRD; RINT-1400 X-ray diffractometer, Rigaku, Tokyo, Japan) and a partial least squares (PLS) regression analysis. ${ }^{(8)}$ These measurements were carried out at $40 \mathrm{kV}, 40 \mathrm{~mA}$ with a $\mathrm{Cu} K \alpha$ source between $5^{\circ}$ and $30^{\circ} 2 \theta$ with a scan speed of $2.0^{\circ} / \mathrm{min}$ in the step scan mode.

The $S_{w}$ of the granules was measured using the single-point BET method (Macsorb HM model-1201, Mountech, Tokyo, Japan). Before measurement, about 1 g of each sample was weighed in a sample tube and was then degassed for 30 min at a temperature of $60^{\circ} \mathrm{C}$ using nitrogen as the purge gas. Subsequently, the specific surface area of the granules was measured using nitrogen adsorption.

The $d_{50}$ and $R_{\mathrm{w}}$ of granules were determined based on the
distribution of particle sizes, which was measured using a sieving machine (Robot Shifter RPS-105, Seisin Enterprise, Tokyo, Japan) using the following sieves: $75,106,150,212$, 300,500 and $800 \mu \mathrm{~m}$. Samples of 10 g were passed through the sieves and stirred during a predefined time of 3 min . Finally, the powder fraction held in each sieve was weighed.

Computer Programs The nonlinear RSM was performed using dataNESIA ${ }^{\circledR}$ version 3.2 (Yamatake Corporation, Fujisawa, Japan). Multiple linear regression analysis was performed using Microsoft Excel ${ }^{\circledR}$ for Windows 2007 (Microsoft Corporation, Redmond, WA, U.S.A.). A chemometric analysis for XRD data was performed using the PLS program associated with the Unscrambler 9.0 software (Camo Technologies, Woodbridge, NJ, U.S.A.). The BayoNet System software, version 5.0. (Mathematical Systems Inc., Tokyo, Japan) was used to construct the probabilistic graphical model among the variables manufacturing process, granules, and tablet properties and to estimate conditional independencies.

## Results

Prediction of the Responses of Tablets Using RSM-S TS and DT were measured as tablet properties. The response surfaces for each tablet property were estimated using RSM-S based on the original data set. The accuracy of the response surfaces was evaluated via leave-one-out cross-validation (LOOCV), which revealed that the correlation coefficients for TS and DT were sufficiently high ( 0.977 and 0.979 , respectively). The response surfaces of the tablet properties are shown in Fig. 2. The TS increased as the water amount $\left(X_{1}\right)$, kneading time $\left(X_{2}\right)$, and compression force $\left(X_{3}\right)$ increased. The amount of $\mathrm{Mg}-\mathrm{St}\left(X_{4}\right)$ had a negligible effect on TS. The DT decreased as $X_{1}, X_{2}, X_{3}$, and $X_{4}$ decreased. Formulations Rp. 13 and Rp. 20 showed the lowest and highest value of DT in all formulations tested, respectively. Therefore, the dissolution test was performed in the limited way to formulations Rp. 13 and Rp. 20. The dissolution rates at 5 min for IMC from formulations Rp. 13 and Rp. 20 were $93.1 \pm 1.7 \%$ and $92.1 \pm 2.6 \%$, respectively. No significant difference was observed between Rp. 13 and Rp. 20.

Optimization of Process Variables Using RSM-S The process variables of tablets were optimized using RSM-S

based on the original data set. The optimization problem was formulated to maximize TS and to minimize DT with an even weight within the range of experimental space. Results of the simultaneous optimum analysis are given in Table 2. The water amount $\left(X_{1}\right)=30.57 \%$, kneading time $\left(X_{2}\right)=3.16 \mathrm{~min}$, compression force $\left(X_{3}\right)=4.04 \mathrm{kN}$, and the amount of $\mathrm{Mg}-\mathrm{St}$ $\left(X_{4}\right)=1.45 \%$ were estimated as the optimal process variables. The following were estimated as the optimal response variables: $\mathrm{TS}=0.98 \mathrm{MPa}$ and $\mathrm{DT}=10.72 \mathrm{~s}$. Table 2 also shows the TS and DT of the optimal process variables. The TS and DT values predicted by RSM-S coincided well with the experimental values.

Prediction of Granule Properties Using RSM-S $Q_{\beta}$, $S_{w}, d_{50}$, and $R_{w}$ were measured as granule properties. The response surfaces for each granule property were estimated using RSM-S based on the original data set. The accuracy of the response surfaces was evaluated by LOOCV, which revealed that the correlation coefficients for $Q_{\beta}, S_{w}, d_{50}$, and $R_{w}$ were sufficiently high $(0.935,0.929,0.899$ and 0.885 , respectively). The analysis of response surfaces showed that the $Q_{\beta}$ and granules increased with increasing kneading time $\left(X_{2}\right)$; however, water amount $\left(X_{1}\right)$ had only a small effect on $Q_{\beta}$. $S_{w}$ increased with increasing water amount $\left(X_{1}\right)$ and kneading time $\left(X_{2}\right) . d_{50}$ was highest for high water amounts $\left(X_{1}\right)$ and short kneading times $\left(X_{2}\right)$. In contrast, $R_{w}$ was highest for small water amounts $\left(X_{1}\right)$ and long kneading times $\left(X_{2}\right)$ (Fig. 3).

Estimation of a Quantitative Latent Structure Model Using a Bayesian Network An analysis of the causal relationships among process variables and granule and tablet properties was used to estimate the latent structure model using a BN. All variables were discretized to three levels for the inference of the conditional probability distribution. The optimal BN models were predicted using Akaike's information criterion (AIC), the K2 algorithm, and minimum description length (MDL) as the judging standards. The accuracy, precision, recall, and $F$-measure of the BN models were evaluated (Fig. 4). The BN model obtained based on the K2 algorithm (Fig. 5) was the highest for all parameters. $Q_{\beta}$ was affected by kneading time $\left(X_{2}\right)$ and had an effect on all granule properties. $S_{w}$ was affected by water amount $\left(X_{1}\right)$ and kneading time $\left(X_{2}\right)$ and had an effect on all tablet properties. No links from the node of the amount of $\mathrm{Mg}-\mathrm{St}\left(X_{4}\right)$ were observed.

Evaluation of the Causal Relationships Underlying the

Table 2. Predicted and Experimental Values of Response Variables of Optimal Process Variables Based on the RSM-S


Latent Structure via Probabilistic Inference Using a Bayesian Network Using BN modeling, the posterior probability of the causal factors was also predicted by conditional probability distributions (CPDs). To clarify the effects on $Q_{\beta}$, the posterior probabilities of the causal factors were predicted from $Q_{\beta}$ and compression force $\left(X_{3}\right)$. The BN model inferred factors with a short kneading time $\left(X_{2}\right)$, low $S_{w}$, middle $D_{50}$, intermediate $R_{w}$, low TS, and short DT for tablets with an intermediate compression force $\left(X_{3}\right)$ and a low $Q_{\beta}$. Conversely, the BN model inferred factors with an intermediate kneading time $\left(X_{2}\right)$, high $S_{w}$, low $D_{50}$, high $R_{w}$, intermediate TS, and intermediate DT for tablets with an intermediate compression $\left(X_{3}\right)$ force and a high $Q_{\beta}$ (Fig. 6).

## Discussion

In this study, tablets containing mainly mannitol, CrossPVP, and MCC were prepared. Mannitol, Cross-PVP, and MCC were chosen as the filler, the disintegrating, and the binding agents, respectively.

Generally, ODTs are produced using a particular manufacturing method. Recently, it was reported that ODTs were also produced by a wet-granulation process using a polymorphic transition from the $\delta$ to the $\beta$ form of mannitol. ${ }^{19,20)}$ In this study, we applied this technique to prepare ODTs.

We selected the amount of water $\left(X_{1}\right)$ (as the granulation liquid), kneading time $\left(X_{2}\right)$, compression force $\left(X_{3}\right)$, and amount of $\mathrm{Mg}-\mathrm{St}\left(X_{4}\right)$ as design variables. Water amount $\left(X_{1}\right)$ and kneading time $\left(X_{2}\right)$ may influence granule properties, such as $Q_{\beta}, S_{w}, d_{50}$, and $R_{w}$, and have an indirect impact on tablet properties. Conversely, compression force $\left(X_{3}\right)$ and amount of $\mathrm{Mg}-\mathrm{St}\left(X_{4}\right)$ may also have a direct effect on tablet properties. When the water amount $\left(X_{1}\right)$ reached ca. $45 \%$, we could (a)

![img-2.jpeg](img-2.jpeg)

Fig. 3. Response Surfaces of Granule Properties Estimated Using RSM-S Based on Water Amount and Kneading Time (a) Amount of $\beta$-mannitol, (b) specific surface area, (c) mean particle size, and (d) relative width.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Four Standard Measures of Bayesian Network Models Based on Each Measurement Criterion
not prepare granules; therefore, the upper limit of the water amount $\left(X_{1}\right)$ was set at $40 \%$. A dissolution test revealed an absence of significant differences between Rp. 13 and Rp. 20. In contrast, Rp. 13 and Rp. 20 exhibited the lowest and longest disintegration times, respectively. This result suggests that all formulations tested have an excellent dissolution property. Therefore, we did not perform dissolution tests for the other formulations.

Response variables, such as $Q_{\beta}, S_{w}, d_{50}, R_{w}$, TS, and DT, were predicted accurately using RSM-S, as shown clearly by the results of the LOOCV. Multiple regression analysis was also performed and the coefficient of determination, which was adjusted with degrees of freedom $\left(R^{* * 2}\right)$ and is an indicator of the fit of each linear regression equation, was estimated.

The $R^{* * 2}$ values for $Q_{\beta}, S_{w}, d_{50}, R_{w}$, TS, and DT were 0.712 , $0.736,0.747,0.89,0.861$, and 0.699 , respectively, resulting in poor estimations; a better result was observed using RSM-S.

The RSM is used widely to visualize the relationships between causal factors and responses. However, this method is limited to the three-dimensional (3D) space and includes basic information about the relationship between only two limited factors and one response. The hyper-Dimensionally Embedded Cuboids (hyperDEC) technique has been developed as a novel approach to visualize multivariable relationships. ${ }^{21)}$ This method overcomes the limitation of the contour plots of 3D surface plots, which cannot display simultaneously the effects of more than two variables. Using an approach similar to hyperDEC, we were able to viscerally and quantitatively understand the relationships between causal factors and responses (Fig. 2). Both TS and DT increased with increasing water amount $\left(X_{1}\right)$, kneading time $\left(X_{2}\right)$, and compression force $\left(X_{3}\right)$. TS surface was similar to DT, indicating that TS and DT were trade-off.

The relationship between two design variables and granule properties were clarified using RSM-S (Fig. 3). Figure 3a suggests that a polymorphic transition from the $\delta$ to the $\beta$ form of mannitol was induced by the wet-granulation process. A concomitant morphological change resulted in an agglomerate consisting of filament-like fine primary crystals ( $\delta$-granule). This phenomenon gave rise to an increase in $S_{w}$. Therefore, the response surface of $Q_{\beta}$ was similar to the $S_{w}$, indicating that $Q_{\beta}$ has a strong influence on $S_{w}$. Because $S_{w}$ was affected not only by $Q_{\beta}$ but also by water amount $\left(X_{1}\right)$, kneading time $\left(X_{2}\right)$, and $d_{50}$, the response surface for the $S_{w}$ was barely different from $Q_{\beta}$.

BNs efficiently implement the probabilistic inference algorithm, which estimates the probability distribution of arbitrary random variables in a model. ${ }^{22,23)}$ To analyze the latent structure among causal factors, granule properties, and responses in ODTs, BN models were constructed using AIC, the K2 algorithm, and MDL as the judging criteria. The internal structures of BN models differed slightly depending on the judging criteria. Therefore, the optimal BN model was estimated using the indices accuracy rate, precision, recall, and
![img-4.jpeg](img-4.jpeg)

Fig. 5. Bayesian Network Model of the Latent Structure among Process Parameters, Granule Properties, and Responses of Tablets Estimated Using the K2 Algorithm

![img-5.jpeg](img-5.jpeg)

Fig. 6. Conditional Probability Distributions (CPDs) of Causal Factors Inferred Using a Bayesian Network Model
Compression pressure and amount of $\beta$-mannitol were set as prior probabilities. The CPDs of the causal factors were estimated for two cases: intermediate compression force and small amount of $\beta$-mannitol, and intermediate compression force and large amount of $\beta$-mannitol.
$F$-measure. In general, there is a trade-off between precision and recall, as greater precision decreases recall and vice versa. The $F$-measure is the harmonic mean of precision and recall and considers both measures. All measures estimated using the model based on the K2 algorithm were more than $90 \%$ accurate, indicating that the prediction ability of the probabilistic model is sufficiently high. In contrast, all measures estimated using the model based on AIC and MDL were less than $90 \%$ accurate (Fig. 4).

The distinctive probabilistic model was estimated by the edges, which represent conditional dependencies, and between the nodes, which represent the variables. The use of a BN model allowed the thorough understanding of the relationships among the variables of the manufacturing process and granule and tablet properties (Fig. 5). As usual, TS and DT are strongly affected by the amount of Mg-St. However, no links between $\mathrm{Mg}-\mathrm{St}\left(X_{\mathrm{t}}\right)$ and TS or DT were observed, as shown in Fig. 5. As shown in Fig. 2, the effect of $X_{\mathrm{t}}$ on TS and DT was rather weak compared with that of the other factors. This may be due to the limited amounts of Mg-St, which were $\leq 2.5 \%$. Another explanation is that the powder sample used to prepare granules was small ( 200 g ) in this study. It is well known that the lubricant effect of Mg -St is dependent on the scale of the samples.

Although $S_{w}, d_{50}$, and $R_{w}$ were mutually dependent, in general, the BN model showed no significant effect of $d_{50}$ and $R_{w}$ on TS and DT. This result indicates that $S_{w}$ is selected as a representative of granule parameters, such as $d_{50}$ and $R_{w}$.

The CPDs of the factors of the ODTs were predicted using
the BN model. The posterior probabilities of the factors for intermediate compression force and high and low $Q_{\beta}$ were appropriately estimated (Fig. 6). The BN model was able to estimate not only the effects of the causal factors on each response, but also the trends in the responses produced by the formulations as CPDs.

## Conclusion

In this study, ODTs composed of IMC, mannitol, CrossPVP, and MCC were prepared. The robustness of the response surfaces estimated via RSM-S was elucidated sufficiently, with high correlation coefficients observed in LOOCV. Optimal process variables were predicted quantitatively using RSM-S. Moreover, a latent structure analysis based on the variables of manufacturing process and granule and tablet properties was performed using BN. We visualized clearly the nonlinear relationships among the variables and identified several important correlations among them.

Acknowledgments This study was supported by a Grant-in-Aid for Scientific Research from the Ministry of Education, Culture, Sports, Science and Technology of Japan. The authors thank Mr. Shozo Iwasaki, Department of Pharmaceutics, Hoshi University, for preparing granules and tablets and Mr. Takaya Sato, CAMO Software Japan Co., Ltd., for assistance with the chemometric approach.
