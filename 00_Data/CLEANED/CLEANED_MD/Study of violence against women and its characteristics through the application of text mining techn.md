# Study of violence against women and its characteristics through the application of text mining techniques 

E. M. A. Stephanie ${ }^{1} \cdot$ L. G. B. Ruiz ${ }^{2} \cdot$ M. A. Vila ${ }^{1} \cdot$ M. C. Pegalajar ${ }^{1}$<br>Received: 21 April 2023 / Accepted: 15 August 2023 / Published online: 14 September 2023<br>(c) The Author(s), under exclusive licence to Springer Nature Switzerland AG 2023


#### Abstract

The Internet provides a wide variety of information that can be collected and studied, creating a massive data repository. Among the data available on the Internet, we can find articles about Violence against Women (VAW) published in the digital press, which are of great societal interest. In this work, we utilized Web scraping techniques to gather VAW-related news from the internet. Applying Text Mining techniques, we conducted a study on VAW and its characteristics. Our work comprises an exploratory analysis and the application of Topic Modelling to VAW events to identify latent topics and their semantic structures. We employed classification algorithms on a set of VAW press articles to determine the type of violence they refer to, namely physical, psychological, sexual, or a combination of them. We proposed two methodologies to target the data: the first one is based on dictionaries of VAW types, while the second approach extends the former by using the predominant violence to identify other associated types. Furthermore, we implemented two feature selection techniques: TF-IDF and Chi $^{2}$. Then, we applied Support Vector Machine, Decision Tree, Bayesian Networks, XGBoost Classifier, Random Forest, and Artificial Neural Networks. The results obtained showed that the classifiers achieved better performance when using Chi $^{2}$. The Boost Classifier demonstrated the best performance, followed by Random Forest.


Keywords Violence against women $\cdot$ Text mining $\cdot$ Machine learning $\cdot$ Classification $\cdot$ Topic modelling

## Abbreviations

ANN Artificial neural networks
BC Boost classifier
BN Bayesian networks
DT Decision tree
VAW Violence against women
LDA Latent Dirichlet allocation
NPL Natural processing lenguage

[^0]RF Random forest
SVM Support vector machine

## 1 Introduction

VAW (Violence against Women) is a social phenomenon that exists in most societies; it does not discriminate on the basis of religion, age, or social class. In [1], VAW is defined as any act of gender-based violence that results in, or is likely to result in, physical, sexual, or psychological harm or suffering to women and girls, including threats of such acts, coercion, or arbitrary deprivation of liberty, whether occurring in public or in private life.

On the other hand, The United Nations, in their statement against VAW, defines VAW as any act of gender violence that results in psychical, sexual, or psychological damage or suffering, including threads, coercion, or deprivation of liberty [2].

All sorts of abuse cause suffering and misery to the victims and their families. They represent a burden on society in


[^0]:    1 Department of Computer Science and Artificial Intelligence, University of Granada, Granada, Spain
    2 Department of Software Engineering, University of Granada, Granada, Spain

addition to having an economic impact with a human and emotional cost. Therefore, this social problem requires a lot of attention, it is essential to take strict measures to eradicate this type of violence to be able to provide a dignified life and gender equality to women and girls.

In many countries, there are laws that protect women and girls, but even these resources are not enough to stop this phenomenon from the society. Now it has become common to hear in the media such as television cases describing acts of VAW, and not only on television, even digital newspapers publish cases of VAW in their digital content. These articles are a source of data that describe facts about violence and its characteristics, becoming a rich source of information that should be studied.

We can find many studies on Violence against Women or Girls. Some of them have been made on short texts: in [3], the authors carried out a Topic Modelling methodology for study domestic violence on tweets. In [4], the authors implemented a similar solution on Twitter for the study of feminist conversations in order to identify gender problems that need to be addressed but do not have political preference. In [5], the authors used tweets and statistical software to conduct a sentimental analysis of femicide in Mexico and Colombia. In [6], the author studies the safety of women in social networks. In this study, Twitter's API was used to obtain tweets and carry out sentiment analysis. Other studies were carried out on reports: in [7], the author made use of sexists report to examine their content for topic and concept extraction. The research made in [8] showed the use of Formal Concept Analysis and thesaurus to find out domestic violence cases in police reports. Another author [9] designed a set of dictionaries with mental health illnesses and produced lexical patterns to identify mental disorders in reports recorded by the police. In [10], the author conducted a study of crimes using police reports in England and Wales. In [11], the author conducted a study on police records in New South Wales to extract information regarding domestic violence victims involving autism. They operated clustering and classification techniques to group crimes based on occurrence frequency. Motwani et al. [12] used reports to discover patterns in crimes against women by means of time-series and Naïve Bayes algorithms. In [13], the authors used police records of domestic violence incidents with structured information (e.g. gender, postcode, ethnicity) and other details to identify patterns such as the type of abuse and injuries suffered by victims. Other studies were conducted on information obtained from the internet: in [14] the information were collected from web applications. This study implemented the sparsitybased document representation to improve Topic Modelling. In [15], a study on violence in India was done by a web scraping approach to retrieve data from media diaries along with the employment of the LDA method for crimes classification. Karami et al. [16] analysed uncovering sexual harassment experiences reports with a text mining approach. LDA solution revealed hidden topics in examined their weight across three variables: institution type, harasser gender and victim's field of study. In [17], crime reports were retrieved from the web in India to apply k-Means for crime detection and k-NN for classification and prediction. In [18], the authors scraped news articles from India to study the VAW on social media and other platforms.

Text Mining is the process of extracting the useful information from the textual data. It is an exciting research area as it tries to discover knowledge from unstructured texts. It is used in various types of research domains like natural language processing, information retrieval, text classification and text clustering. LDA is a very popular technique used today [19-21]. It is widely used in natural language processing to disclose semantic structures named topics [22, 23]. This technique does not require a set of previously labelled documents; therefore, it is an unsupervised algorithm capable of identifying hidden topics from a document's corpus. In addition, Text classification is a branch of Text Mining that can automatically analyse text documents and assign a set of pre-defined categories based on its content using Natural Language Processing (NLP).

Contrary to other studies, our work will be carry out on large text that has no structure, which require more resources to be processed and analysed. Using web scraping techniques, the data will be gathered from different digital newspapers web sites from different countries; Colombia, Peru, Ecuador, Mexico, Argentina, Salvador, Guatemala and Spain, this work will be done in the language of origin of the data in this case Spanish. In this research, Text Mining techniques will be applied to extract interesting knowledge from unstructured text documents, also to understand the nature and effects of VAW. LDA will be apply for the generation and identification of latent themes in the dataset. Additionally, Text classification algorithms will be applied to classify the news into the different types of violence suffered by women and girls.

This research work is organised as follows: Sect. 2 describes the proposed methodology with the phases flow and tasks carried out in this research, Sect. 3 details the results obtained by the text classification procedures applied and Sect. 4 summarises the conclusions of this research.

## 2 Methodology

### 2.1 Data gathering

The first step of this study consisted of data collection. Web scraping is a technique that allows us to gather information from various sources such as web pages, emails, text documents, PDFs, mainframe reports, audio, and video to store

and analyse it. We applied web scraping methods to retrieve news from the internet. The extraction process begins by sending a request to the web page containing the information. If the recipient processes and accepts the request, we obtain the data and send it to the web scraping program for further storage. However, much of this data are partially or completely unstructured, requiring a non-trivial process to transform it into a structured format suitable for the classification algorithms [24].

By applying web scraping techniques, we collected social communication content from different countries, including México, Colombia, Ecuador, Perú, Argentina, Guatemala, El Salvador, and Spain. To gather news related to VAW, we defined several keywords for advanced searches, using terms such as violence against women, femicide, feminicide, and gender violence to obtain specific content on the topic of violence. Through this approach, we managed to collect 7100 news articles related to VAW from various digital journals, which had a scarcely structured format.

In Fig. 1 below, we can observe the distribution of the different documents collected from various newspapers. With web scraping, we obtained a larger number of documents from La Nación and a smaller portion from El Salvador.

We collected 7100 documents from various digital newspapers, all related to VAW events. Additionally, when we observe Fig. 2, we can see the annual distribution of these documents. Our dataset encompasses documents from 2002 to 2020. It is evident that the lowest proportion of documents was obtained between 2002 and 2010, while the highest concentration of data was observed between 2016 and 2019.

### 2.2 Preprocessing

Data processing plays a crucial role in the application of text mining techniques. It is a task of significant importance for knowledge discovery, as it aims to provide structure to the data. In this study, text processing consisted of the following tasks:

- We began by removing any links, numbers, and special characters from the text, thereby reducing the document's size.
- Stop words: we eliminated the most frequent terms that do not add value to the text and could potentially affect the learning process of the text mining models. In this study, it was necessary to add words to the stop words list because it could not eliminate highly frequent words such as "femicide," "woman," among others.
- Tokenization: this task involved separating the text into words or terms called tokens to convert the documents into a list of words.
- Stemming: many words share the same grammatical root. In this task, we replaced each term with its root to reduce the dimensionality of the documents and eliminate unnecessary words. However, stemming was not applied in topic modelling because it made it difficult to interpret the terms in the topics obtained.


### 2.3 Feature selection

Feature Selection is a task of pivotal importance, as the features used in the learning process can significantly influence the performance and efficiency of algorithms. An improper choice may lead to unreliable results. Therefore, it is necessary to make a correct selection of the most relevant features in the text. In this study, we utilized two methods for this task: TF-IDF and $C h i^{2}$. The process followed the next lines.

- Feature Weighting: TF-IDF transforms the text (terms or words) of each news into a vectorial space of features represented in a numerical format. TF-IDF combines two metrics. TF stands for the number of times that a specific term $t$ appears in a document $d$. IDF is the proportion of times that the term appears in all the documents [25]. The resultant matrix represents the document's terms by weights $W(d, t)$. It will be computed as follows:
$W(d, t)=T F(d, t) \cdot \log \left(\frac{N}{d f(t)}\right)$
In Eq. (1), $N$ is the number of documents and $d f(t)$ is the number of documents that contain the term $t$. Thus, the TF-IDF value is the result of the multiplication of the frequency of the term in a document and the $\log$ of the number of documents that present that term [26].

In this study, we applied TF-IDF with the n-gram method. Here, it represented the words in a sequence of length [1, 2]. In addition, we extracted those features that met the max and min thresholds of 0.85 and 0.15 , respectively. In doing so, we obtained appropriate features for the classification problem.

- Chi ${ }^{2}$ : The text may contain weak characteristics for the classifier. As a way to remove them, we used the $C h i^{2}$ algorithm. In the feature selection process, we can find two variables. One of the two is the occurrence frequency of the feature $t_{i}$, and the other one is the occurrence probability of a category $C_{k}$. By executing the $C h i^{2}$ method, we can examine the relevance between $t_{i}$ and the category $C_{k}$. The more relevant information has $t_{i}$, the higher score for $C_{k}$. It can be defined as follows:
$\mathrm{X}^{2}\left(t_{i}, C_{k}\right)=\frac{N(a d-b c)^{2}}{(a+c)(a+b)(b+d)(c+d)}$
The result of Eq. (2) is the correlation between the feature $t_{i}$ and the category $C_{k}$. If it is 0 , then they are independent. The higher the value, the more $t_{i}$ affects the category [27].

![img-0.jpeg](img-0.jpeg)

Fig. 1 Document distribution according to the source
![img-1.jpeg](img-1.jpeg)

Fig. 2 Document distribution by year

In this research, we searched the adequate number of features. The best number was 1000 features. We chose the most relevant 1000 features for the classification algorithms trained.

### 2.4 Tagged training for classification

A classification process begins with a pre-labelled partitioning of the data for training the models, along with a validation set to assess the goodness of fit. In this section, we will
describe how the labelling methods were applied to our training dataset before proceeding with the text classification step.

Figure 3 illustrates the flowchart of the document processing. The document classification requires a separate dictionary for each type of violence, with each dictionary containing a set of keywords that define the glossary. Additionally, each term in the dictionary is associated with a weight, and there is a set of words that carry more impact, forming the most relevant words in the dictionary.

In this research, we predict three types of violence: physical (F), sexual (S), and psychological (P). Accordingly, we

Table 1 Dictionaries' structure


created a dictionary for each type of violence, selecting terms from a thesaurus and conducting exploratory analysis of word frequency. The assignment of weights was based on the following theory: the probability of a specific event occurring ranges from 0 to 1 , where 0 means it will not happen, and 1 means it will definitely occur. For this reason, we assigned a weight of 1 to each term in the dictionary, with higher-impact terms receiving greater weight.

Furthermore, we decided to create a set of strong words related to each wordlist. These strong words are determined by the terms that constitute the dictionary. For instance, in the case of physical violence terms, those that describe the victim's death were assigned strong status. For psychological violence ( P ) terms, words describing verbal abuse, disrespect, and profanity, including racist words, were considered strong. On the other hand, there are no strong terms in the Sexual violence (S) dictionary because all its words have a carnal connection, leading us to consider all of them as strong.

Table 1 details the structure of the dictionaries. The psychical dictionary has 43 terms of which 7 terms are of high relevance. The sexual dictionary presents 8 terms but as they were of a sexual nature, all of them were considered relevant. Lastly, the psychological one has a total of 25 terms of which 8 were highly relevant.

Having defined the dictionaries and the terms they contain, two types of labelling were developed: by weights and matches, and a second method based on weights, matches and relationships between types of violence. The following is an explanation of the techniques used to label the news and assign a type of violence.

### 2.4.1 Classification based on dictionaries and matches between dictionary's terms and news

This labelling method is utilised to associate a document with a specific type of violence. To achieve this, certain rules are followed to validate whether a document references that category. In our corpus of 7100 news articles, allocating a class involves meeting any of the following rules:
(1) Weight threshold: this rule compares each new document with all the dictionaries. It calculates the term matching, and the final score is the result of adding the related weights and matches. As mentioned earlier, the probability of an event occurring lies between $[0,1]$. The optimal threshold was estimated at 0.25 , which was set as the weight for the dictionary's words. If this rule is satisfied, the document is classified under that specific type of violence.

Figure 4 illustrates an example of a specific document having 3 matches in the physical dictionary, with the sum of their weights surpassing the 0.25 threshold. As a result, this document is labelled as "physical violence." However, the psychological and sexual rules were not met for this particular document.
(2) Number of matches: the minimum number of coincidences required was set at 3 . Therefore, a document with at least 3 matches in any dictionary would be identified with the violence type corresponding to that particular dictionary.

Figure 5 illustrates that a specific text had 3 matches with the F (physical violence) dictionary and one match with the P (psychological violence) dictionary. In this case, the document was labelled as F (physical violence) because the rule requires at least 3 matches with any dictionary, and the remaining two dictionaries did not meet this condition.
(3) Finally, the dictionaries contain certain words of high relevance. With this in mind, any document that presents at least one term coinciding with any of the highly relevant terms in the dictionary is labelled with the class corresponding to that specific dictionary.

Figure 6 shows an example where a document had 2 matches with the highly relevant terms of the physical dictionary and 1 match with the psychological dictionary. In this case, the document was labelled as both F (physical violence) and P (psychological violence) because the condition of having at least one highly relevant term was met for both dictionaries.

### 2.4.2 Classification based on weights, matches and relationships amongst types of violence

In addition to the previously explained method, a second labelling methodology was employed. This approach also utilizes dictionaries for each type of violence, including their respective weights and strong terms. By comparing the terms in the dictionaries with those in the news articles using the obtained weights, we can determine the association of the news articles with each type of violence. In this case, the relationships between different types of violence were taken into consideration. We applied two methodologies with the ultimate goal of evaluating our results and determining if

![img-2.jpeg](img-2.jpeg)

Fig. 3 Relationship amongst dictionaries, terms, weights and relevant words
Fig. 4 Weight threshold rule representation
![img-3.jpeg](img-3.jpeg)

Fig. 5 Number of matches rule representation
![img-4.jpeg](img-4.jpeg)

Fig. 6 Relevant terms rule representation
![img-5.jpeg](img-5.jpeg)

Fig. 7 Types of violence and their links

![img-6.jpeg](img-6.jpeg)
there are significant differences that enhance the classification process.

The tagging process based on the relationships between different types of violence involves the detection of three violence types: F (physical), P (psychological), and S (sexual). For the detection task, three rules were applied, as previously explained: the weight of matches between terms and dictionaries, matches between documents and dictionaries, and matches of relevant terms. Subsequently, we modelled the existing links to ultimately label each document with one class.

In Fig. 7, we can observe that when a document is labelled with F (physical violence), it will also be tagged with P (psychological violence), denoted as FP. Conversely, if the document refers to S (sexual violence), it involves both F and P , resulting in its classification as FPS.

In order to establish the relationship between each violence, we followed the next concepts. In [28] it is said that sexual violence ( S ) is any kind of behaviour in which one is forced to obtain stimulation or sexual gratification. For this reason, this sort of violence is a compound of physical and psychological damage. The victims of sexual abuse, especially children, will present psychological consequences, depressive and bipolar disorders, anxiety, stress as well as self-destructive behaviour [29]. The authors of [30] point out that several investigations have been done on different kinds of victims and they showed that the physical, psychological and sexual violence cause a series of negative consequences both physical and psychological. In [31] the authors mention that physical (and/or sexual) assaults always produce any sequel, harm, damage or psychological trauma. Thus, they stress that the psychological violence is a set of attitudes and behaviours where an aggression or abuse is done in a subtler way and harder to detect, assess and prove. Consequently, psychological violence may occur without other kind of abuse (physical or sexual).

From these concepts previously exposed, we concluded that the different types of violence might be related as can be seen in Table 2.

The aforementioned concepts are gathered in Table 2, from which we defined that when physical violence is detected in a document, it will involve psychological violence

Table 2 Relationship among types of violence


as well. If a document manifests psychological violence, then no more violence will be linked. And sexual violence will include the rest of them.

## 3 Algorithms classification

The classification process involves the application of algorithms to detect different kinds of violence described in the news. Before classification, we labelled the training set, where we encountered unbalanced classes. To address this problem, we applied the Smote technique, which involves the synthetic creation of minority samples. This approach balanced the classes and prevented the model from being biased by the other classes. We employed optimization for the parameter search to enhance the classification process, along with cross-validation with $k=10$. The implemented algorithms were Random Forest (RF), Support Vector Machine (SVM), Decision Tree (DT), XGBoost, Naïve Bayes (NB), and Artificial Neural Networks (ANN), and their details are provided below.
(RF) is an algorithm with an ensemble learning approach. It was developed to solve classification and regression problems and is based on Decision Trees that utilize bagging to build each tree and create a forest [32]. We set 600 trees, the Gini criterion, and a depth of 10 .

The second option was (SVM), a supervised machinelearning algorithm for classification. Its goal is to find a hyperplane of maximum margin to split the data into several regions [33]. The parameters settled for this work were $C=1, \gamma=1$, and a linear kernel.

Next up is (DT), an algorithm consisting of a root, branches, and leaves. The root node is the father of all nodes

and serves as the superior node in the tree structure [34]. The following parameters were set for this: a max depth of 10 , a minimum number of 4 samples for splitting, and 6 as the minimum number of samples per leaf.

The fourth algorithm was XGBoost, widely used by scientists in the Machine Learning field owing to its good results. XGBoost is a scalable model that is easy to adapt. Similar to RF, it continuously adds trees and performs feature selection to grow the tree. After incorporating a new tree, the model learns a new function to adjust the residuals of the last prediction [34]. Here we used 10 as the max depth, 0.4 for $\gamma$, and 200 estimators.

The conditional probability-based algorithm (NB) is considered a powerful tool for classification problems. It works well with unbalanced datasets and missing values [35]. We utilized the multinomial distribution for our problem.

Lastly, the well-known (ANNs). ANNs are a popular Soft Computing technique inspired by the neural net of the brain [36]. We designed an ANN with an input layer, 4 hidden layers, and an output layer. The activation function was softmax, and the error function was the categorical cross-entropy for multiclass classification.

### 3.1 Evaluation

There are various ways to measure the effectiveness of a classifier; amongst the most used, we have Precision, F1 score and Accuracy. These metrics derive from determining whether a document was true positive (TF), false positive $(\mathrm{FP})$, true negative $(\mathrm{TN})$ or false negative $(\mathrm{FN})$. In our research, we adopted these three statistics to evaluate the classification done by the models [37].

Accuracy is an indicator often applied to evaluate the performance of the classifiers that work on text-based problems [27]. It represents the portion of documents that were properly estimated within a group and it can be computed using the following formula:
$\mathrm{Acc}=\frac{\mathrm{TP}+\mathrm{TN}}{\mathrm{TP}+\mathrm{FP}+\mathrm{TN}+\mathrm{FN}}$
F1 score is the harmonic mean of precision and recall. It represents the capability of the classifiers to locate a document within the right class. When the recall and precision are high, then the F1 score is high [25]. This metric can be defined as follows:
$F 1$ score $=\frac{2 \mathrm{TP}}{2 \mathrm{TP}+\mathrm{FP}+\mathrm{FN}}$
Thirdly, Precision is a metric that measures the number of samples properly classified against the total [25]. This follows the next formula:
$\mathrm{Precision}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FP}}$
Hundreds of authors have applied the aforementioned metrics so as to assess obtained results with varied models [39-43]. Considering them, we adopted these three metrics to evaluate our text classifiers.

## 4 Results

### 4.1 Exploratory analysis

Through an exploratory analysis of the document collection, we identified relationships between terms known as bigrams and trigrams. Table 3 displays the most commonly occurring bigrams correlated to VAW, such as «redes sociales» (social networks), «ministerio público» (public ministry), and «abuso sexual» (sexual abuse). As for trigrams, we found «gender violence victims», «víctimas violencia género» (gender violence victims in Spanish), «procuradoría general justicia» (attorney general's office), and «mujeres víctimas violencia» (women victims of violence). These results illustrate a combination of the most frequently mentioned words

Table 3 Top 15 bigrams and trigrams


![img-7.jpeg](img-7.jpeg)

Fig. 8 Word cloud of the collected documents about VAW
in the documents. The occurrence of «redes sociales» may be attributed to the fact that it has become the most widely used communication medium where information, including VAW cases, can be published.

The next step is to calculate the word frequency from the tokens (unigrams) of the documents. Table 3 illustrates a set of the 330 most frequent words in our collection. It can be easily observed how feminicidio and femicidio are present amongst the most common ones. These terms define the international homicide of a woman or girl becoming the most representative words used by the media to report about VAW. On the other hand, the terms asesinar, crimen or homicidio, describe an action but are not able to define the kind of victim. In the same line, other words recurrent were casa (house) and pareja (partner), which might suggest that the most common aggressor is the partner and the crime scene home.

In Fig. 8, we can see the most common characteristics of VAW. It seems like casa and pareja are the most mentioned in the database, and femicidio is the most popular of them. This is consistent with the fact that femicidio represents the murder of women and children in many Latin American countries.

### 4.2 Topic modelling

To perform LDA modelling, we aimed to determine the optimal number of topics ( k ) using the log-likelihood measurement and perplexity. Based on these metrics, the best
number of topics was found to be 16 , along with 55 iterations. This combination allowed the algorithm to generate the most representative topics. In Table 4, you can find the topics generated by LDA, along with the 15 most probable terms per topic. Utilizing the distribution probability, we selected the top 20 documents with the highest probability values. From these documents, we identified the 15 most frequent words, which were then used to build the identification labels [29].

However, in Table 4, it can be noticed that topics 6 and 13 do not have any labels. This is because these topics were not represented by any document in their probability distribution. Consequently, we were unable to obtain the 20 most important documents for these topics, which is a crucial step in creating the identification label. The lack of representation may be due to the fact that these topics have a lower probability of occurring in the document collection.

Table 5 expresses the most dominant topics and the obtained distribution of documents. The latter shows how «manifestaciones sobre la VAW en redes sociales» is the dominant one of the collection with a distribution of $0.7421 \%$, followed by the topic «pareja homicida» with $0.3489 \%$, «violencia contra niñas» with $0.3155 \%$, and finally «petición de leyes o políticas de protección e igualdad» with $0.2658 \%$. This data reflects how social networks are a medium of communication widely employed by citizens to protest against the VAW. The acts of violence are happening within the family environment, being the partner the most common aggressor. On the same page, we can see how the girls are now a highly vulnerable group to suffer either physical, psychological or sexual violence. Lastly, we can appreciate the efforts in society to eradicate all forms of VAW by holding marches and protests.

Table 6 details two examples of the most relevant document by topic. In order to identify these documents, we took the highest-two values of the document distribution provided by LDA. The document has a too-long extension therefore we will show the titles for a general idea of the content. We can observe that the labels assigned are capable of a clear representation of the main content of the document distributed within the topic. This makes the label a useful tool to find topics and capture the main idea of the documents in the same distribution.

### 4.3 Text classification

The text classification process was carried out following the two targeting approaches for the training set. In this section, we will present the results obtained by the classifier algorithms for each methodology. The accuracy, precision, and $F 1$ measures will be used to analyse the results and the performance of the classifiers.

Table 4 Relevant topics about violence against women


Table 5 Most dominant topics


### 4.3.1 Classification based on the weights and matches

By applying the labelling methodology using matches between the dictionary's terms and news, we acquired 7 classes to be predicted: F, P, S, FP, FPS, PS, and FS. The results of the classification algorithms are shown in Table 7. It presents the results for the TF-IDF and $C h i^{2}$ feature selection techniques.

The best-performing algorithms were XGBoost and Random Forest. XGBoost generated the best metrics on TF-IDF and $C h i^{2}$. However, with a minimal difference between them, the best performance was obtained using $C h i^{2}$, with an accuracy of 0.90045 and an F1 score of 0.702926 . These values indicate that a high percentage of documents were classified correctly into their respective categories.

On the other hand, RF achieved an accuracy of 0.846135 and an F1 score of 0.59456 , which were significantly improved by XGBoost. The latter proved to be more efficient in classifying the news, demonstrating superior performance and more robust outcomes.

Table 6 Most dominant news per topic


Table 7 Evaluation metrics classification based on the weights and matches


It is interesting to note that despite being one of the most popular algorithms, the ANN presented poor classification results in this problem.

### 4.3.2 Classification based on weights, matches and relationships amongst types of violence

In this section, we present the results obtained by applying the labelling methodology based on weights, matches, and relationships among types of violence. Three classes were identified for prediction: FP, FPS, and P. The results are summarised in the following table.

Table 8 presents the results of the classification process. We can observe that in this scenario, several classifiers offered good performance. XGBoost had the highest metrics, with an accuracy of 0.9845232 and an F1 score of 0.8939695 when applied over the $C h i^{2}$ feature selection method. It was followed by RF with an accuracy of 0.9603095 and an F1 score of 0.7182750 , and ANN with an accuracy of 0.9376820 and an F1 score of 0.7162896 . Based on these results, we can consider XGBoost as the best classification algorithm using the $C h i^{2}$ technique, making it the most efficient model for text classification. Additionally, it is worth mentioning that, as shown by the results, the classification feature selection using $C h i^{2}$ was more accurate in classifying text than those generated by TF-IDF.

Table 9 provides all the accuracy values provided by the algorithms when using the $C h i^{2}$ feature selection. We can observe the Accuracy and Precision measures obtained by the models. In both scenarios, XGBoost stood out as the best

Table 8 Evaluation metrics classification based on weights, matches and relationships amongst types of violence

Table 9 Evaluation accuracy measurements of the algorithms for classification based on weights and matches classification based on weights, matches and relationships amongst types of violence problem




classifier, showing good performance and stable predictions with high accuracy. On the other hand, the least ranked algorithms were DT and NB, as their results were not optimal enough for our problem.

We can observe that in this scenario, several classifiers offered good performance. XGBoost had the highest metrics, an accuracy of 0.9845232 and a $F 1$ score of 0.8939695 applied over the $C h i^{2}$ feature selection method. Followed by RF with an accuracy of 0.9603095 and $F 1$ score of 0.7182750 . Plus, ANN with an accuracy of 0.9376820 and a $F 1$ score of 0.7162896 . From these results, we can consider XGBoost as the best classification algorithm using the $C h i^{2}$ technique. As a consequence, this is the most efficient model for text classification. In addition, I would like to mention that, as can be seen from the results, the classification feature selection by $C h i^{2}$ were more accurate to classify text than those generated by TF-IDF.

## 5 Conclusion

In this research, we explored the use of Text Mining techniques applied to news about VAW. In text classification, applying feature selection with TF-IDF and $C h i^{2}$ helped
considerably reduce the dimension of the documents and improve the performance of the classifiers. The results obtained determined that the features obtained with $C h i^{2}$ yielded better results in terms of Accuracy and F1 measures. Analysing the performance of each classifier, we found that XGBoost was the best algorithm. This suggests that XGBoost and $C h i^{2}$ were a good combination for more stable text classification of types of violence.

Applying Topic Modelling, we generated 16 latent topics related to VAW. The topics' terms clearly showed different features of VAW, and the terms were easy to interpret, making it possible to label most of the themes. Additionally, we could observe the distribution of news by topic and created a tag for each topic. In conclusion, we consider Topic Modelling techniques useful for extracting important information from large and even short texts. This helps discover hidden social topics and their features.

This research demonstrated that Text Mining techniques can be effectively used to study a large amount of unstructured text documents and achieve good results. The findings from this work can serve as strong evidence of how classification techniques can be employed in VAW studies or detecting other kinds of violence.

For future work, we propose to classify the news into different types of VAW using fuzzy rules, which would allow us to have the membership degree of each document per category. Additionally, we suggest combining Topic Modelling with clustering algorithms to group the topics provided by LDA. This could further enhance the understanding and organisation of the topics related to VAW.

Author's contribution All authors have contributed equally to this work.

Funding We acknowledge financial support from the Ministerio de Ciencia e Innovación (Spain) (Research Project PID2020-112495RBC21) and the I + D + i FEDER 2020 project B-TIC-42-UGR20.

Availability of data and materials To access the item, go to https://doi. org/10.6084/m9.figshare.21252987.v1.

## Declarations

Conflict of interest The authors declare no conflicts of interests.
Ethical approval and consent to participate Not applicable.
Consent for publication Not applicable.
