# HAL open science 

## Cerebral modeling and dynamic Bayesian networks

Vincent Labatut, Josette Pastor, Serge Ruff, Jean-François Démonet, Pierre Celsis

## To cite this version:

Vincent Labatut, Josette Pastor, Serge Ruff, Jean-François Démonet, Pierre Celsis. Cerebral modeling and dynamic Bayesian networks. Artificial Intelligence in Medicine, 2004, 30 (2), pp.119-139. 10.1016/S0933-3657(03)00042-3 . hal-00634307

## HAL Id: hal-00634307 <br> https://hal.science/hal-00634307v1

Submitted on 20 Oct 2011

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Cerebral modeling and dynamic Bayesian networks 

Vincent Labatut, Josette Pastor, Serge Ruff, Jean-François Démonet, Pierre Celsis

INSERM Unité 455, Pavillon Riser, CHU Purpan, F-31059 Toulouse Cedex 3, France

## Corresponding author:

Dr Josette Pastor,
Telephone number: 33 (0) 561779500
Fax number: 33 (0) 561499524
Email address: josette.pastor@toulouse.inserm.fr

## Proofs should be sent at:

INSERM Unité 455, Pavillon Riser, CHU Purpan, F-31059 Toulouse Cedex 3, France


#### Abstract

The understanding and the prediction of the clinical outcomes of focal or degenerative cerebral lesions, as well as the assessment of rehabilitation procedures, necessitate knowing the cerebral substratum of cognitive or sensorimotor functions. This is achieved by activation studies, where subjects are asked to perform a specific task while data of their brain functioning are obtained through functional neuroimaging techniques. Such studies, as well as animal experiments, have shown that sensorimotor or cognitive functions are the offspring of the activity of large-scale networks of

anatomically connected cerebral regions. However, no one-to-one correspondence between activated networks and functions can be found.

Our research aims at understanding how the activation of large-scale networks derives from cerebral information processing mechanisms, which can only explain apparently conflicting activation data. Our work falls at the crossroads of neuroimaging interpretation techniques and computational neuroscience.

Since knowledge in cognitive neuroscience is permanently evolving, our research aims more precisely at defining a new modeling formalism and at building a flexible simulator, allowing a quick implementation of the models, for a better interpretation of cerebral functional images. It also aims at providing plausible models, at the level of large-scale networks, of cerebral information processing mechanisms in humans.

In this paper, we propose a formalism, based on dynamic Bayesian networks, that respects the following constraints: an oriented, networked architecture, whose nodes (the cerebral structures) can all be different, the implementation of causality - the activation of a structure is caused by upstream nodes' activation -, the explicit representation of different time scales (from one millisecond for the cerebral activity to many seconds for a PET scan image acquisition), the representation of cerebral information at the integrated level of neuronal populations, the imprecision of functional neuroimaging data, the nonlinearity and the uncertainty in cerebral mechanisms, and brain's plasticity (learning, reorganization, modulation). One of the main problems, nonlinearity, has been tackled thanks to new extensions of the Kalman filter. The capabilities of the formalism's current version are illustrated by the modeling of a phoneme categorization process, explaining the different cerebral activations in normal and dyslexic subjects.

# Keywords 

Computational Neuroscience; Functional Neuroimaging; Dynamic Bayesian Networks; Large-scale Networks

## 1. Introduction

The understanding and the prediction of the clinical outcomes of cerebral lesions, as well as the assessment of rehabilitation procedures, necessitate identifying the cerebral substratum of cognitive or sensorimotor functions, and understanding the information processing mechanisms that are implemented by the substratum and underlie the functions.

In humans, the substratum identification can be only addressed indirectly, traditionally with the clinical anatomical method that establishes the relationships between cerebral lesions and functional deficits, and currently, mainly by activation studies where subjects are asked to perform a specific task while data of their brain functioning are collected through functional neuroimaging techniques. A direct evidence of the brain / mind link can only be obtained in patients, during preoperative situations. Activation studies, as well as animal experiments, have shown that sensorimotor or cognitive functions are the offspring of the activity of large-scale networks of anatomically connected cerebral areas [1,9,27,42].

Knowing the cerebral substratum of a cognitive function is necessary, although not sufficient, to be able to make a precise diagnosis of a functional deficit, or an accurate prognosis of the clinical outcome of a lesion. The main point is interpreting functional

neuroimaging data as the result of information processing at the integrated level of large-scale networks. At this level, cerebral mechanisms are the synthesis of more basic neurobiological, neurophysiological or neuropsychological processes. They can only be approached with the help of computational models, based on the knowledge of more basic processes.

Although research in neuroscience is quickly evolving, definitive answers, either on the cerebral substratum of any cognitive function or on the integrated cerebral mechanisms, are yet unknown. Moreover, knowledge on basic cerebral processes is partial and scattered in various studies, from molecular research to animal experiment and human psychological studies. A modeling approach for the interpretation of functional neuroimaging data should therefore meet three requirements: 1) represent explicitly cerebral information and mechanisms at the integrated level of large-scale networks, 2) integrate different sources of data and knowledge and 3) design models able to evolve rapidly with new findings in neuroscience.

Currently, most models originate either in neuroimaging, and they are based on statistical techniques, or in computational neurosciences and cognitive modeling, and they use connectionist and/or AI-based methods.

# 1.1. The neuroimaging approach 

For a given cognitive task, traditional interpretation methods of functional neuroimaging data allow a spatial or temporal localization of cerebral activation. The so-called segregative method, used for tomographic techniques (functional Magnetic Resonance Imaging (fMRI), Positron Emission Tomography (PET)), aims at independently localizing the areas involved in the task performance, i.e. at knowing

where the function is implemented [22,23]. Electromagnetic surface techniques (electroencephalography (EEG), magnetoencephalography (MEG)) focus mainly on temporal localization, i.e. they uncover and date cerebral events [26]. Although they can answer indirectly to the where with the help of source detection methods, their major concern is when the brain performs specific processes.

More recently, more powerful methods have been designed to take the relationships between different cerebral structures involved in the same cognitive task into account. Functional connectivity [30,31] allows studying the covariation of the activation between some areas thanks to factorial analysis methods. The uncovered relationships are strictly functional and may be a clue, but certainly not a proof, of the existence of a direct anatomical link between structures, since they may reflect only the existence of indirect neuroanatomical pathways. The technique gives then a sketch of what the network of cerebral areas activated is, for a given cognitive or sensorimotor function. Effective connectivity [10,31] aims at understanding the role of anatomical connections in the activation propagation, that is why the activation of an area can affect a cerebral structure, connected downstream with it. However, the strictly statistical use of structural equations allows reversing the mathematical relationship carried by an oriented anatomical link, therefore canceling the link orientation. In addition, by definition of structural equations, the technique bans the direct modeling of non-linear relationships.

Thus, interpretation methods associated to functional neuroimaging techniques can answer the where, when, what and why of cerebral activation. Clearly, they do not answer how the activation of large-scale cerebral networks derives from the brain's structural properties, i.e. neuroanatomy and cerebral connectivity, and from its

functional characteristics, the cerebral information processing mechanisms. Knowing the how, that is the link between function and activation, is necessary to alleviate apparent contradictions in activation data, and make functional neuroimaging a more dependable diagnosis and prognosis aid.

# 1.2. The viewpoint of computational neuroscience and cognitive modeling 

The how is the main goal of each model developed in the field of computational neuroscience. Currently, most existing works in the domain are based on a connectionist approach (formal neural networks), with varying levels of biological plausibility and different levels of representation.

At the highest level of biological plausibility, the goal is the understanding of basic physiological processes in a limited cerebral structure, for example the neuronal oscillations emerging, in the hippocampus, in small networks of specific neurons, such as pyramidal cells [67] or GABAergic inter-neurons [69]. In this case, mathematical models of biochemical and electrical properties are provided at the level of individual cells and cell-to-cell connections. Although these models give some insight of the different synchronous rhythms in the EEG signal, they do not really allow interpreting it in terms of information processing.

At intermediate levels, the decrease of biological plausibility in the cellular representation is counterbalanced by the integration of more structural features, and models move towards a more cognitive interpretation of the functioning of cerebral structures. The levels of biological accuracy and cognitive precision may be very different in those models. For example, the links between thalamocortical dynamics and

vision may be explored in a more physiological [39,40] or a more functional [28] way. In the first case, neurons, represented by their integrated electrical properties (membrane potentials, channel conductance), are embedded in large, neuroanatomically plausible networks, where cerebral organization (e.g. laminae), and connectivity patterns between and within cerebral structures, are described [39]. The model aims at understanding thalamocortical synchrony, under two aspects, its underlying biological mechanisms, and its role in pattern-selective responses in the cortex [40]. In the second case [28], the model departs further from neurobiology, in order to be more representative of the computational characteristics of the brain. The formal neurons, and their connections, are considered as the functional abstraction (e.g. sensitivity to stimulus' features) of pools of specific biological cells, and of the role (e.g. inhibitory) of real anatomical pathways. The model aims at explaining the role of thalamocortical functional mechanisms on the perceptual McCullough effect [28].

Such models, based on architectural and processing properties of the brain, are dominantly used in computational neuroscience [8,41,61,62]. Some of them are based on detailed architectural features, such as cortical columns [29], and/or on complex biological processes, such as the study of the role of dopaminergic modulation on working memory [19] or learning and planning [65].

Neural networks can also be built considering only functional properties and behavioral data $[13,33,38]$, that is considering the mind as an emerging set of cognitive functions independent of the biological substratum. With this purely functional point of view, other methods have been successfully used. Symbolic AI has focused on the modeling of high level cognitive processes such as memory [2,43,54,59,60] or on frameworks for a global representation of the mind [44]. More recently, Bayesian

networks have been used to model visuomotor mechanisms [24], which demonstrates the utility of graphical probabilistic formalisms for cerebral functional modeling.

At the center of image interpretation, are the question "how the activation of largescale networks derives from cerebral information processing mechanisms" and the necessity to provide models explicit enough to be directly used for clinical purpose. Above methods do not meet these requirements. Indeed, physiological modeling [39,40,67,69] derives neuronal activation from biological mechanisms, computational neuroscience $[8,19,28,29,41,61,62,65]$ describes how basic cognitive functions emerge from neuronal activation, and cognitive modeling $[2,13,24,33,38,43,44,54,59,60]$ is not concerned with cerebral plausibility.

Although some works in physiological modeling [66] or computational neuroscience [4] model the relationships between neuronal activity and cerebral activation measured by tomographic techniques, causal connectivity [50] only answers the question and meets the necessity. However, the underlying formalism [49,50], causal qualitative networks based on interval calculus, limits severely the biological plausibility of the models, since it cannot represent major features, such as learning or the non-linearity and the uncertainty of cerebral processes.

In the following we demonstrate how we tackle the problem of the interpretation of functional images for a clinical purpose. In section 2 we briefly describe large-scale cerebral networks, and the constraints imposed both by the need to comply with our goals and by a biologically plausible modeling approach. We show how dynamic Bayesian networks seem the best modeling paradigm. Section 3 deals with the characteristics of our formalism and illustrates its capabilities by an example. Section 4

discusses the advantages and drawbacks of our methodological choices. Finally, we conclude with some perspectives.

# 2. Large-scale cerebral networks 

### 2.1. A networked structure

Activation data, as well as animal experiments, suggest that the neurological base of a cognitive or sensorimotor function is a large-scale network of cortical or subcortical regions $[1,9,15,27,42,58]$, anatomically interconnected through oriented axon bundles. Moreover, studies in animals show the complex connectivity patterns between the regions $[1,27,58]$.

Clinical observations, as well as activation studies in humans [18,55], show that there is no one-to-one correspondence between activated networks and high level functions. In other words, one network can implement several functions, and one function can be implemented by several networks. The first may be explained by the fact that a large-scale network can be the aggregation of parallel networks of subareas, hidden by the low spatial resolution of the neuroimaging techniques but revealed by anatomical studies [1,27]. The second can be answered by a top-down, context-sensitive modulation of activation by control processes [9,10,14], or by a bottom-up influence of the physical properties of the stimulus [12,22,23,26,57].

The function implemented by a large-scale network depends on three properties: the network's structure [27,45], the more elementary functions implemented by its nodes (the functional role of each region), and the properties of its links (length, role: inhibitory or excitatory, ...). The function of a cerebral region emerges from the

neuronal population compounding the area, and can be considered as the integration of the individual behaviors of the neurons.

# 2.2. Cerebral nodes and their representations 

In the light of the preceding paragraph, the whole brain can be viewed as a very complex large-scale network, composed of interconnected and overlapping, functiondedicated, large-scale sub-networks. Every large-scale network can be modeled by a structural network whose nodes are the abstraction of cerebral regions (cortical or subcortical areas or subareas) and edges represent oriented axon bundles. Each structural link, which acts as an information transmitter [37], is characterized by its role (excitatory or inhibitory) and its temporal length, all derived from the properties of the corresponding bundle's fibers (role, physical length, signal transmission speed). Each structural node, which acts as an information processor, is characterized by its connections to other structural nodes and its function.

Each region can be considered as a network of (at least one) smaller neuronal populations, defined by functional (e.g. GABAergic neurons) or architectural (columns, modules [3]) features, and considered only after their functional properties. Therefore, a structural node can be represented by a functional network, i.e. the oriented network whose nodes are the abstractions of the smaller neuronal populations and edges the oriented neuronal fiber packs between them. A functional node implements a functional primitive, which is either the aggregate function of a specific specialized neuronal population, or a function which is supposed to exist, but whose neuronal substratum is not yet identified. When the functional network is composed of only one node, the structural node and its corresponding functional node can be merged. Although it is

supposed to be supported by fibers, a functional link is strictly defined in terms of a functional relationship.

Either in a structural or in a functional network, nodes are information processors and links information transmitters. A cerebral zone is defined as the substratum of a processor, i.e. it is a topographically well-defined, functionally coherent neuronal population whose connections with other populations are well-known.

The function of a structural node is the outcome of the primitives implemented in its functional network and which may all be different. The first constraint on the formalism is thus to be able to represent a network with oriented links and possibly differentiated nodes. This explicit modeling allows the direct expression of hypotheses on the cerebral processing. Functional networks can also be easily modified in order to follow the evolution of neurological knowledge, for example by changing one node (instead of modifying the whole architecture in a formal neural network). Furthermore, experimental results on cerebral plasticity [64] and cortical reorganization [48] reveal that some areas may share functional properties, probably due to similar physical organizations [5,11]. Our hypothesis is that the functional networks corresponding to these areas are different instantiations of a same model, called a generic model. A generic model is thus a partially defined network, where the nodes and links are defined, but the parameters are missing. Computationally speaking, it constitutes a reusable component.

# 2.3. Information representation 

The cerebral information that is processed by a neuronal population is the abstraction of the number and the pattern of this population's activated neurons. It can

be represented both by an energy level, which is indirectly, and in a distorted manner, reflected in the activation level measured by functional neuroimaging techniques, and a category. This representation is supported by results on the topical organization of the brain, which reflects category maps of the input stimuli. For example, primary auditory areas have a tonotopic organization corresponding to interval frequencies [6], the visual cortex has a retinotopic topography [5], and primary motor cortices have a somatotopic organization [1]. The persistence of the somatotopic organization at the level of nonprimary cortices and subcortical structures is in favor of a categorical representation beyond the primary areas [1]. The energy level and the category can also be represented in fibers [37]. When considering the external stimulus, i.e. the input information, the energy may be easily extracted from its psychophysical properties (e.g. a sound intensity) and the category is the summary of these characteristics (e.g. the frequency of a tone).

With a modeling point of view, the energy may be represented through a numerical value, whereas the category is expressed thanks to a more symbolic value. They are respectively called the magnitude and the type of the information or the stimulus.

# 2.4. Information processing 

Modeling the information processing in large-scale networks necessitates taking into account explicitly the dynamic aspects of the cerebral mechanisms, in terms of transmission delays, response times... Moreover, in humans, the only (indirect) measures of cerebral activity are sequences of sampled functional neuroimaging data whose representation requires a time discretization.

Functional neuroimaging data are very indirect measures of the neuronal activity, since they are statistical approximations, derived from the raw signal, of cerebral blood flow variations (tomographical techniques) or electromagnetic field variations (surface techniques) related to neuronal activation. Imprecision, which arises from indirectness and the inevitable experimental and measurement errors, must be modeled.

According to our definition of causality, which is a modification of Hume's one [32], the brain can be considered as a causal network. Our definition states that causality is due to three properties: spatial and temporal contiguity, temporal consistency, and statistical regularity. In other words, two entities A and B are causally linked if they are contiguous relatively to the system they belong to, if the beginning of A precedes the beginning of B, and if most of the times, A provokes B. This definition agrees with Pearl's probabilistic causality [53]. Since anatomical links (axons or axonal bundles), which convey information with very short transmission delays, connect physically cerebral zones, the zones are spatially and temporally adjacent and the condition of contiguity is strictly met. Temporal consistency is the result of the fact that, when two neurons (neuronal populations) are considered, the beginning of the activation of the upstream cell (population) always precedes the activation of the downstream cell (population). Moreover, due to the tremendous amount of factors that may act on the brain's states, either at a large or small scale level, the response of a neuronal population to a given stimulus or information cannot be considered as deterministic. Thus, the relationships between two cells or zones have a probabilistic regularity. Moreover, we want to supply a tool able to implement hypothesis on brain working, which are expressed by scientists or physicians merely in term of causes and effects. That is, both

biological plausibility and the need of models that can help clinical practice impose a causal formalism.

From the probabilistic regularity of cerebral events and the imprecision of the processed information arises the constraint to have uncertainty explicitly represented in the model.

Relationships between cerebral areas or functional primitives, which integrate the relationships that exist at a neuronal level, may be nonlinear (e.g. the sigmoid output function). At the cerebral area level, nonlinearity can be also caused by emission threshold or control processes, i.e. mechanisms putting discontinuities in information propagation. The last constraint is therefore to be able to model both linear and nonlinear cerebral relationships.

Given the modeled system, the cerebral areas networks, and our objectives concerning the use of the models, we have the following constraints on the modeling formalism: (1) an oriented networked architecture, with possibly different nodes, (2) causal relationships, (3) an explicit, discrete and regular representation of time, (4) an adapted representation of cerebral information, (5) the consideration of imprecision of neuroimaging data, and of uncertainty in brain's behavior, (6) nonlinear relationships.

Considering these constraints, causal dynamic Bayesian network are the best formalism. They are a graphical formalism using a directed network, where every node can be different from others. The relationships are causal and can be nonlinear. The use of real random variables allows to measure imprecision through mean and dispersion values, while the use of symbolic random variables allows representing the qualitative part of cerebral information. Furthermore, time can be explicitly modeled.

# 3. Overview of the formalism 

### 3.1. Dynamic Bayesian networks

A causal Bayesian network is a graphical model used to represent conditional independencies in a set of random variables. It consists of a directed acyclic graph where nodes represent random variables and edges represent causal relationships between the variables [51]. A conditional probability distribution is associated with each relationship between a node and its parents. Most of the times, when the random variables are continuous, normal distributions and linear relationships are assumed, for an easier computation. A relationship is then usually expressed as:

$$
Y=a+b X+u_{Y}
$$

where $X$ is the cause of $Y, a$ and $b$ are the relationship's parameters, and $u_{Y}$ is a Gaussian random variable, independent of other variables, representing the unmodeled influences or the noise [52]. If the node is a root, its prior probability is also Gaussian. When some nodes' values are observed, posterior probabilities for the hidden (i.e. nonobserved) nodes can be computed thanks to an inference algorithm, such as the junction tree algorithm [34]. Bayesian networks are usually used to model systems with causal and uncertain relationships. For a more complete description see [51,52].

In a dynamic Bayesian network (DBN), time is seen as a series of intervals called time slices [17,36]. For each slice, a submodel represents the state of the modeled system at the time. Contrary to static (i.e. classical) Bayesian networks, the evolution of random variables through time is considered. Furthermore, a length, expressed in number of slices, is implicitly associated to each relationship between the submodels.

DBNs are used to model Markov processes, i.e. processes where a temporally limited knowledge of the past is sufficient to predict the future. In other words, in a $n$-order Markov process, only the current $(t)$ and $n$ previous $(t-n$ to $t-1)$ time slices are necessary to forecast future values $[25,46]$.

If the set of hidden variables of a DBN constitute a Markov chain, with the set of observable variables depending on the hidden variables (see Fig. 1), then the network is called a state space model (SSM). In a SSM, if all the relationships are linear, the model is said to be a linear dynamical system. There are some specific algorithms to compute posterior distributions in this type of DBN, like the Kalman filter [70], a specialization of the junction tree algorithm.

# Insert Fig. 1 here 

If only the dynamical relationships (i.e. between the hidden variables) are linear, the observation relationships (i.e. between the hidden and observed variables) being non-linear, then the model is a dynamic generalized linear model [21]. If the SSM is fully nonlinear (i.e. both the dynamical and the observation relationships), it is a nonlinear dynamical system. A specific algorithm is needed to make inference, like the extended Kalman filter [46], or more recent (and more efficient) algorithms such as the particle filter [7], the unscented Kalman filter [35], or the divided difference filters [47].

### 3.2. Formal description

We define a static network as the functional expansion of a structural network, i.e. the network where all structural nodes have been replaced by their corresponding functional networks. It is the graphical representation of a network of cerebral zones. Since, it has no temporal feature, it is neither a causal network nor a Bayesian one (it

may be cyclic: see Fig. 3 and Fig. 5). The DBN that is built from the static network expresses the cerebral information processing in the corresponding large-scale networks.

# 3.2.1. Information representation 

Cerebral information is a flowing entity, that is computed at each spatial (cerebral zone) and temporal (time slice) step of the simulation. It is a two-dimensioned data (see section 2.3). The first part, the magnitude, stands for the cerebral energy needed to process the information in the zone. Real random variables represent it in the DBN. For the second part, the type, which represents the cerebral category the zone attributes to the information, the representation is more complex.

A symbol represents a "pure" (i.e. not blurred with noise or another symbol) category of information. For example, when the information represents a linguistic stimulus, a symbol may refer to a non ambiguous phoneme. For cerebral information, the symbol represents, in each zone, the neuronal subpopulation that is sensitive to (i.e. that fires for) the corresponding pure information. For example, in the primary auditory cortex, it may be the subpopulation sensitive to a specific frequency interval. A categorical field is a set of symbols describing stimuli of the same semantic class. For example, the "color" categorical field contains all the color symbols, but it cannot contain phonemes.

A type concerns several symbols, due to the presence of noise or because of some compound information. Let $\mathbb{S}$ be the set of all existing symbols. We assume that a type $T$ is defined for only one categorical field. Let $S_{T}$ be the subset of $\mathbb{S}$, corresponding

to this categorical field. The type $T$ is an application from $S_{F}$ to $[0,1]$, with the property $\sum_{s \in S_{F}} T(s)=1$, i.e. it describes a symbol repartition for a specific categorical field. In a stimulus, this repartition corresponds to the relative importance of each symbol compounding the information carried by the stimulus. Inside the model, $T(s)$ stands for the proportion of s-sensitive neurons in the population that fired for the information whose type is $T$.

Unlike the magnitude, the type is not represented by a random variable. Indeed, it is not necessary to represent its uncertainty (and hence to make the computational complexity harder) since we cannot compare it to neuroimaging data.

Finally, to describe the state of a cerebral zone $X$ at time $t$, we consider the type $T_{X}^{t}$ and the magnitude $M_{X}^{t}$ of the information output by $X$ at that time. Thus for one node in the static network, there are, at each time slice, two nodes in the DBN (Fig. 2).

Insert Fig. 2 here

# 3.2.2. Structure and relationships 

The relationships of the model are the propagation entities, while its nodes are the processing entities. In the static network, the relationship that links two cerebral zones $Y$ and $X$ is the functional abstraction of an anatomical link. A delay $\tilde{c}_{Y}$ representing the average propagation time in the link's fibers is associated to the relationship. It is not dealt with in the static network, but it appears in the DBN. The static relationship between $Y$ and $X$ is represented in the DBN by relationships between the magnitude

and the type of the information output from $Y$ at time $t-\partial_{Y}\left(M_{Y}^{t-\partial_{Y}}\right.$ and $\left.T_{Y}^{t-\partial_{Y}}\right)$ and those of the information output from $X$ at time $t\left(M_{X}^{t}\right.$ and $\left.T_{X}^{t}\right)$, for all $\left.t\right.$

Most of the time, the activity of a cerebral zone depends also on its previous activity. This is represented by a relationship between the $X$ information (i.e. the information output by $X$ ) at time $t-1$ and the $X$ information at time $t$. Fig. 2 summarizes the differences between the static network and the DBN for such a node.

# 3.2.3. Propagation and processing 

For one zone, both the cerebral propagation mechanisms (i.e. the relationships towards the zone) and the processing (spatial and temporal integration of the inputs, and processing as such) are described by a pair of functions, $f_{T_{X}}$ and $f_{M_{X}}$.

Let consider the general case where $n$ zones $Y_{1}, \ldots, Y_{n}$ are inputs to $X$, i.e. $X$ has $n$ parents in the static network. Let $\partial_{1}, \ldots, \partial_{n}$ be the corresponding delays of these relationships. Furthermore, the current activation of $X$ depends of its previous one. In the DBN, this is described by the following equations:

$$
M_{X}^{t}=f_{M_{X}}\left(M_{Y_{1}}^{t-\partial_{X}}, \ldots, M_{Y_{1}}^{t-\partial_{X}}, M_{X}^{t, 1}, u_{X}\right), T_{X}^{t}=f_{T_{X}}\left(T_{Y_{1}}^{t-\partial_{X}}, \ldots, T_{Y_{1}}^{t-\partial_{X}}, T_{X}^{t, 1}\right)
$$

The constraints on the magnitude function depend on the algorithm used to perform the simulation. We chose the DD2 algorithm [47], which allows the use of nonlinear functions. The random variable $u_{X} \sim N\left(0, \sigma^{2}\right)$ models uncertainty in the cerebral processing. When a parameter of a magnitude function can be modified by another node's influence, this parameter has to be modeled as an additional real random variable [20]. This kind of parameters allows modeling some controlled or learning mechanisms.

The type function is any combination of the incoming types and of the previous type that respects our type definition. For example, if both the incoming and the outgoing types are defined on the same categorical field $S$, the type function can be a linear combination such as:

$$
T_{S}^{c}(s)=c_{Y_{1}} T_{Y_{1}}^{r-\bar{c}_{Y_{1}}}(s)+\ldots+c_{Y_{2}} T_{Y_{2}}^{r-\bar{c}_{Y_{2}}}(s)+c_{X} T_{X}^{s-1}(s), \forall s \in S
$$

where $S$ is the categorical field of $T_{X}^{c}, T_{Y_{1}}^{r-\bar{c}_{Y_{1}}}, \ldots, T_{Y_{s}}^{r-\bar{c}_{Y_{s}}}$, and $T_{X}^{s-1}$; and with $\sum c_{*}=1$ in order to keep the property $\sum_{s \in S} T_{S}^{c}(s)=1$. In fact, we extend to all categorical fields the persistence of a "topic" organization at different cortical and subcortical levels, demonstrated for somatosensory stimuli [1]. This assumption is also supported by the existence of parallel distributed networks [27], which is in favor of the maintenance of a topical organization.

The Magnitude and Type functions are flexible enough to allow representing a large variety of cerebral mechanisms, and make the formalism able to adapt to the evolutions of the cerebral mechanisms knowledge.

# 3.2.4. Model building 

The goal of a model is getting a better understanding of the cerebral mechanisms explaining the set of functional neuroimaging data related to a given task.

The first step is the construction of the structural network. Since we build on existing knowledge in neuropsychology, the structural network is supposed to encompass all the regions that are supposed to be involved in the task performance. All

known (from human neuroanatomy) or supposed (i.e. assumed from animal experiments) connections between the regions are represented.

The second step is to develop the functional networks within structural nodes, then achieving the static network. A functional model describes the equations governing its functional primitives and the relationships between the primitives. It utilizes mostly results in neuropsychology or in neurophysiology for the function definition (e.g. the computation in pyramidal cells), and also for setting partly the parameters' values (e.g. the value of a firing threshold). Neuroimaging data are included as observables in the functional network, although their associated primitives, such as the derivation of PETlike data from neuronal activation values, are non neuronal functions. The existence of generic models, that is, non instantiated, reusable, models of functional networks, is assumed.

The third step consists at deriving the $\underline{\mathrm{DBN}}$ from the static network, by giving values to the temporal parameters. Some of them are set according to known physiology results (e.g. the transmission speed in some neural fibers). An important parameter is the length of a time slice, i.e. the time step of the model simulation. It must be shorter or equal than the time scale of the modeled cerebral phenomena, and than the sampling time of the neuroimaging technique. Furthermore, the longer the time slice is, the smaller the number of iterations necessary for the simulation is. Then the length of the time slice must be a compromise between realism and length of the simulation.

# 3.3. Example 

As an example of application of our formalism, a model is given. It is based on an experimental study [56] that focused on the differences between normal and dyslexic subjects, during a phoneme categorization task.

### 3.3.1. The experiment

The hypothesis is that dyslexic subjects are not able to correctly categorize phonemes, because of a dysfunction in some cortical areas involved in the early processing of auditory stimuli [56]. The goal is to detect the regions that behave differently in controls and dyslexic subjects, and to understand the reasons behind the difference.

Six patients and six controls were submitted to a passive hearing of stimuli that are mixes of two phonetically close syllables: /pa/ and /ta/ (including the pure /pa/ and the pure /ta/). The measurements were made with fMRI.

An fMRI run is a sequence of five blocks. A block contains six sequences of four sounds, followed by a rest period. A sequence lasts three minutes. The first three stimuli of every sequence are always the same sound (called the pivotal stimulus) noted dev0, and the last stimulus (called the deviant) is chosen amongst a set of five syllables constituted by four different mixes of /pa/ and /ta/, noted dev2M, dev1M, dev1P and dev2P, plus the pivotal stimulus. Each block corresponds to a specific deviant (Table 1).

Insert Table 1 here

# 3.3.2. Description of the model 

We restrict the large-scale network to a single region, a part of the right temporal superior gyrus, that is involved in the early processing of auditory stimuli, and is activated differently in controls and dyslexic subjects. Our main assumption is that phylogenic processes have given rise to the existence of phonemic processors in the human brain. Since the location of those processors is unknown, they cannot constitute separate structural nodes. Basic mechanisms for the early processing of stimuli ground the striate cortex model presented by Pastor et al. [50]. According to the concept of genericity, the model of each phoneme processor is based on it. In each processor (Fig. 3), a loop between the output (OGN) and the firing threshold (FTN) summarizes the thalamocortical loop in the striate cortex model (Fig. 5) and the parameters are adapted from visual to auditory stimuli processing. Moreover, since fMRI does not provide activation measures at the level of the phonemic processors, the two activation nodes have been merged in a single one (AN).

## Insert Fig. 3 here

The static network shows that lateral inhibitions (LIN nodes) between the two processors involved in the experiment (the /pa/ processor, and /ta/ processor) are assumed (Fig. 3). Since delays are associated to the links in the static network, the unrolled dynamic network is an acyclic oriented graph.

The categorical field contains two symbols (/pa/ and /ta/). The type of a stimulus represents the proportions of the two symbols. Five different types are used, corresponding to the experimental conditions (Table 1).

In Fig. 3, the Stim node stands for the stimulus; it is the input of the model. The Activation Node (AN) reflects the level of the whole region's blood flow variations, linked to the neuronal energy demand. The Input Gating Nodes ( $\mathrm{IGN}_{\mathrm{pa}}$ and $\mathrm{IGN}_{\mathrm{ta}}$ ) express the phoneme processors' sensitivity to the stimulus. They may be considered as the abstraction, in terms of pattern and level of activation, of the cells of the area's input layer. The Output Gating Nodes $\left(\mathrm{OGN}_{\mathrm{pa}}\right.$ and $\left.\mathrm{OGN}_{\mathrm{ta}}\right)$ send information to the downstream areas. They represent, more or less, the integrated activity of the cells of the area's output layer. The Inhibitory Nodes $\left(\mathrm{IN}_{\mathrm{pa}}\right.$ and $\left.\mathrm{IN}_{\mathrm{ta}}\right)$ and Lateral Inhibitory Nodes $\left(\mathrm{LIN}_{\mathrm{pa}}\right.$ and $\left.\mathrm{LIN}_{\mathrm{ta}}\right)$ are supposed to represent the integrated behavior of the GABA-neurons. Because of the LINs, the activation of an IGN causes an inhibition in the opposite IGN. Each Firing Threshold Node ( $\mathrm{FTN}_{\mathrm{pa}}$ and $\mathrm{FTN}_{\mathrm{ta}}$ ) is modulated by an OGN (respectively $\mathrm{OGN}_{\mathrm{pa}}$ and $\mathrm{OGN}_{\mathrm{ta}}$ ) that can lower it. The FTNs are purely functional nodes.

The model is symmetric, that is the functions for both the /pa/ and the /ta/ parts share exactly the same structure and parameters (Table 2), except for the IGNs' sensitiveness to the stimulus. Thus, only the functions for the /pa/ part will be presented. In the following equations, the parameter whose rank is $i$ in the function of a node $X$, is noted $a_{X}^{(i)}$. All the $u_{x}^{\dagger}$ are independent Gaussian variables.

The refractory period of the processor's neurons is modeled in $\mathrm{IGN}_{\mathrm{pa}}$ by a sigmoid function $\varphi_{I G N}$ that makes $M_{I G N_{p}}^{i}$ sensitive to the incoming stimulus only if $M_{I G N_{k}}^{i-1}$, the magnitude of the processor's output, is close to zero:

$$
M_{I G N_{p s}}^{i}=a_{I G N}^{(1)} g_{I G N_{p s}}\left(T_{I i n s}^{i-2}\right)\left(1-\varphi_{I G N}\left(M_{I I G N_{p s}}^{i-1}\right)\right) M_{I i n s_{p s}}^{i-2}+a_{I G N}^{(2)} M_{I G N_{p s}}^{i-1}-a_{I G N}^{(3)} M_{I N_{p s}}^{i-1}-a_{I G N}^{131} M_{L I N_{p s}}^{i-1}+u_{I G N_{p s}}^{i}
$$

The sensitivity of each $\mathrm{IGN}_{\bullet}$ to the received type is defined by a constant type sens. (Table 1). Of course, $\mathrm{IGN}_{\mathrm{pa}}$ is more sensitive to the symbol $/ \mathrm{pa} /$, and $\mathrm{IGN}_{\mathrm{ta}}$ to $/ \mathrm{ta} /$. The function $g_{I G N_{p a}}$ is used with the constant sens $_{\mathrm{pa}}$ and the incoming stimulus' type $T_{S t s s}^{r-2}$ in order to modulate the magnitude of $\mathrm{IGN}_{\mathrm{pa}}$ :

$$
g_{I G N_{p a}}\left(T_{S t s s}^{r-2}\right)=T_{S t s s}^{r-2}(p a) \text { sens } p a(p a)+T_{S t s s}^{r-2}(t a) \text { sens } p a(t a)
$$

The types are used only for the input gating; they do not intervene in the rest of the model. The sigmoid $\varphi_{O G N}$ in $O G N_{p a}$ 's magnitude function allows it to fire only if the magnitude coming from the $\mathrm{IGN}_{\mathrm{pa}}$ is greater than the firing threshold's $\left(\mathrm{FTN}_{\mathrm{pa}}\right)$ one:

$$
\begin{aligned}
& M_{O G N_{p a}}^{t}=a_{O G N}^{(1)} \varphi_{O G N}\left(M_{I G N_{p a}}^{t-1}-M_{F T N_{p a}}^{t-1}\right) M_{I G N_{p a}}^{t-1}+a_{O G N}^{(1)} M_{O G N_{p a}}^{t-1}+u_{O G N_{p a}}^{t} \\
& M_{I N_{p a}}^{t}=a_{I N}^{(1)} M_{I G N_{p a}}^{t-1}+a_{I N}^{(2)} M_{I N_{p a}}^{t-2}+u_{I N_{p a}}^{t} \\
& M_{I J N_{p a}}^{t}=a_{I J N}^{(1)} M_{I G N_{p a}}^{t-1}+a_{I J N}^{(2)} M_{I J N_{p a}}^{t-1}+u_{I J N_{p a}}^{t} \\
& M_{F T N_{p a}}^{t}=a_{F T N}^{(1)}-\left(a_{F I N}^{(2)}\left(a_{F I N}^{(1)}-M_{F T N_{p a}}^{t-1}\right)+a_{F I N}^{(1)} M_{O G N_{p a}}^{t-2}\right)+u_{F G N_{p a}}^{t}
\end{aligned}
$$

Finally, AN consists in the sum of the successive IGNs' activations during one experimental block:

$$
M_{A N}^{t}=M_{I G N_{p a}}^{t-1}+M_{I G N_{p a}}^{t-1}+M_{A N}^{t-1}
$$

We made the hypothesis that the difference of processing between a normal subject and a dyslexic subject was caused mainly by a disorder in the lateral inhibitions. Thus, the two models, one for the average patient and the other for the average control, used

the same functions and shared the same parameters (Table 2), except for the inhibition nodes $\left(\mathrm{IN}_{\bullet}\right.$ and $\left.\mathrm{LIN}_{\bullet}\right)$.

There are no lateral inhibitions in the dyslexic model, and its internal inhibitions are slightly stronger than in the normal model. Table 3 gives the parameters for the inhibition nodes in the normal model, and Table 4 those for the dyslexic one.

Insert Table 3 here

# Insert Table 4 here 

More generally, the parameters were either drawn from the model of the striate cortex [50], or adapted to the representation of an auditory region (instead of a visual cortex) and the explanation of fMRI data, instead of PET scan data.

### 3.3.3. Results and comments

During the simulation, we used five blocks of only one sequence of four syllables (three pivotal stimuli and a deviant). In fact, since the brain's activity returns to rest level between two experimental sequences, we considered that the processed results were comparable to average results obtained during the real experiment. Since, except for the Stim and the AN nodes, all nodes represent neuronal activities, the time unit is set to 1 ms . We used the DD2 algorithm [47] to perform the simulation. The computational complexity of this algorithm is $\underline{O}\left(\underline{L}^{3}\right)$, where $\underline{L}$ is the state dimension [68].

Fig. 4 compares the simulated activation values to the mean activation values, for the controls (left graph) and the dyslexic subjects (right graph). Both for controls and patients, simulation and experimental results were normalized in order to have the same arithmetic mean (0) and the same range (1). In each graph, a pair of bars corresponds to

one block. Light-grey bars stand for the differences between the normalized experimental values and the normalized experimental rest values. Dark-grey bars represent the difference between normalized values of AN and experimental rest values. Bar numbers $1,2,3,4,5$ represent respectively the blocks for deviants dev2M, dev1M, dev0, dev1P and dev2P.

# Insert Fig. 4 here 

For controls, the experimental results shows that the more distant (from the pivotal stimulus, categorically speaking) the deviant is, the stronger the activation is. This is supposed to be caused by a habituation mechanism, due to the repetition of the pivotal stimulus, that lowers the activation, followed by an activation the force of which depends on the "surprise" caused by the deviant. In the model, the internal inhibition allows to mimic the habituation, because several consecutive activations will raise the IN, and thus lower the IGN. On the other hand, the lateral inhibition favors the more activated of the two areas of the gyrus (i.e. the /pa/ part or the /ta/ part), creating this great sensitiveness to the last presented phoneme's distance to the pivotal stimulus.

The interpretation of the dyslexic subjects' results is that they do not correctly categorize the different phonemes. Thus, both the /pa/ and the /ta/ parts of the gyrus activate for each block. The activation level is different in the different blocks, since the sub-regions do not show the same sensitiveness to the phonemes.

## 4. Discussion

Classical neuroimaging models focus on a localization problem. Their goal is to identify a network or a set of cerebral zones implementing some cognitive or sensorimotor function, but they do not aim at explaining how the network's activation

derives from the function performance. Our formalism aims at explaining neuroimaging data, by understanding the underlying cerebral mechanisms leading to the observed activation. The important difference is that this additional information is essential to explain neuroimaging data in the cases where there are apparently contradictory results, or where complex functions are studied.

On the other hand, models in computational neuroscience are characterized both by their biological plausibility and their level of cerebral representation. Unlike neuroimaging models, their goal is to explain how cerebral mechanisms work. But if the modelling level is too low (neuronal mechanisms level), cerebral activity cannot be explained in terms of information processing. On the contrary, if the modelling level is too high (cognitive functions without considering the cerebral substratum), the model cannot lead to neuroimaging interpretation because of the lack of biological plausibility. Our approach can be viewed as a compromise between the biological and the cognitive levels needed to have a tool allowing the explanation of observed activation in terms of information processing.

A better assessment of our formalism is the comparison with BioCaEn [49,50], which has the same or close modeling objectives and constraints. This tool aims at modeling information processing in large-scale cerebral networks, with causal qualitative networks (CQN), based on interval calculus [16]. We adapted to our formalism the model presented in [50] (Fig. 5), based on two PET experiments conducted by Fox \& Raichle [22,23] who studied the modulation, by the presentation rate of visual stimuli, of the activation of the striate cortex. The model highlighted the role of a thalamocortical loop in the habituation phenomenon, which explained partly the experimental results [50].

# Insert Fig. 5 here 

In the model simulation, the time unit is 1 ms . The summation over 40 s of all the AN values is a measure of relative regional cerebral blood flow, once the brain's average activation level is set in the model, at its experimental value. Our simulation (Fig. 6) shows slightly better results than the CQN model. But the real advantages are elsewhere. First, DBNs allow a better control of the dispersion of the calculated values than interval-based simulation, which leads, by construction [63], to a constant increase of the imprecision. Moreover, DBN can directly express non linear functions, while BioCaen is based on linear equations.

## Insert Fig. 6 here

Another advantage of probabilistic networks is the existence and development of a lot of algorithms for parameter estimation and inference. This was not illustrated here since both the experiments described in this paper provided us temporally integrated activation data (respectively, fMRI and PET data), averaged on the subjects. The sample size being one (the average subject), parameter estimation using automatic methods cannot be applied. Thus, the parameters' values were defined only by using neurological knowledge and empirical estimation. However, since we do not aim at building ad hoc models, able to fit only one experiment, but rather more general purpose models, representing cerebral mechanisms, the real robustness of a model does not come from the perfect fit to one experiment, but rather from its robustness over many different situations. We expect that the joint use of EEG or fMRI data will allow to determine more precisely temporal parameters related to different regions and to get a gross approximation of the links between neuronal activation (provided by EEG data)

and haemodynamic activation (provided by fMRI). Transcranial Magnetic Stimulation should allow getting some insights on hidden variables (i.e. neuronal phenomena).

# 5. Conclusion 

We have presented a general framework, allowing interpreting neuroimaging data concerning various cognitive or sensorimotor tasks. This framework has been designed to be open to evolutions of the knowledge in neuropsychology and neurophysiology. DBNs allowed us to model the brain as a dynamic causal probabilistic network with non-linear relationships. This was illustrated with two examples, the first concerning a phonemic categorization process, and the last a visual perceptive process.

Our future work will focus on the integration of more biological plausibility in the modeling framework. Currently, the state of a functional node is represented by the magnitude and the type of the information, after it has been processed by the associated zone. The magnitude and the type correspond to the cumulated firing rate and the pattern of the neurons that have fired in the zone. In particular, the magnitude is used in the estimation of tomographic activation data (metabolic data, relative cerebral blood flow...). However, it is not clear that the neurons that activate and do not fire, do not participate in the tomographic activation. Indeed, it is possible to set apart a zone's activation and its emission. The activation can be seen as the result of the spatial and temporal integration of the zone's inputs, while the emission is the result of the process of the activation and maybe other influences. This first extension of the formalism will allow representing complex relationships between and inside the zones.

Some higher level cognitive processes need the model to be able to combine types defined on different categorical domains. The definition of this new type operator, which is a first step to concept learning, constitutes another question we will address.

Another essential topic is the reusability of our models. Since, today, neuronal and neuroimaging-oriented variables coexist in the models, in the same experimental conditions, two different models must be defined if the data acquisition technique changes. Building generic functional models needs therefore the separation of functional models and interface models, able to translate cerebral information processing variables into neuroimaging results.

Our long-term goal is to progressively include in our framework various validated generic models, in order to have reusable components, and to build a consistent and general brain theory based on large-scale networks.

# Tables 

Table 1
Constants for both phonemic categorization models


Table 2
Identical parameters for both phonemic categorization models


Table 3
Normal phonemic categorization model's specific parameters


Table 4
Dyslexic phonemic categorization model's specific parameters


# Figures captions 

Fig. 1. A state space model ( $x$ and $y$ can be vector-valued variables). The shaded nodes stand for observed variables.

Fig. 2. From the static network to the DBN.

Fig. 3. The static network used to model the cerebral phonemic categorization process. The delay for each relationship is 1 ms , except for the dotted relationships, where it is 2 ms .

Fig. 4. Compared results between simulated data and measures, for the phonemic categorization process.

Fig. 5. The static network used to model the Fox \& Raichle's experiment [22;23]. The delay for each relationship is 1 ms , excepted for the dotted relationships, where it is 2 ms .

Fig. 6. Compared results between simulated data and measures, for the visual perception process.

Hidden nodes
![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)
$t-\partial_{Y} \quad \ldots . . \quad t-1 \quad t$

![img-2.jpeg](img-2.jpeg)

**Stimulus Right Temporal Superior Gyrus**



**Stimulus LINGUO**



**Stimulus LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**



**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**

**Stimulus LINGUO LINGUO LINGUO**



![img-3.jpeg](img-3.jpeg)

Dyslexic subjects

![img-4.jpeg](img-4.jpeg)

Thalamic Structure

![img-5.jpeg](img-5.jpeg)

Stimulus
Rate
$(\mathrm{Hz})$