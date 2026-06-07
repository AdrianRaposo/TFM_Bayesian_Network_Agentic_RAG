# FANE: 

## A FAke NEws Detector Based on Syntactic, Semantic, and Social Features Bayesian Analysis

Varsha Arya<br>Department of Electrical and Computer Engineering, Lebanese American University, Beirut, Lebanon \& Center for Interdisciplinary Research, University of Petroleum and Energy Studies (UPES), Dehradun, India<br>Razaz Waheeb Attar<br>Management Department, College of Business Administration, Princess Nourah bint Abdulrahman University, Riyadh, Saudi Arabia<br>Ahmed Alhomoud<br>Department of Computer Science, Faculty of Science, Northern Border University, Arar, Saudi Arabia<br>Mario Casillo<br>University of Salerno, Italy

Francesco Colace
(2) https://orcid.org/0000-0003-2798-5834

University of Salerno, Italy
Dajana Conte
University of Salerno, Italy
Marco Lombardi
University of Salerno, Italy
Domenico Santaniello
(2) https://orcid.org/0000-0002-5783-1847

University of Salerno, Italy
Carmine Valentino
University of Salerno, Italy

## ABSTRACT

In today's society, the continuous exchange of vast amounts of information, often irrelevant or misleading, highlights the need for greater awareness to distinguish between accurate and false information. Recognizing the reliability of information is critical to limiting the spread of fake news, a pervasive problem affecting various sectors, influencing public opinion, and shaping decisions in health care, politics, culture, and history. This paper proposes a methodology to assess the veracity of information, leveraging natural language processing (NLP) and probabilistic models to extract relevant features and predict the reliability of content. The features analyzed include semantic, syntactic, and social dimensions. The proposed methodology was tested using datasets that include social media news and comments captured during the lockdown due to COVID-19, providing relevant context for the analysis. Experimental validation of these different datasets yields promising results, demonstrating the effectiveness of the proposed approach.

## KEYWORDS

Fake News, Fake News Detection, Information Reliability, Natural Language Processing (NLP), Bayesian Networks, Social Media, Information Veracity, Information Systems

## INTRODUCTION

The advent of new methods of disseminating information has provided humanity with many advantages. Social media, in particular, has provided opportunities for people from different backgrounds and cultures to exchange views and compare perspectives on common interests. These extraordinary opportunities surpass interconnectedness, representing significant influence in various

areas. The exponential amplification of traditional word of mouth through digital platforms enhances the ability to connect individuals worldwide. Moreover, social media is not limited to being a networking tool; it serves as an effective medium for communication. Every day, users access content and opinions that allow them to interact with a wealth of information. Reflecting on recent global experiences, particularly during the COVID-19 lockdown (Pennycook et al., 2020), people have relied heavily on virtual interactions, with social media becoming a primary channel for socialization and information exchange.

However, the significant benefits of social media and the broader internet landscape should be confronted with new and emerging challenges. The ease with which information can be disseminated to a wide audience and the possibility of blending into the masses and creating independent information channels have led to the misuse of these new media. Among the various problems that have emerged, fake news stands out as one of the most prominent concerns.

Fake news is a significant and particularly damaging subset of the broader phenomenon of disinformation. This term refers to deliberately disseminating false or misleading information to deceive or manipulate the public. While disinformation can take many forms, from half-truths to distorted interpretations of facts, fake news is intentionally fabricated to appear true, often presented as legitimate but designed to mislead readers about political, economic, health, or social issues. Misinformation can be intentional and unintentional: when misinformation or misleading information is unknowingly spread, it is called misinformation, an unintentional form. In contrast, fake news is a deliberate product created with the specific goal of misleading. They often appear as genuine news, complete with catchy headlines, fictitious or manipulated sources, and plausible contexts to legitimize the fake news.

Fake news can serve different purposes, sometimes causing "information disorder" phenomena (Wardle \& Derakhshan, 2017) and becoming a significant social phenomenon (Baccarella et al., 2018). Notable examples include the role of fake news in the 2016 U.S. general election (Abd-Alrazaq et al., 2020) and in the U.K. Brexit referendum. Although the concept of fake news is intuitive and easy to understand, providing a definition that captures all its facets is more complex. The interdisciplinary nature of the topic makes it difficult to identify the core characteristics that define fake news in all relevant fields. As a result, numerous studies have attempted to define fake news (Zhou \& Zafarani, 2020) and analyze it in depth (Gelfert, 2018; Tandoc et al., 2018). A critical feature of fake news is the intent to deceive readers (Yang et al., 2019) through false information. Specifically, Allcott and Gentzkow define fake news as intentionally and verifiably false news articles that likely mislead readers (Allcott \& Gentzkow, 2017; Zhan, Z. et al., 2022).

Developing methods to detect fake news is essential to prevent readers from being deceived. This approach can be done by focusing on several aspects. One approach is to analyze news stories' content to determine whether they are true or false through comparison with verified sources. This methodology, known as fact-checking, forms the basis of knowledge-based methods (Zhou \& Zafarani, 2020), which aim to automate the fact-checking process. Other approaches, known as style-based methods, seek to identify linguistic and lexical features of news stories. By comparing these features with those found in verified news stories, it is possible to assess the truthfulness or falsity of the content. Another possible analysis concerns the environment and the way news is disseminated. These methods take advantage of the wide use of social media and the web, where access to information is easier than ever. In particular, it is possible to analyze how news spreads and the behavior of users interacting with it, distinguishing between trusted and untrusted sources based on their history (Zhou \& Zafarani, 2020). Finally, source-based methods focus on identifying the source of the news.

Detecting fake news raises critical ethical issues, including the risk of censorship, algorithmic bias, and a lack of transparency about evaluation criteria. There is also the danger of user surveillance and profiling and the possibility that these technologies could manipulate public discourse or favor political interests. Therefore, the role of detection systems in the context of fake news is to identify and report potentially false or misleading content, helping to reduce misinformation and improve the

quality of public debate. However, their role extends to ensuring transparency, avoiding improperly restricting freedom of expression, or distorting the information landscape by taking on a supporting role in the complex and crowded field of social media.

Among the various methodologies for detecting fake news, this paper presents an approach that exploits multiple properties of the news. Specifically, it analyzes the semantic and syntactic properties of the news to identify key features. These are complemented by an analysis of the spread of the news and the users who share it. The identified features feed into a Bayesian network (BN) capable of predicting the truthfulness or falsity of the news. One of the primary strengths of the proposed approach is its ability to improve performance over time through the careful selection of features incorporated into the network. The proposed approach balances the automation required to handle large datasets and the control the designer retains over the analysis methods.

The structure of this paper is as follows. Section 2 aims to describe the literature in the area of fake news. Section 3 describes the proposed approach based on a stylistic and social analysis of fake news, focusing on which features are processed in the proposed system and introducing the feature acquisition operations. Section 4 illustrates the experimental phase used to validate the method. The experimental phase will describe and comment on the results obtained from the proposed approach on the LIAR, CREDBANK, and UNICO datasets. The latter contains data collected about posts concerning the coronavirus and allows the full use of the proposed system's functionality. Finally, Section 5 presents conclusions and future directions.

# RELATED WORKS 

The fake news issue, although not entirely new, has become a significant concern with the rise of the internet and social networks, making it necessary to develop automated methods to determine the truthfulness of news. Machine learning and deep learning methodologies (Jing et al., 2023; Meel \& Vishwakarma, 2020) have become crucial in this regard, focusing on building loss functions to learn from the data whether news stories are true or false (Nasir et al., 2021). In addition, methods exploiting naive Bayes classifiers (NBCs), support vector machines (SVMs), and random forests (RFs) (Girgis et al., 2018) have shown promising results. However, deep learning techniques using artificial neural networks have performed exceptionally well (Luvembe et al., 2023; Ma et al., 2023). Specifically, artificial neural networks (ANNs) (Islam et al., 2020) process news-related information across multiple layers using parameters calibrated with the available data. These parameters are identified through loss function minimization and the back propagation technique. Despite the high performance of deep learning techniques, a key challenge lies in fully understanding the parameter identification process and how neural networks distinguish between verified and fake news.

Despite these limitations, machine learning and deep learning methods are currently the most effective in addressing the big data challenge (Meneses Silva et al., 2021). Acquiring vast amounts of information enables data mining techniques, including machine learning methods, to identify the veracity of news or documents by integrating external resources (Bondielli \& Marcelloni, 2019). Tembhurne et al. (2022) proposed a model named "Mc-DNN" for fake news detection.

The four main approaches for detecting fake news are knowledge based, style based, network based, and source based. Knowledge-based approaches focus on content analysis and integration of information from external knowledge sources to assess the accuracy of news (Thakar \& Bhatt, 2024). This approach includes techniques based on deep learning and machine learning models that use labeled datasets to distinguish true news from fake news. These approaches, such as SVMs, RF, and NBC, learn to recognize fake news by analyzing semantic, linguistic, and logical patterns and often employ data from credible sources or fact-checking databases to verify claims (Thakar \& Bhatt, 2024). Style-based approaches aim to explore how content is written, trying to identify signs of style and language structure that might indicate the falsity of a news story. Content analysis that relies on NLP, such as sentiment analysis, text classification, and language modeling, clearly falls under this

category. Features such as writing style, vocabulary, linguistic anomalies, sensationalism, and typical indications of manipulated news are examined. Network-based approaches examine social dynamics and user behavior in sharing platforms to identify suspicious dissemination patterns (Thakar \& Bhatt, 2024). This typology includes methodologies that analyze social interactions around news, such as sharing speed and user behavior. Using graph neural networks (GNNs) to model the relationships between users and news is an example of a network-based approach that seeks to understand how fake news spreads within social networks. Finally, source-based approaches focus on assessing the credibility of sources spreading a news story. Source analysis relates to the ability to verify news sources or identify whether the news comes from sources that are recognized as reliable. Zhang et al. (2023) proposed a deep-learning-based fake news detection model. Sahoo \& Gupta (2021) proposed a model based on multiple features for automatic fake news detection on social networks.

Table 1. Summary of fake news detection methodologies


Various detection techniques have been developed based on the processed information, with knowledge-based approaches focusing on specific features such as:

- The author of the news item;
- The headline, which summarizes the content and topic of the news to attract readers' attention;
- The body, which is the actual textual content of the news story;
- The attachments (images/videos), which help make the story more understandable through visual aids.

The headline is significant in determining news credibility (Rubin et al., 2016), as it captures the reader's attention and can induce sharing without verifying the content. To mitigate the spread of unverified news, social networks often encourage users to verify the body of the news first.

Knowledge-based methods can also benefit from graph structures combined with deep learning (Cui et al., 2020; Hu et al., 2021) to process features. Other methodologies use association rules to identify patterns within the text (Diaz-Garcia et al., 2020). Hybrid approaches that combine knowledge-based and style-based methods are also employed (Seddari et al., 2022). Style-based methodologies, in particular, take a linguistically oriented approach involving lexical, syntactic, and semantic features (Afroz et al., 2012) to detect the falsity of written or verbal news.

Key grammatical and lexical features include the number of syllables, words, and sentences. Various approaches to fake news recognition use these features to detect grammatical errors, emotionally charged terms, and persuasive intent. In addition, lexical and grammatical complexity, such as sentence length and number of syllables per word, are considered (Burgoon et al., 2003).

Another detection methodology is to analyze the spread of information on social networks to assess the authenticity of news stories. Frequently, these approaches use epidemiological models, such as the SIR model (Huynh et al., 2023; Shahi et al., 2021). In addition, news source research is a valid method for determining the authenticity of news (Hassan et al., 2020; Liu et al., 2020).

Visual-based features are also employed, which allow the analysis of images and videos associated with news stories (Jin et al., 2017). These features can be used with context-based features, which address the social context in which the news is shared. Social context analysis helps improve the detection and verification of news authenticity (Shu et al., 2017). These features include user-based, post-based, and network-based elements. User-based features describe individuals or groups who interact with news online. Post-based features classify the emotions or opinions of those interacting with news, representing a post-level, group-level, and temporal analysis. Finally, network-based features try to identify the characteristics of the network on which news is shared.

In the literature, some of the most prominent fake news detection techniques use SVMs, conditional random fields (CRFs), RFs, decision trees (DTs), hidden Markov models (HMMs), and logistic regression (LR) (Rubin et al., 2016; Vosoughi et al., 2017). However, machine learning and deep learning techniques, particularly those employing supervised learning, have surpassed these traditional methodologies in terms of performance. Specifically, many studies use deep learning techniques based on recurrent neural networks (RNNs) and convolutional neural networks (CNNs). Early RNN approaches in the context of fake news detection include the work of Qawasmeh et al. (2019), while Chen et al. (2017) present a CNN-based model.

Other studies have obtained significant results using supervised and unsupervised techniques to identify fake news. Yang et al. (2019) propose an unsupervised method that divides users into hierarchical groups and uses Gibbs sampling to calculate their trustworthiness. Castillo et al. (2011) apply supervised learning to create a dataset and determine labeled topics, which are then used to extract relevant features and build a classifier to assess credibility. Janze and Risius (2017) address the 2016 U.S. presidential election using Facebook posts employing various features to combine SVM and RF techniques. Long et al. (2017) detect fake news using a long short-term memory (LSTM) model supplemented with speaker profiles, which serve as attention factors for news text learning and are also used as input data. Finally, Dong et al. (2018) use two-way attention-based recurrent units to extract news content and a deep model to obtain hidden representations of news side information. These inputs form an attention matrix that facilitates learning the distribution of attention to identify fake news.

Table 2. Summary of literature analyzed


The literature study reveals that fake news detection techniques exploit diverse strategies to detect fake news by analyzing different features that describe different aspects of the phenomenon. Below, an approach will be proposed that aims to assess the stylistic and social aspects of the phenomenon by integrating the possibility of understanding from the data how these aspects intersect with each other.

# THE PROPOSED APPROACH 

Over the years, interest in developing new methodologies and systems for detecting fake news has grown significantly. Considering the socioeconomic impact that fake news can generate, governments and companies are increasingly focused on creating tools to assess the veracity of news and take appropriate action. However, current methodologies use different technologies, and the identification of fake news relies on multiple factors (Casillo et al., 2020). As a result, no universally accepted method has yet emerged.

The approach proposed in this section aims to detect fake news from semantic, syntactic, and social perspectives. Each aspect has unique characteristics that can represent and define textual content. The goal is to develop a reference model to identify fake news by capturing its main characteristics. To this end, the proposed system provides semantic, syntactic, and social analysis of fake news. The information obtained is used to train a BN, which then estimates the truthfulness of the news with a certain probability.

Many approaches in the literature primarily aim to analyze the ways in which news spreads, preferring network-based or source-based analyses. Instead, the proposed approach aims to differentiate itself through a style-based analysis integrated with the study of how the news interacts with users. It then goes on to identify classes of users based on their reliability. In this area, the system focuses on analyzing language from a syntactic and semantic point of view by analyzing posts in English, which have metrics of interest capable of identifying the text's reading difficulty level and the author's education level. In addition, techniques for analyzing news sentiment, topic identification, and similarity to fake news are integrated. Finally, the system evaluates the social aspect of the phenomenon by examining, in addition to the number of shares or likes and comments, the mode of interaction and identifying the type of user interacting with the news.

The system processes the information through two main stages. The first stage involves training the BN by analyzing fake news to determine the weights of the nodes in the network corresponding to the probabilistic relationships between the features. Identifying these weights during the learning phase allows fake news to be interpreted based on its syntactic, semantic, and social features (Cordella et al., 2013; De Stefano et al., 2012). Figure 1 illustrates the general workflow.

Figure 1. Summary of the training phase for the proposed detection method
![img-0.jpeg](img-0.jpeg)

The second stage involves filtering and analyzing the news to rank it using the BN. In this stage, the BN processes the news and calculates a degree of falsehood. Figure 2 schematically illustrates the operation of this stage of the system.

Figure 2. Summary of the fake news identification after the training phase
![img-1.jpeg](img-1.jpeg)

The proposed approach aims to develop a detection method that can handle different types of fake news (posts, articles, etc.) and offer an understandable methodology that can be improved with additional elements.

The ability to split the training phase, which takes place offline, with the trained classifier, which is available in the online phase, allows the system to handle fake news classification queries in a consistent time frame. In particular, during the offline phase, data will need to be processed to identify the BN structure that will enable the classification of news. On the other hand, after data cleaning and pre-processing, the prediction phase will occur during the online phase. In addition, using a BN will allow the system to have fast response times, ensuring its scalability and the possibility of interfacing with social media.

# The Syntactic Analyzer 

For the identification of fake news, the syntactic analysis module examines the syntactic indices essential for constructing the Bayesian model, constituting the nodes of the network and their possible values. The indices considered in this module include the number of characters, the Flesch Index, and the Gunning Fog Index (GI).

The number of characters in the text of a news story is a crucial factor in characterizing fake news. In fact, fake news often has excessively long or concise texts. The possible ranges identified for this parameter are divided into five groups, as shown in Table 3. This parameter is particularly relevant for platforms such as Facebook or online blogs, where the number of characters in a post is not limited. In contrast, other social networks, such as Twitter, impose a maximum limit of 280 characters.

Table 3. Intervals for the number of character identifications


The Flesch Index is used to estimate the readability of a text. Although this index was originally developed for English, it can be applied to written and oral texts. The Flesch Index, also known as the Flesch-Kincaid Index (F-K), was introduced in the 1970s by scholars Rudolf Flesch and J. Peter Kinkaid. It was developed empirically by studying average educational attainment within the U.S. Navy. The index is still widely used in education and can be calculated using formula (1).
$F=206.835-\left(84.6^{*} S\right)-\left(1.015^{*} P\right)$
where

- $\quad F$ is the readability of the text, obtained considering the number of words, syllables, and sentences.
- $P$ is the average number of words per sentence (AWS).
- $S$ is the average number of syllables per word (ASW).

Table 4 explains how to interpret this score. Generally, fake news is very hard to read (range $30-60$ ) or very simple (range $70-100$ ).

Table 4. F-K score meaning


Table 4. Continued


The GI compiles the comprehensibility of an English language text. The index can estimate the years of education a person needs to understand the text on first reading. The following steps allow for calculating the GI:

- Select a passage (such as one or more complete paragraphs) of approximately 100 words. Do not omit any sentences.
- Count "complex" words, which consist of three or more syllables. Do not include proper nouns, family slang, or compound words. Do not include common suffixes (such as -es, -ed, or -ing) as a syllable.
- Add average sentence length and percentage of complex words.
- Multiply the result by 0.4 .

The complete formula is:
$G I=0.4^{*}\left[\left(\frac{\text { words }}{\text { sentences }}\right)+100^{*}\left(\frac{\text { ComplesWords }}{\text { Words }}\right)\right]$
Table 5 reports the GI range. Fake news usually presents a fog index between 6 and 9 or 14 and 17.

Table 5. GI range


The F-K and GI allow for the determination of the understanding of the text, and these features permit fake news detection (Choudhary \& Arora, 2021; Santos et al., 2020).

# The Semantic Analyzer 

The semantic analyzer is designed to extract semantic features from news content. The central idea of this module is to semantically analyze documents and extract features that can help assess the veracity of news. For example, mentioning public figures in unusual places may suggest low reliability of the news content, primarily if it reports information about atypical scenarios. The characteristics considered by this module include news topics, similarities to known fake news, and news sentiment.

The first characteristic is the topic of the news. Fake news often focuses on trending topics of interest and can influence public opinion. Commonly affected areas include health, politics, economics, wars, and significant events such as natural disasters. The binary feature indicates whether the news item is related to these topics (1) or not (0). In this context the approach of Colace et al. (2014) can be used to supplement any missing information about it.

The second semantic feature is similar to fake news, assessed using the mixed graph of terms (MGT). This graph represents a text through recurring words and their connections, analyzing possible co-occurrences of terms within the text. The MGT compares the text with previously labeled news articles, allowing the system to estimate the degree to which a news item resembles known fake news. The system then classifies the output as similar, neutral, or dissimilar.

The last semantic feature is the extraction of news sentiment. In this case, texts are analyzed and labeled using a proposed approach (Colace et al., 2015), which estimates the sentiment expressed in the news (Clarizia et al., 2020). This analysis captures the emotions conveyed through words and expressions. For example, the prevalence of negativity in fake news could indicate a characteristic related to the truthfulness of the news. The MGT is used to determine the news's degree of negativity or positivity, with the system's output consisting of a binary element indicating a positive (1) or negative (0) emotion. The semantic analyzer then provides additional input to the BN.

## The Social Analyzer

The social analyzer module considers the following aspects related to the social dynamics that texts generate on social networks:

- The number of shares or likes related to the news. The authors of fake news aim to generate information with a very high number of shares. Under this, the BN input is described in Table 6.
- The number of comments on the news. In general, fake news arouses mixed feelings in users by generating a high number of comments; the range considered is summarized in Table 7.
- User reliability: this parameter aims to exploit the reliability of users interacting with the news. In particular, this information is summarized in a user validator module (UVM), which can be activated when needed. This module is able to monitor the history of user interaction with a news item and can suggest to the system the reliability for the different user categories identified: reliable users (R), unreliable users (UR), and unknown users (NK).

Table 6. List of classes for the number of shares or likes


Table 7. List of classes for the number of comments


The previously introduced parameters represent BN nodes that will act as a classifier. Figure 3 shows the information exploited by the classifier. The pre-elaboration through the syntactic, semantic, and social analyzer permits exploiting the BN to identify the truthfulness of news, returning a coefficient that represents the probability of fake news. In particular, each analyzer provides the aleatory variables whose values can be assumed among the ones provided previously. The syntactic analyzer provides the classifier with the following the variables:

- The number of characters, which can assume the 5 values $0-100$ characters, 100-300 characters, 300-500 characters, 500-700 characters, and more than 700 characters;
- The F-K, which can assume the values provided in Table 4;
- The GI, which can assume the values provided in Table 5.

Figure 3. BN classifier workflow
![img-2.jpeg](img-2.jpeg)

Note. Specifically, the BN classificatory takes advantage of the pre-elaboration related to the news concerning the acquired syntactic, semantic, and social features. From the acquired data, the BN learned by applying the structural learning approach classifies the news as fake or true, returning an associate probability coefficient.

The semantic analyzer provides the variables "topic," "fake news similarity," and "sentiment extraction" that can assume the values described in Section 3.2. Finally, the social analyzer provides

the variables "number of likes" and "number of comments." Furthermore, the fake news classifier can exploit the UVM described in Section 3.3.1. This module provides the additional aleatory variables R, UR, and NK that can assume the values described in Table 8.

Table 8. Labels in BN for R, UR, and NK through the UVM


# The UVM 

The users' opinions about news (Yang et al., 2019) or its propagation in social media (Wu \& Liu, 2018) represent a possible analysis to determine the news' truthfulness. This analysis's inclusion in the proposed approach requires the development of the UVM, which consists of an optional module.

The UVM aims to evaluate users through the ability to recognize fake and authentic news and define a reliability coefficient that quantifies this ability. In particular, this module aims to exploit knowledge about the type of users who come into contact with the news to improve analysis aimed at classifying real and fake news. For this purpose, the interaction between the user and the news and the interaction between the users will be exploited. These interactions make it possible to identify a reliability coefficient of the user who is seen by the system as trustworthy, untrustworthy, or unknown.

For this purpose, the UVM module exploits information from comments and shares to evaluate the behavior of users interacting with training news.

Moreover, the UVM takes advantage of

- The set of training news $N$, which has cardinality $n$
- The user set $U$, which has cardinality $m$
- The matrix $A=\left\{a_{i j}\right\}_{i, j}$ of interactions between news and users
$a_{i j}=\left\{\begin{array}{lc}1 & \text { if the usert } j \text { interacts with the news } i, \\ 0 & \text { otherwise }\end{array}, i=1, \ldots n, j=1, \ldots, m\right.$
- The tensor $B=\left\{b_{i k j}\right\}_{i, k, j}$ of interaction between users
$b_{i k j}=\left\{\begin{array}{lc}1 & \text { if the user } j \text { and the user } k \text { interact with the news } i, \\ 0 & \text { otherwise }\end{array}, i=1, \ldots, n \quad j, k=1, \ldots, m\right.$
The R's identification exploits two aspects: the ability to recognize the truthfulness of news and the number of interactions with other reliable ones. The coefficient $c_{j}$ will express the first aspect for the user $j$, and the coefficient $d_{j}$ the second one.

The ability to recognize news veracity exploits sentiment analysis, which is applied to comments and the history of shares related to specific news. The sentiment analysis information consists of the same information taken by the semantic analyzer for sentiment extraction but with a different purpose. In this module, the sentiment analysis allows for understanding the user's opinion about news and applying the social analysis through the UVM. This user feature takes advantage of formula (5), where the coefficient $c_{j}$ numerically expresses this analysis.
$c_{j}=\frac{1}{\left|\left\{i \in N: a_{i j} \neq 0\right\}\right|} \sum_{i \in N} a_{i j} \varphi(i, j), j \in U$
where $\varphi: N \times U \mapsto\{0,1\}$ is the function that returns the value 1 if the user disagrees with fake news or agrees with true news (the user recognizes the news's truthfulness); otherwise, the function returns 0 . In this way, $c_{j}$ returns the mean of news correctly labeled by the user $j$ among those with whom the user has come into contact. If the set $\left\{i \in N: a_{i j} \neq 0\right\}$ is empty, the coefficient $c_{j}$ will be equal to 0 .

In addition, the UVM also considers the typology of interaction between user $j \in U$ and news through the coefficient $d_{j}$, which expresses an estimation of the interaction between a specific user $j$ and other R. For this purpose, the values $\alpha^{(k, j)}$ evaluate the news average between the user $j$ and other users. In particular, both user $j$ and others interact with specific news and correctly judge its truthfulness. The calculus of the value $\alpha^{(k, j)}$ occurs as follows.
$\alpha^{(k, j)}=\frac{1}{\left|\left\{i \in N: b_{i k j} \neq 0\right\}\right|} \sum_{i \in N} \varphi(i, j) \varphi(i, k) b_{i k j}, k, j \in U, k \neq j$
If $\exists \bar{k} \in U$ such that $\alpha^{(\bar{k}, j)} \neq 0$, the following formula expresses the coefficient $d_{j}$.
$d_{j}=\frac{\sum_{k, k j} \alpha^{(k, j)} c_{k}}{\sum_{k, k j} \alpha^{(k, j)}}$
If, otherwise, $\nexists \bar{k} \in U$ such that $\alpha^{(\bar{k}, j)} \neq 0$, the coefficient $d_{j}$ will be equal to 0 .
In (7) the weighted mean of $c_{k}$ coefficients through the coefficients $\alpha^{(k, j)}$ is calculated. This calculus expresses the reliability of a user interacting with other R in reaction to the same news.

Finally, the reliability coefficient $r_{j}$ is obtained as in (8). This coefficient is a weighted mean between the coefficients $c_{j}$ and $d_{j}$, where the first is weighted more than the second.
$r_{j}=\frac{3}{4} c_{j}+\frac{1}{4} d_{j}, j \in U$
In this way, before the BN training phase of the reliable users set $R=\{j \in U: r \geq$ toll $\}$ can be identified. The reliability study is carried out only on users that provide a significant number of training news interactions.

Table 8 summarizes labels considered by the BN. Termed NK, as the users who do not have enough information for the reliability coefficient calculation, labels determine the percentage of R, UR, and NK who agree or disagree with the news.

If no R interact with the news, the BN considers the label "less than $50 \%$ of $R$ agree." Similarly, if no UR interact with the news, the BN processes the label "less than $50 \%$ of $U R$ disagree."Then, after identifying the coefficient $c_{j}$, associated with the analysis of the user based on their interaction with the news, and the coefficient $d_{j}$, related to the interaction between users, it is possible to process the reliability coefficient $r_{j}$, which allows identification of the correct label for the user within the

system and, therefore, integrates the analysis of the interaction with the news and between users within the processing done through semantic and syntactic analysis. Thus, the R, UR, and NK allow the exploitation of news interactions within the system and integrate the analysis of shares through the labels introduced in Table 8. Finally, the UVM improves the social analysis of the news through integration with the study of the number of shares and the number of likes.

# Learning of the BN 

Having identified the features with which the BN works, it is necessary to determine the network structure that best fits the training data. For this purpose, the multilevel graph (MuG) approach (Casillo et al., 2024), based on integrating the K2 structural learning algorithm through contextual and semantic analysis, is exploited. The graphs on which the MuG approach is based are the context dimension tree (CDT), a domain ontology, and the BN, whose structure will be learned through the data. Specifically, the CDT and ontology graphs share the parts of the nodes, which, through the ontology, are enriched through semantic relations that allow for the identification of dependence and independence between the random variables on which the BN works. In addition, the CDT's contextual analysis capability allows the data to be exploited in their application context by enhancing the semantic relationships identified through ontologies. In this way, data are filtered through the context-awareness paradigm and through a semantic analysis that enriches them through domain ontology. This analysis is functional for identifying a set of dependent and independent relations that allow the identification of a set of constraints that improve the construction of the BN through the K2 structural learning algorithm (Casillo et al., 2024).

## EXPERIMENTAL RESULTS

Analyses were conducted on datasets in the literature and on an ad hoc dataset to test the introduced approach. Data from the UNICO purpose-built dataset were collected between March 2020 and December 2020 through social media posts about the coronavirus.

The UNICO dataset contains posts related to the coronavirus and is set up for binary classification. In addition, the dataset contains information regarding users interacting with the post to exploit the full potential of the proposed approach. In this case, the dataset is unbalanced toward the class associated with fake news.

Other datasets considered include LIAR (Wang, 2017), which contains 12,836 short statements divided into training (10,240 statements), validation ( 1,284 statements), and testing ( 1,267 statements) files, and CREDBANK (Mitra \& Gilbert, 2015), which collects about 60 million tweets.

The LIAR dataset contains policy statements labeled by fact-checking and divided into six categories from which the two classes exploited for classification by the proposed approach can be extrapolated. In addition, the two classes are unbalanced as they do not have an equal number of instances in the dataset. The variety of content ranges across various political themes.

The CREDBANK dataset covers a wide range of topics and contains tweets, which are short content. In addition, the dataset is set up for binary classification, with an imbalance toward true content versus fake news.

Using these datasets, BNs were designed, and experimental results were evaluated in terms of precision, recall, and F1 score.

After this preliminary validation phase, evaluating the system's effectiveness on the UNICO dataset was possible. The dataset was obtained by collecting data from Facebook and Twitter. In particular, the following hashtags were considered: \#covid, \#covid19, \#pandemic, \#coronavirus, \#staysafe, \#stayhome, and \#socialdistancing.

The UNICO dataset contains 14,237 posts collected and tagged by 25 people, including professors, doctoral students, and students at the University of Salerno. The training phase used $75 \%$ of the posts in the dataset $(10,678)$, while $25 \%(3,559)$ were used for the validation phase. Different threshold

values were set during the training phase to evaluate the results. The threshold value that provided the best performance was 0.75 , so it was selected. This value is similar to those used by Bayesian classifier-based methods found in the state of the art (Granik \& Mesyura, 2017). The results obtained are shown in Table 9.

Table 9. Obtained results


The results obtained are promising. In particular, the system works better when analyzing longer posts focused on specific topics.

Specifically, the proposed approach succeeds in obtaining an F-score greater than or equal to 0.78 on all three datasets with dissimilar features. In addition, all three datasets exhibit an imbalance between the true and fake classes, but despite this, the proposed approach succeeds in obtaining satisfactory results.

In particular, the results obtained for Precision and Recall show that the system successfully identifies fake news with satisfactory precision for all three datasets under analysis, consistently achieving recall greater than precision. This indicates that false negatives are a manageable problem for the system, even in unbalanced datasets such as those analyzed.

Moreover, Table 10 compares the accuracy of the proposed approach with the accuracy of others described in Section 2 on the LIAR dataset. Applying the comparison method required training the methods and calibrating the parameters to obtain the accuracy results shown in Table 10.

Table 10. Comparison of methods on the LIAR dataset


FANE methodology provides better accuracy than the analyzed methods. The good accuracy result obtained implies the effectiveness of the proposed approach in hybridizing style-based approaches with the social analysis. In addition, this result confirms the effectiveness of the proposed approach, which is based on BNs. In this way, the proposed methodology is able to achieve better results in terms of accuracy. In fact, BNs allow the representation of the domain of interest to be handled compactly, ensuring rapid access to information and relationships between contextual variables.

The accuracy obtained confirms that despite the imbalance of the LIAR dataset, the proposed approach not only achieves an accuracy of $82.9 \%$ but also performs better than the comparison approaches. This result depends on the possibility of integrating a strategy that includes syntactic and semantic analysis on the one hand and, on the other hand, the possibility of exploiting structural learning techniques integrated with contextual and semantic data analysis that improve the performance of the classical algorithms.

# Experimental Results of the UVM 

This section aims to show the potential of the proposed system with the activation of the UVM. The UNICO dataset allows us to acquire information about the interaction between users and news as well as information about the connection between users and specific news. Of the 3,123 that have interacted with at least one text, only 1,012 have interacted with at least 30 texts.

These users have been labeled as R or UR through the work of the same team of experts responsible for labeling the collected posts. The UVM works on the 1,012 users to determine the reliable ones. Defining the tolerance toll $=0.70$ in order to determine the set of $R=\{j \in U: r \geq$ toll $\}$, the obtained results are shown in Table 11.

Table 11. Results obtained from the performance measurement of the UVM


Indeed, the BN is trained by including the new node linked with analyzing R, UR, and NK, as shown in Table 8 of the UVM. The obtained results are presented in Table 12.

Table 12. Comparison between the proposed approach without and with the UVM on the UNICO dataset


In this case, the system significantly improves performance, achieving $88 \%$ precision and $91 \%$ recall. This confirms, on the one hand, the system's ability to identify fake news and, on the other hand, its low false negative rate.

## CONCLUSION

This paper aims to present a methodology for recognizing fake news based on BNs. The methods described analyze in detail the semantic, syntactic, and social categories used to construct the BN structure. The results show that the proposed approach effectively identifies fake news, offering satisfactory performance and promising results.

However, as in any rapidly evolving field, there is significant room for improvement. A primary goal for the future will be to increase the number of semantic, social, and syntactic categories incorporated into the network structure. Expanding these categories could improve the system's

accuracy, allowing for deeper analysis and more accurate news classification. For example, including new variables reflecting emerging linguistic trends or new patterns of social behavior could further refine the system's ability to distinguish between real and fake news.

In addition, more attention is expected to be focused on improving the social analyzer module to refine the UVM. This improvement could be achieved by defining more detailed user profiles, allowing analysis of the similarity between users and those previously included in the BN training phase. Such an approach would strengthen the sets of trusted and untrusted users, improving the system's ability to identify fake news based not only on the news content but also on the behaviors and credibility of the users who spread it.

Another strategic goal will be developing a real-time, web-based approach to verifying the veracity of news. This would enable the system to operate more efficiently and promptly, responding quickly to new information and reducing the time needed to identify and counter the spread of fake news. Integrating these features could transform the system into an even more powerful and versatile tool, capable of adapting quickly to changes and providing support in dynamic and evolving contexts.

While the results to date are encouraging, future developments aim to make the proposed approach even more robust, flexible, and accurate. This could significantly impact the of countering the spread of fake news in an increasingly complex and interconnected media landscape.

Moreover, the proposed approach could be applied in a real-world scenario by developing an application programming interface (API) service that can permit the detector to be used as support for identifying fake news of several typologies. In addition, the proposed service should allow the BN to be trained to adapt the online phase to the specific application based on specifically collected data. This service could add value because of the role of the disinformation problem and the ethical consequences of fake news. Therefore, it will be necessary to acquire inherent data for the processing required for the proposed approach while maintaining the ability to manage the system both with and without using the UVM, which also requires a data history that is not always available.

Finally, other future developments will involve integrating the proposed approach with other machine learning strategies, specifically deep learning. On the one hand, this will make the proposed approach even more scalable and allow testing the possibility of effectively integrating the proposed approach with techniques based on neural networks to analyze additional features of fake news.

# CONFLICTS OF INTEREST 

The authors of this publication declare there are no competing interests.

## FUNDING

Princess Nourah bint Abdulrahman University Researchers Supporting Project number (PNURSP2024R 343), Princess Nourah bint Abdulrahman University, Riyadh, Saudi Arabia. Also, the authors extend their appreciation to the Deanship of Scientific Research at Northern Border University, Arar, KSA for funding this research work through the project number NBU-FFR-2024-1092-16.

## PROCESS DATES

October 28, 2024
Received: September 3, 2024, Revision: October 4, 2024, Accepted: October 4, 2024

## CORRESPONDING AUTHOR

Correspondence should be addressed to Domenico Santaniello (Italy, dsantaniello@unisa.it)
