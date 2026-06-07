# Article 

## Assessment of Infrastructure Reliability in Expansive Clays Using Bayesian Belief Network

Golam Kabir ${ }^{1, * *}$ and Shahid Azam ${ }^{2 *}$ (D)<br>check for updates<br>Citation: Kabir, G.; Azam, S.<br>Assessment of Infrastructure Reliability in Expansive Clays Using<br>Bayesian Belief Network. CivilEng 2022, 3, 1126-1136. https:// doi.org/10.3390/civileng3040064<br>Academic Editors: Panagiotis<br>Michalis, Manousos Valyrakis,<br>Gordon Gilja and Zied Driss<br>Received: 1 November 2022<br>Accepted: 15 December 2022<br>Published: 18 December 2022

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Industrial Systems Engineering, Faculty of Engineering and Applied Science, University of Regina, 3737 Wascana Parkway, Regina, SK S4S 0A2, Canada
2 Environmental Systems Engineering, Faculty of Engineering and Applied Science, University of Regina, 3737 Wascana Parkway, Regina, SK S4S 0A2, Canada

* Correspondence: golam.kabir@uregina.ca


#### Abstract

Civil infrastructure supported by expansive clays is severely affected by extensive volumetric deformations. The reliability prediction of such facilities is quite challenging because of the complex interactions between several contributing factors, such as a scarcity of data, a lack of analytical equations, correlations between quantitative and qualitative information, and data integration. The main contribution of this research is the development of a modeling approach based on the Bayesian belief network. The modeling results highlight that facility age is the most critical parameter ( $23 \%$ variance), followed by facility type ( $1.37 \%$ variance), for all the investigated types of infrastructure, namely road embankments, buried pipelines, and residential housing. Likewise, the results of sensitivity analysis and extreme scenario analysis indicate that the new method is capable of predicting infrastructure reliability and the assessments were found to be in agreement with expected field behavior. The proposed model is useful in decision making related to civil infrastructure management in expansive clays.


Keywords: expansive clays; infrastructure reliability; volume change; Bayesian network

## 1. Introduction

Expansive clays constitute a class of problematic soils that exhibit swelling and shrinkage due to changes in water content. Civil infrastructure supported by such soils experiences either volumetric deformations due to soil movement or stresses when such movements are restrained [1]. Successive wet-dry cycles due to seasonal weather variations result in gradual fatigue in structural components and the eventual breakage of the facilities, such as municipal roads [2], pipeline networks [3], and residential housing [4]. This is especially true for Regina (Saskatchewan, Canada), where the interplay of a glaciolacustrine expansive clay and a dry continental climate results in extensive damages to lightly loaded structures at the ground surface and at shallow depths [5]. Furthermore, extreme weather events such as high-intensity rainfall and long-lasting droughts have been observed to occur more frequently in the region [6]. Given the continuously increasing maintenance costs, there is a need to predict the reliability of aging infrastructure supported by expansive clays.

The prediction of infrastructure reliability in expansive soil deposits is quite challenging because of the complex interactions between several contributing factors, such as soil properties, hydraulic parameters, ground conditions, and infrastructure type. The nonlinear relationships are further complicated by the following: (i) the scarcity of experimental data; (ii) the lack of analytical equations; (iii) the lack of correlation between quantitative and qualitative information; and (iv) the lack of integration of data from all sources. Clearly, there is a knowledge gap in effectively capturing these wide-ranging issues.

The various challenges can be addressed using different methodologies, such as analytic network processes, fuzzy cognitive maps, artificial neural networks, and the

Bayesian belief network (BNN). Qualitative and comparative evaluations of the available methods [7,8] demonstrated that a BBN-based framework is best suited for infrastructure reliability. Probabilistic graphical approaches based on this method can characterize the uncertainty associated with variables [9]; provide informed decisions in cases of imprecise, incomplete, and ambiguous information [10]; and are flexible to conduct diagnostic analysis (to determine the reasoning for possible causes by observing the effect) or predictive analysis (to determine the reasoning for possible effects by observing the cause) [11,12].

The main purpose of this research was to develop a BBN-based model for the prediction of infrastructure reliability in expansive clays. The BBN-based model is described from the perspective of the theoretical background, parameter selection, data collection and analysis, and model architecture. The modeling results are presented based on both quantitative (sensitivity analysis) and qualitative (extreme scenario analysis) approaches.

# 2. Modeling of Bayesian Belief Network 

### 2.1. Parameter Selection

Swelling and shrinkage in the expansive Regina clay depend on the following distinct but interrelated parameters: (i) soil geology and geotechnical properties [13,14]; (ii) ground cover and vegetation type [15,16]; (iii) seasonal weather and environmental conditions [17,18]; and (iv) hydrologic conditions and depth below surface [19,20]. Based on these factors, a simplified approach was adopted for the selection of parameters affecting volume changes in the expansive clay. First, soil properties were considered to be constant across the city, although there is some variation in the geological deposit in terms of composition in the vertical and lateral directions. Second, ground cover was only considered at two levels, namely an exposed surface (lawns, fields, cemeteries) that allows direct interaction with the atmosphere to allow water migration into and out of the soil, and a covered surface (roads, houses, buildings) that precludes infiltration and evaporation. A similar rationale was adopted for vegetation-that is, the presence of a tree supports transpiration and vice versa. Third, the meteorological parameters of precipitation and evaporation (temperature, humidity, wind, radiation) were collectively represented in terms of ground water content. Environmental conditions such as heat from buildings, corrosion from pipes, and deicing salts from roads were not included. Fourth, hydrologic conditions were identified as either free drainage with no water flowing through the soil or surface ponding facilitating water migration through the soil. Likewise, the depth below surface was considered up to 3.0 m , beyond which the overburden stress cancels out the swelling deformations [21].

The factors affecting infrastructure integrity in Regina included the type and age of the facility. Three types of lightly loaded facilities were selected, namely surface roads, buried pipelines, and residential units. Likewise, a service life of up to 70 years was used to incorporate age. Parameters such as material type, deterioration mechanism, and exposure conditions were considered to be included in the age of the various facilities.

### 2.2. Data Collection and Analysis

Figure 1 gives field data in the investigated expansive clay profile. The ground water content (Figure 1a) from March to November in different years were reported by Azam et al. [22], Fredlund [23], Hamilton [18], Hu and Vu [16], Hu et al. [24], and Yoshida et al. [21]. Compiled by Ito and Azam [25], the water content depicted a vague funnel-like shape around the plastic limit $(27 \% \pm 5)$, with large variations at the surface and a gradual decrease with depth. Using the plastic limit as the datum, the change in water content was used to determine the cumulative volume change (Figure 1b) following the method developed by Ito and Azam [25]. This figure shows a distinct funnel-like shape with up to 100 mm of volumetric deformations close to the surface, and these values gradually diminished around a 3.0 m depth. Furthermore, Figure 2 summarizes the field data in terms of histograms for ground water content, depth below ground, volume change,

and cumulative change. For each of the parameters, the histograms pertain to six distinct levels, thereby gradually capturing field behavior.
![img-0.jpeg](img-0.jpeg)

Figure 1. Field data for the investigated expansive clay profile. (a) Ground water content, (b) cumulative volume change.
![img-1.jpeg](img-1.jpeg)

Figure 2. Histograms of field data for the investigated expansive clay. (a) Ground water content, (b) depth below ground, (c) volume change, (d) cumulative volume change.

2.3. Model Architecture

A BBN-based modeling approach was used. Conceptually, the process is to perform probabilistic inferences or belief updating based on data or observations using the Bayes theorem [26]. Figure 3 shows the proposed BBN-based model for predicting infrastructure reliability in expansive clays. The qualitative component of the model comprised nodes to identify variables of interest and links to denote conditional relationships among the variables [10,27]. The figure shows that nine (9) independent or parent nodes and five (5) dependent or child nodes were connected with fourteen (14) causal links. Likewise, the quantitative component of the model was presented as a set of conditional probabilities for each child node based on the information related to the parent node [28]. The states and units of both the parent and the child nodes are summarized in Table 1.

![img-2.jpeg](img-2.jpeg)

Figure 3. Proposed infrastructure reliability prediction model for expansive clays.

Table 1. States and units of parent and child nodes.


The model architecture was developed using the Netica software [29]. The prior and posterior probabilities of the nodes were calculated after establishing the causal diagram. The updated probability for the $m$ number of mutually exclusive variables $V_{i(i=1,2, \ldots, m)}$ and the given data $D$ was determined according to the following equation [9]:

$$
p\left(V_{i} \mid D\right)=\frac{p\left(D \mid V_{i}\right) \times p\left(V_{i}\right)}{\sum_{i=1}^{m} p\left(D \mid V_{i}\right) \times p\left(V_{i}\right)}
$$

In the above equation, $p\left(V_{j} \mid D\right)$ represents the posterior probability; $p\left(V_{j}\right)$ refers to the prior probability; and $p\left(D \mid V_{j}\right)$ denotes the conditional probability considering that $V_{j}$ is true. The constant value of the denominator represents the total probability.

The dependencies between the child nodes and the parent nodes were quantified using a Conditional Probability Table (CPT). The CPT values of the child nodes were based on the training of exiting field data following the procedure outlined in Kabir et al. [30] and Tang and McCabe [31], as well as on expert judgment following the method given by Cárdenas et al. [32] and Cai et al. [33].

Referring to Figure 3, the CPT values of the GWC, the Delta_GWC, and the Depth nodes were determined based on the compiled data presented in Ito and Azam [25]. Utilizing constant values for the Swell-Shrink Modulus (1.2) and Ratio of Vertical to Horizontal Movement (0.33), an analytical equation given in Ito and Azam [25] was used to calculate the CPT values of the Volume Change node. In contrast, the CPT values for Plantation,

Ground Cover, and Ground Slope were considered to have uniform probabilities and, based on expert judgement, collectively affected Flow Through. The Volume Change and Flow Through were used to generate the CPT values for the Cum_Volume_Change node based on an expectation-maximization algorithm [29,34]. Furthermore, the CPT values for Age and Facility Type were considered to have uniform probabilities and collectively resulted in the Infrastructure_Stability node. Based on expert judgement, the Cum_Volume_Change node and the Infrastructure_Stability node were analyzed to estimate Reliability.

Table 2 presents an example of the determination of the conditional probabilities based on knowledge elicitation. The child node Flow Through depends on parent nodes Ground Cover, Ground Slope, and Plantation. Using an exposed surface, a slope that facilitates free drainage and the presence of trees, the corresponding CPT values for Flow Through are $(33,67)$. These values indicate that the conditional probabilities for Flow Through being in the state of "Yes" and "No" are $33 \%$ and $67 \%$, respectively. The CPTs of the Infrastructure Stability and Reliability nodes were calculated in a similar way. A total of 487 conditional probabilities were generated.

Table 2. Example of determination of conditional probabilities based on knowledge elicitation.


# 3. Results and Discussion 

### 3.1. Results

Sensitivity analysis was performed to identify critical parameters affecting infrastructure reliability due to volume changes in expansive clays. The variance reduction method $[7,29]$ was used to perform the sensitivity analysis because the input parameters have both discrete (such as tree or no tree) and continuous (such as 12-17 or 17-22) values. The variance $(V(R / t))$ of the real value of $R$ (such as Reliability) due to given evidence $T$ (such as age, water content, plantation, or depth) of state $t$, was calculated according to the following equation $[9,29]$ :

$$
V(R \mid t)=\sum_{r} p(r \mid t)\left[Y_{r}-E(R \mid t)\right]^{2}
$$

In the above equation, $r$ is the state of the query node $R, p(r / t)$ represents the conditional probability, $Y_{r}$ denotes the numeric value corresponding to state $r$, and $E(R / t)$ indicates the expected real value of $R$ after the new finding $t$ for node $T$.

Table 3 gives a summary of the sensitivity analysis. Table 4 gives the results of the extreme scenario analysis. Figure 4 shows the infrastructure reliability curves due to swelling.

Table 3. Summary of sensitivity analysis.


Table 4. Summary of extreme scenario analysis.


Table 4. Cont.


![img-3.jpeg](img-3.jpeg)

Figure 4. Cont.

![img-4.jpeg](img-4.jpeg)

Figure 4. Infrastructure reliability curves due to swelling. (a) 27 to 32 GWC, (b) 32 to 37 GWC, (c) 37 to 42 GWC.

# 3.2. Discussion 

According to Table 3, Age showed the highest contribution to variance (23\%), followed by Facility Type ( $1.37 \%$ ), and all other parameters were found to be less than $0.05 \%$. Being the most sensitive parameter, changes in Age have a significant effect on the final output irrespective of facility type. These results are in agreement with the expert opinion. Furthermore, the $25 \%$ variance highlighted that the sensitivity of the reliability (child node) highly depends on the variability of the parent nodes.

Four extreme conditions (Table 4) for each type of civil infrastructure were considered when all of the parent nodes were either in the worst condition or in a favorable condition. For example, clay shrinkage for roads gives the three states for Reliability, namely Low, Moderate, and High, to be 57.1, 40.2, and 2.68, respectively, under the worst condition. The corresponding values under a favorable condition were found to be $4.0,24.0$, and 72.0 , respectively. These data indicate that the reliability of roads will be low for the worst conditions and high for the favorable scenarios. A similar interpretation can be made for clay swelling under roads. Likewise, the same analyses can be performed for the other types of civil infrastructure. Once again, the proposed BBN-based model gives results according to the assumed soil behavior.

To further validate the proposed BBN-based model, more than 420 hypothetical scenarios were generated. Results indicated that the moderate conditions for swelling fell between the extreme conditions. As an example, Figure 4 shows the predicted infrastructure reliability curves due to swelling in expansive clays (based on GWC from 22 to 42). For this analysis, the age of the infrastructure is changed while keeping the states of all the other nodes in accordance with row 7 through row 12 in Table 4. The curves show that infrastructure reliability decreases in a step-wise manner based on the age bracket. Similar reliability curves can be generated for shrinkage in expansive clays.

## 4. Conclusions

This study aimed at examining the interrelationship between several contributing factors that impact the reliability of different infrastructures in expansive soils. The BBN approach was used because it can demonstrate the relationship between different factors in complex systems more effectively when compared with other multi-criteria decision analysis methods. The proposed approach of BBN-based modeling was successfully applied to determine the reliability of civil infrastructure in expansive soils. The modeling results highlighted that facility age is the most critical parameter ( $23 \%$ variance), followed by facility type ( $1.37 \%$ variance), for all the investigated types of infrastructure, namely

road embankments, buried pipelines, and residential housing. Results of the sensitivity analysis and extreme scenario analysis indicated that the method is capable of predicting infrastructure reliability, and the assessments were found to be in agreement with the expected field behavior. For example, it was found that the reliability of roads is low for the worst conditions and high for the favorable scenarios. The model can be further improved by discretizing the Age node in more than the current seven stages. This will allow for the capture of more frequent variations in infrastructure reliability. The proposed model will aid geotechnical practitioners in estimating the probabilistic reliability of different infrastructure under various scenarios. As such, the model is useful in decision making related to civil infrastructure management in expansive clays.

Author Contributions: Conceptualization, G.K. and S.A.; methodology, G.K. and S.A.; software, G.K. and S.A.; validation, G.K. and S.A; formal analysis, G.K. and S.A.; investigation, G.K. and S.A.; resources, G.K. and S.A.; data curation, G.K. and S.A.; writing-original draft preparation, G.K. and S.A.; writing-review and editing, G.K. and S.A.; visualization, G.K. and S.A.; project administration, G.K. and S.A. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.
Data Availability Statement: The data presented in this study are already published in previous studies.
Acknowledgments: The authors would like to acknowledge the University of Regina for providing the computational facilities and Maki Ito for providing the compiled field data given in Figure 1.

Conflicts of Interest: The authors declare no conflict of interest.
