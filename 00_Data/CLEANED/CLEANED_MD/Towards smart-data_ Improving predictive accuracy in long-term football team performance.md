# Towards Smart-Data: Improving predictive accuracy in long-term football team performance 

Anthony Constantinou ${ }^{\mathrm{a}, \mathrm{b}}$ and Norman Fenton ${ }^{\mathrm{b}}$<br>a. Corresponding author. E-mail address: anthony@constantinou.info<br>b. Risk and Information Management (RIM) Research Group, School of Electronic Engineering and Computer Science, Queen Mary University of London, London, UK, E1 4NS.

## THIS IS A DRAFT OF THE ACCEPTED VERSION OF THE FOLLOWING CITATION:

Constantinou, A. C. and Fenton, N. (2017). Towards Smart-Data: Improving predictive accuracy in long-term football team performance. Knowledge-Based Systems, In Press, 2017.

DOI: http://dx.doi.org/10.1016/j.knosys.2017.03.005
Corresponding author: Dr. Anthony Constantinou, E-mail: anthony@constantinou.info
(C) 2017. This manuscript version is made available under the CC-BY-NC-ND 4.0 license: http://creativecommons.org/licenses/by-nc-nd/4.0/

## (c) BY-NC-ND

ABSTRACT: Despite recent promising developments with large datasets and machine learning, the idea that automation alone can discover all key relationships between factors of interest remains a challenging task. Indeed, in many real-world domains, experts can often understand and identify key relationships that data alone may fail to discover, no matter how large the dataset. Hence, while pure machine learning provides obvious benefits, these benefits may come at a cost of accuracy. Here we focus on what we call smart-data; a method which supports data engineering and knowledge engineering approaches that put greater emphasis on applying causal knowledge and real-world 'facts' to the process of model development, driven by what data are really required for prediction, rather than by what data are available. We demonstrate how we exploited knowledge to develop a model that generates accurate predictions of the evolving performance of football teams based on limited data. The model enables us to predict, before a season starts, the total league points a team is expected to accumulate throughout the season. The results compare favourably against a number of other relevant and different types of models, and are on par with some other models which use far more data. The model results also provide a novel and comprehensive attribution study of the factors most influencing change in team performance, and partly address the cause of the widely accepted favourite-longshot bias observed in bookies odds.

Keywords: data engineering; dynamic Bayesian networks; expert systems; favourite-longshot bias; football predictions; knowledge engineering; smart data; soccer predictions.

# 1. INTRODUCTION 

In many application domains, such as consumer shopping behaviour, applying state-of-the-art machine learning methods to very large datasets (often referred to as 'big data') can reveal new insights that would otherwise remain unknown. However, relying purely on large datasets for automated knowledge discovery and prediction can be inappropriate in many real-world domains. For example, the 2007-09 financial crisis revealed that big-data models used by investment banks and rating agencies failed to predict real-world financial risk. Wieland and Wolters (2012) demonstrate how each of the 50+ professional economic models failed to foresee the downturn. This is because such big-data models do not incorporate new and, hence, previously unseen factors - in this case the sudden burst of the USA housing 'bubble' due to high default rates in the subprime mortgage sector after many high risk loans were sold on as low risk securities (IMF, 2009). Similarly, it would be doubtful whether such models could accurately predict the economic consequences of a country leaving the EU.
This paper focuses on a prediction problem that has similarities to financial risk, namely predicting evolving football team performance. In both domains future performance can be suddenly and dramatically affected by rarely seen events and so both require smarter ways to perform data engineering and modelling, rather than rely on ever larger amounts of data.

Football is the world's most popular sport and constitutes an important share of the gambling market. This has motivated numerous researchers to use football events as a real-world application domain to assess various statistical, probabilistic and machine learning techniques. The most common problem addressed is that of predicting the outcome of specific football matches. This started with the popular work of Maher (1982) on a bivariate Poisson model to predict match results based on the attack and defence capabilities from goals scored and conceded, and which was later adopted by Dixon and Coles (1997) for the purpose of generating profit against published market odds. Since then, numerous Poisson-based models have been published. Rue and Salvesen (2000) proposed a time-series Poisson distribution model and demonstrated profitability against Intertops odds; this model was later revised by Cowder et al. (2002) to a computationally less demanding model. Karlis and Ntzoufras (2003) also assessed double Poisson and bivariate Poisson models and concluded that the bivariate Poisson model correlates well between scores of competing teams.

Football predictions also became popular with computer scientists, primarily for the purpose of testing machine learning techniques. These include: Tsakonas et al. (2002) who found genetic programming to be superior to fuzzy models and neural networks in predicting football; Rotshtein et al. (2005) who concluded that the combination of genetic and neural optimisation techniques can lead to 'acceptable' football match predictions; Joseph et al. (2006) who showed that incorporating expert judgments with data into a Bayesian network (BN) model led to more accurate predictions compared to a number of other data-driven machine learning techniques; Min et al. (2008) who combined BNs with rule-based reasoners to predict World Cup matches; Baio \& Blangiardo (2010) who tested a Bayesian hierarchical model and found it to be on par with the Karlis and Ntzoufras (2003) Poisson-based model; and Constantinou et al. (2012; 2013a) who developed a BN model, based on both data and knowledge, to predict English Premier League (EPL) matches before they start (predictions were published online at www.pi-football.com), and demonstrated profitability against all of the available market odds. Such BN models now also extend to assessing referee bias in football (Constantinou et al., 2014).

Rating systems are also popular within the football predictions literature. For example, Knor-Held (2000) proposed a rating system for football teams based on the cumulative link model

for ordered responses, where latent parameters represent the strength of each team. The ELO rating system, which was initially developed to assess the strength of chess players (Elo, 1978), was assessed by Hvattum and Arntzen (2010) and showed that even though the ratings appeared to be useful in encoding the information of past results for measuring the strength of a team, the predictions were still considerably less accurate compared to market odds. The ELO rating and the ELO-based FIFA/Coca-Cola World Ranking (FIFA, 2016) were also assessed by Leitner et al. (2010) who used them to predict tournament winners, and concluded that the accuracy of both ratings was inferior to bookmakers' odds. Constantinou and Fenton (2013b) proposed the pi-rating system, which determines the level of ability of football teams based on the relative discrepancies in scores between adversaries, and showed that it outperformed ELO-based rating systems and was also able to generate some profit against published market odds over a series of five EPL seasons. Such rating systems are now also extended to determining player skill (McHale et al., 2012).

The popularity of football models is in many cases driven by the prospect of identifying market inefficiencies in terms of the published odds available for betting. Sauer (1998) suggested that a betting market can be considered efficient only if profitable opportunities cannot be exploited. While some studies suggest that the football market may be efficient, due to either not discovering profitable betting strategies or due to market odds outperforming the predictions generated by various proposed statistical models (Peel \& Thomas, 1988; 1992; 1997; Pope \& Peel, 1989; Forrest et al., 2005; Graham \& Stott, 2008; Vecer et al., 2009), numerous other authors have concluded that the market is inefficient. For example, many of the Poisson-based studies have claimed market inefficiency due to generating positive returns against published odds under specific conditions (Dixon and Coles, 1997; Rue and Salvesen, 2000; Kuypers, 2000; Dixon \& Pope, 2004). Other studies have reported inefficiencies at the start and at the end of a football season (Goddard \& Asimakopoulos, 2004), and that the odds offered on popular teams are inefficient due to being offered more favourable terms on their wagers (Forrest \& Simmons, 2008). Studies which demonstrate consistent profitability throughout a football season also question the efficiency of the market (Constantinou et al., 2012; 2013a). However, the strongest evidence of inefficiency probably comes from studies that do not employ predictive models, but rather assess bookmaking odds for biases, and claim inefficiency in the presence of the favouritelongshot bias (Cain et al., 2000, Forrest \& Simmons, 2001; 2002); this is where bets on favourites tend to have higher expected returns than bets on longshots. This type of bias seems to extend to home-team bias and most-likely outcome bias (Constantinou \& Fenton, 2013c).

Most of the previous extensive work on results predictions has primarily used historical data of relevant match results. In this paper we do not consider individual match results, but rather exploit external factors which may influence the strength of a team and resulting performance. We are interested in predicting a football team's performance for a whole season (measured by total number of points won) before the season starts. This is an important and enormous gambling market in itself - bettors start placing bets such as which team will win the title, finish in the top four, or be relegated, as soon as the previous season ends. The need for greater accuracy in such predictions has become the subject of international interest following the 2015-16 EPL season when Leicester City finished top of the league, having been priced at 5,000 to 1 by many bookmakers before the start of the season.

While a team's most recent previous seasons' performances are clearly important, changes may occur over the summer break (such as the purchase of new players or other staff) that may have a major influence on the team's future performance. Since no competitive matches occur over the summer break, it is impossible to judge changes in team strength until the new season begins and match results are observed. Moreover, a team's most recent season performance may

not accurately reflect their true strength if, for example, the team had been adversely affected by major injuries from which players have now recovered.

While the model presented in this paper is important in terms of the application domain for the reasons highlighted above, the process by which the data are engineered and the model is developed is equally important in highlighting the benefits of a smart-data approach. The paper is organized as follows: Section 2 discusses the problem associated with data availability, Sections 3 and 4 cover the data engineering and model development processes respectively, Section 5 covers model validation, Section 6 discusses and presents further results of interest, and Section 7 provides our conclusions.

# 2. THE PROBLEM 

It is a common practice to generate models based on what data are available. For the problem of predicting football team performance as measured by league points accumulated from season to season, there are a multitude of potential available data. However, with the exception of previous seasons' league points, there is little obviously relevant data that are readily available. The temptation in such circumstances is to find any 'easily available' data and throw regression or machine learning methods at it. Such data might include things like: average home attendances, financial turnover, number of international players, size of squad etc. In contrast, our starting point was to use knowledge to identify what data are really required to assess the evolution of team strength between seasons. Focusing on the EPL, we have identified the following factors, with the stated assumptions:

1. League points ( $\boldsymbol{L P}$ ): as discussed above.
2. Transfer spending (T): Player transfers (in and out) can influence team strength.
3. Injuries (I): Excessive injuries to key players leads to degraded team performance while fewer than expected injuries leads to improved performance.
4. Managerial changes (M): Different managers may employ different tactics, and may also influence team spirit and morale, amongst others.
5. European (EU) competition involvement: Those few teams involved in the additional European competitions (Champions League and Europa League) face greater demands than those that are not. Their performance in the league may be degraded because of shift in focus away from the league and increased player fatigue due to both the higher number of matches required to be played and the extensive travelling requirement to other countries.
6. Promoted team (P): If a team is new to the EPL due to promotion from the (lower) Championship division, the normal 'benchmark' performance is that of the team they replace. However, promoted teams often have special circumstances that make their performance relative to the team they replace very different.

In what follows we explain why a typical pure data-driven model (e.g. regression) which attempts to predict next season's league points as a function $f(L P, T, I, M, E U, P)$, of the above specified

factors is inappropriate for time-series inference in football. However, first we have to examine whether the dataset is structured correctly, in terms of adhering to this type of time-series influential modelling, otherwise it would be impossible to build an appropriate model.

# 2.1 IDENTIFYING MODEL REQUIREMENTS 

To justify the restructuring of the data, we require a good understanding in terms of how the model is expected to simulate the real-world behaviour of the problem specified. We employ a Bayesian Network (BN) model for this purpose. Figure 1 illustrates the simplified topology of the overall BN model.
![img-0.jpeg](img-0.jpeg)

Figure 1: Simplified model topology of the BN model.

Time-series analysis requires that we take into consideration the following three time steps:
Time step $\boldsymbol{t}_{\mathbf{1}}$ : This first time step represents the previous season. The relevant factors are:

1. Observed factors that have influenced team performance: This node represents a BN component consisting of relevant variables such as player injuries and involvement in European competitions;
2. Observed performance: This node represents a single variable which takes as input the total league points accumulated over the previous season;
3. True team strength: This node represents the latent variable that we are interested in inferring at $t_{1}$, based on the observations provided for nodes which exist in 1 and 2 above. In brief, the true strength of a team represents team performance independent of component (1) factors, such as injuries. If we observe performance $X$ points, in conjunction with factors that are expected to have resulted in changing team performance by $Y$ points ( $Y$ may be positive or negative), then the true strength of that team is $X-Y$

points. This is achieved by setting the Conditional Probability Table (CPT) of node $X$ to $\{Y+$ true strength $\}$.

Time step $\boldsymbol{t}_{2}$ : This second time step represents events of team changes occurring over the summer break. The model assumes that summer breaks occur at the end of the previous season (i.e., $t_{1}$ ) and prior to the start of the next season (i.e., $t_{3}$ ). At $t_{2}$, the node Observed factors that have influenced team strength is another BN component which consists of relevant variables that represent events which may occur over the summer break, such as player transfers.
Time step $\boldsymbol{t}_{3}$ : The third and final time step, $t_{3}$, represents the subsequent season which commences following the summer break. The topology of this time step consists of:

1. Unobserved factors which may influence team performance: This is a BN component identical to that of time step $t_{1}$, with the only difference being that the factors which may influence team performance are unobserved (since this component represents the subsequent season under assessment);
2. True team strength: As in $t_{1}$, this node represents a latent variable that we would like to infer. However, factors that influence team performance are unobserved at $t_{3}$ and hence, the true strength of the team is revised from $t_{1}$ to $t_{3}$ based on observations provided at $t_{2}$.
3. Expected performance: This node represents the ultimate latent variable we would like to assess. This variable is identical to that of time step $t_{1}$ (i.e., Observed performance). At $t_{3}$, however, team performance is unknown (hence Expected performance) and is inferred by conditioning on the revised true team strength in conjunction with the uncertainties that arise as a result of the unobserved factors which may influence team performance.

# 3. DATA ENGINEERING 

Figure 2 illustrates how the relevant data observations (left), collected over seasons 2000/01 to 2014/15, are reconstructed (right) such that they adhere to the modelling concept of Figure 1. The subsections that follow cover the process of data engineering with respect to each of the factors identified in Section 2.

![img-1.jpeg](img-1.jpeg)

Figure 2: Restructuring the data collected (left) to that required by the model (right), where $P S$ (i.e. previous season) is a variable that has already been observed during the previous season, and $N S$ (i.e. next season) is a variable being assessed for the next season.

# 3.1 LEAGUE POINTS 

Data were collected from XScores ${ }^{1}$ (2016) and represent the total league points accumulated by each team per season. As illustrated in Figure 2, the data were split into three variables. Specifically, in terms of training the model for seasons $s$ and $s+1$, the three data variables would be as follows:

1. Points accumulated over season $s\left(t_{1}\right)$;
2. Points accumulated over season $s+1\left(t_{3}\right)$;
3. Discrepancy between observations (1) and (2).

### 3.2 INJURIES

Data were collected from PhysioRoom (2016), and represent the total number of days with injury over all players for each team per season. While this variable is duplicated into the BN (one for previous and another for next season), it was sufficient to retain one instance of this variable in the dataset based on the assumption that injuries are random.

However, it is accepted from knowledge that some teams can deal with injuries better than other teams. In implementing this belief, we found the Man-of-the-Match (MotM) data ${ }^{2}$ provided by WhoScored (2016) to be a good indicator under the assumption that a team's ability to deal with injuries depends on the number of players who can 'make the difference' in a match. Figure 2 shows that the MotM variable is duplicated into the dataset. This is because we assume that the number of MotM players is influenced by player transfers which occur over the summer break; hence we require MotM observations for both $s$ and $s+1$, with observations at $s+1$ conditioning on player transfers that occurred at $t_{2}$.

### 3.3 EUROPEAN COMPETITIONS

Data with respect to the number of European competition matches, as well as the type of competition, have been recorded manually from Wikipedia. A distinct Wikipedia page exists for each team per season. For example, in the case of Arsenal during season 2014/15, the data can be found at (Wikipedia, 2016b). Both variables are duplicated in the dataset in the same way MotM is, since EU qualification at $s+1$ becomes known at the end of $s$ and hence, influences the number of EU matches expected to be played at $s+1$.

### 3.4 MANAGERIAL CHANGES

Relevant data was manually recorded from MyFootballFacts (2016). This involves data relating to changes in management which occurred both during ${ }^{3}$ a football season as well as over the summer break period. The data also capture the number of seasons the previous manager had spent at the club prior to being replaced. We did not duplicate this variable within the dataset under the

[^0]
[^0]:    1 We discovered that data provided by XScores (2016) had errors with respect to the EPL season 2000/01. We have cross validated the data with other sources and confirmed that the data provided by Wikipedia (2016a) were the correct data.
    2 Only players with total appearances greater than the average number of appearances in the EPL are considered.
    3 If a team starts the season without a managerial change but experiences managerial changes some time later within the same season, we assume that such a team experienced a managerial change for the given season only if the new manager took over for at least half of the season.

assumption that most important managerial changes take effect at the end of a football season and hence we considered the variable to be a $t_{2}$ (i.e., summer break) factor.

# 3.5 PROMOTED TEAMS 

Data were also collected from XScores (2016). This is another $t_{2}$ factor since relegations and promotions of teams between leagues occur at the end of each season. As a result, there was no need to duplicate this variable within the dataset, and no further reconstruction was deemed necessary. As a prior belief, we assume that the strength of the three teams promoted to the EPL is equivalent to the team strength of the three respective teams relegated to the Championship (i.e., the $2^{\text {nd }}$ football division in England).

### 3.6 TRANSFERS

We have made use of relevant financial data, namely Net transfer spending and Total team wages, as provided by Telegraph (2016) for seasons 2000/01 to 2010/11, by TSM Plug (2016) for seasons 2011/12 to 2013/14, and by Total Sportek (2016) for season 2014/15. However, in their current structure, these data provide very limited information. This is because the current data structure fails to take into consideration the following two important factors:

1. Relative additional spend: If a team has a positive net investment of X million British pounds (GBPs) on player transfer spend for the upcoming season, then such a team's performance is expected to improve over the next season. If, however, every other team also has a similar positive net investment on new players, then any positive effect is diminished or cancelled.
2. Inflation of salaries and player values. Investing $£ 100 \mathrm{~m}$ to buy players during season 2014/15 is not equivalent to investing $£ 100 \mathrm{~m}$ to buy players during season 2000/01. The same applies to the wage increase of players over the years due to inflation.

As a result, we had to ensure that the model takes into consideration financial data in relative, rather than absolute, monetary terms. In the case of net transfer spending, we addressed this problem by simply considering the relative percentage difference in spending between teams. In the case of team wages, however, there is an extra layer of complexity. Consider team $A$ with previous season's team wages at $£ 100 \mathrm{~m}$, increasing to $£ 120 \mathrm{~m}$ for the subsequent season. To determine the effect of $A$ 's wage increase of $20 \%$ we need to perform comparisons against the average adversary. Suppose the wage bill of the average adversary was $£ 50 \mathrm{~m}$ during the previous season, and increased to $£ 70 \mathrm{~m}$ for the subsequent season. While the average adversary will also be spending $£ 20 \mathrm{~m}$ more on team wages, just like team $A$, this increase constitutes $40 \%$ relative to the previous season for the average adversary, and $20 \%$ for team $A$. Team $A$ was spending $100 \%$ more on team wages relative to the average adversary over the previous season (i.e., $£ 100 \mathrm{~m}$ against $£ 50 \mathrm{~m}$ ), whereas for the subsequent season the relative difference drops down to $71.43 \%$ (i.e., $£ 120 \mathrm{~m}$ against $£ 70 \mathrm{~m}$ ). Under such a scenario, the model will consider that team $A$ will experience a loss in terms of strength over the subsequent season, relative to the average adversary.

# 4. THE TIME-SERIES MODEL 

In this section we demonstrate each of the BN model fragments corresponding to each of the time steps of Figure 1, as well as the process by which the BN model is used as a Dynamic BN (DBN) to assess the evolution of team strength over multiple seasons. Dynamic BNs are BNs which relate variables to each other over time steps, where both the parameters and the structure are fixed. A more general approach where you have BNs with time-indexed random variables is called Temporal BNs. We make use of this approach to model the time steps $t 1, t 2$ and $t 3$, and to revise them between seasons as follows (refer to Figure 1):

1. The unobserved factors at time $t_{3}$ of BN instance $n$ become observed at time $t_{1}$ for BN instance $n+1$;
2. The inferred distribution Expected performance at time step $t_{3}$ of BN instance $n$ becomes observed at time step $t_{1}$ of BN instance $n+1$.

The BN variables consist of both discrete and continuous Gaussian distributions. Team strength and resulting team performance are both measured by the total league points accumulated. All of the data factors that influence performance, such as level of injuries and changes in the quality of players, are represented by discrete variables, whereas all of the variables that measure performance or impact/change in team strength are Gaussian. We have made use of the AgenaRisk toolset (Agena, 2016) to build the model. AgenaRisk makes use of the dynamic discretization algorithm (Neil et al., 2007) to simulate continuous distributions without any restrictions on the type of descendant and ancestor nodes. The CPTs of the data variables are directly learned from data with no missing values. The latent variables (e.g., true team strength, expected performance) are composite variables as defined in Section 2.1.

### 4.1 EXPERT KNOWLEDGE

A limited number of expert variables are introduced into the model. These variables are:

1. Team stress and fatigue: allows the expert to specify the degree of fatigue and/or stress caused to a team as a result of participating in additional competitions in Europe, as shown in Figure 4 of Section 4.2;
2. Squad instability: allows the expert to specify the degree of instability caused to a team as a result of having too many player changes in the first-team squad due to transfers, as shown in Figure 6 of Section 4.3;
3. Managerial ability: allows the expert to specify whether a team's managerial ability has increased, decreased, or remained stable, following the arrival of a new manager, as also shown in Figure 6 of Section 4.3.

The expert variables are incorporated into the model in such a way that they do not influence the data-driven expectations, as long as they remain unobserved. As an example, Figure 3 presents the part of the BN model where the expert node Squad instability is incorporated, and shows how the data-driven prior of the ancestor node Impact of changes in players is preserved ${ }^{4}$, as long as the expert node remains unobserved. This outcome is achieved using the technique described in (Constantinou et al., 2016), which is based on the notion that the statistical outcomes (e.g. Impact [on team strength] of changes in players) are already influenced by the causes an expert might identify as variables missing from the dataset (e.g. Squad instability); hence, the prior expectation of a data-driven node is not amended when incorporating an expert-driven node, as long as the expert variable remains unobserved within the model.
![img-2.jpeg](img-2.jpeg)

Figure 3. Extending the data-driven model (left) by incorporating the expert-driven node Squad instability, with the aim of preserving the data-driven prior of the ancestor node Impact of changes in players (right model) using the technique described in (Constantinou et al., 2016).

# 4.2 TIME STEPS $\boldsymbol{t}_{1}$ AND $\boldsymbol{t}_{3}$ 

Time steps $t_{1}$ and $t_{3}$ are covered jointly in this subsection since they are almost identical in terms of structure and variables considered. Figure 4 presents the BN model fragment which simulates the events at $t_{1}$. As discussed in Section 2.1, the observed team performance, in conjunction with factors that may have influenced team performance, are taken into consideration for inference of the true team strength. Since the observed performance is simply the total number of points accumulated, an integer input is provided as observation for Observed performance. The observed factors that may have influenced team strength are assessed as follows:

1. Impact of European (EU) competition involvement on team performance: This is a mixture of Gaussian distributions conditioned on the type of EU competition (Champions League or Europa League), the level of readiness for EU involvement (e.g. how familiar the team is in terms of participating in EU competitions), and the expert variable Team stress and fatigue (as discussed in Section 4.1).
[^0]
[^0]:    ${ }^{4}$ Note that the technique preserves the expected value of the distribution. The shape and/or the variance of the distribution are subject to amendments (Constantinou et al., 2016).

2. Impact of injuries on team performance: This is a mixture of Gaussian distributions conditioned on the level of injuries in conjunction with the team's ability to deal with injuries (as discussed in Section 3.2).

Figure 5 presents the part of the BN model fragment that simulates the events at $t_{3}$. The difference between components $t_{1}$ and $t_{3}$ (i.e., Figure 4 and 5) is that the factors at $t_{3}$ remain unobserved, and the prior probabilities of the variables $E U$ involvement readiness, $E U$ competition, and Team ability to deal with injuries are conditioned on observations provided to relevant factors at $t_{1}$ and $t_{2}$ as shown in Figure 5.
![img-3.jpeg](img-3.jpeg)

Figure 4: BN fragment $t_{1}$, where $P S$ is previous season.

![img-4.jpeg](img-4.jpeg)

Figure 5: BN fragment $t_{3}$, where $N S$ is next season (and, at that time step, unobserved).

# 4.3 TIME STEP $\boldsymbol{t}_{2}$ 

Figure 6 presents the BN model fragment that simulates the events at $t_{2}$. The factors considered at this time step are as follows:

1. Impact of changes in players: Relative changes in team wages and net transfer spending are taken into consideration to formulate the composite variable Changes in the quality of players (relative to adversaries) which, in conjunction with the expert variable Squad instability, is taken into consideration in revising team strength.
2. Impact of changes in management: Similarly, any arrival of a new manager, in conjunction with the longevity of the departing manager, is taken into consideration to formulate the composite variable Managerial instability. The model assumes that the

managerial instability is conditioned on the longevity of the departing manager. For example, Sir Alex Ferguson spent 26 years as a manager for Manchester United. The replacement of such a manager affects instability in a different way when compared to the replacement of a manager who had only spent a single season at a club. Whether the new manager is believed to be superior to the departing manager can be judged expertly through the expert variable Managerial ability.
3. Impact of promoted teams: Lastly, the impact of promoted teams is solely measured based on the variable Newly promoted. This variable classifies the teams between promoted and non-promoted. Non-promoted teams are further classified into levels of team strength, under the assumption that the arrival of newly promoted teams may influence the performance of existing EPL teams in different ways, based on their strength.
![img-5.jpeg](img-5.jpeg)

Figure 6: BN fragment $t_{2}$, where $P S$ is previous season and $N S$ is next season.

# 5. MODEL VALIDATION 

The validation is divided into two categories:

1. In Section 5.1 the model is validated in terms of how accurately it can predict team performance for each subsequent season, i.e., by assessing the predicted performance at time step $t_{3}$ for each BN instance $n$ against the observed performance at time step $t_{1}$ for each subsequent BN instance $n+1$.

2. In Section 5.2 the model is validated in terms of how accurately it can predict the performance of specific teams which demonstrate the highest volatility in team performance, over a series of seasons.

No similar model exists in the literature to serve as a 'true' comparison for model validation purposes. To assess the performance of the BN we consider three types of models or predictors. First, we consider a naïve method that serves as a lower benchmark predictor as follows:

1. NM (Basic method): simply predicts the league points a team will accumulate at season $s+1$ as the number of league points the team accumulated at season $s$.
Second, we have formulated two regression based models that use the dataset we collated for this study. These are:
2. R1: a standard non-linear regression model that considers the factors presented on the left of Figure 2 (i.e., prior to data engineering), in addition to the league points accumulated at season $s-1$, as predictors for league points accumulated at season $s$. Hence, this is a regression-based predictor before any data engineering practises are performed.
3. R2: a second standard non-linear regression model that considers the same factors as those considered by $R 1$, but in relative terms just like in the BN (e.g., refer to Section 3.6). As a result, $R 2$ predicts the change in league points accumulated between seasons, rather than total league points accumulated per season.

Third, we consider other published match prediction models. Validation is achieved by taking into consideration match result predictions from these models to compute the expected number of league points for each team, per season. This requires access to the predictions generated by such models, but limits the selection to models which focus on the EPL and for seasons that fall within the periods of 2000/01 and 2014/15. We have access to the predictions generated by three models. Additionally, we have also considered the bookmakers' match odds, for a total of four match prediction models for validation purposes. These are:
4. pi-football v1: A BN model used to predict the match outcomes of the EPL season 2010/11 (Constantinou et al., 2012). This model generates match predictions by considering four generic factors for each team, namely a) strength, b) form, c) psychology, and d) fatigue. The model has components corresponding to each of the four generic factors. Component (a) is determined based on relevant historical match data with a limited memory process, which ensures that the more recent match results are more important than the less recent match results. On the other hand, components (b), (c) and (d) are predominantly dependent on subjective information, such as information about the availability of primary key players, team fatigue, team spirit and team match motivation.
5. pi-football v2: A BN model that was based on the philosophy of the pi-football model described above (hence we call them pi-football v1 and pi-football v2) and which was used to predict the match outcomes of the EPL season 2011/12 (Constantinou et al., 2013a).

This model combined data with knowledge about factors such as those considered in pi football $v 1$, but extended to factors such as the toughness of previous match, days gap since previous match, EU competition and National team involvement, and head-to-head bias. The model components were structured hierarchically and this made the model less computationally demanding compared to pi-football v1, and demonstrated even higher profitable returns when assessed against the published market odds.
6. pi-ratings: A rating system developed for the purpose to determine the level of ability of football teams (Constantinou \& Fenton, 2013b). The rating system was assessed by generating match predictions for EPL seasons 2007/08 to 2011/12. This is a very simple rating system that considers goal scoring discrepancies in matches to determine team ability over time. The ratings were assessed for predictive accuracy over five EPL seasons, from 2007/08 to 2011/12, and demonstrated superior performance with respect to the widely accepted ELO-based football ratings, and the performance was also on par (or marginally superior) to bookmakers odds.
7. Bookmakers: We have made use of the published market odds provided by Football-Data (2016) as predictions ${ }^{5}$ for the match instances of EPL seasons 2000/01 to 2014/15. We have considered the average bookmakers' odds for seasons 2005/06 to 2014/15, and the William Hill odds ${ }^{6}$ for seasons 2000/01 to 2004/05.

# 5.1 VALIDATION OF TEAM PERFORMANCE PREDICTION 

We have performed Leave-one-out cross-validation (LOOCV) to assess the accuracy of the BN model. Since the dataset consists of the EPL seasons 2000/01 to 2014/15 inclusive, this makes a total of 300 test cases (i.e., 20 teams per season and over 15 seasons). The LOOCV implies that, for each validated case, the model parameters are trained on the residual 299 cases with the resulting model used to predict the $300^{\text {th }}$, previously unseen, case. This process is repeated 300 times. The results are then compared against the seven models discussed above.

However, as discussed above, only four out of the seven models considered (i.e., $N M, R 1$, $R 2$, and Bookmakers) have predictions generated for all of the 15 seasons, 300 cases. The piratings predictions are restricted to five seasons (i.e., 100 cases), whereas the pi-fooball v1 and pifootball v2 predictions are restricted to a single season (i.e., 20 cases). To keep the comparison fair in these cases, we have also restricted the predictions of the BN model to the respective seasons associated with each of the three models. Consequently, the results presented in Table 1 are separated into four different sets. The main outcomes are:

- $N M$ is by far the worst predictor, as expected.
- The BN smart-data approach leads to superior predictions relative to the regression models $R 1$ and $R 2$, which are also employed with the dataset collated in this study. The regression

[^0]
[^0]:    ${ }^{5}$ Match odds are translated into probabilities and then normalised so that match outcome probabilities sum up to 1 (i.e., by eliminating the profit margin).
    ${ }^{6}$ Average bookmaking odds are not available for seasons 2000/01 to 2004/05. William Hill was the UK's biggest high street bookmaker for that period. Regardless, Constantinou et al., (2013c) showed that the normalised probabilities derived from different bookmakers' odds are almost identical.

models do consider injury and EU data for the season under assessment; implying that the regression models know the level of injury, the ability to deal with injuries, the type of EU competition, as well as the number of EU matches played. Conversely, these factors remain unknown for the season under prediction (i.e., $t_{3}$ ) in the BN model. If we were to remove these factors from the regression models we would have given an unfair advantage to the BN model on the basis that the BN does take this information into consideration at time $t_{1}$, but only for the purpose of assessing the true strength of the team at $t_{1}$. Instead, we had to give the advantage to the regression models. Still, the results suggest that the BN model gains a stronger advantage, over the regression models, from expert knowledge relating to the structure of the network and expert factors incorporated into the structure.

- Bookmakers, pi-football v1, pi-football v2, and pi-ratings, are all based on match data. This implies that these predictors benefit from model re-training after each additional match instance is observed throughout the season. This gives them an advantage with respect to the $B N, R 1, R 2$, and $N M$ predictions which are generated before the season commences. Still, the results in Table 1 show that the BN model outperformed two out of the four match prediction models, including Bookmakers, and this result highlights the potential of smart-data approaches to prediction. These results are also consistent with the predictive accuracy and profitability results reported in (Constantinou et al., 2012; 2013a), even though in those studies the predictive validation was more appropriately based on a match-by-match basis, rather than expected total league points over a season.

Table 1: Average error $E$, along with standard error of the mean (SEM) for each model, in terms of discrepancy between predicted and observed league points accumulated per team per season, over the specified league seasons $(L S)$. The range of league points in the EPL is 0 to 114 .


Figure 7 demonstrates how the predictive error is distributed from top performing teams (ranked at the top of each graph), in terms of total points accumulated between seasons, to bottom performing teams. There are eight graphs corresponding to the BN and each of the other seven models, ordered by worse to best performance based on Table 1. A paired-moving average is superimposed on the graphs.

Almost all graphs demonstrate a consistent pattern whereby the performance of top performing teams is underestimated and vice-versa for the bottom performing teams. This is a very interesting result since this pattern serves as one of the reasons for the existence of the so-called favourite-longshot bias, whereby bookmakers are believed to under-price longshots and overprice favourites on purpose to maximise profit, under the assumption that a higher volume of bets are placed on longshots (Cain et al., 2000, Forrest \& Simmons, 2001; 2002; Constantinou \& Fenton, 2013c). However, our results show that this pattern holds for different types of models, not just for Bookmakers, and arrives naturally irrespective of whether expert knowledge is incorporated with data.

Accepted for publication in Knowledge-Based Systems, 2017.
![img-6.jpeg](img-6.jpeg)

Figure 7: Predictive error (observed minus predicted) distributed from top performing teams (ranked at the top of each graph) to bottom performing teams. A paired-moving average is superimposed on the graphs.

# 5.2 VALIDATION OF TEAM-SPECIFIC UNSTABLE PERFORMANCES 

Time-series forecasting allows us to examine whether the model is equally consistent in predicting the evolution of team strength over multiple seasons. In doing so, we have considered the teams with the most unstable performances between seasons (i.e. teams which generate high discrepancy in points between seasons). We have restricted our selection criteria to teams which participated in at least 10 out of the 15 season considered, and to teams which experience an average discrepancy between seasons of at least 9 points (i.e. equivalent to three wins/losses).

Apart from the BN model, only four out of the seven competing models considered for validation purposes satisfy these criteria. Moreover, six teams meet the strong unstable performance criterion. Table 2 presents how each of the models performs when conditioned on each of these unstable teams. The results show that the error generated by the BN model, $E_{B N}$, increases on average by $14.06 \%$, which is rather faster than Bookmakers (i.e. $E_{\text {Book. }}$ ) that demonstrates an increase in error of $11.44 \%$. On the other hand, when it comes to the other three models, the error increases noticeably faster. The results in this section are in agreement to those presented in Section 5.1, and provide evidence that the predictive performance of the BN remains rather consistent, on average, even for unstable cases. However, on an individual team basis the error can still deviate considerably from the average error demonstrated over multiple seasons. For instance, the maximum error observed by the BN for a single team in a single season is 24.57 points for Liverpool during season 2013/14, followed by the error of 22.92 points for Ipswich during season 2000/01.

Table 2: Time-series validation, where $S$ is the number of seasons a team participated (out of 15 taken into consideration), and $E_{N M}, E_{R 1}, E_{R 2}, E_{\text {Book. }}$, and $E_{B N}$ are the prediction errors generated for No model, R1, R2, Bookmakers, and the BN model respectively.


# 6. SUPPLEMENTARY RESULTS AND DISCUSSION 

The results presented in this section involve the impact of specific factors of interest on team performance, in terms of league points accumulated per team, and hence provide a novel attribution study. Table 3 ranks these factors by positive influence on team performance. The results are as follows:

1. Transfers and team wages: Unsurprisingly, a Much higher net transfer spending (i.e. at least four times higher relative to the average adversary), in conjunction with an Extreme increase in team wages (i.e. at least $50 \%$ increase relative to the average adversary) generates the highest possible gain of 8.49 points. Rather surprising, however, is the reverse effect where Lower net transfer spending (i.e.at least two times lower than the average adversary) in conjunction with High decrease in team wages (i.e. at least $30 \%$ decrease relative to the average adversary) leads to a loss of just 1.75 points. Additionally, instability in terms of changes in players (i.e. when a team generates a high net transfer spending but team wages are reduced considerably; or vice versa) seems to generate a rather unsurprising decrease in performance of 3.73 points.
2. EU competition: Something that has been assumed all along, but for which no suitable analysis exists, is that the involvement in EU competitions negatively influences team performance in the league. Interestingly, the highest possible loss of 16.52 points is generated when a team participates in both ${ }^{7}$ EU competitions with No/Low EU competition readiness (i.e. previous season's EU involvement not surpassing four matches). The Europa League ${ }^{8}$ itself seems to carry a similar effect and generates a loss of 8.47 points. Another interesting observation is that a team with High EU readiness which fails to qualify for an EU competition experiences an important increase in league performance of 5.17 points. The Champions League, on the other hand, does not appear to follow the same pattern of impact. In fact, teams entering the Champions League with No/Low EU readiness seem to generate an increase in league performance of 1.52 points. It should be noted that Champions League qualification brings an immediate major financial reward, much of which is invested in player transfers.
3. Managerial changes: Changes in management do not appear to have as much of an impact on team performance as other factors do. Specifically, when a new manager joins a club, in conjunction with the departing manager's longevity with the club being Low (i.e. maximum of two season), a team's performance declines by 1.05 points. Interestingly, when the longevity of the departing manager is High (i.e. five seasons or more) the loss in performance is 4.64 points. On the other hand, retaining the same manager, which typically implies that the team under assessment is not under-performing (hence not seeking to replace the manager), generates an average of 0.92 points increase in performance.
4. Injuries: As expected, a high injury level in conjunction with the inability to deal with injuries (i.e. not many players capable of receiving the MotM award) leads to a significant loss of 8.31 points. On the other hand, teams who experience low levels of injury in conjunction with high ability to deal with injuries (i.e. many different players capable of receiving the MotM award) leads to 2.81 points increase in performance.
[^0]
[^0]:    7 This can happen when a team qualifies for the Champions league and subsequently joins the Europa league due to an early disqualification from the Champions league.
    8 Previously known as the UEFA Cup.

5. Promoted teams: The average promoted team generates a staggering increase in performance of 8.34 points, relative to the team being demoted in its place. This implies that the top teams of the Championship division are noticeably superior to the bottom teams of the EPL division. This outcome implies that the residual teams within the EPL are expected to lose some points, on average. The model indicates, that only the teams of Medium (i.e. between 50 and 69 points) and High (i.e. 70+ points) strength experience a decrease in performance of 3.02 and 2.91 points respectively, whereas teams of Low strength (i.e. less than 50 points) experience a gain in performance of 0.4 points.

Table 3: Model factors of interest and their impact on team performance, where $P$ is the expected impact on league points for the subsequent season.


# 7. CONCLUSIONS 

We have illustrated the reasoning towards the smart-data approach which is based on methods that support knowledge engineering and data engineering approaches to model development. The purpose of the knowledge engineering approach is to ensure that the model development is driven by what data are really required, rather than by what data are available, in order to achieve predictions and inferences of interest. The purpose of the data engineering approach is to ensure that data adhere to the causal (or otherwise) structure of the model, driven by real-world 'facts'.

The paper demonstrates how we applied this process of reasoning to the problem of predicting changes in football team performances between seasons in a time-series approach. This enabled us to provide more accurate predictions of the evolution of football teams' performance than is possible from purely data-driven models including standard non-linear regression models. Furthermore, the resulting model compares reasonably well against match prediction based models, including the bookmakers, which are based on far more data.

The implications of the paper are two-fold. First, with respect to the application domain, the current state-of-the-art is extended as follows:

1. This is the first study to present a model for time-series forecasting in terms of how the strength of football teams evolves over adjacent seasons, without the need to generate predictions for individual matches.
2. The results provide a novel and comprehensive attribution study of the factors most affecting performance (measured in terms of actual league points difference). For example, although unsurprisingly, the largest improvements in performance result from massive increases in spending on new players (an 8.49 points gain), an even greater decrease (up to 16.52 points) results from involvement in the European competitions (especially the Europa League) for teams that have previous little experience in such competitions.
3. Studies which assess the efficiency of the football gambling market may find the BN model helpful in the sense that it could help explain previously unexplained fluctuations in football odds.
4. Although the study had not intended to address it, the results also question (at least to some extent) the cause of the widely accepted favourite-longshot bias observed in bookies odds. This is because our results show that the favourite-longshot bias pattern holds for different types of models, not just for bookmakers' odds, and arrives naturally irrespective of whether knowledge is incorporated with data.

Second, with respect to the general strategy for learning from data, we have demonstrated that seeking larger datasets is not always the solution in terms of increasing predictive accuracy. The model presented in this paper, for instance, is based on just 300 data instances generated over a period of 15 years, whereas some of the external models considered for comparison purposes, and which underperformed relative to the BN model, are based on up to 5,700 match instances over those 15 years. We have also shown that standard non-linear statistical regression based models, which are still the standard method used in many areas of data-driven prediction for critical real-

world risk assessment problems, such as in medical decision analysis (Kendrick, 2014), failed to achieve predictive accuracy similar to the smart-data BN, or any of the other match-by-match models.

Smart-data aims to improve the quality, as opposed to the quantity, of a dataset which also directly influences the quality of the model. With smart-data one has to have a clear understanding of the inferences of interest. Inferring knowledge from data imposes further challenges and requires skills that merge the quantitative as well as qualitative aspects of data.

The paper questions whether automated learning of the available data is capable of inferring real-world facts, such as those incorporated into the BN model presented in this paper. It may be the case that resulting inferences in many real-world problems will be limited in the absence of expert intervention for data engineering and structure modelling purposes. Future research will examine the capability of causal discovery algorithms in terms of realising various real-world facts, and the impact various data-engineering interventions may have on the results.

# ACKNOWLEDGEMENTS 

We acknowledge the financial support by the European Research Council (ERC) for funding this research project, ERC-2013-AdG339182-BAYES_KNOWLEDGE, and Agena Ltd for software support.
