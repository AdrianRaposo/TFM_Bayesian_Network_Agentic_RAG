# LJMU Research Online 

Matellini, DB, Wall, AD, Jenkinson, ID, Wang, J and Pritchard, R
A Three-Part Bayesian Network for Modeling Dwelling Fires and Their Impact upon People and Property.
http://researchonline.ljmu.ac.uk/id/eprint/8828/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Matellini, DB, Wall, AD, Jenkinson, ID, Wang, J and Pritchard, R (2018) A Three-Part Bayesian Network for Modeling Dwelling Fires and Their Impact upon People and Property. Risk Analysis, 38 (10). pp. 2807-2104. ISSN 02724332

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# A three-part Bayesian network for modelling dwelling fires and their 

## impact upon people and property

D.B. Matellini, A.D. Wall, I.D. Jenkinson \& J. Wang<br>Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John<br>Moores University, United Kingdom

R. Pritchard<br>Merseyside Fire and Rescue Authority, Liverpool, United Kingdom

# ABSTRACT 

In the UK, dwelling fires are responsible for the majority of all fire related fatalities. The development of these incidents involves the interaction of a multitude of variables which combine in many different ways. Consequently assessment of dwelling fire risk can be complex which often results in ambiguity during fire safety planning and decision making. In this paper, a three-part Bayesian Network model is proposed to study dwelling fires from ignition through to extinguishment, in order to improve confidence in dwelling fire safety assessment. The model incorporates both hard and soft data, delivering posterior probabilities for selected outcomes. Case studies demonstrate how the model functions and provide evidence of its use for planning and accident investigation.

Keywords: Bayesian network, dwelling fires, human reaction, probability of fatality, costbenefit.

## 200-CHARACTER SUMMARY

This paper presents a probabilistic graphical model of events in dwelling fires. Case studies demonstrate how the model can be used to produce information that can improve fire safety planning and accident investigation.

# 1 INTRODUCTION 

There is a risk of fire within virtually every existing structure and it is broadly accepted that complete safety from fire is not possible. This is particularly true for dwellings where the accidental actions of the occupants and artefact defects result in a high number of fires and subsequent casualties. Fire risk assessment is a complex task due to the multiple variables and potential outcomes that must be examined. There will normally be a degree of causality between such variables and events which must be considered when assessing a situation. For example, if fire detection is successful this may lead to or cause communication; if communication occurs then human reaction may take place, which may in turn lead to calling the emergency services or attempting to escape, and so on. There are in reality a multitude of variables which affect each other in different ways and at different moments. Sometimes two or more factors must combine to produce an event whilst on certain occasions additional factors will act to escalate the event. Indeed there are many possible combinations that must be considered when examining a fire situation. Taking the assessment of human reaction during a fire as an example, consideration would need to be given to elements such as fire type, fire cues, occupant alertness, and physical / mental condition. Sometimes other influencing variables may apply such as time of day or time of year. Because of the multitude of interrelated variables, fire scenarios can be quite complex affairs. This limits the precision of risk assessments of fire events including the probability of occupant survival, resulting in reasoning and decisions often taking place under uncertainty. Upon such a background, this study contributes towards the assessment of fire safety within dwellings, capturing and reducing the uncertainty of these complex situations. Case studies demonstrate how this can improve confidence in fire safety decision making.

In this paper a three-part Bayesian Network (BN) is proposed, to model UK dwelling fires from the onset of fire through to extinguishment. BNs are Directed Acyclic Graphs of nodes which

represent parameters; causal relationships between nodes are encoded through conditional probability tables. They are suitable for modelling situations which involve uncertainty and can improve the process of decision making. Work by Meacham (2004) discusses further the suitability of BN in this context. The paper also examines how the Analytic Hierarchy Process (AHP) and utility theory can assist decision making for fire risk problems. Another useful approach for studying dwelling fires, in this case focusing upon the behaviour of people, is presented in Ploubidis, Edwards and Kendrick (2015). In this research latent variable models are used to summarise multiple behaviours of occupants. The method allows multiple fire safety behaviour questions to be combined into a single binary summary measure of fire safety behaviour. It is similar to BN in that it includes unobserved random variables, which can be either discrete or continuous. The research can be used to assist with defining fire escape plans. Research which centres on dwelling fires is few and far between. The majority of studies tend to revolve around numerical modelling of fire spread. In terms of modelling dwelling fire safety, BN is a robust and flexible method that can incorporate the uncertainty which is innate to dwelling fires.

In our model, the interaction of numerous variables involved in dwelling fires is represented, to determine the probability of occupant survival, property damage, and other events of interest. This should assist in identifying what the most pressing fire safety issues are, with a view to improve mitigation of fire consequences. This paper builds on work conducted by Matellini, Wall, Jenkinson, Wang and Pritchard (2013a and 2013b), in which parts one and two of the model are presented. Part one of the model covers the initial fire development in a dwelling and focuses on factors that affect human reaction to a fire such as type of fire, time of day, etc. Part two of the model represents further fire development, taking into consideration the actions of the occupant, the location of the dwelling, and the intervention of fire and rescue services, among others. The state of the occupant is assessed at two different stages of the fire. Readers

wishing to gain a greater insight into parts one and two of the model, should refer to (Matellini et al., 2013a and 2013b).

# 2 BACKGROUND 

### 2.1 UK fire fatality statistics and economic significance

Although fire safety has generally improved over time, there are still around 300 fatalities and 9000 non-fatal injuries per year in the UK (Department for Communities and Local Government [DCLG], 2011a). Statistically, dwelling fires account for a small proportion of total fires but they result by far in the greatest number of fatalities. Figure 1 presents a graph with four data sets to illustrate this point. The total number of fires and dwelling fires in the UK are plotted between 1990 and 2011, with the former showing a more undulating and pronounced drop over time compared to the latter. Total fatalities and dwelling only fatalities are also shown on the graph, with both having fallen by around $55 \%$ between 1996 and 2010; however, in 2010 dwelling fires accounted for just $16 \%$ of all fires yet dwelling fire fatalities made-up $79 \%$ of all fire fatalities. Furthermore, the number of dwelling fires which occur per fatality has remained relatively steady over the last decade indicating that more needs to be done to reduce the impact of fires in dwellings when they do occur.

![img-0.jpeg](img-0.jpeg)

Source: Adapted from Communities and Local Government (2012, 2011a, 2010, 2008, 2002), Welsh Government (2012), The Scottish Government (2012), Northern Ireland Fire and Rescue Service (2012).

Figure 1. Number of fires, dwelling fires, fatalities, and dwelling fatalities in the UK. (Note 2011 data is provisional).

Placing monetary value on a human life is a highly debatable and sensitive issue, and goes against the ethos of UK Fire and Rescue Services (FRS). However, for certain types of analysis, it is useful to have an idea of the impact of a disaster upon humans, in economic terms. The model presented in this paper includes an output which does just that, and this gives an additional dimension to the results. DCLG (2011b) publish annual statistics for the estimated cost of consequences of fire in England. One of the consequence categories is "fatalities and injuries". The value for the year 2008 was $£ 552$ million (m) for fatalities, $£ 780 \mathrm{~m}$ for major injuries, and $£ 70 \mathrm{~m}$ for slight injuries. There were 341 fatalities in England in 2008. From this it is possible to derive the value placed on human life in the publication by dividing $£ 552 \mathrm{~m}$ by 341; this gives $£ 1,619,000$. In other work on the cost of fire in England and Wales, Stevens (2008) uses the value $£ 1,375,000$. The average of these two numbers is $£ 1,496,884$. This figure

rounded to the nearest $£ 10,000$ becomes $£ 1.5 \mathrm{~m}$; for simplicity, this was the value adopted for human life in this research. Regarding major injury, Stevens quotes a figure of $£ 155,000$. Since the work by Stevens on the cost of risk from fire lies within realm of this research, this value was the one adopted.

# 2.2 Factors in dwelling fires 

Many factors will affect the development and outcome of a dwelling fire. One of these factors is the fuel present; dwellings often feature highly combustible and toxic materials which result in rapid development of fires and production of lethal gases. Another important aspect of dwelling fires is the behaviour of the occupants. Deciding whether to fight the fire or escape may significantly affect the chances of survival. The physical features of a dwelling also have a major role to play in the outcome of a fire for example the availability of passive fire protection measures (fire doors, fire resistant upholstery, etc.) and active ones (smoke alarms, sprinklers, etc.).

### 2.3 Overview of FRS response

The impact a well prepared FRS crew can have upon a fire is primarily governed by the time it takes to arrive at the incident; this important factor is incorporated into the modelling presented in this research based upon the response standards set by the FRS for Merseyside (Northwest UK), who are collaborators of this research. This FRS, known as Merseyside Fire and Rescue Services (MFRS), plans the location of its fire stations, appliances and personnel so as to be able to respond in a timely manner according to the level of risk they have preestablished for areas of similar population known as Lower layer Super Output Area (LSOA). MFRS have assigned each LSOA with either a "High", "Medium", or "Low" risk level. Response times to incidents are set according to these levels of risk as set out below; the

performance target is to realize these times on $90 \%$ of occasions (Merseyside Fire and Rescue Service, 2009):

- High Risk: First attack within 5 minutes with additional support within 8 to 10 minutes.
- Medium Risk: First attack within 6 minutes with additional support within 9 to 11 minutes.
- Low Risk: First attack within 7 minutes with additional support within 10 to 12 minutes. Fire and rescue response in Merseyside is coordinated through MFRS’ Mobilising and Communication Centre (MACC) which processes all emergency calls redirected from the 999 centre. MACC identifies the type of incident and prioritizes it with regards to other ongoing incidents before notifying the closest suitably prepared available appliance; additional support for the first appliance is subsequently coordinated.


# 2.4 Previous fire and BN research 

Fire science and fire safety have a multitude of dimensions about which research has been conducted. If the perspective of sequence of events during a fire is taken, it is possible to study fire ignition and causes, fire development and smoke spread, detection and fire cues, human response, evacuation, effectiveness of mitigating measures such as sprinklers and fire doors, and firefighting response. Fire science and safety can also be examined from the perspective of locations; in this paper fires in dwellings are examined because of the high rate of fatalities when compared to other fire locations. Within most of the aforementioned fields there is a plethora of research. For example work has been conducted on the topic of fire cues and mitigating measures within homes by Sakata (2004), Hasofer and Bruck (2004), Bruck and Brennan (2001), Yung (2008), and Thor and Sedin (1980). Furthermore, specific research exists on fire alarm systems (Jing and Jingqi, 2012), smoke alarms (Bukowski et al. 2007; Hasofer and Thomas, 2007; Parmer, Corso, and Ballesteros, 2006; Bruck, 2001; Hasofer, 2001;

Hume, 1997a and 1997b), sprinkler systems (Melinek, 1993), and fire doors (McDermott, Haslam, and Gibb, 2010). Aspects of fire growth, in particular flashover fires are examined by Hofmann, Knaust, and Aschenbrenner (2007), and Kennedy and Kennedy (2003), the former focusing on fires within children's bedrooms. Analysis of fire casualties is conducted by Hasofer and Thomas (2006), and Holborn, Nolan, and Golt (2003). Aspects of emergency response and firefighting have also been dealt with for example the timeliness of response (Holborn, Nolan, and Golt, 2004; Mattsson and Juas, 1997; Haurum, 1984). What seems however to be sparse, is research which amalgamates these many dimensions of fire safety, to provide a more inclusive measure of risk. Matellini et al. (2013a) take steps towards achieving this by presenting research based on a BN to assess human reaction to dwelling fire cues prior to the arrival of emergency services. This work is advanced by Matellini et al. (2013b) to incorporate further fire development, occupant response, and intervention by emergency services; in this work a second BN is developed and connected to the original BN using four output nodes. Case studies demonstrate how the survival of the occupant can be affected by conditions such as the location of the property and the intervention of the fire service. Some interesting contributions are made, however, it was noted that the work did not address fires which became complicated and spread to other dwellings. This is an issue which is addressed in the present paper.

Various techniques exist which can support aspects of risk assessment within fires, but probably the most widely applied are Fault Tree (FT) and Event Tree (ET) analysis. This may be because of their step-by-step logical approach, which facilitates establishing paths that lead respectively to and from the occurrence of an unwanted event. There are however shortfalls to FT and ET, specifically that they are not suited to handling multiple parameter dependencies and uncertainty such as those involved in fire events (Khakzad, Khan, and Amyotte, 2011; Zerrouki and Abdallah, 2015). BNs on the other hand, would be suitable for dealing with such

situations. One of the advantages of using this method over alternate techniques, is that it is effective at expressing uncertainty and subsequently inferring results through the insertion of evidence into nodes. Furthermore, BNs facilitate the incorporation of expert judgement into a study, which is particularly useful when hard data is deficient. BNs provide a flexible graphical structure of the subject they are modelling, which is useful for displaying results and formulating further ideas. One of the other uses of BNs is that they can be used as decision making tools. Utility nodes and discrete decision nodes can be attached to a network. The former allows economic value to be placed on particular outcomes or states of a parent node, which when combined with probability, produces a value for risk in economic terms.

A discipline which has applied BN extensively for decision making is medicine particularly for diagnosis, decision of treatments, and prognosis (Smith, Doctor, Meyer, Kalet, and Phillips, 2009; Velikova, Samulskil, Lucas, and Karssemeijer, 2009; Antal, Fannesa, Timmerman, Moreaua, and De Moora, 2003; Onisko, Druzdzel, and Wasyluk, 2001; Wang, Zheng, Good, King, and Chang, 1999; Spiegelhalter, Phillip Dawid, Lauritzen, and Cowell, 1993; Lauritzen and Spiegelhalter, 1998). Other fields in which BN has proved useful include computer sciences (Lauria and Duchessi, 2007; Larranaga and Moral, 2011; Bruza and Van Der Gaag, 1994), industrial safety and risk (Hanninen and Kujala, 2012; Khakzad, Khan, and Amyotte, 2011; Martin, Rivas, Matias, Taboada, and Arguelles, 2009; Trucco, Cagno, Ruggeri, and Grande, 2008; Kannan, 2007; Kohda and Cui, 2007), and finance (Lu, Bai, and Zhang, 2009; Sun and Shenoy, 2007; Kjaerulff and Madsen, 2005; Neapolitan, 2003). A variety of research also exists in which BNs have been developed to address fire related problems, such as fire safety in buildings. Holicky and Schleich (2000) present research in which a BN is used to model an office building fire and subsequently serve as a decision tool for supporting a fire protection system. The network includes aspects of fire detection, automatic suppression, fire brigade intervention, and some utility costs. In succeeding research, Holicky and Schleich

(2002) provide a further developed model to assess the cost of structural collapse and human injury/death resulting from a fire. Various decision and utility nodes are included and used to provide risk profiles for structural collapse dependent upon different safety configurations. Though the model has virtues, it does not take into account the effect that fire rescue services and other associated time-dependent actions, could have upon the situation. Subsequent similar themed work, does however take into account these considerations (Hanea and Ale, 2009). In this research, a BN is developed for a building fire to examine the likelihood of death. The purpose of the model is to serve as a planning tool for new buildings. The virtue of this model is that it incorporates modelling of continuous variables through a distribution-free version of BN. A reduced version of the model is used for demonstrating how aspects of compartment design, alarm detection, response, and evacuation affect the chances of survival. In subsequent work Hanea, Jagtman, and Ale (2012) present a BN to analyse the 2005 Schiphol Cell Complex fire. The network serves as both an accident analysis tool and a building design planning tool. Further application of BNs to model building fires has been conducted to represent the spread of fire from one compartment to another, by mapping the floor plan of a building onto a BN (Cheng and Hadjisophocleus, 2009); the compartments, stairwells and elevator shaft of the building are represented by the nodes. The research develops case studies with the model, for a building with and without sprinklers. Other interesting work with BN was conducted by Khakzad, Landucci, and Reniers (2017) who incorporate into their model temporal evolution of random variables over a discretized timeline. Dividing the timeline into a number of slices, allowed for improvements in the assessment of fire protection systems during fire under domino effect, in chemical plants.

As can be appreciated a reasonable amount of work already exists on the application of BNs to assess aspects of fire safety, but this has been limited mainly to buildings. Such research is

indeed important, but attention must also be paid to dwelling fires where, as previously discussed, the majority of fire fatalities occur.

# 3 METHODOLOGY 

### 3.1 BN model construction

When building a BN, it is important to define clearly the domain which it is meant to represent. Nodes and their states must be appropriately named paying close attention to what they symbolize and how they interrelate, so as to leave no room for misinterpretation. The outputs of a BN will only be meaningful if it has a rational structure and appropriate input data.

The BN model developed in this research is designed to represent conditions and events during a generic dwelling fire from ignition through to extinguishment. The model's structure and data, typifies circumstances from the majority of domestic residence dwellings which have been constructed to relatively similar size, from common building materials. The model, however, is not intended to represent certain dwellings which have significantly different character, e.g. mansions, listed buildings, etc. Developing a model to represent all types of dwellings would not have been practical because of the complexity which would have been generated. Consequently, the BN is designed to represent a generic dwelling with the following attributes:

- Has a maximum of ten bedrooms.
- Is between one and three stories high.
- Has a maximum of one basement level.
- Is not a listed building.

The model was built using the software Hugin Researcher release 7.6 (Hugin Expert A/S, 2012). Several versions of the network were developed over a period of 18 months, before a decision

was taken to proceed with the current version. This involved discussion and exchange of ideas with fire safety experts, including some FRS officers. An eleven step procedure for developing the model parts was defined and applied to ensure consistency throughout the process of building each model part; these steps are outlined below:

Step 1: Establish the domain - set the boundaries for the model as one, and for each of its parts. Step 2: Establish the objective - define what outputs are being sought from the network. Step 3: Establish associated influential themes - clarify the subject matter which affects the outputs established in step 2.

Step 4: Brainstorm nodes - brainstorm all possible parameters that are relevant within the associated themes identified in step 3.

Step 5: Select appropriate nodes - following discussion with experts and reviewing of literature, the list of nodes from step 4 should be reduced to those most pertinent to the domain. Step 6: Connect nodes - connect the nodes and link model parts through instance / transfer nodes.

Step 7: Review network - discuss the structure of the network with experts to ensure that there are no missing factors.

Step 8: Obtain data - seek information for each node from sources including experts, academic papers, reports, industry articles, and data bases.

Step 9: Construct probability tables - express the data through marginal and conditional probability tables for the nodes.

Step 10: Test model integrity - use Hugin to compile the model and test for conflicts in data by inserting random evidence.

Step 11: Calibrate probabilities - compare prior probabilities of certain nodes with real world statistics, to determine if the model is representative of reality.

# 3.2 Model structure 

The BN model is made up of three sequentially linked parts, with each part representing a different phase of a single occupancy dwelling fire. The individual networks can function as standalone models or collectively as a larger BN in which the outputs are expressed through part III nodes, including two utility nodes. Building the model in such a way, not only facilitates its management and presentation, but also enables different stages of a dwelling fire to be examined individually; this partitioned approach should also assist any future developments. Part I of the model is designed to represent the "Initial fire development", part II "Occupant response and further fire development", and part III the "Advanced fire situation and consequences". There is a chronological order to the model with part I feeding into part II, which subsequently feeds into part III.

There are a total of sixty seven chance nodes distributed throughout the three parts of the network. Data is assigned to a parentless chance node or root node via a marginal probability table and to a non-root node via a Conditional Probability Table (CPT). In the model, root nodes typically represent variables which form part of the existing circumstances of a fire while nonroot nodes represent the events and actions which take place. Figure 2 summarizes the contents of the model parts and demonstrates how they link together. Instance nodes are used to link the model together and appear in each of the relevant parts. Nodes are laid-out and connected in a top-down fashion so that variables which intervene later on in a fire, appear towards the bottom of the networks. An account of part three of the model, including discussion of relevant assumptions, now follows. Parts one and two are also introduced, but for a full explanation, Matellini et al. (2013a and 2013b) should be consulted.

![img-1.jpeg](img-1.jpeg)

Figure 2. Schematic diagram of the three-part BN model with main events for each part.

# 3.2.1 Part I of the model - initial fire development 

Part I of the BN model is designed to represent the initial fire development through fourteen discrete chance nodes grouped into "initial circumstances", "fire cues", "human detection", and "human reaction" (Matellini et al., 2013a). The latter of these is considered the focus of part I and includes only a single node, "Human reaction". Figure 3 presents part I of the BN model. There are four instance nodes linking part I with part II and III of the model; these nodes are shaded grey around the edges in Figure 3. Part II is connected to part I via the instance nodes

"Fire start type", "Time of day", "Human reaction", and "Sprinkler activated", while part III to part I via the latter of these. A description of each of these nodes can be found in Matellini et al. (2013a).
![img-2.jpeg](img-2.jpeg)

Figure 3. BN model Part I representing initial fire development. Nodes are grouped into: i) Initial circumstances; ii) Fire cues; iii) Human detection; iv) Human reaction

# 3.2.2 Part II of the model - occupant response and further fire development 

Part II of the BN model deals with occupant response and further fire development through thirty four discrete chance nodes; four additional instance nodes from part I also feature. There are three primary functions to this network. Firstly, it is designed to model the effects of human actions, specifically those of an occupant, a passerby, and a FRS as a unit, through nodes such as 999 call, escape, seeking shelter, firefighting, and passerby intervention. Secondly, the growth of the fire can be investigated based on parameters associated with fuel combustion,

occupant actions, firefighting devices, and FRS intervention. Finally, the effect of the fire development itself and the surroundings (e.g. floor level, fuel toxicity, etc.) upon evacuation, rescue and survival can be examined.

Figure 4 presents part II of the BN model with nodes arranged where possible in chronological order from top to bottom. The focus of this part of the investigation is fire development and occupant survival, assessed through the nodes "Fire growth/flashover" and "State of the occupant FS 1\&2". Fire Stage (FS) 1 and 2 indicate the stage that the fire is at. In FS1 the fire is contained to the room of origin and covers up to $50 \%$ of the room; in FS2 the fire covers over $50 \%$ of the room, but may have also spread to another room.
![img-3.jpeg](img-3.jpeg)

Figure 4. BN Model Part II representing occupant response and further fire development.

Five of the thirty four discrete chance nodes are time-based variables meaning they may be more suitably represented through a continuous chance node. This however, has not been done because there are some limitations regarding the use of such nodes within the Hugin software. The main limitations are that a continuous node cannot be a parent of a discrete node and that they cannot be included in a network containing utility or decision nodes; note that part III of the model contains two utility nodes. Consequently these five nodes have been modelled using discrete chance nodes, in which their individual states represent particular time intervals. The nodes in question are "999 call", "MACC dispatch / call processing time", "Preparation + travel time appliance 1", "Response time appliance 1" and "Appliance 1 at scene". A description of each of these nodes can be found in Matellini et al. (2013b).

# 3.2.3 Part III of the model - advanced fire situation and consequences 

The third part of the BN model addresses the advanced fire situation in a dwelling. Once linked with parts I and II, a complete analysis of a dwelling fire from start to end is possible.

The network contains seventeen discrete chance nodes and two utility nodes which serve to measure the results in monetary terms; there are in addition one and eight instance nodes from parts I and II of the model respectively. The network incorporates parameters representing the spread of fire and containment measures such as fire doors and intervention of FRS'. Arrival time of FRS' is again represented, but on this occasion for fire appliances which arrive in support of the first appliance. As with part II of the model, part III features some time-based nodes which are modelled through discrete rather than continuous nodes. Links with part II of the model allow for the time of arrival of appliance 1 to be assessed. Fire escalation into other dwellings and firefighting complications are also represented. Although it is extremely unlikely for a firefighter to die, with 122 on-duty fatalities registered between 1978 and 2008 (Fire Brigades Union, 2008), the matter is of very high importance and therefore has been included

in the network. This parameter, along with a node representing the state of the occupant, feeds into a utility node "Human cost $£$ ".

Figure 5 presents part III of the network structured so that events flow from top to bottom where possible; utility nodes (diamond boxes) are located towards the right of the network. Similar themed nodes have been kept in proximity to each other. The instance nodes are located at the top of the network, with those from part II towards the left and part I towards the right.
![img-4.jpeg](img-4.jpeg)

Figure 5. BN Model Part III representing advanced fire situation and consequences.

Fires which are extinguished in part II would render this part of the model meaningless except for the utility nodes used to quantify potential losses. There are several aspects of the advanced fire situation which can be examined with part III of the model, namely:

- The impact of FRS response time and intervention of both the first appliance and additional support.
- The influence of the setting in terms of the dwelling characteristics.
- The development of fire based on interaction with various parameters.
- The effect of fire development upon the wellbeing of the occupant and firefighters.
- The effect of fire development upon the dwelling structure.
- The impact on life and assets in terms of economic value.

The focus of this part of the model is human wellbeing and property damage assessed through the nodes "State of the occupant FS 3", "State of firefighter", "Human cost $£$ ", and "Property damage $£$ ". These are briefly discussed, along with a selection of the other nodes, to help explain how part III of the model functions:

- Fire doors present and shut [state: Yes, No] - This root node embodies two factors, the first is the presence of self-closing fire doors within a dwelling, the second is the condition that they are shut during the fire. When completely shut, fire doors are effective at containing fires and smoke within a compartment for a given period of time.
- Fire spread to other compartments [states: Yes, No] - This chance node describes the spread of fire from the room of origin to any other room within the dwelling, including those on other floors.
- Structural failure / collapse [states: Yes, No] - This chance node describes the potential for structural failure and collapse of part or all of the dwelling. This includes sections of roofs

caving in, ceiling buckling, walls collapsing, or even an entire dwelling crumbling to the ground.

- Second rescue attempt required [states: Yes, No] - This chance node represents a person remaining trapped following an unsuccessful first rescue attempt during fire stages 1 and 2, hence a second rescue attempt is required. The purpose of this node is to reduce the size of the CPT of the node "Rescue successful FS3" by acting as an intermediate node between "State of the occupant FS 1\&2" and "Rescue successful FS 3".
- Firefighting complications [states: Yes, No] - This chance node describes the situation of firefighting becoming highly complicated and challenging; this does not imply that dwelling firefighting is straightforward, but rather accentuates situations in which fires grow to the extent that the structure of the dwelling is affected or the dwelling boundaries are exceeded; essentially the node seeks to represent circumstances in which a contained dwelling fire turns into a precarious potential multiple-dwelling fire. The purpose of the node is to model scenarios which adversely affect rescue attempts and endanger firefighter's lives by entrapment.
- Rescue successful FS 3 [states: Yes, No] - This chance node represents the event of the occupant being rescued successfully while the fire is still ongoing. The term "successful" refers to the extraction of the occupant while alive, hence an unsuccessful rescue means that the occupant has lost his/her life. Once extracted their actual state of health is captured in a subsequent node "State of occupant FS 3". Note that FS 3 refers to an advanced or final phase of a fire situation, in which the fire size could vary from small to large depending on factors such as how effective firefighting measures had been. A fire is considered large if it has spread from the room of origin into other compartments or even an adjoining building.

- State of the occupant FS 3 [states: Alive - well/minor injury, Alive - major injury, Dead] - This chance node describes the living status of the dwelling occupant at the more advanced fire stage.
- Firefighter rescue required [states: Yes, No] - This chance node indicates that one or more firefighters have become trapped and that their safety is compromised, thus rescue is required.
- State of firefighter [states: Alive - well/minor injury, Alive - major injury, Dead] - This chance node describes the living status of the trapped firefighter following an attempted rescue.

The two utility nodes within the network, present the losses from fire in economic terms. Essentially, this provides a measure of risk to which experts can relate. The results can then be used to conduct cost-benefit analysis to compare risk reduction ideas. In this model, both utility nodes are discrete. To our knowledge, the software which was used did not allow for a continuous utility node to be constructed. This however did not present a problem given the way the utility tables had been set up. This point is discussed further within the "Property damage $£$ " node below. In terms of the validity of the results from the utility nodes, these were reviewed with experts who deemed them fitting with 'real world' values for an average dwelling. The two utility nodes are detailed below:

- Property damage $£$ - This utility node quantifies the consequence of property damage in $£$. Data has been compiled based on information provided by the Land Registry (Land Registry, 2012). For cases when there is structural collapse, demolition costs have been factored into the values. The discrete utilities have been compiled based on the parent nodes i) "Fire growth / flashover" (part II), ii) "Fire spread to other compartments", iii) "Structural collapse", and iv) "Fire spread to other dwellings". In the utility node table, the cost of damage from each input is overridden by the subsequent 'more damaging' input; for

example, if ii) "Fire spread to other compartments" occurs, then the damage from this is considered greater than i) "Fire growth / flashover", hence the damage value for the former is adopted in the utility node.

- Human cost $£$ - This utility node quantifies economically the consequences of casualties in terms of loss of life, alive with major injury, and alive well/minor injuries. The values used are $£ 1.5$ million and $£ 155,000$ for the first two possibilities, derived as explained in section 2.1; $£ 100$ has been used for well/minor injuries. The utilities have been compiled based on the parent nodes "State of firefighter" and "State of the occupant FS 3". Table 1 has been provided as an example of what the data looks like for one of these utility nodes.

Table I. Utility node table for 'Human cost £'


# 3.3 Data for the model 

### 3.3.1 Construction of CPTs

Directly applicable data did not exist for the construction of CPTs for nodes with many parents. To address this issue, expert opinion was sought and combined with various discerning sources of information (DCLG, 2011b; Stevens, 2008; Yung, 2008; Holt et al., 2004; Mattsson and Juas, 1997; Fire Brigades Union, 2008; DCLG, 2012a; DCLG, 2013). For cases when hard data was limited or could not be directly applied due to it being dated or representative of unrelated geographical regions, expert judgement was used to tailor it to the current study.

A useful approach which reduces the amount of expert elicitation in the construction of CPTs was proposed by Fenton, Neil, and Caballero (2007). The method "is based on the doubly truncated Normal distribution with a central tendency that is invariably a type of weighted function of the parent nodes". The approach is used to develop CTPs of commonly occurring nodes called 'ranked' nodes; a commercial software has been developed to this end. Although the tool is undoubtedly useful to BN users, it was not used in this work.

A number of assumptions had to be made when constructing some of the more complex CPTs. An example of the type of assumptions made within the model is provided below for the node 'Fire spread to other compartments'; note that these assumptions were discussed with experts to ensure their validity:

- If fire was extinguished there could not be fire spread.
- For FRS response: During conditions of fire growth / flashover, if no sprinkler is activated and a fire door is present and shut, each 5 minute delay of appliance 1 increases the probability of fire spread to another compartment by $20 \%$, while each 5 minute delay of additional support by $3 \%$. If fire doors are not shut the probabilities increase by $50 \%$ with the delay of appliance 1 and $20 \%$ with delay of additional support. If fire growth / flashover does not occur the probabilities of fire spread are virtually none existent.
- If sprinklers are activated all probabilities are divided by 10 based upon expert opinion stating that sprinklers are effective on circa $90 \%$ of occasions.
- The arrival of additional support cannot occur before appliance 1 which is reflected in the probabilities.

# 3.3.2 Inspection of prior probabilities 

Prior probabilities of nodes generating results (for example "State of the occupant FS 3") and those with complex CPTs, were compared against statistics in order to calibrate the model and provide partial validation. It is reasonable to expect and accept some minor differences between the values, however if differences were larger than $5 \%$, the relevant section of the network was reviewed. Once calibrated, a final comparison with statistics was carried out to ensure the nodes were representative of reality. It is important to stress at this stage that the numerical results of the model are not significant in an absolute sense, but rather serve to demonstrate its practicality. The following provides an overview of some of the nodes which were inspected; note that probabilities are expressed out of 100 as presented in Hugin:

- Fire extinguished: Prior probabilities were [Yes: 19.30, No: 80.70]. These values were discussed with experts at MFRS who agreed that fire was probably extinguished by an occupant on $20 \%$ of occasions.
- Fire spread to other compartments: Prior probabilities were [Yes: 9.58, No: 90.42]. These values were compared with UK fire spread statistics from Stollard and Abrahams (1999) which show that fire spread beyond the room of origin on $9 \%$ of occasions. These values were very close to the each other and more than acceptable for the model. Note that although the statistics are around 15 years old they are still valid today since the dynamics of fire in dwellings would change little over such a period.
- State of the occupant FS 3: Prior probabilities were [Alive - well / minor injury: 87.10, Alive - major injury: 12.18, Dead: 0.72]. Data was not found with which to compare these values; however annual statistics from DCLG (2002, 2008, 2010, 2011a, 2012b) on the number of dwelling fires and dwelling fire fatalities for the UK was obtained. From these two data sets it is possible to work out the probability of a fatality at a dwelling fire. This

has been computed between the years 1996 and 2010 giving a range between 0.63 and 0.78 with an average of 0.70 and a median of 0.69 . The prior probability of "State of the occupant FS 3" is 0.72 for fatality which is reasonably close to the UK values derived from DCLG. The difference may be explained by the model being representative of Merseyside rather than the UK; furthermore it is known that Merseyside has a higher fatality rate than most of the rest of the country (DCLG, 2011a) which would account for the higher prior probability for fatality.

- Utility node Human cost £: Prior utility [29,975]. This economic measure of the consequences of fire in terms of human life was compared to data derived from the latest set of figures on the economic cost of fire corresponding to the year 2008 for England (DCLG, 2011b), in combination with the number of dwelling fires in England between 2008 and 2010 (DCLG, 2011a). The figure for comparison was obtained as follows:

Total cost of fatal and non-fatal casualties $=£ 1.402 \times 10^{9}$

Percentage of fatalities corresponding to dwelling fires $=79 \%$

Cost of casualties from dwelling fires $=1.402 \times 10^{9} \times 0.79=£ 1.106 \times 10^{9}$

Average number of primary fires 2008 to $2010=99,000$

Percentage of dwelling fires $=38 \%$

Number of dwelling fires $=99,000 \times 0.38=37,017$

Cost of Human casualties per fire $=1.106 \times 10^{9} / 37,017=£ 29,921$

Data on the cost of fire in terms of human life was only available as a combined value for fatalities and injuries. The value provided by the model was just $£ 54$ higher than the value derived from statistics.

- Utility node Property damage £: Prior utility [28,206]. The economic measure of fire in terms of property damage, was compared with a value derived from data from the same two sources from DCLG (2011a and 2011b) as above. The value was computed as follows:

Total cost of property damage from primary fires $=£ 1.490 \times 10^{9}$

Number of building fires $=54,162$

Cost of building damage per fire $=1.490 \times 10^{9} / 54,162=£ 27,584$

The model value compares well with statistics. The difference can be attributed to the latter being inclusive of all building types including premises such as outdoor storage, garages, etc., whilst the model is built for dwellings only.

Table 2 provides a summary of the nodes which were compared with statistics. Columns 4 and 5 contain the statistic source and value; column 6 provides the difference between the model prior probability or economic value and the relevant statistic.

Table II. Summary of nodes that were checked for consistency of prior probabilities and economic values with 'real world' statistics (note probabilities are expressed out of 100).


[^0]
[^0]:    * References for this data are provided in the text within section 3.3.2.

# 3.4 Partial model validation 

The model was partially validated using the approaches outlined below:
a) D-separation: during the construction of the model, d-separation tests were conducted using Hugin to demonstrate that there were no redundant nodes in the network. The tests confirmed that all nodes in the network did have a function.
b) Expert review: the rational of the network was discussed, at various stages, with fire and rescue service experts, to ensure the model represented the reality of dwelling fire safety and the associated circumstances.
c) Sensitivity analysis: these tests demonstrate how responsive a given node is to changes in values of other nodes. The results provide a degree of confidence that the model is working as intended. For this study, the effect upon 'State of the occupant fire stage 3' was examined, as this was one of the main outputs for the entire model. The node was most sensitive to 'Fire spread to other compartments'.

## 4 RESULTS

The BN model can be used to investigate a variety of issues associated with fire safety at a given location. Two case studies are presented in this paper, to demonstrate how the integrated model parts can be used and what type of outputs can be generated. In each case, evidence is inserted into a selection of nodes and posterior probabilities generated for the rest of the nodes.

### 4.1 Case 1 - Smoke alarm effect upon the probability of fatality and the human cost of fire

With the three model parts integrated, the influence of parameters at the initial stage of the fire can be used to measure those at an advanced stage; importantly, the effect of these parameters can now be measured in economic terms.

This case demonstrates how the model can be used for undertaking a simple cost-benefit analysis. The probability of fatality (Figure 6 left y-axis, bars) during a dwelling fire has been plotted together with the human cost in $£$ (Figure 6 right y-axis, points) as a function of the type of smoke alarm installed in the dwelling; note that the human cost quantifies injuries as well as fatalities. It is evident that not having a smoke alarm results in a higher probability of fatality and human cost, a fact already known. However, the model can now be used to assess if it would be worthwhile investing in installing a particular type of smoke alarm with a 10year battery within dwellings in England, that do not have any type of alarm. The calculation for the combined type of smoke alarm is as follows:

# BENEFIT 

Human cost difference between no alarm and combined alarm per fire from model

$$
=37,128-27,326=£ 9,802
$$

Number of dwelling fires (mean 2008-2010) $=37,017$

Number of dwelling fires in which a smoke alarm was not present (approximately 20\% of dwellings do not have smoke alarms (DCLG, 2008)).

$$
=37,017 \times 0.2=7,403
$$

Human cost difference between no alarm and combined alarm for all fires per year (i.e. the benefit should all dwellings have combined smoke alarm)

$$
=9,802 \times 7,403=£ 72,568,127
$$

## COST

Number of dwellings in England $=22,200,000$

Number of dwellings in England without a smoke alarm

$$
=22,200,000 \times 0.2=4,440,000
$$

Combined smoke alarm retail cost $=£ 13.14$ (Amazon, June 2012)

Combined smoke alarm cost to FRS $=£ 7.88$ (assuming $40 \%$ discount)

Installation cost per alarm $=£ 12$

Cost of combined smoke alarm installed $=7.88+12=£ 19.88$

Cost of installing in all dwellings $=4,440,000 \times 19.88=£ 88,267,200$

# COST-BENEFIT 

It would cost $£ 88,267,200$ to install combined smoke alarms with 10-year batteries in all dwellings in England that do not have any smoke alarm, and the benefit would be a reduction of risk in terms of human life of $£ 72,568,127$ per annum. During the first year the cost would exceed the benefit but over the ten year period which the alarms are meant to last, the benefit would exceed the cost by far. Assuming however that the alarms only last 5 years because of tampering, society would still be better off by approximately: $£ 363 \mathrm{~m}$ ( 5 year benefit) - $£ 88 \mathrm{~m}$ $(\operatorname{cost})=£ 275 \mathrm{~m}$.

The above calculation has been repeated for all types of smoke alarms with the result provided in Table 3. Each smoke alarm has a different impact upon risk and hence benefit due to their varying response times as a function of the type of fire. The cost of all the alarms has been obtained from the online retailer Amazon on the same day, for 10-year alarms, and for the same brand of alarm. A $40 \%$ reduction has been applied in costing to FRS' based on expert opinion. However, prices can only be taken as very approximate since market conditions constantly vary. The calculations are only for demonstration of how the model results can be used to assist a cost-benefit exercise. In Table 3 the best option alarm would be combined, with optical and ionisation in second and third place respectively. The combined alarm, capable of detecting

both flaming and smouldering fires quickly, is best for reducing risk, but its higher cost would only make it the first choice if installed for at least 5 years.
![img-5.jpeg](img-5.jpeg)

Figure 6. Probability of death and human cost of fire as a function of type of smoke alarm installed in dwelling.

Table III. Cost-benefit to society of installing smoke alarms in all dwellings in England.


This hypothetical argument for the installation of smoke alarms would also need to consider other factors besides cost and benefit. For instance, according to several firefighters interviewed between 2010 and 2012, some people do not like having a smoke alarm around and have in the past refused firefighters from entering their homes to install free alarms. People are also known to misuse the alarms, for example by painting over them, or even taking the battery out to use elsewhere. These issues would affect the benefit that is theoretically displayed in Table 3, leading to a requirement for further modelling of human behaviour with regards to the acceptance of smoke alarms.

# 4.2 Case 2 - Multiple circumstances effect upon probability of fatality and human cost $£$ (parts I to III) 

The second case study presents a selection of nine common dwelling fire circumstances. Their effects upon the chance of survival of the occupant, the cost of consequences in terms of people and damage to property, are examined. The conditions considered are:

- The presence of any type of smoke alarm
- No smoke alarm
- Any smoke alarm plus a sprinkler system
- No smoke alarm, no sprinkler, and nighttime
- No smoke alarm, no sprinkler, nighttime, occupant asleep, fire door shut
- Any smoke alarm, no sprinkler, nighttime, occupant asleep, fire door open
- No smoke alarm, no sprinkler, nighttime, occupant asleep, fire door open
- No smoke alarm, no sprinkler, nighttime, occupant asleep, fire door shut, occupant not fully mobile
- No smoke alarm, no sprinkler, nighttime, occupant asleep, fire door shut, occupant not fully mobile, fire not extinguished between fire stage 1 and 2

- Materials without fire retardant properties, fire doors open

Results are presented in Figure 7 with probability of fatality shown by bars (measured against the left y-axis) and cost of consequences by markers (measured against the right y-axis). One of the most typical dwelling fire circumstances occurs in homes with any type of smoke alarm installed, no sprinklers system, a nighttime situation with the occupant asleep, and fire doors left open. In such situations the probability of fatality is $0.98 \%$. An equal common circumstance is as before, except that there would not be a smoke alarm present, in which case the probability of fatality rises to $1.56 \%$; the human cost is $£ 49,985$. People who are not fully mobile are also at a higher risk, as shown by the third and second to right bars in Figure 7. In such situations the probability of fatality rises to $1.71 \%$ and $2.06 \%$ (human cost $£ 54,589$ and $£ 64,311$ ) irrespective of whether the fire is extinguished at an early stage. In any case it is unlikely that a person with limited mobility would attempt to extinguish a fire. For these reasons, homes with such individuals should be highlighted as highly vulnerable and additional contingency measures established, such as an automatic alarm system linked to a fire security officer or MACC. The various other results provided in Figure 7 are given to demonstrate the array of circumstances that can be investigated with the model. These can be combined further with response times, human actions, geographic location, and various other characteristics if desired.

![img-6.jpeg](img-6.jpeg)

Figure 7. Cost of dwelling fire consequences based upon a variety of common dwelling fire circumstances.

# 5 CONCLUSION 

Fires in society result in many tragic deaths and have huge economic implications in terms of human losses, property damage, insurance claims and so forth. Data indicates that the total number of fires in the UK is dropping year-on-year; however the key to reducing overall risk from fires lies in dealing with dwelling fires. The complexities of handling the interaction of the multitude of factors that affect the risk from fire, mean that fire safety assessment and planning often involve high levels of uncertainty. To address these matters, this paper presents

a three-part BN, to model the different stages of a generic dwelling fire from its onset through to extinguishment.

# 5.1 Practical applications of the research and future work 

The BN model can be used to assess the risk within similar groups of dwellings / neighbourhoods to assist FRS' plan risk-based operations. There are ongoing changes to the set-up of FRS's throughout the UK, primarily driven by budget cuts. If FRS's are to operate with reduced capacity, they must seek to improve even further the effectiveness of their operations. The research presented in this paper can contribute towards this feat. To the best of our knowledge, a BN has not previously been developed and applied for dwelling fire emergency response planning. Unlike other approaches, this BN model allows uncertainty to be captured in a way that can be easily understood by people involved in decision making within the fire safety discipline. It can be used for both planning and post-fire investigation purposes. Probabilities can be determined for human reaction, fire growth, occupant survival, property damage, among other events of interest. The third part of the model also provides utility nodes so as to be able assess the impact of fire economically. Future work on this model could include the addition of decision nodes.

Two case studies have been conducted to demonstrate how the BN can be used in practice. The first case study examines the effect upon probability of fatality and the economic cost of consequences in terms of people. The results are used to demonstrate how a simple cost-benefit analysis could be undertaken, in support of a nationwide installation of 10-year smoke alarms, highlighting which type of alarm would be the most cost-effective option. The second case study, presents a series of common fire scenarios in dwellings, with the purpose of comparing the effect upon the probability of fatality and human cost. The dangers of nighttime fires without smoke alarms were highlighted, as well as open fire doors for an occupant with limited

mobility. Future studies and experimentation are of course necessary to examine the extent of using such a model in the 'real' world.

# ACKNOWLEDGEMENTS 

This research was funded by the UK Engineering and Physical Sciences Research Council (EPSRC) under grant reference EP/F041993/1, and a Leverhulme Research Fellowship under reference RF/7/RFG/2010/0019. Gratitude would also like to be extended to the Knowledge and Information Management team (KIM) and the Mobilising and Communication Centre at Merseyside Fire and Rescue Authority (MFRA) for their assistance in data and information gathering. Finally the authors would like to acknowledge John Fay and John Kellaway from MFRA for their useful contributions to fire and rescue knowledge.

## DISCLAIMER

This paper is the personal opinion of the authors and does not represent the policy of MFRA.
