# Inferring Distributions Over Depth from a Single Image

Gengshan Yang^{1}, Peiyun Hu^{1}, Deva Ramanan^{1,2}
[^{1}Robotics Institute, Carnegie Mellon University
^{2}Argo AI
*https://github.com/gengshan-y/monodepth-uncertainty
]

###### Abstract

When building a geometric scene understanding system for autonomous vehicles, it is crucial to know when the system might fail. Most contemporary approaches cast the problem as depth regression, whose output is a depth value for each pixel. Such approaches cannot diagnose when failures might occur. One attractive alternative is a deep Bayesian network, which captures uncertainty in both model parameters and ambiguous sensor measurements. However, estimating uncertainties is often slow and the distributions are often limited to be uni-modal. In this paper, we recast the continuous problem of depth regression as discrete binary classification, whose output is an un-normalized distribution over possible depths for each pixel. Such output allows one to reliably and efficiently capture multi-modal depth distributions in ambiguous cases, such as depth discontinuities and reflective surfaces. Results on standard benchmarks show that our method produces accurate depth predictions and significantly better uncertainty estimations than prior art while running near real-time. Finally, by making use of uncertainties of the predicted distribution, we significantly reduce streak-like artifacts and improves accuracy as well as memory efficiency in 3D map reconstruction. Video and code can be found on the project website${ }^{\star}$.

## I. INTRODUCTION

Most contemporary architectures for geometric scene understanding cast the problem as one of regression - given an image, infer a depth for each pixel. However, in safetycritical systems such as autonomous vehicles, such perceptual inferences will be used to make critical decisions and motion plans with considerable implications for safety. For example, what if the estimated depth of an obstacle on the road is incorrect? Here, it is crucial to build recognition systems that (1) allow for safety-critical graceful-degradation in functionality, rather than catastrophic failures; (2) are selfaware enough to diagnose when such failures occur; and (3) extract enough information to take an appropriate action, e.g. a slow-down, pull-over, or alerting of a manual operator. Such requirements are explicitly laid out in Automotive Safety Integrity Level (ASIL) standards which self-driving vehicles will be required to satisfy [18].

Such safety standards represent significant challenges for data-driven machine vision algorithms, which are unlikely to provide formal guarantees of performance [27]. One attractive solution is that of probabilistic modeling, where uncertainty estimates are propagated throughout a model. In the contemporary world of deep learning, deep Bayesian methods [6], [17] provide uncertainty estimates over model parameters (e.g., observing a scene that looks different than experience) and uncertainty estimates arising from ambiguous data (e.g., a sensor failure). We apply such approaches

![img-0.jpeg](img-0.jpeg)

Fig. 1: Given an input image, traditional methods predict a single depth value for each pixel. In this paper, we describe an approach that predicts a per-pixel multi-modal distribution over depth. In the example above, we zoom in onto depth predictions along the dashed green line. Inside the input image, we highlight a segment filled with depth continuities marked with a yellow double-head arrow, where pixels could come from the car in the front, the car behind, or even the building in the back. In the output at the bottom, we mark ground truth depth with blue and depth with higher probabilities with red. While traditional methods incorrectly yield the mean of different modes, our approach successfully captures the multi-modal nature.
to the problem of depth estimation from a single camera. Our particular approach differs from prior work in two notable aspects. First, prior methods often require Monte Carlo sampling to compute uncertainty estimates [6], which can be slow for real-time safety-critical applications. Second, while certainty estimates provide some degree of selfawareness, they are limited to unimodal estimates of scene structure, implicitly producing a Gaussian estimate of depth represented by a regressed mean and regressed variance (or confidence) [17]. Instead, we develop representations that report back multimodal distributions that allow us to ask more nuanced questions (e.g., "what is the second possible depth of a pixel?", "how many modes exist in the distribution?"), as shown in Fig. 1 and Fig. 3.

From a practical perspective, one may ask why bother estimating depth from a single camera when special-purpose sensors for depth estimation exist (such as LIDAR or multiview camera rigs)? Common arguments include cost, payload and power consumption of robots [29], but we motivate this problem from a safety perspective. One crucial method for ensuring ASIL certification is redundancy, and so estimates of scene geometry that are independently produced from various sensors (e.g., independently from LIDAR and independently from cameras) and that agree provide additional

![img-1.jpeg](img-1.jpeg)

Fig. 2: From left to right, we show 3D maps built with LiDAR measurements (left), vanilla monocular depth predictions (middle), and *most certain* monocular depth predictions (right). Color encodes normalized heights. By thresholding depth predictions with uncertainty, we can remove streak-like artifacts (red dotted circles) and reduce memory usage by a quarter. To generate these maps, we feed depth measurements/predictions into OctoMap [14] and use odometry measurements as provided. LiDAR and monocular images come from the KITTI odometry sequence-00, which is not included in training.

![img-2.jpeg](img-2.jpeg)

Fig. 3: Visualization of multi-modal depth predictions on the glass table, where the surface is transparent, making its depth fundamentally ambiguous. Instead of regressing a single depth value or predicting a unimodal distribution, our method yields a multi-modal distribution over depth and successfully captures different modes (the table surface and the wall behind the table).

Fault tolerance. In Fig. 4, we illustrate a situation in which monocular depth estimation complements range sensing.

Our overall approach to probabilistic reasoning is to recast the continuous problem of depth regression (given an image patch *x*, regress a depth value *y* ∈ *R*) as a discrete problem of selecting one out of many possible discretized depths *y* ∈ {1, 2, ... *K*}. Previous work [3] has already demonstrated that discretization can improve the *accuracy* of the underlying depth regression task, but we show that discretization is even more useful for producing simple and efficient (and possibility multimodal) *uncertainty* estimates of depth. Intuitively, K-way classifiers are often trained with softmax loss functions, and so naturally report a distribution over *K* possible discrete depths. Importantly, we find that such distributions can be further improved by recasting the multiclass formulation as a binary *multilabel* task *y* ∈ {0, 1}<sup>*K*</sup> - essentially, train *K* independent binary classifiers that classify patches at particular discrete depths. It is straightforward to show that the binary multilabel formulation can be seen as a relaxation of the multiclass problem that removes a linear constraint. Removing this constraint creates a more challenging learning problem that appears to be better regularized in terms of uncertainty reports. At test-time, we use the *K* logits as an unnormalized distribution over possible depths, though they can easily be normalized post-hoc (to compute summary statistics such as the expected depth).

Our main contributions are as follows:

- We formulate the problem of monocular depth estimation in a probabilistic framework, which gives us confidence intervals of depth instead of point estimations.
- We recast the problem of depth regression as *multi-label* depth classification, which yields *reliable*, *multi-modal* distributions over depth.
- Our method produces accurate depth and significantly better uncertainty estimation over prior art on KITTI and NYU-depth while running *near real-time*.
- Our predicted distribution over depths improves monocular 3D map reconstruction, reducing streak-like artifacts and improving accuracy as well as memory efficiency.

## II. RELATED WORK

**Single Image Depth Estimation:** Early works [13], [26] popularize the problem of inferring scene depth maps from a single image, making use of handcrafted features. Eigen et al. [4] take a data-driven approach to learn features in a coarse-to-fine network that refines global structure with local predictions. Some recent work substantially improves the performance of single image depth estimation using better deep neural network architectures [20], [23], [28].

**Depth Estimation as Classification:** Closely related to our work, Cao et al. [3] formulates depth estimation as a multi-class classification problem and use soft targets to train the model. However, they make inference by choosing the most likely depth class, which does not take full advantage of the depth distribution, while we explore richer inference methods based on the predicted depth distributions. More importantly, the standard multi-class classification approach tends to make confident errors and does not yield reliable uncertainty estimations. Instead, we learn the classification model as *K* independent binary classifiers, which regularizes the model and gives us much better uncertainty estimation as well as noticeable performance improvement on standard benchmarks. Fu et al. [5] formulate depth estimation as ordinal regression, aiming to predict a CDF over depth. However, they do not ensure the predicted CDF to be

![img-3.jpeg](img-3.jpeg)

Fig. 4: A situation in which monocular depth estimation complements range sensing. In the top row, from left to right, we show a monocular image, a binary mask, and an entropy map. The binary mask shows where LiDAR readings are available and the entropy map summarizes the uncertainty of each pixel's predicted distribution. Note that a large chunk of the truck body with black paint has no LiDAR returns since LiDAR sensors are less reliable with less-reflective materials. Our monocular depth estimator successfully predicts high entropy in the area with black paint. In the bottom row, we show depth predictions with uncertain pixels removed. From left to right, we gradually increase the confidence threshold. The rightmost one plots 30% pixels with the most confident depth predictions, in which we see most predictions on the truck body are removed. If a perception system solely relies on LiDAR measurements, it will perceive plenty of free space on the left side, which might lead to catastrophic decisions. If a perception system is designed with redundancy, it would trust LiDAR measurements less at pixels where the monocular estimator predicts uncertainties.

monotonically non-decreasing. This makes it ungrounded to apply probabilistic reasoning for uncertainty estimation. In contrast, we formulate depth estimation as a discrete classification problem, aiming to predict a valid depth PDF.

**Uncertainty in Depth Estimation:** Kendall et al. [17] introduce two kinds of uncertainties: epistemic uncertainty (over model parameters) and aleatoric uncertainty (over output distributions). They show that epistemic uncertainty is data-dependent while aleatoric uncertainty is not. They model aleatoric uncertainty by fitting the variance of Gaussian distributions (also proposed in recent work on lightweight probabilistic extensions for deep networks [7]). However, this might lead to unstable training and suboptimal performance. More importantly, this ignored the fact that depth distributions are multi-modal in many cases (for example at depth discontinuities and reflective surfaces). They capture epistemic uncertainty by Bayesian neural networks [6]. However, it requires expensive Monte Carlo sampling to obtain depth predictions and uncertainty estimations. Instead, we focus on modeling the multi-modal distributions over depth, which gives us more reliable uncertainty metrics without the additional computational overhead.

**Multiple Hypotheses Learning (MHL):** Prior works [11], [21] formulate the problem of learning to predict a set of plausible hypotheses as multiple-choice learning. They train an ensemble of models to produce multiple possibilities and define an oracle to pick up the best hypothesis. Rupprecht et al. [25] uses a shared architecture to produce multiple hypotheses and train the network by assigning each sample to the closest hypothesis. Different from these approaches, we train a single network to produce a multi-modal distribution, from which we can obtain multiple predictions without directly optimizing an oracle loss in training.

## III. METHOD

We solve the problem of inferring continuous depth through discrete classification. To illustrate the method, we first introduce how we discretize continuous depth into discrete categories. Then we show the formulation of depth estimation as a multi-class classification task (mutual exclusive) and a multi-label (binary) classification task (not mutually exclusive). Then we discuss the output of our model, i.e. a probabilistic categorical distribution over discrete depths, and how we will evaluate the output, including evaluating as a standard depth estimation task and as a depth estimation with uncertainty.

**Discretization:** We discretize continuous depth values in the log space. Given a continuous range of depth [a,b), we discretize it into K intervals, i.e. [d1,d2], [d2,d3], ..., [dK,dK+1], with

$$d_k = \log a + \frac{k - 1}{K} (\log b - \log a), k \in \{1 \dots K\}.\tag{1}$$

This captures the perceptual difference in human visual systems, i.e., we care more about differences in depths of close objects than distant ones. Furthermore, due to sensor sampling effects, we tend to encounter more close points rather than far away ones. Working in log space partially alleviates this class imbalance problem.

**Multi-class Classification:** As a baseline method, we first show how we recast the continuous regression as a multi-class classification problem. A discrete distribution over depth y can be parameterized by a categorical distribution Cat(K, µ). We learn to predict the probability µ<sup>k</sup> = p(y = k) of each depth label by minimizing the negative log likelihood. Since we use the output of a softmax layer as the predicted probability, we will also refer to this variant as "Softmax" in the following text. Given a ground truth label y*, image feature x, and the model parameters w, the loss function can be written as,

$$L(\mu|y*) = -\sum_{k=1}^{K} \mathbf{1}(k = y*) \log \mu_k(\mathbf{x}; \mathbf{w}).\tag{2}$$

Here the distribution µ(x;w) is predicted from a K-way multi-class classifier.

![img-4.jpeg](img-4.jpeg)

Fig. 5: Our network architecture consists of an encoder, a spatial pyramid pooling module, and a decoder. Our encoder is a ResNet-50 truncated before global pooling. Spatial pyramid pooling takes ResNet feature then extracts global and semi-global feature through multiscale pooling. The decoder processes pooled feature to predict a un-normalized score map for each discrete depth class a1,...,aK. During training, each un-normalized score map is pushed into a per-pixel soft-labeled binary cross entropy loss; at test time, we perform per-pixel normalization using softmax across all depth classes to ensure a valid per-pixel distribution over depth, from which we can make the final prediction of depth and uncertainty. Original-resolution images are used as input, and the predictions are bilinearly up-sampled to the same resolution as ground-truth.

Equation (2) gives us the cross-entropy between an one-hot label vector $$k(k=y^*)$$ and the predicted distribution $$\mu(\mathbf{x}; \mathbf{w})$$. To incorporate the ordinal nature of the depth labels, i.e., penalize predictions closer to the ground truth less than predictions further away, we replace the one-hot target vector $$k(k=y^*)$$ with a discretized Gaussian centered around the ground truth, i.e.,

$$q(k; y^*) = \frac{1}{Z}e^{\frac{||k-y^*(|^2)}{-2\sigma^2}}, \tag{3}$$

where Z is the partition function.

**Binary Classification:** To alleviate competition between depth classes, we further model continuous depth as a collection of K independent Bernoulli random variables yk ~ B(1, µk), where µk encodes the probability of falling into the kth depth interval. We also refer to this variant as multilabel in the paper. The loss function is written as,

$$L(\mu|y^*) = -\sum_{k=1}^{K} [\tilde{q}(k; y^*) \log \mu_k(\mathbf{x}; \mathbf{w}) + (1 - \tilde{q}(k; y^*))(\log(1 - \mu_k(\mathbf{x}; \mathbf{w})))],$$

where $$\tilde{q}(k; y^*) = e^{\frac{||k-y^*(|^2)}{-2\sigma^2}}$$ is an unnormalized version of soft target distribution.

One can see this as a relaxation of the training objective from Eq.(2) that drops the constraint that $$\sum_k \mu_k = 1$$ [22]. The variance σ² is designed such that for all depth classes within 25% difference to ground truth, their label is greater than 0.5. In test time, we push the pre-logit scores of each binary classifier through a softmax and obtain a distribution over discrete depth, as shown in Fig. 5.

**Predicting Depth from a Distribution:** After obtaining the distribution over depth, Cao et al. [3] report the most confident depth class, ignoring the multi-modal nature of the predicted distribution. Different from their approach, we report the expected depth based on the predicted distribution as $$\mathbb{E}[y] = \sum_k \mu_k d_k$$, which takes into account the whole distribution and yields better depth estimations.

**Uncertainty and Multiple Hypotheses:** We now describe various statistics that can be computed from our multimodal distribution, motivated by autonomous robotic perception. Because the perception module of robots needs to be self-aware enough to report potential failures to the downstream planner or online-mapping module when faced with ambiguous scenes, the first statistic is uncertainty, as computed with Shannon entropy:

$$H(y) = -\sum_k \mu_k \log \mu_k. \tag{5}$$

Secondly, even if the most-likely (or expected) depth of a particular pixel is far away, a robotic motion planner may wish to decrease speed if there is a non-negligible probability that its depth is in the near-field (due to say, a translucent obstacle). As such, our network can directly output multiple depth modes to downstream planners.

**Evaluation:** Evaluating the above functionality on a robotic platform is difficult. Instead, to evaluate the quality of uncertainty estimation, we make use of the area under ROC curve (AUC), which is widely used in stereo vision and optical flow [2], [15]. To assess the accuracy of the multihypotheses output, we follow past work on MHL [11], [21] and use an "oracle" evaluation protocol where an algorithm is allowed to report back multiple depth predictions, and the best one is chosen to compute the accuracy [11]. We also report standard metrics [4] on depth estimation benchmarks.

**Implementation** We follow the architecture of Kuznietsov et al. [19] as shown in Fig. 5. We further add a spatial pyramid pooling module [12] to extract global and semi-global features from the scene. We experimented with different numbers of bins on KITTI. With 32, 64, 96, 128 bins, our method achieves an absolute relative error (ARE) of 9.34%, 8.61%, 8.60%, 8.59%. As improvement becomes marginal, we pick 64 as the number of bins and

![img-5.jpeg](img-5.jpeg)

Fig. 6: Soft target distributions for binary classification in log scale (left) and linear scale (right). We plot the soft target centering on the {11, 17, 23, 29, 35, 41, 47, 53, 59}th depth interval.

![img-6.jpeg](img-6.jpeg)

Fig. 7: How well does the predicted uncertainty correlate with the actual depth estimation performance? We first sort all predictions in ascending order of uncertainty. Then we gradually include more predictions for evaluation by increasing the uncertainty threshold (including more uncertain predictions in the evaluation). The X-axis represents the percentage of pixels we include and Y-axis represents the ARE on the selected pixels. Notice uncertainties estimated by the model trained with multi-class classification loss ("Softmax" [3]) are not well correlated with error, especially for the most confident pixels. On the contrary, the error increases monotonically as confidence drops for our proposed approach ("Binary"). At 80%, our method also achieves a lower error rate (5.4% vs. 5.6%).

used it for all experiments in this paper. Fig. 6 shows the unnormalized soft-target distribution we use when training binary classifiers.

## IV. EXPERIMENTS

We first introduce our experimental setup, including dataset and training details. We then compare to prior estimation methods that reason about uncertainties. Finally, we compare our method with the state-of-the-art on the standard depth estimation task, as well as using multi-hypotheses evaluation [25].

**Setup:** We test our method on the standard depth estimation benchmarks, including KITTI [8] for outdoor scenes (1-80m) and NYU-v2 [4] for indoor scenes (0.5-10m). On KITTI, we follow Eigen's split [4] for training and testing. On NYU-v2, we sample 13k images following [20] for training and test on the official test split.

**Training:** We first initialize the weights of our ResNet-50 backbone with the ImageNet pre-trained ones. To augment training data, we apply random gamma, brightness, and color shift, as in [10]. We fine-tune the weights with an Adam optimizer with an initial learning rate of 0.0001 and decrease the learning rate with a factor of 0.1 after 45 epochs. We train our KITTI model for a total of 60 epochs and our NYU-v2 model for a total of 160 epochs. Our experiments are run on a machine with GeForce GTX Titan X GPU using Tensorflow.

![img-7.jpeg](img-7.jpeg)

Fig. 8: Compared to predictive Gaussian [17] ("Gaussian"), our method ("Binary") yields lower error rate when more than 50% pixels are kept for KITTI, and more than 15% pixels for NYU. By applying Monte Carlo dropout, both predictive Gaussian ("Gaussiandropout") and our approach ("Binary-dropout") see a significant improvement on NYU. While on KITTI, the performance get strictly worse for predictive Gaussian.

### A. Depth Estimation with Uncertainty

**Baselines:** Considering most prior art do not reason about uncertainty, we compare to predictive Gaussian and predictive Gaussian with Monte Carlo dropout (Gaussiandropout) [7], [17] in terms of depth estimation with uncertainty, as shown in Tab. I. For a fair comparison, we re-implement and train predictive Gaussian and Gaussiandropout on KITTI and NYU depth v2. We make sure the re-implemented version has an architecture that is as close as possible to ours. For predictive Gaussian, we use the same backbone architecture but with a different prediction head, which predicts the mean and variance of a Gaussian distribution over depth in log space. To train predictive Gaussian, we minimize the per-batch negative log-likelihood based on the predicted mean and variance. For Gaussiandropout, we use the same backbone architecture and prediction head except we perform dropout with a probability of 0.5 after several convolutional layers, as in Kendall et al. [16]. During inference, we draw 32 samples to make predictions and estimate uncertainty. Following the same idea, we apply Monte Carlo dropout to our binary model, referred to as Binary-dropout.

Following Hu et al. [15], we plot ROC curves to evaluate our depth estimation with uncertainty, as shown in Fig. 7 and Fig. 8. Such curves demonstrate how well the predicted uncertainty correlates with the actual depth estimation performance. A point (*x*, *y*) on the curve indicates a performance of *y* on the least uncertain *x* (%) predictions over all pixels in the test set. Perfect uncertainty estimation, from the perspective of the ROC curve, should rank predictions as if they are ranked by the actual error. As a reference, we include curves with such oracle w.r.t. a specific error metric (absolute relative error or ARE). Below, we first compare two variants of our model (binary classification and multiclass classification). Then we will compare our model to prior art that predicts uncertainty (predictive Gaussian and Gaussiandropout). For each sub-metric under AUC, we follow the definition in Eigen et al. [4].

**Binary classification vs Multiclass classification:** In Fig. 7, we compare the model trained with binary classification loss ("Binary") to the model trained with multi-class


TABLE I: Quantitative evaluation for uncertainty estimation on KITTI (K) and NYU-v2 (N). The best results among methods without Monte Carlo dropout are made bold, while the best considering Monte Carlo dropout are underlined. On both datasets, we compare our method trained with the binary loss ("Binary") and the multiclass loss ("Softmax") to predictive Gaussian [17] ("Gaussian"). The quantitative results are consistent with Fig. 7 and Fig. 8. In terms of AUC on ARE and $1-\delta_{1}$ (the lower the better), our binary loss consistently outperforms predictive Gaussian on both KITTI and NYU-v2. Importantly, when combined with Monte Carlo dropout, our binary model ("Binary-dropout") further reduces the AUC on NYUv2. (17] (K) and NYU-v2 (N). The best results are in the case of a function of $M$ and $M$ and the best prediction for evaluation. Please see Fig. 9 for analysis of the results.

## V. Building Maps with Uncertainty

In this section, we demonstrate one application of geometric uncertainty estimation: robust map reconstruction. Though maps are often constructed in an offline stage, online mapping can be an integral part of autonomous navigation in unknown/changing environments [24].

In practice, is it notoriously difficult to build 3D maps from raw depth predictions because they tend to contain "streak-like artifacts" [1], which not only affect the quality of the map but also increase the memory usage (because they often result in larger occupied volumes). Empirically, we find that such artifacts often happen where ground truth


TABLE II: Performance on KITTI (K) Eigen's split and NYU-V2 depth (N) dataset. The best results over the light-weight setup are bolded, while the best results overall are underlined. On KITTI, our method outperforms the state-of-the-art Fu et al. [5] under the same setup. With its original setup (a heavy-weight backbone and test-time ensemble), [5] runs nearly 17x times slower ( 1250 ms vs 75 ms ). On NYU-v2, our method outperforms Kendall et al. [17] with the same backbone network. With its original setup, Kendall et al. [17] runs 144x slower. Our method further improves when training with dropout and testing with MC sampling [16], referred to as Binary-dropout.


TABLE III: Accuracy and memory usage of online mapping. LiDAR-FOV indicates the map built using LiDAR points in the left camera field of view, which is the upper-bound of our methods. The map built with top $80 \%$ most confident estimations of our model (Ours-binary-80\%) significantly reduces the memory usage and also improves the mapping accuracy.
depth is inherently ambiguous and follows a multi-modal distribution, e.g. depth discontinuities and reflective surfaces. Since our depth estimator is designed to predict multi-modal distributions over depth, we use it to improve the accuracy of map reconstruction. By simply thresholding the uncertainty of each pixel's predicted distributions, we can significantly reduce streak artifacts and memory usage, as shown in Fig. 2.

We evaluate the performance of map reconstruction with and without uncertainty on KITTI odometry sequence-00 [9], which is not included in the training set. Specifically, we run our monocular depth estimator on left RGB images, and feed the output depth maps together with ground-truth odometry as the input of Octomap [14]. The accuracy is measured as the percentage of correctly mapped map cells, where a cell counts as correctly mapped if it has the same state (free or occupied) as the LiDAR map (ground-truth). As shown in Tab. III, applying a simple uncertainty-based ranking and selection improves the accuracy of monocular maps by $1.8 \%$ and reduces the memory usage by $25 \%$.

## CONCLUSION

Robotic applications of perception present new challenges for safety-critical, fault-tolerant operation. Inspired by past approaches that advocate a probabilistic Bayesian perspective, we demonstrate a simple but effective strategy of discretization (with the appropriate quantization, smoothing, and training scheme) as a mechanism for generating detailed predictions that support such safety-critical operations.

## APPENDIX

## A. Ablation study

To reveal the contribution of each design choice to the accuracy of the standard depth estimation task, we perform an extensive ablation study as shown in Tab. V.

Classification vs Regression: We first compare $L_{2}$ regression loss to classification losses (Binary and Multiclass). We find that classification loss always outperforms $L_{2}$ regression method in terms of absolute relative error and $\delta_{1}$. However, $L_{2}$ regression achieves competitive RMSE, likely because it directly minimizes squared error. We also implement Berhu [20] regression loss, and it is still easily out-performed by classification-based methods.

Multiclass vs Binary classification Training with binary classification loss gets similar performance compared to multiclass classification loss on KITTI. However, it yields significantly better results on NYU. Since test images in NYU differ more from the training images than KITTI, we posit that binary classification loss gives better generalization ability compared to multiclass classification loss.

Effect of Monte Carlo dropout On KITTI, Monte Carlo dropout makes prediction performance worse for both binary classification method and predictive Gaussian. However on NYU, it improves results for both methods. This is possible because NYU contains more diverse scenes, where dropout helps prevent overfitting. While on KITTI, training and testing data are highly correlated. Therefore, regularizing the model by dropout does not help.

Expectation vs Most-likely class inference On KITTI, we find that expectation yields better results for all metrics except for $\delta_{1}$. While for NYU, expectation always outperforms (or on par with) most-likely class. This indicates that expectation is a better way of making a prediction from a depth distribution, since it makes use of the whole distribution.

Soft targets vs One-hot targets Comparing the results of training with soft-target distribution vs one-hot label, we find that soft-target always performs better. We posit that by training with soft targets, our model benefits from sample sharing, and thus performs better than using one-hot labels.

TABLE IV: Results of using a mixed KITTI and NYU-v2 dataset for training. The model is trained with binary classification loss and predicts the most-likely class at test time.


## B. Training on mixed KITTI and NYU-v2

To obtain a robust model that works for both indoor and outdoor scenes, we train a single model using KITTI and NYU-v2. To precisely capture the full depth range in both datasets, we adjust the depth range to 0.5 m to 80 m and the number of depth intervals to 100 . At training time, we randomly crop the data to $384 \times 640$ and average loss over the image before averaging over the whole batch. As shown in Tab. IV, when trained jointly, the performance of our model is not severely affected on both datasets.

Acknowledgements This work was supported by the CMU Argo AI Center for Autonomous Vehicle Research.
