# Predicting Gene Function From Patterns of Annotation 

Oliver D. King, ${ }^{1}$ Rebecca E. Foulger, ${ }^{2}$ Selina S. Dwight, ${ }^{3}$ James V. White, ${ }^{4,5}$ and Frederick P. Roth ${ }^{1,6}$<br>${ }^{1}$ Department of Biological Chemistry and Molecular Pharmacology, Harvard Medical School, Boston, Massachusetts 02115, USA; ${ }^{2}$ FlyBase, Department of Genetics, University of Cambridge, Cambridge, CB2 3EH, England; ${ }^{3}$ Department of Genetics, Stanford University School of Medicine, Stanford, California 94305-5120, USA; ${ }^{4}$ JVWhite.Com, Cambridge, Massachusetts 02139, USA; ${ }^{5}$ Department of Biomedical Engineering, Boston University, Boston, Massachusetts 02215, USA


#### Abstract

The Gene Ontology (GO) Consortium has produced a controlled vocabulary for annotation of gene function that is used in many organism-specific gene annotation databases. This allows the prediction of gene function based on patterns of annotation. For example, if annotations for two attributes tend to occur together in a database, then a gene holding one attribute is likely to hold the other as well. We modeled the relationships among GO attributes with decision trees and Bayesian networks, using the annotations in the Saccharomyces Genome Database (SGD) and in FlyBase as training data. We tested the models using cross-validation, and we manually assessed 100 gene-attribute associations that were predicted by the models but that were not present in the SGD or FlyBase databases. Of the 100 manually assessed associations, 41 were judged to be true, and another 42 were judged to be plausible.


[Detailed lists of hypotheses including the curators' comments on each hypothesis, are available at http:// llama.med.harvard.edu/ king/ predictions.html.]

The Gene Ontology Consortium (Gene Ontology Consortium 2000) provides a standardized vocabulary for the annotation of gene attributes, which fall into the three general categories of molecular function, biological process, and cellular component. Organism-specific databases such as FlyBase (FlyBase Consortium 2002), Saccharomyces Genome Database (SGD; Cherry et al. 1998), Mouse Genome Database (MGD; Blake et al. 2002), and WormBase (Stein et al. 2001), have codeveloped this vocabulary, and have used it to annotate genes with the attributes that the biomedical literature asserts that they hold.

These databases are incomplete because there are genes whose attributes are not yet all known, and because there is literature that has not yet been digested by the database curators. In such cases it is useful to have a prediction of whether a gene has a certain attribute. Such predictions can help to make the databases more complete (and consequently more useful to researchers) by directing curators toward literature that they may have overlooked. Also, predictions that are not presently supported by the literature provide new hypotheses that may be tested experimentally.

A variety of approaches for predicting Gene Ontology (GO) attributes have been attempted. Natural language processing was used in Raychaudhuri et al. (2002) to automate the curator's task of extracting gene-attribute associations from literature abstracts. Others have assigned attributes to genes on the basis of microarray data (Hvidsten et al. 2001) or protein folds (Schug et al. 2002). These approaches are especially valuable for assigning attributes to genes with otherwise

[^0]unknown function. But once some attributes of a gene are known, statistical patterns among the annotations themselves can be useful for predicting additional attributes. In this paper, we model the probabilistic relationships between the GO annotations using two approaches, one based on decision trees and the other based on Bayesian networks. We assess the models using cross-validation on the SGD and FlyBase databases. We also manually assess 100 of those gene-attribute associations that the models indicate are likely to hold but that have not been annotated in the databases.

## RESULTS

We downloaded the files containing the three branches of the Gene Ontology (GO) and the lists of SGD and FlyBase annotations from http://www.geneontology.org. These files are updated frequently; the versions we used are from January 22, 2002. From these, we constructed a matrix $Z$ for each organism, where $Z(i, j)=1$ if gene $i$ is associated with attribute $j$ in the database and $Z(i, j)=0$ otherwise. The set of attributes listed in the GO is organized as a directed acyclic graph (DAG)-this is like a hierarchy in which GO terms are subdivided into increasingly detailed or specific child terms; it differs from a hierarchy in that terms may have multiple parents, not just multiple children. An edge from attribute $j$ to attribute $k$ means that $k$ is an instance of attribute $j$ or a component of attribute $j$, so that any gene associated with attribute $k$ is also associated with attribute $j$.

The gene association files usually contain explicit annotations only at the most detailed levels that are supported by the literature, but in constructing $Z$ we also include those associations logically implied by the GO DAG. Thus, $Z(i, j)=1$ if gene $i$ is explicitly annotated as having attribute $j$ or any of the descendants of attribute $j$ in the GO DAG. We excluded


[^0]:    ${ }^{6}$ Corresponding author.
    E-MAIL froth@hms.Harvard.edu; FAX (617) 432-3557.
    Article and publication are at http://www.genome.org/cgi/doi/10.1101/ gr. 440803 . Article published online before print in April 2003.

annotations for the three attributes "biological process unknown," "molecular function unknown," and "cellular component unknown," although in principle these are semantically different from the lack of any annotations, because they indicate that someone has looked (Gene Ontology Annotation Guide; http://www.geneontology.org/doc/GO. annotation.html).

There are roughly 13,000 attributes in the GO DAG, but for any given organism only a subset $A_{1}$ of them is used. We further restricted our attention to the subset $A_{10}$ of those attributes that at least 10 genes were annotated as holding, because the probabilistic relationships between these attributes might be estimated with greater confidence. The approach taken in this paper is to use some of the attributes in $A_{10}$ to predict other attributes in $A_{10}$.

Let $X_{j}$ be an indicator random variable for the attribute $j \in A_{10}$, with $X_{j}(i)=1$ if gene $i$ is annotated as having $j$ and $X_{j}(i)=0$ otherwise. [Note that $X_{j}(i)=Z(i, j)$.] Let $\mathbf{n a d}\left(X_{i}\right)$ denote the vector consisting of all those random variables $X_{k} \in A_{10}$ for which $k \neq j$ and $k$ is neither an ancestor nor a descendant of $j$ in the GO DAG; and let $\mathbf{n a d}\left(X_{j}\right)(i)$ denote the vector of the values of these random variables for the gene $i$.

We used standard machine learning techniques (described in the Methods section) to construct, for each attribute $j$, models $M_{D T}$ (using decision trees) and $M_{B N}$ (using Bayesian networks) for the probability that a gene $i$ is annotated as having attribute $j$, given knowledge of the other attributes that gene $i$ is annotated as holding, excluding attributes that are ancestors or descendants of attribute $j$ in the GO DAG. That is, we constructed models $M_{D T}$ and $M_{B N}$ for $\operatorname{Pr}\left(X_{j} \mid \mathbf{n a d}\left(X_{j}\right)\right)$, which we use for making predictions. (The motivation for ignoring ancestors and descendants when making predictions is discussed in the Manual Assessment section below.) Our approach may be viewed as a supervisedlearning approach to pattern recognition, in contrast to unsupervised methods such as clustering; other supervised approaches that might be fruitful, but which we have not evaluated, include support vector machines and artificial neural networks.

## Cross-Validation

We assessed our models using 10-fold cross-validation on the SGD and FlyBase databases. This was done separately for the two organisms, and in what follows we use ORG to refer to a generic organism, either fly or yeast. First, from among the set $A_{10}$ of attributes with at least 10 associated ORG genes, we selected a subset $T$ of the most specific attributes in $A_{10}$ to be used for the assessment. (See the Methods section for the precise selection criteria.) Then the set $G$ of genes for ORG was randomly partitioned into 10 sets of equal size $( \pm 1)$. For each of the 10 sets of genes, we built models $M_{D T}$ and $M_{B N}$ using the remaining nine sets (combined together) as training data. Then for each gene $i$ in the held-out set, we used these models to compute

$$
q(i, j)=\operatorname{Pr}\left(X_{j}=1 \mid \mathbf{n a d}\left(X_{j}\right)=\mathbf{n a d}\left(X_{j}\right)(i)\right)
$$

for each test attribute $j$ in $T$. (The score $q(i, j)$ may be interpreted as the probability that a gene is annotated with attribute $j$, given that its other annotations, ignoring those for attribute $j$ and its ancestors and descendants in the GO DAG, agree with those for gene $i$.)

The scores $q(i, j)$ for each of the 10 folds of the crossvalidation were pooled together, and for each threshold $t \in[0,1]$ we computed the true-positive rate

$$
T P_{t}=\frac{\#\left[(i, j) \in G \times T: q(i, j) \geq t \& Z(i, j)=1\right]}{\#\left[(i, j) \in G \times T: Z(i, j)=1\right]}
$$

and the false-positive rate

$$
F P_{t}=\frac{\#\left[(i, j) \in G \times T: q(i, j) \geq t \& Z(i, j)=0\right]}{\#\left[(i, j) \in G \times T: Z(i, j)=0\right]}
$$

Figure 1 shows Receiver Operating Characteristic (ROC) curves, plotting $T P_{t}$ versus $F P_{t}$, for models $M_{D T}$ and $M_{B N}$. For comparison, we have also included the ROC curve for a model $M_{D G}$, in which attributes are treated as independent, so that $q(i, j)$ is just the fraction of the genes in the training set that are annotated as having attribute $j$.

There were 6403 genes listed in the SGD association file, and there were 634 attributes that were associated with at least 10 of the genes; 170 of these attributes were in our test set $T$. Thus there were a total of $6403 \times 170=1,088,510$ examples $(i, j)$ in the set $G \times T$. Of these, 4250 were positive (i.e., had $Z(i, j)=1$ ), and the remaining $1,084,260$ were negative. At the point on the ROC curves where the true-positive rate is 0.5 (i.e., where 2125 of the 4250 positive examples are correctly classified as such), 51 of the negative examples were misclassified by $M_{D T}, 143$ by $M_{B N}$, and 261,003 by $M_{D G}$.

There were 7039 genes listed in the FlyBase association file, and there were 794 attributes that were associated with at least 10 of the genes; 218 of these attributes were in our test set $T$. We included in $G$ another 6461 genes with no annotations, to bring the total number of genes in $G$ to 13,500, an estimate for the total number of Drosophila genes (FlyBase Consortium 2002). Thus, there were a total of $13,500 \times 218=2,943,000$ examples $(i, j)$ in the set $G \times T$. Of these, 5360 were positive and the remaining 2,937,640 were negative. At the point on the ROC curves where the truepositive rate is 0.5 (i.e., where 2680 of the 5360 positive examples are correctly classified as such), 382 of the negative examples were misclassified by $M_{D T}, 684$ by $M_{B N}$, and 602,178 by $M_{D G}$.

## Manual Assessment

Although the cross-validation performed above demonstrates that GO annotations may often be predicted accurately on the basis of other annotations, this would be of little use if the organism-specific databases were already saturated, that is, if every genuine gene-attribute association were already annotated. But the databases as they stand now almost certainly contain both errors of inclusion (instances where $Z(i, j)=1$ although gene $i$ does not in fact have attribute $j$ ), and errors of omission (instances where $Z(i, j)=0$ although gene $i$ really does have attribute $j$ ). The GO does in fact define a NOT flag for "negative evidence"-evidence that a gene does not hold an attribute-but in the association files from January 22, 2002, the NOT flag was not used at all in the SGD, and only about 30 times in FlyBase.

Because of the large-scale uncertainty about the truth, we have not attempted to explicitly model the truth of whether a gene has an attribute, but have contented ourselves with modeling the patterns among the annotations themselves. Nonetheless, those gene-attribute pairs $(i, j)$ for which

![img-0.jpeg](img-0.jpeg)

Figure 1 ROC curves for SGD (above) and FlyBase (below), using models $M_{D T}, M_{B N}$, and $M_{I N D}$. On the left are the entire ROC curves, and on the right are details of the ROC curves at low false-positive rates, with the axes rescaled. (Note that in the graphs on the right, the curves for $M_{I N D}$ are not missing; they are just very close to the horizontal axis.)
$Z(i, j)=0$ and $q(i, j)$ is large should be good candidates for errors of omission.

This approach is formally quite similar to approaches used for preference prediction in collaborative filtering (see, e.g., Breese et al. 1998). In a typical application, a model built from a database of customer purchases is used to predict whether customer $i$ would like product $j$ (which he has not purchased), based on the probability that a customer with the same pattern of purchases as customer $i$ (aside from product $j$ ) has purchased product $j$. If this probability is high, a targeted advertisement for product $j$ could be shown to customer $i$.

We are doing something analogous, with genes playing the role of customers, GO attributes playing the role of products, and annotations playing the role of purchases. Annotations are used as an imperfect proxy for true gene-attribute associations, just as purchases are used as an imperfect proxy for true customer preferences.

Consumer products do not generally have an analog of the GO DAG, however. Our motivation for not considering ancestors or descendants of an attribute $j$ in the GO DAG when predicting attribute $j$ is this: If there is an error of omission for gene $i$ having attribute $j$, then because of the way annotations are logically propagated up the GO DAG, there are likely to also be errors of omission for gene $i$ having other attributes that are ancestors or descendants of $j$. Because these attributes can be misleading when we are trying to predict
whether $Z(i, j)=0$ represents an error of omission, we ignore them.

To test this approach, in the process of doing the crossvalidation we also compiled for each organism a list of the 50 gene-attribute pairs $(i, j) \in G \times T$ that had the highest scores $q(i, j)$, among just those pairs with $Z(i, j)=0$. (We used the $q$ scores from $M_{D T}$, because judging from the ROC curves it outperformed $M_{B N}$ at low false-positive rates.) Each list may be thought of as containing 50 hypotheses of the form "gene $i$ is associated with attribute $j$."

A FlyBase curator (R.E.F.) assessed the 50 hypotheses for fly, and an SGD curator (S.S.D.) assessed the 50 hypotheses for yeast. The curators gave each hypothesis a rating of 1,2 , or 3 , with a rating of 1 meaning that the hypothesis is "known to be true" (despite not being listed in the organism-specific database), 2 meaning "known to be false," and 3 meaning "neither of the above." The lists of hypotheses, along with the curators' ratings, are given in Tables 1 and 2. In these tables, and elsewhere in this paper, we prefix the names of GO attributes from the biological process branch with " P ," from the cellular component branch with "C," and from the molecular function branch with "F." More detailed lists, which include the curators' comments on each hypothesis, are available at http://llama.med.harvard.edu/ king/predictions. html. Below we summarize the number of hypotheses that received each rating.


These results indicate that our success rate was between $44 \%$ and $90 \%$ for the 50 FlyBase hypotheses, and between $38 \%$ and $76 \%$ for the 50 SGD hypotheses.

## DISCUSSION

## ROC Analysis

For a perfect classifier, there would be a threshold $t$ for which $T P_{t}=1$ and $F P_{t}=0$. The ROC curve for such a classifier would climb up the line $F P=0$ until it reached this point, and would then follow the line $T P=1$ until it reached the point with $T P=1$ and $F P=1$.

For a method that assigns scores $q(i, j)$ completely at random, the expected ROC curve would be a diagonal line from the point with $F P=0$ and $T P=0$ to the point with $F P=1$ and $T P=1$. (The model $M_{D S D}$ performs better than this because it assigns higher $q$ scores for more commonly occurring attributes.)

It is not possible to perfectly predict whether a gene $i$ is annotated as having attribute $j$ solely on the basis of the other annotations held by gene $i$, because there are often many genes that have exactly the same combination of annotations aside from $j$, some of which are also annotated as having attribute $j$ and some of which are not. For example, nearly half the genes in the SGD have no annotations whatsoever, once those for "biological process unknown," "molecular function unknown," and "cellular component unknown" are removed; another one-sixth of the genes have exactly one explicit annotation (together with the annotations implied by this via the GO DAG). These annotations are difficult to predict: suppose a gene's only explicit annotation is for attribute $j$. Then when trying to predict whether gene $i$ has attribute $j$ without looking at $j$ or its ancestors or descendants in the GO DAG, the gene looks exactly like the 3000 or so genes that have no annotations whatsoever, so the score $q(i, j)$ is low.

Of the 4250 SGD gene-attribute pairs $(i, j) \in G \times T$ for which $Z(i, j)=1,315$ were such that gene $i$ had no annotations among the attributes in $\mathbf{n a d}\left(X_{j}\right)$. This explains why the slope of the ROC curves for SGD (using models $M_{D T}$ and $M_{R N}$ ) decrease sharply before a true-positive rate of $93 \%$ is reached. Similar reasoning explains why the slopes of the ROC curves for FlyBase decrease sharply before a true-positive rate of $78 \%$ is reached. (The ROC curves obtained by computing $q(i, j)$ only when gene $i$ has at least one annotation for an attribute in $\mathbf{n a d}\left(X_{j}\right)$ are available at http://llama.med.harvard.edu/ king/ predictions.html.)

Note that for both FlyBase and SGD, $M_{D T}$ outperforms $M_{R N}$ at low false-positive rates, but eventually $M_{R N}$ gains the advantage. The crossover point for SGD is at a false-positive rate of $\sim 0.02$ (corresponding to $\sim 20,000$ false positives), and the crossover point for FlyBase is at a false-positive rate of $\sim 0.05$ (corresponding to $\sim 150,000$ false positives).

## Discussion of Manual Assessment

In assessing our hypotheses, the GO curators availed themselves of all information at their disposal, including the other GO annotations for the genes, annotations for homologous

Table 1. Top 50 Hypotheses for FlyBase Using Model $M_{D T}$, Sorted Alphabetically by GO Attribute


The first column gives the curator's rating of each hypothesis, with 1 meaning "known to be true," 2 meaning "known to be false," and 3 meaning "neither of the above."
genes in other organisms, FlyBase and SGD internal notes, data from InterPro (Apweiler et al. 2000), and relevant papers.

Below we give examples of FlyBase hypotheses that were rated 1,2 , and 3 , along with the curator's rationale for assigning these ratings.

Table 2. Top 50 Hypotheses for SGD Using Model $M_{\text {trs }}$, Sorted Alphabetically by GO Attribute


The first column gives the curator's rating of each hypothesis, with 1 meaning "known to be true," 2 meaning "known to be false," and 3 meaning "neither of the above."

1. Known to be true: The hypothesis that the gene with FlyBase accession ID CG1909 has the GO attribute "C-nicotinic acetylcholine-gated receptor-channel." The gene CG1909 is annotated as having the function "F-nicotinic acetylcholine receptor-associated protein," from which the hypothesized cellular component association follows.
2. Known to be false: The hypothesis that the gene $h s f$ has the GO attribute "F-heat shock protein." The gene $h s f$ is a tran-
scriptional activator of heat-shock genes. Heat-shock factors are transcription factors that act on the genes that encode heat-shock proteins, but are not chaperones and thus are not themselves heat-shock proteins.
3. Neither of the above: The hypothesis that the gene CG1193 has the GO attribute "P-microtubule-based movement." CG1193 encodes katanin, a microtubule-severing protein. Although it is possible that it is involved in microtubule transport, there is no definite evidence for this.

In many cases, evaluating these hypotheses led the curators to literature or data sufficient to justify adding the annotation to FlyBase or SGD. This is sometimes attributable to the decision of the GO Consortium to model the three branches of the ontology independently. A consequence of this is that the GO DAG has no edges that connect attributes in different branches. Nonetheless, there are cases in which an attribute in one branch (e.g., molecular function) implies an attribute in another branch (e.g., biological process; Gene Ontology Consortium 2001). Because these interbranch logical relations are not codified in the GO DAG, it is incumbent on the curators to maintain consistency between the branches. If the curators are for the most part successful in this, then these relations (and other probabilistic relations within and between the branches) can be learned by our models, and our models can then flag the isolated instances in which annotations were overlooked. Thus, one immediate application of our methods is the improvement of the gene annotation databases. Aside from a few unusual cases, such as predictions that were for GO attributes that are now obsolete, those predictions rated "known to be true" will be added to FlyBase or SGD.

Another application we envision is that a researcher querying a database for genes with some attribute or combination of attributes may like to supplement the list of perfect matches (of which there may be few or none) with genes that are predicted to hold the attributes. This may be helpful in allocating experimental resources. For each hypothesis we evaluated, $<2 \%$ of the genes were annotated as having the hypothesized attribute (usually $<0.5 \%$ ), so blindly fishing around for genes that hold these attributes is likely to be unproductive; but $>40 \%$ of our predictions were judged to be true. The success rate is perhaps much higher, because we do not know whether the hypotheses rated 3 are true or not. The hypotheses rated 3 are perhaps even more

1. Known to be true: The hypothesis that the gene with FlyBase accession ID CG1909 has the GO attribute "C-nicotinic acetylcholine-gated receptor-channel." The gene CG1909 is annotated as having the function "F-nicotinic acetylcholine receptor-associated protein," from which the hypothesized cellular component association follows.
2. Known to be false: The hypothesis that the gene $h s f$ has the GO attribute "F-heat shock protein." The gene $h s f$ is a tran-
interesting than those rated 1, because they may reflect associations that are true but presently unknown, rather than associations that are known but absent from the databases.

In principle, the techniques we used for predicting errors of omission in the databases may also be used to predict possible errors of inclusion, by flagging those existing annotations that have abnormally low $q$ scores. This may be more difficult than predicting errors of omission, however, because

the general sparsity of the databases causes many legitimate annotations to have $q$ scores $<0.01$. We examined 12 of the existing FlyBase annotations that had the lowest $q$ scores, but none appeared to be erroneous. (Here we were looking for errors such as annotations using GO terms not supported by assertions in the literature, rather than errors in the literature itself, which would be harder to assess.)

## METHODS

## Selection of the Test Attributes

We wanted to assess our predictions on test attributes that were reasonably specific, because a prediction that a gene is associated with a general attribute such as "biological process" is rather uninteresting. We also wanted the test attributes to have no GO edges between them, because using logically dependent test attributes could have the effect of rewarding a single good prediction, or penalizing a single bad prediction, multiple times. With these criteria in mind, we chose the set of test attributes $T$ to consist of all the attributes in $A_{10}$ that had no descendants in $A_{10}$, with the additional technical requirement that no attributes $j \in T$ and $k \in A_{10}$ may have any common descendant $l \in A_{1}$, unless $k$ is an ancestor of $j$. The idea is that, if gene $i$ has attribute $j$, we should not be allowed to use any direct evidence for this when predicting whether gene $i$ has attribute $j$ during cross-validation. Because we make predictions just on the basis of the random variables in $\mathbf{n a d}\left(X_{j}\right)$, this is usually not a problem, but sometimes more care is needed because of multiple parentage in the GO DAG. By removing from $T$ any attribute $j$ that violated the technical requirement above, we ensured that no residue of an annotation for an attribute $l$ ever appeared as an annotation for $k \in \mathbf{n a d}\left(X_{j}\right)$ when making a prediction for attribute $j$.

## Decision Trees

See Breiman et al. (1984) or Quinlan (1993) for an overview of decision trees and their applications. For our purposes, the decision tree for attribute $j$ prescribes a sequence of tests to apply to a gene to aid in predicting whether the gene is annotated as having attribute $j$. The tests are all of the form, "Is the gene annotated as having attribute $k$ ?" for some $k \in j$, with $k \in A_{10}$ being neither an ancestor nor a descendant of $j$ in the GO DAG. Which test is applied depends on the result of previous tests-hence the tree structure. (Note that we are using our decision tree to model the conditional probability distribution of $X_{j}$ given $\operatorname{nad}\left(X_{j}\right)$, not just to classify genes as having attribute $j$ or not; some authors use the name "probabilistic decision trees" for trees such as ours.)

We constructed the decision tree for attribute $j$ greedily, by starting with all genes $g$ in the training set in a single root node, and then recursively splitting each node $\boldsymbol{N}$ by testing on the attribute $k$ for which the information gain for attribute $j$ is maximal.

If we test on attribute $k$, splitting $\boldsymbol{N}$ into $\boldsymbol{N}_{0}$ and $\boldsymbol{N}_{1}$, where $\boldsymbol{N}_{i}=\left\{g \in \boldsymbol{N}: X_{k}(g)=t\right\}$, then the information gain is defined to be

$$
H_{\boldsymbol{N}}\left(X_{j}\right)-\operatorname{Pr}\left(g \in \boldsymbol{N}_{0} \mid g \in \boldsymbol{N}\right) H_{\boldsymbol{N}_{0}}\left(X_{j}\right)-\operatorname{Pr}\left(g \in \boldsymbol{N}_{1} \mid g \in \boldsymbol{N}\right) H_{\boldsymbol{N}_{1}}\left(X_{j}\right)
$$

Here $H_{\boldsymbol{N}}\left(X_{j}\right)$ is the entropy of $X_{j}$ at node $\boldsymbol{N}$, which is defined to be $-p_{\boldsymbol{N}} \log \left(p_{\boldsymbol{N}}\right)-\left(1-p_{\boldsymbol{N}}\right) \log \left(1-p_{\boldsymbol{N}}\right)$, where $p_{\boldsymbol{N}}$ is the probability that a gene $g \in G$ at a node $\boldsymbol{N}$ is annotated as having attribute $j$ (see, e.g., Cover and Thomas 1991). As in Niblett and Bratko (1986), we used the estimate

$$
p_{\boldsymbol{N}}=\frac{\#\left\{g \in \boldsymbol{N}: X_{j}(g)=1\right\}+m p(j)}{\#\{g \in \boldsymbol{N}\}+m}
$$

where $p(j)$ is the fraction of the genes in the entire training set that are annotated as having attribute $j$ and $m$ is an adjustable parameter. The term $m p(j)$ is used as a pseudocount-a small sample-size regularization term, with an interpretation as a prior probability in a Bayesian framework (see, e.g., Ewans and Grant 2001); as our prior convictions about $p_{\boldsymbol{N}}$ were fairly weak, we set $m=1$. We used $\#\{g \in \boldsymbol{N}_{i}\} / \#\{g \in \boldsymbol{N}\}$ as an estimate for $\operatorname{Pr}\left(g \in \boldsymbol{N}_{i} \mid g \in \boldsymbol{N}\right)$ for $t=0$ and $t=1$, again following Niblett and Bratko (1986).

When no test at a node $\boldsymbol{N}$ provides a positive information gain, the node is not split, but becomes a leaf. It is labeled with the estimate $p_{\boldsymbol{N}}$ of the probability that a gene at node $\boldsymbol{N}$ has attribute $j$, as defined above.

A tree grown in this manner will usually overfit the training data, and consequently perform poorly on the held-out test data. A standard way of combating this is to prune away some of the branches after the tree is grown. We used the Bayesian Information Criterion

$$
\mathrm{BIC}=-2 \ln \operatorname{Pr}(\text { data } \mid \text { model })+(\ln M) K
$$

which is asymptotically equivalent to the Minimum Description Length (MDL; Schwartz 1978) for model selection during pruning (see e.g. Friedman and Goldszmidt 1996). Here $K$ is the number of free parameters in the model (which in our case coincides with the number of leaves in the decision tree), and $M$ is the number of samples in the data set (which in our case is the number of genes in the training set). The first term measures the goodness of fit of the model to the data, and the second term penalizes model complexity. We pruned the tree in a bottom-up fashion, starting at the leaves and working toward the root, pruning away any branch whose removal caused the tree's BIC score to decrease. In computing the BIC score we treated the genes as independent, so that the likelihood $\operatorname{Pr}($ data $\mid$ model $)$ factored as the product of the likelihood for each gene. (This may not be strictly true, because of homology between genes, for example.)

The score $q(i, j)=\operatorname{Pr}\left(X_{j}=1 \mid \operatorname{nad}\left(X_{j}\right)=\operatorname{nad}\left(X_{j}\right)(i)\right)$ was then just $p_{\boldsymbol{N}_{i}}$, where $\boldsymbol{N}$ is the leaf at which gene $i$ ends up in the decision tree for attribute $j$.

Figure 2 shows the decision tree for the attribute "Cchromatin," constructed using the SGD data.
![img-1.jpeg](img-1.jpeg)

Figure 2 A decision tree for the attribute "C-chromatin" learned from the SGD data. Starting from the top node, if a gene is annotated with the attribute listed in the node, then it travels down the edge labeled "+"; otherwise it travels down the edge labeled "-." Leaf nodes are labeled with the number of genes in the training set that end up at the node, split into those that are annotated with "Cchromatin" in the SGD database (prefixed by "+") and those that are not (prefixed by "-"). Ancestors and descendants of "C-chromatin" in the GO DAG were not allowed for making splits in this tree.

![img-2.jpeg](img-2.jpeg)

Figure 3 A fragment of the Bayesian network for SGD attributes. The full network contains 634 nodes. There is an edge from $X_{j}$ to $X_{k}$ if and only if $X_{j} \in \mathbf{p a}\left(X_{k}\right)$. Most of the displayed vertices have additional outgoing edges, not shown, to vertices that are not shown. Edges in the Bayesian network that are also edges in the GO DAG are shown in black; the remaining edges are shown in gray.

## Bayesian Networks

In the approach described above, we constructed a decision tree modeling $\operatorname{Pr}\left(X_{j} \mid \mathbf{n a d}\left(X_{j}\right)\right)$ independently for each attribute $j$. An alternative approach is to model the joint probability distribution $\operatorname{Pr}\left(X_{1}, X_{2}, \ldots, X_{N}\right)$ of all the attributes. From the joint probability distribution, one can compute conditional probabilities such as $\operatorname{Pr}\left(X_{j} \mid \mathbf{n a d}\left(X_{j}\right)\right)$.

Decision trees assembled independently as in the subsection above are not in general compatible with any single joint distribution (see, e.g., Heckerman et al. 2000), so this alternative approach has the advantage of internal consistency. Another advantage is that from the joint distribution one can also compute predictions for combinations of attributes, rather than just for a single attribute, without relearning the model. One drawback is the increased computational complexity in computing $q(i, j)$.

A Bayesian network (Pearl 1988; Jensen 2001) is a formalism for representing a joint probability distribution as a directed graph, where vertices correspond to random variables and the absence of an edge between vertices indicates a conditional independence between the random variables. Among their many applications, Bayesian networks have been used for medical diagnosis (e.g., Kahn Jr. et al. 1997; Jaakkola and Jordan 1999) and for inferring gene regulatory networks (e.g., Friedman et al. 2000).

By the chain rule of probability, for any ordering $X_{1}, \ldots$, $X_{N}$ of the random variables corresponding to the GO attributes, the joint probability $\operatorname{Pr}\left(X_{1}, \ldots, X_{N}\right)$ factors as

$$
\operatorname{Pr}\left(X_{1}\right) \operatorname{Pr}\left(X_{2} \mid X_{1}\right) \ldots \operatorname{Pr}\left(X_{N} \mid X_{1}, \ldots, X_{N-1}\right)=\prod_{j=1}^{N} \operatorname{Pr}\left(X_{j} \mid X_{1}, \ldots, X_{j-1}\right)
$$

For a Bayesian network, the idea is to exploit conditional independencies between the attributes to find a subset $\mathbf{p a}\left(X_{j}\right)$ of $\left\{X_{1}, \ldots, X_{j-1}\right\}$ for which $\operatorname{Pr}\left(X_{j} \mid \mathbf{p a}\left(X_{j}\right)\right)$ is a good approxima-
tion to $\operatorname{Pr}\left(X_{j} \mid X_{1}, \ldots, X_{j-1}\right)$. This can greatly reduce the number of parameters that must be estimated.

The extent to which these conditional independencies may be exploited depends on the ordering of the variables. Because the logical relations encoded by the GO DAG induce conditional independencies that we would like to exploit, we chose an ordering of the random variables that is compatible with the GO DAG, that is, an ordering $X_{1}, \ldots, X_{N}$ in which $j<k$ whenever $X_{j}$ is a parent of $X_{k}$ in the GO DAG. Because the GO DAG is acyclic, such an ordering exists, and is called a linear ordering or a topological sorting of the DAG. (There are, in fact, many topological sortings of the GO DAG; we did not attempt to find an optimal one.)

As in Friedman and Goldszmidt (1996) and Heckerman et al. (2000), we represented the local conditional probability distributions $\operatorname{Pr}\left(X_{j} \mid \mathbf{p a}\left(X_{j}\right)\right)$ by probabilistic decision trees rather than by conditional probability tables. This is a more parsimonious representation when there are conditional independencies that hold only for particular values of the random variables in $\mathbf{p a}\left(X_{j}\right)$. The decision trees were constructed using the algorithm described in the subsection above, with the following differences.

In the subsection above, when constructing the decision tree for attribute $j$ we allowed splits to be made using any attribute $k \neq j$ for which $k$ was neither a descendent nor an ancestor of $j$ in the GO DAG; here we allowed splits to be made using any attribute $k$ with $k<j$ in the topological sorting of the GO DAG. This means that none of the descendants of $j$ in the GO DAG could be used for splits, but that all of the ancestors of $j$ in the GO DAG could be used, and usually some other attributes as well. We also modified the decision-treegrowing algorithm slightly so that the first test was: "Is $X_{k}(i)=1$ for all of the parents $k$ of $j$ in the GO DAG?" If the answer was "no," then it logically follows that $X_{j}(i)=0$, so gene $i$ was sent to a leaf node $\mathbf{N}$ with $\mathbf{N}_{p}=0$. (Unlike the other

nodes, no pseudocounts were used here because $X_{j}(t)=0$ is a logical necessity; this node was also designated unpruneable.) If the answer was "yes," then the gene was sent to another node, which was then recursively split using the ordinary information gain criterion to complete the tree. This tree was pruned as in the subsection above. The elements of $\mathbf{p a}\left(X_{j}\right)$ were just those $X_{k}$ for which attribute $k$ was used as a split in the pruned decision tree for attribute $j$.

The graphical representation of the Bayesian network is constructed by including a directed edge from vertex $X_{k}$ to vertex $X_{j}$ if and only if $X_{k} \in \mathbf{p a}\left(X_{j}\right)$. The elements of $\mathbf{p a}\left(X_{j}\right)$ are usually called the parents of $X_{j}$; we have not referred to them as such until now, to avoid confusion with the parents of attribute $j$ in the GO DAG. But note that by our choice of an ordering of the attributes, and our modifications to the deci-sion-tree-growing algorithm, we have arranged things so that the GO DAG is a subgraph of the Bayesian network, that is, so that if $k$ is a parent of $j$ in the GO DAG, then $X_{k} \in \mathbf{p a}\left(X_{j}\right)$. (The converse need not be true, however.) We have also ensured that the joint probability distribution defined by the Bayesian network is consistent with the logical constraints imposed by the GO DAG.

Figure 3 shows a fragment of the Bayesian network for the SGD attributes.

Computing the joint probability of a specific sequence of annotations $\mathbf{X}=\left(X_{1}, \ldots, X_{N}\right)$ is straightforward with the Bayesian network: $\operatorname{Pr}(\mathbf{X})$ factors as $\prod_{i=1}^{N} \operatorname{Pr}\left(X_{i} \mid \mathbf{p a}\left(X_{i}\right)\right)$, and if a gene with annotation vector $\mathbf{X}$ ends up at leaf $\mathbf{N}$ in the decision tree for attribute $j$, then the term $\operatorname{Pr}\left(X_{j} \mid \mathbf{p a}\left(X_{j}\right)\right)$ is equal to $p_{\mathbf{N}}$ if $X_{j}=1$, and to $1-p_{\mathbf{N}}$ if $X_{j}=0$.

Now $\operatorname{Pr}\left(\mathbf{n a d}\left(X_{j}\right)=\mathbf{n a d}\left(X_{j}\right)\right)$ ) may be computed by summing the joint probability of $\mathbf{X}$ over all possible assignments of values to the random variables not in $\mathbf{n a d}\left(X_{j}\right)$, keeping the known values of the random variables in $\mathbf{n a d}\left(X_{j}\right)$ fixed as $\mathbf{n a d}\left(X_{j}\right)(t)$. The score $q\left(t, j\right)=\operatorname{Pr}\left(X_{j}=1 \mid \mathbf{n a d}\left(X_{j}\right)=\mathbf{n a d}\left(X_{j}\right)(t)\right)$ is just the ratio of the sum of those joint probabilities for assignments in which $X_{j}=1$ to the total sum.

Computing this sum using brute force has running time exponential in the number of ancestors and descendants of attribute $j$ in the GO DAG. In our computations, each test attribute $j \in T$ had $<2 S$ ancestors in $A_{10}$ and no descendants in $A_{10}$ (because we were predicting only the most detailed attributes), so the brute force method was feasible. But given that any assignment of values to the random variables not in $\mathbf{n a d}\left(X_{j}\right)$ that is not logically consistent with the GO DAG has joint probability zero, we were able to speed up the computation by summing over just those assignments that were logically consistent with the GO DAG. An alternative would be to use the variable elimination algorithm or the junction tree algorithm (see Jensen 2001) to speed up the computation. These algorithms are not always practical for large networks with many undirected cycles, such as ours, but because all but 20 or so of the random variables in our network are instantiated with known values when computing $q\left(t, j\right)$, this is not a problem.

The Bayesian network approach also has a natural extension in which the reliability of different evidence types is explicitly modeled, and the distinction between negative evidence and the absence of evidence is made explicit. Such a model would have two vertices for each GO attribute: an "evidence" vertex that gives the types of evidence (if any), and a "hidden" vertex corresponding to the truth (which is not directly observable). Learning the topology and parameters of such a model would require a technique that deals with missing data, such as the structural EM algorithm (Friedman 1998). The goal would then be to infer the values of all the hidden variables for a gene on the basis of all the evidence for the gene. But the model would have hundreds of hidden variables to sum over, making exact inference infeasible. (Note that even approximate inference in a general Bayesian network is NP-hard [Cooper 1990; Dagum and Luby 1993].)

Nonetheless, there might be some prospect of reasonably estimating the values of the hidden variables using Monte Carlo methods (Gilks et al. 1996) or "loopy" belief propagation (Murphy et al. 1999).

## ACKNOWLEDGMENTS

The authors thank the GO Consortium members, particularly M. Ashburner, M. Cherry, and S. Lewis; and also the anonymous referees for their helpful suggestions. This research was sponsored in part by a grant from Aventis Pharmaceuticals, and by an institutional grant from the HHMI Biomedical Research Support Program for Medical Schools. O.D.K. was supported by an Individual NRSA Fellowship from NHGRI. R.E.F. was supported by a Medical Research Council Project Grant to M. Ashburner.

The publication costs of this article were defrayed in part by payment of page charges. This article must therefore be hereby marked "advertisement" in accordance with 18 USC section 1734 solely to indicate this fact.

## WEB SITE REFERENCES

http://llama.med.harvard.edu/ king/predictions.html; curators' notes on hypotheses.
http://www.geneontology.org; Gene Ontology Consortium homepage.
http://www.geneontology.org/doc/GO.annotation.html; Gene Ontology Annotation Guide.

Received May 18, 2002; accepted in revised form February 13, 2003.

# Predicting Gene Function From Patterns of Annotation 

Oliver D. King, Rebecca E. Foulger, Selina S. Dwight, et al.
Genome Res. 2003 13: 896-904
Access the most recent version at doi:10.1101/gr. 440803

## References This article cites 13 articles, 3 of which can be accessed free at: http://genome.cshlp.org/content/13/5/896.full.html\#ref-list-1

## License

Email Alerting Receive free email alerts when new articles cite this article - sign up in the box at the top right corner of the article or click here.

To subscribe to Genome Research go to:
https://genome.cshlp.org/subscriptions

Cold Spring Harbor Laboratory Press