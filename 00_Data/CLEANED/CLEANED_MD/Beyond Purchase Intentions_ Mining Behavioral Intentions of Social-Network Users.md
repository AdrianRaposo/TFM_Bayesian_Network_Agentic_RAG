# 1. A complete description of the features used in our models 

A diagram of our intention-inference model is shown in Figure 1. Note that Figure 1 is brought for illustration purposes and thus only features edges between layers; edges between specific nodes must be determined separately for each intention according to its own unique priors, intention-specific features and results of feature selection methods applied to it. To avoid a large conditional probability table (cpt), we used a layering-divorcing technique and created a layered bayesian network model:

The first layer (green nodes) contains the target intention nodes that we aim at inferring. The second layer (orange and red nodes) contains either latent (orange nodes) or partially-observed (red nodes) nodes that represent external and internal factors that are highly influential on the formation of behavioral intentions. The third layer (purple nodes) contains observable network features. They serve two purposes: assisting in inferring the behavioral intentions, and serving as observed predictors for second layer's latent variables. We now elaborate on the features used in each layer.

### 1.1. Second-layer features

Values of second-layer features were obtained using our surveys. In order to simulate a real-world inference task (which only considers the public portion of online profiles), values of latent second-layer features were omitted from our test sets (treated as missing values); instead, we tried to infer them using publicly available network features.

Personality This variable represents five broad dimensions of personality obtained from the "Big Five" model of personality dimensions. The big five model distills personality into five traits: neuroticism, extraversion, agreeableness, conscientiousness, and openness to experience.

To measure the Big Five personality traits among survey participants we used a short version of the Big Five Inventory based on BFI-10 Rammstedt and John (2007).

Demographic attributes We considered the following demographic attributes: age, gender, ethnicity (and country of origin), marital status, occupation group, income (latent variable). Only a subset of those attributes was used in each model.

Situational variables Events that might trigger a certain behavioral intention. Those events include personal-life transitions, professional-life transitions, external events (such as a holiday or an election), etc. Priors were obtained for some intentions. For instance, life-transitions are shown to have an important impact on weight-loss intentions Brink and Ferguson (1998).

Emotions Different emotions may serve as either the cause of a behavioral intention or as its effect. Therefore, we went beyond the binary emotion-representation (positive-negative) and also considered fine-grained emotions. The most studied model of discrete emotions is the Ekman model Ekman (1992) which posits the existence of six basic emotions: anger, disgust, fear, joy, sadness and surprise. Since momentary emotion ratings are not particularly indicative of the behavioral intentions explored in this work, survey participants were presented with eight emotion categories (six basic emotions and two positive-negative emotion categories) and were asked to rate their feelings over the past week/month/three months in general.

Interest, Opinion Those variables represent the user's level of interest and opinion regarding topics related to a given intention.

![img-0.jpeg](img-0.jpeg)

Figure 1.: A diagram of our static intention-inference model

# 1.2. Network features 

The value of a network feature was included in our datasets only if it was part of the public portion of one of the user's social-network profiles.

Numeric features (NUMERIC) We considered statistics about the user's activity (number of posts, status updates, number of uploaded photos etc), reactions to the user's content (number of tagged photos, for instance) and the user's reactions to others' content. The latter measure was sparse, as both Facebook and Instagram limit the visibility of such reactions. We also considered basic statistics about the users' network, but we limit ourselves to statistics that are both publicly visible and can be directly extracted from the user's own social-network profile/s (number of friends, followers-following ratio, public-figures-non-public-figures following ratio, etc).

Raw Textual features (TEXT) Textual features were classified as either usergenerated (UG) features (including textual content that was written by the user), or non-user-generated (NUG) features (textual features that were not written by the user such as likes (Facebook) or hashtags (Instagram)). We limit ourselves to textual content that is both publicly visible and was either produced by the target user, or can be directly extracted from the user's own social-network profile/s. Raw textual features were not directly fed to our models. Instead, each textual feature was analyzed using various linguistic methods as described below; Textual-features-related-nodes in our network represent averaged discretized score or frequency of a given category of a given linguistic feature among the user's textual features. Such nodes represent the prevalence of a specific linguistic category among the entire set of raw textual features.

Miscellaneous features (MISC) Miscellaneous features include features that are neither numeric nor textual, such as the mere existence of various social-network accounts, visibility level/s that the user has chosen to apply to her social-network accounts, profile attributes from which demographic attributes can be extracted, etc. MISC features can be seen as social-network accounts' metadata rather than data itself (NUMERIC, TEXT).

# 1.3. Linguistic features 

We use a broad range of linguistic features, created based on our raw textual features.
Keyword-search (KWS-UG, KWS-NUG) For a given intention, or an event, $\mathcal{A}$, we manually identified the most prominent keywords related to $\mathcal{A}$. We then performed a keyword search on our textual features. For some textual features, items that were found to contain a relevant keyword were further processed using a second method, depending on the nature of $\mathcal{A}$ and the nature of the textual feature. This resulted in two groups of features, KWS-UG and KWC-NUG (keyword search applied to user-generated/non-user-generated content).

LIWC (LIWC-UG, LIWC-NUG) LIWC is a text analysis tool that is widely used in psychological studies Tausczik and Pennebaker (2010). Each list of words is associated with a semantic or syntactic category, such as negations, adverbs or tone. LIWC analysis was applied to UG and NUG textual features. However, with regards to NUG features, we only considered a small subset of LIWC categories, mostly concerning topics and sentiment.

Sentiment analysis, part-of-speech tagging (SA, PoS) These were only applied to KWS-UG (SA and PoS) and KWS-NUG (SA), i.e., items that were found to contain at least one relevant keyword. SA was applied to items that were found to contain keywords that relate to the behavioral intention to be inferred, in order to assess the user's opinion on related topics. The use of PoS tagging was more implicit; it was applied to items that were found to contain keywords that relate to events in order to assess whether an event is relevant to each inference task (use of first-person writing, tensed verbs etc).

Topic modeling (LDA-UG, LDA-NUG) Topics were extracted using Latent Dirichlet Allocation (LDA). Shorter features (such as likes) and longer features (such as posts) were considered separately using different parameters. As many likes only contain names (e.g brand names), we considered a like to be both the like's title as well as the category to which it belongs.

Emotions (NRC, LIWC) We automatically quantify emotions from our UG textual features using LIWC and NRC. NRC is a publicly available lexicon of words associated with different emotions, as well as general positive and negative sentiment Mohammad and Turney (2013). We assign a predicted emotion to each UG textual feature and then average across all users' features.

### 1.4. Intention-specific features

Weight-loss intentions: body image. Body image dissatisfaction is a catalyst for weightloss intentions, especially among women Markey and Markey (2005). The relationship between social-network use and body image is mediated through appearance comparison, which in turn can be inferred using various social-network features Kim and Chock (2015); Meier and Gray (2014).

Borrowing intentions: optimism and impulsivity. General impulsivity is linked to higher levels of borrowing Ottaviani and Vandone (2011). Optimists not only believe that they will be able to pay back their debts quicker, but are also less likely to be discouraged from applying due to fear of rejection. This phenomenon, referred to as "discouraged borrowing", may constitute a measure of financial self-efficacy Jappelli (1990).

Job-searching intentions: unemployment statistics and employment history. Employee perception of alternative employment opportunities is a crucial component in

turnover intention Mano-Negrin and Tzafrir (n.d.). We capture this measure using an observed variable which represents an industry-specific unemployment rate. In addition, we hypothesize that the user's employment history can be used to infer current intentions and introduce variables such as average length of time at a job and length of time at the current job which are inferred using network features. The resulting set of variables ("status") may constitute a measure of job-search self-efficacy.

Vaccination intentions: attitudes and habits. Many papers investigate the relation between anti-vaccination positions and other attitudes and habits. Using themes identified in previous work, we create a second keyword set that contains keywords related to attitudes and habits that are known to be strongly linked to anti-vaccination attitudes. This set is treated similarly to other keyword-based features.

Travel-purchase intentions: level of concern about COVID-19. One of the industries hardest hit by COVID-19 is the travel industry, both due to regulations and people's fear to put themselves at risk in crowded flights and hotels. Therefore, as our datasets were collected during the 2020 COVID-19 pandemic, level of concern about COVID-19 appears to be a key determinant of travel-purchase intentions, inferred using demographic and linguistic features.
