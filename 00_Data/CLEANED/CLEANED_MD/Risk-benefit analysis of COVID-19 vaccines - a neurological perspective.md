# Risk-benefit analysis of COVID-19 vaccines a neurological perspective 

Colleen L. Lau (D) and Ian Galea (D)

Rare neurological complications can occur after COVID-19 vaccination, but recent studies show that such complications are much more common after SARS-CoV-2 infection. Novel approaches to risk-benefit analysis such as Bayesian network models can integrate the latest global evidence with local factors to inform decision-making and support the global vaccination effort.

Refers to Palaiodimou, L. et al. Cerebral venous sinus thrombosis and thrombotic events after vector-based COVID-19 vaccines: a systematic review and meta-analysis. Neurology 97, e2136-e2147 (2021) | Patone, M. et al. Neurological complications after first dose of COVID-19 vaccines and SARS-CoV-2 infection. Nat. Med. https:// doi.org/10.1038/s41591-021-01556-7 (2021).

The global roll-out of COVID-19 vaccines is unprecedented in terms of scale and pace. However, although vaccines are crucial for pandemic control, adverse events following immunization (AEFI), even if rare, have contributed to vaccine hesitancy. Emerging reports of AEFI have generated substantial media attention even before proven causation and have affected vaccine confidence and created challenges for risk-benefit analysis of mass vaccination programmes. Even rare AEFI have led to changes to national vaccination guidelines. For example, rare cases of thrombosis and thrombocytopenia syndrome (TTS) after the ChAdOx1 nCov-19 vaccine, which are more common in younger age groups, prompted age-specific restrictions for this vaccine in some countries ${ }^{1}$.

TTS is frequently associated with cerebral venous sinus thrombosis (CVST); in fact, a new systematic review and meta-analysis published in Neurology by Palaiodimou et al. ${ }^{2}$ found that half of individuals who developed TTS after receiving a vector-based vaccine (ChAdOx1 nCoV-19 or Ad26.COV2.S) presented with CVST, and TTS-associated CVST had a pooled mortality of $38 \%$. When considered in isolation, these statistics are worrying and could easily be misconstrued. Two key messages should be communicated alongside such reports: the true incidence of AEFI remains unclear, and comparison with the incidence of similar events after SARS-CoV-2 infection is needed to balance the risks against the benefits.

A large risk-benefit analysis of COVID-19 vaccines focusing on thrombocytopenia
and thromboembolism was published by Hippisley-Cox et al. ${ }^{3}$ in The British Medical Journal in August 2021. Using linked data from around 30 million UK hospital records and the English National Immunisation Database, the study found that risks of thrombocytopenia, venous thromboembolism, arterial thromboembolism, CVST and ischaemic stroke were higher or substantially higher after SARS-CoV-2 infection than after vaccination. The self-controlled case series design enabled comparison between exposed and unexposed periods within the same individuals, thereby eliminating time-invariant confounding and uncertainties about background risks and causality ${ }^{4}$.

A new study published in Nature Medicine by the same group used a similar approach to compare rare neurological complications after COVID-19 vaccination (ChAdOx1 nCov-19 or the mRNA vaccine BNT162b2) and after a positive SARS-CoV-2 test ${ }^{5}$. The most notable finding was an increased risk of Guillain-Barré syndrome (incidence risk ratio (IRR) 2.90) after the ChAdOx1 nCov-19 vaccine, which was confirmed in a second cohort. However, self-controlled case series are prone to bias, especially as they assume that occurrence of an event does not affect subsequent exposure ${ }^{5}$. To limit this bias, data from the 28 -day period before vaccination were excluded from the baseline. However, the occurrence of a neurological condition might delay vaccination by more than 28 days or prevent vaccine uptake altogether, which may result in the baseline period having
fewer patients with these conditions. This artefactual lowering of the baseline prevalence of neurological conditions might have inflated IRRs during post-vaccination periods. Nevertheless, the study's key strength was the comparison of incidence of rare events after vaccination versus after a positive SARS-CoV-2 test, which clearly demonstrated that incidence of all neurological outcomes, including Guillain-Barré syndrome (IRR 5.25), Bell palsy, demyelinating disorders, encephalitis, meningitis, myelitis, myasthenic disorder, haemorrhagic stroke and subarachnoid haemorrhage, was substantially higher after infection than after vaccination.

The study, by Patone et al. ${ }^{3}$, involved over 32 million vaccinated individuals. Studies with such huge sample sizes enable investigation of rare AEFI that would be impossible with clinical trials. Data from such studies are crucial to inform evidence-based risk-benefit analysis and decision-making. With rapidly evolving information about COVID-19 vaccines, weighing risks (AEFI) versus benefits (illness and deaths prevented) has been complex and challenging for individuals, clinicians and public health policy makers. Furthermore, risk-benefit analysis depends on the level of community transmission, vaccine effectiveness and local case fatality rates.

## Incidence of all neurological outcomes ... was substantially higher after infection than after vaccination

The studies described above show that syntheses of evidence from huge databases and large meta-analyses are powerful for investigating rare complications from vaccines versus infections. However, data are likely to continue to emerge from multiple sources and evolve rapidly, making it increasingly challenging to keep abreast of new evidence. Other AEFIs will probably emerge with new vaccines and boosters, and the incidence of late and chronic complications (for example, long COVID) will evolve over time. Novel approaches are needed for (near) real-time risk-benefit analyses that integrate the latest global evidence with locally relevant factors to support local decision-making.

As recently published in Vaccine, Lau et al. used a Bayesian network (BN) model to develop CoRiCal (Covid Risk Calculator) ${ }^{6}$, a decision support tool for the ChAdOx1 nCov-19 vaccine in Australia that takes into account age, sex, local transmission and other local factors ${ }^{7}$. Although Australia has robust AEFI surveillance, risk-benefit analysis has been challenging because of the relatively low

![img-0.jpeg](img-0.jpeg)

Fig. 1 | Bayesian network to assess risks versus benefits of COVID-19 vaccines under different scenarios. Bayesian networks consist of nodes (boxes) and links (arrows) that define probabilistic relationships between parent and child nodes. For example, 'vaccine effectiveness against death' has 'SARS-CoV-2 variant' as a parent node and 'death from COVID-19' as a child node. Conditional probability
tables (not shown) define quantitative relationships between parent and child nodes. A priori probabilities are assigned to parentless nodes (for example, 'sex'). The Bayesian network can be used for risk-benefit analysis under different scenarios, for example, based on the number of vaccine doses, age, sex, SARS-CoV-2 variant and level of community transmission.
transmission rates ( 1,734 deaths as of October 2021) ${ }^{2}$, and large linked datasets such as those used by Patone et al. are not available.

CoRiCal uses a BN to integrate multiple Australian and international data sources. Model inputs can be rapidly updated as evidence evolves, for example, owing to fluctuating transmission rates, waning immunity, new variants and changes in vaccine effectiveness. BNs are conditional probability models that capture joint probabilities of events using directed acyclic graphs. Variables are depicted visually as nodes, with links representing probabilistic parent-child relationships between nodes (FIG. 1). The graphical and transparent representation of assumptions can help build confidence and trust in model outputs. The CoRiCal model was parametrized using probabilities from the literature, government reports and expert opinion ${ }^{3}$, but BNs can also learn probabilities from datasets. CoRiCal could be adapted for other countries or other outcomes - for example, neurological complications based on the data reported in the above studies or learning directly from the datasets.

Risk calculators provide population-level estimates that are applicable for public health

## 6

Novel approaches are needed for (near) real-time risk-benefit analyses
practice, but clinical advice and decisionmaking for individuals should also consider factors such as the individual's demographic and clinical characteristics. An extreme example would be someone who has already sustained a potentially vaccine-induced neurological complication after the first dose of a vaccine; population-level risk-benefit calculations provide estimates for the 'average person' and, therefore, might not apply to this individual. As data become available, more variables can be included in models, but clinical judgement will still be required for situations in which no data are available. Models such as QCovid predict the risk of death or hospitalization from COVID-19 on the basis of demographics and comorbidities, including neurological conditions ${ }^{10}$. Calculators such as CoRiCal and QCovid could potentially be combined. Flexible modelling approaches and risk-benefit visualization tools could support evidence-based decision-making by increasing the accessibility of the latest information to the global citizen, thereby aiding vaccination efforts worldwide.

Colleen L. Lau ${ }^{10}$ and Ian Galea ${ }^{2}$
${ }^{1}$ School of Public Health, Faculty of Medicine, University of Queensland, Brisbane, Queensland, Australia.
${ }^{2}$ Clinical Neurosciences, Clinical and Experimental Sciences, Faculty of Medicine, University of Southampton, Southampton, UK.
${ }^{10}$ e-mail: colleen.lau@uq.edu.au
https://doi.org/10.1038/s41582-021-00606-5

1. MacIntyre, C. R., Veness, B., Berger, D., Hamad, N. \& Bari, N. Thrombosis with thrombocytopenia syndrome (TTS) following AstraZeneca ChAdOx1 nCoV-19 (AZD1222) COVID-19 vaccination - a risk-benefit analysis for people <60 years in Australia. Vaccine 39, 4784-4787 (2021).
2. Palaiodimou, L. et al. Cerebral venous sinus thrombosis and thrombotic events after vectorbased COVID-19 vaccines: a systematic review and meta-analysis. Neurology 97, e2156-e2147 (2021).
3. Hippisley-Cox, J. et al. Risk of thrombocytopenia and thromboembolism after covid-19 vaccination and SARS-CoV-2 positive testing: self-controlled case series study. Br. Med. J. 374, e1951 (2021).
4. Petersen, I., Douglas, I. \& Whitaker, H. Self controlled case series methods as alternative to standard epidemiological study designs. Br. Med. J. 354, i4515 (2016).
5. Patone, M. et al. Neurological complications after first dose of COVID-19 vaccines and SARS-CoV-2 infection. Nat. Med. https://doi.org/10.1038/s41591-021 01556-7 (2021).
6. Immunisation Coalition. CoRiCal: Covid Risk Calculator https://corical.immunisationcoalition.org.au/ (2021).
7. Lau, C. L. et al. Risk-benefit analysis of the AstraZeneca COVID-19 vaccine in Australia using a Bayesian network modelling framework. Vaccine https://doi.org/ 10.1016/j.vaccine.2021.10.079 (2021).
8. Australian Government Department of Health. Coronavirus (COVID-19) Case Numbers and Statistics https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-case-numbers-and-statistics#covid19summary-statistics (2021).
9. Mayfield, H. J. et al. Designing an evidence-based Bayesian network for estimating the risk versus benefits of AstraZeneca COVID-19 vaccine. Preprint at medRxiv https://doi.org/10.1101/2021.10.28. 21265588 (2021).
10. Cift, A. K. et al. Living risk prediction algorithm (QCOVID) for risk of hospital admission and mortality from coronavirus 19 in adults: national derivation and validation cohort study. Br. Med. J. 371, m5751 (2020).

## Acknowledgements

C.L.L. was supported by an Australian National Health and Medical Research Council Fellowship (APP1193826).

## Competing interests

The authors declare no competing interests.