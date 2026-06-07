# The future of the London Buy-To-Let property market: Simulation with temporal Bayesian Networks 

Anthony C. Constantinou*, Norman Fenton

Risk and Information Management (RIM) Research Group, School of Electronic Engineering and Computer Science, Queen Mary University of London, London, United Kingdom

* anthony@constantinou.info

\section*{6

OPEN ACCESS

Citation: Constantinou AC, Fenton N (2017) The future of the London Buy-To-Let property market: Simulation with temporal Bayesian Networks. PLoS ONE 12(6): e0179297. https://doi.org/10.1371/ journal.pone. 0179297 <br> Editor: Yilun Shang, Tongji University, CHINA <br> Received: March 1, 2017 <br> Accepted: May 26, 2017 <br> Published: June 27, 2017}

Copyright: © 2017 Constantinou, Fenton. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: All relevant data are incorporated in the paper.

Funding: We acknowledge the financial support by the European Research Council (ERC) for funding this research project, ERC-2013-AdG339182BAYES_KNOWLEDGE, and Agena Ltd for software support.

Competing interests: The authors have declared that no competing interests exist.

## Abstract

In 2015 the British government announced a number of major tax reforms for individual landlords. To give landlords time to adjust, some of these tax measures are being introduced gradually from April 2017, with full effect in tax year 2020/21. The changes in taxation have received much media attention since there has been widespread belief that the new measures were sufficiently skewed against landlords that they could signal the end of the Buy-To-Let (BTL) investment era in the UK. This paper assesses the prospective performance of BTL investments in London from the investor's perspective, and examines the impact of incoming tax reforms using a novel Temporal Bayesian Network model. The model captures uncertainties of interest by simulating the impact of changing circumstances and the interventions available to an investor at various time-steps of a BTL investment portfolio. The simulation results suggest that the new tax reforms are likely to have a detrimental effect on net profits from rental income, and this hits risk-seeking investors who favour leverage much harder than risk-averse investors who do not seek to expand their property portfolio. The impact on net profits also poses substantial risks for lossmaking returns excluding capital gains, especially in the case of rising interest rates. While this makes it less desirable or even non-viable for some to continue being a landlord, based on the current status of all factors taken into consideration for simulation, investment prospects are still likely to remain good within a reasonable range of interest rate and capital growth rate variations. The results also suggest that the recent trend of property prices in London increasing faster than rents will not continue for much longer; either capital growth rates will have to decrease, rental growth rates will have to increase, or we shall observe a combination of the two events.


## Introduction

In 1998 the Assured shorthold tenancy-a form of assured tenancy with limited security-was introduced in Britain. This type of tenancy constituted a major shift in favourability towards landlords, leading to an explosion of interest in Buy-To-Let (BTL) property investments in the

UK from both amateur and savvy investors, at both national and international level. Even amateur investors have been able to develop enormous portfolios. The case of the Wilsons' is instructive [1]; this couple of ex-maths teachers had started buying homes to let in the late 1980s. In 2015, they were reported to be Britain's biggest BTL couple, at which point they started selling off their property empire, which consisted of approximately 1,000 properties, with a target to make $£ 100 \mathrm{~m}$ profit.

Success stories like these demonstrate the maximum (observed) potential of a BTL investment. Such vast profits can be made with increased amounts of borrowed capital, known as leverage, under the expectation that profits made will be greater than the interest paid on the additional borrowed capital. The high levels of lending to landlords was the basis for the Bank of England to express concerns on numerous occasions about the UK's property market. The problem with excessive amounts of leveraging is that, in the event of a crisis, many investors with excessive amounts of borrowing may be forced to sell at the same time, and this poses a threat to the UK's financial stability. This is, at least, part of the reason why the UK government has announced significant tax reforms specifically to target BTL investors.

There have been arguments in the media that, as an indirect effect of these measures, investors themselves may seek to offset part of their prospective losses by increasing rents, potentially affecting the lives of Londoners who already struggle to find affordable accommodation. However, these tax measures solely focus on BTL investors and hence, it is vital that we first understand the resulting direct effects on investors prior to assessing how the tax changes may indirectly influence the aggregate market. As a result, this paper introduces a novel temporal Bayesian Network (BN) simulator to assess the prospective impact of the various tax changes from the perspective of BTL investors, by taking into account a range of factors and uncertainties.

The paper is structured as follows: The new tax measures are described in detail in Section 2. Section 3 describes the factors being simulated. We provide a brief overview of BNs in Section 4 before describing the temporal BN model employed for simulation in Section 5. The simulation results are presented in Section 6 and discussed in Section 7. Finally, we provide our concluding remarks in Section 8.

# New tax measures for landlords 

This section summarises the changes in taxation for landlords. The new measures involve three key points: a) interest related tax relief, b) stamp duty land tax, and c) wear and tear allowance.

## Interest related tax relief

Under the existing system, all property expenses can be deducted from income when computing tax to be paid. Currently, such expenses receive tax relief at the landlord's highest income tax rate (e.g. $40 \%$ when in the Higher rate tax band; refer to Table 1). Under the new system,

Table 1. Current income tax rates and bands in the UK [3].


https://doi.org/10.1371/journal.pone.0179297.t001

Table 2. Illustration of the new measures through the adjustment period, based on a hypothetical example.


https://doi.org/10.1371/journal.pone.0179297.t002 interest payments will be treated differently to other expenses. Specifically, they will be capped for tax relief at the Basic rate of 20\% [2].

Since this new measure is restricted to the Basic rate income tax band, it gives the impression that those whose income does not surpass the Basic rate income tax band will remain unaffected. However, since interest is not offset against income, everyone's gross profits increase under the new system and hence, this will inevitably push a number of Basic rate tax payers into the Higher rate band that will require them to pay more tax. The new measures seem to move towards taxing turnover rather than actual profits. Note that this measure does not apply to limited companies as they are subject to corporate tax.

To give landlords time to adjust, the government is introducing this change gradually from April 2017, and over four years, with the new measures fully implemented in tax year 2020/21. Table 2 shows how the new measures will affect net profit over this adjustment period, based on a hypothetical example.

# Stamp duty land tax

The Stamp Duty Land Tax (SDLT) is a tax on land transactions in the UK, excluding Scotland where the Land and Buildings Transaction Tax was introduced in April 1, 2015, to replace SDLT [4]. In 2015 the UK government announced higher rates of SDLT on purchases of additional residential properties [5], effective from April 2016.

On the whole, the changes in SDLT increase the tax rate on additional residential properties by $3 \%$, in absolute terms, in each band (refer to Table 3). The overall relative effect, however, is significant. For example, if we had bought an additional property for $£ 300,000$, prior to April 2016, the SDLT would have been $£ 5,000$, whereas today this tax figure is $£ 14,000$. Note that transactions under $£ 40,000$ are not subject to the higher rates. Table 4 illustrates how the additional tax is accumulated based on this example.

Table 3. SDLT changes in the UK for additional residential properties, effective from April 2016 [5].


https://doi.org/10.1371/journal.pone.0179297.t003

Table 4. The increase in the SDLT tax bill with the new measures, based on buying a property at $£ 300,000$.


https://doi.org/10.1371/journal.pone.0179297.t004
Note that the above changes in SDLT are in addition to those effective from December 2014, where the UK government wanted to make tax payments fairer by cutting tax for $98 \%$ of the people buying a home for less than $£ 937,500$, and increasing tax for the $2 \%$ of people who buy a property above that threshold [6]. The SDLT changes of 2014 applied to all residential properties.

# Wear and tear allowance 

For furnished residential properties, the wear and tear allowance allowed landlords to deduct $10 \%$ of the gross rental income from gross profits. This allowance was supposed to represent the average costs of buying or replacing furniture or other capital items in the let property. The new measures, effective from April 1 2016, replaced this allowance with a relief that requires landlords to deduct the costs they actually incur on replacing (not servicing) furnishings, appliances and kitchenware in the property [7].

While this new measure may not appear to be as important as those described in Sections 2.1 and 2.2, it is expected to have a noticeable impact for two reasons. First, it further increases tax bills on the basis that the previous $10 \%$ was largely considered generous (hence the change). Second, this new measure requires additional effort from landlords to keep track of costs and receipts, which becomes tedious for those who own multiple properties.

## Factors being simulated

Before we describe the model and discuss the results from simulation, we first give a brief introduction to the key factors being simulated.

## Capital growth

Official price-paid data, for residential properties in London, is available online with open access by Land Registry [8]. However, these data are limited to 1995 onwards. Older pricepaid data is retrieved by Nationwide, who are the largest building society in the UK as well as in the world [9].

Fig 1 illustrates the annual capital growth generated by Nationwide data for years 1974 to June 2016, and Land Registry data for years 1996 to July 2016. The variation in capital growth between the two dataset is the result of Nationwide data capturing only part of the property sales in London, whereas Land Registry captures all of them. Land Registry data indicates that the average London property has experienced an average annual capital growth of $8.13 \%$ from 1995 to July 2016. On the other hand, Nationwide indicates that the growth for this same period has been $9.24 \%$ (though up to June, instead of July, 2016), and $8.7 \%$ from 1973 (4th quarter) to June 2016.

Fig 1 also captures the three major property market crises. The first was in the early 1980s when a severe global economic recession affected much of the develop world. The second occurred in 1992, also known as Black Wednesday [10], when the British government raised

![img-0.jpeg](img-0.jpeg)

Fig 1. Annual capital growth for residential properties in London.
https://doi.org/10.1371/journal.pone.0179297.g001
interest rates to unstable levels in an effort to control the rate of GBP to meet the limits introduced by the European Exchange Rate Mechanism (ERM). Eventually, the government was unable to keep the GBP above its agreed lower limit and was forced to withdraw from the ERM, which resulted in a fall in interest rates (refer to Section 3.3) and an end to the falling house prices (refer to Fig 1).

The third housing crisis came as a result of the 2007-09 Global financial crisis. The cause of this crisis was the burst of the USA housing 'bubble' due to a high default rate in the subprime home mortgage sector, as a result of many high-risk loans sold on as low-risk securities [11]. The crisis threatened the collapse of large financial institutions, with Lehman Brothers, the fourth largest investment bank in the USA, declaring bankruptcy in 2008. The crisis had an immediate negative effect on the London property market, though considerably lesser than the Black Wednesday crisis, as shown in Fig 1.

# Rental yield and rental growth 

Private rental market statistics for London are available from the Valuation Office Agency [12], though the data used to generate these statistics is stated to be based on a sample of rental information. Their statistics indicate that the average rent in London was $£ 1,727$ between 1 April 2015 and 31 March 2016, based on a sample size of 62,810 . Linking this to the Land Registry [8] data generates an average rental yield of approximately $3.7 \%$.

We have also examined additional rental information which is publicly available by LendInvest [13], who are the world's largest peer-to-peer platform for property. LendInvest statistics show that the rental yields in London spread between $4.5 \%$ and $7.4 \%$. However, these yields are based on rental prices extracted from Zoopla for the period January 12015 to February 18 2016, and are calculated relative to Land Registry 2010 price-paid data. These statistics are overrated for two reasons: a) rental prices are compared to property values dated five to six years back, and b) rental prices on Zoopla represent market advertised rents and not real rents from tenancy agreements.

Portico estate agency's interactive rental yield map indicates that rental yields in London spread between $2.2 \%$ and $5.5 \%$ [14], which are in agreement with the statistics retrieved by the Valuation Office Agency. Portico statistics show that in 2012 half of London was generating rental yields in excess of $6 \%$, whereas since 2015 all London districts are generating rental yields below $6 \%$. This implies that property price growth in London has been increasing faster than rents, at least over the last few years, hence pushing rental yields down. Portico state their

statistics are updated daily based on several hundred estate agents in London, and reflect the three most recent months.

In the case of rental growth, we found official local authority rental data from the Department for Communities and Local Government [15]. We were unable to find relevant private rental income data. Fig 2 illustrates the annual rental income growth since 1998, which averages at $4.69 \%$. Interestingly, local authority rents have been growing approximately half as fast as property prices, which inevitably decreases rental yields over each subsequent year, and which is in agreement with Portico's [14] results. While local authority rents differ from private rents, we expect the two to correlate well.

However, it is reasonable to assume that the growth in the private sector has been slightly higher than the growth in the local authority sector; though still notably inferior to respective capital growth, in order to be in line with the results from Portico and the Valuation Office Agency. Since annual growth from local authority rents has been $4.69 \%$, and annual capital growth has been $8.23 \%$ for the same period, it is likely that annual rental growth in the private sector is somewhere closer to $5.5 \%$.

# Mortgages and interest rates 

The interest rates offered by the various mortgage lenders in the UK are heavily influenced by the Bank of England Base Rate, which is typically used as a reference point. Data from the Bank of England [16] shows that interest rates in the UK have been at record low levels over the last few years (although this has become an international phenomenon following the financial crisis of 2007-09). Fig 3 illustrates the monthly Bank of England Base Rates records from 1975 to August 2016.

The interest rate of a mortgage is further influenced by many other factors. The most important of these currently are:

1. Loan-To-Value (LTV) ratio, which represents the percentage of borrowing relative to the value of the property. The higher the LTV ratio the higher the interest rate. Nowadays, LTV ratios for BTL mortgages are restricted to $75 \%$.
2. Arrangement fees, which are fees you may pay the lender to set up the mortgage. These fees (currently) typically fall into three categories: 1) no fees with a relatively high interest rate, 2) fees ranging from $£ 1,000$ to $£ 2,000$ with a relatively low interest rate, and 3 ) fees as a percentage of the amount borrowed with a relatively low interest rate.
3. Mortgage type, with the most common types (both interest-only and repayment) currently being:
![img-1.jpeg](img-1.jpeg)

Fig 2. Annual rental income growth for local authority properties in London.
https://doi.org/10.1371/journal.pone.0179297.g002

![img-2.jpeg](img-2.jpeg)

Fig 3. Bank of England monthly base rate records, from 1975 to date.
https://doi.org/10.1371/journal.pone.0179297.g003
a. Standard Variable Rate (SVR): Normally offers the highest (variable) interest rates with zero to little fees and the flexibility to repay the mortgage at any time.
b. Trackers and Discounted Variable: Similar to the SVR, but offer more attractive (variable) interest rates for a fixed period of time in exchange for fees and limited overpayments, with penalties if the limit is breached (the limit is typically set to $10 \%$ of outstanding mortgage balance per 12 months). The difference between a tracker and a discounted variable mortgage is that the tracker tends to follow the Bank of England's base rate, whereas the discounted variable tends to follow the base rate set by the lender.
c. Fixed: Offer fixed low interest rates for a fixed period of time in exchange for fees and limited overpayments similar to (ii) above.

Note that once the agreement of a non-SVR mortgage comes to an end, which can last anywhere between 2 to 10 years (shorter durations offer lower interest rates), they revert back to the SVR. Mortgages at SVR tend to be the most expensive. A savvy property investor will typically remortgage, also known as refinancing (refer to Section 3.4), when such an agreement comes to an end.

Table 5 provides some of the most attractive mortgage deals discovered by MoneySuperMarket [17]. Note that the best mortgage is not always the one with the lowest interest rate; i.e. it depends on borrowing, fees and other factors. Further, a borrower cannot always choose the most attractive mortgage deal since each mortgage exhibits different financial and propertyrelated requirements, and the most attractive mortgages tend to have more and stricter such requirements. Table 5 is, therefore, provided only for guidance for simulation.

For simulation we assume that investors tend to prefer the short-term deals which are restricted to 2-year agreements. This is because they allow investors to remortgage more frequently without penalty (i.e. every two years), and they cost less to borrowers who seek larger borrowings, which tends to be the case for BTL investors in London. Specifically, the higher the loan, the more attractive the fee to obtain a low interest rate becomes, relative to interest savings.

# Remortgage 

A remortgage is the process of paying off an active mortgage through the arrangement of a new mortgage, using the same property as security. There are many reasons someone would want to remortgage. For the purpose of this paper, these include:

Table 5. Some of the most attractive BTL mortgage deals (which include the option for interest only) discovered by MoneySuperMarket [17] on September 12, 2016, ranked by interest rate for different initial periods. Note that MoneySuperMarket has access to most, but not the whole, of the BTL mortgage market, and some BTL mortgage deals are only available through financial advisors. The Fees figure includes fees related to arrangement, admin, booking, completion, and survey. When a fee is stated as a percentage, it is calculated with reference to the amount being borrowed.


https://doi.org/10.1371/journal.pone.0179297.t005

1. Releasing equity: After the initial mortgage agreement ends, the property may have increased in value. This gives the option to the investor to release equity, also known as equity withdrawal, to reinvest it in another property. This process can be seen as an aggressive form of leveraging. For example, consider a property bought in 2010 for $£ 300,000$ with $75 \%$ LTV; implying a deposit of $£ 75,000$. Based on an average annual capital growth of $8.5 \%$ (refer to Fig 1), the property in 2016, or after six years, is expected to be worth $£ 489,440$. Assuming an interestonly mortgage, we still owe $£ 225,000$. However, since the property is now worth much more, the revised equity is $£ 433,742-225,000=£ 264,440$, which decreases the LTV rate to $45.97 \%$. If the investor choses to increase LTV back to $75 \%$, this would require borrowing $£ 367,080$, up from $£ 225,000$, hence releasing equity of $£ 142,080$ to reinvest in another property.
2. Reducing LTV: Similar to (a) above, a risk averse investor may choose to remortgage for the purpose of obtaining a lower interest rate, rather than leveraging, through the decreased LTV rate (refer to Table 5).
3. Reducing interest rate: Even if the property prices remain stable, an investor may still choose to remortgage to reduce the interest rate, either because the mortgage has moved to the higher SVR interest rate (refer to Section 3.3), or simply because another lender is offering a better deal.

Remortgaging still comes at a cost, however. For example, in the case of switching lenders additional mortgage fees may apply, such as mortgage broker's and even solicitor's fees.

# Letting agency costs

A letting agent provides lettings and full management of a BTL property, and is a popular option for investors who either have multiple properties, other full-time jobs, or who simply

do not want to spend time on managing a property. In London, letting agency fees are typically more expensive than other parts of the UK. Foxtons [18] and Savills [19], who thrive in London, charge $13.2 \%$ and $15 \%$ (including VAT) relative to rental income for lettings, which involves finding tenants and arranging collection of payments, or $20.4 \%$ for full day-to-day management of the property, which extends to arranging repairs and maintenance. These fees may decrease considerably when a tenancy agreement is repeatedly renewed, as opposed to the agency having to find a new tenant. In addition to these percentage figures, there are other fees, outside of maintenance, which have potential to add up to, or above, $£ 1,000$ per annum $[18,19]$.

Cheaper options include smaller letting agencies which may charge a flat fee of $12 \%$ (or $10 \%$ plus VAT) of rental income, without any hidden additional fees. However, these agencies are scarce, at least throughout inner London and relative to the more popular agencies who aim to cover every major London district. Alternatively, a landlord may choose to let and manage the property without using a lettings agent. This option promises much lower costs-typically restricted to perhaps a few hundred pounds for online advertising, and some other minor expenses.

# Overview of Bayesian networks 

A BN is a well-established graphical formalism that encodes the conditional probabilistic relationships amongst uncertain variables of interest. A BN model consists of nodes, which represent variables, and arcs between nodes, which represent the direction of influence [20]. Underpinning BNs is Bayesian probability inference. The term Bayesian comes from the Bayes' theorem:

$$
P(A \mid B)=\frac{P(B \mid A) P(A)}{P(B)}
$$

which describes how to revise the prior probability of an event $A$ occurring to its posterior probability conditional on new information $B$. For example, event $A$ may represent a disease and factor $B$ may represent a symptom. In this example, the prior probability of $A$ represents the probability of having disease $A$ without knowledge about symptom $B$, whereas the posterior probability of $A$ represents the probability of having disease $A$ given that we know whether symptom $B$ is or is not present.

The structure of a BN model and resulting conditional probability tables (CTPs) can be learnt from either data or knowledge, or a combination of the two. In domains such as bioinformatics and cancer research, where the ability of experts to observe interactions between cells is limited in various ways, applying structure learning algorithms to large datasets can reveal new insights that would otherwise remain unknown. On the other hand, these structure learning algorithms become less desirable in areas where domain experts have good knowledge about the underlying causal mechanisms of the problem. Knowledge-based BN structures are popular in such cases because even the 'best' algorithms often make mistakes, such as 'discovering' that symptoms influence age. BNs are also widely recognised as the most appropriate method to model uncertainty in situations where data are limited but where human domain experts have a good understanding of the underlying causal mechanisms and/or real world facts. However, incorporating such expert knowledge into a BN model is not straightforward and hence, various methods have been proposed for this purpose [21-28].

The model presented in this paper (Section 5) has had its structure solely determined by knowledge. This is because the process of BTL is based on clearly defined rules and regulating protocols. For example, we already know that a mortgage payment is determined by the

![img-3.jpeg](img-3.jpeg)

Fig 4. A simple 3-node BN, with the CPT of node rental income growth and summary statistics superimposed in the graph.
https://doi.org/10.1371/journal.pone.0179297.g004
interest rate in conjunction with the amount borrowed, and that tax payments are determined based on specific thresholds associated with different amounts of income. There is no need to collect relevant data about these factors and apply structure learning methods in an effort to 'discover' these relationships.

Fig 4 presents a simple 3-node BN, which consists of both discrete and continuous variables. BN models which incorporate both discrete and continuous variables are often referred to as hybrid BNs. This example demonstrates how we incorporate and quantify uncertainty in the BTL process. It shows how the subjective indication of $5.5 \%$ about the growth rate of the rental income is assessed in conjunction with deterministic degrees of confidence (in this case Medium which generates $\pm 2 \%$ at $95 \%$ CI). The CPT and summary statistics of the Rental income growth distribution are superimposed in the graph. We have made use of the AgenaRisk BN software [29] which allows simulation of continuous distributions using Dynamic Discretisation [30]. The same parameter learning process applies to a number of other hypothetical inputs. We cover these in detail in Section 5.

When it comes to time-series analysis with BNs, there are two main approaches [31]. The first approach is widely known as a dynamic BN (DBN), which represents a single model that captures all of the properties of the system dynamics and which is capable of producing distributions that relate to different trajectories. DNBs are also generalisations of hidden Markov models [32]. The second approach, which is not as compact as the first one, enables us to relate variables to each other over adjacent time steps without being restricted to a single model that captures all of the properties of the system. For example, a temporal BN (TBN) allows for non-

identical networks to exist at each time step. Note that Gated BNs (GBNs) are similar to TBNs in the sense that they represent processes which include several distinct phases, but GBNs tend to distinguish between sub-networks that are activated or disabled under specific scenarios. Application areas concerned with aspects of time-series analysis with BNs include the application of DBNs to agricultural developments [33], forensic psychiatry [34], medicine [35, 36], and bioinformatics [37]; the application of GBNs to algorithmic trading and stock market movements [38], and the application of TBNs to predicting long-term football team performance [39]. It should be noted that, while we focus on the probabilistic prediction approach for TBNs in this paper, recent theoretical work uses similar ideas to explore the structure and behaviour of complex systems. For example, [40] introduced forest likelihood to assess the complexity of such sparse networks, where the likelihood of the appearance of each forest can be analytically calculated within the framework.

In general, BNs have become increasingly popular in various real-world areas which requires improved decision making processes, including medicine [41--43], project management [33, 44], forensics and legal reasoning [45--48], finance and marketing [49], sports [50], and software engineering [51, 52]. In the property market domain, studies tend to focus on house sale trends using Bayesian estimation and/or averaging. Some of these studies include analyses of: the housing market dynamics by the European Central Bank [53]; the Colombian house price data [54]; what drives Ireland's housing market [55]; the residential property valuation in Hong Kong [56]; downturns [57] and repeat sales indices [58] in US housing market; house sales price in Toronto [59]; the factors which capitalise into house prices in Zurich [60]. In contrast to these past relevant publications, we focus on the property market from the investor's perspective. We examine the impact the new tax measures have on the profitability of the typical BTL property in London, and assess the relevant risks and potential profits of a BTL investment under the pending tax reforms. We have developed a bespoke TBN for this purpose.

# The model 

The topology of the overall TBN is presented in Fig 5. A full description for each of the nodes and respective CPTs is provided in Table 6. The shaded nodes in Fig 5 represent background nodes. A background node is simply a variable that has no ancestors and, for the purposes of this simulation study, represents required input such as property value, interest rate, borrowing, and so on. Note that, while nodes $n p-1$ and $c g n-1$ in Fig 5 have no ancestors, they only exist in time periods $t 2$ to $t 10$ and hence are not background nodes since they are dependent on $t 1$. Fig 5 also distinguishes the following types of nodes:

1. The nodes which are restricted to specific time periods. The model assumes that a single time period represents a single year and hence, $t 5$ represents year five and $t+1$ implies one year after period $t$. Restricting the representation of a single time period $t$ to a whole year, rather than days or months, not only allowed us to maintain the complexity of the model at minimum levels, but also to build a reasonably accurate knowledge-based system of the BTL process which is driven by annual regulations and figures.
2. The input (I) and output (O) nodes. A BN model exists for each time period $t$, and the input and output nodes are the nodes which connect those BN models within the temporal space. Specifically, an input node at time $t$ takes as input (i.e. prior distribution) the respective output (i.e. posterior distribution) associated with this node at time $t-1$. Note that, since $t 1$ represents the starting time interval, input nodes at $t 1$ serve as the background nodes, as discussed above, which require hypothetical observations entered for simulation purposes

![img-4.jpeg](img-4.jpeg)

Fig 5. Topology of the TBN model, where a shaded node is an observable variable, a white node is a latent variable, $I$ is input node, $O$ is output node, and $I O$ is both an input and an output node.
https://doi.org/10.1371/journal.pone.0179297.g005
(refer to Section 5.1). For example, the input node Property value ( $p v$ ) at time $t$ takes as input the output of node $p v$ at $t-1$.

The TBN model incorporates a number of subjective nodes which allow the model to capture the investor's uncertainty relating to the inflation in property expenses, rental income growth, rental income loss from void periods, and capital growth. For each of these cases, we have introduced an Assessed node, which takes as input the investor's belief about the given rate, and a Confidence node, which takes as input the investor's degree of confidence with respect to the input rate, as previously illustrated in the example BN model of Fig 4. Further, Table 6 shows that the available states of a Confidence node are Low, Medium, High, or Certain, and each state generates distributions with the respective deterministic variabilities of $\pm 5 \%$, $\pm 2 \% \pm 1 \%$ and $\pm 0 \%$, at $95 \%$ confidence interval (CI). These observable nodes exists only at $t 1$, as discussed above and also shown in Fig 5.

It is important to note that the BN model described in this paper is developed for simulation purposes based on different hypothetical BTL investment scenarios. These scenarios are based on different hypothetical observations related to various factors of interest such as interest rate, capital and rental growth, along with other relevant factors (refer to Section 6). The purpose of the simulation is to demonstrate how hypothetical changes in these factors may influence a BTL investment, and not to predict how these factors may change in the future. For example, while it is reasonable to assume that capital and rental growth are positively

Table 6. Description of each of the TBN model nodes as defined in the topology of Fig 5.


(Continued)

Table 6. (Continued)


https://doi.org/10.1371/journal.pone.0179297.t006
correlated, there is no need to incorporate such an assumption into this model since we do not seek to predict these outcomes, but we rather assign hypothetical observations to them.

Finally, throughout an investment period an investor may want to intervene on a BTL investment for various reasons, such as to revise borrowing, renew interest rate deals, etc. The causal interpretation underpinning BNs makes these models particularly suitable in informing how outcomes would change as a result of an intervention. Most previous work on BN interventions focus on interventions performed on a particular state of a node that is made independent of all its ancestors. This process is known as graph surgery [20] and represents the standard process for interventional analysis in BNs. In our case, we are interested in intervening on a particular state of a node at a particular time period; hence, making an event at $t$ independent of $t-1$. As a result, we perform graph surgery between time steps, or between BN models within the temporal space, rather than between nodes in a single BN model.

# Simulation and results 

In order to examine the influence of various relevant factors on a BTL investment, we determine a BTL profile. This profile, which we refer to as the Typical BTL London Profile (TBLP), is intended to represent a common profile for BTL property investments in London. The profile serves as the basis for assessment of each of the factors of interest and their impact on the profitability of the investment profile. The description of the TBLP is provided in Section 6.1. Subsequent subsections demonstrate the results from simulation for each of the assessed factors.

## The Typical BTL London Profile (TBLP)

The TBLP is determined by the status of the property market in 2016. The observable input values considered for this profile are provided in Table 7. These inputs are primarily based on what has been discussed in Section 3, as well as on some additional assumptions. The TBLP is determined from the following assumptions or facts:

1. According to Land Registry [8], the average property sale in London in 2016 (up to August) was $£ 635,582$, and the median $£ 430,000$. We consider the purchase of a property at $£ 500,000$.
2. The typical BTL investor seeks to purchase a property with maximum borrowing, or minimum deposit. As a result, we consider that the LTV is set to the current market available maximum of $75 \%$ (i.e. $£ 375,000$ borrowing). Note that, as of May 2017, new regulations on

Table 7. The Typical BTL London Profile (TBLP) considered for simulation.


https://doi.org/10.1371/journal.pone.0179297.t007
rental stress tests have made deposits at $25 \%$ largely insufficient, although occasionally lenders may consider other affordability figures in determining the maximum LTV (see Section 6.2 for more details).
3. We consider an interest rate of $2.2 \%$ at $75 \%$ LTV, and an interest rate of $1.7 \%$ at $60 \%$ LTV or lower, plus an average of $£ 1,000$ fees per annum (e.g. arrangement and valuation fees averaged per annum). These inputs are based on what has been discussed in Sections 3.3 and 3.4, and using Table 5 as guidance. Note that while most lenders allow arrangement fees to be added to the loan, rather than pay them upfront, they still represent a fee and which we consider as an upfront cost when calculating net profit from rental income.
4. We consider a rental yield of $4 \%$ (i.e. $£ 20,000$ ) based on the statistics retrieved by [12], and an annual rental income growth of $5.5 \%$ (with Medium confidence), based on what has been discussed in Section 3.2. We also assume that the loss in rental income from void periods in London averages to two weeks per annum (i.e. $3.85 \%$ loss from rental income), with Medium confidence.
5. We assume that the BTL investment is fully managed by a lettings agency. Further to what has been discussed in Section 3.5, while the bigger letting agencies in Inner London charge $20.4 \%$ (including VAT) of rental income, numerous other smaller agencies, particularly those based in Outer London, charge 12\%. We have not found accurate statistics on this matter, hence we consider the management fees to be $16 \%$ (including VAT), which represents the approximate middle point of the range available in the market.
6. The Other property expenses figure is highly volatile since it may include service charges, ground rent, maintenance costs, solicitor's fees from remortgages, plus any other additional fees a lettings agent may charge and which fall outside of the fixed percentage charge. We assume this figure to be $£ 2,500$ per annum, $20 \%$ of which (or $£ 500$ ) falls under the 'servicing' category and which cannot be used for tax allowance purposes (refer to Section 2.3). We also assume that these expenses grow by $5 \%$ per annum (i.e. faster than typical inflation which we cover later in Section 7.2), with Low confidence.
7. We consider a 10-year average annual capital growth of $8.5 \%$, with Low confidence, based on what has been discussed in Section 3.1.

Table 8. Results (expected values where applicable) from simulation based on the TBLP of Table 7. Monetary values represent EGBPs in thousands (k). The Real rental income/yield figures represent the rental income/yield after accounting for potential rental income loss due to void periods.


https://doi.org/10.1371/journal.pone.0179297.t008 8. We assume the landlord falls within the High rate income tax band of $40 \%$ (see Table 1).

Table 8 illustrates the results from simulation based on the inputs presented in Table 7, and under the assumption that the interest-only mortgage is based on 2-year fixed-rate agreement, which is renewed every two years without releasing equity. At this stage, the results reported are restricted to the expected values of the distributions. Further, since almost all mortgage lenders in the UK allow for annual overpayments up to $10 \%$ of residual mortgage balance, if we were to reinvest net profits from rental income generated at the end of each time period as mortgage overpayments, this would have increased the total net returns by $£ 1.5 \mathrm{k}$ due to the reduced interest payments. Because of the minor impact and for simplicity, we shall assume that the typical investor saves net profits for cash flow.

# Impact of rental yield

Table 9 illustrates the impact rental yield has on net profits. The results show that a change of a single percentage point in rental yield has an impact of $\pm £ 31.2 \mathrm{k}$ on cumulative net profits, over the 10 years. At $2.8 \%$ rental yield, and with confidence set to $\pm 2 \%$ at $95 \%$ CI, the TBLP has a

Table 9. The impact of rental yield on 10-year cumulative net profits. Monetary values represent EGBPs in thousands (k). The highlighted row represents the point at which the investment has risk of becoming lossmaking.


https://doi.org/10.1371/journal.pone.0179297.t009

risk of loss $11.4 \%$ (excluding capital gains), and this risk increases to $100 \%$ when rental yield decreases further to $2.6 \%$.

However, the impact of rental yield extends to much more significant issues. This is because mortgage lenders use rental yield as the basis for assessing the amount they can lend. The proportion of rental income to mortgage interest payments is also known as debt service coverage ratio. Currently, lenders require that a BTL property generates gross rental income that is at least $125-165 \%$ of the mortgage payments (note that as of May 2017, rental stress-tests require a minimum of $140 \%$ ). However, instead of taking the actual mortgage payments into account, lenders stress-test this risk based on high-risk hypothetical interest rates, currently ranging between $5 \%$ and $6 \%$. In the case of borrowing $£ 375 \mathrm{k}$, a lender with $125 \%$ rental coverage requirements at $5 \%$ interest rate would want the property to generate a monthly rental income equivalent to $\frac{£ 375.000 \times 0.05}{12} \times 1.25=£ 1953.13$, which represents a rental yield of $4.69 \%$.

Tougher requirements of $145 \%$ rental yield at $5.5 \%$ interest rate increase rental yield requirements substantially, pushing the acceptable rental yields well above the current average observed in London. However, some lenders may relax some of the stress-test requirements for experienced BTL investors and occasionally, they may consider other forms of income to help borrowers meet affordability demands. Otherwise, the only option left to a borrower is to reduce LTV down to a particular threshold so that rental income passes the stress-test.

# Impact of letting agency fees 

In Section 3 we mentioned that some letting agencies will occasionally charge additional fees that fall out of the fixed percentage fee. The TBLP assumes these fees to be $£ 250$ per annum (this figure is incorporated into Other expenses (oe)), with the fixed percentage letting agency fee set to $16 \%$ inc VAT. In simulating the impact of letting agency fees, we manipulate both of these values. The results in Table 10 show that an investor who does not hire a letting agent is expected to increase net profits by $£ 34.5 \mathrm{k}$, over the 10 -year period, relative to an investor who hires one of the more expensive letting agents for full management of the property.

## Impact of interest rates

In Section 6.1 we explained how the TBLP considers the interest rates of $2.2 \%$ and $1.7 \%$, depending on LTV; i.e. interest rates decrease to $1.7 \%$ if LTV decreases to $60 \%$. Table 8 shows that the requirements for the lower interest rate are met at $t 3$. However, since the mortgage is

Table 10. The impact of letting agency fees on 10-year cumulative net profits. Monetary values represent EGBPs in thousands (k).


https://doi.org/10.1371/journal.pone.0179297.t010

Table 11. The impact of interest rates on 10-year cumulative net profits. Monetary values represent EGBPs in thousands (k). The highlighted row represents the point at which the investment has risk of becoming lossmaking.


https://doi.org/10.1371/journal.pone.0179297.t011 based on a 2-year fixed rate deal, the lower interest rate can be obtained at the end of $t 4$ when the $2^{\text {nd }}$ remortgaging stage occurs (assuming equity is not released). As a result, simulation assumes an interest rate of $2.2 \%$ for time periods $t 1$ to $t 4$, and an interest rate of $1.7 \%$ for time periods $t 5$ to $t 10$. The results in Table 11 show that a change of a single percentage point in interest rates has an impact of $\pm \in 30 \mathrm{k}$ on cumulative net profits. If interest rates were to rise by an absolute $1.2 \%$, the TBLP investment would have a risk of $1.3 \%$ for loss, and this risk becomes $100 \%$ if interest rates were to rise by $1.5 \%$.

## Impact of capital growth

Annual capital growth is one of the more volatile factors being simulated. While we consider the average annual capital growth, over a 10-year period, to be $8.5 \%$ (refer to Section 3.1), data from $[8,9]$ show that for any 10-year period since 1973, the minimum and maximum averaged capital growth rates in London range between $2 \%$ and $18 \%$ respectively. As shown in Table 12, at $2 \%$ average annual growth, and with confidence set to $\pm 5 \%$ at $95 \%$ CI, the TBLP has risk $0.7 \%$ for loss, and this risk increases to $100 \%$ when the capital growth decreases by $4 \%$ per annum.

Table 12 also indicates that a single percentage point difference in capital growth has highly volatile impact. For example, if we were to experience a decrease or increase of one percentage point on the annual average capital growth of $2 \%$, the expected impact would have been $-\epsilon 57 \mathrm{k}$ and $+\epsilon 61.6 \mathrm{k}$ respectively. However, when the annual capital growth averages at $18 \%$ per annum the respective impact is $-\epsilon 213.6 \mathrm{k}$ and $+\epsilon 229.1 \mathrm{k}$. The rule of thumb is that the value of the property doubles every 10 years if the annual capital growth averages roughly at $7.5 \%$.

## Impact of leverage

When property prices increase, an investor may choose to release equity to reinvest it in another property. This is a common investment direction for BTL investors who favour leveraging. However, any additional borrowing above the capital value of the property when it

Table 12. The impact of capital growth on 10-year cumulative capital gains. Monetary values represent EGBPs in thousands ( $k$ ). The highlighted row represents the point at which the investment has risk of becoming lossmaking.


https://doi.org/10.1371/journal.pone.0179297.t012 was brought into the letting business is not tax deductible (see itr in Table 6). Further, the process of leveraging entails greater uncertainties than those in preceding scenarios. To ensure the simulation is realistic, we restrict the value of equity that can be released at each remortgaging stage to roughly a level that ensures additional interest paid from increased borrowing does not result in negative net profit at $99 \%$ CI. In the case where the $99 \%$ mass of the distribution falls into negative net profit, for any time $t$, the LTV rate is decreased in steps of 5 percentage points until this condition is met. This restriction inflates the proportional minimum deposit required when buying additional properties through simulation, and this makes simulation more realistic and in line with the expected stricter affordability stress-tests.

Table 13 indicates the equity that can be released at each remortgaging stage, which we assume occurs every two years, as indicated in Section 6.1. Note that in order to satisfy the requirement on net profits, the LTV is restricted to $70 \%$ at the third and fourth remortgaging stages (i.e. $t 6$ and $t 8$ ), and to $65 \%$ at the fifth remortgaging stage (which may occur at the end of the 10-year period), down from current obtainable maximum of $75 \%$.

Fig 6 illustrates how the equity released at each remortgaging stage allows investors to fund further BTL properties throughout the 10-year period, which in turn may provide the option to release additional equity that can be used for the same purpose. For each additional property purchased, a number of key amendments are reported with respect to the TBLP. Note that each additional property is purchased at $60 \%$ LTV with the lower interest rate of $1.7 \%$, as a result of the restriction introduced on net profits.

The outcomes of Fig 6 are based on the following facts or assumptions:

Table 13. Equity that can be released at each remortgaging stage, with the restriction that additional borrowing does not lead to negative net profit at $95 \%$ CI for any time $t$. Monetary values represent EGBPs in thousands ( $k$ ).


https://doi.org/10.1371/journal.pone.0179297.t013

1. When calculating the available deposit to fund a new BTL investment, we factor in the costs from the new SDLT (refer to Section 2.2), plus a generous $£ 5 \mathrm{k}$ to cover other property purchase costs (e.g. land registry and solicitor fees).
2. Each additional property purchased is assumed to have rental yield that is $1 \%$ higher relative to the TBLP. This is because the additional properties purchased are much cheaper and hence, more likely to be studios and 1-bedroom flats which tend to generate higher rental yields. The simulation also accounts for the annual projected decrease of $0.1 \%$ in rental yields, to be in agreement with the results in Table 8. For example, Fig 6 shows that at $t 2$ Property No. 2 starts with rental yield $4.8 \%$ (i.e. $4 \%+1 \%-0.2 \%$ ), whereas at $t 4$ Property No. 3 starts with rental yield $4.6 \%$ (i.e. $4 \%+1 \%-0.4 \%$ ).
3. The Other expenses figure (refer to Section 6.1) is assumed to be $£ 500$ lower relative to the TBLP, since properties of lower value tend to entail lower such expenses. However,

![img-5.jpeg](img-5.jpeg)

Fig 6. The process of leveraging by increasing borrowing through gross capital gains, and using released equity to fund the purchase of additional properties. https://doi.org/10.1371/journal.pone.0179297.g006

![img-6.jpeg](img-6.jpeg)

Fig 7. Cumulative portfolio, gross capital gains and borrowing (left axis), and net profit (right axis), as a result of leveraging. Both left and right axis represent £GBPs in thousands (k).
https://doi.org/10.1371/journal.pone.0179297.g007
simulation also accounts for the $5 \%$ annual inflation rate (refer to Table 7), in the same way it does for the decreasing rental yield. For example, Fig 6 shows that at $t 2$ Property No. 2 has initial Other expenses set to $£ 2.21 \mathrm{k}$ (i.e. $\left.(£ 2.5 k-0.5 k) \times 1.05^{2}\right)$, whereas at $t 4$ Property No. 3 has $£ 2.43 \mathrm{k}$ (i.e. $\left.(£ 2.5 k-0.5 k) \times 1.05^{4}\right)$.

Fig 7 demonstrates the cumulative property portfolio, borrowing, gross capital gains, and net profit, as a result of leveraging, by taking all of the five prospective properties into consideration as illustrated in Fig 6. Note that leverage stops after $t 8$ without accounting for the equity that could have been released at the end of $t 10$ to buy a sixth property.

# Discussion of the results 

In Section 6 we demonstrated the impact various key factors have on the profitability of the TBLP. These results are discussed in Section 7.1. Profitability comparisons between the old and new tax reforms are provided and discussed in Section 7.2.

## Factors of interest and their impact on the TBLP

There are factors outside of the investor's control which can impact net profits. Profitability assessments of the TBLP suggest that a shift of $1 \%$ in interest rates has almost identical impact to a shift of $1 \%$ in rental yield; i.e. $\pm £ 30 \mathrm{k}$ and $\pm £ 31.2 \mathrm{k}$ respectively, over a 10 -year period. Since the overall profits from rental income average to just 38.7 k , the risk of loss becomes evident when interest rates increase or rental yields decrease by $1.2 \%$, whereas at $1.5 \%$ prospective net profits are eliminated since the risk of loss becomes $100 \%$. Naturally, the risk of loss may occur with a lower combined effect associated with these two factors, and this reveals a substantial risk of turning a BTL investment into a lossmaking one (without accounting for any capital gains). Moreover, given that it is reasonable to expect some BTL investments in London to already suffer from these lower rental yields [14] and higher interest rates (refer to Table 5), these BTL profiles are at a significant risk of becoming lossmaking once the new tax reforms come into full effect in tax year 2020/21.

On the other hand, the landlord has control over which managing agent firm to employ, and whether to employ one. Simulation shows that the difference between not employing and employing one of the more expensive letting agencies, for full property management over the

10-year period, has an impact of $\pm £ 34.5 \mathrm{k}$ on overall net profits (refer to Table 10). Interestingly, the maximum an investor can save from not employing a letting agency is roughly equivalent, as well as limited, to the $1 \%$ shifts in interest rate or rental yield. Another control factor is, naturally, the amount borrowed. In fact, reducing LTV provides potential for an investor to indirectly control the interest rate, on the basis that lower LTV rates have access to lower interest rates.

When it comes to capital growth, a shift of $1 \%$ can have a highly volatile impact due to its diminishing or cumulative effect on capital gains. For example, for any 10-year period since 1973, where the average capital growth rates hover between $2 \%$ and $18 \%$, a shift of $1 \%$ on average capital growth results in an impact on gross capital gains ranging anywhere from $-£ 57 \mathrm{k}$ to $+£ 229.1 \mathrm{k}$ (refer to Table 12).

# Profitability comparison between the old and the new tax reforms 

Table 14 provides detailed summary statistics of the return-on-investment (ROI), with and without leverage, with and without selling the portfolio at the end of the 10-year period, and based on both the old and the new tax reforms. Note that, in the case of selling the portfolio, we consider the following additional facts or assumptions:

1. Agent fees from selling the properties are set to $2 \%$ (these typically range between $1 \%$ and $3 \%$, including VAT).
2. Each property sale assumes a relatively high cost of $£ 5 \mathrm{k}$ to cover solicitor and other fees, but which remains constant over the simulation period.
3. The current annual tax allowance from capital gains is $£ 11.1 \mathrm{k}$ per individual [61]. This allowance tends to increase marginally per annum. We assume that by the end of the 10-year period the allowance will be $£ 15 \mathrm{k}$. We also assume that the property portfolio has two owners, typically husband and wife, which doubles the tax allowance to $£ 30 \mathrm{k}$ per annum. Note that in the case of leverage, we also assume the whole portfolio is sold within a single tax year (i.e. at the end of $t 10$ ) and hence, not benefiting from tax allowances available in other years.
4. Residential tax from capital gains is set to the current rate of $28 \%$ [62], which is in line with the Higher rate tax band considered by the TBLP (refer to Table 1).

The results show that the expected ROI under the new tax measures ranges from $290 \%$ to $591 \%$, depending on whether the investor chooses to leverage and/or sell the portfolio at the end of the 10 years. On the other hand, the expected ROI figures under the old tax measures range from $301 \%$ to $944 \%$. The results are distributed between not leveraging and leveraging, and not selling and selling the portfolio at the end of the period. Specifically, the impact on the TBLP is as follows:

1. In the case of not leveraging, the new tax reforms decrease ROI from $408 \%$ to $396 \%$ when the portfolio is maintained as an investment, or from $301 \%$ to $290 \%$ when the portfolio is sold and capital gains tax is paid. Overall, this represents a rather marginal impact which hovers between $3 \%$ and $4 \%$. However, this impact comes exclusively from reducing net profits from rental income, from 57.1 k to 38.7 k , and which represents a significant impact of $-32.2 \%$.
2. In the case of leveraging, the new tax reforms decrease ROI from $941 \%$ to $590 \%$ when the portfolio is maintained as an investment, and from $667 \%$ to $411 \%$ when the portfolio is sold

Table 14. Overall profit and ROI, based on both the old/current and new tax measures, with and without leverage, and with and without selling the property portfolio. Monetary values represent EGBPs in thousands (k). Note that In the case of leverage, the additional SDLT paid and the additional purchasing costs are already incorporated into Loan/s, since these costs are covered by borrowing.


(Continued)

Table 14. (Continued)


https://doi.org/10.1371/journal.pone.0179297.t014 and capital gains tax is paid. Overall, this represents a significant impact which hovers between $-37 \%$ and $-38 \%$. Similar to Fig 6, Fig 8 demonstrates the process of leveraging when the figures are based on the old/current tax measures, and demonstrates how the purchase of 8 properties is achieved, up from 5 properties when based on the new tax reforms of Fig 6.

However, given that the expected 10-year ROI under the new tax reforms ranges between $290 \%$ and $590 \%$ suggests that long-term investment prospects are likely to remain good if current economic circumstances continue. Table 14 also illustrates how ROI adjusts for different inflation rates. According to the Office for National Statistics in the UK [63], the inflation rate for any 10-year period since 1989, and up to and including 2015, hovers between $1.51 \%$ and $3.7 \%$. The long-term ROI from BTL investments is projected to be well above these rates.

While leverage is the clear winner when it comes to overall profitability, these profits come almost exclusively in the form of capital gains. As a result, leverage limits cash flow and increases the risk of lossmaking in terms of prospective profits from rental income, and this is a major risk for investors without cash reserves. Additionally, leverage requires substantial

![img-7.jpeg](img-7.jpeg)

Fig 8. The process of leveraging the TBLP scenario of Fig 6, when based on the old tax measures. https://doi.org/10.1371/journal.pone.0179297.g008

more effort by investors, since it involves buying additional properties, obtaining just as many mortgages, as well as dealing with additional demands which inevitably arise from additional tenancies. These are factors an investor needs to assess in order to determine whether the increased risk and effort is worth the projected increase in profitability, under different levels of leveraging.

# Concluding remarks 

In 2015 the British government announced a number of tax reforms for individual BTL investors. These new measures increase tax payments for BTL mortgaged investments considerably. To give landlords time to adjust, part of these measures are being introduced gradually from April 2017 with full effect in tax year 2020/21. The paper provides two novel contributions to the state-of-the-art: one is the simulation model itself and the other is the study of a research question which we have not seen before in a real estate context.

The novel TBN model provides the capability to an investor to simulate the impact of various factors and interventions of interest on a BTL investment, and over a 10-year period. The model captures uncertainties of interest and permits for intervention between time steps to allow for risk management of changing circumstances, such as changes in interest rates and rental and capital growths. The temporal Bayesian modelling technique appears to be well suited to address the research question. Unlike past relevant publications which tend to focus on analysing and predicting housing market trends, this paper assesses the prospective performance of BTL investments from the investor's perspective, and examines the impact of incoming tax reforms. The analysis focuses on the London BTL property market and assumes a typical BTL London profile, which we call TBLP, in assessing the impact of various factors of interest, in conjunction with tax reforms. The main conclusions from simulation are:

1. The new tax reforms are projected to have a significant impact on net profits from rental income. Overall, the new tax measures demonstrate high risk in terms of eliminating profits and transforming a BTL investment into a lossmaking investment (excluding capital gains). However, it is important to note that this outcome does not imply that future BTL investors are expected to generate such losses, simply because lenders are likely to take (and already are) a more conservative approach to their rental stress testing and affordability calculations to ensure that borrowers will be in position to meet mortgage payments (i.e. by requesting larger deposits to ensure that rental income will be sufficient to cover mortgage payments and other costs associated with the investment).
2. Property prices in London have been increasing faster than rents. If this trend continues, simulation suggests that rental yields in London will continue to decrease by $0.1 \%$ per annum. In fact, Portico [14] show that in 2012 half of London was generating rental yields in excess of $6 \%$, whereas since 2015 all London districts generate rental yields below 6\%. In reality, this trend cannot continue for much longer. Either capital growth rates will have to decrease, rental growth rates will have to increase, or we shall observe a combination of the two prospective events.
3. Historic low interest rates add substantial uncertainty to BTL investments. It is not clear whether we have entered an era of extremely low interest rates, or whether the Bank of England has plans to increase them. If interest rates rise by an absolute $1.5 \%$ under the new tax reforms, this poses a major risk of collapse of the mortgaged BTL market. However, interest rates are unlikely to increase by this much unless there is strong economic activity, which should in turn have a positive effect on the growth of both the rental income and

capital gains. Further, interest rates are controlled by the Bank of England, and it should be in their best interest not to cause chaos in the UK property market.
4. The significant impact on net profits from rental income poses considerable risk to investors with no cash reserves. This makes the prospect of investors intervening on controlled costs more likely, such as reducing costs related to managing agencies, or limiting leverage to achieve better interest rates through decreased LTV rates.
5. The new tax reforms hit risk-seeking BTL investors who favour leverage much harder than risk-averse investors who do not expand their property portfolio. If lenders introduce stricter criteria for borrowers in light of the tax reforms, the investors' ability to leverage will diminish further. The projected limitation on leveraging will also have a negative effect on demand for property. However, the level of impact on demand is unclear. We have no information with respect to what proportion of property demand is attributed to leveraging. Given that property demand in London is mainly driven by the growing population and the limited housing supply [64], it is unlikely these events will have major impact on overall demand for property.
6. Since the ROI from BTL investments is predominantly driven by capital growth, profitability prospects remain good under the new tax reforms, even when ROI is adjusted for high inflationary rates. In an era of negative prospects about economic stability, and in conjunction with the uncertainties surrounding Brexit in the UK, it may be difficult to foresee how these capital growth rates will be repeated. However, one could argue that such disbeliefs are never-ending and have been refuted multiple times in the past. Regardless, and further to what has been discussed in point (5) above, it is reasonable to expect the capital growth rates to decrease in the near future. Our analyses do not make it possible for us to comment on how capital growth rates are expected to change. However, what we do know is that If we base capital growth expectations on the worst 10-year period observed since 1973, which translates to an average of a $2 \%$ annual capital growth (refer to Section 6.5), and with all the other factors unchanged, the most adverse expected ROI figure over the 10-year period (i.e. without leveraging and after paying capital gains from selling the portfolio) is $69 \%$. Also, according to official Land Registry statistics, the annual capital growth in June 2016 (i.e. pre-Brexit referendum) was $13.82 \%$ for London and $8.01 \%$ for the UK, whereas in March 2017 the respective rates are down to $1.53 \%$ and $4.1 \%$, and continue to follow a decreasing trend. Part of this decrease can also be attributed to the SDLT changes (refer to Table 3), as well as to the incoming BTL tax reforms. The excessive capital growth observed post-2009 crisis can also be seen as a cause of the decreasing growth trend, simply because it is natural to observe a slowdown following excessive growth (and vice versa). The overall complexity of the situation makes it difficult to establish the real effects of the various political events and policy tax interventions on the housing market.

Our aim was to assess the impact of the new tax reforms, and in doing so we considered a common London property profile. London itself, however, consists of boroughs with major differences in terms of property value and demand. For example, the most extreme case between boroughs in 2016 (up to August), shows that property sales in the London borough of Kensington and Chelsea averaged $£ 1.91 \mathrm{~m}$, which is $678 \%$ higher than the average sale of $£ 282 \mathrm{k}$ in the borough of Barking and Dagenham. The results from simulation (refer to Section 6) allow readers to examine how various changes of the key profile inputs influence the BTL investment, and give an indication as to how profitability might change under different circumstances, events, and BTL profiles.

Overall, while the risk of making a loss from rental income is substantial under the new tax measures, and which makes it less desirable or even non-viable for some to continue being a landlord, investment prospects are likely to remain good within a reasonable range of interest rate and capital growth rate variations. Given that the results are based on a typical BTL profile in London, this implies typical rental yields, expenses, and growth rates. Such a profile, however, underestimates the ability of savvy investors in selecting a BTL property for investment purposes. This is because a savvy investor is expected to scrutinise the relevant performing factors, such as rental yield and capital growth, and make calculating decisions which promise greater profitability. On this basis, the prospective profitability reported in this paper is expected to be greater for savvy investors.

# Acknowledgments 

We acknowledge the financial support by the European Research Council (ERC) for funding this research project, ERC-2013-AdG339182-BAYES_KNOWLEDGE, and Agena Ltd for software support.

## Author Contributions

Conceptualization: AC.
Data curation: AC.
Formal analysis: AC.
Funding acquisition: NF.
Investigation: AC.
Methodology: AC.
Software: AC.
Supervision: AC NF.
Validation: AC.
Visualization: AC.
Writing - original draft: AC NF.
Writing - review \& editing: AC NF.
