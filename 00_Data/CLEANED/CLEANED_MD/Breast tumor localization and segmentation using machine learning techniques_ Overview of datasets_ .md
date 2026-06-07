# 1 Breast tumor localization and segmentation using machine learning techniques: Overview of datasets, findings, and methods 

Ramin Ranjbarzadeh ${ }^{1}$, Shadi Dorosti ${ }^{2}$, Saeid Jafarzadeh Ghoushchi ${ }^{3}$, Annalina Caputo ${ }^{4}$, Erfan Babaee Tirkolaee ${ }^{5, *}$, Sadia Samar Ali ${ }^{6}$, Zahra Arshadi ${ }^{7}$, Malika Bendechache ${ }^{8}$<br>${ }^{1}$ School of Computing, Faculty of Engineering and Computing, Dublin City University, Ireland. ramin.ranjbarzadehkondrood2@mail.dcu.ie<br>${ }^{2}$ Department of Industrial Engineering, Urmia University of Technology, Urmia, Iran. Shadi.dorosti@gmail.com<br>${ }^{3}$ Department of Industrial Engineering, Urmia University of Technology, Urmia, Iran. s.jafarzadeh@uut.ac.ir<br>${ }^{4}$ School of Computing, Faculty of Engineering and Computing, Dublin City University, Ireland.<br>annalina.caputo@dcu.ie<br>${ }^{5}$ Department of Industrial Engineering, Istinye University, Istanbul, Turkey.<br>erfan.babaee@istinye.edu.tr<br>${ }^{5}$ Department of Industrial Engineering, Faculty of Engineering, King Abdulaziz University, Jeddah, Saudi Arabia.<br>ssaali@kau.edu.sa<br>${ }^{6}$ Faculty of Electronics, Telecommunications and Physics Engineering, Polytechnic University, Turin, Italy.<br>Zahra.arshadi@gmail.com<br>${ }^{8}$ Lero \& ADAPT Research Centres, School of Computer Science, University of Galway, Ireland. malika.bendechache@universityofgalway.ie

[^0]
[^0]:    * Corresponding author

The Global Cancer Statistics 2020 reported breast cancer (BC) as the most common diagnosis of cancer type. Therefore, early detection of such type of cancer would reduce the risk of death from it. Breast imaging techniques are one of the most frequently used techniques to detect the position of cancerous cells or suspicious lesions. Computer-aided diagnosis (CAD) is a particular generation of computer systems that assist experts in detecting medical image abnormalities. In the last decades, CAD has applied deep learning (DL) and machine learning approaches to perform complex medical tasks in the computer vision area and improve the ability to make decisions for doctors and radiologists. The most popular and widely used technique of image processing in CAD systems is segmentation which consists of extracting the region of interest (ROI) through various techniques. This research provides a detailed description of the main categories of segmentation procedures which are classified into three classes: supervised, unsupervised, and DL. The main aim of this work is to provide an overview of each of these techniques and discuss their pros and cons. This will help researchers better understand these techniques and assist them in choosing the appropriate method for a given use case.

Keywords: Breast cancer, Deep learning, Image segmentation, Tumor segmentation.

## 1. Introduction

Breast cancer (BC) is the second most usual cause of cancer death among women and common malignancy [1]-[3]. Generally, cancer is caused by gene mutation or changes to genes that control the cells' function. Consequently, cells divide uncontrollably and spread into surrounding tissues [4]. BC occurs when certain breast cells start spreading abnormally and have an effect on the inner lining of the milk ducts [5], [6]. These cells divide rapidly and continue to accumulate which leads to forming a lump or mass. Cells may spread through the lymph system (metastasize), the bloodstream, local invasion to lymph nodes or other parts of the body, commonly into bones, brain, liver, and lungs. In this case, the tumor is considered to be malignant (cancerous). Typically, these cells form a tumor which can be felt as a lump or seen on an X-ray [7], [8]. BCs' signs include pain in the nipple, changes in the shape of the breast size, discharge of the nipple, and lymph node swelling [9], [10]. There are many kinds of BC in both invasive and non-invasive groups, such as invasive lobular carcinoma (ILC), ductal carcinoma in situ (DCIS), inflammatory

breast cancer (IBC), lobular carcinoma in situ (LCIS), etc. There are 5 stages of BC ranging from $0-4[11],[12]$.

Women with dense breasts have a higher risk of developing BC in comparison to women with less dense breasts [13]. This is because more connective tissues can be seen in dense breasts than in fatty tissue. This feature can sometimes make it difficult to see tumors in mammogram screening. Based on studies, unilateral BCs commonly occur in the left breast than in the right [14]. There are many identified BC risk factors that raise the probability of cancer including family history, obesity, alcohol use, age of menarche, etc. BC in $\sim 70-80 \%$ is curable for those patients that are diagnosed in the early stage (non-metastatic stage) [15].

In order to detect cancer and the location of the suspicious lesion in the breast (i.e., breast tumor segmentation), imaging techniques of the breast are essential. Imaging can provide different kinds of information including structure, functions, metabolism and morphology; therefore, it is one of the essential and main parts of cancer detection and clinical protocols [16], [17]. Moreover, a variety of tests can detect the spread of cancer. These tests typically are not performed unless the doctor thinks the cancer may have spread. The most common tests include a positron emission tomography (PET) scan, bone scan, chest X-ray, CT scan, MRI scan, and ultrasound. Generally, the breast imaging term refers to breast magnetic resonance tomography (MRT), sonography and mammography [4], [18], [19].

Medical imaging has long been part of BC treatment and has been utilized in all procedures of cancer control from recognition and localization to therapy monitoring and post-therapeutic follow-up [20], [21]. However, there are some weaknesses in using medical imaging for BC segmentation. For example, inaccurate interpretation because of expert's fatigue, low specificity in mammography, decreased sensitivity because of similar tissue densities, etc. Therefore, image interpretation is a time-consuming, operator-dependent and arduous task that entails doctors or certified experts [6], [22].

Imaging tools such as X-ray, magnetic resonance imaging (MRI) diagnostics, and ultrasound yield plenty of details and key information that must be carefully examined and assessed by the radiologist or other medical professional in a short time [23], [24]. The Computer-aided diagnosis (CAD) is an approach that has the potential to boost the subjectivity of conventional histopathological image analysis and help doctors in the interpretation of obtained medical images from the body [25]-[27]. In [28], researchers showed that most experienced experts can diagnose

cancer with $79 \%$ precision; however, $91 \%$ accurate diagnosis is attained using CADs. Nevertheless, there are still limitations for applying automatic recognizing systems in routine clinical practice like excessive dependence on the network.

The limitations of using CAD tools in the daily routine of physicians and experts have been overcome significantly with the advent of artificial intelligence (AI) and machine learning (ML) [29]-[32]. These tools have been utilized efficiently for a variety of real-life applications [197][200]. For instance, ML techniques are able to design a fast and robust model to decrease recognition time and memory requirements. The success of deep learning (DL), ML, and AI techniques in image classification and segmentation in recent years has led to more and more scholars recognizing the potential for enhancing performance by using these techniques in the CAD system [4], [33], [34]. ML techniques in the field of AI seek to define complex relationships that characterize the processes that produce a collection of outputs from a set of empirical ones. CAD uses ML methods to interpret patient data on imaging and/or non-imaging and measures the state of the patient, which are able to help doctors and radiologists in their decision-making process. Furthermore, new researches and development projects to enhance CAD efficiency and adapt CAD for many other complex medical tasks are motivated by the performance of DL strategies in computer vision [8], [35].

In this paper, image segmentation is described as a useful part of image processing in CAD systems. In addition, the contour of BC is explained to recognize benign and malignant masses through 57 BC masses. Moreover, different categories of segmentation methods are discussed in detail as well as their advantages and disadvantages.

This study has summarized the findings of more than 80 scientific research papers in the field of breast tumor segmentation from 2015- 2022 (until 1st November 2022). To find out the number of studies in the field of breast tumor segmentation through unsupervised learning, supervised learning, and DL frameworks a statistical report is provided based on the "Scopus" database. The keywords employed for searching in this database were "breast cancer" AND "name of the strategy (e.g., Decision Tree)" OR "breast tumor" AND "name of the strategy".

This study focuses on reviewing the scientific research papers that applied AI frameworks for breast cancer detection and segmentation. Abbreviations utilized in this study are referenced in Table 1.

The rest of the study is organized as follows: analysis of contours of breast masses is described in

Table 1. List of the abbreviations.



# 2. Analysis of contours of breast masses 

One of the main methods to recognize benign and malignant masses is through contouring of breast masses, which is obtainable by mammography. The contour of malignant mass has spiculated contour and irregular shape, while benign mass is smooth and oval or round [36], [37]. Abnormal cases have varying textures, shapes, and dimensions of contours. Furthermore, for experienced radiologists, it is very strenuous to recognize the malignant breast mass [19], [38]. The diagnosis outcome can be given by a CAD system that incorporates pattern recognition and image processing theory to decrease the false positive (FP) and false negative (FN) rates. In the following, 57 BC masses are indicated in Fig. 1, which are taken from the screen test of the Alberta program for the early detection of BC [39]. The mammogram images in this dataset are from 20 cases. The tumors were graded by the 1D ruler technique in the order of the obtained increasing fractal dimension. The high fractal dimension of malignant tumors is because they are more spiculated and ragged than benign masses [39].
![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

Fig. 1. Fractal investigation of contours for finding the breast masses in mammograms.

# 3. Breast tumor segmentation approaches 

Segmentation of images is a technique that consists of extracting the region of interest (ROI) using an automatic or semi-automatic mechanism [40], [41]. Segmentation is the main part of image processing in CAD systems. Some image segmentation techniques are fundamentally ad hoc and vary precisely in the way they prioritize one or more of the desired properties and in the way they balance one desired property against another and compromise it [42]. The frequently employed segmentation methods can be classified into two broad classes: (1) region segmentation methods that look for areas that satisfy a given criterion of homogeneity, and (2) techniques of edge-based segmentation that search for edges between regions with distinct characteristics [41], [43]. Segmentation methods can also be divided into fine-grained classes [44], depending on the classification scheme employed:

1. Automatic, semi-automatic, and manual methods.
2. Region-based and Pixel-based strategies.
3. Model-based segmentation (contour following, dynamic programming, feature map or multispectral approaches, etc.), manual delineation, and low-level segmentation (region growing, thresholding, etc.).
4. Classical (region-based, edge-based, and thresholding approaches), neural network, fuzzy, and statistical approaches.

There are various applications of segmentation in the medical field, for instance, tumor detection and segmentation, image registration, surgical planning, mass detection in mammograms, etc. [3], [45], [46]. As shown in Fig. 2, the ML-based segmentation methods can be classified into three main categories, namely unsupervised, supervised, and DL methods.

![img-3.jpeg](img-3.jpeg)

Fig. 2. Segmentation methods.

# 4. Supervised Learning 

Supervised learning or supervised ML, is a beneficial technique to classify and process data using machine language and maps an input to an output [47]-[49]. Supervised learning can be grouped into two categories, classification and regression (cf. Fig. 2).

Although supervised learning approaches are able to produce a data output or collect data from the prior experience, these frameworks do not have the capability of classifying any input data correctly that were not among any classes in the training data.

### 4.1 Classification methods

Classification is a supervised learning strategy that learns from the input data (labelled data) and then employs this learning to classify new findings [21], [48], [50], [51]. The classification methods focus on predicting the qualitative response through data analysis and pattern recognition [52]. As displayed in Fig. 3, this review investigates several classification-based methods published articles from 2015 to 2022 in journals of all the subject categories of Scopus. 'Support vector machine (SVM) \& BC', 'SVM \& BC', 'K-nearest neighbors (KNN) algorithm \& BC', 'KNN \& BC', 'random forest (RA) \& BC', 'Decision Trees \& BC', 'Bayesian Network \& BC', and 'Naïve Bayesian \& BC' were used as keywords to search in article titles.

As we can see in Fig. 3, the SVM and RF are the most popular classification method used in the last seven years.

![img-4.jpeg](img-4.jpeg)

Fig. 3. Number of published papers per year using different classification methods for BC detection.
Since 2015 the number of research works that are based on the SVM and RF techniques increased gradually until 2022, when the number of published papers reached over 65 papers. Moreover, the number of papers published based on decision trees increased since 2016. Additionally, it is obvious that the KNN and Bayesian networks are not popular methods for BC classification given that the number of published papers per year is less than 15 papers. In the following, each of these classification methods is introduced and their application to improve the detection, prediction and diagnosis of BC are discussed.

# 4.1.1 Support vector machine 

SVM is a dividing data strategy that learns by some rules to assign labels to objects and is a promising approach for classification [53]-[56]. Due to its quick calculation time, this method has been widely used in BC detection [57]. For instance, Vijayarajeswari et al. [58] introduced an SVM-based approach for the early detection of BC. Initially, the features extracted from mammogram images through the 2D Hough transform approach and classified based on the SVM classifier. The suggested technique indicated that SVM was an effective approach for the classification of the abnormal classes of mammograms. Wang et al. [59] reduced the diagnosis variance via the SVM-based method. Wakankar et al. [60] also analyzed the breast thermogram for the ROI segmentation and classified images using the SVM technique. Akinnuwesi et al. [61] developed a procedure for risk assessment and diagnosis of BC named, BC-RAED. The proposed

method employed Principal Component Analysis (PCA) for extracting features and SVM proposed for cancer diagnosis. Sarosa et al. [62] offered a combined Gray-level co-occurrence matrix and SVM for better diagnosis of malignant and benign tumors. Wassila et al. [63] presented an algorithm for the early detection of BC through rotating the transmitting antenna in the SVM method.

SVM is capable of working well with even semi-structured and unstructured data utilizing a proper kernel function. However, the main disadvantages of the SVM method are large datasets take a long time to train, and the final model is difficult to understand and interpret individual impact, which is not suitable for large datasets and variable weights. Furthermore, in the presence of noise in the dataset, the SVM does not perform very well.

# 4.1.2 K-nearest neighbors algorithm 

KNN algorithm is a non-parametric classifier and simple ML technique. The KNN strategy focuses on the similarity between the new data/samples and available samples and puts the new samples into the group that is most analogous to the existing groups [64], [65]. The KNN strategy has been used for tumor classification in the BC field. For instance, Cherif et al. [66] presented a procedure to speed up the KNN classifier and get a better BC diagnosis system based on clustering and attribute filtering. Rajaguru and Chakravarthy [67] employed KNN and Decision Tree methods to classify the BC tumor. According to the result of this study, KNN method had better performance in BC classification. Athani et al. [64] predicted and classified BC using a KNN algorithm through parallel programming to decrease the procedure time in comparison with the sequential execution form.

KNN method is simple to interpret and is much faster than other frameworks that require training (such as SVM, RF, and decision tree) The main disadvantage of a KNN algorithm is that accuracy depends on the quality of the data and requires high memory to deal with the large data.

### 4.1.3 Random forest

RF is an ML technique that combines classification and regression tree. The RF strategy by creating a number of decision trees at training time tries to generate the class mode (mean/average predictor of the individual trees) and can be used for regression, classification, and other tasks [68]-[70]. Regression predicts a value from a continuous range, whereas classification predicts 'belonging' to the class. The RF can be utilized for both classification and regression tasks, and the

relative importance it assigns to the input features. The RF algorithm has had a major influence on medical image computing over the last few decades. Wang et al. [71] suggested a method for an accurate diagnosis system with high precision through developing RF-based rule extraction. Moreover, a multi-objective evolutionary algorithm (MOEA) was used to optimize the rules. Dai et al. [72] employed the RF algorithm for the BC diagnosis and prediction problem with high accuracy. Al-Quraishi et al. [73] aimed to predict the likelihood of BC recurrence among patients. Therefore, in this study, the Deep Neural Network and RF are applied to compare the accuracy of the models. The outcomes show that the RF technique provides information with high accuracy. However, the RF method's main disadvantage is that a large number of trees will make it too slow and inefficient for real-time applications.

# 4.1.4 Decision Trees 

Decision tree is a popular approach and acts as a predictive method and uses a tree to go from an item's findings to conclusions, regarding the target value of the item [74], [75]. In Tree models, if the target variables take different sets of values, classification, tree leaves and branches, can be used to indicate class labels and conjunctions of features contributing to those labels [76], [77]. Decision tree is a method that has been widely used in different disciplines because it is a reliable and effective decision-making technique and provides high accuracy in classification; therefore, this method has been utilized in medical image processing and BC segmentation. For instance, Jerez-Aragonés et al. [78] incorporated the neural network and decision trees model for detecting the BC. Moreover, they introduced a new method for Bayes' optimal error estimation. Li et al. [79] studied the incidence of BC under different combinations of non-genetic factors. In order to build such a model, a classification based on the tree algorithm was employed. Sumbaly et al. [80] suggested a technique for the early detection of BC through the decision tree-based technique. Hamsagayathri et al. [81] analyzed different decision tree classifier algorithms for early BC diagnosis.

A decision tree strategy is easy to explain to technical teams and does not require the normalization of data. Nonetheless, decision trees are inherently unpredictable and even minor changes in the data will result in significant changes in the layout of the optimal decision tree.

### 4.1.5 Bayesian network

A Bayesian network (decision network, belief network, or Bayes network) is based on Bayes'

theorem and is a probabilistic graphical model for representing multivariate probability distributions which utilize a set of variables with their conditional dependencies via a directed acyclic graph (DAG) [82], [83]. Bayesian network generalizations that can reflect decision issues under uncertainty are called influence diagrams. There are different theories and techniques that are a subtype of Bayesian statistical methods, for example, Bayesian network, Naïve Bayesian, Markov chain Monte Carlo, etc., which are indicated effective tools in BC detection and prediction [84], [85].

Vazifehdan et al. [86] predicted BC recurrence via a hybrid imputation method to effectively deal with the missing data problem. They divided the dataset into two discrete and numerical subsets and used a Bayesian network to impute the first missing values of the discrete fields. Feng et al. [87] employed Bayesian network meta-analysis to synthesize available evidence of indirect or direct comparison of HER2-targeted therapy drugs. Mandal et al. [77] introduced a technique for highly-accurate classification of BC via different cancer classification approaches including Naïve Bayes, decision tree classifiers, and logistic regression.

Bayesian networks are able to handle missing data and avoid overfitting of data. However, the major drawback of a technique involving Bayesian networks is the fact that there is no universally accepted approach for creating a network from data.

# 4.2. Regression methods 

Regression analysis refers to a series of statistical procedures for determining the relationships between one or more independent variables (features or predictors) and a dependent variable (outcome variable) in statistical modeling [77], [88]. In contrast with clustering approaches, in regression analysis data on each group should be analyzed separately [89]. Each regression focuses on a specific group and how its variables contribute to this particular group. There are different methods of regression methods. The most commonly used regressions are linear regression, logistic regression, stepwise regression, etc. [90]. In the following, we show the regression methods that are mostly used in the medical field, especially in the BC field.

Fig. 4 illustrates that regression models turned out to be a popular supervised method over the last decade.

![img-5.jpeg](img-5.jpeg)

Fig. 4. Number of published papers per year using different regression models for BC segmentation.
Since 2015 the number of articles based on the regression technique increased gradually and in 2022, especially, the Linear regression method is one of the most popular methods in regression technique where the number of published papers has increased considerably over the last decades. In fact, in 2022, the number of published papers reached over 110 papers. ANN is another useful method among regression techniques; however, the number of published papers using this technique is not considerably high compared to the Linear regression method. Overall, the number of papers published based on the regression methods are highly increased after 2018 and it can be evidence of these methods gaining popularity in the last few years. Therefore, it is predicted that the number of papers that are based on the regression method will increase in the next years.

In the following, each technique will be introduced and its role in BC detection and diagnoses are explained.

# 4.2.1 Linear regression 

Linear regression is a supervised learning approach where the anticipated result is continuous and has a steady slope [91]. Due to the simplicity to implement and interpret its output coefficients, linear regression is widely employed for a wide range of prediction problems, including BC. For instance, Veronesi et al. [92] evaluated the risk of internal mammary chain metastases via a multivariate analysis and resorting to multiple linear regression of the dependent variable with the logistic transformation. Xiong et al. [93] suggested fine needle aspirate for BC diagnoses and data mining. Moreover, statistical approaches such as principal component analysis (PCA) and partial

least squares (PLS) linear regression analysis as well as data mining approaches such as association rules and decision trees are combined to find the unsuspected relationships. Dunya et al. [94] evaluated the satisfaction with oncologic surgical procedures to optimize long-term health and facilitate the decision-making process. Descriptive statistics and regression analysis were used for this purpose. However linear regression has some disadvantages too. By fitting a linear equation to observed data, linear regression presumes a linear relationship between dependent and independent variables.

# 4.2.2 Support vector regression 

SVR employs the same principle as SVM, but for regression problems. SVR looks for a feasible solution for working with continuous values instead of classification by individualizing the hyperplane that maximizes the margin [95]. Hyper-Plane in SVM is principally the separation line between all classes whereas in SVR it defines as the line that predicts the target value or continuous value. Goli et al. [96] proposed a new SVR method with different kernels. The best subset of features was selected utilizing three feature selection approaches including recursive feature elimination, univariate feature selection using concordance index, and a combination of statistical tests and SVR. However, the SVR has some disadvantages. For example, the SVR algorithm is not suitable for large datasets and is not executed effectively when the dataset includes noise samples, and in cases where the number of features for each data point is much more than the number of training data samples, the SVR will underperform.

### 4.2.3 Gaussian process regression

Gaussian process regression (GPR) method is a non-parametric Bayesian regression approach that generates waves in the field of ML. The GPR technique is capable of working well on small datasets and providing measurements of uncertainty on the predictions and have various application, including BC detection and prediction. Rafe et al. [97] developed a prediction model for BC based on a hybrid incremental learning model and the attributes of the missing values in the dataset are predicted through the Gaussian process regression. The novel classifier is a combination of RBF and AdaBoost, and Gaussian Process Classifier. Qiu et al. [98] suggested a method to track the outcome of post-treatment for evidence-based decision-making in BC. The model is an innovative Hierarchical Gaussian Distribution (HGD) which is estimating the missing portion of the data. The main drawback of the Gaussian Process is that it scales very badly with

# 4.2.4 Artificial neural network 

ANN is a model inspired by biological neural networks and designed to simulate the human brain analysis and process of information [99]-[101]. ANNs are used for modeling non-linear problems and are based on a collection of connected units or nodes called artificial neurons [83], [102], [103]. These networks are the component of AI and solve problems that are impossible to solve by human and statistical standards. ANNs have self-learning capabilities by altering weight values that allow them to generate better results as more knowledge becomes available. That means a complex relationship defines between output and input. ANNs are finding many uses in medical diagnosis applications to solve various health problems [4], [104]. Kaymak et al. [105] suggested an automatic classification of images to diagnose BC. Back propagation neural network (BPPN) is applied for classifying images and it is improved through the radial basis neural network method. Dihge et al. [106] predicted nodal status to prevent unnecessary surgery via an ANN model. In this study, the nodal status in clinically node-negative BC is predicted and candidates for the sentinel lymph node biopsy are identified through the patient-related and pathological characteristics. Lessa and Marengoni [107] introduced a diagnostic system to identify the normal and abnormal tissue in thermographic breast images. The classifier of the proposed method is an ANN model which shows high sensitivity and accuracy. Ahmed et al. [108] utilized two neural network methods, DeepLab and Mask RCNN, with the aim of breast mass classification and segmentation in the cancerous region. However, ANNs have some unexplained functioning of the network including the difficulty of representing the problem to the network. In other words, problems have to be translated into numerical values before being introduced to ANN and hardware dependence.

## 5. Unsupervised learning

Unsupervised learning is a technique of ML in which the model does not need to be supervised by users [46]. Instead, it enables the model to operate on its own to discover trends, patterns, and previously undetected knowledge. It deals primarily with unlabeled data [109]-[111]. The main subsets of the unsupervised learning technique are clustering methods, thresholding methods, region-based methods, and edge-based methods [43], [112], [113]. Clustering is the method of grouping similar objects into separate groups or more specifically, dividing the dataset into subsets so that the data in each subset is calculated following a given distance [114], [115]. Clustering is a common approach for data analysis and is applicable in many fields, including

pattern recognition, image analysis, data mining, etc. [116].
Several unsupervised methods are depicted in Fig. 5.
![img-6.jpeg](img-6.jpeg)

Fig. 5. Number of published papers per year using different unsupervised learning methods for BC segmentation.

As can be seen, the K-means clustering and thresholding algorithms have the largest number of published papers compared to the other clustering methods since 2015. Fuzzy C-mean (FCM) and region-based methods are also popular methods; however, the number of papers has not increased considerably through time. In the following, each technique will be introduced and its role in BC detection and diagnoses are explained.

# 5.1 K-means 

K-means clustering is known as a vector quantization technique that tries to partition $n$ observations into $k$ clusters such that each observation is a component of the cluster with the nearest mean, serving as a cluster prototype [117]-[119]. This method is capable of scaling to large data sets and relatively simple to implement.

Dubey et al. [120] introduced the K-means as an appropriate method that can classify the BC dataset. Zhao et al. [121] combined multiple clinic pathological and genomic variables with dimensional reduction through ML techniques to compare survival predictions. Samundeeswari et al. [122] suggested a method for diagnosing malignant and benign tumors in which the traditional K-means technique is synthesized with ant colony optimization (ACO) and regularization to split

the lesion section with optimum boundary preservation.
However, there are some limitations in this method, including all variables possessing the same variance and K-means considers the variance of the distribution of each variable (attribute) as spherical. Moreover, the K-means algorithm is sensitive to noise and outliers.

# 5.2 K-medoids 

The K-medoids technique is a clustering technique that is related to K-means clustering for segmenting a dataset into k clusters or groups. Moreover, K-medoids method is a type of K-means algorithm that is more resilient to outliers and noises. K-medoids technique uses an individual point in the cluster to describe it, while K-means uses the cluster's mean point [123], [124]. However, the number of papers on BC tumor clustering through the K-medoids is not considerable. Ping et al. [125] improved K-medoids clustering by identifying the patterns of symptom clusters in BC, using data from social media and research studies. In this technique, the main disadvantage is that different initial sets of medoids can produce different clusters. The main advantages of Kmedoids are easy to execute and understand, and lead to quick convergence in a predetermined number of stages and the main disadvantage is that diverse initial sets of medoids can lead to diverse final clustering.

### 5.3 Fuzzy C-mean

FCM clustering is a type of clustering where each data point can be assigned to more than one cluster [126]-[128]. This method also refers to as soft clustering or soft K-means. The FCM has been used as a clustering method in medical diagnoses and BC diagnoses. For example, Tavakol et al. [129] employed the FCM and K-means to detect the tumor region in the color segmentation of the thermal infrared breast images. The results show that the FCM segmentation provides results with more accuracy and no empty cluster. Kumar et al. [130] attempt to hybridize the FCM with the cohort intelligence technique to optimize cluster formation in the malignancy of breast tumor prediction. However, this method is sensitive and does not perform well with highdimensional datasets [126], [131].

### 5.4 Hidden Markov model

The hidden Markov models (HMMs) belong to the statistical models that model the observed data as a series of events or data. This model assumes that a signal is produced by a stochastic double-embedded process and deals with continuous data, presuming that each observation is

conditioned on the state of a hidden Markov chain [132], [133]. HMM has been recognized as a valuable method in healthcare, medical data, and disease detection. For instance, Momenzadeh et al. [134] offered a new model for predicting BC recurrence based on sequential patterns in microarray data. The method utilized gene sets as observation symbols of HMM. Edward et al. [135] analyzed the multivariate hidden Markov technique to assess the quality of life of BC survivors. Kaitouni et al. [132] proposed a combination of local binary pattern, region-growing and HMM approaches to segment breast tumors.

Nevertheless, this method has some drawbacks; for example, HMMs often have a large number of unstructured parameters.

# 5.5 Gaussian mixture models 

Gaussian mixture models (GMM) is a probabilistic density function assuming that a blend of a finite number of Gaussian distributions with unknown parameters produces all data points. The main advantages of the standard GMM are that it is an easy and fast model, less sensitive to scale, and handles clusters of differing sizes; therefore, it is one of the methods that are useful for modeling complex data in areas such as medical science [136]. Prabakaran et al. [137] introduced a model based on a GMM classifier to categorize individual patients based on their tumors' molecular characteristics. Rajaguru \& Prabhakar [138] presented a simple, cost-effective, and noninvasive method for detecting BC at an early stage using GMM and radial basis function (RBF) techniques. Aminikhanghahi et al. [139] classified the detected regions in mammogram images into malignant or benign categories via a combination of GMM and fuzzy logic system (FLS). Punitha et al. [140] classified the BC images as benign and malignant. According to this approach, Gaussian filtering is employed for image pre-processing, dragon fly optimization (DFO) is used for the automatic detection of breast masses, and GLCM and GLRLM techniques were employed to find the texture features.

The main disadvantages of GMM models include: (i) specifying the number of clusters, (ii) assuming a normal distribution for features, and (iii) difficultly incorporating categorical features.

## 6. Deep learning methods

DL is an AI branch of ML that uses neural networks to learn supervised and unsupervised from labeled or unlabeled data [127], [141]-[144]. Different types of models used in DL can be categorized as 1) Supervised models including recurrent neural networks (RNNs), convolutional

neural networks (CNNs), and Classic Neural Networks (Multilayer Perceptrons). 2) Unsupervised models including AutoEncoders, Boltzmann machines, and self-organizing maps (SOMs). Fig. 6 summarizes the different DL techniques used in the BC detection field.
![img-7.jpeg](img-7.jpeg)

Fig. 6. Number of published papers per year using different DL models for BC detection.
As represented in this figure, the DL methods are very popular techniques in the BC field and that is reflected by the number of published papers in this field in the last decade. As can be seen in Fig. 6, over 100 papers were published in the year 2022 alone and this number is expected to increase in the future due to the efficiency of these methods and their accuracy in BC diagnosis and detection.

In the following, each technique is introduced and their role in BC detection and diagnoses is explained.

# 6.1 Convolutional neural networks 

CNNs are popular deep neural network techniques utilized to perform deep feature extraction and classification [24], [49]-[51], [103]. The key to the success of CNN lies in its carefully designed architecture, capable of understanding the input data's local and global characteristics [32], [127], [145]. CNNs have achieved expert-level performances in various fields, including medical research [146]-[148]. For instance, Benzebouchi et al. [149] proposed a 6-layer CNN architecture for the automatic detection of BC that accepts 190 mammogram images as the training

data. For feature extraction, firstly, the key building blocks applied in CNNs are the convolutional layers. The simple application of applying a kernel (mask) to input that results in extracting some features is a convolution operation. When repeatedly applying the same mask to input, an activation map called a feature map shows the position and intensity of the detected feature in a 1D input (signal) or 2-D input (image). After the Convolutional layer, the pooling layer is normally placed. Pooling is required to down-sample information that appeared in the feature maps. The utility of the pooling layer is to decrease the spatial dimension of the volume of input for the next layers [24], [127], [150], [151]. In the following, the activation layer (transfer layer) defines the output values of the obtained feature maps by the former convolutional layer based on a threshold value. The activation function is an element-wise operation over the input volume, and thus, the dimensions of the input and the output are equivalent. In the last layer of the feature extraction procedure, the fully connected (FC) layer is utilized and forms the last few layers in the network. The output from the final pooling or convolutional layer is flattened and then fed into the FC layer. The objective of this layer is to take the outcomes of the convolution/pooling layers and utilize them to classify the image into some predefined labels. For classifying into benign or malignant labels, the Softmax layer is proposed. The Softmax function returns a vector containing the probability distributions for a set of possible outcomes. In a multi-class query, Softmax assigns decimal probabilities to each class [152]-[154]. The sum of such decimal probabilities must equal 1.0. This additional restriction allows training to converge faster than it would otherwise. An example of a CNN structure is demonstrated in Fig. 7.
![img-8.jpeg](img-8.jpeg)

Fig. 7. An example of a CNN structure with different layers.

Ranjbarzadeh et al. [4] proposed a multi-route CNN architecture that uses multi-feature

extraction routes to find more distinction in the breast tissue. Peng et al. [155] suggested a hierarchical model that comprises breast segmentation and tumor segmentation stages. In the first stage, a tumor morphology-aware network was utilized to extract contrastive information. Next, a hybrid inter-class and intra-class distance optimization loss was employed to supervise the model. Wahab and Khan [156] introduced an integrated scoring system for selecting ROI from wholeslide images. Multifaceted fused-CNN and a hybrid-descriptor are applied for this purpose. Zuluaga-Gomez et al. [157] suggested a CAD system based on thermal images. The baseline of this method is the importance of data augmentation and its impact on classification through the CNN models. Gour et al. [158] suggested an error-prone and time-consuming method based on a residual learning-based 152-layer model which is named ResHist model. Their model learns discriminative and rich features from the histopathological images and categorizes histopathological images into malignant and benign classes. Rouhi et al. [159] designed two techniques to diagnose malignant and benign masses in mammograms. Firstly, by applying an ANN model and obtained intensity features an adaptive threshold is calculated in a region-growing process. Secondly, a genetic algorithm is used to generate CNN templates for segmenting mammogram images. Ting et al. [18] introduced an approach to assist experts in diagnosing BC. The CNN improvement for the BC classification classifies the BC tumor into benign tumor, malignant tumor, and healthy patient; however, in this method, there is no prior information on the presence of a cancerous lesion. Xu et al. [160] studied the automatic segmentation of 3D breast ultrasound images and the CNN-based method applied to segment each image into four major tissues: fatty tissue, mass, fibroglandular tissue, and skin. El Adoui et al. [161] suggested two DL methods with the aim of breast tumor segmentation automatically in DCE-MRI images. In this study, two CNNs based on SegNet and U-Net were proposed for DCE-MRI detection and segmentation. Chougrad et al. [162] utilized a CNN-based method to help mammography mass lesions classification, and predict whether the mass lesions are benign or malignant. Furthermore, the importance of transfer learning was explored and the best fine-tuning strategy that adopts the trained CNN model is identified. Wahab et al. [163] suggested a transfer learning-based fast and accurate system for mitotic nuclei detection and segmentation. In this study, a pre-trained CNN is employed for segmentation, and hybrid CNN is applied for the classification of mitoses.

CNNs have some drawbacks like any other method. For instance, a CNN is remarkably slower due to an operation such as downsampling in a MaxPooling layer, If the CNN has some

layers, then the training process will be time-consuming and will require a good GPU to elevate this problem.

# 6.2 Recurrent neural networks 

RNNs are a type of ANN in which nodes create a guided graph along a temporal sequence and have an internal memory that allows them to remember important information about the input data [164]-[166]. As a result, RNNs are good and preferred algorithms for dealing with sequential data and are designed for analyzing streams of data through hidden units. In addition, RNNs can be considered as a series of networks linked together. An RNN can be designed for input, output, or both to work through sequences of vectors. In the RNN method, the information does not move only in one direction from the input layer, through the hidden layer to the output layer. Moreover, having an input memory makes it a suitable technique for predicting tasks. The knowledge in an RNN is looped back on itself [164], [165]. It considers the latest input as well as what it's learned from previous inputs when making a decision. The present and recent past are both inputs to an RNN model. This is significant because the data series contains important information about what will happen next. The current and previous inputs are both given weights by RNNs. An example of an RNN is demonstrated in Fig. 8. As clearly demonstrated in Fig. 8, the information in the current layer can be applied to the previous layer.
![img-9.jpeg](img-9.jpeg)

Fig. 8. An example of an RNN model.

The key benefits of the RNN approach include the ability to process the input of any length, the model size not growing with the size of the input, computation taking into account historical data, and weights being spread over time. For instance, Zheng et al. [167] suggested a model for

predicting the early-stage BC through the RNN and CNN methods with follow-up scans and using mammographic images. They detected suspicious cancerous regions by three cascading object detectors. Chen et al. [168] offered a deep incremental learning system. The model starts by using RNNs to extract features from various kinds of clinical text, such as B-ultrasound, X-rays, and computed tomography (CT). Saleh et al. [169] suggested an optimized deep RNN model based on RNN and the Keras-Tuner optimization technique for BC diagnosis. Patil et al. [170] offered a combination of CNN and RNN models that accepts GLRM features as the input.

However, as with the previous techniques, RNN has also its limitation. The main disadvantages of the RNN are the slow computation and difficulty of accessing information from a long time ago.

# 6.3 Long short-term memory 

Long short-term memory (LSTM) is a DL architecture that uses an artificial RNN architecture [171]. Unlike normal feedforward neural networks, LSTM has feedback links. LSTM models are a kind of RNN that employs special units along with standard units. LSTM units are composed of a memory cell that can preserve information in memory for long periods of time [172]. This kind of network process not only single data points but also entire data sequences [173]. LSTMs deal with problems of feedback links by introducing new gates, such as forget, input and output gates, which enable better preservation of "long-range dependencies" and permit better control over the gradient flow. These gates decide which information to be removed from the cell in that particular timestamp. Increasing the number of repeated layers in LSTM solves the long-range dependence in RNN. An example of an LSTM model is demonstrated in Fig. 9.

LSTM method has been widely employed in the field of medical image processing because of its reliable results. In this regard, Budak et al. [174] suggested a model to overcome early BC diagnosis through pathological images. The end-to-end model is utilized which is constructed on a fully convolutional network (FCN) and bidirectional long short-term memory (Bi-LSTM) to detect BC. Drukker et al. [175] assessed an LSTM model in the prediction of recurrence-free survival in BC patients utilizing features extracted from obtained MRI images during the course of neoadjuvant chemotherapy. Vankdothu et al. [176] combined a CNN with an LSTM to extract more unique features from MRI images for increasing the accuracy of tumor segmentation. Gore et al. [177] offered a CNN model to extract more crucial information from the brain tissue. Next, an LSTM model was employed to classify the obtained features.

period of time.
![img-10.jpeg](img-10.jpeg)

Fig. 9. An example of an LSTM network.

# 6.4 Generative Adversarial Networks 

A generative adversarial network (GAN), is a kind of ANN for generative modeling that is based on generating new and synthetic instances of data that can pass for real data [178], [179]. A GAN model is a generative network that uses two neural network networks to train it [180]. One network is called the "generative network" or "generator" model that learns to generate new plausible samples. Generative modeling entails employing a network (model) to produce new samples that are plausible to come from an existing sample distribution, including generating new images that are identical to but distinct from an established dataset of images [181]. In ML, generative modeling is an unsupervised learning technique that entails automatically learning and discovering patterns or regularities in input data so that the model can be employed to produce or output new examples that could have been derived from the original dataset [182].

The GAN is a modern unsupervised neural network architecture that outperforms conventional nets. GANs are a modern method of training a neural network and encompass not one but two independent nets that act as adversaries and work separately. As illustrated in Fig. 10, the Discriminator (D) is the first neural network, and it is the one that needs to be trained. D is the

classifier wherein once the training is completed, will take over the heavy lifting during regular operations. The Generator (G) is the second network, and its job is to produce random samples that look like real samples and make them fake samples.

D is demonstrated with a random combination of legitimate images from training images and fake images produced by G during training. Its task is to distinguish between real and fake input images. Based on the results, both models attempt to improve their efficiency by fine-tuning their parameters. If D acts well in prediction, G adjusts its parameters to produce enhanced fake samples to fool D. If D's prediction is wrong, it attempts to learn from it in order to avoid making the same error again. The number of correct predictions is the reward for net D , and the number of D 's errors is the reward for G. This process continues until an equilibrium is formed and D's training is optimized. An example of a GAN is demonstrated in Fig. 10. Guan and Loew [183] used the GAN to create synthetic mammographic images from the digital database for screening mammography (DDSM) for the purpose of image augmentation. Fan et al. [184] aimed to generate superresolution ADC images and evaluate their clinical utility by conducting a radiomics investigation to predict the histologic grade and position of BC. Mukherkjee et al. [185] suggested a combination of three different GANs to overcome the problem of fetching the localized features in the latent representation of the image. Güven et al. [186] proposed a 3D GAN model to map the input MRI images into a common feature space.

However, the main disadvantage of the GAN approach is that it is harder to train, and providing various types of data continuously to check the accuracy is essential.
![img-11.jpeg](img-11.jpeg)

Fig. 10. An example of a GAN.

# 6.5 Radial basis function Networks 

RBF networks are a form of artificial neural network that is widely employed to solve function approximation problems. RBNs differ from other neural networks in that they have a universal approximation and learn faster. The input layer, the hidden layer, and the output layer make up an RBF network, which is a form of feed-forward neural network (FFNN) with three layers [187], [188]. An RBF net is a 2-layer network and these networks are not suffering from local minima as multi-layer perceptron (MLP). The input is fully connected to a hidden layer and the output of the hidden layer performs a weighted sum to output. Gaussian RBF is in the inside of hidden layer neurons. An example of a Radial basis function Network is demonstrated in Fig. 11 .
![img-12.jpeg](img-12.jpeg)

Fig. 11. An example of a radial basis function network.
Kanojia \& Abraham [189] introduced a model for the automatic detection of malignancy in histopathological images according to image-processing techniques and RBFN. Ng and Kee [190] suggested a multi-pronged approach comprising linear regression, RBFN, and receiver operating characteristic (ROC) analysis to evaluate thermograms. In fact, the suggested technique was constructed on the ANN and bio-statistical methods. Yavuz et al. [191] classified the BC data samples into malignant/benign through the RBFN, generalized regression neural network (GRNN), and FFNN. Kaymak et al. [192] developed a methodology for classifying BC images based on the BPPN and utilized RBFN to improve the efficiency of the automatic classification of

BC images. Although the time of training is faster in the RBF network, classification is slow compared to MLP due to the fact that every node in the hidden layer has to calculate the RBF function for the input sample vector during classification. The main disadvantage is that RBF networks entail an acceptable coverage of the input space by radial basis functions.

# 6.6 Deep Belief Networks 

Deep belief networks (DBNs) were introduced to provide a solution for problems of conventional neural networks in deep layered networks, which are including having a large number of training datasets, slow learning, and getting stuck in local minima due to poor parameter selection [43], [193]. Fig. 12 depicts a classic DBN for deep features. Based on Fig. 12, there are no connections between two units in the same layer; however, a complete set of connections exists between two adjacent layers. The contextual features from neighboring pixels or spectral signatures of each pixel can be used as the input. Each layer outputs a characteristic of the data it receives. The DBN is a probabilistic generative model that generates a joint probability distribution based on measurable data and labels. To initialize the deep network, a DBN uses an effective layerby-layer greedy learning technique and then fine-tunes all of the weights together with the desired outputs.

Abdel-Zaher et al. [194] represented a CAD scheme for BC detection based on an unsupervised DBN which is followed by backpropagation supervised. Also, the Liebenberg Marquardt learning function was utilized to construct a back-propagation neural network and weights are initialized from the DBN path. Al-antari et al. [195] suggested a BC diagnosis system based on the DBN that detects breast tissue areas automatically and classifies them as normal, malignant, or benign. Ronoud and Asadi [196] introduced E(T)-DBN-ELM-BP and E(T)-DBN-BP-ELM as two new evolutionary approaches that solve the first problem by incorporating DBN and an extreme learning machine (ELM) classifier. However, DBNs have the drawback of not accounting for the two-dimensional structure of an input image, which can have a major impact on their output.

![img-13.jpeg](img-13.jpeg)

Fig. 12. An example of a DBN.

# 7. Breast cancer datasets 

Now that we have seen the different ML techniques used for DC detection and diagnosis, in this section we will have a look at the most popular benchmark datasets used by these techniques to validate their results.

The BC dataset serves as a valuable tool in cancer-related research. Therefore, providing a good and high-quality dataset will allow for better detection, diagnosis and treatment of cancer. There are two main types of datasets used in this field: public and private. These datasets are based on different image types (MRI, sonography, mammography, etc.) and data. Breast cancer digital repository (BCDR), DDSM, mammographic image analysis society (MIAS) are the popular databases that have been widely used in this field. The available breast datasets are elaborated in Table 2.

Table 2. Most popular datasets used for BC detection.



703

# 8. Performance measures 

The performance validation of the classification, prediction, or segmentation techniques can be accomplished by employing various techniques for validating the achieved results. The most popular and broadly employed performance criteria include Specificity, Accuracy, Recall (Sensitivity or True Positive Rate), Precision, Confusion Matrix (CM), and Dice Similarity.

CM is broadly used to give vital information about correct and estimated results created by different techniques for classification or segmentation purposes. An example of a CM matrix for a two-class classification task is indicated in Table 3.

Table 3. Details of classification criteria for breast tumor segmentation.


Here, FN, TN, FP, and TP can be defined as:
TP: Accurately categorized or segmented breast cancer cells as breast cancer cells.
TN : Accurately categorized or segmented normal tissue as normal tissue.
FN : Incorrectly categorized or segmented normal tissue as breast cancer cells.
FP: Incorrectly categorized or segmented breast cancer cells as normal tissue, where Equations (1)-(5) represents their formulas.
$\operatorname{Recall}=\left(\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}}\right)$,
$\operatorname{Precision}=\left(\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}}\right)$,
$\operatorname{Accuracy}=\left(\frac{\mathrm{TN}+\mathrm{TP}}{\mathrm{TP}+\mathrm{TN}+\mathrm{FP}+\mathrm{FN}}\right)$,
$\operatorname{Dice}=\left(\frac{2 \times \mathrm{TP}}{(2 \times \mathrm{TP})+\mathrm{FN}+\mathrm{FP}}\right)$,
$\operatorname{Specificity}=\left(\frac{\mathrm{TN}}{\mathrm{TN}+\mathrm{FN}}\right)$.

# 9. Discussion and conclusion 

BC is one of the most common cancers in the world and among American women in particular, according to the American Cancer Society (ACS). Therefore, the early detection of BC is essential for the effective management of the disease besides reducing the number of deaths. Mammography is one of the screen methods to recognize the boundaries or the contour of benign and malignant masses. In fact, screening mammograms are capable of finding many BCs at an earlier stage before the symptoms are developed.

Since the diagnosis of abnormal cases of BC is tough even for experienced radiologists, CAD is considered as an interdisciplinary technology that combines methods of ML and computer vision

by radiological image processing. The most important part of image processing is segmentation which extracts the identified pixels of organs or lesions from background medical images. In this work, we highlighted and explained the different categories of ML segmentation methods including supervised, unsupervised, and DL. The different techniques and algorithms belonging to each category were defined, and the strengths and weaknesses of these techniques were also highlighted. Furthermore, we also surveyed some state-of-the-art works that used each of these techniques for BC detection in the last decade.

Based on our review of the state-of-the-art works, we were able to find that SVM, RF, and Linear regression are the most popular supervised techniques used for BC segmentation since 2015. In addition, K-mean and thresholding techniques are taken into account as commonly used unsupervised methods in the last seven years. Moreover, our review has also shown that CNNs are considered as the most popular DL approach used in the field of BC segmentation. This was reflected by the significant increase in the number of published papers in the last seven years. This is due to the efficiency of the DL approaches and the accuracy and reliability of their results.

Furthermore, the most popular benchmark datasets used by the different ML techniques for BC segmentation were also outlined. This research serves as a basis and starting point for researchers looking at using ML techniques in the medical field and particularly for BC detection and recognition.

Finally, while there is a lot of work on BC segmentation using ML, particularly DL techniques, there is still a lot to be done to improve these techniques in terms of both accuracy and execution time to allow them to reach their full potential and help further the field of BC segmentation and the medical field in general.

# Acknowledgement 

This publication has emanated from research [conducted with the financial support of/supported in part by a grant from Science Foundation Ireland under Grant number No. 18/CRT/6183 and is supported by the ADAPT Centre for Digital Content Technology which is funded under the SFI Research Centres Programme (Grant 13/RC/2106/_P2), Lero SFI Centre for Software (Grant 13/RC/2094/_P2) and is co-funded under the European Regional Development Fund. For the purpose of Open Access, the author has applied a CC BY public copyright licence to any Author Accepted Manuscript version arising from this submission.

The authors have no conflicts of interest to declare that are relevant to the content of this article.

# Author Contributions 

Conceptualization: Malika Bendechache and Annalina Caputo; Data curation: Zahra Arshadi; Formal analysis: Saeid Jafarzadeh Ghoushchi, Erfan Babaee Tirkolaee, and Zahra Arshadi; Investigation: Ramin Ranjbarzadeh, Shadi Dorosti, Erfan Babaee Tirkolaee, and Sadia Samar Ali; Methodology: Ramin Ranjbarzadeh, Shadi Dorosti; Supervision: Annalina Caputo and Malika Bendechache; Validation: Ramin Ranjbarzadeh, Annalina Caputo, and Saeid Jafarzadeh Ghoushchi; Writing - review \& editing: Ramin Ranjbarzadeh, Annalina Caputo, Malika Bendechache, Sadia Samar Ali, and Erfan Babaee Tirkolaee.

## Declaration of interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data Availability

All datasets available online in public repositories and used by many studies.
