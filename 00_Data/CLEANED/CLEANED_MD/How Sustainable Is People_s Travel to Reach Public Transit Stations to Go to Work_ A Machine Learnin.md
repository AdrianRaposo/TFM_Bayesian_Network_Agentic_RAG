# Article 

## How Sustainable Is People's Travel to Reach Public Transit Stations to Go to Work? A Machine Learning Approach to Reveal Complex Relationships

Panyu Tang ${ }^{1, *}$, Mahdi Aghaabbasi ${ }^{2, * *}$ (D), Mujahid Ali ${ }^{3, * *}$ (D), Amin Jan ${ }^{4, * *}$ (D), Abdeliazim Mustafa Mohamed ${ }^{5,6}$ (D) and Abdullah Mohamed ${ }^{7}$


#### Abstract

check for updates Citation: Tang, P.; Aghaabbasi, M.; Ali, M.; Jan, A.; Mohamed, A.M.; Mohamed, A. How Sustainable Is People's Travel to Reach Public Transit Stations to Go to Work? A Machine Learning Approach to Reveal Complex Relationships. Sustainability 2022, 14, 3989. https://doi.org/10.3390/ su14073989


Academic Editor: Aoife Ahern
Received: 25 February 2022
Accepted: 25 March 2022
Published: 28 March 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 ChengDu Jincheng College, Chengdu 611731, China
2 Centre for Sustainable Urban Planning and Real Estate (SUPRE), Department of Urban and Regional Planning, Faculty of Built Environment, University of Malaya, Kuala Lumpur 50603, Wilayah Persekutuan Kuala Lumpur, Malaysia
3 Department of Civil and Environmental Engineering, Universiti Teknologi Petronas, Seri Iskandar 32610, Perak, Malaysia
4 Faculty of Hospitality, Tourism and Wellness, Universiti Malaysia Kelantan, City Campus, Kota Bharu 16100, Kelantan, Malaysia
5 Department of Civil Engineering, College of Engineering, Prince Sattam Bin Abdulaziz University, Alkharj 16273, Saudi Arabia; a.bilal@psau.edu.sa
6 Building \& Construction Technology Department, Bayan College of Science and Technology, Khartoum 210, Sudan
7 Research Centre, Future University in Egypt, New Cairo 11745, Egypt; mohamed.a@fue.edu.eg

* Correspondence: tangmi127@126.com (P.T.); mahdi@um.edu.my (M.A.); mujahid_19001704@utp.edu.my (M.A.); aminjan@umk.edu.my (A.J.)

Abstract: Several previous studies examined the variables of public-transit-related walking and privately owned vehicles (POVs) to go to work. However, most studies neglect the possible nonlinear relationships between these variables and other potential variables. Using the 2017 U.S. National Household Travel Survey, we employ the Bayesian Network algorithm to evaluate the non-linear and interaction impacts of health condition attributes, work trip attributes, work attributes, and individual and household attributes on walking and privately owned vehicles to reach public transit stations to go to work in California. The authors found that the trip time to public transit stations is the most important factor in individuals' walking decision to reach public transit stations. Additionally, it was found that this factor was mediated by population density. For the POV model, the population density was identified as the most important factor and was mediated by travel time to work. These findings suggest that encouraging individuals to walk to public transit stations to go to work in California may be accomplished by adopting planning practices that support dense urban growth and, as a result, reduce trip times to transit stations.

Keywords: sustainable travel to public transit stations; complex relationship; Bayesian network algorithm; work trip

## 1. Introduction

A transition away from privately owned vehicles (POVs) toward active transport can have major health advantages [1]. Despite the vast benefits of active transport modes, particularly walking, many individuals still prefer POVs. For example, just $36 \%$ of all journeys in the United States were below one mile, and only $27 \%$ of such journeys were conducted by walking or biking [2]. According to statistics from the American Community Survey, the percentage of people who walk to work in the United States has declined from 5.6 per cent in 1980 to 2.8 per cent in 2012 [3].

The "park and ride" concept, which promotes the use of POVs to reach public transit (PT) stations and combines the use of private cars and PT stations to reduce the negative

consequences of private vehicle use, has been the subject of several studies in the past [4-7]. Typically, this system is found at rail transportation terminals and transportation hubs, which allow for both rail and public bus access. However, this system may not be available at local bus stops. POVs are feasible options to reach PT stations where the stations are not within walking distance or in low-density areas [8,9]. Although there is hope that this approach will reduce the negative consequences of private vehicle use (e.g., traffic congestion, pollution, and physical inactivity), it is more desirable for planners to minimize the role of POVs in people's daily travels, particularly those related to work.

PT stations may supplement and extend the variety of active modes significantly [10,11]. Because of this, as well as the fact that POVs are associated with a slew of other well-known issues, there may be room for a modal shift away from POVs toward walking and PT that might reduce the usage of POVs, while also contributing to increased physical activity [12-15]. Because health conditions, work trip qualities, work attributes, and sociodemographic factors may all impact travel patterns [16-21], it is important to know how walking connects to PT travel to work to reap the most advantages.

California has always had a problem with traffic congestion. The cause for this ongoing issue is that the region's population and POV usage have exceeded the transportation facilities. If California's transportation system cannot keep pace with the state's fast urban growth, and if Californians' priority for POVs continues, the traffic problem will undoubtedly worsen soon. To deal with long-term urban traffic issues, dwellers in crowded regions are encouraged to replace POVs with active transportation options and PT, especially for work-related journeys. When people combine walking with PT, which is a hot topic among planners, the advantages of this replacement may be maximized. Walking is the most cost-effective mode of transportation and the most basic form of physical activity [22-25]. Walking also needs a low-cost infrastructure. As a result, it makes sense if planners encourage individuals to walk to PT stations over other active forms of transportation.

Many studies have been conducted on the topic of first-mile connection, which addresses how people reach PT stations. Several studies assessed the impact of sociodemographic characteristics on walking to reach PT stations. Factors, such as age [17,18,26-28], gender [29,30], vehicle ownership [31,32], income [33-35], and education [32,36,37], were significantly correlated with the walking to reach PT stations. Although there are a lot of built environment (BE) factors that impact travel behavior, only a very small number of these factors were included in the first-mile connection studies. These factors included density and distance to PT stations [38-42]. Earlier studies have shown that population density is one of the most significant BE variables, and its impact on travel behavior is stronger than other BE attributes [32,36,43,44]. People in low-density areas are more likely to use POVs than those in medium- and high-density areas [45,46]. Similarly, for individuals who live in low-density regions where the station is too far away to walk to and bus service is not accessible, driving to PT stations may be the sole choice for reaching PT stations [8].

While sociodemographic variables have been well covered in earlier studies, healthrelated factors and their impact on mode choice have rarely been considered in most PT-related walking investigations [1,47,48]. BMI, self-assessed health, self-reported smoker, and yearly frequency of hospital and primary care visits are characteristics addressed in these studies. To the best of the authors' knowledge, no study considered the impact of medical conditions in PT-related walking research. Furthermore, most of these studies neglected job-related issues, as well as those associated with work trips. Flexibility in work arrival time, full-time/part-time worker, the possibility of working from home, the distance between home and work location, trip time to work, time spent transferring on the commute to work if PT is taken, and travel time to PT station are some of the aspects that are overlooked [49-51]. The existence of such data in the U.S. National Household Travel Survey can give an excellent chance to look at the influence of a medical condition and work-related trips on travel mode selection.

There are non-linear and complex interactions between variables in transportation systems (e.g., the relationship between the built environment and car ownership) that


are difficult to study using typical statistical approaches and linear programing methods [52,53,54,55,56,57,58]. Non-linear relationships may be inconsistent, and factors may have threshold correlations with a variable of interest. Because non-linear relationships can help planners to understand the effective influence range of important factors on the target variable, it is interesting to see if this result can be applied to other fields [59]. This supports planners in fine-tuning their strategies [60]. Most PT-related walking studies employed traditional statistical methods (Table 1). However, these methods are unable to reveal complex relationships. In addition, these models have strict linearity assumptions, which limits the ability of these models to be effectively generalized [61,62,63,64,65,66]. Finally, these models are vulnerable to missing and incomplete data. Machine learning (ML) approaches can be used to solve the problems outlined before [67,68,69,70]. The Bayesian Network (BN) model is one of these powerful tools, and it has lately been used successfully in various transport-related research [67,71,72,73,74,75]. A BN model can effectively deal with heterogeneous and under-sampling data, as well as missing, erroneous, or ambiguous data. Because it can effectively alter its network depending on the data provided or entered into it, BN is indeed thought to be excellent for learning changeable behaviors (e.g., mode choice) [76,77,78,79,80,81].

Table 1. Some recent studies on PT-related walking.

LRM = logistic regression model; PDF = probability density function; $\mathrm{CDF}=$ cumulative distribution function; $\mathrm{DE}=$ Descriptive analysis.

The authors of this research utilize the BN model to explore the major indicators of travel mode to reach PT stations and highlight their non-linear interactions using the 2017 U.S. National Household Travel Survey (2017 NHTS). The following are the questions that this research aims to answer: (1) How important are the health condition, work trip, work, and individual and household attributes to individuals who use walking or POV to reach PT stations to go to work in California? (2) Do the most important variables have associations with walking or POV to reach PT stations to go to work?

This paper contributes to the literature in three major ways. To begin with, it adds to the research of mode choice for reaching PT stations to go to work in California and other regions where traffic congestion is a problem. Furthermore, this study evaluates the relative relevance of several elements in walking to work and gives insight into the policy implementation priorities in California and other places with similar conditions. It also demonstrates that important factors have irregularly complex relationships, corroborating the scant data in the literature and providing recommendations for California planning approaches. Finally, this study demonstrates the significant role of trip time to work and its combined effect with population density in POV usage to reach PT stations to go to work, as well as the significant role of population density and its interaction impacts with trip time to PT stations in walking reach PT stations to go to work, thereby bolstering the case for dense urban development.

The following is a breakdown of how the research is structured. The data, variables, and modeling technique are introduced in Section 2. Section 3 discusses the models' results and performance, variable importance, relationships with travel mode to reach PT stations in California, and interaction impacts on mode choice to reach PT stations. The final section highlights the most important findings and explains policy implications.

# 2. Materials and Methods 

In this study, two associative and predictive BN models were developed to reveal the complex relationships between various variables and PT-related walking and PTrelated POVs in California. As previously mentioned, the 2017 U.S. National Household Travel Survey (2017 NHTS) was employed to conduct this study. These models discover interaction effects of independent factors on the usage of walking and POVs to reach PT stations to go to work and assess the relevance of variables in predicting the choice of walking and POV to reach PT stations to go to work. Figure 1 shows the flowchart of this study.
![img-0.jpeg](img-0.jpeg)

Figure 1. This study's flowchart.

### 2.1. Data

This study used data from the 2017 U.S. National Household Travel Survey (2017 NHTS). The NHTS has now become the country's rich source of information on commuting by U.S. citizens throughout all fifty states. This commute behavior database contains journeys taken in a variety of ways and for a variety of reasons. The data for the NHTS are gathered from a randomly selected sample of U.S. households. The NHTS supplies data about individual and household travel behavior patterns. These patterns are related to sociodemographic and geographic factors that impact travel choices and are used to estimate demand. More information can be found at https://nhts.ornl.gov (accessed on 1 January 2020).

This study looked into how Californians utilize walking and privately owned vehicles (POVs) to reach public transportation to go to work. Thus, the study team mined the whole

dataset for relevant data. Public transport in this study refers to public or commuter buses, subways, elevated and light rail, and Amtrak. The following criteria were used to choose the samples: (1) residence in California, (2) the use of public transportation to commute to work, and (3) the use of walking and POVs to reach public transportation to go to work. A total of 796 samples were used to create the final dataset. A total of 19 input variables and 2 target variables were included in the dataset (walk to reach public transit stations and POVs to reach public transit stations). Table 2 lists all of the variables utilized in this investigation.

Table 2. Variables employed in this study.


Table 2. Cont.


In the NHTS dataset, several active modes, including bikes and e-scooters, and passive modes, such as ride-sourcing, are not considered to reach PT stations. This can be regarded as a drawback of the NHTS dataset and a limitation of this study. Furthermore, although the literature suggests that the most critical BE factors for examining the first mile connection to PT stations are population density and distance to the PT station, the NHTS only considers population density. As a result, the only BE input in this investigation was population density, whose direct and significant impacts on travel behavior and mode choice for PT have been widely proven.

# 2.2. Bayesian Network (BN) Model 

Bayesian Networks (BNs), commonly referred to as belief networks, are probabilistic network models that combine probability and graph theory. The following are the main two methods for acquiring BN structures. The first method is based on expert judgment and uses subjective causal links to construct a BN structure. The second method, known as structural learning, uses certain learning models to detect and guide the edges on a given dataset. By using the latter method, this investigation creates the BN architecture. There are numerous data-driven techniques, including Nave Bayesian Networks (NBN), Augmented Naive Bayesian Networks (ABN), and Tree Augmented Networks (TAN). TAN learning generates qualitative BN-depicting variables' interacting dependencies, which aids in generating insights into the crucial elements that influence travel mode choice. Friedman et al. [92] have noted that TAN beats naive Bayes, while retaining the calculation efficiency and stability that naive Bayes is known for. Other data-driven configuration algorithms are less effective and reliable than TAN [93]. In this research, the analysis was performed using SPSS Modeller, which is worth noting.

A BN that is a labelled directed acyclic graph (DAG) represents a joint probability distribution over a collection of random inputs $Q$. Let $Q=\left\{B_{1}, \ldots B_{i}, D\right\}$, where $i$ refers to the number of inputs, the inputs $A_{1}, \ldots A_{i}$ are the variables, and $D$ signifies the class variable (mode to public transit station).

Assume a network structure in which the target variable serves as the root, namely $\prod D=\varnothing$, and every variable possesses the target variable as its sole parent, namely $\prod B_{j}=\{D\}$ for $1 \leq j \leq i$. Equation (1) characterizes a BN as a single joint probability distribution across $Q$.

$$
P\left(B_{1}, \ldots B_{i}, D\right) \cdot \prod_{j=1}^{i} P\left(B_{j}>|D|\right.
$$

When $\prod B_{j}$ has just one parent for any and all $B_{j}$ apart from one variable-lacking parent, the DAG over $\left\{B_{1}, \ldots A_{i}\right\}$ is a tree. When there is only one $j$ so that $\pi(j)=0$, and therefore there is no series $j_{1}, \ldots j_{s}$ so that $\pi(j h)=j_{h+1}$ given $j \leq h \leq s$ and $\pi\left(j_{s}\right)=i_{1}$, there is indeed a function $\pi$ that can describe a tree across $B_{1}, \ldots B_{i}$. Such a function

describes a tree network where $\prod B_{j}=\left\{D, \ldots B_{\pi(j)}\right\}$ if $\pi(i)>0$, and $\prod B_{j}=\{D\}$ if $\pi(j)=0$.

It is an optimization challenge to learn a TAN structure. Chow and Liu [94], who employed conditional mutual information between characteristics, offered a broad technique for solving this problem. The following is a definition of the function:

$$
I M\left(B_{j}, B_{h} \mid D\right)=\sum_{b_{j j}, b_{h j}, d_{j}} P\left(b_{j j}, b_{h j}, d_{j}\right) \log \frac{P\left(b_{j j}, b_{h j} \mid d_{j}\right)}{P\left(b_{j j} \mid d_{j}\right) P\left(b_{h j} \mid d_{j}\right)}
$$

where $I M$ denotes the conditional mutual information, $b_{j j}$ is the $j$ th state of variable $B_{j}, b_{h j}$ is the $j$ th state of variable $B_{h}, d_{j}$ is the $j$ th state of "mode choice to transit station". The optimization challenge of learning a TAN structure is to develop a tree characterizing function across $B_{1}, \ldots B_{i}$ that maximises the log-likelihood.

# 3. Results 

### 3.1. Models' Results and Performance

Two Bayesian Network (BN) models were developed in this study to predict the choice of walking and POVs to reach PT stations among Californians. To develop these models, the structure type of the BN models was the TAN algorithm and the parameter learning method was Bayes adjustment. It is worth mentioning that the data were split into train and test partitions with a ratio of 80:20 before the models' development. The training partition was used to build the models, whereas the test partition was utilized to evaluate the created model using unseen data. The BN models were used to (1) determine the importance of variables in predicting the choice of walking and POVs to reach PT stations, (2) determine relationships with travel mode to reach PT stations in California, and (3) identify the interaction effects of independent variables on the use of walking and POVs to reach PT stations. The structures of the BN models developed in this study are shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. BNs' structure: associations between the travel modes to reach public transport and their most important variables and mediators as identified by the BN model. (a) BN model for walking to reach public transit station; (b) BN model for POV to reach public transit station.

The performance of the two BN models is shown in Table 3. Both models achieved a high accuracy in both the training and testing phases. In addition, the accuracies of the training and testing phases are almost similar, which implies the stability of both models. The models' performance also was assessed using receiver operating characteristic (ROC) diagrams (Figure 3). The ROC curve depicts the sensitivity-specificity trade-off. Models with curves nearer to the top-left corner perform much better. A random model is expected to yield diagonal points (sensitivity = specificity) as a reference point. The nearer the curve is to the ROC space's 45 degree diagonal, the less accurate the test becomes. As can be seen, both models indicated a great performance for both classes (yes and no).

Table 3. Models' performance.


![img-2.jpeg](img-2.jpeg)

Figure 3. Receiver operating characteristic graphs for the BN models developed in this study.

# 3.2. Variable Importance 

Table 4 shows the significance of all independent variables in forecasting travel mode to reach public transit stations. In addition, the cumulative impact of four types of factors is shown in Table 5. For walking, the results showed that work trip attributes (WTA)


dominated the prediction of mode choice to reach PT stations in California. For POV, individual and household attributes (IHA) largely influenced the forecast of mode choice to use PT. Especially, the predictive power of all the WTAs was 0.58 . The combined contribution of IHA variables was 0.33 for POVs.

Table 4. Importance of the various types of variables.

Table 5. Cumulative importance of factors.


In terms of the WTAs' impact on choosing the walking mode to reach PT stations, the trip time to the transit station (TRACCTM) was the most important variable in predicting walking choice to the PT station. Previous research has found a negative association between distance to transit stations and nonmotorized travel behavior [95-97]. As a result, it was expected that the time spent traveling to the transit station would emerge as the most relevant factor in predicting the likelihood of walking to the transit station. Individuals who walk to reach PT stations to go to work may place a different value on their time.

People's gender, income, family responsibilities, and other factors can all contribute to this difference [98]. As a result of these distinctions, different levels of sensitivity to walking time to PT stations may emerge.

In California, the population density (HBPPOPDN) has a 0.12 predictive power for POV usage to reach PT stations. The transport mode to the transit station is heavily influenced by population density [99]. In high-density areas, active transportation modalities are commonly used to reach transit stops. On the other hand, cars are the most prevalent form of transportation to transit stations in low-density areas.

# 3.3. Relationships with Travel Mode to Reach Public Transit Stations in California 

In this section, the non-linear associations of the most important variable of walking and POVs to reach PT stations and the prediction of occurrence of these travel modes are discussed. It is vital to determine these complex relationships since it helps to identify the relevant impact ranges of these factors. According to the results of the BN models, the most important factor for predicting walking adoption to reach PT stations was the trip time to the transit station (TRACCTM), while the population density of participants' house location (HBPPOPDN) was chosen as the most important predictor of POV adoption to reach PT stations.

Figure 4 displays the relationships mentioned above. When the average time to reach PT stations is around 10 min , Californians are more inclined to walk to the transit stations. If the typical commute duration to PT stations is around 40 min , Californians are less likely to walk to PT stations. This study's results are consistent with Sun and Yin [100] findings, which revealed that shorter travel times and shorter distances to PT stations might increase the likelihood of walking to them.
![img-3.jpeg](img-3.jpeg)

Figure 4. Non-linear relationship between the most important variable in each model and prediction of the travel mode choice to reach public transit stations. (a) Prediction of the walking choice to get to public transit; (b) prediction of the POV choice to get to public transit.

If the participants' dwelling is in a densely populated area (e.g., 7000-30,000 persons per square mile), it is unlikely that they will utilize a POV. In contrast, if the dwelling units are in a low-density region (e.g., 750 persons per square mile), POV is more likely

to be used. These findings corroborate those of Nigro, Bertolini and Moccia [99], which found that population density influences the mode of transportation used to access PT stations. Combining the results of the time to the transit station (for the walking model) and population density (for the POV model), when the time to the transit station is less than 10 min or the population density in the household's home location is 7000-30,000 persons per square mile, walking to reach PT stations could be increased by densifying land use around PT stations.

# 3.4. Interaction Impacts on Mode Choice to Reach Public Transit Stationsr 

The strong negative connections between travel time to transit stations and walking to each PT stations suggest that, if the trip duration to transit stations can be reduced, walking will become more popular. The BN model revealed that another variable, population density (HBPPOPDN), mediates the effect of trip time to reach public transit stations (TRACCTM) on walking to PT stations (Figure 5a). Figure 5a illustrates the combined influence of these two variables on forecasting walking to reach PT stations in California. Walking is more probable when the trip time to the PT stations is less than 10 min . These lower trip times to transit stations occur in high density areas (e.g., 7000-30,000 persons per square mile). This means that the TRACCTM's negative relationship with the walking level to the transit station is amplified by HBPPOPDN. The influence of trip time to transit stations on walking to PT stations is mediated more by a population density of 17,000 persons per square mile than by other HBPPOPDN values.
![img-4.jpeg](img-4.jpeg)

Figure 5. Associations between key variables and travel mode choice to reach public transit stations mediated by various variables. (a) The combined influence of population density and trip time to reach public transit stations on forecasting walking to reach PT stations; (b) The combined influence of population density and trip time to work on forecasting usage of POV to reach PT stations.

The substantial negative correlations between participants' housing population density and their usage of POVs to reach PT stations show that if people reside in high-density

areas with integrated public transportation, they will be discouraged from using POVs. Another variable, trip time to work (TIMETOWK), was found to mediate the impact of population density (HBPPOPDN) on using POVs to reach PT stations in the BN model (Figure 5b). The joint impact of these two variables on predicting POV usage to reach PT stations in California is shown in Figure 4b. In high-density locations, using POVs to reach PT stations is less likely (e.g., 7000-30,000 persons per square mile). When the commute time to work is between 42 and 57 min , lower trips using POVs occur. This suggests that TIMETOWK strengthens the HBPPOPDN's negative association with POV usage to reach the transport stations. It is worth noticing that a 57 min commute to work has a greater mediation effect than other TIMETOWK values on the effect of population density on not utilizing POVs to reach PT stations.

# 4. Discussions 

The time it takes to walk to PT stops or stations is the most essential factor in people's choice to walk. Furthermore, it was shown that population density acted as a mediator for this effect. The POV model revealed population density as the most relevant component, which was mediated by the commute time to work. The findings are crucial because they show that planners should concentrate on population density, public transportation, and job locations when contemplating the replacement of POVs with walking to commute to PT stations for work. However, it is critical that the BN's outcomes are unaffected by the following variables: the health condition attributes, the individual and household attributes, the work trip attributes (excluding the trip time to work and trip time to PT stations), and the work attributes. Previous studies have deemed these factors relevant [17,29,31-33,36,47]. However, this research suggests that they may not be necessary to take into consideration. In terms of health condition attributes, a very limited number of studies show that this factor is essential in travel mode choice [1,47,48]. Additionally, this study did not find a substantial effect of these factors on mode choice for PT stations. This may be due to the fact that health conditions may have a greater impact on leisure walking in California than on work-related walking.

As mentioned above, population density emerged as the most important factor of POV usage to reach PT stations and a mediator of the effects of travel time to PT stations on walking to PT stations. This finding reflects the importance of this factor in studying of travel mode choice to PT stations. Several previous studies also stressed the relevance of this factor on travel mode choice [38,39]. Furthermore, according to Nigro, Bertolini and Moccia [99], population density has a significant impact on the mode of transportation to the nearest PT facility.

The density of the population is seen as a crucial component in the success of a PT operation [101]. Population density, particularly for pedestrians, is commonly cited as a factor that encourages more people to use PT. However, research has shown inconsistent outcomes. Higher densities tend to have a more compact land use and closer destinations, which makes walking more possible and beneficial. However, although some research suggests that short-distance walking to reach PT stations is dependent on density, wealth and other societal variables are progressively taking precedence after populational density reaches a certain level [102,103].

## 5. Conclusions and Recommendations

This study employed a Bayesian Network model to examine the relative importance of health condition, work trip, work, and individual and household attributes in trip mode choice to transit stations to go to work and their complex relationships with travel mode choice to transit stations to go to work in California, using data from 2017 NHTS. It is among the first to investigate how population density in California mediates the effects of time to transit stations on walking to transit stations to go to work and how time to go to work mediates the influences of population density on POV usage to reach PT stations to go to work. The findings provide positive consequences regarding densifying population

and land uses around transit stations for walking level growth to reach public transport stations in developed countries' cities, especially car-oriented ones.

The outcomes indicate that work trip attributes play a dominant role in walking to reach PT stations in California. People that have a short trip time to transit stations to go to work are more likely to walk to PT stations. This variable is the most important predictor in the walking model, contributing to more than 0.40 of the predictive power. With a decrease in the trip time to transit stations in California, the walking level for first-mile connections to reach the workplace is expected to grow faster. The determination of efficacious approaches to accelerate growth is key to sustainable transportation in California.

The factors that affect PT-related walking are similar to those that impact urban walking in general, especially in terms of built environment features [104,105]. The appealing aspects of PT, as well as the PT services offered and the transportation options available to individuals, influence how far someone is willing to walk to reach public transportation.

Land use and transportation strategies can be utilized by planners to change the built environment. The setting wherein PT-related walking takes place is defined by nonmodifiable characteristics (e.g., alternative travel alternatives, culture, purpose, physical ability, and the weather). However, urban or transportation planning experts can employ changeable influences (such as density, land use, infrastructure quality, and trip length) to impact the distances people would walk to PT stations to reach the workplace.

Planners should consider promoting high-density development because this has a strong effect on PT-related walking lengths. This development makes the origins and endpoints much closer and increases the transit stations density. These may reduce the distance that individuals must walk to transit stations. Density has also been connected to enhanced walkability, which can attract more walkers by raising the proportion of people who walk to reach transit stations or broadening the catchment area around a transit station.

Typically, people prefer to walk to transit stations through more walkable routes [106]. The higher level of walkability and, in turn, shorter PT-related walking can be achieved through a higher level of street connectivity and lower-level detours [17,18,87,89]. In addition, the tolerable walking travel time of pedestrians to transit stations can be increased if the walkability at the micro-level is improved [107]. Street elements, such as lighting, seating areas, trees, and width of sidewalk, may increase the distances people are willing to walk $[22,108,109]$.

Along with these built-environment solutions, various car-restrictive policies could assist to reduce the use of POVs for general use and reaching transit stations. These regulations can be implemented particularly well in high-density areas, as low-density areas may lack enough PT and walking infrastructures. As a result, the only way to reach transit stations is by using a POV.

This study has a few limitations that deserve comment. First, this study utilized the 2017 NHTS dataset, which does not consider biking, micro-mobility, and ride-sourcing exclusively as modes to reach PT stations. Thus, future studies can apply the BN algorithm considering these modes and using different datasets. Second, the NHTS includes a few variables of the built environment. Hence, it is recommended that future studies develop BN models using more comprehensive datasets. Finally, this study was conducted in a car-oriented setting. Thus, people who use walking to reach public transit stations were underrepresented. Therefore, the outcomes of this study should be transferred cautiously to other cities, especially European ones.

Author Contributions: Conceptualization, M.A. (Mahdi Aghaabbasi), M.A. (Mujahid Ali) and P.T.; methodology, M.A. (Mahdi Aghaabbasi), M.A. (Mujahid Ali) and P.T.; software, M.A. (Mahdi Aghaabbasi) and M.A. (Mujahid Ali); formal analysis, M.A. (Mahdi Aghaabbasi) and M.A. (Mujahid Ali); investigation, M.A. (Mahdi Aghaabbasi) and M.A. (Mujahid Ali); writing—original draft preparation, M.A. (Mahdi Aghaabbasi) and M.A. (Mujahid Ali); funding acquisition, A.J., A.M.M. and A.M. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Acknowledgments: The center of scientific and technological innovation and new economy institute of Chengdu-Chongqing economic zone (No: CYCX202011) and Research center for Sichuan Province into the dual-cycle new development pattern (No: CDNUSXH2021ZC-01).

Conflicts of Interest: The authors declare no conflict of interest.
