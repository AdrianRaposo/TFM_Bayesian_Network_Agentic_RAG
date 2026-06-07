# Article 

## Variational Bayesian Network with Information Interpretability Filtering for Air Quality Forecasting

Xue-Bo Jin ${ }^{1,2}$ (D), Zhong-Yao Wang ${ }^{1,2}$, Wen-Tao Gong ${ }^{1,2}$ (D), Jian-Lei Kong ${ }^{1,2, * *}$, Yu-Ting Bai ${ }^{1,2}$ (D), Ting-Li Su ${ }^{1,2}$, Hui-Jun Ma ${ }^{1,2}$ and Prasun Chakrabarti ${ }^{3}$

## check for updates

Citation: Jin, X.-B.; Wang, Z.-Y.; Gong, W.-T.; Kong, J.-L.; Bai, Y.-T.; Su, T.-L.; Ma, H.-J.; Chakrabarti, P. Variational Bayesian Network with Information Interpretability Filtering for Air Quality Forecasting. Mathematics 2023, 11, 837. https:// doi.org/10.3390/math11040837

Academic Editors: Ioannis E. Livieris, Panagiotis Pintelas and Stavros Stavroyiannis

Received: 2 January 2023
Revised: 31 January 2023
Accepted: 1 February 2023
Published: 7 February 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Artificial Intelligence College, Beijing Technology and Business University, Beijing 100048, China
2 China Light Industry Key Laboratory of Industrial Internet and Big Data, Beijing Technology and Business University, Beijing 100048, China
3 Department of Computer Science and Engineering, ITM SLS Baroda University, Vadodara 391510, India

* Correspondence: kongjianlei@btbu.edu.cn

Abstract: Air quality plays a vital role in people's health, and air quality forecasting can assist in decision making for government planning and sustainable development. In contrast, it is challenging to multi-step forecast accurately due to its complex and nonlinear caused by both temporal and spatial dimensions. Deep models, with their ability to model strong nonlinearities, have become the primary methods for air quality forecasting. However, because of the lack of mechanism-based analysis, uninterpretability forecasting makes decisions risky, especially when the government makes decisions. This paper proposes an interpretable variational Bayesian deep learning model with information self-screening for PM2.5 forecasting. Firstly, based on factors related to PM2.5 concentration, e.g., temperature, humidity, wind speed, spatial distribution, etc., an interpretable multivariate data screening structure for PM2.5 forecasting was established to catch as much helpful information as possible. Secondly, the self-screening layer was implanted in the deep learning network to optimize the selection of input variables. Further, following implantation of the screening layer, a variational Bayesian gated recurrent unit (GRU) network was constructed to overcome the complex distribution of PM2.5 and achieve accurate multi-step forecasting. The high accuracy of the proposed method is verified by PM2.5 data in Beijing, China, which provides an effective way, with multiple factors for PM2.5 forecasting determined using deep learning technology.

Keywords: multiple factors; time series forecasting; deep learning; interpretability; data filtering; variational Bayesian

MSC: 68 T 07

## 1. Introduction

Nowadays, people's living standards are improving with the gradual development of social and economic levels, and they are paying more and more attention to their well-being. It is well known that air quality has a significant impact on health. Therefore, time series forecasting technology for air quality has attracted wide attention. Among the many factors affecting air quality, PM2.5 is the most significant. PM2.5 is a mixture of particles with a diameter of less than or equal to 2.5 microns, including toxic and harmful substances such as elemental carbon, volatile organic compounds (VOC), sulfides, condensates, metal particles, etc. [1], with which it is easy to cause various respiratory and cardiovascular diseases and seriously affect people's health [2]. Accurately forecasting the concentration of PM2.5 can supply complete air quality forecasting information, provide a scientific and accurate theoretical basis for the prevention and control of air pollution, and make the government and the public understand air quality comprehensively.

With the development of sensing technology, historical PM2.5 concentration and other air pollutant data are convenient to obtain, which makes it possible to model the changing

pattern of PM2.5. However, the formation mechanism and change process of PM2.5 data are very complex. They are also affected by seasonal and geographical conditions, including the temporal and spatial dimensions. PM2.5 is a kind of non-stationary time-series data with complex nonlinear and distribution characteristics that increases the difficulty of forecasting PM2.5 concentration accurately. The related research has always been the hotspot in the time series forecasting field.

There have been three methods for air quality forecasting, i.e., the statistical, machine learning, and deep learning models. Simple statistical models include time series models: the autoregressive (AR) models [3,4], the moving average (MA) models and the autoregressive moving average (ARMA) models [5], the machine learning models including artificial neural networks (ANN) [6,7], and random forest (RF) [8], etc. These methods are easy to implement and interpret. However, their small parameter scales and simple structures give them a low ability for feature representation and nonlinear fitting. These methods are only suitable for application to small and stable data sets and cannot solve the large data sets with strong nonlinearity or address the high complexity of the actual PM2.5 data. However, the prediction models may use the state space models and input-output representations [9,10], and the parameters of the models can be obtained by using the parameter identification methods [11,12] such as the least squares algorithms, the Newton algorithms [13,14,15] and the gradient search algorithms [16,17] and so on.

Deep learning methods have been widely used in air quality forecasting on the basis of their powerful modeling nonlinear ability for multivariable and multi-channel massive time series. In particular, recurrent neural networks (RNN) [18], long short-term memory networks (LSTM) [19], gated recurrent units (GRU) [20], etc., have become necessary ways to perform air quality forecasting.

On the other hand, mechanism-based analysis is still an essential way of air quality forecasting. For example, air pollution sources such as PM2.5 have temporal and spatial characteristics, and the pollution in adjacent areas is relatively similar. PM2.5 will also be affected by other air quality and meteorological factors. For example, excessive humidity can easily make PM2.5 dissipate more slowly. Therefore, for PM2.5, which has many influencing factors and complex changes, it is necessary to consider the impact of elements on the concentration change of PM2.5. Researchers found that mechanical pollution factors can help air quality forecasting accuracy. While the formation of its mechanism is very complex, the forecasting accuracy cannot be guaranteed because it only uses the mechanical method in the actual air quality forecasting. Therefore, in recent years, the deep network has become the primary method of air quality forecasting.

However, when training the deep network, it is incorrect to blindly use all the obtained data because a large number of data often have redundant information, which increases the training cost of the network and does not improve or even reduce the forecasting accuracy. Therefore, it is necessary to minimize useless information to improve the network's training efficiency and forecasting accuracy. Researchers have proposed information screening methods and applied them to air quality forecasting. The standard variable screening methods include the Granger causality analysis method [21], mutual information method [22], Spearman rank correlation coefficient [23], a data screening based on single Gauss [24], etc. These methods can quantitatively analyze the relationship between the factors in the multi-dimensional time series and eliminate the variables' useless, inconsistent and conflicting factors. However, these methods can only analyze the conflict and inconsistent relationship but do not consider the redundant relationship. This is because it is known that the redundant input data will make the deep neural network overfit in the modeling process, thus reducing the forecasting performance. Therefore, reducing redundant information remains an open research direction, particularly screening the input information of the deep network effectively.

In addition, the collected air quality data often has another problem: it contains a complex noise distribution. As we know, the complex noise distribution will mask the essential characteristics of the time series data, such as periodicity, seasonality, etc., and

make it challenging to model, thus reducing its forecasting accuracy. Researchers have tended to add the denoising steps before forecasting, such as in the wavelet transform denoising method [25], empirical mode decomposition (EMD) method [26], etc. Conversely, for deep networks, wavelet transform and EMD, an adjustment in parameters is required; therefore, these methods cannot achieve an end-to-end forecasting network.

The main contributions of this paper are as follows.
(1) According to the air quality formation mechanism, this paper provides an interpretable information screening mechanism based on multivariable and multi-channel massive time series data. Compared with the existing methods [21,22,23], the interpretable information screening mechanism can mine the correlation and redundancy between multiple time series input variables that affect air quality, extract helpful information more effectively and eliminate information redundancies.
(2) The interpretable screening filter is embodied in the learning framework to build an end-to-end forecasting network. The screening filter learns the parameters from the input data through Bayesian hyperparametric optimization with multiple Gaussian peaks.
(3) The variational inference structure is introduced into the gated recurrent unit (GRU), following the interpretable information screening layer, to mine the spatial and temporal relation of PM2.5 and enhance the modeling ability of the network for nonlinearity and complex noise distribution.

This paper is organized as follows: Section 2 introduces the related research work for the air quality field, and Section 3 describes the data sets used. Section 4 introduces in detail the methods and forecasting models proposed. Section 5 establishes experiments and the analysis of the results. In Section 6, we give conclusions and suggest future related work.

# 2. Related Works 

### 2.1. PM2.5 Forecasting Method Based on Traditional Methods

Traditional PM2.5 forecasting methods are mainly statistical models and machine learning methods. Because of their relatively simple structures, the statistical methods mostly consider the formation mechanism of PM2.5. They are widely used in the field of air quality forecasting. Liu et al. [27] combined ARIMA with numerical forecasting to forecast the daily and hourly PM2.5 concentration in Hong Kong. Zeng et al. [28] studied the relationship between PM2.5 and meteorological factors in Chengdu within 24 h . They used the generalized additive model to forecast the concentration of PM2.5. Although the traditional forecasting method based on statistics has a relatively good capability in forecasting PM2.5, it has limitations because the formation of PM2.5 is very complex.

Machine learning technology in air pollution forecasting is mainly based on historical data and was modeled nonlinearly, which is more in line with the nonlinearity of actual air pollution data, thus producing higher forecasting accuracy. Wang et al. [29] used an optimal network structure, based on the BP neural network, to forecast the concentration of PM2.5. Fang et al. [8] used a machine learning method to forecast the concentration of PM2.5 in Beijing, China, based on ground LiDAR and meteorological data. Chang et al. [30] used the self-organizing mapping method to extract the temporal and spatial characteristics of PM2.5 concentration and used the back-propagation neural network to make a forecast. Shahriar et al. [31] evaluated hybrid models (ARIMA, ANN, SVM, PCR, DT, and CatBoost) to forecast environmental PM2.5 concentration in many cities in Bangladesh. Among these models, CatBoost has the best performance. Carreno et al. [32] used machine learning techniques to forecast particulate matter levels based on meteorological and climatic features in Talca, Chile.

With the development of sensors and storage technology, there are more and more data about air quality. Although the traditional forecasting methods based on machine learning techniques have a relatively good effect on forecasting PM2.5, these methods have limitations and are more suitable for small data sets. These traditional forecasting methods of simple structure can no longer meet the complex modeling capabilities re-

quired in the context of big data, and it is easy to fall into overfitting, thus reducing the forecasting accuracy.

# 2.2. PM2.5 Forecasting Method Based on Deep Learning 

A deep learning network has recently been widely used in air quality forecasting because of its robust modeling and learning ability. Sun et al. [33] proposed a PM2.5 concentration estimator based on a deep convolution neural network. Shi et al. [34] proposed using an improved integrated depth neural network method based on an attention mechanism to forecast the concentration of PM2.5. Mengfan et al. [35] proposed a new PM2.5 concentration hybrid forecasting model that combines a long short-term memory neural network (LSTM) and a specific convolutional neural network (CNN) with a $1 \times 1$ core size. Wang et al. [36] proposed a spatiotemporal convolution recursive long short-term memory (CR-LSTM) neural network model to forecast PM2.5 for long-term forecasting. Wang et al. [37] proposed a PM2.5 forecasting model that combines content and a bidirectional gated recurrent unit based on sense. These models do not consider the selection of input data for the mechanical characteristics of PM2.5 but improve the forecasting performance based on the improvement of the model. Prihatno et al. [38] proposed a single-dense layer bidirectional long short-term memory (BiLSTM) model to forecast the PM2.5 concentrations in the indoor environment by using time series data.

Although the deep learning method is widely used in the field of time series data for its strong modeling ability, there are limitations to multi-dimensional time series data. Many conflicting and inconsistent data often occur between multi-dimensional time series, such as air quality data. They will reduce the learning efficiency of deep learning and affect the understanding of the data characteristics of the model, thus reducing the accuracy of forecasting.

### 2.3. Multi-Factor PM2.5 Forecasting Method Based on Variable Screening

Given the problems in multi-dimensional air quality time series, many researchers have proposed various methods to consider the relationship between variables to reduce the dimensions of the input series. Zhu et al. [39] proposed an attention-based parallel network (Apnea) to forecast PM2.5 and used the maximum information coefficient (MIC) to conduct spatio-temporal correlation analysis, taking complete account of the linear and nonlinear relationship between the data of each monitoring station. Liu et al. [7] proposed a feature selection algorithm, based on pseudo F statistics, which obtains prime variables related to PM2.5 and then uses support vector regression to forecast PM2.5. Pak et al. [40] used mutual information (MI) to analyze the spatial-temporal correlation of air quality data, taking complete account of the whole region of China centered on the target monitoring station and historical air quality meteorological data. Cifuentes et al. [41] analyzed the impact of different forecasting variables based on the Spearman coefficient, principal component analysis (PCA), and meteorological data on air quality forecasting. Zhu et al. [42] quantified the relationship between different variables through the Pearson coefficient and considered the influence of different monitoring sites and seasons on PM2.5 forecasting.

Although the above methods consider the correlation between variables, these feature selection methods have limitations because they need to be calculated separately and then artificially screened. Moreover, these methods can only analyze the correlation between time series and cannot interpret their redundancy. Finally, the data can be input into the model for training. As such, the selection step is separated from the network and is only a data preprocessing process, which cannot realize an end-to-end forecasting network.

### 2.4. PM2.5 Forecasting Method for Noise Problems

Air quality time series often contain complex noise distribution, affecting the forecasting model's learning and modeling for the time series data [43]. Therefore, the data processing methods of noise reduction and denoising have been favored by researchers. Jin et al. [44] proposed a decomposition integration forecasting method based on wavelet

denoising for PM2.5 data. Samal et al. [45] proposed a hybrid PM2.5 forecasting framework called a time convolution denoising automatic encoder (TCDA) network, which uses the denoising self-encoder to denoise PM2.5 data. Cai et al. [46] designed a denoising selfcoding deep network based on LSTM to develop the accuracy of air pollutants forecasting models. Jin et al. [47] proposed a hybrid deep learning forecaster, using empirical mode decomposition (EMD) to decompose the data into components. They then used a deep network to forecast the PM2.5 in Beijing, China.

Almost all of the above methods are preprocessing for the deep networks, increasing the complexity of forecasting models and operation steps. Besides, these methods have some limitations, such as a lack of a strict mathematical foundation, a small scope of application, etc. Moreover, most of these methods need enough prior knowledge.

Based on the problems and advantages of the above research, this paper considers the correlation and redundancy between input data. It builds a self-learning optimization layer with an interpretable information screening mechanism to improve forecasting network interpretability and accuracy. Further, we create a Bayesian GRU network with variational inference, overcoming the problem that traditional deep learning struggles to fit the complex noise distribution and improving the model's multi-step forecasting accuracy.

# 3. Data Set and Spatial Correlation Analysis 

### 3.1. Data Set

This paper uses the hourly PM2.5 and meteorological data in Beijing from January 2019 to December 2021. Each data set contains 26,280 data points. The meteorological data include temperature, wind direction, and humidity. The sampling frequency of all data is 1 h. The data are normalized as follows:

$$
x^{\prime}=\frac{x-\mu_{x}}{\sigma_{x}}
$$

where $x$ represents the input observation data, $\mu_{x}$ represents the mean value of the observation data, and $\sigma_{x}$ represents the variance of the observation data. The role of Z-score standardization is to unify the data distribution of characteristics and reduce the impact of the characteristics of different distributions on the final results.

### 3.2. Spatial Correlation Analysis

The spatial correlation in the air quality between different areas in Beijing is shown and analyzed below.

Figure 1a shows the geographic location of four different areas in Beijing. The orange area represents "Guanyuan" in the Haidian District in Beijing. The blue areas represent the "Temple of Heaven" in the Dongcheng District in Beijing, the "South Third Ring Road" in the Fengtai District in Beijing, and the "Coloured Glaze River" in the Fangshan District in Beijing, respectively. We will analyze the spatial correlation in the air quality between the "Guanyuan" area and the other three areas.

Figure 1b shows 300 samplings from the "Guanyuan" area and "Temple of Heaven" area, and it can be seen that there is a solid spatial correlation in the air quality data between these two areas. It can also be seen from Figure 1a that those two areas are very near to each other. The high degree of coincidence proves a redundant relationship between them. It is bad practice to put this kind of data with solid redundancies into the neural network for training. For example, a large amount of data leads to an increase in training time; or, when training the neural network, it will lead to overfitting the data and poor forecasting results in practical application.

Figure 1c shows the spatial correlation in the air quality data of the "Guanyuan" area and the "South Third Ring Road" area. It can be seen that the similarity of the data curve between the "Guanyuan" area and the "South Third Ring Road" area is different from that of the "Guanyuan" area and the "Temple of Heaven" area, as shown in Figure 1b. Still, there is also a specific correlation between them. In addition, air pollutants are very vulnerable to

the weather and so the wind blows air pollutants from one area to another relatively close location. Moreover, the "Guanyuan" area and the "South Third Ring Road" are somewhat near, and the other area will affect their air quality. There is a specific correlation between the data of the two regions, but the redundancy between them has been less extensively compared than the "Guanyuan" area and the "Temple of Heaven" area.
![img-0.jpeg](img-0.jpeg)

Figure 1. Spatial Correlation between different areas in Beijing. (a) the geographic location of four different areas in Beijing. The scale is 1:1,000,000. (b) PM2.5 changes in Guanyuan, Haidian, and Temple of Heaven, Dongcheng. (c) PM2.5 changes in Guanyuan, Haidian, and South Third Ring Road, Fengtai. (d) PM2.5 changes in Beijing Guanyuan and Coloured Glaze River, Fangshan.

Figure 1d shows the spatial correlation in the air quality data of the "Guanyuan" area and the "Coloured Glaze River" area. It can be seen there is less similarity between the two regions when comparing Figure 1b,c. It can also be seen that the air pollutants in the two areas will not affect each other due to the distance between the two regions, and that the correlation is low. Therefore, when forecasting the air quality in the "Guanyuan" area, it is not necessary to send the "Coloured Glaze River" data into the neural network for training.

This paper will design a deep forecasting network based on information interpretability filtering. As the first layer of the network, the information interpretability filtering layer selects the $m$-dimensional variable with high correlation and low redundancy from the n-dimensional time series data. Then, these variables are input to train the deep forecasting model. The flow of this model is shown in Figure 2. We will detail the information interpretability filtering in Section 4 and the deep forecasting model in Section 5.

![img-1.jpeg](img-1.jpeg)

Figure 2. A deep forecasting model based on information interpretability filtering ( $\mathrm{m}<\mathrm{n}$ ). The dotted lines with different colors in the figure represent different variables.

# 4. Information Interpretable Filtering 

From a mechanism analysis, the relationship between meteorological elements and air quality contains a complex implicit nonlinear relationship [48,49,50]. For example, when the humidity is high, the water vapor content in the air is significant and tiny water particles surround the PM2.5 solid particles. Due to the increase in moisture content, the density and concentration of PM2.5 particles decrease, decreasing the PM2.5 value [51]. At the same time, rainfall has a significant impact on air quality. Rainwater will adsorb air pollutants and cause them to settle, thereby reducing the concentration of PM2.5 [52]. In addition, there will be a more significant impact between the regions. Due to the flow and diffusion of air, this method will be helpful for forecasting of air quality. However, the amount of information on these mechanisms is vast and complex, making accurate modeling difficult. Air quality forecasting modeling based on big data has recently received extensive attention.

The researchers found that redundant input data not only increase the training cost of the network but also reduce the forecasting accuracy due to overfitting. We know that the air quality data contained redundant information if the two regions were very close. Therefore, using a large amount of data cannot effectively improve forecasting performance. On the other hand, in deep learning networks, more input data will not make the network work more effectively.

The researchers began to consider the correlation between the data and used the method of data analysis to select the data. However, the lack of interpretability of classical data analysis methods makes the forecasting results lack analytical support. This paper will give an information filtering framework, with interpretability based on optimization strategies, by the following two steps:

Step 1: First, mutual information is used to calculate the relationship degree between the variables in the data set, including PM2.5 content or meteorological factor, e.g., temperature, humidity, and wind speed, in different regions.

The mutual information (MI) is calculated in formula (2):

$$
I\left(x, y^{i}\right)=p\left(x, y^{i}\right) \log \frac{p\left(x, y^{i}\right)}{p(x) p\left(y^{i}\right)}
$$

where $x$ is set as the target variable, i.e., PM2.5 content; $y^{i}$ is the variable to be selected; $p\left(x, y^{i}\right)$ is the random distribution of the two variables; $p(x)$ and $p\left(y^{i}\right)$ are marginal distributions.

When the mutual information value between $x$ and $y^{i}$ is more extensive, they have more related information. However, the data with a high correlation may also contain more redundant information, especially in air quality forecasting (as discussed in Section 3). Redundant information is unfavorable for neural network training. Therefore, we chose the most relevant variables but excluded the data with high redundancy. Consequently, we discussed the concept of "effective" mutual information.

Step 2: Adaptive information distance (AID) is proposed to select the input variables with high correlation but low redundancy for the deep network:

$$
D\left(y^{i}\right)=\sqrt{\left(y^{i}-x\right)^{T} S^{-1}\left(y^{i}-x\right)}
$$

where $y^{i}$ is the selected variable based on the mutual information (2), $S$ is the parameter that needs to be determined so that the selected variables can have high correlation and low redundancy, and $x$ is the target variable.

In the information interpretability filtering framework, the parameter $S$ of AID, which directly affects forecasting performance, is optimized to ensure the reliability and validity of variable screening via the Bayesian hyperparameter optimization method [53]. In this study, we use the root mean square error (RMSE) as the objective function for optimizing hyperparameters:

$$
\operatorname{loss}(w)=\sqrt{\frac{1}{T} \sum_{t=1}^{T}\left(x_{t}-\hat{x}_{t}\right)^{2}}
$$

where $w=[S, x]$ is the hyperparameter that needs to be optimized for AID, $T$ is the number of input samples, $x_{t}$ is the target variable, $\hat{x}_{t}$ is the forecasting, and $t$ is the time index. The set of hyperparameters $w^{*}$ can be obtained by minimizing $\operatorname{loss}(w)$ :

$$
w^{*}=\underset{w \in W}{\operatorname{argmin}} \operatorname{loss}(w)
$$

where $w^{*}$ is the optimal parameter determined by Bayesian hyperparameter optimization, $w$ is a set of input parameters, and $W$ is the parameter space of multi-dimensional parameters.

Information interpretability filtering consists of mutual information, AID, and Bayesian hyperparameter optimization. Among these, the mutual information methods selects variables with a high correlation with the target variable. AID sets variables with lower redundancy so that the variables with high correlation and low redundancy will be filtered out. Bayesian hyperparameter optimization learns the parameters required by AID according to the different input data in order to obtain correct input data, thereby improving the forecasting accuracy of the target variable. The computational flow chart of the interpretability filtering of information is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Information interpretability filtering. The dotted lines with different colors in the figure represent different variables.

# 5. Deep Forecasting Network 

Here, we use variational Bayesian gated recurrent unit (VBGRU) in this forecasting model. VBGRU selects GRU as the primary network structure and uses variational methods to train weights with distributed characteristics. The network structure of VBGRU is shown in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4. Deep forecasting network. In the lower right corner of the figure, the blue line represents the weight and bias generated by initialization, and the red line represents the new weight and bias sampled from the corresponding mean and variance through the Monte Carlo sampling module.

As shown in Figure 4, the weights and biases of VBGRU are transformed into distribution via the variational inference method. The specific process is: first, initialize the weight $W$ and bias $b$ of the VBGRU to the distribution of a specific mean and a specific variance. Then, the new weight $W_{\text {sample }}$ and bias $b_{\text {sample }}$ are sampled from the corresponding mean and variance through the Monte Carlo sampling module. The weight calculation method not only optimizes the performance indicators of the model but also learns the uncertainty of the network forecasting on a specific data point. In addition, VBGRU can obtain multiple model outputs by adding sampling points to calculate the uncertainty of the model at a specific point.

Let $W_{(n)}^{(i)}$ denote the nth sampling weight of the ith layer and $b_{(n)}^{(i)}$ denote the bias. In deep Bayesian networks, neither weight nor bias is a definite number, but results are obtained by sampling on a distribution; the distribution parameters $\rho^{(i)}$ and $v^{(i)}$ of weights and biases are obtained through training, and their relationship with weights $W_{(n)}^{(i)}$ and biases $b_{(n)}^{(i)}$ are shown in formulas (6) and (7).

$$
\begin{aligned}
W_{(n)}^{(i)} & =N(0,1) * \log \left(1+\rho^{(i)}\right)+v^{(i)} \\
b_{(n)}^{(i)} & =N(0,1) * \log \left(1+\rho^{(i)}\right)+v^{(i)}
\end{aligned}
$$

Like ordinary deep models, deep Bayesian networks need to determine the optimization goal of the network model through the loss function. Additionally, the loss function needs to be guaranteed to be differentiable so that the network model parameters can be updated using the back-propagation algorithm. The deep Bayesian network uses the variational inference method to calculate the approximate distribution of the complex distribution of model parameters. The degree of approximation between the two is measured by the Kullback-Leibler divergence (KL divergence) in order to realize the differential operation of the loss function on its related variables. However, since the forecasting task is usually performed to forecast a specific value, only using the KL divergence as the loss error between the forecasting result and the network output will mean the model can only learn the distribution characteristics of the data. Therefore, the loss function of the deep Bayesian network is composed of two parts, the differentiable mean absolute error (MAE) and the KL divergence.

Therefore, the formula of the loss function of the deep Bayesian network is as follows:

$$
\operatorname{Loss}=\operatorname{Loss}_{M A E}+\partial \cdot\left[\log \left(Q\left(\omega^{(n)} \mid \theta\right)\right)-\log \left(P\left(\omega^{(n)}\right)\right)\right]
$$

where $\partial$ represents an error weight parameter, generally set as the reciprocal of the number N of all training samples, namely $\partial=1 / N ; P(\omega)$ is a manually set low-entropy prior distribution; $Q(\omega \mid \theta)$ is the posterior distribution of a given parameter.

Through the above analysis, we replace all the weights and biases inside the GRU with different distributions, initialize it to a standard normal distribution, and update the weight parameters of the network model through the Adam optimizer to obtain the best network parameters, that is, to obtain the optimal mean and variance of the weight distribution and bias distribution. Similarly, when using the trained model, the weight and bias distribution are sampled multiple times by sampling, and various sets of forecasting results are obtained. Finally, the multi-group forecasting results are averaged, which are the forecasted values output by the network.

# 6. Experiments 

### 6.1. Experiment Setup and Evaluation Indicators

The learning and forecasting step of the network model is set to 24 , i.e., 24 h of historical data are input into the model as a sample to forecast the next 24 h . The selection of the hyperparameter of the forecasting model is based on experience and multiple attempts. The batch size is set to 40 , the number of training epochs is set to 50 , and the learning rate is set to 0.001 . The Adam optimization algorithm is used to make the model perform supervised learning.

We adopt three evaluation functions to evaluate the forecasting performance of the model, namely: root means square error (RMSE), mean square error (MSE), and mean absolute error ( $M A E$ ). They are calculated by formulas (9)-(11) [24], respectively.

$$
\begin{aligned}
R M S E & =\sqrt{\frac{1}{n} \sum_{t=1}^{n}\left(\hat{x}_{t}-x_{t}\right)^{2}} \\
M S E & =\frac{1}{n} \sum_{t=1}^{n}\left(\hat{x}_{t}-x_{t}\right)^{2} \\
M A E & =\frac{1}{n} \sum_{t=1}^{n}\left|\left(\hat{x}_{t}-x_{t}\right)^{2}\right|
\end{aligned}
$$

where $n$ represents the total number of samples in the data set, $x_{t}$ and $\bar{x}_{t}$ represent the actual value of PM2.5 and the average value of the actual value at time $t$, respectively; $\hat{x}_{t}$ and $\overline{\hat{x}}_{t}$ represent the forecasted value and average value of PM2.5 concentration obtained through experiments at time $t$, respectively. RMSE, MSE, and MAE indicate that the smaller the value is, the better the model's forecasting performance will be.

Analysis of variance is a statistical analysis method used to analyze the influence of categorical independent variables on numerically dependent variables. It can also be used to analyze the significance test of the difference between the mean values of two or more samples. We also used a one-way analysis of variance to validate the results. Variance analysis first acquires statistics on each factor in the target, divides the total change into test value and error value, and constructs statistic F. The formula is as follows:

$$
F=\frac{M S T R}{M S E}
$$

where $M S T R$ measures the variation among the $k \geq 2$ samples and $M S E$ measures the variation within the samples. When the value of $F$ is higher than the value of F-crit (the critical value of the F-test), it means that there is a significant difference in the level of

different factors or the factors have a substantial impact on the results. The opposite means that there is no significant difference in the level of different factors, or that these factors have no substantial impact on the results.

# 6.2. Numerical Experiment and Analysis of PM2.5 in Different Regions 

In this part, we analyze the correlation between PM2.5 in the Guanyuan (GY) area of Haidian District with PM2.5 in other different regions [39], including Temple of Heaven (TOH) in Dongcheng District, South Third Ring Road (STRR) in Fengtai District and Coloured Glaze River (CGR) in Fangshan District. Figure 5 shows a schematic diagram of the positions between different regions. The MI value and AID value between PM2.5 in different regions and PM2.5 in the GY region are shown in Table 1.
![img-4.jpeg](img-4.jpeg)

Figure 5. Distance between target area and other areas. The scale is 1:1,000,000.
Table 1. Comparison of MI value and AID value between PM2.5 of GY and PM2.5 of TOH, STRR, CGR.


It can be seen from Table 1 that the MI values between PM2.5 in the GY region and the other three areas are TOH (0.71), STRR (0.56), and CGR (0.43) in order. Moreover, although the TOH region has a high correlation with the GY region, its AID is 1.39, indicating that there is a high degree of redundancy between the two. Its AID value is also significant, indicating less information about the relationship between the two, while the MI and AID values of STRR are 0.56 and 1.46, respectively, indicating a good correlation and low redundancy. In contrast, the correlation between the CGR and GY regions is very low. As such, we choose PM2.5 in the STRR region as an auxiliary variable to forecast PM2.5 in the GY region.

Figure 6 shows the comparison results of the three evaluation metrics. It is clear from the graph that the RMSE, MSE, and MAE of the combined STRR have the slightest error from the actual values.

![img-5.jpeg](img-5.jpeg)

Figure 6. Two-coordinate error histogram of forecast results based on PM2.5 in different regions.
Table 2 shows that the RMSE, MSE, and MAE results of univariate forecasting using only PM2.5 in the GY region are 26.83, 720.09, and 19.44. When adding PM2.5 in different regions as auxiliary variables to forecast PM2.5 in the GY region, only the use of PM2.5 in the STRR region as an auxiliary variable improved the forecasting accuracy. The results were $26.15,684.02$, and 18.77 , which are $2.5 \%, 5.0 \%$, and $3.5 \%$, respectively, lower than PM2.5 in the GY region, and the fluctuation of the results is also lower than that for PM2.5 in the GY region. Using PM2.5 in the other two regions as an auxiliary variable for forecasting did not improve the forecasting results but increased the forecasting error and reduced the model's forecasting performance. Besides, since the forecasting model in this experiment is the same, the training time for using different regions as the input data of the network is all around 46 s . The results shown in Table 2 verify the correctness of the analysis of the developments in Table 1 and verify the correctness of the relationship between region distance and forecasting performance described in Figures 1-3 in Section 3.

Table 2. Analysis of the forecasting results based on the historical data of PM2.5 in different regions as the input data of the network.


We also used a one-way analysis of variance to validate the results. The result of the one-way analysis of variance is shown in Table 3.

Table 3. One-way analysis of variance on forecasting results based on the historical data of PM2.5 in different regions as the input data of the network. In this table, SS is the sum of squares and df is the degrees of freedom. The MS (mean squares) is the estimate of variance given by SS/df.


Table 3 shows that the value of $F(10.42)$ is higher than the $F$-crit (2.61) value, which indicates that using different regions as the network's input data significantly impacts the forecasting results.

# 6.3. Numerical Experiment and Analysis of Meteorological Factors 

In this part, we analyze the correlation between the other three meteorological factors and PM2.5 in the adjacent area of the Haidian District, including temperature, wind direction, and humidity. The MI value and AID value between PM2.5 in the GY area and meteorological factors in Haidian District are shown in Table 4.

Table 4. Comparison of MI value and AID value between PM2.5 in the GY area and temperature, wind direction, and humidity in the Haidian District.


It can be seen from Table 4 that the MI values between PM2.5 of GY area and meteorological factors in Haidian District are temperature (0.34), wind direction (0.26), and humidity ( 0.22 ), indicating that humidity has the highest correlation with PM2.5 in the GY area. Moreover, the AID of temperature is the highest, the AID of humidity is slightly lower than that of temperature, and the AID of wind direction is the lowest, indicating that both temperature and humidity have low redundancy with GY PM2.5. Therefore, we believe that using humidity as an auxiliary variable to forecast PM2.5 of GY will improve forecasting accuracy.

To verify our conclusion, the optimal results obtained in Table 4 are combined with each meteorological factor to forecast the future of PM2.5. The forecasting results are shown in Figure 7 and Table 4. Figure 7 shows the comparison results of the three evaluation indicators of (GY \& STRR) PM2.5, combined with meteorological factors in different regions. It is clear from the figure that the RMSE, MSE, and MAE of the combined humidity have the slightest error from the actual values. From the results listed in Table 5, it can be seen that the forecasting errors obtained by adding two factors, temperature and wind direction, as auxiliary variables have improved to varying degrees; only the forecasting error of adding the humidity factor as an auxiliary variable has a significant decrease, and the RMSE has decreased from 26.15 to 25.44 , a reduction of $2.7 \%$; MSE decreased from 684.02 to 647.17 , a decrease of $5.4 \%$; MAE decreased from 18.77 to 17.95 , a decrease of $4.4 \%$. Besides, since the forecasting model in this experiment is the same, the training time using different regions as the input data of the network is all around 46 s , and there is no significant difference in the fluctuation of results.

Therefore, we used both PM2.5 and humidity in the STRR region as auxiliary variables to forecast PM2.5 concentrations in GY. At the same time, we also verified the validity of the method proposed in this study and proved that other air qualities and meteorological factors are closely related to the changes in PM2.5 concentration.

![img-6.jpeg](img-6.jpeg)

Figure 7. Two-coordinate error histogram of forecasting results based on different meteorological factors.



We also used a one-way analysis of variance to validate the results. The result of the one-way analysis of variance is shown in Table 6.

Table 6. One-way analysis of variance on forecasting results based on the historical data of PM2.5 in space (GY \& STRR), combined with historical data of meteorological factors in different regions as input data of the network. In this table, SS is the sum of squares and df is the degrees of freedom. The MS (mean squares) is the estimate of variance given by SS/df.


Table 6 shows that the value of F (5.75) is higher than the F-crit (2.61), which indicates that using different meteorological factors in different regions as the network's input data significantly impacts the forecasting results.

# 6.4. Interpretability Analysis 

With the advent of big data, deep learning methods have successfully proven their superiority in processing big data. Still, for deep learning methods, it is not that the more data the model trained, the better the results obtained were. A large amount of data often has a lot of redundant information, which will not only increase the computational cost and reduce the convergence speed of the network but also affect the forecasting performance of the network.

This paper introduces AID based on MI to perform a nonlinear transformation on information and then change the metric value of MI. We aim to eliminate data with high redundancy while selecting highly correlated variables. Whether a different regional factor variable or a meteorological factor variable, this paper calculates the AID between each variable and PM2.5. On this basis, the information filtering method proposed in this paper not only improves the forecasting performance of the network but also has sufficient interpretability.

When analyzing the factors of different regions, we take the TOH region as an example. It can be seen from Table 1 that the MI values between PM2.5 in the TOH region and PM2.5 in the GY region are the highest at 0.71 compared with other regions. This shows that the PM2.5 in the TOH area has the highest correlation with the PM2.5 in the GY area. This is because this phenomenon occurs because the distance between the TOH and GY areas is the closest compared to other areas. Moreover, the AID values between PM2.5 in the TOH region and PM2.5 in the GY region are the lowest at 1.39 compared with other regions, indicating that there is significant redundancy between PM2.5 in the two regions. This is because PM2.5 particles in adjacent areas will undergo a process of dissipating with climatic conditions within a short time. Although there is a substantial time correlation between PM2.5 in adjacent areas, it also leads to a redundant relationship between PM2.5 in adjacent areas. When analyzing meteorological factors, we take humidity as an example. As shown in Table 3, the MI values between humidity and PM2.5 are the highest at 0.34 compared with other meteorological factors, indicating that humidity has the highest correlation with PM2.5. This is because when the humidity rises, the PM2.5 particles will absorb the water vapor in the air and settle after absorbing a certain amount of water vapor, thereby reducing the concentration of PM2.5. It can be seen that humidity will significantly impact the concentration of PM2.5. Besides, because PM2.5 has no inclusion relationship with humidity, there is no redundant information between the data. Therefore, it can also be seen from Table 3 that the AID values between humidity and PM2.5 are the second highest relative to other meteorological factors at 1.69 .

This paper also used each variable as an auxiliary variable to forecast the future PM2.5, as shown in Tables 2 and 4. The results show that the variables selected by the information filtering module are critical for forecasting results. These key variables have a significant correlation and low redundancy with PM2.5. Their addition will significantly improve the forecasting performance of the network. It also shows that these variables play a vital role in promoting the network's ability to learn the changing pattern of PM2.5 better.

## 7. Conclusions and Future Work

In view of the problem that changes in weather data are affected by both temporal and spatial dimensions, as well as the challenge of redundant and conflicting information existing between multi-dimensional air quality data, it is difficult to forecast them accurately. In this paper, an interpretable variational Bayesian deep learning model with an information self-screening function is proposed to forecast the future PM2.5 concentration. The data self-screening layer's ability to screen variables with high correlation and low redundancy, and the anti-noise interference ability of the variational Bayesian gated cyclic unit, are fully utilized in this paper to improve the forecasting accuracy and robustness of future air quality. The validity of the method proposed is shown by the verification experiments of Beijing air quality data and meteorological data and by the careful consideration of RMSE, MSE, MAE, and other indicators.

In future research, we will try to use the method proposed in this paper on more air pollution data sets to test the applicability of this method. Additionally, we will continue to improve our network structure further to improve the overall performance of the forecasting method by means of some identification modeling methods [54-56], such as the multi-innovation theory [57,58] and the hierarchical principle [59-61].

Author Contributions: Conceptualization, X.-B.J.; methodology, Z.-Y.W.; software, Z.-Y.W.; validation, Z.-Y.W.; formal analysis, J.-L.K.; investigation, Y.-T.B.; resources, J.-L.K.; data curation, T.-L.S.; writing—original draft preparation, Z.-Y.W. and W.-T.G.; writing-review and editing, Z.-Y.W.; visualization, W.-T.G.; supervision, T.-L.S.; project administration, X.-B.J.; funding acquisition, H.-J.M. and P.C. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported in part by the National Natural Science Foundation of China, No. 62173007, 62006008, 61903009.

Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
