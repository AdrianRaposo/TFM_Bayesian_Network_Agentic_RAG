# Climate Dynamics: A Network-Based Approach for the Analysis of Global Precipitation 

Stefania Scarsoglio ${ }^{1 *}$, Francesco Laio ${ }^{2}$, Luca Ridolfi ${ }^{2}$<br>1 Department of Mechanical and Aerospace Engineering, Politecnico di Torino, Torino, Italy, 2 Department of Environment, Land and Infrastructure Engineering, Politecnico di Torino, Torino, Italy


#### Abstract

Precipitation is one of the most important meteorological variables for defining the climate dynamics, but the spatial patterns of precipitation have not been fully investigated yet. The complex network theory, which provides a robust tool to investigate the statistical interdependence of many interacting elements, is used here to analyze the spatial dynamics of annual precipitation over seventy years (1941-2010). The precipitation network is built associating a node to a geographical region, which has a temporal distribution of precipitation, and identifying possible links among nodes through the correlation function. The precipitation network reveals significant spatial variability with barely connected regions, as Eastern China and Japan, and highly connected regions, such as the African Sahel, Eastern Australia and, to a lesser extent, Northern Europe. Sahel and Eastern Australia are remarkably dry regions, where low amounts of rainfall are uniformly distributed on continental scales and small-scale extreme events are rare. As a consequence, the precipitation gradient is low, making these regions well connected on a large spatial scale. On the contrary, the Asiatic South-East is often reached by extreme events such as monsoons, tropical cyclones and heat waves, which can all contribute to reduce the correlation to the short-range scale only. Some patterns emerging between mid-latitude and tropical regions suggest a possible impact of the propagation of planetary waves on precipitation at a global scale. Other links can be qualitatively associated to the atmospheric and oceanic circulation. To analyze the sensitivity of the network to the physical closeness of the nodes, short-term connections are broken. The African Sahel, Eastern Australia and Northern Europe regions again appear as the supernodes of the network, confirming furthermore their long-range connection structure. Almost all North-American and Asian nodes vanish, revealing that extreme events can enhance high precipitation gradients, leading to a systematic absence of long-range patterns.


Citation: Scarsoglio S, Laio F, Ridolfi L (2013) Climate Dynamics: A Network-Based Approach for the Analysis of Global Precipitation. PLoS ONE 8(8): e71129. doi:10.1371/journal.pone. 0071129

Editor: Alex J. Cannon, Pacific Climate Impacts Consortium, Canada
Received April 24, 2013; Accepted July 2, 2013; Published August 19, 2013
Copyright: © 2013 Scarsoglio et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
Funding: Funding from the Italian Ministry of Education, Universities and Research (Futuro in Ricerca 2012, Project RBFR12BA3Y) is acknowledged. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.
Competing Interests: The authors have declared that no competing interests exist.

* E-mail: stefania.scarsoglio@polito.it


## Introduction

By combining graph theory and statistical physics, complex network theory provides a powerful tool to investigate the structure and function of complex systems with a large number of interacting elements. The development and characterization of complex networks [1-3] makes their application suitable to analyze a wide range of systems from nature to economy, from engineering to society [4]. Beside the well-established applications to Internet and World Wide Web, neural connections and social dynamics [5], complex networks have been successfully used to study many different phenomena such as, for example, human migration [6], cancer metastasis [7] and earthquake occurrence [8].

The extension of complex network theory to climate sciences is a very recent area yielding climate networks, which usually rely on gridded time series of meteorological preprocessed variables. The nodes of the network are identified by geographical regions corresponding to single points of measurement on the spatial grid of the underlying climate database. Each node has a measured state variable which varies in time. A link between two nodes exists if there is a significant statistical interdependence between their
time series. The linear cross-correlation function is typically used as the simplest possible measure of the statistical interdependence of the temporal series. However, the influence of the choice of an association measure on the topology of the climate network has been studied, by accounting how the temporal complexity of time series influences the absolute correlations [9] and proposing alternative criteria based on the nonlinear mutual information $[10,11]$.

Until now, attention has been mainly devoted to networks based on the global surface temperature field to understand the influence of El Niño and La Niña events in regions which are far from the El Niño-Southern Oscillation (ENSO) area. Although the temperatures in different zones of the world are not significantly affected by El Niño and La Niña, it was surprisingly found that the climate network during these events is sensitively influenced by showing a different structure and a consistent amount of broken links [1214]. The community structure [15] as well as the dynamics of interacting networks [16] have been investigated using the surface temperature fields and related variables (e.g., sea level pressure and equipotential heights).

Apart from some works where different meteorological variables such as equipotential heights [15-17], sea surface temperature,

humidity, and related data [18] are also analyzed, the great part of climate network literature deals with surface air temperature data only. In particular, to the best of our knowledge, a global precipitation analysis has not yet been performed by using the complex network theory. Only Malik et al. [19] recently carried out a complex network study of local extreme monsoonal rainfall in South Asia, while Bayesian networks have been employed to analyze local precipitation in the Iberian peninsula [20], [21].

The gap concerning global precipitation in climate networks is evident even though precipitation teleconnections, especially related to the ENSO occurrence [22], [23], have been recognized for being a crucial aspect in climate and hydrological changes [24], and are increasingly examined for Asian monsoons [25]--[28], European [29], [30], African [31] and American [32], [33] rainfall events.

The present work arises in this scenario and aims at being a first step towards filling this gap in climate network analysis; in fact, precipitation, together with surface temperature and wind, atmospheric pressure and humidity, is one of the most important meteorological variables in defining the climate dynamics. The global annual precipitation over seventy years (1941--2010) is analyzed by means of the complex network theory. We use the Global Precipitation Climatology Centre (GPCC) Database [34]--[36], which is one of the most reliable precipitation datasets providing land-surface precipitation from rain-gauges over the period 1901--2010. Pre-processing of the data is performed to (i) define nodes corresponding to geographical regions (cells) with the same area, and (ii) consider data mainly based on in situ observations (rather than on interpolated values). The precipitation network is built identifying a node with a geographical region, which has a temporal distribution of measured precipitation, and using the linear correlation function to evaluate possible links between nodes. If the statistical interdependence between two nodes is above a suitably chosen threshold, a link between the two nodes is established. The precipitation network is described through classical tools of the complex network theory - such as the degree centrality, the betweenness centrality and the clustering coefficient - as well as measures introduced here for the first time: the weighted average topological distance, which generalizes the average topological distance definition, and the average physical distance of a node from the rest of the network. To analyze the sensitivity of the network to the physical closeness of the nodes, short-term connections are broken and edges between physically distant nodes only survive. In so doing, the unavoidable spatial correlation between physical neighbors is left aside in favor of highlighting the possible interdependence between not confining regions.

## Materials and Methods

In this section the database used to define the precipitation network is described. Details on the pre-processing analysis of data are then offered. Afterwards, we summarize some fundamental concepts in complex network theory [3], [5]. We only introduce measures which are relevant to the present analysis. In the end, starting from the spatio-temporal global precipitation distribution, details on how to build the precipitation network will be given.

### GPCC Full Database Description

The present investigation uses the Global Precipitation Climatology Centre (GPCC) Full Data Reanalysis Version 6, which consists of monthly land-surface precipitation data from rain-gauges built on Global Telecommunication System (GTS) and historic data [34]--[36]. The GPCC Full Database covers the period from January 1901 to December 2010 and is based on both real-time raingauge data as well as non real-time sets of data. The new extended database version was released in December 2011 and the data coverage per month varies from 10,700 to more than 47,000 stations. Non real-time data, coming from dense national observation networks of individual countries and other global and regional collections of climate data, are integrated in the GPCC Full Database using the GPCC Precipitation Climatology Database as analysis background (for more details, see the online documentation [36]).

The monthly global precipitation is reported on a regular grid with a spatial resolution of 0.5° × 0.5°, 1.0° × 1.0°, and 2.5° × 2.5° latitude by longitude. The global gridsystem goes from (-180° W, +90° N) to (+180° E, -90° S). For every gridcell three kinds of data are given: (i) monthly precipitation [mm/month]; (ii) mean monthly precipitation [mm/month] based on the GPCC Precipitation Climatology; (iii) number of gauges per grid. We obtain the annual precipitation by summing the monthly precipitation values.

The GPCC Full Database provides one of the most accurate and complete in situ precipitation data sets. In fact, the wide spatial and temporal coverage makes this database suitable for verification of models [37], [38], for analysis of historic global precipitation [39]--[43], and for research concerning the global water cycle [44], [45], e.g. trend and time-series analyses [46], [47]. Moreover, the number of stations per gridcell is an additional useful piece of information, which can be exploited when evaluating the spatio-temporal precipitation distribution.

### Data Pre-Processing

Although the GPCC Full Database is a very accurate and detailed dataset, there are two main concerns to use it, as it is, to define a complex network. In this section we discuss these two issues and propose our solutions to overcome them.

First, the regular grid based on the angular partition of the terrestrial surface (i.e. the geographic coordinate system) leads to the definition of gridcells with different geometric area. This heterogeneity, which becomes more evident by approaching regions far from the equator, may induce substantial bias and spurious correlation when building the precipitation network. One way to avoid this bias is to use a tessellation technique [48] to divide the gridcells into suitable two-dimensional structures. An alternative axiomatic scheme, based on the idea of node splitting invariance to obtain consistent weights for the most commonly used network parameters, was proposed by Heitzig et al. [49].

Here, we adopt a simpler approach: we build a new grid system with all square cells having a fixed area, d<sub>r</sub> × d<sub>e</sub>. We focus on the equator, where the original GPCC grid system with 2.5° × 2.5° gridcell resolution yields a square cell dimension (d<sub>r</sub> × d<sub>e</sub>) of 278.3 × 278.3 km². The new graticule, which is here proposed, is built maintaining this cell dimension (d<sub>r</sub> × d<sub>e</sub>) fixed for all latitudes. As a consequence, the number of the new cells is variable over the latitude and, in particular, the new graticule has fewer cells than the original GPCC grid system when moving far from the equator. The number of raingauges of a new cell is the sum of all the raingauges present in the GPCC cells which are completely contained by the new cell. The precipitation value of the new cell is instead the average of the precipitation values measured by those GPCC cells which are entirely included into the new cell. To avoid possible overlaps in the longitudinal direction between cells of the new graticule, we adopt the following convention: when two new cells share an edge falling into an original GPCC cell, the contribute of the original cell (in terms of number of raingauges and precipitation value) is fully allocated to the cell of the new grid system which covers most of the GPCC cell area.

The second concern is about the spatio-temporal distribution of measurement stations. In the GPCC Full Database, in fact, there exists an amount of cells for which no measurement is available over several months (i.e., the number of raingauges for the gridcell is 0 ). However, in these cases, the global precipitation information are recovered through the interpolation of global and mean data offered by the GPCC Precipitation Climatology Database. In so doing, the spatio-temporal coverage is complete but some precipitation values can be fully based on interpolated data. This aspect becomes important when the oldest data are analyzed, since fewer measurements were available. In order to consider data mainly based on in situ observations, we define a grid cell as active for a fixed year if there is at least one measurement for every month of the year. Otherwise the grid cell is not active. We then restrict the analysis to a temporal window of 70 years starting from 1941 to 2010, and consider only cells which are active (also not consecutively) for at least 50 years over the temporal window of 70 years. In this way, more than $90 \%$ of the stations will be included in the spatio-temporal precipitation distribution and, in the worst cases, less than $30 \%$ of the distribution ( 20 years over 70 ) will rely on interpolated data. The number of active cells is $M=1731$.

## Complex Network Tools: Definitions and Structural Properties

A network (or graph) is defined by a set $V=1, \ldots, N$ of nodes and a set $E$ of edges (or links) $\{i, j\}$. Here, we assume $N \leq M$, that is the number of nodes of the network, $N$, can be equal or lower than the number of active cells, $M$. Moreover, we suppose that only one edge can exist between a pair of nodes and no self-loops $\{i, i\}$ are allowed. The adjacency matrix, $A$ :

$$
A_{i j}= \begin{cases}0, & \text { if }\{i, j\} \notin E \\ 1, & \text { if }\{i, j\} \in E\end{cases}
$$

takes into account whether a link is active or not between nodes $i$ and $j$. Since the network is considered as undirected, $A$ is symmetric. Since no self-loops are allowed, $A_{i i}=0$.

The degree centrality of a node is defined as

$$
k_{i}=\frac{\sum_{j=1}^{N} A_{i j}}{N-1}
$$

and gives the number of first neighbors of the node $i$, normalized over the total number of possible neighbors $(N-1)$. The degree distribution, $p(k)$, defines the fraction of nodes in the graph having degree $k$. In other words, the degree distribution is the probability that a node in the network is connected to $k$ other nodes.

We here propose the weighted average topological distance of a node as

$$
\bar{D}_{i}=\frac{\sum_{p \text { on } i(i)} d_{i j}}{N_{c i}} \frac{N-1}{N_{c i}}
$$

where the shortest path length, $d_{i j}$, is the minimum number of edges that have to be crossed from node $i$ to node $j$, and $n n(i)$ is the set of all neighbors of $i . N_{c i}$ is the number of nodes connected to node $i\left(N_{c i} \in[1, N-1]\right)$. The first ratio of the right hand side of Eq. (3) accounts for the mean topological distance of node $i$ with respect to all the $N_{c i}$ nodes linked to it, while the second ratio is a weight coefficient considering how strongly node $i$ is connected to the rest of the graph. We introduce this notation to generalize the
classical average topological distance definition [50], $\bar{d}_{i}=\sum_{j=1}^{N} d_{i j} /(N-1)$. In fact, when the graph has disconnected components the average topological distance definition diverges. Relation (3) is identical to the average topological distance when the graph is completely connected ( $N_{c i}=N-1$ for every node). In the case of a graph with disconnected nodes, instead, $\bar{D}_{i}$ does not diverge and can vary in the interval $[1, N-1]$. The extreme value $N-1$ is reached when two nodes, $i$ and $j$, are directly connected one to each other $\left(d_{i j}=1\right)$, but disconnected from the other nodes $\left(N_{c i}=1\right)$. A large $\bar{D}_{i}$ value means that node $i$ is topologically far from the rest of the network.

The local clustering coefficient of a node is

$$
C_{i}=\frac{e\left(\Gamma_{i}\right)}{\frac{k_{i}\left(k_{i}-1\right)}{2}}
$$

where $\Gamma_{i}$ is the set of first neighbors of $i, e\left(\Gamma_{i}\right)$ is the number of edges connecting the vertices within the neighborhood $\Gamma_{i}$, and $k_{i}\left(k_{i}-1\right) / 2$ is the maximum number of edges in $\Gamma_{i}, 0 \leq C_{i} \leq 1$. The local clustering coefficient gives the probability that two randomly chosen neighbors of $i$ are also neighbors. The global clustering coefficient is the mean value of $C_{i}, \bar{C}=\sum_{i=1}^{N} C_{i} / N$.

The betweenness centrality of a node is

$$
B C_{k}=\sum_{i, j \neq k} \frac{\sigma_{i j}(k)}{\sigma_{i j}}
$$

where $\sigma_{i j}$ are the number of shortest paths connecting nodes $i$ and $j$, while $\sigma_{i j}(k)$ gives the number of shortest paths from $i$ to $j$ crossing node $k$. If node $k$ is traversed by a large number of all existing shortest paths (that is, if $B C_{k}$ is large), then node $k$ can be considered an important mediator for the information transport in the network.

## Building the precipitation network

The number of active cells, as previously described, is $M=1731$. Once the time series of the annual precipitation is obtained for each active cell, we can evaluate the cross correlation between all pairs of them. We use the linear Pearson correlation as it is the simplest possible measure to quantify the degree of statistical interdependence between the temporal series. Moreover, Donges et al. [10] found a high level of similarity between Pearson correlation and mutual information networks. The correlation coefficient is given by an element of the correlation matrix, $R_{i j}$, which is symmetric and estimates the strength of a linear interdependence between two temporal series, $s_{i}$ and $s_{j}$ $\left(i, j \in[1, M], R_{i i}=1\right.$ by definition). The correlation coefficient can vary between -1 and 1 . A large positive value means the temporal series are strongly correlated, while a large negative value indicates a strong anti-correlation. Since we are interested in both large positive and negative correlation values, the absolute value of $R_{i j}$ will be used to build the precipitation network [10]. Moreover, the physical distance, $l_{i j}$, is evaluated in kilometers as the shorter great circle path between nodes $i$ and $j$ and stored in the symmetric matrix $L_{i j}$.

The average physical distance of an active cell (node) is defined here as

$$
L_{i}=\frac{\sum_{j=1}^{M} l_{i j}}{M-1}
$$

where *M* is the number of active cells and *lij* is the physical distance between nodes *i* and *j* defined above (*lij* = 0 by definition).

The *edge density* ρ(τ) is defined as:

$$
\rho(\tau) = 1 - P_R(\tau) = \frac{n(\tau)}{\frac{N(N-1)}{2}}, \tag{7}
$$

where *n*(τ) is the number of active links (edges) when the absolute value of *R* (in the following we abbreviate the correlation *Rij* with *R*) is above the threshold τ, while *P<sub>R</sub>*(τ) is the cumulative distribution function of the correlation *R*.

To define the adjacency matrix, *A*, and therefore the network, we refer to Eq. (1) and define that an edge, *E*, between nodes *i* and *j* exists when |*Rij*|>τ. In so doing, the resulting precipitation network is undirected (A is symmetric) and unweighted (all the |*Rij*| values above the threshold correspond to *Aij* = 1). The selection of the threshold τ is a non-trivial aspect of building a climate network [10,12,13]. Since we are primarily interested in highlighting strong correlated and anti-correlated connections, we set τ = 0.5. With this threshold value, the number of active links is *n* = 9481 and the number of nodes is *N* = 1674 (57 nodes out of 1731 are not connected with any other node of the network). The chosen threshold, τ = 0.5, corresponds to an edge density value, ρ, equal to 0.0068. We graphically make the nodes coincide with the center of each active cell, see the blue symbols in the left panel of Fig. 1.

## Results

The properties of the precipitation network are here presented and discussed. Among the network measures introduced in the *Materials and Methods* Section, particular attention will be paid to the degree centrality and the weighted average topological distance. In fact, these two parameters reveal to be the most meaningful for the present analysis.

As mentioned, the precipitation network is made of *N* = 1674 nodes. However, not all of them are completely connected one to the other. This means that the graph has disconnected components. This aspect justifies the choice of proposing a different definition of the mean topological distance, see Eq. (3). In particular, 1632 nodes are completely linked and form a big subnetwork, while the remaining 42 nodes contribute to create 14 smaller micro-networks. The size (number of nodes) of each micro-network varies from 9 to 2. Although visible through the betweenness centrality, the best parameter which physically

![img-0.jpeg](img-0.jpeg)

individuates the nodes of these smaller networks is the weighted average topological distance, *D̅<sub>l</sub>*.

The data analysis is completed by describing the properties of another precipitation network with an additional constraint: an edge, *E*, between nodes *i* and *j* exists when |*Rij*|>τ and *lij* > δ. A suitably large value of the threshold δ leads to define a new precipitation network, where edges only exist between nodes which are physically far from each other. In so doing, the unavoidable spatial correlation between physical neighbors is left aside in favor of highlighting the possible interdependence between not confining regions (i.e., δ > *d<sub>e</sub>*).

To focus on possible links between regions physically far from each other, we set δ = 1000 km and obtain a new network with fewer nodes, *N<sub>δ</sub>* = 640, and links, *n<sub>δ</sub>* = 1632, than the network previously discussed. The American and Asiatic continents are the regions which much suffer of the reduction of nodes, while Western Europe and Australia still have an appreciable number of nodes (see the red symbols in the left panel of Fig. 1). The number of active links, *n*, is reported in the right panel of Fig. 1 as a function of the physical distance, *l* (the scale of values is in 10<sup>3</sup> km, the red line represents the threshold δ = 1000 km).

## Properties of the precipitation network

We start considering the degree centrality for the basic network, see Fig. 2. One clearly distinguishes two regions with the highest degree centrality values: the Sahel region in Africa, and Eastern Australia. The nodes in these regions are directly connected to a great number of other nodes of the network, therefore they are usually referred to as *supernodes*. Beside the supernode areas, there exist regions with fairly high degree centrality values: Northern Europe, Central Asia, Southern Africa, Western US, and Northeastern Brazil. It should be noted the great difference in terms of degree centrality values, *k<sub>i</sub>*, when moving from the West to the East Coast of the US, as well as from Northern Europe towards the Mediterranean Sea. We recall that the degree centrality is the ratio between the number of cells directly linked to a fixed cell, normalized over the total number of possible neighboring cells (*N* − 1). Speaking in terms of the physical area directly connected to a cell, the maximum degree centrality value here reached, *k<sub>i</sub>* = 0.033, corresponds to a directly connected physical area of about 4.3·10<sup>6</sup> km<sup>2</sup>, equivalent to the total area of the countries in the European Union.

Real networks are often scale-free, that is power-law degree distributions are displayed [5], with exponents ranging between −2 and −3. These networks usually result in the simultaneous

![img-1.jpeg](img-1.jpeg)

Figure 1. Nodes and links of the network. (left) Nodes of the network. Each node graphically coincides with the center of an active spatial cell. Red symbols correspond to the nodes of the network (*N<sub>δ</sub>* = 640) with the additional physical constraint, *l<sub>ij</sub>* > δ = 1000 km, while blue symbols correspond to the nodes of the network (*N* = 1674) without this constraint. (right) Number of links, *n*, as a function of the physical distance, *l* [10<sup>3</sup> km]. The scale of values is in 10<sup>3</sup> km, the red line indicates the physical threshold, δ = 1000 km. doi:10.1371/journal.pone.0071129.g001

![img-2.jpeg](img-2.jpeg)

Figure 2. Degree centrality, k<sub>i</sub>, Large values correspond to highly connected nodes. doi:10.1371/journal.pone.0071129.g002

presence of few nodes highly connected to the others (i.e., *supernodes*) and a great amount of barely connected cells. However, because of the finite size of the network, data can have a rather strong intrinsic noise. To smooth the fluctuations generally present in the tails of the distribution, it is often verified if the cumulative distribution function, *P<sub>K</sub>(k)*, presents a power-law behavior. Figure 3 reports the exceedance probability of the node degree, 1 − *P<sub>K</sub>(k)*. A power law decay with exponent equal to −2 is clearly observable in the intermediate range, *k∈[0.005, 0.025]* (see the red line in Fig. 3).

The weighted average topological distance, *D̂<sub>i</sub>*, is represented in the top panel of Fig. 4. The scale of values is restricted to the interval [6,12], while higher values are reported without distinction with the grey color. The grey-colored regions individuate the nodes of the micro-networks. In fact, as mentioned in the *Materials and Methods* Section, disconnected components of the graph have extremely high *D̂<sub>i</sub>* values. In the worst case, when a micro-network has two nodes only, *D̂<sub>i</sub> = N − 1 = 1673*. This situation occurs for 18 nodes out of 1674.

As a first comment, there is quite a notable correspondence between high degree centrality and low weighted average topological distance, and vice versa. This is especially evident, on one hand, for large *k<sub>i</sub>* values as in the supernode areas, whose nodes have the lowest *D̂<sub>i</sub>* values. On the other hand, regions with the highest *D̂<sub>i</sub>* values (grey and red colored zones in the top panel of Fig. 4) have *k<sub>i</sub> → 0*. Few remarkable exceptions to this inverse correspondence are the Atlantic Coast of South-America, the

![img-3.jpeg](img-3.jpeg)

Figure 3. Exceedance probability of the node degree, 1 − *P<sub>K</sub>(k)*. doi:10.1371/journal.pone.0071129.g003

Mongolian area and the Indonesian archipelago. For these regions medium-low *D̂<sub>i</sub>* values do not correspond to appreciably high degree centrality values. It should be noted that the North-American and European regions have quite the same low *D̂<sub>i</sub>* values.

At this stage, it is useful to compare the weighted average topological distance map, *D̂<sub>i</sub>*, with the average physical distance map, *L̂<sub>i</sub>*, offered in the bottom panel of Fig. 4 (the scale of values is in 10<sup>3</sup> km). Some regions (Northwestern Europe, Central Asia and Mongolian area, African Sahel region) have both measures with quite low values and one can infer that the strong topological connection is partially due to the high physical closeness of the nodes involved. However, leaving aside these regions, for the rest of the network there exists an inverse correspondence between the weighted average topological distance and the average physical distance. This aspect is more marked in the Southern Hemisphere, where the average physical distance between active cells is in general higher and, at the same time, nodes are often topologically close one to each other. To this end, one can refer in particular to the Atlantic Coast of South America and Eastern Australia, but also South-Africa, Mid-Western US, Northern South-America and the Indonesian Archipelago. Nevertheless, the inverse proportionality between *D̂<sub>i</sub>* and *L̂<sub>i</sub>* is visible in topologically low connected areas such as Eastern Asia, which is instead a region whose cells on average are not physically far from the rest of the network.

To carry out a sensitivity analysis of the network with respect to the physical neighborhood of the nodes, we here define that an edge between nodes *i* and *j* exists if |*R<sub>ij</sub>*| > τ and, at the same time, the additional physical constraint, *l<sub>ij</sub>* > δ = 1000 km, is satisfied. In so doing, a different network is specified where edges between nodes distant less than δ cannot exist.

The degree centrality and the weighted average topological distance are presented in the left and right panels of Fig. 5, respectively. The current scenario deeply emphasizes the role of the supernode areas of the original network (the African Sahel region and Eastern Australia), which are still the regions with the highest degree centrality and the lowest weighted average topological distance. All the other previously existing links are instead weakened or, in several cases, even broken, meaning that their correlation was due to the physical closeness of the nodes involved. In particular, it is worth noting that the US and Western Europe show now very different patterns. Indeed, Western Europe still preserves a large number of highly connected nodes, while the

![img-4.jpeg](img-4.jpeg)

Figure 4. Weighted average topological distance and average physical distance. (top) Weighted average topological distance, $D_t$. The scale of values spans in the interval [6,12]. Higher values are reported without distinction with grey color. (bottom) Average physical distance, $L_t$. The scale of values is in 10³ km. doi:10.1371/journal.pone.0071129.g004

US have a small amount of nodes which are scarcely connected to the rest of the network.

The evident absence of nodes in Asia and North-America (and the poor connection of the few remaining cells) can be thought in terms of the presence of strong precipitation variation on a relatively short spatial scale, thereby leading to the emergence of high precipitation gradients. A high precipitation gradient can be, for instance, enhanced by the occurrence of regional extreme events (e.g., tropical cyclones, monsoons, tornadoes, blizzards, heat waves) which are usually localized in time and space. The Asian and North-American continents, due to their huge land mass extension, experience the most imponent extreme phenomena [51]. Therefore, in these places precipitation strongly varies on regions which are relatively close one to the other, allowing only short-range links to survive, which are eventually broken by the additional physical constraint, $l_0 > 1000$ km. Examples of these high precipitation gradient areas are South-East and North-West China, Central Asia (including Mongolia, Kazakhstan and Central Russia), India, Nepal and Pakistan, as well as Western (Washington, Oregon and California), Central (Texas, Louisiana, Oklahoma, Arkansas, Kansas, Nebraska, Missouri, Iowa and Minnesota), and Southeastern (Florida, Mississippi, Alabama) United

![img-5.jpeg](img-5.jpeg)

Figure 5. Long-range network, $l_l$ > d = 1000 km. (left) Degree centrality. (right) Weighted average topological distance. The scale of values spans in the interval [8,16], while higher values are reported without distinction with grey color. doi:10.1371/journal.pone.0071129.g005

States. In all these cases, the high precipitation gradient makes extremely dry and extremely wet regions coexist in a few hundred kilometers range.

In the supernode regions (Sahel, Eastern Australia and Western Europe) extreme events in general occur less frequently. Medium (Western Europe) or very low (Sahel, Eastern Australia) rainfall spread out more uniformly on a continental scale, the precipitation gradient is weaker and nodes remain connected in the long-range.

Coming back to the original network with *N* = 1674 nodes, the local clustering coefficient and the betweenness centrality are presented in the top and bottom panels of Fig. 6, respectively (note that a logarithmic representation is adopted for the betweenness centrality). These two measures are a little less significant and weakly related to the degree centrality and the weighted average topological distance maps. In fact, both distributions in Fig. 6 are spotted worldwide without evidencing regions of particular interest.

From a qualitative point of view, the local clustering coefficient presents a strong heterogeneity in the central part of Africa, in Eastern Asia and South America. Some patterned zones with high *C<sub>i</sub>* values are found on coastal regions: Brazil, Eastern Australia and Eastern Africa. More in general, *C<sub>i</sub>* seems to mainly vary

![img-6.jpeg](img-6.jpeg)

Figure 6. Local clustering and betweenness centrality mea-
sures. (top): local clustering coefficient, *C<sub>i</sub>*. (middle): Probability density function, *p*(*C*), of the local clustering coefficient, *C*. The red line represents the global clustering coefficient, *C* = 0.5233. (bottom): betweenness centrality (ln(*BC<sub>i</sub>* + 1) plot is shown). doi:10.1371/journal.pone.0071129.g006

around the values represented by the green and yellow tones (*C<sub>i</sub>* ∈ [0.45,0.65]). As plotted in the middle panel of Fig. 6, the probability density function of the local clustering coefficient, *p*(*C*), quantitatively confirms this behavior by showing a moderately trimodal distribution. The central mode, by far the most probable one, lies very close to the global clustering coefficient value, *C* = 0.5233 (see the red line in the middle panel of Fig. 6), which is the arithmetic mean of the *C<sub>i</sub>* values. Going back to the meaning of this parameter, the present results can be interpreted as follows: on average, there is about 32% of chances that two randomly chosen neighbors of node *i* are also neighbors.

The betweenness centrality unveils the importance of a node in the network. Bottom panel of Fig. 6 summarizes that the nodes of the micro-networks and, more in general, nodes which are poorly connected to the rest of the network are the least important ones. These regions are depicted in dark blue. This result is not trivial, since the contrary (highly connected nodes are important) is not true. In fact, the importance of supernode areas and regions with low *D<sub>i</sub>* values is not detectable at all from the betweenness centrality map.

The shortest path distribution for 4 significant nodes can be observed in Fig. 7. We recall that the shortest path length, *d<sub>ij</sub>*, is the minimum number of edges that have to be crossed from node *i* to node *j*. The four nodes are chosen as examples of relevant behaviors. Two nodes in the Northern and Southern Europe regions are shown in panels A and B, respectively. The Northern Europe node is closely linked to the whole European region and Western Russia. Meanwhile, a topological connection of the same strength is found with Northern and Central America. This pattern can be qualitatively associated to the Gulf Stream impact and to the atmospheric circulation induced by the North Atlantic Oscillation (NAO) [52]. Important connections are also visible with the Australian and African Sahel regions, while the farthest nodes are located in Eastern Asia. Although not physically distant from the Northern Europe node, the Southern Europe node presents a quite different scenario (see panel B). A strong connection is evident with the European and African Sahel regions only, while the links with the American and Australian continents are weaker. The node in the Southern part of America (panel C) is not deeply related to the confining Brazil region, but rather with the Caribbean America as well as with the Indonesian archipelago and Australia. Regions which are fairly linked with this node are the African Sahel, Western Russia and the Mongolian area. As a last example of shortest path length, we consider a node in Eastern Asia (panel D), which is a region with the highest weighted average topological distance (see the top panel of Fig. 4). The Eastern Asia node is topologically well connected only to those nodes which are also physically close to it. The whole European and American continents, which are physically distant, are furthermore vaguely linked to this node. In this case only, the topological distance is somehow related to the physical distance.

Some of the patterns linking mid-latitude to tropical nodes (e.g., North-American and European nodes with Sahel, Indonesian and Central America nodes) seem to suggest the impact of the propagation of planetary waves on precipitation at a global scale level [53]. Beside the influence of stationary planetary waves on the precipitation at local scale [54,55], it was recently found that extreme events simultaneously occur worldwide in concomitance with the amplification of trapped planetary waves [56].

Nevertheless, some links can be qualitatively related to the oceanic and atmospheric circulation [51]. In addition to the Gulf Stream and the NAO effects revealed by the shortest path of Northern Europe node (Fig. 7A), the South-Equatorial Current

![img-7.jpeg](img-7.jpeg)

Figure 7. Shortest path, d<sub>0</sub>, of 4 significant nodes of the network. The measured nodes are represented in each panel by a pink square. (A) Northern Europe, node coordinates: (0° E, 53.75° N). (B) Southern Europe, node coordinates: (16.25° E, 38.75° N). (C) South America, node coordinates: (70° W, 36.25° S). (D) Asia, node coordinates: (115° E, 28.75° N). doi:10.1371/journal.pone.0071129.g007

(linking the Pacific Coast of South America to Eastern Australia and Indonesian Archipelago) and the Brazil Current (linking the Atlantic Coast of South America to the Atlantic Coast of Africa) can be individuated for the South America node (Fig. 7C). The Australia node (see Fig. S1) is affected as well by the South-Equatorial Current branch going from Australia to South Africa. The Africa node (see Fig. S2) is related to the Atlantic Coast of South America through the Brazil Current.

The different patterns expressed by the four nodes in Fig. 7 can be also observed through the physical area connected to each node as a function of the topological distance, see Fig. 8. Although the European trends are similar, the Southern node has significantly lower values in the range d<sub>0</sub>∈[5,10]. Moreover, there is a striking difference between the South America and Asia nodes. In fact, for d<sub>0</sub>∈[4,9], the area connected to the South-American node is up to six/seven times larger than the area linked to the Asia node.

In (Text S1), an animated representation of the shortest path linking a node to the rest of the network - is displayed for the nodes

![img-8.jpeg](img-8.jpeg)

Figure 8. Physical area connected to a node as a function of the topological distance, d<sub>0</sub>. The four nodes of Fig. 7 are displayed. doi:10.1371/journal.pone.0071129.g008

presented in Fig. 7 (see Movies S4, S5, S6, S7) and for other meaningful nodes of the network (see Figures S1, S2, S3 and Movies S1, S2, S3).

We conclude this section offering a possible climatological interpretation of two measures, the weighted average topological distance, D̅<sub>t</sub>, and the betweenness centrality, BC<sub>k</sub>, which both rely on the concept of shortest path. As in complex network theory these two parameters are used to measure the information flow, here they should be intended as indexes of short- and long-range connections. Nodes with low D̅<sub>t</sub> values are in general connected on a larger topological scale where precipitation varies more uniformly (e.g., Sahel region, Eastern Australia, Western Europe), while high D̅<sub>t</sub> values describe regions with short-range connections, due to their higher precipitation variability (e.g., Southeastern Asia). The interpretation of the betweenness centrality is not so straightforward since it represents a mediator of both long- and short-range connections, which equally contribute to the final value of a node they pass through. As a consequence, the information on short- and long-range connections is partially lost. This is the reason why the betweenness centrality map is spotted, without remarkably patterned regions, and it is not very meaningful for the precipitation network.

## Conclusions

The recent development of complex network theory is offering new quantitative tools to disentangle the global climate dynamics. In spite of teleconnections having long been studied in climatology, the idea to read climatic correlations among different Earth regions as forming a complex network is relatively new. Starting from this point of view, we have focused on the global precipitation network. To this aim, we have used reliable datasets of measured land-surface precipitation that have only recently become available. Paying attention not to introduce spurious correlations due to uneven partitions of the Earth surface and to have a sufficient number of measured data in each cell, correlation

analysis (with cut-off at 0.5 ) performed on a 70 year-window has yielded an undirected and symmetric network with 1674 nodes and 9481 links. We have investigated the structure of this precipitation network by some topological properties of nodes (degree centrality, local clustering coefficient, etc.) and, in particular, we have introduced a weighted form of the average topological distance in order to prevent some misleading behaviors when the graph has disconnected components.

Some key aspects of the precipitation network clearly emerge. Firstly, supernodes (i.e., highly connected nodes) occur in the Sahel region in Africa and in Eastern Australia, and a scaling-law behavior is revealed in the node degree distribution. Sahel and Eastern Australia regions are some of the most arid areas in the world. Very low rainfall is uniformly distributed on continental scales and huge extreme events are rare. As a consequence, the precipitation gradient tends to weaken, making these regions well connected on a large spatial scale. This long-range connection is confirmed by the fact that Sahel and Eastern Australia remain supernode regions also in the long-range network (see Fig. 5).

Strongly connected zones are evident also in Northern Europe, Central Asia, Western US, and Northeastern Brazil, even if they are not always characterized by a high betweenness centrality. Remarkably, strong connection differences occur between Northern and Mediterranean Europe as well as between Western and Eastern US. The European differences can be explained by the fact that Northern regions are mostly influenced by the oceanic circulation of the Gulf Stream and the atmospheric effects of the NAO (as observed in Fig. 7A), while Southern Europe is more affected by the Mediterranean, Saharan and Caucasian circulation (as shown in Fig. 7B). Differences for the US connections reflect the emergence of high precipitation gradients, which are partially due to frequent extreme events, and the ENSO influence on Western [32,57] and Eastern [58] US precipitation. Nevertheless, Eastern and Western Coasts are reached by very different ocean patterns: the Gulf Stream on the Atlantic Coast and the North Pacific Current on the Western Coast.

A second key point is the high topological distance of the Pacific region of the Asian continent with respect to the rest of the network. Notice that this behavior is not spuriously due to a geographic reason - namely, the decrease of lands above sea level close to the considered region - but it seems a peculiar feature of the precipitation network. A possible explanation of this network characteristic is the dramatic emergence of monsoons, tropical cyclones and heat waves which reduce the correlation only the to short-range scale. A similar disconnected behavior, even if less marked, is also observable for some coastal regions on the Southern Mediterranean and in Ethiopia. It should be noted as well that islands such as Iceland, Madagascar, New Zealand, and Japan, are completely disconnected from the rest of the network, forming different micro-networks. In fact, islands, which are in general more subject to extreme events [59], are not reached by the influence of the continental land mass and are furthermore exposed to the specific oceanic currents.

Finally, the shortest path distribution proved to be a powerful tool to unveil how information about precipitation in a node is linked to the network. Some geographic regions are embedded in very connected portions of the network and a few jumps between neighboring nodes are sufficient to cover large geographic regions; vice versa, other nodes turn out to be quite isolated from the rest of the network. The same tool is also useful to highlight the geography of this information flux about precipitation. For example, we have shown the case of two nodes in Europe that,
in spite of their closeness, exhibit two rather different connection areas.

The reported results highlight that the complex network approach can be an useful framework to explore the huge amount of climatic data that have been collected in the last years and, then, shed light on climate dynamics.

## Supporting Information

Text S1 Shortest path of significant nodes of the network.
(PDF)
Figure S1 Shortest path of the Australia node (coordinates: $141.25^{\circ} \mathbf{E}, 26.25^{\circ} \mathbf{S}$ ) represented by a pink square. (EPS)

Figure S2 Shortest path of the Africa node (coordinates: $3.75^{\circ} \mathbf{W}, 13.75^{\circ} \mathbf{N}$ ) represented by a pink square. (EPS)

Figure S3 Shortest path of the US node (coordinates: $105^{\circ} \mathbf{W}, 41.25^{\circ} \mathbf{N}$ ) represented by a pink square. (EPS)

Movie S1 Animated representation of the shortest path of the Australia node (coordinates: $141.25^{\circ} \mathbf{E}, 26.25^{\circ} \mathbf{S}$ ) displayed in Fig. S1. The node is indicated by a pink square. (AVI)

Movie S2 Animated representation of the shortest path of the Africa node (coordinates: $3.75^{\circ} \mathbf{W}, 13.75^{\circ} \mathbf{N}$ ) displayed in Fig. S2. The node is indicated by a pink square. (AVI)

Movie S3 Animated representation of the shortest path of the US node (coordinates: $105^{\circ} \mathbf{W}, 41.25^{\circ} \mathbf{N}$ ) displayed in Fig. S3. The node is indicated by a pink square. (AVI)

Movie S4 Animated representation of the shortest path of the Northern Europe node (coordinates: $0^{\circ} \mathbf{E}, 53.75^{\circ} \mathbf{N}$ ) displayed in Fig. 7A of the main text. The node is indicated by a pink square.
(AVI)
Movie S5 Animated representation of the shortest path of the Southern Europe node (coordinates: $16.25^{\circ} \mathbf{E}$, $38.75^{\circ} \mathbf{N}$ ) displayed in Fig. 7B of the main text. The node is indicated by a pink square.
(AVI)
Movie S6 Animated representation of the shortest path of the South America node (coordinates: $70^{\circ} \mathbf{W}, 36.25^{\circ} \mathbf{S}$ ) displayed in Fig. 7C of the main text. The node is indicated by a pink square.
(AVI)
Movie S7 Animated representation of the shortest path of the Asia node (coordinates: $115^{\circ} \mathbf{E}, 28.75^{\circ} \mathbf{N}$ ) displayed in Fig. 7D of the main text. The node is indicated by a pink square.
(AVI)

## Author Contributions

Conceived and designed the experiments: SS FL LR. Performed the experiments: SS. Analyzed the data: SS FL LR. Wrote the paper: SS.
