This item was submitted to Loughborough's Research Repository by the author.
Items in Figshare are protected by copyright, with all rights reserved, unless otherwise indicated.

# Landing site selection during UAS forced landings using decision making Bayesian networks 

PLEASE CITE THE PUBLISHED VERSION
http://dx.doi.org/10.2514/1.I010432
PUBLISHER
© American Institute of Aeronautics and Astronautics
VERSION
AM (Accepted Manuscript)
PUBLISHER STATEMENT
This work is made available according to the conditions of the Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International (CC BY-NC-ND 4.0) licence. Full details of this licence are available at: https://creativecommons.org/licenses/by-nc-nd/4.0/

## LICENCE

CC BY-NC-ND 4.0

## REPOSITORY RECORD

Coombes, Matthew, Wen-Hua Chen, and Peter Render. 2016. "Landing Site Selection During UAS Forced Landings Using Decision Making Bayesian Networks". figshare. https://hdl.handle.net/2134/22828.

# Landing site selection during UAS forced landings using decision making Bayesian networks 

Matthew Coombes, Wen-Hua Chen and Peter Render<br>Loughborough University, Loughborough, LE11 3TU

## I. INTRODUCTION

There is a strong drive for Unmanned Aerial System (UAS) to be integrated into the national airspace system. However, a challenge exists as these UAS must safely and autonomously handle emergency situations as a pilot usually would aboard a manned aircraft. Engine failure is one such situation which has been identified as a critical issue [1].

A forced landing is a complex manoeuvre, that requires research in a number of different areas. First the sites need to be identified using Geographical Information System (GIS) data, and machine vision where the bulk of the research has been conducted [2]. The glide reachability of each site needs to be calculated, which is done simplistically in [3] then extended to include wind and the full manoeuvre in [4]. The landing site needs to be chosen, it must maximise public and airframe safety, discussed in the next paragraph. Finally a path needs to be planned to the chosen site, some of the proposed path planning algorithms are detailed in [5], [6].

An algorithm needs to be developed in order to decide the most suitable forced landing site from a list of known landing sites. There are a vast number of sometimes conflicting criteria that determine the most suitable field for landing. As suggested in [7], decision making is the most important aspect in the initial stage of a forced landing. However, this paper only gives an overview of multi criteria decision making, whilst the work is left for future study. There is some related works that have been conducted for safe landing of commercial aircraft in an emergency [3, 8]. A simple weighted sum decision-making algorithm for commercial aircraft is proposed in [3] to choose an airport within a reachability footprint for an emergency landing. To reduce the probability of "loss of life", [8] proposes to conduct path planning,

[^0]
[^0]:    Research Associate, Dept. of Automotive and Aeronautical Engineering: ttmjc2@lboro.ac.uk
    Professor in Autonomous Vehicles, Dept. of Automotive and Aeronautical Engineering: w.chen@lboro.ac.uk
    Senior Lecturer in Aircraft Aerodynamics, Dept.of Automotive and Aeronautical Engineering: p.r.render@lboro.ac.uk

taking into account risks of four areas involved in the landing process (i.e. en-route, approach, runway and airport) by assigning probabilities based on their associated risks.

# II. FIELD SELECTION CRITERIA 

There are three main criteria for selecting a suitable location for an UAS to attempt a forced landing in order of importance: risk to civilian population, reachability, and probability of a safe landing. These are developed based on the specifications for a forced landing system laid out in [1]. The emphasis is on public safety, where human life and property are more important than the UAS airframe and payload. Mitigating risk to civilian population has a much higher weighting than site reachability and safe landing since aircraft survival is of a lower priority.

## A. Risk to civilian population

As pointed out earlier, the dominant concern in a UAS forced landing situation in civilian airspace is the threat of a crash into people or property. Landing sites close to people or property are given a low rating. This disproportionate rating reflects the low value of the UAS airframe and payload over human lives and property.

## B. Reachability

Previous work in [4] has detailed the reachability analysis of a landing site where the level of reachability is quantified in terms of the excess glide distance $\left(E_{g}\right)$. Flying to a closer site is important as it keeps landing options open and the field can be surveyed much earlier, which gives the aircraft an opportunity to divert to another field if it turns out to be unsuitable. A landing site which is outside of the reachable area is completely unsuitable as the aircraft could crash land anywhere. This can be represented in the Conditional Probability Distribution (CPD) of suitability where $\mathrm{P}\left(\text { suit }^{\max } \mid \text { reach }^{\text {Outofrange }}\right)=0$.

## C. Probability of a safe landing

A technique called the "WOSSSSS" has been widely used by General Aviation (GA) pilots to capture the main factors in making a decision for safe forced landing (e.g. [9, 10]). A GA aircraft is not too dissimilar from an UAS when attempting a safe forced landing at an unprepared site. Therefore, similar factors will be considered in the decision making for UAV forced landing.

- Wind - A good headwind in the landing direction is required to make the landing roll shorter, to minimise the aircraft's kinetic energy relative to the ground, and to maximise survivability.
- Obstacles - There needs to be no obstacles on the approach or landing area (e.g. trees or power lines) to eliminate any chance of collision on landing.
- Size - The site must have an appropriate length for the aircraft to land with a safety factor.
- Shape - The shape of the landing site governs how many landing directions are available to the aircraft on this single landing site. More landing options available means a higher chance of a safe landing.
- Slope - The slope of the landing site shall be flat or uphill to decrease the ground roll of the aircraft.
- Surface - The surface must be suitable to land on, together with a smooth surface without loose material, and free from elevation changes.

To simplify the problem, the probability of making a safe landing can be broken down into two sections: hazards at the landing site and alternative landing options. These can then be evaluated separately.

# III. Forced Landing Bayesian Network Structure 

The Directed Acyclic Graph (DAG) for the Multi Criteria Decision Making (MCDM) Bayesian Network $(\mathrm{BN})$ is constructed using the techniques outlined in [11, 12]. A list of all the nodes, their states and node types are shown in Table 1 while a diagram of the developed DAG is shown in Fig. 1

As described in the previous section, the Suitability (Suit) of a landing site is determined by three criteria nodes: Reachability Reach, safe landing Landing, and civilian proximity (Civ Prox). The CPD for Suit effectively weights the three criteria in the order of preference. There is a greater weighting on Civ Prox than Landing and Reach, which is represented in their CPDs as shown in Table 2. For ease of compiling the CPD for the Landing node, hidden nodes have been used as explained in [13]. CivProx and Reach are pre-calculated, so much of the remaining network is to find the probability of a safe landing (Landing). This is calculated using 5 hidden nodes

The effective size (Eff Size) node encapsulates the relationship between the field length and Wind. The Eff Size of the field increases with a strong head wind and dramatically shortens with a tail wind. Excess landing distance $\left(E_{l}\right)$ is used as a non-dimensional measure of field length, this is the extra landing distance available as a ratio of the total field length.

TABLE 1: List of all node and their discrete states in the proposed BN


TABLE 2: CPD for the utility node Suit, $\mathrm{P}($ Suit $|$ Reach, Landing, CivProx)


Obstacle density (Obs Den) adjusts the danger of obstacles using Eff Size. An larger field with a high obstacle count will be of less concern than the same in a small field as its obstacle density is higher, making obstacles harder to avoid.

The Energy node represents the danger to the landing aircraft from the surface of the landing site by adjusting the danger with Wind. With a Strong Wind, its ground speed is much lower, which makes a surface is less dangerous.

The Land Haz node represents the combined danger of landing from, size, obstacles, and surface type. This is done by combining Eff Size, Obs Den, Energy to the single hidden node Land Haz.

Combining the three chance nodes: Site Opt, Density and Shoot, an overall measure of the field options can be calculated in the hidden node Options, where Density is a measure of how many other fields are reachable from the targeted field.

The decision node Field is the parent of all chance nodes. Each discrete states of Field represents each possible site, the number of states is determined by the number of landing sites (Fn). The CPDs of each chance node is used to enter evidence by instantiating the state that corresponds to the field in question to 1 and setting all other states for that field to 0 . An example is shown in Table 3. This is in order to solve the network for all sites at once. This can be done using diagnostic reasoning, which enables the decision site $D$ to be determined by solving:

$$
D=\underset{\text { Field }}{\operatorname{argmax}} \mathrm{P}\left(\text { Field } \mid \text { Suit }^{\text {Sutiable }}\right)
$$

This is effectively asking which site gives the highest probability of that it is suitable. This is as opposed to the causal reasoning method, which determines the suitability probability $\mathrm{P}\left(\text { Suit suitable }\right)$ for each site as below:

$$
D=\underset{\text { Suit }^{\text {Sutiable }, i \in(1, F n]}}{\operatorname{argmax}} \mathrm{P}\left(\text { Suit } \mid \text { Field }_{i}\right)
$$

where $i$ is the index for each site.
Each landing site can represent more than one entry in Field as there could be more than one landing direction at that site in accordance with Site Opt. While most of their parameters are the same, the states of Wind may change as the landing directions may be different.

TABLE 3: $\mathrm{P}(C P \mid F)$ CPD for the Civilian Proximity node with three fields


![img-0.jpeg](img-0.jpeg)

Fig. 1: The DAG structure for the proposed force landing multi criteria decision making Bayesian Network

This network is to be run online. Upon an engine failure, the aircraft needs to react instantly and make a landing site decision. Being able to run online is also important since there could be inaccuracies in field data, which can only be corrected when the aircraft is close to the landing site. As this is a discrete BN, a small change in $E_{g}$ may lead to a state change in Reach which could change the decision if there are a number of similarly suitable landing sites. Consequently this could result in poor behaviour by the aircraft changing directions repeatedly. This can be prevented by allowing the decision to be changed in flight only if a non-dynamic parameter is changed, i.e. all but Reach.

# IV. RESULTS 

Using a pre-mapped area with known field locations and parameters, a simulation is run to demonstrate the use of the presented decision making algorithm. A map with fourteen pre-surveyed fields is shown in Fig. 2 with discrete criteria states of each landing site shown in Table 4. A single landing direction is considered for each landing site in this example. The scenario is a Cessna 182 in climb-out after taking

TABLE 4: Field parameters


off from Nottingham aerodrome. It has an engine failure at 400 meters above ground level with a wind speed of $10 \mathrm{~m} / \mathrm{s}$ from $270^{\circ}$. Using the reachability analysis algorithm laid out in [4], the proposed MCDM BN, the most suitable site to land in will be selected. Fig. 2 shows an example path used to calculate the landing site reachability. While a Cessna 182 is not a UAS, this system is also suitable for use by GA aircraft as an aid in a situation where they have an engine failure.

As the aircraft's engine fails, the chosen decision landing site is taken from the BN running real time. From the point that the aircraft's engine fails, the marginal posterior distribution for Field is calculated and updated with the arrival of new information, as shown in Table 5. Landing site 13 is the site chosen to attempt the forced landing into, as it has the highest marginal posterior probability of 0.1445 . It is the favoured choice because it is a long field with over $50 \%$ extra length than required, medium reachability, a safe grassy surface, free from obstacles, having both an overshoot and an undershoot, far from the civilian population, and with a medium field density. Landing site 8 is similar and it seems it should be more favourable due to its Med wind state as opposed to Light. However, it is not favoured since there is uncertainty in its obstacle state, represented as $70 \%$ chance of a Low obstacle state and $30 \%$ of a High state. This is an example showing that the BN can handle uncertainty and make use of (soft) evidence in decision making. After injecting this soft evidence into $O b s$, the marginal of Landing site 8 is 0.122. Once the aircraft flies close, it confirms that it is of low obstacle state (i.e. 1 for the Low obstacle), consequently its calculated marginal becomes the highest so will be chosen as the landing site.

If a field decision was selected using the slower casual inference method used in [14], the marginals

![img-1.jpeg](img-1.jpeg)

Fig. 2: Cessna 182 on climb-out from Nottingham aerodrome, suffering an engine failure at 400m AGL. with potential landing sites and landing directions

TABLE 5: Field marginal posterior distribution & Field Suitability marginal posterior distribution


for Suit for each field are also shown in $3^{\text {rd }}$ and $4^{\text {th }}$ columns of Table 5. It can be seen that it reaches the same decision outcome but takes much longer to compute. When running on an Intel i7 computer, the proposed MCDM BN can be run at 4 Hz whereas the casual inference network operates at 1 Hz .

# V. CONCLUSION

The knowledge of a human pilot in evaluating landing sites and making site selection decisions in a forced landing is captured and implemented by a multi criteria decision making BN. It has been identified that public safety is of greater importance, therefore sites without people or property are given highest priority in the network decision making. An underutilised method of solving the BN using diagnostic

reasoning is employed which significantly improves upon computational speed over the causal reasoning method. This enables real-time decision making. The added advantage offered by this method is that it can handle uncertainty in the applied factors without extra modification or effort. An example scenario is presented to show the principle of the networks and verify the effectiveness of the proposal decision making network in an emergency. Further investigation of the decision making behaviour will be conducted by generating a large number of random scenarios.
