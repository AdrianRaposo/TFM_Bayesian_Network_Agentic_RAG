# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Pitchforth, Jay, Wu, Paul, \& Mengersen, Kerrie
(2014)

Applying a validation framework to a working airport terminal model.
Expert Systems with Applications, 41(9), pp. 4388-4400.
This file was downloaded from: https://eprints.qut.edu.au/70943/

## (c) Consult author(s) regarding copyright matters

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

License: Creative Commons: Attribution-Noncommercial-No Derivative Works 2.5

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.1016/j.eswa.2014.01.013

# Applying a Validation Framework to a Working Airport Terminal Model 

Jegar Pitchforth*, Paul Wu, Kerrie Mengersen<br>Queensland University of Technology


#### Abstract

Validation is an important issue in the development and application of Bayesian Belief Network (BBN) models, especially when the outcome of the model cannot be directly observed. Despite this, few frameworks for validating BBNs have been proposed and fewer have been applied to substantive real-world problems. In this paper we adopt the approach by Pitchforth \& Mengersen [32], which includes nine validation tests that each focus on the structure, discretisation, parameterisation and behaviour of the BBNs included in the case study.


We describe the process and result of implementing a validation framework on a model of a real airport terminal system with particular reference to its effectiveness in producing a valid model that can be used and understood by operational decision makers. In applying the proposed validation framework we demonstrate the overall validity of the Inbound Passenger Facilitation Model as well as the effectiveness of the validity framework itself. Keywords: Bayesian Belief Network, validation, application, airport,

[^0]
[^0]:    * Phone: +61 403961878

    Email address: jegar.pitchforth@qut.edu.au ()
    ${ }^{1}$ Queensland University of Technology, Gardens Point Campus, Building P, Lvl 7

# 1. Introduction 

Expert-informed Bayesian Networks, or Bayesian Belief Networks (BBN) [31] are a popular systems modelling approach in cases where the behaviour of a system is not entirely known, or is difficult to observe. In such cases, validation presents a challenge that cannot be answered using the commonly used goodness-of-fit tests, such as AIC, BIC or DIC [14, 33]. In particular, such tests require an objective and directly observed output that can be used to train and then test the model parameters. Such an arrangement is useful in areas where the system output can be observed, but the range of interactions producing such results are too complex to be thought about all at once, such as the technical performance of an information system [29] or the financial performance of some organisation [18].

However, in many cases BBNs are used precisely because no such output is possible to collect, such as in ecology, risk analysis and social behavioural studies [16]. In other cases, such as in airport passenger flows, there is a theoretically observable output but gaining such data is expensive or difficult, making BBNs a much more practical and realistic alternative for describing and predicting the behaviour of the system. This is similar to identifying the effect of a latent variable in the model (see Yet et al. [42] for methods of achieving this), but in these cases the latent variable is the output of the model. In such domains there is no known method of determining overall validity as there is no ground truth data against which model outputs can be compared.

In these cases the question of validation is often only addressed in passing through expert self-checking or otherwise is answered with an incomplete view of validity constructs. For example, Scholten et al. [35] and Stark et al. [38] both use very sophisticated approaches to using expert elicitation in their models, but are limited to validating the results using expert opinion either through direct interview or expert-created scenarios. In such cases it is not useful to provide accurate validity diagnostics, as the test data cannot be seen as ground truth making the diagnostic misleading and may lead to criteria contamination, or self confirmation [7]. In their model of IT project success, Gingnell et al. [15] focus validation attempts only on defending the assumptions of the Noisy OR-gates used in their elicitation to reduce expert workload, which provides an incomplete assessment of model validity. This method of validating the model lends weight to the approach of building confidence in validity incrementally rather than a binary judgment using a single diagnostic measure based on comparison to ground truth data, however it is incomplete from the perspective of the Pitchforth \& Mengersen [32] framework. Another approach is to generate synthetic data and compare the model output against this [3], although this approach also focuses solely on the predictive validity of the model and is essentially equivalent to a Qualitative Features Analysis.

A lmost no work has been conducted on frameworks to address validation in expert elicited models when there is no ground truth dataset available, despite validity issues being raised by critics as an issue with using experts for BBN modelling [10]. However, for a model to be successfully implemented into everyday decision scenarios the user must be confident that they are

receiving an accurate representation of the system they are controlling. If model developers cannot reach some assessment of the validity of their work it is most likely that decision-makers will ignore model results and continue working using traditional methods. In some cases this simply results in nonoptimal system operations, however in the case of critical infrastructure the result can be the development and maintenance of unreasonably high risk protocols.

In response to the lack of methods for validating BN models when no output data are available, a framework of validity tests was introduced by Pitchforth \& Mengersen [32] for practical application to expert-elicited and expert-informed BBNs. These tests were drawn from a variety of disciplines such as statistics, psychology and system dynamics to give helpful guidance on the strength of a model's validity where no ground truth data are available against which model outputs can be tested. However, the framework is still only theoretical and has not been established as practically effective through application to a working model of a real system.

Here we apply that framework to the Inbound Passenger Facilitation Model (IPFM), a model designed to represent the inbound passenger facilitation system at an Australian international airport. This is the first application of the framework by Pitchforth \& Mengersen [32] to a working BN model that cannot be trained and tested using directly observed output data, and has been used to demonstrate the validity of the model to airport stakeholders. In order to achieve this many tests described in this paper have been further developed from the original paper describing the framework.

In using the framework to validate a working airport terminal model, we

aim to first demonstrate that the framework can be usefully applied to models with little or no observable output data and how this can be achieved. Our second aim is to demonstrate that by being subjected to the validity tests in the framework the IPFM has become a more valid representation of the real-world system than prior to their application.

# 1.1. Background 

The IPFM is a model of airport terminal behaviour with a focus on inbound passenger facilitation times. Initial model development was in response to work by Hargreaves [19] that took a deterministic approach to developing a measurement framework (as opposed to a model) for this system. While their work was comprehensive, the lack of a coherent holistic model of the system in question meant the results of the work were never applied in practical operations management. In addition, the sampling strategy required to quantify their metric framework proved infeasible. While limited samples are taken from the airport throughout the year, the rarity of such sampling along with the acknowledged error of the measurements means that such samples are unlikely to be useful for model validation purposes. In this case, using expert opinion to support observational data is an important step in creating reliable and valid systems models.

At the point of conception there were a range of theoretical goals set out for the model, such as integrating disparate datasets that were being maintained by numerous stakeholders, capturing the knowledge of experts and predicting the performance of the system in different scenarios. After a search of existing airport terminal performance models a BBN was identified as a suitable modelling tool for achieving these goals. These goals were grad-

ually refined over the course of the project through interviews and workshops held at each iteration of model development.

Once initial reporting has been completed it became apparent that significant validation testing would be required before the model could be approved for use in managing critical infrastructure. However, much of the model was unable to be tested against objective data because it was too expensive to collect so had been quantified using expert elicitation. This led to an exploration of similar situations in which no directly observable outcome is possible, and ultimately to the development of the framework outlined in Pitchforth \& Mengersen [32] and applied in this paper. For approval to be used in daily operations, these tests of validity needed to be usefully applied and communicated to stakeholders in order to build their confidence that the model is a valid representation of inbound passenger processing.

# 1.1.1. Bayesian Belief Networks 

BBNs are a member of the family of conditional joint probability models known as Bayesian Networks (BN) [31]. These models express systems in terms of the likelihood of each factor (or node) existing in a given state based on the direction and strength of influence from other nodes. There are three main features of a BBN before it is used for simulation; structure, discretisation and parameterisation. In some cases researchers may obviate discretisation by using continuous nodes [22], but this is rare in practical applications, and continuous nodes are usually used in conjunction with discrete nodes [2].

In the process of creating a BBN model, the researcher must first define the domain and scope of the model and arrive at some understanding of the

structure of the network. If full data are available then these can be used directly to learn the network structure algorithmically. Alternatively, Principal Component Analysis [23] can be used to reduce the dimensionality of the data before running learning algorithms, which speeds the learning process in time-critical applications. For expert-elicited and expert-informed networks the number and subject of nodes is defined by the researcher through literature review and expert consultation, as is the number and direction of arcs between nodes.

If discrete nodes are created from continuous assessments, the node must be discretised before parameterisation. Deciding upon discretisation thresholds is a difficult process, as the resulting output of the network can be highly sensitive to this choice. There is a significant amount of research on discretising nodes from data sets in the case of Learning Bayesian Networks [28], however very little has been explored in the case of expert-elicited or expert-informed BBNs [40].

The final stage in model creation is to set prior parameters for each node through a conditional probability table (CPT) that specifies the likelihood of a node's state conditional upon the states of its parent nodes. It is this parameterisation through CPTs that provides the simulation capabilities for BNs generally.

From this process there are seen to be four areas affecting uncertainty in the validity of the BBN model:

1. Structure: The nodes included in the model, and the number and direction of links between nodes.
2. Discretisation: The way the state space has been divided within nodes.

3. Parameterisation: The conditional probabilities associated with node states.
4. Behaviour: The output of the model under interrogation.

# 1.1.2. The passenger facilitation system and the IPFM structure 

![img-0.jpeg](img-0.jpeg)

Figure 1: Schematic diagram of the Inbound Passenger Facilitation Model (IPFM)

The final IPFM consists of four BBN objects linked via a queuing model (see Figure 1). Each of the network objects represents a functional area of the inbound passenger facilitation process, detailing the structure of factors affecting processing time in that area.

![img-1.jpeg](img-1.jpeg)

Figure 2: Schematic diagram of the inbound passenger facilitation system

Figure 2 shows the structure of the facilitation system in Australian airports generally. The four functional areas (see Figure 2) are referred to as:

1. Arrivals Concourse (AC): This area is where passengers enter the airport from their plane through gates. This area contains a duty free shopping store and some restrooms, but is generally just a large hall. Factors affecting facilitation time are the time spent in discretionary activities and the travel time to cover the distance between the gate and the Entry Control Point given the congestion in the area.
2. Entry Control Point (ECP): This area is where immigration checks are conducted at either manually operated modules or automated Smart-

Gate modules. In the IPFM, a passenger is considered in this model to have entered this area once they have joined the queue for processing. Every passenger entering the country must pass through this area, but some passengers will transfer to other flights before reaching this stage and are removed from the model. Factors affecting facilitation time in this area include the processing time at the checkpoints, the number of checkpoints open and the length of the queue at the time it is joined by the passenger.
3. Baggage Collection Area (BCA): Passengers collect their luggage in this area, usually from baggage carousels assigned to specific flights depending on the size of the terminal. Factors affecting facilitation include the delivery time for luggage from the flight and the accessibility of the bag given the congestion in the terminal.
4. Secondary Examination Area (SEA): In this area passengers are selected for scans and interviews regarding issues other than immigration. The SEA is divided into two areas, one controlled by Australian Customs and Border Protection Service (ACBPS) and the other controlled by the Department of Agriculture, Fisheries and Forestry (DAFF) Biosecurity Division. The few passengers interviewed by ACBPS go through a single, highly variable process. A much higher proportion of passengers are sent to the DAFF Biosecurity controlled area where additional processing may occur. Factors affecting facilitation time in this area include the processing time for each module and the length of the queue at the time it is joined by the passenger.

In testing the validity of the model, each of the networks was examined

individually where appropriate and also as a whole in the case of testing model behaviour. In the case of the IPFM, while most variables are theoretically observable, there is great expense and difficulty in acquiring timings for individual passengers through the entire system with the level of coverage required to be a representative sample. In fact, the original reason a model was developed was as a substitute for this type of data collection.

While there may be a number of options for data to support future iterations of the model, at this time there are large gaps in terminal data so we cannot meet the assumptions of traditional model validation tools. Instead we must use a broader framework of systematic questioning to incrementally build confidence in the model through comparison to other models, comparison of sub networks within the model itself and limited prediction tests where data allow.

### 1.2. Validity testing approaches for representations of unobservable phenomena

The concept of testing the validity of measures of unobservable phenomena first arose in the mid-twentieth century with researchers who were concerned with understanding how to build convincing psychological scales. Validating measures of unobservable phenomena has been a central theme in psychometrics because until the introduction of brain scanning technology there was no method available of gaining objective data on thought patterns and mental states [20]. The work carried out by these researchers became a basis for further exploration of the area. Sparse but significant work has been published on the subject of validating models in recent times, summaries of which can be found in Gu et al. [17] and Balci [4]. Recently, Bornstein [6]

called for a process-focused approach to model validation, where confidence in the model is built by systematic experimentation rather than methods examining the correlation between output and criterion. While their approach only referred to the validation of scores obtained through psychometric tests, the Pitchforth \& Mengersen [32] framework applies this same approach to Bayesian Network models which require validation of all four areas of uncertainty. Afzali et al. [1] found that very few studies reported a standard set of validation measures for models with unobservable output and introduced a reporting checklist for validity. However this checklist is specific to decisionanalytic models and focuses more on standardising the model development rather than trying to assess the final model itself. In contrast, the current paper demonstrates that the Pitchforth \& Mengersen [32] framework is applicable to a working Bayesian network model, and focusses on the actual model proposed for use rather than examining the development process.

In the following section we provide an overview of the tests found in the framework by Pitchforth \& Mengersen [32]. We then apply the validation tests to the IPFM to demonstrate that the framework can be applied to a working model of a real system, and that its application leads to a more valid representation of the system.

# 2. Methods: Overview of Validity Tests 

The validation tests used in this study are drawn from Pitchforth \& Mengersen [32], who outline a validation framework for BNs where complete data are not available.

A short description of each test in the context of the IPFM is provided

in this section. This sequence should be run after conducting a literature review and arriving at a working model of the system.

# 2.1. Nomological Validity 

This type of validity is a first step to determine the theoretical position of the model within the context of the wider modelling literature. A nomological map for a BN not only explores the general placement of the model within the literature, but does so within the context of the four areas of uncertainty.

Early nomological maps were very similar to BBNs themselves. However, in the case of writing a nomological map for a BBN, we need to acknowledge the four sources of uncertainty in BN validity. This requires some adjustment to communicate the results graphically. In the case of this map we divide the landscape into four quadrants, each representing one of the four sources of uncertainty.

![img-2.jpeg](img-2.jpeg)

Figure 3: Example layout of the Nomological Map

Three concentric circles centred on the origin of this plane represent the theoretical distance between the model in question (represented by the centre of the circles) and the models or sets of models that are considered similar to the work in question. Those models within the smallest circle are most similar to the model being validated on the dimension represented by the quadrant, while the models in the largest circle are least similar of those within the scope of literature review. By creating a nomological map in this way, we gain an understanding of which other models are useful comparisons for each source of model uncertainty.

If a model cannot be placed within the literature it indicates that more theoretical work is required to justify the arrangement of the model. On its own this test tells us little about the mechanics of the model, but gives us a framework on which to base further hypotheses. If this model is the result of extensive literature search by multiple researchers and can be shown to sit within a known body of work, the nomological validity of the IPFM meets expectations.

# 2.2. Expert based validation 

The first level of validation uses the opinion of experts to confirm that model features match their expectations in a variety of ways. The issue of criterion contamination [7], or using self-confirmation is important to deal with when using expert validation. In the case of the IPFM criterion contamination was avoided by using a subset of experts to create the initial network, then having all experts involved appraise the interpretation of this elicitation. However, there are other methods of avoiding this issue available to researchers. For example, a bootstrapping style method could be adopted wherein experts are asked individually to validate the network, then assessments can be grouped randomly to ascertain whether the judgement of any subset of experts differs significantly from any other subset. The technique applied is largely dependent on the time available to the researcher, and the predicted heterogeneity of the group of experts. In many cases the time requirement of eliciting a BN structure is already very high, so extensive validation testing based on expert opinion is not always practical. Smaller sets of experts can be used in this stage if the population is considered to be relatively homogeneous. For example, in the construction of the IPFM each

set of experts primarily had knowledge of their own area, with very little experience in others. Due to this, expert based validation required a full set of experts despite time limitations.

# 2.2.1. Face Validity 

The face validity of the model refers simply to whether the model structure, discretisation and parameters look as the experts expect them to. This approach is used to appraise the structure and discretisation of network nodes rather than the overall results of the network, as the point of interrogating the model is to discover unusual behaviour rather than simply confirm expert beliefs. Like nomological validity there are few insights we gain from this test on its own, but it must be passed in order to move onto other validation tests as it is a basis of our confidence in the strength of the model validity.

### 2.2.2. Content Validity

Content validity refers to whether the nodes and links in the networks comprehensively describe the inbound passenger facilitation system and the variables that affect its performance. This was determined by first reinterpreting the existing metric framework of the inbound system from Hargreaves [19], then developing the networks further in close consultation with the stakeholders involved in the operation of the relevant part of the system to ensure a comprehensive overview. As in many cases where the Delphi method [34] is used to elicit expert opinion, some of the nodes in the final version of the networks were found to be redundant when the flow of probability through the model was considered, so were removed to increase the content validity of the model.

These two types of validity are typically examined together, as they are both dimensions of the relationship of the BN with other models. Convergent validity is the extent to which the model matches other models of systems that are similar in some way, while discriminant validity is the extent to which the model differs to models of different systems. We use the nomological map from the first test to formulate hypotheses about the comparison models. To demonstrate the convergent and discriminant validity of the IPFM, we choose two example hypotheses:

1. The model behaviour is similar to that of existing available Agent Based Models of airport terminals.
2. The model structure is different to that of other airport process models from different countries in relevant sections.

# 2.3. Data based validation 

Data based validation is the most common type of validity testing in the literature, to the point that many researchers consider it the only true form of validation. However, for most data-based validation methods to work, a comprehensive and accurate dataset is required (taken as ground truth). One of the issues in this case study is the lack of ground truth data for some functional areas of the system, however a number of tests are still possible to run albeit in a limited capacity. Another issue is that almost every available data set cannot be truly considered ground truth as they are susceptible to error.

This type of validity refers to whether certain sub networks of the system are arranged similarly to other sub networks representing similar systems. Typically these networks are taken from alternative models that are considered nomologically proximal to the model in question based on the nomo logical map. Another way of looking at this type of validity is by examining the internal consistency of the structure, discretisation and parameters of the model as determined by nomology or expert opinion. In this case study, identifying candidate sub networks was a simple process as the system is defined formally in legal and procedural documentation. The original object oriented approach to building the IPFM has helped the model maintain good concurrent validity by reusing network structures in situations where the process was the same.

# 2.3.2. Predictive Validity 

This is the most commonly tested dimension of model validity, where the output of the model is compared to real world data. In the case of the inbound passenger facilitation system there is no objective ground truth data available, so we are limited to testing sub networks using Goodness of Fit metrics, the Extreme Conditions Test and Qualitative Features Analysis.

Goodness of fit refers to the extent to which the behaviour of the model reflects what is actually happening in the system. In the case of the IPFM there is no ground truth for the whole model, so datasets that were known to be reliable were compared against relevant sub networks and behaviour.

To do this we use metrics describing the absolute and relative error of the model when fitted to these datasets.

The root mean squared error, or RMSE [25] provides a measurement of absolute error. Formally, RMSE is defined as:

$$
R M S E=\left|\sqrt{\frac{1}{n} \sum_{t=1}^{n}\left(\hat{X}(t)-X(t)\right)^{2}}\right|
$$

where $\hat{X}(t)$ is the model estimated value at time slice $t$ and $X(t)$ is the corresponding benchmark for $n$ time slices. Another metric by which we can judge the fit of the model to the data is Mean Relative Error (MRE), formally defined as:

$$
M R E=\left|\frac{1}{n} \sum_{t=1}^{n} \frac{\hat{X}(t)-X(t)}{X(t)}\right|
$$

Reasonable thresholds should be set a priori in order to assert that these tests have been passed. These should be set with respect to the intended decision scenario for the model. There is no universally accepted threshold, but a $95 \%$ confidence interval is defensible in most cases.

In the Extreme Conditions Test we examine the behaviour of the model under extreme conditions where the outcome is logically certain. The most certain outcome for the IPFM is when no flights are arriving, where we would expect to see the four facilitation areas empty of passengers. In the context of this test, a flat line on a graph of predicted passenger numbers demonstrates that this test produces the hypothesised results. Failure to pass this test will often lead to a complete restructuring of the model before it can be retested. If model behaviour is not as expected in this test, the problem may lie with the structure, discretisation or parameterisation of the network. To determine which specific dimension of the model is at fault more specific tests are required.

Qualitative Features Analysis is an approach investigating the behaviour of the model in everyday scenarios where the difference in outcome can be logically inferred without requiring an exact hypothesis. These tests of predictive validity are less stringent than the extreme conditions test, but provide a much higher level of information about model performance. There are a range of scenarios that can be run on the IPFM, two of which are presented in this paper.

In the first test we hypothesise that a valid simulation would show that passengers are moving sequentially through the system as we can observe in the real terminal. If this is the case, we should see the arrival concourse register passengers first, then the Entry Control Point (i.e. the second area in the system) and so on. Further to this, our hypothesis would be supported if the peak passenger load of each functional area occurs in the same sequence.

Another Qualitative Features Test is to simulate the airport in a scenario in which every gate has a plane unloading at the same time, massively overloading the terminal. In this case our hypothesis is that a valid model would show very high dwell times for each area along with passenger congestion peaks occurring in the same sequence.

# 3. Results 

The results of the validation tests are presented as both evidence of the strength of the model in representing the inbound passenger facilitation system, and as a demonstration that the proposed validation framework can be usefully applied to a model of a real-world system.

# 3.1. Nomological Validity 

The nomological map for the IPFM is depicted in figure 4. Each concentric circle represents the theoretical distance between the model and work conducted by other researchers in each of the four areas of BBN uncertainty.
![img-3.jpeg](img-3.jpeg)

Figure 4: Nomological Map for the IPFM

In some cases numbers appear multiple times on the map, reflecting that


Table 1: Papers included in each group for the nomological map
the corresponding models can be used in comparisons of more than one area of uncertainty. Further to this, numbers may reflect groups of papers in some cases, but individual papers in cases where the work is particularly influential on some dimension of the current model. The papers included in each group are listed in table 1 .

Given that the model can be placed within an extensive and diverse range of literature that offers a good range of comparison models, we have confidence in the model validity for this dimension.

# 3.2. Face Validity 

Having consulted closely with the range of stakeholders involved in the inbound passenger facilitation process, we can determine that the face validity of the IPFM is acceptable. Each organisation was interviewed independently and confirmed that the model structure, discretisation and parameters fit with what is expected to be observed. In addition, experts corroborated the behaviour of the model under normal operational conditions, although this

is not counted as part of the formal validity testing framework.

# 3.3. Content Validity 

The four networks were tested against Hargreaves [19] and Manataki \& Zografos [27] to determine the comprehensiveness of the network structure. The IPFM included all relevant nodes from these models, excluding those obviated by the modelling approach. Examination of node discretisation revealed that all nodes cover their entire state space without gaps. Parameterisation was shown to cover all values present in the data so far, and the behaviour of the model was able to replicate all tested system behaviours.

As a secondary test, we also confirmed with experts that all factors considered in operational decisions are included in all relevant parts of the network structures.

### 3.4. Convergent/ Discriminant Validity

The structure of the model is similar to the hospital models identified in the nomological map, implying good convergent validity on this level. As far as is known, there are no BNs of outbound performance to compare discretisation, but the parameters of the model agree with those found in Hargreaves [19] in sections where the parameters are unlikely to have changed since publication. The behaviour of the IPFM is similar to that of Agent Based Models of airport terminals such as those by Xie et al. [41] and Schultz \& Fricke [36]. When relevant, sub networks were compared to determine that expected differences were observed. For example, the Greek passenger facilitation process is different to the Australian process and this is supported by a comparison of the IPFM with Manataki \& Zografos [27]. Similarly,

our expectation that parameters reflect the observed growth in passenger numbers since the Hargreaves [19] report was published, is supported by the model.

# 3.5. Concurrent Validity 

There are a number of queuing types represented in this model such as having one queue feeding multiple counters, many queues feeding a single counter, and multiple queues feeding multiple checkpoints. Each of these queue types is represented by similar network structures throughout the model, with the figure below presented as an example.

![img-4.jpeg](img-4.jpeg)

Figure 5: Example of two sub networks that demonstrate good concurrent validity

In addition, nodes that represent similar aspects of the system have been discretised and parameterised similarly, ensuring the model is consistent throughout its quantification. Having checked that the model is consistent internally as well as with other models, we can judge the concurrent validity of this model as acceptable.

# 3.6. Predictive Validity 

The predictive validity of the model is given by the results of the three tests outlined below.

### 3.6.1. Goodness of fit

Only the Entry Control Point (ECP) and Secondary Examination Area (SEA) networks could be tested using this metric given the available data. The available data were in the form of a count of the number of passengers departing the ECP or SEA for one minute periods over the course of the test period. The data that were available for use was for 6:00-12:00 and 16:00-20:00 (a total of 10 hours) on Sunday, September 302012 at Brisbane International Airport. The ECP count was obtained from immigration records which record the timestamp of the last keystroke when a passenger is cleared through the ECP. For the purpose of validation these data were treated as the ground truth.

On the other hand, the SEA count was obtained from video analytics on the exit of the SEA. These counts have only been corroborated with manual counts based on video footage, so cannot be seen as ground truth, but provide some comparison.

For the purposes of evaluating the goodness of fit, the cumulative count over time of passengers departing the ECP and SEA, also known as the cumulative departure curve, is used. The cumulative curve is selected rather than the actual count per minute for three reasons. Firstly, by using the cumulative count, it is possible to identify not just whether the model tracks the data accurately, but also see if it drifts away from the data over time; identification of drift is impossible with the instantaneous count. Secondly,

the 'instantaneous count can be noisy. Finally, the cumulative curve is what is used to infer the facilitation rate as well as the number of passengers in an area and the average dwell time for passengers entering an area in that time slice.

The facilitation rate is the slope of the cumulative curve. The number of passengers in the area at a given time slice can be determined by finding the vertical distance (i.e. difference) between the cumulative departure curve and the cumulative arrival curve. The average dwell time, expected at a given time slice, is the horizontal distance between the cumulative arrival and cumulative departure curves.

When tested against the ECP ground truth, the cumulative ECP departure curve predicted by the model was found to track the ground truth well (figure 6). A RMSE value of 42.2 passengers over the 10 hour simulation period was recorded along with a relative error of $5.7 \%$. Note that, due to gaps in the data, the model was not specifically trained against the ECP departure data. Hence, it can be seen that the model is highly effective in predicting passenger movement. It is surmised that this level of accuracy stems from well-informed expert based knowledge on ECP operations which was used to quantify the model.

![img-5.jpeg](img-5.jpeg)

Figure 6: Model output compared with immigration key tap data

The SEA departure curve was compared against video analytics counts supplied by the Intelligent Surveillance group of the Airports of the Future (AOTF) program. The SEA departure curve was similarly compared against data gathered through video analytics. Note that in this instance, the data are not the ground truth and the aim of this comparison is to establish whether the model predicts within the right ballpark. As can be seen from figure 7 , the model predictions generally follow the data well. In this case the RMSE of the IPFM was 70 passengers with a MRE value of $17 \%$ over the simulation period. This gives us a good indication that the model output agrees with the most direct measurements that are possible to get from the system.

![img-6.jpeg](img-6.jpeg)

Figure 7: Model output compared with video based data as provided by the Intelligent Surveillance team of the AOTF project.

# 3.6.2. Extreme Conditions Test 

In this test we hypothesised that in a scenario where no passengers enter the terminal, the model should produce a flat line of passenger numbers in each functional area over time. Figure 8 demonstrates that this is the case. Such a result can be difficult to obtain with a complex BN; by integrating a BN with a stochastic queuing theory based simulation model that enforces hard constraints, we were able to achieve the correct result.

![img-7.jpeg](img-7.jpeg)

Figure 8: Model output resulting from the Extreme Conditions Test, which matches expectations

# 3.6.3. Qualitative Features Analysis 

As hypothesised, the line representing each functional area rises, peaks and drops in a sequence expected based on the known passenger process (see figure 9). The first passengers to arrive move very quickly through the model, but as passenger flow exceeds capacity the numbers in each area build. Of particular interest is the peak hour in the morning, where the model predicts passengers in the Baggage Reclaim Hall for an extended period before they move very quickly through the SEA. Peaks in the Arrival Concourse are very sharp, and contribute slowly to the ECP, which is slightly smoother but peaks at just over 600 passengers. The Baggage Reclaim Hall then smoothes the flow of passengers further, and feeds them slowly into the SEA at first. The

sharp drop on the SEA curve reflects that passengers move quickly through the SEA once they have arrived there. These behaviours are in line with hypotheses.
![img-8.jpeg](img-8.jpeg)

Figure 9: Likely terminal performance output. Note the sequence represented by each line as passengers are depicted moving through the model.

For the second test, the Qualitative Features Analysis demonstrates that the model shows a massive overload of passengers when all flights are set to arrive at the same time ( see figure 10). We see change points in the morning when new modules are opened, and otherwise see an amplification of model curves as would be produced by introducing a number of passengers to the terminal far above plausible levels.

![img-9.jpeg](img-9.jpeg)

Figure 10: Model output resulting from the Qualitative Features Analysis in which all planes land simultaneously. Note the high peaks suggesting long queues at facilitation bottlenecks

# 4. Discussion 

This paper had two major aims:

1. To demonstrate that the Pitchforth \& Mengersen [32] validation framework can be applied to a model of a real world system, and that doing so helps to fine tune the model using practical and hypothetical scenarios; and
2. To demonstrate that there is a high level of confidence in the validity of the IPFM based on the results of validation tests.

# 4.1. The validation framework 

In its application to the IPFM, the validation framework proposed by Pitchforth \& Mengersen [32] has been demonstrated to be a useful addition to the process of creating a practical systems model either partly or entirely based on BBNs. In the case of failed tests, the result pointed the researchers quickly and unequivocally toward a model based solution that improved internal and external validity.

The application of the framework is a step forward in establishing confidence in BBN models. This step provides both an academic advantage in convincing sceptics when presenting BBNs as well as a professional advantage when presenting a model to investors or managers. By being able to demonstrate some level of confidence in the model's validity, researchers can attempt more interesting interrogations of their model and industry partners perceive a much lower level of risk in adopting the model for decision support. The application of this framework to a model of a real system demonstrates that test criteria need not be exact in a statistical sense in order to suggest exact remedies for operational problems. Statisticians are primarily concerned with accuracy in measuring model validity, however it is often the case that applied tests of working models are required to be more robust to a wider range of data than more accurate given perfect test and training datasets. This pragmatic approach allows us to draw the model closer to a representation of the system that is representative enough to be used in operational decisions.

This validation framework is useful even without formalisations of the tests included. For example, in the initial operation of the Qualitative Fea-

tures analysis it was not necessary to specify exactly how many passengers should be generated in order to determine the behaviour of the unadjusted model was inconsistent with hypothesised performance. In this case it was enough to specify that the number of passengers should be simulated such that the terminal was overloaded, and it was possible to make necessary adjustments to parameters based on these results.

While each test is simple in its execution, their results produce a reasonable model when taken as a framework. While many researchers in the past have proposed subsets of the tests in the Pitchforth \& Mengersen [32] network (for example Forrester \& Senge [12], Gingnell et al. [15], Aquaro et al. [3]), the results of the tests are most effective in tuning the model when used within this comprehensive framework. From this perspective, the focus of many researchers on goodness-of-fit is a limited view in the case of complex systems models as the validation of the model is restricted to scenarios for which full datasets have been collected. By also including expert and empirically based validity tests when examining BN models we can incorporate more information about other dimensions of validity. The framework helps avoid the criteria contamination which can occur in other model validation approaches and combines a range of concepts common in Bayesian Network and systems modelling literature such as structure pruning, parameter tuning and scenario checking into a single testing scheme. In many cases with Complex Systems modelling researchers report surprising findings in terms of emergent behaviour. However, special care should be taken when reporting such findings, as in many cases it is difficult to tell whether the model is correctly predicting behaviour that has as yet been unobserved, or is sim-

ply not reflective of the real system in the specific circumstances tested. In cases where non-intuitive emergent behaviour is discovered using a BBN, the validation framework described here provides strong guidance on whether behaviour is emergent or simply invalid. However, the subjective nature of test results means that different types of models cannot easily be compared to each other unless they are sufficiently similar. In addition, the framework is long-winded to report and can absorb a significant amount of the time experts can dedicate to the modelling effort. For a comprehensive assessment of model validation, it is required that at least one extra workshop be held for experts to contribute their opinion on the face validity of the model, and this can be difficult if researchers have not spent time building support for the modelling process amongst experts, or have already used significant amounts of expert time already.

# 4.2. Model Performance 

The final version of the IPFM satisfactorily passes all the tests outlined except for those that require more data. It should be noted that model development was an iterative process in this case study, with each new piece of expert opinion or data contributing to the next stage of model development. As Bar-Yam [5] mentions, it is more useful to focus on changes to small parts of the model at a time than on changing the whole model at once so an iterative process was more suitable. While initially failing some of the proposed validity tests, the IPFM passed all tests in the model's final iteration. Significant development was required for success following a number of failed attempts, demonstrating the use of these validity tests in improving model validity.

A good example of the framework helping to build confidence in the model's validity was the Extreme Conditions Test, which led to a major redevelopment of the overall model, including the restructuring of networks and the introduction of a queuing model to tie all networks together. This very basic but stringent test revealed that the original model predicted a small number of passengers in the system when the airport should have been completely empty. This was revealing of the behaviour of the specific model being tested as well as of BBN models in general; probabilistic interpretations of a system do not always translate neatly into physical interpretations. It was the failing of this test that led to a complete redesign of the high-level structure of the IPFM with the goal of meeting the requirements of the Extreme Conditions Test. The Qualitative Features test was also failed by the original model, as it showed no queue in the SEA in a situation where one had both been logically hypothesised and observed regularly by experts. In running this test, it was discovered that there was an issue with the parameterisation of the network representing the SEA, as the exaggerated behaviour of the overloaded area revealed that passengers moving through the direct exit needed to have some distribution of travel time attributed to them. The performance of the original model was improved by correcting these parameters.

After a number of validation interviews and testing rounds, the model was easily improved to a point that it performed acceptably well on all proposed tests. The resulting model is novel in the airport terminal simulation literature as it takes a probabilistic approach to the physical interpretation of the system, but also introduces a temporal dimension through the use of

queuing models. Having been accepted by project partners as well as passing logical and data-based validation tests, there is reason to have a high level of confidence that the IPFM is a valid representation of the Inbound Passenger Facilitation system at Brisbane International Airport, and only slightly lower confidence that the model is valid for the same system in all Australian international airports.

# 5. Conclusion 

This paper demonstrates that the proposed validation framework by Pitchforth \& Mengersen [32] can be usefully applied to a working BN model of a real world system for which output data are not available. We show that by applying the tests outlined in the framework to the four areas of BN uncertainty we can improve model validity without requiring complete and objective output data, and also provide reports to stakeholders that build their confidence that the model is a reasonable representation of the system of concern. In the application of the framework to a working model we also developed the tests further in order to make them more practical in a real-world context. This is an important contribution to the study of model validity as having a set of practical validation test results allows decision makers to defend their use of the model in daily operations, reporting and system monitoring when discussing future funding and organisational arrangements with government departments and other stakeholders. From an academic perspective, this paper is the first example of applying the framework presented in Pitchforth \& Mengersen [32] to a working BN model and demonstrates that the tests have both practical as well as theoretical impor-

tance in producing valid representations of system behaviour.

In applying these tests to a model of airport operations we also make a valuable contribution to the study of airport modelling by demonstrating that the IPFM is a useful and valid interpretation of the system's behaviour from a complex systems perspective. Using a complex systems approach through the use of a Bayesian Network model allows decision-makers to assess system behaviour in a much wider range of conditions than previous models, including consideration of factors usually overlooked such as staff rosters, passenger types and carrier characteristics. Having such a system available allows decision makers to not only produce reasonable reports of system behaviour under common conditions, but also to observe the behaviour of the passenger processing system under novel conditions.

For example, the IPFM is currently being used to assist in the creation of staff rosters to operate manual checkpoints given known flight schedules. However, in the near future new, larger plane models will be landing at the airport producing entirely different patterns of passenger arrival. Using the IPFM, decision makers can organise staff rosters and adjust processing guidelines to proactively manage these new passenger arrival patterns before the first plane has landed.

The model generally performed well on the proposed validity tests, indicating that the output is a reasonable representation of what is happening in the system from a range of perspectives. The IPFM is now in development to be used by operational managers at Australian airports through specialised user interfaces and visualisations. It should be noted that the inclusion of these validation tests in technical reports provides significant support for in-

dustry partners wishing to convince their counterparts of the utility of the model. In particular, the IPFM was designed for the use of managers associated with government regulators, who are understandably conservative in adopting new methods of prediction and assessment. In this case the inclusion of a comprehensive validation framework assisted in garnering support for model adoption, as there is now a document that can be referred to when questions of model validity arise.

Future work should focus on improving the specificity of the tests and formalising them where possible. First, while a graphical description of the nomological landscape has been developed in this paper, a numerical description would assist in more formally specifying the expectations of the researcher concerning the final network's structure, discretisation, parameterisation and behaviour. Second, this validation framework could also be used to examine the validity of expert opinion itself, as opposed to the output of the model based on such elicitation. The tests applied in this paper could also be used to check that experts are not only thinking about the phenomena in question in a logically consistent way, but also that their responses are in line with the needs of the BN modelling paradigm. Finally, the validation framework used here could be arranged as a BBN itself to allow for conditional weighting of validation tests and calculation of scores representing the strength of confidence in the validity of the model in question.

It is expected that this framework could provide grounding for a new area of research in Complex Systems model validation research as the various tests suggested are expanded, formalised and improved. In this paper we have demonstrated that the present framework is sufficient to check model valid-

ity and tune the model in cases where no ground truth data are available.

# 6. List of References 
