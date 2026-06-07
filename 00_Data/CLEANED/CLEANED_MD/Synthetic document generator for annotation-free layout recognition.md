# Synthetic Document Generator for Annotation-Free Layout Recognition 

Natraj Raman ${ }^{1}$, Sameena Shah ${ }^{2}$ and Manuela Veloso ${ }^{2}$<br>JPMorgan AI Research<br>${ }^{1}$ London, UK.<br>${ }^{2}$ New York, USA.<br>first.last@jpmorgan.com


#### Abstract

Analyzing the layout of a document to identify headers, sections, tables, figures etc. is critical to understanding its content. Deep learning based approaches for detecting the layout structure of document images have been promising. However, these methods require a large number of annotated examples during training, which are both expensive and time consuming to obtain. We describe here a synthetic document generator that automatically produces realistic documents with labels for spatial positions, extents and categories of the layout elements. The proposed generative process treats every physical component of a document as a random variable and models their intrinsic dependencies using a Bayesian Network graph. Our hierarchical formulation using stochastic templates allow parameter sharing between documents for retaining broad themes and yet the distributional characteristics produces visually unique samples, thereby capturing complex and diverse layouts. We empirically illustrate that a deep layout detection model trained purely on the synthetic documents can match the performance of a model that uses real documents.


Keywords Synthetic Image Generation $\cdot$ Bayesian Network $\cdot$ Layout Analysis

## 1 Introduction

Documents remain the most popular source of information and machine understanding of the document contents is critical for several tasks such as semantic search, question answering, knowledge base population and summarization. Traditional information retrieval techniques [1] from documents tend to focus on the text content and ignore the layout structure. However, the layout cues in documents provide necessary context to the text and can serve as an important signal for measuring information saliency. For instance, the retrieved results for a query phrase that matches both a heading and a typical passage should be ranked in favour of the former, since the headings are a natural concise synopsis of the content. Many documents also include tabular formats to summarize and compare information. In such cases, detecting the tables, spatially localizing the table cells and capturing the relationship between them is essential for information discovery. Thus identifying the layout elements such as title, section, illustration, table etc. is a necessary step towards effective understanding of a document.

Layout recognition [2] is a challenging problem owing to the variability in the structure and format of documents. Real-world documents originate in multiple domains, follow different templates, have complex structure and may be of poor-quality. In addition, the layout elements are not explicitly encoded in the digital representation of document formats such as PDFs and scanned images. Even if the layout structure is preserved in some document formats, it requires customized parsers and normalization for consistent treatment across the different formats.

Computer Vision based approaches for layout recognition have the advantage of making no assumption about the document format. Furthermore, the full spectrum of stylistic cues in the visual representation of a document can be efficiently exploited in the image space. Hence it would be beneficial to reframe the task of recognizing the layout elements in a document as detecting the objects in an image. The defacto approach of late in object detection is to use deep learning based feature representation and object segmentation [3]. The success of these methods rely on the

![img-0.jpeg](img-0.jpeg)

Figure 1: Overview of our approach. A document generator encoded as a Bayesian Network is used to construct a large number of synthetic documents. An object detection model is trained purely on these synthetic documents and inference is performed on real documents to identify layout elements such as sections, tables, figures etc.

availability of a large number of images annotated with the bounding boxes and categories of object instances during training. However, annotation exercises are expensive and even when labeled data is readily accessible, it may cater towards a specific domain or have restricted usage. There is a compelling opportunity to address this desperate shortage of free, diverse, unbiased and open-ended labeled documents by creating them on demand.

In this work, we address the problem of obtaining labeled documents for layout recognition by automatically generating documents along with ground-truths for spatial positions, extents and categories of the layout elements. Unlike existing methods [4] that require at least a few seed documents, the proposed generation mechanism needs virtually no access to any real documents. Specifically, we treat every component of a document such as a character glyph, geometric shape, font, alignment, color, spacing etc. as a random variable with a prior distribution. The intrinsic dependencies between the variables are modeled using conditional probability distributions. A synthetic document is constructed by sampling the variables from their corresponding distributions and rendering them in an image lattice. In order to account for the commonality in layout structure between subsets of documents, we introduce the notion of stochastic templates, where each template defines a unique set of distributional parameters. Documents that are instances of the same template share parameters and thus retain a broadly similar theme while differing in visual appearance.

This Bayesian Network [5] formulation of the document generation process can capture complex variations in layout structure, customize the visuals, model uncertainty, and produce large quantities of coherent and realistic synthetic documents. Furthermore, the hierarchical nature of the priors facilitates inductive biases that favor commonly observed patterns and allows parameter inference if samples of these variables from real documents are available. Since the generation process is agnostic to the text content, it is inherently multi-lingual and domain independent. It also provides flexibility in introducing imaging defects due to printing, optics, scanning, occlusion and degradation for simulation of low quality documents.

We illustrate the utility of our approach (see Figure 1) by training an object detector network purely on the synthetically generated documents and assess its ability to detect the layout elements such as sections, figures, tables and table cells on real world documents. In particular, we evaluate on three public datasets [6, 7, 8] and show that the performance difference between a layout detection model trained on real data and synthetic data is less than 4%. We also provide intuitive explanations on what the layout recognition model has really learned. Our main contributions are as following:

1. We propose a new document generator based on Bayesian Network framework to produce synthetic documents along with ground truths required for layout recognition.
2. We show that the generator can model complex layouts, customized templates, versatile languages, imaging defects and construct plausible realistic documents.
3. We empirically illustrate that layout detectors trained simply on synthetic documents can perform as well as those that use real documents.
4. We include quantitative comparisons, qualitative analysis, ablation studies and visual explanations to substantiate our findings.

Samples of synthetic documents corresponding to different domains are available at https://www.jpmorgan.com/synthetic-data.

The paper is organized as follows. Section 2 compares our work with related efforts, Section 3 describes the synthetic generation model in detail, Section 4 outlines the layout detection architecture, Section 5 presents samples of generated documents and discusses the recognition results, and finally Section 6 summarizes our findings.

# 2 Related Work 

Layout analysis of documents is a long standing problem of interest with decades of research efforts. Although Optical Character Recognition (OCR) systems [9] meet the requirements of extracting the text content from document images, they do not address the detection and labeling of semantic roles played by the text blocks. Early attempts [10] towards understanding the logical structure of the documents were largely rule-based. They generally segment the documents recursively into distinct geometric regions of homogeneous blocks by applying morphological operations and texture analysis. The main drawback of these methods are that the features are heuristical, require extensive human efforts to tune and fail to generalize.
Statistical machine learning approaches to model features and train parameters for layout analysis can overcome these drawbacks. Classical algorithms such as Support Vector Machines (SVMs) and Gaussian Mixture Models (GMMs) have been applied [11] for document segmentation tasks. However, these methods rely on hand crafted features and lack the ability to absorb the huge variations of documents in the wild. The advent of deep learning era has paved way for semantically rich features to be automatically extracted from images [12, 13]. Deep convolutional network based models have been used to perform layout analysis in [14], [15] and [16]. In particular, layout segmentation can be viewed as being equivalent to object detection and the recent successful models [17, 18] for detecting salient objects from natural scenes can be adapted to identify the layout elements in a document. Following this route, [19] focuses on identifying figures and formulae while [20] performs table structure recognition. In some cases [21], multi-modal information using both the image and text features have also been used for layout recognition.
The above data-driven deep learning based layout recognition techniques require a large number of annotated images for training, which are both expensive and time consuming to obtain. While it is true that there are a few datasets of documents $[6,7,22,23]$ available with ground-truths for the layout bounding boxes, they focus on specific corpora such as scientific publications and are difficult to extend to other domains or customize for new element types. Furthermore, they maybe bound by usage restrictions due to copyright and licensing constraints. In contrast, the proposed method here automatically generates annotated documents for training the deep learning models and hence do not suffer from these limitations.
Generation of synthetic documents to augment training data has been explored before. In [24], documents are generated by altering the style attributes in a HTML web-page for training an OCR system that recognized Chinese and Russian characters. Similarly, [25] constructs a document synthesis pipeline based on web browser templates to address training data scarcity and mitigate the impact of OCR errors for named entity recognition tasks. [4] proposes a semi-synthetic document creator that alters the font and background of an existing set of real documents to produce new documents. [26] randomly arranges layout elements in $\mathrm{I} \pi \mathrm{I}_{\mathrm{E}} \mathrm{X}$ source files and also replaces elements from existing files in an arbitrary fashion to generate synthetic documents. In contrast to the adhoc nature of above solutions which can only produce limited variations, our approach introduces a principled mechanism to model the physical and logical structure of the document that can create diverse layouts and offers granular control over the depiction of the layout elements.
Image creation using generative neural models has gained interest of late in the vision community. A recursive autoencoder that maps structural representations based on a limited number of labeled documents is used in [27] to augment training data. From annotated examples of layout bounding boxes, [28] generates new layouts using a variational autoencoder framework that incorporates attention mechanisms to capture relationships between layout elements. [29] also employ attention networks, but use self-supervised learning similar to masked language models for predicting the ground-truth tokens and modeling the probability distribution of layouts to sample from. The image generator in [30] takes randomly placed graphic elements as input and uses Generative Adverserial Networks (GAN) to produce different layouts with a differential wireframe rendering layer. Recently [31] proposed an adversarial training approach for controlled document synthesis using reference layout images for guidance. Our work differs from the above methods in its objective, the choice of generative model, its disentangled interpretable nature, the ability to create elements from scratch and importantly, does not require any annotations or real images for generating new documents.

## 3 Synthetic Document Generator

This section describes the Bayesian Network generative model from which the synthetic documents are sampled.

### 3.1 Bayesian Network Formulation

A document is comprised of primitive graphical units such as character glyphs, pictures and geometric shapes that are assembled in a logical structure. These primitive units are governed by a set of style attributes that define their visual representation. For example, the font, alignment and spacing attributes influence the appearance of character blocks

![img-1.jpeg](img-1.jpeg)

Figure 2: Cross section of the Bayesian network in plate notation. The shaded variables are observed and priors are denoted with subscript zero. The subnetworks and functions of variables are marked for illustration.

While stroke attributes control the thickness and color of a line or rectangular shape. These units are grouped into logical layout elements such as headers, sections, tables, footers etc. that describe the semantics of the graphical elements.

The diversity in observed documents is as a result of variations in the primitive units, their styles and the positional structure of the layout elements. A good document generator should have the capability to model these complex variations, provide flexibility to tailor the visuals, account for noise and produce realistic documents.

Our proposed solution employs a Bayesian Network to define the synthetic document generation process. The primitive units, style attributes and layout elements are all treated as random variables and represented as nodes in a graph. The intrinsic dependencies between these variables are symbolised using directed edges. Every node variable is endowed with a conditional probability distribution that quantifies the strength of relationship between a node and its parents. Parent-less nodes are described by marginal distributions. The parameters of a distribution may themselves have prior distributions with hyper-parameters resulting in a hierarchical model. These hyper-parameters are automatically learned during posterior inference if a corpus of real documents is available or set to pre-defined values if expert knowledge is available or could even have further vague priors, reflecting lack of information.

We define stochastic templates that vary in the value of distributional parameters in order to capture the commonality in layout structure across different domains. For instance, a scientific document may have a visual appearance that is totally distinct from a corporate report, yet the documents within the scientific domain may have common patterns. The templates help encode the intra-domain similarity by sharing the same hyper-parameter values for a variable, while the inter-domain similarity is simulated by using unique values across the templates.

The variables that govern the composition of a document are sampled from this Bayesian Network and rendered as an image to produce a synthetic document. The bounding boxes of the layout elements and their corresponding category are recorded during the generative process, thereby creating an implicitly annotated document. This formulation of automatic document synthesis using a Bayesian Network has the following advantages:

- The distributional characteristics of the generative process capture the complex variations in layout, style, content, structure and even abnormalities that are typical in the wild.
- The definition of stochastic templates offer a mechanism to customize for domain specific visual appearances and extend to new unseen domains.
- The hierarchical nature of the priors provides flexibility in learning from data, bias towards a-priori beliefs and focus on discriminative features.
- The causal well-defined structure of the network can cheaply produce massive quantities of coherent and realistic documents, without the need for expensive infrastructure.

# 3.2 Generative Process 

A Bayesian Network $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ is a directed acyclic graph with $\mathcal{V} \in\left\{v_{i}\right\}_{i=1}^{N}$ being the set of random variables represented as graph nodes and $\mathcal{E}$ being the set of edges that define the parent-child relationship between any two nodes. The random variables may be discrete or continuous, observed or latent and potentially multivariate. We use small letters such as $x$ to represent a latent random variable and capital letters such as $X$ to denote an observed variable. Indicators are a special type of latent variable that provides an index over the possible values of a discrete variable and are referred as $z_{x}$. The parameters that govern the prior distribution of a variable uses subscript zero. Thus $x_{0}$ is the set of (hyper) parameters for $x$. We embed these parameters within the classical notation of a distribution - for example, if $x$ is distributed as a Gaussian, then we write $\mathcal{N}\left(\mu_{x_{0}}, \sigma_{x_{0}}^{2}\right)$. Finally, $\mathbb{N}_{x}$ denotes the number of times a variable $x$ is repeatedly sampled while $N_{x}$ is the number of possible values of a discrete variable $x$.
For exposition convenience, we decompose the network into a set of subnetworks $\mathcal{G}=\left\{g_{1} \cup \ldots \cup g_{j} \cup \ldots \cup g_{J}\right\}$ where each $g_{j}$ defines a network fragment. Typically, there is a separate subnetwork for each of the layout element. While the variables are not shared between the element subnetworks, it may share variables that are common to a document. Figure 2 provides a cross-section of the network with emphasis on the document and section subnetworks.

### 3.2.1 Document Subnetwork

The generative process for a document $d$ proceeds as follows:

1. Sample template: Let $t \in \mathbb{R}^{N_{t}}$ be a set of multinomial probabilities over $N_{t}$ different templates and be Dirichlet distributed with parameters $\alpha_{t_{0}} \in \mathbb{R}^{+}$. Choose a template $z_{t, d}$ as

$$
\begin{aligned}
t_{d} & \sim \operatorname{Dir}\left(\alpha_{t_{0}}\right) \\
z_{t, d} & \sim \operatorname{Mult}\left(t_{d}\right)
\end{aligned}
$$

Each template defines a unique set of parameters for a given prior distribution i.e. there are $N_{t}$ values for an $x_{0}$. In the following, the template index $z_{t, d}$ is used to select the hyper-parameter corresponding to a document as $x_{0, z_{t, d}}$.
2. Sample document level variables: The variables such as margin, number of columns and background color influence the overall visual of a document, and are applicable at a document level. Let $\mu_{m}$ and $\sigma_{m}^{2}$ be the mean and variance of a real valued margin variable $m$. Let $\mu_{m}$ be bestowed a normal prior with mean $\mu_{m_{0}}$ and variance $\sigma_{m_{0}}^{2}$, and $\sigma_{m}^{2}$ with an inverse gamma prior parameterized in terms of shape $a_{m_{0}}$ and scale $b_{m_{0}}$. Choose a margin $M_{d}$ as

$$
\begin{aligned}
\mu_{m, d} & \sim \mathcal{N}\left(\mu_{m_{0}, z_{t, d}}, \sigma_{m_{0}, z_{t, d}}^{2}\right) \\
\sigma_{m_{d}}^{2} & \sim \operatorname{InverseGamma}\left(a_{m_{0}, z_{t, d}}, b_{m_{0}, z_{t, d}}\right) \\
M_{d} & \sim \mathcal{N}\left(\mu_{m, d}, \sigma_{m, d}^{2}\right)
\end{aligned}
$$

Similarly, let $c$ be a discrete variable representing the different choices for number of document columns. The observed column value in a document is sampled as

$$
\begin{aligned}
c_{d} & \sim \operatorname{Dir}\left(\alpha_{c_{0, z_{t, d}}}\right) \\
C_{d} & \sim \operatorname{Mult}\left(c_{d}\right)
\end{aligned}
$$

The sampling of background follows the same procedure as $C$.
3. Sample shared variables: Variables are shared across the subnetworks to provide an opportunity to maintain a consistent look and feel across the document, while retaining the option of customization with subnetwork specific overrides. These shared variables include font name, font size and text color. The discrete variables font name and text color are sampled similar to (3). The font size variable follows a two parameter exponential distribution that in general discourages large sized fonts. Let $\phi^{s}$ be a font size variable with known location $\theta_{\phi^{s}}$ and scale $\lambda_{\phi^{s}}$, which is Gamma distributed with shape $a_{\phi_{0}^{s}}$ and scale $b_{\phi_{0}^{s}}$. Choose a positive real-valued font size for the document as

$$
\begin{aligned}
\lambda_{\phi^{s}, d} & \sim \operatorname{Gamma}\left(a_{\phi_{0}^{s}, z_{t, d}}, b_{\phi_{0}^{s}, z_{t, d}}\right) \\
\Phi_{d}^{s} & \sim \operatorname{Exp}\left(\theta_{\phi^{s}}, \lambda_{\phi^{s}, d}\right)
\end{aligned}
$$

4. Sample single instance elements: Let $h$ be a Bernoulli random variable that denotes the probability of a header element with a Beta prior parameterized in terms of shape $a_{h_{0}}$ and scale $b_{h_{0}}$. The presence of a document

header is sampled as

$$
\begin{aligned}
h_{d} & \sim \operatorname{Beta}\left(a_{h_{0}, z_{t, d}}, b_{h_{0}, z_{t, d}}\right) \\
z_{h, d} & \sim \operatorname{Ber}\left(h_{d}\right)
\end{aligned}
$$

Similarly, the presence of other elements such as footer $f$ and title $\tau$ that occur only once in a document are sampled. When an element is present in the document, the subnetworks corresponding to the element are instantiated and sampled.
5. Sample multi-instance elements: Let $\zeta$ be a discrete variable that represents the elements such as section, table, figure, paragraph, bullet, equation etc. that can occur multiple times in a document. First sample the probabilities of these elements in a document from its Dirichlet prior and then repeatedly sample an element as follows:

$$
\begin{aligned}
\zeta_{d} & \sim \operatorname{Dir}\left(\alpha_{\zeta_{0, z_{t, d}}}\right) \\
z_{\zeta_{d, n}} & \sim \operatorname{Mult}\left(\zeta_{d}\right) \quad \forall n=1 \ldots N_{\zeta}
\end{aligned}
$$

where $N_{\zeta}$ is a Poisson distributed variable. The subnetwork corresponding to an element defined by $z_{\zeta_{d, n}}$ is repeatedly instantiated and sampled as described in the sequel.

# 3.2.2 Section Subnetwork 

The section subnet may be instantiated multiple times, and hence when generating a section, the variables that are shared across all sections in the document are sampled once from their priors first. These include the Dirichlet distributed font styles $\phi^{y}$, horizontal alignment $\eta$, fore color $\kappa^{f}$, back color $\kappa^{b}$, border type $\psi^{t}$ and border color $\psi^{c}$ along with the uniformly distributed continuous variables for font scale $\phi^{c}$, pre section spacing $\xi^{1}$ and post section spacing $\xi^{2}$. The above continuous variables are treated as relative values that are scaled against a base unit - for instance, the spacing after a section is a product of a base document level spacing and the post section spacing. Furthermore, a discrete variable $l$ to denote the number of lines in a section and a real valued Gaussian distributed variable $w$ for modeling the number of words in a line is introduced. Finally, we treat words as fundamental units for character blocks and maintain a pre-specified vocabulary of words with multinomial probabilities $\beta$ and sample these probabilities from a Dirichlet variable $\beta_{0}$ once per document.
The content of a section $s$ is generated by first sampling the number of lines $L$ in a section, then the number of words $W$ for each line in the section and finally the word $\Omega$ from the vocabulary.

$$
\begin{aligned}
L_{d, s} & \sim \operatorname{Mult}\left(l_{d}\right) \\
W_{d, s, i} & \sim \mathcal{N}\left(\mu_{w_{d}}, \sigma_{w_{d}}^{2}\right) \quad \forall i=1 \ldots L_{d, s} \\
\Omega_{d, s, i, n} & \sim \operatorname{Mult}(\beta) \quad \forall i=1 \ldots L_{d, s}, \quad \forall n=1 \ldots W_{d, s, i}
\end{aligned}
$$

This section specific content is rendered by applying the sampled pan-section style variables.

### 3.2.3 Table and Figure Subnetworks

A table is parameterized by its percentage of document width, alignment, borders, horizontal and vertical padding, pre and post spacing across blocks, and the number of rows and columns. We also introduce variables to define font and alignment attributes that are unique to a row, column or even a table cell. The cell dimensions are parameterized by a Dirichlet distributed variable that indicates the percentage of width for a cell and a categorical variable denoting the number of lines. Thus a cell maybe empty, has a single value or is wrapped with multiple lines. The padding variables follow an exponential distribution similar to (4) while we assign a fat-tailed Cauchy prior to the number of table rows to allow significant probability for values away from the mean. Rest of the variables follow a Dirichlet or Gaussian prior depending on whether they are discrete or continuous. A table cell content is sampled similar to equation (7).
The figures include both natural images and automatically generated synthetic images in the form of charts. For the former, we maintain a library of images and perform a uniform sampling over this library while new variables for the number of sub-plots within a chart figure, and the chart type within each sub-plot are introduced for the latter. Example chart types include bar, line, scatter, pie, heatmap etc. The chart data is generated randomly from a uniform distribution. Finally, the figure dimensions are parameterized with two continuous variables. The prior definitions follow a pattern similar to the other subnetworks.
Both the table and figure subnetworks include a caption subnet that includes variables for the caption position and content length. The text content of the caption is generated as in (7).

# 3.2.4 Other Subnetworks 

The title subnetwork follows the same procedure as listed in Section 3.2.2 except that there is only a single title per document. The distributional parameters of the variables however vary from that of the section, allowing to introduce title specific nuances.
The paragraph subnetwork introduces new variables for the number of lines in a para and the spacing between lines and across blocks. These continuous variables follow a bounded uniform distribution and are sampled each time the network is instantiated. The content in a line is sampled from a pre-defined corpus of sentences, once per line. The bullet subnetwork is similar to the paragraph, except that a discrete valued bullet type variable and a continuous bullet margin offset variable are used to simulate enumerated text.
The header (and footer) subnetwork contains additional variables for the number of columns in a header and the type of content within a column. For instance, the header may contain a 3 column layout of equal spaces with the first column containing a short logo type text, the second column containing a page number and the third column with a text denoting a running title. The above content types define their corresponding style variables for font, color and alignment and follow the procedure described in Section 3.2.2.

### 3.2.5 Defect Modeling

Documents with imperfections are common in unconstrained environments due to physical degradation and scanning errors. We simulate such low quality documents by introducing defects deliberately into the generative process. Specifically, a series of parameterized deformations corresponding to effects such as ink seepage, occlusion, shadows, blurring and damaged corners are defined and these parameters are treated as random variables as before. For instance, a digital watermark effect has variables for the text content, rotation angle and location and these variables are sampled similar to the other subnetworks.

### 3.2.6 Image Synthesis

Finally, given the set of observed values sampled from the network, an image construction library is used to draw the primitive graphical units at appropriate locations by applying the sampled style attributes. Simultaneously, the position of the corresponding layout elements are recorded. This results in a document $d$ defined on an image lattice $I_{d}$ with layout elements $\mathbf{L}_{\mathbf{d}}=\left\{\left(\iota_{i}, b b o x_{i}\right)\right\}_{i=1}^{N_{L_{d}}}$, where $N_{L_{d}}$ is the number of layout elements in document $d, \iota_{i} \in\left\{O_{1} \ldots O_{\mathbf{C}}\right\}$ is one of the $\mathbf{C}$ layout categories and $b b o x_{i} \in \mathbb{R}_{+}^{4}$ denotes a bounding box.

### 3.3 Parameter Inference

The values of the observed variables in the network can be sampled directly from the conditionals and their corresponding priors. However, it is efficient to learn these parameters offline if we have a corpus of real-world documents. We consider a partially observed network setting where we have data samples for subsets of variables and exploit the knowledge about probabilistic influences between the variables in order to perform posterior inference. Let $\mathcal{D}=\left\{\chi^{1} \ldots \chi^{M}\right\}$ be a multiset of observed data samples for $M$ different variables where $M \ll N$. Let $\Theta_{i}$ denote the parameters of the distribution of an observed variable $i$ with $\Pi_{i}$ being the parameters of its parent variable. The conditional independence of the variables encoded in the above described Bayesian Network structure results in the factorization of their joint distribution into a product of locals and consequently the posterior distribution for $i$ is given as

$$
p\left(\Theta_{i} \mid \chi^{i}\right)=\int p\left(\chi^{i} \mid \Theta_{i}\right) p\left(\Theta_{i} \mid \Pi_{i}\right) d \Theta_{i}
$$

Our specific choice of the distributions for the conditionals and their corresponding priors ensure that the posterior distribution is in the same form as the prior. Due to these conjugate priors, the posteriors can be computed in a closed form. For instance, a multinomial conditional has a Dirichlet prior with parameters $\alpha_{i_{0}} \in \mathbb{R}^{K}$, and from data samples $\chi^{i}$ we can compute $\left(N^{i 1}, \ldots, N^{i k}, \ldots N^{i K}\right)$ where $N^{i k}$ is the number of observations for a discrete variable $i$ with value $k$. The posterior parameters can now be sampled from $\operatorname{Dir}\left(\alpha_{i_{*}}\right)$ where $\alpha_{i_{*}, k}=\alpha_{i_{0}, k}+N^{i k}$. Similar analytical updates for the posteriors are available [32] for the other conditionals including a Bernoulli variable with Beta prior, an exponential variable with Gamma prior, a Gaussian variable with normal prior for the mean and inverse Gamma prior for the variance.

![img-2.jpeg](img-2.jpeg)

Figure 3: Layout Recognition Model Architecture. A feature extraction network takes an image of arbitrary size as input and produces feature maps at different scales. An object detector network determines the categories and bounding boxes of the layout elements.

# 4 Document Layout Recognition 

The goal of layout recognition is to locate the various layout elements in a rasterized document and identify their corresponding layout categories. This objective can be cast as an object detection problem, where instances of visual objects of a certain class along with their spatial location and extent are retrieved from an image. The various layout elements in the document are characterized as the objects of interest here.
Deep learning based feature representation and object segmentation have emerged as the defacto approach [3] to address the object detection problem. However, training these models require a large number of images annotated with the bounding boxes and classes of object instances. The document generator described above can cheaply produce synthetic labeled images required for training a deep learning based object detector, thereby avoiding the need for expensive annotation procedures.
The object detection model architecture used for layout recognition is outlined in Figure 3. It consists of a backbone deep ConvNet [13] that computes a feature hierarchy for a given image at several scales with multiple layers of convolutions and downsampling. This bottom-up pathway of feed-forward computations captures semantics from low to high level and facilitates scale invariance. The lower level semantics produced by this feature hierarchy is combined via lateral connections with a top-down pathway that upsamples spatially coarser but semantically stronger features. The resulting feature pyramid network [33] produces a feature map with fixed dimensions that captures high-level semantics at multiple resolution scales.
This rich multi-scale feature map is fed as input into an object detector subnetwork that performs object classification and bounding box regression. We consider two main classes of detector architectures: (i) a two stage detector in which a sparse set of candidate object locations are generated first and subsequently these candidate locations are refined and classified and (ii) a one stage detector which performs classification and regression directly on a regular dense sampling of object locations. The two-stage detector includes a region proposal network (RPN) [17] that applies convolutions to the feature map and produces bounding boxes for object proposals along with objectness scores. In addition, a region of interest (RoI) pooling layer extracts fixed length feature vector from the feature map corresponding to the object proposals. Finally, these feature vectors are fed into a sequence of fully connected networks (FCN) to determine the object classes and their bounding boxes. In contrast, the one-stage detector [18] avoids explicit region proposals and

instead considers locations across the image. It uses two parallel deep subnetworks directly on the feature map, one to predict the probability of object presence at a spatial position and another for box regression.
Given the set of synthetic document images $\mathbf{I}=\left\{I_{1} \ldots I_{N_{D}}\right\}$ and their corresponding labels $\mathbf{L}$, the layout recognition model is trained based on the above architecture. We compare in our experiments the recognition performance on real documents for different choices of the feature extractor and object detector.

# 5 Experiments 

We present the output of the generator model, outline the evaluation settings and finally discuss the layout recognition results in this section.

### 5.1 Document Generator Results

A few examples of the synthetic documents produced by the document generator is shown in Figure 4. The variety, coherence and realistic nature of the generated documents is evident. The documents have different styles corresponding to fonts, colors, borders, alignments and content lengths for the title and section headings. Not all documents contain these layout elements, mimicking mundane descriptive pages present in typical documents. The bottom part of the figure illustrates the wide range of table element representations. The table borders pertain to rows, columns, headers or individual cells for grid type appearance. The table size, number of rows and columns, density in layout and cell alignments all differ across the tables. The documents also include both natural [34,35] and synthetically generated multi-chart images. Furthermore, the documents vary in their number of columns and the presence, location and style of page numbers, running titles and marker glyphs in the header and footer elements.
It is necessary to annotate the documents at granular cell boundary level to aid in identifying the internal structure of a table. Figure 5 contains examples of documents that exclusively contain tabular format data. In addition to the typical variations for tables outlined above, they also contain many instances of wrapped cells that are important to model notions of logical blocks, required when performing table structure recognition. The variables for table width and number of columns determine the distribution of cell widths, which in turn influences the wrapping behavior of contents within a cell. Such indirect connections between the variables are explicitly modeled through the causal well-defined structure of the Bayesian network and results in diverse yet coherent visual appearances for tens of thousands of cells as illustrated in this figure.
Imperfect documents are an inevitable part of the mix in the real-world and generating such documents is important to make the training process robust to errors. Figure 6 provides some examples of such poor quality documents synthesized by the model. The document on the left simulates a dark corner possibly due to physical degradation, while the one in the middle shows a digital watermark blemish on the same document. The document on the right shows a non-linear bleed-through effect simulating the ink from verso-side of a paper seeping partially into the recto-side.
The text content in the generator model is sampled from a pre-defined corpus of sentences and vocabulary. It is possible to simply substitute with a corpus and vocabulary from another language and follow the same generative process to produce multi-lingual documents. The only constraint is that the prior specified for the font variable should be capable of representing the target language. Figure 7 provides examples of documents generated in French, Chinese and Arabic by the model.
Customizing the generation process is often required to extend support for new domains. Figure 8 shows a few synthetic resume and Figure 9 presents synthetic forms, which were generated by altering the characteristics of standard templates. For example, to cater to the resume domain, the probabilities for presence of headers and footers were set to zero, the padding scale parameter was doubled to increase the inter-spacing between table rows, unequal widths were chosen for multi-column layouts and the targets for vocabulary and figures were modified, while the other subnets largely remained the same. Similarly, for the forms domain the table element was customized to sample pairs of questions and answers with the content derived from [36]. This illustrates the flexibility of the model to cater to domain specific visual layouts by sharing common themes and deviating when necessary.

### 5.2 Sampling Characteristics

It is important to examine the characteristics of the variables sampled from the generator. Table 1 shows the distribution of the layout categories for 10,000 documents produced by the generative process. It contains both the number of times a particular layout category appears in a document and the overall number of instances of a category, which includes potentially multiple occurrences of a category within the same document. For instance, a document may contain only a single instance of title category while it may contain multiple sections.

![img-3.jpeg](img-3.jpeg)

Figure 4: Examples of synthetic documents. The generated documents differ widely in their layout, style, structure, content and composition. See the Section elements in (a), (b) and (c), the Table elements in (d) and (e), the Figure elements in (d) and (f), the Equation elements in (e) and the Header/Footer elements across all the documents.

![img-4.jpeg](img-4.jpeg)

Figure 5: Synthetic tabular data used for training cell recognition. The cells vary in width, height, alignment, border, color etc. A sample cell bounding box is highlighted for illustration.

![img-5.jpeg](img-5.jpeg)

Figure 6: Low-quality noisy documents generated to simulate defects due to physical degradation, ink seepage and scanning errors. left: Uneven background. middle: Digital watermarking. right: Bleed-through effect.

![img-6.jpeg](img-6.jpeg)

Figure 7: Multi-lingual Synthetic Documents. left: French. middle: Chinese. right: Arabic.

Table 1: Layout categories distribution in synthetically generated documents.


![img-7.jpeg](img-7.jpeg)

Figure 8: Synthetic documents generated for Resume domain.
![img-8.jpeg](img-8.jpeg)

Figure 9: Synthetic documents generated for Forms domain.

The distributions for a few observed document variables sampled by the generator is shown in Figure 10. The top section includes a set of discrete variables with a weak concentration for their Dirichlet prior parameters. This results in an asymmetry in the sampled values. For instance, the Bold-Italic font occurs less frequent than other font types. Similarly, the probability of colorful headers or a left aligned page number is lower than their peers. In contrast, the middle section shows variables with a uniform distribution over their possible set of values. The bottom section shows the distribution for a few continuous variables including a Gaussian structure for the number of words per line, a fat-tailed Cauchy density that is skewed for the number of table rows and an exponential decay behavior for the table padding. Thus the sampled values reflect different classes of distributions, which is typical in real world documents.

# 5.3 Evaluation Data and Settings 

We use three publicly available datasets to evaluate the performance of a layout recognition model trained with synthetic documents. The PubLayNet [6] dataset specifically caters to document layout analysis and contains annotated bounding boxes and labels for layout categories such as sections, tables and figures in a document image. It uses a predefined schema in the XML version of the documents in PubMed Central ${ }^{\mathrm{TM}}$ to determine the annotations. The DocBank [7] is a similar benchmark dataset for document layout analysis. It uses the markup tags in the LATEXsystem to recover

![img-9.jpeg](img-9.jpeg)

Figure 10: Distribution of sampled document variables. top: Apriori bias for a subset of values. middle: Uniform distribution over the simplex of possible values. bottom: Histograms reflecting Gaussian, Cauchy and Exponential densities.

Table 2: Prediction results - DocBank dataset.


fine-grained labels such as abstract, author, reference and section in research papers uploaded to arXiv.com. In order to evaluate table structure recognition, we use the PubTabNet [8] dataset. It contains images of heterogeneous tables extracted from scientific articles and contains annotated bounding boxes of the table cells.

We normalize the labels to three main layout categories for consistency: sections (which include document titles), tables and figures for the PubLayNet and DocBank datasets and table cells for the PubTabNet dataset. We perform evaluation on about 5000 documents from these datasets. For comparison purposes, we train the layout recognition model separately both on synthetic and real documents with 10,000 examples. In all the cases, the model fine-tunes the weights of pre-trained object detection models, and is trained for 3 epochs using a stochastic gradient descent optimizer with a learning rate of 0.0025 , momentum of 0.9 and a weight decay of 0.0001 . We use an 8 GPU NVIDIA Tesla V100 instance and an effective batch size of 16 images. We do not apply any transforms on the document images and use them as is as input to the object detector.

Table 3: Prediction results - PubLayNet dataset.


Table 4: Prediction results - PubTabNet dataset.


Table 5: Performance difference between real and synthetic documents for different object detection architectures.


# 5.4 Layout Recognition Results 

The prediction results for layout recognition on the DocBank dataset, both for a model trained on real documents from this dataset and a model trained purely on synthetic documents is shown in Table 2. The precision and recall of a layout category depends on the overlap of the bounding boxes between the prediction and ground truth, with the former accounting for false positives and the latter for false negatives. The difference in F1 scores between the real and synthetic are $4.6 \%$ for the sections, followed by $3.8 \%$ for the tables and $2.7 \%$ for figures with an average of $3.7 \%$.

Table 3 presents the layout recognition performance on the PubLayNet dataset in a similar format as DocBank. Here the difference in F1 scores are $5.8 \%, 4.7 \%$ and $0.5 \%$ for the sections, tables and figures respectively, with an average difference of $3.6 \%$. Both the PubLayNet and DocBank datasets contain documents from scientific publications, and hence the similarity in results are unsurprising. These datasets do not contain granular table cell level annotations, and hence we evaluate the performance of table cell recognition on the PubTabNet dataset and present the results in Table 4. There is only a marginal difference in cell recognition between the detector models trained on real and synthetic tables.
We also compare the performance of the layout recognition model for different feature extraction and object detection frameworks to ascertain whether the synthetic document based training is preferable only for particular types of network architectures. Table 5 presents the difference in F1 scores between the real and synthetic models trained for Resnet [13], Resnext [37], Mobilenet [38] and VGG [12] backbones in combination with FasterRCNN [17], Retina [18] and SSD [39] for object detection. In general the 50 layers deep Resnet backbone performs the best, with similar performance for both two-stage and one-stage detectors. It is noteworthy that the ResNext/FasterRCNN performance is not very far from best performing combinations even though it didn't contain pre-trained weights for an end to end object detector for this combination.
While the above results highlight the autonomous utility of synthetic data, we also evaluate a semi-synthetic scenario in which the generated documents are used for data augmentation. We mix the synthetic documents with real ones and measure whether their inclusion can improve the layout detection task. Table 6 compares the F1 scores for layout detection in PubLayNet using only real documents and augmenting them with 10,000 additional documents generated by our model and a baseline model [26] that uses arbitrary arrangement of the elements. Our model improves over both these, illustrating its applicability for data augmentation tasks and the benefit of a principled generation approach.
Finally, we assess the structural similarity between a real and synthetic document by comparing the spatial layout of their elements. We follow the metrics in [30] and calculate the percentage of overlapping area among any two elements in a document and the alignment index of all the bounding boxes. Additionally, we compare the average number of layout elements in a document. The difference in these values between the real and synthetic documents, along with

Table 6: Usefulness of synthetic documents for data augmentation on layout detection task.


Table 7: Structural similarity analysis between real and synthetic documents.


![img-10.jpeg](img-10.jpeg)

Figure 11: Layout recognition results on scientific documents. Bounding boxes of predictions are highlighted with Section as SEC in blue, Figure as FIG in red, Table as TBL in green and Header/Footer as H/F in gray. the intersection over union of the layout elements for various categories in PubLayNet is shown in Table 7. The low numbers for differences and the high IoUs indicate a greater similarity in the layout space.

# 5.5 Qualitative Analysis 

We include in Figure 11 example predictions on the real documents from the layout recognition model trained on synthetic documents. The annotated bounding boxes and categories are largely inline with expectations. In order to assess the quality of layout recognition on non-scientific documents, we also perform inference on a few publicly available legal reports ${ }^{1}$ and present them in Figure 12. It is interesting that in the middle figure, the model was able to detect a table even in the absence of border cues. The predicted bounding boxes of table cells is shown in Figure 13. The detector successfully groups text blocks that span across columns (see left figure) and rows (see right figure).

We also perform error analysis to understand the reasons for incorrect predictions. Figure 14 highlights the layout elements that were not recognized by the model. A few ground-truth annotations had arguably incorrect layout categorization. Section headings that lack reasonable gaps and rotated tables with colorful background are not picked up by the model. In addition, block diagrams and algorithmic text marked as figures are not recognised. Some of these errors can be addressed by improving the document generator model to include these variations.

[^0] [^0]: ${ }^{1}$ www.cov.com, www.davispolk.com

![img-11.jpeg](img-11.jpeg)

Figure 12: Prediction results on real-world legal documents. Bounding boxes of predictions are highlighted with Section as SEC in blue, Figure as FIG in red, Table as TBL in green and Header/Footer as H/F in gray.



![img-12.jpeg](img-12.jpeg)

Figure 14: Error analysis. Incorrect predictions are highlighted in red. (a): Invalid Section annotation. (b): Sections with regular font style and closely spaced text at the bottom are not recognized. (c): Detection error for rotated tables with non-white background. (d). Figures annotated as Tables. (e): Text blocks annotated as Figures are ignored. (f): Block diagrams are not identified as Figures.
![img-13.jpeg](img-13.jpeg)

Figure 15: Training size impact. As the number of synthetic documents increases, the performance difference between the real and synthetic training models decrease.

Table 8: Impact of training with a subset of layout categories.


![img-14.jpeg](img-14.jpeg)

Figure 16: Interpreting the layout detection model. Important regions in the image for predicting a layout category is highlighted. (a): Large text fonts support Title identification. (b): Spacing appears to be an important cue to discriminate Section classes. (c): Positional information drive Header/Footer detection. (d): Vertical alignments and horizontal strokes influence Table recognition. (e): Irregular stroke patterns possibly define Figure categories. (f): Relative spaces from the margins help decide Equations.

values at the final convolutional layer of the feature map. These forward activation maps are then combined with the gradient of the target category acting as weights. This localization map is plotted on the document image as a heatmap and the resulting figure helps in interpreting the reasons for a prediction.
It can be observed in the top left figure that fonts are a key attribute for identifying titles, with a dominant emphasis on large sized text and some attention on the bold text for ABSTRACT and KEYWORDS. It is interesting that spaces are critical for discriminating sections and equations as highlighted in figure (b) and (d). The importance of complex patterns to understand illustrations (see (e)) or the locations for header and footer (see (c)) is unsurprising. Vertically aligned text appears to play a crucial role in identifying tables. Overall, these explanations can assist in quantifying the importance of the various variables used by the document generator.

# 6 Conclusion 

We presented a principled approach for document generation that can cheaply produce coherent and realistic document images along with labels required for layout recognition. The hierarchical Bayesian Network formulation of the generation process allows capturing complex logical structures and models the diversity of documents observed in unconstrained real-world settings. These synthetic documents can be used in lieu of real documents for training deep object detectors, thereby side-stepping expensive annotation exercises. Our quantiative, qualitiative and interpretable experimental analysis confirm the efficacy of our proposed approach. In the future, we wish to learn the Bayesian Network topology to automatically capture the conditional dependencies, extend the model to a more granular categorization of the layout elements and quantify the relative importance of layout recognition for document understanding tasks.

## Acknowledgments

This paper was prepared for information purposes by the Artificial Intelligence Research group of JPMorgan Chase \& Co and its affiliates ("JP Morgan"), and is not a product of the Research Department of JP Morgan. J.P. Morgan makes no representation and warranty whatsoever and disclaims all liability for the completeness, accuracy or reliability of the information contained herein. This document is not intended as investment research or investment advice, or a recommendation, offer or solicitation for the purchase or sale of any security, financial instrument, financial product or service, or to be used in any way for evaluating the merits of participating in any transaction, and shall not constitute a solicitation under any jurisdiction or to any person, if such solicitation under such jurisdiction or to such person would be unlawful. (C) 2021 JP Morgan Chase \& Co. All rights reserved.
