# Trust-based decision-making for smart and adaptive environments 

Stephan Hammer ${ }^{1}$ ・ Michael Wißner ${ }^{1}$ ・ Elisabeth André ${ }^{1}$

Received: 2 August 2014 / Accepted in revised form: 10 February 2015 / Published online: 16 April 2015
(C) Springer Science+Business Media Dordrecht 2015


#### Abstract

Smart environments are able to support users during their daily life. For example, smart energy systems can be used to support energy saving by controlling devices, such as lights or displays, depending on context information, such as the brightness in a room or the presence of users. However, proactive decisions should also match the users' preferences to maintain the users' trust in the system. Wrong decisions could negatively influence the users' acceptance of a system and at worst could make them abandon the system. In this paper, a trust-based model, called User Trust Model (UTM), for automatic decision-making is proposed, which is based on Bayesian networks. The UTM's construction, the initialization with empirical data gathered in an online survey, and its integration in an office setting are described. Furthermore, the results of a live study and a live survey analyzing the users' experience and acceptance are presented.


Keywords Computational trust $\cdot$ Context awareness $\cdot$ Proactive systems $\cdot$ Energy saving

[^0]1 Human Centered Multimedia, Augsburg University, Universitätsstr. 6a, 86159 Augsburg, Germany


[^0]:    回 Stephan Hammer
    hammer@hcm-lab.de
    Michael Wißner
    wissner@hcm-lab.de
    Elisabeth André
    andre@hcm-lab.de

# 1 Introduction 

Recent advances in sensor technologies enable us to capture the users' physical context continuously and to personalize information and services to them in real-time. One area that might greatly benefit from new forms of context-aware system behaviors are smart energy systems that exploit information on the users' environmental context to support them in saving energy-either by controlling energy-consuming devices proactively or by giving the users personalized advice.

Reducing energy consumption has been a major concern for more than four decades, and many approaches aimed at supporting sustainability were developed during this time (Hazas et al. 2011; DiSalvo et al. 2010). Some tried to improve people's environmental awareness by providing detailed feedback on their energy usage (Gamberini et al. 2012). Others tried to persuade people to reduce their energy demand by exploiting social factors and utilizing, for example, cooperative pervasive games (Simon et al. 2012).

A number of energy management systems allow users to control devices, such as displays or lights, remotely or by setting up time tables. Furthermore, attempts have been made to adjust the energy consumption implicitly based on various context information that describes the users' and the system's surroundings (Cheverst et al. 2005). For example, displays or lights can be switched off if they are not needed. On the one hand, a system that autonomously performs energy saving actions contributes to the users' convenience. On the other hand, proactive system actions are not always understood by users and limit their control over the system. As a consequence, users might lose trust in such a system and give up using it.

For illustration, let us assume a lamp is burning in the user's office even though daylight suffices for performing the work. How should an energy management system react in such a situation? Should it assume the users are aware of their energy consumption and will take necessary actions themselves? Should it switch off the light autonomously? Or should it ask the user for permission via messages presented on the user's display or mobile phone?

In the first case, the system would leave the responsibility for energy reduction with the users, and there would be the risk that users do not see any benefit in the energy management system. The second approach bears the danger that the users do not understand the rationale behind the system's behavior and perceive it as not sufficiently self-explanatory or even as acting in a random manner. In the last case, the system's behavior might appear transparent. However, users might nevertheless be upset because permanent and obtrusive messages interrupt their workflow. The example illustrates that a system needs to carefully balance the benefits and drawbacks of possible actions so as not to risk the users losing trust in its workings.

In this paper, a decision-theoretic approach to a trust management system for smart and proactive environments based on Bayesian Networks, the User Trust Model (UTM), is presented. It assesses the users' trust in a system, monitors it over time, and applies appropriate system reactions to maintain users' trust in critical situations (Yan and Holtmanns 2008). Section 2 discusses prior work in modeling trust, considering work done in the area of agent-based modeling, social media and adaptive and personalized systems. After that, the UTM's construction (Sect. 3) and its integration

into an office setting and the initialization with empirical data (Sect. 4) are described. Sections 5 and 6 present a live study and a live survey investigating the users' experience with and acceptance of the system. Finally Sect. 7 gives a conclusion and an outlook on future work.

# 2 Related work 

In the area of user modeling, research on computational models of trust has become very popular due to the obvious overlap between trust and reputation modeling in recommender systems and social media. Nevertheless, approaches that model trust as a user experience and focus on the affective dimension of trust are rare. This is unsurprising because the psychological aspects of trust are hard to measure directly. In this section, we will first give an overview of computational models starting from approaches that have been presented for agent-based societies, social networks and recommender systems. After that, we discuss how the concept of trust has been treated in ubiquitous computing.

### 2.1 Computational models of trust

Much of the original research on trust comes from the social sciences. Psychologists and sociologists have tried for a very long time to get a grasp of the inner workings of trust in interpersonal and interorganisational relationships. Other fields, such as economics and computer science, relied on their findings to come up with dedicated models of trust that are adapted to the specific requirements of their domains and the context they are applied to. Since trust is a social phenomenon, it seems to be promising to exploit models that have been developed to characterize trust in human societies as a basis for computational models of trust.

Especially in the area of multi-agent systems, computational models for trust-based decision support have been researched thoroughly. Pioneering work in this area has been conducted by Marsh (1994) who modeled trust between distributed software agents as a basis for the agents' cooperation behavior. Computational mechanisms that have been proposed for trust management in agent-based societies include Bayesian Networks (Wang and Vassileva 2005), Dempster-Shafer Theory (Yu and Singh 2002), Hidden-Markov Models (Vogiatzis et al. 2010), Belief Models (Jøsang et al. 2006), Fuzzy models (Castelfranchi and Falcone 2010), game-theoretic approaches (Sankaranarayanan et al. 2007) or decision trees (Burnett et al. 2011). There is empirical evidence that the performance of agent-based societies may be improved by incorporating trust models.

In contrast to the approaches above, work in the area of social media aims to model trust between human users, see Sheridan et al. (2013) or Bhuiyan et al. (2010) for a survey investigating trust in social networks. Using algorithmic approaches or machine learning techniques, trust between users is derived from objective observations, such as behavior patterns in social networks. For example, Adali et al. (2010) assess trust between two users based on the amount of conversation and the propaga-

tion of messages within Twitter. Other approaches derive trust that is given to users from community-based reputation or social feedback (e.g. Ivanov et al. (2013)).

Computational models related to trust have also been explored in the area of recommender systems. Obviously, it does not suffice to generate recommendations solely based on the users' profile and preferences. In addition, the trustworthiness of people, organizations and services involved in the recommendation process have to be taken into account. There is empirical evidence that computational models of trust may help improve the recommendation accuracy of traditional collaborative filtering approaches, see, for example, O'Donovan and Smyth (2005).

Our research focuses on trust which users experience when interacting with a software system. A system may be robust and secure, but nevertheless be perceived as less than trustworthy, for example, because its behavior appears less than transparent or hard to control. Following the terminology by Castelfranchi and Falcone (2010), our work focuses on the affective forms of trust that are based on the user's appraisal mechanisms. That is why we aim at the development of computational trust models that capture how a system-in this paper a smart environment for energy saving-is perceived by a user who is confronted with it.

Computational models that assess trust felt by a user while interacting with a system are rare. There is a large amount of work that aims to identify factors that impact user trust. For example, Glass et al. (2008) research trust-enhancing factors for adaptive and personalized applications. However, they do not implement a model of the user's trust into an adaptive and personalized system based on these factors. Starting from the observation that people respond to technology socially, Lee and See (2004) discuss psychological factors of trust, such as the visual appearance of the interface, that influence to what extent people rely on technology. Yan and Holtmanns (2008) model captures the trust which users experience when interacting with mobile applications. In order to present users with recommendations that help increase their trust, they identified various behaviors that can be monitored by a mobile device in addition to external factors, such as brand impact. The benefits of this approach have been shown by means of simulations. However, the approach has not been embedded in an adaptive and personalized mobile application to control the selection of system actions during an interaction with the user.

# 2.2 Trust in ubiquitous computing 

In the area of pervasive computing, the topic of trust has attracted a significant amount of interest. This comes as no surprise since the high dynamics and openness of pervasive computing environments come not only with great benefits, but also a number of security risks. Due to the large variety of smart objects and devices that can exchange information, the underlying infrastructure is heavily imperiled by manipulations. Typically users interact with such environments on a short-term basis without having the possibility to verify the security of the underlying infrastructure. Vice versa access control in open environments which people can enter and leave at any time is a challenging task. To solve these issues, a number of research projects have investigated how to apply trust mechanisms from the area of network security to pervasive

computing. A common approach is to explicitly model trust relationships between physical devices and exploit this information to choose appropriate devices for cooperatively solving a task, see, for example, Denko et al. (2011).

At the same time, a significant amount of private data is collected silently using sensors worn on the user's body as well as external sensors smoothly integrated into the user's environment. On the one hand, the comprehensive collection of user data contributes to a better personalization of information and services. On the other hand, ubiquitous user modeling may be considered as a threat to privacy. To mitigate this threat, a variety of mechanisms has been presented to preserve the user's privacy and hide confidential information from others, such as preventing the tracking of tagged consumer items or displaying private information on the user's personal device. In our earlier work (Wißner et al. 2014), we presented a trust management system that assesses the users' trust in ubiquitous display environments and decides how and where to present personal information based on location-based context factors, such as other people in the user's immediate neighborhood. While our work did not distinguish between trusted and non-trusted people in the user's physical environment, the approach by Arimura et al. (2014) makes use of physical trust relationships between users. First, face-to-face communication between users is triggered by the authentication system in order to visually confirm users. Only in cases where visual authentication was not successful, the system would ask for additional authentication information, such as passwords. The interesting idea behind this work is the face-to-face communication between users that the authentication process encourages as a basis for the creation of trust between people.

Another factor that may affect the users' trust is the high heterogeneity, uncertainty and unpredictability of pervasive environments. Despite the large number of sensors that are employed to capture user and context information, the analysis and interpretation of the sensor data are error-prone. In our earlier work (Kurdyukova et al. 2012), we aimed to personalize recommendations based on the composition of social groups that were detected using video-based face detection software. However, in natural environments, the accuracy rates of the recognition process were often affected by noisy conditions. Adjusting recommendations to an audience based on incorrect context information may result in system behaviors that appear less than transparent to users. For example, interviews with users of an adaptive digital signage system that automatically adapted to the assumed interest of an audience revealed that some users did not understand the adaption mechanism, but rather had the impression that the system was presenting randomized information (see a study by Müller et al. (2009)). To counter comprehensibility issues caused by inaccurate context information, a number of researchers propose to display confidence values to users, see, for example, the work by Antifakos et al. (2005) or Yan et al. (2010).

Lim and Dey (2010) present a toolkit for generating eight different kinds of explanations automatically (such as what-if, why, how-to etc.), in order to increase the transparency of context-aware systems. Even though the connection to user trust is emphasized in their paper, they do not provide a mechanism to computationally model user trust. Cheverst et al. (2005) investigate techniques to increase the transparency of a system and to give users a higher level of control in a smart office environment. Their work is similar to ours since it investigates the tension between proactive system

behavior and user control and aims at improving the transparency of system behavior. Even though the topics they address have a tight relationship to user trust, they do not explicitly model user trust to decide on appropriate system behaviors.

# 3 The User Trust Model 

The main idea underlying our approach to model the users' trust in a computer system is to derive the trust from a set of intermediate dimensions, the so-called trust dimensions. These trust dimensions describe relevant properties of the system in question. Their definition is based on an earlier survey (Steghöfer et al. 2010) where we elaborated on the determinants of trust in highly dynamic computing systems and interviews with users (Leichtenstern et al. 2010) in order to identify trust factors that are of relevance to user interfaces. In these interviews, users were asked to indicate factors of trust that they felt contributed to their assessment of the trustworthiness of a user interface. The most frequent mentions felt into the following categories that formed the basis of our User Trust Model (UTM) (Kurdyukova et al. 2012):

- Comfort of Use ("The system should be easy to handle") ${ }^{1}$
- Transparency ("I need to understand what the system is doing")
- Controllability ("I want to be in control of the system's actions")
- Privacy ("The system should neither ask for nor reveal private information")
- Reliability ("The system should run in a stable manner")
- Security ("The system should safely transfer data")
- Credibility ("The system should have been recommended by others")
- Seriousness ("The system should have a professional appearance")

We have chosen to model the users' feelings of trust by means of Bayesian networks. A Bayesian network (BN) is a directed, acyclic graph in which the nodes represent random variables while the links connecting nodes describe the direct influence in terms of conditional probabilities (Russell and Norvig 2009). BNs were chosen because they very well meet requirements that should be accounted for by models aimed at assessing users' trust towards computer systems:

Trust as a subjective concept: Throughout literature, there is a consensus that trust is highly subjective. Different users respond individually to one and the same event. While some might find it critical if a system acts autonomously, others might not care. Also, a generally trusting person is also more likely to trust a computer system. To represent this subjective nature of trust in the BN, the model's uncertain belief about the user's trust can be represented by a probability distribution over different levels of trust.

Trust as a non-deterministic concept: The connection between events and trust is inherently non-deterministic. For example, we cannot always be sure that the user notices a critical event at all. Users may also consider a critical event as rather harmless.

[^0]
[^0]:    ${ }^{1}$ Typical statements made by the participants of our earlier study (Leichtenstern et al. 2010) are indicated in brackets.

BNs allow us to make predictions based on conditional probabilities that model how likely the value of a child variable is given the value of the parent variables. For example, we may model how likely it is that the user has a moderate level of trust if the system's behavior is moderately transparent. This allows for a much more flexible approach than, for example, rigid rules that exactly predict how a certain event or situation changes the user's trust.

Trust as a multifaceted concept: Computational models should be able to explicitly represent the relative contribution of different trust dimensions to the assessment of trust and should help predict the user's trust based on these dimensions. Furthermore, it should be easy to alter the model by adding or removing trust dimensions based on new experimental findings or if a certain dimension is not applicable in a given system. With BNs the modeling of relationships between trust and its dimensions is rather intuitive. For example, it is rather straightforward to model that reduced transparency leads to a decrease of trust. In the BN in Fig. 1 each trust dimension is represented by a specific node. Since exact probabilities are difficult to determine, the conditional probabilities were derived from empirical data collected in an online survey, see Sect. 4.1.

Trust as a dynamic concept: Trust depends on experience and changes over time. Following Lumsden (2009), we distinguish between Initial Trust and InteractionBased Trust. Both contribute to the user's overall trust in the system. Initial trust dimensions, such as seriousness, come into effect as soon as a user gets in touch with the system while interaction-based trust dimensions, such as transparency of system behavior, influence the users' experience of trust during the interaction. Again, BNs
![img-0.jpeg](img-0.jpeg)

Fig. 1 Generic User Trust Model for a Smart Energy System. Green context information; Red user traits; Blue trust dimensions; Orange decision nodes (system actions and utility node). (Color figure online)

allow us to model this distinction: Which trust dimension affects which aspect of trust and how both aspects influence the overall trust.

In Fig. 1, a generic BN for modeling trust in the smart energy system is shown. As mentioned above, each trust dimension is represented by its own node (shown in blue). Each trust dimension either affects the Initial Trust or the Interaction-Based Trust. The determinants of Initial Trust are Security, Seriousness and Credibility. Security, for example, could be conveyed by the use of certificates. A system's Seriousness is reflected, for example, by its look-and-feel. Credibility could be supported by additional information, such as a company profile.

Strictly speaking we do not model the relationship between user trust and actual system features, but the relationship between user trust and the user's subjective reflection of them. Even the best security standards will not put a user at ease if he is unaware of their existence. Visual indicators of security, such as closed padlock icons, might fail their purpose because users might be missing the knowledge to interpret them correctly (Dhamija et al. 2006). A recent paper by Florencio et al. (2014) shows that generally accepted rules for password security have to be revisited. Thus not even experts might be able to correctly assess a system's security. As a starting point, we do, however, not further distinguish between actual system features and the user's subjective reflection of them.

For the sake of simplicity, we assume that the initial trust dimensions do not change over time, i.e. we do not consider that a user might only notice a security certificate after having worked with the system for a longer time. The determinants for Interaction-Based Trust are Quality of Interaction and Reliability. The Quality of Interaction is an aggregation of Transparency, Controllability, Comfort of Use and Privacy.

Both the establishment of Initial Trust and Interaction-Based Trust are influenced by the users' Trust Disposition which is characterized by their Competence and general Confidence towards technical systems (shown in red), thus allowing to model the subjectivity of trust mentioned above.

By Confidence, we mean the propensity of individuals or a group of individuals to trust technology in general. Highly confiding people are more likely to trust a particular system than wary people. In our case, Competence refers to the user's general technical knowledge. A lack of knowledge about the performance of technical systems may lead to a miscalibration of trust (Lee and See 2004). For example, non-expert users might be tricked by a shiny interface and overestimate a system's ability, i.e. build up an inappropriately high level of initial trust. However, their interaction-based trust is likely to be seriously affected by system failures-in particular if they are not able to explain them.

We treat the trust dimensions as hidden variables, i.e. they cannot be observed directly, but may be inferred from observable context variables that depend on the specific system (shown in green). For example, the Smart Energy System currently considers the User state, the Social Context, and the Environmental Context.

Finally we included a node called System Action (shown in orange in the upper left corner), representing the different actions the system could take to react to context changes, such as "Switch the light on automatically" if the "User is arriving". Knowing the contextual situation, the BN can estimate the impact of the different system

reactions on the trust dimensions and thus on the user's overall trust. As an example, Transparency, on the one hand, could be negatively affected if the system automatically turns off the light when it is dark outside, while, on the other hand, Controllability could be negatively affected if the system switches the light on autonomously when the user is arriving.

In order to use the BN for decision-making, it was extended to an influence diagram by modeling System Action as a decision node and adding a Utility node that computes the utility of all possible actions and their consequences and returns the action with the highest utility. Since the goal of our work is to maintain and maximize user trust, the Utility node is attached to a node representing the User Trust and measures the utility of each single decision in terms of the resulting user trust.

# 4 Building a smart office 

In the following, we demonstrate how the UTM can be used to guide decision-making in an energy-aware device management system that controls the displays and the light in an office occupied by several people. For each type of device, a BN was constructed from the generic model described in the last section. Modeling the BN and integrating it into the system was done by using the GeNIe modeling environment and the SMILE reasoning engine respectively. ${ }^{1}$ Note that the terms UTM and BN will be used interchangeably from now on.

In the BN for operating the light, whether and, if so, which action the system takes to control the light basically depends on the luminance outside, the user's presence and whether his coworker is present. If the system recognizes a situation in which the light might be adjusted, it may perform the corresponding action autonomously or ask the user for permission via the mobile phone or via the display of the user's PC. In order to not risk disturbing the user, the system might even decide to do nothing, even if there was an action that could have saved energy. The BN for the display has a similar structure. However, it relies on a more fine-grained representation of the user's current activity to distinguish, for example, whether the user is sitting in front of a PC and working with it or engaged in other activities, such as reading a book or leaving his desk while staying in the room. An overview of possible system actions and the utilized context information in both BNs is given in Table 1.

Figure 2 shows the overall architecture of the Smart Office System (numbers in circles refer to the example below). The system runs on a central server which also stores the two UTMs for the light and display. The data needed to recognize the context information for both UTMs is gathered by Arduino-Sensors ${ }^{2}$ that are distributed in the office. We utilize light sensors to measure the outdoor luminance, ultrasonic sensors on the desks to detect the presence of persons and a flex sensor at the door to determine whether the office is empty (assuming that the door would be closed in this situation). The control of the devices (display and light) is conducted via a HomeMatic ${ }^{3}$ system

[^0]
[^0]:    ${ }^{1}$ http://www.genie.sis.pitt.edu/.
    ${ }^{2} \mathrm{http}: / / w w w . a r d u i n o . c c /$.
    ${ }^{3} \mathrm{http}: / /$ www.homematic.com/.

Table 1 Possible system reactions in different contextual combinations


![img-1.jpeg](img-1.jpeg)

Fig. 2 Architecture of the Smart Office System
and remote controlled plugs. Finally, the server can send messages to both the user's display and their mobile device.

As an example of how the system would dynamically adapt the light, let us consider the following example (see circled numbers in Fig. 2). The user is alone in the office, working on the computer. It is still early in the morning, so it is dark outside and the light is on. The system knows this since it is aware of the states of all devices,

and it regularly polls the sensors for the most recent context data (1). As long as the situation does not change (i.e. the context data stays the same), nothing needs to be done. However, a bit later it gets bright outside, which the system registers as a new situation. This new situation is then entered into the appropriate BNs (2). In our case, only the one for the light is affected, outside luminance does not concern the display.

The UTM now has to act and decide on a system action and may thus consider four possibilities to cope with this changed situation: (a) Do nothing, (b) Switch off the light automatically, (c) Ask the user via a message shown on their display whether the light should be switched off, or (d) Ask the user via a message shown on their mobile device. Considering the example, option (b) offers no control to the user and may confuse (i.e. be less transparent) since the action happens automatically and without explanation, but offers a high comfort of use. Option (c) offers more control and transparency but might disturb the user, but at least they can respond immediately, while with option (d) they can ignore the message on their mobile device and thus continue working undisturbed, but if they want to respond they have to pick up the device first. Finally, option (a) certainly leaves the user undisturbed and in control but might not be the proper reaction one expects from a smart office system (and would thus negatively impact comfort of use and transparency). For each of the four possible actions, their impact on the different trust dimensions and the resulting user trust is now calculated. The user trust directly translates to utility (the higher the trust, the higher the utility) and the action with the highest utility is chosen and communicated back to the server (3). Let us assume that it is option (d). Hence, a message is sent to the user's mobile device, giving them the choice of switching off the light or not (4). They choose yes, the answer is sent back to the system (5) which then switches off the light via the HomeMatic (6).

# 4.1 Gathering empirical data (online survey) 

In order to be able to generate decisions, the BNs had to be initialized with data. Both for the light and the display, we collected data in a web-based survey. In both surveys, participants were confronted with textual descriptions of typical situations during daily office routines. For each situation, possible system actions were proposed for the respective device that were supposed to improve the energy consumption of the users. Table 1 summarizes the situations represented by different settings of contextual variables and the possible system reactions.

The purpose of the survey was to discover for each situation which of the system reactions succeeded in maintaining user trust and which did not. To this end, the participants had to rate the system reaction in terms of Transparency, Controllability, Comfort of Use, and Trust using a 5-point Likert scale:

- Q1: I understood why the system was reacting in this way.
- Q2: I had control over the system.
- Q3: I found the system comfortable to use.
- Q4: I found the system to be trustworthy.

In contrast to our earlier work Wißner et al. (2014) where we focused on the relationship between privacy and user trust, the current work investigates the tension between

controllability, transparency and comfort of use. The scenarios were designed in a way that privacy issues were less of a concern (even though they could not be completely excluded). Consequently, we did not include any questions related to privacy in the user study.

All in all, 16 participants ( 7 female, 9 male) evaluated the situations for the light and 22 participants ( 9 female, 12 male) rated the situations for the display. The participants were aged between 24 and 51 years (mean: 28).

# 4.2 Initializing the Bayesian network 

The quantitative data obtained in the online survey enabled us to derive and model probability distributions for each trust dimension for all combinations of context and system reaction. The probability distributions for other node combinations that were not part of the data collected in the online survey (e.g. how Confidence and Competence influence Trust Disposition) were modeled after the results from a previous study (Bee et al. 2012). However, data for other user groups can be easily integrated into the BN by replacing the corresponding distributions in the BN. An interesting resource to explore is the work by Westin, who conducted a large number of studies to determine the percentage of people with certain levels of distrust or privacy concerns, see Kumaraguru and Cranor (2005) for a survey of these studies.

## 5 Live study in the lab

The BN has been trained with data from an online survey. Such data bear the advantage that data are relatively easy to obtain since the participants do not have to be presented with an interactive system. However, an online survey might not convey the experience of a real interaction and thus affect the ratings of the users.

Thus, the question arises of to what extent the BN is able to predict user trust and user preferences in a live setting based on training data that have been acquired by an online survey. To shed light on this question, we decided to conduct a live study in which the participants were presented with the smart office environment and actually able to interact with it.

The purpose of this study was to evaluate the decisions taken by the UTM focusing on two criteria: (1) Would the chosen system reactions affect the users' feelings of trust and the related trust dimensions in a positive way? (2) Would the system reactions match the actions favored by the users? Apart from evaluating the BN approach, we investigated the users' experience and acceptance of our smart office environment.

### 5.1 Experimental setting

During the study the participants had to run through different tasks and situations, all of which simulated the daily routine in an office occupied by several people. Changes in the participant's and the colleague's state (social context) were triggered by the participants themselves and by one of the experimenters who played the role of the participant's colleague. To ensure that all participants conducted the study under the same

conditions and in a realistic way, the room was darkened and changes in the outdoor luminance were simulated by a lamp and by covering and uncovering the light sensor.

# 5.2 Conducting the study 

At first the participants had to provide general demographic information and information about their experience with home automation systems and their trust towards computer systems in general. Furthermore, the participants were asked whether they considered themselves to have a trusting nature.

After a short introduction to the setting and the scenario, the participants had to conduct the first task, and the system showed the reactions that were selected for both devices according to the UTM. After that, the participants had to fill in a short questionnaire for each of the reactions. Each questionnaire included questions Q1Q4, which were also asked in the online survey. Furthermore, the users were asked to choose their preferred system action. For instance, the statement concerning the display and the first task was: "When I enter my office and sit at my desk, I prefer ...

- P1: ...no reaction from the display.
- P2: ...to switch the display on automatically.
- P3: ...to be asked via smartphone for permission to switch on the device.

After that, the procedure continued with the next task and the respective questionnaire. All tasks, the corresponding situations and the selected system reactions triggered by context changes are summarized in Table 2. To make the experiment more realistic, the tasks were embedded in a coherent story.

After rating the last task, the participants had to state what they liked and disliked about the system and to rate statements related to their experience during the usage and their attitude towards the system.

### 5.3 Results

Overall six women and 18 men aged between 23 and 33 (mean: 26) took part in the study. They studied and worked in all kind of professions related ( $88 \%$ ) and not related ( $12 \%$ ) to computer science. All statements in the questionnaires could be rated on a 5-point Likert scale. Ratings lower than 3 were interpreted as disagreement, ratings higher than 3 as agreement with a statement, and a rating of 3 as a neutral attitude. Only five persons reported a high or very high amount of experience with technology for controlling parts of their home environment, such as automatic timers or blind control systems. Eighteen people rated their experience with home automation technology as low or very low. One participant gave a neutral rating.

The participants also had to reflect on their confidence. They had to answer two general statements and one statement related to computer systems. Concerning the statement: I act based on the saying "Trust, but verify", only one participant disagreed. $63 \%$ of all participants agreed and $33 \%$ had a neutral attitude. Concerning the statements I am overly trusting and On most systems, you can be assured that they will do what they should, one third each agreed, disagreed, or rated neutrally.

Table 2 Tasks, changed context variables and system reactions of the user study


Nothing: do nothing, Auto: switch automatically, Phone: ask via smartphone, Display: ask via display

The participants consistently gave high ratings (between 4 and 5) for the criteria Transparency, Controllability, Comfort of Use, and User Trust when evaluating the reactions the system had chosen for the adjustment of the light (see Table 3).

However, some participants criticized that trust was impaired because of missing feedback when the light was switched off after they left the office. Despite these high ratings, in situations in which the system sent a message to the participants' phone, other system reactions were preferred by most of the participants (see Table 3 Preferred SR). These findings were in line with several statements of the participants. For example, several users mentioned that using a phone is inconvenient in many situations - either because it is not within reach or because they have to interrupt their work to read the message on the phone. Accordingly, some users preferred autonomous system actions instead of repeated messages on their phones because this would make the system less obtrusive.

In contrast, the automatically generated reactions for the display matched the preferences of most of the participants in all situations (see Table 3-Preferred SR). In most of the situations the participants clearly favored autonomous reactions for the display (as in the online condition), but at the expense of Controllability and User Trust (see Table 3). While the average trust ratings were still quite high (between 3.5 and 4)

Table 3 Results of the live study: user ratings (mean (M); standard deviation (SD)) for the trust dimensions and the perceived trust related to the selected system reaction (SR), and the preferred SR by most of the users


C: coworker, Nothing: do nothing, Auto: switch automatically, Phone: ask via smartphone, Display: ask via display

the average ratings for Controllability were only mediocre (between 2.5 and 3.5). The ratings for the trustworthiness of autonomous reactions were affected, among other things, by a missing authentication mechanism after switching on the display and by a lack of feedback when leaving the room. The low ratings for "Controllability" could be explained by requests for functionality to set or disable the automatic control of the display.

The concluding questions also showed promising results. Most participants were satisfied ( $83 \%$; M:3.96; SD: .68) and agreed that the system assisted them to improve their energy consumption ( $96 \%$; M: 4.71; SD: .54), that it behaved adequately ( $88 \%$; M: 4.38; SD: .70), and that it was transparent ( $100 \%$; M: 4.96; SD: .20). The lower, but still acceptable results for unobtrusiveness ( $58 \%$; M: 3.71; SD: 1.10) could be mainly explained by the fact that the users had to operate the mobile phone. Further results showed that most of the participants did not feel distracted ( $75 \%$; M: 2.00; SD: 1.00), restricted ( $88 \%$; M: 1.83; SD: 1.07), or observed ( $63 \%$, M: 2.33; SD: 1.18).

# 6 Further investigations 

The results of the live study gave promising results for the control of the display. Most participants preferred the actions that were selected by the system. However, the system's decisions for controlling the light frequently did not match the participants' choices. In the live study, scores for the trust dimensions and user trust were only obtained for the selected system action. Thus, users might have been biased because they were only presented with the system's choice. Furthermore, user scores for the alternatives could help shed light on the question of why participants preferred a particular system reaction.

For these reasons, we decided to complement the live study by a live survey that was conducted under similar conditions as the live study. In the following, the design and the results of the live survey will be described.

### 6.1 Live survey: experimental setting and execution

The aim of the live survey was to acquire user ratings for all combinations of situations and possible system reactions under natural conditions. The experimental setting for the live survey was adopted from the live study (see Sect. 5.1) in order to obtain comparable results. However, instead of running the real system and confronting the participants only with the system actions selected by the UTM, all possible system actions were shown to the participants in each situation.

At the beginning of the survey the participants had again to provide demographic data. After a short introduction to the setting and the scenario, all possible system actions were presented to the participants. They then had to enter the unoccupied and dark office. After entering the room, they were immediately confronted with the first set of possible system actions designated for the light in the office and they had to rate statements related to perceived Transparency, Controllability, Comfort of Use and Trust for each of these actions (see Q1-Q4 in Sect. 4.1).

After rating all system actions, the users were also asked to indicate which system action they preferred. However, in this survey the participants were not to choose one of these actions. Instead, they had to rate the statement "I would prefer the system action..." for each action on a 5-point Likert scale in order to enable an easier comparison of preferences. Then the procedure continued with the next situation and the corresponding questionnaire. The entire sequence of tasks and situations is summarized in Table 2.

In total, eight men and two women aged between 23 and 35 (Mean: 28) took part in the live survey.

# 6.2 Performance of the User Trust Model 

We further investigated how well the UTM performed when compared to the data gathered in the live study and live survey, both in terms of preference and user trust. Similar to the evaluation of the live study described above, we compared the decision generated by the UTM for each situation with the one the users found the most preferable or the most trustworthy.

For the display, most participants ( $73 \%$ for the live study and $90 \%$ for the live survey) preferred the actions chosen by the UTM. The selected system actions also received the highest trust ratings from $80 \%$ of the participants. This means that the trust and preference ratings showed similar tendencies. As mentioned above, in the live study we only asked the participants whether the action taken by the UTM was trustworthy, but did not ask about the trustworthiness of the alternatives. Thus, we only have trust ratings for the actions taken, which were quite high with an average trust of 3.75 (display) and 4.18 (light).

The actions generated by the UTM for the light were much less in line with the preferences of the users. Only $34 \%$ of the people participating in the live study would choose the same actions as the system. In the live survey, only $18 \%$ of the participants expressed the highest preference for the selected system actions. Nevertheless, $80 \%$ of the participants gave the selected system actions the highest trust ratings. The results show that the UTM was able to create trustworthy decisions, but also that trust was not the only factor that determines which action a user preferred.

### 6.3 A further analysis of the trust dimensions

Since the comparison of the UTM's assessments and the collected data revealed differences between the users' trust and their preferences, the collected data were analyzed in more detail. The aim was to identify major factors that affected the users' preferences.

At first, the trust ratings provided by the participants in the online survey as well as in the live survey were investigated. In both surveys, the system actions achieved a similar level of trust for most of the situations. In the live survey, the participants considered actions performed by the system as more trustworthy ( 4.18 on average on the 5-point Likert scale) than doing nothing ( 3.28 on average) albeit not significant. They also expressed a high preference for proactive system reactions ( 4.46 on average)

compared to doing nothing ( 2.47 on average), asking for confirmation on the mobile phone ( 2.59 on average) or asking for confirmation on the display ( 3.18 on average). We furthermore found that trust tended to get higher ratings in the live survey ( 3.91 on average) than in the online survey ( 3.16 on average), a trend we had already observed in Wißner et al. (2014). Apparently the users have more trust in a system that they can actually experience than in a system that is just verbally described to them. With the exception of doing nothing, most system actions got quite high mean values for trust (above 4.0). In our earlier work (Wißner et al. 2014), trust ratings for system actions showed greater variations. One reason is that our earlier work also investigated situations that introduced serious risks to privacy, such as viewing personal information or photos on a public display, depending on the system action chosen. Consequently, users gave a number of system actions rather low trust ratings.

The first trust dimension that was investigated in more detail was perceived Transparency. Both in the online and the live survey, most possible system actions achieved high mean ratings for Transparency (around 4.0 on the 5-point Likert scale). Obviously, most system actions seemed plausible to the participants. Remarkably, the system action "Do nothing" only achieved moderate ratings in $75 \%$ (online survey) and $88 \%$ (live survey) of the situations respectively. In a number of cases, it was even rated significantly less transparent than an automated system reaction (see Table 4). At first, this result may appear surprising. However, we believe that a proactive behavior is noticed by a user more easily than inactivity, which might be one reason for the less positive ratings the users gave to "Do nothing". Interestingly, the result is in line with the experience reported by a company described by Picard and Klein (2001). Customers who bought a product that did not work properly and got excellent support were more likely to keep buying their brand than customers who did not figure out any problems at all with the product.

Table 4 Investigated trust dimension: transparency—significant results of a repeated-measures ANOVA and a Bonferroni-Post-Hoc-Test


Nothing: do nothing, Auto: switch automatically, Phone: ask via smartphone, Display: ask via display

* $\mathrm{p}<.05 ;{ }^{* *} \mathrm{p}<.01 ;{ }^{* * *} \mathrm{p}<.001$

Next, the participants' perceived Controllability in the surveys was analyzed. In the live study, autonomous decisions by the UTM resulted in lower scores for this trust dimension. These findings could be confirmed for most situations of the online and live survey. In all situations, automatic system actions only achieved mean ratings lower than 3.0. They were perceived as less controllable than performing no system action at all or system actions that involved asking the users for confirmation before performing an action. In many cases, the differences were statistically significant. Consistently high ratings for Controllability were achieved by the system action "Ask the user for confirmation via her or his smartphone". However, a comparison of Tables 5 and 6 reveals that the low Controllability scores for automatic system actions did not negatively affect the participants' preferences for those actions.

Although automatic system actions resulted in a decreased perceived control over the system, they were rated as the most preferred actions in most of the situations in which a system reaction was expected. In contrast, "Ask the user for confirmation via his or her smartphone" only achieved mean ratings lower than 3.0 or less in most of the situations (see Table 6). Although this system action was mostly perceived as very controllable, in many situations, participants preferred to have the system respond automatically or to give confirmations via their display.

These findings raised the question of which trust dimension would affect the participants' preferences for a particular system action the most. The results of the live study and the statements of the participants indicated that perceived Comfort of Use could be a decisive factor. To confirm these findings, the ratings for perceived Comfort of Use obtained in the surveys were analyzed in detail. In both surveys, automatic system actions applied to the light and the display scored best. In the live survey, the ratings were in general above 4.0 on the 5-point Likert scale and in some cases even higher than 4.5. In comparison, "Do Nothing" and especially the action "Ask the user for confirmation via her or his smartphone" scored significantly worse (see Table 7). In many situations, participants gave the lowest score for the latter action. In most situations, the mean ratings were lower than 3.0, in individual cases even lower than 2.0.

Overall, an analysis of the participants' preferences revealed that they preferred more comfortable system actions over more controllable actions in both surveys. This finding was confirmed by their statements during the live study as well as during the live survey. The participants liked the idea of being asked in some situations. However, they considered a message on their smartphone only reasonable when they entered or left the office. When they were seated at their desk, they preferred autonomous decisions by the system or messages that were shown on their displays. Using the phone was considered to be inconvenient, e.g. because it was often not within reach and it was also considered obtrusive because the participants would have to interrupt their work every time the phone received a message.

In our earlier work (Wißner et al. 2014), the mismatch between online and live data was less pronounced than in the current paper. We assume one reason to be the fact that the scenarios investigated in the earlier paper included situations in which the user's privacy was at stake. Consequently, the users' choice between different system actions was mainly based on privacy concerns both in the online and the live setting. According to the live survey presented in this paper, users seem to weight

Table 5 Investigated trust dimension: controllability—significant results of a repeated-measures ANOVA and a Bonferroni-Post-Hoc-test


Nothing: do nothing, Auto: switch automatically, Phone: ask via smartphone, Display: ask via display

* $\mathrm{p}<.05 ;{ }^{* *} \mathrm{p}<.01 ;{ }^{* * *} \mathrm{p}<.001$
trust dimensions differently depending on whether they are confronted with a real system or just a verbal description of it. For example, participants expressed a stronger preference for proactive system behaviors in the live survey than was suggested by

Table 6 Investigated: preference-significant results of a repeated-measures ANOVA and a Bonferroni-Post-Hoc-test


Nothing: do nothing, Auto: switch automatically, Phone: ask via smartphone, Display: ask via display * $\mathrm{p}<.05 ;{ }^{* *} \mathrm{p}<.01 ;{ }^{* * *} \mathrm{p}<.001$
the online data from which the Bayesian Network was trained. While our earlier work seemed to indicate that it is possible to train Bayesian networks from online data and employ them in live scenarios, the current paper shows that the reliance on online data is only possible to a limited extent.

Table 7 Investigated trust dimension: comfort of use—significant results of a repeated-measures ANOVA and a Bonferroni-Post-Hoc-Test


Nothing: do nothing, Auto: switch automatically, Phone: ask via smartphone, Display: ask via display

* $\mathrm{p}<.05 ;{ }^{* *} \mathrm{p}<.01 ;{ }^{* * *} \mathrm{p}<.001$


# 7 Conclusion 

We presented an approach for trust-based decision-making for smart and proactive environments based on Bayesian networks, the User Trust Model. It assesses the users' trust experienced while interacting with a system and performs appropriate (i.e.

trustworthy) system reactions to properly adapt to new situations. We described the construction of the UTM, its integration in an office setting, and its initialization with empirical data. The results of a live user study revealed that the system generally succeeded in performing appropriate actions in the investigated situations. Earlier work on computational models of trust either focuses on trust between users or trust between software or hardware components while our work attempts to explicitly model affective user trust towards a pervasive environment. We would like to note that the prediction quality for user trust has only been indirectly measured in this paper. Our approach selects the system action that is supposed to create the highest amount of user trust. Our experiments showed that the users give the selected system actions indeed high trust ratings. However, we did not explicitly address the question of how accurately the UTM predicts the user's current level of trust.

Even though the UTM approach has been developed and evaluated for an energy management system, the basic mechanism is applicable to other kinds of ubiquitous systems as well. Following a component-based software development approach for user modeling as suggested by Dim et al. (2015), the basic structure of the BN representing the dependencies between trust and its dimensions could be reused by other developers for their applications. Only the nodes representing the context and possible system actions would have to be adapted to the corresponding applications. In this way, the development of applications that make decisions based on user trust could be significantly facilitated.

In addition to the live study, we performed a live survey, which gave us not only ratings for the performed system actions, but also for alternatives. The live survey revealed that users had a high amount of trust in the chosen system action, but generally preferred a higher degree of proactive system behavior in order to increase the comfort of use. Obviously, the users' weighting of the trust dimensions in the online survey differed from that in the live survey. Since our results show a discrepancy between the user's trust and preferences, future work should investigate whether giving more weight to Comfort of Use when selecting a system action could rectify this. Another option to explore would be to collect a sufficient amount of live data by recruiting a larger number of users as a basis for the training of the Bayesian Network which was initialized with data obtained from an online survey.

To confront the users with realistic scenarios, we embedded the single tasks into a coherent story representing a working day in the life of the user. As a consequence, the sequence of tasks was not randomized, but determined by the story line. While this approach helped us create a plausible scenario for users, it might have led to an overfit of the Bayesian Network. Future data collection efforts should concentrate on longer scenarios with a larger number of tasks that can be presented in randomized order.

The Bayesian Network used in the paper was initiated by data from 38 individuals. Consequently, the Bayesian Network rather reflected the attitude of a variety of users as opposed to an individual user. In the future, we will investigate how to improve the accuracy of the UTM by incorporating knowledge about user-specific attitudes. Depending on their trust disposition, users might favor different system reactions. For example, users that tend to distrust technical systems might give more importance to a high level of control than to a high level of comfort. A promising approach might

be to distinguish between different categories of users based on multiple dimensions (Knijnenburg et al. 2013). In comparison to the live study, the questionnaire for the live survey contained more questions about participants' opinions and habits concerning sustainability and their trust towards other people and technical systems in general, so this data could be included in the model in the future. In order to achieve an even higher degree of personalization, the UTM could also be trained with data from individual users. In the ideal case, the UTM should not require extensive training before it can be used, but dynamically adapt to people's preferences by learning from their behavior during the interaction with the smart environment.

In our current work, we focused on trust as an attitude as opposed to reliance as a behavior (Lee and See 2004). To evaluate the system's ability to select actions that maximize user trust, we asked participants' to rate the trustworthiness of individual actions. In addition to investigating subjective user impressions, more objective measurements should be addressed, such as the user's reliance on a system as a result of user trust. That is we should investigate to what extent users are willing to relinquish control to the system.

Another important aspect is the decision making for more than one user. For example, some participants wondered whether they were the only person in control of the light. Therefore, the UTM should be extended to be able to consider the trust of all affected users.

So far, we focused on the question of how particular system actions influence the user's level of trust. However, the users' level of trust does not only depend on the momentary system behavior, but also on their experience with the system in the past. For example, users might forgive a minor bug if it occurs for the first time. However, if the system fails repeatedly, the users' trust will be affected significantly. In order to consider how user trust felt at a particular point in time influences user trust experienced at a later point in time, we intend to extend the Bayesian Network to a Dynamic Bayesian Network that allow us to model the dependencies between the current states of variables and earlier states of variables.

Acknowledgments This research is co-funded by OC-Trust (FOR 1085), funded by the German Research Foundation (DFG) and by IT4SE, funded by the German Federal Ministry of Education and Research (Grant number NZL 10/803 IT4SE) under the APRA initiative. The core of our implementation is based on the SMILE reasoning engine and the network shown in this paper was created using the GeNIe modeling environment. Both SMILE and GeNIe are developed and contributed to the community by the Decision Systems Laboratory, University of Pittsburgh and available at http://www.genie.sis.pitt.edu/.
