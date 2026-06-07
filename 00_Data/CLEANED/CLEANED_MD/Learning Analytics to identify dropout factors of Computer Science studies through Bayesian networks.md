# Learning Analytics to Identify Dropout Factors of Computer Science Studies through Bayesian Networks 

Carmen Lacave* and Ana I. Molina and José A. Cruz-Lemus<br>Department of Technology and Information Systems, University of Castilla-La Mancha, Spain

* carmen.lacave@uclm.es

Escuela Superior de Informática, Paseo de la Universidad, s/n, 13021, Ciudad Real (Spain)

## Abstract

Student dropout in Engineering Education is an important problem which has been studied from different perspectives, as well as using different techniques. This manuscript describes the methodology used in order to address this question in the context of learning analytics. Bayesian networks have been used as they provide adequate methods for the representation, interpretation and contextualization of data. The proposed approach is illustrated through a case study about Computer Science (CS) dropout at the University of Castilla-La Mancha (Spain), which is close to $40 \%$. To that end, several Bayesian networks were obtained from a database which contained 383 records representing both academic and social data of the students enrolled in the CS degree during four courses. Then, these probabilistic models were interpreted and evaluated. The results obtained revealed that the best model that fits the data is provided by the CS algorithm although the great heterogeneity of the data studied did not permit the adjustment of the dropout profile of the student too accurately. Nonetheless, the methodology described here can be taken as a reference for future works.

Keywords: learning analytics, Bayesian networks, computer science studies dropout, student profile

## 1. Introduction

Nowadays, a multidisciplinary approach has gained an increasing relevance in the

use of big data analysis to inform decisions in Higher Education known as Learning Analytics (LA) (Fiaidhi 2014; Leitner, Khalil \& Ebner 2017), which is highly related to Educational Data Mining (EDM) (Baker \& Inventado 2014; Dutt, Ismail \& Herawan 2017). It involves different areas related to machine learning and visualization. The analysis of educational databases (Romero \& Ventura 2010) can help to the extraction of knowledge (Bakhshinategh et al. 2017) in terms of certain characteristics such as academic performance (Kabakchieva 2013; Daud et al. 2017) or student dropouts one of the major concerns in education (Abu-Oda \& El-Halees 2015; Dekker, Pechenizky \& Vleeshouwers 2009; Dursun 2011).

The student dropout is a reality that affects all universities. It comprises economic losses, social and, possibly, psychological problems in the student, which is consequently, one of the criteria for evaluating Higher Education institutions. This has become a large concern to the education community and policy makers (Aulck et al. 2016). Such problem significantly affects Engineering studies, and its explanation and prediction has been tackled from different perspectives, as well as using different techniques from the first works by Tinto (Tinto 1975), taken as the groundwork for recent research. Some studies can be found based on the creation of surveys or questionnaires to be answered by the students and whose data are subsequently analysed using descriptive statistics. Nevertheless, in these cases, the prediction of students that are in "high risk" is often very difficult and a waste of time (Kostopoulos, Kotsiantis \& Pintelas 2015). Even if the identification is possible, these methods are not effective enough as it is often too late to avoid student dropout. Hence, the prediction of dropout and retention in Engineering studies are key issues and a challenge for Learning Analytics research (Papamitsiou \& Economides 2014; Tseng et al. 2014).

The application of Learning Analytics and EDM methods allows of the dropouts behaviour modelling, predict future dropouts and identify patterns or profiles of students at risk, giving counsellors a chance to advise and guide students into success. Diverse types of algorithms and techniques can be used for information retrieval from educational databases (Romero \& Ventura 2010). In this regard, several works have tried to predict the academic performance and the risk that students drop out (Aulck et al. 2016), (Barbosa, Serra \& Zimbrão 2015), applying different methods such as classification (Kostopoulos, Kotsiantis \& Pintelas 2015; Patil et al. 2017; regression (Bowers 2010; Burgos et al. 2017; Oyerinde 2017), decision trees (Ouadri \& Kalyankar 2010; Sivakumar, Venkataraman \& Selvaraj 2016; Pereira, Pai \& Fernandes 2017; Kabra \& Bichkar 2011; Asif, et al. 2017), genetic algorithms (Marquez-Vera et al. 2013), association algorithms of data mining, or a combination of several methods (Yukselturk, Ozekes \& Türel 2014; Costa et al. 2017; Lykourentzou et al. 2009) for their prediction in educational setting. To make such prediction, several attributes are used such as academic, social, demographic, personal and family data.

In recent years, the incorporation of Bayesian Networks (BN) (Pearl 1988, Castillo, Gutiérrez \& Hadi 1997; Jensen 2001) into educational and institutional research is an approach that is becoming popular and more applied (Di Pietro et al. 2016; Culbertson 2016; Peña-Ayala 2014; Oviedo, Moral \& Puris 2016). BN are graphical models that use probability as a measure of uncertainty and they have been successfully applied to many real-world domains (Naïm et al. 2007; Pourret, Naïm \& Marcot 2008). BN offer an excellent approach to cope with the uncertainty inherent in educational research (Conati, Gertner \& VanLehn 2002), also offering an intuitive, accessible modelling capability that supports the decision-making and policy-setting processes (Corey 2016; Dunn 2016). BN provide advantages over other models: they

provide a compact way of representing knowledge and adequate methods for the interpretation and contextualization of data (Morales \& Salmeron 2003; Fernández et al. 2011). These leads make easy for the researcher to understand the results without the necessity for a lot of statistical knowledge and, therefore, help them to make decisions. In fact, BN have been recommended to be used in the modelling complexities of Higher Education, since these models represent a 'holistic', global approach to answer common institutional research questions (Di Pietro et al. 2015).

Several authors have applied BN to dropout prediction. The study conducted by Kotsiantis et al. (Kotsiantis, Pierrakeas \& Pintelas 2003) can be considered as one of the pioneering studies in investigating the application of machine learning techniques for this purpose. One of its conclusions stated that the Naïve Bayes algorithm can be successfully used. In (Er 2012), a model for predicting students' performance levels was proposed employing three machine learning algorithms: instance-based learning classifier, decision tree and Naïve Bayes. It concluded that Naïve Bayes indeed performed better than any other machine learning algorithm. Fernández et al. (Fernandez et al. 2011) propose a methodology for analysing performance indicators of higher education based on the use of BN. This study works with several indicators: student performance, average mark when admitted to university, etc.; and it provides an analysis of relevance from the Bayesian network. Morales and Salmerón (Morales \& Salmeron 2003) presented a study in which a Bayesian network is built based on data of students from their university, and then an analysis of data is performed by propagating probabilities and extracting profiles through abductive inference. In (Pal 2012), the author uses a Naïve Bayes classification algorithm to generate predictive models so that the student's dropout management is engineered based on the data of the student's previous year, also colleting the student's academic data such as the Secondary School

mark, the Senior Secondary mark, and the student's family position, etc., to predict the student's performance and find the list of that student who needs special attention. Sharabiani et al. (Sharabiani et al. 2014) created a model using a database of the undergraduate engineering students at the University of Illinois in Chicago. The specific objective of this model was to identify the students who might receive low marks and, thus, need extra help from the educational authorities.

This work proposes the use of BN to obtain a classification model to predict and explain the likelihood of a student dropping out CS studies at the UCLM or graduating, based on data available in an institutional database. Currently, the dropout rate in this degree is around $40 \%$. To do so, we compiled a database of the students enrolled in Computer Science (CS) studies of the University of Castilla-La Mancha (UCLM) in Spain. The database was provided by the UCLM and it contained 383 records with several fields that correspond to both academic and social data of the students enrolled in the CS degree during the courses from 2010 (year in which the degree was implemented) to 2014-2015, including information on whether or not they had abandoned the degree. After the database had been prepared, several BN models were learned to know which features in the currently available data are the strongest predictor of university dropout (Kabakchieva 2013). Then, such models were compared to determine the best classifier and, to it, a total abduction algorithm was applied in order to identify the most probable profile for the student who leaves CS studies.

As a result, what differentiates our work from others is the use of different learning algorithms (supervised and unsupervised) to obtain different Bayesian networks and then compare them with one another to obtain the best classifier. In addition, once identified, our proposal utilises different methods of evidence

propagation to obtain the profile of the student who drops out of CS studies as well as the factors that most influence the prediction of the risk of dropping out.

Therefore, the objective of this paper is twofold:

- On the one hand, to build a model to predict CS studies dropout and find out the dependence relations between the enrolment data of university students, which could explain or shed new light on what motivates them to drop out.
- On the other hand, to propose a methodology in the context of Learning Analytics based on the use of Bayesian networks, which could be applied to similar problems related to the acquisition of information from databases.

The paper is structured as follows: Section 2 presents the theoretical concepts on BN to show how BN can be used in the context of Learning Analytics (LA); Section 3 illustrates the ideas described in the previous sections through a real case study; Section 4 discusses the main results and Section 5 extracts the main conclusions of this work.

# 2. Bayesian networks 

A Bayesian network (Pearl 1988, Castillo, Gutierrez \& Hadi 1997, Jensen 2001) is a probabilistic graphical model that allows of the representation of probabilistic dependence and independence relations between collections of data. It encodes a joint probability distribution over a set of random variables ${ }^{1} \mathrm{X}=\left\{\mathrm{X}_{1}, \ldots, \mathrm{X}_{n}\right\}$ of a problem domain and it is defined in terms of two components (Fernandez et al. 2011):

[^0]
[^0]:    ${ }^{1}$ Capital letters are used to denote variables and lower cases are used to represent the values (also called states) of a variable

- Qualitative component: a directed acyclic graph (DAG), where each node represents a variable and each arc between two variables indicates the existence of a probabilistic dependence between them. In a DAG, nodes are related by connections that describe in an intuitive way the relations of dependence and independence in a set of variables (Castillo, Gutierrez \& Hadi 1997) thanks to the $d$-separation criterion (Pearl 1988).
- Quantitative component: a conditional distribution $p\left(x_{i} \mid p a\left(x_{i}\right)\right)$ for each variable $X_{i}, i=1, \ldots, n$ conditioned on its parents in the graph, denoted as $p a(x)$. Provided that the node does not have any parents in the graph, its distribution is defined by its prior probability $p\left(x_{i}\right)$.

If we consider the independence represented by the network structure, the set of conditional probability distributions specifies a multiplicative factorization of the joint probability ${ }^{2}$ distribution over $\mathbb{X}$ (Pearl 1988; Jensen 2001).

$$
p\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

A BN can be used to reason the situation it models by applying algorithms which are based on the Bayes' Theorem (hence its name). The reasoning process, also known as inference, can be performed in two ways (Pearl 1988):

- Evidence Propagation, which consists in computing the posterior probability distribution of the variables of interest, i.e., the probability distribution over each unobserved variable, given that the value taken by some other variables is

[^0]
[^0]:    ${ }^{2} \mathrm{P}\left(\mathrm{x}_{1}, \ldots, \mathrm{x}_{\mathrm{n}}\right)$ denotes the probability that variable $\mathrm{X}_{1}$ has the value $\mathrm{x}_{1}$.and... and variable $\mathrm{X}_{\mathrm{n}}$ has the value $\mathrm{x}_{\mathrm{n}}$

known. Many inference algorithms have been developed to compute the posterior probability distributions for all the variables (Lauritzen \& Spiegelhalter 1988; Shachter \& Shenoy 1990; Cano, Moral \& Salmeron 2000, Pearl 1988; Shachter \& Peot 1990; Bouckaert, Castillo \& Gutiérrez 1996).

- Abduction, to look for the configuration of a set of variables, called explanation set, which maximize the joint probability given the observed evidence (Pearl 1988). The abduction process is called total or partial depending on whether the explanation set contains every not observed variables or only a subset of them. This process can be generalized to find also the k most probable explanations (Nilsson 1998).


# 2.1. Bayesian network classifiers 

A Bayesian network can be developed manually (Lacave \& Díez, 2003; Millan, Loboda \& Perez-de-la-Cruz 2010), from the specific literature and with the help of experts in the domain to model; automatically, by applying learning algorithms (Neapolitan 2004); or by a combination of them both (Heckerman, Geiger \& Chickering 1995).

The automatic process, also known as learning, consists in taking a database and applying one of the many algorithms that yield both the structure and the conditional probabilities. A Bayesian network learned from a database can be used for classification purposes if it includes the class variable $C$. In this case, the other variables are considered the features and the objective consists in obtaining the posterior probability distribution $\operatorname{Pr}(C \mid \boldsymbol{f})$ over $C$, given case observations $\mathbf{f}$ for the feature variables involved.

Learning algorithms can be of two types:

- Structural learning, by which the structure of the Bayesian network is obtained, that is, the relations of dependence and independence between the variables involved. There are several algorithms to build the network graph from a database, depending on whether or not the structure is fixed. In the first case, the most used fixed structures are Naïve Bayes (NB) (Minski 1963) and TAN (Friedman, Geiger \& Goldszmit 1997). The NB classifier assumes that all feature variables are mutually independent, given the class variable. Although this naïve assumption does not generally hold in practice, NB classifiers tend to show quite competitive performance. TAN classifiers allow for explicitly representing the dependence among the feature variables by a free structure, and in essence may thereby outperform NB classifiers. Alternatively, when the structure is not known, the best-known algorithms for obtaining it are K2 (Cooper \& Herskovits 1992) and PC (Spirtes, Glymour \& Scheines 1993). The K2 algorithm attempts to find an optimal network in terms of the likelihood of the database for each candidate network. In contrast, the PC algorithm tries to determine the structure of the network through statistical tests of independence.
- Parametric learning: provides the quantitative component of the Bayesian network defined by a given structure, i.e., the probability distribution associated with it. The parameters in this case are obtained by maximum likelihood estimation or by EM algorithm (Dempster, Laird \& Rubin 1977).


# 2.2. BN as 'white boxes' in Learning Analytics 

Bayesian networks classifiers are a powerful tool to be used in the context of Learning Analytics (LA) due to several reasons. Firstly, a BN provides a compact way of extracting knowledge from the application of learning methods, allowing also of the

combination of the knowledge given by a human expert with the data collected in a database, even if these data were incomplete.

On the other hand, one of the main drawbacks of the methods commonly used in data mining is that they are difficult to interpret because they act as 'black boxes', providing results without explanation. This trouble can lead to the lack of confidence by the user, which complicates decision making in any field, and to the inability of users to validate it (Xing et al. 2015). However, one of the most important advantages of BN classifiers in the context of Learning Analytics is that the structure of the associated DAG of a BN permits, in an intuitive way, the comprehension of the relations of dependence and independence that exist in a set of variables, even if the user does have any knowledge about artificial intelligence (Castillo, Gutiérrez \& Hadi 1997). If two variables are dependent, this relation can be represented by a path that connects these nodes; alternatively, if two variables are independent, then there should be no way to join these nodes. In this context, the concept of dependence between variables is related to the concept of connection between nodes. Thus, it is possible to find out, with no need of carrying out any numerical calculations, which variables are relevant or irrelevant for some other variable of interest (for instance, a prediction indicator). This process is also known as relevance analysis (Fernandez et al. 2011) and it is very useful to really understand how information is transmitted in these models.

Moreover, BN provide flexible methods of reasoning, and well-founded on probability theory statistically robust enough, capable of providing meaningful results, predicting the value of unobserved variables and explaining the observed ones.

# 3. Case Study 

This section illustrates, through a real case study, how the automatic development of BN from a data collection can be used to address the analysis of CS dropout at the University of Castilla-La Mancha.

### 3.1. Data collection

The UCLM office provided us with a database containing 383 records representing both academic and social data of the students enrolled in the Degree in Computer Science Engineering (DCSE), taught in the Campus of Ciudad Real of the UCLM, from the courses 2010-2011 to 2014-2015, including information about whether each student dropped out. These records do not correspond to a sample of the students, but they represent all the students enrolled in the CS studies during the study period. This database has been created by the Office of Planning and Quality of the UCLM from the form that students fill out to formalize their university registration and each record is structured in the following sixteen fields:

- GENDEK (G), with values Male (M) and Female (F).
- ENROLLEMENT_ $A G E(E A)$, defining the age of the student when they enrolled in the CS studies
- PRIOR_CHOICE (PC), representing the order in which the student chose the Degree of Computer Engineering among all those selected. It has values ranging from 1 to 5 as well as the value UNKNOWN.
- FIRST_ENROLLMENT_YEAR (FEY), defining the first year among 2010 and 2014 the student enrolled in CS studies.

- KIND_ACCESS_UNIV (KAU), defining the way of access to Spanish university: Professional Training (PT), Validation of foreign studies (FOR), university entrance examination (UEE), access examination for people aged over 25 (OLD25), Technical Engineers (TE) and Graduates (GR). The database also contains the value UNKNOWN.
- GRADE_ACCESS (GA), to define the access mark to university, if it applies
- SCHOLARSHIP (SS), with values 1, 0 and 2 to represent, respectively, whether or not the student has had a scholarship, or this information is not known.
- HIGHEST_COURSE_ENROLLED (HYC), with values ranging from 1 to 4, representing the highest course in which the student is enrolled
- \#ENROLLED_SUBJECTS (\#ES): Total number of subjects enrolled, being 40 the maximum number of subjects to pass.
- \#PASSED_SUBJECTS (\#ES) and \#FAILED_SUBJECTS (\#FS): Idem for passed and failed subjects, respectively.
- \#MAX_CONV (\#MC), with values ranging from 0 to 7 , representing the maximum number of times that a student has failed the final examination of the same subject for any subject of the degree.
- WORK (W), to know whether the student has been working during their studies. It has the values NO, PARTIAL, FULL and UNKNOWN, representing, respectively, that the student has not worked, that they have worked at partial time or at full time, and that the information is not known.

- FATHER_STUDIES (FS) and MOTHER_STUDIES (MS): defines the student's father and mother level of studies, respectively, with values NONAPPLIES (when it is unknown), NO_STUDIES, PRIMARY, SECONDARY and HIGHER.
- FAMILY_PROVINCE (FP), with values Ciudad Real and OUT, representing whether or not the province where the student's parents live is Ciudad Real (the one where DCSE studies are taught).
- DROPOUT (D), with values YES and NO, to define if the student has left their studies or, on the contrary, they have graduated.


# 3.2. Automatic modelling of the Bayesian network 

To address the main goal of our research work, several Bayesian networks were developed to model the relationships between the data represented in the database related to the aim of performing a relevant analysis to identify the main factors involved in the student who leaves their CS studies.

### 3.2.1. Database preparation

First, one variable was defined for each of the sixteen fields in the database. One of the main problems of BN is that the excess of granularity in the definition of the values of the variables can increase the computational complexity of the algorithms. Hence, as a previous step, some variables with many values were subjectively simplified such as those related to the age of the student, the number of subjects they passed, failed or in which they enrolled, grouping their values into the following intervals:

- ENROLLMENT_AGE (EA): [18,19], [19,20], [21,25], [26,30], [>30] and UNKNOWN.
- GRADE_ACCESS (GA): [5,6), [6,7), [7,8), [8,9) and [9,10].
- \#ENROLLED_SUBJECTS (\#ES): [1-5], [6,10], [11,20], [21,30], [31,40].
\#PASSED_SUBJECTS (\#PS) and \#FAILED_SUBJECTS (\#FS): [0], [1-5], [6,10], $[11,20],[21,30],[31,40]$

Once the database was prepared according to the previous definition of variables, several BN were developed in a sequential process and afterwards, they were compared both empirically and conceptually, with the aim of making informed choices (Culbertson 2016). Although different programs can be used to learn Bayesian networks from a database, this case study has been carried out with the Elvira program (Elvira Consortium 2002) mainly because it is a free software package, implemented in Java (therefore it runs on several platforms), which provides advanced explanations of the modelled domain and the reasoning performed in the network (Lacave, Luque \& Díez 2007, Ropero, Rénóoij \& Van der Gaag 2018, Molina-Serrano et. Al 2017). The program is the result of a joint project between several universities and it has been developed in a multidisciplinary way and for specific research purposes; as a consequence, Elvira has a very large collection of Bayesian network algorithms, implemented in Java, thus it can run on different platforms and contexts.

# 3.2.2. Fixed structure 

Initially, the first aim of this work was to predict the likelihood abandoned studies according to the evidence known about a student. Hence, a Naïve Bayes (NB) classifier was developed defining DROPOUT as the dependent variable and the rest as predictors,

obtaining the BN shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Naïve Bayes model representing all the variables of the database obtained with the Elvira program.

It can be seen that, in the absence of evidence, the probability that a student left DCSE studies is $0.64(64 \%$ of the records in the database correspond to students who left university). The NB graph specifies that dropout depends on the rest of the variables of the database and that all the predictor variables are independent of one another. This model also specifies some interesting information through the link colour and thickness because in Elvira, the type of dependence between the variables is exposed by the colour and thickness of the links (Lacave, Luque y Díez 2007). The thickness of each link is proportional to the influence that each node transmits to another and the red (or darker) colour represents positive probabilistic dependence, that is, the greater the values the parent takes, the higher the probability of the child taking greater values. For example, the red link to $E A$ reflects that the greater the student, the more likely he will be to drop his studies. The blue link to $\# P S$ reflects that the more subjects he has passed, the less likely he is to drop out.

After studying the graphical model, we noticed that several predictor variables may not be completely independent. Thus, a TAN algorithm was applied to represent that dependence amongst variables. The resulting BN is illustrated in Figure 2. The learned TAN model shows some reasonable dependence, as for instance, from $\# E S$ to $\# P S$.
![img-1.jpeg](img-1.jpeg)

Figure 2. TAN model representing all the variables of the database obtained with the Elvira program.

Because of such differences between the obtained results, considering also the many dependence relations amongst the predictor variables, we decided to build a prediction model, although not imposing any fixed structure to the learning algorithm.

# 3.2.3. Unfixed structure 

In this stage, the K2 algorithm was applied to learn a BN from the database, obtaining the BN depicted in Figure 3. It can be observed that the $G, W$ and $F P$ variables are independent of the rest which means that they do not provide any information to any variables. Furthermore, the studies dropout depends directly, on the number of passed subjects and the highest year coursed, and indirectly, on the mark obtained to access university, the age of the student and the kind of access to university.

![img-2.jpeg](img-2.jpeg)

Figure 3. BN learned after applying K2 algorithm using the Elvira software

Still, we decided to use the PC algorithm to learn a new model, shown in Figure 4. The relations graph and the prior and posterior probabilities were different from the ones obtained with the K2 algorithm. In this PC model, the variable DROPOUT depends only on the number of passed subjects and whether or not the student is working during their studies.

![img-3.jpeg](img-3.jpeg)

Figure 4. BN learned after applying PC algorithm using the Elvira software

# 3.3. Model evaluation 

The assessment of the functionality of a BN is critical regardless of whether the model was built for description, classification or prediction. When data are available, the comparison of predicted values with actual values is the most straightforward way to discern the predictive accuracy of a model; unfortunately, this is not the case and some other methods must be used.

When BN are developed by a learning process, several fit measures are used (Marcot 2012), although /cold-cross-validation is often used when there is no explicit set of test data. It involves randomly splitting cases into $k$ equally sized partitions, cross-validating each partitioned sample across the remaining partitions, and then averaging predictive performance across all the partitions. The main advantage of $k$-fold cross validation is that it allows for the use of as much training data as possible while protecting against model over fit and providing measurements of predictive performance (Corey 2016). It is recommended that $k$ take a value between 5 and 10 to address the 'bias/variance' dilemma (Geman, Bienenstock \& Doursat 1992), in which the minimization of potential bias and prediction error created by an inappropriate data

split competes with the minimization of variance that is created by using a number of training sets to estimate the parameters of a model (Hastie, Tibshirani \& Friedman 2009).

Hence, the qualifying accuracy of the models obtained in the previous section were compared by 5 -fold and 10 -fold cross validation (given the limited amount of cases) using the Elvira program. Table 1 shows the values obtained for the logarithm of the probability score which allows of the conclusion that there is no significant difference amongst the results of cross validation considering 5 or 10 iterations, probably due to the limited sample size. In any case, K2 has better learning performance than the others, as it has also been found in other works in the educative context (Fernandez et al. 2011; Oviedo 2016). Also, TAN model has a very good behaviour, however NB has the worst. This contradicts other previous research (Er 2012) which seems to indicate that the assumption of independence between predictor variables in the case of study presented in this work is not correct.


Table 1. Log-likelihood score with 5 -fold and 10 -fold cross validation.

In addition to evaluating the predictive performance and sensitivity of a model, a final evaluative measure involves considering model complexity (Corey 2016) as part of a holistic evaluation of single models. Complexity can be measured by the number of

variables, links and node states, and is typically used for comparing different models (Marcot 2012).

The complexity of the learned structures can be measured by the number of links that appear in each graph, shown in Table 2. It can be seen that the most complex model is that obtained by the TAN algorithm and the simplest model is provided by the PC algorithm. However, as Figure 4 shows, the graph does not reflect every dependence amongst variables, undoubtedly because the database does not have enough number of records to identify, through the PC algorithm, all those relations. With respect to the K2 and NB models, although both have a similar number of links, the K2 graph is easier to understand and more intuitive since there are fewer crosses between edges.


Table 2. Most probable configuration for students who drop out and its probability in K2 model.

Thus, given the obtained results and taking into account that the objective of this research work is not only to get a good classification model, but also to identify the relationships between data in the database that explain the DCSE studies dropout, it can be concluded that the best model that explains this is the Bayesian network learned through the K2 algorithm (Figure 3), which is consistent with other previous works (Fernandez et al. 2011; Oviedo Bayas 2016; Oviedo, Moral \& Puris 2016).

# 4. Results and discussion

First, the work conducted has shown that it is necessary to compare different classifiers before deciding which one is the best that fits the stated objective, as it has already been stated (Nikolovski et al. 2015; Culbertson 2016).

# 4.1. Significant findings 

Once it has been determined that the best model which fits the database is K2 BN (Figure 3), some interesting findings can be extracted from the model structure, most of which had not been identified in previous research:

- The gender, the fact of being working and the family's residence province are not relevant factors affecting the probability of leaving DESE studies. This fact makes sense because, in the case of gender, $82 \%$ of the students in the enrolment database; regarding work, only $8 \%$ of the students have a part-time or full-time job; and with respect to family province, $80 \%$ lives in Ciudad Real.
- The risk of abandonment depends directly on the number of subjects passed by the student and on the highest course taught by the student, being these factors dependent upon the student's age of enrolment. Therefore, the likelihood of dropping out also depends on the student's age of enrolment.
- The number of subjects passed by the student and the highest course taught by the student-make dropout independent from the rest of the variables in the BN. This means that once we know the number of subjects passed by the student and the highest course taught by a student, the rest of the factors represented in the BN do not provide any information to the risk of abandonment of the student. Hence, these two factors seem crucial for dropout prediction, which is completely coherent with reality.

- The risk of leaving studies and the mark obtained by the student to access university are probabilistically dependent although they become independent when the highest course in which the student is enrolled or the number of passed subjects is known. This means that if one of these two factors is known, the mark obtained to access university does not provide any information to predict the risk of abandonment of DCSE.
- In addition, the likelihood of dropping DCSE depends on the maximum number of times that a student has been examined in any subject. These variables become independent after knowing the number of passed subjects. This means that if the number of subjects passed by the student is known, the number of times that the student has been examined in any subject does not provide information to predict the risk of abandonment of DCSE.
- The number of passed subjects depends not only on the number of enrolled subjects, but also on the highest course in which the student is enrolled, which makes sense.
- The negative relation (blue link) between the student preferences and their father studies indicates that the more priority the DCSE (lower order) in the student's choice, the higher the level of studies of their father. Since there is a positive relation (red link) from $F S$ to $M S$, it can be concluded that the more priority the DCSE in the student's choice, the higher the level of studies of their parents.


# 4.2. Obtaining more information from the classifier model 

On the other hand, with the purpose of making some predictions and in order to identify the relevance of certain factors, we have performed some evidence propagation over K2 BN.

- In the first case, the aim was to estimate the likelihood of dropout of a student aged 18, who chose DCSE in fifth position (the last one), accessed university with a mark of 8 and they do not know yet whether they will receive a scholarship.
![img-4.jpeg](img-4.jpeg)

Figure 5. Example of evidence propagation over K2 network to predict the likelihood of dropping out.

Figure 5 shows the result of the after having fixed as evidence $\mathrm{E}=\{E A=18$, $P C=5, G A=8, G=2\}$. The background colour of known variables is set in grey and its known values are highlighted in red. As a result, it was obtained that the probability of not dropping out ( 0.57 ) is greater than dropping out ( 0.43 ).

Nonetheless, this result is different if the $G A$ value is changed to 5 , then the

probability of dropping out (0.82) is greater than not dropping out (0.18). If $E A$ is changed to a value between 21 and 25 , the probability of dropout slightly increases to 0.84 . On the contrary, if the order of choice is changed to 1 , the probability of dropout remains unchanged. This is because the $G A$ and $E A$ variables make $D$ and $P C$ independent, which implies that knowing the enrolment age of the student and the mark obtained in the university access examination, the order of choice does not provide any information about the risk of dropping out studies. This example illustrates that the mark obtained in the Spanish University Entrance Examination and the enrolment age of the student are very relevant factors to predict dropout when there is only known information about age, access mark, grant and the studies order of choice.

- It has also been analysed, thanks to the 'why' and 'how' explanations provided by Elvira for an evidence case, which of both factors is more relevant in dropout prediction, calculating the kind and the amount of evidence that each finding applies to other certain variable. Figure 6 shows both the joint probability of the findings $\{E A=21-25, E A=8\}$ and also the kind and amount of influence that each one exerts on the target variable DROPOUT.

![img-5.jpeg](img-5.jpeg)

Figure 6. Explanation provided by the Elvira program of the effect that each finding of evidence $\mathrm{E}_{4}=\{E A=21-25, G A=8\}$ has on the probability of DROPOUT variable, as well as the probability of evidence.

With that aim, different evidence cases have been defined with different configurations for both variables, all of them summarised in Table 3. The rows represent evidence cases and, regarding columns, the first one shows an evidence case identifier, the next six columns are for the value and the kind and amount of evidence of each variable (the first three for $E A$ and the other three for $G A$ ) on the focus variable $D$, the seventh column contains the probability of each evidence case and, the last column, the probability of $D$ being equal to YES, given the evidence.


Table 3. Some sensitivity analysis of $E A$ and $G A$ variables on DROPOUT variable, showing the kind and the amount of influence that each finding exerts on the interest variable, as well as the probability of evidence and probability of the DROPOUT variable given such evidence.

For example, the propagation of evidence case $\mathrm{E}_{1}=\{E A=18, G A=8\}$, with $\mathrm{P}\left(\mathrm{E}_{1}\right)=0.016$, produces a decrease in the probability of dropping out, obtaining that $\mathrm{P}\left(D=\mathrm{YES} \mid \mathrm{E}_{1}\right)=0.420$. This is because both findings have a negative impact on the DROPOUT variable although the effect that exerts the finding about the mark is greater than that exerted by the age. When propagating the evidence case $\mathrm{E}_{2}=\{E A=18, G A=5\}$, with $\mathrm{P}\left(\mathrm{E}_{2}\right)=0.08, \mathrm{P}\left(D=\mathrm{YES} \mid \mathrm{E}_{2}\right)=0.823$, the probability of $D$ has increased because the effect that exerts the finding about the mark is positive and that exerted by the age is almost null. This table summarises the results provided by Elvira when explaining an evidence case and reveals that findings do not exert the same kind or amount of influence upon the same variable in different evidence cases. For example, in Table 3 it can be seen that the kind of influence of finding $G A$ on $D$ in $\mathrm{E}_{1}$ is negative and greater than the positive influence of $E A$; nonetheless, in $\mathrm{E}_{4}$, the influence of $G A$ is negative and lower than the positive influence of $E A$.

![img-6.jpeg](img-6.jpeg)

Figure 7. The paths by which evidence flows from findings $E A$ and $G A$ to $D$. Furthermore, the expanded node DROPOUT shows graphically the variations in its probabilities that it has suffered during the propagation of each evidence case of Table 3 .

Figure 7 shows graphically how the $E A$ and $G A$ variables transmit their influence on variable $D$. It can also be seen, in the DROPOUT variable, how its probabilities have changed as each evidence case has been propagated.

# 4.2. Dropout profile 

The dropout profile corresponds to the most probable configuration, which can be obtained by applying an abduction algorithm to the K2 network after setting as evidence $\mathrm{E}=\{D R O P O U T=$ YES $\}$. In this case, the most probable configuration, with a probability of 0.000007 , corresponds to a male (M) aged 18, who elected DCSE studies as his first choice and accessed university through the Spanish University Entrance

Examination with a mark of 5, having benefited from a scholarship. The highest course he took was 1 st and he enrolled in between 6 and 10 subjects, however he did not pass or fail any, because he probably dropped out before the final examinations. In addition, the values of variables $W, F S$ and $M S$ are all the same: 'UNKNOWN'. This may be because $70 \%$ of records in the database have the unknown value in the work field, and $35 \%$ in the parent studies fields. Moreover, the low probability of the configuration obtained reveals a great heterogeneity of the data.

# 5. Conclusions 

Bayesian networks provide a compact way of representing knowledge and adequate methods for the interpretation and contextualization of data without the necessity for advanced statistical knowledge. Hence, Bayesian networks can be considered appropriate models to be used in the context of Learning Analytics.

In this paper, we have addressed the analysis of the CS studies dropout in the UCLM by using Bayesian networks, and the process of data preparation has constituted a decisive task to obtain a model good enough. This model has been obtained after comparing several networks developed automatically through the application of the most known learning algorithms (Naïve Bayes, TAN, K2 and PC). The comparison of the learned networks has been performed by 5 -fold and 10 -fold validation and we have observed that the K2 algorithm provides the BN which fits best data.

### 5.1. Main Findings

K2 model provides the following significant results about CS dropout with respect to the research conducted so far:

- The number of subjects passed by the student and the highest course in which they are enrolled are crucial factors to predict dropout.

- The mark obtained in the Spanish University Entrance Examination is a very relevant factor to predict dropout when it is only known basic enrolment information about the student, such as their age, whether they have a scholarship and the studies order of choice is known. When the highest course in which the student is enrolled or the number of passed subjects is known, the mark obtained to access university does not provide any information to predict the risk of abandonment of DCSE.
- The maximum number of times can be used to predict dropout only if the number of passed subjects is unknown. On the contrary, if the number of passed subjects of the student is known, the number of times that the student has been examined in any subject does not provide information to predict the risk of abandonment of DCSE.
- The gender is not a factor that affects abandonment, nor the student's family residence province or whether the student is working while studying.
- The most probable profile of the dropping out student corresponds to a male aged 18, who chose DCSE studies in $1^{\text {st }}$ position and accessed university through the Spanish University Entrance Examination with a mark of 5, having benefited from a scholarship. The highest course in which he was enrolled when he dropped out was 1st as the was enrolled in between 6 and 10 subjects, although he did not pass or fail any.


# 5.2. Limitations and Future Research 

As the information provided about each student is very limited in the current database, it would be desirable to have more information from every enrolled student to be able to consider more factors when studying the problem of dropout using the approach of learning analytics.

Furthermore, the greater the number of records in the database, the more accurate the learned model. In fact, the great heterogeneity of the data studied, given the limited sample size, did not permit the adjustment of the dropout profile of student too accurately.

Thus, we are working on the preparation of a larger database, in terms of the number of both fields and records. In the first case, we want to include different types of information for each subject such as number of teachers, number of groups, number of students per group, language of instruction, evaluation method, etc. In order to increase the number of records, we wish to collect information from all centres of the university where the CS studies are taught, as well as on other Spanish universities over the last few years. Once we have prepared the database, the objective in the near future will be to replicate the experience described in this manuscript, taking as a reference the methodology described here, and compare the results.
