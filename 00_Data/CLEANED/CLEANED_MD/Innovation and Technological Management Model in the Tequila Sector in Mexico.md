# Article 

## Innovation and Technological Management Model in the Tequila Sector in Mexico

Antonia Terán-Bustamante ${ }^{1, * *}$, Antonieta Martínez-Velasco ${ }^{2 * *}$, Víctor Manuel Castillo-Girón ${ }^{3}$ and Suhey Ayala-Ramírez ${ }^{4 *}$ (D)<br>check for updates<br>Citation: Terán-Bustamante, A.; Martínez-Velasco, A.; Castillo-Girón, V.M.; Ayala-Ramírez, S. Innovation and Technological Management Model in the Tequila Sector in Mexico. Sustainability 2022, 14, 7450. https://doi.org/10.3390/su14127450

Academic Editor:
Mariarosaria Lombardi
Received: 18 April 2022
Accepted: 13 June 2022
Published: 18 June 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Facultad de Ciencias Económicas y Empresariales, Universidad Panamericana, Ciudad de México 03920, Mexico
2 Facultad de Ingeniería, Universidad Panamericana, Ciudad de México 03920, Mexico; amartinezv@up.edu.mx
3 Departamento de Ciencias Económico Administrativas, Centro Universitario de los Valles, University of Guadalajara, Ameca 46600, Mexico; victor.cgiron@academicos.udg.mx
4 Departamento de Ciencias Sociales y Humanidades, Centro Universitario de los Valles, University of Guadalajara, Ameca 46600, Mexico; suhey.ayala@academicos.udg.mx

* Correspondence: ateran@up.edu.mx

Abstract: Creativity, ideas, and an entrepreneurial attitude are needed to innovate. However, it is also necessary to have practical instruments that allow innovations to be reflected in the company. One of those tools is technology. This research aims to analyze innovation and technology in the tequila industry through Bayesian networks with machine learning techniques. Likewise, an innovation and technology management model will be developed to make better decisions, which will allow the company to innovate to generate competitive advantages in a mature low-tech industry. A model is made in which the critical factors that influence management innovation and technology optimally to generate value translate into competitive advantages. The evidence shows that the optimal or non-optimal management of knowledge management and its various factors, through the causality of the variables, allow the interrelation to be more adequately captured to manage it. The results show that the most relevant factors for adequate management of innovation and technology are knowledge management, sales and marketing, organizational and technological architecture, national and international markets, cultivation of raw materials, agave, and management, use of waste, and not research and development.

Keywords: innovation; Bayesian networks; machine learning; Mexico; technology model; technological innovation; tequila industry

## 1. Introduction

Innovation is increasingly important, particularly in economic crises like the one we are currently experiencing caused by the COVID-19 pandemic. However, to innovate, one must consider two key elements within the firm: the management of innovation and technology. These are dynamic processes that need to be considered strategically to generate value.

Innovation is a crucial factor in economic development for companies. Currently, in the knowledge economy, more accelerated innovation processes are developed that generate new products, production processes, and distinctive forms of marketing, commercialization, and organization, which contribute to raising competitiveness, the economic growth of the firm, and at the same time impact the well-being and quality of life of people [1,2].

The company will look for tools that allow it to innovate, improve its productivity, and have competitive advantages. One of those tools that allow the company to innovate is technology management (GT) because the company's activities related to innovation have a more significant impact to the extent that they are adequately managed, their

processes are well defined, they are carried out systematically, and they have an area that coordinates them [3].

COVID-19 affected almost all sectors of the economy; however, the tequila sector in 2021 grew. Production increased by $41.2 \%$ compared to 2020, reaching 487.3 million liters produced. On the other hand, exports also registered their highest level in history, reaching 310.5 million liters. This figure represents $17.6 \%$ compared to the same period in 2020. It is worth mentioning that $70 \%$ of the tequila exported is bottled from the origin, which translates into a more significant economic benefit for the territory protected by the designation of origin tequila (DOT) [4].

Along with production, the consumption of agave grew, presenting an increase of $43.5 \%$, reaching 1 million 866 thousand tons. That is also a historical high for tequila agribusiness [4].

Two other figures that are added to the previous records in the year 2022 of 2021 are the number of registered trademarks. At the end of 2021, the CRT registered 1913 trademarks, while in the year 1995, there were only 516 trademarks; for their part, the registered agave growers at the end of 2021 reached a critical number of 25 thousand agave producers; in 2014, there were barely 3000 agave growers. Therefore, the above figures represent new records for this production chain [4]. The tequila industry has established itself as one of the leading agribusinesses in Mexico by producing one of the most emblematic alcoholic beverages worldwide [5] (Gallardo, 2019); however, to innovate and adopt new technologies throughout the sector, it has to focus on addressing the problems that it presents integrally.

The main problems faced by the tequila industry are the following:
I. Many medium and small companies compete with large companies.
II. Availability and supply of raw material, which suffers from cyclical crises that fluctuate over the years and have a considerable impact on both production levels, costs, and all the points mentioned for the production of tequila and the different distillates [6].
III. The adulterations.
IV. Sustainability, since its treatment processes for some types of waste, such as stillage, are not yet fully efficient.
V. Dissimilar use and development of technology between large and smaller companies, which continue to use old processes.
In addition to the above, it is necessary to consider that the tequila industry is a mature low-tech industry, where there is low intensity in research and development (R\&D).

Derived from the previous problem, the questions that guide the research are: What are the main factors to innovate in a mature low-tech sector like tequila? What are the critical factors in the optimal management of innovation and technology in the tequila industry? Using an innovation and technology management model, how can a company in the tequila sector make better decisions to innovate new products/services, processes, sales and marketing, and the organization? What are the best correlations between the various factors in the innovation management model in the tequila industry?

This research aims to analyze innovation and technology in a mature low-tech sector such as the tequila industry. For this purpose, a predictive decision-making model is designed through Bayesian networks with machine learning techniques.

This research is structured into three sections. The first section addresses the theoretical framework, specifically the management of innovation and technology and its relationship with knowledge. Characterization of the tequila sector in Mexico is also made. The second section presents the methodology of analysis and construction of the tequila model based on Bayesian networks (BNs). Finally, the third section presents the results, discussion, and conclusions.

# 2. Theoretical Framework 

### 2.1. Innovation and Technology Management: Key Elements

Management contemplates the activities from which the human being reflects his creativity and ways of adapting to the context in which he participates. It is the form from which it uses the available knowledge, both theoretical and practical, and the forms in which it manifests itself (artifacts, experience, processes, systems, and products/services) [7].

Innovation and its management are an important issue for high-tech industries and lower technological industries and companies because it has a significant impact on competitiveness.

Technology is applied knowledge (scientific, technical, and traditional). It is a set of knowledge about techniques that can encompass both knowledge and the tangible materialization of that knowledge in a production process, in a system, machinery, or equipment [7].

It is action-oriented practical knowledge; it involves the systematic application of scientific knowledge or other knowledge organized into practical tasks. It is a knowledge whose application is oriented to a specific end to solve action problems, and its object is not simply to know but to act. That is, a knowledge that one has not only in terms of knowledge but also knowing how to do $[8,9]$ and why to do it [10].

Technology integrates components associated with innovation. Innovation is a complex concept, which according to Schumpeter [11], is related to that process of creative destruction in which you have to rebuild to innovate. This process is both a means and an end for companies to respond faster to customer needs and achieve advantages in a global economy. It is about managing a process that always seeks improvements in itself. Nevertheless, it also delivers new products and services to customers efficiently, effectively, and faster than the competition or improves the delivery of existing products and services by improving processes $[3,10]$.

Currently, innovation is a constant process in companies, in which changes are continuously introduced in their products and processes, new organizational methods are applied, new business methods are implemented, essential changes are implemented in the company, and new knowledge is acquired, among others [1,3].

Therefore, innovation has become a core factor in the company that allows it to generate value for its implementation and achieve benefits that are reflected in profitability due to the risks assumed $[3,9]$.

Therefore, the company will look for tools that allow it to innovate, improve its productivity, and have competitive advantages. One of these tools that allow the company to innovate is the management of technology (GT) because the company's activities related to innovation have a more significant impact to the extent that they are properly managed, have well-defined processes, are carried out systematically, and have an area that coordinates them $[2,3,10,12,13]$.

Technological management should be seen as the process that allows acquiring knowledge necessary to make technological innovations; that is, value is created for the company since the efficiency of operations is increased [14].

The company must be able to develop technological capabilities through its management that allow it to identify, adopt, use, dominate, modify, and/or create technologies and make use of new or existing knowledge for the development of new products and improvement in products, processes [15] and the company itself, which enable its sustainability over time $[2,3,7,9,10]$.

The Cotec Foundation [8] conceptualizes technological management as the organization and direction of human and economic resources to increase the creation of new knowledge. The generation of technical ideas allows obtaining new products, processes, and services or improving existing ones; the development of these ideas in prototypes and their transfer to the manufacturing, marketing, and use phases.

For Solleiro and Castañon [16], technology management is the set of tools and techniques that allow an organization to properly take advantage of its resources (people,

money, machines, and information, among others) through the elaboration and execution of innovation plans.

For its part, the National Technology and Innovation Award includes five functions to manage innovation: (i) monitor, (ii) plan, (iii) enable, (iv) protect, and (v) implement [17].

For the Mexican Standard NMX-GT-003-IMNC-2008 on Technology Management [18], adopting a technology management system is a strategic decision of the organization. Therefore, its design and implementation in an organization are influenced by its different needs $[3,18]$.

Barletta et al. [19] argue that innovation is the result of multiple factors that go beyond the activities carried out in R\&D laboratories and include a combination of routines and solutions to problems both inside and outside the R\&D laboratory.

According to the above, to understand the explanatory factors of these activities, it is necessary to understand innovative behavior as a complex phenomenon that is part of the firm's competencies.

# 2.1.1. Management of Innovation, Technology, and Knowledge 

Innovation management requires capturing the continuously created knowledge, which is integrated into work routines when defining long-range strategies or complex problems that demand more structured decision-making. In all cases, knowledge is required. Therefore, it is necessary to understand how it is valued economically, in the organization, and socially and created, used, disseminated, managed, and changed [7].

Innovation implies applying new knowledge; for this reason, companies follow particular learning processes and have defined trajectories that influence their development. Through these learning processes, companies build competencies.

Learning is a process that involves repetition and experimentation, which makes it possible to perform tasks better and faster and identify new production opportunities [3,20].

According to the above, managing knowledge does not necessarily mean innovating; the relevant thing is knowing and understanding how to manage it to influence company improvements. That is, innovations are made in any of its possible forms. That is, to know the dynamics of planning, organizing, controlling, and directing the process so that when used, it has a productive result so that it becomes a conscious and deliberate act of creation, access, use, and protection. Technological learning refers to the dynamic process of acquiring technological capabilities.

Companies learn over time, accumulate knowledge and technological capabilities, progressively undertake new activities, and acquire new technological capabilities. Studies tend to analyze technological learning processes and capacity-building processes together [21].

External sources include strategic alliances and licensing agreements; independent suppliers of materials, components, and equipment; technical analysis of competitors' products; research institutes and universities; experts and consulting firms; patents; conferences; professional and scientific journals; fairs and exhibitions, among others.

Therefore, the learning process is fundamental in the construction of innovation capabilities. The ability to learn and accumulate knowledge over time is the essence of the innovation process, and this is built through its management.

Therefore, knowledge and the development of learning processes become critical elements in generating competitive advantages.

Innovation is a process that enables value to be created and captured from ideas.
Successful innovation management routines are not easy to acquire. Because they represent what a particular firm has learned over time, through a process of trial and error, they tend to be very firm specific.

From a general perspective, knowledge is relevant for low-tech firms and can be conceived as practical knowledge, where it cannot always be distinguished from scientifically generated knowledge. In other words, the adaptation of the process is constructed in an application-oriented form-by doing-are based on the accumulated practical knowledge of the company and the tacit knowledge of people [22].

# 2.1.2. Innovation in Low-Tech Industries or Non-Research-Intensive 

According to the Organization for Economic Cooperation and Development (OECD) [23], a firm's technological level is related to its intensity and expenditure on R\&D. Thus, in the classification, there are companies and sectors of high-tech, medium-tech, and low-tech, measured by the results and impact of R\&D.

For Tidd and Bessant [24], innovation and competitive success are not simply about high-technology companies, innovating is about learning. In recent decades, literature on innovative activities in sectors and firms that do not carry out formal R\&D activities has become widespread, mainly in Germany and Spain [19,25-34] among others.

However, derived from specific studies, especially in the manufacturing industry, these researchers agree that studies of innovation are reduced to the analysis of the intensity of formal R\&D. For this reason, it is only possible to explain the behavior of a part of the productive structure, generally based on knowledge-intensive activities.

However, a significant proportion of studies confirm a strong influence of other factors on the rest of the productive structure. In other words, different types of resources and skills are mobilized that can compensate for the absence of formal efforts in internal R\&D [22,31].

In these companies, the primary sources of knowledge to innovate come from external laboratories, customers, and suppliers. Bender and Laestadius [26] and Rammer, Czarnitzki, and Spielkamp [27] argue that, especially in the case of small and medium-sized companies, R\&D laboratories are often replaced by the development of social technologies, which are associated with human resource management, work organization, and the search for external sources of innovation.

Bender and Laestadius [26] also suggest that formal R\&D is not an essential asset that firms have to generate innovation processes, which are their skills to transform codified knowledge into specific knowledge contextualized in each process organization. Moreover, tacit knowledge allows them to utilize dispersed organizational knowledge to put it together creatively. To generate the organizational skills to innovate, in low-tech sectors, innovation is the result of a particular configuration of tacit and codified resources that firms build throughout their lives rather than strategies based on R\&D [19].

According to Potters [29], R\&D as an input for innovation (output) plays a minor role in low-tech sectors, as they are mature industries where many (small) producers operate at marginal cost. However, these sectors play an essential role in the economy.

For Som and Kirner [30,31], despite the debate and criticism of innovation with a hightech focus, low manufacturing tech (LMT) research shows that non-research-intensive industries are surprisingly innovative and play an essential role in the development of modern economies. The LMT sector bases its innovation on modifying available technologies and existing knowledge to combine them in a hybrid concept with high-tech components.

According to Zouaghi [33] and Law [34], low-tech companies-in contrast with the complexity of high-tech companies-are characterized by focusing on innovation by process, organization, and marketing. For this reason, these companies have low internal innovation capabilities and are dependent on external knowledge acquisitions. In addition to the above low-tech firms, to improve their innovation performance, look for R\&D human capital, while high-tech firms invest in R\&D expenditures. However, due to low R\&D investment, low-tech firms usually lack absorptive capacity [33].

Thomä [32] asserts that innovation at the firm level occurs with or without R\&D, but rarely without acquired skills such as by doing, using, and interacting. These competencies are given through an informal learning process and know-how based on experience. Thus, the excessive emphasis on formal, internal R\&D processes ignores the fact that competencies of this type are a prerequisite for successful innovation.

Knowledge management practices (KMP) are a critical factor that directly affects innovation activities [34]. Thus, knowledge is an essential and complex input.

# 2.2. Characterization of the Tequila Industry in Mexico 

Tequila is one of the most famous drinks nationally and worldwide. It is obtained from the Agave Tequilana Weber Blue plant, better known as Agave Azul, which is produced in 181 municipalities in five states, where there is a denomination of origin for such purposes: Jalisco, its 125 municipalities; Michoacán, 30 municipalities; Nayarit, 8 municipalities; Tamaulipas, 11 municipalities; Guanajuato, 7 municipalities [35].

Tequila is a product that has been associated with the values of regional and national identity, popular culture, literature, and Mexican cinema [36]. Currently, its production constitutes one of the usual activities of Mexico and is significant in the agricultural and industrial development of various states, especially Jalisco [37,38]. Its distinction and importance come from its historical roots; its production and commercialization have reached great cultural and economic relevance [39].

The consolidation of the tequila industry in Mexico has been evident since the last century and now continues. However, in recent years, the popularity of the drink has been increasing, not only nationally but also internationally [40]. This is reflected in the increase in beverage production. From 1995 to 2008, production tripled, going from 104.3 to 312.1 million liters [4]. In terms of value, in 2019, the exports made by 162 companies represented USD 1874.00 (millions of dollars). In 2021, production reaches the highest point in its history, producing about 374 million liters of tequila, the highest volume recorded since 2000, representing, in the last two decades, an increase of $106 \%$ [4]. Germany, Spain, France, and Canada are the leading destinations for these exports. However, the United States is positioned as the leading destination country for this beverage [41,42].

### 2.2.1. Cultivation and Production of The Agave Tequilana Weber Blue Variety

Agave is a plant native to Mexico, there are more than 200 varieties, and only one can be used to produce tequila, the Agave Tequilana Weber Blue variety, which gives the drink its unique organoleptic characteristics and its denomination of origin (DO) [43].

According to the General Declaration of Protection of the Denomination of Origin Tequila (DO) and the NOM of Tequila, for the Weber Blue variety to be used in the manufacture of tequila, it must meet the following two requirements: 1. The Agave Tequilana Weber Blue must be grown within a geographical area delimited by the general declaration of the denomination of origin, and 2. Must be registered with the Tequila Regulatory Council (CRT), a tequila certification body [4].

The Agave Tequilana Weber Blue variety does not exist in wild form, and its vegetative propagation is carried out using the offspring produced by the mother plants, whose ideal planting time is just before the rainy season to favor the beginning of the development of the plant. The average time required by the plant to reach maturity ranges from seven to nine years, a period in which the maximum accumulation of carbohydrates is reached [6,44,45]. The main carbohydrate is inulin, a high molecular weight polymer of approximately 43 fructose monomers whose ends constitute a glucose molecule. For the harvest or Jima of the agaves, all the leaves are cut, and then the plant with a pineapple appearance is cut, which weighs between 20 and $90 \mathrm{~kg}[6,46]$.

Being the raw material for the elaboration of tequila, some companies also take advantage of it to elaborate functional foods such as inulin and fructose; the availability of agave is one of the strategic elements of this industry. Furthermore, given its long life cycle and that during its development it is exposed to various climatic factors such as frost/snowfall, droughts, fires, pests, and diseases, the planning of the crop is essential and must be aligned with the market expectations of tequila. Thus, one of the priorities of the actors involved, particularly the Tequila Regulatory Council, is the inventory of the number of agaves planted according to their age, the place of planting, their owner, their phytosanitary status, their link with a tequila company, among other aspects [4,47,48].

# 2.2.2. The Process of Elaboration and Types of Tequila 

Tequila is made through a process that, although it varies depending on the tools, artifacts, practical types, and techniques that are used, in general, is integrated into six phases: the cultivation and Jima of the agave, cooking, grinding, fermentation, distillation, and packaging for sale and marketing (Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1. The tequila production process. Source: own elaboration [49,50].
According to SAGARPA [44], although agave can be grown on land with a particular slope, the ideal is to do it on flat land whose preparation before planting must include proper subsoiling and fallowing, and be tracked, whitewashed, and quartered or marked. The harvest or Jima of agave usually occurs between 7 and 9 years after planting and translates into obtaining the pineapples or heads of the agave that, when transferred to the factory, undergo a cooking process.

The cooking aims to perform the hydrolysis of fructans to generate simple sugars, fructose, and glucose in an approximate ratio of $90 / 10$, soften the agave for subsequent grinding and promote the generation of essential compounds for the aromatic profile of the final distillate [48].

The grinding consists of tearing cooked heads or pineapples to extract the sugars from the agave. Fermentation is the biochemical breakdown that results in transforming agave sugars into alcohol. Distillation is divided into three phases. In the first, the vinasses are separated from other components such as aldehydes and ketones, obtaining a low alcohol content. In the second, known as rectification, ethyl alcohol is concentrated and purified from other alcohols obtaining what is known as heads and tails. In economic terms, distillation consumes about $50 \%$ of the energy required in the production process, and, therefore, it is the phase where costs could be reduced through strategies that reduce energy consumption. [50]. With these operations, a tequila of $45^{\circ}$ to $50^{\circ} \mathrm{GL}$ is obtained that can be immediately packaged as white tequila or move to a third phase, known as the aging process, whose objective is to give the tequila the color and the bouquet (scent and flavor) depositing it in barrels for a specific time which gives rise to different types of tequila [51].

The packaging of tequila differs according to the type of tequila. For example, in the case of mixed tequila and the sugar of the blue weber tequila, agave contains other types of sugars; its distribution can be in bulk or without packaging or packaging. On the contrary, $100 \%$ Agave Tequila needs to be packaged, usually in new glass containers and with its due labeling to show that the production of agave and the elaboration of tequila occurred within the denomination of origin zone [51].

Table 1. Classification of tequila by the sugars of origin and the time of rest.


Source: own elaboration $[49,50]$.

# 2.2.3. A Technical But Also Traditional Industry 

One of the differentiating elements between companies in the tequila industry is the level of equipment and automation of the different phases of the production process [3,49,50,52]. Although it is not a rule, the most technical companies are those with the largest size and production capacity [53]. At the same time, the rest of the producers experience a hybridization of their processes, and even in many cases, small companies continue to use the artisanal method, as explained in Table 2.

According to the above, the composition of tequila is very complex, it is affected by each of the stages of its production process. Therefore, its scent and flavor-sensory characteristics-depend on the amount and type of volatile compounds present [50].

Table 2. Technification of production processes in tequila producing companies.


Table 2. Cont.


Source: own elaboration $[49,50]$.

# 2.2.4. Waste and Environmental Sustainability in the Tequila Industry 

During the tequila production process, various wastes are generated that, as a whole, place the tequila industry as one of the most polluting [54] and, therefore, this constitutes one of the significant challenges for the sector. The residues with the greatest impact are the leaves of the agave rosette, bagasse, and vinasses [55].

The leaves of the agave rose window represent about $14 \%$ of the usable portion of the plant that, despite its biotechnological potential, are left in the field when harvesting the pineapples or heads, constituting a residue that has no uses so far [45,56].

Bagasse is the fiber of the agave that is obtained once the pineapples have been cooked and ground to generate sugars that, during fermentation, will produce alcohols and other chemical compounds, which will be separated in distillation. In the production of one liter of tequila, between seven and eight kilograms of agave are required, which are converted into five kilograms of bagasse/wet base (residue) once the juice is extracted [45].

According to Moreno et al. [45], bagasse residues can become a raw material source for obtaining various by-products. For example, bagasse as a material to produce organic fertilizer stands out through composting incorporated into the crop fields as fertilizer. The potential of agave bagasse for the production of biofertilizers is very significant due to the recirculation of nutrients in the agave crops themselves. Some tequila companies are trying to change the bagasse composting process to a vermicomposting process to reduce time and improve agave waste management $[45,48]$.

Bagasse can also be used as fuel in boilers, filling furniture and mattresses, fodder for birds and livestock, and brick and adobe making. Another alternative for its use is the one made by obtaining some enzymes with high commercial value that can be used in the development of new products such as biofuels such as bioethanol, mainly due to its hexose content that makes fermentation processes less complicated [45,48].

Vinasses are liquid residues composed of non-volatile substances generated and remain at the bottom of the still after distillation of fermented agave must [45]. In the vinasses remain the agave fibrils that were not retained in the juice filtration stage, depleted yeast cells, residual sugars, acids, esters, higher alcohols, and substances that give caramel color. Although these effluents are not classified as hazardous waste, they are considered complex wastewater $[57,58]$ because they have a chemical oxygen demand more significant than $38,215 \mathrm{mg} / \mathrm{L}$, total solids (ST) greater than $21,883 \mathrm{mg} / \mathrm{L}$, and have a low pH of $3.5-3.9[59,60]$.

Vinasses also contain high concentrations of phenolic compounds that give them a characteristic dark brown color [61]. Although they have some use as biofuels, their characteristics and the high volumes generated make vinasses a tremendous environmen-

tal concern [45,54,60], since their incorrect disposal can cause significant environmental impacts [62], in addition to the significant cost of treating vinasses through an evaporationoxidation process in large vats [63].

This is especially worrisome in regions with high rates of tequila production, such as the state of Jalisco [64,65].

To find alternative solutions to this environmental problem, anaerobic biological processes have been presented, which, in addition to reducing the concentration of pollutants, make it possible to recover methane and hydrogen as potential energy sources within the same tequila production process [60,65,66]. However, currently, this treatment only occurs in large companies, while small and medium-sized companies do not have the financial resources.

On the other hand, the high agricultural and agro-industrial activities of this industry also lead to greater exploitation and contamination of water resources [67,68].

In this context, various eutrophic conditions have been identified in multiple bodies of water caused by excessive and uncontrolled discharges of solid waste and wastewater by agro-industrial activities, which generates anoxic conditions and toxic blooms of cyanobacteria, which can harm wildlife and even pose a threat to nearby settlements [69,70].

Thus, the reduction of this eutrophication demands better management practices for both solid waste and wastewater to reduce the amounts of organic matter and nutrient discharge that enter the hydrographic systems of Jalisco [67,68,71]. The foregoing is so relevant that the government of Jalisco has set a goal for 2030 to reduce its current GHG (greenhouse gas) emissions by $22 \%$, of which $14 \%$ is attributed to waste management and sewage $[72,73]$.

# 3. Materials and Methods 

This research is qualitative (descriptive) and quantitative, with a correlational scope and based on information obtained through questionnaires and semi-structured interviews. A focus group was carried out during the first two months of 2022. A total of four questionnaires were collected, five semi-structured script interviews with experts, cameras, and consultants. The questionnaire was applied to the leading companies in the tequila industry. These firms represent $68 \%$ [4] of the industry. These interviews were conducted with managers and key personnel performing essential activities and processes, such as production and administration. In addition, three interviews were conducted with consultants of the company and two with researchers from the university. All interviewees handle strategic information to generate knowledge and management of innovation and technology within the company or in the study sector.

The focus groups were based on experts' opinions. This model was made to identify the main processes needed for technological innovation management in the tequila industry. The model was developed through a Bayesian network. Once the model was created, a database of 100 records was generated based on the patterns generated through the Bayes network. The data generated represents the network in the sense that it comes from a joint probability distribution modeled by the network. Several experiments were done, generating 1000-, 300-, and 100-record databases. The archive with 100 records was sufficient to obtain conclusions since there were no significant differences in the results in the other two cases.

Once the dataset was available, a classification was made through machine learning tools based on the objective variable management of innovation and technology. The most relevant variables were selected to predict the management of innovation and technology class or variable objective employing the RRelief metric. The central idea of the RRelief algorithm is to estimate the quality of variables based on how well it can distinguish between instances that are close to each other. RRelief calculates a variable score for each variable that can then be applied to classify and select the highest-scoring characteristics to select the most relevant variables to predict the management of innovation and technology variables.

The fundamental challenge in data mining or modeling is to identify and characterize the relationships between one or more data features and some target feature. The remaining features, which are usually not distinguished a priori in real-world problems, are not informative but contribute to the overall dimensionality of the problem space. This increases the computational load for the modeling methods. Feature selection is defined as the process of identifying relevant features and discarding irrelevant ones [74]. There are several types of methods for variable selection. Among them, the filter method stands out.

Filtering methods use an indirect measure calculated from the general characteristics of the training data as a pre-modeling step. Filters are generally fast and work independently of the induction algorithm. Therefore, selected features can be passed to any modeling algorithm. Filtering methods can be roughly classified according to the filtering measures they employ. Those are information, distance, dependency, consistency, similarity, and statistical measures.

Kira and Rendell [75] conceived the original Relief algorithm based on instance-based learning. As an individual evaluation, Relief computes an indirect statistic for each feature that can be used to estimate the feature's relevance to the target variable. These feature weights can range from -1 (worst) to +1 (best). Its strengths are that it does not depend on heuristics, runs in low-order polynomial time, is noise tolerant, and resistant to feature interactions, as well as being applicable for binary or continuous data.

ReliefF is an adaptation of the original Relief algorithm, which is based on many neighbors user parameter k that specifies the use of k nearest hits and k nearest misses in the score update for each. This change increased the reliability of the weight estimate. It is also capable of handling missing data values. It also uses strategies to handle multiclassing. During the evaluation of multiclass problems, ReliefF finds the k closest bugs from each "other" class and averages the weight update based on the prior probability of each class [76].

Next, a clustering process was carried out, that is, unsupervised classification. Clustering is a set of machine learning techniques that select observation classes (clusters), which contribute identical characteristics. Where it happens that the same class has similar characteristics and the observation of separate groups shows a difference in features. It is a non-supervised learning method, where the group tries to identify a relationship between the data without being trained by the response variable (Figure 2).
![img-1.jpeg](img-1.jpeg)

Figure 2. Methodology.
The K-means grouping is the most direct and frequently practiced group method to categorize a data set in many classes [77].

Clustering was carried out using the K-means algorithm, where the number of clusters was selected based on the Silhouette metric that compares the distance between the elements in a cluster with the average distance between the elements of other clusters. It will make it possible to elucidate the factors that allow us to achieve the best results in terms of innovation (Figure 2).

Next, the relationship between the variables was modeled through a Bayesian network (BN). A BN is a probabilistic graphic model that represents a set of variables and their conditional dependencies through a directed acyclic graph (DAG). Bayesian networks can represent and solve decision problems under uncertainty; these are called influence diagrams [78].

In this work, the definition of the variables-parent node to a child-of the model is made up of 36 relevant factors to carry out the management of innovation and technology6 parent nodes and 30 child nodes-which are presented in Table 3.

Table 3. Definition of the variables and nodes.


Table 3. Cont.

-Pineapple crushing/cooking/grinding/agave juice extraction
-Fermentation
-Distillation | Optimum Regular Deficient  |

Table 3. Cont.


In this manner, the conceptual model is made and the Bayesian network was built from six parent nodes called competitive and technological intelligence, strategic planning,

technological planning, human capital, intellectual property protection, and quality and risk management (Figure 3 and Table 4).
![img-2.jpeg](img-2.jpeg)

Figure 3. Management of innovation and technology model: variables and nodes.

Table 4. Main correlations between variables for the management of innovation and technology model.


# 4. Results and Discussion 

### 4.1. Management of Innovation and Technology Model Results

The management of innovation and technology model's result was to develop the best practices of the leading companies in the tequila industry in Mexico.

Once the model was proposed using a Bayes network, multiple assignments were made to the probabilities for each variable (node) based on the experts' opinions until reaching the optimal configuration (Figure 4).

The probabilistic or propagation reasoning of probabilities is to disseminate the effects of evidence through the BN to know the subsequent probability of the other variables. That is, values are assigned to some variables (evidence), and the subsequent probability for the other variables is obtained, given the known variables.

In this way, the $97 \%$ probability of optimal management of innovation and technology was reached with the probabilities indicated in the model. That allows the company to generate value and competitive advantages.

It should be noted that the arcs that join the nodes have thickness and color intensity according to the strength of the interactions between nodes (Table 4).

The strength of influence is calculated from the conditional probability of the child node and expresses the distance between various conditional probability distributions over the child node conditional on the states of the parent node.

The variables protection of intellectual property and designation of origin have the most substantial interaction among all the variables.

The next step was the search for the most relevant variables for the classification, based on the objective variable management of innovation and technology. The RRelief metric indicates that the essential variables are knowledge management, MKT, organizational and technological architecture, national and international markets, cultivation of raw materials, agave, management, and use of waste (Table 5).

Next, the database clustering process was done. Two clusters were generated through the K-means algorithm; this allowed to group the records based on their similarities. In cluster 1 (C1) are grouped the registries with a denomination of origin and intellectual property protection. These pair of variables are the ones that showed strong linkage with each other. That is, the value of one of the influences that of the other (Figure 5).

Thus, C 1 has the desirable characteristics to achieve innovation. This is shown by the relationship between the most relevant variables. C1 shows that if the protection of intellectual property variable has a "YES" value, the cultivation of raw material variable obtains the optimal value in most cases (see Figure 6).

Similarly, it was found that if the knowledge management variables have optimum value, the sales and MKT variable has optimum value in most cases (see Figure 7).

Table 5. Most relevant variables for classification.


![img-3.jpeg](img-3.jpeg)

Figure 4. Bayes Network for management of innovation and technology in the tequila sector in Mexico.

![img-4.jpeg](img-4.jpeg)

Figure 5. Scatter plot for protection of intellectual property and designation of origin grouped by cluster.

![img-5.jpeg](img-5.jpeg)

Figure 6. Scatter plot for cultivation of raw vs. protection of intellectual property grouped by cluster.
![img-6.jpeg](img-6.jpeg)

Figure 7. Scatter plot for knowledge management vs. sales and MKT grouped by cluster.

# 4.2. Innovation and Industrial Property in the Tequila Sector 

The results show that in a low technology sector such as the tequila industry there is not much focus and investment towards research and development (R\&D). However, there is innovation. Innovation has allowed this low-tech sector to improve agricultural management processes, facilitating activities and reducing the risks to which workers are exposed. Likewise, it has been possible to mechanize tasks that allow the establishment of plantations in places where labor is scarce.

According to Cárdenas [81], over several decades, there have been significant technological advances in the tequila industry, which have been taken advantage of in all stages of its production process: cooking, grinding, fermentation, and distillation. However, these advances have been exploited unevenly due to the abysmal differences between large, medium, and small companies.

In addition to the above, there is also innovation in its products, where premium and superpremium artisan tequilas stand out and all tequila drinks.

On the other hand, the intensity of the innovation process can measure its results-outputs-and the efforts made to innovate-inputs. One of these ways of measuring innovation has been the patents obtained as an indicator of the result.

In the case of patents, in 2012 the tequila sector had 92, and in 2021, it has 120, representing an increase of $30.4 \%$ [82]. Concerning trademarks, in the year 2022 there are 1590 registered trademarks of packaging at the national level with a denomination of origin and 380 registered trademarks of packaging abroad with a denomination of origin. In addition, the number of trademarks registered as a tequila drink is 226 certified under the NMX-049-NORMEX-2004 standard [4,79].

For the tequila industry, the primary protection element is the denomination of origin certificate. The number of companies that produce tequila certified with a denomination of origin amounts to 272 by 2022. In addition, there are currently 118 companies for mixed tequila, while among $100 \%$ tequila companies there are 154 [4].

According to the above, a strong influence of other factors was confirmed to innovate in the tequila industry. These factors are characterized by focusing on innovation by process, organization, and marketing, which can compensate for the absence of formal efforts in internal R\&D [19,22,29,33,34].

In these sectors, the primary sources of knowledge to innovate come from social technologies associated with human resource management, work organization, and the search for external sources of innovation like customers and suppliers [19,26,27].

Therefore, R\&D as an input for innovation (output) plays a minor in this mature low-tech sector [29]. Instead, innovation results from a particular configuration of tacit and codified resources that firms build throughout their lives rather than strategies based on R\&D [19,29]. Thus, knowledge management practices (KMP) are a critical factor that directly affects innovation activities [32,34].

# 5. Conclusions 

Innovation and technology management are crucial in creating value for companies by allowing people and companies to use knowledge and existing resources more efficiently to learn and innovate. Moreover, the ability to manage it for the benefit of the business, aligned with the rest of its strategic functions considering a dynamic environment such as the current one, will allow it to maximize its competitive advantages. In other words, it is learning to identify or create opportunities, developing products with added value, looking for new ways to serve different consumers, detecting where and how new markets can be created and grown, rethinking services, among others, and seeking a social impact.

Implementing an innovation and technology management model allows companies to make better decisions to innovate and have competitive advantages. The benefits of this model are reflected in the new products or services, savings due to the development of new processes; entering new markets, increased sales, and higher profitability.

Based on this, a model has been generated through a Bayes network based on expert opinions in the tequila industry. A set of data was obtained based on the existing patterns between the nodes (variables).

The analysis of the data generated through the model has shown that according to their relevance for the classification, the essential variables for innovation are knowledge management, marketing, organizational and technological architecture, national and international markets, cultivation of raw materials, and management and use of waste, among others.

Likewise, it is shown that the variables that are related to greater strength through the arcs that join the nodes that represent them in the model are protection of intellectual property and designation of origin, strategic planning and mission, vision, values, value system model and clients, protection of intellectual property and sales, and MKT. These relationships emphasize the aspects that need to be taken care of to consolidate innovation.

Thus, it is essential to note that the variables that represent the concepts taken into account by experts in the field should be monitored and improved, considering the synergy suggested by the relationships between them and the relevance found through the analysis of the data generated using the patterns found in the designed model.

On the other hand, innovation can be of vital importance for the performance of low-tech companies. However, a large part of the public policies to stimulate innovation is focused on R\&D and in high-tech companies, which leaves out the low-tech sectors that have a significant impact on the economic development of countries. Moreover, the classification and use of the term low-tech sectors do not clarify the limits between high- and low-tech industries, affecting public policy formulation that supports these low-tech sectors.

In the case of the tequila sector, there are agricultural producers and small and mediumsized companies that could benefit from public policies focused on the knowledge of innovation and its application in their context. It would allow them to innovate to have competitive advantages and be more profitable and sustainable.

In summary, considering only formal R\&D activities in low-tech industries leaves out a large part of the productive apparatus with different competencies to innovate and not necessarily traditional R\&D activities.

In future work, it is recommended to consider more factors that improve innovation in the sustainability of the process. In this sense, relations with companies that participate in the world market for alcoholic beverages, mergers between these companies, and legal and informal national and international mechanisms regulate business networks and the consumption of these drinks.

Author Contributions: Conceptualization, A.T.-B., A.M.-V., V.M.C.-G. and S.A.-R.; methodology, A.T.-B. and A.M.-V.; software, A.T.-B. and A.M.-V.; validation A.T.-B. and A.M.-V.; formal analysis, A.T.-B. and A.M.-V.; investigation, A.T.-B., A.M.-V., V.M.C.-G. and S.A.-R.; resources, A.T.-B., A.M.-V., V.M.C.-G. and S.A.-R.; data curation, A.T.-B. and A.M.-V.; writing—original draft preparation, A.T.-B., A.M.-V., V.M.C.-G. and S.A.-R.; writing-review and editing, A.T.-B. and A.M.-V.; visualization, A.T.-B., A.M.-V., V.M.C.-G. and S.A.-R.; supervision, A.T.-B., A.M.-V., V.M.C.-G. and S.A.-R.; project administration, A.T.-B. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
