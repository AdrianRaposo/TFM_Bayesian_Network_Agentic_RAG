![img-0.jpeg](img-0.jpeg)

Affiliation:<br>${ }^{1}$ First Quantum Minerals Limited, Zambia.<br>${ }^{2}$ Aalto University, Department of Civil Engineering, Finland.

Correspondence to:
R. Mishra

Email:
riteshmining@gmail.com

## Dates:

Received: 14 Jan. 2019
Revised: 15 Apr. 2020
Accepted: 14 Mar. 2021
Published: June 2021

## How to cite:

Mishra, R., Uotinen, L., and Rinne, M. 2021
A Bayesian network approach for geotechnical risk assessment in underground mines.
Journal of the Southern African Institute of Mining and Metallurgy, vol. 121, no. 6, pp. 287-294.

DOI ID:
http://dx.doi.org/10.17159/24119717/581/2021

## A Bayesian network approach for geotechnical risk assessment in underground mines

## R. Mishra ${ }^{1}$, L. Uotinen ${ }^{2}$, and M. Rinne ${ }^{2}$

## Synopsis

Underground mining gives rise to geotechnical hazards. A formal geotechnical risk assessment can help to forecast and mitigate these hazards. Frequentist probability methods can be used when the hazard does not have many variables and a lot of data is available. However, often there is not enough data for probability distributions, such as in the case of new projects. The risk assessment is often subjective and qualitative, based on expert judgement. The purpose of this research is to present the use of Bayesian networks (BNs) as an alternative to existing risk assessment methods in underground mines by combining expert knowledge with data as it becomes available. Roof fall frequency forecasting using parameter learning is demonstrated with 1141 sets of roof fall data across 12 coal mines in the USA. The prediction is nearly identical for individual mines, but when multiple mines are evaluated it is difficult to find a single best fit distribution for annual roof fall frequency. The BN approach with TNormal distribution was twice as likely to fit the observed data compared to the Poisson distribution assumed in the past. A hybrid approach using BN combining multiple probability distribution curves from historical data to predict annual roof fall is proposed. The BN models can account for variability for multiple parameters without increasing the complexity of the calculation. BNs can work with varying amounts of data, which makes them a good tool for real-time risk assessment in mines.

## Keywords

Bayesian network; expert opinion models; geotechnical risk; incident forecasting; parameter learning; roof fall risk.

## Introduction

Geotechnical risks increase as mines progress deeper, and these risks are commonly managed using probability-based risk assessment (Dershowitz and Einstein, 1984; Galvin, Hebblewhite, and Salmon, 1999; Baecher and Christian, 2003; Mishra et al., 2017). The challenge with this approach is the lack of suitable data. Often there is not enough data for probability distributions, and historical data cannot be used for new projects in areas with no prior mining activities. The risk assessment is often subjective and qualitative, based on expert judgement. This paper aims to present the use of Bayesian networks (BNs) as an alternative method for risk assessment in underground mines. Spalling depth and roof collapse predictions are used as examples.

While qualitative assessment helps to carry out a quick risk assessment in the absence of data, it can be very broad and vague and can be highly influenced by personal opinion and bias. The variability of the condition of the rock mass compounds the problem as operations can run into previously unknown geological structures. Mining at great depth also means that collecting geotechnical information through conventional methods such as core drilling is very expensive. Non-intrusive geophysical methods involve limitations of coverage, range, and accuracy. Because of the uncertainty of geotechnical conditions with increased depth (e.g. geological contacts, rock properties), a formal geotechnical risk assessment outlining the scope, methodology, and resource requirement is preferable (Mishra and Rinne, 2014). The risk management framework should have a feature that enables it to learn from the data gained as mining progresses deeper.

Where historical frequencies of incidents are available, appropriate probability distributions can be used to forecast future failures. Duzgun and Einstein (2004) demonstrated the use of the Poisson distribution to forecast roof collapses in coal mines. Given the variability in mining conditions associated with each roof failure, it is often difficult to select one distribution which best describes all roof collapses. This paper extends their work by performing parameter learning on roof fall data across 12 mines and 1141 roof fall incidents to create probability distributions.

When extensive data is available, analytical design methods can be used to calculate the factor of safety. Significant variability in data can lead to conservative and expensive reinforcement design.

# A Bayesian network approach for geotechnical risk assessment in underground mines 

Probabilistic analyses (PoF) account for the variability in data and are often used today, as opposed to deterministic analyses. This paper combines the factor of the safety method for reinforcement design against roof collapse in underground mines with a Bayesian network to address the variability of the underlying data.

Risk assessment methodologies and approaches for the underground mining industry have been discussed extensively in the past (Brown, 2012; Mishra and Rinne, 2014; Eskesen et al., 2004; Paté-Cornell and Dillon, 2006; Paté-Cornell, 2007). Einstein and Baecher (1983) proposed that mining projects should be evaluated for their geotechnical risk levels through Geotechnical Risk Classification (GRC) from as early as the pre-feasibility study, and these values should be updated as the project progresses and more data becomes available. Kelly and Smith (2009) discussed the current state of the art of Bayesian inference in probabilistic risk assessment. Work has been done in the past using Bayesian networks to model major accidents using near misses (Khakzad, Khan, and Paltrinieri, 2014). Bayesian networks have also been used in dam risk assessment (Smith, 2006; Li, Yan, and Shao, 2007), tunnel risk assessment (Sousa and Einstein, 2007; Spackova and Straub, 2011), modelling uncertainties in rockfall hazards (Sousa and Einstein, 2012), safety assessment in construction projects (Zhang et al., 2014), and dynamic failure assessment in process plants (Meel and Seider, 2006). This paper discusses the use of BNs to convert probabilistic risk assessment from a frequentist approach to a Bayesian approach. It demonstrates how BNs can be used as an alternative to test the goodness of fit of competing probability distributions.

## Methodology

Geotechnical risk is defined as a product of the likelihood of the geotechnical hazard and the severity of the consequence if the hazard were to be realized. Bayesian networks can be used to carry out both the likelihood and consequence assessment for a given hazard. In this paper, a BN has been used only to evaluate the likelihood of a roof or block collapse.

Bayesian networks or Bayesian belief networks are based on Bayes' theorem (Bayes and Price, 1763). They describe the conditional relationship between two or more variables using probability as defined in Equation [1].

$$
P(H \mid E)=[P(E \mid H) \times P(H)] / P(E)
$$

where $H$ and $E$ represent a hypothesis $(H)$ being tested and corresponding evidence $(E)$ to support this hypothesis. $P(H \mid E)$ is called the posterior probability, which is the probability of the hypothesis $(H)$ being true given particular evidence $(E) . P(E \mid H)$ is called the likelihood, which is the probability of observing evidence $(E)$ if the hypothesis were true. $P(H)$ is called the priori, which is the prior belief in the hypothesis. $P(E)$ is called the marginal likelihood, which represents the prevalence of the evidence in the base population. For instance, in a mining context, it is assumed that large angular discontinuities cause roof collapse. This assumption can be treated as one of several hypotheses in BNs that lead to roof collapse. $P(H \mid E)$ for this hypothesis can be written as $P($ large angular discontinuity / roof collapse). $P($ large angular discontinuity), or the priori, would be the frequency rate of large angular discontinuities in the mine, such as an 'average of 10 discontinuities per mine'. $P$ (roof collapse), or the marginal likelihood, would be the frequency rate
of the roof collapses, such as 'two roof collapses per year'. $P$ (roof collapse / large angular discontinuity), or the likelihood, would be the number of times a large angular discontinuity caused a roof collapse, such as 'one out of two roof collapses was caused by large discontinuities'.

Figure 1 shows the structure of a BN which has been modified from work by Smith (2006) to split the model into a causal model, a BN, and a decision-making model. $H_{-} 1$ and $H_{-} 2$ are examples of two hypothesis nodes leading to the evidence node $E$. The hypothesis and evidence nodes, along with the solid directional arrows, form the causal model. The circular nodes and solid arrows form the BN causal model, while the dotted arrows represent the flow of information in a BN. The circular nodes at the origin of the solid arrows are called 'parent' nodes ( $P(H_{-} 1)$, $P(H_{-} 2)$ ), while the nodes at the end of the solid arrows are called 'child' nodes.

Relationships between the nodes are defined with the use of priors and conditional probability tables or cause-effect relationship tables. This model can now be used to evaluate the likelihood of the evidence if the hypothesis is true. This form of inferencing from hypothesis to evidence is called forward inferencing. Observed data can be fed into the same model to back-calculate the likelihood of the hypothesis being true through backward inferencing. This process of forward and backward inferencing creates a decision-making model. The process helps to evaluate and update our prior beliefs in the light of new evidence and thus improve predictions.

The network shown in Figure 1 can now be converted to carry out risk assessment by defining the risk being assessed as the evidence and the contributing factors as hypotheses. The same model can also be used to carry out backward inferencing and parameter learning (Penton and Neil, 2012). To carry out parameter learning, the unknown parameter is defined as the evidence, such as the mean and variance for a normal distribution. The available data is entered into the hypothesis nodes, and the model is solved using Equation [1] to arrive at the likely value for the unknown parameter. All the BNs in this paper are created and solved using Agena Risk version 7 (Agena, 2017). Several Bayesian network modelling software packages are available to carry out the modelling. Agena Risk was chosen over the others because of its ability to deal with continuous
![img-1.jpeg](img-1.jpeg)

Decision Making Model
Figure 1-Decision-making model using a Bayesian network. Circular nodes and solid arrows show the causal model, and dotted arrows show the flow of information (after Smith, 2006)

# A Bayesian network approach for geotechnical risk assessment in underground mines 

variables along with non-numeric nodes. Comprehensive literature on the use of Agena Risk (Fenton, Neil, and Caballero, 2007; Fenton and Neil, 2012) across multiple cases was available, which assisted in the modelling of incidents.

## Spalling depth forecasting using BN and analytical methods

This section discusses the concept of combining analytical methods for estimating the potential for spalling depth in tunnels with BNs. The usage of BNs allows the variability in the collected data to be taken into account better. To enable a direct comparison with existing frequentist methods, we have chosen a case example where a lot of data is available. To demonstrate the use of a BN in conjunction with the analytical method, we have used the spalling estimation method as described by Martin and Christiansson (2009) and the Olkiluoto case data from Siren et al. (2011). The Olkiluoto case describes a high-level spent nuclear fuel repository at a depth of 420 m in hard crystalline rock in Finland.

The failure mechanism that is studied is the formation of thin slabs. Progressively, these slabs form a continuous wedge of spalled material. To establish the size of the wedge to be supported with tunnel reinforcement, the analytical method requires the uniaxial compressive strength (UCS) of the rock and local principal stresses to be known. The factor of safety (FoS) for the roof reinforcement can then be calculated using Equation [2]:

$$
F O S=\frac{\sigma_{s m}}{\sigma_{\theta \theta}}
$$

where $\sigma_{s m}$ is the rock spalling strength and $\sigma_{s o}$ is the tangential stress at the rock surface. The spalling strength is extracted from the UCS of the rock by multiplying by a scaling factor, $k$. For Olkiluoto, UCS is represented by a normal distribution with a mean of 115 MPa and a standard deviation of 23 MPa (Siren et al., 2011), and $k=0.57 \pm 0.02$ has been used for crystalline rock (Martin and Christiansson, 2009). At a depth of 400 m , the major horizontal stress and minor vertical stresses were taken as in Posiva (2009), and to account for data variability both of these were represented by triangular distributions with corners in the lower $10 \%$ fractile, the mean, and the upper $90 \%$ fractile (Table I). Using the Kirsch (1898) equations (Equation [3]), these values can be used to calculate the resulting tangential stress at the rock surface. The shape factor $A=2.60$ was obtained as a median value calculated from the profiles listed in Siren et al. (2011). The uncertainty of the stress direction is omitted for the sake of simplicity.

$$
\sigma_{\theta \theta}=A \sigma_{1}-\sigma_{3}
$$

The FoS (Equation [2]) can now be calculated (Equation [4]). Using the mean values the FoS becomes

Table I
Major horizontal stress and minor vertical stress at Olkiluoto at a depth of 400 m. (Posiva, 2009)


$$
F O S=\frac{\sigma_{s m}}{\sigma_{\theta \theta}}=\frac{k \cdot U C S}{A \sigma_{1}-\sigma_{3}}=\frac{0.57 \cdot 115 \mathrm{MPa}}{2.60 \cdot 25.6 \mathrm{MPa}-10.6 \mathrm{MPa}}=1.17
$$

indicating a small risk of spalling damage at Olkiluoto, according to Siren et al. (2011). The damage depth can be calculated with Equation [5] modified after Martin and Christiansson (2009):

$$
S_{d}=a\left(0.5 \frac{\sigma_{\theta \theta}}{\sigma_{s m}}-0.52 \pm 0.1\right)
$$

Assuming the nominal tunnel radius to be $a=5 \mathrm{~m}$, the corresponding mean damage depth $\left(S_{d}\right)$ is zero ( $\sim 0.46 \mathrm{~m}$ ) and the extreme value using the +0.1 upper limit would, at a maximum, be 0.037 m .

The empirical factor $0.52 \pm 0.1$ describing the observed damage depth in Martin and Christiansson (2009) was modelled using a triangular distribution with a lower limit of 0.42 , mode of 0.52 , and upper limit of 0.62 . The empirical factor is based on nine published case histories (Andersson, 2005; Martin et al., 2001) in a wide range of rock mass conditions and major in-situ stresses ranging from 10 MPa to 140 MPa . The rock types consisted of limestone (UCS 80 MPa ), andesite (UCS 100 MPa ), granite (UCS 220 MPa ), and quartzite (UCS 350 MPa ). The variability of $\sigma_{1}, \sigma_{2}$, and $k$ means that there will be combinations that exhibit spalling despite the FoS being greater than unity.

For spalling strength, the factor $k$ was modelled using a triangular distribution with a lower limit of 0.55 , mode of 0.57 , and upper limit of 0.59 , as suggested in Martin and Christiansson (2009) for crystalline rocks. It should be noted that the factor $k$ is defined for the mean UCS and the UCS is not entered as a distribution. The model allows for any combination of strength and stress, while in reality high stresses are more likely in strong rock and low stresses in weak rock. For weak rocks, the model may result in conservative results. The model may incorrectly predict the spalling phenomenon occurring in weak rocks or the occurrence of high stresses in weak rocks. The analytical method does not reveal what the spatial extent or probability of such damage is. The site-specific acceptance criteria as a function of FoS can be selected based on site-specific observations of FoS when there is no spalling, very minor spalling, or extensive spalling, as suggested in Martin and Christiansson (2009).

For a true deterministic example, the FoS will need to be calculated individually for all combinations of variables. This method requires extensive data collection. In reality, frequentist probability methods are used in conjunction with random sampling (e.g. Monte Carlo) or structured sampling (e.g. Latin hypercube sampling). The disadvantage of the frequentist probabilistic method is that the complexity of the model grows exponentially as the number of uncertain variables increases beyond two (Matarawi and Harrison, 2017). Additionally, the FoS values do not directly give the probability of failure (PoF), but prescribed tables can be used to compare FoS and PoF (Galvin, Hebblewhite, and Salmon, 1999).

Bayesian networks can be used to take the variability into account directly. Accounting for variability eliminates any need to use FoS and establishes the PoF directly. Figure 2 shows the PoF calculation using the BN. The $\sigma_{1}$ and $\sigma_{2}$ nodes were used to calculate $\sigma_{m}$ using Equation [3]. The $\sigma_{s m}$ node was obtained by multiplying the empirical factor $k$ by the mean UCS of 115 Mpa. Factor of safety and spalling depth nodes were obtained using Equations [2] and [5] respectively. The BN model predicts a $92.3 \%$ chance that the FoS will be greater than unity, while

# A Bayesian network approach for geotechnical risk assessment in underground mines 

![img-2.jpeg](img-2.jpeg)

Figure 2-Bayesian network model to forecast spalling and spalling depth using Equations [2], [3], and [4]. Equations [2] and [3] are solved to give 'factor of safety' nodes. Equation [5] is solved using the 'factor of safety' and 'empirical factor' nodes to provide the spalling depth
deterministic calculation using Equation [2] would have resulted in a single FoS value of 1.17. BNs can thus take into account the variability of multiple variables in analytical assessment to make failure predictions. In the presented example, the analysis was carried out in the least favourable direction. If the actual tunnel direction is known, the BN can be expanded to include the variability of the stress orientations. The current approach with the empirical factor $k$ requires the usage of the mean UCS value. If the distribution of UCS is known, the crack initiation strength can be taken as a lower bound estimate for the spalling initiation strength as formation of cracks precedes the onset of spalling.

## Roof collapse forecasting using BN with roof fall frequency data

## Parameter learning on roof fall frequency data for roof fall forecasting

This section discusses the use of parameter learning in a BN to learn distributions from historical roof collapse data in coal mines. It considers the example of roof fall risk estimation using roof fall frequency data collected by the Mine Safety and Health Administration (MSHA) in coal mines situated in the USA. The data is from the period between 1979 and 1997 across 12 anonymized underground mines in the Appalachian region (Duzgun and Einstein, 2004; Mine Safety and Health Administration, 2000). This data has been analysed in the past by curve fitting the accident frequency to an appropriate probabilistic distribution to forecast failure (Duzgun and Einstein, 2004; Einstein, 1997). Mine ID 4601816 was considered for the parameter learning demonstration as it had the largest sample size, with 108 roof fall incidents. Figure 3 shows the annual frequency of the number of roof falls (NoF) in Mine ID 4601816.

Duzgun and Einstein (2004) used an exponential distribution for the time between failures and a Poisson distribution for
the annual roof fall frequency (NoF) to fit the roof fall data for roof fall prediction. The Poisson distribution is a one-parameter probability distribution as shown in Equation [6] for annual roof fall frequency.

$$
P(N O F)=e^{-\lambda} \times\left(\lambda^{N O F} / N O F!\right)
$$

The Poisson parameter lambda $(\lambda)$ is the mean roof fall frequency per year and NoF is the annual roof fall frequency whose probability of occurrence $(\mathrm{P}(\mathrm{NoF})$ ) is being evaluated. Parameter $\lambda$ for the roof fall frequency for the abovementioned mine is 5.68 , using data from Figure 3. In the frequentist approach to risk assessment one value of $\lambda$ is used to plot the probability distribution. Any frequentist interpretation of a statistical parameter is referred as the 'classical approach' in this paper.

The Bayesian approach to solving this problem considers the $\lambda$ parameter of the Poisson distribution as a variable itself. The parameter learning capabilities of the BN can then be used to learn the lambda parameters from the population. Figure 4 shows the BN used to learn the probability distribution of $\lambda$. The parent node lambda $(\lambda)$ was assumed to have a uniform prior probability between 0 and 20 . Uniform prior probability implies that all values between 0 and 20 had the same probability of being equal to $\lambda$. The child nodes to this parent are the number of roof failures occurring in different years, with the annual roof fall frequency on the x -axis and probability distribution (PD) on the y -axis. The conditional probability between lambda and roof fall node is defined by the Poisson equation as shown in Equation [6]. Nineteen child nodes were added to the BN to enter roof fall frequency data available for 19 years, as shown in Figure 4 from Y1 to Y19. An additional node named 'forecasted NOF' was added to show the results of the parameter learning to give the revised roof fall frequency. The BN was solved using the parameter learning to revise the $\lambda$ distribution from the prior uniform distribution. The revised distribution, in turn, provided the 'predicted roof fall frequency'. As the evidence for year 20 becomes available, it can then be added as an additional child node, which will then revise both the $\lambda$ and predicted roof fall frequency distribution in the light of the additional evidence.

When the Bayesian prediction of annual roof fall frequency (NoF) probability distribution (PD) is compared with the classical Poisson distribution obtained from Equation [6], the Bayesian prediction is nearly identical, as shown in Figure 5. Despite being almost identical in probability distribution, both the classical
![img-3.jpeg](img-3.jpeg)

Figure 3-Annual roof fall frequency in Mine 4601816. Number of roof falls (NoF)

# A Bayesian network approach for geotechnical risk assessment in underground mines 

![img-4.jpeg](img-4.jpeg)

Figure 4-Parameter learning BN to learn lambda ( $\lambda=$ mean roof falls per year) from observed roof falls. The $y$-axis shows the probability distribution, while the $x$-axis shows the different values of lambda and forecast annual roof falls for the left and right nodes
![img-5.jpeg](img-5.jpeg)

Figure 5-Classical Poisson vs Bayesian Poisson comparison for annual roof fall (NoF) probability for Mine 4601816
and Bayesian curves are a poor fit to the observed data when a Poisson distribution is assumed. A mathematical comparison of goodness of fit of competing distributions is discussed later in the paper.

The data for Mine 460186 was then assumed to follow a normal distribution with mean and variance replacing $\lambda$ as the parent node. The normal distribution was limited to a lower tolerance of zero annual roof falls and an upper tolerance of 20 annual roof falls, resulting in a truncated normal or TNormal distribution (Thompson, 1950). In order to avoid unreal results of non-integer annual roof falls, the TNormal distribution was constructed using integer intervals in Agena Risk (Agena, 2017). The mean and variance parameters were assumed to have uniform priors. The mean and variance parameters for the normal distribution were learned using parameter learning from the observed data for 19 years, similarly to that carried out in Figure 4. The resulting Bayesian network is shown in Figure 6, while a comparison of the classical Poisson distribution, Bayesian TNormal distribution, and the actual observed data is shown in Figure 7.

The relative error of the forecast value was carried out using Equation [7] for both the Poisson and normal distribution (ISO, 1993).

$$
E=\frac{\sqrt{\left(P_{0}-R F_{0}\right)^{2}}}{R F_{0}}
$$

where $E$ is the relative error in the forecast data, $P_{o}$ is the forecast probability of $n$ roof falls in a year, and $R F_{o}$ is the relative frequency of $n$ roof falls. Using Equation [7], the average relative
error in the forecast using classical Poisson distribution was $55 \%$, which was reduced to $37 \%$ when the Bayesian TNormal distribution was used.

## Using 'goodness of fit' results from multiple distributions for roof fall forecasting

There are mathematical tests, such as Kolmogorov-Smirnov test and the chi-square goodness of fit test, that can be carried out to evaluate how well a proposed distribution fits the data (Ang and Tang, 1984). These tests use statistical parameters such as the mean, which is not directly observed in the population but is inferred from a sample population. An alternative method using BN is to evaluate the frequency with which the historical data (evidence) occurs in the assumed probability distribution (hypothesis) (Fenton and Neil, 2012). This can be modelled using a BN where several probability distributions, in this case truncated normal and Poisson distribution, form the node states for a parent node (Figure 8).

The child nodes are values observed in each of the 19 years for Mine 4601816. The prior probability of the parent node 'Competing distributions' is considered to be $50 \%$ for each, meaning that both the distributions are equally likely to be correct. The conditional probability table for the child node is conditional on the parent nodes as shown in Table II for the node 'Roof fall Y_1'.
![img-6.jpeg](img-6.jpeg)

Figure 6-Parameter learning BN to learn normal distribution parameters from observed roof falls
![img-7.jpeg](img-7.jpeg)

Figure 7-Classical Poisson vs Bayesian normal comparison for roof fall probability in Mine 4601816. Summary statistics of the two graphs are shown in Table II

# A Bayesian network approach for geotechnical risk assessment in underground mines 

![img-8.jpeg](img-8.jpeg)

Figure 8-Goodness of fit test for competing distributions using BN. Roof fall data from 19 years is used to determine the goodness of fit of the competing distribution. Goodness of fit results are used to provide a weighted roof fall forecast

Table II
Node probability table showing the relation between competing distributions and roof fall frequency


The values in parentheses for TNormal represent the mean, variance, lower bound, and upper bound respectively, while the values in parentheses for Poisson show the $\lambda$. These are statistical summary parameters of the Poisson and normal distributions shown in Figure 7. This BN is solved by entering roof fall values from year 1 to year 19, resulting in a posterior probability of $70 \%$ for the Bayesian TNormal distribution and $30 \%$ for the classical Poisson distribution. The posterior probabilities imply that there is a $70 \%$ probability of observing the given data under the Bayesian normal distribution, compared to $30 \%$ under the classical Poisson distribution. In other words, the observed data is more than twice as likely under the Bayesian TNormal distribution compared to the Poisson distribution. Therefore, Bayesian TNormal is a better model for forecasting the roof fall frequency in Mine 4601816. This goodness of fit test using the observed parameters was carried out for all 12 mines, and the Bayesian TNormal distribution was found to be a better fit compared to classical Poisson distribution in seven of the 12 mines. The results of this analysis are shown in Table III.

These results indicate that it is unlikely to have one distribution that is the best fit for roof fall data across different mines. Bayesian networks can overcome this problem by creating a hybrid distribution curve weighted according to the goodness of fit test results. The percentage probability values indicate which of the two distributions is more likely to fit the data better when they are compared. For example, if both truncated normal and Poisson distributions are used to forecast a roof fall in Mine 4601816, the forecast is weighted $70 \%$ in favour of normal distribution and $30 \%$ in favour of Poisson distribution as obtained from the goodness of fit test. Hybrid distributions can be useful in early stages of data collection, where limited data makes it difficult to identify a unique distribution that correctly represents the population. The number of distribution should be limited to two or three as the intention of the hybrid model is to evaluate potential distributions that are expected to describe the population. As additional information becomes available over time, the one distribution that best describes the population should be chosen from the hybrid distribution.

## Discussion

## Bayesian networks for real-time risk assessment

Geotechnical incidents in deep mines can have severe consequences due to both unfavourable mining conditions and the difficulty of rescue and recovery operations following an incident. Real-time risk assessment can help mitigate both the hazard and the consequences through advance warning. Bayesian networks can work with varying amounts of data, which makes them a good tool to carry out a real-time risk assessment at mine sites. Bayesian networks can either be integrated with the existing on-site information management system or strategic instrumentation and monitoring can be implemented once the Bayesian model has been defined.

The process of incorporating real-time risk assessment using BNs is shown in Figure 9. The first step in the process is to define a causal model for a failure such as stope collapse using nodes and probability tables. The contributing nodes can be numeric nodes with continuous values such as stress around the stope, the number of discontinuities, roof convergence, etc. Alternatively, these nodes can be non-numeric, with subjective states such as the quality of the filling in of the discontinuities. If the nodes are non-numeric, the prior probability of each of the nodes will have to be defined. Numeric nodes can consist

Table III
Goodness of fit test results for classical Poisson and Bayesian TNormal distribution for roof fall frequency


# A Bayesian network approach for geotechnical risk assessment in underground mines

of information which is collected, in real time, such as roof convergence measurement using an extensometer, or seismicity using geophones. For these nodes, appropriate site-wide instrumentation needs to be planned in such a way that sufficient data is collected, and their prior probabilities are defined using probability distribution. Numeric nodes can also consist of data, which is collected intermittently through inspection and is not continuous. Joint set numbers, joint roughness, blast vibrations, *etc.* fall into the category of non-continuous numeric nodes. Either these nodes can be defined using a probability distribution or the distribution can be learnt using parameter learning.

After the nodes and their prior probabilities have been defined, the BN is solved for the current risk level on the basis of the available information. As data is fed from real-time instrumentation, the risks are updated in real time to inform the relevant stakeholders. The same network can also be used to feed information on incidents and near misses that occur in the mine to carry out backward inferencing and revise all the prior probabilities. This method also assists with incident investigation to identify the most likely cause of the incident and improve the accuracy of the forecasting model.

## Advantages and limitations of Bayesian network-based risk assessment

Bayesian networks offer the flexibility of working in the absence of historical data by replacing it with expert opinion-based prior probabilities. In conventional frequentist risk assessment, a summary of statistical parameters such as the mean and median is often used to carry out the risk assessment. Even when the full probability distribution is used, the computational requirements increase significantly as the number of parameters increases. BNs, however, can work with complex causal models where each node uses a probability distribution instead of summary statistics. Expert opinion-based risk assessment implies that a BN can quickly adapt to an existing subjective risk assessment practice in the mine. This improves the repeatability of the risk assessment process when performed by different personnel for the same mine. Its ability to perform backward inferencing on a risk assessment model allows the BN to be used for incident investigation. This iterative process of risk forecasting and incident investigation improves the reliability of the model by updating the assumed prior probabilities. Backward inferencing also encourages improved collection of data and rigorous incident investigations. The ability of BNs to work with site instrumentation opens up the possibility of creating a real-time risk assessment and warning system in a mine.

The use of expert opinions in the absence of data is also one of the main disadvantages of BN-based risk assessment. Incorrect prior probabilities lead to incorrect incident forecasts, which need to be validated through incident investigations in the future. The additional poor understanding of incident causation and failure mechanism also results in incorrect forecasts. Given the reliance on experts, it is prone to human error and expert biases. Real-time risk assessment using BNs can be challenging if a large part of the mine needs to be monitored for risk, as this would require extensive instrumentation, which can be expensive. Additionally, BNs can only work on the basis of an underlying causal model. Modelling error or the omission of key influencing factors can lead to incidents not predicted by the warning system. However, after every incident, backward inferencing should be carried out to test whether the causal model explains the incident. If not, additional investigation and instrumentation are necessary in order to improve the warning system.

## Conclusions

Bayesian networks provide a flexible framework for carrying out risk assessment from zero to scarce to an abundant amount of measured data available. They can take into account the full variability of source data by the use of probability distributions. Spalling depth and the risk of roof fall were analysed using the Bayesian approach as an alternative to the analytical method. This approach was also used to convert the factor of safety calculation for spalling into a probability of whether spalling will happen. If spalling takes place, what are the probabilities of

![img-9.jpeg](img-9.jpeg)

**Figure 9—Real-time risk management process flow using BN**

# A Bayesian network approach for geotechnical risk assessment in underground mines 

various spalling depths?
Parameter learning using BNs was demonstrated using roof fall data across 12 mines over 19 years. The results show the weakness in applying a single type of probability distribution that provides the best fit for roof fall frequency in all the mines that were studied. A methodology of combining multiple distributions to produce a weighted forecast was proposed to overcome the challenge of a best fit from a single probability distribution in the presence of limited data. This study indicates that BNs may present a good platform for a real-time risk assessment tool by combining expert knowledge with available data, including online measurements from the field.

## Acknowledgement

The authors gratefully acknowledge the financial support provided by the Online Risk Management in Deep Mines (ORMID) project funded by the Academy of Finland under the grant no. 297770.
