# Personalized Tumor Growth Prediction Using Multiscale Modeling 

Serbulent Unsal ${ }^{1}$, Aybar Acar ${ }^{3}$, Mehmet Itik ${ }^{7}$, Ayse Kabatas ${ }^{5}$, Oznur Gedikli ${ }^{4}$, Feyyaz Ozdemir ${ }^{6}$, Kemal Turhan ${ }^{1}$<br>${ }^{1}$ Karadeniz Technical University, Biostatistics and Medical Informatics, Trabzon, Turkey<br>${ }^{2}$ Middle East Technical University, Health Informatics, Ankara, Turkey<br>${ }^{3}$ Middle East Technical University, Cancer Systems Biology Laboratory, Ankara, Turkey<br>${ }^{4}$ Karadeniz Technical University, Physiology, Trabzon, Turkey<br>${ }^{5}$ Karadeniz Technical University, Mathematics, Trabzon, Turkey<br>${ }^{6}$ Karadeniz Technical University, Medical Oncology, Trabzon, Turkey<br>${ }^{7}$ Izmir Democracy University, Mechanical Engineering, Izmir, Turkey

Address for Correspondence: Kemal Turhan, E-mail: kturhan@@gmail.com
Received: 28-07-2020; Accepted: 29.07.2020; Available Online Date: 15.10 .2020
(Copyright 2020 by Dokuz Eylül University, Institute of Health Sciences - Available online at www.jbachs.org
Cite this article as: Unsal S, Acar A, Itik M, Kabatas A, Gedikli O, Ozdemir F, Turhan K. Personalized Tumor Growth Prediction Using Multiscale Modeling. J Basic Clin Health Sci 2020; $4: 347-363$.


#### Abstract

Purpose: Cancer is one of the most complex phenomena in biology and medicine. Extensive attempts have been made to work around this complexity. In this study, we try to take a selective approach; not modeling each particular facet in detail but rather only the pertinent and essential parts of the tumor system are simulated and followed by optimization, revealing specific traits. This leads us to a pellucid personalized model which is noteworthy as it closely approximates existing experimental results.

Methods: In the present study, a hybrid modeling approach which consists of cellular automata for discrete cell state representation and diffusion equations to calculate distribution of relevant substances in the tumor microenvironment is favored. Moreover, naive Bayesian decision making with weighted stochastic equations and a Bayesian network to model the temporal order of mutations is presented. The model is personalized according to the evidence using Markov Chain Monte Carlo. To validate the tumor model, a data set belonging to the A549 cell line is used. The data represents the growth of a tumor for 30 days. We optimize the coefficients of the stochastic decision-making equations using the first half of the timeline.

Results: Simulation results of the developed model are promising with their low error margin (all correlation coefficients are over 0.8 under different microenvironment conditions) and simulated growth data is in line with laboratory results ( $r=0.97, \mathrm{p}<0.01$ ).

Conclusions: Our approach of using simulated annealing for parameter estimation and the subsequent validation of the prediction with invitro tumor growth data are, to our knowledge, is novel.


Keywords: neoplasms, patient-specific modeling, adenocarcinoma of lung, precision medicine

## INTRODUCTION

Despite much progress in oncology, molecular biology, and related fields, cancer is still a condition for which the prognosis is generally a shortened lifespan or lowered quality of life, frequently dramatically so. The complex and individually particular behavior of cancer decreases success rates of cancer therapies. The usual steps of cancer therapy are: deciding on tumor's pathological type, staging the cancer using clinical data and planning the therapy according to medical guidelines which are informed by bulk statistics. In this routine, there is little room to calculate and predict a patient's therapy response in a bespoke way.

Mathematical models that use patient-specific data and up-todate scientific evidence has implications on the evidence-based practice of personalized medicine. Use of individually tuned mathematical models give clinicians the ability to compare
alternative therapy plans and predict outcomes. These models have an important role in the early drug development and for development of therapy scheduling. However, this search for personalized therapy has not yet met success. In the present study we propose a hybrid tumor model for the Non-Small Cell Lung Cancer (NSCLC) and a personalization framework.

Different approaches exist to develop tumor models. Continuous tumor models simulate tumor growth within a set of differential equations, making them good options in modeling complex systems (1-6). Simulating attributes of a tumor at tissue scale is trivial with continuous models. However, it is a non-trivial challenge to use them for simulating individual cell dynamics or discrete events in a cell or in the cell's microenvironment. Discrete models are a solution to this problem. Simulation of

the tumor system dynamics, which cannot be easily modeled by the continuous approach can be possible with the discrete modeling techniques such as the orientation mechanism of tumor according to nutrients (7), effects of the cell adhesion on tumor growth as well as effects of the proteolytic enzymes (8), competition between cell colonies (9), genetic parameters on the tumor movement (10). Hence, it could be concluded that discrete models provide sufficient flexibility in modeling cell-state scale tumor dynamics. Continuous and discrete modeling approaches could be thus combined into hybrid models (11). Most of the time a discrete model is created at cell scale to simulate behavior of the cells and a continuous model is used at tissue scale to simulate distribution of substances like oxygen or glucose in tumor micro environment in hybrid modeling $(9,12)$.

In this study, such a framework has been developed for personalized tumor modeling that includes tumor and tissue specific parameters gathered from the literature for A549 (13), which is a well-known cell line derived from lung adenocarcinoma. Cellular automata are used for discrete cell state representation. Substance distribution in the vascular tumor micro-environment is calculated by using partial differential equations. Mutations of cells are modeled with a probabilistic network. A Naive Bayes approach is chosen for the decision-making module of each cell. Weighted stochastic equations are created for modeling decisions of the tumor cells. Overall, this approach enables us to create a model which can easily be personalized through the optimization of individual parameters using simulated annealing. Simulation results of the developed model are promising with their low error margin (all correlation coefficients are over. 8 under different microenvironment conditions) and the simulated growth data fits well to xenograft model (experimental and simulation results were found to be positively correlated, $r=0.97, p<0.01$ ).

## Comparison with the State of the Art

According to the best of our knowledge;

- Our model is the first such model able to accurately regress the personalized growth of lung adenocarcinoma given data from the stages.
- Our approach of personalization uses simulated annealing and its validation with a xenograft model is novel.
- The model also incorporates a hierarchical Bayesian network of the tumor which is created from A549 mutation data and uses this model to predict the order of occurrence and timing of consecutive mutations during tumor progression. Although there are a few models $(14,15)$ which use mutation data, our model uses temporal and hierarchical order of specific cancer driver genes which has, thus far, to our knowledge, has not been leveraged.
- We propose novel stochastic equations to obtain a personalized model and estimate the importance (weight) of each with optimization.


## METHODS

## Details of the Tumor Model

We base our model on the one proposed by Gerlee and Anderson (16). Figure 1 shows the components a comprehensive tumor model should have.

Our model is specific to lung cancer adenocarcinoma. The fixed parameters used in the model are gathered from in-vitro and in-vivo experiments from literature. The modules implemented in this study are shown in Figure 2, the modules which are not implemented in this study but planned for future studies are also showed in figure and coded in gray.
![img-0.jpeg](img-0.jpeg)

Figure 1. Example for a general tumor model.
![img-1.jpeg](img-1.jpeg)

Figure 2. Implemented modules in study with potential modules for future implementation

Cellular automata are used to make decisions based on substance distribution and mutation effects, since rule-based automata are well suited to simulating a system which depends on many variables. Decisions for migration, proliferation, apoptosis and substance consumption, are based on the state of each cellular automaton, which use a stochastic decision making process.

Each module will be discussed in the subsequent sections. In terms of the software infrastructure; Python (17) is used as the main platform of implementation for the model, FiPy (18) is

used to solve PDEs, and Cython (19) for increased efficiency of simulation. Finally, PyGame (20) was used for implementing the graphical user interface and for visualization.

## Model Parameters

Most of the physical parameters used in our simulator are specific to lung cancer adenocarcinoma, while some are general parameters for tumors or tumor microenvironments. The A549 cell line was selected as a basis, since it represents a very common lung tumor presentation. Table 1, below, shows the parameters, symbols, and values used, with references.

## Diffusion of Substances in the Tumor Microenvironment

Tumor growth consists of the consumption, growth, production, migration, apoptosis and necrosis phases. Tumors need oxygen and glucose to grow and they also produce waste. If a tumor cannot find enough oxygen it goes into hypoxia, if the tumor cannot obtain enough nutrition (glucose), hypoglycemia begins. Producing waste $\left(\mathrm{H}^{+}\right.$ions) is another effect of the cell's increased metabolism, however this also helps tumors create advantageous microenvironments for themselves, as low pH is favored by most tumors, giving them a competitive edge over normal cells.

Substance diffusion into the tissue is modeled as:

$$
\frac{\partial m}{\partial t}=D \nabla^{2} m+m H s_{c a p}-s_{c e l l}
$$

Equation 1 calculates the substance diffusion within the tissue boundaries. We assume that there are capillaries spread throughout
the tissue which supply fixed substance flow to the tissue and tumor cells. This equation is valid for consumed substances such as oxygen and glucose in our model (Figure 3). Waste substances
![img-2.jpeg](img-2.jpeg)

Figure 3. An example of oxygen distribution in cell microenvironment. Transverse sections of randomly placed capillaries are shown as red dots. The $X$ and $Y$ axes are coordinates of tumor growth are and normalized between $0-1$.

Table 1. Parameters used in model


such as $\mathrm{H}+$ ions produced by tumor cells (and normal cells, alike) are, likewise, removed by capillaries. Accordingly, for waste, we modify our diffusion model as shown in Equation 2:

$$
\frac{\partial m}{\partial t}=D \nabla^{2} m+m H s_{c a p}-s_{c e l l}
$$

In equations 1 and $2, S_{\text {cell }}$ stands for the consumption or production of substance by tumor cells and $S_{\text {cap }}$ is the fixed term for the substance delivery or removal capacity of capillaries. Finally, H is a very large number which is used to dampen the effects of neighbors for the specific coordinate where the capillary exits. The particulars are elaborated on in Appendix B.

Once the conditions of tumors' microenvironments are thus modeled, internal dynamics of tumor cells can be explored.

## Intracellular Model

Throughout their life cycles, cells make several critical biochemical decisions. The first among these is about proliferation. Tumor cells decide whether they will proliferate, or not, based on genetic and microenvironment conditions. Another critical decision is to trigger apoptosis, if necessary. Furthermore, tumor cells can alter their energy production strategy: When oxygen concentration is below a specific threshold, they change their energy metabolism from aerobic to anaerobic.

During the simulation, at each time step, each simulated cell should decide what its biochemical state is. The cell should decide on many dimensions; such as whether it will die or not, how it will produce energy, its substance consumption budget. Moreover, whether any mutations will occur. This should be completed before other decisions are given, since nearly all other subsystems are affected by genetic variations.

After genetic changes occur, the cell starts to explore its environment to find if there are any other cells in the neighborhood and detect the amount of vital substances to use in the decisionmaking process. Then the cell decides how it will produce energy, by using aerobic or anaerobic energy metabolisms. Finally, the cell decides on its status; either apoptosis, quiescence, proliferation or migration. The decision process is based on probabilistic functions. The parameters (i. e weights) are found using optimization, as explained in the results section. Details of functions used in subsystems are explained in the following subsections. Overview of the model can be seen in Figure 4. Details of the intracellular model can be found at Appendix A.

## RESULTS

## Consistency

A tumor model should be consistent with the basics of tumor biology. We first test this consistency using experimental data. Studies show that primary cell such as primary mouse embryonic fibroblasts (33) and tumor growth is accelerated under hypoxia which is observed both in-vitro for LNCaP prostate cancer cells (34) and tumor xenografts models with MDA-MB-231 breast cancer cells and LNCaP cells $(35,36)$. Figure 5 shows our model is
![img-3.jpeg](img-3.jpeg)

Figure 4. Overview of the model.
consistent with literature (35) for hypoxic growth dynamics. The Pearson correlation coefficient is calculated between model and previous studies for hypoxic and normoxic conditions. A strong correlation for both hypoxic ( $r=0.992$ ) and normoxic ( $r=0.991$ ) conditions is observed on tumor volume. Also as seen in Figure 6 , under hypoxia, which could be defined as $10 \% \mathrm{O}_{2}$ of normoxia (37), the apoptotic region is considerably larger and tumor shows migratory behavior. This phenomenon can be observed in experimental studies $(38,39)$.

Many studies have shown that glucose is an important factor in tumor growth. This fact was shown not only in-vitro experiments with healthy pulmonary microvascular endothelial cells (40), immortalized T lymphocytes (Jurkat cell line) (41), tumor cell lines such as BT549, MDA-MB-468, MCF-7 for breast cancer (42, 43), but also in vivo experiments by observation of SCCVII tumor growth in C3H/HeN mice and HCT-116 tumor growth in Rag2M mice (44). Our model is in line with these studies as shown in Figure 7. The Pearson correlation coefficient calculated between model and in-vitro results (42) for normal and low glucose conditions. A strong correlation for both normal ( $r=0.998$ ) and low glucose ( $r=0.898$ ) conditions is observed on tumor cell number. Limitation of growth under low glucose can also be observed by comparing tumor morphology, as seen in Figure 8.

![img-4.jpeg](img-4.jpeg)

Figure 5. a, b. (35) reports tumor growth under hypoxic conditions (10\% $\mathrm{O}_{2}$ ) (a). Our in-silico experiment results (b).
![img-5.jpeg](img-5.jpeg)
![img-6.jpeg](img-6.jpeg)

Figure 6. Tumor growth based on time for hypoxia and normoxia. Red cells have proliferative, green cells have quiescent, and white cells have migratory phenotypes while blue represents non-viable cells, whether apoptotic or necrotic.

Chemotaxis is a fundamental mechanism that determines tumor morphology (45): defined as motility of cells towards resources like oxygen and glucose (46) which is observed in healthy cells such as vascular smooth muscle cells (47) and tumor cells (48). To ensure that cells in our model simulate chemotactic behavior we created a set of capillaries as shown in Figure 9. Subsequently, the growth of the simulated tumor was monitored. It was observed that, in simulation, the tumor cells tended to the capillaries as shown Figure 10 which is in line with in vitro studies which includes 3D assays for A549 cell line (48).

Tumor growth patterns fit a Gompertzian growth curve, i. e. a sigmoid function (49-54). Our simulations are also validated by
the observation that the tumor growth process can be defined as a sigmoid curve that starts with a high exponential growth rate but eventually levels-off with saturation (see Figure 11). The Pearson correlation coefficient calculated between model and study for long term tumor growth. A strong correlation ( $r=0.8$ ) for long term tumor growth is observed between experimental and simulation results (55).

Data from Figure 5, Figure 7, and Figure 11 were extracted using Web Plot Digitizer (56) and used in calculation of the Pearson correlation coefficients.

![img-7.jpeg](img-7.jpeg)

Figure 7. a, b. Previously reported (41) tumor growth under different glucose concentrations (a). Results of our in-silico results (b).
![img-8.jpeg](img-8.jpeg)

Figure 8. Tumor growth based on time for normal $(17 \mathrm{mM})$ and low $(5 \mathrm{mM})$ glucose levels.
![img-9.jpeg](img-9.jpeg)

Figure 9. Distribution of capillaries along a diagonal line with diffusion of oxygen and glucose shown. The $X$ and $Y$ axes are coordinates of tumor growth are and normalized between $0-1$.

![img-10.jpeg](img-10.jpeg)

Figure 10. Tumor growth based on time with the same diagonal axis with capillaries. Red cells have proliferative, green cells have quiescent, and white cells have migratory phenotypes while blue represents non-viable cells, whether apoptotic or necrotic.

![img-11.jpeg](img-11.jpeg)

Figure 11. a, b. Tumor growth function fits to a Gompertzian model. Experimental results (55) for long term tumor growth (a). Tumor growth function fits to a Gompertzian model. Results of simulation from our model (b).

Mutations are the foundation for the genetic structure of tumors and these are also what determine the individual differences in different cancers. In the past, some mathematical tumor models have used this fact. Some models incorporate the effects of mutation on only one locus (57-59) while some have grouped several gene mutations according to their phenotypes (60-62). Yet, according to the best of our knowledge, none of them inspect the effects of multiple cancer driver genes and their temporal order together, in a multiscale model. We use the results of a temporally ordered inference model generated from a multi-patient study (63). For example, in the model, the occurrence of the KRAS mutation is a prerequisite for TP53 mutations and TP53 mutation is a prerequisite for the occurrence of CDK2NA mutations. In our simulations, as well, we have observed that TP53 mutations only occur after KRAS mutations and only in the cells which already have accumulated KRAS mutations. Likewise, we were able to recreate other dependencies, e.g. TP53 to CDK2NA. Figure 12 shows how mutations occur in a temporal and hierarchical order, indicating that our modeling strategy is successful in simulating the actual mutation timelines in tumor progression. Using this system, a multi-clonal tumor model is created, allowing for the fact that different parts of a tumor may have different progressions of mutation.

### Personalization: Estimating Parameters per Individual

Different approaches are found in the literature for the personalization of mathematical tumor models. For example, Prokopiou et al. calculates the proliferation saturation index by using the ratio of tumor volume to the carrying capacity of tumors (64). On the other hand, Saribudak et al. use gene expression values to personalize their model (65), and Kogan used PSA levels to individualize their model (66).

In our model, we used a stochastic decision approach on cellular automata. The decisions of each cell simulating automaton are based on the tumor microenvironment, e.g. oxygen and glucose.

![img-12.jpeg](img-12.jpeg)

Figure 12. KRAS, TP53 and CDK2NA mutant cells at $t=100$.
![img-13.jpeg](img-13.jpeg)

Figure 13. Results of a tumor growth experiment (67) and simulation results.
concentrations. Weights of these variables in terms of their effect on a particular individual's tumor are determined by using optimization. We use simulated annealing as the optimization method.

The parameter optimization results can be seen in Figure 13. Results were obtained by optimizing parameters using the first 15 days of tumor growth data gathered from the experimental results from a xenograft (67). Afterwards, the simulation was run with the optimized parameters. Predicted tumor growth after optimization is also shown Figure 13. The model's prediction closely mirrors the growth trend of the xenograft.

## DISCUSSION

The literature includes many studies on personalized medicine, but most of these are results of bulk biostatistics and bioinformatics analyses (68-70). Tumor models on the other hand, have potential in providing mechanistic and generative (in that future states can be simulated) personalized predictions. In this study, we demonstrate a tumor model based on empirical observations and biochemical properties from previous literature. This model is amenable to tuning and extension, and able to provide personalized predictions.

To the best of our knowledge, our model is novel in that it can predict personalized growth patterns of lung adenocarcinoma in a way that can be validated by xenograft model data. A hierarchical Bayesian network modeling the genotypes of tumor subpopulations was also created to predict ordering and timing of mutations during tumor progression.

The approach has a number of potential limitations. First and foremost, it is a two dimensional (or rather 2.5D) model of what is essentially a three dimensional phenomenon. We model the tissue as a single layer of cells. While this is not necessarily a high fidelity simulation of the real tissue, it is a computationally tractable approximation, especially for epithelial tissues. Likewise, the substance portfolio is limited and does not include a host of cellular signaling, most importantly hormones and cytokines, which significantly affect cell behavior. From a computation standpoint, the optimization method used (simulated annealing), while avoiding local minima is still subject to fixing on unrealistic solutions (minima with physically impossible parameter values). While this can be checked and the simulation discarded if it were the case, a more robust solution would be, in the future, to use a constrained stochastic optimization algorithm. Finally, the mutation subsystem (i. e. the hierarchical Bayesian network) is based on well-known and catalogued mutations and cannot possibly simulate the existence or effects of novel mutations. The simulation will not be able to accurately predict the growth of tumors with such mutations, should they occur in a patient. Doing so requires predicting phenotype solely from genotype and is an open research question.

We validated our model's behavior with experimental data from literature $(35,42,48,55,67)$. We observed that both under hypoxia and hypoglycemia our model's growth pattern is in line with experimental results which is explained in detail at Results section. Furthermore, our model shows the expected Gompertzian curve in chemotactic behavior and in general growth pattern. Our personalization strategy is also promising. We have shown that if a model consistent with tumor biology can be developed, it can be personalized using a simple parameter optimization method like simulated annealing.

In the future we will extend our model by simulating effects of the immune system and integrate chemotherapy, radiotherapy and immunotherapy results to our model towards developing a clinical decision support tool.

Informed Consent: The ethical form is not needed since the study is a computational work and no patient data is used

Compliance with Ethical Standards: The consent form is not needed since the study is a computational work and no patient data is used

Peer-review: Externally peer-reviewed.
Author Contributions: Concept - SU, AA, MI, AK, OG, FO, KT; Design - SU, AA, MI, AK, OG, FO, KT; Supervision - SU, AA, MI, AK, OG, FO, KT; Fundings - SU, AA, MI, AK, OG, FO, KT; Materials - SU, AA, MI, AK, OG, FO, KT; Data Collection and/or Processing - SU, AA, MI, AK, OG, FO, KT; Analysis and/or Interpretation - SU, AA, MI, AK, OG, FO, KT; Literature Search SU, AA, MI, AK, OG, FO, KT; Writing Manuscript - SU, AA, MI, AK, OG, FO, KT; Critical Review - SU, AA, MI, AK, OG, FO, KT

Conflict of Interest: No conflict of interest was declared by the authors.
Financial Disclosure: This research is funded by TUBITAK [grant number 114E634]. This funding source had no role in the design of this study and will not have any role during its execution, analyses, interpretation of the data, or decision to submit results.

Presented in: The manuscript is only available as a pre-print in Biorxiv (https:// www.biorxiv.org/content/10.1101/510172v1). The manuscript was presented in 9th International Symposium on Health Informatics and Bioinformatics HIBIT 2015, Muğla, Türkiye, and, Tıp Bilişiminde Yenilikler Sempozyumu, Türkiye, 25 Mart 2017 and was published in abstract form in the proceedings of the congress.

# Appendix A 

## Proliferation

Each simulated cell's proliferation subsystem decides whether the cell is in a proliferating state or not. When the cell is quiescent, if there is free space for growth, if parameters such as nutrition and oxygen level are favorable, then the cell has a good chance of proliferating.

It is assumed that the maximum rate of proliferation will take place at optimal conditions. When a cell's microenvironment is closer to optimal conditions the proliferation probability increases; otherwise it decreases. Inputs used for the proliferation decision are oxygen concentration, glucose concentration and pH . Genetic effects are also used in the probability distribution function. The equation A1 is used to decide the proliferation state of the cell:

$$
\begin{aligned}
& \left(P_{g}, P_{h}, P_{d}\right)=\left\{w_{p o} \times p_{o}+w_{p g} \times p_{g}+w_{p h} \times p_{h}+p_{d}\right. \text { ifCell'sMetabolismisAerobic } w_{p g} \times p_{g}+ \\
& w_{h} \times w_{p h}+p_{d} \text {, ifCell'sMetabolismisAnaerobic }
\end{aligned}
$$

In equation A. 1, $P_{o}$ represents the weighted proliferation probability, $P_{o}$ is the probability coefficient for oxygen. $P_{o}$ is calculated based on oxygen concentration at the coordinates of cell which represented with mo and given by:

$$
P_{o}=\frac{m_{o}-h o_{o}}{c_{o}-h o_{o}}
$$

In equation A. 2, ho $_{o}$ is hypoxia induced apoptosis threshold which is the minimum oxygen concentration for proliferation and $c_{o}$ is background oxygen concentration which is the maximum oxygen concentration for cell's microenvironment as given in Table 1. Probability coefficient for glucose $P g$, represents glucose concentration at the coordinates of the cell:

$$
P_{g}=\frac{m_{g}-h g_{o}}{c_{g}-h g_{o}}
$$

Calculation of the probability coefficient for pH , represented by $P_{o}$, is more complex than $P_{o}$ and $P_{g}$, because for oxygen and glucose higher concentration correlates with higher probability for proliferation, but for pH , the cell needs an optimal pH level to have the highest chance of proliferation. Thus, $P_{o}$ is calculated as a piecewise function:

$$
P_{h}=\left\{\frac{m_{p h}-m i n_{p h}}{p h_{o}-m i n_{p h}}, i f m_{p h}<p h_{o} \left\lvert\, \frac{m_{g}-m a x_{p h}}{\mid p h_{o}-m a x_{p h}}\right.\right\}, i f m_{p h}>p h_{o} 1, i f m_{g}=p h_{o}
$$

where $\min _{p h} \max _{p h}$ are minimum and maximum values of pH that a tumor cell can live under; $p h_{o}$ is the optimal pH level for proliferation as given in table 1 and $m_{p h}$ is pH level at the coordinates of cell. Finally, $P_{g}$ represents effects of the cell's accumulation of mutations on the proliferation probability and will be explained in the "Genetic Effects on Tumor" subsection.

## Invasion

When a cell decides on proliferation or migration, the next question is about finding the most convenient place to do so. The invasion system models this decision based on microenvironment conditions. The invasion system uses oxygen, glucose and $\mathrm{H}^{+}$concentration as input parameters. When scanning neighbour cells with traditional methods for invasion, a strange effect occurs, as mentioned by Gerlee and Anderson (16). The tumor tends to grow in a tree-like way, sprouting branches. Although we could not explain this effect, we overcome this issue by scanning cells orthogonally and diagonally at consecutive time steps, in interleaved fashion, as explained in Gerlee and Anderson.

To find optimal invasion coordinates, the cell prefers the direction where oxygen and glucose concentration is maximum. For $\mathrm{H}^{+}$concentration the cell should look for optimal pH level or nearest level to optimal, given as $p h_{o}$ in Table 1. The invasion propensity score sinv can then be calculated as:

$$
s_{i n o}=\left\{w_{m o} \times m_{a}+w_{m g} \times m_{g}+w_{m h} \times m_{h}\right. \text { ifCell'sMetabolismisAerobicw } w_{m g} \times m_{g}+
$$

$w_{m h} \times m_{h}$, ifCell'sMetabolismisAnaerobic
(A.5)

An error margin $\left(e_{m o}\right)$ should be determined which simulates the transient insensitivity of cells to proliferative opportunities. When maximum $s_{i n o}$ is determined, each cell's $s_{i n o}$ is compared to the maximum $s_{m o}$. If the difference between them is not more than $e_{m o}$ then this cell is a candidate for invasion. After all candidates are determined, one candidate is selected randomly and a new tumor cell appears at coordinates of the chosen cell.

# Migration 

Cell migration is an important factor in the morphology of the tumor. Tumor cells may decide to migrate if conditions are not suitable to survive or proliferate. In the migration subsystem, each simulated tumor cell decides whether to manifest a migratory phenotype or not. Then, it finds a suitable place for invasion by using invasion subsystem and finally it invades the location directly or by using the cell movement subsystem. The migration subsystem decides to manifest the most likely phenotype with a naive Bayes approach similar to the proliferation subsystem. There are three types of environmental parameters that force a cell to migrate. The first one is the oxygen level. When oxygen level decreases below $h o_{x}$ then the cell's possibility of choosing a migratory phenotype is calculated with equation A. 6

$$
P_{h o m}=\frac{h o_{m}-m_{a}}{h o_{m}} * 100
$$

where $P_{\text {hom }}$ stands for hypoxia based migration probability in percent, $h_{o m}$ is hypoxia induced migration threshold which is determined based on simulation results as $5 \times h o_{g l}$ (see table 1) and $m_{a}$ is oxygen concentration at the cell's coordinates. In a similar way migration probability based on glucose level can be calculated with A. 7:

$$
P_{h g m}=\frac{h g_{m}-m_{g}}{h g_{m}} * 100
$$

where $P_{h g m}$ stands for hypoglycemia based migration probability in percent, $h g_{m}$ is hypoglycemia induced migration threshold which is determined based on simulation results as $5 \times h g_{a}$ (see Table 1) and $m_{g}$ is glucose concentration at the cell's coordinates.

## Apoptosis

Beyond natural apoptosis, three cases are considered for apoptosis in our model: Hypoxia, hypoglycemia and extremely low pH level can cause apoptosis.

When the oxygen level decreases below\% 1.5, hypoxia starts until oxygen runs out (\% 0). It has been shown that\% 55 of NSCLC Adenocarcinoma (A549) cells die when oxygen level reaches\% 0 . Also, it is known that the natural apoptosis rate is $\% 10$ for A549 cells (24).

Since $\frac{55-10}{1.5-0}=3$, for each $\% 0.1$ change at oxygen level, apoptosis survival probability increases $\%$ 3. Based on this assumption, hypoxia based apoptosis probability can be calculated as:

$$
P_{h a}\left(M_{a}, P_{d a}\right)=\frac{\left(1.5-h g_{a}\right)_{a 3+10}}{100}-p_{d a}
$$

where oxygen concentration at the coordinates of the cell are represented with $m_{p a}$ and probability of as genetic effects decreases apoptosis chance and is represented by $p_{d a}$.

Cells can live without oxygen but not without glucose. Hypoglycemia induced apoptosis probability $\left(P_{h o}\right)$ can be calculated when $m_{g}<h g_{a}$ as follows:

$$
P_{h a}\left(M_{g}, P_{d a}\right)=\frac{m_{g}}{h g_{a}}-p_{d a}
$$

The last factor which causes apoptosis is pH level. An acidic microenvironment is favorable for the tumor because cancerous cells are more resistant to acidic environment than parenchyma.

But, when pH level decreases to severely low levels all kinds of cells start to die. When this effect is modeled, pH level at the coordinates of the cell is represented by $m_{h}$ and $\min _{p h}$ stands for the minimum pH level of cell microenvironment. Thus, we can calculate $P_{\text {ha }}$ (apoptosis probability based on pH ) as:

$$
P_{\text {ha }}\left(M_{h}, P_{d a}\right)=\frac{m_{h}-\min _{p h}}{p h_{h}-\min _{p h}}-p_{d a}
$$

Apoptosis probability is calculated using oxygen, glucose and pH level. However, even as the cell decides to start apoptosis it will wait for a period. This delay acts as a low-pass filter and prevents the cell from being affected by noise and momentary oscillations of microenvironment signals. There are more complicated methods that can be found in literature to model delayed systems (71).

# Energy Metabolism 

Tumor cells can produce energy by using two different metabolisms; aerobic and anaerobic. In aerobic metabolism, oxygen and glucose are used to produce energy:

$$
C_{6} H_{12} O_{6}+6 O_{2} \Rightarrow 6 C O_{2}+6 H_{2}+3 B A T P
$$

In the anaerobic metabolism, only glucose is used to produce energy:

$$
C_{6} H_{12} O_{6} \Rightarrow 2 A T P+2 H^{+}
$$

In our model, the energy metabolism shift is only based on oxygen concentration; genetic effects are ignored for the sake of simplicity.

Metabolism shift starts at $\% 5$ oxygen concentration with $20 \%$ probability and reaches $\% 100$ probability at $1 \%$ oxygen concentration (24). If the concentration is over $5 \%$ then the cell always chooses aerobic metabolism. Oxygen concentration at coordinates of cell as percentage ( $m_{p o}$ ) is obtained from:

$$
\mathrm{m}_{\mathrm{po}}=\frac{\mathrm{m}_{\mathrm{o}}}{\mathrm{c}_{\mathrm{o}}}
$$

and the probability of a cell's metabolism change from aerobic to anaerobic is calculated by:

$$
P_{e}=\left(\frac{m_{p o}}{100}\right), i f 0.01 \leq m_{p o} \leq 0.051, i f m_{p o}<0.01
$$

There is also a delay introduced before the decision for a metabolism shift, with the same rationale as for the delay for the apoptosis decision, explained above.

## Oxygen - Glucose Consumption and Acid Production

Tumor cells have a baseline oxygen consumption rate, represented by $u_{o}$ as seen in Table 1, but this rate changes based on cellular conditions. For example, a cell will not use oxygen when under anaerobic metabolism. Also, the cell's state will affect oxygen consumption. We assume that the cell consumes $\% 50$ more oxygen in a proliferative state than in the quiescent state.

Glucose consumption $\left(u_{g}\right)$ is calculated in a similar way. Glucose consumption in aerobic and anaerobic states are calculated based on the stoichiometry of the respective metabolisms. Proliferative cells are assumed to use $\% 50$ more glucose, similar to oxygen.

Acid production is observed in the anaerobic metabolism, due to glycolysis. Hydronium production rate $(p h)$ is taken from literature (16). In a proliferative state, hydronium production is assumed to increase by $\% 50$, since glucose consumption increases with the same ratio.

# Cell Stress and Movement 

Physical simulations on tumors show us that there is a proliferative belt on tumor mass. This belt is caused due to various reasons, e.g. cell-cell adhesion and cell-ECM adhesion (4). In our model, instead of treating each physical effect one by one in detail, we use a stress score variable.

The stress score for each cell is calculated proportional to the cell's distance from tumor's edge. Pressure on cells located in deeper parts of tumor will be higher than cells which are located at the edge of the tumor because of cell-cell adhesion and cell-ECM adhesion. Edge cells' tendency of migration is thus higher than deep cells.

## Genetic Effects on Tumor

When modeling cancer, simulating genetic effects, taking into account all variations is intractable. Since the aim of this study is only creating a simple proof of concept model, just a few important mutations of A549 are included, based on literature (63).

Our model uses an inheritance mechanism. When a simulated cell proliferates, it copies the DNA of its ancestor, so mutations are transferred between generations. As a first step, the relationship between mutations determined. After this step, probabilities of mutations calculated. Finally, effects of the mutations are added to the model. In the model, only two types of mutation effects are considered: mutations' effects on probabilities of proliferation and apoptosis.

For both, if any mutation occurs in a cell, each driver mutation provides only a small selective growth advantage to the cell, on the order of a $0.4 \%$ increase in the difference between cell birth and cell death (72). Since only $5 \%-10 \%$ of these are driver mutations, we calculate each driver will have an effect of $8 \%$. Thus, if any mutation occurs in a cell, it is assumed that proliferation probability increases $8 \%$ or apoptosis probability decreases $8 \%$ based on mutation type. These relationships and effects are shown in Table A1 with minimum and maximum probabilities of observing said mutations in the population.

The model for the mutations is based on a Bayesian network. At each time step, a simulated cell triggers its own mutation system. For each mutation, preconditions are checked. For example, for A549, EGFR mutation almost never occurs in tumors with KRAS mutation or TP53 mutation occurs if KRAS gene has a mutation. For the sake of simplicity, we assume that these mutations are all pathogenic.

After ancestors of the mutation are validated, a mutation probability is determined for each viable mutation. Finally, if a mutation occurs, effects of said mutations, whether on proliferation or apoptosis, are applied to the cell in question, and will affect its future decision equations.

Table A1. Mutations of A549 used in model


# Appendix B 

$m\left(\vec{c}, t\right)$ means concentration of substance at coordinates $\vec{c}$ at time $t . D$ is diffusion constant of substance. Since our model is 2D,

$$
\vec{c}=(x, y)
$$

we could know the concentration of substance at specified coordinates at time $t$. To solve equation it could also be written as below:

$$
\frac{\partial m(\vec{c}, t)}{\partial t}=D\left(\frac{\partial^{2} m}{\partial x^{2}}+\frac{\partial^{2} m}{\partial y^{2}}\right)
$$

A detailed explanation for this equation could be found in literature (76). Physical representation of diffusion phenomenon which is represented as equation B. 2 could be seen in figure:
![img-14.jpeg](img-14.jpeg)

Figure 14. Diffusion as a physical phenomenon.
After the basic equation of diffusion is formed, only a source term is needed which represents consumption or production of the substance for a coordinate at a specific time (75):

$$
s(\vec{c}, t)=s(x, y, t)
$$

Oxygen and glucose which are consumed by cells are subtracted from equation B. 2:

$$
\frac{\partial m(\vec{c}, t)}{\partial t}=D\left(\frac{\partial^{2} m}{\partial x^{2}}+\frac{\partial^{2} m}{\partial y^{2}}\right)-s(\vec{c}, t)
$$

and source term for hydrogen ions $\left(\mathrm{H}^{+}\right)$which are produced at the end of glycolysis is added:

$$
\frac{\partial m(\vec{c}, t)}{\partial t}=D\left(\frac{\partial^{2} m}{\partial x^{2}}+\frac{\partial^{2} m}{\partial y^{2}}\right)+s(\vec{c}, t)
$$

Now effects of capillaries should be added to the equation. We accomplish this by using an implicit source term which is a product of a fixed value with diffusion term (m). We also multiply it with a huge value $(\mathrm{H})$ to winnow effects of neighbors out. We write the final equation for consumed substances as:

$$
\frac{\partial m}{\partial t}=D \nabla^{2} m+m H s_{c a p}-s_{c e l l}
$$

for produced substances it will be:

$$
\frac{\partial m}{\partial t}=D \nabla^{2} m-m H s_{\text {cap }}+s_{\text {cell }}
$$

Finally, initial and boundary conditions for equations B. 4 - B. 5 will be determined (77). We assume that boundaries of grid with $L \times L$ size, concentration equals 0 . Initial conditions could be defined as

$$
m(x, y, 0)=f(x, y), \forall(x, y) \in R, R=[0, L] \times[0, L]
$$

with Dirichlet boundary conditions

$$
\begin{aligned}
& m(x, 0, t)=m(x, L, t)=0,0 \leq x \leq L, \forall t \geq 0 \\
& m(0, y, t)=m(L, y, t)=0,0 \leq y \leq L, \forall t \geq 0
\end{aligned}
$$

# Non-dimensionalization 

Non-dimensionalization can be done by dividing each term of an homogeneous equation to parameters which have the same units (78). In this study, diffusion constants and consumption/ production rates were non-dimensionalized with the following equations:

$$
\begin{aligned}
d^{*} & =\frac{3600 \times \delta_{t} \times d}{a} \\
r^{*} & =\frac{3600 \times \delta_{t} \times r \times n}{c_{b}}
\end{aligned}
$$

These are generalized forms of non-dimensionalization equations. In equation B. 10, $d^{\prime}$ is a nondimensional diffusion constant. Tumor cell doubling time ( $\delta t$ ) multiplied by 3600 to convert hour to second. Original diffusion constant is represented with $d$. Area (a) is the total area (in $\mathrm{cm}^{2}$ ) of the grid. In equation B. 11, $r^{\prime}$ represents non-dimensional consumption/production rate. Original rate is represented by $r$. Maximum number of tumor cells (which equals to number of grid's cells) is represented by $n$. Finally background concentrations are represented by $c_{b}$. Using these equations B. 10 - B. 11, $u_{x}, u_{y x}, u_{y x x}, p_{x}, d_{x}, d_{y}, d_{b}$ were non-dimensionalized.