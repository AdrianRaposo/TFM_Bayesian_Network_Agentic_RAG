# COMMUNICATIONS BIOLOGY 

## ARTICLE

## Benthic ecosystem cascade effects in Antarctica using Bayesian network inference

Emily G. Mitchell ${ }^{188}$, Rowan J. Whittle ${ }^{2}$ \& Huw J. Griffiths ${ }^{2}$

Antarctic sea-floor communities are unique, and more closely resemble those of the Palaeozoic than equivalent contemporary habitats. However, comparatively little is known about the processes that structure these communities or how they might respond to anthropogenic change. In order to investigate likely consequences of a decline or removal of key taxa on community dynamics we use Bayesian network inference to reconstruct ecological networks and infer changes of taxon removal. Here we show that sponges have the greatest influence on the dynamics of the Antarctic benthos. When we removed sponges from the network, the abundances of all major taxa reduced by a mean of $42 \%$, significantly more than changes of substrate. To our knowledge, this study is the first to demonstrate the cascade effects of removing key ecosystem structuring organisms from statistical analyses of Antarctica data and demonstrates the importance of considering the community dynamics when planning ecosystem management.

[^0]
[^0]:    ${ }^{1}$ Department of Zoology, University of Cambridge, Downing St, Cambridge CB2 3EJ, UK. ${ }^{2}$ British Antarctic Survey, High Cross, Madingley Road, Cambridge CB3 0ET, UK. ${ }^{3}$ email: ek338@cam.ac.uk

The ecological structure of modern Antarctic benthic marine communities differs from the rest of the world. There is a paucity of shell crushing predators (sharks, rays, durophagous decapods), leading to dominance by epifaunal suspension feeding groups such as sponges^{1–5}. Disturbance to dominant benthic taxa, such as the sponges, has the potential to alter the ecosystem, but it is not known how. Generally, there are limited data on the structure and function of Southern Hemisphere benthic ecosystems compared with other areas globally. Despite this limited data, Antarctic benthic marine communities are abundant and diverse^{6} with complex functional diversity and a highly structured, three-dimensional, physical configuration^{1,7–9}.

The South Orkney Islands (SOI) are located in the Southern Ocean, 604 kilometres north-east of the tip of the Antarctic Peninsula, at a latitude of around 60° 35′ S. The seafloor around the SOI has an exceptionally high biodiversity; one-fifth of the animals found in the entire Southern Ocean are represented^{10,11}. Benthic biodiversity in the SOI has been studied previously^{10–12}. Brasier et al.^{10} showed that benthic communities in the SOI were strongly correlated with the hardness of the seafloor. Soft sediments were dominated by deposit feeders, hard surfaces had a greater abundance and richness of taxa, and an overall higher biomass. They were also dominated by filter feeding Vulnerable Marine Ecosystem (VME) taxa^{10}. VME's are marine areas that are vulnerable to the effects of anthropogenic activities, such as fishing^{13}.

The South Orkney Islands Southern Shelf (SOISS) was the first designated Marine Protected Area (MPA) from the high seas on the planet (Fig. 1), established in 2009^{10,14}. MPA's are clearly defined geographically, and managed using legal and protective measures for the long-term conservation of nature, associated ecosystem services, and cultural values^{15}. The SOISS MPA is managed under the Commission for the Conservation of Antarctic Marine Living Resources (CCAMLR)^{10}. Our data come from within the South Orkney MPA and the surrounding area, at the shelf break. Using in situ photographs, ten dominant phyla can be identified from the SOISS benthic invertebrate community. The community is dominated by VME taxa (these are habitat forming taxa which could not be confidently identified from photographs), echinoderms and cnidarians, with frequent bryozoan and poriferan taxa^{10}.

New approaches for assessing biodiversity across MPA's are increasingly important given their increased prevalence in international conservation strategies and the associated costs of assessment and monitoring^{10}. Our study determines the community structure on different spatial scales using Bayesian Network Inference (BNI) analysis. BNI is a technique to statistically infer the causal relationships (or dependencies) between different variables, which in this study are different taxa and different environmental factors such as substrate type and depth^{16}. In the BNI presented here, the variables such as a taxon, or an environmental factor, are described as 'nodes', and the relationship between them as 'connections' (more usually known as 'edges' in network literature), so that the network consists of a series of connected nodes. The strength of the relationship between two nodes (i.e. the strength of the connection) is given by the Influence Score (IS), which is calculated as a cumulative frequency distribution over all possible discrete states^{17}. Discrete Bayesian Network Inference Algorithms (BNIAs) enable the inference of causal relationships (over just mutual correlations), as well as non-linear interactions. We use BNIAs to determine the key taxa and environmental factors that underpin Antarctic benthic community dynamics and use the Bayesian networks to infer likely changes of taxon removal within this MPA.

The BNIA Banjo^{16} was used to generate two different Bayesian networks over different spatial scales^{18}. The fine-scale analysis used 527 individual photographs, which covered 0.51 m^{2} for each sample and the large-scale analyses grouped photographs within

![img-0.jpeg](img-0.jpeg)

**Fig. 1 Locality map. a** Location map of South Orkney Islands sampling and **b**-**e** photographs of key taxa and habitats from the South Orkney Region. **b** Soft sediments dominated by echinoderms and arthropoda; **c** soft sediment with dropstones colonised by cnidaria, bryozoans, sponges, and encrusting taxa; **d** hard substrate dominated by echinoderms and encrusting taxa; **e** large sponge-dominated habitat.

![img-1.jpeg](img-1.jpeg)

**Fig. 2 Fine-scale Bayesian network.** Dependencies between nodes are indicated by the lines connecting them, the width of which indicates the occurrence rate in the bootstrap analyses (wider lines indicate higher occurrence). Arrows indicate nonmutual dependence between two nodes where the head of the arrow is dependent taxa, for example the arrow from region to substrate indicates that substrate depends on region. Mutual dependencies are indicated as double headed arrows. Mean interaction strengths of the correlations are indicated; positive interaction strengths indicating aggregation, negative interaction strengths indicating segregation. Taxa that have no dependencies on another node are not shown. Purple arrows depict dependencies on substrate. The dark blue arrow is between two physical nodes (Region and Substrate). Red arrows are those dependencies resulting from Region and light blue arrows are those that affect percent encrusting.

21 transects of 1.2 km long for each sample. The raw data were filtered to avoid Type I errors through zero-inflation. The fine-scale analysis included the physical nodes: Depth, Substrate and Region (Fig. 1, Supplementary Table 1) and seven taxonomic groups (Supplementary Table 2). The large-scale analysis included Depth, Substrate and Region (Supplementary Table 3) and 12 taxonomic groups (Supplementary Table 4). The data were discretized into zero, low, and high groups[^19], using medians to differentiate the boundary for the low and high abundances. For percentage encrusting and depth, quartiles were used, and modes for region and substrate (Supplementary Tables 5–6). Quartiles are used for percent encrusting and depth rather than medians because there is no zero state for these groups, and so in line with previous work (e.g., Milns et al. 2010), we have used quartiles because just two states would limit the information that could be extracted from this factor, and three is not commonly used. To minimize outliers bias, 100 samples were bootstrapped at 95% level by randomly selecting 95% of the total number of samples for each analysis[^20]. The subsample networks were then found using Banjo, and the final network taken to be the network where the connections occurred in the majority of bootstrapped subsampled with the strength of dependency given by the mean interaction strength of the bootstrapped connections (see 'Methods' for more details). This bootstrapping analysis was applied to both the fine-scale and large-scale data sets.

One of the most powerful aspects of using BNIA is the ability to make inferences of how one node (taxa or physical variable) is likely to change given another node being in a given state (zero, low, or high for a taxon). We used our BN to infer how the most changes in abundance of the most connected taxon would affect the abundances of the other taxa.

### Results

**Fine-scale network.** Within the fine-scale network analyses (~0.51 m²), of the ten nodes included in the analyses, eight were connected within the network, with unidentified VME taxa and arthropods not connected. Substrate was the most connected node (five connections) and depth the least (one connection) (Fig. 2). There was one dependency between two taxa—Cnidarians and Echinoderms. The other dependencies were between physical nodes and taxa and two physical nodes.

![img-2.jpeg](img-2.jpeg)

**Fig. 3 Bayesian networks of large-scale data.** Dependencies between nodes are indicated by the lines connecting them, the width of which indicates the occurrence rate in the bootstrap analyses (wider lines indicate higher occurrence). Single-headed arrows indicate nonmutual dependence between two taxa; mutual dependencies are indicated by double headed arrows. Mean interaction strengths of the correlations are indicated; positive interaction strengths indicating aggregation, negative interaction strengths indicating segregation. Taxa that have no dependencies with another node are not shown. Light blue depicts dependencies between different taxa and purple between physical nodes and taxa.

**Large-scale network.** The large-scale network (between sampling events) had 14 nodes within the analyses, of which Depth, Actinopteri (fish) and Annelids were not connected (Fig. 3). At this spatial-scale there were insufficient samples in the different Region groups to include Region in the analysis. Porifera was the most connected taxon (five connections) and substrate the most connected physical variable (three connections). The strongest dependency was between bryozoans and percentage of encrusting organisms (0.5639) and the only negative dependency was between euryalids (basket stars) and arthropods (−0.1664). All taxa had a direct or indirect connect with Porifera. There were two mutual dependencies between VME unknown and Porifera and between Bryozoa and VME unknown.

**Inferred taxon abundance changes with Porifera removal.** In the large-scale network Porifera is the most connected node and taxon (Fig. 3), and changes in their abundance will influence all taxa apart from the unconnected Annelida. The inferred changes in abundance state for all taxa connected to Porifera are given in Fig. 4 and Supplementary Table 7. For example when Porifera change from 'High' to 'Zero' abundance, the probability of Echinoderms existing in a 'Zero' abundance state increases by 80%, while the probability of 'High' state decreases by 60% (Fig. 4, Supplementary Table 7). This result suggests that if sponges decrease in abundance, the echinoderms will as well. This pattern of decreasing taxa abundance with decreasing Porifera is seen for all connected taxa except arthropods. Arthropods appear robust to changes, owing to negative dependency with Euryalida, which has a positive dependency with Porifera. With this being the smallest effect with a <20% change. Porifera have the greatest impact on Bryozoa, with a 100% change to zero state when Porifera are in zero state. Ophiuroidea see an increase in the probability of a 'Low' abundance state with 'Zero' Porifera state, but this is coupled to an increase in 'Zero' state probability, reflecting an overall abundance decrease. The strength of the effect of a decrease in Porifera on taxa decreases as the length of the chain of dependencies, number of nodes connecting the taxon to Porifera, decreases.

[^19]: Reference 19
[^20]: Reference 20
[^21]: Reference 21
[^22]: Reference 22
[^23]: Reference 23
[^24]: Reference 24
[^25]: Reference 25
[^26]: Reference 26
[^27]: Reference 27
[^28]: Reference 28
[^29]: Reference 29
[^30]: Reference 30
[^31]: Reference 31
[^32]: Reference 32
[^33]: Reference 33
[^34]: Reference 34
[^35]: Reference 35
[^36]: Reference 36
[^37]: Reference 37
[^38]: Reference 38
[^39]: Reference 39
[^40]: Reference 40
[^41]: Reference 41
[^42]: Reference 42
[^43]: Reference 43
[^44]: Reference 44
[^45]: Reference 45
[^46]: Reference 46
[^47]: Reference 47
[^48]: Reference 48
[^49]: Reference 49
[^50]: Reference 50
[^51]: Reference 51
[^52]: Reference 52
[^53]: Reference 53
[^54]: Reference 54
[^55]: Reference 55
[^56]: Reference 56
[^57]: Reference 57
[^58]: Reference 58
[^59]: Reference 59
[^60]: Reference 60
[^61]: Reference 61
[^62]: Reference 62
[^63]: Reference 63
[^64]: Reference 64
[^65]: Reference 65
[^66]: Reference 66
[^67]: Reference 67
[^68]: Reference 68
[^69]: Reference 69
[^70]: Reference 70
[^71]: Reference 71
[^72]: Reference 72
[^73]: Reference 73
[^74]: Reference 74
[^75]: Reference 75
[^76]: Reference 76
[^77]: Reference 77
[^78]: Reference 78
[^79]: Reference 79
[^80]: Reference 80
[^81]: Reference 81
[^82]: Reference 82
[^83]: Reference 83
[^84]: Reference 84
[^85]: Reference 85
[^86]: Reference 86
[^87]: Reference 87
[^88]: Reference 88
[^89]: Reference 89
[^90]: Reference 90
[^91]: Reference 91
[^92]: Reference 92
[^93]: Reference 93
[^94]: Reference 94
[^95]: Reference 95
[^96]: Reference 96
[^97]: Reference 97
[^98]: Reference 98
[^99]: Reference 99
[^100]: Reference 100
[^101]: Reference 101
[^102]: Reference 102
[^103]: Reference 103
[^104]: Reference 104
[^105]: Reference 105
[^106]: Reference 106
[^107]: Reference 107
[^108]: Reference 108
[^109]: Reference 109
[^110]: Reference 110
[^111]: Reference 111
[^112]: Reference 112
[^113]: Reference 113
[^114]: Reference 114
[^115]: Reference 115
[^116]: Reference 116
[^117]: Reference 117
[^118]: Reference 118
[^119]: Reference 119
[^120]: Reference 120
[^121]: Reference 121
[^122]: Reference 122
[^123]: Reference 123
[^124]: Reference 124
[^125]: Reference 125
[^126]: Reference 126
[^127]: Reference 127
[^128]: Reference 128
[^129]: Reference 129
[^130]: Reference 130
[^131]: Reference 131
[^132]: Reference 132
[^133]: Reference 133
[^134]: Reference 134
[^135]: Reference 135
[^136]: Reference 136
[^137]: Reference 137
[^138]: Reference 138
[^139]: Reference 139
[^140]: Reference 140
[^141]: Reference 141
[^142]: Reference 142
[^143]: Reference 143
[^144]: Reference 144
[^145]: Reference 145
[^146]: Reference 146
[^147]: Reference 147
[^148]: Reference 148
[^149]: Reference 149
[^150]: Reference 150
[^151]: Reference 151
[^152]: Reference 152
[^153]: Reference 153
[^154]: Reference 154
[^155]: Reference 155
[^156]: Reference 156
[^157]: Reference 157
[^158]: Reference 158
[^159]: Reference 159
[^160]: Reference 160
[^161]: Reference 161
[^162]: Reference 162
[^163]: Reference 163
[^164]: Reference 164
[^165]: Reference 165
[^166]: Reference 166
[^167]: Reference 167
[^168]: Reference 168
[^169]: Reference 169
[^170]: Reference 170
[^171]: Reference 171
[^172]: Reference 172
[^173]: Reference 173
[^174]: Reference 174
[^175]: Reference 175
[^176]: Reference 176
[^177]: Reference 177
[^178]: Reference 178
[^179]: Reference 179
[^180]: Reference 180
[^181]: Reference 181
[^182]: Reference 182
[^183]: Reference 183
[^184]: Reference 184
[^185]: Reference 185
[^186]: Reference 186
[^187]: Reference 187
[^188]: Reference 188
[^189]: Reference 189
[^190]: Reference 190
[^191]: Reference 191
[^192]: Reference 192
[^193]: Reference 193
[^194]: Reference 194
[^195]: Reference 195
[^196]: Reference 196
[^197]: Reference 197
[^198]: Reference 198
[^199]: Reference 199
[^200]: Reference 200
[^201]: Reference 201
[^202]: Reference 202
[^203]: Reference 203
[^204]: Reference 204
[^205]: Reference 205
[^206]: Reference 206
[^207]: Reference 207
[^208]: Reference 208
[^209]: Reference 209
[^210]: Reference 210
[^211]: Reference 211
[^212]: Reference 212
[^213]: Reference 213
[^214]: Reference 214
[^215]: Reference 215
[^216]: Reference 216
[^217]: Reference 217
[^218]: Reference 218
[^219]: Reference 219
[^220]: Reference 220
[^221]: Reference 221
[^222]: Reference 222
[^223]: Reference 223
[^224]: Reference 224
[^225]: Reference 225
[^226]: Reference 226
[^227]: Reference 227
[^228]: Reference 228
[^229]: Reference 229
[^230]: Reference 230
[^231]: Reference 231
[^232]: Reference 232
[^233]: Reference 233
[^234]: Reference 234
[^235]: Reference 235
[^236]: Reference 236
[^237]: Reference 237
[^238]: Reference 238
[^239]: Reference 239
[^240]: Reference 240
[^241]: Reference 241
[^242]: Reference 242
[^243]: Reference 243
[^244]: Reference 244
[^245]: Reference 245
[^246]: Reference 246
[^247]: Reference 247
[^248]: Reference 248
[^249]: Reference 249
[^250]: Reference 250
[^251]: Reference 251
[^252]: Reference 252
[^253]: Reference 253
[^254]: Reference 254
[^255]: Reference 256
[^256]: Reference 257
[^257]: Reference 258
[^258]: Reference 259
[^259]: Reference 259
[^260]: Reference 260
[^261]: Reference 261
[^262]: Reference 262
[^263]: Reference 263
[^264]: Reference 264
[^265]: Reference 265
[^266]: Reference 266
[^267]: Reference 267
[^268]: Reference 268
[^269]: Reference 269
[^270]: Reference 270
[^271]: Reference 271
[^272]: Reference 272
[^273]: Reference 273
[^274]: Reference 274
[^275]: Reference 276
[^276]: Reference 277
[^277]: Reference 278
[^278]: Reference 279
[^279]: Reference 279
[^280]: Reference 280
[^281]: Reference 281
[^282]: Reference 282
[^283]: Reference 283
[^284]: Reference 284
[^285]: Reference 285
[^286]: Reference 286
[^287]: Reference 287
[^288]: Reference 288
[^289]: Reference 289
[^290]: Reference 290
[^291]: Reference 291
[^292]: Reference 292
[^293]: Reference 293
[^294]: Reference 294
[^295]: Reference 295
[^296]: Reference 297
[^297]: Reference 298
[^298]: Reference 299
[^299]: Reference 299
[^300]: Reference 299
[^301]: Reference 291
[^302]: Reference 292
[^303]: Reference 293
[^304]: Reference 294
[^305]: Reference 295
[^306]: Reference 296
[^307]: Reference 297
[^308]: Reference 298
[^309]: Reference 299
[^310]: Reference 291
[^311]: Reference 292
[^312]: Reference 293
[^313]: Reference 294
[^314]: Reference 295
[^315]: Reference 296
[^316]: Reference 297
[^317]: Reference 298
[^318]: Reference 299
[^319]: Reference 291
[^320]: Reference 292
[^321]: Reference 293
[^322]: Reference 294
[^323]: Reference 295
[^324]: Reference 296
[^325]: Reference 297
[^326]: Reference 298
[^327]: Reference 299
[^328]: Reference 291
[^329]: Reference 292
[^330]: Reference 293
[^331]: Reference 294
[^332]: Reference 295
[^333]: Reference 296
[^334]: Reference 297
[^335]: Reference 298
[^336]: Reference 299
[^337]: Reference 291
[^338]: Reference 292
[^339]: Reference 293
[^340]: Reference 294
[^341]: Reference 295
[^342]: Reference 296
[^343]: Reference 297
[^344]: Reference 298
[^345]: Reference 299
[^346]: Reference 291
[^347]: Reference 292
[^348]: Reference 293
[^349]: Reference 294
[^350]: Reference 295
[^351]: Reference 296
[^352]: Reference 297
[^353]: Reference 298
[^354]: Reference 299
[^355]: Reference 296
[^356]: Reference 297
[^357]: Reference 298
[^358]: Reference 299
[^359]: Reference 291
[^360]: Reference 292
[^361]: Reference 293
[^362]: Reference 294
[^363]: Reference 295
[^364]: Reference 296
[^365]: Reference 297
[^366]: Reference 298
[^367]: Reference 299
[^368]: Reference 299
[^369]: Reference 291
[^370]: Reference 292
[^371]: Reference 293
[^372]: Reference 294
[^373]: Reference 295
[^374]: Reference 296
[^375]: Reference 297
[^376]: Reference 298
[^377]: Reference 299
[^378]: Reference 291
[^379]: Reference 292
[^380]: Reference 293
[^381]: Reference 294
[^382]: Reference 295
[^383]: Reference 296
[^384]: Reference 297
[^385]: Reference 298
[^386]: Reference 299
[^387]: Reference 291
[^388]: Reference 292
[^389]: Reference 293
[^390]: Reference 294
[^391]: Reference 295
[^392]: Reference 296
[^393]: Reference 297
[^394]: Reference 298
[^395]: Reference 299
[^396]: Reference 291
[^397]: Reference 292
[^398]: Reference 293
[^399]: Reference 294
[^400]: Reference 295
[^401]: Reference 296
[^402]: Reference 297
[^403]: Reference 298
[^404]: Reference 299
[^405]: Reference 296
[^406]: Reference 297
[^407]: Reference 298
[^408]: Reference 299
[^409]: Reference 291
[^410]: Reference 292
[^411]: Reference 293
[^412]: Reference 294
[^413]: Reference 295
[^414]: Reference 296
[^415]: Reference 297
[^416]: Reference 298
[^417]: Reference 299
[^418]: Reference 291
[^419]: Reference 292
[^420]: Reference 293
[^421]: Reference 294
[^422]: Reference 295
[^423]: Reference 296
[^424]: Reference 297
[^425]: Reference 298
[^426]: Reference 299
[^427]: Reference 291
[^428]: Reference 292
[^429]: Reference 293
[^430]: Reference 294
[^431]: Reference 295
[^432]: Reference 296
[^433]: Reference 297
[^434]: Reference 298
[^435]: Reference 299
[^436]: Reference 291
[^437]: Reference 292
[^438]: Reference 293
[^439]: Reference 294
[^440]: Reference 295
[^441]: Reference 296
[^442]: Reference 297
[^443]: Reference 298
[^444]: Reference 299
[^445]: Reference 296
[^446]: Reference 297
[^447]: Reference 298
[^448]: Reference 299
[^449]: Reference 291
[^450]: Reference 292
[^451]: Reference 296
[^452]: Reference 297
[^453]: Reference 298
[^454]: Reference 299
[^455]: Reference 296
[^456]: Reference 297
[^457]: Reference 298
[^458]: Reference 299
[^459]: Reference 291
[^460]: Reference 292
[^461]: Reference 293
[^462]: Reference 294
[^463]: Reference 295
[^464]: Reference 296
[^465]: Reference 297
[^466]: Reference 298
[^467]: Reference 299
[^468]: Reference 291
[^469]: Reference 292
[^470]: Reference 291
[^471]: Reference 292
[^472]: Reference 293
[^473]: Reference 294
[^474]: Reference 295
[^475]: Reference 296
[^476]: Reference 297
[^477]: Reference 298
[^478]: Reference 291
[^479]: Reference 292
[^480]: Reference 293
[^481]: Reference 294
[^482]: Reference 295
[^483]: Reference 296
[^484]: Reference 297
[^485]: Reference 291
[^486]: Reference 292
[^487]: Reference 293
[^488]: Reference 291
[^489]: Reference 292
[^490]: Reference 291
[^491]: Reference 292
[^492]: Reference 293
[^493]: Reference 294
[^494]: Reference 295
[^495]: Reference 296
[^496]: Reference 297
[^497]: Reference 298
[^498]: Reference 291
[^499]: Reference 292
[^500]: Reference 293
[^501]: Reference 294
[^502]: Reference 295
[^503]: Reference 296
[^504]: Reference 297
[^505]: Reference 298
[^506]: Reference 299
[^507]: Reference 291
[^508]: Reference 292
[^509]: Reference 293
[^510]: Reference 294
[^511]: Reference 295
[^512]: Reference 296
[^513]: Reference 297
[^514]: Reference 291
[^515]: Reference 296
[^516]: Reference 297
[^517]: Reference 298
[^518]: Reference 291
[^519]: Reference 292
[^520]: Reference 293
[^521]: Reference 294
[^522]: Reference 295
[^523]: Reference 296
[^524]: Reference 297
[^525]: Reference 298
[^526]: Reference 299
[^527]: Reference 291
[^528]: Reference 292
[^529]: Reference 293
[^530]: Reference 294
[^531]: Reference 295
[^532]: Reference 296
[^533]: Reference 297
[^534]: Reference 298
[^535]: Reference 299
[^536]: Reference 291
[^537]: Reference 292
[^538]: Reference 293
[^539]: Reference 294
[^540]: Reference 295
[^541]: Reference 296
[^542]: Reference 297
[^543]: Reference 298
[^544]: Reference 299
[^545]: Reference 296
[^546]: Reference 297
[^547]: Reference 298
[^548]: Reference 299
[^549]: Reference 291
[^550]: Reference 292
[^551]: Reference 296
[^552]: Reference 297
[^553]: Reference 298
[^554]: Reference 299
[^555]: Reference 291
[^556]: Reference 297
[^557]: Reference 298
[^558]: Reference 299
[^559]: Reference 291
[^560]: Reference 291
[^561]: Reference 292
[^562]: Reference 295
[^563]: Reference 296
[^564]: Reference 297
[^565]: Reference 298
[^566]: Reference 299
[^567]: Reference 298
[^568]: Reference 299
[^569]: Reference 291
[^570]: Reference 292
[^571]: Reference 293
[^572]: Reference 291
[^573]: Reference 292
[^574]: Reference 297
[^575]: Reference 298
[^576]: Reference 299
[^577]: Reference 298
[^578]: Reference 299
[^579]: Reference 291
[^580]: Reference 292
[^581]: Reference 293
[^582]: Reference 291
[^583]: Reference 297
[^584]: Reference 298
[^585]: Reference 299
[^586]: Reference 291
[^587]: Reference 299
[^588]: Reference 299
[^589]: Reference 291
[^590]: Reference 292
[^591]: Reference 293
[^592]: Reference 291
[^593]: Reference 292
[^594]: Reference 297
[^595]: Reference 298
[^596]: Reference 299
[^597]: Reference 298
[^598]: Reference 299
[^599]: Reference 291
[^600]: Reference 292
[^601]: Reference 293
[^602]: Reference 291
[^603]: Reference 295
[^604]: Reference 297
[^605]: Reference 298
[^606]: Reference 291
[^607]: Reference 298
[^608]: Reference 299
[^609]: Reference 291
[^610]: Reference 292
[^611]: Reference 293
[^612]: Reference 291
[^613]: Reference 295
[^614]: Reference 297
[^615]: Reference 298
[^616]: Reference 291
[^617]: Reference 298
[^618]: Reference 299
[^619]: Reference 291
[^620]: Reference 292
[^621]: Reference 293
[^622]: Reference 291
[^623]: Reference 295
[^624]: Reference 297
[^625]: Reference 298
[^626]: Reference 291
[^627]: Reference 291
[^628]: Reference 291
[^629]: Reference 292
[^630]: Reference 291
[^631]: Reference 293
[^632]: Reference 291
[^633]: Reference 295
[^634]: Reference 297
[^635]: Reference 298
[^636]: Reference 291
[^637]: Reference 291
[^638]: Reference 291
[^639]: Reference 291
[^640]: Reference 297
[^641]: Reference 291
[^642]: Reference 291
[^643]: Reference 297
[^642]: Reference 291
[^644]: Reference 297
[^645]: Reference 298
[^646]: Reference 298
[^647]: Reference 298
[^648]: Reference 291
[^649]: Reference 291
[^650]: Reference 291
[^651]: Reference 291
[^652]: Reference 291
[^653]: Reference 295
[^652]: Reference 291
[^653]: Reference 298
[^654]: Reference 298
[^655]: Reference 298
[^656]: Reference 298
[^657]: Reference 298
[^658]: Reference 291
[^659]: Reference 291
[^660]: Reference 291
[^661]: Reference 291
[^662]: Reference 291
[^662]: Reference 291
[^663]: Reference 291
[^664]: Reference 298
[^665]: Reference 298
[^666]: Reference 291
[^667]: Reference 298
[^668]: Reference 291
[^669]: Reference 291
[^670]: Reference 291
[^671]: Reference 291
[^672]: Reference 291
[^673]: Reference 291
[^674]: Reference 298
[^675]: Reference 298
[^676]: Reference 298
[^677]: Reference 291
[^677]: Reference 291
[^678]: Reference 291
[^679]: Reference 291
[^680]: Reference 291
[^681]: Reference 291
[^682]: Reference 291
[^683]: Reference 291
[^684]: Reference 291
[^685]: Reference 291
[^686]: Reference 291
[^687]: Reference 291
[^688]: Reference 291
[^690]: Reference 291
[^691]: Reference 291
[^692]: Reference 291
[^692]: Reference 291
[^693]: Reference 291
[^694]: Reference 291
[^695]: Reference 291
[^696]: Reference 291
[^697]: Reference 291
[^700]: Reference 291
[^697]: Reference 291
[^698]: Reference 291
[^700]: Reference 291
[^699]: Reference 291
[^700]: Reference 291
[^701]: Reference 291
[^702]: Reference 291
[^703]: Reference 291
[^704]: Reference 291
[^705]: Reference 291
[^706]: Reference 291
[^707]: Reference 291
[^708]: Reference 291
[^709]: Reference 291
[^710]: Reference 291
[^711]: Reference 291
[^711]: Reference 291
[^711]: Reference 291
[^711]: Reference 291
[^712]: Reference 291
[^713]: Reference 291
[^714]: Reference 291
[^715]: Reference 291
[^716]: Reference 291
[^717]: Reference 291
[^717]: Reference 291
[^717]: Reference 291
[^718]: Reference 291
[^719]: Reference 291
[^720]: Reference 291
[^721]: Reference 291
[^721]: Reference 291
[^722]: Reference 291
[^723]: Reference 291
[^724]: Reference 291
[^725]: Reference 291
[^726]: Reference 291
[^727]: Reference 291
[^728]: Reference 291
[^729]: Reference 291
[^730]: Reference 291
[^730]: Reference 291
[^731]: Reference 291
[^731]: Reference 291
[^732]: Reference 291
[^733]: Reference 291
[^734]: Reference 291
[^735]: Reference 291
[^736]: Reference 291
[^737]: Reference 291
[^738]: Reference 291
[^739]: Reference 291
[^740]: Reference 291
[^741]: Reference 291
[^742]: Reference 291
[^740]: Reference 291
[^741]: Reference 291
[^742]: Reference 291
[^743]: Reference 291
[^742]: Reference 291
[^744]: Reference 291
[^750]: Reference 291
[^751]: Reference 291
[^752]: Reference 291
[^753]: Reference 291
[^754]: Reference 291
[^755]: Reference 291
[^756]: Reference 291
[^757]: Reference 291
[^761]: Reference 291
[^761]: Reference 291
[^762]: Reference 291
[^762]: Reference 291
[^763]: Reference 291
[^764]: Reference 291
[^765]: Reference 291
[^7777]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291
[^780]: Reference 291


![img-3.jpeg](img-3.jpeg)

Fig. 4 Schematic diagrams showing how the probabilities of each taxa being in a given state (zero, low, high) change given Porifera states. The thickness of the arrow connecting different states indicates the percentage change between the two connected states. The thickness of the node indicates the proportion of samples in that state.

The effect of the changing abundance state of Porifera had a significant influence on the community, with a mean change in probability state (from High to Zero) $\Delta p^{\text {Porifera }}=0.4210$. In contrast, the mean change in probabilities between different substrates is smaller (Supplementary Tables 7-9): between Silt to Rocky $\left(\Delta p^{\text {Silt to Rocky }}=0.2181\right)$, Silt to Gravel $\left(\Delta p^{\text {Silt to Gravel }}=\right.$ 0.3569 ) and Rocky to Gravel $\left(\Delta p^{\text {Rocky to Gravel }}=0.1883\right)$.

## Discussion

To our knowledge, this study is the first time the cascade effects of removing key ecosystem structuring organisms has been found with statistical analyses of data from a Marine Protected Area. By considering the community as a network of interactions, we were able to quantify the relative importance of different taxa. Porifera was the most connected variable within the large spatial-scale network and we were able to demonstrate the cascading effects that changing their abundance had on other taxa. These effects varied, depending on the proximity of each taxon to Porifera and the nature of the dependency, suggesting that different taxa have different resilience to the removal of sponges. However, the effects were mostly negative: a decrease in Porifera led to a decrease in echinoderms, molluscs, bryozoans and ophiuroids. Cnidarians had an intermediate dependency, and showed a smaller reduction. Notably, changing the abundance of Porifera had a stronger influence on the abundance of other taxa than changing the substrate type (Supplementary Tables 7-9), showing that the contribution of Porifera to the network is likely over and above them just being a colonisation substrate.

The only group that showed an increase in abundance with a decrease in sponges were the arthropods. However, only certain large and conspicuous arthropod taxa (decapods and large pyc-nogonids-Brasier et al. ${ }^{20}$ ) were detectable using the photographic analysis. The majority of images with high arthropod numbers were in areas of open, muddy habitat, leaving the individuals exposed and easier to count. Many smaller arthropods, such as isopods and amphipods (generally not detected using this scale of photography), are known to have strong positive ecological associations with Antarctic sponges, where the highest mean density of amphipods on a single sponge was 1295 individuals ${ }^{21}$. The predicted increase in arthropod numbers probably only applies to the observed large species that have a preference for open habitats, e.g., Nematocarcinus lanceopes and Notocrangon antarcticus.

Antarctic sponge-dominated communities are structured by biological interactions, supporting diverse microbial and macrofaunal communities ${ }^{21,22}$. Predation upon sponges is important in structuring Antarctic benthic communities ${ }^{23,24}$. They act as settling surfaces, contributing considerable structural heterogeneity to numerous colonising epibionts including benthic diatoms and bacteria ${ }^{24-29}$. Larger invertebrates such as polychaete worms, bivalves, gastropods, amphipods and isopods live on, and in sponges ${ }^{24,30}$. Sponges also directly affect the physical characteristics, structural and oceanographic, of the benthic habitat. Large demosponges and hexactinellids change the small-scale topography of the seafloor, providing new microhabitats and biogenic hard substrates. They also have the ability to transform the local oceanography by physically obstructing currents and, as active filter feeders, pumping thousands of litres of seawater through their systems and removing or concentrating nutrients ${ }^{31}$.

Porifera can dominate some Antarctic seafloor communities. While forming a significant component of the community in our data, they are not the most numerous taxon, however, they do

dominate the biomass in most regions^{10}. This study highlights the importance of sponges to the South Orkney ecosystem, as the organisms that have the most connections within our network and their significant influence on taxon abundance probabilities (Figs. 3, 4). Our result provided quantitative support for their importance as community structuring organisms, as highlighted by Bell^{29}.

Potential threats to the South Orkney ecosystem, in particular the sponges, include climate change, longline fishing and ocean acidification. Ocean warming is thought to cause increased thermal stress on sponge assemblages. This stress could cause disease and mortality owing to a decrease in the efficacy of defence mechanisms, and via the development of pathogens^{32}. There are currently no commercial bottom fisheries within the South Orkney area, however, demersal fishing is occurring in other areas with similar habitats and ecology. Longline fishing for Patagonian toothfish occurs around South Georgia and other sub-Antarctic islands^{14,33}. Research fishing for toothfish has also recently expanded to include a wider area, reaching to the north of the South Orkney Islands^{14}, putting the whole area at risk. At present the SOISS MPA covers <50% of the shelf and slope of the region meaning that the majority of the archipelago could be vulnerable to future fishing.

Our Bayesian network inference shows that disruption to the benthic community will cause cascade effects on many areas of the ecosystem, potentially leading to a regime shift from a rich and diverse epibenthic community supported by sponges, to an infaunal dominated system. The removal of sponges could result in a replacement by other habitat forming groups. However, our network analyses found that large branching or erect cnidarians did not mediate sponge loss and, given their physical structure, would be under similar threat from benthic fishing as the sponges^{35}. Organisms with calcified skeletons, bryozoans and some cnidarians, are at an even greater risk from ocean acidification than sponges^{35}; making the simple replacement of sponges with other similar groups unlikely, resulting in a marked change to both the habitat and community structure with the loss of the major three-dimensional structures.

As with all benthic image based analyses, many groups will be underrepresented. This underrepresentation is particularly true for the dominant infauna in soft sediment areas^{10} (e.g. polychaetes and molluscs), and for organisms that are too small to capture in the image. This network method for understanding ecological change included a variety of data types, such as different physical variables, as well as biotic abundances. In order to delve deeper into ecosystems dynamics, the inclusion of more physical variables, such as temperature or pH, would enable further inference of how these communities are likely to change in the near future.

There are notable differences between the processes that regulate the fine and large-scale networks in our results. The fine spatial-scale networks were dominated by environmental variables, whereas the larger scale networks were dominated by taxa interactions. In the fine spatial-scale networks, substrate was the most connected node, and therefore changes in the substrate would have the greatest effect on the community. This reflects the findings of other studies around Antarctica^{10,36,37}. Hard surfaces are linked to an abundance of Bryozoa, Porifera, Cnidaria and Echinodermata, owing to the potential for colonisation by a diversity of benthic organisms. There is only one taxonomic dependency at this fine scale—between Cnidaria and Echinodermata. Environmental factors, such as currents and hard surfaces, particularly on a small and medium scale, are conducive to the growth and diversity of suspension feeding assemblages. For dense aggregations of suspension feeders to occur, abundant suspended material, and water movement are needed^{1}; hard surfaces are also required for colonisation. Areas where there are large accumulations of structural organisms, such as sponges, tend to be in more hydrodynamically active regions^{1}, with surfaces suitable for colonisation. These requirements may be reflected by the influence of Substrate in our large-scale results. Antarctic benthic communities show a large amount of patchiness in species composition at small or intermediate spatial scales^{1,7}. Our fine-scale analyses likely reflect the local environmental patchiness, at a between photograph scale, that result in these changes. The differences between the fine and large-scale networks demonstrate the importance of taking into account different spatial scales—without the large-scale network the between taxon interactions would not have been revealed.

To our knowledge, this study provides the first statistical evidence that changes to sponge-dominated communities will have cascading effects on most other aspects of Antarctic benthic community structure. This method provides a methodology to identify these habitat structuring taxa, in order to prioritise them for further protection, and for them to be considered in management plans for potentially harmful anthropogenic activities such as longline fishing. The dominance of sponges in driving our networks show that some VME taxa are more vital in maintaining the overall health of an ecosystem than others. Given these results, sponges should be considered as a priority, even above other VME taxa, when designing new conservation measures in Antarctica and the Southern Ocean.

## Methods

The data for this study were collected in the austral summer of 2016, on board the BAS research ship RRS James Clark Ross^{38}. Biological abundance data was taken from photographic images from Brasier et al.^{10} (see methodology within). The images were taken with a Shallow Underwater Camera System (SUCS), in transects of 10 photographs, 10 m apart. Replicant transects were separated by 100 m, at water depths of 500 m, 750 m and 1000 m^{10}. Each photograph in the analysis was 0.51 m^{2} in area. In the analyses, ‘VME unknown' was biological material unidentifiable to phylum, but distinguishable as VME taxa, e.g. branched or budding fragments which could be bryozoan or cnidarian species. The percentage cover of encrusting species was recorded by Brasier et al.^{10}, as the number of individual colonies was not always possible to distinguish between colonising taxa^{10}. Physical variables, such as substrate texture, were also observed from the SUCS images^{10}.

Taxonomic resolution of the data originally collected was dependent upon the ability to distinguish the organism in the images^{10}. For our analysis, the taxonomic hierarchy analysed related to the abundance level of that group, as lower abundance, finer scale taxonomic groupings would be zero-inflated so not able to be used within our methodology (cf. Milns et al.^{39}). Taxonomic groupings included were Annelida, Arthropoda, Cnidaria, Echinodermata, Mollusca, Bryozoa, Actinopteri, Porifera and Echinodermata. The echinoderm taxa Ophiuroides and Euryalids also occurred in large enough numbers to be analysed as separate groups. The taxa in each of these groupings can be seen in the Brasier et al.^{10}

The raw data (taxon ID from photographs) was highly zero-inflated (84.9% of entries), so data grouping was performed to capture the fine-scale (individual photographs at ∼cm scale) and large-scale (replicate transects at ∼km scale) ecology of the ecosystems. For the fine-scale network there were 527 samples (abundances from individual photographs) and twelve nodes. Four were physical nodes (Depth, Region, Substrate and Substrate Texture, Table 1), two were functions of the specimens present (percent encrusting), five were taxa classified to Phylum level (Arthropoda, Bryozoa, Porifera, Cnidaria and Echinodermata) and there was one bin-group (VME Unknown) Supplementary Table 2.

For the large-scale network, the data from all the photographs in each event (up to three replicate transects) was combined to form 21 samples with 16 nodes. For factor nodes (Region, Texture and Substrate) the modal variable was taken, taxa nodes were summed, and the mean was used for Percent Encrusting and Depth. Texture was excluded from analyses due to the high zero-count. Two nodes were functions of the specimens present (percent encrusting), ten taxa were analysed (Annelid, Arthropod, Cnidarian, Echinoderm, Mollusc, Bryozoan, Actinopteri, Ophiuroidea, Euryalida, Porifera) and one bin-group (VME Unknown) was used. The combination of the two networks enabled the investigation of both physical and biotic interactions across multiple spatial scales.

We chose these relatively coarse taxonomic groupings in order to maximise the statistical power of our analyses. This statistical power enabled us to reconstruct a complex network of dependencies, thus revealing the subtle relationships between different taxa. The coarse grouping is a limitation of this method, because the homogenisation of some diverse groups, such as echinoderms, groups together organisms with variable life modes and traits (and therefore differing relationships with other taxa). However, the coarse level of identification was necessary with this volume of data (over 500 photographs), and the patchiness and rarity of many taxa. Future studies involving a higher density of photographs will allow for genus or species level separation, and/or an analysis based upon functional traits classification.

Table 1 Table of network properties for the two networks found. Chains are defined as series of dependencies containing more than two nodes. Link density is mean number of connections per node, connectance is the number of connections/number of nodes*(number of nodes-1).

dependencies | Negative
dependencies | Mutual | Connectance | Link
density | Maximum
chain length | Number
of chains | Mean
chain length  |

Analysis. One approach to understanding how ecosystems function is to consider the ecosystem as a network (cf. Miln et al. ${ }^{28}$ ). Different taxa or groups of taxa are considered 'nodes' and their interactions are described as 'connections' (more usually known as 'edges' in Baysian networks), which link interacting taxa together. A node that the connections feed into are called 'parents'. Work has centred on gene regulatory networks ${ }^{27}$, neural information flow networks, and with more recent applications to ecological and palaeoecological networks ${ }^{18,39-41}$. It is important to note that the structure produced by the BNIA reflects the associations caused by co-localisations (two taxa which both have a high abundance), not by a specific interaction, for example predation. By using BNIA, direct dependencies between taxa can be detected, minimising auto-correlation between two nodes. For example, if A depends on B which depends on C, there could be a correlation between A and C. However, this correlation would not represent an interaction or association between A and C, merely the two correlations between A and B and B and C. BNIA enables only the realised dependencies to be found, ensuring only actual interactions and associations are found.

Bayesian network inference was performed in Banjo ${ }^{16}$. The BNIA software used was Banjo v2.0.0, a publicly available Java based algorithm ${ }^{29,41}$. Banjo uses uniform priors, so boundaries for the different discretized groups were chosen to ensure even splitting between the groups. Discretized data were input into Banjo, which then generated a random network based on the input variables. A greedy search was then performed to find a more likely network than the random one generated. This search was repeated 10 million times for each set of input data and the most probable network was then output. The maximum number of parents was set to 3 to limit artefacts ${ }^{29}$.

The BNIA used require discrete data, which ensures data noise is masked, and only the relative densities of each taxon are important ${ }^{39}$. We split the data into three intervals; zero counts, low counts and high counts. Low counts consisted of counts below the median for the taxa group and high counts were counts over the median. Medians were used over means because for some groups the high counts were very high, and would result in a very small number of samples grouped in the highest interval (cf. Milns et al. ${ }^{29}$ ). A large amount of bins maintains the amount of information present in the dataset, while fewer bins provide more statistical power, and greater noise masking. Yu ${ }^{19}$ has shown that for ecological data sets three different bins is a good balance. Zero was treated as a separate entity because the presence of one individual is very different to a zero presence, in contrast to zero gene expression, for example. Data preparation for Banjo (grouping and discretization) was carried out in $\mathrm{R}^{42}$, as was the statistical analysis of the data. Further analysis of banjo outputs, when required, used the functional language Haskell ${ }^{43}$. The scripts are available on Github (github.com/egmitchell/bootstrap).

To minimise outliers bias, 100 samples were bootstrapped at $95 \%$ level by randomly selecting $95 \%$ of the total number of samples for each analysis ${ }^{29,43}$, and then finding the subsample network using Banjo. For each connection calculated, the probability of occurrence was calculated, and the resultant distributions analysed to find the number of Gaussian sub-distributions using normal mixture models ${ }^{44}$. This probability distribution was bimodal for each data set, which suggests that there were two distributions of connections, those with low probability of occurrence, and those with highly probable connections. The final network for each area was taken to be those connections which were highly probable. The threshold for being labelled 'highly probable' depended on the network (as determined by the normal mixture modelling analyses): $53 \%$ for fine-scale network and $51 \%$ for the large-scale network. The magnitude of the occurrence rate is indicated in the network by the width of the line depicting the connection.

The direction of the connection between nodes indicates which node (taxon) has a dependency on the other node (taxon). For each connection, the directionality was taken to be the direction that occurred in the majority of bootstrapped networks. Where there was no majority (directional connections have a probability between 0.4 and 0.6 ), the connection was said to have bidirectionality, or indicated a mutual dependency.

The IS can be used to gauge the type and strength of the interaction between two nodes. If the IS $=1$, this corresponds with a positive correlation. When node 1 is high, node 2 will be high. An IS of -1 corresponds to a negative correlation: High node 1 corresponds to a low node 2 . An $\mathrm{IS}=0$ does not mean there is no correlation between the two nodes. IS $=0$ means that the interaction is nonmonotonic. Sometimes node 1 will be positively correlated with node 2 , sometimes negatively. The mean IS for each connection was calculated for each sample area.

Contingency test filtering. In order to avoid Type I errors introduced by high zero counts, which is common in ecological data sets, we excluded rare taxa, which were found in under $33 \%$ of the grid cells. Note, that this method of exclusion could potentially mean that a taxon with high abundance in a very limited area is excluded from analyses. To further guard against Type I errors, we also used a method of contingency test filtering that removed from consideration a connection between two variables whose joint distribution showed no evidence of deviation from the distribution expected from their combined marginal distributions (chisquared tests, $p>0.25)^{44}$. This threshold was used to ensure no chance of removing truly dependent dependencies, so that only artefacts such as those found between high zero counts were removed from consideration. These links were provided to the BNIA to exclude from consideration.

Inference. Inferring how one node (taxa or physical variable) is likely to change given another node being in a given state is done by calculating the probability of node A being in a given state given node B is in a given state. All nodes that have dependencies between A and B and so are included in the calculation:

$$ \mathrm{P}(\mathrm{~A} \mid \mathrm{B})=\sum_{m=1}^{m=N_{m}+1} \frac{\prod_{i=1}^{m=N} \mathrm{P}\left(\mathrm{~B}*{i} \mid A*{p+1}\right)}{\sum_{m=1}^{m=N} P\left(B \mid A_{m}\right) P\left(A_{m}\right)} $$

The $N$ are the total number of nodes in the chain and $n$ and $m$ are the indices for the chain of nodes of length N connecting the first and end nodes. S are the number of discrete states for each node, which are indexed $s$. In order to infer the likely change of one taxon's (A) abundance on another's abundance (B), the probabilities of all taxa that occur in the network between A and B have to be taken into account. For example, for the probability that B is in a Zero abundance state given A is in a high abundance state, and given that B are connected through a dependency of B on C and C on A , the probability is calculated as follows: the probabilities of C existing in all states is calculated given a High abundance state for A , and then the probabilities for B existing in a Zero state is calculated for each state of C and then summed together to give the probability of B in Zero given A in high. To work out the inferred change in B given a change in A from High to Zero would involve taking the difference between the probabilities for each state of B given A is high with each state of B given A is low. For the code used to generate these inferred probabilities, please see ref. ${ }^{45}$.

Reporting summary. Further information on research design is available in the Nature Research Reporting Summary linked to this article.

## Data availability

Data generated within the study was modified from Braiser et al. ${ }^{10}$ and is available in the public repository Figshare ${ }^{46}$ : https://doi.org/10.6084/m9.figshare.12214568.v1.

## Code availability

Code is available on github.com/egmitchell/bootstrap and ref. ${ }^{45}$ : https://doi.org/10.5281/ zenodo. 3969969 .

Received: 8 May 2020; Accepted: 16 September 2020; Published online: 16 October 2020

## Acknowledgements

Natural Environment Research Council Independent Research Fellowship NE/S014756/1 to E.G.M. R.J.W. and H.J.G. are part of the British Antarctic Survey Polar Science for Planet Earth Programme; R.J.W. in the BAS Palaeoenvironments, Ice-sheets and Climate Change team and HJG in the Biodiversity, Evolution and Adaptation team. We thank Dr Madeline Brasier for analysing and quantifying the original photographs, the officers and crew of the RRS James Clark Ross and the participants in the SO-AntEco expedition (JR15005). This work is a contribution to the SCAR (Scientific Committee on Antarctic Research) AntEco (State of the Antarctic Ecosystem) Programme.

## Author contributions

E.G.M., R.J.W., and H.J.G. conceived the study, discussed the results, wrote the text, and made the figures. E.G.M. analysed the data. H.J.G. led the team collecting the original data.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s42003-020-01310-8.

Correspondence and requests for materials should be addressed to E.G.M.
Reprints and permission information is available at http://www.nature.com/reprints
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/ licenses/by/4.0/