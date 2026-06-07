# Preface: Special Issue on Advanced Methodologies for Bayesian Networks 

Maomi Ueno ${ }^{1}$

Published online: 21 December 2016
(c) Ohmsha, Ltd. and Springer Japan 2016


#### Abstract

The second AMBN was held in Yokohama, Japan on November 16-18, 2015, co-sponsored by the Japanese Society Artificial Intelligence (JSAI) and the National Institute of Advanced Industrial Science and Technology (AIST).The AMBN workshop had over 100 participants and many lively and interesting discussions over the course of its duration. This special issue of New Generation Computing (NGC) has come out from these extensive activities of the researchers in BNs field.After the workshop, six excellent papers in the conference were recommended to submit to this special issue with the requirement at least $30 \%$ extension from the Post Proceeding of AMBN2015 (LNAI, Springer) version. Each paper was reviewed by one meta-reviewer and two reviewers. As a result, all the six papers were accepted for publication in this journal.


Keywords Artificial intelligence $\cdot$ Machine learning $\cdot$ Probabilistic graphical model $\cdot$ Bayesian networks

Over the last few decades, Bayesian networks (BNs) have become an increasingly popular AI approach for treating uncertainty around random variables.

The International Workshop on Advanced Methodologies for Bayesian Networks (AMBN 2010) was held on November 18-19, 2010, at the Campus Innovation Center in Tokyo, Japan [1, 2].

In AMBN 2010, we concentrated on exploring methodologies for enhancing the effectiveness of BNs, including modeling, reasoning, model selection, logicprobability relations, and causality.

[^0]
[^0]:    $\boxtimes$ Maomi Ueno
    ueno@ai.is.uec.ac.jp
    1 University of Electro-Communications, 1-5-1, Chofugaoka, Chofu-shi, Tokyo 182-8585, Japan

The second AMBN was held in Yokohama, Japan on November 16-18, 2015, cosponsored by the Japanese Society Artificial Intelligence (JSAI) and the National Institute of Advanced Industrial Science and Technology (AIST) [3, 4].

In AMBN 2015, in addition to exploring advanced methodologies of BNs, we discussed practical considerations for applying BNs in real-world settings, covering concerns such as scalability, incremental learning, and parallelization.

In spite of the short announcement period, 29 papers were submitted, and only 15 papers were accepted in the AMBN proceedings, which was published in the Lecture Notes in Artificial Intelligence series by Springer. Each submission underwent rigorous by three members of the AMBN Program Committee, with each PC member reviewing at most two papers.

The members of Program Committee (PC) are leading researchers in BNs field:

- Chair Joe Suzuki (Osaka University, Japan)
- Chair Maomi Ueno (University of Electro-Communications)
- Russell Almond (Florida State University, USA)
- Alessandro Antonucci (IDSIA, Switzerland)
- Cassio P. de Campos (Queens University, UK)
- Hei Chan (The Institute of Statistical Mathematics, Japan)
- Arthur Choi (UCLA, UCLA)
- Adnan Darwiche (UCLA, USA)
- Robin Evans (University of Oxford, UK)
- Luca Faes (University of Trento, Italy)
- David Heckerman (Microsoft, USA)
- Antti Hyttinen (University of Helsinki, Finland)
- Aapo Hyvarinen (University of Helsinki, Finland)
- Seiya Imoto (University of Tokyo, Japan)
- Yoshinobu Kawahara (Osaka university, Japan)
- Manabu Kuroki (The Institute of Statistical Mathematics, Japan)
- Jose A. Lozano (University of the Basque Country UPV/EHU, Spain)
- Peter Lucas (Institute for Computing and Information Sciences, The Netherlands)
- Brandon Malone (Max Planck Institute, Germany)
- Alessio Moneta (Scuola Superiore Sant'Anna, Italy)
- Yoichi Motomura (National Institute of Advanced Industrial Science and Technology, Japan)
- Petri Myllmaki (University of Helsinki, Finland)
- Judea Pearl (UCLA, USA)
- Jose M. Pena (Linkoping University)
- Hiroshi Sakamoto (Kyuushu Institute of Technology, Japan)
- Shohei Shimizu (Osaka university, Japan)
- Peter Spirtes (CMU, USA)
- Milan Studeny (Institute of Information Theory and Automation, Czech Republic)
- Yi Wang (Institute of High Performance Computing, Singapore)
- Takashi Washio (Osaka University, Japan)

- Changhe Yuan (Queens College/CUNY, USA)
- Jiji Zhang (Lingnan University, Hong Kong)
- Kun Zhang (University of Southern California, USA)

The AMBN workshop had over 100 participants and many lively and interesting discussions over the course of its duration. This special issue of New Generation Computing (NGC) has come out from these extensive activities of the researchers in BNs field.

After the workshop, six excellent papers in the conference were recommended to submit to this special issue with the requirement at least $30 \%$ extension from the Post Proceeding of AMBN2015 (LNAI, Springer) version.

Each paper was reviewed by one meta-reviewer and two reviewers. As a result, all the six papers were accepted for publication in this journal.

The first paper titled as "On Model Selection, Bayesian Networks, and the Fisher Information Integral" provides a very fundamental analysis of model selection for Bayesian networks from information theoretical approach. This paper addresses Bayesian Information Criterion (BIC) model selection that includes a constant term involving the Fisher information matrix. They find that, for complex Bayesian network models, the constant term is a negative number with a very large absolute value that dominates the other terms for small and moderate sample sizes. For networks with a fixed number of parameters, their experiments show that the constant term can vary significantly depending on the network structure. In particular, star-like networks have smaller complexity than networks where the node degree is more uniform.

The second paper titled as "Learning Causal Graphs with Latent Confounder Information in Faithfulness Violations" addressed a fundamental and important analyses for causal graphs with latent common causes. Ancestral graph models are effective and useful for representing causal models with some information of such latent variables. The causal faithfulness condition, which is usually assumed for determining the models, is known to often be weakly violated in statistical view points for finite data. One of the authors developed a constraint-based causal learning algorithm that is robust against the weak violations while assuming no latent variables. In this study, we applied and extended the thoughts of the algorithm to the inference of ancestral graph models. The practical validity and effectiveness of the algorithm are also confirmed using some standard datasets in comparison with the other traditional methods.

The third paper titled as "Duplicate Detection for Bayesian Network Structure Learning" presents a new duplicate detection technique for Breadth-first branch and bound in score-based Bayesian network structure learning problem. Previously, an external sorting-based technique was used for delayed duplicate detection (DDD). They propose a hashing-based technique for DDD and a bin packing algorithm for minimizing the number of external memory files and operations. They also give a structured duplicate detection approach which completely eliminates DDD. Empirically, they demonstrate that structured duplicate detection is significantly faster than the previous state of the art in limited-memory settings. Their results

show that the bin packing algorithm incurs some overhead, but that the overhead is offset by reducing I/O when more memory is available.

The fourth paper titled as "Joint Analysis of Multiple Algorithms and Performance Measures" develops statistical procedures that are able to account for multiple competing measures at the same time and to compare multiple algorithms altogether. In particular, they propose two tests: a frequentist procedure based on the generalized likelihood-ratio test and a Bayesian procedure based on a multinomial-Dirichlet conjugate model. They further extend them by discovering conditional independences among measures to reduce the number of parameters of such models, as usually the number of studied cases is very reduced in such comparisons. Real data from a comparison among general purpose classifiers is used to show a practical application of their tests.

The fifth paper titled "Improving Record Linkage Accuracy with Hierarchical Feature Level Information and Parsed Data" addresses probabilistic record linkage with hierarchical feature level information. This study extends the naive Bayes classifier with such hierarchical feature level information. Moreover, they illustrate the benefits of their method over previously proposed methods on 4 datasets in terms of the linkage performance. The results show an improved performance of the methods considered on further parsed datasets

The sixth paper titled "Efficient Bayesian Network Structure Learning for Maximizing the Posterior Probability" addresses the problem of efficiently finding an optimal Bayesian network structure for maximizing the posterior probability using a Branch and Bound (B \& B) technique. To make the search more efficient, B \& B technique needs a tighter upper bound so that the current score can exceed it more easily. This paper proposes two upper bounds and prove that they are tighter than the existing one. Moreover, this paper demonstrate that the proposed two bounds render the search to be much more efficient using the Alarm and other major data sets. For example, the search is three to four times faster for $n=100$ and two to three times faster for $n=500$.

We would like to thank all of the authors and the reviewers of the published papers. We also thank for the support of the Editorial board of NGC, the Editorial Office.

Maomi Ueno, Guest Editor
