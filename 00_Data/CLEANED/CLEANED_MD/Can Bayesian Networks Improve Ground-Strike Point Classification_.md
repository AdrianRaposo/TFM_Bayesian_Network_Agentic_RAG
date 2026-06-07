# Article 

## Can Bayesian Networks Improve Ground-Strike Point Classification?

Wandile Lesejane ${ }^{1}$, Hugh G. P. Hunt ${ }^{1, * *}$, Carina Schumann ${ }^{1 *}$ and Ritesh Ajoodha ${ }^{2 *}$


#### Abstract

check for updates Citation: Lesejane, W.; Hunt, H.G.P.; Schumann, C.; Ajoodha, R. Can Bayesian Networks Improve Ground-Strike Point Classification? Atmosphere 2024, 15, 776. https:// doi.org/10.3390/atmos15070776

Academic Editors: Vernon Cooray, Farhad Rachidi and Marcos Rubinstein

Received: 31 May 2024
Revised: 19 June 2024
Accepted: 24 June 2024
Published: 28 June 2024


## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 The Johannesburg Lightning Research Laboratory, School of Electrical and Information Engineering, University of the Witwatersrand, Johannesburg 2050, South Africa
2 School of Computer Science and Applied Mathematics, University of the Witwatersrand, Johannesburg 2050, South Africa

* Correspondence: hugh.hunt@wits.ac.za


#### Abstract

Studying cloud-to-ground lightning strokes and ground-strike points provides an alternative method of lightning mapping for lightning risk assessment. Various k-means algorithms have been used to verify the ground-strike points from lightning locating systems, producing results with room for improvement. This paper proposes using Bayesian networks (BNs), a model not previously used for this purpose, to classify lightning ground-strike points. A Bayesian network is a probabilistic graphical model that uses Bayes' theorem to represent the conditional dependencies of variables. The networks created for this research were trained from the data using a score-based structure-learning procedure and the Bayesian information criterion score function. The models were evaluated using confusion matrices and kappa indices and produced accuracy values ranging from $86 \%$ to $94 \%$ and kappa indices of up to 0.76 . While BN models do not outperform k-means algorithms, they offer an alternative by not requiring predetermined distances. However, the easy implementation of the k-means approach means that no significant gain is made by implementing the more complex Bayesian network approach.


Keywords: bayesian network; lightning; lightning location systems; ground-strike point; IEC62858

## 1. Introduction

Lightning locating systems (LLSs) employ multiple sensors to collect data from lightning return strokes, which are grouped into flashes as per the International Electrotechnical Commission (IEC) 62585 standards to create lightning density maps for risk assessment [1]. However, the aggregation of strokes into single flashes often leads to underestimation of lightning density, particularly when flashes consist of multiple strokes hitting different ground-strike points (GSPs) [1-5]. This underestimation has direct implications for risk assessments, which are crucial for mitigating lightning-induced hazards such as forest fires or damage to photovoltaic plants [6-10]. While LLSs utilize various triangulation techniques to locate strokes, these methods often suffer from significant uncertainty due to technical and observational errors [11]. To refine the accuracy of GSP identification, machine learning algorithms like variations of the k-means method have been employed [12,13]. These approaches have achieved high classification accuracies between $79 \%$ and $95 \%$ against ground truth data observed using high-speed cameras and LLS networks with high-performance metrics [13].

However, despite their accuracy, these algorithms are limited by their reliance on a predetermined distance threshold to distinguish whether a new stroke should be classified as a new ground-strike point. Choosing the threshold value should be based on the location accuracy of the network in question, but location accuracy can vary over the coverage region of a network greatly. Poelman et al. discuss this in detail along with the challenges of choosing a threshold value while investigating GSP activity over the entirety of Europe [3].

This also raises questions about the ability of algorithms to classify GSP if the LLS network performance is not at a peak level, which is often the case in developing countries [4,13].

In this research, we investigate an approach that does not require setting a threshold distance. This approach introduces Bayesian networks (BNs) as a novel approach to GSP analysis, exploring their potential to overcome the limitations of existing methodologies. Bayesian statistics and other machine learning techniques have been previously used to assess LLS performance [14,15,16,17,18], typically through Bayes' theorem with prior probabilities and likelihoods estimated from the literature, but never to address the problem of GSP classification. Unlike traditional methods, BNs do not require fixed thresholds and offer a flexible framework for modeling conditional dependencies among variables. By leveraging Bayesian statistics-which have been previously utilized in LLS performance assessments but not for GSP classification-this study employs BNs to elucidate the relationships between observable variables and the target variable: the previous strike point (PSP). The PSP categorizes a stroke into a new ground channel (NGC) or a pre-existing channel (PEC), which is critical for accurate stroke classification.

The paper begins with an overview of the current approaches to GSP classification and their performance assessments (Section 2). This is then followed by a description of the method used in the study-Bayesian network theory-the dataset used, and the implementation of the approach (Section 3). The performance results of the approach are then presented and summarized (Section 4), and finally, these results are compared with the known approaches and the effectiveness of the proposed approach is discussed in Section 5. The paper is then concluded.

# 2. GSP Algorithms 

Figure 1 is a schematic of the occurrence of a flash. Figure 1 b shows the flash hierarchy. If a single flash has four strokes, and three of the strokes hit the ground at the same point while one hits the ground at another point, there are two GSPs. Figure 1c depicts the locations of the strokes, while Figure 1d depicts the occurrence of the lightning flash over the period of time. Various studies have analyzed lightning ground-strike points using different methods and data sources and have obtained varied results. Common features across these studies include the number of reporting sensors, the time of reporting, the estimated distance, and the peak current of lightning discharges [19,20,21,22]. Campos et al. used data from the US National Lightning Detection Network to study multiple lightning ground contacts [20]. Matsui et al. analyzed negative flashes with multiple GSPs using the Japanese Lightning Detection Network [21]. Pedeboy et al. validated GSP identification using data from Austrian and French LLSs [22]. Nag et al. provided insights on LLS characteristics and validation techniques using global data [19]. Methods for GSP analysis include LLS techniques that combine the time of arrival and signal direction for geo-location [22], kmeans clustering for verification [22,23], and the groupGCP algorithm that sorts strokes by the semi-major axes (SMAs) [20]. Matsui et al. employed a propagation delay correction (PDC) technique to improve geo-location accuracy [21]. Nag et al. used self-referencing, ground truth data, video validation, and LLS performance comparisons [19].

Evaluation of these methods has shown varied performance, as shown in Table 1. For example, Matsui et al. found a mean of 3.5 strokes per flash with multiple GSPs [21]. Pedeboy et al. reported high discriminatory efficiency with matched GSP and lightning data [22]. Campos et al.'s GroupGCP algorithm achieved high performance efficiency for return strokes and full lightning flashes [20]. Nag et al. validated GSPs using multiple methods, including statistical analyses and video data [19]. The first algorithm classified new ground contact (NGC) strokes with $60.8-92.0 \%$ accuracy, while the second and third algorithms had ranges of $64.6-95.3 \%$ and $98.3-99.1 \%$, respectively. Pre-existing contacts (PECs) were classified with $63.8-79.3 \%$ accuracy by the third algorithm and $84.4-99.4 \%$ and $87.6-99.4 \%$ by the first and second algorithms, respectively. Overall, the algorithms had accuracy ranges of $79.9-94.4 \%[13]$.

![img-0.jpeg](img-0.jpeg)

Figure 1. A diagram that shows a flash with two GSPs and four strokes occurring over time, adapted from Valine and Krider [24]. Strokes 1, 2, and 4 are at GSP1, and stroke 3 is at GSP 2. (a) A lowresolution image of a lightning flash with multiple strokes, the strokes contact the ground at different points. (b) A diagram that is a schematic of a flash hierarchy adapted from Pédeboy [1]. It shows a single flash with two GSPs and four strokes. Strokes 1, 2, and 4 are at GSP1, and stroke 3 is at GSP 2. (c) Illustration of lightning flash with two GSPs. (d) Illustration of lightning occurrence over a period of time.

Table 1. A table of summarized results obtained using three algorithms used in the current literature [13].


## 3. Data and Methods

### 3.1. Bayesian Networks

Bayesian networks provide a compact representation of the joint probability distribution of variables, where each variable's conditional probability depends on its parent variables [25]. The joint probability of a Bayesian network is expressed as:

$$
P\left(x_1, x_2, \ldots, x_n\right) = \prod_{i=1}^{n} P\left(x_i | p x_i\right),
$$

where $x_i$ are variables, and $p x_i$ are their parent variables [26,27].

Figure 2 illustrates a Bayesian network with six variables. The joint probability is expanded using the Bayesian theorem chain rule and Equation (1):

![img-1.jpeg](img-1.jpeg)

**Figure 2.** A Bayesian network schematic diagram, adapted from Zhang and Poole [28]: $x_1$ and $x_2$ are parents of $x_3$, $x_3$ and $x_6$ are parents of $x_5$, and $x_4$ is a descendant of $x_3$.

Learning a Bayesian network involves obtaining a model that describes the joint probability distribution of variables using data samples. This step is crucial for density estimation, inference queries, specific predictions, and knowledge discovery [29]. Bayesian network models can be trained through structure learning and parameter learning. Parameter learning estimates the parameters of a fixed Bayesian network model from a complete dataset. It can be achieved using maximum likelihood estimation (MLE) or Bayesian statistics [29]. Inference reduces the global probability distribution to a conditional probability of observed variables, allowing probabilistic queries and data imputation [29,30].

Structure learning uncovers variable correlations. It includes score-based structure learning and treats each potential model as a statistical problem, using a scoring function to fit models to data. The model with the highest score is chosen [29]. Constraint-based structure learning assumes a Bayesian network represents variable independence. Conditional dependence and independence tests are run for all variables to create a suitable model [29]. Bayesian model averaging combines multiple models to obtain an average [29]. Bayesian networks utilize various algorithms for structure learning, such as hill climbing and tabu search. Tabu search optimizes graphical models by iteratively searching for the minimum of an objective function [31]. Bayesian networks rely on probabilistic model selection to identify the best-fitting model using scoring functions like the Gaussian log-likelihood, Akaike information criterion (*AIC*), and Bayesian information criterion (*BIC*). The Gaussian log-likelihood is defined as [32]:

$$
L_k = \sum_{i=1}^{n} \log f_k(x_i),
$$

where $f_{k}\left(x_{i}\right)$ is the Gaussian function:

$$
f\left(x_{i}\right)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{\frac{-1}{2} \frac{\left(x_{i}-x\right)^{2}}{\sigma^{2}}}
$$

The AIC function estimates the variance between the data used to generate the model and the fitted potential model [33]:

$$
A I C=-2 \ln L\left(\Theta_{i} \mid x\right)+2 k
$$

where $L$ is the likelihood function and $k$ is the number of model parameters.
BIC, similar to AIC, transforms the posterior probability of the model [34,35]:

$$
B I C=-2 \ln L\left(\Theta_{i} \mid x_{j}\right)+2 k \ln (n)
$$

where $k$ is the number of model parameters, $n$ is the number of data records, and $L$ is the likelihood function.

BIC was introduced for independent, identically distributed observations and linear models [36], assuming the likelihood is from the regular exponential family [29,34]. It selects a model by maximizing the posterior probability of a potential model from a dataset $[34,36,37]$. The posterior probability is described by:

$$
P\left(M_{i} \mid x_{j}\right)=\frac{P\left(x_{j} \mid M_{i}\right) P\left(M_{i}\right)}{P\left(x_{j}\right)}
$$

where $P\left(x_{j}\right)$ is the marginal probability distribution of the data and $P\left(M_{i} \mid x_{j}\right)$ is the marginal likelihood of the model [34,37].

Maximizing the posterior probability of a potential model and considering it as a continuous function gives:

$$
P\left(M_{i} \mid x_{j}\right)=\frac{P\left(M_{i}\right)}{P\left(x_{j}\right)} \int_{\Theta_{i}} L\left(\Theta_{i} \mid x_{j}\right) f\left(\Theta_{i} \mid M_{i}\right) d \Theta_{i}
$$

where the integral is the continuous function of the model's likelihood given its parameter vectors and prior distribution. From Equation (4), we have

$$
\begin{gathered}
P\left(M_{i} \mid x_{j}\right)=\frac{P\left(M_{i}\right)}{P\left(x_{j}\right)} \int_{\Theta_{i}} L\left(\Theta_{i} \mid x_{j j}\right) f\left(\Theta_{i} \mid M_{i}\right) d \Theta_{i} \\
-2 \ln P\left(M_{i} \mid x_{j}\right)=2 \ln P\left(x_{j}\right)-2 \ln P\left(M_{i}\right)-2 \ln \int_{\Theta_{i}} L\left(\Theta_{i} \mid x_{j j}\right) f\left(\Theta_{i} \mid M_{i}\right) d \Theta_{i}
\end{gathered}
$$

Expanding the integral using a Taylor expression gives:

$$
\begin{aligned}
\ln L\left(\Theta_{i} \mid x_{j}\right) & \approx \ln L\left(\Theta_{i} \mid x_{j}\right)+\left(\Theta_{i}-\Theta_{i}^{\prime}\right) \frac{\partial \ln L\left(\Theta_{i}^{\prime} \mid x_{j}\right)}{\partial \Theta_{i}} \\
& +\frac{1}{2}\left(\Theta_{i}-\Theta_{i}^{\prime}\right)\left[\frac{\partial^{2} \ln L\left(\Theta_{i}^{\prime} \mid x_{j}\right)}{\partial \Theta_{i} \partial \Theta_{i}^{\prime}}\right]\left(\Theta_{i}-\Theta_{i}^{\prime}\right)
\end{aligned}
$$

with $I=\left[-\frac{1}{n} \frac{\partial^{2} \ln L\left(\Theta_{i}^{\prime} \mid x_{j}\right)}{\partial \Theta_{i} \partial \Theta_{i}^{\prime}}\right]$, the integral becomes [34,37]:

$$
\begin{aligned}
\int_{\Theta_{i}} L\left(\Theta_{i} \mid x_{j}\right) f\left(\Theta_{i} \mid M_{i}\right) d \Theta_{i} & \approx L\left(\Theta_{i}^{\prime} \mid x_{j}\right) \int_{\Theta_{i}} \exp \left(-\frac{1}{2}\left(\Theta_{i}-\Theta_{i}^{\prime}\right)[I]\left(\Theta_{i}-\Theta_{i}^{\prime}\right)\right) \\
& \times f\left(\Theta_{i} \mid M_{i}\right) d \Theta_{i}
\end{aligned}
$$

Approximating the integral by its symmetry gives:

$$
\int_{\Theta_{i}} \exp \left(-\frac{1}{2}\left(\Theta_{i}-\Theta_{i}^{\prime}\right)\left[I\right]\left(\Theta_{i}-\Theta_{i}^{\prime}\right)\right) f\left(\Theta_{i} \mid M_{i}\right) d \Theta_{i}=(2 \pi)^{i / 2}|I|^{-\frac{1}{2}}
$$

Substituting Equation (7) into Equation (6), we obtain [34,37]:

$$
\begin{aligned}
S\left(M_{i} \mid x_{j}\right) & =-2 \ln P\left(M_{i}\right)-2 \ln \left(L\left(\Theta_{i}^{\prime} \mid x_{j}\right)(2 \pi)^{i / 2}|I|^{-\frac{1}{2}}\right) \\
& \approx-2 \ln L\left(\Theta_{i}^{\prime} \mid x_{j}\right)-2 k \ln n
\end{aligned}
$$

Bayesian networks do not require prior assumptions about the data and are suitable for small datasets. They show which features directly affect the target value and how features are interconnected, making them useful for prediction through inference.

# 3.2. Data 

The data used for this analysis were provided by the South African Lightning Detection Network (SALDN) in Johannesburg, South Africa, for the years 2017 to 2019 [12,38]. The dataset consists of 15 features and 1311 entries with no missing data, as described in Table 2. An additional feature, flash number, was used to categorize the lightning strokes according to IEC 62585 [1]. Strokes with an inter-stroke delay of 500 milliseconds and a maximum distance of 10 km between them were categorized as a single flash. The ground truth dataset is represented by the feature strike point, which was validated using high-speed cameras capturing events to the millisecond.

Table 2. Descriptions of data features.


Figure 3 shows an image representation of lightning flash 74 from the data over a map of Johannesburg. The red crosses indicate GSP locations of strokes captured by the LLSs. Figure 4 displays images of the two strike points captured by a high-speed camera. The time stamps indicate that the strokes occurred within a tenth of a second apart, confirming they are part of the same flash.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** A picture of flash 74 plotted on a Johannesburg map. Strokes at strike point 1 are enclosed in green triangles, and those at strike point 2 are enclosed in a blue rectangle. Note that the lower triangle is not included at the upper location due to a reported location error.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Images of strike point 1 and 2 from flash 74 captured with a high-speed camera by Dr. Carina Schumann [39,40]. (**a**) A low-resolution image of lightning stroke 1 at the first GSP (green triangle above) captured with a high-speed camera by Dr. Carina Schumann. (**b**) A low-resolution image of lightning stroke 2 at the second GSP (blue square above) captured with a high-speed camera by Dr. Carina Schumann. (**c**) A superimposed low-resolution image of strokes 1 and 2 at their respective GSPs.

The semi-major and semi-minor distances were converted from kilometers to degrees for consistency. Time was converted from hours:minutes:seconds to seconds to be read as a float. The dataset has 463 flashes, with 213 single-stroke flashes excluded as they do not have a PSP variable.

# 3.3. Methods 

The aim of this analysis was to determine the GSP of a stroke given the GSP of the previous stroke for flashes that have more than one stroke. To make such predictions, another feature was added: the previous strike point (PSP). First, the data were categorized according to the flashes, then single-stroke flashes were removed as they were not significant for the purpose of the project. The stroke labels in each flash were observed and were used to determine the value of the PSP. If a stroke label is the same as the previous one, PEC, then the PSP label for that entry is 1 ; if it is not the same, NGC, then the PSP label is 0 . The data have more strike points classified as NGCs than PECs: this is in alignment with the observation made in the research of global GSP characteristics in negative downward flashes [12], which then creates a class imbalance. It should also be noted that the initial stroke of each flash was removed since it does not have a PSP value.

BN-learn is an R package that is capable of Bayesian network modeling analysis by means of structure learning, parameter learning, and inference [41]. The package contains algorithms for data pre-processing, inference, parameter learning, and structure learning that combines the data and prior knowledge [41] that are necessary for Bayesian network modeling. It is capable of handling discrete Bayesian networks, Gaussian Bayesian networks, and conditional linear Gaussian Bayesian networks using real data [41].

Five Bayesian network models were created using the data. For each model, a k-fold cross validation was run 50 times on the data to obtain the mean classification errors and their standard deviations. This is done to evaluate how well the models are expected to perform. K-fold cross validation is a training method whereby the training data are divided into $k=10$ samples, then $k-1$ samples are trained while the other sample is used as the testing sample. The algorithm is repeated until all the samples have been used as the testing sample, then the average loss is calculated as the performance measure. The models were trained using a score-based structure-learning procedure with tabu search. The first model included all the variables and was trained from the raw data. The second model was trained with all the variables and with the date information set as the conditional dependencies of PSP. The third model excluded dates and times, while the fourth model excluded dates, times, and ellipse information. Both these models had the number of sensors and the degrees of freedom set as parent nodes of PSP. The last model was created using the time, strike point, PSP, latitude and longitude and ellipse information.

The algorithm used for creating the models involved a structure-learning procedure with tabu search and the Bayesian information criterion (BIC). The full code is available on GitHub: https://github.com/Lwano31/BN_models (accessed on 11 May 2024) [40,42]. The steps of the algorithm are summarized as follows:
i. Set up conditional dependencies from the data.
ii. Learn the best-fit directed acyclic graph (DAG) from data with dependencies.
iii. Perform cross validation on the DAG (data $=$ DAG, runs $=50$ ).
iv. Calculate the loss with target $=$ PSP.
v. Predict the output from the fitted DAG.
vi. Plot the DAG.
vii. Repeat the algorithm for the other models.

This is captured in the following code sample:

```
net = tabu(flash_data, score = 'bic-g')
graphviz.plot(net, shape = 'rectangle',
layout = 'fdp', highlight =
list(nodes = c("PSP", parents(net, "PSP")),
arcs = incoming.arcs(net, "PSP"),
col = "darkblue", fill = "tomato", lwd = 3))
bn.cv(data=flash_data, net,runs=50
loss.args = list(target = 'PSP'))
predicted = predict(bn.fit(net,flash_data), "PSP", flash_data)
```


# 3.4. Analysis 

The performance of the models was evaluated using a confusion matrix, which is suitable for binary classification models [43]. Figure 5 shows a schematic of a confusion matrix with the true and predicted class values. It computes the ratio of true positives (TPs), false positives (FPs), true negatives (TNs), and false negatives (FNs), allowing the calculation of performance measures such as accuracy, precision, recall, and F1-score.

## TRUE CLASS

![img-4.jpeg](img-4.jpeg)

Figure 5. A schematic of a confusion matrix, adapted from Mohajon [44].

$$
\begin{aligned}
\text { Precision } & =\frac{T P}{T P+F P} \\
\text { Recall } & =\frac{T P}{T P+F N} \\
F 1-\text { score } & =\frac{2 \times \text { Precision } \times \text { Recall }}{\text { Precision }+ \text { Recall }} \\
\text { Accuracy } & =\frac{T P+T N}{T P+T N+F P+F N}
\end{aligned}
$$

Balanced accuracy and kappa statistics were also used to evaluate model performance while taking into account the class imbalance [43,45].

## Baselines

The following baseline algorithms were used for comparison:

- Naive Bayes: constructs a Bayesian probabilistic model assuming all variables are independent [46];
- Multilayer perceptron (MLP): a neural network that assigns weights to multiple variables to produce a binary output [47];

- Logistic regression: similar to MLP but uses an activation function like sigmoid to obtain an output [47];
- Random tree: a decision tree generated from random datasets [48];
- Random forest: a combination of tree classifiers with random sampling [49];
- Sequential minimal optimization (SMO): optimizes a support vector machine (SVM) using Lagrangian multipliers [50].
The methods have various limitations due to the tools used and the type of data. The data are a hybrid of discrete and continuous data for which BN-learn has only one loss function that is suitable. BN-learn only has two algorithms for maxima and minima searches. Another limitation of BN-learn is that discrete nodes can only be parent nodes of continuous nodes: even with prior knowledge of a continuous node being a parent of a discrete node, the library does not allow that.


# 4. Results 

### 4.1. Directed Acyclic Graphs

Figures 6-10 are the Bayesian networks produced using a score-based structurelearning procedure on BNlearn with tabu search with a BIC scoring function that is suitable for data that are a hybrid of continuous and discrete data. The green highlighted nodes are the PSP, which are the target value and its parent node, and the edges from the parent nodes to the target node are highlighted in navy blue. In the first model, Figure 6, the probability distribution of PSP has a conditional dependence on the year. The second model, Figure 7, shows that PSP depends on the year, month, day, and number of sensors, and the third Bayesian network model, Figure 8, shows that in these, the probability distribution of PSP has a conditional dependence on the flash number and the number of sensors. The fourth model, Figure 9, shows that on this model, the probability distribution of PSP has a conditional dependence on the flash number and the number of sensors. In the last model, Figure 10, PSP is a parent node and has no dependence on other features.
![img-5.jpeg](img-5.jpeg)

Figure 6. Model 1 Bayesian network diagram. The parent node of PSP is the year, and the strike point is a descendant of PSP [40].

The first model (Figure 6) included all the variables and was trained from the raw data without conditional dependencies. The probability distribution of PSP shows condi-

tional dependence on the year. The descendant node of PSP is the semi-minor axis of the uncertainty ellipse.
![img-6.jpeg](img-6.jpeg)

Figure 7. Model 2 Bayesian network diagram. The parent nodes of PSP are the number of sensors, year, month, and day, while the strike point is a descendant of PSP [40].

The second model (Figure 7) included all the variables from the LLS data, but now, conditional dependencies were set for PSP. The model shows that PSP depends on the year, month, day, and number of sensors. The descendant node of PSP is the semi-minor axis of the uncertainty ellipse.
![img-7.jpeg](img-7.jpeg)

Figure 8. Model 3 Bayesian network diagram. The parent nodes of PSP are the number of sensors and flash number; PSP is a parent node of the strike point [40].

The third model (Figure 8) then excluded the year, month, day, and time features. The parent nodes of PSP are the number of sensors and degrees of freedom. The descendant node of PSP is the semi-minor axis of the uncertainty ellipse.
![img-8.jpeg](img-8.jpeg)

Figure 9. Model 4 Bayesian network diagram. The parent nodes of PSP are the number of sensors and flash number; PSP is a parent node of the strike point [40].

The fourth model (Figure 9) was then trained with selected LLS variables: latitude, longitude, peak current, chi-square, degrees of freedom, and number of sensors. The target value, PSP, has conditional dependencies on the degrees of freedom and number of sensors.
![img-9.jpeg](img-9.jpeg)

Figure 10. Model 5 network diagram. The parent node of the strike point is PSP [40].
Finally, the fifth model (Figure 10) was trained with the time, longitude, latitude, semimajor and semi-minor axes of the uncertainty ellipse, and the ellipse angle. The target value,

PSP, is a parent node with no conditional dependence on other features. The descendants of PSP are the time, longitude, and semi-major axis of the uncertainty ellipse.

# 4.2. Performance Measures 

The comparative performances of the models, as summarized in Table 3, reveal notable differences in accuracy, balanced accuracy, and kappa statistics. Model 2 stands out with the highest accuracy ( $93.9 \%$ ), balanced accuracy ( $88.0 \%$ ), and kappa statistic ( 0.76 ), indicating superior overall performance. This suggests that the specific features or algorithms used in Model 2 are more effective for this application compared to the others. In contrast, Model 1, while satisfactory, shows the lowest performance metrics in each category, which may signal potential areas for improvement, such as parameter tuning or feature selection. Models 3 and 4 demonstrate moderately high performance, with Model 4 slightly leading in accuracy but trailing in balanced accuracy compared to Model 3. Model 5, with performance metrics generally in the mid-range, offers a balance but highlights room for enhancement in balancing classification accuracy across different classes.

Table 3. Overall model performances with accuracy, balanced accuracy, and kappa statistic.


Table 4 details the predictive performance of the five models, highlighting their precision, recall, and F1-scores across two categories: new ground channel (NGC) and preexisting channel (PEC). Notably, Model 2 exhibits superior performance, with precision scores exceeding $80 \%$ for NGC and reaching $96.1 \%$ for PEC and closely mirrored by its recall and F1-scores. Conversely, Model 1, while effective for PEC predictions, shows room for improvement in NGC detection, indicating potential areas for model refinement. The detailed performance metrics, particularly the F1-scores, underscore the varying strengths of each model at balancing precision and recall, which are essential for optimizing GSP classification.

Table 4. Predictive performance of target values for each model with precision, recall, and F1-scores.


Figure 11 shows the box plots of the classification errors for the k-fold cross validation of the five BN models over 50 runs. The classification errors for each model are summarized in Table 5, which indicates the mean classification errors and standard deviations for a k value of 10 and 50 runs.

Table 5. K-fold cross validation results with mean classification errors and their standard deviations.


The classification errors of the models vary, with Model 1 having errors between 0.108 and 0.126, Model 2 having errors between 0.138 and 0.159, Model 3 having errors between 0.122 and 0.151, Model 4 having errors between 0.119 and 0.140, and Model 5 having errors between 0.118 and 0.132 .
![img-10.jpeg](img-10.jpeg)

Figure 11. Classification error bars with confidence intervals [40].

# 5. Discussion 

Model 1 (Figure 6) was trained using all variables and shows PSP dependence only on the year. It produced the lowest accuracy and kappa index, indicating that the year alone is insufficient. The model had the lowest mean classification error during k-fold cross validation, suggesting a narrow error range but limited predictive capability. Model 2 (Figure 7) included date information and the number of sensors as conditional dependencies. It achieved the highest accuracy ( $93.9 \%$ ) and kappa statistic ( 0.76 ), despite having the highest mean classification error. The classification error was evenly spread around the mean, suggesting higher uncertainty due to outliers. Model 3 (Figure 8) excluded date and time features and showed PSP dependence on the degrees of freedom and number of sensors. It produced the third-highest accuracy and kappa statistic, indicating reduced performance without time and date information. The classification error distribution suggested higher mean error uncertainty. Model 4 (Figure 9) excluded date, time, and ellipse information. It performed slightly better than Model 3, implying that ellipse information does not significantly affect PSP prediction. The classification error was similar to that of Model 3, with high mean error uncertainty. Model 5 (Figure 10) used only the ellipse information and time, with PSP as a parent node. It produced the lowest accuracy and kappa statistic but had a narrow error range, indicating consistent but limited performance.

Overall, Model 2 outperformed the others, showing that BNs benefit from set conditional dependencies. Class imbalance slightly affected all models, with lower precision,

recall, and F1-scores for NGC strokes compared to PEC strokes. High kappa statistics indicated substantial agreement between actual and predicted targets.

# 5.1. Baseline Discussion 

Other machine learning algorithms were trained on the data, and k-fold cross validation was performed; the results are compared to those of the BN (Tables 6 and 7). The BN produced better predictive performance than all the other algorithms, especially for NGC strokes, indicating better handling of the class imbalance. Naive Bayes and SMO were the second-best performers, while random tree had the poorest results.

Table 6. Predictive performance of target value using other machine learning algorithms as baselines, with precision, recall, and F1-scores.


Table 7. Overall model performances using other machine learning algorithms as baselines, with accuracy and kappa statistic.


### 5.2. K-Means and BN Discussion

When comparing BN models with k-means algorithms (Table 8), BN models fall within the performance range of all three k-means algorithms, particularly for identifying PEC strokes. However, k-means algorithms outperformed BN models at identifying NGC strokes. GroupGCP had the best overall performance, while BN models demonstrated substantial agreement between actual and predicted targets. K-means algorithms rely on predetermined distance thresholds and other conditions, making them easy to implement with high accuracy. BN models, however, provide an algorithm that does not rely on predetermined parameters and offers insight into data feature dependencies.

This comparison makes for a clear answer to the question of whether a Bayesian network approach is relevant for the classification of GSPs. Quite simply, the answer is 'no'. While the Bayesian network approach does not require an artificial distance threshold to be implemented-and can possibly identify other dependencies other algorithms do not

rely on-this does not yield any measurable performance increase. On top of that, it is a significantly more complex approach to implement. As such, it is recommended that the established k-means approaches continue to be used.

Table 8. Summarized results from global GSP characteristics in negative downward lightning flash research [13] using three algorithms used in the current literature combined with the results from BN models.


# 5.3. Future Work 

This analysis can be improved by using a distance threshold to determine the target value, as used in the k-means algorithms. Even though k-fold cross validation works well for imbalanced data, the problem could be alleviated by applying a SMOTE technique during the pre-processing of data to make the minor class have the same number of samples as the major class. Making use of other programming tools and libraries with Bayesian network capabilities could be an interesting investigation, particularly to compare the results with the ones obtained in this research. Another investigation that could be done in the future would be to use the obtained DAGs from the BN models to learn the parameters of other lightning data from various LLSs, such as the data used for global GSP characteristics in negative downward lightning flashes research from Brazil, Austria, France, Spain, and the United States of America [13].

## 6. Conclusions

The purpose of this research was to investigate whether Bayesian networks (BNs) offer a viable solution to ground-strike point (GSP) classification based on locations obtained by lightning locating systems (LLSs). Bayesian networks, as probabilistic directed acyclic graphs, learn the joint probability distribution of variables from a dataset, which can then be used to predict GSPs for each lightning stroke. The objectives were to obtain lightning data, select relevant features, categorize the dataset into lightning flashes according to IEC 62858, develop BN models, and analyze the models' performance. These objectives were successfully achieved using lightning data provided by the South African Weather Service. The BN models were developed through a structure-learning procedure and analyzed using confusion matrices and kappa statistics.

Five BN models were created using various combinations of variables. The first model used raw data, while subsequent models incorporated assumptions about joint probabilities. Although the first model had the lowest mean classification error during cross validation, the second model produced the best results, with an accuracy of $93.9 \%$ and a kappa index of 0.73 . Six algorithms-Naive Bayes, logistic regression, multi-layer perceptron, random tree, random forest, and sequential minimal optimization-were used as baselines. While all produced good results, BN outperformed them. Both BN and the baseline models were affected by class imbalance, with the minor class having worse prediction results.

When comparing BN models to the k-means algorithms used in global GSP characteristics research [13], k-means performed better overall. The highest accuracy of BN models was slightly lower than GroupGCP but higher than Meteorage and Matsui k-means. Despite BN's good performance, k-means remains the best method for GSP analyses due to its ease of implementation and consistent results. In summary, while Bayesian networks offer an alternative for GSP analysis, they do not surpass the performance of k-means methods. However, BN models provide valuable insights and handle class imbalances effectively, making them a viable complementary approach to existing methods.

Author Contributions: Conceptualization, H.G.P.H.; Data curation, H.G.P.H. and C.S.; Formal analysis, W.L.; Funding acquisition, H.G.P.H. and C.S.; Methodology, W.L.; Resources, H.G.P.H. and C.S.; Software, W.L.; Supervision, H.G.P.H. and R.A.; Validation, C.S.; Visualization, W.L. and C.S.; Writing—original draft, W.L.; Writing—review and editing, H.G.P.H., R.A., and C.S. All authors have read and agreed to the published version of the manuscript.

Funding: This work is based on research that is supported in part by the National Research Foundation of South Africa and their support of research through the Thuthuka Programme (unique grant No.: TTK23030380641 and CSRP23030380658) and by DEHNAFRICA and their support of the Johannesburg Lightning Research Laboratory.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Requests to access the datasets should be directed to the corresponding author.

Acknowledgments: We would like to acknowledge the South African Weather Service for providing the SALDN data used in this study: specifically, Michelle Hartslief and Morné Gijben.

Conflicts of Interest: The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.
