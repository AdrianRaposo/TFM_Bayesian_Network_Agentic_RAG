# bnRep: A Repository of Bayesian Networks from the Academic Literature 

Manuele Leonelli<br>MANUELE.LEONELLI@IE.EDU<br>School of Science and Technology<br>IE University<br>Madrid, Spain


#### Abstract

Bayesian networks (BNs) are widely used for modeling complex systems with uncertainty, yet repositories of pre-built BNs remain limited. This paper introduces bnRep, an opensource R package offering a comprehensive collection of documented BNs, facilitating benchmarking, replicability, and education. With over 200 networks from academic publications, bnRep integrates seamlessly with bnlearn and other R packages, providing users with interactive tools for network exploration.


Keywords: Bayesian networks, Probabilistic graphical models, R package, Repository

## 1 Introduction

Bayesian networks (BNs) (Pearl, 1988) are a powerful machine learning model widely used in practice due to their ability to model complex systems with uncertainty and interpretability. Their widespread application spans diverse fields such as engineering reliability (Kabir and Papadopoulos, 2019), environmental sciences (Kaikkonen et al., 2021), healthcare (Kyrimi et al., 2021), and supply chain management (Hosseini and Ivanov, 2020), among others. They are implemented in various software tools, including R packages (e.g. bnlearn Scutari, 2010; gRain Højsgaard, 2012), Python libraries (e.g. pgmpy Ankan and Panda, 2015; pyAgrum Ducamp et al., 2020), and standalone software (e.g. AgenaRisk, BayesiaLab, BayesServer, Hugin Expert, GeNie Modeler, and Netica) ${ }^{1}$, making them accessible to a wide range of users and applications. Despite their widespread application, BNs remain an active research area with ongoing advancements in learning algorithms (e.g. Kuipers et al., 2022; Liu and Constantinou, 2022), inference techniques (e.g. Lin et al., 2020), and new types of networks (e.g. Atienza et al., 2022).

Key reasons for the success of BNs include their explainability, flexibility, and status as the gold standard for causal modeling. Unlike black-box models, BNs offer an intuitive, transparent structure, aligning with trends in eXplainable AI (XAI) (Rudin, 2019). They provide insights into cause-and-effect relationships rather than just correlations (Peters et al., 2017). BNs are also accessible to a broad audience, not requiring deep expertise in computer science or mathematics (Kelly et al., 2013; Moe et al., 2021). Their modular design integrates data, expert knowledge, and model outputs (Leonelli et al.,

[^0]
[^0]:    1. Available at https://www.agena.ai, https://www.bayesia.com, https://www.bayesserver.com, https://www.hugin.com, https://www.bayesfusion.com/genie/, and https://www.norsys.com/netica.html, respectively.

2020; Marcot and Penman, 2019) and supports scenario and "what-if" analyses for simulating interventions and predicting outcomes (e.g. Pitchforth and Mengersen, 2013).

Despite the widespread use, flexibility, and numerous advantages of BNs, repositories of pre-built and documented BNs remain limited compared to other areas of machine learning. In fields like deep learning, there are extensive repositories such as TensorFlow Hub and PyTorch Hub that provide access to a wide range of pre-trained models ${ }^{2}$. Similarly, scikit-learn offers datasets and model repositories for classic machine learning algorithms, facilitating replication, benchmarking, and educational purposes. In contrast, repositories of BNs are relatively scarce, with some notable exceptions like the Bayesian Network Repository (including 31 BNs ), the BNMA BN repository (including 75 BNs ), and the BayesFusion Interactive Model Repository (including 46 BNs ). ${ }^{3}$ However, these collections are often smaller, provide less detailed documentation, and are not consistently updated to reflect recent advancements in BN research.

This gap motivated the creation of bnRep, an open-source R package that offers a comprehensive collection of documented BNs, enabling users to explore, compare, and apply them across various domains. The repository includes over 200 BNs from more than 150 different academic publications, each accompanied by detailed documentation. In the following sections, we provide a brief overview of BNs and present the key features and purposes of the bnRep package, highlighting why R was chosen as the development platform and how the package serves both research and practical needs.

# 2 Bayesian networks 

While a full account of Bayesian networks can be found in several monographs (e.g. Koller and Friedman, 2009), a brief overview is provided here to highlight the key concepts.

A BN gives a graphical representation of the relationship between a vector of variables of interest $\boldsymbol{Y}=\left(Y_{1}, \ldots, Y_{p}\right)$ using a directed acyclic graph (DAG) $G$ and a factorization of the overall probability distribution $P(\boldsymbol{Y})$ in terms of simpler conditional distributions $P\left(Y_{i} \mid \boldsymbol{Y}_{\Pi_{i}}\right)$, where $\boldsymbol{Y}_{\Pi_{i}}$ denotes the parents of $Y_{i}$ in $G$. More formally, the overall factorization of the probability distribution induced by the BN can be written as:

$$
P_{G}(\boldsymbol{Y})=\prod_{i=1}^{p} P\left(Y_{i} \mid \boldsymbol{Y}_{\Pi_{i}}\right)
$$

This factorization has several advantages: it reduces the number of parameters to estimate, allows for easier expert elicitation of local relationships, and makes better use of available data by focusing only on the relevant variables and their parents.

The academic literature has mostly focused on three types of distributional assumptions depending on the nature of the variables: discrete, Gaussian, and conditional linear Gaussian (see e.g. Bodewes and Scutari, 2021). Discrete BNs (Heckerman et al., 1995) are such that $\boldsymbol{Y}$ is a Multinomial random variable and the local distributions are defined as

$$
Y_{i} \mid \boldsymbol{Y}_{\Pi_{i}} \sim \operatorname{Multi}\left(\theta_{i j k}\right), \text { where } \theta_{i j k}=P\left(Y_{i}=j \mid \boldsymbol{Y}_{\Pi_{i}}=k\right)
$$

[^0]
[^0]:    2. Available at https://www.tensorflow.org/huband https://pytorch.org/hub/, respectively.
    3. Available at https://www.bnlearn.com/bnrepository/, https://bnma.co/bnrepo/, and https://repo.bayesfusion.com/, respectively.

The parameters $\theta_{i j k}$ are usually reported in conditional probability tables, reporting the conditional probabilities for each parents' configuration.

Gaussian BNs (Geiger and Heckerman, 1994) assume $\boldsymbol{Y}$ follows a multivariate Normal distribution and the local distributions are defined as linear regressions over the parents:

$$
Y_{i} \mid \boldsymbol{Y}_{\Pi_{i}} \sim \mathcal{N}\left(\beta_{i 0}+\sum_{j \in \Pi_{i}} \beta_{i j} y_{j}, \sigma_{i}^{2}\right)
$$

where the $\beta$ 's are the regression parameters and $\sigma_{i}^{2}>0$.
Conditional Linear Gaussian BNs (Heckerman and Geiger, 1995) combine discrete and continuous random variables. Discrete $Y_{i}$ 's can only have discrete parents and their distribution is as in Equation (2). Continuous $Y_{i}$ 's can have both discrete and continuous parents, and their distribution is a mixture of Gaussian distributions (Equation 3), one for each discrete parent configuration.

BNs can be constructed in various ways: they may be learned from data using algorithms that infer both the structure (DAG) and the conditional probabilities (Kitson et al., 2023; Scutari et al., 2019), elicited from expert knowledge (Barons et al., 2022; Nyberg et al., 2022), or developed through a combination of the two. In practice, many models combine data-driven learning for the probabilistic parameters with expert-elicited structures or relationships, allowing for more accurate and interpretable representations of complex systems (Constantinou et al., 2023).

# 3 The bnRep package 

### 3.1 Why R?

R was chosen as the platform for bnRep due to its robust ecosystem for statistical modeling and seamless integration with existing tools for BNs. The bnlearn package (Scutari, 2010), one of the most widely used packages for learning and inference in BNs, provides the core class objects for bnRep, directly supporting the three main types of BNs previously discussed. Additionally, bnlearn includes various exporting functions (such as write.bif and write.net), enabling users to easily transfer models between R and both Python and basically all standalone BN software. This ensures that models from bnRep can be utilized across different platforms and software environments, making the repository versatile for diverse applications and users' preferences.

The choice of R ensures that bnRep benefits from the CRAN ecosystem, which enforces clear documentation standards and regular package updates. This guarantees that bnRep is user-friendly, thoroughly documented, and accessible to a wide range of users. Moreover, bnRep is compatible with other R packages such as gRain (Højsgaard, 2012) and BayesNetBP (Yu et al., 2020) for inference, bnmonitor (Leonelli et al., 2023) for model diagnostics, and qgraph (Epskamp et al., 2012) for visualization, allowing for extended functionality within the R environment.

### 3.2 Purposes of bnRep

With growing interest in comparing the performance of structural learning algorithms (Constantinou et al., 2021; Scutari et al., 2019), bnRep plays a central role in providing

a benchmarked repository of models that enhances replicability and promotes collaboration in BN research. Researchers can test new algorithms against established models, ensuring consistent evaluation across studies. Additionally, the package serves as an educational tool, offering a diverse collection of models that help students and practitioners explore and learn about BNs across various domains (de Beaufort et al., 2015; Johnson et al., 2014). By sharing knowledge through an accessible, well-documented, and up-to-date repository, bnRep fosters both innovation and cross-disciplinary applications of BNs.

# 3.3 bnRep at a glance 

The bnRep package currently includes 214 BNs, with the number of networks constantly evolving as new models are added. Most networks come from papers published from 2020 onwards, and all are stored as bn.fit objects from the bnlearn package, which supports three types of BNs: discrete, Gaussian, and conditional linear Gaussian. These are the most widely used types of BNs in research and applications, making bnlearn's support for these models crucial for bnRep's extensive and versatile repository.

The package also includes the bnRep_summary dataframe, which provides detailed information about each network. This includes the type of network, summaries of the DAG structure (form, number of nodes, edges, etc.), how the probabilities and DAG were defined (from data, expert knowledge, etc.), and the area of application (e.g., environmental science, engineering, medicine). Summaries of the repository and the networks' characteristics, along with visualizations, are available on the bnRep GitHub page (https://github.com/manueleleonelli/bnRep).

To facilitate interactive exploration, bnRep includes a Shiny app, accessible via the bnRep_app() function. The app allows users to filter and explore the networks' database. It is freely available online at https://manueleleonelli.shinyapps.io/bnRep/, providing a user-friendly interface to access the repository without needing to install the R package.

## 4 Conclusions and future directions

The bnRep package provides a comprehensive, well-documented repository of BNs, making it a valuable resource for researchers and practitioners. By facilitating benchmarking, replicability, and education, bnRep supports the advancement of BN research and cross-field collaboration. Its integration with bnlearn ensures compatibility with widely-used tools, while the Shiny app enhances accessibility for users.

Future updates will expand the repository to include new types of networks, such as copula (Hanea et al., 2015), additive (Kratzer et al., 2023), hybrid (e.g. Pérez-Bernabé et al., 2016), dynamic (e.g. Shiguhara et al., 2021), and continuous time BNs (Nodelman et al., 2002). The project's open-source nature encourages contributions through GitHub, fostering community-driven growth. Additionally, benchmarking functions will be introduced, promoting the development of consistent evaluation methods in the BN field. In conclusion, bnRep not only addresses the current lack of documented BNs but also lays the foundation for establishing benchmarks and fostering innovation in BN research.
