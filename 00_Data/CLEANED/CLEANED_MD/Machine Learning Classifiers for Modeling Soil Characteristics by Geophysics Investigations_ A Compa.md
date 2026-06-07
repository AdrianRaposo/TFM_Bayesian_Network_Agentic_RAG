# Article 

## Machine Learning Classifiers for Modeling Soil Characteristics by Geophysics Investigations: A Comparative Study

Chee Soon Lim ${ }^{1}$, Edy Tonnizam Mohamad ${ }^{1}$, Mohammad Reza Motahari ${ }^{2}$, Danial Jahed Armaghani ${ }^{3, *}$ and Rosli Saad ${ }^{4}$<br>1 Geotropik-Centre of Tropical Geoengineering, School of Civil Engineering, Faculty of Engineering, Universiti Teknologi Malaysia, Skudai 81310, Malaysia; geotropik@utm.my (C.S.L.); edy@utm.my (E.T.M.)<br>2 Department of Civil Engineering, Faculty of Engineering, Arak University, 38156-8-8349 Arak, Iran; M-Motahari@araku.ac.ir<br>3 Institute of Research and Development, Duy Tan University, Da Nang 550000, Vietnam<br>4 Geophysics Section, School of Physics, Universiti Sains Malaysia, Pulau Pinang 11800, Malaysia; rosli@usm.my<br>* Correspondence: danialjahedarmaghani@duytan.edu.vn

Received: 21 July 2020; Accepted: 15 August 2020; Published: 19 August 2020


#### Abstract

To design geotechnical structures efficiently, it is important to examine soil's physical properties. Therefore, classifying soil with respect to geophysical parameters is an advantageous and popular approach. Novel, quick, cost, and time effective machine learning techniques can facilitate this classification. This study employs three kinds of machine learning models, including the Decision Tree, Artificial Neural Networks, and Bayesian Networks. The Decision tree models included the chi-square automatic interaction detection (CHAID), classification and regression trees (CART), quick, unbiased, and efficient statistical tree (QUEST), and C5; the Artificial Neural Networks models included Multi-Layer Perceptron (MLP) and Radial Basis Function (RBF); and BN models included the Tree Augmented Naïve (TAN) and Markov Blanket, which were employed to predict the soil classifications using geophysics investigations and laboratory tests. The performance of each model was assessed through the accuracy, stability and gains. The results showed that while the BAYESIANMARKOV model achieved the highest overall accuracy ( $100 \%$ ) in training phase, this model achieved the lowest accuracy ( $34.21 \%$ ) in testing phases. Thus, this model had the worst stability. The QUEST had the second highest overall training accuracy ( $99.12 \%$ ) and had the highest overall testing accuracy ( $94.74 \%$ ). Thus, this model was somewhat stable and had an acceptable overall training and testing accuracy to predict the soil characteristics. The future studies can use the findings of this paper as a benchmark to classify the soil characteristics and select the best machine learning technique to perform this classification.


Keywords: soil classification; tree-based models; geophysics investigation; P-wave; S-wave; laboratory testing

## 1. Introduction

The seismic P- and S-waves downhole logging method is capable of determining and measuring the distribution and physical properties of soil adjacent to a borehole annulus. In this method, a number of sensors (P- and S-wave geophones) are positioned at different interval depths within the borehole, whereas the seismic source is situated upon the ground surface. The speed of the P-wave movement is higher than that of the S-wave. The advantage of P-wave is that ground water cannot affect its propagation velocity mostly in soil material, hence resulting in a higher precision level [1].

The measurements can be recorded as physical phenomena. Moreover, the artificial physical sources, e.g., electrical and nuclear sources, can be used for the purpose of perturbing the medium and measuring the perturbation response. A number of parameters such as density, orientation, porosity, and lithology of soil in the neighboring area of the borehole (i.e., the physical properties) can be measured through analyzing the available data. In definition, geophysical logging refers to non-disruptive in-situ physical properties of soil [2]. Directly measuring the soil stiffness in situ causes the minimization of material disturbance [1]. In Geotechnics, a key measure in site characterization is to determine the seismic wave velocity [3]. The P- and S-wave velocities are applicable to the calculation of basic elastic material properties, such as the soil bulk modulus and shear modulus. To effectively evaluate the seismic ground motions, these parameters cannot be overlooked [4]. The materials of P-wave velocities can be assessed from field and laboratory observations [5,6]. In addition, a comparison was made between the obtained values of the P-wave velocity $(V p)$ and parameters such as density, the SPT-N values, velocity index, and friction angle. Remember that the shear wave velocity (S-wave, Vs) in soil is dependent upon different parameters, such as the soil type, confining stress, and level of the soil compaction [7]. However, no adequate attention has been paid to the effects of some other parameters like the size and shape of soil material upon Vs. Such parameters mainly affect the delegation of the applied normal stress of the soil; this way, they have a direct impact on the Vs magnitude. According to a number of previously conducted studies in this field, the bender elements can be effectively used in determining Vs in different types of materials, e.g., sand, and glass beads. A number of empirical equations in granular materials were proposed by to predict Vs on the basis of size, shape, and the confining stress of material under dry and saturated conditions (e.g., [7]).

Formerly, to determine the seismic wave velocity, most researchers and practitioners have made use of the seismic surface refraction and reflection methods. Since borehole receivers emerged and seismic shear wave sources were developed, borehole seismic wave velocity logging methods received more attention. A method that can be simply used to produce seismic shear waves is wooden plank hammering. This technique uses a hammer as energy source at the surface to impact a wood plank and generates shear waves. This is typically accomplished by coupling a plank to the ground near the borehole and then impacting the plank in the vertical and horizontal directions. It can obtain the shear waves that are detectable through the use of downhole receivers. Such receivers are able to effectively measure downhole Vs. Receivers (geophones) are applicable to logging the waves that are generated by seismic shear wave sources in hundreds of meters depths [4]. Table 1 gives a summary of the seismic borehole methods proposed in literature to measure seismic velocity [4,8]. The methods are the up-hole seismic, downhole seismic, suspension seismic, and cross-hole seismic. These methods are also called PS logging since the measurement of both compression wave $(V p)$ and shear wave $(V s)$ can be done at the same time [9].

Table 1. The preliminary selected list of downhole geophysical methods.


* Only when the hole is filled with fluid; ++ PVC casing.

Geophysical results can be used to identify or describe soil properties in different layers. Normally, soil properties and subsequently soil classifications are measured/identified in a laboratory. However, sample preparations and doing the relevant tests in a laboratory are costly and time consuming [10]. For that reason, indirectly classifying soil through the use of geophysics results has received much attention from the academic community. In the geophysics field, the novel computational techniques are faster, easier to carry out, and more precise in comparison to theoretical/empirical techniques [11]. Recently, many researchers in science and engineering fields have made use of soft computing and machine learning (ML) techniques [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]. In addition, lots of these techniques have been

adopted by different scholars in geophysics and geotechnics [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]. Concerning the classification of soil characteristics, several ML techniques were adopted by various studies. The Support Vector Machine (SVM) was the most frequently used technique to classify the soil attributes. Multiple types of SVM including Linear, Gaussian, Polynomial, and Radial Basis were utilized for soil type classification [10,50,51,52,53,54,55,56]. Furthermore, several types of Decision Trees (DTs), including the Classification and Regression Decision Tree (CART), J48, Random Forest (RF), Bagged trees, and gradient boosting trees were adopted to classify soil characteristics [51,52,57,58]. Some studies also applied the Artificial Neural Network (ANN) and its variants [51,52] for classifying the soil characteristics. Based on the mentioned studies, it seems that soft computing and ML techniques are able to map a proper, simple, applicable, and accurate way for soil characterizations/classifications.

While the studies above signify essential contributions to the application of ML in soil classification research, they also have some significant limitations. These studies deal only with a limited set of ML classifiers, though the number of possible classifiers is large. Advanced DT techniques such as Chi-Square Automatic Interaction Detection (CHAID), Quick, Unbiased, and Efficient Statistical Tree (QUEST), and C5 have not been considered in a comparative study; however, it has been shown that these DTs can generate highly accurate results for many applications. Some variations of ANN, such as the Radial Basis Function (RBF), have been overlooked to classify the soil characteristics. Besides, the probabilistic techniques such as the Bayesian Network (BN) and its variants have not been adopted in soil classification research. This study attempts to employ different types of prediction models, including DT, ANN, and BN, to classify the soil types. To this end, six input variables, including $\mathrm{V}_{\mathrm{p}}$, $\mathrm{V}_{\mathrm{s}}$, Moisture content, Liquid Limit (LL), Plastic Limit (PL), and specific gravity of soils (Gs), were taken into consideration. Four DT algorithms, including CART, CHAID, QUEST, and C5; two ANN models, including Multi-Layer Perceptron (MLP) and RBF; and two BN algorithms, including Tree Augmented Naïve (TAN) and Markov Blanket were used. The performance of the models employed was assessed through the overall accuracy of each model, the recall and precision of each classifier, and for each soil characteristic and gain.

In the following, background of machine learning models together with some descriptions related to case studies, field investigations, and laboratory tests will be given in Section 2. Then, Section 3 describes modeling procedures and their results in determining soil classifications. In addition, this section will discuss results of models' stability and the importance of variables. Finally, in Section 4, discussion and conclusions regarding the model results will be given.

# 2. Materials and Methods 

The present study used and applied three types of ML algorithms, i.e., Decision Trees (DTs), Artificial Neural Networks (ANNs), and Bayesian Networks (BNs). It employed eight models to classify soil characteristics. For DTs, the authors adopted Chi-Square Automatic Interaction Detection (CHAID), Classification and Regression Trees (CART), Quick, Unbiased, and Efficient Statistical Trees (QUEST), and C5. The ANN models employed included ANN-Multi Layer Perceptron (ANNMLP) and ANN-Radial Basis Function (ANNRBF). Concerning the BNs, the authors applied the BN-Tree Augmented Naïve (BAYESIANTAN) and Bayesian Networks Markov Blanket (BAYESIANMARKOV) methods to the data. In the followings, some brief explanations are provided for the characteristics of each model used.

### 2.1. Description of DT Algorithms

Kass [59] developed the CHAID that is known as a data mining algorithm. Then, a DT model was grown by CHAID through performing a number of sequential combinations and splits on the basis of the Chi-Square test. In fact, CHAID is a tree-based structure technique that has been made by combining a group of rule classifiers. In this technique, for predicting the independent parameter, there is need to form a tree structure of the dependent parameters. The accuracy level of the rules formed in the previous step is denoted by the ratio of records holding the specific value for the target variable to the values given for the independent variables. Another CHAID objective is the generation

of wider and non-binary trees. In addition, for the overfitting avoidance purpose, this algorithm prunes DT in an automatic way.

Breiman [60] developed the CART model as a binary DT applicable to modelling purposes. The CART objective is exploring the optimal split. In case of different variables types, CART can be used to classify the input variables values ordering from smallest to largest ones. This technique makes a trial split in aiming at determining the best split point; for example, in case the call split point is termed "S", all the cases with a value smaller than "S" will go to the left, which forms the child node ( $\mathrm{X}<\mathrm{S}$ ); otherwise, the instances will be sent to the right child node $(X>S)$. CART makes attempts to decrease the leaf nodes' impurity level in such a way that the best data partition could be selected. In CART, three potential indices are taken into account to choose the best data partition: Gini criterion entropy, and Twoing criterion. The selection of the above-noted indices has a significant effect on the performance of CART. In other words, selecting the best indices will result in achieving the best predictive performance.

The QUEST was developed by Loh and Shih [61]. This algorithm addresses variable selection bias issues, particularly the exhaustive-search method that is used in CART. The QUEST selects each splitting variable and its associated split value sequentially instead of simultaneously. This algorithm employs several statistical tests, including overall level of significance, p-value, and F-test to determine the splitting variable at a particular node.

The C5 algorithm is an improved and commercialized version of C4.5 which was developed by Quinlan [62]. C4.5 can be used for both continuous and categorical target variables. This algorithm creates binary splits on continuous variables and multiway splits on categorical variables. Additionally, a heuristic searching strategy is employed by C4.5 for variable splitting. Regarding the splitting criterion, the C4.5 uses an impurity measure, such as gain ratio. A C4.5 tree size is controlled using a pessimistic pruning strategy. Finally, the missing data in C4.5 are handled by adding a new level to the tree. While the C5 inherits the characteristics of the C4.5, this algorithm offers several enhancements to C4.5, such as the ability to specify unequal misclassification costs, the application of fuzzy splits on continuous variables, and boosting trees.

# 2.2. ANN Algorithms 

ANN is a variety of artificial intelligence that simulates functions of the human brain. In general, ANN aims at classifying experiential knowledge [63]. In this method, there is a set of layers, each of which is contained a chain of neurons. In each layer, the neurons are connected through weighted links [63,64,65,66,67,68]. It worth noting that the excitatory associations are indicating by positive weights, and the inhibitory associations are showing by negative weights [69]. A typical ANN structure in which there are three layers, including the input layer, hidden layer, and output layer that is able to do process of feed forward and error propagation, is presented in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. A typical structure of Artificial Neural Networks (ANN).

ANN has two major classes, including Multilayer Perceptron (MLP) and Radial Basis Function (RBF). MLP is a kind of feedforward ANN. Typically, an MLP contains at least three layers of nodes, including an input layer, a hidden layer, and an output layer. In general, each node (except the input nodes) is assumed as a neuron that utilizes a non-linear activation function. Besides, MLP employs a supervised learning technique known as backpropagation to train the model. Various layers and non-linear activation of MLP distinguish this model from the linear perceptron. MLP is capable of distinguishing not linearly separable data. The RBF is a kind of ANN which employs radial basis functions as functions of activation. The network's output is a linear combination of radial basis functions of the inputs and neuron parameters.

# 2.3. BN Algorithms 

Bayesian Network (BN) is a non-parametric model that represents multivariate probability distributions in the form of a directed graphical model [70]. In a BN model, a set of random variables is represented by the network's nodes, as well as the causal relationships between variables denoted by directed arcs. Each conditional probability distribution is associated with a node that quantifies the influences the parents of the node have on it. It worth noting that a BN model denotes the casual relationships between nodes; however, the arcs in the network do not necessarily denote direct cause and effect. The Naïve Bayes is the simplest form of the BN model. The Naïve Bayes has two basic assumptions as follows: (1) all other input variables are conditionally independent of each other given the target variable and (2) all other input variables are directly dependent on the target variable. However, these assumptions are unrealistic [71]. To relax the first assumption and achieve better performance over the Naïve Bayes, the Tree Augmented Naïve Bayes (TAN) approach was introduced by Friedman, et al. [72]. TAN employs a tree structure, in which each input variable only depends on the target variable and one other input variable. In order to implement the classification, the TAN uses a maximum weighted spanning tree that maximizes the probability of the training data [73] (Figure 2a). According to Madden [71], creation of a complete BN model for classification may be computationally ineffective because the full structure may not be related to classification. To identify all input variables in the network that are required to predict the target variable and remedy the abovementioned issue, Markov Blanket Networks were proposed by Pearl [74]. Indeed, the Markov Blanket chooses the set of nodes in the dataset that include the target variable's parents, its children, and its children's parents (Figure 2b).
![img-1.jpeg](img-1.jpeg)

Figure 2. Structures of Tree Augmented Naïve (TAN) and Markov Blanket Networks.

### 2.4. Case Study and Data Collection

Investigations required for this research were carried out at three sites in Metro Manila, Philippines, which are prone to earthquake occurrence. The sites were Las-Pinas, Katipunan Avenue, and Bulacan,

which belong to regional bedrock of the area namely Guadalupe Tuff Formation (GTF). Basically, the GTF consists of essentially horizontal interlayer of elastic sediment often tuffaceous (sandstone, siltstone and shales) and characterized by horizons of residual weather products (Figure 3). The compressive strength of specimens from different layers classify the components of the GTF varies from very dense/stiff soil to very soft rock with typical compressive strength ranges between 200 to 10,000 kpa or more.
![img-2.jpeg](img-2.jpeg)

Figure 3. Geology map of study area within Metro Manila.

# 2.5. Downhole Seismic Method 

In the method of PS logging, the most widely adopted method is the seismic downhole logging. The receiver is consisted of three components of geophones (i.e., one vertical for P-wave plus two horizontals for S-wave) clamped to the borehole wall firmly for each measurement process. The two S-wave records were attained through striking horizontally the loaded wooden plank in opposite directions. As a result, the attained S-wave records had reversed polarity. On the other hand, the P-wave record was attained through the measurement of the P-wave produced by dropping a weight upon a metal plate that was situated upon the ground. To determine Vs and Vp, the S- and P-wave records are taken into consideration, respectively. This way, the layer's elastic properties (Poisson's ratio and Young's modulus) can be computed. The measurement depth is confined to 100-200 m; it should be also noted that in cases where a soft layer is overlain by a hard layer, the soft one might not be measured [4]. Such arrival time of the P- and S-waves produced are measured for the purpose of determining the low strain in-situ S- and P-wave velocities ( Vs and Vp ) and predicting the soil dynamic properties of sub-strata.

### 2.5.1. Seismic Waves

Seismic waves are typically generated due to an impulsive activity that releases an energy like an abrupt breaking of rock in the earth or a detonation. Wave propagation and particle movement are two significant parameters in the classification of the seismic waves. In general, seismic waves fall into two major classes, namely body waves and surface waves, which are explained in the following.

### 2.5.2. Body Waves

Body waves refer to movements that travel with high velocity and frequency through the inner layers of the Earth. Such waves are categorized into two main types: P-wave (i.e., the primary wave) and S-wave (i.e., the secondary wave). Amongst all types of seismic waves, the P-wave occurs with the highest speed. It has the capacity of propagating through liquid or solid; it is the first type of wave that seismic detectors receive (Equation (1)). The wave causes the particles to be vibrating parallel to direction of the wave propagation. It makes some dilations and compressions of rock particles (see Figure 4).

$$
\mathrm{Vp}=\left[\frac{K + 4 / 3 \mu}{\rho}\right]^{1 / 2}
$$

where, $K, \mu$, and $\rho$ represent Bulk modulus, shear modulus, and density, respectively.

![img-3.jpeg](img-3.jpeg)

Figure 4. P-waves; particle motion, compressional and dilatation.
On the other hand, the S-wave, which is indicated by particle vibration, is perpendicular to the wave propagation direction. In comparison with the P-wave, it has fewer levels of frequency and velocity (see Figure 5). This type of wave is separated into two components: a component parallel to surface of the ground (Sh) and another one that is vertical to surface of the ground (Sv).

Normally, Vs is slower than Vp, and also the S-waves are not capable of passing through liquid (Equation (2)).

$$
\mathrm{Vs}=\left[\frac{\mu}{\rho}\right]^{1 / 2}
$$

where, $\mu$ and $\rho$ represent shear modulus and density, respectively.

![img-4.jpeg](img-4.jpeg)

Figure 5. S-waves; particle motion and direction of propagation.

### 2.5.3. Surface Waves

Surface wave travels only through the earth crust with a lower level of velocity and frequency compared to the body wave. These waves are low frequency; thus, seismograph can simply recognize them using a wide wavelength. This type of wave causes the destructions and damages during an

earthquake occurrence. Surface waves are also categorized into two classes: Rayleigh waves and Love waves.

The Rayleigh wave triggers particles for an elliptical movement in a plane perpendicular to the surface that contains the wave propagation direction (see Figure 6). Initially, the displacement of particles is great; then, it decreases with depth in an exponential way [75]. The Rayleigh waves are propagated alongside a free surface or a boundary between two solid media, which will cause the waves to travel round the earth surface. These waves have a lower velocity in comparison with the body waves.
![img-5.jpeg](img-5.jpeg)

Figure 6. The behavior of particle elliptical motion in Rayleigh waves.
A Love wave is articulated by particles vibration parallel to surface of the ground. There is a similarity between the Love wave and the S-wave; however, the former only appears in surface layer, while Vs is lower. In general, the Love waves are generated by polarized S-waves in case the particle vibration is parallel to the free surface and perpendicular to the wave movement direction (Figure 7). Velocity of the Love waves is somewhere between the Vs of the surface layer and deeper layer.
![img-6.jpeg](img-6.jpeg)

Figure 7. Particle motion of Love waves in horizontal plane.

# 2.5.4. Data Acquisitions 

For the purpose of the present research, data acquisition is classified into two different types, namely geotechnical data acquisition (core drilling, soil boring, and laboratory testing) and geophysical data acquisition (the seismic down-hole logging method).

The seismic downhole logging was conducted with the help of 24 channel ABEM Terraloc MK8 seismograph well attached to downhole seismic cables. A six-Hz detector containing three geophone components was attached to the end of the seismic cable; two horizontal geophones were also utilized for the purpose of recording S-waves and a single vertical geophone was utilized for recording P-waves (Figure 8). Then, 3 inches of ( 77 mm ) PVC pipe was implemented in the borehole. The bottom end of the PVC pipe was positioned very close to the PVC cap; this was because of the fact that where steel casing is utilized, the impacts will be of a higher importance. Right at the PVC cap center, a hole of the

size 17 mm was drilled for the aim of grouting. In addition, to make sure the hole would remain intact with rock mass or soil, cement-bentonite was used for grouting the space between the PVC casing and borehole wall with a mixture ratio of 1:1; the procedure started from the borehole bottom in a way to avoid cavities that may appear in the course of grouting.

The seismic downhole method performs direct measurement of Compression (P) or Shear (S) wave velocities or both in a PVC cased borehole which advanced through soil to require depth. The annulus between the borehole surface and the PVC casing is carefully cement-grouted to ensure the hole remains intact with the soil. Water was filled inside the cased borehole before starting the measurements to improve or enhance the grounding of the soil. The test was carried out using a 24 channel ABEM Terraloc MK8 seismograph by lowering a geophone to a full depth in the cased borehole. A seismic source is triggered by a 12lb sledgehammer by striking vertically onto a steel plate placed on the ground near the borehole to create the compression or P-wave. Alternatively, the sledgehammer strikes horizontally to either ends of the concrete/wooden block to generate the shear or S-wave. The travel time is recorded from the moment of seismic source initiation until reception at the geophone. The geophone is raised to a new depth at every 1 m depth interval. The same process is repeated from the bottom of the borehole until to the top of the PVC casing (Figure 9).

After that, the detector was cautiously lowered down to the end of the grouted borehole; then, it was fastened firmly to the borehole wall for the purpose of achieving better grounding, hence producing finally results of a higher quality and reliability. In the interval of $0.5-1 \mathrm{~m}$, data regarding the P - and S -waves were attained with considering the borehole situation to seismic source distance (P- or S-waves). It was necessary because with an increase in the distance, it could result in velocity error calculation. With an assumption indicating that the distance between the borehole and seismic source is getting close to zero, it was recognized that wave might travel not through the soil layer, but through the borehole casing, where an incorrect arrival time could be detected [76]. It is somewhat different to acquire downhole-related data in the cases of the P-wave and S-wave.

The data related to the downhole P-wave seismic are obtained from the P-wave seismic source. Such data are generated through vertically striking a steel plate situated at $1-1.84 \mathrm{~m}$ from borehole with the use of a 6 kg sledgehammer (Figure 9a). The downhole S-wave seismic data are obtained from an S-wave seismic source, which is generated through horizontally striking on the opposite direction of a weighted wooden plank (on top of it by car/lorry) using a 6 kg sledgehammer (see Figure 9b). The use of the wooden plank weighted on top of it by lorry, car, or any heavy object is for the aim of providing a proper friction contact with the ground. Every direction of horizontal hammer strike upon the wooden plank generates an S-wave with an opposite polarity in comparison with the opposite direction of horizontal hammer strike. It worth noting that prior to the beginning of measurements, inside the borehole casing was filled with water for the purpose of enhancing the grounding of soil adjacent to the well. On-site photos of the P- and S-waves data acquisition are presented in Figure 10.
![img-7.jpeg](img-7.jpeg)

Figure 8. Seismograph and down-hole detector; (a) ABEM Terraloc MK8 seismograph, (b) downhole detector.

![img-8.jpeg](img-8.jpeg)

Figure 9. Seismic down-hole data acquisition, (a) P-wave (b) S-wave.
In this study, IXRefraX, SeisOpt@2D, Surfer 8, and Microsoft excel software were used to process the collected seismic downhole P - and S -wave data. The obtained results were employed to calculate the $\mathrm{Vs}, \mathrm{Vp}$, and interval velocity $(\Delta \mathrm{V})$. Vs and Vp are computed on the basis of the waves' first travel time alongside the path distance. Equation (3) was utilized to calculate the path distance of the waves (l).

$$
l=\sqrt{X^{2}+d^{2}}
$$

where, X and d are distance between seismic sources to borehole and depth of detector, respectively.
The corrected first arrival time is given by Equation (4):

$$
\mathbf{t}=\frac{\mathrm{d}}{l} \times \mathrm{T}
$$

The seismic first arrival time ( T ) is plotted against the path distance of waves ( $l$ ), or the corrected first arrival time ( t ) is plotted against the detector depth (d), where slope actually denotes velocity. This curve is separated into a number of proper regions of straight lines signifying $\Delta \mathrm{V}$. To achieve empirical correlation relationships, the seismic results processed, which include Vs, Vp, and $\Delta \mathrm{V}$, are correlated with relevant borehole record.

![img-9.jpeg](img-9.jpeg)

Figure 10. On-site seismic down-hole data acquisition; (A) P-wave and (B) S-waves.

# 2.6. Laboratory Testing 

The procedures applied in the present study to testing the samples for a project are well conformed with the ASTM standards and with the selected references such as Soil testing for Engineers by Lambe and Whitman [77]. The following tests were carried out on collected samples in laboratory.

### 2.6.1. Analysis of the Soil Particle Size

The soil particle size analysis quantitatively determines the particle distribution in soil. The distribution of particle sizes was obtained using sieve No. 200. The individual particles that were found in particular soil indicate the soil performance features. In addition, the percentage by weight of the materials that pass through its succession sieve is recorded.

### 2.6.2. Atterberg Limits

The tests of plastic limit and liquid limit are conducted for defining the lower/upper moisture content (MC) points at which a specific soil stops performing as a plastic. This test can be conducted only on cohesive soils. The liquid limit (ASTM D-425-66) actually shows the water content of soil, which is indicated as the percentage of the weight of the oven-dried soil at the boundary between

plastic and liquid states. On the other hand, the plastic limit (ASTM D44-59) indicates the percentage of the mass of the oven-dried soil between the plastic and semi-solid states at laboratory.

# 2.6.3. Moisture Content of Soils (ASTM D 2216-98) 

The test of MC of soil is done based on the water weight in soil. This test shows how various types of soil behave at different moisture levels. This is a ratio stated as the percentage of the water weight in a specific mass of soil to the solid particles weight.

### 2.6.4. Soil Specific Gravity

The soil specific gravity test was done for determining the specific gravity of soils that can pass through a 4.75 mm (No. 4) sieve using pycnometer. In cases where soil is consisted of particles larger than the 4.75 mm sieve, the test method C 127 is generally adopted for the material retained on the 4.75 mm sieve; this test can be conducted for materials that pass through a 4.75 mm sieve.

### 2.7. Input and Output Parameters

As mentioned earlier, many properties of the soil can be considered as model inputs for the purpose of soil classification. Then, after reviewing of literature and available data from field and laboratory, six parameters were used to obtain a suitable model for determining/predicting soil class/type. These parameters include Vp, Vs, MC, liquid limit (LL), plastic limit (PL), and specific gravity of soils (Gs). The samples measured in this study consist of 151 data samples which were obtained from 9 different boreholes. The statistical information regarding the input parameters used in modeling of this study is shown in Table 2. These data were measured in the field as well as in the laboratory. After doing the tests, we prepared a database comprising of 151 datasets with 6 mentioned inputs where in each dataset there is a class of type of soil. Depending to the depth of samples collection, different soil classifications i.e., clay with low plasticity (CL), clayey sand (SC), silty sand (SM), and clay with low plasticity $(\mathrm{CH})$ were observed in the site. Out of 151 datasets, a number of $42,80,18$, and 11 were, respectively, obtained for CL, SC, SM, and CH soil classes. In our database, values or categories of 1, 2, 3 , and 4 were assigned for $\mathrm{CL}, \mathrm{SC}, \mathrm{SM}$, and CH soil classes, respectively. In addition, averages values of $2225.44 \mathrm{~m} / \mathrm{s}, 1129.64 \mathrm{~m} / \mathrm{s}, 34.85 \%, 40.97 \%, 14.71 \%$ and $2.63 \mathrm{~g} / \mathrm{cm}^{3}$ were obtained and used for input parameters to determine soil classifications.

Table 2. The used input parameters for determining soil classifications.


## 3. Results

This study employed eight ML models including, four DT models, two artificial neural network models, and two Bayesian network models. These models included CHAID, CART, C5, QUEST, ANNMLP, ANNRBF, BAYEIANTAN, and BAYESIAN MARKOV. It is worth mentioning that data were split into train $(80 \%)$ and test $(20 \%)$ partitions before the models' employment [22,78]. There is no agreement on the partitioning ratio among different studies. Since the sample size used in this study was relatively small, this present study allocated $80 \%$ of the data for training because it is necessary to ensure that the models examine more samples and, therefore, probably finds a more desirable solution. Besides, if the training dataset is small, the models of interest cannot learn general principles,

and consequently, the models will have unsatisfactory test set performance. The sample size of train data was 113 and test data was 38 . This study used several criteria to assess the performance of models employed, including recall, precision, overall accuracy, gains chart, and agreement between the models employed.

Table 3 shows the overall accuracy of the models employed. For the training dataset, the BAYESIANMARKOV model achieved the highest overall accuracy (100\%) while the QUEST, ANNMLP, and ANNRBF achieved the greatest accuracy ( $94.74 \%$ ) for the testing phase. On the other hand, the BAYESIANMARKOV model obtained the lowest overall accuracy ( $34.21 \%$ ) though the CHAID, CART, ANNMLP, ANNRBF, and BAYESIANTAN obtained the lowest overall accuracy.

Table 3. Overall accuracy of the models employed.


The training recall and precision (Table 4) of the classifiers for each soil characteristic are shown in Figure 11. Notably, all classifiers predicted soil characteristics of " 3 " and " 4 " more accurately than other traits. Category " 1 " was generally less correctly predicted than the other soil attributes, though the BAYESIANMARKOV model predicted this category with high accuracy. Moreover, CART, ANNMLP, ANNRBF, and BAYESIANTAN followed the same patterns of recall and precision. That is, attributes of " 3 " and " 4 " were predicted most accurately, followed by characteristic " 2 ". It is also worth noting that in five models, including CART, ANNMLP, ANNRBF, BAYESIANTAN, and BAYESIANMARKOV, the recall and precision were identical. Thus, the corresponding trend lines of recall and precision in each related diagram have coincided.

Table 4. Performance criteria used in this study.


As pointed out previously, a series of gain charts were used to assess the performance of the models employed. The gains are estimated through Gains $=(\mathrm{n} / \mathrm{N}) \times 100$. The n means the number of hits in quantile, and N represents the total number of hits. Here, it is requisite to notice that "hit" points to the success of a model to forecast the first value in the set. In gains chart, the perfect model with perfect confidence (where hits $=100 \%$ of cases) is denoted by the blue line. The oblique red line represents the at-chance model.

Moreover, other models in the chart are implied by other lines in the midst. The area between a model and the red line can compare a model employed and the at-chance model. This area recognizes how much better an employed model is compared to the at-chance model. Besides, the space between a model proposed and the best model knows where a proposed model can be grown.

In the gains chart, it is important to maximize the space between the models' curves and the at-chance model. Besides, the higher lines represent better models, particularly on the left side of the chart. Figure 12 displays the gain charts for DT models, neural network models, and Bayesian models to predict the soil characteristics. For the training phase, almost all models showed similar behavior for all four categories of soil characteristics. However, for classes " 1 " and " 2 ", the BAYESIANMARKOV

model showed the best performance. Concerning the testing phase, the BAYESIANMARKOV models showed the worst performance to predict the categories of " 1 ", " 2 ", and " 4 ". For the class of " 3 ", almost all models, except the CHAID, showed similar performance. The CHAID showed the worst performance to predict the category of " 3 ".
![img-10.jpeg](img-10.jpeg)

Figure 11. Training recall and precision of the models employed.

![img-11.jpeg](img-11.jpeg)

Figure 12. Gain chart of the models employed.
Table 5 provides an overview of the agreement between the predictions of the models employed. Hence, the agreement level between the predictions was $96.46 \%$ for the training dataset and $36.32 \%$ for

the test dataset. This shows that the models employed predicted the soil characteristics somewhat similarly in the training phase.

Table 5. Agreement between the models developed to classify the soil characteristics.


# 3.1. Models Stability 

According to the overall accuracy of the models employed, the stability of the models can be discussed here. The models' stability refers to the similarity between the training and testing overall accuracy. The stability of the ML models is important because it is adequate for generalization and essential and enough for consistency of empirical risk minimization. As shown in Table 3, four models, including C5, QUEST, ANNMLP, and ANNRBF, had the highest stability. Among these models, the neural network models outperformed the tree-based models in terms of stability (Figure 13). Besides, the BAYESIANMARKOV achieved the highest training accuracy; however, its testing accuracy was awful.
![img-12.jpeg](img-12.jpeg)

Figure 13. Variability or dispersion of the data in ANNMLP and ANNRBF models.

### 3.2. Importance of Variables

Figure 14 presents the bar chart of each variable's importance for each ML model employed in this study. The importance of variables varied between models employed. In addition, the number of important variables differed noticeably. The most important variable for four models, including CHAID, QUEST, ANNMLP, and BAYESIANTAN, was “Vp”. Three models, including CART, C5, and BAYESIANMARKOV, identified “Vs” as the most important variable. Besides, “Gs” was the most important variable for ANNRBF.

![img-13.jpeg](img-13.jpeg)

**Variable Importance**


**Figure 14.** Importance of variables derived from various models employed.

### 4. Discussion and Conclusions

This study was set out to (1) apply well-known ML algorithms to predict the characteristics of soil and (2) to compare the performance of these models for predicting the soil characteristics/classifications. Four tree-based algorithms, including C5, CHAID, QUEST, and CART; two neural networks algorithms, including ANNMLP and ANNRBF; and two Bayesian networks algorithms, including BAYESIANTAN and BAYESIANMARKOV, were applied to a dataset from a geographical study. The performance of each model was evaluated regarding its overall accuracy, recall, precision, stability, and variable importance.

Among all models employed, the BAYESIANMARKOV model achieved the highest accuracy in the training phase (100%), while this model achieved the lowest accuracy in testing phase (34.21%). This implied that the BAYESIANMARKOV model lacked stability and it may not be suitable for analyzing the soil classification. The possible reason behind the low accuracy of BAYESIANMARKOV model in testing phase might be insufficient testing data. Typically, the availability of more test data is preferred because it provides a better understanding of how well the models generalize to unseen data. Furthermore, with less testing data, the performance statistic might have greater variance. All in all, it is an extremely challenging task to split data into train and test sets when a small dataset is available. While the BN models can be assumed as robust techniques to reason probabilistically, they involve the

encoding of possibilities, speculating the points where randomized actions can occur and, therefore, require a more heuristic attempt to create.

The QUEST had the second highest overall training accuracy ( $99.12 \%$ ) and had the highest overall testing accuracy $(94.74 \%)$. Thus, this model was somewhat stable and had an acceptable overall training and testing accuracy to predict the soil characteristics. In a comparison between the Bayesian Network and DT models, Bayesian Network models work well with small datasets compare to DTs. These models also have a faster processing time. More importantly, they are less susceptible to overfitting compared to DTs. On the other hand, DTs are much more flexible and easier to understand compared to the Bayesian network models. However, DTs are extremely prone to overfitting. The ANN models outperformed other models in terms of stability. ANN models are now widely used due to their capabilities in generating quick results. However, these models are a black box and suffer from explainability.

The procedure of modeling presented in this study can be used by researchers and engineers in order to classify the soils during geophysics investigations. In addition, the same procedure can be implemented for other soil types using similar input parameters.

Author Contributions: Conceptualization, D.J.A.; Data curation, R.S.; Formal analysis, C.S.L.; Supervision, E.T.M.; Writing-review and editing, C.S.L., M.R.M. and D.J.A. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Acknowledgments: Authors acknowledge with thanks Edy Tonnizam Mohamad Director-Geotropik, Centre of Geoengineering, Universiti Teknologi Malaysia, for provision of data of this study and encouragement given thorough out the paper.
Conflicts of Interest: The authors confirm that this article content has no conflict of interest.
