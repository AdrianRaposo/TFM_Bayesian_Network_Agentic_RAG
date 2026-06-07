# Modelling uncertainty in social-natural interactions 

R. F. Ropero ${ }^{\mathrm{a}}$, R. Rumí ${ }^{\mathrm{a} b}$, P. A. Aguilera ${ }^{\mathrm{a}}$<br>${ }^{a}$ Informatics and Environment Laboratory, Dept. of Biology and Geology, University of Almería, Spain<br>${ }^{b}$ Dept. of Mathematics, University of Almería, Spain


#### Abstract

Socio-ecological systems can be represented as a complex network of causal interactions. Modelling such systems requires methodologies that are able to take uncertainty into account. Due to their probabilistic nature, Bayesian networks are a powerful tool for representing complex systems where interactions between variables are subject to uncertainty. In this paper, we study the interactions between social and natural subsystems (land use and water flow components) using hybrid Bayesian networks based on the Mixture of Truncated Exponentials model. This study aims to provide a new methodology to model systemic change in a socio-ecological context. Two endogenous changes - agricultural intensification and the maintenance of traditional cropland - are proposed. Intensification of the agricultural practices leads to a rise in the rate of immigration to the area, as well as to greater water losses through evaporation. By contrast, maintenance of traditional cropland hardly changes the social structure, while increasing evapotranspiration rates and improving the control over runoff water. These results indicate that hybrid Bayesian networks are an excellent tool for modelling social-natural interactions.


Keywords: Systemic change, Socio-Ecological System, Water flows, Hybrid Bayesian Networks, Mixtures of Truncated Exponentials

[^0]
[^0]:    ${ }^{\text {a }}$ Corresponding author.
    Email addresses: rosa.ropero@ual.es (R. F. Ropero), rrumi@ual.es (R. Rumí*), aguilera@ual.es (P. A. Aguilera)

# 1. Introduction 

Nature and society are clearly related and so any delimitation between natural and social systems is artificial and arbitrary (Berkes and Folke, 1998). Instead, they should be considered as a complex system of interactions operating on different scales; this is referred to as a Socio-Ecological System (SES) (Anderies et al., 2004; Cadenasso et al., 2006; Folke, 2006). In the context of SES, a systemic change can be defined as a fundamental change in the interactions within a system, arising either from an external hazard event or from gradual endogenous change, which leads to a shift in the state of the system to another with new properties (Kinzig et al., 2006; Filatova and Polhill, 2012).

Graphically the SES can be represented as a network of nodes (social and natural components), with a number of links between them. When a hazard event occurs or a component undergoes gradual change, the change can be propagated through the entire system by means of cause-effect interactions between the components of the SES. These types of interactions are subject to the uncertainty inherent in the system (Clark, 2002; Refsgaard et al., 2007). This uncertainty can be modelled using probability theory (Ricci et al., 2003; Walker et al., 2003; Refsgaard et al., 2007; Warmink et al., 2010).

Bayesian networks (BNs) are considered one of the most powerful tools for representing complex systems of causal interactions between variables that are subject to uncertainty (Borsuk et al., 2004; Jensen and Nielsen, 2007; Pourret et al., 2008; Korb and Nicholson, 2011; Carmona et al., 2013; Kelly et al., 2013; Landuyt et al., 2013; Nash et al., 2013). Their graphical structure allows stakeholders to understand the relationships easily. In addition, they provide stakeholders with a participatory framework because the learned model can be refined manually by adding or removing arcs (or even variables) from the graph to better represent reality (Voinov and Bousquet, 2010).

BNs models have already been successfully applied in environmental modelling (Aguilera et al., 2011; Kelly et al., 2013; Landuyt et al., 2013; Dyer et al., 2014). Whereas BNs usually estimate models using discrete domains, most environmental and social variables are continuous. A common solution is to discretise continuous variables, but this involves some loss of statistical information (Uusitalo, 2007). Estimation of a model directly from the original discrete and continuous (hybrid) data returns a more accurate model. In turn, this model is able to report more specific answers to the proposed scenarios. The main problem when dealing with hybrid BNs is that, initially,

there is no common structure to represent the distribution of the variables. The Mixtures of Truncated Exponentials (MTE) model (Moral et al., 2001) provides us with a common structure to represent both the discrete and continuous variables simultaneously, in such a way that all the computations needed to perform probability propagation in the model can be done using the same structure (Moral et al., 2001). The versatility of BNs allows any statistic of interest to be calculated from the variables, including the probability of extreme values.

Two of the main challenges in SES research (Filatova and Polhill, 2012) are: (i) to accommodate the study of systemic change while taking uncertainty into account (Clark, 2002), and (ii) to represent the new state of the system after systemic change has been propagated (Filatova and Polhill, 2012). Since BNs are modelled by means of probability distributions, risk and uncertainty can be estimated more accurately than by using models which only consider mean values (Uusitalo, 2007). They allow a system to be represented both in its current state (a priori), and a posteriori, once the change has been propagated through the system, using the probability distribution functions of the variables. Their main purpose is to provide a framework for efficient reasoning about the system they represent, in terms of updating information about unobserved variables, when new information (changes to a single or several observed variables) is incorporated to the system. This is known as probability propagation or probabilistic inference. However, not every change included into a component of the system (one or more variables) will lead to systemic change because some components may be conditionally independent. This property is expressed in the graph by means of the d-separation concept (see Section 2 for a more detailed explanation).

# 1.1. Outline of the paper 

Global socio-economic changes affect regional and local socio-economic structures (Lambin et al., 2001; Foley et al., 2005) and lead to changes in land uses in the landscape (Schmitz et al., 2005; Caillault et al., 2013) and in the structure and functionality of natural ecosystems (Matson et al., 1997; Foley et al., 2005; Rudel et al., 2009). One of the main effects of these changes relates to the behaviour of water flows (Scanlon et al., 2005; Maes et al., 2009; Toda et al., 2010; Park et al., 2014). The concepts of green and blue water flows were defined to introduce the whole water cycle into water management plans (Falkenmark, 1997; Rockstroem, 2000). Blue water is the

amount of rainfall that exceeds the soil's storage capacity and feeds rivers, lakes and aquifers. Green water refers to the rainfall that infiltrates into the root zone of the soil to support the primary productivity of natural and agricultural systems through evapotranspiration (Falkenmark, 1997; Falkenmark and Folke, 2002). Green and blue water flow through natural subsystems across the landscape, participating in several ecological processes; as a result, there is a clear interaction between land use and green and blue water flows (Willaarts et al., 2012). The characteristics of soil and the type and cover of vegetation determine the amount of water that evaporates back to the atmosphere, infiltrates into the soil or flows away as runoff (Falkenmark, 2003; Willaarts et al., 2012). For example, tropical forest and Mediterranean pasture have high green water flows, whilst urban land and irrigated herbaceous croplands have high blue water flows (Rockstroem and Gordon, 2001; Willaarts, 2009).

In this paper, we study a Spanish catchment as a SES. Three variables were selected to represent the socioeconomic subsystem while land use and green and blue water flows were selected to represent the natural subsystem.

The aim of the study is to demonstrate the ability of hybrid BNs to model systemic change. We develop a new methodology, which considers the tails of the probability distribution functions to identify systemic change, and we carry out statistical tests to differentiate between different states of the system. By this means, we provide the expert with a set of tools to help assess systemic change.

# 2. Methodology 

### 2.1. Study area

The study area comprises the catchment of the river Adra in south-eastern Spain (Figure 2). It is bounded to the north by the Sierra Nevada, to the south by the Mediterranean Sea, to the aast by the Sierra de Gádor, and to the west by the Sierra Filabres. It occupies 74.400 Ha , and supports an estimated population of 124.000 people distributed over fourteen municipalities.

The landscape of the Sierra Nevada mountain range is characterized by dense woodland, mainly oaks and conifers species with Mediterranean scrubland. In the upper reaches, the original Mediterranean forest with oaks remains, whilst the scrubland is the result of several episodes of deforestation (García-Latorre and Sánchez-Picón, 2001). The socioeconomy is characterized by several small municipalities accommodating and ageing population

![img-0.jpeg](img-0.jpeg)

Figure 1: Outline of the methodology divided into four different steps: i) data collection (explained in Section 2.2) ii) model learning, iii) evidence propagation, and iv) analysis of results (explained in Section 2.4). Statis.Inst., Statistical Institute; Env.Inf.Net., Environmental Information Network; Vars., Variables; Sub., Subsystem; Sig.Diff., significant difference in statistical test; Syst.Change., Systemic Change; Emig, emigration rates; Immig, immigration rates.

with a high rate of migration. In the foothills of Sierra Nevada, mixed and irrigated crops replace woodland and the social structure indicates a slightly younger population, though still with a high migration rates.

In the east of the area, in the Sierra de Gádor foothills, land uses comprise traditional croplands including olive and almond groves with patches of woodland and scrub, creating a complex and heterogeneous landscape. The socioeconomy is characterised by depopulation and an older population.

In the middle and west of the study area, the landscape is composed by scrubs and some patches of woodland whose configuration was determined by historical trends in the 19th century (mining and the deforestation of natural forest) (García-Latorre and Sánchez-Picón, 2001).

In the lower reaches, the land uses are intensive agriculture with greenhouses and irrigated crops, mixed with scrubland. Immigration rate is significant given the incoming of a new workforce to the greenhouses.

# 2.2. Data collection 

Taking into account socio-economic characteristics of the study area (CCA, 2007; Camarero et al., 2009), three representative variables (ageing, emigration and immigration rates) were selected. Data on these variables were obtained for each municipality from the Andalusian Statistical Institute (Figure $1 i$ i). The ageing component was summarised by calculating the percentage of people older than 65 years old, while emigration and immigration rates were calculated as percentages of the total population.

The BalanceMEd model (Willaarts, 2009; Willaarts et al., 2012) was applied to calculate the water flows described above (Figure 1 i)). This is a semi-deterministic model developed to quantify hydrological functioning in Mediterranean catchments using long time series of monthly rainfall and potential evapotranspiration data. The model assumes that a fraction from the total precipitation is intercepted by vegetation or soil and evaporates directly as a Non Productive Green Water (NPGW). Another fraction from the total precipitation can be intercepted on impermeable surfaces and is returned to the atmosphere as Consumptive Blue Water (CBW). The remaining precipitation reaches the soil and is taken up by plants and transpired, this portion is termed Productive Green Water flow (PGW). When the infiltrated water exceeds the soil storage capacity, it can either percolate or drain as Runoff Blue Water (RBW). In the specific case of greenhouse crops, we consider that the concept of PGW is not applicable since the crops are irrigated from

![img-1.jpeg](img-1.jpeg)

Figure 2: Study area. a) altitude, and b) land uses.

Table 1: Summary statistics of the continuous variables in the data set. PGW, Productive Green Water; NPGW, Non Productive Green Water; CBW, Consumptive Blue Water; RBW, Runoff Blue Water; SD, standard deviation.


groundwater flows rather than from direct precipitation. Moreover, evaporative flows are difficult to evaluate under a greenhouses cover. For that reason, in this specific case, we focus on CBW when considering greenhouse crops as the land use.

Nine land uses representative of the study area landscape were selected (Table 2). These data were obtained from the Land Use and Land Cover shape file from Andalusian Regional Government using ArcGis v.9.3.1 (ESRI, 2006) (Figure $1 i$ )). They are expressed as a discrete variable which represents the presence of each land uses as a percentage.

Table 2: Land uses selected and percentage of each one in the data set.


![img-2.jpeg](img-2.jpeg)

Figure 3: An example of a discrete Bayesian network with five binary variables ( $X_{1}, X_{2}$, $X_{3}, X_{4}$ and $X_{5}$ ). Note that $P\left(X_{i}=1 \mid \ldots\right)$ is not specified as it can directly be computed as $1-P\left(X_{i}=0 \mid \ldots\right)$. Although the arrow has a specific direction, it actually represents a two-way relationship between the variables.

Table 1 shows the main statistics of the continuous socioeconomic and water flow variables in the data set. The land use variable is discrete and the description of each category and its percentage in the data set are shown in Table 2.

# 2.3. Model description 

A BN is a statistical multivariate model for a set of variables $\mathbf{X}=$ $\left(X_{1}, \ldots, X_{n}\right)$, which is defined in terms of two parts (Jensen and Nielsen, 2007) ${ }^{1}$ :

1. Qualitative part: A directed acyclic graph (Fig. 3(a)) where each vertex represents a variable in the model and each edge, linking two variables, represents the statistical dependence between them. The graph represents the general structure of the model and allows the most relevant or irrelevant variables in the model to be identified without any numerical calculations. Moreover, it is helpful in enabling fluid communication between expert and non-expert (McDowell et al., 2009).
2. Quantitative part: A conditional probability distribution $p\left(x_{i} \mid p a\left(x_{i}\right)\right)$ for each variable $\left(X_{i}\right)$ given its parents $\left(p a\left(X_{i}\right)\right)$ in the graph. It indicates how strong the relationship between the variables shown in the
[^0]
[^0]:    ${ }^{1}$ Capital letters e.g. $X_{i}$ represent random variables, whilst lower case letter, e.g. $x_{i}$ represent values of the corresponding variables

![img-3.jpeg](img-3.jpeg)

Figure 4: Example of two variables $X$ and $Z$ d-separated by $Y$
graph is and models the joint probability distribution of the variables according to the following decomposition:

$$
p\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

The existence of conditional independencies in the graph, together with the above mentioned decomposition, allows the BNs to perform local computations, which means that they can deal with complex models (Getoor et al., 2004; Luo et al., 2005).

The ability of BNs to represent the independencies in the graph in a natural way makes them a highly appropriate tool to study systemic change. One of the main features of systemic change is that every change introduced into the system affects all the components (set of variables) involved in the system, rather than just some of them. This feature is difficult to model using more classical statistical tools; in contrast, the type of connections in the BN graph implicitly encodes this kind of situations. Not all inputs to the model would lead to a systemic change. Using the d-separation concept (Pearl, 1988) it is possible to select the variables that connect different parts of the graph, allowing the systemic change to propagate all through the network.

Figure 4 shows a simple example of the d-separation concept. In this situation, variables $X$ and $Z$ are d-separated by $Y$ i.e., $X$ and $Z$ are independent, if we do not know the exact value of $Y$, so an input in the model only for variable $X$ will not affect variable $Z$ (and viceversa) and so that input will not promote a systemic change. Fig 4 represents a very simple BN but the concept of d-separation is the same for larger BNs: given several parents for $X$ and $Z$ and children for $Y$ forming different components, then as long as $Y$ and its descendant are unknown, $X$ and $Z$ are independent, i.e., any change in $X$ or its parents is not propagated to $Y$ or its parents (For

more information see Pearl (1988) and Jensen and Nielsen (2007) Section 2.2.)

In the presence of continuous and discrete variables it is necessary a specific model able to deal simultaneously with these variables. Several approaches have been devised to deal with this problem. The Conditional Gaussian model (Lauritzen, 1992) was the first model developed, but it puts some restrictions on the network: (i) the joint distribution of the continuous variables has to follow a multivariate Gaussian, (ii) a discrete variable can not have a continuous parents. An alternative is the MTE model, which does not impose any restriction on the network. In the MTE model, the density functions for the continuous variables are expressed as piecewise functions with linear combination of exponentials in each piece. They were initially defined by Moral et al. (2001), and they are capable of dealing with different probability distributions due to their great fitting power (Cobb et al., 2006). For estimating the parameters of the model, we followed the approach of Moral et al. (2003) and Rumí et al. (2006), which is based on an iterative least squares algorithm. For more detailed explanations of this topic we refer the reader to Cobb et al. (2007); Langseth et al. (2009).

BN models based on the methodology proposed here have already been successfully applied in environmental modelling (Aguilera et al., 2010, 2013), as well as in other fields (Fernández et al., 2007; Cobb et al., 2013).

In this way, hybrid BNs have been shown to provide an excellent tool for studying interactions between social and natural subsystems from an uncertainty perspective (Ropero et al., 2014).

# 2.4. Model learning, evidence propagation and analysis of results 

In the model learning stage, the structure of the model is defined taking into account the theoretical background developed in Section 1.1 (Figure 1 ii)). Natural and social subsystems are connected through causal interactions, and land use is clearly influenced by the social subsystem (Lambin et al., 2001; Foley et al., 2005; Schmitz et al., 2005; Rudel et al., 2009; Ropero et al., 2014). Furthermore, the relationship between water flows and landscape are widely described in the literature (Scanlon et al., 2005; Maes et al., 2009; Toda et al., 2010). Figure 5 shows the qualitative part of the model. Estimation of the parameters of the model was carried out according to

![img-4.jpeg](img-4.jpeg)

Figure 5: Qualitative part of Hybrid BN. By their nature every variable except one (land use) were continuous. Emig, emigration rates; Immig, immigration rates; PGW, productive green water; NPGW, non productive green water; CBW, consumptive blue water; RBW, runoff blue water.

Section 2.3 using the Elvira ${ }^{2}$ software (Elvira-Consortium, 2002), which implements the algorithms to estimate the probability distributions and carries out the inference process.

After the model is learned, the next step is evidence propagation or inference (Figure 1 iii)). There are several methods that can be applied to obtain the results either exactly or approximately; in the case of complex models which cannot be solved in an exact way. In our case, we selected the ShenoyShafer algorithm (Shenoy and Shafer, 1990) which is able to deal with hybrid model and is specifically adapted to the MTE model (Rumí and Salmerón, 2007).

The evidence (new information) represents the change in one component of the SES which is propagated through the system, causing the systemic change (Figure 1 iii)). It was introduced into the land use component in order to simultaneously determining the influence on the social subsystem and the water flow component. The current state of the system, "a priori", reflects the probability in the case where no new information is added to the system. The evidence is introduced as the presence of one of the states of the land use variable. We selected two different endogenous changes: presence of traditional cropland and presence of greenhouses, which address both the land use trends that are observed in the study area.

Once the change is introduced into the model as evidence, we can take advantage of the versatility of BNs to obtain detailed results. The change

[^0]
[^0]:    ${ }^{2}$ This is a free software based on JAVA. It can be found in http://leo.ugr.es/elvira

alters the interactions in the model, leading to changes in the distribution of each variable. The distribution of the variables is then used to display the final result of the inference. The mathematical relationships that govern the interactions are expressed in a BN by means of conditional probability distributions, which are difficult to interpret. In contrast, the behaviour of the variables, both a priori and a posteriori is expressed through univariate probability distributions, which are much easier to interpret, especially for environmental systems.

For this reason, changes are commonly quantified in terms of the mean value of the variable. Sometimes, however, the mean value is not the most appropriate statistic to represent a probability distribution because it does not allow the overall behaviour of the variable to be tracked.

For a more comprehensive study of the results, we measured how the proposed changes are propagated to the water flow component and to the social subsystem, looking at the tail values of the probability distribution of each water flow and social variable as the means to defining the extent of the difference between the a priori and a posteriori distributions. In any probability distribution, the tails are highly relevant because they show the probability of the extreme values of the variable - in this case, the very high or very low water flows, and the very high or very low emigration and immigration rates and ageing. We first defined the threshold values of the tails since there are no references in the literature to identify what constitutes an extreme value. For this purpose, a k-means clustering (Anderberg, 1973; Jain et al., 1999) with 3 clusters was performed dividing the original data in three groups, according to their similarity. The first group was considered as the left tail, the second group as the centre of the distribution, and the third group as the right tail. Accordingly, the upper and lower thresholds were determined as the points that separated the first and the third cluster from the second. Once the thresholds were obtained, we computed the cumulative probability of both the left (lower) and right (upper) tails of all the water flow and social variables. As an example, Figure 6 shows the computation of these cumulative probabilities and the degree of change for a variable X in the a priori and a posteriori scenarios. Using the k-means clustering method, the left tail threshold was determined as $X<37$, and the right tail threshold was determined as $X>59$. Then the cumulative probability of the tails were computed, and we can see for example that $P(X>59)=0.34$ a priori, but it decreases to 0.13 a posteriori.

As pointed out in Aguilera et al. (2011), validation methods in BNs de-

pend on the aim of the model. When the aim is inference, as in this paper, appropriate validation methods are experts opinions or comparison with models that try to solve the same problem. In this case, there are no other models relating socioeconomic-land use and green and blue water flows in a SES framework. Therefore, validation by experts is considered to be the appropriate model. However, as a way of validating the conclusions drawn from the results obtained, we performed several goodness-of-fit tests. To determine whether there were significant differences between the variables $a$ priori and a posteriori (that is, between the different states of the system) we simulated a sample of size 1000 from each of the a priori and a posteriori probability distribution functions. Then we carried out a two-sided Kolmogorov-Smirnov test at a 0.05 level of significance. If significant differences are found between the system state a priori and a posteriori in both social and natural subsystems, the change introduced in the model can be considered as a systemic change (Figure 1 iv)).

# 3. Results 

Table 3 shows the mean and standard deviation values of the variables both in the current situation (a priori), and after the two land use changes are simulated (a posteriori). The tails of the distributions were also analyzed (the procedure is detailed in Section 2.4) as a part of the interpretation of the results. Table 4 shows the probability in the tails and Table 5 shows the p-values of the two-sided Kolmogorov-Smirnov tests. Figures 7, 8, and 9 show the probability distributions of social and water flow variables in the current situation, and under both land use change scenarios (a posteriori).

### 3.1. A priori

A priori shows the current situation without any change introduced in the system. The ageing variable has a mean value of $21.65 \%$, while emigration and immigration rates are $2.56 \%$ and $1.87 \%$, respectively (Table 3). Social variables are more probable in the left tail (Table 4, Figure 7).

Likewise, the probability of green water, (both productive and non productive), are more probable in upper values (Table 4, Figure 8), with mean values of 223.17 mm for PWG, and 123.04 mm for NPGW (Table 3). RBW has the same behaviour, with a mean value equal to 454.74 mm (Table 3),

![img-5.jpeg](img-5.jpeg)

Figure 6: An example of the probabilities of the left $(\mathrm{P}(X<37))$ tail, and the right $(\mathrm{P}(X>59))$ tail in variable X a priori, in black, and a posteriori, in red, and its mean values between brackets. As we can see, mean value decreases which indicates the shift of the distribution function to the left. Probabilities in the tails show us that the change of the function is much more intensive in the right tail than in the left.

Table 3: Mean and standard deviation (SD) values of water flow and social variables obtained from the (a priori and a posteriori) probability distribution. PGW, productive green water; NPGW, non productive green water; CBW, consumptive blue water; RBW, runoff blue water.


Table 4: Threshold of left and right tails, and probability values in the tails of water flow, and social variables for the current situation (a priori) and both land use changes (a posteriori). As an example, in the ageing variable, 0.39 a priori is the probability of having fewer than $19.08 \%$ of people older than 65 years old, while 0.17 is the probability of having more than $28.44 \%$ of people older than 65 years old. The thresholds in social variables are expressed as a percentage of the population; thresholds for water flows are in mm. PGW, Productive Green Water; NPGW, Non Productive Green Water; CBW, Consumptive Blue Water; RBW, Runoff Blue Water.


![img-6.jpeg](img-6.jpeg)

Figure 7: Probability distribution of social variables a priori and after both land use changes (a posteriori). The vertical black lines represent the threshold values of the tails of the variables. Note that probability functions are defined as a piecewise function using MTEs.

![img-7.jpeg](img-7.jpeg)

Figure 8: Probability distribution of green water flow variables a priori and after both land use changes (a posteriori). The vertical black lines represent the threshold values of the tails of the variables. Note that probability functions are defined as a piecewise function using MTEs.

![img-8.jpeg](img-8.jpeg)

Figure 9: Probability distribution of blue water flow variables a priori and after both land use changes (a posteriori). The vertical black lines represent the threshold values of the tails of the variables. Note that probability functions are defined as a piecewise function using MTEs

Table 5: P-values of Kolmogorov-Smirnov test among simulated values from a priori and a posteriori distribution functions. PGW, Productive Green Water; NPGW, Non Productive Green Water; CBW, Consumptive Blue Water; RBW, Runoff Blue Water. *The distribution functions are significantly different at a 0.05 level of significance.


and increased probabilities of falling into the right tail, 0.53 (Table 4, Figure 9). By contrast, CBW probabilities increase in the left tail, with 0.64 of probability (Table 4, Figure 9), and 209.32 mm mean value (Table 3).

In this state of the system, the population is ageing, and both emigration and immigration rates are low. The structure of the landscape determines that RBW and PGW are the main water flows.

# 3.2. Intensive Agriculture with Greenhouses 

This land use change involves the presence of crops grown under greenhouse cover in the catchment.

The ageing mean value decreases from $21.65 \%$ to $17.94 \%$ (Table 3). A look at probability values in the tail shows the change more clearly than the mean value. The decreasing trend in this variable is more noticeable when the tails of the distribution are studied- these indicate that there is little probability of a population with greater than $28 \%$ over 65 (in the left tail, probability decreased from 0.17 to close to zero (Table 4, Figure 7)). On the other hand, immigration mean value increases from $1.87 \%$ to $1.92 \%$ (Table 3 ). In this case, the probability values of the tails are also small (Table 4, Figure 7). Furthermore, both variables show significant differences between the a priori and the new scenario (Table 5). By contrast, as Figure 7 shows, emigration rates hardly changes (Table 3, and 4) which is confirmed by the two-sided Kolmogorov-Smirnov test (Table 5).

The means of all the water flow variables increase, in NPGW from 123.04

mm to 173.97 mm from 209.32 mm to 559.09 mm in CBW, and from 454.74 mm to 537.35 mm in RBW (Table 3). If only these mean values were taken into account, the behavior of blue and green water flows can be considered similar, since they both increase under this first scenario. However, there is a marked difference between the two when we consider the probabilities in the tails of the distribution. In the case of NPGW, the right tail probability increases from 0.45 to 0.72 (Table 4, Figure 8) which only emphasizes the $a$ priori behavior, i.e. higher water flows are more likely than lower ones.

But in CBW, a marked change in the trend is predicted. The probability of the left tail (extremely low flows) decreases from 0.64 to 0.049 ; while probability of right tail values (extremely high flows) increases from 0.21 to 0.67 .

Similarly, the mean RBW value increases from which one might expect an increase in the right tail probability, and a decrease in the left tail. However, the probability in both tails increases (Table 4 and Figure 9). This shows a peculiar behaviour in the variable, which means that both high and low extremes values of runoff become more probable than a priori, whilst the moderate values are less probable.

For NPGW, CBW and RBW, there are significant differences in the distribution functions a priori and under this scenario (Table 5).

# 3.3. Traditional Agriculture 

The land use change introduced into the SES is expressed as the greater presence of traditional croplands. Mean ageing and immigration hardly change, nor does their probability distributions with respect to the a priori situation (Tables 3 and 5, Figure 7). By contrast, the emigration variable shows a significant difference between the a priori and the new scenario, with slightly higher probabilities in the left tail (Table 4 and 5, Figure 7).

Both mean PGW and mean NPGW increase, from 223.17 mm to 284.39 mm , and from 123.04 mm to 151.85 mm respectively (Table 3 ).

For both variables, the mean indicates an increase, while a study of the tails provides additional information about whether the extremes of the distribution become more or less pronounced. As we can see in Table 4, the probability of high PGW in the right tail shifts from 0.24 to 0.70 while the mean shows a more moderate increase. This means that, under this second scenario, extremely high PGW flows are $46 \%$ more probable than a priori. In the same way, the NPGW left tail (the probability of extremely low NPGW)

decreases from 0.36 to 0.04 . However, the shift in the mean is proportionally less, from 123.04 mm to 151.85 mm .

The means of both CBW and RBW fall from 209.32 mm to 124.48 mm for CBW, and from 454.74 mm to 260.75 mm for RBW (Table 3). The probability of left tail of CBW (extremely low flows) also increases from 0.64 to 0.80 (Table 4). In this case, the tail values reinforce the trend described by the change in the mean, and the probability of extremely low values also increases.

In contrast, the RBW left tail probability increases from 0.15 to 0.50 , giving more information about the extent of the change in this variable (Table 4, Figure 9). In this case, the evidence introduced in the model implies the change in the tendency from an a priori situation where runoff was quite probable in higher values (probability of the right tail decrease from 0.53 to 0.20 ), to a situation in which lower values are more probable.

For these four water flow variables, there are significant differences between the a priori situation and this scenario (Table 5).

# 4. Discussion 

### 4.1. Case study results

Intensive greenhouse agriculture is one of the most important economic activities in the south-east of Spain, and it can impact both social and natural subsystems (IEC, 2004). In the study area, greenhouses are mainly located in the lower reaches, where population is characterized by a significant immigration rate. Under the first scenario of an increase in intensive agriculture, the incoming young population has the effect of reducing the extreme values of the ageing variable (i.e. the proportion of people over 65 falls). By contrast, emigration hardly changes (i.e., the departure of people looking for a job elsewhere is virtually unchanged). However, the behavior of the socioeconomic subsystems changes as a result of the intensification (García-Álvarez-Coque, 2002). These results concord with numerous studies made by different Spanish economic entities (García-Álvarez-Coque, 2002; IEC, 2004; CCA, 2007); which show that the agricultural intensification in the south-east of Andalusia has led to an increased influx of foreigners, mainly young people, to work in the greenhouses. This has reversed the trend of an increasingly ageing population, and has also led to an increase in the birth rate so changing the social structure of the area.

Vegetation cover around the greenhouses is often eliminated (to avoid invasion of pests into the greenhouses). As a result, the evaporation rates from the bare soil and plastic surfaces (greenhouses cover)-, described as NPGW and CBW, respectively- increase. As agriculture intensifies, NPGW becomes more important. However, while CBW in the a priori situation was low, the increase in greenhouse cover increases CBW quite significantly. In contrast, RBW has a peculiar behaviour, whereby both low and high extreme flows increase while moderate flows decreases.

The results demonstrate how water flows are modified when soil and natural vegetation cover are lost due to the introduction of plastic surfaces (greenhouses). The increase in evaporative losses reduces the water available for human and agricultural supply (thus, in semiarid regions such as this, efforts need to focuss on optimizing water use and minimizing water losses). Moreover, increase in runoff flows can alter soil structure due to increased erosion. Agricultural intensification leads to greater homogeneity in the landscape, and a loss of connectivity (the capability of the landscape to facilitate bio-physical flows), (Taylor et al., 1993), which implies poorer control of the nutrient and water cycle (De-Lucio-Fernández et al., 2003).

Agricultural intensification is a gradual trend that significantly modifies both natural and social subsystems, creating a new state in the system. Thus, it can be considered as a systemic change from the expert's point of view.

In our study area, traditional croplands comprise a mixture of woody rain-fed crops of olive, almond groves and grapevines with patches of herbaceous subsistence crops and natural vegetation managed in a traditional way. This heterogeneous pattern of traditional land use has been promoted as an alternative management system, which can bring economic and environmental benefits (Schmitz et al., 2005; Anderson et al., 2009). Such croplands are found mainly in the Sierra de Gádor foothills, which is a landscape characterized by an ageing population and depopulated municipalities.

The presence of traditional croplands does not imply a new incoming population, nor the emigration of young people and so neither ageing nor immigration change significantly from their a priori values. Although emigration changes (Table 5), it does not imply an alteration of the global behavior of the socioeconomic subsystem (CCA, 2007).

Given that traditional croplands are a mixture of woody and herbaceous crops and scrub, with areas of forest, the PGW is higher (Willaarts, 2009) because the evaporative demand of woody vegetation is higher than for herbaceous. Patches of scrubland and woodland, as well as the olive and almonds

groves increased, and imply an increase in the PGW flow. At the same time, these traditional systems, are characterized by an absence of bare solid, and a presence of herbaceous crops, which slightly increases NPGW (Rockstroem, 2000) and markedly decreases CBW. Agriculture heterogeneity involves a tighter control over RBW. The structure of this Mediterranean multifunctional rural landscape with its patchwork of different types of land use, together with the presence of mature ecosystems next to exploited plots, favours this control of runoff (De-Lucio-Fernández et al., 2003; Anderson et al., 2009).

In terms of whether an increase in traditional croplands can be described as a systemic change or not, we can say that systemic change can be defined as a fundamental change which involves a shift in the system state to another with new properties (Kinzig et al., 2006; Filatova and Polhill, 2012). The model indicates that this does not happen under this second scenario and so increasing traditional agriculture cannot be considered as a systemic change from this point of view.

# 4.2. Hybrid BNs and systemic change 

In order to assess modifications in the interactions between the different components of a SES, we will examine the variables one by one, because 1) any change in the interactions will lead to changes in the variables - which are easier to interpret and 2) in BNs, causal interactions between different components in an SES are modelled by conditional probability distribution functions (see Section 2.3), which are not conducive to an intuitive environmental interpretation. The versatility of BNs allows several statistics to be calculated from the results of the variables. In this case, mean values and the probability of the tails were calculated. Although mean values provide clear information about the behavior of the variables, the tails allow the extent of the changes to be assessed.

These results highlight that BNs are powerful tools for representing complexity and are able to deal with some of the challenges of SES modelling. In this way, important interactions among components are not omitted, and a balance between model complexity and computational time is achieved. Furthermore, using the hybrid approach instead of an approach that handles only discrete variables, means that, the model learning stage is carried out with all the statistical information contained in the data. Thus, the loss of information implied in the discretization process is avoided (Uusitalo, 2007; Aguilera et al., 2010, 2013). The qualitative part of the BNs allows the general structure of the systems to be defined along with the connections

between the different components of the model and their dynamics represented by probability distribution functions. Therefore, BNs are specifically designed to deal with complex systems under conditions of uncertainty.

In this respect, BNs manage uncertainty using probability theory: this is a well-founded theory and there are a wide range of algorithms and procedures, already developed and validated in the literature, which can be applied to parameter estimation and inference. In the specific case of SES modelling, the use of BNs contributes to uncertainty analysis in several ways: (i) in the representation of the independencies of the variables of the model which, by its nature, is intuitive in BNs, through the application of the d-separation concept, and (ii) by the different statistics calculated from the results (mean, standard deviation, tail probabilities, and goodness-of-fit test). Taken together, these make up a broad range of tools to aid the decision-making by experts regarding the uncertainty in the modelling of systemic change under the SES framework.

Thus, expert knowledge and machine learning techniques can be combined in different ways as an important part in SES modelling: both are capable of focussing on the most important components and can evaluate the model to improve it (Cyr et al., 2010; Haapasaari and Karjalainen, 2010; Voinov and Bousquet, 2010; Zorrilla et al., 2010). Modelling with the participation of experts and stakeholders has several advantages from a social, instrumental and methodological point of view (Voinov and Bousquet, 2010). Management decisions are usually more effective if all the social groups take part in the management process, sharing information and opinions, each being aware of their responsibilities and roles.

BNs are able to deal with probability propagation, since new information can been introduced into one or more components of the natural or social subsystems and the effects over the rest of the SES can be inferred. Therefore, the current situation and the new system state can be easily compared because the model results can be displayed together in a single graph showing changes in probability distribution (see Figures 7, 8, and 9). In summary, the probabilities are updated when new information is incorporated into the model and they can be analyzed to evaluate the systemic change in SESs.

Certain issues remain to addressed in the future, which could improve the application of BNs in SESs and systemic change modelling. Since environmental data is usually collected from neighbouring areas, spatial autocorrelation has to be taken into account in BNs (Cano et al., 2004; Tucker et al., 2005). Another consideration is how hybrid BNs could be used in a temporal

framework. Whilst some attempts to address this aspect can be found (Ihler et al., 2007; Moradkhani, 2008; Barillec and Cornford, 2009; Zhang et al., 2012) it is an aspect that requires further investigation. Sensitivity analysis would be a normal way to validate the estimation of the parameters in a BN. However, no sensitivity analysis algorithm has yet been developed for the MTE model. This would lead to a greater impact of this model in future applications.

# Acknowledgements 

This work has been supported by the Spanish Ministry of Economy and Competitiveness through project TIN2010-20900-C04-02, by Junta de Andalucía through projects P08-RNM-03945, P11-TIC-7821, and from ERDF funds. R. F. Ropero is supported by a FPU research grant, AP2012-2117 from the Spanish Ministry of Education, Culture and Sport. We are grateful to the four anonymous reviewers and the editors for their constructive and useful comments on the manuscript.
