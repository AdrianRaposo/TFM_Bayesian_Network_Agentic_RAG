# Bayesian Network Multi-classifiers for Protein Secondary Structure Prediction 

Víctor Robles ${ }^{\text {a }}$, Pedro Larrañaga ${ }^{\text {b }}$, José M. Peña ${ }^{\text {a }}$,<br>Ernestina Menasalvas ${ }^{\text {a }}$, María S. Pérez ${ }^{\text {a }}$, Vanessa Herves ${ }^{\text {a }}$ and<br>Anita Wasilewska ${ }^{\text {c }}$<br>${ }^{a}$ Department of Computer Architecture and Technology, Technical University of<br>Madrid, Madrid, Spain, \{vrobles, jmpena, emenasalvas, mperez, vherves\}@fi.upm.es<br>${ }^{\text {b }}$ Department of Computer Science and Artificial Intelligence, University of the Basque Country, San Sebastián, Spain, ccplamup@si.ehu.es<br>${ }^{\text {c }}$ Department of Computer Science, University of Stony Brook, Stony Brook, New York, anita@cs.sunysb.edu


#### Abstract

Successful secondary structure predictions provide a starting point for direct tertiary structure modelling, and also can significantly improve sequence analysis and sequence-structure threading for aiding in structure and function determination. Hence the improvement of predictive accuracy of the secondary structure prediction becomes essential for future development of the whole field of protein research.

In this work we present several multi-classifiers that combine the predictions of the best current classifiers available on Internet. Our results prove that combining the predictions of a set of classifiers by creating composite classifiers is a fruitful one. We have created multi-classifiers that are more accurate than any of the component classifiers. The multi-classifiers are based on Bayesian networks. They are validated with 9 different datasets. Their predictive accuracy results outperform the best secondary structure predictors by $1.21 \%$ on average.

Our main contributions are: (i) we improved the best know predictive accuracy by $1.21 \%$, (ii) our best results have been obtained with a new semi naïve Bayes approach named Pazzani-EDA and (iii) our multi-classifiers combine results of previously build classifiers predictions obtained through Internet, thanks to our development of a Java application.

Key words: Multi-classifier, supervised classification, machine learning, stacked generalization, Bayesian networks, protein secondary structure prediction, Pazzani-EDA.

# 1 Introduction 

Prediction of a secondary structure of a protein from its amino acid sequence remains an important and difficult task. Not only can successful predictions provide a starting point for direct tertiary structure modelling, but they can also significantly improve sequence analysis and sequence-structure threading for aiding in structure and function determination [1].

Since early attempts to predict secondary structure, most effort have focused on development of mappings from a local window of residues in the sequence to the structural state of the central residue in the window (see Figure 1). A large number of methods for estimating such mappings have been developed.

Methods predicting protein secondary structure have improved substantially in the 90's through the use of machine learning methods and evolutionary information from the divergence of proteins in the same structural family. At the alignment level, the increase of the size of databases and the ability to produce profiles that include remote homologs using PSI-BLAST [2] have also contributed to performance improvement [34].

In this paper we present a protein secondary structure prediction multi-classifier system based on the stacked generalization paradigm [5] in which a number of classifier layers are designed to be part of a global multi-classifier, where the upper layer classifiers receive the class predicted by its immediately previous layer as input. The multi-classifier system has been programmed as a JSP Web application using several Java classes.

During the past several years, in a variety of application domains, researches in machine learning have reignited the effort to learn how to create and combine an ensemble classifiers. This research has the potential to apply accurate composite classifiers to real world problems by intelligently combining known learning algorithms.

Classifier combination falls within the supervised learning paradigm. This task orientation assumes that we have been given a set of training examples, which are customarily represented by feature vectors (training records). Each training example is labelled with a class target, which is a member of a finite, and usually small set of class labels. The goal of supervised learning is to predict the class labels of examples that have not been seen.

Combining the predictions of a set of component classifiers has shown to yield accuracy higher than the most accurate component on long variety of supervised classification problems [6].

We have used nine main datasets to train and test our approach: a training set, the PDB_SELECT list [7] of March 2002 (HS1771), and eight test sets (RS126 [8], CB513 [9] and 6 different datasets from the EVA project [10]).

We have developed a two layer classification system in which we use a set of protein secondary structure prediction servers of Internet as layer-0 single classifiers, and we induce, over predictions made, different Bayesian network structures that acts as a consensed voting system at layer-1.

The rest of the paper is organized as follows. Section 2 explains the multiclassifier schema. Section 3 describes the datasets for the level-0 classifiers. In Section 4 we present in detail the statistics used to compare the secondary structure servers and the multi-classifiers. Section 5 describes the six level-0 classifiers used in construction of our multi-classifiers. Section 6 describes how to obtain the datasets for the level-1 classifiers (i.e. multi-classifiers). Section 7 contains a description of the level-1 multi-classifiers. In Section 8 we shortly discuss the experimental results. Finally, Section 9 contains the conclusion and the future research plans.

# 2 Multi-classifier schema 

We present a multi-classifier for protein secondary structure prediction based on a straightforward approach that has been termed stacked generalization by Wolpert [5]. In its most basic form, its layered architecture consists of a set of component classifiers that form the first layer. Wolpert [5] calls the component classifiers the level-0 classifiers and the combining classifier, the level-1 classifier. In this work we introduce 7 different level-1 classifiers. See Figure 2 for the schema of our stacked generalization classifiers.

Stacked generalization is a framework for classifier combination in which each layer of classifiers is used to combine the predictions of the classifiers of its preceding layer. A single classifier at the top-most level outputs the ultimate prediction. In our approach, we use a two-level system that has a Bayesian network as this single, combining classifier and this Bayesian network is used to perform the last classification step.

# 3 Datasets for protein secondary structure prediction 

We have used nine different datasets to develop and test our multi-classifiers. They are:

- HS1771: The dataset HS1771, with 1771 sequences, has been used for training and testing our multi-classifiers. This dataset is the PDB_SELECT list [7] published on March, 2002. The PDB_SELECT lists are intended to save time and effort by offering a representative selection of the PDB database, that is currently a factor of eight smaller than the entire database.
- CB513: This dataset of 513 sequences was developed by Cuff and Barton [9] with the aim of evaluating and improving protein secondary structure prediction methods. It is, perhaps, one of the most used independent dataset in this field.
- RS126: This original set of 513 sequences by Rost and Sander [8], currently correspond to a total of 23,363 amino acids positions (this number has varied slightly over the years due to changes and corrections in the PDB [11]).
- EVA1, ..., EVA6: 6 novel test sets are provided by the datasets available from the real-time evaluation experiment called EVA [10], which compares a number of prediction servers on a regular basis using the sequences deposited in the PDB every week. In particular we have used all the datasets labelled "common1" to "common6" published on 19/10/2002.


## 4 Statistics in the PSSP problem

To validate the results obtained in the methods of secondary structure prediction, a set of statistic factors has been defined.

In order to compute these statistics, a 3 x 3 -sized confusion matrix has been used, where the rows show the states of the actual secondary structure (obtained through the DSSP program [12]) and the columns describe the states of the secondary structure predicted by the classifier. Table 1 shows the elements of the confusion matrix.

The following values are calculated from the confusion matrix:

- $o b s_{H}$ : represents the number of residues observed in state helix $(\mathrm{H})$, that is, the states H that appear in the real structure,
- $o b s_{E}$ : represents the number of residues observed in state $\beta$ strand (E),
- $o b s_{L}$ : represents the number of residues observed in state coil (L),
- $p r d_{H}$ : represents the number of residues predicted in state helix (H),
- $p r d_{E}$ : represents the number of residues predicted in state $\beta$ strand (E),

- $\operatorname{prd}_{L}$ : represents the number of residues predicted in state coil (L),
- $N_{\text {res }}$ : represents the total number of residues of the chain, that is, the length of the sequence.

In a mathematical representation, we observe that:
$M_{i j}$ denotes the number of residues observed in state $i$ and predicted in state $j$, with $i, j \in\{H, E, L\}$

The total number of residues observed in state $i$ is:

$$
o b s_{i}=\sum_{j \in\{H, E, L\}} M_{i j}
$$

The total number of residues predicted in state $j$ is:

$$
\operatorname{prd}_{j}=\sum_{i \in\{H, E, L\}} M_{i j}
$$

and the total number of states in the sequence is:

$$
N_{\text {res }}=\sum_{i} o b s_{i}=\sum_{j} p r d_{j}=\sum_{i, j} M_{i j}
$$

# 4.1 Three-state prediction accuracy: $Q_{3}$ 

This is the measure used traditionally for evaluating the accuracy of secondary structure prediction. This parameter represents the total number of residues correctly predicted. In order to calculate it, the states helix, $\beta$ strand and coil correctly predicted are added (sum of all $M_{i i}$ ), dividing this sum by the total number of residues of the observed sequence $\left(N_{\text {res }}\right)$ and expressing the result as percentage. $Q_{3}$ is obtained as:

$$
Q_{3}=100 \frac{1}{N_{\text {res }}} \sum_{i=1}^{3} M_{i i}
$$

### 4.2 Per-state percentages

To define the accuracy for a particular state (helix, strand, coil), there are two possible variants:

- Percentage of all residues observed in a particular state (\%obs).

$$
Q_{i}^{\% o b s}=100 \frac{M_{i i}}{o b s_{i}}
$$

In this way, for example, it is possible to calculate the percentage of residues observed in the state helix $H$.

- Percentage of all residues correctly predicted in a particular state (\%prd).

$$
Q_{i}^{\% p r d}=100 \frac{M_{i i}}{p r d_{i}}
$$

For example, for a particular state $i=\mathrm{H}$, it is possible to calculate the percentage of residues correctly predicted in the state helix $H$.

# 4.3 Information index 

The information index is given by:

$$
i n f o=\ln \left(\frac{P_{p r d}}{P_{o b s}}\right)
$$

where $P_{o b s}$ describes the probability for finding one particular string of $N_{\text {res }}$ residues with $o b s_{i}$ residues being in structure $i$ out of all combinatorial possible ones, and $P_{p r d}$ is the probability for a particular realization of the confusion matrix $M$. The resulting information index is:

$$
i n f o=\frac{i n f o \% o b s+i n f o \% p r d}{2}
$$

with:

$$
\begin{aligned}
& i n f o \% o b s=1-\frac{\sum_{i=1}^{3} p r d_{i} \ln p r d_{i}-\sum_{i, j=1}^{3} M_{i j} \ln M_{i j}}{N_{r e s} \ln N_{r e s}-\sum_{i=1}^{3} o b s_{i} \ln o b s_{i}} \\
& i n f o \% p r d=1-\frac{\sum_{i=1}^{3} o b s_{i} \ln o b s_{i}-\sum_{i, j=1}^{3} M_{i j} \ln M_{i j}}{N_{r e s} \ln N_{r e s}-\sum_{i=1}^{3} p r d_{i} \ln p r d_{i}}
\end{aligned}
$$

### 4.4 Matthew's correlation coefficients

Matthew's correlation coefficients [13] are not influenced by the percentage of true positives (number of elements of the structure $i$ correctly predicted

divided by the number of the elements of the structure $i$ ) in a sample, being the best way of evaluating different methods. The result is a number between -1 and 1 , where value 1 represents a perfect coincidence, value -1 a total inequality and value 0 indicates that the prediction has not correlation with the results.

Although the correlation coefficient is an useful measure of the accuracy of the prediction, this coefficient does not evaluate the similarity between the prediction and the protein. In order to know the accuracy of the prediction, the segment overlap measure is taken into account. Matthew's correlation coefficients are defined by the following formula:

$$
C_{i}=\frac{p_{i} n_{i}-u_{i} o_{i}}{\sqrt{\left(p_{i}+u_{i}\right)\left(p_{i}+o_{i}\right)\left(n_{i}+u_{i}\right)\left(n_{i}+o_{i}\right)}}
$$

with:

$$
p_{i}=M_{i i}, n_{i}=\sum_{j \neq i} \sum_{k \neq i} M_{j k}, o_{i}=\sum_{j \neq i} M_{j i}, u_{i}=\sum_{j \neq i} M_{i j}
$$

$i, j \in\{H, E, L\}$,
where:

- $n_{i}$ : contains the number of different states observed in $i$ and predicted as state $j$, being $j$ different from $i$. For example, for the state $i=H, n_{i}$ represents the number of states $H$ observed in the sequence and predicted as $L$ or $E$.
- $u_{i}$ : contains the number of residues observed in the state $i$ and predicted in a state different from $i$. For example, for the state $i=H, u_{i}$ represents the number of states $H$ observed in the sequence and predicted as $E$ or $L$.
- $p_{i}$ : represents the number of residues observed in the state $i$ and correctly predicted.
- $o_{i}$ : represents the number of residues observed in a state different from $i$ and predicted as $i$.


# 4.5 SOV: Segment OVerlap measure 

Statistics applied previously are general statistics, and thus, can be applicable to every classification problem. However, the segment overlap (SOV) is a measure, developed by Rost [14] and modified by Zemla [15], which specifies the specific objectives of the secondary structure prediction.

Unlike the measure $Q_{3}$, which considers the residues in an individual fashion, $S O V$ measures the accuracy taking the different segments of a sequence into account. $S O V$ provides the measure of the segment overlap for an only state $(H, E$ or $L)$ or for all three states.

If for example we consider the state $\operatorname{coil}(L)$, the measure $S O V$ calculates the accuracy of the segments prediction in such state. A segment is considered a part of the sequence where the state $i$ appears consecutively (in this case, $L$ ). Therefore, $100 \%$ is obtained when the segments of the observed sequence are equal to the predicted sequence. When the $S O V$ is calculated for all the three states, the segments of the three states (helix, $\beta$ strand and coil) are taking into account.

# 4.5.1 Per-stage segment overlap 

This value is given by:

$$
\operatorname{SOV}(i)=100 \frac{1}{N(i)} \sum_{S(i)} \frac{\operatorname{minov}\left(s_{1}, s_{2}\right)+\delta\left(s_{1}, s_{2}\right)}{\operatorname{maxov}\left(s_{1}, s_{2}\right)} \operatorname{len}\left(s_{1}\right)
$$

where:

- $s_{1}$ and $s_{2}$ : are the observed and predicted secondary structure segments (in state $i$, which can be either $H, E$ or $L$ ),
- $\operatorname{len}\left(s_{1}\right)$ : is the number of residues in the segment $s_{1}$,
- $\operatorname{minov}\left(s_{1}, s_{2}\right)$ : is the length of actual overlap of $s_{1}$ and $s_{2}$, i.e. the extent for which both segments have residues in state $i$,
- $\operatorname{maxov}\left(s_{1}, s_{2}\right)$ : is the length of the total extent for which either of the segments $s_{1}$ or $s_{2}$ has a residue in state $i$,
- $\delta\left(s_{1}, s_{2}\right)$ : is the integer value defined as being equal to the following:

$$
\delta\left(s_{1}, s_{2}\right)=\min \left\{\begin{array}{c}
\operatorname{maxov}\left(s_{1}, s_{2}\right)-\operatorname{minov}\left(s_{1}, s_{2}\right) \\
\operatorname{minov}\left(s_{1}, s_{2}\right) \\
\operatorname{int}\left(0.5 * \operatorname{len}\left(s_{1}\right)\right) \\
\operatorname{int}\left(0.5 * \operatorname{len}\left(s_{2}\right)\right)
\end{array}\right\}
$$

- $\sum$ : is taken over all the pairs of segments $\left(s_{1}, s_{2}\right)$, where $s_{1}$ and $s_{2}$ have at least one residue in state $i$ in common,
- $N(i)$ : is the number of residues in state $i$ defined as follows:

$$
N(i)=\sum_{S(i)} \operatorname{len}\left(s_{1}\right)+\sum_{S^{\prime}(i)} \operatorname{len}\left(s_{2}\right)
$$

The two sums are taken over $S$ and $S^{\prime} . S(i)$ is the number of all pairs of segments $\left(s_{1}, s_{2}\right)$, where $s_{1}$ and $s_{2}$ have at least one residue in state $i$ in common. $S^{\prime}(i)$ is the number of segments $S_{1}$ that do not produce any segment pair.

Figure 3 shows a fragment of an observed sequence and a predicted sequence, where the elements of the $S O V$ formula are depicted.

# 4.5.2 Segment OVerlap quantity measure for all three states 

This value is obtained by applying this formula:

$$
S O V=100 \frac{1}{\sum_{i} N(i)} \sum_{i} \sum_{S(i)} \frac{\operatorname{minov}\left(s_{1}, s_{2}\right)+\delta\left(s_{1}, s_{2}\right)}{\operatorname{maxov}\left(s_{1}, s_{2}\right)} \operatorname{len}\left(s_{1}\right)
$$

where $\sum_{i} N(i)$ is a sum of $N(i)$ over all three conformational states ( $i=$ helix, strand, coil).

## 5 Level-0 composite classifiers

After an exhaustive search over Internet, we have found 9 secondary structure prediction servers. We have selected, with our own experimental results, the best 6 servers as the level -0 classifiers. The Table 2 shows all the contacted servers, with its location and prediction method. Also, Figure 4 shows the geographical location of the servers.

### 5.1 JPred

JPred [16] is an interactive protein secondary structure prediction Internet server. The server allows a single sequence or multiple alignment to be submitted, and returns predictions from six secondary structure prediction algorithms that exploit evolutionary information from multiple sequences. A consensus prediction is also returned.

All the secondary structure prediction methods used, require either, multiple sequences or an alignment of multiple sequences. Thus, if a single sequence is submitted, an automatic process creates a multiple sequence alignment, prior to prediction [16].

Six different prediction methods: DSC [17], PHD [8], NNSSP [18], PREDATOR [19], ZPRED [20] and MULPRED [21] are then run, and results from each method are combined into a simple file format.

A consensus prediction based on a simple majority method of NNSSP, DSC, PREDATOR and PHD is provided by the JPred server.

# 5.2 SSPro 

SSPro is a fully automated system for the prediction of protein secondary structure. The system is based on an ensemble of bidirectional recurrent neural networks (BRNNs) [22|23]. BRNNs are graphical models that learn from data the transition between an input and an output sequence of variable length. The model is based on two hidden Markov chains, a forward and a backward chain, that transmit information in both directions along the sequence, between the input and the output sequences. Three neural networks model respectively the forward state update, the backward state update and the input and hidden states to output transition. BRNNs are trained in a supervised fashion using the gradient descent algorithm. The error signal is propagated through the model using the BPTS (backpropagation through structure) algorithm, an extension of BPTT (backpropagation through time), used in unidirectional recurrent neural networks.

A set of 11 bidirectional recurrent neural networks is trained on the dataset. The networks contain roughly 70,000 adjustable weights, have normalized exponentials on the outputs and are trained using the relative entropy between the target and output distributions. The final predictions are obtained averaging the network outputs for each residue.

### 5.3 PHD

PHD [24] was the first method to incorporate evolutionary information (in the form of multiple sequence alignment data) in the prediction of protein secondary structure. The first step in a PHD prediction is generating a multiple sequence alignment. The second step involves feeding the alignment into a neural network system. Correctness of the multiple sequence alignment is as crucial for prediction accuracy as that the alignment contains a broad spectrum of homologous sequences.

The PHD methods process the input information on multiple levels. The first level is a feed-forward neural network with three layers of units (input, hidden, and output). Input to this first level sequence-to-structure network consists

of two contributions: one from the local sequence, i.e., taken from a window of 13 adjacent residues, and another from the global sequence. Output of the first level network is the 1D structural state of the residue at the centre of the input window. The second level is a structure-to-structure network. The next level consists of an arithmetic average over independently trained networks (jury decision). The final level is a simple filter.

# 5.4 PSIPRED 

PSIPRED [3] is a simple and reliable secondary structure prediction method. It use a two-stage neural network to predict protein secondary structure based on the position specific scoring matrices generated by PSI-BLAST. The prediction method is split into three stages: generation of a sequence profile, prediction of initial secondary structure, and finally the filtering of the predicted structure.

### 5.5 PROF

The Prof server [25] is a classifier for protein secondary structure prediction which is formed by cascading (in multiple stages) different types of classifiers using neural networks and linear discrimination. To generate different classifiers it has been used GOR formalism-based methods extended by linear and quadratic discriminations [26,27] and neural network-based methods [28,24]. The theoretical foundation for Prof comes from basic probability theory which states that all of the evidence relevant to a prediction should be used in making that prediction.

### 5.6 SAM-T02

The SAM-T02 [29] method is used for iterative SAM HMM construction, remote homology detection and protein structure prediction. It updates SAMT99 by using predicted secondary structure information in its scoring functions.

The SAM-T02 server is an automatic method that uses two-track hidden Markov models (HMMs) to find and align template proteins from PDB to the target protein. The two-track HMMs use an amino-acid alphabet and one of several different local-structure alphabets.

The SAM-T02 prediction process consists of several parts:

- Finding similar sequences with iterative search using SAM-T2K.
- Predicting local structure properties with neural nets.
- Finding possible fold-recognition templates using 2-track HMMS (the SAMT02 method).
- Making alignments to the templates.
- Building a specific fragment library for the target (with fragfinder).
- Packing fragments and fold-recognition alignments to make a 3D structure (with undertaker).


# 6 Obtaining the datasets for multi-classifiers training 

The process of creating an appropriate dataset for both training and evaluation of the multi-classifiers, as shown in Figure 5, has been achieved in following steps:
(1) High-quality datasets of proteins with known secondary structure are selected. The most representative dataset designed by different groups are HS1771, CB513, RS126 as well as the six data sets gathered by EVA project [10]. From all of them only HS1771 has been used for the training phase of a multi-classifier. This dataset has been selected because it is the most complete of the nine datasets. The remaining ones will be used in the testing phase of the algorithm.
(2) These sequences of proteins are submitted to the six web servers and the process waits for their replies. These replies came as either web pages or e-mail messages.
(3) The replies, once they have been received, are processed. The prediction for the secondary structure of the protein is extracted from the body of the message or from the contents of the web page.
(4) The results are stored in a new dataset to be processed by a multiclassifier. For each of the aminoacids of the protein an instance of the dataset is inserted with all the predictions from the servers and the actual value of its secondary structure.

## 7 Level-1 classifiers based on Bayesian networks

As exposed in [30] we have used Bayesian networks as the consensed voting system. Thus, for building the level-1 classifiers, we have used three different Bayesian network structures: naïve Bayes, Interval Estimation Naïve Bayes (IENB) and the idea of Pazzani of joining attributes in naïve Bayes.

# 7.1 Naïve Bayes 

The naïve Bayes classifier $[31,32]$ is a probabilistic method for classification. It performs an approximate calculation of the probability that an example belongs to a class given the values of predictor variables. The simple naïve Bayes classifier is one of the most successful algorithms on many classification domains. In spite of its simplicity, it is shown to be competitive with respect to other more complex approaches in several specific domains.

This classifier learns from training data the conditional probability of each variable $X_{k}$ given the class label $c$. Classification is then done by applying Bayes rule to compute the probability of $C$ given the particular instance of $X_{1}, \ldots, X_{n}$,

$$
P\left(C=c \mid X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right)
$$

Naïve Bayes is founded on the assumption that variables are conditionally independent given the class. Therefore, posterior probability of the class variable is formulated as follows,

$$
P\left(C=c \mid X_{1}=x_{1}, \ldots, X_{n}=x_{n}\right) \propto P(C=c) \prod_{k=1}^{n} P\left(X_{k}=x_{k} \mid C=c\right)
$$

This equation is highly appropriate for learning from data, since probabilities $p_{i}=P\left(C=c_{i}\right)$ and $p_{k, r}^{i}=P\left(X_{k}=x_{k}^{r} \mid C=c_{i}\right)$ may be estimated from training data. The result of the classification is the class with highest posterior probability.

### 7.2 Interval Estimation Naïve Bayes

Interval Estimation Naïve Bayes (IENB) [33] belongs to the semi naïve Bayes approaches that correct the probabilities produced by the standard naïve Bayes. In this approach, instead of calculating the point estimation of the conditional probabilities from data, as simple naïve Bayes does, confidence intervals are calculated. After that, the search for the best combination of values into these intervals is performed. The goal of this search is try to relieve the assumption of independence among variables the simple naïve Bayes does. This search is carried out by a heuristic search algorithm and is guided by the accuracy of the classifiers.

To deal with the heuristic search EDAs -estimation of distribution algorithmshave been selected. EDAs [34] are non-deterministic, stochastic and heuristic

search strategies that belong to the evolutionary computation approaches. In EDAs, a number of solutions or individuals is created every generation, evolving once and again until a satisfactory solution is achieved. In brief, the characteristic that most differentiates EDAs from other evolutionary search strategies, such as GAs, is that the evolution from a generation to the next one is done by estimating the probability distribution of the fittest individuals, and afterwards, by sampling the induced model. This avoids the use of crossover or mutation operators, and, therefore, the number of parameters that EDAs requires is reduced considerably.

# 7.3 Pazzani 

Pazzani in [35] proposes to improve the naïve Bayes classifier by searching for dependencies among attributes. He develops two algorithms for detecting dependencies among attributes: Forward Sequential Selection and Joining (FSSJ) and Backward Sequential Elimination and Joining (BSEJ).

In this paper, we propose to make a heuristic search of the Pazzani structure with the target of maximize the percentage of successful predictions. We perform this heuristic search with EDAs. The resulting algorithm is called Pazzani-EDA algorithm and a multi-classified build upon it, the MC-PazzaniEDA multi-classifier.

Figure 6 contains an example of two Pazzani structures and their corresponding individuals.

Thus, for a dataset with $n$ attributes, individuals will have $n$ genes, each one with an integer value between 0 an $n$. The value 0 represents that the corresponding attribute is not part of the Pazzani structure. A value between 1 and $n$ means that the corresponding attribute belongs to that group in the Pazzani structure.

### 7.4 Level-1 classifiers

After all the predictions outputs from the six web servers are collected a preliminary study of the predictive accuracy is performed. The statistics presented on Section 4 are calculated. A detailed discussion of these results is included in the next section.

Taking these results into account, we have built and trained the following seven multi-classifiers based on Bayesian networks:

- Naïve-Bayes with the:
- best 4 severs (MC-NB-4),
- best 5 severs (MC-NB-5) and
- best 6 severs (MC-NB-6).
- Interval Estimation Naïve-Bayes with the:
- best 4 severs (MC-IENB-4),
- best 5 severs (MC-IENB-5) and
- best 6 severs (MC-IENB-6).
- MC-Pazzani-EDA with the best 6 servers.

The best six servers (sorted by their accuracy) are: PSIPRED, SSPro, SAMT02, PHD Expert, Prof and JPred. Further details are shown on Tables 3-11.

# 8 Results 

Statistics of the predictions performed by the six selected servers (described in section 5) and the seven multi-classifiers are presented in a form of tables: Tables 3 to 11. We present one table for each of the datasets (HS1771, CB513, RS126, EVA1, EVA2, EVA3, EVA4, EVA5 and EVA6).

These results show that the best classifier for these datasets is PSIPRED. Although its predictions of the secondary structure are of the highest accuracy, it has been further improved by our multi-classifier architectures.

Improvements in terms of overall accuracy are presented on Table 12. These results are compared to PSIPRED predictions on each of the datasets. Our results show that the best multi-classifier algorithm is MC-Pazzani-EDA with and absolute improvement of $1.21 \%$ compared to PSIPRED. If we consider a relative improvement, taking the theoretical maximum accuracy of $88 \%$ into account, MC-Pazzani-EDA outperforms the best classifier by $13.30 \%$. This algorithm gets better results in all but one (EVA6) of the datasets. In Figure 7, we show the final structure obtained by MC-Pazzani-EDA. The four better servers have been included in this structure.

### 8.1 Detailed analysis of HS1771 results

Here are some details of a deeper analysis of the results obtained for HS1771, the most complete dataset for protein second structure prediction.

The most interesting results have been achieved for $\beta$ strand prediction. PSIPRED predicts accurately $69.18 \%$ of the cases while MC-Pazzani-EDA gets $79.05 \%$ giving an improvement of $9.87 \%$. As a drawback, coil structures are classified

correctly in a $76.76 \%$ of the cases, instead of the previous $80.29 \%$ (although predictions have a better quality $80.94 \%$ vs. PSIPRED $75.72 \%$ ).

Another important remark is that the information index is better for all the multi-classifiers compared to PSIPRED. Multi-classifiers have information indexes between 0.43 and 0.44 while PSIPRED has a index of 0.41 .

Matthews' correlation coefficients are also better for all multi-classifier approaches.

The best improvements achieved by multi-classifiers are focus on $\alpha$ helix and $\beta$ strands. Coil prediction is less accurate than some of the best servers.

# 9 Conclusions and Future Research 

On this paper several multi-classifiers based on Bayesian networks have been proposed for the problem of protein secondary structure prediction. Although significant improvements are achieved using simple classifiers (like naïve Bayes), the best results are obtained with innovative methods. These methods have been designed as wrapper approaches for existing Bayesian network classifiers. Interval Estimation Naïve Bayes (IENB) performs an estimation of the best classification probabilities inside of the boundaries of confidence intervals. Another new approach is the design of a variant of Pazzani classification method (greedy search), using heuristic search for selecting the most appropriate features for the classification procedure. Both new approaches use EDAs (estimation of distribution algorithms) to deal with heuristic search.

The multi-classifier system has been programmed as a JSP Web application using several Java classes. This system provides the following features:

- It compares the existing prediction servers world-wide. Statistics of their accuracy and other quality measures are extracted.
- An appropriate selection of datasets for protein secondary structure prediction has been selected.

These datasets have been used to train/test meta-classifiers commented above. The results obtained by these methods have outperformed existing state-of-the-art classifiers by $1.21 \%$ getting the best results ever obtained for this problem ( $80.99 \%$ from CB513-the most commonly used- and $80.25 \%$ for HS1771the most complete-).

There are open issues still ahead:

- To evaluate new classification methods as second level strategies.

- To publish the meta-classifiers as an open-access web service.
- To create a portal to access existing web servers for PSSP prediction. This service would provide users with a single point to access multiple servers.

