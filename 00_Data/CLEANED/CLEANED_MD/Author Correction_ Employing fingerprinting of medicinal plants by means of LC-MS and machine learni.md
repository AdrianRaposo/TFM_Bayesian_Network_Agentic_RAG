# SCIENTIFIC REPORTS 

natureresearch

## OPEN

## Author Correction: Employing fingerprinting of medicinal plants by means of LC-MS and machine learning for species identification task

Pavel Kharyuk, Dmitry Nazarenko, Ivan Oseledets, Igor Rodin, Oleg Shpigun, Andrey Tsitsilin \& Mikhail Lavrentyev (D)<br>Correction to: Scientific Reports https://doi.org/10.1038/s41598-018-35399-z, published online 19 November 2018

This Article contained errors.
Following the publication of this Article, the authors discovered unintentional train-test leakage in the machine learning experiment. This was caused by the authors not taking into account highly correlated LC-MS repletions of individual physical samples. This is now corrected.

In the abstract:
"Even with elimination of all retention time values accuracies of up to $96 \%$ and $92 \%$ were achieved on validation set for plant species and plant organ identification respectively."
now reads:
"Even with elimination of all retention time values accuracies of up to around $85 \%$ were achieved on validation set for plant species and plant organ identification."

In the Results:
"Encoded data vectors with 25 variables were used to train logistic regression and continuous Bayes classifiers (bothNaive Bayes and hybrid BayesianNetwork) with resulting identification accuracy of $96 \%$ and $84-87 \%$ on Test 1 respectively. All abovementioned models showed accuracy of $68-77 \%$ on Test 2."
now reads:
"Encoded data vectors with 25 variables were used to train logistic regression and continuous Bayes classifiers (both Naive Bayes and hybrid Bayesian Network) with resulting identification accuracy of $85 \%$ and $68-69 \%$ on Test 1 respectively. All of the above mentioned models showed accuracy of $68-75 \%$ on Test 2."
"According to the Table 1 Part 1, classifier based on Tucker decomposition with principal angle distance measure performs well ( $93 \%$ and $86 \%$ respectively for Test 1 and Test 2 )."
now reads:
"According to the Table Table 1 Part 1 Part 1, classifier based on Tucker decomposition with principal angle distance measure performs well ( $78 \%$ and $84 \%$ respectively for Test 1 and Test 2 )."

![img-0.jpeg](img-0.jpeg)

Figure 1.
![img-1.jpeg](img-1.jpeg)

Figure 2.

# In the Discussion: 

"The most obvious increase was shown by BN on Test 2, where emergence of correct labels in Top5 jumped by more than $20 \%$ compared to "winner takes all" approach. Although exact accuracy values may drop when using larger and more diverse datasets, this shows great potential of discrete BNs in such applications. All in all, TopN representation can be considered a more preferable way of output - narrowing possible candidates to $3-5$ with $95 \%$ or more accuracy can be more beneficial than $80 \%$ accurate single candidate species."
now reads:
"The most obvious increase was shown by bayesian networks on Test 2, where emergence of correct labels in Top5 jumped by around $20 \%$ compared to "winner takes all" approach. Although exact accuracy values may drop when using larger and more diverse datasets, this shows great potential of BNs in such applications. All in all, TopN representation can be considered a more preferable way of output - narrowing possible candidates to 3-5 with $90 \%$ accuracy can be more beneficial than $75 \%$ accurate single candidate species."
"Algorithms showed high distinguishing ability between most classes (up to $92 \%$ accuracy), excluding very similar pair of classes (roots, roots and rhizomes)."
now reads:
"Algorithms showed high distinguishing ability between most classes (up to $86 \%$ accuracy), excluding very similar pair of classes (roots, roots and rhizomes)."

Additionally, as a result of these errors, Figures 2, 6, Table 1 and the Supplementary Figure file S1 have been corrected in the original HTML and PDF of this Article. The original versions of Figures 2, 6 and Table 1 are reproduced below as Figure 1, Figure 2 and Table 1 respectively. The original version of Supplementary Figure 1 is included as a Supplementary File in this notice.

These errors have now been corrected in the PDF and HTML versions of the Article, and in the accompanying Supplementary Information file.


Table 1. Comparative characteristics of implemented approaches. Test 2 is independent from Train/Test 1 parts. In Part 1 and Part 3 all values presented are medians across 5-times repeated 5-fold cross validation runs. In Part 2 the same partitioning was used but final results were computed as top-N's (see Supplementary S1.2).

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41598-020-67201-4. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/. (c) The Author(s) 2020