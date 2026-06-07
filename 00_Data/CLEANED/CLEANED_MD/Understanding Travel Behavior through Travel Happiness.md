# TUDelft 

Delft University of Technology

## Understanding Travel Behavior through Travel Happiness

Mantouka, Eleni G.; Vlahogianni, Eleni I.; Papacharalampous, Alexandros E.; Heydenrijk-Ottens, Léonie; Shelat, Sanmay; Degeler, Viktoriya; van Lint, Hans

DOI
10.1177/0361198119836761

Publication date
2019
Document Version
Final published version
Published in
Transportation Research Record

## Citation (APA)

Mantouka, E. G., Vlahogianni, E. I., Papacharalampous, A. E., Heydenrijk-Ottens, L., Shelat, S., Degeler, V., \& van Lint, H. (2019). Understanding Travel Behavior through Travel Happiness. Transportation Research Record, 2673(4), 889-897. https://doi.org/10.1177/0361198119836761

## Important note

To cite this publication, please use the final published version (if applicable).
Please check the document version above.

## Copyright

Other than for strictly personal use, it is not permitted to download, forward or distribute the text or part of it, without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license such as Creative Commons.

## Takedown policy

Please contact us and provide details if you believe this document breaches copyrights.
We will remove access to the work immediately and investigate your claim.

# Green Open Access added to TU Delft Institutional Repository 

'You share, we take care!' - Taverne project
https://www.openaccess.nl/en/you-share-we-take-care

Otherwise as indicated in the copyright section: the publisher is the copyright holder of this work and the author uses the Dutch legislation to make this work public.

# Understanding Travel Behavior through Travel Happiness 

Eleni G. Mantouka ${ }^{1}$, Eleni I. Vlahogianni ${ }^{1}$, Alexandros E. Papacharalampous ${ }^{2}$, Léonie Heydenrijk-Ottens ${ }^{3}$, Sanmay Shelat ${ }^{3}$, Viktoriya Degeler ${ }^{3}$, and Hans van Lint ${ }^{3}$


#### Abstract

The aim of this paper is to extend past research on travel behavior analysis by investigating travelers' emotions and perceptions of the system's performance. Perceived travel happiness as an extension of travel satisfaction is researched in the framework of the decision-making process during traveling. Socio-demographic, cognitive, and affective data were collected from a questionnaire survey that took place in Athens (Greece), the Netherlands, and Barcelona and Salamanca (Spain). A Bayesian network was developed to investigate the interrelations between travel happiness and parameters that affect travel behavior. Findings revealed that travel mode choice directly affects the level of happiness that a person experiences during everyday trips. Moreover, travel happiness is directly associated with the traveler's perception of the occurrence of disruptions during everyday trips and the level of tolerance he/she has toward such disruptions. Results also indicated that further research should focus on understanding how the topology and performance of each country's system affect travel-related choices. Finally, a discussion of the most significant results is provided.


The recent technological and communication advances in the transport landscape with the plethora of travel mode alternatives offered to travelers' for their everyday trips result in a highly complex travel decision-making process that should be understood and modeled to make sensible predictions with regard to the effects of interventions in transport systems (1). Previous research that has analyzed how travel-related choices are made has usually been based on the concept of a utility function that encapsulates the trade-offs travelers consider when making decisions. The factors in such utility functions may be predetermined for each individual (e.g., car ownership, driver license possession, location of work), or refer to each traveler's characteristics (e.g., gender, age, occupation, income) and emotions (e.g., anxiety, the perception of crowdedness). Moreover, trip-related attributes, such as cost and travel time, are also included in such functions. Subsequently, the sign and significance (or lack thereof) of these factors are derived from observed choices (decision utility) (2), either in a simulated environment (stated preferences surveys, travel simulators) (3) or from travel diaries (4).

Over the last decades, researchers have shown that experienced utility (i.e., the utility in hindsight) may differ from decision utility, because of travelers' emotions and feelings during traveling $(5,6)$. To this end, researchers
have turned to investigate travelers' emotions and perceptions on the trip as well by introducing the notion of travel satisfaction. According to (7-9), satisfaction with travel consists of two dimensions: one affective (emotional), which refers to emotions experienced during a trip, and one cognitive (reasoned) dimension, which refers to the evaluation of the trip. Moreover, travelers' satisfaction can be seen as a measure of the extent to which a service matches their expectations (10). A significant portion of the research has addressed the cognitive dimension of travel satisfaction (11, 12). In (13), researchers emphasize measuring both the cognitive and the affective component of travel satisfaction or well-being, taking into consideration different emotions: whether or not the traveler feels bored, fed up, stressed, calm, enthusiastic, or confident during the trip. Several studies (14-16) have examined the level of stress experienced during commuting trips. There is evidence that many other aspects of travel behavior,

[^0]
[^0]:    ${ }^{1}$ Department of Transportation Planning and Engineering, School of Civil Engineering, National Technical University of Athens, Athens, Greece
    ${ }^{2}$ AETHON Engineering Consultants P.C., Athens, Greece
    ${ }^{3}$ Department Transport \& Planning, Faculty Civil Engineering \& Geosciences, Delft University of Technology, Delft, the Netherlands

rather than just travel mode, are associated with travel satisfaction. These may include trip duration and invehicle activities $(17,18)$. Furthermore, other studies show that travel choices are more likely to be motivated by the goal of enhancing happiness rather than by the traditionally studied concept of reducing travel cost $(19,20)$. As highlighted by some researchers, travelers' attitudes and emotions are more important when planning to travel than objective travel quantities (costs, travel times, etc.) (21). In (22), a five-level scale, the so-called satisfaction with travel scale, is proposed to examine whether or not emotional reasons affect travel choices. Results indicated that different activities (trip purpose) result in different levels of satisfaction with travel. Some researchers have investigated travelers' satisfaction with different travel modes (17), whereas others have focused on public transport systems (23). It turns out that the use of specific modes is among the strongest differentiators in the level of travel satisfaction (24, 25). Furthermore, travelers' satisfaction is found to influence travel choices mainly for short distance and urban trips (26). Although these findings clearly point toward the relevance of the affective dimension in travel choice behavior, there is still a limited body of knowledge that conceptualizes and quantifies the role of this affective dimension. The gap of knowledge that arises from the literature concerns the importance of affective factors in the decision-making process of everyday traveling and the relationship between them and other cognitive factors. Another interesting question is whether or not the perception of the traveler with regard to the transport system and the trip affects his/her travel decisions.

The scope of this paper is to investigate the existence of interrelationships between traditionally examined user- and system-related factors that may affect travel behavior and affective factors under the umbrella concept of Travel Happiness. The difference between this study and the more well-known notion of travel satisfaction is that with regard to travel happiness in this paper we aim to combine decision utility with: (a) the satisfaction from the level of service; and (b) two factors that express a user's perception of the various aspects of his/ her trip. This perception is described through two variables. The first one is the probability that a traveler assigns to the occurrence of a disruption or other unexpected event during his/her trip. The second one is the level of tolerance that the traveler has toward the occurrence of such unexpected events. The investigation of factors that affect travel behavior and the interrelations between various factors and travel happiness is performed through the analysis of data collected from a questionnaire survey using Bayesian networks.

The remainder of the paper is organized as follows. First, the methodological approach of the study is briefly discussed and the questionnaire used for the survey is presented. Then, the most meaningful statistics of the sample are analyzed and findings based on the Bayesian network structures are presented in detail. Finally, the most significant conclusions and suggestions for further research are presented.

## Travel Behavior and Happiness

## A Brief Definition of Travel Happiness

Following research on the emotional aspects of travel choices, the concept of travel happiness has been gradually introduced as a broader term that includes travel satisfaction, placing emphasis on the "generalized" emotions travelers experience during trips (19, 27).

First, we briefly place travel happiness in a broader context. Travel happiness can be considered as an attribute in the continuum of decision-making in life (including mobility and transport), which may be perceived from two intertwined temporal dimensions. The first one is the medium-term dimension, which aggregates the feelings of users about their overall mobility patterns. The second is the short-term dimension, which encapsulates the dynamically changing sense of happiness (constituted by affective factors during travel), which may, of course, vary in relation to the trip conditions (Figure 1). This long-term aspect of travel happiness is linked to life satisfaction, which, in this paper, is considered to relate to travel happiness as an external mood affected by a generalized perception of a traveler's life conditions. Life satisfaction measures how people evaluate their life as a whole, rather than their current feelings. Life satisfaction includes subjective data and personal evaluation of a person's health, education, income, personal fulfillment, and social conditions. Based on the OECD report (28), the Greeks rate their life satisfaction as equal to 5.2 ., way below the average of OECD countries, which is 6.5 . The Dutch rate their life satisfaction as equal to 7.4 and Spanish people as equal to 6.4 .

The short-term aspect of travel happiness is related to general, macroscopically forming travel choices that are related to strategic factors and the well-being of a person, as well as users' perceptions of the services and system operation, and the specifications of the transport system. In some studies, happiness is used as a proxy for the notion of well-being as it is considered to be the main subjective indicator of social system performance (25). The link between happiness and travel behavior has not been thoroughly studied. Nonetheless, there is a small body of literature, including (29), that has investigated how trip attributes are associated with traveler's emotions. This provides some evidence that travel happiness correlates with travel mode choice decisions, although

![img-0.jpeg](img-0.jpeg)

Figure I. Travel happiness in the continuum of decision-making in life.

Morris et al. also suspect potential links with other travel choices (6).

One of the challenges is that travel happiness, or any other variable that describes a person's feelings and emotions, is challenging to measure, especially in the case of travel behavior analysis (30). To this end, we assume that travel happiness can be measured on a five-point Likert scale, which is a common and generally accepted way of measuring opinions, perceptions, and behaviors. As noted, the concept of travel happiness has not yet been systematically quantified and assessed with regard to the factors that may influence it. As far as is known, the connection between travel behavior and happiness from a perspective of combining travel mode choice, trip purpose, users' perceptions of the trip in the context of personal demographics, and mobility profiles has not been extensively researched. In this paper we present an attempt to do so. A powerful tool for exploring the relationship between these factors is a Bayesian network, which allows us to estimate the conditional probabilities between these factors in a structured way.

## Bayesian Networks

Bayesian networks (BNs) are graphical representations for encoding the conditional probabilistic relationships among variables of interest. The nodes of the graph represent variables and the arcs between variables represent causal, influential, or correlated relationships. A BN for a set of variables consists of two parts. The qualitative part is a network structure $G$ in the form of a directed acyclic graph (DAG), in which nodes are in a one-to-one mapping with the random variables $X$ and links characterize the dependence among connected variables. The quantitative part is a set of local probability distributions/tables $\Theta=\left\{P\left(X_{i} \mid \Pi_{1}\right), \ldots, P\left(X_{n} \Pi_{n}\right)\right\}$ for each node/ variable $X_{i}$, conditional on its parents $\Pi_{i}$. These conditional probability tables demonstrate the probability of $X_{i}$ with respect to each combination of its parent variables. In a $\mathrm{BN}, X_{j}$ is referred to as a parent of $X_{i}$ if a direct link exists from $X_{j}$ to $X_{i} . \Pi_{i}$ is used to denote the set of parent variables of $X_{i}$. If a variable has no parents, the local probability distribution collapses to its marginal $P(X)$.

In a BN model, $G$ is the model structure and $\Theta$ holds the model parameters. The DAG topology of a BN only asserts the conditional dependence of children given parents. Therefore, by integrating structure $G$ and parameter $\Theta$, and by using the chain rule, the joint distribution for $X$ in a BN can be decomposed into a factorized form with smaller and local probability distributions, each of which involves one node and its parents only:

$$
P(X)=\prod_{i=1}^{n} P\left(X_{i} x_{\Pi(i)}\right)
$$

In other words, the joint probability distribution $P(X)$ can be exclusively encoded by the pair $(G, \Theta)(31)$. For discrete random variables, this conditional probability is often represented by a table, listing the local probability that a child node takes on each of the feasible values for each combination of values of its parents. The joint distribution of a collection of variables can be determined uniquely by these local conditional probability tables (CPT), also referred to as parameters tables. Let the $n\left(x_{i}, x_{\Pi(i)}\right)$ be the number of observations in which the variable $X_{i}$ has adopted the values $x_{i}$ and its parents $\Pi_{i}$ the values $x_{\Pi(i)}$. The standard estimate for a parameter $P\left(X_{i} x_{\Pi(i)}\right)$ is (32):

$$
P\left(X_{i} \mid x_{\Pi(i)}\right)=\frac{n\left(x_{i}, x_{\Pi(i)}\right)}{n\left(x_{\Pi(i)}\right)}
$$

The structure of and the relationships in BNs can rely on both expert knowledge and relevant statistical data, meaning that they are well suited for enhanced decisionmaking (33). There are three methods for structuring learning for a BN:

1. Constraint-based algorithms: These algorithms use conditional independences and dependences induced from the data to detect the Markov blankets of the variables to recover the structure of a BN, for example, PC, max-min parents and children and Grow-Shrink.
2. Score-based algorithms: These algorithms aim at maximizing a scoring function (log-likelihood, AIC, BIC, e logarithm of the Bayesian Dirichlet equivalent score, etc.) by means of a heuristic search strategy (search and score), such as hill climbing and tabu search. A scoring function used

Table 1. Description of the Parts of the Questionnaire


in structural learning in BNs is typically scoreequivalent.
3. Hybrid algorithms: These algorithms combine constraints with search and score. The most common hybrid algorithm is the max-min hill climbing, which starts with the constraint-based stage to develop the skeleton and then carries out a search and score-based strategy using the skeleton obtained as the candidate edge set (34).

In this paper, the tabu search algorithm is implemented for the development of the BN. This is a score-based algorithm moving from one solution to its neighboring solution while trying to maximize log-likelihood. This algorithm was selected because it results in a DAG as opposed to hybrid algorithms and the structure of the graph is learned directly from the data.

Conditional independence (CI) tests are functions of the CPT implied by the graphical structure of the network through the observed frequencies for the random variables $\boldsymbol{X}$ and $\boldsymbol{Y}$ and all the configurations of the conditioning variables $\boldsymbol{Z}$. The CI test used in this case was mutual information, an information-theoretic distance measure defined as follows:

$$
M I(X, Y \mid Z)=\sum_{i=1}^{R} \sum_{j=1}^{C} \sum_{k=1}^{I} \frac{n_{i j k}}{n} \log \frac{n_{i j k} n++k}{n_{i+k} n+j k}
$$

It is proportional to the log-likelihood ratio test (they differ by a $2 n$ factor, where $n$ is the sample size), and it is related to the deviance of the tested models (35).

With regard to the evaluation of the trained models, the most common way to obtain unbiased estimates of the goodness of fit of a Bayesian structure is the k -fold cross-validation technique (36). The goodness of fit of the true network (the one emerged from the tabu algorithm) is compared with the performance of an empty and a random network.

In this project, structure learning was data driven and performed by using the bnlearn package (37) of the R language (38).

## Data Collection

Data used for the analysis were collected through a questionnaire survey that took place in three European countries: Greece, the Netherlands and Spain. The questionnaire consists of four parts and 27 questions and is aimed at investigating factors that affect travel mode choice and identifying different mobility profiles as well as respondents' perceptions of the system they use. A comprehensive description of the content of each part is provided in Table 1.

In the first part of the questionnaire, respondents are asked about their usual trip, namely, for what purpose and what mode of transport they use every day. This part also includes questions about the number of trips per trip purpose, number of transfers on the usual trip, work time flexibility, and public transport pass possession. Furthermore, respondents are asked about their attitude toward mobility as a service (MaaS), namely, whether or not they use or would be willing to use any MaaS service (taxi, Uber, car sharing, or car pooling). Respondents are asked to determine the level of happiness they experience during their usual trip using a fivepoint scale, on which 1 represents very unhappy and 5 very happy. Then, respondents are asked about their tolerance with regard to changes of network and service conditions (e.g., traffic congestion, road accident, strike, etc.). Again, respondents answer using a five-point scale, on which 1 represents not tolerant and 5 represents very tolerant. Finally, respondents are asked to state their estimation with regard to the possibility of the occurrence of any unexpected event, such as road closure and vehicle damage, during their usual trip using a five-point scale ( 1 represents not possible and 5 represents certain).

In the second part of the questionnaire, respondents are asked about the importance of various factors in their choice of their usual travel mode. The importance of each factor is described on a five-point scale from 1 (not important) to 5 (extremely important). Factors that are examined are: cost, travel time, reliability, cleanliness and comfort, flexibility, availability, safety, security, real-

Table 2. Sample Size per Country


time information provision, in-vehicle activities, accessibility, weather conditions, and parking availability. In the third part of the questionnaire, respondents are asked to assess the travel mode they use the most according to the same attributes on a five-point scale from low to high. Finally, in the last part of the questionnaire, demographic characteristics (gender, age, income, car ownership, etc.) of the sample are identified.

## Survey Execution and Sample Size

The questionnaire survey had a total duration of 10 weeks and was conducted both online and on site. In the case of the Netherlands, the survey was conducted solely online and lasted for 2 weeks. In Greece and Spain, the online platform was open for more than a month (January to February 2018), whereas the on-site survey had a total duration of 10 weeks. The on-site survey was carried out in metro stations and bus stations, which had connections with other modes of transport, as well as in activity/leisure centers. Places where people were waiting were specially chosen because this meant they could use some of the time they had to kill in filling in the questionnaire.

The final sample size included a total number of 2,199 valid responses and is representative of each country's population. The sample size per country, as well as the corresponding number of original responses, are presented in Table 2.

## Analysis of Responses

The sample of the three countries is well distributed according to gender, age, and income distribution. As shown in Table 3, the Greek sample includes younger people, with just $4 \%$ being older than 65 . On the contrary, both the Dutch and Spanish samples have a welldistributed sample according to age. The Dutch sample had the largest group of unemployed and retired people and, therefore, it is not surprising that the number of respondents with a high income level was the smallest. Moreover, income distribution for the Spanish sample is almost equally spread, although it would be expected that this would show a more left-skewed distribution as was shown by the Greek population.

Table 3. Demographic Characteristics of the Sample


The sample includes different modes of transport that are divided into three categories: private vehicles (car and motorcycle), public transport, and soft modes (cycling and walking). The majority ( $47 \%$ ) of people in all countries undertake their everyday trips by car, followed by metro ( $24 \%$ ) in Greece, train ( $20 \%$ ) in the Netherlands, and bus ( $16 \%$ ) in Spain. A further statistical analysis of the sample indicated that Dutch travelers prefer to use either car or bicycle when traveling for leisure. Moreover, they prefer to walk only when they undertake trips for personal reasons, such as shopping and family visits. In the Greek sample, most trips for educational purposes (to and from school, college, university) are undertaken by public transport, and especially by metro and bus. On the contrary, Spanish students either travel by bus or walk to their place of study.

From the preliminary analysis of the responses, it is shown that Dutch travelers are, in general, happier during their everyday trips when compared with Greek travelers who appear to be the least happy among the three samples. In all three samples, travelers who usually use soft modes of transport for their everyday trips are happier when compared with regular public transport users.

Figure 2 depicts the distribution of the level of tolerance with respect to changes in the transport network's conditions. Figure 3 shows the distribution of the respondents' perceptions of the probability of the occurrence of any unexpected event during everyday trips. With regard to expecting disruptions during a trip, the Dutch respondents appear to be the most optimistic and the Greek ones the most apprehensive. Furthermore, in Greece, roads are heavily congested, especially during peak hour, and frequent strikes negatively affect public transport services. This can explain the low tolerance level of the Greek population. The Dutch respondents showed

![img-1.jpeg](img-1.jpeg)

Figure 2. Distribution of the level of tolerance with respect to changes in the transport network's conditions.


Figure 3. Distribution of the respondents' perceptions of the probability of the occurrence of any unexpected event during everyday trips.
higher tolerance for disruptions to the transport network. Interestingly, in Spain, the level of tolerance of the travelers seems to follow a normal distribution. Concerning the travelers' perceptions of the possibility of the occurrence of disruptions to the network, half of the Spanish and Dutch respondents consider it as not that possible ( $50 \%-52 \%$, respectively). More specifically, $27 \%$ of the Dutch respondents assigned zero probability, in contrast to only $10 \%$ of the Spanish respondents. On the other hand, $44 \%$ of the Greek respondents considered it as more than slightly possible.

## Results

This section provides the results of the Bayesian network developed to assess the associations between travel mode choice and users' characteristics and feelings, as well as their perceptions of everyday trips. The Bayesian network that emerged from the analysis is depicted in Figure 4. The relationships between variables are depicted by arcs that provide two measures: (a) the strength of the association, which takes values from 0 (weak association) to 1 (strong association); and (b) the probability of the arc's direction depicting a causal relationship, which ranges from 0.5 (the direction is uncertain) to 1 (the direction depicted is the only possible one), written in brackets. It is very common for arc directions to change between different learning algorithms as a result of score equivalence.

The nodes in the graph represent user-related characteristics (age, gender, income, number of cars, work time flexibility, and home location), trip-related characteristics (trip purpose, cost, and travel mode), and affective factors (travel happiness, possibility of the occurrence of any unexpected event, and level of tolerance). The relationships among factors are represented by arcs. The log-likelihood ratio of the network was estimated as -28080.21 and the expected loss estimated after 10 -fold cross-validation was 12.88. Goodness of fit of this network (true network) was compared with an empty and a random graph. The expected loss ratio for the empty and random graph is 13.64 and 13.55 , respectively, higher than the trained model, which means that the trained model fits the data better than the null and random model.

Based on the structure of the Bayesian network depicted in Figure 4 as well as the CPTs that emerge from the analysis, some significant results are presented. Findings revealed significant interrelations among demographics of the users. More specifically, the age and gender of the users stand as predictors of their total annual personal income. Furthermore, a user's age appears to be strongly associated with the intention to use MaaS. It is observed that the elderly ( $>55$ years old) are more likely to use a taxi as an alternative mode of transport for their everyday trips, whereas the younger travelers ( $<34$ years old) may choose between a variety of services such as car pooling, car sharing, or Uber. This is reasonable, because younger people are more familiar with new services and technology in contrast with the elderly who prefer to use traditional and well-known services.

Moreover, age and income stand as predictors of the trip purpose. The age and income of the traveler may reflect his/her occupation and, therefore, determine the usual purpose of everyday trips. A traveler's income also stands as a predictor of the number of cars that a person owns, with those travelers who have a higher income being more likely to have more than one car. Knowing the number of cars that a person owns or has access to together with their trip purpose makes it possible to predict travel mode. Although people who own a car are more likely to use it for every trip purpose, students who have access to or own a car will most likely not use it when traveling to and from their place of study.

In addition, income and travel mode are strongly associated with the travel cost of everyday trips. Moreover, travel cost may be used as a predictor of a traveler's

![img-2.jpeg](img-2.jpeg)

Figure 4. Trained Bayesian network for travel happiness and mode choice.
home location. More specifically, people living in urban areas are more likely to spend less money on their everyday trips compared with those living in rural or suburban areas.

Furthermore, the trip purpose together with a traveler's income may provide an insight into his/her work time flexibility. It appears that people with a high income are more likely to have flexible working hours.

Consequently, all trip-related and user-related predetermined factors are used for travel mode choice decisions. The Markov blanket of travel happiness, namely, the subset of the network including travel happiness parents, its children, and parents of its children (39), is identified by a green rectangle on the BN below. It is observed that travel mode choice is the only variable that directly affects the level of travel happiness experienced during everyday trips. Moreover, travel happiness is strongly related with factors describing the user's perception of the system they use the most, namely, tolerance
![img-3.jpeg](img-3.jpeg)

Figure 5. Interrelations among country and the Markov blanket of travel happiness.
and the probability of the occurrence of an unexpected event.

A further investigation into how each country's specific characteristics may affect travel happiness was conducted by developing a supplementary Bayesian network, which is depicted in Figure 5. This BN was developed based on the Markov blanket of travel happiness node as it emerged from the first analysis. With regard to the evaluation of the network's structure, the same approach was followed and results indicate that the network fits the data well. The trained network was compared with an empty and a random graph, and assessed through the log-likelihood function, which showed that the expected loss was lower for the trained network.

According to the results, a strong association between country and all the affective factors that are taken into consideration is identified. Moreover, travel mode choice decisions are also strongly related to country. These preliminary results highlight the need for further investigation into how cultural differences may affect travelers' perceptions and their feelings during everyday trips. Finally, besides the cultural differences that are enclosed in the variable "country", differences with regard to the transport systems are also implied. Such differences both in relation to the system's topology and performance in each country should not be ignored when analyzing travel behavior.

## Conclusions

This paper aimed to investigate relationships between travelers' characteristics, perceptions, and emotions

during everyday trips. For this purpose, a questionnaire survey was conducted in three European countries (Greece, the Netherlands and Spain). The questionnaire consisted of four parts and 27 questions and was aimed at identifying mobility profiles and factors that affect travel choices, as well as travelers' perceptions of the system they use the most. The sample collected after 10 weeks of both an on-site and online survey was well distributed according to gender and age. Both private vehicle users and public transport users are included in the sample. In addition, users of soft of transport are also included in the sample, but they are underrepresented.

Data were used for the development of a Bayesian network that allowed us to infer meaningful interrelations between travelers' choices, characteristics, and perceptions. Results indicated that travel mode choice is the only variable that directly affects the level of travel happiness that a traveler experiences during his/her trip. Furthermore, users' perceptions of the occurrence of unexpected events and the level of tolerance they have toward such events are also directly associated with travel happiness.

The results that emerged from the analysis of the Bayesian network can be used in the framework of quantifying travel happiness to better understand how travel mode choices are made. To this end, the level of tolerance with regard to a system's disruptions and the perceived probability of an unexpected event occurring in a specific mode can be exploited to measure the level of travel happiness. The identified associations between users' characteristics, travel choices, and travel happiness can be exploited to create a personalized trip-based approach to quantifying travel happiness.

Modern research in transport and daily travel behavior places particular emphasis on the needs and requirements of each traveler separately. The findings of this research can be exploited in such systems and applications that seek to provide personalized information and recommendations by highlighting the importance of emotions in the decision-making process of traveling. Moreover, the results can be exploited by policy makers to improve the conditions of and services provided by modern transport systems. Future research should further investigate the notion of travel happiness and examine possible interrelations between travel happiness and additional travel-related choices such as route and time of departure decisions. Furthermore, research should emphasize supplementary variables which may affect the level of travel happiness that the traveler experiences during everyday trips. Finally, it would be interesting to deepen the analysis of the emotional state of the traveler by analyzing specific emotions such as boredom, excitement, anxiousness, and pleasure.

## Acknowledgments

This work is part of the My-Travel Companion (My-TRAC) project funded under the European Union's Horizon 2020 research and innovation program.

## Author Contribution

The authors confirm their contributions to the paper as follows: study conception and design, EM, EV, AP; data collection and initial discussions on the possible statistical inference, EV, EM, HVL, LH-O, SS, VD, AP; analysis and interpretation of results, EM, EV, AP, VD, HVL; draft manuscript preparation, EM, EV, VD, HVL. All authors reviewed the results and approved the final version of the manuscript.
