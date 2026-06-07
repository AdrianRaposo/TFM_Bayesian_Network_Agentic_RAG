# scientific reports 

## OPEN Machine learning and computer vision technology to analyze and discriminate soil samples

Sema Kaplan ${ }^{1}$, Ewa Ropelewska ${ }^{2}$, Seda Günaydın ${ }^{1}$, Kadir Sabancı ${ }^{1}$ \& Necati Çetin ${ }^{1,2}$

Soil texture is one of the most important elements to consider before planting and tillage. These features affect the product selection and regulate its water permeability. Discrimination of soils by determining soil texture features requires an intense workload and is time-consuming. Therefore, having a powerful tool and knowledge for texture-based soil discrimination could enable rapid and accurate discrimination of soils. This study focuses on presenting new models for 6 different soil sample groups (Soil_1 to Soil_6) based on 12 different machine learning algorithms that can be utilized for various problems. As a result, overall accuracy values were determined as greater than 99.2\% (Trilayered Neural Network). The greatest accuracy value was found in Bayes Net (99.83\%) and followed by Subspace Discriminant ( $99.80 \%$ ). In the Bayes Net algorithm, MCC (Matthews Correlation Coefficient) and F-measure values were obtained as 0.994 and 0.995 for Soil_4 and Soil_6 sample groups while these values were 1.000 for other soil groups. Soil types can visually vary based on their texture, mineral composition, and moisture levels. The variability of this can be influenced by fertilization, precipitation levels, and soil cultivation. It is important to capture the images in soil conditions that are more stable. In conclusion, the present study has proven the feasibility of rapid, non-destructive, and accurate discrimination of soils by image processing-based machine learning.

Keywords Soil, Machine learning, Multi-object detection, Texture, Image processing
Agriculture has a strategic importance in the development of humanity, thus, is among the most important sectors of the world. Soils provide an environment for plant nutrients, water, and seed germination thus, are the main sources of agricultural production. Considering climate change-induced migrations, ecology and urban development, soil properties should be well-known for sustainable agriculture ${ }^{1,2}$. The biological, physical and chemical attributes of soils must be suitable to fulfill their functions and to provide soil-dependent ecosystem services. Advanced intensive farming practices cause soils to become increasingly prone to degradation ${ }^{3}$.

Soil texture is a physical soil property that expresses the percentage of individual particles within the soil mass. Texture is a critical factor with significant effects on physical and chemical characteristics, including primarily soil-water balance, germination, root development ${ }^{4}$, cation exchange capacity ${ }^{5}$, aggregation ${ }^{6}$ and erosion susceptibility ${ }^{1,7}$. Texture can traditionally be approximated by the "texture by feel" method, depending on the experience of the person performing the application in the field ${ }^{8}$. Detailed and accurate analysis is made in a laboratory using a hydrometer ${ }^{9}$ or pipette method ${ }^{10}$. These methods are costly and require some time to determine soil texture. They are also non-environment friendly methods since chemicals are used to provide dispersion. With the increase in application areas of new technologies in agriculture, developments are achieved in agricultural production. In this sense, precision farming practices, which are used more and more frequently, provide advantages to researchers in terms of developing reliable, cost-effective, and faster ways to measure and characterize soil properties ${ }^{11-14}$. Accurate definition of soil properties is quite a significant issue for optimum conditions and sustainable use of soil, which is a natural resource. Recently, textural properties have been determined using sensors ${ }^{15,16}$. Also, Aitkenhead et al. ${ }^{17}$ estimated the texture of the soil profile using images obtained from a smartphone, although it could not achieve high accuracy rates. Heterogeneity in field conditions has been the main obstacle factor limiting the immediate use of methods. Artificial intelligence algorithms emerge as models

[^0]
[^0]:    ${ }^{1}$ Department of Soil Science and Plant Nutrition, Faculty of Agriculture, Erciyes University, Kayseri, Turkey. ${ }^{2}$ Skierniewice, Poland ${ }^{3}$ Department of Biosystems Engineering, Faculty of Agriculture, Erciyes University, Kayseri, Turkey. ${ }^{4}$ Electrical and Electronics Engineering, Karamanoglu Mehmetbey University, Karaman, Turkey. ${ }^{5}$ Department of Agricultural Machinery and Technologies Engineering, Faculty of Agriculture, Ankara University, Ankara, Turkey. ${ }^{6}$ Ewa Ropelewska is an independent researcher. ${ }^{17}$ email: necati.cetin@ankara.edu.tr

that transform traditional methods. They are applied for data analysis in many areas and allow researchers to analysis at reliable limits with minimum soil preparation^{18}.

Artificial intelligence is the approach that imitates the human brain and can make decisions and finalize the process in the face of new formations by transferring human characteristics such as image perception, speech, recognition, learning, and thinking to the digital environment. In other words, artificial intelligence is a thinking and decision-making model created by computer algorithms that can think just like humans^{19,20}. Machine learning is the performance of a specific task through the acquisition and interpretation of extensive data by computer systems. With the advent of machine learning and image processing, it is possible to efficiently categorize soil samples^{21}. Machine learning comes to the fore in subjects such as image perception, speech, and recognition^{22}. Classification processes are carried out by processing images, and videos through machine learning algorithms. Generally, in soil discrimination by machine learning algorithms, the following steps are followed respectively, image acquisition, segmentation, feature extraction, and ground classification.

In the literature, there are a limited number of reports that extensively examine classification of soil by using artificial intelligence approach such as adaboost, tree, and artificial neural network algorithms^{23}, support vector machine^{23,24}, artificial neural network^{25}, random forest^{26}, and back-propagation neural network^{27}. Additionally, Khatti and Grover^{28} made model recommendations for geotechnical designers/engineers to develop an optimum performance flexible computational model to predict soil properties. However, no study has been reported in which detailed comparison of machine learning algorithms in soil classification. The main aim of this study is (I) to discriminate the soil samples with the use of machine learning and image processing operations, (II) to introduce a new model for soil discrimination, and (III) to detailed comparison of machine learning models. The innovative approach involving image analysis and artificial intelligence to distinguish soil samples. Thus, the soil discrimination was performed in a robust, inexpensive, and non-destructive. The novelty of this study is related to the determination of texture parameters (about 2172 textures for 12 color channels for each soil image) by image analysis, and the classification of soil samples based on textures from the individual color channels of the images using various machine learning and neural network models.

## Materials and methods

### Soil sampling

From different locations, between 0 and 30 cm depth of disturbed samples were taken. The soil samples were homogenized by passing them through a 2 mm sieve after being air-dried in the laboratory at around 22--24 °C temperatures. To get an accurate assessment of the soil conditions, soil samples from various locations were analyzed for pH, electrical conductivity (EC)^{29}, calcium carbonate content (CaCO_{3})^{30}, and soil organic carbon (SOC) content^{31}. Soil texture was determined with the use of Bouyoucus hydrometer method, which is based on the principle of finding the ratios of dispersed clay (< 0.002 mm), silt (0.002--0.05 mm), and sand (0.05--2 mm) particles^{9}. Six groups of soil samples as Soil_1 (38° 50′ 27.8″ N 35° 11′ 58.9″ E), Soil_2 (38° 26′ 39.7″ N 35° 32′ 41.0″ E), Soil_3 (38° 39′ 48.8″ N 35° 34′ 02.0″ E), Soil_4 (38° 39′ 48.8″ N 35° 34′ 02.0″ E), Soil_5 (38° 47′ 25.1″ N 35° 39′ 14.5″ E) and Soil_6 (38° 51′ 08.6″ N 35° 44′ 36.2″ E) which have the similar texture (sandy loam) and taken from six different locations, were selected from the soils whose sand, silt and clay ratios were determined and they were allocated to be studied with machine learning methods. Flow chart of the study is given in Fig. 1.

## Methods

### Image acquisition system

In the present study, the image acquisition system was composed of a digital CCD (Charge-Coupled Device) camera-lens (Nikon D5600, and 18--145 mm Nikon AF-S Nikkor, Japan), lens, tripod, imaging platform and lighting equipment. To capture without any shadows, images were taken in a dark condition^{32}. Soil samples were placed in petri plate. Images were captured using a camera that was mounted vertically at a fixed height of 50 cm. The studied soil sample groups are given in Fig. 2. The ‘jpeg' file format is used to save a total of 600 high-resolution images and 100 images were used for each soil type for texture analysis.

### Image processing

In total, the used dataset included 600 images (100 images for each of 6 soil samples). The soil images were processed to extract texture parameters. The images were originally saved in the BMP file format after the light backdrop was changed to black. It was performed in MATLAB R2023a (MathWorks, Inc. Natick, MA, USA). Then, the images could be easily segmented into the black background and lighter soil samples. Soil samples were separated from the background and each sample was considered as one region of interest (ROI). This step was carried out using the MaZda software^{33--35}. MaZda was also used for the conversion of soil images to individual color channels R, G, B, L, a, b, X, Y, Z, U, V, and S. In the case of each soil image in each channel, 181 image textures based on the histogram, co-occurrence matrix, autoregressive model, run-length matrix, gradient map, and Haar wavelet transform were computed, so that a total of 2172 texture attributes were obtained for each soil sample.

### Machine learning approaches

Image texture parameters after selection were used to distinguish soil samples. Machine learning algorithms were modeled by MATLAB R2023a (MathWorks, Inc. Natick, MA, USA) and WEKA 3.8.4 (Machine Learning Group, University of Waikato, Hamilton, New Zealand). The texture selection was carried out in WEKA using the Correlation-based Feature Selection and Best First subset evaluator. In total, 60 attributes were selected from a set of 2172 texture parameters so that the ratio of the number of attributes to instances was 1:10. The set of the most important features for classification included 7 textures of images in color channel R, 5 textures from color

![img-0.jpeg](img-0.jpeg)

Figure 1. Flow chart of the study.

channel *G*, 3 textures from color channel *B*, 2 textures from color channel *L*, 5 textures from color channel *a*, 3 textures from color channel *b*, 4 textures from color channel *X*, 4 textures from color channel *Y*, 4 textures from color channel *Z*, 6 textures from color channel *U*, 11 textures from color channel *V*, and 6 textures of images in color channel *S*.

MATLAB was used to build the classification models related to groups of Trees, Naive Bayes, SVM (Support Vector Machine), KNN (K Nearest Neigbors), Ensemble, and Neural Networks. For classification, a test mode of tenfold cross-validation was applied. For training and testing the algorithms, the dataset was randomly divided into 10 parts, and each part was treated in turn as the test set, and the remaining nine parts as the training sets. The learning was performed a total of 10 times using different training sets. The overall error was estimated as the average of 10 error estimates. Ten folds are generally appropriate to ensure the reproducibility of results and obtain the best error estimate^{36}. The models providing the highest accuracies were chosen. The following models and parameters were selected:

![img-1.jpeg](img-1.jpeg)

**Figure 2.** Soil samples used in the study.

- Fine Tree—maximum number of splits: 100; split criterion: Gini's diversity index; Surrogate decision splits: off;
- Quadratic SVM—kernel function: quadratic; kernel scale: automatic; box constraint level: 1; multiclass method: one-vs-one; standardize data: yes;
- Fine KNN—number of neighbors: 1; distance metric: Euclidean; distance weight: equal; standardize data: yes;
- Subspace Discriminant (Ensemble)—Ensemble method: subspace; learner type: discriminant; number of learners: 30; subspace dimension: 31;
- Narrow Neural Network—number of fully connected layers: 1; first layer size: 10, activation: ReLU; iteration limit: 1000; regularization strength (Lambda): 0; standardize data: yes;
- Wide Neural Network—number of fully connected layers: 1; first layer size: 100; activation: ReLU; iteration limit: 1000; regularization strength (Lambda): 0; standardize data: yes;
- Bilayered Neural Network—number of fully connected layers: 2; first layer size: 10; second layer size: 10; activation: ReLU; iteration limit: 1000; regularization strength (Lambda): 0; standardize data: yes;
- Trilayered Neural Network—number of fully connected layers: 3; first layer size: 10; second layer size: 10; third layer size: 10; activation: ReLU; iteration limit: 1000; regularization strength (Lambda): 0; standardize data: yes.

For these models, confusion matrices, overall accuracies, TPR (True Positive Rate) and FNR (False Negative Rate) were determined.

The following step was created classification models by WEKA machine learning software^{36-38}. Different algorithms from the groups of Trees, Bayes, Rules, Functions, and Meta were tested. Tenfold cross-validation was employed as the test mode. The most successful algorithms were Random Forest from the group of Trees, PART from the group of Rules, Bayes Net from the group of Bayes, and Logistic from the group of Functions. The following parameters of the algorithms were set:

- PART—batchSize: 100; debug: False; binarySplits: False; doNotCheckCapabilities: False; seed: 1; confidenceFactor: 0.25; reducedErrorPruning: False; numFolds: 3; minNumObj: 2; unpruned: False; useMDLcorrection: True;
- Random Forest—bagSizePercent: 100; batchSize: 100; doNotCheckCapabilities: False; debug: False; maxExecutionSlots: 1; numIterations: 100; seeds: 1; storeOutOfBagPredictions: False; calcOutOfBag: False; breakTiesRandomly: False;
- Bayes Net—searchAlgorithm: K2 -P 1 -S BAYES; batchSize: 100; doNotCheckCapabilities: False; debug: False; useADTree: False; estimator: SimpleEstimator -A 0.5;
- Logistic—debug: False; batchSize: 100; doNotCheckCapabilities: False; ridge: 1.0E-8; useConjugateGradientDescent: False.

# Model performance evaluation 

The overall accuracies, the confusion matrices with accuracies for 6 soil classes, and values of TPR (True Positive Rate), FPR (False Positive Rate), Precision, F-Measure, and MCC (Matthews Correlation Coefficient) and (Eqs. 1-8) were determined ${ }^{39-41}$.

$$
\begin{gathered}
\text { Accuracy }=(\mathrm{TP}+\mathrm{TN}) /(\mathrm{TP}+\mathrm{FP}+\mathrm{TN}+\mathrm{FN}) \\
\mathrm{TPR}(\text { Recall })=\mathrm{TP} /(\mathrm{TP}+\mathrm{FN}) \\
\mathrm{FPR}=\mathrm{FP} /(\mathrm{FP}+\mathrm{TN}) \\
\text { Precision }=(\mathrm{TP} / \mathrm{TP}+\mathrm{FP}) \\
\mathrm{F}-\text { Measure }=2 \mathrm{TP} /(2 \mathrm{TP}+\mathrm{FP}+\mathrm{FN}) \\
\mathrm{MCC}=((\mathrm{TP} \times \mathrm{TN})-(\mathrm{FN} \times \mathrm{FP})) / \sqrt{((\mathrm{TP}+\mathrm{FN})} \\
\times(\mathrm{TN}+\mathrm{FP}) \times(\mathrm{TP}+\mathrm{FP}) \times(\mathrm{TN}+\mathrm{FN}))
\end{gathered}
$$

where: TP, True Positive; TN, True Negative; FP, False Positive; FN, False Negative.

## Results and discussion

Some properties of studied soil sample groups are presented in Table 1. The highest pH and EC values were determined from Soil_1 sample class with the values of 8.46 and $0.827 \mathrm{ds} \mathrm{m}^{-1}$. Soil_5 had the greatest $\mathrm{CaCO}_{3}$ ( $21.120 \%$ ) and organic matter ( $5.95 \%$ ). Soil_1 and Soil_3 had the greatest phosphorus with the values of 5.494 and 5.179 , respectively, while the lowest value was found as 2.545 in Soil_5 sample class. Clay, silt, and sand values varied from 10.71 to $13.94,18.18$ to 28.28 and 59.60 to 67.91 , respectively.

In this study, two different ways were followed in the analysis. In the first method, Fine Tree, Quadratic SVM, Fine KNN and Subspace Discriminant algorithms and neural network algorithms as Bilayered Neural Network, Wide Neural Network, Narrow Neural Network, and Trilayered Neural Network were performed by using MATLAB. In the second method, PART, Random Forest, Bayes Net, Logistic algorithms were carried out by using WEKA. A total of 12 algorithms were modeled on soil samples and the results were compared in detail.

The overall accuracy of the Fine Tree algorithm was determined as $99.7 \%$. Herein, $1 \%$ of FNR was found in Soil_1 and Soil_4 samples, while other sample groups were classified with accuracies of $100 \%$. The overall accuracy value for Quadratic SVM and Fine KNN algorithms was obtained as $99.7 \%$. In these algorithms, Soil_4 and Soil_6 soil groups were classified with a value of $99 \%$, while other soil groups were classified as $100 \%$. Among all algorithms, the Subspace Discriminant algorithm had the greatest overall accuracy with a value of $99.8 \%$. In this algorithm, all soil groups were classified with $100 \%$ accuracy except for Soil_4 (TPR:99\%) samples (Fig. 3). In the neural network algorithms, the overall accuracy of Wide Neural Network, Narrow Neural Network, and Bilayered Neural Network was determined as $99.5 \%$. In all these algorithms, the TPR was found to be $99 \%$ and $98 \%$ for Soil_4 and Soil_6, respectively, and $100 \%$ for all other soil samples. The overall accuracy of Trilayered Neural Network ( $99.2 \%$ ) was lower than other neural network algorithms. In addition, the FNR values of the Soil_1, Soil_4, Soil_5, and Soil_6 algorithms were revealed as $1 \%, 1 \%, 2 \%$ and $1 \%$, respectively, while the Soil_2 and Soil_3 samples are classified with accuracy of $100 \%$ (Fig. 4).

Average accuracy and confusion matrices of PART, Random Forest, Bayes Net and Logistic algorithms are presented in Table 2 and model performance results are given in Table 3. The PART algorithm classified the studied soil samples with a value of $99.67 \%$. Precision values were found to be 0.990 for Soil_5 and Soil_6, while 1.000 for other soil groups supported these findings. While FPR values were obtained as 0.002 in Soil_5 and Soil_6 classes, it was obtained as 0.000 in all other soil classes. The highest MCC and F-Measure values were found to be 1.000 in Soil_1, Soil_2 and Soil_3 classes. The lowest MCC and F-Measure values were determined in Soil_6 with 0.988 and 0.990 , respectively. In the Random Forest algorithm, the average accuracy value was found to be $99.67 \%$. For this algorithm, MCC and F-Measure values were obtained as 0.988 and 0.990 for Soil_4 and Soil_6, respectively, and 1.000 for other soil groups. Soil_1, Soil_2, Soil_3, and Soil_5 had the greatest FPR with the value of 1.000 . However, Soil_5 and Soil_6 had the highest FPR values as 0.002 . In this machine learning group, Bayes


Table 1. Some properties of studied soil samples.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** Confusion matrices—selected traditional machine learning models (Overall accuracies: Fine Tree—99.7%, Quadratic SVM—99.7%, Fine KNN—99.7%, Subspace Discriminant—99.8%).

Net algorithm had the greatest average accuracy and model performance results. The average accuracy value of Bayes Net algorithm was determined as 99.83%. Moreover, the FPR value was obtained as 0.990 in the Soil_6 samples, and MCC and F-Measure values were determined as 0.994 and 0.995 for Soil_4 and Soil_6, while these values were found to be 1,000 in the other soil groups. The precision value was found as 0.990 for Soil_4 group, and this value was set as 1,000 for other algorithms. Among these machine learning groups, Logistic algorithm had the lowest average accuracy with a value of 99.50%, and TPR values were obtained as 0.990 and 0.980 for Soil_4 and Soil_6, respectively. MCC values were also determined as 0.994, 0.988 and 0.982 for Soil_1, Soil_4 and Soil_6, respectively. The lowest F-Measure values were obtained as 0.985 in Soil_6. Soil_6 was followed by Soil_4 and Soil_1 with the values of 0.990 and 0.995, respectively. Soil_1, Soil_4, and Soil_6 had the lowest Precision values as 0.990 while the Soil_2, Soil_3, and Soil_5 had the greatest Precision values as 1.000.

Considering overall accuracy values and performance metrics, the most successful models were BayesNet (99.83%), Subspace Discriminant (99.80%), Quadratic SVM (99.7%), Fine KNN (99.7%) and Fine Tree (99.7%), respectively. In addition, among the neural network models, Narrow, Wide and Bilayered Neural Networks were more successful with the value of 99.5%, while Trilayered Neural Network was the least successful model with the value of 99.2%.

For the soil classification using soil properties (moisture content, specific gravity, clay content, plastic, void ratio, and liquid limit parameters) and machine learning methods, Pham et al.^{23} used Adaboost, Tree and artificial neural network (ANN) modeling. The authors indicated that the developed adaboost model showed that it could well classify the soil and, in this model only 11 samples were not correctly identified among the total 88 data. Similar with the present study, Barman & Choudhury^{24} focused on texture properties of soil and classified by image analysis and support vector machine. According to their result of multi-class classification, the average percentage of accuracy ranges between 81.25% and 96.84%. Li et al.^{22} reported soil classification based on machine learning algorithm, and authors compared SVM and CNN (Convolutional Neural Network). CNN classification results were more successful than the SVM with the classification results between 85.91% and 95.58%.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Confusion matrices—selected neural network models. (Overall accuracies: Narrow Neural Network—99.5%, Wide Neural Network—99.5%, Bilayered Neural Network—99.5%, Trilayered Neural Network—99.2%).

in CNN, and between 88.37% and 91.16% in SVM. Comply to the present study, Azizi et al.^{25} studied deep learning to classify aggregates of any size in specific classes. The authors stated to train the Inception-v4, ResNet50, VggNet16, and CNN, architects were utilized, and the accuracies were above 95%, however the greatest accuracy value was found by ResNet50 (98.72%).

Bahrens et al.^{26} used a deep learning approach for digital soil mapping and random forest. The extended Gaussian pyramid and mixed scaling produced the best-performing set of covariates, and deep learning modeling produced the most accurate estimates, on average 4–7 percent more accurate than random forest, according to the experiments carried out by the authors using three different datasets. Mengistu and Alemayehu^{27} presented soil classification and characterization by sensor network approach and computer vision. The authors stated that characterization and classification are performed by Back-propagation neural network, the neural network was created with the 7 inputs and 6 neurons in it is output layer to classify soils, and 89.7% accuracy is achieved. Khatti and Grover^{42} compared the relationship between the index properties of the soil and CBR (California Bearing Ratio) with regression and ANN models in the literature. Researchers stated that the performance results (R) of simple regression, multi regression and artificial neural network models ranged between 0.5339 and 0.9736. It was emphasized that the highest result (0.9736-ANN) was found in the relevant study. Khatti and Grover^{42} also determined appropriate hyperparameters in ANN for the best prediction of soil geotechnical properties. Researchers have shown that ANN models based on the LM (Levenberg—Marquardt), BFG (BFGs Quasi—Newton) and SCG (Scaled Conjugate Gradient) algorithm require data sets with strong (0.61–0.80) to very strong (0.81–1.00) correlations. On the other hand, they revealed that ANN models based on GDM (Gradient Descent with Momentum), GD (Gradient Descent) and GDA (Gradient Descent Algorithm with Adaptive Learning) algorithms only need data sets with strong correlations to achieve a performance higher than 0.90. Bahmed et al.^{44} used Gaussian process regression (GPR), ensemble tree (ET), support vector machine (SVM), and decision tree

Table 2. Average accuracies and confusion matrices of soil sample class.


Table 3. Classification performance results of soil sample class.

(DT)), and hybrid (relevance vector machine (RVM)) to determine the most appropriate performance model for predicting the unconfined compressive strength (UCS) of the soil. They used relevance vector machine (RVM) models. The authors measured the performance of the models with three new index performance measures: the a20-index, the index of scatter (IOS), and the index of agreement (IOA). The PSO-optimized Laplacian kernel-based RVM model UCS16 has been identified as the optimal performance model after it outperformed all other models with higher a20-index (testing = 67.30, validation = 55.95), IOS (testing = 0.2799, validation = 0.3506) and IOA (testing = 0.8634, validation = 0.7795).

The physical attribute of soil texture is significant and highly changeable. It has a significant impact on numerous other soil properties, such as fertility and water retention capacity, which are highly relevant for agricultural productivity^{45,46}. Thus, understanding soil texture diversity is essential for managing soil, developing agricultural policies, and keeping an eye on how land use is affecting the ecosystem^{46,47}. Accurate evaluations of soil groups and soil loss are essential for reducing the effects of erosion and enhancing the fertility of agricultural fields^{48}. In the present study, many backgrounds were tried while obtaining images. In order to obtain better results, colors in which the petri dish is located, and the background color is completely different from the sample color were preferred. This was the most important limitation of the study. The developed techniques can be easily applied to different sample groups. In addition, the investigated technique can also be combined with spectroscopic approaches to achieve higher accuracy^{49}. In this way, very similar objects can be easily distinguished. Herein, an important point is to apply feature selection and determine the proper features for the input when working in many different band groups and color channels. Furthermore, spectra and textures can be reduced by downsampling multi-feature data. In this way, greatest classification or prediction success can be achieved.

Achieving to sustainable development, effective soil monitoring is essential. Machine learning and computer vision technologies are revolutionizing soil texture analysis by making it effective, accurate and accessible. These advances simplify soil assessment processes and increase the reliability of soil texture estimates, which is vital for informed decision-making in agricultural and environmental management. The integration of citizen science initiatives increases the accuracy and local validity of digital soil maps^{50}. Machine learning and computer vision advance the understanding and management of soil resources and provide solutions for sustainable land use practices and precision agriculture.

## Conclusion

Accurate and efficient soil texture classification is essential for sustainable land management, agricultural productivity, and environmental protection. This study utilizes machine learning approaches to determine soil samples and shows the detection accuracy without increasing enormous calculations. While the most successful results were obtained in Bayes Net and Subspace Discriminant algorithms, less successful results were found in the Trilayered Neural Network algorithm compared to the others. Different soil types may differ visually according to their texture, mineral and moisture content. This could vary according to fertilization, rainfall amount and soil tillage. For this reason, the images to be taken should be in more stable soil conditions. The design of soil type determination systems is step by step, then the control and optimization of the systems could be performed by machine learning models.

## Data availability

The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request.

Received: 30 April 2024; Accepted: 5 August 2024
Published online: 27 August 2024

# Author contributions 

S.K.: sources, methodology, formal analysis, investigation, writing; E.R.: software, data curation, methodology, formal analysis, visualization, and writing; S.G.: investigation, formal analysis, and writing; K.S.: software, formal analysis; N.Ç.: conceptualization, methodology, formal analysis, and writing.

## Competing interests

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# Additional information 

Correspondence and requests for materials should be addressed to N.Ç.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by-nc-nd/4.0/.
(c) The Author(s) 2024