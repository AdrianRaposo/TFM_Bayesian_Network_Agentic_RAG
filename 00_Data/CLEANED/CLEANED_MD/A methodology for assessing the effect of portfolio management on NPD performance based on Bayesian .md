![img-0.jpeg](img-0.jpeg)

The University of Manchester

# A methodology for assessing the effect of portfolio management on NPD performance based on Bayesian network scenarios

**DOI:** 10.1111/exsy.12186

## Document Version

Accepted author manuscript

Link to publication record in Manchester Research Explorer

## Citation for published version (APA):

Yang, Y., & Xu, D. (2017). A methodology for assessing the effect of portfolio management on NPD performance based on Bayesian network scenarios. *Expert Systems, 34*(2). https://doi.org/10.1111/exsy.12186

## Published in:

Expert Systems

## Citing this paper

Please note that where the full-text provided on Manchester Research Explorer is the Author Accepted Manuscript or Proof version this may differ from the final Published version. If citing, it is advised that you check and use the publisher's definitive version.

## General rights

Copyright and moral rights for the publications made accessible in the Research Explorer are retained by the authors and/or other copyright owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

## Takedown policy

If you believe that this document breaches copyright please refer to the University of Manchester's Takedown Procedures [http://man.ac.uk/04Y6Bo] or contact uml.scholarlycommunications@manchester.ac.uk providing relevant details, so we can investigate your claim.

![img-1.jpeg](img-1.jpeg)


# A methodology for assessing the effect of portfolio management on NPD performance based on Bayesian network scenarios 

Ying Yang ${ }^{1 *}$ | Dong-Ling Xu ${ }^{2}$

${ }^{1}$ School of Management, Hefei University of Technology, Hefei, China
${ }^{2}$ Manchester Business School, The University of Manchester, Manchester, UK

## Correspondence

Ying Yang, School of Management, Hefei University of Technology, Hefei, 230009, China.
Email: yangying@hfut.edu.cn
Funding Information
European Commission, EC-GPF-314836. China National Nature Science Foundation, 71301040, 71573071, 71202047.

## Abstract

Firm growth and profitability come primarily from new product development. Portfolio management has been emphasized in improving new product development (NPD) performance under multiple project environments. However, few researchers have demonstrated the consequence of different combinations of portfolio management practices on NPD performance. In this study, a decision support methodology based on Bayesian network scenarios is used to simulate the effect of portfolio management on NPD performance in uncertain environments. Firstly, portfolio management factors are identified and performance criteria determined. And then, the causal relationships among the factors are modelled within similar time frames, and a Bayesian network model is developed by parameter learning from data. A case study is carried out for project/portfolio managers in Chinese firms. The most informative factors affecting NPD performance are identified by sensitive analysis, and the best and worst scenarios with different combinations of portfolio management practices are analysed. The study extends the application of Bayesian networks to assess the performance under changing conditions and highlights some managerial suggestions to improve NPD performance.

## KEYWORDS

Bayesian network scenarios, effect assessment, new product development performance, portfolio management practices

Because PM includes a set of multiple interdependent activities which constantly change and develop over time, modelling the relationships between PM practices and NPD performance remains difficult (Jonas et al., 2013). The first evidence of the relationships comes from Cooper et al. (1999). Portfolio management practices and performance of 205 American companies were reported. The findings show that the best company achieved dramatically better portfolio success than the worst. And then, the consequences of portfolio management decisions on NPD performance are examined in marketing simulation exercises conducted with mid-level managers (McNally et al., 2013). The research reveals that the three outcomes of portfolio management decision, including value maximization, balance, and strategic fit, have impact on NPD and firm performance. Meanwhile, the linkages between multiple project portfolio management and NPD performance are modelled by linear regression analysis (Patanakul, 2013). Because linear regression methods have limited capability of measuring performance, there is no clear explanation

about what the consequence of implementing portfolio management in uncertain environments is (de Oliveira, Possamai, Dalla Valentina, \& Flesch, 2012). Moreover, they cannot diagnose the key portfolio management factors which cause low NPD performance.

Bayesian networks (BNs) have been widely applied in the area of both business intelligence and information integration (Duan \& Da Xu, 2012, Chen, 2016, Nonlinear relationships between variables in uncertain environments can be simulated for prediction and diagnosis (Chanda \& Aggarwal, 2016; Chin, Tang, Yang, Wong, \& Wang, 2009; Perkusich, Soares, Almeida, \& Perkusich, 2015). Bayesian learning algorithms can efficiently aggregate the output of members of networks (Chen, 2016; Wang et al., 2010) and handle both nominal and numeric attributes well (Duan \& Da Xu, 2012).

Scenario analysis based on Bayesian networks helps decision makers by estimating future performance by assuming different conditions. Büyüközkan, Kayakutlu, and Karakadılar (2015) used BNs to predict and simulate impacts of lean manufacturing on business performance. De Oliveira et al. (2012) applied BNs to forecast the performance of innovation projects under the consideration of transformational leadership in organizations. Hou, Zhao, Zhao, and Zhang (2016) used dynamic Bayesian networks to predict mobile users' behaviours and locations. A medical decision support system is also developed based on BNs to assess pulmonary infections and to make decisions on severity degree (Zarikas, Papageorgiou, \& Regner, 2015). In this paper, we introduce BN scenarios to analyse the effects of PM practices and provide managerial suggestions to improve NPD performance.

The primary contribution of the study is a decision support methodology to assess the effect of portfolio management on NPD performance. There are many management practice factors which will impact NPD performance. Which practices are key influential factors? How should the complicated relationships among portfolio management practices be modelled? How should the effects of different combinations of portfolio management practices on NPD performance be simulated? The methodology based on BN scenarios presents a transparent model to decision makers for improving NPD performance and helps firms implement portfolio management effectively.

The next section is reserved for the literature review about the effect of portfolio management on NPD and fundamentals of BN scenario analysis. The proposed methodology, including problem structuring, causal modelling, and Bayesian network modelling, is detailed in Section 3. A case study is conducted in Section 4, including sensitivity and scenario analysis. Managerial implications and conclusions are presented in Section 5 and Section 6, respectively.

## 2 | LITERATURE REVIEW

### 2.1 | The effect of portfolio management on new product development performance

Portfolio management is a manifestation of business strategy dealing with issues about investment for the future (Cooper et al., 1999). In a rapidly changing technological and competitive environment, research and development (R\&D) investments are paramount to business
survival and future prosperity. R\&D project portfolio management aims to obtain portfolio success-that is to maximize portfolio value, to align projects with business strategy and to obtain a balanced portfolio with synergies.

First of all, top managers should select and evaluate projects based on their profitability to maximize the value of an R\&D portfolio. A clearly defined and consistently applied portfolio selection and evaluate process can help achieve positive portfolio results (Cooper et al., 1999) and improve NPD performance (Krishnan \& Ulrich, 2001). On the one hand, a well-designed, explicit process provides a platform for managers to communicate and to make effective decisions. New projects or proposals can be evaluated, selected, and prioritized on the platform. Exiting projects may be reprioritized and re-allocated resources according to the decisions. On the other hand, a wellimplemented process may achieve high performance by the usage of PM methods and techniques (Cooper, 1999). Inappropriate projects will be terminated in a timely manner, which will release limited R\&D resources and re-allocate them to important projects (Cooper, 2008). Project termination quality may positively affect the success of portfolios and prevent portfolios from deviating investments into non-strategic projects (Chao, Kavadias, \& Gaimon, 2009). Consequently, new product success rate would be improved (Martinsuo \& Lehtonen, 2007).

Secondly, top managers and project managers are responsible for the strategic fit of an R\&D portfolio in order to implement firm strategies well. Top managers are important decision makers involved in portfolio management. They make NPD project screening, selection, resource allocation and other key decisions (Cooper \& Kleinschmidt, 1995). If top managers actively support portfolio management activities in NPD, they will deliver required decisions timely and communicate with project managers effectively to help them understand firm objectives (Unger, Kock, Gemünden, \& Jonas, 2012). Strong support from top managers is helpful to align projects with business strategy (Luftman, 2004).

Meanwhile, project managers' competency in PM cannot be ignored. They can move business strategy through practices and manage an effective strategic implementation effort (Irani, Kamal, Furlong, \& Al-Karaghouli, 2010). High competency of project managers in the initial stage may link a R\&D project portfolio to firm strategy (Artto \& Dietrich, 2004). A skilful project manager with a clear definition of roles and responsibilities can manage day-to-day activities in portfolio management and deliver high quality projects on time and within budget (Morris \& Jamieson, 2005).Therefore, NPD project performance and net profit would be enhanced.

Finally, synergy is an important objective when managing R\&D portfolios. It is referred to as cross-project coordination. In a portfolio context, synergies include not only technical and market synergy among projects but also cooperation between firms and venders. Generally, project managers focus only on their individual project success. However, a project manager with high competency will participate in strategic decision activities and play vital roles in portfolio management (Zahir Irani, Alsudiri, Al-Karaghouli, \& Eldabi, 2013). If project managers record and deliver reliable project information to other managers in project portfolio management, both synergies and sales growth rate will be achieved effectively (Jonas, Kock, Gemu, \& n, 2013).

In summary, portfolio management practices can be identified with respect to managers and processes. Managers' support and involvement activities in portfolio management process will achieve portfolio success and then enhance NPD performance. Moreover, both the portfolio success, including strategic fit, average project success and synergy, and the NPD performance, such as NPD success rate, net profit, and sales growth rate are influenced by portfolio management activities.

### 2.2 Scenario analysis by Bayesian networks

Scenario analysis is a decision process of analysing possible future events by taking alternative possible outcomes into account. Scenario analysis technique is a tool to tell stories about the future and to explore uncertainties (Stewart, French, \& Rios, 2013). It presents decision makers with several possible future outcomes, such as an optimistic, a pessimistic, or a most likely scenario.

Bayesian networks have been accepted as a scenario analysis technique in systematic reviews (Chai, Liu, \& Ngai, 2013). Variables with probabilities are linked in BNs where Bayes' theorem and related learning algorithms are used to calculate probabilities of future outcome states. It is common to use Bayesian networks to construct scenarios in decision support. Ulengin, Kabak, Onsel, et al. (2010) developed a BN scenario to analyse transportation-environment relationships. Cinicioglu, Önsel, and Ülengin (2012) used BN scenarios for competitiveness analysis of the automotive industry in Turkey. Future scenarios built by BNs are also used in financial loss assessment (Häger \& Andersen, 2010) and stock market analysis (Khorram et al., 2011).

Bayesian networks scenarios have been used for performance analysis in recent years. Li, Rajpal, Sawhney, and Li (2009) is one of the pioneers who used BNs for predicting business performance, assessing the effect of lean manufacturing on firm sustainability. Li, Sawhne, and Wilck (2013) prioritized the efforts of lean six sigma by BN scenarios. Büyüközkan et al. (2015) also constructed BN scenarios to simulate the lean manufacturing effect on business performance. Marco et al. (2012) applied BN scenarios to predict performance of innovation projects. Consequently, the effect of portfolio management on NPD performance can be analysed and predicted by BN scenarios. In this paper, key factors of portfolio management will be identified and scenarios with different combinations of portfolio management practices will be studied below.

## 3 THE PROPOSED METHODOLOGY

### 3.1 Problem structuring

Problem structuring is to identify portfolio management factors and criteria of performance. In this stage, all research variables and criteria in BNs are presented. Because portfolio management is a decisionmaking process involving managers as key players, we identify portfolio management factors from two groups. One is related to processes, including process design and implementation (DI) and project termination; the other is associated with managers, including top management involvement (TMI) and project manager competency. Additionally, two
contextual factors, technology turbulence and market turbulence, which may impact NPD performance will be considered.

Process DI describes how well portfolio management activities are organized and scheduled. A formal and explicit process provides a platform for communication and decision making, which results in transparent and clear decisions and improves the quality of project evaluation and selection (Martinsuo \& Lehtonen, 2007). In a wellimplemented process, all projects in a portfolio will be regularly reviewed.

Project termination is a type of detection decision to re-allocate resources among projects. If initial goals and objectives of a project are not met or some technical issues cannot be resolved, the project would be terminated (Unger et al., 2012). Top managers should dismiss or re-assign the project team, release remaining resources, and accept or reject deliverables. Therefore, effective termination indicates the gain of resources and the control over investments.

Top management involvement refers to a group of top managers who participate in portfolio decision activities (Felekoglu \& Moultrie, 2014). If top managers recognize the importance of PM, they will adopt appropriate methods and implement regular reviews to ensure that a portfolio supports strategic objectives (Cooper et al., 1999).

The competency of project managers has been recognized as an important criterion for project success (Zahir Irani et al., 2013). It refers to the capability, knowledge, and responsibility of project managers in implementing portfolio management.

Additionally, portfolio success may be affected by external environments. It is a challenge for organizations to sustain long-term competitive advantages in turbulent environments (Dayan \& Colak, 2008). Because the turbulence is mainly caused by changes in both new technology and customer preference, we identify two external environment factors including technology turbulence and market turbulence.

Consequently, we select four portfolio management factors and two contextual factors to construct a Bayesian network for assessing their impacts on portfolio success and NPD performance. Strategic fit, average project success, and synergy are used to measure portfolio success and criteria including sales growth rate, net profit, and NPD success rate to measure NPD performance.

### 3.2 Causal modelling within similar time frames

To use Bayesian networks for assessing the effect of portfolio management practices on NPD performance, a directed acyclic graph (DAG), namely a Bayesian causal map, should be initially developed. Causal modelling is to construct a DAG that represents cause-effect relationships among portfolio management factors. Different techniques have been employed to construct a DAG, such as textual analysis (Swan, 1995), soft system approaches (Ülengin, Önsel, Aktas, Kabak, \& Özaydın, 2014), and matrix algebra analytic methods (Büyüközkan et al., 2015). In this study, a Delphi-type group decision-making approach (Ülengin et al., 2014) is used to conceptualize the relationships. Experts from NPD domains were invited to give judgement about the cause-effect relationships between factors and performance criteria.

Firstly, a causal map is initially constructed based on the responses of experts. Some questions are designed based on the

correlation among variables. Ten experts, including academics and top managers from manufacturing, were required to answer these questions about each variable. For example, if there is variable $B$ strongly correlated with variable $A$, a question will be designed as following:

Do you think there exists a direct causal relationship between $A$ and $B$ ? If yes, which is the cause?

All possible causal relationships among variables are incorporated in the causal map. Missing arrows among variables imply conditional independencies, which is critical in making Bayesian inference (Nadkarni \& Shenoy, 2004).

Secondly, causal loops in the causal map are detected and removed within similar time frames. Because an acyclic graphical structure is essential to Bayesian inference, the loops should be eliminated. We check the issues and de-aggregate variables of the loop into twotime frames to solve the problem. For example, there exists a reciprocal causal relationship between strategic fit and NPD success rate, which may be caused by their dynamic relations across multiple time frames. In the first time frame $t_{1}$, the portfolio with high strategic fit tends to be allocated sufficient resources and to achieve a high NPD success rate. Then the high NPD success rate will enhance the strategic fit of the portfolio in a future point of the second time frame F1 $t_{2}$, as shown in Figure 1. We retain one of the two relations and exclude the other from the causal map just as Nadkarni and Shenoy (2001) stated.

Lastly, the causal map is delivered to experts for a final review. For those relationships where there are significant disagreements, specific explanations are presented to reach a final consensus. As a result, the DAG of portfolio management for Bayesian inference is constructed, F2 as shown in Figure 2.

### 3.3 | Bayesian network modelling

The DAG presents only the qualitative relationships among variables. Bayesian network modelling can further quantify the relationships using probability distributions of connected variables. Parameters to be determined in Bayesian networks consist of marginal probabilities and conditional probabilities of variables.

Suppose that there are $N$ variables, $X_{1}, X_{2}, \ldots, X_{N}$, included in the DAG. For a variable $X_{i}$, its set of parents can be denoted by $P a\left(X_{i}\right)$. The joint probability of the network can be presented as follows:

$$
P\left(X_{1}, X_{2}, \ldots, X_{N}\right)=\prod_{i=1}^{N} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

The probabilities of variables can be obtained by a data-based approach that automatically learns the numerical values of the parameters from data (Ulengin et al., 2014). Several learning algorithms have been developed for this purpose, such as the expectationmaximization algorithm and the gradient descent method. Because the expectation-maximization algorithm has been proved a flexible tool for calculating maximum likelihood estimates and more robust than the gradient descent method (Lauritzen, 1995), we used the former to learn parameters for the Bayesian networks.

The objective of parameter learning is to find the most likely network given the data. It includes an expectation (E) step and a maximization (M) step. In the E step, all of the expected values of missing data are computed by using regular inference with the existing BN. In the M step, the BN with maximum likelihood is found using the extended data.

Suppose $N$ is the Bayesian network and $D$ is the data, the learning result is a new network which gives the highest likelihood $P(N \mid D)$. According to Bayes rule,

FIGURE 1 Relationships within two frames
![img-2.jpeg](img-2.jpeg)

FIGURE 2 The directed acyclic graph for portfolio management

$$
P(N \mid D)=P(D \mid N) P(N) / P(D)
$$

Since all the candidate networks have the same $P(D)$, only $P(D \mid N)$ $P(N)$ should be maximized. It can be transformed to maximize its logarithm:

$$
\text { Maximize } \log P(D \mid N)+\log P(N)
$$

When each candidate network has no prior probability, all the networks can be considered equally likely before learning process starts. It means that $\log (P(N))$ is constant. Therefore, the objective of parameter learning is changed to maximize the log likelihood $\log (P(D \mid N))$ (Heckerman, Geiger, \& Chickering, 1995). Suppose the data $D$ consists of $n$ independent cases $d_{1}, d_{2}, \ldots, d n$, then the log likelihood can be expressed as follows:

$$
\begin{aligned}
\log (P(D \mid N)) & =\log (P(d 1 \mid N) P(d 2 \mid N) \ldots P(d n \mid N)) \\
& =\log (P(d 1 \mid N))+\ldots+\log (P(d n \mid N))
\end{aligned}
$$

Because case $d_{j}(j=1,2, \ldots, n)$ is an instance including values for the variables of the BN in a particular situation, the probability of the instance, $\log \left(P\left(d_{j} \mid N\right)\right)$, can be easily calculated using regular inference.

The learning process is iterative and is repeated until the log likelihood numbers no longer improve more than a set tolerance level. After the most likely network is obtained, the conditional probability table of variables in the Bayesian network can be determined.

## 4 | CASE STUDY

## 4.1 | Data collection

The data collection of this study is based on the answers of questionnaires sent to the participants of a survey. We conducted the survey with 169 project/portfolio managers in Chinese firms. Participants are selected from three different management levels: top managers, mid-level managers, and project coordinators in companies. The questionnaire is constituted by 12 variables and corresponding 45 questions to measure them, besides the basic information of participants. The variables and their corresponding questions are as follows:

- PM process design and implementation (five questions)
- Project termination (five questions)
- Top management involvement (seven questions)
- Project manager competency (four questions)
- Technology turbulence (four questions)
- Market turbulence (five questions)
- Strategic fit (four questions)
- Average project performance (four questions)
- Synergy (three questions)
- NPD performance (three questions)

Likert scales from one "strongly disagree" to five "strongly agree" are used to measure a respondent's opinion for questions. Some quesT1 tions are listed in Table 1.

TABLE 1 Some questions for portfolio management factors and performance criteria


With respect to demographic characteristics, the final sample consists of different respondent profiles: top manager (10.1\%), midlevel managers (42\%), and project coordinators (47.9\%). They are mainly from industries of manufacturing (37.3\%), IT service (26.6\%), financial service (6.5\%), R\&D service (10.7\%), construction (5.3\%), real estate (2.4\%), and others (18.9\%). A total of $56 \%$ of them have invested more than $5 \%$ of their sales in research and development, and $58 \%$ have more than 10 projects managed concurrently. A total of $79.3 \%$ of the companies are large and medium sized enterprises, as shown in Table 2.

### 4.2 | Bayesian network construction

We use the commercial software Netica to automate the parameter learning process. The DAG and the data collected from the survey are entered into the software. To facilitate the learning process, the data should be discretised initially. Generally, they are transformed into a form of three states: low, medium, and high (Häger \& Andersen, 2010). Because the values of variables are measured on a 5-point scale, we discretise the variables by dividing the scale into three states equally: $[1,1.7]$ as low, $[1.7,3.4]$ as medium, and $[3.4,5]$ as high (Ülengin et al., 2014).

The parameters of a new BN are then obtained through the learning process. After three iterations when the log likelihood has no change, the probabilities of variables in the BN are determined from the learning process, and the results are shown graphically using bar charts, in Figure 3.

There are a total of 12 variables and 20 causal relationships between variables in the BN. All of the variables have different probabilities in each state based on the causal relationships. Taking the variable project performance for example, there is a probability of $1.46 \%$ that the project performance of the analysed firms is low, while the probability of maintaining a high performance level is $68.7 \%$. Meanwhile, the average level of project performance in the analysed firms is 3.71 , belonging to the high state $[3.4,5]$.

TABLE 2 The sample characteristics


![img-3.jpeg](img-3.jpeg)

FIGURE 3 The Bayesian network for portfolio management The Bayesian network for portfolio management is developed by aggregating expert knowledge to obtain qualitative causal relationships and by learning from data to obtain the quantitative probabilities. It can be used for performance diagnosis or prediction based on different inference processes, such as sensitivity analysis and scenario analysis.

### 4.3 | Sensitivity analysis

Sensitivity analysis is a type of diagnostic inference process. The diagnostic results show how much the belief or mean value of the target node could be influenced by other varying nodes in BNs (Ülengin et al., 2014). To identify the most informative portfolio management factors in crystallizing the states of NPD performance, we analyse all of the criteria of NPD performance in the form of diagnostic inference. Suppose $Q$ is a target variable and $F$ is an independent variable. The degree of sensitivity of $Q$ to $F$ can be described by the variance reduction (or variance explained) $V_{r}$ of the real value of $Q$ (Pearl, 2014):

$$ V_{r}=V(Q)-V(Q) F $$

$V(Q)$ is the variance of the real value of node $Q$ before any new findings, and $V(Q) F)$ is the one after new findings for node $F$.

First, we select NPD success rate as a target node to investigate its key factors. The sensitivity analysis report shows that the most significant factor affecting NPD success rate is strategic fit, which brings a variance reduction of $5.18 \%$. The sensitivity degree of project performance and synergy to NPD success rate are $3.58 \%$ and $1.1 \%$, respectively. Therefore, if a new product portfolio is aligned with business strategy at a high level, the NPD success rate will be increased significantly. Similarly, when the strategic fit is regarded as a target node, the contribution of portfolio management practices to the strategic fit is obtained from the sensitivity analysis (Figure 4).

The important practices are process DI, top management involvement, and project manager competency with the sensitivity degrees of $19.3 \%, 10.1 \%$, and $5.3 \%$, respectively. Hence, process DI is the key factor to strategic fit. This indicates that PM process DI impacts the strategic fit and in turn has a positive impact on the NPD success rate, as shown in Figure 5. An improvement of a portfolio management process can lead to a growth in both strategic fit and NPD success rate.

Secondly, we investigate the second criteria of NPD performance: sales growth rate. The sensitivity analysis results show that the maximum variance reduction is caused by the node synergy (7.9\%). And then, the sensitivity analysis result of synergy presents the contribution of portfolio management practices to it, as shown in Figure 4. Process DI, project manager competency, and project termination contribute to project performance at $14.2 \%, 12.5 \%$, and $11 \%$, respectively. As a result, process DI plays the most important role in improving synergy. An improvement of portfolio management processes not only increases the NPD success rate but also enhances the sales growth rate of firms greatly.

Similarly, contribution factors of net profit can also be analysed. The most significant factor of net profit is project performance,

![img-4.jpeg](img-4.jpeg)

FIGURE 4 Sensitivity analysis of strategic fit and synergy
resulting in a variance reduction of $4.34 \%$. And then, the sensitivity analysis of project performance shows that project termination, project manager competency, process DI, and top management involvement all contribute to project performance at the sensitivity degrees of $14.4 \%, 14 \%, 13.4 \%$, and $8.2 \%$, respectively. As a result, project termination plays the most important role in improving project performance. An increase of project termination quality in portfolio management will greatly improve the net profit of firms.

Finally, we summarize the results of the sensitivity analysis conducted on both the NPD performance level and the portfolio success level. Top management involvement, project manager competency, project termination, and process DI are important factors to NPD performance. The contribution of both the external technology and market environments is not significant to NPD performance. Consequently, we select the four practices of portfolio management to further conduct scenario analysis about the improvement of NPD performance.

### 4.4 Scenario analysis

Scenario analysis can provide valuable insight to anticipate future outcomes by assuming different conditions. It is mainly used to estimate business performance (Büyüközkan et al., 2015), market risk (Groth \& Muntermann, 2011), or failure (Sun \& Shenoy, 2007). The majority of scenario analysis looks at the best options to firm benefits or the worst conditions (Suryani, Chou, Hartono, \& Chen, 2010).

We also develop two scenarios, one optimistic and the other pessimistic, by considering a number of possible events about portfolio management practices and present NPD performance changes under
the scenarios. In the optimistic scenario, all of the portfolio management practices are assumed at high level states. In the pessimistic one, each of the four factors is assumed at a low level. We analyse portfolio success and NPD performance by conducting a predictive inference. And then, the changes on the probability of different states in the BN structure are observed, and the prior and posterior marginal probabilities for the two scenarios are presented, as shown in Table 3. T3 92

The pessimistic scenario is designed so that all portfolio management practices are at a low level. In this case, portfolio management processes are not well designed and implemented, top managers are seldom involved in portfolio management, inappropriate projects cannot be terminated promptly, and project managers have low competency in steering projects. It can be immediately observed that this case leads to a low portfolio management performance with a probability of $33.3 \%$, declining greatly compared with the prior marginal probabilities (Table 3). Obviously, when the situations worsen and the level of portfolio management practices drop to low states in the pessimistic scenario, probability of the NPD success rate, net profit, and sale growth rate all decrease greatly to a low level.

In the optimistic scenario, if the levels of portfolio management practices all increase to high states, there is $60 \%$ chance of having a high NPD success rate, $59.8 \%$ probability of having a high net profit, and $66.6 \%$ probability of having a high sales growth rate. As for PM performance, the probabilities of its three measures all increase much more than the prior marginal probability.

The two scenarios show that the implementation of portfolio management in firms has important effects on NPD performance. Although the optimistic scenario is an idealistic situation that may hardly be implemented, the impressive difference of $21-25 \%$ for

TABLE 3 The prior and posterior marginal probabilities for the two scenarios


NPD performances in high levels between the worst and best case should be given consideration. It indicates that effective portfolio management practices undoubtedly increase NPD performance.

## 5 | MANAGERIAL IMPLICATIONS

The scenario analysis results show that key portfolio management practice should be emphasized when firms hope to improve their NPD performance. Top management involvement, manager competency, portfolio management process DI, and project termination are important practices to firms. These results also align with findings of Jonas et al. (2013), Patanakul (2013), Unger et al. (2012), and Lerch and Spieth (2013).

First, top management involvement plays an important role for improving NPD performance. Top managers should participate in the decision making process of portfolio management and take responsibility for the success of a new product portfolio. They will constitute a favorable culture for portfolio management in multiple project environments (Unger et al., 2012). Moreover, business strategy can be easily conveyed and understood by R\&D members through the communication of top managers. Although there is no direct link between TMI and NPD performance, TMI can directly influence the strategic fit of product portfolios and project performance, which subsequently can impact NPD performance positively.

Second, the competency of project managers is the second important factor to project performance, following top management involvement. It indicates that project managers' knowledge, skills, and experience in portfolio management will impact NPD performance significantly. Just as Patanakul (2013) stated, it is a challenge to manage a project portfolio effectively without the competencies of multitasking and multi-team management. If project managers have the skills to participate in strategy development and to manage effective strategic implementation efforts, NPD performance can be highly improved, especially in a multiple-project organization (Artto \& Dietrich, 2004).

Third, portfolio management process design and implementation are closely related to the strategic fit of new product portfolios and NPD performance. An explicit and flexible process provides a framework to communicate with and to understand each other. Project evaluation and selection decision making are performed transparently with clear rules and procedures (Martinsuo \& Lehtonen, 2007). As a result, NPD projects will be ensured to align with firm strategies by an effective process. Furthermore, a well-designed and well-implemented portfolio management process can stimulate top managers' involvement in new product portfolio management so that sufficient resources can be assigned and portfolio management performance enhanced.

Finally, project termination is essential to align a product portfolio with business strategies. Resources can be released from terminated projects and re-allocated to other prioritized projects. Whether an inappropriate project is promptly detected is related to the implementation of portfolio management processes. Therefore, it is urgent to enhance the implementation quality of the processes in multiple project environments. A strict selection routine and standardized process will lead to transparent decisions and ultimately to detection and abortion of wrong projects (Blichfeldt \& Eskerod, 2008).

## 6 | CONCLUSIONS

With the increasing number of new products concurrently developed, firms are confronted with the challenges of handling project portfolios. Portfolio management performance significantly contributes to NPD performance and firm profitability. Several studies have analysed the influential factors of portfolio management performance based on empirical evidence, such as manager dispositions or management methods. However, portfolio success is also highly dependent on management practices operated by top or mid-level managers. The paper presents the first study that analyses the relationships among portfolio management practices and NPD performance and develops a decision making method to model their causal relationships. We expect that it

can provide an important insight for developing a portfolio management map for top managers.

The proposed method provides a structured approach to the issues related to improving NPD performance through portfolio management. Based on the data collected in a survey of 169 project/ portfolio managers, four main components of portfolio management practices are identified through sensitivity analysis, which includes top management involvement, project manager competency, project termination, and portfolio management process design and implementation. The best and worst scenarios are analysed to provide suggestions for improving NPD performance by different portfolio management practices.

The use of Bayesian networks allows uncertainties in new product portfolio management to be modelled and helps to predict the consequence of management enhancement in practices. It facilitates an in-depth analysis of the causal relationships between portfolio management practices and NPD performance and makes it possible to test and forecast NPD performance in different scenarios.

Future research should focus on how to further map the causal relationships among variables and how to improve the fitness of Bayesian network models. Identifying the causal relationship between variables plays an important role for Bayesian inference. The Bayesian causal map for assessing NPD performance may be further refined by using data mining techniques in addition to expert judgements. Additionally, the intervals adopted to discretise variables are important to model Bayesian networks. How to determine the range values of intervals and how to improve the effectiveness of Bayesian networks are still to be investigated.

## ACKNOWLEDGMENTS

The work described in this paper was substantially supported by the China National Nature Science Foundation under the grant no. 71202047, 71573071 and 71301040, and partially supported by the European Commission under the grant no. EC-GPF-314836 and Alliance Manchester Business School Research Support Found.

# Author Query Form 

## Journal: Expert Systems

## Article: exsy_12186

Dear Author,
During the copyediting of your paper, the following queries arose. Please respond to these by annotating your proofs with the necessary changes/additions.

- If you intend to annotate your proof electronically, please refer to the E-annotation guidelines.
- If you intend to annotate your proof by means of hard-copy mark-up, please use the standard proofing marks. If manually writing corrections on your proof and returning it by fax, do not write too close to the edge of the paper. Please remember that illegible mark-ups may delay publication.
Whether you opt for hard-copy or electronic annotation of your proofs, we recommend that you provide additional clarification of answers to queries by entering your answers on the query sheet, in addition to the text mark-up.



Required software to e-Annotate PDFs: Adobe Acrobat Professional or Adobe Reader (version 7.0 or above). (Note that this document uses screenshots from Adobe Reader X)
The latest version of Acrobat Reader can be downloaded for free at: http://get.adobe.com/uk/reader/
Once you have Acrobat Reader open on your computer, click on the Comment tab at the right of the toolbar:
![img-5.jpeg](img-5.jpeg)

1. Replace (Ins) Tool - for replacing text.

Strikes a line through text and opens up a text box where replacement text can be entered.

## How to use it

- Highlight a word or sentence.
- Click on the Replace (Ins) icon in the Annotations section.
- Type the replacement text into the blue box that appears.
idard framework for the analysis of m icy. Neverthcless, it also led to exogs
le of strateg
ber of com
is that the st
nain compo
level, are exa
important Worilr on entry by oulirc
M henceforthi' we arren the 'hheh

3. Add note to text Tool - for highlighting a section to be changed to bold or italic.

Highlights text in yellow and opens up a text box where comments can be entered.

## How to use it

- Highlight the relevant section of text.
- Click on the Add note to text icon in the Annotations section.
- Type instruction on what should be changed regarding the text into the yellow box that appears.
namic responses of mark ups ent with the VAR evidence
![img-6.jpeg](img-6.jpeg)
2. Strikethrough (Del) Tool - for deleting text.

Strikes a red line through text that is to be deleted.

## How to use it

- Highlight a word or sentence.
- Click on the Strikethrough (Del) icon in the Annotations section.
there is no room for extra profits al (ups are zero and the number of (et) values are not determined by Blanchard and Kiyotaki (1987), rfect competition in general equili ts of aggregate demand and supply lassical framework assuming monol oen an ovommonc number of fime

4. Add sticky note Tool - for making notes at specific points in the text.

Marks a point in the proof where a comment needs to be highlighted.

## How to use it

- Click on the Add sticky note icon in the Annotations section.
- Click at the point in the proof where the comment should be inserted.
- Type the comment into the yellow box that appears.
![img-7.jpeg](img-7.jpeg)

5. Attach File Tool - for inserting large amounts of text or replacement figures.

Inserts an icon linking to the attached file in the appropriate pace in the text.

## How to use it

- Click on the Attach File icon in the Annotations section.
- Click on the proof to where you'd like the attached file to be linked.
- Select the file to be attached from your computer or network.
- Select the colour and type of icon that will appear in the proof. Click OK.

END
![img-8.jpeg](img-8.jpeg)
6. Add stamp Tool - for approving a proof if no corrections are required.

Inserts a selected stamp onto an appropriate place in the proof.

## How to use it

- Click on the Add stamp icon in the Annotations section.
- Select the stamp you want to use. (The Approved stamp is usually available directly in the menu that appears).
- Click on the proof where you'd like the stamp to appear. (Where a proof is to be approved as it is, this would normally be on the first page).

9 the business cycic, starting winn the on perfect competition, constant ret
![img-9.jpeg](img-9.jpeg)
otaki (1987), has introduced produc general equilibrium models with nomin:
![img-10.jpeg](img-10.jpeg)
![img-11.jpeg](img-11.jpeg)

For further information on how to annotate proofs, click on the Help menu to reveal a list of further options:
![img-12.jpeg](img-12.jpeg)