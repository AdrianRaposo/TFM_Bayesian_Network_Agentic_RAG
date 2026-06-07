# Article 

## A Novel Approach for Improving the Security of IoT-Medical Data Systems Using an Enhanced Dynamic Bayesian Network

Mohammed Amin Almaiah ${ }^{1,2, *}$, Sandeep Yelisetti ${ }^{3}$, Leena Arya ${ }^{4}$, Nelson Kennedy Babu Christopher ${ }^{5}$, Kumaresan Kaliappan ${ }^{6}$, Pandimurugan Vellaisamy ${ }^{7}$, Fahima Hajjej ${ }^{8}$ and Tayseer Alkdour ${ }^{9}$


#### Abstract

check for updates Citation: Almaiah, M.A.; Yelisetti, S.; Arya, L.; Babu Christopher, N.K.; Kaliappan, K.; Vellaisamy, P.; Hajjej, F.; Alkdour, T. A Novel Approach for Improving the Security of IoT-Medical Data Systems Using an Enhanced Dynamic Bayesian Network. Electronics 2023, 12, 4316. https://doi.org/10.3390/ electronics12204316


Academic Editor: Juan-Carlos Cano

Received: 3 September 2023
Revised: 10 October 2023
Accepted: 13 October 2023
Published: 18 October 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Information Technology, Aqaba University of Technology, Aqaba 11947, Jordan
2 Applied Science Research Center, Applied Science Private University, Amman 11931, Jordan
3 Department of IT, V R Siddhartha Engineering College, Vijayawada 520007, India
4 Department of CSE, Koneru Lakshmaiah Education Foundation, Mangalagiri, Vaddeswaram 522502, India
5 Department of Computer Science and Engineering, Saveetha School of Engineering, Chennai 602105, India
6 Maratsolutions, Coimbatore 641001, India
7 School of Computing, Department of Networking and Communications, SRM Institute of Science \& Technology, Kattankulathur Campus, Chennai 603203, India
8 Department of Information Systems, College of Computer and Information Sciences, Princess Nourah bint Abdulrahman University, P.O. Box 84428, Riyadh 11671, Saudi Arabia
9 College of Computer Science and Information Technology, King Faisal University, Al-Ahsa 31982, Saudi Arabia

* Correspondence: m.almaayah@aau.edu.jo


#### Abstract

IoT (Internet of Things) devices are increasingly being used in healthcare to collect and transmit patient data, which can improve patient outcomes and reduce costs. However, this also creates new challenges for data security and privacy. Thus, the major demand for secure and efficient data-sharing solutions has prompted significant attention due to the increasing volume of shared sensor data. Leveraging a data-fusion-based paradigm within the realm of IoT-protected healthcare systems enabled the collection and analysis of patient data from diverse sources, encompassing medical devices, electronic health records (EHRs), and wearables. This innovative approach holds the potential to yield immediate benefits in terms of enhancing patient care, including more precise diagnoses and treatment plans. It empowers healthcare professionals to devise personalized treatment regimens by amalgamating data from multiple origins. Moreover, it has the capacity to alleviate financial burdens, elevate healthcare outcomes, and augment patient satisfaction. Furthermore, this concept extends to fortifying patient records against unauthorized access and potential misuse. In this study, we propose a novel approach for secure transmission of healthcare data, amalgamating the improved context-aware data-fusion method with an emotional-intelligence-inspired enhanced dynamic Bayesian network (EDBN). The findings indicated that F1 score, accuracy, precision, recall, and ROC-AUC score using DCNN were $89.3 \%, 87.4 \%, 91.4 \%, 92.1 \%$, and 0.56 , respectively, which was second-highest to the proposed method. On the other hand, the F1 score, accuracy, precision, recall, and ROC-AUC scores of FRCNN and CNN were low in accuracy at $83.2 \%$ and $84.3 \%$, respectively. Our experimental investigation demonstrated superior performance compared with existing methods, as evidenced by various performance metrics, including recall, precision, F measures, and accuracy.


Keywords: IoT-medical network; data security; IoT-medical security; emotional intelligence; EDBN

## 1. Introduction

Emotional intelligence healthcare merges technology and AI with a focus on empathizing with patients' emotions. By utilizing sophisticated algorithms and data analysis, it enables medical professionals to gain insights into patient behaviors and improve their quality of care. This approach not only leads to personalized treatment but also aids in identifying potential mental health and medical problems before they escalate, ultimately reducing healthcare costs [1].

Fusion-based healthcare systems in IoT environments combine various data sources, such as patient data, medical records, and photographs, to provide a comprehensive view of a patient's health [2]. This approach allows medical professionals to understand a patient's medical history, current health, and potential future health risks. Real-time monitoring of patient health is also made possible through this integration, enabling prompt identification and treatment of medical issues. By utilizing sensors and devices connected to the IoT, the system gathers data from multiple sources and fuses it into one complete picture, as shown in Figure 1. This data fusion offers valuable insights to healthcare providers, aiding in informed decision making for a patient's care. Additionally, the system offers advanced analytical capabilities, allowing healthcare professionals to detect patterns in patient data, anticipate future health problems, and optimize treatment plans [3].
![img-0.jpeg](img-0.jpeg)

Figure 1. IoT with AI based Healthcare System.
Emotional intelligence is being incorporated into healthcare to protect data collected by IoT devices. By considering the human element and security aspect, this concept can detect anomalies and threats to data security. It can also identify unusual user behavior to prevent malicious activity. This approach not only enhances data security, but also ensures its reliability [4].

IoT (Internet of Things) devices are increasingly being used in healthcare to collect and transmit patient data, which can improve patient outcomes and reduce costs. However, this also creates new challenges for data security and privacy. Here are some ways that IoT devices can be used to enhance the security of healthcare data [5]:

Encryption: IoT devices should use encryption to secure data transmission and storage. This implies that data are encoded in a way that only authorized parties may decode.

Authorization and Authentication: In order to guarantee that only authorized users may access and alter data, devices should utilize authentication and authorization protocols. This can be done using methods such as passwords, biometrics, or smart cards.

Data Access Control: Access to patient data should be restricted to authorized personnel only. This can be done by implementing role-based access control, where each user is granted access to data based on their role and level of authorization.

Regular Auditing: Regular auditing of the IoT system can help identify any security vulnerabilities and monitor user activity. This can be done through system logs, alerts, and reports.

Data-sharing issues in healthcare systems have been a long-standing challenge due to concerns around data privacy, security, and ownership. Fusion-based approaches, which combine data from multiple sources to provide more comprehensive and accurate insights, can exacerbate these issues if not handled appropriately. Emotional intelligence (EI) can

play a critical role in addressing these issues by enabling healthcare providers to understand and manage the emotional aspects of data sharing and privacy concerns [6]. Fusion-based procedures sometimes include merging data from many sources, such as electronic health records (EHRs), to give a more complete picture of a patient's health, medical devices, and patient-generated data. However, there may be substantial problems with data security and privacy due to this connection [7]. One illustration is that the exchange of patient data between healthcare professionals may be limited by legal and ethical considerations, which can lead to a lack of data sharing between healthcare providers. This, in turn, can impede the ability of healthcare providers to provide effective care [8].

Emotional intelligence can help healthcare providers address these issues by enabling them to better understand and manage the emotional aspects of data sharing and privacy concerns. For example, healthcare providers with high levels of emotional intelligence can better understand patients' concerns around data sharing and privacy and can communicate more effectively with them to address their concerns. They can also work more effectively with other healthcare providers to ensure that patient data are shared securely and appropriately [9].

Overall, the healthcare providers must ensure that IoT devices are secure and patient data are protected by implementing various security measures such as encryption, authentication, access control, auditing, and privacy by design [10]. This will help to maintain patient trust and confidence in the use of IoT in healthcare. Data-sharing issues in healthcare systems with fusion-based approaches can be addressed by leveraging emotional intelligence to better understand and manage the emotional aspects of data sharing and privacy concerns. By doing so, healthcare providers can provide more effective care and improve patient outcomes, as shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Artificial-intelligence-based IoT healthcare system.
The major demand for secure and efficient data-sharing solutions has prompted significant attention due to the increasing volume of shared sensor data. Leveraging a data fusion-based paradigm within the realm of IoT-protected healthcare systems has enabled the collection and analysis of patient data from diverse sources, encompassing medical devices, electronic health records (EHRs), and wearables. This innovative approach holds the potential to yield immediate benefits in terms of enhancing patient care, including more precise diagnoses and treatment plans. It empowers healthcare professionals to devise personalized treatment regimens by amalgamating data from multiple origins. Moreover, it has the capacity to alleviate financial burdens, elevate healthcare outcomes, and augment patient satisfaction. Furthermore, this concept extends to fortifying patient records against unauthorized access and potential misuse. In this study, we propose a novel approach for secure transmission of healthcare data, amalgamating the improved context-aware

data-fusion method with an emotional-intelligence-inspired enhanced dynamic Bayesian network (EDBN).

The remainder of this article's structure is as follows. Various background studies on the methods used for data security in the healthcare sector are included in Section 2. The suggested EDBN methodology for securing and categorizing IoT data for transmission is elaborated in Section 3. Results that validate performance and predictability are presented in Section 4 along with the appropriate explanations. In Section 5, the conclusion is presented along with future prospects.

# 2. Related Works and Background 

### 2.1. Data Fusion for Healthcare Data Security in IoT

In recent years, there has been growing interest in using data-fusion techniques to enhance the security of healthcare data in the IoT. Data fusion can help detect anomalies and identify potential security threats by integrating data from enormous sources, such as electronic health records, wearables, and medical sensor devices.

Previous researchers [11-13] discussed a hybrid AI model that combines deep learning and fuzzy logic to analyze data from multiple IoT devices and optimize the network load. The article highlights the potential benefits of this approach for various applications, including healthcare, smart cities, and industrial automation. Another research group [14] presented a hybrid delay-aware adaptive clustering method for intelligent data fusion in wireless sensor networks. The method optimizes the data-fusion process by taking into consideration the communication delay and energy consumption of the sensor nodes. Refs $[15,16]$ proposed an approach that uses a combination of rule-based and machine learning techniques to integrate data from multiple sources and generate meaningful insights. The study provided simulation findings that showed how the suggested strategy might enhance the precision and dependability of IoT health systems. Refs [17,18] proposed an Internet-of-Things (IoT)-enabled data-fusion method for sleep-healthcare applications that integrates data from multiple sources including wearable devices, smartphones, and environmental sensors. The proposed method uses a deep learning-based approach to extract features from the raw data and generate sleep-related metrics.

### 2.2. Healthcare with Emotional Intelligence in IoT

Studies [19-23] have discussed the potential of cognitive computing, emotional intelligence, and artificial intelligence in healthcare, with a focus on their applications in disease diagnosis, treatment, and personalized healthcare. Authors have suggested a disease-diagnostic paradigm for intelligent healthcare systems that is supported by artificial intelligence and the Internet of Things (IoT) and integrates data from multiple sources, including wearable devices, smartphones, and environmental sensors [24-32]. Researchers have provided an overview of the key concepts and technologies involved in AIoT healthcare architectures and highlighted the potential benefits of AIoT healthcare architectures, including improved patient care, reduced costs, and increased efficiency [33-42].

In summary, within the context of this review based on the above considerations in an IoT-based healthcare environment, a healthcare system with emotional intelligence within the IoT has the potential to improve patient outcomes, but there are several challenges that need to be addressed. These challenges include privacy and data-security concerns, integration with existing systems, reliability and accuracy of emotional intelligence analysis, user acceptance and adoption, ethical concerns, and the cost of IoT-based healthcare applications.

## 3. Materials and Methods

## A. Low-Pass Filter

Low-pass filters are a type of filter that let low-frequency signals pass through while blocking or attenuating higher-frequency signals. In order to filter out noise and undesired high-frequency signals, low-pass filters are frequently employed in IoT healthcare data. This

can be especially important when dealing with patient data, as the noise and interference can be misinterpreted and lead to incorrect diagnoses or treatments.

$$
H(s)=1 /\left(1+(s / w)^{2}\right)
$$

where $H(s)$ is the transfer function of the filter, $s$ is the frequency of the signal, and $w$ is the cutoff frequency of the filter.

$$
(\mathrm{N}=1): \mathrm{Y}(\mathrm{n})=(1 / 1)^{*} \mathrm{X}(\mathrm{n})=\mathrm{X}(\mathrm{n})
$$

$Y(n)=(1 / N) * \Sigma X(k)$ is true for some arbitrary $N \geq 1$.

$$
Y(n)=(1 /(N+1)) * \Sigma X(k)=(1 /(N+1)) *(X(n)+\Sigma X(k))
$$

A low-pass filter is a filter used to remove higher-frequency components from a signal. This type of filter is commonly used for preprocessing IoT healthcare data because it can reduce noise and other unwanted high-frequency components. Low-pass filters are also used to reduce the amount of high-frequency interference that can be present in a wireless signal. This is especially important when dealing with medical devices, as high-frequency interference can disrupt the signal and cause incorrect readings. Low-pass filters can help ensure that the signal remains clear and accurate, enabling more accurate readings and diagnoses.

$$
Y(n)=X(n) * H(n)
$$

where $Y(n)$ is the output signal, $X(n)$ is the input signal, $H(n)$ is the impulse response of the filter. A simple low-pass filter is a moving-average filter, which can be expressed as:

$$
H(n) A=\frac{1}{N} * \sum(k=0 \text { to } N-1) X(n-k)
$$

where $N$ is the number of samples in the moving average.
The output signal can then be expressed as:

$$
Y(n)=1 / N^{*} \Sigma(k=0 \text { to } N-1) X(n-k) * X(n)
$$

# B. Improved Context-Aware Data Fusion (ICDF) 

The improved context-aware data-fusion (ICDF) algorithm is an advanced data-fusion and analysis technique that combines multiple data sources and context information to create a single, comprehensive dataset. ICDF is particularly applicable to healthcare systems that involve both physical and virtual components and can be used to improve patient monitoring or medical decision making. In an IoT healthcare system, ICDF can be used to provide a better understanding of patient data by combining streaming real-time data from connected medical devices with patient-specific context information, such as age and medical history. By combining these different data sources, ICDF can provide more accurate and comprehensive patient information, which can be used to detect abnormalities, monitor patient conditions, and improve the accuracy of medical decision making. Algorithm 1 is shown the Improved context-aware data fusion (ICDF).

$$
\text { Fused value }=\mathrm{P}(\mathrm{x} \mid \text { value1, value2, value3...Value } \mathrm{N})^{*} \mathrm{P}(\mathrm{x})
$$

The ICDF algorithm also provides better scalability and flexibility for the healthcare system. By using multiple data sources and context information, the algorithm can be easily adapted to different scenarios and environments, making it suitable for largescale healthcare systems. Additionally, the algorithm can be used to detect anomalies and trends in patient data, which can be used for further analysis and understanding of patient conditions.

A continuous-time signal is transformed mathematically into its frequency domain representation using the Fourier transform. It is described in terms of continuous data, and its formula is provided in Equations (8) and (9):

$$
\begin{gathered}
\mathrm{F}(\omega)=\int\left[\mathrm{f}(\mathrm{t})^{*} \exp (-\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt} \\
\mathrm{X}[\mathrm{k}]=\Sigma\left[\mathrm{x}[\mathrm{n}]^{*} \exp (-\mathrm{j}(2 \pi / \mathrm{N}) \mathrm{kn})\right]
\end{gathered}
$$

Algorithm 1: Improved context-aware data fusion (ICDF)
1: Input: Set of sensor data S
2: Step 1: Perform local data fusion to combine similar pieces of data into a single entity.
3: Fused data $=($ Data $1+$ Data $2+$ Data3 $+\ldots+$ DataN $) / \mathrm{N}$
4: Step 2: For each entity in S, apply context-aware data-fusion methods to adjust the data based on context.
5: Step 3: Aggregate the results of the individual data-fusion methods into a single entity using a weighted average or other suitable method.
6: Step 4: Perform global data fusion on the aggregated entity using fuzzy logic or other suitable methods to adjust the data based on global context.
7: Output: Single fused data entity.
Let $X=[x 1, x 2, \ldots, x n]$ be a set of $n$ data sources, where $x i$ represents the data from the i-th source. Let $Y=[y 1, y 2, \ldots, y m]$ be a set of $m$ contextual attributes, where yi represents the contextual attribute from the i-th source.

Let $Z=[z 1, z 2, \ldots, z n]$ be the data-fusion result, where zi represents the fused data from the i-th source. The ICDF algorithm computes the fused data as follows:

The Morkov model fusion equation is:

$$
Z=f(X, Y)=(1-\alpha) * X+\alpha * Y
$$

where $\alpha$ is the weighting factor for combining the fusion data $Y$ with the observation data X, as mentioned in Equation (10).

Let us consider the exponential term, $\exp (-\mathrm{j} \omega \mathrm{t})$. By Euler's formula, we can express it as:

$$
\exp (-\mathrm{j} \omega \mathrm{t})=\cos (\omega \mathrm{t})-\mathrm{j}^{*} \sin (\omega \mathrm{t})
$$

Substituting this back into the original equation, we have:

$$
\mathrm{F}(\omega)=\int\left[\mathrm{f}(\mathrm{t})^{*}(\cos (\omega \mathrm{t})-\mathrm{j}^{*} \sin (\omega \mathrm{t}))\right] \mathrm{dt}
$$

We can separate the integral into two parts: one for the real part (cosine) and one for the imaginary part (sine). Let us start with the real part:

$$
\mathrm{F}(\omega)=\int\left[\mathrm{f}(\mathrm{t})^{*} \cos (\omega \mathrm{t})\right] \mathrm{dt}
$$

To evaluate this integral:

$$
\int\left[\mathrm{f}(\mathrm{t})^{*} \cos (\omega \mathrm{t})\right] \mathrm{dt}=(1 / 2) * \int\left[\mathrm{f}(\mathrm{t})^{*}\left(\mathrm{e}^{*}(\mathrm{j} \omega \mathrm{t})+\mathrm{e}^{*}(-\mathrm{j} \omega \mathrm{t})\right)\right] \mathrm{dt}
$$

Now, we can expand the exponential terms:

$$
\mathrm{F}(\omega)=(1 / 2) * \int\left[\mathrm{f}(\mathrm{t})^{*} \mathrm{e}^{*}(\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}+(1 / 2) * \int\left[\mathrm{f}(\mathrm{t})^{*} \mathrm{e}^{*}(-\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}
$$

Applying the linearity property of integrals, we can separate the integrals:

$$
\mathrm{F}(\omega)=(1 / 2) * \int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}+(1 / 2) * \int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(-\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}
$$

Since the function $f(t)$ is real-valued, the two integrals are complex conjugates of each other:

$$
\begin{aligned}
& \mathrm{F}(\omega)=(1 / 2) * \int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}+(1 / 2) * \int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(-\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt} \\
& \mathrm{~F}(\omega)=(1 / 2) * \int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}+(1 / 2) *\left[\int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}\right]^{*}
\end{aligned}
$$

Simplifying, we have:

$$
\begin{gathered}
\mathrm{F}(\omega)=(1 / 2) * \int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}+(1 / 2) *\left[\int\left[\mathrm{f}(\mathrm{t}) * \mathrm{e}^{-}(\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}\right]^{*} \\
\mathrm{~F}(\omega)=\int\left[\mathrm{f}(\mathrm{t}) * \exp (-\mathrm{j} \omega \mathrm{t})\right] \mathrm{dt}
\end{gathered}
$$

Equation (12) states that the Fourier transform of a signal $f(t)$ is equal to the integral of the product of the signal $f(t)$ and the complex exponential $\exp (-\mathrm{j} \omega \mathrm{t})$, where $\omega$ is the angular frequency. In the context of IoT healthcare data fusion, this equation can be used to analyze the frequency components of healthcare data from different sources. By performing the Fourier transform, one can analyze the frequency content of the data to identify patterns and correlations between different data sources.

Contextual attribute weighting: The first step of the ICDF algorithm is to weight the contextual attributes based on their importance in the current context.

Let $\mathrm{w}=[\mathrm{w} 1, \mathrm{w} 2, \ldots, \mathrm{wm}]$ be the weight vector for the contextual attributes, where wi represents the weight for the $i$-th contextual attribute. The weight vector can be calculated using a variety of techniques, such as entropy-based weighting or principal component analysis.

Data normalization: The second step is to normalize the data from each source to ensure that they are on the same scale. This is done to prevent sources with larger values from dominating the fusion result. Let $\mathrm{xi}^{\prime}$ be the normalized data from the $i$-th source, which can be calculated as follows:

$$
x i t=\frac{(x i-\min (x i))}{(\max (x i)-\min (x i))}
$$

where, in Equation (13), $\min (x i)$ and $\max (x i)$ represent, respectively, the minimum and maximum values of the data from the $i$-th source.

Contextual attribute-based data fusion: The third step is to fuse the normalized data based on the contextual attributes. Let $Z=[z 1, z 2, \ldots, \mathrm{zm}]$ be the contextual attribute vector for the current context, where zi represents the value of the i-th contextual attribute. The fused data di can be calculated as follows in Equation (14):

$$
d i=\frac{\sum j=1 m\left(x i^{\prime} j * w j * \delta(z i, y j)\right)}{\sum j=1 m(w j * \delta(z i, y j))}
$$

where $x i^{\prime} j$ is the normalized data from the $i$-th source for the $j$-th contextual attribute, $\delta(z i, y j)$ is the Kronecker delta function that returns 1 if $z i=y j$ and 0 otherwise, and $\Sigma j=1 m$ $\left(w j^{*} \delta(z i, y j)\right)$ is the normalization factor.

# C. Advanced Recursive Feature Elimination (ARFE) 

Advanced recursive feature elimination (ERFE) is an advanced version of RFE that uses a genetic algorithm to search for the optimal feature set. ERFE works by iteratively removing attributes and building a model on those attributes that remain. It then evaluates the model. Note that ERFE is a computationally intensive algorithm and may require a

significant amount of time and resources to run on large datasets. Therefore, it is recommended to use ARFE with caution and consider other feature-selection algorithms if the computational cost is a concern.

Let $X$ be the input dataset with $n$ features and $m$ samples, and $y$ be the corresponding target variable. Let $S$ be the initial set of candidate features, and $k$ be the number of features to eliminate at each step. Let J be the performance metric to optimize.
Initialization: Set $S=\left\{x_{-} 1, x_{-} 2, \ldots, x_{-} n\right\}$, where $x_{-} i$ is the $i$-th feature in $X$. Train a machine learning model $\mathrm{M}_{-} 0$ on the dataset using all the features in S . Compute the initial performance score $\mathrm{J}_{-} 0=\mathrm{J}(\mathrm{y}, \mathrm{M}_{-} 0(\mathrm{X}))$.

We can perform the features initialization with the given dataset:

$$
y=(1 / m)\left(x_{1}{ }^{*} f_{1}+x_{2}{ }^{*} f_{2}+\ldots+x_{m}{ }^{*} f_{m}\right)-(1 / m)\left(x_{1}{ }^{*} y_{1}+x_{2}{ }^{*} y_{2}+\ldots+x_{m}{ }^{*} y_{m}\right)
$$

Next, we can distribute $(1 / \mathrm{m})$ to each term within the summations:

$$
y=(1 / m) x_{1}{ }^{*} f_{1}+(1 / m) x_{2}{ }^{*} f_{2}+\ldots+(1 / m) x_{m}{ }^{*} f_{m}-(1 / m) x_{1}{ }^{*} y_{1}-(1 / m) x_{2}{ }^{*} y_{2}-\ldots-(1 / m) x_{m}{ }^{*} y_{m}
$$

Now, we can rearrange the terms:

$$
\begin{aligned}
& y=\left[(1 / m) x_{1} * f_{1}-(1 / m) x_{1} * y_{1}\right]+\left[(1 / m) x_{2} * f_{2}-(1 / m) x_{2} * y_{2}\right] \ldots+\left[(1 / m) x_{m} * f_{m}\right. \\
& \left.-(1 / m) x_{m} * \ldots y_{m}\right] \\
& y=(1 / m)\left[x_{1} *\left(f_{1}-y_{1}\right)+x_{2} *\left(f_{2}-y_{2}\right)+\ldots+x_{m} *\left(f_{m}-y_{m}\right)\right] \\
& y=(1 / m) \sum\left[x_{i} *\left(f_{i}-y_{i}\right)\right]
\end{aligned}
$$

Feature ranking: Compute the importance score of each feature in S, based on a ranking method such as correlation-based or filter-based methods.
Advanced Recursive feature elimination: Eliminate the k least important features from S, based on their importance scores. Let $S^{\prime}$ be the remaining features in $S$. Train a new machine learning model $\mathrm{M}_{-} \mathrm{i}$ on the dataset using the features in $\mathrm{S}^{\prime}$. Compute the performance score $\mathrm{J}_{-} \mathrm{i}=\mathrm{J}(\mathrm{y}, \mathrm{M}_{-} \mathrm{i}(\mathrm{X}))$. If $\mathrm{J}_{-} \mathrm{i}>\mathrm{J}_{-}\{\mathrm{i}-1\}$, set $\mathrm{S}=\mathrm{S}^{\prime}$ and go to step 2. If $\mathrm{J}_{-} \mathrm{i} \ll \mathrm{J}_{-}\{\mathrm{i}-1\}$, terminate the algorithm and select the features in $\mathrm{S}_{-}(\mathrm{i}-1\}$ as the final feature subset.

This research uses a recursive approach to eliminate the least important features iteratively until the stopping criterion is met. The feature-selection process is based on the performance score of the machine learning model, and the feature-ranking method can be customized based on the specific problem domain. ARFE adds additional features to the basic RFE algorithm, such as dynamic programming and early stopping criteria, to improve the efficiency and accuracy of the feature-selection process.

$$
\text { Feature Selection }=\left(\sum \mathrm{i}=1 \mathrm{n}(\mathrm{Xi}-\overline{\mathrm{X}})^{2} /(\mathrm{n}-1)\right)
$$

where $\overline{\mathrm{X}}$ is the sample mean, $\mathrm{X}_{\mathrm{i}}$ is a data point, and n is the number of data points.
Now, let us express the summation in terms of an integral. We assume a continuous probability distribution function $F(X)$ for the dataset.

The integral representation of the sample variance equation becomes:
Feature Selection $=\int(\mathrm{X}-\overline{\mathrm{X}})^{2} \mathrm{dF}(\mathrm{X})=\int\left(\mathrm{X}^{2}-2 \overline{\mathrm{X}} \mathrm{X}+\overline{\mathrm{X}}^{2}\right) \mathrm{dF}(\mathrm{X})$.
Next, we can distribute the integral over each term:
Feature Selection $=\int \mathrm{X}^{2} \mathrm{dF}(\mathrm{X})-2 \overline{\mathrm{X}} \int \mathrm{X} \mathrm{dF}(\mathrm{X})+\overline{\mathrm{X}}^{2} \int \mathrm{dF}(\mathrm{X})$.
Now, let us simplify each integral term individually:
The first term, $\int \mathrm{X}^{2} \mathrm{dF}(\mathrm{X})$, represents the expected value or the second moment of X , denoted as $\mathrm{E}\left(\mathrm{X}^{2}\right)$ :

$$
\text { Feature Selection }=\mathrm{E}\left(\mathrm{X}^{2}\right)-2 \overline{\mathrm{X}} \mathrm{E}(\mathrm{X})+\overline{\mathrm{X}}^{2} \int \mathrm{dF}(\mathrm{X})
$$

The second term, $\int \mathrm{X} \mathrm{dF}(\mathrm{X})$, represents the expected value or the first moment of X , denoted as $\mathrm{E}(\mathrm{X})$ :

$$
\text { Feature Selection }=\mathrm{E}\left(\mathrm{X}^{2}\right)-2 \overline{\mathrm{X}} \mathrm{E}(\mathrm{X})+\overline{\mathrm{X}}^{2}
$$

Finally, the third term, $\int \mathrm{dF}(\mathrm{X})$, represents the integral of the probability distribution function $F(X)$ over its entire range, which equals 1 :

$$
\text { Feature Selection }=\mathrm{E}\left(\mathrm{X}^{2}\right)-2 \overline{\mathrm{X}} \mathrm{E}(\mathrm{X})+\overline{\mathrm{X}}^{2}
$$

Therefore, the derived equation for feature selection using the integral representation is:

$$
F(S)=E\left(X^{2}\right)-2 \overline{X} E(X)+\bar{X}^{2}
$$

This equation represents the feature-selection criterion based on the second moment $\left(\mathrm{E}\left(\mathrm{X}^{2}\right)\right)$, the first moment $(\mathrm{E}(\mathrm{X})$ ), the sample mean $(\overline{\mathrm{X}})$ of the dataset, and $\mathrm{F}(\mathrm{S})$ feature selection. The enhancement in this algorithm lies in calculating the average score improvement $(\Delta S)$ for each feature. It measures the impact of removing a feature on the model's performance by considering the average improvement in the optimization criterion across multiple iterations. This helps in selecting features that consistently contribute the least to the overall performance.

# D. Emotional-Intelligence-Based Healthcare System 

## Enhanced Dynamic Bayesian Network (EDBN)

A form of Bayesian network called a dynamic Bayesian network (DBN) is able to describe and analyze dynamic systems. These networks are used in a variety of applications, including healthcare systems. In particular, DBNs can be used to model the dynamics of patient healthcare and to identify potential interventions and outcomes. For example, a DBN can be used to identify the most appropriate treatments for a patient, based on their current health state and risk factors. It can also be used to predict the potential outcomes of a particular treatment or intervention. This can help healthcare providers make more informed decisions about treatments and interventions.

An EDBN can model different aspects of a patient's health, including their medical condition, their lifestyle, and their environment. It can also represent the relationships between these factors and how they change over time. This allows healthcare providers to better understand and predict the progression of a patient's health. EDBNs are composed of a set of nodes, each of which represents a random variable, and a set of directed edges that represent the conditional dependencies between the variables. These edges can be used to represent relationships between variables, such as how a patient's symptoms can change over time.

The probability distribution equation for an enhanced Bayesian network is as follows:

$$
P(M \mid N)=P(M \cap N) / P(N)
$$

where $M$ and $N$ are two sets of random variables.
If we have variables a1, a2, a3... an, then the probabilities of a different combination of a1, a2, a3... $\mathrm{a}_{\mathrm{n}}$ are known as joint probability distribution.
$\mathrm{P}\left[\mathrm{a} 1, \mathrm{a} 2, \mathrm{a} 3, \ldots, \mathrm{a}_{\mathrm{n}}\right]$ can be written in the following way in terms of the joint probability distribution:

$$
\begin{aligned}
& =\mathrm{P}\left[\mathrm{a} 1 \mid \mathrm{a} 2, \mathrm{a} 3, \ldots, \mathrm{a}_{\mathrm{n}}\right] \mathrm{P}\left[\mathrm{a} 2, \mathrm{a} 3, \ldots, \mathrm{a}_{\mathrm{n}}\right] \\
& =\mathrm{P}\left[\mathrm{a} 1 \mid \mathrm{a} 2, \mathrm{a} 3, \ldots, \mathrm{a}_{\mathrm{n}}\right] \mathrm{P}\left[\mathrm{a} 2 \mid \mathrm{a} 3, \ldots, \mathrm{a}_{\mathrm{n}}\right] \ldots \mathrm{P}\left[\mathrm{a}_{\mathrm{n}-1} \mid \mathrm{a}_{\mathrm{n}}\right] \mathrm{P}\left[\mathrm{a}_{\mathrm{n}}\right]
\end{aligned}
$$

In general, for each variable Ai , we can write the equation as:

$$
\mathrm{P}(\mathrm{Ai} \mid \mathrm{Ai}-1, \ldots \ldots, \mathrm{~A} 1)=\mathrm{P}(\mathrm{Ai} \mid \operatorname{Parent}(\mathrm{Ai}))
$$

EDBNs also incorporate temporal information, which allows them to incorporate changes in the system as time progresses. This makes them well suited for modeling healthcare data, as the dynamics of a patient's health can change quickly over time. EDBNs are also used to model the relationships between variables in time-series data. This can be used to identify patterns in the data that may be useful for diagnosis or treatment. The proposed architecture of this research, in Figure 3, above, indicates the various data sources, such as data collected via smart phones, smart watches, hospitals, and others. These data are given to the neural network and the useful features are extracted, such as heart rate, blood pressure, and facial features such as eyes and mouth to identify the emotions of the patients. Here, the extracted features such as data for the eyes and mouth are converted into vectors and the vectors are added to the data obtained through sensor integration and given as input to the convolutional neural network, which helps in identification of the emotions of the person under various health conditions and vice versa. Here, the backpropagation algorithm with IDBN is used. The data fusion and the secure communications are achieved using the ICDF algorithm, ARFE, and IDBN network.
![img-2.jpeg](img-2.jpeg)

Figure 3. Proposed emotional-intelligence healthcare system.

# 4. Results and Discussion 

With the use of two separate sets of databases for patients with ages ranging from 25 to 60 , the findings of this study were examined. The dataset was first gathered to look at how sensor displacement affected activity recognition in actual environments. It expands on the ideas of self-placement, induced displacement, and optimal placement. As versions of extreme displacement, the ideal and mutual-displacement conditions might serve as boundary conditions for recognition algorithms. The dataset included a sizable number of people, sensor modalities, and extracted physical activities. It monitored 17 different participants as they engaged in 33 various behaviors, such as walking, running, jogging, leaping up, and jumping rope.

## Precision

The precision of each model's class predictions was measured. The calculation was performed by dividing the total number of true positives (TP) by the total number of true positives and false positives.

$$
(\mathrm{FP}) \cdot \text { Precision }=\mathrm{TP} /(\mathrm{TP}+\mathrm{FP})
$$

## Recall

Recall was computed by dividing the total number of true positives by the sum of true positives and false negatives.

$$
\text { Recall }=\mathrm{TP} /(\mathrm{TP}+\mathrm{FN})
$$

# Accuracy 

Accuracy is a measure of how accurately a model classifies all instances. It was calculated by dividing the number of true positives plus true negatives (TN) by the total number of instances.

$$
\text { Accuracy }=(\mathrm{TP}+\mathrm{FP}) /(\mathrm{TP}+\mathrm{TN}+\mathrm{FP}+\mathrm{FN})
$$

## F1 Score

The model's performance was evaluated using the F1 score, which combines precision and accuracy. The harmonic mean of precision and accuracy was used for its computation. The F-measure formula is as follows:

$$
\text { F1 Score }=2^{*}(\text { precision } * \text { accuracy }) /(\text { precision }+ \text { accuracy })
$$

In Table 1, Figure 4, it is possible to see the F1 score, accuracy, precision, recall, and ROC-AUC score of the proposed methodology (EI-EDBN), as well as comparative results using a CNN, DCNN, and FRCNN. The F1 score, accuracy, precision, recall, and ROC-AUC score of the proposed method are $92.1 \%, 97.3 \%, 95.4 \%, 96.3 \%$, and 0.52 , respectively. It is possible to see that the EI-EDBN method leads to better outcomes.

Table 1. Performance Metrics Analysis.


In addition, F1 score, accuracy, precision, recall, and ROC-AUC score using DCNN were found to be $89.3 \%, 87.4 \%, 91.4 \%, 92.1 \%$, and 0.56 , respectively, which were secondhighest to the proposed method. On the other hand, the F1 scores, accuracy, precision, recall, and ROC-AUC scores of FRCNN and CNN were low in accuracy, at $83.2 \%$ and $84.3 \%$, respectively.

Figure 5a-d display the results of the performance comparison for datasets I and II. The graph clearly illustrates how the performances of the suggested and existing tactics compare. Figure 4a displays the outcomes of the recommended EI-EDBN's recall comparison for healthcare data, and it can also be observed from the data that the recommended EI-EDBN technique yielded extremely exact results. Figure 4b displays the outcome of precision comparisons using the proposed EI-EDBN model for healthcare data. It can be noted from the results that the recommended EI-EDBN technique has excellent recall performance. Figure 4c displays the accuracy comparison of the proposed EI-EDBN model for healthcare data. So, it is concluded that EI-EDBN is the recommended strategy.

In Figure 5, the results of the performance comparison for the two datasets are displayed. The results demonstrate that the suggested approach outperformed the conventional approaches for both datasets.

Table 2 displays the performance comparison results for the two datasets. We infer from Table 2 that the performance results of the proposed approach are better for dataset 1 than for dataset 2. Figure 5a,b display the outcomes of the comparison of recall and precision for the two datasets. Additionally, it is clearly shown that the recommended technique produces superior results than the ones being used now. Figure 5c,d display the comparison of accuracy and F1 score for both datasets.

![img-3.jpeg](img-3.jpeg)

Figure 4. (a) Comparison of recall; (b) comparison of precision; (c) comparison of accuracy; (d) comparison of F1 score.

![img-4.jpeg](img-4.jpeg)

Figure 5. (a) Comparison of datasets for recall; (b) comparison of datasets for precision; (c) comparison of datasets for accuracy; (d) comparison of datasets for F1 score.

Table 2. Performance Comparison Results.


# 5. Conclusions 

Fusion-based secure healthcare with emotional-intelligence integration for sharing sensor data and the IoT is a promising approach to improving the monitoring of patient health by fusing data from various sources, including sensors and IoT devices, analyzing the data using machine learning algorithms, and detecting emotions to provide a holistic view of patient health. The merging of data from numerous sources enables healthcare practitioners to monitor patients' health in real time, identify possible health risks, and deliver prompt treatments. The use of emotional intelligence enables physicians to recognize emotional states that may have an influence on patient health and give necessary care. Secure communication is essential for maintaining the security, integrity, and availability of patient data. The EI-EDBN technique proposed in this research ensures the secured communication protocols are included in the encrypted data in transit and ensures that only authorized individuals may access the data. Also, the emotional-intelligence-trained model of this system classifies all the relevant health data from the group of patients, which makes it easier for the information provider to treat the data accurately and securely. Overall, fusion-based secure healthcare with emotional-intelligence integration for sensor data sharing and the IoT has the potential to revolutionize monitoring of patient health and improve healthcare outcomes by providing a comprehensive view of patient health, early detection of potential health issues, and timely interventions. As IoT devices and sensors are increasingly utilized in the healthcare field, this approach holds immense potential for various future applications, such as enhancing remote patient monitoring, facilitating personalized medicine, and managing population health. Moreover, this approach can be effectively applied to other areas of healthcare, such as monitoring mental health and managing chronic diseases. Furthermore, integrating emotional intelligence into healthcare can greatly impact patient satisfaction and overall quality of care. With ongoing technological advancements, there is also the potential for this approach to incorporate more sophisticated machine learning algorithms and data-analysis techniques, thereby providing more precise and individualized insights. By collaborating with industry partners and healthcare organizations, practical implementation strategies for this approach can be developed for real-world healthcare settings. In summary, the possibilities for this work are vast and have the potential to significantly enhance healthcare delivery and improve patient outcomes.

Author Contributions: Conceptualization, M.A.A.; Methodology, S.Y., M.A.A., L.A., N.K.B.C., K.K., P.V., F.H. and T.A.; Software, M.A.A. and S.Y.; Validation, S.Y., M.A.A., L.A., N.K.B.C., K.K., P.V., F.H. and T.A.; Formal analysis, S.Y., M.A.A., L.A., N.K.B.C., K.K., P.V., F.H. and T.A.; Investigation, S.Y., M.A.A., L.A., N.K.B.C., K.K., P.V., F.H. and T.A.; Data curation, S.Y., M.A.A., L.A., N.K.B.C., K.K., P.V., F.H. and T.A.; Writing—original draft, L.A.; Writing—review \& editing, S.Y., M.A.A., L.A., N.K.B.C., K.K., P.V., F.H. and T.A. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported through the Annual Funding track by the Deanship of Scientific Research, Vice Presidency for Graduate Studies and Scientific Research, King Faisal University, Saudi Arabia (Project No. Grant No. 4446) and Princess Nourah bint Abdulrahman University Researchers Supporting Project number (PNURSP2023R236), Princess Nourah bint Abdulrahman University, Riyadh, Saudi Arabia.

Institutional Review Board Statement: Not applicable in this research.
Informed Consent Statement: Not applicable for this research.
Conflicts of Interest: The authors declare no conflict of interest.
