# How activity type, time on the job and noise level on the job affect the hearing of the working population. Using Bayesian networks to predict the development of hypoacusia. 

Jesús P. Barrero, Susana García-Herrero \& Miguel A. Mariscal<br>University of Burgos, Escuela Politécnica Superior, Avda. Cantabria s/n, 09006 Burgos, Spain<br>J.M. Gutierrez<br>Instituto de Física de Cantabria, CSIC-University of Cantabria, 39005 Santander, Spain


#### Abstract

In this research we identify the main factors believed to trigger occupational hypoacusia in an effort to increase our knowledge of how this occupational disease occurs and develops. With this goal in mind, we have gathered various demographic/personal, occupational and non-occupational data from a heterogeneous sample of 1,418 workers. The data selected include the noise levels to which the individuals in the sample are exposed. This entailed taking measurements at their respective jobs, as well as doing an objective assessment of their hearing ability, which required administering medical hearing tests. Lastly, the workers completed a survey on various habits and other factors deemed to be influential, and on the respondents' own perception of their hearing.

Bayesian networks were used to obtain the conditioned probability of developing hypoacusia based on the data collected from the sample. Specifically, for this study we used the general network created by the relationships between all of the factors associated with developing hypoacusia in order to analyze the influence individually and by grouping three specific variables: activity sector, noise level and time on the job. This work yielded a considerable database that can be used to conduct a multitude of analyses intended to study and predict the hearing acuity of the working population under different scenarios. Specifically, in the case at hand, the Bayesian network obtained indicates that the three factors analyzed influence the hearing of the individuals, though to different extents. The least influential factor involves the sector of activity, followed by the noise level on the job, which varies noticeably in favor of better hearing for workers in jobs whose noise levels are rated as low. Finally, we deemed time on the job (which is also related to age), as the most influential factor as it exhibits the largest differences among its potential states, with workers whose time on the job is rated as low or medium exhibiting the best likelihood of having good hearing.


## 1 INTRODUCTION

Some 360 million people around the world are affected by hypoacusia to varying extents, with the effects ranging from physical to social and psychological (Díaz, Goycoolea, \& Cardemil, 2016). Deafness can cause problems involving spoken communication, cognitive deterioration and mental health (Lin et al., 2013; Mohr et al., 2000; Pascolini \& Smith, 2009; Van Vliet, 2005). It can even entail a higher risk of mortality (Hallam, Ashton, Sherbourne, \& Gailey, 2006; Yueh, Shapiro, MacLean, \& Shekelle, 2003). When we speak of the factors that determine the risk of developing hypoacusia as an occupational disease, the most typical trigger for this disease is noise (Fernando Pablo J.A, 1996), although other majors factors include the sound pressure level, the type of noise, the noise exposure time and age, as well as the characteristics of the worker, the working environment, the distance and position relative to the sound source, gender, diseases, osteoclerosis and deafness due to cranial trauma, among others (Fernando Pablo J.A, 1996). This study focuses on noise, the duration of the noise exposure and the nature of the activities carried out by the individuals as factors in the development of hypoacusia.

In terms of noise, some 80 million Europeans are routinely exposed to noise levels in excess of the tolerance limit ( 65 dB ) specified by the World Health Organization (WHO) (Sanz López, 2013). Direct and indirect exposure to this physical phenomenon accounts for $11 \%$ of workplace accidents. As concerns work-related diseases, it is calculated that hypoacusia caused by noise ranks third among occupational diseases (Bartosińska \& Ejsmont, 2002). It shares this place with pathologies involving years lived with disability (YLD), behind depression and unintentional injuries (Díaz, Goycoolea, \& Cardemil, 2016)

The development of legislation and technical reference documentation on noise intensified in the second half of the $20^{\text {th }}$ century, following the end of the Second World War. In the 1950s, and with the publication of the book The Effects of Noise on Man in 1970, Karl D. Kryter (Kryter, 2013) related noise exposure time and noise intensity to the probability that workers exposed to different noise levels would suffer hearing damage. In 1975, the International

Organization for Standardization drafted the ISO 1999 standard, on determining the hearing risk from noise exposure. This was also done by means of conventions of the International Labour Organization, such as convention number 155 of 1981 (OIT 155, 1981), on occupational safety and health and the working environment, ratified by Spain in 1985. This regulation laid the foundations for Spain's national law, and in 1989 led to Royal Decree 1316/1989 (RD 1316, 1989), which was updated fifteen years later to create the current law in Royal Decree 286/2006 (RD 286, 2006), on protecting the health and safety of workers against risks related to noise exposure.

In 2006, Royal Decree 1299/2006 (RD 1299, 2006) was published in Spain, which approved the new listing of occupational diseases in the Social Security system, and laid down criteria for reporting and recording them. This regulation includes noiserelated hypoacusia or deafness in group 2 of the occupational diseases, cataloguing it as neurosensory, bilateral and irreversible occupational deafness for frequencies 3 to 6 KHz related to jobs that expose workers to constant noises whose equivalent daily sound level is equal to or higher than 80 decibels. The latest publications from the Observatory for Occupational Diseases and Diseases Caused or Aggravated by Work (Observatorio de Enfermedades Profesionales, 2017), created by the Spanish government, show that in Spain, of all the occupational diseases recognized in 2016, 3.08\% involved hypoacusia, and of all the diseases deemed to have been caused by work, $0.51 \%$ were associated with the ear.

In order to model and analyze the influence of the potential factors affecting hearing loss, we consider a representative sample of 1,418 workers and use da-ta-driven Bayesian networks for probabilistic modeling and inference (Castillo, Gutierrez, \& Hadi, 2012). Bayesian networks are increasingly popular machine learning tools that are widely applied in health studies - e.g. in healthcare (Friedman, Linial, Nachman, \& Pe'er, 2000; Lucas, Van der Gaag, \& Abu-Hanna, 2004; Mani, Valtorta, \& McDermott, 2005) or disease transmission (Lau et al., 2017) particularly in problems involving discrete variables. Bayesian networks provide a sound methodology to define parsimonious joint probabilistic models for the variables of interest (hearing loss and influential factors in this study) by considering only the relevant marginal and conditional dependence relationships among the variables (García-Herrero et al., 2017; Pittavino et al., 2017), as learned from the available data using efficient learning algorithms (Acciardi, 2008). This provides users with efficient modeling and analysis tools for probabilistic data analysis (Koller \& Friedman, 2009) as an alternative to more complex techniques, such as neural networks or the analysis of hierarchical multilevel tra-
jectories (Peter, March, \& du Prel, 2016; Shipley, 2009).

This research focuses on the working population and utilizes Bayesian networks to analyze the probability of developing hypoacusia based on multiple variables, which in our case are grouped as demographic and personal factors (meaning those that characterize a specific population), occupational factors (those related to the working conditions in different companies) and non-occupational factors (those that are manifested outside the work environment). This study considers the hypothesis that the combination of these factors affects the hearing health of people, which is why the sensitivity analyses generated with the Bayesian network proposed consider all of the model's variables, such that every factor is involved in each analysis.

Finally, it should be noted that this study was designed for the purpose of answering the basic questions of how and why some workers develop hypoacusia. How do the main occupational factors influence this? In what proportion? To answer this, one of the main lines of this research focuses on studying the noise level and time on the job variables in the primary sectors of activity.

## 2 FRAMEWORK. RELATIONSHIP BETWEEN HYPOACUSIA AND OCCUPATIONAL FACTORS.

We define occupational factors as those related to the working conditions that could in some way have an effect on the development of hypoacusia.

There are many papers and studies that relate the noise that is produced in the workplace to the hypoacusia suffered by part of the population. Occupational noise, therefore, is a contaminant of great interest that can negatively influence the health of workers who are exposed to it at their work center (Hernández Díaz \& González Méndez, 2007). As concerns the characteristics of the noise to which a worker is exposed, the consequences that the noise exposure has on hearing function vary depending on several factors, including the type of noise, its intensity, and the individual's chronicity and susceptibility (Nowak \& Bilski, 2003). Fernando Pablo (Fernando Pablo J.A, 1996) regards the noise type as a basic factor in terms of the frequency spectrum it exhibits, as well as of its stable, intermittent, fluctuating or impacting nature. This author concludes that it is generally accepted that constant noise is more tolerable than intermittent noise. As concerns the frequency of the noise, it is generally considered that noise that is mostly distributed at frequencies above 500 Hz is more harmful than noise with predominantly low frequencies. As for hearing thresholds, it is important to note that a typical drop was identified

in the hearing tests at $4,000 \mathrm{~Hz}$, which has long been considered to be indicative of noise-induced hypoacusia (Rytzner \& Rytzner, 1981). Narrow-band noises are also considered more dangerous than broadband noises. Impact noises, when very loud, can cause immediate injury due to acoustic trauma (Fernando Pablo J.A, 1996). According to (Sanz López, 2013), as concerns the intensity, time and intermittency, hearing loss induced by an average noise in a group of workers increases with noise intensity and exposure time almost linearly. In a workplace with a constant noise intensity, the rise in noise-induced hearing loss over time approaches an exponential function. Likewise, according to Fernando Pablo (Fernando Pablo J.A, 1996), the importance of the level to the development of hypoacusia is essential: "Even if no exact relationship can be established between the sound pressure level and hearing damage, it is obvious that the higher the sound pressure, the greater the hearing damage (loss of hearing), but the relationship between the two is not linear". Given current regulations and the studies presented to date, the limit for preventing hypoacusia if exposed to a constant noise over 40 hours a week is considered to be 80 dB .

Another vitally important factor is noise exposure time, which is typically considered from two aspects, according to authors like Fernando Pablo (Fernando Pablo J.A, 1996). One is the hours/day or hours/week of exposure, and the other is the time on the job, or the number of years that the worker has been in a job with a given noise level. If the exposure is interrupted, the damage is reduced as the ear can recover from listening fatigue. Apparently the ear can withstand more energy if the exposure is intermittent instead of constant when faced with a single impulse of short, intense noise (Ward, 1995). According to Borg (Borg, 2001), most noise-induced hearing loss occurs in the first five years of exposure. Thus, the damage rises quickly at first, but then slows gradually. López González (López González, 1981), who conducted a study with 88 workers at the "Desembarco del Granma" textile plant who had been on the job more than eight months, concluded that the noise pollution present had a negative effect on the health of the personnel exposed, despite the short exposure time, leading to hearing problems. There is also research, like that by Talbott-E.O. (Talbott et al., 1990), who did a study of 245 individuals ranging in age from 56 to 68 who retired after 30 years of work, and found, by way of hearing tests, severe hearing damage in $67 \%$ of the oldest workers (from 64 to 68 years of age). Other studies also agree and predict that occupational hypoacusia will more often be present in old individuals than in young ones (Delgado, 1991; Mcshane, Hyde, Finkelstein, \& Alberti, 1991). There are likewise studies that propose that the harmful effect of noise is proportional to the duration of the exposure
(Clemente Ibáñez, 1991), with many authors agreeing with this conclusion, including Sataloff (Sataloff, 1953), Howell (Howell, 1978), Burns and Robinson (Burns \& Robinson, 1970) and Dobie (Dobie, 1995). We can state that there is a direct relationship between the length of the noise exposure and the presence of hearing loss, especially at 4,000 Hz and nearby frequencies (Burns \& Robinson, 1970; Dobie, 1995; Howell, 1978; Sataloff, 1953). As for the form in which deafness or hypoacusia occurs, there is evidence that over the long term, noiseinduced hearing damage is caused by the gradual accumulation of microtraumas due to noise that, little by little, result in the degradation of hearing ability (Gravendeel \& Plomp, 1960).

There is also a proven direct relationship between the combination of loud noise and many years of exposure, and the incidence of occupational hypoacusia (Calviño del Río, Abreu García, \& Cárdenas Sotolongo, 1982). Delgado (Delgado, 1991), in a study of 120 shipyard workers under the age of 50 , found a high percentage of hearing loss involving the loudest work stations in the shop, and demonstrated a relationship with the years of exposure to industrial noise. Ruiz (Ruiz, 1997) conducted a study on 207 workers at the Tenerife North - Los Rodeos airport in Spain, differentiating between those who were exposed to noise and those who were not. The relationship between the presence of hypoacusia and the greatest exposure to loud noises was $16: 29(55.17 \%)$ for those who were exposed to noise, and $27: 178(15.17 \%)$ for those who were not. There is, therefore, a notable difference in terms of the incidence of hypoacusia in exposed individuals versus those who are not. Along these same lines, Flottorp (Flottorp, 1973) did a study with 70 disc jockeys and found that one-third exhibited significant hearing loss for high-frequency sounds, while in the control group, without the same noise exposure, only $1 \%$ had similar problems.

In terms of the type of activity, workers in the industrial sector and in certain activities involving construction or maintenance seem to be exposed to the highest noise levels. There are several studies, like the one by Hernández (Hernández Díaz \& González Méndez, 2007), that have found that noise is a significant contaminant in the aluminum work industry. In their study, Tosal Suárez and Santa María (Tosal \& Santa María, 1992) took sound pressure readings at 1277 points in a Spanish saw mill and wood processing plant, finding that the predominant level was in excess of $90 \mathrm{~dB}(\mathrm{~A})$ and affected $49.27 \%$ of the workers. Espinosa and Sánchez (Espinosa \& Sánchez, 1991) did a study with 150 random patients who had worked in industry in Puertollano, Spain, and found a noise level in excess of $100 \mathrm{~dB}(\mathrm{~A})$ during the workday, which had negative effects on the health of those exposed. In another study of 746 patients who worked in shipyards

owned by Nervión S.A. (Spain), it was found that $65.9 \%$ of them exhibited hypoacusia to some extent, but it was only determined to be an occupational disease in $1.33 \%$ of them (Monasterio \& Serrano, 1991).

The model used in our research places particular importance on the three factors described earlier: the type of industry or activity of the company where the individuals work, the noise level present in the workplace and the number of years on the job. These factors were characterized by using the set of variables described in the section below, and that includes, for example, the number of daily hours of noise exposure, the use of hearing protection or time exposure limits, exposure to noise in previous jobs, exposure to ototoxic agents, and others.

## 3 DATA AND METHODOLOGY

### 3.1 Data collection

In concert with the occupational risk prevention service Ingemédica S.L., various medical and occupational environment data were collected over a period of approximately two years from a sample of 1,418 workers of various sectors of activity, ages and nationalities who were working in companies in the provinces of Burgos and Valladolid, Spain.

The research involved two main activities. The first required obtaining the data on the noise levels in the workplace, which entailed having qualified industrial health specialists take noise measurements using sound meters and noise dosimeters and employing proper measurement techniques. The second consisted of doing audiometric medical testing (to provide objective data on the hearing ability of the individuals) and completing surveys (to collect data on various aspects, such as habits and the subjective perception that the respondents had of their own hearing ability). These surveys, published by the Health and Social Welfare Council of the Board of Castilla y León and authorized by Spain's Ministry of Health and Consumer Affairs (Uña, García, \& Betegón, 2000), are based on occupational health monitoring protocols. In keeping with the health monitoring protocols and applicable Spanish laws on Occupational Risk Prevention (Ley31/1995, 1995; RD 286, 2006), the hearing tests were administered by specialized personnel (occupational physicians and company nurses) using audiometers and soundproof cabins. All of these data were collected with the consent of the individuals and companies involved, and then anonymized.

This yielded a broad sample of individuals and their associated demographic data (age, gender, nationality, blood pressure, etc.), occupational data (type of sector or area of activity of the company where they work, their job description, the noise present in the workplace, the number of daily hours
of noise exposure, the time on the job, the use of hearing protection or noise exposure time limits, occupational exposure to noise at previous jobs, and exposure to ototoxic agents), and lastly, data on nonoccupational factors (exposure to noise outside the workplace, such as due to hunting, listening to loud music, etc., a family history of deafness, auditory diseases, previous otological problems or the use of drugs that affect hearing).

### 3.2 Conceptual Model

The conceptual model for this research is given below (see Figure 1). It aims to explain how the development of hypoacusia is affected by various factors of a demographic/personal, occupational and non-occupational nature for the individuals in the sample. To satisfy this objective, we considered those key variables in our research that can most objectively determine an individual's hearing level following the administration of hearing tests. These variables are Speech Average Loss (SAL), the Early Loss Index (ELI) and the Percent Overall Hearing Loss. We will analyze the effect that the remaining factors have on these variables.

The model consists of the following variables:

- Demographic and personal variables: gender, age, blood pressure, nationality, height and weight.
- Occupational variables: noise level at the individual's current job (measured), number of daily hours of noise exposure, time on the job (number of years at current job), noise exposure in previous jobs, number of years of occupational noise exposure in previous jobs, occupational exposure to ototoxic agents, sector, job description and noise protection system, either through time exposure limits or the use of personal protection.
- Non-occupational variables: noise exposure outside the workplace, a family history of deafness, general diseases that might affect hearing, previous otological problems and use of ototoxic drugs.
- Variables for evaluating hypoacusia:
$\checkmark$ Scientific or objective, resulting from the administration of audiometric tests: SAL/ELI/\% Overall Loss
$\checkmark$ Subjective: perceived hearing ability, quality of communications, volume needed to hear TV, hearing in noisy environments and discomfort caused by loud noises.

Figure 1: Expanded conceptual model of occupational, nonoccupational and demographic factors associated with the development of hypoacusia.
![img-0.jpeg](img-0.jpeg)

Source: Compiled by authors.

### 3.3 Study Variables

This study considers a total of 32 variables (described in the preceding section). The target variable selected is the Binaural Loss Percent Index, the influence on which was analyzed, in particular, by taking into account the area of activity, the worker's time on the job and the noise level at the work station.

## Percent Binaural Loss

The percent loss is a widely used and intuitive method for assessing hearing level based on audiometric tests (Uña et al., 2000), one that provides a "social" assessment of hearing loss. This index is of great legal significance in Spain when qualifying disability due to deafness or hypoacusia. Also used in this assessment is the opinion of a medical board, which evaluates the potential chronic diseases present in the patient. The disability percentage is then determined, as per Royal Decree 1971/999 (RD 1971, 1999), based on the level of hearing loss exhibited by an individual.

When assessing hearing loss, the preliminary thresholds are evaluated for $500,1000,2000$ and 3000 Hz tones. To calculate the percent loss in one ear, the individual percents for each tone are added. To calculate the percent overall hearing loss in both ears, the loss in the better ear (expressed as percent hearing loss) is multiplied by five, and the loss in the worse ear is multiplied by one. The losses are added and divided by six, as shown in Figure 2.

Figure 2: Formulas for calculating Percent Overall Loss.

$$
\begin{gathered}
\% \text { monaural loss }=\left(\frac{\sum \text { Loss } d B(A) \text { for } 500,1,000,2,000 \text { y } 3,000 \mathrm{~Hz}}{4} \sim 25\right) \times 1,5 \\
\% \text { binaural loss }=\left(\frac{5 \times \% \text { loss in the better ear }+\% \text { loss in the worse ear }}{6}\right)
\end{gathered}
$$

Source: Uña Gorospe M.A.
The average binaural loss is $1 \%$, with a minimum value of $0 \%$ and a maximum of $67 \%$.

This variable was discretized into the following interval ranges for the Percent Binaural Hearing Loss (see Table 1).

Table 1: Sample distribution by Percent Binaural Loss.


Source: Compiled by authors.

## Sector

The sample was divided into the groups shown in Table 2, which represent the traditional sectors of the economy: 1. Construction (includes construction, assembly and maintenance activities) / 2. Agriculture and Livestock / 3. Industry (Includes general industrial activities, particularly in the food, mining, lumber, machinery and chemical industries) / 4. Services.

Table 2: Sample distribution by sector.


Source: Compiled by authors.

Note that the construction sector accounts for practically half of the sample, with a much lower representation for the agriculture/livestock, at just $0.35 \%$ of the sample. As a result, the latter was excluded from the sensitivity analyses conducted for this study.

## Years on the Job

Figure 3 below shows the sample distribution based on the years on the job variable, which accounts for the number of years that an individual in the sample has been at the same job. This is an independent, quantitative and continuous variable. The sample average is 10.2 years, with a minimum value of 0 years and maximum of 49 years.

Figure 3: Distribution of the Years on the Job variable.
![img-1.jpeg](img-1.jpeg)

Source: Compiled by authors.

The Years on the Job variable was discretized into the groups shown in Table 3:

Table 3: Sample distribution by Years on the Job.


Source: Compiled by authors.

## Noise Level

In order to analyze the results of the noise measurement levels, these were divided into four groups, in keeping with Royal Decree 286/2006 of 10 March, on protecting the health and safety of workers against risks associated with noise exposure (RD 286, 2006), and which takes into account the measurement indicators LAeq.d (Daily equivalent noise level in dB ) and Lpeak (Peak noise level in dB ). In order to simplify the understanding of our results, we ranked these levels from low to very high, as shown in Table 4.

Table 4: Sample distribution by noise levels.


Source: Compiled by authors.

Note that almost half of the individuals in the sample ( $46.54 \%$ ) work in jobs with a moderate amount of noise. Approximately $30 \%$ work in environments that, based on the current regulation, present a low health risk, while over $22 \%$ of the population is exposed to levels that are considered hazardous, with $15.09 \%$ in the least favorable group from the standpoint of hearing health (very high level).

### 3.4 Bayesian Networks

One of the main problems for building probabilistic models (e.g. the joint probability distribution, JPD) in applications with a large number of discrete variables is the huge number of parameters involved, which grows combinatorially with the number of variables (Castillo et al., 2012). For instance, in this study, which has 32 variables, the number of parameters (probabilities) required to specify the JPD is larger than $10^{9}$. Therefore, the direct specification of the JPD is prone to overfitting and its use may lead to misleading conclusions.

Bayesian networks are probabilistic graphical models that allow constructing simple ad-hoc probabilistic models for a particular problem by building

on the relevant dependencies among the variables, which are derived from empirical data in the form of a directed acyclic graph, DAG. The resulting graph (see, e.g. Figure 4) is a simple and powerful analysis tool that allows exploring the marginal and conditional dependencies for the problem as given by the available data (Koller \& Friedman, 2009). Moreover, the resulting model allows deriving a simple factorization of the JPD by considering a number of local conditional probabilities (one for each variable, conditioned to its parents; i.e. the nodes with direct incoming links), in the following form: $p\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid \pi_{i}\right)$, where $\pi_{i}$ represents the parent of $x_{i}$ in the graph. This factorization requires a small number of parameters.

Efficient inference methods have also been developed to compute any conditional probability $P(x \mid y)$, where $x$ is the target variable and $y$ the influence factors, given the factorized representation of the JPD (Castillo et al., 2012).

### 3.5 Model Validation

So as to evaluate the performance of the trained model and its generalization capability, we propose a 10 -fold cross-validation (Kohavi, 1995), to which end we define a partition of the full sample into ten disjoint data subsets, each containing $\mathrm{N} / 10$ elements, which are used as a test set for the remaining data in order to train the model. This yields a prediction for the full set that is compared with the data in terms of the Receiving Operating Characteristic curve (Fawcett, 2006), which is a standard validation approach for probabilistic and binary classifiers. More specifically, we will use the Area Under the Curve (AUC), which varies from 0.5 (random conjecture) to 1 (perfect performance), and can be interpreted as an overall measure of accuracy (Hanley \& McNeil, 1982). This thus yields an AUC for each group of the target variable that reflects the model's high capacity to predict the corresponding group. In our case, the AUCs obtained were $0.96,0.95,0.98,0.87$ and 0.75 , which indicates a high ability for the five groups into which our target variable is divided (\% Binaural Loss), with the worst results being obtained for the less sampled groups.

## 4 RESULTS

The main results of this study are summarized next. We first describe the Bayesian network obtained and the marginal probabilities, adjusted for the primitive variables considered in this research sector, noise level and time on the job - in order to analyze their influence on the hearing health of the individuals in the sample considered. Then, in the subsections that follow, we describe the results of the sensitivity analyses for the variables mentioned.

### 4.1 Bayesian Network used

The graph that results from the Bayesian network proposed shows the various relationships between the different variables (see Figure 4).

The results of the initial probabilities (see Table 5) indicate that most of the individuals in the sample have good hearing, with no hearing loss (Group 1) or minor hearing loss (Group 2). If we consider the different variables analyzed, we see that the workers that exhibit the highest likelihood of having good hearing are, by sector, those in the service sector, $93.47 \%$ of whom exhibit the best hearing possible, versus $86.47 \%$ of workers in the construction sector. As concerns the time on the job, the probability of having good hearing is highest for those who have been on the job for the least amount of time ( $<3$ years), at $94.47 \%$. This figure decreases gradually with the number of years on the job to $82.73 \%$ for the group with the longest time on the job ( $>16$ years). Lastly, as concerns the noise level on the job, there is a considerable difference between the workers exposed to low noise levels, who have a $94.74 \%$ probability of being in the group with the best hearing possible, and those exposed to moderate, high or very high noise levels, who have lower and very similar probabilities of having the best hearing possible, their percentages being $86.55 \%, 86.57 \%$ and $87.69 \%$, respectively.

Figure 4: Graph of the Bayesian network
![img-2.jpeg](img-2.jpeg)

Source: Compiled by authors.

Table 5: Initial probabilities for the variables vs Percent Binaural Loss.


Source: Compiled by authors.

### 4.2 Sensitivity Analysis. Noise Level and Time on the Job vs. Percent Binaural Loss

This sensitivity analysis considers the combined influence of noise level and time on the job as influential factors in the development of hypoacusia (see Table 6). Note that the probability of a worker having good hearing decreases as the time on the job increases. This probability falls as the number of years on the job increases in practically every case, independently of the noise level associated with the job. Note also that the entire group of workers in jobs with low noise levels, regardless of the time on the
job, have a likelihood of being in the group with the best hearing that is higher than their initial $89.04 \%$ probability. This happens in no other groups (with moderate, high or very high levels), whose workers are only more likely than their initial probabilities to be in the group with the best hearing if their time on the job is below ten years.

We may thus conclude that hearing loss increases with time on the job, an effect that is more pronounced in workers who carry out their jobs in environments where the noise level is not low, as Figure 5 shows.

Table 6: Sensitivity Analysis. Noise Level and Time on the Job vs Percent Binaural Loss.


Source: Compiled by authors.

Figure 5: Comparison graph for excellent hearing based on Noise Level and Time on the Job.
![img-3.jpeg](img-3.jpeg)

Source: Compiled by authors.

### 4.3 Sensitivity Analysis. Noise Level and Time on the Job vs. Percent Binaural Loss

This sensitivity analysis aims to show the combined influence of the sector and time on the job variables on the development of hypoacusia. Note that the probability that workers will have good hearing diminishes as the time on the job increases, with this figure dropping as the number of years on the job rises in every case, regardless of the area of activity (see Table 7). Furthermore, the entire group of workers in the service sector, except for those with the most years on the job ( $>16$ years), have a probability of being in the group with the best hearing that is above the initial probability of $89.04 \%$, something that does not happen for the other sectors (construction and industry), whose workers are only have a higher probability of being in the group with the best
hearing that is higher than the initial probability if the number of years on the job is low, but not if this number is higher than 10 years for industry workers or 6 years for construction workers.

If we analyze all the cases, the group of workers with the highest probability of having good hearing is service sector workers with a low time on the job ( $<3$ years), with a probability of $96.25 \%$. In contrast, the group of workers with the least favorable probabilities in terms of hearing loss is construction workers with the longest time on the job ( $>16$ years), for whom this figure stands at $80.10 \%$.

We may conclude, then, that hearing loss rises with time on the job, with construction sector workers exhibiting the worst hearing, as shown in Figure 6 .

Table 7: Sensitivity Analysis. Sector and Time on the Job vs Percent Binaural Loss. .


Source: Compiled by authors. Figure 6: Comparison graph for excellent hearing based on Sector and Time on the Job.

![img-4.jpeg](img-4.jpeg)

Source: Compiled by authors.

### 4.4 Sensitivity Analysis. Noise Level and Time on the Job vs. Percent Binaural Loss

This sensitivity analysis shows that for noise levels classified as low, the probability that a worker will have good hearing is similar for all three sectors, with this figure being higher than the initial probability of $89.04 \%$ ( $94.57 \%$ for the service sector, $94.84 \%$ for construction and $94.64 \%$ for industry, see Table 8). In the case of workers who are subjected to moderate and loud noises, we see that for

the three sectors, the probability of having the best hearing (Group 1) drops considerably. Ultimately we find that for very high noise levels, only the industrial sector maintains its downward trend, while for the service and construction sectors, this trend is inverted.

We can also see that only in the case of the service sector does the probability of having good hearing when the noise level is very high ( $91.22 \%$ ) exceed the initial probability of $89.04 \%$.

We therefore conclude that hearing loss rises generally as the noise level on the job increases from low to high, regardless of the sector. This trend is maintained in the industrial sector for noise levels classified as very high, but varies in the service and construction sectors, where the probabilities of having good hearing are greater than for high levels, as shown in Figure 7.

Table 8: Sensitivity Analysis. Sector Noise Level vs Percent Binaural Loss.


Source: Compiled by authors.
Figure 7: Comparison graph for excellent hearing based on Sector and Noise Level on the Job.
![img-5.jpeg](img-5.jpeg)

Source: Compiled by authors.

### 4.5 Sensitivity Analysis. Sector, Noise Level on the Job and Time on the Job vs Percent Binaural Loss

This sensitivity analysis considers the combined effect that the three study variables - sector, noise level and time on the job - have on the development of hypoacusia. The results are shown in Table 9.

As concerns the sector variable, although the service sector presents the most extreme results for one of its variants (high noise levels), in general we see that the worst probabilities for overall hearing are in the construction sector, where those workers who are subjected to noise levels classified as low, moderate or very high have a worst hearing probability than that for workers in the service on industry sectors. From this perspective, we find that workers in the service sector have the best overall probability of having good hearing.

As for the noise level on the job variable, we see that in general, individuals who work in jobs where the noise level is classified as low exhibit better hearing than workers in environments with moderate, high or very high noise levels, for whom the difference between the levels are much less pronounced.

If we focus on the time on the job variable, we see that in general, the probability of having good hearing is inversely proportional to the time on the job for every sector, and practically for all noise lev-
els. Specifically, note that the probability of being in the group with the best hearing with a probability higher than the initial $89.04 \%$ is present when the time on the job is low.

In light of the results, we may infer that the factors analyzed influence the development of hypoacusia, such that the probabilities of its development rise with the noise level and with the time on the job for any sector of activity. In general, it is the workers in the service sector who exhibit the best hearing levels, and those in the construction service the worst (see Figure 8).

It may also be concluded that the influence of the factors analyzed differs in intensity. The least influential factor, meaning that with the lowest percentage variations when the conditions for the other two factors remain unchanged, is the sector variable, followed by the noise level on the job variable, which varies considerably in favor of better hearing for noise levels classified as low, in comparison to the other noise levels (moderate, high and very high). Finally, the most influential factor is time on the job, as it displays the greatest differences among its potential states, with workers that report a low or moderate amount of time on the job ( $<10$ years) having the highest probability of exhibiting good hearing.

Table 9: Sensitivity Analysis. Sector, Noise Level and Time on the Job vs Percent Binaural Loss.



Source: Compiled by authors.

Figure 8: Comparison graph for excellent hearing based on Sector, Noise Level on the Job and Time on the Job.
![img-6.jpeg](img-6.jpeg)

Source: Compiled by authors.

## 5 DISCUSSION

One of the outcomes of this research was the compilation of an important database consisting of 1,418 individuals, for whom over 30 characteristics were gathered that can be used to conduct a multitude of analyses intended to study and predict the quality of hearing of the working population under different scenarios. It was with this objective that we created a Bayesian network to consider the main factors affecting the development of hypoacusia. These were classified based on their demographic/personal, occupational and non-occupational origins, with the result being that one of the main contributions of this study was the application of the aforementioned Bayesian network methodology. In our case, this allowed us to analyze a combination of the sector, noise level and time on the job factors to determine the probability that an individual will manifest a given level of hearing acuity.

In an effort to have reliable data for this research, medical audiometric tests were administered to assess the hearing acuity of the individuals in the sample, the results of which were processed using the Percent Binaural Loss index. The $\% \mathrm{BL}$ is a widely used and intuitive method that is of great legal sig-
nificance when assessing disability due to deafness. The sample that made this study possible shows that the average individual has a binaural loss of $1 \%$. Considering the large diversity of the sample, whose respondents work in various jobs in different sectors of the economy, we found that their overall hearing health was good, since $86.11 \%$ of the individuals analyzed did not exhibit any kind of hearing loss, and in only six cases (approximately $0.28 \%$ of the sample size) was the hearing loss in excess of $30 \%$.

As part of the analyses for this research involving the influence on the hearing acuity of the individuals, first we considered the three selected factors separately: sector, noise level and time on the job. We noticed that, by sector, it is service workers who are most likely to have good hearing, with those in the construction sector having the worst hearing. As concerns the time on the job, the likelihood of having good hearing is higher for those who have been on the job the shortest length of time, a likelihood that drops gradually as the time on the job increases. Lastly, for the noise level factor, those individuals who are exposed to low noise on the job exhibit substantially better probabilities of having good hearing than those who are exposed to moderate, high or very high noise levels.

We then analyzed the combined influence of the noise level and time on the job factors, observing

how the likelihood that workers will have good hearing decreases with their time on the job, with this probability dropping consistently as the number of years on the job rises in practically every case, independently of the noise level associated with the job. We also noted that all the workers in jobs with noise levels classified as low have a likelihood of being in the group with the best hearing that is higher than the initial $89.04 \%$ probability.

In terms of the analysis of the joint influence that the sector and time on the job variables have on the development of hypoacusia, we see that hearing loss is directly proportional to time on the job, with those workers in the construction sector having the highest probability of exhibiting hearing loss, versus those in the service sector, who have the lowest. Those in the latter group, except for the most senior workers ( $>16$ years on the job), have a likelihood of being in the group with the best hearing that is higher than the initial $89.04 \%$ probability.

When we analyzed the joint influence of the sector and noise level factors, we concluded that hearing loss increases in general when the noise level on the job rises from low to high, independently of the sector of activity. This trend is maintained in the industrial sector for noise levels classified as very high, but varies in the service and construction sectors, where the probabilities of having good hearing are greater than for high levels.

The study of the three factors together (sector, noise level and time on the job) confirmed the above findings. As concerns the sector factor, even though the service sector exhibits the most extreme results for one of its variants (high noise level), in general we see that the workers in this sector present higher probabilities of having good hearing, with the opposite being true for construction sector workers. In terms of the noise level on the job factor, we see that, in general, individuals who work in environments that are classified as low-noise have better hearing than those who are exposed to moderate, high or very high level noise environments, who exhibit a much less pronounced difference between one another. If we focus on the workers' time on the job, we generally see that the likelihood of having good hearing is inversely proportional to the time on the job for all sectors and for practically all noise levels.

In light of these results, we may infer that the factors analyzed affect the development of hypoacusia, such that the probability that it will develop rises with noise level and time on the job for any sector of activity. In general, it is the workers in the service sector who exhibit the best hearing, with construction sector workers having the worst hearing.

As concerns the noise level on the job, our study confirms the theories that relate the noise that is produced on the job with the hypoacusia that affects part of the population. Therefore, noise is an con-
taminant of great interest, as Hernández (Hernández Díaz \& González Méndez, 2007) had anticipated, that can negatively affect the health of workers who are exposed to it at their work centers. Also verified are the studies conducted by Sanz (Sanz López, 2013) and the publications of Fernando Pablo (Fernando Pablo J.A, 1996) on the relevance between noise level and the development of hypoacusia, which hold that the higher the sound pressure, the greater the hearing damage or impairment.

As concerns the time on the job factor, our research confirms the studies that hold that hearing worsens with prolonged exposure, as stated by Fernando Pablo (Fernando Pablo J.A, 1996), who refers to this variable as "occupational age", or the number of years that a worker has been employed in a job with a given noise level. Also confirmed along this same line are the empirical studies by López González (López González, 1981) and Talbott-E.O. (Talbott et al., 1990), among others. Our results also concur with those of studies that posit that the harmful effect of noise is proportional to the duration of the exposure, such as Clemente Ibáñez (Clemente Ibáñez, 1991), Sataloff (Sataloff, 1953), Howell (Howell, 1978), Burns and Robinson (Burns \& Robinson, 1970) and Dobie (Dobie, 1995).

Seemingly confirmed as well is the direct relationship between the combination of high noise levels and several years of exposure and the incidence of occupational hypoacusia, as noted by Calviño del Río (Calviño del Río et al., 1982), Delgado (Delgado, 1991), Ruiz (Ruiz, 1997), who concludes that there is a marked difference in terms of the incidence of hypoacusia between the exposed and nonexposed population, and Flottorp (Flottorp, 1973).

As a final conclusion, it is important to note that the three factors analyzed differ in intensity in terms of how they affect the hearing of individuals. The least influential factor is the sector of activity, followed by the noise level on the job, which varies considerably in favor of better hearing for noise levels classified as low, and finally time on the job, which is the most influential factor and exhibits the greatest differences between its potential states, with workers whose time on the job is rated as low or medium exhibiting the best likelihood of having good hearing.

Lastly, this study provides a foundation for future research that can be used in specific studies to analyze in depth some of the factors that comprise our Bayesian network, and thus relate variables of diverse origins, whether demographic, professional or non-professional, to the development of hypoacusia.

## Conflict of interest

The authors declare that there is no conflict of interest in the publication of this document.

## Acknowledgments

The authors are grateful to the Ingemédica S.L. Prevention Service for their collaboration in collecting the data used to conduct this study.

## 5 BIBLIOGRAPHY

Acciardi, M. (2008). Bayesian networks en diagnóstico psiquiátrico o psicopatológico.
Bartosińska, M., \& Ejsmont, J. (2002). Health condition of employees exposed to noiseextra auditory health effects. Wiadomosci lekarskie (Warsaw, Poland: 1960), 55, 2025.

Borg, P.-O. B., Erik. (2001). Long-term objective and subjective audiologic consequences of closed head injury. Acta oto-laryngologica, 121(6), 724-734.
Burns, W., \& Robinson, D. W. (1970). Hearing and noise in industry. Hearing and noise in industry.
Calviño del Río, A., Abreu García, V., \& Cárdenas Sotolongo, B. (1982). Sordera profesional; enfermedad frecuente en la práctica de la salud ocupacional; informe preliminar. Revista cubana de higiene y epidemiología, 20(3), 408-418.
Castillo, E., Gutierrez, J. M., \& Hadi, A. S. (2012). Expert systems and probabilistic network models: Springer Science \& Business Media.
Clemente Ibáñez, M. (1991). Enfermedades profesionales del oído. Revista Medicina y Seguridad del Trabajo(152).
Delgado, C. (1991). MC Efecto sobre la audición en ambiente laboral ruidoso. Revista Medicina y Seguridad del Trabajo, Madrid(152).
Díaz, C., Goycoolea, M., \& Cardemil, F. (2016). Hipoacusia: Trascendencia, incidencia y prevalencia. Revista Médica Clínica Las Condes, 27(6), 731-739.
Dobie, R. A. (1995). Prevention of noise-induced hearing loss. Archives of OtolaryngologyHead \& Neck Surgery, 121(4), 385-391.
Espinosa, F., \& Sánchez, M. (1991). El ruido industrial como patología laboral. Revista Medicina y Seguridad del Trabajo, Madrid(152).
Fawcett, T. (2006). An introduction to ROC analysis. Pattern recognition letters, 27(8), 861-874.
Fernando Pablo J.A. (1996). Manual de Higiene Industrial: Fundación Mapfre.
Flottorp, G. (1973). Music-A Noise Hazard? Acta oto-laryngologica, 75(2-6), 345-347.
Friedman, N., Linial, M., Nachman, I., \& Pe'er, D. (2000). Using Bayesian networks to analyze expression data. Journal of computational biology, 7(3-4), 601-620.

García-Herrero, S., Lopez-Garcia, J. R., Herrera, S., Fontaneda, I., Báscones, S. M., \& Mariscal, M. A. (2017). The Influence of Recognition and Social Support on European Health Professionals' Occupational Stress: A Demands-Control-Social SupportRecognition Bayesian Network Model. BioMed research international, 2017.
Gravendeel, D., \& Plomp, R. (1960). Micro-noise trauma? AMA archives of otolaryngology, 71(4), 656-663.
Hallam, R., Ashton, P., Sherbourne, K., \& Gailey, L. (2006). Acquired profound hearing loss: Mental health and other characteristics of a large sample: Hipoacusia adquirida profunda: Salud mental y otras características de una muestra grande. International Journal of Audiology, 45(12), 715-723.
Hanley, J. A., \& McNeil, B. J. (1982). The meaning and use of the area under a receiver operating characteristic (ROC) curve. Radiology, 143(1), 29-36.
Hernández Díaz, A., \& González Méndez, B. M. (2007). Alteraciones auditivas en trabajadores expuestos al ruido industrial. Medicina y seguridad del trabajo, 53(208), 09-19.
Howell, R. (1978). A seven-year review of measured hearing levels in male manual steelworkers with high initial thresholds. Occupational and Environmental Medicine, 35(1), 27-31.
Kohavi, R. (1995). A study of cross-validation and bootstrap for accuracy estimation and model selection. Paper presented at the Ijcai.
Koller, D., \& Friedman, N. (2009). Probabilistic graphical models: principles and techniques: MIT press.
Kryter, K. D. (2013). The effects of noise on man: Elsevier.
Lau, C. L., Mayfield, H. J., Lowry, J. H., Watson, C. H., Kama, M., Nilles, E. J., \& Smith, C. S. (2017). Unravelling infectious disease ecoepidemiology using Bayesian networks and scenario analysis: A case study of leptospirosis in Fiji. Environmental modelling \& software, 97, 271-286.
Ley de Prevención Riesgos Laborales, 31/1995, de 8 de noviembre (1995).
Lin, F. R., Yaffe, K., Xia, J., Xue, Q.-L., Harris, T. B., Purchase-Helzner, E., . . . Simonsick, E. M. (2013). Hearing loss and cognitive decline in older adults. JAMA internal medicine, 173(4), 293-299.
López González, L. (1981). Comportamiento del umbral auditivo en jóvenes trabajadores de una industria textil Comportamiento del umbral auditivo en jóvenes trabajadores de una industria textil: IMT.
Lucas, P. J., Van der Gaag, L. C., \& Abu-Hanna, A. (2004). Bayesian networks in biomedicine and health-care: Elsevier.
Mani, S., Valtorta, M., \& McDermott, S. (2005). Building Bayesian network models in

medicine: The MENTOR experience. Applied Intelligence, 22(2), 93-108.
Mcshane, D. P., Hyde, M. L., Finkelstein, D. M., \& Alberti, P. W. (1991). Unilateral otosclerosis and noise-induced occupational hearing loss. Clinical Otolaryngology, 16(1), 70-75.
Mohr, P. E., Feldman, J. J., Dunbar, J. L., McConkey-Robbins, A., Niparko, J. K., Rittenhouse, R. K., \& Skinner, M. W. (2000). The societal costs of severe to profound hearing loss in the United States. International journal of technology assessment in health care, 16(04), 11201135.

Monasterio, R., \& Serrano, M. (1991). B. Patología del Ruido. Medicina y seguridad en el trabajo(152), 39-44.
Nowak, J., \& Bilski, B. (2003). Factors modifying noise-induced hearing loss. Medycyna pracy, 54(1), 81-86.
Observatorio de Enfermedades Profesionales. (2017). Memoria Anual 2016. Observatorio De Enfermedades Profesionales (CEPROSS) Y De Enfermedades Causadas O Agravadas Por El Trabajo PANOTRATSS. Retrieved from http://www.segsocial.es/Internet 1/Estadistica/Est/Observat orio de las
Enfermedades Profesionales/cepross2k11/Pa rtes_comunicados/a\%C3\%B1o2014/index.ht m. .
OIT. Convenio sobre seguridad y salud de los trabajadores y medio ambiente de trabajo (1981). Ginebra

Pascolini, D., \& Smith, A. (2009). Hearing Impairment in 2008: a compilation of available epidemiological studies. International journal of audiology, 48(7), 473-485.
Peter, R., March, S., \& du Prel, J.-B. (2016). Are status inconsistency, work stress and workfamily conflict associated with depressive symptoms? Testing prospective evidence in the lidA study. Social Science \& Medicine, 151, 100-109.
Pittavino, M., Dreyfus, A., Heuer, C., Benschop, J., Wilson, P., Collins-Emerson, J., . . . Furrer, R. (2017). Comparison between generalized linear modelling and additive Bayesian network; identification of factors associated with the incidence of antibodies against Leptospira interrogans sv Pomona in meat workers in New Zealand. Acta tropica, 173, 191-199.
RD REAL DECRETO 286/2006, de 10 de marzo, sobre la protección de la salud y la seguridad de los trabajadores contra los riesgos relacionados con la exposición al ruido (2006).

RD Real Decreto 1299/2006 de 10 de noviembre, por el que se aprueba el cuadro de enfermedades profesionales en el sistema de la Seguridad Social y se establecen criterios para su notificación y registro (2006).

Real Decreto 1316/1989, de 22 de octubre, sobre protección de trabajadores frente a los riesgos derivados de la exposición al ruido durante el trabajo (1989).
Real Decreto 1971/1999, de 23 de diciembre, de procedimiento para el reconocimiento, declaración y calificación del grado de minusvalía (1999).
Ruiz, E. (1997). Contaminación Acústica: Efectos sobre Parámetros Físicos y Psicológicos. Tesis Doctoral. Documento ftp://tesis. bbtk. ull. es/ccppytec/cp188. pdf.
Rytzner, B., \& Rytzner, C. (1981). Schoolchildren and Noise: The 4 kHz Dip-Tone Screening in 14391 Schoolchildren. Scandinavian audiology, 10(4), 213-216.
Sanz López, L. (2013). Caracterización del cocleograma de ratón CBA en un modelo de ototoxicidad inducido por ruido.
Sataloff, J. (1953). Effect of prolonged exposure to intense noise on hearing acuity. Arch. Otolaryng, 58, 62-80.
Shipley, B. (2009). Confirmatory path analysis in a generalized multilevel context. Ecology, 90(2), 363-368.
Talbott, E. O., Findlay, R. C., Kuller, L. H., Lenkner, L. A., Matthews, K. A., Day, R. D., \& Ishii, E. K. (1990). Noise-induced hearing loss: a possible marker for high blood pressure in older noise-exposed populations. Journal of occupational medicine.: official publication of the Industrial Medical Association, 32(8), 690-697.
Tosal, J., \& Santa María, G. (1992). Riesgo profesional en aserrado y preparación industria de la madera. Revista Salud y Trabajo. Madrid(89).
Uña, M., García, E., \& Betegón, A. (2000). Protocolo de vigilancia sanitaria específica para los/las trabajadores/as expuestos al ruido. Madrid: Centro de Publicaciones de la Secretaría Técnica del Ministerio de Sanidad y Consumo, 1-77.
Van Vliet, D. (2005). The current status of hearing care: can we change the status quo? Journal of the American Academy of Audiology, 16(7), 410-418.
Ward, W. D. (1995). Endogenous factors related to susceptibility to damage from noise. Occupational medicine (Philadelphia, Pa.), 10(3), 561-575.
Yueh, B., Shapiro, N., MacLean, C. H., \& Shekelle, P. G. (2003). Screening and management of adult hearing loss in primary care: scientific review. Jama, 289(15), 1976-1985.