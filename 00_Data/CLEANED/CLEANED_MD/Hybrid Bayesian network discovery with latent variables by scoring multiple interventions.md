# Hybrid Bayesian network discovery with latent variables by scoring multiple interventions 

Kiattikun Chobtham ${ }^{1}$ (D) $\cdot$ Anthony C. Constantinou ${ }^{1}$ ・ Neville K. Kitson ${ }^{1}$<br>Received: 20 December 2021 / Accepted: 25 October 2022 / Published online: 28 November 2022<br>(c) The Author(s) 2022


#### Abstract

In Bayesian Networks (BNs), the direction of edges is crucial for causal reasoning and inference. However, Markov equivalence class considerations mean it is not always possible to establish edge orientations, which is why many BN structure learning algorithms cannot orientate all edges from purely observational data. Moreover, latent confounders can lead to false positive edges. Relatively few methods have been proposed to address these issues. In this work, we present the hybrid mFGS-BS (majority rule and Fast Greedy equivalence Search with Bayesian Scoring) algorithm for structure learning from discrete data that involves an observational data set and one or more interventional data sets. The algorithm assumes causal insufficiency in the presence of latent variables and produces a Partial Ancestral Graph (PAG). Structure learning relies on a hybrid approach and a novel Bayesian scoring paradigm that calculates the posterior probability of each directed edge being added to the learnt graph. Experimental results based on well-known networks of up to 109 variables and 10 k sample size show that mFGS-BS improves structure learning accuracy relative to the state-of-the-art and it is computationally efficient.


Keywords Ancestral graphs $\cdot$ Causal insufficiency $\cdot$ Latent confounders $\cdot$ Structure learning

[^0]
[^0]:    Communicated by Sriraam Natarajan.
    $\boxtimes$ Kiattikun Chobtham
    k.chobtham@qmul.ac.uk
    Anthony C. Constantinou
    a.constantinou@qmul.ac.uk
    Neville K. Kitson
    n.k.kitson@qmul.ac.uk

    1 Bayesian Artificial Intelligence Research Lab, Risk and Information Management (RIM) Research Group, School of Electronic Engineering and Computer Science, Queen Mary University of London (QMUL), London E1 4NS, UK

# 1 Introduction 

A Bayesian Network (BN) is a probabilistic graphical model with a Directed Acyclic Graph (DAG) G where nodes $\mathbf{X}=\left\{\mathrm{X}_{1}, \ldots, \mathrm{X}_{\mathrm{N}}\right\}$ represent random variables and directed edges represent dependencies or causal relationships between variables (Verma and Pearl, 1990). A BN is a generative model that captures the joint probability distribution of the data variables. The dependencies between discrete variables are described via conditional probabilities, such as $\mathrm{P}\left(\mathrm{X}_{\mathrm{i}} \mid\right.$ parent $\left(\mathrm{X}_{\mathrm{i}}\right)$ ) where parent $\left(\mathrm{X}_{\mathrm{i}}\right)$ is the set of parents of node $\mathrm{X}_{\mathrm{i}}$ in the DAG. The joint distribution over all nodes is defined as the product of all conditional probabilities as follows:

$$
\mathrm{P}\left(\mathrm{X}_{1}, \mathrm{X}_{2}, \mathrm{X}_{3}, \ldots \mathrm{X}_{\mathrm{N}}\right)=\prod_{\mathrm{i}=1}^{\mathrm{N}} \mathrm{P}\left(\mathrm{X}_{\mathrm{i}} \mid \operatorname{parent}\left(\mathrm{X}_{\mathrm{i}}\right)\right)
$$

Because directed edges in BNs can often be viewed as causal relationships, BNs offer the potential to go beyond predictive inference by enabling causal reasoning for intervention and counterfactual reasoning. Examples of BNs applied to different areas include medicine (Thornley et al., 2012), sports (Constantinou, 2020), social science (de Waal et al., 2016), finance (Constantinou and Fenton, 1905), geology (Runge et al., 2019), bioinformatics (Sachs et al., 2005) and law (de Zoete et al., 2019). Many of the BNs applied to real-world problems are determined by knowledge, or both knowledge and data (Constantinou et al., 2016). In this paper, however, we focus on the automated discovery of BN structures from data.

Structure learning methods generally fall into two main classes of learning known as score-based and constraint-based learning. The score-based algorithms rely on search methods that explore the search space of graphs and an objective function that scores each graph visited, where the highest scoring graph discovered is returned as the preferred graph. On the other hand, constraint-based learning relies on conditional independence (CI) tests that are used to determine edges and the orientation of some of those edges. Hybrid learning algorithms that combine the two above approaches are often viewed as an additional category of learning. Irrespective of the learning class, BN structure learning represents an NP-hard problem where the number of possible graphs grows super-exponentially with the number of variables. Moreover, large or dense networks tend to require large sample sizes to achieve reasonable structure learning accuracy, and this is a problem because computational complexity increases both with the number of the variables and the sample size.

Learning the structure of a BN involves two more important issues that go beyond computational complexity. Firstly, structures that represent a serial connection $(\mathrm{A} \rightarrow \mathrm{B} \rightarrow \mathrm{C}$ or $\mathrm{A} \leftarrow \mathrm{B} \leftarrow \mathrm{C})$ or a divergence connection $(\mathrm{A} \leftarrow \mathrm{B} \rightarrow \mathrm{C})$ cannot be differentiated by observational data, which means algorithms may fail to orientate these edges. This is because these structures encode the same CI statement $\mathrm{A} \perp \mathrm{C} \mid \mathrm{B}$. Randomly orientating these edges into one of the equivalence structures leads to different DAGs. This set of DAGs is known as a Markov equivalence class and is represented by a Completed Partially DAG (CPDAG). Secondly, data often do not capture all the relevant variables, and learning from data with latent variables is referred

to as learning under the assumption of causal insufficiency. A latent confounder represents a special case of a latent variable where the missing variable is a common cause of two or more observed variables, and this tends to lead to spurious edges between observed variables. Because a DAG is not detailed enough to capture spurious relationships, ancestral graphs have been proposed for this purpose. Specifically, the Maximal Ancestral Graph (MAG) by Richardson and Spirtes (2000) represents an extension of the DAG where directed edges represent parental or ancestral relationships and bidirected edges represent confounding. Moreover, a Partial Ancestral Graph (PAG) represents a set of Markov equivalent MAGs (Spirtes et al., 2001), in the same way that a CPDAG represents a set of Markov equivalent DAGs (Andersson et al., 1997).

Numerous constraint-based algorithms have been proposed to tackle learning under the assumption of causal insufficiency from purely observational data. Wellestablished constraint-based algorithms include the FCI algorithm by Spirtes et al. (2001), and its variants, conservative FCI (cFCI) by Ramsey et al. (2012), majority rule FCI (mFCI) by Colombo and Maathuis (2014), and RFCI by Colombo et al. (2011). The FCI algorithm assumes that the joint probability distribution is a perfect map with a faithful graph, but this assumption is often violated when applying the algorithm to real data. The cFCI, mFCI and RFCI are all FCI-based variants. For example, the RFCI algorithm can be viewed as a faster version of FCI that performs fewer CI tests. Details about the cFCI and mFCI algorithms are provided in Sect. 2.5.

Hybrid algorithms that learn under the assumption of causal insufficiency include CCHM (Chobtham and Constantinou, 2020), $\mathrm{M}^{3} \mathrm{HC}$ (Tsirlis et al., 2018), RFCI-BSC (Jabbari et al., 2017; Jabbari and Cooper 2020) and GFCI (Ogarrio et al., 2016). The CCHM algorithm combines the first and second steps of cFCI with a greedy hillclimbing search similar to $\mathrm{M}^{3} \mathrm{HC}$, and uses causal effects to return a MAG. Both CCHM and $\mathrm{M}^{3} \mathrm{HC}$ assume the data follow a Gaussian distribution. The GFCI algorithm works with both discrete and continuous variables. It combines the score-based FGS (Ramsey, 2015) with the orientation rules in FCI. It starts by obtaining the dependencies from the learnt CPDAG returned by FGS, and performs CI tests on those dependencies to remove potential false positive edges. The result of this process is a skeleton. Finally, orientation rules of FCI are applied to the graph skeleton to produce a PAG. RFCI-BSC is the most relevant algorithm to our work and is discussed in Sect. 2.4.

Structure learning algorithms that learn purely from observational data are restricted to identifying graphs up to Markov equivalence classes. This means interventional data is often required to identify edge orientations, and this can be achieved by comparing post-interventional distributions with pre-interventional distributions. Classic randomised controlled trials (Fisher, 1935) can be viewed as one kind of interventional data that captures treatments and their outcomes. They typically involve randomly assigning patients into two groups, where the so-called treatment group is given the drug being tested, and the control group is given a placebo. If the outcome distribution differs significantly between the two groups, the difference is viewed as the effect of the drug. Pearl (Pearl, 2000) describes this as the difference between "given that we see" (observational data) and "given that we do" (interventional data). Therefore, interventional data can be used in conjunction with observational data to orientate edges that would otherwise remain unoriented.

Algorithms that learn from both observational and interventional data tend to do so from pooled data, which is a method that pools all data sets together with intervened variables specified. These algorithms aim to generate a graph that is consistent, as much as possible, with all input data. Examples include IGSP (Wang et al., 2017) and GIES (Hauser and B¨uhlmann, 2012) that return a DAG from pooled causally sufficient data. Other methods involve determining the results of CI tests from each data set separately and constructing a single graph using conflict resolution strategies. For causally insufficient data, the COmbINE algorithm by Triantafillou and Tsamardinos (2015) implements the cFCI approach to learn the common characteristics and the results of CI tests from different data sets, which it then converts into Boolean Satisfiability (SAT) instances in a MINISAT application to resolve any conflicts. Other algorithms that operate on such results of CI tests include HEJ (Hyttinen et al., 2014) which uses Clingo (Gebser et al., 2011)—an Answer Set Programming (ASP) rule-based declarative programming language that solves various representations of NP-hard optimisation tasks (Gelfond and Lifschitz, 1988; Niemela, 1999)—for conflict resolution. It produces cyclic directed mixed graphs encoding results of CI tests from conditioning and marginalisation operations, and the graphs may contain directed, bidirected or undirected edges. The ACI algorithm (Magliacane et al., 2017) also relies on Clingo and can be viewed as a computationally less expensive variant of HEJ that operates in the search space of ancestral graphs but which does not support bidirected edges for latent confounder representation. Lastly, JCI (Mooij et al., 2020) is a constraint-based algorithm that uses auxiliary context variables and system variables, which the authors define as variables of interest (presumably observed variables) and intervention targets respectively. JCI learns from a pooled data set including knowledge about the relationship between context variables and generates a directed mixed graph, but which does not fall under the ancestral graph family. Table 1 summarises the main features

Table 1 Overview of relevant structure discovery algorithms that assume causal insufficiency and learn graphs from multiple interventions


of these relevant algorithms.
In this paper, we propose a novel hybrid structure learning algorithm called mFGSBS, that produces a PAG from causally insufficient observational data and one or more interventional data sets. The paper is organised as follows: Sect. 2 provides preliminary information, Sect. 3 describes the proposed algorithm, Sect. 4 describes the evaluation process, Sect. 5 presents the empirical results, and we provide concluding remarks and discussions for future work in Sect. 6.

# 2 Preliminaries 

The preliminaries focus on the methods relevant to the mFGS-BS algorithm that we later describe in Sect. 3. Specifically, Sect. 2.1 covers ancestral graphs, Sect. 2.2 covers interventions, Sect. 2.3 covers the BDeu objective function, Sect. 2.4 covers the Bayesian scoring method that assigns probabilities to CI tests, and Sect. 2.5 covers the majority rule from mFCI.

### 2.1 Ancestral graphs

Recall from Sect. 1 that a PAG represents a set of Markov equivalent MAGs, and that a MAG is an extended version of a DAG that represents relationships under the assumption of causal insufficiency. A MAG can contain the following types of edges: $\ldots, \rightarrow$, and $\leftrightarrow$. The undirected edge $\mathrm{A}-\mathrm{B}$ indicates that A is an ancestor of B or a selection variable, and B is an ancestor of A or a selection variable. The selection variable indicates the presence of selection bias in the data set. In this work, we will assume selection bias is not present in the data, and hence the undirected edge will not be present in the MAGs or the PAGs we consider. Further, the directed edge $\mathrm{A} \rightarrow \mathrm{B}$ indicates parental or ancestral relationships, and the bidirected edge $\mathrm{A} \leftrightarrow \mathrm{B}$ refers to the presence of a latent confounder where A and B are related but where neither A is an ancestor of B nor B is an ancestor of A . In a PAG, the variant mark (o) at the endpoint of edges indicates that the endpoint could be a tail $(-)$ or an arrowhead $(>)$ in the equivalence class of MAGs. For example, $\mathrm{o} \rightarrow$ in the PAG indicates that the edge can be either $\leftrightarrow$ or $\rightarrow$ in the equivalent MAGs, whereas o - o indicates that the edge in the equivalent MAGs can be $\rightarrow, \leftarrow$ or $\leftrightarrow$. Both MAGs and PAGs are acyclic graphs and do not allow the existence of almost directed cycles that may occur when $\mathrm{A} \leftrightarrow \mathrm{B}$ is present and B is an ancestor of A (Richardson and Spirtes, 2000). Figure 1 illustrates an example of a DAG with latent variables $\mathrm{L}_{1}$ and $\mathrm{L}_{2}$, along with two examples of Markov equivalent MAGs that represent the conditional independencies between the observed variables in the marginal DAG and the latent variables, and the PAG representing the Markov equivalence class of those MAGs (Chobtham and Constantinou, 2020).

![img-0.jpeg](img-0.jpeg)

Fig. 1 A causal DAG with observed variables $\{\mathrm{V}, \mathrm{W}, \mathrm{X}, \mathrm{Y}, \mathrm{Z}\} \cup$ latent variables $\left\{\mathrm{L}_{1}, \mathrm{~L}_{2}\right\}$ in grey, with two examples of Markov equivalent MAGs, and the Markov equivalent PAG of MAGs

# 2.2 Interventions 

To resolve variant marks in a PAG requires that we look beyond observational data. As discussed in Sect. 1, interventional data can help us orientate some of these edges. Figure 2 illustrates the three different intervention mechanisms by comparing the preintervention and post-intervention actions. Specifically, a Perfect intervention is what Pearl describes as do-calculus (do(X)) where the intervened variable is set to a given state with no uncertainty (Pearl, 2000). A perfect intervention modifies the original causal structure by rendering the intervened variable independent of its causes (also referred to as graph surgery). On the other hand, an Imperfect intervention or a mechanism change (Tian and Pearl, 2001) can be viewed as having external intervention nodes that act like switching parents (I) on an intervened variable X for each external intervention node. Specifically, $\mathrm{I}=1$ activates the intervention where the target node X is parameterised over $\Theta_{\mathrm{X}}^{1}$, whereas when $\mathrm{I}=0$ the intervention is deactivated and target node X is parameterised over $\Theta_{\mathrm{X}}^{0}$ which would imply no external influence on node X. Applications of imperfect intervention are often observed in healthcare studies, where medicine and therapeutic actions often have an imperfect effect in terms of treating symptoms or curing diseases (Rickles, 2009). Lastly, an Uncertain intervention (Eaton and Murphy, 2007) represents the case where an external intervention I has multiple target nodes, or where the intervention on node X comes from more than one intervening route, as opposed to the imperfect intervention that assumes the relationship between intervention nodes and target nodes is one-to-one. Unlike perfect intervention, imperfect and uncertain interventions do not modify the graph and instead manipulate the node parameters.

![img-1.jpeg](img-1.jpeg)

Fig. 2 An illustration of the mechanisms of Perfect, Imperfect, and Uncertain interventions, where the square box represents the target node(s), $\Theta_{X \mid Y}^{0}, \Theta_{Y}^{0}$ are the parameters for nodes $X$ and $Y$ respectively when $I=0$ (representing no intervention), and $\Theta_{X \mid Y}^{1}, \Theta_{Y}^{1}$ are the parameters for nodes $X$ and $Y$ respectively when $\mathrm{I}=1$ (representing an external imperfect or an uncertain intervention)

# 2.3 The Bayesian Dirichlet equivalent uniform (BDeu) score 

Score-based algorithms use an objective function to assess each graph visited in the search space of graphs. The Bayesian Dirichlet equivalent uniform (BDeu) is one of the most commonly used objective functions in structure learning used to identify the maximum a posteriori (MAP) structure. It represents a variant of BD and BDe scores that assumes equivalent uniform priors. Importantly, these are decomposable scores where the total score of the graph represents the sum of the scores assigned to each of its nodes. A decomposable score is important for structure learning because most local scores can be reused, rather than recomputed, when exploring neighbouring graphs. BDeu is also score-equivalent in that it produces the same score for Markov equivalent structures, and hence it is used to search for the DAGs which entail the same joint probability distribution. The BD score was first introduced by Heckerman et al. (1995), under the assumption that the data follow a Dirichlet distribution. Pairing structure learning with BD as the objective function implies that the algorithm is

searching for a DAG G that maximises the posterior probability $\mathrm{P}(\mathrm{G} \mid \mathrm{D})$ given the data D. Structure learning from data can be viewed as an optimisation problem to maximise $\mathrm{P}(\mathrm{G} \mid \mathrm{D}) \propto \mathrm{P}(\mathrm{G}) \mathrm{P}(\mathrm{D} \mid \mathrm{G})$ where the highest posterior probability of a learnt graph $G$ is approximated to the highest log-likelihood score:

$$
\log \mathrm{P}(\mathrm{G} \mid \mathrm{D})=\log \mathrm{P}(\mathrm{G})+\log \mathrm{P}(\mathrm{D} \mid \mathrm{G})
$$

where $\mathrm{P}(\mathrm{G})$ is the prior distribution over all DAGs. Because the search space of DAGs grows super-exponentially with the number of variables, it is impractical to specify informative priors for each DAG. For simplicity, the prior distribution is often taken to be uniform. The BD score can be computed as follows:

$$
\mathrm{P}(\mathrm{D} \mid \mathrm{G})=\prod_{\mathrm{i}=1}^{\mathrm{N}} \prod_{\mathrm{j}=1}^{\mathrm{q}_{\mathrm{i}}}\left[\frac{\Gamma\left(\Sigma_{\mathrm{k}} \alpha_{\mathrm{ijk}}\right)}{\Gamma\left(\Sigma_{\mathrm{k}} \alpha_{\mathrm{ijk}}+\Sigma_{\mathrm{k}} \mathrm{n}_{\mathrm{ijk}}\right)} \prod_{\mathrm{k}=1}^{\left|\mathrm{X}_{\mathrm{i}}\right|} \frac{\Gamma\left(\alpha_{\mathrm{ijk}}+\mathrm{n}_{\mathrm{ijk}}\right)}{\Gamma\left(\alpha_{\mathrm{ijk}}\right)}\right]
$$

where N is the number of variables, $\mathrm{q}_{\mathrm{i}}$ is the number of possible combinations of values of the parents of node $X_{i}$ (it is 1 if there is no parent), $j$ is the index over the combinations of values of the parents of node $X_{i},\left|X_{i}\right|$ is the number of states of node $X_{i}, k$ is the index over the possible values of node $X_{i}, \Gamma$ is the Gamma function, $n_{i j k}$ is the total number of instances in data D where the parents of node $\mathrm{X}_{\mathrm{i}}$ have the $\mathrm{j}^{\text {th }}$ combination of values, and ${ }_{i j}$ is the prior for the equivalent sample size (ess) - also known as the imaginary sample size (iss). The prior parameters are set to $\alpha_{i j k}=\left.\alpha /_{\mid X_{i}}\right|_{q_{i}}$. The study by Silander et al. (2012) suggests that reasonable values for hyperparameter are $\in[1,20]$ where larger values tend to produce denser DAGs. Because the BDeu score is very small, it is preferred to take its log value and its closed form expression is:

$$
\text { BDeu score }=\sum_{\mathrm{i}=1}^{\mathrm{N}} \sum_{\mathrm{j}=1}^{\mathrm{q}_{\mathrm{i}}}\left[\log \frac{\Gamma\left(\alpha / \mathrm{q}_{\mathrm{i}}\right)}{\Gamma\left(\alpha / \mathrm{q}_{\mathrm{i}}+\Sigma_{\mathrm{k}} \mathrm{n}_{\mathrm{ijk}}\right)}+\sum_{\mathrm{k}=1}^{\left|\mathrm{X}_{\mathrm{i}}\right|} \log \frac{\Gamma\left(\alpha /_{\mid X_{i}} \mid q_{i}+n_{i j k}\right)}{\Gamma\left(\alpha /_{\mid X_{i}} \mid q_{i}\right)}\right]
$$

BN structure learning represents an NP-hard problem, which means that searching over all possible graphs is intractable. One solution to this problem is the use of heuristics such as Greedy search, but these approaches will often get stuck in a local optimum solution. Other score-based solutions include exact learning which guarantee to return the highest scoring graph, but these are restricted to a relatively small set of variables and are out of the score of this paper. BDeu is established as one of the most commonly used objective functions in hybrid and score-based structure learning, and algorithms such as the hybrid GFCI and RFCI-BSC, as well as score-based Greedy Equivalent Search (GES) (Chickering, 2003), including its more efficient variant Fast Greedy equivalent Search (FGS) (Ramsey, 2015), use BDeu to greedily traverse the search space of graphs.

# 2.4 Assigning probabilities to conditional independence tests and directed edges 

Previous works that assumed prior probabilities for the existence of directed edges, as opposed to a binary outcome, include those by Castelo and Siebes (2000) who

introduced the idea of assigning subjective prior probabilities (specified by experts) to directed edges, and by Scutari (2017) who assumed the marginal uniform prior probabilities of directed edges $\mathrm{A} \rightarrow \mathrm{B}$ and $\mathrm{A} \leftarrow \mathrm{B}$ to be $1 / 4$, while the prior probability of the independency between A and B to be $1 / 2$ in a variant of the BD score called the Bayesian Dirichlet sparse score (BDs).

Hyttinen et al. (2014) proposed a Bayesian scoring method that applies prior probabilistic weights to the results obtained from CI tests. These prior probabilities are subjective and obtained from knowledge. In this paper, we modify this method so that the prior probabilities are objectively calculated from data, and are assigned to directed edges rather than to the results obtained from CI tests. These details are discussed in Sects. 3.1 and 3.2. With reference to the method by Hyttinen et al. (2014), the posterior probability of $\mathrm{CI}\left(\mathrm{P}\left(\mathrm{r} \mid \mathrm{D}_{\mathrm{OBS}}\right)\right)$, given observational data, is:

$$
\mathrm{P}\left(\mathrm{r} \mid \mathrm{D}_{\mathrm{OBS}}\right)=\frac{\text { prior } \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{r}\right)}{\text { prior } \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{r}\right)+(1-\text { prior }) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \bar{r}\right)}
$$

where r is an arbitrary CI that A and B are independent given $\mathrm{Z}(\mathrm{A} \perp \mathrm{B} \mid \mathrm{Z}), \overline{\mathrm{r}}$ is an arbitrary conditional dependence that A and B are dependent given $\mathbf{Z}(\mathrm{A} \not \mathrm{B} \mid \mathrm{Z}), \mathbf{Z}$ is the set of variables that is the separation set (Sepset) of variables A and B , prior is an informative or uninformative probability from knowledge that $\mathrm{A} \perp \mathrm{B} \mid \mathrm{Z}$ is true, P $\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{r}\right)$ is the network score of $\mathrm{A} \perp \mathrm{B} \mid \mathrm{Z}$ (marginal likelihood), and $\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \overline{\mathrm{r}}\right)$ is the network score of $\mathrm{A} \not \mathrm{B} \mid \mathrm{Z}(\mathrm{A} \rightarrow \mathrm{B}$ or $\mathrm{A} \leftarrow \mathrm{B})$.

Similarly, Jabarri et al. (2017) used the BDeu score to obtain a posterior probability for CI in the hybrid RFCI-BSC algorithm, and assumed a uniform prior as the uninformative probability for each result obtained from CI tests as follows:

$$
\mathrm{P}\left(\mathrm{r} \mid \mathrm{D}_{\mathrm{OBS}}\right)=\frac{\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{r}\right)}{\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{r}\right)+\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \overline{\mathrm{r}}\right)}
$$

where $\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{r}\right)$ is the BDeu score (marginal likelihood) of structure $\mathrm{A} \leftarrow \mathrm{Z} \rightarrow \mathrm{B}$ $(\mathrm{A} \perp \mathrm{B} \mid \mathrm{Z})$, and $\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \overline{\mathrm{r}}\right)$ is the BDeu score of structure $\mathrm{A} \leftarrow \mathrm{Z} \rightarrow \mathrm{B}$ and $\mathrm{A} \rightarrow$ $\mathrm{B}(\mathrm{A} \not \mathrm{B} \mid \mathrm{Z})$, and all variables in Z are parents of both A and B . These structures are proposed by Jabarri et al. $(2017 ; 2020)$ to be the representation of all possible structures that correspond to the relevant CI tests. Since the marginal likelihoods can be found in the objective scores computed by score-based learning (Margaritis, 2005), the BDeu score of these structures can be used to derive the marginal likelihoods for discrete variables. The RFCI-BSC algorithm learns a structure from discrete observational data under the assumption of causal insufficiency. Moreover, it generates multiple PAGs by sampling over the joint posterior probabilities of CI, and picks the PAG with the highest joint posterior probability of CI. Since the decision for CI is determined with a random threshold, this makes the output of the algorithm nondeterministic. Empirical experiments show that RFCI-BSC fails to generate results for input data with sample size 10 k or higher (Constantinou et al., 2021).

# 2.5 Majority rule FCI 

Recall from Sect. 1 that cFCI and mFCI are constraint-based algorithms and both represent extensions of FCI that improve edge orientation accuracy. cFCI is similar to cPC (Ramsey et al., 2012), where cPC does not (and cFCI does) assume causal insufficiency. In this paper, we also implement the majority rule from mFCI , in addition to the Bayesian scoring method described in Sect. 2.4 to compute the prior probabilities of directed edges, to determine the likelihood of an unshielded triple being a v-structure (details will be in Sect. 3.2.2).

Compared to FCI, cFCI performs additional CI tests on A and C given on all subsets of all neighbours of A and C including B , for each unshielded triple A-B-C, to more conservatively determine v -structures and orientate edges. This implies that cFCI discovers fewer, although with higher certainty, directed edges compared to FCI. For discrete data, the $\mathrm{G}^{2}$ test can be used as the statistical test for determining CI between A and C conditional on B :

$$
\mathrm{G}^{2}=2 \sum_{\mathrm{a}, \mathrm{c}, \mathrm{~b}} \mathrm{n}_{\mathrm{acb}} \ln \frac{\mathrm{n}_{\mathrm{acb}} \mathrm{n}_{\mathrm{b}}}{\mathrm{n}_{\mathrm{ab}} \mathrm{n}_{\mathrm{cb}}}
$$

where $n_{a c b}$ is the total number of instances in data which $A=a, B=b$ and $C=c$. The calculation of the total number of instances of $n_{a b}, n_{c b}$ and $n_{b}$ is analogous to that of $\mathrm{n}_{\mathrm{acb}}$. A p-value associated with each statistical test result is then used to reject or accept CI, where a cut-off threshold of 0.05 is generally used establishing independence. For each unshielded triple A-B-C in the v-structure phase, the conservative rule from cFCI classifies each unshielded triple as either a definite v-structure, a definite non v-structure, or an ambiguous triple given the Sepsets, e.g. if B is not in any Sepsets A and C, the conservative rule will classify the unshielded triple A-B-C as a definite v-structure. Later, Colombo and Maathuis (2014) found that the conservative rule was orientating few of the v-structures and proposed the majority rule which can be viewed as the relaxed version of the conservative rule. They called this new variant the majority rule FCI (mFCI). Specifically, in mFCI , the majority rule classifies each unshielded triple A-B-C as:
a. A v-structure if B is in less than $50 \%$ of the Sepsets of A and C,
b. A non v-structure if B is in more than $50 \%$ of the Sepsets of A and C,
c. An ambiguous triple if B is in $50 \%$ of the Sepsets of A and C.

## 3 The mFGS-BS algorithm

Recall from Sect. 2 that both the score-based and constraint-based algorithms covered in this paper produce a graph in the Markov equivalence class. This means that not all edges can be orientated given observational data, and only a few of the algorithms in the literature consider both observational and interventional data in an attempt to orientate as many edges as possible.

The mFGS-BS algorithm described in this section learns a PAG from both observational and interventional data, under the assumption of causal insufficiency and that

the intervened variables are subject to perfect intervention. The novelty of mFGS-BS involves assigning probabilities to each possible directed edge. If the two opposing directions between a pair of variables both have probabilities that are higher than a given threshold, then a bidirected edge is assumed.

We first describe in Sect. 3.1 how the probabilities of directed edges from a single observational data set can be obtained, and then describe in Sect. 3.2 how we extend this concept to cases in which we want to learn a structure from both observational and interventional data. Sect. 3.3 provides the overall description of mFGS-BS.

# 3.1 Determining the probabilities of directed edges from a single observational data set 

We devise a new method to determine directed edges that is largely based on the methods of Hyttinen et al. (2014) and Jabbari et al. (2017) that focus on assigning probabilities to each result obtained from CI tests, which we previously covered in Sect. 2.4. For the rest of this paper, we label observational data as $\mathrm{D}_{\mathrm{OBS}}$ and interventional data as $\mathrm{D}_{\mathrm{INT}}$. When assuming the unconditional independence between two variables A and B, we modify Eq. (2) to consider the possibility of edges A B (i.e. no edge between A and B), $\mathrm{A} \rightarrow \mathrm{B}$ and $\mathrm{A} \leftarrow \mathrm{B}$ in a DAG as follows:

$$
\mathrm{P}\left(\mathrm{AB} \mid \mathrm{D}_{\mathrm{OBS}}\right)=\frac{\mathrm{P}(\mathrm{AB}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{AB}\right)}{\mathrm{P}(\mathrm{AB}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{AB}\right)+\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \rightarrow \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \leftarrow \mathrm{~B}\right)}
$$

Since $\mathrm{P}\left(\mathrm{AB} \mid \mathrm{D}_{\mathrm{OBS}}\right)+\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}})+\mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)=1$ and $\mathrm{P}(\mathrm{AB})+$ $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})+\mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})=1$, then:

$$
\begin{gathered}
1-\left(\mathrm{P}\left(\mathrm{~A} \rightarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{OBS}}\right)+\mathrm{P}\left(\mathrm{~A} \leftarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{OBS}}\right)\right)= \\
\frac{(1-(\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})+\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}))) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{AB}\right)}{(1-(\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})+\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}))) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{AB}\right)+\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \rightarrow \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \leftarrow \mathrm{B}\right)} \\
\text { where } \mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B}) \text { is the prior probability of directed edge } \mathrm{A} \rightarrow \mathrm{B}, \mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}) \text { is } \\
\text { the prior probability of directed edge } \mathrm{A} \leftarrow \mathrm{~B} \text { that we later describe in Sect. 3.2, P } \\
\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \rightarrow \mathrm{~B}\right) \text { is the BDeu score of structure } \mathrm{A} \rightarrow \mathrm{~B}, \text { and } \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \leftarrow \mathrm{~B}\right) \text { is the }
\end{gathered}
$$

where $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})$ is the prior probability of directed edge $\mathrm{A} \rightarrow \mathrm{B}, \mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})$ is the prior probability of directed edge $\mathrm{A} \leftarrow \mathrm{B}$ that we later describe in Sect. 3.2, P $\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \rightarrow \mathrm{B}\right)$ is the BDeu score of structure $\mathrm{A} \rightarrow \mathrm{B}$, and $\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \leftarrow \mathrm{B}\right)$ is the BDeu score of structure $\mathrm{A} \leftarrow \mathrm{B}$.

Because we assume that the learnt ancestral graph is a PAG that may contain bidirected edges, the bidirected edge $\mathrm{A} \leftrightarrow \mathrm{B}$ corresponds to the dependency between A and B from the assumed true structure $\mathrm{A} \leftarrow \mathrm{L} \rightarrow \mathrm{B}$ (A $\&$ B) where L is a latent confounder. The dependency between A and B in a PAG can be $\mathrm{A} \rightarrow \mathrm{B}, \mathrm{A} \leftarrow \mathrm{B}$ or $\mathrm{A} \leftrightarrow \mathrm{B}$. Because Eq. (3) is not suitable to calculate the posterior probabilities of these types of edges, we devise two equations: (1) calculating $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)$ by ignoring $\mathrm{A} \leftarrow \mathrm{B}$, as described in Case 1 below, and (2) calculating $\mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)$ by ignoring $\mathrm{A} \rightarrow \mathrm{B}$, as described in Case 2 below. These enable us to calculate the probabilities of each of these directed edges independently. If the posterior probabilities of both directed edges $\mathrm{A} \rightarrow \mathrm{B}$ and $\mathrm{A} \leftarrow \mathrm{B}$ are higher than a given threshold, then mFGS-BS

is not be able to orientate the given directed edges and will produce the bidirected edge $\mathrm{A} \leftrightarrow \mathrm{B}$.

Case 1 Calculate $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)$ given the assumption that $\mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)=0$, $\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \leftarrow \mathrm{B}\right)=0$ and $\mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})=0$ from Eq. (3), then:

$$
\begin{aligned}
& 1-\mathrm{P}\left(\mathrm{~A} \rightarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{OBS}}\right) \\
& =\frac{(1-\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)}{(1-\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \rightarrow \mathrm{~B}\right)}
\end{aligned}
$$

Case 2 Calculate $\mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)$ given the assumption that $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)=0$, $\mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \rightarrow \mathrm{B}\right)=0$ and $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})=0$ from Eq. (3), then:

$$
\begin{aligned}
& 1-\mathrm{P}\left(\mathrm{~A} \leftarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{OBS}}\right) \\
& =\frac{(1-\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)}{(1-\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \leftarrow \mathrm{~B}\right)}
\end{aligned}
$$

From this, we define the posterior probabilities of directed edges as specified by Definition 1.

Definition 1 Assuming the learnt graph is a PAG, we define a bidirected edge $\mathrm{A} \leftrightarrow \mathrm{B}$ as the dependency between A and B derived from the possibility of both $\mathrm{A} \rightarrow \mathrm{B}$ and $\mathrm{A} \leftarrow \mathrm{B}$, where the posterior probabilities $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)$ and $\mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{OBS}}\right)$ are:

$$
\begin{aligned}
& \mathrm{P}\left(\mathrm{~A} \rightarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{OBS}}\right) \\
& =1-\frac{(1-\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)}{(1-\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \rightarrow \mathrm{~B}\right)} \\
& \mathrm{P}\left(\mathrm{~A} \leftarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{OBS}}\right) \\
& =1-\frac{(1-\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)}{(1-\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{OBS}} \mid \mathrm{A} \leftarrow \mathrm{~B}\right)}
\end{aligned}
$$

# 3.2 Determining the probabilities of directed edges from both observational and interventional data sets 

We extend the approach above to learn from an observational data set and one or more interventional data sets, which the algorithm processes in turn. For each interventional data set, $I N T_{i}$, the algorithm uses Eqs. (4) and (5) to determine the posterior probability of each directed edge. We use the term "posterior" here to reflect the fact that this probability, denoted for example, $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{INT}_{i}}\right)$, is based both on the current interventional data set being processed and all previous data sets processed.

$$
\begin{aligned}
& \mathrm{P}\left(\mathrm{~A} \rightarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{INT}_{\mathrm{i}}}\right) \\
& =1-\frac{(1-\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{INT}_{\mathrm{i}}} \mid \mathrm{A} \mathrm{~B}\right)}{(1-\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{INT}_{\mathrm{i}}} \mid \mathrm{A} \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{INT}_{\mathrm{i}}} \mid \mathrm{A} \rightarrow \mathrm{~B}\right)} \\
& \mathrm{P}\left(\mathrm{~A} \leftarrow \mathrm{~B} \mid \mathrm{D}_{\mathrm{INT}_{\mathrm{i}}}\right) \\
& =1-\frac{(1-\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{INT}_{\mathrm{i}}} \mid \mathrm{A} \mathrm{~B}\right)}{(1-\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B})) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{INT}_{\mathrm{i}}} \mid \mathrm{A} \mathrm{~B}\right)+\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B}) \times \mathrm{P}\left(\mathrm{D}_{\mathrm{INT}_{\mathrm{i}}} \mid \mathrm{A} \leftarrow \mathrm{~B}\right)}
\end{aligned}
$$

The term $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})$ on the right hand side of Eq. (4) represents the objective prior probability of directed edge $\mathrm{A} \rightarrow \mathrm{B}$ based on the previously processed data sets. The term $\mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})$ plays an analogous role as the objective prior for $\mathrm{A} \leftarrow \mathrm{B}$ in Eq. (5). The prior for $\mathrm{A} \rightarrow \mathrm{B}$ is taken to be either the posterior for that directed edge computed in the previous iteration, that is, $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B} \mid \mathrm{D}_{\mathrm{INT}_{\mathrm{i}-1}}\right)$, or a prior derived using Eq. (6) whichever is the larger.

$$
\begin{aligned}
\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})= & \max \left\{\mathrm{P}_{\mathrm{FGS}}(\mathrm{~A} \rightarrow \mathrm{~B}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: \mathrm{i}-1}}, \mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})_{\mathrm{A} \rightarrow \mathrm{~B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}\right\} \\
& +\sum_{\mathrm{k}=1}^{\mathrm{i}-1} \mathrm{P}(\mathrm{~A}-\mathrm{B})_{\text {local BDeu of B, target }=\mathrm{A}} \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{\mathrm{k}}}
\end{aligned}
$$

where $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})$ is computed from three factors on the right hand side of Eq. (6):

- Factor 1: $\mathrm{P}_{\mathrm{FGS}}(\mathrm{A} \rightarrow \mathrm{B}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: \mathrm{i}-1}}$ is the probability of directed edge $\mathrm{A} \rightarrow \mathrm{B}$ over all previously learnt CPDAGs from FGS across $\mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: \mathrm{i}-1}}$ (further details are provided in Sect. 3.2.1).
- Factor 2: $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}$ is the probability of directed edge $\mathrm{A} \rightarrow \mathrm{B}$ calculated from the ratio of Sepsets determining v-structure $\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}$ using the majority rule from $\mathrm{D}_{\mathrm{OBS}}$ (further details are provided in Sect. 3.2.2).
- Factor 3: $\sum_{\mathrm{k}=1}^{\mathrm{i}-1} \mathrm{P}(\mathrm{A}-\mathrm{B})_{\text {local BDeu of B, target }=\mathrm{A}} \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{\mathrm{k}}}$ is the summation of all relative changes in the local BDeu scores of node B compared to $\mathrm{D}_{\mathrm{OBS}}$, when the intervened variable is A across all previously learnt $\mathrm{D}_{\mathrm{INT}}$. The relative changes in the local BDeu scores are described in Sect. 3.2.3.


# 3.2.1 Factor 1: Determining the probabilities of directed edges given the occurrence rates of each directed edge over all learnt CPDAGs 

The first, out of the three, factors used to calculate the prior probability of a directed edge is based on the occurrence rate of each directed edge derived from the probability of directed edge $\mathrm{A} \rightarrow \mathrm{B}\left(\mathrm{P}_{\mathrm{FGS}}(\mathrm{A} \rightarrow \mathrm{B}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: \mathrm{i}-1}}\right)$ over all learnt CPDAGs obtained by applying FGS to each input data set. Specifically,:

$$
\begin{aligned}
& \mathrm{P}_{\mathrm{FGS}}(\mathrm{~A} \rightarrow \mathrm{~B}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: i-1}} \\
& \quad=\frac{\text { \#directed edge }(\mathrm{A} \rightarrow \mathrm{~B})}{\text { \#total directed edge }(\mathrm{A} \rightarrow \mathrm{~B})+\text { \#total directed edge }(\mathrm{A} \leftarrow \mathrm{~B})}
\end{aligned}
$$

where:

$$
\begin{aligned}
& \text { directed edge }(A \rightarrow B) \\
& \quad=\left\{\begin{array}{l}
1 \quad: \text { if } A \rightarrow B \text { is in a learnt CPDAG } \\
0.5: \text { if } A-B \text { is in a learnt CPDAG and the intervened variable }=A \\
0 \quad: \text { otherwise }
\end{array}\right.
\end{aligned}
$$

and:

$$
\begin{aligned}
& \text { total directed edge }(A \rightarrow B) \\
& \quad=\left\{\begin{array}{l}
1: \text { if } A \rightarrow B \text { is in a learnt CPDAG } \\
1: \text { if } A-B \text { is in a learnt CPDAG and the intervened variable }=A \\
0: \text { otherwise }
\end{array}\right.
\end{aligned}
$$

The total number of directed edges $\mathrm{A} \rightarrow \mathrm{B}$ represents the number of directed edges $\mathrm{A} \rightarrow \mathrm{B}$ present in each of the learnt CPDAGs. Note that CPDAGs learnt from interventional data should not produce directed edges entering the intervened variable due to the graph surgery mechanisms illustrated in Fig. 2 (i.e., interventions are rendered independent of their parents). For example, if the undirected edge $\mathrm{A}-\mathrm{B}$ is present in the learnt CPDAG when we intervene on node A , the algorithm assigns probability 0 for directed edge $\mathrm{A} \leftarrow \mathrm{B}$ and probability 0.5 for directed edge $\mathrm{A} \rightarrow \mathrm{B}$ to account for the risk of false positive edges learnt by FGS, since it does not produce bidirected edges in the presence of latent confounders (Ogarrio et al., 2016).

It is important to clarify that in the absence of intervention, an undirected edge in the learnt CPDAG does not imply equal probability for either direction (Kummerfeld, 2021). The correct probability for each directed edge can be obtained by enumerating all possible DAGs from the learnt CPDAG. However, this tends to increase the computational complexity of the algorithm substantially, especially in the case of mFGS-BS which is designed to produce a CPDAG for each input data set. For simplicity and reasons of efficiency, when an undirected edge is present in a learnt CPDAG, mFGS-BS assumes a probability of 0.5 for either direction.

# 3.2.2 Factor 2: Determining the probabilities of directed edges given the ratios of Sepsets determining v-structures 

Because the joint probability distribution from interventional data will not capture all dependencies, we consider the v-structures as determined by observational data. Therefore, interventional data is not used by this factor. In mFCI, the v-structures are obtained from unshielded triples that are part of an initial undirected graph determined by statistical CI tests. Then, the majority rule in mFCI is used to definitively orientate the edges of unshielded triples A-B-C into v-structures $\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}$, determined by the ratio of Sepsets (Colombo and Maathuis, 2014). In this paper, we use a novel method to instead calculate the probabilities of these directed edges,

where $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}$ and $\mathrm{P}(\mathrm{C} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}$ correspond to the individual probabilities of directed edges $\mathrm{A} \rightarrow \mathrm{B}$ and $\mathrm{C} \rightarrow \mathrm{B}$ in producing v-structure $\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}$ given the observational data. In order to assign a probability to directed edges in an unshielded triple A-B-C, mFGS-BS considers how many of the Sepsets of A and C contain B. If B is in less than $50 \%$ of the Sepsets of A and C (i.e., the ratio of Sepsets $<0.5$ ) then we assume that B does not block an active path between A and C . Hence, the likelihood of v -structure $\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}$ will be higher than 0.5 , and from this we deduce that $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}>0.5$ and $\mathrm{P}(\mathrm{C} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}>$ 0.5 . Conversely, if B is in $\geq 50 \%$ of the Sepsets of A and C , we deduce that the unshielded triple A-B-C is unlikely to be a v-structure and that instead is likely to be either $\mathrm{A} \rightarrow \mathrm{B} \rightarrow \mathrm{C}, \mathrm{A} \leftarrow \mathrm{B} \rightarrow \mathrm{C}$ or $\mathrm{A} \leftarrow \mathrm{B} \leftarrow \mathrm{C}$. These assumptions lead to Eq. (7) and (8) which are calculated independently as follows:

$$
\begin{gathered}
\mathrm{P}(\mathrm{~A} \rightarrow \mathrm{~B})_{\mathrm{A} \rightarrow \mathrm{~B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}=\mathrm{P}(\mathrm{C} \rightarrow \mathrm{~B})_{\mathrm{A} \rightarrow \mathrm{~B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}} \\
=\left\{\begin{array}{ll}
1-\text { the ratio of Sepset : the ratio of Sepset } 0.5 \\
0.5 & : \text { the ratio of Sepset } \geq 0.5
\end{array}\right. \\
\mathrm{P}(\mathrm{~A} \leftarrow \mathrm{~B})_{\mathrm{A} \rightarrow \mathrm{~B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}=\mathrm{P}(\mathrm{C} \leftarrow \mathrm{~B})_{\mathrm{A} \rightarrow \mathrm{~B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}=0.5
\end{gathered}
$$

where the ratio of Sepsets $=\frac{\mid \text { Sepsets of } \mathrm{A} \text { and } \mathrm{C} \text { which contain } \mathrm{B} \mid}{\text { all Sepsets of } \mathrm{A} \text { and } \mathrm{C} \text { । }}$, |Sepsets of A and C which contain B| and |all Sepsets of A and C| represent the number of Sepsets in $\mathrm{D}_{\mathrm{OBS}} \cdot \mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}, \mathrm{P}(\mathrm{C} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}$ from Eq. (7), $\mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}$ and $\mathrm{P}(\mathrm{C} \leftarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B} \leftarrow \mathrm{C}} \mid \mathrm{D}_{\mathrm{OBS}}$ from Eq. (8) are assigned the value of 0.5 for the reasons covered in Sect. 3.2.1.

# 3.2.3 Factor 3: Determining the probability of directed edges given the relative changes in local BDeu scores 

From Eq. (1), we know the BDeu score of a graph represents the summation of all local BDeu scores assigned to each node within that graph. The local BDeu score for node $\mathrm{i}\left(\mathrm{Z}_{\mathrm{i}}\right)$ (Cussens, 2012) is denoted as:

$$
\mathrm{Z}_{\mathrm{i}}=\sum_{\mathrm{j}=1}^{\mathrm{q}_{\mathrm{i}}}\left[\log \frac{\Gamma\left(/ \mathrm{q}_{\mathrm{i}}\right)}{\Gamma\left(/ \mathrm{q}_{\mathrm{i}}+\Sigma_{\mathrm{k}} \mathrm{n}_{\mathrm{ijk}}\right)}+\sum_{\mathrm{k}=1}^{\left|\mathrm{X}_{\mathrm{i}}\right|} \log \frac{\Gamma\left(/ \mid \mathrm{X}_{\mathrm{i}} \mid \mathrm{q}_{\mathrm{i}}+\mathrm{n}_{\mathrm{ijk}}\right)}{\Gamma\left(/ \mid \mathrm{X}_{\mathrm{i}} \mid \mathrm{q}_{\mathrm{i}}\right)}\right]
$$

The effect of an intervention represents the difference between pre and postintervention distributions of the children of a target node (Zhang, 2006). We consider the difference in their local BDeu scores to represent the effect of the intervention, assuming the sample size of the input observational data is the same with the sample size of the interventional data when computing this difference. From this, we obtain the relative change in the local BDeu scores as described by Definition 2.

Definition 2 Assuming equal sample size for both observational and interventional data, the relative change in the local BDeu scores between pre-intervention $\left(\mathrm{Z}_{\mathrm{i}} \mid \mathrm{D}_{\mathrm{OBS}}\right)$

and post-intervention $\left(Z_{i} \mid D_{I N T}\right)$ of node $i$ is:

$$
\left|\frac{\mathrm{Z}_{\mathrm{i}}\left|\mathrm{D}_{\mathrm{OBS}}-\mathrm{Z}_{\mathrm{i}}\right| \mathrm{D}_{\mathrm{INT}}}{\mathrm{Z}_{\mathrm{i}} \mid \mathrm{D}_{\mathrm{OBS}}}\right|
$$

For example, when we intervene on node A when $\mathrm{A} \rightarrow \mathrm{B}$ is present in the graph, then we would expect the effect of this intervention to be reflected in the probability distribution of B . When A is the intervened variable and the undirected edge $\mathrm{A}-\mathrm{B}$ is learnt by FGS given $\mathrm{D}_{\mathrm{INT}}$, we are interested in the likelihood of the directed edge $\mathrm{A} \rightarrow \mathrm{B}$ being present in the true graph. In this case, the probability of directed edge $\mathrm{A} \rightarrow \mathrm{B}$ is measured by Factor 3 in terms of the relative change in the local BDeu score of node B , given $\mathrm{D}_{\mathrm{INT}}$ and $\mathrm{D}_{\mathrm{OBS}}$, as defined by Eq. (9).

Example 1 This example is described with reference to Fig. 3, and assumes that the true DAG is the one shown in Fig. 1. Figure 3a shows the undirected graph as constructed by the CI tests given $\mathrm{D}_{\mathrm{OBS}}$, to determine unshielded triples. Figure 3b, c and d present the three hypothetical CPDAGs learnt by FGS from three different data sets. We first illustrate how to derive Factor 2 in Table 2, where the first column shows that the CI tests over V and Y , given the unshielded triple $\mathrm{V}-\mathrm{X}-\mathrm{Y}$ in Fig. 3a, return 3 Sepsets with p -values greater than the cut-off threshold of 0.05 . The only Sepset of node V and Y that contains X is $\{\mathrm{W}, \mathrm{X}, \mathrm{Z}\}$. This means that the ratio of Sepsets in determining the given v-structure will be 0.333 , as shown in the second column in Table 2. The third and fourth columns show how we arrive at the calculation of Factor 2, given Eqs. (7)
![img-2.jpeg](img-2.jpeg)

Fig. 3 a The undirected graph produced by the CI tests given $\mathrm{D}_{\mathrm{OBS}}, \mathbf{b}-\mathbf{d}$ and the three CPDAGs learnt by FGS from observational and interventional data $\left(\mathrm{D}_{\mathrm{OBS}}, \mathrm{D}_{\mathrm{INT}_{1}}\right.$ and $\left.\mathrm{D}_{\mathrm{INT}_{2}}\right)$ generated based on the DAG shown in Fig. 1, with variables targeted for intervention $\mathrm{T}_{1}=\{\mathrm{V}\}, \mathrm{T}_{2}=\{\mathrm{W}\}$ shown in rectangles


![img-5.jpeg](img-5.jpeg)


and (8) respectively, each of which corresponds to a probability of the directed edge being present in the true graph.

Table 3 illustrates how Factor 3 is calculated, that produces the relative change in the local BDeu scores as described in Sect. 3.2.3. The example is based on one observational data set, two interventional data sets, and one intervened variable per interventional data set as shown in Fig. 3c and d. Figure 3c shows that the undirected edge $\mathrm{V}-\mathrm{X}$ is learnt by FGS given $\mathrm{D}_{\mathrm{INT}_{1}}$. When V is the intervened variable, we observe that the relative change in the local BDeu score of node X is 0.0119 from the effect of this intervention, so this increases the probability of directed edge $\mathrm{V} \rightarrow \mathrm{X}$ being present in the true graph. Table 3 also shows the relative changes in the local BDeu score of V and Z are 0.0174 and 0.0001 respectively when W is the intervened variable in Fig. 3d.

Finally, Table 4 presents the outputs produced by each of the three factors, and with reference to the directed edges presented in the first column. The calculations in the second, third and fourth columns correspond to the outputs of Factors 1, 2 and 3 respectively. In calculating Factor 1 for directed edge $\mathrm{X} \rightarrow \mathrm{Y}$, Fig. 3b, c and d show that $\mathrm{X} \leftarrow \mathrm{Y}$ appears once and $\mathrm{X} \rightarrow \mathrm{Y}$ appears twice across the three CPDAGs, thus $\mathrm{P}_{\mathrm{FGS}}(\mathrm{X} \rightarrow \mathrm{Y}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: 2}}=0.67$. For directed edge $\mathrm{W} \rightarrow \mathrm{V}$, Fig. 3b shows $\mathrm{W}-\mathrm{V}$, Fig. 3c shows no edge, and Fig. 3d shows $\mathrm{W}-\mathrm{V}$ given $\mathrm{D}_{\mathrm{INT}_{2}}$ and hence, $\mathrm{P}_{\mathrm{FGS}}(\mathrm{V} \rightarrow \mathrm{W}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: 2}}$ is set to 0 and $\mathrm{P}_{\mathrm{FGS}}(\mathrm{W} \rightarrow \mathrm{V}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: 2}}$ to 0.5 . This is because W is the intervened variable in Fig. 3d, and from this we can conclude that if an edge is discovered between V and W , then the direction of that edge can only be entering V . Note that $\mathrm{P}_{\mathrm{FGS}}(\mathrm{W} \rightarrow \mathrm{V}) \mid \mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1: 2}}$ is set to 0.5 and not to 1 because FGS suggests $\mathrm{W}-\mathrm{V}$ instead of $\mathrm{W} \rightarrow \mathrm{V}$. Finally, the fifth column of Table 4 shows the overall calculation for the prior probability of each directed edge, that takes into consideration all three factors, given Eq. (6).

# 3.3 Algorithm mFGS-BS 

We now use the concepts described in Sects. 3.1 and 3.2 to formulate the mFGS-BS algorithm. The pseudocode of mFGS-BS is provided in Algorithm 1. The algorithm takes as an input an observational data set and one or more interventional data sets, the set of variables targeted for intervention for each interventional data, and the hyperparameters specified in Algorithm 1. The overall process of mFGS-BS is shown in Fig. 4. The first step in Algorithm 1 performs CI tests given an observational data set. Steps 2 to 4 derive the initial prior probabilities of directed edges forming vstructures and the probabilities of directed edges learnt by FGS given an observational data set. Step 5 then iteratively calculates the posterior probabilities of directed edges derived from each interventional data set, as described in Sect. 3.2. In the last steps, a PAG is constructed from the posterior probabilities of directed edges obtained after processing the last interventional data set, based on a hyperparameter cut-off threshold c a directed edge or bidirected edge.


Table 4 Examples of the calculation of the prior probability of directed edges with reference to Example 1, Fig. 3, Tables 2 and 3


Algorithm 1: mFGS-BS (majority rule and Fast Greedy equivalent Search with Bayesian Scoring)
Input: interventional data sets $\mathrm{D}_{\mathrm{INT}_{1}}$, an observational data $\mathrm{D}_{\mathrm{OBS}}$, intervened variable sets $\Upsilon_{t}$, significance threshold $t$, posterior probability cut-off threshold c, maximum Sepset size k
Output: a PAG
Step 1 Set up a complete undirected graph $\mathcal{U}$ and Sepset $\mathbf{Z}$ size $=0$
Repeat
Remove the dependencies for each pair $(A, B)$ in $\mathcal{U}$ if they become independent given subsets of
Sepset $\mathbf{Z}$, determined by significance threshold $t$ in $D_{\text {OBS }}$
Sepset $\mathbf{Z}$ size $=$ Sepset $\mathbf{Z}$ size +1
Until Sepset $\mathbf{Z}$ size k has been tested
Step 2 Given unshielded triple $A-B-C$ from $\mathcal{U}$ resulting from Step 1, perform CI tests, with significance threshold $t$, on $A$ and $C$ given all neighbours of $A$ and $C$ including $B$, given $D_{O B S}$ and calculate Factor 2 $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B}-\mathrm{C}}\left[\mathrm{D}_{\mathrm{OBS}}, \mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B}-\mathrm{C}}\right] \mathrm{D}_{\mathrm{OBS}}, \mathrm{P}(\mathrm{C} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B}-\mathrm{C}}\left[\mathrm{D}_{\mathrm{OBS}}\right.$ and $\left.\mathrm{P}(\mathrm{C} \leftarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B}-\mathrm{C}}\right] \mathrm{D}_{\mathrm{OBS}}$ according to Equations (7) and (8)
Step 3 Run FGS on $\mathrm{D}_{\mathrm{OBS}}$ and add the learnt CPDAG to the list $\mathcal{L}_{G}$
Step 4 For each pair $(A, B)$ over all variables
Calculate the prior probabilities $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B}), \mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})$ for each possible directed edge $\mathrm{A} \rightarrow \mathrm{B}, \mathrm{A} \leftarrow \mathrm{B}$ where $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})=\max \left\{\mathrm{P}_{\mathrm{FGS}}(\mathrm{A} \rightarrow \mathrm{B})\left[\mathrm{D}_{\mathrm{OBS}}, \mathrm{P}(\mathrm{A} \rightarrow \mathrm{B})_{\mathrm{A} \rightarrow \mathrm{B}-\mathrm{C}}\right] \mathrm{D}_{\mathrm{OBS}}\right\}$
Calculate the posterior probabilities $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{1}}\right), \mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{2}}\right)\right.\right.$ for each possible directed edge $\mathrm{A} \rightarrow \mathrm{B}, \mathrm{A} \leftarrow \mathrm{B}$ according to Equations (4) and (5)
End for
Step 5 For i=1 to I-1
Run FGS on $\mathrm{D}_{\mathrm{INT}_{1}}$ and add the learnt CPDAG to the list $\mathcal{L}_{G}$
For each pair $(A, B)$ over all variables
If $A$ is the intervened variable
Calculate Factor $3 \mathrm{P}(\mathrm{A}-\mathrm{B})_{\text {local BDeu of B,target }=\mathrm{A}}\left[\mathrm{D}_{\mathrm{OBS}, \mathrm{INT}_{1}}\right.$ given Equation (9) and add it to the list $\mathcal{L}_{S}$
End if
Calculate the prior probabilities $\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B}), \mathrm{P}(\mathrm{A} \leftarrow \mathrm{B})$ for each possible directed edge $\mathrm{A} \rightarrow \mathrm{B}$ and $\mathrm{A} \leftarrow \mathrm{B}$ given Equation (6), where Factor 1 is calculated given $\mathcal{L}_{G}$, Factor 2 is calculated given Equations (7) and (8) in Step 2, and Factor 3 is calculated given $\mathcal{L}_{S}$
$\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B}) \leftarrow \max \left\{\mathrm{P}(\mathrm{A} \rightarrow \mathrm{B}), \mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{2}}\right)\right]\right.$
$\mathrm{P}(\mathrm{A} \leftarrow \mathrm{B}) \leftarrow \max \left\{\mathrm{P}(\mathrm{A} \leftarrow \mathrm{B}), \mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{2}}\right)\right]\right.$
Calculate the posterior probabilities $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{1+1}}\right), \mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{1+1}}\right)\right.\right.$ for each possible directed edge $\mathrm{A} \rightarrow \mathrm{B}, \mathrm{A} \leftarrow \mathrm{B}$ according to Equations (4) and (5)
End for
End for
Step 6 Repeat until no cycles or an almost cyclic are present in the output graph
For each pair $(A, B)$ in all variables
Select edge $\mathrm{A} \rightarrow \mathrm{B}$ if the posterior probability $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{1}}\right)\right.$ is higher than threshold c ;
Select edge $\mathrm{A} \leftrightarrow \mathrm{B}$ if the posterior probabilities $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{2}}\right)\right.$ and $\mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{3}}\right)$ are both higher than threshold c ;
Select edge A o- o B if the posterior probabilities $\mathrm{P}\left(\mathrm{A} \rightarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{3}}\right)\right.$ and $\mathrm{P}\left(\mathrm{A} \leftarrow \mathrm{B}\left[\mathrm{D}_{\mathrm{INT}_{4}}\right)$ are both lower or equal to threshold c , but $\mathrm{A}-\mathrm{B}$ exists in $\mathcal{U}$.
End for
If the graph contains a cycle or an almost cyclic
Remove an edge that causes a cycle, or an almost cycle, where the edge selected is the one that has the lowest posterior probability.
End If
End
Step 7 Output a PAG by combining the set of edges learnt from Step 6

# 4 Case studies, data simulation and evaluation 

We consider six networks that greatly vary in dimensionality. All six case studies are based on real networks constructed by experts and are taken from the literature. These are: (a) Asia which is a small network that captures the relationships between a visit to Asia, tuberculosis and lung cancer (Lauritzen and Spiegelhalter, 1988), (b)

![img-8.jpeg](img-8.jpeg)

Fig. 4 The overall process of the mFGS-BS algorithm that iteratively processes data sets and calculates posterior probabilities of directed edges to generate a PAG

Table 5 The properties of the six real-world networks considered for evaluation


Sports which is a small network that measures the effect of possession in football matches, on shots generated and goals scored (Constantinou et al., 2020), (c) Property which is a medium-size network for investment decision making in the UK property market (Constantinou et al., 2020), (d) Alarm which is a medium-size network of an alarm notification system for patients (Beinlich et al., 1989), (e) ForMed which is a large network modelling the risk of violent reoffending in mentally ill prisoners (Constantinou et al., 2020), and (f) Pathfinder which is a very large network for diagnosis of lymph-node diseases (Heckerman et al., 1992). The properties of these six networks are provided in Table 5.

We use the networks to generate one observational and up to 10 interventional data sets. The true MAGs and true DAGs for each of the networks are available in the Bayesys repository (Constantinou et al., 2020). For each true DAG, we consider observational and interventional data sets over two sample sizes $(\mathrm{n}=1 \mathrm{k}$ and $\mathrm{n}=10 \mathrm{k})$. Interventional data are generated using the bnlearn R package (Scutari, 2019). For each data set, we randomly choose one or five variables to be targeted for intervention. This means it is possible for the same variable is targeted for intervention in more than one interventional data set. We remove all incoming edges entering intervened variables, and we assume a uniform distribution for each state of variables targeted for intervention, before the intervention is set, as in (Korb et al., 2004). Finally, 10\% of the variables in the smaller networks (Asia and Sports) and 5\% of the variables in the larger networks (Property, Alarm, Formed and Pathfinder) are made latent.

The structure learning performance is evaluated using the graphical measures of Precision, Recall, F1 and the Balance Scoring Function (BSF). The F1 score ranges from 0 to 1 , and represents the harmonic mean of Precision and Recall, calculated as follows: $\mathrm{F} 1=2 \times\left(\frac{\text { Precision } \times \text { Recall }}{\text { Precision }+ \text { Recall }}\right)$. The BSF score (Constantinou, 2020) considers all four confusion matrix parameters (TP, TN, FP and FN) to return a balanced score $\mathrm{BSF}=0.5 \times\left(\frac{\mathrm{TP}}{\mathrm{a}}+\frac{\mathrm{TN}}{\mathrm{i}}-\frac{\mathrm{FP}}{\mathrm{i}}-\frac{\mathrm{FN}}{\mathrm{a}}\right)$, where a is the number of edges in the true MAG, i is the number of independencies in the true $\mathrm{MAG}, \mathrm{i}=\frac{\mathrm{N}(\mathrm{N}-1)}{2}-\mathrm{a}$, and N is the number of variables. The BSF score ranges from -1 to 1 , where 1 corresponds to a perfect match between learnt and true graphs, 0 represents a score equivalent to that obtained from an ignorant empty or a fully connected graph, and -1 corresponds to the worst possible mismatch. To minimise uncertainty, we repeat the experiments five times per algorithm and obtain the average scores.

We compare the graphical scores obtained by mFGS-BS to those obtained by COmbINE, RFCI-BSC and GFCI, which are three similar algorithms that also produce a PAG. RFCI-BSC assigns probabilities to CIs that are used to learn a PAG, which is the most similar approach to mFGS-BS, whilst the well-establish GFCI supports latent variables and has been shown to more accurate than FCI and RFCI (Ogarrio et al., 2016). An important difference amongst these algorithms is that COmbINE enables learning from multiple interventional data sets while RFCI-BSC and GFCI do not. RFCI-BSC and GFCI are hybrid algorithms which assume the input data are observational. We therefore combined the observational and interventional data sets into a single data set, which we used as an input to these algorithms. This serves as a baseline experiment where the RFCI-BSC and GFCI algorithms produce a result given all data, but without taking advantage of interventional information.

COmbINE was tested using the MATLAB implementation by Triantafillou (2016) while RFCI-BSC and GFCI were tested using the rcausal package, which is the R wrapper for Tetrad Library (Wongchokprasitti, 2019). Note the output of COmbINE represents a special type of PAG that contains dashed edges (--) indicating uncertainty about the existence of an edge learnt from each interventional data set. Since we are interested in the direction of causation, all output PAGs are measured against the ground truth MAG using the penalty scores described in Table 6. Regarding the hyperparameter inputs of the algorithms, the significant threshold for the G-square hypothesis test is set to 0.05 , and the max Sepset size of the conditioning set is set to 10 , in all algorithms. The posterior probability cut-off threshold of mFGS-BS is set to 0.5 , and the default ess of BDeu in mFGS-BS, RFCI-BSC and GFCI is set to 1. We also apply a runtime limit of four hours to each graph learnt/experiment for all algorithms.

# 5 Empirical results 

The results are separated into four subsections. We start with Sect. 5.1, where we measure the sensitivity to the order of interventional data sets, we use the Alarm network to generate 5 and 10 interventional data sets with sample sizes 1 k and 10 k by intervening on a random single variable per data set and $5 \%$ of the variables in the

Table 6 The edge and orientation penalty scores used by the scoring metrics, where $\rightarrow$ represents one of the output edges of COmbINE


data are made latent. Then, we randomise 20 orderings of 5 and 10 interventional data sets, and evaluate the results. In Sect. 5.2, we assess the impact of each of the three factors described in Sect. 3.2.2 on graphical learning accuracy. Sect. 5.3 compares the results of mFGS-BS to those of the other algorithms when we intervene on a single variable per interventional data set, and Sect. 5.4 when we intervene on five variables per interventional data set.

# 5.1 Assessing the sensitivity of the ordering of interventional data sets 

The mFGS-BS algorithm updates the posterior probabilities of directed edges by taking into consideration a single interventional data set at a time. In this subsection, we evaluate how this ordering might influence the graphical performance of the algorithm. This experiment involves the different combinations of 5 and 10 interventional data sets, and sample sizes 1 k and 10 k . The boxplot in Fig. 5 shows the BSF and F1 scores of mFGS-BS when applied to each hyperparameter setting involving the Alarm network.
![img-9.jpeg](img-9.jpeg)

Fig. 5 The boxplots show the BSF and F1 scores of mFGS-BS from 20 random interventional data orderings generated from the Alarm network, assuming one intervened variable and $5 \%$ latent variables per data set, over two sample sizes and two numbers of interventional data sets. The boxplots report the average values (the symbol x in the box) along with the median (the middle line of the box), and the maximum and minimum scores (the whiskers of the box)

Each of the four scenarios involves 20 randomised orderings of interventional data. The results show that the average BSF score is $0.73 \pm 0.0363$ when we have 5 interventional data sets at 1 k sample size each, and the variability decreases to $0.81 \pm 0.0058$ for 10 interventional data sets at 10 sample size each. We observe that the average F1 scores are mostly consistent with the BSF scores. Both the BSF and F1 scores show that there is a minor deviation in the scores obtained from structure learning, depending on the ordering of interventional data sets, and the standard deviation decreases with the number and size of the interventional data sets.

# 5.2 Assessing the impact of Factors 1, 2, and 3, described in Sect. 3.2 

We assess the impact of the three factors described in Sect. 3.2 by modifying Eq. (6) to consider one, or combinations of two, factors at a time. As shown in Table 7, mFGSBS-1 refers to considering Factor 1 only, mFGS-BS-23 considers Factors 2 and 3, etc. The impact is measured in terms of graphical accuracy, based on the metrics Precision, Recall, F1 and BSF shown in Table 7. The experiments are based on the Alarm network and assume $5 \%$ latent variables (one latent variable in this case), and sample sizes 1 k and 10 k .

The results in Table 7 depict the average learning performance over 10 experiments, from considering just one interventional data set to considering 10 interventional data sets. We repeat these experiments five times, and each time we randomly choose a new variable to be targeted for intervention. Considering one factor alone, the results clearly show considerable drop in performance across almost all cases. Combinations of two factors increase performance, particularly when Factor 3 is included in the combination. Although Factor 1 appears to be less important than Factors 2 and 3, considering all three factors (i.e., the default mFGS-BS) does lead to a slightly better overall performance across all combinations.

### 5.3 Results based on one variable targeted for intervention per interventional data set

In this subsection, we assume that each interventional data contains a single variable that is randomly targeted for intervention. Because RFCI-BSC failed to generate a PAG for almost all cases in which the sample size is 10 k , we restrict its comparisons to experiments where the sample size is up to 1 k . Figure 6 shows the results obtained by applying the algorithms to the Asia network over two sample sizes. The x -axis represents the total number of interventional data sets considered for learning, and the y -axis represents the specified scoring metric, runtime, or the number of edges learnt. Each data point in these graphs represents the average result across five iterations. Each iteration involves new data sets and new variables targeted for intervention. The results show that mFGS-BS outperforms GFCI and RFCI-BSC, and to a lesser degree COmbINE which demonstrates erratic performance, across all four metrics and two sample sizes. Importantly, the results show that both mFGS-BS and COmbINE continue to improve with the number of interventional data sets. Conversely, the graphical accuracy of GFCI and RFCI-BSC decreases with the number of interventional data

Table 7 The impact of Factors 1, 2 and 3 (refer to Sect. 3.2) on graphical performance, where mFGS-BS considers all of the three factors (default version), mFGS-BS-1 considers Factor 1 only, mFGS-BS-12 considers Factors 1 and 2 only, etc. The results represent average performance over multiple experiments with synthetic Alarm network data, as described in Sect. 5.2


The best performance values are shown in bold

![img-10.jpeg](img-10.jpeg)

Fig. 6 Average performance of the algorithms when applied to synthetic data generated from the Asia network, assuming one intervened variable and $10 \%$ latent variables per data set, over two sample sizes
sets, and this is expected since these two algorithms used pooled data, where the postinterventional and pre-interventional distributions may conflict. Lastly, COmbINE is found to be considerably faster than both mFGS-BS and GFCI at 10 k sample size.

Figure 7 repeats the results for the Sports network, which is also a small network. However, compared to Asia, the Sports network contains a considerably higher number of free parameters. Overall, the results show that the algorithms deliver a rather similar performance when the number of data sets is low, with the gap in performance increasing as the number of data sets increases. The accuracy of mFGS-BS increases faster with the number of data sets, and this eventually makes the gap in performance important at higher number of data sets. Interestingly, while COmbINE is the fastest algorithm on Asia, it is the slowest on Sports. A possible explanation is the number of free parameters, which is 1,049 in Sports compared to just 18 in Asia, despite the two

![img-11.jpeg](img-11.jpeg)

Fig. 7 Average performance of the algorithms when applied to synthetic data generated from the Sports network, assuming one intervened variable and $10 \%$ latent variables per data set, over two sample sizes
networks having just one variable difference. This suggests that COmbINE might not scale well with dense networks, or with networks that contain multinomial rather than Boolean variables, whereas RFCI-BSC fails to return an output and instead returns an out-of-memory error. Lastly, GFCI produces a high number of learnt edges, and this number continues to increase with the number of data sets and greatly surpasses the number of true edges.

Table 8 summarises the average results across all experiments in which a single variable is targeted for intervention. The results show that mFGS-BS performed best in the small and medium networks and across all four scoring metrics, followed by COmbINE, then GFCI and finally RFCI-BSC. In terms of runtime, however, GFCI is found to be the fastest algorithm in most experiments, followed by mFGS-BS, then


Table 8 (continued)


The best performance values are shown in bold

COmbINE, and finally RFCI-BSC which could not process any of the larger networks within the runtime limit.

Figures 8 and 9 repeat the results for the medium networks Alarm and Property respectively. While there are some variations in the results, the overall conclusions that can be derived from these results are consistent with those derived from the smaller networks of Asia and Sports. A notable exception is that COmbINE performs better than mFGS-BS, in terms of BSF and recall, in Property. However, this result is restricted to the sample size of 10 k , and this is because COmbINE fails to generate a result within the four-hour runtime limit for sample size 1 k and RFCI-BSC fails to return a result when the experiments rely on more than two interventional data sets. Because COmbINE does not return a result for any of these larger networks within the four-hour time limit, we shown these results in the Appendix (see Figs. 12 and
![img-12.jpeg](img-12.jpeg)

Fig. 8 Average performance of the algorithms when applied to synthetic data generated from the Alarm network, assuming one intervened variable and $5 \%$ latent variables per data set, over two sample sizes

![img-13.jpeg](img-13.jpeg)

Fig. 9 Average performance of the algorithms when applied to synthetic data generated from the Property network, assuming one intervened variable and $5 \%$ latent variables per data set, over two sample sizes
13). Overall, the larger networks show that GFCI outperforms mFGS-BS slightly in ForMed, perhaps because any differences between the observational and interventional data with just one intervened node is relatively minor in this larger network. mFGS-BS outperforms GFCI considerably in Pathfinder in terms of graphical accuracy. Pathfinder is the network with the highest number of free parameters considered in this study, and this complexity might explain why all algorithms perform relatively poorly on Pathfinder compared to the other networks.

# 5.4 Results based on five variables targeted for intervention per interventional data set 

This subsection focuses on the results when the number of intervened variables is increased from one (the results in Sect. 5.3) to five, for each interventional data.

Because the Asia and Sports networks contain less than 10 variables, we do not consider them here since it would be unrealistic to assume that half of the network variables are targeted for intervention. Instead, we consider the networks of Property, Alarm, ForMed and Pathfinder where the number of variables ranges from 27 to 109.

Figure 10 presents the results based on the Property network and shows that both mFGS-BS and COmbINE improve their performance relative to the corresponding results in Fig. 9 which consider only one intervened variable. Table 9, which summarises the average results obtained when considering five intervened variables, shows that mFGS-BS performs best across all metrics at 1 k sample size, whereas COmbINE performs best across all metrics at 10 k sample size for the Property network. However, as shown in Fig. 10, the runtime of COmbINE increases much faster with the number
![img-14.jpeg](img-14.jpeg)

Fig. 10 Average performance of the algorithms when applied to synthetic data generated from the Property network, assuming five intervened variables and $5 \%$ latent variables per data set, over two sample sizes. The runtime of COmbINE at 1 k sample size is not shown in the charts, because its runtime is much higher

Table 9 Average performance across all experiments in which five variables are targeted for intervention per data set, where M indicates out-of-memory error, and T indicates failure to complete learning within the four-hour runtime limit


Table 9 (continued)


The best performance values are shown in bold

of data sets, and fails to generate any results within the four-hour runtime limit when the number of data sets is three or more. RFCI-BSC, on the other hand, returned an out-of-memory error when applied to these data sets. Therefore, the average results reported in Table 9 may underestimate the performance of COmbINE and RFCI-BSC for sample size 1 k , since the average is derived solely by focusing on a lower number of data sets on which the performance tends to be worse.

Figure 11 repeats the results for the Alarm network. As before, COmbINE failed to produce a result for all experiments within the four-hour time limit. However, the results of COmbINE this time extend up to six interventional data sets and enable us to draw reasonably confident conclusions. mFGS-BS performs best overall and across almost all the different number of data sets and sample sizes. Both mFGS-BS and
![img-15.jpeg](img-15.jpeg)

Fig. 11 Average performance of the algorithms when applied to synthetic data generated from the Alarm network, assuming five intervened variables and $5 \%$ latent variables per data set, over two sample sizes

COmbINE perform better compared to the case of a single intervened variable, and continue to improve with the number of data sets, whereas GFCI and RFCI-BSC do not.

For the large and very large networks, COmbINE and RFCI-BSC fail to produce any results. On the other hand, both mFGS-BS and GFCI are able to generate results for all experiments across both sample sizes. The experimental results obtained from ForMed and Pathfinder case studies can be found in the Appendix (Figs. 14 and 15). Note that, in the case of these larger networks, five intervened variables represent a relatively low number. Still, as shown in Table 9, mFGS-BS performs considerably better than GFCI and RFCI-BSC across almost all experiments. The only case in which GFCI performs slightly better than mFGS-BS is for ForMed at 1 k sample size, where GFCI averages scores of 0.58 and 0.59 for BSF and Recall respectively, whereas mFGS-BS averages scores of 0.57 for both metrics. On the other hand, the cases in which mFGS-BS outperforms GFCI involve much higher discrepancies in scores. For example, the most extreme case involves the Pathfinder case study where mFGS-BS averages a Precision score of 0.52 at 10 k sample size, whereas GFCI averages a score of just 0.13 .

The main conclusions from the results are:

- mFGS-BS is found to be sensitive to the ordering of interventional data sets. However, the sensitivity is relatively small in terms of graphical accuracy, and decreases with the number and the size of interventional data sets.
- Employing all three factors to determine edge direction produces the most accurate graphs (refer to Sect. 3.2.2). Factor 1, which determines the probability of directed edges given the output of FGS, and Factor 2 which determines the probability of directed edges based on the ratio of Sepsets determining v-structure, are found to have a stronger impact (in terms of increasing the F1 and BSF scores) than Factor 3 which relies on changes in objective score between observational and interventional data.
- mFGS-BS is found to be more accurate than the other algorithms when we simulate just one intervened variable. Specifically, mFGS-BS generates the highest F1 and BSF scores for the Asia, Sports and Alarm networks in most of the experiments (refer to Table 8). COmbINE and RFCI-BSC often fail to generate a result within the four-hour runtime limit when applied to the larger networks. The average BSF and F1 scores of mFGS-BS are approximately $45 \%$ and $38 \%$ higher compared to GFCI across all networks, while the average BSF and F1 scores of COmbINE are $16 \%$ and $15 \%$ higher compared to GFCI over all experiments in which COmbINE generates a result.
- The performance of both mFGS-BS and COmbINE continues to improve with the number of interventional data sets, while the performance of GFCI and RFCI-BSC does not. This highlights the advantage of algorithms that consider additional data sets independently. Moreover, the number of edges learnt by mFGS-BS tends to be lower compared to the number of edges present in the true MAGs, for the medium, large and very large networks. Note that while GFCI generates more edges when the number of interventional data sets increase, its overall performance in terms of BSF and F1 scores does not increase.

- The overall performance of mFGS-BS and COmbINE continues to improve with the number of variables targeted for intervention as expected, since the higher number of interventions can be viewed as providing additional causal information to the model. The average BSF scores increase by approximately $9 \%$ and $11 \%$ when considering five, instead of one, intervened variables per interventional data for the mFGS-BS and COmbINE algorithms respectively.
- The runtime of mFGS-BS, relative to the other three algorithms, appears to be worst in small and medium networks. However, the runtime of mFGS-BS, RFCI-BSC and GFCI scale linearly with the number of interventional data sets. In contrast, the empirical results suggest that COmbINE does not scale well with additional data sets. One explanation might be because COmbINE uses the MINISAT application to solve SAT instances encoded from results of CI tests, and the time to solve these SAT instances increases exponentially with the number of variables. A rather unexpected finding is that the computational time of COmbINE is higher when the sample size is 1 k compared to 10 k . This might be because the results of CI tests learnt from low sample sizes contain more conflicts compared to those obtained when the sample size of the input data is higher. Lastly, GFCI is found to be the fastest algorithm in almost all of the experiments, as expected, since it does not consider each input data set independently.


# 6 Conclusion 

This paper describes the mFGS-BS hybrid algorithm which produces a PAG by learning the probabilities of each directed edge from one observational data set and one or more interventional data sets in a causally insufficient setting. The posterior probabilities learnt from one data set are considered as candidate objective priors for learning from the next data set. Three other mechanisms contribute to the objective priors used with each data set: colliders identified from the observational data; the CPDAGs produced by running the FGS algorithm on each data set; and a score-based approach relating to intervention targets. Pairs of nodes which have a directed edge in each direction with a probability above a given threshold are treated as having a bidirected edge between them, so that the algorithm produces a PAG.

The results of mFGS-BS were compared to those obtained by COmbINE, which also enables learning from multiple observational and interventional data sets. We have also compared the results against the RFCI-BSC and GFCI algorithms with pooled data, which serves as the baseline performance not accounting for variables targeted for intervention. The empirical evaluation was based on six case studies of different complexity, with varying numbers of intervened variables, interventional data sets, and sample sizes. Overall, the results show that mFGS-BS considerably outperforms the baseline algorithms in terms of graphical accuracy, and also outperforms COmbINE in most of the experiments. RFCI-BSC and GFCI consider a single data set of pooled data rather than each input data set independently. GFCI was the faster algorithm because it performs fewer CI tests by design, whereas RFCI-BSC tends to fail to

produce a result when applied to larger networks and sample sizes. Lastly, mFGSBS offers considerable improvements in learning efficiency compared to COmbINE, which failed to produce any results, within the four-hour runtime limit, for the larger networks.

A limitation of mFGS-BS is that it is sensitive to the ordering of the data sets and assumes equal sample size across all input data sets. This is, of course, an unrealistic assumption in practice. Future revisions of mFGS-BS will adjust the algorithm such that the local BDeu scores can be normalised to enable learning from multiple data sets with varying sample sizes. Other future research directions could focus on enabling learning from interventional data sets that contain imperfect and uncertain interventions (refer to Sect. 2.2), in addition to perfect interventions.

Acknowledgements This research was supported by the ERSRC Fellowship project EP/S001646/1 on Bayesian Artificial Intelligence for Decision Making under Uncertainty (Constantinou, 2018), and by the Royal Thai Government Scholarship offered by Thailand's Office of Civil Service Commission (OCSC).

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/ by/4.0/.

# Appendix: Supplementary results 

See Figs. 12, 13, 14 and 15.

![img-16.jpeg](img-16.jpeg)

Fig. 12 Average performance of the algorithms when applied to synthetic data generated from the Formed network, assuming one intervened variable and $5 \%$ latent variables per data set, over two sample sizes.

![img-17.jpeg](img-17.jpeg)

Fig. 13 Average performance of the algorithms when applied to synthetic data generated from the Pathfinder network, assuming one intervened variable and $5 \%$ latent variables per data set, over two sample sizes.

![img-18.jpeg](img-18.jpeg)

Fig. 14 Average performance of the algorithms when applied to synthetic data generated from the Formed network, assuming five intervened variables and $5 \%$ latent variables per data set, over two sample sizes.

![img-19.jpeg](img-19.jpeg)

Fig. 15 Average performance of the algorithms when applied to synthetic data generated from the Pathfinder network, assuming five intervened variables and $5 \%$ latent variables per data set, over two sample sizes.
