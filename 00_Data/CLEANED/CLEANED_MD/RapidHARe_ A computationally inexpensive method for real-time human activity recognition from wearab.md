# RapidHARe: A computationally inexpensive method for real-time human activity recognition from wearable sensors 

Roman Chereshnev ${ }^{1}$ and Attila Kertész-Farkas ${ }^{* 1}$<br>${ }^{1}$ Department of Data Analysis and Artificial Intelligence, Faculty of Computer Science, National Research<br>University Higher School of Economics (HSE), Moscow, Russia

September 26, 2018


#### Abstract

Recent human activity recognition (HAR) methods, based on on-body inertial sensors, have achieved increasing performance; however, this is at the expense of longer CPU calculations and greater energy consumption. Therefore, these complex models might not be suitable for real-time prediction in mobile systems, e.g., in elder-care support and long-term health-monitoring systems. Here, we present a new method called RapidHARe for real-time human activity recognition based on modeling the distribution of a raw data in a halfsecond context window using dynamic Bayesian networks. Our method does not employ any dynamic-programming-based algorithms, which are notoriously slow for inference, nor does it employ feature extraction or selection methods. In our comparative tests, we show that RapidHARe is an extremely fast predictor, one and a half times faster than artificial neural networks (ANNs) methods, and more than eight times faster than recurrent neural networks (RNNs) and hidden Markov models (HMMs). Moreover, in performance, RapidHare achieves an F1 score of $94.27 \%$ and accuracy of $98.94 \%$, and when compared to ANN, RNN, HMM, it reduces the F1-score error rate by $45 \%, 65 \%$, and $63 \%$ and the accuracy error rate by $41 \%, 55 \%$, and $62 \%$, respectively. Therefore, RapidHARe is suitable for real-time recognition in mobile devices.


## 1 Introduction

The increasing availability of wearable body sensors leads to novel scientific studies and industrial applications in the ubiquitous computing field [1, 2]. The main areas include gesture recognition (GR) [3], recognition of activities of daily living (ADL), human activity recognition (HAR) [4], and human gait analysis (HGA) [5]. Gesture recognition mainly focuses on recognizing hand-drawn gestures in the air. Patterns to be recognized may include numbers, circles, boxes, or Latin alphabet letters. Recognition of activities of daily living, on the other hand, aims to recognize daily lifestyle activities performed primarily by the subject's [6, 7]. For instance, an interesting research topic is recognizing activities in or around the kitchen, such as cooking, loading the dishwasher or washing machine, and so on [8]. Often, these activities can be interrupted by, for example, answering the phone. Human activity recognition (HAR) usually focuses

[^0]
[^0]:    * Correspondence to akerteszfarkas@hse.ru

on activities related to or performed by legs, such as walking, jogging, turning left or right, jumping, lying down, going up or down the stairs, sitting down, and so on. Human gait analysis (HGA) focuses not only on the recognition of activities observed but also on how activities are performed. This can be useful in health-care systems for monitoring patients recovering after surgery, fall detection, or diagnosing the state of, for example, Parkinson's disease [5, 9, 10]. An important application in HGA is installing body accelerometers on the hips and legs of people with Parkinson's disease [11]. Here, the objective is to detect freezing of the gait and prevent falling incidents.

Our research group generally focuses on developing methods related to HGA and HAR, and in this article we were interested in and studied HAR methods, which have the following properties:

1. Low prediction latency.
2. Smooth, continuous activity recognition within a given activity and rapid transition in between different activities.
3. Speed and energy efficiency for mobile-pervasive technologies.

The first requirement ensures that the model is of low latency; therefore, activity prediction can be made instantly based on the latest observed data. Therefore, bidirectional models, such as bidirectional long short-term memory (LSTM) recurrent neural networks (RNN) [12] or dynamic time warping (DTW) [13] methods, are not appropriate for our aims for two main reasons: First, these bidirectional methods require a whole observed sequence before making any predictions, which would therefore increase their latency. Second, the prediction they make on a frame is based on subsequent data. Standard hidden Markov models (HMMs) have become the de facto approach for activity recognition [14, 15, 16, 17], and they yield good performance in general. However, they do so at the expense of increased latency in prediction, because Viterbi algorithms use the whole sequence, or at least some part of it, to estimate a series of activities (i.e., hidden states), and their time complexity is polynomial. Therefore, in our opinion, HMMs are not adequate for on-the-fly prediction, because the latency of these methods can be considered rather high.

The second point is to ensure that an activity recognition method provides consistent prediction within the same activity, but changes rapidly when the activity has changed. Lester et al. [16] have pointed out that a single-frame prediction method such as decision stumps is prone to yielding scattered predictions. However, human activity data are time series data in nature, and subsequent data frames are highly correlated. This tremendous amount of information can be exploited simply by sequential models such as HMM and RNN, or by incorporating the sliding-window technique to single-frame methods (e.g., nearest-neighbor). In fact, the authors in [15] have pointed out that the continuous-emissions HMM-based sequential classifier (cHMM) performs systematically better than its simple single-frame Gaussian mixture model (GMM) counterpart ( $99.1 \%$ vs. $92.2 \%$ in accuracy). Actually, the proposed sequential classifier wins over all its tested single-frame competitors (the best single-frame classifier is the nearest mean (NM) classifier which achieves up to $98.5 \%$ in accuracy). This highlights the relevance of exploiting the statistical correlation from human dynamics.

Continuous sensing and evaluating CPU-intensive prediction methods rapidly deplete a mobile system's energy. Therefore, the third point requires a system to be energy-efficient enough for mobile-pervasive technologies. Several approaches have been introduced for this problem. Some methods aim to keep the number of necessary sensors low by adaptive selection [18] or based on the activity performed [19, 20, 21], for accurate activity prediction. Other approaches aim to reduce the computational cost by feature selection [22], feature learning [23], or proposing computationally inexpensive prediction models such as C4.5, random forest [24], or decision trees [25]. In this study, we put emphasis on a computationally inexpensive prediction model that uses little memory and takes few

computational steps while still achieving good performance.
Recently, deep-learning technologies, deep LSTM, and deep convolutional LSTM (DCSLTM) have emerged for activity recognition systems with superb performance, mainly in ADL and GR [26, 27]. These methods are capable of learning features automatically from the data [28]. The price of this skill is that they consist of millions of model parameters that are more difficult to train, and most importantly, they result in longer prediction times and require more CPU time compared to inexpensive models such as decision trees. On the other hand, we argue that these methods have too high of a capacity for HAR and HGA problems, and thus they overfit. In our opinion, these problems involve only a few thousands input features, and the "complexity" of the underlying data manifold is rather low. LSTM methods have the capacity to remember the activity performed sometime ago, which might be useful for recognizing daily activities, such as scrambling eggs or washing dishes. However, for HAR and HGA-related problems, such skills are not needed, because we think that the current activity is independent of activities performed some time ago. For instance, if the next activity is going to be walking up the stairs, then it is because there are stairs ahead, and this fact is independent of previous activities, whether the user was sitting or running before. In our opinion, our hypothesis is supported by the studies in [26, 27]. Both studies have reported improvement in performance for ADL using deep LSTM methods. However, in freezing-of-gait prediction tasks, Hammerla et al. have reported a 76\% F1 score in Table 2 in [27], while a simple method such as random forests and C4.5 using smartly crafted features has achieved an F1 score over $95 \%$ on the same dataset, as shown in Table 2 in [24]. Similar conclusions can be reached from the results presented in Table 2 in [29], where the nearest-neighbor and random forest methods outperform multilayer perceptrons in test scenarios (which the authors termed "impersonal" and "hybrid") in which training and test data were recorded by different users. We think these results support our argument, and, therefore, deep models of high capacity for HAR and HGA problems do not seem to be justified to us. We believe that smartly designed features used along with computationally inexpensive models can provide faster and more energy-efficient methods with low latency for this field.

In this article, we present a novel method for HAR called RapidHARe for real-time prediction of continuous activity recognition. The proposed model is a small dynamic Bayesian network that does not utilize the Viterbi algorithm or other dynamic programming approaches for activity prediction, but instead utilizes the data distribution within a small, half-second-long context window. Moreover, our method does not employ feature transformation and selection methods. This provides a quick method that does not require exhaustive CPU calculations. Therefore, RapidHARe is suitable for real-time recognition. Moreover, it is inexpensive for mobile systems and can be employed in elder-care support and long-term health-monitoring systems such as freeze-of-gait prediction, fall detection, robotic exoskeletons in health care, and surgery recovery.

This article is organized as follows: In section 2, we introduce the mathematical model of RapidHARe by using dynamic Bayesian networks. In section 3, we describe the data we used in our experiments. In section 4, we present our experimental results obtained and discuss our findings. Finally, we conclude our study in the last section.

# 2 Methods 

We created a dynamic Bayesian network, whose structure is shown in Figure 1. The states, i.e., activities, denoted by $S$ and the probability of a state $s_{t}$ at a given time $t$ with respect to a given observed context window $v_{t}, v_{t-1}, \cdots, v_{t-K}$ of length $K$, is formulated by

$$
\begin{gathered}
P\left(s_{t} \mid v_{t}, v_{t-1}, \cdots, v_{t-K}\right)= \\
\frac{\prod_{k=0}^{K} P\left(v_{t-k} \mid s_{t}\right) P\left(s_{t}\right)}{\sum_{n=1}^{N} \prod_{k=0}^{K} P\left(v_{t-k} \mid s_{t}=n\right) P\left(s_{t}=n\right)}
\end{gathered}
$$

Certainly, at the beginning of performance, when $t<K$, the context window is adjusted. In our experiments, we did not use different $a$ priori class probabilities for different $P\left(s_{k}\right)$. This is because we did not want our model to be biased toward some states that are abundant in the training data. Therefore, the activity prediction should be based fully on the data, and the state probabilities $P\left(s_{k}\right)$ can be omitted from Eq. 1.

The state being performed at time $t$ can be predicted as follows:

$$
\hat{s}_{t}=\operatorname{argmax}_{s_{t}}\left\{P\left(s_{t} \mid v_{t}, v_{t-1}, \cdots, v_{t-K}\right)\right\}
$$

Since the optimum of Eq. 2 is invariant to normalization, the normalization factor can be omitted from Eq. 1. This gives us a very simple model for activity prediction in the following form:

$$
\hat{s}_{t}=\operatorname{argmax}_{s_{t}}\left\{\prod_{k=0}^{K} P\left(v_{t-k} \mid s_{t}\right)\right\}
$$

This model can be implemented using the rolling-window technique for real-time continuous activity recognition; thus, the model remains fast for large $K \mathrm{~s}$, and redundant calculation of $P\left(v_{t-k} \mid s_{t}\right)(k>0)$ can be avoided by using tables.
![img-0.jpeg](img-0.jpeg)

Figure 1: Illustration of an unfolded dynamic Bayesian network w.r.t. an activity series.

The distribution $P(V \mid S)$ with respect to a given state is modeled with Gaussian mixture models (GMMs), and its parameters are trained using the expectation-maximization (EM) method. The training of GMMs was straightforward because training data were segmented.

Overall, we obtained a simple and fast model that consumes little energy to recognize human activities.

## 3 Data collection

To perform our experiments, we have recorded a total of 5 hours of data from 18 participants performing 8 different activities. These participants were healthy young adults: 4 females and 14 males with an average age of 23.67 years (standard deviation [STD]: 3.69), an

Table 1: Characteristics of data and activities


![img-1.jpeg](img-1.jpeg)

Figure 2: Sensor locations. Circles show EMG sensors, while boxes represent accelerometers and gyroscopes.

Average height of 179.06 cm (STD: 9.85), and an average weight of 73.44 kg (STD: 16.67). The participants performed a combination of activities at normal speed in a casual way, and there were no obstacles placed in their way. For instance, starting in the sitting position, the participant was instructed to perform the following activities: sitting, standing up, walking, going up the stairs, walking, sitting down. The experimenter recorded the data continually using a laptop and annotated the data with the activities performed. This provided us a long, continuous sequence of segmented data annotated with activities. We developed our own data-collector program. In total, 1,138,079 samples were collected. A summary of the activities recorded and other characteristics of the data is shown in Table 1.

During data collection, we used MPU9250 inertial sensors and electromyography (EMG) sensors made in the Laboratory of Applied Cybernetics Systems, MIPT (www.mipt.ru). Each EMG sensor has a voltage gain of about 5000, and a band-pass filter with bandwidth corresponding to a power spectrum of EMG (10–500 Hz). The sample rate of each EMG-channel is 1.0 kHz, the ADC resolution is 8 bits, and the input voltages is 0–5 V. The inertial sensors consisted of a three-axis accelerometer and a three-axis gyroscope integrated into a single chip. Data were collected with the accelerometer's range equal to ±2g with sensitivity 16.384 LSB/g and the gyroscope's range equal to ±2000°/s with sensitivity 16.4 LSB/°/s. All sensors were powered with a battery, which helped to minimize electrical grid noise.

Accelerometer and gyroscope signals were stored in int16 format. EMG signals were stored in uint8. In our experiments, all data were scaled to range [–1, 1].

In total, six pieces of inertial sensors (three-axis accelerometer and three-axis gyroscope) and one pair of EMG sensors were installed symmetrically on the right and left legs with elastic bands. A pair of inertial sensors were installed on the rectus femoris muscle 5 cm

above the knee, a pair of sensors around the middle of the shinbone at the level where the calf muscle ends, and a pair on the feet on the metatarsal bones. This provided 36 features. Two EMG sensors were placed on the vastus lateralis and connected to the skin by three electrodes. The EMG sensors additionally provided two more features. The locations of the sensors are shown in Figure 2. In total, 38 signals were collected.

The sensors were connected through wires with each other and to a microcontroller box, which contained an Arduino electronics platform with a Bluetooth module. The microcontroller collected 56.3500 samples per second on average, with a STD 3.2057, and then transmitted them to a laptop through the Bluetooth connection.

Data acquisition was carried out mainly inside a building. We note that data were not recorded on a treadmill. The data are available in [30].

# 4 Results and discussions 

The performance of our RapidHARe model was evaluated using a supervised cross-validation approach [31]. In this approach, data from a designated participant were held out for tests, data from another participant were held for validation, and the rest of the data from the 16 participants were used for training. Thus, this approach gives a reliable estimation of how an activity recognition system would perform on a new user whose data have not been seen before. In our experiments, we repeated this test for every user in the dataset and averaged the results. A similar testing procedure has been introduced by Weiss et al. [29]. Our methods were implemented using the Python scikit-learn package (version 0.18.1) on a PC equipped with Intel Core i7-4790 CPU, 8 Gb DDR-III 2400 MHz RAM, and Nvidia GTX Titan X GPU.

Please note that, besides the feature scaling described in section 3, we did not use any preprocessing step, feature extraction, or feature selection methods.

### 4.1 On hyperparameters

In our first experiment, we determined the values of the length of the context window and number of the Gaussian components in $P(V \mid S)$ via grid search for RapidHARe. In our tests, the covariance matrices $\Sigma$ in all Gaussian components were restricted to be diagonal. The results were evaluated in terms of accuracy and F1 score and are shown in Figures 3 and 4. They indicate that a good performance can be achieved using $K=26$ for the context window length. However, for the Gaussian components, it seems that for dynamic activities, such as walking and running, the higher the number of Gaussian components, the better the performance. On the other hand, for static activities, such as sitting and standing, a large number of Gaussian components hinders the activity recognition. Therefore, we set the number of Gaussian components for $P(V \mid S)$ for the following activities: walking, 18; running, 18; going up, 16; going down, 16; sitting, 2; standing up, 5; sitting down, 7; and standing, 4. The activity recognition results using these hyperparameters are shown in Table 2, and we achieved $97.85 \%$ accuracy, $87.4 \%$ precision, $87.22 \%$ recall, and an $86.4 \%$ F1 score. The confusion matrix is shown in Table 3.

![img-2.jpeg](img-2.jpeg)

Figure 3: Accuracy w.r.t. the number of Gaussian components and the length of the context window.
![img-3.jpeg](img-3.jpeg)

Figure 4: F1 scores w.r.t. the number of Gaussian components and the length of the context window.

Table 2: Results of activity recognition


Table 3: Confusion matrix


# 4.2 Continuous activity recognition 

Next, we examined how well RapidHARe performs on continuous activity recognition. For this reason, we took a continuous series of activities and performed the activity recognition. Then, we plotted the true and predicted activities on a time line, shown in Figure 5. The results show that our method does predict continuous activities, and it does not predict scattered activities for neighboring frames except for a few frames.

However, it looks like, misclassification occurs on the borders in many cases. Furthermore, if we enlarge the standing-sitting activity at 35.6 sec , as shown in Figure 6, we can see that our method predicts sitting activity, at around 40.94 sec , a small fraction of a second earlier than it happened, according to the data annotation. It is unlikely that our method can predict the future. This phenomenon could be a result of inaccurate data segmentation made by the data controller and by the fact that it is difficult to exactly determine an activity border in 10-20 ms. We also plotted over the activities the signals measured by the x -axis accelerometer placed on the right thigh. This example shows that, in our opinion, the activity borders predicted by our model are actually aligned with the signal changes more appropriately than are the borders determined by the experimenter.

In order to mitigate this phenomenon, we allow some tolerance in the misclassification if it occurs on the activity border. Thus, we tolerate up to 25 data frames (which is about half a second) to be misclassified on the activity border if and only if our method correctly recognizes the succeeding activity. We believe that a half-second misclassification on the activity borders during continuous activity recognition is acceptable in practice. Moreover, if we allow misclassification on the borders, then we think the performance measures will put an emphasis on more reliable estimation for the actual scattered misclassification made by the model, and it will be more tolerant of inaccurate data segmentation.

When we tolerate misclassification on the border up to 25 data frames, we obtain $98.68 \%$ accuracy, $91.52 \%$ recall, $92.5 \%$ precision, and $91.34 \% \mathrm{~F} 1$ on average over all activities. The detailed results for each activity are shown in Table 4. The confusion matrix obtained with border tolerance is presented in Table 5.

In the rest of our experiments, we allowed a border tolerance up to 25 data frames, unless otherwise specified.

![img-4.jpeg](img-4.jpeg)

Figure 5: Continuous activity recognition

![img-5.jpeg](img-5.jpeg)

Figure 6: Activity recognition at 35.6 s enlarged from Figure 5. The line represents the x-axis acceleration value recorded by accelerometer located on thigh.

### 4.3 Directional features

Examining the results in Tables 4 and 5 shows that the recognition performance of sitting down and standing up activities are relatively poor compared to other activities. We further investigated the problem, and we plotted the data recorded with a 3D accelerometer sensor located on the left thigh during standing, sitting, standing up, and sitting down activities. Data are shown in Figure 7. The figure reveals that data from static activities are precisely concentrated on countersides, but the data from dynamic activities lay on top of each other and in-between the static activities. Therefore, it is difficult to distinguish the two dynamic activities. However, if we consider the time stamp of the data in the dynamic activities, we can see that data from the sitting-down activity go from standing to sitting, but data related to the standing-up activity go from sitting to standing activity. Therefore, we created additional features to indicate changes in signal data. For a signal datum $s_i[t]$ at time $t$ from $x$ and $z$-axis accelerometer sensors located on both thighs, we created four additional features as $d_i[t] = s_i[t] - s_i[t - a]$, called directional features, where $i = {1, 2, 3, 4}$ indexes the aforementioned signals, and $a$ is a lag parameter denoting time offset. For instance, if $s_i[t]$ is the signal obtained at time $t$ from the $x$-axis accelerometer sensor located on the left thigh, then $d_i[t]$ indicates how much this signal has changed since time $t - a$. Thus, we obtained four additional features. The original 38-feature-data vector $s[t]$ were concatenated with 4-feature-data vector $d[t]$, yielding 42 features in total for every sample. These new features add extra information about the direction of movements.

To calibrate the lag parameter, we ran a line search and obtained the best results using $a = 15$, which is equivalent to approximately a third of a second (data not shown). Thus, in the rest of our test, we used $a = 15$ for the lag parameter.

The results obtained using the directional features are shown in Table 6, and they indicate a 50–65% decline in the overall error (cf. Table 4) for the measured metrics. However, closer investigation of the sitting down and standing-up activities reveals even greater improvement. For instance, the F1 score increases from 80.47% to 93.43% for sitting down and from 85.69% to 96.94% for standing-up. The confusion matrix obtained using directional features, shown in Table 7, also shows decreased misclassification of activities (cf. Table 5).

Table 4: Continuous activity recognition allowing border tolerance


Table 5: Confusion matrix allowing border tolerance


![img-6.jpeg](img-6.jpeg)

Figure 7: Data from x- and z-axis accelerometer located on left thigh. Data from y-axis accelerometer were nearly constant and thus are not shown.

### 4.4 State-of-the-art methods

Here, we introduce the state-of-the-art methods that we used in our comparative tests, and we provide the experimental results of the grid search used to find the best hyperparameter settings. The following methods were used: hidden Markov model (HMM), artificial neural network (ANN), and recurrent neural network (RNN). HMM was taken from hmmlearn (version 0.2.0), while ANN and RNN were taken from the Keras (version 1.2.2) libraries with Theano (version 0.8.2) support in Python.

In the HMM, the data emission probabilities were modeled with Gaussian mixture models. Initial state probabilities were equally 0.125. The state transition probability matrix we used is shown in Table 8. Between certain activities, the transition probabilities are set to zero to prohibit absurd transitions. For instance, a *sitting* cannot be followed by *running* without first *standing up*. We calibrated the transition matrix manually because we did not want HMM to prefer states based on *a priori* information obtained from the training data.

We ran a grid search on the number of GMM components vs. the window length used in the Viterbi algorithm in order to find the best hyperparameters. Parameters were initialized randomly, and tests were repeated five times. The averaged results (along with the standard deviations (STD) in parentheses) are shown in Table 9. Our results indicate that the best accuracy can be achieved using 30 Gaussian components with 50 data frames passed to the Viterbi algorithm. In our experiments with HMMs, we decided to use the same number of

Table 6: Results of activity recognition with directional features


Table 7: Confusion matrix using directional features


GMM components as for the RapidHARe for two reasons: First, this gives us better performance with HMM, and second, the prediction speeds of HMM and RapidHARe becomes comparable. The choice of the window length is also critical. Long windows result in large lag times in prediction. Because the sampling rate is around 56 samples per seconds, the main drawback of long window length is that the system has to wait a long time to collect the adequate number of data samples before prediction. For instance, a window length 50 results in almost a 1 s lag time before any prediction can be made. However, the advantage of long windows is that the prediction can be made for a bigger data chunk, which reduces the prediction time per sample. In our experiments, we decided set the window length to 10 because we found this to be the best trade-off between accuracy and speed. Fewer data yielded worse accuracy, while longer blocks increased the prediction latency.

To find the best ANN structure, we ran a grid search over the following hyperparameters: (1) number of hidden units within a layer from 10 to 400; (2) number of hidden layers: 1 or 2 ; (3) activation function: sigmoid or rectified linear unit (ReLU). The training was performed with an Adam optimizer and with early stopping. In the early stopping, the training stopped if the validation loss reduced less than 1e-6 in the last three epochs or if the average validation loss of the last 10 epochs was greater than the average validation loss of the preceding 10 epochs (that is, the cost tended to grow). An example for the learning curves along with the loss on the validation set is shown in Figure 8. Tests were repeated five times; average results are shown in Table 10, along with STD in parentheses. The results indicate that structures with the ReLU activation function performed poorly; however, two-layered structure with a sigmoid activation function seemed to be overfit and slow in prediction. The best performance with ANN can be achieved using a single layer network with

Table 8: Transition matrix for hidden Markov model


Table 9: HMM grid search result


Tests were repeated five times; mean results are shown along with STD in parentheses. Performance measures are averaged over activities. ${ }^{1}$ The number of parameters in the models to be trained. ${ }^{2}$ Time in micro seconds to predict the activity of a single data frame measured on a single-thread CPU. ${ }^{3}$ Time in seconds to wait to collect an adequate number of data samples.
![img-7.jpeg](img-7.jpeg)

Figure 8: Learning curve for early stopping. Training terminated after epoch 80 because of lack of improvement on the validation set.
sigmoid activation function having 200 hidden unites, and this is the structure we used in our comparative tests.
For the best hyperparameter search for the RNN, we ran a grid search over the number of hidden units from 10 to 200 using sigmoid or ReLU activation functions. Tests were repeated five times, and the averaged results along with STD presented in Table 11. The results indicate that RNN can be considered rather slow. Moreover, ReLU seems to perform poorly compared to the sigmoid activation function. The best performance was achieved using 200 hidden units with a sigmoid activation function organized in a single layer. Thus, this is the structure for RNN we used in our comparative tests.

# 4.5 Comparison to state-of-the-art methods 

Here we compare the performance of the RapidHARe methods to state-of-the-art methods. Recognition performance was evaluated by recall, precision, F1 score, and accuracy, and our main results are summarized in the Table 12A. The best results were achieved using the RapidHARe method using directional features (RapidHARe-DF) and all features from all sensors when we allowed tolerance on the border between activities. RapidHARe-DF has achieved a $94.27 \%$ F1 score and $98.94 \%$ accuracy. Compared to ANN, RNN, and HMM,

Table 10: Artificial neural network grid search result


this decreased the F1 score error rate by $46 \%, 66 \%$, and $63 \%$ and the accuracy error rate by $41 \%, 55 \%$, and $62 \%$, respectively. Allowing border tolerance improves performance metrics. For instance, by allowing border tolerance, the RapidHARe-DF method reduced the F1 score error rate by $52 \%$ and the accuracy error rate by $49 \%$ when compared to the case when border tolerance was not allowed. However, border tolerance for ANN, RNN, and HMM reduced the F1-score error rate by $19 \%, 2 \%$, and $15 \%$, respectively, and the accuracy error rate by $15 \%, 2 \%$, and $15 \%$, respectively. This suggests that the ANN, RNN, and HMM methods tend to make more scattered misclassifications within the same activity rather than at the border between different activities.

Because one of our aims is to develop a simple model for HAR prediction, we tested these methods with fewer features as well. First, we kept the triaxial accelerometer data obtained from accelerometers located on the thigh and shin, and second, we kept the accelerometer data from only the thigh. All gyroscope and EMG data were omitted. The results are shown in Tables 12B and 12C. When border tolerance is taken into account, ANN's performance drops from $89.4 \%$ to $62.16 \%$ in the F1 score as the amount of information and the number of features decrease. The F1 scores for RNN and HMM decrease moderately from $83.31 \%$ to $76.73 \%$ and $84.34 \%$ to $73.54 \%$, respectively. While RapidHARe also shows loss in performance, RapidHare-DF seems to be robust, and its performance remains roughly the same; it outperforms all state-of-the-art methods under limited data. Similar tendencies can be observed when the

Table 11: Recurrent Neural network


performance is evaluated in accuracy with and without allowing border tolerance.
The CPU time is remarkably low for our model. RapidHARe and RapidHARe-DF perform activity predictions around one and a half times faster than ANN, eight times faster than HMM , and more than ten times faster than RNN. It is worth noting that the number of model parameters is also the lowest for our model, while HMM and RNN consist of significantly more parameters. The timing results and the number of parameters are shown in Table 12 as well. In our opinion, these facts make our model plainly appropriate for real-time recognition.

# 5 Conclusions 

In this article, we have presented a new, fast, and computationally inexpensive method, called RapidHARe, for continuous activity recognition. It predicts activities based on the distribution of the raw data in a small, half-second-long context window, in which the distribution was modeled using Gaussian mixture models. Note that, our method does not employ any dynamic-programming-based algorithms for inference, as they are known to be slow. This fact makes RapidHARe an extremely fast predictor; as comparative tests showed, our method is one and a half times faster than an ANN method, and more than eights time faster than RNN and HMM methods.

RapidHARe outperforms the current state-of-the-art methods in accuracy as well. However, performance can be further improved using additional features, termed directional features, that exploit information about signal changes. This information is especially useful in distinguishing among sitting-related activities, such as sitting down and standing up. We also discussed the difficulty of exactly determining the border between two subsequent activities in the signal. If we allow a little tolerance around the border in the performance evaluation, then RapidHARe provides nearly perfect performance, while the other methods' performance remain roughly the same. This, in our opinion, indicates that the other methods tend to make scattered misclassifications within the same activity.

It is also worth mentioning that our method did not utilize any data preprocessing, feature-selection, extraction, or transformation methods, and it still achieved outstanding performance. Perhaps these preprocessing methods could contribute to better performance, but this would come at the expense of additional CPU time.

Table 12: A) Main classification results


Performance measures are averaged over activities. ${ }^{1}$ RapidHARe using directional features (DF). ${ }^{2}$ The number of parameters in the models to be trained. ${ }^{3}$ Time in micro seconds to predict the activity of a single data frame measured on a single-thread CPU.

In this article, we investigated HAR methods from purely computational aspects, but we did not discuss any hardware-related issues or how our systems could be implemented on mobile devices. Since our method is the fastest and requires the smallest amount of memory to store the predictor model, we believe that RapidHARe would consume the least amount of energy compared to the current state-of-the-art methods, independently from the hardware specifications. That is, if a HAR system were implemented on a PC, mobile phone, or microcontroller, the energy consumption for data collection or for wireless data transfer from the sensors to work stations (PC, mobile phone) would be the same independently from the chosen HAR model.

Finally, we also mention that GPUs (and NPUs) are becoming standard chips in mobile devices in order to perform AI features - for instance, in Huawei's Mate 10 (Kirin 970) and Google's Pixel 2 (Adreno 540) - and therefore, HAR systems could perform inference on these GPUs. In this case, the inference will become faster and independent of the method, albeit at the expense of additional energy consumption. As we argued in the introduction that the HAR problem is simple and does not require a large number of data features and computationally exhaustive inference algorithms, we think that the speed gained by GPUs might be not worth the additional energy consumption required by GPUs and by the data transfer from the CPU/memory to the GPU.

# Acknowledgements 

We gratefully acknowledge the support of NVIDIA Corporation with the donation of the GTX Titan X GPU used for model parameter training in this research. We would like thank the participants in the data acquisition for the effort and time they devoted to this work. We would also like to thank to Timur Bergaliyev and his lab members Sergey Sakhno and Sergey Kravchenko from Laboratory of Applied Cybernetic Systems at MIPT and BiTronics Lab (www.bitronicslab.com) for their technical support on using sensors.
