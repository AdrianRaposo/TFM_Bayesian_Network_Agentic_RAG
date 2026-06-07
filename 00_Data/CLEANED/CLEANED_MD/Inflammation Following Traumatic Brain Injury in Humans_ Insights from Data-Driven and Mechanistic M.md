# Inflammation Following Traumatic Brain Injury in Humans: Insights from Data-Driven and Mechanistic Models into Survival and Death 

Andrew Abboud ${ }^{1 \dagger}$, Qi Mi ${ }^{2,3 \dagger}$, Ava Puccio ${ }^{4}$, David Okonkwo ${ }^{4}$, Marius Buliga ${ }^{5}$, Gregory Constantine ${ }^{3,6}$ and Yoram Vodovotz ${ }^{1,3 *}$<br>${ }^{1}$ Department of Surgery, University of Pittsburgh, Pittsburgh, PA, USA, ${ }^{2}$ Department of Sports Medicine and Nutrition, University of Pittsburgh, Pittsburgh, PA, USA, ${ }^{3}$ Center for Inflammation and Regenerative Modeling, McGowan Institute for Regenerative Medicine, University of Pittsburgh, Pittsburgh, PA, USA, ${ }^{4}$ Department of Neurological Surgery, University of Pittsburgh, Pittsburgh, PA, USA, ${ }^{5}$ Department of Mathematics, University of Pittsburgh, Bradford, PA, USA, ${ }^{6}$ Department of Mathematics and Department of Statistics, University of Pittsburgh, Pittsburgh, PA, USA

## OPEN ACCESS

Edited by:
Craig J. Thalhauser, Bristol Myers Squibb, USA

## Reviewed by:

Cecilia M. P. Rodrigues, University of Lisbon, Portugal Gaurav K. Gupta, Tufts University School of Medicine, USA
*Correspondence: Yoram Vodovotz vodovotzy@upmc.edu
${ }^{\dagger}$ These authors have contributed equally to this work and co-first authors.

Specialty section:
This article was submitted to Experimental Pharmacology and Drug Discovery, a section of the journal Frontiers in Pharmacology

Received: 31 July 2016
Accepted: 13 September 2016
Published: 27 September 2016
Citation:
Abboud A, Mi Q, Puccio A, Okonkwo D, Buliga M, Constantine G and Vodovotz Y (2016) Inflammation Following Traumatic Brain Injury in Humans: Insights from Data-Driven and Mechanistic Models into Survival and Death. Front. Pharmacol. 7:342. doi: 10.3389/fphar. 2016.00342

Inflammation induced by traumatic brain injury (TBI) is a complex mediator of morbidity and mortality. We have previously demonstrated the utility of both data-driven and mechanistic models in settings of traumatic injury. We hypothesized that differential dynamic inflammation programs characterize TBI survivors vs. non-survivors, and sought to leverage computational modeling to derive novel insights into this life/death bifurcation. Thirteen inflammatory cytokines and chemokines were determined using Luminex ${ }^{\top M}$ in serial cerebrospinal fluid (CSF) samples from 31 TBI patients over 5 days. In this cohort, 5 were non-survivors (Glasgow Outcome Scale [GOS] score $=1$ ) and 26 were survivors (GOS > 1). A Pearson correlation analysis of initial injury (Glasgow Coma Scale [GCS]) vs. GOS suggested that survivors and non-survivors had distinct clinical response trajectories to injury. Statistically significant differences in interleukin (IL)-4, IL-5, IL-6, IL-8, IL-13, and tumor necrosis factor- $\alpha$ (TNF- $\alpha$ ) were observed between TBI survivors vs. non-survivors over 5 days. Principal Component Analysis and Dynamic Bayesian Network inference suggested differential roles of chemokines, TNF- $\alpha$, IL-6, and IL-10, based upon which an ordinary differential equation model of TBI was generated. This model was calibrated separately to the time course data of TBI survivors vs. non-survivors as a function of initial GCS. Analysis of parameter values in ensembles of simulations from these models suggested differences in microglial and damage responses in TBI survivors vs. non-survivors. These studies suggest the utility of combined data-driven and mechanistic models in the context of human TBI.

Keywords: inflammation, TBI outcome, mathematical modeling, data-driven modeling, mortality, inflammatory mediators in CNS

[^0]
[^0]:    Abbreviations: CBF, cerebral blood flow; CSF, cerebrospinal fluid; DAMP, damage-associated molecular pattern molecule; GCS, Glasgow Coma Scale; GOS, Glasgow Outcome Scale; IL, interleukin; MIP, macrophage inflammatory protein; TBI, traumatic brain injury; TNF- $\alpha$, tumor necrosis factor- $\alpha$; VEGF, vascular endothelial growth factor.

# INTRODUCTION

Traumatic brain injury (TBI) remains a leading medical problem in the United States, causing severe long-term morbidity and, in some cases, mortality. Between 1.6 and 3.8 million sports-related concussions alone are reported each year, while an estimated 5.3 million people are living with long-term cognitive and psychological impairments annually (Selassie et al., 2008). These traumatic injuries are caused by direct and indirect biomechanical forces to the cranium, and result in a neurometabolic energy crisis in the brain (Giza and Hovda, 2014). These changes have immediate pathogenic effects on ion homeostasis, regional cerebral blood flow (CBF), and cerebral metabolism, while also carrying downstream "immunoexcitotoxicity" effects by activating immune receptors on microglia (brain macrophage-like cells) and astrocytes in response to cellular injury and oxidative stress (Blaylock and Maroon, 2011; Woodcock and Morganti-Kossmann, 2013). These cellular and molecular cascades can be both neuroprotective and neurotoxic, and ultimately impact patients' prognosis and recovery (Selassie et al., 2008).

While the clinical progression and biological underpinnings of TBI have been studied extensively, accurately predicting a patient's prognosis following a TBI remains a difficult challenge for clinicians. Traditionally, the diagnosis of concussions and TBI have fallen into a "one size fits all" approach. Recently, however, there has been impetus toward a multifaceted and targeted approach that matches a TBI treatment plan with a number of variable clinical trajectories (Collins et al., 2014). Even so, current predictors of outcome after severe TBI are neither sufficiently sensitive nor specific to be used for clinical decision making in the acute recovery period (Gao and Zheng, 2015).

Thus, although the clinical segregation of TBI patients is improving, there still remains a need for clear biomarkers and/or diagnostic modalities to predict individual patient's likelihood of recovery, disability, and mortality. This challenge is not unique to TBI, but has proven to be an obdurate obstacle for health care providers in the management of many disease states including cancer, sepsis, and transplantation.

One central process that affects outcomes following TBI is that of acute inflammation, involving mediators such as TNF- $\alpha$, IL-6, IL-8, and IL-10 (Woodcock and MorgantiKossmann, 2013). However, the inflammatory response to injury and infection is complex, dynamic, and highly dependent on patient-specific conditions. We and others have shown the efficacy of data-driven computational models in segregating patients using circulating inflammatory cytokines, chemokines, and damage-associated molecular pattern (DAMP) molecules (Zaaqoq et al., 2014; Namas et al., 2015; Almahmoud et al., 2015a,b; Abboud et al., 2016; Namas et al., 2016b). We have recently reported on the utility of multiplexed analysis of circulating inflammatory mediators combined with data-driven modeling to define potentially novel inflammatory mechanisms that segregate survivors vs. non-survivors of blunt trauma (Abboud et al., 2016). Separately, mechanistic mathematical models have served as the basis for patient-specific predictions and virtual clinical trials in the setting of human blunt trauma, including an exploration of the inflammatory characteristics of survivors and non-survivors (Brown et al., 2015).

Herein, we hypothesized that early TBI-induced inflammation can foreordain similar patients for survival vs. mortality, and carried out a combined clinical and in silico study to gain insights into this process. In the present study, we sought to gain insights from data-driven modeling to develop mechanistic models of TBI, in order to better understand the inflammatory characteristics of TBI survivors and non-survivors.

## MATERIALS AND METHODS

## Traumatic Brain Injury Patients

Severe TBI patients were enrolled prospectively as approved by the University of Pittsburgh Institutional Review Board upon meeting inclusion criteria judged by the on-call neurosurgeon. Informed consent was obtained by the legal authorized representative prior to study procedures. CSF and blood samples were obtained by trained study personnel for the initial enrollment and through 5 days of ICU admission. A trained neuropsychological technician obtained the 6 - and 12 -month Glasgow Outcome Scale (GOS) scores. The patient cohort consisted of 34 TBI patients [29 survivors ( 27 males/2 females) and 5 non-survivors ( 4 males/1 female)]. Non-survivors were determined by having a Glasgow Outcome Scale (GOS) score of 1 by 12 month follow up, and had a Glasgow Coma Scale (GCS) score (an estimate of TBI injury severity) of $5.6 \pm 0.58$ on hospital arrival. Survivors had a similar admission GCS of $6.2 \pm 0.26$ (Table 1), with a GOS score of $2-5$.

## Clinical Data

The data on each subject consisted of two distinct components, namely clinical/demographic data and CSF inflammatory mediator data. Clinical/demographic (one-dimensional) variables included: age, gender, presence of infection, bleeding, surgical decompression, presence of subarachnoid hemorrhage, and initial GCS score. The GCS score quantified the initial brain injury severity on a numerical scale from 3 to 15 . The GOS score was utilized as the outcome variable and was viewed as the response variable to study and predict neurological outcome, as a function of the other input variables. The GOS score quantifies the neurological outcome at 6 and 12 months post-TBI. GOS scores ranged from 1 to 5 , with 1 indicating death and higher values indicating a progressively better neurological state of health.

TABLE 1 | General demographics and injury characteristics of TBI patient cohort.


## Inflammatory Mediator Data

In addition to the clinical and demographic data, inflammatory mediator data were collected from all 34 patients. The data were plotted as time series for the following 13 cytokines/chemokines (assayed using Luminex ${ }^{\mathrm{TM}}$ multiplexing technology): IL-1 $\alpha$, IL-1 $\beta$, IL-2, IL-4, IL-5, IL-6, IL-8, IL-10, IL-13, macrophage inflammatory protein (MIP)-1 $\alpha$, MIP-1 $\beta$, tumor necrosis factor (TNF)- $\alpha$, and vascular endothelial growth factor (VEGF). The inflammatory mediator time series variables varied in both in length and in the time sequence at which they were collected.

## Statistical Analysis

All data were analyzed using SigmaPlot ${ }^{\mathrm{TM}} 11$ software (Systat Software, Inc., San Jose, CA). Statistical difference between survivors and non-survivors was determined by Student's $t$ test. Group-time interaction of plasma inflammatory mediators' levels between survivors and non-survivors was determined by Two-Way Analysis of Variance (ANOVA) and quantified by area under the curve (AUC) using the mean values for each time point, then calculating non-survivors/survivors AUC fold change. Statistical significance for this study was set at a $p<0.05$.

## Computational Methods: PCA

Normalized inflammatory mediator data (each measurement taken to be a single point in 13-dimensional inflammatory mediator space) were transformed into principal component space using the MatLab ${ }^{\circledR}$ function, princomp. We then examined projections of inflammatory mediators into principal component space by using the score coefficients for the first 2 or 3 principal components.

## Computational Methods: DyBN

We carried out Dynamic Bayesian Network (DyBN) inference to model the evolution of probabilistic dependencies within a system over time, and to suggest possible feedback interactions among inflammatory mediators. This analysis was carried out using MATLAB ${ }^{\mathrm{TM}}$ (The Math Works, Inc., Natick, Ma) as previously described by our group (Azhar et al., 2013; Almahmoud et al., 2015c; Abboud et al., 2016). Inflammatory mediators were represented at multiple time points within the same network structure. The data were separated in adjacent 24 h time periods up to 5 days ( $0-24 \mathrm{~h}, 24-48 \mathrm{~h} . . .96-120 \mathrm{~h}$ ). In this approach, time was modeled discretely as in a discrete Markov chain. Each mediator was given a time index subscript indicating the time slice to which it belonged. Additional temporal dependencies were represented in a DyBN by edges between time slices. Each node in the network was associated with a conditional probability distribution of a variable that is conditioned upon its parents (upstream nodes).

## Computational Methods: Ordinary Differential Equation Model

We constructed a mechanistic model using ordinary differential equations (ODE), based on core interactions inferred from PCA and DyBN. Before constructing this model, we sought to gain further insights into potential relationships between time and peaks in the CSF levels of these cytokines. Accordingly, the
distributions of Peak time of TNF- $\alpha$, IL-6, and IL-10) were plotted. This analysis suggested that most patient's TNF- $\alpha$ and IL-10 peak at the early time point ( $t<20 \mathrm{~h}$ post-injury) and IL-6 peaks slightly later (at $\sim 30 \mathrm{~h}$ post-injury).

The model equations are depicted below:

$$
\begin{aligned}
\frac{d \mathrm{D}}{d \mathrm{t}} & =\mathrm{d}_{0} \mathrm{M}-\mathrm{d}_{1} \mathrm{D} \\
\frac{d \mathrm{M}}{d \mathrm{t}} & =\left(\frac{\mathrm{m}_{0} \mathrm{D}}{1+\mathrm{m}_{1} \mathrm{D}}+\frac{\mathrm{m}_{2} \mathrm{C}}{1+\mathrm{m}_{3} \mathrm{C}}+\frac{\mathrm{m}_{4} \mathrm{TNF}}{1+\mathrm{m}_{5} \mathrm{TNF}}}+\frac{\mathrm{m}_{6} \mathrm{IL}_{6}}{1+\mathrm{m}_{7} \mathrm{IL}_{6}}\right) \\
& \frac{1}{1+\mathrm{m}_{8} \mathrm{IL}_{10}}-\mathrm{m}_{9} \mathrm{M} \\
\frac{d \mathrm{C}}{d \mathrm{t}} & =\frac{\mathrm{c}_{0} \mathrm{D}}{1+\mathrm{c}_{1} \mathrm{D}}-\mathrm{c}_{2} \mathrm{C} \\
\frac{d \mathrm{IL}_{10}}{d \mathrm{t}} & =i_{0} \mathrm{M}-i_{1} \mathrm{IL}_{10} \\
\frac{d \mathrm{TNF}}{d \mathrm{t}} & =\frac{\mathrm{t}_{0} \mathrm{M}}{1+\mathrm{t}_{1} \mathrm{IL}_{10}}-\mathrm{t}_{2} \mathrm{TNF} \\
\frac{d \mathrm{IL}_{6}}{d \mathrm{t}} & =\frac{\mathrm{b}_{0} \mathrm{M}^{6}}{1+\mathrm{b}_{1} \mathrm{IL}_{10}}-\mathrm{b}_{2} \mathrm{IL}_{6}
\end{aligned}
$$

Terms in the model: Damage/dysfunction/DAMPs (D), Activated inflammatory cells/microglia (M), Chemokine (C), IL-10 (IL ${ }_{10}$ ), TNF- $\alpha$ (TNF), IL-6 (IL ${ }_{6}$ ).

This model encompasses the following biology. Cytokines and chemokines are produced by inflammatory cells, which in turn are activated by damage (not directly) and further production of cytokines and chemokines. Model variables and equations are the following: damage (D), inflammatory cells (M), chemokine (C), TNF- $\alpha$, IL-6, and IL-10. This model incorporates positive feedback from the pro-inflammatory cytokines TNF- $\alpha$ and IL6 , and negative feedback from the anti-inflammatory cytokine IL-10.

The damage variable D is a lumped variable that stands both for overall tissue damage/dysfunction (e.g., changes in CBF, elevated intracranial pressure, and associated neurometabolic changes (Blaylock and Maroon, 2011; Woodcock and MorgantiKossmann, 2013; Giza and Hovda, 2014), and, at a molecular level, the DAMPs released from damaged or dysfunctional brain tissue (e.g., S100B; Woodcock and Morganti-Kossmann, 2013). This variable is assumed to be driven only by activated inflammatory cells/microglia (M), and regulated negatively by both anti-inflammatory influences as well as self-decay. The most important equation in the model is the one for inflammatory cells (M), because the level of these cells regulates the level of all cytokines in this model.

Model parameters and their biological correlates are depicted in Table 2. Before fitting our models to CSF data from TBI patients, the actual data including cytokines and GCS (which represents the initial damage value was normalized to a scale from 0 to 10 . In the case of damage, an initial damage value of zero is equated with a GCS score of 15 , and an initial damage value of 10 represents a GCS score of 3 . For cytokines, the mean cytokine value in survivors and non-survivors were calculated at time points: $0,17,35,60,82$, and 104 h . In addition to the model parameters shown in the equations (see above), two

additional parameters (the initial values of inflammatory cells and chemokine) had to be estimated.

Our fitting procedure was as follows. We choose the initial guess for parameters (randomly or based on previous parameter estimations) and applied the Nelder-Mead simplex method for parameter optimization. The error function in our case is just the sum of errors between computed values of cytokines from the model equations and the values from original mean cytokine values (we simply computed the Euclidean distance between two data vectors). All analysis was performed using Matlab®.

## RESULTS

## TBI Survivors and Non-survivors are Not Be Segregated by Glasgow Coma Scale Score, Suggesting Divergent Responses to Injury

The overall enrollment resulted in a final cohort of 29 survivors (mean age: 31.6 ± 5.6) with a GCS of 6.0 ± 0.24. Five nonsurvivors (mean age: 41.0 ± 7.4, p = 0.172) with a GCS of 5.6 ± 0.57, p = 0.313 (Table 1). Thus, there were no significant differences between groups in age or GCS. A comparison between groups of initial GCS with a 6 month GOS per patient reveals no apparent correlation between the severity of the initial head trauma with 6 month survival (GOS > 1) and mortality (GOS = 1; Figure 1). These results suggest that patient-specific factors in response to TBI, rather than magnitude of injury alone, drive differential outcomes following injury.

We therefore hypothesized that TBI-induced cerebral inflammation drives, or is associated with, the divergent outcomes of survival and death following TBI. To test this hypothesis, we analyzed the dynamics of multiple inflammatory mediators in the CSF, using both standard statistical analyses and computational modeling.

## Time Courses of CSF Inflammatory Mediators Segregate Survivors from Non-survivors

We first hypothesized that dynamics of CSF inflammatory mediators, as a surrogate for brain inflammation following TBI, would differ between survivors and non-survivors. In support of this hypothesis, time course analyses for each of 13 inflammatory mediators revealed differences in 6 mediators over 5 days by Two-Way ANOVA, IL-4, 5, 6, 8, 13, and TNF-α (Figures 2A–M). Notably, levels of IL-6 and IL-8 were the only mediators with mean values elevated above 1000 pg/ml (Figures 2N,O).

![img-0.jpeg](img-0.jpeg)

**FIGURE 1 | Initial GCS scores could not segregate patients for mortality vs. survival.** An initial GCS score was calculated following the traumatic insult. The GOS score was utilized as the outcome variable and was viewed as the response variable. The GOS score quantifies the neurological outcome at 6 and 12 months post-TBI. GOS scores ranged from 1 to 5, with 1 indicating death and higher values indicating a progressively better neurological state of health. There were no statistical differences in the mean GCS between survivors (6.0 ± 0.24) and non-survivors (5.6 ± 0.57, p = 0.313). Furthermore, a plot of GCS vs. GOS was unable to cluster those who went onto survive (GOS > 1) from those who died (GOS = 1). These findings highlight the inutility of GCS alone in predicting patient outcomes.

TABLE 2 | Parameters of ordinary differential equation model of TBI.


![img-1.jpeg](img-1.jpeg)

FIGURE 2 | Time courses of CSF inflammatory mediators segregate survivors from non-survivors. In addition to the clinical and demographic data, inflammatory mediator data were collected from all 34 patients. The data were plotted as time series for the following 13 cytokines/chemokines. The inflammatory mediator time series variables varied in both in length and in the time sequence at which they were collected. (A-M) Time course analyses for each of 13 inflammatory mediators revealed differences in 6 mediators over 5 days by Two-Way ANOVA, IL-4, 5, 6, 8, 13, and TNF- $\alpha$. The mediator levels were highly variable, oscillating frequently and at relatively low levels. (N,O) Notably, levels of IL-6 and IL-8 were the only mediators with mean values elevated above $1000 \mathrm{pg} / \mathrm{ml}$.

## Principal Component Analysis Suggests Conserved General Wiring of Inflammation in TBI Survivors and Non-survivors

We next sought to gain further insights into how the dynamic inflammatory responses of TBI survivors and non-survivors might differ using Principal Component Analysis (PCA), with the hypothesis that PCA would identify a core inflammation program, and that principal characteristics/drivers inferred by PCA would differ between survivors and non-survivors. We have previously utilized this approach to suggest primary drivers of inflammation in mice subjected to experimental trauma/hemorrhagic shock (Mi et al., 2011), in rats undergoing sepsis in the presence or absence of hemoadsorption as an experimental treatment (Namas et al., 2012), in swine undergoing experimental endotoxemia (Nieman et al., 2012), and in human pediatric acute liver failure (Azhar et al., 2013) and trauma (Namas et al., 2016a). We first carried out PCA of the full CSF time course data in all TBI patients, which identified the first principal component as a linear combination of TNF- $\alpha$, MIP-1 $\alpha$, MIP-1 $\beta$, IL-8, IL-10, and IL-6 (Figure 3A).

This analysis suggested a core, dynamic inflammation program characterized by chemokines (MIP-1 $\alpha$, MIP-1 $\beta$, IL-8), pro-inflammatory cytokines (TNF- $\alpha$, IL-6), and anti-inflammatory cytokines (IL-10). This analysis also supports the well-established roles for IL-6, IL-8, and IL-10 in TBI (Bell et al., 1997; Morganti-Kossman et al., 1997; Maier et al., 2001; Woodcock and Morganti-Kossmann, 2013).

We next carried out this analysis separately on survivors and non-survivors, in an attempt to discern whether survival and death were driven by a differential activation of this core inflammatory program, due to different initial conditions or patient-specific characteristics. The separate PCA conducted on time course CSF data from survivors and non-survivors suggested similar primary characteristics of inflammation in these patient sub-groups: IL-6, IL-10, MIP-1 $\beta$, and IL-8, the first 4 components, were shared by both survivors and non-survivors (Figures 3B,C).

## DyBN Inference Suggests Differential Activation of the Inflammatory Network in TBI Survivors and Non-survivors

We next hypothesized that, despite sharing similar primary characteristics, TBI survivors, and non-survivors would differ on the basis of dynamic networks of inflammation. Biological networks often exhibit properties of "switches," in which inferred positive and negative feedback structures are hypothesized to lead to different biological programs depending on the state of the network (Eungdamrong and Iyengar, 2004; Ferrell, 2013). In multiple prior studies of the inflammatory response in humans, we have suggested that "central nodes" in DyBN networks are those nodes exhibiting self-feedback and also cross feedback with other self-feedback nodes (Azhar et al., 2013; Zaaqoq et al., 2014; Almahmoud et al., 2015a,b; Abboud et al., 2016; reviewed in Namas et al., 2015).

DyBN inference based on time course data from survivors and non-survivors suggested the presence of a dynamic inflammatory response encompassing several central nodes connected to several outputs. Similar to PCA, DyBN inference of data from both survivors and non-survivors suggested that the cytokine IL-6 and the chemokine IL-8 were central nodes in the CSF postTBI, exhibiting self-feedback and affecting each other as well as downstream nodes. In addition, DyBN inference in data from TBI survivors suggested a third mediator, IL-1 $\alpha$, involved in a hypothetical switch state (Figure 4).

## A Mechanistic Model Based on Ordinary Differential Equations Suggests Differences in Microglial and Damage Responses in TBI Survivors vs. Non-survivors

The foregoing data-driven modeling suggested two key hypotheses centered on the cytokine IL-6. First, both PCA and DyBN identified IL-6 as a central characteristic and dynamic network node, respectively, which is substantiated by multiple prior studies (Bell et al., 1997; Morganti-Kossman et al., 1997; Maier et al., 2001; Woodcock and Morganti-Kossmann, 2013).
![img-2.jpeg](img-2.jpeg)

FIGURE 3 | Survivors and non-survivors share a similar core inflammatory wiring. (A) PCA analysis was carried out on survivor and non-survivor data combined to assess the underlying inflammatory process. This analysis identified a linear combination of TNF- $\alpha$, MIP-1 $\alpha$, MIP-1 $\beta$, IL-8, IL-10, and IL-6 as part of the first principal component. (B,C) We next carried out this analysis separately on survivors and non-survivors, with the null hypothesis being that there would not be any significant differences between these groups based on PCA if the core inflammatory "wiring" was overall similar across patients (and if the ultimate life and death outcome were due to a differential activation of this "wiring" due to different initial conditions or patient-specific characteristics. The first 4 principal components driving inflammation in survivors and non-survivors were IL-6, IL-10, MIP-1 $\beta$, and IL-8.

![img-3.jpeg](img-3.jpeg)

FIGURE 4 | Non-survivors DyBN was characterized by a bimodal switch state, conferring a homogeneous inflammatory response. Both survivor and non-survivor inflammatory networks shared the IL-6 and IL-8 as central nodes, an observation which is supported by elevated levels of both IL-6 and IL-8 in the CSF analysis. Importantly, a key difference was that the non-survivors system was characterized by a bimodal inflammatory switch state that confers an inevitable and homogeneous inflammatory response while the survivors had a tri-modal structure. The non-survivors network displayed all outputs shared between IL-6 and IL-8, irrespective of switch state. Such a network characteristic is congruent with a unimodal inflammatory phenotype, in this case a pathological type which ultimately leads to mortality. Notably, the survivors system contained the addition of a unique central node, IL-1α, which seemingly conferred a selective advantage for these patients. Thus, a DyBN inference showing an inflammatory network capable of mounting many diverse responses is a defining feature of survival.

A more specific hypothesis, derived from DyBN inference, is the presence of positive feedback behavior in IL-6. To test these hypotheses, and specifically the importance of IL-6 positive feedback in driving survival or death, we sought to use mechanistic mathematical modeling.

We constructed a mechanistic model based on the PCA and DyBN studies, leveraging prior experience with modeling acute inflammation mechanistically in the contexts of sepsis, endotoxemia, traumatic injury, and wound healing (Kumar et al., 2004, 2008; Chow et al., 2005; Day et al., 2006; Reynolds et al., 2006; Mi et al., 2007; Daun et al., 2008; Li et al., 2008; Torres et al., 2009; Nieman et al., 2012; Brown et al., 2015). A key feature of these prior mechanistic models is the forward feedback loop of inflammation → tissue damage/dysfunction → inflammation (An, 2014; Namas et al., 2015), which we hypothesize plays out in the present context in the form of IL-6 positive feedback.

To test this hypothesis, we constructed the ODE model shown schematically in Figure 5, in which IL-6 feeds back upon its own production/release by activated brain microglia (as well as potentially by astrocytes and neurons) as a function of damage/DAMPs (such as S100B), whose release is induced by injury (Woodcock and Morganti-Kossmann, 2013). We included chemokines in the model as well, based on PCA and DyBN inference, and due to their role in activating local inflammatory cells as well as attracting exogenous inflammatory cells into the brain as the blood-brain barrier breaks down following TBI (Pearn et al., 2016). Finally, the model included TNF-α and IL-10 as prototypical pro- and anti-inflammatory mediators, respectively.

We used ordinary differential equations (ODE) to generate this fairly abstract, lumped parameter model (see Table 2 for model parameters); the model building and parameterization process is detailed in the Section Materials and Methods. We hypothesized that fitting the TBI ODE model to data for survivors separately from non-survivors—and creating ensembles of survivor-specific and non-survivor-specific models followed by an interrogation of the changes in parameter values and initial conditions required to account for these fitted model (Prince et al., 2006; Namas et al., 2013)—would allow us to gain insights into how a similar dynamic network of interactions could lead to such divergent outcomes following TBI. Accordingly, we fit the ODE model to data as described in the Section Materials and Methods, leading to an ensemble of simulations depicted in Figure 6 relative to the CSF levels of TNF-α, IL-6, and IL-10 in survivors and non-survivors, respectively. In this study, we ran 100 simulations of which 25 were removed as outliers relative to the data (leaving 75 simulations total). Overall, both survivor-specific and non-survivor-specific models fit relatively well to the IL-10 and TNF-α data, with the fits to IL-6 data being poorer (Figure 6). The Damage variable fits are plausible given a GCS score-scaled starting value and a final value scaled to either survival (damage = 0, the minimal value) or death (damage = 10, the maximal value).

![img-4.jpeg](img-4.jpeg)

FIGURE 5 | Schematic of ODE model. A mechanistic model using ordinary differential equations (ODE), based on core interactions inferred from PCA and DyBN and the hypothesis that inflammation drives tissue damage/dysfunction, release of DAMPs, and further inflammation in a positive feedback cycle centered on the cytokine IL-6. D, damage/dysfunction/DAMPs; M, activated inflammatory cells/microglia; C, chemokine.

We next rank-ordered the fold change between survivors' mean estimated parameter values and ones from non-survivors' based on 75 simulations, i.e., ratio = $\frac{\text{Survivor}}{\text{Non-survivor}}$ (see Table 3). This analysis of ODE model simulations suggested that the key differences between TBI survivors and non-survivors were as follows:

- A nearly 6-fold increase in the value of $d0$, the rate of damage/DAMP production by activated inflammatory cells/microglia in response to a given magnitude of injury, in non-survivors over survivors;
- A nearly 4-fold increase in the value of init $M$, the initial value for inflammatory cells/microglia, in non-survivors over survivors;
- An approximately 3.5-fold increase in the value of $d1$, the decay rate of damage/DAMPs, in survivors over nonsurvivors; and
- An approximately 2.7-fold increase in the value of $i0$, the rate of IL-10 production by activated inflammatory cells, in survivors over non-survivors.

Thus, our simulations suggest that key determinants of whether or not a given TBI patient survives or succumbs to his/her injuries relate to the baseline levels of activated microglia at the time of injury, the degree to which microglia produce DAMPs in response to injury, the degree to which damage is healed or DAMPs are cleared, and the degree to which microglia produce IL-10 or other anti-inflammatory mediators.

## DISCUSSION

In the present study, we sought to determine if the inflammatory response induced by injury, assessed in the form of trajectories of CSF inflammatory mediators analyzed using in silico methods, would shed insight into why some TBI patients survive and others die. By collecting serial CSF samples, and generating data-driven and mechanistic models of inflammation in a small group of TBI patients, we were able to segregate those who would survive the traumatic injury from those who would go on to die.

A central observation of this study was that the GCS alone could not predict mortality in TBI patients. Patients presenting with a similar degree of injury were destined for disparate clinical outcomes. This finding is, of course, not unique to this study, but has been cited by many and points to the inutility of the GCS as a tool for predicting patient outcomes (Gao and Zheng, 2015). Moreover, this finding highlights the difficulty of using clinical observations and physical examination in the post-TBI setting to stratify patients for outcomes. This further suggests underlying causes such as genetic predispositions and aberrant biological processes—such as differences in the inflammatory response to brain injury—must be considered in assessing the clinical course of TBI patients.

## Insights from Statistical Analysis and Data-Driven Modeling

We hypothesized that underlying inflammatory processes and their downstream immunoexcitotoxic effects would be imperative to driving pathology following TBI. In support of this hypothesis, survivors could be differentiated from nonsurvivors based on levels of six inflammatory mediators in the CSF, similar to multiple prior studies (Bell et al., 1997; Morganti-Kossman et al., 1997; Maier et al., 2001; Woodcock and Morganti-Kossmann, 2013), albeit with levels that were dynamically changing in nature and present mostly at low levels. Thus, the CSF inflammatory mediator analysis highlights the dynamic complexity of the post-TBI inflammatory response, and suggests the need for dynamic, non-linear modeling approaches to capture key features of inflammation in these patients.

One such data-driven approach, DyBN, has been used recently in the setting of post-traumatic inflammation to successfully differentiate a group of blunt trauma survivors and nonsurvivors (Abboud et al., 2016). In the present study, DyBN inferred both conserved and divergent dynamic networks in TBI survivors and non-survivors, respectively. The inferred dynamic CSF inflammation networks of both survivors and nonsurvivors shared the cytokine IL-6 and the chemokine IL-8 as central nodes, an observation which is supported by significantly elevated levels of both IL-6 and IL-8 in the CSF in both this and prior studies (Bell et al., 1997; Morganti-Kossman et al., 1997; Maier et al., 2001; Woodcock and Morganti-Kossmann, 2013). Importantly, a key difference was that the non-survivors system was characterized by a bimodal inflammatory switch state that confers an inevitable and homogeneous inflammatory response. A key network characteristic was the suggestion that output nodes are shared between IL-6 and IL-8, irrespective of which central node (IL-6 or IL-8) dominates the "switch." Such a network characteristic is congruent with a unimodal inflammatory phenotype, in this case a pathological type which ultimately leads to mortality.

![img-5.jpeg](img-5.jpeg)

FIGURE 6 | Comparison of ODE model predictions vs. data. The ODE model described schematically in Figure 5 and detailed in the Section Materials and Methods was fit separately to the CSF data of TBI survivors and non-survivors, respectively. One-hundred simulations were performed, of which 25 were outliers relative to the data and so were omitted (resulting in a final total of 75 simulations). The data are shown as box and whisker plots, with black symbols representing simulated data at the given time point, and the red symbols representing actual data at those time points. Damage variable data are scaled to the GCS and ultimate survival or death outcome as described in the Section Materials and Methods. (A,E) TNF- $\alpha$; (B,F) IL-6; (C,G) IL-10; (D,H) Damage.

TABLE 3 | Fold changes (survivors:non-survivors) in parameter values from 75 ODE simulations.


Conversely, the dynamic network inferred in survivors was characterized by IL-6, IL-8, and an additional central node, IL$1 \alpha$, which seemingly conferred a selective advantage for these patients. In the inflammatory network of survivors, a three-way switch state with variable output characteristics suggests that patients who would go on to survive were capable of recruiting additional inflammatory pathways, through which a survival advantage was conferred. Thus, we hypothesize that a dynamic inflammatory network capable of mounting variable responses is a hallmark of survival. Interestingly, IL-1 $\alpha$ is both a cytokine and a DAMP that is induced in the context of injury (Namas et al., 2015) that was recently inferred through modeling to be a central part of the injury response to both peripheral tissues (Starzl et al., 2015) and nerves (Vasudeva et al., 2015). Furthermore, these findings may also suggest a host-protective role for IL-1 $\alpha$ and possibly the NLRP3 inflammasome pathway (Davis et al., 2011) following TBI, which should be studied further.

## Insights from Mechanistic Modeling

To expand upon the insights and hypotheses generated from data-driven modeling, we generated an ODE model that was based on a core set of interactions discerned from PCA and DyBN, which in turn were derived from time courses of CSF inflammatory mediators as a proxy for TBI-induced inflammation occurring in the injured brain. Thus, the present study constitutes a progression from data to data-driven modeling to mechanistic modeling, which we have described as a rational means by which to progress from data to knowledge (An et al., 2012). We demonstrated the utility of this general approach previously, in the context of experimental endotoxemia in swine, in a study in which we used time course data and PCA to yield a two-compartment ODE model of acute inflammation (Nieman et al., 2012). In the present study, this approach was expanded to include DyBN, in order to go beyond principal characteristics to a delineation of putative feedback loops and central network nodes.

The reduced ODE model we generated was on the order of prior ODE models of acute inflammation (Kumar et al., 2004; Day et al., 2006; Reynolds et al., 2006). While such reduced models are often of predominantly theoretical utility rather than being quantitatively predictive, we nonetheless sought to parameterize the TBI model with time course of CSF data from TBI survivors vs. non-survivors. Our goal was to generate an ensemble of models differing only in the values of model parameters and initial conditions, but with identical model structure and similar fit to data, and then to leverage an approach we have described previously (Prince et al., 2006; Namas et al., 2013), in which we compared the values of these parameters in TBI survivors and non-survivors.

Given the relatively abstracted nature of our ODE model, certain formalisms that are likely not biologically realistic were employed. A key focus of the model was the inferred positive feedback behavior of IL-6. In order to obtain reasonable model fits to the data, we used the sixth power of M in the IL-6 equation to account for this positive feedback behavior because our experiments with lower powers gave worse fitting results (data not shown). Though this is likely not biologically plausible, it is a reasonable formalism given the simplicity of our model and the fact that the positive feedback behavior of IL-6 likely involves multiple indirect mechanisms that are not modeled.

Despite such limitations inherent in the process of abstraction, the ensemble modeling approach we utilized led to several plausible hypotheses regarding the differences underlying TBI survivors and non-survivors. These hypotheses center on an elevated number of activated inflammatory cells/microglia at baseline in non-survivors vs. survivors; an elevated production of DAMPs by non-survivor inflammatory cells in response a similar magnitude of injury; and, conversely, a higher clearance rate for DAMPs and a higher anti-inflammatory response (assessed as CSF IL-10) in survivors vs. non-survivors. Future studies are required in order to both validate these hypotheses and refine the ODE model to account more explicitly for the biological interactions abstracted in the current model. Clearly, these hypotheses are related to the structure of the model we utilized, which in turn is based on a core hypothesis that our group has developed over several years regarding the positive feedback loop of inflammation $\rightarrow$ damage/dysfunction $\rightarrow$ inflammation (An, 2014; Namas et al., 2015). There may well be alternative hypotheses to explain the evolution of inflammation in TBI, but this positive feedback-based hypothesis does concur with the inferred positive feedback behavior of a key inflammatory mediator, the cytokine IL-6.

This study was primarily limited by the small number of patients enrolled and the number of data points collected. This

study could also be improved by utilizing a stringent casecontrolled 1:1 matching protocol to control for confounding clinical factors between patients. We additionally recognize the difficulty of obtaining serial CSF samples in a clinical setting, and suggest further analyses of blood serum and CSF should be utilized to evaluate the utility of inflammatory mediators circulating systemically. Lastly, this study was of course limited in the fact that we could not control for the variability in each patient's course of treatment.

## CONCLUSIONS

The present study highlights a potential pathway by which to go from dynamic data via data-driven modeling to mechanistic modeling in a complex human inflammatory disease. While further studies are needed in order to validate key predictions, the present study may point to both novel mechanistic insights and clinically translational applications.

## AUTHOR CONTRIBUTIONS

AA and QM, Substantial contributions to the conception of the work, computational analysis, interpretation of data, and manuscript text; AP and DO, Substantial contributions to the design of the clinical data collection and analysis; MB and GC, Substantial contributions to the computational analysis and interpretation of data; YV, Substantial contributions to the conception of the work, computational analysis, interpretation of data, and critical revisions of the manuscript text for important intellectual content.

## ACKNOWLEDGMENTS

This work was supported in part by Commonwealth of Pennsylvania grant SAP\#4100068505 and by National Institutes of Health grant P50GM53789 to YV, and the Walter Copeland Fund of the Pittsburgh Foundation to AP.

Collins, M. W., Kontos, A. P., Reynolds, E., Murawski, C. D., and Fu, F. H. (2014). A comprehensive, targeted approach to the clinical care of athletes following sport-related concussion. Knee Surg. Sports Traumatol. Arthrosc. 22, 235-246. doi: 10.1007/s00167-013-2791-6
Daun, S., Rubin, J., Vodovotz, Y., Roy, A., Parker, R., and Clermont, G. (2008). An ensemble of models of the acute inflammatory response to bacterial lipopolysaccharide in rats: results from parameter space reduction. J. Theor. Biol. 253, 843-853. doi: 10.1016/j.jtbi.2008.04.033
Davis, B. K., Wen, H., and Ting, J. P. (2011). The inflammasome NLRs in immunity, inflammation, and associated diseases. Annu. Rev. Immunol. 29, 707-735. doi: 10.1146/annurev-immunol-031210-101405
Day, J., Rubin, J., Vodovotz, Y., Chow, C. C., Reynolds, A., and Clermont, G. (2006). A reduced mathematical model of the acute inflammatory response: II. Capturing scenarios of repeated endotoxin administration. J. Theor. Biol. 242, 237-256. doi: 10.1016/j.jtbi.2006.02.015
Eungdamrong, N. J., and Iyengar, R. (2004). Modeling cell signaling networks. Biol. Cell 96, 355-362. doi: 10.1016/j.biolcel.2004.03.004
Ferrell, J. E. Jr. (2013). Feedback loops and reciprocal regulation: recurring motifs in the systems biology of the cell cycle. Curr. Opin. Cell Biol. 25, 676-686. doi: 10.1016/j.cel.2013.07.007

Gao, J., and Zheng, Z. (2015). Development of prognostic models for patients with traumatic brain injury: a systematic review. Int. J. Clin. Exp. Med. 8, 19881-19885.
Gira, C. C., and Hovda, D. A. (2014). The new neurometabolic cascade of concussion. Neurosurgery 75(Suppl. 4), S24-S33. doi: 10.1227/neu. 0000000000000505

Kumar, R., Chow, C. C., Bartels, J. D., Clermont, G., and Vodovotz, Y. (2008). A mathematical simulation of the inflammatory response to anthrax infection. Shock 29, 104-111. doi: 10.1097/SHK.0b013e318067da56
Kumar, R., Clermont, G., Vodovotz, Y., and Chow, C. C. (2004). The dynamics of acute inflammation. J. Theoret. Biol. 230, 145-155. doi: 10.1016/j.jtbi.2004.04.044

Li, N. Y. K., Verdolini, K., Clermont, G., Mi, Q., Hebda, P. A., and Vodovotz, Y. (2008). A patient-specific in silico model of inflammation and healing tested in acute vocal fold injury. PLoS ONE 3:e2789. doi: 10.1371/journal.pone. 0002789
Maier, B., Schwerdtfeger, K., Mautes, A., Holanda, M., Müller, M., Steudel, W. I., et al. (2001). Differential release of interleukines 6, 8, and 10 in cerebrospinal fluid and plasma after traumatic brain injury. Shock 15, 421-426. doi: 10.1097/00024382-200115060-00002
Mi, Q., Constantine, G., Ziraldo, C., Solovyev, A., Torres, A., Namas, R., et al. (2011). A dynamic view of trauma/hemorrhage-induced inflammation

in mice: principal drivers and networks. PLoS ONE 6:e19424. doi: 10.1371/journal.pone. 0019424

Mi, Q., Rivière, B., Clermont, G., Steed, D. L., and Vodovotz, Y. (2007). Agent-based model of inflammation and wound healing: insights into diabetic foot ulcer pathology and the role of transforming growth factor-b1. Wound Rep. Reg. 15, 617-682. doi: 10.1111/j.1524-475X.2007. 00271.x

Morganti-Kossman, M. C., Lenzlinger, P. M., Hans, V., Stahel, P., Csuka, E., Ammann, E., et al. (1997). Production of cytokines following brain injury: beneficial and deleterious for the damaged tissue. Mol. Psychiatry 2, 133-136. doi: $10.1038 /$ sj.mp. 4000227
Namas, R. A., Bartels, J., Hoffman, R., Barclay, D., Billiar, T. R., Zamora, R., et al. (2013). Combined in silico, in vivo, and in vitro studies shed insights into the acute inflammatory response in middle-aged mice. PLoS ONE 8:e67419. doi: 10.1371/journal.pone. 0067419

Namas, R. A., Almahmoud, K., Mi, Q., Ghuma, A., Namas, R., Zaaqoq, A., et al. (2016a). Individual-specific principal component analysis of circulating inflammatory mediators predicts early organ dysfunction in trauma patients. J. Crit. Care. 36, 146-153. doi: 10.1016/j.jcrc.2016.07.002
Namas, R. A., Vodovotz, Y., Almahmoud, K., Abdul-Malak, O., Zaaqoq, A., Namas, R., et al. (2016b). Temporal patterns of circulating inflammation biomarker networks differentiate susceptibility to nosocomial infection following blunt trauma in humans. Ann. Surg. 263, 191-198. doi: 10.1097/SLA. 0000000000001001
Namas, R., Mi, Q., Namas, R., Almahmoud, K., Zaaqoq, A., Abdul Malak, O., et al. (2015). Insights into the role of chemokines, damage-associated molecular patterns, and lymphocyte-derived mediators from computational models of trauma-induced inflammation. Antiox. Redox Signal. 10, 1370-1387. doi: $10.1089 /$ ars. 2015.6398
Namas, R., Namas, R., Lagoa, C., Barclay, D., Mi, Q., Zamora, R., et al. (2012). Hemoadsorption reprograms inflammation in experimental Gram-negative septic fibrin peritonitis: insights from in vivo and in silico studies. Mol. Med. 18, 1366-1374. doi: 10.2119/molmed.2012. 00106
Nieman, K., Brown, D., Sarkar, J., Kubiak, B., Ziraldo, C., Vieau, C., et al. (2012). A two-compartment mathematical model of endotoxin-induced inflammatory and physiologic alterations in swine. Crit. Care Med. 40, 1052-1063. doi: 10.1097/CCM.0b013e31823e986a

Pearn, M. L., Niesman, I. R., Egawa, J., Sawada, A., Almenar-Queralt, A., Shah, S. B., et al. (2016). Pathophysiology associated with traumatic brain injury: current treatments and potential novel therapeutics. Cell Mol. Neurobiol. doi: 10.1007/s10571-016-0400-1. [Epub ahead of print].

Prince, J. M., Levy, R. M., Bartels, J., Baratt, A., Kane, J. M. III, Lagoa, C., et al. (2006). In silico and in vivo approach to elucidate the inflammatory complexity of CD14-deficient mice. Mol. Med. 12, 88-96. doi: 10.2119/2006-00012
Reynolds, A., Rubin, J., Clermont, G., Day, J., Vodovotz, Y., and Ermentrout, G. B. (2006). A reduced mathematical model of the acute inflammatory response: I. derivation of model and analysis of anti-inflammation. J. Theor. Biol. 242, 220-236. doi: 10.1016/j.jtbi.2006.02.016
Selassie, A. W., Zaloshnja, E., Langlois, J. A., Miller, T., Jones, P., and Steiner, C. (2008). Incidence of long-term disability following traumatic brain injury hospitalization, United States, 2003. J. Head Trauma Rehabil. 23, 123-131. doi: 10.1097/01.HTR.0000314531.30401.39

Starzl, R., Wolfram, D., Zamora, R., Jefferson, B., Barclay, D., Ho, C., et al. (2015). Cardiac arrest disrupts caspase-1 and patterns of inflammatory mediators following localized tissue injury in rats: insights from computational modeling. Front. Immunol. 6:587. doi: 10.3389/fimmu.2015.00587
Torres, A., Bentley, T., Bartels, J., Sarkar, J., Barclay, D., Namas, R., et al. (2009). Mathematical modeling of post-hemorrhage inflammation in mice: studies using a novel, computer-controlled, closed-loop hemorrhage apparatus. Shock 32, 172-178. doi: 10.1097/SHK.0b013e318193cc2b
Vasudeva, K., Vodovotz, Y., Azhar, N., Barclay, D., Janjic, J. M., and Pollock, J. A. (2015). In vivo and systems biology studies implicate interleukin-18 as a central mediator in chronic pain. J. Neuroimmunol. 283, 43-49. doi: 10.1016/j.jneuroim.2015.04.012

Woodcock, T., and Morganti-Kossmann, M. C. (2013). The role of markers of inflammation in traumatic brain injury. Front. Neurol. 4:18. doi: 10.3389/fneur.2013.00018

Zaaqoq, A. M., Namas, R., Almahmoud, K., Azhar, N., Mi, Q., Zamora, R., et al. (2014). Inducible protein-10, a potential driver of neurally-controlled IL-10 and morbidity in human blunt trauma. Crit. Care Med. 42, 1487-1497. doi: 10.1097/CCM. 0000000000000248

Conflict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Copyright © 2016 Abboud, Mi, Puccio, Okonkwo, Buliga, Constantine and Vodovotz. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.