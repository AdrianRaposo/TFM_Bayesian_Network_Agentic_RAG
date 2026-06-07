# Marco Ramoni: an appreciation of academic achievement 

Isaac S Kohane, ${ }^{1}$ Peter Szolovits ${ }^{2}$

- Additional materials are published online only. To view these files please visit the journal online (www.jamia.org).
${ }^{1}$ Harvard Medical School, Children's Hospital Informatics Program, Boston, Massachusetts, USA
${ }^{2}$ MIT Computer Science and Artificial Intelligence Laboratory, Cambridge, Massachusetts, USA


## Correspondence to

Dr Peter Szolovits, MIT
Computer Science and Artificial Intelligence Laboratory, 32 Vassar Street, Cambridge, MA 02139, USA; psz@mit.edu

Received 28 February 2011
Accepted 22 March 2011
Published Online First
7 April 2011

## ABSTRACT

We review the scholarly career of our colleague, Marco Ramoni, who died unexpectedly in the summer of 2010. His work mainly explored the development and application of Bayesian techniques to model clinical, public health, and bioinformatics questions. His contributions have led to improvements in our ability to model behavior that evolves in time, to explore systematic relationships among large sets of covariates, and to tease out the meaning of data on the role of genetic variation in the genesis of important diseases.

The untimely and unexpected death of Dr Marco Ramoni in June 2010 deprived our community of an exciting and productive voice. It is fitting that AMIA has chosen to award a paper prize in his honor at the annual Summit on Translational Bioinformatics. Here, we wish to summarize Dr Ramoni's contributions to our technical field, to explain the significance of the honor that is being bestowed in his name.

Dr Ramoni's formal education was at the University of Pavia in Italy, where he obtained his Bachelor's degree in Logic and Philosophy of Science in 1987 and his PhD in Biomedical Engineering in 1993, ${ }^{1}$ under the supervision of Dr Mario Stefanelli. From 1993 to 1995, he was a postdoctoral fellow in Dr Vimla Patel's laboratory at McGill University. From 1995 to 1999 he served as a Research Fellow at The Open University in the UK, during which time he also held brief appointments at the University of London and the University of Massachusetts at Amherst. He joined Harvard Medical School in 2000, advancing through the ranks of Instructor, Assistant Professor and Associate Professor, and also served on the Harvard-MIT Health Sciences and Technology (HST) Division's faculty from 2005. He was also a staff scientist at Children's Hospital Boston, Associate Director of the Harvard Partners Center for Genetics and Genomics, and Director of the Children's Hospital branch of the Boston-area Biomedical Informatics Research Training Program. He served on the editorial boards of four journals, was Associate Editor of BMC Genomics, and had been a reviewer for dozens of journals and conferences, including the AMIA Summit on Translational Bioinformatics, where he was a member of the scientific program committee. Dr Ramoni was also principal investigator (PI) of various NIH grants, exploring gene expression control, genetic predictors of nicotine dependence, pharmacogenomics of asthma treatment, control of RNA expression, and modeling of ischemic stroke. He participated in other research efforts in the areas of translational
bioinformatics, integration of biomedical knowledge, and information-theoretic methods to identify quantitative trait loci from functional and structural genomic information. Dr Ramoni was a popular lecturer in many Harvard and MIT classes, and for the last 5 years had been co-director of the biomedical computing class offered jointly by HST and the MIT Department of Electrical Engineering and Computer Science. He had supervised four HST doctoral students, two master's students, and numerous research fellows. Dr Gil Alterovitz, one of those doctoral students, won the AMIA Martin Epstein award for his 2006 paper describing the principal results of his dissertation. ${ }^{3}$

Dr Ramoni published four books ${ }^{4-6}$ and was working on a new textbook in biomedical informatics with Drs Alterovitz and Szolovits at the time of his death. Starting in 1989, he had published over 75 peer-reviewed papers, with more still appearing posthumously, 37 conference papers, and 20 book chapters. He and his wife Rachel were nearing completion of their first work of fiction.

The touchstone of Dr Ramoni's work and his passionate intellectual theme was the use of Bayesian network methods to describe natural phenomena. ${ }^{37}$ Early in his career, this interest led him to develop techniques for efficient probabilistic reasoning under ignorance, which provided exciting theoretical results extending the Bayesian network and influence diagram literature, ${ }^{8}$ as well as applications to problems such as the prediction of future blood glucose concentrations in diabetic patients ${ }^{9}$ and, later, outcomes for intensive care patients. ${ }^{10}$ With Dr Paola Sebastiani and others, Dr Ramoni developed a series of elegant methods to model complex time-dependent phenomena with Markov and Bayes models. ${ }^{1112}$ One of their approaches assumes that, for modest lengths of time, the behavior of a system may be described as a Markov transition model. However, over longer spans, other models, with other dynamics, may take over and generate the visible behavior of the system. The learning problem in such a world requires the ability to identify clusters of behaviors that exhibit similar dynamics, which might then be collapsed into one of the short-term Markov models, plus a scheme to identify the most likely points of transition among these clusters and the related transition probabilities. ${ }^{13}$ Of course all this must be done in the face of missing data, noise, fundamental variability in the system, ${ }^{14}$ and the need for reasonable approximations to limit the complexity of the learning problem. Their approach integrates these two tasks in a Bayesian optimization framework. The method has been applied not only to clinical conditions, but also to building models in

genomics, robot behavior, and even detection of compromised activity in a computer server. Dr Ramoni was also vitally interested in understanding medical reasoning according to formal models from epistemology, with Dr Stefanelli, ${ }^{1}$ and from cognitive science, with Dr Patel. ${ }^{15}$

When Dr Ramoni joined the Children's Hospital Informatics Program and the faculty of Harvard Medical School, he readily admitted to knowledge of biology and genetics in particular that did not go any further than that of the popular, lay literature. Remarkably, in the space of 10 years Dr Ramoni published over 50 articles mostly in the domain of bioinformatics and genomescale analyses, many of these ground-breaking and appearing not only in the top methodological journals but also in the leading biological investigation journals. In the realm of transcriptional analysis, Dr Ramoni pioneered a Markovian clustering by time of thousands of mRNA expression signatures, ${ }^{16}$ this at a time when most analyses even of time series did not capture this important temporal element. When others looked for conservation or for biochemical change as a clue as to the pathogenicity of single nucleotide polymorphisms, Dr Ramoni used an integrative Bayesian technique to include not only these measures but also experimental assessments of the effects of changes in viral genomes in order to better estimate the probabilities of pathogenicity. ${ }^{17}$ Dr Ramoni repeatedly emphasized in his publications and with his collaborators the importance of prediction not only as a clinically useful tool but as a scientifically grounding figure of merit in assessing models of pathogenicity. ${ }^{18-26}$ He applied this approach to the transcriptional profile of invasiveness of cancer cells, ${ }^{27}$ to the prognosis of epithelial ovarian cancer, ${ }^{28}$ and to refractory periodontitis. ${ }^{29}$

Most revolutionarily, at a time when as a community we were in the midst of evaluating single SNPs for their implications in human disease, Dr Ramoni was obtaining predictive models across a multiplicity of SNPs. This was most evident in his predictive models of stroke in patients with sickle cell disease ${ }^{25}$ and artherosclerotic disease. ${ }^{22}$ These early efforts have been succeeded by dozens of others following in his large footsteps. In addition to clinical prediction, Dr Ramoni applied similar techniques to dissect out the regulatory networks in determining muscle differentiation, ${ }^{2930}$ the feedback loops governing cell cycle, ${ }^{3132}$ and the cellular toxicities of chemotherapeutic agents. Although his focus was on genomic medicine, this did not stop him from productively contributing to many other domains in the biomedical informatics arena. For example, he contributed to an information theoretic reformulation of a multiplicity of ontologies in a way that allowed for sound computation of enrichment calculations in genetic analyses as well as enforcing semantic coherence. ${ }^{3334}$ He applied his predictive techniques also to predicting the course of asthma patients from medical record data, ${ }^{293536}$ influenza spread in populations from emergency room data, ${ }^{36}$ and early and cost-effective identification of unsuccessful and potentially successful drug trials from early trial data. ${ }^{37-39}$ In addition to this scholarly pioneering, Dr Ramoni left a legacy of grateful trainees in this new domain of probabilistic bioinformatics with a remarkable 20 of these trainees over the last 10 years, many of whom are already in junior faculty positions at leading institutions. His engineeringinformed approach to biomedical investigation set important directions for our field and lives on in the careers of his students and his productive publication record. ${ }^{1}$

[^0]
## Competing interests None.

Provenance and peer review Not commissioned; internally peer reviewed.

# Obituary 

## In Memoriam: Darlene P Vian

Darlene LeMay Pearson Vian, 78, of Palo Alto, California passed away on February 9, 2011. Ms Vian worked at the Stanford University Medical School for over 37 years. She was Secretary of the Faculty Senate for nearly 10 years. She was hired in 1980 by Ted Shortliffe to help establish the MS/PhD program in
![img-0.jpeg](img-0.jpeg)

Darlene Vian, 1932-2011

Biomedical Informatics and soon discovered that working with students was her true calling. As Student Services Administrator, she managed recruiting, admissions, degree programs, traineeships, social events at her home, the annual retreat at Asilomar Conference Grounds, and alumni relations, including an annual alumni banquet. Perhaps her greatest contribution came as an advisor to the students, helping them deal with issues of funding, coursework, thesis writing, deciding whether to leave school early, and personal problems. She was largely responsible for the esprit and positive experience that two generations of graduate students enjoyed. As an example of her unstinting devotion, she was still consulting to the program one week before her death. In recognition of her incredible work, Ms Vian was awarded the Stanford Graduate Service Award in 1999.

Darlene was an exceptional woman who touched the lives of many members of JAMIA's editorial team, authors, and reviewers.

## Brian P McCune, Edward H Shortliffe

Correspondence to Brian P McCune, Cyladian Technology Consulting, 825 Oak Grove Avenue, Suite D101, Menlo Park, CA 94025-4427, USA; mccune@cyladian.com
Competing interests None
Provenance and peer review Internally peer reviewed
J Am Med Inform Assoc 2011;18:369. doi:10.1136/amiajnl-2011-000352