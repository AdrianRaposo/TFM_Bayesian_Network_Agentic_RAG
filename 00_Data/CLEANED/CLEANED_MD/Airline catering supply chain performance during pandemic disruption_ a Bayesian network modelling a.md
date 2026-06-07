# Airline Catering Supply Chain Performance during Pandemic Disruption: A Bayesian Network Modelling Approach

Catering Sector  |

## SCHOLARONE ${ }^{\text {TM }}$ Manuscripts

# Airline Catering Supply Chain Performance during Pandemic Disruption: A Bayesian Network Modelling Approach 

## Abstract

Purpose: The supply chain (SC) encompasses all actions related to meeting customer requests and transferring materials upstream to meet those demands. Organisations must operate towards increasing SC efficiency and effectiveness to meet SC objectives. Although most businesses expected the COVID-19 pandemic to severely negatively impact their SCs, they did not know how to model disruptions or their effects on performance in the event of a pandemic, leading to delayed responses, an incomplete understanding of the pandemic's effects and late deployment of recovery measures.

Design/Methodology/Approach: This paper presents a method for modelling and quantifying SC performance assessment for airline catering. In the COVID-19 context, the researchers proposed a Bayesian network (BN) model to measure SC performance and risk events and quantify the consequences of pandemic disruptions.

Findings: The research simulates and measures the impact of different triggers on SC performance and business continuity using forward and backward propagation analysis, among other BN features, enabling us to combine various SC perspectives and explicitly account for pandemic scenarios.

Research Limitations: This research has been developed to respond specifically to the gap in knowledge about the airline catering subsector, limiting the study scope to this perspective and precluding consideration of, for example, airports, airline cargo and manufacturing. The other main limitation is the BN model's static approach to developing a network of risk factors. Future research could improve on the research by considering more risk variables disturbing multiple nodes and links.

Originality: This study's findings offer a fresh theoretical perspective on the use of BNs in pandemic SC disruption modelling. The findings can be used as a decision-making tool to predict and better understand how pandemics affect SC performance.

Keywords: Bayesian Network, Logistic, Performance Measurement System, Variables, Supply Chain Management, Airline Catering Sector, COVID-19

Paper type: Research Paper

# 1. Introduction 

In the pandemic era, supply chains (SCs) have fundamentally evolved, and traditional performance measurements are no longer suitable. In the airline catering context, traditional assessment approaches may need to be phased out in favour of developing new SC measurement systems (Van Hoek, 1998). This is because management may not 'see' SC-wide areas for improvement, and standard performance indicators may limit opportunities to optimise SCs (Van Hoek, 1998).

### 1.1 Aviation Supply Chains during COVID-19

The unexpected events associated with COVID-19 have impacted most business activities, especially the aviation industry, without being restricted to a single location or moment in time. Instead, there have been ongoing impacts on SCs around the world at the level of manufacturing, distribution centres, logistics and markets (Sudan and Taggar, 2021). Only a few weeks into the crisis, huge layoffs and closures had already occurred, and many airlines were financially fragile. According to ICAO, the world's air traffic had dropped to levels never seen before in history.

Furthermore, many people have died from COVID-19, wreaking further havoc on the economy, not least due to the need to lockdown cities and countries to prevent more deaths, halting manufacturing and logistics activities, affecting the supply and demand of various products (Singh et al., 2021). Notably, decisions made by one firm in an SC network directly impact the performance of other firms in today's dynamic environment (Ojha et al., 2018).

### 1.2 Supply Chain Disruption

Thus, COVID-19 has seriously disrupted SCs. Upstream SC disruptions disrupt the normal flow of goods and materials, posing a serious risk to the normal operations of downstream firms (Bode and Wagner, 2015). Transportation disruptions have undermined actual goods flows and product mobility, resulting in stalled operations, sales losses, late deliveries and reputational damage. Transportation and freight industries have also been strongly impacted (Sudan and Taggar, 2021).

# 1.3 Impact on the Aviation Industry 

To maintain operations in the pandemic context, aviation companies are increasingly forming long-term strategic partnerships with several capable suppliers, collaborating on product development, inventory control and non-core process outsourcing (Chan and Qi, 2003). Figure 1 shows that the global total number of passengers in 2021 declined between $49 \%$ and $50 \%$ compared to 2019 , a direct result of COVID-19. This decrease impacts not only airlines, airports, manufacturers and air traffic management but also food and beverage producers.

World passenger traffic evolution
1945 - 2021*
![img-0.jpeg](img-0.jpeg)

Figure 1. ICAO Air Transport Reporting Form A and A_S plus ICAO estimates
The COVID-19 pandemic has depleted the travel and tourism industries, with airlines suffering their greatest losses in history and facing a period of extended uncertainty. Meanwhile, with redesigned services and stricter safety and hygiene requirements, a 'new normal' for airline catering has arrived. As passenger numbers declined in February and March, airlines lost roughly 80,000 tonnes of daily cargo capacity, requiring the use of specialised private aircrafts for freight, with such businesses adding over 20,000 tonnes to their daily capacity. Road transportation encountered various obstacles, with non-essential-sector activity drastically decreasing and other sectors, such as food retail, experiencing significant demand spikes. Nonetheless, the sector moved quickly to reorient capacity within two weeks (Chains, 2020).

In the context of airline catering, operations are usually impacted by air traffic volume. Decreased traffic reduces demand for food and beverages, considerably impacting the airline catering subsection in terms of inventory management, stock, quantity of meals ordered and

overall system processes. Most material orders are filled using a Just-in-Time (JIT) process; upon obtaining raw materials, they must be consumed or put into production according to the menu schedule. This situation requires rapid decision-making and involves the organisation's entire SC. This, along with other factors, has meant that COVID-19 has had the following notable effects on the airline catering subsector:

- Changes to hygiene, packaging, handling and on-board services;
- New approaches to menu development;
- New expectations for suppliers in the short- and medium-term;
- New employee negotiations and contracts; and
- The fallout from long-term effects on the airline industry.

Notably, during emergencies, efficient and reliable performance measurement systems are needed. Rapid evaluations must be integrated into SCs to resolve complex situations such as pandemics. From an economic and social standpoint, lockdowns cannot be considered a long-term solution, especially when a large portion of the population relies on daily wages for survival (Singh et al., 2021). Thus, planning is extremely beneficial in terms of emergency SC Management (SCM), and investing a small amount of time and resources to achieve a minimum level of preparedness can dramatically improve outcomes for vulnerable populations, reducing the impact on people and infrastructure. Most infectious threats require the same set of SC preparedness activities, and there are many resources that can help organisations prepare.

According to Walker Jaroch (2020), the COVID-19 pandemic has refocused attention on food safety best practices in the airline catering context, especially how food can be prepared and transported from the kitchen to the plane in a sanitary manner. Nonetheless, this has changed scheduling and delayed SC processes because not only surfaces but also walls, air vents, offices and logistics equipment need to be cleaned and sanitised according to new COVID-19 protocols. This includes, for example, the interior of the delivery vans: both the driver's cabin and the back of the vans or trucks, where food is stored for distribution. This has required airline caterers to develop techniques and procedures to protect the safety of their workers, partners and clients.

COVID-19's social distancing rules, sickness-related labour shortages and lockdown procedures have caused widespread problems for the food processing industry. In restricted locations, such as fruit and vegetable packing plants or meat processing plants, appropriate social distancing measures may compromise operational efficiency, and adequate staff protections are required. Many businesses have also reported high rates of employee absences;

for example, workforce availability in French meat processing plants in COVID-19-affected regions reduced by up to $30 \%$ during 2020 (Chains, 2020).

# 1.4 Research Goal 

This study aims to consider the impact of implementing Bayesian network (BN) modelling to measure SC performance in the airline catering context. These objectives can be measured using various performance indicators, depending on the focus, whether, for example, environmental, economic, social or integrative (Beske-Janssen et al., 2015). Among the goals of performance evaluation is to determine the level of functionality of an SC (Majercak, 2021). To accomplish this, it is critical to track and manage the performance of various tasks across the SC, including logistics, inventory management and warehousing, demand forecasting and supplier and customer relationship management. To this end, SC performance measurement systems enable the adoption of performance metrics that span multiple firms and processes (Maestrini et al., 2017).

These objectives have been framed in terms of the following research questions:
I. Does customer satisfaction impact SC performance in the airline catering context?
II. Does every stage in the process contribute to SC performance in the COVID-19 context?

The challenges associated with this study's inquiry are crucial for evaluating SC performance. According to Van Hoek (1998), new measurement approaches should pave the way for SC competitiveness by directing management attention to areas where SCs can be improved. This paper responds by proposing a new method for measuring SCM performance. The BN approach proposed should build on current knowledge about measuring SC performance in the airline catering context. Additionally, the performance measurement system developed can be adopted by practitioners to guide their decision-making in response to unpredictable events.

The rest of this paper is organised as follows. Section 2 reviews the current literature concerning measuring SC performance, with a focus on SCM and an emphasis on the importance of a few key issues. Section 3 proposes a BN-based performance measurement model. Section 4 describes the algorithm used to calculate performance and aggregate results Section 4, an algorithm that builds on fuzzy set theory to address the real-world measurement problem. Section 5 provides a basic demonstration of the model's application, and Section 6 concludes the paper with a summary of the performance measurement method.

# 2. Existing Performance Measurement in Supply Chain Management 

Most applied research approaches involve some measure of the performance of the developed solution (Beamon, 1999). However, the many performance measurement techniques available complicates choosing the right tool. These can be categorised according to their intended use, with examples including green SCM, sustainable SCM and SCM performance monitoring (Abolbashari et al., 2018a). Generally, performance measurement research focuses on examining existing performance measurement systems, categorising and studying performance measures within a category, and developing frameworks for developing performance measurement systems for various types of systems (Beamon, 1999). There are far too many ways to measure performance to generalise the research's findings on the link between logistics practices and performance (Majercak, 2021).

### 2.1 Traditional and Current Supply Chain Performance Measurement

Over the last year, there are quite a number of definition given to supply chain performance. Neely $(1995,2005)$ refer supply chain performance measurement as a set of metrics that used to examine the efficiency and effectiveness of the action. Similarly, Tangul (2004) and Galakashi et al (2018a,b) states that performance measurement in supply chain (connect with a process of quantifying effectiveness and efficiency of action. Seiler (2016) refer supply chain performance as a combination of different measure to assess and quantify the effectiveness and efficiency of action along the supply chain. As highlighted by earlier his signal and Thakkar (2012), there are various measurement in measuring supply chain performance such as using qualitative and quantitative measurement, supply chain operation reference (SCOR), modelling, balance scorecard and financial non-financial measures.

Current SC performance assessment methods are insufficient because they focus significantly on cost as a key (if not single) metric, are not inclusive, are frequently at odds with the organisation's strategic goals, and fail to consider the impact of uncertainty (Beamon, 1999). For instance, Gunasekaran et al (2001) recommend comprehensive framework in assessing improved operational performance in supply chain via measuring the total cash flow time, customer query time, improved relationship management activities, rate of extent investment and net profit vs productivity ratio. Meanwhile, traditional indicators, which primarily concern economic issues, are insufficient for evaluating the performance of longterm SCs (Beske-Janssen et al., 2015), and because there are too many flaws, the contributions

of the performance management systems in use are discounted in the SCM context (Chan and Qi, 2003). Standard performance measurement theory has mostly concentrated on financial
littics, such as BDI, cash flow and profits (Majercak, 2021), and mostly considered short
term applications. Notably, many organisations collect data that is solely financial and operational in nature, with various financial and operational statistics available for most organisations, including overhead expenses, income and profit. One of the reasons that organisations struggle to survive long-term is a focus on the short term. Hence, Fonseca and
Krevele (2020) have highlighted the importance of a total framework for short and long-term
in measure SC performance in various situations, for example in the pandemic of COVID-19.
Because SC performance management systems should include inter-firm performance measures, there are significant challenges in terms of integrating and sharing data from multiple firms, coordinating inter-firm processes and infrastructure and managing relationships with external SC partners throughout the assessment process. Traditional (internal) performance management systems typically target processes and data for a single firm (Maestrini et al., 2017).

The traditional approach has the disadvantages of being backwards-looking, disregarding intangible aspects and delaying information evaluation. SCs must constantly improve, especially in the COVID-19 context. To achieve this, we must improve our understanding of what makes SCs function, rather than focusing on narrow company-specific or function-specific metrics. According to Chan and Qi (2003), research concerning measuring SCM performance can be either qualitative or quantitative. For example, Beamon (1999) employs customer satisfaction and responsiveness, flexibility, supplier performance and costs to model the SC and divides indicators into three categories: resources, output and adaptability.

Apart from financial measure in measuring supply chain performance, there are man-
other supply chain performance measures highlights in previous research. Different industry or
different organization may require different type of supply chain design, strategies and
performance measurement (Beamon and Bidek, 2008; Nguyen et al., 2021). For instance, the
use of Balance scorecard in measuring, supply chain performance. A study from Reefke and
Trocchi (2013) and Nouri et al (2019) proposed to use balance scorecard in measuring supply
chain performance which only measure factors that are directly associated with supply chain
strategy rather than measuring everything (Pinnoyamoorthy and Mutali, 2008). Specifically,
balance scorecard incorporate both financial and non-financial measures which look at four
different angles namely customer, financial, process and learning growth (Raval et al 2019).
Recent study by Frederico et al (2021) proposed balance scorecard approach in measuring

# Study chain performance in the industry 8.0 era. They recommend that the four standards of 

balance scorecard support current supply chain activity in current digital era.

From COVID-19 was considered an unexpected event in the aviation context, traditional performance measurement systems have proven unsuitable for evaluating airline catering's SC performance during this period, demanding an alternative approach capable of incorporating emergency circumstances. This is because the traditional systems cannot support the entire SC performance process, instead focusing on individual stages. Moreover, these systems often cover only a component of the SC (e.g. supplier side, customer side or internal SC activities) and employ a specific measurement scope (e.g. external partner capabilities, SC processes or connections), and the scientific literature does not provide comprehensive insight (Maestrini et al., 2017). As highlighted by Gopal and Thakkar (2012), modelling is one of the popular tool in assessing supply chain performance. This context gives rise to this paper's proposed novel performance measure-system, which adopts a BN approach to assess performance in the context of unexpected events.

## 3. Proposed Bayesian Network Modelling Approach

This section provides a brief overview of BN theory, detailing its benefits and the justifications for using it as a modelling method to achieve performance excellence, along with indicating how it outperforms the prevalent classical models, ultimately enabling the elaboration of a performance management system for SCM.

BNs are particularly suited to assessing SC performance in the COVID-19 context because they can account for the uncertainty by measuring the SC's contingency strategies, as their widespread adoption to address system complexity and uncertainty suggests (Feng et al., 2014). Other advantages of BNs over commonly used multivariate models include their suitability for limited data situations and the fact that correlations between factors in the dataset are integrated into the probabilistic dependencies (Jensen et al., 2009). Notably, researchers have already used BNs in the SC context (Maleki and Cruz-Machado, 2013). For instance, a recent study by Seyedmohsen and Ivanov (2021) suggests that a multi-layer BN can be useful for crisis management during the pandemic by enabling the identification of SC disruption triggers and risk events. Graphical modelling features numerous advantages for data modelling when used in conjunction with statistical techniques. First, because it captures all of the interdependencies of the variables, it can easily manage scenarios with missing data. Second, a BN can learn causal linkages, allowing it to better grasp a problem area and predict intervention outcomes. Third, the model's causal and probabilistic semantics make it suitable

for mixing previous information (typically in causal form) and data. Fourth, Bayesian statistical approaches combined with BNs provide an effective and consistent way to avoid data overfitting (Heckerman, 1997).

Furthermore, the backward and forward propagation analysis involved in BN modelling is unique and advantageous for measuring the impact of different triggers of SC performance and business sustainability (Seyedmohsen and Ivanov, 2021).

# 3.1 Using Bayesian Networks to Assess Supply Chains During Emergencies 

BNs represent a probabilistic graphical method for building models using data or expert opinions, providing probabilistic and graph-theoretic models representing uncertain knowledge and reasoning (Tang and Liu, 2007). Prediction, anomaly detection, diagnostics, automated insight, reasoning, time series prediction and uncertain decision-making are just a few of the activities that they can be utilised for. BNs are probabilistic because they are constructed from probability distributions, which leads to conditional probability distributions (Abolbashari et al., 2018a). There are also probability laws for prediction and anomaly detection, reasoning and diagnostics, decision-making in response to uncertainty, and time series prediction.

BNs can also be visualised as Asia Networks (see Figure 2) and as directed acyclic graphs that combine probabilistic relationships and update probabilistic beliefs using Bayes' rule (El Amrani et al., 2021). Although neither is required to visualise the structure of a BN, they are excellent ways of understanding a model. For example, the decision relationship diagram, which includes event nodes and decision nodes, is a directed acyclic graph application developed for decision analysis with the essential responsibility of providing a proper description of the probability function. All additional computations can be conducted using symbolic operations on the probability expression upon completing the network configuration (Kang et al., 2020).

There are nodes and links in the networks. The variables of interest are represented by nodes, and the links connecting the nodes represent causal relationships between the variables (Musharraf et al., 2016). A BN is a graph with nodes connected by directed links. A variable, such as a person's height, age or gender, is represented by each node in a BN. A variable can be discrete, as in the case of gender (male or female, among other designations), or continuous, as in the case of age. The structural specification refers to the structure of the BN, which

comprises nodes and links. Adding links between nodes indicates that one node directly influences the other. Even if there is no link between two nodes, it remains possible that they are connected via other nodes. However, depending on the evidence that is established by other nodes, they may become dependent or independent.
![img-1.jpeg](img-1.jpeg)

Figure 2. Example Bayesian network for airline catering
Figure 2 shows a BN for a simulation airline catering case study. The construction process for this case study is detailed in Section 5 of this paper. Meanwhile, Table I outlines the four key analytics operations that a BN can perform: descriptive analytics, diagnostic analytics, predictive analytics and prescriptive analytics.

Table I The four major analytics procedures conducted by Bayesian networks


Prescriptive analytics should be utilised to support real-world SCM initiatives to enable the monitoring of all SC entities. Predictive analytics employs approaches and tools such as business rules, algorithms, machine learning, and computational modelling to analyse data from a range of sources, including historical and transactional data, real-time data feeds, and big datasets. However, producing prescriptive analytics is complicated, meaning most firms have not yet adopted this aspect. Nonetheless, prescriptive analytics can considerably impact how organisations make decisions and, ultimately, improve their bottom line. Meanwhile, descriptive analytics consider past events and predictive analytics forecast future events, making neither suitable for this research paper. Instead, we adopt prescriptive analytics, which have a clear objective: the delivery of guidance on possible outcomes.

# 3.2 Research Flow Diagram 

Various efforts have been made to ensure that this study meets its objectives. Figure 3 presents a flowchart detailing the research's movement from data gathering to the data analysis.
![img-2.jpeg](img-2.jpeg)

Figure 3. Research Flow Diagram

# 4. Indicators for Performance Measurement 

To reveal meaningful insights into SC performance in the pandemic context, it was critical to utilise relevant indicators for measuring performance for the particular SCs in question. These indicators needed to reflect the SC's overall performance and incorporate relevant non-financial and intangible performance components. Concerning the latter, for example, customers are paying more attention to delivery reliability and delivery frequency flexibility, which are non-financial but crucial to firm strategy in the Just-in-Time manufacturing world (Chan and Qi 2003). Given the aims and methods of each SC vary, each SC requires its own set of relevant measures. Thus, this paper proposes BN modelling to analyse the performance of airline catering SCs.

According to Chan and Qi (2003), these performance indicators should measure components that are critical to SC goals and strategies, components with inter-influence and which represent a common concern for SC partners, and components involving both internal and external partners and customers.

Furthermore, because the performance of the entire chain is aggregated in one location, processes are transparent, and complete performance data are available. At each point in an SC, the system is designed to identify and solve all potential problems, with performance metrics available to all staff. That is, every distribution centre and corporate headquarters has a wall covered in boards with graphs and tables on which the current performance indicators are displayed and updated on a regular basis, enabling all employees at all locations to see how the SC is performing compared to its defined goals (Cuthbertson and Piotrowicz, 2011).

## 5. Bayesian Network Construction

This paper's performance assessment focuses on a few key areas that pertain to three categories: input measures, output measures and composite measures (Chan and Qi, 2003)

To create a BN, it is first necessary to create a causal graphical model with a directed acyclic graph to represent the interdependencies between the various key performance indicators. Knowledge engineers who use BNs for modelling can assign belief degrees to the associated probabilities at BN nodes. Because these algorithms necessitate a large amount of data, the second method, expert opinion data collection, is commonly used (Abolbashari et al., 2018a). Although scholars have introduced numerous performance indicators (Abolbashari et al., 2018b), practitioners should be aware that most performance indicators are generic and must be tailored to their specific SC.

The second step is data gathering. The ERP system is the most reliable data source. However, because not all data is prepared in an ERP system, practitioners may need to conduct interviews with specialists to reveal tacit knowledge. Thus, the BN should be expanded to include measure reliance and independence (Pochampally et al., 2009), enabling the BN to learn from the data using unsupervised learning algorithms.

However, at this point, quality becomes a concern (Maleki and Cruz-Machado, 2013). It is necessary to examine the BN to ensure that it accurately replicates the real world before applying the model to the in-context monitoring of performance metrics.

Construction of this research's model involved following the five steps detailed by Abolbashari et al. (2018):

Step 1: Expert selection. Experts who have measured and managed SC performance are chosen. Before designating someone as an expert, an interview with each member of the knowledge management team is undertaken to determine their knowledge. A manager is deemed an expert if their expertise reaches a particular threshold.

Step 2: KPI determination. KPIs are utilised to determine which nodes make up the BN. Experts are provided a primary set of KPIs and asked to vote on the list to finalise it, using a bi-directional weighted voting approach that considers each expert's perspective. A KPI's score is included in the BN model if it surpasses a specified threshold.

Step 3: Relationship determination between KPI. This stage has two main objectives. The first stage defines the relationship between the final set of KPIs, and the second stage checks for cyclic relationships. These two objectives are pursued simultaneously rather than sequentially, which has several advantages. First, because less information is received from experts during the knowledge diffusion process, both the experts and the network function take less time. Experts are left with fewer options to choose from if they reveal their thoughts about the links in a BN in a way that leads to the formation of a cycle, eliminating the unwanted option that leads to that formation. Second, the researcher uses all of the information collected from the experts in the development of the BN, which contrasts with traditional approaches that see researchers create BNs based on expert opinions before rejecting some of the information obtained to avoid a cycle(s). The researcher may need to follow up with the experts to check the adjustments, another time-consuming process.

Step 4: Interpretation of CPT. Each child node is given a Conditional Probability Table (CPT). It is not always easy to elaborate the CPT, especially for large BNs. To complete a CPT for a child node with $n$ parents, experts must specify the probability values.

Step 5: BN Development. In phases 2 and 3, the BN model is built using algorithms. Algorithm 2 is used to design the BN's architecture after utilising the Weighted-Voting Algorithm to finalise the BN's nodes and generate pairs of nodes in line 2 of Algorithm 5.

The five steps involved in constructing a BN are presented as the framework illustrated in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. BN construction steps (Abolbashari et al., 2018a)

Thus, this research's BN construction began with selecting experts for initial indicator selection. Next, indicator selection was voted on by experts based on the pool of supply chain indicators presented in Table II. The subsequent vote was combined using Dempster-Shafer, giving a result of either cycle or no cycle. When the cycle indicated a link between the two nodes, it would produce a link in the acyclic direction and all the link nodes would then be considered to constitute a CPT interpretation, with the resulting CPT table comprising an indicator's node, state and probability. These values were then utilised to construct the BN using Bayesian software, as detailed in the following subsection.

According to Hosseini and Ivanov (2019), directed acyclic graphs with a collection of nodes (variables) and a set of arcs that indicate the dependency or causal links among variables are used to graphically represent BNs. Consider the structure of a BN as a directed acyclic gap represented by G , where $G=(V, E)$, and $V=\{X 1, X 2, \ldots, X n\}$ represents a set of random variables (nodes) and E is a set of arcs (edges) (Pochampally et al., 2009). The causal relationship between $X i$ and $X j$ is represented by an inbound arc from $X i$ and $X j$, where $X i$ is the parent node of $X j$, and $X j$ is the child of $X$, implying that the likelihood of $X j$ depends on the likelihood of $X i$. As mentioned, the causal relationships between child and parent nodes can be quantified using a CPT (Pochampally et al., 2009). This set of parent nodes is generally denoted as $\pi$. The second element, $\Theta$, implies the set of parameters of the BN. Equation 1 defines the joint probability distribution of network nodes:

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi_{i}\right)=\prod_{i=1}^{n} \theta_{X_{i} \mid \pi_{i}}
$$

Equation 1

Tse et al. (2012) uses conditional probability in a Bayesian network. If the existence of some evidence B is contingent on the existence of a hypothesis A , the probability that both A and B occurred $-\mathrm{P}(\mathrm{A}, \mathrm{B})-$ is given by Equation 2 :
$\mathrm{P}(\mathrm{A}, \mathrm{B})=\mathrm{P}(\mathrm{A}) \mathrm{P}(\mathrm{B} \mid \mathrm{A})$
Equation 2

If A is relevant for B , then B must likewise be relevant for A , according to the multiplication law of probability, which describes commutativity. Figure 5 illustrates the differential BN connection.
![img-4.jpeg](img-4.jpeg)

Figure 5. Bayesian network connections. a) Serial, b) Diverging, c) Converging (Tse et al., 2012)
$\mathrm{P}(\mathrm{A}, \mathrm{B})=\mathrm{P}(\mathrm{A}) \mathrm{P}(\mathrm{B} \mid \mathrm{A})=\mathrm{P}(\mathrm{B}) \mathrm{P}(\mathrm{A} \mid \mathrm{B})$, meaning
$P(B \mid A)=\frac{P(B) P(A \mid B)}{P(A)}$
Equation 3

This study has adopted several performance variables to demonstrate the BN approach, building on recent research by the aforementioned Abolbashari et al. (2018a) along with Maleki and Cruz-Machado (2013) and Ojha et al. (2018).

The model's performance variables have been chosen based on the needs of the SC being considered and based on the managerial-level knowledge of the experts interviewed. This ultimately produced the following indicators: time, cost, customer satisfaction, quality, forecasting accuracy and supplier performance. After determining the variables, it was necessary to find links between variables in the acyclic graphical network. According to Abolbashari et al., (2018), the information listed can then be integrated using the DempsterShafer theory. Table II presents a simulation set of indicators for monitoring SC performance based on a thorough assessment of the literature.

Table II. Pool of Supply Chain Indicators


Not all companies have to consider all of these indicators (Abolbashari et al., 2018a). A model's indicators should be chosen based on an organisation's needs, especially in the COVID-19 context. Thus, assuming the managerial knowledge of the experts, Table III presents expert voting on the pertinence of each indicator.

Table III. Expert voting on the indicators presented


In Table III, the mean of the votes for each indicator is used to generate the score value, with the threshold value $(\gamma)$ for an indicator's inclusion being 0.5 . That is, indicators were chosen if the mean vote exceeded 0.5 , leading the experts to ultimately decide on eight indicators, as listed in Table IV, alongside the possible states for each indicator.

Table IV. Final set of indicators


After deciding on the final set of indicators, the next step was determining how the indicators relate to each other. Experts were asked for their thoughts on the relationship between the various indicators. As mentioned, the data were then combined using the Dempster-Shafer theory (Abolbashari et al., 2018a), producing unique types of relationships for each pair of indicators. Meanwhile, the cycle prevention algorithm monitored expert viewpoints to prevent a cycle from forming. Figure 6 depicts the final between-indicators mapping.
![img-5.jpeg](img-5.jpeg)

Figure 6. Acyclic graphical network based on the work of Abolbashari et al. (2018a)
The final step was identifying a CPT for every node (i.e. variables). Nodes are presented in table form to provide a vision to enable easy identification of parent and child nodes, with nodes including cost, supplier performance, forecasting and procurement cycle time. Only the effectiveness node was only a child node; the other variables were both parent and child nodes.

The probability distribution for the parent nodes should also be established to complete the BN and prepare it for future analysis (Abolbashari et al., 2018a). The probability distribution value might be derived from a case study or the current state of an SC department's operations. Table V presents the probability distribution for the specified indicators. Certain probability distributions were obtained by examining how an organisation had behaved over time with regard to these performance measurement variables, and these are shown for a period of time. For example, only $40 \%$ of procurements were completed through e-procurement, and $70 \%$ of the time, the organisation failed to accurately estimate future demands, resulting in the given product or service not meeting current needs (Abolbashari et al., 2018a). The final BN model appears in Figure 6 and was created using Bayes server software.

Table V. Probability Distribution Table


![img-6.jpeg](img-6.jpeg)

Figure 7. A Bayesian network for an airline catering supply chain

# 5.1 Bayesian Network Reasoning 

Bayesian reasoning describes a statistical inference method that uses Bayes' theorem to update a hypothesis' probability when more data or information become available. BNs can reason in the face of uncertainty and update their forecast based on new data (Huang et al., 2019). This is critical when modelling the measurement of the performance of an SC using partial and iterative observations. The four types of reasoning BNs enable can help managers make decisions and better analyse their approach to assessing SC performance (Abolbashari et al., 2018a).

### 5.2 Modes of Reasoning

Four modes of reasoning (diagnostic, predictive, inter-causal and mixed) are possible in BN modelling (Abolbashari et al., 2018a). Following a brief description of each of these four types of reasoning, this section illustrates their functionality and how they may be used to assess and control SC performance. The researcher demonstrates how different types of reasoning in BNs can be employed in the context of SC performance monitoring and management to improve decision-making and sensitivity analyses (Abolbashari et al., 2018a).

Evidence is an important term for analysing BNs and updating the network. This feature allows the use of managerial-level insights to update information about various nodes in the BN network, allowing the utilisation of BNs as a visualisation tool (Abolbashari et al., 2018a).

Predictive Reasoning. The probability distribution for the child nodes can be determined using this type of reasoning, which is based on accessible information about the parent nodes. Figure 8 demonstrates the reasoning flow from top to bottom (parent nodes to child nodes). A child node may represent the BN's effectiveness (see Figure 7), and parents could be any of the immediate (e.g. quality) or non-immediate (e.g. forecasting) parent nodes. When we have information about the states of the parent nodes and want to see the degree of performance effectiveness of the SC in uncertain situations, we can use this reasoning method. We might also consider how parent nodes affect child nodes and use different values for parent nodes to establish the system's intelligence level (Abolbashari et al., 2018a). This type of analysis is known as sensitivity analysis, and it serves as a benchmark for various organisational departments, serving as an objective for their upcoming trading session. Scenario 1 explains the use of predictive reasoning in the context of assessing the performance of airline catering SCs.

![img-7.jpeg](img-7.jpeg)

Figure 8. Predictive reasoning

Scenario 1: Building on the conceptual illustration in Figure 8, this scenario exemplifies placing evidence in the parent nodes according to the organisation's current circumstances, an organisation can begin to measure its performance indicators. Consider, for instance, the procurement process performance: if we have data about the state of a node, we can input it into the model, which updates the entire network and produce an estimate of the procurement process level (Abolbashari et al., 2018a).

Meanwhile, Figure 9 demonstrates that if customer satisfaction is high, the degree of efficiency of the performance of the airline catering SC increases from $47 \%$ to $52 \%$. These data can be used to generate various outcomes. If only a small percentage of consumers (i.e. airlines) are happy with the level of service they receive, an airline caterer can consider how much its total performance would improve if dissatisfied customers were completely satisfied. The BN model's evidence-consideration feature is not restricted to one indicator. The outcomes for the other four parent indicators were as follows: High for cost, Reasonable for procurement cycle time, High for forecasting and Low for supplier performance (due to COVID-19-related strikes). As an example of how this latter result appears in the real world, suppliers must undergo extra processes before delivering raw materials to the airline catering stores, complicating supplier ability to deliver goods on time.

![img-8.jpeg](img-8.jpeg)

Figure 9. The Bayesian network's evidence-consideration feature

Diagnostic Reasoning. This reasoning method moves from effects to causes, with specific circumstances constituting evidence for child nodes, and beliefs about parent nodes being consequently modified. When we desire a specific degree of airline catering SC effectiveness and want to know how to achieve that, we can use this reasoning method, making it extremely beneficial to a company's strategic planning. If an organisation aspires to a given level of performance, the network will be updated and presented with a set of steps to achieve that goal. Scenario 2 elaborates on this application.

![img-9.jpeg](img-9.jpeg)

Figure 10. Diagnostic reasoning
Scenario 2: Building on the conceptual illustration in Figure 10, this scenario indicates that the current efficiency status is ineffective (a likely value of $47 \%$ ). Assuming that the company wants efficiency to achieve $100 \%$ efficiency, the BN will automatically update the entire network from bottom to top with the updated required values for the indicators whenever this desired level of performance is inserted into the model as proof, as Figure 11 illustrates. The revised values of the indicators reflect the changes that the organisation has to make for each indicator. Diagnostic reasoning enables determination of the types of modifications required.
![img-10.jpeg](img-10.jpeg)

Figure 11a.. Diagnostic reasoning helps improve efficiency
In the case study, the following improvements for each indicator were required for the airline catering SC to achieve efficiency: costs should be $60 \%$ lower, procurement cycle time must be reasonable $52 \%$ of the time, the supplier must achieve a $60 \%$ better performance, and forecasting must be $60 \%$ more accurate.

![img-11.jpeg](img-11.jpeg)

Figure 11b. Diagnostic reasoning helps improve efficiency
Inter-causal Reasoning. Once we establish the true status of one of a node's parents, we can measure the status of another parent (Abolbashari et al., 2018b). When access to the values of all effective variables is not possible, this feature is extremely crucial for procurement. Various factors, such as the confidential nature of some information, the time delay in obtaining the requested information, and the unwillingness of some departments to share information due to internal competition among departments at the same hierarchical level, may all contribute to this inaccessibility. Scenario 3 elaborates on this situation.
![img-12.jpeg](img-12.jpeg)

Figure 12. Inter-causal reasoning

Scenario 3: Building on the conceptual illustration in Figure 12, this scenario exemplifies the inter-causal reasoning method in the context of measuring the performance of airline catering SCs. Given reasonable evidence for the states of quality and forecasting are

available, information or the level of supplier performance is updated by inputting this data into the BN model, as Figure 12 demonstrates.
![img-13.jpeg](img-13.jpeg)

Figure 13. Inter-casual reasoning in the context of measuring the performance of airline catering supply chains
The information available does not provide an estimate of the supplier's contribution to SC performance. By obtaining information about the two other nodes, the BN increases our knowledge and grasp of the supplier's true performance level, which we now know is $72 \%$ rather than $40 \%$. Not only can the BN be used to evaluate customer performance, it can also be used to evaluate supplier performance. This BN characteristic is advantageous and can be utilised to assess SC partners. When we do not have or will not have information about the state of a given node, we can use inter-causal reasoning to approximate the state of that node (Abolbashari et al., 2018b).

Combined Reasoning. The final reasoning method BNs enable considers the state of a node with the states of both parent and child nodes visible simultaneously. Scenario 4 briefly exemplifies how combined reasoning functions.
![img-14.jpeg](img-14.jpeg)

Figure 14. Combined reasoning
Scenario 4: Building on the conceptual illustration in Figure 14, this scenario shows how a BN can examine the effect of evidence at both the parent and child of a node simultaneously (see Figure 15). When the only information available is about the status of forecasting (for example, High accuracy), we know that the evidence will be of higher quality. If there is also information about customer satisfaction (for example, High), this evidence will also update our information about the quality level. In fact, combined reasoning represents a hybrid of diagnostic and predictive reasoning. Combined reasoning approaches a specific node from two directions. When information concerning forecasting accuracy is available, the BN first offers information about the quality level (Abolbashari et al., 2018b).
![img-15.jpeg](img-15.jpeg)

Figure 15. Combination Reasoning of customer satisfaction and high accuracy forecasting

When there is also information available for customer satisfaction, the BN provides more detailed and up-to-date information about the quality level in the second attempt. Consequently, simultaneously having information about a node's parent and child enables combined reasoning to derive information about the state of a node (Abolbashari et al., 2018b).

The simulation case study produced enables the elaboration of a way for airline catering organisations to utilise BNs to measure and improve SC performance.

# 5.3 Interpreting the Findings 

It is acknowledged that COVID-19 has produced many issues, including travel restrictions, economic crises, decreased passenger demand, significantly decreased aircraft service demand and changes to passenger behaviour. For instance, according to the International Air Transport Association, the drop in economic activity and commerce impacted freight about $30 \%$ year-on-year in April 2020, with the impact remaining around $12 \%$ in August of the same year (OECD, 2020). Meanwhile, passenger air transport, as measured by revenue per passenger kilometre, had decreased $90 \%$ year-on-year in April 2020 and remained down $75 \%$ in August 2020. The pandemic has affected almost every sector in the aviation organisation: airlines, airports and airline catering organisations. Changes in passenger demand for in-flight meals disrupting SCs has represented a key challenge for airline catering organisations. This empirical study has mapped the current performance of airline catering SCs using key performance indicators in a BN that airline caterers can use to improve their decisionmaking processes, improve their SC performance and achieve sustainability. This study's findings make a significant theoretical and practical contributions to the bodies of knowledge about SC performance measurement and the airline catering sector.

By implementing BN modelling to analyse airline catering SC performance in the COVID-19 context, managers and executives can identify which performance indicators most impact their organisation's SC performance (Rabbi et al., 2020). Managers and experts can monitor current SC performance according to the current performance level of each performance indicator, helping them to understand the organisation's current relative position in the industry. According to Rabbi et al. (2020), managers can use diagnostic analyses to determine the target performance indicator levels needed to obtain satisfactory overall results.

Notably, Scenario 4 demonstrates that customer (i.e. airline) satisfaction may impact airline catering SCs. When the data is available to update BNs for customer satisfaction, the quality node will demonstrate a quantitative, which depends on the satisfaction level of the customer. If the customer displays a high level of satisfaction, the quality improves. However,

most managers have limited resources for monitoring, prioritising and optimising customer satisfaction to substantially help achieve an SC's performance goals.

Every stage in a BN is strongly linked. When one data point is added to the model, it changes other data points, impacting the overall results. For example, in the scenario mentioned above, each parent and child node contributes to the performance of the other parent and child nodes. Adding forecasting and customer satisfaction data can change the performance quality of an airline catering SC, especially in the pandemic context, in which core analysis is important for remaining sustainable. Given this research is solely focused on the airline catering SC performance perspective, future scholars should empirically investigate SC performance in other aviation sub-sectors (e.g. airline, airport, cargo operation, ground handling, and maintenance, repair and overhaul).

# 5.4 Theoretical and Managerial Implications 

This study's findings make a few important theoretical contributions. First, the BN approach enables identification of different performance measures, including customer satisfaction, quality, procurement performance, future forecasting, efficiency and effectiveness. As highlighted by previous research, there are many tools to examine supply chain performance measurement such as balance scorecard (Frederico, 2021), financial performance (Galankash and Rafiei, 2021) benchmarking (Wong and Wong, 2008), non-financial performance (Beamon and Balcik, 2008), SCOR or supply chain operation reference (Nguyen et al., 2021; Agarwal et al., 2006), as well as modelling (Euchi et al 2018). This study adopts Bayesian modelling network in measuring supply chain performance in airline catering context. This study extends current literature on both Bayesian Network Modelling (BN) method and supply chain performance measurement literature. Specifically, this study provide useful information of using BN in measuring supply chain performance. The BN construction steps shares in this study provide useful guidelines and references for future scholar to conduct supply chain performance study using BN method. In fact, an exploration of supply chain performance in rarely explored sector which is airline catering context in this research bridge the literature gap. As recommended by Kamble and Gunasekaran (2019), more study from different method such as BN method use in measuring supply chain performance would give meaningful insight to the scholars in the field. Additionally, the detail discussion provided in this study provide opportunities for future scholars to adopt the same method in examining the same issue in different context. Additionally, this study also enhances BN literature with investigating supply


every stage in the process contribute to the SC performance, especially in the COVID-19 context.

# 6. Conclusion 

This paper has detailed the significant flaws in current performance measurement methods, particularly in terms of SCM. This paper proposes using BNs to measure the performance of airline catering SCs in the COVID-19 context - a context entailing many uncertainties in terms of decision-making - to ultimately improve SCM. The paper has detailed existing SC performance measurement approaches, the proposed BN modelling method, the construction of the BN are outlined and some suggested applications. Building on previous studies, this paper highlights several additional effects. For example, rather than using historical values of an outcome, the temporal impacts between leading indicators and a lagging outcome are captured to produce a lower predicting error. Meanwhile, the paper presents the BN construction framework adapted from the extant literature, broadening the current body of knowledge to improve SC performance measurement systems in the airline catering context. Although certain issues may not have been completely eradicated by the BN approach, these issues can be significantly minimized by the more comprehensive and realistic risk assessment and more dynamic and adaptive risk management offered by BNs. This can contribute to the substantial efforts currently directed towards recovering from the pandemic and building a more robust system capable of withstanding future crises. Future research are also suggested to look at BN method in assessing supply chain performance in humanitarian context.

This research also features certain limitations that can be used to drive future research. These include the lack of prior research on BNs in the airline catering context. Furthermore, this model application only analysed a small number of risk variables; thus, future studies could consider various other risk variables that affect different nodes and linkages between nodes.

# Airline Catering Supply Chain Performance during Pandemic Disruption: A Bayesian Network Modelling Approach 

## Abstract

Purpose: The supply chain (SC) encompasses all actions related to meeting customer requests and transferring materials upstream to meet those demands. Organisations must operate towards increasing SC efficiency and effectiveness to meet SC objectives. Although most businesses expected the COVID-19 pandemic to severely negatively impact their SCs, they did not know how to model disruptions or their effects on performance in the event of a pandemic, leading to delayed responses, an incomplete understanding of the pandemic's effects and late deployment of recovery measures.

Design/Methodology/Approach: This paper presents a method for modelling and quantifying SC performance assessment for airline catering. In the COVID-19 context, the researchers proposed a Bayesian network (BN) model to measure SC performance and risk events and quantify the consequences of pandemic disruptions.

Findings: The research simulates and measures the impact of different triggers on SC performance and business continuity using forward and backward propagation analysis, among other BN features, enabling us to combine various SC perspectives and explicitly account for pandemic scenarios.

Research Limitations: This research has been developed to respond specifically to the gap in knowledge about the airline catering subsector, limiting the study scope to this perspective and precluding consideration of, for example, airports, airline cargo and manufacturing. The other main limitation is the BN model's static approach to developing a network of risk factors. Future research could improve on the research by considering more risk variables disturbing multiple nodes and links.

Originality: This study's findings offer a fresh theoretical perspective on the use of BNs in pandemic SC disruption modelling. The findings can be used as a decision-making tool to predict and better understand how pandemics affect SC performance.

Keywords: Bayesian Network, Logistic, Performance Measurement System, Variables, Supply Chain Management, Airline Catering Sector, COVID-19

Paper type: Research Paper

# 1. Introduction 

In the pandemic era, supply chains (SCs) have fundamentally evolved, and traditional performance measurements are no longer suitable. In the airline catering context, traditional assessment approaches may need to be phased out in favour of developing new SC measurement systems (Van Hoek, 1998). This is because management may not 'see' SC-wide areas for improvement, and standard performance indicators may limit opportunities to optimise SCs (Van Hoek, 1998).

### 1.1 Aviation Supply Chains during COVID-19

The unexpected events associated with COVID-19 have impacted most business activities, especially the aviation industry, without being restricted to a single location or moment in time. Instead, there have been ongoing impacts on SCs around the world at the level of manufacturing, distribution centres, logistics and markets (Sudan and Taggar, 2021). Only a few weeks into the crisis, huge layoffs and closures had already occurred, and many airlines were financially fragile. According to ICAO, the world's air traffic had dropped to levels never seen before in history.

Furthermore, many people have died from COVID-19, wreaking further havoc on the economy, not least due to the need to lockdown cities and countries to prevent more deaths, halting manufacturing and logistics activities, affecting the supply and demand of various products (Singh et al., 2021). Notably, decisions made by one firm in an SC network directly impact the performance of other firms in today's dynamic environment (Ojha et al., 2018).

### 1.2 Supply Chain Disruption

Thus, COVID-19 has seriously disrupted SCs. Upstream SC disruptions disrupt the normal flow of goods and materials, posing a serious risk to the normal operations of downstream firms (Bode and Wagner, 2015). Transportation disruptions have undermined actual goods flows and product mobility, resulting in stalled operations, sales losses, late deliveries and reputational damage. Transportation and freight industries have also been strongly impacted (Sudan and Taggar, 2021).

# 1.3 Impact on the Aviation Industry 

To maintain operations in the pandemic context, aviation companies are increasingly forming long-term strategic partnerships with several capable suppliers, collaborating on product development, inventory control and non-core process outsourcing (Chan and Qi, 2003). Figure 1 shows that the global total number of passengers in 2021 declined between $49 \%$ and $50 \%$ compared to 2019, a direct result of COVID-19. This decrease impacts not only airlines, airports, manufacturers and air traffic management but also food and beverage producers.

World passenger traffic evolution
1945 - 2021*
![img-16.jpeg](img-16.jpeg)

Figure 1. ICAO Air Transport Reporting Form A and A_S plus ICAO estimates
The COVID-19 pandemic has depleted the travel and tourism industries, with airlines suffering their greatest losses in history and facing a period of extended uncertainty. Meanwhile, with redesigned services and stricter safety and hygiene requirements, a 'new normal' for airline catering has arrived. As passenger numbers declined in February and March, airlines lost roughly 80,000 tonnes of daily cargo capacity, requiring the use of specialised private aircrafts for freight, with such businesses adding over 20,000 tonnes to their daily capacity. Road transportation encountered various obstacles, with non-essential-sector activity drastically decreasing and other sectors, such as food retail, experiencing significant demand spikes. Nonetheless, the sector moved quickly to reorient capacity within two weeks (Chains, 2020).

In the context of airline catering, operations are usually impacted by air traffic volume. Decreased traffic reduces demand for food and beverages, considerably impacting the airline catering subsection in terms of inventory management, stock, quantity of meals ordered and

overall system processes. Most material orders are filled using a Just-in-Time (JIT) process: upon obtaining raw materials, they must be consumed or put into production according to the menu schedule. This situation requires rapid decision-making and involves the organisation's entire SC. This, along with other factors, has meant that COVID-19 has had the following notable effects on the airline catering subsector:

- Changes to hygiene, packaging, handling and on-board services;
- New approaches to menu development;
- New expectations for suppliers in the short- and medium-term;
- New employee negotiations and contracts; and
- The fallout from long-term effects on the airline industry.

Notably, during emergencies, efficient and reliable performance measurement systems are needed. Rapid evaluations must be integrated into SCs to resolve complex situations such as pandemics. From an economic and social standpoint, lockdowns cannot be considered a long-term solution, especially when a large portion of the population relies on daily wages for survival (Singh et al., 2021). Thus, planning is extremely beneficial in terms of emergency SC Management (SCM), and investing a small amount of time and resources to achieve a minimum level of preparedness can dramatically improve outcomes for vulnerable populations, reducing the impact on people and infrastructure. Most infectious threats require the same set of SC preparedness activities, and there are many resources that can help organisations prepare.

According to Walker Jaroch (2020), the COVID-19 pandemic has refocused attention on food safety best practices in the airline catering context, especially how food can be prepared and transported from the kitchen to the plane in a sanitary manner. Nonetheless, this has changed scheduling and delayed SC processes because not only surfaces but also walls, air vents, offices and logistics equipment need to be cleaned and sanitised according to new COVID-19 protocols. This includes, for example, the interior of the delivery vans: both the driver's cabin and the back of the vans or trucks, where food is stored for distribution. This has required airline caterers to develop techniques and procedures to protect the safety of their workers, partners and clients.

COVID-19's social distancing rules, sickness-related labour shortages and lockdown procedures have caused widespread problems for the food processing industry. In restricted locations, such as fruit and vegetable packing plants or meat processing plants, appropriate social distancing measures may compromise operational efficiency, and adequate staff protections are required. Many businesses have also reported high rates of employee absences;

for example, workforce availability in French meat processing plants in COVID-19-affected regions reduced by up to $30 \%$ during 2020 (Chains, 2020).

# 1.4 Research Goal 

This study aims to consider the impact of implementing Bayesian network (BN) modelling to measure SC performance in the airline catering context. These objectives can be measured using various performance indicators, depending on the focus, whether, for example, environmental, economic, social or integrative (Beske-Janssen et al., 2015). Among the goals of performance evaluation is to determine the level of functionality of an SC (Majercak, 2021). To accomplish this, it is critical to track and manage the performance of various tasks across the SC, including logistics, inventory management and warehousing, demand forecasting and supplier and customer relationship management. To this end, SC performance measurement systems enable the adoption of performance metrics that span multiple firms and processes (Maestrini et al., 2017).

These objectives have been framed in terms of the following research questions:
I. Does customer satisfaction impact SC performance in the airline catering context?
II. Does every stage in the process contribute to SC performance in the COVID-19 context?

The challenges associated with this study's inquiry are crucial for evaluating SC performance. According to Van Hoek (1998), new measurement approaches should pave the way for SC competitiveness by directing management attention to areas where SCs can be improved. This paper responds by proposing a new method for measuring SCM performance. The BN approach proposed should build on current knowledge about measuring SC performance in the airline catering context. Additionally, the performance measurement system developed can be adopted by practitioners to guide their decision-making in response to unpredictable events.

The rest of this paper is organised as follows. Section 2 reviews the current literature concerning measuring SC performance, with a focus on SCM and an emphasis on the importance of a few key issues. Section 3 proposes a BN-based performance measurement model. Section 4 describes the algorithm used to calculate performance and aggregate results Section 4, an algorithm that builds on fuzzy set theory to address the real-world measurement problem. Section 5 provides a basic demonstration of the model's application, and Section 6 concludes the paper with a summary of the performance measurement method.

# 2. Existing Performance Measurement in Supply Chain Management 

Most applied research approaches involve some measure of the performance of the developed solution (Beamon, 1999). However, the many performance measurement techniques available complicates choosing the right tool. These can be categorised according to their intended use, with examples including green SCM, sustainable SCM and SCM performance monitoring (Abolbashari et al., 2018a). Generally, performance measurement research focuses on examining existing performance measurement systems, categorising and studying performance measures within a category, and developing frameworks for developing performance measurement systems for various types of systems (Beamon, 1999). There are far too many ways to measure performance to generalise the research's findings on the link between logistics practices and performance (Majercak, 2021).

### 2.1 Traditional and Current Supply Chain Performance Measurement

Over the last year, there are quite a number of definition given to supply chain performance. Neely $(1995 ; 2005)$ refer supply chain performance measurement as a set of metrics that used to examine the efficiency and effectiveness of the action. Similarly, Tangen (2004) and Galakashi et al (2018a,b) states that performance measurement in supply chain connect with a process of quantifying effectiveness and efficiency of action. Seiler (2016) refer supply chain performance as a combination of different measure to assess and quantify the effectiveness and efficiency of action along the supply chain. As highlighted by earlier by Gopal and Thakkar (2012), there are various measurement in measuring supply chain performance such as using qualitative and quantitative measurement, supply chain operation reference (SCOR), modelling, balance scorecard and financial non-financial measures.

Current SC performance assessment methods are insufficient because they focus significantly on cost as a key (if not single) metric, are not inclusive, are frequently at odds with the organisation's strategic goals, and fail to consider the impact of uncertainty (Beamon, 1999). For instance, Gunasekaran et al (2001) recommend comprehensive framework in assessing improved operational performance in supply chain via measuring the total cash flow time, customer query time, improved relationship management activities, rate of return investment and net profit vs productivity ratio. Meanwhile, traditional indicators, which primarily concern economic issues, are insufficient for evaluating the performance of longterm SCs (Beske-Janssen et al., 2015), and because there are too many flaws, the contributions

of the performance management systems in use are discounted in the SCM context (Chan and Qi, 2003). Standard performance measurement theory has mostly concentrated on financial metrics, such as ROI, cash flow and profits (Majercak, 2021), and mostly considered shortterm applications. Notably, many organisations collect data that is solely financial and operational in nature, with various financial and operational statistics available for most organisations, including overhead expenses, income and profit. One of the reasons that organisations struggle to survive long-term is a focus on the short term. Hence, Fonseca and Azevedo (2020) have highlighted the importance of a total framework for short and long-terms to measure SC performance in various situations, for example in the pandemic of COVID-19.

Because SC performance management systems should include inter-firm performance measures, there are significant challenges in terms of integrating and sharing data from multiple firms, coordinating inter-firm processes and infrastructure and managing relationships with external SC partners throughout the assessment process. Traditional (internal) performance management systems typically target processes and data for a single firm (Maestrini et al., 2017).

The traditional approach has the disadvantages of being backwards-looking, disregarding intangible aspects and delaying information evaluation. SCs must constantly improve, especially in the COVID-19 context. To achieve this, we must improve our understanding of what makes SCs function, rather than focusing on narrow company-specific or function-specific metrics. According to Chan and Qi (2003), research concerning measuring SCM performance can be either qualitative or quantitative. For example, Beamon (1999) employs customer satisfaction and responsiveness, flexibility, supplier performance and costs to model the SC and divides indicators into three categories: resources, output and adaptability.

Apart from financial measure in measuring supply chain performance, there are many other supply chain performance measures highlights in previous research. Different industry or different organization may require different type of supply chain design, strategies and performance measurement (Beamon and Balcik, 2008; Nguyen et al., 2021). For instance, the use of Balance scorecard in measuring supply chain performance. A study from Reefke and Trocchi (2013) and Nouri et al (2019) proposed to use balance scorecard in measuring supply chain performance which only measure factors that are directly associated with supply chain strategy rather than measuring everything (Punniyamoorthy and Murali, 2008). Specifically, balance scorecard incorporate both financial and non financial measures which look at four different angles namely customer, financial, process and learning growth (Raval et al 2019). Recent study by Frederico et al (2021) proposed balance scorecard approach in measuring

supply chain performance in the Industry 4.0 era. They recommend that the four standpoint of balance scorecard support current supply chain activity in current digital era.

Given COVID-19 was considered an unexpected event in the aviation context, traditional performance measurement systems have proven unsuitable for evaluating airline catering's SC performance during this period, demanding an alternative approach capable of incorporating emergency circumstances. This is because the traditional systems cannot support the entire SC performance process, instead focusing on individual stages. Moreover, these systems often cover only a component of the SC (e.g. supplier side, customer side or internal SC activities) and employ a specific measurement scope (e.g. external partner capabilities, SC processes or connections), and the scientific literature does not provide comprehensive insight (Maestrini et al., 2017). As highlighted by Gopal and Thakkar (2012), modelling is one of the popular tool in assessing supply chain performance. This context gives rise to this paper's proposed novel performance measure-system, which adopts a BN approach to assess performance in the context of unexpected events.

# 3. Proposed Bayesian Network Modelling Approach 

This section provides a brief overview of BN theory, detailing its benefits and the justifications for using it as a modelling method to achieve performance excellence, along with indicating how it outperforms the prevalent classical models, ultimately enabling the elaboration of a performance management system for SCM.

BNs are particularly suited to assessing SC performance in the COVID-19 context because they can account for the uncertainty by measuring the SC's contingency strategies, as their widespread adoption to address system complexity and uncertainty suggests (Feng et al., 2014). Other advantages of BNs over commonly used multivariate models include their suitability for limited data situations and the fact that correlations between factors in the dataset are integrated into the probabilistic dependencies (Jensen et al., 2009). Notably, researchers have already used BNs in the SC context (Maleki and Cruz-Machado, 2013). For instance, a recent study by Seyedmohsen and Ivanov (2021) suggests that a multi-layer BN can be useful for crisis management during the pandemic by enabling the identification of SC disruption triggers and risk events. Graphical modelling features numerous advantages for data modelling when used in conjunction with statistical techniques. First, because it captures all of the interdependencies of the variables, it can easily manage scenarios with missing data. Second, a BN can learn causal linkages, allowing it to better grasp a problem area and predict intervention outcomes. Third, the model's causal and probabilistic semantics make it suitable

for mixing previous information (typically in causal form) and data. Fourth, Bayesian statistical approaches combined with BNs provide an effective and consistent way to avoid data overfitting (Heckerman, 1997).

Furthermore, the backward and forward propagation analysis involved in BN modelling is unique and advantageous for measuring the impact of different triggers of SC performance and business sustainability (Seyedmohsen and Ivanov, 2021).

# 3.1 Using Bayesian Networks to Assess Supply Chains During Emergencies 

BNs represent a probabilistic graphical method for building models using data or expert opinions, providing probabilistic and graph-theoretic models representing uncertain knowledge and reasoning (Tang and Liu, 2007). Prediction, anomaly detection, diagnostics, automated insight, reasoning, time series prediction and uncertain decision-making are just a few of the activities that they can be utilised for. BNs are probabilistic because they are constructed from probability distributions, which leads to conditional probability distributions (Abolbashari et al., 2018a). There are also probability laws for prediction and anomaly detection, reasoning and diagnostics, decision-making in response to uncertainty, and time series prediction.

BNs can also be visualised as Asia Networks (see Figure 2) and as directed acyclic graphs that combine probabilistic relationships and update probabilistic beliefs using Bayes' rule (El Amrani et al., 2021). Although neither is required to visualise the structure of a BN, they are excellent ways of understanding a model. For example, the decision relationship diagram, which includes event nodes and decision nodes, is a directed acyclic graph application developed for decision analysis with the essential responsibility of providing a proper description of the probability function. All additional computations can be conducted using symbolic operations on the probability expression upon completing the network configuration (Kang et al., 2020).

There are nodes and links in the networks. The variables of interest are represented by nodes, and the links connecting the nodes represent causal relationships between the variables (Musharraf et al., 2016). A BN is a graph with nodes connected by directed links. A variable, such as a person's height, age or gender, is represented by each node in a BN. A variable can be discrete, as in the case of gender (male or female, among other designations), or continuous, as in the case of age. The structural specification refers to the structure of the BN, which

comprises nodes and links. Adding links between nodes indicates that one node directly influences the other. Even if there is no link between two nodes, it remains possible that they are connected via other nodes. However, depending on the evidence that is established by other nodes, they may become dependent or independent.
![img-17.jpeg](img-17.jpeg)

Figure 2. Example Bayesian network for airline catering
Figure 2 shows a BN for a simulation airline catering case study. The construction process for this case study is detailed in Section 5 of this paper. Meanwhile, Table I outlines the four key analytics operations that a BN can perform: descriptive analytics, diagnostic analytics, predictive analytics and prescriptive analytics.

Table I The four major analytics procedures conducted by Bayesian networks


Prescriptive analytics should be utilised to support real-world SCM initiatives to enable the monitoring of all SC entities. Predictive analytics employs approaches and tools such as business rules, algorithms, machine learning, and computational modelling to analyse data from a range of sources, including historical and transactional data, real-time data feeds, and big datasets. However, producing prescriptive analytics is complicated, meaning most firms have not yet adopted this aspect. Nonetheless, prescriptive analytics can considerably impact how organisations make decisions and, ultimately, improve their bottom line. Meanwhile, descriptive analytics consider past events and predictive analytics forecast future events, making neither suitable for this research paper. Instead, we adopt prescriptive analytics, which have a clear objective: the delivery of guidance on possible outcomes.

# 3.2 Research Flow Diagram 

Various efforts have been made to ensure that this study meets its objectives. Figure 3 presents a flowchart detailing the research's movement from data gathering to the data analysis.
![img-18.jpeg](img-18.jpeg)

Figure 3. Research Flow Diagram

# 4. Indicators for Performance Measurement 

To reveal meaningful insights into SC performance in the pandemic context, it was critical to utilise relevant indicators for measuring performance for the particular SCs in question. These indicators needed to reflect the SC's overall performance and incorporate relevant non-financial and intangible performance components. Concerning the latter, for example, customers are paying more attention to delivery reliability and delivery frequency flexibility, which are non-financial but crucial to firm strategy in the Just-in-Time manufacturing world (Chan and Qi 2003). Given the aims and methods of each SC vary, each SC requires its own set of relevant measures. Thus, this paper proposes BN modelling to analyse the performance of airline catering SCs.

According to Chan and Qi (2003), these performance indicators should measure components that are critical to SC goals and strategies, components with inter-influence and which represent a common concern for SC partners, and components involving both internal and external partners and customers.

Furthermore, because the performance of the entire chain is aggregated in one location, processes are transparent, and complete performance data are available. At each point in an SC, the system is designed to identify and solve all potential problems, with performance metrics available to all staff. That is, every distribution centre and corporate headquarters has a wall covered in boards with graphs and tables on which the current performance indicators are displayed and updated on a regular basis, enabling all employees at all locations to see how the SC is performing compared to its defined goals (Cuthbertson and Piotrowicz, 2011).

## 5. Bayesian Network Construction

This paper's performance assessment focuses on a few key areas that pertain to three categories: input measures, output measures and composite measures (Chan and Qi, 2003)

To create a BN, it is first necessary to create a causal graphical model with a directed acyclic graph to represent the interdependencies between the various key performance indicators. Knowledge engineers who use BNs for modelling can assign belief degrees to the associated probabilities at BN nodes. Because these algorithms necessitate a large amount of data, the second method, expert opinion data collection, is commonly used (Abolbashari et al., 2018a). Although scholars have introduced numerous performance indicators (Abolbashari et al., 2018b), practitioners should be aware that most performance indicators are generic and must be tailored to their specific SC.

The second step is data gathering. The ERP system is the most reliable data source. However, because not all data is prepared in an ERP system, practitioners may need to conduct interviews with specialists to reveal tacit knowledge. Thus, the BN should be expanded to include measure reliance and independence (Pochampally et al., 2009), enabling the BN to learn from the data using unsupervised learning algorithms.

However, at this point, quality becomes a concern (Maleki and Cruz-Machado, 2013). It is necessary to examine the BN to ensure that it accurately replicates the real world before applying the model to the in-context monitoring of performance metrics.

Construction of this research's model involved following the five steps detailed by Abolbashari et al. (2018):

Step 1: Expert selection. Experts who have measured and managed SC performance are chosen. Before designating someone as an expert, an interview with each member of the knowledge management team is undertaken to determine their knowledge. A manager is deemed an expert if their expertise reaches a particular threshold.

Step 2: KPI determination. KPIs are utilised to determine which nodes make up the BN. Experts are provided a primary set of KPIs and asked to vote on the list to finalise it, using a bi-directional weighted voting approach that considers each expert's perspective. A KPI's score is included in the BN model if it surpasses a specified threshold.

Step 3: Relationship determination between KPI. This stage has two main objectives. The first stage defines the relationship between the final set of KPIs, and the second stage checks for cyclic relationships. These two objectives are pursued simultaneously rather than sequentially, which has several advantages. First, because less information is received from experts during the knowledge diffusion process, both the experts and the network function take less time. Experts are left with fewer options to choose from if they reveal their thoughts about the links in a BN in a way that leads to the formation of a cycle, eliminating the unwanted option that leads to that formation. Second, the researcher uses all of the information collected from the experts in the development of the BN, which contrasts with traditional approaches that see researchers create BNs based on expert opinions before rejecting some of the information obtained to avoid a cycle(s). The researcher may need to follow up with the experts to check the adjustments, another time-consuming process.

Step 4: Interpretation of CPT. Each child node is given a Conditional Probability Table (CPT). It is not always easy to elaborate the CPT, especially for large BNs. To complete a CPT for a child node with $n$ parents, experts must specify the probability values.

Step 5: BN Development. In phases 2 and 3, the BN model is built using algorithms. Algorithm 2 is used to design the BN's architecture after utilising the Weighted-Voting Algorithm to finalise the BN's nodes and generate pairs of nodes in line 2 of Algorithm 5.

The five steps involved in constructing a BN are presented as the framework illustrated in Figure 4.
![img-19.jpeg](img-19.jpeg)

Figure 4. BN construction steps (Abolbashari et al., 2018a)

Thus, this research's BN construction began with selecting experts for initial indicator selection. Next, indicator selection was voted on by experts based on the pool of supply chain indicators presented in Table II. The subsequent vote was combined using Dempster-Shafer, giving a result of either cycle or no cycle. When the cycle indicated a link between the two nodes, it would produce a link in the acyclic direction and all the link nodes would then be considered to constitute a CPT interpretation, with the resulting CPT table comprising an indicator's node, state and probability. These values were then utilised to construct the BN using Bayesian software, as detailed in the following subsection.

According to Hosseini and Ivanov (2019), directed acyclic graphs with a collection of nodes (variables) and a set of arcs that indicate the dependency or causal links among variables are used to graphically represent BNs. Consider the structure of a BN as a directed acyclic gap represented by G , where $G=(V, E)$, and $V=\{X 1, X 2, \ldots, X n\}$ represents a set of random variables (nodes) and E is a set of arcs (edges) (Pochampally et al., 2009). The causal relationship between $X i$ and $X j$ is represented by an inbound arc from $X i$ and $X j$, where $X i$ is the parent node of $X j$, and $X j$ is the child of $X$, implying that the likelihood of $X j$ depends on the likelihood of $X i$. As mentioned, the causal relationships between child and parent nodes can be quantified using a CPT (Pochampally et al., 2009). This set of parent nodes is generally denoted as $\pi$. The second element, $\Theta$, implies the set of parameters of the BN. Equation 1 defines the joint probability distribution of network nodes:

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi_{i}\right)=\prod_{i=1}^{n} \theta_{X_{i} \mid \pi_{i}}
$$

Equation 1

Tse et al. (2012) uses conditional probability in a Bayesian network. If the existence of some evidence B is contingent on the existence of a hypothesis A , the probability that both A and B occurred $-\mathrm{P}(\mathrm{A}, \mathrm{B})-$ is given by Equation 2 :
$\mathrm{P}(\mathrm{A}, \mathrm{B})=\mathrm{P}(\mathrm{A}) \mathrm{P}(\mathrm{B} \mid \mathrm{A})$
Equation 2

If A is relevant for B , then B must likewise be relevant for A , according to the multiplication law of probability, which describes commutativity. Figure 5 illustrates the differential BN connection.
![img-20.jpeg](img-20.jpeg)

Figure 5. Bayesian network connections. a) Serial, b) Diverging, c) Converging (Tse et al., 2012)
$\mathrm{P}(\mathrm{A}, \mathrm{B})=\mathrm{P}(\mathrm{A}) \mathrm{P}(\mathrm{B} \mid \mathrm{A})=\mathrm{P}(\mathrm{B}) \mathrm{P}(\mathrm{A} \mid \mathrm{B})$, meaning
$P(B \mid A)=\frac{P(B) P(A \mid B)}{P(A)}$
Equation 3

This study has adopted several performance variables to demonstrate the BN approach, building on recent research by the aforementioned Abolbashari et al. (2018a) along with Maleki and Cruz-Machado (2013) and Ojha et al. (2018).

The model's performance variables have been chosen based on the needs of the SC being considered and based on the managerial-level knowledge of the experts interviewed. This ultimately produced the following indicators: time, cost, customer satisfaction, quality, forecasting accuracy and supplier performance. After determining the variables, it was necessary to find links between variables in the acyclic graphical network. According to Abolbashari et al., (2018), the information listed can then be integrated using the DempsterShafer theory. Table II presents a simulation set of indicators for monitoring SC performance based on a thorough assessment of the literature.


Not all companies have to consider all of these indicators (Abolbashari et al., 2018a). A model's indicators should be chosen based on an organisation's needs, especially in the COVID-19 context. Thus, assuming the managerial knowledge of the experts, Table III presents expert voting on the pertinence of each indicator.

Table III. Expert voting on the indicators presented


In Table III, the mean of the votes for each indicator is used to generate the score value, with the threshold value $(\gamma)$ for an indicator's inclusion being 0.5 . That is, indicators were chosen if the mean vote exceeded 0.5 , leading the experts to ultimately decide on eight indicators, as listed in Table IV, alongside the possible states for each indicator.

Table IV. Final set of indicators


After deciding on the final set of indicators, the next step was determining how the indicators relate to each other. Experts were asked for their thoughts on the relationship between the various indicators. As mentioned, the data were then combined using the Dempster-Shafer theory (Abolbashari et al., 2018a), producing unique types of relationships for each pair of indicators. Meanwhile, the cycle prevention algorithm monitored expert viewpoints to prevent a cycle from forming. Figure 6 depicts the final between-indicators mapping.
![img-21.jpeg](img-21.jpeg)

Figure 6. Acyclic graphical network based on the work of Abolbashari et al. (2018a)
The final step was identifying a CPT for every node (i.e. variables). Nodes are presented in table form to provide a vision to enable easy identification of parent and child nodes, with nodes including cost, supplier performance, forecasting and procurement cycle time. Only the effectiveness node was only a child node; the other variables were both parent and child nodes.

The probability distribution for the parent nodes should also be established to complete the BN and prepare it for future analysis (Abolbashari et al., 2018a). The probability distribution value might be derived from a case study or the current state of an SC department's operations. Table V presents the probability distribution for the specified indicators. Certain probability distributions were obtained by examining how an organisation had behaved over time with regard to these performance measurement variables, and these are shown for a period of time. For example, only $40 \%$ of procurements were completed through e-procurement, and $70 \%$ of the time, the organisation failed to accurately estimate future demands, resulting in the given product or service not meeting current needs (Abolbashari et al., 2018a). The final BN model appears in Figure 6 and was created using Bayes server software.

Table V. Probability Distribution Table
![img-22.jpeg](img-22.jpeg)

Figure 7. A Bayesian network for an airline catering supply chain

# 5.1 Bayesian Network Reasoning 

Bayesian reasoning describes a statistical inference method that uses Bayes' theorem to update a hypothesis' probability when more data or information become available. BNs can reason in the face of uncertainty and update their forecast based on new data (Huang et al., 2019). This is critical when modelling the measurement of the performance of an SC using partial and iterative observations. The four types of reasoning BNs enable can help managers make decisions and better analyse their approach to assessing SC performance (Abolbashari et al., 2018a).

### 5.2 Modes of Reasoning

Four modes of reasoning (diagnostic, predictive, inter-causal and mixed) are possible in BN modelling (Abolbashari et al., 2018a). Following a brief description of each of these four types of reasoning, this section illustrates their functionality and how they may be used to assess and control SC performance. The researcher demonstrates how different types of reasoning in BNs can be employed in the context of SC performance monitoring and management to improve decision-making and sensitivity analyses (Abolbashari et al., 2018a).

Evidence is an important term for analysing BNs and updating the network. This feature allows the use of managerial-level insights to update information about various nodes in the BN network, allowing the utilisation of BNs as a visualisation tool (Abolbashari et al., 2018a).

Predictive Reasoning. The probability distribution for the child nodes can be determined using this type of reasoning, which is based on accessible information about the parent nodes. Figure 8 demonstrates the reasoning flow from top to bottom (parent nodes to child nodes). A child node may represent the BN's effectiveness (see Figure 7), and parents could be any of the immediate (e.g. quality) or non-immediate (e.g. forecasting) parent nodes. When we have information about the states of the parent nodes and want to see the degree of performance effectiveness of the SC in uncertain situations, we can use this reasoning method. We might also consider how parent nodes affect child nodes and use different values for parent nodes to establish the system's intelligence level (Abolbashari et al., 2018a). This type of analysis is known as sensitivity analysis, and it serves as a benchmark for various organisational departments, serving as an objective for their upcoming trading session. Scenario 1 explains the use of predictive reasoning in the context of assessing the performance of airline catering SCs.

![img-23.jpeg](img-23.jpeg)

Figure 8. Predictive reasoning

Scenario 1: Building on the conceptual illustration in Figure 8, this scenario exemplifies placing evidence in the parent nodes according to the organisation's current circumstances, an organisation can begin to measure its performance indicators. Consider, for instance, the procurement process performance: if we have data about the state of a node, we can input it into the model, which updates the entire network and produce an estimate of the procurement process level (Abolbashari et al., 2018a).

Meanwhile, Figure 9 demonstrates that if customer satisfaction is high, the degree of efficiency of the performance of the airline catering SC increases from $47 \%$ to $52 \%$. These data can be used to generate various outcomes. If only a small percentage of consumers (i.e. airlines) are happy with the level of service they receive, an airline caterer can consider how much its total performance would improve if dissatisfied customers were completely satisfied. The BN model's evidence-consideration feature is not restricted to one indicator. The outcomes for the other four parent indicators were as follows: High for cost, Reasonable for procurement cycle time, High for forecasting and Low for supplier performance (due to COVID-19-related strikes). As an example of how this latter result appears in the real world, suppliers must undergo extra processes before delivering raw materials to the airline catering stores, complicating supplier ability to deliver goods on time.

![img-24.jpeg](img-24.jpeg)

Figure 9. The Bayesian network's evidence-consideration feature

Diagnostic Reasoning. This reasoning method moves from effects to causes, with specific circumstances constituting evidence for child nodes, and beliefs about parent nodes being consequently modified. When we desire a specific degree of airline catering SC effectiveness and want to know how to achieve that, we can use this reasoning method, making it extremely beneficial to a company's strategic planning. If an organisation aspires to a given level of performance, the network will be updated and presented with a set of steps to achieve that goal. Scenario 2 elaborates on this application.

![img-25.jpeg](img-25.jpeg)

Figure 10. Diagnostic reasoning
Scenario 2: Building on the conceptual illustration in Figure 10, this scenario indicates that the current efficiency status is ineffective (a likely value of $47 \%$ ). Assuming that the company wants efficiency to achieve $100 \%$ efficiency, the BN will automatically update the entire network from bottom to top with the updated required values for the indicators whenever this desired level of performance is inserted into the model as proof, as Figure 11 illustrates. The revised values of the indicators reflect the changes that the organisation has to make for each indicator. Diagnostic reasoning enables determination of the types of modifications required.
![img-26.jpeg](img-26.jpeg)

Figure 11a.. Diagnostic reasoning helps improve efficiency
In the case study, the following improvements for each indicator were required for the airline catering SC to achieve efficiency: costs should be $60 \%$ lower, procurement cycle time must be reasonable $52 \%$ of the time, the supplier must achieve a $60 \%$ better performance, and forecasting must be $60 \%$ more accurate.

![img-27.jpeg](img-27.jpeg)

Figure 11b. Diagnostic reasoning helps improve efficiency
Inter-causal Reasoning. Once we establish the true status of one of a node's parents, we can measure the status of another parent (Abolbashari et al., 2018b). When access to the values of all effective variables is not possible, this feature is extremely crucial for procurement. Various factors, such as the confidential nature of some information, the time delay in obtaining the requested information, and the unwillingness of some departments to share information due to internal competition among departments at the same hierarchical level, may all contribute to this inaccessibility. Scenario 3 elaborates on this situation.
![img-28.jpeg](img-28.jpeg)

Figure 12. Inter-causal reasoning

Scenario 3: Building on the conceptual illustration in Figure 12, this scenario exemplifies the inter-causal reasoning method in the context of measuring the performance of airline catering SCs. Given reasonable evidence for the states of quality and forecasting are

available, information or the level of supplier performance is updated by inputting this data into the BN model, as Figure 12 demonstrates.
![img-29.jpeg](img-29.jpeg)

Figure 13. Inter-casual reasoning in the context of measuring the performance of airline catering supply chains
The information available does not provide an estimate of the supplier's contribution to SC performance. By obtaining information about the two other nodes, the BN increases our knowledge and grasp of the supplier's true performance level, which we now know is $72 \%$ rather than $40 \%$. Not only can the BN be used to evaluate customer performance, it can also be used to evaluate supplier performance. This BN characteristic is advantageous and can be utilised to assess SC partners. When we do not have or will not have information about the state of a given node, we can use inter-causal reasoning to approximate the state of that node (Abolbashari et al., 2018b).

Combined Reasoning. The final reasoning method BNs enable considers the state of a node with the states of both parent and child nodes visible simultaneously. Scenario 4 briefly exemplifies how combined reasoning functions.
![img-30.jpeg](img-30.jpeg)

Figure 14. Combined reasoning
Scenario 4: Building on the conceptual illustration in Figure 14, this scenario shows how a BN can examine the effect of evidence at both the parent and child of a node simultaneously (see Figure 15). When the only information available is about the status of forecasting (for example, High accuracy), we know that the evidence will be of higher quality. If there is also information about customer satisfaction (for example, High), this evidence will also update our information about the quality level. In fact, combined reasoning represents a hybrid of diagnostic and predictive reasoning. Combined reasoning approaches a specific node from two directions. When information concerning forecasting accuracy is available, the BN first offers information about the quality level (Abolbashari et al., 2018b).
![img-31.jpeg](img-31.jpeg)

Figure 15. Combination Reasoning of customer satisfaction and high accuracy forecasting

When there is also information available for customer satisfaction, the BN provides more detailed and up-to-date information about the quality level in the second attempt. Consequently, simultaneously having information about a node's parent and child enables combined reasoning to derive information about the state of a node (Abolbashari et al., 2018b).

The simulation case study produced enables the elaboration of a way for airline catering organisations to utilise BNs to measure and improve SC performance.

# 5.3 Interpreting the Findings 

It is acknowledged that COVID-19 has produced many issues, including travel restrictions, economic crises, decreased passenger demand, significantly decreased aircraft service demand and changes to passenger behaviour. For instance, according to the International Air Transport Association, the drop in economic activity and commerce impacted freight about $30 \%$ year-on-year in April 2020, with the impact remaining around $12 \%$ in August of the same year (OECD, 2020). Meanwhile, passenger air transport, as measured by revenue per passenger kilometre, had decreased $90 \%$ year-on-year in April 2020 and remained down $75 \%$ in August 2020. The pandemic has affected almost every sector in the aviation organisation: airlines, airports and airline catering organisations. Changes in passenger demand for in-flight meals disrupting SCs has represented a key challenge for airline catering organisations. This empirical study has mapped the current performance of airline catering SCs using key performance indicators in a BN that airline caterers can use to improve their decisionmaking processes, improve their SC performance and achieve sustainability. This study's findings make a significant theoretical and practical contributions to the bodies of knowledge about SC performance measurement and the airline catering sector.

By implementing BN modelling to analyse airline catering SC performance in the COVID-19 context, managers and executives can identify which performance indicators most impact their organisation's SC performance (Rabbi et al., 2020). Managers and experts can monitor current SC performance according to the current performance level of each performance indicator, helping them to understand the organisation's current relative position in the industry. According to Rabbi et al. (2020), managers can use diagnostic analyses to determine the target performance indicator levels needed to obtain satisfactory overall results.

Notably, Scenario 4 demonstrates that customer (i.e. airline) satisfaction may impact airline catering SCs. When the data is available to update BNs for customer satisfaction, the quality node will demonstrate a quantitative, which depends on the satisfaction level of the customer. If the customer displays a high level of satisfaction, the quality improves. However,

most managers have limited resources for monitoring, prioritising and optimising customer satisfaction to substantially help achieve an SC's performance goals.

Every stage in a BN is strongly linked. When one data point is added to the model, it changes other data points, impacting the overall results. For example, in the scenario mentioned above, each parent and child node contributes to the performance of the other parent and child nodes. Adding forecasting and customer satisfaction data can change the performance quality of an airline catering SC, especially in the pandemic context, in which core analysis is important for remaining sustainable. Given this research is solely focused on the airline catering SC performance perspective, future scholars should empirically investigate SC performance in other aviation sub-sectors (e.g. airline, airport, cargo operation, ground handling, and maintenance, repair and overhaul).

# 5.4 Theoretical and Managerial Implications 

This study's findings make a few important theoretical contributions. First, the BN approach enables identification of different performance measures, including customer satisfaction, quality, procurement performance, future forecasting, efficiency and effectiveness As highlighted by previous research, there are many tools to examine supply chain performance measurement such as balance scorecard (Frederico, 2021), financial performance (Galankashi and Rafiei, 2021)benchmarking (Wong and Wong, 2008), non-financial performance (Beamon and Balcik, 2008), SCOR or supply chain operation reference (Nguyen et al., 2021; Agarwal et al., 2006), as well as modelling (Euchi et al 2018). This study adopts Bayesian modelling network in measuring supply chain performance in airline catering context. This study extends current literature on both Bayesian Network Modelling (BN) method and supply chain performance measurement literature. Specifically, this study provide useful information of using BN in measuring supply chain performance. The BN construction steps shares in this study provide useful guidelines and references for future scholar to conduct supply chain performance study using BN method. In fact, an exploration of supply chain performance in rarely explored sector which is airline catering context in this research bridge the literature gap. As recommended by Kamble and Gunasekaran (2019), more study from different method such as BN method use in measuring supply chain performance would give meaningful insight to the scholars in the field. Additionally, the detail discussion provided in this study provide opportunities for future scholars to adopt the same method in examining the same issue in different context. Additionally, this study also enhances BN literature with investigating supply

chain performance in rarely explored field, airline catering. Compared to previous research on BN, many study are focusing on supply chain risk assessment (Zhou et al 2022; Cao et al 2019 humanitarian supply chain performance ( Lu and Zhang, 2022) and others.
Second, this research's measurement of performance using BNs represents a novel method of evaluating SC performance in the pandemic context, simulating disruptions and their consequences on the performance of airline catering SCs. The eight variables which represent the nodes in BN in this study from airline catering perspectives namely quality, forecasting, effectiveness, supplier performance, procurement cycle time, customer satisfaction, cost and efficiency enhance the supply chain performance measurement literature.

Third, this paper's contribution builds on applications of BNs, with the research design proposing a viable framework for using probabilistic interdependency modelling to capture the complexity and uncertainty in SC networks. This study fills a gap in the current body of knowledge with utilizing BN method in examining supply chain performance measurement in current pandemic era. This modelling approach offers a one-of-a-kind capacity for modelling interconnected risks in a network (Ojha et al., 2018). Understanding the complex behaviours of a risk is compounded by the sensitivity of risk exposure at different nodes with varying inventory and backup levels. Discussion provided in this study provide a comprehensive information for future research to carry out similar study using BN method.
Meanwhile, in terms of practical applications, using BN reasoning methods can help managers evaluate performance monitoring and management to ultimately improve decision-making and sensitivity analysis. By implementing BN modelling to analyse airline catering SC performance in the COVID-19 context, managers and executives can identify which performance indicators most impact their organisation's SC performance. In this work, Bayesian Network reasoning was used to support the BN analysis in this study. 'Evidence' has been identified as an important notion in BN analysis and network updating. The features assist and enable practitioners to update information about various nodes (variables) in the BN, allowing for improved analysis when utilizing the BN as a visualisation tool. For instance, as in COVID-19 situation, by implementing the diagnostic reasoning to the analysis, the reasoning enables determination of the types of modifications required. Practitioners could benefit this reasoning when an organisation aspires to a given level of performance efficiency. Therefore, as result of action, suppliers must undergo extra processes before delivering raw materials to the airline catering stores, complicating supplier ability to deliver goods on time. Thus, by analyzing the benefit of BN modelling to the supply chain performance, this paper has shown

every stage in the process contribute to the SC performance, especially in the COVID-19 context.

# 6. Conclusion 

This paper has detailed the significant flaws in current performance measurement methods, particularly in terms of SCM. This paper proposes using BNs to measure the performance of airline catering SCs in the COVID-19 context - a context entailing many uncertainties in terms of decision-making - to ultimately improve SCM. The paper has detailed existing SC performance measurement approaches, the proposed BN modelling method, the construction of the BN are outlined and some suggested applications. Building on previous studies, this paper highlights several additional effects. For example, rather than using historical values of an outcome, the temporal impacts between leading indicators and a lagging outcome are captured to produce a lower predicting error. Meanwhile, the paper presents the BN construction framework adapted from the extant literature, broadening the current body of knowledge to improve SC performance measurement systems in the airline catering context. Although certain issues may not have been completely eradicated by the BN approach, these issues can be significantly minimized by the more comprehensive and realistic risk assessment and more dynamic and adaptive risk management offered by BNs. This can contribute to the substantial efforts currently directed towards recovering from the pandemic and building a more robust system capable of withstanding future crises. Future research are also suggested to look at BN method in assessing supply chain performance in humanitarian context.

This research also features certain limitations that can be used to drive future research. These include the lack of prior research on BNs in the airline catering context. Furthermore, this model application only analysed a small number of risk variables; thus, future studies could consider various other risk variables that affect different nodes and linkages between nodes.

# References 

Abolbashari, M.H., Chang, E., Hussain, O.K. and Saberi, M. (2018b), 'Smart Buyer: a Bayesian Network modelling approach for measuring and improving procurement performance in organisations', Knowledge-Based Systems, Vol. 142, pp. 127-148. https://doi.org/10.1016/j.knosys.2017.11.032
Agarwal, A., Shankar, R. and Tiwari, M.K. (2006), "Modeling the metrics of lean, agile and leagile supply chain: an ANP-based approach", European Journal of Operational Research, Vol. 173 No. 1, pp. 211-25.
Badulescu, Y., Hameri, A.P. and Cheikhrouhou, N. (2021), 'Evaluating demand forecasting models using multi-criteria decision-making approach', Journal of Advances in Management Research, Vol. 18, No. 5, pp. 661-683. https://doi.org/10.1108/JAMR-05-2020-0080
Beamon, B.M. (1999), 'Measuring supply chain performance', International Journal of Operations and Production Management, Vol. 19 No. 3. https://doi.org/10.1108/01443579910249714
Beamon, B. M. and Balcik, B. (2008), "Performance measurement in humanitarian relief chains", International Journal of Public Sector Management, Vol. 21 No.1, pp. 4-25. .
Beck, P. and Hofmann, E. (2012), 'Multiple criteria decision making in supply chain management - currently available methods and possibilities for future research', Die Unternehmung, Vol. 66 No. 2, pp. 180-213. https://doi.org/10.5771/0042-059x-2012-2180
Beske-Janssen, P., Johnson, M.P. and Schaltegger, S. (2015), '20 years of performance measurement in sustainable supply chain management - what has been achieved? Supply Chain Management, Vol. 20 No. 6, pp. 664-680. https://doi.org/10.1108/SCM-06-20150216
Bode, C. and Wagner, S.M. (2015), 'Structural drivers of upstream supply chain complexity and the frequency of supply chain disruptions', Journal of Operations Management, Vol 36, pp. 215-228. https://doi.org/10.1016/j.jom. 2014.12 .004
Cao, Shoufeng; Bryceson, Kim and Hine, Damian (2019), "An Ontology-based Bayesian network modelling for supply chain risk propagation", Industrial Management \& Data Systems, Vol. 119 No.8, pp.1691-1711. doi:10.1108/imds-01-2019-0032
Chains, F.S. (2020), 'Comparing crises: Great Lockdown versus Great Recession', Comparing Crises: Great Lockdown versus Great Recession, June, pp. 1-11. https://doi.org/10.4060/ca8833en
Chan, F.T.S. and Qi, H.J. (2003), 'An innovative performance measurement method for supply chain management', Supply Chain Management, Vol. 8 No. 3, pp. 209-223. https://doi.org/10.1108/13598540310484618
Cuthbertson, R. and Piotrowicz, W. (2011), 'Performance measurement systems in supply chains: a framework for contextual analysis', International Journal of Productivity and Performance Management, Vol. 60 No. 6, pp. 583-602. https://doi.org/10.1108/17410401111150760
El Amrani, S., Ibne Hossain, N.U., Karam, S., Jaradat, R., Nur, F., Hamilton, M.A. and Ma, J. (2021), 'Modelling and assessing sustainability of a supply chain network leveraging multi Echelon Bayesian Network', Journal of Cleaner Production, 302. https://doi.org/10.1016/j.jclepro.2021.126855
Euchi, Jalel; Bouzidi, Dalel; Bouzid, Zahira (2018). Interpretive Structural Modeling Technique to Analyze the Interactions Between the Factors Influencing the Performance of the Reverse Logistics Chain. Global Journal of Flexible Systems Management, (), doi:10.1007/s40171-018-0200-1

Feng, N., Wang, H.J. and Li, M. (2014), 'A security risk analysis model for information systems: causal relationships of risk factors and vulnerability propagation analysis', Information Sciences, Vol. 256, pp. 57-73. https://doi.org/10.1016/j.ins.2013.02.036
Fonseca, L. and Azevedo A., (2020), "COVID- 19: outcomes for Global Supply Chains", Management \& Marketing. Challenges for the Knowledge Society, Vol. 15, No. Special Issue, pp. 424-438, DOI: 10.2478/mmcks-2020-0025.
Frederico, G. F., Garza-Reyes, J. A., Kumar, A., and Kumar, V. (2021). Performance measurement for supply chains in the Industry 4.0 era: a balanced scorecard approach. International Journal of Productivity and Performance Management, vol. 70, no.4, pp. 789807.

Galankashi, M.R., Fallahiarezoudar, E., Moazzami, A., Helmi, S.A., Rohani, J.M. and Yusof, N.M. (2018a), "An efficient integrated simulation-Taguchi approach for sales rate evaluation of a petrol station", Neural Computing and Applications, Vol. 29 No. 4, pp. 1073-1085.
Galankashi, M.R., Helmi, S.A., Hisjam, M. and Rahim, A.R.A. (2018b), "Leanness assessment in automotive industry: case study approach", International Journal of Value Chain Management, Vol. 9 No. 1, pp. 70-88.
Galankashi, M. R. and Rafiei, F. M. (2021). Financial performance measurement of supply chains: a review. International Journal of Productivity and Performance Management.
Gunasekaran, A., Patel, C. and Tirtiroglu, E. (2001), "Performance measures and metrics in a supply chain environment", International Journal of Operations and Production Management, Vol. 21 Nos 1-2, pp. 71-87, doi: 10.1108/01443570110358468.
Gopal, P. R. C. and Thakkar, J. (2012). A review on supply chain performance measures and metrics: 2000-2011. International journal of productivity and performance management.Vol.61, no.5, pp. 518-547.
Heckerman, D. (1997), 'Bayesian Networks for Data Mining', Data Mining and Knowledge Discovery, Vol. 1, 79-119.
Ho, W., Xu, X. and Dey, P. K. (2010), 'Multi-criteria decision making approaches for supplier evaluation and selection: a literature review', European Journal of Operational Research, Vol. 202 No. 1, pp. 16-24. https://doi.org/10.1016/j.ejor.2009.05.009
Hosseini, S. and Ivanov, D. (2019), 'A new resilience measure for supply networks with the ripple effect considerations: a Bayesian network approach', Annals of Operations Research. https://doi.org/10.1007/s10479-019-03350-8
Hosseini, S. and Ivanov, D. (2021), 'A multi-layer Bayesian network method for supply chain disruption modelling in the wake of the COVID-19 pandemic', International Journal of Production Research. https://doi.org/10.1080/00207543.2021.1953180
Huang, L., Cai, G., Yuan, H. and Chen, J. (2019), 'A hybrid approach for identifying the structure of a Bayesian network model', Expert Systems with Applications, Vol. 131 No. 814, pp. 308-320. https://doi.org/10.1016/j.eswa.2019.04.060
Jensen, K.L., Toftum, J. and Friis-Hansen, P. (2009), 'A Bayesian Network approach to the evaluation of building design and its consequences for employee performance and operational costs', Building and Environment, Vol. 44 No. 3, pp. 456-462. https://doi.org/10.1016/j.buildenv.2008.04.008
Kang, L., Chu, Y., Leng, K. and Van Nieuwenhuyse, I. (2020), 'Construction of fast retrieval model of e-commerce supply chain information system based on Bayesian network', Information Systems and E-Business Management, Vol. 18 No. 4, pp. 705-722. https://doi.org/10.1007/s10257-018-00392-6
Khan, S.A., Chaabane, A. and Dweiri, F.T. (2018), 'Multi-criteria decision-making methods application in supply chain management: a systematic literature review. Multi-Criteria Methods and Techniques Applied to Supply Chain Management, June. https://doi.org/10.5772/intechopen. 74067

Maestrini, V., Luzzini, D., Maccarrone, P. and Caniato, F. (2017), 'Supply chain performance measurement systems: a systematic review and research agenda', International Journal of Production Economics, Vol. 183, pp. 299-315. https://doi.org/10.1016/j.ijpe.2016.11.005
Majercak, P. (2021), 'Design of a supply chain performance monitoring system for a company in the context of the COVID-19 pandemic', SHS Web of Conferences, 92, 01028. https://doi.org/10.1051/shsconf/20219201028
Maleki, M. and Cruz-Machado, V. (2013), 'Supply chain performance monitoring using Bayesian network', International Journal of Business Performance and Supply Chain Modelling, Vol. 5 No. 2, pp. 177-197. https://doi.org/10.1504/IJBPSCM.2013.053492
Musharraf, M., Smith, J., Khan, F., Veitch, B. and MacKinnon, S. (2016), 'Assessing offshore emergency evacuation behavior in a virtual environment using a Bayesian Network approach', Reliability Engineering and System Safety, Vol. 152, pp. 28-37. https://doi.org/10.1016/j.ress.2016.02.001
Neely, A. (2005), "The evolution of performance measurement research: developments in the last decade and a research agenda for the next", International Journal of Operations \& Production Management, Vol. 25 No. 12, pp. 1264-77.
Neely, A., Gregory, M. and Platts, K. (1995), "Performance measurement system design: a literature review and research agenda", International Journal of Operations \& Production Management, Vol. 15 No. 4, pp. 80-116, reprinted in International Journal of Operations \& Production Management, Vol. 25 No. 12, 2005, pp. 1228-63.
Nguyen, T. T. H., Bekrar, A., Le, T. M., \& Abed, M. (2021, May). Supply Chain Performance Measurement using SCOR Model: a Case Study of the Coffee Supply Chain in Vietnam. In 2021 1st International Conference On Cyber Management And Engineering (CyMaEn) (pp. 1-7). IEEE.
, F.A., Nikabadi, M.S. and Olfat, L. (2019), "Developing the framework of sustainable service supply chain balanced scorecard (SSSC BSC)", International Journal of Productivity and Performance Management, Vol. 68 No. 1, pp. 148-170, doi: 10.1108/IJPPM-04-20180149 .
Ojha, R., Ghadge, A., Tiwari, M.K. and Bititci, U.S. (2018), 'Bayesian network modelling for supply chain risk propagation', International Journal of Production Research, Vol. 56 No. 17, pp. 5795-5819. https://doi.org/10.1080/00207543.2018.1467059
Parthiban, P., Zubar, H.A. and Garge, C. P. (2012), 'A multi criteria decision making approach for suppliers selection', Procedia Engineering, Vol. 38, pp. 2312-2328. https://doi.org/10.1016/j.proeng.2012.06.277
Paul, A., Shukla, N., Paul, S.K. and Trianni, A. (2021), 'Sustainable supply chain management and multi-criteria decision-making methods: a systematic review', Sustainability (Switzerland), Vol. 13 No. 13. https://doi.org/10.3390/su13137104
Pochampally, K.K., Gupta, S.M. and Govindan, K. (2009), 'Metrics for performance measurement of a reverse/closed-loop supply chain', International Journal of Business Performance and Supply Chain Modelling, Vol. 1 No. 1, pp. 8-32. https://doi.org/10.1504/IJBPSCM.2009.026263
Punniyamoorthy, M. and Murali, R. (2008), "Balanced score for the balanced scorecard: a benchmarking tool", Benchmarking: An International Journal, Vol. 15 No. 4, pp. 420443.

Rabbi, M., Ali, S.M., Kabir, G., Mahtab, Z. and Paul, S.K. (2020), 'Green supply chain performance prediction using a Bayesian belief network', Sustainability (Switzerland), Vol. 12 No. 3, pp. 1-19. https://doi.org/10.3390/su12031101
Citation
Raval, S.J., Kant, R. and Shankar, R. (2019), "Benchmarking the Lean Six Sigma performance

measures: a balanced score card approach", Benchmarking: An International Journal, Vol. 26 No. 6, pp. 1921-1947. https://doi
Reefke, H. and Trocchi, M. (2013), "Balanced scorecard for sustainable supply chains: design and development guidelines", International Journal of Productivity and Performance Management, Vol. 62 No. 8, pp. 805-826, doi: 10.1108/IJPPM-02-2013-0029.
Saraswati, C.L. (2018), 'Strategic procurement practices through deep supplier relationships and exchange of valuable knowledge at pt aerofood indonesia: a study at Aerofood ACS Unit Denpasar', Jurnal Administrasi Bisnis, Vol 58 No. 2, pp. 11-20.
Seiler, A.C. (2016), Measuring Performance in Supply Chain Networks, Doctoral dissertation, University of Salford.
Singh, S., Kumar, R., Panchal, R., Manoj, K. and Tiwari, M.K. (2021), 'Impact of COVID-19 on logistics systems and disruptions in food supply chain', International Journal of Production Research, Vol. 59 No. 7. https://doi.org/10.1080/00207543.2020.1792000
Sivakumar, G., Almehdawe, E. and Kabir, G. (2022), 'Developing a decision-making framework to improve healthcare service quality during a pandemic', Applied System Innovation, Vol. 5 No. 1, pp. 1-21.
Sudan, T. and Taggar, R. (2021), 'Recovering Supply Chain Disruptions in Post-COVID-19 Pandemic Through Transport Intelligence and Logistics Systems: India's Experiences and Policy Options', Frontiers in Future Transportation, Vol. 2. https://doi.org/10.3389/ffutr.2021.660116
Tang, H. and Liu, S. (2007), 'Basic theory of fuzzy Bayesian networks and its application in machinery fault diagnosis', Proceedings - Fourth International Conference on Fuzzy Systems and Knowledge Discovery, FSKD 2007, 4(Fskd), 132-137. https://doi.org/10.1109/FSKD.2007.202
Tangen, S. (2004), "Performance measurement: from philosophy to practice", International Journal of Productivity and Performance Management, Vol. 53 No. 8, pp. 726-737
Tse, H., Chow, K.P. and Kwan, M. (2012), 'Reasoning about evidence using Bayesian networks', IFIP Advances in Information and Communication Technology, 383 AICT, 99113. https://doi.org/10.1007/978-3-642-33962-2_7

Van Hoek, R.I. (1998), 'Measuring the immeasurable' - measuring and improving performance in the supply chain', Supply Chain Management, Vol. 3 No. 4, pp. 187-192. https://doi.org/10.1108/13598549810244232
Zaim, H., Ramdani, M. and Haddi, A. (2016), 'Multi-criteria analysis approach based on consumer satisfaction to rank B2C E-commerce websites', SITA 2016 - 11th International Conference on Intelligent Systems: Theories and Applications. https://doi.org/10.1109/SITA.2016.7772260
Zhou, Y., Li, X., and Yuen, K. F. (2022), "Holistic risk assessment of container shipping service based on Bayesian Network Modelling", Reliability Engineering \& System Safety, 220, 108305 .
Žic, J. and Žic, S. (2020), 'Multi-criteria decision making in supply chain management based on inventory levels, environmental impact and costs', Advances in Production Engineering And Management, Vol. 15 No. 2, pp. 151-163. https://doi.org/10.14743/APEM2020.2.355