# Temporal-spatial Correlation Attention Network for Clinical Data Analysis in Intensive Care Unit 

Weizhi Nie, Yuhe Yu, Chen Zhang, Dan Song*, Lina Zhao, Bai Yunpeng


#### Abstract

In recent years, medical information technology has made it possible for electronic health record (EHR) to store fairly complete clinical data. This has brought health care into the era of "big data". However, medical data are often sparse and strongly correlated, which means that medical problems cannot be solved effectively. With the rapid development of deep learning in recent years, it has provided opportunities for the use of big data in healthcare. In this paper, we propose a temporal-saptial correlation attention network (TSCAN) to handle some clinical characteristic prediction problems, such as predicting death, predicting length of stay, detecting physiologic decline, and classifying phenotypes. Based on the design of the attention mechanism model, our approach can effectively remove irrelevant items in clinical data and irrelevant nodes in time according to different tasks, so as to obtain more accurate prediction results. Our method can also find key clinical indicators of important outcomes that can be used to improve treatment options. Our experiments use information from the Medical Information Mart for Intensive Care (MIMIC-IV) database, which is open to the public. Finally, we have achieved significant performance benefits of $\mathbf{2 . 0 \%}$ (metric) compared to other SOTA prediction methods. We achieved a staggering $90.7 \%$ on mortality rate, $45.1 \%$ on length of stay. The source code can be find: https:// github.com/yuyuheintju/TSCAN.


Index Terms-Deep Learning, Medical Time Series, MIMIC-IV, Clinical Data Analysis.

## I. INTRODUCTION

THE explosive growth of electronic healthcare data and the rapid development of artificial intelligence technology have facilitated the deep application of healthcare data in multiple scenarios [1]. On the one hand, the rapid development of the Internet of Things (loT) and big data technologies provides technical support for the large-scale acquisition, safe storage, and rapid analysis of medical health data. The health care sector has now entered the era of big data. On the other hand, artificial intelligence has reached a new stage, with both theory and technology making big steps forward. Machine

Manuscript received April 19, 2005; revised August 26, 2015. This work was supported in part by the National Natural Science Foundation of China (62372337) and the Natural Science Foundation of Tianjin (16JCZDJC31100, 16JCZDJC31100).

Weizhi Nie, Yuhe Yu, Chen Zhang, Dan Song are with the school of electrical and information engineering, Tianjin University (e-mail: weizhinie@tju.edu.cn; yuyuhe@tju.edu.cn; zhangchen001@tju.edu.cn; dan.song@tju.edu.cn).

Lina Zhao, is with Department of Anesthesiology, Tianjin Medical University General Hospital.

Bai Yunpeng, MD Postdoctor, is with Department of Cardiac surgery, Tianjin University Chest Hospital (e-mail: oliverwhite@126.com).
learning, especially deep learning, provides technical support for intelligent medical applications.

Electronic Health Record (EHR) contains a variety of medical time-series data organized in different forms, such as records of patients' admission times, medications taken and procedures scheduled, observations of laboratory results, etc. The health status of patients in Intensive Care Unit (ICU) needs to be monitored in real time to ensure that the health care staff can provide timely and effective care and that the treatment plan can be adjusted according to the development of the patients' condition. Therefore, indicators of a patient's physical health that are regularly monitored, such as respiratory rate, heart rate, and blood pressure, often contain a wealth of information that can be used to formulate a patient's treatment strategy.

Quantifying patient health and predicting future outcomes is an important area of critical care research [2]. One of the most immediately relevant outcomes for the ICU is in-hospital mortality, leading many studies toward the development of mortality prediction models. The accuracy of early mortality prediction can benefit the formulation of patients' care strategies. Traditionally, discharge date estimation is done manually by clinicians, which is time-delayed and unreliable [3]. Deep learning models based on EHR can improve the accuracy of length of stay prediction, which can reduce the burden on clinicians in terms of administration. Meanwhile, decompensation prediction enables more complex decision planning, and phenotype classification can also be used early on as a complementary aid to the doctor's diagnosis.

However, the value of medical time series is huge but the density is very low. These situations have brought great challenges to accurate data analysis. As a result, the core problem of health care big data research is how to use artificial intelligence technology to fully explore the value in data and realize the transformation of data values into applications. Most of the work being done now uses a small number of physiological variables and doesn't pay much attention to correlations of different variables. For instance, [4], [5] proposed benchmarks to address four meaningful clinical tasks. [6] proposed to use LSTM recurrent neural networks to handle clinical diagnosis. [3] proposed a temporal pointwise convolutional networks to handle length-of-stay prediction. However, all of these methods often lose too much relevant diagnostic data due to the sparsity of the data. At the same time, they can't say how important the diagnostic information is for the task, and it's not easy for them to give a guiding diagnosis and treatment plan.

We propose a temporal-spatial correlation attention network (TSCAN) to address various clinical characteristic prediction problems, such as predicting death, predicting length of stay, detecting physiologic decline, and classifying phenotypes. Our proposed temporal and spatial attention networks are designed to facilitate multiple core information fusion and extraction tasks. To fully exploit the information in the temporal dimension of the medical time series, we introduce a recursive and merged attention mechanism, which enables the fusion of information from previous time periods in the current time period and allows for an orderly exploration of the hidden information in the temporal dimension when dealing with long time series. Additionally, we consider both temporal and spatial dimensions, taking into account the relevance of both dimensions and fusing them, making our approach more comprehensive than most studies on medical time series, which only consider temporal connections.

Our method can effectively remove irrelevant items in clinical data as well as irrelevant nodes in time based on different tasks, resulting in more accurate prediction results. Our method can also find key clinical indicators of important outcomes that can be used to improve treatment options. Finally, we select data from the MIMIC-IV dataset to demonstrate the performance of our approach.

The contributions of this paper are as follows:

- We propose a temporal-spatial correlation attention network (TSCAN) to handle some clinical characteristic prediction problems, All indicators have exceeded the current optimal algorithm;
- We expanded the physiological variables in medical time series to 155 with the advice of professionals in collaboration with local hospitals. We also publish these data ${ }^{1}$ for other researchers' work;
- We discuss the contribution ratios of the 155 physiological variables selected for the task on the advice of professionals, which have important implications for subsequent optimization of the model and medical recommendations.
The remainder of this article is organized as follows. Section 2 illustrates the process of data selection. Section 3 presents several related works. Section 4 provides the details of our approach. The corresponding experimental results and analysis are given in Section 5. Finally, we discuss the limitations and our future work and conclude this paper in Section 6.


## II. Related Work

EHR contains different types of medical time-series data, and a great deal of research has been accomplished in medical time series analysis. The key to the research is how to automatically extract temporal associations and long-range dependencies from the data, and the main methods of the research focus on traditional machine learning methods and deep learning methods based on neural networks, of which deep learning-based medical time series analysis has gradually become a major research direction in recent years.

[^0]
## A. Traditional machine learning algorithms

Traditional machine learning methods for building predictive models based on medical time-series data have been developed over decades, including conditional random field (CRF) [7], Expectation-Maximization algorithm (EM) [8], Bayesian networks [9] and others. Caruana et al. [10] showed that backpropagation can be effective in medical data analysis, and Cooper et al. [11] demonstrated the application of eight machine learning algorithms, including K-nearest neighbor (KNN), in predicting patients' survival. Awad et al. [12] used a random forest algorithm to predict early mortality of patients, and Bayesian networks [13], [14] were used to develop multi-label classifiers, which were applied to medical multi-classification problems. Logistic Regression (LR) was widely used in the field of predicting mortality risk among hospitalized patients [11], [15]-[17] and was chosen as one of the baselines.

## B. Deep learning algorithms

In recent years, deep learning technology with deep neural networks as the core has been gradually emerging in the field of medical applications with the increase of computers' computing power. Lasko et al. [18] used hierarchical autoencoders (AEs) based on time-series data of uric acid measurements to predict the risk of gout and acute leukaemia. Chen et al. [19] proposed a model based on CNN to extract local temporal associations in time-series data for the prediction of futural risk of congestive heart failure (CHF) and chronic obstructive pulmonary disease (COPD). Mobley et al. [20] applied ANN to length of stay prediction, Grigsby et al. [21] considered length of stay prediction as a binary classification task in order to identify patients at risk of long-term hospitalisation in early stage, and Emma et al. [3] proposed the Temporal Pointwise Convolution (TPC) achieving relatively good results in this task.

Lipton et al. [6] extracted 13 variables of laboratory outcome from paediatric ICU patients and used Long Short-Term Memory networks (LSTM) to learn temporal associations and long-distance dependencies in time-series data. Choi et al. [22] used a variety of RNN models such as Gated Recurrent Unit (GRU) and LSTM networks to process clinical time-series data for the prediction of medical events. It is worth mentioning the extensive application of LSTM in clinical prediction tasks, including prediction of cardiac arrest [23], acute kidney injury [24], missing data inference [25], prediction of drugs [26], [27] and length-of-stay prediction [28].

## C. Application on specific tasks

In the task of mortality prediction, [29], [30] illustrated that artificial neural networks (ANN) can achieve better results than Logistic Regression. For decompensation prediction tasks, the Recurrent Attentive and Intensive Model (RAIM) [31] and Simply Attend and Diagnose (SAnD) [32] have applied attention mechanisms to predict physiological decompensation of critical patients in ICU. Phenotype classification is also a promising task and temporal convolutional networks [33]


[^0]:    ${ }^{1}$ https://github.com/yuyuheintju/TSCAN

and feedforward networks [18], [34] have already be used in predictions of diagnostic codes based on medical timeseries data. There were researches indicating that deep learning models represented by LSTM performs well in predicting mortality [35], [36], length of stay [28] and diagnostic classification [37]. So LSTM [4] was chosen as another baseline.

## III. MIMIC-IV DATASET

## A. Data Description

We use the Medical Information Mart for Intensive Care (MIMIC-IV v0.4) dataset [38]. The MIMIC-IV database is a public database of clinical data that researchers from all over the world can use for free. The database has clinical information on more than 380,000 patients who were admitted to Beth Israel Deaconess Medical Center in Boston, Massachusetts, USA, from 2008 to 2019. Like other EHR databases, it keeps detailed information on patients' demographics, lab tests, medication administration, vital signs, surgical operations, disease diagnosis, medication management, survival status, and more.

MIMIC-IV uses a modular approach to organize data. It has three modules that are made up of 27 tables that make it easy to use data from different sources separately or together. Another advantage is the protection of patients' privacy, which is de-identified in two steps: the first is to replace the patient identifier, hospital identifier, and so on with a random code, and the second is to add a random number of days to the date data fixed for each patient.

## B. Data Selection

The data pre-processing workflow is illustrated in Fig.1. The MIMIC-IV critical care database contains 76540 ICU stays from 53150 patients admitted.

In the first step, the important data are taken straight from the original MIMIC-IV tables and put in order by subject, which is another word for patient. This step has two parts: keeping only adults who were in the ICU (over the age of 18), who were in the ICU only once, and who did not move between ICU wards or wards during the same hospital stay. In this step, differences in how children's and adults' bodies operate and other unclear factors are taken out. This leaves 47,046 unique patients with a total of 59,372 ICU stays.

In the second step, we exclude clinical events that cannot be matched with ICU stays. Firstly, it considers events missing admission ID (HADM_ID), and only events with HADM_ID are reserved. Secondly, since the stays.csv table allows the connection of HADM_ID with ICU stays, we exclude events that do not have HADM_ID in stays.csv. Then, for events where ICU stay IDs (ICUSTAY_ID) are defaults, they can be recovered by attempting to check the ID. Finally, we only retain events for which the ICUSTAY_ID is present in stays.csv.

In the third step, a patient has a single ICU admission, which is also described as an "episode". In this script, for each episode, a list of events is put together in order of time, with only the variables from a list that has already been set. We use 155 physiologic variables, expanding from 17 variables, which are a subset from the Physionet/CinC

Challenge 2012 [39]. During the collaboration, the local hospitals helped choose the 155 physiological variables, which included 5 categorical variables and 150 continuous value variables. The 24 variables of 155 are list in Table.I. Thus far, we have obtained over 92 million events from five tables (icu/inputevents, icu/procedureevents, icu/chartevents, icu/outputevents, hosp/labevents). Finally, we fixed a test set of $15 \%(7,057)$ of patients, including 8,906 ICU stays.

## IV. Our Approach

Our model is designed to find correlations in both time and space, taking into account both temporal trends and connections between features. We hope to integrate the features of the previous time period when processing information of the end time period for long medical time sequences, and to fully exploit the hidden features of the time dimension. For the task of predicting in-hospital deaths, we want to know how much each of the 155 variables we chose in advance has to do with it. The model needs to figure out which of the three indicators-blood protein, blood pressure, and heart rate-is the best predictor of hospital mortality. This will help doctors focus on the most important information about their patients. The framework is illustrated in Fig.2, which includes two key modules: 1) Encoder: It is used to obtain the feature vector of each element in both temporal and spatial dimension; 2) Fusion-Encoder: It is used to fuse the information of these elements and obtain the final feature at the end time. The module enables a time-segmented solution to integrate information from all time periods and takes advantage of the features of the time dimension.

## A. Problem Define

For each patient, we need to predict in-hospital mortality, and other tasks in each time interval, such as the length-ofstay prediction. Fig. 3 shows the problems. To predict, we only use previous clinical data from each time interval. As shown in Fig.3, we chose the data from $t$ hours before the prediction time point as the reference data for the predicting related tasks in this paper.

For each patient $i$, we can obtain a set of samples $X^{i}=$ $\left\{x_{1}^{i}, x_{2}^{i}, \ldots, x_{t}^{i}\right\}$, where $X^{i} \in R^{t \times d} . t$ denotes that we select $t$ times clinical data before prediction time point. $d$ denotes that the $d$ clinical test values are selected in each hour. In Section 3, we select 155 clinical values based on the advice of Professor Doctor. Here, we apply the one-hot method [40] to handle clinical data and convert these clinical values in to the format of vector. Finally, in each hour, clinical data $1 \times 155$ can be convert to $1 \times d$ dimension vector for final predict task.

In the prediction task, our model needs to map medical features to clinically meaningful labels such as length of stay, in-hospital mortality, etc. A predictive model for c classification can be represented as a mapping from input to category, i.e. $f\left(X^{i}\right): R^{t \times d} \rightarrow\{0,1, \ldots, c\}$ and the entire sample data set is then denoted as $D=\left\{X^{i}, y^{i}\right\}_{i=1}^{N}$, where $y_{i}$ is the target label, $N$ is the number of samples. For the in-hospital mortality task, the patient target label is $y \in\{0,1\}$, where 0 denotes survival and 1 denotes death. The predictive model is derived

![img-0.jpeg](img-0.jpeg)

Fig. 1: Data selection. The critical care database of MIMIC-IV contains 76540 ICU stays from 53150 patients admitted, and after four data processing scripts, we can obtain 47046 ICU stays from 59372 patients admitted. Then further filtered according to the requirements of the different tasks.
from the input data $X^{i}$ to obtain the output $y_{i}^{*}=f\left(X^{i}, \theta\right)$, where $\theta$ is the parameters of the model. The key of our work is to obtain the best parameter $\theta^{*}$ for different tasks, which can minimize the difference between the output of model $y_{i}^{*}$ and the true label $y_{i}$. In the next subsection, we will detail the structure of our model.

## B. Temporal-spatial Correlation Attention Network

In order to consider the temporal and spatial information, we apply the two-branch network as Fig.2. Each branch has
the same structure, which includes the initial Encoder $E_{e}$ and the Fusion-Encoder $E_{f}$.

We divided each sample $X^{i}$ into $n$ equal parts based on the time dimension and the model follows these chunks for input:

$$
X^{i}=\left[X_{0}^{i}, X_{1}^{i}, \ldots, X_{n-1}^{i}\right], \quad X_{j}^{i} \in R^{\frac{1}{n} \times d}
$$

Temporal Branch. As shown in the upper part of Fig.2, this branch consists of two parts: an Encoder and $n-1$ FusionEncoder. $X_{0}^{i}$ is the input of Encoder and the output is denoted

TABLE I: The 24 selected clinical variables. 155 physiological variables were selected on the advice of the local hospitals during the collaboration, including 5 categorical variables and 150 continuous-value variables. Here are shown 24 of them.


![img-1.jpeg](img-1.jpeg)

Fig. 2: TSCAN. It can be divided into two branches in both space and time, which is the same tandem style with one Encoder and and $(n-1)$ Fusion-Encoder. In the temporal domain, the input is divided equally into $n$ parts into the model and an additional step of input transposition allows to utilize the attention in the characteristic field for spatial domain. as $z_{0}$ :

$$ z_{0}=E_{e}\left(X_{0}^{i} ; \omega\right) $$

where $\omega$ denotes the network parameters of Encoder. Encoder's core structure is based on a multi-head self-attention mechanism. The calculation in Encoder can be expressed in detail as follows:

$$ \begin{aligned} & E_{1}=P E\left(X_{0}^{i}\right) \ & z_{0}^{\prime}=M S A\left(X_{0}^{i}+E_{1}\right) \ & z_{0}=F F N\left(z_{0}^{\prime}\right) \end{aligned} $$

Then we process the following set of data, $X_{j}^{i}, j=$ $1, \ldots, n-1$, and merge it with previous data information, $z_{j-1}$.

The Fusion-Encoder $E_{f}$ has the same internal structure, but there is a recursive relationship. The j-th Fusion-Encoder is represented by:

$$ z_{j}=E_{f}\left(X_{j}^{i}, z_{j-1} ; \delta_{j}\right), \quad j=1,2, \ldots, n-1 $$

where $\delta_{j}$ denotes the network parameters of the j-th FusionEncoder. When $j=1$, connect line (1) in model and the second input of the 1st Fusion-Encoder is the output of Encoder, $z_{0}$. For $j=2,3, \ldots, n-1$, the second input of FusionEncoder is the output of the last Fusion-Encoder, $z_{(j-1)}$, at which point line (2) is connected. The calculation in the j-th

![img-2.jpeg](img-2.jpeg)

Fig. 3: Problem define. We choose the data of $t$ hours before the prediction time point for prediction tasks.

Fusion-Encoder is as follows:

$$
\begin{aligned}
& E_{j}=P E\left(X_{j}^{i}\right) \\
& Q=M S A\left(X_{j}^{i}+E_{j}\right) \\
& K=z_{j-1} \\
& V=M L P(\text { Concate }(Q, K)) \\
& z_{j}^{\prime}=M C A(Q, K, V) \\
& z_{j}=F F N\left(z_{j}^{\prime}\right)
\end{aligned}
$$

The core is a multi-head cross-attention mechanism in which Q is derived from self-attentive output of the j-th time series $X_{j}^{i}$, K from the previous Fusion-Encoder's output, and V from a mapping that combines Q and K . In this case, V focuses on a relatively global feature, so the recursive structure can also focus on global information.

Spatial Branch. We transpose time series blocks of $n$ equal parts as the input of the spatial branch to obtain the relevance of variable dimensions by attention mechanism. As shown in Fig.2, $\left(X_{j}^{i}\right)^{T} \in R^{d \times \frac{1}{6}}$, replaces $X_{j}^{i}$ of temporal branch. There is no additional difference between this branch and the upper one, both are composed of Encoder and Fusion-Encoder.

Finally, we can obtain $z_{n-1}^{t}$ from the temporal branch and $z_{n-1}^{s}$ from the spatial branch. Here, we connect $z_{n-1}^{t}$ and $z_{n-1}^{s}$ as the final feature of patient in the predict time point, and apply the Softmax to train and obtain final predict result. Algorithm 1 shows the overall training process.

## V. EXPERIMENTS

In this section, we select samples from patients according to different tasks. In next subsections, we will first introduce the evaluation metrics. Then, we present the results of our approach in the MIMIC-IV dataset and also discuss these experimental results. In particular, based on the results of the experiments, we invited Professional Doctors to analyze the data and give us useful clinical feedback. This showed that the model could be used and was effective.

## A. Evaluation Metrics

Predicting in-hospital mortality is a binary classification task, so the area under the receiver operating characteristic (AUC-ROC) is the main way to measure how well it works, and the area under the Precision-Recall (AUC-PR) is the supplement. The main metric for length-of-stay prediction is Median Absolute Deviation (MAD) which is lower to indicate

## Algorithm 1 Temporal-spatial Correlation Attention

Require: the initialization parameters $\omega_{0}^{t}, \delta_{0}^{t}, \omega_{0}^{s}, \delta_{0}^{s}$, the number of epochs $M$, the number of batches in each epoch $I$ and the number of parts $n$.
$: \omega^{t} \leftarrow \omega_{0}^{t}, \delta^{t} \leftarrow \delta_{0}^{t}, \omega^{s} \leftarrow \omega_{0}^{s}, \delta^{s} \leftarrow \delta_{0}^{s}$ (Initialize parameters)
$m \leftarrow 0, i \leftarrow 0$ (Initialize the counter)
while $m<M$ do
$m \leftarrow m+1$
while $i<I$ do
$i \leftarrow i+1$
for Temporal branch do
$z_{0}^{t}=E_{e}\left(X_{0}^{i} ; \omega^{t}\right)$
for $j \leftarrow 1$ to $n-1$ do
$z_{j}^{t}=E_{f}\left(X_{j}^{i}, z_{j-1}^{t} ; \delta_{j}^{t}\right)$
for Spatial branch do
$z_{0}^{s}=E_{e}\left(X_{0}^{i} ; \omega^{s}\right)$
for $j \leftarrow 1$ to $n-1$ do
$z_{j}^{s}=E_{f}\left(\left(X_{j}^{i}\right)_{T}, z_{j-1}^{s} ; \delta_{j}^{s}\right)$
Concate $z_{n-1}^{t}, z_{n-1}^{f}$ to $z_{n-1}$
Softmax $z_{n-1}$ to $y_{i}^{s}$
$\omega^{t *}, \delta^{t *}, \omega^{s *}, \delta^{s *}=\arg \min _{\omega, \delta} \operatorname{Distance}\left(y_{i}^{s}, y_{i}\right)$
$\omega^{t} \leftarrow \omega^{t *}, \delta^{t} \leftarrow \delta^{t *}, \omega^{s} \leftarrow \omega^{s *}, \delta^{s} \leftarrow \delta^{s *}$
return $\omega^{t}, \delta^{t} \quad$ (Output parameters of Temporal branch); $\omega^{s}, \delta^{s}$ (Output parameters of Spatial branch).
better performance, and Cohen's linear weighted kappa score (KAPPA) that the higher the better is usually used as a supplement. Most patients have more than one condition, so it's clear that phenotype classification is a multi-label classification problem, and we chose macro- and micro-averaged AUCROC as the evaluation criteria for this problem. Predicting decompensation is made easier by treating it as a binary classification task like predicting death, which is also mainly judged by the AUC-ROC.

## B. Results

Traditionally, Logistic Regression (LR) was the most accurate model for medical time series. In recent years, LSTM and some deeplearning methods have done well with time series. In this section, Logistic Regression [4] and LSTM [4] were used as a baseline and compared with our approach.

For in-hospital mortality prediction, the prediction time point is defined as 48 h after the beginning of the ICU stay, and $t=48 \mathrm{~h}$ which means one ICU stay is one sample. As can be seen from the Table.II, TSCAN shows a huge improvement in classification scores relative to the baseline, with feature concatenation improving by 0.011 relative to LR and Max pooling improving by 0.052 relative to LSTM, and we have achieved significant performance benefits of $0.2 \%$ compared to other SOTA methods (TPC) in ACU-ROC.

For length-of-stay prediction, we select prediction time point every 12 hours, begining at the fourth hour after the patient is admitted to the ICU and ending with the patient's discharge or death. $t=320 \mathrm{~h}, n=4$ and the task aims to predict

TABLE II: Result on in-hospital mortality prediction.


TABLE III: Result on length-of-stay prediction.


TABLE IV: Result on phenotype classification.


TABLE V: Result on decompensation prediction.


the remaining time spent of patients in ICU. As shown in Table.III, TSCAN realize a reduction of three points compared to LSTM and more than forty points compared to logistic regression in MAD. For the metric of KAPPA, TSCAN also improves by 0.009 compared to channel-wise LSTM.

For phenotype classification, $n=4$, the prediction time point is described as the end of the ICU stay (the patient is discharged or dies), and the time-series data of $t=320$ h are used to classify phenotype in order to make full use of the data during the patient's stay in the ICU. In other words, for phenotype classification, those less than 320 in length in the temporal dimension are padded with zero, and those that are
redundant are removed. As shown in the Table. IV, it can be seen that TSCAN improves by 0.056 in macro-averaged AUCROC and 0.040 in micro-averaged AUC-ROC over logistic regression. Compared to LSTM, the experiment shows an improvement of 0.025 in the macro-averaged AUC-ROC and 0.018 in the micro-averaged AUC-ROC. This shows that the internal Fusion-Encoder module also works well for problems with more than one label.

For decompensation prediction, $n=4$, we select a prediction time point every hour, 4 h after the beginning of the ICU stay, and $t=320 \mathrm{~h}$. And the results are shown in the Table V. It can be seen that TSCAN has an improvement

![img-3.jpeg](img-3.jpeg)

Fig. 4: Results of different numbers of indicators on inhospital mortality prediction. With the number of indicators increasing from 17 to 155, the growth rate of AUC-ROC is levelling off.

of 0.043 in the AUC-ROC metric and 0.112 in the AUCPR metric compared to Logic Regression, and 0.021 in the AUC-ROC metric compared to LSTM. And we have achieved significant performance benefits of 0.7% compared to other SOTA methods (channe-wise LSTM) in ACU-ROC. Even when the data is pre-processed to get a time-equal sequence, it is clear that our method can still do a great job.

### *C. Discussion on In-hospital Mortality*

We take data from the initial 48 hours of ICU stays as the sample for the prediction task. Early prediction of hospital deaths can help identify patients who are at high risk and give medical staff an alert. In the next subsections, we apply this task to define some parameters of a prediction model that will be utilized in other tasks.

*1) Number of Indicators:* In this paper, data from 155 clinical indicators was selected to handle related prediction tasks based on the recommendations of the local hospital. From a medical point of view, the accuracy of mortality prediction with different number of variables as reference is expected to vary, theoretically setting the higher the number of variables the higher the accuracy. To compare the effect of the number of variables on the results of the experiment, we randomly select clinical data from 17-155 to verify the impact of variables on prediction accuracy. The related experimental results are shown in Fig.4.

As shown in Fig.4, The number of indicators increases from 17 to 155, demonstrating that the accuracy of mortality prediction improves with the number of variables, which is congruent with objective evidence. It is shown that our model can well exploit the indicators suggested by the hospital and make full use of them in the prediction task. However, we also find that the rate of growth is gradually decreasing. This condition means that continued increases in the number of indicators may not achieve a significant improvement in forecasting. Due to data limitations, the following task also utilize 155 variables as input.

![img-4.jpeg](img-4.jpeg)

Fig. 5: Weights of times on in-hospital mortality prediction. Each encoder takes 12 hours of data input, corresponding to the twelve scales on the horizontal axis in turn, and the vertical axis shows the weights that each hour occupies.

*2) Ablation Studies:* As shown in Fig.2, the model of the scheme can be separated into two branches: the temporal domain and the characteristic domain (i.e. the spatial domain), so the ablation experiments are mainly based on the comparison of these two branches and the comparison of different fusion methods. We conducted experiments in the spatial and temporal domains respectively, and then fused the two branches in different ways. Four fusion methods are selected including feature concatenation, adding fusion, bilinear pooling and max pooling (prediction followed by fusion). The results of the ablation studies are shown in the Table.VI.

As seen in the table above, the performance of attention in the temporal domain alone is superior to that in the spatial domain alone, with an AUC-ROC score of 0.025 greater the former than the latter. Analyzing the sources of this conclusion reveals that, for medical time series, the correlation between adjacent times is extremely high, although the independence between variables is relatively high. It is also obvious that combining the temporal and spatial dimensions gives better metrics, with max pooling fusion providing the best results and concatenate fusion being the next best.

*3) Attention in Temporal Domain:* In this paper, we apply sequence time data to handle prediction problem. Naturally, We hope to find the contribution of data at different time points to the prediction results. From in-hospital mortality prediction task, we divide 48 hours’ data into 4 parts and each part include 12 hours’ data. We can obtain 4 attention maps. Here, we calculate the weights and visualize it like Fig.5. The horizontal axis represents the data of 12 moments and the vertical axis represents the correlation extracted of the temporal dimension.

From these visual result, we can find that the closer to the prediction time point, the more contribution to the prediction. As the distance from the predicted time point increases, the correlation gradually decreases. This is also combined with the actual clinical diagnosis and treatment situation. We also modified the parameter *n* of the data grouping and got similar results. For other prediction and classification tasks, we achieve the similar results. Due to the length of the paper,

TABLE VI: Ablation studies on in-hospital mortality prediction.


![img-5.jpeg](img-5.jpeg)

Fig. 6: Indicator weights for predicting in-hospital mortality The horizontal axis shows the 15 variables with the highest weighting and the vertical axis indicates their contribution to the prediction of in-hospital mortality.
the other tasks are not to discuss the weight of data in time.
4) Attention in Clinical Indicators: Attention mechanism is used to get the weights of each indicator. We hope to find out how each of the 155 chosen indicators helps with the task. Attention extraction in the spatial domain can help us reach this goal.

As shown in Fig.6, the horizontal axis shows the 15 indicators with the highest contribution ratios of the 155 used in the experiment. The vertical axis shows how much each variable contributed to the prediction of in-hospital mortality. For example, Activated Clotting Time made up more than 0.025 of the weights, which is the highest percentage. Knowing how important each indicator is can help doctors decide what to focus on and how to treat their patients. These results show that coagulation is a major factor in a patient's chance of survival, as is the use of Amiodarone for arrhythmias, SCUF for heart failure, and Magnesium for treating patients with disorders of the body's internal environment. The above situation has been affirmed by professional doctors, and it also proves that our approach has obvious advantages in the discovery of the cause of the disease, and can be applied to similar prediction tasks and the discovery of potential causes of the disease, such as DNA screening and functional discovery.

## D. Discussion on Length-of-stay Prediction

This task is to predict remaining time spent in ICU at every 12 hours of stay, which is framed as a classification problem with 10 buckets (one for ICU stays shorter than a day, seven
![img-6.jpeg](img-6.jpeg)

Fig. 7: Indicator weights for predicting length of stay It can be seen that Activated Clotting Time accounts for the highest percentage of weights at near 0.03 .
day-long buckets for each day of the first week, one for stays of over one week but less than two, and one for stays of over two weeks). With this work, ICU beds can be used more efficiently and patients can be cared for better.

We also focus on the contribution of the selected 155 indicators to the task. As shown in Fig.7, the horizontal axis shows the 15 variables with the highest proportion of the 155 variables used in the experiment, and the vertical axis indicates their contribution to the prediction of length-of-stay. From these results, we can see that ALT is responsible for the most weights, which is close to 0.03 .

## E. Discussion on Phenotype Classification

Phenotyping has applications in cohort construction for clinical studies, comorbidity detection and risk adjustment, quality improvement and surveillance, and diagnosis [45]. Based on the ICU data, the phenotyping classification task is to figure out which type of acute care the patient is in. There are 25 common conditions selected for this paper, including 8 chronic conditions that are common co-morbidities and risk factors in ICU such as essential hypertension, 12 severe conditions that are relatively more dangerous to life such as pneumonia, and 5 mixed conditions that are recurrent or chronic, with periodic acute episodes, as shown in Table.VII.

The attention map of clinical indicators is shown in Fig.8. The weights of the top 15 variables are shown on the horizontal axis, and their contributions to the task of phenotyping classification are shown on the vertical axis. Several indicators such as the esophageal echo, height, PA catheter, and PICC

TABLE VII: ICU phenotypes. There are 25 common conditions selected for this paper including 8 chronic conditions, 12 severe conditions and 5 mixed conditions.


line accounted for a higher weighting of over 0.008 , which suggests that medical staff could pay more attention to those factors when judging the phenotype.

## F. Discussion on Decompensation Prediction

The goal of this task is to figure out which patients are likely to get much worse in the next 24 hours. This setting is currently manually designed with early warning scores and thresholds below which alerts are triggered, so most of these scoring systems are based on simple thresholds and a small number of common physiological indicators, such as the National Early Warning Score (NEWS) [46] and the Modified Early Warning Score (MEWS) [47]. Decompensation prediction in the paper aims to detect patients who are physiologically decompensating, or whose conditions are deteriorating rapidly.

Referring to previous work [5], and trying to fit the early warning scoring system as closely as possible, the task of decompensation prediction in our experiment is considered as a prediction of mortality in the next 24 hours for patients in the ICU and is done every hour. So, our experiments can be run on the MIMIC-IV database, which will pull out correct features and labels.

For each hour as a prediction time point, the data is matched to a target label that says whether the patient died within 24 hours of that hour. In contrast to predicting in-hospital mortality and phenotype classification, for a single ICU stay, more than one sample can be made.

The attention map of clinical indicators is shown in Fig.9. The vertical axis shows the contribution ratios of the first 15 variables, which account for the highest weight in the task. The percentages for the top 15 variables are relatively
![img-7.jpeg](img-7.jpeg)

Fig. 8: Weights of indicators on phenotype classification. The horizontal axis presents the top 15 variables in terms of proportion and the vertical axis indicates their contribution to the task.
![img-8.jpeg](img-8.jpeg)

Fig. 9: Weights of indicators on decompensation prediction. The vertical axis shows the contribution ratios of the first 15 variables, which account for the most weight. Indicators with the highest weight is Capilary refill rate.
average, ranging from 0.005 to 0.006 . The predictions are consistent with clinical reality. For the PICC line, the patient needs intravenous nutrition and rehydration therapy, and for the PA catheter, the patient needs to be checked for complex hemodynamic disturbances. Both of these are treatments for patients who are pretty sick.

On the one hand, the results suggest that patients with IABP on left heart assist devices, arrhythmia drugs such as amiodarone, verapamil, and chest pain might be more likely to deteriorate, while patients with cardiac dysfunction might be less likely to survive. On the other hand, the capillary

refill rate and phenylephrine are important predictors of a patient's prognosis in cases of circulatory failure. This means that stable circulation and enough blood flow to tissues and organs are needed to improve the prognosis of a patient. The above indicates that cardiovascular system disease plays an important role in predicting decompensation.

## VI. CONCLUSION

The widespread use of EHR and the fast growth of deep learning have made it possible for medical time series to be processed and used in new ways. In this paper, we use the MIMIC-IV database to build a deep learning model for medical time series. This model does well at predicting inhospital mortality, with evaluation metrics that are much better than the baseline. First, based on an attention mechanism, the segmentation of the data and internal structure of the Fusion-Encoder in TSCAN give full consideration to temporal correlation of the clinical time series. Secondly, our model can also find key clinical indicators of important outcomes that can be used to improve treatment options. This has an effective guiding role for clinical diagnosis and treatment in practice.

## ACKNOWLEDGMENT

This work was supported in part by the National Natural Science Foundation of China (62272337, 61902277) and the Natural Science Foundation of Tianjin (16JCZDJC31100).
