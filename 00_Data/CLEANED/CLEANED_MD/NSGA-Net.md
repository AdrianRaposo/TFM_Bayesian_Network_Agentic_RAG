# NSGA-Net: Neural Architecture Search using Multi-Objective Genetic Algorithms Supplementary Materials 

Zhichao Lu, Ian Whalen, Vishnu Boddeti, Yashesh Dhebar, Kalyanmoy Deb, Erik Goodman and Wolfgang Banzhaf<br>Michigan State University<br>East Lansing, Michigan<br>\{luzhicha, whalenia, vishnu,dhebarya, kdeb,goodman, banzhafw\}@msu.edu

## ACM Reference Format:

Zhichao Lu, Ian Whalen, Vishnu Boddeti, Yashesh Dhebar, Kalyanmoy Deb, Erik Goodman and Wolfgang Banzhaf. 2019. NSGA-Net: Neural Architecture Search using Multi-Objective Genetic Algorithms Supplementary Materials. In Proceedings of the Genetic and Evolutionary Computation Conference 2019 (GECCO '19). ACM, New York, NY, USA, 5 pages. https://doi.org/10.1145/3321707.3321729

## 1 DUPLICATE CHECKING AND REMOVAL

Due to the directed acyclic nature of our encoding, redundancy exists in the search space defined by our coding, meaning that there exist multiple encoding strings that decode to the same network architecture. Empirically, we have witnessed the redundancy becomes more and more severe as the allowed number of nodes in each phase's computational block increase, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1: Increase in redundancy as node count increases.

Since the training of a deep network is a computationally taxing task, it is essential to avoid the re-computation of the same architecture. In this section, we will provide with an overview of an algorithm we developed to quickly and approximately do a duplicate-check on genomes. The algorithm takes two genomes to be compared as an input, and outputs a flag to indicate if the supplied genomes decode to same architecture.

[^0]In general, comparing two graphs is NP-hard, however, given that we are working with Directed Acyclic Graphs with every node being the same in terms of operations, we were able to design an efficient network architecture duplicate checking method to identify most of the duplicates if not all. The method is built on top of simply intuition that under such circumstances, the duplicate network architectures should be identified by swapping the node numbers. Examples are provided in Figure 2. Our duplicates checking method first derive the connectivity matrix from the bit-string, which will have positive 1 indicating there is an input to that particular node and negative 1 indicating an output from that particular node. Then a series row-and-column swapping operation takes place, which essentially try to shuffle the node number to check if two connectivity matrix can be exactly matched. Empirically, we have found this method performs very efficiently in identifying duplicates. An example of different operation encoding bit-strings decode to the same network phase is provided in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: Examples of different encoding bit strings that decode to the same network computation block.

## 2 ARCHITECTURE COMPLEXITY ESTIMATION

We argue that the choice of inference time or number of parameters as proxies for computational complexity are sub-optimal and ineffective in practice. In fact, we initially considered both of these objectives. We concluded from extensive experimentation that inference time cannot be estimated reliably due differences and inconsistencies in computing environment, GPU manufacturer, and GPU temperature etc. Similarly, the number of parameters only relates one aspect of computational complexity. Instead, we chose to use the number of floating-point operations (FLOPs) for our second objective. The following table compares the number of active nodes, the number of connections, the total number of parameters and the FLOPs over a


[^0]:    Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).
    GECCO' 19, July 13-17, 2019, Prague, Czech Republic
    (C) 2019 Copyright held by the owner/author(s).

    ACM ISBN 978-1-4503-6111-8/19/07... $\$ 15.00$
    https://doi.org/10.1145/3321707.3321729

Table 1: Network examples comparing the number of active nodes, number of connections, number of parameters and number of multiply-adds.


![img-2.jpeg](img-2.jpeg)

Figure 3: Set of networks architectures on the trade-off frontier discovered by NSGA-Net.

Table 2: Summary of relevant related work along with datasets each method has been applied to, objectives optimized, and the computational power used (if reported). Methods not explicitly named are presented as the author names. PTB refers to the Penn Treebank [14] dataset. The Dataset(s) column describes what datasets the method performed a search with, meaning other datasets may have been presented in a study, but not used to perform architecture search. A dash represents some information not being provided. We attempt to limit the focus here to published methods, though some unpublished methods may be listed for historical contingency.

