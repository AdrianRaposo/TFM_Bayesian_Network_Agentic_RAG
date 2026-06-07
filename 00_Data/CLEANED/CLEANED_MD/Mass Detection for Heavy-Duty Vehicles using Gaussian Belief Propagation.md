# Mass Detection for Heavy-Duty Vehicles using Gaussian Belief Propagation 

Matthew Eagon<br>Mechanical Engineering<br>University of Minnesota<br>Minneapolis, MN 55455<br>eagon012@umn.edu

Setayesh Fakhimi
Robotics Institute
University of Minnesota
Minneapolis, MN 55455
fakhi003@umn.edu

Adam Pernsteiner
Mechanical Engineering
University of Minnesota
Minneapolis, MN 55455
perns015@umn.edu

William F. Northrop
Mechanical Engineering
University of Minnesota
Minneapolis, MN 55455
wnorthro@umn.edu


#### Abstract

Predicting vehicle mass is critical to accurately estimate energy use and emissions of commercial trucks. However, data from vehicle telematics is often not at sufficient temporal resolution or accuracy for use in model-based detection methods. In this work, a new statistical mass prediction technique is described for heavy-duty vehicles that incorporates the use Gaussian Belief Propagation (GBP) for probabilistic inference. Similar to Bayesian inference models, the GBP model typically requires less labeled training data than other contemporary machine learning techniques. First, a factor graph is constructed, and a set of Gaussian belief nodes with associated means and variances are fitted to the training data. To better handle noisy input data, the GBP mass prediction model utilizes a k-nearest factors (kNF) algorithm for probabilistic inference on unseen testing data. The proposed method is compared with a classical weighted k-nearest neighbors ( kNN ) regressor. This statistical kNF-GBP model works even with low-quantity, low-quality initial training data, while being capable of realtime mass estimation. Unlike the kNN regressor, the GBP model produces a measure of uncertainty with its predictions. The proposed method is validated using curve-sampled driving data collected from multiple cloud-connected Class 8 regional haul diesel trucks. Both the kNN regressor and the kNF-GBP mass prediction model were able to predict payload mass with coefficients of determination above 0.97 with minimal data preprocessing.


Index Terms-Mass prediction, Bayesian network, machine learning, AI.

## I. Introduction

Mass is an important parameter for accurately predicting vehicle energy use and emissions, especially for commercial vehicles. Heavy-duty vehicles used in regional delivery operations encounter extensive mass fluctuations over the course of normal operations leading to correspondingly large changes in energy use. Traditionally, vehicles are weighed on scales at the origin of their trip, or using motion scales embedded in highways. However, direct measurement cannot be performed frequently enough for delivery vehicles that will have varying loads throughout their trips. Several methods are in development that hope to provide on-board scale measurements to determine payload mass, although their implementation remains limited due to high cost and the need to retrofit existing vehicles.

For electric vehicles, accurate energy usage estimations are necessary to determine the remaining range of the vehicle, decrease driver anxiety, and provide a pathway for further
technological advances. Furthermore, predicting the energy usage of a predetermined route assists in definite locations for recharging and developing accurate electric vehicle models. To accurately estimate the energy usage of a vehicle, it is crucial to determine the payload mass of the vehicle throughout its travel. Many approaches have been developed to estimate mass including control systems, model-based methods (i.e. sensor fusion), and machine learning techniques.

Mass detection can be accomplished by using data available through vehicle telematics systems. However, data is not often sampled frequently enough for use in model-based models or empirical correlations. In addition, lack of ground truth mass measurements from stationary scales prohibits the use of machine learning models that require extensive training. This paper presents a method that overcomes these challenges by developing a vehicle mass prediction method using a Gaussian Belief Propagation (GBP) framework with k-nearest neighbors ( kNN ), which can accurately detect vehicle mass using sparsely collected vehicle telematics data and a small training data set.

First, GBP is used to fit a factor graph model to available training data. The factor graph has three primary types of nodes: (i) data factors (referred to simply as factors), (ii) smoothing factors, and (iii) belief nodes. Factors represent training datapoints, while the belief nodes are updated as probabilistic (Gaussian) models representing the belief at a point, which is informed by neighboring factors and smoothing factors (which mediate between belief nodes). On its own, GBP is capable of probabilistic inference by returning the nearest belief node to any given datapoint. However, performance is hindered by noisy data, especially with limited data availability. Using k-nearest factors ( kNF ) and combining their adjacent beliefs, the proposed kNF-GBP mass prediction model provides better robustness to noise while still providing probabilistic outputs that give a measure of uncertainty (i.e. variance) along with the mean prediction. Like a normal inverse-distance weight kNN regressor, the kNF-GBP model can update over time as more training data becomes available, though a retraining step is required. On the data used in this study, the performance of kNF-GBP model is similar to that of a normal kNN regressor when comparing the kNF-GBP mean estimate, though the variance

![img-0.jpeg](img-0.jpeg)

Figure 1: Proposed framework for inference-based mass estimation.

associated with each kNF-GBP estimate provides a useful measure of uncertainty in practice, especially for out-of-sample inputs.

## II. Literature Review

Techniques for mass estimation have been intensively studied using several different approaches. Contemporary mass estimation methods from the field of control systems often utilize either Kalman filtering or recursive least squares (RLS). In Lingman and Schmidtbauer's work, the mass of a heavy-duty vehicle and the slope of the road were estimated using an extended Kalman Filter with speed as a measurement. The addition of an accelerometer to measure the specific force on the vehicle allowed for the use of two simplified filters to estimate both parameters simultaneously [1]. Boada et al. used a dual Kalman filter to estimate vehicle mass and road irregularities via suspension deflection sensors and a vertical accelerometer, which allowed for the mass to be estimated even while the vehicle was stationary. This method was tested on automobiles and light commercial vehicles, obtaining errors of <5% and <6% respectively [2]. Vahidi et al. used RLS with both single and multiple forgetting factors on CAN bus data from heavy vehicles to estimate both mass and road grade [3]; Raffone later used a similar method to estimate mass [4]. Fathy et al. used a supervisor algorithm that checked the vehicle yaw, acceleration, velocity, wheel slip ratios, and net longitudinal force to use an RLS algorithm only when the vehicle is sufficiently perturbed [5]. McIntrye's et al. developed a two-stage estimation strategy, using an adaptive least-squares estimator to detect mass and a nonlinear estimator for a refined determination of the road grade [6].

Model-based or sensor-based mass detection methods typically use standard signals from properly instrumented vehicles. Two very recent works from Skugor et al. and Jensen et al., respectively, use a model of the longitudinal vehicle dynamics with specific vehicle parameters to estimate mass [7], [8]. Other works use sensor fusion from several sensors relevant to vehicle mass to determine if a truck is loaded, estimating the payload mass once the loading pattern is found [9]–[11]. Similarly, in a previous work by Zhang et al., GPS, INS, and wheel-speed sensors were integrated to determine vehicle mass and road grade [12]. Fechtner et al. and Spaeth et al. separately proposed methods to detect payload mass by measuring the tire pressure with highly sensitive pressure sensors to optimize range prediction and assist energy-efficient driving strategies [13], [14]. In contrast, a method proposed by Wilhelm et al. required no additional sensors, but presented an eight step technique (such as calculating power, acceleration, etc.) to provide real-time mass estimation during wide-open-throttle acceleration events [15].

Many recent works utilize neural networks for prediction or classification of various vehicle parameters [16]–[19]. Torabi et al. introduce a feedforward neural network (FNN) approach to estimate the road grade and vehicle mass for heavy-duty vehicles on highways using the vehicle velocity, acceleration, engine torque, and time as inputs [17]. The road grade and heavy duty mass estimation had an average root-mean-square (RMS) error of 0.10-0.14 degrees and 1%, respectively; although this method has shown to be inaccurate when the magnitude of the road grade is large, or when the vehicle acceleration or torque vary especially quickly [17]. Korayem et al. paper explored both a dynamic system model-based and a machine learning approach to estimate trailer mass, with the machine learning (i.e. neural network) approach demonstrating a greater ability to accurately estimate mass during the braking phases of driving, which may be difficult for model-based approaches to achieve [18]. Ziaukas et al. proposed using a Residual Neural Network to classify tire pressure for one tire on a commercial semitrailer. The classes for the tire pressure were as follows: 8.5 bar (nominal pressure), 7.0 bar, and 5.5 bar. The network was able to classify the tire pressure with an accuracy of above 90% [19].

Unlike control and model based methods, the proposed kNF-GBP model does not require additional sensors to be added to the vehicle. This reduces cost and allows the method to be used on already existing vehicles. Similar to ma-

chine learning based methods, the kNF-GBP model requires training data before it can be used to make estimations. However, the kNF-GBP model requires less extensive data than a typical machine learning model, allowing the kNF-GBP model to work with vehicles that collect data with lower frequency. Additionally, the kNF-GBP provides a statistical model as an output rather than a single value, where the mean may be taken as an estimate and the variance may be used as a measure of the confidence in that estimate.

## III. Problem Description

The mass detection problem involves estimating vehicle mass over the course of a trip using available sensor data, and is most relevant for vehicles that encounter large fluctuations in mass due to changing payloads. In addition to driving data from an instrumented vehicle, any mass detection method requires ground-truth mass measurements to evaluate model accuracy. Heavy vehicles are typically weighed using scales at the origin of their trip or at weigh stations along highways, though it is currently challenging to gather and combine disparate datasets from weigh stations with available driving data from vehicle telematics devices or on-board loggers. In this work, payload mass measurements were periodically documented over roughly 2 years for 10 Class 8 Volvo VN Series diesel trucks as part of the Zero- and Near Zero-Emission Freight Facilities (ZANZEFF) project. The same trucks were instrumented with Geotab loggers collecting telematics data, which was then aligned with known payload mass measurements to create an initial dataset as input to the proposed mass estimation method.

Geotab specializes in telematics on large scale vehicle data collection, which is required for fleets since they track location and ensure vehicles are properly maintained accordingly. Geotab patented and utilizes a curve logic algorithm to send data to the data server [20], [21]. The curve logic algorithm checks points of maximum error by determining if the difference between the predicted and actual position is small or large. If the difference is small, the points are not used and logged into the server. This algorithm is applied to every measurable parameter in the system, resulting in a non-uniformly sampled dataset with many missing or incomplete datapoints, offering an additional challenge to any datadriven mass estimation method. Before being used as input to themodel, the initial driving data was linearly interpolated and filtered, upsampling to a regular 1 Hz frequency and eliminating or replacing any missing data.

Each input datapoint contained the following measurements: reference torque, engine load, engine speed, velocity, acceleration, change in fuel, GPS coordinates, and time of day. These measurements all have potential correlations, direct or indirect, to the vehicle mass. In the developed mass detection method, each prediction was represented as a Gaussian distribution. Gaussian distributions are convenient for the following reasons: they have a simple analytic form, complex operations can be expressed with simple formulae, and they can often adequately represent real-world events [22]. The proposed framework, shown in Fig. 1, consists

![img-1.jpeg](img-1.jpeg)

Figure 2: Factor graph structure (constructed with a 1:2 ratio of belief nodes to factors).

of a black-box statistical inference model using GBP (no vehicle model necessary) to determine payload mass, with preprocessed input data used to train the model.

## IV. Methodology

The approach to determine payload mass heavily relies on the following architecture: the GBP algorithm with an established factor graph and K-Nearest Neighbors for multidimensional line fitting. From this, a relationship is developed between curve-sampled data and the unknown mass.

### A. Gaussian Belief Propagation

GBP is a probabilistic inference algorithm where messages are passed synchronously through interconnected variable nodes formed by a factor graph. Probabilistic inference is employed to describe the relationships between data and variables to form a posterior probability distribution through Bayes' Rule to assist in decision making.

A factor graph is constructed to connect the variable nodes to factors which represent the various associations. Within the factor graph, edges connect factors to variable nodes, respectively, and utilize the Hammersley-Clifford theorem Eq.(1) by representing probability distributions as events in a Markov network, where the given values are dependent on the values of their close neighbors.

$$p(X) = \prod_{i} f_i V_i \tag{1}$$

where $f_i$ represents the factors, $V_i$ is the subset of variables, and $p(X)$ is the product of all given factors [22].

Factors emphasize the conditional independence between variable nodes, which determines the joint posterior of each variable node. Each variable node is represented as a Gaussian distribution, where the posterior updates by sending and receiving messages from neighboring nodes via factors. The following phases represent a single iteration within the message passing architecture: variable-to-factor, factor-to-variable, and belief update. The variable-to-factor message

![img-2.jpeg](img-2.jpeg)

Figure 3: kNN regression for a new unlabeled datapoint.
allows the factor to recognize what the belief of the variable would be if the receiving factor node did not exist. Factor-tovariable refers to a message sent to an adjacent variable node. Following this, the factor aggregates messages from all the other adjacent variable nodes and marginals accordingly from the receiving node's variables to express the factor's belief. These 3 operations within the message passing algorithm allow convergence to the exact marginals. The mathematical representations are further explained in a recent paper by Joseph Ortiz et al. [22].

In Fig. 2, GBP is applied to a simple line-fitting case. The variable nodes (also known as belief nodes if referring to the variable nodes' marginal distribution), move accordingly to their neighboring factors, which dictates their marginal distributions. For instance, if a factor (a new data point) is added between $n$ variable nodes, the marginal distributions (updated by message-passing) for the corresponding nodes are shifted with a height measurement function within the model to change the relative axial positioning.

To further generalize the model, a variable node is added to the factor graph and a new factor (measurement/features) is placed between n-adjacent factors and variable nodes. Once placed, the message update process determines the correct placement of the new or existing variable nodes based on the height measurement function and Gaussian inference. During each synchronous iteration, all variable nodes and factors send/receive messages in parallel, respectively. This process repeats until convergence is reached (reduce error via Huber Loss) for new variable nodes or factors. Once the model has converged, the new variable node's location (y-label value) is calculated with the maximum posteriori (MAP).

## B. K-Nearest Neighbors

To predict the mass of new data points, the proposed method uses the kNN algorithm for regression. As the driving data includes attributes with vastly different scales, the data is normalized to improve the performance of the kNN algorithm. An $L_{2}$ norm is used as a distance metric to determine the closest training points. The output for each new data point is the predicted mass, which is simply the weighted average mass of the $k$ closest labeled training points as described by Eq.(2).

$$
Y(\boldsymbol{X})=\frac{\sum_{i=1}^{k} w_{i} Y_{i}}{\sum_{i=1}^{k} w_{i}}=\sum_{i=1}^{k} w_{i} Y_{i}
$$

where $Y$ is the predicted output for the input vector $\boldsymbol{X}$ of some new unlabeled datapoint, $w_{i}$ and $Y_{i}$ are the weight and labeled output for each of the $k$ nearest neighbors. The weights are inversely proportional to the distance measure for each point, and are scaled such that they sum to 1 , as shown in Eq.(3).

$$
w_{i}=\frac{1 / d_{i}}{\sum_{i=1}^{k} 1 / d_{i}}
$$

where $d_{i}=\left\|\boldsymbol{X}-\boldsymbol{X}_{i}\right\|_{2}$ is the Euclidean distance between the input vectors for the point of interest $\boldsymbol{X}$ and one of its neighbors $\boldsymbol{X}_{i}$.

In the chosen implementation, a K-Dimensional Tree (KDTree) is used as it speeds up the nearest-neighbors search, with $O(k \log (n))$ average time complexity [23], [24].

## C. GBP with K-Nearest Factors

Combining the concepts of GBP and kNN, it is possible to maintain some statistical information from GBP-based probabilistic inference while making predictions more robust to noise and outliers. In k-nearest factors ( kNF ) GBP, the nearest $k$ training points are identified as in kNN. The factors associated with these training points are then located within the factor graph, from which the adjacent belief nodes are found. In this work, the GBP factor graph is constructed such that there is a $1: 1$ ratio of belief nodes to factors. Training points were ordered by their labeled output and a belief node was placed between each pair of points. Thus, the GBP model fits with a very high coefficient of determination, almost as if the belief nodes were linearly interpolated between datapoints. A similar structuring of the factor graph could be done with an arbitrary $1: n$ ratio of belief nodes to factors, where $n \geq 1, n \in \mathbb{R}$. In any case, each factor will be placed between two belief nodes, so kNF results in $2 k$-nearest belief nodes. These means and beliefs can be combined as described in Eq.(4) and Eq.(5), respectively.

$$
\begin{aligned}
& \mu_{\boldsymbol{X}}=\frac{\sum_{i=1}^{2 k} w_{i} \mu_{i}}{2 k} \\
& \sigma_{\boldsymbol{X}}^{2}=\frac{\sum_{i=1}^{2 k} w_{i}\left(\sigma_{i}^{2}+2 \sum_{i} \sum_{j<i} \operatorname{cov}\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{j}\right)\right)}{4 k^{2}}
\end{aligned}
$$

where $\mu_{\boldsymbol{X}}$ is the predicted mean, $\sigma_{\boldsymbol{X}}^{2}$ is the predicted variance for given datapoint $\boldsymbol{X}, k$ is the number of nearest factors to consider, and $\operatorname{cov}\left(\boldsymbol{X}_{i}, \boldsymbol{X}_{j}\right)$ is the covariance between vectors $\boldsymbol{X}_{i}$ and $\boldsymbol{X}_{j}$ which are nearest factors to $\boldsymbol{X}$. The weights $w_{i}$ for each point are determined as in the inverse-distance weighted kNN model, described by Eq.(3), except that each distance is represented twice to account for the two belief nodes attached to each factor.

## D. Data Preprocessing

As previously mentioned in Section III, the driving data used to generate these results were collected from a set of 10 heavy-duty Class 8 Volvo VN Series diesel trucks using Geotab loggers, which use a non-uniform curve sampling algorithm to collect data that is then stored on a virtual

![img-3.jpeg](img-3.jpeg)

Figure 4: Available mass data from trips taken by trucks immediately after the reported mass measurement.

cloud server [21]. The mass data was recorded based on average weights and quantities of known payload items, and mass measurements were only considered valid from the start of a trip until the first stop lasting longer than 20 minutes. However, some reported times for the mass measurements did not match to a recorded trip, and were ignored. Fig.4 shows the number of training points with valid mass measurements for 2000 lb ranges of mass values. Most trips, and most of the long trips (greater than 10000 seconds), had payload weights between 6000 and 20000 lbs, while relatively few trips had mass values above 35000 lbs, but all valid trips were considered when generating the results.

After filtering out datapoints with missing values and linearly interpolating between sampled points, the input data was further preprocessed. The dimensionality of the original driving data was reduced by only selecting relevant attributes, and all attributes (inputs and output) were scaled using min-max normalization. Finally, the training data was ordered by the output label before constructing the GBP factor graph with a 1:1 ratio of belief nodes to training points. Principal component analysis (PCA) was explored as an option for further dimensionality reduction, but was found to have little value for the given training data.

## V. Results & Discussion

To evaluate the inverse-distance weighted kNN regressor and the kNF-GBP methods, various models were trained and tested to assess the impacts of reducing the available training data and making more general multi-truck models. Labeled data was sampled randomly without replacement to evaluate each model. For the single-truck model, the full set of 862003 available labeled datapoints was split into training, test, and validation sets containing 60%, 20%, and 20% of the data, respectively. For the 10-truck model, the full set of 8997617 datapoints was split into training, test, and validation sets containing 20%, 60%, and 20% of the data, respectively, reducing the proportion of training data in order to speed up execution and limit memory requirements. Data for the multi-truck models was preprocessed together as though it originated from a single truck.

![img-4.jpeg](img-4.jpeg)

Figure 5: GBP model after fitting to training data.

After testing a range of values from 1 to 100, the optimal value of *k* for both kNN and kNF-GBP was found to be 2. Even with *k* = 100, the worst-performing *k* value, the coefficient of determination was greater than 0.93 for both the 10-truck and single-truck models. Fig.5 shows the results of GBP line fitting for the 10-truck model after just 8 update iterations (beliefs were initialized to zero prior to training), with a coefficient of determination above 0.999. Performance metrics for key models with *k* = 2 are summarized in Tab.1, with the corresponding results visualized in Fig.6. The kNN regressor models do not require any training step, and were therefore used to test the effect of increasing the proportion of training data on the 10-truck model performance. As shown in Fig.6, the performance of the kNF-GBP model approaches that of the kNN models, and the performance of these models improves with increased training data.

Both models showed highly similar performance on the test and validation datasets, with the kNN regressor very slightly outperforming the kNF-GBP model. In addition, the

Table 1: Performance metrics for mass prediction models (train/test/split)


![img-5.jpeg](img-5.jpeg)

Figure 6: Performance of multiple trained predictors (k=2). Payload mass measurements are left min-max normalized. The numbers in parentheses below each plot denote the train/test/validation split (in % of available data) used for model evaluation.

Mass training data was held constant over the course of a trip (because the reported measurements were completely trusted until the vehicle stopped) making this training set different than most reported in the literature. Typically, a mass estimate from the on-board diagnostics (OBD) might be used as the ground truth mass as it is sometimes reported along with the other OBD driving data. In particular, when these mass estimates are model-based, the mass estimate will fluctuate over the course of the trip in a way that correlates highly with the certain related attributes coming from the OBD. In this case, the labeled mass output was held constant over time even as the attributes in the input vector – reference torque, engine load, engine speed, velocity, acceleration, change in fuel, GPS coordinates, and time of day – fluctuated greatly. The kNN and kNF-GBP models function relatively well with such data, especially for low values of *k*, because labeled outputs are well represented and somewhat clustered.

With both the kNN and kNF-GBP models, overfitting is a significant concern. However, unlike the kNN model, the proposed kNF-GBP model can be made more robust to noisy data by reducing the ratio of belief nodes to training points and accounting for the variance of each prediction. Nonetheless, both models show impressive performance on the analyzed test and validation sets even after training on very little data, and even when utilizing data from 10 separate trucks at once. With just 10% of data reserved for training, the 10-truck models still showed coefficients of determination above 0.97 for the test and validation sets. A significant drop in performance does eventually occur when the test set is drastically reduced. With just 1% of the overall dataset used in training, the coefficients of determination on the test and validation sets were found to be just above 0.83 for the 10-truck models.

## VI. Conclusion & Future Work

Mass is a key parameter for making vehicle energy usage estimates, emissions estimates, and for analyzing logistics, especially for companies operating commercial vehicles. It is particularly challenging to estimate the mass of heavy-duty vehicles because of their different configurations (e.g., driving with or without a trailer), and objects may shift during transport or be loaded into trailers such that there is an uneven weight distribution. Telematics data presents an opportunity to save costs on dedicated sensors (e.g., tire pressure sensors) if acceptable mass estimates are obtainable from (labeled) OBD driving data alone. In this work, we proposed a new method for estimating the mass of road vehicles by borrowing concepts from kNN to improve the robustness of GBP-based probabilistic inference.

The potential of the proposed method was demonstrated using historical driving data from a set of 10 heavy-duty Class-8 diesel trucks, joined with trusted payload mass

measurements whenever a matching trip was found. Despite the initial set of labeled data being non-uniformly sampled, and containing some missing and noisy values, a simple sequence of preprocessing steps greatly improved the data quality to support model performance. With a $k$-value of 2, both a inverse-distance weighted kNN regressor and a similarly designed kNF-GBP model provided mass estimates with coefficients of determination above 0.97 on the test and validation sets for both single-truck and generalized multitruck models, even when using as little as $10 \%$ of available labeled data for training.

Future work will focus primarily on refining the proposed approach and directly comparing it against other mass estimation methods. At least two competing mass estimation methods, one neural network-based and one model-based, will be compared against the proposed kNF-GBP mass estimation model on at least two different datasets containing historical driving data from at least two different types of vehicles. A set of suitable neural network-based models and model-based mass estimation methods - primarily those recursively comparing the actual and expected energy usage, and updating the mass accordingly - are under development.

## Acknowledgment

This material is based upon work supported by the U.S. Department of Energy's Office of Energy Efficiency and Renewable Energy (EERE) under the Vehicle Technologies Office Award Number DE-EE0009233.

## Disclaimer

The views expressed herein do not necessarily represent the views of the U.S. Department of Energy or the United States Government.
