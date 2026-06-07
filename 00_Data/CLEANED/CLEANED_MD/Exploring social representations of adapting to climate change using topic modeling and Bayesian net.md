# Exploring social representations of adapting to climate change using topic modeling and Bayesian networks 

Timothy Lynam ${ }^{1,2,3}$


#### Abstract

When something unfamiliar emerges or when something familiar does something unexpected people need to make sense of what is emerging or going on in order to act. Social representations theory suggests how individuals and society make sense of the unfamiliar and hence how the resultant social representations (SRs) cognitively, emotionally, and actively orient people and enable communication. SRs are social constructions that emerge through individual and collective engagement with media and with everyday conversations among people. Recent developments in text analysis techniques, and in particular topic modeling, provide a potentially powerful analytical method to examine the structure and content of SRs using large samples of narrative or text. In this paper I describe the methods and results of applying topic modeling to 660 micronarratives collected from Australian academics/researchers, government employees, and members of the public in 2010-2011. The narrative fragments focused on adaptation to climate change (CC) and hence provide an example of Australian society making sense of an emerging and conflict ridden phenomena. The results of the topic modeling reflect elements of SRs of adaptation to CC that are consistent with findings in the literature as well as being reasonably robust predictors of classes of action in response to CC. Bayesian Network (BN) modeling was used to identify relationships among the topics (SR elements) and in particular to identify relationships among topics, sentiment, and action. Finally the resulting model and topic modeling results are used to highlight differences in the salience of SR elements among social groups. The approach of linking topic modeling and BN modeling offers a new and encouraging approach to analysis for ongoing research on SRs.


Key Words: Bayesian network modeling; climate change adaptation; narrative; sense making; social representations; text analysis; topic modeling

## INTRODUCTION

When something unfamiliar emerges or when something familiar does something unexpected people need to make sense of what is emerging or going on. When people started dying of AIDS in the early 1980s; when agricultural input companies sought to introduce genetically modified organisms (GMOs) into farming systems; or when the global financial crisis (GFC) erupted in 2008 people individually and collectively needed to make sense of the new and unfamiliar. In recent years people across the globe have been faced with making sense of climate change (CC; Wolf and Moser 2011, Moloney et al. 2014). Making sense of phenomena is of course a necessary step that enables individuals and groups to cognitively, emotionally, and physically relate to what is going on (Weick 1995, Weick et al. 2005, Klein et al. 2006, Weick 2012).
Social representations theory (SRT) posits processes and mechanisms through which individuals and society make sense of the unfamiliar (Moscovici 1973, 1984, 2000, Wagner and Hayes 2005, Höijer 2011). In essence SRT explains the emergence and dynamics of common sense knowledge and value systems within and across social groups. For more than 50 years SRT has been usefully applied to a diverse portfolio of issues with the theory under active development (Howarth et al. 2011). The last decade has witnessed a number of researchers applying SRT to climate change with most of this work documenting social representations (SRs) using the following data sources: news media reporting (Carvalho 2010, Jaspal and Nerlich 2014, Jaspal et al. 2016), surveys or focus group discussions with members of the general public (Cabecinhas et al. 2008, Reusswig and MeyerOhlendorf 2010, Olausson 2011, Smith and Joffe 2013, GómezMartín and Armesto-López 2014, Moloney et al. 2014, Wibeck 2014, Baquiano and Mendez 2016), and both surveys and media
analyses (Shrestha et al. 2014). Emerging from this work has been an expanding and deepening understanding, among researchers, of how different social groups represent climate change.
Much less is known about social representations of people responding to climate change or about linkages between climate change SRs and action. Only a single theory-based article addressed human responses: Jaspal et al. (2014) suggest researchers need to integrate SR's, identity theory and sociopsychological action to understand human responses to climate change. The first objective of this paper responds to this need through presenting empirically based explorations of linkages between SRs of adaptation, climate change, identity, and action in the context of human responses to climate change. It is recognized that action in relation to climate change presumes some form of climate change representation: the two social objects (climate change and adaptation) are integrally linked.
The second objective of the paper is methodological: automated text analysis or data mining techniques have, consistently and for quite some time, been advocated as an approach to compliment more traditional SRT research approaches (Doise et al. 1993, Lahlou 1996, Kronberger and Wagner 2000, Chartier and Meunier 2011). In a pioneering paper Lahlou (1996) described using lexical analysis software ALCESTE, (Reinert 1983, 1990) to statistically extract elements of SRs associated with eating. Since then a small number of studies have been published using automated text analysis (virtually all using ALCESTE) to identify SRs (Chartier and Meunier 2011).
Automated text analysis has however, evolved significantly in the last 10 years (Evans and Aceves 2016), particularly in relation to the use of hierarchical probability models (topic models) as

[^0]
[^0]:    ${ }^{1}$ Reflecting Society, ${ }^{2}$ James Cook University, Department of Anthropology, ${ }^{3}$ CSIRO

random generating processes for both documents and terms (Blei et al. 2003, McNamara 2011, Riordan and Jones 2011, Blei 2012, Roberts et al. 2014). Although a relatively new field of statistics, topic modeling is rapidly gaining attention across a range of application domains including, for example, a variety of machine learning and data mining tasks (Cook and Krishnan 2015, Wang and Han 2015); analysis of political texts and processes (Grimmer 2010, Roberts et al. 2014, Koltsova and Shcherbak 2015, Lucas et al. 2015); the examination of social networks through writings in social media (Tang and Li 2015); assessing scholarly impact (Gerrish and Blei 2010) and the content of scholarly publications (Griffiths and Steyvers 2004); reviewing consumer research publications (Wang et al. 2015); and evaluating online health service delivery (Chen et al. 2015).
The theory that underpins topic modeling, which sees topics as the generators of documents and word distributions, maps very well onto SRT, which sees SRs as the underlying common sense knowledge of socially relevant phenomena that serve as the basis for thinking, communicating, orientating in the world, and action (Moscovici 1973, Wagner and Hayes 2005). The combination of SRT and topic modeling appears to be a potentially highly informative combination for SR research but the two have so far not been used together. A second objective of the paper is therefore, to document an example of applying topic modeling as an automated text analysis tool in SR research.
Topic modeling makes the following simplifying assumptions (Blei et al. 2003, Blei 2012):

- First, documents, or in our case narrative fragments, are assumed to be bags of words. The structure of sentences and relationships among words are not used;
- Second, topics are defined as distributions of words from a fixed vocabulary. Topics are therefore the imaginary random processes that generate the word distributions that we see in a document;
- Third, documents comprise distributions of topics (documents usually comprise multiple topics) with topics being distributions of words.

Narrative or conversation is seen by many to be the fundamental mechanism of human sense making, cognition, communication, and memory (Barthes and Duisit 1975, Mandler 1984, Bruner 1986, 1990) and key to the formation and maintenance of SRs (László 1997, Wagner and Hayes 2005, Jovchelovitch 2012). In this paper an approach to the analysis of micronarratives collected as part of a collaboration to explore factors enabling or constraining adaptations to CC is described. SRT is the theoretical framework for the investigation and topic modeling is used as a dominant analytical method. Through this analysis answers to the following three questions are presented:

1. Can we reliably detect elements of SRs associated with adaptation to climate change in conversation fragments using topic modeling?
2. Does an understanding of SR's associated with adaptation to climate change enable us to predict CC related action?
3. How are SR elements distributed among different (selfidentifying) social groups?

The data and fuller description of collection process are more fully described in Lynam and Fletcher (2015) so only salient points will be provided here. Thereafter the results of the analyses are presented and discussed in relation to the three questions posed above. I conclude with a reflection on the strengths and weaknesses of the approach used.

## METHODS

## Data collection

An online survey instrument, based on SenseMaker (Cognitive_Edge, http://cognitive-edge.com/sensemaker/), was designed and tested by the research team and then implemented on three separate occasions between June 2010 and April 2011: the first elicited responses from people attending an international scientific symposium on CC held in Australia (CCC, $\mathrm{n}=193$ ); the second elicited responses from individuals working in an Australian state government department with a mandate to work on CC (AUS_GOVT, $\mathrm{n}=121$ ); and the third elicited responses from individuals working on CC in Canada and from a panel of residents living along the eastern seaboard of Australia (AUS_CAN, $\mathrm{n}=627$ ). At the conference attendees were invited to a booth where computers were made available for them to enter their experiences. In addition postcards were provided with the URL to the survey for those seeking to complete the survey at another time. For the Australian state government department respondents were collectively contacted by their department head and invited to participate in the survey. For the Australian public survey an established survey panel was used and potential respondents were invited to participate by the panel managers. For the purposes of this paper only responses from those in each of the surveys who identified themselves as Australian were used $(\mathrm{n}=660)$.
The survey instrument used an integrated mixed methods approach (Tashakkori and Teddlie 2010) in which respondents were asked to imagine being in a conversation with strangers. They were then prompted to respond to a question posed to them by one of the strangers by typing text into an online text box:

Imagine you are in a lift (elevator) with 2 people who are discussing how people and institutions are reacting to climate change. One person mentions that several obstacles constrain the extent to which people are able to prepare for impacts and or adapt. The other person says that she knows of a few examples in which people and institutions are already responding. They turn to you and ask for your perspective on what makes preparation I reaction possible or difficult. How would you respond?

After responding to this prompting question respondents were asked a series of questions in relation to this narrative fragment. One of these questions gave respondents seven options for how their response related to change from which they could select all that applied (preventing change, magnifying change, getting ready for change, changing, recovering from change, reinforcing the effects of change, and none of these). In addition respondents were asked to identify their own social role from a list of six options (Scientist / Academic / Researcher; Government agency employee; NGO employee; Community representative; Private sector employee; and Other).

## Topic model development

Topic models were fit to narrative fragments written by respondents in response to the above prompt. Narrative fragments tended to be short (mean of 53 words) and varied in length from a few words to a maximum of 342 .

Preprocessing of the fragments, prior to model fitting, comprised correcting obvious spelling errors with a word processor, word stemming, and stop word removal. Stemming converts terms to their basic root or stem so that variants, such as climate, climatic, climates would be treated as the same term, e.g., climat. Stop words, e.g., the, it, on, if, contribute little to topic identification and so were removed using the SMART stop word list from Lewis et al. (2004). The corpus of narrative fragments was preprocessed using the stm package (Roberts et al. 2016) in R (R Core Team 2015) to yield a corpus of 660 documents with 1568 terms, i.e., a vocabulary of 1568 terms.

An important choice to make when fitting a topic model is the number of topics to model - k. For the analyses presented here a two-stage process was used to identify a suitable k : first 10 models were fit to the data using $\mathrm{k}=10$ to 100 in increments of 10 . Smaller k was found to yield better fitting models so in the second stage another set of models were fit using $\mathrm{k}=2,3,5,7,10,15,20,25$, and 30 topics. Model suitability was assessed using a combination of the exclusivity and semantic coherence metrics recommended by Roberts et al. (2014) as well as holdout probability. Exclusivity is a measure of the proportion of the top words in a topic that are exclusive to that topic whereas semantic coherence is a measure of the frequency with which top words in a topic cooccur (Mimno et al. 2011, Roberts et al. 2014 and Appendix therein). Holdout probability measures the likelihood of the model when predicting a subset of the data that was not used for model building.

For the analysis presented in this paper a k of 10 , i.e., 10 topics, was selected because it provided higher granularity of topics, i.e., higher exclusivity relative to lower k models, had high semantic coherence, and also performed well from a holdout probability perspective. Once the model was fit to the data, narrative fragments that reflected high proportions for each of the topics were read to ensure the topics results were sensible.

Fitting a topic model creates two important matrices used in the analyses presented here: the first, theta, comprises the proportion of each document assigned to each topic (where documents in our case were the narrative fragments). Each document (row in the matrix) will have a value for each column (topic) that represents the proportion of that document assigned to that topic. The second matrix, beta, comprises the word probabilities for each topic. Each word (row in the matrix) will have a value for each column (topic) that represents the probability of that word in each topic. Topic labels (Table 1) were created by the author for each topic after careful reading of the top terms for each topic in conjunction with reading narratives (documents) that were highly representative of each topic, i.e., they had high theta values for that topic.

## Predicting action, modeling SR structure

To assess whether the results of topic modeling were useful for predicting CC related actions required two steps: first, we needed to identify how respondents related their narratives to change;
and then second we needed to establish a predictive relationship between these change classes and the proportions of topics in their narratives. Recall that respondents were presented with seven options of how their response related to change from which they could select anywhere from one to seven of these options (preventing change, magnifying change, getting ready for change, changing, recovering from change, reinforcing the effects of change, and none of these). Selection of the seventh (none) excluded selection of any of the other options. There were thus $2^{6}=64$ plus $1=65$ unique change classes which, given the data set $(\mathrm{n}=660)$, was too many for our analyses. In addition many of these classes had only a few responses. The number of change classes was reduced to five using Bayesian Latent Class Analysis (BLCA; White and Murphy 2014). BLCA seeks to find latent classes (clusters) in sets of binomial data. BLCA uses a mixture modeling framework to model a target distribution (in our case a multinomial of change class) from a mixture of the seven Bernoulli distributions. BLCA produces class (group) probabilities for each response and item probabilities (where items are the seven binomial variables) for each class or group. The output of the BLCA was a latent class with the input being the matrix of binomial responses to the seven options of how the described experience related to change. Each response in the dataset was assigned to the highest probability latent class with the class being the target for model prediction. Class proportions and item probabilities for these classes are shown in Table 2.

The second step was to test our ability to correctly classify every response as one of these change classes based on the topic proportions in that response. Two tree-augmented naïve Bayes (TAN) classification models (Friedman et al. 1997, Scutari 2010) were trained to classify respondent BLCA Class: the first (base TAN model) included only discretized topic proportions (theta) for each topic and discretized sentiment score. The second (saturated TAN model) had all base variables as well as variables associated with the following: the sample; the respondent (age, gender, education, social group); who the story was about; and seven scales associated with the importance of information, sense of control, efficacy, degree to which respondents felt isolated, the influence of plans or planning, the degree of denial among participants, and the perceived stability of the situation.

A range of discretization's $(\mathrm{n}=2$ to 10 bins) of the theta matrix were tested with best classification accuracy achieved using data discretized into three levels. TAN model prediction accuracy was estimated using a modified 10 -fold cross validation (Kohavi 1995), which divided the data into 30 groups rather than 10 to provide more data for model learning in each iteration. The following process was used: every row in the data matrix was randomly assigned to one of 30 equal sized groups; TAN models were developed with data from 29 of the groups and the data from the held out group was then used for testing (prediction); the BLCA (action) class was "hidden" for the test group and the topic proportions and sentiment score used to predict the action class; these predicted action classes were then compared to the actual action class; each group was held out in turn so the procedure yielded 30 estimates of action class prediction performance.

The sentiment score for each narrative fragment was estimated using the approach and sentiment score library of Hu and Liu (2004), Liu (2012) within the qdap package in R (Rinker 2013).

Table 1. Topic titles, key topic terms (probability and frequency/exclusivity or frex) with mean, sd, median, min, and maximum statistics for topic proportions across the corpus. Frex terms are terms with the highest frequency and exclusivity scores. Most likely terms are the terms with the highest probability.


Sentiment scoring sums the number of positive and the number of negative terms in each document. The negative sum is then subtracted from the positive sum and the result is divided by the square root of the number of terms to yield a sentiment score for the document. As with the theta values sentiment was discretized into three levels: negative, neutral, and positive.
To identify the probabilistic relationships among topical, sentiment, and action elements of the SR's associated with adaptation to climate change a Bayesian Network (BN) model was developed using the bnlearn package (Scutari 2010) of R (R Core Team 2015). Five thousand random networks were generated and then the TABU algorithm, with the k2 score, was used to find the relationships among variables that maximized the score for the data (Scutari 2010, Nagarajan et al. 2013). Models were tested using 30 -fold cross validation described earlier.

BN models were exported to Netica (https://norsys.com/netica. html), which was used for sensitivity analyses and for display purposes. Sensitivity analysis identifies how each variable in the model contributes to uncertainty in the target variable (BLCA class).

## RESULTS AND DISCUSSION

## Overview of topics

Recall that topics are distributions over words. The key terms for each topic, i.e., those with highest probability or highest frex score where frex is a combination of frequency and exclusivity, are shown in Table 1. For example, the terms with the highest frex scores for topic 1 (Barriers) were: barrier, issu, prepar, overcom,
knowledg, obstacle and order and the highest probability terms were: prepar, issu, communiti, inform, impact, understand, chang. Note also that every term in the vocabulary occurs in every topic.

The dominant topic across the corpus was Topic 5 associated with belief and trust as illustrated in the following quote.

I would tell them to do their own research into the subject and don't believe all that is written and said until it can be verified by an honourable source, even then that can be taken with a grain of salt sometimes. (Member of the public, AUS_NS sample, Topic5 proportion $=0.65$ ).
The next most common topic (Topic 9) was associated with empowerment and guidance as illustrated by the following example:

I understand how many people can feel disempowered and unable to do anything. There are people who are doing great things to address the issue but for the majority of people, they either don't understand the full extent of the problem or they feel that there is nothing that they can do that would make a difference. It would be good if we could get more information out there through the popular media which could somehow convey the urgency of the situation but also give people a sense of being able to do something about it - emphasise that even small actions make a difference if everyone takes part. (Government employee, AUS_GOVT sample, Topic9 proportion $=0.91$ ).

Topics 1 (Barriers), 2 (Capacity to act), 7 (Responsibility), and 8 (Finding the way) were next most common, each comprising about $10 \%$ of the corpus:

Table 2. Tree-augmented naïve (TAN) Bayes classification accuracy of respondent action class (BLCA Class) and item probabilities for the BLCA classification. Random classification accuracy was taken to be 0.2 .

Magnify |   |

Lack of knowledge and understanding of the likely impacts, fear campaigns, and apathy (why should I care - taxi driver) are the biggest obstacles. Knowledge and preparation are the keys to managing climate-related disasters as effectively as possible. (Media representative, AUS_NS sample, Topic 1 proportion $=0.67$ ). Preparation and response to CC depends on individuals and communities [sic] adaptive capacity. And adaptive capacity has a number of elements, including current levels of health status, economic status, governance structures. Also, responses to CC can be at a very grassroots level as well as at a high level government level. (Scientist / Academic / Researcher, AUS_CCC sample, Topic 2 proportion $=0.88$ ). Climate change is inevitable and until South America, China and the Iberian Peninsula start to change there is little point in Australians doing anything. I have personally experienced the areas mentioned and anything Australia does will have little or no registerable impact compared to the harm being inflicted by nations whose populations have little or no knowledge of climate change and do not care. (Member of the public, AUS_NS sample, Topic 7 proportion $=0.88$ ). Helping ourselves to try \& be responsible. Insulation, water tanks, careful use of electricity, planting trees if possible. (Member of the public, AUS_NS sample, Topic 8 proportion $=0.85$ ). Topics 3 (Theories of change) and 4 (Living green) were next most common across the corpus, each comprising a little less than $10 \%$ of the corpus:

The difficulty with dealing with climate change is found within the institutional arrangements we currently have. Most arrangements are inadequate to deal with a problem that is ill defined, and thus inadequately addressed with existing capacity that is [sic] falls well short of what is appropriately required. This is driven by a socio-political setting that is oriented towards other social priorities such as economic development that takes precedence over ecological wellbeing. To address climate change issues (symptoms of the problem) we must first address governance and institutional systems (cause or source of the problem) conducive for climate change adaptation. (Scientist / Academic / Researcher, AUS_CCC sample, Topic 3 proportion $=0.89$ ). I and others I am close to have changed their use of energy/power in their daily lives to decrease their footprint. This includes turning devices off where possible, installing fans to decrease A/C use etc., I have recently purchased a new car. I chose a diesel small car with low energy consumption. I am currently installing $P / V$ cells to generate my own power and decrease my reliance on energy generated from fossil fuels that generate high carbon emissions. (Member of the public, AUS_NS sample, Topic 4 proportion $=0.84$ ). Topics 6 (Technology and Economics) and 10 (Natural phenomenon) had the lowest mean proportions across the corpus with about $6 \%$ each:

The constraining factors are cost, technology and a lack of urgency in some areas. Obviously we cannot continue in the long term using constant growth as the only basis for a strong economy. Doing nothing is not really an option and the longer we leave it the more difficult and costly it will be. I don't really have the answers but we need to do something. (Member of the public, AUS_NS sample, Topic 6 proportion $=0.66$ ). I tell them there is no such thing as climate change that it has happened countless times in the past and it has

nothing whatsoever to do with what we are doing with carbon. A single explosion out of a single volcano puts more carbon into the atmosphere than the whole world together and we cannot control the volcano. Whatever we do about carbon it is only about money collection to feed inefficient government. (Scientist / Academic / Researcher, AUS_NS sample, Topic 10 proportion $=0.81$ ).

These examples show that the model derived topics do represent underlying discussion topics that are reasonable and may be reflective of the underlying SRs of adapting to climate change and are consistent with findings elsewhere in the literature, e.g., Lorenzoni et al. (2007), Whitmarsh (2009), Olausson (2011). The examples we have used in these topic descriptions reflect narrative fragments with high proportions of the focal topic. Most documents should comprise multiple topics and the relationships among topics across the body of narratives could provide a new way of looking at SR structure. We present results to demonstrate this claim in a later section of the paper but first we demonstrate the relationship between topics and action as SRT suggests SRs comprise "... patterns and features of discourse and extended activity realised by individuals..." (Wagner and Hayes 2005:255).

## Predicting action class using topic proportions and sentiment scores

Survey respondents were asked to identify how the experience they described related to change. We have previously described how the selections of options they made were assigned to one of five discrete (latent) classes (preparing, changing, reinforcing, preventing or magnifying, and none of these) and how treewaugmented naïve Bayes (TAN) modeling was used to classify each of the 660 responses into one of these action classes based on topic proportions and sentiment scores. If, as SRT suggests, SRs orient people to action, then knowledge of SRs associated with CC adaptation should enable us to identify likely action classes. To benchmark these classifications model results were compared to a random assignment: random assignment of responses to an action class would, on average, get the class assignment correct $20 \%$ of the time. Classification accuracy better than random indicates what can be learned about action through knowing about topic proportions.

Overall the classification accuracy of the TAN models was close to twice as good as a random assignment. Unfortunately this aggregated performance masked some poor classification performance: we were able to predict preparing, changing, or none very much better than a random assignment model but the classification accuracy with reinforcing and preventing / magnifying was worse than the random assignment model (Table 2). To put this in context: based only on topics generated from narrative fragments and the sentiment generated from words in the fragments the TAN model was able to correctly predict those that were preparing to adapt to climate change $58 \%$ of the time, those that were adapting (changing) to climate change $34 \%$ of the time, and those that were doing none of these things $51 \%$ of the time (Table 2).

The poor classification accuracy for the Reinforcing and Prevent / Magnify classes is attributed to two things: first, the small number of responses in these two classes provides fewer cases for model learning; and second these two groups were quite mixed in the action items assigned to them: Group 4 (Reinforcing) in
particular had all action options except "none of these" assigned to it while group 5 (Prevent / Magnify) comprised a mixture of two quite different activities: preventing change and magnifying change (Table 2).

Sensitivity analyses of the action class node in the base TAN model identified Topic 10 (Natural phenomena), Topic 2 (Capacity to act), Topic 5 (Belief, trust), and Sentiment score as the predictor variables contributing most to uncertainty in the BLCA (action) class classification. Topic 10 separated the two action classes (Preparing and Changing) from None: when respondents had a high proportion of Topic 10 (Natural phenomena) in their narratives they were four times more likely to be classed as "None" compared with those with low proportions of Topic 10 (see example below). Preparing and Changing were over four times more likely than None with low proportions of Topic 10.

Although man contributes in a minimal fashion by overpopulation, agriculture and pollution the forces of nature such as solar radiation, magnetic and geothermal forces, rotation and planetary and celestial conjunctions create most of the change. (Member of the public, AUS_NS sample, Topic 10 proportion $=0.76$, BLCA class None).

Topic 2 was strongly related to Preparing: respondents with high proportions of Topic 2 (Capacity to act) were 7 times more likely to be Preparing than those with low proportions of Topic 2. When readying themselves to change respondents needed to assess or discuss what capacities were needed to act. But Topic 2 was also common among narratives of those changing.

In some circumstances practical capacities exist with well resourced people and in other circumstances people may not have the resources and have no idea as to how they can be adapting. (NGO Employee, AUS_CCC sample, Topic 2 proportion $=0.76$, BLCA class Preparing).
Being the dominant (highest probability) topic, Topic 5 (Belief, trust) was associated with all action classes. It was however, useful for exploring the different facets of belief and trust and how these worked through to action. High levels of Topic 5 were associated both with Preparing and with None as the following examples illustrate:

People do not always trust the source of their knowledge of climate change, resulting in scepticism and resentment. Media, government influence affects the way people deal with climate change. People are unsure if climate change is happening and then if they do believe they may not know how to go about changing their behaviours. I think money is a big issue for some people. For some people denying the impacts of climate change is a way to protect themselves from another stressor. (Government employee, AUS_CCC sample, Topic 5 proportion $=$ 0.39 , BLCA class Preparing).

I don't think we have enough proof yet that climate change is real. (Member of the public, AUS_NS sample, Topic 5 proportion $=0.43$, BLCA class None).
Topic modeling does therefore generate informative topics reflective of elements of SRs of adapting to climate change. Topic

Fig. 1. Representation of the Bayesian Network model developed using the TABU algorithm and k2 score. Topic proportions are shown in blue, self-identified respondent role in grey, and action class in red. Bars in each box reflect the probability of the states (for topics low, moderate, and high) with probabilities shown as percentages. Probabilistic relationships among variables are represented as directed arrows.
![img-0.jpeg](img-0.jpeg)
proportions were sufficiently strongly associated with action classes to enable reasonably accurate prediction.

## Topic proportions among social groups

The algorithm used to develop the BN finds the association among variables that maximizes the k2 score (the penalized likelihood of the data, for this exploration the discretized proportions of topics, sentiment scores, action class, and selfidentified social role for each response were used). The resulting BN can be thought of as a probabilistic snapshot of SR elements associated with SRs of adapting to climate change drawn from a sample of 660 Australians (Fig. 1). The following discussion of structure and elements of SRs draws heavily on the structuralist SR perspectives of Abric (2001), Wagner and Hayes (2005), and Lahlou and Abric (2011).
The BN was used to examine several properties of SR structure. First the co-occurrence probabilities of, and dependencies among, topics or SR elements; second the core and peripheral elements of the SR; and third the most salient (probable) topics (elements) across subgroups of the sample.
Using all variables to predict the state of each topic in turn yielded a mean (std) proportion correctly predicted of $0.66(0.08)$, i.e., prediction accuracy twice as good as a random model. In what follows a few examples of "storylines," derived from querying the BN probabilities are described as examples of the associations among topics, i.e., SR elements:

1. If a person believed climate change to be a natural phenomenon (Topic 10) they would have no need to include capacity to act (Topic 2) or theories of change (Topic 3) in their narratives but would likely include beliefs and trust (Topic 5). This was the case: those with high proportions of Topic 10 were one tenth as likely to have high proportions of Topic 2, half as likely to have high proportions of Topic 3 but 20 times more likely to have high proportions of Topic 5 in their narratives relative to those with low proportions of Topic 10 ;
2. Those discussing barriers to changing (Topic 1) would also likely discuss capacity to act (Topic 2), the need for empowerment and guidance (Topic 9) and theories of change (Topic 3). Again these expectations were supported by the BN results: high proportions of Topic 1 (Barriers) were 23 times more likely associated with high proportions of Topic 9, 30 times more likely to be associated with high proportions of Topic 3, and 24 times more likely to have high proportions of Topic 2 than those with low proportions of Topic 1;
3. Respondents with high proportions of Topic 4 (Living green) were almost 7 times more likely to have high proportions of Topic 6 (Technology \& economics) in their narratives than were those with low proportions of Topic 4.
The BN model thus provides a probabilistic synthesis (with known predictive accuracy) of the SR of adapting to CC observed across the sample.

Fig. 2. Bar graphs of probabilities associated with each topic state (i.e., topic proportion of high, medium, or low) for each topic by social group (government employees, members of the public, and researchers).
![img-1.jpeg](img-1.jpeg)

A body of SR theorists have written about the core and peripheral elements of SRs: core elements are seen as the stable, universal components that "give the representation its significance and coherence" while peripheral elements are more ephemeral and perhaps not as broadly salient (Abric 1996, Wagner et al. 1996, Abric 2001, Wagner and Hayes 2005, Lahlou and Abric 2011). If it is assumed that stable topic proportions (SR elements) across social groups are indicative of core elements of the SR then querying the BN model probabilities identified Topic 6 (Technology \& Economics), Topic 9 (Empower \& Guide) to be relatively stable, i.e., relatively constant probabilities of topic proportions, across the social groups in the model (government employees, researchers, the public and other; Fig. 2). Sentiment and action class were also relatively stable across these groups.

The BN model was also used to explore the salience of different SR elements (topics) across the social group each respondent identified with. The probabilities of topic proportions for each of the three major groups are shown in Figure 2 and illustrate the differences and similarities in salience of topic proportions (SR elements) across groups: based on Euclidian distance measures government employee and researcher patterns of probability across topic proportions were more similar to each other than either was to that of the public. Most notable was the much higher probability of high proportions of Topic 10 (Natural phenomenon) among the public ( 9 times higher than government employees and 3 times higher than researchers) and higher proportions of Topic 8 among the public (Finding the way, twice as high as government employees and 5 times higher than researchers). Highly salient for the public therefore, is the need for help to deal with the natural phenomenon of CC. Topic proportions are also useful to illuminate the relative distributions, in topical space, of individuals drawn from different social groups. The topics to which the variable respondent role was most sensitive were Topics $10,8,3$, and 2 so these were used to map
individual locations in topical space: the much higher levels of Topic 10 (Natural phenomena) among members of the public relative to government employees or researchers is clearly visible in Figure 3, as is the strong negative relationship between Topic 10 and Topic 8 (Finding the way) among government employees.

The BN highlights a view of SRs that integrates meanings (including those beyond the focus of climate change), emotions, and actions, a view consistent with recent empirical results (Lorenzoni et al. 2007, Whitmarsh 2009, Fischer et al. 2012, Evans et al. 2016) and theory (Gifford 2011, Jaspal et al. 2014). From this perspective people make sense of the world through broad, shared, and interconnected networks of meaning, emotion, and action, not via narrowly defined, single-issue themes, attitudes, or behaviors.

The combination of BNs and topic modeling may thus provide a relatively straight forward approach to the examination of SR content (the word distributions of the topics, specific emotional content, and actual activities) and SR structure (the interconnected networks of relationships among topics, sentiment, and action). The approach is consistent with SRT and through the use of Bayesian probability theory, relatively simple to interpret.

## CONCLUSIONS

Topic modeling appears to offer considerable potential for the examination of SRs. The topics generated from an Australian sample of narrative fragments associated with adaptation to climate change capture elements of SRs of CC adaptation prevailing at that time. These automated, text-analytic "bag of words" distributions of words and topics provide a new way to examine SRs while sharing complimentary theoretical assumptions: that topics or SR elements are the underlying random processes that generate the observed word and topic distributions.

Fig. 3. Topic proportion maps for Topic 8 (Finding the way) and Topic 10 (Natural phenomenon) for people identifying as members of the public, government employees, and researchers. Symbol color reflects the proportion of Topic 3 (Theories of change) and symbol size reflections the proportion of Topic 2 (Capacity to act). Each point on the map is the location of one narrative. Vertical and horizontal dashed lines indicate where topic proportions $=0.10$. Points to the right or above these lines are considered to have notable proportions of those topics.
![img-2.jpeg](img-2.jpeg)

The topics themselves were informative and provided logically related and probabilistic storylines of how people in the sample represented the phenomenon of adaptation to climate change. Additionally, topic proportions provide information on SR structure and topic (SR element) salience across the sample or subgroups within the sample.
Theory holds that SRs include cognitive, emotional, and action elements. The BN modeling used in this paper demonstrates the statistical integration of these elements: the TABU model presented was used to discover the relationship among variables that was most likely given the data. As far as is known this approach has not previously been applied in SR research.
The results presented here support research and theory that conceive SRs as shared and interconnected networks of meanings, emotion, and action that extend beyond a single issue or thematic focus. This is both good news and bad: on the one hand it provides multiple possible leverage points for action to influence outcomes; but on the other it highlights that the core elements of SRs may be protected or maintained by issues / topics / elements that are only distally related to the focal issue.
The approach of eliciting micronarratives and then having respondents interpret their narratives using a small number of defined measures enabled identification of topics but also identification of how these topics related to action. The approach provides a potentially powerful and fully integrated hybrid of qualitative and quantitative methods.
Although the methods described in this paper appear to hold promise as a new data collection and analytical approach to exploring SRs, what was done has limitations that suggest caution
in interpretation: SRs of contentious issues such as CC and CC adaptation are likely to be in constant flux; although some of the elements identified in the original data set are likely to be persistent, new topics are likely to have emerged and the relative salience of topics is bound to have changed since the data were collected.

In addition the data from researchers, government employees, and the public were collected over a period of almost 11 months, time enough for changes to occur in the SR elements, and particularly given the very negative Australian media coverage of CC at that time (Bacon 2013). The data were not collected from a random sample and hence are not considered representative of groups or sections of the Australian populace.

## Responses to this article can be read online at: http://www.ecologyandsociety.org/issues/responses. php/8778

## Acknowledgments:

The support and assistance of staff and students from the University of the Sunshine Coast in relation to collecting data at the NCCARF conference is gratefully acknowledged. The research was part of the South East Queensland Climate Adaptation Research Initiative, a partnership between the Queensland and Australian Governments, the CSIRO Climate Adaptation National Research Flagship, Griffith University, University of the Sunshine Coast, and University of Queensland. The initiative aimed to provide research

knowledge to enable the region to adapt and prepare for the impacts of climate change. The comments and suggestions of three anonymous reviewers helped clarify and improve the paper - thank you all. Thanks also to Iain Walker for ongoing support and insight. Support for completion of the paper was provided by Reflecting Society and James Cook University.

## LITERATURE CITED

Abric, J.-C. 1996. Nature and function of the core system of social representations. International Journal of Psychology 31:1443-1443.

Abric, J.-C. 2001. A structural approach to social representations. Pages 42-47 in K. Deaux and G. Philogene, editors. Representations of the social. Blackwell, Oxford, UK.

Bacon, W. 2013. Sceptical climate Part 2: climate science in Australian newspapers. The Australian Centre for Independent Journalism, Sydney, Australia.

Baquiano, M. J., and A. J. P. Mendez. 2016. Social representations of climate change: a cross-cultural investigation. American International Journal of Contemporary Research 6(1).

Barthes, R., and L. Duisit. 1975. An introduction to the structural-analysis of narrative. New Literary History 6:237-272. http://dx.doi.org/10.2307/468419

Blei, D. M. 2012. Probabilistic topic models. Communications of the ACM 55:77-84. http://dx.doi.org/10.1145/2133806.2133826

Blei, D. M., A. Y. Ng, and M. I. Jordan. 2003. Latent Dirichlet allocation. Journal of Machine Learning Research 3:993-1022.

Bruner, J. S. 1986. Actual minds, possible worlds. Harvard University Press, Cambridge, Massachusetts, USA.

Bruner, J. S. 1990. Acts of meaning. Harvard University Press, Cambridge, Massachusetts, USA.

Cabecinhas, R., A. Lázaro, and A. Carvalho. 2008. Media uses and social representations of climate change. Pages 170-189 in A. Carvalho, editor. Communicating climate change: discourses, mediations and perceptions. Centro de Estudos de Comunicação e Sociedade, Universidade do Minho, Portugal.

Carvalho, A. 2010. Media(ted) discourses and climate change: a focus on political subjectivity and (dis)engagement. Climate Change 1:172-179. http://dx.doi.org/10.1002/wcc. 13

Chartier, J.-F., and J.-G. Meunier. 2011. Text mining methods for social representation analysis in large corpora. Papers on Social Representations 20:37.31-37.47.

Chen, Z., P. W. Koh, P. L. Ritter, K. Lorig, E. O. Bantum, and S. Saria. 2015. Dissecting an online intervention for cancer survivors: four exploratory analyses of internet engagement and its effects on health status and health behaviors. Health Education \& Behavior 42:32-45. http://dx.doi.org/10.1177/1090198114550822

Cook, D. J., and N. C. Krishnan. 2015. Activity learning: discovering, recognizing, and predicting human behavior from sensor data. Wiley, Hoboken, New Jersey, USA. http://dx.doi. org/10.1002/9781119010258

Doise, W., A. Clemence, and F. Lorenzi-Cioldi. 1993. The quantitative analysis of social representations. Harvester Wheatsheaf, Hemel Hempstead, UK.

Evans, J. A., and P. Aceves. 2016. Machine translation: mining text for social theory. Annual Review of Sociology 42:21-50. http:// dx.doi.org/10.1146/annurev-soc-081715-074206

Evans, L. S., C. C. Hicks, W. N. Adger, J. Barnett, A. L. Perry, P. Fidelman, and R. Tobin. 2016. Structural and psycho-social limits to climate change adaptation in the Great Barrier Reef Region. PLoS ONE 11:e0150575. http://dx.doi.org/10.1371/journal. pone. 0150575

Fischer, A., V. Peters, M. Neebe, J. Vávra, A. Kriel, M. Lapka, and B. Megyesi. 2012. Climate change? No, wise resource use is the issue: social representations of energy, climate change and the future. Environmental Policy and Governance 22:161-176. http:// dx.doi.org/10.1002/eet. 1585

Friedman, N., D. Geiger, and M. Goldszmidt. 1997. Bayesian network classifiers. Machine Learning 29:131-163. http://dx.doi. org/10.1023/A:1007465528199

Gerrish, S., M, and D. M. Blei. 2010. A language-based approach to measuring scholarly impact. Pages 375-382 in Proceedings of the 27th International Conference on Machine Learning, Haifa, Israel.

Gifford, R. 2011. The dragons of inaction: psychological barriers that limit climate change mitigation and adaptation. American Psychologist 66:290-302. http://dx.doi.org/10.1037/a0023566

Gómez-Martín, M. B., and X. A. Armesto-López. 2014. Assessing knowledge of social representations of climate change and tourism. Pages 307-321 in C. A. Brebbia, S. Favro, and F. D. Pineda, editors. Sustainable tourism VI. WITPress, Southampton, UK. http://dx.doi.org/10.2495/st140241

Griffiths, T. L., and M. Steyvers. 2004. Finding scientific topics. Proceedings of the National Academy of Sciences 101:5228-5235. http://dx.doi.org/10.1073/pnas. 0307752101

Grimmer, J. 2010. A Bayesian hierarchical topic model for political texts: measuring expressed agendas in senate press releases. Political Analysis 18:1:35. http://dx.doi.org/10.1093/pan/ mpp034

Höijer, B. 2011. Social representations theory a new theory for media research. Nordicom Review 32:3-16.

Howarth, C., N. Kalampalikis, and P. Castro. 2011. Editorial: 50 years of research on social representations: central debates and challenging questions. Papers on Social Representations 20:9.1-9.11.

Hu, M., and B. Liu. 2004. Mining and summarizing customer reviews. Pages 168-177 in Proceedings of the 10th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), New York, New York, USA. http://dx.doi. org/10.1145/1014052.1014073

Jaspal, R., and B. Nerlich. 2014. When climate science became climate politics: British media representations of climate change in 1988. Public Understanding of Science 23:122-141. http://dx. doi.org/10.1177/0963662512440219

Jaspal, R., B. Nerlich, and M. Cinnirella. 2014. Human responses to climate change: social representation, identity and sociopsychological action. Environmental Communication 8:110-130. http://dx.doi.org/10.1080/17524032.2013.846270

Jaspal, R., B. Nerlich, and K. van Vuuren. 2016. Embracing and resisting climate identities in the Australian press: sceptics, scientists and politics. Public Understanding of Science 25:807-824. http://dx.doi.org/10.1177/0963662515584287

Jovchelovitch, S. 2012. Narrative, memory and social representations: a conversation between history and social psychology. Integrative Psychological and Behavioral Science 46:440-456. http://dx.doi.org/10.1007/s12124-012-9217-8

Klein, G., B. Moon, and R. R. Hoffman. 2006. Making sense of sensemaking 1: alternative perspectives. IEEE Intelligent Systems 21:70-73. http://dx.doi.org/10.1109/MIS.2006.75

Kohavi, R. 1995. A study of cross-validation and bootstrap for accuracy estimation and model selection. Pages 1137-1143 in International Joint Conference on Artificial Intelligence. Morgan Kaufmann, San Francisco, California, USA.

Koltsova, O., and A. Shcherbak. 2015. 'LiveJournal Libra!': The political blogosphere and voting preferences in Russia in 2011-2012. New Media \& Society 17:1715-1732. http://dx.doi. org/10.1177/1461444814531875

Kronberger, N., and W. Wagner. 2000. KEYWORDS in context: statistical analysis of text features. Pages 299-317 in M. W. Bauer and G. Gaskell, editors. Qualitative researching with text, image and sound. SAGE, London, UK.

Lahlou, S. 1996. A method to extract social representations from linguistic corpora. Japanese Journal of Experimental Social Psychology 35:278-291. http://dx.doi.org/10.2130/jjesp. 35.278

Lahlou, S., and J.-C. Abric. 2011. What are the "elements" of a representation? Papers on Social Representations 20:20.1-20.10.

László, J. 1997. Narrative organization of social representations. Papers on Social Representations 6:155:172.

Lewis, D. D., Y. Yang, T. G. Rose, and F. Li. 2004. RCV1: A new benchmark collection for text categorization research. Journal of Machine Learning Research 5:361-397.

Liu, B. 2012. Sentiment analysis and opinion mining. Morgan \& Claypool, San Rafael, California, USA.

Lorenzoni, I., S. Nicholson-Cole, and L. Whitmarsh. 2007. Barriers perceived to engaging with climate change among the UK public and their policy implications. Global Environmental Change 17:445-459. http://dx.doi.org/10.1016/j.gloenvcha.2007.01.004

Lucas, C., R. A. Nielsen, M. E. Roberts, B. M. Stewart, A. Storer, and D. Tingley. 2015. Computer-assisted text analysis for comparative politics. Political Analysis 23:254-277. http://dx.doi. org/10.1093/pan/mpu019

Lynam, T., and C. Fletcher. 2015. Sensemaking: a complexity perspective. Ecology and Society 20(1):65. http://dx.doi. org/10.5751/es-07410-200165

Mandler, J. M. 1984. Stories, scripts, and scenes: aspects of schema theory. L. Erlbaum Associates, Hillsdale, New Jersey, USA.

McNamara, D. S. 2011. Computational methods to extract meaning from text and advance theories of human cognition. Topics in Cognitive Science 3:3-17. http://dx.doi.org/10.1111/ j.1756-8765.2010.01117.x

Mimno, D., H. M. Wallach, E. Talley, M. Leenders, and A. McCallum. 2011. Optimizing semantic coherence in topic models. Pages 262-272 in Proceedings of the Conference on Empirical Methods in Natural Language Processing. Association for Computational Linguistics, Stroudsburg, Pennsylvania, USA.

Moloney, G., Z. Leviston, T. Lynam, J. Price, S. Stone-Jovicich, and D. Blair. 2014. Using social representations theory to make sense of climate change: what scientists and nonscientists in Australia think. Ecology and Society 19(3):19. http://dx.doi. org/10.5751/es-06592-190319

Moscovici, S. 1973. Foreword. Pages ix-xiv in C. Herzlich, editor. Health and illness: a social psychological analysis. Academic Press, London, UK. http://dx.doi.org/10.1111/j.2044-8309.1996.tb01079. x

Moscovici, S. 1984. The phenomenon of social representations. Pages 3-69 in R. M. Farr and S. Moscovici, editors. Social representations. Cambridge University Press, Cambridge, UK.

Moscovici, S. 2000. Social representations: explorations in social psychology. Polity Press, Cambridge, England.

Nagarajan, R., M. Scutari, and S. Lèbre. 2013. Bayesian networks in $R$ with applications in systems biology. Use R! Series, Volume 48. Springer, New York, New York, USA. http://dx.doi. org/10.1007/978-1-4614-6446-4

Olausson, U. 2011. "We're the ones to blame": citizens' representations of climate change and the role of the media. Environmental Communication 5:281-299. http://dx.doi. org/10.1080/17524032.2011.585026

R Core Team. 2015. R: A language and environment for statistical computing. The R Project for Statistical Computing, Vienna, Austria.

Reinert, M. 1983. Une méthode de classification descendante hiérarchique: application à l'analyse lexicale par contexte. Les cahiers de l'analyse des données 8:187-198.

Reinert, M. 1990. Alceste une méthodologie d'analyse des données textuelles et une application: Aurelia de Gerald de Nerval. Bulletin de méthodologie sociologique 26:24-54. http://dx. doi.org/10.1177/075910639002600103

Reusswig, F., and L. Meyer-Ohlendorf. 2010. Social representation of climate change. A case study from Hyderabad (India). Europäischer Hochschulverlag GmbH, Bremen, Germany.

Rinker, T. W. 2013. qdap: Bridging the gap between qualitative data and quantitative analysis. The R Project for Statistical Computing. Vienna, Austria.

Riordan, B., and M. N. Jones. 2011. Redundancy in perceptual and linguistic experience: comparing feature-based and distributional models of semantic representation. Topics in Cognitive Science 3:303-345. http://dx.doi.org/10.1111/ j.1756-8765.2010.01111.x

Roberts, M. E., B. M. Stewart, and D. Tingley. 2016. stm: $R$ package for structural topic models. [online] URL: http://www. structuraltopicmodel.com

Roberts, M. E., B. M. Stewart, D. Tingley, C. Lucas, J. LederLuis, S. K. Gadarian, B. Albertson, and D. G. Rand. 2014. Structural topic models for open-ended survey responses. American Journal of Political Science 58:1064-1082. http://dx.doi. org/10.1111/ajps. 12103

Scutari, M. 2010. Learning Bayesian networks with the bnlearn R Package. Journal of Statistical Software 35(3):1-22. http://dx. doi.org/10.18637/jss.v035.i03

Shrestha, S., K. Burningham, and C. B. Grant. 2014. Constructions of climate change on the radio and in Nepalese lay focus groups. Environmental Communication 8:161-178. http://dx. doi.org/10.1080/17524032.2014.906480

Smith, N., and H. Joffe. 2013. How the public engages with global warming: a social representations approach. Public Understanding of Science 22:16-32. http://dx.doi.org/10.1177/0963662512440913

Tang, J., and J. Li. 2015. Semantic mining of social networks. Pages 1-205 in Y. Ding, P. Groth, and J. Hendler, editors. Synthesis lectures on the semantic web: theory and technology. Morgan \& Claypool, San Rafael, California, USA. http://dx.doi. org/10.2200/s00629ed1v01y201502wbe011

Tashakkori, A., and C. Teddlie. 2010. SAGE handbook of mixed methods in social \& behavioral research. SAGE, Los Angeles, California, USA. http://dx.doi.org/10.4135/9781506335193

Wagner, W., and N. Hayes. 2005. Everyday discourse and common sense. The theory of social representations. Palgrave, New York, New York, USA.

Wagner, W., J. Valencia, and F. Elejabarrieta. 1996. Relevance, discourse and the 'hot' stable core of social representations: a structural analysis of word associations. British Journal of Social Psychology 35:331-352. http://dx.doi.org/10.1111/j.2044-8309.1996. tb01101.x

Wang, C., and J. Han. 2015. Mining latent entity structures. Pages 1-159 in J. Han, L. Getoor, W. Wang, J. Gehrke, and R. Grossman, editors. Synthesis lectures on data mining and knowledge discovery. Morgan \& Claypool, San Rafael, California, USA. http://dx.doi. org/10.2200/s00625ed1v01y201502dmk010

Wang, X., N. T. Bendle, F. Mai, and J. Cotte. 2015. The Journal of Consumer Research at 40: a historical analysis. Journal of Consumer Research 42:5-18. http://dx.doi.org/10.1093/jcr/ ucv009

Weick, K. E. 1995. Sensemaking in organizations. SAGE, Thousand Oaks, California, USA.

Weick, K. E. 2012. Organized sensemaking: a commentary on processes of interpretive work. Human Relations 65:141-153. http://dx.doi.org/10.1177/0018726711424235

Weick, K. E., K. M. Sutcliffe, and D. Obstfeld. 2005. Organizing and the process of sensemaking. Organization Science 16:409-421. http://dx.doi.org/10.1287/orsc.1050.0133

White, A., and T. B. Murphy. 2014. BayesLCA: an R Package for Bayesian latent class analysis. Journal of Statistical Software 61 (13):1-28. http://dx.doi.org/10.18637/jss.v061.i13

Whitmarsh, L. 2009. Behavioural responses to climate change: asymmetry of intentions and impacts. Journal of Environmental Psychology 29:13-23. http://dx.doi.org/10.1016/j.jenvp.2008.05.003

Wibeck, V. 2014. Social representations of climate change in Swedish lay focus groups: local or distant, gradual or catastrophic? Public Understanding of Science 23:204-219. http:// dx.doi.org/10.1177/0963662512462787

Wolf, J., and S. C. Moser. 2011. Individual understandings, perceptions, and engagement with climate change: insights from in-depth studies across the world. Climate Change 2:547-569. http://dx.doi.org/10.1002/wcc. 120