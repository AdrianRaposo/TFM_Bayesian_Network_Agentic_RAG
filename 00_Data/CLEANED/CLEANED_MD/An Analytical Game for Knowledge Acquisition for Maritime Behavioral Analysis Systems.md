# Article 

## An Analytical Game for Knowledge Acquisition for Maritime Behavioral Analysis Systems

Francesca de Rosa ${ }^{1,2, *}$ (D) and Alessandro De Gloria ${ }^{1}$<br>1 Electrical, Electronics and Telecommunication Engineering and Naval Architecture Department, University of Genoa, 16145 Genoa, Italy; adg@elios.unige.it<br>2 NATO STO Centre for Maritime Research and Experimentation, 19126 La Spezia, Italy<br>* Correspondence: francesca.derosa@cmre.nato.int

Received: 15 November 2019; Accepted: 6 January 2020; Published: 14 January 2020


#### Abstract

The use of Bayesian networks for behavioral analysis is gaining attention. The design of such algorithms often makes use of expert knowledge. The knowledge is collected and organized during the knowledge acquisition design task. In this paper, we discuss how analytical games can be exploited as knowledge acquisition techniques in order to collect information useful to intelligent systems design. More specifically, we introduce a recently developed method, called the MARISA (MARItime Surveillance knowledge Acquisition) Game. The aim of this game is to ease the elicitation from domain experts of a considerable amount of conditional probabilities to be encoded into a maritime behavioral analysis service based on a multi-source dynamic Bayesian network. The game has been deployed in two experiments. The main objectives of such experiments are the validation of the network structure, the acquisition of the conditional probabilities for the network, and the overall validation of the game method. The results of the experiment show that the objectives have been met and that the MARISA Game proved to be an effective and efficient approach.


Keywords: analytical game; simulation game; knowledge acquisition; information systems; knowledge-base; knowledge engineering; Maritime; behavioral analysis; multi-source; dynamic bayesian network

## 1. Introduction

Due to the significant amount of information available and its associated uncertainty, there is a growing attention towards expert systems in support of human Situational Awareness able to perform probabilistic reasoning [1], such as the ones based on Bayesian networks (BNs). Expert systems are intelligent systems designed on the basis of knowledge acquired from experts [2]. Situational Awareness (SAW), which represents one of the steps of decision-making processes, can be defined as a mental model of the environment, built through "the perception of the elements in the environment within a volume of time and space, the comprehension of their meaning and the projection of their status in the near future" [3].

Knowledge acquisition (KA), which is a step of primer importance in the design of many systems, is the process of extracting, structuring, and organizing domain knowledge from experts [4]. Two widely used techniques are unstructured or structured interviews (i.e., protocol-generation techniques) [4]. Additional techniques include protocol analysis techniques, hierarchy-generation techniques, matrix-based techniques, sorting techniques, limited-information, and constrained-processing tasks and diagram-based techniques [5]. Details on the different techniques and their use can be found in the abundant literature on the topic (e.g., [6-9]).

With respect to KA for Bayesian networks, the most widely adopted methods for the elicitation of the network structure and parameters are interviews and questionnaires. However, literature has

discussed several issues related to probability elicitation from experts, such as expert limited time availability, biases, probability inconsistencies (i.e., probabilities not summing up to one), and the difficulty of verbalizing probabilities, especially when related to tacit knowledge [1]. In fact, often expert's knowledge is not directly accessible or easy to express [10].

Researchers have been looking at solving those issues by modifying the interview or questionnaire approaches. For example, some proposed to adopt gamble-like elicitation methods or the use of specifically designed probability scales [11,12]. Others proposed techniques to generate full conditional probability distributions from a reduced number of elicited assessments (e.g., [13-15]). Although several works have addressed the problem of experts' probability elicitation (e.g., [16-19]), research is still required to develop more efficient and effective techniques. The authors have proposed the use of innovative approaches based on analytical gaming (i.e., [20]). The use of games for KA is based on the concept that games are "a communication mode capable of linking tacit to formal knowledge by provoking action and stimulating experience" [21].

The use of games and gamification [22,23] in a non-gaming context is not a new concept. While the terms serious game and wargame identify full games that have a scope beyond mere entertainment, the term gamification refers to the use of game elements for this scope. Serious games have been formally established by Abt in the seventies [24], when he started exploring the use of games for learning purposes. However, the modern use of games with a purpose different than entertainment (i.e., training, communication or research) can be traced back to the early 19th century, when modern wargames started to appear (i.e., Kriegsspiel). Wargames are a well-formalized kind of simulation game which embodies a "warfare model or simulation whose operation does not involve the activities of actual military forces, and whose sequence of events affects and is, in turn, affected by the decisions made by players representing the opposing sides" [25].

Analytical wargames are wargames designed with a research purpose. Data-exchange serious game, instead, is the term through which the serious game community identifies games for collecting information from the players [26]. With the term analytical games, we will denote a set of games broader than analytical wargames. More specifically, we will refer to games designed not for entertainment, whose main purpose is research and data collection on decision-making, either in its complete dynamic cycle (like wargames) or a portion of it (i.e., SAW). Those games can be implemented on different gaming platforms (i.e., board games or computerized games). While analytical wargames explore the full decision-making cycle at strategical, operational, and a tactical level, analytical games extend the scope to the study of decision-making to the cognitive level. Some serious games focusing on SAW have been developed (e.g., [27]), but, according to the authors' knowledge, their focus is primarily on training. An exception is a game assessing Team Situational Awareness [28]. Games have started to be seen as a tool to explore human problem-solving strategies to inform computational algorithm optimization in the context of protein structure design [29] and vehicle powertrain controller design [30]. The findings derived from these games have shown that human-derived strategies can be a powerful approach when used in conjunction with computational algorithms. Recently, the authors have used analytical games, such as the Reliability Game [20], as knowledge acquisition tools for the design of algorithms to be used in information systems in support to SAW. The Reliability Game, which was inspired by the Risk Game [31], collects information regarding the impact of information source factors (i.e., source quality and source type) on human situational assessment. The data collected in the form of beliefs on a certain state of affairs has been used to gain insight on how to model within BNs source reliability, which generally is a latent variable.

In this article, we present and demonstrate the use of a new analytical game, which appears to be an effective and efficient tool to inform the design of BNs. In fact, the use of a questionnaire for knowledge acquisition purposes is often regarded as complex, boring, and time-consuming, leading to the elicitation issues listed above. The use of techniques and methods derived from games introduces entertainment in repetitive and tedious operations, like the ones performed by the experts during the traditional KA tasks. Therefore, we gamified the KA task through the use of a specifically designed

game, namely the MARISA (MARItime Surveillance knowledge Acquisition) Game. This game has been used to validate the structure and elicit the conditional probabilities for a multi-source dynamic Bayesian network (MSDBN), which performs behavioral analysis in order to support monitoring and surveillance in the maritime context.

Figure 1 shows the outline of the overall KA approach proposed in this paper. To support Situational Awareness of maritime operators, an MSDBN for behavioral analysis is under development. The KA problem is defined (i.e., eliciting conditional probabilities in a certain amount of time and validating the network structure) and the appropriate analytical game is instantiated. The specific method, called the MARISA Game, is played by domain experts (military and civilians). The output (cards and notes) is easily processed and used in the MSDBN, which is then evaluated in operational trials.
![img-0.jpeg](img-0.jpeg)

Figure 1. The knowledge acquisition (KA) approach discussed in this paper.
The remainder of the paper is organized as follows. Section 2 provides the background on the knowledge engineering problem addressed. Specifically, it describes dynamic Bayesian networks and challenges for the MSDBN design. Section 3 presents the MARISA Game and the KA experiments run. Section 4 reports the experiment results and discussions. Finally, Section 5 presents the conclusions and future work.

# 2. The Knowledge Engineering Problem 

### 2.1. Dynamic Bayesian Networks

A dynamic Bayesian network (DBN) is an extension of a Bayesian network (BN) to model probabilistically time-series [32,33]. More specifically, it can be interpreted as a sequence of time slices. Each time slice $(t)$ encodes a static BN.

A BN is a Directed Acyclic Graph (DAG) that enables reasoning under uncertainty within the Bayesian framework [34]. This graphical structure is defined through a set of random variables that are represented through nodes, and their conditional dependencies that are encoded through arcs. When an arc between the nodes $X$ and $Y$ is specified as $X \rightarrow Y$, then the node $X$ is defined as the parent node of $Y$.

Let us define a set of random variables $X=\left\{X_{1}, \ldots, X_{n}\right\}$ with $n$ total number of BN nodes. We can order the nodes such that the parents of a node $X_{i}$, also known as parent configuration, are a set

of variables $p a\left(X_{i}\right)=\left\{X_{q}, \ldots, X_{i-1}\right\} \subseteq\left\{X_{1}, \ldots, X_{i-1}\right\}$. In BNs, a node is conditionally independent of its non-parent ancestors, therefore

$$
p\left(X_{i} \mid X_{1}, \ldots, X_{i-1}\right)=p\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

As described in [33], in a DBN, we can denote with $U=\left\{U_{1}, \ldots, U_{T}\right\}$ a set of random variables, which can be partitioned in $U_{t}=\left(X_{t}, Z_{t}, Y_{t}\right)$, where $t=1 \ldots T$ represents the time slice, $X_{t}$ represents the observed variables (i.e., input variables), $Z_{t}$ represents hidden (latent) variables, and $Y_{t}$ the output variables of a state-space model. It has to be highlighted how in general the term dynamic refers to the dynamic nature of the system modelled, but the network is not changing over time.

A DBN can be defined as a pair, $\left(B_{1}, B \rightarrow\right)$, where $B_{1}$ is a BN defining the prior $p\left(U_{1}\right)$, and $B \rightarrow$ is a two-slice temporal Bayes net (2TBN), which encodes the conditional probability $p\left(U_{t} \mid U_{t-1}\right)$ through a DAG. More specifically, this relation can be expressed as follows:

$$
p\left(U_{t} \mid U_{t-1}\right)=\prod_{i=1}^{n} p\left(U_{t}^{i} \mid p a\left(U_{t}^{i}\right)\right)
$$

For notional reasons, we can assume that a first-order Markov assumption holds. Therefore, the parents of a node, $p a\left(U_{t}^{i}\right)$, can be in the same time slice or in the previous one. More in general, arcs can be defined across more than two slices.

By unrolling the 2TBN over $T$, we obtain the semantics of the DBN. More specifically, we can define the joint probability distribution as:

$$
p\left(U_{1: T}\right)=\prod_{t=1}^{T} \prod_{i=1}^{n} p\left(U_{t}^{i} \mid p a\left(U_{t}^{i}\right)\right)
$$

In the engineering community, more and more DBNs are adopted as uncertainty representation and inference tools. One of the reasons for that can be found in the good balance between expressiveness and tractability [33].

The BN knowledge engineering task includes the definition of the relevant variables, their relations, and the conditional probability distributions [1]. The first two aspects determine the BN structure. The last one, which determines the associated BN conditional probability tables (CPTs), consists of specifying for each $X_{i}$ the expression in Equation (1). The CPTs are often elicited from experts that might be requested to answer several questions such as: "What is the probability of a fish transshipment taking place given that the two ships of interest are performing a rendezvous?".

# 2.2. A Multi-Source Bayesian Network for Behavioral Analysis 

The Multi-Source Dynamic Bayesian Network (MSDBN) for Behavioral Analysis Service is one of the innovative data and information fusion services developed within the EC H2020 Maritime Integrated Surveillance Awareness (MARISA) project. This is a border and external security project, whose main goal is to increase end-user operators SAW. The MSDBN is a probabilistic based vessel behavioral analysis tool that presents a layered hierarchical structure, proposing an easy yet powerful mechanism to define a multi-source BN accounting for source reliability [35]. The MARISA project has been organized in a two-phase iterative design approach. Each phase culminated in a set of five operational trails run by end-users (i.e., Guardia Civil, Italian Navy, Netherlands Coast Guard, Portuguese Navy, and the Hellenic Ministry of Defence) for validation purposes. More specifically, the trials took place in the Northern Sea, the Iberian area, the Ionian Sea, the Aegean Sea, and the Bonifacio Strait area.

The network structure was developed and validated with the support of experts, and the MSDBN CPTs for the $t=0$ time slice have been elicited from experts, using a traditional questionnaire approach

in the first design phase and the MARISA Game in the second one. For $t>0$, the CPTs were defined as described in [35].

# 2.3. The Knowledge Acquisition for the MSDBN 

In the first design phase, the MSDBN prototype has been tailored only to the use case of illegal diving in the Northern Sea. This is a problem often encountered by the local law enforcement authorities. In fact, the shipwrecks of the Golden Age are an appealing target for treasure hunters.

As the number of BN parameters to be elicited grows exponentially with the number of nodes in the network, the number of questions in the first phase questionnaire was relatively contained. Moreover, a color coding was adopted in order to facilitate the intuitive understanding of the state of the MSDBN variables included in the questions, which are all Boolean (e.g., variable name is written either in blue or red, if the variable state is True or False, respectively). Nevertheless, a considerable effort has been required by the domain expert due to the complexity of the task.

During the second design phase, the MSDBN has been expanded to address the detection of anomalous behaviors that might be indicators of illegal immigration, illegal-unreported-unregulated (IUU) fishing, smuggling of goods, and piracy. The structure of the final MSDBN has been defined on the bases of relevant literature on maritime anomaly detection (e.g., [36,37]), news regarding trends on such illegal activities (e.g., illegal immigration in Italy) and discussions with domain experts. The conditional probabilities in the final MSDBN are considerably more than in the initial one. Therefore, we opted for the adoption of a different KA method, namely the MARISA (MARItime Surveillance knowledge Acquisition) Game. This is an analytical game designed to provide an engaging environment to increase the quality of the BN conditional probability elicitation and to facilitate open discussions, which are very valuable in system design. The need for a different KA approach derives from the one of presenting to the experts an easier tool for the elicitation of CPTs of the final MSDBN. Besides the complexity of the task, another important aspect that played a role in the decision of applying gaming techniques was to facilitate the user in the task execution by providing context and support in the question interpretation. In fact, the questions presented in the first KA phase were not always easily understood.

## 3. Method for KA: MARISA Game

### 3.1. MARISA Game Design

The MARISA Game is a one round multi-player board game, which makes use of cards (i.e., knowledge cards) to convey to players the required information. On the basis of the information in the knowledge cards, players need to assess which could be the state of a possible variable of interest. Their assessment is recorded in the form of beliefs and mapped to subjective probabilities, which are used to populate the MSDBN CPTs. The length of each game session depends on the number of CPTs that need to be elicited from the experts.

The next subsections summarize the world, content, and system design of the MARISA Game. The world design can be defined as "the creation of the overall backstory, setting and theme", the content design refers to the "creation of characters, items, puzzles and missions", while the system design refers to the "creation of rules and underlying mathematical patterns" [38].

### 3.2. World Design

The MARISA Game is set in a maritime scenario. Each participant plays the role of a junior navy officer assigned to a duty location on one of the islands of a fictitious archipelago, called the MARISA Islands.

The six MARISA Islands are depicted on the game board (Figure 2). This archipelago is very peculiar as all of the five bigger islands suffer from one and only one illegal activity. This characteristic makes those islands a perfect duty location to train junior officers, as they need to focus only on one

specific activity and gain domain knowledge on it. Those islands are named after the illegal activity taking place on them (e.g., Piracy Island, IUU Fishing Island, Illegal Diving Island, Smuggling of Goods Island, and Illegal Immigration Island), while the smaller central island is the Reliability Island, where the main Command Centre for the area is located. On this island, the junior officers are trained on the assessment of the reliability of the sources of information providing reports to the Command Centre.
![img-1.jpeg](img-1.jpeg)

Figure 2. MARItime Surveillance knowledge Acquisition (MARISA) Game board.
The players need to gain a sound domain knowledge in order to proceed in their career. The level of expertise of a player is represented by the number of knowledge tokens that the player collects. The first player that collects all the knowledge tokens is the winner.

# 3.3. Content Design 

At the start of the game session, the players are presented with an informed consent form to be signed, explaining the aims of the experiment and the way in which the data will be treated. In addition, a short pre-game personal information form is provided. Then, the players are introduced by a facilitator to the game core, rules, scenario, and different game elements (e.g., game board, cards, and query track sheets).

For each island, there is a corresponding knowledge card deck. The knowledge cards provide knowledge constructs in the form of portions of the MARISA MSDBN related to the different illegal activities. Figure 3 shows an excerpt of the DBN structure related to illegal diving and its subdivision in the knowledge structures to be analyzed by the experts in the game.

Two different kinds of knowledge cards have been designed and used. More specifically, cards that contain the knowledge structures referring to the model of a situation (i.e., orange boxes in Figure 3) present such knowledge in a graphical form. This representation recalls the graphical one of BNs (Figure 4a). Instead, the knowledge structures related to the model of source reliability (i.e., blue boxes in Figure 3) are presented in natural language form (Figure 4b). These knowledge structures are included only in the Reliability Island card deck. A color coding is adopted as a visual cue to support experts' assessment. In fact, the Boolean variable is green if its state is True, red if its state is False, and white if its state is not determined, as it must be assessed by the player based on state of the other ones. The variables refer to ship characteristics, ship kinematic conditions, information source type, geographical factors, and environmental conditions that are compatible with the analyzed illegal activities.

The data gathering area on which the players need to mark their belief regarding the state of the query variable is included in the card area containing the knowledge structure. In the MARISA Game,

the data gathering area is a segment between the two possible hypotheses on the query variable state that are $H_{1}=$ False or $H_{2}=$ True $($ False $=F$ and True $=T$ in Figure 4a,b).
![img-2.jpeg](img-2.jpeg)

Figure 3. Portion of the multi-source Bayesian network (adapted from [35]) and its division in knowledge structures.
![img-3.jpeg](img-3.jpeg)
(a) Knowledge card from the Smuggling of goods Island decks
![img-4.jpeg](img-4.jpeg)
(b) Knowledge card from the Reliability Island deck

Figure 4. Example of a knowledge card.

In addition to the knowledge card decks, there is a commendation card deck that contains bonus cards to request new knowledge cards at any time or to move to an island of choice.

A specific color coding is used to help players refer to a specific illegal activity. The color code, in fact, is repeated on the knowledge cards of a specific deck and on the respective query track sheet.

Additional information has been collected from the players' discussions, which has been captured in the facilitator notes. In fact, in the MARISA Game, the facilitator also has the role of data collector.

After the game, instead, the players are requested to fill in a player experience (PX) post-game evaluation questionnaire. Several methods can be used to assess PX [39,40], including surveys. Although this approach might suffer from some common issues of self-reported assessments (i.e., relying on players' memories [40] and answer correlation with performance), it was selected as it is the cheapest, easiest, and quickest assessment method.

The post-game questionnaire deployed evaluates the PX on a five-point Likert scale along several dimensions (i.e., overall attitude, sensory and imaginative immersion, flow, challenge, confidence, relevance, satisfaction, workload, and usability). Although an extensive validation campaign of the questionnaire has not yet been possible, it has to be underlined that it actually consists of an extension and adaptation to analytical games for KA of other widely used PX questionnaires (i.e., the Game Experience Questionnaire [41] and the updated Model for the Evaluation of Educational Games [42]-MEEGA+). The main adaptations consist of wording changes, the substitution of the usability MEEGA+ questions with others derived from the Questionnaire for User Interaction Satisfaction (QUIS) [43,44], and the introduction of questions related to physical and cognitive workload. More specifically, the more general QUIS questions, which are used to assess subjective satisfaction for human-computer interfaces, have been adapted to the concept of games that are assimilated to a system. The workload questions, instead, have been excerpted from the NASA Task Load Index (NASA-TLX) [45], which is one of the most used workload self-assessment tools.

# 3.4. System Design 

In order to collect knowledge tokens, players need to proceed in the game by moving on each island path. This is achieved by throwing a dice and move the pawn of a number of corresponding tiles. This path tiles have colors that correspond to the following actions or areas:

1. Green: no action associated;
2. Beige: allows looking at the knowledge cards as per result of another dice;
3. Purple: allows picking one bonus card from the commendation card deck;
4. Red: start tile and area of arrival when changing island thanks to a commendation card;
5. Blue: harbors to move between islands.

Islands are connected via Sea Lines of Communication (SLOCs) that are represented on the board game. Those SLOCs can be travelled with the ships that are available at the anchorages of the islands ports (harbor tiles). The SLOCs connecting the bigger islands are two-ways, while the ones connecting those islands to the Reliability Island are one-way.

As previously mentioned, each island has a corresponding knowledge card deck with portions of the MSDBN model, which we will denote as a knowledge structure $K S_{\alpha \gamma}^{d}$, where $d=1, \ldots, d_{\max }$ represents the number of card decks, $s=1, \ldots, s_{\max }$ the knowledge structures in the card deck $d$ and $c=1, \ldots, c_{\max }$ the possible presentations of the knowledge structure $s$ for deck $d$. Each knowledge card presents a message $M_{n}^{d}$, where $n=1 \ldots n_{\max }$ are the cards in a card deck $d$. A message can contain one or more knowledge structures. Those are composed by a query variable $(Q)$ and other variables $(D)$ that have a direct dependency with $Q$ as per MSDBN model. Each knowledge structure is presented to the player in all its configurations that are all the possible combinations of $D$ states. Tables 1 and 2 summarize the MARISA Game state and view, respectively. The game state are all the relevant variables that may change during the play, while the game view is the subset of the game state that is visible to the player in each round [38].

Table 1. MARItime Surveillance knowledge Acquisition (MARISA) Game state.


Table 2. MARISA Game view.


${ }^{1}$ Provided $=$ item value provided to the player; ${ }^{2}$ Assessed $=$ player has to assess the item and record the assessment.

Players are required to state their belief regarding the state of the variable $Q$, in relation to the states of the variables $D$. The position of the mark on the data gathering segment correspond to the degree of belief that the state of $Q$ might be either True or False, given the evidence provided regarding the $D$ variables. If beliefs are interpreted as the expression of subjective probabilities [46], then positioning the mark on the left end of the segment (i.e., $F$ ), would correspond to the assessment that the probability that the state of $Q$ is False equals 1 . Once the beliefs are marked, the knowledge card is put aside. Players are allowed to go back and look at them when filling in the next ones. As previously mentioned, to obtain knowledge cards, the players need to reach a beige tile on the map and throw a ten facet dice. If we denote the number obtained through the dice as $N$, for $N \leq s_{\max }$, the player receives a knowledge card presenting some configurations of the $N$ th knowledge structure. If the participant already received all the knowledge cards corresponding to the considered knowledge structure, he or she will not receive an additional knowledge card. For $N>s_{\max }$, the player can choose the knowledge card to receive. It has to be mentioned that the game mechanics to obtain the knowledge cards have been slightly modified on the fly in both experiments in order to make the game quicker to accommodate operational contingencies that limited the expert time availability (Section 4). In this simplified version, it was assumed that, for $N \leq 6$, the player would obtain one knowledge card, while, for $N>6$, the player would obtain two knowledge cards.

As the players fill in the cards, they advance in their career and this is tracked on their career status sheets, on which the knowledge card already received can be marked. Moreover, the full structures of the MSDBN model for the related illegal activities are depicted. When players complete a knowledge card deck, they earn the corresponding knowledge tokens and are entitled to receive a card from the commendation card deck. The player who first obtains all the promotions (i.e., all the knowledge tokens) is the winner. The game continues until all the players have finished all the cards.

To summarize, the main elements that characterise the MARISA Game are:

1. the assessment of hypotheses relative to maritime anomalies;
2. the use of cards to communicate messages to the player;
3. the investigation component;
4. the rating of the player beliefs related to the knowledge constructs provided through cards;
5. the collection of knowledge tokens.

Figure 5 presents a simple flow diagram of the game. As previously mentioned, players can use their commendation cards at any time during the game. This process has been omitted in this figure for clarity. Table 3 lists the main game mechanics implemented in this game and their description [47]. Figure 6, instead, present a schematic view of the main mechanics and the game economy through a

Machination diagram [48,49]. For notional reasons, it is assumed that only two islands are present and a one player perspective is assumed. However, the diagram could be easily extended to include the multi-player turn-based perspective and additional islands. This diagram focuses primarily on the formalization of the collection of knowledge cards (simplified version) and possibly knowledge tokens in a game turn, while the movements on the game board as a result of the dice rolling is modeled at a higher level of abstraction, as this is a very common mechanic.
![img-5.jpeg](img-5.jpeg)

Figure 5. Diagram of a MARISA Game session.
Table 3. List of the main MARISA Game mechanics.


![img-6.jpeg](img-6.jpeg)

Figure 6. MARISA Game machinations diagram [48].

# 3.5. Knowledge Acquisition Experiments 

In order to collect the data required for the MSDBN, two game sessions have been organized. The main objectives of the experiments can be summarized as follows:

1. collection of the players belief to be used to define the MSDBN conditional probability tables;
2. validation of the MSDBN structure;
3. validity of the MARISA Game.

Several perspectives on how to validate (or evaluate) games exist (e.g., [50-52]). In this work, we follow the perspective that this activity could be assimilated to the "confirmation through the provision of objective evidence that the requirements for a specific intended use or application of a system have been fulfilled" [53], where the term "system" refers to the game. Following [54], this fit for purpose concept can be associated with four principles-more specifically, the ability to employ the new capability (i.e., ensure that the capability works properly that the players can use it and that the capability is actually exercised), the ability to detect change during the experiment, the ability to isolate the reason for change, and the ability to relate results to actual operations (i.e., result utility).

The first experiment (EXP1) has been run with four Spanish experts, namely three maritime law enforcement experts from the Guardia Civil and one civilian engineer. A second experiment (EXP2) has been run with five Italian participants (Figure 7), namely four military experts from the Italian Navy and one engineer. Table 4 provides additional information on the participants characteristics and demographics. The experiments allowed to adapt the MSDBN design to the maritime illegal activity patterns observable in the Iberian area and the Ionian Sea area, respectively.

![img-7.jpeg](img-7.jpeg)

Figure 7. MARISA Game session with the Italian Navy.
Table 4. Participants demographics and characteristics.


# 4. Results and Discussion 

From the analysis of the game results, it has been possible to deduce that all three objectives discussed in Section 3.5 have been met. With respect to the first objective, the MARISA Game allowed the collection of the players' belief assessments for the different knowledge structures. Those beliefs have been mapped to subjective probabilities (Section 3.4) and used to populate the MSDBN. As an example of such process, we can consider Figure 8. It shows four different configurations of the same knowledge structures included in a knowledge card of the Smuggling of Goods (SMG) Island card deck and the corresponding belief stated by a player during EXP2 (Section 3.5). For this example, we have the following three variables:

1. $Q$ : Compatible with SMG: vessel characteristics;
2. $D_{1}$ : Compatible with SMG: vessel type;
3. $D_{2}$ : Compatible with SMG: vessel size.

The resulting subjective probabilities are:

$$
\begin{aligned}
& p\left(Q=\text { True } \mid D_{1}=\text { True } ; D_{2}=\text { True }\right)=0.825 \quad p\left(Q=\text { False } \mid D_{1}=\text { True } ; D_{2}=\text { True }\right)=0.175 \\
& p\left(Q=\text { True } \mid D_{1}=\text { True } ; D_{2}=\text { False }\right)=0.525 \quad p\left(Q=\text { False } \mid D_{1}=\text { True } ; D_{2}=\text { False }\right)=0.475 \\
& p\left(Q=\text { True } \mid D_{1}=\text { False } ; D_{2}=\text { True }\right)=0.350 \quad p\left(Q=\text { False } \mid D_{1}=\text { False } ; D_{2}=\text { True }\right)=0.650 \\
& p\left(Q=\text { True } \mid D_{1}=\text { False } ; D_{2}=\text { False }\right)=0.100 \quad p\left(Q=\text { False } \mid D_{1}=\text { False } ; D_{2}=\text { False }\right)=0.900
\end{aligned}
$$

![img-8.jpeg](img-8.jpeg)
(a) The knowledge structure with both the parent variables with a state True
(b) The knowledge structure with the first the parent variable with a state True and the second one with a state False
![img-9.jpeg](img-9.jpeg)
(c) The knowledge structure with the first the parent variable with a state False and the second one with a state True
(d) The knowledge structure with both the parent variables with a state False

Figure 8. Examples of different configurations of the same knowledge structure.
Therefore, the complete CPT for the Compatible with SMG: vessel characteristics variable of the MSDBN is summarized in Table 5. The mapping has been performed for all the collected data, leading to the definition of the CPTs of the full MSDBN.

Table 5. Conditional probability table of the query variable Compatible with smuggling of goods : vessel characteristics for the Ionian Sea experiment.


With respect to the second objective, the use of the game allowed to verify and then validate the MSDBN structure. In fact, already in the playtest phase, the game proved to be an effective verification method, as a player highlighted some wrong MSDBN design assumptions. These assumptions have been removed in the final MSDBN structure, which has been presented in the two experiments. The presentation of knowledge cards acted as an inject, naturally stimulating discussions and substituting the questions of structured interview approaches. The generated discussions and consequent feedback showed that the proposed MSDBN structure is appropriate.

The experiment results positively support the game validation objective. In fact, the two experiments showed that the game overall was well perceived and, after a short explanation of the rules, players started playing confidently, without major support from the facilitator. This allowed the facilitator to focus on the discussion and collection of verbal feedback. During those discussions, qualitative (i.e., network structure) and quantitative aspects related to the MSDBN have been analyzed in depth.

Although the mechanics selected for the MARISA Game did not prove to be wrong, due to time constraints dictated by operational duties of the persons participating to the experiments, it was agreed at the beginning of both experiment sessions to increase the number of knowledge cards provided to the player at each turn and to modify the winning condition. More specifically, it was agreed that the winner is the player collecting more knowledge tokens in a certain amount of time. Due to this change, the players were also invited to focus on the Islands corresponding to the illegal activity on which they had more expertise. This suggests that the game mechanics that support quick games should be preferred.

As discussed in Section 3.3, there are two different types of knowledge card layouts. Most of the players stated that the graphical presentation of the knowledge structure is very useful if there are not many variables $(D)$ in addition to the query variable. The average response was that the graphical presentation is convenient for $D \leq 4$, while, for $D>4$, the presentation in natural language form appears to be more adequate. However, those are preliminary observations and further investigation should be performed.

From the verbal feedback and the feedback questionnaire, the MARISA Game appears to be perceived as a more engaging and stimulating method compared to traditional approaches to elicit the CPTs for Bayesian networks. Appendix A presents the self-reported results of the game PX assessment in the form of frequency tables. It includes also the response rate, the mode (Mo), and the interquartile range $(I Q R)$, which is adopted as an index of consensus $(I Q R=0$ for strong consensus).

The results of the questionnaire show that the overall attitude towards the game is positive. The game was perceived as an adequate experimentation tool ( $M o=4, I Q R=0.25$ ). However, players did not have the initial feeling that it would be easy (initial feeling of ease $M o=3, I Q R=0.50$ ), they felt confident that the experiment would support the stated goal, thanks to the facilitation approach ( $M o=4, I Q R=1.00$ ) and to the game structure and content ( $M o=4, I Q R=0.25$ ). However, it appears that it was not very clear for all the players how the game relates to the stated goal ( $M o=4$, $I Q R=2.00$ ). This might be due to the fact that most of the players were not familiar with the MSDBN Service concepts or the MARISA project. Therefore, the introduction brief providing context to the participants should have been more detailed and focused on this aspect. The answers suggest that several players have a preference of using games over other KA methods. However, there is no consensus on this $(M o=5, I Q R=2.25)$. This might also be linked to the fact that none of them was involved in the KA session where traditional approaches were employed. The responses regarding flow show that the participants were concentrated ( $M o=4, I Q R=0.25$ ) and some fully occupied with the game ( $M o=5, I Q R=2.00$ ), but, as expected, the MARISA Game is not a high-engagement game that leads to a full immersion, forgetting about time (i.e., lost of track of time: $M o=1, I Q R=2.00$ ) and surroundings (i.e., forgot about surroundings: $M o=1, I Q R=2.00$ ). As can be observed in Appendix A, an overall positive feedback has been provided with respect to:

1. the usability of the game as a system;
2. the facilitation process;
3. the sensory and imaginative immersion;
4. the players' satisfaction.

However, responses report a moderate level of monotony of the game session ( $M o=3, I Q R=1.25$ ), of challenge $(M o=3, I Q R=1.25)$ and of impressiveness $(M o=3, I Q R=1.25)$. Moreover, it was not perceived by most players as a rich experience $(M o=2, I Q R=1.25)$. Therefore, future developments of this game should address these aspects. Finally, an interesting result was observed through the feedback related to workload. In fact, we observed how most of the players felt that the task to accomplish was

moderately complex and demanding in terms of mental activity ( $M o=3, I Q R=1.25$ ). Moreover, they stated that also the work to achieve the level of performance obtained was moderated ( $M o=3$, $I Q R=0.25)$. This might be related to the fact that the game is considered easy $(M o=4, I Q R=0.50)$. This result is in contrast to the one received for the KA session using the traditional questionnaire approach and positively support the concept of using analytical games for KA.

The free form written feedback highlights the positive attitude of the operators towards the use of game methods (i.e., board games) for purposes beyond entertainment (i.e., "Board games are a fantastic classic way to have fun! Adopting them to obtain feedback and motivate people is a great idea!"). One player stated that the game was unfolding too quickly to appreciate the relevance and ability of such approach to support the stated goal. However, he also admitted to be severely sleep deprived due to work related activities.

Some players requested from the facilitator duplicated knowledge cards, probably because they had forgotten to mark them on the recording sheet. Therefore, the recording sheet did not prevent this occurrence adequately. However, an interesting observation relates to the consistency of the belief statements in such duplicated cards. By comparing the players' answers, it has been possible to observe how some provide fairly consistent answers when exposed to the same stimulus, up to a player that provided the same answers in all the three duplicated knowledge cards. Instead, another player proved to be inconsistent when providing the answers to the duplicated cards. Although this is just a preliminary observation, it might suggest that similar strategies should be investigated further to determine if they could be employed to better characterize the players' profile and, therefore, the validity of the answers provided.

The MARISA Game evaluation is positive from a fit for purpose perspective. The observations during the experiment and the feedback received proved that the game overall works appropriately and is capable of collecting the data as per experimentation plan. The results showed that it possesses the ability to easily detect changes (i.e., belief variations for different knowledge structure configurations) and the experimental set-up (i.e., the design of the knowledge cards) makes it very simple to identify the reason for change. Additionally, a positive evaluation of the game has been obtained with regard to the collected knowledge utility. In fact, the MSDBN designed with the support of this game has been successfully tested and evaluated in two of the MARISA project operational trials, namely the Northern Sea trial and the Iberian trial. As can be noticed, the first one is not one of the areas for which the MSDBN was specifically tailored by playing the game with local experts. However, the system evaluation suggests that the knowledge collected could be representative also of other geographical regions. This will be the focus of further research.

# 5. Conclusions 

This work explores the use of the MARISA Game, which is an analytical game designed to support knowledge acquisition from maritime surveillance experts of a considerable amount of conditional probabilities to be used into a maritime behavioral analysis service, based on a multi-source dynamic Bayesian network. Two experiments have been run with different players and the results wield a positive outcome. More specifically, all the objectives were met in both cases. Those objectives consisted of the validation of the multi-source dynamic Bayesian network structure, the elicitation of its conditional probabilities, and the game evaluation. In fact, the game acted as a natural form of structured interview, supporting not only the elicitation of the conditional probabilities, but also the validation of the network structure. The knowledge utility was proven in the successful operational trials where the behavioral analysis service was deployed. Improvements in the KA task were observed in terms of expert time required and complexity of the task compared to traditional questionnaire approaches. Finally, a positive feedback was received in terms of player experience.

This paper supports the concept of using analytical games, such as the MARISA one, for knowledge acquisition, knowledge engineering, and, in general, participatory design. Future work will be devoted to increase the understanding of which game mechanics better fit the knowledge engineering problem

and experimentation constraints (i.e., time availability), to enhance the player profiling and to improve the pre-game communication protocol. Moreover, future efforts will focus on improving the game from a sensory and imaginative immersion perspective, in order to provide a richer experience to the players. Furthermore, research will address the definition of evaluation protocols for such games (including the validation of player-experience questionnaires) and on the deployment of the game to a broader set of experts in order to increase our understanding of the strength and weaknesses of the use of gaming for knowledge acquisition.

Author Contributions: Conceptualization, F.d.R.; Methodology, F.d.R.; Validation, F.d.R., Investigation, F.d.R.; Writing-Original draft preparation, F.d.R.; Writing-Review and editing, A.D.G. and F.d.R.; Supervision, A.D.G. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Acknowledgments: The authors gratefully acknowledge the support of NATO STO Centre for Maritime Research and Experimentation for sharing the data that enabled this work. In fact, this data has been collected through the deployment of the game within the MARISA project. MARISA European research project has received funding from the European Union's Horizon 2020 research and innovation program under Grant No. 740698. The authors would like to thank all the game participants, David Merino Delgado, and Giovanni Laneve for their support with the experimentation sessions. Moreover, the authors would like to thank Cdr. Paolo Lombardi for the support in the playtesting of the game.
Conflicts of Interest: The authors declare no conflict of interest.

# Abbreviations 

The following abbreviations are used in this manuscript:


## Appendix A. Results of the K2AGQ

This section reports the results collected through the PX questionnaire in the form of frequency tables. The five point Likert scale proposed for the ranking presented the following verbal anchors: 1 -Not at all, 3-Moderately, 5-Extremely. Additionally, the tables include the response rate (RR) in the form of percentage, the mode (Mo), and the interquartile range (IQR). The response rate is never $100 \%$ as one player did not provide the answers, and some players did miss a couple of items in their feedback.

Table A1. MARISA Game feedback—Challenge.


Table A2. MARISA Game feedback—Confidence.


Table A3. MARISA Game feedback—Flow.


Table A4. MARISA Game feedback—Overall attitude


Table A5. MARISA Game feedback—Relevance


Table A6. MARISA Game feedback—Satisfaction


Table A7. MARISA Game feedback—Sensory and imaginative immersion


Table A8. MARISA Game feedback—Workload


Table A9. MARISA Game feedback—Usability


Table A9. Cont.

