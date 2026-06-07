# Artificial intelligence as law 

## Presidential address to the seventeenth international conference on artificial intelligence and law

Bart Verheij ${ }^{1}$

Published online: 14 May 2020
(c) The Author(s) 2020


#### Abstract

Information technology is so ubiquitous and AI's progress so inspiring that also legal professionals experience its benefits and have high expectations. At the same time, the powers of AI have been rising so strongly that it is no longer obvious that AI applications (whether in the law or elsewhere) help promoting a good society; in fact they are sometimes harmful. Hence many argue that safeguards are needed for AI to be trustworthy, social, responsible, humane, ethical. In short: AI should be good for us. But how to establish proper safeguards for AI? One strong answer readily available is: consider the problems and solutions studied in AI \& Law. AI \& Law has worked on the design of social, explainable, responsible AI aligned with human values for decades already, AI \& Law addresses the hardest problems across the breadth of AI (in reasoning, knowledge, learning and language), and AI \& Law inspires new solutions (argumentation, schemes and norms, rules and cases, interpretation). It is argued that the study of AI as Law supports the development of an AI that is good for us, making AI \& Law more relevant than ever.


Keywords Artificial intelligence $\cdot$ Law $\cdot$ Knowledge representation and reasoning $\cdot$ Machine learning $\cdot$ Natural language processing $\cdot$ Argumentation

[^0]
[^0]:    $\boxtimes$ Bart Verheij
    bart.verheij@rug.nl
    1 Department of Artificial Intelligence, Bernoulli Institute of Mathematics, Computer Science and Artificial Intelligence, University of Groningen, Groningen, The Netherlands

# 1 Introduction 

It is my pleasure to speak to you today ${ }^{1}$ on Artificial Intelligence and Law, a topic that I have already loved for so long-and I guess many of you too-and that today is in the center of attention.

It is not a new thing that technological innovation in the law has attracted a lot of attention. For instance, think of an innovation brought to us by the French 18th century freemason Joseph-Ignace Guillotin: the guillotine. Many people gathered at the Nieuwmarkt, Amsterdam, when it was first used in the Netherlands in 1812 (Fig. 1, left). The guillotine was thought of as a humane technology, since the machine guaranteed an instant and painless death.

And then a contemporary technological innovation that attracts a lot of attention: the self-driving car that can follow basic traffic rules by itself, so in that sense is an example of normware, an artificial system with embedded norms. In a recent news article, ${ }^{2}$ the story is reported that a drunk driver in Meppel in my province Drenthe in the Netherlands was driving his self-driving car. Well, he was riding his car, as the police discovered that he was tailing a truck, while sleeping behind the wheel, his car in autopilot mode. His driver's licence has been withdrawn.

And indeed technological innovation in AI is spectacular, think only of the automatically translated headline 'Drunken Meppeler sleeps on the highway', perhaps not perfect, but enough for understanding what is meant. Innovation in AI is going so fast that many people have become very enthusiastic about what is possible. For instance, a recent news item reports that Estonia is planning to use AI for automatic decision making in the law. ${ }^{3}$ It brings back the old fears for robot judges (Fig. 1, right).

Contrast here how legal data enters the legal system in France where it is since recently no longer allowed to use data to evaluate or predict the behavior of individual judges:

## LOI n ${ }^{0}$ 2019-222 du 23 mars 2019 de programmation 2018-2022 et de réforme pour la justice (1)—Article 33

Les données d'identité des magistrats et des membres du greffe ne peuvent faire l'objet d'une réutilisation ayant pour objet ou pour effet d'évaluer, d'analyser, de comparer ou de prédire leurs pratiques professionnelles réelles ou supposées.
[The identity data of magistrates and members of the registry cannot be reused with the purpose or effect of evaluating, analyzing, comparing or predicting their actual or alleged professional practices.]

[^0]
[^0]:    ${ }^{1}$ This text is an adapted version of the IAAIL presidential address delivered at the 17th International Conference on Artificial Intelligence and Law (ICAIL 2019) in Montreal, Canada (Cyberjustice Lab, University of Montreal, June 19, 2019).
    2 'Beschonken Meppeler rijdt slapend over de snelweg' (automatic translation: 'Drunken Meppeler sleeps on the highway'), RTV Drenthe, May 17, 2019.
    3 'Can AI be a fair judge in court? Estonia thinks so', Wired, March 25, 2019 (Eric Miller).

![img-0.jpeg](img-0.jpeg)

Fig. 1 Technological innovation in the law in the past (left) and in the future? (right). Left: Guillotine at the Nieuwmarkt in Amsterdam, 1812 (Rijksmuseum RP-P-OB-87.033, anonymous). Right: TV series Futurama, judge 723 (futurama.fandom.com/wiki/Judge_723)
![img-1.jpeg](img-1.jpeg)

Fig. 2 A car breaching traffic law, automatically identified

The fears are real, as the fake news and privacy disasters that are happening show. Even the big tech companies are considering significant changes, such as a data diet. ${ }^{4}$ But no one knows whether that is because of a concern for the people's privacy or out of fear for more regulation hurting their market dominance. Anyway, in China privacy is thought of very differently. Figure 2 shows an automatically identified car of which it is automatically decided that it is breaching traffic lawsee the red box around it. And indeed with both a car and pedestrians on the zebra crossing something is going wrong. Just this weekend the newspaper reported about

[^0]
[^0]:    4 'Het nieuwe datadieet van Google en Facebook' (automatic translation: 'The new data diet from Google and Facebook', nrc.nl, May 11, 2019.

how the Chinese public thinks of their social scoring system. ${ }^{5}$ It seems that the Chinese emphasise the advantages of the scoring system, as a tool against crimes and misbehavior.

Against this background of the benefits and risks of contemporary AI, the AI community in the Netherlands has presented a manifesto ${ }^{6}$ emphasising what is needed: an AI that is aligned with human values and society. In Fig. 3, key fields of research in AI are listed in rows, and in columns three key challenges are shown: first, AI should be social, and should allow for sensible interaction with humans; second, AI should be explainable, such that black box algorithms trained on data are made transparent by providing justifying explanations; and, third, AI should be responsible, in particular AI should be guided by the rules, norms, laws of society.

Also elsewhere there is more and more awareness of the need for a good, humane AI. For instance, the CLAIRE Confederation of Laboratories for AI Research in Europe ${ }^{7}$ uses the slogan

Excellence across all of AI
For all of Europe
With a Human-Centered Focus.
In other words, this emerging network advertises a strong European AI with social, explainable, responsible AI at its core.

And now a key point for today: AI \& Law has been doing this all along. At least since the start of its primary institutions-the biennial conference ICAIL (started in 1987 by IAAIL), ${ }^{8}$ the annual conference JURIX (started in 1988) ${ }^{9}$ and the journal Artificial Intelligence \& Law (in 1992)—, we have been working on good AI. In other words, AI \& Law has worked on the design of socially aware, explainable, responsible AI for decades already. One can say that what is needed in AI today is to do AI as we do law.

# 2 Legal technology today 

But before explaining how that could go let us look a bit at the current state of legal technology, for things are very different when compared to the start of the field of AI \& Law.

For one thing, all branches of government now use legal technology to make information accessible for the public and to provide services as directly and easily as possible. For instance, a Dutch government website ${ }^{10}$ provides access to laws, regulations and treaties valid in the Netherlands. The Dutch public prosecution provides an online knowledge-based system that gives access to fines and punishments

[^0]
[^0]:    5 'Zo stuurt en controleert China zijn burgers' (automatic translation: 'This is how China directs and controls its citizens', nrc.nl, June 14, 2019.
    ${ }^{6}$ bnvki.org/wp-content/uploads/2018/09/Dutch-AI-Manifesto.pdf.
    ${ }^{7}$ claire-ai.org.
    8 iaail.org.
    9 jurix.nl.
    10 wetten.overheid.nl.

![img-2.jpeg](img-2.jpeg)

Fig. 3 Artificial Intelligence Grid: foundational areas and multidisciplinary challenges (source: Dutch AI Manifesto ${ }^{6}$ )
in all kinds of offenses. ${ }^{11}$ There you can for instance find out what happens when the police catch you with an amount of marihuana between 5 and 30 grams. In the Netherlands, you have to pay 75 euros, and there is a note: also the drugs will be taken away from you. Indeed in the Netherlands all branches of government have online presence, as there is a website that gives access to information about the Dutch judicial system, including access to many decisions. ${ }^{12}$

An especially good example of successful legal technology is provided by the government's income tax services. ${ }^{13}$ In the Netherlands, filling out your annual tax form has become very simple. The software is good, it is easy to use, and best of all: in these days of big interconnected data much of what you need to fill in is already filled in for you. Your salary, bank accounts, savings, mortgage interest paid, the value of your house, it is all already there when you $\log$ in. In certain cases the tool even leaves room for some mild tax evasion-or tax optimisation if you like-since by playing with some settings a married couple can make sure that one partner has to pay just below the minimal amount that will in fact be collected, which can save about 40 euros.

One might think that such legal tech systems are now normal, but that is far from true. Many countries struggle with developing proper legal tech at the government level. One issue is that the design of complex systems is notoriously hard, and this is already true without very advanced AI.

[^0]
[^0]:    11 www.om.nl/onderwerpen/boetebase.
    12 uitspraken.rechtspraak.nl.
    13 www.belastingdienst.nl.

Also the Netherlands has had its striking failures. A scary example is the Dutch project to streamline the IT support of population registers. One would say a doable project, just databases with names, birth dates, marriages, addresses and the like. The project was a complete failure. ${ }^{14}$ After burning 90 million euros, the responsible minister-by the way earlier in his career a well-recognized scientist—had to pull the plug. Today all local governments are still using their own systems.

Still legal tech is booming, and focuses on many different styles of work. The classification used by the tech index maintained by the CodeX center for legal informatics at Stanford university distinguishes nine categories (Marketplace, Document Automation, Practice Management, Legal Research, Legal Education, Online Dispute Resolution, E-Discovery, Analytics and Compliance). ${ }^{15}$ It currently lists more than a 1000 legal tech oriented companies.

And on the internet I found a promising graph about how the market for legal technology will develop. Now it is worth already a couple of 100s of millions of dollars, but in a few years time that will have risen to 1.2 billion dollars-according to that particular prediction. I leave it to you to assess what such a prediction really means, but we can be curious and hopeful while following how the market will actually develop.

So legal tech clearly exists, in fact is widespread. But is it AI, in the sense of AI as discussed at academic conferences? Most of it not really. Most of what we see that is successful in legal tech is not really AI. But there are examples.

I don't know about you, but I consider the tax system just discussed to be a proper AI system. It has expert knowledge of tax law and it applies that legal expertise to your specific situation. True, this is largely good old-fashioned AI already scientifically understood in the 1970s, but by its access to relevant databases of the intercon-nected-big-data kind, it certainly has a modern twist. One could even say that the system is grounded in real world data, and is hence an example of situated AI, in the way that the term was used in the 1990s (and perhaps before). But also this is clearly not an adaptive machine learning AI system, as is today expected of AI.

# 3 AI \& law is hard 

The reason why much of the successful legal tech is not really AI is simple. AI \& Law is hard, very hard. In part this explains why many of us are here in this room. We are brave, we like the hard problems. In AI \& Law they cannot be evaded.

Let us look at an example of real law. We go back to the year when I was born when pacifism was still a relevant political attitude. In that year the Dutch Supreme court decided that the inscription 'The Netherlands disarm', mounted on a tower (Fig. 4) was not an offense. ${ }^{16}$ The court admitted that indeed the sign could be

[^0]
[^0]:    14 'ICT-project basisregistratie totaal mislukt' (automatic translation: 'IT project basic registration totally failed'), nrc.nl, July 17, 2017.
    15 techindex.law.stanford.edu.
    16 Supreme Court The Netherlands, January 24, 1967: Nederland ontwapent (The Netherlands disarm).

![img-3.jpeg](img-3.jpeg)

Fig. 4 Nederland ontwapent (The Netherlands disarm). Source: Nationaal Archief, 2.24.01.03, 918-0574 (Joost Evers, Anefo)
considered a violation of Article 1 of the landscape management regulation of the province of North Holland, but the court decided that that regulation lacked binding power by a conflict with the freedom of speech, as codified in Article 7 of the Dutch constitution.

An example of a hard case. This outcome and its reasoning could not really be predicted, which is one reason why the case is still taught in law schools.

The example can be used to illustrate some of the tough hurdles for the development of AI \& Law as they have been recognized from the start; here a list used by Rissland (1988) when reviewing Anne Gardner's pioneering book 'An AI approach to legal reasoning' (Gardner 1987), a revision of her 1984 Stanford dissertation. ${ }^{17}$ I am happy that both are present in this room today.

1. Legal reasoning is rule-guided, rather than rule-governed In the example, indeed both the provincial regulation and the constitution were only guiding, not governing. Their conflict had to be resolved. A wise judge was needed.
2. Legal terms are open textured In the example it is quite a stretch to interpret a sign on a tower as an example of speech in the sense of freedom of speech, but that is what the court here did. It is the old puzzle of legally qualifying the facts, not at all an easy business, also not for humans. With my background in mathematics, I found legal qualification to be a surprisingly and unpleasantly underspecified problem when I took law school exams during my first years as assistant professor
[^0]
[^0]:    ${ }^{17}$ For more on the complexity of AI \& Law, see for instance (Rissland 1983; Sergot et al. 1986; BenchCapon et al. 1987, 2012; Rissland and Ashley 1987; Oskamp et al. 1989; Ashley 1990, 2017; van den Herik 1991; Berman and Hafner 1995; Loui and Norman 1995; Bench-Capon and Sartor 2003; Sartor 2005; Zurek and Araszkiewicz 2013; Lauritsen 2015).

![img-4.jpeg](img-4.jpeg)

Fig. 5 The subsumption model
in legal informatics in Maastricht, back in the 1990s. Today computers also still would have a very hard time handling open texture.
3. Legal questions can have more than one answer, but a reasonable and timely answer must be given I have not checked how quickly the supreme court made its decision, probably not very quickly, but the case was settled. The conflict was resolved. A solution that had not yet been there, had been created, constructed. The decision changed a small part of the world.
4. The answers to legal questions can change over time In the example I am not sure about today's law in this respect, in fact it is my guess that freedom of speech is still interpreted as broadly as here, and I would not be surprised when it is now interpreted even more broadly. But society definitely has changed since the late 1960s, and what I would be surprised about is when I would today see such a sign in the public environment.

One way of looking at the hurdles is by saying that the subsumption model is false. According to the subsumption model of law there is a set of laws, thought of as rules, there are some facts,-and you arrive at the legal answers, the legal consequences by applying the rules to the facts (Fig. 5). The case facts are subsumed under the rules, providing the legal solution to the case. It is often associated with Montesquieu's phrase of the judge as a 'bouche de la loi', the mouth of the law, according to which a judge is just the one who makes the law speak.

All hurdles just mentioned show that this perspective cannot be true. Rules are only guiding, terms are open-textured, there can be more answers, and things can change.

Hence an alternative perspective on what happens when a case is decided. Legal decision making is a process of constructing and testing a theory, a series of hypotheses that are gradually developed and tested in a critical discussion (Fig. 6). The figure suggests an initial version of the facts, an initial version of the relevant rules, and an initial version of the legal conclusions. Gradually the initial hypothesis is adapted. Think of

![img-5.jpeg](img-5.jpeg)

Fig. 6 The theory construction model (Verheij 2003a, 2005)
what happens in a court proceedings, and in what in the Netherlands is called the 'raadkamer', the internal discussion among judges, where after a careful constructive critical discussion-if the judges get the time for that of course-finally a tried and tested perspective on the case is arrived at, showing the final legal conclusions subsuming the final facts under the final rules. This is the picture I used in the 2003 AI \& Law special issue of the AI journal, edited by Edwina Rissland, Kevin Ashley, and Ronald Loui, two of them here in this room. A later version with Floris Bex emphasises that also the perspective on the evidence and how it supports the facts is gradually constructed (Bex and Verheij 2012). In our field, the idea of theory construction in the law has for instance been emphasised by McCarty (1997), Hafner and Berman (2002), Gordon (1995), Bench-Capon and Sartor (2003) and Hage et al. (1993).

# 4 Al as law 

Today's claim is that good AI requires a different way of doing AI, a way that we in the field of AI \& Law have been doing all along, namely doing AI in a way that meets the requirements of the law, in fact in a way that models how things are done in the law. Let us discuss this perspective a bit further.

There can be many metaphors on what AI is and how it should be done, as follows.

1. AI as mathematics, where the focus is on formal systems;
2. AI as technology, where the focus is on the art of system design;
3. AI as psychology, where the focus is on intelligent minds;
4. AI as sociology, where the focus is on societies of agents.

And then AI as law, to which we return in a minute (Table 1).

Table 1 AI metaphors


In AI as mathematics, one can think of the logical and probabilistic foundations of AI, indeed since the start and still now of core importance. It is said that the namegiver of the field of AI—John McCarty-thought of the foundations of AI as an instance of logic, and logic alone. In contrast today some consider AI to be a kind of statistics 2.0 or 3.0 .

In AI as technology, one can think of meticulously crafted rule-based expert systems or of machine learning algorithms evaluated on large carefully labeled data sets. In AI as technology, AI applications and AI research meet most directly.

In AI as psychology, one can think of the modeling of human brains as in cognitive modeling, or of the smart human-like algorithms that are sometimes referred to as cognitive computing.

In AI as sociology, one can think of multi-agent systems simulating a society and of autonomous robots that fly in flocks.

Perhaps you have recognized the list of metaphors as the ones used by Toulmin (1958) when he discussed what he thought of as a crisis in the formal analysis of human reasoning. He argued that the classical formal logic then fashionable was too irrelevant for what reasoning actually was, and he arrived at a perspective of logic as law. ${ }^{18}$ What he meant was that counterargument must be considered, that rules warranting argumentative steps are material-and not only formal-, that these rules are backed by factual circumstances, that conclusions are often qualified, uncertain, presumptive, and that reasoning and argument are to be thought of as the outcome of debates among individuals and in groups (see also Hitchcock and Verheij 2006; Verheij 2009). All of these ideas emphasised by Toulmin have now been studied extensively, with the field of AI \& Law having played a significant role in the developments. ${ }^{19}$

The metaphors can also be applied to the law, exposing some key ideas familiar in law.

[^0]
[^0]:    ${ }^{18}$ Toulmin (1958) speaks of logic as mathematics, as technology, as psychology, as sociology and as law (jurisprudence).
    ${ }^{19}$ See for instance the research by Prakken (1997), Sartor (2005), Gordon (1995), Bench-Capon (2003) and Atkinson and Bench-Capon (2006). Argumentation research in AI \& Law is connected to the wider study of formal and computational argumentation, see for instance (Simari and Loui 1992; Pollock 1995; Vreeswijk 1997; Chesñevar et al. 2000). See also the handbooks (Baroni et al. 2018; van Eemeren et al. 2014).

If we think of law as mathematics, the focus is on the formality of procedural rule following and of stare decisis where things are well-defined and there is little room for freedom.

In law as technology, one can think of the art of doing law in a jurisdiction with either a focus on rules, as in civil law systems, or with a focus on cases, as in common law systems.

In law as psychology, one can think of the judicial reasoning by an individual judge, and of the judicial discretion that is to some extent allowed, even wanted.

In law as sociology, the role of critical discussion springs to mind, and of regulating a society in order to give order and prevent chaos.

And finally the somewhat pleonastic metaphor of law as law, but now as law in contrast with the other metaphors. I think of two specific and essential ideas in the law, namely that government is to be bound by the rule of law, and that the goal of law is to arrive at justice, thereby supporting a good society and a good life for its citizens.

Note how this discussion shows the typically legal, hybrid balancing of different sides: rules and cases, regulations and decisions, rationality and interpretation, individual and society, boundedness and justice. And as we know this balancing best takes place in a constructive critical discussion.

Which brings us to bottom line of the list of AI metaphors (Table 1).
5. AI as law, where the focus is on hybrid critical discussion.

In AI as law, AI systems are to be thought of as hybrid critical discussion systems, where different hypothetical perspectives are constructed and evaluated until a good answer is found.

In this connection, I recently explained what I think is needed in AI (Fig. 7), namely the much needed step we have to make towards hybrid systems that connect knowledge representation and reasoning techniques with the powers of machine learning. In this diagram I used the term argumentation systems. But since argumentation has a very specific sound in this community, and perhaps to some feels as a too specific, too limiting perspective, I today speak of AI as Law in the sense of the development of hybrid critical discussion systems.

# 5 Topics in AI 

Let me continue with a discussion of core topics in AI with the AI as Law perspective in mind. My focus is on reasoning, knowledge, learning and language.

### 5.1 Reasoning

First reasoning. I then indeed think of argumentation where arguments and counterarguments meet (van Eemeren et al. 2014; Atkinson et al. 2017; Baroni et al. 2018). This is connected to the idea of defeasibility, where arguments become defeated when attacked by a stronger counterargument. Argumentation has been used to

Fig. 7 Bridging the gap between knowledge and data systems in AI (Verheij 2018)
![img-6.jpeg](img-6.jpeg)
address the deep and old puzzles of inconsistency, incomplete information and uncertainty.

Here is an example argument about the Dutch bike owner Mary whose bike is stolen (Fig. 8). The bike is bought by John, hence both have a claim to ownershipMary as the original owner, John as the buyer. But in this case the conflict can be resolved as John bought the bike for the low price of 20 euros, indicating that he was not a bona fide buyer. At such a price, he could have known that the bike was stolen, hence he has no claim to ownership as the buyer, and Mary is the owner.

It is one achievement of the field of AI \& Law that the logic of argumentation is by now well understood, so well that it can be implemented in argumentation diagramming software that applies the logic of argumentation, for instance the ArguMed software that I implemented long ago during my postdoc period in the Maastricht law school (Verheij 2003a, 2005). ${ }^{20}$ It implements argumentation semantics of the stable kind in the sense of Dung's abstract argumentation that was proposed some 25 years ago (Dung 1995), a turning point and a cornerstone in today's understanding of argumentation, with many successes. Abstract argumentation also gave new puzzles such as the lack of standardization leading to all kinds of detailed comparative formal studies, and more fundamentally the multiple formal semantics puzzle. The stable, preferred, grounded and complete semantics were the four proposed by Dung (1995), quickly thereafter extended to 6 when the labeling-based stage and semi-stable semantics were proposed (Verheij 1996). But that was only the start because the field of computational argumentation was then still only emerging.

For me, it was obvious that a different approach was needed when I discovered that after combining attack and support 11 different semantics were formally possible (Verheij 2003b), but practically almost all hardly relevant. No lawyer has to think about whether the applicable argumentation semantics is the semi-stable or the stage semantics.

One puzzle in the field is the following, here included after a discussion on the plane from Amsterdam to Montreal with Trevor Bench-Capon and Henry Prakken. A key idea underlying the original abstract argumentation paper is that derivationlike arguments can be abstracted from, allowing to focus only on attack. I know that for many this idea has helped them in their work and understanding of argumentation. For me, this was-from rather early on-more a distraction than an advantage

[^0]
[^0]:    ${ }^{20}$ For some other examples, see (Gordon et al. 2007; Loui et al. 1997; Kirschner et al. 2003; Reed and Rowe 2004; Scheuer et al. 2010; Lodder and Zelznikow 2005).

![img-7.jpeg](img-7.jpeg)

Fig. 8 Argumentation
as it introduced a separate, seemingly spurious layer. In the way that my PhD supervisor Jaap Hage put it: 'those cloudy formal structures of yours' - and Jaap referred to abstract graphs in the sense of Dung-have no grounding in how lawyers think. There is no separate category of supporting arguments to be abstracted from before considering attack; instead, in the law there are only reasons for and against conclusions that must be balanced. Those were the days when Jaap Hage was working on Reason-Based Logic (1997) and I was helping him (Verheij et al. 1998). In a sense, the ArguMed software based on the DefLog formalism was my answer to removing that redundant intermediate layer (still present in its precursor the Argue! system), while sticking to the important mathematical analysis of reinstatement uncovered by Dung (see Verheij 2003a, 2005). For background on the puzzle of combining support and attack, see (van Eemeren et al. 2014, Sect. 11.5.5).

But as I said from around the turn of the millenium I thought a new mathematical foundation was called for, and it took me years to arrive at something that really increased my understanding of argumentation: the case model formalism (Verheij 2017a, b), but that is not for now.

# 5.2 Knowledge 

The second topic of AI to be discussed is knowledge, so prominent in AI and in law. I then think of material, semi-formal argumentation schemes such as the witness testimony scheme, or the scheme for practical reasoning, as for instance collected in the nice volume by Walton et al. (2008).

I also think of norms, in our community often studied with a Hohfeldian or deontic logic perspective on rights and obligations as a background. ${ }^{21}$ And then there are the ontologies that can capture large amounts of knowledge in a systematic way. ${ }^{22}$

[^0]
[^0]:    ${ }^{21}$ See for instance (Sartor 2005; Gabbay et al. 2013; Governatori and Rotolo 2010).
    ${ }^{22}$ See for instance (McCarty 1989; Valente 1995; van Kralingen 1995; Visser 1995; Visser and BenchCapon 1998; Hage and Verheij 1999; Boer et al. 2002, 2003; Breuker et al. 2004; Hoekstra et al. 2007; Wyner 2008; Casanovas et al. 2016).

One lesson that I have taken home from working in the domain of law-and again don't forget that I started in the field of mathematics where things are thought of as neat and clean-one lesson is that in the world of law things are always more complex than you think. One could say that it is the business of law to find the exactly right level of complexity, and that is often just a bit more complex than one's initial idea. And if things are not yet complex now, they can become tomorrow. Remember the dynamics of theory construction that we saw earlier (Fig. 6).

Figure 9 (left) shows how in the law different categories of juristic facts are distinguished. Here juristic facts are the kind of facts that are legally relevant, that have legal consequences. They come in two kinds: acts with legal consequences, and bare juristic facts, where the latter are intentionless events such as being born, which still have legal consequences. And acts with legal consequences are divided in on the one hand juristic acts aimed at a legal consequence (such as contracting), and on the other factual acts, where although there is no legal intention, still there are legal consequences. Here the primary example is that of unlawful acts as discussed in tort law. I am still happy that I learnt this categorization of juristic facts in the Maastricht law school, as it has relevantly expanded my understanding of how things work in the world. And of how things should be done in AI. Definitely not purely logically or purely statistically, definitely with much attention for the specifics of a situation.

Figure 9 (right) shows another categorization, prepared with Jaap Hage, that shows how we then approached the core categories of things, or 'individuals' that should be distinguished when analyzing the law: states of affairs, events rules, other individuals, and then the subcategories of event occurrences, rule validities and other states of affairs. And although such a categorization does have a hint of the baroqueness of Jorge Luis Borges' animal taxonomy (that included those animals that belong to the emperor, mermaids and innumerable animals), the abstract core ontology helped us to analyze the relations between events, rules and states of affairs that play a role when signing a contract (Fig. 10). Indeed at first sight a complex picture. For now it suffices that at the top row there is the physical act of signing-say when the pen is going over the paper to sign-and this physical act counts as engaging in a contractual bond (shown in the second row), which implies the undertaking of an obligation (third row), which in turn leads to a duty to perform an action (at the bottom row). Not a simple picture, but as said, in the law things are often more complex than expected, and typically for good, pragmatic reasons.

The core puzzle for our field and for AI generally that I would like to mention is that of commonsense knowledge. This remains an essential puzzle, also in these days of big data; also in these days of cognitive computing. Machines simply don't have commonsense knowledge that is nearly good enough. A knowledgeable report in the Communications of the ACM explains that progress has been slow (Davis and Marcus 2015). It goes back to 2015, but please do not believe it when it is suggested that things are very different today. The commonsense knowledge problem remains a relevant and important research challenge indeed and I hope to see more of the big knowledge needed for serious AI \& Law in the future. Only brave people have the chance to make real progress here, like the people in this room.

One example of what I think is an as yet underestimated cornerstone of commonsense knowledge is the role of globally coherent knowledge structures-such as

![img-8.jpeg](img-8.jpeg)

Fig. 9 Types of juristic facts (left); tree of individuals (right) (Hage and Verheij 1999)
the scenarios and cases we encounter in the law. Our current program chair Floris Bex took relevant steps to investigate scenario schemes and how they are hierarchically related, in the context of murder stories and crime investigation (Bex 2011). ${ }^{23}$ Our field would benefit from more work like this, that goes back to the frames and scripts studied by people such as Roger Schank and Marvin Minsky.

My current favorite kind of knowledge representation uses the case models mentioned before. It has for instance been used to represent how an appellate court gradually constructs its hypotheses about a murder case on the basis of the evidence, gradually testing and selecting which scenario of what has happened to believe or not (Verheij 2019), and also to the temporal development of the relevance of past decisions in terms of the values they promote and demote (Verheij 2016).

# 5.3 Learning 

Then we come to the topic of learning. It is the domain of statistical analysis that shows that certain judges are more prone to supporting democrat positions than others, and that as we saw no longer is allowed in France. It is the domain of open data, that allows public access to legal sources and in which our community has been very active (Biagioli et al. 2005; Francesconi and Passerini 2007; Francesconi et al. 2010a, b; Sartor et al. 2011; Athan et al. 2013). And it is the realm of neural networks, back in the days called perceptrons, now referred to as deep learning.

The core theme to be discussed here is the issue of how learning and the justification of outcomes go together, using a contemporary term: how to arrive at an explainable AI, an explainable machine learning. We have heard it discussed at all career levels, by young PhD students and by a Turing award winner.

The issue can be illustrated by a mock prediction machine for Dutch criminal courts. Imagine a button that you can push, that once you push it always gives the outcome that the suspect is guilty as charged. And thinking of the need to evaluate systems (Conrad and Zeleznikow 2015), this system has indeed been validated by the Dutch Central Bureau of Statistics, that has the data that shows that

[^0]
[^0]:    ${ }^{23}$ For more work on evidence in AI \& Law, see for instance (Keppens and Schafer 2006; Bex et al. 2010; Keppens 2012; Fenton et al. 2013; Vlek et al. 2014; Di Bello and Verheij 2018).

![img-9.jpeg](img-9.jpeg)

Fig. 10 Signing a sales contract (Hage and Verheij 1999)
this prediction machine is correct in 91 out of a 100 cases (Fig. 11). The validating data shows that the imaginary prediction machine has become a bit less accurate in recent years, presumably by changes in society, perhaps in part caused by the attention in the Netherlands for so-called dubious cases, or miscarriages of justice, which may have made judges a little more reluctant to decide for guilt. But still: $91 \%$ for this very simple machine is quite good. And as you know, all this says very little about how to decide for guilt or not.

How hard judicial prediction really is, also when using serious machine learning techniques, is shown by some recent examples. Katz et al. (2017) that their US Supreme Court prediction machine could achieve a $70 \%$ accuracy. A mild improvement over the baseline of the historical majority outcome (to always affirm a previous decision) which is $60 \%$, and even milder over the 10 year majority outcome which is $67 \%$. The system based its predictions on features such as judge identity, month, court of origin and issue, so modest results are not surprising.

In another study Aletras and colleagues (2016) studied European Court of Human Rights cases. They used n-grams and topics as the starting point of their training, and used a prepared dataset to make a cleaner baseline of $50 \%$ accuracy by random guessing. They reached $79 \%$ accuracy using the whole text, and noted that by only using the part where the factual circumstances are described already an accuracy of $73 \%$ is reached.

Naively taking the ratios of 70 over 60 and of 79 over 50, one sees that factors of 1.2 and of 1.6 improvement are relevant research outcomes, but practically modest. And more importantly these systems only focus on outcome, without saying anything about how to arrive at an outcome, or about for which reasons an outcome is warranted or not.

![img-10.jpeg](img-10.jpeg)

Fig. 11 Convictions in criminal cases in the Netherlands; source: Central Bureau of Statistics (www.cbs. nl), data collection of September 11, 2017

And indeed and as said before learning is hard, especially in the domain of law. ${ }^{24}$ I am still a fan of an old paper by Trevor Bench-Capon on neural networks and open texture (Bench-Capon 1993). In an artificially constructed example about welfare benefits, he included different kinds of constraints: boolean, categorical, numeric. For instance, women were allowed the benefit after 60, and men after 65. Trevor found that after training, the neural network could achieve a high overall performance, but with somewhat surprising underlying rationales. In Fig. 12, on the left, one can see that the condition starts to be relevant long before the ages of 60 and 65 and that the difference in gender is something like 15 years instead of 5 . On the right, with a more focused training set using cases with only single failing conditions, the relevance started a bit later, but still too early, while the gender difference now indeed was 5 years.

What I have placed my bets on is the kind of hybrid cases and rules systems that for us in AI \& Law are normal. ${ }^{25}$ I now represent Dutch tort law in terms of case models validating rule-based arguments (Verheij 2017b) (cf. Fig. 13 below).

# 5.4 Language 

Then language, the fourth and final topic of AI that I would like to discuss with you. Today the topic of language is closely connected to machine learning. I think of the labeling of natural language data to allow for training; I think of prediction such

[^0]
[^0]:    ${ }^{24}$ See also recently (Medvedeva et al. 2019).
    ${ }^{25}$ See for instance work by (Branting 1991; Skalak and Rissland 1992; Branting 1993; Prakken and Sartor 1996, 1998; Stranieri et al. 1999; Roth 2003; Brüninghaus and Ashley 2003; Atkinson and BenchCapon 2006; Čyras et al. 2016).

![img-11.jpeg](img-11.jpeg)

Fig. 12 Neural networks and open texture (Bench-Capon 1993)
![img-12.jpeg](img-12.jpeg)

Fig. 13 Arguments, rules and cases for Dutch tort law (Verheij 2017b)
as by a search engine or chat application on a smartphone, and I think of argument mining, a relevant topic with strong roots in the field of AI \& Law.

The study of natural language in AI, and in fact of AI itself, got a significant boost by IBM's Watson system that won the Jeopardy! quiz show. For instance, Watson correctly recognized the description of 'A 2-word phrase [that] means the power to take private property for public use'. That description refers to the typically legal concept of eminent domain, the situation in which a government disowns property for public reasons, such as the construction of a highway or windmill park. Watson's output showed that the legal concept scored $98 \%$, but also 'electric company' and 'capitalist economy' were considered with $9 \%$ and $5 \%$ scores, respectively. Apparently Watson sees some kind of overlap between the legal concept of eminent domain, electric companies and capitalist economy, since $98+9+5$ is more than a 100 percent.

And IBM continued, as Watson was used as the basis for its debating technologies. In a 2014 demonstration, ${ }^{26}$ the system is considering the sale of violent video

[^0]
[^0]:    ${ }^{26}$ Milken Institute Global Conference 2014, session 'Why Tomorrow Won’t Look Like Today: Things that Will Blow Your Mind', youtu.be/6fJOtAzICzw?t=2725.

games to minors. The video shows that the system finds reasons for and against banning the sale of such games to minors, for instance that most children who play violent games do not have problems, but that violent video games can increase children's aggression. The video remains impressive, and for the field of computational argumentation that I am a member of it was somewhat discomforting that the researchers behind this system were then outsiders to the field.

The success of these natural language systems leads one to think about why they can do what they do. Do they really have an understanding of a complex sentence describing the legal concept of eminent domain; can they really digest newspaper articles and other online resources on violent video games?

These questions are especially relevant since in our field of AI \& Law we have had the opportunity to follow research on argument mining from the start. Early and relevant research is by Raquel Mochales Palau and Sien Moens, who studied argument mining in a paper at the 2009 ICAIL conference $(2009,2011)$. And as already shown in that paper, it should not be considered an easy task to perform argument mining. Indeed the field has been making relevant and interesting progress, as also shown in research presented at this conference, but no one would claim the kind of natural language understanding needed for interpreting legal concepts or online debates. ${ }^{27}$

So what then is the basis of apparent success? Is it simply because a big tech company can do a research investment that in academia one can only dream of? Certainly that is a part of what has been going on. But there is more to it than that as can be appreciated by a small experiment I did, this time actually an implemented online system. It is what I ironically called Poor Man's Watson, ${ }^{28}$ which has been programmed without much deep natural language technology, just some simple regular expression scripts using online access to the Google search engine and Wikipedia. And indeed it turns out that the simple script can also recognize the concept of eminent domain: when one types 'the power to take private property for public use' the answer is 'eminent domain'. The explanation for this remarkable result is that for some descriptions the correct Wikipedia page ends up high in the list of pages returned by Google, and that happens because we-the people-have been typing in good descriptions of those concepts in Wikipedia, and indeed Google can find these pages. Sometimes the results are spectacular, but also they are brittle since seemingly small, irrelevant changes can quickly break this simple system.

And for the debating technology something similar holds since there are web sites collecting pros and cons of societal debates. For instance, the web site procon.org has a page on the pros and cons of violent video games. ${ }^{29}$ Arguments it has collected include 'Pro 1: Playing violent video games causes more aggression, bullying, and fighting' and 'Con 1: Sales of violent video games have significantly increased while violent juvenile crime rates have significantly decreased'. The web

[^0]
[^0]:    ${ }^{27}$ See for instance (Schweighofer et al. 2001; Wyner et al. 2009, 2010; Grabmair and Ashley 2011; Ashley and Walker 2013; Grabmair et al. 2015; Tran et al. 2020).
    ${ }^{28}$ Poor Man's Watson, www.ai.rug.nl/ verheij/pmw.
    29 videogames.procon.org.

site Kialo has similar collaboratively created lists. ${ }^{30}$ Concerning the issue 'Violent video games should be banned to curb school shootings', it lists for instance the pro 'Video games normalize violence, especially in the eyes of kids, and affect how they see and interact with the world' and the con 'School shootings are, primarily, the result of other factors that should be dealt with instead'.

Surely the existence of such lists typed in, in a structured way, by humans is a central basis for what debating technology can and cannot do. It is not a coincidence that-listening carefully to the reports-the examples used in marketing concern curated lists of topics. At the same time this does not take away the bravery of IBM and how strongly it has been stimulating the field of AI by its successful demos. And that also for IBM things are sometimes hard is shown by the report from February 2019 when IBM's technology entered into a debate with a human debater, and this time lost. ${ }^{31}$ But who knows what the future brings.

What I believe is needed is the development of an ever closer connection between complex knowledge representations and natural language explanations, as for instance in work by Charlotte Vlek on explaining Bayesian Networks (Vlek et al. 2016), which had nice connections to the work discussed by Jeroen Keppens yesterday (2019).

# 6 Conclusion 

As I said I think the way to go for the field is to develop an AI that is much like the law, an AI where systems are hybrid critical discussion systems.

For after phases of AI as mathematics, as technology, as psychology, and as sociology—all still important and relevant—, an AI as Law perspective provides fresh ideas for designing an AI that is good (Table 1). And in order to build the hybrid critical discussion systems that I think are needed, lots of work is waiting in reasoning, in knowledge, in learning and in language, as follows.

For reasoning (Sect. 5.1), the study of formal and computational argumentation remains relevant and promising, while work is needed to arrive at a formal semantics that is not only accessible for a small group of experts.

For knowledge (Sect. 5.2), we need to continue working on knowledge bases large and small, and on systems with embedded norms. But I hope that some of us are also brave enough to be looking for new ways to arrive at good commonsense knowledge for machines. In the law we cannot do without wise commonsense.

For learning (Sect. 5.3), the integration of knowledge and data can be addressed by how in the law rules and cases are connected and influence one another. Only then the requirements of explainability and responsibility can be properly addressed.

For language (Sect. 5.4), work is needed in interpretation of what is said in a text. This requires an understanding in terms of complex, detailed models of a

[^0]
[^0]:    ${ }^{30}$ kialo.com.
    31 'IBM's AI loses debate to a human, but it's got worlds to conquer', cnet.com, February 11, 2019.

situation, like what happens in any court of law where every word can make a relevant difference.

Lots of work to do. Lots of high mountains to conquer.
The perspective of AI as Law discussed here today can be regarded as an attempt to broaden what I said in the lecture on 'Arguments for good AI' where the focus is mostly on computational argumentation (Verheij 2018). There I explain that we need a good AI that can give good answers to our questions, give good reasons for them, and make good choices. I projected that in 2025 we will have arrived at a new kind of AI systems bridging knowledge and data, namely argumentation systems (Fig. 7). Clearly and as I tried to explain today, there is still plenty of work to be done. I expect that a key role will be played by work in our field on connections between rules, cases and arguments, as in the set of cases formalizing tort law (Fig. 13, left) that formally validate the legally relevant rule-based arguments (Fig. 13, right).

By following the path of developing AI as Law we can guard against technology that is bad for us, and that-unlike the guillotine I started with-is a really humane technology that directly benefits society and its citizens.

In conclusion, in these days of dreams and fears of AI and algorithms, our beloved field of AI \& Law is more relevant than ever. We can be proud that AI \& Law has worked on the design of socially aware, explainable, responsible AI for decades already.

And since we in AI \& Law are used to address the hardest problems across the breadth of AI (reasoning, knowledge, learning, language)-since in fact we cannot avoid them-, our field can inspire new solutions. In particular, I discussed computational argumentation, schemes for arguments and scenarios, encoded norms, hybrid rule-case systems and computational interpretation.

We only need to look at what happens in the law. In the law, we see an artificial system that adds much value to our life. Let us take inspiration from the law, and let us work on building Artificial Intelligence that is not scary, but that genuinely contributes to a good quality of life in a just society. I am happy and proud to be a member of this brave and smart community and I thank you for your attention.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licen ses/by/4.0/.
