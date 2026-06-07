# HIAL open science 

## Customer's behavior modeling for manufacturing planning

Sotiris Makris, George Chryssolouris

## To cite this version:

Sotiris Makris, George Chryssolouris. Customer's behavior modeling for manufacturing planning. International Journal of Computer Integrated Manufacturing, 2010, 23 (07), pp.619-629. 10.1080/09511921003793809 . hal-00608405

## HAL Id: hal-00608405 <br> https://hal.science/hal-00608405v1

Submitted on 13 Jul 2011

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

International Journal of Computer Integrated Manufacturing

![img-0.jpeg](img-0.jpeg)

Customer's behavior modeling for manufacturing planning


scholarone Manuscript Central

URL: http://mc.manuscriptcentral.com/tandf/tcim Email:ijcim@bath.ac.uk

# Customer's behavior modeling for manufacturing planning 

S. Makris ${ }^{1}$, G. Chryssolouris ${ }^{1 *}$<br>${ }^{1}$ Laboratory for Manufacturing Systems and Automation, Department of Mechanical Engineering and Aeronautics, University of Patras, 26500 Rio, Patras, Greece.<br>Tel.: +30 2610 997262, Fax: +30 2610997744


#### Abstract

This paper deals with a customer driven manufacturing planning approach. Manufacturers have adopted modern communication technologies for the information flow related to customers' orders. However, there is still high uncertainty in the information provided. This work introduces a model for estimating the probability that once a customer has received a potential delivery date for a product, whether he will actually place the order. In this instance the manufacturing resources should be committed to this order. The Bayesian networks method is adopted and an automotive industrial case study is discussed.


Keywords: PROBABILISTIC MODELS, MASS CUSTOMIZATION, DECISION SUPPORT SYSTEMS

## Introduction

This work discusses a method of evaluating the probability that a customer, under a certain delivery time and price and given a set of factors, submits an order for a product. This is based on the Bayesian networks method (Schay2007) and is applied to the automotive industry. With appropriate modification, the method is applicable to industry in general.

The automotive industry for a long time has been following the "push" model; build products, based on one or more forecasts and eventually creating stocks of these products. The dealers' role was important since they were obliged to acquire a minimum quantity of the vehicles produced, and therefore, push the product to the market. The customer's element was actually not the driving factor in the automotive production. The automotive industry is turning from the "push" model to a customer driven model, which necessitates that a method be developed to quantify the customers' likely responses to what the automotive is offering (Michalos et al 2010).

[^0]
[^0]:    *xrisol@lms.mech.upatras.gr (Corresponding author)

Today's research on mass customization (Mourtzis et al. 2008, Chryssolouris et al 2008) does consider the fluctuating demand. This fluctuating demand is based on assumptions and forecasts the production of many products' variants apparently without meeting the customers' real needs. Involving the customer in the manufacturing process is more than just forecasting his possible preferences, but it actually calls for his precise requirements to be met. In the mass customization approach, which aims to simultaneously target scores of individual customers by offering them product variations, tailored specifically to fit their individual needs, understanding customer behaviour under growing market stratification conditions is critical (Pasek et. al. 2008). A growing interest over the past decade in the mass customization approach underscores the importance of the individual consumer choices, in terms of both their structure and parameters (Tseng and Piller 2003).

There is a risk involved in the order promising process and the method proposed in this paper, has been developed in order to face it. This risk is caused by the fact that a dealer provides the customer with a due date for his order. As soon as a due date is given to the customer, the production plant needs to be in position to accomplish the order in this date. Therefore, when planning the resources usage for a period of time, it is necessary to know, if this order should be considered or not. Consequently, it is essential to have an estimation of what the possibility will be as to whether the customer will actually place the order or he will withdraw it. In the case of his withdrawing the order, the planning should be adjusted. So, a more accurate estimation of a customer's likely decision, will be an important aid for the preparation of a more accurate plan for the production that will be subject to a minimum amount of changes.

In order for this risk to be eliminated, the paper discusses a method of quantifying the likelihood that a customer will actually place his order and therefore, help the production planner

to establish a more accurate plan. A typical case, in which such resource locking situation occurs, is that of the automotive when a customer, at dealership, asks for a delivery date that would eventually lead to locking the plants and supply chain's resources in order for the delivery date to be considered rather robust.
[Insert table 1 about here]

The above are demonstrated in the example of Table 1, where two customers are competing for the same delivery date, however, Customer B withdraws his order since he thinks that the delivery date D2 offered to him is late. On the other hand, Customer A gets an early delivery date D1, however, for some reason such as a more competitive priced vehicle offered by a competing brand in the same time frame, he withdraws too. The method discussed in this paper aims to address the quantification of each of the customer's likelihood to submit or withdraw his order and assist in the process of providing a suitable delivery date that will increase the sale probability. The paper addresses the uncertainty for order submission utilizing the Bayesian networks approach. Production research has adopted a number of models for dealing with the uncertainty in manufacturing.

The majority of the research effort addresses the issues of the information flow and the coordination of manufacturing resources across the production networks. The internet based communication technology can be adjusted to the needs of the customer driven manufacturing (Poirier and Bauer 2001, Wiendahl and Lutz 2002, Chryssolouris el al. 2003, Mourtzis el al. 2008, Makris et al. 2008). In a research that evaluated similar problems to the current paper, Tolio and Urgo have discussed the problem of production planning approaches that are

considering the availability of complete information and usually fail to deal with real manufacturing environments, characterized by uncertainty affecting the time that the manufacturing operations are executed, the routing of the parts, the requirement of materials and the resources. Their research analysed the issue of negotiation and planning of external resource usage, in a manufacturing system, affected by uncertainty. In particular, the need of resources is considered uncertain and it is modelled through a scenario based formulation (Tolio and Urgo. 2007).

A probabilistic model for decision makers dealing with the uncertainty of equipment selection process (Manassero, Semeraro, Tolio 2004) has been developed and verified in automotive manufacturing, ranking a set of alternative and assigning a probability that the ranking remains stable even in case of uncertainty in assumptions. In addition, a genetic algorithm based dynamic scheduler and a distributed, agent-based shop floor control system have been implemented aiming at systems which can handle critical complexity, reactivity, disturbance and optimality issues at the same time (Monostori, Kádár and Hornyák 2007). Monostori discussed the process of applying to manufacturing, pattern recognition techniques, expert systems, artificial neural networks, fuzzy systems and hybrid artificial intelligence (AI) techniques. In addition, hybrid AI and multi-strategy machine learning approaches were discussed. Agent-based (holonic) systems were highlighted as promising tools for managing complexity, changes and disturbances in production systems. The additional integration of more traditional AI and ML techniques, with the agent-based approach in the field of intelligent machines, can be predicted resulting in systems with emergent behaviour (Monostori, 2003).

In the literature, customer behaviour modelling has been discussed for identifying the way that the wealth of data in databases can be used for the evaluation of customers'

preferences. According to Bounsaythip and Runsala's report, the current methods of estimating a customer's behaviour, are based on building their databases with a significant amount of data, in order for them adapt to the needs of each customer. Methods such as Neural networks, KMeans clustering, Self organising maps, decision trees have been proposed in the literature for performing data mining and data clustering for customer profiling (Bounsaythip and Runsala, 2001). Song et al. have developed a methodology that detects changes of customer behaviour automatically from the customer profiles and the data of sales at different time snapshots (Song et. al. 2001). Pasek et al., attempted to quantify the way that the combined effects of individual decision making, under abundant choice conditions, impact the model defining optimal variety on the firm's level, in an effort to integrate the information flow between the product design and marketing (Pasek et. al. 2009). Kwan et. al., developed constructs for measuring the online movement of e-customers, and used a mental cognitive model to identify the four important dimensions of the e-customer behaviour, abstracted their behavioural changes by developing a three-phase e-customer behavioural graph, and tested the instrument via a prototype that used an online analytical mining (OLAM) methodology. A prototype with an empirical Web server log file wasused for verifying the feasibility of the methodology (Kwan et. al., 2005).

All the methods mentioned above, are actually performing customer segmentation and profiling, based on a wealth of data with reference to the customer. The method proposed in the current paper, needs to evaluate a customer, without having his historical data. The added value of the method is to utilize knowledge of the domain's specialist and to introduce the critical factors that make a model quantify the buyer's likely decision. The specialist's knowledge comprises the specific factors that influence the customer's decision as well as the weight of

each factor on the total decision. The Bayesian network proposed models these factors and assigns conditional probabilities for modelling the importance of each factor.

The factors influencing the customer's behavior are discussed in section 2 and the Bayesian networks' model is developed according to these factors. The use of this method is demonstrated in a typical automotive industrial case study.

# Model analysis 

## Law of total probability and Bayes theorem

This work is based on two basic mathematical principles which are outlined below, the Law of Total Probabilities as well as the Bayes' theorem.

According to the Law of total Probabilities, the probability of an incident $\mathrm{A}_{1}$ is the sum of the probability of every incident $B_{n}$, multiplied with the probability of the incident $A$ given the $\mathrm{B}_{\mathrm{n}}$ (Everitt 2006, Schay 2007).

$$
P\left(A_{1}\right)=\left[P\left(A_{1} \mid B_{1}\right) * P\left(B_{1}\right)\right]+\left[P\left(A_{1} \mid B_{2}\right) * P\left(B_{2}\right)\right]+\ldots . .+\left[P\left(A_{1} \mid B_{n}\right) * P\left(B_{n}\right)\right]
$$

Alternatively it can be expressed as:

$$
P\left(A_{1}\right)=\sum\left[P\left(A_{1} \mid B_{n}\right) * P\left(B_{n}\right)\right]
$$

It is possible to combine incidents and represent them graphically, by constructing a belief network, a typical example of which is shown in Figure 1.

The Bayes' theorem relates the conditional and marginal probabilities of stochastic events A and B (Everitt 2006, Schay 2007).

$$
P(A \mid B)=[P(B \mid A) * P(A)] / P(B)
$$

The terms in the Bayes' theorem have the following conventional meaning:

- $\mathrm{P}(\mathrm{A})$ is the "prior" probability of A . It is "prior" in the sense that it does not take into account any information about B .
- $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$ is the conditional probability of A , given B . It is also called the posterior probability because it derives from or depends upon the specified value of B .
- $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$ is the conditional probability of B given A .
- $\mathrm{P}(\mathrm{B})$ is the prior or marginal probability of B , and acts as a normalizing constant.

This paper discusses a set of factors for modelling a customer's likely decision about submitting an order for a highly customised product or not. These factors can be used for quantifying the customer's decision. The paper demonstrates the means of possibly utilising the Bayesian networks method in order for these factors to be modelled.

# Bayesian network for calculation of probability 

A factor identified to be having an impact on the probability of sale, in the context of this work and case study, is the vehicle's driving quality. This relationship is depicted by the Bayesian network in Figure 1. The factor GoodDrive models the quality of drive and has three potential states, Excellent, Moderate and Adequate. Similarly, the probability of sale is modeled by the node ProbabilityofSale and has three potential states: High, Medium and Low.
[Insert Figure 1 about here]

According to the Bayesian networks' principles, to calculate the state of the ProbabilityofSale, with the highest probability to occur, it is necessary that the Conditional Probabilities Table, seen in Figure 2, to be defined. This table defines the probability of the state High occuring as soon as the state Excellent, Moderate, Adequate occur in the node GoodDrive. The table has a size of $3 \times 3$, that is three factors from the node GoodDrive and three from the

node ProbabilityofSale. Filling in this table is done either manually by experts or by utilizing historical data (Rabiner 1989).
[Insert Figure 2 about here]

This paper has defined nineteen factors that influence a customer's decision to proceed with submitting his order. The factors are discussed later in section "Modelling the customer's likely decision". However, in case that a second factor, such as the CompetitivePrice factor is modeled with the previous approach, then the Bayesian network of Figure 3 is obtained.
[Insert Figure 3 about here]

To evaluate the impact of both factors, the GoodDrive and the CompetitivePrice factors on the ProbabilityofSale, it is necessary that the CPT be filled in as shown in Figure 4. The table size has grown dramatically to be $3 \times 3 \times 3=27$, combining all three potential states of the three nodes.
[Insert Figure 4 about here]

The size of the CPT depends on the number of states (s), the number of parents (p), and the number of parent states $\left(s_{p}\right)$ in the following way (Gerssen and Rothkrantz 2006):

$$
\operatorname{size}(\mathrm{CPT})=\mathrm{s} \times\left(\mathrm{s}_{\mathrm{p}}\right)^{\mathrm{p}}(4)
$$

For every possible combination of parent states, there is an entry listed in the CPT. Therefore, for a large number of parents the CPT will expand drastically. In real life cases, as the one examined in this paper, the model has nineteen parent nodes influencing the node

ProbabilityofSale the size of the CPT would be: $\operatorname{size}(C P T)=s \times\left(s_{p}\right)^{n}=3 \times 3^{19}=3.486 .784 .401$. It is obviously impractical to fill in a CPT that requires this number of entries, therefore, an alternative way of approaching it is necessary.

# Reverse Bayesian network for calculation of probability of sale 

This work suggests the reverse process for conducting Bayesian inference. A simple example is discussed to clarify the use of the Law of total probabilities and the Bayes' theorem in this work.

In the following Bayesian network, the impact of ProbabilityofSale to the GoodDrive node is examined as shown in Figure 5. It is assumed that the probability that a customer will buy a vehicle is known. Therefore, the most likely state to occur from the ProbabilityofSale node is known. In addition, it is known that high probability of sale is most likely when the drive quality of the vehicle is also high. This is modeled by the conditional probabilities table that relates the ProbabilityofSale with GoodDrive potential states and is shown in Figure 6. Then, with the use of the Law of total probability, it is possible for the probabilities of the GoodDrive states to be calculated.
[Insert Figure 5 about here]
[Insert Figure 6 about here]

$$
\begin{gathered}
\mathrm{P}(\text { Excellent })=\mathrm{P}(\text { Excellent|High }) * \mathrm{P}(\text { High })+\mathrm{P}(\text { Excellent|Medium }) * \mathrm{P}(\text { Medium })]+ \\
\mathrm{P}(\text { Excellent|Adequate }) * \mathrm{P}(\text { Adequate })
\end{gathered}
$$

Substituting the probabilities, we obtain:

$$
\mathrm{P}(\text { Excellent })=0,95791 * 1+0,04039 * 0,00+10^{-20} * 0,00=0,95791 \text { that is } 95,791 \% \rightarrow 96 \% \text {. }
$$

Therefore, given that the probability of sale is high, the customer would prefer a car that offers Excellent drive by $96 \%$. This is a result that follows also common sense.

Based on the above, it is possible to reverse the inference logic by considering the Bayes theorem and utilizing the prior probability that a customer will be having particular preferences about the vehicle's drive quality. This is represented by the GoodDrive node, and then the likelihood that a state of the ProbabilityofSale node will occur will be calculated.
[Insert Figure 7 about here]

This is demonstrated by the example in Figure 7, by applying the Bayes Theorem, it is possible for the node ProbabilityofSale from the node GoodDrive to be derived.

$$
P(\text { High } \mid \text { Excellent })=
$$

$$
P(\text { Excellent } \mid \text { High }) \cdot P(\text { High })
$$

$$
\begin{aligned} & \(0,95791 * 0,33 \quad 0,95791 * 0,33+0,04039 * 0,33+0,019 * 10^{-20}=0,959 \rightarrow 96 \% \\ &\)\hline\end{aligned}
$$

Thus, it is feasible to reverse the probabilities calculation method by the adoption of the Bayes theorem. This reversing approach is very important since it can be utilized to quantify the ProbabilityofSale, based on a number of other factors by first structuring a Bayesian network of factors having been influenced by the ProbabilityofSale and then by reversing the calculation as shown above, the ProbabilityofSale is finally calculated.

The benefit of this reverse process is that we can calculate the ProbabilityofSale node by filling in a 3x3 CPT for the link of the ProbabilityofSale with the node GoodDrive. For every additional link that is added to the Bayesian network, following this reverse approach, a single CPT $3 \times 3$ in size has to be filled in; it is therefore a manageable task. This approach will be generalized in the following section and will be demonstrated in the form of a realistic model.

# Industrial case study 

This section demonstrates the application of the reverse decision making method in an automotive industry case. Initially, the most important factors that influence a customer's decision are outlined and afterwards they are modeled with the help of the Bayesian networks method.

## Modelling the customer's likely decision

The major factors that influence a customer's decision to place a vehicle order have been identified and analyzed after industry experts have been interviewed. These factors are presented shortly as follows:
[Insert table 2 about here]
These factors have been modelled as nodes in a Bayesian network. Each factor has three potential states that evaluate the customer's perception of the factor. For example, the factor NeedTheVehicleEarly, has three potential states:

- No requirements, if the customer has no special requirements about the time he receives the vehicle,
- Insignificant requirements, if he has some preference but of minor urgency,
- Specific requirements, if he has strict time requirements, e.g. he needs the vehicle as soon as possible for a family trip and his old car has broken down.

All the factors have been modeled in the same way and in three potential states. This model is represented in the following table.
[Insert table 3 about here]

The Bayesian network that links each of these factors with the customer's likely decision is shown in Figure 8.

[Insert Figure 8 about here]

In terms of the Bayesian networks, linking two nodes, e.g. the node GoodDrive with the node CustomersDecision, requires that the CPT be filled in. The CPT of the specific relation is seen in Figure 9.

# Conditional probabilities tables' modeling 

Filling in the CPTs can be done by the following options:

- An expert fills in the table based on his experience.
- Use past data to teach the network to adopt one of the methods found in the literature
- Use equations to link the two nodes and generate the CPT data.

In this particular paper a method that utilizes the expert knowledge and the use of
equations has been adopted. In particular, a normal distribution has been used to generate the CPT data for each condition of node CustomersDecision the value node GoodDrive would have a likelihood around a mean value with a standard deviation. In each state of the node GoodDrive a value has been allocated as follows:

- State Excellent has the value of 10,
- State Moderate has the value of 5,
- State Adequate has the value of 0 .

In this case, the probability of sale is affected by the quality of drive as follows:

- The probability of sale would be more likely if the drive quality was Excellent,
- the probability of sale would be less likely if the drive quality was Moderate,
- the probability of sale would be very low if the drive quality was Adequate.

The above have been modeled by having adopted a Normal Distribution linking that of the CustomersDecision with the factor DriveQuality, as follows. If the node CustomersDecision is a Yes then, the node GoodDrive will have a value of 10 with a standard deviation of 2; actually, this means that achieving a Yes decision is more likely provided that the GoodDrive

node is Excellent since Excellent is mapped to a value of 10. In a similar way, a CustomersDecision case where both state Yes and No have the same probability linked to a value of 5 of the factor GoodDrive with a standard deviation of 2; a Low probability of sale is linked to a value of 0 of the factor GoodDrive with a standard deviation of 1.

The CPTs that are generated from the above mentioned distributions for the specific link, between the CustomersDecision and GoodDrive, can be seen in Figure 9. Reading this table, in 59,9 \% of the cases that a CustomersDecision was Yes, the GoodDrive value node would be Excellent.

From the above, it occurs that a $2 \times 3$ CPT should be built for linking each CustomersDecision node with each individual node. Therefore, it is necessary that nineteen CPTs, $2 \times 3$ in size be filled which is rather manageable compared with the case that a CPT, 3.486.784.401 in size should be filled in, as shown in section " Bayesian network for calculation of probability".
[Insert Figure 9 about here]

# Web application software implementation 

The Bayesian network model has been built with the use of the Netica ${ }^{\circledR}$ commercial software package (Norsys 2009). Netica was chosen because it offered a Java API rich enough to allow the programming of the Bayesian network in the form of a web application.

A web application was developed in order for end users to be assisted at manipulating the model in a user friendly way. A screenshot of the Bayesian inference web application can be seen in Figure 10. The end user being typically a dealer, at the dealership, is entering his assessment about the customer, based on the factors that were defined in Table 2.

[Insert Figure 10 about here]
The application follows the 3-Tier paradigm and consists of the following layers as seen in Figure 11:

- the Graphical user interface layer that is built with the use of the Java Server Pages-JSP (SUN-JSP 2009),
- the business logic layer that is written in Java and is accessed by the user via the JSP pages,
- the data repository in this application, is a set of plain text files that stores the Bayesian inference data, the CPTs, the nodes, the states and the result of the Bayesian inference
[Insert Figure 11 about here]

The outcome of the inference can be seen in Figure 12. According to this evaluation, the customer will most likely place his order, $56,7 \%$, however, there is another $43,3 \%$ that he will not be placing his order; the assessment in this case, is rather positive. The result of the evaluation is a relative measure and can be used for comparing alternative assessments that are performed for a customer. This means that the model evaluates a value per node in the Bayesian network. Each value of each node, corresponds to a potential scenario; for example, a potential value "Fully" in the node "ComplyToTimeRequirements" reflects a scenario that a vehicle is promised to be delivered to the customer early enough to address his time requirements. In this case, it is likely that the state Yes of the CustomersDecision node would be let's say 90\%, In a similar way, a different delivery date could be promised to the customer being later than his requested delivery date. In this case, the node "ComplyToTimeRequirements" would be set to "NoComply". In this case, the state Yes of the CustomersDecision node would probably be lower than in the previous case, let's say $50 \%$. Therefore, the states of the node CustomersDecision can be used as a measure for comparing different sets of values in each node of the Bayesian network. In case that a customer receives an evaluation of $50 \%$ for a set of

factors and for another, the same customer receives a $90 \%$, then the $90 \%$ is better and more preferable since it increases the probability for the customer to buy the product. Therefore, the model actually quantifies the impact of the change of delivery date.
[Insert Figure 12 about here]

# Discussion 

Currently, there is a high uncertainty whether a customer will place an order for a vehicle under a certain delivery date and cost conditions. The method that was previously analyzed can be used for quantifying the likelihood that customers will place an order. This likelihood can then be used in order for the customer to be offered a vehicle earlier, in case that his time requirements were not addressed and his likely behavior would be not to place the order. In this case though, the supply chain will need to react much faster in order to supply the necessary material necessary for the customer's order, by imposing a cost of customization (Mourtzis et al. 2008). However, this cost is balanced by the fact that the vehicle is produced for a final customer and not for a dealer thus, it is sold at the best possible price. On the other hand, if the probability for a customer to place an order is rather high, then a vehicle that is produced a bit later, based on the normal scheduling procedure, will be chosen and no additional customization activities are necessary.

## Conclusions

This paper described a method of evaluating a customer's likely response, under a specific delivery time and requesting a highly customised product. The paper discussed the impact of such a customer's behavioural evaluation on the manufacturing planning and the importance of having a method for quantifying the customer's likely decision as to whether to submit an order

or not. The method demonstrated the integration of the Bayesian networks theory into a real life industrial case. These methods are usually quite theoretical and difficult to be used, due to the mathematical background required. The paper has demonstrated a reverse decision method of simplifying the decision making process. A method was analysed to avoid entering the large amount of conditional probabilities that the typical Bayesian network would require. The paper suggested that the structure of the Bayesian network be reversed, thus minimise the necessary amount of data required for performing the Bayesian inference. The integration of the method into a web based software tool is simple enough and enables end users to use it in real life situations.

In addition, the paper demonstrated a method for capturing the knowledge of the domain's specialist and introduced the critical factors that make a model quantify the buyer's likely decision. The method is able to evaluate a customer, having a limited amount of data about him. The specialist's knowledge comprises the specific factors that influence the customer's decision as well as the weight of each factor on the total decision. The Bayesian network proposed, models these factors and assigns conditional probabilities to model the importance of each factor. The paper demonstrated that the Bayesian networks method wassuitable for quantifying a customer's likely decision and could be used effectively formodelling a set of factors that determine his behaviour.

Further work is necessary for the tool to be integrated as a module of a supply chain control tool for automatically assessing a customer's likely response, under the different delivery dates of the vehicle.

Acknowledgments
This work has been partially supported by the research project "MyCar", funded by the CEU. The authors would like to express their gratitude to Mr Peter Cowburn, Mr Domingo Lapadula

from Ford of Europe and Mrs Francesca Di Luccio from Centro Richerce Fiat for supporting this research effort.

# Table with captions 


Table 1. Competing orders from individual customers during the order promising process


Table 2. Factors affecting a buyer's likelihood to buy a vehicle

satisfaction | Ambivalent  |
requirements | Specific requirements  |

Table 3. Potential states of each factor affecting a buyer's likelihood to buy a vehicle

# Figure Captions 

Figure 1. GoodDrive impact on ProbabilityofSale
Figure 2. Conditional probabilities table for GoodDrive impact on ProbabilityofSale
Figure 3. GoodDrive and CompetitivePrice impact on ProbabilityofSale
Figure 4. Conditional probabilities table for GoodDrive and CompetitivePrice impact on ProbabilityofSale

Figure 5: Probabilistic distribution of the variables of cost and revenue using Bayesian networks
Figure 6: Conditional probability table between ProbabilityOfSsale and GoodDrive
Figure 7: Impact of the node GoodDrive on node ProbabilityofSale
Figure 8. Bayesian network for customer's likely decision
Figure 9. Conditional probabilities table between ProbabilityOfSale - GoodDrive populated with data generated by the distributions

Figure 10. Screenshot of the web application for Bayesian inference
Figure 11. 3-Tier model of the Bayesian inference web application
Figure 12. Screenshot of Bayesian inference outcome

![img-1.jpeg](img-1.jpeg)

Figure 1. GoodDrive impact on ProbabilityofSale $122 \times 34 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$


Figure 2. Conditional probabilities table for GoodDrive impact on ProbabilityofSale $84 \times 24 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$

![img-2.jpeg](img-2.jpeg)

Figure 3. GoodDrive and CompetitivePrice impact on ProbabilityofSale $122 \times 58 \mathrm{~mm}(300 \times 300$ DPI)


Figure 4. Conditional probabilities table for GoodDrive and CompetitivePrice impact on ProbabilityofSale
$115 \times 52 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$

![img-3.jpeg](img-3.jpeg)

Figure 5. Probabilistic distribution of the variables of cost and revenue using Bayesian networks $106 \times 27 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$

![img-4.jpeg](img-4.jpeg)

Figure 6. Conditional probability table between ProbabilityOfSsale and GoodDrive $98 \times 45 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$

![img-5.jpeg](img-5.jpeg)

Figure 7. Impact of the node GoodDrive on node ProbabilityofSale $105 \times 25 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$

International Journal of Computer Integrated Manufacturing Page 30 of 34

![img-6.jpeg](img-6.jpeg)

Figure 8. Bayesian network for customer's likely decision
250x178mm (300 x 300 DPI)

![img-7.jpeg](img-7.jpeg)

URL: http://mc.manuscriptcentral.com/tandf/tcim Email:ljcim@bath.ac.uk

![img-8.jpeg](img-8.jpeg)


Figure 9. Conditional probabilities table between ProbabilityOfSale - GoodDrive populated with data generated by the distributions
$105 \times 44 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$

![img-9.jpeg](img-9.jpeg)

Figure 10. Screenshot of the web application for Bayesian inference
209x168mm (300 x 300 DPI)

![img-10.jpeg](img-10.jpeg)

Figure 11. 3-Tier model of the Bayesian inference web application $137 \times 79 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$


Figure 12. Screenshot of Bayesian inference outcome $205 \times 160 \mathrm{~mm}(300 \times 300 \mathrm{DPI})$