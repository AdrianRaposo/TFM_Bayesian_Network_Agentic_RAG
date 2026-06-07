![img-0.jpeg](img-0.jpeg)

This item is the archived peer-reviewed author-version of:

An approach for reconciling different perspectives and stakeholder views on risk ranking

Reference:

Goerlandt Floris, Reniers Genserik. - An approach for reconciling different perspectives and stakeholder views on risk ranking
Journal of cleaner production / Masson - ISSN 0959-6526 - 149(2017), p. 1219-1232
Full text (Publisher's DOI): https://doi.org/10.1016/J.JCLEPRO.2017.02.129
To cite this reference: https://hdl.handle.net/10067/1415950151162165141

# An Approach for Reconciling Different Perspectives and Stakeholder Views on Risk Ranking

#### Abstract

Risk ranking is a widely used technique for selecting and prioritizing multiple risks facing an organization or decision maker. In industrial practice and in academic work, risk ranking methods are commonly based an implicit risk conceptualization, adopting a particular foundational perspective and accounting for selected factors. Nevertheless, different stakeholders may adhere to various risk conceptualizations, applying different foundational perspectives and accounting for different factors in the ranking process. Identifying a gap in the literature to coherently consider these different foundations, this paper presents an approach for reconciling different foundational perspectives and stakeholder views, accounting for uncertainties about these. The approach is presented based on three foundational perspectives (the expected value, uncertainty and moral perspective), and developed as a Bayesian Network - Influence Diagram. The main use of the model is to make possible controversies in risk prioritization explicit, facilitating stakeholder deliberation. The model can easily be extended with new perspectives on risk ranking, or adapted based on additional knowledge about other aspects, e.g. relating to risk perception. The graphical representation allows insights into the contribution of various aspects, facilitating the selection of appropriate risk management actions. The developed model is applied to an example, suggesting that the envisaged benefits of the proposed approach are plausible. It is concluded that the novel approach has a clear potential for reconciling different foundational perspectives and stakeholder views on risk ranking. Nevertheless, it is stressed that the conceptual contribution made in this paper should be more elaborately tested in practical settings, substantiating the findings further.


# KEYWORDS 

Risk ranking; expected value, uncertainty; moral considerations; foundational issues

## WORD COUNT

8166 words

# 1. INTRODUCTION 

In risk research, there is a recent focus on foundational issues addressing concepts, theories, principles and terminology (Aven and Zio 2014). One fundamental issue is how to rank different risks, which is of considerable importance for prioritizing and selecting risks for risk treatment. Communities face a range of risks, ranging from natural hazards such as tsunamis to technological hazards such as oil spills from shipping accidents and social hazards such as crime and riots. Many organizations apply sequential (also known as "ad hoc") risk ranking, i.e. they wait until a risk draws their attention and then put effort and resources in better understanding and managing that risk (Meyer and Reniers 2013). Thus, priority is given temporarily to these risks, drawing away awareness and resources from other risks. The success of sequential risk ranking depends on the number of risks faced, the processes how these attract attention, how fast uncertainty about them can be reduced and how precise the ranking needs to be (Long and Fischhoff 2000). While such an approach may lead to an acceptable situation, there is a clear risk that a focus on vivid minor risks leads to neglecting more serious ones, thereby resulting in more negative consequences which may have been avoided by more proactive risk management strategies (Fischhoff and Morgan 2009).

Another approach, in focus in this paper, is simultaneous risk ranking. Here, all relevant risks are considered at once, which requires comparisons of their relative importance, thus informing treatment policies aimed at making best use of the limited available resources (Meyer and Reniers 2013). Developing frameworks and practical methods for guiding this selection is a fundamental issue and several methods to this effect have been proposed, for instance for life-cycle risk management (Ayoub et al. 2015) and sustainable development (Sovacool et al. 2016). Risk matrices are widely used tools, recommended in various industries (IMO 2010; ISO 2010; NHS 2008). Recommendations for their design and use have been made also in scientific environments (Duijm 2015; Goerlandt and Reniers 2016; Ale et al. 2015; Flage and Røed 2012). Other approaches for risk ranking include qualitative risk scoring methods (Deisler 1997; Gardoni and Murphy 2014),

environmental comparative risk assessment techniques (Morgenstern et al. 2000; Andrews et al. 2004), multi-criteria decision analysis (Brito and de Almeida 2009; Linkov et al. 2006; Li et al. 2009) and deliberative methods (Florig et al. 2001; Morgan et al. 2001; Susel et al. 2016).

One issue which has been identified as a challenge in risk ranking is the existence of a multitude of risk definitions (Fischhoff and Morgan 2009), an issue raised also elsewhere in the literature (Hampel 2006; Slovic 1999). Different underlying risk conceptualizations and corresponding risk perspectives for analyzing and ranking risks can lead to different risk rankings and subsequent prioritization for risk management. In the context of risk ranking, not much explicit attention has been given to the existence of different foundational perspectives, and methods are lacking to make disagreements on this level explicit and to overcome these. Some approaches mentioned above take note of this risk-conceptual challenge (Fischhoff and Morgan 2009; Gardoni and Murphy 2014), but subsequently present a risk ranking approach based on a particular conceptualization of risk.

In contrast, the contribution made in this paper is to formulate a model to incorporate and reconcile different foundational perspectives on which aspects are relevant in risk ranking. The presented model is flexible to include different stakeholder views on the foundational perspectives and the specific considered aspects, while also accounting for uncertainties in their measurement. The model assists in a deliberative stakeholder process for risk ranking by making the possible disagreements about risk foundational issues explicit and by offering an easy approach to determine risk scores and ranks according to different foundational views. Despite the existence of various foundational risk perspectives, no methods are known to exist which focus on reconciling these.

The remainder of this article is organized as follows. Section 2 outlines selected risk foundations, focusing on three risk perspectives derived from these foundations. Section 3 presents the model for integrating these perspectives for a stakeholder-driven risk ranking. Section 4 presents an example application illustrating its applicability. A discussion follows in Section 5. Section 6 concludes.

# 2. RISK FOUNDATIONS: PERSPECTIVES ON RISK 

There are various controversial issues underlying the risk analysis discipline. One instance is the realist-constructivist schism, where realists are convinced that technical risk estimates constitute true representations independent of the convictions of the involved analysts, whereas constructivists believe that risks are mental constructions relative to a social group (Shrader-Frechette 1991; Bradbury 1989; Thompson and Dean 1996). A related fundamental question is whether, and how, public concerns and moral aspects of risk imposition should be accounted for in risk management, or whether factual and/or expert knowledge alone should be the guiding principle (Rosa 1998; Perhac 1996; Liobikiené and Juknys 2016; Qin et al. 2016).

These issues relate to the perspective taken for describing, measuring and/or ranking risk, which in turn is based on different conceptualizations of risk. Three different risk foundations are briefly outlined next. The corresponding risk scoring procedures are elaborated further in Section 3.2, where these are incorporated in the Influence Diagram model.

### 2.1. Expected value perspective

In technical risk analysis, risk is commonly defined as the statistical expected value of probabilities and consequences of an undesired event (Faber and Stewart 2003; Campbell 2005). This expected value is the weighted sum of all possible consequences of the action, where the weights are given by the probability associated with each consequence. It is thus a two-dimensional, quantitative concept, which lends itself to mathematical treatment. Decision making according to this perspective is in line with the utilitarian strategy, which defines rationality as taking actions which optimize the expected utility (Shrader-Frechette 1991). In risk descriptions, this perspective focuses on the knowledge dimension as the determination of probabilities of occurrence and associated consequences is based on data, expert judgments and engineering/natural science models. In

contrast, perceptual, moral or cultural aspects attributed to risk in other conceptualizations are omitted from the perspective (Thompson and Dean 1996; Shrader-Frechette 1991; Rosa 1998).

# 2.2. Uncertainty perspective 

While widespread, the expected value perspective has been criticized for not sufficiently accounting for uncertainties in the risk quantification. Different uncertainty classification systems have been proposed, e.g. distinguishing aleatory and epistemic uncertainty (Parry 1996), endodoxastic and metadoxastic uncertainty (Hansson 2006) and evidential and outcome uncertainty (Levin 2005).

The main issue especially in focus in the latter classification system is the need for a systematic treatment of uncertainties in the background knowledge, because probabilities (or other measures of uncertainty) are ill-suited to convey information about the strength of the evidence on which these measurements are based (Flage et al. 2014). Assumptions underlying the risk analysis can lead to significant deviations between the quantified consequences and how these actually might occur, and classical expected value perspectives are argued to be ill-suited to deal with such uncertainties. Hence, in the uncertainty-perspective for risk analysis and risk ranking, focus is on events/consequences and their associated uncertainties (related to outcome and evidence). Such perspectives start from an understanding of the risk concept as consisting of events, consequences of human value, and associated uncertainties (Aven and Renn 2009). Variations of this perspective exist and different methods for conveying the strength of evidence and the importance of underlying assumptions have been proposed (Goerlandt and Reniers 2016; Berner and Flage 2016).

### 2.3. Moral perspective

A final considered perspective also steps away from probability-based thinking and more broadly accounts for moral (or ethical) considerations relevant in risk management. In particular, apart from the probability and consequence dimension of classical risk perspectives, the risk source is accounted for in the risk concept (Wolff 2006; Gardoni and Murphy 2014). Thus, risk is understood as a multi-dimensional, hierarchical concept, which lends itself for focus on both the consequences

and the probabilities, as well as the source of risk events. Here, the risk source refers to the agent(s) whose actions create or help to maintain risks. The source dimension is argued to capture a central public concern about morality, namely, how a risk is created and sustained (Shrader-Frechette 1991; Stern and Fineberg 1996). That is, risks created through negligence or recklessness can be considered more important than risks where such moral responsibilities are not relevant. Rather than the incurred consequences, morally blameworthy behaviors of agents constituting the risk source can be the focus of the risk event when it occurs, leading to blame, reputation damage and shame (Wolff 2006; Gardoni and Murphy 2014; Kermisch 2012a).

# 3. RECONSILING PERSPECTIVES: AN INFLUENCE DIAGRAM MODEL 

In this section, the proposed model for reconciling the different risk perspectives and stakeholder views is presented. First, the main premises underlying the model are presented. Subsequently, the modeling approach is briefly introduced and the resulting Influence Diagram model presented. For reasons of brevity, the risk scoring methods and the subdimensions considered therein are only described very summarily, referring to the original papers where these methods are elaborated.

### 3.1. Underlying premises

A first premise in constructing the model for determining a risk ranking is that different foundational perspectives currently co-exist and have been argumented for. These are based on different views on the nature of the risk concept, giving varying importance to uncertainties and moral aspects in risk management besides probabilistic risk estimates (Aven and Renn 2009; Kermisch 2012b; Wolff 2006). Here, it is taken that the various perspectives capture, based on their respective foundational understandings, relevant characteristics for prioritizing risk events for risk management. Moreover, it has been argued that the adherence to different risk conceptions by different stakeholder groups is influenced by the social and institutional context in which these operate, i.e. that defining risk is an exercise in power (Thompson and Dean 1996; Slovic 1999).

Consequently, while arguing for specific risk concepts and risk ranking methods is considered worthwhile and important, it is likely that different conceptualizations are deeply rooted in different communities and organizations so that different stakeholders may disagree on the appropriate foundations for risk ranking. This is in line with the premises dynamics of social institutions: 'individuals negotiating their way through the organizational constraints of actively interpreting, challenging, accepting, and recreating their social environment are limited to a style of discourse consistent with the constitutive premises of that environment' (Rayner 1992). In other words, organizational commitments can lead members of their organizations to be 'forced' to work with certain risk perspectives, due to a priori commitments made by their organization. This can be, for instance, due to different industry guidelines for risk definitions and risk rankings (IMO 2010; NHS 2008; ISO 2010), which can differ across organizations or stakeholder groups (Bradbury 1989; Shrader-Frechette 1991; Thompson and Dean 1996). Additionally, practitioners from different fields can adhere to rather diverse disciplinary discourses in dealing with risk, which may differ again from the general public's understanding, from which disagreements on risk perspectives can result (Althaus 2005; Hampel 2006).

Hence, accepting the reality of different risk conceptualizations, it is considered useful to create a model for integrating different risk perspectives. Such an integrated model can make disagreements on foundational issues explicit, it can be further used to evaluate the significance of these disagreements in relation to the resulting risk rankings and can thus provide a platform for reconciling different views on risk-foundational issues.

A second premise is that different stakeholders do not necessarily agree about the measurements of the (sub)dimensions in the risk ranking methods (Apostolakis and Pickett 1998). For instance, one stakeholder may find the consequences fairly distributed and may find that risks are voluntarily taken, whereas another does not share these views. The importance of different stakeholder views in risk ranking has also been acknowledged in earlier work especially on deliberative and multi-

attribute methods (Florig et al. 2001; Morgan et al. 2001; Susel et al. 2016; Li et al. 2009). Consequently, the model incorporates the views of multiple stakeholders, both related to the adherence to different foundational perspectives, as well as to the measurement of the (sub)dimensions considered in the risk ranking methods.

Third, the use of the model for ranking risks is clarified, where a view is adopted that it has a primarily heuristic usefulness. In other words, the ranking resulting from the model is not taken as a final prioritization, but rather as an input of a subsequent stakeholder review and discussion. Thus, the model has several uses, in line with ideas presented by Hodges (1991). First, it acts as a bookkeeping device for summarizing the knowledge about the different risks and stakeholder views. The model can summarize multi-dimensional knowledge about the risks in an easily accessible format, an issue of convenience. Second, it provides a platform for communication, as the graphical component presents a transparent display of the salient features of the different risks in the stakeholders' view. This is useful because the different dimensions of risks can be important to select appropriate risk management actions, and because techniques for visually representing these different dimensions in e.g. risk diagrams have limitations due to visual clutter as soon as several dimensions are shown (Flage and Røed 2012; Goerlandt and Reniers 2016). Third, the model and its outcome act as an aid to thinking, providing a platform for subsequent deliberative risk ranking, as in an earlier proposed multi-attribute risk ranking method (Li et al. 2009). These above uses have been argued to be acceptable for non-predictive models (Hodges 1991).

There are several reasons why the ranking resulting from the model is not taken as final. First, the approach acknowledges the importance of deliberation as recommended in several publications on risk management (Stern and Fineberg 1996; Apostolakis and Pickett 1998), also in context of Bayesian Network modeling (Bertone et al. 2016). Deliberation overcomes causes for mistrust, increases understanding, and brings new insights to the stakeholders. This is especially important

because different risks with similar total ranks may require, due to unequal contributions of different subdimensions, alternative risk management actions.

Furthermore, the model uses present a way to overcome its inherent limitations, as it could be argued that not all relevant aspects of risk ranking are included in the model and that the risk scales developed in earlier work are not perfectly ranking the risks due to inherent limitations of the risk scales. This also relates to arguments about the inherent subjectivity in risk analysis (SchraderFrechette 1991, Meyer and Reniers 2013), where many simplifying choices and assumptions are made. Given the different roles of risk analysts, decision makers and stakeholders in risk-informed decision-making, it is essential that the different actors agree on the followed procedures and that there are mechanisms in place to overcome possible disagreements (Rosqvist 2010; Stern and Fineberg 1996).

Finally, it is well documented that a ranked index resulting from weighing various dimensions involves conceptual challenges and should be carefully applied (Cardona 2005; Carreño et al. 2007; Simpson 2006). Thus, the calculated risk scores suggest a ranking rather than declaring the risks to be of a certain definite severity.

# 3.2. Influence Diagram model for reconciling risk ranking methods 

### 3.2.1. Modeling approach

The second premise of Section 3.1, describing a simultaneous entertainment of different beliefs by multiple stakeholders, is accounted for through a modeling approach capable of efficiently dealing with uncertainty. Bayesian Networks (BNs) are efficient, relatively simple and accessible also to non-experts, and therefore widely applied tools to model uncertainties about phenomena.

In Bayesian statistics, prior probabilities and likelihoods are applied to produce posterior probabilities. A BN model uses Bayesian probabilistic thinking to describe relationships between variables (Darwiche 2009). Such models can be extended to an Influence Diagram (ID) by also

including variables for decisions and/or the utilities of these (Howard and Matheson 2005). In this regard, IDs are useful tools to develop utility rankings. An attractive feature of BNs and IDs is their simple graphical representation as an acyclic graph with nodes and arcs. Chance nodes represent probabilistic state variables, processes or functions, whereas utility nodes are used to assign utilities to specific states, and arcs represent a probabilistic dependency between the nodes. The mathematical basis of BNs and IDs is well documented in the literature (Darwiche 2009; Howard and Matheson 2005), and is not further elaborated here.

From the first premise given in Section 3.1, it follows that each foundational perspective and risk ranking method can be understood as an alternative hypothesis about the issues involved in risk ranking, with the possibility that different stakeholders attach different levels of credibility to these. In risk modelling, the alternative hypothesis approach for accounting for model uncertainty is wellknown (Zio and Apostolakis 1996). Similarly, the weighted risk score (WRS) of the different models can be summarized as follows:

$$
W R S=\sum_{i=1}^{N} p_{i}\left(R S i \mid M_{i}\right)
$$

where $\mathrm{M}_{\mathrm{i}}$ is a model for risk ranking, RSi the risk score (i.e., a utility) according to model $\mathrm{M}_{\mathrm{i}}$, and $\mathrm{p}_{\mathrm{i}}$ a subjective probability assigned to the model, which can be interpreted as a measure of its credibility. In the model described below, various stakeholders can assign different credibility levels to each model.

# 3.2.2. Overall model 

The model integrating the three outlined foundational perspectives is shown in Fig. 1. The variable Risk Event is a parent variable which is used to propagate the information about the identified risks to the various dimensions considered in the risk perspectives. Stakeholder has a similar role, and additionally enables the different stakeholders to encode their support for the three considered foundational perspectives. The corresponding variable Foundational Perspective links to the three

risk scales, to enable calculation of their respective contribution to the weighted ranking, i.e. it acts as a weighing variable between alternative hypotheses. The risk ranking models corresponding to the three foundational perspectives are grouped under the submodel variables Risk Scale 1, Risk Scale 2 and Risk Scale 3. These submodels are presented in more detail in Section 3.2.3. to 3.2.5. Finally, the variables RS1, RS2 and RS3 show a numerical rank based on an assigned value function, and WRS shows a weighted score derived from the three scales according to the weights given to each foundational perspective.
![img-1.jpeg](img-1.jpeg)

Fig. 1 Overall model for risk scoring according to different perspectives

# 3.2.3. Risk Scale 1: Expected value perspective 

The risk ranking according to the expected value perspective proceeds according to a straightforward procedure. First, the probability about the occurrence of events and their consequences is determined based on data, expert judgments and/or engineering models. Then, the probabilities and consequences are binned into ranges and risks are ranked into low, medium and high risk, based on a multiplication of the probability and consequence dimension as in risk matrix approaches (NHS 2008; Meyer and Reniers 2013).

The above procedure is converted into an Influence Diagram model as shows in Fig. 2. For each risk event, the CPTs corresponding to the variables Probability and Consequences are recorded based on the results of the preceding risk analysis. A further inference between Probability and Consequence results in a value for Risk based on the rationale of the classical risk matrix approach. The CPT of the variable Risk is shown in Fig. 3. The states of the variable Consequence (minor, adverse, severe and catastrophic) are defined using the classification proposed in the corresponding variable in the risk scale according to the moral perspective (Gardoni and Murphy 2014), to ensure compatibility.
![img-2.jpeg](img-2.jpeg)

Fig. 2 Submodel for Risk Scale 1: expected value perspective

Finally, a numerical value for the risk ranking is derived based on the probabilistic variable Risk. For reasons of compatibility of the scale applied in the risk scale according to the moral perspective (Gardoni and Murphy 2014) (see Section 3.2.5), a score ranging from 1 to 10 is constructed, as follows:

$$
R S 1=\frac{9}{2}\left(\sum_{i=1}^{3} p_{i} u_{i}\right)+1
$$

Where $\left\{p_{1}, p_{2}, p_{3}\right\}=\{P($ low $), P($ medium $), P($ high $)\}$ the probabilities of the states of the variable Risk, and $u_{i}$ the utility assigned to these states to convert these in a one-dimensional value. Here, following values are adopted to construct the scale from 1 to 10: $\left\{u_{1}, u_{2}, u_{3}\right\}=\{0,1,2\}$.

![img-3.jpeg](img-3.jpeg)

Fig. 3 CPT for variables Risk in Risk Scale 1

It is noted that to avoid linguistic ambiguity, which is a well-known issue in risk assessment (Johansen and Rausand 2015), the scales of the variables Probability and Consequence should be carefully concretized. We here refer to the definitions given by Gardoni and Murphy (2014), and to Appendix A where this is issue is further addressed.

# 3.2.4. Risk Scale 2: Uncertainty perspective 

The risk ranking method corresponding to this uncertainty perspective proceeds according to the following procedure (Abrahamsen et al. 2014). First, uncertainty about the occurrence of events and their consequences is measured using probabilities interpreted as an assessor's degrees of belief in light of available evidence, through an uncertainty model (e.g. event/fault trees or Bayesian Networks). Then, risks are provisionally ranked in to low, medium and high risk, using a qualitative scale for uncertainty and consequence as in a classic risk matrix approach. Subsequently, the strength-of-knowledge underlying the measurement of the risk events is determined using a qualitative scale where an assessor judged the joint evidential support by data, experts, models and assumptions. Using these assessments, the baseline risk ranking is moved up one category for risk events with a low or medium strength of evidence.

The above procedure is translated into an Influence Diagram as shown in Fig. 4. For each risk event, the CPTs corresponding to the variables Probability, Consequence and Strength of Evidence are recorded based on the results of the uncertainty model and the qualitative strength of evidence

assessment scheme. A further inference between Probability and Consequence leads to a Baseline Risk as in a classical risk matrix approach. The variable Risk is determined starting from the Baseline Risk, updated with knowledge about the Strength of Evidence. The CPTs of the variables Baseline risk and Risk are shown in Fig. 5, and are determined based on information in the original literature on the risk scale according to the uncertainty perspective (Abrahamsen et al. 2014). The states of the variable Consequence (minor, adverse, severe and catastrophic) are defined based on the classification proposed in the corresponding variable in the risk scale according to the moral perspective (Gardoni and Murphy 2014), to ensure structural compatibility with that method.
![img-4.jpeg](img-4.jpeg)

Fig. 4 Submodel for Risk Scale 2: uncertainty perspective

The numerical value for the risk scale RS2 is derived using the same procedure as shown in Section 3.2.3. In particular, use is made of Equation (2) in assigning a risk score between 1 and 10 based on the variable Risk.
![img-5.jpeg](img-5.jpeg)

Fig. 5 CPTs for variables Baseline risk and Risk in Risk Scale 2

As noted in Section 3.2.3, to avoid linguistic ambiguity, the scales of the variables Probability, Consequence and Strength of Evidence should be carefully concretized. We here refer to the definitions given by Gardoni and Murphy (2014) and by Abrahamsen et al. (2014), and to Appendix A where specific terminology is given for selected variables as illustration.

# 3.2.5. Risk Scale 3: Moral perspective 

In the moral perspective, a risk ranking is determined based on three dimensions: probability, consequences and the risk source. Each of these is further composed of several subdimensions.

In the operationalization of the risk source, three subdimensions are identified. A first dimension is causation and responsibility, recognizing the differences between direct and indirect causation. In direct causation, the risk would not exist but for a direct human action, e.g. in routine daily tasks, recreational activities or in activities involving artefacts created by humans. In indirect causation, the risks are influenced by our actions, but are not under our control in the sense that we can choose to eliminate or no longer permit such risks (Gardoni and Murphy 2014). The second subdimension of the risk source concerns whether a risk is voluntary or involuntary. A voluntarily incurred risk occurs when an individual understands the risk he is exposing himself to, is competent in making risk decisions and agrees to incur a given risk. A risk is involuntary if these conditions are not fulfilled (Cranor 2007). The third subdimension addresses the relation between who is put at risk and who caused the risk. Some activities impose a risk to oneself, whereas other activities put other individuals at risk through one's activities (Cranor 2007). When risks are imposed on others, judgments about the acceptability of such imposition often differs depending on whether the party bearing the burden caused by risk imposition also is in a position to gain from this imposition (Shrader-Frechette 1991).

The operationalization of the probability dimension in the moral perspective, accounts for the probability of the risk event, as well as the associated confidence in the probability estimates

(Gardoni and Murphy 2014). In this regard, this perspective thus has similarities to the uncertainty perspective by also considering the evidential strength for the probability assignment. However, in the uncertainty perspective, the strength of evidence addresses both probability and consequence dimensions.

The consequence dimension is finally composed of the magnitude of the consequences and the fairness of their distribution (Gardoni and Murphy 2014). Starting from a capabilities-based approach (Murphy and Gardoni 2006), the magnitude of the consequences is defined here as a function of the change in capabilities and where individuals in the relevant population end up with respect to certain tresholds of capabilities. Four consequence categories are retained: minor, adverse, severe and catastrophic consequences (Gardoni and Murphy 2014). The fairness of the distribution of the consequences addresses another moral dimension. Some risks are created and shared in a reasonably equitable manner, whereas other risks are primarily borne by one or several stakeholder(s). An equitable distribution does not necessarily mean that the distribution of consequences is equal across a population, but it does imply that they are fairly distributed. Inequitable distribution means that the consequences are not fairly distributed across a population. For further insights in the fairness of distribution, the literature is referred to (Shrader-Frechette 1991; Gardoni and Murphy 2014).

The risk ranking method corresponding to this moral/ethical perspective proceeds according to following procedure (Gardoni and Murphy 2014). First, a scale for each risk dimension is derived from tabulated levels for combinations of their relevant subdimensions. Then, giving equal importance to each risk dimension, the resulting risk scale is determined based on the subscales of the three subdimensions.

The above procedure is translated into an Influence Diagram as shown in Fig. 6, which shows the overall risk scale based on the three subdimensions. The variables Risk Event and Stakeholder are

used as parent nodes to propagate information about the aspects considered in the three subdimensions. The Probability Subscale, Consequence Subscale and Source Subscale are submodels which are represented in more detail in Fig. 7. Each of these submodels result in a subscale, which is combined to an overall risk ranking in the variable Risk Scale. Finally, a numerical value for the risk ranking is derived in the variable Risk Scale 3, using a scale ranging from 1 to 10 as in the original source (Gardoni and Murphy 2014). The corresponding CPT is shown in Fig. 8. For reasons of compatibility with the scales resulting from the expected value perspective (Section 3.2.3.) and the uncertainty perspective (Section 3.2.4.), and for allowing weighting these scales based on the stakeholders' views on the foundational perspectives, a continuous score is constructed, as follows:

$$
R S 3=\sum_{i=1}^{10} p_{i} u_{i}
$$

Here, $p_{i}$ are the probabilities of the states of the variable Risk Scale and $u_{i}$ the utility assigned to these to convert these in a one-dimensional value. The values $u_{i}=i(\mathrm{i}=1, \ldots, 10)$ are adopted.
![img-6.jpeg](img-6.jpeg)

Fig. 6 Submodel for Risk Scale 3: moral perspective

Fig. 7 shows the BNs constructed for the subdimensions according to the moral perspective, based on the description provided in the original source (Gardoni and Murphy 2014). In the Probability Subscale, the information encoded in the variables Probability and Strength of Evidence is used to determine the Probability Scale, based on the corresponding CPT shown in Fig. 8. In the

Consequence Subscale, an inference is made about the Consequence Scale using the information in the variables Consequence and Distribution of consequences and the CPT shown in Fig. 8. In the Source Subscale, an inference is made between the variables Voluntariness and Relationship between who causes the risk and who is put at risk, determining the scale for the variable Involvement. Together with the variable Causation, this leads to the state of the Source scale. All CPTs for the source subscale are shown in Fig. 8.
![img-7.jpeg](img-7.jpeg)

Fig. 7 Models for the probability, consequence and source subscales in Risk Scale 3

![img-8.jpeg](img-8.jpeg)

Fig. 8 CPTs for variables Consequence scale, Involvement, Probability scale, Risk scale and Source scale, in Risk Scale 3

As noted in Section 3.2.3, to avoid linguistic ambiguity, the scales of the variables in the Probability Scale, Consequence Scale and Source subscale should be carefully concretized. We here refer to the definitions given by Gardoni and Murphy (2014), and to Appendix A where specific terminology is given for selected variables as illustration.

# 4. APPLICATION: ILLUSTRATIVE EXAMPLE 

The model for the different risk scales is applied to a number of generic risk events, with characteristics as shown in Fig 9 for the expected value (Scale 1) and uncertainty perspective (Scale 2), and as shown in Fig. 10 for the moral perspective (Scale 3). The choice to use generic risk events for illustrating the model's applicability is made primarily to focus on the underlying modeling approach rather than on specific application cases, in line with the intended contribution to generic methods and approaches underlying the risk analysis discipline. Nevertheless, to make the example more concrete, one risk event (RE4) is described in further detail in Appendix B.
![img-9.jpeg](img-9.jpeg)

Fig. 9 CPTs for considered aspects of example risk events, Risk scale 1 and 2;
abbreviations as in Fig. 5

![img-10.jpeg](img-10.jpeg)

Fig. 10 CPTs for considered aspects of example risk events, Risk scale 3;
abbreviations as in Fig. 8

The model described in Section 3.2 is applied to these risk events under following credibility levels the three assumed stakeholders assign to each foundational perspective (FP):

- Stakeholder 1: $\mathrm{p}(\mathrm{FP} 1)=1, \mathrm{p}(\mathrm{FP} 2)=0, \mathrm{p}(\mathrm{FP} 3)=0$
- Stakeholder 2: $\mathrm{p}(\mathrm{FP} 1)=0, \mathrm{p}(\mathrm{FP} 2)=1, \mathrm{p}(\mathrm{FP} 3)=0$
- Stakeholder 3: $\mathrm{p}(\mathrm{FP} 1)=0, \mathrm{p}(\mathrm{FP} 2)=0, \mathrm{p}(\mathrm{FP} 3)=1$

The assumption of complete adherence to the different foundational perspectives is made because different scholars have argued for such perspectives (Campbell 2005; Faber and Stewart 2003; Abrahamsen et al. 2014; Gardoni and Murphy 2014), i.e. these authors would likely adhere to their view on the issues involved in risk ranking. Moreover, this choice most clearly shows how different perspectives result in different risk rankings, thus showing the use of the developed model.

Table I shows the risk scores and associated risk rankings for the risk events (RE) with characteristics shown in Fig. 9 and Fig. 10, for the three considered stakeholders (SHs) and associated views on the appropriate foundational risk perspectives according to Equation (4).

The weighted risk score (WRS) results from the model of Section 3.2.2 as a weighted average of the risk scores of the three stakeholders, according to the weight given to each stakeholder. In this illustrative example, each stakeholder is given equal weight. The weighted risk rank (WRR) is the ordinal ranking of the risk events corresponding to the WRS.

As an alternative aggregate scoring and ranking method, the Borda algorithm can be used. This algorithm is mainly used in voting problems, but has also been applied in risk management contexts (Meyer and Reniers 2013; Ni et al. 2010; Garvey 2009). It assigns a linearly decreasing Borda score to the risk events according to their ranked risk scores as obtained for each stakeholder. Thus, for a given stakeholder, the risk events are first ranked according to their risk scores. Then, the highest ranked risk event receives a Borda score (n-1), with n the number of risk events. The second-highest ranked risk event gets a Borda score (n-2), and so on, until the lowest-ranked risk event, which receives Borda score zero. In case risk scores are tied, an average of the two Borda scores corresponding to the ranks of the risk events is assigned to each of these. Finally, the Borda scores are added across stakeholders (ABS, aggregate Borda score) and a corresponding ranking produced (ABR, aggregate Borda rank). This Borda method by construction assigns equal importance to each stakeholder.

Table I Risk scores and risk rankings for the specified risk events


Notes: $\mathrm{RE}=$ risk event, $\mathrm{SH}=$ stakeholder, $\mathrm{WRS}=$ weighted risk score, $\mathrm{WRR}=$ weighted risk rank, $\mathrm{ABS}=$ aggregate Borda score, $\mathrm{ABR}=$ aggregate Borda rank

From the results, it is seen that the different risk scoring methods, which correspond to the different foundational perspectives, lead to quite different risk rankings. While the risk ranking generally speaking decreases for lower number risk events, there are rather important differences in the assigned risk scores for specific risk events. For instance, for RE2 and RE4, Risk Scale 2 (adhered to by SH2) leads to very high risk values compared to the other rating schemes, due to the high importance given to the evidential strength in the uncertainty perspective. While the moral perspective also accounts for the evidential strength (although only through the probability of event occurrence), the corresponding effect is not very large. In cases where the evidential strength is high (as in RE1, RE3 and RE5), the expected value (SH1) and uncertainty (SH2) perspectives result in the same risk scores. In contrast, the moral perspective (SH3) differentiates these events based on the risk source, particularly due to the causation, voluntariness and distribution of consequences.

The weighted scoring and rankings between the stakeholder views, along with the scores according to the individual stakeholder views, can be used as a basis for discussion between the stakeholders. In the given illustrative example, the ranks according to WRR and ABR coincidentally result in the same risk ranking as the expected value perspective, but in general different rankings can result compared to the individual risk scales according to the different foundational perspectives.

Apart from understanding each other's priorities for the risk ranking based on the model outcome, the graphical nature of the model, shown in Fig. 11 for RE3, makes it rather easy for the stakeholders to understand the contributions of the features of the risk events in the risk ranking. In this regard, the model can be used to quickly and easily bring forward the information about the risk events encoded in the CPTs. Insights gained from selecting the desired model states can assist the deliberative process for agreeing on a final risk ranking between the stakeholders. Information about the risk events provided in tabular form as in Fig. 9 and Fig 10. can also provide certain insights, but the inferences made through the model according to the risk scales provides extra information in an accessible format.
![img-11.jpeg](img-11.jpeg)

Fig. 11 Graphical display of the Source submodel, applied to for RE3

Insight in the salient features of the risk events can also help in defining risk management actions. For instance, for risks which receive a high risk ranking because of an unfair distribution of the consequences, management efforts can focus on improving the fairness dimension. Another example concerns risk events which have a high risk ranking due to the presence of evidential uncertainty with respect to the consequences. For such cases, risk management actions can constitute increased research and development efforts for better understanding the processes involved or by developing better consequence models.

# 5. DISCUSSION 

One important premise underlying the construction of the model for integrating foundational risk perspectives and corresponding risk ranking is that different perspectives can be adhered to by different stakeholders. The inherent plausibility of the perspectives and the social dynamics of organizations can be reasons for this, see Section 3.1. However, it is also a fact that some risk perspectives have received much criticism. Especially the expected value perspective and corresponding risk scoring has been criticized, e.g. because it cannot distinguish risks with high probability and low consequences from risks with low probability and high consequences having the same expected value (Aven and Zio 2014), because it is insensitive to the uncertainties surrounding the assessment (Abrahamsen et al. 2014; Fischhoff and Morgan 2009), or because it lacks moral dimensions related to responsibilities (Kermisch 2012a; Gardoni and Murphy 2014). In risk management, moral considerations such as impacts on social and human rights are increasingly in focus (van der Ploeg and Vanclay 2017). Moreover, where risk scores are derived from a tabulation similarly as in risk matrices, the limited resolution of the categories leads to loss of information, also known as "risk ties" (Cox 2008).

Focusing on the issue of uncertainty, a useful distinction can be made between 'Type-I', 'Type-II' and 'Type-III' risks, which is applied especially in the organizational accident risk management literature (Meyer and Reniers 2013; Reniers and Sörensen 2013). The distinctions are useful because these types require different risk analysis techniques and risk management approaches (Meyer and Reniers 2013; Klinke and Renn 2002). Here Type-I risks are accidents which occur rather frequently within organizations, because of which there is relatively much historical data and experience available within the organization. This concerns mainly occupational accidents, i.e. personal injuries and health-related incidents. Type-II risks are larger-scale accidents, which may affect larger parts of the organization and beyond. Examples are large-scale explosions and fires. Such accidents occur occasionally in the wider industry, such that they do not come as a complete

surprise in the sense that these risks are conceivable. Nonetheless, uncertainties about their occurrence are much larger, and even though mathematical approaches exist for analyzing and managing those risks, these are based on strong assumptions and rely extensively on expert judgments with different levels of evidential support. Various interpretations exist for Type-III risks, also known as black swans (Haugen and Vinnem 2015; Paté-Cornell 2012), but they can be understood as are extreme events which are "unthinkable" in the sense that people are not capable of (or not mentally ready for) realizing that such events may really occur, because there is no data or knowledge available to convincingly point to its possibility.

It is clear that not all foundational risk perspectives and corresponding risk scales of Section 2 can appropriately distinguish these risk types. The uncertainty and moral perspectives can be argued to account for this through the inclusion of an aspect related to the strength of evidence in the risk ranking. However, an exact understanding of what "low", "medium" and "high" evidential uncertainty means and how to delineate these categories in practical applications requires more research (Aven and Zio 2014), whereas subsequent proposals have addressed this issue in more detail (Goerlandt and Reniers 2016; Berner and Flage 2016).

One approach for distinguishing between Type-I and Type-II risks is presented by Reniers and Van Erp, who propose a method based on a matrix which maps combinations of information availability and variability (Reniers and Van Erp 2016). This 'risk type matrix' is illustrated in Fig. 12.
![img-12.jpeg](img-12.jpeg)

Fig. 12: Risk type matrix based on Variability and Information availability (Reniers and Van Erp 2016)

The matrix of Fig. 12 can be set up and employed by an organization to determine the risk type, and thus the approach which is to be followed to tackle the risk. Area $A$ will be most difficult to deal with, while area $D$ will be easiest for decision-making. An organization can also modify the basic idea shown in Fig. 12, as shown in Fig. 13. The qualitative scales for information availability and variability can then be elaborated and refined, as in Fig. 13 using the labels 'very low', 'low', 'very limited', 'limited', 'adequate', etc.. The matrix can then be used to distinguish the different areas $A$, $B, C, D$. These areas can be used to determine which analysis technique(s) should be employed in the decision making process with respect to the risks relevant for the organization.
![img-13.jpeg](img-13.jpeg)

Fig. 13: Illustrative example of matrix for determining the operational risk type
(Reniers and Van Erp 2016)

Another issue is the ambiguity in the understanding of what classifies as a Type-III (or black swan) event. Referring to discussions on this topic (Haugen and Vinnem 2015; Paté-Cornell 2012),

disagreements e.g. arise over for which reference group the risks are (in-)conceivable and about whether these risks concern surprises relative to "anything in the past" or "relative to our knowledge" (Haugen and Vinnem 2015), which are small but lead to significantly different interpretations of what qualifies as Type-III risk. In either case, the evidential strength would likely be classified as "low" in the risk ranking methods according to the uncertainty (Section 3.2.4) and moral (Section 3.2.5) perspectives. However, then the distinction between low strength of evidence for Type-II risks and Type-III risks is not clear, even though these would require different types of risk management (Meyer and Reniers 2013; Klinke and Renn 2002). Consequently, more research is needed on more precisely defining how to distinguish Type-II and Type-III risks in relation to the low strength of evidence, and how to improve the risk scales to better account for these distinctions.

Arguably, it would be a noble aim for the risk research community to develop a unified perspective to risk ranking. This could be achieved by discarding some of the existing perspectives by successfully arguing for or empirically showing the supremacy of one of these, or by developing a new unifying one. However, given the sometimes strong adherence to particular perspectives, this may not be easily achievable, if even possible at all. Given the existence of, and adherence to different views, the developed model seems a plausible way to increase focus on foundational issues in practical risk management, by explicitly accounting for the different views on the appropriateness of given perspectives.

The developed model can assist deliberative risk ranking by providing a in a fast and easy approach to rank risks according to different foundational perspectives and stakeholder views. Where other scientific work has developed and proposed specific risk scales (Abrahamsen et al. 2014; Campbell 2005; Gardoni and Murphy 2014; Florig et al. 2001; Fischhoff and Morgan 2009), the developed model fills a gap in the literature on risk ranking by explicitly accounting for different views. By making the possible disagreements explicit and through the visual modeling approach which makes the contributing aspects of the risk events easily identifiable, mutual understanding between

stakeholders can be improved and a final risk ranking determined. However, this also necessitates that the users of the risk ranking model understand the BN method sufficiently well to use it in a deliberation. Providing explanations of the conclusions of a BN can be viewed as presenting inference results in a manner that enhances the user's insight into how these results were obtained (Suermondt 1992). The issue of explanation has been elaborately discussed by Lacave and Díez (2002), and e.g. methods based on argumentation theory have been proposed to support explanation (Timmer et al. 2017). While the success of the explanation of the proposed approach to risk ranking likely is an important aspect of the acceptability and trust by stakeholders and decision makers, this issue is left for future research.

Contrary to existing models for risk ranking, the developed model allows a probabilistic description of the variables in the risk ranking models. This explicit treatment of uncertainty in the states can be relevant in situations where members of a given stakeholder group have different beliefs about the specific states, or where various interpretations about specific aspects of the risk event can occur. In the examples of Section 4, this uncertainty is explicitly accounted for e.g. for the variables Causation and Strength of evidence in risk Scale 3, see Fig. 10. The difficulty of drawing clear limits between e.g. voluntary and involuntary risks has been raised as well in the literature (Cranor 2007), and also in such cases the simultaneous assignment of a truth-value to mutually exclusive states can be a useful model features to overcome such challenges ${ }^{1}$. Similarly, assessing the likely moral issue of causation, and in particular whether the risk event is caused intentionally, through negligence, recklessness or whether no such morally blameworthy causes are relevant, can be difficult. This is especially the case in complex systems, where multiple agents work in a multilevel control structure to keep the system within acceptable safety limits (Dekker 2011). The Bayesian paradigm upon which the presented integrated risk ranking model is based, can efficiently

[^0]
[^0]:    ${ }^{1}$ For instance, citizens living in an apartment complex prone to landslides can be taken to make a voluntary choice to live there (e.g. to live close to work), but may also have little alternatives due to too high costs of living in other residential areas. In the model, this could be treated by assigning different probabilities to the states of the variable Voluntariness in Risk Scale 3.

propagate uncertainties about the risk events throughout the model, leading to an explicit incorporation of different views about the various states in the final risk scores. In the overall model as shown in Section 3.2, it is taken that the risk aspects considered in the expected value and uncertainty ranking methods are independent from stakeholder judgments, unlike for the moral perspective. The reason for this is that the former perspectives are typically based on an understanding that risk analyses are performed by risk analysts and experts, without stakeholder involvement (Kermisch 2012a; Abrahamsen et al. 2014). This link can however easily be incorporated as well for these perspectives, if so desired.

Furthermore, it should be stressed that the risk ranking methods included in the presented model are not the only ones existing, as outlined in the introduction. In the context of this paper, this selection and restriction is made primarily for reasons of brevity and clarity of presentation of the chosen perspectives and the overall approach. Evidently, the proposed modeling approach can easily be extended to more risk ranking methods. The modeling approach through BNs and IDs moreover is very flexible to develop new risk ranking methods which account e.g. for issues related to economical aspects (Reniers and Sörensen 2013), risk perception (Slovic 1999; Fischhoff and Morgan 2009), trust and social acceptance (Kermisch 2012a; Kermisch 2012b).

A final issue, which the authors would like to stress, is that the model is presented primarily as a new conceptual approach to reconcile different perspectives and risk ranking mechanisms, to fill a gap in the reconciliation between different perspectives on risk ranking. As argued above, the underlying risk ranking methods may be in need for further refinement and empirical testing, and as such are not the focus of the presented work. In addition, the approach itself as presented is a conceptual contribution in that it has not been tested in actual stakeholder processes, using actual risk events and corresponding stakeholder judgments. Such empirical testing clearly is important, as is also the issue of the explanation to stakeholders and decision makers. These issues however are left for future research.

# 6. CONCLUSIONS 

This paper has presented and illustrated a new model for integrating different stakeholder views and foundational perspectives on risk ranking. A Bayesian Network model was created integrating ranking methods based on the expected value, uncertainty and moral perspectives, which was extended to an Influence Diagram to arrive at a risk score per perspective and a weighted ranking. The model has a straightforward use to condense knowledge about many risk events, in which the graphical display offered by the graph structure is a matter of convenience to highlight the salient features of each risk event. The main intended use of the model is however to assist in a deliberative stakeholder process, where the risk scores and rankings resulting from the model are inputs to arrive at a finally agreed ranking between stakeholders. The model is applied to a set of example risk events, clearly illustrating that the same events can be ranked quite differently when different foundational views are adhered to. In making such differences explicit, the model can assist the stakeholder deliberation process, whereas the scores and rankings and can be used to reconcile different views by increasing understanding of the aspects considered relevant in the foundational risk perspectives the stakeholders adhere to. The model can enhance understanding of the aspects contributing to the rankings. The proposed approach can be extended to include other perspectives for risk ranking, and can easily be adapted to new insights in this research area. The main intended contribution of this work is conceptual in the sense that a new conceptual modeling approach is presented for reconciling stakeholder perspectives on risk foundational issues. In that sense, it is stressed that the approach has not yet been extensively tested with actual risk events in stakeholder processes. This important work is left for future research.

# LIST OF ABBREVIATIONS 


## ACKNOWLEDGEMENTS

The research presented in this paper has been conducted in the context of the "Strategic and Operational Risk Management for Wintertime Maritime Transportation System" (BONUS STORMWINDS) project. This has received funding from BONUS, the joint Baltic Sea research and development programme (Art 185), funded jointly from the European Union's Seventh Programme for research, technological development and demonstration, and from the Academy of Finland. The work has also received financial support through the "REliability and Safety Engineering and Technology for large maritime engineering systems" (RESET) project, which is part of the H2020 Marie Skłodowska-Curie Research and Innovation Staff Exchange programme.

## APPENDIX A

As discussed in Section 3.2.3, 3.2.4 and 3.2.5, the scales of the variables applied in the risk scales should be carefully concretized in practical settings, to avoid linguistic ambiguity. In principle, the exact terminology applied can be adapted to specific application domains, where e.g. consequences relate to fatalities, environmental damages or costs. Examples from such applied scales are given e.g. by Li et al. (2009), IMO (2010) and ISO 1776:2002 (ISO 2002). Referring also to Gardoni and Murphy (2014) and Abrahamsen et al. (2014), some examples of explanations for the scales of selected variables of Risk Scale 2 (uncertainty perspective) and Risk Scale 3 (moral perspective).

Table A.I Scales for variable Strength of evidence of Risk Scale 2,
based on Abrahamsen et al. (2014)


Table A.II Scales for variable Consequence of Risk Scale 3,
based on Murphy and Gardoni (2006) and Gardoni and Murphy (2014)


Table A.II Scales for variable Distribution of consequences of Risk Scale 3


# APPENDIX B 

As a practical illustration of the risk ranking approach, the risk of a large-scale oil spill from maritime transportation in the Gulf of Finland during the winter season is taken, from the viewpoint of responsible oil response authorities. Referring to Fig. 9 and Fig. 10, the case corresponds to RE4. It should be stressed that while the below elaboration is partly based on quite extensive risk analyses and selected information sources, some parts (mainly relating to Risk Scale 3) are purely for illustration purposes and may not correspond to the views of any actual stakeholders.

The Gulf of Finland is an intensely navigated sea area, and large volumes of oil are transported especially from Russian oil terminals. During wintertime, the sea area is characterized by a complex and dynamic ice cover, and the ships navigating in the area are subjected to the Finnish-Swedish Winter Navigation System. In practice, this means that ships have to conform to certain technical and operational requirements to be allowed to trade and receive support in the area, and that various information systems are in place to support the traffic (Valdez Banda et al. 2016). The Gulf of Finland boasts a valuable but vulnerable ecosystem, which may be severely impacted in case of oil spills (Leiger et al. 2012).

Focusing on the risk of oil spill in wintertime conditions, it is known that navigational accidents in winter conditions occur relatively frequently (Goerlandt et al. 2017). Accidents leading to oil spill are very rare, mainly due to the operational profile of winter navigation operations, but large-scale oil spills are possible (Valdez Banda et al. 2016). The only significant accidental spill to date, involving the Runner 4, involved a relatively small amount of spilled oil. However, due to the complexity of dynamic sea ice and the challenges in recovering oil, large parts of the Estonian coast were polluted with oil (Wang et al. 2008). Based on the analysis by Valdez Banda et al. (2016), the probability of a large scale oil spill is taken as 'medium', defined as in Gardoni and Murphy (2014) within a range of $10^{-3}$ and $10^{-2}$. The corresponding consequences are taken as 'adverse' or 'severe'

(definitions as in Table A.II) with equal probability, as the ecosystem may recover from the pollution in better or worse condition, and economic consequences may be significant but are not catastrophic. In the example of RE4 in Fig. 9 and Fig. 10, it is taken that stakeholders disagree about the strength of evidence for making the probability assignment. Mostly, the strength of evidence is taken as 'medium' (with definitions as in Table A.I), but different stakeholders are taken to rely on different sources of information (the risk analysis referred to above, the accident of the Runner 4, or own judgments) to arrive at the probability assignment, acknowledging the different epistemic import these information sources provide.

In Risk Scale 3, the distribution of consequences in case of a large scale oil spill is taken as equitable, as it is considered that in oil spills in ice conditions can occur in Finnish, Estonian and Russian waters due to the maritime transport taking place in all three. All parties have an equitable share in the risks, and cross-border cooperation is needed to control the risks (HELCOM 2009). Similarly, the relation between who causes the risk and who is put at risk is taken to be selfimposed, as the nations allowing oil transportation to take place in their sea areas are responsible for taking the risk of oil pollution to their ecosystems. The voluntariness is in RE4 mostly considered 'fully voluntary', which means that the organizations are robustly aware of the given risk and have extensive ability to control the exposure to the risk. In the example of Fig. 10, all stakeholders believe the awareness is robust, and two stakeholders believe the Finnish Swedish Winter Navigation System is extensively able to prevent accidents, while the response authorities have extensive ability to collect spilled oil. However, one stakeholder finds that only some degree of control is in place over the risk, due to the inherent difficulty in accident prevention and due to the complexity of collecting oil from dynamic ice, and consequently finds the voluntariness 'partially voluntary'. Finally, the causation is univocally considered 'inculpable' by all stakeholders. Accident causation in complex socio-technical systems such as the maritime transportation is a complex phenomenon, where recklessness, negligence and intentional wrongdoing are in principle

possible. However, the stakeholders here adhere to an understanding that in the given area, with the reputation of the shipping companies trading there and the security measures in place, accidents would occur despite the best intentions of the actors involved.

For the above described RE4, the corresponding model inputs for the relevant variables are given in Fig. 9 and Fig. 10. The resulting risk scores and risk ranks are shown in Table I.
