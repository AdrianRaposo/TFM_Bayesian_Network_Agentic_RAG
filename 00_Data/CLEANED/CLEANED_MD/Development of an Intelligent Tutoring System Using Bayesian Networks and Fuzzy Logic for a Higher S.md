# Article 

## Development of an Intelligent Tutoring System Using Bayesian Networks and Fuzzy Logic for a Higher Student Academic Performance

Meltem Eryılmaz ${ }^{1, *}$ (D) and Afaf Adabashi ${ }^{2}$ (D)<br>1 Department of Computer Engineering, Atilim University, Ankara 06830, Turkey<br>2 Department of Software Engineering, Atilim University, Ankara 06830, Turkey; adabashi.afaf@gmail.com<br>* Correspondence: meltem.eryilmaz@atilim.edu.tr; Tel.: +90-312-586-8346

Received: 19 August 2020; Accepted: 18 September 2020; Published: 23 September 2020


#### Abstract

In this experimental study, an intelligent tutoring system called the fuzzy Bayesian intelligent tutoring system (FB-ITS), is developed by using artificial intelligence methods based on fuzzy logic and the Bayesian network technique to adaptively support students in learning environments. The effectiveness of the FB-ITS was evaluated by comparing it with two other versions of an Intelligent Tutoring System (ITS), fuzzy ITS and Bayesian ITS, separately. Moreover, it was evaluated by comparing it with an existing traditional e-learning system. In order to evaluate whether the academic performance of the students in different learning groups differs or not, analysis of covariance (ANCOVA) was used based on the students' pre-test and post-test scores. The study was conducted with 120 undergraduate university students. Results showed that students who studied using FB-ITS had significantly higher academic performance on average compared to other students who studied with the other systems. Regarding the time taken to perform the post-test, the results indicated that students who used the FB-ITS needed less time on average compared to students who used the traditional e-learning system. From the results, it could be concluded that the new system contributed in terms of the speed of performing the final exam and high academic success.


Keywords: intelligent tutoring system; adaptive e-learning; knowledge level; Bayesian network; fuzzy logic

## 1. Introduction

Recently, there has been a rapid growth in web-based intelligent tutoring systems (ITSs) to support teaching processes, with the aim of helping students adaptively navigate through online learning materials. Web-based educational systems facilitate distance learning, and offer easy access to any knowledge domain and learning process, at any time, for learners from different backgrounds with different needs, preferences, and characteristics [1]. According to Yang et al. [2], the differences among student characteristics play an important role in developing web-based educational environments. Therefore, successful online teaching demands multimedia techniques, adaptive techniques, and reasoning abilities in addition to a user-friendly interface. Students often enjoy the ease of use and communication in virtual learning environments, as well as personalized learning paths [3]. Thus, the challenge is to develop web-based learning systems that are dynamically adapted to each individual user in order to deliver knowledge effectively. Therefore, web-based educational systems have to be dynamically adaptable for the individual learner and they must be capable of monitoring the learner activities and be capable of providing personalization for specific needs, preferences, and knowledge. Moreover, these systems have to offer students more freedom in order to navigate through online course content and control their learning pace and learning sequence [4]. Because of these features, educational

institutions, whether traditional or online, rapidly began to adopt adaptive learning environments, virtual learning environments, and e-learning management systems to increase the number of students of online courses [3,5].

Adaptive navigation supported technology, which has the ability to help students acquire knowledge faster and improve learning outcomes, is one of the common technologies applied to web-based educational systems [6]. Many intelligent tutoring systems (ITSs) adopt such technology, such as the intelligent tutoring systems platform (ITSPL) [4], which supports student navigation in cyberspace by adapting to the goals and knowledge of the individual user [7,8]. The ability of an ITS to provide adaptivity is based on the technology of student modeling. According to John Self [9], student modeling is a process that is responsible for representing a student's goals and needs, analyzing the student performance and determining prior and gained knowledge. However, the student modeling process is not a black-or-white one, but it often deals with uncertainty, and it cannot be accurately said that a student has learned the concept or not [1]. Therefore, the challenge is to construct an effective student model, which is the key component in an ITS to deal with uncertainty. Uncertainty in educational systems can occur from examining student variables such as assessing the level of student knowledge [10].

ITSs use artificial intelligence (AI) techniques to automatically adapt the teaching content to fit learners' needs and goals. Personalized and adapted e-learning environments can be established using AI techniques, which are mainly applied in knowledge representation, managing learning strategies, and monitoring students' status [11]. AI is a branch of computer science interested in making computers behave like human beings. Its rich resources of tools, technologies, and paradigms of computing such as fuzzy logic and Bayesian networks, and it has proved to be extremely useful in solving challenging problems in different fields as well as educational environments involving incomplete and/or uncertain knowledge. Bayesian network and fuzzy logic are widely used in the literature to develop the student model and solve the problem of uncertainty in adaptive e-learning systems [12,13,14]. The Bayesian network is a tool used to manage knowledge from different situations and model the interdependencies between domain topics. Moreover, it is able to increase the ability of an ITS to make the appropriate decision based on students' characteristics. The Bayesian network is a direct acyclic graph (DAG) that is used to model dependency between various concepts of a particular domain based on a probability distribution [15]. Bayesian networks have been used as a probabilistic framework to solve the problem of dynamically managing and updating student models [16]. These networks can represent different components of a student model such as knowledge level, learning styles, goals, and motivation, etc. Bayesian networks receive a great deal of attention from designers and developers of adaptive educational systems due to their sound mathematical foundations, as well as for their ability to handle uncertainty, using probabilities. Another tool, fuzzy logic is able to increase the ability of an ITS to examine and assess a student's academic performance, which is one of the most important parts of the educational process. Fuzzy logic can be viewed as an extension of the concept of a fuzzy set theory proposed by Lotfi Zadeh in 1965 [17]. It reflects how people think and attempts to model the human sense of words and decision-making. It is a form of multi-valued logic that allows the definition of intermediate values between conventional evaluations, such as true/false, yes/no, high/low, and big/small. The fuzzy logic system (FLS) maps a crisp input into a fuzzy output using the fuzzy sets theory. In general, an FLS consists of four stages: the fuzzifier, rule base, inference engine, and defuzzifier [18]. The fuzzy logic technique, with its ability to handle imprecise information and uncertainty, has been used to improve the performance of an adaptive e-learning system and assessing and evaluating student knowledge [19,20].

This paper develops an intelligent tutoring system, called FB-ITS, using a hybrid method based on the Bayesian network and fuzzy logic to adaptively support students in learning an Excel course; the adaptation is achieved by modeling the students according to their knowledge level. Since this paper presents a study concerning the combination of two techniques of artificial intelligence that include the Bayesian network and fuzzy logic, in the development of ITSs where educational materials

can be personalized for individual learners, it takes a step toward the evaluation of the proposed system by comparing it with the existing models.

FB-ITS takes the advantages of fuzzy logic and the Bayesian network. The fuzzy logic is used to determine the student performance in a particular topic of domain according to her/his prior knowledge; the Bayesian network is used to identify the state of the related topics in which they are ready to learn, or not, according to the evidence that comes from the fuzzy logic system. Therefore, this study develops and implements three versions of the ITS. The first version is created using the Bayesian network only; the second version is created using the fuzzy logic only, and the third version is created using a combination of the Bayesian network and fuzzy logic, and is called FB-ITS. Moreover, the evaluation is conducted by comparing the proposed FB-ITS with a traditional e-learning system that has been developed without the use of artificial intelligence technologies

The purpose of this study is to develop and suggest an intelligent tutoring system, called FB-ITS, by combining the positive sides of both fuzzy logic and the Bayesian model, using a hybrid method to adaptively support students in learning, in which the adaptation is achieved by modeling the students according to their knowledge level.

The research questions of this study, in line with this general purpose are:
Does the building of a student model, using Bayesian networks based on fuzzy logic, increase the performance of ITS in terms of student academic performance compared to using fuzzy logic and Bayesian networks separately?

Do students who studied with FB-ITS have higher academic performances than students who studied using the traditional e learning system? This study presents the design and implementation details of the intelligent tutoring system developed. It presents the architecture of FB-ITS, including all its components: knowledge domain model, student model, adaption model, and user interface. Moreover, it discusses the usage of fuzzy logic and the Bayesian network in development of FB-ITS, in detail. The study presents the experiment conducted to evaluate the developed system. Moreover, summary results of the experiment include the comparison of the three versions of the ITS in which the design is based on: (1) fuzzy logic; (2) Bayesian networks; and (3) a combination of Bayesian networks with fuzzy logic technique. It presents the results of the comparison of the developed ITS, including the three versions with the traditional e-learning system.

The major objectives of developing FB ITS are:

- To identify and update the Knowledge Level (KL) of a student;
- To provide adaptation of the course material in which topics should be delivered, which topics need revision, and which topics have been learned;
- To allow each individual student to finish the e-learning course at his/her own pace; and
- To provide feedback and hints for an individual student.


# 2. Related Works 

ITSs are typically classified into several different parts, and each part plays an important role. The basic architecture of an ITS consists of four components: student model, knowledge domain model, tutoring model, and user interface model [11,21]. These basic components interact with each other to achieve different functions. Several ITSs have been developed for learners in different areas with various strategies in order to improve teaching ways and help students learn better [8,22]. ITSs aim to adapt a comprehensive learning approach to meet the needs of students. Therefore, it is essential that the students' model should be created accurately while considering their knowledge levels, learning skills, and preferences [22,23]. Then, the information required must be used and developed in order to improve the e-learning environments. Hence, AI techniques are regarded as useful tools for several reasons as they have the ability of developing the human decision-making process and building automatic learning models. There are several AI techniques that have been used to build and develop intelligent e-learning systems, including fuzzy logic, Bayesian networks, neural networks, and genetic

algorithms. These techniques can help one to learn from uncertain, vague, and incomplete data. Furthermore, the ability of AI techniques to imitate the intelligence of human beings, and their ability to solve complex problems, makes them ideal tools in e-learning.

Artificial Neural Network (ANN) is a supervised learning model consisting of a large number of simple processing units, called "neurons", arranged in different layers, known as input layer, hidden layer, and output layer, while a multilayer neural network is a connection of simple neurons called "perceptron". Neural networks can be utilized to develop intelligent e-learning systems to assist during the educational process and act as the teacher in the traditional classroom. Learning Styles Identify Artificial Neural Networks (LSID-ANN), an approach based on artificial neural networks, is used by Bernard et al. [24] for identifying students' learning styles, based on the Felder-Silverman learning style model. LSID-ANN uses four artificial neural networks with a three-layer perceptron configuration. Each network is designed for one of the four learning style dimensions: active/reflective, sensing/intuitive, visual/verbal, and sequential/global. In addition, the authors evaluate the LSID-ANN approach by using real data from 127 computer science undergraduate students, including their behavior data in a university course and their results on the Index of Learning Styles (ILS) questionnaire. This study achieved a pleasing accuracy level of learning style identification; thus, helping teachers with giving good advice to their students, as well as increasing student performance and learning satisfaction.

Genetic algorithms are an evolutionary computing method of artificial intelligence used to solve complex problems because they provide a large number of approximate alternative solutions for optimal solutions. The idea of genetic algorithms is based on the mechanism of natural selection and the natural gene system [25]. Azough et al. [26] studied the problems facing the development of e-learning systems as an optimization problem and addressed them using genetic algorithms. They described an adaptive system used to generate adaptive pedagogical paths based on the learners' profile and current basic learning objectives. A genetic algorithm is successfully applied by Han [27] to evaluate a personalized learning system able to dynamically update the process of the course and the target user model during the learning process. As a result, this study provides a good framework with the ability to generate the personalized courses in an e-learning environment.

Fuzzy logic and Bayesian network techniques are widely used for developing intelligent educational systems. They have been used in various ways, such as examining and assessing student characteristics to generate student profiles, for the purpose of evaluating their level of knowledge to be used as bases for building educational systems [28,29]. These techniques are also used to facilitate the diagnostic process in order to adjust course content to meet the needs and preferences of each learner [30,31]. Hsieh et al. [32] proposed a personalized recommendation system for an English article based on accumulated learner profiles. This system employs the fuzzy inference method, memory cycle updates, learner preferences, and analytic hierarchy process to improve the English language abilities of students in an intensive reading environment.

Moreover, in the research conducted by Priya and Keerthy [33], the rule-based fuzzy logic technique has been used for an automatic learning process to provide adaptive instructions to learners through an e-learning system. The fuzzy knowledge definer with personalized brilliancy evaluation (FuzKPBE) is introduced in this paper to predict the related course and concepts based on the specific individual skills of each concept. Almohammadi et al. [18] proposed a fuzzy logic based system that can learn the preferred knowledge delivery to the various students, based on their individual characteristics, to generate a personalized learning environment.

A web-based educational system that performs individualized instruction on the domain of programming languages has been developed by Chrysafiadi and Virvou in [1]. This approach is implemented and evaluated in an educational application module called "fuzzy knowledge state definer" (FuzKSD). FuzKSD operates based on fuzzy cognitive maps (FCMs) to perform user modeling by dynamically identifying and updating the knowledge level of students related to all the domain subjects. Additionally, a system has been presented by Asopa et al. [34] to evaluate student performance

in ITS environments, in which a fuzzy inference system provides the students with step-by-step instructions as to their learning status.

Another well-known AI technique used to construct intelligent e-learning systems is Bayesian networks. Andes, which is an adaptive educational system developed by Gertner and VanLehn [35], uses Bayesian networks to find former probabilities of knowing a set of knowledge elemental parts in teaching physics. Moreover, Bayesian networks have been used [36] to construct an ITS named Virtual Physics System (ViPS) to teach physics concepts in middle schools. In this system, the Bayesian network is used to represent the domain knowledge, to find the possible setups that can be created using components created by an individual student during the learning processes, as well as to generate an adaptive feedback and dynamic hints regarding student actions. Another Bayesian student model has been proposed to measure the difficulty of the problem of parameter specification [37]. This research conducted many experiments to compare the performance of two Bayesian student models. In one of them, the parameters were specified by the experts, in the other, these parameters were learned from the data. It was concluded that both student models provided a satisfactory result in estimating the variables of knowledge. The Personal Home Page (PHP) Intelligent Tutoring System (PHP ITS) was developed by Weragama and Reye in [38]. PHP ITS aims to support novices in learning the PHP language for the purpose of developing dynamic web pages. This system provides exercises for students to solve and then provides appropriate feedback based on the answers. In PHP ITS, the Bayesian network is used to update the students' knowledge level of each topic based on student progress.

In addition, the Bayesian network has been used to develop a solution-based intelligent tutoring system (SITS) for teaching computer programming [39]. SITS takes advantage of Bayesian networks to manage uncertainty based on probability theory for decision-making, to help students in learning.

The comparison of the accuracy of the Bayesian network and fuzzy logic techniques in developing the student model, which are used to predict a student's knowledge level, is discussed [40]. This comparison is based on two variables, prediction_time and correct_prediction. The study concluded that the Bayesian network has higher accuracy than fuzzy logic in predicting student knowledge level. Therefore, this paper attempts to enhance the efficiency of a student model by benefitting from the advantages of both techniques and to overcome their limitations. Integrating fuzzy logic and the Bayesian network into a student model of an ITS is a good idea since both techniques are more consistent with the human being decision making processes.

The student model in FB ITS is a hybrid model that brings the features of fuzzy logic and the Bayesian network together. The reason for using the hybrid method is the fact that the student model needs to combine various aspects of students' characteristics in order to carry out the personalization efficiently [2]. The student model is responsible for tracking the changes in students' knowledge and identifying which parts of knowledge topic a student knows and has learned, and which parts are still not learned.

It has been observed that there are numerous studies in the literature on fuzzy logic and the Bayesian model used in developing learning environments. However, while creating a student model, studies that use these two models together have not been encountered.

# 3. The Proposed System's Architecture 

The proposed system aims to provide an adaptation of the course material based on the knowledge level of a student, in which a topic should be delivered, which topic needs revision, and which topic has been learned. This system is able to identify and update the knowledge level (KL) of a student, allowing each individual student to finish the e-learning course at his/her own pace and provide feedback and hints for an individual student. The basic architecture of FB-ITS, as presented in Figure 1, is based on the classical architecture of ITSs [41]. The importance of the developed FB-ITS is that it is a web-based system which can be used anywhere at any time. This system has been tested in

Google Chrome, Mozilla Firefox, Microsoft Edge, and Internet Explorer browsers. Therefore, it allows a multitude of learners to access the FB-ITS from different platforms.
![img-0.jpeg](img-0.jpeg)

Figure 1. Basic architecture of fuzzy Bayesian intelligent tutoring system (FB-ITS).
This ITS was implemented in the Microsoft Visual Studio 2015 development environment using ASP.net, an open-source server-side web application framework designed for developing dynamic web applications. The functionality of the system was written using VB.net, which is a multi-paradigm, object-oriented programming language, implemented on the. NET Framework. Since an FB-ITS is a web-based system, there should be some mechanism for representing, storing and retrieving data related to the components of the system (the knowledge domain model and the student model) and any data related to the student-system interaction in order to provide adaptation. Microsoft SQL Server 2014 was used to create and manage the database. Microsoft SQL Server is compatible with ASP.net and they interact with each other properly.

Three versions of the ITS were developed and implemented in this research based on the architecture presented in Figure 1. These versions have the same components except for the student model. The student model in the first version was created using the Bayesian network, only according to the Bayesian student model. In the second version, it was created using fuzzy logic only, and in the third version, the student model was created using a combination of the Bayesian network and fuzzy logic, named FB-ITS, to meet the objectives of this study. The purpose of creating these three versions is to answer the research questions and to demonstrate that combining the Bayesian network and fuzzy logic technology increases the performance of the ITS, compared to using fuzzy logic and Bayesian networks separately.

# 3.1. Knowledge Domain Model 

The knowledge domain model in the FB-ITS contains the repository of course materials related to Excel, including test questions, quizzes, and solution keys for each question. All questions and related solution keys are separated from the tutoring system, which are stored in the database. This separation allows developers to create or modify questions without modifying the system itself. The tests and quizzes are displayed when the system attempts to determine the student's knowledge level, and determine whether or not the student had understood a particular topic. Each topic corresponds to one node in the Bayesian network.

Knowledge domain have included the lecture notes and test questions of the Excel course, which is a spreadsheet program, and are provided by the system in various formats, particularly in HTML files, including text, images, and videos according to the syllabus of Introduction to Computers and Information Systems course (CMPE 105) at Atilim University. The instructional objective of this course was to develop computer literacy and competency by introducing fundamentals of computer systems and to develop skills in using software tools. Students were expected not only to explore the Windows environment and learning management systems, but also to use software applications, such as word processors, spreadsheets, and presentation programs.

# 3.2. Student Model 

In FB-ITS, the student model stores both the static and the dynamic characteristics of each learner. Static characteristics include the student name, username, gender, department, and password. This information is set by students during the registration session and this information remains unchanged except for the password that the student can change from her/his profile. The dynamic characteristics, which include the student's knowledge level, is updated during the learning process depending on the student's performance.

The student model in FB-ITS is a hybrid model that brings the features of fuzzy logic and the Bayesian network together. The reason for using the hybrid method is the fact that the student model needs to combine various aspects of student characteristics in order to carry out the personalization efficiently [2]. The student model is responsible for tracking the changes in the students' knowledge and identifying which parts of the knowledge topic a student knows, and has learned, and which parts are still not learned. It consists of two layers, as shown below in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Student model of FB-ITS.

### 3.2.1. First Layer: Fuzzy Logic System

In the FB-ITS, the fuzzy logic system is used to determine the student's performance in a particular topic taking two factors into account; the pre-test grade and the topic test grade. These tests are multiplechoice questions used as variables for gathering evidence to update the Bayesian network, which is why these two variables "Pretest-Grade" and "TopicTest-Grade" used as input variables in the study. On the other hand, the variable student performance in a particular topic of the course material was used as the output of this study, and was utilized as the "Performance".

The "Pretest-Grade" is the score of the pre-test given to the student to measure her/his prior knowledge in a particular domain, the "TopicTest-Grade" is the score of the test given to the student after completing the study of each topic of course material and the "Performance" is the degree of success in a domain topic. A correlating model of the input and output variables is achieved by the established fuzzy rules created by eight faculty members who are experts in the field of computer engineering, and who have taught Excel before. For the input variables, three fuzzy sets are defined for each input variable to describe the student test grade, as it was calculated out of 100 points for both the pre-test and topic test as thus:

- Poor: the degree of success in the domain topic ranges from $0 \%$ to $50 \%$.

- Good: the degree of success in the domain topic ranges from $40 \%$ to $80 \%$.
- Excellent: the degree of success in the domain topic ranges from $70 \%$ to $100 \%$.

Moreover, two fuzzy sets are defined for the output variable to describe the student's performance of a particular topic of the learning material as follows:

- Low: the level of performance in the domain topic ranging from $0 \%$ to $80 \%$.
- High: the level of performance in the domain topic ranging from $70 \%$ to $100 \%$.

Each input variable determines three intervals of membership functions. The membership functions of the test grade consist of poor, good, and excellent levels as shown in Figure 3a. An input and output variable is placed in a scale ranging from 0 to 100. Figure 3b shows the membership functions of the output. This membership function includes the low and high of a student's performance in a particular topic.
![img-2.jpeg](img-2.jpeg)

Figure 3. (a) The membership functions of the test grade, (b) The membership functions of the output.
In this study, the fuzzy rules are provided by experts. All the rules are configured with two input variables (pretest-Grade and TopicTest-Grade) and one output variable (Performance). Given below are the sets of rules using IF-THEN logic:

- If the (pretest-Grade is poor) and the (TopicTest-Grade is poor) then the Performance is Low.
- If the (pretest-Grade is poor) and the (TopicTest-Grade is good) then the Performance is Low.
- If the (pretest-Grade is poor) and the (TopicTest-Grade is excellent) then the Performance is High.
- If the (pretest-Grade is good) and the (TopicTest-Grade is poor) then the Performance is Low.
- If the (pretest-Grade is good) and the (TopicTest-Grade is good) then the Performance is High.
- If the (pretest-Grade is good) and the (TopicTest-Grade is excellent) then the Performance is High.
- If the (pretest-Grade is excellent) and the (TopicTest-Grade is poor) then the Performance is Low.
- If the (pretest-Grade is excellent) and the (TopicTest-Grade is good) then the Performance is High.
- If the (pretest-Grade is excellent) and the (TopicTest-Grade is excellent) then the Performance is High.

Fuzzy rules are triggered after any change in the value of the test result of a particular topic and it updates the performance level of this topic. The output of the fuzzy model is passed to the Bayesian network model as an evidence to update the knowledge level of the related topics.

# 3.2.2. Second Layer: Bayesian Network 

This study uses the Microsoft Bayesian network Toolkit (MSBNx) to construct the Bayesian network model, which is a component-based Windows application for creating and evaluating Bayesian networks [42]. Where the Bayesian network in FB-ITS is implemented by MSBNx, the Excel topics network can be easily modified to address another learning domain.

In FB-ITS, the Bayesian network model consists of 11 nodes, which represent the topics of the Excel course. A total of 11 topic titles were grouped in terms of the Excel course content, according to the syllabus of Introduction to Computers and Information Systems course (CMPE 105).

The dependencies existing among the course topics can be represented as prerequisite relationships. For instance, Topic-1 has to be learned before Topic-2, because understanding Topic-1 is a prerequisite to understanding Topic-2. The node of Topic-1 being depended upon is also called the pre-requisite node. The entire DAG of the Bayesian network implemented in the FB-ITS is shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network implemented in FB-ITS.
After constructing the Bayesian network, a conditional probability distribution (CPD) table is designed for each topic node, taking its parents in the network into account. In this work, all CPDs values were obtained by the experts and the experience of instructors. These probability values will then be used by the model for inference about the problem. The CPD value for Y given X is denoted by $\mathrm{P}(\mathrm{Y} \mid \mathrm{X})$. In the context of Excel topics, the probability of a student having learned topic-1 (Excel Environment) is denoted by $\mathrm{P}($ Topic-1). Moreover, the probability of a student having learned Topic-2 given Topic-1 is denoted by $\mathrm{P}($ Topic-2|Topic-1). $\mathrm{P}($ Topic-2 $=$ Learned/Topic-1 $=$ Learned $)$ is the probability that the student has learned Topic-2 given evidence that the prerequisite Topic-1 has been learned.

The primary purpose of tracking a student's behavior during the interaction with the system is to collect evidence to update the Bayesian network model, where the evidence is the already observed information about this student. Several assessment approaches are used to collect evidence to update the Bayesian network, such as the student's direct responses or his/her answers to the exam questions. Furthermore, some systems include the student's performance scores, time spent on questions, sequences of reading pages or reading times to enhance the student's assessment. In this study, the fuzzy logic system is used to collect the evidence taking into account the prior and current knowledge in a particular topic. The main purpose of the Bayesian network model is to predict the KL of related topics and to identify which topic is ready to be learned and which are not based on the probability.

For each topic node in the Bayesian network model, there are two states: learned or not learned by the student. The learned state of certain topics in the Excel course can be assessed by calculating the posterior probability $\mathrm{P}($ topic $=$ learned/evidence), where the evidence is the student's performance on a prerequisite topic obtained from the fuzzy logic model. If the posterior probability of the topic is greater than or is equal to a certain threshold (this work defines it as being equal to 0.8), this topic is marked as "Learned". Otherwise, the topic is marked as "notLearned". The threshold choosed by the experts as 0.8 because Atilim University uses European Credit Transfer System (ECTS) (https://ec.

europa.eu/education/resources-and-tools/european-credit-transfer-and-accumulation-system-ects) as an internal credit accumulation system, in accordance with the Bologna Process. According to this system, the percentage 80 means the status is "Good" and the grade point is 3.00 over 4.00.

After the topic is marked as "Learned" or "notLearned", the entire Bayesian network is updated and the system can decide which next topic is ready for the student to learn, based on the probabilities of the topic nodes in the Bayesian network. It should be mentioned that the choice of threshold value being equal to 0.8 indicates that a topic having been learned. Finally, FB-ITS updates the dropdown menu to display the topics links in different colors based on these probabilities.

# 3.3. FB-ITS User Interface 

The adaptation model uses the information stored in the student model and knowledge domain model to adapt relevant learning materials. The output of this model is transferred to the system interface to be presented to the student. The adaptation model offers a pedagogical option to support the individual student during the learning process. The adaptive navigation support method is one of the common adaptation methods used in web-based educational systems to support a student to navigate in the learning environment by adapting to the preferences, goals, and knowledge of the individual student [12,43]. This method is used here by the FB-ITS user interface to support a student during the learning process, which involves link hiding and link annotations.

FB-ITS uses drop-down menus to help the student to navigate and browse the course materials. The drop-down menu is more helpful since it guides the student to learn Excel topics step-by-step. This menu can be dynamically updated in terms of font color, based on the current knowledge state of the student and the student is not able to proceed to the next topic until she/he masters the pre-requisite topics by hiding the links for topics that are not yet ready to be learned. Moreover, through the drop-down menu, FB-ITS can notify the student about which topic is ready to be learned and which is not. The link annotation is used for highlighting each topic with an appropriate color based on the student's knowledge level. In addition to the navigation support method, an adaptive presentation mechanism is used by FB-ITS to present the contents of a course topic in various ways, such as text, images, and videos, in order to meet the individual student needs and preferences and to understand the topic effectively.

The FB-ITS is a completely web-based system that can be accessed through a web browser. A student interacts with the proposed system via the user interface. In order to use the system for the first time, a student has to create an account through the registration page. When a student logs into the system for the first time, she/he is required to complete a pre-test to determine her/his prior knowledge of Excel. The pre-test consists of 22 multiple-choice questions. It is possible for the student not to answer any questions if she/he has no relevant knowledge.

The home page of the system appears after finishing the pre-test as shown in Figure 5. In this page, a student can navigate the course materials from the left dropdown menu. The content of the lesson is displayed as text and images. Furthermore, the system provides a video lecture to help a student understand the topic with further explanation, which meets the student's preferences. After the student finishes reading the lesson, she/he has to answer the related test questions. Then, the system will provide feedback according to the test score.

![img-4.jpeg](img-4.jpeg)

Figure 5. System home page.

# 4. Materials and Methods 

### 4.1. Participants

The participants of this study were undergraduate students attending to the Introduction to Computers and Information Systems course (CMPE 105) at Atilim University in the 2019-2020 academic year. This course was selected due to the fact that it has been incorporated into the curriculum of most undergraduate disciplines, so it is expected that more participants will be able to contribute to the evaluation of the proposed system. First, the sample of participants was divided randomly into two groups. The first group (Group A), which is an experimental group, contained 60 students and the second group (Group B), which is a control group, contained 60 students. The sample distribution of group A and B, according to gender and prior knowledge in Excel, is given in Table 1. The sample of the students in Group A was separated into three major subgroups, A1 (ITS using Bayesian networks only, control group 1), A2 (ITS using fuzzy logic only, control group 2), and A3 (Fuzzy Bayesian, experimental group). Each group contains 20 participants.

Table 1. Distribution of participants according to gender and prior knowledge.


### 4.2. Data Collection

Pre-test and Post-tests were used in the research to measure the academic performance of the students. Expert views about content validity and assessment criteria relevance of the tests were obtained based on a triple classification scale. For validity and reliability matter of the multiple-choice test, the study was conducted on a total of 100 students in the pilot study.

4.3. Data Analysis

The collected data from the study were analyzed using Statistical Package for Social Sciences (SPSS) software package (https://www.ibm.com/analytics/spss-statistics-software). The analysis is based on descriptive statistics and analysis of covariance (ANCOVA). In testing every hypothesis of the research, a $5 \%$ significance level that was based on and the differences, which are significant at $1 \%$, were also highlighted.

In order to see whether the academic performance variable for the students studying in learning environments differs or not, covariance analysis (ANCOVA) was used based on the data obtained from knowledge tests performed as pre-test and post-test. For the covariance analysis, which is performed by taking the controlled variable, firstly, equality of the group error variances and normality of distribution of dependent variable were tested. Levene statistics was used for the homogeneity of group variances, and the Kolmogorov-Smirnov test was used to test the normality of the distribution of independent variable.

# 4.4. Experimental Procedure 

The participants in every group received the same content for learning Excel despite using different systems (A1, ITS using Bayesian networks only, A2, ITS using fuzzy logic only, A3, FB ITS, and B, a traditional e learning system). In the presented study, the experiment was conducted for a period of six weeks to validate the proposed system for practical use. In the first week of the experiment, every student attended to the 60-minute session to become familiar with the systems (ITS and a traditional e-learning system). Following that, a pre-survey was presented to the students in order to collect preliminary information such as gender, department, and grade point average (GPA), which is a number representing the average value of the accumulated final grades earned in courses over time. They were then subjected to a pre-test, which was distributed before dividing the participants sample into groups. After that, the students started studying the Excel topics. At the end of the experiment, they completed a post-test as shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. The Experimental Design.

# 5. Results 

## Students' Academic Performance

RQ1. Does the building of a student model using Bayesian networks based on fuzzy logic increase the performance of ITS in terms of student academic performance compared to using fuzzy logic and Bayesian networks separately?

To answer this question, the following hypothesis was put forward:
H1: there is a statistically significant difference between the three groups (A1, A2, and A3) on student academic performance, in favor of Group A3.

Table 2 shows that group A3 had the highest mean value on student academic performance $(\mathrm{M}=82.95, \mathrm{SD}=18.59)$ while group A2 had the lowest mean value on student academic performance $(\mathrm{M}=69.77, \mathrm{SD}=22.81)$.

Table 2. Descriptive Statistics of groups A1, A2, and A3.


In order to test hypothesis H1, the analysis of covariance (ANCOVA) was conducted to compare the students' academic performances in three different groups involved in the experiment. The independent variable was the type of the e-learning system (Groups A1, A2, and A3), and the dependent variable consisted of scores on student academic performance administered after the experiment was completed. The participants' scores on the pre-test administration of the basic knowledge test were used as the covariate in this analysis. Preliminary checks were conducted to ensure that there was no violation of the assumptions of linearity, homogeneity of variances, homogeneity of regression slopes, and reliable measurement of the covariate. Levene's test for equality of variances was used for homogeneity of group variances. The assumption that variances were homogeneous was met, as shown in Table 3.

Table 3. Levene's test for homogeneity of the group variances.


Table 4 illustrated that, after adjusting for pre-test scores, there was a significant difference between the three groups on the post-test scores of the students, $\mathrm{F}(2,56)=11.571, p<0.001$, partial eta squared $=0.292$ (The F means ratio of two variances, df means the number of degrees of freedom; the number of values in the final calculation of a statistic that are free to vary, A $p$-value which means significance value, less than 0.05 is statistically significant, partial Eta squared which is a squared measure of association defined as the ratio of variance in an outcome variable explained by a predictor variable, after controlling for other predictors), indicated a large effect size [44]. Moreover, the results show that, there was a significant moderate effect of the pre-test scores on the post-test scores of the students $(\mathrm{F}=27.074, p<0.05)$, as indicated by a partial eta squared value of $33 \%$.

Table 4. Tests of Between-Subjects Effects.


R-squared $=0.372$ (Adjusted R-squared $=0.338$ ).
The ANCOVA test indicated significant differences between the three groups (A1, A2, and A3). The results of this test did not show exactly where the significance between each two groups lies. As further analysis is needed, the groups between which there is a difference were evaluated by Pairwise Comparisons with Bonferroni adjustment for multiple comparisons.

The results shown in Table 5 indicated significant mean differences between the post-test scores of the group A3 and the group A1 at the $5 \%$ level (mean difference $=27.067$ ), and between the post-test scores of the group A3 and the group A2 at the $5 \%$ level (mean difference $=30.110$ ). There was no significant mean difference between groups A1 and A2. The average difference between the environments with A3 is higher than other environments (A1 and A2).

Table 5. Bonferroni Test (Pairwise Comparisons).


Based on estimated marginal means. * The mean difference is significant at the 0.05 level. a. Adjustment for multiple comparisons: Bonferroni.

H1 is confirmed and it can be concluded that the students who used FB-ITS (A3) to learn Excel yield significantly better academic performance than the students who studied with the ITS using the Bayesian network (A1) and fuzzy logic (A2).

RQ2. Do the students who studied using FB-ITS have a higher academic performance than the students who studied using the traditional e-learning system?

To answer this question, the following hypothesis was put forward:
H2: There is a statistically significant difference between the two groups (A3 and B) in student academic performance in favor of Group A3.

The descriptive statistics for Groups A3 (FB-ITS) and B (traditional e-learning system) are presented in Table 6. This table shows that Group A3 had a higher mean value in the student academic performance $(\mathrm{M}=82.95, \mathrm{SD}=18.587)$ than Group B $(\mathrm{M}=64.33, \mathrm{SD}=26.256)$. In other words, it can be said that the students who used FB-ITS in learning performed better academically compared to the students using the traditional e-learning system.

Table 6. Descriptive Statistics of groups A3 and B.


To test hypothesis H2, a one-way between-groups analysis of covariance was conducted to compare the students' academic performance in two different groups. The independent variable was the type of the e-learning system (A3 and B), and the dependent variable consisted of the scores for the students' academic performance administered after the experiment was completed. The participants' scores on the pre-test administration of the basic knowledge test were used as the covariate in this analysis.

Preliminary checks were conducted to ensure that there was no violation of the assumptions of linearity, homogeneity of variances, homogeneity of regression slopes, and reliable measurement of the covariate.

From Table 7, after adjusting for the pre-test scores, it has come to the light that there was a significant difference between Groups A3 and B on the post-test scores of the students, $\mathrm{F}(1,77)=21.092$, $p<0.001$. The partial eta squared $=0.215$ indicated a large effect size [36]. There was a weak relationship between the pre-test and the post-test scores, as indicated by a partial eta squared value of $20 \%$.

Table 7. Tests of Between-Subjects Effects.


R-squared $=0.283$ (Adjusted R-squared $=0.264$ ).
H 2 is confirmed, and it can be concluded that the students who studied under FB-ITS (A3) have significantly better academic performance than the students who studied using the traditional e-learning system (B).

There is also a statistically significant difference between the groups A1, A2, and A3 in time taken to perform the post-test. Group A2 had the highest mean time value ( $\mathrm{M}=10.65, \mathrm{SD}=5.65$ ), and group A1 had $(M=8.64, S D=6.03)$, while group A3 had the lowest mean time value $(M=7.87, S D=4.84)$. According to the descriptive statistics of the time taken values of two groups, Group B had a higher mean time value $(M=13.86, S D=5.90)$ than group $A 3(M=7.87, S D=4.84)$.

# 6. Discussion and Conclusions 

This study applied AI techniques, including the Bayesian network and fuzzy logic, to create a novel hybrid student model, in order to offer adaptive instruction and personalized support in a web-based intelligent tutoring system. A web-based intelligent tutoring system called FB-ITS was designed and implemented in the present study.

According to the findings, the evaluation of the proposed system showed significantly satisfactory results and positive effects in terms of the students' academic performances, where the results revealed that the students who used FB-ITS to learn Excel had higher academic performances than students who studied Excel with the ITS using the Bayesian network and fuzzy logic separately. By comparing the performance of the presented system with the traditional e-learning, it was concluded that the students

who studied with FB-ITS had a higher mean value on academic performance than the students who studied using the traditional e-learning system. The results of the present work support the results of other studies that used AI techniques to develop intelligent educational systems [1,14,38,45].

Moreover, in terms of the level of time taken to perform the post-test, FB-ITS recorded the lowest mean time value compared with the other two versions. The students who used the FB-ITS needed less time on average to perform the post-test than the students who used the traditional e-learning system. In a similar study [36], the adaptive intelligent system has a good performance compared with another educational system in terms of the time needed to read each domain concept.

The major contribution of the presented study is the development of a new model. It is a novel hybrid student model that combines Bayesian networks and fuzzy logic techniques, and which is designed to promote adaptation and personalization in educational systems. In this manner, the presented student model helps the students who already have prior knowledge about the domain to save time and effort during the learning process. Moreover, it tracks the changes of the knowledge level of the students and dynamically adapts the learning material accordingly. The other contribution comes from the development of a unique online intelligent tutoring system named FB-ITS by the researcher using Microsoft Visual Studio and SQL Server Management Studio. FB-ITS can provide adaptation based on a student's knowledge level using the adaptive navigation support, including the adaptive learning techniques, such as link annotation and link hiding, where the link annotation is used to highlight each topic with an appropriate color. Link hiding is used to hide any links for topics that are not yet ready to be learned.

In addition, the proposed ITS framework can be used as a reference model to develop instances of intelligent tutoring systems by focusing on different views of the domain model, as well as the adaptation model.

In future studies, FB-ITS can be extended to different courses, and the evaluation of the system can be done with different dependent variables. The adaptation of the course materials can be done based on different learning styles besides the knowledge level.

Author Contributions: M.E., with a Bachelor of Science degree in Statistics from METU, Ankara-Turkey, completed her MS degree in Computer Engineering Department at ATILIM University in Ankara. She then was awarded a PhD degree from CEIT (Computer Education and Instructional Technology) Department of Ankara University. M.E. currently conducts research on flipped learning, e-learning, and adaptive learning at the Computer Engineering Department of ATILIM University, as well as jointly continues to publish articles with international institutions on the same, and similar topics, regarding Artificial Intelligence in learning. In this study, she contributes in writing-original draft preparation, supervision, methodology, and editing. A.A. is a software engineer. This study contains part of her PhD thesis, which was supervised by M.E. She contributes in formal analysis, methodology, writing-original draft preparation. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.
