# Quantifying Uncertainty with Probabilistic Machine Learning Modeling in Wireless Sensing 

Amit Kachroo<br>Amazon Lab126<br>Sunnyvale, California, USA<br>amkachro@amazon.com

Sai Prashanth Chinnapalli<br>Amazon Lab126<br>Sunnyvale, California, USA<br>saic@amazon.com


#### Abstract

The application of machine learning (ML) techniques in wireless communication domain has seen a tremendous growth over the years especially in the wireless sensing domain. However, the questions surrounding the ML model's inference reliability, and uncertainty associated with its predictions are never answered or communicated properly. This itself raises a lot of questions on the transparency of these ML systems. Developing ML systems with probabilistic modeling can solve this problem easily, where one can quantify uncertainty whether it is arising from the data (irreducible error or aleotoric uncertainty) or from the model itself (reducible or epistemic uncertainty). This paper describes the idea behind these types of uncertainty quantification in detail and uses a real example of WiFi channel state information (CSI) based sensing for motion/no-motion cases to demonstrate the uncertainty modeling. This work will serve as a template to model uncertainty in predictions not only for WiFi sensing but for most wireless sensing applications ranging from WiFi to millimeter wave radar based sensing that utilizes AI/ML models.


Index Terms—probabilistic modeling, Bayesian networks, wireless sensing, WiFi, uncertainty quantification

## I. INTRODUCTION

The application of artificial intelligence (AI)/ machine learning (ML) algorithms in wireless sensing applications is seeing an immense growth over the years, and in-fact these models are now embedded into real-world products and features. The main advantages of utilizing AI/ML techniques over conventional principle techniques is the reduced computation complexity, increased energy efficiency, and better optimal solutions [1]. However, one of the biggest challenges associated with these AI/ML models is in its inference reliability or put simply, how confident is the model in its predictions. This unfortunately has not been clearly understood or quantified in the domain of AI/ML in wireless sensing area. Recently, there has been a lot of research on this topic [2]-[4], but these are mostly limited to medical or computer vision field. This paper will therefore present the science behind the uncertainty modeling, which will help to answer the model reliability. We will dwell into more details about this method with a real example of WiFi channel state information (CSI) based sensing for motion/no-motion detection application.

Generally, uncertainty is classified into two broad categories, aleotoric and epistemic uncertainty [5]-[7]. Aleotoric derives its name from the Latin word "alea" that means the roll of a dice and Epistemic derives its name from the Greek word
"episteme", which can be roughly translated as knowledge. Therefore, aleotoric uncertainty is the internal randomness of a phenomena and epistemic is presumed to derive from the lack of knowledge regarding the phenomena. In wireless sensing applications, this is a very common phenomenon where a AI/ML model trained on a certain set of home environments performs in a very uncertain way when tested on a different home environment. The main reason of the failure of these ML models is because of the model not only learns the features extracted from the radio frequency (RF) signals but also learns the other information from environment, which is not desired in RF sensing. This extra information is due to the fact that the RF signals are highly dependent on the scattering conditions such as reflections/ diffraction's from the objects in the environment (walls, furniture, etc.), and also on the position and distance of different objects or human/pets from the radio device. Therefore, it becomes a necessity for AI/ML model developed for wireless sensing to communicate its reliability or uncertainty associated with its predictions.

In this work, we will discuss the method to include uncertainty (aleotoric and epistemic) into the ML model, and discuss pros and cons of this approach in detail. In summary, the main contributions of the paper are,

- Understanding different types of uncertainty associated with a AI/ML model.
- Modeling uncertainty in a AI/Ml model with a real life example of WiFi sensing.
- Discussions on the results highlighting the need of incorporating uncertainty in wireless sensing applications.
This paper is organized as follows, Section II discusses the different types of uncertainty in detail for AI/ML models, Section III presents the details of the WiFi CSI based motion/nomotion detection application. In Section IV, we will discuss the model and the results of uncertainty quantification for our example in detail and finally, the conclusion with future work are drawn in Section V.


## II. Uncertainty in AI/ML models

To start with, the term uncertainty actually in itself means lack of knowledge to a particular outcome. In AI/ML domain, this can be attributed to either data itself (measurement noise, or wrong labeling) or to the model (model parameters) or lack

of training data. This is broadly classified as aleotoric and epistemic uncertainty.

- Aleotoric or indirect uncertainty- This type of uncertainty arises from the unaccounted factors, such as environment settings, noise in the input data, or bad input feature selections. It is also known as an irreducible error and can’t be remediated with more data. One of the solution to overcome such uncertainty is to make sure that the data collection strategy is carefully designed and the measurement environment is constrained so that the effect of environment or any external factors is minimized. Also careful feature selection that represents the phenomena or application is of utmost importance to avoid such uncertainty.
- Epistemic or direct uncertainty- This type of uncertainty usually arises from the lack of knowledge about the model or data. One example can be over-generalization, where the ML model is very complex as compared to the amount of data it is trained on and thereby overgeneralizes on a test dataset. This type of uncertainty can be overcomed by collecting more data or experimenting with different ML model architectures or by changing/tweaking model parameters. Since, this uncertainty is caused inherently by the model/data, therefore it can be easily reduced by more data or by different model architecture.

Epistemic uncertainty is also used to detect dataset shifts (test data has different distribution than training), or adversarial inputs. Modeling epistemic uncertainty is challenging than modeling the aleotoric one. The later one is incorporated in the model loss function while the epistemic is highly dependent on the model itself and may vary from one model architecture to other.

## A. Modeling Aleotoric and Epistemic Uncertainty

Given a dataset, $\mathbb{D}=\left\{X_{i},y_{i}\right\}, i \in\{1, \ldots, n\}$, where $X_{i}$ is the $i^{t h}$ input, $y_{i}$ is the $i^{t h}$ output and $n$ is the total number of input examples in the dataset, the ML model can be then described as a function, $\hat{f}: X_{i} \mapsto \hat{y_{i}}$, or

$$
\hat{y}_{i}=\hat{f}\left(X_{i}\right)
$$

and lets assume the original data generating process can be given by a function $f: X_{i} \mapsto y_{i}$, such that $y_{i}=f\left(X_{i}\right)+\epsilon_{i}$, where $\epsilon_{i}$ represents the irreducible error caused by measurement errors during data collection or by wrong labeling in the training data or bad input feature selection. Thus, the mean square error (MSE) between the actual labels and predicted labels from the model will be given as,

$$
\begin{aligned}
E\left(y_{i}-\hat{y_{i}}\right)^{2} & =E\left(f\left(X_{i}\right)+\epsilon_{i}-\hat{f}\left(X_{i}\right)\right) \\
& =\underbrace{[f\left(X_{i}\right)-\hat{f}\left(X_{i}\right)]^{2}}_{\text {reducible error }}+\underbrace{\operatorname{Var}\left(\epsilon_{i}\right)}_{\text {irreducible error }}
\end{aligned}
$$

The first part in (2) is model dependent and therefore represents epistemic uncertainty while the second term (variance
of $\epsilon_{i}$ ) is the irreducible or aleotoric uncertainty. This variance of $\epsilon_{i}$ is also known as the Bayes error, which actually is the lowest possible prediction error than can be achieved with any model. In literature, $\epsilon$ is generally modeled as an independent and identically distributed (i.i.d) Normal distribution, $\epsilon_{i} \sim \mathcal{N}\left(\mu_{i}, \sigma_{i}\right)$. To incorporate the aleotoric uncertainty in a AI/ML model, the final layer can be therefore replaced with a probabilistic layer, usually a normally distributed one with a mean of $\mu$ and a standard deviation of $\sigma$. During training/testing phase, samples are drawn from this layer for prediction and also for aleotoric uncertainty quantification ${ }^{1}$. The problem with this approach is to figure out how to learn the parameters of this Normal distribution. This can be solved by defining a new cost function, negative log-likelihood (NLL) that represents the loss between a distribution and the true output label.

The NLL is equivalent to maximizing the likelihood of observing a data given a distribution with its parameters. In NLL, the logarithmic probabilities associated with each class is summed up for a dataset. This closely resembles the cross entropy loss function except in cross entropy, the last classification activation is implicitly applied before taking the logarithmic transformation, while in NLL this is not the case. The NLL is given as,

$$
\mathrm{NLL}=-\log P\left(y_{i} \mid X_{i} ; \mu, \sigma\right)
$$

With NLL as a cost function and the last layer as a probabilistic layer, the aleotoric uncertainty can thus be modeled as described in Algorithm 1. The independent normal layer can be implemented in any modern day ML packages. In our case, we used the TensorFlow Probability package [8] to model such layer.

```
Algorithm 1 method to measure Aleotoric uncertainty
Input: \(\mathbb{D}\left(X_{i}, y_{i}\right)\), replace output layer with probabilistic
    node: \(\mathcal{N}(\mu, \sigma)\), define optimizer as rmsProp and set it's
    learning rate, set num_epochs for training.
Output: \(\hat{y}_{i}\)
    for epoch \(=1\) to num_epochs do
        i) Calculate loss and gradients using NLL (3) and the
        defined optimizer
        ii) Apply gradients and update weights
        iii) Monitor loss and accuracy
    end for
    6: Determine the parameters \(\mu\) and \(\sigma\) from the output layer
```

Once the mean and standard deviation is determined, we can then easily figure out the $95 \%$ confidence interval for the trained data or even for the test data. For classification problems, the last layer can be modeled as a categorical distribution, where for each class, there is a learned distribution and based on the learned parameters for these distribution,

[^0]
[^0]:    ${ }^{1}$ This assumes the ML architecture chosen is able to give high accuracy before replacing the output layer.

aleotoric uncertainty can be measured across classes. For more details on the implementation in TensorFlow, one can refer to [8].

Until now, we modeled the aleotoric uncertainty in a AI/ML model as a probabilistic layer at the output and a custom loss function as NLL, the next part is to model the epistemic uncertainty caused by the model itself. To include this epistemic uncertainty, the weights associated with each layer will now be considered as a random variable with a given probability distribution rather than a single deterministic value, which was the case before in a normal neural networks. The parameters of these weight distribution are then learnt by Bayes backpropagation algorithm, mention in detail in [9]. In short, the difference between this type of Bayesian neural network and a normal neural network can be summarized as,

- Classic neural networks: the weights are, $\theta_{i}=\hat{\theta}_{i}$
- Probabilistic neural network or Bayesian Neural networks: the weights are sampled from: $\theta_{i} \sim N\left(\hat{\mu}_{i}, \hat{\sigma}_{i}\right)$.
In the feed-forward pass, a sample from these weights is used to determine the output and then the Bayesian back prop is used to determine the distribution parameters. Since, the weights are assumed to be a random variable, the first step is to determine their distribution. From Baye's theorem, the distribution of weights given the training data $\mathbb{D}$ is given as,

$$
p(\theta \mid \mathbb{D})=\frac{p(\mathbb{D} \mid \theta) p(\theta)}{\int p\left(\mathbb{D} \mid \theta^{\prime}\right) p\left(\theta^{\prime}\right) d \theta^{\prime}}
$$

where $p(\theta)$ in the above equation is called the prior distribution, $p(\mathbb{D} \mid \theta)$ is the likelihood of observing data given weights, $p(\theta \mid \mathbb{D})$ is the posterior distribution and the denominator is the normalizing constant. In principle, the Bayesian learning works simply by,

- Assume a prior distribution for weights, $p(\theta)$.
- Using training data $\mathbb{D}$ to determine the likelihood $p(\mathbb{D} \mid \theta)$
- Finally determine the posterior density $p(\theta \mid \mathbb{D})$ using Bayes theorem.
This looks easier but the main challenge is in determining the normalizing constant as it involves solving or approximating a complicated solution to the integral. One of the popular method to approximate it is with the variational Bayes, which is a very popular technique in the AI/ML domain [10]. Variational Bayes approximates the posterior distribution with a secondary function, known as variational posterior which is of a known form. This approximation may lead to a posterior that may be very inaccurate. This however can be overcomed by tuning the function parameters so that it matches to the original posterior distribution as much as possible. Let $q(\theta \mid \phi)$ be the approximated posterior distribution (variational posterior) instead of the true posterior density, $p(\theta \mid \mathbb{D})$, parameterized by $\phi$. Thus, to approximate the variational posterior as close as possible to the original posterior distribution, the difference between them should be as minimum as possible [9], [11]. This difference between two distributions can be easily measured by Kullback-Leibler divergence (KLD). Therefore, the KLD between $q(\theta \mid \phi)$ and the true posterior $p(\theta \mid \mathbb{D})$ is given as,

$$
\begin{aligned}
& \operatorname{KLD}(q(\theta \mid \phi) \| p(\theta \mid \mathbb{D}))=\int q(\theta \mid \phi) \log \left(\frac{q(\theta \mid \phi)}{p(\theta \mid \mathbb{D})}\right) d \theta \\
& =\int q(\theta \mid \phi) \log \left(\frac{q(\theta \mid \phi) p(\mathbb{D})}{p(\mathbb{D} \mid \theta) p(\theta)}\right) d \theta \\
& =\int q(\theta \mid \phi) \log p(\mathbb{D}) d \theta+\int q(\theta \mid \phi) \log \left(\frac{q(\theta \mid \phi)}{p(\theta)}\right) d \theta \\
& -\int q(\theta \mid \phi) \log p(\mathbb{D} \mid \theta) d \theta
\end{aligned}
$$

On further expanding the terms in (5), the first term will reduce to, $\int q(\theta \mid \phi) \log p(\mathbb{D}) d \theta=\log p(\mathbb{D}) \int q(\theta \mid \phi) d \theta=\log p(\mathbb{D})$. The second term is $\operatorname{KLD}(q(\theta \mid \phi) \| p(\theta))$, and the last term is nothing but expectation of the NLL of $\log p(\mathbb{D} \mid \theta)$ under the variational posterior $q(\theta \mid \phi)$. Since the first term is constant, we can write (5) as a loss function- $L(q \mid \mathbb{D})$ as,

$$
L(q \mid \mathbb{D})=\operatorname{KLD}(q(\theta \mid \phi) \| p(\theta))-\mathbb{E}_{q(\theta \mid \phi)}(\log p(\mathbb{D} \mid \theta))
$$

Taking negative of the above equation (6), will represent the lower bound on the log-evidence, and is known as the evidence lower bound (ELBO) loss as $\operatorname{KLD}(q(\theta \mid \phi) \| p(\theta))$ is always positive. Hence, the minimization of (6) will be a maximization of ELBO loss.

Maximizing this ELBO loss represents a trade-off between the KLD term and expected log-likelihood term. On one hand, the divergence between the variational posterior $(q(\theta \mid \phi))$ and actual posterior $(p(\theta))$ should be as small as possible but on the other hand, the variational posterior parameters should maximize the expectation of the log-likelihood $\log p(\mathbb{D} \mid \theta)$, implies that the model will assign a high likelihood to the data. Therefore, with this new ELBO loss, and weights modeled as a random variable with a distribution, the epistemic uncertainty can be modeled as described in Algorithm 2.

Algorithm 2 method to measure Epistemic uncertainty
Input: $\mathbb{D}\left(X_{i}, y_{i}\right)$, define optimizer as rmsProp and set its learning rate, set num_epochs for training.
Output: $\hat{y}_{i}$
Initialization
a) Assign a prior distribution with density $p(\theta)$ to weights $\theta$. This can be as simple as a normal Gaussian distribution.
b) Assign the weights to variational posterior with density $q(\theta \mid \phi)$ with some trainable parameter $\phi$.
2: for $e p o c h=1$ to num_epochs do
i) Calculate loss and gradients using NLL part from (6) and optimizer
ii) learn $\phi$ using KLD from (6) to approximate the variational posterior as close to original posterior.
iii) Apply gradients and learn weight parameters
iv) Monitor loss and accuracy
4: end for
Determine class probabilities or mean/variance.

![img-0.jpeg](img-0.jpeg)
(a) Normal ML model with deterministic weights $\theta_{i j}$, where $i, j$ depend on the layer to layer connection.

![img-1.jpeg](img-1.jpeg)
(b) Probabilistic neural network where weights and output layer are represented as a distribution.

Fig. 1: A two layer ML model showing the difference between a normal ML model and a probabilistic ML model.

Now, to combine both aleotoric and epistemic uncertainty in a AI/ML model, we can just combine these layers with weights as random variable with a probabilistic output layer as described before. This type of a model as compared to a conventional AI/ML model can be easily visualized as shown in Fig. 1. In the next section, we will look into a real example of modeling uncertainty in a WiFI CSI sensing application.

## III. WiFi CSI Sensing

The CSI from a WiFi device provides amplitude and phase information that can be used in applications such as motion/nomotion detection. Since WiFi is ubiquitous, deploying any CSI application is easy and very cost effective. In this section, we will look at one of the application of WiFi sensing for motion/no-motion detection. Mathematically, the measured baseband to baseband CSI in a WiFi is given as [12], [13],

$$
\begin{aligned}
& H_{i, j, k}=\sum_{n=1}^{N} a_{n} \Phi_{i, j} e^{-j 2 \pi f_{k}\left[d_{i, j, n} / c+\tau_{i}+\nabla_{t}+\eta \nabla_{f}\right]} \\
& H_{i, j, k} \in \mathbb{C}^{N_{T x} \times N_{R x} \times N_{s c} \times N_{s a m p l e s}}
\end{aligned}
$$

where, $a_{n}$ is the amplitude of the received signal, $\Phi_{i, j}$ is the beamforming matrix, $f_{k}$ is the $k^{t h}$ carrier frequency, $\tau_{i}$ is the time delay from Cyclic Shift Diversity (CSD) of the $i^{t h}$ transmit antenna, $\nabla_{t}$ is the Sampling Time Offset (STO), $\eta$ is the Sampling Frequency Offset, and $\nabla_{f}=f_{k}^{\prime} / f_{k}-1$. Therefore, the WiFi CSI data represents a 4D (dimensional) complex vector as shown in Eq. (7) with $\left(N_{T x}, N_{R x}, N_{s c}, N_{\text {samples }}\right)$ as its dimensions, where $N_{T x}$ is number of transmit antennas, $N_{R x}$ is the number of received antennas, $N_{s c}$ is the number of subcarriers, and $N_{\text {samples }}$ are the number of collected time samples. The CSI sampling rate in our experiment is fixed at 100 Hz , which is enough to capture any human motion signatures [14]. Also, we will utilize CSI amplitude to generate input features for our probabilistic AI/ML model ${ }^{2}$.

The intuition behind using CSI amplitude for motion/nomotion detection is that the human motion causes amplitude

[^0]fluctuations, which can discriminate motion and no-motion case [12], [15]. In our experiment, we will consider 4 different homes, where we collect CSI data and label it as motion and no-motion depending on the subject is moving or not-moving there. To observe the uncertainty in the predictions of our model, we would use permutations of 3 homes for training and keep one home for testing. Intuitively, this will represent an interesting scenario where the test data will behave mostly as a out of distribution data that the model will not have learned during training. Since the data is limited, we have to rely on generating features from the CSI data.

To begin with, we will pre-process the raw CSI data collected from these 4 homes so as to remove outliers and noise in the CSI data. These steps will also mitigate some of the hardware ailments to some extent that may affect CSI data quality adversely [12], [15]. The brief details of each step are as follows,

- Hampel filtering: Hampel filter removes and replaces any outlier points or jitter in the CSI data by the median value of the hampel filter window.
- Subcarrier selection: Choosing the right subcarriers is very important as different subcarriers are affected differently in an environment and a particular set of subcarriers can't be generalized for every home [16]. We rank subcarriers in terms of having high mean power and variance and choose top 5 subcarriers from that ranking list. The idea is that motion causes the amplitude fluctuations with a high mean power, while the noisy subcarrier will have high variance but not high mean power ${ }^{3}$.
- Standardize and mean of top 5 subcarriers: After selecting the top 5 subcarriers, random noise across subcarriers can be further reduced by taking the mean across these subcarriers. Apart from removing noise, it simplifies the output as it creates a single 1D time series.
- Feature engineering: Before feeding the pre-processed 1D time series data to ML algorithm, we will generate

[^1]
[^0]:    ${ }^{2}$ Phase information is also useful but is very sensitive to environment changes and can lead to lot of false-positive cases.

[^1]:    ${ }^{3}$ Since our main aim is to quantify uncertainty, any other subcarrier selection method can be used here. For simplicity, we will use the mean power and variance as a metric to choose subcarriers.

![img-2.jpeg](img-2.jpeg)

(a) An example from test Home-1, where the model is very confident about its prediction (less aleotoric and less epistemic uncertainty). The predicted and true label are both 'No-motion'.

![img-3.jpeg](img-3.jpeg)

(b) An example from test Home-3, where the model is very uncertain about its prediction (high aleotoric and high epistemic uncertainty). The prediction and true label are both 'Motion'.

Fig. 2: Aleotoric (different class probability) and Epistemic uncertainty in different homes.

7 high level features<sup>4</sup> - a combination of both temporal and spectral features. The temporal features chosen are sample entropy, skewness, and kurtosis while the selected spectral features are binned entropy, Fourier entropy, maximum Doppler and doppler spread.

Finally, after all these steps, we will end up with a 1D time series of shape, N_samples × 7 as our input and the output would be N_samples × 2, where the last dimension in it refers to the two classes of motion and no-motion. In the next section, we will discuss more on the model and corresponding results on uncertainty quantification in these 4 homes.

## IV. ML MODELING AND RESULTS

For our experiments, we will create a very simple two probabilistic model layers with the first layer having 4 nodes, and second one with 2 nodes. The output layer is modeled as a probabilistic layer to capture the aleotoric uncertainty. The prior distribution and trainable posterior distribution in the first layer are both set as a multivariate Normal distribution with activation set to rectified linear unit (relu). The second layer has 2 dense nodes with no activation, while the prior and posterior distribution of this layer is also set to a multivariate Normal distribution<sup>5</sup>. The final layer in this model is defined as a one hot categorical layer with 2 outputs each representing a distribution. Hence, the output will have four outputs representing means and standard deviations (4 outputs) for each class. The divergence function in both layers can be defined empirically. However, this may not be required if Normal distribution is assumed as prior and posterior distribution as it has a tractable analytical solution for the divergence.

The model is then trained on 3-homes for 200 epochs while testing on one left out home. The batch size is kept to 4, and optimizer used to train the model is RMSprop. This model

TABLE I: Test home results with accuracy and mean entropy for no-motion and motion class.


is implemented in TensorFlow with TensorFlow's probability module with layers such as DenseReparameterization and OneHotCategorical [8]. Figure 2 shows one example from two test homes-1 and -3, while being trained on the rest 3 homes. As one can observe, the model trained on homes-2, 3, and 4, is very certain on his prediction in that one example data from home-1, while the model trained on homes-1,2, and 4, is very uncertain in his prediction in that one example data from home-3. Although, one may observe that in both examples, the prediction match very well with the true label but with probabilistic modeling, the model was able to convey the most important information that is how much uncertain or confident the model was in its prediction for that example data.

To analyze the model's uncertainty across the full test set, we can use entropy of the distribution as a metric for uncertainty. The entropy is given as, H_i = − ∑_j=1^n_i p_i log2(p_i), where n_t is the number of samples of a class and i represents one of those samples. Thus, higher the entropy of a class, higher is the uncertainty. Table I presents the mean entropy for each class in all the test home cases, and Fig. 3 shows the Entropy for each class in case of test home-3. There are few important observations from these results,

- Although the accuracy for test home-1 is 80% but the mean entropy for motion class is very high as compared to the no-motion class. This implies that the model is very uncertain in its prediction on motion classes as compared to the no-motion class. Same can be inferred for test home-4.

<sup>4</sup>More features can be used for analysis but since our main aim was to determine uncertainty, we kept it to the 7 features.

<sup>5</sup>One can define any distribution but for simplicity and tractability, we kept it multivariate Normal distribution.

![img-4.jpeg](img-4.jpeg)

Fig. 3: Entropy measure for test home 3 for each class, where the model is trained on Home-1,2 and 4. This test home represents the highest uncertainty for both of its classes.

- Test home-2 and home-3 are having equal mean entropies across classes but the accuracy is lower in home-3, which means the model is performing really bad in terms of predictions for both the classes and is very uncertain in its predictions as compared to other homes especially for no-motion class.
- The best performance of the model is on test home-4 in the no-motion class.

Finally, with this probabilistic modeling example on a WiFi CSI data for uncertainty quantification, one can easily understand the importance of such models in wireless sensing domain, where data is highly dependent on the measurement environment and prone to errors. This ability to convey the confidence or uncertainty with a model's prediction is therefore very handy. On the contrary, there are some disadvantages to this probabilistic ML modeling: 1) training of probabilistic machine learning models is computationally expensive and takes a lot of time to converge, 2) A reliable prior distribution and the assumed variational posterior is a pre-requisite as can be seen from previous sections, and finally 3) the implementation can be challenging if there are memory or computation constraints.

## V. CONCLUSION AND FUTURE WORK

In this paper, we describe the need for uncertainty quantification of AI/ML models and laid the foundations for modeling the two types of uncertainty (aleotoric and epistemic uncertainty) in a AI/ML model. We also describe the different cost functions and Bayesian technique used in the quantification of aleotoric and epistemic uncertainty. As an example, we looked into a wireless sensing case of motion/no-motion detection with WiFi CSI and quantified uncertainty for each test home where the model was trained on other homes. Furthermore, to quantify uncertainty on the whole test set, we used Entropy as a broader metric. The results highlight the need for uncertainty quantification, where we observed that even though in test Home-1, the prediction accuracy was high but the predictions for motion class as compared to no-motion class were very uncertain. We also saw the case of test Home-3 having high epistemic as well as high aleotoric uncertainty with less prediction accuracy. These results are valuable as it forces one to rethink on the data collection strategy or feature engineering to handle aleotoric uncertainty or the need to collect more data or iterate over different model architecture to overcome epistemic uncertainty. In future, we would explore different methods to overcome the aleotoric and epistemic uncertainty in wireless sensing applications.

## ACKNOWLEDGMENT

The authors would like to thank Morris Hsu, Maxim Arap, Ravi Ichapurapu, Swamy Inti, and Abhishek Sanaka for their great support and help during this work.
