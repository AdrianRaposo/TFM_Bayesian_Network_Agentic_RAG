# Probability elicitation using geostatistics in hydrocarbon exploration 

André Luís Morosov ${ }^{1}$ (D) $\cdot$ Reidar Brumer Bratvold ${ }^{1}$<br>Received: 20 August 2020 / Accepted: 23 July 2021 / Published online: 27 August 2021<br>(C) The Author(s) 2021


#### Abstract

The exploratory phase of a hydrocarbon field is a period when decision-supporting information is scarce while the drilling stakes are high. Each new prospect drilled brings more knowledge about the area and might reveal reserves, hence choosing such prospect is essential for value creation. Drilling decisions must be made under uncertainty as the available geological information is limited and probability elicitation from geoscience experts is key in this process. This work proposes a novel use of geostatistics to help experts elicit geological probabilities more objectively, especially useful during the exploratory phase. The approach is simpler, more consistent with geologic knowledge, more comfortable for geoscientists to use and, more comprehensive for decision-makers to follow when compared to traditional methods. It is also flexible by working with any amount and type of information available. The workflow takes as input conceptual models describing the geology and uses geostatistics to generate spatial variability of geological properties in the vicinity of potential drilling prospects. The output is stochastic realizations which are processed into a joint probability distribution (JPD) containing all conditional probabilities of the process. Input models are interactively changed until the JPD satisfactory represents the expert's beliefs. A 2D, yet realistic, implementation of the workflow is used as a proof of concept, demonstrating that even simple modeling might suffice for decision-making support. Derivative versions of the JPD are created and their effect on the decision process of selecting the drilling sequence is assessed. The findings from the method application suggest ways to define the input parameters by observing how they affect the JPD and the decision process.


Keywords Probability elicitation $\cdot$ Geostatistics $\cdot$ Multiple-prospect exploration $\cdot$ Sequential decisions

## 1 Introduction

When oil \& gas companies explore or develop new hydrocarbon reserves, they must plan and decide the order in which the prospects and appraisal wells will be drilled. Value can be added by sequentially exploring potential drilling areas as the information gathered from each prospect provides useful information for choosing the next well to drill or even stop exploring.

In the exploratory phase of a hydrocarbon field, the information available for the decisions is scarce, often limited to seismic interpretations and data from analogous fields.

[^0]Drilling the pioneer well opens a new dimension of information: well-data. It has a high cost but is fundamental in confirming oil presence, understanding the geology, correlating it with the seismic response, and estimating reserves.

The improved understanding that comes from specific welldata might impact future drilling choices by changing the decision maker's (DM) beliefs about the likelihood of uncertain outcomes from each prospect. The beliefs about the likelihood are quantified using probabilities which are used in a decision model that relates decisions, decision alternatives, uncertain outcomes, and their payoffs. Solving it defines the course of action that yields the highest expected value (EV) for the decision metric, often being the net present value, commercially producible reserves, or volume of oil in place.

The sequential drilling problem has been discussed in different contexts by several authors, e.g., [1-8]. The main goal is to create value by identifying the optimal drilling policy and proceed accordingly. The process is separated into two activities: (1) probabilistic modeling and (2) solving the sequential


[^0]:    ㄷ André Luís Morosov
    andre.morosov@gmail.com
    Reidar Brumer Bratvold
    reidar.bratvold@uis.no
    1 University of Stavanger and National IOR Centre of Norway, Stavanger, Rogaland, Norway

decision model. A complete probabilistic model is required to solve the decision model, and different probabilistic models may lead to different decisions.

Considering the available data in the exploration phase, the probabilistic modeling of the process is highly dependent on geoscientists, known as experts in the decision context, which bear and summarize all technical knowledge available about the area. The process of transforming the expert's belief about the likelihood of uncertain outcomes into probabilities is called elicitation. Probability elicitation is important in any decision-making process and is a subject of study that have developed different assessment techniques to different applications $[9-11]$.

One difficulty is the high number of assessments necessary to have a complete probabilistic model. Without any prior knowledge about variables relationships, it is necessary to produce $k^{n}-1$ probability values, where $n$ is the number of random variables (i.e. wells) and $k$ is the number of their states (e.g. dry, high productivity, low porosity). The elicitation process rapidly grows with the problem dimensions, where a simple case with 3 wells, each with 3 possible states, requires 26 probability values for a complete JPD. Although 26 assessments may be practically possible for an experienced geoscientist who understands probability concepts, it is rarely achieved by interviewing oil \& gas experts. To bypass the need to explicitly elicit every single joint probability, simpler methods are available. [1] show how to obtain the JPD from the marginal probabilities and pairwise conditional probabilities by using the maximum entropy method described in [12] and used in [13]. The principle is to find the JPD closest to the joint uniform distribution that still honors all pairwise conditional probabilities. It is equivalent to minimizing the Kullback-Liebler (KL) distance [14] between the distribution under construction and the distribution assuming probabilistic independence between the variables. [15, 16] show how to build a Bayesian network, which is an implicit way of representing the JPD, by using marginal probabilities for source, reservoir and trap levels, and the probabilistic relationships between them resulting in a Bayesian network. The aforementioned methods are ways of reducing the necessary number of assessments for probabilistic modeling, but all count on expert opinion as a primary source of probability assessment. Another difficulty is the lack of data in the exploratory period, demanding a higher share of subjective knowledge in the elicitation process which might not be visible to or even understood by the DM. ${ }^{1}$

The method proposed in this article is, to the best of our knowledge, novel use of geostatistics to help experts and DMs in the elicitation context described above. It tackles the two

[^0]aforementioned difficulties at the same time: (1) provides all joint probabilities in the JPD regardless of the problem size and (2) makes probability elicitation, highly based on subjective knowledge, more transparent. The hard data required ${ }^{2}$ in the geostatistical process, which is scarce in the exploration phase, is replaced by plausible geological property spatial distributions. The process is very visual, being easy to generate realizations that best represent expert subjective knowledge by interactively changing the workflow input parameters. Another benefit is that geostatistics is a more familiar tool for geoscientists, when compared to Bayesian networks or numerical optimization methods, leading to more confident and intuitive results.

The use of geostatistics to define the drilling campaign has already been used to generate the JPD in a different context as discussed in [18]. In their work, the aim was to optimize the number of wells and their placement in an onshore shale-gas environment with high uncertainty in productivity outcomes even for a vastly drilled area. The geostatistics role is to geographically estimate the chances of success based on findings of previously drilled wells. Different from the exploration phase, there is a large set of hard data available and the elicitation process is not strictly dependent on experts. Geostatistics is not limited to geosciences as today, the technique has application in many other sciences. One example is shown in [19] who uses geostatistics in epidemiology.

The following sections will provide a very brief introduction to the basics of geostatistics, introduce and describe the novel method, and demonstrate its application on a compelling 2D case. Later, alternative JPDs are generated from the same ensemble of realizations but with different processing techniques. Each one is used to solve the same sequential decision problem and the results are compared to observe the impacts that different processing methods have in the final decision policy.

## 2 Geostatistics

Populating subsurface models with uncertain properties (e.g. porosity and permeability) is a challenging task considering that the information obtained from actual measurements in the wells covers only a tiny fraction of the total area of the subsurface reservoir. Geostatistics originated in the mining industry [20] as an attempt to better estimate gold ore grade, became very popular in the oil and gas industry including to spatially distribute geological properties in subsurface models.

Geostatistics is a general term that includes different techniques to generate subsurface realizations. Perhaps the most used are Sequential Gaussian Simulation (SGS) and

[^1]
[^0]:    ${ }^{1}$ A consistent decision requires the DM to trust the probability assessment, which is often outsourced to experts. A transparent elicitation process helps the DM to understand and trust the assessment results.

[^1]:    ${ }^{2}$ Although often used in geostatistics, well-data is not required. The pilotpoints method is one example of it [17].

Sequential Indicator Simulation (SIS) for spatial distributions of continuous and discrete variables, respectively. Both techniques are called simulation because they populate a grid using a random sequence. If the simulation is repeated with the same input data, the populated grid (realization) would be different because the path of populating would be different, yielding a different result. ${ }^{3}$ The realizations can be considered equiprobable and analyzing them collectively shows the uncertainty related to the spatial distribution of geological properties.

Newer and more advanced techniques include MultiplePoint Simulation (MPS), Process-Mimicking modeling, and Object-Based simulation, each one having its own set of premises. MPS is similar to SGS but the pairwise spatial statistics represented by the variogram function is expanded to higherorder statistical moments through the concept of training images, which improves its ability to reproduce complex smallscale features [21]. MPS, SGS, and SIS are "cell-based", i.e. the simulations build the distributions cell-by-cell, and are easily conditioned to hard data but require additional actions to produce large-scale geometries or structures (trends) in the realizations. Object-based frameworks can produce largescale trends (geometries) by distributing objects like channels or lobes with uncertain parametric geometries [22]. Processmimicking also produces compelling large-scale features aiming to mimic results obtained from modeling the geological process (depositional environments). Both object-based and process-mimicking approaches provide realizations that are geologically more appealing but conditioning them to hard data is not direct as in methods like SGS and MPS [21, 22]. This brief review of the techniques is not exhaustive but merely exemplifies the multitude of available techniques to generate stochastic subsurface realizations.

Geostatistical modeling in this article uses the SGS approach because it is widely used in the Oil\&Gas industry, and is implemented using the Stanford Geostatistical Modeling Software (SGeMS). ${ }^{4}$ SGeMS is a flexible opensource computer package including a large library of algorithms to generate geostatistical realizations, which are described in [23].

## 3 Methodology

During the exploratory phase, geoscientists are expected to provide probabilities of prospect findings to support drilling decisions. At this point, the available information about the subsurface is generally limited to seismic interpretation, analogous fields, and conceptual geological knowledge.

[^0]Geostatistics provides powerful means for probability assessment albeit are not commonly used during this phase due to the lack of well-data.

This section presents a method summarized in Fig. 1 that exploits geostatistics to help with probability the elicitations, which becomes a systematic, transparent, and traceable method. In the diagram, yellow color indicates input required or elicitation choices, and blue color indicates the output of the method.

First, it generates variability in geological property spatial distributions that geoscientists consider plausible, here called "Concept models"". Later it uses the collection of realizations bearing variability to generate a joint probability distribution of joint geological events.

### 3.1 Geological property realizations-set

The realizations set is generated following the left part of the workflow in Fig. 1. In this workflow, hard data are not limited to real measurements but include constraints extracted from geoscientists' beliefs.

The concept models are the main input for the process and provide a general shape indicating how the geologic property ${ }^{6}$ of interest might be spatially distributed in the exploration area. Each concept model is a deterministic shape upon which the geostatistical process will generate variability. There might be as many different concept models as necessary to cover plausible uncertain scenarios and they are indexed by $m$ to a total of $M$. It is not restrictive in what geological property to use, provided it will assist the elicitation process supporting a certain decision. Figure 2 shows an example with 5 concept models where the geological property is the facies-type indicator. This same example is used in the Application section. Each concept model entails a set of "Geostatistical Simulations" to generate a "Realizations set".

The final objective of the geostatistical process is to generate realizations with plausible property variations in the vicinity of preconceived "Well positions". Collectively, the realizations create variability of the geological property by being more similar to the concept model in areas away from the Well positions and dissimilar to the models in areas near Well positions. To achieve it, we use a set of "Pilot-points" [17] to collect values from the concept models and use them as hard data in the geostatistical process. i.e. condition the stochastic realizations to the expected trends. The areas where variability is mostly created are centered on the well positions and their sizes defined by the "Variability range" parameter.

[^1]
[^0]:    ${ }^{3}$ This statement assumes that the pseudo-random number seed is not the same. If it is, the resulting realizations would be the same with the same input data. ${ }^{4}$ Available at http://sgems.sourceforge.net

[^1]:    ${ }^{5}$ In this section, italic style indicates a direct reference to the block diagram in Fig. 1.
    ${ }^{6}$ The process was designed for a single property. For multiple properties, it can be repeated to generate one JPD for each property.
    ${ }^{7}$ There is an implicit inner loop in this task that will repeat the simulation process for all realizations required for each concept $m$.

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Elicitation Workflow. Yellow color indicates input and blue color output. Each concept model generates a desired number of realizations with higher variability in the vicinity of the well positions

In these areas *pilot-points* are absent. Figure 2 also shows an example of how the *pilot-points* (white dots), *well positions (white crosses)*, and *variability range* can be set over the concept models.

The spacing of *pilot-points* is determined by geoscientists running the method and will change how similar the realizations will be to the concepts. If they are too close to each other, the realizations-set will not have significant variability and if they are too far from each other, the morphology of the input model will be compromised. Checking if the set of realizations has enough variability and still resembles the original concept can be done by looking at the mean and variance maps, as shown from Figs. 4, 5, 6, 7, 8, or even looking at individual realizations sampled from the set as in Attachment A.

For the geostatistical simulations, it is interesting to provide a target "*Distribution*" so the output realizations will have the desired proportion of simulated values, or in other words, the histogram of each realization will have a certain desired shape. For example, if a concept model has twice as much low-property values as high-property values, it is interesting to keep the same proportion in the realizations. Additionally, it is necessary to determine a "*Variogram*" that yields realizations compatible with the concept model morphology. Variogram and distribution definitions can be done interactively to restrict realization distortion when compared to the originating concept.

The likelihood of each concept is represented by the "*Number of realizations*" created in each iteration *m*. For example, if it is believed that all concept models are equally probable, the same number of realizations should be created for each of them, mimicking a uniform probability distribution. The "*Number of realizations*" acts as a weighting factor for the mathematical aggregation of different experts' opinions, combining the realizations into the same set, and its value can be set as an expert consensus or a DM trust-based definition.

This description of how to create a realizations-set for each concept (left side of Fig. 1) implies a geostatistical framework that uses variogram functions as input, which in our case is the SGS. Our elicitation method could use any geostatistical

![img-1.jpeg](img-1.jpeg)

**Fig. 2** Concept models overlaid by control points (white dots), well positions (white crosses), and corresponding variability areas

framework of choice (e.g. MPS, process-mimicking) by directly taking realizations-sets from them. The only restriction is that the realizations satisfactory resemble the concepts and have variability in the vicinity of the well positions.

### 3.2 Stochastic dataset

The right side of Fig. 1 shows how to obtain the JPD from the geostatistical realizations. All realizations collected from all $M$ concept models are stacked into the "Accumulated realizations dataset", from where the "Sampling" task samples property values within the "Search range" $(r)$ of "Wells positions". Considering the subjective character of the concept models, the precise position of the prospect is less relevant than its relative position to the other prospects. In this sense, the "Search range" $(r)$ is a parameter that defines the area, centered on each well location, where property values are sampled and must be smaller or equal to the variability range. For a 2D realization, the total number of samples $N_{s}$ to be collected in each realization, considering the total number of wells $n$, is:
$N_{s}=n(1+2 r)^{2}$
For example, if the search range is set to 0 , only the value corresponding to the exact location of each well is sampled, and the collection of the $n$ samples for each realization becomes a single entry in the "Stochastic dataset". In this case, the number of entries in the stochastic dataset will be the same number of accumulated realizations. By increasing the range, it is possible to increase the number of entries for a single realization by a factor of $(1+2 r)^{2}$, reducing the total number of realizations necessary for better statistical description.

### 3.3 Processing methods

The "Joint probability distribution" is the end result of the workflow and is estimated from the stochastic dataset using the preferred "Processing method". The simplest processing is to estimate joint probabilities by counting the occurrence for each possible joint event in the dataset and dividing it by the total number of entries. The collection of joint probabilities for all possible joint-events forms the JPD which might be stored in a multi-dimensional matrix. Here this approach is simply referred to as "the counting method" which is the base processing used in the JPDs comparison presented in section 8.

In the counting method, joint-events without occurrence are assigned zero joint-probability so it assumes that there are enough ${ }^{8}$ entries to represents the probabilistic problem. It can be contested, as Carl Sagan said: "absence of evidence is

[^0]not evidence of absence", so the next subsections present a few other ways of estimating the JPD starting from the same stochastic dataset.

### 3.3.1 Additive smoothing

Smoothing is a technique used in language modeling to correct the probabilities of events not found in the dataset [24]. These techniques adjust the probability estimates by making the distributions more uniform, i.e. events previously assigned with zero probability are reassigned with a small probability value, and events previously assigned with high probability are reassigned with a slightly lower probability. The additive smoothing adds a small quantity $0<\alpha<1$ to the frequency of a certain joint event. Here this concept was adapted to directly correct the joint probabilities:
$P_{\text {smooth }}=\frac{P_{\text {original }}+\alpha}{1+\alpha N}$
The probability correction is applied to all $N$ joint probabilities, yielding a new JPD. The value $\alpha$ is designed so the minimum probability of the corrected distribution corresponds to a certain arbitrary value instead of 0 . For our application, $\alpha$ was chosen to be about one order of magnitude lower than the smallest non-zero probability before smoothing, giving $\alpha=$ $1.0710^{-6}$. Also, for cases where $\alpha$ is expected to be much lower than the maximum joint probability, $1+\alpha N$ approximates the factor by which non-zero probabilities are decreased.

### 3.3.2 Maximum entropy principle

The maximum entropy principle (MEP) described in [12] and used in $[1,25]$ in the context of optimizing the drilling sequence, estimates the JPD through a minimization problem where the constraints are the marginal and conditional probabilities. While applying our method to the example in section 5 , we attempted to generate a JPD starting from the counting method and applying the MEP later, but it was unsuccessful. We believe that the failure is due to the size of the distribution, which has a larger number of variables and constraints when compared to the published examples. In our example, the minimization process converges to a JPD very similar to the initial distribution guess.

### 3.3.3 Generative modeling

In the machine-learning field, generative models belong to a class of algorithms designed to estimate the joint distribution of the random variables based on a training dataset [26, 27]. This concept is interesting since it bridges the gap between our stochastic dataset and the JPD estimation. Generative models


[^0]:    ${ }^{8}$ The determination of the number of entries in the dataset will depend on how many variables exist in the probabilistic model and is part of the elicitation process. JPDs obtained from datasets with different number of entries can be compared by solving the decision problem.

include Naive Bayes, Autoencoders, and Generative Adversarial Networks (GAN). [28] describe the implementation of a derivative method from GAN called Conditional Tabular GAN (CTGAN) which was used here to build an alternative version of the JPD. Here the CTGAN will be used to generate a stochastic dataset of $10^{6}$ and $10^{7}$ samples when trained with the original dataset ( 30,250 samples from range 5 and 110,250 from range 10).

### 3.4 JPD assessment

While running the elicitation workflow in Fig. 1, experts should check if the marginal and conditional probabilities present in the resulting JPD are reasonable given their knowledge of the uncertain process and any supporting data. This check may be demanding depending on the number of variables, states, and the experts' domain knowledge. If the JPD does not satisfactorily reflect the experts' beliefs, the entire workflow should be repeated with different input parameters until a reasonable JPD is reached. This approach is valuable in the elicitation process because it extracts the knowledge from experts visually and interactively, whilst ensuring that the process is comprehensive and traceable.

To check how sensitive the decisions are to different numbers of entries and processing methods, alternative JPDs created from the same dataset can be used to solve the sequential decision problem. Comparing different JPDs helps experts in the elicitation process as it provides information about the effect of the elicitation process in the actual decisions.

### 3.5 General comments

It is quite easy to make inferences in a probabilistic model explicitly represented by its JPD. Given the JPD, marginal and conditional probabilities are found simply by summing the probabilities over the variables not explicitly elicited, and doing so becomes a matter of navigating into subsets of the JPD. For example, to find the marginal distribution in Well $X$, the JPD values should be summed over all variables but Well $X$, collapsing the multi-dimensional matrix into a single dimension vector. To find the conditional probabilities of Well $X$ given Well $Y$ (or vice versa), the summation will be done over all variables but Well $X$ and Well $Y$, collapsing the original distribution into a two-dimensional matrix, representing a subset of the original JPD.

In a 2D application, each horizontal position will contain a single property value representing it. In a 3D application, each position has multiple property values along the depth. In this case, one could assess the corresponding expected hydrocarbon reserve values (or equivalent NPV) and sum it along the depth, resulting in a single value per horizontal position, transforming the modeling into a reserves-equivalent 2D model.

## 4 Facies indicator modeling choice

Facies type indicator is the geological property chosen to be modeled in the workflow application shown in the next section. The major reasons are because it relates more directly to a decision context to optimize the drilling sequence and, is visually straightforward which helps in the elicitation process. This section better explains the facies indicator choice and the reasoning.

### 4.1 Rationale about facies indicator

In the exploratory phase, geological knowledge is frequently obtained from petroleum system modeling [29], which describes the genesis process of hydrocarbon accumulations. The simultaneous presence of factors, namely: kitchen, trap, seal, migration, and reservoir presence are required for the hydrocarbon accumulation existence. Commonly, the elicitation process would assess the probability of each of these conditioning factors independently $[15,16]$ and estimate the discovery chance of success (CoS). CoS alone does not help the DM choose between two successful prospects since one may be more economically attractive than the other, even with a smaller CoS. For instance, a well might successfully discover oil but in small quantities or in poor-quality reservoirs, entailing economic loss. In this sense, a better definition of success is finding economic hydrocarbon reserves that can incorporate both CoS and economic value. This way events where at least one of the genesis factors is absent entail in absence of reserves whilst events where there is the presence of hydrocarbons are valued differently by their reserve estimation. A simple model for reserves estimation is presented in Eq. 3:
$\operatorname{Reserves}($ well $)=\left(\pi r_{d}^{2} h_{o}\right) N T G\left(\Phi_{e} S_{O} / B_{O}\right) O R F$
Here the reserves attributed to a well is a function of its Net-to-gross ratio (NTG), average effective porosity $\Phi_{e}$ along the oil-bearing zone, average oil saturation $\left(S_{o}\right)$, formation volume factor $\left(B_{o}\right)$, estimated oil recovery factor $(O R F)$, the equivalent drainage radius $\left(r_{d}\right)$ attributed to the well, and the thickness bearing oil $\left(h_{o}\right)$. All these parameters are uncertain but for the sake of illustration, when considering all variables constant but $h_{o}$ and $\Phi_{e}$, the reserves are proportional to the product $h_{o} \Phi_{e}$.
$\operatorname{Reserves}($ well $) \propto h_{o} \Phi_{e}$
The thickness $h_{o}$ is kept explicit because it might be correlated to seismic surface maps and useful when evaluating prospect locations. Given the lack of well-data, it is more reasonable to work qualitatively with facies indicator $(f)$ distribution rather than porosity distributions. The variable $f$ is categorical (e.g. coarse sand, shale, facies \#1, facies \#3) and

relates to geologic numerical properties. Through the use of correlations found in analogous fields, the porosity becomes a stochastic function of the facies indicator $\Phi_{c}(f)$, just like oil saturation $S_{O}(f)$, and recovery factor $\operatorname{ORF}(f)$. In this simplified representation, the reserves become a function of $h_{o}$ and $f$. Moreover, the relationship between facies type and the reservoir quality is more intuitive (e.g. shale, laminated sand, coarse sand).

### 4.2 Design of facies concept models

The spatial distribution of $f$ can be modeled from basin-level studies, analogous fields data, and seismic data. Such models display possible depositional environments and the corresponding possible spatial dispositions of facies. Modeling could be as simple as a conceptual drawing using analog data to generate scenarios about the morphology (e.g. paleochannels, geobodies), could use systematic methods [30], or even derive from the whole sedimentary basin models [29]. The last approach is called Basin and Petroleum Systems Modeling [16] and is available in commercial software. Seismic inversion techniques are also useful resources for the conception of facies models needed in the workflow [31-33]. In [31, 32], the concept of sand probability can be directly related to the facies models.

### 4.3 Facies modeling embeds genesis parameters

It might seem strange that in an exploratory context, the uncertainty about discovery does not account for the genesis process of hydrocarbon accumulation or, in other words, how can someone model reserves without knowing if the reservoir contains hydrocarbons? In our method, the genesis factors (kitchen, trap, seal, migration, and reservoir presence) are all embedded in the facies modeling. It is assumed that reservoir facies occur where all these factors are present whilst all the events where at least one of the factors is absent are modeled as non-reservoir facies. This assumption means that if there is reservoir, there is hydrocarbon. The chances of success can be calibrated by artificially increasing the joint events of non-reservoir facies in all wells.

The adjustment of the CoS for different wells can be accomplished by generating realizations that have the same effect on the reserves. One approach is to use a concept model that includes non-reservoir facies for regions below a certain CoS threshold and reservoir facies for regions with higher CoS , adjusting the number of realizations so the marginal probability of finding non-reservoir corresponds to the expected probability of unsuccessful drilling. Another approach is to increase the proportion of non-reservoir facies, used as input to the geostatistical modeling until the marginal and conditional probabilities are coherent with the traditional CoS concept. In situations where hydrocarbons have already been
found in the area, or for appraisal phases, the facies modeling does not require any of these adjustments.

## 5 Application

The method will be demonstrated in a synthetic 2D model, developed to represent a simple yet realistic exploratory case. The prospective area is $7,5 \mathrm{~km}$ by 10 km and is overlaid by a grid of 50 m by 50 m cells, resulting in 150 cells in the $x$ direction and 200 cells in the $y$-direction. Regional knowledge about the basin suggests that the prospection target is a deep marine depositional environment with the sediment source located north of the area but with the exact location unknown. The objective of this example is to identify the optimal drilling sequence of the exploration campaign, where the prospect locations are previously chosen based on seismic horizons and other relevant information. The objective is met through a decision process that requires the probabilistic assessment of the area.

The knowledge from different experts about the depositional environment of the area is represented by the facies models shown in Fig. 2, which are the concept models in the elicitation workflow notation. Due to a lack of additional evidence, the five models are considered equiprobable. Shale is represented by facies type \#0 (purple), poor-quality sandstone by \#1 (light blue), medium-quality sandstone by \#2 (yellow), and high-quality sandstone by \#3 (red). The average porosity and permeability attributed to each facies-type increase with the reservoir quality (from \#1 to \#3), while shale is not a reservoir rock. In this example, we limit the number of concept models to five. However, in a more realistic application, there could be as many models with as many facies types as necessary to express the limitation of knowledge about the area.

The prior exploration campaign considers drilling 8 exploration wells denoted $A$ through $H$ with their exact positions shown in Table 1. The initial drilling order is alphabetical because wells $A, B$, and $C$ have respectively the highest CoS and in case of positive results, further prospects would investigate further volume.

Figure 3 is obtained by superimposing the 5 concept models considering the facies categories as scores from 0 to 3 , where 0 means non-reservoir and 3 means high-quality reservoir. The superimposed map is the sum of the scores to a maximum of 15 . In this map is possible to observe the positions of the 8 exploration wells.

In the elicitation method, the 8 wells become random variables with 4 possible states (facies) where the complete set of joint probabilities requires $4^{8}-1=65,535$ assessments. The size of this problem was chosen to be small enough to be tractable on desktop computers and large enough to portrait a more generalized process and solution.

Table 1 Well positioning of the drilling campaign


The variability range, spacing of the pilot-points, and variogram parameters, all necessary to proceed with the workflow, were determined based on several iterations with the geostatistics tool. The pilot-points are visible in Fig. 2 as a grid of white dots and the variability ranges are the vicinity of the wells where the pilot-points are absent. The main objective is to have realizations that respect the geological knowledge and collectively have variability around the wells. The chosen pilot-points spacing is 5 cells and the variability range is 10 cells, while the chosen variogram parameters are presented in Table 2. In addition to expert knowledge, the variogram parameters can be determined using available data from the area or analogous fields.

In SGeMS software, the variogram ranges are set as the number of cells, the major-range is measured along the vertical axis, the medium-range along the horizontal axis, and the azimuth angle is clockwise starting from the vertical axis. The nugget effect is a variogram parameter that affects the

![img-2.jpeg](img-2.jpeg)

Fig. 3 Quality surface superimposing the facies models

Table 2 Variogram ellipsoid ranges and azimuths for each facies model


variability of closely spaced samples and, after the interactive process, was set to 0.1 for a total sill of 1. The chosen variogram function was Gaussian.

Finally, the distribution of values is exactly the facies proportion observed in each concept model and, the number of realizations was arbitrarily set to 50 for each iteration *m*. Creating 50 realizations from each of the 5 facies models leads to a total of 250 realizations.9 This description covers all necessary information used to generate the realizations dataset.

Figures 4, 5, 6, 7, 8 present the statistical summaries of each model, calculated using the same system of scores from 0 to 3. The average (left figure part) and variance (right figure part) were calculated for each cell along all realizations. Within these figures, hotter colors mean higher values and white squares delimit the areas with the variability range of 10 cells. The pilot-points are visible in the variance maps appearing as purple dots. Attachment A shows realizations samples from each index concept model. Average maps show that morphology is kept in the ensemble and the variance maps show that variability was successfully created within the search area from where the sampling will occur.

In Fig. 9, the average and variance maps are shown for the complete accumulated set. From the average map, we observe that well *A* is positioned in the area with the highest expectation and well *H* with the lowest. In the variance map, the upper and lower parts have higher values, indicating where the depositional concepts differ most, surpassing the variability generated in the central wells.

The accumulated realizations-set is the key to transform the elicited knowledge into a statistical process. If facies values were collected only from the exact well locations, the dataset would contain 250 occurrences, and would not be reasonable to directly extract the JPD from it. There must be enough data to adequately represent the relationship between wells and that is why the definition of a search range is necessary. It is an interactive process and here it was decided to look for search ranges of 5 and 10 cells, resulting in datasets with 30,250 and 110,250 entries, respectively.

^{9} The choice of 50 realizations of each concept is arbitrary and does not need to be larger as the number of samples is boosted by increasing the search range, i.e., sampling the well surroundings. A sensitivity about the number of realizations is presented in section 8.

Fig. 4 Average map (left) and variance map (right) of the realizations set created from facies model 1

Fig. 5 Average map (left) and variance map (right) of the realizations set created from facies model 2

Fig. 6 Average map (left) and variance map (right) of the realizations set created from facies model 3

Average map of Model1

![img-3.jpeg](img-3.jpeg)


![img-4.jpeg](img-4.jpeg)


![img-5.jpeg](img-5.jpeg)

Fig. 7 Average map (left) and variance map (right) of the realizations set created from facies model 4

Fig. 8 Average map (left) and variance map (right) of the realizations set created from facies model 5

Fig. 9 Average map (left) and variance map (right) of the accumulated realizations set

Average map of Model4

![img-6.jpeg](img-6.jpeg)

Variance map of Model4

![img-7.jpeg](img-7.jpeg)

Variance map of Model5

![img-8.jpeg](img-8.jpeg)

Variance map of Model5

![img-9.jpeg](img-9.jpeg)

Average map of realizations dataset Variance map of realizations dataset

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

## 6 JPD quality assessment

Marginal probabilities obtained from both range options (5 and 10 cells) are shown in Fig. 10 along with their absolute difference. Moving from range 5 to 10 , the largest variations were: $P(A=\# 3)$ decreased $8,5 \% ; P(A=\# 2)$ increased $7,4 \% ; P(F=\# 1)$ increased $6,4 \%$; none of them significantly changing the shape of the distributions. At the same time, the number of unique joint events increased from 6662 to 10,825 out of the 65,356 possibilities, meaning that 4163 new unique occurrences were found and will have a probability assigned. The effects of the search range in the decision results are shown later and until then, all references to the realizations dataset are based on the case with a search range of 10 cells.

Through the process it was possible to obtain a JPD where all facies types can be expected in every well, i.e. none of the marginal probabilities are zero. The marginal probabilities confirm the information from the average map in Fig. 9 where Well $A$ has the smallest chance of finding shale and the largest chance of finding high-quality sandstone. Well $B$ has worse expectation than $C$ and $D$, whilst Well $H$ has the worst expectation and may end up being canceled depending on the drilling results from other wells.

For the cases where experts do not agree with the results, changes should be made in the input parameters to guide the results towards distributions that better represent their belief. For instance, if one believes that $\mathrm{P}(\mathrm{A}=\# 0)$ is too low, increasing the number of realizations from concept model 3 would increase this probability. If one believes the JPD is too optimistic, then the probability of non-reservoir facies should be increased for all wells, which can be accomplished by adding new entries of facies \#0 in all wells directly to the stochastic dataset, increasing their relative frequency.

During the interactive process of creating the JPD, we observed that the maps from Figs. 4, 5, 6, 7, 8, and the marginal distributions, are good overall indicators of how well the JPD captures the experts' expectations considering the chosen parameters.

Inspection of conditional probabilities to evaluate prospect dependencies, i.e. how information obtained from one well (or more) changes the expectation of others, provides a deeper assessment of the JPD. For an exhaustive assessment of pairwise conditional probabilities would require 224 conditional distributions, with a total of 896 probability values. Some of these distributions might be more relevant than others and a smarter approach is to find a better indicator of key dependencies among the prospects.

### 6.1 Mutual information metric

Information theory, founded by Shannon [34], includes metrics that can be used to assess the amount of information contained in a probability distribution [35, 36]. Among the metrics, mutual information $I(X, Y){ }^{10}$ stands out because it represents the amount of information obtained from one well by observing another:
$I(X, Y)=\sum_{y \in f} \sum_{x \in f} P(x, y) \log \left(\frac{P(x, y)}{P(x) P(y)}\right)$
where, in our example, the random variables $X$ and $Y$ are different wells belonging to the set $\{A, B, C, D, E, F, G, H\}$ and can, respectively, assume values $x$ and $y$ from the facies set $f=\{\# 0, \# 1, \# 2, \# 3\}$. $P(x, y)$ is the pairwise joint probability while $P(x)$ and $P(y)$ are the marginal probabilities. Mutual information is symmetric and the complete set of measurements in the original JPD is shown in Table 3.

Well $H$ has the highest values considering all other wells, indicating that observing its outcome greatly impacts the expectations of the remaining wells, or, observing other wells greatly impacts expectations for well $H$. At the same time, well $F$ has, on average, the lowest mutual information values meaning that its outcome has a lower impact on other expectations and vice versa.
$I(B, H)=0.234$ stands out as the highest value in the table because their positioning provides quite different results in almost all concept models. For example, it is expected that $B=\# 0$ and $H=\# 3$ in model 1 and $B=\# 2$ and $H=\# 0$ in model 4. in the concept models. $I(A, C)=0.008$ stands out as one of the lowest values in the table because good results in one can mean good results in the other like in models 2 and 4 or bad results like in models 1 and 3 .

Though very intuitive, this metric lacks description on whether the pairwise relationship has a positive or negative correlation, or in other words, how finding a specific facies type affects the probability of finding another facies type.

### 6.2 Pairwise entropy variation

Entropy is a measurement of how much uncertainty is contained in the distribution, reaching its highest value for the uniform distribution and zero when a single event has $100 \%$ probability; i.e., certainty. The entropy is given by:
$\mathcal{H}(X)=-\sum_{x \in f} P(x) \log (P(x))$
where $\mathcal{H}$ is the entropy of the random variable $X$ and $P(x)$ is the probability of $X$ having facies $x$. For the application in this article, each well has 4 possible states, hence the maximum entropy of any marginal distribution corresponds to the entropy of the uniform distribution of 4 discrete states which is 0.6021 . Extending this concept to a case where information about another variable $Y$ is known to be $y$, the conditional entropy value is calculated as:

[^0]
[^0]:    ${ }^{10}$ In this article all information-theoretic metrics are calculated with logarithm base $e$

$$
\mathcal{H}(X \mid Y=y)=-\sum_{x \in J} P(x \mid y) \log (P(x \mid y))
$$

The difference $\mathcal{H}(X \mid Y=y)-\mathcal{H}(X)$ is called here pairwise entropy variation $\Delta \mathcal{H}(X \mid Y=y)$ and measures how much uncertainty has changed about $X$ after finding that $Y=y$. It has more resolution than mutual information because it shows how specific facies values impact the posterior distribution. The values.

Table 4 shows the entropy variations as a percentage of the entropy from the uniform distribution ( 0.6021 ) for the variables in the rows after finding specific facies value in the variables in the columns.

The values in the table theoretically range from $-100 \%$ to $100 \%$. Positive difference means posterior distribution is closer to the uniform distribution (i.e. less certain) and a decrease in entropy value means that it is closer to depicting a single most probable outcome (i.e. more certain).

The relationships are not symmetric; e.g., $\Delta \mathcal{H}(A \mid H=0)=$ $8.6 \%$ while $\Delta \mathcal{H}(H \mid A=0)=-62 \%$. The fact that specific observations have specific impacts on the posterior distributions provides a more comprehensive quality check of the JPD. Table 4 results help pinpoint the extreme examples of how information reduces uncertainty in Fig. 11 or increases uncertainty in Fig. 12.

Based on a thorough analysis of all relationships (suppressed here), it is possible to better understand the relationships among wells. Starting with well $H, P(H=\# 0)$ increases greatly with $A=\# 0$ and $G=\# 0$, while $P(H=\# 3)$ increases greatly with $B=\# 0$ and $G=\# 3$. This relationship follows directly from the alignment of prospects $H, A, D$, and $G$ in the direction of facies \#3 path in the concept model 1 (see Fig. 4) while being almost orthogonal to the alignment of prospects $B$ and $C$ in concept models 2, 3 and 4 (see Figs. 5, 6, 7). This is the same reason for $\mathrm{P}(\mathrm{B}=\# 0)$ greatly increase with $\mathrm{H}=\# 3$ and $\mathrm{C}=\# 0$. On the other hand, central prospects $A, C, D$, and $F$, have less probability variations among them, suggesting that the difference among facies models is the main contributing factor for higher entropy variations. If a smoother entropy variation is desired, more concepts should be added to the workflow, resulting in a transitioning pattern of the main directions of deposition.

## 7 Optimal sequential drilling policy

The purpose of developing the JPD is to support decisions on optimal drilling policy, so, it is important to assess how different JPDs affect the decision results, similar to a sensitivity analysis. In this section, the decision framework and the method of sequence optimization are briefly described. Figure 13 shows a simplified schematic of the decision model with 8 wells, each having 4 possible states. Initially, there are 9 alternatives: drill one of the 8 wells or none. If the choice is to drill, each alternative
expands into a set of possible outcomes where each outcome connects to another decision node, until the last drilling decision is made.

In a sequential forward-thinking, after deciding the first position, there will be fewer alternatives for the next decision and so on, until the last decision. Revenue ${ }^{11}$ and probability ${ }^{12}$ values are assigned to each possible outcome. The goal is to identify the sequence of decisions that maximizes the exploration campaign EV, i.e. identify the optimal drilling policy. It is done by always choosing the alternative with the highest expected revenue value, no matter the outcome. To that end, it is necessary to know the optimal choices of all future decision epochs, so, EV calculations must be done exhaustively in a backward fashion, starting from the possible decision nodes of the last epoch. This method of solving sequential decision models was studied and formalized by Bellman in [37] and for probabilistic applications is called Stochastic Dynamic Programming (SDP), summarized with this modified version of Bellman's equation:
$V_{i}(\boldsymbol{\omega})=\sum_{j=1}^{k}\left\{P\left(x_{i}=o_{j} \mid \boldsymbol{\omega}\right)\left(r_{i}^{j}+\delta V\left(\boldsymbol{\omega}_{i}^{j}\right)\right)\right\}$
where, for a generic decision node, each alternative indexed $i$ has $k$ possible outcomes $o$ indexed $j$, each with probability $P\left(x_{i}=o_{j} \mid \boldsymbol{\omega}\right)$ and immediate reward $r_{i}{ }^{j}$. The vector $\boldsymbol{\omega}$, represents all the information available at this decision node and is updated to $\boldsymbol{\omega}_{i}{ }^{j}$ when outcome $o_{j}$ is observed in the alternative $i$. Finally, $V_{i}(\boldsymbol{\omega})$ represents the EV of each alternative at decision nodes, considering each outcome immediate reward $r_{i}^{j}$ added to the maximum expected value $V\left(\boldsymbol{\omega}_{i}{ }^{j}\right)$ of all subsequent optimal decisions deriving from $o_{j}$, discounted by a factor $\delta$. Equation 8 is recursive and shows how to substitute all future decisions deriving from each alternative, by a single revenue EV obtained by applying the highest EV criterion. The optimal decision never has a negative EV because there is always the option of not drilling.

The solution process promotes the orderly substitution of each decision node in the model by its equivalent EV when applying the optimal criterion. It starts from the last decision stage $\left(V\left(\boldsymbol{\omega}_{i}{ }^{j}\right)=0\right)$ and proceeds backward until a single EV representing the optimum policy is found. Since all possible future EV (known as continuation values in $[1,6]$ ) had to be calculated in the process, the optimum policy contains the best course of action for every possible outcome.

### 7.1 Revenue model

The revenue model, also known as the value function in [38], describes the immediate reward $r_{i}{ }^{j}$ for every possible outcome in the decision model. For simplicity, in our application, the

[^0]
[^0]:    ${ }^{11}$ The revenue model is defined in section 7.1.
    ${ }^{12}$ Obtained accordingly from the JPD


Fig. 10 Comparison of marginal probabilities obtained with a search range of 5 and 10 cells
revenue model presents a constant relationship with the facies type found in the wells. The net revenue is -10 economic units if the well lands in facies type \#0, representing the cases where there are no hydrocarbon reserves. If the well lands facies \#1, net revenue is -1 economic unit, representing a small reserve volume but not enough to compensate for the drilling cost. If it lands in facies \#2 or facies \#3, the net revenue is 20 and 40 economic units, respectively, reflecting that reserves are correlated with facies type through different porosity and permeability distributions in different facies, as described in Eqs. 3 and 4.

The discount factor plays a role in balancing the prospect's direct monetary reward $\left(r_{i}{ }^{f}\right)$ and indirect expected monetary reward $\left(V\left(\omega_{i}{ }^{f}\right)\right)$ obtained in the future. In the oil exploration context, the wells might only produce after the declaration of commerciality and production facilities are built. For that, we chose not to penalize future cash flows during the exploration campaign by setting $\delta=1$.

### 7.2 Solution complexity

The termination branches of the equivalent decision tree are called leaves and are estimated to be 3.4 billion for the current example, including the "Don't drill" alternative. The exponential increase of the number of leaves with the size of the sequence (dimensions) was called the "curse of dimensionality" in [37] and is one major reason why sequential decision problems are frequently simplified. Our method describes an

Table 3 Pairwise mutual information


elicitation process that provides the JPD explicitly in a matrix form, which helps to solve the sequential decision model by reducing the solution time when compared to implicit JPD representations like Bayesian networks.

## 8 Comparison of results

In this section, the JPDs obtained from alternative processing methods will be used to identify the decision policy that optimizes the sequential drilling problem. By comparing the results, it is possible to evaluate the impact of different considerations on the final decision policy and optimized value. The idea is to select the smallest search range and simplest processing method, or in other words, the lowest probabilistic model resolution, from which there is no change in the decision process.

### 8.1 Comparison description

Table 5 shows 16 different JPDs using search range of 5 cells (indexed from 1 to 8 ) and 10 cells (indexed from 9 to 16). The starting point is the counting method based on the 250 realizations ( 50 from each concept) corresponding to distributions 1 and 9 . The additive smoothing method (blue font) is applied over distributions 1 and 9 considering two different values of minimum joint-probability $\left(P_{\min }\right)$, consequently altering the maximum joint-probability value $\left(P_{\max }\right)$. The CTGAN algorithm (red font) is trained using the same dataset from distributions 1 and 9 , and used to generate other versions of the JPD by resampling the model using $10^{6}$ and $10^{7}$ samples, increasing the number of unique joint-events found. The sensitivity of the JPD to the number of realizations is assessed from increasingly larger geostatistical datasets. Distributions 6 and 7 are obtained by counting joint-events from 500 realizations set, and distributions 14 and 15 from 1000 realizations ${ }^{13}$.

[^0]
[^0]:    ${ }^{13}$ The initial 250 realizations set is a subset of the 500 realizations set, which is also a subset of the 1000 realizations set.

Table 4 Relative pairwise entropy variation given outcome finding


![img-12.jpeg](img-12.jpeg)

Fig. 11 Examples of high decrease in entropy given new information

In our analysis, the JPD obtained from the 1000 realizations is considered the comparison reference, and the KL-distance [14] measures how dissimilar each JPD is to this reference distribution ${ }^{15}$. The entropy value is presented as a measure of how much uncertainty is present in each distribution. Its minimum possible value is 0 corresponding to a JPD where a single joint event has $100 \%$ probability of occurrence (certainty). Its maximum possible value is 4.82 corresponding to the uniform distribution with the 8 variables with 4 possible states each (highest uncertainty).

The prior EV is calculated using the marginal probabilities obtained from each distribution (e.g. Fig. 10) and the revenue model described in section 7.1. This value corresponds to the expected value of the drilling sequence before gathering any additional information. $V_{0}$ is the exploration campaign's optimal expected revenue, i.e. when the drilling sequence follows the optimal drilling policy identified by the SDP using geological information. $\Delta V_{0}$ is the difference between the prior EV and $V_{0}$ (posterior) corresponding to the total value of information (VoI) of the drilling sequence. Prior EV is the minimum EV of the sequence, consequently, $\Delta V_{0}$ is higher or equal to zero.

The last columns show the first well of the policy followed by the candidates for the second well. The first does not depend on any additional information while the second well depends on the outcome of the first one, hence there are 4 possible candidates.

### 8.2 Results analysis

Increasing the number of geostatistical realizations slightly increases the entropy and manages to increase the

[^0]number of unique events but with a much lower proportion. The limited number of samples raises concerns about the overfitting of the JPDs. This concern is the main reason different processing techniques are tested. The processing options provide alternatives for building the JPD that avoids assigning zero probability to events given the limited number of samples from the stochastic dataset. The regularization effect is observed in the column Unique events where the CTGAN greatly increases the number of observed joint-events and the smoothed distributions provide (by definition) join-probability values to all 65,536 possible events. The effect is also observed by the slight increase of the entropy and the increase in KL distance from the reference distributions (7 and 15).

Analyzing the metrics for JPDs built using a search range of 5 cells against the ones using and 10 cells, we observe that the processing methods have similar effects on both ranges, except for the Prior EV. There is a systematic difference of about 5 economic units between the prior EV of these two ranges which is propagated to the posterior $V_{0}$ and consequently disappears in the $\Delta V_{0}$. This difference comes from a fundamental difference in the marginal probabilities which in turn reflects the spatial uncertainty modeled in the JPDs. When using the range of 5 cells, the proportion of neighboring facies type is lower as the sampling area has a lower overlap with the neighbor facies type in the concept models (see Figs. $4,5,6,7,8)$. Increasing the search range from 5 to 10 adds more spatial uncertainty, systematically increasing the entropy and reducing the prior EV of all deriving JDPs. This search range relationship is important to the elicitation process as this helps experts to better tune this parameter according to their prior beliefs.


[^0]:    ${ }^{15}$ Distributions built using range of 5 cells use distribution 7 as reference and distributions built using range of 10 cells use distribution 15 as reference.

![img-13.jpeg](img-13.jpeg)

Fig. 12 Examples of increase in entropy given new information
![img-14.jpeg](img-14.jpeg)

Fig. 13 Decision tree schematic

At last, using different JPD versions might change the decisions to be made, i.e. the policy. The initial part of the policy from both reference distributions ( 7 and 15) are identical, regardless of the search range, starting with well $C$ and having well $G$ if $C=\# 0$ or well $D$ for any other result. The policies from the JPDs using the CTGAN method differ most from the reference distribution, with distribution 13 having the biggest difference. All other distributions (excluded the ones from CTGAN) have very
similar policies to the reference, with the difference being that if $C=\# 0$, then well $D$ is recommended, and if $C=\# 1$, then well $G$ is recommended. This is a minor change because when one follows these policies to the third well in the sequence, $G$ appears after $D$ and $G$ appears after $D$.

It is interesting to observe that although well $A$ has the highest marginal EV, the first well in the policies is well $C$ which ranks 2nd in the marginal EV. After well $C$, either well $D$ or $G$ is the

Table 5 Comparison of the JPDs under consideration


next in the drilling sequence ranking 3rd and 4th in the marginal EV. Well $G$ appearing as a second candidate is interesting because its EV ranks 4th in the marginal EV and it is positioned farther away from the center, indicating its spatial information relevance in the decision-making process. Overall, the geological information brought by $G$ compensates its prior lower expected values.

## 9 Assumptions and implications

This section states the implicit assumptions made during the elicitation method and its subsequent application in the sequential decision model.

### 9.1 Geostatistical framework given new data

Once the geostatistical realizations provide a satisfactory JPD, they are not used anymore because the spatial relationship they provide is present in the JPD and because all possible outcomes (in our example is facies types) are considered in the modeling. In other words, the JPD is capable of standing alone during the actual exploration campaign.

However, in the situation where the belief of the original assumptions (e.g. concept model, variogram) changes as a result of new geological evidence, the original JPD would be inadequate and the whole elicitation process would have to be repeated to properly update the JPD.

The SDP adds value by considering the intertwined relationship among decision and information which would not be possible to exploit without at least two subsequent information acquisitions using the same JPD. Rebuilding the geostatistical realizations every time new information arrives is considered a closed-loop approach (e.g. [39]) which fundamentally differs from the SDP. For this reason, it is beneficial to try to anticipate many different scenarios during the elicitation process.

### 9.2 Production interference

The revenue model described in section 7.1 assumes that the outcome of one well does not affect the outcomes of the other wells, e.g. when the decision metric is hydrocarbon volume in-place. This assumption does not hold for reserves if the production of the wells under consideration might be significantly affected by the production (or injection) from the others. In this case, the revenue model must account for these interferences, described in [38] as a coupled value function.

The development of revenue models that account for production interference among wells can be done through the use of subsurface flow simulations and are the subject of future work.

### 9.3 Well locations given new data

Another assumption upon the method builds is the fixed location of the drilling candidates. The consideration of the variability and search ranges means that small location changes within these areas are already accounted for in the modeling. But in situations where new information demands larger location changes, another JPD would have to be replaced.

If the original input parameters and assumptions still hold, the same realizations set could be used to re-sample the stochastic dataset. This is a great advantage of the method because the effort of building a JPD with different numbers of wells and positions does not depend on the realizations set.
[40] presents a method that intentionally starts with a larger number of candidate positions and lets the SDP "filter" the poorer locations and the changing of well location is naturally done by the drilling policy obtained from the SDP.

## 10 Conclusions

The work presented here shows a novel method to elicit probabilities for value creation and decision-making support in the context of hydrocarbon exploration. It is based on a geostatistical process that "translates" geological expert knowledge into probabilities through the creation of conceptual models representing possible subsurface bodies. In the absence of well-data, the conceptual models can be created based on any other source of information available whilst the presence of well-data further assist conceptual modeling. The method is by nature interactive as it gradually shapes input parameters to assess if resulting realizations and their corresponding JPDs are representative of experts' current beliefs.

Implementation complexity depends on available resources. Even a relatively simple 2D model, as presented and discussed in this article, might suffice for decision-making. The application of the method illustrated how to specify required input parameters. While creating the realizations, the parameters to be determined are the variogram functions, number of realizations, variability range, and pilot-point spacing. Later, to build the JPD the parameters required are the search range and the processing method. To assess whether the resulting JPD reflects the expert's beliefs regarding geological relationships, quality-check procedures were demonstrated. Our experience is that the overall content of the JPD can be effectively ${ }^{16}$ and comprehensively probed through the inspection ${ }^{17}$ of sampled realizations (see Attachment A), average and variance maps, and marginal probability distributions.

[^0]
[^0]:    ${ }^{16}$ Here are presented the last result, after iterating several times with the geostatistical workflow. The inspections were effective during the iterations partial results which are surpassed here.
    ${ }^{17}$ Visual inspection to check if the process generated variability keeping the intended geometric "shape" of the property spatial distribution. The acceptance criterion is left to the experts conducting the process.

Further adequacy of the JPD is assessed through mutual information and entropy variation indicators, which analyze the conditional relationships among wells.

Increasing the search range increases the number of unique joint-events samples used in the JPD estimation which helps to reduce the overfitting effect. It also incorporates more spatial uncertainty to the JPD, reducing the optimal EV of the drilling sequence. It was also observed that the choice of 50 realizations from each concept model (250 in total) is robust enough considering the decision results, dismissing the need for probabilistic models with "higher resolution" (i.e more realizations). In the attempt to reduce, overfitting additive smoothing seems better than CTGAN because it did not change the resulting policy.

The policies obtained from the different JPDs seem to be similar among them. All optimal policies, begin with wells $A$ or $C$ and continue with either $A, C, D$, or $G$. A brief geological analysis shows that the exploration path within the policies seems to adapt to the probability contents of the different JPDs.

Future work will extend the approach discussed in this paper beyond the exploration phase of hydrocarbon fields where, traditionally, the decisions are embedded in the modeling workflow through optimization procedures [39, 41, 42]. An extension of the probabilistic approach presented here has the potential to improve decision-making during the development phase because the decisions will benefit from significantly better data support and the large number of reservoir simulations aimed to generate probabilistic production forecasts under geological uncertainty.

# Attachment A: Samples from the ensemble of realizations 

![img-15.jpeg](img-15.jpeg)

Fig. 14 Samples from the realizations of the concept model 1

![img-16.jpeg](img-16.jpeg)

Fig. 15 Samples from the realizations of the concept model 2
![img-17.jpeg](img-17.jpeg)

Fig. 16 Samples from the realizations of the concept model 3

![img-18.jpeg](img-18.jpeg)

Fig. 17 Samples from the realizations of the concept model 4
![img-19.jpeg](img-19.jpeg)

Fig. 18 Samples from the realizations of the concept model 5

Nomenclature JPD. Joint probability distribution; DM. Decision maker; SGeMS. Stanford Geostatistical Modeling Software; EV. Expected Value; SDP. Stochastic Dynamic Programming; KL. Kullback and Leibler (distribution divergence metric); $n$. Total number of wells (random variables); $k$. Number of outcomes (possible states); $m$. Index of the concept model; $M$. Total number of concept models; $N_{t}$. Number of samples in each realization; $r$. Search range, in number of cells; CoS. Chance of success; $N T G$. Net to gross ratio; $S_{t r}$. Average oil saturation; $B_{t r}$. Formation volume factor; $O R F$. Oil recovery factor; $r_{d}$. Equivalent drainage radius; $h_{t r}$. Thickness bearing oil; $\Phi_{t r}$. Effective porosity; $f$. Facies type indicator; $I(X \mid Y)$. Mutual information of random variable $X$ and $Y$; $P(x)$. Probability of variable $\mathrm{X}=\mathrm{x} ; P(x, y)$. Probability of variable $\mathrm{X}=\mathrm{x}$ and $\mathrm{Y}=\mathrm{y} ; \mathcal{H}(\mathrm{X})$, Entropy of variable X distribution; $\mathcal{H}(\mathrm{X} \mid \mathrm{Y}=\mathrm{y})$. Conditional entropy of variable X distribution given $\mathrm{Y}=\mathrm{y} ; \Delta \mathcal{H}$ $(X \mid Y=y)$, Pairwise entropy variation; $V_{i}(\omega)$. Expected value from alternative $\mathrm{i} ; \boldsymbol{\omega}$. Observation vector or key; $i$. Alternative index; $j$. Outcome index; $r_{i}{ }^{j}$. Immediate reward from outcome j of alternative $\mathrm{i} ;$ $V\left(\boldsymbol{\omega}_{i}{ }^{j}\right)$. Expected value coming from outcome j of alternative $\mathrm{i} ; P_{\text {original }}$. Joint probability from the maximum likelihood method; $P_{\text {omouth. }}$ Joint probability after additive smoothing; $\alpha$. additive smoothing parameter; $N$. Total number of probability values in the JPD; VoI. Value of information

Acknowledgments The authors acknowledge the Research Council of Norway and the industry partners - ConocoPhillips Skandinavia AS, Aker BP ASA, Eni Norge AS, Total E\&P Norge AS, Equinor ASA, Neptune Energy Norge AS, Lundin Norway AS, Halliburton AS, Schlumberger Norge AS, Wintershall Norge AS, and DEA Norge AS of The National IOR Centre of Norway for support. Also, the authors acknowledge Nicolas Remy and Alexandre Boucher for the SGeMS software, and Jianbing Wu and Lei Xu for the freely available CTGAN Python code.

Funding Open access funding provided by University Of Stavanger.
Data availability The datasets generated during and/or analyzed during the current study are available in Morosov, Andre Luis (2021), "Dataset Used in the Article: Probability Elicitation Using Geostatistics in Hydrocarbon Exploration", Mendeley Data, V1, doi: https://doi.org/10. 17632/5ndvnh6ffm.1.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
