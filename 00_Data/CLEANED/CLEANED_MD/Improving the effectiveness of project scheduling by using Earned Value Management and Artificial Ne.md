# Improving the effectiveness of project scheduling by using Earned Value Management and Artificial Neural Network 

## Mejorar la eficacia de la programación de proyectos mediante el uso de la gestión del valor ganado y redes neuronales artificiales

Soetjipto, Jojok Widodo * ${ }^{1}$ https://orcid.org/0000-0003-0026-8296<br>Ratnaningsih, Anik* https://orcid.org/0000-0002-1970-4927,<br>Arifin, Syamsul * https://orcid.org/0009-0004-3784-3236,<br>Adinanda, Della Ayu * https://orcid.org/0009-0002-5939-0798,<br>Wicaksono, Kristya Hadi * https://orcid.org/0009-0003-1150-6904

* Universitas Jember, Jember, INDONESIA

Fecha de Recepción: 17/06/2024
Fecha de Aceptación: 19/07/2024
Fecha de Publicación: 01/08/2024
PAG: 161-173

## Abstract

During construction, uncontrolled resources impact project performance. Earned Value Management (EVM) is a widespread method used for project management based on time and cost control. Advances in Information Technology (IT) provide options to improve the EVM method. The EVM is a project-level method that excludes detailing the behavior of project parameters at the level of construction operations, they are handled in aggregated economic terms over time. Thus, this work studies the improvement of EVM using IT to express the handling of operational variables. This article uses a road construction project as a case study, to evaluate three approaches (i.e., Bayesian Network (BN), Artificial Neural Network (ANN), and Hybrid EVM-ANN) as improvement options for the EVM method. It was found that the ANN provides the best improvement of EVM results. The use of ANN and project parameters improves the handling of EVM. By mayor forecast effectiveness, is expected to improve the quality and availability of data for decision making, a condition which in turn may improve agility and adaptability of the project as-built outcomes. The model EVM-ANN uses parameters that influence project implementation completion, making it easier to assess project time performance based on various conditions in the field so that the project can obtain the best strategy to ensure project completion on time.
Keywords: EVM; ANN; BN; project scheduling performance; agility.


## Resumen

Durante la construcción, los recursos no controlados impactan el desempeño del proyecto. La Gestión del Valor Ganado (GVG) es un método ampliamente utilizado para la gestión de proyectos basado en el control de tiempos y costos. Los avances en las Tecnologías de la Información (TI) brindan opciones para mejorar el método GVG. El GVG es un método a nivel de proyecto que excluye detallar el comportamiento de los parámetros del proyecto a nivel de operaciones de construcción, se manejan en términos económicos agregados a lo largo del tiempo. Por lo tanto, este trabajo estudia la mejora del GVG utilizando TI para expresar el manejo de variables operativas. Este artículo utiliza un proyecto de construcción de carreteras como caso de estudio, para evaluar tres enfoques (es decir, Red Bayesiana (RB), Red Neuronal Artificial (RNA) y EVM-RNA Híbrida) como opciones de mejora para el método GVG. Se encontró que la RNA proporciona la mejor mejora de los resultados del GVG. El uso de la RNA y los parámetros del proyecto mejora el manejo del GVG. Al tener una mayor efectividad en los pronósticos, se espera que mejore la calidad y disponibilidad de los datos para la toma de decisiones, una condición que a su vez puede mejorar la agilidad y adaptabilidad de los resultados del proyecto tal como está construido. El modelo EVM-ANN utiliza parámetros que influyen en la finalización de la implementación del proyecto, lo que facilita la evaluación del desempeño del tiempo del proyecto en función de diversas condiciones en el campo para que el proyecto pueda obtener la mejor estrategia para garantizar su finalización a tiempo.

Palabras clave: EVM; ANN; BN; desempeño de la programación de proyectos; agilidad.

[^0]
[^0]:    ${ }^{1}$ Corresponding author:
    Universitas Jember, Jember, INDONESIA
    Corresponding author: jojok.teknik@unej.ac.id

# 1. Introduction 

Construction projects require vast amounts of resources and many variants. The resources utilized influence project schedule development. The existence of uncontrolled resources will cause ineffective scheduling and be difficult to modify as the project progresses (Fang et al., 2024). Therefore, the project schedule must be prepared carefully (Mehrdad et al., 2021). The previous study has used several methods in arrangement schedules, including Earned Value Management (EVM) (Cândido et al., 2014), the use of metaheuristics (Mehrdad et al., 2021), the use of Bayesian Networks (BN) (Chang, 2021), Monte Carlo (Agustin et al., 2023), Viable and Antifragile Project Management (VAPM) (Lotfi et al., 2023), and others.

In traditional project management, performance measurement uses EVM, which combines three main project parameters: work progress, finances, and time. EVM provides a way to comprehensively monitor project performance by comparing planned performance with actual performance, identifying variations, and estimating the project's final duration and cost. This technique is considered more advanced than traditional measurement tools such as PERT, Cost, and Schedule Control Systems Criteria (C/SCSC) (Cândido et al., 2014). EVM results from a study of various good practices by senior project managers, recorded as Body Knowledge Project Management guidelines. The Project Management Institute (PMI) issued this guidebook (Project Management Institute, 2021).

EVM is a cost and time control method integrated by measuring cost and time performance. Traditional scheduling methods often need to be corrected in estimating project conditions, resulting in errors in determining duration, inefficiency, frequent delays, etc. The EVM correctly can have a good impact, including achieving project costs, determining the project's scope, scheduling control, anticipating project delays, and communicating (Netto et al., 2020). The EVM can produce the Variance of schedule and cost (SV and CV), the Performance Index of Schedule and Cost (SPI and CPI), the estimate to completion (ETC), the estimated project completion time (EAS), and the estimated all-cost (EAC) (Arifin et al., 2023). Therefore, effective management of resource allocation and scheduling by EVM in construction projects is critical; besides that, these elements also greatly influence each other between schedule and project costs.

The EVM can not support the implementation of lean construction, which needs measurement techniques grounded in the physical and qualitative aspects of production progress. The EVM is simply an extension of the traditional approach of measuring work and financial progress over time, unable to provide a comprehensive managerial tool for analyzing building projects due to insufficient consideration of resource mobilization and indirect construction costs (Cândido et al., 2014). Meanwhile, Lean Construction creates excellent production systems that optimize, reduce, or eliminate workflows to improve delivery and production times (Garcés y Pena, 2023). The Lean Construction method combines collaborative production planning and control within a team so that EVM needs to be aligned with transparent operations and production plans, project workflows can be measured objectively such as Percent Plan Complete (PPC), Schedule Variance (SV), and Cost Variance (CV) (Novinsky, 2018). Therefore, the EVM approach uses current performance data to predict future conditions with the consideration of validation and other project variables.

The latest developments in the world of construction today require the feasibility of project scheduling, especially in complex situations. Awareness of resilience is vital because of disruptions in planning and scheduling and the resulting negative impact of project managers' thoughtlessness (Nachbagauer, 2022). Sustainability in project management is needed to formulate multi-objective decision-making problems by considering essential sustainability factors, such as planning, monitoring, and controlling projects highly depend on the life cycle's financial, environmental, and companionable aspects (Chawla et al., 2018). Resilience is an attempt to encounter sudden disappointments while improving functionality after a disruption (Lotfi et al., 2023). So, it requires project management that applies against fragility, resilience, sustainability, and skillfulness in various planning and scheduling phases for complex networks and systems.

Advances in information technology, computing, and scientific analysis methods have provided many benefits to knowledge and practice in construction. Several prediction models have succeeded in estimating future conditions well. The BN method provides an estimation method through probabilistic inference by considering uncertainty weights. This method has been used to determine estimated project completion times (Wicaksono et al., 2023), can be used as an efficient tool for detecting train delays (Lessan et al., 2019), able to manage and predict safety risks in construction (Zhang et al., 2014), able to model leadership on very complex construction projects (Shen et al., 2024). The Viable and Antifragile

Project Management (VAPM) method applies antifragility, resilience, sustainability, and skillfulness in complex network and system planning and scheduling phases (Tomov, 2022). This method can reduce negative impacts in planning and scheduling due to the unknown to many project managers. Several new methods and technologies have been applied in lean project management through reducing network complexity, namely the Internet, blockchain, and Artificial Intelligence (AI). (Lotfi et al., 2023). The hybrid multi-objective particle swarm optimization (MOPSO) method and EVM theory can identify and predict the project's overall performance (Lotfi et al., 2023). The AI can speed up schedules, reduce costs, and overall failure to complete construction projects (Abishek et al., 2023). Intensive System of Systems (SISoS) and Agile Software can generate operator feedback to ensure the project meets objectives (Gates, 2008). The ANN model can evaluate the influence of coordination factors on construction project performance (Alaloul et al., 2018). Apart from that, the ANN method can also predict project performance based on factors that influence the project, such as project party coordination, scheduling, project experience, and senior managers' support (Maya et al., 2023).

Therefore, this paper will review the improvement of the EVM method with the BN or ANN method (whichever has the highest accuracy). The selected hybrid model can help make accurate, practical, and agile decisions in project scheduling.

# 1.1. Research Objective 

The objective of this study is to describe the meaning of EVM improvement efforts using other methods to obtain a hybrid model that can improve the quality of decision-making, which in turn can increase the agility and adaptability of the results of the project schedule planning.

This article is organized as follows: Section 2 describes the methods used in this study; Section 3 describes the results of the project data analysis; Section 4 discusses the implications of EVM improvements on project time performance; finally, the full text is summarized in Section 5, which presents conclusions and recommendations for future research on project time performance.

## 2. Methods

In this research, the researcher developed a project performance prediction model to obtain the project schedule's accuracy, effectiveness, and agility results. (Figure 1) shows the design, stages, and milestones of the research. The research starts by analyzing project data, including schedule, environmental conditions, construction methods, and project management. This data is needed to calculate project time performance and provide input in compiling factors that influence the project. This study analyzed data with extensive surveys and interviews with professionals about the list of all activities, the duration and relationship of each activity, factors influencing the project, and other relevant data.
![img-0.jpeg](img-0.jpeg)

Figure 1. Research design and its milestone

# 2.1. Project Brief Review 

This project is located on the southern causeway (Trans-South Java Road Project Development Tulungagung Serang - Malang), which connects three districts in East Java. This project requires a planned duration of 131 weeks, funded by the Indonesian Budget. The advantages of the objects studied in the project are that they have a wide area, open field, and extensive rock and soil excavation works, which have a high risk of achieving their project goals. It requires an adequate construction method, i.e., equipment, blasting systems, and speed-up completion. Suboptimal impact control can affect the failure of quality, quantity, cost, and time.

The research object's weakness is the construction of a new road on the south coast, which is a few kinds of work constrained by rugged terrain and no source of materials produced directly at the project site, requiring materials from outside projects. This project has a very tight schedule with extreme work locations, so the risk of project delays is very high if not managed well. The $S$ curve data that the project team has prepared is based on the project conditions so that at the start of the project, it can exceed the set targets, but at the end of the project, there are many obstacles resulting in delays. At this stage, data will be produced on the planned schedule and the realization of the results of project work implementation. This data will calculate the SPI (Schedule Performance Index) value.

The analysis in this study uses data from weeks 1 to 110 as generator data, while weeks 111 to 121 are the prediction results from three methods, namely EVM, BN, and ANN.

### 2.2. Scheduling and SPI Analysis

EVM measures current performance based on Planned Value (PV), Earned Value (EV), and Actual Cost (AC). PV is a monetary value plan for a specific period or progress according to the Scheduled Work Cost Budget (BCWS) schedule. EV is the amount of financial value based on the work budget plan, calculated according to the work items completed in a certain period. This value is called the Budget Cost of Work Performed (BCWP). AC is the actual expenditure during a specific period, referred to as the Actual Cost of Work Performed (ACWP). ACWP is obtained from recording financial reports through a cost planning and control system (Project Management Institute, 2021). The Schedule Performance Index (SPI) measures the efficiency of project time utilization, which is calculated based on the Schedule Variance (SV) value. Calculation analysis uses the following equation (Project Management Institute, 2021) (Equation 1), (Equation 2):

$$
S V=E V-P V
$$

$$
S P I=E V / P V
$$

SPI shows the progress/delay of work progress against the scheduling plan. SPI > 1 means work progress is more significant than planned, SPI = 1 means progress is according to plan, and SPI < 1 indicates a delay from the plan. SPI can help project managers identify trends over time and estimate the duration of project completion. Future performance can be determined using the geometric average of project performance when measuring SPI.

### 2.3. Prediction Completion Project Based on EVM

EVM is an important factor in estimating project trajectory and outcomes. EVM requires real project progress data so that project managers can make decisions easily. However, EVM has major challenges, namely errors in interpreting data, inappropriate application of EVM metrics, or lack of training among team members. This can lead to inefficient use. The prediction model using EVM can be seen in (Figure 2).

![img-1.jpeg](img-1.jpeg)

Figure 2. Estimate at Completion Prediction and Estimate to Complete
Source: (EVM Analysis)

# 2.4. Prediction Completion Project Based on BN 

Previous research has shown that the BN Model is a tool for predicting the probability of an event based on previous events. Applications of BN predictions include project completion time estimates (Wicaksono et al., 2023), efficient tools for managing train schedules (Lessan et al., 2019), tools for managing and predicting safety risks in construction (Zhang et al., 2014), able to become a leadership model on very complex construction projects (Shen et al., 2024). A simple Bayesian network usually consists of a parent node, child nodes, and arrows representing the relationships between the nodes. Nodes $A$ and $B$ are the parents, and node $C$ is the child, as shown in (Figure 3).
![img-2.jpeg](img-2.jpeg)

Figure 3. Simple Bayesian Network
Source: (Soetjipto, 2018)
The Bayesian model uses the formula (Chang, 2021) (Equation 3), (Equation 4):

$$
\begin{gathered}
P(B \mid A)=\frac{P(A \mid B) P(B)}{P(A)} \\
P(A)=\sum_{i} P\left(A \mid B_{i}\right) P\left(B_{i}\right)
\end{gathered}
$$

$P(B \mid A)=$ probability of event $B$ occurring when $A$ has already occurred (posterior) (the functional predictive); $P(B)=$ Prior probability of event $B$ without considering other factors; $P(A \mid B)$ is the likelihood ratio; $i=$ number of events (Equation 5).

$$
\mathrm{P}(\mathrm{~A}, \mathrm{~B}, \mathrm{C})=\mathrm{P}(\mathrm{C} \mid \mathrm{A}, \mathrm{~B}) \mathrm{P}(\mathrm{~A}, \mathrm{~B})=\mathrm{P}(\mathrm{C} \mid \mathrm{A}, \mathrm{~B}) \mathrm{P}(\mathrm{~A} \mid \mathrm{B}) \mathrm{P}(\mathrm{~B})
$$

In BN, there are parent node variables and child variables. There are two categories of relationships between the two variables, namely: (i) shallow logical relationships, namely conditional probability nodes that can be calculated directly through logical analysis, and (ii) the parent node relationship model influences child nodes through synthetic actions which are usually conditional probability tests given by experienced people or experts (Chang, 2021).

# 2.5. Prediction Completion Project Based on ANN 

Given a set of data indicating a mapping from one multivariate information space to another, an artificial neural network (ANN) is a computational mechanism that can acquire, represent, and figure that mapping. An ANN comprises several layers of mutually coupled neurons or linking processing elements. An ANN typically consists of three layers: input, hidden, and output. Outside sources provide information about the inquiry to the input layer. The hidden layers are connected to other layers rather than the exterior. The result is sent outside by the output layer. The number of layers (one-layered and multi-layered networks), the type of connection between neurons (layered, wholly linked, and cellular), and the type of learning process (feed-forward and feedback) are used to categorize different types of networks (Maya et al., 2023). (Figure 4) depicts a typical feed-forward ANN structure architecture using Mahlab.
![img-3.jpeg](img-3.jpeg)

Figure 4. Typical structure of feed-forward ANN
Source: (Mathlab Analysis)
Three well-defined parameters are necessary for practical training: learning rate, momentum factor, and training/testing tolerance. The variable known as tolerance indicates how precise the network's output has to be for it to pass testing and training. Rather than being expressed as the output value, the most significant tolerance is expressed as a $\%$ of the output range. For instance, if the tolerance is set to 0.1 , the output value must fall between $10 \%$ and the output's range to be deemed accurate. The network performance may suffer if a too-loose (big) or too-tight (minor) tolerance is chosen (Darwish, 2024).

Consequently, the tolerance in this investigation was established at 0.025. The network's learning rate determines the number of steps to navigate through the weight and reduce error. A learning rate adjustment of 0.7 or 0.8 was made for this investigation. On the other hand, applying a momentum component multiplied by the prior weight change solves the learning rate balance problem. It allows for quick adjustments even while the learning rate is controlled. This study chose a momentum factor of 0.9 (Alaloul, 2018).

Learning to adjust weights or connection strength is called network training. The trial networks used in this study were trained using Back-propagation and Elman-propagation learning algorithms in a supervised mode (Mahdi et. al, 2023). Three subsets were created from the obtained data: the training set received $80 \%$ of the data ( 100 weeks), the validation set received $10 \%$ ( 10 weeks), and the test set received $10 \%$ ( 10 weeks). The network was given the training data set as inputs, and calculations were made for the outputs. The network weights are adjusted based on the discrepancies between the computed and target outputs. This process continues until the error converges to an acceptable level. Therefore, it uses (Equation 6) expression of the MSE to minimize the construction of the input-to-output mapping (Mahdi et. al, 2023) (Equation 6):

$$
M S E=\frac{\sum_{i=1}^{n}\left(o_{i}-P_{i}\right)^{2}}{n}
$$

Where $n$ is the number of samples in the training phase, $O i$ is the target output related to the sample $i(i=1,2,3 \ldots n)$, and $P i$ is the predicted output from the network.

ANN is a purely empirical model; therefore, the validation phase is critical to successful training and operation. The network validation aims to ensure its ability to generalize within limits robustly set by the validation data rather than simply memorizing the input-output relationships contained in the training data. The model is deemed valid if such performance is adequate. During the training process, there will be more than one point, after which the error rate typically increases because the generalization stops improving, and the over-fitting begins. Therefore, when the validation error increased for a specified number of epochs, the training was stopped, and the parameters corresponding to the minimum of this validation error were returned and saved. Network testing is essentially the same as validating it, except that the network is shown some data that has never been seen before during the development process, and no corrections are made (Mahdi et. al, 2023).

# 2.5. Prediction Completion Project Based on ANN 

Based on the results of a review of project data and literature reviews, which professional engineers on the project have confirmed, the following parameters were obtained: (i) Equipment, (ii) Materials, (iii) Construction method, (iv) Labor; and (v) Environment. Meanwhile, parameters that have a negligible influence and are ignored are (i) Cost estimate, (ii) Financial project, (iii) Scheduling, (iv) Project documents, and (v) Community.

## 3. Results

The EVM method is the only method that is still believed to be able to measure project performance. Still, this method only uses current performance indices to predict future conditions without considering historical data and changes in project behavior, so other methods are needed to cover this method. BN and ANN methods can better predict future conditions through historical data analysis. Then, the selected method will be developed by looking at the factors that influence project behavior to obtain a model that can predict the most appropriate project performance and provide proactive recommendations/strategies for stakeholders to decide what is best for the project. This model can help make accurate, practical, and agile decisions in project scheduling. Accuracy is needed because the project has a lot of uncertainty in both the internal and external environment, effectiveness because the project has many activities involving a lot of resources, and agility is also really needed because the project must adapt quickly to dynamic changes in the project.

The EVM method is the only method that is still believed to be able to measure project performance. Still, this method only uses current performance indices to predict future conditions without considering historical data and changes in project behavior, so other methods are needed to cover this method. BN and ANN methods can better predict future conditions through historical data analysis. Then, the selected method will be developed by looking at the factors that influence project behavior to obtain a model that can predict the most appropriate project performance and provide proactive recommendations/strategies for stakeholders to decide what is best for the project. This model can help make accurate, practical, and agile decisions in project scheduling. Accuracy is needed because the project has a lot of uncertainty in both the internal and external environment, effectiveness because the project has many activities involving a lot of resources, and agility is also really needed because the project must adapt quickly to dynamic changes in the project.

### 3.1 Determining the SPI value

The SPI value calculation analysis results for the three models have different values. The SPI EVM value is calculated based on measuring real progress achievements, which are then predicted using EAC. The BN SPI value is obtained from the results of CPT (Conditional Probability Table) analysis as an estimator for estimating the SPI for the following year. ANN uses the structure of feed-forward prediction analysis. A comparison of the SPI value results can be seen in (Figure 5). The results show that the SPI value for the EVM method is close to the same as the ANN method, while the BN method has SPI values that tend to be lower than the other methods. This is caused by differences in determining prediction numbers from the three methods, where the EVM and ANN methods can use values according to the analysis results. In contrast, the BN method uses a category approach, which is then translated into numerical values.

![img-4.jpeg](img-4.jpeg)

Figure 5. Comparison of SPI values using EVM, BN, and ANN methods

# 3.2 Progress Performance Evaluation 

The next step after obtaining the SPI value is to calculate the weekly and cumulative weight of the completion of road project work. The cumulative weight calculation analysis results can be seen in (Table 1), and a comparison graph of achievements between various methods can be seen in (Figure 6). The progress performance evaluation will compare initial planning and actual achievements in the field with predicted performance achievements based on the EVM, BN, and ANN methods.
![img-5.jpeg](img-5.jpeg)

Figure 6. Progress Performance Evaluation
(Figure 6) shows that the actual achievements of project performance have progressed compared to the initial plan up to week 98. It can be seen from the realization graph above the plan graph. However, there was a delay after the 99th week until the end of the specified time. It impacts predictions using the EVM method, where the SPI value is always greater than 1, causing predictions of project completion to be ahead of plan. Although the value is slightly lower, the estimated project performance achievements produced using the ANN method follow the pattern of the accomplishments in realization. Meanwhile, the BN method estimates the project performance achievements below the real project achievements because this BN method estimates the achievement value using category values (good, medium, and fail), which are returned to this value and translated into the project performance achievement value.

Table 1. Results of cumulative weight analysis of project completion


In (Table 1), the highest accuracy value in predicting project performance achievements is the ANN method and the EVM and BN methods, respectively. The ANN method was able to predict with an accuracy of $92.72 \%$, while the EVM and $B N$ methods were respectively $86.16 \%$ and $70.41 \%$. Therefore, this research details predictions of the performance achievements of this project using the ANN method linked to previously determined parameters, namely Equipment, Material, Construction Method, Labor, and Environment.

# 3.3 Hybrid EVM-ANN based on project data behavior dynamically 

As a method for measuring project performance, the EVM method has weaknesses in predicting future project performance and achievements. Meanwhile, ANN can estimate future events as it has been proven that SPI data can be modeled to predict future conditions with an accuracy rate of $92.72 \%$. However, according to the results confirmed by the senior project engineer, this model still needs to include parameter behavior that can influence the project. So, this model must be continued by dynamic changes in project conditions.

In this research, of the ten factors proposed based on historical and reference data, only five profoundly influence project changes. The operation of heavy equipment strongly influences changes in the conditions of this project, changes in the material supply chain, the accuracy of implementation methods, labor conditions, and changes in environmental conditions. Therefore, this model will include these factors as model parameters. These project parameters will be assessed based on a list of project events during the project. The assessment method for each parameter can be seen in (Table 2).

Table 2. Assessment of project parameters based on project event attributes


After obtaining the assessment results for each parameter, the assessment data will be analyzed using the ANN method and used as a project performance assessment factor. The results of the project performance assessment can be seen in (Figure 7). This figure shows that the predicted performance due to the combination of parameters has a value that is almost the same as the project's actual performance. Meanwhile, the most distant estimate is obtained when this modeling involves the results of laboratory assessments. If you look at the project data above, you can see that with a very long project model and open conditions, it is inevitable that this project uses more heavy equipment than labor. So, the results of this estimate are based on the facts and data in the field.

![img-6.jpeg](img-6.jpeg)

Figure 7. Progress Performance Evaluation based on the EVM-ANN approach

Based on the analysis of the EVM-ANN model, the results showed that these five parameters could increase the model's prediction accuracy to $94.46 \%$ from the previous $92.72 \%$. Meanwhile, the most significant contributor to this factor is heavy equipment ( $94.24 \%$ ), followed by materials, construction methods, environment, and labor, with accuracy values respectively $93.14 \%, 90.78 \%, 90.16 \%$, and $88.42 \%$.

# 5. Conclusion 

Measuring project performance so far still relies heavily on the EVM model because EVM can calculate time and cost performance simultaneously. However, traditional EVM models cannot anticipate changes that often occur in an everchanging project scope. Another challenge lies in interpreting EVM metrics such as Schedule Variance (SV) and Cost Variance (CV), which are calculated based on initial and static plans; this is very different from the project status, which constantly changes over time. Therefore, this paper must correct EVM weaknesses through innovative approaches by utilizing various new models with better accuracy. The hybrid EVM-ANN method measures much better when predicting future project performance. This is proven by the research results, which increased EVM accuracy from $86.16 \%$ to $92.72 \%$.

Facing dynamic changes in road projects, including weather, site conditions, equipment conditions vulnerable to damage, labor with varying knowledge/attitudes, and many other factors cause the risk of performance achievement being threatened. The project requires a team that can manage the project accurately, effectively, and agile. Therefore, with the limitations of the existing project team, it must be supported by sound project management systems and methods and be able to provide warnings when problems arise in the initial phase, one of which is project delays. Apart from that, it can predict future project conditions if one of the project parameters fails in its provision so that the project team can anticipate by developing new strategies to deal with these problems.

However, this article still has a weakness: the longer the prediction period, the more significant the gap between the estimated results and the actual data. Therefore, this study must be divided into several periods from the total project implementation time to produce accurate SPI predictions.

The feasibility and reliability of project scheduling have become very important in new project management because of the demands for practical implementation in the planning phase to project implementation. Project management must overcome fragility due to the pressure of projects designed for stability, which can be defined as highly complex in pursuit of effectiveness and interdependency (Lotfi et. Al, 2023). Resilience in project management is also really needed because project management must be able to handle pressure without resulting in project management failure. Sustainability planning produced by the project team must provide benefits throughout the project cycle. Stakeholders and end users are responsible for designing, developing, and testing products or services.

## 6. Acknowledgements

I would like to express my sincere appreciation to Universitas Jember for their financial support of this research project. Their funding played a crucial role in the successful execution of this study and the attainment of our research goals.

# 7. Referencias 

Abishek, S.; Prabakaran, P.; bharath, A. A.; vaardhini, S. (2023). Optimizing Resource Allocation and Scheduling in Construction Projects Using Ai \& Optimization Algorithms. Interantional Journal of Scientific Research in Engineering and Management, 07(12), 1-10. https://doi.org/10.55041/ijsrem27863
Abuhasel, K. (2023). Sustainable Green City Development Project Analysis using the Critical Path Method (CPM) and the Crashing Project Method on Time and Cost Optimization. Engineering, Technology and Applied Science Research, 13(3), 10973-10977. https://doi.org/10.48084/etasr. 5980
Agustin, C. E.; Soetjipto, J. W.; Hasanudin, A. (2023). Probability of Accuracy in Cost and Time Using the Monte Carlo Method in the Earned Value Concept for Road Projects. Journal of Applied Civil Engineering and Infrastructure Technology, 4(1), 42-47. https://doi.org/10.52158/jaceit.v4i1.151
Alaloul, W. S.; Liew, M. S.; Zawawi, N. A. W.; Mohammed, B. S.; Adamu, M. (2018). An Artificial neural networks (ANN) model for evaluating construction project performance based on coordination factors. Cogent Engineering, 5, 1-18. 10.1080/23311916.(2018), 5: 1507657
Arifin, M. F. A.; Sarifatuzzuhriyah, M.; Liu, S. S. (2023). Cost and Time Control Analysis with Earned Value Method in the MRT-Hub Building Construction. Jurnal Teknik Sipil Dan Perencanaan, 25(1), 90-99. https://doi.org/10.15294/jtsp.v25i1.43043
Barrientos-Orellana, A.; Ballesteros-Pérez, P.; Mora-Melià, D.; Cerezo-Narváez, A.; Gutiérrez-Bahamondes, J. H. (2023). Comparison of the Stability and Accuracy of Deterministic Project Cost Prediction Methods in Earned Value Management. Buildings, 13(5). https://doi.org/10.3390/buildings13051206
Cândido, L. F.; Heineck, L. F. M.; De Paula Barros Neto, J. (2014). Critical analysis on earned value management (EVM) technique in building construction. 22nd Annual Conference of the International Group for Lean Construction: Understanding and Improving Project Based Production, IGLC 2014, June 2014, 159-170. https://www.researchgate.net/publication/274067989_Critical_analysis_on_earned_value_management_EVM_technique_in_building_construction?enrichId=rgreq-38f19d8cb1dab1b864bf21250a594144-
XXX\&enrichSource=Y292ZXJQYWdlOzI3NDA2Nzk4OTtBUzoyMTExOTMsNjA1NzI5MjhAMTQyNzM2Mzc4MT c1OA\%3D\%3D\&el=1_x_2\&_esc=publicationCoverPdf
Chawla, V.K.; Chanda, A.K.; Anggra, Chawla, G.R. (2018). The sustainable project management: A review and future possibilities. Journal of Project Management. 3, 157-170. doi: 10.5267/j.jpm.2018.2.001
Chang, D. T. (2021). Hybrid Bayesian Neural Networks with Functional Probabilistic Layers [Cornell University]. http://arxiv.org/abs/2107.07014
Chauhan, M.; Kumar, R. (2023). Integrating the multi-objective particle swarm optimization-based time-cost trade-off model with earned value management. Asian Journal of Civil Engineering, 24(8), 3293-3303. https://doi.org/10.1007/s42107-023-00710-5
Darwish, D. (2024). Improving Techniques for Convolutional NeuralNetworks Performance. European Journal of Electrical Engineering and Computer Science. Vol 8 (1). https://www.researchgate.net/deref/http\%3A\%2F\%2Fdx.doi.org\%2F10.24018\%2Fejece.2024.8.1.596?_tp=eyJjb 250ZXb0Ijp7ImZpcnN0UGFnZSI6InB1YmspY2F0aW9uIiwicGFnZSI6InB1YmspY2F0aW9uIiwicG9zaXRpb24iOi JwYWdlQ29udGVudCJ9fQ
Devanshu, V.; Rajgor, M. (2018). A Critical Literature Review on Implementation of Earn Value Management. International Journal of Constructive Research in Civil Engineering, 4(1). https://doi.org/10.20431/24548693.0401004

Efe, P.; Demirors, O. (2019). A change management model and its application in software development projects. Computer Standards and Interfaces, 66(April), 103353. https://doi.org/10.1016/j.csi.2019.04.012
Fang, Fu; Q.i Liu; Guodong, Yu. (2024). Robustifying the resource-constrained project scheduling against uncertain durations. Expert Systems with Applications, Volume 238, Part D. https://doi.org/10.1016/j.eswa.2023.122002.
Garcés, G.; Pena, C. (2023). A Review on Lean Construction for Construction Project Management. Revista Ingeniería de Construcción Vol 38 (1).doi: 10.7764/RIC.00051.21
Gasparotti, C.; Raileanu, A. B.; Rusu, E.; Raileanu, A. (2017). The Earned Value Management-A Measurement Technique of the Performance of the Costs and Labor in the Project Mathematical and Quantitative Methods The Earned Value Management-A Measurement Technique of the Performance of the Costs and Labor in the Project. Acta Universitatis Danubius, 13(May). https://www.researchgate.net/publication/316654971
Gates, R. (2008). Increasing Probability of Success for Complex System of System by Integrating System Engineering, Agile Project Management with Program Performance Management. https://www.defense.gov/About/Biographies/Biography/Article/602797/

Huynh, Q.-T.; Nguyen, T.-H.; Nguyen, N.-H.; Cao, P.-N. (2020). A Method for Project Completion Cost Prediction Using LSTM in Earned Value Management Technique. IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology, 2020(1), 1-5. https://doi.org/10.1109/SigTelCom49868.2020.9199064
Kamandang, Z. R.; Putra, I. N. D. P.; Nauli, A. R. (2023). A Guideline of Earned Value Method (EVM) Implementation as Decision Baseline on Acceleration Solutions for Construction Project Scheduling. Romanian Journal of Applied Science and Technology, 16(3), 447-453. www.techniumscience.com\%0AA
Lessan, J.; Fu, L.; Wen, C. (2019). A hybrid Bayesian network model for predicting delays in train operations. Computers and Industrial Engineering, 127(March), 1214-1222. https://doi.org/10.1016/j.cie.2018.03.017
Lotfi, R.; Weber, G.; Ozeceylan, E. (2023). Recent Advances on Viability and Antifragility in Project Scheduling Call for papers. Advances in Civil Engineering, 2023(May 2023). https://www.hindawi.com/journals/ace/si/297210/
Mahdi, QAMN; Atta, M.N.; Khan, A.; Lashari, SA.; Ramli, DA. (2023). Training Learning Weights of Elman Neural Network Using Salp Swarm Optimization Algorithm. Procedia Computer Science 225 (2023) 1974-1986. doi: 10.1016/j.procs.2023.10.188

Maya, R.; Hassan, B.; Hassan, A. (2023). Develop an artificial neural network (ANN) model to predict construction projects performance in Syria. Journal of King Saud University - Engineering Sciences, 35(6), 366-371. https://doi.org/10.1016/j.jksues.2021.05.002
Mehrdad, P.; Delgoshaei, A.; Ali, A. (2021). A multi-objective scheduling algorithm for multi-mode resource constrained projects in the presence of uncertain resource availability. Brazilian Journal of Operations and Production Management, 18(1), 1-26. https://doi.org/10.14488/BJOPM.2021.007
Moslemi Naeni, L.; Shadrokh, S.; Salehipour, A. (2014). Erratum to A fuzzy approach for the earned value management [International Journal of Project Management, 32, (2014), 709-716]. International Journal of Project Management, 32(4), 709-716. https://doi.org/10.1016/j.ijproman.2013.02.002
Nachbagauer, A. (2022). Resilient Project Management, Journal Modern Project Management. 10(1), doi: 1019255/JMPM02901
Netto, J. T.; de Oliveira, N. L. F.; Freitas, A. P. A.; Dos Santos, J. A. N. (2020). Critical Factors and Benefits in the Use of Earned Value Management in Construction. Brazilian Journal of Operations and Production Management, 17(1), 1-10. https://doi.org/10.14488/BJOPM. 2020.007
Newton, M. (2018). A Systematic Literature Review of Project Management Tools And Their Impact On Project Management Effectiveness [Purdue University]. In Business Ethics Quarterly (Vol. 3, Issue 12). https://docs.lib.purdue.edu/open_access_theses?utm_source=docs.lib.purdue.edu\%2Fopen_access_theses\%2F14 30\&utm_medium=PDF\&utm_campaign=PDFCoverPages
Novinsky, M.; Nesensohn, C.; Ihwas N.; Haghsheno, S. (2018). "Combined Application of Earned Value Management and Last Planner System in Construction Projects." In: Proc. 26th Annual Conference of the International. Group for Lean Construction (IGLC), Chennai, India, pp. 775-785.doi: doi.org/10.24928/2018/0491. Available at: www.iglc.net.
Project Management Institute. (2021). PMBOK Guide 7th edition. In Project Management Institute, Inc. 14 Campus Boulevard Newtown Square, Pennsylvania USA. www.PMI.org.
Rajgor, M. B.; Varia, D. S.; Pitroda, J. R. (2018). To Study and Implement Earn Value Management on Industrial Project Using Microsoft. Ijirt, 4(12), 424-430. https://www.researchgate.net/publication/354322958
Shen, H.; Luo, L.; Niu, X.; Fu, C.; Han, Y. (2024). Dynamic Bayesian Network-Enabled Approach for Organizational Leadership Measurement of Complex Construction Projects. MDPI, 14(4). https://doi.org/10.3390/buildings14041123
Soetjipto, J.W.; Adi, T.J.W.; Anwar, N. (2018). Dynamic bayesian updating approach for predicting bridge condition based on Indonesia Bridge Management System (I-BMS). International Conference in Rehabilitation and Maitenance on Civel Eengineering 2018. Proceeding MATEC Web of Conferences 195, 02019 (2018). doi: https://doi.org/10.1051/matecconf/201819502019
Tomov, Latchezar. (2022). Antifragile Project Management: The Deming paradigm and beyond. Procedia Computer Science. 201. 632-638. 10.1016/j.procs.2022.03.083.
Wicaksono, K. H.; Soetjipto, J. W.; Halik, G. (2023). Prediction of Project Schedule Performance Index for Trans South Java Road Project using Bayesian Network. UkaRsT, 7(1), 46-59 https://doi.org/10.30737/ukarst.vi1.3552.
Zhang, L.; Wu, X.; Skibniewski, M. J.; Zhong, J.; Lu, Y. (2014). Bayesian-network-based safety risk analysis in construction projects. Reliability Engineering \& System Safety, 131, 29-39. https://doi.org/10.1016/j.ress.2014.06.006