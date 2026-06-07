# Monographs in Computer Science 

Editors

David Gries<br>Fred B. Schneider

## Springer

New York
Berlin
Heidelberg
Barcelona
Budapest
Hong Kong
London
Milan
Paris
Santa Clara
Singapore
Tokyo

# Monographs in Computer Science 

Abadi and Cardelli, A Theory of Objects
Brzozowski and Seger, Asynchronous Circuits
Selig, Geometrical Methods in Robotics
Nielson [editor], ML with Concurrency
Castillo, Gutiérrez, and Hadi, Expert Systems and Probabilistic Network Models

# Enrique Castillo José Manuel Gutiérrez Ali S. Hadi 

## Expert Systems and Probabilistic Network Models

With 250 Figures

Enrique Castillo
Cantabria University
39005 Santander, Spain
E-mail: castie@ccaix3.unican.es

Ali S. Hadi
Cornell University
358 Ives Hall
Ithaca, NY 14853-3901
USA

Series Editors:
David Gries
Department of Computer Science
Cornell University
Upson Hall
Ithaca, NY 14853-7501
USA

José Manuel Gutiérrez
Cantabria University
39005 Santander, Spain
E-mail: gutierjm@ccaix3.unican.es

Fred B. Schneider
Department of Computer Science
Cornell University
Upson Hall
Ithaca, NY 14853-7501
USA

Library of Congress Catologing-in-Publication Data
Castillo, Enrique.
Expert systems and probabilistic network models / Enrique
Castillo, José Manuel Gutiérrez, Ali S. Hadi.
p. cm. - (Monographs in computer science)

Includes bibliographical references and index.
ISBN-13:978-1-4612-7481-0 e-ISBN-13:978-1-4612-2270-5
DOI: $10.1007 / 978-1-4612-2270-5$

1. Expert systems (Computer science) 2. Probabilities.
I. Gutiérrez, José Manuel. II. Hadi, Ali S. III. Title.
IV. Series.

QA76.76.E95C378 1997
006.3'3-dc20 96-33161

Printed on acid-free paper.
(c) 1997 Springer-Verlag New York, Inc.

Softcover reprint of the hardcover lst edition 1997

All rights reserved. This work may not be translated or copied in whole or in part without the written permission of the publisher (Springer-Verlag New York, Inc., 175 Fifth Avenue, New York, NY 10010, USA), except for brief excerpts in connection with reviews or scholarly analysis. Use in connection with any form of information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed is forbidden.
The use of general descriptive names, trade names, trademarks, etc., in this publication, even if the former are not especially identified, is not to be taken as a sign that such names, as understood by the Trade Marks and Merchandise Marks Act, may accordingly be used freely by anyone.

Production managed by Lesley Poliner; manufacturing supervised by Johanna Tschebull.
Photocomposed using the authors' $\mathrm{IA}_{\mathrm{E}} \mathrm{X}$ files.
987654321
ISBN-13:978-1-4612-7481-0 Springer-Verlag New York Berlin Heidelberg SPIN 10524048

To all the people of the former Yugoslavia with the hope that they will live together in peace and be friends, as are the authors, despite the differences in our religions, languages, and national origins.

# Preface 

The artificial intelligence area in general and the expert systems and probabilistic network models in particular have seen a great surge of research activity during the last decade. Because of the multidisciplinary nature of the field, the research has been scattered in professional journals in many fields such as computer science, engineering, mathematics, probability, and statistics. This book collects, organizes, and summarizes these research works in what we hope to be a clear presentation. Every effort has been made to keep the treatment of the subject as up-to-date as possible. Actually, some of the material presented in the book is yet to be published in the literature. See, for example, the material in Chapter 12 and some of the material in Chapters 7 and 11.

The book is intended for students and research workers from many fields such as computer science; engineering and manufacturing; medical and pharmaceutical sciences; mathematical, statistical, and decision sciences; business and management; economics and social sciences; etc. For this reason, we assumed no previous background in the subject matter of the book. The reader, however, is assumed to have some background in probability and statistics and to be familiar with some matrix notation (see, e.g., Hadi (1996)). In a few instances, we give some programs in Mathematica to perform the calculations. For a full understanding of these programs some knowledge of Mathematica is needed.

The book can be used as a reference or consulting book and as a textbook in upper-division undergraduate courses or in graduate-level courses. The book contains numerous illustrative examples and end-of-chapter exercises. We have also developed some computer programs to implement the various algorithms and methodologies presented in this book. The current version of these programs, together with a brief User's Guide, can be obtained from the World Wide Web site http://ccaix3.unican.es/ AIGroup. We have used these programs to do the examples and we encourage the reader to use them to solve some of the exercises. The computer programs can also help research workers and professionals apply the methodology to their own

fields of study. Actually, we have used these programs to analyze some reallife applications (case studies) in Chapter 12. We therefore encourage the reader to use and explore the capabilities of these programs. It is suggested that the reader repeat the computations in the examples and solve the exercises at the end of the chapters using these programs. We hope that making such programs available will facilitate the learning of the material presented in this book. Finally, the extensive bibliography included at the end of the book can also serve as a basis for additional research.

Although some theory is present in the book, the emphasis is on applications rather than on theory. For this reason, the proofs of many theorems are left out, numerous examples are used to illustrate the concepts and theory, and the mathematical level is kept to a minimum.

The book is organized as follows. Chapter 1 is an introductory chapter, which among other things, gives some motivating examples, describes the components and development of an expert system, and surveys other related areas of artificial intelligence. Chapters 2 and 3 describe the main two types of expert systems: rule-based and probabilistic expert systems. Although the two types of expert systems are introduced separately, rulebased expert system can be thought of as a special case of the more powerful probabilistic expert system.

It is argued in Chapters 1-3 that two of the most important and complex components of expert systems are the coherence control and the inference engine. These are perhaps the two weakest links in almost all current expert systems, the former because it has appeared relatively recently and many of the existing expert systems do not have it, and the latter because of its complexity. In Chapters $1-3$ we show how these subsystems can be implemented in rule-based and probability-based expert systems and how the probability assignment must be done in order to avoid inconsistencies. For example, the automatic updating of knowledge and the automatic elimination of object values are important for maintaining the coherence of the system. Chapters $5-10$ are mainly devoted to the details of such implementations.

The materials in Chapter 5 and beyond require some concepts of graph theory. Since we expect that some of the readers may not be familiar with these concepts, Chapter 4 presents these concepts. This chapter is an essential prerequisite for understanding the topics covered in the remaining chapters. Building probabilistic models, which are needed for the knowledge base of a probabilistic expert system, is presented in Chapters 5-7. In particular, the independence and conditional independence concepts, which are useful for defining the internal structure of probabilistic network models and for knowing whether or not some variables or sets of variables have information about other variables, are discussed in Chapter 5. As mentioned in Chapter 4, graphs are essential tools for building probabilistic and other models used in expert systems. Chapter 6 presents the Markov and Bayesian network models as two of the most widely used graphical

network models. Chapter 7 extends graphically specified models to more powerful models such as models specified by multiple graphs, models specified by input lists, multifactorized probabilistic models, and conditionally specified probabilistic models.

Chapters 8 and 9 present the most commonly used exact and approximate methods for the propagation of evidence, respectively. Chapter 10 introduces symbolic propagation, which is perhaps one of the most recent advances in evidence propagation. Chapter 11 deals with the problem of learning Bayesian network models from data. Finally, Chapter 12 includes several examples of applications (case studies).

Many of our colleagues and students have read earlier versions of this manuscript and have provided us with valuable comments and suggestions. Their contributions have given rise to the current substantially improved version. In particular, we acknowledge the help of the following (in alphabetical order): Noha Adly, Remco Bouckaert, Federico Ceballos, Jong Wang Chow, Javier Díez, Dan Geiger, Joseph Halpern, Judea Pearl, Julius Reiner, Milan Studený, and Jana Zvárová.

Enrique Castillo
Jose Manuel Gutiérrez
Ali S. Hadi

# Contents 

Preface ..... vii
1 Introduction ..... 1
1.1 Introduction ..... 1
1.2 What Is an Expert System? ..... 2
1.3 Motivating Examples ..... 3
1.4 Why Expert Systems? ..... 7
1.5 Types of Expert System ..... 8
1.6 Components of an Expert System ..... 10
1.7 Developing an Expert System ..... 14
1.8 Other Areas of AI ..... 16
1.9 Concluding Remarks ..... 20
2 Rule-Based Expert Systems ..... 21
2.1 Introduction ..... 21
2.2 The Knowledge Base ..... 22
2.3 The Inference Engine ..... 28
2.4 Coherence Control ..... 48
2.5 Explaining Conclusions ..... 52
2.6 Some Applications ..... 53
2.7 Introducing Uncertainty ..... 65
Exercises ..... 65
3 Probabilistic Expert Systems ..... 69
3.1 Introduction ..... 69
3.2 Some Concepts in Probability Theory ..... 71
3.3 Generalized Rules ..... 85
3.4 Introducing Probabilistic Expert Systems ..... 86
3.5 The Knowledge Base ..... 91
3.6 The Inference Engine ..... 102
3.7 Coherence Control ..... 104

3.8 Comparing Rule-Based and Probabilistic Expert Systems ..... 106
Exercises ..... 108
4 Some Concepts of Graphs ..... 113
4.1 Introduction ..... 113
4.2 Basic Concepts and Definitions ..... 114
4.3 Characteristics of Undirected Graphs ..... 118
4.4 Characteristics of Directed Graphs ..... 122
4.5 Triangulated Graphs ..... 129
4.6 Cluster Graphs ..... 139
4.7 Representation of Graphs ..... 144
4.8 Some Useful Graph Algorithms ..... 158
Exercises ..... 172
5 Building Probabilistic Models ..... 175
5.1 Introduction ..... 175
5.2 Graph Separation ..... 177
5.3 Some Properties of Conditional Independence ..... 184
5.4 Special Types of Input Lists ..... 192
5.5 Factorizations of the JPD ..... 195
5.6 Constructing the JPD ..... 200
Appendix to Chapter 5 ..... 204
Exercises ..... 206
6 Graphically Specified Models ..... 211
6.1 Introduction ..... 211
6.2 Some Definitions and Questions ..... 213
6.3 Undirected Graph Dependency Models ..... 218
6.4 Directed Graph Dependency Models ..... 237
6.5 Independence Equivalent Graphical Models ..... 252
6.6 Expressiveness of Graphical Models ..... 259
Exercises ..... 262
7 Extending Graphically Specified Models ..... 267
7.1 Introduction ..... 267
7.2 Models Specified by Multiple Graphs ..... 269
7.3 Models Specified by Input Lists ..... 275
7.4 Multifactorized Probabilistic Models ..... 279
7.5 Multifactorized Multinomial Models ..... 279
7.6 Multifactorized Normal Models ..... 292
7.7 Conditionally Specified Probabilistic Models ..... 298
Exercises ..... 311
8 Exact Propagation in Probabilistic Network Models ..... 317
8.1 Introduction ..... 317

8.2 Propagation of Evidence ..... 318
8.3 Propagation in Polytrees ..... 321
8.4 Propagation in Multiply-Connected Networks ..... 342
8.5 Conditioning Method ..... 342
8.6 Clustering Methods ..... 351
8.7 Propagation Using Join Trees ..... 366
8.8 Goal-Oriented Propagation ..... 377
8.9 Exact Propagation in Gaussian Networks ..... 382
Exercises ..... 387
9 Approximate Propagation Methods ..... 393
9.1 Introduction ..... 393
9.2 Intuitive Basis of Simulation Methods ..... 394
9.3 General Frame for Simulation Methods ..... 400
9.4 Acceptance-Rejection Sampling Method ..... 406
9.5 Uniform Sampling Method ..... 409
9.6 The Likelihood Weighing Sampling Method ..... 411
9.7 Backward-Forward Sampling Method ..... 413
9.8 Markov Sampling Method ..... 415
9.9 Systematic Sampling Method ..... 419
9.10 Maximum Probability Search Method ..... 429
9.11 Complexity Analysis ..... 439
Exercises ..... 440
10 Symbolic Propagation of Evidence ..... 443
10.1 Introduction ..... 443
10.2 Notation and Basic Framework ..... 445
10.3 Automatic Generation of Symbolic Code ..... 447
10.4 Algebraic Structure of Probabilities ..... 454
10.5 Symbolic Propagation Through Numeric Computations ..... 455
10.6 Goal-Oriented Symbolic Propagation ..... 464
10.7 Symbolic Treatment of Random Evidence ..... 470
10.8 Sensitivity Analysis ..... 472
10.9 Symbolic Propagation in Gaussian Bayesian Networks ..... 474
Exercises ..... 478
11 Learning Bayesian Networks ..... 481
11.1 Introduction ..... 481
11.2 Measuring the Quality of a Bayesian Network Model ..... 484
11.3 Bayesian Quality Measures ..... 486
11.4 Bayesian Measures for Multinomial Networks ..... 490
11.5 Bayesian Measures for Multinormal Networks ..... 499
11.6 Minimum Description Length Measures ..... 506
11.7 Information Measures ..... 509
11.8 Further Analyses of Quality Measures ..... 509

11.9 Bayesian Network Search Algorithms ..... 511
11.10The Case of Incomplete Data ..... 513
Appendix to Chapter 11: Bayesian Statistics ..... 515
Exercises ..... 525
12 Case Studies ..... 529
12.1 Introduction ..... 529
12.2 Pressure Tank System ..... 530
12.3 Power Distribution System ..... 542
12.4 Damage of Concrete Structures ..... 550
12.5 Damage of Concrete Structures: The Gaussian Model ..... 562
Exercises ..... 567
List of Notation ..... 573
References ..... 581
Index ..... 597