# A decision support tool for risk-benefit analysis of Japanese encephalitis vaccine in travellers 

## Running title: Japanese encephalitis vaccine risk-benefit tool

Colleen L Lau ${ }^{1,2 *}$ MBBS, PhD; Deborah J Mills ${ }^{2 *}$ MBBS MPHTM; Helen Mayfield ${ }^{1}$ PhD; Narayan Gyawali ${ }^{3}$ PhD; Brian Johnson ${ }^{3}$ PhD; Hongen Lu ${ }^{1}$ PhD; Kasim Allel ${ }^{4}$ MSc; Philip N Britton ${ }^{5,6}$ PhD; Weiping Ling ${ }^{7}$ MPH; Tina Moghaddam ${ }^{8}$ BE(Hons)/BSc; Luis Furuya-Kanamori ${ }^{1}$ PhD

[^0]
[^0]:    ${ }^{1}$ School of Public Health, Faculty of Medicine, The University of Queensland, Herston, Australia
    ${ }^{2}$ Dr Deb The Travel Doctor, Travel Medicine Alliance, Brisbane, Australia
    ${ }^{3}$ Mosquito Control Laboratory, QIMR Berghofer Medical Research Institute, Herston, Australia
    ${ }^{4}$ Department of Disease Control, London School of Hygiene and Tropical Medicine, London, UK
    ${ }^{5}$ Department of Infectious Diseases and Microbiology, Children's Hospital Westmead, Westmead, Australia
    ${ }^{6}$ Child and Adolescent Health and Sydney ID, Sydney Medical School, University of Sydney, Sydney, Australia
    ${ }^{7}$ UQ Centre for Clinical Research, Faculty of Medicine, The University of Queensland, Herston, Australia
    ${ }^{8}$ School of Information Technology and Electrical Engineering, Faculty of Science, The University of Queensland, St Lucia, Australia

    * The authors contributed equally to this manuscript

    Corresponding author:
    Dr Luis Furuya-Kanamori
    A: 288 Herston Road, The University of Queensland, Herston QLD 4006, Australia
    E: l.furuya@uq.edu.au

    Preliminary results of the study were presented at the $18^{\text {th }}$ Conference of the International Society of Travel Medicine, Basel, Switzerland (May 21-25, 2023).

#### Abstract

Background: During pre-travel consultations, clinicians and travellers face the challenge of weighing the risks versus benefits of Japanese encephalitis (JE) vaccination due to the high cost of the vaccine, relative low incidence in travellers ( $\sim 1$ in one million), but potentially severe consequences ( $\sim 30 \%$ case-fatality rate). Personalised JE risk assessment based on the travellers' demographics and travel itinerary is challenging using standard risk matrices. Therefore, we developed an interactive digital tool to estimate risks of JE infection and severe health outcomes under different scenarios to facilitate shared decision making between clinicians and travellers.


Methods: A Bayesian network (conditional probability) model risk-benefit analysis of JE vaccine in travellers was developed. The model considers travellers' characteristics (age, sex, comorbidities), itinerary (destination, departure date, duration, setting of planned activities), and vaccination status to estimate the risks of JE infection, development of symptomatic disease (meningitis, encephalitis), clinical outcomes (hospital admission, chronic neurological complications, death), and adverse events following immunisation.

Results: In low-risk travellers (e.g., to urban areas for $<1$ month), the risk of developing JE and dying is low ( $<1$ per million) irrespective of the destination; thus, the potential impact of JE vaccination in reducing the risk of clinical outcomes is limited. In high-risk travellers (e.g., to rural areas in high JE incidence destination for $>2$ months), risk of developing symptomatic disease and mortality is estimated as 9.5 and 1.4 per million, respectively. JE vaccination in this group would significantly reduce the risk of symptomatic disease and mortality (by $\sim 80 \%$ ) to 1.9 and 0.3 per million, respectively.

Conclusion: The JE tool may assist decision-making by travellers and clinicians and could increase JE vaccine uptake. The tool will be updated as additional evidence becomes available. Future work needs to evaluate the usability of the tool. The interactive, scenario-based, personalised JE vaccine risk-benefit tool is freely available on www.VaxiCal.com.

Keywords: Bayesian, immunization, pre-departure, travel, vaccine hesitancy

# Introduction 

Japanese encephalitis (JE) virus is endemic in Asia and is the leading cause of viral encephalitis in the region, causing approximately 100,000 cases and 25,000 deaths annually. ${ }^{1}$ The chance of US travellers to Asia contracting JE has been estimated to be $<1$ per million travellers annually. ${ }^{2,3}$ This figure is often used in pre-travel risk assessment; however, Connor et al. have questioned its accuracy and usefulness. ${ }^{3}$ The inaccuracy of both the numerator (i.e., due to underreporting and/or challenges in diagnosis ${ }^{5}$ ) and the denominator (i.e., the number of travellers to JE endemic regions) used to generate estimates of risk may result in considerable imprecision. Furthermore, the quoted risk is an estimate for all travellers to Asia, but risk assessments should be personalised based on the travellers' age, comorbidities, destination, season and duration of the trip, and planned travel activities.

Effective JE vaccines with low risk of local and systemic adverse events following immunisation (AEFI) have become available in recent years. ${ }^{5,6}$ Despite this, clinicians in the USA do not offer the vaccine to the majority of higher-risk travellers. ${ }^{7}$ In another study in Australia, it was found that even when JE vaccines were offered, uptake by travellers remained low $(<30 \%) .{ }^{9}$ Vaccine cost (e.g., AUD 300-350 in Australia for a dose of Imojev [chimeric live attenuated vaccine], USD 600-700 in the USA for two doses of Ixiaro [Vero cell-derived inactivated vaccine], EUR 200-300 in Europe for two doses of Ixiaro) and perception of low risk of the disease have been cited as the main reasons for the low JE vaccine uptake. ${ }^{10}$ While there is ongoing work to reduce chimeric JE vaccine costs for travellers through the use of intradermal fractional dosing, ${ }^{10-12}$ there is also a need to better assess and communicate personalised risks to travellers. ${ }^{13}$

Given the relatively low incidence of JE in travellers, ${ }^{2}$ but potentially severe consequences of the disease (e.g., $30 \%$ case-fatality rate ${ }^{15}$ and $30-40 \%$ severe neurological sequalae in symptomatic patients ${ }^{16}$ ) for which there is no specific treatment, it is difficult for

both clinicians and travellers to weigh the risks and benefits of JE vaccination. Doing so requires estimating the probability of a traveller being bitten by a JE virus (JEV)-infected mosquito based on travel destination, season, duration, and location (e.g., rural or urban), followed by the probability of developing a symptomatic form of the disease (i.e., encephalitis or meningitis; 1 in 250 JEV infected travellers ${ }^{16}$ ), followed by the likelihood of dying ( 1 in 3 symptomatic patients ${ }^{15}$ ) or progressing to severe neurological complications ( 1 in 2.5 symptomatic patients ${ }^{16}$ ), which would be a very challenging task during pre-travel consultation using standard risk matrices.

This challenge can be addressed using conditional probability models, such as Bayesian networks, ${ }^{18}$ to provide risk estimates under different scenarios, and for model outputs to be linked to an interactive digital tool to enable better communication of the risks (i.e., AEFI) versus benefits (i.e., reduction in risk of JE infection and complications) of immunisation to the users. Bayesian networks are a flexible modelling framework that has been successfully used to incorporate multiple sources of evidence on the risks and benefits of immunisation. ${ }^{18,19}$ Therefore, we aimed to develop a Bayesian network model for risk-benefit analysis of JE vaccines in travellers, and to use the model outputs to drive an online interactive, scenariobased, personalised JE vaccine decision support tool to effectively communicate the risks and benefits to travellers.

# Methods 

No primary data were used for this study; only data extracted from published articles and aggregated publicly available data (e.g., Global Health Observatory data repository) were utilised. The project was reviewed by The University of Queensland Research Ethics and Integrity office (2022/HE000927) and was deemed to be exempt from ethics review under the National Statement on Ethical Conduct in Human Research.

# Model design 

Bayesian networks are conditional probability models composed of a directed acyclic graph, which provide visual representation of the assumptions and relationships between and among variables in a causal structure. ${ }^{22}$ The variables in the graphs are represented by nodes (each with several possible states [e.g., male/female, age groups]), which are connected by edges (arrows) to represent the direction of the relationship between the nodes. A path is an unbroken sequence of nodes connected by edges, and kindship terms are used to represent the relationships within a path. The ancestor or parent nodes are the input variables (e.g., traveller's characteristics, itinerary), which are linked to the intermediate nodes (e.g., risk of being bitten by JEV-infected mosquito), which are subsequently connected to the child nodes or outcomes variables (e.g., risk of death). Relationships between nodes are quantified using conditional probability tables that define the probability of a node being in each state, either based on prior distributions, user's input (for parent nodes), or conditional on the state of parent nodes (for intermediate and child nodes).

The structure of this JE Bayesian network was designed using a facilitated elicitation process with experts in travel medicine and immunisation (DJM, CLL, LFK), vector-borne diseases (NG, BJ), and neurological infections (PB), and based on available evidence from multiple sources of data that could be used to parameterise the conditional probability tables. During the first round of discussion, experts outlined the scope of the model, set the key input and output nodes for clinical relevance, and defined the path for the flow of conditional probabilities from input nodes, through the intermediate nodes, and down to the output nodes. Several iterations of the model were developed until consensus was reached. If evidence was not available, nodes were not linked even if there was plausible relationship between the nodes

(e.g., presence of comorbidities and risk of hospital admission). The model was built in GeNIe Modeler version 4.0 (BayesFusion, LLC).

# Data sources 

The model was parameterised using empirical data and expert judgment. Evidence was extracted from a range of sources and combined scientific literature (e.g., in vivo mosquito experiments, human observational and interventional studies, and research synthesis), and reports from government and international agencies (Table 1). A systematic review was carried out to identify relevant evidence on risk of JE clinical outcomes (Supplementary material S1). Evidence was systematically collected and summarised in conditional probability tables. The model was restricted to JE vaccines licensed in Australia, i.e., Imojev and JEspect (trade name in Europe and the USA of Ixiaro).

The model does not include default prior distributions (e.g., $50 \%$ male, $50 \%$ female) for input nodes as in previous Bayesian models ${ }^{18,19,21}$ which are mainly utilised for population level decision risk-benefit analyses. For an individual level pre-travel risk assessment, it is anticipated that clinicians will have access to the traveller's demographic characteristics, medical history, vaccination status, and itinerary to define the baseline scenario. Alternative scenarios can be simulated by changing the input nodes to examine the impact of interventions (e.g., vaccination) on the outcomes (see below Sensitivity analysis).

## Implementation of the online JE tool

To make the JE Bayesian network accessible to travellers and clinicians, we developed the JE tool, an online web application deployed on Amazon Elastic Compute Cloud (https://aws.amazon.com/ec2/). The system was designed in three classic tiers consisting of presentation, business logic, and data layers (Figure 1).

i) The presentation layer is where end users (e.g., clinicians) interact with the system through a web-based interface. It provides the forms for users to enter the required information to define a scenario of interest (e.g., age, sex, travel information), and presents the outputs of risk estimates (e.g., risk of death) in text and charts.
ii) The business logic layer processes the inputs from end users and transfers the input parameters to the data layer using Protocol Buffers (Protobuf).
iii) The data layer is the engine that runs the model, calculates the risks and benefits, and constructs the output for the users. This is implemented in Python and uses the SMILE version 1.6 (BayesFusion, LLC) wrapper to connect to the Bayesian network model. The JE tool is implemented using the latest frameworks including React version 17.0.2 or higher (https://react.dev/) for front-end responsive interface, Python version 3.8.10 (https://www.python.org) for back-end business logic and control, and Nginx 1.18.0 (https://www.nginx.com/) as the HTTP server to handle the requests and responses.

# Risk-benefit analysis 

The risks (i.e., AEFIs) versus the benefits (i.e., reduction in risk of symptomatic form of the disease [meningitis or encephalitis] and clinical outcomes [hospital admission, chronic neurological complications, death]) of JE vaccination was assessed at an individual level (rather than at a population level) given that pre-travel risk assessment is typically personalised based on the traveller's demographic characteristics and itinerary. The risk-benefit analysis of Imojev vaccine was conducted under different scenarios, using two hypothetical travellers with distinct risk profiles and by varying their travel destinations (i.e., very low [ $<0.1]$, low [0.1-1], medium [1-2], or high [ $>2$ JE cases per million population] JE incidence countries).

- Traveller 1: A 45-year-old female without comorbidities, travelling during low transmission season for business purposes to an urban area for two weeks, and she always uses personal protective measures (PPM) against mosquitoes.
- Traveller 2: A healthy 25-year-old male, backpacking during high transmission season for two months in rural areas, and he irregularly uses personal protective measures against mosquitoes.


# Sensitivity analysis 

Sensitivity analyses were conducted to examine the impact of different input nodes, by varying their parameters, on the probability of the outcomes. Three separate sensitivity analyses were conducted for:
i) The effectiveness of PPM use and the influence of traveller's itinerary (i.e., travel season, destination, length of the trip, and setting of planned activities) on the risk of JEV infection.
ii) Vaccine effectiveness against symptomatic form of the disease and clinical outcomes by travellers' demographic characteristics.
iii) Vaccine safety profile by travellers' demographic characteristics.

All sensitivity analyses were conducted in a tool developed in Phyton version 3.8.10 using SMILE version 1.6 (BayesFusion, LLC).

## Results

## Model

Our Bayesian network model consists of three components (Figure 2), and the states for each node as well as assumptions are summarised in Table 1. The first component collects inputs on travel itinerary (i.e., month of departure, length of trip, destination, setting of planned activities) and use of PPM against mosquitoes. The month of departure and destination are used

to establish if the travel will occur during no, low, or high transmission season (intermediate node) to determine the level of exposure to mosquitoes. This information is combined with JE incidence at the destination to estimate the probability of being bitten by a JEV-infected mosquito, and subsequent JE infection (Figure 2, red dotted box).

The second component of the model estimates the risk of symptomatic form of the disease (i.e., meningitis or encephalitis) or clinical outcomes (i.e., hospital admission, chronic neurological complications, death) based on the probability of the traveller being infected by JEV, and his/her vaccination status, age, and comorbidities. It is worth noting that the probability of long-term neurological complications is influenced by the probabilities of clinical illnesses and deaths because this only occurs among those who survive (Figure 2, blue dotted box).

The third component of the model does not contain intermediate nodes and uses demographic characteristics and type of JE vaccine received as input nodes to estimate the risk of AEFIs (Figure 2, grey dotted box).

# Risk benefit-analysis 

Results are presented for the risk of developing symptomatic form of the disease and mortality, and AEFIs. The complete set of results for the other clinical outcomes can be found in the supplementary material ( $\boldsymbol{S 2}$ ). Based on traveller 1's demographic characteristics and itinerary, her risk of contracting JEV and dying is low ( $<1$ per million) irrespective of the destination; thus, the potential impact of Imojev vaccine in reducing her risk of clinical outcomes is limited (Figure 3).

Based on traveller 2's characteristics, his risk of contracting JEV and developing symptomatic disease and/or dying is low ( $<1$ per million) in JE very low and low incidence destinations. However, his risk is higher ( $>1$ per million) in destinations with medium and high

JE incidence. The impact of Imojev vaccination is greater in medium and high JE incidence destinations, where the risk of developing symptomatic disease would be reduced from 1.8 to 0.4 (medium JE incidence destination) and from 9.1 to 1.8 (high JE incidence destination) per million. Likewise, the risk of death would substantially decline with Imojev, from 1.4 to 0.3 (high JE incidence destination) per million. Although, the risk of any AEFIs with Imojev is $\sim 1$ in 12 vaccinated individuals, the severity of AEFIs is reported to be most often mild and unlikely to affect daily activities ${ }^{22}$ (Figure 3).

# Sensitivity analysis 

Effectiveness of PPM and the influence of traveller's itinerary on asymptomatic JEV infection
Our model estimated that during the low transmission season, the use of PPM is effective in reducing the risk of asymptomatic JEV infection in travellers to very low and low incidence destinations (e.g., the chances of asymptomatic JEV infection if travelling to a rural setting for 1-2 months decreases from $\sim 1$ in 77,000 without PPM to $\sim 1$ in 179,000 if always using PPM).

The effectiveness of PPM in high transmission season is limited to very low and low JE incidence destinations, and trip duration of 3-6 months. For example, the chance of asymptomatic JEV infection in an urban setting during a 1-2 month trip decreases from $\sim 1$ in 105,800 without PPM to $\sim 1$ in 191,570 if PPM was always used. The effect of PPM on the risk of asymptomatic JEV infections in JE medium and high incidence destinations was modest (Figure 4).

## Vaccine effectiveness against clinical outcomes

In an adult traveller infected with JE, the chances of developing symptomatic disease (i.e., encephalitis and meningitis) is $\sim 1$ in 100 if unvaccinated, and reduced to $\sim 1$ in 500 with

vaccination. Likewise, in a JEV infected adult traveller without comorbidities, the chance of death is $\sim 1$ in 667 without vaccination and $\sim 1$ in 3,333 with vaccination (Figure 5).

# Vaccine safety profile 

Our model showed comparable relative safety profiles of JEspect and Imojev vaccines. Higher risk of AEFIs were observed in children aged under 5 years, whereas the differences between sexes and within age groups above 5 years were negligible (Figure 6).

## Discussion

The risk-benefit analysis of JE vaccine is multifactorial and challenging. In this paper, we present an interactive, scenario-based, JE vaccine risk-benefit tool that encompasses key traveller's characteristics available at the time of a pre-travel medical consultation (e.g., age, destination, season and duration of the trip) to estimate the risk of developing symptomatic disease and clinical outcomes, the effectiveness of vaccination in preventing these outcomes, and the risk of AEFIs. The personalised JE vaccine decision support tool is freely available on www.VaxiCal.com.

In 2002, Shlim and Solomon described JE prevention in travellers as an intersection of four factors: i) widespread disease throughout Asia, ii) low incidence in travellers, iii) high rate of mortality and disability in symptomatic cases, and iv) vaccine safety concerns. ${ }^{24}$ After 20 years, with the development and introduction of newer vaccine classes (with better safety profile compared to mouse-brain derived vaccines), safety is no longer a major issue. ${ }^{6}$ Furthermore, the global incidence is decreasing due to public health efforts to control JE and national immunisation programs. ${ }^{25}$ However, there has been little progress to improve decision-making when weighing the risk of a low incidence disease with high rate of severe clinical outcomes in symptomatic cases. Cost-benefit analyses have evaluated the benefit of JE

vaccines in $\mathrm{US}^{26}$ and business travellers ${ }^{27}$ under different risk scenarios, but tools were not implemented and made publicly available. Our free online interactive tool is the first attempt, using a non-cost-benefit approach, to facilitate this complex decision-making process.

There is no consensus about the risk of symptomatic JE in travellers to Asia, with estimates as low as 1 in 10 million ${ }^{28}$ and as high as 1 in 250,000 trips. ${ }^{29}$ However, there is general agreement that the risk is heterogenous across different types of travellers, thus the importance of personalised risk assessment tools. Most clinical guidelines ${ }^{25,27-29}$ recommend JE immunisation if travelling to endemic areas for 30 or more days during transmission season, and for short-term travellers (less than 30 days) if at high risk (e.g., visiting rural areas) (Table 2). The addition of a personalised JE vaccine risk-benefit tool as part of the JE immunisation guidelines may simplify the stratification of travellers by JE risk (e.g., low, medium, high), and therefore help identify those who would benefit the most from immunisation even if travelling for shorter period of times.

The model outputs and scenario analysis could greatly help facilitate more informed decision making between clinicians and travellers, which may result in increased vaccine uptake as well as reinforce the importance of PPM use. Risk tolerance and financial circumstances vary between travellers and may affect how they perceive and use the model outputs. Therefore, future studies will need to evaluate the acceptability, perceived utility, and the impact of the tool on clinicians' and travellers' attitudes and decision making towards JE vaccination and preventive measures.

A key benefit of using Bayesian networks is that the model structure and inputs developed in this project can be updated as new evidence becomes available. ${ }^{32}$ For example, JE geographical distribution is expanding, ${ }^{33}$ and peri-urban transmission of JE is emerging; ${ }^{32}$ as a consequence, non-leisure (e.g., business) travellers are likely now to also be at risk of JE infection as observed in a recent case series. ${ }^{36}$ The modelling platform can also be adapted to

include other aspects of the complex enzootic cycle of JEV, such as travellers' proximity to reservoir and amplifying hosts (e.g., wading birds and pigs), which are subject to changes in climate and landscape. Another benefit of our approach is that the platform and digital workflow can be adapted for supporting public health responses (at a population level, rather than for individual patients) for vaccine prioritisation in the event of a large JE outbreak, as well as modified for other travel medicine vaccines (e.g., yellow fever, rabies) or medications (e.g., malaria chemoprophylaxis) benefiting pre-travel clinical practice.

There are some limitations that need to be considered when interpreting the outputs of the model. First, the model is based on assumptions (as detailed in Table 1) that may not hold in all circumstances. For example, the model assumes homogeneous JE transmission across a country, which is not the case in some countries (e.g., India). ${ }^{37}$ Second, the model does not account for differences in planned activities (e.g., backpacking versus staying in an air conditioned hotel). We used the expected proportion of time spent at different locations/settings (i.e., rural, mixed, urban) as a proxy for the type of activities and the risk of being bitten by a mosquito. Third, the model cannot be validated using empirical data due to the need for longitudinal data of JEV-infected and JEV-non-infected travellers. However, there was consensus about the model structure and the estimates used in each of the nodes, though the quality and accuracy of the latter may not be optimal. Fourth, the complex natural enzootic cycle of JEV between Culex mosquitoes, most often Cx tritaeniorhynchus (in Asia), wading birds, and pigs is not captured in the model, nor the yearly variability of JEV transmission. Instead, average annual JE incidence in humans and JE cases reported in returned travellers were used as proxy for JEV circulating in different destinations. We acknowledge that local JE incidence may not be the best marker of JE risk in travellers, due to socioeconomic differences between tourists and local population (e.g., tourists staying in hotels and locals in unscreened houses in close proximity to rice fields), diagnostic limitations (e.g., lack of capacity to rule

out other flavivirus infections), and differences in vaccination coverages across countries. ${ }^{34}$ Fifth, at this stage, multiple destinations with different JE incidence (e.g., Japan [very low] and Vietnam [medium]) cannot be entered into the tool, and each destination needs to be modelled separately.

In conclusion, a Bayesian network was developed for risk-benefit analysis of JE vaccines in travellers, and implemented in an interactive, scenario-based, personalised JE vaccine decision support tool (www.VaxiCal.com). This is the first attempt to facilitate the decision-making process of both travellers and clinicians for JE vaccination by using quantitative estimates of risks and benefits. The tool will be updated as more evidence becomes available and from users' input. Future work will be conducted to evaluate the usability and usefulness of the tool for decision making by clinicians and travellers.

Acknowledgement: The authors will like to acknowledge that the Bayesian network model was built using GeNIe modeler and the tool on VaxiCal.com uses SMILE, both were made available free of charge for academic purposes by BayesFusion, LLC (https://www.bayesfusion.com/). The authors would also like to acknowledge the support and input from Dr Sarah McGuinness, Dr Miguel Cabada, and Dr Jenny Sisson, which substantially improve our model.

Funding: The project was partially funded by an International Society of Travel Medicine Research Awards, which was funded through a generous donation from GeoSentinel Foundation. LFK was supported by an Australian National Health and Medical Research Council (NHMRC) Early Career Fellowship (APP1158469). CLL was supported by an NHMRC Investigator Grant (APP1193826). The funders had no role in the study design, data collection and analysis, decision to publish or preparation of the manuscript.

Conflicts of interest: The authors do not have any conflicts of interest to declare.

# Authors' contribution 

- Conception and design of the study: DJM, CLL, LFK
- Design of the model: DJM, CLL, HM, NG, BJ, PB, LFK
- Collection and assembly of the data for probability tables: NG, BJ, PB, KA, WL, LFK
- Implementation of the online tool: DJM, HL, TM, LFK
- Drafted the initial manuscript: LFK
- Critically revised the manuscript: All authors
- Final approval of manuscript: All authors


# Front end 

Figure 1. System architecture of the Japanese encephalitis tool. The system consists of presentation (blue box), business logic (green box), and data (orange box) layers.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Bayesian network model for assessing the risk-benefit of Japanese encephalitis vaccine in travellers. The model contains three components, the Japanese encephalitis virus infection (red dotted box), clinical outcome (blue dotted box), and adverse events following immunisation (grey dotted box).

Input nodes are represented by blue shaded boxes, intermediate nodes by yellow shaded boxes, and outcome nodes by orange shaded boxes. Clinical illness and death are outcomes nodes, but also serve as intermediate nodes for other clinical outcomes.

![img-2.jpeg](img-2.jpeg)

Figure 3. Top panel: Risk (per 1,000,000) of symptomatic disease (blue) and death (red) due to Japanese encephalitis if unvaccinated (solid line) and vaccinated (dotted line) by incidence of Japanese encephalitis at destination. The shaded areas represent the reduction in risk of symptomatic disease and death due to JE vaccination.
Bottom panel: Risk of any, systemic, and local adverse events following immunisation (AEFI) with Imojev.

![img-3.jpeg](img-3.jpeg)

Figure 4. Heat plots for the risk (as a chance of 1 in x ) of asymptomatic Japanese encephalitis viral infection by length of the trip, use of personal protective measures against mosquitoes (PPM), and incidence of Japanese encephalitis and places to visit in the country of destination during low (top panel) and high (bottom panel) transmission season. The range of risk of asymptomatic Japanese encephalitis viral infection ranged from 1 in 1000 to 1 in 10,5 million, thus the results are presented in a $\log 10$ scale.

![img-4.jpeg](img-4.jpeg)

Long-term neurological complications

![img-5.jpeg](img-5.jpeg)

Figure 5. Heat plots in Japanese encephalitis virus infected travellers for the risk (as a chance of 1 in x ) of symptomatic disease, hospital admission, short- and long-term neurological complications, and mortality, by presence of comorbid conditions, and age of the traveller.

![img-6.jpeg](img-6.jpeg)

Figure 6. Heat plots for the risk (as a chance of 1 in x ) of any, local, and systemic adverse events following immunisation (AEFI), by Japanese encephalitis vaccine, sex, and age of the traveller.