# Predicting Software Defects in Varying Development Lifecycles using Bayesian Nets 

Norman Fenton, Martin Neil, William Marsh, Paul Krause and Rajat Mishra

RR-05-11
December 2005
![img-0.jpeg](img-0.jpeg)

University of London
Department of Computer Science

.

# Predicting Software Defects in Varying Development Lifecycles using Bayesian Nets 

Norman Fenton ${ }^{1}$, Martin Neil ${ }^{1}$, William Marsh<br>Department of Computer Science<br>Queen Mary, University of London<br>Mile End Road, London<br>and ${ }^{1}$ AgenaLtd, London<br>norman, martin, william<br>@dcs.qmul.ac.uk

Paul Krause<br>Department of Computing<br>University of Surrey<br>Guildford, SURREY, UK<br>p.krause@surrey.ac.uk

Rajat Mishra<br>Philips Software Centre, Bangalore, India<br>rajat.mishra@philips.com


#### Abstract

An important decision problem in many software projects is when to stop testing and release software for use. For many software products, time to market is critical and therefore unnecessary testing time must be avoided. However, unreliable software is commercially damaging. Effective decision support tools for this problem have been built using causal models represented by Bayesian Networks (BNs), which incorporate both empirical data and expert judgement. Previously, this has required a custom-built BN for each software development lifecycle. We describe a more general BN, which, together with the AgenaRisk toolset, allows causal models to be applied to any development lifecycle without the need to build a BN from scratch. The model and toolset have evolved in a number of collaborative projects and hence capture significant commercial input. Extensive validation trials have taken place among partners on the EC funded project MODIST (this includes Philips, Israel Aircraft Industries and QinetiQ) and the feedback so far has been very good. For example, for projects within the range of the models predictions of defects are very accurate. Moreover, the causal modelling approach enables decision-makers to reason in a way that is not possible with other regression-based models of software defects.


## Categories and Subject Descriptors

D.2.8 [Software Engineering] Metrics - Product metrics. K.6.3 [Management of Computing and Information Systems] Software Management - Software development.

## General Terms

Management, Measurement, Reliability.

## Keywords

Causal Models, Dynamic Bayesian Networks, Software Defects, Decision Support.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee.
Conference'04, Month 1-2, 2004, City, State, Country.
Copyright 2004 ACM 1-58113-000-0/00/0004

## 1. INTRODUCTION

A number of authors, for example [3, 6, 21], have recently used Bayesian Networks (BNs) in software engineering management. In our own earlier work [8] we have shown how BNs can be used to predict the number of software defects remaining undetected after testing. This work lead to the AID tool [20] developed in partnership with Philips, and used to predict software defects in consumer electronic products. Project managers use a BN-based tool such as AID to help decide when to stop testing and release software, trading-off the time for additional testing against the likely benefit.
Rather than relying only on data from previous projects, this work uses causal models of the Project Manager's understanding, covering mechanisms such as:
poor quality development increases the number of defects likely to be present
high quality testing increases the proportion of defects found.
Causal models are important because they allow all the evidence to be taken into account, even when different evidence conflicts. Suppose that few defects are found during testing - does this mean that testing is poor or that development was outstanding and the software has few defects to find? Regression-based models of software defects are little help to a Project Manager who must decide between these alternatives [10]. Data from previous projects is used to build the BN, with expert judgements on the strength of each causal mechanism.
In this paper, we extend the earlier work by describing a much more flexible and general method of using BNs for defect prediction. We also describe how the AgenaRisk [1] toolset is used to create an effective decision support system from the BN. An important limitation of the earlier work was the need to build a different BN for each software development lifecycle - to reflect both the differing number of testing stages in the lifecycle and the differing metrics data available. Given the work required to build a BN, this severely limits the practically of the approach. To overcome this limitation, we describe a BN that models the creation and detection of software defects without commitment to a particular development lifecycle. We then show how a software development organisation can adapt this BN to their development lifecycle and metrics data with much less effort than is needed to build a tailored BN from scratch.
The contents of the remainder of the paper are as follows: in Section 2 we introduce BNs and show how they are used for causal modelling in software engineering. Section 3 introduces the idea of a 'phase' as a sub-part of a software

lifecycle and shows how several phase models can be combined to model different lifecycles. The phase model is described in detail in Section 4; Section 5 shows how it is adapted to different development lifecycles. An experimental validation of defect predictions is described in Section 6.

## 2. DEFECT PREDICTION WITH BNs

### 2.1 Bayesian Nets

A Bayesian net [13] (BN) is a graph (such as that shown in Figure 1) together with an associated set of probability tables. The nodes represent uncertain variables and the arcs represent the causal/relevance relationships between the variables.
![img-1.jpeg](img-1.jpeg)

Figure 1 BN for Defect Prediction
The BN of Figure 1 forms a causal model of the process of inserting, finding and fixing software defects. The variable 'effective KLOC implemented' represents the complexityadjusted size of the functionality implemented; as the amount of functionality increases the number of potential defects rises.
The 'probability of avoiding defect in development' determines 'defects in' given total potential defects. This number represents the number of defects (before testing) that are in the new code that has been implemented.
However, inserted defects may be found and fixed: the residual defects are those remaining after testing. Variables representing a number of defects take a value in a numeric range, discretised into numeric interval.
There is a probability table for each node, specifying how the probability of each state of the variable depends on the states of its parents. Some of these are deterministic: for example the 'Residual defects' is simply the numerical difference between the 'Defects in' and the 'Defects fixed'. In other cases, we can use standard statistical functions: for example the process of
finding defects is modelled as a sequence of independent experiments, one for each defect present, using the 'Probability of finding a defect' as a characteristic of the testing process:

Defects found $=B($ Defects inserted, Prob finding a defect $)$
where $B(n, p)$ is the Binomial distribution for $n$ trials with probability $p$. For variables without parents the table just contains the prior probabilities of each state.
The BN represents the complete joint probability distribution - assigning a probability to each combination of states of all the variables - but in a factored form, greatly reducing the space needed. When the states of some variables are known, the joint probability distribution can be recalculated conditioned on this 'evidence' and the updated marginal probability distribution over the states of each variable can be observed.
The quality of the development and testing processes is represented in the BN of Figure 1 by four variables discretised over the 0 to 1 interval:
probability of avoiding specification defects
probability of avoiding defects in development
probability of finding defects
probability of fixing defects.
The BN in Figure 1 is a simplified version the BN at the heart of the decision support system for software defects. None of these probability variables (or the 'Effective KLOC implemented' variable) are entered directly by the user: instead, these variables have further parents modelling the causes of process quality as we describe in Section 4.

### 2.2 Decision Support with BNs

Although the underlying theory (Bayesian probability) has been around for a long time, executing realistic BN models was only first made possible in the late 1980s as a result of breakthrough algorithms and software tools that implement them [13]. Methods for building large-scale BNs are even more recent ( $[11,19]$ ) but it is only such work that has made it possible to apply BNs to the problems of software engineering.
Drawing on this work in various commercial projects with Agena, Fenton and Neil have built BN-based applications that have proved the technology is both viable and effective. Several of these applications have been related to systems or software assessment. Especially significant was the TRACS tool [18] to assess vehicle reliability for QinetiQ (on behalf of the MOD) and the AID tool [20] to predict software defects in consumer electronic products for Philips. Much of the modelling work described here has been done as part of the MODIST project [9], which extends the ideas in AID. The toolset implementation has been based on Agena's AgenaRisk technology that was extended to incorporate recent developments in building large-scale BNs that was undertaken in the SCULLY, SIMP and SCORE projects [11].
Two features of AgenaRisk are especially critical for building this model:

Large tables can be handled efficiently. For example, in the default model here the number of defects may range from 0 to 3000 , in intervals of varying size.
Probability tables are generated from numerical and statistical expressions by simulation. The expression given above using the binomial distribution is not only

the conceptual model but also how the model is specified.

### 2.3 Building the BN Model

Like all BNs, the defect model was built using a mixture of data and expert judgements. Understanding cause and effect is a basic form of human knowledge, underlying our decisions. For example, a project manager knows that more rigorous testing increases the number - and proportion of - defects found during testing and therefore reduces the number remaining in the delivered software.
It is obvious that the relationship is not the other way round. However, it is equally obvious that we need to take into account whatever evidence we have about: the likely number of defects in the software following development; the capabilities of the team; and the adequacy of the time allowed. The expert's understanding of cause and effect is used to connect the variables of the net with arcs drawn from cause to effect.
To ensure that our model is consistent with these empirical findings, the probability tables in the net are constructed using data, whenever it is available. However, when there is missing data, or the data does not take account of all the causal influences, expert judgement must be used as well.

## 3. VARYING THE LIFECYCLE

When we describe defects being inserted in 'implementation' and removed in 'testing' we are referring to the activities that make up the software development lifecycle. We need to fit a decision support system to the lifecycle being used but practical lifecycles vary greatly. In this section, we describe how this can be achieved without having to build a bespoke BN for every different lifecycle. The solution has two steps: the idea of a lifecycle 'phase' modelled by a BN and a method of linking separate phase models into a model for an entire lifecycle.

### 3.1 A Lifecycle Phase

We model a development lifecycle as made up from 'phases', but a phase is not a fixed development process as in the traditional waterfall lifecycle. Instead, a phase can consist of any number and combination of such development processes. For example, in the 'incremental delivery' approach the phases could correspond to the code increments; each phase then includes all the development processes: specification, design, coding and testing. Even in a traditional waterfall lifecycle it is likely that a phase includes more than one process with, for example, the testing phases involving some new design and coding work.
The incremental and waterfall models are just two ends of a continuum. To cover all parts of this continuum, we consider all phases to include one or more of the following development activities:

Specification/documentation: This covers any activity whose objective is to understand or describe some existing or proposed functionality. It includes: requirements gathering writing, reviewing, or changing any documentation (other than comments in code).
Development (or more simply coding): This covers any activity that starts with some predefined requirements (however vague) and ends with executable code.

Testing and rework: This covers any activity that involves executing code in such a way that defects are found and noted; it also includes fixing known defects.
The phase BN includes all these activities, allowing the extent of each activity in any actual phase to be adjusted. In the most general case, a software project will consist of a combination of these phases. In Section 4 we describe the BN model for one phase in more detail. First, in the next section, we describe how multiple instances of the BN are linked to model an arbitrary lifecycle.

### 3.2 Linking Phases: Dynamic BNs

Whatever the development lifecycle, the main objective is: given information about current and past phases we would like to be able to predict attributes of quality for future phases. We therefore think of the set of phases as a time series that defines the project overall. This is readily expressed as a Dynamic Bayesian Network (DBN) [2]. A DBN allows time-indexed variables: in each time frame one of the parents of a timeindexed variable is the variable from the previous time frame. Figure 2 show how this is applied when the quality attribute is the number of residual defects.
![img-2.jpeg](img-2.jpeg)

Figure 2 A Dynamic BN Modelling a Software Lifecycle
The dynamic variable is shown with a bold boundary. We construct the DBN with two nodes for each time-indexed variable: the value in the previous time frame is the 'input' node (here 'Residual defects pre') and it has no parents in the net. The node representing the value in this time frame is called the 'output node' (here 'Residual defects post'). Note that the variable for the current time frame 'Residual defects post' depends on the one for the previous time frame, but as an ancestor rather than as a parent since it is clearer to represent the model with the intermediate variable 'Total defects in'.
As well as defects, we also model the documentation quality as a time-varying quality attribute. Recall that documentation includes specification, which even in iterative developments is often prepared in one phase and implemented in a later phase. We consider specification errors as defects so a phase in which documentation is the main activity may lead to an important incremental change in documentation quality that is passed on to the next phase.

## 4. MODELLING A SINGLE PHASE

We describe the 'phase-level BN', which models a single software development phase, first giving an overview and then describing two part of the BN in more detail.

### 4.1 Overview

The phase BN is best presented as six 'subnets', each consisting of BN variables, as shown in Figure 3, with grey arrows marking where there is at least one variable in one subnet which is a parent of a variables in different subnets. The subnet plays no part in inference but is a useful for guide for the user of the BN.
![img-3.jpeg](img-3.jpeg)

Figure 3 Subnets of the Phase BN
The subnets are:
Scale of New Functionality Implemented. Since we are to build and test some software we may be implementing some new functionality in this phase. This subnet
provides a measure of the size of this functionality.
Specification and Documentation. This subnet is concerned with measuring the amount of specification and documentation work in the phase, the quality of the specification process and determining the change in the quality of the documentation as a result of the work done in the phase (modelled as a time-indexed variable).
Design and Development. This subnet models the quality of the design and development process, which influences the probability of inserting each of the potential defects into the software.
Testing and Rework. This subnet models the quality of the testing process and the rework process, influencing the probabilities of finding and fixing defects.
Defect and Insertion and Discovery. This subnet follows the pattern already described in Section 2.1, adapted to handle changes to the number of defects using a timeindexed variable. The amount of 'new functionality implemented' will influence the inherent number of defects in the new code. We distinguish between potential defects from poor specification and 'inherent potential defects', which are independent of the specification. The number of these is a function of the number of function points delivered (based on empirical data by Jones $[14,15]$ ).

### 4.2 Specification and Documentation

Figure 4 shows the Specification and Documentation subnet. Before implementing any functionality there is assumed to be some specification of it. If we are lucky this specification will be a well-written document at the appropriate level of detail. However, in many cases it may be nothing more than a vague statement of requirements. Generally, therefore, there may be work that needs to be done on the specification as part of this
![img-4.jpeg](img-4.jpeg)

Figure 4 Specification and Documentation Subnet

lifecycle phase.
The 'scale of all new specification and documentation work in this phase' and 'spec \& doc process quality' will determine the 'adequacy of documentation for new functionality (after spec work this phase)' that is being implemented in this phase. If, for example, there is very little new functionality (and so the 'scale of new specification and documentation work' is low) then, even if the 'spec \& doc process quality' is poor, it is likely that adequacy of documentation will be sufficient. On the other hand, if there is a lot of new functionality the scale of new specification and documentation work is likely to be high, which means that the process quality will need to be good in order for the documentation to be adequate.
This subnet shows the use of 'indicator' nodes: for example the experience of the staff is an indicator of the process quality. Indicators can easily be tailored to match the information available in the software development environment - see Section 5.

### 4.3 Testing and Rework

Figure 5 shows the testing and rework subnet.
![img-5.jpeg](img-5.jpeg)

Figure 5 Testing and Rework Subnet
The better testing process the more likely we are to find the defects. We may or may not decide to fix the defects found in testing in this phase; the success of such fixes will depend on the 'probability of fixing defect'. The two probabilities are used to update the number of residual defects in the 'Defect Insertion and Discovery' subnet and to predict the number of residual defects at the start of any subsequent phase in which further development and/or testing of the software takes place.

### 4.4 Variations on the Phase Model

In principle, the phase net can describe any phase, even if it includes only some of the software development activities. A phase with no development or testing (i.e. was just specification/documentation) is modelled by setting the new functionality implemented to zero, and the development, testing and rework effort to zero.
This effectively restricted the model to the subnet concerned with specification and documentation and ensured that the
information about defects was not changed (since without coding or testing defects are neither introduced nor removed).
However, it is irksome for users to enter dummy information to ensure that certain variables are set to zero, so we introduced a set of variants of the phase BN that explicitly model the cases where at least one of the software development activities is not undertaken:

1. specification/documentation and development carried out in the phase, but not testing
2. specification/documentation and testing carried out in the phase, but not development
3. development and testing carried out in the phase, but not specification/documentation
4. only specification/documentation carried out in the phase
5. only development carried out in the phase, and
6. only testing carried out in the phase.

These BNs are constructed by selecting the relevant subnets and omitting those that are irrelevant. The BN modelling the general case is known as the 'all activities' phase BN.

## 5. APPLICATION METHODOLOGY

There are two steps for applying the defect prediction model to a specific software development environment:

1. choose the 'indicators' used to judge the qualities of the different processes
2. link together phase BNs to model the full lifecycle.

### 5.1 Quality Indicators

Indicator variables used in the BN can be customised to match the indicators used within the organisation. As well as editing names given to an indicator in the questionnaire, its probability table can be adjusted. The formula language of the AgenaRisk toolset makes this feasible. Consider, for example, the 'Testing process quality' (TPQ) shown in Figure 5. The suggested indicators are:

Quality of documented test cases
Testing process well defined
Testing staff experienced
The process quality and the indicator values are judged on a five-point scale from 'very low' to 'very high': the judgement being relative to the norm for the development environment. To set up the indicators, an expert need only judge its 'strength' as an indicator of the underlying quality attribute. Given that the process quality really is high, how certain is it that the staff will be experienced? We have found the truncated normal distribution useful for creating a probability expressing an expert's assessment of the 'strength' of an indicator. For example, suppose:

$$
\begin{gathered}
\text { Testing process well defined }=\text { TNormal('TPQ', 0.6) } \\
\text { Testing staff experience }=\text { TNormal('TPQ', 0.2) }
\end{gathered}
$$

this expresses the judgement that the staff experience is the stronger indicator, since it has a smaller variance parameter $(0.2)$ than the other indicator. In both cases the mean value of the indicator is given by the parent process quality.

### 5.2 Lifecycle Modelling

We show two examples of how the phase BN and its variants can be linked to model different lifecycles.

# 5.2.1 Iterative Development 

An incremental software lifecycle is modelled by a series of the 'all activities' phase BN. The diagram shown is Figure 6 is this is displayed in the AgenaRisk toolset.
![img-6.jpeg](img-6.jpeg)

Figure 6 An Incremental Development Lifecycle
Figure 7 shows an example of the predicted defects for this model. In increment 1, the defects before the start of the phase is set to zero and the new functionality to 50 function points; increment 2 has 250 function points and the final increment 50 function points of new functionality. Although each phase includes all the activities, the first one gives most effort to specification and the final one most effort to testing and rework. The number of residual defects falls from increment 2 to increment 3 as a result of the testing effort.

### 5.2.2 A Waterfall Example with Integration

This example, in Figure 8, shows a waterfall lifecycle but with initial development of modules 1 and 2, including some lowlevel testing, done by two separate teams, for example modelling development at different sites or the use of subcontractors.
The initial development follows different lifecycles: the two phases for module 1 being 'specification, development but no testing' followed by 'testing only', while module 2 has a specification only initial phase. This difference may represent the different way that metrics data is gathered at the two sites as well as actual lifecycle differences.
![img-7.jpeg](img-7.jpeg)

Figure 8 A More Complex Lifecycle with Two Teams
The 'join' subnet combines the defect estimates for the two modules, taking account of their relative size, before two phases of testing applied to the system as a whole. This example also shows that user trials can be modelled as a 'testing only' phase.

### 5.3 Toolset

Our experience from earlier commercial projects is that project managers and other users who are not BN experts do not wish to use a BN directly via a general purpose BN editor. Instead, the BN needs to be hidden behind a more specialised user interface. The toolset provided by AgenaRisk is actually an application generator that enables toolset users to tailor both the underlying BN models and the user interface that is
![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

Figure 9 Accuracy of the Prediction for 32 Projects
provided to the end-users when the application is generated.
The main functions provided to the end-user are:

1. Observations can be entered using a questionnaire interface, where questions correspond to BN variables. Each question includes an explanation and the user can select a state (if the number of states is small) or enter a number (if the states of the variable are intervals in a numeric range). Answers given are collected into 'scenarios' that can be named and saved. At least one scenario is created for each software development project but it is possible to create and compare multiple scenarios for a project.
2. Predictions are displayed as probability distributions and as summary statistics (mean, median, variance). Distributions are displayed either as bar charts or as line graphs (see Figure 7) depending on the type of variable and the number of states. The predictions for several scenarios can be superimposed for ease of comparison. Summary statistics can be exported to a spreadsheet.
The questionnaires shown to the end user can be configured widely. For example, questions can be grouped and ordered arbitrarily and the question text is fully editable. Not all variables need have a question, allowing any BN variable to be hidden from the end user.

## 6. VALIDATION

The toolset and models have been widely trialled by various commercial organisations, including those involved in the MODIST project, namely Philips, Israel Aircraft Industries (Tel Aviv) and QinetiQ (Malvern). In addition, Philips has recently completed a retrospective trial of thirty-two projects carried out at Bangalore.

### 6.1 Aim and Methodology

The aim of the recent Philips trial was to evaluate the accuracy of the AgenaRisk defect prediction capabilities in software projects. Initially, 116 consumer electronics software projects completed between 2001 and 2004 were assessed for inclusion in the trial against the following criteria:
reliable data was available
project resulted in a commercial product
some key people from the project were still available for interview
the projects should represent a range of product domains and a variety of design layers, including user interface, intermediate and driver layers.
Thirty-two projects were identified as suitable for the trial, based on these criteria.
A questionnaire, based on the AgenaRisk form for entering observations, was used to collect qualitative and quantitative information from key project members. This data was entered into the model to predict the number of defects found in testing. These predictions were then compared with the actual number of defects found in all testing phases. Data was collected in two rounds: in the second round a more detailed interview was conducted with the 'Quality Leaders' for each project resulting in improved data and improved predictions.
The trial used a variant of the 'all-activities' phase-level net. The single BN was used since it was not possible in this retrospective trial to separate the defect data into separate phases.

### 6.2 Results

The main results of the trial were:
For code sizes between 10 and 90 KLOC , the predictions for defects found were exceptionally accurate (inaccuracies are less than $30 \%$ ).

The best predictions (inaccuracy $<20 \%$ ) were obtained for code sizes between 50 and 87 KLOC.
For code size $<5$ KLOC the prediction inaccuracy was more than $70 \%$.
For code sizes between 5 and 10 KLOC and greater than 90 KLOC , the prediction inaccuracy was between $40 \%$ and $80 \%$.
The relative inaccuracies outside the range 10 to 90 KLOC were inevitable given that the default used has been configured only for code between 20 to 80 KLOC .

### 6.3 Lessons from the Validation

![img-10.jpeg](img-10.jpeg)

Figure 10 Stub Phase for Existing Code
The validation also showed the need to ensure that the model closely matches the situation. For example, the inaccuracies for projects outside the range of the default model are largely explained by the 'defects pre' variable, representing the number of defects before the (one and only) development phase. Unless a value is explicitly entered here, a default value is assumed, which heavily biased the defect predictions upwards for the smaller projects and may also bias the prediction downwards for larger projects.
Although it is easy to enter a value in the AgenaRisk toolset, we did not provide a systematic method to determine the appropriate value. Many of the projects in the trial enhanced existing software, so the initial defects was not expected to be zero. This problem was easily overcome within the modelling method we have described by explicitly modelling the preexisting code, using a simple stub phase (no specification, development or testing), as shown in Figure 10.

## 7. CONCLUSIONS

We have shown how a wide variety of software lifecycles can be modelled using a Dynamic Bayesian Net, in which each time frame is a lifecycle 'phase' combining all software development activities in different amounts. This approach allows a BN for software defect prediction to be tailored to different software development environments. The AgenaRisk toolset makes this a practical approach, providing a formula language with standard statistical distributions which can be used to change the quality indicators available in each software development team.

The approach and toolset have been extensively trialled by industrial partners in a collaborative project. Despite making little use of the available tailoring capabilities, a retrospective trial of 32 projects showed a good fit between predicted and actual defect counts.
The AgenaRisk toolset allows the use of large variable state spaces that are necessary to achieve accurate predictions, with the formula language making the construction of very large probability tables feasible. However, discretisation errors can still be a problem especially when the net is used for problems of widely varying scale, as was shown by the projects in the retrospective trial. The AgenaRisk toolset now incorporates dynamic discretisation $[16,17]$ to overcome this problem.
We have also used AgenaRisk to reason about software projects as a whole [9] and the trade-off between time, resources and quality. Many of the factors are common in these two models, covering both the assessment of process quality and the product quality achieved and required. In future, we hope to combine the two models into a single decision support system for software projects. Part of this is being done in the eXDecide project [5].

## 8. ACKNOWLEDGMENTS

This report is based in part on work undertaken on the following funded research projects: MODIST (EC Framework 5 Project IST-2000-28749), SCULLY (EPSRC Project GR/N00258), SIMP (EPSRC Systems Integration Initiative Programme Project GR/N39234), and SCORE (EPSRC Project Critical Systems Programme GR/R24197/01). We also acknowledge the contributions of individuals from Agena, Philips, Israel Aircraft Industries, QinetiQ and BAE Systems.
