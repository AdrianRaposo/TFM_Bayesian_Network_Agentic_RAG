# Antimicrobials for the treatment of drugresistant Acinetobacter baumannii pneumonia in critically ill patients: a systemic review and Bayesian network meta-analysis 

Su Young Jung ${ }^{1,2}$, Seung Hee Lee ${ }^{1}$, Soo Young Lee ${ }^{3,4}$, Seungwon Yang ${ }^{5}$, Hayeon Noh ${ }^{5}$, Eun Kyoung Chung ${ }^{3 *+}$ and Jangik I. Lee ${ }^{1,2 *+}$


#### Abstract

Background: An optimal therapy for the treatment of pneumonia caused by drug-resistant Acinetobacter baumannii remains unclear. This study aims to compare various antimicrobial strategies and to determine the most effective therapy for pneumonia using a network meta-analysis.


Methods: Systematic search and quality assessment were performed to select eligible studies reporting one of the following outcomes: all-cause mortality, clinical cure, and microbiological eradication. The primary outcome was allcause mortality. A network meta-analysis was conducted with a Bayesian approach. Antimicrobial treatments were ranked based on surface under the cumulative ranking curve (SUCRA) value along with estimated median outcome rate and corresponding $95 \%$ credible intervals (CrIs). Two treatments were considered significantly different if a posterior probability of superiority $(P)$ was greater than $97.5 \%$.
Results: Twenty-three studies evaluating 15 antimicrobial treatments were included. Intravenous colistin monotherapy (IV COL) was selected as a common comparator, serving as a bridge for developing the network. Five treatments ranked higher than IV COL (SUCRA, 57.1\%; median all-cause mortality $0.45,95 \%$ CrI $0.41-0.48$ ) for reducing all-cause mortality: sulbactam monotherapy (SUL, 100.0\%; 0.18, 0.04-0.42), high-dose SUL (HD SUL, 85.7\%; $0.31,0.07-0.71$ ), fosfomycin plus IV COL (FOS + IV COL, 78.6\%; 0.34, 0.19-0.54), inhaled COL plus IV COL (IH COL + IV COL, $71.4 \% ; 0.39,0.32-0.46$ ), and high-dose tigecycline (HD TIG, $71.4 \% ; 0.39,0.16-0.67$ ). Those five treatments also ranked higher than IV COL (SUCRA, 45.5\%) for improving clinical cure ( $72.7 \%, 72.7 \%, 63.6 \%, 81.8 \%$, and $90.9 \%$, respectively). Among the five treatments, SUL ( $P=98.1 \%$ ) and IH COL + IV COL ( $P=99.9 \%$ ) were significantly superior to IV COL for patient survival and clinical cure, respectively. In terms of microbiological eradication, FOS + IV COL $(P=99.8 \%)$ and SUL $(P=98.9 \%)$ were significantly superior to IV COL.
(Continued on next page)

[^0]
[^0]:    * Correspondence: cekchung@khu.ac.kr; jangik.lee@snu.ac.kr
    ${ }^{\dagger}$ Equal contributors
    ${ }^{3}$ Department of Pharmacy, College of Pharmacy, Kyung Hee University, 26
    Kyungheedae-ro, Dongdaemun-gu, Seoul 02447, Republic of Korea
    ${ }^{+}$Department of Pharmacy, College of Pharmacy, Seoul National University, 1
    Gwanak-ro, Gwanak-gu, Seoul 08826, Republic of Korea
    Full list of author information is available at the end of the article

## Conclusions

This Bayesian network meta-analysis demonstrated the comparative effectiveness of fifteen antimicrobial treatments for drug-resistant A. baumannii pneumonia in critically ill patients. For survival benefit, SUL appears to be the best treatment followed by HD SUL, FOS + IV COL, IH COL + IV COL, HD TIG, and IV COL therapy, in numerical order.

## Keywords

Pneumonia, Critically ill patients, Antimicrobials, Drug-resistant, Acinetobacter baumannii, Network meta-analysis

## Background

Nosocomial pneumonia is a leading cause of death in critically ill patients [1, 2]. The mortality rates associated with hospital-acquired pneumonia (HAP) or ventilator-associated pneumonia (VAP) in intensive care units (ICU) range from 38% to 70% or higher [3, 4]. One of the most common pathogens of nosocomial pneumonia is Acinetobacter baumannii (A. baumannii). Because A. baumannii exhibits relatively high virulence and antimicrobial resistance compared with other organisms, the prevalence of multidrug-resistant (MDR) or extensively drug-resistant (XDR) A. baumannii has kept increasing to at least 80% in past decades [5]. One of the important risk factors for MDR/XDR-bacterial infections in ICU is an inappropriate antibiotic therapy [6]. Considering the paucity of clinical data on the comparative effectiveness of various antimicrobial treatments for MDR/XDR A. baumannii pneumonia, it is pressing to accumulate clinically reliable scientific evidence to guide the selection of an optimal antimicrobial treatment for the infection.

Colistin-based, sulbactam-based and tigecycline-based antimicrobial treatments are currently considered the reserved treatment options for MDR/XDR A. baumannii infections [7, 8]. However, the clinical data comparing the antimicrobial treatments adequately with respect to the effectiveness and safety of the treatment of such infections, particularly nosocomial pneumonia, are inconsistent owing to small sample sizes, and substantial between-study heterogeneity [9--13]. In addition, to date there is no consensus based on strong evidence to confirm the therapeutic superiority of a monotherapy or combination therapy and clinical preferences among various antimicrobial combination regimens [9, 10]. Therefore, clinicians are still facing challenges to apply evidence-based pharmacotherapy in clinical practice for the treatment of nosocomial pneumonia.

Currently available studies have compared the effectiveness of different antimicrobial treatment options only in pairs within the studies [14--16]. Although the results from those studies are informative, the relative effectiveness throughout a variety of therapeutic options remains unknown. Network meta-analysis (NMA) is a relatively novel meta-analysis strategy that integrates both direct evidence from pairwise comparisons within a study and indirect evidence from common-comparator comparisons across the studies [17, 18]. Compared with conventional meta-analyses, NMA allows comparisons across multiple treatments simultaneously even when the treatments were not directly compared in previous studies. Furthermore, NMA using a Bayesian approach uniquely provides the probability estimates that enable clinicians to make an intuitive pharmacotherapy decision [19]. The Bayesian approach allows us to adopt the strengths from data across multiple studies and does not require an assumption of normal distribution [20]. Therefore, the approach is more favorable than the frequentist approach when small numbers of studies are included in each pair of comparisons.

The aim of this study was to evaluate the comparative effectiveness of currently available antimicrobial options, including monotherapy and combination therapy, for the treatment of critically ill patients with nosocomial pneumonia caused by MDR/XDR A. baumannii, using a Bayesian NMA approach.

## Methods

A systematic review and the Bayesian NMA were performed in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-analyses (PRISMA) extension statement for network metaanalyses [21].

### Search strategy

A comprehensive literature search was performed using the electronic databases of PubMed, Embase, and the Cochrane Central Register of Controlled Trials from the inception of each database to 31 March 2017. The literature search was limited to human studies without language restrictions. In order to identify appropriate articles that evaluated the antimicrobial treatments for patients with nosocomial pneumonia caused by MDR/XDR pathogens, the following text words and medical subject heading (MeSH) terms were used: “pneumonia”, “HAP”, or “VAP”; “drug resistant”, “carbapenem-resistant”, “MDR”, or “XDR”; “aminoglycoside”, “carbapenems”,

“colistin”, “fosfomycin”, “glycopeptide”, “glycylcycline”, “polymyxin”, “rifampin”, “sulbactam”, or “tigecycline”. In addition, proceedings from relevant conferences and the references that were listed in all retrieved articles were also manually searched to ensure a complete identification of all eligible studies.

## Selection criteria

The types of study included in the analysis were randomized controlled trials (RCTs) and observational studies in which antimicrobial agents were compared in the treatment of critically ill adult patients with HAP or VAP caused by MDR/XDR A. baumannii. Studies were included if they evaluated at least one of the following three outcomes with clear definitions: all-cause mortality, clinical cure, or microbiological eradication. All-cause mortality, defined as the incidence of deaths from any cause in ICU within the follow-up duration of approximately 30 days, was chosen as the primary outcome variable for the comparison of antimicrobial effectiveness. If all-cause mortality in the ICU was not available in the studies, in-hospital mortality data were used. Clinical cure and microbiological eradication were selected as the secondary outcome variables. Clinical cure was defined as a resolution of signs and symptoms of pneumonia by the end of therapy, whereas microbiological eradication was defined as a confirmed negative result in a follow-up bacterial culture by the end of therapy.

Excluded studies are as follows: (1) case series, (2) studies that enrolled pediatric patients, (3) studies that enrolled patients with community-acquired pneumonia, and (4) studies in which less than half of study population had pneumonia.

## Quality assessment and data extraction

Two investigators (SYJ and SHL) independently screened the titles and abstracts of the articles, and reviewed their full texts based on the pre-specified selection criteria. Any inconsistencies between the two investigators were resolved by extensive discussion with the third investigator (HN). Quality assessment of included studies was performed by two investigators (SYJ and SHL), and was crosschecked by the third investigator (SY). The quality of included RCTs was assessed using the Cochrane Collaboration Risk of Bias Tool [22]. The quality of observational studies was evaluated using the Newcastle-Ottawa Scale (NOS) [23]. Studies with an NOS score <7 were considered at high risk of bias [24, 25]. After excluding the studies with high risk of bias, the remaining studies were included in the final analyses. Two investigators (SYJ and SHL) independently extracted the following data from each study using a standardized extraction form: year of publication, type of study design (i.e. RCT or observational study), patient population characteristics, specific antimicrobial therapy with dosing strategy as either an intervention or a comparator, and outcome measurements with their definitions. Antimicrobials administrated at greater than standard dosage for the treatment of MDR/XDR A. baumannii pneumonia were separately categorized as high-dose regimens for each antimicrobial agent, as referred to in previous studies [26--28].

## Data synthesis and analysis

Pairwise meta-analyses were initially performed for direct comparisons between different antimicrobial treatments using Stata software (version 13.0, StataCorp, College Station, TX, USA). Homogeneity and consistency were assumed in drawing valid conclusions from NMA analyses [29]. Homogeneity assumption was satisfied when the magnitude of heterogeneity within direct pairwise comparisons was acceptable. Heterogeneity of the treatment effects across trials in each pair was examined by the Q test and quantified using the I^{2} statistic. The I^{2} values < 40%, 40%--75%, and > 75% accompanied by a p value <0.10 from the Q test were considered mild, moderate, and high heterogeneity, respectively [30]. A consistency assumption referring to the lack of disagreements between direct and indirect comparisons was required to be met in integrating direct and indirect evidence in the NMA [31]. Inconsistency in the entire network of each outcome was assessed by either the Lu-Ades model or design-by-treatment interaction model, according to a configuration of the loop in the network [32--34]. The consistency assumption was rejected when the p value of the inconsistency test was < 0.05. Publication bias was also evaluated with a funnel plot and Egger's test if ten or more studies were included in each pairwise meta-analysis [30].

The Bayesian NMA was performed for multiple comparisons using WinBUGS (version 1.4.3, MRC Biostatistics Unit, Cambridge, UK). Both fixed-effect and random-effect models were fitted. The best model was chosen based on the deviance information criterion (DIC) that suggests a significantly better fit of the model with a value lowered by 2--3 points [35]. Markov chain Monte Carlo (MCMC) samplers were run in WinBUGS using three chains with different initial values. Non-informative priors were used to produce posterior distribution for the treatment effects, allowing the data to dominate the final estimates (vague normal distribution with mean of 0 and variance of 0.0001). There were 10,000 updates generated for each set of the chains, and the first 10,000 iterations were discarded as the burn-in phase. Brooks-Gelman-Rubin diagnostic plots were used to verify the convergence of the MCMC simulations [36].

The estimates of Bayesian NMA were reported as rank probabilities to identify the relative rankings of antimicrobial treatments based on the surface under the cumulative ranking curve (SUCRA), ranging from 0% (statistically certain to be the worst treatment) to 100% (statistically certain to be the best treatment) [37]. Because SUCRA rankings could exaggerate the small differences since those are relative values, the estimates of median outcome rates were also reported with the corresponding 95% credible intervals (CrIs) to specify the absolute magnitude of therapeutic effectiveness. Then, Bayesian posterior probabilities of superiority were calculated to identify a significant difference between an individual treatment and a common comparator. The probabilities of superiority (P) indicated the probabilities of the odds ratio (OR) being < 1 for all-cause mortality and > 1 for clinical cure and microbiological eradication. The treatment with P > 97.5% or P < 2.5% was considered statistically superior or inferior to the comparator, respectively [38--40]. Although whether or not a confidence interval (CI) for the OR not crosses 1 determines a statistically significant difference in frequentist statistics, the concept of posterior probability in Bayesian statistics was used to demonstrate the certainty of comparative results [41--43].

Sensitivity analyses were performed to evaluate the robustness of the Bayesian NMA results. Although most patients included in this analysis had drug-resistant A. baumannii pneumonia, the comparative effectiveness of antimicrobial treatments could be affected by type(s) of infection other than pneumonia or causative pathogen(s) other than A. baumannii. Therefore, two sensitivity analyses were performed exclusively using the studies in which all patients had pneumonia or were infected by A. baumannii, respectively.

## Results

### Study selection and quality assessment

A total of 6688 articles were identified through the electronic database search. Additional 4 records were identified through a manual search by reviewing conference proceedings and the reference lists of retrieved articles. After removing 2017 duplicates, 4675 articles were assessed for relevance by screening the title and abstract. Afterward, 128 relevant articles were screened for eligibility by full-text evaluations. Finally, 23 articles that met the inclusion criteria were included in our Bayesian NMA (Fig. 1). Those 23 articles consist of four RCTs [44--47], three prospective observational studies [48--50], and sixteen retrospective studies [51--66]. A PRISMA extension checklist for reporting systematic reviews comparing multiple treatments involving NMA is shown in Additional file 1: Table S1.

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Study selection process according to the Preferred Reporting Items for Systematic Reviews and Meta-analyses guideline

The results of quality assessment for the included studies are shown in Additional file 2: Table S2 and Table S3. None of the RCTs had high risk of bias for sequence generation, addressing outcome data, selective reporting, or funding source. However, two studies had high risk of bias for double blinding. Bias assessment for allocation concealment was difficult owing to insufficient information available in most studies. All observational studies had a total bias score of at least 7 points based on the NOS, which indicates a low risk of bias.

### Study characteristics

The Bayesian NMA was performed using 23 studies that consist of a total of 2118 adult patients. Table 1 shows the characteristics of the studies including patient population, antimicrobial therapy with a total daily dose, and outcomes of each study. The NMA evaluated 15 different antimicrobial treatments, including intravenous colistin (IV COL), sulbactam (SUL), and tigecycline (TIG) as monotherapy or combination therapy. Among them, SUL and TIG administrated at their higher doses were separately categorized as high-dose (HD) regimens: HD SUL defined as a total daily dose of 9 g/day or higher and HD TIG as a total daily dose of 200 mg/day after a loading dose of 200 mg [49, 52]. Across the studies analyzed, the mean (or median) age of the patients ranged from 48 to 82 years, and the mean Acute Physiology and Chronic Health Evaluation II (APACHE II) score from 12 to 24. Most studies reported two-arm

Table 1 Characteristics of the studies included in the Bayesian network meta-analysis


Table 1 Characteristics of the studies included in the Bayesian network meta-analysis (Continued)


Abbreviations: AB Acinetobacter baumannii, CAR carbapenem, COL colistin (mostly in colistin base activity (CBA) units), CR carbapenem-resistant, FOS fosfomycin, GLY glycopeptide, HAP hospital-acquired pneumonia, HD high dose, IH inhaled, IV intravenous, IMI imipenem, KP Klebsiella pneumoniae, MDR multidrug-resistant, MERO meropenem, MIU million international units, $n / N$ number of outcome events/number of patients in each intervention, NR not reported, PA Pseudomonas aeruginosa, RIF rifampin, SAPS Simplified Acute Physiology Score, SOFA Sepsis-Related Organ Failure Assessment score, SUL sulbactam (frequently used with ampicillin but described only as SUL in the table), TDM therapeutic drug monitoring, TEI teicoplanin, TIG tigecycline, VAN vancomycin, VAP ventilator-associated pneumonia, XDR extensively drug-resistant ${ }^{\text {a }}$ COL $1 \mathrm{MIU} \approx 30 \mathrm{mg}$ of colistin base activity (CBA) $\approx 80 \mathrm{mg}$ of colistimethate (CMS) ${ }^{\text {b }}$ Values are mean Acute Physiology and Chronic Health Evaluation II score unless otherwise indicated ${ }^{\text {c }}$ Other types: bloodstream infection 20\%, complicated intra-abdominal infection $2 \%$ ${ }^{\text {d }}$ Other types: bloodstream infection $14 \%$ ${ }^{\text {e }}$ Median value ${ }^{\text {f }}$ Mean value ${ }^{\text {g }}$ Other types: bloodstream infection 13\%, wound infection 5\%, peritonitis 3\%, urinary tract infection $2 \%$, biliary tract infection $2 \%$ ${ }^{\text {h }}$ Other types: bloodstream infection 19\%, etc. 17\% ${ }^{\text {i }}$ Other types: bloodstream infection 5\%, urinary tract infection 5\%, soft skin tissue infection 3\%, intra-abdominal infection 6\%, etc. 3\% comparisons except for two studies with three-arm comparisons. Figure 2 presents the network plots of direct comparisons for each outcome, showing predominant pairwise comparisons of antimicrobials with IV COL. IV COL also served as a bridge node to construct the network with a closed loop, allowing indirect comparisons within the network. Hence, IV COL was selected as a common comparator in the Bayesian NMA.

## Assessment of heterogeneity, inconsistency, and model fit

Table 2 presents the results of heterogeneity in direct pairwise comparisons involving at least two studies. Overall, no statistically significant heterogeneity was observed in most direct pairwise comparisons for each outcome $\left(I^{2}<40 \%, p>0.01\right)$ except for two comparison pairs. Comparison pairs of SUL plus IV COL (SUL + IV COL) versus carbapenem plus IV COL (CAR + IV COR) for all-cause mortality $\left(I^{2}=43.2 \%\right)$, and IV COL versus TIG for microbiological eradication $\left(I^{2}=53.4 \%\right)$ showed moderate heterogeneity, but was not statistically significant $(p>0.10)$. Publication bias was not evaluated because the number of studies included in each pair was fewer than 10 . There was no evidence of significant inconsistency in the entire network of each outcome ( $p>$ 0.05 ; Additional file 3: Table S4). Inconsistency was assessed based on the design-by-treatment interaction model because a triangle-loop of each network was formed by one three-arm and one two-arm study in common. All Bayesian NMA estimates were derived from fixed-effect models because of their better fit than that of random-effect models for all three outcomes (allcause mortality, $\mathrm{DIC}*{\text {fixed }}=84$ versus $\mathrm{DIC}*{\text {random }}=86$; clinical cure, 68 versus 70 ; microbiological eradication, 71 versus 73 ).

## Bayesian NMA ranking

The SUCRA rank probabilities and Bayesian posterior estimates of the effect of various antimicrobial treatments on all-cause mortality are presented in Fig. 3. SUL monotherapy ranked first for reducing all-cause mortality (SUCRA, 100.0\%; median outcome rate 0.18 , $95 \% \mathrm{CrI} 0.04-0.42$ ) among the 15 antimicrobial treatments. Four treatments, in addition to SUL, ranked

![img-1.jpeg](img-1.jpeg)

higher than IV COL (57.1%; 0.45, 0.41–0.48) and included HD SUL (85.7%; 0.31, 0.07–0.71), fosfomycin plus IV COL (FOS + IV COL, 78.6%; 0.34, 0.19–0.54), inhaled COL plus IV COL (IH COL + IV COL, 71.4%; 0.39, 0.32–0.46), and HD TIG (71.4%; 0.39, 0.16–0.67). Rifampin plus IV COL (RIF + IV COL, 57.1%; 0.43, 0.31–0.55) ranked the same as IV COL. SUL + IV COL (7.1%; 0.68, 0.37–0.89) ranked the lowest among the 15 different antimicrobial treatments.

Figure 4 shows the SUCRA rank probabilities and Bayesian posterior estimates of the effect of various antimicrobial treatments on clinical cure. HD TIG ranked first for improving clinical cure (SUCRA, 90.9%; median outcome rate 0.72, 95% CrI 0.43–0.91) among the 12 antimicrobial treatments. IV COL (45.5%; 0.51, 0.46–0.56) and TIG (45.5%; 0.48, 0.31–0.66) tied for seventh place. Besides HD TIG, IH COL + IV COL (81.8%; 0.64, 0.56–0.70), RIF + IV COL (72.7%; 0.63, 0.34–0.85), HD SUL (72.7%; 0.62, 0.26–0.90), SUL (72.7%; 0.60, 0.39–0.79), and FOS + IV COL (63.6%; 0.56, 0.35–0.74) ranked higher than IV COL. SUL + IV COL (0.30, 0.09–0.62) and CAR + IH COL (0.29, 0.08–0.62) were the two lowest-ranked treatments with the same SUCRA value of 9.1%.

Figure 5 presents SUCRA rank probabilities and posterior estimates of the effect of various antimicrobial treatments on microbiological eradication. FOS + IV COL ranked highest for microbiological eradication (SUCRA, 100.0%; median outcome rate 0.95, 95% CrI 0.73–1.00) among the 15 different antimicrobial treatments. SUL (92.9%; 0.85, 0.60–0.97) was next highest, followed by SUL + IH COL (85.7%; 0.80, 0.40–0.96), and RIF + IV COL (64.3%; 0.69, 0.57–0.79). CAR + IH COL (57.1%; 0.66, 0.34–0.89), CAR + IV COL (57.1%; 0.65, 0.38–0.86), and SUL + IV COL (57.1%; 0.64, 0.34–0.87) ranked fifth. IH COL + IV COL (42.9%; 0.60, 0.52–0.69), IH COL (42.9%; 0.59, 0.10–0.96), and TIG + IH COL (42.9%; 0.58, 0.19–0.90) tied for eighth place, followed by IV COL (28.6%; 0.54, 0.50–0.59). TIG (7.1%; 0.32, 0.16–0.52) was the lowest-ranked treatment among the 15 different antimicrobial treatments.

Figure 6 displays a clustered SUCRA ranking plot in the three dimensions of x-axis (all-cause mortality), y-axis (clinical cure), and bubble size (microbiological

Table 2 Direct pairwise comparisons and heterogeneity

$(95 \% \mathrm{CI})$ | Number of events | Number of patients | Number of studies | Heterogeneity test |  |

Abbreviations: CAR carbapenem (imipenem or meropenem), CI confidence interval, COL colistin, FOS fosfomycin, GLY glycopeptide (vancomycin or teicoplanin), HD high dose, IH inhaled, IV intravenous, OR odds ratio, RIF rifampin, SUL sulbactam, TIG tigecycline, vs. versus ${ }^{a}$ Quantified value of OR variation attributable to heterogeneity ${ }^{\mathrm{b}} p$ value from $Q$ test based on chi-square statistic eradication). The plot includes 12 antimicrobial treatments, commonly included in the analyses of all three outcomes. The relative size of each bubble is in proportion to the $100 \%$ SUCRA value of FOS + IV COL. IV COL fell in the center of the plot with a relatively small bubble size. Five antimicrobial treatments (SUL, HD SUL, FOS + IV COL, IH COL + IV COL, and HD TIG) fell in farther in the right upper corner of the plot than IV COL. SUL was in the farthest-right upper position with a relatively large bubble size among the five treatments, suggesting that overall, SUL is associated with a more favorable therapeutic effect than other treatments for the three outcome variables. The bubble size of both HD SUL and HD TIG was relatively small among the top 5 treatments placed in the farthest-right upper corner, indicating that those treatments have relatively lower benefits in terms of microbiological eradication.

## Bayesian posterior probability of superiority

Table 3 presents the Bayesian probabilities of superiority to IV COL, the key comparator in NMA networks. SUL was significantly superior to IV COL for reducing all-cause mortality (OR $0.27,95 \% \mathrm{CrI}$ $0.06-0.91$ ) with a $98.1 \%$ probability of superiority $(P)$. TIG (OR $1.75,95 \% \mathrm{CrI} 1.09-2.81$ ) demonstrated a higher all-cause mortality rate than IV COL with $1.0 \%$ of $P$, indicating that TIG is significantly inferior to IV COL ( $P<2.5 \%$ ) for reducing all-cause mortality. In terms of clinical cure, only IH COL + IV COL was significantly superior to IV COL (OR $1.67,95 \% \mathrm{CrI}$ $1.20-2.29$ ) with a $P$ of $99.9 \%$. Except for IH COL + IV COL, there were no statistically significant differences between IV COL and the other 10 antimicrobial treatments that were evaluated in the NMA for the clinical cure outcome. FOS + IV COL (OR 15.20, 95\% CrI $2.27-428.60$ ), RIF + IV COL (1.88, 1.14-3.13), and SUL (4.82, 1.22-25.83) were significantly superior to IV COL in terms of microbiological eradication rate (Table $3 ; P=99.8 \%, 99.4 \%$, and $98.9 \%$, respectively). On the other hand, TIG was significantly inferior to IV COL ( $P=1.7 \%$; OR $0.40,95 \% \mathrm{CrI} 0.16-0.94$ ) in microbiological eradication.

![img-2.jpeg](img-2.jpeg)

Fig. 3 Surface under the cumulative ranking curve (SUCRA) rankings and posterior estimates of treatment effect on all-cause mortality. Greater SUCRA value indicates higher probability of being the best treatment for reducing all-cause mortality. Abbreviations: CAR carbapenem (imipenem or meropenem), COL colistin, CrI credible interval, FOS fosfomycin, GLY glycopeptide (vancomycin or teicoplanin), HD high-dose, IH inhaled, IV intravenous, RIF rifampin, SUL sulbactam, TIG tigecycline

$\%$ | Posterior estimates
Median (95\% CrI) |   |

Fig. 4 Surface under the cumulative ranking curve (SUCRA) rankings and posterior estimates of treatment effect on clinical cure. Greater SUCRA value indicates higher probability of being the best treatment for improving clinical cure. Abbreviations: CAR carbapenem (imipenem or meropenem), COL colistin, CrI credible interval, FOS fosfomycin, GLY glycopeptide (vancomycin or teicoplanin), HD high-dose, IH inhaled, IV intravenous, RIF rifampin, SUL sulbactam, TIG tigecycline

![img-3.jpeg](img-3.jpeg)

Fig. 5 Surface under the cumulative ranking curve (SUCRA) rankings and posterior estimates of treatment effect on microbiological eradication. Greater SUCRA value indicates higher probability of being the best treatment for improving microbiological eradication. Abbreviations: CAR carbapenem (imipenem or meropenem), COL colistin, Crl credible interval, FOS fosfomycin, GLY glycopeptide (vancomycin or teicoplanin), HD high-dose, IH inhaled, IV intravenous, RIF rifampin, SUL sulbactam, TIG tigecycline

![img-4.jpeg](img-4.jpeg)

Fig. 6 Clustered ranking plot based on surface under the cumulative ranking curve (SUCRA). The plot shows SUCRA values of twelve antimicrobial treatments, commonly included in the analyses of the following outcomes: all-cause mortality, clinical cure, and microbiological eradication. A treatment lying in the farther-right upper corner is more effective in both all-cause mortality and clinical cure than other treatments. In addition, the larger bubble size reflects the greater SUCRA value in terms of microbiological eradication. Abbreviations: CAR carbapenem (imipenem or meropenem), COL colistin, FOS fosfomycin, GLY glycopeptide (vancomycin or teicoplanin), HD high-dose, IH inhaled, IV intravenous, RIF rifampin, SUL sulbactam, TIG tigecycline

Table 3 Bayesian NMA estimates of probability of superiority (P) and odds ratio (OR)


Abbreviations: CAR carbapenem (imipenem or meropenem), COL colistin, CrI credible interval, FOS fosfomycin, GLY glycopeptide (vancomycin or teicoplanin), HD high-dose, IH inhaled, IV intravenous, NA not available, RIF rifampin, SUL sulbactam, TIG tigecycline ${ }^{*} P>97.5 \%$ and $P<2.5 \%$, statistically significant superiority and inferiority, respectively

## Sensitivity analyses

According to the sensitivity analyses (Additional file 4: Table S5), the orders based on SUCRA values and statistical significance remained similar after removing specific studies from the analysis pool. For the first sensitivity analysis, six studies were eliminated from the original study pool because patients with other infectious diseases besides pneumonia were enrolled in those studies, though the proportion was small. Even after removing those six studies, the SUCRA rankings were comparable with those in the main analysis. In another sensitivity analysis exclusively using 14 studies in which all patients were infected by A. baumannii, the SUCRA value for IH COL + IV COL therapy was lower, especially for clinical cure, because most of the studies comparing IH COL + IV COL with IV COL were excluded. This sensitivity analysis suggests the robustness of our analysis by showing that concurrent infection site(s) other than the respiratory tract and the type of causative pathogen may not markedly affect the comparative effectiveness estimates of the antimicrobial treatments evaluated in this NMA.

## Discussion

To the best of our knowledge, this is the first and the most comprehensive Bayesian NMA evaluating the comparative effectiveness of various antimicrobial treatment regimens for MDR/XDR A. baumannii pneumonia in critically ill patients. An important finding of our study is that SUL was the most effective therapy to reduce the all-cause mortality in critically ill patients. The top five treatments with high probabilities of survival benefit were SUL (SUCRA 100.0\%), HD SUL (85.7\%), FOS + IV COL (78.6\%), IH COL + IV COL (71.4\%), and HD TIG (71.4\%) (Fig. 3). Those five treatment options generally ranked high for improving clinical cure and microbiological eradication as well. However, HD TIG and HD SUL had relatively lower SUCRA values for microbiological eradication among the 15 different antimicrobial treatments. A possible explanation for those lower rankings in microbiological eradication is that, based on the published data, A. baumannii isolates in the two HD treatment groups were less susceptible to TIG or SUL (MIC $>1 \mathrm{mg} / \mathrm{L}$ for TIG; MIC $>16 \mathrm{mg} / \mathrm{L}$ for SUL, respectively) $[49,52]$.

The results of this study corroborate growing recent evidence that suggests SUL as a promising treatment option in the management of Acinetobacter infections [67-69]. Multiple clinical studies have reported that the patient group treated with SUL had a substantially low rate of mortality, ranging from $17 \%$ to $33 \%$ during approximately 2 weeks of treatment [67-70]. In addition, Oliveira et al. report that polymyxin (colistin or polymyxin B) treatment is significantly associated with higher mortality than SUL, with a relative risk of 1.52 [70]. Similarly, this Bayesian NMA demonstrated that SUL was superior to IV COL with the probabilities of superiority greater than $97.5 \%$ in terms of reducing allcause mortality and improving microbiological eradication. However, caution needs to be exercised when interpreting and applying our findings to clinical practice, owing to the retrospective nature and relatively

small sample sizes of the studies included in this NMA, and potential inherent bias, if any, in reporting the results of the original studies.

According to a recent conference report from the European Society of Intensive Care Medicine, a 4-hour infusion of SUL 3--4 g every 8 hours is recommended for severe A. baumannii infections involving isolates with higher MICs for SUL (≥8 mg/L) [10]. A recent pharmacodynamic modeling study conducted in healthy adults demonstrated that a 4-hour infusion of SUL 3 g every 8 hours would be an appropriate dosage regimen of SUL for less-susceptible A. baumannii [71]. The findings from healthy adults may not be generalizable to critically ill patients owing to pharmacokinetic alterations associated with critical illness [71, 72]. Nevertheless, it is noteworthy that prolonged-infusion dosing was found to be a much more effective strategy to achieve a high probability of target concentration attainment over a range of MICs than a dose-escalation strategy [71]. In the HD SUL treatment group in this NMA, the infusion time of HD SUL was within 1 hour even though SUL MIC for isolated A. baumannii was > 16 mg/L [49]. It could be inferred that a more prolonged infusion time was necessary for improving microbiological eradication, considering the time-dependent antimicrobial activity of SUL [72].

Among combination regimens evaluated in this NMA, FOS + IV COL and IH COL + IV COL had a more beneficial effect on all-cause mortality, with favorable effectiveness in clinical cure and microbiological eradication (Fig. 6). In terms of microbiological eradication, FOS + IV COL demonstrated the greatest SUCRA value in our Bayesian NMA. FOS may be an effective adjunctive therapy for pneumonia caused by MDR/XDR A. baumannii, considering the synergistic effect of COL and FOS in vitro [73--75]. However, owing to the paucity of clinical data evaluating the efficacy and safety of FOS + IV COL, adjunctive FOS should be used with caution until clinical studies adequately confirm its promising effect in patients with severe pneumonia. According to the guideline recently updated by the Infectious Diseases Society of America, adjunct IH COL therapy is suggested for the treatment of HAP/VAP due to A. baumannii that is sensitive only to COL, particularly for patients with insufficient response to IV COL monotherapy [76]. Similarly, in this NMA, the probability of superiority analysis showed that IH COL + IV COL yielded additional therapeutic superiority in terms of clinical cure, and comparable effectiveness in other outcomes, compared with IV COL.

Besides IH COL, several aerosolized antimicrobial agents including amikacin, tobramycin, and fosfomycin were evaluated for the treatment of gram-negative pneumonia in previous studies comparing the efficacy of IH antimicrobial adjunct therapy to various IV antimicrobial agents with that of IV monotherapy or IH placebo [77--80]. However, antimicrobial agents evaluated in those studies could not be included as treatment nodes in our NMA to construct a single connected network. Furthermore, non-MDR/XDR A. baumannii pneumonia patients were largely included in those studies. Of note, more evidence is required to determine the appropriate administration method of IH antimicrobials for optimal clinical benefit in patients with pneumonia because the delivery devices, dosing, ventilator settings, and endotracheal tube size may affect the therapeutic response [76, 81].

There are a few limitations in this meta-analysis. The major limitation of this NMA is the absence of aerosolized antimicrobials other than IH COL as aforementioned. Another important limitation is that the analysis was mostly based on retrospective studies (16 out of 23 studies in total). Considering the retrospective nature of most included studies, this NMA should be viewed as a hypothesis-generating study rather than definitive clinical evidence, despite rigorous quality assessments. The safety profiles of all antimicrobial treatments were not evaluated due to insufficient data on adverse drug reactions and substantial differences between studies in the baseline laboratory values or organ function parameters. In addition, the novel antimicrobial treatments with potential activity against A. baumannii, such as vabomere, plazomicin, cefiderocol and eravacycline, were not included in this NMA owing to absence of published data on the patients with MDR/XDR A. baumannii pneumonia [82--84]. It remains to be determined whether any of these agents may have a role in this clinically important infection. Additionally, this NMA could not clearly address the role of combination therapy over single-agent therapy. In fact, the purpose of this NMA was not to specifically compare the effectiveness between combination therapy and monotherapy but to evaluate the overall comparative effectiveness of different antimicrobial treatment options. Last, variability in identifying the causative pathogen among the included studies could not completely distinguish colonization from infection in HAP and VAP. Clinical studies more robustly detecting the true infectious organism in HAP or VAP may be necessary to accurately and precisely determine the effects of antimicrobial treatments for MDR/XDR A. baumannii pneumonia.

## Conclusions

This Bayesian NMA provides clinically meaningful evidence to aid clinicians in selecting the optimal antimicrobial regimen for the treatment of critically ill patients with MDR/XDR A. baumannii pneumonia. SUL appears to be the best treatment among fifteen different antimicrobial regimens investigated for survival benefit.

Apart from SUL, FOS + IV COL, HD SUL, IH COL + IV COL, and HD TIG therapy may be appropriate alternative treatment options. The comparative results of our analysis should be tailored to the antimicrobial susceptibility testing result of each individual patient when making treatment decisions. Appropriate and well-controlled studies would be necessary to prospectively verify the findings of our current study in patients with nosocomial pneumonia.

## Additional files

Additional file 1: Table S1. PRISMA checklist of items to include when reporting a systematic review and a network meta-analysis. (DOCX 20 kb) Additional file 2: Table S2. Risk of bias assessment of randomized controlled trials. Table S3. Risk of bias assessment of observational studies. (DOCX 20 kb)

Additional file 3: Table S4. Inconsistency assessment. (DOCX 14 kb) Additional file 4: Table S5. Results of sensitivity analyses. (DOCX 17 kb)

## Abbreviations

AB: Acinetobacter baumannii; APACHE II: Acute Physiology and Chronic Health Evaluation II; CAR: Carbapenem; CI: Confidence interval; COL: Colistin; CR: Carbapenem-resistant; Crl: Credible interval; DIC: Deviance information criterion; FOS: Fosfomycin; GLY: Glycopeptide; HAP: Hospital-acquired pneumonia; HD: High dose; IH: Inhaled; IMI: Imipenem; IV: Intravenous; KP: Klebsiella pneumoniae; MCMC: Markov chain Monte Carlo; MDR: Multidrug-resistant; MERO: Meropenem; MIU: Million international units; n/N: Number of outcome events/number of patients in each intervention; NR: Not reported; OR: Odds ratio; PA: Pseudomonas aeruginosa; PRISMA: Preferred Reporting Items for Systematic Reviews and Meta-analyses; RIF: Rifampin; SAPS: Simplified acute physiology score; SOFA: Sepsis-related organ failure assessment score; SUCRA: Surface under the cumulative ranking curve; SUL: Sulbactam; TDM: Therapeutic drug monitoring; TD: Teicoplanin; TIG: Tigecycline; VAN: Vancomycin; VAP: Ventilator-associated pneumonia; XDR: Extensively drug-resistant

## Acknowledgements

This study was supported by the Research Institutes of Pharmaceutical Science in Seoul National University.

## Funding

No funding was received for this analysis.

## Availability of data and materials

All data supporting the results and conclusions reported in this article are included in this published article.

## Authors' contributions

SYJ, SHL, HN, and SY searched the literature, reviewed the articles, and performed the quality assessment. SYJ and SYL participated in statistical analyses and data interpretation. SYJ, SHL, and SYL designed the study and drafted the manuscript. JIL and EKC conceived the study, were in charge of overall direction and planning, and edited the drafted manuscript. All authors have read and approved the final manuscript.

## Author's information

Not applicable.

## Ethics approval and consent to participate

Not applicable.

## Consent for publication

Not applicable.

## Competing interests

The authors declare that they have no competing interests.

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Author details

^{1}Department of Pharmacy, College of Pharmacy, Seoul National University, 1 Gwanak-ro, Gwanak-gu, Seoul 08826, Republic of Korea. ^{2}Research Institute of Pharmaceutical Sciences, Seoul National University, Seoul, Republic of Korea. ^{3}Department of Pharmacy, College of Pharmacy, Kyung Hee University, 26 Kyungheedae-ro, Dongdaemun-gu, Seoul 02447, Republic of Korea. ^{4}Department of Public Health Science, Graduate School of Public Health, Seoul National University, Seoul, Republic of Korea. ^{5}Department of Pharmacy, College of Pharmacy, Yonsei University, Incheon, Republic of Korea.

Received: 27 September 2017 Accepted: 4 December 2017
Published online: 20 December 2017

## Submit your next manuscript to BioMed Central and we will help you at every step:

- We accept pre-submission inquiries
- Our selector tool helps you to find the most relevant journal
- We provide round the clock customer support
- Convenient online submission
- Thorough peer review
- Inclusion in PubMed and all major indexing services
- Maximum visibility for your research

Submit your manuscript at www.biomedcentral.com/submit
(1) BioMed Central