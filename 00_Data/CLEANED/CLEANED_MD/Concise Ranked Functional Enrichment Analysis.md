# Concise ranked functional enrichment analysis 

Xinglin Jia*<br>Department of Mathematics<br>Iowa State University<br>Ames, IA 50011 USA<br>xjia@iastate.edu

An Phan*<br>Department of Mathematics<br>Iowa State University<br>Ames, IA 50011 USA<br>ahphan@iastate.edu

Claus Kadelka<br>Department of Mathematics<br>Iowa State University<br>Ames, IA 50011 USA<br>ckadelka@iastate.edu

## CCS CONCEPTS

- Applied computing $\rightarrow$ Systems biology; Computational biology


## KEYWORDS

Gene set enrichment analysis, Bayesian network

## ACM Reference format:

Xinglin Jia, An Phan, and Claus Kadelka. 2023. Concise ranked functional enrichment analysis. In Houston '23: The 14th ACM Conference on Bioinformatics, Computational Biology, and Health Informatics, September 03-06, 2023, Houston, TX. ACM, New York, NY, USA, 1 page. https://doi.org/10.1145/3584371.3613044

## ABSTRACT

The integration of technology with large-scale biology has resulted in a proliferation of genome-wide expression data. Functional enrichment methods identify functional categories (e.g., biological processes) that preferentially annotate differentially expressed genes. Many existing methods operate in a binary manner, disregarding valuable information contained in the gene ranking. The few methods that consider the ranking often return redundant or non-specific functional categories. To address these limitations, we propose a novel functional enrichment method called Concise Ranked Functional Enrichment (CRFE). CRFE effectively leverages the ranking information in gene expression datasets to compute a non-redundant set of specific functional categories that are notably enriched for highly ranked genes.

Using four treatment-control RNA-seq datasets, we compare the performance of CRFE with the two most widely used types of functional enrichment methods, Gene Set Enrichment Analysis and over-representation analysis. We assess the methods based on three metrics: Firstly, the method should identify functional

[^0]categories that are particularly enriched for the highly ranked genes, thereby maximizing the potential insights gained from the ranking. Secondly, the hierarchical structure of annotation databases such as the Gene Ontology implies that many functional categories have similar gene annotations. A good method should return a set of functional categories with minimally overlapping gene annotations. Thirdly, to enable a more meaningful biological interpretation, the returned functional categories should have high information content, i.e., annotating only a few genes.

Our findings demonstrate that CRFE excels in all evaluated criteria, outperforming all investigated existing methods, each of which exhibits deficiencies in at least one metric. Furthermore, we provide a comprehensive interpretation of the functional categories identified by CRFE, showcasing its usefulness for experimentalists. In conclusion, CRFE capitalizes on the valuable information inherent in ranked gene lists to compute an informative set of functional categories that summarizes the provided genome-wide expression data. With its superior performance, CRFE shows great promise as the preferred method for functional enrichment analysis.


[^0]:    *Both authors contributed equally to this research.
    Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).
    BCR 23, September 3-6, 2023, Houston, Texas USA (C) 2023 Copyright held by the owner/author(s).
    ACM ISBN 979-8-4007-0126-9/23/09
    https://doi.org/10.1145/3584371.3613044