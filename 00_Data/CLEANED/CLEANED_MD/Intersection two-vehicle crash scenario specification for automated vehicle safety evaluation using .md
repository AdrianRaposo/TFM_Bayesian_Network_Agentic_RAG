# Intersection Two-Vehicle Crash Scenario Specification for Automated Vehicle Safety Evaluation Using Sequence Analysis and Bayesian Networks 

$\left[\right.$ Preprint ${ }^{1 *}$<br>Yu Song ${ }^{1}$, Madhav V. Chitturi², David A. Noyce ${ }^{2}$

1. University of Connecticut, 2. University of Wisconsin-Madison


#### Abstract

This paper develops a test scenario specification procedure using crash sequence analysis and Bayesian network modeling. Intersection two-vehicle crash data was obtained from the 2016-2018 National Highway Traffic Safety Administration (NHTSA) Crash Report Sampling System (CRSS) database. Vehicles involved in the crashes are specifically renumbered based on their initial positions and trajectories. Crash sequences are encoded to include detailed pre-crash events and concise collision events. Based on sequence patterns, the crashes are characterized as 55 types. A Bayesian network model is developed to depict the interrelationships among crash sequence types, crash outcomes, human factors, and environmental conditions. Scenarios are specified by querying the Bayesian network's conditional probability table. Distributions of operational design domain (ODD) attributes (e.g., driver behavior, weather, lighting condition, intersection geometry, traffic control device) are specified based on conditions of sequence types. Also, distribution of sequence types is specified on specific crash outcomes or combinations of ODD attributes.


Keywords: motor vehicle crash; test scenario; sequence of events; operational design domain; probabilistic graphical model

[^0]
[^0]:    *Preprint, final version to be published in Accident Analysis and Prevention.
    Please direct questions to the corresponding author, Y. Song, email: fred.song@uconn.edu.

# 1 Introduction 

Scenario-based testing is an essential part of automated vehicle (AV) safety evaluation, and generating challenging scenarios is critical for such testing (Koopman \& Wagner, 2016; Riedmaier et al., 2020). Historical crash data consists of challenging scenarios faced by human drivers and is a good source of data for developing test scenarios that may also be challenging for AVs (Najm et al., 2007; Nitsche et al., 2017; Scanlon et al., 2021). As advanced driving assistance systems (ADAS) and automated driving systems (ADS) are developed to replace human drivers partially or fully, it is reasonable to expect AVs to have the capabilities to handle challenging scenarios faced by human drivers and mitigate crash outcomes. Therefore, by mining data of crashes involving human-driven vehicles, we would be able to generate safety-critical scenarios to test the capabilities of AVs in handling interactions with human-driven vehicles. The same approach can also be used to extract safety-critical scenarios from data of AV-involved crashes and generate scenarios to test AV interactions with other AVs (Song, 2021; Song et al., 2021).

Prior efforts in developing test scenarios using historical crash data have developed characterization of crashes to be used as representative scenarios for the evaluation of ADAS or ADS. The crash characterization was developed by summarizing and mining patterns in crash attributes (Najm et al., 2007; Nitsche et al., 2017; Sander \& Lubbe, 2018; Sui et al., 2019; Watanabe et al., 2019; Esenturk et al., 2021, 2022). The end products from prior efforts - representative scenarios - lack considerations of crash progression, dynamics, and mechanisms, which are important information to distinguish crashes and their outcomes (Song et al., 2021; Wu et al., 2016).

The objective of this paper is to propose a crash-data-based scenario generating procedure that improves crash characterization and scenario specification by employing crash sequence analysis and Bayesian network modeling. Prior studies have defined scenario as a sequence of scenes, which include actions and interactions between moving objects, as well as the surrounding environment (Ulbrich et al., 2015). Layered models of potentially needed elements for scenario specification has been proposed by AV safety evaluation projects such as PEGASUS, which has a layer of moving object actions and interactions, and several other layers for elements in the surrounding environment (Sauerbier et al., 2019). In this study, a crash scenario is defined as crash sequence + description of the operational design domain (ODD). Crash sequence analysis generates informative crash sequence types that describe crash dynamics and progression. Bayesian network modeling provides a model of crash mechanisms. The two analyses together enable the specification of crash scenarios depicted by the actions and interactions of moving participants, crash outcomes, and ODD variables including physical environmental conditions and human factors.

In this paper, we focus on applying the scenario generating procedure to intersection two-vehicle crashes. The reasons are: 1) intersection two-vehicle crashes are prevalent, making up more than a quarter of all crashes on United States roadways, and 2) intersection two-vehicle crashes contain complex interactions (both vehicle-vehicle and vehicle-environment) that need to be tested for AV safety proving. Crash data was obtained from the 2016-2018 Crash Report Sampling System (CRSS) of the United States National Highway Traffic Safety Administration (NHTSA). Following this section: Section 2: A literature review summarizing key literature in scenario generation using historical crash data, crash sequence analysis, and application of Bayesian networks in crash analysis. Section 3: Description of the CRSS data, special data preparation for scenario development, crash sequence data processing techniques, and other crash attributes used in modeling. Section 4: Explanation of methods employed in the scenario generating procedure. Section 5: Results of crash characterization based on sequences, Bayesian network modeling of variable dependencies, and a demonstration of scenario specification process. Section 6: Discussion and conclusion.

## 2 Literature Review

### 2.1 Scenario Generation Using Historical Crash Data

Historical crash data has been used to generate scenarios for different purposes, such as general vehicle safety testing, evaluation of crash avoidance systems, ADAS, and ADS (Najm et al., 2007; Aust, 2010; Kusano

\& Gabler, 2012, 2013; Lenard et al., 2014; MacAlister \& Zuby, 2015; Nitsche et al., 2017; Sander \& Lubbe, 2018; Sui et al., 2019; Watanabe et al., 2019; Scanlon et al., 2021). Some prior research developed a comprehensive set of scenarios that cover as many crash types and ODDs as possible, using a national-level crash database and by summarizing crash attributes (Najm et al., 2007). Most prior studies focused on some specific types of crashes and extracted or characterized crash scenarios using national-level crash databases (Kusano \& Gabler, 2012, 2013; Lenard et al., 2014; MacAlister \& Zuby, 2015; Nitsche et al., 2017; Sander \& Lubbe, 2018; Sui et al., 2019). Several studies proposed systematic methodologies to characterize crashes and specify representative scenarios (Aust, 2010; Nitsche et al., 2017; Watanabe et al., 2019). A most recent Waymo LLC study used municipal-level crash report census data to reconstruct crash scenarios in simulations for AV safety evaluation (Scanlon et al., 2021).

# 2.2 Crash Sequence Analysis 

Crash sequences are chronologically ordered events that happened during the pre-crash and crash periods. Crash sequence analysis has a similar purpose with sequence analysis in biological and sociological research, focusing on identifying representative components of sequences, the similarity (or dissimilarity) between sequences, and the relationship between sequences and potential outcomes (Wu et al., 2016).

Prior studies on crash sequence analysis are limited. Krull et al. found significant relationships between the order of rollover and fixed-object collision events and single-vehicle crash injury severity outcomes (Krull et al., 2000). Wu et al. adapted sequence analysis methods from biological and sociological research to fatal single-vehicle run-off-road crash data, characterized crashes and found significant relationship between crash sequence types and crash injury severity outcomes (Wu et al., 2016). Song et al. used sequence analysis to characterize California AV crash sequences, found significant association between crash sequence types and multiple crash attributes, and proposed a scenario-based AV evaluation framework with crash sequences as the core component (Song et al., 2021). In more recent research, a methodology was developed for crash sequence analysis that could help select optimal techniques (e.g., sequence encodings, dissimilarity measures) for multiple different use cases in studying crashes (Song, 2021; Song et al., 2022). A case study of interstate single-vehicle crash characterization was used to demonstrate the effectiveness and usefulness of the proposed methodology.

### 2.3 Bayesian Networks for Crash Analysis

Bayesian networks are graphical models known for their use in revealing variable dependencies, and are widely applied in artificial intelligence, medical, and genetic research (Pearl, 2009). Prior applications of Bayesian networks in traffic crash research focused on crash forensics, estimating effects of contributing factors on crash outcomes, and predicting crash outcomes (Davis, 2001, 2003; Davis et al., 2011; de Oña et al., 2013; Ma et al., 2018; Prati et al., 2017; Zhu et al., 2017; Zong et al., 2019; Zou \& Yue, 2017). With large samples of crash data, Bayesian networks were shown to be effective in identifying complex interrelationships among multiple crash attributes and crash outcomes (de Oña et al., 2013; Prati et al., 2017).

## 3 Data

Crash data from the NHTSA CRSS database was used in this study. The CRSS is a United States crash database with crash data extracted from nationally sampled crash reports (NHTSA, 2018). A total of about 150,000 crash observations were included in the 2016-2018 CRSS crash data, representing about 20 million police-reported crashes. The CRSS database organizes data into crash, vehicle, person, and event levels. The four levels of data can be linked through unique IDs for crashes, vehicles, and persons. In this paper, the crash, vehicle, and event level data files were used.

# 3.1 Subsetting 

Since intersection two-vehicle crashes were the focus of this paper, a subset of crashes of the 20162018 CRSS data was obtained by applying the criteria listed in Table 1. The criteria ensured a data set consisting of intersection two-vehicle crashes involving only passenger vehicles in motion. Crashes that involved emergency vehicles, were alcohol-related or happened at locations with special configurations (e.g., work zone) were excluded, since the crash dynamics, sequences, and ODDs can be significantly different under the impact of those factors. We are concerned that the nature of those "special" crashes could lead to drastically different sequences of events and outcomes from the "common" crashes, and a separate analysis would be needed develop relevant scenarios for "special" crashes. In this paper, we focused on generating scenarios for the "common" crashes. By applying the criteria, we obtained a data set consisting of 39,850 observations, representing nearly 6 million crashes.

Table 1 Subsetting criteria


Note: * Light trucks with Gross Vehicle Weight Rating (GVWR) $\leq 10,000$ LBS.

### 3.2 Numbering Crash Participants

Each intersection two-vehicle crash has two participating motor vehicles. The CRSS numbered the two vehicles as Vehicle 1 and Vehicle 2 "sequentially", without specifying the basis for that ordering(NHTSA, 2018). Before analyzing the data and developing crash scenarios, we renumbered the vehicles based on their initial positions and trajectories in crashes. By renumbering the participating vehicles, we ensured that scenarios generated using the crash data have consistent vehicle alignments. In simulation-based tests with a two-vehicle crash scenario, the automated driving system (ADS) being tested would be aligned as one of the two participating vehicles (Scanlon et al., 2021). The ADS would be first aligned as Vehicle 1, with Vehicle 2 as an adversarial agent, and then be aligned as Vehicle 2, with Vehicle 1 as an adversarial agent. In that case, we can fully make use of one scenario and test the ADS on both roles in a two-vehicle crash.

To renumber the participating vehicles, information about vehicles' initial positions and trajectories was obtained from the PC23 Crash Type Diagram of CRSS, as shown in Figure 1. For two-vehicle crashes, there are 5 high-level categories including "Same Trafficway Same Direction", "Same Trafficway Opposite Direction", "Change Trafficway Vehicle Turning", "Intersect Paths", and "Miscellaneous". The 5 high-level categories split into 10 configurations (denoted as using letters from "D" to "M"), which split again into more specific crash types (with participating vehicles position and trajectory numbered from " 20 " to " 99 "). Not all crash types appeared in the intersection two-vehicle crash sample. Crash types not included in the sample were marked with a red slash in Figure 1.

Rules of vehicle renumbering are also illustrated in Figure 1. Participants marked with a red dot were numbered as Vehicle 1, participants with a blue dot were numbered as Vehicle 2, and participants with a gray dot had the original numbering kept. Take the " 68 -69" (left turn meets through) combination in crash configuration "J" as an example, the vehicle with an initial position and trajectory " 68 " (left turn) is numbered as Vehicle 1, and the vehicle with an initial position and trajectory " 69 " (through) was numbered as Vehicle 2.
![img-0.jpeg](img-0.jpeg)

Figure 1 CRSS two-vehicle crash types and participant renumbering (NHTSA, 2018)

# 3.3 Encoding Sequences 

The crash sequences were formed using four CRSS variables, PCRASH1 (pre-event movement), PCRASH2 (critical event pre-crash), and PCRASH3 (attempted avoidance maneuver) in the vehicle level data set VEHICLE, as well as the SOE (sequence of events) variable from the event level data set CEVENT. The PCRASH1 3 variables describe "what a vehicle was doing just prior to the critical precrash event", "what made the vehicle's situation critical", and "what was the corrective action made, if any, to this critical situation" (NHTSA, 2018). The SOE variable records series of harmful and non-harmful events occurred in the crashes, in chronological order.

The PCRASH1 3 and SOE events were combined following the rule illustrated in Figure 2. If the first event in SOE was a Vehicle 1 event, then the PCRASH1 3 events of Vehicle 1 were inserted before the PCRASH1 3 events of Vehicle 2, and all PCRASH events were inserted before SOE. Vice versa, if the first event in SOE was a Vehicle 2 event, then the PCRASH1 3 events of Vehicle 2 were inserted before the PCRASH1 3 events of Vehicle 1, and all PCRASH events were inserted before SOE.

Type 1: Vehicle 1 Event Occurred First in SOE
![img-1.jpeg](img-1.jpeg)

Figure 2 Sequence structure

Lengths (number of events) of the sequences ranged from 7 to 16, as shown in Table 2. With over $92 \%$ of the sequences having 7 events (with 6 PCRASH events and 1 SOE event), the average length was 7.2. Sequences longer than the average usually have more collision events. For example, the three sequences with 16 events were:

- 1L-1L-1N-2ST-2OEO-2N-2XV-1CARG-1ROR-1XF-1XF-1XF-2ROL-2XF-2XF-2XF
- 1ST-1ST-1N-2ST-2OET-2N-1XV-2ROL-2XF-2XF-1ROR-1XF-1XP-1XP-1XP-1XF
- 1L-1N-2ST-2OEO-2R-2XV-1XV-2ROR-1XF-1XF-1XO-1XO-1XO-1XO-1XO

Each of the three 16 -event sequences describes a crash where run-off-the-road events happened after the collision between two vehicles, and multiple collisions with fixed object ("XF"), non-fixed objects ("XO"), or pedestrians ("XP") happened afterwards. For detailed event encoding information, please refer to Table A - 1 of Appendix A.

Table 2 Sequence lengths


CRSS has a total of 160 categories of pre-crash and collision events, including 20 in PCRASH1, 57 in PCRASH2, 14 in PCRASH3, and 69 in SOE. With two participating vehicles, the total number would be 320. With a length of 16 , there would be theoretically $320^{16}$ possible sequences. Identifying patterns in sequences would be difficult with too many event categories. Therefore, in this study, the events were encoded by consolidating events that are similar in nature. With the encodings, the total number of event categories became 71, including 14 in PCRASH1, 29 in PCRASH2, 11 in PCRASH3, and 17 in SOE. Details of event encodings are in Table A - 1 of Appendix A.

# 3.4 Other Crash Attributes 

To specify crash scenarios, variables describing crash outcomes, human factors, and environmental conditions were needed, in addition to the crash sequence patterns. The crash outcomes help identify scenarios with more severe injuries and fatalities, which may be of more interest in testing AVs. The human factors and environmental conditions help define ODDs which consist of other moving objects and static surroundings. Crash outcome variables used in this paper are summarized in Table 3. Variables describing human factors and environmental conditions are summarized in Table 4.

Table 3 Crash outcomes


Note: Sample size 39,850 .

Table 4 Human factors and environmental conditions


Note: Sample size 39,850 .
Labels with " + " indicate conditions of Vehicle 1 on the left side and Vehicle 2 on the right side.
In speeding, etc.: $\mathrm{U}=$ Unknown; $\mathrm{Y}=\mathrm{Yes} ; \mathrm{N}=$ No.

More than half ( $52.5 \%$ ) of the sampled crashes ended with a maximum injury severity of no apparent injury, less than half ( $46.9 \%$ ) with injury to different extents, and $0.4 \%$ with fatality. In terms of manner of collision, angle crashes made up $47.0 \%$ of the sample crashes, front-to-rear crashes made up $38.7 \%$, and others made up $14.3 \%$. The crash outcomes reflect a motor vehicle's exposure to crash risks. When setting up test scenarios for AV safety evaluation, the exposure can be adjusted through selecting a combination of crash sequence types.

In this paper, the human factors variables were derived from the "D22 Speeding Related" and "D24 Related Factors - Driver Level" variables of the CRSS VEHICLE data file. We focused on the most frequent driver factors involved in the sample crashes, including speeding, careless driving, did not see, reckless driving, and improper control. In terms of environmental condition variables, we included urbanicity, time of day, lighting condition, weather, type of intersection, speed limits, road surface condition, and traffic control device. For test scenario specifications, the human factors and environmental conditions describe the ODDs.

# 4 Methodology 

This paper employed a procedure of two steps to specify crash scenarios which include crash sequences and depictions of ODDs. The first step was characterization of crash sequences using sequence analysis, and the second step was ODD specification based on a Bayesian network modeling of relationships among crash sequences, outcomes, human factors, and environmental conditions. Sequences and ODDs make up scenarios. Crash sequences describe what could happen between moving objects in the scenarios. ODDs illustrate the surrounding environment in the scenarios.

A crash sequence describes the progression of events that happened in a crash over time. It naturally provides a structure to model complex interactions between vehicle, driver, and the surrounding environment. The reasons that a sequence clustering + Bayesian network design was implemented in this paper rather than a more complex modeling design such as a dynamic Bayesian network were: 1) Such a model is simple and easy to interpret. 2) For a descriptive scenario library, the model offers enough detailed information on the cooccurrence of certain types of crash sequences and ODD settings. 3) Historical crash data only allows us to model interactions to such a level of detail. The CRSS crash sequences themselves include some information about vehicles' interaction with elements of the ODD such as roadside objects. Relative to the interactions between moving objects which changes rapidly, the ODD variables added in the Bayesian network modeling can be considered static.

### 4.1 Crash Sequence Comparison and Clustering

In sequence analysis, the encoded crash sequences were compared and grouped. The basis of sequence comparison and clustering is the measure of dissimilarity, which quantifies the difference between each pair of sequences (Cornwell, 2015; Studer \& Ritschard, 2014, 2016). Optimal matching (OM) based dissimilarity measures have been widely used in bioinformatic and sociological research to for gene sequence or life course sequence analysis (Abbott, 1983, 1995; Cornwell, 2015; Kruskal, 1983; Studer \& Ritschard, 2014, 2016). Some other studies also found OM based dissimilarity measures to be appropriate for crash sequence analysis (Song, 2021; Song et al., 2021, 2022). In the same study, we proposed a methodology to select the optimal encoding schemes and dissimilarity measures for different crash analysis use cases and found the Levenshtein distance to be an overall good choice for measuring crash sequence dissimilarity.

The OM takes two sequences and aligns them. The alignment of sequences involves several operations such as substitutions, deletions/insertions (or indels), compression and expansions, and transpositions (or swaps) $(13,18,30)$. The Levenshtein distance uses only substitutions and indels, with fixed and unified costs (e.g., substitution $=$ indel $=1$ ). The mathematical expression of OM based dissimilarity between a pair of sequences, $x$ and $y$, is:

$$
d_{O M}(x, y)=\min _{j} \sum_{i=i}^{\ell_{j}} \gamma\left(T_{i}^{j}\right)
$$

where $\ell_{j}$ denotes the transformations needed to turn sequence x into y ; and
$\gamma\left(T_{i}^{j}\right)$ is the cost of each elementary transformation $T_{i}^{j}$ (e.g., indel or substitution).

An example of sequence alignment using Levenshtein distance is shown in Table 5. There are multiple ways to align two sequences, "ABCD" and "ACB". Using a substitution cost of $s$ and an indel cost of $d$, the two ways of alignment shown in Table 5 yielded different total costs. The OM then applies a greedy algorithm to return the minimum alignment cost as the dissimilarity between the two sequences.

Table 5 Sequence alignment


Note: Insertion is marked with $\varnothing$,
Deletion is marked with slash/,
Substitution is marked with underline

The Needleman-Wunsch algorithm is a classic OM algorithm to align sequences and find sequence dissimilarities (Needleman \& Wunsch, 1970). For two sequences, A and B, an empty matrix L, of size length $(\mathrm{A})+1$ by length $(\mathrm{B})+1$ is created. Based on a set of indel and substitution costs, the algorithm fills matrix L and returns the smallest alignment cost (i.e., the dissimilarity) between sequences A and B. Pseudocode of the Needleman-Wunsch algorithm is as follows (Song et al., 2021).

```
Algorithm Needleman-Wunsch(A, B)
# initialize
L <- matrix of size length(A) + 1 * length(B) +1
d <- indel cost
s <- substitution cost
# fill the cells of L
for i = 0 to length(A)
    L(i,0)<- d*i
for j = 0 to length(B)
    L(0, j)<- d*j
for i = 1 to length(A)
    for j = 1 to length(B) {
                        insert <- L(i, j-1) + d
                        delete <- L(i-1, j) + d
                        substitute <- L(i-1, j-1) + s
                        L(i, j) <- max(insert, delete, substitute)
                        }
# smallest alignment cost (distance)
return L(length(A), length(B))
```

Using the Levenshtein distance, a dissimilarity matrix for a set of crash sequences is calculated. The matrix is of size $\mathrm{n}^{*} \mathrm{n}$, where n is the number of sequences in the set. Each element in the matrix indicates the dissimilarity between a pair of sequence. The dissimilarity matrix can then be used as an input for a clustering algorithm to characterize crash sequences as distinctive types.

For clustering, we employed a weighted k-medoid method in this paper. K-medoid clustering has been applied in prior studies for crash characterization due to its good performance with categorical data and robustness against outliers (Nitsche et al., 2017; Song et al., 2021). The weighted k-medoid clustering algorithm

used in this paper was developed by Studer, accommodating sampling weights (provided by CRSS data sets) in the clustering (Studer, 2013). The sequence dissimilarity calculation and sequence clustering were completed using R and the libraries "TraMineR" and "WeightedCluster" (Gabadinho et al., 2011; R Core Team, 2019; Studer, 2013).

To characterize the intersection two-vehicle crashes, the sequence comparison and clustering were done under the existing CRSS crash configuration (CC) classification. The distribution of CC is shown in Table 6. Sequence comparison and clustering was done for each CC category. By conducting sequence analysis using existing CC classification, we kept the rarer crash types which would otherwise be overlooked if all 39,850 crash sequences were analyzed in a lump sum. Those rarer crash types are especially useful for developing potentially challenging test scenarios.

Table 6 Distribution of CRSS intersection two-vehicle crash configurations


# 4.2 Bayesian Network Modeling 

Bayesian network modeling has been used in prior studies to evaluate factors affecting crash type and injury severity (Davis, 2001, 2003; Simoncic, 2004; Davis et al., 2011; Fenton \& Neil, 2011; Zhu et al., 2017; Zou \& Yue, 2017; Ma et al., 2018; de Oña et al., 2013; Prati et al., 2017). Bayesian networks are directed acyclic graphs (DAGs), with nodes denoting variables and directed edges denoting the dependencies between variables (Pearl, 1985). The strengths of influences between variables are measured by conditional probabilities. If the graph has variables $x_{1}, \ldots, x_{n}$, and $S_{i}$ as the set of parents of $x_{i}$, an estimated conditional probability is then $P^{\prime}\left(x_{i} \mid S_{i}\right)$. The following joint probability distribution exists for the graph:

$$
P\left(x_{1}, \ldots, x_{n}\right)=\prod_{i} P^{\prime}\left(x_{i} \mid S_{i}\right)
$$

A Bayesian network can be specified based on expert opinions when the number of variables is small and variable relationships are intuitive and simple. Oftentimes, defining a network is too complicated for humans and would need a data-driven approach to accomplish (Koller \& Friedman, 2009). The construction of a Bayesian network consists of two steps (Zhu et al., 2017; Zou \& Yue, 2017):

- Structure learning: determine selection of variables (nodes) and determine the dependencies or independencies between nodes, to form a DAG.
- Parameter learning: based on the determined DAG, estimate a conditional probability table for each node to quantify relationship between nodes.
In this paper, the structure learning was completed using a hill climbing algorithm, which finds the network structure with the highest Akaike information criterion (AIC) score. The AIC score used in the R library, "bnlearn" is calculated as the classic definition rescaled by -2 (Scutari, 2010):

$$
A I C=\ln (\hat{L})-2 k
$$

where $\hat{L}=$ the estimated maximum likelihood of the model; $\mathrm{k}=$ the number of estimated parameters. Therefore, a higher AIC score means a better Bayesian network model. The learned network structure was slightly adjusted based on the authors' domain knowledge in traffic crashes. Multiple networks structures were generated and compared to determine a most appropriate one for ODD specification, based on the conditional probability table. The structure and parameter learning were completed using R and the "bnlearn" library (R Core Team, 2019; Scutari, 2010). Bayesian networks were visualized using the "Rgraphviz" library (Hansen et al., 2021).

Based on a determined Bayesian network, we could understand the direct and indirect dependencies among variables including sequence types (developed from the sequence analysis), crash outcomes (manner of collision and injury severity), human factors, and environmental conditions, using graph visualizations. We could also identify the sequence types likely yielding serious crash outcomes and the ODD settings for specific sequence types by querying for conditional probabilities in the network. Scenarios can be defined using combinations of sequence types and ODD settings, and can be used to help render simulation tests for AV safety evaluation.

# 5 Results 

This section presents the results of 1) crash sequence characterization from sequence analysis and 2) variable dependencies from Bayesian network modeling. Finally, an example of scenario specification based on the crash sequence type and Bayesian network is provided at the end of this section.

### 5.1 Sequence Types

As mentioned, sequence clustering was carried out for each CC category using Levenshtein distance and weighted k -medoid clustering. To measure the quality of clustering and determine the appropriate number of clusters, clustering quality indices including the Weighted Average Silhouette Width (ASWw), Hubert's Gamma (HG), Point Biserial Correlation (PBC), and Hubert's C (HC) were calculated. We used k values ranging from 2 to 25 to cluster the sequences and plotted the indices for comparison.

The plots in Figure 3 illustrate the clustering quality indices for the clustering of CC D (Same Trafficway, Same Direction - Rear End, 39\% of all crashes) crash sequences. An optimal k value would give us maximum ASWw, HG, and PBC (all range from -1 to 1), and a minimum HC (ranges from 0 to 1). Figure 3(a) shows the original values of the four indices but is difficult to read, since the indices have different average values. Figure 3(b) shows the standardized index curves for easier comparison, and it shows that when $\mathrm{k}=12$ the ASWw, HG, and PBC all reach satisfactory high levels and at the same time HC reaches a satisfactory low level. Therefore, $\mathrm{k}=12$ was chosen as the number of clusters for CC D sequence clustering. The same procedure of plotting quality indices and determining the appropriate k value was applied to all CC categories.

![img-2.jpeg](img-2.jpeg)

Figure 3 Clustering quality indices for CC D (rear end) sequences

The clustering results are summarized in Table 7. In each cluster, only the sequence representing the most sequences is presented. More detailed results showing the top three representative sequences are shown in Table A - 2 of Appendix A. CC D Same Trafficway, Same Direction - Rear End ( $39 \%$ of all) crashes were characterized as 12 sequence types, CC J - Change Trafficway, Vehicle Turning - Turn Across Path ( $18 \%$ of all) crashes were characterized as 3 sequence types, CC K - Change Trafficway, Vehicle Turning - Turn Into Path ( $17 \%$ of all) crashes were characterized as 9 sequence types, and CC L - Intersect - Straight Paths ( $16 \%$ of all) crashes were characterized as 14 sequence types.

Interpretation of the representative sequences is presented in Table 7 for easier understanding of the sequence types. For example, the representative sequence of Type e3, in coded form, was "1ST-1OES-1BR-2ST-2OIS-2NA-1XV-1ROR-1XF-1NCH", and was interpreted as "v1 moving straight-other encroached into lane SD (brake and turned right) $\rightarrow$ v2 moving straight (no)", meaning Vehicle 1 and Vehicle 2 were both moving straight along the same direction. Some other vehicle encroached into Vehicle 1's lane, making Vehicle 1 brake and steer right. Vehicle 1 then collided into the rear of Vehicle 2, which did not make any maneuver to avoid the collision. Following the collision, Vehicle 1 ran off the road, hit a fixed object, and suffered a noncollision harmful event.

For the development of AV testing scenarios, it is important to balance details and abstraction, as rare but safety-critical crashes may be buried into larger groups of more common crashes in the clustering process.

By further characterizing intersection two-vehicle crashes under the existing crash configurations, some rare crash configurations such as E (Same Trafficway, Same Direction - Forward Impact) and G (Same Trafficway, Opposite Direction - Head On) could be represented and considered in scenario specification. Within each crash configuration category, the sequence clustering was able to identify different pattens in the pre-crash events and effectively assign sequences into distinct clusters. For example, the first three clusters under the D (Same Trafficway, Same Direction, Rear-End) crash configuration, as shown in Table 7, represent different initial states: d1 has Vehicle 1 moving straight and Vehicle 2 decelerating, d2 with Vehicle 1 making a right turn and Vehicle 2 stopped, and d3 with Vehicle 1 negotiating a curve and Vehicle 2 stopped. In addition to differences in initial states, types of collision avoidance maneuvers were also differentiated by the sequence clustering. Therefore, the resulting sequence types provide useful information for determining the initial locations, actions, and behavior of agents when recreating the scenarios in simulation.

Table 7 Sequence clustering results


Note: v1 = Vehicle 1; v2 = Vehicle 2. See Section 3.2 Numbering Crash Participants for details. $\mathrm{SD}=$ same direction. The arrow symbol, " $\rightarrow$ ", means that the vehicle left of the arrow collided into the vehicle right of it. Content in the parentheses is crash avoidance maneuver, no parenthesis means action unknown.

(Table 7 Continued)


Note: $\mathrm{SD}=$ same direction; $\mathrm{OD}=$ opposite direction; $\mathrm{CS}=$ cross street.

# 5.2 Variable Dependencies 

Using a hill climbing algorithm with AIC as the criterion for model selection, a Bayesian network was learned to illustrate the relationships among sequence types, crash outcomes, human factors, and environmental condition variables. The network is shown in Figure 4. Each node represents a variable, and the directed arcs represent dependencies among variables. The weight of an arc represents its strength, measured by the potential change in AIC score led by removal of the arc from the network (i.e., the difference between the network's AIC score with and without the arc) (Scutari, 2010). If the change in AIC is negative, that means removing the arc harmed the network by losing information. Therefore, a more negative difference indicates a higher arc strength (i.e., stronger relationship between two variables). The network was only slightly adjusted by removing an arc from lighting condition ("light") to "weather" to simplify the network without compromising the overall model AIC score.
![img-3.jpeg](img-3.jpeg)

Note: Crash outcomes are in blue; human factors are in pink; environmental conditions are in white.
Numbers indicate strengths (change in AIC) of arc, the more negative, the stronger the link.

## Figure 4 Bayesian network generated from hill climbing learning

The Bayesian network shows that sequence type had strong relationships with crash outcome variables - maximum injury severity ("maxsev") and manner of collision ("moc"). Sequence type was also directly or indirectly associated with human factors and environmental conditions. Five strongest direct links with sequence type were manner of collision ("moc"), traffic control device ("tcd"), maximum injury severity ("maxsev"), speeding, and careless driving ("careless").

The variable pointed by the arrowhead of an arc is directly dependent on the variable on the other end of the arc. Note that the arcs pointing from crash sequence type to crash outcomes indicated expected dependencies, as supported by prior studies' findings that the order of events and actions taken during the precrash and crash periods directly affect manner of collision and injury severity (Wu et al., 2016). As mentioned, a Bayesian network can be specified by a human expert or be constructed using data-driven approaches.

Therefore, depending on how much influence of expert opinions was incorporated in the specification of Bayesian networks, prior studies suggested different network structures regarding the relationships between crash outcomes and human and environmental factors (Ma et al., 2018; Zou \& Yue, 2017; de Oña et al., 2013; Prati et al., 2017). In the studies analyzing crash causations, expert opinions heavily affected the Bayesian network design, thus arcs pointed from human and environmental factors to crash outcomes (Ma et al., 2018; Zou \& Yue, 2017). However, the studies following a data-driven approach showed that Bayesian networks learned from crash data had some arcs pointing from crash outcomes to human and environmental factors (de Oña et al., 2013; Prati et al., 2017). In this study, the Bayesian network learned from crash data, as shown in Figure 4, has similar arc patterns with the latter studies applying a primarily data-driven approach.

To confirm that the primarily data-driven approach generated a better network than an expert-opinion oriented approach, an alternative Bayesian network was constructed with more influence of the authors' intuitions and domain knowledge, as shown in Figure 5. In the alternative network, arcs were manually added to point from human factors and environmental conditions to sequence types. The resulted network shows very weak arc strengths. Therefore, we followed the data-driven approach and selected the Figure 4 network as the final Bayesian network for test scenario specification.
![img-4.jpeg](img-4.jpeg)

Note: Dashed arcs indicate weak strengths ( $>0$ ).
Figure 5 Alternative Bayesian network

A note on interpreting the inter-variable relationships in the Bayesian network such as that between sequence type ("seqtype") and variables such as traffic control devices ("tcd") in the Figure 4 network: Based on intuition, one may think that sequence type should be dependent on traffic control device and not the other way around, but such an intuition-based dependency requires strong assumptions of the process of how a traffic control device would affect the formation of a certain sequence type. There is no variable or data available in the crash database to support such assumptions. On the other hand, the current dependency should be interpreted as "given the information of a sequence type, one would know the type of traffic control device that was installed at intersections where such type of sequence most likely occurred", which is strong and supported by the data.

To confirm the relationships between sequence types and crash outcomes, as well as between sequence types, human factors, and environmental conditions, we tested the local network structural stability by developing partial Bayesian networks as shown in Figure 6 and Figure 7. Figure 6 shows that the relationships between sequence types and crash outcomes did not change after removing all other variables from the original network (in Figure 4). Figure 7 shows that the local network structure changed only slightly on type of intersection ("typint") and speed limit ("spdlim") after crash outcome variables were removed from the original network. Therefore, the local network structures were stable, confirming the relationships between sequence types and other variables.
![img-5.jpeg](img-5.jpeg)

Figure 6 Bayesian network of sequence types and crash outcomes
![img-6.jpeg](img-6.jpeg)

Figure 7 Bayesian network of sequence types, human factors, and environmental conditions

# 5.3 Scenario Specification 

The final Bayesian network in Figure 4 is of two uses in specifying test scenarios. First, crash sequences of certain injury severity levels can be selected based on the dependencies between sequence types and crash outcomes. Second, after sequence types of interest are determined, their associated ODD attributes can be specified based on the dependencies among sequence types, human factors, and environmental conditions. The scenario specification can be done by querying the conditional probability table generated from the final Bayesian network. We demonstrate the process here with an example.

If we would like to specify scenarios for some intersection two-vehicle crashes that resulted in fatalities, we can first query the final Bayesian network to obtain the distribution of sequence types that resulted in fatalities, as shown in Figure 8. Using the "bnlearn" library in R, the distribution was generated based on Monte Carlo particle filters (Scutari, 2010). The query was run 1,000 times ( 1,000 replications), each time obtaining the counts of crashes under all sequence types. Then the average count was calculated within each sequence type over the 1,000 replications. The Figure 8 illustration presents the distribution of average counts. The distribution shows that sequence types $\mathrm{j} 2, \mathrm{j} 3, \mathrm{k} 3,17,112$, and 113 were the most frequent fatal crash sequences.
![img-7.jpeg](img-7.jpeg)

Figure 8 Distribution of sequence types resulting in fatalities

If we would like to specify ODDs for a sequence type, for example, k3, we can query the Bayesian network again for distributions of human factor and environmental condition variables using "seqtype $=\mathrm{k} 3$ " as a criterion. The crash type k 3 is illustrated in Figure 9, and it is a type of "changing traffic way turning into path" crash, where Vehicle 2 (V2 in figure) is moving straight and hitting Vehicle 1 (V1 in figure) which is turning left onto the trafficway that Vehicle 2 is on.
![img-8.jpeg](img-8.jpeg)

Figure 9 Illustration of crash type k3

Two examples of Bayesian network query for crash type k3 are demonstrated here. Table 8 shows query results for the distribution of intersection type and traffic control device (TCD) in k3 crashes. Table 9 shows query results for the distribution of drivers' speeding behavior and time of day in k3 crashes. The two tables are color coded to show larger values in darker green and smaller values in lighter green. From the query results we found that k 3 crashes happened most frequently at 4 -legged intersections with sign control on minor approaches, 3 -legged intersections with sign control on minor approaches, and at 4 -legged intersections with signal control on all approaches. Speeding was not related to $95 \%$ of k3 crashes. More k3 crashes happened in daytime than in nighttime, but the proportion of speeding-related crashes in all k3 crashes were the same $2 \%$ regardless of daytime or nighttime.

Table 8 Distribution of intersection type and TCD in k3 crashes


Note: Average values of 1,000 replications.
Labels with " + " indicate conditions of Vehicle 1 on the left side and Vehicle 2 on the right side.

Table 9 Distribution of speeding behavior and time of day in k3 crashes


Note: Average values of 1,000 replications.
$\mathrm{N}=$ not speeding, $\mathrm{U}=$ unknown, $\mathrm{Y}=$ speeding.

With the information obtained from Table 8 and Table 9, we can specify several ODDs for the testing of k 3 crash sequence type. For example, "a 4 -legged intersection with sign control on the minor approaches at daytime". More complex queries can also be run to obtain more comprehensive descriptions of ODDs. Given an ODD, we can also obtain the distribution of sequence types by querying the Bayesian network and carry out tests accordingly. For example, Table 10 shows the query results of sequence type distribution at signalcontrolled intersections. The results are color-coded to show the within-category (4-legged or 3 legged)

distribution, with darker color indicating a higher proportion and lighter color indicating a lower proportion within category. Most frequently occurred crash sequence types for both 4 -legged and 3-legged signalized intersections are i1, d12, j2, and j3. Crashes can be sampled based on this distribution and used to reconstruct scenarios in a simulation environment for AV testing.

Table 10 Distribution of sequence types at signal-controlled intersections


Note: Average values of $1,000 \mathrm{replications}$.

Specified scenarios can be validated in simulation for their capabilities in testing AV safety. Based on the scenario design, moving agents (including an AV agent and agents simulating other road users) can be deployed and the ODD settings can also be rendered in the simulation. If the AV agent fails to maintain safety throughout the scenario simulation. The scenarios are then proved to be useful in capturing safety flaws of the AV agent. Various types of AV agents developed by different organizations can be included in the simulation testing to validate the reliability of the scenario library.

# 6 Discussion and Conclusion 

This paper presents a procedure to generate crash scenarios for AV safety testing. The method consists of two steps, 1) characterization of crashes encoded by sequences of events using sequence analysis techniques, and 2) specification of scenarios based on a Bayesian network modeling dependencies among crash sequence types, crash outcomes, and variables depicting ODDs. The procedure was demonstrated using 2016-2018 intersection two-vehicle crash data from the NHTSA CRSS database.

This paper has two major findings. First, we characterized the intersection two-vehicle crashes as 55 types based on their patterns in sequences of events. The 55 crash sequence types offered more information about crash progression to the original CRSS configuration and helped identify rare crash types which could otherwise be overlooked. Second, we found the dependencies among crash sequence types, crash outcomes, human factors, and environmental conditions using a Bayesian network. Sequence types were found to be the core of the network and have direct effects on crash outcomes, as expected. The dependencies of human factors and environmental conditions on sequence types are useful in specifying ODDs for crash sequence types and identifying distributions of crash sequence types for specific ODDs.

The contribution of this paper is that it offers a methodology to systematically generate a crash scenario library based on national-level crash databases. Such a library would offer a comprehensive set of crash sequence types and ODDs, making it an appropriate guide for developing simulation-based tests for AV safety evaluation. Therefore, such a scenario library would complement scenario generating methodologies developed based on vehicle kinematic data sources such as naturalistic driving data and crash reconstruction data. Comparing with previous efforts in systematically generating scenarios for AV testing using crash data, such as the work by Nitsche et al. (2017), Sander and Lubbe (Sander \& Lubbe, 2018), and the Safety Pool scenario library of Warwick University (Esenturk et al., 2021, 2022), the approach we proposed in this paper is a significant improvement. That is because 1) the crash sequence modeling captures the interactive dynamics and 2) the Bayesian network provides a comprehensive but interpretable representation of the relationships between all types of factors involved in crashes. Importantly, for specifying AV testing scenarios, the inclusion of crash dynamics conforms to the definition of "scenario" (Ulbrich et al., 2015); the model interpretability ensures that testers or experts are able to comprehend the meaning of each scenario; and the model comprehensiveness offers a large scenario space which allows the flexibility to develop tests targeting different levels of safetycriticality and various ODD settings.

Future work along this paper's line of research would bring improvements by addressing the limitations in crash sequence data source. More detailed crash event data than what we obtained from the CRSS database (or any other current national or state-level crash database in the United States) were not available, so crash sequences used in the case study were limited to the level of details provided by CRSS. More ODD attributes would benefit the Bayesian network modeling by providing more information. However, a more complex network would take more effort to interpret. For future work, data sources with more detailed crash sequence data would be sought and used to generate more detailed crash characterization. More elaborative Bayesian network models, such as dynamic Bayesian network, would be explored for use in modeling crash sequences and ODDs for AV test scenario specification. Also, an important next step would be the integration of crash sequences and vehicle kinematic information to define concrete scenarios that can be implemented in simulation-based testing platforms, as well as the validation of scenarios in testing AV safety performance.

## Funding

This research was partially sponsored by the Safety Research using Simulation University Transportation Center (SAFER-SIM). SAFER-SIM is funded by a grant from the U.S. Department of Transportation's University Transportation Centers Program (69A3551747131). The work presented in this paper remains the responsibility of the authors.

# Appendix A 

## Table A - 1 Event Encodings

## PCRASH1



# PCRASH3 


## SOE


Table A - 2 Intersection two-vehicle crash sequence types




