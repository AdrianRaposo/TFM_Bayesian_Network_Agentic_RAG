# Application of a Bayesian Network in a GIS based Decision Making System 

A. Stassopoulou, M. Petrou \& J. Kittler<br>Dept. of Electronic and Electrical Engineering<br>University of Surrey<br>Guildford GU2 5XH, U.K.


#### Abstract

In this paper we show how a Pearl Bayes network of inference can be used with a GIS in order to combine information from different sources of data for the purpose of classification. Data may include satellite images, topographic maps, geological maps etc, each one with its own resolution and accuracy. We show how this uncertainty in the input data is incorporated in the network and develop also a method to construct the conditional probability matrices used by the network. We demonstrate our approach within the framework of the problem of assessing the risk of desertification of some burned forests in the Mediterranean region.


## 1 Introduction

In Geographic Information Systems most of the time the data represented by the various layers are of diverse origins with varied degrees of accuracy. These data usually have to be combined for the inference of some conclusions expressed in the form of labellings. The straightforward combination of information coming from the various layers often used for convenience (e.g. see Grunblatt et al. 1992, Chuvieco and Congalton 1989, Sader et al. 1995), not only fails to take into consideration the reliability of each source of information, it also ignores the fact that the rules of combining the information themselves may be unreliable. Thus, inspite of the uncertain

rules and the uncertain data, the output of such a GIS is a hard labeling with no indication given as to how reliable this classification is.

This is because most GIS perform reasoning with simplistic inference mechanisms in the form of IF-THEN rules. In rule-based reasoning, one has to know for certain that an assertion is true or false in order to draw a conclusion. Although the truth of certain premises may be suggestive of the truth of a conclusion, it may not imply it conclusively. It is evident that performing inference in any real world domain always requires some simplifications to be made. It is necessary therefore to bear in mind that conclusions drawn even from absolutely correct data may not always be correct.

In this paper we present a Pearl Bayes network for probabilistic reasoning with a GIS for the purpose of assessing the risk of desertification after a forest fire. The reason we chose this particular type of network, is because it allows the modelling of both types of uncertainty in the reasoning process, namely the uncertainty in the reasoning rules (modelled with the help of the conditional probability matrices involved in the network) and the uncertainty in the data (modelled by the probability with which a certain input parameter belongs to a certain class).

A Bayesian network (Pearl 1988, Pearl 1986, Pearl 1993, Charniak 1991, Henrion 1989, Goldman et al. 1993) is a powerful tool which can be used for the fusion of information coming from disparate sources with varying degrees of reliability. In these networks each node represents a variable the label of which is either given or has to be assessed and the relationships between the nodes are expressed in terms of conditional probabilities. Each variable can be labelled with a label from a corresponding finite set with a certain degree of confidence. The input data may concern any of the nodes and once they are fed into the right node, a mechanism is provided for the propagation of their information to all other nodes of the system.

So far Bayesian networks have been very widely applied in medical systems to perform medical diagnosis (Olesen et al. 1993, Hamilton et al. 1994). Medicine is one area where categorical decisions are not sufficient but instead one has to reason under various sources of uncertainty. Other applications involve forecasting (Abramson 1994, Gu et al. 1994), computer vision

(Gong and Buxton 1993) etc. Bayesian networks are particularly applicable to cause-effect problems i.e. problems that can easily be represented by cause-effect relationships between the variables of interest, as is the case in most medical problems and in the particular application presented in this paper. Their ability to perform bidirectional reasoning has also made them useful for troubleshooting system failures, including software and hardware problems as well as mechanical failures of cars and jet engines (Heckerman et al. 1995). The use of Bayesian networks in Geography, however, has been very limited with a few notable exceptions (e.g. Ducksbury 1993, Hass 1991).

In section 2 we shall present a brief literature survey of the various methods that have been used so far for reasoning with a geographic information. In section 3 we shall present a very brief overview of Bayesian networks so that we can establish our terminology. In section 4 we shall present the particular problem we have to solve with the help of which we shall exemplify the various aspects of using a Bayesian network with a GIS. We shall also describe the Bayesian network constructed for solving this problem. In section 5 we shall discuss how to model the uncertainty in the data assuming a certain type of error in the corresponding measurements and how to incorporate the uncertainty of the data into the network. In section 6 we shall discuss ways of deriving the conditional probability matrices needed by the Bayesian network. In section 7 we present some results of applying the theory developed in the previous sections to a set of real data concerning an area of study in Greece for which the expert's classification is available from ground inspection. We also compare our method with the IF-THEN rule based inference method. We conclude in section 8.

# 2 Literature Survey 

We classify the various methods used for fusion of information to two major categories, namely distributed versus centralised approaches. In the distributed approaches, the data from each sensor are processed separately and the outcomes from all the sources are combined. The data from each sensor are processed anyway whatever approach one uses, but in the case we are talking about, the data from each source are processed fully so that each pixel acquires a label

from the list of labels to be used in the final classification one tries to achieve. Subsequently, each source is given a different weight of significance and the results from each separate classification are combined into a final labeling scheme.

More often is preferred to combine data rather than conclusions drawn from individual sources. The combined data could be raw (as for example in Benediktson and Swain 1990, Benediktson et al. 1990,) or partly processed (as for example in Peddle and Franklin 1992, Richards et al. 1982). Such systems are centralised systems where there is a central inference mechanism employed to do the classification on the basis of all the data received.

Starting with distributed systems, Solberg et al. (1993) used satellite images and GIS ground cover data for land-use classification. The basic fusion model performed a linear combination of the probabilities of a pixel belonging to a particular class given the measurements from different sources of information. This linear function is the result of an assumption that the measurements from each source are independent.

Mason et al. (1992) developed the MuSIP (MultiSensor Image Processing) system for the development of data fusion techniques for the exploitation of multisensor and multitemporal images. The approach used was region based and the fusion of information happened at the high level of region classification. As the regions of each individual image were assigned labels from the final list of labels to be used, with varying probabilities, this system is a distributed system. The system was applied to forestry and one of the objectives was to detect changes occurring in forests, particularly those concerned with deforestation and afforestation. The input to the high level data fusion are two PUDs (Picture Understanding Databases) designed for storing 2D vector information, like regions, lines, points etc. For each region, information is stored concerning its attributes (e.g. size and shape), its bounding frame and adjacent regions. The output of the fusion model is another PUD, containing the matching regions and an error PUD containing regions that could not be matched. The matching of regions was based on a number of matching tests, namely attribute matching, label, relational and boundary matching. Each of these tests produced a confidence value supporting a specific region. These values were then combined using the Dempster-Shafer approach(Shafer 1976).

Some centralised systems that combine data instead of conclusions are reviewed next. Grunblatt et al. (1992) used a GIS together with simple ecosystem models for desertification assessment and mapping in Kenya. In this study five desertification indicators were selected for investigation: water erosion, wind erosion, vegetation degradation, range utilisation and human settlement. After deriving the status i.e. state or condition of these indicators by assigning values, the desertification hazard was calculated as a summation of the various indicator class values.

A forest fire hazard mapping was developed by Chuvieco and Congalton (1989). In this study digitally processed Thematic Mapper data were integrated with other layers of geographic information to derive a forest fire hazard map. The variables in this model included the basic factors that affect forest fires. For the integration of the five layers of information mentioned above, it was assumed that some of those layers have a higher influence on fire hazard than others and were ranked accordingly. The approach included several steps; first each data layer was weighted according to its impact on increasing the fire hazard. Second, each data layer was then divided into different levels which were assigned coefficients of 0,1 and 2 based on the ranking of high, medium and low fire hazard respectively. The final formula index was a linear combination of the results of the different layers.

Sader et al. (1995) used a GIS rule-based model to identify forest wetlands in Maine. An additive model was developed for this study. The model consisted of four hierarchical layers: each layer incorporated the GIS data and was arbitrarily assigned a weight based on its presumed contribution to identify wetlands. Each pixel was analysed at each layer in the model. The weights assigned to themes and attributes in the GIS model produced a numerical value that indicated the potential for a forest wetland to exist at any location. A lower weight was given to a GIS layer which was thought to be correlated with other variables in the database. As we will see in the description of our model later on, dependencies and independencies among the variables are presented in the structure of the Bayesian network and the propagation of information assures that these dependencies or independencies are not violated.

Binaghi and Rampini (1993) used fuzzy reasoning to combine land-use observables and ancillary observables to deduce the best fire risk judgement for each pixel in the studied area.

Land-use observables were classified into five classes of land cover using Landsat Thematic Mapper image. Ancillary observables included elevation, slope and other factors that affect forest fires. Linguistic labels low, medium and high were then introduced to describe these observables and were quantified with standard membership functions. The result was a degree of membership in the low, medium and high fire risk classes.

Middelkoop and Janssen (1991) developed a method of knowledge-based classification based on temporal relationships between classes. In this study spectral image information, information stored in a geographic information system and knowledge about crop rotation by means of state transition matrices were combined in a Bayesian maximum likelihood classification. The study involved acquisition of knowledge about the temporal relationships between classes from the available data and experts and representation of the knowledge.

Frank (1988) combined Landsat Thematic Mapper data with topographic and topoclimatic variables to map dominant vegetation communities in the Colorado Rocky Mountain Front Range. The thematic spectral bands were transformed into five band ratios and normalised difference variables to characterise the spectral patterns of vegetation community cover types. Slope, elevation, aspect and relief measures were also obtained to examine topographic effects on vegetation distributions. A topoclimatic index was created from a Digital Elevation Model to distinguish between favourable habitats for windblown and snow-covered communities. SlopeAspect index was used to characterise prevailing wind effects on soil, moisture and subsequent vegetation distributions. All these variables obtained were combined linearly to provide a discriminant score for an observation, for each dominant community. Then, using discriminant scores each observation was assigned to the dominant community using the posterior probability: the probability that an observation with a discriminant score of $D$ belonged to dominant vegetation community group $G$ was estimated by the conditional probability and the observation was assigned to the group which produced the largest conditional probability.

Srinivasan and Richards (1990) classified remotely sensed data into urban, woody vegetation, grass land and soil. The reasoning was based on IF-THEN rules which fired and gave a classification of the reason for a cover type (label) into three categories: prima facie reason, supportive

or criterion, each of which indicated a certain strength of the conclusion given the premises. After all the rules fired, the class labels were given endorsements based on the quantity of reasons for and against a class label. The endorsement was mainly biased by the strong reasons that confirm or deny a label.

Srinivasan and Richards (1990) also developed another system for land-use classification where the central inference mechanism used was based on the Dempster-Shafer theory (Shafer 1976). This evidential system was used to classify the pixels in the image of Sydney Harbor, into three primary features: water, cultural (man-made) and vegetation. Four Landsat Multispectral Scanner (MSS) images have been used from the bands 4, 5, 6 and 7. The system incorporated explicit knowledge in the form of several knowledge bases, each relating to a different source. These contain facts and rules specific to that source. Based on the data available to the source, the appropriate rules fired giving rise to the basic probability assignments (degrees of belief showing to what extend the data support the various class labels) to various nodes in a predefined hierarchy of possible class labels. The control mechanism forward chains through each rule base going from data to possible labels. Dempster-Shafer theory is then used to provide a consistent set of beliefs over all available data sources.

Duckshury (1993) used a Pearl Bayes network to classify urban regions versus non-urban in aerial photographs. He did not use multisource data, but rather multiprocessor data. In fact all his data came from an aerial image which, however, was processed in various ways so that different measurements concerning the same region were deduced. The different measurements (statistics) were then assessed and combined using a Pearl Bayes network, into a belief of the region to be urban.

# 3 Bayesian Networks 

Belief or Bayesian networks are directed acyclic graphs in which the nodes represent multivalued variables, comprising a collection of mutually exclusive and exhaustive hypotheses. The arcs signify direct dependencies between the linked variables and the strength of these depend-

encies are quantified by conditional probabilities.
Consider a typical node $X$ having m children $Y_{1}, Y_{2}, \ldots, Y_{m}$ and $n$ parents $U_{1}, U_{2}, \ldots, U_{n}$ as shown in figure 1 (The node variables will be denoted by capital letters and the parent and children will also have a subscript to distinguish among them). What follows is a description of the propagation algorithm developed by Pearl (Pearl 1988, Pearl 1986).
![img-0.jpeg](img-0.jpeg)

Figure 1: The parents and children of a typical node $X$ in a polytree

The purpose of the Bayesian network is to give a belief in each possible labeling for each node after some evidence arrives. That is, it gives the conditional probability of a node being in each of its states given the evidence observed. In order to estimate the belief of a node we need the information sent by the parents (causal), the information sent by the children (diagnostic) and the conditional probability matrices. The messages that communicate this information obtained by the parents are denoted by $\pi$ and the messages that carry information from the children are denoted by $\lambda$. We denote the belief in each node $X$ by $\operatorname{BEL}(X)$ which is a vector with elements $\operatorname{BEL}\left(x_{i}\right)$ where the small letter indicates a particular value of a state $i$ indicated by the subscript. Before any propagation commences we initialise the network. Every node is assigned a vector $\lambda$, a vector $\pi$ and a vector $B E L$. These vectors have as many elements as there are possible states for this node. To initialise the network, we set all elements of all $\lambda$ vectors to 1 . We also set all elements of the $\pi$ vectors of the root nodes equal to the prior probabilities for the corresponding states. All the values of the remaining variables of the network can be computed now

form the above initialised quantities, and the elements of the conditional probability matrices. An element of the conditional probability matrix looks like $P\left(x_{i} \mid u_{1 j_{1}}, \ldots, u_{n j_{n}}\right)$ and gives the probability of state $i$ for node $x$ conditioned on the states of its parent nodes. In addition to the above, each node, except the leaf nodes has a $\pi_{(s e n d)}$ vector that can be communicated to its children. This $\pi_{(s e n d)}$ vector carries as a subscript the name of the child it goes to. For example $\pi_{X}\left(u_{i j}\right)$ indicates the $j$ th element of the $\pi$ vector of the $U_{i}$ parent sent to its child $X$. Also, each node except the root nodes carries a $\lambda_{(s e n d)}$ vector which can be communicated to its parents. This $\lambda_{(s e n d)}$ vector carries as a subscript the name of the child it comes from. It has as many elements as the states of the parent node it goes to. For example $\lambda_{Y_{j}}\left(x_{i}\right)$ means the contribution of the $Y_{j}$ th child to the $i$ th state of parent $X$.

Having established our terminology, we can now summarize below the steps of the algorithm:

# - Step 1: Belief updating 

When node $X$ is activated it inspects both the $\pi_{X}\left(u_{i j}\right)$ messages communicated by its parents and the $\lambda_{Y_{j}}(x), j=1, \ldots, m$ messages communicated by each of its children (In case of two subscripts, the first indicates which variable's value and the second indicates the corresponding state i.e. $\pi_{X}\left(u_{i j}\right)$ indicates the $\pi$ value of the $j$ th state of the $U_{i}$ th parent).

By using these it updates its belief to

$$
B E L\left(x_{i}\right)=\alpha \lambda\left(x_{i}\right) \pi\left(x_{i}\right)
$$

where

$$
\pi\left(x_{i}\right)=\sum_{j_{1}} \cdots \sum_{j_{n}}\left[P\left(x_{i} \mid u_{1 j_{1}}, \ldots, u_{n j_{n}}\right) \prod_{m} \pi_{X}\left(u_{m j_{m}}\right)\right]
$$

where each summation ranges over all possible values of each parent,

$$
\lambda\left(x_{i}\right)=\prod_{j} \lambda_{Y_{j}}\left(x_{i}\right)
$$

and $\alpha$ is a normalising constant rendering $\sum_{x} B E L(x)=1$

# - Step 2: Bottom-up propagation 

Using these messages, $X$ computes a new $\lambda$ message to be sent to its parents $U_{i}$ :

$$
\begin{aligned}
& \lambda_{X}\left(u_{i j}\right)=\beta \sum_{m} \\
& \quad\left[\lambda\left(x_{m}\right) \sum_{j_{1}} \cdot \sum_{j_{i-1}} \sum_{j_{i+1}} \cdot \sum_{j_{n}}\left[P\left(x_{m} \mid u_{1 j_{1}}, \ldots, u_{(i-1) j_{i-1}}, u_{i j}, u_{(i+1) j_{i+1}}, \ldots, u_{n j_{n}}\right) \prod_{k \neq i} \pi_{X}\left(u_{k j_{k}}\right)\right]\right]
\end{aligned}
$$

where $\lambda\left(x_{m}\right)$ is given by 3 and the summation is over all possible values of all parents except parent $U_{i}$, for which we compute the $\lambda$ message for its $u_{i j}$ value.

## - Step 3: Top-down propagation

Each node computes the new $\pi$ messages to be sent to each of its children. The message that $X$ sends to its $j$ th child $Y_{j}$ is given by:

$$
\pi_{Y_{j}}\left(x_{i}\right)=\alpha \prod_{k \neq j} \lambda_{Y_{k}}\left(x_{i}\right) \sum_{j_{1}} \cdots \sum_{j_{n}}\left[P\left(x_{i} \mid u_{1 j_{1}}, \ldots, u_{n j_{n}}\right) \prod_{i} \pi_{X}\left(u_{i j_{i}}\right)\right]
$$

or equivalently

$$
\pi_{Y_{j}}\left(x_{i}\right)=\alpha B E L\left(x_{i}\right) / \lambda_{Y_{j}}\left(x_{i}\right)
$$

However, in order to apply the formulae and propagation algorithm above the network has to be singly connected i.e. only one path should exist between any two nodes. Otherwise the network is considered to have loops and various methods exist in the literature for handling them (Suermondt and Cooper 1991, Pearl 1988).

# 4 Problem Formulation 

The purpose of this work was to assess the risk of desertification of certain burned forest areas in Greece, by combining data from various sources together with expert knowledge about the desertification processes.

Desertification is land degradation in arid, semi-arid and dry sub-humid areas resulting from various factors, including climatic variations and human activities. The Mediterranean region is characterised by extensive aridity, forest fires, overgrazing and improper land use. This, combined with irregular but intensive precipitation can lead to land degradation.

Two major factors that directly influence the degree of risk of desertification of a burned forest are its regeneration potential and the danger of soil erosion. Attica is an area of arid and semiarid climate that suffers from repeated forest fires. The dominant forest species is Aleppo pine and a number of bushy species. Aleppo pine regenerates naturally after a forest fire due to the presence of mineral elements in the ash and the lack of competition for nutrients and water from other plant species, provided that the pine trees that were burned had left on the ground enough seeds of good quality. Maquis-type plants regenerate naturally after a forest fire by re-sprouting. The extent and rate of natural regeneration of a burned forest area, under Mediterranean conditions, depend on precipitation, surface geology, surface structure etc. This area of study in Greece is not thought of containing microclimates in it. We are actually interested in the relative ranking of burned forests within the same relatively small area of study, for the purpose of prioritising the reforestation resources of the country. Thus, over the whole area one can easily assume constant climatic conditions. Therefore, from all the factors that are known to influence the forest regeneration and soil erosion only those which are expected to vary from one site to the other are considered, namely soil depth, ground slope, rock permeability, aspect and animal grazing.

What follows is a description of the network constructed to tackle this problem.
The constructed network is shown in figure 2 alongside the labels (states) each node can take. Due to the nature of the problem we have designed the network so that the variables are discrete.

The main reason for this is that some of the variables in the network cannot be represented by real values (i.e. rock type) and due to the restrictions involved in having a network with both discrete and continuous variables, we have decided to have only discrete valued nodes. The number of possible classes of each variable is also shown in figure 2.

The arcs between the nodes show causal dependencies and are quantified by conditional probability matrices which reflect the rules the experts use when making similar decisions. The exact values of their elements are chosen using training data. In order to specify a Bayesian network we need to assign prior probabilities to all root nodes and conditional probabilities for all labels of all non-root nodes given all possible combinations of labels of their parents i.e. direct predecessors. When no prior knowledge is available, equal probabilities are assigned to all possible states of the root nodes.
![img-1.jpeg](img-1.jpeg)

R : Rock Type (permeable, semi-permeable, impermeable)
S : Slope (gentle, middle, steep)
SD : Soil Depth (bare, shallow, deep)
A : Aspect (south, west/east, north)
AG : Animal Grazing (slightly, moderately, heavily grazed)
E : Erosion (low, medium, high)
RP: Regeneration Potential (low, medium, high)
D : Desertification (no/slight, low, medium, high,very high)

Figure 2: The Bayesian network constructed

The network we have is not singly connected, because there exists more than one path between two nodes ( $S D$ and $D$ ). Before we discuss how we deal with this connectivity, we shall give the basic steps by which the beliefs for each of nodes $E, R P$ and $D$ are updated, ignoring the fact that $S D$ influences both $E$ and $R P$ directly. In particular we may for the moment split node

$S D$ into two, each part influencing one only child node as shown in figure 3.
We now demonstrate the propagation equations of the previous section with an example input to the network of figure 3:

At the initial state, before observing any evidence, all $\lambda$ 's are unit vectors since no variable has any observed descendant and therefore no evidence exists to favour any particular state. The root nodes have a $\pi$ equal to their prior probability i.e. $(1 / 3,1 / 3,1 / 3)$ except aspect which has a prior probability $(1 / 4,1 / 2,1 / 4)$ since the second state covers two possible classes (west and east) and therefore does not have equal prior probabilities.

Suppose that $R$ receives evidence indicating permeable rocks. The actual evidence that $R$ receives is represented by a dummy child sending a $\lambda$ message which is of the form $(1,0,0)$ with 1 at the corresponding position indicated by the evidence. This $\lambda$ message is multiplied element by element with the $\lambda$ message received from the genuine child node $E$, which is $(1,1,1,)$. Node $R$ will therefore update its belief using the equation:

$$
\begin{gathered}
B E L\left(R_{\text {perm }}\right)=\alpha \lambda\left(R_{\text {perm }}\right) \pi\left(R_{\text {perm }}\right)=\alpha \times 1 \times 1 / 3=\frac{\alpha}{3} \\
B E L\left(R_{\text {semi }}\right)=\alpha \lambda\left(R_{\text {semi }}\right) \pi\left(R_{\text {semi }}\right)=\alpha \times 0 \times 1 / 3=0 \\
B E L\left(R_{\text {imperm }}\right)=\alpha \lambda\left(R_{\text {imperm }}\right) \pi\left(R_{\text {imperm }}\right)=\alpha \times 0 \times 1 / 3=0
\end{gathered}
$$

Obviously $\alpha$ must be 3 .
![img-2.jpeg](img-2.jpeg)

Figure 3: Bayesian network without loop

After updating its belief, $R$ sends a $\pi$ message to its child $E$ which in this case is equal to its belief i.e. $(1,0,0)$.

Upon receiving this $\pi$ message, $E$ will update its belief using:

$$
\begin{aligned}
B E L\left(E_{i}\right) & =\alpha \lambda\left(E_{i}\right) \pi\left(E_{i}\right)=\alpha \pi\left(E_{i}\right) \\
& =\alpha \pi\left(E_{i}\right)
\end{aligned}
$$

since $\lambda\left(E_{i}\right)=\lambda_{D}\left(E_{i}\right)=1$, for all $i$, i.e the $\lambda$ message that $D$ sends to $E$ is a unit vector since $D$ was not instantiated and the $\pi\left(E_{i}\right)$ is given by:

$$
\pi\left(E_{i}\right)=\sum_{k, l, m}\left[P\left(E_{i} \mid R_{k}, S_{l}, S D 1_{m}\right) \pi_{E}\left(R_{k}\right) \pi_{E}\left(S_{l}\right) \pi_{E}\left(S D 1_{m}\right)\right]
$$

where the summation ranges over all possible values of each parent $R, S$ and $S D 1$. Since we have not yet quantified the matrix $P\left(E_{i} \mid R_{k}, S_{l}, S D 1_{m}\right)$, for all $i, k, l, m$, we will omit writing down equation (8) explicitly. However, the vectors $\pi_{E}(R), \pi_{E}(S)$ and $\pi_{E}(S D 1)$ are equal to $(1,0,0),(1 / 3,1 / 3,1 / 3)$ and $(1 / 3,1 / 3,1 / 3)$ respectively ( $R$ sends its current belief to $E$ whereas $S$ and $S D_{1}$ send as $\pi$ their prior probability). The components of these three vectors are the ones, whose possible product combinations will be used in equation (8). However, the final sum will only include all the product combinations given the permeable state of rocks, since this is the only non-zero element in the vector $\pi_{E}(R)$.

Since $S$ and $S D 1$ represent data nodes and are therefore clamped, their beliefs are not updated and therefore $E$ does not send any $\lambda$ message to these parents. However, it will send a $\pi$ message to its child $D$ given by:

$$
\pi_{D}\left(E_{i}\right)=\alpha B E L\left(E_{i}\right) / \lambda_{D}\left(E_{i}\right)=\alpha B E L\left(E_{i}\right)
$$

i.e. the $\pi$ message that $E$ will send to $D$ will be its belief.

Upon receiving this information $D$ will update its belief using:

$$
B E L\left(D_{i}\right)=\alpha \lambda\left(D_{i}\right) \pi\left(D_{i}\right)=\alpha \pi\left(D_{i}\right)
$$

since $D$ did not receive diagnostic information (i.e. $\lambda$ ), the $\lambda\left(D_{i}\right)=1$, and $\pi\left(D_{i}\right)$ is given by:

$$
\pi\left(D_{i}\right)=\sum_{k, m}\left[P\left(D_{i} \mid E_{k}, R P_{m}\right) \pi_{D}\left(E_{k}\right) \pi_{D}\left(R P_{m}\right)\right]
$$

where the summation ranges over all possible values of each parent $E$ and $R P$. Equation (11) is identical to equation (8) where again we omit the calculation due to the yet undefined matrix involved.

Node $D$ will then send a $\lambda$ to all its parents except the one it received the message from i.e. $E$. So the message that it will send to $R P$ is given by:

$$
\begin{aligned}
\lambda_{D}\left(R P_{i}\right) & =\beta \sum_{m}\left[\lambda\left(D_{m}\right) \sum_{k}\left[P\left(D_{m} \mid E_{k}, R P_{i}\right) \pi_{D}\left(E_{k}\right)\right]\right. \\
& =\beta \sum_{m}\left[\sum_{k}\left[P\left(D_{m} \mid E_{k}, R P_{i}\right) \pi_{D}\left(E_{k}\right)\right]\right. \\
& =1
\end{aligned}
$$

$\lambda\left(D_{m}\right)$ is 1 , for all $m$ and the summation is over all possible values of all parents except parent $R P$, for which we compute the $\lambda$ message for its $i$ th value. Since $D$ did not receive any diagnostic message and was triggered by a $\pi$ message, the $\lambda$ vector send by $D$ to $R P$ is a vector with all its elements 1. Therefore $R P$ will receive a vector which will not alter its belief. This is based on the fact that evidence gathered at a particular node ( $E$ in our case) does not influence any of its spouses $(R P)$ until their common child (i.e. node $D)$ gathers diagnostic support. This is sensible since evidence on rock type should not alter our belief in regeneration potential.

In our network there are two paths between $S D$ and $D$ and in order to handle the loop we used the method of conditioning(reasoning by assumptions) which is based on the ability to change the connectivity of a network and render it singly connected by instantiating a selected group of variables (Suermondt and Cooper 1991, Pearl 1988).

# 5 Coping with Uncertain Data 

If there was no uncertainty in the data, the input data concerning a node should be in the form of hard labeling (Pearl 1988, Olesen at al. 1989). For example the input to a node $S$ of our example network could be of the form $(1,0,0)$ implying that $S$ is labelled gentle with probability 1 and

both other labels are rejected (they have probability zero). In practice, however, data are never certain, even when they are given to us as hard classifications. We shall examine below the various forms of input data and how uncertainty in them can be handled. Then we shall discuss how the parameters of such process may be assessed in a GIS.

# 5.1 Data expressed as a continuous-valued variable 

Quite often a variable in a problem is a real valued function that can be measured directly. This is the case for example of soil depth or aspect. Such data are stored in raster form in the corresponding GIS layer. In the case of continuous variables the way to incorporate uncertainty is relatively straight forward. In this section, we shall show how, if we have a model of the error distribution in the measuring process, this error can be taken into consideration when we define the uncertainty in the data. For simplicity we shall demonstrate our approach assuming Gaussian error distribution.

Assume that we are given a measurement for one of the input nodes of the network of figure 2. If we assume that the input measurement, $\mu$, has an error which is normally distributed with mean, $\mu$, and variance $\sigma^{2}$, then the probability of the input variable belonging to class $i$ i.e. $C_{i}$, given the measurement $\mu$ is given by:

$$
\mathrm{P}\left(C_{i} \mid \mu\right)=\frac{K_{i}}{K}
$$

where

$$
K_{i}=\frac{1}{\sqrt{2 \pi} \sigma} \int_{l_{i}}^{u_{i}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x
$$

and

$$
K=\frac{1}{\sqrt{2 \pi} \sigma} \int_{\min }^{\max } e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x
$$

The $l_{i}$ and $u_{i}$ denote the lower and upper limit of class $i$ respectively and $\min$ and $\max$ denote the minimum and maximum values that the measured variable can take.

After some manipulation we get:

$$
K_{i}=\frac{1}{2}\left\{\operatorname{erf}\left(\frac{u_{i}-\mu}{\sqrt{2} \sigma}\right)-\operatorname{erf}\left(\frac{l_{i}-\mu}{\sqrt{2} \sigma}\right)\right\}
$$

and

$$
K=\frac{1}{2}\left\{\operatorname{erf}\left(\frac{\max -\mu}{\sqrt{2} \sigma}\right)-\operatorname{erf}\left(\frac{\min -\mu}{\sqrt{2} \sigma}\right)\right\}
$$

where $\operatorname{erf}(x)$ is the error function defined by:

$$
\operatorname{erf}(x) \equiv \frac{2}{\sqrt{\pi}} \int_{0}^{x} e^{-t^{2}} d t
$$

# 5.2 Data expressed as class labels 

The formula derived above is appropriate if we are given the value of the measured variable directly. This, however is not usually the case. Quite often the measured variables are quantised grossly and all we are given is a class label of the object stored in vector or raster format. Even when the input data are of discrete nature, there is always some uncertainty associated with them because often this discretization is achieved by measuring a variable that can take continuous values and grossly discretizing it into a few ranges that define the corresponding classes, without taking into consideration the error of the measurement.

In the absence of any information, all we can assume is that the measured variable could equally likely have been any of the values in the range of values that characterise the particular class. In other words, in terms of the notation introduced above, all we can say is that $\mu$ has a uniform probability density function in the range $\left(l_{i}, u_{i}\right)$. Then we can calculate the probability of the object to belong to any class $C_{j}$ as follows:

$$
P\left(C_{j} \mid l_{i}<\mu<u_{i}\right)=\int_{l_{i}}^{u_{i}} P\left(C_{j} \mid \mu\right) P(\mu) d \mu
$$

The above formula can be easily derived as follows:

$$
P\left(C_{j} \mid l_{i}<\mu<u_{i}\right)=\frac{P\left(l_{i}<\mu<u_{i} \mid C_{j}\right) P\left(C_{j}\right)}{P\left(l_{i}<\mu<u_{i}\right)}
$$

$$
=\frac{P\left(C_{j}\right) \int_{l_{i}}^{u_{i}} P\left(\mu \mid C_{j}\right) d \mu}{\int_{l_{i}}^{u_{i}} P(\mu) d \mu}
$$

Assuming that $\mu$ is uniformly distributed over the range $\left[l_{i}, u_{i}\right]$, the integral in the denominator is equal to 1 and the equation becomes:

$$
\begin{aligned}
P\left(C_{j} \mid l_{i}<\mu<u_{i}\right) & =P\left(C_{j}\right) \int_{l_{i}}^{u_{i}} P\left(C_{j} \mid \mu\right) P(\mu) / P\left(C_{j}\right) d \mu \\
& =\int_{l_{i}}^{u_{i}} P\left(C_{j} \mid \mu\right) P(\mu) d \mu
\end{aligned}
$$

which gives equation 19. Now substituting equation 13 into this equation and assuming a uniformly distributed $\mu$ as before we can obtain the probability of the variable to be in class $j$, i.e. $C_{j}$, given that the measuring process indicated class $i$, i.e. $C_{i}^{\prime}$, by:

$$
P\left(C_{j} \mid C_{i}^{\prime}\right)=\frac{1}{u_{i}-l_{i}} \int_{l_{i}}^{u_{i}} \frac{K_{j}}{K} d \mu
$$

Thus, the probability of a variable to belong to class $i$ instead of being taken as equal to 1 (after the evidence), is set to:

$$
P\left(C_{i} \mid C_{i}^{\prime}\right)=\frac{1}{u_{i}-l_{i}} \int_{l_{i}}^{u_{i}} \frac{K_{i}}{K} d \mu
$$

An exact solution to the above integral is difficult to be obtained. Therefore, standard numerical integration techniques have been employed in order to obtain a satisfactory approximate solution.

# 5.3 Data not obviously related to a continuous-valued variable 

Some of the data pertaining to a problem may not be easily associated with a measurable continuous variable. Such data are for example, rock type and human influence and they are stored in vector format. Although not obvious, both these data, in spite of the fact that they are expressed by linguistic descriptors, they can still be quantified. For example, there are models now being developed that attempt to quantify human influence by the number of cattle heads in

the region, or by the distance from the nearest road or town, the population density, etc. If such a model is available, the uncertainty in this variable can be expressed by one of the methods described in section 5.1 and 5.2.

Rock type on the other hand cannot really be mapped on the real axis. However, the property of rock type that is relevant to a particular problem may be. For example, if what enters into the reasoning process is not directly the rock type, but the property of rocks in terms of their water permeability, then this is a measurable quantity that can be mapped on the real axis. Rock permeability ranges from $10^{-1} \mathrm{~m} / \mathrm{sec}$ for pebble beds down to $10^{-12} \mathrm{~m} / \mathrm{sec}$ for granites. The three classes of permeability are roughly characterised by the following ranges of this value:

- impermeable: $10^{-12} \mathrm{~m} / \mathrm{s}-10^{-8} \mathrm{~m} / \mathrm{s}$
- semi-permeable: $10^{-8} \mathrm{~m} / \mathrm{s}-10^{-5} \mathrm{~m} / \mathrm{s}$
- permeable: $10^{-5} \mathrm{~m} / \mathrm{s}-10^{-2} \mathrm{~m} / \mathrm{s}$

One can envisage that now we have mapped this property of the rocks on the real axis, we can apply the method of section 5.1 to define the uncertainty associated with it. In this particular case however, the range of values is so large that uncertainty in the measurement is probably of secondary relevance. The most significant uncertainty probably stems from the intrinsic variability of the properties of the particular rocks, rather than the measuring process. For example, hard limestones could be characterised by permeabilities anywhere between $10^{-4}$ and $10^{-10}$ depending on the amount of solution features they contain. This uncertainty should be the one we model in this case rather than the uncertainty in the measuring process.

# 5.4 Application to the constructed network 

Most of the networks considered deal with either continuous or discrete variables. This is because of the restriction that continuous parents must have continuous children. In the case of our network, we would like to have as continuous variables only the input (data) nodes but not the intermediary ones, since some of these variables cannot take continuous values. Therefore,

we formed a network with only discrete variables. To accommodate for input variables of continuous nature, we can imagine that our network has an extra layer of input nodes each linked to one of the existing root nodes. These new parent nodes will now form the new set of roots in the modified Bayesian network. These parents will represent the input as obtained using the GIS input data with a possible error. So the new set of root variables will consist of nodes $R^{\prime}, S^{\prime}, S D^{\prime}, A^{\prime}$ and $A G^{\prime}$ were the $\left({ }^{\prime}\right)$ represents the given input.
![img-3.jpeg](img-3.jpeg)

Figure 4: Bayesian network constructed

Each one of these roots will be linked with the corresponding variable which will represent the actual variable i.e. the variable after the incorporation of uncertainty or error in the measuring process. These variables consist of the nodes $R, S, S D, A$ and $A G$. As it can be seen from figure 4 we added 5 extra nodes and 5 more arcs. We therefore need to construct 5 more conditional probability matrices, one for each arc. Each of these matrices will be of dimension $3 \times 3$. An example of an entry in the second matrix, which relates the ideal slope with the one given, would be: $P\left(S=\right.$ steep $\left|S^{\prime}=\right.$ steep $)$ which is the probability of slope being steep given that the measuring process indicated steep.

Assume for example, that we are given by the source that slope is steep. We then input at node $S^{\prime}$ a vector $(0,0,1)$ with 1 at the position indicated by the data. The belief that slope is indeed steep, i.e. $B E L(S=$ steep $)$, will be the probability of slope being steep, given that the measuring process indicated steep i.e. $P\left(S=\right.$ steep $\left|S^{\prime}=\right.$ steep $)$, i.e. the corresponding entry of the conditional probability matrix relating $S$ to $S^{\prime}$. This is the actual value that will get propagated downwards. This value is given by equation 21.

This trick is needed because in a classical Bayesian network with hard classification input, confidence in the input data can be altered by the evidence propagation procedure. In our case we want to avoid that. As long as we realize it, we can input our data directly to the unprimed parent nodes in the form of soft classification which is not to be altered during the reasoning process. So figure 4 is only a conceptual structure, and in practice instead of changing the network structure, we modify the beliefs of the input nodes of the original network, so that the belief will be set according to the error estimation.

Another general issue is the way we choose the uncertainty level. For the case of continuous valued variables we tried to refer everything to one number. For example, we choose the $\sigma$ of the variable coming from the most reliable source in such a way that the confidences in each class were almost hard. Then we chose the standard deviations of the error of the less reliable variables to be multiples of the previous value appropriately scaled to take into account the fact that the variables are measured by different units in different scales. These multiplication factors were chosen according to linguistic expressions of opinion by experts, in the form "I say that soil depth is twice as unreliable as aspect" and also by tuning the network to agree with the experts' opinion in the assessment of some training sites.

For each region we have the DEM data with $20 \mathrm{~m} \times 20 \mathrm{~m}$ resolution. From these we calculate the aspect and slope. Aspect is expressed as the angle between the normal to the ridge and the north direction. This is expressed in positive degrees form 0 to 360 measured clockwise from the north. Aspect is therefore represented by a circle starting clockwise from the north and completing 360 degrees, as:

- North: $0^{\circ}-45^{\circ}$
- West: $45^{\circ}-135^{\circ}$
- South: $135^{\circ}-225^{\circ}$
- East: $225^{\circ}-315^{\circ}$
- North: $315^{\circ}-360^{\circ}$

Due to the nature of these boundaries (non continuous), we created for our network, the following classes together with the limits which apply only to half the circle as follows:

- South: $180^{\circ}-225^{\circ}$
- West/East: $225^{\circ}-315^{\circ}$
- North: $315^{\circ}-360^{\circ}$

Any measurements, $\mu$, that fall below 180 degrees, are taken as $360-\mu$.
Slope is calculated by the tangent of the given slope angle times 100 i.e. $\tan \theta \times 100$ where $\theta$ is the slope angle calculated from the DEM data. The three classes of slope are:

- Gentle: $0 \%-20 \%$
- Middle: $20 \%-40 \%$
- Steep: $40 \%-x$

The GIS data regarding both variables are available in the form of measurements. For each measurement, $\mu$, of each of the variables we have associated with it a standard deviation $\sigma$. Since the two variables (namely slope and aspect) were obtained from the most accurate source, we assign a $\sigma$ which will indicate high confidence in the data. Therefore we set $\sigma=2$ for slope and set a $\sigma$ for aspect which is equivalent to that of slope, appropriately scaled to correspond to the range of values of aspect. Therefore $\sigma$ of aspect is estimated to be 9 . Since the measurement is given, we apply equation 13. This will give the probability of each class of each variable given the measurement, i.e. $P\left(C_{i} \mid \mu\right)$ which is effectively the belief in that class, i.e. $B E L\left(C_{i}\right)$. This is shown diagrammatically by figures 5a to 5c.

Figure 5a represents the belief in the variable, slope say, before the uncertainty i.e. $B E L\left(S^{\prime}\right)$. It is represented by the belief vector $(0,1,0)$ with 1 at the position being indicated by the measurement. The $\tau_{1}$ and $\tau_{2}$ are the bounds of the class indicated. Now, we assume that this input measurement has an error which is normally distributed with mean $\mu=$ measurement and

variance $\sigma^{2}$ as shown in figure 5b. This is the Gaussian which we integrate in equations 14 and 15 to obtain equation 13. Equation 13 will give the belief in each class of the actual variable, i.e. $B E L(S)$, which is shown diagrammatically by figure 5c.
![img-4.jpeg](img-4.jpeg)

Figure 5: Belief distribution of slope assuming (a) no uncertainty and (c) uncertainty according to the probability density function (b)

For the other two variables soil depth $(S D)$ and rock type $(R)$, the GIS data indicated the particular class to which each variable belonged.

Soil depth, measured in centimeters (cm), is divided into the following three classes according to experts:

- Bare: $0 \mathrm{~cm}-5 \mathrm{~cm}$

- Shallow: $5 \mathrm{~cm}-30 \mathrm{~cm}$
- Deep: $30 \mathrm{~cm}-\infty$

The GIS data indicate the class that each pixel belongs to and therefore we apply equation 20 to calculate the belief in $S D$ after the incorporation of uncertainty. We choose a $\sigma=2.5$ for this variable which is twice the sigma taken for slope and aspect, scaled accordingly. This is due to the fact that soil depth is less accurate than the slope and aspect which are obtained from DEM data. The fact that we set a sigma twice as that of slope and aspect is justified a posteriori by the training data (i.e. the sites whose desertification risk is known) which are used to tune the parameters of the network.

The possible rock types for our problem were:

- Hard Limestones
- Mica Schists
- Metamorphic
- Calcareous tertiary deposits
- Siliceous tertiary deposits
- Colluvium

Out of these types, mica schists and metamorphic rocks, are definitely considered as impermeable, whereas hard limestones, colluvium and tertiary deposits are on the boarder between permeable and semi-permeable. In the first case we set the belief of rock permeability to $(0,0,1)$ with 1 at the impermeable state and in the second case we set the belief of rock permeability to $(0.50,0.50,0)$ with equal probability in the given rock being permeable and semi-permeable.

# 6 Coping with Uncertainty in the Rules 

The propagation of information in the network relies on the conditional probabilities concerning the nodes that are related to each other by explicit causal relations. In this paper we also present a novel methodology for constructing the conditional probability matrices for use by the Bayesian network to perform the inference. A conditional probability matrix such as $P(A \mid B, C)$ can be represented by a table with one entry for each possible combination of the states of the variables $A, B$ and $C$. However, when the number of parents is large or/and when the number of possible states of the participating variables is large, then direct elicitation of such a table is difficult because the required data grows exponentially with the number of variables involved. There have been nevertheless proposed some approximation techniques of this conditional probability $P(A \mid B, C)$ from pairwise relations such as $P(A \mid B)$ and $P(A \mid C)$ (Kim and Pearl 1987, Kim and Pearl 1983). The most common model of this type is disjunctive interaction (the "noisy OR-gate") (Pearl 1988). The basic theory behind this is that any member of a set of conditions is likely to cause a certain event and this likelihood does not diminish when several of these conditions exist simultaneously. However disjunctive interaction is based on some assumptions which are only true in some cases. Other methods of estimating the conditional probability matrices are ad hoc based on expert rules (Henrion 1989, Haas 1991).

For the network of the size presented here these conditional probabilities are expressed by a $3 \times 3 \times 3 \times 3$ matrix, the elements of which have to be specified. For example, one element of the conditional probability matrix relating erosion to its parent variables i.e. rock permeability, slope and soil depth would give the conditional probability of erosion to be in a particular state given the states of each of the three influencing variables. There is no mention in the literature how the elements of this matrix can be specified in practice.

There are some geophysical phenomena, however, for which either an analytic model exists in the form of an equation that has been deduced from careful consideration of the underlying physical processes, or an equation has been defined in an empirical way to express quantitatively observations and expertise built up over the years. We shall demonstrate here how the elements

of the conditional probability matrix can be defined when such an equation is available. We shall also discuss what can be done when no such equation is available.

# 6.1 When an analytic equation relating causes to effects is available 

We will demonstrate here a way to specify the independent elements of the conditional probability matrix of erosion which will take into account not only the relationship between a child node and its parents but also the importance that each of the parent variables bares on the child. This is possible because an analytic formula exists that expresses quantitatively the relationship between erosion and the factors that affect it. The formula used here is the one proposed by Stehlik (Morgan 1986) and is very similar to the Universal Soil Loss Equation (USLE) and is as follows:

$$
\text { mean annual soil loss }=D \cdot R \cdot P \cdot S \cdot L \cdot O
$$

where $D$ is the climatic factor which in our case is assumed to be constant over the whole study area, $R$ is the petrological factor and assesses the rock type according to the permeability of its weathered debris and $P$ expresses the erodibility of the soil. $P$ is related to soil depth which is inversely related to erosion. Deep soils, for example, due to their larger water storage capacity, are less sensitive to erosion than shallow soils. The way we incorporate soil depth into this erodibility factor is to assume that for a constant type of soil in the study area, soil depth and soil erodibility are related using a linear function. We can assume this linear function since we are only interested in a specific, small range of soil depth in which a more or less linear relationship between the two may be assumed. (As long as the range of the independent variable is small, any non linear function can be approximated by a linear one.). In this way we derive a function that will give us $P$ given the depth of the soil. $S$ and $L$ are the slope steepness and length factor respectively. The length factor may be assumed constant over all the sites. $S$ is given by:

$$
S=0.24+0.106 s+0.0028 s^{2}
$$

where $s$ is the slope in per cent.

$O$ in equation 22 is the vegetation cover which is dependent upon the percentage cover. In our case $O$ is constant since the area of interest is burned and therefore there is no vegetation cover. Thus for our problem this formula is simplified as follows:

$$
\text { mean annual soil loss }=f(S, R, P)=\alpha \cdot R \cdot S \cdot P
$$

where $\alpha$ is a constant and $P$ represents erodibility of the soil which is a function of soil depth. In order to estimate the constant $\alpha$ we will need to estimate $D, L$ and $O$ from equation 22 . We know that $D$ is expressed in terms of the mean annual precipitation, $r$, using the equation:

$$
D=0.0014 r-0.38
$$

In our study area we know $r$ to be constant to 437 mm and therefore we estimate $D=0.23 . O$ is constant equal to 4 since this corresponds to 0 percentage cover and $L$ is constant equal to 1 which corresponds to 20 m length of slope. We therefore derive $\alpha=0.92$.

Each one of these variables $f, R, S$ and $P$ has three possible states or classes corresponding to the three classes of each one of the variables $E, R, S$ and $S D$ in the network. Assume that we denote the lower and upper boundaries of a certain class of a node by subscripts 1 and 2 .

Now assume that we want to estimate the conditional probability of erosion belonging to a certain class given the classes of the variables that it depends on. This conditional probability clearly can be estimated by evaluating the following formula:

$$
P(e \mid r, s, s d)=\frac{\int_{R_{1}}^{R_{2}} \int_{S_{1}}^{S_{2}} \int_{P_{1}}^{P_{2}} u\left(f(S, R, P)-E_{1}\right) * u\left(E_{2}-f(S, R, P)\right) d S d R d P}{\left(R_{2}-R_{1}\right) *\left(S_{2}-S_{1}\right) *\left(P_{2}-P_{1}\right)}
$$

where small letters for the variables mean their actual assigned class labels and $u$ is a heaviside function which is equal to 1 when its argument is positive and 0 otherwise.

The above formula seems pretty straight forward and in principle one can calculate the integrals analytically and derive an expression which for given values of the class boundaries will yield the value of the conditional probability. However, in practice the analytic calculation of the triple integral is prohibitively complicated for the general case due to the great number of

possible cases one has to consider. Thus, we estimated the above probabilities by the Monte Carlo method: For each possible combination of classes of the arguments of the conditional probability we drew 40000 samples uniformly distributed over the volume $\left[R_{1}, R_{2}\right],\left[S_{1}, S_{2}\right]$ and $\left[P_{1}, P_{2}\right]$. The number of samples that make the integrand in the numerator in equation 23 non-zero divided by the total number of samples drawn is an estimate of the conditional probability. Table 1 gives the entries of this matrix calculated as described above. Each entry gives the conditional probability of erosion being in one of the states low, medium and high ( $L, M$, $H$ respectively) given the states of the three variables as shown in the first three columns.

We follow the same procedure for all possible combinations of states of $E$ and its parents in order to complete the whole conditional probability matrix.

# 6.2 When no analytic formula is available between causes and effects 

When no analytic formula exists between causes and effects, one has to deduce the elements of the conditional probability matrix using training data and expert rules expressed in vague linguistic terms. This is the case for assessing the regeneration potential of a forest and its risk of desertification.

No quantitative formula exists that relates the regeneration potential to its contributing factors. One can easily reason and derive one such formula but to our knowledge there are no detailed studies done which would allow us to calculate, for example, the constants that will appear in it. This situation is similar regarding the dependence of the factor of desertification on the regeneration potential and erosion. Thus, for the calculation of the elements of these matrices appropriate numbers had to be chosen to reflect the rules followed by the experts, namely:

1. The more soil, the more seeds and more nutrition and therefore the higher the potential of a forest to regenerate naturally.
2. The way the land surface area is oriented towards the sun affects the amount of radiation it receives. South facing aspects due to the higher amounts of heat they receive from the sun, tend to be drier. On such slopes natural vegetation is usually sparser compared to

vegetation on north-facing aspects.
3. The more animals that graze the land, the lower the potential to regenerate.
4. The higher the erosion, the higher the desertification risk.
5. The lower the potential of an area to regenerate, the higher the risk of desertification. We are also given that this factor influences desertification more than erosion.

The above general rules were used to give some initial values to the elements of the conditional probability matrix, interpreting that high means $80 \%$ confidence, low means $20 \%$ confidence and so on. Then these values were tuned using training sites for which the experts' (hard) classification was available. It must be noted that ideally this tuning should be done using historical data where the state of a number of sites is compared with the state predicted by he experts some years earlier and statistics are performed. However, in view of the lack of such data one can only tune the parameters in such a way that the systems' assessment agrees with that of the expert in as many sites as possible.

# 7 Experimental Results 

In this section we will present the results of the network when applied on 53 sites using GIS data. We have implemented Pearl's propagation algorithm in C. We then compare our method with the results obtained using the GIS data with reasoning in the form of IF-THEN rules i.e. ignoring the uncertainty. In each case we compare the results with the expert's classification which was based on field data.

### 7.1 Reasoning using the Bayesian network

The inference mechanism described above could be applied either at pixel or, preferably, at region level. The latter would obviously make the algorithm faster. At whatever level it is applied, it is necessary for the entity that has to be classified to have uniform attributes. For example, our method could not be applied to a region consisting partly from south looking slopes and partly from west looking slopes. In that case fuzzy logic would have been more appropriate, as fuzzy logic deals with partial membership to various classes. Thus, to apply our inference mechanism to the region level, some preprocessing is needed: As each layer of


Table 1: Conditional probability matrix for erosion.

the GIS has different tessellation of the land into polygons, a composite tessellation must first be created by considering a union of all polygons in all layers. This way each small polygon created will have a unique set of attribute classes or measurements which can be fed into our system to assess its risk of desertification. In our case, part of the data, i.e. aspect and slope, were given in raster format. Thus, the smallest "polygon" we had was a single pixel and that is why we had to apply our system at a pixel level.

The final classification of a site was performed by averaging the corresponding probabilities of the site pixels.

There are 5 possible desertification classes:

- Class 1 : Sites without any risk of desertification after a forest fire
- Class 2 : Sites with a low risk of desertification
- Class 3 : Sites with a moderate risk of desertification
- Class 4 : Sites with a high risk of desertification
- Class 5 : Sites with a very high risk of desertification

All sites have been classified by an expert using ground data.
Out of the 53 available sites, 39 sites were used for training and 14 sites were used for testing the final system. Table 2 shows the results of the 39 sites using GIS data with uncertainty. Table 3 shows the results of the 14 test sites using GIS data with uncertainty. Using GIS data the system agreed with the expert on 28 out of the 39 training sites, with the majority of the misclassified sites falling into the adjacent classes. Out of the 14 test sites, 8 agreed with the expert. The sites that were correctly classified are indicated by a " $\sqrt{ }$ " in the last column of the tables. We have also tested the system on the 53 sites using GIS data with no uncertainty. In this case, for slope and aspcet we calculated the mean slope and aspect of each site and classified it by inputting $100 \%$ probability to the class it fell in. For the rest of the variables we gave again $100 \%$ probability to the class indicated. When tested with these certain input, the system agreed with the expert on 28 out of the 53 sites.

# 7.2 Rule-based reasoning 

We compare our results with those obtained when reasoning without uncertainty, but simply performing inference using IF-THEN rules.

An example of such a rule is:


So for each pixel in each site we test to see if the premises of a rule are satisfied in order to draw a conclusion. We then classify the site according to the classification of the majority of the pixels.

For the raster data available for slope and aspect we simply classify them according to which class range the measurement falls. The rest of the data were already in classes. Out of the total of 53 sites $18(13 / 39+5 / 14)$ agreed with the expert's classification. Results on the 39 sites are shown again in table 2. The classification of the 14 sites is shown in table 3. In both tables agreement with the experts is indicated with a " $\bullet$ " in the last column.

The lower accuracy observed when reasoning with IF-THEN rules lies in the fact that hard labellings were used thus ignoring the degree of uncertainty in the GIS data. This should not be the case since the degree of belief in the input is significant for determining the output. Although the classification of the input may suggest the class to which the output belongs, when we have degrees of beliefs attached to these input variables we may end up with a different output classification. This is why probabilistic reasoning with a Bayesian network gives better results. By including uncertainty only in the inference (i.e. using Bayesian network with certain data) still we have better results than by ignoring any sort of uncertainty and applying rule-based inference. However the best results are obtained by incorporating uncertainty in the data as

well as in the inference.
Another notable advantage of the Bayesian network over the traditional IF-THEN inference is that we can include in the structure of the network variables which latter on can leave uninstantiated in case of lack of information. For example, in the network created for this particular application we have included the variable animal grazing which although affects the potential of an area to regenerate, there were no data available for input from the GIS. So when performing the propagation one can leave this variable uninstantiated, as in our case. If we later on receive some information regarding this variable we can simply input it in the network. In contrast, in IF-THEN reasoning any variables on which we do not have information are omitted from the rules. Therefore any future available information on this variable will require altering the rule base and constructing new rules to account for the new variable.

# 8 Discussion and Conclusions 

In this paper we have shown how a Pearl Bayes network was constructed for the purpose of fusing information in a GIS systems. The information includes data of different resolution and accuracy. It was therefore necessary for the system to be able to reason with uncertainty.

We have presented techniques to handle data input as raw measured values or as class memberships. We also discussed ways of dealing with data in vector or raster form.

The designed system was tested on 53 sites using the GIS data assuming uncertainty with promising results. The majority of the misclassified sites were not given a completely wrong classification but rather a classification into a neighbouring class. This is expected due to the discrepancy between field and GIS data. Results also show that reasoning with uncertainty using a Pearl Bayes network performed significantly better than rule-based reasoning of the IF-THEN form. Results of the Baysian network with certain data also performs better than rule-based reasoning since it still applies some uncertainty in the inference. However, results showed that the incorporation of uncertainty in the data is also essential in order to get satisfactory results. This proves the fact that the confidence with which a label is assigned is significant in deriving

the correct conclusion. The incorporation of uncertainty also provides the additional information on how probable the alternative labels are.

To summarise, we believe that the major contributions of this work are:

- It showed how artificial intelligence techniques can successfully be applied to geographical issues. More specifically, how a Bayesian network can be used as a tool for performing probabilistic reasoning in a GIS.
- It presented a technique for introducing uncertainty not only in the knowledge provided but in the input data as well, which in most cases are obtained from various sources with varied degrees of reliability.
- It presented a novel methodology for obtaining the parameters to be used by the system in case a formula exists relating the connected variables. We believe that this is particularly useful since the quantification of the Bayesian network, still remains a largely unexplored area.


# Acknowledgements 

This project was funded by the Council of European Communities, under the Environment programme, contract EVSV 0025. The authors are grateful to Dr G. Nakos of The Institute of Mediterranean Forest Ecosystems, Greece, for providing the data and supplying the expert knowledge. Professor D. Rokos and Dr. V. Andronis of the National Technical University of Athens are also gratefully acknowledged for repeatedly providing the GIS data.
