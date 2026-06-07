# 基于迭代阈值分割的星载 SAR 洪水区域快速提取 

苗 添, 曾虹程*，王 贺，陈 杰<br>(北京航空航天大学电子信息工程学院, 北京 100191)


#### Abstract

摘 要：基于星载合成孔径雷达（synthetic aperture radar，SAR）的洪水区域提取可对洪灾信息进行高效提取。然而，传统提取方法往往时间复杂度较高，严重影响了洪灾区域获取的时效性。基于改进迭代阈值分割原理，本文提出了一种星载 SAR 图像洪水区域快速提取方法。首先，对预处理后的 SAR 图像进行高新拟合再抽样，抑制 SAR 图像直方图并雷点的影响。其次，利用迭代阈值算法进行水体提取，并基于形态学滤波对噪声进行抑制。最后，对已识别的水体区域开展变化检测，实现洪灾区域的提取。基于 2020 年 7 月郡阳湖流域特大洪灾前后的哨兵-1 SAR 图像，本文开展了洪水区域提取对比试验。试验结果表明，该方法可在保证洪水区域提取精度的同时，显著提升处理效率。


关键词：合成孔径雷达；迭代阈值分割；变化检测；洪水区域提取
中图分类号：TP 751.1 文献标志码：A DOI:10.12305/j.issn. 1001-506X. 2022.09.08

## A fast extraction method of flood areas based on iterative threshold segmentation using spaceborne SAR data

MIAO Tian, ZENG Hongcheng*, WANG He, CHEN Jie<br>(School of Electronics and Information Engineering, Beihang University, Beijing 100191, China)


#### Abstract

Flood area extraction method based on spaceborne synthetic aperture radar（SAR）can extract flood area with high precision. However, traditional flood area extraction methods are time consuming, which will seriously affect the time effectiveness of flood area extraction. In this paper, an improved iterative threshold segmentation method for fast extraction of flood area is proposed, using spaceborne SAR images. Firstly, the preprocessed SAR image is resampled by Gaussian fitting to suppress the influence of abnormal points in the histogram of SAR image. Then, the water body is extracted by the iterative threshold segmentation method, and the noise suppression is performed using the morphological filtering. Finally, change detection is carried out to obtain the flood area, based on the extracted water body. Based on the Sentinel-1 SAR images of Poyang Lake before and after the flood in July 2020, a comparative experiment of flood area extraction is carried out in this paper. Experimental results shows that the method can extract the flood area quickly with high accuracy.

Keywords: synthetic aperture radar (SAR) ; iterative threshold segmentation; change detection; flood area extraction


## 0 引 言

洪涝灾害以其发生的频率高、影响的范围广、造成的破坏强等特点一直受到科研人员的高度关注 ${ }^{[1]}$ 。由于洪灾成

因复杂，对其进行准确预测较为困难。因此，在洪灾发生后，及时地进行洪灾区域提取对救灾工作有着重要的意义。

目前，遥感卫星技术被广泛应用于洪灾监测中。其中，光学卫星的图像直观、分辨率高，但受观测区域的气象条件

[^0]
[^0]:    收稿日期:2020-10-16; 修回日期:2021-11-23; 网络优先出版日期:2022-03-01。
    网络优先出版地址: https://kns. cnki. net/kcms/detail/11.2422.TN. 20220301. 1632. 014. html

    * 通讯作者。

    引用格式：苗添，曾虹程，王贺，等. 基于迭代阈值分割的星载 SAR 洪水区域快速提取[J]. 系统工程与电子技术, 2022, 44(9): 2760-2768.

    Reference format: MIAO T, ZENG H C, WANG H, et al. A fast extraction method of flood areas based on iterative threshold segmentation using spaceborne SAR data[J]. Systems Engineering and Electronics, 2022, 44(9): 2760-2768.

影响较大，在复杂的气象条件下难以胜任检测工作，且仅能在白天工作。而星载合成孔径雷达（synthetic aperture radar，SAR）凭借其全天时、全天候工作，分辨率高，不受昼夜、天气影响，检测能力强、范围广等独特的优势，在近些年来被广泛应用到对地环境监测中 ${ }^{[2]}$ 。基于上述的优点，本文开展了基于星载 SAR 图像的洪水灾害检测处理研究。

利用星载 SAR 进行洪水区域提取主要是通过水体提取和图像变化检测来实现的。当前，较为常见的洪水区域提取方法是：利用 Otsu 阈值分割算法 ${ }^{[3]}$ 、K-Means 聚类算法 ${ }^{[4]}$ 等图像分割或图像分类方式提取灾前与灾后水体，再通过相减变化检测来提取洪灾区域。这类方法效果稳定、可靠，提取的准确率较高，但也存在局限；由于需要进行遍历或多次迭代，其耗时都相对较长，检测效率较低。针对这一问题，本文提出一种基于改进迭代阈值分割的 SAR 图像洪水区域快速提取方法，可在保持较高准确率的同时显著缩短算法的处理时间，提升洪灾区域提取的效率。

## 1 基于 SAR 图像的洪灾区域传统提取方法

目前，有许多学者对遥感技术在洪灾检测中的应用进行研究，并取得了一些成果。由于光学卫星成像易受天气及水汽云层的影响，因此多采用 SAR 图像或光学图像与 SAR 图像融合的方式进行水体提取与洪灾区域检测。

对 SAR 来说，由于不同地表的粗糙度相差较大，雷达信号在其上的散射方式不同，导致不同地表对应的后向散射系数不同。雷达信号在水体上以镜面反射为主，而在陆地上以散射为主。根据这一点，可利用图像分割或图像分类进行水体提取，再通过图像变化检测提取洪灾区域。传统的水体提取方法有 Otsu 阈值分割算法 ${ }^{[5]}$ 、最大熵阈值分割算法 ${ }^{[6]}$ 、K-Means 算法、期望最大化（expectation-maximum，EM）算法 ${ }^{[7-8]}$ 等方法。近年来，随着深度学习等领域的发展，U 型网络（U-Net） ${ }^{[9]}$ 、全卷积网络（fully convolutional networks, FCN） ${ }^{[10]}$ 等深度学习模型也在 SAR 的水体提取中得到了应用。

Otsu 阈值分割算法在水体提取中的应用较为普遍。其原理为寻找阈值，使该阈值分割所得的两部分图像的类间方差达到最大值 ${ }^{[11]}$ ：

$$
\sigma_{D}^{2}=p_{1} \times\left(\bar{x}_{1}-\bar{x}\right)^{2}+p_{2} \times\left(\bar{x}_{2}-\bar{x}\right)^{2}=p_{1} \times p_{2} \times\left(\bar{x}_{1}-\bar{x}_{2}\right)^{2}
$$

式中： $\sigma_{D}^{2}$ 为两部分图像的类间方差； $p_{1} 、 p_{2}$ 分别为阈值分割两部分图像所占比例； $\bar{x}_{1} 、 \bar{x}_{2} 、 \bar{x}$ 分别为两部分图像和整体图像像素值的均值。这一方法比较成熟，也得到了较多应用，如孙亚勇等 ${ }^{[12]}$ 利用改进的 Otsu 阈值分割法对 2015 年 7、8月份的缅甸伊洛瓦底江下游洪水影响区域进行研究；郭欣等 ${ }^{[13]}$ 利用哨兵-1A 卫星数据，采用 Otsu 阈值分割算法对 2017 年 6 月湖南省宁乡市遭受洪涝灾害的地区进行研究。其算法均通过实验对比验证了准确性与可行性。Otsu阈值分割算法原理简单、效果稳定，但在使用时需要对所有可能的阈值取值进行一次遍历，时间复杂度较高。此外，对

于 SAR 图像而言，单纯地以后向散射系数值为参考依据，会受到山体阴影等的影响，容易对部分地区造成误判，造成准确率下降。

最大熵阈值分割算法与 Otsu 阈值分割算法原理类似，区别在于其阈值取值为使两部分图像的总熵值达到最大值时的值：

$$
h_{r}=h_{1}+h_{2}=-\sum_{i=1}^{n} p_{1_{i}} \times \log p_{1_{i}}-\sum_{i=-n-1}^{N} p_{2_{i}} \times \log p_{2_{i}}
$$

式中： $h_{i}$ 为图像的总熵值； $h_{1} 、 h_{2}$ 分别代表阈值分割后两部分图像的熵值； $p_{1} 、 p_{2}$ 分别为两部分图像中各个像素值所占比例； $n$ 为阈值对应的像素值等级； $N$ 为像素值等级个数。利用最大熵阈值分割算法提取水体，同样存在时间复杂度高、易受山体阴影影响等缺点。

在水体提取中，常用的图像分类方法有 K-Means 算法和 EM 算法。K-Means 算法通过多次迭代，修正聚类中心，将原始数据分为若干不同类别，直到准则函数达到最优值，从而实现图像的分类 ${ }^{[14]}$ 。EM 算法的原理是在概率模型中找到参数最大似然估计或最大后验估计的算法。通过多次迭代，实现对目标的分类。

$$
I(\theta)=\log L(\theta)=\log P(X \mid \theta)=\log \sum_{i} P(X, Y \mid \theta)
$$

式中： $\theta$ 为待估测值； $X$ 为观测变量值； $Y$ 为未知变量值； $L(\theta)$为似然函数； $I(\theta)$ 为对似然函数取对数的结果。其原理如下：通过多次迭代，改变 $\theta$ ，使似然函数最大化，优化分类结果。随着机器学习的发展，这两种非监督性学习在 SAR 图像水体提取中也得到了较多应用，但是由于需要通过多次迭代来进行提取，因而所需时间往往比阈值分割法更长。

近年来，随着相关理论与技术的完善，深度学习在 SAR 图像处理中得到了广泛应用。在水体提取中，研究者们根据 SAR 图像自身的特点对经典的深度学习分割模型进行改进，提出了针对 SAR 图像的基于 U-Net、FCN-8S、双边分割网络（bilateral segmentation network，BiSeNet）等分割网络的水体提取算法，取得了较好的结果。戴牧宸等 ${ }^{[15]}$根据 SAR 图像特点，对传统的双边网络进行改进，减少了原网络中空间路径的卷积层数，采用深度残差网络（deep residual network, ResNet) 作为上下文路径骨干网络对 SAR 图像进行海陆分割，实验表明，其分割效果较好，且泛化能力较强。Shamsolmoali 等 ${ }^{[16]}$ 基于常规的 U-Net 网络，针对 SAR 图像的特点进行改进，将残差网络加入传统的 U-Net 之中。在上下采样路径中，加入紧密连接的残差网络块，对不同尺度的上下文信息进行聚合。实验表明，该方法较传统的 U-Net 网络而言，提取准确率得到了提高。

此外，相关学者还基于 SAR 图像与光学图像融合结果开展洪灾区域提取研究 ${ }^{[17-18]}$ ，取得了较好的效果，但超出本文研究范围，不再详细说明。

由于洪水检测的特殊性，对算法的时效性和准确性均有较高的要求，上述算法均需较长时间。针对这一问题，本

文将开展基于星载 SAR 图像的洪灾区域快速提取方法研究。

## 2 基于改进迭代阈值分割的 SAR 图像洪水区域快速提取方法

迭代阈值分割算法在光学图像处理中得到了较多的应用，但在 SAR 图像处理中应用较少。由于 SAR 在成像过程中会受到相干斑噪声及各类畸变的影响，因此部分像素点会受到影响，像素值因此被改变，进而影响到阈值的选取。为了减少异常点对提取效果的影响，需结合 SAR图像特点，对噪声进行抑制。基于迭代阈值分割算法的原理及 SAR 图像处理的相关理论，对迭代阈值分割算法进行改进，以实现对 SAR 图像洪水区域的快速提取，如图 1所示。
![img-0.jpeg](img-0.jpeg)

图1 基于迭代阈值分割算法的 SAR 图像洪水区域提取流程图
Fig. 1 Flow chart of flood area extraction of SAR image based on iterative threshold segmentation algorithm

首先，对灾前和灾后的 SAR 图像进行预处理，具体包括裁剪、多视处理 ${ }^{[18]}$ 、辐射校正 ${ }^{[20]}$ 、几何校正 ${ }^{[21]}$ ，保证 SAR图像的相干斑噪声、辐射畸变、几何畸变等得到抑制；在此基础上，对预处理后的数据进行分级、高斯拟合、抽样，对异常点带来的影响进行进一步抑制；其次，利用迭代阈值分割算法计算所需阈值，实现对 SAR 图像进行分割处理；然后，开展形态学滤波处理，抑制图像噪声对水体识别带来的影响；最后，基于相减变化检测，实现洪灾区域的有效提取。

## 2. 1 预处理

阈值分割是完全根据图像像素值进行分割的一项技术，因此图像中存在的各类畸变及异常点都会对分割结果带来影响。SAR 在成像过程中会受到各类畸变的影响而产生部分异常点，进而影响后续水体的提取及洪灾区域的检测。因此，在水体提取和图像变化检测之前，需要对原始图像进行预处理，以达到抑制各类噪声与畸变的目的。预处理的流程如图2所示。
![img-1.jpeg](img-1.jpeg)

Fig. 2 Preprocessing flow chart
对灾前与灾后图像进行裁剪，使洪灾区域位于图像中央，方便观测的同时减小图像大小，加快处理速率，如图3所示。再依次对图像进行多视处理、辐射校正、几何校正，分别对图像的相干斑噪声、辐射畸变、几何畸变进行抑制，得到预处理后的结果。
![img-2.jpeg](img-2.jpeg)

图3 原始图像与裁剪后的图像的范围
Fig. 3 Range of the original image and the cropped image

## 2. 2 改进的迭代阈值分割算法

预处理结束之后，基于迭代阈值分割算法原理，分别对灾前和灾后研究区域的 SAR 图像进行水体提取。迭代阈值分割算法是基于无限逼近思想提出的一种阈值分割方法。最初，由 Ridler 和 Calvard ${ }^{[22]}$ 提出一种阈值计算框架，通过多次选择不断优化阈值，以达到最佳分割效果，如图 4 所示。
![img-3.jpeg](img-3.jpeg)

图4 用于迭代阈值选择的示意图图像处理器
Fig. 4 Schematic image processor for iterative threshold selection
图4中，比较器对输入图像像素与当前阈值进行比较。选择器根据比较器的结果向转换器发送信号，转换器在接受信号后，将对应的输入图像像素点转换为背景图像像素点或目标图像像素点；阈值平均模块负责分别计算两个区域的阈值并进行平均得到新的阈值。当图像中的每个像素点都经过一次处理后，即完成一次迭代。通过多次迭代，当阈值不再变化或两次阈值的差值小于规定值时，即完成迭代阈值分割。

Trussel ${ }^{[23]}$ 对该计算框架进行数学归纳，将阈值计算公式归纳为

$$
T_{k=1}=\frac{\sum_{h=1}^{T_{k}} b \cdot n(b)}{2 \sum_{k=1}^{T_{k}} n(b)}+\frac{\sum_{h=T_{k+1}}^{n} b \cdot n(b)}{2 \sum_{k=1}^{T_{k}} n(b)}
$$

式中： $T_{k}$ 表示第 $k$ 次迭代的阈值； $b$ 表示灰度等级； $n(b)$ 表示对应灰度等级的像素点个数。Magid 等 ${ }^{[24]}$ 又对 Trussel 的归纳进行了证明。

假设阈值 $T$ 满足：

$$
T=\frac{A+B}{2}
$$

式中： $A 、 B$ 分别为背景部分和目标部分的某一特殊数学表示。定义误差函数 $e^{2}$ ：

$$
e^{2}=\int_{a}^{T}(i-A)^{2} h(i) \mathrm{d} i+\int_{a}^{N}(B-i)^{2} h(i) \mathrm{d} i
$$

式中： $i$ 为各个像素点的灰度值； $h(i)$ 为每个像素值等级所占比例。为使误差函数最小，对其求导，得

$$
\begin{gathered}
\frac{\mathrm{d} e^{2}}{\mathrm{~d} A}=0.5\left[\left(\frac{A+B}{2}\right)-A\right]^{2} h\left(\frac{A+B}{2}\right)+ \\
\int_{0}^{\frac{A+B}{2}}-2(i-A) h(i) \mathrm{d} i- \\
0.5\left[\left(\frac{A+B}{2}\right)-B\right]^{2} h\left(\frac{A+B}{2}\right)=0
\end{gathered}
$$

计算可得

$$
A=\frac{\int_{0}^{T} i \cdot h(i) \mathrm{d} i}{\int_{0}^{T} h(i) \mathrm{d} i}=\mu_{0}
$$

式中： $\mu_{0}$ 表示背景部分图像的平均灰度等级。同理，可得

$$
B=\mu_{1}
$$

式中： $\mu_{1}$ 表示目标部分图像的平均灰度等级。至此，迭代阈值分割算法的证明完成。

迭代阈值分割算法通过多次迭代不断优化阈值，当相邻两次阈值相同或其差值小到预定范围时，确定最后一次迭代的结果为最终阈值。迭代阈值分割算法流程图如图5所示。
![img-4.jpeg](img-4.jpeg)

图5 迭代阈值分割算法流程图
Fig. 5 Flow chart of iterative threshold segmentation algorithm
如图5所示，其计算流程如下：将高斯拟合并采样后的数据输入，将初始阈值 $t_{1}$ 设置为所有像素点的均值，并进行初次分割。在分割后，分别计算背景部分与目标部分的平均像素值，并将二者的平均值作为新的阈值 $t_{2}$ ，比较 $t_{1}$ 与 $t_{2}$ ，当二者不相等时，继续迭代，当二者相等时，完成阈值的计算。

这一算法对于像素值呈双峰状分布的图像有良好的分割效果。常见的 Otsu 阈值分割算法和最大熵阈值分割算法由于需要对所有像素等级进行遍历，因此其时间复杂度较高，采用常规方法实现上述两种算法，复杂度为 $O\left(n^{2}\right)$ 。而迭代阈值分割算法不需要对所有像素值进行遍历，仅通过数次迭代即可达到较好的分割效果，计算速度相对更快，效率更高。

在进行 SAR 图像水体提取时，由外界影响导致的异常点往往会影响提取效果，针对这一问题，提出一种改进的迭代阈值分割算法。由于水体的后向散射系数较低，陆地的后向散射系数较高，因此在理想状态下，包含较大区域水体的 SAR 图像后向散射系数分布为双峰状，当山体阴影影响较大时，后向散射系数的分布会产生畸变，使个别等级的像素点个数异常。针对 SAR 图像自身易受山体阴影影响、存在相干斑噪声等干扰的问题，结合 SAR 图像中像素值的分布特征，可先对 SAR 图像的像素值进行分级量化，对量化后的数据进行拟合再抽样，对该类畸变进行抑制。之后，利用抽样所得数据进行迭代阈值分割，最后再进行形态学滤波，对噪点进行抑制。其流程如图6所示。
![img-5.jpeg](img-5.jpeg)

图6 改进的迭代阈值分割算法流程图
Fig. 6 Flow chart of improved iterative threshold segmentation algorithm
具体步骤如下：
首先，将预处理后的 SAR 图像中每个像素点的像素值转化为分贝形式：

$$
y_{i}=10 \lg x_{i}
$$

式中： $x_{i}$ 为原始像素点的像素值； $y_{i}$ 为转化后 dB 图像对应像素点的值。对转化后图像的像素点值进行分级、量化，分为 $N$ 个等级，并统计每个等级的像素点个数。之后，对其进行拟合。目前，在变化检测技术发展过程中，基于参数模型的方法应用较广。常用的模型有高斯模型 ${ }^{[25]}$ 、广义高斯模型 ${ }^{[26]}$ 、瑞利-高斯模型等 ${ }^{[27]}$ 。考虑到高斯分布的灵活性和稳定性，且多种涉及被动传感器的数据分布模型均为高斯模型或广义高斯模型，本文中的 SAR 图像像素值分布图采用高斯函数进行拟合，本文选用高斯函数对数据进行拟合，拟合函数如下：

$$
f(x)=\sum_{k=1}^{N} a_{k} \cdot \mathrm{e}^{\frac{x-\bar{b}_{k}^{2}}{c_{k}}}
$$

式中： $f(x)$ 为高斯拟合函数； $x$ 为原始的离散数据； $a_{k} 、 b_{k} 、 c_{k}$为高斯函数中的常量； $N$ 为拟合阶数。依据拟合情况调整拟合阶数，以达到最优拟合效果。完成拟合后，进行抽样，将抽样结果存人 $N \times 1$ 的一维矩阵之中。然后，再对抽样结果进行迭代阈值分割。

迭代阈值分割算法的总体思路为：首先设置初始阈值，再不断对其进行调整、迭代，每一次调整的输入参数为上一次迭代中得到的结果，经过数次迭代之后，最后产生一个理想的阈值。

其算法实现步骤如下：
首先，将图片中的像素点依据其幅值进行排序，将初始阈值设置为所有像素点像素值的平均值 $t_{1}$ ：

$$
t_{1}=\sum_{i=1}^{N} p_{i} \cdot y_{i}=\sum_{i=1}^{N} p_{i} \cdot 10 \lg x_{i}
$$

然后，按照初始阈值 $t_{1}$ 将原始图像分成 1、2 两部分，分别计算两部分的后向散射系数差值的平均值：

$$
\begin{aligned}
& \dot{y}_{1}=\sum_{i=1}^{n_{1}} p_{i} \cdot y_{i}=\sum_{i=1}^{n_{2}} p_{i} \cdot 10 \lg x_{i} \\
& \dot{y}_{2}=\sum_{i=1}^{n_{2}} p_{i} \cdot y_{i}=\sum_{i=1,2,3}^{n_{3}} p_{i} \cdot 10 \lg x_{i}
\end{aligned}
$$

式中： $y_{i}$ 代表像素点的值； $x_{i}$ 为未转化前像素点的值； $p_{i}$ 表示其对应的概率； $n_{1}$ 表示阈值对应的像素等级。

接着将二者的平均值作为新的阈值 $t_{2}$ ：

$$
t_{2}=\frac{\dot{y}_{1}+\dot{y}_{2}}{2}
$$

对新的阈值与之前计算的阈值进行对比。若 $t_{2}$ 与 $t_{1}$ 的值相同，则 $t_{2}$ 为所求阈值；若不相同，则继续计算，不断迭代，直至相等或两次阈值的差值小于设定值时，最后一次迭代的阈值即为所求阈值 $t$ 。根据阈值，将原图像转化为二值图像。所得二值图像即为洪水区域的提取结果：

$$
g\left(y_{i}\right)=\left\{\begin{array}{l}
0, y_{i} \geqslant t \\
255, y_{i}<t
\end{array}\right.
$$

式中： $y_{i}$ 为原始像素值； $t$ 为阈值； $g\left(y_{i}\right)$ 为处理后的像素值。

### 2.3 形态学滤波与洪水区域提取

由于阈值分割法在处理时会忽视图像中蕴含的空间信息，因此部分没有得到完全抑制的异常点会给算法的判断带来影响，从而产生离散的噪点。针对这一问题，在完成水体初步提取后，采用形态学滤波对噪点进行抑制 ${ }^{[28]}$ 。由于噪点分布较为分散，为了减少形态学滤波对水体提取效果的影响，尽量选择尺寸较小的处理元素进行处理。本文中，选取尺寸为 $3 \times 3$ 的矩形进行形态学滤波。先进行腐蚀运算，再进行膨胀运算。腐蚀运算以处理单元的中心点为锚点，在原图像中移动处理单元，遍历图像的每一个像素。取结构元素覆盖下的原图对应区域内的所有像素的最小值，用这个最小值替换当前像素值，得到结果；膨胀运算与腐蚀运算相反，取结构元素覆盖下的原图对应区域内的所有像素的最大值，用最大值替换当前像素值，得到结果。经过形态学滤波，图像的噪声得到抑制，灾前与灾后的水体得到提取。

洪水区域提取的最后一步，对灾前、灾后图像进行变化检测。在之前的处理中，实现了对灾前与灾后水体的分别提取。在此基础上，利用相减变化检测可得到灾后相比灾前扩张的水体部分，此部分即为洪灾区域。通过先提取水体再进行变化检测的方式，可抑制零星噪点对变化检测结果的影响。具体流程为：利用灾后水体提取图像减去灾前水体提取图像，对应相随点值相减。对于未变化地区，相减后的结果为 0 ，对于遭受洪涝灾害的地区，相减后结果为 255 。所得二值图像即为遭受洪灾区域的提取结果。

## 3 实验结果与分析

### 3.1 实验数据

2020年7月，鄱阳湖流域发生特大洪水，给当地群众的生命财产安全带来了严重威胁。本文基于星载 SAR 图像对 2020 年 7 月鄱阳湖流域的洪水进行研究。本文选用欧空局哨兵-1卫星的数据进行相关研究。选用的 SAR 图像

为 Level-1 级别，干涉宽幅（interferometric wide swath， IW）模式、地距多视影像（ground range detected，GRD）类型的单极化成像。本次使用的数据信息如表1所示。

表1 原始图像数据信息
Table 1 Original image data information


## 3.2 实验结果

经过预处理的图像如图7所示。
![img-6.jpeg](img-6.jpeg)
(a) 数据1预处理后的SAR图像
(b) Preprocessed SAR image of data 1
![img-7.jpeg](img-7.jpeg)
(b) 数据2预处理后的SAR图像
(c) Preprocessed SAR image of data 2
![img-8.jpeg](img-8.jpeg)
(c) 数据3预处理后的SAR图像
(c) Preprocessed SAR image of data 3

图7 预处理后的 SAR 图像
Fig. 7 Preprocessed SAR image

提取预处理后 SAR 图像像素点数据，按照其像素值大小，均匀分为 500 个等级，并统计每个等级像素点个数。之后利用高斯分布对数据进行拟合，对拟合效果进行评估。分别计算不同阶数拟合函数的拟合系数与均方根误差 （root mean square error, RMSE），如图8所示。
![img-9.jpeg](img-9.jpeg)
(a) 不同阶数高斯拟合的拟合系数
(a) Fitting coefficients of different orders of Gaussian fitting
![img-10.jpeg](img-10.jpeg)
(b) 不同阶数高斯拟合的RMSE
(b) RMSE of different orders of Gaussian fitting
$\rightarrow$ ：数据 $1 ; \rightarrow$ ：数据 $2 ; \rightarrow$ ：数据3。
图8 不同阶数高斯拟合的效果
Fig. 8 Effect of different orders of Gaussian fitting
由图8可知，数据1与数据3应采用六阶高斯函数，数据2采用五阶高斯函数。高斯拟合后的结果如图9所示。常量取值如表2所示。
![img-11.jpeg](img-11.jpeg)

像素值等级
(a) 数据1原始数据与拟合结果
（a）Original data and fitting results of data 1
![img-12.jpeg](img-12.jpeg)
(b) 数据2原始数据与拟合结果
(b) Original data and fitting results of data 2
![img-13.jpeg](img-13.jpeg)
(c) 数据3原始数据与拟合结果
(c) Original data and fitting results of data 3
：原始数据；一：高斯拟合曲线。
图9 原始数据与拟合结果
Fig. 9 Original data and fitting results

表2 高斯拟合函数参数
Table 2 Parameters of Gaussian fitting function


利用迭代阈值分割算法分别计算 3 幅图像的阈值，计算结果如下：2019年7月20日的 SAR 图像阈值等级为

119，图像中对应像素点的值为 $-16.18 \mathrm{~dB} ; 2020$ 年 3 月 16日的 SAR 图像阈值等级为 109 ，图像中对应像素点的值为

$-16.07 \mathrm{~dB} ; 2020$ 年 7 月 14 日的 SAR 图像阈值等级为 122 ，图像中对应像素点的值为 $-15.36 \mathrm{~dB}$ 。依据阈值对图像进行分割，得到初步提取的结果，再对其进行形态学滤波，滤波前后结果如图 10 所示。
![img-14.jpeg](img-14.jpeg)
(a) 数据1水体提取结果
（a）Water area extraction of data 1
![img-15.jpeg](img-15.jpeg)
(c) 数据2水体提取结果
(c) Water area extraction of data 2
![img-16.jpeg](img-16.jpeg)
(e) 数据3水体提取结果
(e) Water area extraction of data 3
![img-17.jpeg](img-17.jpeg)
(b) 形态学滤波后数据1水体提取结果
(b) Water area extraction of data 1 after morphological filtering
![img-18.jpeg](img-18.jpeg)
(d) 形态学滤波后数据2水体提取结果
(d) Water area extraction of data 2 after morphological filtering
![img-19.jpeg](img-19.jpeg)
(f) 形态学滤波后数据3水体提取结果
(f) Water area extraction of data 3 after morphological filtering

图10 形态学滤波前后水体提取结果
Fig. 10 Water area extraction before and after morphological filtering
对提取水体后的结果进行统计：数据 1 的 SAR 图像中，提取水体所占比例为 $23.31 \%$ ；数据 2 的 SAR 图像中，提取水体所占比例为 $18.45 \%$ ；数据 3 的 SAR 图像中，提取水体所占比例为 $27.81 \%$ 。与数据 2 相比，鄱阳湖流域的水体面积在 7 月增加了 $50.73 \%$ ；即使与数据 3 ，即 2019 年同期相比，鄱阳湖流域的水体面积也增加了 $19.30 \%$ 。

分别对数据 3 与数据 2 、数据 3 与数据 1 的提取结果进行相减变化检测，并将结果与灾前、灾后叠加形成的 RGB (red green blue) 图像进行对比，其结果如图 11 所示。
![img-20.jpeg](img-20.jpeg)
(a) 洪灾区域结果
(a) Extraction of the flood area
![img-21.jpeg](img-21.jpeg)
(c) 洪灾区域RGB合成图像
(c) RGB composite image of flood area
![img-22.jpeg](img-22.jpeg)
(b) 相比去年同期扩张区域图像
(b) Extraction of expansion area compared with the same period last year
![img-23.jpeg](img-23.jpeg)
(d) 相比去年同期扩张区域 RGB合成图像
(d) RGB composite image of expansion area compared with the same period last year

图11 洪灾区域提取结果对比
Fig. 11 Comparison of extraction of flood area
在 RGB 图像中，红色区域即为遭受洪涝灾害地区，由图11可知，通过水体提取和相减变化检测，洪灾区域基本实现了提取。根据相减变化检测结果可知，与 2020 年 3 月相比，在 2020 年 7 月，鄱阳湖流域的水体面积有明显的增大，鄱阳湖流域的西南部分扩张尤为明显，鄱阳湖的北部区域扩张相对较少；与 2019 年同期相比，鄱阳湖也扩张了一部分，扩张部分集中在鄱阳湖西部区域和东南区域。

为评估水体提取结果，利用 Landsat-8 光学卫星开展验证实验 ${ }^{[29]}$ 。由于2020年7月鄱阳湖流域雨水较多、云层较厚，光学卫星难以观测，因此选用2019年7月 Landsat-8的图像与提取结果进行对比，如图 12 所示。
![img-24.jpeg](img-24.jpeg)

图 12 Landsat-8 光学卫星2019年7月鄱阳湖区域图像
Fig. 12 Landsat-8 optical satellite image of Poyang Lake area in July 2019

除了与迭代阈值分割算法进行对比外，本文还选用 Otsu 阈值分割算法、K-Means 非监督性学习、EM 算法的提取结果进行对比，如图 13 所示。

![img-25.jpeg](img-25.jpeg)
(a) 本文算法提取结果
(a) Extraction result of the algorithm of this paper
![img-26.jpeg](img-26.jpeg)
(c) K-means非监督性学习提取结果
(c) Extraction result of K-Means algorithm
![img-27.jpeg](img-27.jpeg)
(b) Otsu阈值分割算法提取结果
(b) Extraction result of Otsu algorithm
![img-28.jpeg](img-28.jpeg)
(d) EM算法提取结果
(d) Extraction result of EM algorithm

图13 不同算法的提取结果
Fig. 13 Extraction results of different algorithms
为验证本文所提方法的有效性，通过采样评估对上述 3 种提取方式的提取效果进行评估。具体方法为：在光学卫星图像中分别随机选取 300 个点，分别统计 3 种提取方式的准确率、虚警率、漏警率、计算时间等 ${ }^{[16]}$ 。其结果如表 3 所示。

表 3 不同提取方式评估结果
Table 3 Evaluation of different extraction methods


根据随机采样后的对比结果可知，对于 2019 年 7 月 都阳湖流域的 SAR 图像，迭代阈值分割法与 Otsu 阈值分割法的阈值较为接近，两者的提取效果差距不大；K-Means 非监督性学习提取的结果与前二者相比，准确率较低、虚警率较高、漏警率较为接近。EM 算法的准确率最高，虚警率和漏警率都较低；在计算时间方面，本文使用处理器为 Intel Core i7-9850H CPU 的计算机完成实验，其中迭代阈值分割算法完成对 2019 年 7 月都阳湖流域 SAR 图像数据的处理需

要 1.045 s ，而 Otsu 阈值分割算法需要 10.016 s ，K-Means 非监督性学习需要 78.153 s 。Otsu 阈值分割算法由于需要对所有后向散射系数等级进行一次遍历，因此算法的时间复杂度较高，导致所需时间较长。而对于 K-Means 算法和 EM 算法，均需要进行多次迭代，所需时间远大于前两种方法。对于迭代阈值分割算法，在一般情况下，仅需迭代数次即可得出阈值，所需时间大大减少，提取效率也相应得到了提高。

## 4 结 论

本文提出了一种基于改进迭代阈值分割的 SAR 图像洪水区域快速提取方法。该方法首先通过预处理与高斯拟合对噪声和畸变进行抑制，之后通过迭代阈值分割算法提取水体，再利用形态学滤波抑制噪声，最后通过变化检测提取洪水区域。与传统的洪水区域提取算法相比，该算法在保证较高提取准确率的同时提高了处理速度，使提取效率得到提升。将该方法应用于2020年7月都阳湖流域的洪水灾害研究中，通过预处理、水体提取、变化检测等流程，得到了都阳湖流域洪水区域的提取结果。通过将结果与 Landsat-8 光学卫星图像的对比，该方法的可靠性与准确性得到了验证；通过与传统提取方式的对比实验，表明了迭代阈值分割算法在洪水区域提取中的高效性，为利用 SAR 图像提取洪水区域提供了新的研究思路。

后续在这方面的主要工作内容为：(1) 对算法的适用性进行进一步检验，考虑复杂情况下的洪涝区域提取，如城市内涝等；(2) 考虑结合光学图像信息，改进算法结构，提升准确率。

## 参考文献

[1] CUMMING I G, WONG F H. Digital signal processing of synthetic aperture radar data: algorithms and implementation[M]. Boston: Artech House, 2004.
[2] MOREIRA A, PRATS-IRAOLA P, YOUNIS M, et al. A tutorial on synthetic aperture radar[J]. IEEE Geoscience and Remote Sensing Magazine, 2013, 1(1): 6-43.
[3] 龚林松, 李士进. 基于改进的 SLIC 和 OTSU 的遥感影像水体提取[J]. 计算机技术与发展, 2019, 29(1): 145-149.
GONG L S, LI S J. Water information extraction from remote sensing imagery based on improved SLIC and OTSU[J]. Computer Technology and Development, 2019, 29(1): 145-149.
[4] NIHARIKA E, ADEEBA H, KRISHNA A S R, et al. Kmeans based noisy SAR image segmentation using median filtering and otsu method[C]//Proc. of the IEEE International Conference on IoT and Application, 2017.
[5] AO W, XU F, LI Y C, et al. Detection and discrimination of ship targets in complex background from spaceborne ALOS-2 SAR images[J]. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2018, 11(2): 536-550.
[6] 李致衡, 陈亮, 张博程, 等. 基于最大熵阈值分割的 SAR 图像溢油检测[J]. 信号处理, 2019, 35(6): 1111-1117.
LI Z H, CHEN L, ZHANG B C, et al. SAR image oil spill detection based on maximum entropy threshold segmentation[J].

Journal of Signal Processing, 2019, 35(6): 1111 - 1117.
[7] KERSTEN P R, LEE J S, AINSWORTH T L. Unsupervised classification of polarimetric synthetic aperture radar images using fuzzy clustering and EM clustering[J]. IEEE Trans. on Geoscience and Remote Sensing, 2005, 43(3): 519-527.
[8] KHAN K U, YANG J, ZHANG W J. Unsupervised classification of polarimetric SAR images by EM algorithm[J]. IEICE Trans. on Communications, 2007, 90(12): 3632-3642.
[9] FENG W Q, SUI H G, HUANG W M, et al. Water body extraction from very high-resolution remote sensing imagery using deep U-Net and a superpixel-based conditional random field model[J]. IEEE Geoscience and Remote Sensing Letters, 2018, $16(4): 618-622$.
[10] AN Q Z, PAN Z X, YOU H J. Ship detection in Gaofen-3 SAR images based on sea clutter distribution analysis and deep convolutional neural network[J]. Sensors, 2018, 18(2): 334-336.
[11] OTSU N. A threshold selection method from gray-level histograms [J]. IEEE Trans. on Systems, Man \& Cybernetics, 2007, 9(1): 62 - 66.
[12] 孙亚勇, 黄诗峰, 李纪人, 等. Sentinel-1A SAR 数据在缅甸伊洛瓦底江下游区洪水监测中的应用[J]. 遥感技术与应用, 2017, 32(2): 282 - 288.
SUN Y Y, HUANG S F, LI J R, et al. The downstream flood monitoring application of Myanmar Irrawaddy River based on Sentinel-1A SAR[J]. Remote Sensing Technology and Application, 2017, 32(2): 282 - 288.
[13] 郭欣,赵银娣. 基于 Sentinel-1A SAR 的湖南省宁乡市洪水监测[J]. 遥感技术与应用, 2018: 33(4): 646-656.
GUO X, ZHAO Y D. Flood inundation monitoring in ningxiang of Hunan province based on Sentinel-1A SAR[J]. Remote Sensing Technology and Application, 2018, 33(4): 646-656.
[14] HARTIGAN J, WONG M. Algorithm AS 136: a K-means clustering algorithm[J]. Journal of the Royal Statistical Society, 1979, 28(1): 100 - 108.
[15] 戴牧宸, 冷祥光, 熊博在, 等. 基于改进双边网络的 SAR 图像海陆分割方法[J]. 雷达学报, 2020, 9(5): 886-897.
DAI M C, LENG X G, XIONG B L, et al. Sea-land segmentation method for SAR images based on improved BiSeNet[J]. Journal of Radars, 2020, 9(5): 886-897.
[16] SHAMSOLMOALI P, ZAREAPOOR M, WANG R, et al. A novel deep structure U-Net for sea-land segmentation in remote sensing images[J]. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2019, 12(9): 3219-3232.
[17] 王志豪, 李刚, 蒋骁. 基于光学和 SAR 遥感图像融合的洪灾区域检测方法[J]. 雷达学报, 2020, 9(3): 539-553.
WANG Z H, LI G, JIANG X. Flooded area detection method based on fusion of optical and SAR remote sensing images[J]. Journal of Radars, 2020, 9(3): 539-553.
[18] PRAKASH R, SINGH D, PATHAK N P. A fusion approach to retrieve soil moisture with SAR and optical data[J]. IEEE Journal of Selected Topics in Applied Earth Observations \& Remote Sensing, 2012, 5(1): 196-206.
[19] SICA F, REALE D, POGGI G, et al. Nonlocal adaptive multi-
looking in SAR multipass differential interferometry[J]. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2015, 8(4): 1727 - 1742.
[20] 张过, 蒋永华, 李立涛, 等. 高分辨率光学/SAR 卫星几何辐射定标研究进展[J]. 测绘学报, 2019, 48(12): 1604-1623. ZHANG G, JIANG Y H, LI L T, et al. Research progress of high-resolution optical/SAR satellite geometric radiometric calibration[J]. Acta Geodactica et Cartographica Sinica, 2019, 48(12): $1604-1623$.
[21] SMALL D. Flattening gamma: radiometric terrain correction for SAR imagery[J]. IEEE Trans. on Geoscience and Remote Sensing, 2011, 49(8): 3081-3093.
[22] RIDLER T W, CALVARD S. Picture thresholding using an iterative selection method[J]. IEEE Trans. on Systems, Man \& Cybernetics, 2007, 8(8): 630-632.
[23] TRUSSELL H J. Comments on "picture thresholding using an iterative selection method"[J]. IEEE Trans. on Systems, Man \& Cybernetics, 1979, 9(5): 311.
[24] MAGID A, ROTMAN S R, WEISS A M. Comments on picture thresholding using an iterative selection method[J]. IEEE Trans. on Systems, Man \& Cybernetics, 1990, 20(5): 1238-1239.
[25] BRUZZONE L, PRIETO D F. Automatic analysis of the difference image for unsupervised change detection[J]. IEEE Trans. on Geoscience and Remote Sensing, 2000, 38(3): 1171-1182.
[26] BAZI Y, BRUZZONE L, MELGANI F. An unsupervised approach based on the generalized Gaussian model to automatic change detection in multitemporal SAR images[J]. IEEE Trans. on Geoscience and Remote Sensing, 2005, 43(4): 874-887.
[27] WANG G T, WANG Y L, JIAO L C. Adaptive spatial neighborhood analysis and Rayleigh-Gauss distribution fitting for change detection in multi-temporal remote sensing images[J]. Journal of Remote Sensing, 2009, 13(4): 639-646.
[28] BASSO D, COLNAGO M, AZEVEDO S, et al. Combining morphological filtering, anisotropic diffusion and block-based data replication for automatically detecting and recovering unscanned gaps in remote sensing images[J]. Earth Science Informatics, 2021, 14(3): 1145-1158.
[29] ROY D, WULDER M, LOVELAND T, et al. Landsat-8: Science and product vision for terrestrial global change research[J]. Remote Sensing of Environment, 2014, 145: 154-172.
[30] 谷鑫志, 曾庆伟, 谌华, 等. 高分三号影像水体信息提取[J].遥感学报, 2019, 23(3): 555-565.
GU X Z, ZENG Q W, SHEN H, et al. Study on water information extraction using domestic GF-3 image[J]. Journal of Remote Sensing, 2019, 23(3): 555-565.

## 作者简介

雷 潘（1997-），男，硕士研究生，主要研究方向为 SAR 图像处理。曾虹程（1989-），男，讲师，博士，主要研究方向为 SAR 成像处理、误差分析与补偿以及新体制雷达设计。
王 贺（1998-），男，硕士研究生，主要研究方向为 SAR 成像处理。陈 杰（1973-），男，教授，博士，主要研究方向为星载合成孔径雷达系统建模、高分辨率星载 SAR 成像处理、新体制成像雷达系统技术。