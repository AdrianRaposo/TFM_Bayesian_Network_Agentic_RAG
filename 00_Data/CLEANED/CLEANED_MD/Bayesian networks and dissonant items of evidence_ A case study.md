# Bayesian networks and dissonant items of evidence: a case study 

Ilaria De March, Franco Taroni

School of Criminal Justice, University of Lausanne, Switzerland


#### Abstract

The assessment of different items of evidence is a challenging process in forensic science, particularly when the relevant elements support different inferential directions. In this study, a model is developed to assess the joint probative value of three different analyses related to some biological material retrieved on an object of interest in a criminal case. The study shows the ability of probabilistic graphical models, say Bayesian networks, to deal with complex situations, those that one expects to face in real cases. The results obtained by the model show the importance of a conflict measure as an indication of inconsistencies in the model itself. A contamination event alleged by the defense is also introduced in the model to explain and solve the conflict. The study aims to give an insight in the application of a probabilistic model to real criminal cases.


Keywords: DNA evidence; Activity level interpretation; Bayesian networks; Conflict measure

## 1 Introduction

DNA is often considered as a gold standard in forensic science [1, 2]; its ability to link a stain to an individual and its high selectivity fascinate courts of justice. The improvements in DNA profiling technologies currently make it possible to obtain complete profiles from low amounts of biological material.

[^0](c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/


[^0]:    *Corresponding author: ilaria.demarch@unil.ch

As a consequence, questions relating how the biological material came on an object of interest rather than questions about who the biological material is linked are raising more and more attention [3, 4]. In particular, DNA evidence evaluation (throughout the use of the likelihood ratio as the measure of the value of recovered material) considering propositions at an activity level $[5,6]$ is recommended by the ENFSI Guidelines for Evaluative Reporting in Forensic Science [7] in cases that involve small quantities of biological material. The evidence evaluation under activity level propositions requires the assessment of a number of complex mechanisms that are often case dependent [8]. In the past few years, a lot of studies and publications were focused on the transfer, persistence, prevalence, and recovery mechanisms (see [9] for an extensive review). The literature provides valuable knowledge on the impact of the aforementioned mechanisms and proves their strong dependency on case circumstances.

Additional troubles arise when a joint assessment of different scientific results has to be performed. In these cases, the assessment can prove to be very challenging, in particular when the analytical results individually tend to support different propositions.

The aim of this work is to present a case study in which three dissonant [10] scientific results are of interest, all related to the biological field and obtained from analyses made on the same object.

Although inspired from a real criminal case, the relevant circumstances have been slightly changed for the purpose of the study. The analysis is performed by the aid of a Bayesian network (BN for short) allowing one to structure the variables relevant to the problem in a logical way [11].

The article is structured as follows: in Section 2 the context of the case is presented, as well as the relevant forensic results. Section 3, after a brief technical definition of BNs, describes the development of a model taking into account the different elements that characterize all the relevant information to deal with in the case at hand. The relationships between the different elements are studied, in order to analyze how they impact on each other. Section 4 presents the results obtained from the model; a discussion about the results and some final remarks can be found in Section 5.
(C) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

# 2 Scenario 

The scenario of interest is the following: a victim $(V)$ is found stabbed to death in her flat where she lived alone. According to several witnesses, $V$ used to wear a golden necklace, which is not found on the body, nor on the crime scene or in the rest of the victim's apartment. About a month later, a suspect $(S)$ is apprehended; during the search of $S$ 's flat, a broken necklace is recovered and seized for forensic analysis. While $S$ declares that the necklace is a family object, and that it has not been touched for years, the prosecution claims that the necklace belonged to $V$, and that it has been snatched off the victim's neck by $S$ during the aggression. No other forensic element is retrieved. The question about whether that necklace is the victim's one becomes then crucial for the trial. A first forensic laboratory (say, Lab 1) performs a DNA analysis on the necklace, as well as a presumptive test to detect the presence of human cells. No DNA profile can be obtained by this analysis, and the presumptive test previously gave a negative result, too. A few months later, a second forensic laboratory (say, Lab 2) repeats a DNA analysis on the object, resulting in a complete profile corresponding to that of $V$. This second result plays a key role at trial. Indeed, the court established that the necklace was precisely the one of the victim, snatched by $S$ during the aggression that lead to the dead of the victim herself. $S$ was then sentenced for the murder of $V$.

## 3 Graphical models

The analysis of this scenario has been performed by using a probabilistic environment, namely a Bayesian network.

### 3.1 A brief definition of Bayesian networks

A Bayesian network is a directed acyclic graph (DAG) composed by nodes, that represent the variables relevant to the problem, connected by directed edges, that symbolize the probabilistic relationships between variables. A conditional probability table (CPT) is associated to each node ${ }^{1}$ and shows the

[^0](c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/


[^0]:    ${ }^{1}$ Note that in this case only discrete nodes have been considered. Bayesian networks can also include continuous nodes; in the latter case, the CPT refers to the probability density function associated to the node.

probability distribution of each state of the node (i.e. the true value that the variable can assume) depending on the states of the node's parent variables. A node, $A$, is called to be parent of a second node, $B$, if the edge that connects them departs from $A$ directed to $B$. Stated otherwise $A$ is a parent node of $B$ because its true state conditions the true state of $B$. Therefore, $B$ is called a child node of $A$.

The joint probability of the set of variables $\left\{X_{1}, \ldots, X_{n}\right\}$ composing the model is equal to:

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \operatorname{par}\left(X_{i}\right)\right)
$$

where $\operatorname{par}\left(X_{i}\right)$ is the set of the parent nodes of the variable $X_{i}$.
This latter equation is called the chain rule of Bayesian networks and formally defines the meaning of a Bayesian network: a representation of the joint probability distribution for all the variables. It can be observed that variables $X_{1} \ldots X_{n}$ are conditionally independent given their parents.

The following sections show, step-by-step, the development of a Bayesian network modeling the case described in Section 2.

# 3.2 The model at time $t_{0}$ 

Let's consider time $t_{0}$ to be the moment of the aggression of the victim $V$. The first part of the model concentrates on whose and how much DNA was on the necklace at that moment. Of course, this depends on what actually happened, stated otherwise, on whether the prosecutor's version of facts (indicated by $H_{p}$ ) or the defense's $\left(H_{d}\right)$ is true:

- $H_{p}$ : The suspect snatched the necklace off the victim's neck during the aggression.
- $H_{d}$ : The necklace belongs to the suspect and has not been touched for years.

It is worth noting that other propositions could be specified, both under the prosecutor's and the defense's point of view. These alternatives are not considered in this work, since they were not put forward by parties at trial.

The relevant variables that allow one to represent the situation at time $t_{0}$ are structured in the BN showed in Figure 1. This structure corresponds
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

to an extension of the Bayesian network accounting for evidence evaluation given activity level propositions [11].
![img-0.jpeg](img-0.jpeg)

Figure 1: Part of the Bayesian network representing the situation at time $t_{0}$-the time of the aggression. The states of node $H$ represent the two competing propositions of interest.

The two nodes denoted Background account for the DNA quantity of a single source (victim or suspect) already present on the necklace at the moment of the aggression. The states of each node are None (no DNA at all), Low, Medium and High DNA levels. For the node Background suspect, and assuming $H_{p}$ to be true, we expect that no DNA originating from the suspect is present on the necklace before the aggression. This corresponds to a probability of 1 assigned to the state None (absence of DNA). On the contrary, if $H_{d}$ is true, the necklace has not been touched for years, and the suspect cannot even tell if she ever wore it. For these reasons, the most plausible result is to observe no background DNA (state None); low, medium or high quantities of DNA are considered as far less probable. The probability assignments for this node are shown in Table 1a.

With an analogous reasoning, if we consider that $H_{d}$ is true, the state None of node Background victim has a probability of 1. In fact, the DNA of the victim is not expected to be on a necklace belonging to the suspect. On the other hand, if $H_{p}$ is true, the amount of DNA expected to be on the necklace is of the order of nanograms [12]. So, the state Medium is considered to be the more probable. The probability assignments for this node can be found in Table 1b.
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

Table 1: Conditional probability tables for the nodes related to the DNA already present on the necklace (background) at the moment of the aggression.
(a) CPT for the node Background suspect


(b) CPT for the node Background victim


The two nodes called Transfer model the quantity of DNA transferred by each of the two sources on the necklace at the moment of the aggression. For both nodes, under $H_{d}$, the quantity transferred has to be None (absence of DNA), since, of course, if the suspect's version of facts is true the necklace was in the suspect's jewelry box at the moment of the aggression.

Under $H_{p}$, the two nodes present similar conditional probability tables (see Tables 2a and 2b). The states Low and Medium are considered the most probable for both nodes [13, 14, 15]: in the node Transfer victim necklace, the state Medium is considered slightly more probable than Low, on the basis of the broader surface of the necklace that could have been in contact with the victim. Conversely, for the node Transfer suspect necklace, the state Low is considered the most probable, since under this description of the facts only the suspect's hand would have been in contact with the necklace, and only for a short time.

The quantity of DNA transferred during the action is influenced by a large number of parameters: the intensity of the action and possibly its duration in time [see, e.g., 16, 17, 18], the intrinsic properties of the surface [19, 20], the shedding properties of the donor [21, 22, 23, 14], as well as other external factors such as the actions performed before the activity of interest [23].

Despite a large number of studies have been conducted regarding the quantity of touch DNA transferred during a particular activity [see, for instance, 17, 13, 16, 19, 24], their results can not be easily applied to the variety of parameters mentioned above and that characterize the case under investigation. For example, the shedding properties of the subjects implied
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

Table 2: Conditional probability tables for the nodes related to the DNA of one of the two possible sources transferred on the necklace at the moment of the aggression.
(a) CPT for the node Transfer suspect necklace.


(b) CPT for the node Transfer victim necklace.


(victim and suspect) are difficult to be investigated, as well as the actions performed before the alleged activities.

For this reasons, the states corresponding to the nodes Transfer and Background, as well as to other nodes presented in the following steps, will represent broad and qualitative categories rather than more precise quantities. Nevertheless, those studies allowed us to restrict the number of categories (quantities greater than nanograms are not expected to be observed [14], that is the reason why all quantities above nanograms are grouped in the same state "High").

Finally, the node $D N A$ at $t_{0}$ stands for the total amount of DNA present on the necklace at the moment of the aggression. The states of the variable take into account all the possible sources of the biological material (suspect, victim, or a mixture of both), and the potential quantities, described again in the categories specified before. The states relative to this node are listed in Table 3.

The states reported in Table 3 cover all the possible combinations of sources and quantities relevant for the case at hand, and it will be employed again to represent the states of other nodes in the network - notably $D N A$ at $t_{1}$ (Section 3.3), DNA at $t_{2}$ and DNA extracted Lab 1 (Section 3.4), DNA extracted Lab 2 and Results Lab2 (Section 3.5). It is important to stress here that the presence of DNA from a third donor is not considered in this work, since the case circumstances and the two parties' versions of facts suggest a close-set situation; an extension of the model including also DNA coming from an extraneous source is nevertheless theoretically possible.
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

Table 3: List of the states accounting for all the combinations of DNA sources and quantities relevant for the case. These states define several nodes in the model, namely $D N A$ at $t_{0}$ (Section 3.2), $D N A$ at $t_{1}$ (Section 3.3), $D N A$ at $t_{2}$ and $D N A$ extracted Lab 1 (Section 3.4), DNA extracted Lab 2 and Results Lab 2(Section 3.5).


The CPT for the node $D N A$ at $t_{0}$ has been filled logically, by summing the DNA coming either from the background or the transfer mechanism. Regarding the quantities, the following rules have been applied:

- When two different quantities are summed, a probability of 1 is assigned to the higher quantity. For example, for the column corresponding to Transfer suspect necklace $=$ Low, Background victim $=$ Medium, Background suspect $=$ None and Transfer victim necklace $=$ None, a probability of 1 will be assigned to the state $V+S$, medium.
- When the same quantity characterizes the states of parent nodes, a probability of 1 is assigned to a state corresponding to the same quantity. For example, for the column corresponding to Transfer suspect necklace $=$ Low, Background victim $=$ Low, Background suspect $=$ None and Transfer victim necklace $=$ None, a probability of 1 will be assigned to the state $V+S$, low.

The CPT for this node can be found in Supplementary Table 1.
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

# 3.3 The model at time $t_{1}$ 

The second part of the network considers the moment the necklace was seized by the police, one month after the aggression.
![img-1.jpeg](img-1.jpeg)

Figure 2: Extension of the network that includes the two nodes accounting for the situation at $t_{1}$, that is, the moment the necklace was seized.

As it is shown in Figure 2, this part of the network is composed by two nodes:

1. $D N A$ at $t_{1}$, that, similarly to $D N A$ at $t_{0}$, accounts for the total amount of DNA present on the necklace at the moment of the seizing;
2. Cleaning, a variable that models the possible cleaning of the necklace during the month between the aggression and the seizing.

This second variable has two possible states: Cleaning cloth and None. An additional state could take into account the possibility that the necklace was cleaned with specific chemical products; since this would entail the recovery of fragmented DNA, if any, and that it is not an action allegedly performed by the suspect, this additional possibility has not been considered, leaving only the two aforementioned states to describe this variable. Under $H_{d}$ the state None has a probability of 1 (and conversely, the state Cleaning cloth has a probability of 0 ), in line with the suspect's declarations about the necklace. Under $H_{p}$, the probability values are set as equivalent for the two states. The CPT describing this node is illustrated in Table 4.

The node $D N A$ at $t_{1}$ has the same 10 states as node $D N A$ at $t_{0}$, that is, those listed in Table 3. The probability values assigned in this conditional
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

Table 4: CPT for the node Cleaning.


probability table are essentially related to the persistence of DNA on the object. Under $H_{d}$, and knowing that the necklace has not been cleaned (the state Cleaning $=$ Cleaning cloth is impossible under $H_{d}$ ), the persistence probability is considered equal to 1 . In fact, according to the suspect, the necklace had been stored in a confined place for years, not being manipulated. Therefore, it can be considered that the most important loss of DNA occurred in the weeks that followed the last DNA deposition on the object, years back, and that no relevant loss occurred in the month between the moment the victim was killed and the moment the necklace was seized [8].

The probability values assigned to the states of this node under $H_{p}$ can be found in the Supplementary Table 2. The table has been filled with the following rules: for the state Cleaning $=$ None, a probability of 0.9 has been assigned to the corresponding state in the table, and the complementary, 0.1 , has been assigned to the lower category. For instance, the probability $P(\mathrm{DNA}$ at $t_{1}=$ $V$, medium $|\mathrm{DNA}$ at $t_{0}=V$, medium, Cleaning $=$ None, $\left.H_{p}\right)=0.9$ and $P(\mathrm{DNA}$ at $t_{1}=$ $V$, low $|\mathrm{DNA}$ at $t_{0}=V$, medium, Cleaning $=$ None, $\left.H_{p}\right)=0.1$.

Under this version of facts, after the aggression the necklace would have been transferred to the suspect's apartment and stored in the jewelry box. The persistence of the DNA on the necklace would then only be affected by the initial manipulations, and can therefore be considered as quite high.

For the values corresponding to the state Cleaning $=$ Cleaning cloth the same rule detailed previously has been applied, using this time the values 0.3 and 0.7 . It is considered, in fact, that the use of a cleaning cloth, while heavily diminishing the total amount of DNA present on the external surface of the necklace, would not affect the DNA present in-between the chains.

# 3.4 The model at time $t_{2}$ 

The part of the network shown in Figure 3 is intended to model the results obtained by the first forensic laboratory (Lab1).
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

![img-2.jpeg](img-2.jpeg)

Figure 3: Part of the network that models the results of Lab1. It is connected to the rest of the network, showed in Figure 2, through the node DNA at $t_{1}$.

The quantity at disposal at the beginning of the analysis is considered to be exactly the quantity described in node $D N A$ at $t_{1}$. This assumption is justified by the short delay between the seizing of the necklace and the beginning of the forensic analysis on the object.

The node Method 1 describes the sampling technique chosen by the first forensic laboratory. This node has two states (Swab and Other). This node is not intended to model the uncertainty related to the sampling technique it is known for sure that the laboratory swabbed the object - but rather to make explicit in the model the dependency of the results on the technique chosen. The node Method 1 in fact, has an influence on the nodes Proportion and Efficiency.

The node Proportion models the uncertainty about the proportion of the object that has been sampled. It is considered that, given the lack of visible stains, the sampling has been performed on the majority of the outer surface of the necklace - that is, not in-between the chains.

The node Efficiency models both the sampling and the extraction efficiency. In their article, Wood et al. [25] found that the quantity of DNA extracted when sampling a biological stain with the swab method varied along with the nature of the surface carrying the stain and with the swab characteristics. The efficiency described in this study for metallic surfaces varies between around 5 and $20 \%$ of the total amount of biological material present in the stain. These values are in line with those found by Butts [26], who described
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

an average efficiency comprised between 7 and $16 \%$. The CPTs for the nodes Proportion and Efficiency are shown in Tables 5a and 5b.

Table 5: Conditional probability tables for the nodes Proportion and Efficiency relative to the method applied in Lab 1. Extreme values ( $0-70 \%$ and $90-100 \%$ for Table 5a; $0-5 \%$ and $30-100 \%$ for Table 5 b ) are set equal to zero, and for sake of simplicity are not shown in Tables.
(a) CPT for the node Proportion.


(b) CPT for the node Efficiency.


The initial amount of DNA present on the necklace ( $D N A$ at $t_{1}$ ) as well as the proportion sampled and the efficiency of the method have an impact on the amount of DNA extracted from the sampling [15], described by the variable DNA extracted Lab 1. This variable has the same states shown in Table 3, and its CPT is illustrated in the Supplementary Table 3. It is intended to model the reduction of the DNA extracted - thus, available for analysis with respect to the amount that was present on the exhibit previously to the sampling, depending on the sampling and extraction efficiency, as well as on the proportion of the exhibit that has been sampled.

The node DNA extracted Lab 1 has an impact on two other variables: Results Lab 1, modeling the results of the genetic profile obtained by the first laboratory, and Presumptive test, accounting for the result of the analysis of the mitochondrial DNA, targeting the region cytochrome $b$ and aiming to detect the presence of human cells ${ }^{2}$.

The analysis of the cytochrome $b$ has proved to give positive results even in presence of low amounts of biological material [27]. Nevertheless, in this case analysis, the probability to obtain a false negative result for small amounts of DNA has not been neglected. The CPT for this node is shown in Table 6.

The CPT for the variable Results Lab 1 is presented in Table 7. The states for this node correspond to the genetic profiles expected to be observed:

[^0](c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/


[^0]:    ${ }^{2}$ It is worth noticing that a different kind of presumptive test - notably, a presumptive test not requiring the DNA extraction - would entail a different structure of the model.

Table 6: CPT for the node Presumptive test. A probability of 0.2 has been assigned to account for a false negative result, when dealing with a low quantity of material extracted.


a profile corresponding to that of the victim (state V), to that of the suspect (state S), to a mixture including both $(\mathrm{V}+\mathrm{S})$, or no profile retrieved (No profile). These states do not specify if the retrieved profile is complete or partial; an extension of the conditional probability table to take into account these two possibilities could be envisaged. For low amounts of extracted DNA, a probability of 0.2 has been assigned to the state "No profile", accounting for the possibility that the quantity extracted is too low to be efficiently amplified and sequenced.

Table 7: CPT for the node Results Lab 1.


The amount of DNA at disposal previous to the analysis ( $D N A$ at $t_{1}$ ) as well as the proportion of the object that has been sampled will influence the amount of DNA at disposal on the necklace after the sampling process, modeled in the variable $D N A$ at $t_{2}$. The CPT for this node is represented in the supplementary Table 4, and is defined by the states shown in Table 3. The variable $D N A$ at $t_{2}$ mainly accounts for a reduction of the total amount of DNA present on the necklace with respect to the values shown in the variable $D N A$ at $t_{1}$, depending on the proportion of the object that has been sampled.
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

# 3.5 Model at $t_{3}$ 

Finally, this part of the model describes the result of the analysis conducted by the second forensic laboratory (Lab 2) and it is shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4: Part of the network that models the result of Lab 2.
It is structured following the same logic of the previous part (see Section 3.4), except for the absence of a node Presumptive test, this one not having been performed by the second laboratory. In this case, the sampling method represented by the node Method 2 is the direct immersion of the necklace in an extraction solution. Given the sampling technique, the proportion of the exhibit that has been sampled is considered to be around 1 ; therefore, the node Proportion is not intended to model the uncertainty about this factor, but is introduced as a reminder of the general dependency of the DNA extracted on this variable. For the node Efficiency, the same states previously defined have been considered. The probability table for this node is shown in Table 8. Given the sampling technique applied, an higher probability for the efficiency of the immersion technique has been assigned to the state " $15-20 \%$ " with respect to the others states of the variable [26].

Table 8: CPT for the node Efficiency relative to the method applied in Lab 2. Extreme values ( $0-5 \%$ and $30-100 \%$ ) are set equal to zero and have been omitted for simplicity.


(C) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

The CPT for the node DNA extracted Lab 2 in presented in the Supplementary Table 5. The node Results Lab 2 is described by the states listed in Table 3. The table has been constructed following the same logic as the CPT of the node Results Lab 1, with the exception that in this case, the amplification and sequencing techniques applied in the second laboratory are more sensitive, and therefore able to report a result even in presence of low amounts of material. Table 9 illustrates the CPT for this node.

Table 9: CPT for the node Results Lab 2.


By combining the sub-models previously detailed in Sections 3.2 to 3.5, the full structure of the Bayesian network for this case can be obtained, as illustrated in Figure 5.

# 3.6 The possibility of a contamination event 

After the Lab 2 having obtained a complete profile corresponding to the victim from the necklace, the defense claims that this could have been produced as a result of a contamination. The necklace is in fact known having been transferred from Lab 1 to Lab 2 at the same time with other objects seized at the crime scene, and having been sampled in laboratory 2 at the same time with those objects. According to the defense, a part of the biological material originated by the victim could have been indirectly transferred on the necklace, causing its detection during the analysis of laboratory 2 [28]. In order to take into account this new allegation, the Bayesian network shown in Figure 5 has been updated by introducing a node Contamination (hereafter shorten in $C$ for sake of clarity). This node representing the indirect transfer of an
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

![img-4.jpeg](img-4.jpeg)

Figure 5: Complete Bayesian network describing the case of interest.
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

unspecified quantity of the victim's DNA, its states are "None", indicating that no contamination occurred, and "V, low", standing for the indirect transfer of a minute quantity of DNA (in the order of picograms) stained from the victim upon the necklace during the post-analytical phase in Lab 1 or the pre-analytical phase in Lab 2. The states " $C=$ medium" and " $C=$ high" being considered more likely in cases where a direct and gross contact occurred, they have been neglected from this probabilistic analysis. The final structure of the Bayesian network, including the node Contamination, is illustrated in in Figure 6. The new CPT for the node DNA at $t_{2}$, accounting for the effect of a possible contamination, is presented in Supplementary Table 6 .

# 4 Results 

The likelihood ratio (LR) is the commonly accepted measure to assess the probative value of a forensic finding $[29,30,31,32]$.

The LR accounts for the ratio between the probabilities to observe a set of forensic results (denoted as $E_{1}, \ldots, E_{N}$ ) given at least two alternative propositions of interest. In this case, exactly two propositions will be considered, say $H_{p}$ and $H_{d}$ (see Section 3.2 for the definition of the propositions):

$$
L R=\frac{P\left(E_{1}, \ldots, E_{N} \mid H_{p}\right)}{P\left(E_{1}, \ldots, E_{N} \mid H_{d}\right)}
$$

In the case at hand, there are three forensic results that need to be assessed (see also [33]), namely:
$E_{1}$ The negative result of the presumptive test performed by Lab 1;
$E_{2}$ The negative result of the DNA analysis reported by Lab 1;
$E_{3}$ A low quantity of DNA corresponding to the victim's profile retrieved in Lab 2.

The use of a graphical model facilitates calculations. When instantiating the relevant variables (Presumptive test $=$ Negative, Results Lab $1=$ No profile, Results Lab $2=\mathrm{V}$, low), the Bayesian network illustrated in Figure 5 produces a likelihood ratio that tends to infinity, reflecting the fact that the probability of observing the results (in particular, the complete profile of
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

![img-5.jpeg](img-5.jpeg)

Figure 6: Development of the Bayesian network illustrated in Figure 5, including the new node Contamination. This last node affects the amount of DNA available for the analysis of the second laboratory.
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

the victim) given the defense's point of view is equal to 0 . Stated otherwise, there is no reason for the victim's DNA to be on the necklace if the defense's version of facts is true. It is important to underline that the likelihood ratio would always tend to infinity when these variables are instantiated (i.e., Presumptive test $=$ Negative, Results Lab $1=$ No profile, Results Lab $2=\mathrm{V}$, low), independently from the specific values assigned in the CPTs linked to all other variables.

Results obtained by instantiating variables of this network can still be more carefully analyzed by studying the potential conflict existing between the two laboratories' results. Formally speaking, the conflict measure [34, 11] is defined as

$$
\operatorname{conf}(E)=\log \frac{\prod_{i=1}^{n} P\left(E_{i}\right)}{P\left(E_{1}, \ldots, E_{n}\right)}
$$

where $E_{i}$ represents a single scientific finding and $E$ the whole body of evidence at disposal. A positive conflict measure describes the situation where the joint probability of all the elements of evidence is lower than the multiplication of the probabilities of every single item, meaning that some of the items of evidence have an inferential direction opposed to the others $[10,35]$.

When considering the qualitative and quantitative aspects of the model depicted in Figure 5, the conflict measure is around 1.8, reflecting a situation in which two items of evidence (the negative results of the presumptive test and of the DNA analysis of Lab 1) tend to favor $H_{d}$ while the third item of evidence (the positive result of the DNA analysis in Lab 2) tends to favor $H_{p}$. The conflict measure obviously depends on the particular probability values assigned to the different CPTs. In order to in-depth explore this aspect, a sensitivity analysis has been conducted on the variables that have not been informed by published data. The analysis has been conducted by widely varying the values for nodes Cleaning, $D N A$ at $t_{1}, D N A$ at $t_{2}, D N A$ extracted Lab 1 and DNA extracted Lab 2, and by studying the impact of the different probability values on the conflict measure. Note that a sensitivity analysis on the likelihood ratio cannot be performed, since the likelihood ratio always tends to infinity in this case. DNA extracted Lab 1 represents the variable that individually minimizes the conflict value. In particular, if it is consider the extreme case for which, independently from the efficiency of the technique and the proportion of necklace that has been sampled, the quantity of DNA extracted is alway in the lower category with respect to
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

the real quantity present on the object, then the conflict measure results equal to 0.86 . This reflects a common sense observation: if the techniques used in Lab 1 are not able to efficiently extract - and then sequence the DNA present on the necklace, the different results obtained by the two laboratories can be explained. It is worth noting that, even under this scenario, the conflict measure is always positive. Stated otherwise, it does not exist one single variable in the model that can individually solve the conflict. In order to study the joint effect on the conflict measure of different probability assignations, two additional simulations have been performed. In the first simulation, the probability values for the aforementioned variables correspond to the values producing, individually, a maximization of the conflict (see Tables 7 to 11in Supplementary material for the values corresponding to each variable). Similarly, the second simulation was performed by assigning to each variable the values that individually minimized the conflict (see Tables 12 to 16 in Supplementary material). For both simulations, a conservative assumption was made in order to fill the CPT of the nodes DNA extracted Lab 1 and DNA extracted Lab 2: that is, the techniques used by the second laboratory are considered able to extract a quantity of DNA corresponding to the category actually present on the necklace, independently from the proportion sampled and the extraction efficiency. On the contrary, for the first laboratory, a probability of 0.2 has been assigned to the states "Low" when the quantity of DNA actually present on the necklace was "Low". Conversely, a probability of 0.8 has been assigned to the state "None" - that means, no DNA extracted. Again, this conservative assumption does not take into account the dependence of the quantity extracted on the proportion swabbed and on the efficiency of the extraction. This point is somewhat in contrast with the logic behind the network construction, and can be accepted only in the context of the sensitivity analysis. The conflict values obtained from the first and second simulation are, respectively 4.15 and 0.12 . It is worth noting that both simulations result in a positive conflict value; as observed before, even a conservative set of probability assignations is not able to fully explain away the conflict.

When introducing the Contamination variable (see Figure 6) the results of the model change substantially.

First of all, it can be noticed that the likelihood ratio does no longer tend to infinity. In fact, $C$ allows for the victim's DNA to be retrieved on the necklace even if $H_{d}$ is true. The likelihood ratio that can be obtained depends of course on the probability values that describe the variable $C$, as
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

well as on the probability values assigned to the other variables. As specified above, the decision was made to assign values between 0.8 and 1 to the prior probability that no contamination occurred $(P(C=0) \in[0.8,1))$. Conversely, a probability comprised between 0 and 0.2 has been assigned to the state $P(C=$ low $)$.

Figure 7a shows the LR as a function of the probability of no contamination. It can be seen that the likelihood ratio always tend to support the defense's point of view, except for values of $P(C=0)$ greater than 0.98 . Above this value, the LR tends to support the prosecutor's proposition. The green (dashed) and red (dotted) lines show the values of the LR that can be obtained when the other variables in the model are in the configurations for which the conflict is maximized and minimized, respectively.

In Figure 7b is shown the conflict measure as a function of the probability of no contamination. It can be seen that the conflict measure, $\operatorname{conf}(E)$, is equal to 0 for $P(C=0) \simeq 0.89$. Above this value, the conflict become positive and always higher along with the increasing of $P(C=0)$, for reaching the value of 1.8 when $P(C=0)=1$, that is, for the limit situation for which the model including the Contamination variable corresponds to the initial model shown in Figure 5.

# 5 Discussion and conclusions 

DNA evidence evaluation when dealing with activity level propositions has been recognized as a challenging issue by many authors in the recent years $[3,4,36,37,38,15,24]$.

The ENFSI Guideline for Evaluative Reporting in Forensic Science [7] recommends DNA trace evidence to be evaluated in the light of propositions at the activity level $[5,39]$, since in this case the complex mechanisms of transfer, persistence and recovery play a critical role in the assessment of the value of a given item of evidence.

The quantitative features of the model - notably, the likelihood ratio and the conflict value - obviously depend on all the probability assignments relative to the different variables. Data allowing one to inform the probabilities are often not straightforward to obtain. A number of studies about the relevant parameters that have an impact on the transfer, persistence and recovery mechanisms do exist. Unfortunately, they often adopt very strict experimental set-ups, either to limit the influence of other external parameters or because
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

![img-6.jpeg](img-6.jpeg)

Figure 7: Figure 7a shows the likelihood ratio as a function of the probability that no contamination occurred. The vertical line indicates the value of $P(C=$ None $)$ for which the inferential support of the items of evidence changes direction. This value is $\simeq 0.98$. Figure 7 b shows the conflict measure as a function of the probability that no contamination occurred. The line in pink (on the right of the vertical line) indicates the region corresponding to a likelihood ratio supporting $H_{p}$, conversely, the line in blue (on the left of the vertical line) indicates a LR supporting $H_{d}$. For both graphics, the other CPTs in the model have been left unchanged with respect to the initial assignations. Conversely, the green (dashed) and red (dotted) lines show the values of the LR and of the conflict measure that can be obtained when the other variables in the model are in the configurations for which the conflict is maximized and minimized, respectively.
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0
license http://creativecommons.org/licenses/by-nc-nd/4.0/

of laboratory limitations [40, 24]. Even the results from studies performed in less strict conditions, trying to mime real world circumstances $[41,36]$ are difficult to apply to other scenarios, given the impact of variables (e.g. environmental conditions, shedding characteristics of the participants in the study, ...) that are difficult to control and replicate. Extrapolation from published data for practical use in a case analysis can then be troublesome. Moreover, the probability assignments on other variables, such as Cleaning are subjective by nature; others, such as the Extraction efficiency are specific to the methods and kits used by each laboratory [42] and would then require a most careful analysis in order to validate the values presented in this article. In our opinion, these difficulties should not prevent the forensic scientist to provide a statement "at the activity level" when the circumstances of a case require it (see [38] for an extensive discussion). It is also important to stress that only the quantitative features of the model would be affected by the specific probability assignments, while the qualitative features are stable. In other words, the inferential direction of the results of Lab 1 and Lab 2 will always diverge, generating a conflict, that can be solved by the variable $C$; the LR tends to be mostly in favor of the defense's proposition (except for situations implying high values of $P(C=$ None $)$ ) throughout the different probability assignments, while the conflict will mostly tend to be negative. On the other hand, the extent of the conflict depends on the probability assignments in the different CPTs, which also impact on the value of $P(C=$ None $)$ for which the likelihood ratio becomes equal to 1.

It is worth discussing the impact that the probability of a contamination event can have on the results issued from the model, when dissonant items of evidence are reported. Even a relative low probability of contamination can lead to a reversal of the conclusions firstly obtained. It is legitimate to ask about the justification of the values assigned to the states of the variable Contamination. The studies of Basset and Castella [43] and Kloosterman et al. [44] provide informative data about the overall occurrence of contamination events within a forensic laboratory. Whereas the majority of contaminations concern a direct or secondary transfer of material from staff members to objects related to the case, a few number of case-to-case contaminations have been reported. Moreover, as noticed for example in Basset and Castella [43] and Thompson [45], this last type of contaminations can be difficult to detect, implying that the reported occurrence could be underestimated. Moreover, it is important to stress that a general contamination rate is not necessarily the relevant value to be used in a case: the probability that a contamination
(c) 2019. This manuscript version is made available under the CC-BY-NC-ND 4.0 license http://creativecommons.org/licenses/by-nc-nd/4.0/

occurred has to be assigned by considering the unique relevant circumstances of a real case. The values tested for this variable, and depicted in Figures 7a and 7 b , are then justified on the basis of this line of reasoning.

A number of studies recognize the existence of several possible mechanisms of contamination that can occur during the whole process of evidence recovery and exploitation (see, e.g., [46, 47, 48]). The ENFSI Contamination Prevention Guidelines [49] acknowledge the fact that it is challenging to completely eliminate contamination events, and that forensic laboratories should provide a transparent traceability of contaminations detected. The current scientific knowledge about the issue of contaminations therefore suggests that a probability of contamination different from zero can not be neglected. The issue of contamination can have a minor impact in cases where abundant cell material is found, or when the nature of the recovered material can be determined; but in cases involving only small quantities of biological material a careful evaluation of the findings needs to take into account this aspect $[7,4,14]$, as well as all the other complex extrinsic mechanisms (for instance, transfer, persistence, alternative legitimate activities) that can explain the recovery of the DNA of interest.

Finally, it is worth noticing that other explanations (for instance, a systematic lack of trust in the results of Lab 1) could have contributed to the conflict resolution. The decision to concentrate the analysis on the Contamination variable is due, on the one hand, by the circumstances of the case and the defendant's allegations, on the other hand, by the currently recognized fact that contaminations and DNA retrieving following indirect transfer are far from being rare events [43, 36, 44].
