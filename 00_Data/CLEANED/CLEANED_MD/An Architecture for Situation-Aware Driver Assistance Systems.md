# An Architecture for Situation-Aware Driver Assistance Systems 

Matthias Röckl, Patrick Robertson, Korbinian Frank, Thomas Strang<br>German Aerospace Center, Institute of Communications and Navigation

# Motivation

- To detect hazardous situations early, precise and reliable, relevant situational information has to be observed and assessed
- Much situational information is already available in current vehicle technology but is not exploited at present

![img-0.jpeg](img-0.jpeg)

*Source: http://www.youtube.com/watch?v=CFWhcwtgqQU*

*Source: http://www.youtube.com/watch?v=QKjUz6z8vmA*

*Slide 2 > An Architecture for Situation-Aware Driver Assistance Systems > Matthias Röckl*

*DLR* **Deutsches Zentrum für Luft- und Raumfahrt e.V.**

*in der Helmholtz-Gemeinschaft*

*65th Vehicular Technology Conference VTC2007-Spring > 25.04.2007*

# Driver Assistance
## Active Safety Applications

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

Slide 3 > An Architecture for Situation-Aware Driver Assistance Systems > Matthias Röckl
65th Vehicular Technology Conference VTC2007-Spring > 25.04.2007

# Cooperative Active Safety Applications 

$\checkmark$ Vehicle-2-X-Communication (V2X): Exchange of information between vehicles and between vehicle and infrastructure with wireless vehicular ad-hoc networks (VANET)
$\checkmark$ Cooperation: Situational information exchange in VANETs to achieve a global utility maximization
$\checkmark$ Examples:
$\checkmark$ Lane Change Warning
$\checkmark$ Traffic Jam Ahead Warning
$\checkmark$ Cooperative Merging Assistant
$\checkmark$ Static/Dynamic Black Spot Warning

# Architectural Components

![img-3.jpeg](img-3.jpeg)


![img-4.jpeg](img-4.jpeg)

# Utility-based Knowledge Exchange 

"Catch 22": High situation awareness vs. low channel load
$\checkmark$ High situation awareness requires high information exchange, BUT high channel load increases packet drops
$\checkmark$ Question: Which information should be sent when, to whom, in which level of inference by consuming which resource?
$\checkmark$ Key factors:
$\checkmark$ Consideration of partner knowledge: Information selection and prioritisation according to knowledge of the partners
$\checkmark$ Network selection: Affiliation of various types of networks (e.g. WAVE, GSM/UMTS, DAB)
$\checkmark$ Level of inference tradeoff: Compromise of inference level (from raw sensor information to highly inferred information)
$\checkmark$ Nevertheless, privacy constraints (e.g. confidential driver information) have to be considered

# Knowledge Broker
## Modelling uncertainty and causality

- Situation description is subject to uncertainty due to:
  - Noise in sensor data
  - Insufficient temporal or spatial sensor readings
  - Malfunction of sensors
  - Unreliable wireless data exchange
  - Manipulation by malicious intruders
- Modelling of situations by random variables and their causal relations with (Dynamic) **Bayesian networks**
- Application description as pluggable Bayesian network fragments

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

# Reasoning 

## $\checkmark$ Hazard Detection:

Estimation of the situation according to hazard descriptions

## $\checkmark$ Prediction:

Estimation of situational information concerning different context (i.e. for future point in time, at remote location, etc)

## $\checkmark$ Assessment of partner's knowledge:

Estimation of knowledge state of partners (for knowledge dissemination, hazard detection and prediction)

## $\checkmark$ Consistency Check:

Detection of incorrect information

## $\checkmark$ Learning:

Definition or update of network structure and conditional probability distributions

# Conclusions 

Situation Awareness in vehicular environments will increase safety on the road by laying the foundation for novel and sophisticated applications

Single middleware connecting applications (information consumers) and sensors (information producers) is required

Models inherently expressing uncertainty and causality enable learning, hazard detection, prediction, assessment of partner's knowledge and consistency check

Information exchange has to incorporate various factors (network availability, partner knowledge, etc) to maximize the global utility

# Thank you for your attention! 

## Questions?

Matthias Röckl<br>German Aerospace Center (DLR)<br>Institute of Communications \& Navigation<br>Matthias.Roeckl@dlr.de

![img-8.jpeg](img-8.jpeg)

# **Deutsches Zentrum für Luft- und Raumfahrt e.V. in der Helmholtz-Gemeinschaft**

![img-9.jpeg](img-9.jpeg)

Slide 11 > An Architecture for Situation-Aware Driver Assistance Systems > Matthias Röckl
65th Vehicular Technology Conference VTC2007-Spring > 25.04.2007