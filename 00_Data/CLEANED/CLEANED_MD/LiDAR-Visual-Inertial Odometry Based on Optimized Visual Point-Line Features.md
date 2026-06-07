# Article 

## LiDAR-Visual-Inertial Odometry Based on Optimized Visual Point-Line Features

Xuan He ${ }^{1,2}$, Wang Gao ${ }^{1,2, *}$, Chuanzhen Sheng ${ }^{3,4}$, Ziteng Zhang ${ }^{3,4}$, Shuguo Pan ${ }^{1,2}$, Lijin Duan ${ }^{5}$, Hui Zhang ${ }^{1,2}$ and Xinyu Lu ${ }^{1,2}$

## check for updates

Citation: He, X.; Gao, W.; Sheng, C.; Zhang, Z.; Pan, S.; Duan, L.; Zhang, H.; Lu, X. LiDAR-Visual-Inertial Odometry Based on Optimized Visual Point-Line Features. Remote Sens. 2022, 14, 622. https:// doi.org/10.3390/rs14030622

Academic Editor: Giuseppe Casula
Received: 20 December 2021
Accepted: 26 January 2022
Published: 27 January 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Instrument Science and Engineering, Southeast University, Nanjing 210096, China; hexuan@seu.edu.cn (X.H.); psg@seu.edu.cn (S.P.); amzhanghui@seu.edu.cn (H.Z.); 220213597@seu.edu.cn (X.L.)
2 Key Laboratory of Micro-Inertial Instrument and Advanced Navigation Technology, Southeast University, Nanjing 210096, China
3 State Key Laboratory of Satellite Navigation System and Equipment Technology, Shijiazhuang 050081, China; shengchuanzhen@163.com (C.S.); zzteng54@163.com (Z.Z.)
4 The 54th Research Institute of China Electronics Technology Group Corporation, Shijiazhuang 050081, China
5 Linzi District Transportation Service Center, Zibo 255400, China; lzqitysjqdjgs@zb.shandong.cn

* Correspondence: gaow@seu.edu.cn

Abstract: This study presents a LiDAR-Visual-Inertial Odometry (LVIO) based on optimized visual point-line features, which can effectively compensate for the limitations of a single sensor in real-time localization and mapping. Firstly, an improved line feature extraction in scale space and constraint matching strategy, using the least square method, is proposed to provide a richer visual feature for the front-end of LVIO. Secondly, multi-frame LiDAR point clouds were projected into the visual frame for feature depth correlation. Thirdly, the initial estimation results of Visual-Inertial Odometry (VIO) were carried out to optimize the scanning matching accuracy of LiDAR. Finally, a factor graph based on Bayesian network is proposed to build the LVIO fusion system, in which GNSS factor and loop factor are introduced to constrain LVIO globally. The evaluations on indoor and outdoor datasets show that the proposed algorithm is superior to other state-of-the-art algorithms in real-time efficiency, positioning accuracy, and mapping effect. Specifically, the average RMSE of absolute trajectory in the indoor environment is 0.075 m and that in the outdoor environment is 3.77 m . These experimental results can prove that the proposed algorithm can effectively solve the problem of line feature mismatching and the accumulated error of local sensors in mobile carrier positioning.

Keywords: multi-sensor fusion; visual point and line feature; SLAM; LiDAR-visual-inertial odometry

## 1. Introduction

Multi-sensor fusion localization technology based on Simultaneous Localization and Mapping (SLAM) is a fundamental technology in the field of high-precision localization of mobile carriers [1]. The SLAM-based multi-sensor fusion system applied to mobile carriers can be divided into two core parts: the front-end, and the back-end. The function of the front-end is used to analyze the environmental fingerprint information collected by the sensors, in order to estimate the positional information of the mobile carrier in time. In addition, the change in the surrounding environment with the movement of the carrier is restored. The function of the back-end is used to obtain the final positioning results by iteratively optimizing the position estimates obtained from the front-end analysis. Depending on the sensors used in the front-end, it can be divided into methods mainly based on LiDAR and vision [2,3]. Engineers and researchers in related fields have conducted a lot of research in both directions and produced a series of research-worthy results.

The main vision-based SLAM approach, namely visual odometry (VO), has long dominated the SLAM technology field due to the lower cost of the camera compared with

LiDAR. However, pure monocular visual SLAM systems cannot recover metric scales. Thus, there is a growing trend to utilize low-cost inertial measurement units to assist monocular vision systems, which is called visual-inertial odometry (VIO). Monocular VIO provides high-quality self-motion simulation by using monocular cameras and inertial measurement unit (IMU) measurements, which has significant advantages in terms of size, cost, and power. Based on the method of feature association, visual SLAM can be classified into feature point method and direct method. The feature point-based method VIO accomplishes the inter-frame feature constraint by extracting and matching image feature points [4,5,6]. Therefore, rich environmental texture is required to ensure that the threshold of the number of effective feature points required for feature tracking is reached. Tracking loss of feature points is prone to occur in weak texture environments such as parking lots and tunnels, which in turn affects localization accuracy and real-time performance. The theoretical basis of the direct method-based VIO is the assumption of constant grayscale [7,8]. It only needs to capture environmental features by the changes in the grayscale image to establish constraints, which has a better real-time performance. Nevertheless, the tracking accuracy is greatly affected by environmental illumination changes. Therefore, stable and rich line feature models are required to be introduced into the front-end to provide stable and accurate feature constraints for visual back-end state estimation. In 2018, He et al. proposed PL-VIO based on point-line feature fusion, but too many optimization factors greatly limited the real-time performance in practical tests [9]. In 2020, Wen et al. proposed PLS-VIO to optimize the 6-DOF pose by minimizing the objective function and improving the line feature matching filtering strategy to reduce the probability of mismatching [10]. Although the VIO based on point-line features has a positive effect on the number of features [11,12], it still cannot solve the scale uncertainty problem of monocular cameras. The development of VIO in practical applications still has certain limitations.

As another important technical means of SLAM-based localization technology, SLAM mainly based on LiDAR is also widely used in the industry for its high resolution, high accuracy, and high utilization of spatial features. In 2016, Google proposed Cartographer, a 2D LiDAR based on particle filtering and graph optimization. In 2017, Zhang et al. proposed the LOAM for the first time, which uses the curvature of the LiDAR point cloud to register the effective point cloud features as planar points and edge points [13]. In 2018, Shan et al. proposed LeGO-LOAM based on LOAM, which uses the ground plane feature point cloud to further filter outliers from the scanned point cloud and improve the LOAM frame [2]. In 2020, Shan et al. further introduced the LIO-SAM algorithm based on the previous work, which uses IMU pre-integrated measurements to provide initial pose estimation for laser odometry [14]. In addition, a Bayesian network-based factor graph optimization framework is proposed, in which the global position is constrained by adding GPS factors, and an incremental smooth global voxel map is established. These schemes provide technical feasibility for the high-precision positioning by fusing LiDAR with other sensors.

However, due to the inherent shortcomings of the main sensing sensors, such as the limited scanning angle of LiDAR and the sensitivity of the mainly vision-based methods to light variations, these methods can hardly show excellent robustness in real-world applications. To further improve the localization performance, LiDAR-Visual-Inertial Odometry, as a multi-sensor fusion localization method, has become a research focus of SLAM with its advantages of multi-sensor heterogeneity and complementarity.

The existing LVIO multi-sensor fusion strategy can be described from the front-end and back-end perspectives. First, the front-end fusion strategy of LVIO is introduced. Generally, LiDAR acts as a feature depth provider for monocular VO as a way to improve the scale ambiguity of visual features. Meanwhile, VO performs state estimation from the extracted visual features, which is provided as the initial state for LiDAR scan matching. Therefore, the quantity and quality of visual features are closely related to the precision of state estimation of the fusion system. In existing fusion systems, the features extracted

by camera are mainly point features [15,16]. Xiang et al. proposed a combination of fisheye camera and LiDAR based on a semantic segmentation model, which improved the confidence of the depth of visual features in the driving environment of unmanned vehicles [15]. Chen et al. proposed a method to construct a loopback constraint for LiDARvisual odometry by using the Distributed bag of Words (DboWs) model in the visual subsystem, although, without introducing IMU sensors to assist in the initial positional estimation [16]. In 2021, Lin et al. proposed R2LIVE to incorporate IMU into the fused localization system, in which the LiDAR odometry is used to establish depth constraints for VIO [17]. Although the above-mentioned algorithms exhibit superior performance to the VIO based on point features, it is still difficult to extract rich and effective features in weak texture environments, which leads to the failure in LiDAR scan matching. Therefore, additional feature constraints on the LiDAR need to be added with line features that are more robust to environmental texture and luminosity variations. Visual SLAM based on point-line features has been studied but not widely applied to LVIO systems in recent years [18,19]. In 2020, Huang et al. first proposed a LVIO based on a robust point and line depth extraction method, which greatly reduces the three-dimensional ambiguity of features [18]. Zhou et al. introduced line features in the direct method-based VIO to establish data association [19]. The above-mentioned algorithms provide technical feasibility for LVIO based on point-line features.

From the perspective of the back-end fusion strategy, LVIO can be classified into two categories based on different optimization algorithms: filter-based methods and factor graph methods. Although the filtering method is a traditional technology to realize multisensor fusion, its principle defect of frequent reconstruction of increasing or decreasing sensors limits its application in LVIO [20]. As an emerging method in recent years, the factor graph method can effectively improve the robustness of SLAM system when a single sensor fails because of its plug-and-play characteristics. Therefore, it is widely applied to deal with such heterogeneous aperiodic data fusion problems [21]. In addition, since LVIO is in the local frame, there are inherent defects such as accumulated errors. Thus GNSS measurements need to be introduced for global correction [22-24] to realize local accuracy and global drift-free position estimation, which makes full use of their complementarity [24]. The research on adding GNSS global constraints into the local sensor fusion framework are as follows: Lin et al. modified the extended Kalman filter to realize a loose coupling between GPS measurements and LiDAR state estimation, but there is a large single linearization error to be solved [17]. In 2019, Qin et al. proposed VINS-Fusion, which uses nonlinear optimization strategies to support Camera, IMU, and GNSS [25], but it assumes that GNSS is continuous and globally convergent, which is inconsistent with reality. In any case, these strategies presented above provide numerous reliable ideas.

Generally speaking, we can conclude that the existing LVIO fusion system has two problems that deserve further exploration. First, on the premise of ensuring the real-time performance, more abundant feature constraints are needed to improve the pose estimation accuracy of LVIO. Secondly, global constraints are needed to globally optimize the LVIO local pose estimation results. To address these issues, this study presents a LiDAR-VisualInertial Odometry based on optimized visual point-line features. First of all, an improved line feature extraction in scale space and constraint matching strategy based on the square method are proposed, which provides richer visual feature for the front-end of LVIO. Secondly, multi-frame LiDAR point clouds were projected into the visual frame for feature depth correlation, which improves the confidence of monocular visual depth estimation. At the same time, the initial visual state estimation can be used to optimize the scan matching of LiDAR. Finally, a factor graph based on the Bayesian network was used to build the LVIO fusion system, in which the GNSS factor and loop factor are introduced to constrain LVIO globally, to achieve locally accurate and globally drift-free position estimation in the complex environment.

## 2. System Overview

The general framework of the LiDAR-Visual-Inertial Odometry based on optimized visual point-line features proposed in this study is shown in Figure 1. The system consists of the front-end of LiDAR-Visual-Inertial Odometry tight combination and the back-end of factor graph optimization.

![img-0.jpeg](img-0.jpeg)

**Figure 1.** Overall algorithm framework, system inputs include IMU, camera, lidar, and optional GNSS. IMU provides initial state correction for VIO subsystem and LiDAR-inertial odometry (LIO) subsystem, VIO, and LIO systems use each other's information to improve the positioning accuracy, and GNSS signals are optionally added to the back-end to provide global constraints.

In the front-end of our algorithm, the visual odometry not only extracts point features but also further extracts line features in the improved scale space and performs geometric constraint matching on them, which improves the number of features in the weak texture environment. Then, the feature depth provided by LiDAR point clouds performed a role in correlating the depth of monocular visual features. IMU pre-integration provides all necessary initial values, including attitude, velocity, acceleration bias, gyroscope bias, and three-dimensional feature position, for completing the initial state estimation after time alignment with a camera. If VIO initialization fails, the IMU pre-integration value is used as the initial assumption to improve the robustness of the fusion system in the texture-free environment.

After the front-end initialization is successfully realized, the back-end optimizes the factor graph by using the estimated residual of each sensor's state. IMU pre-integration, visual residual, and lidar residual were added to the factor graph as local state factors for maximum posteriori estimation. In order to further correct the cumulative error of local state estimation, the residual of GNSS single-point positioning measurements was used as the global positioning factor to add to the factor graph. Besides, when the system detects the path loop, the loop factor will be added to the factor graph to participate in the nonlinear optimization and obtain the optimal global pose estimation.

## 3. Front-End: Feature Extraction and Matching Tracking

### 3.1. Line Feature Extraction

Commonly used line feature extraction algorithms include Hough [26], LSWMS [27], EDLine [28], and LSD [29]. Weighing factors such as accuracy, real-time performance, and the need for parameter adjustment, we chose LSD to extract line features. According to the bottom parameter optimization strategy, we modified an improved LSD algorithm and a minimum geometric constraint method to realize line feature constraint matching.

Given an N-layer Gaussian pyramid as the scale space of LSD line features, the scale ratio of images in each layer is defined to reduce or eliminate the sawtooth effect in images. After scaling the image $s$ times, a downsampling was performed, and then the gradient was calculated for all pixels in the new image obtained after downsampling. By traversing the image and getting the gradient values of all pixels, the pixel gradient rectangle can be merged according to the density of same-sex points to obtain a rectangle-like line segment $l$. The density $d$ of homogeneous points in the rectangle can be expressed as:

$$
d=\frac{k}{\operatorname{length}(l) \cdot \operatorname{width}(l)}, d \leq D
$$

where $k$ is defined as the total number of pixels in the rectangle, and $D$ is the density threshold of parity points. Different from the hypothesis in [12], a low co-location density threshold in the outdoor complex texture environment will extract a large number of invalid line features. Therefore, it is necessary to re-optimize the strategy according to the underlying parameters and select the following combinations near the original parameters ( $s=0.8, D=0.7$ ), for real-time and accuracy experiments.

We measured the positioning accuracy by the root mean square error of absolute trajectory error (APE_RMSE). The accuracy and real-time performance of different values of $s$ and $D$ on the Hong Kong 0428 dataset are shown in Figure 2. The Monte Carlo method was used in this experiment. Within the parameter range that ensures the stable operation of the line feature extraction algorithm, we conducted three experiments. First of all, as shown in Figure 2a, under the premise that the original scaling times $s=0.8,100$ random numbers were selected in the range of $D \in(0.3,0.9)$ to carry out the experiment of density threshold selection. Secondly, as shown in Figure 2b, we kept the original density threshold $D=0.7$, and then selected 100 random numbers in the range of $s \in(0.4,0.9)$, which is to select the appropriate range of scaling times $s$. Finally, as shown in Figure 2c, within the appropriate parameter range obtained in the previous experiments, 100 groups of parameter combinations were randomly selected for line feature extraction to obtain the optimal value.
![img-1.jpeg](img-1.jpeg)

Figure 2. Underlying parameter selection. (a) Density threshold selection, (b) scaling times selection. (c) Experimental results by selecting the best combination of parameters. Noted that decreasing $s$ and $D$ will show better real-time performance with negligible loss of accuracy.

According to Figure 2c it can be seen that the operation time is shorter when the value of $(s, D)$ is around $(0.5,0.6)$ or around $(0.6,0.6)$. Furthermore, we compared the accuracy of the above two groups of parameters. It can be concluded that the accuracy of line feature extraction of the former group is slightly higher than that of the latter group. Considering

the accuracy and real-time, we chose $s=0.5, D=0.6$ as the parameter combination for our system.

# 3.2. Inter-Frame Feature Constraint Matching 

Different from the neighboring line merging of different line features within the same frame in feature extraction, the least square method-based line feature constraint matching is for the same line feature pair whose angle and distance change between two consecutive frames. Considering the angle and translation changes in the same line feature pair during the carrier movement, a minimized sparse matrix model can be constructed to ensure the minimum total error in matching the line features extracted between the front and back frames.

Given a line $I^{\mathrm{IV}}=\left[n^{\mathrm{IV} T}, v^{\mathrm{IV}^{T}}\right]^{T} \in R^{6}$ extracted from the world coordinate system, where $n^{\mathrm{IV}}, v^{\mathrm{IV}} \in R^{3}$ is the normal vector and direction vector, respectively, of $I^{\mathrm{IV}}$, let the transformation matrix from the world frame to camera frame be $T_{\mathrm{C}}^{\mathrm{IV}}=\left[R_{\mathrm{C}}^{\mathrm{IV}}, t_{\mathrm{C}}^{\mathrm{IV}}\right]$, with $R_{\mathrm{C}}^{\mathrm{IV}}, t_{\mathrm{C}}^{\mathrm{IV}}$ denoting the rotation and translation, respectively, then $I^{\mathrm{IV}}$ can be expressed in Plücker coordinates within the camera frame as:

$$
I^{\mathrm{C}}=\left[\begin{array}{c}
n^{\mathrm{C}} \\
v^{\mathrm{C}}
\end{array}\right]=T_{\mathrm{C}}^{\mathrm{IV}} I^{\mathrm{IV}}=\left[\begin{array}{cc}
R_{\mathrm{C}}^{\mathrm{IV}} & {\left[t_{\mathrm{C}}^{\mathrm{IV}}\right]_{T_{\mathrm{C}}} R_{\mathrm{C}}^{\mathrm{IV}}} \\
0 & R_{\mathrm{C}}^{\mathrm{IV}}
\end{array}\right]\left[\begin{array}{c}
n^{\mathrm{IV}} \\
v^{\mathrm{IV}}
\end{array}\right] \in R^{6}
$$

It can be seen that the matching of line feature pairs in the camera frame is a 6-DOF parametric matching problem. In order to improve the accuracy and simplify the line feature matching problem, it can be simplified as a 4-DOF parameter matching optimization problem. Let all the line feature pairs obtained by matching between two consecutive frames in the camera frame be:

$$
F_{i j}=\left\{\left(l_{i}, l_{j}\right) \mid j \in[1, n]\right\}
$$

where $l_{i}$ and $l_{j}$ are certain line features extracted in the previous frame and subsequent frame, respectively, $n$ is the total number of line features in the subsequent frame.

According to the variation in the inter-frame line characteristics shown in Figure 3, the parameter matrix can be set as $e_{i j}=\left[\theta_{i j}, \mu_{i j}, \rho_{i j}, d_{i j}\right]^{T}, \theta_{i j}$ and $d_{i j}$ are the included angle and translation distance between two consecutive frames, respectively, $\mu_{i j}$ and $\rho_{i j}$ are the projection ratio and length ratio of the front-to-back interframe line features. Constructing the parameter matrix may establish a linear constraint matrix $A_{i}=\left[e_{i 1}, \ldots, e_{i j}, e_{i n}\right]$ of the subsequent keyframe for $l_{i}$. The target vector of the matching judgment of $l_{i}$ is $m_{i}=\left[m_{i 1}, \ldots, m_{i j}, \ldots, m_{i n}\right]^{T}$. The value of each component is determined by the result of feature matching, where matching is 1 and non-matching is 0 . If $\sum m_{i n}=1$, the linear constraint $A_{i} m_{i}=t$ will be satisfied. Therefore, the line feature matching problem can be optimized into a constrained matching equation based on least squares:

$$
\min _{m_{i}} \lambda\left\|m_{i}\right\|_{1}+\frac{1}{2}\left\|A_{i} m_{i}-t\right\|_{2}
$$

where $\lambda$ is the weight coefficient and $t=[0,1,1,0]^{T}$ is the constraint target vector.
![img-2.jpeg](img-2.jpeg)

Figure 3. Deviation of a line feature during the movement of the carrier. (a) Parallel offset (b) angular offset.

# 3.3. LiDAR-Aided Depth Correlation of Visual Features 

LiDAR-aided depth correlation of visual features can effectively improve the scale ambiguity of monocular cameras. Since the LiDAR resolution is much lower than that of the camera, the use of only a single frame of sparse point cloud depth correlation will result in a large number of visual feature depth deletions [30]. Therefore, this study purposes a strategy of superimposing multi-frame sparse point cloud to obtain the depth value of the point cloud, which is used to establish the depth correlation with the visual features.

As shown in Figure 4, $f_{1}^{V}$ is a feature point in the visual frame $\{V\}$, and $\left\{d_{1}^{L}, \ldots, d_{m}^{L}\right\}$ is a group of depth point clouds in the lidar frame $\{L\}$. Projecting $d_{n}^{L}$ onto a unit spherical surface $\left\{V_{g}\right\}$ with $f_{1}^{V}$ as the spherical center to obtain a projection point $d_{n}^{V_{g}}$ :

$$
d_{n}^{V_{g}}=R_{L}^{V_{g}} d_{n}^{L}+p_{L}^{V_{g}} \quad n \in[1, m]
$$

where $R_{L}^{V_{g}}$ and $p_{L}^{V_{g}}$ are the rotation matrix and external parameter matrix of $\{L\}$ to $\left\{V_{g}\right\}$, respectively. Taking $f_{1}^{V}$ as the root node to establish KD tree to search for the three closest depth points $d_{1}, d_{2}, d_{3}$ on the sphere. Then, connecting $f_{1}^{V}$ with the camera center $O$ and intersecting $\Delta d_{1} d_{2} d_{3}$ with $O_{d}$, we can obtain the characteristic depth of $f_{1}^{V}$ as $f_{1}^{V} O_{d}$.
![img-3.jpeg](img-3.jpeg)

Figure 4. Association of visual feature depth.

## 4. Back-End: LVIO-GNSS Fusion Framework Based on Factor Graph

### 4.1. Construction of Factor Graph Optimization Framework

The framework of factor graph optimization based on the Bayesian network proposed in this study is shown in Figure 5. The state vector in that world frame construct according to the constraint factor shown in the figure is:

$$
\mathcal{X}=\left[x_{1}, x_{2}, \ldots, x_{i}, \lambda_{1}, \lambda_{2}, \ldots, \lambda_{p}, 1,2, \ldots, l, d_{1}^{e}, d_{2}^{e}, \ldots, d_{k}^{e}, d_{1}^{p}, d_{2}^{p}, \ldots, d_{k}^{p}\right]
$$

where $x_{n}=\left[p_{n}, q_{n}, v_{n}, b_{a}, b_{g}\right]$ represents the IMU state at the $n$th time, which includes the carrier position $p_{i}$, the rotation quaternion $q_{i}$ and the velocity $v_{n}$ obtained by IMU preintegration in the world frame, $b_{a}$ and $b_{g}$ stand for the acceleration bias and the gyroscope bias in IMU body frame, respectively, $\lambda_{p}$ represents the inverse depth of the visual point feature in the visual frame from its initial observation in the first frame, $l$ represents the orthogonal frame of the visual line feature, $d_{k}^{e}$ and $d_{k}^{p}$ stand for the distances between the LiDAR feature points and its corresponding edge or plane feature point cloud, respectively.

![img-4.jpeg](img-4.jpeg)

Figure 5. Factor graph optimization framework of our system. Constraints of factor graph on the keyframe maintenance include three local constraints and two global constraints.

Therefore, the Gaussian-Newton method can be used to minimize all cost functions to construct a maximum a posteriori estimation problem, to perform nonlinear optimization on the state vectors in the sliding window:

$$
\begin{gathered}
\min _{\mathcal{X}}\left\{\left\|r_{p}-\mathcal{J}_{p} \mathcal{X}\right\|^{2}+\sum_{k \in B}\left\|r_{B}\left(\hat{z}_{k+1}^{k}, \mathcal{X}\right)\right\|_{p_{i}}^{2}+\right. \\
\left.\sum_{(i, j) \in F} \rho\left(\left\|r_{f}\left(\hat{z}_{i}^{j}, \mathcal{X}\right)\right\|_{p_{i}}^{2}\right)+\sum_{(i, j) \in L} \rho\left(\left\|r_{l}\left(\hat{z}_{i}^{j}, \mathcal{X}\right)\right\|_{p_{i}}^{2}\right)+\sum d_{k}^{c}+\sum d_{k}^{p}\right\}
\end{gathered}
$$

where $\left\{r_{p}, \mathcal{J}_{p}\right\}$ contains the prior states after the marginalization in the sliding window, and $\mathcal{J}_{p}$ is the Jacobian matrix, $r_{B}\left(\hat{z}_{k+1}^{k}, \mathcal{X}\right)$ represents the IMU residuals, and $p_{i}$ is the IMU covariance matrix; $r_{f}\left(\hat{z}_{i}^{j}, \mathcal{X}\right)$ and $r_{l}\left(\hat{z}_{i}^{j}, \mathcal{X}\right)$ represent the re-projection errors of visual point and line features, $p_{i}$ is the visual covariance matrix, and $\rho$ represents Huber norm, with specific values as follows:

$$
\rho(e(s))=\left\{\begin{array}{cc}
\frac{1}{2} e_{1}(s)^{2} & e(s)=e_{1}(s),\left|e_{1}(s)\right| \leq \delta \\
\delta\left|e_{2}(s)\right|-\frac{1}{2} \delta^{2} & e(s)=e_{2}(s),\left|e_{2}(s)\right|>\delta
\end{array}\right.
$$

The specific meaning of each sensor cost function in Formula (6) is as follows.

# 4.2. IMU Factor 

The IMU state of the $k$ th frame and the $k+1$ th frame in the global coordinate system can be defined as:

$$
\begin{gathered}
x_{k}=\left[p_{b_{k}}^{G}, q_{b_{k}}^{G}, v_{b_{k}}^{G} b_{a k}, b_{g k}\right] \\
x_{k+1}=\left[p_{b_{k+1}}^{G}, q_{b_{k+1}}^{G}, v_{b_{k+1}}^{G} b_{a k+1}, b_{g k+1}\right]
\end{gathered}
$$

Take the IMU state of the $k$ th frame, $x_{k}$, as an example, which includes position $p_{b_{k}}^{G}$, rotation $q_{b_{k}}^{G}$, velocity $v_{b_{k}}^{G}$, accelerometer bias $b_{a k}$ and gyroscope bias $b_{g k}$.

Next, the IMU residual equation can be constructed, which is defined as:

$$
r_{B}\left(\xi_{k+1}^{k}, \mathcal{X}\right)=\left[\begin{array}{c}
r_{p} \\
r_{q} \\
r_{v} \\
r_{b a} \\
r_{b g}
\end{array}\right]=\left[\begin{array}{c}
R_{G}^{B_{b}}\left(p_{b_{k+1}}^{G}-p_{b_{k}}^{G}+\frac{1}{2} g \Delta t_{k}^{2}-v_{b_{k}}^{G} \Delta t_{k}\right)-\hat{p}_{k+1}^{k} \\
2\left[q_{b_{k}}^{G-1} \otimes q_{b_{k+1}}^{G} \otimes \hat{q}_{k+1}^{k-1}\right]_{x y z} \\
R_{G}^{B_{b}}\left(v_{k+1}^{G}+g \Delta t_{k}-v_{k}^{G}\right)-\hat{v}_{k+1}^{k} \\
b_{a k+1}-b_{a k} \\
b_{g k+1}-b_{g k}
\end{array}\right]
$$

where $\left[r_{p}, r_{q}, r_{v}, r_{b a}, r_{b g}\right]^{T}$ represents the observation residual of IMU state between two consecutive keyframes in the sliding window, including the residual of position, rotation, velocity, accelerometer bias and gyroscope bias, $R_{G}^{B_{b}}$ represents the pose conversion matrix of the $k$ th frame from the IMU coordinate system to GNSS global coordinate system, and $\left[\hat{p}_{k+1}^{k}, \hat{q}_{k+1}^{k}, \hat{v}_{k+1}^{k}\right]$ represents the IMU pre-integration value of two keyframes in the sliding window within $\Delta t_{k}$.

# 4.3. Visual Feature Factor 

The visual feature factor is essentially the re-projection error of the visual feature, that is, the difference between the theoretical value projected on the image plane and the actual observation value. In order to unify the coordinate system in Section 3.3, we provide the definition of re-projection error on the unit sphere instead of the generalized image plane. Specific schematic diagrams are shown in Figures 6 and 7.
![img-5.jpeg](img-5.jpeg)

Figure 6. Re-projection error of visual point features.
![img-6.jpeg](img-6.jpeg)

Figure 7. Re-projection error of visual line features.

# 4.3.1. Visual Point Feature Factor 

In this study, the visual feature factors are built with reference to VINS-Mono [5]. As shown in Figure 6, the re-projection error of visual point features can be defined as the difference between the projection point on the unit spherical surface and the observation value after distortion correction. Given the $i$ th normalized projection point $\hat{f}_{i}^{j}=\left[\hat{u}_{i}^{j}, \hat{v}_{i}^{j}, 1\right]^{T}$ and observation point $f_{i}^{j}=\left[u_{i}^{j}, v_{i}^{j}, 1\right]^{T}$ in the $j$ th frame, we use the first observation value $f_{i}^{j}=\left[u_{i 0}^{j}, v_{i 0}^{j}, 1\right]^{T}$ in the $j$ th frame to define the visual point feature factor as:

$$
\left\{\begin{array}{c}
r_{f}\left(\hat{z}_{i}^{j}, \mathcal{X}\right)=\left[\begin{array}{c}
\hat{u}_{i}^{j}-u_{i}^{j} \\
\hat{v}_{i}^{j}-v_{i}^{j}
\end{array}\right] \\
{\left[\begin{array}{c}
u_{i}^{j} \\
v_{i}^{j}
\end{array}\right]=R_{B}^{V}\left(R_{G}^{B_{i}}\left(R_{B_{0}}^{G}\left(R_{V}^{B} \frac{1}{\kappa_{i}}\left[\begin{array}{c}
u_{i 0}^{j} \\
v_{i 0}^{j}
\end{array}\right]+p_{V}^{B}\right)+p_{b_{0}}^{G}-p_{b_{i}}^{G}\right)-p_{V}^{B}}
\end{array}\right.
$$

where $R_{B}^{V}$ represents the external parameter matrix between camera and IMU, which is obtained by calibration, $R_{G}^{B_{i}}$ represents the pose conversion matrix from the IMU observation in the $j$ th frame to the global coordinate system, $R_{B_{0}}^{G}$ represents the pose conversion matrix from the global coordinate system to the initial IMU observation, $\kappa_{i}$ stands for the inverse depth of $f_{j}^{i}, p_{V}^{B}$ represents the displacement from the IMU coordinate system to the camera coordinate system. Finally, $p_{b_{0}}^{G}$ and $p_{b_{i}}^{G}$ represent the displacement of the first and the $i$ th IMU observation in the global coordinate system, respectively.

### 4.3.2. Visual Line Feature Factor

As shown in Figure 7, similar to the visual point feature, the definition of the reprojection error of the visual line feature is as follows: Given the characteristics of a visual line in space, the end point of a line segment is the center of the sphere to construct a unit sphere. Therefore, the reprojection error is the difference between the projection line on the unit sphere and the observed value. According to Equation (2), given the observed value of the characteristic factor of the ith line in the $j$ th frame in the camera coordinate system as $I_{c_{i}^{j}}=\left[n_{c_{i}^{j}}^{j}, v_{c_{i}^{j}}\right]^{T}$, the projection line is obtained by projecting it onto the unit sphere, and can be expressed as:

$$
\hat{I}_{c i}^{j}=\left[\begin{array}{c}
\hat{I}_{1} \\
\hat{I}_{2} \\
\hat{I}_{3}
\end{array}\right]=\mathrm{K} n_{c i}^{j} \in R^{6}
$$

where K is the camera internal reference projection matrix. It can be seen from Equation (12) that the spatial coordinates of the line features projected onto the unit sphere are only related to $n_{c}$. The two end points of the observation line are $a_{i}^{j}$ and $b_{i}^{j}$, then the re-projection error of the line feature can be expressed by the dotted distance from the two end points of the observation line feature to the projection line feature:

$$
\left\{\begin{aligned}
r_{l}\left(\hat{z}_{i}^{j}, \mathcal{X}\right)=\left[d\left(a_{i}^{j}, \hat{I}_{c i}^{j}\right), d\left(b_{i}^{j}, \hat{I}_{c i}^{j}\right)\right]^{T} \\
d\left(a_{i}^{j}, \hat{I}_{c i}^{j}\right) & =\frac{\left(a_{i}^{j}\right)^{T} \hat{I}_{c i}^{j}}{\sqrt{\hat{I}_{1}^{2}+\hat{I}_{2}^{2}}} \\
d\left(b_{i}^{j}, \hat{I}_{c i}^{j}\right) & =\frac{\left(b_{i}^{j}\right)^{T} \hat{I}_{c i}^{j}}{\sqrt{\hat{I}_{1}^{2}+\hat{I}_{2}^{2}}}
\end{aligned}\right.
$$

### 4.4. LiDAR Factor

As mentioned in Section 3.3, after the LiDAR-assisted monocular visual depth correlation, the VIO will provide the LiDAR with visual initial positional estimates to correct

the motion distortion of the LiDAR point cloud and improve the scan matching accuracy. The scanning matching error between adjacent keyframes of LiDAR involved in this study can be expressed by the distance from the feature point to the matched edge line and feature plane as:

$$
\left\{\begin{array}{c}
d_{k}^{e}=\frac{\left|\left(X_{(k+1, i)}^{e}-X_{(k, a)}^{e}\right) \times\left(X_{(k+1, i)}^{e}-X_{(k, b)}^{e}\right)\right|}{\left|X_{(k, a)}^{e}-X_{(k, b)}^{e}\right|} \\
\left(X_{(k+1, i)}^{p}-X_{(k, b)}^{p}\right) \\
d_{k}^{p}=\frac{\left(\left(X_{(k, a)}^{p}-X_{(k, b)}^{p}\right) \times\left(X_{(k, a)}^{p}-X_{(k, c)}^{p}\right)\right)}{\left|\left(X_{(k, a)}^{p}-X_{(k, b)}^{p}\right) \times\left(X_{(k, a)}^{p}-X_{(k, c)}^{p}\right)\right|}
\end{array}\right.
$$

where $X_{(k+1, i)}^{e}$ represents the edge feature point at the $k+1$ th time, $X_{(k, a)}^{e}$ and $X_{(k, b)}^{e}$ are the endpoint of the edge line matched with the feature point at the $k$ th time, $X_{(k+1, i)}^{p}$ represents the plane feature point at the $k+1$ th time, and the feature surface matched with it at the $k$ th time can be represented by three points $X_{(k, a)}^{p}, X_{(k, b)}^{p}$ and $X_{(k, c)}^{p}$.

# 4.5. GNSS Factor and Loop Factor 

When the carrier moves to a GNSS signal trusted environment, GNSS factors can be added to optimize with local sensors. The time interval of two frames of GNSS observations is $\Delta t$, and given the GNSS measurements $p_{k}^{G \tau}$ in the global frame and $p_{k}^{V \tau}$ representing the observation of LVIO in the global frame, the GNSS factor can be expressed by the following observation residuals:

$$
r_{G}\left(\hat{z}_{k+1}^{k}, \mathcal{X}\right)=p_{k}^{V \tau}-p_{k}^{G \tau}
$$

Different from the assumption in [14] that GNSS factors are added to the system only when the GNSS measurement covariance is smaller than the LVIO measurement covariance, we noticed that the accuracy of outdoor GNSS positioning results is much higher than the LVIO local positioning results. The covariance threshold size for judging whether to add GNSS factors has little impact on the positioning accuracy. Therefore, we present that once the GNSS signal is detected by the system, the GNSS factor is added to the factor graph. In this way, even if the mobile carrier enters the GNSS rejection environment (such as the indoor parking lot or tunnel), it can also provide a more accurate initial observation value after GNSS correction. The fusion strategy of GNSS and LVIO is shown in Figure 8.

Further, considering the possible overlap of the mobile carrier travel area, i.e., the mobile carrier travels to the same position again after a period of time, we also added a loopback detection link to establish the loopback constraint that exists between non-adjacent frames. Unlike introducing another sensor (GNSS) for global correction of the local sensor (LVIO), the loopback factor establishes the correlation between the current observed frames and the historical data by the local sensor itself to obtain a globally consistent estimate. The conditions for adding the loopback factor are similar to those of GNSS. Once the carrier motion trajectory is detected to travel to the environment passed by the history, the loop factor is added to the factor graph. By registering with the point cloud of the prior map, the historical trajectory is corrected, and the global pose estimation result with higher accuracy is obtained.

![img-7.jpeg](img-7.jpeg)

Figure 8. Fusion strategy of GNSS and LVIO. The initial rotation $R_{G}^{L}$ of LVIO in the local frame and the global frame is set to identity matrix. GNSS provides global constraints to LVIO to correct the global position of LVIO and update $R_{G}^{L}$, and the new $R_{G}^{L}$ is used for the next frame of LVIO.

# 5. Experimental Results 

### 5.1. Real-Time Performance

### 5.1.1. Indoor Environment

For evaluating the real-time performance of our algorithm, we randomly selected the MH_01_easy dataset for indoor experiments. Since the strategy of adding line feature constraints to the VIO subsystem of our algorithm is referenced to PL-VIO, the time consumption of several threads involving line features of PL-VIO and this algorithm is compared. As shown in Figure 9, the appropriate selection of hidden parameters and the least-squares-based geometric constraint matching strategy have positive effects on real-time performance. The time cost of the line feature extraction and matching process and the line feature tracking process of the proposed algorithm is about one-third that of similar algorithms.

The time consumption of the line feature matching process is shown in Figure 9a. In the period of $(110 \mathrm{~s}, 170 \mathrm{~s})$, the carrier passes through the well-lit factory wall duct area. The number of line features extracted by both algorithms increases, and the corresponding time cost of line feature matching also increases with the number of line features. However, unlike PL-VIO which is significantly affected by the increase in the number of line features, the line feature matching the process time of our algorithm remains relatively stable within 1 ms . The reason is that the number of invalid line features is reduced due to the geometric constraint-based line feature matching strategy, which improves the accuracy of line feature matching between the front and current frames of the image. In the time-consuming of line feature tracking process shown in Figure 9b, it can be seen that in the initial stage ( $0 \mathrm{~s}, 5 \mathrm{~s}$ ) of the visual subsystem, the line feature tracking process of the two systems takes longer. The reason is the UAV is at rest during this time and the VIO subsystem does not receive sufficient motion excitation, which leads to its incomplete initialization. After 5 seconds of initialization, the PL-VIO line feature tracking time remains stable at about 125 ms , while the time consumption of our algorithm is about $4 / 5$ less than that of PL-VIO, about 25 ms . It has a strong positive effect on the real-time performance of the fusion system in the actual operating environment.

Although as shown in Figure 9c, the time-consuming cost of the line feature residual optimization process increases by about 10 ms , the time-consuming of the line feature tracking process is significantly reduced. Thus, the proposed method leads to a decrease in the total time cost of the three line feature-related processes in the fusion system, which still has a better real-time performance overall than before the improvement.

![img-8.jpeg](img-8.jpeg)

Figure 9. Real-time comparison experiment of MH_01_easy dataset. (a) Line feature extraction and matching process. (b) Line feature tracking process. (c) Line feature residual optimization process.

# 5.1.2. Outdoor Environment 

Since the distribution characteristics of line features are different in indoor and outdoor environments, in order to fully evaluate the superior performance of this algorithm in terms of real-time, we selected the Hong Kong 0428 dataset for outdoor experiments. The experimental results are shown in Figure 10.

Different from the indoor environment, the outdoor environment has more complex conditions of light refraction and reflection, and the dynamic interference such as pedestrians and vehicles in the driving process of moving vehicles. The time consumption of the line feature matching process in the outdoor environment is shown in Figure 10a. It can be seen that the line feature matching time of PL-VIO in the outdoor environment is about 10 ms on average, and our algorithm still maintains the same good real-time characteristics as the indoor environment. In the line feature tracking process shown in Figure 10b, it can be seen that the line feature tracking process in the initialization phase $(0 \mathrm{~s}, 5 \mathrm{~s})$ of the visual subsystem is abnormally high for both systems. The same reason is that the VIO system is not provided sufficient motion excitation at the beginning of the vehicle stationary phase. It can be concluded that it is more difficult to match and track

visual line features in the outdoor environment, and the time consumed for line feature tracking rises about 3-4 times compared with the indoor environment. However, the time consumed by our algorithm is still greatly shortened compared with similar algorithms, leaving more time for the optimization of a multi-sensor fusion at the back-end.
![img-9.jpeg](img-9.jpeg)

Figure 10. Real-time comparison experiment of Hong Kong 0428 dataset. (a) Line feature extraction and matching process. (b) Line feature tracking process. (c) Line feature residual optimization process.

In addition, as shown in Figure 10c, the time-consuming cost of the line feature residual optimization process is not much different from that of PL-VIO. Combining the above three time-consuming threads, it can be proved that our algorithm can achieve better real-time performance in different environments.

# 5.2. Positioning Accuracy 

### 5.2.1. Indoor Environment

In this study, the EuROC dataset was used to compare and verify the positioning accuracy of each algorithm in the indoor environment. The experimental environment was in a factory with complex signal refraction and reflection conditions. LiDAR frequently fails in the experimental environment, so no comparison was made. The comparison of the point-line feature results extracted by PL-VIO and our algorithm in the experimental environment is shown in Figure 11.

![img-10.jpeg](img-10.jpeg)

Figure 11. Comparison of point-line feature extraction results in poor lighting conditions and weak texture environment. (a) Point-line feature extraction results of PL-VIO. (b) Point-line feature extraction results of our algorithm.

As seen in Figures 12 and 13 and Table 1, the introducing line features in the image frames to add additional feature constraints can reduce the positioning error of the system to some extent, especially in areas with dim light and poor textures. For example, during the ( $160 \mathrm{~s}, 240 \mathrm{~s}$ ) time, the UAV flight area is nearly full of darkness. Thus it is difficult for Harris corner point detection method to extract the corner points with large grayscale difference from the surrounding pixel blocks. The reduction in the number of effective feature points directly leads to poor feature tracking accuracy. Therefore, the absolute trajectory error of VINS-Mono based on point features is larger in this interval (as shown in Figure 13a). In contrast, PL-VIO based on point-line features and the present algorithm are less negatively affected by illumination, and the absolute trajectory error remains within 0.6 m . In a longitudinal comparison of similar algorithms based on point and line features, the accuracy of our algorithm is significantly improved over PL-VIO. These results are attributed to the high quality of matching by the geometric constraint strategy, which avoids the missegmentation of long-line features and then misclassification as invalid matches. The experimental results demonstrate the robustness and accuracy of this algorithm in the case of single system failure, which is important for localization in complex indoor environments.

Table 1. Motion estimation errors of each algorithm in indoor dataset.


![img-11.jpeg](img-11.jpeg)

Figure 12. Comparison of trajectory fitting curve of each algorithm in the indoor dataset. (a) Global trajectory fitting curve. (b) Details of local trajectory. (c) Details of local trajectory.
![img-12.jpeg](img-12.jpeg)

Figure 13. Comparison of positioning results of each algorithm in the indoor dataset. (a) APE_RMSE error fitting curve. (b) Comparison of index of absolute trajectory error.

5.2.2. Outdoor Environment

To evaluate the performance of the algorithm we conducted in the outdoor environment, the Hong Kong dataset was used for performance evaluation and it was compared with other similar advanced algorithms. The experimental equipment and environment are shown in Figure 14. The sensor models are as follows: the camera is BFLY-U3-23S6C-C, the LiDAR is HDL 32E Velodyne, IMU is Xsens Mti 10, and the GNSS receiver is u-blox M8T. In addition, we utilized the high-grade RTK GNSS/INS integrated navigation system, NovAtel SPAN-CPT, as the ground truth.
![img-13.jpeg](img-13.jpeg)

Figure 14. Experimental equipment and environment. (a) The experimental vehicle and sensors setup. (b) Image of experimental environment.

To verify the superior performance of each aspect of our system, we performed ablation experiments, constructed without GNSS global correction (*), without visual line features (\#), and our complete system (proposed), respectively. The experimental results are shown in Figures 15 and 16 and Table 2.

Table 2. Motion estimation errors of each algorithm on outdoor dataset.


![img-14.jpeg](img-14.jpeg)

Figure 15. Comparison of trajectory fitting curve of each algorithm in the indoor dataset. (a) Global trajectory fitting curve. (b) Details of local trajectory. (c) Details of local trajectory.
![img-15.jpeg](img-15.jpeg)

Figure 16. Comparison of positioning results of each algorithm on outdoor dataset. (a) APE_RMSE error fitting curve. (b) Comparison of index of absolute trajectory error.

From Figure 15, it can be seen that VIO and LIO, which are mainly based on a single sensor, each have different defects. First of all, VIO(VINS-Mono) is introduced. Before starting the movement, the moving carrier stopped at the roadside parking position for about 10 seconds. VIO was not given a large motion excitation during this period, which led to the VIO not being initialized properly. Secondly, the cumulative error caused by the scale uncertainty of the monocular camera increased significantly over time, and a large-scale estimation error was already generated at the second lap. Although the scale drift of LIO (LIO-SAM) is not large, it will immediately fail and keep restarting in the complex area of signal fold reflection. After LiDAR resumes operation, the translation and rotation of the current frame will be accumulated based on the positional estimation at the last frame that did not fail, resulting in the misjudgment of stopping the motion at the carrier motion to $(50 \mathrm{~m}, 150 \mathrm{~m})$. When the carrier moves to the corner, LIO re-estimates the position and attitude. It was misjudged that the carrier stopped at $(50 \mathrm{~m}, 150 \mathrm{~m})$ for a while and then began to turn, so it lost the estimated position and attitude for a period of time, which led to a large positioning error.

In a longitudinal comparison with the other LVIO system (LVI-SAM), we can conclude that our complete algorithm maintains a lower drift rate and localization integrity, which benefits from the extra constraint of line features and the global correction of GNSS. In conclusion, even in complex outdoor environments, our algorithm still outperforms other advanced algorithms.

# 5.3. Mapping Performance 

As a demonstration of the superiority of our algorithm in building maps, we compared the building results with other advanced algorithms on different datasets. The visual line feature extraction and map building results are shown in Figure 17. Compared with PL-VIO, our algorithm has a great improvement in the number of visual line features extracted, which is attributed to the improved line feature extraction strategy. In a factory environment with complex lighting conditions, the line features in the actual environment will look minutely curved due to the refraction of light. Due to the proper value of the threshold value $D$ of the density of homogeneous points, the angle tolerance of fitting pixels to approximate rectangles in this environment can be improved, thus increasing the number of line feature extraction. Further, the accuracy of the bit pose estimation is also substantially improved by the combination of the improved line feature extraction and tracking optimization strategies.
![img-16.jpeg](img-16.jpeg)

Figure 17. Comparison of visual line feature extraction mapping. (a) show the mapping of each subsystem before improvement, and (b) show our algorithm mapping.

Further, comparison of the LiDAR point cloud detail views is shown in Figure 18. The more accurate VIO pose estimation after the line features are added provides a more accurate initial value for LiDAR scan matching, and reduces a large number of point cloud mismatching. Comparison of global point cloud trajectories is shown in Figure 19.

The area marked by circles demonstrates that the data drift caused by cumulative errors is significantly reduced by adding a GNSS factor and loop factor to our algorithm.
![img-17.jpeg](img-17.jpeg)

Figure 18. Comparison of LiDAR point cloud map details. (a) show the mapping of each subsystem before improvement, and (b) show our algorithm mapping.
![img-18.jpeg](img-18.jpeg)

Figure 19. Comparison of global point cloud trajectory. (a) show the mapping of each subsystem before improvement, and (b) show our algorithm mapping.

# 6. Discussion 

Multi-sensor fusion positioning technology based on SLAM provides new opportunities for the high-precision positioning of mobile carriers. In this study, two problems that need to be further explored in the existing LVIO fusion system are proposed. The first problem is that LVIO system needs enough environmental feature information. According to the previous studies of Pumarola et al. [11] and Fu et al. [12], theoretically, the accuracy of the fusion system can be improved by increasing the constraint of visual line features. Huang et al. also proved that the average positioning error of the fusion system based on point-line feature can generally be improved, from the traditional $2.16 \%$ to $0.93 \%$ [18]. In this study, the steps of increasing visual line feature constraints are further optimized. The Monte Carlo method was used to select the appropriate scaling ratio and the density threshold of homogeneous points, which improves the angle tolerance of pixel fitting to line features. To a certain extent, it reduces the probability that short segments are wrongly judged as invalid features. According to the experiment of parameter selection in Section 3.1, compared with the indoor environment where the angle and translation of line features change little, the movement of line features between consecutive frames is more complicated in the outdoor environment. Therefore, the density threshold of homogeneous points needs to be lowered to reduce the probability that the valid line feature pairs are misjudged as invalid matches when turning sections. The results of outdoor real-time analysis shown in Section 5.1.2. show that the traditional method based on point-line features is difficult to match and track the visual line features in the outdoor environment,

which takes a long time. However, the time consumption of this algorithm maintained a low level, which is beneficial to leave more time for back-end fusion optimization.

To solve the problem of line feature mismatching during the movement of carriers, Zhou et al. established a constraint equation using the 6-DOF Plücker coordinates of line features to perform matching optimization [19]. However, this increases the computational complexity of the fusion system, which is inconsistent with the lightweight requirements of autonomous driving positioning. In this study, the link of line feature constraint matching is simplified, and the original 6-DOF parameters are replaced by 4-DOF which represents the movement of line features for optimization. Thus, it can reduce the computational complexity of the system and effectively improve the inter-frame matching accuracy of line features. To explore the superiority of the proposed algorithm in real-time and positioning accuracy, we compared the precision and the time-consuming of three processes related to line features of this algorithm with several similar advanced algorithms in different environments. The experimental results show that our optimization strategy based on front-end point-line features effectively achieves the positive balance between reducing time consumption and improving accuracy.

The second problem to be solved is the global optimization of LVIO local pose estimation results by introducing global constraints. To further improve the positioning accuracy of local sensors, Qin et al. proposed a GNSS and local sensor fusion method to construct GNSS residual factors to correct the cumulative error of VIO [25]. Further, we propose a factor graph based on Bayesian network, in which GNSS observations are added as global constraint factors. The accumulated errors of LVIO are corrected by using GNSS observations within 0.1 s interval from LVIO keyframes as global constraint. In this study, it is proved that GNSS global constraint factor can effectively correct LVIO positioning error in the outdoor environment. It should be noted that since the coordinate of the current frame of LVIO is calculated from the coordinate of the previous frame, longterm observation or long moving distance will lead to more serious data drift. However, the GNSS observations are in the global coordinate, so long-term observation is not related to the data drift. Therefore, we can reasonably speculate that the longer the algorithm runs, the more obvious the correction effect of GNSS on LVIO will be. More comprehensively, LVIO will continue local positioning in GNSS rejection environment, so the positioning continuity of mobile carriers in different environments can be effectively guaranteed.

# 7. Conclusions 

In this study, a LiDAR-Visual-Inertial Odometry based on optimized visual point-line features is proposed, taking advantage of the heterogeneous complementary characteristics of multiple sensors. First, a visual line feature extraction and matching optimization method is proposed. By improving the line feature extraction in the scale space and selecting the appropriate scaling ratio and same-sex point density threshold, the number of line features extracted in the light complex environment is largely improved to provide richer feature information for the front-end. Meanwhile, the original 6-DOF parameter optimization problem is further improved to a 4-DOF parameter optimization problem by using a least squares-based line feature constrained matching strategy. The complexity of the fusion system is reduced, and more accurate visual pose estimation is effectively accomplished. Second, the LiDAR point cloud is projected into the visual coordinates for depth correlation. Meanwhile, the initial pose estimation provided by the optimized VIO is used to help LiDAR scan matching. Finally, a factor graph method based on Bayesian networks is established. Two global constraint factors are added to the factor graph framework to constrain LVIO globally, which are the global constraint of GNSS factors from external sensors and the loop factor constraint of local sensors. The experimental results show that the algorithm can achieve real-time attitude estimation with good localization and mapping accuracy in different environments.

In the future, we will further improve and refine our work in the following aspects. First, the point cloud alignment algorithm of the loop factor in this study utilizes the

traditional ICP algorithm, which is time-consuming to perform the nearest domain search using the KD tree. Thus, we will consider the improvement of the point cloud alignment algorithm next. Second, the inclusion of the GNSS factor in this study only utilizes the GNSS pseudo range single point positioning result. Although it is relatively simple and feasible on the vehicle platform with only one GNSS receiver, there is still room for improvement in the positioning accuracy of GNSS. A more accurate correction of LVIO by using higher accuracy RTK positioning results will be considered in the next step. Finally, since our proposed fusion system consists of two subsystems with high runtime computational resource requirements, we will work on reducing the resource occupation rate of the algorithm. Further, we will evaluate the positioning accuracy of the algorithm on vehicles with limited computing resources.

Author Contributions: Conceptualization, Z.Z., C.S., H.Z. and X.L.; methodology, X.H.; software, X.H.; validation, S.P. and L.D.; formal analysis, X.H.; investigation, W.G. and X.H.; resources, S.P., W.G. and X.H.; writing-original draft preparation, X.H.; writing-review and editing, W.G. and X.H.; supervision, S.P. and W.G.; project administration, W.G.; funding acquisition, S.P. All authors have read and agreed to the published version of the manuscript.

Funding: This research study was funded by the Fundamental Research Funds for the Central Universities (2242021R41134) and the Research Fund of the Ministry of Education of China and China Mobile (MCM20200J01).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
