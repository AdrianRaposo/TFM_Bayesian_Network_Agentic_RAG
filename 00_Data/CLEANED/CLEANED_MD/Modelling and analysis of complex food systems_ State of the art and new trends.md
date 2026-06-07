# Modelling and analysis of complex food systems: State of the art and new trends 

Nathalie N. Perrot, Ioan-Cristian I.-C. Trelea, Cédric C. Baudrit, Gilles Trystram, P. P. Bourgine

## To cite this version:

Nathalie N. Perrot, Ioan-Cristian I.-C. Trelea, Cédric C. Baudrit, Gilles Trystram, P. P. Bourgine. Modelling and analysis of complex food systems: State of the art and new trends. Trends in Food Science and Technology, 2011, 22 (6), pp. 304 - 314. 10.1016/j.tifs.2011.03.008 . hal-01000973

## HAL Id: hal-01000973 <br> https://hal.science/hal-01000973v1

Submitted on 12 Jul 2017

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

2 Modelling and analysis of complex food systems: state of the art and new trends

4 Authors
5 Perrot N. ${ }^{\mathrm{a}}$, Trelea, I.C. ${ }^{\mathrm{a}}$, Baudrit, C. ${ }^{\mathrm{a}}$, Trystram, G. ${ }^{\mathrm{b}}$, Bourgine, P. ${ }^{\mathrm{c}}$

6

7 Affiliations
$8{ }^{a}$ UMR782 Génie et Microbiologie des Procédés Alimentaires. AgroParisTech, INRA, 78850
9 Thiverval-Grignon, France (Tel.: +331-30-81-53-79; fax : +331-30-81-55-97; email:
nathalie.perrot@grignon.inra.fr.cedric.baudrit@grignon.inra.fr, cristian.trelea@agroparistech.fr)

12
$13{ }^{\text {b }}$ UMR GENIAL. AgroParisTech, INRA 1 avenue des Olympiades 91744 MASSY Cedex, 14 France (tél : $+331 \quad 69 \quad 93 \quad 50 \quad 69$; fax : $+331 \quad 69 \quad 93 \quad 51 \quad 85$; email: 15 gilles.trystram@agroparistech.fr).

16
${ }^{\text {c }}$ ISC PIF (Institut des Systèmes complexes Paris Ile de France), UMR 7656, C R E A. Centre 18 de Recherche en Épistémologie Appliquée. École Polytechnique/CNRS, 32, boulevard Victor 19 - 75015 Paris, France (Tél. +331 45526411 - Fax : +331 455264 55, email : paul.bourgine@polytechnique.edu)

# Abstract 

The aim of this review is twofold. Firstly, we present the state of the art in dynamic modeling and model-based design, optimization and control of food systems. The need for nonlinear, dynamic, multi-physics and multi-scale representations of food systems is established. Current difficulties in building such models are reviewed: incomplete, piecewise available knowledge, spread out among different disciplines (physics, chemistry, biology, consumer science) and contributors (scientists, experts, process operators, process managers), scarcity, uncertainty and high cost of measured data, complexity of phenomena and intricacy of time and space scales. Secondly, we concentrate on the opportunities offered by the complex systems science to cope with the difficulties faced by food science and engineering. Newly developed techniques such as model-based viability analysis, optimization, dynamic Bayesian networks etc. are shown to be relevant and promising for design and optimization of foods and food processes based on consumer needs and expectations.

## 38 Introduction

Food engineering covers a large spectrum of applications that include, but are not limited to: product engineering, process engineering, control, optimisation and decision support systems. Some 25 years ago, modelling and simulation of food processing was mostly dedicated to product preservation with safety considerations, most of the studies focused on timetemperature diagrams for predicting and limiting residual spores or micro-organisms in foods. Due to increased process understanding and computing power, applications emerged where

other quality attributes were considered: moisture content, colour, viscosity, sometimes food composition. More recently, food structure was also considered (e.g. viscosity, porosity) and models became available to represent the evolution of such structure (Theys, Geeraerd \& Van Impe 2009). In parallel, progress in observation and analytical methods (imaging techniques, magnetic and electronic beams) allowed investigating different structural scales and interactions between chemical species, mainly between macromolecules and small molecules. Food starts to be viewed as a complex system, with various possible interactions between key variables at different scales (from nano scale to macroscopic one) (Baudrit, Sicard, Wuillemin \& Perrot 2010).

It is now recognised in most scientific domains that dynamic modelling and computer simulations are valuable tools for product and process understanding, design, optimisation and control. The purpose of a mathematical model is to capture relevant features (in a given context) of a complex object or process, based on existing theoretical understanding of the phenomena and available measurements. Current industrial applications usually rely on extremely simplified, stationary models that cannot produce a realistic evaluation of transient effects on plant performance, quality and safety conditions and environmental impact. The modelling and simulation research efforts should be directed towards main phenomenological aspects, coupling different scales, such as heat, mass, momentum, population balance coupled with chemical reactions.

Design of new foods as 'intelligent' vectors for target molecules responsible for nutritional or sensory properties became a major goal for food industry. These target molecules can be sapid or aroma compounds, micro-nutriments or microorganisms of interest (technological

flora used in the fermented products) whose controlled release or digestion satisfies physiological objectives of bioavailability. E. Windhab suggested in 2004 an integrating concept (PIECE: Preference, Acceptance Need) taken over by the platform 'Food for life', expressing the need to establish a compromise between all these properties. Up to now, few studies were able to work in a such a complex design space. Existing reverse engineering publications focus either on safety or sensory questions. Sustainability and environmental impact are additional factors to be taken into account.

The emerging field of complex systems science, situated at the crossroads of mathematics and artificial intelligence (cf. the living roadmap for complex system http://cssociety.org/tikidownload_wiki_attachment.php?attId=123), develops methods and tools to comprehend and describe instable and changing environments, systems that evolve and adapt through internal and external dynamic interactions and are not predictable within a conventional scientific framework. Our thesis is that techniques developed in complex systems science are applicable and useful to tackle difficulties encountered in food systems.

# Understanding and modelling of complex food systems: state of the art 

Model-based approaches in food science, technology and engineering have received great attention during the past three decades (Banga, Balsa-Canto \& Alonso, 2008; Datta, 2008; Sablani, Datta, Rahman \& Mujumdar, 2007) and numerous academic works have been dedicated to modelling and its applications (Bimbenet, Schubert \& Trystram, 2007). The demand for models is now clearly established; as an example, the European Food for Life

platform (www.ciaa.be) presents modelling as a key tool for the development of European food Industries. Compared to chemical engineering, where modelling is now part of virtually any scientific and technical development, food engineering follows a similar trend, with considerable ( $\sim 20$ years) delay. In the authors' view, one of the main reasons for this delay is the increased complexity of food systems, including physical, chemical and biological phenomena on a wide range of time and space scales (Georgakis, 1995; Perrot, Bonazzi \& Trystram, 1998; Christakos, 2002; Banga et al., 2008).

# Dynamic models for food systems 

This review makes a particular emphasis on dynamic models, able to describe transient process operation. Typical examples are batch processes, which always operate in transient state. For continuous processes, optimising start-up, shutdown or recipe change regimes can be important for reducing costs and environmental impact. On-line control of continuous processes also require dynamic models for unavoidable disturbance compensation, such as variations in raw materials (Trystram \& Courtois, 1994).

First principles vs. data-driven models
When modelling approach is primarily guided by the knowledge of the underlying mechanisms, the resulting model is usually termed as 'first principles' or 'white box'. Classical examples include heat, mass and momentum transfer, chemical and biochemical conversions, etc. The scales covered by first principles range from atomic to macroscopic ones. A lot of innovative work today is dedicated to micro and meso scale. As an example,

SAFES (Fito, LeMaguer, Betoret \& Fito, 2007) illustrates the use of thermodynamics to understand the evolution of food during processing. Multiphase approaches viewed as a general background by Datta (2008) cover similar scales. Available molecular tools become increasingly relevant for food matrices but the connection with macroscopic scales remains difficult.

In contrast with first principles, empirical 'data-driven' or 'black-box' models describe observed tendencies in experimental data by arbitrary mathematical functions such as polynomials or artificial neural networks (ANN). Quick and easy-to-use when sufficient experimental data is available, such models also encounter important limitations when applied to food systems: risk of over-parameterisation, interpretation difficulty, lack of generalisation ability when food composition or process parameters are changed outside the range of the initial experimental design (Banga et al., 2008). Last but not least, the number of required measurements increase exponentially with the number of studied factors.

A quite efficient intermediate approach consists in designing a model structure based on first principles and complete missing information by empirical relationships derived directly from experimental data. Such models are sometimes called 'grey box'. A dynamic research field is the development of artificial intelligence-based approaches (Linko, 1998; Davidson, 1994; Allais, Perrot, Curt \& Trystram, 2007) taking into account the human expert knowledge. Many applications especially for food quality control (for a review see (Perrot et al., 2006)) were reported, mostly based on the theory of fuzzy sets. Nevertheless, the bottleneck of these approaches is the difficulty to capture the dynamic of the system using the expert knowledge. This difficulty was also pointed out by the community of cognitive science (Hoffman,

132 Shadbolt, Burton \& Klein, 1995; Farrington-Darby \& Wilson, 2006).

133
$134[$

Building of the food models
137 A typical approach for model development is schematically shown in Figure 1. On the basis of literature review, previous scientific or expert background and experimental evidence, a first set of hypothesis, mechanisms, state variables and parameters is defined. Generally, one space and/or time scale is explicitly taken into account. Other scales are usually lumped into some apparent or average material properties. Uncertainty is rarely considered. When it is, it can be taken into account explicitly, e.g. via fuzzy numbers (Ioannou, Mauris, Trystram, Perrot, 2006) or implicitly by considering statistical distributions of model parameters. Selected model structure primarily depends on the planned use of the model: hypothesis testing, simulation, state estimation and software sensors, control design optimisation, etc. Model parameters are determined from classical experimental designs or from specifically designed optimal ones (Banga, Balsa-Canto \& Alonso, 2008). Once the model is build and its parameters determined, a range of tools is available for indentifiablity, sensitivity and uncertainty analysis, both structural and parametric (Walter and Pronzato, 1997). The outcome of these procedures may be the reconsideration of model hypothesis and structure, and/or the design of additional experiments to allow reliable parameter identification.

# 153 Limitations of current modelling approaches for food systems

Model-based approaches in food engineering are usually subject to one or more of the limitations synthesised in the first column of Table 1 (Bimbenet et al., 2007; Baudrit, Hélias \& Perrot, 2009; Fito et al., 2007; Ioannou, Mauris, Trystram, \& Perrot, 2006; Perrot et al., 2006; Van Impe, 1996). Moreover, several of these difficulties often arise simultaneously in food technology and biotechnology (Van Impe, 1996).
[Table 1 about here]
160 In many domains, existing knowledge of food scientists has led to specific models, valid in a tiny domain, either of composition or of physico-chemical environment. Moreover, their conceptual framework does not allow easy integration of results coming from other existing models (Rodriguez-Fernandez, Balsa-Canto, Egea \& Banga, 2007). For instance, most processing aspects are covered by differential equations of heat and mass transfer phenomena (H\&M), whereas microbiological or chemical aspects are mostly described by simple kinetic equations; coupling those is sometimes possible but not easy or general. Moreover non homogeneous scales can increase the complexity of the modelling task.

Furthermore, experimental data in food science and technology is often limited in amount and quality. On-line sensors are currently available for technological measurements only, such as temperature, pressure, velocity, etc. Measurements related directly to food quality (microbial count, desired or undesired compound concentration, texture...) are still performed by off-line laboratory analysis and are slow, costly, and labour-intensive. In large projects, a rule of thumb is that one laboratory analysis is ultimately obtained per full-time equivalent of the personnel involved in the project and per day. Compared to measurements performed in other fields (mechanics, electronics and even chemistry), laboratory analysis in food science are

subject to significant uncertainty. Differences of $\pm 0.5$ logarithmic units on replicate microbial counts, for example, are considered normal, while this represents a factor of 3. In sensory analysis, 30 or $50 \%$ variations between replicates are usual. Testing mechanism hypothesis and building reliable models based on scarce and uncertain data is obviously a difficult task. To cope with the bottlenecks bring by the study of food complex systems, some ways of research appear to be promising (second column in Table 1).

Co-operation between disciplines
Many scientific fields share the challenge of unifying complex and dissimilar data (Desiere, German, Watzke, Pfeifer, \& Saguy, 2001) and deal with multiple physics models. As shown by Datta (2008), food structure development is not just a function of current parameters like temperature and moisture, but of their entire history, when the complex physical structure develops, changes porosity and transport properties.

One of the research streams is related to the development of reliable models integrating different sources and format of knowledge is so-called knowledge integration. The principle is to deal with the different pieces of the puzzle of knowledge represented under different formalisms: data, models, expertise. One of the problems that must be addressed (Stuurstraat \& Tolman, 1999) is how to cope with the conflicting requirements of each particular subsystem, optimized for its own knowledge domain. No easy solutions are available by now. The key point is the ability to cope with knowledge of different nature, at different scales, expressed in different formalisms (conservation laws and human rules of expertise for example) and to be able to take them into account in a unified manner. Nevertheless, this

issue is a key for the future, enabling us to exploit the different sources of knowledge that we are developing in our laboratories today. Interactions between various fields of science was pointed out in connection with environmental and natural resource issues (Christakos, 2002) biological issues (Olivier et al., 2010), nutrition (McLachlan \& Garett, 2008) etc.

# Uncertainty 

Another key issue in food processes is the management of the uncertainty. Explicit integration of uncertainty has become crucial in industrial applications and consequently in decision making processes (Baudrit, Dubois \& Guyonnet, 2006). In food processes, few contributions are available including uncertainy on model parameters or on model structure itself (Perrot et al., 2006; Petermeier et al., 2002). However, taking into account the complexity of microbiological and/or physicochemical transformations in food processes, available knowledge is often tainted with vagueness, imprecision and incompleteness. Furthermore, for use in industrial applications, models and especially mechanistic models should be studied upon their sensitivity to this uncertainty (Bimbenet et al., 2007; Banga, et al., 2008).

## Computing power

Computationally demanding tasks are increasingly used in food processes. These include for example simulation of spatially distributed models, stochastic migration of molecules to determine diffusion and partition properties in complex media (Vitrac \& Hayert 2007), mathematical viability calculations (Sicard et al. 2009), dynamic optimisation (Banga, J.R., Balsa-Canto, Moles \& Alonso 2003), global sensitivity analysis etc. These tasks require new

calculation methods on computer grids to be tested and implemented (Reuillon, Chuffart, Leclaire, Faure \& Hill 2010).

A representative example: modelling of a cheese-making process
To illustrate previous considerations, consider the case of the modelling and simulation of a cheese making process. The quality of soft mould cheese depends on environmental factors during ripening (relative humidity, temperature, gas composition) and on interactions between inoculated micro-organisms and curd substrates. The concentrations of these substrates is subject to variations in milk quality and cheese-making conditions (Helias, Mirade \& Corrieu, 2007). Over the last 10 years, more than 112 studies (FSTA and ISI web of sciences sources) have been carried out to understand this process in a microbial, physicochemical, biochemical and sensory points of view. About 52\% of those models were empirical. For example Bonaiti, Leclerc-Perlat, Latrille and Corrieu (2004) developed a RSM approach to predict the pH and substrate evolution versus time for a soft cheese. Sihufe et al. (2010) used the principal component analysis to predict the optimal ripening time, while Jimenez-Marquez, Thibault and Lacroix (2005) have proposed a neural network to predict the ripening state of a cheese. Nearly $46 \%$ of the studies fell into the first principles category. $44 \%$ were mechanistic approaches based on mass transfer laws, e.g. for syneresis prediction (Helias et al., 2007; Tijskens \& De Baerdemaeker, 2004), sometimes combined with microbial growth laws (Riahi et al., 2007; Guillier, Stahl, Hezard, Notz \& Briandet, 2008). In the remaining 2\% of the publications, expert systems were developed.

Most of the analysed publications were focused on one specific phenomenon, were limited to the experimentally explored domain without any generalisation ability and without taking into account the inherent uncertainty. For example the mass loss model presented in (Helias et al., 2007) is developed under the hypothesis of average water and convective heat transfer coefficients fixed for air velocity upper than $0.2 \mathrm{~m} . \mathrm{s}^{-1}$ while for some ripening chamber in the industry this velocity is lower than $0.2 \mathrm{~m} . \mathrm{s}^{-1}$. Water activity is also supposed to be constant while it is true in some specific configurations of the process. Integrating other type of information, such as expert knowledge or dealing explicitly with the uncertainty of the process could have enhanced the results. Each of those studies, constitute a part of the puzzle of knowledge that were built to understand the cheese making process but are not sufficient, taken alone, (1) to understand it in its global behaviour including all the scales and (2) to use it in decision making systems.

Some recent studies have nevertheless proposed approaches for modelling the links between different scales and different type of knowledge, including uncertainty (Arguelles, Castello, Sanz \& Fito, 2007; Baudrit, Sicard, Wuillemin \& Perrot, 2010; Thomopoulos, Charnomordic, Cuq \& Abecassis, 2009). Quite a few such integrating approaches are available up to now. Knowledge is still missing to model complex processes such as cheese making. Considerable experimental effort, large databases and progress in microbial physiology are needed to understand numerous variables relevant for cheese making and their interactions.

# 263 New opportunities: Complex system science for food engineering 

265 It follows from previous considerations that remarkable opportunities are now open for theories and techniques developed in the field of complex systems science, to be applied and adapted to food science and technology. The rest of this review will concentrate on knowledge integration, management of the uncertainty and model analysis for reverse engineering purposes.

## 271 Knowledge integration

272 Knowledge integration has been reported in several application fields, including food science. Quintas, Guimaraes, Baylina, Brandao \& Silva (2007) studied complex caramelisation reactions. Alternative reaction pathways have been suggested, each described by a different set of differential equations. Automatic model selection was performed based on parameter identification results. Allais, Perrot, Curt \& Trystram (2007) illustrate how mechanical laws can be coupled with an expert knowledge database to better comprehend a sponge finger batter process. Hadyanto et al. (2007) applied similar ideas to quality prediction of bakery products.

A Systematic Approach for Food Engineering Systems (SAFES) based on the theoretical framework of irreversible thermodynamics has been proposed by Fito, Le Maguer, Betoret \& Fito (2007). The principle is to define a simplified and unifying space of structural features, called 'structured phases and components'. These features are grouped in a composition matrix and are time dependant. The approach has been applied to different processes, e.g.

prediction of the change in protein conformation during ripening (Arguelleset al., 2007). A central hypothesis is the identifiability of the resulting model. This hypothesis is not always satisfied, however, when establishing relationships between food composition and structure, in realistic foods.

The contribution presented by Thomopoulos et al. (2009) concentrates on durum wheat chain analysis. The developed information system allows the integration of experimental data, expert knowledge representation and compilation as well as reasoning mechanisms, including the decision tree learning method. The principle is to encode the existing knowledge about a given food chain in a unified language. The uncertainty pertaining to the expert knowledge is taken into account in the form of fuzzy sets. The information system can be used in assisting decision makers but can not handle numeric approaches, like model based optimal control. As a last example, Baudrit et al. (2010) have shown that by introducing expert knowledge, a good prediction on the microbial and physicochemical kinetics during the ripening of a camembert type cheese was possible, based on limited experimental data set. The theoretical framework used here is that of Dynamic Bayesian Networks (DBNs) proposed by Murphy (2002). DBNs are classical Bayesian networks (Pearl, 1988) in which nodes representing random variables are indexed by time (equation 1). In the considered example, the average adequacy rate in predicting microscopic and macroscopic scales was of $85 \%$, on a test data basis of 80 measurements.

where $X(t)=\left\{X_{1}(t), \ldots X_{N}(t)\right\}$ and $P a\left(X_{i}(t)\right)$ denotes the parents of $X_{i}(t)$ in the graphical structure of the DBN. This probability represents the beliefs about possible trajectories of the dynamic process $\mathrm{X}(\mathrm{t})$. Figure 2 illustrates a DBN representing a network applied on the example of cheese ripening.

# Management of the uncertainty 

Uncertainty, as explained in detail by Datta (2008), is usually of significant concern in food processing, perhaps more than in other domains. Uncertainties are often captured within a probabilistic framework. It is particularly true in food engineering for risk assessment (Aziza, Mettler, Daudin \& Sanaa, 2006). Generally, uncertainty pertaining to the parameters of mathematical models representing physical or biological processes can be described by a single probability distribution. However, this method requires substantial knowledge to determine the probability law associated with each parameter. It is more and more acknowledged that uncertainty concerning model parameters has two origins (Ferson \& Ginsburg, 1996):

It may arise from randomness (often referred to as 'stochastic uncertainty') due to natural variability of observations resulting from heterogeneity or the fluctuations of a quantity over time.

Alternatively, uncertainty may be caused by imprecision (often referred to as 'epistemic uncertainty') due to a lack of information. This lack of knowledge may arise from a partial

lack of data or because experts provide imprecise information. For example, it is quite common for experts to estimate the numerical values of parameters in the form of confidence intervals according to their experience and intuition.

The uncertainty affecting model parameters is thus due both to randomness and incomplete knowledge. This is typically the case in presence of several, heterogeneous sources of knowledge, such as statistical data and expert opinions. The most commonly used theory for distinguishing incompleteness from randomness is the imprecise probabilities calculus developed at length by Peter Walley (1991). In this theory, sets of probability distributions capture the notion of partial lack of probabilistic information. While information regarding variability is best conveyed using probability distributions, information regarding imprecision is more accurately represented by families of probability distributions. Examples of tools to encode probability families include probability boxes (Ferson \& Ginsburg, 1996), possibility distributions (also called fuzzy intervals) (Dubois, Nguyen \& Prade, 2000) or belief functions introduced by Dempster (Dempster, 1967) and elaborated further by Shafer (Shafer, 1976) and Smets (Smets \& Kennes, 1994) make it possible to encode such families.
[Table 2 about here]
As an illustration, consider mass loss model during a ripening process, developed by Baudrit, Hélias \& Perrot (2009). The idea of this contribution is to take into account the imprecise nature of available information about the heat and water transfer coefficients and to jointly propagate variability and imprecision to the estimation of cheese mass loss through the ripening process. In order to do this, the most faithfully available knowledge and the

associated form of uncertainty was implemented (Table 2). For the measurements, spatial variations of humidity and temperature due to climate control were taken into account. Due to low airflow velocity inside ripening chambers, imprecision about the heat and mass transfer coefficients reported in the literature was incorporated and represented by means of a possibility distribution. The joint propagation of these uncertainties, coupling random sampling with interval calculus, has led the authors to provide key information for improving the control of the mass loss of cheeses under industrial conditions. A further step forward would be the integration of the uncertainty as part of the model equations.

Analysis of the models for reverse engineering purposes applied to complex food systems

Model based optimization for identification and control
Model-based optimization is usually implemented for three major areas in food technology (Banga et al. 2008): optimal identification of model parameters, building reduced-ordered models for faster simulation and selection of optimal operating policies (model predictive control). A worked-out example in the first category is given by Balsa-Canto, RodriguezFernandez \& Banga (2007), where the identification of kinetic parameters for thermal degradation of microorganisms is considered. Authors show how well-designed time-varying experiments can achieve an accurate and robust identification of model parameters, with a reduced experimental effort. In modelling of fermentation kinetics, optimal experimental design was applied by Bernaerts, Versyck, \&Van Impe (2000), Smets, Versyck, Van Impe (2002), with similar conclusions.

A comprehensive review of optimal control for food processes was provided by Garcia, Balsa-Canto, Alonso \& Banga (2006). Global optimisation methods like evolutionary algorithms, scatter search and particle swarm optimisation ensure robust convergence towards optimal control profile despite the presence of constraints and local optima. An interesting contribution can be found applied to the alcoholic fermentation of a beer production process (Trelea, Titica \& Corrieu, 2004). The results demonstrate the possibility of obtaining various desired final aroma profiles and reducing the total process time using dynamic optimization of three control variables: temperature, top pressure and initial yeast concentration in the tank. Applied to the alcoholic fermentation, it has led to the reduction of the production cost (reducing the process residence time from 121 hours to 95 hours) for an existing sort of beer without altering its aroma profile (figure 3). Compared to classical sequential quadratic programming optimisation (SQP), PSO optimisation, as well as other stochastic search algorithms, require much less conditions on the dynamic model, objective function and constraints (continuity, derivability) and can thus be applied to almost any existing process model without further reformulation.
[Figure 3 about here]

Viability theory for decision help or control purposes
Given the dynamics of a complex process, a 'viable' control is sequences of actions driving the process along admissible evolutions. Admissible evolutions are such that the industrial production constraints are satisfied and the consumer expectations, expressed as targets, are reached. The main purpose of the viability theory is to explain the evolution of a system

(model exploration), determined by given non deterministic dynamics and viability constraints, to reveal the concealed feedbacks which allow the system to be regulated and provide selection mechanisms for implementing them. Cost function can also be associated to trajectories in the state space. The aim is to reach a target with an optimal trajectory (minimal cost). If we denote $\operatorname{SF}(\mathrm{x})$, the set of evolutions governed by the controlled dynamical system $\mathrm{x}^{\prime}(\mathrm{t})=\mathrm{f}(\mathrm{x}(\mathrm{t}), \mathrm{u}(\mathrm{t}))$, the viability kernel is defined by (Equation 2):

$$
\operatorname{Viab}_{F}(K):=\left\{x \in K \mid \exists x(.) \in S_{F}(x), \forall t>0, x(t) \in K\right\}
$$

This is a variant of the viability problem called capture basin. Numerical schemes to solve `viability' or `capture' problems were firs proposed by Saint Pierre (1994).

As in model-based optimizations methods, an optimal control can be calculated on the basis of the dynamic model. The advantage of the viability approach compared to the previous one is that the exact calculus of the frontier of the admissible evolutions is included in the viability scheme (Martin, 2004). It is also possible, by evaluation of the distance of each evolution to the calculated frontier at each time step, to quantify the robustness of each control trajectory in the state space (Alvarez, Martin \& Mesmoudi, 2010). Indeed, nearer is the evolution to the frontier of the tube, less robust is the selected viable trajectory. Nevertheless viability suffers from the curse of dimensionality, with a need for an exhaustive search in the state space, in contrast to stochastic calculus. Such a bottleneck is in pass to be solved with research led in computer science and increased availability of powerful computer systems (Reuillon, et al., 2010).

A pioneering application of viability theory to food processes was the optimisation of Camembert cheese mass loss during ripening, while preserving an equilibrate growth of ripening microorganisms (expressed using the expert knowledge). The control variables taken into account in the algorithms were the relative humidity and the temperature of the ambient air of the ripening chamber (Sicard et al. 2009). In this study, the computation was achieved by the distribution of the algorithm on a cluster composed of 200 CPU (Central Processing Units). An example of viability kernel calculated for 12 days of ripening is presented figure 4. The distance of the determined viable trajectory to the boundary (frontier) of the viability tube is shown. An optimal ripening control trajectory calculated using the viability algorithm was implemented and validated experimentally. The gain in ripening time with a trajectory selected in the viability kernel for a given quality of the cheese, was of 5 days, to be compared with the residence time in the ripening chamber of around 12 days for a standard control policy $\left(92 \%\right.$ relative humidity and $\left.12^{\circ} \mathrm{C}\right)$.
[Figure 4 about here]

Finally, both optimal control and viability theory are relevant approaches for reverse engineering purposes and can integrate global requirements encountered in food industry (nutritional, organoleptic, economical, technical, environmental, etc...). Nevertheless, their main limitation is the availability of dynamic models sufficiently representative of the complex phenomena involved in food processes.

# Conclusion 

The paper reviews current trends in modelling, design and control of foods and manufacturing processes, by pointing out modern promising approaches to tackle complexity, uncertainty, lack of complete first principles understanding and of reliable data and its high cost. Considerable opportunities are now open to capture and manage the complex dynamics of food systems, coupling different scales and reduce the associated uncertainty. Tight collaboration with various disciplines is needed to unify complex and dissimilar data and knowledge. Fundamental tools developed in complex systems science appear to be able to deal with the identified bottlenecks:

- Develop high-dimension models, integrating all relevant time and space scales, without reduction.
- Develop approaches for decision making and reverse engineering, integrating various sources of information and associated uncertainty.

Key issues towards these goals are knowledge integration, unifying mathematical formalisms, uncertainty representation and management, optimal control, viability and increased computing power. Complex system science provides appealing research directions for these issues and has proven some efficiency to tackle such complex problems as multiscale reconstruction in embryogenese (Olivier et al., 2010). Nevertheless, it is obvious that further interdisciplinary work is required at the frontier of complex system science, which is on its own at the boundary of mathematics, physics and computer science, and food science. A generic structure for this modelling approach could lead in the future to intelligent systems

able to guide the user in defining a model, coupling different mathematical tools and solving the problem by bringing together available knowledge, irrespective of its format and scale.

# Selected publications 

Allais, I., Perrot, N., Curt, C. \& Trystram, G., (2007). "Modelling the operator know-how to control sensory quality in traditional processes. Journal of Food engineering, 83 (2), 156-166.

Alvarez, I., Martin, S. \& Mesmoudi, S. (2010) "Describing the Result of a Classifier to the End-User: Geometric-based Sensitivity". In 19th European Conference on Artificial Intelligence, Lisbon, August 2010.

Arguelles, A., Castello, M., Sanz, J. \& Fito, P. (2007). Application of the SAFES methodology in manchego-type cheese manufacture. Journal of Food Engineering, 83(2), 229-237.

Aubin, J.P. (1991). Viability Theory. Boston, Basel: Birkhauser.

Aziza, F., Mettler, E., Daudin, J. J. \& Sanaa, M., (2006). Stochastic, compartmental, and dynamic modeling of cross-contamination during mechanical smearing of cheeses. Risk Analysis: 26 (3) 731-745.

Banga, J.R., Balsa-Canto, E., \& Alonso, A. A. (2008). Quality and safety models and optimization as part of computer-integrated manufacturing. Comprehensive reviews in food science and food safety, 7, 168-174.

Banga, J.R., Balsa-Canto, E., Moles, C.G., \& Alonso, A. A. (2003). Improving food processing using modern optimization methods. Trends in Food Science \& Technology, 14, $131-144$.

Baudrit, C., \& Dubois, D. (2006). Practical Representation of Incomplete Probabilistic Knowledge. Comput. Stat. Data Anal., 51(1), 86-108.

Baudrit, C., Dubois, D., \& Guyonnet, D. (2006). Joint Propagation and Exploitation of Probabilistic and Possibilistic Information in Risk Assessment Models. IEEE Trans. on Fuzzy Syst., 14(5), 593-608.

Baudrit, C., Hélias, A., \& Perrot, N. (2009). A Joint treatment of imprecision and variability in food engineering: Application to cheese mass loss during ripening. Journal of Food Engineering, 93, 284-292.

Baudrit, C., Sicard, M., Wuillemin, P. H. \& Perrot N. (2010). Towards a global modelling of the Camembert-type cheese ripening process by coupling heterogeneous knowledge with dynamic Bayesian networks. Journal of Food Engineering, 98 (3), 283-293.

Bernaerts, K., Versyck, K.J. \& Van Impe, J. (2000). On the design of optimal dynamic experiments for parameter estimation of a Ratkowsky-type growth kinetics at suboptimal temperatures. International Journal of Food Microbiology, 54, (1-2), 27-38.

Bimbenet, J.J., Schubert, H., \& Trystram, G. (2007). Advances in research in food process engineering as presented at ICEF9. Journal of Food Engineering, 78, 390-404.

Bonaiti, C., Leclercq-Perlat, M.N., Latrille, E. \& Corrieu, G. (2004). Deacidification by debaryomyces hansenii of smear soft cheeses ripened under controlled conditions : relative humidity and temperature influences. Journal of dairy science, 87(11), 3976-3988.

Christakos, G. (2002). On the assimilation of uncertain physical knowledge bases: Bayesian and non Bayesian techniques. Advances in Water Ressources, 25, 1257-1274.

Clerc, M. \& Kennedy, J. (2002).The particle swarm - Explosion, stability, and convergence in a multidimensional complex space IEEE Transactions On Evolutionary Computation, 6, 5873.

Cozman, F. G. (2000). Credal networks. Artificial Intelligence Journal, 120, 199-233.

Datta, A. K., (2008). Status of physics-based models in the design of food products, processes, and equipment. Comprehensive Reviews in Food Science and Food Safety, 7(1), $121-129$.

Davidson, V.J. (1994). Expert systems in process control, Food Research International, 27, $121-128$.

Dempster, A.P. (1967). Upper and Lower Probabilities Induced by a Multivalued Mapping. Ann. Math. Stat., 38, 325-339.

Desiere, F., German, B., Watzke, H., Pfeifer, A., \& Saguy, S. (2001). Bioinformatics and data knowledge : the new frontiers for nutrition and foods. Trends in Food Science \& Technology, 12 (7), 215-229.

De Vleeschouwer, K., Van der Plancken, I., Van Loey A. \& Hendrickx, M. E. (2009). Modelling acrylamide changes in foods: from single-response empirical to multiresponse mechanistic approaches. Trends in Food Science \& Technology 20(3-4), 155-167

Dubois, D., Nguyen, H.T. \& Prade, H. (2000). Possibility theory, probability and fuzzy sets: misunderstandings, bridges and gaps. In Fundamentals of Fuzzy Sets, Dubois,D. Prade,H., Eds: Kluwer , Boston, Mass, 343-438.

547 Farrington-Darby, T. \& Wilson, J. R. (2006). The nature of expertise: A review. Applied Ergonomics, 37, 17-32

549
550 Ferson, S. \& Ginzburg, L.R. (1996). Different methods are needed to propagate ignorance and variability. Reliability Engineering and Systems Safety, 54, 133-144.

552
553 Fito, P., LeMaguer, M., Betoret, N. \& Fito, P.J. (2007). Advanced food process engineering to model real foods and processes: The "SAFES" methodology. Journal of Food Engineering, $83,390-404$.

556
557 García, M.S.G., Balsa-Canto, E., Alonso, A.A. \& Banga, J.R. (2006). Computing optimal operating policies for the food industry. Journal of Food Engineering, 74 (1), 13-23.

560
561 Georgakis, C. (1995). Modern tools of process control: the case of black, gray and white models. Entropie, 194, 34-48.

563
564 Guillier, L., Stahl, V. , Hezard, B., Notz, E. \& Briandet, R. (2008). Modelling the competitive growth between Listeria monocytogenes and biofilm microflora of smear cheese wooden shelves. International Journal of Food Microbiology 128(1), 51-57.

568 Hadiyanto, A., Asselman, A., Van Straten, G., Boom, R.M., Esveld, D.C., \& Van Boxtel, A.J.B. (2007). Quality prediction of bakery products in the initial phase of process design. Innovative Food Science Emerging Technologies. Innovative Food Science \& Emerging Technologies, 8(2), 285-298.

Helias, A., Mirade, P. S., \& Corrieu, G. (2007). Modeling of camembert-type cheese mass loss in a ripening chamber: Main biological and physical phenomena. Journal of Dairy Science, 90, 5324-5333.

Hoffman, R. R., Shadbolt, N. R., Burton, A. M., \& Klein, G. (1995). Eliciting knowledge from experts - a methodological analysis. Organizational Behavior and Human Decision Processes 62 (2), 129-158.

Ioannou, I., Mauris, G., Trystram, G., \& Perrot, N. (2006). Back-propagation of imprecision in a cheese ripening fuzzy model based on human sensory evaluations. Fuzzy Sets and Systems, 157, 1179-1187.

Jimenez-Marquez, S. A., Thibault, J., \& Lacroix, C., (2005). Prediction of moisture in cheese of commercial production using neural networks. International Dairy Journal 15 (11), 11565871174 .

588 Karim, M. N., Yoshida, T., Rivera, S. L., Saucedo, V. M., Eikens B. \& Gyu-Seop O. (1997). 589 Global and local neural network models in biotechnology: application to different cultivation 590 processes. Journal of Fermentation and Bioengineering: 83 (1) 1-11 83(1), 1-11.

592 Kasabov N. (2005). Discovering rules of adaptation and interaction: from molecules and gene 593 interaction to brain functions. In Conference HIS'04, 4th international conference on hybrid 594 intelligent systems. Japan, page 3.

595
596 Kennedy, J., Eberhart, R.C., \& Shi, Y.(2001). Swarm intelligence. Morgan Kaufmann 597 Publishers, San Francisco.

598

599 Linko, S. (1998). Expert Systems: what can they do for the food industry. Trends in Food 600 Science \& Technology, 9, 3-12.

601

602 Lutton, E., Pilz, M., \& Levy J. (2005). The Fitness Map Scheme. Application to interactive 603 multifractal image denoising. In Conference CEC2005, IEEE Congress on Evolutionary 604 Computation in Edinburgh, UK, September 2nd-5th.

605

606 McLachlan, M. \& Garrett, J., (2008). Nutrition change strategies: the new frontier. Public 607 Health Nutrition, 11(10), 1063-1075.

Martin, S. (2004). The cost of restoration as a way of defining resilience: a viability approach applied to a model of lake eutrophication. Ecology And Society, 9(2), 8.

Murphy, K.P., (2002). Dynamic bayesian networks. In Probabilistic Graphical Models, Jordan Press.

Olivier, N., Luengo-Oroz, M., Duloquin, L., Faure, E., Savy, T., Veilleux, I., Solinas, X., Débarre, D., Bourgine, P., Santos, A., Peyriéras, N., Beaurepaire, E. (2010). Cell lineage reconstruction of early Zebrafish embryos using label-free nonlinear microscopy. Science, $329,967-971$.

Pearl, J. (1988). Probabilistic Reasoning in Intelligent systems: Networks of Plausible Inference. Morgan Kaufmann, San Diego.

Perrot, N., Bonazzi, C., \& Trystram, G. (1998). Application of fuzzy rules-based models to prediction of quality degradation of rice and maize during hot air drying. Drying Technology, 16(8), 1533-1535.

Perrot, N., Agioux, L., Ioannou, I., Mauris, G., Corrieu, G. \& Trystram, G. (2004). Decision support system design using the operator skill to control cheese ripening. Journal of Food Engineering 64, 321-333

Perrot, N., Ioannou, I., Allais, I., Curt, C., Hossenlopp, J., \& Trystram, G. (2006). Fuzzy concepts applied to food product quality control: a review. Fuzzy Sets and Systems, 157, $1145-1154$.

Petermeier, H., Benning, R., Delgado, A;, Kulozik, U., Hinrichs, J., \& Becker, T. (2002). Hybrid model of the fouling process in tubular heat exchangers for the dairy industry. Journal of Food Engineering, 55, 9-17.

Poli, R. (2009) Mean and variance of the sampling distribution of particle swarm optimizers during stagnation IEEE Transactions, Evolutionary Computation, 13, 712-721.

Quintas, M., Guimaraes, C., Baylina, J., Brandao, T.R.S. \& Silva, C.L.M. (2007). Multiresponse modelling of the caramelisation reaction. Innovative Food Science \& Technology, 8(2), 306-315.

Reuillon, R., Chuffart, F., Leclaire, M., Faure, T. \& Hill D. (2010), «Declarative Task Delegation in OpenMOLE», in proceedings of the IEEE International Conference on High Performance Computing \&Simulation (HPCS 2010), Caen, France, June 2010, 7p.

Riahi, M. H., Trelea, I. C., Picque, D., Leclerq-Perlat, M.N., Helias, A. \& Corrieu, G. (2007). Model describing Debaryomyces hansenii growth and substrate consumption during a smear soft cheese deacidification and ripening. Journal of Dairy Science 90(5), 2525--2537.

Rodriguez-Fernandez, M., Balsa-Canto, E., Egea, J.A., \& Banga, J.R. (2007) Identifiability and robust parameter estimation in food process modelling : application to a drying model. Journal of food Engineering, 83, 374-383.

Sablani, S., Datta, AK, Rahman, MS \& Mujumdar, AS, (2007). Handbook of food and bioprocess modelling techniques, A. Mujumdar, A. Datta, S. Sablany, S. Rahman, Bocca Raton Fla, CRC Press.

Saint Pierre P. (1994). Approximation of the viability kernel. Applied mathematics and optimization, 29, 187-209.

Sicard M., Perrot N., Baudrit C., Reuillon R., Bourgine P., Alvarez I. \& Martin S. (2009). The viability theory to control complex food processes. European Conference on Complex Systems (ECCS'09), University of Warwick (UK).

Sihufe, G. A., Zorrilla S. E., Perotti, M.C., Wolf, I.V., Zalazar, C.A., Sabbag, N.G., Costa, S.C. \& Rubiolo, A.C. (2010). Acceleration of cheese ripening at elevated temperature. An

671 estimation of the optimal ripening time of a traditional Argentinean hard cheese. Food Chemistry: 119 (1), 101-107.

673

674 Shafer, G. (1976). A Mathematical Theory of Evidence. Princeton University Press.

675

676 Slade, L., \& Levine, H. (1995). Water and the glass transition. Dependence of the glass transition on composition and chemical structure: special implications for flour functionnality in cookie baking. Journal of Food Engineering, 24, 431-509.

679

680 Smets, P. \& Kennes R. (1994). The transferable belief model. Artificial Intelligence, 66, 191681234 .

682

683 Smets I.Y.S., Versyck, K.J.E. \& Van Impe, J. (2002). Optimal control theory: A generic tool for identification and control of (bio-)chemical reactors, Annual Reviews in Control, 26 (1), $685 \quad 57-73$.

686

687 Stuurstraat, N. \& Tolman, F. (1999). Product modelling to building knowledge integration. 688 Automation in construction, 8(3), 269-275.

689

690 Theys, T. E., Geeraerd A. H. \& J. F. Van Impe (2009). Evaluation of a mathematical model 691 structure describing the effect of (gel) structure on the growth of Listeria innocua,

Lactococcus lactis and Salmonella Typhimurium. Journal of Applied Microbiology 107(3), $775-784$.

694

695 Thomopoulos, R., Charnomordic, B., Cuq, B. \& Abecassis, J. (2009). Artificial intelligencebased decision support system to manage quality of durum wheat products. Quality Assurance and Safety of Crops \& Foods, 1 (3) 179-190.

698

699 Tijskens, E., \& De Baerdemaeker, J. (2004). Mathematical modelling of syneresis of cheese curd. Mathematics and computers in simulation, 65(1-2), 165-175.

701

702 Trelea, I. C. (2003).The particle swarm optimization algorithm: convergence analysis and parameter selection, Information Processing Letters, 85, 317-325

704

705 Trelea, I.C., Titica, M., \& Corrieu, G. (2004). Dynamic optimisation of the aroma production in brewing fermentation. Journal of Process Control, 14, 1-16.

707

708 Trystram, G. \& Courtois, F. (1996). Food process modelling and simulation, In Computerized control systems in the food industry, Ed G. Mittal, M. Dekker, New York, 55-85.

710

711 Van Impe, J.F. (1996). Power and limitations of model based bioprocess optimization. Mathematics \& Computers in simulation, 42, 159-169.

Varela, F. (1979). Principles of biological autonomy, New York, Elsevier North Holland.

Vitrac, O. \& Hayert, M. (2007) Effect of the distribution of sorption sites on transport diffusivities: A contribution to the transport of medium-weight-molecules in polymeric materials. Chemical Engineering Science, 62 (9), 2503-2521.

Walley, P. (1991). Statistical Reasoning with Imprecise Probabilities, Chapman and Hall.

Walter, E., Pronzato, L. Identification of Parametric Models from Experimental Data, Springer-Verlag, Heidelberg, 1997. Xviii, 413 pages.

731 Figure 1: A typical approach for model development in food engineering

732

733 Figure 2: An example of DBN applied to cheese ripening presented in Baudrit, Sicard, Wuillemin \& Perrot (2010), with la, Gc and Ba microorganisms concentrations, la and lo substrate and product concentration, T temperature of the ripening cell, colour, coat, humidity, odour and under-rind macroscopic sensory evolutions.

737

738 Figure 3: Fermentation time reduction of an existing beer without changing the final aroma profile. Top: aroma concentrations at the end of the alcoholic fermentation. Bottom: operating conditions for the alcoholic fermentation process.

741

742 Figure 4: An example of viability tube for 12 days of a cheese ripening process. Distance square map for each point is presented in colour: from blue near the boundary of the viable tube, to red at the heart of the tube. 3 dimensions are taken into account for the calculus of the viable state: mass, respiration rate of the microorganisms and temperature of the surface of the cheese.

752 List of tables

753

754 Table 1: Difficulties for the development and analysis of the models in food engineering (column 1) and possible solutions (column 2).

756

757 Table 2: Type of uncertainties propagated in a mechanistic model of cheese mass loss during a ripening process.

758

759

760

761

![img-0.jpeg](img-0.jpeg)

Figure 1: A typical approach for model development in food engineering

![img-1.jpeg](img-1.jpeg)

Figure 2: An example of DBN applied to cheese ripening presented in Baudrit, Sicard, Wuillemin \& Perrot (2010), with la, Gc and Ba microorganisms concentrations, la and lo substrate and product concentration, T temperature of the ripening cell, colour, coat, humidity, odour and under-rind macroscopic sensory evolutions

![img-2.jpeg](img-2.jpeg)

Figure 3: Fermentation time reduction of an existing beer without changing the final aroma profile. Top: aroma concentrations at the end of the alcoholic fermentation. Bottom: operating conditions for the alcoholic fermentation process.

![img-3.jpeg](img-3.jpeg)

Figure 4: An example of viability tube for 12 days of a cheese ripening process. Distance square map for each point is presented in colour: from blue near the boundary of the viable tube, to red at the heart of the tube. 3 dimensions are taken into account for the calculus of the viable state: mass, respiration rate of the microorganisms and temperature of the surface of the cheese.

Table 1: Difficulties for the development and analysis of the models in food engineering (column 1) and possible solutions (column 2).


Table 2: Type of uncertainties propagated in a mechanistic model of cheese mass loss during a ripening process.
