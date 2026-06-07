# A fast numerical method for max-convolution and the application to efficient max-product inference in Bayesian networks 

Oliver Serang<br>Freie Universität Berlin and<br>Leibniz-Institute of Freshwater Ecology and Inland Fisheries (IGB)<br>orserang@uw.edu

Published in the Journal of Computational Biology, 2015 Aug;22(8):770-83. doi:10.1089/cmb.2015.0013


#### Abstract

Observations depending on sums of random variables are common throughout many fields; however, no efficient solution is currently known for performing max-product inference on these sums of general discrete distributions (max-product inference can be used to obtain maximum a posteriori estimates). The limiting step to max-product inference is the max-convolution problem (sometimes presented in log-transformed form and denoted as "infimal convolution", "min-convolution", or "convolution on the tropical semiring"), for which no $O(k \log (k))$ method is currently known. Here I present a $O(k \log (k))$ numerical method for estimating the max-convolution of two nonnegative vectors (e.g., two probability mass functions), where $k$ is the length of the larger vector. This numerical maxconvolution method is then demonstrated by performing fast max-product inference on a convolution tree, a data structure for performing fast inference given information on the sum of $n$ discrete random variables in $O(n k \log (n k) \log (n))$ steps (where each random variable has an arbitrary prior distribution on $k$ contiguous possible states). The numerical maxconvolution method can be applied to specialized classes of hidden Markov models to reduce the runtime of computing the Viterbi path from $n k^{2}$ to $n k \log (k)$, and has potential application to the all-pairs shortest paths problem.


## 1 Introduction

In many fields it is common to have access to information about sums of random variables and to desire information about those variables themselves. In mass spectrometry, when two (or more) analytes with similar mass-to-charge

are measured, the intensity of the resulting peak is a function of the sum of abundances of those analytes (this problem occurs not only in the mass spectrometry of small molecules, but also in measuring isotope measurement in elemental and nuclear mass spectrometry). In transcriptomics, the abundance of a particular non-unique read (i.e., an RNA sequence that maps to multiple locations in the transcriptome or genome) provides information about the sum of the abundances of all transcripts that contain the read (each transcript weighted by how many copies of the read it carries). Proteomics has its own version of non-unique reads, shared peptides which can be found in multiple proteins (not only are shared peptides the principal source of difficulty in protein inference $[14,17,18]$, they are also responsible for the difficulty evaluating putatative sets of discovered proteins $[16,19])$. In population genetics, the prior knowledge about population structure can suggest an expected number of individuals with a particular genotype, which in turn yields probabilistic information about the individuals whose aggregate genotypes are expected to produce that sum (inference is particularly pronounced in polyploids, which increase the dimensionality of the problem [15]).

In all of these fields, the information on sums of random variables presents a singular obstacle to computational biology. And regardless of how infrequently we as scientists directly discuss our current inability to effectively utilize information about sums of random variables, the perception of our limited ability to meet the challenge has become firmly entrenched in our collective unconscious; the silent agreement on our inability to turn the sausage grinder backwards and convert the sausage (information about the sum of several random variables) back into the pigs (information about those random variables that contributed to the sum) is so well-established that it not only defines the way that we address these data (i.e., mass spectra peaks containing multiple analytes, counts of nonunique reads, etc.), but it also causes us to discard data and even limit research directions we might otherwise consider. For instance, in mass spectrometry, substantial effort is invested in chromatography [2,9] and other separation techniques [12], which aim to distinguish and separate analytes so that they will not be measured by the mass spectrometer simultaneously (thereby reducing the chances of analytes resulting in overlapping peaks); the task of decomposing this useful aggregate information from overlapping peaks back into information about its contributing parts is eschewed in favor of significant investments in instrumentation (e.g., more and more advanced separation technologies and higher-resolution mass spectrometers [11]), and still it is common practice to discard shared isotope peaks and shared peptides even though they may comprise a large percent of the data and contain additional information [5, 19]. Likewise, in genomics and transcriptomics it is common to simply discard all data from non-unique reads $[10,23]$. In burgeoning fields such as metagenomics, this loss of data- and subsequent loss of information- can be even more pronounced, for instance when all data that map to two or more species of interest are discarded. In some cases, recovering this lost information will be the key to making strong conclusions, such as distinguishing between two closely related species (or bacterial strains) in a metagenomic mixture.

# Sum-product inference 

Fast Fourier transform- (FFT-)based convolution can be used to dramatically improve the efficiency of computing the sum-product addition of two discrete random variables. For three discrete random variables where $M=L+R$ and where $L \in\{0,1, \ldots k-1\}$ and $R \in\{0,1, \ldots k-1\}$, then the probability mass function (PMF) of $M$ can be computed via the convolution of the PMFs of $L$ and $R$, denoted $\operatorname{pmf}_{L}$ and $\operatorname{pmf}_{R}$ respectively. Note that it is sufficient to compute $\operatorname{pmf}_{M}^{\prime} \propto \operatorname{pmf}_{M}$, because the result will be scaled so that its sum is of unity $\left(\operatorname{pmf}_{M}=\frac{\operatorname{pmf}_{M}^{\prime}}{\sum_{m} \operatorname{pmf}_{M}^{\prime}[m]}\right)$ :

$$
\begin{aligned}
\operatorname{pmf}_{M}[m] & \propto \sum_{\ell} \sum_{r} \operatorname{Pr}(L=\ell) \operatorname{Pr}(R=r) \operatorname{Pr}(M=\ell+r) \\
& =\sum_{\ell} \operatorname{Pr}(L=\ell) \operatorname{Pr}(R=m-\ell) \\
& =\operatorname{pmf}_{L} * \operatorname{pmf}_{R}
\end{aligned}
$$

where $*$ performs the convolution between the two $k$-length vectors storing each PMF.

Whereas naive convolution would compute $\operatorname{pmf}_{M}$ in $O(k \times k)$ steps, FFT exploits the bijection of this convolution to the product between two polynomials (where the vectors being convolved are the coefficients of the polynomials being multiplied and the coefficients of their product forms the vector result); this bijection enables the use of alternative forms for representing the polynomials (each order $k-1$ polynomial can be represented through $k$ unique points through which it passes), which in turn permits elegant divide and conquer algorithms such as the Cooley-Tukey FFT to compute fast convolution in $k \log (k)$ steps. Subtraction in the sum-product (i.e., computing $L=M-R$ ) scheme can be performed by first negating $R^{\prime}=-R$ (this is done by reversing reversing the vector storing the $\operatorname{PMF} \operatorname{pmf}_{R^{\prime}}[r]=\operatorname{pmf}_{R}[-r]$ ), and then adding $L=M+R^{\prime}$ as before via FFT convolution $\operatorname{pmf}_{L}^{\prime}=\operatorname{pmf}_{M} * \operatorname{pmf}_{R^{\prime}}$. Also, the runtime constant on FFT convolution algorithms is generally very low, partly due to the nature of elegance of the algorithms and partly because implementations have been optimized heavily due to the ubiquity of convolution in signal processing.

The task of processing information about the sum of $n$ discrete variables (each with $k$ bins) to retrieve information on the individual variables can be performed naively in $O\left(k^{n}\right)$ steps by simply enumerating the exponentially many possible outcomes; however, such brute-force techniques are wildly inefficient when either $n$ or $k$ become large. Fortunately, recent work proposes methods to decompose larger problems (e.g., into multiple sums and differences of pairs of discrete variables of the form $M=L+R$ and $L=M-R$, very fast inference can be achieved. This has been derived for binary variables $(k=2)$ in $n \log (n) \log (n)$ [21], and was independently discovered for arbitrary discrete distributions (i.e., where $k>2$ ) and to multidimensional distributions (via matrix convolution, which can be decomposed into one-dimensional convolutions by the row-column

algorithm) using the probabilistic convolution tree [13] (algorithm 1). In the general case, distributions on all individual variables conditional on information about the sum can be computed in $O(n k \log (n k) \log (n))$ steps (whenever $k \log (k)$ fast convolution is available):

$$
\begin{aligned}
\operatorname{convolutionTreeCost}(n, k) & =\sum_{u=1}^{\log (n)} \frac{n}{2^{u}} \operatorname{convolutionCost}\left(k 2^{u}\right) \\
& =\sum_{u=1}^{\log (n)} \frac{n}{2^{u}} k 2^{u} \log \left(k 2^{u}\right) \\
& =n k \sum_{u=1}^{\log (n)} \log (k)+\log \left(2^{u}\right) \\
& =n k \sum_{u=1}^{\log (n)} \log (k)+u \\
& =n k\left[\sum_{u=1}^{\log (n)} \log (k)\right]+\left[\sum_{u=1}^{\log (n)} u\right] \\
& =n k[\log (n) \log (k)]+\left[\frac{\log (n)(\log (n)+1)}{2}\right] \\
& \in O(n k \log (n k) \log (n)
\end{aligned}
$$

In practice, this can be significantly faster than the $O\left(n^{2} k^{2}\right)$ steps required by dynamic programming when fast convolution is not available. For instance, when an observed transcript fragment could originate from $n=256$ species, and where the abundance of each species is discretized into $k=1024$ bins, then fast convolution makes inference more than 1800 times faster (the difference between one algorithm taking 1 second and the other taking 30 minutes), and the disparity only grows for problems with larger values of $n$ and $k$. It should be noted that these are only approximate runtimes calculated from the Big O form; in practice, it is fairly likely that methods based on fast convolution will be significantly faster, because of the method's inherent properties and the fact that very optimized implementations exist.

# Max-product inference 

Qualitatively, max-product inference is a close cousin to sum-product inference. Where sum-product inference considers each of the exponentially many joint events and allows each to contribute to the result (in hidden Markov models, this is analogous to the forward-backward algorithm), max-product inference allows only the highest-quality joint events to contribute (in hidden Markov models, this defines the Viterbi path). Both inference methods have complementary advantages and disadvantages: The advantage of sum-product inference

```
Algorithm 1 The probabilistic convolution tree algorithm utilizes fast
convolution (or fast max-convolution) to efficiently turn information on sums of
variables back into information on the individual variables. The first parameter
\(\left(\operatorname{pmf}_{X_{1}}, \operatorname{pmf}_{X_{2}}, \ldots \operatorname{pmf}_{X_{n}}\right)\) is a collection of \(n\) multidimensional discrete distri-
butions (with same dimension). In the case of univariate distributions, they are
one-dimensional PMFs with \(k\) possible outcomes. The second parameter \(\operatorname{pmf}_{M}\)
is a multidimensional discrete distribution (with same dimension as \(X_{1}, X_{2}, \ldots\) )
where \(M=X_{1}+X_{2}+\ldots+X_{n}\). The third parameter is a convolution operator
(e.g., either standard convolution or max-convolution). The algorithm returns
a pair of values. The first is a collection of likelihood distributions given on
the information from the sum \(M,\left(\operatorname{pmf}_{Y_{1}}, \operatorname{pmf}_{Y_{2}}, \ldots \operatorname{pmf}_{Y_{n}}\right)\). The second is the
prior distribution of \(M\) after adding together all \(X_{1}+X_{2}+\ldots X_{n}\). When \(n\)
is not an integer power of 2, dummy variables whose PMFs of length 1 (i.e.,
PMFs that are Kronecker deltas with 100\% chance of having value 0 ) should be
padded on until the next power of 2 is reached (this will allow construction of
a full binary tree without changing the sum).
procedure ProbabilisticConvolutionTREE \(\left(\left(\operatorname{pmf}_{X_{1}}, \operatorname{pmf}_{X_{2}}, \ldots \operatorname{pmf}_{X_{n}}\right)\right.\),
\(\operatorname{pmf}_{M}, *_{\text {param }}\)
    forwardTree \(\leftarrow\left[\left[\operatorname{pmf}_{X_{1}}, \operatorname{pmf}_{X_{2}}, \ldots \operatorname{pmf}_{X_{n}}\right]\right]\)
    for \(i=1\) to len \(\left(\log _{2}(n)\right) i+=1\) do
        currentLayer \(\leftarrow\) forwardTree \([-1] \quad \triangleright\) Where \([-1]\) gives the last index as
in Python
        newLayer \(\leftarrow[]\)
        for \(j=1\) to len(currentLayer) \(-1, j+=2\) do
            sum \(\leftarrow\) currentLayer \([j] *_{\text {param }}\) currentLayer \([j+1]\)
            newLayer.append(normalized(sum))) \(\triangleright\) Add the PMFs using the
\(*_{\text {param }}\) operator
            end for
            forwardTree.append(newLayer)
        end for
        reverseTree \(\leftarrow\left[\left[\operatorname{pmf}_{M}\right]\right]\)
        for \(i=1\) to len \(\left(\log _{2}(n)\right), i+=1\) do
            currentLayer \(\leftarrow\) reverseTree \([-1]\)
            newLayer \(\leftarrow[]\)
            forwardTreeLayerToSubtract \(\leftarrow\) forwardTree \([-i-2] \quad \triangleright\) Python
notation for the second to last layer in forwardTree
            for \(j=1\) to len(currentLayer), \(j+=1\) do
                lhs \(\leftarrow\) forwardTreeLayerToSubtract \([2 j]\)
                rhs \(\leftarrow\) forwardTreeLayerToSubtract \([2 j+1]\)
                rhsSubtracted \(\leftarrow\) currentLayer \([j] *_{\text {param }}(-r h s) \triangleright\) Negation reverses
the vector
21: \(\quad \triangleright\) Then the \(*_{\text {param }}\) operator performs addition
22: \(\quad\) newLhs \(\leftarrow\) normalized(rhsSubtracted)
23: \(\quad\) lhsSutracted \(\leftarrow\) currentLayer \([j] *_{\text {param }}(-l h s)\)
24: \(\quad\) newRhs \(\leftarrow\) normalized(lhsSubtracted)
25: \(\quad\) newLhs \(\leftarrow\) newLhs.narrowToTheSupportOf(lhs)
26: \(\quad\) newRhs \(\leftarrow\) newRhs.narrowToTheSupportOf(rhs)
27: \(\quad\) newLayer.append(newLhs)
28: \(\quad\) newLayer.append(newRhs)
29: end for
30: reverseTree.append(newLayer \(\boldsymbol{z}\)
31: end for
32: \(\forall j\), \(\operatorname{pmf}_{Y_{j}} \leftarrow\) reverseTree \([-1][j]\)
33: \(\operatorname{pmf}_{Z} \leftarrow\) forwardTree \([-1][0]\)
34: \(\quad\) return \(\left(\left(\operatorname{pmf}_{Y_{1}}, \operatorname{pmf}_{Y_{2}}, \ldots \operatorname{pmf}_{Y_{n}}\right), \operatorname{pmf}_{Z}\right) \triangleright\) First return value: collection of
likelihood distributions
35: \(\quad \triangleright\) Second return value: prior distribution on \(M\)
36: end procedure
```

is its democratized equal weighting of all joint events, the variety of which can provide a rich description of any high-probability joint events suggested by the data; however, this can also have disadvantages in that many low-quality joint events (i.e., those with low joint probability) may shape the result as much as a small number of high-quality results. Likewise, in sum-product inference, multiple mutually exclusive joint events can simultaneously contribute to the result, raising the potential to erroneously infer implausible conclusions, because both may be plausible before considering the other. It is because of these disadvantages in sum-product inference that max-product inference is widely used, because it forces the inferences to be jointly plausible (not simply individually, but as a whole), and because it drowns out noise from low-quality configurations that can diffuse and lower the certainty of conclusions in sum-product inference.

Specifically, efficient max-product inference on sums of random variables would be quite useful; in addition to the examples of shared peptides, nonunique reads, etc. found throughout computational biology (wherein we have information about the sum of variables, but want to draw conclusions about the variables themselves), more efficient max-product inference would make possible new inference algorithms on specialized classes of hidden Markov models (HMMs) where the transition probabilities from the state at index $a$ to the state at index $b$ depend on a function of either $a+b$ or $a-b$ or $b-a$. Such HMMs have applications in finance and time series analysis, where the $k$ states at any layer are high-resolution discretizations of some quantity or price, and where the probability of a price moving up or down is influenced by the quantity up or down it moved since the previous time point. In a general HMM with $k$ states and $n$ layers of those states, performing either sum-product (via the forward-backward algorithm) or max-product (via the Viterbi algorithm) inference requires $O\left(n k^{2}\right)$ steps; however, performing sum-product inference on the specialized class of HMMs mentioned above would require only $O(n k \log (k))$ steps, because each layer can be processed as a two-node convolution tree. But finding the Viterbi path on such a model in $O(n k \log (k))$ steps is not currently feasible, because doing so would require performing max-convolution (where the max of all valid pairings is chosen rather than the sum over all valid pairings) in $O(k \log (k))$ steps.

However, despite the promise of max-product inference on sums of random variables, a fast practical solution that utilizes $O(k \log (k))$ max-convolution (i.e., one with speed roughly comparable to FFT-based standard convolution) is not yet available for the general max-convolution problem problem. One special cases for use only when $k=2[8,20]$, can solve the problem in $n \log (n)$ time by sorting the $n$ variables in descending order of probability $\operatorname{Pr}\left(X_{1}=1\right) \geq$ $\operatorname{Pr}\left(X_{2}=1\right) \geq \cdots \geq \operatorname{Pr}\left(X_{n}=1\right)$ and then exploiting the property that any case where the number of "true" variables $\sum_{j} X_{j}=m$ must prefer the first $m$ variables in the sorted order. This method understandably fails when $k>2$ because there is no guarantee of an ordering that will satisfy all dimensions (when $k=2$, increasing the probability of $\operatorname{Pr}\left(X_{j}=1\right)$ has a useful effect of decreasing the probability of $\operatorname{Pr}\left(X_{j}=0\right)$ by the same amount in order to preserve the

unitary value of the sum). When $k>2$, a similar idea to the sorting approach can be used, but not without approximation or some method for exploring or optimizing the exponential space of joint events [15].

Adapting the probabilistic convolution tree algorithm from algorithm 1 (by simply replacing all uses of $*$ with $*_{\max }$ when adding pairs of variables) achieves only an $O\left(n^{2} k^{2}\right)$ runtime for max-product inference because additions and subtractions between individual pairs of random variables will require $O\left(k_{1} \times k_{2}\right)$ time without a faster algorithm for max-convolution. It is tempting to try to derive an FFT equivalent to max-convolution, a subtle difference makes this challenging: Where standard convolution uses the operations $(+, \times)$ on realvalued numbers (a "ring"), max-convolution employs (max, $\times$ ) (alternatively applying a log-transformation to the probabilities being convolved will negate them and thus change the problem to the equivalent $(\min ,+)$ operations, called min-convolution, infimal convolution, or convolution on the "tropical semiring"). Regardless of which form is used, the employment of the max (or min in the min-convolution case) downgrades the operation from a ring to a "semiring" because the max and min operations have no inverse. Thus, the max-product addition of two discrete random variables takes a different form, which is no longer bijective to polynomial multiplication:

$$
\begin{aligned}
\operatorname{pmf}_{M}[m] & \propto \max _{\ell} \max _{r} \operatorname{Pr}(L=\ell) \operatorname{Pr}(R=r) \operatorname{Pr}(M=\ell+r) \\
& =\max _{\ell} \operatorname{Pr}(L=\ell) \operatorname{Pr}(R=m-\ell) \\
& =\operatorname{pmf}_{L} *_{\max } \operatorname{pmf}_{R}
\end{aligned}
$$

where $*_{\max }$ is the max-convolution operator. The loss of the bijective polynomial representation prevents the exploitation of the Lagrange form of polynomials, and thus there is no known $k \log (k)$ algorithm for performing max-convolution.

Excluding such highly specialized methods as the rank method of Babai [1] (which achieves a runtime of $O\left(k_{1} \sqrt{k_{2} \log \left(k_{2}\right)}\right)$ time but only when the vector of length $k_{2}$ contains elements with value 0 or $\infty$ ), the two most sophisticated maxconvolution algorithms applicable to probabilistic inference are from Bussieck et al. [4] and Bremner et al. [3].

The method from Bussieck has a $O\left(k^{2}\right)$ runtime in the worst case, but under a certain distribution values in the two vectors being convolved, the authors demonstrate an expected runtime of $O(k \log (k))$ [4]. The approach works by starting the result $\forall m, \operatorname{pmf}_{M}^{\prime}[m] \leftarrow-\infty$ and then proceeds by sorting the two vectors being convolved ( $L$ and $R$ ) in descending order. Their method then proceeds through both lists head-first to generate the first $k \log (k)$ sorted terms of $\forall \ell, r \operatorname{pmf}_{L}[\ell] \operatorname{pmf}_{R}[r]$. Each of these terms is used to update the appropriate index in the result vector $\operatorname{pmf}_{M}^{\prime}[\ell+r] \leftarrow \max \left(\operatorname{pmf}_{M}^{\prime}[\ell+r], \operatorname{pmf}_{L}[\ell] \operatorname{pmf}_{R}[r]\right)$. Thus far, the algorithm is $\in O(k \log (k))$, but there may be indices of $\operatorname{pmf}_{M}^{\prime}$ that have not yet been set (they are still equal to $-\infty$ ); each of these must be computed, and each such direct computation takes $O(k)$ time (if there are $\Omega(k)$ such unset indices, then the overall runtime becomes $O\left(k^{2}\right)$ ). Despite the

significant achievement posed by the construction of this algorithm, the authors suggest that the runtime constant is quite high due to the overhead of the sophisticated algorithms used to sort the largest $k \log (k)$ values while neither sorting nor even generating all $k^{2}$ values; they suggest that their result is of mostly theoretical import, and suggest using other methods in practice.

The method of Bremner et al. (which was subsequently extended by Williams [22]) draws a relationship between min-convolution and the necklace alignment problem, wherein two two collections of beads, each on its own circular string, are rotated to optimally align [3]. Their method is the most sophisticated in existence, and consists of a highly complicated exploitation of similarity to the allpairs shortest paths problem to achieve a method with a subquadratic worst-case runtime of $O\left(k^{2} \frac{(\log (\log (k)))^{3}}{\log (k) \log (k)}\right)$ for each max-convolution (the runtime of the Bremner et al. method can also be improved using a more recent method for solving the all-pairs shortest paths problem, decreasing the runtime to $\frac{k^{2}}{2^{(k)} \sqrt{\log (k))}}$. [22]). Even if it were possble to be implemented with runtime constant as optimized as FFT, the cost of using a max-convolution tree to solve the previously mentioned metagenomic max-product inference problem on $n=256$ variables where each has $k=1024$ states would be over 166 times slower than the cost of solving an equally sized sum-product problem with FFT convolution (the number of steps required was calculated numerically to avoid computing a closed form of the computational cost).

Thus, even with significant mathematical sophistication of these two state-of-the-art methods, practically efficient max-product inference may be out of reach for even moderately sized problems.

# 2 A numerical method for efficiently estimating max-convolution 

Here I will introduce a numerical method for estimating the max-convolution in $k \log (k)$ time, which can be applied easily using existing high-performance numerical software libraries. This is essentially performed by transforming both the inputs and outputs of the FFT to achieve $p$-norm convolution, which in turn is used as an approximation for max-convolution via the Chebyshev norm.

For a max-convolution between $\operatorname{pmf}_{L}$ and $\operatorname{pmf}_{R}$

$$
\operatorname{pmf}_{M}^{\prime}[m]=\max _{\ell} \operatorname{pmf}_{L}[\ell] \operatorname{pmf}_{R}[m-\ell]
$$

at each $m$ value, the shifted products terms can be rewritten as a simple vector $u^{(m)}$ where elements are defined by

$$
u^{(m)}[\ell]=\operatorname{pmf}_{L}[\ell] \operatorname{pmf}_{R}[m-\ell]
$$

Furthermore, because PMFs consist of nonnegative real values (or machineprecision representations), then this can be rewritten using the Chebyshev norm,

which computes the maximum absolute value in the vector $u^{(m)}$. Because $u^{(m)}$ comes from the product of PMF terms, it is also nonnegative and thus absolute values can be ignored in both the computation and the result:

$$
\begin{aligned}
\operatorname{pmf}_{M}^{\prime}[m] & =\max _{\ell} u^{(m)}[\ell] \\
\left|\operatorname{pmf}_{M}^{\prime}[m]\right| & =\lim _{p \rightarrow \infty}\left\|u^{(m)}\right\|_{p} \\
\left|\operatorname{pmf}_{M}^{\prime}[m]\right| & =\lim _{p \rightarrow \infty}\left(\sum_{\ell}\left|u^{(m)}[\ell]\right|^{p}\right)^{\frac{1}{p}} \\
\operatorname{pmf}_{M}^{\prime}[m] & =\lim _{p \rightarrow \infty}\left(\sum_{\ell} u^{m)}[\ell]^{p}\right)^{\frac{1}{p}}
\end{aligned}
$$

And then each element of $u^{(m)}[\ell]$ can be expanded back into its original factors:

$$
\operatorname{pmf}_{M}^{\prime}[m]=\lim _{p \rightarrow \infty}\left(\sum_{\ell} \operatorname{pmf}_{L}[\ell]^{p} \operatorname{pmf}_{R}[m-\ell]^{p}\right)^{\frac{1}{p}}
$$

At this point, a sufficiently large value $p^{*}$ is used in place of the limit $p \rightarrow \infty$ :

$$
\operatorname{pmf}_{M}^{\prime}[m] \approx\left(\sum_{\ell} \operatorname{pmf}_{L}[\ell]^{p^{*}} \operatorname{pmf}_{R}[m-\ell]^{p^{*}}\right)^{\frac{1}{p^{*}}}
$$

At this point, it can be observed that every time elements of the PMFs $\operatorname{pmf}_{L}[\ell]$ and $\operatorname{pmf}_{R}[m-\ell]$ appear, they are raised to the $p^{*}$ power; thus, it is possible to change variables and let

$$
\begin{array}{ll}
\forall \ell & v_{L}[\ell]=\operatorname{pmf}_{L}[\ell]^{p^{*}} \\
\forall r & v_{R}[r]=\operatorname{pmf}_{R}[r]^{p^{*}}
\end{array}
$$

yielding

$$
\operatorname{pmf}_{M}^{\prime}[m] \approx\left(\sum_{\ell} v_{L}[\ell] v_{R}[m-\ell]\right)^{\frac{1}{p^{r}}}
$$

A similar strategy can be made for $\operatorname{pmf}_{M}^{\prime}$; it is possible to introduce another vector $v_{M}$ such that every element $\operatorname{pmf}_{M}^{\prime}[m]$ is the result of

$$
\begin{aligned}
\operatorname{pmf}_{M}^{\prime}[m] & \approx v_{M}[m]^{\frac{1}{p^{*}}} \\
v_{M}[m] & =\sum_{\ell} v_{L}[\ell] v_{R}[m-\ell]
\end{aligned}
$$

And thus it becomes clear that $v_{M}$ is the result of standard convolution (not a max-convolution) between $v_{L}$ and $v_{R}$. This suggests a numerical algorithm that can make use of existing FFT convolution libraries to compute $v_{M}=v_{L} * v_{R}$ in $O(k \log (k))$ steps (algorithm 2).

Algorithm 2 Numerical max-convolution (initial version), a numerical method to estimate the max-convolution of two PMFs or nonnegative vectors. The parameters are two PMFs $\operatorname{pmf}_{L}$ and $\operatorname{pmf}_{R}$ (by definition nonnegative) and the numerical value $p^{*}$ used for computation. The return value is a numerical estimate of the max-convolution $\operatorname{pmf}_{L} *_{\max } \operatorname{pmf}_{R}$.

```
procedure MAXCONVOLUTION \(\left(\mathrm{pmf}_{L}, \mathrm{pmf}_{R}, p^{*}\right)\)
    \(\forall \ell, v_{L}[\ell] \leftarrow \operatorname{pmf}_{L}[\ell]^{p^{*}}\)
    \(\forall r, v_{R}[r] \leftarrow \operatorname{pmf}_{R}[r]^{p^{*}}\)
    \(v_{M} \leftarrow \operatorname{pmf}_{L} * \operatorname{pmf}_{R} \quad \triangleright\) Standard FFT convolution is used here
    \(\forall m, \operatorname{pmf}_{M}^{\prime}[m] \leftarrow v_{M}[m]^{\frac{1}{p^{*}}}\)
    return \(\operatorname{pmf}_{M}^{\prime} \triangleright\) The return value is an estimate of the max-convolution result
end procedure
```


# 2.1 Reducing underflow 

The main caveat for numerical methods is often the loss of precision due to underflow when raising small probabilities to the power $p^{*}$ (in this case, no overflow occurs because the inputs are probabilities); such losses may not be undone later when raising to the $\frac{1}{p^{*}}$ power. One way to limit unnecessary loss of precision is to recognize that since $\mathrm{pmf}_{M}^{\prime}$ will be normalized after it is estimated, then it can be scaled arbitrarily during computation without altering the final result. For this reason it can be beneficial to scale a vector by dividing by its maximum element before raising it to the $p^{*}$ or $\frac{1}{p^{*}}$ power; this will start the dominant elements close to 1 , and thus allow them to lose little information to underflow. Using this strategy yields a slightly modified algorithm (algorithm 3).

Note that, like standard implementations of fast convolution $*$, in implementing the fast $*_{\max }$ operator it is possible to automatically choose between a naive implementation or the fast numerical implementation depending on the size of the problem; on very small problems (e.g. $k=8$ ), the naive operation will have less overhead and can be a bit faster (the specific threshold can be chosen roughly by comparing the expected running time from the fast numerical method $O\left(k^{\prime} \log \left(k^{\prime}\right)\right)$ (where $k^{\prime}$ is double the next integer power of two and the $\log$ is base two) to the $O\left(k_{1} \times k_{2}\right)$ ); this can reduce numerical error further.

## 3 Results

I briefly compare the speed and accuracy of the fast numerical max-convolution method as compared to naive max-convolution. Both methods are implemented in the Python programming language using floating point math and the numpy package (the fast numerical max-convolution method is implemented from algorithm 3.

Algorithm 3 Numerical max-convolution (normalized version), a numerical method to estimate the max-convolution of two PMFs or nonnegative vectors (revised to reduce underflow). The parameters are two PMFs $\operatorname{pmf}_{L}$ and $\operatorname{pmf}_{R}$ (by definition nonnegative) and the numerical value $p^{*}$ used for computation. The return value is a numerical estimate of the max-convolution $\operatorname{pmf}_{L} *_{\max } \operatorname{pmf}_{R}$.
procedure MAXCONVOLUTIONREVISED $\left(\operatorname{pmf}_{L}, \operatorname{pmf}_{R}, p^{*}\right)$
2: $\ell_{\max } \leftarrow \operatorname{argmax}_{\ell} \operatorname{pmf}_{L}[\ell]$
3: $\quad r_{\max } \leftarrow \operatorname{argmax}_{r} \operatorname{pmf}_{R}[r]$
4: $\quad \forall \ell, v_{L}[\ell] \leftarrow\left(\frac{\operatorname{pmf}_{L}[\ell]}{\operatorname{pmf}_{L}\left[\ell_{\max }\right]}\right)^{p^{*}}$
5: $\quad \forall r, v_{R}[r] \leftarrow\left(\frac{\operatorname{pmf}_{R}[r]}{\operatorname{pmf}_{R}\left[r_{\max }\right]}\right)^{p^{*}}$
6: $\quad v_{M} \leftarrow \operatorname{pmf}_{L} * \operatorname{pmf}_{R} \quad \triangleright$ Standard FFT convolution is used here
7: $\quad m_{\max } \leftarrow \operatorname{argmax}_{m} v_{M}[m] \quad \triangleright$ Correct any small errors in FFT convolution
8: $\quad \forall m, \operatorname{pmf}_{M}^{\prime}[m] \leftarrow\left(\frac{v_{M}[m]}{v_{M}\left[m_{\max }\right]}\right)^{\frac{1}{2^{k}}}$
9: $\quad$ return $\operatorname{pmf}_{L}\left[\ell_{\max }\right] \operatorname{pmf}_{R}\left[r_{\max }\right] \operatorname{pmf}_{M}^{\prime} \quad \triangleright$ Undo the previously performed scaling
10: end procedure

# 3.1 Practical efficiency of fast numerical max-convolution 

The speed of naive max-convolution is compared to the fast numerical estimate. For each $k \in\{32,64,128,256,512,1024,2048,4096,8192\}$, random pairs of vectors with uniform elements (i.e., each element is drawn from uniform $(0,1)$ ). The result of the max-convolution $\operatorname{pmf}_{L}^{\prime} *_{\max } \operatorname{pmf}_{R}^{\prime}$ is computed via $O\left(k^{2}\right)$ naive max-convolution and the fast numerical method. Figure 1 demonstrates an substantial speedup in practice.

### 3.2 Accuracy of fast numerical max-convolution compared to naive max-convolution

A cursory empirical test of the numerical stability as a result of $p^{*}$ and the vector length $k$ was performed. In figure 2, the numerical stability was demonstrated on 64 random pairs of vectors for each length $k \in 128,256,512,1024$. For all $p^{*} \in\{2,4,8,16,32,64\}$, and the relative absolute error of each element in the result of the max-convolution is computed $\left|\frac{\text { numerical }[m]-\text { exact }[m]}{\text { exact }[m]}\right|$, where numerical $[m]$ and exact $[m]$ refer to the value at index $m$ of the numerical and naive results respectively. (Figure 2) demonstrates the relationship between $p^{*}, k$, the relative absolute error and the magnitude of the exact result.

Qualitatively, optimizing the numerical performance involves satisfying competing ideals: when $p^{*}$ is large, the problem solved converges to the maxconvolution inference, but underflow becomes significant. When $p^{*}$ it's too small, non-maximal terms contribute to the result (more similar to a standard convolution).

![img-0.jpeg](img-0.jpeg)

Figure 1: Runtime comparison between naive and fast numerical convolution. Note the increasing gap between the two curves, which indicates a nonlinear speedup because of the log-scaling of both axes (because the runtime of the fast numerical method is dominated by FFT calculation).

![img-1.jpeg](img-1.jpeg)

Figure 2: The influence of the parameter $p^{*}$ on max-convolution accuracy. For each $k \in\{256,512,1024\}, 64$ replicate max-convolutions are performed to compare the relative error of the fast numerical method compared to the naive method. This is performed for different values of $p^{*}$; lower values of $p^{*}$ perform well when the exact result is close to zero, and higher values of $p^{*}$ perform better otherwise, and this relationship seems invariant of $k$ when the data are scaled in the manner presented (they are scaled so that the largest element has value 1 ).

Although more sophisticated numerical analysis would almost certainly yield larger improvements to the method, a simple improvement is exploited: Generally the relative error is fairly low, but only becomes high in these experiments when the exact value at that index is close to zero (this is intuitive from the formula for relative absolute error). Since underflow is the only numerical consideration (because the values are normalized to the maximum), then it follows that a result that is not close to zero at some index is convergent when $p^{*}$ is substantially large (if it suffered from too much underflow, then it would approach zero quickly). Therefore, when using a high value of $p^{*}$, indices where the numerical solution is close to zero indicate that the potential for numerical error, and suggest that a smaller value of $p^{*}$ could be used for those indices. This yields a further improvement where a more accurate result can be constructed from two calls of algorithm 3; this improved method is shown in algorithm 4, and runs in roughly twice as many steps as algorithm $3($ still $\in O(k \log (k)))$. Note that this piecewise method could be trivially extended to use more than two values of $p^{*}$, increasing accuracy at the expense of additional runtime (although, assuming the results using the different values of $p^{*}$ are computed in decreasing order, then the routine could potentially terminate once the result has been estimated at all indices with adequate numeric stability).

# 3.3 Using fast numerical convolution to solve a probabilistic subset sum problem 

Lastly, a three-way piecewise implementation of max-convolution similar to the one shown in algorithm 4 but using $p^{*} \in\{4,32,64\}$ (the Python code of this three-way piecewise method is given in the accompanying Python demonstration code) is used to solve a simulated probabilistic generalization of the the subset sum problem. In this problem, $n=32$ people go shopping and each person $j$ in $\{1,2, \ldots n\}$ buys exactly one of two items (the price of the item they do purchase is $\mu_{j}^{(\text {true })}$ and the price of the item they do not purchase is $\mu_{j}^{(\text {false })}$ ), where the costs of both items for each person $j$ are unknown to us. Then, given fuzzy knowledge about the costs of these items with all prices discretized into $k=256$ bins (i.e., $\forall j, \operatorname{pmf}_{X_{j}}[\ell]$ where $\ell \in\{0,1, \ldots k-1\}$ ) and given fuzzy knowledge about the total amount spent $\left(\operatorname{pmf}_{M}\right.$, where $M=\sum_{j} X_{j}$ ), we try to infer the amount spent by each person (i.e., for each person $j$, estimating $\left.\mu_{j}^{(t r u e)}\right)$.

Data are generated as follows: At each variable $X_{j}, j \in\{1,2, \ldots n\}$, two means are randomly sampled $\mu_{j}^{(\text {true })}, \mu_{j}^{(\text {false })} \sim \operatorname{uniform}(0, k-1)$, and a discretized Gaussian PMF is centered about each mean (the standard deviations of the Gaussians are each sampled $\sigma_{j}^{(t r u e)}, \sigma_{j}^{(f a l s e)} \sim \operatorname{uniform}\left(0, \frac{k}{10}\right)$ ). A vector proportional to the PMF $\operatorname{pmf}_{X_{j}}[\ell]$ is computed using the sum of these Gaussians with a vector of uniform noise $\alpha^{(m)}[\ell] \sim \operatorname{uniform}(0,0.0001)$. The likelihood distribution on the sum $M=\sum_{j} X_{j}$ is generated by adding a Gaussian with mean $\sum_{j} \mu_{j}^{(t r u e)}$ and variance $0.005 \times(n k-(n-1))$ (i.e., $0.005 \times$ the

```
Algorithm 4 Numerical max-convolution (piecewise normalized ver-
sion), a numerical method to estimate the max-convolution of two PMFs or
nonnegative vectors (further revised to strategically choose p*). The param-
eters are two PMFs pmf
by definition nonnegative). The return value is a numerical estimate of the
max-convolution pmf
max Convolutiong
max ConvolutionRevised from algorithm 3. Note that the values of p*
p}
application.
procedure maxConvolutionPiecewise(pmf
        p}
        p}
        \tau \leftarrow 0.6 \triangleright This is a two-way piecewise implementation; higher orders will be
    slower and more accurate
        f
        f aggressive calculation
        for m to k, m+ = 1 do
            if }f_{higher}[m]\geq\mp@subsup{\tau}{}{*}\mathrm{ then
                f[m]\leftarrowf aggressive[m]\triangleright When high-p* result is large enough,
underflow isn't an issue
            else
            f[m]\leftarrowf_{stable}[m]\triangleright Where the high-p* result is small, use f
```

```
    end if
    end for
    return f
end procedure
```

possible number of outcomes for $M$ ), plus point-wise samples of uniform noise $\alpha^{(o u t)}[\ell] \sim \operatorname{uniform}(0,0.0001)$.

On each problem instance, likelihoods for all inputs $\left(\operatorname{pmf}_{Y_{1}}, \operatorname{pmf}_{Y_{2}}, \ldots \operatorname{pmf}_{Y_{n}}\right)$ are computed twice, once using naive max-convolution and once using the numerical method. Note that even though these values of $n$ and $k$ do not appear particularly large, the full max-convolution tree that they produce will will compute several max-convolutions on the order of $O(k)$ and a few on the order of $O(n \times k)$, which in this case can be $32 \times 256=8192$. For this reason, computing the likelihood curve with the naive result requires 159 seconds, while the fast numerical approach takes 0.935 seconds to compute a highly similar result.

A single likelihood distribution $\operatorname{pmf}_{Y_{j}}$ for one particular $j \in\{1,2, \ldots n\}$, which was computed using the naive method, the fast numerical method is plotted in figure 3. This figure also demonstrates the utility of max-product inference by also showing the result from sum-product inference, which is much less informative (and does not have a mode close to the correct answer.

# 4 Discussion 

Although its ethos may ultimately limit the utility of this method to numerical settings where small errors are tolerable (as opposed to the to more general theoretical papers previously mentioned $[3,4]$ ), numerical method proposed here gives a simple and very fast estimate of the max-convolution result, which could allow use of numerical max-convolution (or max-product inference on the sums and differences between discrete distributions) in settings where it is currently far too computationally expensive. The largest caveat to the method is the inaccuracy that can occur due to numerical bottlenecks (e.g., underflow); however, for many problems (e.g., practical applications of the max-product inference problem in figure 3), the numerical method is sufficient to perform high-quality inference, but in a dramatically faster time.

Furthermore, the connection between the max-convolution problem and the all-pairs shortest path problem from graph theory [3] means that the fast numerical method may be used to compute fast numerical approximations to that important computer science problem. Such fast numerical estimates could complement theoretical solutions to that problem.

A more in-depth theoretical analysis of the algorithm's error would likely yield multiple opportunities to modify the algorithm in order to decrease error. For example, one possible improvement could be performed by using log-transformed real values: in log-transformed space, raising to the power $p^{*}$ would be equivalent to scaling by $p^{*}$, and would not produce significant underflow. Furthermore, the operations required by FFT convolution could be performed in log-space by translating the ring $(+, \times)$ on real values to its equivalent ring $\left(\log _{+}, \log _{+}\right)=\left(\log _{+},+\right)$on log-transformed values, where the operation $\log _{+}(x, y)$ is performed by dividing out the greater of the two arguments $x$ (w.l.o.g.) and then computing $\log \left(1+\frac{y}{x}\right)=\log (1+z)$ via Taylor series; performing the Cooley-Tukey FFT on log-transformed values (or possibly using

![img-2.jpeg](img-2.jpeg)

Figure 3: Using fast numerical max-convolution for max-product inference. A single likelihood distribution for one particular $j \in\{1,2, \ldots n\}$ from the probabilistic generalization of the subset-sum problem is shown. This distribution is computed via a probabilistic max-convolution tree (the problem is solved twice, once with naive max-convolution and once via fast numerical max-convolution). The true mode value $\mu_{j}^{(\text {true })}$ for that $j$ is indicated by the bar beneath the largest mode. To compare the results of different types of inference, the sum-product result from the convolution tree (using the standard convolution operator) is also plotted; note that sum-product inference produces a less discriminative likelihood curve because many possible joint events have diffused into it.

a different FFT algorithm that is particularly well suited for log-transformed values) could represent one route for improving the accuracy.

In a similar vein, more sophisticated techniques for locally choosing among a small number of values for $p^{*}$ (compared to a simple piecewise function on two possible values of $p^{*}$ ). For instance, under roughly uniform distributions of values in the two vectors being max-convolved, the values closest to zero (and thus having higher chance of having high relative absolute error) will occur more commonly at the first and last indices of the numerical estimate (because those indices take the maximum over smaller collections of elements, and are thus more likely to be smaller values). Similar attention could be put toward scaling the vectors prior to taking elements to the $p^{*}$ (compared to the current procedure of dividing by the maximum element value) may minimize the underflow on a large number of points with large values. A most exciting possibility would be that having an accurate estimate of the max-convolution result somehow could be used to compute a more accurate result (e.g., using approximate results from different $p^{*}$ and exploiting the property $\|\cdot\|_{p} \geq\|\cdot\|_{p+\delta}$ when $p \geq 1$ and $\delta>0$ ). Such directions of future research could possibly solving the maxconvolution iteratively over a bounded or constant number of subproblems where each subproblem requires $O(k \log (k))$, by first computing initial estimates of the max-convolution result with the numerical method presented here, and then using those initial estimates to parameterize a subsequent call to the numerical method in a manner reminiscent of the QR algorithm for eigendecomposition $[6,7]$. From algorithm 4, it seems highly likely that there will be more ways by which an initial result can be used to obtain a higher-accuracy result.

Furthermore, even pursuing methods for obtaining very high accuracy with large values of $p^{*}$ may not always be of substantial interest. Indeed, even if no improvement to accuracy is ever presented, the design and parameterization of machine learning methods (including graphical models) has traditionally been empirically driven, and the use of exact max-product inference is hardly sacrosanct in every application (as opposed to inference somewhere between sum-product and max-product). From this perspective, rather than choosing $p^{*}$ as a static constant value $p^{*}=1$ (i.e., performing sum-product inference) or $p^{*} \rightarrow \infty$ (i.e., performing max-product inference), $p^{*}$ could be viewed as a hyperparameter that is used to position inference on a continuum somewhere between all joint events contributing equally to the end result (sum-product) and only the best joint event contributing (max-product), and intermediate values of $p^{*}$ would establish a preference for the top few joint events. In this sense, the value chosen for $p^{*}$ could be driven by the data, and the problem of $p$-norm convolution (where a finite $p$ is desired, rather than max-convolution where $p \rightarrow \infty$ ) can already be solved with very high accuracy by the proposed numerical method for any moderate choice of $p^{*}$.

# 5 Availability 

A simple illustration of the fast numeric max-convolution method in Python (using the numpy package), including a three-way piecewise implementation, is available at https://bitbucket.org/orserang/fast-numerical-max-convolution.

## Acknowledgements

Thanks to Mattias Franberg and Ryan Emerson for the helpful comments.
