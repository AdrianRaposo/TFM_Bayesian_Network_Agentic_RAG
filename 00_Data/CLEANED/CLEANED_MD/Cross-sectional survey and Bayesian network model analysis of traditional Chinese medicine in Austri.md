# BMJ Open Cross-sectional survey and Bayesian network model analysis of traditional Chinese medicine in Austria: investigating public awareness, usage determinants and perception of scientific support 

Michael Eigenschink (1) ${ }^{1}$ Luise Bellach (1) ${ }^{1}$ Sebastian Leonard, ${ }^{2}$<br>Tom Eric Dablander, ${ }^{1}$ Julian Maier (1) ${ }^{1}$ Fabian Dablander (1) ${ }^{3}$ Harald H Sitte (1)

To cite: Eigenschink M, Bellach L, Leonard S, et al. Cross-sectional survey and Bayesian network model analysis of traditional Chinese medicine in Austria: investigating public awareness, usage determinants and perception of scientific support. BMJ Open 2023;13:e060644. doi:10.1136/ bmjopen-2021-060644

- Prepublication history and additional supplemental material for this paper are available online. To view these files, please visit the journal online (http://dx.doi.org/10.1136/ bmjopen-2021-060644).

Received 01 March 2022
Accepted 29 January 2023

Check for updates
(c) Author(s) (or their employer(s)) 2023. Re-use permitted under CC BY-NC. No commercial re-use. See rights and permissions. Published by BMJ.
For numbered affiliations see end of article.

[^0]
## ABSTRACT

Objectives Despite the paucity of evidence verifying its efficacy and safety, traditional Chinese medicine (TCM) is expanding in popularity and political support. Decisions to include TCM diagnoses in the International Classification of Diseases 11th Revision and campaigns to integrate TCM into national healthcare systems have occurred while public perception and usage of TCM, especially in Europe, remains undetermined. Accordingly, this study investigates TCM's popularity, usage and perceived scientific support, as well as its relationship to homeopathy and vaccinations.
Design/Setting We performed a cross-sectional survey of the Austrian population. Participants were either recruited on the street (in-person) or online (web-link) via a popular Austrian newspaper.
Participants 1382 individuals completed our survey. The sample was poststratified according to data derived from Austria's Federal Statistical Office.
Outcome measures Associations between sociodemographic factors, opinion towards TCM and usage of complementary medicine (CAM) were investigated using a Bayesian graphical model.
Results Within our poststratified sample, TCM was broadly known ( $89.9 \%$ of women, $90.6 \%$ of men), with $58.9 \%$ of women and $39.5 \%$ of men using TCM between 2016 and 2019. Moreover, $66.4 \%$ of women and $49.7 \%$ of men agreed with TCM being supported by science. We found a positive relationship between perceived scientific support for TCM and trust in TCM-certified medical doctors ( $\rho=0.59,95 \%$ CI 0.46 to 0.73 ). Moreover, perceived scientific support for TCM was negatively correlated with proclivity to get vaccinated ( $\rho=-0.26,95 \% \mathrm{Cl}$ $-0.43$ to -0.08 ). Additionally, our network model yielded associations between TCM-related, homeopathy-related and vaccination-related variables.
Conclusions TCM is widely known within the Austrian general population and used by a substantial proportion. However, a disparity exists between the commonly held public perception that TCM is scientific and findings from evidence-based studies. Emphasis should be placed on

## STRENGTHS AND LIMITATIONS OF THIS STUDY

$\Rightarrow$ Using a cross-sectional survey design, this study comprehensively explores the usage patterns and sociodemographic associations of traditional Chinese medicine in a European population.
$\Rightarrow$ The data were collected from a convenience sample gathered through online and in-person surveys.
$\Rightarrow$ To increase the validity of inferences, the sample was poststratified using representative data from Austria's Federal Statistical Office ('Statistik Austria').
$\Rightarrow$ Using a novel statistical modelling method (Bayesian Gaussian graphical copula model), data were robustly explored and partial correlations between all ascertained variables recorded.
$\Rightarrow$ Due to the retrospective character of the crosssectional survey, answers are naturally prone to recall and response bias.
$\Rightarrow$ Although the data were carefully collected and poststratified, limitations like self-selection bias still apply to the sampling methodology.
supporting the distribution of unbiased, science-driven information.

## INTRODUCTION

Traditional Chinese medicine (TCM), an alternative medical practice shaped by Taoism and Confucianism, was first documented over two millennia ago in the compendium Huangdi Neijing. ${ }^{1}$ As a core feature of China's cultural heritage, TCM is predominantly practised in Asia but has gradually been introduced to the international medical community due to China's opening to the West and its promotion by the Chinese Communist Party. ${ }^{2-4}$ The apogee of this expansion can be seen in WHO's decision to include TCM


[^0]:    Correspondence to
    Dr Harald H Sitte; harald.sitte@meduniwien.ac.at

diagnoses in its 11th revision of the International Classification of Diseases (ICD-11). ${ }^{36}$ This controversial decision follows a lengthy campaign to integrate complementary medicine (CAM) services into national healthcare systems through the WHO Traditional Medicine Strategy 2014-2023. ${ }^{7}$ Notably, the origin of this document raises concerns over conflicts of interest as its development was supported technically, logistically and financially by the People's Republic of China, the Government of the Hong Kong Special Administrative Region and the Hong Kong WHO Collaboration Centre for Traditional Medicine. ${ }^{7}$

Despite acquiring international recognition, TCM's theoretical foundation diverges from a modern understanding of science; invoking the 'life-energy' qi, ${ }^{8}$ a network of channels through which qi passes called meridians, ${ }^{9}$ and the metaphysical forces of yin and yang, which are claimed to be imbued into all entities. ${ }^{110}$ In practice, while some randomised controlled trials (RCTs) point towards an effect of TCM therapies on various clinical outcomes, ${ }^{11-14}$ meta-analyses and Cochrane reviews have concluded that the overall data landscape either yields low-quality evidence or is not sufficient to support regular clinical usage. ${ }^{15-19}$ Of note, the largest proportion of TCM-related RCTs examine the efficacy of acupuncture, and effects seem to dissipate on usage of strict control group designs. ${ }^{20-22}$ Thus, empirical evidence behind many TCM therapies and diagnostics is deemed poor. ${ }^{23}$

In addition to well-known phytotherapeutics like Ginkgo biloba or Lycium barbarum, TCM also actively supports the usage of animal-derived products to treat diseases like stroke, myocardial infarction, convulsion and pain syndromes. ${ }^{2324}$ Pangolin scales, tiger bones, seahorses, rhino horns and bear bile are among a few of the items used in TCM that have sparked international concern due to reports of animal rights violations, poaching of endangered species and the incentivisation of animal trafficking. ${ }^{25-29}$ Indeed, seizure numbers of animal-derived medicinal products totalled 40434 during 2018 in the European Union (EU) alone, with Thailand and China constituting the largest exporters. ${ }^{30}$

Today, TCM is exported to over 160 countries, ${ }^{31}$ generating high revenue within the USA and EU. ${ }^{3233}$ Thus, with the establishment of verified TCM schools teaching acupuncture and herbal medicine in North America, Australia and Europe, ${ }^{34}$ there are strong reasons to suggest that TCM has moved beyond the Asian market. ${ }^{35}$ Considering its lack of scientific basis, this growth in popularity sparks concerns regarding patient safety. Contrary to other CAM practices like homeopathy, TCM endorses the application of pharmacologically active substances. However, compared with conventional therapeutics, traditional remedies and phytotherapeutics are not subject to the same regulatory requirements and stringent testing. ${ }^{3637}$ Due to their non-purified nature and reportedly variable compositions, concentrations of desired active agents may differ greatly and contamination with potentially poisonous substances might occur. ${ }^{38-41}$ Indeed, unwanted interactions with conventional therapeutics and serious adverse events have been reported in the literature. ${ }^{42-45}$

Despite a clear demand for high-quality research, there exists a paucity of information on TCM usage patterns in European countries compared with the data available from official Chinese government reports or studies deriving from other Asian countries. ${ }^{46-48}$ Moreover, there is considerable data heterogeneity across European studies evaluating CAM usage patterns. ${ }^{49}$ Few studies have evaluated the general public's attitude towards CAM, ${ }^{5051}$ even fewer have focused on the perception of TCM outside Asia, ${ }^{52-54}$ and none have reported on the public's perception of its scientific support. Thus, following two European social survey data analyses conducted by Kemppainen et al and Fjær et al, ${ }^{5556}$ this study aims to elucidate the awareness, acceptance and usage of TCM in a Central European population, as represented by Austria, while putting special emphasis on the public's perception of TCM's scientific support. Additionally, we also investigate public trust in TCM practitioners because (i) trust in CAM practitioners has been shown to be enhanced by institutional guarantees, ${ }^{57}$ thus is potentially altered by the perception of scientific support, and (ii) trust in practitioners was shown to determine patient satisfaction, ${ }^{58}$ thereby possibly influencing usage frequency and treatment expenditures. Of note, TCM-related expenses are not financed by Austrian public health insurance and are thus paid by patients themselves.

Finally, we explore the proclivity to use TCM when in combination with homeopathy, the most prevalent type of CAM in Austria. ${ }^{59}$ Furthermore, we analyse the relationship between TCM usage and the utilisation of vaccines, as data on CAM users point towards a reduced readiness to get vaccinated when compared with nonusers. ${ }^{60-63}$ Ultimately, using a Bayesian graphical model, we explore the multivariate conditional (in)dependence structure of all variables queried in our survey. Thereby, we retrieve partial correlations that indicate distinct associations allowing us to untangle the complex interactions that underlie CAM usage.

## METHODS

## Data collection

We performed a questionnaire-based cross-sectional study within the Austrian general population. Our study was divided into two phases to ensure a representative sample size: (i) an interview-based street survey and (ii) an online survey. The questionnaires were designed using the online survey tool 'SoSciSurvey'. The street survey was conducted on 6 April 2019 by 19 different interviewers on 12 highly frequented and sociodemographically heterogeneous places throughout Vienna, Austria. Interviewers were trained with a test group, received detailed instructions ahead of their participation and, on the day of the street survey, were in constant communication with the organising team. The online survey was uploaded as an article on 2 March 2019 on the website of the most

popular daily free newspaper in Austria (named 'Heute', translated 'Today'). The link was open for participation for a total of 6 days, spanning from 2 March to 7 March.

## Procedures

Individuals were approached indiscriminately by interviewers. After informed consent was obtained and electronically recorded, interviewers asked questions and recorded responses according to a predefined answer scheme on a mobile device. Interviewers were instructed to remain impartial and cognisant of their speech and body language to minimise bias introduced by intonation, connotation and gesturing. Responses were recorded anonymously. The median duration of the survey was 189 seconds per participant.

The online survey was identical to the street survey, except for minor modifications that were necessary for the survey to be fully comprehensible in the absence of an interviewer. A CAPTCHA was implemented to distinguish true participants from automated responders. After providing detailed information about data storage and privacy, consent was obtained through a digital form at the beginning of the survey. As SoSciSurvey does not use IP address filtering, thereby enabling the possibility of repeated participation by the same respondent, participants were directly addressed on the first page of the survey and specifically asked to only participate once. Moreover, we used an average relative completion speed cut-off of 2.0 to filter out meaningless, potentially duplicate responses. ${ }^{64}$ Consistent with the street survey, responses were recorded anonymously. The median duration of the survey was 212 seconds per participant. It is probable that the increased time taken to complete the online survey compared with the street survey was due to the addition of an introductory page, a CAPTCHA and a finishing page.

## Questionnaire

Designed by our team from the Medical University of Vienna (10 researchers) to combine classical sociodemographic determinants with indicators of CAM usage, the questionnaire especially focused on the utilisation of TCM. It included a total of 21 items: 6 pertained to sociodemographic factors (gender, age, citizenship, level of education, employment and income), 8 queried TCM directly (awareness, general usage, usage frequency, perception of scientific support, trust in TCM-certified medical doctors and TCM expenses), 4 focused on additional CAM usage patterns (homeopathy and vaccination hesitancy) and 3 were asked to further characterise our sample (study participation, chronic illness and money spent on conventional medicine). The questionnaire was tested via a pre-questionnaire on a heterogenous group of 20 people ${ }^{65}$ of varying age and sociodemographic characteristics in consecutive phases. Inputs were considered and the questionnaire was optimised between phases. In some instances, the questionnaire was taken in person with the interviewer present to immediately discuss the respondents' thoughts ('think aloud'). This allowed for optimisation of question comprehensibility, appropriateness, order and wording to ensure the validity of questionnaire items. The questionnaire can be obtained from the online supplemental file 1 in both German and English (translated by the authors and cross-checked by a native English speaker).

## Statistical analysis

We used a Bayesian graphical model to explore the multivariate conditional (in)dependence structure of our variables. In a graphical or network model, each variable represents a node and an edge is drawn between two nodes if they are conditionally associated, that is, if they are associated after adjusting for all other variables; the edge weight is given by the strength of this association. ${ }^{66}$ The model allowed us to answer questions such as 'how strongly is gender associated with TCM usage frequency after adjusting for all other variables?'. The fact that many conditional associations can be handled within a single model and intuitively visualised made this approach ideal for exploring relationships between our variables. Note that we did not conduct a statistical power analysis because our goal is not to test hypotheses and control the false positive and false negative error rates. That is, we did not specify a hypothesised effect size and derive a necessary sample size from it. This is because our goal is to quantify the uncertainty across the estimated (conditional) relationships between variables, and our Bayesian method naturally accounts for uncertainty and guards against overconfidence.

One of the most widely used graphical models is the Gaussian graphical model, which assumes that the data follow a multivariate Gaussian distribution. ${ }^{66}$ The inverse of the covariance matrix parameterises this model, which then yields a matrix of partial correlations when it is standardised. As many of our variables were categorical (eg, gender and chronic disease) or ordinal (eg, education and income), they did not follow a Gaussian distribution. To be able to model the dependencies between our variables without making incorrect assumptions about their univariate marginal distributions, a Gaussian copula was used. ${ }^{6768}$ The Gaussian copula graphical model ${ }^{69} 70$ allowed us to separate the modelling of the dependency between variables (which is achieved through the Gaussian copula) from modelling the marginal distributions (which we do without assuming a particular parametric form). ${ }^{68}$ Similar to the Gaussian graphical model, the Gaussian copula graphical model is parameterised by an inverse covariance matrix which, when standardised, yields a matrix of partial correlations that encode the dependencies between our variables; the key difference is that now the different univariate marginal distributions of our variables are respected. It is this partial correlation matrix, as well as the simple correlation matrix, that we have focused on in our analysis.

Quantifying uncertainty is an important part of any statistical analysis because it guards against

Table 1 Overview of CAM usage

acupuncture | Has used
homeopathy | Has recommended
homeopathy  |

An overview of female and male CAM usage examining the relative frequencies of five criteria: (1) TCM awareness, (2) usage of TCM, (3) usage of acupuncture, (4) usage of homeopathy, (5) homeopathy propagation.

CAM, complementary medicine; TCM, traditional Chinese medicine. overconfidence. Bayesian inference provides a principled and practical approach to quantifying uncertainty, therefore we employed it in our analysis. Bayesian inference requires specifying a prior distribution over parameters, which then gets updated to a posterior distribution when combined with data. We assigned a recently introduced Matrix-F distribution to the inverse covariance matrix in our Gaussian copula graphical model. ${ }^{7172}$ While the Matrix-F distribution constitutes a more flexible prior compared with the widely used Wishart prior, we note that with sample sizes as large as ours, the prior has little influence on the posterior. We used the R package BGGM (V.2.0.4) for our analysis. ${ }^{72}$ We report summaries of the posterior distribution for all partial correlations as well as marginal correlations in the Gaussian copula graphical model. Furthermore, the extent to which the variance of each variable can be explained by all other variables is reported. ${ }^{7374}$

As for data exclusion, 75 participants were excluded from all analyses due to missing and inconclusive data. Moreover, 19 participants were excluded from the analysis shown in table 1. For TCM-related analyses, 232 individuals who reported unawareness of TCM or indicated inconsistency in their knowledge of TCM, homeopathy or acupuncture, and 13 participants who had skipped analysis-relevant questions were excluded. Additionally, 34 participants were excluded for not providing information about their medical expenses in our analysis of the personal financial cost of TCM. Of note, for the Bayesian graphical model, we imputed the income group of 156 participants and the medical expenses of the 34 participants who chose not to provide the respective data using the R package mice (V.3.14.0). ${ }^{75}$ For more comprehensibility, data acquisition, curation and analysis are summarised as a flow chart in figure 1.

Of note, as our sample was skewed towards the young and more educated population and suffered from a relative under-representation of males, we poststratified it using data deriving from 'Statistik Austria', ${ }^{76}$ Austria's Federal Statistical Office. All results displayed in this paper (except figure 2) are derived from the poststratified sample. For reasons of transparency, all raw descriptive statistics can be found in the R-script uploaded in our GitHub repository (Dataset). ${ }^{77}$ Because a method to use poststratification in the estimation of the Bayesian Gaussian copula graphical model does not currently exist, we poststratified manually, subsampling our dataset with replacement using poststratification weights and estimating the graphical model on the subsampled data. We repeated this procedure 250 times. Combining the estimates from these runs yielded a poststratified graphical model. The graphical model and figures that are based on the raw data are attached as online supplemental figures 1S-3S.

All statistical analyses were conducted using the statistical computing language R V.4.0.0. ${ }^{78}$ We used the R package BGGM (V.2.0.4) for our analysis. The R-script can be obtained from the online GitHub repository (Dataset). ${ }^{77}$

## Patient and public involvement statement

Other than giving feedback on the questionnaire, neither patients nor the general public were actively involved in (i) the design and (ii) the conducting of the study as well as (iii) the reporting of outcomes and (iv) dissemination of research results.

## RESULTS

A total of 1382 participants completed either the online ( $\mathrm{n}=918$ ) or street ( $\mathrm{n}=464$ ) survey. After exclusion of missing and inconclusive data, ${ }^{64}$ a total of 1307 participants were eligible for data analysis.

## Demographic analysis

Our study population consisted of 901 women and 406 men with a mean age of 41.7 (SD 15.6) and 40.5 (SD 16.9) years, respectively; $76.9 \%(1005 / 1307)$ of our study population were Austrian citizens, $91.5 \%$ (1195/1307) originated from European countries and $0.07 \%$ (1/1307) were Chinese citizens. The majority of participants ( $67.7 \%(610 / 901)$ women and $67.0 \%(272 / 406)$ men) were employed at the time of data collection (figure 2); $42.2 \%(380 / 901)$ of women and $39.4 \%(160 / 406)$ of men had a university degree and $32.1 \%(244 / 760)$ of women and $47.2 \%(162 / 343)$ of men reported a monthly income exceeding $€ 2000$ (excluding 141 women and 63 men who chose not to report their income bracket). Moreover,

![img-0.jpeg](img-0.jpeg)

Figure 1 Flow chart depicting the acquisition, processing and analysis of the data (created with BioRender.com). CAM, complementary medicine; TCM, traditional Chinese medicine.
$45.3 \%(408 / 900)$ of women and $38.7 \%(157 / 406)$ of men suffered from a chronic disease. Compared with the Austrian general population, men were strongly underrepresented in our sample population. Additionally, when compared with the Austrian general population, the sample was skewed towards the young with more people in the 15-29 years age bracket ( $36.7 \%$ (149/406) vs $21.5 \%$ for men and $26.8 \%(241 / 901)$ vs $19.4 \%$ for women) and correspondingly less in the 65-84 years age bracket ( $10.6 \%(43 / 406)$ vs $17.8 \%$ for men and $8.6 \%$ $(77 / 901)$ vs $20.6 \%$ for women). The participants also had higher levels of education compared with the Austrian general population: only $36 / 406(8.9 \%)$ of men and
$45 / 901(5.0 \%)$ of women in our sample reported lower secondary education as their highest level of education, compared with $16.9 \%$ and $22.0 \%$ in the general population. ${ }^{76}$ Similarly, the proportion of men and women in our sample reporting to have completed a Bachelor's, Master's or PhD qualification was $39.4 \%(160 / 406)$ and $42.2 \%(380 / 901)$, respectively, compared with $12.7 \%$ and $12.5 \%$ in the general population. ${ }^{76}$

Thus, using data derived from 'Statistik Austria'76 (Austria's Federal Statistical Office), we poststratified our sample in order to more closely represent the Austrian general population in terms of gender, age and education. An analysis of TCM awareness and usage, acupuncture

![img-1.jpeg](img-1.jpeg)

Figure 2 The distribution of (A) age, (B) highest level of education attained and (C) average monthly income in euro (€), by gender. Yellow bars and blue bars represent female and male participants, respectively. *A-level with additional education in economics, cooking, etc.
usage as well as homeopathy usage and propagation is presented in table 1.

## TCM-related analysis

Regarding the frequency of TCM usage, $58.9 \%$ of women and $39.5 \%$ of men used TCM at least once between 2016 and 2019. An examination of participants reporting high usage frequencies revealed a gender imbalance with $31.8 \%$ of women compared with $24.9 \%$ of men reporting usage at least five times during the same 3 -year period; $48.6 \%$ of women and $30.3 \%$ of men used acupuncture at least once in the past 3 years, with $22.0 \%$ of women and $17.8 \%$ of men using it at least five times. Further statistics and unweighted data are provided in table 2.

Furthermore, we evaluated the perception of scientific support for TCM and trust in TCM-certified medical doctors; $66.4 \%$ of women and $49.7 \%$ of men 'mostly agreed' or 'completely agreed' with TCM being scientific. This trend is congruent with $83.3 \%$ of women and $70.2 \%$ of men who 'mostly agreed' or 'completely agreed' with TCM-certified medical doctors being trustworthy alongside $7.2 \%$ of women and $18.8 \%$ of men who either 'did not agree' or 'rather disagreed'. Further information
and unweighted data regarding the perception of scientific support for TCM and trust in TCM-certified medical doctors can be obtained from table 3.

In order to better understand the personal financial cost of TCM, we evaluated the most recent 3-year history of participant's medical and TCM expenses; $52.4 \%$ of women and $66.9 \%$ of men spent $<\in 100$ on TCM-related therapies, while $14.2 \%$ of women and $8.3 \%$ of men spent $>\in 750$. Additional information and unweighted data regarding conventional medicine and TCM expenses can be obtained from table 4.

## Bayesian graphical model

A Bayesian Gaussian copula graphical model was used to explore (conditional) associations between the ascertained variables. ${ }^{68} 77$ Figure 3 shows the partial and marginal correlation networks, with edge sizes indicating the posterior mean of the (conditional) associations. The marginal correlation network provides information about how strongly any two variables are related without taking any other variable into account. The partial correlation network, on the other hand, indicates how strongly any two variables are associated if all other variables are taken

Table 2 Analysis of acupuncture and TCM usage between 2016 and 2019


The number of times female and male participants have used (A) acupuncture or (B) TCM between 2016 and 2019.
TCM, traditional Chinese medicine.
into account. Naturally, partial correlations are weaker than marginal correlations, as indicated by the reduced edge size observable in figure 3. We focus on partial correlations with posterior means and $95 \%$ credible intervals, as shown in figure 4.

Currently, a standardised way does not exist to use poststratification in the estimation of Bayesian Gaussian copula graphical models. We therefore poststratified manually, subsampling our dataset with replacement using poststratification weights and estimating the graphical model on the subsampled data. Of note, literature considers correlation coefficients between $(-) 0.7$ and $(-) 1.0,->0.3$ and $(-) 0.7$ and 0.0 and $(-) 0.3$ to indicate strong, moderate and weak correlations, respectively. ${ }^{79}$

Strong positive partial correlations between vaccine usage [13] and utilisation of booster vaccines [14]
( $\rho=0.85,95 \%$ CI 0.80 to 0.90 ), homeopathy usage [11] and propagation of homeopathy [12] ( $\rho=0.70,95 \% \mathrm{CI}$ 0.56 to 0.84 ), as well as a moderate positive partial correlation between the frequency of TCM usage [7] and money spent on TCM [10] ( $\rho=0.62,95 \%$ CI 0.50 to 0.72 ) were observed. Interestingly, a moderate partial correlation was also found between the perceived scientific support for TCM [8] and trust in TCM-certified medical doctors [9] $(\rho=0.59,95 \%$ CI 0.46 to 0.73 ).

Regarding money spent on TCM between 2016 and 2019 [10], next to the strong positive partial correlation with TCM usage frequency [7], weak positive partial correlations with acupuncture usage frequency [15] ( $\rho=0.26,95 \%$ CI 0.08 to 0.41 ), overall medical expenses [5] ( $\rho=0.22,95 \%$ CI 0.06 to 0.37 ) and income

Table 3 Analysis of the perception of scientific support for and trust in TCM-certified medical doctors


Female and male (A) perception of scientific support for TCM and (B) trust in TCM-certified medical doctors. Results conform to a Likert scale in which 'do not agree' indicates a perception of weak scientific support and distrust, and 'completely agree' indicates perception of strong scientific support and trust.
TCM, traditional Chinese medicine.


[3] $(\rho=0.16,95 \% \mathrm{CI} 0.01$ to 0.32$)$ were observed. TCM usage frequency [7] was also positively associated with the utilisation of acupuncture [15] after adjusting for all other variables ( $\rho=0.42,95 \% \mathrm{CI} 0.27$ to 0.57 ). Moreover, medical expenses between 2016 and 2019 [5] yielded a weak positive partial correlation with the proclivity to get vaccinated [13] ( $\rho=0.19,95 \% \mathrm{CI} 0.03$ to 0.34 ). Interestingly, both income [3] and TCM usage frequency [7] showed positive partial correlations with the propagation of homeopathy [12] ( $\rho=0.25,95 \% \mathrm{CI} 0.07$ to 0.43 and $\rho=0.28,95 \% \mathrm{CI} 0.04$ to 0.51$)$.
The usage of vaccines [13] showed a weak negative partial correlation with perceived scientific support for TCM [8] ( $\rho=-0.26,95 \% \mathrm{CI}-0.43$ to -0.08 ). Moreover, age [2] also negatively correlated with the proclivity to get vaccinated [13] ( $\rho=-0.15,95 \% \mathrm{CI}-0.29$ to -0.01 ). Interestingly, income [3] showed a negative correlation with TCM usage frequency [7] ( $\rho=-0.19,95 \% \mathrm{CI}-0.34$ to -0.03 ), after adjusting for all other variables. A visual depiction of all partial correlations is shown in figure 4.
While the partial correlations in figure 4 show the (conditional) associations between pairs of variables, figure 5 indicates how much the variance of each variable can be explained by all other variables in the model. ${ }^{74}$ This is summarised by posterior distributions of the Bayesian R-squared measure for each variable. ${ }^{75}$ A larger R-squared for a particular variable implies that the other variables are more relevant in predicting its value.
Notably, TCM expenses and acupuncture usage frequency yielded mean R-squared values of 0.67 ( $95 \%$ CI 0.61 to 0.73 ) and 0.65 ( $95 \%$ CI 0.58 to 0.71 ), respectively. Moreover, R-squared values with a mean $>0.50$ were observed for the readiness to use booster vaccines ( $\mathrm{R}^{2}=0.56,95 \% \mathrm{CI} 0.51$ to 0.61 ), propagation of homeopathy ( $\mathrm{R}^{2}=0.56,95 \% \mathrm{CI} 0.50$ to 0.61 ), TCM usage frequency ( $\mathrm{R}^{2}=0.53,95 \% \mathrm{CI} 0.46$ to 0.61 ) and perceived scientific support for TCM ( $\mathrm{R}^{2}=0.55,95 \% \mathrm{CI} 0.47$ to 0.62 ).
Additionally, the usage of vaccines ( $\mathrm{R}^{2}=0.49,95 \% \mathrm{CI}$ 0.42 to 0.55 ), income ( $\mathrm{R}^{2}=0.42,95 \% \mathrm{CI} 0.34$ to 0.50 ), age ( $\mathrm{R}^{2}=0.44,95 \% \mathrm{CI} 0.37$ to 0.51 ) and usage of homeopathy ( $\mathrm{R}^{2}=0.41,95 \% \mathrm{CI} 0.35$ to 0.48 ) presented with mean R-squared values $>0.40$. Other sociodemographic determinants yielded lower correlations, for example, highest level of education ( $\mathrm{R}^{2}=0.33,95 \% \mathrm{CI} 0.24$ to 0.43 ), gender ( $\mathrm{R}^{2}=0.31,95 \% \mathrm{CI} 0.22$ to 0.41 ), medical expenses ( $\mathrm{R}^{2}=0.26,95 \% \mathrm{CI} 0.17$ to 0.36 ) and state of chronic disease ( $\mathrm{R}^{2}=0.24,95 \% \mathrm{CI} 0.13$ to 0.37 ). Interestingly, while there seems to be a moderately strong partial correlation between perceived scientific support for TCM and the trust in TCM-certified medical doctors, the R-squared value of 0.37 ( $95 \%$ CI 0.31 to 0.44 ) for TCM trustworthiness is comparatively low-indicating the existence of important additional variables not included in our survey.

## DISCUSSION

To the best of our knowledge, this is the first study to address usage patterns in relation to sociodemographic

![img-2.jpeg](img-2.jpeg)

Figure 3 Bayesian network model depicting (A) partial correlations and (B) marginal correlations of variables obtained through the cross-sectional survey. Blue edges indicate positive (partial) correlations, while red edges represent negative (partial) correlations. The circles around the nodes give the posterior mean of the explained variance for the respective variable (more precisely depicted in figure 5). The absolutes reported beneath each model indicate the effect size of the thickest observable edge. MD, medical doctor; TCM, traditional Chinese medicine.
parameters in a Central European population, outside of the European Social Survey. Also, our study is the first to use a Bayesian Gaussian copula graphical model to explore these connections. The fact that the majority of respondents reported awareness of TCM indicates that the practice has been promulgated throughout the Austrian population. Furthermore, with over a half of women and
over a third of men reporting to have used TCM between 2016 and 2019, TCM appears to have a notable role as a healthcare modality within the Austrian population. This is reflected in the public perception that TCM is mostly or completely supported by scientific evidence, with twothirds of women and almost half of men holding this view. The discrepancy between perception of TCM and

Partial correlations between all variables (poststratified)
![img-3.jpeg](img-3.jpeg)

Figure 4 Detailed summary of partial correlations observed in the Bayesian network model for all included nodes. Partial correlations are summarised with posterior means and $95 \%$ credible intervals. MD, medical doctor; TCM, traditional Chinese medicine.

![img-4.jpeg](img-4.jpeg)

Figure 5 Posterior distributions of the variance explained by all other variables in the model, shown for each queried item. MD, medical doctor; TCM, traditional Chinese medicine.
empirical support might stem from complex socioscientific interactions and is explored in the paragraphs below.

## Public perception of science

Personal perception of scientific support for TCM was determined by asking the question: "Do you agree with TCM being a science-backed treatment modality?" While on the surface a simple question, an accurate response depends on a mutual understanding of the definition of science. This raises issues as, even within the domain of science, the word 'science' encompasses a number of definitions, including a method of inquiry, a systematised body of knowledge and a social construct. ${ }^{80}$ In addition, it is plausible that the public interpretation of science extends beyond the formal definitions accounted for in this study. Although there is little evidence available for the Austrian population, this is exemplified in a survey of a British population, in which public attitudes towards science were recorded, and science was found to be collectively understood as a broad and ambiguous topic tantamount to technological advancement. The most popular ideas that emerged when asked to think about science included the three branches of science studied at school, that is, physics, chemistry and biology ( $24 \%$ ), and simply 'school' ( $12 \%$ ). Other answers included 'chemicals', 'white', 'coats', 'tubes' and 'nature'. ${ }^{81}$ While a survey of this nature calls into question the public's understanding of the definition of science, it does not report on the level of science literacy. Evidence in this domain suggests that the public have mixed levels of scientific literacy. Indeed, when querying an Italian population, Bucchi and Saracino found that over a third of respondents did not know
that the sun is not a planet, electrons are smaller than atoms or that antibiotics do not kill viruses. ${ }^{82}$

## Confounding factors in the public understanding of TCM's scientific support

While TCM's appeals to tradition stand in contrast to modern evidence-based medicine, written records of TCM have nonetheless led researcher's on the path to medical discoveries, namely artemisinin and arsenic trioxide. ${ }^{2383-86}$ Discoveries such as these imply a validity to TCM, which could promote public acceptance of TCM's scientific veracity. However, it is important to note that these therapeutics reached clinical acceptance through strict adherence to scientific principles. ${ }^{838487-89}$

Moreover, the superficial resemblance of TCM to conventional medicine may suggest to the public that both practices uphold comparable scientific rigour. This phenomenon has been discussed by Lobera and Rogero-Garcia who argue that the scientific appearance of alternative therapies can instil a sense of trust in the layperson. ${ }^{90}$ Concurrent with this effect is authority bias, in which experts are credited with competence by virtue of their position. Commonly experienced in a medical setting, it is conceivable that TCM projects a sense of medical authenticity through authority bias. ${ }^{91}$

Altogether, an imprecise public perception of science in combination with TCM's historical ties in the development of conventional treatments; the superficial resemblance of TCM and conventional medicine and the eminence-based veil through which TCM is communicated ${ }^{23}$ could be contributing factors towards a belief that TCM is sufficiently supported by scientific evidence.

Future studies may benefit from predefining the term 'science' with keywords or including qualifying questions to assess science literacy in their survey.

## Public trust in TCM-certified doctors

Notwithstanding the disparity between perceived scientific support and the absence of credible evidence that applies to many TCM treatments, the Austrian general public's trust in TCM-certified medical doctors is high. Our data show that $83.3 \%$ of women and $70.2 \%$ of men 'mostly' or 'completely trust' physicians with a TCM degree. While efforts have been made to introduce different item scales to standardise the measurement of trust between patients and physicians, high-quality data are scarce. Nevertheless, it seems generally accepted to distinguish between two modalities: social trust and interpersonal trust. ${ }^{92} 93$ Covering social trust, a Dutch study conducted by van der Schee et al showed trust in CAM to be associated with positive media coverage, recommendation by acquaintances and personal experience with CAM. Moreover, the analysis showed trust in CAM practitioners to increase with awarded institutional guarantees; $86.3 \%$ of participants reported an increase of trust should the CAM practitioners also hold a degree in conventional medicine-a finding corroborated by a study analysing a German population. ${ }^{5794}$

Analogous to the aforementioned impact of aesthetics on perceived scientific support for TCM, the showcasing of CAM certificates and degrees, as well as partnerships with official CAM associations, appears to enhance trust in TCM practitioners. ${ }^{57}$ This hypothesis aligns with our results since a positive partial correlation between trust in TCM doctors and perceived scientific support for TCM was observed-supporting the notion that the perception of TCM's scientific fundamentals by the general public might also depend on the institutionalisation, official recognition and certification of TCM education. Indeed, official TCM degrees can be acquired for substantial amounts of money at multiple universities, TCM schools and educational institutions in Austria. ${ }^{95-99}$ Moreover, the influence of the scientific community and scientific journals on the portrayal of TCM has to be critically examined. For example, bought special issues in Nature (2011) and Science (2014) lend credibility and visibility to TCM practices. ${ }^{100101}$

## Public expenses on TCM

Regarding TCM expenses, our data show that approximately $10 \%$ of participants spent more than a total of €750 on TCM between 2016 and 2019. This finding is interesting since out-of-pocket payments for medical care approximate a total of €901.25 per capita per annum in Austria. ${ }^{55} 102$ Importantly, Austria employs a compulsory healthcare insurance system with the possibility of optional private healthcare. In this context, it has to be emphasised that in Austria the coverage of CAM by tax-financed healthcare insurance has been a topic of political discourse. ${ }^{103}$ Yet, the idea of integrating CAM therapies within national healthcare services when there is insufficient empirical evidence to validate their efficacy and safety is not unique to Austria. This development is connected to the political and economic dimensions of TCM. ${ }^{5}$ It is a declared goal of the Chinese Communist Party that TCM should be (i) universally accessible for the Chinese population, (ii) attract health tourists to China and (iii) spread its influence across the world. ${ }^{245}$ Indeed, the WHO Traditional Medicine Strategy 2014-2023, considers 'promoting universal health coverage by integrating T\&CM (traditional medicine and complementary medicine) services and self-healthcare into national health systems ${ }^{, 7}$ one of its three main objectives. An inclusion of TCM diagnostic criteria in the ICD-11 thus makes the diagnoses billable to insurance companies, furthering the expansion of TCM as a worldwide business model, despite the scientific basis of many TCM treatments being refuted. ${ }^{5}$

## Study limitations

As the cross-sectional survey included retrospective components, answers are naturally prone to response and recall bias. Moreover, as we did not record (i) the number of individuals approached in the street survey and (ii) the number of individuals that accessed our online survey, we are unable to provide a survey refusal and response rate. Nonetheless, it must be noted that on usage of multivariate models, non-response bias does not necessarily alter results. ${ }^{104}$ In order to obtain a larger sample size, an online survey was performed in addition to the street survey. Although this increase in participants allowed for usage of poststratification techniques, a sample size of 1307 still calls for cautious interpretation of data.

Furthermore, because the survey was uploaded to the website of Austria's most popular free newspaper ('Heute'), the collected sample might partially reflect the characteristics of its regular readership rather than the general population. Additionally, a relative under-representation of male participants can be found in our study population. To address this, we poststratified our sample with data deriving from 'Statistik Austria' (Austria's Federal Statistical Office) in order to more closely represent the Austrian general population. As our data are limited to Austria, future studies are warranted to investigate our findings on an international scale. Moreover, as CAM can be a polarising subject, it is possible that our survey may have selected for respondents with strong opinions towards complementary medicine. Adding to this issue, it is also possible that the link to our survey might have been shared in CAM-themed fora. Furthermore, as disclosure of nationality was left to the discretion of respondents, it is possible that our sample may positively skew towards East-Asian ethnicities. However, as Chinese citizens only make up around $0.15 \%$ of the Austrian population, ${ }^{105}$ it is unlikely that putative over-representation of a Chinese population would

have distorted our data significantly. This corresponds with our sample as only one participant ( $0.07 \%$ ) had Chinese citizenship.

## CONCLUSION

An indisputable disparity exists between the public notion that TCM is supported by scientific evidence and the empirical evidence itself, which portrays a widely unsubstantiated alternative medical practice. Arguably, this discrepancy is also mirrored in political decisions that enhance the credibility of CAM by encouraging its institutionalisation and integration within national healthcare systems. Considering the lack of evidence proving TCM's efficacy and safety, its endorsement of pharmacologically active agentsand simplified authorisation thereof-as well as the efforts made to criminalise TCM criticism in China, medical authorities should focus on a critical examination of TCM. Accordingly, treatments supported by empirical evidence should be pursued, and critical discourse based on scientific principles should be fostered. Furthermore, medical authorities should adhere to strict intellectual honesty, and place an emphasis on improving the scientific literacy of the general public to safeguard informed patient-driven decision-making, especially in the face of potential misinformation and disinformation.

## Author affiliations

${ }^{1}$ Center for Physiology and Pharmacology, Institute of Pharmacology, Medical University of Vienna, Wien, Austria
${ }^{2}$ Institute of Microbiology and Infection, University of Birmingham School of Dentistry, Birmingham, UK
${ }^{3}$ Department of Psychological Methods, University of Amsterdam, Amsterdam, The Netherlands

Twitter Michael Eigenschink @Meigenschink and Luise Bellach @LBellach
Acknowledgements The authors of the manuscript are particularly grateful for the assistance of the interviewers who voluntarily participated in the creation of our dataset and, therefore, laid the foundation for the study and the present manuscript. Moreover, the authors thank Lisa Krammer and Lukas Dearing for their valuable comments on the questionnaire, and Donald Williams for answering questions about his BGLM package.
Contributors Guarantor: ME; conceptualisation: ME, LB, TED, JM, HHS; methodology: ME and TED; survey: ME, LB, TED, JM, HHS; data analysis: FD and ME; data curation: FD and ME; writing—original draft preparation: ME, LB, FD and SL; writing—review and editing: JM, SL, FD and HHS; project supervision: HHS. All authors have read and agreed to the submitted version of the manuscript.
Funding The study was funded by the Medical University of Vienna.
Competing interests None declared.
Patient and public involvement Patients and/or the public were not involved in the design, or conduct, or reporting, or dissemination plans of this research.
Patient consent for publication Not applicable.
Ethics approval After correspondence with the chair of the ethics committee of the Medical University of Vienna, due to the study design, approval by an ethics committee was not required. The study was exempted from further approvals. Participants gave informed consent to participate in the study before taking part.
Provenance and peer review Not commissioned; externally peer reviewed.

Data availability statement Data are available in a public, open access repository. The datasets used and/or analysed during the current study are readily available from our GitHub repository: DOI: 10.5281/zenodo.7313185.
Supplemental material This content has been supplied by the author(s). It has not been vetted by BMJ Publishing Group Limited (BMJ) and may not have been peer-reviewed. Any opinions or recommendations discussed are solely those of the author(s) and are not endorsed by BMJ. BMJ disclaims all liability and responsibility arising from any reliance placed on the content. Where the content includes any translated material, BMJ does not warrant the accuracy and reliability of the translations (including but not limited to local regulations, clinical guidelines, terminology, drug names and drug dosages), and is not responsible for any error and/or omissions arising from translation and adaptation or otherwise.
Open access This is an open access article distributed in accordance with the Creative Commons Attribution Non Commercial (CC BY-NC 4.0) license, which permits others to distribute, remix, adapt, build upon this work non-commercially, and license their derivative works on different terms, provided the original work is properly cited, appropriate credit is given, any changes made indicated, and the use is non-commercial. See: http://creativecommons.org/licenses/by-nc/4.0/.

## ORCID IDs

Michael Eigenschink http://orcid.org/0000-0001-6469-5014
Luise Bellach http://orcid.org/0000-0001-7026-0033
Julian Maier http://orcid.org/0000-0001-6016-1947
Fabian Dablander http://orcid.org/0000-0003-2650-6491
Harald H Sitte http://orcid.org/0000-0002-1339-7444
