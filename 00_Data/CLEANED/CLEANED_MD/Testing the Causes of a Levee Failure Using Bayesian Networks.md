# Research 

## Testing the Causes of a Levee Failure Using Bayesian Networks

## Evaluación de las causas de falla de un dique usando redes bayesianas

William García-Feria ${ }^{* 1}$, Julio Colmenares-Montañez ${ }^{\circledR 1}$, German Hernández-Pérez*1<br>${ }^{1}$ Universidad Nacional de Colombia (Bogotá-Colombia).<br>*Correspondence e-mail: wmgarciaf@unal.edu.co

Recibido: 30/12/2021. Modificado: 18/11/2021. Aceptado: 09/02/2022.


#### Abstract

Context: Forensic geotechnical engineering aims to determine the most likely causes leading to geotechnical failures. Standard practice tests a set of credible hypotheses against the collected evidence using backward analysis and complex but deterministic geotechnical models. Geotechnical models involving uncertainty are not usually employed to analyze the causes of failure, even though soil parameters are uncertain, and evidence is often incomplete.


Method: This paper introduces a probabilistic model approach based on Bayesian Networks to test hypotheses in light of collected evidence. Bayesian networks simulate patterns of human reasoning under uncertainty through a bidirectional inference process known as "explaining away." In this study, Bayesian Networks are used to test several credible hypotheses about the causes of levee failures. Probability queries and the K-Most Prob- able Explanation algorithm (K-MPE) are used to assess the hypotheses.
Results: This approach was applied to the analysis of a well-known levee failure in Breitenhagen, Germany, where previous forensic studies found a multiplicity of competing explanations for the causes of failure. The approach allows concluding that the failure was most likely caused by a combination of high phreatic levels, a conductive layer, and weak soils, thus allowing to discard a significant number of competing explanations.

Conclusions: The proposed approach is expected to improve the accuracy and transparency of conclusions about the causes of failure in levee structures.

Keywords: forensic geotechnical engineering, Bayesian Networks, levee failure
Language: English

## Open access

Cite as: W. Garcia-Feria, J. Colmenares-Montañez, G. Hernández-Pérez. "esting the Causes of a Levee Failure Using Bayesian Networks". Ing, vol. 27, no. 2, 2022. e18538. https://doi.org/10.14483/23448393.18538
(c) The authors; reproduction right holder Universidad Distrital Francisco José de Caldas.

# Resumen 

Contexto: La ingeniería geotécnica forense tiene como objetivo determinar las causas más probables que conducen a fallas de tipo geotécnico. La práctica habitual pone a prueba un conjunto de hipótesis a la luz de la evidencia, utilizando análisis retrospectivos y modelos geotécnicos complejos pero deterministas. Los modelos geotécnicos que involucran incertidumbre no suelen emplearse para analizar las causas de falla, a pesar de que los parámetros del suelo son inciertos y la evidencia suele ser incompleta. Método: Este artículo presenta un enfoque de modelo probabilístico basado en redes bayesianas para evaluar hipótesis con base en la evidencia recolectada. Las redes bayesianas simulan patrones de razonamiento humano bajo incertidumbre a través de un proceso de inferencia bidireccional conocido como explaining away [explicación]. En este estudio, las redes bayesianas se utilizan para probar hipótesis creíbles sobre las causas de falla de un dique. Para evaluar las hipótesis se utilizan consultas de probabilidad y el algoritmo de explicación más probable (K-MPE).
Resultados: El enfoque se empleó en el análisis de un dique en Breitenhagen, Alemania, donde varios estudios forenses anteriores encontraron multiplicidad de explicaciones contrapuestas acerca de las causas de falla. El enfoque permite concluir que la causa más probable de falla fue una combinación de altos niveles freáticos, una capa de suelo de alta permeabilidad y suelos de baja resistencia, lo que permitió descartar un número significativo de explicaciones contrapuestas.
Conclusiones: Se espera que el enfoque probabilístico propuesto mejore la precisión y la transparencia de las conclusiones sobre las causas de falla en estructuras tipo dique.
Palabras clave: ingeniería geotécnica forense, redes bayesianas, falla de diques
Idioma: Inglés

## 1. Introduction

Drawing conclusions about the causes of geotechnical failures can be strongly affected by parameters and model uncertainties. Therefore, conclusions derived from forensic assessments often seem to be arbitrary and controversial. Although forensic analyses follow a rigorous process, the lack of a probability-based framework can lead to costly and inefficient engineering solutions, as well as to the wrong legal decisions.

Graphical probabilistic methods such as Bayesian Networks (BNs) can improve the practice of forensic geotechnical engineering. Their ability to model competing hypotheses about the causes of failure makes them a suitable tool for forensic assessments. BNs have been mainly used in medicine, legal, and forensic science, mostly to support decisions in circumstances where uncertainty or imprecision prevails [1]-[5]. Forensic engineering has partially used BNs for drawing reasonable conclusions about the causes of failures. Several studies, such as those presented in [6]-[9], demonstrate their applicability. Despite the benefits of BNs in forensic engineering, they have not been widely adopted in forensic geotechnical studies [10].

This paper presents a Bayesian Network approach to support decisions in forensic geotechnical assessments. The approach relies on the generic forensic engineering process for failure assessment but incorporates a probabilistic framework to consider parameters and model uncertainties. The Breitenhagen levee failure that occurred in Germany in 2013 is used to validate the proposed BN approach. Data, studies, and some assumptions associated with the Breitenhagen levee failure, which are presented in [11], [12], and [13], are used as a starting point for this study.

The results show that the proposed BN approach can support the forensic geotechnical process. Moreover, the interpretability and traceability of BNs ensure a rational decision based on a probabilistic framework. Therefore, legal decisions and engineering solutions can be supported by more objective conclusions.

# 2. Forensic geotechnical engineering 

Forensic geotechnical engineering deals with investigating and communicating the causes of failures attributed to geological/geotechnical aspects [14], [15]. It involves the analysis of cause-effect relationships using the scientific method and some complementary techniques. Most forensic engineering methodologies focus on structural failures [16]. However, very few procedures and guidelines have been adapted to fulfil forensic geotechnical requirements. Among them, there is a methodology for levee failures [12], a conceptual framework proposed in [23], and a modified version of the observational method [24].

From a broader perspective, this process includes four stages [16], [17]: (1) collecting evidence, (2) developing failure hypotheses, (3) testing hypotheses against evidence, and (4) finding the most likely cause of failure. In the first stage, forensic engineers collect all available information to understand the circumstances that led to the failure. Sources of information may include field observations and investigation, traditional and drone photography, working drawings, contract documents, eyewitness interviews, and construction records [16].

The second stage aims to develop credible hypotheses of failure based on the collected evidence. Brady [17] and Bell [25] suggest that conventional design methods used in engineering practices are not suitable for developing credible hypotheses. These methods apply synthesis techniques based on forwarding reasoning. Synthesis could lead to wrong conclusions about the causes of failure because the collected evidence is forced to match biased hypotheses. [20] recommends deductive analysis to investigate the causes of failures, where the collected evidence guides the development of credible hypotheses.

In the third stage, hypotheses about the causes of failure are tested against the collected evidence. Back analysis has been commonly used to accept or reject hypotheses. However, selecting analytical tools and interpreting results from back analysis requires experienced engineers [26], mainly when the failure is represented by complex soil constitutive models and demanding analytical tools.

The fourth stage is the goal of any forensic assessment. A credible cause of failure is reached when all alternative hypotheses are eliminated and only one (or some) match the evidence. Selecting the most likely cause (or causes) of failure is quite a challenging task. Occasionally, the selected cause of failure seems arbitrary or subjective due to large uncertainties in both parameters and models [12], [25] and [20] suggest using the scientific method to overcome subjectivity. The scientific method tests hypotheses against the collected evidence in order to approve or disapprove its validity. In other words, the method reexamines the collected evidence to determine if a hypothesis can explain it.

In forensic geotechnical engineering, [23] and [27] propose some guidelines based on the scientific method. [20] goes further and argues that reliable scientific interpretations about causes of failure should come from statistic and probabilistic analysis. To date, very few forensic engineering assessments use probabilistic tools [13], [28]. Furthermore, [29] recognize the scarcity of previous literature about this topic.

# 3. Bayesian Networks 

This section introduces some important concepts regarding Bayesian Networks (BNs). Several standard textbooks, such as [30] and [31], are recommended for an extended introduction. A BN is a probabilistic model that combines probability and graph theories [32]. BNs are used for inference and reasoning under uncertainty due to their ability to simulate human reasoning processes [33]. Forward and backward inference is recognized as a crucial characteristic in BNs. These attributes, along with a rigorous probabilistic background, have led BNs to successful applications [1], [2], [5], [6]. In the technical literature, BNs are also known as Bayesian expert systems, probabilistic graphic networks, belief networks, or Bayes nets.

### 3.1. Basic definitions

A problem involving reasoning under uncertainty and decision-making can be represented through a causal graph G (see Fig. 1). G is a structure consisting of nodes and edges ${ }^{1}$. Nodes represent events or variables, and edges embody causal relationships between nodes [31]. A pair of nodes $X_{i}$ and $X_{j}$, belonging to a set of nodes $X=\left\{X_{1}, \ldots, X_{n}\right\}$, can be connected by a directed edge $X_{i} \rightarrow X_{j}$. When the edges in $G$ do not form a cycle, $G$ is known as a directed acyclic graph (DAG). Nodes encode random variables, propositions, or sample spaces. A node can have any number of states in a discrete set or in a continuous set. For example, node $X_{i}$ in Fig. 1 has two states $X_{i}=\left\{X_{i}^{0}, X_{i}^{1}\right\}$, whereas the sample space of node $X_{j}$ is described by a Gaussian distribution $X_{j} \sim N\left(\mu_{X_{j}}, \sigma_{X_{j}}\right)$
![img-0.jpeg](img-0.jpeg)

Figure 1. A simple causal graph $G$
Causal relationships between nodes $X$ are graphically represented by edges $E$. In the context of BNs, causality denotes dependencies between variables or the direct influence of node $X_{i}$ on node $X_{j}$. Usually, this influence is not entirely deterministic. Therefore, $E$ expresses the probabilistic

[^0]
[^0]:    ${ }^{1}$ Graphs are usually denoted as $G=(V, E)$, where $V=\left\{v_{1}, v_{2}, v_{3}, \ldots\right\}$ represents the set of vertices and $E=\left\{e_{1}, e_{2}, e_{3}, \ldots\right\}$ represents the set of edges. However, given that, in probabilistic graphical models, each node is associated with a random variable $X_{i}$, the graphs are directly denoted $G=(X, E)$ with $X=\left\{X_{1}, X_{2}, X_{3}, \ldots\right\}$ and $X_{i}$ representing nodes and random variables simultaneously.

influence of $X_{i}$ on $X_{j}$. For discrete variables, the influence is represented by a conditional probability table (CPT). In the case of continuous variables, conditional probability distributions (CPD) are employed. A CPT specifies a probability distribution over the states of $X_{j}$ given each possible state of $X_{i}$. In more general terms, a CPT encodes $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$, where $p a\left(X_{i}\right)$ represents the set of nodes in $X$ with edges pointing to $X_{i}$. The term $p a\left(X_{i}\right)$ is read as parents of $X_{i}$.

A causal graph is defined as a Bayesian Network when all the following conditions are met [30]:

1. Each node has a finite set of mutually exclusive states.
2. The edges do not form a cycle between nodes (i.e., it is a DAG).
3. The strength of the causal relationship between variables is expressed by conditional probabilities tables or distributions (CPTs or CPDs).

# 3.2. Structure of a Bayesian Network 

The structure of a BN refers to the type of relationships (connections) between nodes. There are three basic connections in a BN: serial, converging, and diverging. Each type of connection determines which nodes are updated when some evidence is entered in the BN.

A serial connection between three nodes is shown in Fig. 2a. In this structure, node $A$ influences $B$, which in turn influences $C$. If the state of $A$ is known (i.e., $A$ is instantiated), it will influence the state of $C$ through node $B$. Similarly, if the state of $C$ is known, the state of $A$ will change through $B$. On the contrary, if the state of node $B$ is known, the flow of information between $A$ and $C$ is blocked. In this case, $A$ and $C$ are $d$-separated given $B$.

Fig. 2b presents a diverging connection between three nodes. If some evidence is included in $B$, information is transmitted to $A$ and $C$. However, any additional evidence included in $A$ when $B$ is instantiated will not be transferred to $C$. In this case, $A$ and $C$ are $d$-separated given $B$, or $A$ and $C$ are conditionally independent given $B$.

In a converging connection (Fig. 2c), any evidence entered in $A$ and $C$ will change the state of node $B$. Likewise, any evidence included in $B$ will change the state of $A$ and $C$. Hence, $A$ and $C$ can transmit information between them when $B$ is instantiated. In other words, $A$ and $C$ are $d$-connected given $B$. In any other case, $A$ and $C$ are $d$-separated.

The power of BNs resides on combining Bayes's rule and the chain rule. These characteristics give BNs the ability for decision-making and abductive reasoning. Bayes's rule states that prior belief about a hypothesis can be modified if some evidence is available. Let us say that $H$ represents a hypothesis and $E$ some evidence related to $H$. The updated belief about $H$ given $E$ can be calculated through Bayes's rule (Eq. 1). In Eq. 1, $P(H \mid E)$ represents the posterior (updated) probability of $H$ given $E, P(E \mid H)$ the likelihood of the evidence given the hypothesis $H$, and $P(H)$ the prior probability of $H$. The term in the denominator is the marginal likelihood, which normalizes the posterior probability.

$$
P(H \mid E)=\frac{p(E \mid H) p(H)}{\sum_{H} p(E \mid H) p(H)}
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. Basic connections in BNs: (a) serial connection, (b) diverging connection, (c) converging connection. Grey nodes indicate instantiation

The chain rule reflects the properties of a BN. Let $X^{\prime}=\{A, B, C, D, E\}$ be the universe of variables that describe a problem. If $G_{B N}$ defines a Bayesian network over $X^{\prime}$ (Fig. 3), then Eq. (2) represents the conditional probability of $G_{B N}$, where $A$ and $B$ are parent nodes and $C, D$, and $E$ are children nodes. Eq. (2) can be rewritten in the compact form of Eq. (3). Although a $G_{B N}$ is sufficient for updating probabilities, BNs with many nodes have a high computational cost. Some efficient algorithms such as junction three and stochastic simulation considerably reduce this cost.

$$
\begin{gathered}
P\left(X^{\prime}\right)=P(A) P(B) P(C \mid A, B) P(D \mid A, B) P(E \mid A, B) \\
P\left(X^{\prime}\right)=\prod_{i=1}^{N} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
\end{gathered}
$$

# 3.3. Abductive reasoning in Bayesian Networks 

BNs play a significant role in the field of abductive reasoning methods. Abduction refers to generating plausible explanations (hypotheses) for a set of observations (evidence) related to a phenomenon. Fig. 4 presents the abductive process described in [34] adapted to the geotechnical context. Based on the collected evidence and observed behavior, several credible hypotheses are generated. These hypotheses constitute a set of possible explanations for a geotechnical failure (i.e., causes of failure). A BN, along with a metric-based criterion, is used to select the most probable hypothesis (i.e., the best explanation).

Let $x_{o}$ be a set of collected evidence for the observed nodes $X_{O}$ in a BN (Fig. 3). An explanation is an arrangement of states for the unobserved nodes $X_{U}=x_{U}$ that is consistent with $x_{o}$. Abductive reasoning aims to find the best explanation (Most Probable Explanation, MPE) among a set of possible explanations [35]. Eq. (4) defines the MPE in which $x_{U}^{*}$ is a single arrangement of states

![img-2.jpeg](img-2.jpeg)

Figure 3. Example of a BN with five nodes: two parents and three children. Dash lines indicate sets of observed and unobserved nodes.
![img-3.jpeg](img-3.jpeg)

Figure 4. Abductive process [34] adapted to the geotechnical context.
for $X_{U}$. Although the MPE is a useful metric, abductive reasoning is also interested in the K Most Probable Explanations (K-MPE) [36]. The K-MPE identifies and organizes the most probable states of $X_{U}$ according to their joint probabilities.

$$
x_{U}^{*}=\operatorname{argmax}_{x_{U}} P\left(x_{U} \mid x_{0}\right)
$$

# 4. Bayesian Network approach for forensic assessment of a levee failure 

Assessing evidence and evaluating competing hypotheses are regarded as challenging tasks [15], [18]. Abductive and probabilistic reasoning can support these tasks through the rigorous mathematical frame-work of BNs. The five-step approach proposed in this paper is described in the following subsections. In general, the approach defines a set of competing hypotheses about the causes of a levee failure and builds a BN to test them. The collected evidence is included in the BN to assess the hypotheses via an abductive process. The approach identifies the most probable causes of failure (explanations) using the K-MPE metric over the set of credible hypotheses.

# 4.1. The five-step approach 

The first step consists of identifying credible hypotheses about the causes of failure. In geotechnical engineering, common failure hypotheses are related to pore water pressures, loading magnitudes, and subsoil conditions [13]. Each credible hypothesis is translated into the BN through a node. Subsequently, several states are assigned to each node according to its characteristics.

The second step defines evidence nodes to the observed or behavioral variables. These nodes can include, among others, stability condition, deformation magnitude, water level elevation, runout distance, and slip geometry. In some cases, mediating variables could be required to connect hypotheses and evidence nodes. For example, the Factor of Safety (FoS) can be defined as a mediating variable to link a hypothesis node related to the soil strength and an evidence node associated with the stability condition.

Given the set of hypotheses and observed nodes, the next step identifies causal relationships between nodes. Causality is easily identifiable when a physical model of the phenomenon is available. Otherwise, the BN structure can be supported on semantic and syntax substructures known as idioms [37]. It is easily identifiable by expressions such as 'attributable to, due to, as a consequence of, impact, caused by, resulting in', among others.

Once the causal graph has been defined (i.e., nodes and edges), the fourth step aims to elicit the conditional probability tables (CPT). This quantitative information can be obtained from mathematical models (e.g., computer simulations) or databases. Expert knowledge can also be used to determine the CPD values. However, analyses with multiple nodes could limit the use of expert knowledge.

The final step involves entering the collected evidence into the BN, updating the nodes, and evaluating the competing hypotheses. In this step, the BN is used to answer questions in the form of conditional probability queries, in other words, to find the probabilities of unobserved nodes given specific states in observed nodes [38]. The K-MPE is a particular type of query that aims to identify the K most likely states of the nodes given some evidence. Its results can be used to draw conclusions about the causes of failure. In this study, hypotheses describing the causes of failure from a forensic perspective are statistically compared by evaluating their likelihoods.

## 5. Application example: the Breitenhagen levee failure

The proposed five-step BN approach was applied to the Breitenhagen levee failure. [12] presented a comprehensive forensic study of this case based on a sensitivity analysis. The failure scenarios and geotechnical models presented in [12] are used to validate the proposed BN approach.

### 5.1. General description

The Breitenhagen levee failure occurred in June 2013 during the Sale River floods in SaxonyAnhalt, Germany. According to [11], the failure was a slope instability due to sustained high water levels in both the Elbe and Saale rivers. The levee at the failure location was $3,5 \mathrm{~m}$ high with a

$3,0 \mathrm{~m}$ wide crest. The slope at the waterside was $1 \mathrm{~V}: 3,1 \mathrm{H}$, whereas the slope at the landside was $1 \mathrm{~V}: 2,1 \mathrm{H}$.

Fig. 5 presents a cross-section of the levee and a simplified stratigraphy inferred from borings reported in [11]. The levee consists mainly of two soil layers. The upper soil is a homogeneous cohesive material, underlain by a sandy soil at about $5,5 \mathrm{~m}$ below the levee's crest.
![img-4.jpeg](img-4.jpeg)

Figure 5. The Breitenhagen levee at the failure location, cross-section, and simplified stratigraphy. NHN (Normalhöhennull) corresponds to the vertical datum used in Germany

Some authors conducted forensic assessments to determine the causes of the Breitenhagen levee failure. For example, [11] concluded that the most likely cause of failure was the existence of a conductive layer inside the levee. [12] used a series of photographs taken at the moment of failure to infer a circular slip surface. These authors also identified a pond by the waterside, indicating a possible connection between the aquifer (sand layer) and the landside. A later study, [13], determined that the failure was likely caused by locally weak soils and high water pore pressures in the aquifer. The proposed BN approach is applied and explained in detail in the following sections.

# 5.2. Step 1. Identification of hypothesis nodes 

Hypotheses about possible causes of failure are defined using the evidence collected from previous studies [11], [12]. Two sets of hypotheses are identified. The first set includes three hypotheses related to the following pore pressure conditions (Fig. 6):

- phreatic level elevation,
- existence of a conductive layer, and
- existence of high pore pressures inside the levee due to a pond connection.

The second set consists of hypotheses associated with the parameters of two soil models: MohrCoulomb for drained conditions and SHANSEP for undrained behavior. The Mohr-Coulomb model includes the parameters $\phi^{\prime}$ (effective angle of shear resistance) and $c^{\prime}$ (effective cohesion intercept). The SHANSEP model contains the parameters S (normally consolidated stress ratio), m (strength increase exponent), and POP (pre-overburden pressure).

A unique node is assigned to each pore pressure condition and each soil parameter. For the sake of simplicity, discrete values are used to describe the set of possible states of each node.

Fig. 6 and Table I summarize the hypothesis nodes used in this study and their corresponding discrete states.
![img-5.jpeg](img-5.jpeg)

Figure 6. Levee models for hypotheses related to pore pressure conditions: (a) basic model, (b) phreatic level elevations, (c) existence of a conductive layer, (d) existence of high pore pressures inside the levee due to a pond connection

Table I. Definition of hypothesis nodes and their corresponding states


# 5.3. Step 2. Definition of evidence nodes 

Two evidence nodes are defined to account for observed or behavioral variables. The first node corresponds to the levee's stability condition. This node includes two states: stable and unstable. The stability condition is usually evident and only requires visual inspection. However, some cases require the evaluation of experienced engineers. For the Breitenhagen failure, the unstable condition was inferred from photographs taken during the event [11]. The consequences of the failure (e.g., floods) may also be used to define the levee's stability condition.

The second evidence node refers to the slip surface geometry. Identifying and measuring slip surfaces is a challenging task. Slip surfaces usually disappear after failure or cannot be fully observed. In some cases, the start and end locations of slip surfaces are identifiable. For the Breitenhagen failure, six start and six end locations were defined. Each location represents a possible interval within which start and end points can be observed.

Fig. 7 presents an example of two entry and exit intervals, as well as two potential circular slip surfaces. A total of 36 start-end point combinations are defined. Table II presents the evidence nodes used in the analysis and their corresponding states.
![img-6.jpeg](img-6.jpeg)

Figure 7. Example of potential slip surfaces with entry and exit intervals. Start and end points of slip failures can be observed within these intervals

Table II. Definition of evidence nodes and their corresponding states


# 5.4. Step 3. Causal connections 

The causal relationships between hypothesis nodes and evidence nodes are defined using mathematical models and semantic substructures. Bishop's limit equilibrium equations are used to infer causal connections between nodes representing soil parameters and evidence nodes. On the other hand, causal connections between hypothesis nodes related to pore pressure conditions and evidence nodes are deduced from semantic substructures. For instance, [12, p. 70] describes the causes of levee failure in the following terms: "the levee breach is likely caused by unexpected high pore pressures [...] and unexpected saturation of the levee". [11, p. 35] (translated from German) describes the causes of failure as follows: "the primary cause of damage is a combination of several partial causes such as [...] horizontal water seepage due to a root zone on the waterside". The causal graphs for both Mohr-Coulomb and SHANSEP models are presented in Fig. 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. Causal graphs for the Breitenhagen failure analysis: (a) Mohr-Coulomb (drained) constitutive model, (b) SHANSEP (undrained) soil model

### 5.5. Step 4. Elicitation of conditional probability distributions

The elicitation of conditional probability tables (CPTs) consists of two phases. The first phase includes the definition of prior probabilities for hypothesis nodes. In the case of Breitenhagen failure, no prior knowledge about the causes of failure is available. Therefore, states for each hypothesis node are equally probable and described by discrete uniform distributions.

The second phase involves eliciting the CPTs for evidence nodes. A numerical experiment consisting of 200.000 Monte Carlo simulations is used to infer these CPTs. In the experiment, a random sequence of states is generated based on the prior probabilities of hypothesis nodes. Each sample from the sequence is tested via a slope stability analysis using D-Stability [39] and a Python script.

Bishop's equations are implemented in the slope stability calculations.
The set of results from the calculations (i.e., stability condition and slope geometry) are used to elicit the CPTs of evidence nodes and described by discrete distributions using the states presented in Table II.

Fig. 9 and Fig. 10 depict the BNs for the Breitenhagen failure along with their prior distributions (i.e., no evidence) for both hypotheses and evidence nodes.
![img-8.jpeg](img-8.jpeg)

Figure 9. BN for the drained constitutive model (Mohr-Coulomb) before observing any evidence

# 5.6. Step 5. Entering evidence and evaluating competing hypotheses 

The set of competing hypotheses is evaluated by entering the available evidence into the BN. The evaluation begins by defining the set of hypotheses. Each competing hypothesis represents a combination of states in the hypothesis nodes. For example, hypothesis H1, defined as a saturated levee, proposes a high phreatic level ( $\mathrm{PL}=\mathrm{High}$ ) as the cause of failure. For H 1 , there is no existence of a conductive layer $(\mathrm{CL}=\mathrm{No})$ nor a pond connection $(\mathrm{PC}=\mathrm{No})$. Moreover, the soil parameters assume intermediate values. Four additional competing hypotheses similar to H 1 are presented in Table III.

Table III. Five competing hypotheses about the causes of the Breitenhagen levee failure


![img-9.jpeg](img-9.jpeg)

Figure 10. BN for the SHANSEP soil model before observing any evidence
Once the competing hypotheses are defined, a set of probability queries are constructed using the available evidence. Two types of probability queries are identifiable depending on their structure: predictive and abductive. Predictive queries ask about the probability of observing the available evidence, provided that a hypothesis is met. For instance, Eq. (5) represents the probability of observing an unstable condition with the slip geometry $\mathrm{SG}_{12}$, provided that hypothesis H 1 is met.

$$
P\left(S C=\text { Unstable }, S G\left|S G_{12}\right| S T=\text { High }, C L=N o, P C=N o\right)
$$

On the other hand, abduction queries use the BN to answer questions about the probability of observing a hypothesis given the available evidence. Eq. (6) represents the abduction query for the

probability of observing hypothesis H 1 , given that the slope is unstable, and the slip failure has a geometry represented by $\mathrm{SG}_{12}$.

$$
P\left(S T=\text { High }, C L=N o, P C=N o \mid S C=\text { Unstable }, S G=S G_{12}\right)
$$

The competing hypotheses from Table III. are just five out of thousands of available credible hypotheses resulting from combining the states of the hypothesis node.

Given this large number of hypotheses, the K-MPE algorithm is implemented. In this study, the K-MPE algorithm is used to find the best three explanations for the Breitenhagen levee failure.

# 6. Results 

Table IV shows the results for the probability queries performed on hypotheses H 1 to H 5 . When the BN is used as a predictive tool, hypothesis H 4 better predicts the available evidence than the rest of the hypotheses. In other words, a saturated levee, along with weak soils, is more likely to lead to an unstable condition with the slip geometry $\mathrm{SG}_{12}$. Fig. 11 depicts the instantiations for the predictive query associated with H 4 in drained condition.

When the BN is used for abductive reasoning, the available evidence $\left(\mathrm{SC}=\right.$ Unstable, $\left.\mathrm{SG}=\mathrm{SG}_{12}\right)$ is better explained by hypothesis H 4 than $\mathrm{H} 1, \mathrm{H} 2$, and H 3 . However, the probability of hypothesis H5 does not show a significant difference in comparison to H4. Therefore, H5 is also a reasonable explanation for the Breitenhagen levee failure.

Table IV. Results for predictive and abductive queries performed on hypotheses H 1 to H 5


The K-MPE algorithm was implemented to find the most probable explanations. Table V lists the $K=3 M P E$ for the drained soil constitutive model, along with the instantiations of the hypothesis nodes. For the drained condition, the best explanation for the levee failure is the existence of a conductive layer and low values of soil strength parameters. Interestingly, the second and third best explanations are also related to low values of $\mathrm{c}^{\prime}$ and $\phi^{\prime}$. None of the $K=3 M P E$ includes the pond connection as an explanation for the levee failure.

Table VI lists the $K=3 M P E$ for the undrained soil constitutive model. In this case, the best explanation is the simultaneous existence of a high phreatic level, a conductive layer, and low POP values. As with the drained condition, a pond connection does not explain the levee failure.

![img-10.jpeg](img-10.jpeg)

Figure 11. Updated nodes for a predictive query associated with H4 (drained condition)

Table V. $K=3 M P E$ for the drained soil constitutive model


Table VI. $K=3$ MPE for the undrained soil constitutive model


# 7. Discussion 

The Bayesian Network approach presented in this study proposes a substantial advance for objectively determining the causes of levee failures. The five steps of the approach quantitatively account for credible hypotheses as causes of failure. Moreover, the collected evidence is transparently included in the process in order to draw conclusions based on probabilistic and abductive reasoning.

To date, little research has been published on the role of Bayesian Networks in investigating causes of geotechnical failures. For example, [13] propose a Bayesian-based method to update prior probabilities of failure scenarios by including collected evidence. However, said approach does not account for multiple or simultaneous causes due to assumptions related to mutual exclusivity in probabilistic analysis. The BN approach overcomes this limitation by assigning a node to each credible hypothesis without restricting the simultaneous occurrence of two or more events.

Other approaches, such as the ones proposed in [10], use BNs to diagnose the causes of failures based entirely on data. The probability relationships (i.e., CPTs) are learned from data without resorting to physical-based models. Although this approach could reach reasonable conclusions, data from failures is scarce and is not always available. The BN approach overcomes these shortcomings by building probability relationships via mathematical models broadly accepted by the geotechnical community.

In this work, the BN approach was applied to the Breitenhagen levee. The results demonstrate the capabilities of BN to draw conclusions about the causes of failure. The most probable explanation seems to be the simultaneous existence of a high phreatic level, a conductive layer, and low soil resistance values. Not surprisingly, this conclusion appears to agree well with previous studies based on sensitivity analysis [12] and traditional forensic analysis [11]. However, the results contradict the findings of [13], which associate the failure with high pore pressures due to a pond connection to an aquifer.

The levee failure assessment using the BN approach is based on several assumptions. For instance, independence between hypothesis nodes is assumed, even though it is known that some soil parameters are correlated. Furthermore, some hypothesis nodes associated with pore water pressures could not be independent in the sense that, for example, a pond connection to an aquifer could lead to a reduction in the phreatic level. In that case, an edge between the two hypothesis nodes should be included. The results obtained from step 4 were used to confirm the independence of the hypothesis nodes. In this case, several BN structures were built using only data obtained from simulations. The best-rated BN structures did not show a correlation between the hypothesis nodes.

Another assumption is that the hypothesis nodes are collectively exhaustive. In other words, the BN encompasses the entire range of possible causes leading to failure, and at least one of them must occur to explain the failure. Other possible causes could be disregarded if they are not included in the BN. Hence, credible hypotheses should be proposed using engineering expertise.

The steady-state condition assumed for pore water pressures is a significant limitation that could lead to erroneous conclusions about the causes of failure [13]. For the Breitenhagen levee failure, the pond connection seems to be irrelevant due to the high impact of the phreatic line position. The three most probable explanations derived from the K-MPE metric corroborate this assumption when comparing their probabilities of occurrence. However, unsteady conditions for piezometric pressures could be relevant. Further research studies could evaluate the influence of transient flow and assess the statistical significance between different failure scenarios using metric criteria such as the Bayes factor or the log likelihood function.

Data from slope stability simulations are used to elicit the CPTs. In this study, the limit equilibrium method and drained/undrained constitutive models (Mohr-Coulomb and SHANSEP) are used. Although finite element methods and unsaturated soil constitutive models could better represent the actual condition of the levee, the computational cost is considerably higher. Consequently, analysis methods and constitutive soil models should be selected based on accuracy requirements, the engineers' experience, and available evidence.

The proposed BN approach can be generalized to any type of forensic geotechnical assessment, including but not restricted to failures in dams, slopes, foundations, and excavations. The results from this study demonstrate its capability for drawing objective conclusions about the causes of geotechnical failures.

# 8. Conclusions 

A straightforward Bayesian Network approach to support decisions in forensic geotechnical engineering is presented. The approach follows a five-step sequence that reflects the generic forensic engineering process for failure assessment. Furthermore, it includes the mathematical consistency of Bayesian Networks. BNs can significantly improve the accuracy and transparency of forensic conclusions by supporting their findings on probability and abductive reasoning.

Unlike traditional forensic approaches, competing hypotheses about the causes of failure can be probabilistically compared. Besides, BNs can simultaneously deal with multiple hypotheses and find the most probable explanation to geotechnical failures.

The BN approach is applied to investigate the causes of the Breitenhagen levee failure. Three failure scenarios related to pore water conditions and two soil constitutive models with their corresponding parameters are used as hypotheses about causes of failure. Causal connections between hypothesis nodes and evidence nodes are defined through a mathematical model and common geotechnical idioms. In the case under study, the CPTs were estimated from thousands of slope stability simulations using the states of hypothesis nodes. Evidence collected from failure was used to update the BN through predictive and abductive queries.

The three most probable explanations for the levee failure were estimated using the K-MPE algorithm. A high phreatic level combined with a conductive layer and low soil strength parameters seems to be the most probable cause of failure.

The BN approach can be applied in any forensic geotechnical assessments where several competing hypotheses need to be evaluated. However, the computational effort and time required for calculation could limit its use. Future work should prioritize: 1) building efficient BN structures for describing forensic assessments and 2) extending the BNs approach to analyzing geotechnical failures in foundations, excavations, slopes, and dams.

# William Mauricio García-Feria 

PhD candidate in Civil Engineering, Universidad Nacional de Colombia; Master's in engineering - Geotechnics, Universidad Nacional de Colombia. He belongs to the GENKI (Geotechnical Engineering Knowledge and Innovation) research group.
Email: wmgarciaf@unal.edu.co

# Julio Esteban Colmenares-Montañez 

PhD in Engineering, Imperial College of London; Master of Science in Soil Mechanics and Environment, Imperial College of London; professor at Universidad Nacional de Colombia. Director of the GENKI (Geotechnical Engineering Knowledge and Innovation) research group.
Email: jecolmenaresm@unal.edu.co

## Germán Jairo Hernández-Pérez

PhD in Engineering, Computer Science, The University of Memphis; Master's in computer science, The University of Memphis; professor at Universidad Nacional de Colombia. Director of the ALGOS-UN (algorithms and combinatorics) research group.
Email: gjhernandezp@gmail.com