BOGNA MRÓWCZYŃSKA, Ph.D. ${ }^{1}$<br>E-mail: bogna.mrowczynska@polsl.pl<br>MARIA CIEŚLA, Ph.D. ${ }^{1}$<br>E-mail: maria.ciesla@polsl.pl<br>ALEKSANDER KRÓL, Ph.D. ${ }^{1}$<br>E-mail: aleksander.krol@polsl.pl<br>ALEKSANDER SŁADKOWSKI, Ph.D. ${ }^{1}$<br>(Corresponding author)<br>E-mail: aleksander.sladkowski@polsl.pl<br>${ }^{1}$ Silesian University of Technology, Faculty of Transport<br>Krasińskiego 8, Katowice, Poland

Traffic Planning<br>Original Scientific Paper<br>Submitted: 5 Aug. 2016<br>Accepted: 7 Apr. 2017

# APPLICATION OF ARTIFICIAL INTELLIGENCE IN PREDICTION OF ROAD FREIGHT TRANSPORTATION 


#### Abstract

Road freight transport often requires the prediction of volume. Such knowledge is necessary to capture trends in the industry and support decision making by large and small trucking companies. The aim of the presented work is to demonstrate that application of some artificial intelligence methods can improve the accuracy of the forecasts. The first method employed was double exponential smoothing. The modification of this method has been proposed. Not only the parameters but also the initial values were set in order to minimize the mean absolute percentage error (MAPE) using the artificial immune system. This change resulted in a marked improvement in the effects of minimization, and suggests that the variability of the initial value of S2 has an impact on this result. Then, the forecasting Bayesian networks method was applied. The Bayesian network approach is able to take into account not only the historical data concerning the volume of freight, but also the data related to the overall state of the national economy. This significantly improves the quality of forecasting. The application of this approach can also help in predicting the trend changes caused by overall state of economy, which is rather impossible when analysing only the historical data.


## KEY WORDS

forecasting methods; freight transport; artificial immune system; clonal selection; Bayesian networks; double exponential smoothing;

## 1. INTRODUCTION

Forecasting the volume of freight has a significant importance for future decisions for the entire economy, as well as its individual participants. The size of transport is dependent on various factors and therefore more accurate forecasts require complex forecasting tools. However, for initial assessment the use of older simple models is sufficient; for example, Holt-Winters double exponential smoothing. They are widely used today in many areas of science, because of ease of
use and low values of forecast errors. However, to this day such methods are still undergoing refinement. In article [1] the authors justify the need for adjustments in the Holt-Winters double exponential smoothing. In article [2] the authors present a selection method of parameters of model exponential smoothing, which are solved by the minimization of the problem. In [3] the authors of the most commonly used techniques for smoothing such as moving average or exponential smoothing. They specially designed weight coefficients which were employed for smoothing the forecast.

Currently, forecasting models are often supported by artificial intelligence methods. In article [4] the authors applied immune algorithm for estimating the optimal coefficients of logarithm support vector regression. In [5] neural networks of the Autoregressive Integrated Moving Average (ARIMA) method was used to reduce the sensitivity to input errors. In [6] the Bayesian network was used to predict the stock price.

The future of road transportation development impacts investment decisions of companies. An interesting approach to the use of forecasting in the supply chain optimization is described in [7]. The article presents the optimization of the supply chain cost by methods of integer programming. Data needed to optimize the production capacity and warehouse inventory is obtained by forecasting using the method of exponential smoothing. A lot can be found in literature on the use of forecasting in the fields of transport. A guidebook [8] has been compiled for those involved in transport planning. It provides a number of forecasting techniques.

In this paper double exponential smoothing method was used to estimate the volume of freight transport. Calculations were made using Holt-Winters double exponential smoothing, but as optimization variables the $\alpha$ and $\beta$ parameters as well as the initial values of $F_{1}$ and $S_{1}$ (Equation 1 and 2) were adopted, and optimization

was made using artificial immune system. Then, the forecasting Bayesian networks method was used.

The main objective of research presented in this paper was to improve the commonly applied methods of prediction by the use of selected artificial intelligence methods. Having in mind the fact that many important business decisions depend on the forecasts, the authors tried to identify limitations in commonly used forecasting methods and to propose possible solutions, which could improve the accuracy of the forecasts. But the practitioners should be aware that mathematical models are only the tool for deci-sion-making support and the final choice depends on their experience and knowledge.

## 2. DATA DESCRIPTION

The article examines cargo transport by type and by destination. The transport by type is divided into the transport for hire or reward and the transport for own purpose. Table 1 presents the values for both types of freight road transport in Poland according to Central Statistical Office, Warsaw 2005 - 2014.

Table 1 - Transportation of cargo in total and divided into transport for hire or reward and into transport on own account (thousand tons)


This is a summary of the most representative data, which is the least susceptible to random fluctuations. From 2005 to 2013 the growth of cargo transport by type was relatively stable. However, transport activities for hire and reward grew at a more robust pace. In 2012 there was a temporary decline in the value of transported cargo for both types. Cargo transport directions can be either domestic or international (Table 2). The national transport is understood as one in which all traffic is carried out using vehicles registered in Poland and roadways running entirely through the Polish territory.

Table 2 - Cargo transportation divided into national and international transport (thousand tons)


## 3. METHODOLOGY

### 3.1 Holt-Winters double exponential smoothing

Looking at the distribution of the various phenomena observed in road transport, due to the lack of seasonal data, the Holt-Winters double exponential smoothing was used. Based on the time series data (Table 1 and Table 2) the forecast was performed for the next two years (2014 -2015). Holt-Winters double exponential smoothing is given by the formulas:

$$
\begin{aligned}
& F_{1}=y_{1} \\
& S_{1}=y_{2} \cdot y_{1} \\
& F_{t-1}=\alpha \cdot y_{t-1}+(1-\alpha) \cdot\left(F_{t-2}+S_{t-2}\right) \\
& S_{t-1}=\beta \cdot\left(F_{t-1} \cdot F_{t-2}\right)+(1-\beta) \cdot S_{t-2}
\end{aligned}
$$

where:
$t$ - index of time series, a collection of observations made at equal intervals; $t \in N$, where $N$ - the set of natural numbers; $t-1$ - previous period to $t$, and $t-2$ previous to $t-1 ; y_{t}$ - the time series data (in Tables 1 and 2, the time index $t=3$ corresponds to the year 2007. Then index $t=t-1$ corresponds to the year 2006 and index $t=t-2$ corresponds to the year 2005); $y_{t}$ - the volume of transport appropriate for a given year); $F_{t-1}$ - smoothed value of the variable forecasted at the time $t-1 ; S_{t-1}-$ smoothed value of growth of the trend at moment $t-1$; $\alpha$ - data smoothing factor, $\alpha \in[0,1] ; \beta$ - trend smoothing factor, $\beta \in[0,1]$.

Forecast for the period $t \leq n$ is determined by the equation:

$$
y_{t}^{*}=F_{t-1}+S_{t-1}
$$

In turn, the forecast for time $t>n$ is determined from the formula:
$y_{t}^{*}=F_{n}+(t-n) \cdot S_{n}$
where:
$y_{t}^{*}$ - forecast of variable $y$ at time $t ; F_{n}$ - the equivalent of the smoothed value obtained with a simple exponential smoothing model for period $n ; S_{n}$ - smoothed value of the growth trend for period $n ; n$ - number of elements of variable time series for forecasted variable.

The initial values of $F_{1}$ and $S_{1}$ are needed to do the double exponential smoothing. A variety of substitutions can be used. Besides the initial values preset in Formulas 1 and 2 the linear function of the trend as $F_{1}$ and the free term of linear trend function as $S_{1}$ can be applied. The parameters $\alpha$ and $\beta$ are determined by the process of optimization (here: using Solver of Excel of MS Office) for which the average square error of expired forecast is minimized.

### 3.2 Double exponential smoothing supported by artificial immune system

There is another modification to the Holt-Winters double exponential smoothing proposed in this article. It involves the treatment of $F_{1}$ and $S_{1}$ as independent variables and their value is determined by optimization, as well as $\alpha$ and $\beta$ variables, where the square error of expired forecasts is minimized. An artificial immune system was used as an optimization tool.

### 3.3 Evaluation of forecast accuracy

The accuracy of forecasts can be assessed by defining errors "ex-post" One such error is MAPE, where MAPE (Mean Absolute Percentage Error) is defined as:
$M A P E=\frac{1}{n} \sum_{i=1}^{n} \frac{\left|y_{t}-y_{t}^{*}\right|}{y_{t}} \cdot 100 \%$
where:
$n$ - number of observations; $y_{t}$ - value of the time series for a moment or period of time $t ; y_{t}^{*}$ - predicted value of $y$ for a moment or a period of time $t$.

Minimization of the error MAPE was the aim of all calculations made in this article using described methods.

The Pearson correlation coefficient was determined to evaluate the values dependence of the data and forecast. The Pearson correlation coefficient is a measure of the linear relationship between two vectors of variables. The correlation coefficient takes values in the range $[-1,1]$. The more absolute value of the correlation coefficient is closer to the value 1 , the higher is the linear relationship between the data, but the interpretation of the force correlation for each of the observed phenomenon may be different. A positive sign of the coefficient indicates positive
correlation. This means that as real data increase so do the predicted values increase.

The Pearson's correlation coefficient evaluates the correlation between $y_{t}$ of the time series and received expired forecasts $y_{t}^{*}$. The results of all calculations have been subjected to this evaluation.

### 3.4 Artificial immune system

Artificial immune system is one of the artificial intelligence methods [9]. It is similar to the natural immune system of the human body. The natural immune system is an important element of integral human defence system. The human body has several mechanisms to protect itself against external attacks of microorganisms. Intact skin protects it physically. Body fluids such as tears and mucus protect it chemically. The immune system begins to operate when the antigens start to penetrate the body.

The body learns to recognize and to neutralize antigens that attack it. The antibodies with a better fit to the shape of the antigen immobilize the invaders. At the beginning of the attack of antigens, the body may not have the appropriate antibodies. The better suited antibodies are cloned and mutated and among them the most effective ones can be found. Then comes the stage of proliferation - the rapid proliferation of antibody-producing matched cells. Those cells are released into the bloodstream, where they fight antigens. The number of antibodies is reduced after the elimination of the antigens. Some antibodies create a memory cell and at the next attack of the same antigens the immune system is able to recognize the threat more quickly. The process of searching for better antibodies is called clonal selection and its numerical model is used in the optimization.

As mentioned above, artificial immune system is the tool, which was used to determine the parameters $\alpha$ and $\beta$ and initial values of $F_{1}$ and $S_{1}$ of the Holt-Winters double exponential smoothing (Formulas 1-4). It was done by optimization.

In the numerical solutions of the proposed case the antibody is the following sequence of numbers:
$\left[\alpha, \beta, F_{1}, S_{1}\right]$
where $\alpha, \beta \in[0,1]$, and $F_{1}, S_{1} \in R$.
The antigen is an unknown optimal solution, which is aimed at by the antibody - the solution of an algorithm of clonal selection. The value of the inverse of the objective function representing the optimization criterion is the measure of affinity. The MAPE error (Equation 7) is accepted as the criterion of optimization in these calculations.

## Numerical algorithm of clonal selection

1) Initialization: draw from the population of antibody and designate the value of affinity functions.

2) Proliferation: the antibodies with the highest affinity functions result in large quantities of clones.
3) Mutation: selected antibodies from cloned ones are subjected to mutations.
4) Suppression: the number of antibodies is reduced to the number of the base population. The diversity of solutions is maintained.

Own implementations of algorithms written in C ++
for all the calculations were used in the article.

### 3.5 Bayesian network use for forecasting

A structure of Bayesian network corresponds to the cause and effect relationship in a given set of random variables. The usefulness of Bayesian networks in practical applications is manifested by the fact that knowledge of any set of observations (states of some variables) allows the calculation of the probability distributions for the remaining unknown variables [10]. Thus having the past values taken by some variables the Bayesian network allows the calculation of the distribution of probabilities of the future states, and finally the expected value, which is the sought forecast [11].

The network's name is derived from Bayes' theorem, which calls for a revision of the existing beliefs about the probability values in the light of new facts. The network activity is based on two fundamental theorems of probability theory: the formula for the complete probability and Bayesian theorem. Both theorems are powerful inference tools in every chain of probabilistic relationship despite their simplicity [12].

Structure of a Bayesian network. Bayesian network is a directed acyclic graph in which the vertices represent random variables, and edges correspond to relations of cause and effect relationship between these variables. Each vertex $X$ is associated with a table of conditional probabilities, which describes the strength of the relationship. This table contains the conditional probabilities $P\left(X \mid P_{1}, P_{2}, \ldots\right)$ of the individual conditions of the random variable $X$ for different conditions adopted by the direct parents of $P_{1}, P_{2}, \ldots$ (Figure 1). For vertices without parents (so-called root causes) conditional probabilities come down to simple probabilities.
![img-0.jpeg](img-0.jpeg)

Figure 1 - Structure of a Bayesian network

Training of a Bayesian network. Bayesian network knowledge is contained in its topology and in the tables of conditional probabilities associated with random variables. The first step is to identify those variables and the second step is to establish the relationships among them. This task is usually performed by an expert, but in the rare cases this can be done automatically on the basis of available data. The values of conditional probabilities can also be set by an expert based on their knowledge and experience, but more often the network is automatically "trained" based on historical data [13]. The data do not have to cover all the conditions of all the variables.

Inference in Bayesian networks. Practical use of Bayesian networks consists of introducing the information which is currently known -the states of some random variables are set, and then probability distributions of other variables are updated. Prediction making assumes that the future unknown condition results from the variable conditions corresponding to the past events, which are known at the time of making the forecast.

One of the simplest Bayesian networks that can be used in forecasting is shown in Figure 2a. The assumption is that the values (conditions of random variables) for the present and past moments $\left(y_{0-1}, y_{0-2}, y_{0-3}\right)$ are known (here four values), a probability distribution is searched for the future moment. There is no relationship between the variables corresponding to the past because they are unnecessary - all of these variables belong to the past, and are now currently known facts. The next structure used in the research involved only three past values, but additionally the information concerning unemployment rate in the present and previous year was taken into account (Figure 2b). This information was introduced in the form of three states: 'decrease', 'increase' and 'no change'.

The selection of the number of states of random variables. An important issue when designing a Bayesian network is an appropriate determination of the number of the states adopted by random variables. The higher the number, the more accurate are the resulting predictions. On the other hand, with limited number of historical data, it is possible that some states will not be assigned to any value during the network learning. This situation affects negatively the network learning process. To avoid this, a rather small number of states was proposed. The tests showed that the optimum number of states is seven. At the same time, to ensure the accuracy of processing, the following procedure was used: instead of keeping the direct assignment between values of historical data and states of random variables, a decomposition process was made. A single historical value was expressed as a linear combination of values corresponding to the states for each of the random variable. In this way, a single series of historical data generated the entire set

![img-1.jpeg](img-1.jpeg)

Figure 2 - The Bayesian networks used for prediction: a) simple, b) with unemployment rate
of learning records containing pure states, whose distribution corresponds to coefficients of decomposition.

## 4. ANALYSIS

Calculations were made with all described methods. In Tables 4-8 the first and the second line show the results for forecasting method using Bayesian network, the third line, the results and adopted parameters for the Holt-Winters double exponential smoothing and the fourth line contains the results and parameters for the double exponential smoothing obtained by optimization using artificial immune system. In all the subsequent tables and figures the following abbreviations are used: Real Data - RD; Bayesian network BN; Bayesian network with Unemployment Rate - BNUER; Holt-Winters double exponential smoothing- HM; Holt-Winters double exponential smoothing supported by Artificial Immune System - HM - AIS.

In the case of BN method and HM-AIS, a dozen calculation runs were carried out and the tables present solutions with the smallest MAPE error. Generally, such an error corresponds to the highest value of the correlation coefficient.

Figures 3-9 show the values of carriages and forecasts made by the used methods. In Tables 4-8 the Pearson correlation coefficients, the value of MAPE errors, and for solutions using HM and HM-AIS the initial
values of $F_{1}$ and $S_{1}$ (Formulas 1 and 2) and parameters $\alpha$ and $\beta$ (Formulas 3 and 4) are summarized.

As mentioned earlier, in the years 2005 to 2013 the growth of goods transportation was rather stable. The upward trend was fairly solid and random fluctuations small. A temporary dip in the transport of goods took place in 2012, but the difference is not significant. Judging by the smoothed charts (Figure 3), the next few years are likely to see a continuous steady growth in value. Table 3 summarizes the MAPE mistakes and correlation coefficients for forecasts from Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3 - Total transport - real values, smoothed and forecast for 2014-2015

Forecasting for hire or reward transport (Figure 4) by all four methods achieved almost identical graphs, which show an increase in volume of cargo transport in

Table 3 - Total transport - evaluation of results


hire or reward transport. HM-AIS and BN-UER strongly smoothed random fluctuations. The other two methods proved to be sensitive to the reduction in freight of volume in 2012.

Table 4 summarizes the MAPE errors and correlation coefficients for forecasts from Figure 4. The initial value $F_{1}$ of the HM-AIS method again took a similar value as the HM calculation method.
![img-3.jpeg](img-3.jpeg)

Figure 4 - Transport for hire or reward - real values, smoothed and forecast for 2014-2015

Figure 5 shows the forecasts for transport on own account. In this case, the BN method proved to be very sensitive to declines in the volume of transport on own account in 2012. BN-UER reacted slightly, and HM was linear, due to the reduction of random fluctuations. Thus, the forecasts point to stable growth and low probability of random fluctuations.
![img-4.jpeg](img-4.jpeg)

Figure 5 - Transport on own account - real values, smoothed and forecast for 2014-2015

As can be seen in Table 5 the BN-UER has the lowest MAPE error and HM-AIS has the highest correlation coefficient, although these values have deteriorated somewhat in relation to previous forecasts. In HM-AIS the optimization parameters $\alpha$ and $\beta$ differ significantly from the corresponding parameters in HM, but the initial values are very similar.

Further forecasts relate to national and international transport, without breakdown by hire or reward transport and transport on own account. National transport represents the vast majority of the whole transport. In 2012 the effect of reducing the amount of transported cargo is shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6 - National transport - real values, smoothed and forecast for 2014-2015

As can be seen from Table 6, MAPE error for the BN-UER method is the lowest. HM-AIS has the highest correlation. The initial value $F_{1}$ of the HM-AIS and HM took almost identical values.

The participation of international transport in the volume of transport of Polish companies is not significant, but just like the national transport- it is constantly growing (Figure 7).
![img-6.jpeg](img-6.jpeg)

Figure 7 - International transport - real values, smoothed and forecast for 2014-2015

Therefore, the forecasts are probably more reliable and the line of prediction runs almost in a straight line in relation to the true values of the previous years. The increase in cargo transportation in these forecasts is quite large. MAPE error (Table 7) for all methods is slightly higher, but the correlation coefficient indicates the high linear relationship with real data and expired forecasts. The initial value $F_{1}$ of the HM-AIS and HM took identical values.

In summary: the best tools turned out to be the BNUER and the HM-AIS methods. MAPE error is minimal for BN-UER method in four cases and for HM-AIS in two cases. The correlation coefficients were close to 1 in almost all cases in BN-UER and HM-AIS methods. It is apparent that the modifications brought positive effects. Moreover, the compatibility of the initial $F_{1}$ obtained by HM and HM-AIS confirms the validity of the use of Formula 1 for determining the initial value of $F_{1}$. While $S_{1}$ obtained by optimizing is significantly different from the value determined by Formula 2. This suggests that $S_{2}$ also should be determined by

Table 4 - Transport for hire or reward - evaluation of results


Table 5 - Transport on own account - results


Table 6 - National transport - results


Table 7 - International transport - results


optimization. It is possible for instance by Solver of Excel, similarly as determined $\alpha$ and $\beta$ in HM.

## 5. CONCLUSION

In this paper the four ways to predict the volume of the freight by the Polish transport companies were considered. The methods that were used are: Holt-Winters double exponential smoothing (HM), the Holt-Winters double exponential smoothing supported by artificial immune system (HM-AIS), in which the authors proposed the designation of initial values $F_{1}$,
$S_{1}$ and parameters $\alpha$ and $\beta$ in the way of optimizing by the use of clonal selection, the Bayesian networks (BN) and proposed by authors the Bayesian networks with Unemployment Rate (BN-UR).

All four methods worked rather well. Worse results of using calculations are due to an insufficient number of data for this method - the learning process requires large sets of data. However, when the input data were extended and involved also the unemployment rate (which corresponded to overall state of economy) the forecasts obtained by the BN-UR appeared to be the most accurate. The additional advantage of it is that

the result is not only a single number, but a whole probability distribution which can be a valuable hint when making a decision.

The comparison of results of method HM and HMAIS gave interesting observations. In all cases better results were obtained by HM-AIS. The relations among the designated parameters were also very interesting. $F_{1}$ obtained from optimization always accepted a very similar value to the one taken as an initial in the HM method. This confirms the validity of substitution of $y_{1}$ values for $F_{1}$ and suggests the use of optimization to determine $S_{2}$. It is possible for instance by Solver of Excel of MS Office.

The accuracy of all known methods of prediction suffers when the real trend rapidly changes, so practitioners should be aware of this disadvantage and take into account other available evidences when making decisions. A decision maker is responsible for their choice; no mathematical model can provide a final verdict.

A decision maker should be aware that the accuracy of the forecast strongly depends on the relevancy of the model and the input data. If a decision maker faces the problem of rapid discontinuity in available historical data, they will have to take into account as much other knowledge concerning the problem as possible.

BOGNA MRÓWCZYŃSKA, dr inż. ${ }^{1}$
E-mail: bogna.mrowczynska@polsl.pl
MARIA CIEŚLA, dr inż. ${ }^{1}$
E-mail: maria.ciesla@polsl.pl
ALEKSANDER KRÓL, dr inż. ${ }^{1}$
E-mail: aleksander.krol@polsl.pl
ALEKSANDER SŁADKOWSKI, prof. dr hab. ${ }^{1}$
E-mail: aleksander.sladkowski@polsl.pl
${ }^{1}$ Politechnika Śląska, Wydział Transportu
ul. Krasińskiego 8, Katowice, Polska

## ZASTOSOWANIE SZTUCZNEJ INTELIGENCJI W PROGNOZOWANIU PRZEWOZÓW TRANSPORTEM DROGOWYM

## STRESZCZENIE

Planowanie transportu wymaga dosyć często przewidywania wielkości przewozów. Taka wiedza jest konieczna do oceny trendów w gospodarce i wspomagania podejmowania decyzji przez duże i małe przedsiębiorstwa transportowe. Celem prezentowanej pracy jest przedstawienie zastosowań wybranych metod sztucznej inteligencji, które mogą poprawić dokładność prognozy. Pierwszą z zastosowanych metod jest metoda Holta, jedna z metod wygładzania wykładniczego. Zaproponowano pewną jej modyfikację. Na drodze minimalizacji błędu MAPE przy pomocy sztucznego systemu immunologicznego wyznaczane są nie tylko parametry metody, ale i jej wartości początkowe. Ta zmiana spowodowała znaczną poprawę wyników minimalizacji i potwierdziła, że
uzmiennienie wartości poczatkowej S2 ma wpływ na wyniki. Następnie zastosowano metodę prognozowania za pomocą sieci Bayesa. Zastosowanie sieci Bayesa bierze pod uwagę nie tylko historyczne dane dotyczące wielkości przewozów, ale także dane dotyczące ogólnego stanu gospodarki narodowej. To znacznie poprawia jakość prognozy. Zastosowanie tej metody może pomóc w przewidywaniu zmian tendencji spowodowanych przez ogólny stan gospodarki, co jest raczej niemożliwe przy analizowaniu tylko danych historycznych.

## SŁOWA KLUCZOWE

metody prognozowania; wielkość przewozów; sztuczny system immunologiczny; selekcja klonalna; sieci Bayesa; wygładzanie wykładnicze; metoda Holta;
