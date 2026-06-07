# UNIVERSITY of TASMANIA 

## University of Tasmania Open Access Repository

## Cover sheet

Title
Sequence classification restricted Boltzmann machines with gated units

Author
Son Tran, d'Avila Garcez, A, Weyde, T, Yin, J, Zhang, Q, Karunanithi, M

## Bibliographic citation

Tran, Son; d'Avila Garcez, A; Weyde, T; Yin, J; Zhang, Q; Karunanithi, M (2020). Sequence classification restricted Boltzmann machines with gated units. University Of Tasmania. Journal contribution.
https://figshare.utas.edu.au/articles/journal_contribution/Sequence_classification_restricted_Boltzmann_machin
Is published in: 10.1109/TNNLS.2019.2958103

## Copyright information

This version of work is made accessible in the repository with the permission of the copyright holder/s under the following,

## Licence.

Rights statement: © 2020 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.

If you believe that this work infringes copyright, please email details to: oa.repository@utas.edu.au

## Downloaded from University of Tasmania Open Access Repository

Please do not remove this coversheet as it contains citation and copyright information.

University of Tasmania Open Access Repository

Library and Cultural Collections
University of Tasmania
Private Bag 3
Hobart, TAS 7005 Australia
E oa.repository@utas.edu.au

# Sequence Classification Restricted Boltzmann Machines With Gated Units 

Son N. Tran ${ }^{\circledR}$, Artur d’Avila Garcez ${ }^{\circledR}$, Tillman Weyde, Jie Yin ${ }^{\circledR}$, Qing Zhang, and Mohan Karunanithi


#### Abstract

For the classification of sequential data, dynamic Bayesian networks and recurrent neural networks (RNNs) are the preferred models. While the former can explicitly model the temporal dependences between the variables, and the latter have the capability of learning representations. The recurrent temporal restricted Boltzmann machine (RTRBM) is a model that combines these two features. However, learning and inference in RTRBMs can be difficult because of the exponential nature of its gradient computations when maximizing log likelihoods. In this article, first, we address this intractability by optimizing a conditional rather than a joint probability distribution when performing sequence classification. This results in the "sequence classification restricted Boltzmann machine" (SCRBM). Second, we introduce gated SCRBMs (gSCRBMs), which use an information processing gate, as an integration of SCRBMs with long short-term memory (LSTM) models. In the experiments reported in this article, we evaluate the proposed models on optical character recognition, chunking, and multiresident activity recognition in smart homes. The experimental results show that gSCRBMs achieve the performance comparable to that of the state of the art in all three tasks. gSCRBMs require far fewer parameters in comparison with other recurrent networks with memory gates, in particular, LSTMs and gated recurrent units (GRUs).


Index Terms-Recurrent neural networks (RNNs), restricted Boltzmann machines, sequence classification, temporal learning.

## I. INTRODUCTION

MODELING sequences is an important research topic with a variety of applications, ranging from natural language processing [1], [2] to computer vision [3]. While some studies focus on predicting time-series events [4], [5], classification with sequential data also receives significant attention [6]-[8]. A sequence can be associated with one label for a full input sequence or with a sequence of labels, typically one for each element of the sequence. In [10] and [11], the terms conventional and strong are established, respectively,

[^0]for these classifications for tasks. In this article, for ease of presentation, we use the term sequence classification to refer to the strong case, i.e., the labeling of each element of the sequence. Solutions to this classification problem can enable a wide range of real-world applications. For example, speech recognition transcribes a sequence of acoustic feature vectors with spoken words, optical character recognition (OCR) converts images of handwritten or printed text into machineencoded text, and activity recognition predicts human actions from a sequence of sensor data.

The sequence classification problem has attracted research in dynamic Bayesian models, such as hidden Markov models (HMMs) [11] and conditional random fields (CRFs) [12]. An advantage of these models is the ability to learn the relationships between sequence labels, which is useful for temporal reasoning. However, recent research has seen an increasing interest in recurrent neural networks (RNNs) for sequence classification. Different from dynamic Bayesian models, most RNN models assume that the class labels in a sequence are independent, given the sequence inputs. This makes inference easier but sacrifices dynamic inference based on the temporal dependences between the sequence labels. A key advantage of RNNs is the ability to learn the temporal representations from data using recurrent hidden layers; however, they have a problem of vanishing/exploding gradients, especially when learning from long sequences using backpropagation through time [13]. This issue can be addressed by incorporating different memory gates in hidden layers, as shown in long short-term memory (LSTM) [13] and gated recurrent units (GRUs) [14]. There have been many attempts to combine the advantages of representation learning with dynamic inference. Most approaches integrate a dynamic Bayesian model and deep neural network [15], e.g., by placing a CRF on top of a bidirectional LSTM (bi-LSTM) [16]. Another approach is the recurrent temporal restricted Boltzmann machine (RTRBM), an extension of the restricted Boltzmann machine (RBM). The RTRBM is a generative graphical model that represents a distribution of sequences and has the ability to learn hidden features [5], [17]. However, learning and inference in RTRBMs are difficult because of the high complexity of computing a joint distribution.

## A. Contributions

As the first contribution of this article, we propose a novel and compact model based on RBMs, which we call sequence classification RBMs (SCRBM), to support representation learning and dynamic inference on the classification


[^0]:    Manuscript received July 30, 2018; revised March 26, 2019 and September 30, 2019; accepted December 1, 2019. (Corresponding author: Son N. Tran.)
    S. N. Tran is with the Discipline of Information and Communication Technology, University of Tasmania, Hobart, TAS 7005, Australia (e-mail: sn.tran@utas.edu.au).
    A. Garcez and T. Weyde are with the Department of Computer Science, City, University of London, London EC1V 0HB, U.K. (e-mail: a.garcez@city.ac.uk; t.e.weyde@city.ac.uk).
    J. Yin is with the Discipline of Business Analytics, The University of Sydney, Sydney, NSW 2006, Australia (e-mail: jie.yin@sydney.edu.au).
    Q. Zhang and M. Karunanithi are with the Australian E-Health Research Centre, CSIRO, Brisbane, QLD 4209, Australia (e-mail: qing.zhang@csiro.au; mohan.karunanithi@csiro.au).

    Color versions of one or more of the figures in this article are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TNNLS.2019.2958103

of sequences. The SCRBM is constructed by rolling RBMs with their class nodes over time. Each RBM at time $t$ has a layer of visible units $\left(X^{i}\right)$ and a layer of hidden units $\left(H^{i}\right)$. Together with class nodes $Y^{i}$ denoting the labels at time $t$, they form a model representing a distribution: $p\left(y^{1: T}, \mathbf{x}^{1: T}, \mathbf{h}^{1: T}\right)$. When it comes to inference, there are two questions to answer. First, in order to compute gradients, one needs to infer the hidden states, given the state of the input layer and the class labels from the distribution $p\left(H^{1: T} \mid \mathbf{x}^{1: T}, y^{1: T}\right)$. This can be done using variational methods, i.e., treating a hidden unit as a mean field, similar to [5]. Second, to predict the state of the class labels given the state of the input layer, in the best case, one can search for the most probable labels from the conditional distribution, i.e., solving $\arg \max _{Y^{1: T}} p\left(Y^{1: T} \mid \mathbf{x}^{1: T}\right)$. In this article, we show that this type of inference can be carried out efficiently by propagating the expectation of the prediction for the previous labels to compute the state of the hidden layer. In other words, the hidden state at time $t$ is dependent on the previous prediction (class labels at $t-1$ ), and thus, by association, the state of the class labels at any time point is dependent on the prediction of the labels at the previous time point. For learning, we maximize the log likelihood of the training data. It has been shown that learning a local RBM with labels is tractable [18], [19], but learning the entire sequence is not. This is because it is not easy to marginalize out hidden units in the sequential case, which can be done analytically in the case of a single discriminative RBM. Also, computation becomes expensive due to the exponential growth of possible assignments to the sequence of labels. To solve this problem, we use the abovementioned mean-field technique to factorize the conditional probability of a sequence into a product of probabilities of local discriminative RBMs.

One drawback of SCRBM is that it cannot capture longterm information and is prone to the problem of vanishing/ exploding gradient similar to RNNs [13]. Therefore, in the second contribution of this article, we improve the performance of SCRBM by proposing an idea to integrate SCRBM with LSTM through an information processing gate. This model is called gated SCRBM (gSCRBM). The idea is to take advantage of LSTM cells that use different types of memory gates to handle temporal information. In particular, besides the hidden state, an LSTM cell maintains a cell state to convey the information along the chain over time, while memory gates are used to decide which information should be added or removed from the cell state. In gSCRBM, the cell state is the same as in LSTMs and we integrate a memory gate layer into the hidden layer of the SCRBM. By doing this, we keep the information processing mechanism as it is in LSTMs while allowing probabilistic inference of the class layer as done in SCRBM.

In our experiments, we evaluate the SCRBM and gSCRBM models on three tasks: OCR, Conll 2000 chunking, and multiresident activity recognition in a smart home. The results show that gSCRBM outperforms the state of the art in all three tasks.

Despite having a simpler structure, SCRBM achieves the promising results in OCR and, notably, the highest accuracy for chunking. This motivated further empirical exploration to
compare SCRBM with RNNs, especially with ones having complex memory gates such as GRUs [14] and LSTMs [13]. The results show that the performance of the SCRBM, in some cases, is comparable to that of GRUs and LSTMs, even though SCRBM is considerably more compact, requiring far fewer parameters. The source code for the proposed models can be found at https://github.com/sontranai/scrbm/.

The remainder of this article is organized as follows. In Section II, we discuss the related literature. Section III presents the SCRBM model. In Section IV, we propose the integration of LSTM gating techniques into the SCRBM, leading to the gSCRBM. Section V describes the empirical evaluation of the proposed models. Section VI concludes this article and discusses the future work.

## II. Related Work

A recent work on dynamic Bayesian models has focused on improving the learning of CRFs by using gradient boosting techniques, such as second-order gradient boosting [8] and gradient tree boosting [20]. In order to incorporate representation learning into CRFs, Do and Artieres [15] proposed neural CRF, which extends CRFs by using neural networks to represent energy functions. On the side of neural networks, LSTMs have been the dominant approach as they can mitigate the problem of vanishing gradients. Other variants of gated neural network are also used in a wide range of sequence classification problems, which can be categorized into architecture variants and cell variants [21]. In terms of network architectures, bi-LSTM where two LSTMs are coupled together, one for forward inference and another for backward inference, has been successful in language processing [22]. In [16], a CRF is placed on top of a bi-LSTM, in which the lower part is used for representation learning and the upper part is used for dynamic inference. In terms of cells, GRU [14] is another variant of gated RNNs, which reduces the complexity compared to LSTMs by combining input and forget gates and sharing values between the cell state and hidden states. Another variant of LSTM is peephole LSTM where cell states are added to the gates [23].

Besides the Bayesian and neural approaches discussed earlier for sequence classification, modeling sequence data with RBMs has been studied previously [4], [5]. However, as generative models, they are not easy to apply to classification tasks. The key problem is that the exact gradient cannot be computed analytically so that approximation algorithms have to be used. By contrast, SCRBM is a discriminative model whose log likelihood is tractable, building on the work on discriminative RBMs. In addition to tractability, another motivation for having a discriminatively learned variant of RTRBMs is the desire for better classification performance. It has been shown in [24] that with sufficient training examples, discriminative learning tends to do better on the task it is optimized for than its generative counterpart model. This has been confirmed by the empirical results of classRBM on nonsequential data [18]. Differently from that work, SCRBM as proposed here is designed for classification with sequence data. Graphically, an SCRBM can be seen as a classRBM with recurrent connections between hidden units, similar to

the relation between RNNs and feedforward neural networks. However, the design of the SCRBM is less straightforward as we have to solve the issue of intractability, as detailed in Section III.

In recent work, the recurrent temporal discriminative RBM (RTD-RBM) has been proposed [25]. It is a generalized version of the RTRBM tailored for discriminative inference. In the SCRBM, we use a similar approach to the RTD-RBM but with a different architecture and a broad evaluation (the RTD-RBM was only evaluated on melody prediction). Also, RTD-RBMs require more parameters than SCRBMs because RTD-RBMs generalize RTRBMs by including connections from the previous hidden layers to the current class labels. Another related model is the dynamic Boltzmann machine [26] that supports online learning for sequence prediction, mainly applied to regression. Combining LSTM and RTRBM has been studied in [27], but for generation rather than classification.

## III. SCRBM

## A. Model

An SCRBM is constructed by rolling RBMs with class labels over time. The model defines a probability distribution

$$
p\left(y^{1: T}, \mathbf{x}^{1: T}, \mathbf{h}^{1: T}\right)=\prod_{t=1}^{T} p\left(y^{t}, \mathbf{x}^{t}, \mathbf{h}^{t} \mid \mathbf{h}^{t-1}\right)
$$

where $\mathbf{x}^{1: T}, \mathbf{h}^{1: T}$ are time series of the visible and hidden states, $y^{1: T}$ is the class-label sequence, and $\mathbf{h}^{0}$ are the biases of the hidden units.

The main problem of this model, as highlighted in [4], is that inference is intractable. This, however, can be solved by adding recurrent connections, as done for the RTRBM [5]. In RTRBM, class labels are not included. In SCRBMs, the local distribution at time $t, p\left(y^{t}, \mathbf{x}^{t}, \mathbf{h}^{t} \mid \mathbf{h}^{t-1}\right)$, is replaced by

$$
p\left(y^{t}, \mathbf{x}^{t}, \mathbf{h}^{t} \mid \hat{\mathbf{h}}^{t-1}\right)=\frac{\exp \left(-E_{\theta}\left(y^{t}, \mathbf{x}^{t}, \mathbf{h}^{t} ; \hat{\mathbf{h}}^{t-1}\right)\right.}{\sum_{y^{\prime}, \mathbf{x}^{\prime}, \mathbf{h}^{\prime}} \exp \left(-E_{\theta}\left(y^{t}, \mathbf{x}^{t}, \mathbf{h}^{t} ; \hat{\mathbf{h}}^{t-1}\right)\right.}
$$

where $\hat{\mathbf{h}}^{t-1}$ is the vector of expected values of the hidden units at $t-1$

$$
\hat{\mathbf{h}}^{t-1}=\mathbb{E}\left\{\mathbf{H}^{t-1} \mid \mathbf{x}^{1: t-1}, y^{1: t-1}\right\}
$$

with the local energy function

$$
\begin{aligned}
E_{\theta}\left(y^{t}, \mathbf{x}^{t}, \mathbf{h}^{t} ; \hat{\mathbf{h}}^{t-1}\right)=-\left[\left(\mathbf{x}^{t}\right)^{\top} \mathbf{W}_{x h}\right. & \left.+\mathbf{u}_{y^{t}}^{\top}+\left(\hat{\mathbf{h}}^{t-1}\right)^{\top} \mathbf{W}_{h h}\right] \mathbf{h}^{t} \\
& -\mathbf{a}^{\top} \mathbf{x}^{t}-b_{y^{t}}-\mathbf{c}^{\top} \mathbf{h}^{t}
\end{aligned}
$$

which is characterized by the parameters: $\theta=\left\{\mathbf{W}_{x h}, \mathbf{W}_{h h}\right.$, $\mathbf{U}, \mathbf{a}, \mathbf{b}, \mathbf{c}\}$. The local energy function (4) is an extension of the standard notation of the energy function of RBMs [28]. The total energy of an SCRBM is the sum of all local energy functions from time 1 to $T$. It represents the correlation between the hidden units and the external units (input, labels, and previous hidden) with weight matrices applied, and it is also used to compute a probability distribution, as shown in (2). Here, $\mathbf{W}_{x h}$ is the weight matrix between visible units
![img-0.jpeg](img-0.jpeg)

Fig. 1. Graphical representation of (a) RNN cell and (b) SCRBM cell. The green arrows indicate the directed connections from the previous hidden nodes; the red and blue arrows (resp. lines) indicate the directed (resp. undirected) connections from current labels and inputs, respectively.
and hidden units; $\mathbf{W}_{h h}$ is the recurrent/temporal connection weight matrix of the hidden units; $\mathbf{U}$ is the weight matrix between the class units (represented by one-hot vectors) and the hidden units; $\mathbf{a}, \mathbf{b}$, and $\mathbf{c}$ are the biases of the visible units, hidden units, and class units, respectively; and $\mathbf{u}_{y^{t}}$ is the column vector $y^{t}$ of $\mathbf{U}$ which is the result of the multiplication of $\mathbf{U}$ and the one-hot vector for $y^{t}$.

The set of parameters in (4) can be reduced by omitting the biases of the visible units because it will be canceled out in the conditional distribution calculation. Fig. 1(a) and (b) shows the resulting structure of the SCRBM. It has the same set of parameters as an RNN. However, the SCRBM is very different in terms of its formulation as defined earlier and in terms of inference and learning, as given described in Sections III-B and III-C.

Different from the generative distribution [see (1)], the conditional distribution is tractable. It offers a computational advantage at inference and learning, where sampling is not needed, as shown in Sections III-B and III-C. In a nutshell, with the earlier realization, SCRBM is a tractable RTRBM for sequence classification.

## B. Inference

As mentioned earlier, inference for units in the hidden layer given the inputs and labels is easy, as in [5], where each hidden unit can be treated as a mean field as follows:

$$
\hat{\mathbf{h}}^{t}=\sigma\left(\mathbf{W}_{x h}^{\top} \mathbf{x}^{t}+\mathbf{u}_{y^{t}}+\mathbf{W}_{h h}^{\top} \mathbf{h}^{t-1}+\mathbf{c}^{t}\right)
$$

For classification with the SCRBM, one would like to search for the most probable assignment of $Y^{1: T}$ given the inputs $x^{1: T}$. In this article, we show that SCRBM can efficiently infer the state of the hidden layer while performing prediction. As discussed earlier, once the class labels at $\mathrm{t}-1$ are known, it is straightforward to infer the state of the hidden layer. We now show that the inference of class labels is also easy, given the state of the hidden layer. In particular, from the mean-field values of the hidden layer in the previous time step, we can infer the class labels using the following conditional distribution:

$$
p\left(y^{t} \mid \mathbf{x}^{t}, \hat{\mathbf{h}}^{t-1}\right)=\frac{\exp \left(-\mathcal{F}\left(\mathbf{x}^{t}, y^{t}, \hat{\mathbf{h}}^{t-1}\right)\right)}{\sum_{y^{\prime}} \exp \left(-\mathcal{F}\left(\mathbf{x}^{t}, y^{\prime}, \hat{\mathbf{h}}^{t-1}\right)\right)}
$$

with free energy

$$
\mathcal{F}\left(\mathbf{x}^{t}, y, \hat{\mathbf{h}}^{t}\right)=-b_{y}-\sum_{j} \log \left(1+\exp \left(\mathbf{w}_{x h, j}^{\top} \mathbf{x}^{t}+u_{y j}+c_{j}\right)\right)
$$

Algorithm 1 Inference With SCRBM
Data: Input: $\mathbf{x}^{1: T}$
Result: Output: $\mathbf{y}^{1: T}$
for $t=1: T$ do
set $\hat{\mathbf{y}}^{t}=p\left(\mathbf{y}^{t} \mid \mathbf{x}^{t}, \hat{\mathbf{h}}^{t-1}\right)$
set $y^{t}=\arg \max _{\hat{\mathbf{x}}} \hat{y}_{\hat{\mathbf{x}}}^{t}$
set $\hat{\mathbf{h}}^{t}=\sigma\left(\mathbf{W}_{x h} \mathbf{x}^{t}+\mathbf{U} \hat{\mathbf{y}}^{t}+\mathbf{W}_{h h} \mathbf{h}^{t-1}+\mathbf{c}^{t}\right)$
end
where $\mathbf{w}_{x h, j}$ is the $j$ th column of the weight matrix $\mathbf{W}_{x h}$ between the hidden units and the units of the visible layer corresponding to the inputs, and $u_{y j}$ is an element of the weight matrix $U$ between the hidden units and the units Y corresponding to the class labels. Here, the visible biases a have been canceled out, which makes the number of parameters equivalent to that of a standard RNN with the same number of hidden units, i.e., $\theta=\left\{\mathbf{W}_{x h}, \mathbf{W}_{h h}, \mathbf{U}, \mathbf{b}, \mathbf{c}\right\}$.

As opposed to the joint distribution in (2), the conditional distribution (6) is tractable, i.e., it can be computed analytically. The difference lies in the denominators of the two distributions: $\sum_{y^{\prime}, \mathbf{x}^{\prime}, \mathbf{h}^{\prime}} \exp \left(-E_{\theta}\left(y^{\prime}, \mathbf{x}^{\prime}, \mathbf{h}^{\prime} ; \hat{\mathbf{h}}^{t-1}\right)\right)$ of the joint distribution and $\sum_{y^{\prime}} \exp \left(-\mathcal{F}\left(\mathbf{x}^{t}, y^{\prime}, \hat{\mathbf{h}}^{t-1}\right)\right)$ of the conditional distribution. While the joint distribution sums over all possible values of the input, label, and hidden states, the conditional distribution only needs to perform a summation over all possible values of labels, which is much more feasible. This also helps to simplify the learning with SCRBM as we will show in Section III-C.

From (6), we can predict the value of the class labels. Once $\mathbf{y}^{t}$ is known, we use it to infer the mean-field values $\hat{\mathbf{h}}^{t}$ as in (5). Let us put this in a specific context, starting from $t=1$, the conditional distribution $p\left(y^{1} \mid \mathbf{x}^{1}, \hat{\mathbf{h}}^{0}\right)$ can be computed exactly by marginalizing out the hidden variable $\mathbf{h}^{1}$ while having $\hat{\mathbf{h}}^{0}$ as parameters. In order to calculate the values of the current step from the prediction of the previous step, we do not use its predicted value of $y^{1}$, instead we use the distribution to infer the mean-field value $\hat{\mathbf{h}}^{1}$. This value is then passed to the next prediction step and so on. The details of the SCRBM inference algorithm are given in Algorithm 1.

From Algorithm 1, we can see that SCRBMs can capture the dependences between class variables over time through the inference of hidden units using the expected values of the class units.

## C. Learning

In SCRBMs, we are interested in learning the conditional distribution

$$
p\left(y^{1: T} \mid \mathbf{x}^{1: T}\right)=\frac{p\left(\mathbf{x}^{1: T}, y^{1: T}\right)}{\sum_{y^{\prime \prime}: T} p\left(\mathbf{x}^{1: T}, y^{\prime 1: T}\right)}
$$

However, it is difficult to marginalize out all hidden variables $\mathbf{h}^{1: T}$ to compute this distribution exactly. The complexity of learning our model would increase exponentially with the length of the sequence, due to the need to sum over all possible combinations of classes at every time step. Thus, instead of computing the distribution directly, we simplify it
by marginalizing out the hidden variable at each time $t$ using the expectation of the hidden state at the previous time $t-1$. Let us consider

$$
\begin{aligned}
p\left(\mathbf{x}^{1: T}, y^{1: T}\right) & =\sum_{\mathbf{h}^{1: T}} p\left(y^{1: T}, \mathbf{x}^{1: T}, \mathbf{h}^{1: T}\right) \\
& =\sum_{\mathbf{h}^{1: T}} \prod_{t=1}^{T} p\left(y^{t}, \mathbf{x}^{t}, \mathbf{h}^{t} \mid \mathbf{h}^{t-1}\right)
\end{aligned}
$$

If we first compute the expectation of $\mathbf{h}^{t-1}$ given the previous input states $\mathbf{x}^{1: t-1}$ and $y^{1: t-1}$, which is equivalent to minimizing the total energy function of the SCRBM, then we have

$$
q\left(\mathbf{x}^{1: T}, y^{1: T}\right)=\prod_{t=1}^{T} p\left(y^{t}, \mathbf{x}^{t} \mid \hat{\mathbf{h}}^{t-1}\right)
$$

One can view this as an expectation step to be followed by an optimization step, which maximizes the log likelihood of this simplified distribution

$$
\begin{aligned}
q\left(y^{1: T} \mid \mathbf{x}^{1: T}\right) & =\frac{\prod_{t=1}^{T} p\left(y^{t}, \mathbf{x}^{t} \mid \hat{\mathbf{h}}^{t-1}\right)}{\sum_{y^{\prime \prime}: T} \prod_{t=1}^{T} p\left(y^{\prime \prime}, \mathbf{x}^{t} \mid \hat{\mathbf{h}}^{t-1}\right)} \\
& =\frac{\prod_{t=1}^{T} p\left(y^{t}, \mathbf{x}^{t} \mid \hat{\mathbf{h}}^{t-1}\right)}{\prod_{t=1}^{T} \sum_{y^{\prime \prime}} p\left(y^{\prime \prime}, \mathbf{x}^{t} \mid \hat{\mathbf{h}}^{t-1}\right)} \\
& =\prod_{t=1}^{T} p\left(y^{t} \mid \mathbf{x}^{t}, \hat{\mathbf{h}}^{t-1}\right)
\end{aligned}
$$

Since $p\left(y^{t} \mid \mathbf{x}^{t}, \hat{\mathbf{h}}^{t-1}\right)$ is tractable as shown in (6), we can compute the above-mentioned distribution exactly. Now, one can learn the model by maximizing the log-likelihood function

$$
\ell=\sum_{y^{1: T}, \mathbf{x}^{1: T}} \sum_{t=1}^{T} \log p\left(y^{t} \mid \mathbf{x}^{t}, \hat{\mathbf{h}}^{t-1}\right)
$$

Similar to other time-series connectionist models, such as standard RNNs and RTRBMs, we train the model using backpropagation through time. The update of the model's set of parameters, denoted by $\theta$, is shown in the following:

$$
\nabla \theta=\sum_{t=1}^{T}\left(\frac{\partial_{\theta} \log p\left(y^{t} \mid \mathbf{x}^{t}, \hat{\mathbf{h}}^{t-1}\right)}{\partial \theta}+\frac{\partial_{\theta} \hat{\mathbf{h}}^{t}}{\partial \theta} \mathcal{O}^{t}\right)
$$

where $\left(\partial_{\theta} \hat{\mathbf{h}}^{t}\right) / \partial \theta=\left(\partial_{\theta} \sigma\left(\mathbf{W}_{x h}^{\top} \mathbf{x}^{t}+\mathbf{u}_{y^{t}}+\mathbf{W}_{h h}^{\top} \mathbf{h}^{t-1}+\mathbf{c}^{t}\right)\right) / \partial \theta$ and $\left(\partial_{\theta} \log p\left(y^{t} \mid \mathbf{x}^{t}, \hat{\mathbf{h}}^{t-1}\right)\right) / \partial \theta$ are local derivatives, and $\hat{\mathbf{h}}^{t-1}$ is a value, not a function of $\theta$; and for mathematical convenience

$$
\mathcal{O}^{t}=W_{h h}^{\top} \hat{\mathbf{h}}^{t+1}\left(1-\hat{\mathbf{h}}^{t+1}\right) \mathcal{O}^{t+1}+\frac{\partial \log p\left(y^{t+1} \mid \mathbf{x}^{t+1}, \hat{\mathbf{h}}^{t}\right)}{\partial \hat{\mathbf{h}}^{t}}
$$

## IV. GSCRBMs

Section III showed how SCRBMs are constructed, learned, and used for the classification of sequences. However, similar to RNNs, SCRBMs are not able to model long-term dependences and are prone to the problem of vanishing/exploding gradients [13]. In order to address these points, in this section, we show how to integrate memory gates such as

![img-1.jpeg](img-1.jpeg)

Fig. 2. (a) LSTM cell. (b) SCRBM cell with gated output.

in LSTM with SCRBMs, which results in the gSCRBM. A graphical representation of hidden layers in gSCRBM is shown in Fig. 2(b). It is similar to the LSTM in Fig. 2(a), except that we take one memory gate (the output gate in this case) and integrate it into the SCRBM.

The information processing in gSCRBM operates as follows:

$$
\begin{aligned}
\mathbf{i} &= \mathbf{W}_{si}\mathbf{x} + \mathbf{W}_{hi}\mathbf{h}^{t-1} + \mathbf{b}_i \\
\mathbf{f} &= \mathbf{W}_{sf}\mathbf{x} + \mathbf{W}_{hf}\mathbf{h}^{t-1} + \mathbf{b}_f \\
\mathbf{o} &= \mathbf{W}_{so}\mathbf{x} + \mathbf{W}_{ho}\mathbf{h}^{t-1} + \mathbf{b}_o \\
\mathbf{\epsilon} &= \mathbf{W}_{ss}\mathbf{x} + \mathbf{W}_{ho}\mathbf{h}^{t-1} + \mathbf{b}_o \\
\hat{\mathbf{v}} &= \frac{\exp(b_k)}{\sum_{k'}\exp(b_k')\prod_{j}(1+\exp(o_{j''} + u_{k''})} \\
y &= \underset{k}{\exp(b_k)} \\
\hat{\mathbf{o}} &= \mathbf{o} + \mathbf{U}\hat{\mathbf{v}} \\
\mathbf{c} &= \sigma(\mathbf{f}) \ast \mathbf{c}^{t-1} + \sigma(\mathbf{i}) \ast \mathbf{\epsilon} \\
\mathbf{h} &= \sigma(\hat{\mathbf{o}}) \ast \tanh(\mathbf{c})
\end{aligned}
$$

The computations of the input gate, forget gate, output gate, and $\hat{c}$, which can be seen in (15)–(18), respectively, are similar to the LSTM. In order to integrate the output gate into the SCRBM, we add a mean-field unit ($\hat{\mathbf{o}}$) for that gate, similar to the approach in Section III-A. The same can be done for other gates in LSTMs; however, in our experiments, we found that a gSCRBM with input gate only (denoted as gSCRMi) and a gSCRBM with output gate only (denoted as gSCRMo) perform better than gSCRBMs with more gates. This indicates that the input and output gates contain the most predictive information.

For the input gate, we replace (19) and (21)–(23) by the following equations, respectively:

$$
\begin{aligned}
\hat{\mathbf{v}} &= \frac{\exp(b_k)}{\sum_{k'}\exp(b_{k'})}\prod_{j} \left( 1 + \exp(ij + u_{kj}) \right) \\
\hat{\mathbf{i}} &= \mathbf{i} + \mathbf{U}\hat{\mathbf{v}} \\
\mathbf{c} &= \sigma(\mathbf{f}) \ast \mathbf{c}^{t-1} + \sigma(\hat{\mathbf{i}}) \ast \mathbf{\epsilon} \\
\mathbf{h} &= \sigma(\mathbf{o}) \ast \tanh(\mathbf{c})
\end{aligned}
$$

In this case, the cell state is updated with the probability estimation of labels though input gate, as shown in (26).

## V. EXPERIMENTS

### A. OCR

1) **Data Set**: The MIT OCR data set[^1] is a widely used benchmark for evaluating sequence classification algorithms [29]. We use two popular partitions from [7] and from [9] and [16]. In the former, called here "ms" for model selection, the data are partitioned into ten groups, each consisting of training, validation, and test sets. We select the models based on the performance on the validation set and report their average accuracy on the test sets. In the latter, here called "cv" for cross validation, the data are divided into ten folds without validation sets for model selection.

2) **Evaluation Method**: Each model is expected to predict the correct label corresponding to the image of a character as it is drawn. All the models are evaluated using the average classification accuracy per sequence $E(y, y^*)$, where $y$ and $y^*$ are the predicted and the true sequence sets, respectively, as follows:

$$
E(y, y^*) = \frac{1}{N} \sum_{i=1}^{N} \left[ \frac{1}{L_i} \sum_{j=1}^{L_i} \mathcal{I}((y_i)_j \neq (y_i^*)_j) \right] \tag{28}
$$

where $N$ is the total number of test examples, $L_i$ is the length of the $i$th sequence, and $\mathcal{I}$ is the $0 - 1$ indicator function.

3) **Model Comparison**: We compare the performance of SCRBM on the above-mentioned sequence labeling task with the following models: multiclass support vector machines (SVM_multiclass) [30], structured support vector machines (SVM_struct) [31], max-margin Markov network (M3N) [29], averaged perceptron [32], search-based structured prediction (SEARN) [33], CRF [12], [34], HMM [11], LogitBoost [35], TreeCRF [20], RTDRBM [25] (using the inference algorithm proposed in this article to adapt to the sequence labeling task), and state-of-the-art models:

1) **Structured Learning Ensemble (SLE) [7]**: An optimized ensemble of 7 models: SVM_multiclass, SVM_struct, M3N, Perceptron, SEARN, CRF, and HMM.

2) **Neural CRF [15]**: A combination of CRF and deep networks.

3) **Gradient Boosting CRF (GBCRF) [8]**: CRF trained by a gradient boosting algorithm.

4) **Results**: For the "ms" partitioning, a grid search was carried out to determine the best model. We report the best results of the methods evaluated in [7]. For the SCRBMs, RTDRBM, and RNNs, the optimized hyperparameters include the learning rate and the number of hidden units. The traditional RNNs employ tanh as the activation function for the hidden units. We also use early stopping, with the performance of the models on the validation set being determined after each epoch. The training was stopped if the validation performance does not improve in ten consecutive epochs. The models have been trained using the Adam algorithm [36]. For the "cv" partition, since the model selection is not possible, we run each model using a different number of hidden units from {50, 100, 500, 1000, 2000, 5000, 10000} and report the lowest average test error rate for the models. The training method is Adam starting at the learning rate of 0.001. In the "ms" partition, this hyperparameter value was found to be an optimal choice for all connectionist models: RNN, GRU, LSTM, SCRBM, and gSCRBM. The number of training epochs is fixed to 30.

Table I shows the individual results. gSCRBMo outperforms all the other models. It is worth noting that the performance

[^1]: http://www.seas.upenn.edu/~taskar/ocr/

TABLE I
Averaged Test Set Error Rates (\%) of Various Models on the MIT OCR Sequence Labeling Task


of our model is considerably better than that of SLE, neural CRF, and GBCRF, which are the state of the arts to this OCR task.

## B. Chunking

The CoNLL 2000 shared task ${ }^{2}$ is a benchmark data set for sequence classification with a focus on chunking. The task is to classify the words in sentences into syntactic parts, e.g., noun phrase (NP) or verb phrase (VP). The data set consists of 8936 and 2012 sentences for training and testing, respectively. We use the binary features from [37] for these data. In this experiment, we use the 50000 most common features from the training set. The motivation behind the selection of this type of features is that it can help RNNs to achieve better performance than the Glove. 6 B or word2vec features. Although the word2vec features are smaller in terms of size, generic approaches, such as RNN, GRU, and LSTM, do not perform well, and therefore, more complex variants, i.e., biLSTM [38], bi-LSTM-CRF [16], and CNN-biLSTMCRF [39], are needed.

Since the data set only includes training and testing samples, we do not perform model selection and early stopping. Instead, we tested different numbers of hidden units [50,100,500,1000] and report the best results on the test set. These values are chosen based on the computational capacity of the machines used for this experiment as a higher number of hidden units would have resulted in computational overload. We use again Adam to take the advantage of the sparsity of the features, the initial learning rate for it is 0.001 as this setting worked very well in the case of OCR mentioned earlier, and also in many other cases from our experience. For evaluation, we use F1 score: $F 1=2($ precision $*$ recall $) /($ precision + recall $)$. The results of the experiments as well as the state-of-theart results reported in [17] and [41]-[44] are shown in Table II.

[^0]TABLE II
F1 Scores for the CoNLL 2000 Chunking Task. Again, the SCRbm


## C. Activity Recognition in Smart Homes

In this experiment, we evaluate our models on activity recognition in smart homes. We use the CASAS data ${ }^{3}$, which is available from Washington State University and contains data from the smart department testbed with two residents where each resident performing 15 unique activities. The data were collected over 26 days in a smart home equipped with 37 ambient sensors. The data in CASAS are presented in "Date Time Sensor_ID Value Resident_ID Activity" format. For example, "2008-11-10 14:28:17.986759 M22 ON 22" shows that resident 2 is hanging up clothes at 14:28:17.986759 on 2008-11-10 when motion sensor M22 is triggered. Similarly, "2008-11-10 14:38:47.974299 M13 OFF 2819 " means at 14:38:47.974299 on 2008-11-10 when motion sensor M13 is off, and resident 1 is setting the dining room table for dinner, while resident 2 is setting out ingredients for dinner in the kitchen. Different from the previous tasks on OCR and chunking, activity recognition in smart homes is very challenging because of the following reasons. First, the sequences in the data set are considerably long as each of them has been recorded in several hours each day. The minimum length of the sequences is 500 and the maximum length is 866 . Second, data collection and annotation are difficult, which results in a small number of samples for training.

We partition the CASAS data into 24 days for training, 1 day for validation, and 1 day for testing. The competitors to our models are the state of the arts used for multiresident activity recognition in smart homes, including factorial HMM [44] and factorial CRF [37], [45]. We also compare with different types of RNNs, denoted as mRNNs, mGRUs, and mLSTMs, which have multiple outputs representing activities of different residents. Since, in this article, we design our models for single output, we combine the activities of multiple residents to a single label. We performed the model selection by using grid search on the number of hidden units and learning rate, similar to the previous experiments on "ms" partition of OCR. For completeness, we carry out a comparison with HMMs, CRFs, RNNs, GRUs, and LSTMs on the same combined labels.

In Tabel III, we show the performance for activities of two residents in the smart house. Each model is tested 20 times and

[^1]
[^0]:    ${ }^{2}$ https://www.clips.uantwerpen.be/conll2000/chunking/

[^1]:    ${ }^{3}$ http://ailab.eecs.wsu.edu/casas/

TABLE III Prediction Accuracy for All Models on CASAS Data Set. $\mathrm{R}_{1}$, $\mathrm{R}_{2}$, and $\mathrm{R}_{\text {all }}$ are the Accuracy of Predicted Activities of RESIDENT I, RESIDENT 2, AND THE JOINT ACTIVITIES


the averaged prediction accuracy is reported. The performance of a model is measured by the accuracy of each resident's activities and the accuracy of all residents' activities. The former is computed as

$$ \mathrm{R}*{m}=\frac{1}{\left|D*{t e s t}\right|} \sum_{a^{m, 1: T} \in \mathcal{D}*{t e s t}} \frac{1}{T} \sum*{t}\left(a^{m, t}==\hat{a}^{m, t}\right) $$

where $a^{m, t}$ and $\hat{a}^{m, t}$ are the ground truth and the predicted activity of resident $m$ at time $t$, respectively; $a^{m, t}==\hat{a}^{m, t}$ is 1 if the activity of resident $m$ at time $t$ is predicted correctly; otherwise, it is 0 . Similarly, the accuracy for activities of all residents is

$$ \mathrm{R}*{\text {all }}=\frac{1}{\left|D*{t e s t}\right|} \sum_{\mathbf{a}^{1: T} \in \mathcal{D}*{t e s t}} \frac{1}{T} \sum*{t}\left(\bigwedge_{m}\left(a^{m, t}==\hat{a}^{m, t}\right)\right) $$

where $\bigwedge_{m}$ is the Boolean AND operator and $\mathbf{a}^{1: T} \in \mathcal{D}_{\text {test }}$ is the activities of all residents in the test set.

The results show that by using memory gates, performance of predicting both residents' activities can be improved significantly, e.g., from $58.38 \%$ with mRNN to $83.10 \%$ and $83.23 \%$ with mGRU and mLSTM, respectively, and from $71.73 \%$ with RNN to $81.25 \%$ and $85.55 \%$ with GRU and LSTM, respectively. This is because the lengths of the data sequences are substantial, which bolsters the need for memory gates, while the consistency in daily activities of the residents is high enough to largely reduce the risk of having overfitting. It is shown that SCRBM with input gating achieved the highest performance, better than the other models. In the case of resident 1, multitask GRU has a similar performance with gSCRBM $_{i}$ but achieved lower accuracy for resident 2 and for joint activities. Note that in the smart house, it is very important to predict exact activities of all residents at a time to understand their collaborative and interactive behaviors.

## D. SCRBM Versus GRU and LSTM

As shown in the experiments mentioned earlier, SCRBM has achieved promising empirical results in the OCR and chunking tasks, despite its lack of complex memory gates. This motivates a further investigation into this model in comparison

TABLE IV Averaged Test Set Errors of RNNs With Tanh Units, GRU, LSTM, AND SCRBM ON THE TAGGING DATA SET


with popular variants of RNNs such as gated recurrent units and LSTM, which use complex memory gates in their hidden units, and with a standard RNN using tanh hidden units. It is worth noting that for a visible layer with $M$ units and a hidden layer with $N$ units, the number of weights in the RNN and SCRBM is the same, while GRUs and LSTMs will have, respectively, $2 N(M+N+1)$ and $3 N(M+N+1)$ more weights than the RNN and SCRBM. In general, if the number of labels is small, then the SCRBM will be approximately three times more compact than the GRU and four times more compact than the LSTM.

First, we evaluate the SCRBM, RNN, GRU, and LSTM on the POS tagging data set from Penn Treebank ${ }^{4}$. The data are partitioned into different training sets with 500, 1000, 2000, 4000, and 2000 examples. Models are selected by holding out $10 \%$ of the examples and are then evaluated on a test set with some 1600 sentences. The challenge here is that the lexical features are very large, approximately 450000 . Table IV shows the results where we can see that SCRBM performs competitively in comparison to GRU and LSTM. In particular, SCRBM is better than RNN in all five cases, better than GRU in two cases, and better than LSTM in three cases.

Second, we evaluate the effectiveness of SCRBM, RNN, GRU, and LSTM when they have the same number of parameters: 100 hidden units for both SCRBM and RNN, 33 hidden units for GRU, and 25 hidden units for LSTM. For completeness, we also include in the graphs in the following, GRU and LSTMs with 100 hidden units each. We evaluate the models on the OCR and POS tagging with 2000 training sentences and Conll2000 chunking. Since the original chunking data do not provide a validation set, we used $2.5 \%$ of their training data for training and the rest for validation. The original test set was used for testing as provided. In this experiment, for efficiency, we only use three chunking labels as in [37]. The evaluation metrics are the predictive error rate (as before) and the average negative log likelihood on the validation and test sets. All models are trained using Adam with an initial learning rate of 0.001 which, as we found, is generally good for all the models on all three data sets. Figs. 3 and 4 show that SCRBM generalizes better than RNNs, GRU, and LSTM with the same size or number of hidden units. Figs. 3(b.1), (b.2), (c.1), and (c.2) show that in the POS tagging and chunking data sets, all models achieve their best performances very quickly after only a few epochs, with the SCRBM achieving at that point the lowest test set error. Fig. 3(a.1) shows that in the OCR data set, SCRBM performs similar to the LSTM with the same number of 100 hidden units. As for the average negative log likelihood, one can

[^0] [^0]: ${ }^{4}$ http://www.cis.upenn.edu/treebank

![img-2.jpeg](img-2.jpeg)

Fig. 3. x-axis: number of epochs. y-axis: predictive errors. All models achieve their best performance very quickly after only a few epochs, with the SCRBM achieving at that point the lowest test set error, except for the OCR data set where the LSTM with 100 hidden neurons is slightly better. (a.1) OCR train. (b.1) POS train. (c.1) Chunking train. (a.1) OCR validation. (b.1) POS 2000 validation. (c.1) Chunking validation. (a.2) OCR test. (b.2) POS 2000 test. (c.2) Chunking test.

![img-3.jpeg](img-3.jpeg)

Fig. 4. x-axis: number of epochs. y-axis: average negative log likelihood. SCRBM achieves the lowest negative log likelihoods on validation and test sets. (a.1) OCR train. (b.1) POS train. (c.1) Chunking train. (a.1) OCR validation. (b.1) POS 2000 validation. (c.1) Chunking validation. (a.2) OCR test. (b.2) POS 2000 test. (c.2) Chunking test.

see in Figs. 4(a.1), (a.2), (b.1), (b.2), (c.1), and (c.2) that the SCRBM generalizes better than the other models as it achieves the lowest negative log likelihoods on the validation and test sets. This, along with Table IV, explains why in some cases GRUs and LSTMs may be better but only when they have more hidden units.

### *E. SCRBM Versus BiLSTM and Stacked-LSTM*

In the previous experiments, we compare our SCRBM cell with different types of cells, including traditional RNN cell,

#### TABLE V

GSCRBM_{i} VERSUS BiLSTM AND STACKEDLSTM


GRU cell, and LSTM cell. We also carried out an experiment on LSTM peephole cell on ORC and Chunking data sets, which achieved lower results than our gSCRBM.

In this section, we compare the performance of SCRBM/gSCRBM with advanced LSTM structures [21]. In particular, we choose Bidirectional LSTM (BiLSTM) [38], [46] and Stacked LSTM (StackedLSTM) [47], [48]. Although a direct comparison with (vanilla) SCRBM/gSCRBM may not be fair, experiments in the OCR data set show that gSCRBM_{i}, is slightly better than both BiLSTMs and StackedLSTMs (2 layers), but the differences are not statistically significant. For chunking, BiLSTMs outperform SCRBMs but SCRBMs are much faster. In Table V, we report the results of SCRBM_{i}, BiLSTM, and StackedLSTM using the activity recognition data set in Section V-C. It is showed that in this data set, both BiLSTM and StackedLSTM perform slightly better than gSCRBM_{i}, which is not surprised because gSCRBM_{i}, as a generic model, does not use bidirectional connections or stacking architecture.

#### VI. CONCLUSION

We have proposed a simple model for the classification of sequences by rolling RBMs with class labels over time. The main advantages of SCRBM are: it performs representation learning and inference efficiently and it is very compact with a number of parameters equivalent to that of standard RNNs with the same number of hidden neurons. Inference with SCRBM is done by performing prediction of the class and computing mean-field values of the hidden layer at each time t. We train SCRBM by computing the expectation of hidden units at time t − 1 for each element of the conditional distribution. This makes learning tractable. More importantly, when coupling SCRBM with complex memory gates in LSTM, we can achieve performance improvement in certain cases. In the experiments, we evaluate the effectiveness of the proposed model in sequence classification on three tasks: OCR, chunking, and multiactivity recognition. In these tasks, we show that the combination of SCRBM and input or output memory gate of LSTM outperforms the state of the art. Furthermore, we show that SCRBM can perform better than all other models in the chunking task, and it can generalize at least as well as GRU and LSTMs without the need for complex memory gates in the hidden units in the case of OCR, POS, and chunking. As future work, we intend to perform further evaluations of the SCRBMs at sequence learning. The systematic study of such simple recurrent models, possibly together with the use of knowledge extraction, should offer a better understanding of the basic ingredients for effective sequence learning.

Finally, there has been a resurgence of interest in RBMs although not for sequence classification [49], [50]. In [49],

a regularization technique is proposed to train RBMs for static data using generative methods. In [50], learning of RBMs is accelerated by using parallel computing and hardware design. The addition of regularization, attention, and dropout, as well as parallel speedups, is the possible directions of extensions of SCRBMs.

## ACKNOWLEDGMENT

The authors would like to thank S. Cherla for his suggestion and discussion. They would also like to thank C. Sutton for providing the features of the Conll2000 Chunking Task.
