# University of Wollongong 

## Research Online

Faculty of Science, Medicine and Health - Papers:
Faculty of Science, Medicine and Health
Part B

## Quantification of inter-regional differences in risk mitigation from prescribed burning across multiple management values

Brett Cirulis<br>University of Melbourne

Hamish Clarke
University of Wollongong, hamishc@uow.edu.au
Mathias M. Boer
Universty of Western Sydney, matthias.boer@uwa.edu.au
Trent D. Penman
University of Melbourne, tpenman@uow.edu.au
Owen F. Price
University of Wollongong, oprice@uow.edu.au
See next page for additional authors

## Publication Details

Cirulis, B., Clarke, H., Boer, M., Penman, T., Price, O. \& Bradstock, R. (2019). Quantification of inter-regional differences in risk mitigation from prescribed burning across multiple management values. International Journal of Wildland Fire, Online First 1-13.

[^0]
[^0]:    Research Online is the open access institutional repository for the University of Wollongong. For further information contact the UOW Library: research-pubs@uow.edu.au

# Quantification of inter-regional differences in risk mitigation from prescribed burning across multiple management values 


#### Abstract

Fire agencies are moving towards planning systems based on risk assessment; however, knowledge of the most effective way to quantify changes in risk to key values by application of prescribed fire is generally lacking. We present a quantification and inter-regional comparison of how risk to management values responds to variations in prescribed burning treatment rate. Fire simulations were run using the PHOENIX RapidFire fire behaviour simulator for two case study landscapes in interface zones in Tasmania and the Australian Capital Territory (ACT), Australia. A Bayesian network approach used these data to explore the influence of treatment and weather on risk from wildfire. Area burnt, length of powerline damaged and length of road damaged responded more strongly to treatment in the ACT than in Tasmania, whereas treatment mitigated house loss and life loss more strongly in Tasmania than the ACT. The effect of prescribed burning treatment rate on area burnt below minimum tolerable fire interval was similar in each case study landscape. Our study shows that the effectiveness of prescribed burning at mitigating area burnt by wildfire and other key values varies considerably across landscapes and values.


## Publication Details

Cirulis, B., Clarke, H., Boer, M., Penman, T., Price, O. \& Bradstock, R. (2019). Quantification of inter-regional differences in risk mitigation from prescribed burning across multiple management values. International Journal of Wildland Fire, Online First 1-13.

## Authors

Brett Cirulis, Hamish Clarke, Mathias M. Boer, Trent D. Penman, Owen F. Price, and Ross A. Bradstock

Quantification of inter-regional differences in risk mitigation from prescribed burning across multiple management values

Brett Cirulis ${ }^{1, a}$, Hamish Clarke ${ }^{2,3}$, Matthias Boer ${ }^{3}$, Trent Penman ${ }^{1}$, Owen Price ${ }^{2}$, Ross Bradstock ${ }^{2}$

5 ' School of Ecosystem and Forest Sciences, The University of Melbourne, Victoria 3363, Australia
$6{ }^{2}$ Centre for Environmental Risk Management of Bushfires, Centre for Sustainable Ecosystem
7 Solutions, University of Wollongong, NSW 2522, Australia
$8{ }^{3}$ Hawkesbury Institute for the Environment, Western Sydney University, Locked Bag
9 1797, Penrith, NSW 2751, Australia
10
${ }^{\text {a }}$ Corresponding author.

12 Brett Cirulis, Bushfire Behaviour and Management, The University of Melbourne, Water Street, 13 Creswick, 3363, Australia.

14 Ph. +61 402094 668, bcirulis@unimelb.edu.au

15

16 Key words

Wildfire, bushfire, wildland fire, trends, climate change

18

19 Suggested running head

20 Quantifying prescribed fire risk mitigation

# Abstract 

Fire agencies are moving toward planning systems based on risk assessment, however knowledge of the most effective way to quantify changes in risk to key values by application of prescribed fire is generally lacking. We present a quantification and inter-regional comparison of how risk to management values responds to variations in prescribed burning treatment rate. Fire simulations were run using the PHOENIX RapidFire fire behaviour simulator for two case study landscapes in interface zones in Tasmania and the Australian Capital Territory (ACT), Australia. A Bayesian Network approach used these data to explore the influence of treatment and weather on risk from wildfire. Area burnt, length of powerline damaged and length of road damaged responded more strongly to treatment in the ACT than in Tasmania, while treatment mitigated house loss and life loss more strongly in Tasmania than the ACT. The effect of prescribed burning treatment rate on area burnt below minimum tolerable fire interval was similar in each case study landscape. Our study shows that the effectiveness of prescribed burning at mitigating area burnt by wildfire and other key values varies considerably across landscapes and values.

## Summary for non-specialist

We use fire behaviour simulations and Bayesian Networks to estimate the risk mitigation effects of prescribed burning for area burnt, house loss, life loss, length of powerline and road damaged, and area burnt below minimum tolerable fire interval. Our methods can be used to quantify and compare risk across regions.

# 43 Introduction 

44 Fire management consists of a range of activities across the planning, response and recovery phases, which are undertaken to manage the economic, social and environmental risks from wildfire (Bradstock and Gill 2001; Gill et al. 2013). A pre-eminent priority of fire management is risk to life and property e.g. the 2018 Greece fires which at the time of writing resulted in the loss of 91 lives and damaged over 2,000 houses (Kantouris and Nellas 2018). Wildfires can also have impacts on mental health and community wellbeing (Jakes and Sturtevant 2013; Eisenman et al. 2015), infrastructure and economic productivity (Nielsen-Pincus et al. 2014) and a wide range of environmental values including biodiversity and soil, water and air quality (Bradstock 2008; Sawyer et al. 2017; Smith et al. 2011; Williamson et al. 2016).

Prescribed burning is used in fire management to reduce risks from wildfire by directly modifying fuel properties through the application of fire under moderate weather conditions (Penman et al. 2011a; Burrows and McCaw 2013). The effects of different types of prescribed burning strategies (e.g. spatial configurations, treatment rates) in altering wildfire characteristics such as area burned have been partially explored (Fernandes \& Botelho 2003; Boer et al. 2009; Price et al. 2015a, 2015b; Salis et al. 2018). However, further work is needed to quantify the differential effects of prescribed burning on risk reduction across a wide range of management values, given the diversity of values affected by wildfire and the potential for conflicting effects (e.g. asset protection and biodiversity conservation; Driscoll et al. 2010; Penman et al. 2011a). Quantification of interregional differences in prescribed burning effectiveness would support the efficient allocation of resources within and between regions.

Fire behaviour simulation models provide a methodology for investigating alternative prescribed burning strategies and other fire management decisions (Finney 2005; Cary et al. 2016). These simulators apply models of fire behaviour to environmental determinants such as vegetation type and condition, terrain and weather to estimate key fire properties such as intensity, rate of spread and flame height in a spatially explicit manner. These fire properties can then be used as input to

estimate risk to multiple management values (Ager et al. 2010; Thompson et al. 2011; Salis et al. 2013; Driscoll et al. 2016). By applying estimates of likelihood and cost to simulations, cost effectiveness of alternative management strategies can be compared and evaluated (Penman et al. 2014a; Thompson et al. 2015). Bayesian Networks (BNs) offer a probabilistic methodology for evaluating the sensitivity of risk and the benefits or costs of a given decision or strategy (Johnson et al. 2010; Kelly et al. 2013; Pollino et al. 2007).

While there have been diverse studies (e.g. King et al. 2006; Ager et al. 2010; Barros et al. 2017) that have used simulations to estimate changes in risk in response to differing strategies (i.e. variations in treatment rate and pattern), studies that systematically explore the way in which response of risk to treatment may vary across ecosystems are lacking. Such lack of knowledge is critical because policy and operational choices concerning the efficacy of treatment in risk mitigation need to account for biophysical and human context and its fundamental effects on fire regimes and risk. For example, King et al. (2013) showed that the response of number of wildfires and the area burned by them, to differing rates of prescribed burning, was estimated to differ substantially between arid and cool temperate ecosystems in Australia. Differing cities will have differing levels of exposure and vulnerability of people and property to wildfires according to legacies of development patterns and other biophysical constraints (Bradstock et al. 2012; Penman et al. 2014a; Alcasena et al. 2018). Thus, response of risk to treatment may be expected to differ considerably, due to such variations.

In this study we estimate how the effects of differing rates of treatment on risk are likely to vary in two peri-urban landscapes in south-eastern Australia. These case studies, situated on western edges of the small sized cities of Canberra and Hobart, exhibit both similarities and some differences that encapsulate much of the context for the risk mitigation and management problem in relatively densely populated urban centres across southern Australia. Both have experienced major wildfires in the last 50 years that have resulted in significant losses of lives and property (Fromm et al. 2006; Henley 2013; Hyde 2013). Both are situated adjacent to mountainous terrain, covered by fire-prone

eucalypt-dominated forest and woodlands. Both have also experienced varying degrees of population growth and urban expansion, though in this regard Canberra has grown more rapidly and recently (www.abs.gov.au, accessed 11 May 2018). Is there a common response of risk to treatment or do fundamentally different responses emerge as a function of differences in key human and environmental influences? The answer to this question will determine the extent to which novel solutions for risk mitigation via prescribed burning need to be derived to suit local context. We specifically tested the following hypotheses:

- the biophysical and human properties of fire-prone landscapes influence the effectiveness of prescribed burning at wildfire risk mitigation, resulting in regional differences in the response to treatment rate and
- the risk reduction afforded by a given prescribed burning rate differs between key management values.

107

108

109 Methods

110 Study area
111 Two case study landscapes were chosen in the ACT and Tasmania, both with a substantial Wildland Urban Interface (WUI) and history of large fires resulting in significant house loss. Both case study landscapes were approximately 200,000 ha, which corresponds with the upper end of the size distribution of wildfires in local ecosystems. The ACT case study landscape stretched from the capital Canberra in the east to the Brindabella Ranges in the west (Figure 1), with a population of approximately 420,000 (www.abs.gov.au, accessed 11 May 2018). The area contains a mixture of native forest, agricultural land and urban areas. Major vegetation types within forested areas are dry and wet sclerophyll forest, dominated by Eucalyptus spp., and in high altitude areas, subalpine woodland forest. Mean annual rainfall ranges from 615 mm at Canberra airport to 1051 mm at Mt

Ginini in the ranges to the south of the study area (www.bom.gov.au, accessed 11 May 2018). Mean summer daily maximum temperatures are $27.1^{\circ} \mathrm{C}$ at Canberra Airport and $19.2^{\circ} \mathrm{C}$ at Mt Ginini.

The Tasmania landscape was centred on the capital city, Hobart (Figure 1). As with the ACT landscape, the study area included a relatively small population (circa. 222,000 in the Greater Hobart Area; www.abs.gov.au, accessed 11 May 2018), forests and agricultural areas. Major vegetation types within forested areas are dry and wet sclerophyll forest. Mean annual rainfall ranges from 614 mm at Hobart to 897 mm at Mt Kunanyi in the Wellington Range to the west of Hobart (www.bom.gov.au, accessed 11 May 2018). Mean summer daily maximum temperatures are $21.3^{\circ} \mathrm{C}$ in Hobart and $12.8^{\circ} \mathrm{C}$ at Mt Kunanyi.

Both case study landscapes were part of the Eucalypt forest (temperate) fire regime niche, a relatively high productivity niche characterised by infrequent low-intensity litter fires in spring and medium-intensity shrub fires in spring and summer (Murphy et al. 2013). Typically fire intensity ranges from $1,000-5,000 \mathrm{~kW} \mathrm{~m}^{-1}$, although under extreme weather conditions crown fires can occur and fire intensity may reach 10,000-50,000 $\mathrm{kW} \mathrm{m}^{-1}$. Fires typically recur every 5-20 years, although the interval between fires can be as long as 20-100 years (Murphy et al. 2013). From 2009 to 2014 an annual average of $1.85 \%$ of the ACT was treated with prescribed burning (ACT Government 2014). In Tasmania between the 2008-2009 and 2012-2013 fire seasons, prescribed fire was applied to an average of $0.66 \%$ of treatable land, ranging from $0.29 \%$ to $1.58 \%$ (Richards et al. 2014).

Fire behaviour simulations

The effect of prescribed fire fuel treatment scenarios on future fire behaviour was examined using the fire characterisation and fire spread simulator PHOENIX RapidFire v4.0.0.7 (hereafter PHOENIX; Tolhurst et al. 2008). PHOENIX was selected as it used operationally by agencies in all the states of eastern and southern Australia (Bentley and Penman 2017). Huygens' propagation

principle of fire edge (Knight and Coleman 1993) is used in PHOENIX to simulate two dimensional fire growth over complex landscapes. Rate of spread is calculated by one of two fire behaviour models - a modified McArthur Mk5 forest fire behaviour model (McArthur 1967; Noble et al. 1980) and a generalisation of the CSIRO southern grassland fire spread model (Cheney et al. 1998).

PHOENIX uses a range of other modules including fuel accumulation models to account for varying fuel loads with increasing time since fire based on fuel type, wind modification based on topographic variation based on the Wind Ninja program (www.firemodels.org/index.php/windninja-introduction, accessed November 2011) and fire spotting (via ember propagation, spread and spotfire ignition; Saeedian et al. 2010). We refer readers to Tolhurst et al. (2008) for more details on the model structure. A 30 m resolution digital elevation model was included to allow PHOENIX to account for the influence of topography on fire behaviour. Fuel accumulation models for major vegetation types of the case study landscape were provided by the relevant agencies in both ACT and Tasmania; ACT Parks and Conservation and the NSW Rural Fire Service for the ACT study region and the Department of Primary Industries, Parks, Water and Environment (DPIPWE) for the Tasmania study region. Disruptions to fuels through streams and roads were represented by the estimated width on a 30 m raster and were also provided by the relevant agencies. All simulations were run using 180 m resolution grid cells to optimise model performance based on the recommendations by Tolhurst et al. (2008). PHOENIX was run in 'batch' mode with a modified output format that included the following metrics for each cell within each fire: ember density, convection, intensity and flame length.

Model input data

A series of daily weather datasets was selected from Automatic Weather Station (AWS) records based on the Forest Fire Danger Index (FFDI) from 1994 to 2015; these datasets represent the

distribution in regional weather conditions affecting fire behavior in the case study areas. We used the Hobart AWS station (Bureau of Meteorology (BOM) site no. 94929) for the Tasmanian simulations and the Tuggeranong AWS station (BOM site no. 070339) for the ACT simulations. FFDI is a composite measure that combines temperature, relative humidity and wind speed with a long term drying index to predict the difficulty of fire suppression (McArthur 1967; Noble et al. 1980). Five of the six FFDI categories have been recorded in each case study landscape (LowModerate, High, Very High, Severe, Extreme). To capture variability in weather, three weather types were selected within each of these categories based on the predominant FFDI driver - i) strong wind, ii) strong wind with a significant directional change or iii) high air temperature. Up to three different days were chosen for each of these FFDI drivers, which when combined with available observations within each FFDI category resulted in 34 weather dates for the ACT case study landscape and 26 for the Tasmania landscape. Each weather stream contained hourly data for air temperature, relative humidity, wind speed, wind direction, drought factor and curing. All weather streams covered a 24 -hour period beginning from midnight to allow the model to generate stable and realistic estimates of fuel moisture based on temperature and relative humidity (Tolhurst et al. 2008).

Fuel loads were varied to represent a range of past fuel management scenarios. PHOENIX estimates fuel loads using separate fuel accumulation curves for combined surface/near surface, elevated and bark fuels (Hines et al. 2010). These curves use a negative exponential growth function and vary between vegetation types (Watson 2011). To capture the effect of varying prescribed fire treatment rates in the landscape, a series of prescribed burning treatments were simulated over a period of 20 years (Penman et al. 2014a). The influence of wildfire on fuel loads was simulated by selecting a subset of actual wildfire sizes for a period of 30 years at a rate equivalent to the historical observed wildfire incidence rate in the case study landscapes (Bradstock et al. 2014). The treatable portion of each case study landscape was separated into management sized 'burn blocks'. These burn blocks were a combination of historic prescribed fire boundaries and future planned burns. In the ACT

study region, the data were provided by ACT Parks and Conservation and the NSW Office of Environment and Heritage (on behalf of ACT Parks and Conservation). In the Tasmania study region, the data were provided by DPIPWE. A selection routine incorporating wildfire history, treatment percentage ( $0,1,2,3,5$ and 10 percent) and minimum burn intervals was then applied to the burn blocks iteratively over 20 a year period. For burn blocks classified as edge, a minimum burn interval of 5 years was used as it reflects what is feasible to achieve by the agencies whilst still allowing fuels to recover sufficiently. For landscape blocks, the minimum burn interval is the minimum tolerable fire interval for the majority of the vegetation type within each block. This process was replicated 5 times to give a total of 30 simulated fire history layers for each case study landscape to be incorporated into the PHOENIX simulations.

Ignition locations were selected using a probabilistic approach. Ten thousand random points were generated within each study area. An ignition probability was calculated for each point based on an empirical model developed for similar forest types (Penman et al. 2015). In the model, ignition probability is a function of environmental factors (such as topography and productivity) and built environment factors (such as housing density and distance to the nearest road). From the 10,000 random points, 1,000 ignition points with the highest ignition probabilities were selected for use in the simulations. Individual fires were ignited at 11am and propagated for 12 hours, unless selfextinguished within this period. To minimise ignition location bias and reduce total simulation time, the 1,000 ignition points were randomly split into 5 groups of 200 ignitions. Each of these 200 ignitions was simulated for a single replicate of each weather category/driver combination ( $\mathrm{n}=14$ for ACT, $\mathrm{n}=11$ for Tasmania) and fuel treatment ( $\mathrm{n}=6$ ), resulting in 98,000 fires in the ACT case study landscape and 77,000 fires in the Tasmania case study landscape.

Area burnt was a direct output from the fire behaviour simulations. Effectiveness of prescribed burning at mitigating wildfire impacts was assessed on five values: house loss, loss of human life, length of powerline damaged, length of road damaged and area burnt below minimum tolerable fire interval (TFI). TFI is an ecological measure used in conservation management that considers the amount of time between fires required for native vegetation to reproduce such that vegetation diversity can be maintained (Department of Environment and Sustainability 2012). Area burnt below TFI was calculated from area burnt and existing TFI mapping supplied by the management agencies, and impacts on other values were calculated using loss functions. The probability of house loss was calculated as a function of ember density, flame length and convection as presented in (Tolhurst and Chong 2011). House loss was calculated per 180 m cell and then multiplied by the number of houses in that cell to estimate the number of houses lost per fire. House locations were derived from authoritative national location data (PSMA 2016). Statistical loss of human life was based on house loss (using the house loss function), the number of houses exposed (using simulation output) and the number of people exposed to fire (Harris et al. 2012). Mesh block data from the Australian Bureau of Statistics was used to calculate the average number of people per household in each block. These data were then combined with the house location dataset to give the total number of people exposed to fire. Due to a lack of empirical data regarding the risk of damage to roads and powerlines, we used a simple threshold of $10,000 \mathrm{~kW} / \mathrm{m}$ to determine if roads or powerlines within each 180 m cell were considered damaged by fire. The effects of fire are largely associated with infrastructure such as signs and road closures, rather than damage to the road surface itself. Locations of roads and powerlines were provided by ACT Parks, Tasmanian Department of Primary industries, Parks, Water and Environment and Conservation and the NSW Rural Fire Service.

BNs are directed acyclic graphs with variables represented by nodes and the directional relationships between the nodes represented by arrows. In the BN developed for this study, two primary node types were used; stochastic nodes and decision nodes. Stochastic nodes are random variables represented by a conditional probability table which contain the join probability distributions for the variable (Korb and Nocholson 2011). Decision nodes represent discrete decisions that can be made by users and when used in a BN, these are refered to as Bayesian Decision Networks (BDNs). The probability distributions and associated uncertainty for the stochastic nodes, together with the selected discrete values of the decision nodes, are propagated throughout the network and outputs are presented as likelihoods.

In this study, a BDN was used to evaluate prescribed burning effectiveness in mitigating risk. Broadly we followed the recommended methods for developing Bayesian Networks of Marcot et al. (2006) and Chen and Pollino (2012). The primary steps used were to construct a conceptual model of the problem, develop influence diagrams to depict the relationships of the conceptual model and finally populate all the conditional probability tables within the model. A simple conceptual model (Figure 2) was developed based on previous BN studies of fire management (Penman et al. 2011b; Penman et al 2014b). In the model, fire weather and fire management affect the distribution of fire sizes. Fire weather, fire size and fire management then all affect the extent of loss for a value of interest. The conceptual model was then used to create the influence diagram which included the full set of management decisions and values (Figure 3).

Data for the conditional probability tables (CPTs) in the Bayesian Network were derived from the simulation study for the case study landscapes. Data generated in the fire simulations were used to estimate the probability distributions in the CPTs for each of the fire size and value impact nodes. At each node continuous data were discretised on a log scale across the range of values in an iterative fashion to get a relatively even distribution across the non-zero values. Fire weather in the model was quantified using FFDI. For each FFDI category, we calculated the average maximum daily FFDI across the average fire season for the study area using data from the same weather

stations used to run PHOENIX. These values were then classified into fire days and days without fire, where a fire day was defined as a day on which fire was recorded within a 200 km radius of the weather station. The proportional distribution of fire days in each of the five categories of FFDI was then used in the Bayesian Network.

The Bayesian Network was used to estimate the risk to each value at each treatment level from the simulation-derived distributions of data. The resultant risks provide a basis for comparison between regions that explicitly incorporates the observed frequency of fire weather conditions in each case study landscape. Risk values were the expected node likelihoods for area burnt, house loss, life loss, length of powerline damaged, length of road damaged and area burnt below TFI for each of the six prescribed burning treatment rates. Risk values were also estimated in relation to expected node likelihoods with no treatment, to allow for comparison of the relative change in risk at different prescribed burning treatment rates across both case study landscapes.

# Results 

Impact estimation

Unplanned fires were considerably larger in the Tasmania case study landscape than in the ACT case study landscape (Figure 4; see Supplementary Material for similar plots for each management value). Although each landscape had a large range of area burnt for any given FFDI category and treatment rate, maximum area burnt integrated across all weather categories was 1.5-2.1 times bigger in Tasmania than in the ACT, depending on the treatment rate (Tables 1 and 2). The magnitude of differences was greater for mean area burnt (2.7-5.9 times bigger in Tasmania) and greater still for median area burnt (14.7-24 times bigger in Tasmania). Mean and maximum house loss was greater in Tasmania than ACT, but median house loss results were low (0-2) in each landscape. Median life loss (0) and mean life loss (1-4) were also similar in each landscape, but maximum life loss was considerably greater in the ACT up to 5\% treatment rates, but higher in

Tasmania (149 lives lost) than the ACT (35 lives lost) at 10% treatment rates. For length of powerline damaged, length of road damaged and area burnt below minimum TFI, mean and maximum impacts were much higher in Tasmania than the ACT. Overall, area burnt declined with increasing treatment rate. However, in both landscapes, easing fire weather conditions by a single FFDI category usually resulted in a greater reduction in median, 3rd quartile and maximum area burnt than increasing the treatment rate from 0 to 10% (Figure 4). As with area burnt, there was a decrease in house loss, life loss and length of powerline and road damaged as treatment increased, while area burnt below minimum TFI increased with increasing treatment rate.

### Risk estimation

The effect of increasing treatment rate was preserved after adjusting for the relative frequency of fire weather conditions in each landscape i.e. the risk of substantial area burnt and significant house loss, life loss and length of road and powerline damaged declined with increasing rate of treatment, whereas increased treatment resulted in greater areas burnt below minimum TFI (Figure 5). Risks were uniformly greater in Tasmania than in the ACT, regardless of value or treatment rate. With no treatment, expected area burnt was 669 ha in Tasmania and 54 ha in the ACT. This decreased to 539 ha and 25 ha respectively at a treatment rate of 10%. As treatment rate increased from 0 to 10% in Tasmania, expected house loss declined from 4.4 to 2.3 and expected life loss declined from 0.8 to 0.6. Risk of house loss and life loss were almost constant across all treatment levels in the ACT (about 0.2), however prescribed burning effects were apparent when relative risk was examined (see below). Expected length of powerline damaged in Tasmania decreased from 434 m to 297 m as treatment increased from 0 to 10%. The equivalent figures for expected length of road damaged were 7.6 km and 5.4 km. In the ACT, expected lengths of powerline and road damaged with no treatment (44 m and 605 m respectively) were substantially larger than at the maximum treatment rate of 10% (26 m and 285 m respectively). In both landscapes, increasing treatment from 0 to 10%

led to steady increases in expected area burnt below minimum TFI, with the exception of an increase from $5 \%$ to $10 \%$ in treatment rate the ACT, which resulted in a slight decline from 5.6 ha to 5.5 ha.

Prescribed burning led to much greater relative reductions in area burnt in the ACT (12-54\%) than in Tasmania (2-19\%; Figure 6). There were also greater relative reductions in risk in the ACT for length of powerline damaged (13-41\%) and length of road damaged (11-53\%) compared to Tasmania (4-32\% and 5-29\% respectively). At up to 5\% treatment rates, the relative effect of prescribed burning on area burnt below TFI was greater in the ACT (7-14\% increases) than in Tasmania (2-9\% increases), but at a treatment level of $10 \%$ this trend reversed, with a relative increase in risk in Tasmania of $14 \%$ and in the ACT of $12 \%$. In contrast, at all treatment rates there was a greater relative reduction in the risk of house loss (9-49\%) and life loss (8-24\%) in Tasmania than in the ACT (4-24\% and 4-18\% respectively). It was generally not possible to achieve a 50\% reduction in risk in either case study landscape. Exceptions were area burnt (54\%) and length of road damaged (53\%) in the ACT at 10\% treatment rates, while house loss in Tasmania was almost halved ( $49 \%$ reduction) at $10 \%$ treatment rates.

# Discussion 

Relationships between prescribed burning treatment rates, area burnt and risk reduction supported our hypotheses and largely conformed to previous findings (King et al. 2006; Bradstock et al. 2012). Prescribed burning led to a reduction in area burnt and risk of asset loss, but an increase in area burnt below minimum TFI. Weather, however, had a consistently greater effect than prescribed burning on area burnt and related risks, also in line with previous simulation studies (Cary et al. 2009; Penman et al. 2013) and empirical studies (Price and Bradstock 2010; 2012 and others). Furlaud et al.'s (2017) findings that implementable treatment plans (corresponding to our treatment rates of 1-5\%) would only have a small effect on fire extent across Tasmania, are comparable to our

findings of relatively low reduction in area burnt from prescribed burning in the State's south-east. However, while Furlaud et al. (2017) did not investigate house loss, we found that the risk for this value could be halved at $10 \%$ treatment rates. Bradstock et al. (2012) found that treatment rates of $7-10 \%$ were required to in order to halve risk to people and property in Sydney, a region whose vegetation and climate more closely resembles the ACT than Tasmania. Penman et al. (2014) found that halving the risk of high intensity fires reaching houses in Sydney was possible at rates of $10 \%$ if treatment was exclusively in the WUI, but that the same rate of treatment, when confined to landscape burns, achieved a reduction of just $19 \%$. We found that in the ACT reductions in risk of $50 \%$ or more were possible for area burnt and length of road damaged, but that house loss and life loss did not respond as strongly to a maximum treatment rate of $10 \%$. However, in our simulations treatment was distributed across both landscape and interface zones. Possibly, higher levels of risk reduction to assets within the WUI in this landscape could be achieved if treatments were concentrated near the interface (Penman et al. 2013; Kennedy and Johnson 2014). Importantly, current treatment rates in both landscapes are well below $5 \%$ and a treatment rate of $10 \%$ is not currently likely to be achievable due to various constraints such as budgets, resource limitations and available days suitable for prescribed burning (e.g. Clarke et al. (in press)). Overall, the effectiveness of prescribed burning at mitigating area burnt by wildfire and other key values varied considerably across landscapes and values: i.e. a given rate of prescribed burning did not deliver the same degree of risk mitigation for all values, and the results differed between study landscapes.

Although the Tasmania and ACT case study landscapes share many similarities in fire regime, climate and vegetation type, there are considerable differences in the risk profiles. These may be driven by variations in fuel load, terrain, fuel accumulation and asset arrangement in the landscape. The proportion of forest in ACT and Tasmania is similar ( $48 \%$ and 54\%; ESCAVI 2003), but the mean proportion of forest in ACT census blocks ( $1.6 \%$ ) is considerably lower in than in Tasmania (17\%) (Australian Bureau of Statistics, 2011 Census). Populated areas are thus around ten times more forested in Tasmania than in the ACT. Overall fire size showed little response to treatment

level in the Tasmanian case study landscape but a strong response in the ACT landscape. This contrasted with the house loss results, where Tasmania showed a strong response to prescribed burning. A possible explanation for this is that the house loss metric factors in fire intensity, convection and ember attack. Given the terrain, forest type and proximity of housing to vegetation in the Tasmania case study landscape, house loss there may be more driven by flame contact, radiant heat and short-range spotting (Cruz et al. 2012) than in the ACT landscape. This is supported by the fact that values with intensity-driven loss functions like length of powerline and road damaged showed very similar responses to treatment level as area burnt in both the ACT and Tasmania. These results demonstrate the importance of considering the interplay between multiple fire properties and the arrangement of assets throughout the landscape, rather than simpler measures such fire presence/absence and fire intensity.

The effect of treatment level on the ecological value of area burnt below minimum TFI was consistent between case study areas but unlike the other values, increases with treatment percentage. The reason for this is that although the prescribed burning selection routine was constrained to not burn below the minimum TFI, increased treatment places more of the landscape at risk of being burnt by the next wildfire before the minimum TFI. The simulation results reflect this in both the ACT and Tasmania case study landscapes up to treatment rates of 3\%. However, beyond $3 \%$ in both landscapes, the effect of prescribed burning is dampened by the fact that wildfire size is also decreasing, thus burning less area below minimum TFI. In the ACT case study landscape, it is evident from the area burnt results that wildfire size is reduced sufficiently to result in a decrease in area burnt below minimum TFI under 5\% and 10\% treatment rates. The response of this indicator of ecological values provides a basis for understanding trade-offs between management objectives such as biodiversity conservation and reduction of risk to life and property (e.g. Bentley and Penman 2017).

Whilst the simulation methodology was consistently applied to both case study landscapes, a number of caveats and limitations apply to both our study design and the PHOENIX RapidFire

simulator. There are a range of additional management strategies to reduce wildfire risk that we did not consider, such as manual fuel removal, suppression, fuel breaks, asset construction characteristics and general community preparedness. Although some of these strategies can be simulated in PHOENIX, their current implementation within the simulator does not accurately address the complexities of real world situations (Penman et al. 2013). Nevertheless, one study found that increasing fuel treatment led to only marginal increases in containment success due to suppression (Penman et al. 2013). Although rapid gains continue to be made in the development of simulations (Duff et al. 2018), the primary focus of this study was to analyse the effect of fuel treatment on wildfire risk. The prescribed burning assignment routine, although based on actual management burn blocks, operated randomly within edge and landscape zones. While random assignment of fire treatment has been shown to decrease fire size in past studies (Bradstock et al. 2012; Price et al. 2015), other studies have shown that management decisions and the application of prescribed burning close to assets can further reduce the risk to assets (Finney 2001; Finney et al. 2007; Bentley and Penman 2017; Penman et al. 2014b). Fuel load within each burn block in this study was also considered to be reset to its lowest value in PHOENIX for surface, elevated and bark fuels. In reality, prescribed burning is performed in mild fire weather resulting in a mosaic of fire severity within each burn block, which will yield varying post-fire fuel properties, fire behaviour and impacts (Penman et al. 2007; Loschiavo et al. 2017; McCarthy et al. 2017). Furthermore, post fire fuel accumulation within PHOENIX is assumed to be follow an Olson curve (Olson 1963), i.e. a negative exponential growth equation. Although surface fuel accumulation can be reliably represented by an Olson curve, the suitability of an Olson curve for elevated and bark fuels is largly untested (e.g. Duff et al. 2012; Dalgleish et al. 2015). Further, although state agencies have invested in developing curves specifically for local vegetation types (e.g. Watson 2011), it is not clear how consistent these estimates are between case study landscapes.

The risk trade-offs presented here reflect the methodologies used for estimation of impacts: life and property loss, length of powerline and road damaged, and area burnt below TFI. Overall risk

estimates should therefore be interpreted in light of known or potential weaknesses in these models, such as the use of a single fire intensity threshold alone to determine the length of powerline and road damaged or knowledge gaps concerning tolerable fire intervals. However, the use of loss functions to characterise wildfire impacts on various values is essentially modular, allowing for their revision or replacement as improvements and alternatives become available. The methodology also allows for the introduction of new values (e.g. other environmental and health values) as loss functions are developed. Integration over the entire distribution of fire weather likelihood at a given location provides a better estimate of risk than methods limited to specific fire weather categories (e.g. Ager et al. 2010; Salis et al. 2016; Furlaud et al. 2017; Alcasena et al. 2018), but our method still allows for the interrogation of these results along those lines. Weather inputs can be adjusted to reflect new observations or projected changes in fire weather conditions due to climate change (Clarke and Evans 2018).

We have developed a methodology for quantifying risk as a function of prescribed burning. The method incorporates inherent differences between landscapes in weather, fuel, asset arrangement and ignition patterns, and a Bayesian Network to that provides a quantitative basis for assessing risks to multiple management values. These features allow for formal comparisons between both landscapes and values. While we have applied this methodology to two fire-prone case study landscapes, future studies could expand this to a more comprehensive selection of fire-prone areas in Australia and elsewhere, exploring the influence of variation in climate, population and land use on prescribed burning effectiveness. Such a systematic investigation could explore the reasons why risk does not always respond linearly to prescribed burning and why there may be diminishing returns in response to increasing treatment rates. Further studies could also utilise the Bayesian Network framework to incorporate information about economic costs and climate change impacts and investigate trade-offs between different management options (Driscoll et al. 2016).

# Acknowledgements 

451 This research was partly financially supported by the Bushfire and Natural Hazards Cooperative Research Centre. Thank you to the Tasmanian Fire Service, the NSW Rural Fire Service and the ACT Parks and Conservation Service for providing data. The authors declare no conflicts of interest.

Figure captions

Figure 1 Study area location. Fire behaviour simulations were carried out for two case study landscapes in south-eastern Australia, Tasmania (left) and the Australian Capital Territory (ACT; right).

Figure 2 Conceptual model for the analysis of fire management decisions, used to formulate influence diagrams for Bayesian Network model of risk mitigation from prescribed burning.

Figure 3 Example influence diagram for Bayesian Network model of risk mitigation from prescribed burning. Data is for the Tasmania case study landscape with no treatment.

Figure 4 Fire behaviour simulation output for area burnt in ACT (top) and Tasmania (bottom) case study landscapes. Each panel shows the distribution of area burnt at different treatment rates within a given fire weather category. Each category includes FFDI values driven primarily by temperature, wind speed and wind direction change. For all boxplots, lower and upper whiskers span the 95\% interval, lower and upper hinges show first and third quartile, central line shows median and notch shows $95 \%$ confidence interval of median. Similar plots for each management value are shown in Supplementary Figures 1-10.

Figure 5 Influence of prescribed burning and weather on risk for area burnt and five key management values in the ACT (cross) and Tasmania (circle) case study landscapes. For each treatment level, the Bayesian Network incorporates all weather streams and adjusts impacts to reflect the proportional distribution of fire days within the five fire weather categories in each case study landscape.

Figure 6 Influence of prescribed burning and weather on relative risk for area burnt and five key management values in the ACT (cross) and Tasmania (circle) case study landscapes. For each treatment level, the Bayesian Network incorporates all weather streams and adjusts impacts to reflect the proportional distribution of fire days within the five fire weather categories in each case study landscape. Relative risk is defined as the change in risk due to treatment, with a value of 1 representing no treatment. Note the Y axis scale is different for area burnt below TFI.

# Supplementary material 

Supplementary Figure 1 Impact estimation for house loss in Tasmania case study landscape. Each panel shows the distribution of house loss at different treatment rates within a given fire weather category. Each category includes FFDI values driven primarily by temperature, wind speed and wind direction change.

Supplementary Figure 2. As for Supp Fig 1, but for life loss.

Supplementary Figure 3. As for Supp Fig 1, but for length of powerline damaged.

Supplementary Figure 4. As for Supp Fig 1, but for length of road damaged.

Supplementary Figure 5. As for Supp Fig 1, but for area burnt below minimum tolerable fire interval (TFI).

494 Supplementary Figure 6. Impact estimation for house loss in ACT case study landscape. Each panel
495 shows the distribution of house loss at different treatment rates within a given fire weather category.
496 Each category includes FFDI values driven primarily by temperature, wind speed and wind
497 direction change.

498 Supplementary Figure 7. As for Supp Fig 6, but for life loss.

499 Supplementary Figure 8. As for Supp Fig 6, but for length of powerline damaged.

500 Supplementary Figure 9. As for Supp Fig 6, but for length of road damaged.

501 Supplementary Figure 10. As for Supp Fig 6, but for area burnt below minimum tolerable fire
502 interval (TFI).

506 Ager AA, Vaillant NM, Finney MA (2010) A comparison of landscape fuel treatment strategies to mitigate wildland fire risk in the urban interface and preserve old forest structure. Forest Ecology and Management 259, 1556-1570.

509 Ager AA, Evers CR, Day MA, Preisler HK, Barros AM, Nielsen-Pincus M (2017) Network analysis of wildfire transmission and implications for risk governance. PLoS One 12, e0172867.

511 Alcasena FJ, Ager AA, Salis M, Day MA, Vega-Garcia C (2018) Optimizing prescribed fire allocation for managing fire risk in central Catalonia. Science of the Total Environment 621, 872885 .

514 Aponte C, Tolhurst KG, Bennett LT (2014) Repeated prescribed fires decrease stocks and change attributes of coarse woody debris in a temperate eucalypt forest. Ecological Applications 24, 976516989 .

517 ACT Government (2014) The ACT strategic bushfire management plan 2014-2019. Canberra, Australia: Emergency Services Agency.

519 Barros AMG, Ager AA, Day MA, Preisler HK, Spies TA, White E, Pabst R, Olsen KA, Platt E, Bailey JD, Bolte JP (2017). Spatiotemporal dynamics of simulated wildfire, forest management, and forest succession in central Oregon, USA. Ecology and Society 22(1), 24. https://doi.org/10.5751/ES-08917-220124

523 Bentley PD, Penman TD (2017) Is there an inherent conflict in managing fire for people and conservation. International Journal of Wildland Fire 26, 455-468.

525 Boer MM, Sadler RJ, McCaw L, Grierson PF (2009) Long-term impacts of prescribed burning on regional extent and incidence of wildfires: evidence from 50 years of active fire management in SW Australian forests. Forest Ecology and Management 259, 132-142.

528 Bowman DMJ, Balch J, Artaxo P, Bond WJ, Cochrane MA, D’Antonio CM, DeFries R, Johnston FH, Keeley JE, Krawchuk MA, Kull CA, Mack M, Moritz MA, Pyne S, Roos CI, Scott AC, Sodhi NS \& Swetnam TW (2011) The human dimension of fire regimes on Earth. Journal of Biogeography 38, 2223-2236.

532 Bradstock RA (2008) Effects of large fires on biodiversity in south-eastern Australia: disaster or template for diversity? International Journal of Wildland Fire, 17, 809-822.

534 Bradstock RA \& Gill AM (2001) Living with fire and biodiversity at the urban edge: in search of a sustainable solution to the human protection problem in southern Australia. Journal of Mediterranean Ecology 2, 179-195.

537 Bradstock RA, Cary GJ, Davies I, Lindenmayer DB, Price OF, Williams RJ (2012) Wildfires, fuel treatment and risk mitigation in Australian eucalypt forests: insights from landscape-scale simulation. Journal of Environmental Management 105, 66-75. doi:10.1016/J.JENVMAN.2012.03.050

541 Bradstock R, Penman T, Boer M, Price O, Clarke H (2014) Divergent responses of fire to recent warming and drying across south-eastern Australia. Global Change Biology 20, 1412-1428.

543 Burrows N, McCaw L (2013) Prescribed burning in southwestern Australia. Frontiers in Ecology and the Environment 11, e25-e34. doi:10.1890/120356

545 Calkin DC, Finney MA, Ager AA, Thompson MP, Gebert KM (2011) Progress towards and barriers to implementation of a risk framework for US federal wildland fire policy and decision making. Forest Policy and Economics 13, 378-389. doi:10.1016/J.FORPOL.2011.02.007

548 Cary GJ, Flannigan MD, Keane RE, Bradstock RA, Davies ID, Lenihan JM, Li C, Logan KA, Parsons RA (2009) Relative importance of fuel management, ignition management and weather for area burned: Evidence from five landscape-fire-succession models. International Journal of Wildland Fire 18, 147-156.

Cary GJ, Davies ID, Bradstock RA, Keane RE, Flannigan MD (2016) Importance of fuel treatment for limiting moderate-to-high intensity fire: findings from comparative fire modelling. Landscape Ecology 32,1473-1483.

Chen SH, Pollino CA (2012) Good practice in Bayesian network modelling. Environmental Modelling \& Software 37, 134-145.

Cheney N, Gould J, Catchpole WR (1998) Prediction of fire spread in grasslands. International Journal of Wildland Fire 8, 1-13.

Chong D, Tolhurst K, Duff T (2012) PHOENIX RapidFire 4.0 Convection and Ember Dispersal Model. In 'Bushfire CRC'. (Melbourne, http://www.bushfirecrc.com/sites/default/files/phoenix 4 convection and spotting.pdf)

Clarke H, Tran B, Boer MM, Price O, Kenny B, Bradstock R (in press) Climate change effects on the frequency, seasonality and interannual variability of suitable prescribed burning weather conditions in south-eastern Australia. Agricultural and Forest Meteorology.

Cruz MG, Sullivan AL, Gould JS, Sims NC, Bannister AJ, Hollis JJ, Hurley RJ (2012) Anatomy of a catastrophic wildfire: the Black Saturday Kilmore East fire in Victoria, Australia. Forest Ecology and Management 284, 269-285.

Dalgleish SA, van Etten EJB, Stock WD, Knuckey C (2015) Fuel dynamics and vegetation recovery after fire in semiarid Australian shrubland. International Journal of Wildland Fire 24, 613623 .

Department of Sustainability and Environment (2012). Code of practice for bushfire management on public land. Melbourne, Australia: Victorian Government.

573 Driscoll DA, Lindenmayer DB, Bennett AF, Bode M, Bradstock RA, et al. (2010) Resolving
574 conflicts in fire management using decision theory: asset protection versus biodiversity
575 conservation. Conservation Letters 3, 215-223.

576 Driscoll DA, Bode M, Bradstock RA, Keith DA, Penman TD, Price OF (2016) Resolving future
577 fire management conflicts using multicriteria decision making. Conservation Biology 30, 196-205.
578 doi:10.1111/COBI. 12580

579 Duff TJ, Bell TL, York A (2012) Predicting continuous variation in forest fuel load using
580 biophysical models: a case study in south-eastern Australia. International Journal of Wildland Fire
$581 \quad 22,318-332$.

582 Duff TJ, Cawson JG, Cirulis B, Nyman P, Sheridan GY, Tolhurst KG (2018) Conditional
583 performance evaluation: using wildfire observations for systematic fire simulator development.
584 Forests 9, 189. doi:10.3390/f9040189

585 Eisenman D, McCaffrey S, Donatello I, Marshal G (2015) An ecosystems and vulnerable
586 populations perspective on solastalgia and psychological distress after a wildfire. EcoHealth 12,
$587 \quad 602-610$.

588 ESCAVI (2003) Australian vegetation attribute manual: national vegetation information system,
589 version 6.0. Executive Steering Committee for Australian Vegetation Information, Department of
590 the Environment and Heritage, Canberra.

591 Fernandes PM, Botelho HS (2003) A review of prescribed burning effectiveness in fire hazard
592 reduction. International Journal of Wildland Fire 12, 117. doi:10.1071/WF02042

593 Finney MA (2005) The challenge of quantitative risk analysis for wildland fire. Forest Ecology and
594 Management 211, 97-108. doi:10.1016/J.FORECO.2005.02.010

Finney MA, Seli RC, McHugh CW, Ager AA, Bahro B, Agee JK (2007) Simulation of long-term landscape-level fuel treatment effects on large wildfires. International Journal of Wildland Fire 16, $712-727$.

Fromm M, Tupper A, Rosenfeld D, Severanckx R, McRae R (2006) Violent pyro-cumulonimbus storm devastates Australia's capital and pollutes the stratosphere. Geophysical Research Letters 33, L05815. doi:10.1029/2005GL025161

Furlaud JM, Williamson GJ, Bowman DMJS (2017) Simulating the effectiveness of prescribed burning at altering wildfire behaviour in Tasmania, Australia. International Journal of Wildland Fire 27, 15-28. https://doi.org/10.1071/WF17061

Gill AM, Stephens SL, Cary GJ (2013) The worldwide "wildfire" problem. Ecological Applications 23, 438-454. doi:10.1890/10-2213.1

Harris S, Anderson W, Kilinc M and Fogarty L (2012) The relationship between fire behaviour measures and community loss: an exploratory analysis for developing a bushfire severity scale. Natural Hazards 63, 391-415.

Henley J (2013) Firestorm. In 'The Guardian', 26 May 2013. (Eds F Panetta, J Richards, M Khalili) Available at https://www.theguardian.com/world/interactive/2013/may/26/firestorm-bushfire-dunalley-holmesfamily [Verified 26 July 2018]

Hines F, Tolhurst KG, Wilson AAG, and McCarthy GJ (2010) Overall fuel hazard assessment guide. Fourth edition. Department of Sustainability and Environment, Melbourne, Victoria, Australia. Available at https://www.ffm.vic.gov.au/ data/assets/pdf file/0005/21110/Report-82-overall-fuel-assess-guide-4th-ed.pdf [Verified 26 July 2018]

Holland GJ, Clarke MF, Bennett AF (2017) Prescribed burning consumes key forest structural components: implications for landscape heterogeneity. Ecological Applications 27(3), 845-858.

618 Hyde M (2013) 2013 Tasmanian bushfires inquiry: Volume One. (Department of Premier and
619 Cabinet: Hobart, Tas., Australia) Available at
620 http://www.dpac.tas.gov.au/__data/assets/pdf_file/0015/208131/1.Tasmanian_Bushfires_Inquiry_R eport.pdf [Verified 26 July 2018]

622 Jakes PJ, Sturtevant V (2013) Trial by fire: Community Wildfire Protection Plans put to the test.
623 International Journal of Wildland Fire 22, 1134-1143.

624 Johnson S, Mengersen K, de Waal A, Marnewick K, Cilliers D, Houser AM, Boast L (2010)
625 Modelling cheetah relocation success in southern Africa using an Iterative Bayesian Network
626 Development Cycle. Ecological Modelling 221, 641-651.

627 Kantouris C, Nellas D (2018) Death toll from Greek wildfire reaches 91 as village grieves.
628 Associated Press News. Available at
629 https://apnews.com/e4391bcaefda4cf0901cbd3be3f89847/Death-toll-from-Greek-wildfire-reaches-
630 91-as-village-grieves [Verified 6 August 2018]

631 Kelly RA, Jakeman AJ, et al. (2013) Selecting among five common modelling approaches for
632 integrated environmental assessment and management. Environmental Modelling \& Software 47, $159-181$.

634 Kennedy MC, Johnson MC (2014) Fuel treatment prescriptions alter spatial patterns of fire severity around the wildland-urban interface during the Wallow Fire, Arizona, USA. Forest Ecology and Management 318, 122-132.

637 King KJ, Cary GJ, Bradstock RA, Chapman J, Pyrke A, Marsden-Smedley JB (2006) Simulation of prescribed burning strategies in south-west Tasmania, Australia: effects on unplanned fires, fire regimes, and ecological management values. International Journal ofWildland Fire 15, 527-540. doi:10.1071/WF05076

641 King KJ, Cary GJ, Bradstock RA, Marsden-Smedley JB (2013) Contrasting fire responses to climate and management: insights from two Australian ecosystems. Global Change Biology 19, $1223-1235$.

644 Knight I, Coleman J (1993) A fire perimeter expansion algorithm-based on Huygens wavelet propagation. International Journal of Wildland Fire 3, 73-84.

646 Krawchuk MA, Moritz MA, Parisien M-A, van Dorn J, Hayhoe K (2009). Global pyrogeography: The current and future distribution of wildfire. PLoS ONE 4, e5102.

648 Loschiavo J, Cirulis B, Zuo Y, Hradsky BA, Di Stefano J (2017) Mapping prescribed fire severity in south-east Australian eucalypt forests using modelling and satellite imagery: a case study. International Journal of Wildland Fire 6, 491-497.

651 Maindonald, J. H. (2011), Bayesian Artificial Intelligence, Second Edition by Kevin B. Korb, Ann E. Nicholson. International Statistical Review, 79: 497-497. doi:10.1111/j.1751$5823.2011 .00159 \_18 . x$

654 Marcot BG, Steventon JD, Sutherland GD, McCann RK (2006) Guidelines for developing and updating Bayesian belief networs applied to ecological modeling and conservation. Canadian Journal of Forest Research 36, 3063-3074.

657 McArthur AG (1967) Fire behaviour in eucalypt forests, Leaflet No. 107. In. (Forestry and Timber Bureau: Canberra)

659 McCarthy G, Moon K, Smith L (2017) Mapping fire severity and fire extent in forest in Victoria for ecological and fuel outcomes. Ecological Management and Restoration 18, 54-65.

661 Murphy BP, Bradstock RA, Boer MM, Carter J, Cary GJ, Cochrane MA, Fensham RJ, RussellSmith J, Williamson GJ, Bowman DMJS (2013) Fire regimes of Australia: a pyrogeographic model system. Journal of Biogeography 40, 1048-1058.

Nielsen-Pincus M, Moseley C, Gebert K (2014) Job growth and loss across sectors and time in Western US: the impact of large wildfires. Forest Policy and Economics 38, 199-206.

Noble I, Gill A, Bary G (1980) McArthur's fire-danger meters expressed as equations. Australian Journal of Ecology 5, 201-203.

Olson JS (1963) Energy storage and the balance of producers and decomposers in ecological systems. Ecology 44, 322-331.

Penman TD, Kavanagh RP, Binns DL, Melick DR (2007) Patchiness of prescribed burns in dry sclerophyll eucalypt forests in South-eastern Australia. Forest Ecology and Management 252, 2467232 .

Penman TD, Christie FJ, Andersen AN, Bradstock RA, Cary GJ, Henderson MK, Price O, Tran C, Wardle GM, Williams RJ, York A (2011a) Prescribed burning: how can it work to conserve the things we value? International Journal of Wildland Fire 20, 721-733. doi:10.1071/WF09131

Penman TD, Price O, Bradstock RA (2011b) Bayes Nets as a method for analysing the influence of management actions in fire planning. International Journal of Wildland Fire 20, 909-920.

Penman TD, Collins L, Price OF, Bradstock RA, Metcalf S, Chong DMO (2013) Examining the relative effects of fire weather, suppression and fuel treatment on fire behaviour - A simulation study. Journal of Environmental Management 131, 325-333.

Penman TD, Bradstock RA, Price OF (2014a) Reducing wildfire risk to urban developments: Simulation of cost-effective fuel treatment solutions in south eastern Australia. Environmental Modelling and Software 52, 166-175.

Penman TD, Collins L, Syphard AD, Keeley JE, Bradstock RA (2014b) Influence of Fuels, Weather and the Built Environment on the Exposure of Property to Wildfire. PLoS ONE 9(10), e111414. doi:10.1371/journal.pone. 0111414

687 Penman TD, Parkins KA, Mascaro S, Chong D, Bradstock RA (2015) National fire danger rating system probabilistic framework project, Final report year three. In. (Bushfire and Natural Hazards CRC: Canberra)

690 Pollino CA, Woodberry O, Nicholson A, Korb K, Hart BT (2007) Parameterisation and evaluation of a Bayesian network for use in an ecological risk assessment. Environmental Modelling and Software 22(8), 1140e1152.

693 Price OF, Penman TD, Bradstock RA, Boer MM, Clarke H (2015a) Biogeographical variation in the potential effectiveness of prescribed fire in south-eastern Australia. Journal of Biogeography 42, 2234-2245. doi:10.1111/JBI. 12579

696 Price OF, Pausas JG, Govender N, Flannigan M, Fernandes PM, Brooks ML, Bird RB (2015b) Global patterns in fire leverage: the response of annual area burnt to previous fire. International Journal of Wildland Fire 24, 210-297. (doi:10.1071/WF14034Global)

699 Price OF, Horsey B, Jiang N (2016) Local and regional smoke impacts from prescribed fires Natural Hazards and Earth System Sciences Discussion 16, 2247.

701 PSMA (Public Sector Mapping Agencies) (2016). Geocoded National Address File Database. Available at https://www.psma.com.au/products/g-naf [Verified 21 January 2019].

703 Richards R, Ferguson S, Cornish K, Whight S, Williamson G (2014) Bushfire in Tasmania: a new approach to reducing our statewide relative risk. (State Fire Management Council Unit, Tasmania Fire Service: Hobart, Tas., Australia) Available at http://www.sfmc.tas.gov.au/sites/sfmc.tas.gov.au/files/Bushfire_In_Tasmania\%20V1.2\%20pdf\%20 web\%20version_0_0.pdf [Verified 26 July 2018]

708 Saeedian P, Moran B, Tolhurst K, Halgamuge MN (2010) Prediction of high-risk areas in wildland fires. In 'Information and Automation for Sustainability (ICIAFs), 2010 5th International Conference on' pp. 399-403. (IEEE)

711 Salis M, Ager AA, Arca B, Finney MA, Bacciu V, Duce P, Spano D (2013) Assessing exposure of human and ecological values to wildfire in Sardinia, Italy. International Journal of Wildland Fire $22,549-565$. doi:10.1071/WF11060

714 Salis M, Laconi M, Ager AA, Alcasena FJ, Arca B, Lozano O, Fernandes de Oliveira A, Spano D (2016) Evaluating alternative fuel treatment strategies to reduce wildfire losses in a Mediterranean area. Forest Ecology and Management 368, 207-221. doi:10.1016/J.FORECO.2016.03.009

717 Salis M, Del Giudice L, Arca B, Ager AA, Alcasena-Urdiroz F, Lozano O, Bacciu V, Spano D, 718 Duce P (2018). Modeling the effects of different fuel treatment mosaics on wildfire spread and behavior in a Mediterranean agro-pastoral area. Journal of Environmental Management 212, 490505. doi:10.1016/j.jenvman.2018.02.020

721 Sawyer R, Bradstock R, Bedward M, Morrison RJ (2018) Soil carbon in Australian fire-prone forests determined by climate more than fire regimes. Science of the Total Environment 639, 526537 .

724 Smith HG, Sheridan GJ, Lane PNJ, Nyman P, Haydon S (2011) Wildfire effects on water quality in forest catchments: A review with implications for water supply. Journal of Hydrology 396, 170726192 .

727 Spies TA, White E, Ager A, Kline JD, Bolte JP, Platt EK, Olsen KA, Pabst RJ, Barros AMG, Bailey JD, Charnley S, Morzillo AT, Koch J, Steen-Adams MM, Singleton PH, Sulzman J, Schwartz C, Csuti B (2017) Using an agent-based model to examine forest management outcomes in a fire-prone landscape in Oregon, USA. Ecology and Society 22(1), 25. https://doi.org/10.5751/ES-08841-220125

732 Thompson MP, Calkin DE, Gilbertson-Day JW, AgerAA (2011) Advancing effects analysis for integrated, large-scale wildfire risk assessment. Environmental Monitoring and Assessment 179, 217-239. doi:10.1007/S10661-010-1731-X

735 Thompson, M. Anderson, N (2015). Modeling fuel treatment impacts on fire suppression cost savings: A review. California Agriculture 69, 164-170.

737 Tolhurst K, Shields B, Chong D (2008) PHOENIX: development and application of a bushfire riskmanagement tool. Australian Journal of Emergency Management 23, 47-54.

739 Tolhurst KG, Chong DM (2011) Assessing potential house losses using PHOENIX RapidFire. In 'Proceedings of Bushfire CRC \& AFAC 2011 Conference Science Day', 1 September 2011, Sydney, NSW, Australia. (Ed. RP Thornton) pp. 74-76. (Bushfire Cooperative Research Centre: Sydney, NSW, Australia) Available at
http://www.bushfirecrc.com/sites/default/files/managed/resource/74-
86_assessing_potential_house_losses.pdf

745 Watson PJ (2011) Fuel load dynamics in NSW vegetation. Part 1: forests and grassy woodlands. Report to the NSW Rural Fire Service. Centre for Environmental Risk Management of Bushfires, University of Wollongong, NSW, Australia.

748 Williamson G, Bowman DMJS, Price OF, Henderson SB, Johnston FH (2016) A transdisciplinary approach to understanding the health effects of wildfire and prescribed fire smoke regimes. Environmental Research Letters 11, 125009.

![img-0.jpeg](img-0.jpeg)

Figure 1 Study area location. Fire behaviour simulations were carried out for two case study landscapes in south-eastern Australia, Tasmania (left) and the Australian Capital Territory (ACT; right).

![img-1.jpeg](img-1.jpeg)

760 Figure 2 Conceptual model for the analysis of fire management decisions, used to formulate influence diagrams for Bayesian Network model of risk mitigation from prescribed burning.
![img-2.jpeg](img-2.jpeg)

763

764 Figure 3 Example influence diagram for Bayesian Network model of risk mitigation from prescribed burning. Data is for the Tasmania case study landscape with no treatment.

![img-3.jpeg](img-3.jpeg)

Figure 4 Fire behaviour simulation output for area burnt in ACT (top) and Tasmania (bottom) case study landscapes. Each panel shows the distribution of area burnt at different treatment rates within a given fire weather category. Each category includes FFDI values driven primarily by temperature, wind speed and wind direction change. For all boxplots, lower and upper whiskers span the 95\% interval, lower and upper hinges show first and third quartile, central line shows median and notch shows $95 \%$ confidence interval of median. Similar plots for each management value are shown in Supplementary Figures 1-10.

![img-4.jpeg](img-4.jpeg)

777

778 Figure 5 Influence of prescribed burning and weather on risk for area burnt and five key management values in the ACT (cross) and Tasmania (circle) case study landscapes. For each treatment level, the Bayesian Network incorporates all weather streams and adjusts impacts to reflect the proportional distribution of fire days within the five fire weather categories in each case study landscape.

![img-5.jpeg](img-5.jpeg)

Figure 6 Influence of prescribed burning and weather on relative risk for area burnt and five key management values in the ACT (cross) and Tasmania (circle) case study landscapes. For each treatment level, the Bayesian Network incorporates all weather streams and adjusts impacts to reflect the proportional distribution of fire days within the five fire weather categories in each case study landscape. Relative risk is defined as the change in risk due to treatment, with a value of 1 representing no treatment. Note the Y axis scale is different for area burnt below TFI.

793
794
795
796
797

Table 1
Summary of the distributions of area burnt and estimated impacts on management values from fire behaviour simulations for the ACT case study landscape (prior to Bayesian Network analysis). Data is summarised across all weather scenarios.


Table 2
Summary of the distributions of area burnt and estimated impacts on management values from fire behaviour simulations for the Tasmania case study landscape (prior to Bayesian Network analysis).


# 802