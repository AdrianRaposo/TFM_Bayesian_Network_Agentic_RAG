# Estimating Single-Cell Lag Times via a Bayesian Scheme ${ }^{\text {V }}$ 

P. K. Malakar* and G. C. Barker<br>Institute of Food Research, Norwich Research Park, Colney, Norwich NR4 7UA, United Kingdom

Received 9 June 2008/Accepted 9 September 2008


#### Abstract

Network models offer computationally efficient tools for estimating the variability of single-cell lag phases. Currently, optical methods for estimating the variability of single-cell lag phases use single-cell inocula and are technically challenging. A Bayesian network model incorporating small uncertain inocula addresses these limitations.


It is possible to measure the variability of growth from single cells by microscopy $(4,5)$, but these methods are laborious. Optical density measurements provide a rapid method for generating growth data from small inocula. However, the cell density for which a significant optical measurement is obtained is quite high. The detection threshold for this optical method is typically $\sim 10^{7}$ cells $\mathrm{ml}^{-1}$. Conclusions concerning growth from a single cell to a population of $\sim 10^{7}$ cells must be extrapolated from growth observed after the detection threshold (3). This extrapolation adds to measurement uncertainty when trying to estimate the variability of growth from single cells.

There is a consensus among microbiologists that bacterial cells undergo a period of adjustment (lag phase) when placed in a new environment. After adjustment, an exponentially growing population is established which, ultimately, reaches an upper limit (stationary phase). This population limit is caused by the depletion of nutrients or by the accumulation of waste products of metabolism. Growth is not observed during the lag phase. The lag phase and subsequent growth before the stationary phase can be modeled using a biphasic linear function,

$$
\ln \left(N_{t}\right)=\ln (n)+\mu \times \max (t-L)
$$

where $N_{t}$ is the population size at time $t, n$ is the inoculum size, $\mu$ is the specific growth rate, and $L$ is the population lag time.

It has been shown that the population lag phase, under the assumptions of the biphasic linear model, is related to the lag phase of the individual cells which make up the inoculum (1). A bacterial population at time $t$, grown from an inoculum consisting of $n$ cells, can be represented by

$$
N_{t}=\sum_{i=1}^{n} e^{\mu \times \max \left(t-L_{i} / t\right)}
$$

where $\mu$ is the specific growth rate for cells (we assume that this is constant within the cell inoculum). Note that the lag phases of individual cells in the inoculum, $L_{i}$, are identically and independently distributed random variables. The natural

[^0]logarithm of the cell population for a sufficiently long time (when $t$ is greater than the maximum of $L_{i}$ ) is

$$
\ln \left(N_{t}\right)=\ln (n)+\mu\left[t-\left(\frac{\sum_{i=1}^{n} e^{-\mu \times L_{i}}}{-\frac{1}{\mu} \ln \frac{e^{-\mu \times L_{i}}}{n}}\right)\right]
$$

Then, from the biphasic growth model, the population lag time $K_{n}$, arising from an initial inoculum of size $n$, is

$$
K_{n}=-\frac{1}{\mu} \ln \frac{\sum_{i=1}^{n} e^{-\mu \times L_{i}}}{n}
$$

and the time it takes to establish a population with size $N_{b}$ in the exponential phase is

$$
t_{b}=\frac{\ln \left(N_{b}\right)}{\mu}-\frac{\ln (n)}{\mu}+K_{n}
$$

The Bioscreen (Labsystems, Finland) system is an automated optical density reader. Bacterial suspensions are dosed into wells arranged in a honeycomb pattern in a plate. Each well can hold $400 \mu 1$ of cell suspension, and the turbidity of the suspension increases as the density of bacterial cells in the suspension increases. The increase of turbidity can be correlated with cell numbers. There are 200 wells in a Bioscreen plate, and the measurement of population growth using this system can generate sufficient data for estimating the variability of single-cell lag phases. If each well initially holds one cell, then for each well

$$
t_{b}=\frac{\ln \left(N_{b}\right)}{\mu}+L
$$

This can be interpreted as the distribution of times, $t_{b}$, for a population of wells and is equivalent to a shifted form of the distribution, $L$, for individual cell lag times (2).

It is a challenge experimentally to place exactly one cell in all of the wells in a Bioscreen honeycomb plate. If it is possible to introduce one cell into $50 \%$ of the wells and two cells into the rest of the wells, then $t_{b}$ has a mixture distribution


[^0]:    * Corresponding author. Mailing address: Institute of Food Research, Norwich Research Park, Colney, Norwich NR4 7UA, United Kingdom. Phone: 441603 255141. Fax: 441603 507723. E-mail: pradeep.malakar@bbsrc.ac.uk.
    ${ }^{\dagger}$ Published ahead of print on 19 September 2008.

$$
p\left(t_{b}\right)=0.5\left[\frac{\ln \left(N_{b}\right)}{\mu}+L\right]+0.5\left[\frac{\ln \left(N_{b}\right)}{\mu}-\frac{\ln (2)}{\mu}+K_{2}\right]
$$

where the terms in brackets are symbolic representations for distributions that correspond to monodisperse inocula. Generalizing to an uncertain number of cells in each well gives

$$
p\left(t_{b}\right)=\sum_{n=1}^{\infty} p(n)\left[\frac{\ln \left(N_{b}\right)}{\mu}-\frac{\ln (n)}{\mu}+K_{n}\right]
$$

where $p(n)$ is the distribution of inoculum sizes. With this construction, efficient statistical methods combined with Bayesian methodology can be used to establish the distribution of lag times of single cells, $p\left(L_{i}\right)$, for small $n$. The scheme computes the Bayesian posterior for $p\left(L_{i}\right)$ based on prior beliefs and on observed information for $t_{b}$ from the Bioscreen system. Prior beliefs concerning $N_{b}$ and $\mu$ can be obtained from independent calibration experiments, so these variables include only slight uncertainty.

Practical schemes introduce an uncertain number of cells into each well of a Bioscreen plate by serial dilution of a volume containing a known density of cells. This inoculation leads to a Poisson distribution for the number of cells in a well, and a significant number of wells will be empty. In this case, a well that does not show any signs of growth during an experimental period could still contain a cell (or cells) if this cell has a long lag time. Equation 8 is not sufficient for estimating the lag-phase distribution of cells unless the wells in a Bioscreen plate are certainly not empty (i.e., $n$ is $>0$ ).

To address this problem, we can consider the Bioscreen experiment a combination of two events. The first event is the initial inoculation of a well with an uncertain number of cells which is determined by a Poisson distribution and parameterized by the expectation of the cell number $\theta$. The second event is uncertain growth from cells in the well which is quantified by the specific growth rate $\mu$ and the distribution of single-cell lag times $(L)$; a finite distribution parameterized by $\alpha$, within the
range $(0, d)$, is a convenient representation for prior belief concerning $L$. Note that $\alpha$ can be a set of parameters; for example, if $L$ has a one-sided truncated exponential distribution $(0<L \leq d)$, then $\alpha$ is the set containing both $d$ and the exponential rate. We reexpress equation 1 as

$$
p\left(t_{b} \mid \mu, \theta, \alpha\right)=p(0)\left(L_{0}\right)+\sum_{n=1}^{\infty} p(n)\left[\frac{\ln \left(N_{b}\right)}{\mu}-\frac{\ln (n)}{\mu}+K_{n}\right]
$$

where $L_{0}$ is a delta function at a $t_{b}$ of $d\left\{p\left[L_{0}\left(t_{b}=d\right)\right]=1\right\}$. We introduce $t_{c}$ as the duration of the Bioscreen experiment, and if a population of size $N_{b}$ had been established before or at $t_{c}$, in each well, the observed time taken to establish this population is equal to $t_{b}$. If a population with size $N_{b}$ has not been established at time $t_{c}$, then $t_{b}$ is uniformly distributed between $t_{c}$ and $d$.

This provides a complete prescription for the estimation of the Bayesian posterior distribution for $L$ based on a Bioscreen observation (i.e., values for $t_{b}$ ). The posterior distribution is suitable for inclusion in quantitative risk assessments. Note that equations 2 to 9 are derived from equation 1.

We acknowledge support from BBSRC United Kingdom.
We thank J. Baranyi and A. Metris for their helpful discussions during the preparation of the manuscript.
