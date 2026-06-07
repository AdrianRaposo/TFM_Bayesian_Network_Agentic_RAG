# Investigating the efficiency of the Asian handicap football betting market with ratings and Bayesian networks 

Anthony C. Constantinou ${ }^{\mathrm{a}, \mathrm{b}, *}$<br>${ }^{a}$ Bayesian Artificial Intelligence Research lab, School of Electronic Engineering and Computer Science, Queen Mary University of London (QMUL), London, E1 4NS, UK<br>${ }^{\mathrm{b}}$ The Alan Turing Institute, UK

Received 8 August 2021
Accepted 29 October 2021
Pre-press 20 December 2021
Published 15 September 2022


#### Abstract

Despite the massive popularity of the Asian Handicap (AH) football (soccer) betting market, its efficiency has not been adequately studied by the relevant literature. This paper combines rating systems with Bayesian networks and presents the first published model specifically developed for prediction and assessment of the efficiency of the AH betting market. The results are based on 13 English Premier League seasons and are compared to the traditional market, where the bets are for win, lose or draw. Different betting situations have been examined including a) both average and maximum (best available) market odds, b) all possible betting decision thresholds between predicted and published odds, c) optimisations for both return-on-investment and profit, and d) simple stake adjustments to investigate how the variance of returns changes when targeting equivalent profit in both traditional and AH markets. While the AH market is found to share the inefficiencies of the traditional market, the findings reveal both interesting differences as well as similarities between the two.


Keywords: Directed acyclic graph, football prediction, graphical models, profitability, rating system, return-on-investment, soccer prediction

## 1. Introduction

Football prediction models have become immensely popular over the last couple of decades, and this is due to the increasing popularity of football betting. In the academic literature, such models typically focus on predicting the outcome of a match in terms of home win, draw, or away win; known as the 1 X 2 distribution. Several types of models have been published for this purpose and include rating systems (Leitner et al., 2008; Hvattum \& Arntzen, 2010; Constantinou \& Fenton, 2013; Wunderlich \& Memmert, 2018), statistical methods (Dixon \& Coles, 1997; Rue \& Salvesen, 2000; Crowder et al., 2002; Goddard, 2005; Angelini \& De Angelis, 2017), machine learning techniques (Huang \& Chang, 2010;

[^0]Arabzad et al., 2014; Pena, 2014), knowledge-based systems (Joseph et al., 2006), and hybrid methods that combine any of the above (Constantinou \& Fenton, 2017; Constantinou, 2018; Hubacek et al., 2018). In the recent special issue international competition Machine Learning for Soccer, the models that topped the performance table are hybrid and heavily rely on rating systems (Constantinou, 2018; Hubacek et al., 2018).

In Asia, the most popular form of betting (also common in Europe) is the so-called Asian Handicap (AH). This form of betting introduces a hypothetical handicap (i.e., advantage) typically in favour of the weaker team. Specifically, traditional AH introduces a goal deficit to the team more likely to win before kick-off. The manipulation of the match outcome creates interesting situations in which betting is determined by hypothetical, rather than actual, match outcome. Examples of the various types of AH

ISSN 2215-020X © 2022 - The authors. Published by IOS Press. This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial License (CC BY-NC 4.0).


[^0]:    *Corresponding author: Anthony C. Constantinou. E-mail: a. constantinou@qmul.ac.uk.

betting are provided in Section 2. This type of betting has also become popular in the UK over the last couple of decades. Football (soccer) syndicates are rumoured to bet millions per week, often on behalf of clients, on AH outcomes offered by bookmakers in Asia (Williams-Grut, 2016). This is because the Asian markets attract higher volumes of bets and offer greater market liquidity. Estimates suggest that over $70 \%$ of the betting turnover for football is recorded with Asian bookmakers (Kerr, 2018).

Whereas there is a large literature analysing traditional betting strategies, with researchers investigating how to optimise their betting, there has been only four published papers involving some analysis related to AH. Specifically, Vlastakis et al (2008) used AH odds as one of their model variables to predict match scores and showed that they are a strong predictor of match outcomes. Grant et al (2018) used AH odds, in conjunction with 1X2 odds, to analyse arbitrage opportunities and showed that these exist across a large number of fixed-odds and exchange market odds. Hofer and Leitner (2017) described how to derive information from live AH and Under/Over odds in order to maximise expected returns. Finally, and in an effort to educate gamblers, Hassanniakalager and Newall (n.d.) investigated the product risk associated with different football odds and showed that the AH odds would generally generate lower losses compared to other popular types of bet such as the 1X2, Under/Over, and correct score. Remarkably, no previous published work involves a model specifically designed for, and assessed with, AH bets.

The purpose of this paper is to investigate the efficiency of the AH market in relation to the 1X2 market. The 1X2 market has been extensively studied and the literature provides mixed empirical evidence regarding its efficiency, with most evidence pointing towards a weak-form efficient market (Giovanni \& De Angelis, 2019). In this paper, the efficiency of both markets is measured in terms of the ability of the model in discovering profitable betting opportunities given both average and maximum market odds. The model is based on a modified version of the pi-rating system, which is a previously published football rating system (Constantinou \& Fenton, 2013), that generates ratings that reflect team scoring ability. The ratings are provided as input to a novel hybrid Bayesian Network (BN) model specifically constructed to simulate the influential relationships between possession, shots, and goals, to predict both 1 X 2 and AH outcomes.

A BN is a type of a probabilistic model introduced by Pearl (Pearl, 1985) that consists of nodes and arcs. Nodes represent variables and arcs represent conditional dependencies. A BN that consists of both discrete and continuous variables, such as the one constructed in this study, is called a hybrid BN. Each variable has a corresponding Conditional Probability Distribution (CPD) that captures the magnitude as well as the shape of the relationship between directly linked variables. If we assume that the arcs in the BN represent influential relationships, then such a model can be viewed as a causal graph and represents a unique Directed Acyclic Graph (DAG) that can be used for interventional analysis. Otherwise, the arcs represent conditional dependencies that are not necessarily causal relationships, and such a BN is not a unique DAG but rather a Partial DAG that represents an equivalence class of DAGs. For a quick introduction to BNs, with a focus on football examples, see (Constantinou \& Fenton, 2018).

Based on 13 English Premier League seasons and betting simulations under different assumptions, the findings reveal interesting differences as well as similarities between the AH and 1X2 markets. Importantly, the AH market is found to share inefficiencies with the traditional 1X2 market, and this provides opportunities for 'beating' the market. The paper is structured as follows: Section 2 describes the rules of the AH betting market, Section 3 describes the model, Section 4 covers the data and the process of model fitting, Section 5 presents the results, and Section 6 provides the concluding remarks.

## 2. Asian handicap betting rules

In what follows, the decimal odds system is used (also known as European odds) for payoff in the event of winning a bet. The decimal odds represent the total return ratio of the stake; implying that the stake is already included in the decimal number. For example, a payoff of ' 3 ' returns three times the stake; i.e., a bet of $£ 1$ would return $1 \times 3=£ 3$ ( $£ 2$ profit). Odds also reflect probability that incorporates the bookmakers' profit margin. An example from data is the Arsenal versus Crystal Palace match played on 21/04/2019 with average 1X2 market odds $1.54,4.44,6.03$, corresponding to probabilities $\{64.94 \%, 22.52 \%, 16.58 \%\}$. Summing up these probabilities gives us $104.04 \%$, and the implied average profit margin of $4.04 \%$.

The AH betting market operates such that adversaries are handicapped according to their difference in

Table 1
The whole-goal AH outcome for different hypothetical scores between Arsenal and Crystal Palace


strength. The term handicap means that one team is assigned a hypothetical score (including fractional) advantage before the match is played. All types of AH betting offered by the bookmakers involve two possible outcomes. This means that the AH betting market reduces the possible match outcomes from three (i.e., 1X2) to two. Each binary outcome corresponds to each team winning, with the odds adjusted subject to the given handicap.

The standard AH betting involves assigning a hypothetical score advantage to the underdog. This represents the most common type of AH betting, and aims to make the contest equal. That is, the handicap applied is the one ${ }^{1}$ that optimises the odds, for both teams to win, towards 2 (or $50 \%$ chance of winning) and hence, it maximises the uniformity of the AH payoff distribution. While this represents the most popular type of bet, the AH market offers different types of score advantage, each of which we discuss below, including the possibility to assign a hypothetical score advantage to the favourite rather than the underdog.

The market offers three types of AH betting that need to be modelled explicitly into the model, as well as in the betting simulation. These are:
i. Whole goal handicap: A team is given a wholegoal handicap such as -1 or +1 . In this case, the possibility of a draw is eliminated by removing the draw outcome from the equation and normalising the probabilities of the residual two outcomes to sum up to 1 . If a handicap draw is observed, the bet is voided (refunded).

Let us revisit the example from data discussed at the beginning of this section, involving Arsenal versus Crystal Palace with average 1X2 market odds $\{1.54,4.44,6.03\}$. Arsenal was the

[^0]strong favourite. The bookmakers introduced the handicap of -1 , which maximised the uniformity of the AH distribution with odds $\{1.87,1.99\}$. The match ended 2-3; i.e., -1 for Arsenal. The AH winner was Crystal Palace since it won the match by one goal difference, which makes it two goals difference given the handicap; i.e., this made the settlement score, which is the match result after the handicap is considered, equal to 2. Table 1 illustrates how the whole-goal AH is determined based on other hypothetical score lines between Arsenal and Crystal Palace.
ii. Half-goal handicap: A team is given a half-goal handicap such as -1.5 or +1.5 . Assuming a match between $X$ and $Y$ and a handicap of +1.5 (i.e., $X$ receives a 1.5 goal advantage), and that a bet is placed on $X$, the bet would win as long $X$ does not lose by more than one goal difference; otherwise the bet is lost. In this case, the possibility of a draw is eliminated by the handicap itself, since it is not possible for the settlement score to be a draw.

An example from data is the Liverpool versus Wolves match played on 12/05/2019 with average 1X2 market odds $\{1.30,5.62,10.17\}$. Liverpool was the strong favourite. The bookmakers introduced the handicap of -1.5 , which maximised the uniformity of the AH distribution with odds $\{1.91,1.95\}$. The match ended $2-0$ (i.e., +2 ) in favour of Liverpool. The AH winner was Liverpool since it won the match by two goals difference; i.e., 0.5 goals more than the handicap. This made the settlement score equal to 0.5 . Table 2 illustrates how the half-goal AH is determined based on other hypothetical score lines between Liverpool and Wolves.
iii. Quarter-goal handicap: A team is given a quarter-goal handicap such as -0.25 or +0.25 . This type of handicap is, in fact, a combined whole-goal and a half-goal handicap.


[^0]:    ${ }^{1}$ The other handicaps do not share the same market liquidity; implying limited stakes and possibly also higher profit margins, for the bookmaker, due to lower competition.

Table 2
The half-goal AH outcome for different hypothetical scores between Liverpool and Wolves


Table 3
The quarter-goal AH outcome for different hypothetical scores between Fulham and Newcastle


For example, if we bet $£ 10$ on the away team to win given $\mathrm{AH}-0.25$ with odds 2 (i.e., $50 \%$ ), the stake would be divided between the nearest whole-goal and half-goal handicaps. That is, a $£ 5$ bet will be placed on the away team to win given $\mathrm{AH} \pm 0^{2}$ with odds $\sim 2.5$ (i.e., $40 \%$ ) and another $£ 5$ bet on the away team to win given $\mathrm{AH}-0.5$ with odds $\sim 1.66$ (i.e., $60 \%$ ). Note that the odds for the quarter-goal handicap reflect the average payoff, in terms of probability, of the two nearest handicaps. Since this is a combination of two bets, each bet is executed independently. For example, a score of $0-0$ would have resulted in voiding $\mathrm{AH} \pm 0$ (i.e., $£ 5$ are returned) and winning $\mathrm{AH}-0.5$ (i.e., $£ 5 \times 1.66=£ 8.3$ are returned).

An example from data is the Fulham versus Newcastle match played on 12/05/2019 with average 1X2 market odds $\{2.50,3.53,2.78\}$. Fulham was the weak favourite. The bookmakers introduced the handicap of -0.25 , which maximised the uniformity of the AH distribution with odds $\{2.15,1.75\}$. The match ended $0-4($ i.e., -4$)$ in favour of Newcastle. The AH winner was Newcastle, since it won the match by four goals difference; i.e., 4.25 goals more than the handicap. This made the settlement

[^0]score equal to -4.25 . Table 3 illustrates how the quarter-goal AH is determined based on other hypothetical score lines between Fulham and Newcastle.

## 3. The model

The overall model combines ratings with BNs. The rating system captures the skill of teams over time, and provides the ratings as an input into the BN model which captures the magnitude of the relationships between variables of interest. The two subsections that follow describe the rating system and the BN model respectively.

### 3.1. The rating system

The pi-rating is a football rating system that determines team ability based on the relative discrepancies in scores between adversaries. It was first introduced in (Constantinou \& Fenton, 2013) and thereafter used in (Constantinou, 2018; Hubacek et al., 2018; 2019; Van Cutsem, 2019; Wheatcroft, 2020). Modified versions of the pi-rating also formed part of the top two performing models in the international competition Machine Learning for Soccer (Constantinou, 2018; Hubacek et al., 2018). This paper makes use of the original pi-rating system (Constantinou \& Fenton, 2013), with two modifications described below.


[^0]:    ${ }^{2}$ A zero-goal AH implies no handicap, but that there must be a match winner; otherwise, the bet is voided.

The pi-ratings assign a 'home' $(H)$ and an 'away' $(A)$ rating to each team, to account for team-specific home advantage and away disadvantage. Therefore, when a team $X$ plays against team $Y$, the match prediction is determined by team's $X$ rating $H$ versus team's $Y$ rating $A$. The ratings are revised after each match based on two learning rates: a) the learning rate $\lambda$ which determines to what extent new match results override previous match results in terms of the impact in determining current team ratings, and b) the learning rate $\gamma$ which determines to what extent performances at home grounds influence a team's away rating and vice versa. Therefore, at the end of a match between teams $X$ and $Y$, the new ratings at time $t$ are revised given the most recent ratings at time $t-1$ as follows:

$$
\begin{aligned}
& X^{\prime} \text { s } H \text { rating : } R_{X H}^{t}=R_{X H}^{t-1}+e_{H} \lambda \\
& X^{\prime} \text { s } A \text { rating : } R_{X A}^{t}=R_{X A}^{t-1}+\gamma\left(R_{X H}^{t}-R_{X H}^{t-1}\right) \\
& Y^{\prime} \text { s } A \text { rating : } R_{Y H}^{t}=R_{Y H}^{t-1}+e_{A} \lambda \\
& Y^{\prime} \text { s } H \text { rating : } R_{Y H}^{t}=R_{Y H}^{t-1}+\gamma\left(R_{Y A}^{t}-R_{Y A}^{t-1}\right)
\end{aligned}
$$

where $e$ is the error between the observed goal difference $\Delta_{o}$ and rating difference $\Delta_{-} p$ which, for home and away teams, is measured as follows:

$$
e_{H}=\Delta_{o H}-\Delta_{p H} \text { and } e_{A}=\Delta_{o A}-\Delta_{p A}
$$

respectively, where

$$
\begin{aligned}
& \Delta_{o H}=G_{o H}-G_{o H} \text { and } \Delta_{o A}=G_{o A}-G_{o H} \\
& \Delta_{p H}=G_{p H}-G_{p A} \text { and } \Delta_{p A}=G_{p A}-G_{p H}
\end{aligned}
$$

where $G_{o H}$ and $G_{o A}$ are goals observed for home and away teams respectively, and similarly $G_{p H}$ and $G_{p A}$ are goals predicted for home and away teams.

While the original pi-ratings represent a diminished expectation of goal difference against the average opponent in the data, in this paper they represent the actual goal difference expectation. Specifically, the rating equation in this paper is simplified not to include the deterministic function $\Psi(e)=3 \times \log _{10}(1+e)$ defined in the original paper (Constantinou \& Fenton, 2013), which is a function that diminishes the importance of each additional goal difference under the assumption that a win is more important than increasing goal difference. The justification for this first modification is that, in AH, we are only interested in goal differences and thus, the motivation here is to optimise for goal difference rather than the ability to win matches.

The second modification involves the learning rate $\lambda$. In this paper, $\lambda$ is multiplied by $k$ when a match involves at least one team which had previously played less than 38 matches, according to available data. This modification aims to increase the speed by which team ratings converge for new teams during their first EPL season (each team plays 38 matches in a season), and is expected to be especially impactful during the very first season in the data since, at that point, all teams are considered 'new' by the rating. Therefore, the revised pi-ratings exclude $\psi(e)$, defined above, and include $k$, as follows:

$$
R_{X H}^{t}=R_{X H}^{t-1}+e_{H} \lambda k \text { and } R_{Y A}^{t}=R_{Y A}^{t-1}+e_{A} \lambda k
$$

where $k=3$ for match instances in which both teams had previously played less than 38 matches; otherwise $k=1$. The parameter $k$ was optimised in terms of minimising prediction error $e$. A limitation here is that the $k$ parameter was optimised given integer inputs from 1 to 10 . For future work, it is recommended that the $k$ parameter is optimised given real numbers.

### 3.2. The BN model

The graph of a BN model can be automatically discovered from data, determined by knowledge, or a combination of the two. Learning the correct graph of a BN from data remains a major challenge in the fields of probabilistic machine learning and causal discovery. While some structure learning algorithms perform well with synthetic data, it is widely acknowledged that this level of performance does not extend to real-world data which typically incorporate noise and latent confounders.

In disciplines like bioinformatics, applying structure learning algorithms can reveal new insights that would otherwise remain unknown. However, these algorithms are less effective in areas with access to domain knowledge, such as in sports. As a result, the BN model in this paper has had its graphical structure determined by the temporal fact that possession influences the number of shots created, which in turn influence the number of shots on target, and which in turn influence the number of goals scored. Each of these factors is also dependent on the level of rating difference between the two teams, as illustrated in Fig. 1. This type of model can also be characterised as a hierarchical Bayesian model of which the network is the structural representation, and where the nodes represent variables or hyperparameters of statistical distributions.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The BN model. The Rating Difference $(R D)$ is the only observable node in the network, determined by the pi-ratings, and represents the difference between the home team's prior home rating and the away team's prior away rating $R_{X H}^{t-1}-R_{Y A}^{t-1}$.

The temporal order of events in the BN graph naturally captures the importance of each event in predicting goals scored. For example, the graph assumes that shots on target have a direct influence on goals scored, whereas possession has an indirect influence and hence, while influential, it is assumed to be less impactful than shots on target. While the temporal order defines direct and indirect influences, note that the magnitude of direct influences is still determined by data.

For each match, the prior ratings are retrieved and the difference in team ratings is used as an input into the BN model, which is a Hybrid BN model consisting of both discrete and continuous variables, designed in AgenaRisk (Agena, 2019). Specifically, the actual input is the difference between prior home and away ratings, and is passed to the BN model as an observation to node Rating Difference $(R D)$ in the form of

$$
R_{X H}^{t-1}-R_{Y A}^{t-1}
$$

To ensure that the BN model is trained accurately with respect to the rating data, the parameterisation of the CPDs is also restricted to match instances in which both teams had previously played at least 38 matches. All the residual variables in the BN model are latent. Specifically,
i. The node $R D$, which represents the observable rating difference between teams, is a mixture of Gaussian probability density functions $\sim N\left(\mu, \sigma^{2}\right)$; one for each state of node Rating Difference Level (RDL). Specifically, for $-\infty<R D<\infty$,

$$
\begin{aligned}
& f(R D \mid \mu, \sigma^{2}, R D L)= \\
& \quad\left[\left(\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-\frac{\left(R D-\mu\right)^{2}}{2 \sigma^{2}}}\right) \mid R D L\right]
\end{aligned}
$$

where parent $R D L$ is a discrete distribution, $\mu$ is the average rating difference and $\sigma^{2}$ the variance of the rating differences. $R D L$ consists

Table 4
Predetermined levels of rating difference


of 23 states $^{3}$, where each state corresponds to a pre-determined level of rating difference as shown in Table 4. For example, the rating difference level 3 is parameterised based on all historical match instances in which adversaries had rating difference $R D=R_{X H}^{i-1}-R_{Y A}^{i}$ ranging from 1.765 to $<1.93$. The granularity of the 23 states has been chosen to ensure that for any combination of rating difference there is enough data points (more than 50) for a reasonably well informed prior.
ii. The node $P$, which represents ball possession, is a mixture of probability density functions $\sim \operatorname{Beta}(a, \beta)$; one for each state of $R D L$. Specifically, for $P \in[0,1]$,

$$
\begin{aligned}
& f(P \mid a, \beta, R D L)= \\
& \quad\left(\left.\frac{P^{a-1}(1-P)^{\beta-1}}{\operatorname{Beta}(a, \beta)} \right\rvert\, R D L\right)
\end{aligned}
$$

where $\operatorname{Beta}(\alpha, \beta)$ is the Beta function, $\alpha$ is the first shape parameter of the Beta function, also known as the alpha parameter, and represents the number of minutes the home team is in possession of the ball, and $\beta$ is the second shape parameter of the Beta function, also known as the beta parameter, that represents the number of minutes the away team is in possession of the ball. Thus, $P$ reflects the possession rate associated with the home team, over a Beta distribution, whereas for the possession of the away team the model assumes $1-P$.
iii. The node $p(S M)$, which represents the probability to generate a shot per minute spent in possession of the ball, is also a mixture of probability density functions $\sim \operatorname{Beta}(a, \beta)$ given $R D L$, where $\alpha$ is the number of shots and

[^0]$\beta$ is the number of minutes minus the number of shots.
iv. The node $S$, which represents the expected number of shots, is a Binomial probability mass function $\sim B(n, p)$,

$$
\begin{aligned}
& f(k, n, p)-\operatorname{Pr}(k \mid n, p)= \\
& \quad \operatorname{Pr}(S=k)=\left(\frac{n!}{k!(n-k)!}\right) p^{k(1-p)^{n-k}}
\end{aligned}
$$

where $n$ represents the number of minutes in possession of the ball defined as ${ }^{4} \mathrm{P} \times 90$, under the assumption a match lasts 90 playable minutes, and $p$ is $p(S M)$; i.e., the probability to generate a shot per minute spent in possession of the ball, as defined above.
v. The node $p(S T)$, which represents the probability for a shot to be on target, is also a mixture of probability density functions $\sim \operatorname{Beta}(a, \beta)$ given $R D L$, where $a$ is the number of shots on target, and $\beta$ is the number of shots off target; i.e., total shots minus shots on target.
vi. The node $S T$, which represents the expected number of shots on target, is also a Binomial probability mass function $\sim B(n, p)$, where $n$ is the expected number of shots $S$ and $p$ is the probability for a shot to be on target $p(S T)$.
vii. The node $p(G)$, which represents the probability to score a goal, is also a mixture of probability density functions $\sim \operatorname{Beta}(a, \beta)$ given $R D L$, where $\alpha$ is the number of goals scored, and $\beta$ is the number of shots on target successfully defended; i.e., total shots on target minus goals scored.
viii. The node $G$, which represents the expected number of goals scored, is also a Binomial probability mass function $\sim B(n, p)$, where $n$ is the expected number of shots on target $S T$, and $p$ is the probability to score a goal $p(G)$.
ix. The node 1 X 2 is a discrete distribution with states Home win, Draw, and Away win, determined by the distributions $G$ of both home $(H)$

[^1]
[^0]:    ${ }^{3}$ The decision to discretise $R D L$ represents a practical choice for Hybrid BN modelling. In this case, discretising $R D$ into $R D L$ was necessary to capture conditional Beta-Binomial relationships from Possession to Goals scored, given the rating difference between adversaries.

[^1]:    ${ }^{4}$ For the away team (i.e., $A T$ ) it is $(1-P) \times 90$.

Table 5
The data variables used to train the rating system (R), the BN model (BN), and to simulate betting (B)


and away $(A)$ teams; i.e., $1 \mathrm{X} 2=$ "Home win" if $G_{o H}>G_{o A}$, "Away win" if $G_{o H}<G_{o A}$, "Draw" otherwise.
x. The node $G D$, which represents goal difference, is simply $G_{o H}-G_{o A}$.
xi. The node $A H$ represents a set of nodes corresponding to all the possible AH outcomes with state probabilities for home and away wins, given $G D$, as defined in Section 2.

It should be clear by this point that for both home and away teams: a) nodes $P$ and $p(S M)$ are hyperparameters of Beta node $S$, b) nodes $S$ and $p(S T)$ are hyperparameters of Beta node $S T$, and c) nodes $S T$ and $p(G)$ are hyperparameters of node $G$; effectively creating a Beta-Binomial Hybrid BN process.

## 4. Data and model fitting

### 4.1. Data

The rating method, the BN model, and the betting simulation are based on data collected from www.football-data.co.uk and manually recorded from www.nowgoal.com. Table 5 specifies which of the data variables are used by the rating system, the BN model, and the betting simulation. For example, the rating system only requires information about goal data and hence, it only considers variables Date, Home team, Away team, Home goals, and Away goals. Since the ratings are used as an input into the BN model, they represent an additional BN variable and at the same time make the BN model independent of variables Date, Home team and Away team.

The data are based on the English Premier League (EPL) seasons 1992/93 to 2018/19. However, AH odds data were available only from season 2006/07 onwards, whereas ball possession data which is needed by the BN model were available only from season 2009/10 onwards. As a result, the rating system is trained with up to 27 seasons of data, the BN is parameterised with up to 10 seasons of data (since it requires possession data), and the betting simulation is performed over 13 seasons (since it requires AH odds data).

### 4.2. Model fitting

By definition, the ratings are developed in a temporal manner. That is, for a match prediction at time $t$ the model considers team ratings at time $t-1$. For any match prediction, a team's rating will always be based on the most recent rating prior to the date of the match under prediction, and a team's rating will always be based on past match results.

Conversely, the BN model functions as a machine learning model independent of time and is validated using leave-one-out cross validation (LOOCV). A prediction between teams that have rating difference $Z$, where $Z$ is one of the 23 RDLs as defined in Table 4, is derived from all data matches with rating difference Z, excluding the match under prediction during validation.

This combination of model parameterisation and validation with a rating system and a BN model is adopted by (Constantinou, 2018). The validation approach is unconventional because the BN model assumes no temporal relationships. When applied to past matches, it generates predictions at time $t$

based on the whole data set which may include future match results. The reason this approach works well, without overestimating the future accuracy of the model, is because it does not matter whether the data comes from past or future. This is because the model assumes that the relationship between, for example, shots on target and goals scored remains invariant over time for the average EPL team, and empirical results support this claim. These include:
i. The results presented in Sections 5.2 and 5.3 which show that predictive accuracy is consistent across all 13 seasons tested, including the three seasons 2006/07 to 2008/09 which did not form part of the BN's training data;
ii. The model in (Constantinou, 2018) which was based on this approach and ranked 2nd in the international Machine Learning for Soccer competition, with a prediction error consistent with the validation error.

The empirical support for the model extends to demonstrating that the model can produce good predictions for matches between teams $X$ and $Y$ even when the prediction is derived from match data that neither X nor Y participated in (Constantinou, 2018). This claim is also supported by the results presented in this paper. Specifically, during Seasons 2006/07 to 2008/09 the following teams have had their performance determined by data that did not include any of their matches: a) Sheffield United, b) Charlton, and c) Derby. The reason this occurred is because, as discussed above, the BN model was trained with data from season 2009/10 onwards, which does not include any match instances associated with these teams. Their performance in terms of possession, shots, shots on target and goals scored was derived by other similar match situations in terms of rating difference between home and away teams.

This approach has advantages and disadvantages. The disadvantage is that, for those who are interested in how such a model would have performed in the past, the results only approximate past performance under the assumption the model would have been trained with at least the same amount of data as the test model. On the other hand, the advantage is that this approach allows us to preserve the sample size of the training data throughout validation, and this enables us to validate how the resulting model would have performed over multiple seasons without modifying its parameterisation (excluding the removal of a single sample; i.e. the match under assessment during validation).

To understand why this is important, consider evaluating match instances five seasons in the past. A temporal model would require the removal of the five most recent seasons from the training data. This would have led to limited samples for some of the predetermined levels of rating difference shown in Table 4. The limited data issue can only be overcome by reducing the number of predetermined levels of rating difference (i.e., the dimensionality of the model); but doing so would produce a different model than the one described. Instead, the approach adopted by (Constantinou, 2018) enables us to address the temporal aspect of the problem through the ratings and to preserve the fitting of the BN across all seasons tested; effectively enabling us to test the current parameterised model on multiple seasons independent of time.

## 5. Results

The results are reported in terms of rating (i.e., goal difference) error, predictive accuracy and profitability. Specifically, Section 5.1 assesses the accuracy of the modified pi-ratings in terms of expected goal difference error, Section 5.2 assesses the accuracy of the overall model in predicting both AH and 1X2 outcomes, and Section 5.3 assesses the capability of the model in terms profitability in both 1 X 2 and AH markets.

### 5.1. Pi-ratings accuracy and overall model fitting

Figure 2 shows that the optimal $\lambda$ and $\gamma$ parameters, that minimise the goal difference error as defined in Section 3, are $\lambda=0.018$ and $\gamma=0.7$. Note that while the results are based on training data from seasons 1992/93 to 2018/19, the optimisation is restricted to match instances in which both teams had previously played at least 38 matches; a total of 9,073 match instances. This is to ensure that the model is optimised on matches in which both teams have had their ratings developed by at least one football season.

The optimal learning rates are fairly consistent with those reported in (Constantinou \& Fenton, 2013) (i.e., $\lambda=0.035$ and $\gamma=0.7$ ) on the basis of minimising goal difference error over five EPL seasons, with those reported in (Van Cutsem, 2019) (i.e., where $\lambda=0.06$ and $\gamma=0.6$ ) on the basis of minimising mean squared goal difference error over eight EPL seasons, with those reported in (Constantinou, 2018),

![img-1.jpeg](img-1.jpeg)

Fig. 2. The optimal modified pi-rating learning rates and associated prediction error $e$, given $k=3$, are $\lambda=0.018$ and $\gamma=0.7$. The results are based on training data from seasons 1992/93 to 2018/19. The optimisation is restricted to match instances in which both teams had previously played at least 38 matches; a total of 9,073 match instances.
$\lambda=0.054$ and $\gamma=0.79$, on the basis of minimising the Rank Probability Score (RPS) error metric (Constantinou \& Fenton, 2012) over multiple leagues worldwide, and with those reported in (Hubacek et al., 2018), $\lambda=0.06$ and $\gamma=0.5$, where pi-ratings had been used in conjunction with Gradient boosted trees parameters to minimise RPS over multiple leagues worldwide.

However, note that the optimal learning rate $\lambda$ is lower in this study, and this is likely due to the modification that performs more aggressive rating revisions to the first 38 matches of each team, since it is intended to improve the speed of rating convergence. Interestingly, the overall mean goal difference error shown in Fig. 2, $e=1.2283$ (or $e^{2}=1.509$ ), is considerably lower than those reported in (Constantinou \& Fenton, 2013) and (Van Cutsem, 2019), where $e^{2}=2.625$ and $e^{2}=2.66$ respectively, and this suggests that the modifications have had a positive impact on the ratings.

Figure 3 illustrates the expected goal difference for each of the 23 rating difference levels. Level 23 represents the highest rating discrepancy in favour of the away team, where the average expectation of the match is a score difference of -1.38 (or 1.38 goals in favour of the away team), and level 1 represents the highest rating discrepancy in favour of the home team with an expected score difference of 2.18 (or 2.18 goals in favour of the home team). The graph reveals a linear relationship between rating discrepancy and score discrepancy.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Sensitivity analysis between the 23 states of $R D L$ node and the expected goal difference, with linear trendline superimposed as a dashed red line.

As shown in Table 4, the granularity of the 23 intervals was selected to ensure that for any rating difference state there are at least 50 data points for a reasonably well-informed prior of observed goal difference. As with any discretised variable, different splits produce slightly different results. In the case of the $R D L$ distribution, any changes in discretisation will remain faithful to the linear relationship illustrated in Fig. 3; implying that we should expect minor changes to the interval averages as long as the number of splits remains invariant and data points for each interval are maintained above 50.

Table 6
The discrepancy in prediction error $e$ for the different combinations of $\lambda$ and $\gamma$, relative to the optimal inputs of $\lambda=0.018$ and $\gamma=0.7$. Darker green cells represent lower discrepancy, whereas darker red cells represent higher discrepancy. Recommended inputs for $\lambda$ and $\gamma$ are the ones that generate up to $0.01 \%$ discrepancy


Any minor model amendment is naturally expected to have minor impact on the predicted probabilities, and any minor impact is expected to have some influence on the results based on small discrepancies between predicted and published market odds (i.e., small $\theta$ values as defined later in subsection 5.3 , such as $\theta=1$ or 2 ). However, no changes are expected for larger discrepancies. Since the conclusions in this paper are not driven by results that are based on such small differences between predicted and observed odds, any minor modification is not expected to alter concluding remarks.

Table 6 presents the discrepancy in prediction error $e$ for the different hyperparameter combinations of $\lambda$ and $\gamma$, relative to the prediction error generated by the optimal inputs of $\lambda=0.018$ and $\gamma=0.7$. Recommended values for $\lambda$ and $\gamma$, that could be considered as an alternative to the optimal values of $\lambda=0.018$ and $\gamma=0.7$, are the ones that generate up to $0.01 \%$ discrepancy in prediction error. A total of 31 different combinations, excluding the optimal combination, generate discrepancy within the $0.01 \%$ threshold. By keeping the value for $\lambda$ static, the recommended hyperparameter combinations are a) $\lambda=0.017$ and $\gamma=0.65-0.73$, b) $\lambda=0.018$ and $\gamma=0.65-0.74$, c) $\lambda=0.019$ and $\gamma=0.65-0.74$, and d) $\lambda=0.02$ and $\gamma=0.7-0.72$.

### 5.2. Predictive accuracy

Predictive accuracy is measured for both 1X2 and AH distributions. The Brier Score is used to measure the accuracy of the binary AH outcome, and the RPS metric (Constantinou \& Fenton, 2012) is used to measure the accuracy of the multinomial 1X2

Table 7
Predictive accuracy across all seasons, based on the Rank Probability Score (RPS) for multinomial 1X2 predictions and the Brier Score (BS) for binary AH predictions. Lower score indicates higher predictive accuracy for both RPS and BS


distribution. The RPS can be viewed as a Brier Score extended to multinomial ordinal distributions.

Table 7 shows that the RPS error for the 1X2 outcomes ranges from 0.184 to 0.213 with an average RPS of 0.195 across all 13 EPL seasons. This result compares well relative to previous studies that assumed pi-ratings. Specifically, in (Constantinou, 2018) the RPS ranged from 0.187 to 0.236 for 52 different leagues worldwide, with an average RPS of 0.211 at validation, an average RPS of 0.203 for EPL matches, and an average RPS of 0.208 in the competition. Similarly, the average RPS was $\sim 0.2$ in (Hubacek et al., 2018), according to Fig. 3, and 0.206 in the competition.

These results are consistent with those reported in Section 5.1, which show that the overall error $e$

![img-3.jpeg](img-3.jpeg)

Fig. 4. Investigating the prediction shift over time, with reference to the four main variables of the BN model. The shift is measured in terms of the expected value of the specified distribution, and by adding a football season's worth of data, to the training data set, at a time.
optimises lower in this study; i.e., the ratings more accurately predict score difference. The results from profitability presented in Section 5.3 are also consistent with these findings.

### 5.2.1. Time-series analysis and sample size requirements

The model is trained with data the covers 13 years of data, and not all the variables could be measured throughout this period. Still, the model seems to work well without evidence of bias. This subsection investigates whether the variables used in the model show any drift over time that the model might have filtered out. Moreover, because the dimensionality of the model has been adjusted relative to the available sample size, this subsection also reports the sample size required for the model priors to be well informed by data.

Figure 4 presents the results from time-series analysis in investigating potential shifts in the predictive outputs of the model over time. The analysis is performed by increasing the training data set by a single football season's worth of data at a time, and the shift is measured in terms of changes in the expected value of the given distribution. As shown in Fig. 4, the analysis focuses on the four main variables of the BN
model; namely possession, shots, shots on target, and goals scored. Moreover, the different levels of rating difference (refer to Table 4) are categorised into four groups, and are measured with reference to the 10 specified seasons.

The reason the first three, out of the 13, seasons are not considered here is because (as later shown in Table 8) the BN model was not trained with data samples from the first two seasons, and this also means that any results obtained during the third season rely on very low samples. As previously discussed in subsection 3.2, the reason the first two seasons are not considered by the BN model is because the BN is trained with match instances in which both teams had previously played at least 38 matches, to allow for the pi-ratings to converge to reasonably accurate estimates before considered for model training.

The results are discussed with reference to Table 8, which presents the available samples for each of the 23 levels of rating difference, after each subsequent league data set is added to the training data set that was used to learn the BN model. The results show that many of the shifts occur in the first few seasons, and this is reasonable since the first seasons are the ones which rely on fewer samples. Shifts are also observed after adding the most recent leagues, but these shifts

Table 8
The number of data samples observed in each of the 23 intervals of Rating Difference Level (RDL) after each subsequent league data set is added to the training data. Darker red cells represent sample size less than 19 (equivalent to less than half a season's data), orange cells represent sample size less than 38 (equivalent to more than half, and less than, a season's data), and white cells represent sufficient sample size


are largely restricted to the outputs of possession and shots on target, and involve matches with a level of rating difference between 1 to 6 . The most important output of the model, which is the goal difference, remains essentially unchanged over time. Therefore, while it is reasonable to assume that shifts in playing style might occur naturally from season to season, collectively these shifts appear to have no meaningful impact on the prediction of goal difference, from which the 1 X 2 and AH distributions are formed.

Lastly, the results in Table 8 suggest that the model described in this paper should be trained with at least five seasons of league data, to ensure that the model priors are well informed by data. Because the model is trained with publicly available data, and which only increases over time, there is no motivation to use less data than what is currently available and hence, this requirement should not be viewed as a limitation.

### 5.3. Profitability

The assessment of profitability is based on 13 EPL seasons and considers both the average and the best available (maximum) market odds. The simulation is evaluated both in terms of maximising profit as well as the Return On Investment (ROI). A standard betting strategy is used where fixed singe-unit bets (e.g., $£ 1$ ) are placed on 1 X 2 and AH outcomes with payoff that is higher than the model's estimated unbiased payoff by at least $\theta$, where $\theta$ is the discrepancy between the predicted probability and the payoff probability. For example, if the model predicts $51 \%$ and the bookmakers' payoff for that event is $50 \%$ (i.e., odds of 2 ), then $\theta=1$; i.e., the bookmakers pay $1 \%$
more than the model's estimate. The betting simulation is performed across all payoff decision thresholds $\theta$, for both 1X2 and AH outcomes. The results are first discussed in terms of 1X2 betting performance with reference to Tables 9, 10 and 11; then in terms of AH betting performance with reference to Tables 12, 13 and 14 .

Table 9 presents the profitability generated by 1 X 2 bets over all possible payoff decision thresholds $\theta$, assuming static $\theta$ across all 13 seasons, for both average and maximum market odds. Unsurprisingly, the results show that it is much easier for the model to generate profit when taking advantage of the maximum market odds. Moreover, low thresholds $\theta$ (i.e., when the predictions are roughly in agreement with market odds) are not profitable. Interestingly, ROI maximises at much higher thresholds $\theta$ compared to profit; i.e., profit maximises at $8 \%$ and $9 \%$ whereas ROI at $18 \%$ and $16 \%$, for average and maximum market odds respectively. This is because lower thresholds $\theta$ generate a higher number of bets which can generate higher profit even if ROI is lower.

Tables 10 and 11 show how the profitability changes when we consider the threshold $\theta$ that maximises ROI (Table 10) or profit (Table 11) per season, rather than considering a static $\theta$ across all seasons (Table 9), for both average and maximum market odds. Profit, once more, tends to maximise on lower thresholds $\theta$ compared to ROI. As an example, Table A1 provides the information used during the betting simulation to assess profitability for 1X2 outcomes, based on average odds of season 2010/11 as shown in Table 10.

The results show that the optimal threshold $\theta$ varies dramatically between seasons, and there is much to

Table 9
Profitability based on average (left) and maximum (right) market odds for 1X2 bets simulated over 13 EPL seasons; from 2006/09 to 2018/19


Table 10
The payoff discrepancies $\theta$ that maximise ROI per season (in yellow shading), based on 1X2 bets and for both average (left) and maximum (right) market odds. The optimal $\theta$ discrepancy is chosen over all $\theta$ that generate at least 30 bets in a single season


be gained by identifying the optimal $\theta$. However, the high variance of $\theta$ suggests that is not reasonable to expect that we will be able to successfully predict the optimal value of $\theta$ before a season starts. Moreover, while the results are restricted to cases with 30 or more bets in a single season, it is clear that in many cases the sample size remains insufficient for deriving reliable and robust single-season conclusions. This
means that the maximised profitability presented in Tables 10 and 11 is not a realistic expectation of realworld performance; only Table 9 is. These results are important because they highlight the danger when optimising models based on the results of a single season (or few seasons), which is often the case in the literature. This outcome is also discussed in Section 6 , point $i v$.

Table 11
The payoff discrepancies $\theta$ that maximise profit per season (in yellow shading), based on $\mathbf{1 X 2}$ bets and for both average (left) and maximum (right) market odds. The optimal $\theta$ discrepancy is chosen over all $\theta$ that generate at least 30 bets in a single season


Table 12
Profitability based on average (left) and maximum (right) market odds for $\mathbf{A H}$ bets simulated over 13 EPL seasons; from 2006/07 to 2018/19


Interestingly, while maximising profit per season is guaranteed to also maximise profit over all seasons (Table 11), the same does not apply to ROI (see

Table 10 and compare it to Table 11). That is, optimising the betting strategy for maximum ROI per season does not necessarily imply that ROI will

Table 13
The payoff discrepancies $\theta$ that maximise ROI per season (in yellow shading), based on $\mathbf{A H}$ bets and for both average (left) and maximum (right) market odds. The optimal $\theta$ discrepancy is chosen over all $\theta$ that generate at least 30 bets in a single season


Table 14
The payoff discrepancies $\theta$ that maximise profit per season (in yellow shading), based on $\mathbf{A H}$ bets and for both average (left) and maximum (right) market odds. The optimal $\theta$ discrepancy is chosen over all $\theta$ that generate at least 30 bets in a single season


maximise across all seasons. Table 10 shows that even though ROI is maximised for each season independently, the overall ROI across all 13 seasons is $9.03 \%$ in the case of average odds, which is notably lower compared to the respective overall ROI of $12.96 \%$ in Table 11. However, this observation does not extend to the case of maximum market odds. This outcome is also discussed in Section 6, point $v i$.

Tables 12, 13, and 14 repeat the analysis of Tables 9, 10, and 11, but for AH rather than 1X2 betting. Table A2 presents an example of the information used during the betting simulation to assess profitability from AH bets, and it is based on average odds of season 2010/11 as shown in Table 13. Overall, the AH bets appear to generate both lower profit as well as ROI compared to 1X2 bets. As with 1X2 bets, optimising for maximum ROI per season

leads to a lower ROI across all seasons, compared to maximising profit. Specifically, Table 13 shows that when maximising ROI per season leads to an overall ROI of $5.7 \%$ for average odds, which is lower than the respective average ROI of $6.33 \%$ in Table 14 when maximising profit. Once more, this observation only applies to the case of average market odds.

An interesting observation is that AH betting generates a lower number of bets when $\theta$ is low, compared to 1 X 2 betting, and a higher number of bets when $\theta$ is high. This suggests that AH betting is less sensitive to the betting decision threshold $\theta$ compared to 1 X 2 betting, for both average and maximum market odds. Furthermore, the optimal threshold $\theta$ for AH bets does not vary as much as it did for 1X2 bets. Despite the relatively low variance of $\theta$ and the common occurrence of winning $60+$ out of 100 AH bets, profitability is still inconsistent between seasons. This is because match bets do not share the same payoff.

### 5.3.1. Odds of bets simulated

When it comes to the bets simulated, the 1X2 bets tend to average odds greater than 3 which suggests that the model tends to recommend bets on outsiders; a behaviour that is consistent with previous studies including the original pi-rating (Constantinou \& Fenton, 2013; Constantinou, 2018). Conversely, the AH bets tend to be simulated on favourite outcomes with average season odds typically ranging between 1.6 and 1.8. However, it is important to note that an issue with the AH odds retrieved from www.footballdata.co.uk is that they do not always represent the odds associated with the handicap that maximises the uniformity of the AH distribution, as discussed in Section 2. For example, the AH odds for seasons 2009/10 and 2010/11 appear to be predominantly based on $\pm 0 \mathrm{AH}$; i.e., no handicap, with the outcome of draw eliminated. Examples of this issue can also be viewed in Table A2; e.g., refer to the imbalanced AH odds for dates 14/08, 11/09 and 27/11.

According to Table 15, at least part of the AH odds of the first five seasons do not reflect the standard AH outcome, whereas the eight most recent seasons appear to be correctly based on the standard AH outcome that aims to make the competition equal. Results from predictive accuracy and profitability suggest that there is no meaningful difference between the first five and the last eight seasons. Therefore, we have no reason to assume that this might have influenced the overall conclusions. Finally, the preference of the model to bet on favourite AH outcomes

Table 15
The mean average and mean maximum AH odds for each of the 13 seasons


remains consistent across all 13 seasons. This outcome is also discussed in Section 6, point ii.

A possible limitation here is that, while the AH market offers multiple handicaps for each match, this study has only considered one handicap per match. However, it is reasonable to assume that the results presented in this paper approximate the overall AH market. This is because when the model suggests a bet on team $X$ for a given handicap, then we should expect the model to suggest a bet on team X regardless the handicap, since any handicap must remain faithful to the expected goal difference of the match, which determines $\theta$.

### 5.3.2. Betting stake adjustments

Figure 5 presents the cumulative profit generated over eight different betting scenarios that represent the combinations of the following betting options: a) optimising for maximum ROI or profit, b) optimising $\theta$ per season or across all seasons, and c) simulating 1 X 2 or AH bets. The results illustrate how the difference in profit and ROI evolves across the 13 seasons between 1X2 and AH bets. While AH bets generate considerably lower profit and ROI, the profitability is much less volatile than 1X2 bets and hence, it is subject to a lower risk of loss which can often be detrimental. For example, note the significant losses for the two best performing scenarios during matches 1900 to 2100, which are both based on 1X2 bets. However, the lower risk of loss also limits profits.

A fairer assessment of risk between 1X2 and AH profits would be to simply optimise stakes such that, at the end of the betting period, they both pro-

![img-4.jpeg](img-4.jpeg)

Fig. 5. Cumulative profit when the betting procedure is optimised for either profit or ROI, overall or per season, and based on either 1X2 or AH maximum market odds. The results are based on 13 EPL seasons; from 2006/09 to 2018/19. Optimisations for overall profit and ROI, across all 13 seasons, are restricted to $\theta$ discrepancies that generate at least 100 bets over those 13 seasons.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Comparing the volatility of profits when the stakes of AH bets is increased by as much required for the cumulative profit to match that of 1 X 2 bets.

duce the same profit. Figure 6 provides these results by extending the scenarios of Fig. 5 to include an additional betting scenario in which AH stakes are increased proportional to the difference in cumulative profit between 1 X 2 and AH bets. For example, in Fig. 6a the new AH betting scenario assumes an increase of 5.59 times the stakes of AH bets, in order for the cumulative profit to become equal to that generated by 1 X 2 bets.

Overall, the graphs suggest that if we want AH bets to generate as much profit as 1 X 2 bets do, then profit from AH bets will likely be subject to a similar risk of loss as with 1X2 bets. Therefore, while AH is often preferred due to the lower variance of returns, this advantage is rather eliminated when we need to bet proportionally larger to match the expected profit produced by the corresponding 1 X 2 bets. This outcome is also discussed in Section 6, point iii.

## 6. Discussion and concluding remarks

This paper presented a model specifically developed for the prediction and assessment of the AH football betting market. The model is based on a modified version of the pi-ratings system which measures the relative scoring ability between teams. The modified pi-ratings are used as an input into a novel BN model that had its graphical structure determined by the temporal assumption Possession $\rightarrow$ Shots $\rightarrow$ Shots on Target $\rightarrow$ Goals scored, which captures the natural causal chain of these events via a Beta-Binomial Hybrid BN modelling process. One example of this assumption is that possession occurs before shots (or shots on target) and hence, shots are assumed to be more impactful than possession in terms of determining goals scored.

Using goal scoring data over the last 27 EPL seasons, the modified pi-ratings discovered a strong linear relationship between team rating difference and expected goal difference. However, the linear relationship is oscillatory (refer to Fig. 3) and this suggests that goal data alone may be insufficient in completely explaining team ability. Future work will investigate whether factors beyond goals scored could better explain this relationship. For example, in (Constantinou \& Fenton, 2017) it was shown that the three teams who were promoted to the EPL, from the English Championship, tend to perform significantly better than the teams they replace. This is an important factor not taken into consideration by the pi-ratings; i.e., the teams are promoted with either an
ignorant rating (if it is their first time in the EPL) or with the rating they had when they were last relegated, which clearly underestimates their performance once they return to the EPL.

AH betting is assessed with reference to the traditional 1X2 betting. The assessment is based on both average and maximum market odds and over all possible betting decision thresholds in terms of discrepancy between predicted and offered market odds. Furthermore, the assessment differentiates between betting strategies that are optimised for ROI and betting strategies that are optimised for profit. Key observations include:
i. The previous literature has generally focused on maximum market odds, and this is understandable since professional gamblers aim to maximise payoff. Still, average odds are important because they reveal the expected returns for the average gambler. Moreover, maximum odds are not attainable by everyone since many countries do not allow access to many of the online bookmakers, including exchangebased websites which often offer the best odds (excluding commission). This study shows that the maximum available market odds increase profits by up to four times relative to average odds. Specifically, taking advantage of the maximum market odds can lead to increased profits that range anywhere between $42 \%$ (refer to overall profits in Table 13) and 296\% (refer to maximised profits in Table 9).
ii. The recommended AH bets tend to be on favourite outcomes with odds that typically average between 1.6 and 1.8 per season. Conversely, the recommended 1X2 bets tend to be on outsider outcomes with odds averaging above 3. The reduction of the problem from a three-state multinomial to a binary distribution (i.e., from 1 X 2 to AH ) explains why the odds move from 1-in-3 to 1-in-2, but not why the recommended bets switch from outsiders to favourites.
iii. AH bets generate lower profit as well as ROI compared to 1X2 bets. Specifically, 1X2 bets are found to generate $\sim 2.5$ to $\sim 5.5$ times higher profit and $\sim 2.5$ to $\sim 4$ times higher ROI compared to AH bets (refer to Fig. 6). For this reason, returns from AH bets tend to be considerably less volatile and subject to a lower risk of loss. While this outcome is in agreement with (Hassanniakalager \& Newall, n.d.), this pre-

sumed advantage of AH betting is flawed. This is because, when the betting stakes of AH bets are increased proportional to the difference in cumulative profit between 1 X 2 and AH bets, the variance of profit from AH bets increases towards the variance of profit from 1 X 2 bets. This implies that, when aiming for the same profit at the end of the same period of time, AH bets are not necessarily less risky than 1X2 bets.
iv. Past studies often focus on a single football season, and profitability tends to be reported based on the betting decision threshold that maximises ROI under the assumption that the optimal betting decision threshold remains invariant between seasons. However, the results in this paper show that the optimal betting decision threshold varies dramatically between seasons, despite predictive accuracy being consistent across the 13 seasons, and this applies to both 1 X 2 and AH bets; albeit to a lower degree for AH bets.

This implies that the profitability presented in Tables 10, 11, 13, and 14 is not a realistic expectation of real-world performance. This is because the optimal betting decision threshold is not consistent between seasons, and the high variance suggest that it is unreasonable to assume we will be able to predict the decision threshold that maximises profit or ROI before a season starts. Therefore, the choice of evaluating football models based on the threshold that maximises profitability in a single football season, which is often the case in the literature, should be discouraged. Moreover, the optimal betting decision threshold is also dependent on whether we would like to maximise ROI or profit. On the other hand, Tables 9 and 12 represent a more realistic expectation of real-world performance, even though it is unlikely that we will follow a static betting decision threshold across these many seasons.
v. Neither profit nor ROI are consistent between seasons, and this applies to both 1 X 2 and AH bets. While the overall performance of the model is good enough to beat the market, it is still possible for the best possible betting decision threshold to be lossmaking for a whole season (see Tables 10, 11, 13, 14). While this is true for average market odds, the risk is eliminated when we consider maximum odds; though some seasons were barely profitable.
vi. Finally, the results show that choosing to optimise for maximum ROI per season will likely produce undesired results in the long term, and this applies to both 1 X 2 and AH bets. On the other hand, choosing to optimise for maximum profit (rather than ROI) per season, not only guarantees that the profit is maximised across all seasons, but also often generates a higher overall ROI, across all seasons, compared to the overall ROI generated when optimising for maximum ROI for each season independently. This finding is important since most of the previous studies focus on maximising ROI, often for individual seasons.

Lastly, it is important to note that this paper has considered football data up to season 2018/19. The two subsequent seasons have been partly affected by the COVID-19 pandemic, where many matches were played with fewer or without fans. Relevant studies have shown that this event had an insignificant or a significant negative effect on home advantage (Wunderlich et al., 2021; McCarrick et al., 2021). The model described in this paper does not to consider this event. However, because the model relies on pi-ratings which involve a home and an away rating for each team, it can be easily adjusted to consider such previously unseen events. For example, if we assume that home advantage is not relevant for a particular match, we could consider assigning the 'away' ratings to both teams for that match. Future research works could investigate whether such modelling modifications, that take into consideration the effect of playing in empty stadiums, improve predictive accuracy.

## Acknowledgments

This research was supported by the ERSRC Fellowship project EP/S001646/1 on Bayesian Artificial Intelligence for Decision Making under Uncertainty, by The Alan Turing Institute in the UK, and by Agena Ltd.

# Appendix A: Sample results from betting simulations 

Table A1
Details of profitability for case in Table 10: Season $=2010 / 11$, Odds $=$ Average, Bets $=1 \mathrm{X} 2$, Optimisation $=$ ROI, and $\theta=10 \%$


Details of profitability for case in Table 13: Season $=2010 / 11$, Odds $=$ Average, Bets $=$ AH, Optimisation $=$ ROI, and $\theta=11 \%$
