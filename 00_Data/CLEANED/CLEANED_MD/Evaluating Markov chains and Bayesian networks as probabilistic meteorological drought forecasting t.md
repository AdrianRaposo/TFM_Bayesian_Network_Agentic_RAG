# Evaluating Markov chains and Bayesian networks as probabilistic meteorological drought forecasting tools in the seasonally dry tropics of Costa Rica 

Kenneth Gutiérrez-García ${ }^{1,2} \cdot$ Alex Avilés ${ }^{3} \cdot$ Alexandra Nauditt ${ }^{4} \cdot$ Rafael Arce ${ }^{1} \cdot$ Christian Birkel ${ }^{1}$<br>Received: 24 August 2022 / Accepted: 21 August 2023 / Published online: 7 September 2023<br>(c) The Author(s) 2023


#### Abstract

Meteorological drought is a climatic phenomenon that affects all global climates with social, political, and economic impacts. Consequently, it is essential to develop drought forecasting tools to minimize the impacts on communities. Here, probabilistic models based on Markov chains (first and second order) and Bayesian networks (first and second order) were explored to generate forecasts of meteorological drought events. A Ranked Probability Score (RPS) metric selected the best-performing model. Long-term precipitation data from Liberia Airport in Guanacaste, Costa Rica, from 1937 to 2020 were used to estimate the 1-month Standardized Precipitation Index (SPI-1) characterizing four meteorological drought states (no drought, moderate drought, severe drought, and extreme drought). The validation results showed that both models could reflect the climatic seasonality of the dry and rainy seasons without mistaking $4-5$ months of the rain-free dry season for a drought. Bayesian networks outperformed Markov chains in terms of the RPS at both reproducing probabilities of drought states in the rainy season and when compared to the months in which a drought state was observed. Considering the forecasting capability of the latter method, we conclude that these models can help predict meteorological drought with a 1-month lead time in an operational early warning system.


## 1 Introduction

Drought is a climatic feature that affects all climate zones of the planet, and its impact is reflected in social, political, and economic costs (UNDRR 2021; IPCC 2021). For instance, in 2011, the drought in the Horn of Africa affected almost 13 million people, and in 2012, the USA experienced its worst drought since the 1950s, affecting $80 \%$ of croplands (Ki-moon 2014). Other prominent global examples include the decadal droughts in Chile and Australia since

[^0]2010 (Saft et al. 2015; Garreaud et al. 2020). Furthermore, climate change projections for tropical regions indicate that droughts are likely to become more frequent and severe, mainly due to rising temperatures (Van Lanen et al. 2015; UNDRR 2021; IPCC 2021). The Central American Dry Corridor (CADC) is the most vulnerable region in Central America to climate variability and change, as identified by the FAO 2016. A minimum of 4 months without rainfall (dry season) and a population vulnerable to socio-economic change commonly characterize the CADC (Gotlieb et al. 2019; Quesada-Hernández et al. 2019). In 2015, parts of Central America and the CADC experienced one of the most severe droughts in the previous 10 years, as more than 3.5 million people needed assistance; the most significant impacts were reflected in food insecurity, as crops suffered a poor harvest, resulting in large economic losses (FAO 2016).

Despite the socio-economic impacts caused by droughts, Mishra and Desai (2006) alerted of a deficiency in drought mitigation efforts and the limitations in forecasting dry conditions. The importance of drought forecasting, mainly meteorological drought, can be inferred from a decrease in precipitation as the beginning of several cascading effects such as the


[^0]:    $\boxtimes$ Kenneth Gutiérrez-García kenneth.gutierrez-garcia@zalf.de
    1 Department of Geography and Water and Global Change Observatory, University of Costa Rica, San José, Costa Rica
    2 Leibniz Centre for Agricultural Landscape Research (ZALF), Müncheberg, Germany
    3 Grupo de Evaluación de riesgos ambientales en sistemas de producción y servicios (RISKEN), Carrera de Ingeniería Ambiental, Facultad de Ciencias Químicas, Universidad de Cuenca, Cuenca, Ecuador
    4 Institute for Technology and Resources Management in the Tropics and Subtropics (ITT), Cologne, Germany

decrease in soil moisture, streamflows, and groundwater levels, with the consequent impact on agricultural production and societal welfare. Van Loon (2015) defines drought as a sustained period of low water availability compared to average conditions, with spatial and temporal characteristics that vary from one region to another. Wilhite and Glantz (1985) classified drought into meteorological, agricultural, hydrological, and socio-economic drought according to the chronological order of reduced precipitation and its impacts, where meteorological drought is usually defined as the degree of dryness compared to the average amount and duration of a dry period. The degree of dryness is often characterized in terms of duration, severity, and frequency using precipitation indices (WMO; Global Water Partnership 2016; Romero et al. 2020). Among different indices, the most widely applied is the Standardized Precipitation Index - SPI (McKee et al. 1993; WMO 2012). Albeit the SPI does not consider actual rainfall volume due to the normalization process with a fitted statistical distribution, it is a comparable unit-less index (WMO; Global Water Partnership 2016). Nonetheless, the SPI possesses limitations, as, for example, it cannot determine the impact of rising temperatures on future drought patterns (Vicente-Serrano et al. 2010).

Northern Costa Rica forms part of the CADC and is no exception to other drought-affected regions; however, few studies exist to understand the behavior of droughts (Birkel 2006). A major challenge characterizing droughts in the seasonally dry tropics is the 4 to 5 months dry season with virtually no rainfall. The latter dry season is part of the climate variability of the region and has to be clearly differentiated from droughts that mostly manifest as a rainfall deficit over the rainy season (Quesada-Hernández et al. 2019; Romero et al. 2020). Linked to the latter is the challenge that poses the methodology used to determine the beginning and end of drought events (Mishra and Singh 2011). Therefore, many different modeling techniques were used for different purposes, such as regression analysis assuming a linear relationship between predictor and predictand. However, the linearity assumption precludes from adequate long-term forecasting (Avilés et al. 2016).

Time series models such as Autoregressive Integrated Moving Average (ARIMA) (Modarres 2007; Han et al. 2010) and Seasonal Autoregressive Integrated Moving Average (SARIMA) (Fernández et al. 2008) models were proposed for drought forecasting. However, identification, estimation, and diagnostics of the most appropriate time series model depends on the user and the purpose of the model (Mishra and Singh 2011). Neural networks (Mokhtarzad et al. 2017; Khan et al. 2020) are nonlinear models that can characterize complex data patterns at the expense of increased computational burden (Mishra et al. 2011; Avilés et al. 2016).

Probabilistic models can explicitly account for the uncertainty of drought-related variables with Markov chains (MC) being the most commonly used (Paulo and Pereira 2007; Avilés et al. 2016; Estácio et al. 2021). Past studies used MC to forecast short-term rainfall deficits in Paulo et al. (2005) and (Yeh and Hsu 2019). More sophisticated Bayesian networks were not as widely used for drought forecasting (Madadgar and Moradkhani 2013) and therefore need testing in tropical regions (Avilés et al. 2016) and particularly in Central America, where Maldonado et al. (2018) mentions that there is no standardized methodology to produce forecasts, which suggest that some of these forecasts are based on subjective evaluations.

Therefore, we tested and compared two probabilistic models to detect and forecast meteorological drought in the seasonally dry tropics of northern Costa Rica. The first model was based on Markov chains, and the second model used Bayesian networks based on copula functions. These models were set up and run with a continuous and highquality monthly precipitation time series from 1937 to 2020, utilizing a single weather station.

The specific objectives were to
i) test Markov chains of first and second order with a long precipitation time series.
ii) evaluate the performance of Bayesian network models of two- and three-dimensional copulas.
iii) compare these probabilistic models to establish the region's most suitable drought forecast method.

## 2 Study area

The Tempisque catchment (Fig. 1) belongs to the province of Guanacaste and is located in the North Pacific of Costa Rica. According to the National Meteorological Institute (2008), this region is the most water limited in the country. Water scarcity develops due to the low rainfall rates and resultant streamflow during the dry season from December until April. The average annual rainfall in the region is 1700 mm , with mean temperatures of $32^{\circ} \mathrm{C}$ during the day and $22^{\circ} \mathrm{C}$ at night. The rainy season extends from May to November with lower rainfalls around July which is known as Veranillo de San Juan (Ramírez 1983) or canícula (Fig. 1). Mean monthly rainfall from Liberia International Airport weather station over the dry season months is 17 mm with a monthly wet season average of 226 mm . The driest year was 1997 with an annual monthly average precipitation of 57 mm . The wettest year was 1955, with an average of 238 mm . From 1973 to 2003, the mean daily streamflow of the Tempisque River at Guardia gauging station was $24.6 \mathrm{~m}^{3} / \mathrm{s}$ with the lowest flow of $2.6 \mathrm{~m}^{3} / \mathrm{s}$ measured in late April (Birkel et al. 2017). This marked intra-annual seasonality is associated with the

Fig. 1 Overview of the study region (small inlet map), the main Tempisque River, and the weather station location in the main panel (a) showing the mean annual spatial rainfall distribution and (b) the average monthly precipitation (19812020) with the black lines indicating the precipitation range for each month. Data source: Liberia International Airport weather station and CHIRPSv2 (Funk et al. 2014) for the spatial rainfall map
![img-0.jpeg](img-0.jpeg)
seasonal movement of the Intertropical Convergence Zone (ITCZ) and other oceanic-atmospheric regulators such as the El Niño Southern Oscillation (Durán-Quesada et al. 2010).

Despite the marked seasonality and drought proneness of the region, the area used for agriculture increased from $0 \%$ in 1950 to $27.8 \%$ in 2010, changing from a subsistence model to an export-oriented industrial model (Birkel et al. 2017). The region is one of the primary producers of rice and melon and processes more than $50 \%$ of the sugar cane of the country (PIAAG 2019). These activities are carried out intensively and use extracted water from the Tempisque River as the main source to support the irrigation needs.

## 3 Materials and methods

### 3.1 Data sources

For the analysis and modeling of drought, precipitation records from the Liberia International Airport weather station with an 84-year time series (1937-2020) were used (location in Fig. 1). The data were obtained from the National Meteorological Institute with less than 5\% information gaps. Missing data was linearly infilled from a double mass curve using the Climate Hazards Group Infrared Precipitation with Stations (CHIRPSv2) (Funk et al. 2014). The CHIRPS product correlated well $\left(R^{2}>\right.$ 0.8 ) with observed precipitation in the region (Arciniega et al. 2022) and could adequately simulate the duration of
streamflow droughts (Venegas-Cordero et al. 2021) in the Tempisque catchment.

### 3.2 Drought classification

The infilled precipitation series were checked for outliers, and a Mann-Kendall statistical test was performed to verify that the series was stationary. We did not detect non-stationary behavior, and subsequently, no transformation was performed prior to the drought analysis. The R package SPEI (Beguería and Vicente-Serrano 2017) was used for all calculations. The Standardized Precipitation Index (SPI) was selected to characterize drought periods (McKee et al. 1993) and was based on fitting a Gamma statistical distribution to the rainfall empirical distribution. It was calculated on a monthly scale (SPI-1) due to our focus on meteorological drought as the precursor to other drought phenomena and then reclassified into four drought states (Table 1). SPI-1 values greater than -0.99 were considered as "no drought." The "moderate drought" category includes values between -1 and -1.49 , while the "severe drought" category consists

Table 1 Definition of drought states


of -1.5 to -1.99 . SPI-1 values less than -2 are categorized as "extreme drought." The SPI-1 time series was divided into a calibration period (1937-1999), in which the probabilities were calculated, and a validation period (2000-2020), in which the calculated probabilities were tested as an indicator of forecasting performance.

### 3.3 Probabilistic models

### 3.3.1 Markov chains

Probabilistic models based on Markov chains are commonly used for drought prediction (Mishra and Singh 2011; Avilés et al. 2016). According to Avilés (2017), these models are composed of "a set of transition probability matrices that indicate the probabilities of occurrence of the states of a system for a time interval of the future from the information of the current state and/or states of past intervals, depending on the order of the model." These transition probabilities determine the behavior of the Markov chains, and this converts them into conditional probabilities (Wilks 2003).

It is from these transition matrices that the next month's drought category can be predicted based on the current month's observation for first-order Markov chains (MC1). In the case of second-order Markov chains (MC2), it is the same principle, but with the difference that the forecast of the next month is based on the observation of two previous months. Here, we used non-homogeneous Markov chains considering the climatic seasonality of the study area. The latter means that the probabilities are not fixed for any given month, but instead will vary from month to month. The transition probability of a month is determined by the category of the previous month. According to Steinemann (2003), this characteristic is known as the Markov Property, which is expressed as follows:
$p i j=\operatorname{Pr}\{X(t+1)=j \mid X t=i\}$
where pij represents the transition probability in which $\mathrm{X}(\mathrm{t}+1)$ equals the category $j$ given that Xt equals the category $i$. To calculate the transition probability (pij), the relative frequencies, which are the conditional probabilities of the transitions between each category (mij), must be estimated. This can be expressed as
$p i j=m i /\left(\sum j m i j\right) i, j=1$
where the numerator represents the number of transitions of the category $i$ to the category $j$, while the denominator is the sum of the number of transitions of the category $i$ to any other category.

Unlike MC1 models, MC2 models require three subscripts for the estimation of transition probabilities since dependencies of more than two time periods are considered for their calculation (Wilks 2003). The first subscript is the state or category at time $\mathrm{t}-1$, the second is the category at time $t$, and the third is the state at future time $\mathrm{t}+1$. According to Avilés et al. (2015), this is formulated as follows:
phij $=\operatorname{Pr}\{\mathrm{X}(\mathrm{t}+1)=j \mid \mathrm{Xt}=\mathrm{i}, \mathrm{X}(\mathrm{t}-1)=h\}$
In this case, the transition probability phij, in which $\mathrm{X}(\mathrm{t}+1)$ is equal to state $j$, is given by Xt being equal to drought state category $i$, and $\mathrm{X}(\mathrm{t}-1)$ being equal to category $h$. The transition probabilities phij are estimated by
phij $=\mathrm{mhij} /\left(\sum j \mathrm{mhij}\right) h, i, j=1$
The numerator is the number of transitions from categories $h$ and $i$ to category $j$; and the denominator is equal to the sum of the number of transitions from categories $h$ and $i$ to any other category. This model considers values further back in time, so the number of possible transitions increases exponentially, resulting in larger matrices, compared to the MC1 model.

### 3.3.2 Bayesian networks

According to Madadgar and Moradkhani (2013), Bayesian networks describe the conditional dependence of a set of random variables based on direct acyclic graphs (DAG). Following Heckerman (1998), the first step in developing a Bayesian network is to define the variables and states to be modeled, in this case, the drought categories. The second step consists of generating the DAG that encodes the conditional independence assertions, which is called the structure of the Bayesian network:
$\mathrm{P}(\mathrm{xtn} \mid \mathrm{xt} 1, \ldots, \mathrm{x}(\mathrm{tn}-1))=\mathrm{P}(\mathrm{xt} 1, \ldots, \mathrm{xtn}) / \mathrm{P}(\mathrm{xt} 1, \ldots, \mathrm{x}(\mathrm{tn}-1))$
where xtn represents the forecast probabilities, which are calculated from the division of the predictive variables, i.e., the joint distributions associated with the variables. To define these distributions, we used copula functions, which model the joint behavior of the variables (Avilés et al. 2016; Madadgar and Moradkhani 2013). Copulas form multivariate functions by linking uni-variate functions (Shiau 2006), which make it possible to separate the effects of dependence from the effects of marginal distributions. This simplifies the modeling of the dependence of the random variables (Schmidt 2006). These functions were introduced by Sklar (1959), who, in his theorem, describes how copulas interact between multivariate distribution functions and their marginal distribution. The theorem states that a multivariate

distribution $\mathrm{F}(\mathrm{X} 1, \ldots, \mathrm{Xn})$, for all X in the domain F , can be expressed as follows:
$\mathrm{F}(\mathrm{X} 1, \ldots, \mathrm{Xn})=\mathrm{C}\{\mathrm{U} 1(\mathrm{X} 1), \ldots, \mathrm{Un}(\mathrm{Xn})\}$
where the marginal distribution in the interval $(0,1)$ is represented by U1 (X1), while C is the cumulative distribution (CDF) of the copula. Therefore, Eq. (5) can be reformulated as
$\mathrm{P}(\mathrm{xtn} \mid \mathrm{xt} 1, \ldots, \mathrm{x}(\mathrm{tn}-1))=\mathrm{C}(\mathrm{Ut} 1, \ldots, \mathrm{Utn}) / \mathrm{C}(\mathrm{Ut} 1, \ldots, \mathrm{U}(\mathrm{tn}-1))$
Based on Eq. (7), the Bayesian network models can be calculated. For Bayesian networks of first order (BN1), it is necessary that $n=2$; whereas if $n=3$, we have the models of Bayesian networks of second order (BN2), which are expressed as follows:
$\mathrm{P}(\mathrm{Xt} 2 \mid \mathrm{Xt} 1)=\mathrm{C}(\mathrm{Ut} 1, \mathrm{Ut} 2) / \mathrm{Ut} 1$
$\mathrm{P}(\mathrm{Xt} 3 \mid \mathrm{Xt} 1, \mathrm{Xt} 2)=\mathrm{C}(\mathrm{Ut} 1, \mathrm{Ut} 2, \mathrm{Ut} 3) /(\mathrm{C}[\mathrm{Ut} 1, \mathrm{Ut} 2])$
Equations (8) and (9) must be rewritten so that the probabilities of each category do not exceed the CDF thresholds established in Table 1. Considering that xds represents the CDF threshold, the equations are defined as
$\mathrm{P}(\mathrm{Xt} 2 \leq \mathrm{xds} \mid \mathrm{Xt} 1)=(\mathrm{C}[\mathrm{U}(\mathrm{Xt} 1), \mathrm{U}(\mathrm{Xt} 2 \leq \mathrm{xds})]) /(\mathrm{U}[\mathrm{Xt} 1])$
$\mathrm{P}(\mathrm{Xt} 3 \leq \mathrm{xds} \mid \mathrm{Xt} 1, \mathrm{Xt} 2)=(\mathrm{C}[\mathrm{U}(\mathrm{Xt} 1), \mathrm{U}(\mathrm{Xt} 2), \mathrm{U}(\mathrm{Xt} 3 \leq \mathrm{xds})]) /(\mathrm{C}[\mathrm{U}(\mathrm{Xt} 1), \mathrm{U}(\mathrm{Xt} 2)])$
The next step identifies the appropriate dependence structures to form the joint distributions (Avilés et al. 2016). For this, the temporal dependence is modeled by performing a copula fitting according to the marginal distributions. The CDF is used to convert the observations into pseudo-observations with values in the interval $(0,1)$, which are the marginal distribution used in the copula fitting.

A total of four types of copulas are used: two elliptic (Normal and Student) and two Archimedean (Clayton and Frank). The best fit is selected according to two criteria:

- a $p$ value greater than 0.05 and
- the lowest statistical value (S), based on the Cramérvon Mises statistic, which is a measure of the distance between empirical and parametric copulas(Anderson 1962) expressed as
$\mathrm{S}=\int_{a} \Delta \mathrm{C}(\mathrm{u})^{2} \mathrm{dC}(\mathrm{u})$,
$\Delta \mathrm{C}=\sqrt{n}\left(C_{E m p}-C_{0}\right)$
where S is the Cramér-von Mises statistic value; cEmp and C 0 are the empirical and parametric copulas, respectively, both of which fit the $n$-size data. Once the best-fit copulas are selected monthly and applied to Eqs. (10) and (11), they
are used to develop the Bayesian networks of both first and second order.


### 3.4 Model forecast evaluation

From the previous steps, four models are obtained and statistically validated to select the most appropriate for drought forecasting. This validation uses a weighted probability score, known as Ranked Probability Score (RPS), and expressed as
$\mathrm{RPS}=\sum_{\mathrm{m}=1}^{3}(\mathrm{Ym}-\mathrm{Om})^{2}$
This method calculates the forecast errors in terms of the probability attributed to the events. Additionally, it penalizes the forecasts that are further away from the observations (Avilés 2017). The result of Eq. (13) is the difference between the predicted probabilities $(\mathrm{Ym})$ and the observed probabilities $(\mathrm{Om})$. A perfect forecast should have an RPS equal to zero, and the further away from this value, the greater the difference between the predicted and observed probabilities.

## 4 Results

### 4.1 Long-term climatic variability and meteorologic droughts

Data from the airport weather station showed (Fig. 1) a marked difference in the amount of precipitation between the dry and rainy seasons. The dry months from December to April exhibited monthly rainfall averages of less than 25 mm , while in the rainy months from May to November, rainfall exceeded 150 mm per month, except for November. There was a difference of approximately 165 mm between April and May, while from November to December, the change in average rainfall was almost 90 mm . Hence, no transition period between the seasons could be detected, as the increase in rainfall in May is almost immediate, and the decrease in precipitation in November is just as abrupt (Fig. 2); however, an analysis of daily or weekly data may reveal a transition period. The highest monthly rainfall occurs in September and October with an average close to 340 mm . Between July and August, rainfalls are lower compared to May to June and September to October. This period was also called mid-summer drought or "veranillo" (Alfaro 2014). A Mann-Kendall test was performed on the time series which resulted in a $z$-value $=1.134$ and a $p$-value $=$ 0.257 , evidencing the stationarity of the time series.

The monthly Standardized Precipitation Index (SPI-1) was calculated from the precipitation data (Fig. 3) and

![img-1.jpeg](img-1.jpeg)

Fig. 2 Heat map depicting average monthly precipitation (19372020) for the airport weather station. The white shading represents low-to-zero precipitation, while the blue tiles represent higher accumulated precipitation
clearly identified that drought events have occurred historically. In fact, two months of extreme drought were detected in July and August 1939 with SPI-1 $=-3.7$. This condition of an SPI-1 being equal to or less than -3.7 did not occur again in 57 years, until September 1996, with a record low SPI-1 of -4 , and a year later, in September 1997, the absolute minimum SPI-1 of -4.5 was detected. The most extreme drought in recent years occurred in July 2014, with an SPI-1 of -3.4 .

In summary (Table 2), the lowest monthly precipitation of the weather station was 0 mm , which exclusively occurred in dry months, while the maximum monthly precipitation was 818 mm . The monthly average was 137 mm , and the annual average was 1630 mm . The maximum SPI-1 was 3.0, corresponding to June 1979, with an accumulated monthly rainfall of 761 mm compared to a monthly long-term average of 137 mm .

Fig. 3 Monthly standardized precipitation index (SPI-1) for the airport weather station (1937-2020). The letter A indicates the extreme drought of July-August 1939. Letter B marks the extreme droughts of September 1996 and 1997, while letter C highlights the extreme drought of July 2014
![img-2.jpeg](img-2.jpeg)

Table 2 Summary statistics of precipitation time series and derived SPI-1


### 4.2 Categorization of drought states

The SPI-1 values were reclassified according to Table 1, with the aim of identifying the months that presented a drought event, as well as recognizing the severity of the events and the frequency of occurrence.

Table 3 Number of drought events observed per month and classified by drought state


Out of the 1002 months of the time series, 91 were in some category of drought, which represents about $9 \%$ of the data. As shown in Table 3, the moderate drought category occurred most frequently with 45 events, followed by severe drought with 27 observed events, and finally, extreme drought with 18 events. Interestingly, the majority of extreme drought events occurred in July and August, whereas moderate droughts occurred in May and October/ November.

### 4.3 Markov chain drought modeling

Equation (2) was applied to obtain the relative MC1 frequencies of the transitions between months. Twelve transition matrices were obtained which established the transition probabilities for the current month given the previous month. The results for the rainy season are shown in Table 4. We only show the rainy months since the dry season months from December to April are a natural climatic feature of the seasonally dry tropics. Furthermore, the results for the dry season established a $100 \%$ probability of transition to the non-drought category for all dry months. Therefore, the MC1 model calculated - as expected - no drought probability for the dry season.

To interpret Table 4, the probabilities of the occurrence of a specific state for a month need to be compared with the probabilities of the same state of the previous month. For example, if May is in the no drought category, June has an $88 \%$ chance of remaining in that same category; an $8 \%$ chance of moving to state 1 (moderate drought); a $0 \%$ chance of state 2 (severe drought); and there is a $4 \%$ chance of an extreme drought event (state 3). The MC1 model did
not assign transition probabilities from one drought state to another in the month of May. The reason was that historically April has never presented any drought event, as shown in Fig. 4. In contrast, May has presented drought events, which allows calculating the transitions between drought states for the following months. For instance, when May
![img-3.jpeg](img-3.jpeg)

Fig. 4 (a) Cumulative distribution function of the SPI-1 time series for the airport station showing the thresholds for each drought category and (b) the resulting heatmap of historical drought occurrence

Table 4 Rainy season transition probabilities of drought states for the MC1 model


presents a state 3 , June has a $67 \%$ probability of changing to state 0 , and a $33 \%$ probability of changing to state 2 . August, September, and October are the months with the highest probability of transition to state 3 , which, according to MC1, was the most likely trimester of extreme drought occurrence.

Equation (4) was used to calculate the drought state transition frequencies for the second-order Markov chains. These transitions consider the states of two months prior to the month to be forecast. The possible combinations increase from 16 possibilities in model MC1 to 64 in MC2 (Table 5).

The interpretation of Table 5 is similar to that of model MC1, with the difference that model MC2 takes into account two previous states. Thus, when May was in state 3 and April in state 0 , June has a $67 \%$ probability of presenting a no drought event (state 0 ); it also has a $33 \%$ probability of being in state 2 , while it has a $0 \%$ probability for states 1 and 3. Another example is that if September is in state 0 and August is in state 1 , then October has a $60 \%$ probability of no drought. Even if it would have a $40 \%$ probability of being state 1 , no resulting state 2 and 3 droughts are possible.

It is also important to note that with MC1 and MC2, a $50 \%$ probability of two opposite states can occur. This situation occurred in both models in September and October. This means that even considering two previous months, the Markov chain models have the disadvantage of giving the same probability for two opposite states, which represents a problem when deciding whether there will be a drought state.

### 4.4 Bayesian networks applied to analyze meteorological drought

The results from the validation period for the probabilities of the first-order Bayesian network per month in the rainy season are shown in Fig. 5. For all months, the no drought category exhibited the highest probability of occurrence, while the drought states $1-3$ have a much lower probability, each below $20 \%$ since the distributions observed in the calibration period tend to be above the no drought threshold. However, the no drought category showed a decrease in the probability of occurrence after a drought event was observed, together with an increase in the probabilities of occurrence of a drought event. For example, in the month of May, the average probability of the no drought 0 category was $77 \%$, but in 2008, that probability dropped to $65 \%$, and in 2015, the probability was $60 \%$; in those two years, meteorological drought events occurred.

This behavior was also present in other months, most notably in July, where two drought events occurred (2012 and 2014), and the drought probabilities increased to almost $25 \%$, while those of the no drought category dropped to $35 \%$ probability. The only month that does not present this behavior is June due to the weak correlation of
pseudo-observations between May and June (Table 6), generating greater uncertainty in the transition of those months. In general, the best-fit dry season Copula was the symmetric Frank type, while in the rainy season, it was the asymmetric Clayton copula that predominated. The wider range of the Frank dependence parameter seems to better adapt to the dry season characteristics compared to the negative tail dependence of the Clayton copula.

Similar to the first-order model, the second-order Bayesian networks required the copula parameters to be fitted, which results in three-dimensional copulas. Therefore, the selection of copulas for this model included three parameters. The elliptic copulas (normal and T) were the best fit, except for June. This means that when two months are grouped together, the distributions were of an elliptic shape. The difference in the statistical value of the normal and T copulas was very small, considering more than five decimal places. Figure 6 shows the results of the second-order Bayesian network model with the no drought category acquiring the highest probability (average of $84 \%$ probability) for all months. In addition, moderate drought has an average probability of $8 \%$, severe drought of $5 \%$, while extreme drought has an average probability of $3 \%$. With the 2nd-order Bayesian model, the probabilities remained stable throughout the validation period. July was the only exception since the probabilities were more inconsistent during the validation period and due to the heavy tail of the fitted Clayton copula. Therefore, this month showed that the probabilities of drought states increased when a drought event was observed, while the probability of the no drought category decreased with respect to its historical behavior.

### 4.5 RPS evaluation for all drought states

We compared the models using the RPS validation method for all categories, including the no drought category, for the validation period (2000-2020). The RPS values obtained are shown in Table 7 and visualized in Fig. 7.

From December to April, the MC1 resulted in an RPS $=$ 0 , meaning a perfect prediction. However, this is because this model predicts a $100 \%$ probability of no drought in the dry months. The latter is to be expected, as shown in Fig. 4, since the dry season months do not experience meteorological drought. In the case of the Bayesian network models, there is a difference between the forecast and the observed for those same months due to the Bayesian models always assigning probabilities of occurrence to the four drought categories. For the rainy season months, differences between forecasts and observations were observed contrary to the dry season.

In the first two months of the rainy season (May-June), the models showed a similar behavior; however, from July to November, the Bayesian networks outperformed the Markov

Table 5 Rainy season transition probabilities of drought states for the MC2 model


Table 5 (continued)


chain models with RPS statistics closer to zero, more closely representing the observed drought states. The RPS calculated for the validation period and observed droughts from Table 8 and Fig. 8 showed the differences between the modeled forecast and the observed droughts.

The two Markov chain models had similar behavior, except in July, where the first-order model showed a greater difference. In October, forecasts showed a decrease in performance, but an improvement in November. The secondorder Bayesian model showed a similar performance to those of the Markov chains with greater differences in May. The first-order Bayesian networks showed the best performance throughout the rainy season. The best results were obtained for August and November.

## 5 Discussion

### 5.1 Drought characterization in the tropics using SPI

The Standardized Precipitation Index (SPI) was used to characterize drought events monthly from January 1937 to June 2020. At the long-term Airport meteorological station, meteorological drought events have historically occurred between May and November throughout the rainy season. The dry season months are characterized by little or no precipitation, which is a climate feature, meaning that a significant decrease in precipitation in relation to the average rainfall for the dry season months is not possible. This variability in the behavior of meteorological drought can condition the results of the forecasts since the construction of the probabilities depends on the amount of input information given to the models. However, the 84-year precipitation record can be considered sufficiently long including enough information content in the form of climatic variability and drought events that historically occurred.

Large parts of Costa Rica including the Tempisque catchment in the Guanacaste region are characterized by a climate condition known as mid-summer drought (MSD) or "veranillo" in Spanish in July and August, which is characterized by an increase in trade winds and a decrease in precipitation (Ramírez 1983). This period occurs annually; however, its initiation and duration are variable (Amador 2008). Alfaro (2014) found that in the Tempisque basin between the period 1949-2010, the MSD had an average duration of 45 days with an average rainfall of 2.7 mm . Therefore, it is important to take the MSD into consideration for drought forecasting to be able to differentiate between a drought event and the recurrent MSD. The latter distinction could be achieved using the Bayesian networks, especially the first-order Bayesian network model which provides enough flexibility in assigning drought probabilities in the months when drought was observed, as shown in Fig. 5. However, it is important to mention that these probabilities of a drought state did not exceed those of the no drought state.

Another important climate influence on the Costa Rican Pacific is ENSO (El Niño Southern Oscillation) that associates a warming Pacific Ocean with a decrease in precipitation compared to average conditions. However, in the periods 1982-1983 and 1992-1993, when El Niño showed a strong signal (Wolter and Timlin 1998),

Fig. 5 Monthly probabilities of the first-order Bayesian network model for the rainy season of the validation period from 2000 to 2020
![img-4.jpeg](img-4.jpeg)

Table 6 Correlations of the pseudo-observations for each month at the airport weather station


this was not reflected in a state of drought. Between 1982 and 1983, there were only two months of drought, but these were not consecutive and rather with a separation of eight months. Between 1992 and 1993, only May 1992 showed a moderate drought, with an SPI-1 value of -1 and slightly below normal precipitation. However, other
periods classified as strong ENSO, which occurred in the years 1972-1973 and 1997-1998 (Wolter and Timlin 1998), showed drought states in the observed time series. In 1972, there were four consecutive months of drought between July and October; in 1973, there was no drought since El Niño had already weakened by the end

Fig. 6 Monthly probabilities of the second-order Bayesian network model for the rainy season of the validation period from 2000 to 2020
![img-5.jpeg](img-5.jpeg)

Table 7 RPS values for all models and all state categories


Values that meet the best-fit selection criteria for each month, which are the values equal to or closest to zero, are highlighted in bold and underlined
of the previous rainy season. Between 1997 and 1998, a very strong El Niño was recorded in the region, resulting in a 3-month long extreme drought event from August to October 1998, also shown by Muñoz-Jiménez et al. (2018) relating rainfall deficit to ENSO indicators. The
latter authors also identified that strong ENSO events do not always result in a significant rainfall deficit and subsequent drought events in northwestern Costa Rica, mainly due to the complex teleconnection with the nearby Caribbean Sea (Enfield and Alfaro 1999).

Fig. 7 Model validation for all state categories from January to December using the RPS criterion

Table 8 Calculated RPS values for all models and only for drought state categories


Values that meet the best-fit selection criteria for each month, which are the values equal to or closest to zero, are highlighted in bold and underlined

Fig. 8 Model validation for the months presenting a drought category $1-3$ using the RPS criterion (excluding the dry season from December to April)

![img-6.jpeg](img-6.jpeg)

### 5.2 Forecasting capability of the tested probabilistic drought models

The framework of the Markov chain models is both simple and efficient (Sharma and Panu 2012); however, the results of these models showed, in this study, transition combinations between states that have not been observed historically. The latter resulted in the MC1 and MC2 models being unable to calculate probabilities (these cases are represented in Tables 3 and 4 with a dash). However, the fact that some combinations have not been observed does not mean they cannot occur in the future. Similar to Cancelliere et al. (2006), this generates errors in the transition probabilities, which makes these models unsuitable for very complex systems (Fung et al. 2020).

The Markov chains showed reasonable performance in the dry season since they were able to predict the no drought events with perfect RPS values (Table 8). However, this was expected since (Fig. 4) the dry season is a climatic feature of the study region rather than a drought event. Similarly to Liu et al. (2009), Markov chains achieved better performance in the no drought and moderate drought states but presented problems in forecasting events of greater severity. On the other hand, the first-order model (MC1) performed slightly better than the second-order model (MC2), meaning that, although MC2 has more information to base the forecast

upon, this does not necessarily lead to better forecasts (Rahmat et al. 2016).

According to Avilés et al. (2016) and Madadgar and Moradkhani (2013), models based on Bayesian networks (BN) have the potential to better forecast droughts than Markov chain models. The Bayesian networks (BN1, BN2) obtained the lowest RPS scores, in addition to monthly distributions that appropriately reflected observed droughts. Then, the probabilities of no drought decreased, and those of any drought category increased. Thus, as in Ji Yae Shin et al. (2016), Guo et al. (2019), and Raza et al. (2021), BNs generated a solid framework for forecasting drought events in the rainy season of our study region, particularly for the months August and November. The latter because although the likelihood of a non-drought state is higher, the decrease in probability during months when droughts were observed and the slight increase in drought probability suggested that the precipitation data distribution is not normal compared to past years, warranting caution in case this trend continues, as it may obscure the occurrence of a drought state.

Furthermore, the use of time-variable copula functions in BN models was an advantage to better match the observed data distributions despite more complexity. Thus, each month has a specific fit, and even when the same copula type is applied for multiple months, the fitted parameters allow the forecasts to adapt to the climatic condition of each month according to the behavior of the distributions. According to Shiau (2006), copula functions allow to construct a dependence structure between variables. The bestfit Clayton copulas were fitted in June, July, August, and October and obtained the best results in forecasting the observed drought events. This type of copula is characterized by a strong density and concentration of data in the left tail (Mendoza and Galvanovskis 2014), meaning that there is a relationship with negative events or, in this case, drought states. It can, therefore, be expected that drought events in any month increase the probability of a drought in the month to follow.

The BN1 models incorporated 2 months of information and can use the actual SPI data, unlike the MC1 models, which only contemplate the binary information (drought categories) of a single month. This allows the BN1 model to be more dynamic since the information is constantly adapted and updated monthly using parametric copula and marginal distributions. In the case of MC2, it was found that higherorder Markov chains presented problems when sizing and projecting data since the more months accumulated, the fewer transitions are considered. The latter thus generates a poor approximation of the transition probabilities (Lall and Sharma 1996). Even though we tested different types of copulas, non-parametric approaches allow us to avoid a priori assumptions about the choice of a model similar to Sharma and Lall (1999).

One of the limitations of the probabilistic models presented is that they depend on the time series characteristics of historic data and, in our case, on the probabilities calculated based on monthly SPI values. In other words, to forecast the following months' drought category, it is necessary to know the precipitation in advance. Therefore, this class of time series models needs to be coupled to a regional climate model precipitation forecast. Steyn et al. (2016) stated that a double Gaussian function effectively modeled the annual precipitation cycle in Guanacaste, which could be an option to build a model that predicts precipitation and forecasts droughts within a BN. Additionally, the models presented are strictly only valid in the case of stationarity, which might limit their use with strongly non-stationary time series. Here, we could show that since 1937, the precipitation record did not show changing mean nor variance over time, justifying the use and potential of the models applied.

## 6 Conclusions

Historical drought events in Guanacaste, Costa Rica, were analyzed, and probabilistic meteorological drought forecasts were obtained using the 84-year long-term airport weather station records. From the comparison and validation of these models, we conclude that the firstorder Bayesian networks showed the best performance for monthly forecasts with the ability to differentiate between the climatic characteristics of dry and rainy season months. The probability of predicting a drought never reached the level of the non-drought state with Bayesian networks, which also showed greater sensitivity with a slight increase in the probability of drought for some months compared to the other models. The Bayesian network model also automatically adjusted the probabilities during the wet season according to the monthly behavior, even when the no drought category had the highest probability. The latter is a critical advantage since it allows the forecast to be dynamically based on the drought status of increasing or decreasing drought probabilities. Future research will explore the applicability of these models with SPI at different temporal scales to detect and forecast other types of droughts that have a more direct impact on communities, such as hydrological and agricultural droughts. The latter will also enable to increase in the lead time of forecasted drought events.

KG would like to acknowledge a DAAD travel grant to work with AA at the University of Cuenca, Ecuador.

Code availability The model codes can be obtained upon reasonable request to the first author.

Author contribution Conceptualization, all authors; methodology, K.G., A.A., R.A., C.B.; resources and funding, A.N., C.B.; data curation, K.G., C.B.; writing-original draft preparation, K.G., A.N., C.B.; writ-ing-review and editing, all authors.; visualization, K.G. All authors have read and agreed to the published version of the manuscript.

Funding Open Access funding enabled and organized by Projekt DEAL. This research was supported by the DAAD and BMBF-funded "TropiSeca" project and received support by the University of Costa Rica funds to OACG (ED-3199).

Data availability The data can be obtained upon reasonable request to the first author.

## Declarations

Ethics approval Not applicable.
Consent to participate Not applicable.
Consent for publication Not applicable.
Conflict of interest The authors declare no competing interests.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
