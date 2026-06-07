# HHS Public Access 

Author manuscript
IEEE Trans Med Imaging. Author manuscript; available in PMC 2016 August 24.
Published in final edited form as:
IEEE Trans Med Imaging. 2015 July ; 34(7): 1549-1561. doi:10.1109/TMI.2015.2405341.

## 3-D Stent Detection in Intravascular OCT Using a Bayesian Network and Graph Search

## Zhao Wang,

Department of Biomedical Engineering, Case Western Reserve University, Cleveland, OH at the time of this work. He is now at Massachusetts Institute of Technology, Cambridge, MA

Michael W. Jenkins,
Department of Biomedical Engineering, Case Western Reserve University, Cleveland, OH

## George C. Linderman,

Department of Biomedical Engineering, Case Western Reserve University, Cleveland OH at the time of this work. He is now at Yale University, New Haven, CT

Hiram G. Bezerra,
Harrington Heart and Vascular Institute, University Hospitals Case Medical Center, Cleveland, OH

## Yusuke Fujino,

Harrington Heart and Vascular Institute, University Hospitals Case Medical Center, Cleveland, OH

## Marco A. Costa,

Harrington Heart and Vascular Institute, University Hospitals Case Medical Center, Cleveland, OH

## David L. Wilson, and

Department of Biomedical Engineering, Case Western Reserve University, Cleveland, OH

## Andrew M. Rollins

Department of Biomedical Engineering, Case Western Reserve University, Cleveland, OH


#### Abstract

Worldwide, many hundreds of thousands of stents are implanted each year to revascularize occlusions in coronary arteries. Intravascular optical coherence tomography (OCT) is an important emerging imaging technique, which has the resolution and contrast necessary to quantitatively analyze stent deployment and tissue coverage following stent implantation. Automation is needed, as current, it takes up to 16 hours to manually analyze hundreds of images and thousands of stent struts from a single pullback. For automated strut detection, we used image formation physics and machine learning via a Bayesian network, and 3-D knowledge of stent structure via graph search. Graph search was done on en face projections using minimum spanning tree algorithms. Depths of all struts in a pullback were simultaneously determined using graph cut. To assess the method, we employed the largest validation data set used so far, involving more than 8,000 clinical images from 103 pullbacks from 72 patients. Automated strut detection achieved a $0.91 \pm 0.04$ recall, and


[^0]
[^0]:    Personal use of this material is permitted. However, permission to use this material for any other purposes must be obtained from the IEEE by sending a request to pubs-permissions@ieee.org
    Correspondence to: Andrew M. Rollins.

$0.84 \pm 0.08$ precision. Performance was robust in images of varying quality. This method can improve the workflow for analysis of stent clinical trial data, and can potentially be used in the clinic to facilitate real-time stent analysis and visualization, aiding stent implantation.

# Index Terms 

Bayesian methods; graph search; optical coherence tomography; stent

## I. INTRODUCTION

Every year, hundreds of thousands of patients with coronary artery diseases in the US are treated with intravascular stents. Improper deployment of stents and resulting tissue responses (e.g. delayed heating) are associated with stent thrombosis, which is a lifethreatening complication [1]. Intravascular optical coherence tomography (OCT) [2] is a catheter-based optical imaging technique that can provide 3-D images of coronary arteries with very high resolution ( $10-20 \mu \mathrm{~m}$ ). OCT has demonstrated significant advantages in strut coverage analysts due to better resolution and contrast compared to the alternative technology, intravascular ultrasound (IVUS) [3], which has a resolution about 100-200 $\mu \mathrm{m}$. For clinical intravascular OCT imaging, one pullback typically contains hundreds of crosssectional images. Metallic stents strongly reflect tight and manifest as bright reflections coupled with dark shadows in OCT images (Fig. 1). This signature allows for accurate stent strut ${ }^{1}$ assessment. They may also exhibit other signatures in cases of very thick neointima coverage [4]. Stent analysis in OCT images is extremely time-consumming. To compute quantitative metrics, such as stent area and strut coverage, analysts must manually mark every strut in individual frames (Fig. 1). Given that a single pullback contains hundreds or even thousands of stent struts, it usually takes up to 16 hours for an expert analyst to manually analyze all the struts from all the frames based on our experience (the analysis time may differ depending on the complexity of analysis and experience of analysts). Automated detection of stents could greatly alleviate this burden on analysts and reduce inter-observer variability. This will benefit offline analysts of large clinical trials of new stent designs and facilitate live-time feedback during stent deployment for potential support of treatment decisions.

Several studies on metallic stent detection in OCT images have been recently reported [413]. While differing in specific methods, studies [5-8,11] have employed single A-line analysts or 2-D edge detections to capture the signatures of individual struts (i.e. bright reflections and shadows). Later studies have used feature extraction and classification techniques to facilitate stent detection. Tsantis et al [9] applied probabilistic neural networks to detect stent struts based on a variety of strut features extracted using continuous wavelet filters. However, as this study used images acquired from femoral arteries, the performance of the method in clinical intracoronary OCT imagers is unknown. A later study by Mandelias et al [12] extended the wavelet based detection method and achieved higher

[^0]
[^0]:    ${ }^{1}$ In the literature, each Intersection of a stent wire with an image is described as a "strut." To limit confusion, we continue this convention. We refer to stent wire or mesh for the larger construct.

accuracy and shorter processing time. However, the validation data size is small (4 pullbacks). Lu et al [10] applied bagging decision trees as the classifier on an initial screen of candidate struts, and achieved promising results in a moderately sized validation set. Such classification-based methods can take advantage of human expert knowledge, and can easily combine multiple features for decision-making, and are therefore potentially more robust. Xu et al. [4] focused on a restricted category of cases where stent struts lacked the typical bright spot and shadow appearance, but instead appeared as elongated ridges due to very thick tissue coverage. Therefore, a 2-D ridge detector was proposed [4]. All of these studies have used local image features of individual "struts" (see footnote ${ }^{1}$ ) for detection, without consideration to continuity of stent wires or the 3-D cylindrical shape of stents. Validation studies of most of these methods have been typically conducted employing less than 20 pullbacks. Although promising results have been achieved in the limited data sets selected in these studies, the generality of these methods to large clinical data sets have not been demonstrated.

Stents typically have regularized structures (Fig. 1) and knowledge of their 3-D structure can potentially aid stent analysis, especially in instances of stent struts with unclear signatures due to imaging physics or artifacts (Fig. 1). Although there have been no direct 3-D stent detection methods proposed for intravascular OCT, methods to reconstruct 3-D stents and to quantify the stent cell size were proposed by Gurmeric et al [6] and Wang et al [13]. There have been studies making use of 3-D image data for stent detection and analysis outside the OCT regime. The number of studies is very limited, mainly due to the inability of other imaging modalities to capture coronary stents in sufficient detail. For example, Klein et al. [14] proposed a method for automatic segmentation of stents in Computed Tomography (CT) images for endovascular aortic replacement, structures much larger than coronary stents. In this method, Dijkstra's shortest path algorithm [15] was used to link automatically generated seed points on the stent graft. However, as the seed points were connected in an uncontrolled manner, many false edges could be generated, and ad hoc heuristics were added to remove these false edges.

In this study, we propose a new method for stent detection in OCT images. We focus on metallic stents with a shadow signature in OCT images. Methods for detecting stents without such a signature are beyond the scope of this study and can be found elsewhere [4, 12]. Our goal is to create a method which will perform robustly with images encountered in the clinical environment. To achieve robustness, we used some approaches novel to stent analysis. First, we used a Bayesian network based upon physical principles of OCT imaging and computed a probability of stent strut appearance in an A-line. Second, we exploited stent wire continuity from adjacent frames and proposed a novel method based on graph algorithms to detect the stent strut locations in an en face view. Finally, we considered the physical stent model and localized the depths of all the stent struts in a pullback simultaneously using a graph cut algorithm. In the next section, we describe the algorithms in detail. Then, we describe the validation experiments, and analyze results of the comparison with human experts.

## IL ALGORITHMS

The major steps of our method are illustrated in Fig. 2. First, each A-line is assigned a probability for strut presence using a Bayesian approach. The strut depth is roughly estimated for probabilistic inference of strut presence. In the second stage. strut A-line positions are reinforced using 3-D stent mesh information. Third, the exact depth locations of all struts in a pullback are simultaneously determined, making use of 3-D information. In the following sections, we introduce the details of each stage of the method.

## A. Image Preprocessing

All OCT images used in this study were acquired by commercial Fourier Domain OCT systems (C7-XR™ OCT Intravascular Imaging System, St. Jude Medical Inc., St. Paul, Minnesota). This OCT system has an axial resolution of ~15μm and a transversal resolution of ~30μm. The scan characteristics of the system are: 50,000 lines/s, 504 lines/frame, yielding 100 fps and 20 mm/s pullback speed yielding a 200 μm frame interval.

Intravascular OCT images are naturally acquired in polar coordinates. We use r and θ to represent the axial (depth) and angular coordinate of each A-line respectively. The OCT raw data were logarithmically compressed and normalized to the range of 0--1 and operated upon in polar coordinates (θ, r). Calibration was performed by adjusting the z-offset according to a priori knowledge of the catheter size [2]. The luminal boundary of the vessel, and guide wire artifacts were robustly identified using a dynamic programming algorithm described previously [16, 17]. The luminal boundary information is used m subsequent stent detection.

## B. Probabilistic Detection of Strut Positions Using a Bayesian Network

The first stage is to detect A-lines in angle θ containing stent struts. After this stage, each Aline is given a probability of strut presence, and this probabilistic output is utilized in the next stage of the algorithm. As metallic stent struts strongly reflect light, each strut casts a dark shadow in the (θ, r) image (Fig. 3). We project the 2-D polar coordinate image into one dimension (Fig. 3(b)) by averaging intensity values along each A-line between the lumen and a depth of 1.5 mm, the nominal imaging depth in OCT. Strut locations correspond to local minima in this curve. Several previous studies also utilized projected A-lines for strut detection [6, 7, 18], but the specific methods are different from the probabilistic method described below.

We consider physical principles in the detection of struts in the 1-D projection curve. Only some local minima are caused by struts. Others are from artifacts or tissue intensity differences between adjacent A-lines. We define the relative difference between adjacent peak and valley points to be shadow contrast (SC). Based upon physics and observation, we determine that the magnitude of SC depends on the distance from the catheter to the lumen wall (represented by dist) and by the thickness of the tissue covering the strut (represented by depth). When the lumen boundary is far from the catheter (high dist), signal intensity drops as the beam is out of focus. For deeply embedded struts (high depth), there is more signal accumulated from tissue superficial to the strut. In both cases, SC will be smaller.

We can model these cause-effect relationships using a Bayesian network [19--21] as shown in Fig. 3(d). It encodes the causal dependencies between variables, and more importantly, compactly represents the full joint probability distribution defined by all the variables. For example, in Fig. 3(d), the arrows link the causes (also parents) dist and depth to the effect (also child) SC, and this is consistent with our discussions above. The node SC also encodes the conditional probability P(SC|dist, depth). For baseline cases where the OCT is performed immediately after stent implantation, there will be no tissue covering the struts, so the network can be simplified by not considering the strut depth. The time of stent implantation is recorded in the database and is readily available. This information could be used to select the Bayesian network structure.

Formally, a Bayesian network is a directed acyclic graph (DAG) in which each node X has a conditional probability distribution P(X|Parents(X)) that quantifies the effect of the parents on the node. An important feature of a Bayesian network is that each variable is independent of its nondescendants given its parents. Given some observed variables and known conditional probabilities, we can find the posterior probabilities of the unknown variables using probability theory.

In the stent detection problem defined in Fig. 3, our task is to query the probability of strut presence among all the peaks given our observations. We can directly observe the values of SC and dist. We can also estimate the probability of strut presence, P(strut), and P(SC|dist, depth) from manually analyzed training data. As SC, dist and depth are continuous variables, we can discretize them into bins to generate the conditional probability tables (for depth we include an additional value undefined to make it compatible with presence of no strut). Note that the strut depth is a latent variable because struts are not yet detected. According to probability theory, we can directly query the probability of strut presence P(strut|SC, dist) given values of SC and dist, by marginally summing over all the possible depths a strut could occupy: where strut is a binary variable present or not present. However, we have found that such an approach is noisy for strut not-present and ambiguous strut positions. On the other hand, the strut depth is well-defined in high confidence strut A-lines with a reflection-shadow appearance. Since adjacent struts are likely to be embedded at similar depths below the tissue (Figs. 1, 3), we can use high confidence strut depths to estimate the depths in surrounding locations. Based on these considerations, we decided to adopt the following algorithm in which we first get a quick estimate of strut depth and then improve estimates of the probability of strut presence and strut depth in subsequent steps.

# Algorithm ESTIMATE-STRUT-PRESENCE 

Step 1: Roughly estimate the strut depth bin for each of the peaks in the 1-D projection (i.e. suspected struts) using maximum likelihood estimation (MLE):

$$
\text { depth }_{M L E}=\underset{\text { depth }}{\arg \max } P(S C \mid \text { dist, depth })
$$

Step 2: Identify high confidence struts by estimating $P($ strut $\mid S C$, dist $)$ and selecting only the peaks that are associated with high probability (e.g. $\mathrm{P}=0.7$. We have found that the threshold value of $0.6-0.8$ has little effect on the final output of the algorithm. But a further aggressive value $0.8-1$ or $<0.6$ may generate significant errors) of strut presence. Notice that we can now treat strut depth as a deterministic variable by using the estimated depth bin from Step 1. Equation (1) can now be evaluated using the equations below.

$$
\begin{aligned}
& P(\text { strut } \mid S C, \text { dist })=\frac{P(S C, \text { dist, depth }_{M L E}, \text { strut })}{\sum_{s t r u t} P(S C, \text { dist, depth }_{M L E}, \text { strut })} \\
& =\frac{P(S C \mid \text { dist, depth }_{M L E}) P(\text { dist }) P\left(\text { depth }_{M L E} \mid \text { strut }\right) P(\text { strut })}{\sum_{s t r u t} P(S C \mid \text { dist, depth }_{M L E}) P(\text { dist }) P\left(\text { depth }_{M L E} \mid \text { strut }\right) P(\text { strut })} \\
& =\frac{P(S C \mid \text { dist, depth }_{M L E}) P\left(\text { depth }_{M L E} \mid \text { strut }\right) P(\text { strut })}{\sum_{s t r u t} P(S C \mid \text { dist, depth }_{M L E}) P\left(\text { depth }_{M L E} \mid \text { strut }\right) P(\text { strut })}
\end{aligned}
$$

Step 3: Determine strut depths of high-confidence struts identified in Step 2, and use these high-confidence depth locations to interpolate strut depths for other suspected struts in the 1D projection curve. The refined strut depth is determined by searching the A-line within the depth bin found in Step 1 for the point $r^{*}$ that optimizes an objective function associated with strut features. For a given point $r$ we use a linear objective function that models the strut presence by combining the features of bright strut reflection, low intensity shadow and high gradient at the strut-shadow transition

$$
f_{r}=S_{r}+\mu I_{r}+\lambda M_{r}
$$

where $S_{r}$ is the slope of the A-line segment $L_{r}$ following $r$ to greater depths in the tissue. $L_{r}$ is selected to be $70 \mu \mathrm{~m}$ long to cover the transition between the bloom and the shadow. This bright-to-dark signature is the convolution of the point spread function of the laser spectrum and the edge of the strut surface and is relatively consistent. $I_{r}$ is the intensity at $r, M_{r}$ is the mean intensity of the A-line segment ( $500 \mu \mathrm{~m}$ long) after $L_{r}$ representing the intensity of the shadow. Variables $\mu$ and $\lambda$ are weights determined using methods described in Section III C. Choosing a longer or shorter segment of shadow to estimate its mean intensity may also be valid but the corresponding optimal values of $\mu$ and $\lambda$ may be different. It should be noted that Eq. (4) also applies to struts with only a shadow signature (no bright reflection) due to

the term S_{r} and M_{r}. From the determined high confidence struts, a virtual stent contour is generated by interpolation (interpolation uses the same method as in stent area quantification and will be discussed in detail in Section II E). The depths of all other suspected struts are simply the intersection between the virtual stent contour and the strut A-lines. For those images where there are no high-confidence struts, Steps 3 and 4 are not executed and the result from (3) will be directly used.

Step 4: Determine the final estimated probability P(strut\SC, dist) using (3) with the updated depth information found in Step 3 for all suspected struts.

In summary, for a given new local minimum from the 1-D A-line projections, we obtain SC and dist directly and estimate depth from (2) based on pre-learned probabilities P(SC\dist, depth) from training data. We then update the estimate of strut depth in Steps 2 and 3 by combining information from within the A-line and from adjacent struts. Finally, we determine the final probability of strut presence in the A-line using (3) and the updated depth. This is similar to the expectation-maximization algorithm [22] but with the incorporation of application-specific knowledge. Thus at the end of this stage of the algorithm, we have identified all A-lines in the pullback that apparently contain stent struts and a probability is given to each identified strut location.

## C. En face reinforcement of strut locations

In this stage of the algorithm, stent wire continuity is used to reinforce possible stent strut positions obtained from the probabilistic network in the first stage, and to capture some ambiguous struts that would be missed using only single frame processing. The reinforced strut A-lines from the output of this step will be used as the input to the next stage of the algorithm in Section II D. Our approach uses all the 1-D projections computed as above, over all of the frames in the stented region of the pullback. The result is a 2-D en face image as shown in Fig. 4, displayed as a function of pullback distance and θ, giving an image as though the vessel was cut open longitudinally, flattened, and projected to the viewer. It should be noted that the en face projection view has a distorted geometry because the stent mesh further away from the catheter has a larger circumferential dimension per unit angle. Moreover, longitudinal motion can also be observed in Fig. 4 in that the stent cell becomes larger if the relative pullback speed is slower (e.g. due to non-uniform pullback or cardiac motion). However, it is clear from Fig. 4 that the global structure of the stent mesh is well preserved showing well-organized and repeated units. The key idea is to segment the stent mesh in this view. The high probability struts determined from Section II B are utilized as seed points for stent mesh segmentation as illustrated in detail later. This approach incorporates 3-D information of stent mesh structure, and it utilizes such information efficiently, i.e. instead of processing the whole 3-D image stack, we only need to process a single en face projection image to determine strut locations in the entire pullback.

A potential problem with this approach is that, although the number of most commonly used stent types in US clinics is limited, there are actually more than 100 different stent designs (Fig. 1) in the current global market. There will certainly be more in the future. The resulting appearance of stent mesh in the en face projection view may have a plethora of possible

patterns depending on the stent design (e.g. Fig. 1). Therefore, a stent segmentation method may not generalize well if it makes too strong an assumption about the mesh shape of a stent. An attractive strategy is to use a "model-free" method that works well regardless of what type of stent is implanted. Here, we propose such a method based on the minimum spanning tree (MST) technique from graph theory.

Consider an undirected graph $G=(V, E)$ with vertices (nodes) $V$ and edges $E$. We construct such a graph with each vertex consisting of a pixel in the en face projection image, and with each edge defined by a connection between two pixels, as obtained in an 8-neighbour system. With edge weights equal to the average intensity of the two pixels in the en face projection image, a connected subgraph with low total edge weights will tend to trace out the dark stent wires. In graph theory, MST is a subgraph that connects every vertex with a total weight minimizing all possible spanning trees. Suppose we have found some seed points along the stent mesh, and we want to connect them, a MST can generate a unique path between seed points and this path is very likely to follow the stent mesh where intensity is low. From the probabilistic output given in Section II B, we can easily generate seed points by applying a high confidence threshold. Here we use $\mathrm{P}>0.7$. Hence, using MST, we can record the paths linking seed points, and combine all the paths to get the stent mesh.

However, MST alone does not generate a complete stent mesh because the stent mesh can have cycles, which are not possible with a MST. Therefore, we adopt a rescue procedure to make the resulting stent into a complete mesh. If two leaf nodes (i.e. nodes with no children) of the path recorded with MST are circumferentially adjacent and connected in another nonshortest path, we connect them using Dijkstra's shortest path algorithm [15] in which the low intensity stent mesh is again very likely to be covered. We have found that a reasonable heuristic to select the circumferentially adjacent region for two leaf nodes is to check whether they are within a 35-degree (circumferentially) by 3-frame (longitudinally) rectangular region.

Formally, we define $S$ as the set of seed points, edge weight $w(u, v)$ as the average intensity of $u$ and $v, \Pi[v]$ as the parent of $v$ in the tree, key $[v]$ as the minimum weight of any edge connecting $v$ to a vertex in the tree, $Q$ as a min-priority queue to store the unvisited vertices, $r$ as any seed point chosen to be the starting point, $P$ to store the path we found, $L[s]$ to indicate whether the seed point is a leaf $(L[s]=1)$. We use the following algorithm modified from Prim's MST algorithm [23]:

```
Algorithm MST-STENT
    Initialize: \(\Pi[v] \leftarrow 0, \operatorname{key}[v] \leftarrow \infty: \forall v \in V, Q \leftarrow V(G), P \leftarrow\) empty, \(L[s] \leftarrow 1: \forall s \in S\), key \([r] \leftarrow 0\)
    while \(Q\) is not empty
        Extract \(u\) from \(Q\)
        for each \(v\) in \(Q\) adjacent to \(u\)
            if \(w(u, v)<\operatorname{key}[v], \Pi[v] \leftarrow u, \operatorname{key}[v] \leftarrow w(u, v)\)
            if \(v \in S\)
            Back track \(v\) until reach another seed point \(s^{\prime}\), add the path in \(P\)
            \(L\left[s^{\prime}\right] \leftarrow 0\)
```

9 for all the leaves found $m$ MST
10 if there is no path in $P$ within the circumferentially adjacent region between two leaf nodes
11 Link them using Dykstra's shortest path algorithm and add the path in $P$
12 return $P$

Line 2-5 are a straightforward implementation of Prim's algorithm. Briefly, all the unvisited vertices are stored in a min-priority queue with respect to their key values. During each loop, the tree grows by adding the edge with the minimum weight connecting the existing tree to an unvisited vertex and the path is stored. Line 6-8 connects the currently visited seed point to a previously found seed point according to the stored path. In line 7, $s^{\prime}$ always exists because Prim's algorithm maintains a single tree. We start from one of the seed points, the root. In the worst case, $s^{\prime}$ will be the root. When the major loop (lines 2-8) is completed, there will be a MST and an intermediate stent mesh stored in $P$ connecting all of the seed points. The loop 9-11 implements the rescue operation whereby we fill in the missing wires in the stent mesh.

In practice, the intermediate stent mesh path might have traversed artifactual regions where the cost just happens to be low. This can usually be avoided by segmenting the artifactual regions and assigning zero cost to those regions before running the MST-STENT algorithm and removing the regions in the segmented stent mesh. Most commonly, this problem arises at vessel side branches (Fig. 4), which tend to be dark, bulky regions in the en face projection image. We exclude side branches before running MST-STENT using the following simple method. We threshold the en face projection image with a cut-off value given from the mean intensity of regions occupied by seed points. A region is identified as a side branch if its area is larger than a pre-defined threshold (here we use 20 pixels). A more principled method will be investigated in the future. Another common low intensity artifact is the guide wire-blocked region (Fig. 4). However, this is segmented during preprocessing and can be excluded from the stent mesh.

En face stent mesh detection is a high-level tool to augment the output of the probabilistic stage of the algorithm. Specifically, an initial screening of stent locations is performed by including all candidate strut locations with at least a low confidence probability ( $\mathrm{P}>0.3$ ). We then check whether these struts are part of the stent mesh found in MST-STENT. If so, we keep them; otherwise, we drop them. Combing this extra 3-D information for stent detection is potentially more robust than single frame processing.

Another benefit of en face stent mesh detection is for 3-D visualization. As the entire stent mesh can be detected, en face processing can potentially generate better 3-D visualization than using only the sparse stent struts detected in single frames. For the purpose of visualization, we simply keep all the detected strut positions on the stent mesh in the en face projection view.

# D. Simultaneous Depth Localization of All Struts 

So far, we have identified A-lines containing stent struts. The next step is to determine the precise depth location of the struts in those A-lines. The key difference between the method

presented here and previous methods is that we localize the depths of all struts simultaneously using a graph search technique, whereas previous methods detect depths one-by-one. Therefore, we again benefit from 3-D spatial information, including struts from neighboring frames. Consider that a stent is a tubular structure, which is expanded at implantation. Unless there is a rupture, a very rare event, the implanted stent will maintain its tubular shape with some deformations caused by resistance from the vessel. Choosing the centroid of the lumen as the reference point, distances to struts are not likely to vary dramatically between adjacent struts. This enforces an important hard constraint on deformation:

$$
\left|d_{j}-d_{a d j(j)}\right|<T
$$

where $d_{j}$ is the distance between a strut $j$ to the lumen centroid, and $a d j(j)$ is the set of adjacent struts to strut $j$ in 3-D space. Here, 3-D adjacent struts include the ones in the same frame and across neighboring frames. Moreover, as OCT is scanned during a pullback in a helical pattern, the last A-line of the current frame is also adjacent to the first A-line in the next frame. $T$ is the deformation constraint. If we construct a graph with each node formed by a pixel in the A-lines containing struts (termed strut line), and associate each node with the objective function $f_{r}$ given in (4), the globally optimized depths for all struts corresponds to an optimal surface under the hard deformation constraint m the 3-D OCT pullback (Fig. 5).

The optimal surface can be efficiently found using a specially constructed graph proposed by Li et al [24]. The basic idea of the method is to transform the optimal surface search problem into an equivalent minimum closure search problem (where closure indicates that successors of any node are still in the set), which can be solved using graph cut algorithms [24-27].

We transfer the problem into a minimum closure problem with the following operations: 1) In each A-line containing a strut, we change the cost of each node to the difference between the node and the node immediately below. Here the lower nodes are the pixels farther away from the lumen. 2) For each node, make an edge to the node immediately lower than the current node; further, make an edge to the farthest lower node in 3-D adjacent strut lines it could reach under the deformation constraint. These edges are assigned infinite weights and are used as "shape priors" or "hard constraints." In particular, the intra-strut-line edges will ensure that a feasible surface will intersect each A-line exactly once. The inter-strut line edges ensure that distances of adjacent struts to the lumen centroid should not differ more than T. 3) Make the lowest layer nodes strongly connected (every node is reachable from other nodes). Under these conditions, the optimal surface corresponds to the optimal closure in the graph [24].

We next solve the optimal closure problem using graph cut algorithms according to Picard [28]. Searching for the minimum cut is well studied and there are several efficient algorithms available [29, 30]. In this study, we used the maximum flow algorithm developed by Boykov and Kolmogorov [26].

# E. Quantification of Clinically Relevant Metrics 

After identifying stent strut locations in 3D, we can make various clinically relevant measurements (Fig. 6), such as stent area (the area enclosed by the stent struts in a 2D image), malapposition area (area in a 2-D image enclosed by the lumen boundary and malapposed struts), neointima area (the area enclosed by the lumen boundary and the stent struts in follow-up cases where there is tissue coverage), and strut-level measurements (individual strut coverage thickness, malapposition distance, etc.). For a more complete list of possible quantitative metrics that can be derived from the image, please refer to Tearney et al [31]. Once all the stent struts and the luminal boundary of the vessel are detected, any quantitative metrics defined above can be computed. Specifically, all area measurements rely on obtaining a virtual stent contour from detected struts. We adopt a two-step interpolation scheme to determine the stent contour. First, from detected stent struts, we generate evenlyspaced virtual, "interpolated" points between them. These virtual points are placed at a depth from the luminal boundary which is linearly interpolated in the $(\mathrm{r}, \theta)$ view from depths of adjoining struts. This process fills gaps between sparse struts. If the number of struts in the current frame is too small, there will likely be large interpolation errors. In such cases, we combine strut locations from adjacent $\pm 1$ frames for interpolation. Second, we generate the complete stent contour from both real and virtual stent struts using cubic spline interpolation with respect to the catheter center. This two-step interpolation approach is very similar to how human experts perform the task manually. Although we have described the situation at follow-up where there are mostly covered struts, the above process also works for those instances where there are malapposed struts (and therefore negative depths).

## III. EXPERIMENTAL METHODS

## A. Validation Data

The image sets used for the validation studies were collected from the database of the Cardiovascular Imaging Core Laboratory, University Hospitals Case Medical Center (Cleveland, OH). These images were collected by commercial Fourier-domam OCT systems (C7XR ${ }^{\mathrm{TM}}$, St. Jude Medical Inc., St. Paul, Minnesota), and have been previously analyzed by multiple expert analysts using commercial OCT workstations (St. Jude Medical Inc.) for other purposes. The statistics describing the validation data are listed m Table 1.

There are in total more than 8000 manually analyzed images from 103 pullbacks from 72 patients. The data are from 3 stent types. The data range from baseline to follow-up cases at different time points (note that the true number of images containing stent struts from the 103 pullbacks is more than 10,000 , but because of time constraints, not every image was analyzed by human experts). In order to represent the widest possible range of cases that may be encountered in a clinical setting, no images were excluded from the data set for any reason. In particular, in each pullback, every image that had been analyzed by human experts was included in the validation. Therefore, images with different intensity, contrast, collected by different machines and with different artifacts commonly seen in clinical imaging, were included in this large validation set.

# B. Gold standard 

For our purposes, there are two limitations of strut detection by human expert analysts (Fig. 7). First, analysts marked the front edge, instead of the center, of the strut bloom for analysis. From the perspective of OCT image formation, we know that the actual strut front surface is the center of the point spread function, and should be near the center of the bloom. (To account for this, analysts routinely add a constant offset for strut-level analyses). Nevertheless, the mark that we obtain from manually analyzed images is placed on the front of the bloom. Because of this, to determine whether an automatically detected strut and a manually detected strut coincide, we require the distance between centroids of the strut markings to be within a distance tolerance along the A-line. Using the same 342 struts of 2 pullbacks randomly selected from the validation data analyzed by two analysts with one marking the strut bloom center, and one marking the bloom front edge, we determined the distance to be $108 \mu \mathrm{~m}$, within which the two analysts reached an agreement of $99 \%$ in detecting all the struts. Second, analysts did not mark every strut in a frame (Fig. 7) (this is true for almost all cases). In fact, they only marked struts having both a bright reflection and a dark shadow. This criterion was established so as to minimize inter-observer variations in strut-level analysis. However, it is quite common to find image evidence of struts without bright reflections due to an obliquely incident illumination angle. Because these are indeed true stent struts and are necessary for accurate stent area quantification, our algorithm was designed to include them. As a result, our automatic method finds many actual struts not identified as bright struts by analysts, resulting in an overestimation of false positives. As a consequence of the bias in the gold standard, the actual precision of our algorithm should be better than that reported.

## C. Training and Evaluation Studies

To evaluate automated stent strut detection, we compared results to gold standard detection and collected true positives (TP), false positives (FP), and false negatives (FN). True negatives (TN) are not informative as one might consider almost all non-strut pixels in the image as TN. As metrics of the accuracy of the automated detection system, recall (sensitivity) and precision are computed as follows:

$$
\text { Recall }=\text { TP } /(\text { TP }+F N) \quad \text { Precision }=\text { TP } /(\text { TP }+F P)
$$

First, we evaluated the effect of the size of the training data set on the Bayesian classification stage of the algorithm. Using a subset of randomly selected 10 pullbacks ( 978 images) from the validation data, we tracked the performance of the method by varying the training data size from $1,3,5,10,15,20,30,40$, to 50 pullbacks. To isolate analysis of this step, we did not include the en face processing for this experiment, but instead simply classified the strut locations using the Bayes decision rule ( $\mathrm{P}>0.5$ ).

Second, we assessed the accuracy of the en face stent mesh segmentation. For this purpose, we compared the automatic segmentation to the manually segmented stent wires by a human expert in the en face view in a subset of 18 pullbacks ( 2251 images, $\sim 12,000$ struts) using Dice's coefficient [32]. To demonstrate that the algorithm is applicable to different stent designs, we included two different, yet representative types of stents. The first type is Xience

V stent (n=15), which is the most commonly used stent type both in the U.S. and around the world. It has longitudinal bridges linking adjacent circumferential wires (Fig. 1 (b)). The second type is Nobori stent (n=3), in which adjacent circumferential wires are directly connected at junctions. Most of the stents used nowadays have similar shapes to these.

We then evaluated the major parameters equipped in the algorithm. The major free parameters are the weighting constants $\mu$ and $\lambda$ used in the objective function (4), and the deformation constraint $T$ in (5). Since (4) is a linear function, the parameters are estimated using a linear classifier such as single-layer perceptron [33] from the training data. For this task, the classification is between strut pixels and non-strut pixels in the same A-line. We determined $\mu \approx-0.4$ and $\lambda=0.3 . T$ was determined by selecting the threshold within which $99 \%$ of the analyst-marked struts from the training data satisfy the constraint. This value was found to be 0.3 mm .

With the optimized parameters, we assessed the perfonnance of the entire algorithm to detect strut locations using all the human analyzed validation data. Results are also presented stratified by degree of neointima coverage. In all cases, the data used for training were different from the data used for validation.

Finally, we compared quantitative stent areas derived from automatically detected struts by our algorithm to those from manual analysis using the commercial software. Both correlation and Bland-Altman plots [34] were used to assess agreement. We did not evaluate other area measurements because the ground truth numbers of these measurements were not recorded in the datasets due to the limitation of the commercial software. We do not report strut level measurements because of limitations of manual strut markings discussed in Section III B.

# IV. RESULTS 

## A. Bayesian Classification Affected by the Training Data Size

Fig. 8 shows the performance of the method for detecting struts as a function of training data size. Even with a small number of pullbacks (e.g. 5 or 10), the number of struts is quite large, and the performance approaches that obtained with many more training data. At about 20 pullbacks, the performance of the method reaches a stable plateau. For the following studies, we used 20 pullbacks as the training data size.

## B. En face Stent Mesh Segmentation

Fig. 9 illustrates examples of stent mesh segmentation in two stents with different designs. In both cases, MST-STENT performs well with an overall accuracy of DSC $=0.87 \pm 0.04$ (Dice's coefficient). But it achieved a higher accuracy with Nobori stents (DSC=0.92 $\pm 0.06$ ) than with Xience V stents (DSC=0.86 $\pm 0.02$ ). An example of the stent mesh search is illustrated in supplementary video 1.

## C. Validation of Stent Strut Detection in a Large Clinical Data Set

Fig. 10 shows strut detection statistics stratified by neointima coverage thickness. The algorithm achieved higher recall in struts with no or thin coverage, as compared to struts

with thick coverage. Malapposed struts can be detected with a high recall 0.90±0.14), although with a reduced precision (0.75±0.19). Reduced precision for malapplosed struts corresponds to false positives from residual blood or struts which were just not marked by experts. The precision of the algorithm in cases with >0.3mm tissue coverage is high despite its lower recall, and this is mainly because the detected false positives were also fewer. Overall, our method demonstrated 0.91±0.04 recall, and 0.84±0.08 precision. We again note that the actual performance is better than these numbers as experts did not always mark struts which were not bright (Fig. 7).

Fig. 11 demonstrates the robust performance of the presented method in images of vaiying quality and in the presence of various artifacts. Fig. 11 (a--d) show struts with different thickness of tissue coverage (including negative coverage, i.e. malaposition). Fig. 11 (e) shows an image acquired by an eccentrically positioned catheter, and the signatures of struts between 2 to 4 o'clock are very weak. But the algorithm was still able to detect them. Fig. 11 (f) illustrates that the method can correctly detect the struts in images with very low contrast, which are quite common clinically and are usually due to residual luminal blood or blood inside the catheter. Fig. 11 (g) shows that echo artifacts (bright multiple reflections in A-lines) do not affect the detection of the actual struts. Fig. 11 (h) illustrates an example where two stents were implanted overlapping in the same artery, which again can be handled well by the method. Fig. 12 shows some examples where the algorithm failed. The algorithm may mistakenly classify certain artifacts that generate strut-like shadows as struts (Fig. 12 (a)). The algorithm may miss struts with very thick coverage where almost no shadows are present (Fig. 12 (b)). These errors were initially generated from the Bayesian inference model and were tolerated by the subsequent steps of the algorithm. A common circumstance for disagreements between the algorithm and analysts is in the case of branching junctions of stents, where the struts bifurcate and the algorithm detected one strut where two were actually present very close together (Fig. 12 (c)). However, this disagreement does not significantly affect quantitative metrics derived later.

Automatically derived stent areas correlate well (r=0.988) with areas determined by analysts (Fig. 13). A Bland-Altman plot indicates a bias with analysts giving smaller areas than the automated method. We believe that stent area is underestimated in the manual analysis because the stent contour was reconstructed from the front edge of the bloom without correction. The algorithm generated greater errors for those stents with larger areas as the struts were away from the catheter and were out of focus and were more difficult to detect.

## D. 3-D Visualization

For visualization, all the struts of a pullback were marked by an experienced analyst manually and confirmed by a second observer. A 3-D reconstruction was created using software Amira (Visualization Sciences Group, Burlington, MA). Compared to manual detection (Fig. 14 (a)), the automated method, especially en face processing, generated a more complete stent mesh for visualization (Fig. 14 (b)). The corresponding fly-through view (Fig. 14 (c)) shows malapposed struts.

# E. Computation Time 

Using a program written in mixed languages of MATLAB and C++, processing time for a single pullback with 150 frames on a duo-core 3.0 GHz CPU is around 2 minutes. Additional speed optimization is possible. The approach is sufficiently fast that it can be considered feasible for live-time, clinical use.

## V. DISCUSSION

In this paper, we presented a novel method for automated detection of stent struts in intravascular OCT pullbacks. Our approach uses both Bayesian network and graph search techniques, and has been proven to be effective and robust by analyzing a large data set collected in clinical environments.

We incorporated the knowledge of OCT image formation to represent the structure of the Bayesian network for stent strut detection. Because the network structure is consistent with human logic and captures the intrinsic causal relationships between variables, it is associated with lower risks of overtraining or poor generality. Additionally, the Bayesian network explicitly characterizes the probability of strut presence, and this provides greater flexibility and adaptability than binary classifiers.

We also proposed a novel approach for stent detection by processing an en face projection image synthesized from the entire OCT sequence. This approach is dramatically different from all previous studies [4-13] where stent detection is performed in a frame-by-frame manner. Using 3-D mesh shape for stent strut detection is a difficult problem because of the diverse range of stent designs that are implanted in patients. The proposed method based upon minimum spanning tree is the first real attempt to use the continuity of stent wires in 3D to aid strut detection. Results are encouraging. The method assumes little knowledge about the design of a particular type of stent, and searches for the optimal stent mesh purely based on image data. This offers great generality and convenience for practical usage because analysts can blindly apply the algorithm without the need to specify the stent type for each pullback.

There are two additional advantages of performing stent mesh segmentation in the en face view. First, it can improve 3-D visualization of the entire stent as shown in Fig. 14 (b). 3-D visualization of stents can provide important morphological information for clinical diagnosis, such as malapposition and stent fracture [35, 36]. Longitudinal vessel features are significantly under-sampled by current commercial OCT systems ( $200 \mu \mathrm{~m}$ between frames for the C7-XR ${ }^{\mathrm{TM}}$, St. Jude Medical Inc.) as compared to the axial and transverse resolutions $15-\mu \mathrm{m}$, with the pixel size smaller than the optical resolution). If only clear struts are detected in 2-D frames, there are gaps and the 3-D reconstruction suffers. En face processing can help pick up many ambiguous struts that are unclear in single frames, but are indeed real struts by combining neighboring slice information (Fig. 1). Although these ambiguous struts are usually not included for quantification, they are beneficial for 3-D visualization. The second advantage is that manual post-correction of a wrongly segmented wire in the en face projection view can be more efficient than in individual frames. Analysts can use an algorithm such as live-wire or intelligent scissors [37] to add or delete some wires. This is

equivalent to the analyst correcting stent struts in several frames at once. In comparison, single-frame based methods require the operators to manually correct every wrongly determined strut, which is time intensive.

It should be noted that the en face stent segmentation method is robust against motion artifacts (Fig. 4). Specifically, the stent mesh may look less uniform due to geometric distortions along the circumferential direction because the stent mesh father away from the catheter has a larger circumferential dimension per unit angle, and due to non-uniform pullback or cardiac motion in the longitudinal direction. However, as the MST-STENT algorithm does not directly use the shape information of the stent and as long as the stent mesh is connected in the en face view, the perfonnance of the algorithm is less likely to be affected. In addition, the motion artifacts have little impact on the measured strut parameters because the quantification is performed in the cross-sectional view in Cartesian coordinates.

In addition to using graph search to detect those A-lines containing struts, we used graph search to determine the depth location of struts. This incorporates the roughly cylindrical shape of the stent in global processing. These high-level approaches allow cross-sectional frames with very sparse struts (usually at junctions) to be localized accurately.

We have not directly compared the presented method with previous studies because there is no standard intravascular OCT image database so far that can be used for comparison. The authors of the various studies selected their own images for validation purposes. However, it is worthy of note that the sizes of validation data sets employed in all previous studies are nearly an order of magnitude smaller than that used in the current study.

We have not separately evaluated the performance of lumen segmentation in this study, which could also affect the stent detection accuracy. The lumen segmentation method [16, 17] is in general very robust in images of varying quality and has been used in an earlier report for stent detection [10].

This study has some limitations. First, as discussed in Section III B, the gold standard is biased to exclude some difficult to observe struts. The algorithm tends to detect more stent struts than analysts, leading to misleading FP detections and an underestimation of detection performance. In addition, assessed algorithm performance could be degraded because of noisy training data. That is, multiple analysts were used, each with their own thresholds for strut detection. Nevertheless, the effect should be limited, as we found reasonable ( $95 \%$ ) inter-observer agreement (unpublished data with 6 cases, 3 observers). For the training data used to train the Bayesian network, a slight axial shift (marking the bloom front edge vs. center) does not affect strut A-line classification because the entire A-line is labeled as either strut or non-strut. Although we cannot exclude the possibility that the marked bloom front edge may generate wrong conditional probability values for certain boundary depth and distance values, given the extremely large training data ( 20 cases, $>1800$ images, $>14,000$ struts), such noise will be washed out in the final conditional probability table. Second, the current Bayesian network model neglects the effect of differences in the background signal from tissue surrounding a strut on the resulting shadow contrast. Adding this factor would complicate the inference model, but perhaps yield improvements. Third, the proposed

method works best with metallic stents exhibiting shadows, and does not detect all struts when there is thick neointima coverage and reduced shadows. As a result, recall is somewhat degraded with thicker neointima (Fig. 10). With the success of modern drug eluting stent designs [38], thick coverage is less of an issue. In fact, fewer than $5 \%$ of struts were thickly covered $m$ our database. In the event of a study having particularly thick neointima coverage, manual review and editing could be warranted. Fourth, we do not consider nonmetallic, bioresorbable stents. Nevertheless, we believe that our 3-D graph search and machine learning methods would provide tools for solving the difficult challenge of detecting bioresorbable stent struts.

# VI. CONCLUSIONS 

In conclusion, we have demonstrated a novel 3-D method for automated stent strut detection in intravascular OCT. Our method combines human expert knowledge and high level information for stent strut detection, and has achieved robust performance $\mathrm{m}>8000$ clinical images from 103 pullbacks. The algorithm has the potential to vastly reduce the manual stent analysis needed for both clinical and research purposes.

## Acknowledgments

The authors thank St. Jude Medical Inc. and University Hospitals Case Medical Center Cardiovascular Imaging Core Laboratory for providing the validation data.

This work was supported by grants R01 HL114406, R21 HL108263 and RO1 HL095717 from the National Institutes of Health.
