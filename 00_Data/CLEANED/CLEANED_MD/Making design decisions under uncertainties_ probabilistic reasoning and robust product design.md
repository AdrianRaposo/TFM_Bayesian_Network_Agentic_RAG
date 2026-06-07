# Making design decisions under uncertainties: probabilistic reasoning and robust product design 

Paul Christoph Gembarski ${ }^{1}$ (D) $\cdot$ Stefan Plappert ${ }^{1}$ (D) $\cdot$ Roland Lachmayer ${ }^{1}$ (D)<br>Received: 10 December 2020 / Revised: 30 July 2021 / Accepted: 4 August 2021 /<br>Published online: 19 August 2021<br>(c) The Author(s) 2021


#### Abstract

Making design decisions is characterized by a high degree of uncertainty, especially in the early phase of the product development process, when little information is known, while the decisions made have an impact on the entire product life cycle. Therefore, the goal of complexity management is to reduce uncertainty in order to minimize or avoid the need for design changes in a late phase of product development or in the use phase. With our approach we model the uncertainties with probabilistic reasoning in a Bayesian decision network explicitly, as the uncertainties are directly attached to parts of the design artifact's model. By modeling the incomplete information expressed by unobserved variables in the Bayesian network in terms of probabilities, as well as the variation of product properties or parameters, a conclusion about the robustness of the product can be made. The application example of a rotary valve from engineering design shows that the decision network can support the engineer in decision-making under uncertainty. Furthermore, a contribution to knowledge formalization in the development project is made.


Keywords Bayesian network $\cdot$ Decision network $\cdot$ Probabilistic reasoning $\cdot$
Decision-making under uncertainty $\cdot$ Solution space development

## 1 Introduction

How can a development team design an aircraft wing, when it is not known which of five different available engine types will be mounted below? There are different answers to this problem that all have their pros and cons: For example, if the development team decides to dimension the wing with respect to the heaviest and biggest engine, this will influence properties and efficiency of the aircraft negatively when a much lighter one is installed later.

[^0]1 Institute of Product Development, Leibniz University of Hannover, An der Universität 1, 30823 Garbsen, Germany


[^0]:    Paul Christoph Gembarski
    gembarski@ipeg.uni-hannover.de

If the development team e.g., decides instead to dimension a wing for each of the five engine types, apparently four drafts will be discarded later, the resources that were spent to design them are lost and the efficiency of the development team suffers.

Independently from understanding product development as problem-solving or decisionmaking process, development teams need to make decisions about the design object that are subject to uncertainty (Hazelrigg, 1998; Ullman, 2001; Vajna et al., 2014; Pahl et al., 2007). Such uncertainties occur due to translation errors from customer requirements to functional requirements during specification (Suh, 1990; Girod et al., 2003), generally due to vagueness in the early phase of development (Xu et al., 2007; Velasquez \& Hester, 2013), but also due to e.g., emergent functions and failures that go along with the integration of components to a system (Papakonstantinou et al., 2012; Shields \& Singer, 2017). Not to forget about tolerances and deviations resulting from manufacturing (Gembarski \& Lachmayer, 2018; Pérez et al., 2006; Schleich \& Wartzack, 2015).

Considering these uncertainties is a major concern of complexity management (Frizelle, 1998; Suh, 2005; Gembarski \& Lachmayer, 2017). Basically, two different strategies may be observed here. The first one aims at the artefact and is to make the design itself insensitive to uncertainties in the sense of robust design (Hazelrigg, 1998; Taguchi et al., 2000; Park et al., 2006). The second strategy targets on the process and is to enable the development team to quickly assess the consequences of a decision on the product as well as its life cycle and thus efficiently respond to changes (Renzi et al., 2017; Li et al., 2018). An effortful way to do this is establishing knowledge-based engineering and design automation systems to rapidly compute changes and make knowledge accessible for future development projects (Verhagen et al., 2012; Hopgood, 2012; Biedermann \& Meboldt, 2020; Gembarski, 2020; Stettinger et al., 2014). Another way, especially in the early phase of development, is to discover dependencies between customer requirements and functional requirements, e.g., applying Quality Function Deployment or Axiomatic Design (Suh, 1990; Terninko, 1997; Kulak et al., 2010).

A fundamentally different approach is to model the uncertainty as such, which is done e.g., by fuzzy sets in the context of requirement engineering (Antonsson \& Otto, 1995; Vanegas \& Labib, 2005; Liu, 2011). Here one aim is to mimic imprecise human naturallanguage processing, working with ratings and including vague data in e.g., prioritizing requirements (Lima et al., 2011; Temponi et al., 1999).

In this paper, we investigate another approach to model uncertainties explicitly which is probabilistic reasoning in a Bayesian decision network (Nielsen \& Jensen, 2009; Moullec et al., 2013). The idea behind is to infer based on incomplete information which is expressed by unobserved variables in the Bayesian network and consider this in defining product properties and architectures.

The remainder of this article is structured as follows: in Section 2, the theoretical background regarding uncertainty in engineering design and the modeling of uncertainties with probabilistic reasoning is presented. Afterwards, Section 3 points out related work with respect to the application of Bayesian decision networks for design problems. Section 4 describes our approach to use such a network to decide about product properties and quantify options for robust design on the example of a rotary valve. Finally, Section 5 provides the discussion and lessons learned, while Section 6 summarizes the article and points out further research potentials.

# 2 Theoretical background 

Considering uncertainty during product development is a necessary task (Wiebel et al., 2013; Chalupnik et al., 2009). Following (Kreye et al., 2011), there are four different types of uncertainty:

- Data uncertainty: This type contains all uncertainties due to vagueness of inputs for models and development processes like imprecise requirements (Velasquez \& Hester, 2013).
- Model uncertainty: These encompass uncertainties and imperfections with respect to synthesis and analysis models, e.g., a model for finite element analysis has simplifications regarding boundary conditions and resolution, which result in deviations of the mechanical properties (He et al., 2020).
- Phenomenological uncertainty: This kind describes deviations in the behavior of the actual created design artefact in comparison to the desired behavior (Papakonstantinou et al., 2012).
- Context uncertainty: Such uncertainties describe the influence of the environment on a system or design artefact, e.g., a differing use scenario of the customer after deployment (De Weck et al., 2007).

Understanding uncertainty as modeling object of a design artefact, development teams have two fundamental options for implementation, implicit and explicit modeling. Regarding the first, designers do not model uncertainty as such, but the tools of the computer aided engineering environment integrate uncertainty considerations. Taking the example of multi-objective optimization, the above-mentioned data and context uncertainty can easily be implemented by automatically varying the inputs for the optimizer (He et al., 2020; Wolniak et al., 2020). This applies both for design variables which are varied by the optimizer itself and design parameters that are kept constant by the optimizer (Gunawan \& Azarm, 2005). Approaches like Latin Hypercube Sampling divide the design variable space accordingly into equal sets in order to identify not only the pareto optimal solutions as is done by the optimizer but also to examine the neighborhood of these points in order to get robust designs and uncover sensitivities of design variable changes on the objective function of the optimization (Alinejad \& Botto, 2019; Venanzi \& Materazzi, 2013).

Another way of implicitly considering data and context uncertainties is the creation of design automation systems. Here, the design process of a component is completely formalized and implemented into a computer aided engineering environment (Brockmöller et al., 2020; Amadori et al., 2012; La Rocca \& van Tooren, 2010). Variations of requirements can be directly computed into product variants, allowing to analyze sensitivities of changes and find clusters of solutions for requirement sets (Siqueira et al., 2019; Schätz et al., 2010). The modeling is commonly based on techniques for the synthesis of expert systems (La Rocca, 2012; Plappert et al., 2020b).

In explicit modeling, uncertainties are attached directly to parts of the design artefact's model. One way to do this is the application of probabilities to varying design parameter values and their occurrences (Suh, 2005; Nielsen \& Jensen, 2009). Since such probabilities usually are dependent and condition each other, approaches like Bayesian networks have been formulated (Koski \& Noble, 2011).

In order to better understand how a Bayesian network works, the Bayesian rule (1), which is the core of inference, is explained using a simplified application example for the dosing of powder for the preparation of hot drinks. In the first step, the cause-effect pair of watery hot drink as effect and the low powder dosing as cause is considered, whereby the probability $\mathrm{P}($ low $\mid$ watery) (posterior probability) is searched with which the cause is actually responsible for the effect, i.e., given the effect (here watery), how probable is the cause (here low). The probability of the general occurrence of the cause of low powder dosing (prior probability) is determined using a sensor with a probability $\mathrm{P}($ low $)=0.1$ and based on a statistical analysis, the watery taste occurs with a probability of $\mathrm{P}($ watery $)=0.2$. Due to the subjective perception of the watery taste, the likelihood of the effect is given as $\mathrm{P}($ watery $\mid$ low $)=0.8$. The application of the Bayesian rule leads to a probability of $\mathrm{P}($ low $\mid$ watery $)=0.4$, so the low powder dosage is to $40 \%$ the reason for the watery taste of the hot drink.

$$
\mathrm{P}(\text { cause } \mid \text { effect })=\frac{\mathrm{P}(\text { effect } \mid \text { cause }) \mathrm{P}(\text { cause })}{\mathrm{P}(\text { effect })}
$$

An extension of the presented example is shown in Fig. 1, where the causes blocked powder supply and defective flow sensor are possible reasons for the watery hot drink. For better traceability, the effects and causes can be represented as nodes with probabilities in a directed acyclic graph (DAG), where the causal relationships between the nodes are shown as arcs (Russel \& Norvig, 2012; Zhu \& Deshmukh, 2003). The parent nodes blocked powder supply and defective flow sensor are not dependent on any other node, therefore they are described by their occurrence or prior probability. In contrast, the dependence of the nodes incorrect mixing ratio and watery hot drink on prior nodes is expressed by conditional probability tables (CPTs). As new knowledge or evidence becomes available, the conditional probability distributions of the unobserved variables are updated, allowing the Bayesian network to infer (Moullec et al., 2013).

As an extension to the Bayesian networks, decision networks represent the knowledge about an uncertain problem domain as well as the available actions and the desirability of the individual states (Zhu \& Deshmukh, 2003). The structure of the decision network is

![img-0.jpeg](img-0.jpeg)

Fig. 1 Simple example for a Bayesian network for a watery hot drink

characterized by a DAG, which is based on the chance nodes of a Bayesian network and extended with additional node types for actions and utilities (Russel \& Norvig, 2012):

- Chance Nodes: random variables where each node is attached to a conditional distribution indexed by the state of the parent node as used in a Bayesian network
- Decision Nodes: variables that represent a selection of actions or design parameters for the engineer to make a decision
- Utility Nodes: nodes with a utility function describing the preferred results

Once the conditional probabilities of the Bayesian network are updated, the possible actions are evaluated by setting the decision nodes and made available to the utility node (Russel \& Norvig, 2012). As a result, the action that has the most added value based on the utility functions is proposed. By dividing the uncertainties in the Bayesian network and the decision parameters into decision nodes, the recommendations given can be easily understood and the decision network can be easily extended. In addition, it enables optimal decision-making, even if only partial observations of the world are given (Murphy \& Others, 2001). For an example for a decision network see Section 4.

# 3 Related work 

In engineering design, decisions in the early phases of product development often have to be made under high uncertainty regarding the impact on the entire product life cycle. In the related literature, Bayesian networks are often used to model the uncertainty in order to represent the possible solution space (Moullec et al., 2013; Shahan \& Seepersad, 2009), to reduce large data sets by integrating them into a model (Hanafy \& Elmaraghy, 2011) or generally to represent relationships between sets of variables in the form of probabilities (Ren et al., 2009; Zhu \& Deshmukh, 2003).

When modeling a Bayesian network, two sources of uncertainty are often considered. Either the uncertainty is mapped as probability for the optimal solution when exploring the solution space, or it is estimated based on data from the utilization phase of the product and its impact on the entire product life cycle is determined.

Moullec et al. (2013), e.g., describe a Bayesian network, which spans a design space by manipulating deterministic and probabilistic data in order to perform product architecture generation and exploration. By using templates for the modeling of the chance nodes, among other things the design variables, constraints and confidence levels are represented so that the compatibility of components for a bicycle can be checked. Bayesian networks do not only offer the possibility to represent the designer's knowledge and experience (Shahan \& Seepersad, 2009), they can also be built and updated by analyzing data, so that they can be used to predict future designs based on data about past products (Jones et al., 1993; Hanafy \& Elmaraghy, 2011).

Wang et al. (2018) also span a solution space using BN to support the engineer in the decision-making process for Design for Additive Manufacturing (DfAM). For this purpose, they consider parameters of the manufacturing process, in relation to the machine and the part to be printed, as well as possible materials, based on which a statement about the product properties can be made.

A common criticism of the Bayesian networks is the need for precise information in the form of prior and conditional probabilities (Ren et al., 2009), which is not always available, especially for new products where no data from use is known. In these cases, expert

knowledge is usually used, where the problem modeling and especially the uncertainty estimation is subjective (Moullec et al., 2013).

Ren et al. (2009) take up the criticism of the need for precise probabilities for Bayesian networks by formulating the input variables of the Bayesian network as fuzzy probabilities. In their application of a fuzzy Bayesian network (FBN) they use risk factors to predict the collision probability of an offshore installation during loading due to human error, already in an early phase of product development. FBN seem to allow more flexibility and easier interpretation through verbal expressions (Ren et al., 2009), thereby increasing the computational effort and expanding the possible solution space, similar to another layer of nodes in the Bayesian network.

Also, Rastayesh et al. (2020) deal with the possible risks or failures of a product by using a BN instead of risk priority numbers (RPN) to determine the most critical failure causes from an FMEA analysis. For this purpose, they analyze the influence of factors such as high temperature or over voltage on the probability of failure of a MOSFET for a fuel cell.

Shahan \& Seepersad (2009) follow another approach by using the Bayesian network for set-based collaborative design, where different design departments model their promising regions in the design space for an unmanned aerial vehicle. Afterwards, these local networks are shared and combined to find common interests, limit the design space and propose appropriate design parameters to support decision-making.

A combination of the uncertainties in the use phase and the representation of possible design parameters to span the solution space was not mentioned in the found literature, although a holistic view of the uncertainties in engineering design is desirable.

# 4 Application of probabilistic reasoning in engineering design 

Rotary valves or metering feeders are used for metering and conveying free-flowing bulk materials. Figure 2 shows a rotary valve which portions bulk material with the rotor pockets and transports the filling per rotation. It consists of the components housing, rotor and shaft and is used because it is easy to handle and ensures reproducible results. Due to the volumetric dosing, the dimensions or design of the rotary valve have to be adapted to the used
![img-1.jpeg](img-1.jpeg)

Fig. 2 Rotary valve for the dosing of bulk food

bulk material (Vetter, 2002). Furthermore, the gap between the housing and the rotary valve has to be taken into consideration to prevent bulk material from being drawn into the valve or the bulk material from being sheared off. Especially for discontinuous and quantitative dosing, the size of the rotor pocket is decisive. The aim of the engineer is to find the size of the rotor pocket that covers as many possible and probable scenarios.

# 4.1 Modeling of a decision network for the application example 

A decision network was created to support the design engineer in the decision-making process for the optimal rotor pocket size, which also represents the given uncertainties due to the boundary conditions. As application scenario, the rotary valve is integrated into a machine for the preparation of hot drinks and doses the bulk food in the required quantity for different types of hot drinks. Furthermore, the machine is installed in different locations, e.g., in home kitchens, offices or cafés. The modeled decision network (Fig. 3) consists of three parts: the Bayesian part, which represents the uncertain boundary conditions, the decision part, in which possible design decisions are stored, and the utility part, which contains the functions for the evaluation of preferred outcomes. The Bayesian part or Bayesian network contains seven chance nodes. The initial nodes bulk food and place of use represent the possible use cases in the application scenario. To be able to make a statement about the effects of the initial nodes, further nodes are used, like the nodes shear, weight, and density, which are dependent on the selected bulk food. The node quantity of liquid required for hot drinks varies depending on the place of use. To determine the quantity to be dosed, the node dosing volume is used, which depends on the nodes weight, density, and quantity of liquid. The additional node shear considers the effects of bulk food on the functionality of the rotary valve. The decision part consists of five decision nodes, which describe possible actions or design parameters. The decision nodes rotor diameter, pocket length, and pocket width represent the dimensions of the rotor pocket. The decision node rotor pocket size depends on these and displays the different pocket sizes as volumes. The node pocket
![img-2.jpeg](img-2.jpeg)

Fig. 3 Decision Network for rotary pocket size

quantity is used to model the influence of the number of pockets on dosing behavior. The utility part evaluates the optimal rotor pocket size according to criteria such as shear utitlity, exact dosing, fast dosing, and high variability. For this purpose, the utility function of the utility node represents the preferred outcomes, including design conditions.

# 4.2 Programming of the decision network for the application example 

An open source package for directed graphical models called Bayes Net Toolbox (BNT) was used to program the decision network for the application example in Matlab. The variety of implemented inference algorithms (Murphy \& Others, 2001) allows to first model the Bayesian network and then to search for a suitable inference strategy.

First, the programming in Matlab was started with the representation of the Bayesian network. A part of the programmed Bayesian network is shown in Fig. 4. The occurrence probabilities of the chance nodes bulk food and place of use are stored. Since the probabilities of the chance nodes shear, weight, density, and quantity of liquid depend on the parent nodes bulk food or place of use, they are stored in the form of conditional probability tables (CPTs). As the CPT for the dosing volume for hot drink contains 48 rows, it is not shown in the figure. The reason why CPTs were used is that the application example contains only discrete variables and therefore the inference was simplified. The probability values are from a similar project and were determined empirically.

To determine the possible rotor pocket sizes, possible design parameters were stored. For the variation of the diameter a range from 40 to 70 mm was defined. The pocket length varies between 15 and 30 mm , and the pocket width between 10 and 30 mm . These geometric configurations or variants result, on the one hand, from the limitation of the solution space due to the reduced installation space within the machine and, on the other hand, from the manufacturing restrictions in the production of the pockets. The defined step size of 5 mm is intended to ensure that very similar application scenarios are mapped with one rotor design to also reflect the robustness of the solution. By this procedure the decision network can
![img-3.jpeg](img-3.jpeg)

Fig. 4 Bayesian network for dosage in the preparation of hot drinks

easily be extended. The number of pockets depends on the rotor pocket size. In general, a maximum utilization of the available rotor surface is targeted.

The sum of utilities of all possible outcomes, weighted by the probability of their occurrence (Hazelrigg, 1998), describes the general utility function. As this general utility function also contains results that lead to an unsuitable design layout, the following conditions are also represented in the utility function:

- High Variability: One rotor pocket size should be able to cover many different and most likely dosing volumes. A filling level of the pocket size between 90 and $100 \%$ is assumed. This criteria is considered the most important for robust design.
- Flexible Dosing: Multiple pockets on the rotor allow more precise dosing without the loss of time due to the higher number of rotations.
- Fast Dosing: With the same variability, the rotor pocket size should be preferred, which can dose the most likely dosing volume in fewer rotations.
- Exact Dosage: To assess the accuracy of the dosing process, the average deviation of the dosed volume at a filling level of $95 \%$ compared to the desired dosing volume is calculated.
- Shear Utility: The shear utility represents the functional impairment of the rotary valve due to shearing of the bulk food. It takes into account the probable influence of the bulk food during shearing and the shearing angle, which depends on the position and size of the rotor pocket.

The listed conditions first restrict the solution space, since only valid solutions are considered. Then, the conflicts between the conditions must be solved by the algorithm in the form of a prioritization. For example, an exact dosage leads to a small rotor pocket size, whereas a fast dosage requires a large rotor pocket size.

# 4.3 Results of the decision network 

The goal of the decision network for the application example is to assist the engineer in selecting the optimal rotor pocket size. To do this, the solution space is continuously constrained to simplify the search for a robust solution. After eliminating all solutions that are technically infeasible, such as a pocket number that would lead to geometric overlaps on the rotor, the solution space is further constrained by the utility functions described in Section 4.2 (Fig. 5).

To represent the solution space reduction, the trade-off between dosing as variable as possible, through a small rotor pocket size, and dosing as quickly as possible, through a low operating time, is used. In the first step (Fig. 5a) the shear utility is used as a selection criterion, so that solutions with a shear utility factor below 70 are eliminated. With this limit, only solutions with a low probability of wear are considered. For the restriction of fast dosing in Fig. 5b, only solutions are allowed which do not exceed an operating time of 60 s . This value was chosen so that the time span for one dispensing operation is acceptable, compared to the total working time of the machine. Subsequently, variability and exact dosing are used as selection criteria (Fig. 5c). Here, the dosed volume through the rotor with a filling level of $90-100 \%$ may only deviate by $\pm 5 \%$ from the required dosing quantity. This leads to the effect that small pocket sizes with many turns are eliminated, since the deviation per turn is decisive here. Due to the search for a solution that is as robust as possible, it should be possible to use the rotor pocket size in as many application scenarios as possible. For this purpose, we use the utility probability with a value of at least $33.33 \%$, so that the selected cellular wheel pocket size can be used in one third of the probable application cases

![img-4.jpeg](img-4.jpeg)

Fig. 5 Reduction of the Solution Space through Utility Functions
(Fig. 5d). The solution with the maximum utility probability and the shortest operating time is selected as the optimal size.

Table 1 shows the results of the decision network in Matlab for different information levels or usage scenarios. The second column with the name Known Information represents the different levels of evidence or observation as input for the Bayesian part. The columns Most Probable Dosing Volume and Probability Dosing Volume represent the chance node dosing volume and thus the output of the Bayesian network. The next block of the table represents the decision part. Here the dimensions Rotor Diameter (RD), Pocket Length (PL), and Pocket Width (PW) as well as the resulting $95 \%$ Rotor Pocket Filling are listed. The Pocket Quantity is the number of pockets that most frequently fit on the area of the rotor. The utility part contains the selection criteria for the optimal rotor pocket size and the Shear Utility shows the expected utility for sheared bulk food. The columns Average Dosing Deviation and Turns represent the dosing behavior. The Utility Probability describes the added probabilities of the dosing volumes, which can be dosed with the rotor pocket size. Hereby it is to be noted that a higher information level does not necessarily lead to a higher utility probability, since this depends on the uncertainty or the variety of probabilities of the chance nodes. This can also be shown by comparing the utility probabilities for no known information with $38.81 \%$ and for bulk food 2 with $35.48 \%$. The column rotor design refers to the different designs of the rotor in Fig. 6 at different information levels.

Based on these results, the implications of the uncertainty on the design can be estimated and recommendations for the designer can be derived to support him in the development of robust products.

# 4.4 Knowledge discovery and design implications 

The decision network is able to uncover sensitivities of design parameters on the later design artifact and its robustness. As an example, for bulk food with a higher density, such as bulk food 1 and 2, smaller rotor pocket sizes tend to be used, as in rotor design a), b), c) and d). In contrast, for bulk food 3 with a lower density, rotor designs f) and g) are preferred. In addition, the location of use has an influence, since locations with a greater demand for liquid also require more bulk food to be dosed. This again leads to larger rotor pocket sizes.

Table 1 Results for the optimal rotary pocket size with utility probabilities

Information | Most Probable
Dosing Volume
$[\mathrm{ml}]$ | Probability
Dosing
Volume [\%] | Rotor
Diameter
$[\mathrm{mm}]$ | Pocket
Length
$[\mathrm{mm}]$ | Pocket
Width
$[\mathrm{mm}]$ | 95\% Pocket
Filling
$[\mathrm{ml}]$ | Pocket
Quantity | Shear
Utility | Turns | Dosing
Deviation
$[\mathrm{ml}]$ | Utility
Probability
$[\%]$ | Rotor
Design |

![img-5.jpeg](img-5.jpeg)

Fig. 6 Different Designs of the Rotary Valve Rotor

The optimal rotor design a) with no information available, can be traced back to the high probability for bulk food 1 and place 1.

Additionally, the utility probability of the decision network allows a prediction about the robustness of the design:

- High utility probability: For a value with a high utility probability, the assumption can be made that this value represents a suitable solution for as many scenarios as possible and therefore no further changes are necessary. In addition, the described uncertainty within the decision network has little influence on the result and therefore it can be concluded that it is a robust product.
- Low utility probability: For a low utility probability a value can only cover a part of the possible scenarios. A high diversity within the decision network may be the result of a higher uncertainty influence. For this reason, products have to be adaptable to different conditions, i.e., high variability or modifiability is required.

Based on the solution space reduction and calculation of the utility probability, a selection can be made for the rotor pocket size that is suitable for the most probable use cases. E.g., in case no further information is available, the upper diagram of Fig. 7 shows the distribution of utility probabilities for all possible rotor pocket sizes based on the decision nodes. It can be seen that the rotor pocket size with a volume of 1.36 ml represents the preferred solution with a utility probability of $38.81 \%$. In addition, the lower diagram shows that the rotor pocket size has the highest utility probability. However, this can only be attributed to three use cases with relatively high probabilities of occurrence. Thus, the rotor pocket size of 1.36 ml can only be used very specifically and can therefore not be defined as a robust solution.

Decision networks are suitable for deriving and handling incomplete information because they represent it in the form of probabilities, which restrict the solution space or consider

![img-6.jpeg](img-6.jpeg)

Fig. 7 Probability of Dosing Volume and Fitting of Rotor Pocket
it in more detail when the level of information or knowledge is higher. In the example of the rotary valve, there is incomplete information about the specific application scenario, e.g. which bulk food is used and at which location the machine is set up. This uncertainty is reflected in the probabilities of occurrence, which in turn lead to a wide range of possible dosing volumes. For example, the incomplete information about the bulk food and the location leads to a rotor pocket size of 1.36 ml , which can only cover the possible use cases with a utility probability of $38.81 \%$. In contrast, a restriction of the solution space for the use of bulk food 3 and location 3 leads to a rotor pocket size of 4.86 ml and the solution found completely represents the restricted solution space. It was shown that when incomplete information requires a wide range of possible solutions, the restriction of the solution space becomes necessary by increasing the knowledge. Besides the occurrence probabilities of the boundary conditions, the downstream nodes may also contain incomplete information about the occurrence, the existing dependency or its weighting.

# 5 Discussion 

As the example described above shows, the BDN supports the designer in discovering knowledge in the form of sensitivities, since the influence of external boundary conditions (e.g. place of installation or the usage scenarios) on the product, in particular on the design

parameters, like geometry or materials, can be evaluated. In addition, dependencies between requirements can be represented and structured by considering cause-effect relations. In this way, the solution space of the design artifact can be spanned. Individual solutions then can be tested regarding requirement fulfillment and analyzed with respect to possible requirement corridors which is one source of robustness. In addition, robustness can be considered by using utility functions to restrict the solution space, which cover a wide range of use cases. Thus, the relation between solution space and requirement space can be formalized already at an early development stage and with acceptable effort. This aspect is valuable for decision support in the engineering process, but also for marketing and product management, e.g., for customer segmentation.

By modeling the BDN in different parts, i.e., Bayesian, decision, and utility part, the modeling activities can be performed in various stages in the product development process. First, taking specification design and requirement engineering, the design team can easily compare different scenarios of weighting requirements by adjusting the nodes of the Bayesian part. Especially in the case of conflicting requirements this supports design teams in defining the prioritization or conflict resolution strategy. In our example with the hot drink brewing machine, the Bayesian network additionally supports the refinement of functional requirements, i.e., the decomposition of the dosing volume according to type of bulk food, weight, density, but also risky properties such as the shear probability leading to possible later malfunctions. This has the advantage that, e.g., the weight or density of the bulk food is easier to relate to the dosing volume than only the information about the bulk food used. Additionally, the approach necessitates designers to think about possible misbehavior of the later designs on a functional level. Even if distinct probabilities or statistical data are not available, a scenario analysis may be performed with low, medium or high likelihoods of failure occurrences. In summary, the main task in this early phase is the structuring of the solution space and the derivation of evaluation criteria for later concepts.

Second, the BDN can be used with a focus on conceptual design by extending the Bayesian with decision and utility part. For this purpose, possible and relevant design parameters on a functional level are determined and information about the sensitivity of individual solution concepts with respect to changes in requirements is inferred by updating the BDN. In the example above, the required dosing volume per application is such a parameter since at this time this is independent from the later solution concept. The utility functions can then also be used to evaluate and compare possible solutions.

Third, addressing drafting and embodiment design, the relations of draft determining parameters, and their values can be computed. Here, the robustness consideration also offers potential in defining variants of the product and its components. In the case of our example, this is reflected by the diameter of the rotary valve: Even if the use case of the hot drink brewing machine is variable, a solution for updating the machine to a different use case is exchanging the rotor with another pocket design. As a consequence, e.g., the design of the housing should be standardized accordingly.

Referring back to the four fundamental types of uncertainty mentioned by Kreye et al. (2011), two of them are directly addressed through BDN: First, data uncertainty is reflected by the implemented probabilities for the occurrences of requirements and their values. Second, context uncertainty is represented by the different use cases, disturbances and their respective probabilities. If one now considers the other two types, phenomenological and model uncertainty, the answer is more difficult. Regarding phenomenological uncertainty, the BDN could indeed answer questions on that if the according effects can be coded. An example of this is the implementation of manufacturing tolerances, wear and random system failures, e.g., due to component reliability. Here the question is whether an implementation

into the BDN or other modeling approaches, e.g., numerical multi-objective optimization, are more efficient. Here, the level of information and the frequency of change are decisive criteria for the selection of the modeling approach: The predominantly incomplete information and the high uncertainty during the early development phase lead to the necessity that the models need to be changed and adapted frequently. At this stage, a statement of sensitivities such as BDN is often sufficient and the modeling and computational effort remains manageable. As development progresses, the solution space considered becomes smaller, so that a detailed consideration of the geometry, e.g. in the form of a CAD model, becomes necessary and the modeling and calculation effort is reduced. In combination with a numerical optimization, e.g., combined with Latin-Hypercube-Sampling, the actual usage process can be modeled to provide a more detailed estimation of the product design and further converge the solution space.

With respect to model uncertainty, the known criticism of the BDN approach is still valid. Preconditions for its use are modeling experience, knowledge of the usage scenarios, and the availability of data, which includes not only conditional probabilities but also statistical data. Especially the availability of data is difficult for creative designs without predecessors. In our example, the single probabilities were obtained from experts and empirical data from prototype tests. The latter is objective but perhaps not statistically verified, while the first is more or less subjective. In order to validate the model, a test on decision gates in former, already completed projects, where it should come to similar conclusions as the designers, seems at least possible.

# 6 Conclusion \& future research 

Robust products are defined as products which are insensitive to uncertainties. With our approach, we take up this definition and can represent the uncertainty with a BDN in the form of conditional probabilities. The product properties or possible design parameters are stored in the decision part and a statement about the insensitivity of the products is made via the utility functions, among others in the form of the utility probability.

As stated in the introduction, uncertainty during development often leads to reduced efficiency, either of the product or of the development team which has to discard drafts or perform later changes due to new knowledge or changed requirements. In context of a generic product development process, involving specification design, conceptual design and embodiment design, we show different application areas and guiding questions for knowledge discovery. In this way, sensitivities of design parameter changes can be discovered and the robustness of a design may be examined with respect to different usage scenarios, supporting the decision-making process during development.

An open question is, what model resolution and following that, what modeling effort is necessary to sufficiently perform the activities of spanning, structuring and converging the possible solution space. Here, a comparison of different approaches, e.g., the BDN approach and robust numerical optimization at different stages of the development process could deliver new insights. Especially in the phase of embodiment design, when the solution space is already broadly restricted, robustness needs to consider, e.g., geometric tolerances due to the later manufacturing processes. In our example of the hot drink brewing machine, the shear probability of the inbound bulk food is likely to be influenced by the achievable tolerances. Including this into the BDN is possible, but since this design phase already operates with geometric models, design data for numerical analysis and optimization is basically available and offers the possibility of describing the design problem on a very detailed level.

On the other hand, the spanned solution space in specification design might be too large and to abstract to be structured by numerical optimization, especially when the resolution about design variables is still low and subject to a high probability of change.

To reduce the modeling effort, an algorithmization of, e.g., the variation of input parameters of a foundational Bayesian network by evolutionary algorithms or numerical optimization is a possible avenue to be investigated. Furthermore, to address the initially mentioned translation errors from customer to functional requirements, the integration of fuzzy sets as representation of requirements is likely.

Beside product development, the integration of BDN and recommender systems could be another starting point for further research. As recommender systems guide customers towards interesting and useful features for an individual value proposition (Plappert et al., 2020a; Felfernig \& Burke, 2008; Thakur et al., 2011), a system that can handle uncertain input parameters, incomplete data or even imprecisely formulated requirements could be a valuable building block for a sales support system as these also represent solution spaces.

Funding Open Access funding enabled and organized by Projekt DEAL.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
