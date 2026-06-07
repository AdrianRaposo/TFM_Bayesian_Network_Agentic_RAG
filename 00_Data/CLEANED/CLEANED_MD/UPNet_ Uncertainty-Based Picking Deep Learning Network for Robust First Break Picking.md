# UPNet: Uncertainty-based Picking Deep Learning Network for Robust First Break Picking 

Hongtao Wang, Jiangshe Zhang, Xiaoli Wei, Li Long, Chunxia Zhang


#### Abstract

In seismic exploration, first break (FB) picking is a crucial aspect in the determination of subsurface velocity models, significantly influencing the placement of wells. Many deep neural networks (DNNs)-based automatic picking methods have been proposed to accelerate this processing. Significantly, the segmentation-based DNN methods provide a segmentation map and then estimate FB from the map using a picking threshold. However, the uncertainty of the results picked by DNNs still needs to be analyzed. Thus, the automatic picking methods applied in field datasets can not ensure robustness, especially in the case of a low signal-to-noise ratio (SNR). In this paper, we introduce uncertainty quantification into the FB picking task and propose a novel uncertainty-based picking deep learning network called UPNet. UPNet not only estimates the uncertainty of network output but also can filter the pickings with low confidence. Many experiments evaluate that UPNet exhibits higher accuracy and robustness than the deterministic DNNbased model, achieving State-of-the-Art (SOTA) performance in field surveys. In addition, we verify that the measurement uncertainty is meaningful, which can provide a reference for human decision-making.


Index Terms—First break picking, Uncertainty quantification, Bayesian deep learning.

## I. INTRODUCTION

DETECTING the first break (FB) of P-wave or S-wave in pre-stack seismic gather is a crucial problem in seismic data processing. Accurate FB picking can provide precise static correction results, significantly improving the performance of subsequent seismic data processing [1], e.g., velocity analysis, stratigraphic imaging, etc. The current inefficient manual FB picking cannot satisfy the requirement because of the increase in the density of seismic data acquisition. Thus, the automatic FB picking algorithm has become a fundamental problem in reducing the seismic processing period.

In the initial exploration of automatic picking methods, many techniques identify FB by analyzing its signal characteristics. These characteristics include energy ratio-based methods [2] [3] [4] [5], higher-order statistics-based methods [6] [7], etc. Concretely, taking the feature named the shortand long-time average ratio (STA/LTA) [2] [3] as an example, the local feature of a single trace is calculated by a sliding window. The time at which the STA/LTA value first exceeds the threshold (set in advance) is considered FB. Then, considering the correlation between multiple signals, the correlation

[^0]coefficient is proposed to identify FB [8] [9]. Later, the feature signal extraction method of multiple signals is proposed one after another [10] [11] [12] [13].

Different from the above traditional model-driven methods, the current rapid development of picking methods based on machine learning (ML) or deep learning (DL) is a kind of data-driven approach [14] [15] [16] [17]. Generally, these datadriven models must train on a few samples with manual labels before predicting FB. In general, current popular methods can be divided into three classes: clustering method-based methods, local image classification-based methods, and end-to-end segmentation-based methods. First, the clustering-based picking method generally transforms seismic signal data into other domains, then uses the clustering methods to split the clusters, and finally defines the boundary of two clusters as FB. Concretely, Xu et al. [18] proposed a multi-stage clustering-based method, which first determines the first-break time window, then utilizes an improved clustering method to obtain the initial FBs of every single trace, and finally considers comprehensively the picking results of the near traces to refine the pickings. Then, Gao et al. [19] considered the clustering methods based on a shot-gather (multiple signals level) to enhance the correlation of automatic pickings among the near traces. Currently, Lan et al. [20] proposed a more complex and robust automatic picking method based on fuzzy C means clustering (FCM) and Akaike information criterion (AIC) further to improve the accuracy and robustness of clustering-based methods. Second, the local image classification-based methods split the whole shot gather image into a few mini-patch and then utilize neural networks (NN) or machine learning classification methods to classify the minipatch sub-image into two classes, i.e., FB or non-FB. At a very early time, McCormack et al. [21] proposed using a fully connected network (FCN) to complete the binary classification task. Then, FCN was replaced by convolutional neural networks (CNN) for image classification to improve classification accuracy [22]. Different from classification for picking FB directly, Duan et al. [23] first obtain a preliminary picking result based on the traditional picking method and then utilize CNN to identify poor picks. Currently, Guo et al. [24] combined more feature information as the input of the classifier and proposed a new post-processing method to improve the stability of the picking results. Compared to NNbased methods, the classic machine learning-based methods outperform in a small sample size scenario, e.g., support vector machine (SVM) [25], support vector regression (SVR), and extreme gradient boosting (XGBoost) [26]. Third, end-to-end segmentation-based methods are currently the most


[^0]:    Corresponding authors: Jiangshe Zhang
    H.T. Wang, J.S. Zhang, X.L. Wei, L. Long, C.X. Zhang are with the School of Mathematics and Statistics, Xi'an Jiaotong University, Xi'an, Shaanxi, 710049, P.R.China.

    The research is supported by the National Key Research and Development Program of China under grant 2020AAA0105601, the National Natural Science Foundation of China under grant 61976174 and 61877049.

popular automatic picking methods since fully convolutional networks (FCN) [27] and U-Net [28] are widely used for pixellevel segmentation and have excellent segmentation accuracy. Concretely, FCN was applied to segment the position of FB in the image of a shot gather, and the techniques of semisupervised learning and transfer learning were conducted to learn a better high-level feature [29] [30] [31]. Then, U-Net, an excellent medical image segmentation tool, was utilized to solve the segmentation task of labeling FBs [14] [15] [16] [17]. Yuan et al. [32] further proposed post-processing to refine the U-Net-based picking results, where a recurrent neural network (RNN) regresses FBs for every trace. Moreover, the popular transformer has also been used for the segmentation task concerning picking FB [33].

Semantic segmentation-based methods are the most efficient and have been well-evaluated in practical applications. Unfortunately, DNNs are black-box models, and we cannot explain the specific role of each neural layer [34]. Therefore, controlling the physical significance of each layer output is impossible. However, the principle of the FB picking task is to put quality before quantity, i.e., the accuracy should be guaranteed even if the picking rate is reduced [1]. To solve the security problem of automatic picking, we introduce the concept of uncertainty quantification (UQ) into FB picking. UQ methods mainly measure two parts of uncertainty, epistemic uncertainty (model uncertainty) and aleatoric uncertainty (data uncertainty) [35]. In this paper, we focus on the epistemic uncertainty of neural networks, where the main task is modeling and solving the posterior distribution of the model weights. Specifically, the obtained posterior distribution can help us estimate the uncertainty of the FB picked by NN and then filter the outliers among the automatic pickings. With the proposed methods of Monte Carlo (MC) dropout [36], Bayes by Backprop (BBB) [37], and deep ensemble [38], the computational cost of uncertainty quantification is greatly reduced, and the generalization of the model is dramatically improved. Further, uncertainty quantification methods are extended to semantic segmentation [39], especially to the segmentation tasks of medical images [40] [41], remote sensing images [42], etc. However, no uncertainty quantification method fully applies to segmentation-based FB picking methods.

To analyze the uncertainty of the FB pickings of the DL-based method, we propose a novel uncertainty-based picking network named UPNet, which includes a Bayesian segmentation network (BSN), a multi-information regression network (MIRN), and an uncertainty-based decision method (UDM). Concretely, BSN estimates a posterior distribution of the FB picking map of a 2-dimension (2D) gather. MIRN infers the accurate FB time based on the segmentation map sampled from the above posterior distribution. Finally, UDM decides on the final FB picking based on the uncertainty of MIRN regression results.

The structure of this article is summarized as follows. Section II introduces preliminary knowledge about FB picking and uncertainty quantification. Section III describes the details of our proposed UPNet. Then, performance validation of the proposed method on four field datasets is shown in Section IV. Finally, Section V concludes this article.

## II. PRELIMINARY

### A. Problem Statement

FB picking is a problem of detecting the first changed point, which indicates a first arrival wave event in the seismic signal data. For instance, the red dash line (Fig. 1, left) labels the FB since there is the first pronounced trough. Generally, the source determines the FB mode (peak or trough). In a higher scale view, the FBs of the adjacent signals on a shot gather usually have a stronger correlation, as shown in the right subfigure of Fig. 1. Based on the spatial characteristics of FB mentioned above, we define the FB picking task as a statistical inference problem $P(\mathbf{t}|\mathbf{G})$, which infers the FB of a time series $\mathbf{t}$ based on the shot gather $\mathbf{G}$.

![img-0.jpeg](img-0.jpeg)

Fig. 1. A showcase of the FB picking task. The left subfigure shows the FB of a single trace. The right subfigure indicates a high correlation among the FBs of the adjacent traces. The red dotted box indicates the location of the single-channel signal in the left subfigure.

### B. Uncertainty quantification for FB Picking

We transform the picking model to a probability model to introduce the uncertainty of FB. In view of statistic, the inference of FB $P(\mathbf{t}|\mathbf{G})$ can be described as solving a maximum posterior estimation:

$$
\tilde{\mathbf{t}}=\arg \max_{\mathbf{t}}\{P(\mathbf{t} \mid \mathbf{G}, \mathcal{D})\}
$$

where $\mathbf{G}$ represents a shot gather, $\mathbf{t}$ represents the FB of each trace in the shot gather $\mathbf{G}$, and $\mathcal{D}$ represents the annotation knowledge of FB, i.e., the labeled dataset. In this paper, we only consider the model uncertainty, i.e., epistemic uncertainty, in the inference model (Eq. 1). Concretely, the model weights $\mathbf{w}$ are assumed to follow a posterior distribution $P(\mathbf{w} \mid \mathcal{D})$. Therefore, the posterior distribution can be expressed by a form of marginal average:

$$
P(\mathbf{t} \mid \mathbf{G}, \mathcal{D})=\int_{\mathbf{w}} P(\mathbf{t} \mid \mathbf{G}, \mathbf{w}) \cdot P(\mathbf{w} \mid \mathcal{D}) d \mathbf{w}
$$

where $P(\mathbf{t} \mid \mathbf{G}, \mathbf{w})$ is an inference model with weights $\mathbf{w}$.
However, the true posterior $P(\mathbf{w} \mid \mathcal{D})$ is intractable, and we have to utilize other techniques to approximate it, e.g.,

![img-1.jpeg](img-1.jpeg)

Fig. 2. The main flow chart of a new framework we propose to pick FB times robustly.

Variational inference (VI) [43], which minimizes the Kullback-Leibler (KL) divergence between the true posterior $P(w|D)$ and an approximation distribution $q(w)$:

$$KL\left[q(w) \|\mathbf{F}(w|D)\right] = \int q(w) \ln \frac{q(w)}{P(w|D)} dw,\qquad(3)$$

Then, we maximize the evidence low bound (ELBO) deduced by Eq. 3 to optimize the approximation distribution $q(w)$:

$$ELBO(q) = KL\left[q(w) \|\mathbf{F}(w, D)\right] - \ln P(D).\qquad(4)$$

However, traditional VI-based methods could be more inefficient in optimizing Eq. 4 and are hard to apply to deep learning-based methods directly. Fortunately, Gal and Ghahramani [36] claimed that Monte Carlo dropout applied in a deep neural network can be approximated to a VI processing. The dropout technique is usually used to avoid the overfitting performance of training processing and is only conducted in training processing. Unlike only using dropout in training processing, [36] enables the neural network model to a posterior probability model with the help of dropout layers. Concretely, the dropout technique defines a series of Bernoulli variables $z$ and multiplies it by the weight matrix $M$ of a full-connection or convolutional layer, e.g., $M_i$ is the weight matrix of the $i$th layer, that is,

$$\mathbf{W}_i = \mathbf{M}_i \cdot \text{diag}([z_{i,j}]_{j=1}^{K_i}),\tag{5}$$

$$z_{i,j} \sim Bernoulli(p_i), \quad i = 1, \ldots, L, j = 1, \ldots, K_{i-1},\tag{6}$$

where $p_i$ is the dropout rate of $i$th layer, $L$ is the number of layers, and $K_i$ is the number of neural units of $i$-th layer. Further, Gal and Ghahramani [36] proved that NN with the dropout technique is a posterior probability model. Next, we inspect the posterior distribution of the model output $t^* \sim q(t^*) G^*, D)$. Specifically, we sample the model weights $T_s$ times from $q(w|D)$, denoted as $w^{(1)},..., w^{(T_s)}$, and infer FB based on $T_s$ models respectively:

$$\hat{t}_k = f_{w^{(k)}}(G^*), k = 1, \ldots, T_s,\tag{7}$$

where $\hat{t}_k$ is the predicted FB vector using the $k$-th sampled model. The above sampling is sampling $z$ in Eq. 6. The statistical characteristics of the posterior distribution $q(t^*) G^*, D)$, e.g., the mean and the variance, are estimated by Monte Carlo methods. Thus, Gal and Ghahramani [36] noted this type of dropout as the MC dropout. First, the mean can be inferred by the average of sampled FBs:

$$\text{Mean}(t^*)_j = E_q \left[t^*_{j}\right] \approx \frac{1}{T_s} \sum_{k=1}^{T_s} \hat{t}_{j,k},\tag{8}$$

where $t^*_{j}$ represents the random variable of $j$-th FB, $\hat{t}_{j,k}$ is the $j$-th element of $k$-th sampled prediction (Eq. 7), and $E_q[\cdot]$ means the expectation based on the posterior distribution $q(t^*) G^*, D)$. Momentously, the mean of $t^*$ usually is a robust prediction of Bayesian NN, and we also take it as the final output of NN in this paper. More importantly, the uncertainty of FB can be captured by estimating the variance of $t^*$ using the Monte Carlo method as well. Concretely, the variance of $j$-th element of $t^*$ is estimated by:

$$\text{Var}(t^*)_j = E_q \left[t^{*2}_j\right] - \left[E_q t^{*2}_j\right]^2 \approx \frac{1}{T_s} \sum_{k=1}^{T_s} \hat{t}_{j,k}^2 - \left[\frac{1}{T_s} \sum_{k=1}^{T_s} \hat{t}_{j,k}\right]^2,\tag{9}$$

Overall, the estimated mean can be used for FB prediction, and the computed variance can help determine trust in FB.

### III. METHODOLOGY

UPNet consists of two processes: a training process and an inference process, as illustrated in Fig. 2. Since the Bayesian Segmentation Network (BSN) and the Multi-Information Regression Network (MIRN) are two neural networks (NNs), the training process optimizes the weights of BSN and MIRN using a joint-loss function as shown in Fig. 2(a). After the training process, UPNet infers robust FB picking through BSN, MIRN, and the Uncertainty-based Decision Method (UDM) sequentially. Next, we introduce the principles of each

component and the details of the training process and inference process in turn.

### A. Bayesian Segmentation Network (BSN)

To represent the distribution of the predicted FB, we construct a DL-based probability model, namely, BSN. Specifically, we utilize a popular semantic segmentation model, the U-Net [28], to detect the signal of FB and employ the Monte Carlo (MC) dropout technique [36] to convert the U-Net into a probabilistic model. Fig. 3 illustrates the structural design of BSN. The input of BSN is a shot gather, and the output is the binary segmentation map. This map labels the noise before FB as 0 and the signal after FB as 1. Next, we will introduce the details of BSN.

![img-2.jpeg](img-2.jpeg)

Fig. 3. BSN: a U-Net with the MC dropout technique. The input of BSN is a 2-dimensional (2D) gather, and the output is a segmentation map that indicates the region before FB (pixels labeled 0, blue) and the region after FB (pixels labeled 1, red).

The U-Net we use is a fully convolutional neural network designed with an encoder-decoder architecture and skip connections. In this paper, the depth is set to 3, indicating that down-sampling is performed three times. The convolutional (Conv) layers, Batch-Normalization (BN) layers, rectified linear units (ReLU) activation layers [44], Max-Pooling layers, dropout layers, transposed convolution (ConvTranspose) layers, and Sigmoid layer are the main components of the BSN. The convolutional unit is repeated many times (purple layers in Fig. 3) in the entire processing, and the model includes a Conv layer (3×3 kernel, stride = 1, and padding = 1), a BN layer, and a ReLU activation layer. The dropout layer with a constant dropout rate is applied after the final convolutional unit. In the encoder section, Max-Pooling layers (with a stride of 2) are utilized to downsample and compress redundant information. In the decoder section, we use ConvTranspose layers for upsampling, with a kernel size = 2×2 and a stride of 2. The skip connections are also used to concatenate the decoded features and the original shallow encoded features, aiming to recover the segmentation details better. Finally, we use a Conv layer with a 1×1 kernel to compress and summarize the decoded outputs without changing the output shape. We also employ a Sigmoid layer to normalize the segmentation map within the [0, 1] range. Moreover, the kernel numbers of each Conv layer should be underlined to equal the number of output channels. There are 15 Conv layers with kernel numbers of 32, 32, 64, 64, 128, 128, 256, 256, 128, 128, 64, 64, 32, 32, and 1, respectively.

Since BSN is a probability model, the model weights should be sampled in the inference process from the posterior distribution of weights w ← p(w|D) (in Eq. 2). The sampling processing is defined as the Bernoulli variables of dropout layers sampled from a Bernoulli distribution with a successful probability equal to the dropout rate. Then, the BSN with sampled weights infers the segmentation map of FB S for the gather G:

$$S = f_{w}^{\text{BSN}}(G), \tag{10}$$

where $f_{w}^{\text{BSN}}$ is the BSN with the sampled model weight w. To approximate the distribution of the segmentation map of the gather G, we conduct sampling $T_s$ times and obtain corresponding $T_s$ group weights. Accordingly, we can calculate the $T_s$ segmentation graph, denoted as $S_1, \ldots, S_{T_s}$.

### B. Multi-Information Regression Network (MIRN)

Above BSN has given a FB segmentation on a large scale. However, there are still pixel-scale deviations if we use the threshold method to obtain FB from the segmentation map [14]. Thus, MIRN is proposed to correct the errors using a regression strategy. In Fig. 4(a), MIRN includes an encoding module and a regression module. On one hand, the encoding module encodes three parts of information: the segmentation map of BSN, the original signal of traces, and the low-frequency signal of the traces. We claim that BSN has analyzed the FB region on a global level. Thus, it is sufficient for MIRN to infer specific FB values trace by trace. The segmentation map S (Eq. 10) is divided by columns into $N$ vectors, $\{s_j\}_{j=1}^N$, $j$ from 1 to $N$, where $N$ represents the number of traces in a gather. For convenience, we take the calculation of $j$-th trace as an example. The original signal of $j$-th trace is called $g_j$. To capture the local feature, we also encode the low-frequency signal of $g_j$, denoted as $g_j$. Fig. 4(b) illustrates the specific design of the low-frequency signal convolutional layer. Concretely, there are two Conv modules, which contain six layers in total. The first Conv module includes a 1D Conv layer with a kernel length of 7, striding of 1, and padding of 3, followed by a BN layer and a hyperbolic tangent (Tanh) activation layer [45], sequentially. The second Conv module consists of a 1D Conv layer with a kernel size of 3, stride of 1, and padding of 1. A BN layer and a ReLU activation layer are in sequence, followed by this. Mainly, since the value range of $\{g_j^0\}_{j=1}^N$ is [-1, 1], a Tanh activation layer is applied in the first layer to enhance the ability to capture phase information. Subsequently, three Long Short-Term Memory (LSTM) layers [46] $f_1^L$, $f_2^L$, $f_3^L$ encode $g_j^0$, $g_j$, $s_j$ into three hidden vectors $h_j^0$, $h_j^1$, and $h_j^2$, respectively, where the length of all three hidden vectors is 16. To match the complexity of the model and the data, we set different numbers of recurrent layers for $f_1^L$, $f_2^L$, and $f_3^L$, i.e., three, two, and one. On the other hand, the regression module fuses three encoded vectors ($h_j^0$, $h_j^1$, and $h_j^2$). It maps the fused vector to the corresponding pixel index of FB using three full connection (FC) layers as shown in the Regression Module of Fig. 4. Specifically, $h_j^0$, $h_j^1$, and $h_j^2$ are sequentially concatenated into a vector of length 48. Subsequently, three FC layers output two vectors of length 12 and 4 and a scale value, respectively. Particularly,

the value range of the scale value is [0, 1], which represents the percentage of the relative position in the original sampling length $T$ in the time domain. Thus, we multiply this scalar by the length $T$ to recover the corresponding index of FB. In MIRN, we repeat this process for each trace and obtain the FB indexes, denoted as $\mathbf{t}^{*}=\left[\hat{t}_{1}, \ldots, \hat{t}_{N}\right]$.
![img-3.jpeg](img-3.jpeg)

Fig. 4. The flow chart of MIRN. A 2D gather is divided into N traces, and MIRN picks FB trace by trace. The shape (or length) of each element is marked in the lower right corner.

## C. Uncertainty-based Decision Method (UDM)

UDM consists of two steps: calculating uncertainty and removing unstable picking. On the one hand, MIRN can regress corresponding FB vectors based on the segmentation maps sampled from BSN, and we denoted them as $\mathbf{t}_{(\mathbf{1})}^{*}, \ldots, \mathbf{t}_{(\mathbf{T}_{s})}^{*}$, where $T_{s}$ is sampling times of BSN and the length of each vector is $N$. Thus, the uncertainty of FB corresponding to $j$-th trace can be expressed by the variance of $T_{s}$ pickings (Eq. 9):

$$
\operatorname{Var}\left(t_{j}^{*}\right) \approx \frac{1}{T_{s}} \sum_{k=1}^{T_{s}} \hat{t}_{j, k}^{2}-\left[\frac{1}{T_{s}} \sum_{k=1}^{T_{s}} \hat{t}_{j, k}\right]^{2}
$$

where $\hat{t}_{j, k}$ represents $j$-th element in $\mathbf{t}_{(\mathbf{k})}^{*}$, where $j=1, \ldots, N$. On the other hand, unstable picking can be removed based on the estimated variance. Since variance is a random variable, we can calculate an empirical distribution of variance. Subsequently, we obtain a threshold of variance $t_{\text {var }}(p)$, which ensures:

$$
\left|\frac{\#\left(\hat{F}_{v}(v)<t_{\text {var }}(p)\right)}{N_{\text {all }}}-p\right|<0.1 \%
$$

where $\hat{F}_{v}$ represents the empirical distribution function (EDF) of the variance, $\#(\cdot)$ represents the count function, $v$ represents the random variable corresponding to variance, and $N_{\text {all }}$ is the number of all traces. We call $p$ confidence level, which can be determined by the quality of the survey. For instance, $p$ can be set as 0.9 when the survey data has high SNR and 0.6 when the survey data has low SNR. Subsequently, the pickings with the variances greater than $t_{\text {var }}(p)$ are removed. Finally, the FBs of the remaining traces with low picking variances are determined by calculating the mean value of the sampled picks:

$$
\hat{t}_{j}=E\left(t_{j}^{*}\right) \approx \frac{1}{T_{s}} \sum_{k=1}^{T_{s}} \hat{t}_{j, k}
$$

where $j$ is in the index set of the remaining traces.

## D. Training and Inference of UPNet

1) Preprocess: Before starting training and inference, the traces in the 2D gather should be preprocessed, including linear moveout (LMO) correction and trace-wise normalization. On the one hand, we crop the input region of the gather based on the LMO correction, which utilizes a velocity prior to the current survey to estimate reference arrival times for each trace. Especially, the reference arrival time of the $j$-th trace $t_{j}$ is computed by:

$$
t_{j}=d_{j} / v+t_{0}
$$

where $d_{j}$ is the offset, i.e., the distance between the source and the receiver. $v$ and $t_{0}$ are the reference velocity and the interception time of the prior information in the current survey, which is detailed in III.B. Therefore, the top boundary $\mathrm{U}_{j}$ and the bottom boundary $\mathrm{D}_{j}$ of the crop index of $j$-th trace are computed by:

$$
\mathrm{U}_{j}=t_{j}-\frac{h}{2} ; \mathrm{D}_{j}=t_{j}+\frac{h}{2}-1
$$

where $h$ represents the cropped length. On the other hand, we normalize each trace of the gather after LMO correction using the trace-wise normalization method:

$$
g_{i j}^{n}=\frac{g_{i j}}{\max _{i=1, \ldots, T}\left\{\left|g_{i j}\right|\right\}}, j=1, \ldots, N
$$

where $g_{i j}$ represents the amplitude of the $i$-th row and $j$-th column of the gather $\mathbf{G}, g_{i j}^{n}$ is the corresponding normalization value, and $N$ is the trace number of the gather $\mathbf{G}$. After these two steps, we crop the gather to a smaller shape and map it into the range of $[-1,1]$
2) Training Process: UPNet contains two learning tasks: a segmentation task (BSN) and a regression task (MIRN). To improve the cooperative picking ability of BSN and MIRN, we train them simultaneously in the same training framework as shown in Fig. 2(a). However, the optimization problem of the multi-task model is intractable. We must keep the balance among the loss function of various tasks to mitigate the disappearance of gradients. In our study, we adopt a balance strategy of loss functions, named MetaBalance [47]:

$$
\mathrm{L}^{\mathrm{B}}=\mathrm{L}^{\mathrm{Seg}}+\mathrm{L}^{\mathrm{Reg}} \cdot \frac{\left|\mathrm{~L}^{\mathrm{Reg}}\right|}{\left|\mathrm{L}^{\mathrm{Seg}}+\epsilon\right|}
$$

where $\mathrm{L}^{B}, \mathrm{~L}^{\text {Seg }}$ and $\mathrm{L}^{\text {Reg }}$ are the loss function of the balanced, the segmentation task, and the regression task, respectively. Especially, the adaptive balance parameter $\frac{\left|\mathrm{L}^{\text {Seg }}\right|}{\left|\mathrm{L}^{\text {Seg}}+\epsilon\right|}$ does not participate in the backward propagation of the gradient, and $\epsilon$ is a positive number very close to 0 to ensure division. Specifically, the loss function $L^{\text {Seg }}$ used in the segmentation task is the binary cross entropy (BCE) loss function to supervise the difference between the segmentation maps of ground truth $\mathbf{S}^{\mathrm{GT}}$ and prediction $\mathbf{S}^{\mathrm{P}}$. The specific loss function on a pair of $\mathbf{S}^{\mathrm{GT}}$ and $\mathbf{S}^{\mathrm{P}}$ is defined by:
$L^{\text {Seg }}\left(\mathbf{S}^{\mathrm{P}}, \mathbf{S}^{\mathrm{GT}}\right)=-\sum_{i=1}^{T} \sum_{j=1}^{N} \frac{s_{i j}^{\mathrm{GT}} \cdot \log s_{i j}^{\mathrm{P}}+\left(1-s_{i j}^{\mathrm{GT}}\right) \cdot \log \left(1-s_{i j}^{\mathrm{P}}\right)}{T \cdot N}$

where $s_{i_{j}^{\mathrm{GT}}}^{\mathrm{GT}}$ and $\log \left(1-s_{i_{j}^{\mathrm{P}}}^{\mathrm{P}}\right)$ are the $i$-th row and $j$-th column values of the $\mathbf{S}^{\mathrm{GT}}$ and $\mathbf{S}^{\mathrm{P}}$, respectively, and $T$ and $N$ are the number of time samples and traces, respectively. Moreover, we use the smooth L1 loss function to supervise the deviation between manual FB $\mathbf{t}^{\mathbf{M}}$ and automatic FB $\mathbf{t}^{\mathbf{A}}$. The smooth L1 loss function defined on a gather is:

$$
\begin{gathered}
\mathrm{L}^{\mathrm{Re}_{\mathrm{g}}}\left(\mathbf{t}^{\mathbf{A}}, \mathbf{t}^{\mathbf{M}}\right)=\sum_{j=1}^{N} \frac{l_{j}}{N} \\
l_{j}= \begin{cases}0.5\left(t_{j}^{M}-t_{j}^{A}\right)^{2} / \beta, & \text { if }\left|t_{j}^{M}-t_{j}^{A}\right|<\beta \\
\left|t_{j}^{M}-t_{j}^{A}\right|-0.5 \times \beta, & \text { otherwise }\end{cases}
\end{gathered}
$$

where $t_{j}^{M}$ and $t_{j}^{A}$ are the $j$-th values of $\mathbf{t}^{\mathbf{A}}$ and $\mathbf{t}^{\mathbf{M}}$.
3) Inference Process: After the training process, UPNet infers the FB of a new 2D gather that has not been seen before through four sequential steps as shown in Fig. 2. First, we sample $T_{s}$ groups of the weights, denoting these BSNs as $f_{1}^{\mathrm{BSN}}, \ldots, f_{T_{s}}^{\mathrm{BSN}}$. Second, the preprocessed gather is input into these BSNs, and the segmentation maps $\mathbf{S}_{\mathbf{1}}, \ldots, \mathbf{S}_{\mathbf{T}_{\mathbf{s}}}$ are computed. Third, the trained MIRN predicts the corresponding FBs $\mathbf{t}_{\mathbf{1}}^{*}, \ldots, \mathbf{t}_{\mathbf{T}_{\mathbf{s}}}^{*}$ for $\mathbf{S}_{\mathbf{1}}, \ldots, \mathbf{S}_{\mathbf{T}_{\mathbf{s}}}$. Finally, the sampled FBs $\mathbf{t}_{\mathbf{1}}^{*}, \ldots, \mathbf{t}_{\mathbf{T}_{\mathbf{s}}}^{*}$ are filtered by the UDM, and we obtain the inferred FBs $\left\{\hat{t}_{j}\right\}_{j=1}^{N}$ for $N$ traces. Since the inference processes of the BSNs are independent, the computation processes can be parallel. Furthermore, the same applies to MIRN. Thus, even though the sampling time is extensive, the computational time of UPNet can be managed.

## IV. EXPERIMENTS

## A. Datasets and Metrics

To facilitate comparison of other popular methods and other researchers expediently reproduce our approach, we test on a group of the open source field datasets from all unique mining sites in three provinces of Canada provided by [48], including four datasets, named Lalor, Brunswick, Halfmile, and Sudbury, respectively. More details of each dataset are shown in Tab. I, in which label ratio is the ratio of the number of labeled traces to the number of all traces. The provided FB labels are first obtained using the STA/LTA method and then corrected by experts. Notably, each FB in these datasets is annotated at the trough of the arrival waveform.

TABLE I
OPEN DATASET INFORMATION


To evaluate the FB of automatically picking methods, we adapt the metrics of a benchmark method of the open-source dataset we use [48]. For convenience, $\mathbf{t}^{\mathrm{A}}$ and $\mathbf{t}^{\mathrm{M}}$ represent the picking vector of automatical methods and humans on a 2D gather. Particularly, both lengths of them are $N$, and the FB values of the traces removed by UDM are -1 . Since UPNet removes some picks with low confidence, we introduce a new metric called automatic pick rate (APR), not mentioned in
[48], which calculates the rate of automatic picks compared to manual picks:

$$
\operatorname{APR}\left(\mathbf{t}^{\mathrm{A}}\right)=\frac{1}{N} \sum_{j=1}^{N} I\left\{t_{j}^{\mathrm{A}}>0\right\}
$$

where $t_{j}^{\mathrm{A}}$ is the $j$-th element of $\mathbf{t}^{\mathrm{A}}$, and $I\{\cdot\}$ is the indicator function. Next, we will briefly introduce the metrics utilized in the study [48]. First, the hit rate within k pixel (HR@kpx, $k=$ $1,3,5,7$, and 9 ) is used to measure the accuracy of automatic FB:

$$
\operatorname{HR} @ k \mathrm{px}\left(\mathbf{t}^{\mathrm{A}}, \mathbf{t}^{\mathrm{M}}\right)=\frac{\sum_{j=1}^{N} I\left\{\left|t_{j}^{\mathrm{A}}-t_{j}^{\mathrm{M}}\right|<k\right\} \cdot I_{j}}{\sum_{j=1}^{N} I_{j}}
$$

where $t_{j}^{\mathrm{M}}$ is the $j$-th element of $\mathbf{t}^{\mathrm{M}}$, and

$$
I_{j}=I\left\{t_{j}^{\mathrm{A}}>0, t_{j}^{\mathrm{M}}>0\right\}
$$

Second, the mean absolute error (MAE) measures the mean deviation between the automatic picking and the manual picking:

$$
\operatorname{MAE}\left(\mathbf{t}^{\mathrm{A}}, \mathbf{t}^{\mathrm{M}}\right)=\frac{\sum_{j=1}^{N}\left|t_{j}^{\mathrm{A}}-t_{j}^{\mathrm{M}}\right| \cdot I_{j}}{\sum_{j=1}^{N} I_{j}}
$$

Third, the root mean square error (RMSE) represents the stability of the automatic picking and is defined by:

$$
\operatorname{RMSE}\left(\mathbf{t}^{\mathrm{A}}, \mathbf{t}^{\mathrm{M}}\right)=\frac{\left(\sum_{j=1}^{N}\left|t_{j}^{\mathrm{A}}-t_{j}^{\mathrm{M}}\right|^{2} \cdot I_{j}\right)^{1 / 2}}{\sum_{j=1}^{N} I_{j}}
$$

Finally, the mean bias error (MEB) is defined by:

$$
\operatorname{MBE}\left(\mathbf{t}^{\mathrm{A}}, \mathbf{t}^{\mathrm{M}}\right)=\frac{\sum_{j=1}^{N}\left(t_{j}^{\mathrm{A}}-t_{j}^{\mathrm{M}}\right) \cdot I_{j}}{\sum_{j=1}^{N} I_{j}}
$$

To some extent, MBE can represent the preference of automatic picking methods for position picking. For instance, MBE $<0$ indicates that the method favors selecting the pixels before those corresponding to FBs.

## B. Implement Details

This subsection has three aspects: a four-fold experiment setting, hyperparameters setting of the LMO correction, and training hyperparameters tuning method. First, to compare with the benchmark method [48], we followed the same fourfold experiment described in their study, where the model is evaluated in four dataset splits, respectively. Tab. II shows four training scenarios that mimic real-world applications. This involves training on a few field surveys and predicting results for other surveys that have not been seen before. To avoid

experimental variability, these four folds use different combinations of training sets and are tested on various validation and test sets. Moreover, the experiments of each fold are independent of each other, so data leakage cannot occur. Second,

TABLE II
FOUR-FOLD EXPERIMENT SETTING


the LMO correction has two important hyperparameters (Eq. 14): the reference velocity and the interception time $t_{0}$. Tab. III illustrates the details of the hyperparameters used in these four field surveys, which are estimated by a few manually picking FBs. Concretely, the reference velocity ranges from $5136.20 \mathrm{~m} / \mathrm{s}$ to $6013.97 \mathrm{~m} / \mathrm{s}$, and the interception time falls within the range of [0.0017s, 0.0367s]. Subsequently, the LMO correction under these parameters is conducted for each fold, and the height of the cropped gather is 128 , i.e., $h=128$ in Eq. 15. Moreover, to avoid the influences of the unpicked region, we only retain the traces with manual annotations and divide the entire gather after LMO correction into pieces with a width of 256. Thus, the final gathers used in experiments are 918, 14582, 3879, and 4389 gathers of shape $=(128,256)$ in Sudbury, Brunswick, Halfmile, and Lalor, respectively.

TABLE III
HYPERPARAMETERS IN THE LMO CORRECTION


Finally, we tune the training hyperparameters using a grid search method. Specifically, we consider the hyperparameters, including the size of the training mini-batch ( $\mathrm{BS} \in$ $\{2,4,8,16,32,64,128\})$, the learning rate of the optimizer $(\mathrm{Lr} \in\{1 \mathrm{e}-2,1 \mathrm{e}-3,1 \mathrm{e}-4\})$, optimization method (Opt $\in\{$ Adam [49], SGD [50]\}), and the dropout rate (dr $\in$ $\{0.1,0.2,0.3,0.4,0.5\})$. Each combination of hyperparameters is repeated ten times using ten random initial seeds of weights. The performance of combinations is evaluated on the mean values of MAE of validation sets over ten training with various random seeds. Tab. IV indicates the best combination of hyperparameters for each fold in the grid search.

TABLE IV
HYPERPARAMETER SETTING OF TRAINING PROCESSING


## C. Comparative Experiments

To evaluate the performance of UPNet, we compare four state-of-the-art (SOTA) methods for automatically picking methods quantitatively. We also visualize the picking results of a classic picking method, the current end-to-end SOTA method, and UPNet. There are a few studies on the opensource dataset used in our study: the benchmark method [48], the self-trained network [51], and the multi-stage segmentation picking network (MSSPN) [52]. Since the training method of benchmark [48] and the self-trained network [51] are the same as ours, we compare UPNet with them. UPNet is an end-to-end method. Thus, we also compare an end-to-end SOTA method called CNNRNN [32]. Moreover, we also compared the traditional method STA/LTA to verify the generalization of automatic methods.

Next, we detail the training processes of each comparative model. First, the length of the long window and the short window in the STA/LTA method are selected among $\{50,40,30,20,10\}$ and $\{5,4,3,2\}$, respectively, as suggested by [53]. We select the combinations of each fold corresponding to the best test MAE as the optimal parameters of STA/LTA. Second, due to the complexity of implementing the benchmark method and the self-trained network, we directly reference the experimental results in the original papers to prevent accuracy errors resulting from the issues we encountered during reproduction. Finally, we adopt the parameters used in the original paper to train CNNRNN—specifically, BS=4 for CNN, BS=10 for RNN, and $\mathrm{Lr}=1 \mathrm{e}-3$ for both CNN and RNN. Moreover, the ground truth of the segmentation is involved in the benchmark method, the self-trained network, and CNNRNN. They all label the pixels before FBs as 0 and others as 1, similar to UPNet.

For each fold, the benchmark method, the self-trained network, CNNRNN, and our UPNet are trained ten times with various seeds using the training hyperparameters mentioned above. Additionally, UPNet takes the sampling ten times in the inference process. Tab. V showcases the test results of these five models, where each value in the table indicates the mean value $\pm$ the standard deviation. Concretely, the APR of UPNet can be controlled by $t_{\text {var }}(p)$, and we assume $80 \%$ traces can be picked. Thus, we set $t_{\text {var }}(0.8)$ to remove the unstable picking of UPNet. Tab. V illustrates that UPNet outperforms another four automatic picking methods on Brunswick, Halfmile, and Lalor test sites. Notably, the self-trained method is extraordinary with two round training processes. The incorrect manual picking is removed between the two training processes. There are a few lousy manual picking in Sudbury. Multiple training processes used in the self-trained network can correct these error. Thus, the selftrained network performs well in the HR@5-9px, RMSE, MAE of Sudbury. However, the precision of the self-training network is insufficient, so both UPNet and CNNRNN exceed it on the HR@1px and HR@3px. UPNet performs better than the self-trained on accuracy (MAE) and stability (RMSE) for another three folds. Then, UPNet can outperform STA/LTA, the benchmark, and CNNRNN a lot in the test of four-folds, specifically in fold 3. In the Brunswick test, the HR@1px

TABLE V
Four-Fold Experimental Results of Five Comparative Methods


![img-4.jpeg](img-4.jpeg)

Fig. 5. Four classic picking cases of the STA/LTA, CNNRNN, UPNet, and manual picking on the surveys of Sudbury, Brunswick, Halfmile, and Lalor, respectively.
of UPNet is $99 \%$, indicating its reliability in picking surveys with relatively high SNR in real-world scenarios. Furthermore, comparing end-to-end methods (CNNRNN and UPNet) with the methods of the segmentation plus threshold post process (the benchmark and the self-trained network), we conclude that the end-to-end method is more suitable for the FB picking task. We analyze that the blurred boundary of the FB signal in the segmentation map causes the low HR@1px. Moreover, unlike CNNRNN, UPNet can filter unstable pickings based on
computed uncertainty. Specifically, the lowest RMSE verifies that UPNet is the most robust method for picking FB. Finally, in comparing STA/LTA and deep learning-based methods, we observe that the accuracy and stability of STA/LTA can not meet the real need because of the many manual parameters and the various noises of the field. Therefore, the deep learning-based automatic picking method is better for the FB picking task. Through the above analysis, we have verified the superiority of UPNet from a quantitative perspective. Next, we

visualize four classic picking cases of each test site.

Next, we visualize four classic picking cases on each test site, as shown in Fig. 5. UPNet achieves relatively robust picking in these four examples, even in the Lalor dataset with low SNR. Concretely, Fig. 5(d) shows that FB has continuous jumps, but UPNet achieves good recognition ability. Even in the places with large jumps (traces 60-80), UPNet picks a little robust FB. This verifies that UPNet has the picking characteristics of preferring to miss rather than to overuse. Furthermore, UPNet can also be used to evaluate manual picking. For instance, at traces 230-250 in Fig. 5(c), manual picking is terrible, but the picking of UPNet is still robust. Moreover, UPNet can avoid over-picking. Specifically, in Fig. 5(b), the noise at the position of trace 75-100 is extreme, and accurate FB cannot be easily picked manually. It is reasonable not to pick these traces in such a scenario. UPNet does this, but for CNNRNN, there is no measurement of the picking error. Finally, picking the STA/LTA method is acceptable in the areas where the FB signal is separated from the background noise. However, it is a local method. It cannot pick according to the global FB trend when the noise changes drastically. Therefore, the characteristic of local picking leads to easy jumping in picking, such as the jumping of yellow circles in Fig. 5(a)-(c). Based on the analysis of the above visual results, we conclude that UPNet is more robust and suitable for practical applications than other methods.

### V-D Uncertainty Representation in First Break Picking

After comparing the advantages of our method and other segmentation-based methods in evaluating metrics, we further explore why introducing uncertainty measures can improve the accuracy and stability of the first break picking. From the quantitative point of view, we calculate the sample distribution of UPNet output and analyze the correlation between the regression variances and corresponding MAEs. Specifically, we take a trained model on Fold 4 as an example. We take the variance of the sample distribution of UPNet regression as the horizontal coordinate and the MAE between the mean value of the sample distribution and the manual FB as the longitudinal coordinate. Fig. 6(a) illustrates how these points are distributed on a plane and shows that a larger variance results in a bigger MAE. Further, we conduct linear regression based on these points to understand the quantifiable relationship between variance and MAE. Fig. 6(b) indicates that the linear regression function is $y=1.5365x+1.4362$, meaning that for every one increase in variance, MAE increases by 1.5365. Moreover, we also run the Pearson correlation test, and his null hypothesis is that the Pearson correlation coefficient $\rho$ is equal to 0, and his alternative hypothesis is that $\rho \neq 0$. In this showcase, the total number of points is 1122304, and the Pearson correlation coefficient $\rho=0.3356$. The hypothesis test corresponds to a p-value of 0.0000 , rounded to 4 decimal places. Thus, we can reject the null hypothesis at a significance level of $\alpha=0.001$, meaning we consider it relevant.

In order to further verify the relationship between the estimated variance and the picking reliability, we visualize two specific picking cases on traces of Lalor as shown in Fig. 7
![img-5.jpeg](img-5.jpeg)

Fig. 6. (a) Count the 2-dimensional points (variances of UPNet regression, MAE) and visualize them on a heat map. (b) Conduct Pearson coefficient test and linear regression.
and 8. On the one hand, when the variance of the sampled distribution is large, the automatic picking of UPNet on this trace is suspect. Fig. 7(b) shows the kernel density estimation (KDE) of the sampled distribution of this trace, while Fig. 7(a) illustrates that the significant variance (0.037) leads to poor picking (indicated by the blue arrow). On the other hand, when the variance is slight, the picking of UPNet on this trace is reliable. Fig. 8 shows that picking with low variance in the sampled distribution is accurate.
![img-6.jpeg](img-6.jpeg)

Fig. 7. A showcase of the UPNet picking with a large variance.
![img-7.jpeg](img-7.jpeg)

Fig. 8. A showcase of the UPNet picking with a low variance.

## E. Robustness Test

To further test the robustness of the UPNet, we add Gaussian noise with different SNRs to the test sites and evaluated both the trained UPNet and CNNRNN on the gather with various SNRs. We assume that the four test datasets used have relatively high SNRs, meaning no noise is present. Thus, we can inject Gaussian noise to generate the polluted gather with the expected constant SNR, which is defined by:

$$
\text { SNR }=10 \times \log _{10} \frac{\sigma_{z}^{2}}{\sigma_{n}^{2}}
$$

where $\sigma_{s}^{2}$ and $\sigma_{n}^{2}$ represent the signal variances and the Gaussian noise, respectively. Subsequently, the variance of the added Gaussian noise can be computed using:

$$
\sigma_{n}^{2}=\sigma_{s}^{2} / 10^{\mathrm{SNR}^{*} / 10}
$$

where $\mathrm{SNR}^{*}$ is the constant SNR and $\sigma_{s}^{2}$ can be estimated from each single trace signal directly. We generate eight Gaussian noise data sets with $20,10,5,3,1,-1$, and -5 SNRs, respectively. We select the best model in the training of ten random seeds for UPNet and CNNRNN in each fold experiment, totaling eight models. Then, we test these eight models on corresponding test datasets with various SNRs. For UPNet, we use the variance threshold $t_{\text {var }}(0.8)$ defined in Eq. 12 to filter the unstable pickings. Fig. 9 visualizes the robustness test results on Brunswick. Specifically, UPNet outperforms CNNRNN under various SNRs, exhibiting higher HR@3px and lower MAE. In Fig. 9, we observe a phenomenon: CNNRNN shows a noticeable decrease in MAE at $\mathrm{SNR}=3$, while for UPNet, it occurs at $\mathrm{SNR}=-1$. This phenomenon also indicates that UPNet has more vital antinoise ability than CNNRNN.
![img-8.jpeg](img-8.jpeg)

Fig. 9. Anti-noise ability test of UPNet and CNNRNN on Brunswick.

## V. CONCLUSION

In this paper, we propose a novel deep learning-based end-to-end FB picking framework that incorporates uncertainty quantification, thereby enhancing the accuracy and stability of the automatic picking process. After analyzing various experiments, three conclusions can be inferred. (1) UPNet can estimate the uncertainty of the picked FB directly and eliminate the unstable picks to enhance both accuracy and stability. (2) The test performance of UPNet in field surveys achieves SOTA, and the picking characteristics of UPNet also align with the principle of erring on the side of excess in practical applications. (3) Compared with other end-toend deep learning methods such as CNNRNN, UPNet has more substantial anti-noise capabilities, further verifying its feasibility for application in field surveys.

## ACKNOWLEDGMENT

The author would like to thank Mr. Pierre-Luc St-Charles from Applied Machine Learning Research Team Mila, Québec AI Institute for providing the open datasets.
