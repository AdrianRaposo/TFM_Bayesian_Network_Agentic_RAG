# The risk of additional branch works in the construction of railway projects 

Agnieszka Leśniak ${ }^{1}$, Filip Janowiec ${ }^{2}$, Jorge Rueda Benavides ${ }^{3}$


#### Abstract

Every decision or action taken as part of a construction project involves risk. Unforeseen branch works that may occur during the construction investment are the so-called additional work. They cause risk, both for the contractor and the investor. Skilful management of this risk may lead to minimizing the change in the investment duration or minimizing the change in the cost of the contractual amount. The work proposes a method of analysing the risk of industrial works that may occur during additional works in railway construction investments. A constructed Bayesian network based on the risk component of industrial works was used for the analysis. Bayesian networks are listed as one of the 31 techniques suggested for risk analysis in accordance with the ISO 31010 standard, which enables the correct analysis of the examined problem with satisfactory accuracy. During the construction of the network, historical data was obtained from completed and settled railway infrastructure construction projects, and 125 unique records corresponding to additional works were identified. The created Bayesian network combines technological aspects resulting from the specificity of the implementation of branch works in railway construction projects with a practical assessment of their risk. The proposed network model allows for risk analysis by defining various event scenarios, and has high application capacity resulting from the ease of applying its results in practice in the implementation of railway investments.


Keywords: risk assessment, Bayesian Belief Networks, construction, railway infrastructure, additional branch works

[^0]
[^0]:    ${ }^{1}$ Assoc. Prof. DSc., PhD., Eng., Cracow University of Technology, Faculty of Civil Engineering, ul. Warszawska 24, 31-155 Cracow, Poland, e-mail: agnieszka.lesniak@pk.edu.pl, ORCID: 0000-0002-4811-5574
    ${ }^{2}$ PhD., Eng., Cracow University of Technology, Faculty of Civil Engineering, ul. Warszawska 24, 31-155 Cracow, Poland, e-mail: filip.janowiec@pk.edu.pl, ORCID: 0000-0002-1627-7181
    ${ }^{3}$ Assoc. Prof.. PhD., Eng., Auburn University, College Of Engineering, Department of Civil and Environmental Engineering, 238 Harbert Center, Auburn, AL 36849 USA, e-mail: jrueda@auburn.edu, ORCID: 0000-0003-0334-6499

# 1. Introduction 

The construction of railway infrastructure in Poland is primarily related to the implementation of large national programs. Currently, one of the largest modernization programs - "National Railway Program until 2023" [1]. Its continuation will be another construction investment program, which is currently in the phase of consultations and obtaining funds for implementation. Its implementation is planned for the years 2023-2027 with the possibility of extension until 2030.

Following [1] there are over 19,500 km of railway lines in Poland. The railway infrastructure includes a number of building structures, linear structures and buildings [2]. In terms of construction, each of the listed elements has an individual category of a building structure specified in the Construction Law Act, is associated with a different technology of construction works and requires unique legal and organizational conditions [3].

Elements of the railway infrastructure, like any other building structure, must be constructed on the basis of superior regulations, i.e. in accordance with the rigor of the Construction Law [3]. The content of the Act classifies individual construction objects into one of 30 categories, according to their technical nature and manner of use. One element of railway infrastructure may be assigned to several different categories of building structures, and the final classification is decided by the designer responsible for preparation of technical documentation.

Due to the large variety of designers' approaches, construction works are divided into branches, corresponding to the scope of construction work actually performed, in accordance with the regulation [4]. Such a classification seems more reasonable, as it is directly related to the competencies of people performing independent technical functions in the construction industry (designers or site managers). There is no doubt that the categorization will depend on the subjective opinions of third parties. In addition, this division is used by the investor when creating key tender documents. This convention is also applied during the subsequent stages of the project, until its completion. Considering the above conditions, a similar division of branch works may include from several to a dozen or so types of works, depending on the size of the entire construction investment.

Dividing construction works into branches and understanding the characteristics of branch works can improve the description of common phenomena occurring during the implementation of the entire construction project. One of the best examples of work division applications for the problem under consideration seems to be additional works (variations) [5].

Unforeseen industry works that may occur during the construction project are the so-called additional works (less often - variation works) [6, 7]. They cause risk for both the contractor and the investor. Skilful management of this risk may lead to minimizing or avoiding cost and schedule growth [8-10]. It is therefore reasonable to get to know this phenomenon and to choose an appropriate risk management strategy, especially in the area of large construction projects, such as the construction of railway infrastructure.

Additional works in construction projects are a common phenomenon, occurring during the implementation of many types of building structures. The nature of these works,

their frequency of occurrence, as well as the effects depend on the specificity of the investment [11].

Correct mapping of additional works requires knowledge of the relevant parameters of the risk management models used. In the case of the previous works of the authors [6], these are primarily two basic parameters used to describe the risk - the probability of the occurrence of a certain event and its consequences. So far, attempts to investigate additional works have concerned projects in various regions of the world [6, 12, 13]. A detailed approach, dedicated to the risk of additional works in railway construction investments, has been presented in [6]. This method of risk description has been developed through the use of Bayesian networks, as well as the creation of a risk management component according to ISO 31000:2018 [14].

This article presents the method of creating a new part of the network, containing the characteristics of industry works in additional works, arising during the construction of railway infrastructure in Poland. Historical data from selected completed railway investments will be used to build the extension of the core network.

# 2. Risk in railway construction management 

### 2.1. Risk management according to international standards

Every decision or action taken as part of a construction project is susceptible to certain risks. As a rule, risk can be understood as a function of the probability of occurrence of certain events and their consequences [14]. It is assumed that these consequences may have a positive or negative impact on the course of the construction project. Positive effects are associated with gains of all kinds, while negative effects relate to losses or failures. Each party to the construction investment process should strive to maximize the likelihood of positive consequences and their scope, as well as to minimize the impact of negative consequences. All of these activities are called risk management. Depending on how risk is understood, its impact on the project and the goals of individual stakeholders managing the project, risk management can be radically different $[15,16]$.

A wide spectrum of various types of construction projects, as well as their location in the context of local legal regulations, influenced the development of many international risk management standards, adequate to regional conditions. Some of the key ones include: PMBOK [17], COSO ERM [18] and ISO 31000:2018 [14]. The most commonly used standard is the ISO 31000:2018 standard [14], as it is characterized by the most general approach, indicating to users the main guidelines and principles that they should follow when managing risk.

Risk management according to ISO 31000:2018 [14] is based on three key areas and their interdependencies, the understanding of which will determine the quality of the introduced risk management method, as well as its effects.pp. The authors of the standard indicate that the following issues should be properly known [14]: Risk management principles; Risk management framework; Risk management process. Only after analysing each element of

the listed issues can you start working directly with risk. The risk management framework is adopted as a starting point for further considerations (Fig. 1). According to the assumption, the performance of all specified actions guarantees the possibly correct and complete way of capturing the risk of the analysed issue.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Risk management framework according to ISO 31000. Source: own study based on [14]

The risk management framework illustrated in Fig. 1 allows for orderly, harmonized risk management, which can be comparable, measurable, and contribute to the correct response to emerging risks. Examples of applications of the ISO 31000 approach are successfully used in practice, in the case of general [19] and branch problems related to construction works [6].

# 2.2. Risk of railway construction projects 

A properly prepared and planned construction project should be preceded by a detailed risk analysis in order to minimize the negative consequences that may occur at subsequent stages of implementation. The risk management process includes several stages, including: identification, analysis and evaluation, which are usually crowned with risk assessment. This assessment includes the comparison of the obtained risk values to previously defined reference levels, allowing for the appropriate classification of the determined risk and the methods of its mitigation.

Risk management can be adapted to the type of construction objects for which this process will be carried out. Small residential buildings will be characterized by conditions different from those affecting large constructions that are part of the public infrastructure [20,21].

Effective risk management involves the use of many different methods, often including original methods, dedicated to various types of projects. The basic package of methods and techniques that can be used in the course of risk management is presented in the ISO 31010 standard [22].

Railway construction projects are the subject of many studies and analyses. Based on the works carried out so far, it can be concluded that many of the risks arising during the entire project are a set of well-recognized risks, and a large part is unique to the works carried out within the railway infrastructure. Among the unique risks, there are risks related to the administrative process or obtaining consents, arrangements and administrative decisions [23], the impact of the implementation of engineering structures on the entire investment [24], risks related to the certification of railway infrastructure to the requirements of the Technical Interoperability Specifications [25], or also shaping track layouts based on time or cost criteria in the context of the entire investment life cycle [26].

The multitude of unusual phenomena entails numerous risks that must be properly identified, quantified and assessed in order to minimize their impact, especially negative, on the entire project. For this purpose, public investors and other participants in the construction investment process conduct numerous talks and public dialogue. One of the effects of the work carried out to improve cooperation during the implementation of railway investments was the development and agreement of the so-called "Risk Matrix" [27], which is a set of good practices and a balanced division of many risks, including those that may arise during the implementation of works on railway infrastructure.

# 3. Materials and methods 

### 3.1. Bayesian belief networks

Bayesian Belief Networks (BBN) have numerous applications, but above all they show great utility for problems related to uncertainty, decision-makingpp. or other problems that are immeasurable, difficult to measure or based on incomplete knowledge [28]. BBN have been widely used for risk management purposes, including the management of risk of construction projects [29]. BBN are also listed as one of the 31 techniques suggested for risk analysis under ISO 31010 [22]. This allows us to believe that its adoption allows for a correct analysis of the examined problem with satisfactory accuracy.

The basic relationship used in the construction of the BBN is Thomas Bayes' theorem, which relates the conditional probabilities of two mutually conditioning events. The Thomas Bayes' theorem is represented by Eq. (3.1), while the conditional probability theorem is represented by Eq. (3.2) [30].

$$
P(A \mid B)=\frac{P(B \mid A) \times P(A)}{P(B)}
$$

where: $A$ and $B$ are events and $P(B)>0, P(A \mid B)$ - the probability of event $A$, provided that event $B$ occurs, $P(B \mid A)$ - the probability of event $B$, provided that event $A$ occurs

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

where: $A$ and $B$ are events and $P(B)>0, P(A \mid B)$ - the probability of event $A$, provided that event $B$ occurs, $P(A \cap B)$ - the probability of intersection of events $A$ and $B$.

The first approaches to applying the Bayes theorem were implemented for statistical analysis, which were classified into the so-called Bayesian inference. The systematic development of the undertaken issues in the field of statistics led to the proposition of a concept involving the combination of Bayesian reasoning with graph theory. On the basis of this proposal, a mathematical tool called Bayesian networks appeared, used in the decision theory of various research fields [28].

Bayesian networks are acyclic directed graphs in which the nodes represent events and the arcs (edges) the causal relationships (distributions of variables) between these events. Events in nodes are also called "states". The nodes of the network contain random variables described by probability distributions, or more often, defined by probabilities given at a fixed, known level - a determined probability level.

The use of the BBN in risk management allows for effective analysis of individual phases of the process, with particular emphasis on risk evaluation and its quantification [31]. This, in conclusion, allows for relatively easy risk mitigation and risk management proposals.

The practical application of this method has been observed for several years to more and more complex problems in the field of risk management in construction projects [32].

BBN are also successfully used to manage the risk of selected issues included in the management of construction projects. An example of such considerations is the paper [33], in which the authors focus on the risks associated with safety during construction works. Another research problem was presented in [34], where a BBN was created to analyze the degradation of existing structures. Yet another approach is presented in the work [6], where the problem of additional works in railway construction projects is discussed.

# 3.2. Additional branch works 

The number of factors influencing the creation of additional works is significant and is often associated with the individual characteristics of the analysed construction project. In the work [6], several factors were proposed that may be of key importance in the context of the occurrence of additional works. Regardless of their quantity and nature, they lead to the emergence of certain works that must be performed in order to properly perform the subject of the contract. Each additional work carried out within projects related to the construction of railway infrastructure will consist of several or a dozen or so interrelated works within construction industries.

With Poland's accession to the EU, numerous internal regulations were unified for the needs of the European rail transport market. One of the documents created is the Railway Transport Act [2], which contains all the definitions necessary for the proper functioning of railway transport. Appendix No. 1 to this Act is the "List of Elements of Railway Infrastructure" specifies the components of the railway route and accompanying devices. Based on the list of railway infrastructure elements and taking into account the specificity of independent technical functions in construction (described in Chapter 1 of the work), works can be divided into 9 basic types of branch works. This division is presented in Table 1.

This division will be used for the purposes of this article, and shortened names corresponding to the types of industry works will be used in the content of the work.

Table 1. Branch works


An example of industry additional works may be the discovery of a buried section of a railway track not inventoried in the submitted design documentation. According to the investor's decision, these works required its demolition, as well as the dismantling of all underground installations, including signalling devices. Thus, this additional work consisted of 3 types of branch works, i.e. track works, installation works and reconstruction of the signalling devices.

The occurrence of additional works is a phenomenon with a large number of combinations of branch additional works. Each of the possible situations may cause different consequences, as well as a different impact on the ongoing construction project. It seems extremely important to properly identify possible additional works, as well as link them with branch works. Knowledge derived from completed construction projects seems to be particularly important.

# 3.3. Historical data analysis 

In the course of the study presented in this paper, historical data was obtained from 16 completed and settled railway infrastructure construction projects in Poland. These data concerned large investments with a budget of over PLN 5,000,000.00 (EUR 1,152,286.14 - average NBP exchange rates as of December 31, 2018), completed and settled in the period from January 1, 2012, until December 31, 2018. All projects were related to the reconstruction of the railway infrastructure of the national manager of the railway network PKP PLK S.A.

The information received made it possible to quantify the risk of additional works and their consequences. However, previously unused data can be used to characterize the share of branch works in additional works.

Out of 16 analysed investments, data on additional works were selected. All contract documents, most often corresponding to individual additional works, were identified. It was decided that for the purposes of the work, they will be classified as individual branch works, and if they contain several types of works, they will be treated as a separate case. For example, an additional work associated with two branch works would be considered as two additional works with different types of branch works. This way of presenting data is more beneficial for people using the network, which will be discussed in more detail in the next section. For such conditions, 125 unique records were identified, corresponding to additional works. Each record was assigned to one of the previously accepted types of branch works. The number of individual branch works and their percentage share in the total number of records are presented in Table 2.

Table 2. Historical data


For the analysed historical data, it was possible to read the consequences of individual branch works in the form of changes in the duration of the investment (Table 3) and changes in the contractual amount (Table 4). Each of the consequences was assigned to one of the specified variants and expressed by the probability of occurrence.

Table 3. Duration change due to branch works


Table 3 - Continued from previous page


Table 4. Change in the contractual amount as a result of branch works


# 3.4. Branch works risk 

The context of the risk of additional works in the earlier works of the authors [6] was analysed in relation to the entire investment. The created model presented the possibility of the occurrence or non-occurrence of additional works, without their quantitative analysis. This assumption made it possible to focus on the consequences of all additional works occurring during the investment. The feedback received made it possible to assess how the risk of additional works affects the originally assumed duration of the investment and its base budget.

The risk of industrial works should be understood differently, focusing on more detailed information. These, in turn, should be related to the type of branch works and their consequences expressed in measurable values (amount in PLN thousand and time in days). The assumptions made in this way make it possible to obtain data in the context of a specific additional work. Thanks to the information received, it is possible to determine which type of branch works generates the most severe consequences, which of them should be avoided, and what is the general risk of this phenomenon.

A proprietary approach was used to assess the risk, based on a commonly used tool the risk matrix [15]. It was proposed that the risk reference levels should be characterized as combinations of both analysed consequences. This will allow for risk estimation in a probabilistic way, not in a deterministic way, as has been used so far. This method of risk estimation will allow for determination of risk together with information about the most probable level of risk. The risk matrix is presented in Table 5, while the description of risk levels is included in Table 6.

Table 5. Risk matrix


For the reference levels of the risk of branch works defined in this way, the construction of the model was commenced.

Table 6. Risk levels


# 4. Results and discussion 

The construction of the model began with the determination of the BBN topology. For this purpose, the cause-and-effect sequence leading to the occurrence of additional works was analysed. Next, the focus was on the possible consequences and the previously established risk reference levels. This led to the creation of the network layout shown in Fig. 2.
![img-1.jpeg](img-1.jpeg)

Fig. 2. BBN Topology

The starting point for further considerations will be the "additional works" node, from which the further part of the network, presenting the risk of additional works, will be derived. Subsequently, in accordance with the cause-and-effect chain, the following network nodes will be defined, representing respectively: branch works, their consequences and the risk assessment node. Four nodes of the BBN will be used to determine the risk of industrial works. The method of connecting the nodes will correspond to the previously defined network topology (Fig. 2). Events and their probabilities in individual network nodes will be assumed according to the described variants, in accordance with the following rule:

- "Additional works" node - authors' own research from [6];
- "Type of Works" node - data from Table 2;
- "Time Change" node - data from Table 3;
- "Amount Change" node - data from Table 4;
- "Risk level" node - data from Table 5.

Subsequently, the analysis of possible combinations of events and filling in the tables of conditional probabilities was started. In the case of modelling the risk matrix ("Risk Level" node), a "deterministic node" was used, while the others were defined as "general discrete nodes". After determining all possible events and conditional probabilities, the network was ready for use. BBN, along with the so-called "general scenario" is shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3. BBN "Risk of branch works"

The created Bayesian network allows for risk analysis by defining various scenarios of events. The result is information on the risk of branch works. The "Risk level" node presents a set of probabilities of all risk levels that depend on the given scenarios of events. These levels of risk can be adjusted to appropriate situations arising during construction and assembly, with particular emphasis on additional works.

A similar approach, i.e. referring to the assumed risk levels, is a common phenomenon used in research practice $[35,36]$. The created BBN models, however, require appropriate mathematical modelling, which should fully reflect the real process that may occur during construction works. This is undoubtedly a great difficulty because many of them are unique processes, highly complex or difficult to fully describe.

Comparable problems and uncertainties may be found in the BBN model created by the Authors, which allows to determine the risk of branch additional works. It should be noted, however, that the construction of the BBN itself is based on the probability of events, which allows modelling phenomena with high uncertainty [37].

In view of the above, and based on the results of previous research, it can be assumed that the Bayesian network model being created may be one of the best representations of the studied phenomenon.

# 5. Conclusions 

The paper proposes a way of analysing the risk of branch works that may appear during the occurrence of additional works in railway construction investments. The created BBN based on the risk component of branch works was used for the analysis. Individual event probabilities were determined through the collection, processing, and analysis of data and information from 16 railway infrastructure construction projects completed in Poland. It is worth noting that the ISO 31010 standard suggests the BBN method as one of the risk management methods [22]. In terms of the accuracy of the selection of influence factors, the adopted method is estimated by large resources and possibilities, small nature and degree of uncertainty, and high complexity [37]. This allows to believe that its adoption allows for a correct analysis of the examined problem with satisfactory accuracy. The article also proposes an original method of risk assessment, which presents combinations of both consequences (time and cost) of industry works.

The value of the determined risk can be related to your own expectations and previously defined criteria. The work proposed 5 levels of risk, the quantification of which was related to the combination of probability and consequences of branch works. The proposed risk levels are included in a risk matrix commonly used in practice. As a starting point for further analyses, a risk assessment was proposed for the general situation, i.e. a scenario containing all cases defined in the own research - based on the created BBN.

Modelling various scenarios of events corresponding to the real situation during the investment is one of the undoubted advantages of the created model. As a result of the conducted work, the following conclusions can be drawn:

- The created BBN combines technological aspects resulting from the specificity of the implementation of branch works in railway construction projects, along with a practical assessment of their risk.
- The model makes it possible to update probabilities at network nodes by using data from completed construction projects.
- The network has a high application capacity, resulting from the ease of applying its results in practice, during the implementation of railway investments.
The results obtained and the conclusions made allow the Authors to believe that the model can be used in practice and adapted to the expectations and needs of participants in the construction investment process in the railway industry. In order to fully confirm the researched thesis, the authors' own future research will be carried out, for which new cases of additional works carried out as part of other railway infrastructure.


# Ryzyko dodatkowych prac branżowych przy budowie inwestycji kolejowych 

Słowa kluczowe: ocena ryzyka, sieci Bayesa, budownictwo, infrastruktura kolejowa, prace dodatkowe

## Streszczenie:

Elementy infrastruktury kolejowej mogą zostać zakwalifikowane do kilkunastu różnych kategorii, a o ich finalnym sklasyfikowaniu decyduje projektant odpowiadający za sporządzenie dokumentacji technicznej. Wobec dużej różnorodności podejść projektantów stosuje się w praktyce podział robót budowlanych ze względu na branże, odpowiadające zakresom prac. Podział robót budowlanych na branże oraz zrozumienie charakterystyk prac branżowych może poprawić opis powszechnych zjawisk pojawiających się podczas realizacji przedsięwzięcia budowlanego. Jednym z przykładów podziału

prac wydają się być roboty dodatkowe, które w przedsięwzięciach budowlanych są zjawiskiem powszechnym, występującym w trakcie realizacji wielu rodzajów obiektów budowlanych. Charakter tych prac, ich częstość występowania, a także skutki zależą od specyfiki oraz otoczenia inwestycji. Sposób opisu ryzyka został rozwinięty przez autorów pracy we wcześniejszych publikacjach poprzez zastosowanie sieci bayesowskich, a także stworzeniu komponentu zarządzania ryzykiem wg normy PN-EN ISO 31000:2018. Opracowany model dał satysfakcjonujące wyniki i pozwolił na stosowanie metody w praktyce.

W niniejszym artykule zaprezentowano sposób tworzenia nowego fragmentu sieci, zawierającego charakterystykę robót branżowych w robotach dodatkowych, powstających podczas trwania przedsięwzięć budowy infrastruktury kolejowej w Polsce. Do budowy rozszerzenia sieci bazowej zostaną wykorzystane dane historyczne, pochodzące z zakończonych inwestycji kolejowych.

Każda decyzja podejmowana w ramach przedsięwzięcia budowlanego jest obarczona ryzykiem. Ryzyko można rozumieć jako funkcję prawdopodobieństwa wystąpienia pewnych zdarzeń oraz ich konsekwencji. Przyjmuje się, że konsekwencje te mogą oddziaływać pozytywnie, jak i negatywnie. Zarządzanie ryzykiem według ISO 31000:2018 opiera się na trzech kluczowych obszarach i ich wzajemnych zależności, od których zrozumienia zależeć będzie jakość metody zarządzania ryzykiem, a także jej efekty. Na podstawie dotychczasowych prac można stwierdzić, iż wiele z ryzyk pojawiających się podczas trwania przedsięwzięcia jest zbiorem dobrze rozpoznanych ryzyk, ale część z nich jest unikalna dla robót prowadzonych w obrębie infrastruktury kolejowej.

Sieci bayesowskie są wymieniane jako jedna z 31 technik sugerowanych do analizy ryzyka zgodnie z normą ISO 31010. Pozwala to sądzić, iż jej przyjęcie umożliwia prawidłową analizę badanego problemu przy zadowalającej dokładności. Podstawową zależnością wykorzystywaną przy budowie sieci jest twierdzenie Thomasa Bayesa, wiążące prawdopodobieństwa warunkowe dwóch zdarzeń warunkujących się nawzajem.

Nieprzewidziane roboty branżowe, które mogą się pojawić podczas trwania inwestycji budowlanej stanowią tzw. roboty dodatkowe. Powodują one ryzyko, zarówno wykonawcy, jak i inwestora. Umiejętne zarządzaniem tym ryzykiem może prowadzić do zminimalizowania zmiany czasu trwania inwestycji lub zminimalizowania zmiany kwoty umownej. Zasadnym jest zatem poznanie tego zjawiska oraz dobranie odpowiedniej strategii zarządzania ryzykiem, zwłaszcza w obrębie dużych przedsięwzięć, takich jak budowa infrastruktury kolejowej.

Występowanie robót dodatkowych, zwłaszcza robót branżowych jest zjawiskiem o dużej liczbie kombinacji. Każda z możliwych sytuacji może powodować różne konsekwencje, a także inny wpływ na inwestycję budowlaną. Niezwykle ważnym wydaje się, aby odpowiednio zidentyfikować możliwe roboty dodatkowe i powiązać je z robotami branżowymi. Szczególnie istotna wydaje się być wiedza, pochodząca z zakocena ryzyka, sieci Bayesa, budownictwo, infrastruktura kolejowa, prace dodatkoweończonych przedsięwzięć.

W trakcie prowadzonych badań pozyskano dane historyczne, pochodzące z 16 zakończonych przedsięwzięć budowy infrastruktury kolejowej w Polsce. Otrzymane informacje posłużyły do scharakteryzowania udziału robót branżowych w robotach dodatkowych. Aby informacje te mogły zostać zaaplikowane do nowego elementu sieci bayesowskich musiały zostać odpowiednio opracowane. Ostatecznie zidentyfikowano 126 unikalnych rekordów, odpowiadających robotom dodatkowym. Każdy rekord został przypisany do jednego z przyjętych typów robót branżowych. Dla analizowanych danych historycznych można było odczytać konsekwencje poszczególnych robót branżowych w postaci zmiany czasu trwania inwestycji oraz zmiany kwoty umownej. Każdą z konsekwencji przypisano do jednego z określonych wariantów i wyrażono za pomocą prawdopodobieństwa wystąpienia.

Do oceny ryzyka wykorzystano autorskie podejście, oparte na powszechnie stosowanym narzędziu - matrycy ryzyka. Zaproponowano, aby poziomy referencyjne ryzyka zostały scharakteryzowane

jako kombinacje obu analizowanych konsekwencji. Pozwoli to na oszacowanie ryzyka w sposób probabilistyczny, nie jak dotychczas stosowano, w sposób deterministyczny.

Budowę modelu rozpoczęto od etapu ustalenia topologii sieci bayesowskiej. W tym celu przeanalizowano ciąg przyczynowo - skutkowy prowadzący do wystąpienia robót dodatkowych. Następnie, skupiono się na możliwych konsekwencjach oraz wyznaczonych wcześniej poziomach referencyjnych ryzyka. Punktem wyjścia do dalszych rozważań został węzeł"roboty dodatkowe". Kolejno zdefiniowano następujące po sobie węzły sieci, przedstawiające odpowiednio: roboty branżowe, ich konsekwencje oraz węzeł oceny ryzyka. Zdarzenia oraz ich prawdopodobieństwa w poszczególnych węzłach sieci zostały przyjęte według opisanych szczegółowo w pracy wariantów. Po określeniu wszystkich możliwych zdarzeń oraz prawdopodobieństw warunkowych budowa modelu sieci została zakończona. Zaproponowany model pozwala na analizę ryzyka poprzez definiowanie różnych scenariuszy zdarzeń. Wynikiem analizy jest informacja na temat ryzyka robót branżowych. Węzeł "Poziom ryzyka" przedstawia zbiór prawdopodobieństw wszystkich poziomów ryzyka, które są uzależnione od zadanych scenariuszy zdarzeń. Wynikiem prowadzonej analizy ryzyka są prawdopodobieństwa wszystkich zdefiniowanych poziomów ryzyka. Poziomy te można dostosowywać do odpowiednich sytuacji pojawiających się podczas realizacji budowlano montażowych, ze szczególnym uwzględnieniem robót dodatkowych.

W pracy zaproponowano sposób analizy ryzyka robót branżowych mogących występować w ramach robót dodatkowych w inwestycjach kolejowych. Do analizy wykorzystano zbudowaną sieć bayesowską opartą o komponent ryzyka robót branżowych. W efekcie prowadzonych prac można sformułować następujące wnioski:

- Stworzona sieć bayesowska łączy aspekty technologiczne, wynikające z specyfiki realizacji robót branżowych w kolejowych przedsięwzięciach budowalnych wraz z praktycznym oszacowaniem ich ryzyka.
- Model umożliwia aktualizację prawdopodobieństw w węzłach sieci poprzez wykorzystanie danych pochodzących z zakończonych przedsięwzięć budowlanych.
- Sieć ma dużą zdolność aplikacyjną, wynikającą z łatwości stosowania jej wyników w praktyce, w trakcie realizacji inwestycji kolejowych.