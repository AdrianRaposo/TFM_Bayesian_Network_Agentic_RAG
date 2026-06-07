# Development of a model based on Bayesian networks to estimate the probability of sheep lice presence at shearing 

B. J. Horton ${ }^{\mathrm{A}, \mathrm{F}}$, D. L. Evans ${ }^{\mathrm{B}}$, P. J. James ${ }^{\mathrm{C}}$ and N. J. Campbell ${ }^{\mathrm{D}, \mathrm{E}}$<br>${ }^{\text {A }}$ DPIW Tasmania, PO Box 46, Kings Meadows, Tas. 7249, Australia.<br>${ }^{\text {B }}$ Department of Agriculture \& Food WA, PO Box 609, Denmark, WA 6333, Australia.<br>${ }^{\text {C }}$ Animal Research Institute, Department of Primary Industries and Fisheries, 665 Fairfield Road,<br>Yeerongpilly, Qld 4105, Australia.<br>${ }^{\text {D }}$ Department of Primary Industries Victoria, 475 Mickleham Road, Attwood, Vic. 3049, Australia.<br>${ }^{\text {E }}$ Present address: 5 Anka Close, Eltham, Vic. 3095, Australia.<br>${ }^{\mathrm{F}}$ Corresponding author. Email: brian.horton@dpiw.tas.gov.au


#### Abstract

This paper describes the development of a model, based on Bayesian networks, to estimate the likelihood that sheep flocks are infested with lice at shearing and to assist farm managers or advisers to assess whether or not to apply a lousicide treatment. The risk of lice comes from three main sources: (i) lice may have been present at the previous shearing and not eradicated; (ii) lice may have been introduced with purchased sheep; and (iii) lice may have entered with strays. A Bayesian network is used to assess the probability of each of these events independently and combine them for an overall assessment. Rubbing is a common indicator of lice but there are other causes too. If rubbing has been observed, an additional Bayesian network is used to assess the probability that lice are the cause. The presence or absence of rubbing and its possible cause are combined with these networks to improve the overall risk assessment.


## Introduction

Current advice is not to treat sheep for lice unless lice are present (Armstrong et al. 2001). However, there is always some uncertainty regarding whether lice might be present but have not been detected (James et al. 2001). As a result many sheep flocks are treated with lousicides after shearing, even when the manager does not believe that lice are present (Horton et al. 2002; James and Riley 2004; Reeve and Thompson 2005).

Lice can be difficult to detect, since $\sim 2500$ lice per sheep are needed to observe an average of one louse per 10 cm wool parting (James and Moon 1999) and in the early stages of an infestation only a few sheep in the mob may have lice (James et al. 2002). Lice reproduce slowly so there may be a low likelihood of detecting an infestation that began several months earlier (James and Crawford 2001) especially if an insecticide was applied. Therefore, if there is a risk of the presence of lice, the decision to treat 'just in case', may be reasonable.

If lice are present but are not treated at shearing they can cause significant reductions in wool cut and attract penalties for cotting and staining. Wilkinson et al. (1982) found losses in total value of $8-23 \%$ depending on the degree of infestation, Niven and Pritchard (1985) losses of up to $28 \%$ and Cleland et al. (1989) losses of $13 \%$. In addition, a long wool treatment may be required to minimise further production or wool value losses. This can be expensive, labour intensive and will increase the likelihood of unacceptable levels of insecticide residues in the wool clip (James 2002). Making the correct decision on whether to treat for lice or forego treatment at shearing therefore has significant implications for wool producers.

The use of Bayesian networks (Charniak 1991) is a method of combining information that is related to the probability to be
estimated. Robertson and Wang (2004) have given a detailed description of the use of a Bayesian network for irrigation decisions. This system combined a range of items of information (some of which were not known with absolute certainty) to assist decisions on the selection of irrigation systems for dairy farms. Bayesian networks allow a calculation of probability to be made at any point during data entry, so they are ideal for situations where information is incomplete. They are also useful where there is an extra cost in time or money in obtaining complete information since they can indicate whether the result would change if more information was available.

This report describes the development of a model utilising Bayesian networks to determine the risk that lice may be present at shearing to assist producers in deciding whether or not to treat for lice. The model does not carry out a full economic analysis. It is intended to be part of a larger decision support system including information on current lousicides, pesticide residue implications (Campbell and Horton 2002) and other information about lice management (LiceBoss 2008).

## Methods

Lice may be present in a flock for various reasons including:
(i) an infestation was not eradicated at the previous shearing;
(ii) lice have entered with purchased sheep, or other sheep deliberately brought onto the property; and
(iii) lice have entered with stray sheep, including strays from the home property returned by neighbours.

Although Crawford et al. (2001) showed that lice could be transferred on the footwear or clothing of shearers or other sheep

handlers in close contact with sheep, the risk is considered low in most situations and has not been included here.

Each of the above risks is considered independently using a Bayesian network. If sheep are rubbing then another network is used to assess the probability that lice caused the rubbing. All these separate networks are combined for an overall risk that lice are present.

## Bayesian networks

Fig. 1 shows the network to determine the likelihood that lice are present at the current shearing because they were present at the previous shearing, but were not eradicated. The assessment of lice at the previous shearing is based on the manager's statement about the presence or absence of lice at that time, adjusted by whether or not any lice treatment has been applied in recent years. The
![img-0.jpeg](img-0.jpeg)

Fig. 1. Bayesian network diagram representing decisions associated with the probability that lice were present at shearing and were not eradicated by treatment. In all figures the unshaded squares relate to information that the user may enter. Information in shaded squares must be estimated by the model.
effectiveness of any treatment applied is determined by a series of questions specific to the chemical and method used.

Fig. 2 shows the three networks for calculating the probability that lice entered with purchased sheep. Sheep returning from agistment are included here. Separate questions relating to the treatment of purchased rams, ewes and other sheep are asked, assuming that ram breeders are less likely to have lice than general sheep traders and that purchased stock are likely to be treated differently.

Fig. 3 shows the three networks for the probability that lice entered through straying sheep, either the neighbours' strays entering or strays from the property leaving and then returning. Separate questions are asked relating to neighbours that are believed to be free of lice, those that are known to have lice and those for which there is no information. This allows for managers who take greater care of fences beside high-risk properties, or who find strays but know the source to be unlikely to have lice.

If rubbing has been observed in any sheep then the network in Fig. 4 is used to determine the probable causes of rubbing. Even if rubbing has an obvious cause other than lice, this does not mean that lice are not also contributing, or lice may be present at low levels but not yet causing wool damage.

Fig. 5 shows the combination of all networks to assess the risk that lice are present for any, or several, reasons and that this result is consistent with the presence or absence of rubbing.

The program works through the network in the direction of the arrows, since all arrows in a Bayesian network must go in the same direction (i.e. no recursion). At each node in the network, the value may be known either because the user entered a value or because it is fixed by information obtained at a previous node. If the value is unknown, then it is assigned based on the relevant probability allowing for all information decided at previous nodes. The model returns the probability of lice due to each of the three separate possible causes and the overall probability that lice are present.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Bayesian network diagram representing decisions associated with the probability that lice were brought in with purchased sheep. The same set of decisions are replicated independently for (a) rams, (b) ewes and (c) other sheep, providing independent probabilities for each group.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Bayesian network diagram representing decisions associated with the probability that lice entered with straying sheep. The same set of decisions are replicated independently for (a) neighbours believed to be free of lice, (b) neighbours with no information about lice status and (c) neighbours known to have lice or with a high probability of having lice, providing independent probabilities for each group.

## Probability of eradication

## Years since last treatment

Plant and Dawson (1999) reported that properties that did not treat for lice had a lower lice prevalence than flocks that were treated. If the manager did not treat for lice at the previous shearing and lice are not obvious at the current shearing then
the probability that they were present 12 months ago is low. Therefore, if the manager says that no treatment was used the probability of lice at the previous shearing is set at $3 \%$, although this will be increased if rubbing is present. If they last treated more than 2 years previously then it is assumed that only new entry and not treatment failure needs to be considered.

## Lice present at the previous shearing

If the sheep were treated at the last shearing then an estimate is made of the probability that lice were actually present at that shearing. This estimate is then modified according to the likelihood of eradication by any treatment that has been applied.

The program user may indicate that:
(i) lice were definitely present at the previous shearing;
(ii) the manager is sure lice were not present;
(iii) the manager is not sure whether or not lice were present; and
(iv) there is no information about the lice status at the last shearing.

In the first case, the probability of lice at the previous shearing is $100 \%$. Surveys by Morcombe et al. (1996) found that lice were present in $\sim 10 \%$ of cases where the managers indicated that their property was louse free. However, their survey studied the manager's belief and the actual lice presence at the current shearing. The question asked by the program relates to the manager's belief that lice were present at the previous shearing. If the manager had believed lice were not present at the previous shearing when they were actually present then in
![img-3.jpeg](img-3.jpeg)

Fig. 4. Bayesian network diagram to assess the probable cause or causes of rubbing.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Combination of all Bayesian networks to assess the probability that lice are currently present in the flock, allowing for consistency with the presence or absence of rubbing. The light shaded sections are the outputs from the networks in Figs 1 to 4 and the dark shaded node gives the overall probability of the presence of lice.
most cases they would have been detected by the following shearing. Therefore the figure used for the risk of lice in case (ii) is $6 \%$. In the same surveys, lice were present in $\sim 50 \%$ of cases for properties where managers were unsure and this figure is used in case (iii). This is different from (iv), where there is no information and the local lice prevalence is used.

## Treatment applied

All treatments registered for use off-shears or in short wool have been shown to be highly effective against lice when used correctly on susceptible lice populations. However, there are many issues relating to standard of application and factors such as achieving complete muster, standard of shearing, rainfall after treatment and chemical resistance may affect the likelihood of eradication.

Morcombe and Young (1993) estimated that in $35 \%$ of infested flocks treated off-shears or in short wool, the treatment did not kill all the lice. This corresponds to a probability of eradication of $65 \%$. Users can accept this figure or work through a series of questions required to obtain a more precise answer.

The program asks questions specific for the method selected to determine whether the treatment was carried out exactly according to registered procedure. If any deficiencies in the method are identified then the probability of eradication is reduced accordingly. Where possible, the probability of success for any procedure is based on published studies of dipping or treatment methods, although estimates by lice treatment experts were required for some situations.

## Shower dipping

Lund et al. (1996) studied the effect of shower nozzles, pressure, boom height and rotation on the degree of wetting of the sheep. The relative wetting has been used to derive approximate probabilities of eradication if the optimum conditions are not used.

## Plunge dipping

Downing (1994) and Lund et al. (1997) reported the effect of swim length and number of dunks on the degree of wetting of the sheep by plunge dipping. Their results were used to derive approximate probabilities of eradication if the swim length was less than 9 m or sheep were not dunked twice.

## Split shearing

Morcombe and Young (1993) found that of properties with lice that had a single shearing, $31 \%$ failed to eradicate lice, whereas on those with split shearing failure to eradicate was $38 \%$. Therefore, the probability of eradication with split shearing is only $90 \%$ of the probability of eradication without split shearing.

## Purchased sheep

This section includes all sheep deliberately introduced to the property, whether purchased, agisted or returning from agistment or loan. Properties that trade in sheep will be exposed to sheep from several other flocks and this can increase the risk that some introduced sheep will have lice. Properties that purchase ewes on an annual basis will have a risk related to the source of ewes. If they purchase each year only from a single source their risk will be lower than those that purchase at auction. Ram suppliers are more likely to try to remain free of lice (Horton and Champion 2001). They are less likely to introduce other sheep and some producers breed their own rams primarily to avoid the introduction of any sheep (Horton and Champion 2001).

If the incidence of lice on all properties is $x$ then each different supplier has a probability $x$ of being infested with lice. If there are introductions from $n$ different sources, then the risk of lice $=1-(1-x)^{n}$.

The model uses the local lice prevalence as the risk for general sheep purchases, a lower risk for breeding ewe suppliers ( $70 \%$ of local prevalence), then lower again for ram suppliers ( $30 \%$ of local prevalence). These values are estimates, based on reports that stud breeders take more care to avoid lice

(Horton and Champion 2001) and may need adjustment by advisers for local conditions. If the sheep are purchased from a regular supplier who is 'known' not to have lice, the probability that the stock do actually have lice is set at $5 \%$. The risk of lice may be reduced further by quarantine, inspection or treatment.

Sheep brought onto the property may be quarantined for a period before mixing with the resident flock. This may allow time for any lice present in the purchased group to be detected by noticeable signs of rubbing. An 18-week quarantine should be adequate to detect lice if they are present, while shorter periods provide a proportionate reduction in probability of lice detection. A long quarantine is often impractical so the sheep may be inspected for lice and in this case the chance of finding lice, if present, will depend on the number of sheep examined, the number of partings and the time elapsed since purchase (James et al. 2002). The purchased sheep may be treated with a lousicide either before or after a quarantine period. In this case the success of the treatment depends on whether the purchased sheep were shorn before treatment and whether a sufficient quarantine period elapsed after treatment for methods that do not kill immediately. If the treatment is not appropriate for the wool length (e.g. dipping or backline treatment applied too long after shearing) or the quarantine period is inadequate (after backliner or insect growth regulator treatment) then the treatment is ignored. Otherwise it is given the same probability of success as treatment of other stock at shearing.

A comprehensive list of questions is required to consider methods of handling purchased or introduced sheep (inspection, quarantine, treatment). The program uses three sets of similar questions to allow for rams, ewes and other sheep. If there were no purchases in any particular category, then the corresponding question screen is not displayed for that category of purchase.

## Strays

The program asks the user to consider neighbours in three risk categories: (i) those believed to be lice-free (actual risk set at $5 \%$ ), (ii) those of unknown lice status (local prevalence used) and (iii) those known to have lice, of high risk status, or who have lice in most years (risk assessed as 100\%). Even if a lousy stray is found it is not assumed that the home flock became infested, since sufficient contact may not have occurred. Therefore, the probability of transfer of lice from strays to the home flock is set at $80 \%$.

If stray sheep are observed then the risk is based on the assessment of the neighbours' lice risk. However, if no strays have been seen, then rather than assume no risk, it is based on the quality of the fences, as assessed by the manager.

Morcombe and Young (1993) concluded that reported incidents of stray sheep accounted for about one-third of new infestations of lice and suggested that purchases probably accounted for up to two-thirds. However, as not all strays would have been reported the proportion of new infestations due to strays is probably higher than this. The default settings provide a similar risk of lice from purchases and strays.

Good boundary fences reduce the risk of infestation whether or not neighbours have lice and good internal fences can minimise the risk that a single stray sheep will infest the whole flock. Some properties keep different mobs separated by internal natural boundaries such as rivers, cropped areas, or by main roads. However, rather than ask general questions about fence quality and then attempt to guess whether strays occurred, the program asks the manager to directly estimate the risk of straying sheep, based on local experience. This is asked separately for each of the three categories of neighbours described above. The probability of lice for each category is the probability of lice for that neighbour if strays are observed, or the probability of lice combined with the estimated probability of straying if no strays were seen.

## Signs of rubbing

Lice are difficult to find when present in low numbers, but signs of rubbing are more conspicuous (James et al. 2001). Therefore the presence or absence of rubbing is considered, together with assessment of the risk that lice entered the flock on purchased or stray sheep or were not eradicated at the last treatment. Whether or not rubbing is likely to be due to the presence of lice can be assessed independently.

Johnson et al. (1993) reported that grass seeds were the most common cause of fleece derangement, followed by lice, then itchmite. Itchmite is believed to be less common now as a result of collateral control provided by macrocyclic lactone (ML) worm drenches and the importance of grass seeds will vary widely amongst different production zones and systems. Alternative causes of rubbing considered by the model include grass seeds, itchmite, wool break, bush rub, photosensitisation, breeds of sheep that shed wool and may give the appearance that they are rubbing and exotic disease. These are assessed using a decision tree developed by Moir (2006). The relative probability of each of these events is shown in Table 1. This is the probability of that event in a random flock, i.e. not necessarily one in which rubbing has occurred. The Bayesian network adjusts all probabilities proportionately to higher values when it is known that rubbing has been observed. Some possible causes can be eliminated or confirmed by appropriate checks.

Table 1. Relative probability of causes of rubbing
The probability shown is that the causes listed here are present in a flock selected at random. The probabilities for a flock with signs of rubbing are higher but maintain the same relative proportions


## Default settings

If the producer has no knowledge of any risk factors discussed above (e.g. the property has been recently purchased and no records are available) then the risk is based only on the prevalence of infested flocks in the district. This ranges from $10 \%$ in many of the intensively farmed areas to in excess of $40 \%$ for some range areas (Reeve and Thompson 2005). A value appropriate to the location is used as the starting point for several of the calculations.

The default settings for the model, shown here, are adjusted so that if no other information is available about the property, the expected probability of lice generated by the model is similar to the local prevalence:

- Regional lice prevalence $=30 \%$
- Treated at previous shearing, but method and chemical not known
- Chance of eradication if lice at last shearing $=65 \%$
- No information on lice status at last shearing
- No information on whether split shearings are used
- Manager has not looked for lice and rubbing status is not known
- One source of rams, quarantine for rams 8 weeks before mixing with home flock
- One source of ewes, quarantine 12 weeks before mixing with home flock
- No other purchases
- Five neighbours of unknown lice status
- No information on strays, but fence condition indicates $50 \%$ chance of straying


## Overall probability of lice

The probability that lice are currently in the flock is less than the sum of the probabilities that lice were not eradicated, were
purchased or strayed in, because two or three of these events may have occurred simultaneously:

$$
\text { Overall lice probability }=1-(1-e) \times(1-p) \times(1-s)
$$

where $e$ is the probability lice were present but were not eradicated, $p$ is the probability that lice entered in purchased sheep but were not detected or treated successfully and $s$ is the probability that lice entered with strays.

## Results

If no other information is entered, the model gives a probability of lice at the current shearing of $31 \%$. This is slightly higher than the local prevalence in Australia because the default settings have been deliberately set to avoid too optimistic a result based on limited information.

Table 2 shows an example of the estimated probability of lice using the model with the default settings, and with a series of different settings. In most cases only one or two items are changed from the default settings so although the probability of eradication, purchase of lice or lice entry by strays may be low in different cases, it is only in the last case considered in Table 2 that the overall probability of lice being present is low.

The probability that lice were present at the last shearing, but not eradicated, is $12 \%$. This is consistent with Morcombe and Young (1993) who found that, where a flock was already infested, the chance that treatment would fail to eradicate was $\sim 35 \%$ (a $30 \%$ risk that lice were present at the previous shearing, combined with a $35 \%$ failure to eradicate $=10.5 \%$ ). The default settings give a $17 \%$ risk of lice in purchased sheep and a $12 \%$ risk of lice entering in strays. The combined risk of lice entering under these assumption is $1-(1-0.17) \times$ $(1-0.12)=27 \%$. Again, these risks can be compared with the findings of Morcombe and Young (1993) where in

Table 2. Probability (\%) of lice for a range of scenarios
The default settings are used unless indicated otherwise. The overall probability of lice is always less than the sum of the other probabilities because these are independent, so in some cases lice will be present due to more than one cause


flocks not infested previously ( $70 \%$ in this case), $22 \%$ subsequently had lice if no strays were observed and $31 \%$ were infested if straying sheep had entered.

## Rubbing

If the manager indicates that there is definitely no sign of rubbing then the risk that lice are present is estimated to be $25 \%$. The risk increases to $65 \%$ if rubbing has been observed, although this will be modified as other risk factors are entered. The model is very sensitive to the presence or absence of rubbing and output from the module on the cause of rubbing has a critical influence in determining whether the risk of lice is high or low.

If rubbing is possibly due to a known cause other than lice, then the model ignores rubbing and behaves as it would if the response had been that the manager had not checked for any signs of rubbing.

## Probability of eradication

If the probability of eradication at the previous shearing is reduced from $65 \%$ to $50 \%$ the probability that lice were present and not eradicated increases from $11 \%$ to $15 \%$. If the probability of eradication is as high as $80 \%$, the probability that lice were present but not eradicated is reduced to $6 \%$.

## Lice at the previous shearing

If lice were present at the previous shearing then the risk of lice due to failure to eradicate is high ( $39 \%$ ), doubling the overall risk of lice $(56 \%)$ compared with a property that did not previously have lice ( $28 \%$ ). Split shearing increases the risk that lice will not be eradicated from $10 \%$ to $13 \%$ but since it does not affect entry of lice, this does not have a major influence on the overall risk unless the risk from purchases and strays is very low.

## Purchased sheep

Purchase of sheep from a large number of suppliers results in a higher risk of bringing in lice, with a $17 \%$ risk from a single ram supplier, compared with $34 \%$ if five different suppliers are used. However, the estimated risk can be reduced where appropriate treatment or quarantine has been carried out.

## Strays

The estimated risk of lice from strays ranges from $2.4 \%$ if no strays were observed to $24 \%$ if strays were definitely seen. The risk due to unobserved strays can be reduced if the fences are known to be in good condition.

## Low risk properties

If all aspects are combined then the risk that lice were present at the last shearing but not eradicated, that lice were purchased, or that lice entered on strays, can all be sufficiently low to give a low overall risk of lice.

## Discussion

The program is designed to be used by a manager or adviser to decide whether or not a flock with unknown lice status requires
treatment, although it can be used for other purposes. The user can work through all the issues that may affect the possibility that lice are currently in the flock. Alternatively, the program could be used for a flock that is known to have lice where the manager wishes to assess the risks that might have led to the infestation. Or it might be used as an early step in the development of a biosecurity plan to identify important risk factors (Evans and Karlsson 2001). It can also be used for training advisory staff who have limited experience with lice control by allowing them to examine a range of scenarios to estimate the effect of different lice control options. Advisers can adjust all the settings to suit their own local conditions or experience.

The model is not highly sensitive to individual items entered other than those that clearly lead to a high risk. Therefore the only way to reduce the risk to low levels is by covering a wide range of issues thoroughly.

The rubbing model can be used separately from the other networks, to assist a wool producer in determining the cause of wool damage where this may be unrelated to lice. However, when used with the main program it integrates fully with the other details entered.

The use of a Bayesian network allows an adviser using the program to obtain some information from the manager and then estimate the probability of lice based on the information supplied. Where the missing information might change the result enough to affect whether or not a treatment is applied the adviser can decide to obtain further data. For example, the presence of rubbing may require that the mob be brought in for more detailed examination to determine the cause, or it may be necessary to obtain records of the treatments of purchased stock. The use of Bayesian networks to assist decision making with incomplete data, may also have benefits in other areas of decision support in agriculture, for example where there is an additional cost to obtain extra information.

## Acknowledgements

Funding for development of this model was provided by Australian wool producers and the Australian Government through Australian Wool Innovation Limited. Don Moir, Department of Agriculture \& Food WA provided a decision tree on which the rubbing network was based. Michael Horton (School of Computing, University of Tasmania) provided assistance in development of the Bayesian network and comparison with other decision support systems.
