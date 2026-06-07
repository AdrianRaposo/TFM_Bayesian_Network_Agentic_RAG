# Combine Harvester Low Crushing Rate Operation Strategy Research by Using Bayesian Network 

Yehong Liu, Dong Sun, Baoyan Xu, Shumao Wang, Xin Wang*<br>Beijing Key Laboratory of Optimized Design for Modern Agricultural Equipment, College of Engineering, China Agricultural University (East Campus), Beijing, China<br>wangxin117@cau.edu.cn


#### Abstract

As the main harvesting machinery, the combine harvester is often due to improper adjustment of its operating parameters resulting in increased crushing rate and grain waste during the harvesting process. To quickly obtain the working range of key operating parameters under low crushing rate, this study conducted field tests on the relevant parameters affecting the crushing rate and finally selected the travel speed, feed rate, threshing drum speed, concave clearance, and crushing rate as node variables for the construction of the Bayesian network model. Based on the "search-and-score" algorithm, the best network structure can be obtained using the combination of the Akaike Information Criterion (AIC) scoring function and the hill-climbing method. In the obtained network, adjusting the proportion of the lowest level of the crushing rate nodes to $100 \%$, the operation strategy under the condition of low broken rate obtained by the network reasoning was: feed rate < $6 \mathrm{~kg} / \mathrm{s}$, travel speed $<5 \mathrm{~km} / \mathrm{h}$, concave clearance $=10 \mathrm{~mm}$, threshing drum speed $<900 \mathrm{rpm}$. Three field trials were carried out using this optimized operation strategy, and the measured crushing rates were $0.93 \%, 0.95 \%$, and $1.07 \%$, respectively, and the average crushing rate was $0.98 \%$. At the same time, when the optimized strategy was not used, the crushing rates were, respectively, $1.12 \%, 1.41 \%$, and $1.93 \%$, and the average crushing rate was $1.48 \%$. The test results prove that the operation strategy based on Bayesian network inference can effectively reduce the crushing rate in the harvesting process.


Index Terms-Combine harvester; Operation parameters; Low crushing rate; Bayesian network.

## I. INTRODUCTION

The combine harvester is the most widely used machinery when harvesting crops and can complete multiple procedures such as reaping, threshing, sieving, cleaning, and collection in the field. Therefore, when crops enter the harvester, they will be subjected to various mechanical movements such as pounding, vibration, and rolling, and these mechanical movements always damage the grain of the crop to a certain extent [1]. The crushing rate is often used as an important indicator to measure the work quality of the combine harvester and is generally defined as the percentage of grain mass caused by mechanical damage to the total grain mass harvested [2], [3]. A large number of broken grains, in
addition to reducing the economic benefits of farmers, are more prone to mildew and deterioration that affects the breeding process [4]. The harvesting process of the combine harvester is shown in Fig. 1. At present, there has been much research on the formation mechanism of crushing rate in the harvesting process. The force and movement state of the grain in the threshing and separation process are analyzed based on the functional principle, the dynamic principle, and other methods, thus improving the design parameters of the components to achieve the effect of reducing the mechanical damage during the harvesting process [5]-[9]. The important point is that component design errors and unsuitable working parameters, especially in the threshing and separation system, are the main reasons for the crushing rate. For example, the shape of the spike of the cylinder, the threshing method, and the threshing speed will affect the crushing rate [10]-[15]. In addition to mechanical factors, the crushing rate is also affected by the moisture content. The rotation speed of the threshing drum must be adjusted appropriately to reduce the damage to the seeds or pods of the crop when harvesting crops with different moisture content [16], [17]. Most of these studies use the mathematical model-driven method; especially, the Response Surface Analysis (RSA) has been widely used. This kind of method can be summarized into three parts. First, the values of the operation parameters and the crushing rate are obtained through field experiments. The second step is to analyze the influence of each operation parameter on the crushing rate through Design-Expert and build a mathematical model that takes the crushing rate as a dependent variable and the operating parameter as independent variables. Finally, the optimal combination of operating parameters under low crushing rate is obtained by using the multi-objective parameter optimization. The time cost of completing the above process is high, especially in the steps of mathematical modeling and solution. On the other hand, only the relationship between each parameter and the crushing rate is studied, and the interaction between different operation parameters has not been paid attention to.

In recent years, machine learning technology has also been applied to the monitoring of the crushing rate. The purpose of distinguishing crushing grains can be realized by using Back Propagation (BP), Convolutional Neural Networks (CNN),

decision tree, or other methods to identify grayscale images or hyperspectral images which collected from the unloading process or granary [18]–[20]. However, this class of methods mostly obtains data sets from an ideal experimental environment and is rarely used in actual wheat harvest.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Combine harvester harvesting process.

In summary, by redesigning key components or adjusting operating parameters, the crushing rate can be reduced and predicted. However, it takes a long time to redesign components, and the method of constructing operation parameters and crushing rate models requires strong mathematical analysis capabilities, making these two methods not suitable for ordinary farmers in the daily harvesting process. Recently, manufacturers, such as CASE, New Holland, and Fendt, have built-in different harvesting strategies, such as optimal seed quality, lowest seed loss/broken, and best cleaning quality [21]. In fact, there are many types of combine harvesters used by farmers. Obtaining the operation strategy with a low crushing rate according to the farmers' own models and the harvesting environment to improve harvesting quality is an urgent problem in the current harvesting process.

With the aim of solving the above problems, a method of using Bayesian network to obtain the operation parameters for combine harvesters under low crushing rate was proposed. The process is mainly as follows. Firstly, we selected the factors that have a greater impact on the crushing rate: feed rate, threshing drum speed, concave clearance, and moisture content. Then a four-factor three-level orthogonal experiment was carried out in the wheat field and the influence of each factor on the crushing rate was analyzed. A discrete Bayesian network was constructed with nodes such as travel speed, feed rate, concave clearance, threshing drum speed, crushing rate, and the scoring function was combined with the hill-climbing method to obtain the optimal network structure. To obtain the optimal combination of operation parameters under the lowest crushing rate, the lowest level of the crushing rate nodes in the network was set to 100 % so that the range of each parameter was obtained through Bayesian inference. Experiments have proved that wheat harvested under this strategy can achieve a lower crushing rate than wheat harvested by experience.

Compared to RSA and machine learning in existing research, the use of a Bayesian network has the following advantages:

1. The use of network graphics can more intuitively express the relationship between each parameter and the crushing rate, which is convenient to understand;
2. It can not only analyze the influence of each operation parameter on the crushing rate, but also analyze the interaction between operation parameters;
3. The data obtained from field experiments are directly used to construct a Bayesian network, which effectively reduces the time cost of mathematical modeling.

## II. METHOD USED FOR REASONING OPERATION STRATEGY

### A. Bayesian Network

The Bayesian network was used to mine the nexus between each important operation parameter and the influence of each parameter on the crushing rate to obtain the operation strategy under the low crushing rate.

The Bayesian network is a probabilistic graph model, first proposed by Pearl in 1985, and through the Bayesian network, rigorous probabilistic reasoning can be displayed graphically [22]. The network nodes represent random variables, and causal (or non-conditional independent) variables are connected with arrows. One node at both ends of the arrow is the "cause" and the other node is the "effect", and there will be a conditional probability value between these two nodes.

Building a Bayesian network requires determining the structure and parameters of the network. In this study, the experiment data set was a complete data set (no missing or observed abnormalities) so that no parameter learning is required. Therefore, based on the Bayesian method, the conditional probability distribution between various variables was calculated and the nodes with causal relationship were connected to form a network.

The score-based search method was used to learn the best Bayesian network structure in this study. This method regards Bayesian Net (BN) structure learning as a

combinatorial optimization problem and determines the structure that best fits the data by searching the space of the network structure composed of nodes. But according to Robinson's reasoning, when the number of variables increases, the dimensionality of the search space increases exponentially and it is difficult to quickly obtain the optimal solution [23]. Therefore, the following method, as shown in

![img-1.jpeg](img-1.jpeg)

Fig. 2. The construction process of the Bayesian network.

### *B. Scoring Function and Searching Method*

In Bayesian networks, the relationship between the parent node and the child node is expressed by conditional probability, and the scoring function is a measure of the strength of the relationship between the parent node and the child node. In this study, the network structure was judged by the scoring function, respectively, based on Bayesian method and information theory. The commonly used scoring functions based on the Bayesian method are the K2 score and the Bayesian Dirichlet-Likelihood Equivalent (BDe) score, and the definition formulas of the two scoring functions refer to the related literature [24]. Generally, Akaike Information Criterion (AIC) is based on the concept of entropy, which is a weighted function of the accuracy of the fitting and the unknown number of parameters. The Bayesian information criterion (BIC) was proposed by Schwarz in 1978 and used log-likelihood to measure the degree of fit between the network structure and the data [25]. The hill-climbing method was used to find the optimal structure of the network. This algorithm chooses an optimal solution - from the adjacent solution space of the current solution - as the current solution each time, and its main content is divided into two parts:

1. Local operations (add edge, reduce edge, delete edge), the score is used as the criterion for whether to choose the operation;
2. Determine whether to update the model structure by greedy selection.

### III. BAYESIAN NETWORK CONSTRUCTION PROCESS

#### *A. Data Collection*

In June 2019, a Lovelink GM80 was used in Weifang City, Shandong Province, to conduct a wheat harvest test. A 50-acre field was selected and the wheat grew evenly and without lodging in the test field. The following describes the collection and calculation methods for each key parameter.

The F20 high-precision GPS module (measurement accuracy of 0.05 m/s) was used to collect the travel speed of the combine harvester. The speed of the threshing drum was collected by an encoder. The data of the travel speed and the rotation speed of the threshing drum were transmitted to the STM32 processor of the terminal (installed in the cab of the combine harvester) through the Controller Area Network (CAN) protocol, and the data are processed and stored. The data acquisition system is shown in Fig. 3.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Data collection system.

The feed rate of the combine harvester is defined in (1)

$$q = \rho H v (1 + \delta), \tag{1}$$

where *q* is the feed rate (kg/s), *ρ* is the crop density (kg/m<sup>2</sup>), *H* is the cutting width (m); *v* is the travel speed (m/s), and *δ* is the grass-to-grain ratio.

Usually, the cutting width was constant when the combine harvester was working, the *ρ* and *δ* were measured according to the "five-point method" to calculate the feeding amount. Each sampling site had an area of 1 m<sup>2</sup>, as Fig. 4 shows, and the wheat was cut manually and its mass was weighed. Finally, we took the arithmetic mean of the mass of the five points as *ρ* in the experimental area. In addition, the wheat was completely threshed and the stalk mass and grain mass were weighed, respectively, and the ratio of the two masses was the *δ*.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Five-point method used for sampling.

The five-point method was also applied for moisture, 50 g of samples were taken at each point, and the moisture content of the grains obtained was measured with the QLY-DR measuring instrument. The concave clearance was adjusted manually to obtain different concave clearance values.

The orthogonal test method was used to quickly obtain the data, and the Ls(34) orthogonal table was constructed as Table I.

moisture
content | Threshing
drum speed
(pm) | Travel
speed
(km/h) | Concave
clearance
(mm)  |

TABLE I. ORTHOGONAL TEST CONDITION.

The selection of the level of each factor was based on the following:

1. Rotation speed of the threshing drum

The rated working speed of the threshing drum of GM80 combine harvester is about 1000 rpm. To explore the influence of different threshing drum speeds on the quality of operation, in combination with related research, the threshing drum speed was set at 900 rpm, 1000 rpm, and 1100 rpm.

1. Feed rate and travel speed

The density of the crop in the same area is approximately constant and the amount of feeding is positively related to the operating speed. Therefore, a different feed rate can be calculated by adjusting the travel speed. The feed rate of the GM80 model during normal harvesting is 8 kg/s and the corresponding travel speed is 6 km/h, thus set the travel speed of the harvester to 4 km/h, 6 km/h, and 8 km/h to explore the impact of different feed rates on the operation quality.

1. Concave clearance

Concave clearance generally maintains a constant value during the harvesting process. To prevent stoppage, three types of concave clearance of 10 mm, 15 mm, and 20 mm were selected.

1. Moisture content

Experiments were carried out, respectively, in the morning, middle, and evening, and the average value of the crop moisture content in the three time periods was 15.1 %, 13.3 %, and 14.4 % using the five-point sampling method.

Due to the existing monitoring technology of crushing rate, it is basically based on the ideal state of the grain in the laboratory environment. Therefore, as can be seen in Fig. 5, the manual sampling method was used in this study to calculate the crushing rate of each test.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Manual selection of broken grain and calculation of the broken rate.

B. Data Preprocessing and Initial Analysis

The complex field environment and the influence of the vibration of the combine harvester itself lead to abnormal data in the data obtained in the experiment. To accurately construct the crushing rate model, the Grubbs criterion was used to eliminate abnormal values in the original data. The main steps are as follows:

1. Calculate the residual of each data point

$$v_i = x_i - \overline{x}. \tag{2}$$

1. Estimate standard deviation according to the Bessel method

$$\hat{\sigma}(x) = \sqrt{\frac{\sum_{i=1}^{n} v_i^2}{n-1}}.\tag{3}$$

1. Calculate the inspection value

$$G = \frac{|v_i|}{d(x)}.\tag{4}$$

1. Select the appropriate confidence level (selected inhere α = 0.05) and query the Grubbs critical value table to obtain the critical value G0.

1. Compare the size of the test value G and the critical value G0; if G > G0, discard the abnormal data.
2. Repeat steps (1)~(5) until there are no abnormal data in the sample data set.

The data collected by the orthogonal test were processed according to the Grubbs criterion, and the abnormal data in the data column were gradually discarded. Then the normal value of each column was averaged and finally 636 data records were obtained. Some of the data are shown in Table II.

TABLE II. PART OF THE FINAL TEST DATA RESULTS.

|  Test
No. | Feed rate
$(\mathbf{k g} / \mathbf{s})$ | Threshing drum speed
$(\mathbf{r p m})$ | Travel speed
$(\mathbf{k m} / \mathbf{h})$ | Grain moisture content
$(\%)$ | Crushing rate
$(\%)$ | Concave clearance
$(\mathbf{m m})$  |

Note: The combine harvester has been adjusted to the best working condition before the test.

To preliminarily determine the structure of Bayesian network, the influence between the operation parameters and the crushing rate was analyzed. In the actual harvesting process, farmers cannot change the grain moisture content at any time, so the grain moisture content was not used as a node in the Bayesian network. In addition, the influence of threshing drum speed and feed rate on crushing rate was analyzed under different concave clearance, when grain moisture content was at medium level. The image is as follows in Fig. 6.

![img-5.jpeg](img-5.jpeg)

Fig. 6. The impact of selected key operating factors on the crushing rate: (a) Concave clearance $=10 \mathrm{~mm}$; (b) Concave clearance $=15 \mathrm{~mm}$; (c) Concave clearance $=20 \mathrm{~mm}$.

It can be seen from the figures that when the concave clearance was 10 mm , the crushing rate increased as the feed rate increased, and when the speed of the threshing drum increases, the crushing rate decreases. And when the feed rate was low and the threshing drum speed was high, the crushing rate was at the lowest value and the crushing rate was at the maximum when the feeding amount was higher and the threshing drum speed was low. When the concave clearance was 15 mm or 20 mm , although the crushing rate decreased when the feed rate was higher, the crushing rate increased slightly when the speed of the threshing drum increased.

## C. Bayesian Network Construction and Optimization

It can be seen from Fig. 6 that the relationship between the crushing rate and each parameter is not completely linear, so it is difficult to obtain the specific conditions of each parameter under the low crushing rate by solving the equation. However, the Bayesian method can realize the reasoning of "from effect to cause" and obtain the numerical value of each operation parameter that satisfies the low crushing rate.

The BN was constructed by taking the feed rate, drive speed, threshing drum speed, concave clearance, and the crushing rate as the node variables. Since a discrete Bayesian network needs to be constructed, the data needed to be hierarchically processed. The final result of the division (in Table III) was based on the level of division of each parameter in the orthogonal experiment.

TABLE III. THE SPECIFIC SITUATION OF THE NODES OF THE BAYESIAN NETWORK.

name | Level 1 | Level 2 | Level 3 | Level 4  |
speed (rpm) | rotation | $<900$ | $900-1000$ | $1000-1100$ | $>1100$  |
|  Concave clearance
$(\mathrm{mm})$ | gap | 10 | 15 | 20 | -  |

After determining the network nodes, enter the collected data into the program after grading, and the Bayesian network was initially constructed as shown in Fig. 7. In the constructed initial network structure, only the relationship between each parameter and the crushing rate was connected. The nodes were represented by boxes that contained the

name of the node, the division level, and the probability of each level.

The AIC, BIC, K2, and BDe scoring functions combined with the hill-climbing method were used to iteratively search for the optimal network structure. The hill-climbing method uses three search operators to optimize the Bayesian network, and the iterative process is shown in Fig. 8. With the continuous iteration of the hill-climbing method, the update process of the network structure is shown in Fig. 9, where the red, blue, and green circles represent "add arc", "reduce arc", "reverse arc". "Add arc" means that there is a connection between two nodes, and a connecting arc needs to be added; "reduce arc" means that there is no connection between two nodes, and a connecting arc needs to be subtracted; "reverse arc" means that the influence between two nodes is opposite, the direction of the arc side needs to be reversed.

The final network structure scores obtained in the four scoring functions are shown in Table IV, and the final network structure obtained under the AIC score got the highest score. As shown in Fig. 10, this network structure was chosen to infer the harvest strategy under a low crushing rate.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Preliminary construction of the Bayesian network mode.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Iterative steps to find the optimal network structure using the hill-climbing method.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Update process of network structure: (a) Initial network structure; (b) Update of the candidate network structure.

![img-9.jpeg](img-9.jpeg)

Fig. 10. Optimal Bayesian network structure.

TABLE IV. STRUCTURE SCORES IN DIFFERENT SCORING FUNCTIONS.


IV. ANALYSIS AND VERIFICATION OF THE HARVEST STRATEGY WITH LOW CRUSHING RATE

A. Low-Breaking Rate Harvesting Strategy

Set the proportion of the first level in the crushing rate node to 100 %, as shown in Fig. 11, and the probability value of each grade in the remaining nodes in the network will also change accordingly. When the crushing rate was at the lowest level, the first level of (< 5 km/h) travel speed accounted for the highest proportion is 72.8 %; the first level of concave clearance (10 mm) accounted for the highest proportion is 74.5 %, and the threshing drum speed was at the first level (<

900 rpm) and accounted for the highest proportion is 70.1 %.

![img-10.jpeg](img-10.jpeg)

Fig. 11. The state of the network under low crushing rate.

### *B. Strategy Verification*

The operation strategy obtained by Bayesian reasoning was used as the experimental group, and the harvesting strategy set by the operators based on experience was used as the control group, and three experiments were carried out, respectively. The test process records and the breaking rate results are shown in Table V.

**TABLE V. VALIDATION TEST RESULTS OF THE LOW CRUSHING RATE HARVESTING STRATEGY.**


Numbers 1, 3, and 5 in the table are test groups. The crushing rates of the three tests were 0.98 %, 0.95 %, and 1.07 %, and the average crushing rate was 0.98 %. Numbers 2, 4, and 6 are the control groups, which were harvested according to the experience of the harvester driver, and the crushing rates were 1.12 %, 1.41 %, and 1.93 %, respectively, and the average crushing rate was 1.49 %. The crushing rate of each item in the experimental group was lower than that of the control group, indicating that the operating strategy obtained by Bayesian inference was effective.

### **V. CONCLUSIONS**

To obtain the optimal combination of operating parameters under the low crushing rate of the combine harvester, a Bayesian network-based solution method is proposed in this paper. The contributions of this paper are as follows:

1. In the constructed Bayesian network, travel speed, feed rate, threshing drum speed, concave clearance, and the crushing rate are nodes, and the relationships between each node are represented by a one-way arrow, which intuitively expresses the interaction between parameters and breakage rate.

2. Four scoring functions (AIC, BIC, BDe, and K2) were combined with the hill-climbing method to obtain the optimal network structure, which improves the accuracy of the network structure describing the relationship between parameters and the crushing rate.

3. The optimal combination of operation parameters at a low crushing rate, which was obtained by reasoning based on the optimal network structure, was: travel speed < 5 km/h, feed rate < 6 kg/s, threshing drum speed < 900 rpm, and concave clearance = 10 mm. The test results showed that the average crushing rate was reduced by 0.51 % with this strategy than without this strategy.

The field test results have demonstrated the correctness of the proposed method. However, during the test, only one type of combine harvester was used, so further study is needed to study the effectiveness of the proposed method when other combine harvesters are used or in different wheat fields.

### **CONFLICTS OF INTEREST**

The authors declare that they have no conflicts of interest.
