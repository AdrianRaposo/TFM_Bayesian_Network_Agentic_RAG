# Variable optimisation of medical image data by the learning Bayesian Network reasoning 

A.B Orun and N. Aydin, Member, IEEE


#### Abstract

The method proposed here uses Bayesian non-linear classifier to select optimal subset of attributes to avoid redundant variables and reduce data uncertainty in the classification process often used in medical diagnosis. The method also exploits the structural reasoning ability of Bayesian Networks (BN) to optimize large number of attributes to prevent overfitting, meanwhile it maintains the high classification accuracy. This process simplifies the complex data analyses and may lead to a cost reduction in clinical data acquisition process.


## I. INTRODUCTION

The learning classifiers have been designed to learn from different cases by using their inference capabilities by generating rules from the cases and then they exploit those rules to classify the new cases. In some circumstances the data may contain considerable amount of uncertainty which may also be represented through the appropriate use of probability. The methods used in learning classifiers may appear in different forms, such as reinforcements learning, genetic algorithms, evolution, etc. [13]. Learning classifier systems rely on cause-effect (rule-based) network of variables. The network configuration may be established manually or automatically. Manually constructed network depends on expert knowledge/experience and may reach the conclusion faster than automatically constructed networks. Because automatic configuration of a network is reached by trial-and-error basis operations and requires large number of calculations, but on the other hand it operates according to more objective statistical criteria. As we know that human being (even at expertise level) can not be as objective as an automatic algorithm to construct a network, especially when cause-effect relations between the large number of variables are very complicated. An automatic network construction procedure may only be justified objectively by data mining, which means the patterns within large data set are searched and detected. An automatic network construction procedure also includes too many options such as automatic threshold selection, discretization methods of continuous variables, multi-net options, etc. which are the components of

Manuscript received April 1, 2010. This work was supported by EPSRC (grant number GR/M53035)
A.B Orun was with the University of Birmingham, School of Computer Science. He is now with Orun Computer Consultancy in Birmingham - UK. (e-mail: orun@orun-scientific.co.uk)
N. Aydin is with Yildiz University, Electrical and Electronics Faculty, Istanbul - Turkey. (e-mail : naydin@yildiz.edu.tr)
automatic process. The ultimate accuracy of classification heavily depends on network consistency. This requires a proper connection between the nodes, adequately selected network parameters (threshold, discretization methods, etc.) and efficient structure learning algorithms (Search \& scoring, dependency analysis, etc). Adequately selected subset of variables also play an important role in reliable network construction and accurate classification. We have to note that a large number of variables is not necessarily improve the classification results because some variables may contain inconsistent data and may confuse the whole classification process.

## II. PREVIOUS WORKS

Non-linear classifiers like Bayesian networks (BN) are in pressing demands for an accurate analysis of medical data which may contain considerable amount of uncertainty (e.g. missing patient information, uncertainty in observations or test results, etc.). In recent years too many research have been carried out to exploit Bayesian networks for medical data analysis and decision making. Dagum and Chavez [5] focus on approximation algorithms to be used in Bayesian networks to solve time-pressured decision problems in medical applications. These algorithms simplify the process and run faster than the exact algorithms. Within this work our experiments focus on a variable optimisation method which leads to data and cost reduction. Some similar attempts in the past have been made by several authors to reduce Bayes network complexity. Xiang and Poh [19] exploit the concept of space and temporal abstraction to reduce the computational complexity. Wellman et al. [18] improve the reasoning ability of network by constructing a network which contains only the data related to a set of observations and not the whole knowledge base. Langley and Sage [12] use forward selection method to specify the most suitable subset of variables. Kohavi and John [11] use best first-search by accuracy estimates method to find best subset. Drugan and Wiering [20] use minimum descriptive length to select the features which helps identify redundancy at different levels. Peng et al. [21] integrate filter and wrapper methods into a sequential search procedure. Morais and Aussem [22] introduce novel Markov boundary to reduce feature set. Zhang et al. [23] use a feature extraction technique based on principal component analysis.

# III. SUBSET OF VARIABLE SELECTION 

Overfitting is one of the major problems in data mining which may happen if data set contains too many variables and hence a large number of conditional probability table entries. The chance of this event may be reduced by considering only a "subset" of variables, the process is also called "feature (variable) selection". This is already an active research topic of data mining. Introduced work here brings a different approach to feature selection by exploiting bayesian nets. Several authors already work on "variable selection" (as already mentioned in Chapter II). In our work the selection of optimum set of variables among the others is made at the early stage of the network construction (after training) by the algorithm called dependency analysis and on this basis the ultimate network is constructed with the connections of these variables [3]. The dependency analysis used at the first stage of variable selection process mentioned by many authors so that it gives better classification results than scoring-based algorithms [6] [7]. The novel method for selecting a subset of variables introduced here based on the major steps and may be summarized as follows:

1. A number of BN classifiers are constructed, each on a subset of randomly selected variables. This group is a very small proportion of the total number of combinations (like the ratio of $1 / 10,000$ approximately)
2. The combinations of variables then become the subject of classification by BN and the accuracy achieved with each on the original data set becomes the element of class variable.
3. BN classifier selects the best-classifying subset of variables. This is not limited to the member of subset which one presented to the BN classifier.
4. The best classifying subset of variables is used in the final BN classifier to classify the original data.

## IV. METHODS AND TECHNIQUES

Bayesian Network $(B N)$ is a directed acyclic graph $(D A G)$ which performs knowledge representation and reasoning even under uncertainty. It is also called directed Markov fields, belief network or casual probabilistic network [11] BN is a probabilistic model which graphically encode the conditional independence $(C I)$ relationships among the set of data. In $B N$ each node represents database attribute and called variable. The arcs between nodes represent dependency relationships of variables. $B N$ is very efficient tool to model the joint probability distribution of variables. In example Let $\mathrm{U}=\left\{\mathrm{A}_{1}, \ldots \mathrm{~A}_{\mathrm{n}}\right\}$ be a random variable denoting patterns spanning the $n=N x M$ dimensional vector space. The joint probability distribution $\mathrm{P}=\left(\mathrm{A}_{1}, \ldots \mathrm{~A}_{\mathrm{n}}\right)$ is then a product of all conditional probabilities and may be represented as ;

$$
P(U)=\prod_{i} P\left(A_{i} \mid p a\left(A_{i}\right)\right)
$$

where $\mathrm{pa}\left(\mathrm{A}_{\mathrm{i}}\right)$ is the parent set of $\mathrm{A}_{\mathrm{i}}$. Structural learning is a major specification of $B N$. This is based on constructing relationships between the variables and at some extent similar to data mining principles. The major difficulty is the automatic configuration of a correct casual structure of nodes within the networks. Structural learning algorithms fall into two categories : a) search and scoring based. b) dependency analysis. In our experiments the latter one is used to construct the network. The structural learning Bayesian Network software package (PowerConstructor©) used in this work [4] accepts entering a continuous variable and uses Markov condition to get a collection of conditional independence statements from the network.

## V. VARIABLE SELECTION MATRIX (VSM)

At this stage we investigate the effect of the "existence" of variables to the classification accuracy in the network. By selecting the mode of each variable randomly (existence is represented by 1 or non-existence by 0 ) we configure the Variable Selection Matrix (VSM) as is shown in Table 1. To avoid any regular pattern of variable selection which might be caused by the random variable selection process, the variable selection criteria is shifted from 0 to 1 progressively from beginning of the matrix to end of it. Therefore the initial rows of matrix tend to have more 0 values than last rows.

## VI. NETWORK OPTIMISATION

For each combination of variables in each row (Table 1), we repeated the classification procedure $\left(C P_{i}\right)$ using PowerConstructor with the parameter options $(t=0.1$, equal width discretization method with 13 intervals) using the training/test sets but in each time with the specified group of variables (specified in each combination). For each combination of variables in a row, the classification accuracy is found by $C P_{i}$ and recorded in the last column (class variable). Once the table is completed, then whole table (including binary values and their classification results) is recorded as a new file and used as a new training set. The number of all possible combination of 23 variables is enormously large (about $8 \times 10^{6}$ combinations). This would also be the number of all classification procedures which would theoretically cover all possible cases. Due to impracticality of this large amount of work we use only a limited set of combinations ( 83 cases) which is deemed to be a subset of all combinations (about $1 / 10,000$ of all possible cases) and this subset is statistically expected to represent the substantial portion of whole set. This form of combination has been decided after overviewing the

histogram of different variable distributions where the most suitable one was selected to avoid a regular pattern in VSM.

TABLE I
VARIABLE SELECTION MATRIX (VSM)
![img-0.jpeg](img-0.jpeg)

In the matrix (variable exists $=1$ and otherwise $=0$ ) where the corresponding accuracy of classification result for each row is shown in the last column (class node). Here for each row a compete $B N$ classification procedure $\mathrm{CP}_{\mathrm{i}}$ is repeated to calculate the corresponding classification accuracy.

## VII. CLASSIFICATION

The classification procedure uses network training data set of 300 cases and test set of 48 cases which are the only available data extracted from the large archive of skin lesion images where the only sufficiently visible ones have been selected among the others. Both sets are independent from each other and both contain same type of 23 variables. The classification process which classifies two cases (melanoma or benign) is applied after the discretization of the continuous variables by 13 intervals and "equal frequency" method which are decided by experiments and give more accurate results than other options (e.g. "equal width" or "entropy based" methods). The conditional independence threshold value $t$ (which specifies the links between nodes) is selected as small as possible $(t=0.1)$ to improve the training accuracy. But if $t$ is selected smaller than that, then the model becomes more complex and the test accuracy decreases. The classification procedure described here is repeated for each combination of variables located in each row of variable selection matrix.

## VIII. DATA SELECTION

The data sets used within this work contain two types of variables. First one is acquired by Spectrophotometric Intracutaneous Analysis (SIA) technique using a special imaging device SIAscope ${ }^{\circledR}$ which produces eight narrow-
band spectrally filtered images of the skin over the area of $24 \times 24 \mathrm{~mm}$ in the range of wavelength between 400 and 1000 nm . Second type of variables is acquired by direct clinical examination such as dermatoscopy (epiluminescence microscopy, dermoscopy, oil-emersion microscopy, etc.).
The classification procedure here uses training and test data sets. The training set contains 300 cases ( 42 melanoma and 258 benign) and test set contains 48 cases ( 10 melanoma and 38 benign). Both sets are independent from each other and contain 23 variables which correspond to lesion's characteristic features (e.g. symmetry, diameter, etc.). Especially by the use of different ranges of light spectrum, a clear visible identification of total melanin, collagen and blood is possible. For example $I R$ band is used to analyse the quantity of collagen within the papillary dermis. The melanin below the dermoepidermal junction is identified since the spectral remittance of melanin changes with respect to its position in epidermis and papillary dermis. The information about some variables are obtained by asking the patients (e.g. change in size, shape and colour of the lesion; change in sensation, bleeding and inflammation) and some information are the demographic data (age, sex, etc.). Some of the variables are described by Moncrieff et al. [15]. The abbreviations in Table 1 are : dermal melanin (der_mel), displacement with erythematous blush (disp_blus), measures of lesion diameter (diam_6, diam_7), sensitivity (sens), collagen holes (coll_bin), blood globules (bg_bin), erythematous blush (bl_blush), dermal melanin globules (dm_glob), assymetry (asym), biaxial symmetry (sym2).

## IX. NETWORK CONSTRUCTION

The graphical display utility provided by PowerConstructor software package is shown in Figure 1. The network is generated automatically in semantic form after the training stage which contains the subset of 6 nodes. After the training process conditionally dependent nodes are linked to each other (the direction of arrows is not important).
![img-1.jpeg](img-1.jpeg)

Figure 1. Network configuration generated after training process which includes optimum set of attributes (Case A)

The results in Table 2 also show that parametric images yields more accurate classification results than direct image data obtained by clinical examination (Cases D and E).

TABLE I I
CLASSIFICATION RESULTS


In Table 2, Case G and H show the maximum classification accuracy results obtained. The reason why $100 \%$ accuracy can not be reached is, because unlike the decision trees, the Bayesian networks are generative models and a such model which gives $100 \%$ classification accuracy would possibly be overfitting one. The accuracy results of A and C are not comparable since the fist one depends on automatic classification procedure without human interaction where as the latter one depends on manual selection of variables by the medical experts.

## X. CONCLUSION

The aim of this work is to compare different classification results where each case uses different combination of variables. The aim of work is also to define the most appropriate network which contains minimum number of nodes with the high level of classification accuracy. Since
the improvement of classification accuracy is not the ultimate goal of this work, no particular attention is paid on comparing the results with different classification algorithms like decision tree, instance-based inducer, rule induction, etc. The work presented here rather focuses on minimising the number of variables. This will reduce the cost and labour work of the routine clinical tasks. The minimised set of variables here also provides better classification results than the complete set which includes all variables. This is because optimisation procedure may eliminate those variables which cause confusion by overfitting, uncertainty, etc.
