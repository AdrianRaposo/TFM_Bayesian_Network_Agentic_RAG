# ON A LEAST SQUARES ADJUSTMENT OF A SAMPLED FREQUENCY TABLE WHEN THE EXPECTED MARGINAL TOTALS ARE KNOWN 

By W. Edwards Deming and Frederick F. Stephan

1. Introduction. There are situations in sampling wherein the data furnished by the sample must be adjusted for consistency with data obtained from other sources or with deductions from established theory. For example, in the 1940 census of population a problem of adjustment arises from the fact that although there will be a complete count of certain characters for the individuals in the population, considerations of efficiency will limit to a sample many of the cross-tabulations (joint distributions) of these characters. The tabulations of the sample will be used to estimate the results that would have been obtained from cross-tabulations of the entire population. ${ }^{1}$ The situation is shown in Fig. 1 in parallel tables for the universe and for the sample. For the universe the marginal totals $N_{i .}$ and $N_{. i}$ are known, but not the cell frequencies $N_{i i}$; for the sample, however, tabulation gives both the cell frequencies $n_{i j}$ and the marginal totals $n_{i .}$ and $n_{. i}$.

In estimating any cell frequency of the universe, such as $N_{i i}$, three possibilities present themselves; from the sample one may make an estimate from the $i$ th row alone, another from the $j$ th column alone, and still another from the over-all ratio $n_{i i} / n$ : specifically, the three estimates would be $n_{i i} N_{i} / n_{i}$, $n_{i j} N_{. i} / n_{. i}$, and $n_{i i} N / n$. As a result of sampling errors these will not be identical except by accident, and though any of them by itself may be considered accurate enough, still, if the whole $r \times s$ table of universe cell frequencies were so estimated, the marginal totals would not come out right. In this paper we present a rapid method of adjustment, which in effect combines all three of the estimates just mentioned, and at the same time enforces agreement with the marginal totals. The method is extended to varying degrees of cross-tabulation in three dimensions.

In any problem of adjustment where the conditions are intricate it is necessary to have a method that is straight-forward and self-checking; this becomes imperative when we realize that in the three-dimensional Case VII of the problem now at hand (vide infra), any adjustment in one cell must be balanced by adjustments in at least seven others. The method of least squares is one possible procedure for effecting an adjustment and at the same time enforcing certain conditions among the marginal totals. It is essentially a scheme for

[^0]
[^0]:    ${ }^{1}$ Examples will occur in the 1940 census publications. Further discussion of this problem and of the sampling procedure is given by the authors in "The sampling procedure of the 1940 population census," Jour. Am. Stat. Assn., Vol. 35 (1940), pp. 615-630.

arriving at a set of calculated or adjusted observations that will satisfy the conditions of the problem, and at the same time minimize the sum of the weighted squares of the residuals, symbolized as

$$
S=\Sigma w\left(n_{e}-n_{0}\right)^{2}
$$

$n_{e}$ and $n_{0}$ being the calculated and observed numbers in a cell, and $n_{e}-n_{0}$ the corresponding residual. It is the nature of the conditions imposed on the adjusted values that distinguishes one type of problem from another. Least squares has the practical advantage of uniqueness, once the weights of the observations have been assigned, and it possesses the theoretical dignity of giving one kind of "best" estimates under ideal conditions of sampling. For our present purpose we shall minimize sums of the form

$$
S=\Sigma\left(m_{i}-n_{i}\right)^{2} / n_{i}
$$

$n_{i}$ being the observed frequency in the $i$ th cell, and $m_{i}$ the calculated or adjusted frequency therein. The conditions among the $m_{i}$ will arise from the fact that the marginal totals, after adjustment, must agree with their expected values, namely, the deflated marginal totals of the universe (for example, $m_{i}$, and $m_{. i}$ as defined in eqs. (6) and (7)).

By definition, weight and variance are inversely proportional, hence the principle of least squares is identical with the minimizing of chi-square. Here the variance in the $i$ th cell is $\nu_{i}\left(1-\nu_{i} / n\right)$, where $\nu_{i}$ is the expected number in that cell, and $n$ is the total number in the sample. Now if $\nu_{i}$ is sufficiently well approximated by $n_{i}$, it follows that if no cell contains an appreciable fraction of the whole sample (a circumstance requiring a fair sized number of cells-perhaps 100), the variance may be taken as $\nu_{i}$ for every $i$, and the minimized $S$ can be used as chi-square. But regardless of the number of cells, if the $n_{i}$ be not too much different from one another, so that the factor $1-\nu_{i} / n$ may be treated as a constant, we still get the least squares solution by minimizing $S$ as defined in eq. (2).
2. The two dimensional problem. Suppose that the data on two characteristics (e.g. age and highest grade of school completed) are obtained for each member of a universe of $N$ individuals, and that tabulations of the data provide either (a) one set of marginal totals $N_{1}, N_{2}, \ldots, N_{r}$, or (b) in addition, the marginal totals $N_{.1}, N_{.2}, \ldots, N_{. s}$. The nature of the tabulations is presumed such that it is not feasible to count the numbers $N_{i j}$ in the cells, as would be done if one character were crossed with the other. Suppose, however, that for a sample of $n$ individuals selected in a random manner from the universe, the two characters are crossed with each other, so that we know not only all the $s+r$ marginal totals $n_{.1}, \ldots, n_{r}$ of the sample but also the numbers $n_{i j}$ ( $i=1,2, \cdots, r ; j=1,2, \cdots, s$ ). The problem is to estimate the unknown frequencies $N_{i j}$ in the cells of the universe. This will be done by finding the calculated or adjusted sample frequencies $m_{i j}$ and then inflating them by the inverse sampling ratio $N / n$.

For the least squares solution we seek those values of $m_{i j}$ that minimize ${ }^{2}$

$$
S=\Sigma\left(m_{i j}-n_{i j}\right)^{2} / n_{i j}
$$

wherein the $m_{i j}$ are subjected to one of the following sets of conditions:
Case I: One set of marginal totals known. Assume $N_{1 .}, N_{2 .}, \cdots, N_{r}$. to be known. Then we require

$$
\sum_{i} m_{i i}=m_{i .}, \quad i=1,2, \cdots, r
$$

These $r$ equations constitute $r$ conditions on the adjusted $m_{i j}$.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Showing the System of Notation for the Cell Frequencies and Marginal Totals of the Universe and the Sample in the Two Dimensional Problem
Case II: Both sets of marginal totals known. Here the adjusted cell frequencies must satisfy not only condition (4) but also

$$
\sum_{i} m_{i j}=m_{. j} \quad j=1,2, \cdots, s-1
$$

there being now a total of $r+s-1$ conditions. In both cases,

$$
\begin{aligned}
& m_{i .}=N_{i} \cdot n / N \\
& m_{. j}=N_{. j} n / N
\end{aligned}
$$

In other words, $m_{i .}$ and $m_{. j}$ are the deflated marginal totals, i.e., $N_{i .}$ and $N_{. j}$ divided by the actual sampling ratio $N / n$. The $m_{i .}$ and $m_{. j}$ are not independent, for

[^0]
[^0]:    ${ }^{2}$ The sign $\sum$ will denote summation over all possible cells, unless otherwise noted. $\sum$ will denote summation over all values of $i$, and similarly for an inferior $j$ or $k$. The dot, as in $n_{. i}$, will signify the result of summing the $n_{i j}$ over all values of $i$ in the $j$ th column.

$$
N_{.1}+N_{.2}+\cdots+N_{. s}=N_{1 .}+N_{2 .}+\cdots+N_{r .}=N
$$

It is for this reason that if $i$ runs through all $r$ values in eq. (4), then $j$ can run through only $s-1$ in eq. (5). A similar equation also exists for the marginal totals of the sample, namely,

$$
n_{.1}+n_{.2}+\cdots+n_{. s}=n_{1 .}+n_{2 .}+\cdots+n_{r .}=n
$$

Solution of the two dimensional Case I. Assuming that the adjusted values of the $m_{i j}$ have been found, let each take on a small variation $\delta m_{i j}$; then the differentials of eqs. (3) and (4) show that

$$
\begin{gathered}
\frac{1}{2} \delta S=\Sigma\left\{\left(m_{i j}-n_{i j}\right) / n_{i j}\right\} \delta m_{i j}=0 \quad \text { (one equation) } \\
\sum_{i} \delta m_{i j}=0, \quad i=1,2, \cdots, r \quad(r \text { equations })
\end{gathered}
$$

Multiply now eq. (11i) by the arbitrary Lagrange multiplier $-\lambda_{i}$, and add eqs. (10) and (11) to obtain

$$
\Sigma\left\{\left(m_{i j}-n_{i j}\right) / n_{i j}-\lambda_{i .}\right\} \delta m_{i j}=0 . \quad \text { (one equation) }
$$

By the usual argument, one may now set each brace equal to zero, recognizing that the $r$ Lagrange multipliers are then no longer arbitrary but must satisfy the relation

$$
m_{i j}=n_{i j}\left(1+\lambda_{i}\right)
$$

The adjusted frequencies $m_{i j}$ can be computed at once as soon as the $\lambda_{i}$. are found. To evaluate them one may rewrite the conditions (4) using the righthand member of (13) for $m_{i j}$, obtaining

$$
m_{i .}=n_{i .}\left(1+\lambda_{i .}\right)
$$

Another way to arrive at this same relation is to sum each member of eq. (13) in the $i$ th row. However obtained $\lambda_{i}$. is now known, since $m_{i}$. and $n_{i}$. are known, and in fact eq. (13) now gives

$$
m_{i j}=n_{i j}\left(m_{i .} / n_{i .}\right)
$$

The adjustment is thus a simple proportionate one by rows, the cells in any one row all being raised or lowered by the proportionate adjustment in the row total. Case I thus amounts to $r$ independent one dimensional proportionate adjustments, one for each row, and any one or all may be carried out, as desired. This result can be obtained by a simpler approach but is presented in this way for consistency with later cases.

The minimized sum of squares may be computed directly, or from the row totals by seeing that

$$
S=\sum_{i}\left(m_{i .}-n_{i .}\right)^{2} / n_{i .}
$$

The term $\left(m_{i .}-n_{i .}\right)^{2} / n_{i}$. for the $i$ th row may be considered separately, and

used as $\chi^{2}$ with $s-1$ degrees of freedom, or all rows may be combined into the minimized $S$ as given in eq. (16), and used as $\chi^{2}$ with $r(s-1)$ degrees of freedom.

Solution of the two dimensional Case II. In addition to eqs. (11) we now have also

$$
\sum_{i} \delta m_{i j}=0 \quad j=1,2, \cdots, s-1
$$

which comes by differentiating eqs. (5). By addition of eqs. (10), (11), and (17), after multiplying eq. (11i) by $-\lambda_{i}$, and eq. (17j) by $-\lambda_{. j}$, we obtain

$$
\Sigma\left\{\left(m_{i j}-n_{i j}\right) / n_{i j}-\lambda_{i .}-\lambda_{. j}\right\} \delta m_{i j}=0
$$

Equating each brace to zero, as before, we find that

$$
m_{i j}=n_{i j}\left(1+\lambda_{i .}+\lambda_{. j}\right)
$$

wherein $\lambda_{. s}$ is to be counted 0 . The adjustment is now no longer proportionate by rows, but involves every cell.

To evaluate the Lagrange multipliers in eq. (19) we may sum the two members downward and across in Fig. 1 and obtain the $r+s-1$ normal equations

$$
\begin{array}{ll}
n_{i .} \lambda_{i .}+\sum_{i} n_{i j} \lambda_{. j}=m_{i .}-n_{i .}, & i=1,2, \cdots, r \\
\sum_{i} n_{i j} \lambda_{i .}+n_{. j} \lambda_{. j}=m_{. j}-n_{. j}, & j=1,2, \cdots, s-1
\end{array}
$$

These can be reduced for numerical computation. The top row solved for $\lambda_{i}$. gives

$$
\lambda_{i .}=\left(1 / n_{i .}\right)\left\{m_{i .}-\sum_{i} n_{i j} \lambda_{. j}\right\}-1
$$

whereupon by substitution into the bottom row of eqs. (20) we arrive at the $s-1$ normal equations

$$
\begin{aligned}
& \lambda_{.1} \quad \lambda_{.2} \quad \cdots \quad \lambda_{. s-1}=1 \\
& n_{.1}-\sum_{i} \frac{n_{i 1} n_{i 1}}{n_{i .}} \quad-\sum_{i} \frac{n_{i 1} n_{i 2}}{n_{i .}} \cdots \quad-\sum_{i} \frac{n_{i 1} n_{i . s-1}}{n_{i .}}=m_{.1}-\sum_{i} \frac{n_{i 1} m_{i .}}{n_{i .}} \\
& n_{.2}-\sum_{i} \frac{n_{i 2} n_{i 2}}{n_{i .}} \cdots \quad-\sum_{i} \frac{n_{i 2} n_{i . s-1}}{n_{i .}}=m_{.2}-\sum_{i} \frac{n_{i 2} m_{i .}}{n_{i .}} \\
& n_{. s-1}-\sum_{i} \frac{n_{i . s-1} n_{i . s-1}}{n_{i .}}=m_{. s-1}-\sum_{i} \frac{n_{i . s-1} m_{i .}}{n_{i .}} \\
& 0 .
\end{aligned}
$$

Because of symmetry in the coefficients, those below the diagonal are not shown, indeed, in a systematic computation, they are not used. The 0 in the bottom

row is appended for the computation of the minimized $S$, if desired. The number of Lagrange multipliers to be solved for directly is $s-1$, and the remaining ones come by substitution into eq. (21), $\lambda_{. s}$ being counted 0 .

A simple procedure for calculating the coefficients in the normal equations (22) is to set up a preparatory table by dividing each $n_{i j}$ in the $i$ th row by $\sqrt{n_{i .}}$; also to write down $m_{i} / \sqrt{n_{i .}}$ for that row, for use on the right-hand side of the normal equations (compare Tables I and II). In machine calculation the constant divisor $\sqrt{n_{i .}}$ would be left on the keyboard until the entire $i$ th row is divided; or, if reciprocal multiplication is preferred, the multiplier $1 / \sqrt{n_{i .}}$ would be left on. From this preparatory table, the cumulation of squares and crossproducts in the vertical gives the required summations for the coefficients. The sum check would be applied in the usual manner.
3. A numerical example of the two dimensional Case II. The fact is that in practice one need not bother about forming and solving the normal equations because they will be displaced by a simplifying iterative procedure, to be explained in a later section. For illustration, however, we may do an example both ways, first using the normal equations and the adjustment (19), later on accomplishing the same results by the quicker method.

We may start with the unitalicized numbers in the $4 \times 6$ array of Table I, assuming these to be the sampling frequencies $n_{i j}$ to be adjusted. Actually, they were obtained by deflating $1 / 20$ th (for a supposed 5 per cent sample) the New England age $\times$ state table on p. 1108 of vol. 2 of the Fifteenth Census of the U.S., 1930, then varying the deflated values by chance with Tippett's numbers to get our sampling frequencies $n_{i j}$. The italicized entries in Table I represent the final (adjusted) $m_{i j}$, and it is these that we now set out to get. We start off with the sampling frequencies $n_{i j}$ and the known marginal totals $m_{.1}, m_{.2}$, etc., where $m_{i .}=N_{i .} n / N, m_{. j}=N_{. j} n / N$, as in eqs. (6) and (7). The Lagrange multipliers shown along the left-hand and top borders arise in the calculations now to be undertaken.

Table II is the preparatory table, advised at the close of the last section. It is derived from Table I by dividing the $i$ th row of sample frequencies by $\sqrt{n_{i .}}$. For example, the entry 8.64 in the cell $i=3, j=2$ comes by dividing 419 by $\sqrt{2352}, 419$ being the entry in the cell of the same indices in Table I, and 2352 being the sum of the third row. The sums at the bottom and right-hand side are for checking the formation of the normal equations. The cumulations of squares and cross-products along the vertical give the summations required for the normal eqs. (22), which now appear numerically as eqs. (23).


Performing the solution by any favorite procedure one will obtain

$$
\lambda_{.1}=.01182 \quad \lambda_{.2}=.01490 \quad \lambda_{.3}=.00119
$$

TABLE I
A table of artificial sample frequencies, an artificial 5 percent sample of native white persons of native white parentage attending school, by age by state, New England, 1930. The adjusted frequency $m_{i j}$ in each cell is shown italicized just below the corresponding sample frequency $n_{i j}$


The adjusted $m_{i j}$ (italicized) are rounded off, hence when summed may occasionally disagree a unit or so with the expected marginal totals (also italicized), the latter arise by deflation from the universe rather than by direct addition of the $m_{i j}$.
whereupon by substitution into eq. (21) comes

$$
\begin{array}{ll}
\lambda_{1 . .}=-.0146 & \lambda_{4 .}=-.0162 \\
\lambda_{2 .}=-.0003 & \lambda_{5 .}=-.0230 \\
\lambda_{3 .}=+.0234 & \lambda_{6 .}=-.0034
\end{array}
$$

The next step is to compute the $m_{i j}$ by eq. (19). Table I is now bordered with the Lagrange multipliers for a convenient arrangement of the factors required, and the calculation is completed. It will be noted that, for example

$$
m_{32}=419(1+.0234+.0149)=435
$$

The $m_{i j}$ thus calculated are shown italicized in Table I. The marginal totals, found by adding the $m_{i j}$ just calculated, do not agree exactly everywhere with the expected totals, because of rounding off to integers: the errors of closure, however, are slight, and it is a simple matter to raise or lower some of the larger cells by a unit or two to force exact satisfaction of the conditions, if this is desired.
4. The three dimensional problem. Here the $N$ cards of the universe are sorted and counted for one and perhaps a second and third characteristic, and possibly crossed by pairs in various combinations (Cases I-VII). The sample of $n$, however, is crossed by all three characteristics, which is to say that the

TABLE II
This comes by dividing each sample frequency in Table I by the corresponding $\sqrt{n_{i}}$. (This operation would ordinarily be done a row at a time)


cell frequencies $n_{i j k}$ are all known (refer to Fig. 2). As before, the adjusted frequencies are required.

Case I: One set of slice totals known. Assume the slice totals $N_{1 . .}, N_{2 . .}$, $\cdots, N_{r . .}$ to be known; the conditions are then

$$
\sum_{i k} m_{i j k}=m_{i . .}=N_{i . .} n / N \quad i=1,2, \cdots r
$$

being $r$ in number. The summation to be minimized is

$$
S=\Sigma\left(m_{i j k}-n_{j j k}\right)^{2} / n_{i j k}
$$

being similar to that in eq. (3), except that now there are three indices to be summed over instead of two. Following a procedure similar to that used before, we differentiate eqs. (27) and (28) and introduce the $r$ Lagrange multipliers $\lambda_{i}$.

with eq. (27). The steps are identical with those of the two dimensional Case I, and the result is at once

$$
m_{i j k}=n_{i j k}\left(1+\lambda_{i \ldots}\right)=n_{i j k}\left(m_{i \ldots} / n_{i \ldots}\right)
$$

This adjustment, like that shown by eq. (15), is a simple proportionate one, but this time by slices rather than by columns. All cell frequencies having the same $i$ index are raised or lowered in the same proportion.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Showing the System of Notation for the Cell Frequencies and Marginal Totals in the Three Dimensional Sample

Case II: Two sets of slice totals known. Here, in addition to the slice totals of Case I we know also

$$
N_{.1 .}, N_{.2 .}, \cdots, N_{. s .}
$$

whence arise the $s-1$ additional conditions

$$
\sum_{i k} m_{i j k}=m_{. j .}=N_{. j}, n / N, \quad j=1,2, \cdots, s-1
$$

Using the Lagrange multiplier $\lambda_{. j}$. here, and $\lambda_{i .}$. with eq. (27) as before, we find that

$$
m_{i j k}=n_{i j k}\left(1+\lambda_{i . .}+\lambda_{. j .}\right)
$$

in which $\lambda_{. s}$. is to be counted zero. This adjustment is proportionate by tubes, the ratio $m_{i j k} / n_{i j k}$ being constant along the $i j$ th tube and in fact equal to $m_{i j} . / n_{i j}$, independent of $k$. Unfortunately we do not here know the face totals $m_{i j}$. and are unable to make use of the proportionality as we shall in Case IV.

To solve for the $r+s-1$ Lagrange multipliers we sum the members of eq. (31) over $j$ and then over $i$ and arrive at the normal equations

$$
\begin{aligned}
& n_{i . .} \lambda_{i . .}+\sum_{j} n_{i j .} \lambda_{. j .}=m_{i . .}-n_{i . .}, \quad i=1,2, \cdots, r \\
& \sum_{i} n_{i j .} \lambda_{i . .}+n_{. j .} \lambda_{. j .}=m_{. j .}-n_{. j .}, \quad j=1,2, \cdots, s-1
\end{aligned}
$$

These can be reduced to $s-1$ equations in precisely the same way that eqs. (20) were reduced, but because of the iterative process to come further on, we shall not pursue the reduction here.

Case III: All three sets of slice totals known. All slice totals

$$
\begin{aligned}
& N_{.1 .}, N_{.2 .}, \cdots, N_{. s .} \\
& N_{1 . .}, N_{2 . .}, \cdots, N_{r . .} \\
& N_{. .1}, N_{. .2}, \cdots, N_{. . t}
\end{aligned}
$$

now being known, in addition to conditions (27) and (30) we require here

$$
\sum_{i j} m_{i j k}=m_{. . k}=N_{. . k} n / N, \quad k=1,2, \cdots, t-1
$$

which makes a total of $r+(s-1)+(t-1)$ or $r+s+t-2$ conditions. The same kind of manipulation as used heretofore gives

$$
m_{i j k}=n_{i j k}\left(1+\lambda_{i . .}+\lambda_{. j .}+\lambda_{. . k}\right)
$$

with $\lambda_{. s}$. and $\lambda_{. . t}$ to be counted zero. The adjustment is no longer proportionate by slices or tubes, but involves every cell. In practice, once the normal equations are solved and the Lagrange multipliers worked out, one proceeds very much as in the two dimensional Case II: for each of the $t$ slices, corresponding to the $t$ values of $k$, there will be a two dimensional adjustment, the 1 in eq. (19) being replaced now by $1+\lambda_{. . k}$.

The normal equations for the Lagrange multipliers can be found by performing double summations on eq. (34). The result is

$$
\begin{array}{ll}
n_{i . .} \lambda_{i . .}+\sum_{j} n_{i j .} \lambda_{. j .}+\sum_{k} n_{i . k} \lambda_{. . k}=m_{i . .}-n_{i . .}, & i=1,2, \cdots, r \\
\sum_{i} n_{i j .} \lambda_{i . .}+n_{. j .} \lambda_{. j .}+\sum_{k} n_{. j k} \lambda_{. . k}=m_{. j .}-n_{. j .}, & j=1,2, \cdots, s-1 \\
\sum_{i} n_{i . k} \lambda_{i . .}+\sum_{j} n_{. j k} \lambda_{. j .}+n_{. . k} \lambda_{. . k}=m_{. . k}-n_{. . k}, & k=1,2, \cdots, t-1
\end{array}
$$

If these calculations were to be carried out, one would simplify the computation by solving the top row for $\lambda_{i . .}$, getting

$$
\lambda_{i . .}=\left(1 / n_{i . .}\right)\left\{m_{i . .}-\sum_{j} n_{i j .} \lambda_{. j .}-\sum_{k} n_{i . k} \lambda_{. . k}\right\}-1
$$

and then substituting this into the middle and last rows of eqs. (35) to get a reduced set of $s+t-2$ normal equations for the Lagrange multipliers $\lambda_{. j}$. and $\lambda_{. . k}$, the numerical values of which when set back into eq. (36) give the $\lambda_{i . .}$. In all the summations of eqs. (35) and (36), $\lambda_{. s}$. and $\lambda_{. . t}$ would be counted zero. But here again, the iterative process to be explained later will displace the use of normal equations, so actually we are not interested in reducing them.

Case IV: One set of face totals known. It may be that the $r s$ face totals

$$
N_{11 .}, N_{12 .}, \cdots, N_{i j .}, \cdots, N_{r s .}
$$

are known from crossing the $i$ and $j$ characters in the universe. The conditions are then

$$
\begin{array}{ll}
\sum_{k} m_{i j k}=m_{i j .}=N_{i j .} n / N & i=1,2, \cdots, r \\
& j=1,2, \cdots, s
\end{array}
$$

The adjustment here turns out to be

$$
m_{i j k}=n_{i j k}\left(1+\lambda_{i j}\right)
$$

but by summing both sides over the index $k$ to evaluate $\lambda_{i j}$. it is seen that

$$
m_{i j .}=n_{i j .}\left(1+\lambda_{i j}\right)
$$

whence

$$
m_{i j k}=n_{i j k}\left(m_{i j .} / n_{i j}\right)
$$

This adjustment is thus proportionate by tubes, like that in eq. (31), though here the factor $m_{i j} / n_{i j}$. is known and eq. (40) can be applied at once.

Case V: One set of face totals, and one set of slice totals known. Sometimes, in addition to the $r s$ face totals of Case IV, the slice totals

$$
N_{. .1}, N_{. .2}, \cdots, N_{. . t}
$$

will also be known, in which circumstances the conditions (37) are to be accompanied by

$$
\sum_{i j} m_{i j k}=m_{. . k}=N_{. . k} n / N, \quad k=1,2, \cdots, t-1
$$

The same procedure as previously applied yields now

$$
m_{i j k}=n_{i j k}\left(1+\lambda_{i j .}+\lambda_{. . k}\right)
$$

with $\lambda_{. . t}$ to be counted zero. Summations performed over $k$, and then over $i$ and $j$ together, give the normal equations

$$
\begin{aligned}
& n_{i j .} \lambda_{i j .}+\sum_{k} n_{i j k} \lambda_{. . k}=m_{i j .}-n_{i j .} \\
& \sum_{i j} n_{i j k} \lambda_{i j .}+n_{. . k} \lambda_{. . k}=m_{. . k}-n_{. . k}
\end{aligned}
$$

The number of equations is $r s+t-1$, since $\lambda_{. . t}$ does not exist. As before, a simplification can be effected by solving the top row for $\lambda_{i j}$. and making a substitution into the lower one, but because of the great advantage of the iterative process to be seen further on, we shall not carry out the reduction.

Before going on it might be noted that although this case is three dimensional, it reduces to the two dimensional Case II if one considers that $i j$. is one index running through the values $11,12, \cdots, 21,22, \cdots, r s$, and that $\ldots k$ is a second index running through the values $1,2, \cdots, t$. This can be seen by the similarity between eqs. (43) and (20).

Case VI: Two sets of face totals known. If in addition to the face totals of Case IV, the face totals

$$
N_{.11}, N_{.12}, \cdots, N_{. s t}
$$

are also known from further crossing the $j$ and $k$ characters in the universe, we shall require

$$
\begin{array}{ll}
\sum_{i} m_{i j k}=m_{. j k}=N_{. j k} n / N, & j=1,2, \cdots, s \\
& k=1,2, \cdots, t-1
\end{array}
$$

in addition to the conditions (37). In place of eq. (40) of Case IV we now find that

$$
m_{i j k}=n_{i j k}\left(1+\lambda_{i j .}+\lambda_{. j k}\right)
$$

in which $\lambda_{. j t}$ is to be counted zero for all $j$. No simple relation such as eq. (40) is possible here, because the adjustment is not proportionate by tubes; the Lagrange multipliers must be evaluated. This can be accomplished by summing the members of eq. (45) over $k$ and $i$ in turn, resulting in the normal equations

$$
\begin{aligned}
& n_{i j .} \lambda_{i j .}+\sum_{k} n_{i j k} \lambda_{. j k}=m_{i j .}-n_{i j .} \\
& \sum_{i} n_{i j k} \lambda_{i j .}+n_{. j k} \lambda_{. j k}=m_{. j k}-n_{. j k}
\end{aligned}
$$

Since $\lambda_{. j t}$ does not exist for any values of $j$, the number of equations is $r s+s(t-1)=s(r+t-1)$. They break up at once into $s$ sets each of $r+t-1$ equations, one set for every $j$ value. In fact, the problem can be considered as $s$ sets of the two dimensional Case II. Any one value of $j$ gives a slice, which can be looked upon as fulfilling the specifications of the two dimensional Case II. Each set of normal equations can be reduced in the same manner that eqs. (20) were reduced.

Case VII: All three sets of face totals known. All totals now being known, we require

$$
\begin{array}{ll}
\sum_{k} m_{i j k}=m_{i j .}=N_{i j .} n / N, & i=1,2, \cdots, r \\
& j=1,2, \cdots, s \\
\sum_{i} m_{i j k}=m_{. j k}=N_{. j k} n / N, & j=1,2, \cdots, s \\
& k=1,2, \cdots, t-1 \\
\sum_{i} m_{i j k}=m_{i . k}=N_{i . k} n / N, & i=1,2, \cdots, r-1 \\
& k=1,2, \cdots, t-1
\end{array}
$$

The adjusting relation is

$$
m_{i j k}=n_{i j k}\left(1+\lambda_{i j .}+\lambda_{. j k}+\lambda_{i . k}\right)
$$

in which $\lambda_{. j t}$ is to be counted zero for any $j, \lambda_{r . k}$ for any $k$, and $\lambda_{i . t}$ for any $i$. The normal equations for the Lagrange multipliers are

$$
\begin{aligned}
& n_{i j .} \lambda_{i j .}+\sum_{k} n_{i j k} \lambda_{. j k}+\sum_{k} n_{i j k} \lambda_{i . k}=m_{i j .}-n_{i j .} \\
& \sum_{i} n_{i j k} \lambda_{i j .}+n_{. j k} \lambda_{. j k}+\sum_{i} n_{i j k} \lambda_{i . k}=m_{. j k}-n_{. j k} \\
& \sum_{i} n_{i j k} \lambda_{i j .}+\sum_{i} n_{i j k} \lambda_{. j k}+n_{i . k} \lambda_{i . k}=m_{i . k}-n_{i . k}
\end{aligned}
$$

being $r s+r t+s t-r-s-t+1$ in number. They can be reduced in the same way that previous normal equations have been reduced; but here again, the iterative process will render the use of normal equations unnecessary, except for theoretical purposes, e.g. justification of the iterative process.
5. A simplified procedure-iterative proportions. It is well known in least squares that the number of Lagrange multipliers in any problem is equal to the number of conditions imposed on the adjustment. Here the conditions have appeared in sets, depending on which marginal totals are involved. By a comparison of eqs. (15) and (29) on the one hand, with eqs. (19), (31), (34), (42), (45), and (48) on the other, we see that wherever there was only one set of marginal totals involved we came out with a proportionate adjustment, but that in all other cases it was not so; the Lagrange multipliers involved were unfortunately related to one another through normal equations. We now make the observation, however, that as a first approximation the adjustments may all be considered proportionate, and we shall be able to write down an expression for the error in this approximation, and shall be able to eliminate it by a succession of proportionate adjustments.

Take the two dimensional Case II for an example. In eq. (21) one may recognize $\left(1 / n_{i .}\right) \sum_{j} n_{i j} \lambda_{. j}$ as a weighted average of $\lambda_{. j}$ for the $i$ th row. There will be a weighted average of $\lambda_{. j}$ for the first row, another for the second, etc., one for each value of $i$; consequently one may appropriately speak of the $i$ th

average of $\lambda_{. i}$, writing it $i$-av. $\lambda_{. i}$. Substituting from eq. (21) into (19) one then sees the adjustment (19) appear as

$$
m_{i j}=n_{i j}\left(m_{i .} / n_{i .}+\lambda_{. j}-i-\mathrm{av} . \lambda_{. j}\right)
$$

If, on the other hand, $\lambda_{. j}$ had been eliminated from eqs. (20), instead of $\lambda_{i}$, the result would have been

$$
m_{i j}=n_{i j}\left(m_{. j} / n_{. j}+\lambda_{i .}-j-\mathrm{av} . \lambda_{i .}\right)
$$

From either eq. (50) or (51) it is clear why the adjustment (19) is not proportionate by rows or columns, and why Case II does not break up into $r$ or $s$ sets of Case I: the reason is that $\lambda_{. j}$ in any cell is not necessarily equal to the average $\lambda_{. j}$ for that row, nor is $\lambda_{i}$. in any cell necessarily equal to the average $\lambda_{i}$. for that column. If nevertheless one were to make the simple proportionate adjustment

$$
m_{i j}^{\prime}=n_{i j}\left(m_{i .} / n_{i .}\right)
$$

along the horizontal in the $i$ th row, the horizontal conditions (4) will be enforced but not the vertical ones (5); i.e., it will be found that $m_{i .}^{\prime}=m_{i}$, but that usually not all $m_{. j}^{\prime}=m_{. j}$. This is because eq. (52) effects only a partial adjustment, each $m_{i j}^{\prime}$ being in error through the disparity between the $\lambda_{. j}$ proper to the $j$ th column, and the average of all the $\lambda_{. j}$ for the $i$ th row, as seen in eq. (50). This error can then be diminished by turning the process around and subjecting these $m_{i j}^{\prime}$ to a proportionate adjustment in the vertical according to the equation

$$
m_{i j}^{\prime \prime}=m_{i j}^{\prime}\left(m_{. j} / m_{. j}^{\prime}\right)
$$

which may be considered an application of eq. (51) wherein the disparity between any $\lambda_{i}$. and the average $\lambda_{i}$. for the $j$ th column has been neglected. It is the vertical conditions that will now be found satisfied, but perhaps not all of the horizontal ones, because some of the row totals may have been disturbed. The cycle initiated by eq. (52) is therefore repeated, and the process is continued until the table reproduces itself and becomes rigid with the satisfaction of all the conditions, both horizontal and vertical. The final results coincide with the least squares solution, which is thus accomplished without the use of normal equations.

Usually two cycles suffice. In practice the work proceeds rapidly, requiring only about one-seventh as much time as setting up the normal equations and solving them. The tables III-V show the various stages of the work when the method of iterative proportions is applied to the sample frequencies of Table I. It will be noticed that the results of the third approximation (Table V) are final, since if the process were continued, the table would only reproduce itself.

The same process can be extended to three or more dimensions with an even greater relative saving in time. To see how the method of iterative proportions

applies in one of the three dimensional cases, we may go back to Case III. By the substitution afforded through eq. (36) the adjusting eq. (34) may be put into the form

TABLE III
The method of iterative proportions applied to the data of Table I. First stage: A proportionate adjustment by rows by eq. (52). Note that $m_{i}^{\prime}=m_{i}$, , but that $m_{. j}^{\prime} \neq m_{. j}$


TABLE IV
A continuation of the process initiated in Table III. The figures in Table III are now adjusted proportionately by columns according to eq. (53). The vertical totals $m_{. j}^{\prime \prime}$ and $m_{. j}$ now are equal, but the agreement of the horizontal totals accomplished in Table III has been slightly disturbed


$$
m_{i j k}=n_{i j k}\left(m_{i . .} / n_{i . .}+\lambda_{. j .}+\lambda_{. . k}-i \text {-av. } \lambda_{. j .}-i \text {-av. } \lambda_{. . k}\right)
$$

Equally well it could have been written

$$
m_{i j k}=n_{i j k}\left(m_{. j} / n_{. j .}+\lambda_{i . .}+\lambda_{. . k}-j \text {-av. } \lambda_{i . .}-j \text {-av. } \lambda_{. . k}\right)
$$

or

$$
m_{i j k}=n_{i j k}\left(m_{. . k} / n_{. . k}+\lambda_{i . .}+\lambda_{. j .}-k-a v . \lambda_{i . .}-k-a v . \lambda_{. j .}\right)
$$

Any of these three equations shows why the adjustment (34) is not proportional by slices, and why this case does not break up into $r$ or $s$ or $t$ sets of the three dimensional Case I. As a first approximation it does, as is now clear from these three equations, and by making successive proportionate adjustments we may thus arrive at the least squares values. To go about the work we could first calculate the values of

$$
m_{i j k}^{\prime}=n_{i j k}\left(m_{i . .} / n_{i . .}\right)
$$

then

$$
m_{i j k}^{\prime \prime}=m_{i j k}^{\prime}\left(m_{. j} / m_{. j}^{\prime}\right)
$$

# TABLE V 

The cycle is commenced again. The figures of Table IV are subjected to a proportionate adjustment by rows, according to eq. (52). And since these results turn out to be almost a reproduction of Table IV but with both horizontal and vertical conditions satisfied, they are considered final. The agreement with the $m_{i j}$ in Table I should be noted


followed by

$$
m_{i j k}^{\prime \prime \prime}=m_{i j k}^{\prime \prime}\left(m_{. . k} / m_{. . k}^{\prime \prime}\right)
$$

These three successive adjustments would constitute a cycle, which would then be repeated in whole or in part until the table becomes rigid with the satisfaction of all three sets of conditions.
6. Simplification when only one cell requires adjustment. On occasions it happens in sampling work that one is especially interested in one particular cell of the universe, and would like to have a result for it in advance before the other cells are adjusted. Sometimes it even happens that the others individually are of no particular concern. In such circumstances one merely places the cell

of interest in one corner of the table by an appropriate interchange of rows and columns, and then compresses the rest of the table into the cells adjacent to it. In the two dimensional Case II one would thus work with a $2 \times 2$ table, one corner cell being the one of special interest, the other three being the result of compression. The marginal totals of the row and column belonging to the cell of interest are unaffected. For illustration we may suppose that from the sample shown in Table I we require only $m_{61}$. We then start with the $2 \times 2$ Table VI, which is derived from Table I by compression. Commencing with Table VI, one might first adjust by rows according to eq. (52), then by columns by eq. (53). One cycle of iterative proportions is sufficient, as is seen in Table

TABLE VI
Derived from Table I by compression, the cell $i=6, j=1$, requiring adjustment


TABLE VII
A proportionate adjustment of Table VI
Rows adjusted by eq. (52)


Columns adjusted by eq. (53)


Conclusion: $m_{61}=3915$

VII, and the value 3915 found for $m_{61}$ is in good agreement with its value shown in Tables I and V. The scheme of compression provides a quick method of getting out an advance adjustment for a cell of special interest, and the result so obtained will ordinarily be in good agreement with what comes later when and if all the cells are adjusted.

In the three dimensional Cases II, III, V, VI, and VII, one compresses the original table to a $2 \times 2 \times 2$ table, and then uses the method of iterative proportions. (The other cases do not require consideration, since they are proportionate adjustments wherein one is already at liberty to adjust as few or as many cells as he likes without altering the equations or the routine.) The same procedure can be extended to the adjustment of two cells, the only modification

being that in two dimensions we shall compress to a $2 \times 3$ or a $3 \times 3$ table, depending on whether the two cells do or do not lie in the same row or column. In three dimensions we compress to a $2 \times 2 \times 3$, or a $2 \times 3 \times 3$, or a $3 \times 3 \times 3$ table; the first if the two cells lie in the same $i, j$, or $k$ tube, the second if they lie in the same slice but not in the same tube, the third if they are in separate slices.
7. Some remarks on the accuracy of an adjustment. A least squares adjustment of sampling results must be regarded as a systematic procedure for obtaining satisfaction of the conditions imposed, and at the same time effecting an improvement of the data in the sense of obtaining results of smaller variance than the sample itself, under ideal conditions of sampling from a stable universe. It must not be supposed that any or all of the adjusted $m_{i j}$ in any table are necessarily "closer to the truth" than the corresponding sampling frequencies $n_{i j}$, even under ideal conditions. As for the standard errors of the adjusted results, they can easily be estimated for the ideal case by making use of the calculated chi-square. For predictive purposes, however (which can be regarded as the only possible use of a census by any method, sample or complete), it is far preferable, in fact necessary, to get some idea of the errors of sampling by actual trial, such as by a comparison of the sampling results with the universe, as can often be arranged by means of controls. There is another aspect to the problem of error-even a 100 per cent count, even though strictly accurate, is not by itself useful for prediction, except so far as we can assert on other grounds what secular changes are taking place.

In conclusion it is a pleasure to record our appreciation of the assistance of Miss Irma D. Friedman and Mr. Wilson H. Grabill for putting the formulas and procedure into actual operation with census data, and thereby disclosing defects in earlier drafts of the manuscript.

Bureau of the Census,
Washington