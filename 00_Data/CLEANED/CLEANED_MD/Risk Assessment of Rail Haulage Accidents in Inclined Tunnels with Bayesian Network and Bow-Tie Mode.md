## Risk assessment of rail haulage accidents in inclined tunnels with Bayesian network and bow-tie model

Qingwei Xu and Kaili Xu*<br>School of Resources and Civil Engineering, Northeastern University, Shenyang 110819, China

Rail haulage system is an important part in mine production as people and materials are mainly transported through rail haulage equipment. The purpose of this communication is to establish a composite risk analysis model of rail haulage accidents in inclined tunnels based on Bayesian network and bow-tie model, which can be used to predict the risk of rail haulage accidents in mines and adopt relevant safety measures towards critical basic events. First, a simple case study of mapping fault tree into Bayesian network was introduced. Second, the risk level and critical basic events could be achieved according to forward analysis and backward analysis of Bayesian network with the help of GeNIe software. The obstacles on rails, unqualified rails and acceleration or deceleration were identified as the first category critical basic events of rail haulage accidents based on the above analysis. Third, acceleration or deceleration was chosen as the risk Bayesian node and a detailed analysis was made using bow-tie model. Twelve preventive safety measures were set on the left to prevent basic events and 10 mitigative safety measures were set on the right to mitigate accident consequences, the risk of rail haulage accidents in inclined tunnels can further be reduced by bow-tie analysis. Composite risk analysis model can be applied for similar risk analysis of rail haulage accidents.

Keywords: Bayesian network, bow-tie model, rail haulage accidents, risk assessment.

Mine production provides the necessary resources like coal, iron and ore for social development, but it also causes many accidents that leads to death ${ }^{1-3}$. Therefore, mine production safety plays an important role in protecting the rapid development of national economy ${ }^{4-6}$. Rail haulage system is one of the most important parts in mine production ${ }^{7-10}$ as people and materials are mainly transported through rail haulage equipment. Rail haulage accidents may cause serious casualties and huge loss of property ${ }^{11}$. To prevent rail haulage accidents, risk assessment should first be conducted. There have been studies on the risk assessment of mine ventilation system ${ }^{12,13}$. However, at present, there are no relevant studies on the safety assessment of rail haulage system published in English, except some simple analysis in Chinese references such as Fault Tree Analysis ${ }^{14}$. Never-

[^0]theless, there is a lack of systematized safety analysis method on rail haulage accidents. Therefore, it is important to construct a systematized safety analysis method and prevent rail haulage accidents.

There are a lot of risk assessment methods including fuzzy evaluation method ${ }^{15-18}$, gray evaluation method ${ }^{19-21}$ and analytic hierarchy process (AHP) ${ }^{22-25}$. Li et al. ${ }^{17}$ have established a fuzzy model based on fuzzy sets and information diffusion to evaluate flood risk. Liu et al. ${ }^{26}$ have set up a comprehensive assessment method that combines AHP and gray evaluation method to ensure safety in mine production. Besides, some scholars have applied game theory ${ }^{27-29}$ for risk analysis. For example, Xia et al. ${ }^{27}$ put forward an evolutionary game model to study the risk analysis of cooperation under the spatial public goods game. These methods make good performance in forward analysis, but have difficulties in backward analysis. The risk assessment of rail haulage accidents, not only requires the forward analysis, but also backward analysis. Taking the influence of top event (whether happened or not it happened) on basic events into consideration, backward analysis is studied to find the critical basic events.

Bayesian network can realize the idea of both forward and backward analysis, which is widely used in the field of risk analysis. Bayesian network has been applied for the risk analysis of water resource management ${ }^{30}$, chemical infrastructure ${ }^{31}$, urban expressway ${ }^{32}$, water pollution accident ${ }^{33,34}$ and software project ${ }^{35}$. Tang et al. ${ }^{33}$ have developed a Bayesian network including six root nodes and three middle-layer nodes, which is applied to identify the possibility of potential risk of water pollution. Weber et al. ${ }^{36}$ and Landuyt et al. ${ }^{37}$ reviewed the application of Bayesian network. Weber presented a review over the last decade on the application of Bayesian network to dependability, risk analysis and maintenance; Landuyt discussed the number of Bayesian belief network-based ecosystem service models developed over the last decade. Although Bayesian network can recognize the risk nodes of potential accidents, it cannot give prevention measures effectively unless it is equipped with other techniques such as bow-tie model ${ }^{38,39}$.

Bow-tie model is also used widely as a risk analysis tool, because it integrates basic causes, possible consequences and corresponding safety measures of an accident in a transparent diagram. Bow-tie model has been applied to risk control ${ }^{40}$, risk assessment of gas oil storage ${ }^{41}$ and chemical industry ${ }^{42}$, risk management of sea ports ${ }^{43}$ and hydrogen sulphide ${ }^{44}$, risk evaluation of gas pipelines ${ }^{45,46}$ and organizing learning process ${ }^{47}$ as well as workplace ${ }^{48}$. Chevreau et al. ${ }^{47}$ proposed a complete and efficient method to manage risk analysis through bow-tie representation. Ruijter et al. ${ }^{49}$ divided bow-ties into quantitative and qualitative bow-ties. Most quantitative bow-ties use fault tree along with event tree and barriers to calculate risk, and qualitative bow-tie uses simpler


[^0]:    *For correspondence. (e-mail: xklsafety@163.com)

cause-effective scenarios with barriers to communicate risk49. Due to its static characteristics, bow-tie method cannot be used easily in dynamic risk analysis. However, if it is combined with Bayesian network, this problem would be solved50,51.

Integrating Bayesian network and bow-tie model can not only identifies the risk nodes of accidents, but also gives prevention measures. This composite model has been applied to quantitative risk analysis of offshore drilling operation52, dust explosion scenario53, gas leakage during biomass gasification54 and process system55.

However, until now, a composite analysis model of rail haulage accidents is not available, and we wish to fill this gap. Therefore, this study aims at building a composite analysis model of rail haulage accidents in inclined tunnels with Bayesian network and bow-tie model and considers it as an extension to previous studies based on fault tree analysis14. Be different from previous studies based on fault tree analysis14, risk level of rail haulage accidents and potential results can be achieved in terms of available information in the study. Additionally, the critical basic events of rail haulage accidents can be identified and prevented by relevant safety measures based on the above application.

This communication recapitulates the fundamental theories of a composite analysis model and background of rail haulage accidents. To illustrate the applicability of the composite analysis model, a real example of rail haulage accident in an inclined tunnel is given.

Bayesian network includes network nodes, directed links, conditional probabilities of nodes and a directed acyclic graph, which reflects uncertain relationship among network nodes. This method is widely applied to some uncertain analysis. Bayesian network is based on Bayesian formula, and the probability of event A under the occurrence of event B can be expressed as

$$
P(A \mid B)=\frac{P(B \mid A) \times P(A)}{P(B)}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. A simple fault tree.
where $P(A)$ is the prior probability of event $A, P(A \mid B)$ is the posterior probability of event $A$ under the occurrence of event $B, P(B \mid A)$ is the conditional probability of event $B$ under the occurrence of event $A, P(B)$ is the prior probability of event $B ; P(A)$ is not related to event $B$ and $P(B)$ is not associates to event $A$.

If the set of event $A$ is $A=\left\{a_{1}, a_{2}, \cdots, a_{n}\right\}$, the Bayesian formula of $P(B)$ can be expressed as

$$
P(B)=\sum_{i=1}^{n} P\left(B \mid a_{i}\right) P\left(a_{i}\right)
$$

The occurrence probability of a specific accident can be derived by the prior probability of basic events with Bayesian network, and Bayesian network reflects the relationship between prior probability and posterior probability. Before quantitative analysis with Bayesian network, the risk factors of accidents should be identified according to other methods such as fault tree analysis. The nodes of Bayesian network are composed of main risk factors.

Bayesian network can be analysed with the help of GeNIe ${ }^{56}$ software, created and developed by the Decision Systems Laboratory, University of Pittsburgh. Abimbola et al. ${ }^{57}$ studied the risk analysis of managed pressure drilling operation with Bayesian network based on GeNIe software. However, very little information is available on the specific process. In this study, a case study was first introduced.

A simple fault tree is shown in Figure 1. Hypothesis of the prior probability of each basic event was $P\left(X_{i}\right)=0.1$, and then the probability of top event $P(T 1)$ could be calculated as

$$
P(T 1)=P\left(x_{1}\right)\left[1-\left(1-P\left(x_{2}\right)\right)\left(1-P\left(x_{3}\right)\right)\right]=0.019
$$

The probability of intermediate event $P\left(A_{1}\right)$ can be calculated as

$$
P\left(A_{1}\right)=1-\left(1-P\left(x_{2}\right)\right)\left(1-P\left(x_{3}\right)\right)=0.19
$$

If the top event had already taken place, at this condition of $P(T 1)=1$, the posterior probability of each basic event could be calculated according to Bayesian formula (1) as

$$
\begin{aligned}
& P\left(x_{1} \mid T 1\right)=\frac{P\left(T 1 \mid x_{1}\right) P\left(x_{1}\right)}{P(T 1)}=\frac{P\left(A_{1}\right) P\left(x_{1}\right)}{P(T 1)}=1 \\
& P\left(A_{1} \mid T 1\right)=\frac{P\left(T 1 \mid A_{1}\right) P\left(A_{1}\right)}{P(T 1)}=\frac{P\left(x_{1}\right) P\left(A_{1}\right)}{P(T 1)}=1 \\
& P\left(x_{2} \mid T 1\right)=P\left(x_{2} \mid A_{1}\right)=\frac{P\left(A_{1} \mid x_{2}\right) P\left(x_{2}\right)}{P\left(A_{1}\right)}=0.526
\end{aligned}
$$

$$
P\left(x_{3} \mid T 1\right)=P\left(x_{3} \mid A_{1}\right)=\frac{P\left(A_{1} \mid x_{3}\right) P\left(x_{3}\right)}{P\left(A_{1}\right)}=0.526
$$

Mapping the fault tree of Figure 1 into Bayesian network and analysing it using GeNle software, and the Bayesian network is shown in Figure 2.

Logic AND gate of fault tree should be transformed into Bayesian network as follows (Table 1).

Table 1. AND gate of fault tree in Bayesian network


![img-1.jpeg](img-1.jpeg)

Figure 2. Bayesian network of the case study.
![img-2.jpeg](img-2.jpeg)

Figure 3. The bar chart of case study.
![img-3.jpeg](img-3.jpeg)

Figure 4. The backward analysis of Bayesian network.

Logic OR gate of fault tree should be transformed into Bayesian network as follows (Table 2).

With the given information, the probability of leaf node could also be calculated by forward analysis in Bayesian network, the result is $P(T 1)=0.019$. The bar chart of Bayesian network is shown in Figure 3.

The actual value of occurrence probability of $P(T 1)$ is 0.019 , and the actual value will be shown when the chart is double clicked.

Bayesian network can not only perform forward analysis but also backward analysis. Meanwhile, hypothesis of the leaf node had already taken place. With the evidence of $P(T 1)=1$ and updating information, the Bayesian network can be changed into Figure 4.

According to Figure 4, the posterior probabilities of root nodes and intermediate nodes are clearly shown.

A bow-tie (Figure 5) consists of a fault tree on the left side and an event tree on the right side, and centering in it is a critical event with a certain occurrence probability. The causes of events indicate the left of the bow-tie, and consequences imply the right. The causes are basic events that may lead to accidents and the consequences are the loss (including health and treasure) due to accidents. To prevent critical accidents, safety barriers should be adopted. Preventive safety measures are set on the fault tree side and, therefore, they come before the top event; mitigative safety measures are set on the side of event tree and, therefore, they come after the top event.

Rail haulage equipment in inclined tunnels consists of tramcar, chain and a hook, which is pulled by electric

Table 2. OR gate of fault tree in Bayesian network


![img-4.jpeg](img-4.jpeg)

Figure 5. The sketch of bow-tie model.

Table 3. The symbol descriptions and occurrence probabilities of events


Table 4. Probability levels of accident occurrence ${ }^{59}$


cars or winch wire ropes in inclined tunnels. People, materials and gangues are mainly transferred through rail haulage equipment which exerts an important influence on the safety production of mines.

With modernization the depth construction of mines and mining to the usage-cycle of rail haulage in inclined tunnels will also be increased, leading to increase in rail haulage accidents in inclined tunnels. Among the accidents, the frequency of haulage vehicle accidents is higher than that of others.

The haulage vehicle accidents refer mainly to tramcars travelling fast in inclined tunnels free from wire rope traction, and the consequence will be quite serious. The people working in deeper mines will be injured if they do not escape on time. Additionally, vent lines, water pipes, cables and roadway support will also be destroyed.

The rail haulage accident in an inclined tunnel of a mine (see ref. 14 for full data) is shown in Figure 6. The symbol descriptions of Figure 6 are listed in Table 3. Simple qualitative analysis could be achieved based on Figure 6. Logic OR gate takes up $83 \%$ according to the composition of logic gates of the fault tree, which means that the occurrence probability of an accident is very high.

Transfer of the fault tree of Figure 6 into Bayesian network is shown in Figure 7.

To get the occurrence probability of rail haulage accidents in inclined tunnels, it is necessary to know the occurrence probability of each basic event in advance.

Table 5. Severity levels of accident consequences


Table 6. Risk levels of accidents


![img-5.jpeg](img-5.jpeg)

Figure 6. The fault tree of a rail haulage accident.

The prior probability of each basic event can be found in Table 3.

With updating the prior probability and the logical relationship of each basic event in Bayesian network, the occurrence probability of rail haulage accidents in inclined tunnels can be achieved by the forward analysis of Bayesian network using GeNIe software, the result is $P(T)=0.022$. The occurrence possibility of rail haulage accidents is shown in Table 4.

To get the specific risk level of rail haulage accidents, the severity levels (Table 5) should also be shown. Statistics ${ }^{58}$ indicates that rail haulage accidents in inclined
tunnels can lead to three deaths and four cases of minor injuries, indicating the severity level of rail haulage accidents to be very high.

The risk level of rail haulage accidents in inclined tunnels can reach 20 (Table 6), which combines occurrence probability and severity, and safety measures should be adopted immediately according to Table 7.

It is necessary to identify the importance of basic events to prevent rail haulage accidents in inclined tunnels. In the risk analysis of rail haulage accidents, if a certain consequence is observed, it should be considered as new information corresponding to Bayesian network to update probabilities. If the rail haulage accident had occurred under the condition of $P(T)=1$, the posterior probability of basic events is shown in Table 3.

When the top event happens, the occurrence probability of basic events $X_{1}, X_{2}, X_{3}, X_{4}, X_{5}$ and $X_{21}$ will significantly increase according to the analysis of posterior probability in Table 3 and Figure 8. Due to these probability revisions, the occurrence probabilities of rail haulage accidents and their consequences will be changed. Therefore, the most probable configuration of basic events leading to a rail haulage accident is determined by the occurrence of basic events $X_{1}, X_{2}, X_{3}, X_{4}, X_{5}$ and $X_{21}$. Therefore, in the risk management and safety assessment of rail haulage accidents, these basic events should be given priority to reduce the occurrence probability and decrease the risk.

We have studied the influence of basic event (whether it happened or not) on the occurrence probability of top events, with setting $P\left(T \mid x_{i}=1\right)$ and $P\left(T \mid x_{i}=0\right)$ respectively and the results are shown in Table 3.

Comprehensive analysis of the data in Table 3 shows that although the basic events $X_{4}, X_{5}$ and $X_{21}$ are likely to cause the top events to happen, and when each of the three basic events does not happen, the occurrence probability of the top events does not decrease significantly. While the basic events $X_{1}, X_{2}$ and $X_{3}$ do not happen respectively, the occurrence probability of top events decreases significantly.

Basic events can be divided into three categories according to the probability of occurrence and the effectiveness of prevention measures of top events. The first category includes $X_{1}, X_{2}$ and $X_{3}$, which possibly leads to top events. Moreover, when basic events do not happen, the occurrence probability of top event decreases

![img-6.jpeg](img-6.jpeg)

Figure 7. Bayesian network of the rail haulage accident in an inclined tunnel.

Table 7. Risk levels of accidents and required measures


![img-7.jpeg](img-7.jpeg)

Figure 8. The probability changes of critical basic events of rail haulage accidents. significantly. The second category includes $X_{4}, X_{5}$ and $X_{21}$ which are also likely to cause top events. However, when these basic events do not happen, the occurrence probability of top events does not decrease significantly. The third category includes the remainding basic events which are not likely to lead to the occurrence of top events. Besides, whether basic events happen or not, they do not have a great influence on the occurrence probability of top events.

The basic event of $X_{3}$ belongs to the first category according to the above analysis. It is chosen as a risk Bayesian node and makes detailed analysis with bow-tie model. The bow-tie analysis of $X_{3}$ acceleration or deceleration is shown in Figure 9.

On the left of bow-tie is fault tree analysis including five causes which can lead to acceleration or deceleration. On the right of bow-tie is event tree analysis including three results of rail haulage accidents in inclined tunnels. Twelve preventive safety measures are set on the left to prevent the occurrence of basic events, and ten mitigative safety measures are set on the right to mitigate accident consequences. Therefore, the risk of rail haulage accidents in inclined tunnels can be further reduced by bow-tie analysis.

Our results confirm that the systematized model based on Bayesian network and bow-tie analysis can be successfully applied to the risk assessment of rail haulage accidents in inclined tunnels. At the same time, the risk level of top events and critical basic events can be obtained. Besides, preventive, mitigative safety measures should also be adopted to decrease the risk of accidents. Motivated by the application of safety assessment in other fields, such as Bayesian network in risk analysis ${ }^{31}$ and bow-tie model in risk assessment ${ }^{41}$, upon which our theoretical study is based. Unlike previous research, this

![img-8.jpeg](img-8.jpeg)

Figure 9. Bow-tie analysis of acceleration or deceleration.
is the first time that a systematized model is applied to risk analysis of rail haulage accidents in inclined tunnels. Our results can be applied to similar risk analysis of rail haulage accidents. To minimize the workload of analysis, only one critical basic event was chosen as the risk Bayesian node and makes a detailed analysis with bowtie model. Other basic events should be analysed with bow-tie model in future studies to make a comprehensive risk analysis of rail haulage accidents in inclined tunnels.

In this study, a risk assessment model of rail haulage accidents in inclined tunnels is developed based on Bayesian network and bow-tie analysis. With forward and backward analyses of Bayesian network as advantages, the critical basic events that lead to rail haulage accidents in inclined tunnels are identified. These are respectively identified as obstacles on rails, unqualified rails and acceleration or deceleration. Then, the basic event acceleration or deceleration is chosen as the risk Bayesian node and makes a detailed analysis with bow-tie model, twelve preventive safety measures are set on the left to prevent
basic events and 10 mitigative safety measures are set on the right to mitigate accident consequences.

1. Chen, H. et al., Research on 10-year tendency of China coal mine accidents and the characteristics of human factors. Saf. Sci., 2012, 50, 745-750.
2. Cao, Q. G. et al., Risk management and workers safety behavior control in coal mine. Saf. Sci., 2012, 50, 903-913.
3. Yu, H. M. and Chen, H., Production output pressure and coal mine fatality seasonal variations in China, 2002-2011. J. Saf. Res., 2013, 47, 39-46.
4. Wei, C. F., Pei, Z. and Li, H. M., An induced OWA operator in coal mine safety evaluation. J. Comput. Syst. Sci., 2012, 78, 9971005 .
5. Chen, S. S., Xu, J. H. and Fan, Y., Evaluating the effect of coal mine safety supervision system policy in China's coal mining industry: a two-phase analysis. Resour. Policy, 2015, 46, 12-21.
6. Liu, J. H. and Song, X. Y., Countermeasures of mine safety management based on behavior safety mode. Proc. Eng., 2014, 84, $144-150$.
7. Wang, S. Y. and Zuo, H. Y., Safety diagnosis on coal mine production system based on fuzzy logic inference. J. Cent. South Univ., 2012, 19, 477-481.

8. Adenso-Diaz, B., Lev, B. and Artime, R., Simulation in dynamic environments: optimization of transportation inside a coal mine. IIE Trans., 2004, 36, 547-555.
9. Roumpos, C. et al., The optimal location of the distribution point of the belt conveyor system in continuous surface mining operations. Simul. Model. Pract. Theory, 2014, 47, 19-27.
10. Greberg, J. et al., Alternative process flow for underground mining operations: analysis of conceptual transport methods using discrete event simulation. Minerals, 2016, 65, 1-14.
11. Feng, X. L. et al., Wireless mobile monitoring system for tram rail transport in underground coal mine based on WMN. International Conference on Computational Aspects of Social Networks, 2010.
12. Shen, F. M., Chen, B. H. and Yang, J., Study on construction and quantification of evaluation index system of mine ventilation system. Proc. Earth Planet. Sci., 2009, 1, 114-122.
13. Xu, G. et al., Effective utilization of tracer gas in characterization of underground mine ventilation networks. Proc. Saf. Environ. Protect., 2016, 99, 1-10.
14. Jing, G. X., Feng, C. G. and Du, W., System safety analysis on rail haulage accident in inclined tunnel. China Saf. Sci. J., 2000, 3, 23-27 (in Chinese).
15. Niknejad, A. and Petrovic, D., A fuzzy dynamic Inoperability Input-output Model for strategic risk management in global production networks. Int. J. Product. Econ., 2016, 179, 44-58.
16. Liu, Y. L. et al., The assessment of traffic accident risk based on grey relational analysis and fuzzy comprehensive evaluation method. Nat. Hazards, 2017, 88, 1409-1422.
17. Li, Q. et al., Research on flood risk analysis and evaluation method based on variable fuzzy sets and information diffusion. Saf. Sci., 2012, 50, 1275-1283.
18. Chu, H. D. et al., Risk assessment of water inrush in karst tunnels based on two-class fuzzy comprehensive evaluation method. Arab. J. Geosci., 2017, 179, 1-12.
19. Li, H. et al., Risk Assessment of China's overseas oil refining investment using a fuzzy-grey comprehensive evaluation method. Sustainability, 2017, 696, 1-18.
20. Zheng, G. Z. et al., Multihierarchical gray evaluation method to assess building energy conservation. J. Energy Eng., 2011, 2, 88-98.
21. Zhi, Y. L., Wang, H. M. and Liu, G., Study of fuzzy evaluation method on ecological civilization construction based on grey interval number. Int. J. U- and E-service, Sci. Technol., 2015, 2, $263-280$.
22. Li, L., Liu, F. and Li, C. B., Customer satisfaction evaluation method for customized product development using entropy weight and analytic hierarchy process. Comput. Ind. Eng., 2014, 77, 80-87.
23. Chen, T. et al., A hybrid fuzzy evaluation method for safety assessment of food-waste feed based on entropy and the analytic hierarchy process methods. Exp. Syst. Appl., 2014, 41, 7328-7337.
24. Tan, X. D. et al., Evaluation of the effect of a health education campaign of HIV by using an analytical hierarchy process method. Int. J. Environ. Res. Public Health, 2007, 3, 254-259.
25. Sun, H. Y., Wang, S. F. and Hao, X. M., An improved analytic hierarchy process method for the evaluation of agricultural water management in irrigation districts of north China. Agric. Water Manag., 2017, 179, 324-337.
26. Liu, Y. J. et al., Study of a comprehensive assessment method for coal mine safety based on a hierarchical grey analysis. J. China Univ. Min. Technol., 2007, 1, 6-10.
27. Xia, C. Y. et al., Risk analysis and enhancement of cooperation yielded by the individual reputation in the spatial public goods game. IEEE Syst. J., 2017, 3, 1516-1525.
28. Wang, J. et al., Utility evaluation based on one-to-N mapping in the Prisoner's dilemma game for interdependent networks. PLoS ONE, 2016, 12, 1-14.
29. Chen, M. H. et al., Evolution of cooperation in the spatial public goods game with adaptive reputation assortment. Phys. Lett. A, 2016, 380, 40-47.
30. Varouchakis, E. A., Palogos, I. and Karatzas, G. P., Application of Bayesian and cost benefit risk analysis in water resources management. J. Hydrol., 2016, 534, 390-396.
31. Khakzad, N., Application of dynamic Bayesian network to risk analysis of domino effects in chemical infrastructures. Reliab. Eng. Syst. Saf., 2015, 138, 263-272.
32. Yu, R. J. et al., Crash risk analysis for Shanghai urban expressways: a Bayesian semi-parametric modeling approach. Acci. Anal. Prevent., 2016, 95, 495-502.
33. Tang, C. H. et al., Risk analysis of emergent water pollution accidents based on a Bayesian Network. J. Environ. Manage., 2016, 165, 199-205.
34. Farmani, R., Henriksen, H. J. and Savic, D., An evolutionary Bayesian belief network methodology for optimum management of groundwater contamination. Environ. Model. Software, 2009, 3, 303-310.
35. Hu, Y. et al., Software project risk analysis using Bayesian networks with causality constraints. Decis. Support Syst., 2013, 56, 439-449.
36. Weber, P. et al., Overview on Bayesian networks applications for dependability, risk analysis and maintenance areas. Eng. Appl. Artif. Intell., 2012, 4, 671-682.
37. Landuyt, D. et al., A review of Bayesian belief networks in ecosystem service modelling. Environ. Model. Software, 2013, 46, 1-11.
38. Badreddine, A. and Amor, N. B., A Bayesian approach to construct bow tie diagrams for risk evaluation. Process Saf. Environ. Prot., 2013, 91, 159-171.
39. Khakzad, N., Khan, F. and Amyotte, P., Dynamic safety analysis of process systems by mapping bow-tie into Bayesian network. Process Saf. Environ. Prot., 2013, 91, 46-53.
40. Dianous, V. D. and Fiévez, C., A more explicit demonstration of risk control through the use of bow-tie diagrams and the evaluation of safety barrier performance. J. Hazard. Mater., 2006, 3, 220-233.
41. Thienen-Visser, K. V. et al., Bow-tie risk assessment combining causes and effects applied to gas oil storage in an abandoned salt cavern. Eng. Geol., 2014, 168, 149-166.
42. Aqlan, F. and Ali, E. M., Integrating lean principles and fuzzy bow-tie analysis for risk assessment in chemical industry. J. Loss Prevent. Process Ind., 2014, 29, 39-48.
43. Mokhtari, K. et al., Application of a generic bow-tie based risk analysis framework on risk management of sea ports and offshore terminals. J. Hazard. Mater., 2011, 2, 465-475.
44. Yazdi, M., The Application of bow-tie method in hydrogen sulfide risk management using layer of protection analysis (LOPA). J. Failure Prevent., 2017, 2, 291-303.
45. Lu, L. L. et al., A comprehensive risk evaluation method for natural gas pipelines by combining a risk matrix with a bow-tie model. J. Nat. Gas Sci. Eng., 2015, 25, 124-133.
46. Anjuman, S., Rehan, S. and Tesfamariam, S., Risk analysis for oil and gas pipelines: a sustainability assessment approach using fuzzy based bow-tie analysis. J. Loss Prevent. Process Ind., 2012, 3, 505-523.
47. Chevreau, F. R., Wybo, J. L. and Cauchois, D., Organizing learning processes on risks by using the bow-tie representation. J. Hazard. Mater., 2006, 3, 276-283.
48. Targoutzidis, A., Incorporating human factors into a simplified 'bow-tie' approach for workplace risk assessment. Saf. Sci., 2010, 2, 145-156.
49. Ruijter, A. D. and Guldenmund, F., The bowtie method: a review. Saf. Sci., 2016, 88, 211-218.
50. Shan, X., Liu, K. and Sun, P. L., Risk analysis on leakage failure of natural gas pipelines by fuzzy Bayesian network with a bow-tie model. Sci. Program., 2017, 2017, 1-11.
51. Bilal, Z., Mohammed, K. and Brahim, H., Bayesian network and bow tie to analyse the risk of fire and explosion of pipelines. Process Saf. Prog., 2017, 2, 202-212.

52. Khakzad, N., Khan, F. and Amyotte, P., Quantitative risk analysis of offshore drilling operations: a Bayesian approach. Saf. Sci., 2013, 57, 108-117.
53. Yuan, Z. et al., Risk analysis of dust explosion scenarios using Bayesian networks. Risk Anal., 2015, 2, 278-291.
54. Yan, F. et al., Fuzzy Bayesian network-bow-tie analysis of gas leakage during biomass gasification. PLoS ONE, 2016, 7, 1-21.
55. Khakzad, N., Khan, F. and Amyotte, P., Dynamic safety analysis of process systems by mapping bow-tie into Bayesian network. Process Saf. Environ. Protect., 2013, 91, 46-53.
56. GeNie, Decision Systems Laboratory, University of Pittsburg.
57. Abimbola, M. et al., Safety and risk analysis of managed pressure drilling operation using Bayesian network. Saf. Sci., 2015, 76, $133-144$.
58. State Administration of Work Safety, available at http://media. chinasafety.gov.cn:8090/iSystem/shigumain.jsp (accessed on 10 August 2017)
59. CCPS, Layers of protection analysis-simplified process risk assessment. New York: American Institute of Chemical Engineers, Center for Chemical Process Safety, 2001.

ACKNOWLEDGEMENTS. The work was partly supported by The National Key Research and Development Program of China (2017YFC0805100).

Received 16 August 2017; revised accepted 14 December 2017
doi: $10.18520 / \mathrm{cs} / \mathrm{v} 114 / \mathrm{i} 12 / 2530-2538$

## Exclusion of putative CATSPER2 and STRC gene deletion and FOXI1 gene mutations in a unique cohort with sensorineural deafness and male infertility from south India

Justin Margret Jeffrey ${ }^{1}$, Jayasankaran Chandru ${ }^{1}$, Amritkumar Pavithra ${ }^{1,3}$, Murugesan Kalaimathi ${ }^{1}$, Nagarathinam Indhumathi ${ }^{2}$, Pangadan Ashraf ${ }^{1}$ and C. R. Srikumari Srisailapathy ${ }^{1, *}$<br>${ }^{1}$ Department of Genetics, Dr. ALM Post Graduate Institute of Basic Medical Sciences, University of Madras, Taramani Campus, Chennai 600 113, India<br>${ }^{2}$ Department of Medical Genetics, Apollo Hospitals, Chennai 600 006, India<br>${ }^{3}$ Present address: Post Graduate and Research Department of Biotechnology, Women's Christian College, College Road, Chennai 600 006, India

Prelingual genetic deafness and male infertility can appear as isolated findings or as part of a syndrome. Deafness-Infertility Syndrome (DIS) was previously reported to be caused due to a rare contiguous gene

[^0]deletion of CATSPER2 and STRC genes on chromosome 15q15.3. We tested this contiguous gene deletion in a unique cohort of 15 probands with deafness and male infertility, who were partners in assortative mating from south India. Screening for this alleged contiguous gene deletion did not test positive. Given high parental consanguinity, it is possible that infertility and deafness may not be part of a contiguous gene deletion, but two independent events. As a next option we screened another candidate gene FOXI1 (5q35.1), known to independently influence sperm maturation and also encode transcriptional factor of a deafness gene SLC26A4, to implicate for this DIS phenotype. However none of the probands had any pathogenic mutations in FOXI1 gene. Having excluded (i) DIS contiguous gene deletion and (ii) FOXI1 gene mutations' role in this phenotype, we conclude that this unique cohort's genetic etiology can be resolved using high-throughput NGS and CNV assessment. This approach may also identify potential linkage to any novel genes.

Keywords: Assortative mating, contiguous gene deletion, CATSPER2, STRC, p.I35S.

DEAFNESS may occur by itself as an isolated phenotype or as a part of a syndrome in which the hearing loss is associated with other medical conditions. One such autosomal recessive syndrome is sensorineural deafness with male infertility (DIS) which is due to a contiguous gene deletion of the CATSPER2 and STRC genes on chromosome 15q15.3 (ref. 1). Cation Channel Sperm Associated 2 (CATSPER2) encodes calcium channels required for hyperactive motility of the sperm tail to push through the egg cell ${ }^{2,3}$. Adjoining CATSPER2 is the stereocilin (STRC) gene, expressed in the stereocilia of the outer hair cells of the inner ear, involved in mechanoreception of sound waves ${ }^{4}$. Hence when the deletion is present both deafness and anomaly in morphology and motility of the sperm exist in males; whereas females with this deletion have only hearing loss but are fertile ${ }^{5}$. Similarly, FOXI1 (Forkhead box I1) has a functional role in hearing, fertility and male acidosis. It is a potential transcriptional activator of an auditory gene SLC26A4 (ref. 6) which also has a role in epididymal expression that is required for male fertility. Mutations in FOXI1 gene (5q35.1) cause sensorineural deafness syndrome with distal renal tubular acidosis and male infertility ${ }^{7}$.

So we tested for this contiguous gene deletion in a unique cohort of assortatively mating families, where the male partners have both sensorineural deafness and infertility as a phenotype. Furthermore we improvised the approach by adding another candidate gene FOXI1 which has not been concurrently screened in DIS probands. So far this gene has only been screened in prelingual deaf without infertility, although FOXI1 has a role in sperm maturation. So this adds to the novelty of the study design.


[^0]:    *For correspondence. (e-mail: crsrikumari.hhl@gmail.com)