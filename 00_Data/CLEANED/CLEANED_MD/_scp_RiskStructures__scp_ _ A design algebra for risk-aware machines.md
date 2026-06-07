# RISKSTRUCTURES: A design algebra for risk-aware machines 

Mario Gleirscher (1), ${ }^{1,2}$ Radu Calinescu (1),2,3 and Jim Woodcock (D)<br>Computer Science Department, University of York, York, UK


#### Abstract

Machines, such as mobile robots and delivery drones, incorporate controllers responsible for a task while handling risk (e.g. anticipating and mitigating hazards; preventing and alleviating accidents). We refer to machines with this capability as risk-aware machines. Risk awareness includes robustness and resilience and complicates monitoring (i.e., introspection, sensing, prediction), decision making, and control. From an engineering perspective, risk awareness adds a range of dependability requirements to system assurance. Such assurance mandates a correct-by-construction approach to controller design, based on mathematical theory. We introduce RISKSTRUCTURES, an algebraic framework for risk modelling intended to support the design of safety controllers for risk-aware machines. Using the concept of a risk factor as a modelling primitive, this framework provides facilities to construct, examine, and assure these controllers. We prove desirable algebraic properties of these facilities, and demonstrate their applicability by using them to specify key aspects of safety controllers for risk-aware automated driving and collaborative robots.


Keywords: Correct construction; Formal development; Risk awareness; Run-time mitigation; Safety controllers; Robots and autonomous systems

## 1. Introduction

Humans identify and predict dangers and take actions to avoid or recover from dangerous situations. Likewise, autonomous machines can be expected to handle risk (e.g. hazardous environmental situations, erroneous control inputs, machine faults) on their own. Such machines should continuously judge risk in a situation, using introspection, estimating the current situation, and predicting future situations. While some risks can be avoided, for most of them only the likelihood of their occurrence or the likelihood and severity of their consequences can be reduced. This circumstance requires a careful analysis of risk causes and consequences in terms of risk factors, and the investigation of temporal and causal relationships between these. Risk can be handled by various measures [HM99, AASB*06], ranging from passive measures to active control schemes. The former include, for example, flexible surfaces or soft materials used on robot arms and predetermined breaking points in machine chassis [HASH09]. The latter include low-level continuous control mechanisms [SC88], high-leveldiscrete-event

[^0]
[^0]:    Correspondence to: Mario Gleirscher, e-mail: mario.gleirscher@york.ac.uk
    ${ }^{1}$ Mario Gleirscher was supported in part by the German Research Foundation (DFG) under the Fellowship Grant no. 381212925.
    ${ }^{2}$ Work by Radu Calinescu and Mario Gleirscher was partially supported by the Lloyd's Register Foundation under the Autonomy Assurance International Programme (AAIP) Grant CSI:Cobot.
    ${ }^{3}$ Radu Calinescu was additionally supported by the UKRI Project EP/V026747/1 "Trustworthy Autonomous Systems Node in Resilience".

controllers [MGW*18, Gle17], and remote or supervisory control schemes [She03]. Overall, active control schemes detect violations of safety properties and try to reestablish a safe state.

Objective and hypothesis Decades ago, it was suggested that machine autonomy requires extensive sensor fusion, qualitative reasoning (e.g. [HM99]), and the internalisation of models of consciousness [HG03]. However, to this date, domains such as human-robot collaboration and autonomous driving are far from full autonomy in unrestricted environments, to a good extent because of difficulties in assurance [KW17, AZI*17]. As similar engineering challenges have been solved through formal design techniques (see, e.g. the survey papers [GM20, GFW19]), we hypothesise that these difficulties can be reduced by bespoke rigorous design techniques ${ }^{4}$ beyond what can be achieved by employing general-purpose formal design methods alone. Such techniques could guide the correct construction of safety controllers that, inspired by [HM99, HG03], integrate a simple form of consciousness of risk, hereafter called risk awareness, into a machine.

Contributions Based on this hypothesis, we introduce RISKSTRUCTURES, an algebraic framework for designing correct-by-construction safety controllers for risk-aware machines. In line with conventional risk analysis, this framework uses the notion of a risk factor as a modelling primitive and, going beyond preliminary results from our previous work [Gle17, Gle18], enhances its formalisation and proves key algebraic properties of a factorbased design calculus for risk-aware controllers. Our work focuses on qualitative risk modelling, enabling the use of different approaches to dealing with uncertainty. A risk structure can be used to formally specify acceptance criteria ${ }^{5}$ and from these, one can synthesise safety controllers [GC20] and reason about their correctness. The presented theory is supported by the research tool YAP [Gle20], which interprets risk structures encoded in a domain-specific language and automates analysis and synthesis steps. To the best of our knowledge, this work is the first to give an algebraic account of risk modelling while building a bridge to safety controller design for risk-aware machines, adding design guidance to state-of-the-art dependability and risk assessment techniques, monitoring approaches, and optimal control models (Sect. 8).

The remainder of this article is structured as follows. After summarising background material and the used formalism (Sect. 2), Sects. 3 to 7 present our framework, using examples (Sect. 3 and sects. 4.3, 6.2 and 7.4) and discussing the rationale for its components (Sects. 5.5 and 6.3). Sect. 7.6 summarises RISKSTRUCTURES as an approach to model uncertain negative outcomes of a machine's actions. Based on [BFK13], Table 5 highlights how low-level uncertainties can be dealt with in RISKSTRUCTURES. After a comparison to previous research in Sect. 8, we add concluding remarks in Sect. 9. Proof details are listed in Appendix A.

# 2. Preliminaries 

Beyond the avoidance and removal of development mistakes [ALRL04, Sec. 3.3.2] by rigorous design [GFW19] and dependability techniques [ALRL04, Sec. 5.3.1], there are immanent operational risks to be dealt with by bespoke machine features. This section introduces terminology, gives an overview of risk analysis and handling for robots and autonomous systems, and explains the formalism used in this work.

### 2.1. Risk analysis, assessment, and handling

Risk is the possibility of undesired outcomes (e.g. loss, injury, damage) of an action (whether nominal, faulty, or malicious) with uncertain alternative outcomes [KG81]. ${ }^{6}$ Particularly relevant are the actions (e.g. failures, incidents, accidents) in hazardous states (e.g. faults). Risk can be assessed by the likelihood of a hazard, the likelihood of exposure of an asset to this hazard, the likelihood of an undesired outcome if this hazard occurs, and the severity of this outcome [Lev95, Kum07]. As such, it is useful to identify causal relationships between events and to quantify risk using stochastic models (cf. reliability analysis of repairable systems [Kum07]) .

[^0]
[^0]:    ${ }^{4}$ That is, techniques dedicated to capturing risk factors.
    ${ }^{5}$ For readers familiar with refinement-based development: a risk structure $\mathfrak{R}$ refined by a process $P$, after hiding $P$ 's irrelevant events, can be used to express risk acceptance in $P$ and verify this criterion of $P$.
    ${ }^{6}$ For the sake of simplicity, we neglect for whom the outcome is undesired and who performs the action. However, such aspects are useful and can be added.

Knowledge about risk often stems from accidents [SR02]. Methods such as hazard and operability studies (HazOp), event tree analysis, and layer of protection analysis help engineers to disclose hazardous event chains and design countermeasures (e.g. interventions) in response to and for the prevention of accidents [Lev95]. Fault tree analysis (FTA) and failure mode and effects analysis (FMEA) specialise in the identification, assessment, and reduction of faults or failures. There are many variants and combinations of these techniques, enriched with intuitive models and visual languages (e.g. AcciMaps [SR02]; STAMP [Lev04] for systemtheoretic process analysis [Lev12]; UML for HazOp [GMGP10]; CORAS diagrams [LSS11]), tailored for specific stages in the system life cycle [Eri15], and used to shape assurance arguments [McD94, GC17].

Using FTA, one can produce a fault tree (FT), a versatile causal model of fault propagation in a system, relating an undesired event $e_{u}$ with a set $B$ of basic events connected by various gates (e.g. AND, OR, NOT). A minimum cut set (MCS) is a minimal set of events causing $e_{u}$. Dynamic FTs are an extension modelling the ordering of such events, leading to minimal cut sequences. Such sequences describe minimal sets of events to occur in a particular order to activate $e_{u}$. FTs can be expressed by connecting sets $\min C S \subseteq 2^{B}$ in the disjunctive normal form in the antecedent and with $e_{u}$ in the consequent of the implication $\left(\bigvee_{S \in \min C S} \bigwedge_{e_{b} \in S} e_{b}\right) \Rightarrow e_{u}$, where $\min C S$ denotes all MCSs for $e_{u}$, and $e_{b}$ stands for a basic event.

For quantitative analysis, FTA and FMEA have been further formalised using probabilistic models [Kum07, ORS06], particularly, input/output Markov chains [BCS07] for checking probabilistic temporal properties, or Markov automata [VJK16] for efficient calculation of failure rates. FTs can be synthesised from failure annotations of stochastic Petri nets [UPM18] or from counterexamples generated by continuous stochastic logic model checking of continuous time Markov chains [LFL13].
Risk handling. Many operational risks cannot be avoided or mitigated by passive measures (e.g. physical segregation, safe materials). Mechanical or electronic equipment failures are usually addressed by fault-tolerant, robust, or diverse designs [Bir17], human errors by ergonomic interfaces, controllers robust to unsafe inputs [Lev12], and adverse environmental events by bespoke safety functions (e.g. safety modes [AZI ${ }^{+}$17]). An elegant transition from formal FTs into the specification of such functions is described in [HRS98].

Run-time verification (RV) checks event traces recorded during operation for violation (safety) or acceptance (co-safety) of a property [LS09]. RV can range from simple watchdogs, the checking of constraints on complex algorithm outputs $\left[\mathrm{BBH}^{+} 17\right]$, to Bayesian prediction to warn about violated health parameters such as low battery time [IMM18] and violated probability thresholds for rear-end collisions [CLC ${ }^{+}$19]. Huang et al. $\left[\mathrm{HEZ}^{+}\right.$14] show how monitoring-oriented programming (MOP) [MJG ${ }^{+}$11] allows the checking of safety properties in message communications of the robot operating system ${ }^{\dagger}$ (ROS). While these works focus on the synthesis of property monitors, there are also approaches to the design of property enforcers (e.g. [GPBB08]). Already in the 1980s, Sobek and Chatila [SC88] proposed the interruption of robot plan execution by safety monitors (e.g. for obstacle detection) responding with corrective actions (e.g. obstacle avoidance) and mitigation monitors resuming the planner after action success. Simmons [Sim94] speaks of deliberative components for normal situations and reactive behaviours for exceptional situations. Sorin et al. [SLJS16] describe the generation of safety monitors for ROS-based autonomous robots using rules with corrective actions.

Risk-aware control offers a versatile approach to property enforcement, for example, to minimise collision risk of autonomous vehicles (AVs). Althoff et al. [AKWB11] work with a probabilistic variant of inevitable collision states [FA04] to approximate collision probability and cost beyond the planning horizon by Monte Carlo sampling of trajectories. These metrics allow the ranking of simulated trajectories in navigation decisions. Pereira et al. [PBHS13] experiment with a grid-based minimal collision risk planner and a risk-aware Markov decision process (MDP) for navigating an underwater vehicle. Sanger [San14] formalises risk-aware movement by a risk estimate based on state uncertainty and the cost of control errors, implemented in a neuronal network-based AV controller. Feyzabadi and Carpin [FC14] propose a risk-aware planning algorithm using constrained MDPs, illustrated for autonomous indoor navigation. Müller and Sukhatme [MS14] encode collision risk by a Gamma distribution of the state and uncertain distance to a nearest obstacle. Shalev-Shwartz et al. [SSSS18] investigate collision-free navigation based on driving rules following the Duty of Care approach from Tort law [Har00]. This approach assumes proper response of other traffic participants in typical driving scenarios. The vehicle action space is discretised to simplify the control problem. Inspired by the notion and versatility of FTs, the present work seeks to identify the commonalities of works in risk-aware control and property enforcement and provide a unified risk handling framework.

[^0]
[^0]:    ${ }^{\dagger}$ See https://www.ros.org

# 2.2. Formalism and notation 

Our framework uses the communicating sequential processes (CSP, [Hoa85, Ros10]) approach to algebraic specification and labelled transition system (LTSs, [BK08]) to reason about its operational semantics. Let $\Sigma$ be the set of all concrete events of a process, called its alphabet. We distinguish two special events: $\checkmark$ for the termination of a process and $\tau$ for the invisible event, resulting from hiding observations. We require $\checkmark, \tau \notin \Sigma$ and define $\Sigma^{\checkmark}=\Sigma \cup\{\checkmark\}, \Sigma^{\tau}=\Sigma \cup\{\tau\}$, and $\Sigma^{\checkmark, \tau}=\Sigma^{\checkmark} \cup \Sigma^{\tau}$.
Definition 1 (Process) A process is an expression of the form

$$
P::=a \rightarrow P \mid ? x: A \rightarrow P|P \cap P| P \square P \mid P \|_{A} P|P ; P| P \backslash A|S K I P \mid S T O P
$$

with event $a \in \Sigma$, shared alphabet $A \subseteq \Sigma$, event prefix $(\rightarrow)$, prefix choice $(? x: \rightarrow)$, non-deterministic choice $(\cap)$, external choice $(\square)$, generalised parallel composition $(\S)$, sequential composition (; ), hiding $(\backslash)$, termination (SKIP), and deadlock (STOP). Let $\mathcal{P}$ be the set of all processes.
Each expression $P \in \mathcal{P}$ corresponds to observable behaviours represented in a trace model. Traces are finite sequences over $\Sigma^{\checkmark}$ abstracting from details (e.g. internal states) of $P$ 's executions. In the trace model, traces $(P)$ yields the trace semantics of $P$. For example, $\operatorname{traces}(S T O P)=\{\langle \rangle\}$ and $\operatorname{traces}(S K I P)=\{\langle \rangle,\langle\checkmark\rangle\}$. initials $(P)=$ $\{a \mid\langle a\rangle \in \operatorname{traces}(P)\}$ denotes the set of all initial events of $P$. For processes $P$ and $Q$, we write $P \sqsubseteq_{s} Q$ to say that $Q$ s-refines $P$ (or $P$ is s-refined by $Q$ ) and that $\operatorname{traces}(P) \supseteq \operatorname{traces}(Q)$, with the usual abbreviation $P=_{s} Q \Longleftrightarrow P \sqsubseteq_{s} Q \wedge Q \sqsubseteq_{s} P .{ }^{8}$ We use the term control state for a process and write $\|$ if $A=\Sigma$. Below, we consider $P=S y \| E n$, with a system $S y$ interacting with its environment $E n$, or $P=E n(S y)$, with the CSP expression En using Sy.
Definition 2 (Labelled transition system) A LTS is a tuple $T=\left(S, \Sigma^{T}, \rightarrow, S_{0}\right)$ with a set $S$ of states, a set $\Sigma^{T} \subseteq$ $2^{\Sigma^{\tau}} \backslash\{\varnothing\}$ of abstract events (i.e., sets of concrete events), a relation $\rightarrow \subseteq S \times \Sigma^{T} \times S$ of state transitions when engaging in these events, and a set $S_{0} \subseteq S$ of initial states. Omission of $S_{0}$ results in an uninitialised LTS $\left(S, \Sigma^{T}, \rightarrow\right.$ ), further omission of $\Sigma^{T}$ in a directed graph $(S, \rightarrow)$ with $\rightarrow \subseteq S \times S$, called transition system (TS). Let $\mathcal{T}$ be the set of all TSs.
We write $s \xrightarrow{e} s^{\prime}$ if $\left(s, e, s^{\prime}\right) \in \rightarrow, s \xrightarrow{e}$ if $\exists s^{\prime} \in S:\left(s, e, s^{\prime}\right) \in \rightarrow, s \rightarrow$ if $\exists e \in \Sigma^{T}, s^{\prime} \in S:\left(s, e, s^{\prime}\right) \in \rightarrow, s \xrightarrow{e}$ if $\nexists s^{\prime} \in S:\left(s, e, s^{\prime}\right) \in \rightarrow$, and $s \nrightarrow$ if $\nexists e \in \Sigma^{T}, s^{\prime} \in S:\left(s, e, s^{\prime}\right) \in \rightarrow$. A $\varnothing$ indicates discharged cases in proofs.

## 3. RISKSTRUCTURES: overview

In this section, we give an overview of the components of the proposed framework. We describe the abstraction facilitated by RISKSTRUCTURES, building a bridge between (probabilistic) process modelling, risk analysis, and controller design. Moreover, we illustrate the main concepts, terminology, and work steps using an example from the road vehicle domain, which will be revisited in later sections.

Figure 1 (bottom right) shows an example of a process $P$ (Definition 1) associated with an LTS $T$ (Definition 2). $P$ describes actions of one or several agents (e.g. a machine, an operator) in a physical environment, for example, a manually driven vehicle with some kind of driving assistance on an urban road. $P$ 's actions include data processing, control stimuli via actuators, and the monitoring of process outcomes. In this example, data processing occurs with $n a v$, where the machine performs calculations for navigation (stored internally and displayed to the driver), step of the driver interpreting data for a next control action, warn of the vehicle sending information to the driver, and resume of the vehicle returning from a risk handling procedure. Control stimuli include the action $d r v$, where the driver performs a default driving manoeuvre, $s w B r$ where the vehicle executes a swerve and brake manoeuvre, and emBr representing an emergency braking action conducted by the vehicle. Monitored outcomes include, for example, the occurrence ( $e^{\ln c_{d}}$ ) of the risk factor loss of driving control $\left(\ln c_{d}\right)$, a potential accident ( $e^{\ln c_{d}}$ ) following $e^{\ln c_{d}}$, and the performance and success of a mitigation $\left(m^{\ln c_{d}}\right)$ of this factor, recognised by the machine, and idling or no output $\left(\tau_{i}\right)$. Underspecification and uncertainty in $P$ can be described by non-determinism or quantified by probabilities $\left(\lambda_{i}\right)$ on action outcomes. $\operatorname{traces}(P)$ denotes possible chains of events and $T$ the reachable states $\left(s_{i}\right) .{ }^{9}$

[^0]
[^0]:    ${ }^{8}$ We use $\sqsubseteq_{T}$ for trace refinement and $\subseteq_{F D}$ for failures-divergences refinement and refer the inclined reader to [Ros10].
    ${ }^{9} \operatorname{traces}(P)$ contains finite traces reaching such states such that causes can be represented by well-founded sets.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Risk structure $\mathfrak{R}$ partitioning the states of the process $P$, that is, labelling $P$ 's states with the phases inactive ( $0^{\text {loc }}$, white) and active (loc, dark gray) of the risk factor $\operatorname{loc}_{\mathrm{d}}$; $P$ 's transitions are classified into endangerments (dashed arcs), mitigations (solid arcs), and other transitions (dotted arcs); incomplete abstractions may contain unclassified states (light-grey)

Risk, as introduced in Sect. 2.1, can then be qualitatively (or quantitatively) characterised in $P$ as the possibility (probability) of an undesired state (e.g. $s_{4}$ ) being finitely reachable from a particular state (e.g. $s_{1}$ ) in $T$. Next, Fig. 1 shows the abstraction from $P$ into an exemplary risk structure $\mathfrak{R}$ comprising the single factor $\operatorname{loc}_{\mathrm{d}}$. This abstraction allows one to focus on the events relevant from the perspective of this factor, that is, its activation ( $e^{\operatorname{loc}_{\mathrm{d}}}$ ) and mitigation ( $m^{\operatorname{loc}_{\mathrm{d}}}$ ). Accordingly, this abstraction step includes the labelling of regions of $P$ 's state space with predicates (e.g. for hazards and, more generally, situations) and the construction of $\mathfrak{R}$ over the resulting abstract state space. Moreover, this representation helps one to focus on the structure of risk of a certain application by using information about factors encoded in predicates (e.g. active, inactive) and real-valued functions (e.g. [AKWB11, PBHS13]). These predicates and functions can be derived from hazard analysis (Sect. 2.1) and be used to allow a risk-aware machine to estimate risk levels of reachable states and to plan and execute actions reaching or avoiding the corresponding states.

For example, the factor $\operatorname{loc}_{\mathrm{d}}$ partitions $T$ 's state space (cf. nodes in the bottom right of Fig. 1) into regions where $\operatorname{loc}_{\mathrm{d}}$ is inactive ( $0^{\text {loc }_{d}}$, white), active (loc $l_{d}$, dark grey), or where an accident (loc $l_{d}$, light-grey) has happened. To focus on the practical handling of $\operatorname{loc}_{\mathrm{d}}$ in $P$, outcomes (e.g. $e^{\operatorname{loc}_{\mathrm{d}}}, m^{\operatorname{loc}_{\mathrm{d}}}, \tau_{s}$ ) are paired with their control actions (e.g. $d r v, s w B r, e m B r$; dotted arcs) and merged into sets of transition labels called events (e.g. $\left\{s w B r / m^{\operatorname{loc}_{\mathrm{d}}}, \ldots\right\},\left\{s w B r / \tau_{2}, \ldots\right\})$. To keep track of mishap states, such as $s_{6}$, we assign the label $\underline{\text { loc }_{d}}$ to states where undesired consequences after an unmitigated $e^{\operatorname{loc}_{\mathrm{d}}}$-event will be materialised. Such states might be reached, for example, after the execution of $e m B r, d r v$, and $s w B r$ with a collision $e^{\operatorname{loc}_{\mathrm{d}}}$ as the possible outcome. $\underline{\text { loc }_{d}}$ enables risk assessment in terms of likelihood and severity. To design mitigations for $\underline{\text { loc }_{d}}$, we introduce an extra risk factor (e.g. col) handling $e^{\text {lod }_{d}}$ in analogy to $e^{\text {loc }_{d}}$. This technique will be discussed below. Overall, for $\operatorname{loc}_{\mathrm{d}}$, $\mathfrak{R}$ reduces to just two abstract states $\left(0^{\text {loc }_{d}}, \operatorname{loc}_{d}\right)$ and two events, the endangerment $e^{\operatorname{loc}_{\mathrm{d}}}$ (dashed arc) and the mitigation $m^{\operatorname{loc}_{\mathrm{d}}}$ (solid arcs). We assume there to be observational refinement or some simulation relation between $T$ and $\mathfrak{R}$.

Overall, risk awareness amounts to the machine incorporating $\mathfrak{R}$ in its decisions such that expected risk from its own actions does not exceed an acceptable level. So, how can we engineer $\mathfrak{R}$ ?

From an engineering perspective, our approach requires neither $P$ nor $\mathfrak{R}$ to exist in a complete form to facilitate the aforementioned abstraction or refinement. One can rather think of these two artefacts as being developed concurrently.

Table 1. A generic situation/action/factor table (a) and per-cell risk analysis checklists (b, c)


(a) Generic situation/action/factor table


(b) Factor activation analysis (causes/consequences)

Why would $f_{i}$ occur with/during action $a_{j}$ in situation $\sigma_{k}$ ?
What if $f_{i}$ occurs with/during action $a_{j}$ in situation $\sigma_{k}$ ?

1. What is the likelihood of occurrence of $f_{i}$ ?

Quantified by $\operatorname{Pr}\left[f_{i} \mid a_{j}, \sigma_{k}\right]$.
2. What is the risk of an accident $f_{i}$ following $f_{i}$ ?

Quantified by the likelihood $\operatorname{Pr}\left[\underline{f_{i}} \mid f_{i}, a_{j}, \sigma_{k}\right]$ and
the severity $\operatorname{sev}\left(f_{i} ; f_{i}, a_{j}, \sigma_{k}\right)$.
3. Which other factors are related to the activation of $f_{i}$ ?

Qualified by relationships such as $f_{i}$ requires $f_{j}, f_{i}$ causes $f_{k}$; and quantified by $\operatorname{Pr}\left[f_{k} \mid f_{i}, a_{j}, \sigma_{k}\right]$.
(c) Factor mitigation analysis

How can we mitigate $f_{i}$ during or after action $a_{j}$ in the situation $\sigma_{k}$ ?
4. Which mitigation options $m$ are available to reach $\bar{f}_{i}$ ?
5. What is the risk of an accident $f_{i}$ following $\bar{f}_{i}$ ?

Quantified by the likelihood $\operatorname{Pr}\left[\underline{f_{i}} \mid \bar{f}_{i}, m, a_{j}, \sigma_{k}\right]$ and
the severity $\operatorname{sev}\left(\underline{f_{i}} ; \bar{f}_{i}, m, a_{j}, \sigma_{k}\right)$.
6. Which other factors are related to the mitigation of $f_{i}$ ?

Qualified by relationships such as $f_{i}$ prevents $f_{j}, f_{i}$ causes $f_{k}$; and quantified by $\operatorname{Pr}\left[f_{k} \mid \bar{f}_{i}, m, a_{j}, \sigma_{k}\right]$.
For example, one might start with a part of $P$, then, after risk analysis, continue with a part of $\mathfrak{R}$, and in a second iteration, maybe even after a period of operation, proceed with another part of both $P$ and $\mathfrak{R}$. In this sense, $\mathfrak{R}$ can be incrementally developed. The notion of a situation will help us to structure such a development. A situation, $\sigma$, is an abstract state that describes a particular context (i.e., a scene or environment), an activity (i.e., a task, operating mode, a use case, or scenario), and a configuration of hazardous events occurring in $P$. Engineers and risk analysts are familiar with tables and graphs, for example, when applying HazOp or FMEA to assess risk factors of certain machine actions in particular situations. We will, therefore, show in the following how one can develop $\mathfrak{R}$ by means of what we call a situation/action/factor table (Table 1a).

One may want to start with an initial set of application-specific situations and actions that the machine under consideration can perform, together with an initial set of factors, maybe obvious from accident experience and preliminary hazard analyses. Then, each resulting cell in Table 1a would involve a focused cause/consequence analysis (e.g. [ORS06]) and risk assessment (Sect. 2.1), for example, using risk graphs [Kum07, p. 53]. Tables 1 b and 1 c elaborate ideas in [Gle18] for such analyses, including the estimation of the conditional probability $\operatorname{Pr}[X \mid Y]$ and severity $\operatorname{sev}(X ; Y)$ of an event $X$ under the condition $Y$. We use $0^{f}, f, \bar{f}$, and $\underline{f}$ to denote the inactive, active, mitigated, and mishap phases of a factor f, explained in Sect. 4.1. Incrementally, one would add further situations, actions, and factors to the table. At some point, one can split the table into several smaller ones. Please, note that such tables are not subject of this work. We presented them merely to hint to the data to be collected for building $\mathfrak{R}$. Moreover, when formalising situations, we will only consider the hazardous events part. In our future work, we will discuss situations in more detail.

Table 2. Example of a situation/action/factor table for road driving


Legend: Numbers indicate the analysis steps applied from the Table 1b and 1c; situation/action/factor parameters for $\operatorname{Pr}$ and sev are determined by the cell (hence omitted); values after the colon are exemplary; probabilities are abstracted to $h / m / l$ for high/medium/low; relationship sources are determined by the column (hence omitted); * . . . cross-reference to other cell;-irrelevant/not applicable

Extending the Example from Fig. 1 In Fig. 1, we illustrated basic concepts by discussing a single risk factor $\left(\mathrm{loc}_{\mathrm{d}}\right)$. Now, we extend our discussion to a more realistic setting by investigating situations, system actions, and further risk factors. In Table 2, we consider actions such as releaseAirbag ( $r A$ ), responsible for mitigating a collision col, that is, $m^{\text {col }}=r A$. However, $r A$ itself may be associated with two failure modes: failure on demand $\mathrm{fod}_{\mathrm{rA}}$ (i.e., $r A$ not performed when requested) and spurious trip $\mathrm{st}_{\mathrm{rA}}$ (i.e., $r A$ performed when not requested). In forward reasoning, one can ask: What if $\mathrm{fod}_{\mathrm{rA}}$ or $\mathrm{st}_{\mathrm{rA}}$, both influencing or determining the behaviour of $r A$, are activated in manual or autonomous driving mode? $\mathrm{st}_{\mathrm{rA}}$ in manual mode would increase the probability of a crash because of a loss of control loc ${ }_{\mathrm{d}}$ from shock and distraction. $\mathrm{st}_{\mathrm{rA}}$ in autonomous mode may cause shock injuries but would unlikely cause a crash. fod $_{\mathrm{rA}}$ will be irrelevant in normal situations but in a collision, risk will be quite similar to the case of no airbag.

Table 2 can store probabilistic relationships, for example, between near-collision ncol and collision col. Probabilities for ncol and col will be highly dynamic and need to be estimated and used for decision making at run-time. Probabilities for $\mathrm{fod}_{\mathrm{rA}}$ maybe more stable, known from experiments, and can be used in risk assessment at designtime. Requirements on the confidence in probability estimates are specific to each factor. Note the variety of relationships between situations, actions, and factors, for example, in manual mode $\operatorname{loc}_{\mathrm{d}}$ requires $\mathrm{st}_{\mathrm{rA}}$, fod $_{\mathrm{rA}}$ in collision is similar to col in no airbag, $\mathrm{st}_{\mathrm{rA}}$ in manual mode extends $\mathrm{st}_{\mathrm{rA}}$ in autonomous mode, and the airbag, subject of risk assessment in the two $r A$-columns, mitigates col.

Graphs (e.g. FTs) can be used to visualise and elicit the information stored in Table 2 if these tables get more complex. The tabular representation is, however, integrative, scales, and conveys the scheme recurring across the cells as well as the relationships between situations, actions, and factors. We will discuss and use some of these relationships in our framework.

The components of a design algebra for risk-aware machines will be described in the following sections: risk factors and risk spaces (Sect. 4), mitigation orders (Sect. 5), factor dependencies (Sect. 6), and, finally, RISKSTRUCTURES (Sect. 7), illustrated by examples and a discussion of applications.

# 4. Risk spaces 

This section introduces risk factors and risk spaces, frequently abbreviated by "factors" and "spaces", as the basic elements of the algebraic framework.

### 4.1. Risk factors

We first define the notion of a risk factor using a LTS and describe its properties and meaning.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Basic template of a risk factor $f$ (a) with a description of f's events (b)

Definition 3 (Risk factor) Let $\left(P h_{\mathrm{f}}, \Sigma^{\mathrm{f}}, \rightarrow_{\mathrm{f}}\right)$ be an uninitialised LTS according to Definition 2. Extending this LTS, a risk factor is a tuple $\mathrm{f}=\left(P h_{\mathrm{f}}, \Sigma^{\mathrm{f}}, \rightarrow_{\mathrm{f}}, \preceq_{\mathrm{f}}, s_{\mathrm{f}}\right)$ with

- A finite set $P h_{\mathrm{f}}$ of phases of f ,
- A finite set $\Sigma^{\mathrm{f}} \subset 2^{\Sigma^{\prime}} \backslash\{\varnothing\}$ specifying significant events for f ,
- A labelled transition relation $\rightarrow \subseteq P h_{\mathrm{f}} \times \Sigma^{\mathrm{f}} \times P h_{\mathrm{f}}$,
- A partial order $\preceq_{\mathrm{f}} \preceq_{\mathrm{f}} \subseteq P h_{\mathrm{f}} \times P h_{\mathrm{f}}$ called phase order of f , and
- A pair $s_{\mathrm{f}} \in \mathbb{R}_{+}^{2}$ with $s_{\mathrm{f}}^{(1)} \leq s_{\mathrm{f}}^{(2)}$ denoting the severity of the least and worst expected impact of $\mathrm{f} .{ }^{10}$

Let $\mathcal{F}$ be the set of all risk factors.
We consider factors f with $\rightarrow_{\mathrm{f}}$ according to Fig. 2a with $P h_{\mathrm{f}}=\left\{0^{f}, f, \bar{f}\right\}$ for the phases inactive ( $0^{f}$, typically, the initial phase), active $(f)$, and mitigated $(\bar{f})$, where $\preceq_{\mathrm{f}} \preceq_{\mathrm{f}}$ is at least ${ }^{11}$ the reflexive transitive closure of $\left\{\left(f, 0^{f}\right),(f, \bar{f})\right\}$, and with $\Sigma^{\mathrm{f}}=\left\{e^{\mathrm{f}}, \bar{e}^{\mathrm{f}}, m^{\mathrm{f}}, m_{d}^{\mathrm{f}}, m_{e}^{\mathrm{f}}, o_{n}^{\mathrm{f}}, o_{m}^{\mathrm{f}}, o_{e}^{\mathrm{f}}\right\}$.

The interval $s_{\mathrm{f}}$ represents the severity (also known as the detriment or negativity) of f's expected materialised impact or consequences for any relevant assets if f gets and stays active. Impact can include, for example, damage of the environment, injury of humans, loss of a valuable, or any combination of these.
Events and factor types. By Definition 3, for any $p, p^{\prime} \in P h_{\mathrm{f}}$ if $\left(p, e, p^{\prime}\right) \in \rightarrow_{\mathrm{f}}$ then $e \neq \varnothing$. f is deterministic if and only if for every phase the events of all outgoing transitions are pairwise disjoint. We require $\forall p \in$ $P h_{\mathrm{f}}:\left(\bigcup_{\{p, e, p^{\prime}\} \in p \rightarrow} e\right) \backslash\{\mathrm{r}\}=\Sigma .{ }^{12}$ Figures 2a and 2b indicate the meaning of the events in $\Sigma^{\mathrm{f}}$ for factor modelling. The three phase-preserving events $o_{n}^{\mathrm{f}}, o_{e}^{\mathrm{f}}$, and $o_{m}^{\mathrm{f}}$ complement the endangerment and mitigation events. Moreover, we distinguish some special types of factors:

- If $m^{\mathrm{f}} \cup m_{d}^{\mathrm{f}}=\varnothing$ then we call f final, otherwise reducible.
- For any reducible f with $m^{\mathrm{f}} \neq \varnothing$, if $\bar{e}^{\mathrm{f}} \subset e^{\mathrm{f}}$ then we call f strongly reducible.
- If $m_{d}^{\mathrm{f}}=\varnothing$ then we call f indirectly reducible.

Modelling mishaps. Observing from the example in Sect. 3, the mishap phase $\underline{f}$, modelling incidents or accidents from $f$, complements the severity information encoded in f.s and enables risk assessment solely based on a single risk factor. It turns out, however, that $\underline{f}$ is non-essential for the basic framework we want to discuss in the following sections. While we keep $\underline{f}$ for factor-specific risk assessment, to simplify algebraic reasoning about factors as discussed below, we collapse $\underline{f}$ into $f$ and $\underline{e}^{\mathrm{f}}$ into $o_{n}^{\mathrm{f}}$. Furthermore, we introduce a final factor $\mathrm{f}^{\prime}$ to model the corresponding mishap. This approach simplifies the basic factor model and allows the conversion of $\mathrm{f}^{\prime}$ into a reducible factor when a mitigation for $\mathrm{f}^{\prime}$ is available. For example, as illustrated in Table 2, the factor col provides accident handling for the factor ncol, whose likelihood of occurrence under the condition of $\operatorname{loc}_{\mathrm{d}}$ is high. In [Gle18, GC20], however, we have started to work with a refined factor model including $\underline{f}$ as well

[^0]
[^0]:    ${ }^{10}$ By usual convention, for an ordered $n$-tuple $t$ and $i \in[1 . . n]$, we write $t^{(i)}$ to refer to the value of the $i$-th element of $t$. Furthermore, if $t$ has a uniquely named element $e$, we write $t . e$ to refer to the value of $e$ in $t$.
    ${ }^{11}$ Some applications might give rise to a linear $\preceq_{\mathrm{f}} \preceq_{\mathrm{f}}$ by adding at most one out of $\left\{\left(0^{f}, \bar{f}\right),\left(\bar{f}, 0^{f}\right)\right\}$.
    ${ }^{12}$ In testing, this is known as input-enabledness [Tre08].

as further phases and events (e.g. for mishap alleviation). In order to preserve the main results presented here, such extensions require $\preceq_{\mathrm{f}} \preceq_{\mathrm{f}}$ to have a unique maximal element (discussed in Sect. 5.3) and an adjustment of constraint definitions in Sect. 6.1. We conclude that $P h_{\mathrm{f}}$ and $\Sigma^{\mathrm{f}}$ comprise a useful minimal set of elements for a generic risk factor $f$.

# 4.2. Risk states, spaces, and space composition 

Risk factors give rise to risk states and risk spaces. Let $F \subset \mathcal{F}$ be a finite factor set (Definition 3) where each $\mathrm{f} \in F$ has the form $\mathrm{f}=\left(P h_{\mathrm{f}}, \Sigma^{\mathrm{f}}, \rightarrow_{\mathrm{f}}, \preceq_{\mathrm{f}} \preceq_{\mathrm{f}}, s_{\mathrm{f}}\right)$.
Definition 4 (Risk state) Assume that risk factors are unique, that is, $\forall \mathrm{f}, \mathrm{g} \in F: \mathrm{f} \neq \mathrm{g} \Rightarrow P h_{\mathrm{f}} \cap P h_{\mathrm{g}}=\varnothing$. Then, a risk state is a faithful total injection $\sigma: F \rightarrow \bigcup_{\mathrm{f} \in F} P h_{\mathrm{f}}$, that is, $\forall \mathrm{f} \in F: \sigma(\mathrm{f}) \in P h_{\mathrm{f}}$.
A risk state abstracts from states of $P$ by focusing on risk-related information in form of state propositions associated with the factor phases. Such propositions will, however, not be formalised in this work.
Definition 5 (Risk space) For a factor set $F$, a risk space $R(F)$ is the function space given by

$$
R(F)=\left\{\sigma \in F \rightarrow \bigcup_{\mathrm{f} \in F} P h_{\mathrm{f}} \mid \sigma \text { is total } \wedge \sigma \text { is an injection } \wedge \forall \mathrm{f} \in F: \sigma(\mathrm{f}) \in P h_{\mathrm{f}}\right\}
$$

We omit the parameter $F$ from $R$ if it is clear from the context and denote the set of all risk spaces by $\mathcal{R}$.
By Definition 5, $R$ is non-empty and finite if and only if $F$ is non-empty and finite. $R$ defines the set of all states an arbitrary ${ }^{13}$ combination of factor phases might give rise to. Note that $\sigma(\mathrm{f})$ can now be used to refer to the phase of factor $f$ in a risk state $\sigma$.
Definition 6 (Compatibility of risk states) Given $F_{1}, F_{2} \subset \mathcal{F}, \sigma \in R\left(F_{1}\right)$ and $\sigma^{\prime} \in R\left(F_{2}\right)$ are compatible, written

$$
\sigma \approx \sigma^{\prime} \Longleftrightarrow \forall \mathrm{f} \in F_{1} \cap F_{2}: \sigma(\mathrm{f})=\sigma^{\prime}(\mathrm{f})
$$

Notice that any two risk states $\sigma \in R\left(F_{1}\right)$ and $\sigma^{\prime} \in R\left(F_{2}\right)$ are compatible if $F_{1} \cap F_{2}=\varnothing$ and, furthermore, that state equality implies $F_{1}=F_{2}$ and, therefore, state compatibility. This compatibility is a prerequisite for risk space composition as follows.
Definition 7 (Risk space composition) The composition $\otimes: \mathcal{R} \times \mathcal{R} \rightarrow \mathcal{R}$ of the two risk spaces $R\left(F_{1}\right)$ and $R\left(F_{2}\right)$ is defined by

$$
R\left(F_{1}\right) \otimes R\left(F_{2}\right)=\left\{\sigma_{1} \cup \sigma_{2} \mid \sigma_{1} \in R\left(F_{1}\right) \wedge \sigma_{2} \in R\left(F_{2}\right) \wedge \sigma_{1} \approx \sigma_{2}\right\}
$$

Now, we can derive a basic law relating the union of risk factors and the composition of risk spaces. Furthermore, it will turn out that $R$ is a homomorphism.

## Lemma 1 (Exchange of $\cup$ and $\otimes$ )

$$
R\left(F_{1} \cup F_{2}\right)=R\left(F_{1}\right) \otimes R\left(F_{2}\right)
$$

Proof sketch. The proof is by mutual existence and uniqueness: For each $\sigma \in R\left(F_{1} \cup F_{2}\right)$, (i) there exists a $\sigma_{1} \cup \sigma_{2} \in R\left(F_{1}\right) \otimes R\left(F_{2}\right)$ and (ii) this pair is unique, and (iii, iv) conversely. Details on the proof can be taken from Appendix A.

Lemma 2 ( $R$ is homomorphic) $R$ is a homomorphism in the context of $(\mathcal{F}, \cup)$ and $(\mathcal{R}, \otimes)$.
![img-2.jpeg](img-2.jpeg)

[^0]
[^0]:    ${ }^{13}$ Below, we also view $R$ as "the most general (risk) structure" for a specific factor set.

Proof sketch. We first make sure that we deal with semi-groups and then show by algebraic manipulation that $\otimes$ is associative. Details on the proof can be taken from Appendix A.

Two specific classes of risk states and a basic lemma close this section. $R(\{\mathrm{f}\})=\left\{\left[\mathrm{f} \mapsto 0^{f}\right],[\mathrm{f} \mapsto f],[\mathrm{f} \mapsto \bar{f}]\right\}$ forms the trivial risk space for f , and $R(\varnothing)=\varnothing$ the empty risk space, used in the following equality.
Corollary 1 For finite $F \subset \mathcal{F}$, Lemma 1 yields $R(\varnothing)$ to be the zero element of composition with $\otimes$ :

$$
R(\varnothing) \otimes R(F)=R(F)
$$

# 4.3. Example: risk factors on the road 

In the following, we discuss Table 2 more deeply and provide further examples for the event sets in Fig. 2b. Tracing back through the causal relation from col, we find that collisions require near-collisions to occur beforehand. Based on that observation, we identify a combination of swerve \& brake ( $s w B r$ ) to be a possible mitigation for ncol. However, the action $s w B r$ gives rise to the failure on demand fod $_{\mathrm{br}}$ of the car's braking action $b r$. This extension of the analysis in Table 2 results in another dependency, namely, fod $_{\mathrm{br}}$ impedes the mitigation of ncol, technically, it disables the braking action $b r$.

Tracing forward through the causal relation, we may stop at application-specific factors. Such factors can be modelled as final, that is, the machine will not mitigate them. This way, final factors define the scope of $\mathfrak{R}$. However, as explained in Sect. 4.1, a design increment of the machine can turn a final into a reducible factor. For example, designing an airbag into a car makes col reducible. This epistemic limit explains why safety always has to be considered relative to a known factor set $F$ [Glel4].

Tracing back again from fod $_{\mathrm{br}}$ discloses the failure mode degradation of brake degbr. degbr causally relates to fod $_{\mathrm{br}}$ like ncol relates to col: degbr will make br ineffectual but not ineffective, if one does not intervene, degbr will actually cause fod $_{\mathrm{br}}$. We want degbr to be strongly reducible, based on a mitigation $m^{\text {deg }}{ }_{\text {br }}$ that establishes $\overline{d e g}_{\text {br }}$ from which only a strict subset $\bar{e}^{\text {deg }_{\text {br }}} \subset e^{\text {deg }_{\text {br }}}$ can occur. In phase degbr, drive by and halt would be a conservative option for $m^{\text {deg }_{\text {br }}}$ to be implemented by a safety controller. These reasoning steps are summarised in Fig. 3.

While the state bi-partition for $\operatorname{loc}_{\mathrm{d}}$ shown in Fig. 1 seems sufficient, some factors need a tri- or $n$-partition. For example, fod $_{\mathrm{br}}$ suggests a vehicle repair. Therefore, Fig. 2a introduces a third phase to separate the state where a brake failure (fod $_{\mathrm{br}}$ ) is mitigated ( $\left.f o d_{\mathrm{br}}^{\mathrm{r}}\right)$ from the state $0^{\text {fod }_{\mathrm{br}}}$ where the brake is fully operational. Because fod $_{\mathrm{br}}$ requires an off-line repair action $m_{r}^{\text {fod }_{\mathrm{br}}}$, it is indirectly reducible. Two further examples for such a factor would be leaking or damaged battery and run out of fuel. Reaching the "safe state" $\overline{f o d_{\mathrm{br}}}$ is possible via an intermediate stable state such as halted at car repair shop. From this phase, recovery $\left(m_{r}^{\text {fod }_{\mathrm{br}}}\right)$ to the inactive phase $0^{\text {fod }_{\mathrm{br}}}$ should be feasible. In contrast, ncol or too close to the front vehicle are factors that can often be dealt with by braking or swerving correspondingly (i.e., $s w B r$ ). Thus, reaching $0^{n c o l}$ should be possible. In this sense, ncol is directly reducible.

Risk awareness emerges from combining several factors (e.g. $F=\left\{\operatorname{loc}_{\mathrm{d}}, \mathrm{ncol}, \mathrm{col}, \mathrm{st}_{\mathrm{rA}}, \mathrm{fod}_{\mathrm{rA}}, \mathrm{fod}_{\mathrm{br}}, \operatorname{deg}_{\mathrm{br}}\right\}$ ) into a risk space $R(F)$, detecting the current risk state, and estimating the likelihood of neighbouring, potentially worse, risk states. Our example suggests that risk awareness contains a notion of machine health. One might expect an autonomous vehicle to take full responsibility of emergency control in any of the states in $R(F)$.
![img-3.jpeg](img-3.jpeg)

Fig. 3. Factor instances (deg $_{\mathrm{br}}$, fod $_{\mathrm{br}}$, ncol, col) and their dependencies (thick arcs, e.g. requires)

![img-4.jpeg](img-4.jpeg)

Fig. 4. Risk factor $f$ with non-deterministic fractions $u e^{\mathrm{f}}, u m^{\mathrm{f}}$, and $u m_{r}^{\mathrm{f}}$. The label $\tau$ is to be read as $\{\tau\}$

This example illustrates how the proposed formalism captures and guides the way of thinking of safety engineers responsible for developing and assuring safety controllers of autonomous machines.

# 4.4. Discussion: abstraction and types of risk factors 

Types of risk factors and risk states Factors can be used to model faults, failure modes, hazards, incidents, and accidents. Final factors can model, for example, permanent and off-line repairable faults, and reducible factors, for example, transient and on-line repairable faults.

States with an active final factor f (Sect. 4.1) expose the process $P$ to residual risk infinitely long and often, thus, almost certainly materialising the consequences of $f$. By using $\mathfrak{R}$, a risk-aware machine in a process $P$ should govern its (often probabilistic) choices to not enter such states.

Uncertainty in risk factors Figure 1 illustrates the abstraction from a possibly probabilistic process $P$ into a deterministic risk structure $\mathfrak{R}$ with a single factor, now call it $f$. This abstraction could preserve the probability of occurrence of $f$, if estimated, in $\mathfrak{R}$. However, the quantities of $f$ (especially the probabilities) will often not be confidently known even if they are continuously estimated during operation. But, as indicated in Fig. 4, assumptions about the events of $f$ might still be made, for example,

1. uncertainty about the actual occurrence of an endangerment $e^{\mathrm{f}}$ expressed as $u e^{\mathrm{f}}=o_{u}^{\mathrm{f}} \cap e^{\mathrm{f}}$,
2. uncertainties $u m^{\mathrm{f}}=o_{u}^{\mathrm{f}} \cap m^{\mathrm{f}}$ and $u m_{r}^{\mathrm{f}}=o_{m}^{\mathrm{f}} \cap m_{r}^{\mathrm{f}}$ in the success of mitigation $m^{\mathrm{f}}$ and recovery $m_{r}^{\mathrm{f}}$, or
3. the likelihood of an accident $\underline{f}$ from $f$.

Deterministic risk factors ( $u e^{\mathrm{f}}=\varnothing$, Definition 3) assume that $\mathfrak{R}$ is certain about the preconditions that activate $f$, that is, from observing $e^{\mathrm{f}}, \mathfrak{R}$ knows that the machine enters $f$. However, $u e^{\mathrm{f}} \neq \varnothing$ means that $\mathfrak{R}$ can observe $e^{\mathrm{f}}$ but $P$ does not necessarily move to a state fulfilling $f$.

An example for 1 . could be an obstacle tracked within safe braking distance with low confidence, justifying both states $0^{f}$ and $f$. This situation requires further state estimation (e.g. a homing algorithm [NSV03]) to disclose further information about the tracked obstacle. We also discuss this below in Sect. 7.6.

Moreover, $e^{\mathrm{f}} \backslash u e^{\mathrm{f}}$ can describe known causes of f and $u e^{\mathrm{f}}$ potential causes of $\mathrm{f} . o_{u}^{\mathrm{f}} \supseteq e^{\mathrm{f}}$ means that $\mathfrak{R}$ is uncertain about all of f's causes. Following [Ros10, p. 116], $u e^{\mathrm{f}}$ is followed by non-deterministic choice over $0^{f}$ and $f$, modelled by $\tau$ from an anonymous state $(\mathrm{O})$ in the factor LTS. Analogously, with $u m^{\mathrm{f}}$ for $f$ and $u m_{r}^{\mathrm{f}}$ for $\bar{f}$. The factor in Fig. 4 is equivalent to the one in Fig. 2a according to the following lemma.

## Lemma 3 (Isolating uncertainty preserves factor properties)

$$
\mathrm{f}_{(4)}=_{F D} \mathrm{f}_{\{2 u\}}
$$

Proof sketch. The proof is by showing that in both cases, considering uncertainty explicitly by isolating nondeterminism (Fig. 4) and considering uncertainty implicitly by not isolating non-determinism (Fig. 2a), we deal with the same factor model. Details on the proof can be taken from Appendix A.

For the sake of simplicity of the discussion, we neglect further non-determinism possible for the three other actions $\bar{e}^{t}, m_{d}^{t}$, and $\underline{e}^{t}$. However, our discussion suggests that in future work we can explore a factor theory addressing those factor types that are likely to occur frequently in practical applications.

# 5. Mitigation orders 

This section investigates three basic orders over risk spaces, all intended to support the evaluation (e.g. comparison) of successors of a particular risk state reached after further endangerments or deployed mitigations. The fully and partially comparable inclusive mitigation orders (Sect. 5.1), both partial orders, are based on qualitative information, and the strong mitigation order (Sect. 5.2), a linear order, is based on quantitative information. These orders depend on the available information about risk and are related (Sect. 5.3).

### 5.1. Qualitative mitigation orders

Let $R(F)$ be a risk space (Definition 5) for a factor set $F \subseteq \mathcal{F}$. Then, we define a partial order $\preceq_{m} \subseteq R \times R$ as follows.

Definition 8 (Fully comparable inclusive mitigation order) For any pair of states $\sigma, \sigma^{\prime} \in R$, define

$$
\sigma \preceq_{m} \sigma^{\prime} \Longleftrightarrow \forall \mathrm{f} \in F: \sigma(\mathrm{f}) \preceq_{\mathrm{f}} \sigma^{\prime}(\mathrm{f})
$$

By $\sigma \prec_{m} \sigma^{\prime} \Longleftrightarrow \sigma \preceq_{m} \sigma^{\prime} \wedge \sigma \neq_{m} \sigma^{\prime}$, we induce the corresponding strict order. $\sigma$ and $\sigma^{\prime}$ are said to be incomparable if and only if $\sigma \not \preceq_{m} \sigma^{\prime} \wedge \sigma^{\prime} \not \preceq_{m} \sigma$. Intuitively, $\sigma \preceq_{m} \sigma^{\prime}$ signifies that " $\sigma^{\prime}$ is a better achievement in risk mitigation than $\sigma .{ }^{114}$ However, $\preceq_{m}$ requires full comparability of two states. It might be cumbersome to require such comprehensive knowledge to determine which state is "more or less risky" than another. Allowing for both epistemic and aleatory uncertainty, we might instead account for partial knowledge in the phase orders (Definition 3) at the level of $R$ by providing a relaxed partial order as follows.

Definition 9 (Partially comparable inclusive mitigation order) For states $\sigma, \sigma^{\prime} \in R$, define

$$
\sigma \precsim_{m} \sigma^{\prime} \Longleftrightarrow \forall \mathrm{f} \in F: \sigma(\mathrm{f}) \preceq_{\mathrm{f}} \sigma^{\prime}(\mathrm{f}) \vee\left(\left(\sigma(\mathrm{f}), \sigma^{\prime}(\mathrm{f})\right) \notin \preceq_{\mathrm{f}} \wedge\left(\sigma^{\prime}(\mathrm{f}), \sigma(\mathrm{f})\right) \notin \preceq_{\mathrm{f}}\right)
$$

We use $\prec_{m}^{-}$and $=_{m}^{-}$to distinguish the corresponding strict order and equality for $\precsim_{m}$ from $\prec_{m}$. Intuitively, Definition 9 requires a "betterment in risk from $\sigma$ to $\sigma^{\prime \prime}$ based exactly on the comparable phases.

Lemma 4 For any pair of risk states $\sigma, \sigma^{\prime} \in R$, we have that

$$
\sigma \preceq_{m} \sigma^{\prime} \Rightarrow \sigma \precsim_{m} \sigma^{\prime}
$$

Proof of Lemma 4. $\preceq_{\mathrm{f}}$ is antisymmetric. By definition of $\preceq_{m}$, we may assume

$$
\begin{aligned}
& \forall \mathrm{f} \in F: \sigma(\mathrm{f}) \preceq_{\mathrm{f}} \sigma^{\prime}(\mathrm{f}) \\
& \vdash \sigma(\mathrm{f}) \preceq_{\mathrm{f}} \sigma^{\prime}(\mathrm{f}) \\
& \vdash \sigma(\mathrm{f}) \preceq_{\mathrm{f}} \sigma^{\prime}(\mathrm{f}) \vee\left(\left(\sigma(\mathrm{f}), \sigma^{\prime}(\mathrm{f})\right) \notin \preceq_{\mathrm{f}} \wedge\left(\sigma^{\prime}(\mathrm{f}), \sigma(\mathrm{f})\right) \notin \preceq_{\mathrm{f}}\right) \quad \text { ( } \forall \text {-intro, assumption for each } \mathrm{f}) \\
& \vdash \forall \mathrm{f} \in F: \sigma(\mathrm{f}) \preceq_{\mathrm{f}} \sigma^{\prime}(\mathrm{f}) \vee\left(\left(\sigma(\mathrm{f}), \sigma^{\prime}(\mathrm{f})\right) \notin \preceq_{\mathrm{f}} \wedge\left(\sigma^{\prime}(\mathrm{f}), \sigma(\mathrm{f})\right) \notin \preceq_{\mathrm{f}}\right)
\end{aligned}
$$

## Corollary 2

$$
\sigma^{\prime} \neq_{m}^{-} \sigma \Rightarrow \sigma^{\prime} \neq_{m} \sigma
$$

[^0]
[^0]:    ${ }^{14}$ This notation might feel unusual as risk reduction is about lowering risk. So, if $\sigma^{\prime}$ is a state with lower risk than state $\sigma$ then we could write " $\sigma \succeq_{m} \sigma^{\prime \prime \prime}$. But we might agree that being in $\sigma^{\prime}$ is better than residing in $\sigma$. Moreover, for risk mitigation, reaching better states from worse is in the foreground. Thus, it seems reasonable to use the inverted notation $\sigma \preceq_{m} \sigma^{\prime}$.

Proof of Corollary 2.

$$
\begin{aligned}
& \sigma^{\prime} \neq_{m}^{\prime} \sigma \Rightarrow \sigma^{\prime} \neq_{m} \sigma \\
& \neg\left(\sigma^{\prime} \preceq_{m} \sigma \wedge \sigma \preceq_{m} \sigma^{\prime}\right) \Rightarrow \neg\left(\sigma^{\prime} \preceq_{m} \sigma \wedge \sigma \preceq_{m} \sigma^{\prime}\right) \\
& \sigma^{\prime} \preceq_{m} \sigma \wedge \sigma \preceq_{m} \sigma^{\prime} \Leftarrow \sigma^{\prime} \preceq_{m} \sigma \wedge \sigma \preceq_{m} \sigma^{\prime}
\end{aligned}
$$

In Sect. 7.6, we revisit how features such as partial orders account for uncertainty in RISKSTRUCTURES.

# 5.2. Quantitative mitigation orders 

So far, we have seen how partial orders account for a lack of knowledge and potential uncertainties about risk. Now, we will investigate the use of impact or consequence data in form of severity intervals, if available for specific factors, to interpolate knowledge gaps, model uncertainty, and derive a linear order over $R$.

We continue with definitions for dealing with intervals. Given two intervals $\left[l_{1}, u_{1}\right),\left[l_{2}, u_{2}\right) \subset \mathbb{R}_{+}$, the convex hull is a map $\sqcup: \mathbb{R}_{+}^{2} \times \mathbb{R}_{+}^{2} \rightarrow \mathbb{R}_{+}^{2}$ given by

$$
\left[l_{1}, u_{1}\right) \sqcup\left[l_{2}, u_{2}\right)=\left[\min \left\{l_{1}, l_{2}\right\}, \max \left\{u_{1}, u_{2}\right\}\right)
$$

For a family of $n \in \mathbb{N}$ intervals $I=\left(\left[l_{i}, u_{i}\right)\right)_{i \in[1 . . n]}$, we use the abbreviation $\bigsqcup I=\left[l_{1}, u_{1}\right) \sqcup \ldots \sqcup\left[l_{n}, u_{n}\right)$. Furthermore, let active: $R(F) \rightarrow 2^{F}$ with active $(\sigma)=\{\mathrm{f} \in F \mid \sigma(\mathrm{f})=f\}$ be the map returning the set of active factors of a risk state. Moreover, let $S: R \rightarrow \mathbb{R}_{+}^{2}$ with

$$
S(\sigma)=\bigsqcup(\mathrm{f} . s)_{\mathrm{f} \in \text { active }(\sigma)}
$$

be a map for the construction of the severity interval of a risk state from the intervals of its factors. ${ }^{15}$ Whereas the minimal severity of a factor f is given by $\mathrm{f} . s=[0,0)$, the minimal severity $S(\sigma)$ of a state $\sigma$ is the empty interval []), which we equate with the empty set, $]=\varnothing$. For any two real-valued intervals $[a, b),[c, d) \in \mathbb{R}_{+}^{2}$, Ishibuchi and Tanaka [IT90] define with $[a, b) \leq[c, d) \Longleftrightarrow a \leq c \wedge b \leq d$ a partial order over such intervals.

Moreover, we say that two risk states $\sigma, \sigma^{\prime} \in R$ are severity-equivalent if and only if their accumulated severity intervals are equal, that is, $\sigma \sim_{\mathrm{s}} \sigma^{\prime} \Longleftrightarrow S(\sigma)=S\left(\sigma^{\prime}\right)$. We have that $\sigma=\sigma^{\prime} \Rightarrow \sigma \sim_{\mathrm{s}} \sigma^{\prime}$ because the factors that are in their active phases are identical. The relation $\sim_{\mathrm{s}}$ is an equivalence relation because it is reflexive, symmetric, and transitive (all by the usual equivalence over intervals). Furthermore, $\sim_{\mathrm{s}}$ induces equivalence classes $[\sigma]_{\sim_{\mathrm{s}}}=\left\{\sigma^{\prime} \in R \mid \sigma^{\prime} \sim_{\mathrm{s}} \sigma\right\}$ over $R$ for any $\sigma \in R$ with the corresponding quotient class $R / \sim_{\mathrm{s}}$. With the family $(\mathrm{f} . s)_{\mathrm{f} \in F}$ of severity intervals of $F$, we now define an order over $R / \sim_{\mathrm{s}}$.
Definition 10 (Strong mitigation order) For $[\sigma]_{\sim_{\mathrm{s}}},\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}} \in R / \sim_{\mathrm{s}}$, define

$$
[\sigma]_{\sim_{\mathrm{s}}} \leq_{m}\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}} \Longleftrightarrow \forall \hat{\sigma} \in[\sigma]_{\sim_{\mathrm{s}}}, \hat{\sigma}^{\prime} \in\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}: S(\hat{\sigma}) \geq S\left(\hat{\sigma}^{\prime}\right) \vee S\left(\hat{\sigma}^{\prime}\right) \subset S(\hat{\sigma})
$$

$[\sigma]_{\sim_{\mathrm{s}}} \leq_{m}\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}$ can be dropped from $R / \sim_{\mathrm{s}}$, yielding

$$
\forall \hat{\sigma} \in[\sigma]_{\sim_{\mathrm{s}}}, \hat{\sigma}^{\prime} \in\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}: \hat{\sigma} \leq_{m} \hat{\sigma}^{\prime} \Longleftrightarrow S(\hat{\sigma}) \geq S\left(\hat{\sigma}^{\prime}\right) \vee S\left(\hat{\sigma}^{\prime}\right) \subset S(\hat{\sigma})
$$

$\leq_{m}$ codifies that $\sigma^{\prime}$ (a) reduces or (b) focuses risk if the union of its severity intervals is

1. Lower in the ranking $\leq$ of interval numbers or
2. Strictly narrower than the corresponding union for $\sigma$.

Condition (a) seems immediately intuitive. Condition (b) conveys the intuition that the interval carries less uncertainty about the consequences expected from $\sigma^{\prime}$ than from $\sigma$. Equivalence classes in $R / \sim_{\mathrm{s}}$ abstract from the factors from which the merged severity intervals originate. This abstraction has to be carefully taken into account when using $\leq_{m}$ and, therefore, when specifying severity. Note that $\leq_{m}$ is based on the convex hull of severity intervals from the active phases of a pair of risk states. Apart from the convex hull, interval addition and multiplication are relevant for alternative mitigation orders as we shall see below. However, a detailed investigation is left for future work. Let us now consider some properties of $\leq_{m}$.

[^0]
[^0]:    ${ }^{15}$ Note that $S$ over-approximates (i.e., constructs the convex hull from) sparsely distributed severity intervals.

Lemma $5 \leq_{m}$ is linear over $R / \sim_{\mathrm{s}}$.
Proof sketch. We show by case analysis that any two risk states are comparable and $\leq_{m}$ is antisymmetric. The complete proof is stated in Appendix A.

Corollary 3 After dropping Lemma 5 by Formula (6), we have that $\leq_{m}$ is also linear over $R$.
Lemma $6\left(R, \leq_{m}\right)$ and $\left(R / \sim_{\mathrm{s}}, \leq_{m}\right)$ are well ordered.
Proof sketch. Lemma 6 follows from a finite $R$ (by definition) and, thus, finite $R / \sim_{\mathrm{s}}$, and linearity of $\leq_{m}$ (by Lemma 5).
Definition 11 For $\sigma \in R(F)$, we also write $0^{F} \equiv \forall \mathrm{f} \in F: \sigma(\mathrm{f})=0^{f}$ and $\mathbf{F} \equiv \forall \mathrm{f} \in F: \sigma(\mathrm{f})=f$. We denote by $\top^{F}$ the set of maximal elements and by $\perp^{F}$ the set of minimal elements of $\left(R, \preceq_{m}, \precsim_{m}, \leq_{m}\right)$. We characterise the minimal elements in $\left(R(F), \preceq_{m}\right)$ by

$$
\perp^{F} \equiv\left\{\sigma \in R(F) \mid \forall \sigma^{\prime} \in R(F): \sigma^{\prime} \preceq_{m} \sigma \Rightarrow \sigma^{\prime}={ }_{m} \sigma\right\}
$$

and analogously for $\left(R, \precsim_{m}\right)$ and $\left(R, \leq_{m}\right)$ and the maximal elements.
Corollary 4 If $\forall \mathrm{f} \in F:\left(P h_{\mathrm{f}}, \preceq_{\mathrm{f}}\right)$ is linear, then $\left(R(F), \preceq_{m}\right)=\left(R(F), \precsim_{m}\right)$. If $R \neq R(\varnothing)$ then $\perp^{F}$ and $\top^{F}$ are non-empty and, therefore, have a proper manifestation. For $\left(R / \sim_{\mathrm{s}}, \leq_{m}\right), \perp^{F}$ and $\top^{F}$ are singletons.
Proof of Corollary 4. The proof is by contradiction. For the sake of brevity, we only consider a sketch of this proof. Assume we have two state classes $[\sigma]_{\sim_{\mathrm{s}}},\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}$ in $\perp^{F}$ with $[\sigma]_{\sim_{\mathrm{s}}} \neq_{m}\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}$. Because of our assumption, state classes are in linear order. Thus, by definition of $\perp^{F}$, one of these state classes causes a violation of the universal quantification in Definition 11 and, therefore, one of the classes cannot be in $\perp^{F}$ which contradicts our assumption. The proof is analogous for $\top^{F}$.
Corollary $5\left(R / \sim_{\mathrm{s}}, \leq_{m}\right)$ forms a complete lattice.
Proof of Corollary 5. Linearity of $\leq_{m}$ implies that every non-empty subset of $R / \sim_{\mathrm{s}}$ has a greatest lower bound and a least upper bound.

# 5.3. Relating mitigation orders 

The strong mitigation order characterised by the Lemmas 5 and 6 is driven by the number of active factors and their severity intervals (because of the definition of $S$ ) but not by the equality of factor phases among the compared risk states. This offers the possibility of abstraction from individual factors and focusing on severity estimates. To avoid infeasible models (e.g. specifications that get too strong to be realisable), we require that the addition of severity intervals constitutes a relational extension of either $\preceq_{m}$ or $\precsim_{m}$, formally,

$$
\left(\forall \hat{\sigma} \in[\sigma]_{\sim_{\mathrm{s}}}, \hat{\sigma}^{\prime} \in\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}: \hat{\sigma} \preceq_{m} \hat{\sigma}^{\prime} \vee \hat{\sigma} \precsim_{m} \hat{\sigma}^{\prime}\right) \Rightarrow[\sigma]_{\sim_{\mathrm{s}}} \leq_{m}\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}
$$

Dropped to $R$, this implies $\hat{\sigma} \preceq_{m} \hat{\sigma}^{\prime} \vee \hat{\sigma} \precsim_{m} \hat{\sigma}^{\prime} \Rightarrow \hat{\sigma} \leq_{m} \hat{\sigma}^{\prime}$ for all pairs $\left(\hat{\sigma}, \hat{\sigma}^{\prime}\right) \in[\sigma]_{\sim_{\mathrm{s}}} \times\left[\sigma^{\prime}\right]_{\sim_{\mathrm{s}}}$, therefore,

$$
\hat{\sigma} \preceq_{m} \hat{\sigma}^{\prime} \vee \hat{\sigma} \precsim_{m} \hat{\sigma}^{\prime} \Rightarrow S(\hat{\sigma}) \geq S\left(\hat{\sigma}^{\prime}\right) \vee S\left(\hat{\sigma}^{\prime}\right) \subset S(\hat{\sigma})
$$

for full and partial comparability, otherwise implying

$$
\left(\hat{\sigma}, \hat{\sigma}^{\prime}\right) \notin \preceq_{m} \wedge\left(\hat{\sigma}, \hat{\sigma}^{\prime}\right) \notin \precsim_{m} \Rightarrow \mathrm{~T}
$$

Intuitively, if $\hat{\sigma}$ is "worse" than $\hat{\sigma}^{\prime}$ then its accumulated severity interval $S(\hat{\sigma})$ has to be greater than that of $\hat{\sigma}^{\prime}$ and, therefore, must not be contained in that of $\hat{\sigma}^{\prime}$. Moreover, if $\hat{\sigma}$ and $\hat{\sigma}^{\prime}$ are incomparable in $\preceq_{m}$ and $\precsim_{m}$ (i.e., some factors have inversely ordered or incomparable phases) then $S(\hat{\sigma})$ and $S\left(\hat{\sigma}^{\prime}\right)$ are allowed to form any relationship (signified by T for "true"), for example, Formula (7).

What is the (necessary and) sufficient condition on $F$ to satisfy the requirement expressed by Formula (7)? Risk spaces and risk state pairs are the interpretations and, therefore, potential models satisfying the relational extension imposed by Formula (7). Answering this question suggests the following lemma.
Lemma 7 For $\sigma, \sigma^{\prime} \in R(F)$,

$$
\sigma \preceq_{m} \sigma^{\prime} \vee \sigma \precsim_{m} \sigma^{\prime} \Rightarrow \operatorname{active}(\sigma) \supseteq \operatorname{active}\left(\sigma^{\prime}\right)
$$

![img-5.jpeg](img-5.jpeg)

Fig. 5. Visualisation of the case distinction to establish Theorem 1, with $\mathrm{f}, \mathrm{g}, \mathrm{h} \in \mathcal{F}, \operatorname{TS}(R, \rightarrow)$, and $\sigma \rightarrow \sigma^{\prime}$

Proof sketch. The proof is by induction over $F$ and relies on the assumptions that, for any $\mathrm{f} \in F, f$ is the unique maximal element in $\preceq_{\mathrm{f}}$ and that the map active (Sect. 5.2) only returns such elements. The whole proof is stated in Appendix A.

Again, fix a finite $F$ and a pair $\sigma, \sigma^{\prime} \in R(F)$ and assume $\sigma \preceq_{m} \sigma^{\prime} \vee \sigma \preceq_{m} \sigma^{\prime}$. Then, by Lemma 7, $\sigma^{\prime}$ incorporates a subset of $\sigma$ 's active factors. To show that $S\left(\sigma^{\prime}\right)$ preserves $S\left(\sigma^{\prime}\right) \subset S(\sigma)$, the right-hand part of the disjunction in the consequent of Formula (7), it is sufficient to investigate $S\left(\sigma^{\prime}\right)$ for any factor deactivation possible in a transition from $\sigma$ to $\sigma^{\prime}$. We can summarise all such possibilities in five cases:

1. all intervals remain $\left(\sigma^{\prime}=\sigma\right)$,
2. only intervals in the convex hull of the remaining intervals are removed,
3. intervals only increasing the lower bound of this hull are removed,
4. intervals only decreasing the upper bound of this hull are removed, and
5. intervals increasing the lower bound and decreasing the upper bound of this hull are removed.

This case distinction is visualised in Fig. 5 and also works for $\sigma^{\prime}$ such that $\sigma \prec_{m} \sigma^{\prime}$. Formula (7) is also satisfied if all factors in $F$ are assigned the same interval, call it $s^{F}$. In conclusion, the sufficient condition on $F$ to satisfy Formula (7) is the "unique maximal element" precondition in the proof of Lemma 7. Apart from this precondition, Formula (7) holds of an arbitrary finite $F \subseteq \mathcal{F}$. Below, we shall call $\preceq_{m}$ and $\precsim_{m}$ inclusive mitigation orders, and $\leq_{m}$ a strong mitigation order. We arrive at the following theorem.
Theorem 1 The strong mitigation order $\leq_{m}$ extends the partially comparable inclusive mitigation order $\precsim_{m}$ which, in turn, extends the fully comparable inclusive mitigation order $\preceq_{m}$. Formally, for $\sigma, \sigma^{\prime} \in R$ :

$$
\sigma \preceq_{m} \sigma^{\prime} \stackrel{\text { Lemma }}{ }{ }^{4} \sigma \precsim_{m} \sigma^{\prime} \stackrel{\text { Lemma }}{ }{ }^{7} \sigma \leq_{m} \sigma^{\prime}
$$

# 5.4. Application: evaluating local, regional, and global safety 

The orders $\preceq_{m}, \precsim_{m}$, and $\leq_{m}$ allow a local evaluation of safety in the sense that their definitions only require the comparison of pairs of risk states. Two further qualitative notions of safety seem to be useful.

Let $R$ be non-empty and finite and reach: $R \times \mathcal{P} \rightarrow 2^{R}$. Given a process $P \in \mathcal{P}$ and a risk state $\sigma \in R$, $\operatorname{reach}(\sigma, P) \subseteq R$ denotes the set of risk states reachable from $\sigma$ by finite executions (prefixes) of $P$ where $\sigma$ itself is always reachable and, thus, $\sigma \in \operatorname{reach}(\sigma, P)$. Figure 6 (light-grey area) exemplifies such a set. Then, we use the presented orders to determine non-empty sets of minimal and maximal elements in $R$ reachable by $P$, such as $\max _{\preceq_{m}} \operatorname{reach}(\sigma, P)$ or $\min _{\precsim} \operatorname{reach}(\sigma, P)$. In Fig. 6, the risk states 1 to 3 and 5 to 7 , connected by double arcs, are the ones reachable from $\sigma$ after at most two consecutive endangerments or mitigations. Reachability arcs are labelled with the weakest applicable order. Single arcs illustrate potential modifications or extensions of the reachability set, for example, by the states 4 and 8 to 10 after a reassessment of the operational environment by the machine.

In the situation described by the process $P$ in the risk state $\sigma$, these two sets signify the regionally safest (max, white circles) and the regionally most hazardous (min, dark-grey circles) states, respectively. The smallest such set will only and exactly contain $\sigma$, meaning $P$ cannot reduce risk in $\left(R, \precsim_{m}\right) . \preceq_{m}$ and $\precsim_{m}$ enable a regional evaluation of safety inasmuch as once a maximal element in $\max _{\precsim} \operatorname{reach}(\sigma, P)$ is reached, $\precsim_{m}$ limits reasoning about safer states that $P$ could reach from $\sigma$.

![img-6.jpeg](img-6.jpeg)

Fig. 6. Visualisation of local, regional, and global safety in a risk space $R$
Besides local and regional safety, $\left(R / \sim_{\mathrm{s}}, \leq_{m}\right)$ supports global evaluation because of its linearity (Lemma 5). With $\leq_{m}$, there are always unique safest and riskiest states in $\operatorname{reach}(\sigma, P) / \sim_{\mathrm{s}}$ (Corollaries 4 and 5). In contrast, $\preceq_{m}$ and $\preceq_{m}$ will not guarantee this uniqueness. Note that the use of equivalence classes leads to more abstract forms of safest and riskiest states. Overall, Lemma 6 and Corollary 5 provide necessary conditions for deriving finite strategies (i.e., policies, choice resolutions) that stabilise or terminate $P$ in a safest state.

Quantitative mitigation orders (e.g. $\leq_{m}$ ) will have to be calculated at run-time, according to $\mathfrak{R}$ by estimating probabilities of factor occurrence and severity of factor consequences from situational data only available during operation. In $P$, safety can then be observed as the gradual presence or absence of risk over traces $(P)$. On a side note, the reliability as the gradual presence or absence of defective behaviour can be seen as a special case when considering only factors that model faults.

# 5.5. Discussion: ethical aspects of mitigation orders 

Linear mitigation orders such as $\leq_{m}$ promote machines with negative utilitarian decision ethics [War12, p. 51]. For example, severity intervals could be calculated at run-time based on sensor data about the possible operational situation of the machine. Expected outcomes of enabled mitigations, if any, will then be comparable according to $\leq_{m}$. This comparability allows the assessment of the actual reachability of states with strictly lower risk. Any resolution of a near-accident situation (Sect. 4.3) or a tram ${ }^{16}$ problem [Foo78] would then consist in the choice of the mitigation leading to the state with the lowest risk or the least severe of the expected negative outcomes. This scheme characterises negative utilitarianism.

Linear mitigation orders globally resolve decisions based on explicit and, therefore, disputable criteria. Consequently, utilitarian ethics have been criticised to lead to oversimplified approaches to resolve indecision. Such critiques stress the difficulty of predicting the positive and negative effects (i.e., "double effects" [Foo78]) of certain actions, in our case, the estimation of the severity of an activated factor and the reached state [War12, pp. 48-49]. Appreciating the equality of any two groups of the human family [Uni48], one could conclude that tram problems should be solved by random decisions, independent of whether these are made by humans or machines. However, in analogy to risk-averse humans (Sect. 3), a risk-aware machine should make (self-inflicted) tram problems unlikely, that is, avoid such decisions rather than aiming at their random or utilitarian resolution. The likelihood of tram problems is an important subject to be investigated.

Accordingly, a structured risk model with dependencies between factors could be used to complement utilitarian decision ethics with Kantian ethics, that is, to use $\leq_{m}$ to decide about conservative measures before high-severity factors get activated. This results in what is called "rule utilitarianism" [War12, p. 52]. For example, we can model the necessary preconditions of certain tram problems as risk factors and a machine based on this model could use these factors to constrain its behaviour. Although the presented model can be used with linear orders, the discussions below stay agnostic of the mitigation order.

[^0]
[^0]:    ${ }^{16}$ Also known as the "trolley problem", a situation where any of the enabled actions leads to an unacceptable outcome.

# 6. Factor dependencies 

Usually, only subsets of a risk space $R$ and a process $P$ 's traversals of $R$ are relevant. Identifying these subsets is the task of risk analysis and can be difficult if the relevance of each risk state can only be determined at runtime based on its context in $R$ and the state of $P$. As highlighted in Sect. 3, it is then useful to model (causal) relationships between (phases of) factors, their events (i.e., activation, mitigation), and, consequently, risk states. For example, we might want to specify that (i) the activation of a risk factor causes the activation of another factor, (ii) the mitigation of one factor causes the activation of several other factors, or (iii) the activation of a factor requires the activation of some other factors. We can take account of dependencies, such as illustrated in Table 2 (e.g. requires ncol, causes $\log _{d}$ ), by imposing constraints on pairs of consecutive risk states and their comprising factors' phases. For this, we use binary relations over $R$ to hypothesise causality assumptions about less known or controllable parts of $P$ (i.e., the environment $E n$ ) and express causality requirements for known and controllable parts of $P$ (i.e., the system $S y$ ).

### 6.1. Relations over risk spaces

Let $F \subseteq \mathcal{F}$ and consider the space $R(F)$ and two distinct factors $\mathrm{f}, \mathrm{g} \in F$. In the following, we employ relational specification to formalise factor dependencies as relations over $R$, that is, as subsets of $R \times R$. For example, a causes ${ }^{17}$ constraint requires of a pair $\left(\sigma, \sigma^{\prime}\right) \in R \times R$ that if f is active then, within at most one (logical) step, g must be active until f gets either inactive or mitigated.

Let $\mathcal{C}$ be the set of all constraints. For the translation of constraints into a form useful for the discussion below, we use the map $\llbracket \cdot \rrbracket_{\mathrm{c}}^{R}: \mathcal{C} \rightarrow 2^{R \times R}$ to denote the relational semantics of constraints over $R$. To distinguish different semantic maps, as will be defined later, we use subscripts, for example, c in $\llbracket \cdot \rrbracket_{\mathrm{c}}^{R}$. Recall that we use $\sigma(\mathrm{f})$ to refer to the phase of factor f in state $\sigma$ (Sect. 4.2).

For example, causes constraints can be encoded as relations over $R$ by the definition

$$
\llbracket \mathrm{f} \text { causes } \mathrm{g} \rrbracket_{\mathrm{c}}^{R}=\left\{\left(\sigma, \sigma^{\prime}\right) \in R \times R \mid \underbrace{\sigma(\mathrm{f}) \neq f \wedge \sigma^{\prime}(\mathrm{f})}_{\text {activation of } \mathrm{f} \ldots}=f \wedge \underbrace{\sigma(\mathrm{~g}) \neq \bar{g}}_{\text {when } \mathrm{g} \text { not mitigated }} \Rightarrow \underbrace{\sigma^{\prime}(\mathrm{g})=g}_{\text {...activates } \mathrm{g}}\right\}
$$

This constraint implies that factor activation takes a logical time step corresponding to a strictly positive real-time duration (i.e., $>0$ ) in $P$. Note that this definition of causes encodes the assumption that g , once or as long as mitigated, cannot be caused (again) by activating f. While this behaviour is often to be expected of any mitigation designed for g , one can define a more general constraint, say alwaysCauses, to capture this behaviour. Moreover, causes is to be read as "is sufficient to cause" rather than as "is necessary to cause", and it extends to factor sets. Given $F, G \subseteq \mathcal{F}$ with $F \cap G=\varnothing$, we define

$$
\llbracket F \text { causes } G \rrbracket_{\mathrm{c}}^{R}=\left\{\left(\sigma, \sigma^{\prime}\right) \in R \times R \mid \exists \mathrm{f} \in F \forall \mathrm{~g} \in G: \sigma(\mathrm{f}) \neq f \wedge \sigma^{\prime}(\mathrm{f})=f \wedge \sigma(\mathrm{~g}) \neq \bar{g} \Rightarrow \sigma^{\prime}(\mathrm{g})=g\right\}
$$

Note that all pairs $\left(\sigma, \sigma^{\prime}\right)$ violating the antecedent of the conditional are in $\llbracket \mathrm{f}$ causes $\mathrm{g} \rrbracket_{\mathrm{c}}^{R}$ as well.
As another example, the requires constraint can be defined in relational form by

$$
\llbracket \mathrm{f} \text { requires } \mathrm{g} \rrbracket_{\mathrm{c}}^{R}=\left\{\left(\sigma, \sigma^{\prime}\right) \in R \times R \mid \underbrace{\sigma^{\prime}(\mathrm{f})=f}_{\text {an active } \mathrm{f} \text { requires... }} \Rightarrow \underbrace{\sigma(\mathrm{~g})=g}_{\text {an active } \mathrm{g} \text { in the preceding state }}\right\}
$$

The lifting of requires to factor sets $F, G \subseteq \mathcal{F}$ with $F \cap G=\varnothing$ is described as

$$
\llbracket F \text { requires } G \rrbracket_{\mathrm{c}}^{R}=\left\{\left(\sigma, \sigma^{\prime}\right) \in R \times R \mid \exists \mathrm{f} \in F: \sigma^{\prime}(\mathrm{f})=f \Rightarrow \forall \mathrm{~g} \in G: \sigma(\mathrm{g})=g\right\}
$$

This variant of the requires constraint refers to all factors specified on its right-hand side and, this way, resembles an ADD-gate as used in FTA. The side condition $F \cap G=\varnothing$ avoids that a factor requires or causes itself (i.e., it avoids the "chicken and egg" problem).

[^0]
[^0]:    ${ }^{17}$ Used in form of MCSs in FTA and, less frequently formally, in FMEA (see Sect. 2.1).

Table 3. A selection of constraints more commonly used in causal reasoning


Legend: See the dimensions discussed in the text of Sect. 6.1; $\checkmark \ldots$ implemented in YAP [Gle21]

Remark 1 causes models weak causality and requires models a strong causality. causes and requires constitute basic dependency templates and exemplify how dependencies support the safety engineer or risk analyst in causal modelling in a state-based relational way.

Analogously, there are many possible factor dependencies over $R$ that resemble causal reasoning of techniques such as FTA (Sect. 2.1). Such dependencies can be classified along several dimensions:

- phase combination (PC): active to active $(F \rightleftarrows G)$, active to mitigated $(F \rightleftarrows \bar{G})$, active to inactive $\left(F \rightleftarrows 0^{G}\right)$, mitigated to mitigated $(\bar{F} \rightleftarrows \bar{G})$, mitigated to active $(\bar{F} \rightleftarrows G)$, mitigated to inactive $\left(\bar{F} \rightleftarrows 0^{G}\right)$; combinations thereof are possible;
- direction (D) of cause-effect analysis: forward ( $\rightarrow$, e.g. for modelling sufficient conditions or propagation), backward ( $\leftarrow$, e.g. for modelling necessary conditions or explanation);
- polarity $(\mathrm{P})$ : obligation $(+)$, permission ( $\circ$ ), inhibition $(-)$;
- causality (C): strong (s, sequential events), weak (w, simultaneous events);
- multiplicity (M): one-to-one (1:1), one-to-many (1: $n$ ), many-to-one ( $n: 1$ ), many-to-many ( $m: n$ ) where $m, n>0$; self-referential ${ }^{18}(1: 0)$;
- factor combination (FC): " $\sim m$ out of $n$ " where $\sim \in\{\leq,=, \geq\}$ and $1 \leq m \leq n$.

These dimensions ${ }^{19}$ characterise factor dependencies commonly used in risk analysis. Most of the constraints listed in Table 3 are realised in our tool YAP [Gle21], which enables their use based on previous discussions in [Gle18, Gle17]. However, their comprehensive treatment would exceed the scope of this work.

We have now seen that constraints prune irrelevant state pairs. This mechanism is reflected by the following definition.
Definition 12 (Relational semantics of constraints) For a set of constraints $C \subseteq \mathcal{C}$,

$$
\llbracket C \rrbracket_{c}^{R}=\left\{\begin{array}{l}
R \times R, \quad C=\varnothing \\
\bigcap_{k \in C} \llbracket k \rrbracket_{c}^{R}, \text { otherwise }
\end{array} \quad \subseteq R \times R\right.
$$

Constraints are an instrument for specifying structures over risk spaces. Regarding the composition of spaces, this instrument requires the definition of the following well-formedness condition.

[^0]
[^0]:    ${ }^{18}$ In this case, we allow $F=G=|\mathrm{f}\rangle$.
    ${ }^{19}$ Naïve combination of all dimensions results in more than 1000 possibilities to define constraints. Many of these possibilities are not essentially different and some might not even be useful. Table 3 does, however, not aim to cover all useful constraints.

Listing 1: YAP script modelling the situation transferObj from Table 4

```
factormodel {
    dmgo desc "object damage"
    mishap
    requiresNOf(1|hp,fodg)
    sev=[5,10);
    fodg desc "failure on demand of grabber"
    requires(slp)
    causes(dmgo);
    slp desc "slippery grabber"
    requires(wet)
    direct
    detectedBy(.senseSlip)
    mitigatedBy(.incFr)
    sev=[2,6);
    wet desc "wet grabber surface"
    causes(slp)
```

```
    direct;
    hp desc "high grabber pressure"
    mitPreventsMit(slp)
    direct
    detectedBy(.senseFr)
    mitigatedBy(.linFr)
    sev=[3,8];
    /* str desc "spurious release"; equal to fod */
}
27}\mathrm{ controlloop collRob {
28}\mathrm{ mode senseSlip desc "identify slip";
29}\mathrm{ mode incFr desc "increase grabbing pressure"
30 update "pressure**";
31}\mathrm{ mode senseFr desc "sense pressure"
32}\mathrm{ guard "pressure > threshold(obj)";
33}\mathrm{ mode limFr desc "limit grabbing pressure"
34 update "pressure = threshold(obj)";
```

Table 4. Situation/action/factor table for grabbing scenarios performed by collaborative robots


Legend: $h \ldots$ high, $m \ldots$ medium, -not analysed; see also Table 2 for guidance

Definition 13 (Well-formedness of constraints) Let $R(F)$ be a space formed by a factor set $F \subseteq \mathcal{F}$. We say that a constraint $k \in \mathcal{C}$ is well-formed for $R(F)$ if and only if it does not refer to factors other than the ones in $F$, formally, if and only if $\llbracket k \rrbracket_{k}^{R} \subseteq R(F) \times R(F)$. We say that $C \subseteq \mathcal{C}$ is well-formed for $R(F)$ if and only if each element in $C$ is well-formed for $R(F)$.

### 6.2. Example: collaborative robots

To illustrate relationships for structuring risk perception, we apply our framework to a scenario in human-robot collaboration. Table 4 shows a risk analysis similar to Table 2 for a robotic arm with a grabber. Consider such a robot ( $w$ )orking by repetitively ( $g$ )rabbing, holding, and ( $r$ ) eleasing work pieces. Water or oil on the robot's grabber (wet) can cause the grabber to be slippery (slp) such that holding an object may increase the likelihood of accidentally dropping it ( $\operatorname{Pr}\{s l p \mid s l p\}$ ). For our further analysis, we generalise the negative outcome from the phase $s l p$ to an additional final risk factor $\mathrm{dmg}_{\mathrm{o}}$. Obviously, increased grabbing pressure can mitigate slp. However, forward reasoning leads to the conclusion that increased pressure could be too high (hp) causing damage to the object $\left(\mathrm{dmg}_{\mathrm{o}}\right)$. However, because we plan to install an intervention in our machine, we omit the dependency hp causes $\mathrm{dmg}_{\mathrm{o}}$. Moreover, a FTA of the sensor software and the actuator hardware results in the factor mistaken loosening of the grabber $\left(\mathrm{st}_{\mathrm{r}}\right)$, which, for the sake of simplicity, we equate with a failure on demand of the "grab \& hold" action (fod ${ }_{g}$ ). Applying final backward causal reasoning, the object's high falling onto a hard surface causes damage of the object $\left(\mathrm{dmg}_{\mathrm{o}}\right)$ and requires ${ }_{1}$ (at least one of) slippery grabber (slp), fod ${ }_{g}$, or a spurious trip of the "release" action $\left(\mathrm{st}_{\mathrm{r}}\right)$.

Listing 1 encodes this analysis in a script processable by YAP, which calculates the risk space and the phase transition relation. The resulting risk graph in Fig. 7 can be useful as a controller design template for a risk-aware machine. Further details on how this graph can be constructed are discussed in Sect. 7.

![img-7.jpeg](img-7.jpeg)

Fig. 7. Graph for risk structure $\mathfrak{R}_{\text {transferObj }}$ with factor set $F=\{\mathrm{dmg}$, fod, slp, wet, hp $\}$ generated by YAP from Listing 1. To increase readability, inactive factors are not shown in the nodes

# 6.3. Discussion: abstraction, compatibility, and characteristics of risk factors 


#### Abstract

Abstraction Two structurally different risk states $\sigma, \sigma^{\prime} \in R$ (i.e., $\sigma \neq \sigma^{\prime}$ ) can be severity-equivalent (i.e., $\sigma \sim_{\mathrm{s}} \sigma^{\prime}$ ). Moreover, the family (f.s) $f_{k F}$ of severity intervals of $F$ forms a cut of causal chains and, thus, defines the scope of $\mathfrak{R}$. These intervals abstract from potential consequences of active factors. This abstraction is left to the modeller (i.e., the risk analyst or safety engineer) and can vary significantly, depending on the assets (e.g. humans, animals, environment) and impact categories (e.g. certain injuries, damage, loss) under discussion. For example, assume two independent consequences $c_{A}$ and $c_{B}$ (e.g. a class of injuries of an operator $A$, a class of damages of an object $B$ ) associated with possible ${ }^{20}$ intervals $\left[l_{A}, u_{A}\right)$ and $\left[l_{B}, u_{B}\right)$. Consider a single factor f causing both $c_{A}$ and $c_{B}$. This circumstance suggests the consistency condition $\mathrm{f} . s \subseteq\left[l_{A}+l_{B}, u_{A}+u_{B}\right)$, requiring that all consequences of f (i.e., $c_{A}, c_{B}$ ) have to be measurable in their severity along the same scale. Our example stresses the difficulty of comparing injury with damage. However, if $c_{B}$ was another class of injuries of that operator then $c_{B}$ would fit into the same scale as $c_{A}$. Practitioners often formalise these concepts for quantitative analysis. However, we leave this for future work.


Factor compatibility Consequences of several factors should be compatible such that the convex hull of their intervals (recall $\sqcup$ from Formula (4)) has a consistent meaning of severity in $\left(R, \leq_{m}\right)$. Consider the two factors f and g . Both can describe three cases with their individually specified intervals f.s and g.s:

1. f and g share all their consequences (e.g. both cause $c_{A}$ ).
2. f and g share some of their consequences (e.g. f causes $c_{A}$ and $c_{B}, \mathrm{~g}$ causes $c_{B}$ ).
f. $\rightarrow$ (CA) $\mathrm{g} \rightarrow$ (CA)
3. f and g do not share any consequences (e.g. f causes $c_{A}, \mathrm{~g}$ causes $c_{B}$ ).
f. $\rightarrow$ (CA) $\mathrm{g} \rightarrow$ (CR)

If both factors get active in case 1 , the convex hull can be backed by the condition f.s $\sqcup \mathrm{g} . s \subseteq\left[l_{A}, u_{A}\right)$. Case 2 can be split into the $\leq_{m}$-compatible case 1 for $c_{B}$ and case 3 for $c_{A}$. In case 3, generally, the convex hull may extend both the range of consequences and the severity intervals. However, the consistency condition f.s $\sqcup \mathrm{g} . s \subseteq\left[l_{A}, u_{A}\right) \sqcup\left[l_{B}, u_{B}\right)$ implied by $\leq_{m}$ seems inappropriate. For example, if $c_{A}$ and $c_{B}$ signify damage of two independent objects with the same interval, the hull would not account for this because of idempotency of interval union.

[^0]
[^0]:    ${ }^{20}$ For $\left[l_{A}, u_{A}\right)$ and $\left[l_{B}, u_{B}\right)$, we assume sufficient knowledge about possible consequences and their accurate evaluation.

![img-8.jpeg](img-8.jpeg)

Fig. 8. Risk graphs for $F=\left\{\mathrm{st}_{\mathrm{rA}}, \mathrm{loc}_{\mathrm{d}}\right\}$ after applying causes (a), requires (b), and both (c), using YAP
In summary, while $\leq_{\mathrm{m}}$ can deal with consequences shared by all risk factors (case 1), partially shared (case 2) or independent consequences (case 3) require a further investigation out of scope.
Condition 1 (Factor convergence) The use of $\leq_{\mathrm{m}}$ with several risk factors requires severity specifications to be based on a single compound consequence and a single severity scale across all factors.

The problematic case 3 could be modelled by an additional factor $h$ that is caused by $f$ and $g$ and carries an up-shifted severity interval, for example, $h . s=f . s+g . s$, and $f, g$, and $h$ are all defined with respect to a single new consequence $c_{A+B}$. In Sect. 6.1 and Table 3, we have seen how such a dependency can be specified by constraints on the risk space, that is, by $\{f, g\}$ causes $h$ and $h$ excludes $\{f, g\}$. excludes assures that severity calculation for states in phase $h$ is only based on the interval h.s.

Based on this analysis, we call a factor set $F \leq_{\mathrm{m}}$-compatible if the way of combining the severity intervals for each subset $F^{\prime} \subseteq F$ fulfils Condition 1. For support in achieving and maintaining compatibility, the next paragraphs exemplify how factor severity and dependencies play together with mitigation orders. We also explore conditions for the well-formedness of severity intervals.

Factor characteristics and dependencies Constraints over risk spaces have implications on the characteristics of risk factors such as their severity intervals. Conversely, severity intervals govern $\leq_{\mathrm{m}}$ and can impose wellformedness conditions on the definition of constraints. In the following, we explore the impact of two different well-formedness conditions ( $\mathrm{f} . s \subseteq \mathrm{~g} . s$ and $\mathrm{f} . s \supseteq \mathrm{~g} . s$ ) on $\leq_{\mathrm{m}}$ and the influence of choosing either one on the monotonicity of mitigation strategies. For example, for a constraint

$$
\begin{array}{ll}
\text { f causes } \mathrm{g}, & \text { the condition } \mathrm{f} . s \subseteq \mathrm{~g} . s, \quad \text { and for } \\
F \text { causes } G, & \text { the condition } \bigcup_{\mathrm{f} \in F} \mathrm{f} . s \subseteq \bigcup_{\mathrm{g} \in G} \mathrm{~g} . s
\end{array}
$$

seems coherent with the (probabilistic) relationship between the activation of causal and consequential factors. Particularly, the condition in Formula (12) expresses that if f causes g then f should have at most the potential impacts of g .

Consider the airbag spurious trip ( $\mathrm{st}_{\mathrm{rA}}$ with $s=[5,12)$ ) causing loss of driving control ( $\mathrm{loc}_{\mathrm{d}}$ with $s=[2,17)$ ) from the example in Table 2. For $\mathrm{st}_{\mathrm{rA}}$ causes $\mathrm{loc}_{\mathrm{d}}$, the two intervals would fulfil the aforementioned condition. The structure fulfilling this constraint is shown in Fig. 8a, it includes the states $\mathbf{0}$ with $S(\mathbf{0})=[0,0), l o c_{d}$ with $S\left(l o c_{d}\right)=[2,17)$, and $l o c_{d} s t_{r A}$ with $S\left(l o c_{d} s t_{r A}\right)=[2,17)$, with three equivalence classes in $R\left(\left\{\mathrm{st}_{\mathrm{rA}}, \mathrm{loc}_{\mathrm{d}}\right\}\right) /=_{\infty}$ ordered according to

$$
l o c_{d} \overline{s t_{r A}}, l o c_{d} s t_{r A}, l o c_{d} \quad<_{\mathrm{m}} \quad \overline{l o c_{d}} s t_{r A}, s t_{r A} \quad<_{\mathrm{m}} \quad \overline{l o c_{d}}, \overline{s t_{r A}}, \mathbf{0}, \overline{l o c_{d} s t_{r A}}
$$

On the contrary, assume a risk structure where $\mathrm{st}_{\mathrm{rA}} . s=[2,17)$ and $\mathrm{loc}_{\mathrm{d}} . s=[5,12)$ in order to be compliant with the converse condition $\mathrm{f} . s \supseteq \mathrm{~g} . s$. From this structure, we obtain the order

$$
\overline{\operatorname{loc}_{d}} s t_{r A}, \operatorname{loc}_{d} s t_{r A}, s t_{r A} \quad<_{\mathrm{m}} \quad \operatorname{loc}_{d} \overline{s t_{r A}}, \operatorname{loc}_{d} \quad<_{\mathrm{m}} \quad \overline{\operatorname{loc}_{d}}, \overline{s t_{r A}}, \mathbf{0}, \overline{\operatorname{loc}_{d} s t_{r A}}
$$

In both orders, mitigation paths (i.e., sequences of solid arcs) in Fig. 8a, for example,

$$
m^{\mathrm{loc}_{d}} \rightarrow m^{\mathrm{st}_{\mathrm{rA}}} \rightarrow m_{r}^{\mathrm{st}_{\mathrm{rA}}} \rightarrow m_{r}^{\mathrm{loc}_{d}} \rightarrow S K I P
$$

remain in their equivalence class or lead to a state in a better class according to $\leq_{m}$. Mitigations (solid arcs) deactivate at least one factor and, thus, lead to a better state according to $\prec_{\mathrm{m}}$. We call such paths through $\mathfrak{R}$ mitigation monotonous [GK17, Def. 8]. However, if intervals are specified in coherence with Formula (12), seven instead of five out of the twelve mitigations strictly reduce risk.

Analogously, for a constraint f requires g , the condition $\mathrm{f} . s \supseteq \mathrm{~g} . s$ seems useful. The two factors in our example fulfil this condition for $\operatorname{loc}_{\mathrm{d}}$ requires $\mathrm{st}_{\mathrm{rA}}$. The structure fulfilling this constraint is shown in Fig. 8b, with the states ordered according to

$$
\operatorname{loc}_{d} s t_{r A} \quad<_{\mathrm{m}} \quad \overline{\operatorname{loc}_{d}} s t_{r A}, s t_{r A} \quad<_{\mathrm{m}} \quad \overline{s t_{r A}}, \mathbf{0}, \overline{\operatorname{loc}_{d} s t_{r A}}
$$

whereas intervals specified the opposite way (following $\mathrm{f} . s \subseteq \mathrm{~g} . s$ ) would lead to a less distinctive order

$$
\overline{\operatorname{loc}_{d}} s t_{r A}, \operatorname{loc}_{d} s t_{r A}, s t_{r A} \quad<_{\mathrm{m}} \quad \overline{s t_{r A}}, \mathbf{0}, \overline{\operatorname{loc}_{d} s t_{r A}}
$$

Again, mitigation paths are monotonous and coherent with the above condition; four instead of three out of seven mitigations strictly reduce risk according to $\leq_{m}$. Overall, a violation of the mentioned conditions does not influence mitigation monotonicity of this risk structure with respect to $\leq_{m}$ but it reduces non-determinism in a strategy over $\mathfrak{R}$.

Figure 8c shows a risk graph for the discussed causes/requires constraint pair fulfilling both conditions. Note that the states are equivalent to Fig. 8b but the arc $0 \xrightarrow{e^{s t_{r A}}} s t_{r A}$ in Fig. 8b is replaced by $0 \xrightarrow{e^{\operatorname{loc}_{d} s_{r A}}} s t_{r A} \operatorname{loc}_{d}$ and the edge $s t_{r A} \operatorname{loc}_{d} \xrightarrow{m_{r}^{\mathrm{loc}_{d}}} m_{r}^{\mathrm{loc}_{d}} \overline{s t_{r A} \operatorname{loc}_{d}}$ is added. In summary, the causes constraint streamlines the transition relation of the risk structure as opposed to the requires constraint. This can be useful for merging factors during reduction of a risk structure. However, Fig. 8a shows that causes is less restrictive than requires, particularly, allowing $e^{\operatorname{loc}_{d}}$ to occur without a previous $e^{\mathrm{st}_{\mathrm{rA}}}$, for example, due to other causes not made explicit as factors in the model.

An in-depth analysis of techniques for making $F$ compatible, a discussion of a set of rules relating factor characteristics and factor dependencies, as well as an alternative to $\leq_{m}$ are subject of future work.

# 7. RISKSTRUCTURES: the language 

In the previous sections, we have explored how a risk space $R$ can be used for assessing risk mitigation capabilities of a process $P$ (cf. Fig. 1) and for equipping $P$ with a form of risk awareness. Risk in specific situations has a specific causal structure. We have seen how dependencies in a factor set $F$ focus on this structure. Starting from the full extension of $R$, we select subsets of $R$, making assumptions if the structure is not entirely known in advance. This focus and these assumptions can be expressed by a constrained composition. Specifically, based on constraints on the combinations of factor phases, on the phase transitions, and on the synchronisation of events corresponding to the CSP model of concurrency, we can specify

- which region of $R$ we want to pay attention to (i.e., the scope of safety guarantees) and
- which region of $R$ we consider to be safe for a process $P$ (i.e., conventional safety).

We use LTSs for investigating the operational semantics of RISKSTRUCTURES, beginning with factors and their constrained composition, and accompanied by a discussion of the consistency, well-formedness, and validity of their algebraic semantics.
Definition 14 (Risk structure) Given a factor set $F \subseteq \mathcal{F}$, a risk structure $\mathfrak{R}$ is an expression of the form

$$
\mathfrak{R}::=p|\mathfrak{R} \| \mathfrak{R} \mid[\mathfrak{R}]_{C}
$$

where, for a factor $\mathrm{f} \in F$ (Definition 3), phase $p \in P h_{\mathrm{f}}$ (e.g. $0^{f}, f, \bar{f}$ ) is a risk structure and $C \subseteq \mathcal{C}$ is a set of constraints (Definition 12). Let $\mathcal{S}$ be the set of all risk structures, including all phases $\bigcup_{\mathrm{f} \in \mathcal{F}} P h_{\mathrm{f}} \subset \mathcal{S}$.

The binary operator $\|$ signifies the parallel composition of two structures, and the binary operator $[\cdot]_{C}$ applies all constraints in the set $C$ to a risk structure.

Operational semantics Let the map $\llbracket \cdot \rrbracket: \mathcal{S} \rightarrow \mathcal{T}$ uniquely assign a LTS to a CSP process corresponding to a risk structure. With $\mathfrak{R} \in \mathcal{S}$ we associate a LTS $\llbracket \mathfrak{R} \rrbracket_{r}=\left(R, \Sigma^{u}, \rightarrow, R_{0}\right)$ with the risk space $R$ (Definition 5), the abstracted used alphabet $\Sigma^{u} \subset 2^{\Sigma^{v}} \backslash\{\varnothing\}$ (Definition 1, Sects. 7.1, 7.2, 7.3), the transition relation $\rightarrow \subseteq$ $R \times \Sigma^{u} \times R$ (Definitions 15 and 16, Sect. 7.3), and a set of initial states $R_{0} \subseteq R$. The operational semantics and algebraic properties of the operators and constructs of the language in Definition 14 are provided below. The construction of the used alphabet $\Sigma^{u}$ will be explained along with the operators.

# 7.1. Risk factors as sequential processes 

A risk factor $\mathrm{f} \in F$ (Figs. 2 and 3) can be represented as a sequential, mutually recursive process $\mathfrak{R}_{\mathrm{f}}$ according to Definition 1. We express f as

$$
\begin{aligned}
& \mathfrak{R}_{\mathrm{f}}=0^{f} \\
& 0^{f}=? x: e^{\mathrm{f}} \rightarrow f \square ? x: o_{n}^{\mathrm{f}} \rightarrow 0^{f} \\
& f=? x: m_{d}^{\mathrm{f}} \rightarrow 0^{f} \square ? x: o_{e}^{\mathrm{f}} \rightarrow f \square ? x: m^{\mathrm{f}} \rightarrow \bar{f} \\
& \bar{f}=? x: \bar{e}^{\mathrm{f}} \rightarrow f \square ? x: m_{r}^{\mathrm{f}} \rightarrow 0^{f} \square ? x: o_{m}^{\mathrm{f}} \rightarrow \bar{f}
\end{aligned}
$$

(init)
(inactive)
(active)
(mitigated)

Note the use of f as a symbol for the risk factor as a transition system (Fig. 2a) and the use of $f$ for the CSP process that models this factor in its active phase. Different fonts signify the semantic difference. Also notice that $p \xrightarrow{\mathrm{f}}$ for any $p \in P h_{\mathrm{f}}$ of a non-deterministic factor (Fig. 4) corresponds to the $\sqcap$-fraction in $\square$.
This mapping enables an algebraic treatment of factors in CSP.
The semantics of a single factor f in phase $p \in P h_{\mathrm{f}}$ is given by $\llbracket p \rrbracket_{r}=\left(R(\{\mathrm{f}\}), \Sigma^{\mathrm{f}}, \rightarrow_{f},\{\llbracket \mathrm{f} \mapsto p \rrbracket\right)$ ) and the elements of this tuple are given by Definition 3 and described in Fig. 2. For example, $\llbracket 0^{f} \rrbracket_{r}=\left(R(\{\mathrm{f}\}), \Sigma^{\mathrm{f}}, \rightarrow_{f}\right.$ , $\left\{\llbracket \mathrm{f} \mapsto 0^{f} \rrbracket\right\}$ ) provides the semantics of f initialised with the phase $0^{f}$. For each factor, we assume a phase order $\preceq_{\mathrm{f}}$ as given in Sect. 4.1.

Factor alphabets for global input-enabledness Based on the definitions in Sect. 4.1, the condition

$$
\forall \mathrm{f}, \mathrm{~g} \in F:\left(\bigcup_{e \in \Sigma^{\mathrm{f}}} e\right) \backslash\{\tau\}=\left(\bigcup_{e^{\prime} \in \Sigma^{\mathrm{g}}} e^{\prime}\right) \backslash\{\tau\}=\Sigma
$$

requires all factors to support the alphabet $\Sigma$ of the process $P$. This choice does not affect risk space composition (Sect. 4.2) but allows factors to be composed in parallel synchronously and be ready to agree with some event $P$ offers. This attempt to avoid interleaving requires input-enabledness of $\mathfrak{R}$ (Sect. 4.1). Given $F$ in terms of a factor family $\left(\mathrm{f}_{i}\right)_{i \in[1 . . n]}$ with $n \in \mathbb{N}$, one way to satisfy Formula (14) is a structured alphabet with compound (i.e., multi-part) events

$$
r \cdot \alpha_{1} \cdot \alpha_{2} \ldots \alpha_{n}
$$

with $\alpha_{1} \cdot \alpha_{2} \ldots \alpha_{n} \in \Sigma^{\mathrm{f}_{1}} \cdot \Sigma^{\mathrm{f}_{2}} \ldots \Sigma^{\mathrm{f}_{n}}$ and a central channel $r$ of type $\Sigma^{\mathrm{f}_{1}} \cdot \Sigma^{\mathrm{f}_{2}} \ldots \Sigma^{\mathrm{f}_{n}}$ through which $\mathfrak{R}$ can observe and influence $P$. For $i, j \in[1 . . n]$ with $i \neq j$, two (partially defined) factor event sets, say an endangerment $e^{\mathrm{f}_{i}} \in \Sigma^{\mathrm{f}_{i}}$ activating factor $\mathrm{f}_{i}$ and a mitigation $m^{\mathrm{f}_{i}} \in \Sigma^{\mathrm{f}_{j}}$ of factor $\mathrm{f}_{j}$, then correspond to the set of (fully defined) compound events given by

$$
\operatorname{events}_{\mathfrak{R}}\left(r ? e^{\mathrm{f}_{i}}!m^{\mathrm{f}_{i}}\right)=\left\{r \cdot \alpha_{1} \ldots ? e^{\mathrm{f}_{i}} \ldots!m^{\mathrm{f}_{i}} \ldots \alpha_{n} \mid \alpha_{1} \in \Sigma^{\mathrm{f}_{1}}, \ldots, e^{\mathrm{f}_{i}} \in \Sigma^{\mathrm{f}_{i}}, \ldots, m^{\mathrm{f}_{i}} \in \Sigma^{\mathrm{f}_{i}}, \ldots, \alpha_{n} \in \Sigma^{\mathrm{f}_{n}}\right\}
$$

At the level of $P$, these compound events are equivalently given by

$$
\operatorname{events}_{P}\left(r ? e^{\mathrm{f}_{i}}!m^{\mathrm{f}_{i}}\right)=\left\{r \cdot x_{1} \ldots x_{i} \ldots x_{j} \ldots x_{n} \mid x_{1} \in \bigcup_{e \in \Sigma^{\mathrm{f}_{1}}} e, \ldots, x_{i} \in e^{\mathrm{f}_{i}}, \ldots, x_{j} \in m^{\mathrm{f}_{i}}, \ldots, x_{n} \in \bigcup_{e \in \Sigma^{\mathrm{f}_{n}}} e\right\}
$$

This channel type is inspired by suggestions in [Ros10, Sec. 1.2.4] and by [BS01, Sec. 3.4]. Thus, each factor f synchronises with the projection from $\Sigma$ into $\Sigma^{\mathrm{f}}$ and is always ready to agree with some event offered by

$P .{ }^{21}$ This construction models partial observability of $P$ through factors implemented by sensors and actuators and, for a deterministic factor set $F$, guarantees deadlock freedom of $P \| \mathfrak{R}$, modelling that a corresponding implementation of $F$ can always monitor and influence $P$.

# 7.2. Composition 

Let $A, B, F \subseteq \mathcal{F}$ be factor sets with $A, B \subseteq F$ and, for $i \in\{1,2,3\}, \mathfrak{R}_{i} \in \mathcal{S}$ be structures according to Definition 14 with $\llbracket \mathfrak{R}_{i} \rrbracket_{r}=\left(R_{i}, \Sigma_{i}^{u}, \rightarrow_{i}, R_{i, 0}\right)$. Now, we may want to combine two structures, say $\mathfrak{R}_{1}$ and $\mathfrak{R}_{2}$, with possibly intersecting factor sets, for example, if two safety engineers are trusted with two HazOps of the same machine. Let the map scope: $\mathcal{S} \rightarrow 2^{\mathcal{F}}$ identify the factors referred to by a structure. Then, scope $\left(\mathfrak{R}_{1}\right) \cap \operatorname{scope}\left(\mathfrak{R}_{2}\right)$ indicates all shared factors.

Because a single factor cannot be in two different phases at the same time, we apply Definition 6 for $F_{1}=$ $\operatorname{scope}\left(\mathfrak{R}_{1}\right)$ and $F_{2}=\operatorname{scope}\left(\mathfrak{R}_{2}\right)$ to uniquely define the transition relation resulting from parallel composition: only those states can be combined whose factors in the shared scope are in their identical phases.
Definition 15 (Parallel composition) We define $\llbracket \mathfrak{R}_{1} \| \mathfrak{R}_{2} \rrbracket_{r}=\left(R, \Sigma^{u}, \rightarrow, R_{0}\right)$ with $R=R_{1} \otimes R_{2}$ (see Definition 7 and Lemma 1) and $R_{0}=R_{1,0} \otimes R_{2,0}$. For states $\sigma_{1}, \sigma_{1}^{\prime} \in R_{1}, \sigma_{2}, \sigma_{2}^{\prime} \in R_{2}$, the composed transition relation $\rightarrow$ is given by the left, right, and synchronous step rules

$$
\begin{aligned}
& \frac{\sigma_{1} \xrightarrow{e_{+}} \sigma_{1}^{\prime} \quad \sigma_{2} \xrightarrow{f} \sigma_{2}^{\prime} \sigma_{2}^{\prime}}{\sigma_{1} \cup \sigma_{2} \xrightarrow{e \backslash f} \sigma_{1}^{\prime} \cup \sigma_{2}}[\sigma_{1} \approx \sigma_{2}, \sigma_{1}^{\prime} \approx \sigma_{2}, e \neq f], \\
& \frac{\sigma_{1} \xrightarrow{e_{+}} \sigma_{1}^{\prime} \quad \sigma_{2} \xrightarrow{f} \sigma_{2}^{\prime} \sigma_{2}^{\prime}}{\sigma_{1} \cup \sigma_{2} \xrightarrow{f \backslash e} \sigma_{1} \cup \sigma_{2}^{\prime}}[\sigma_{1} \approx \sigma_{2}, \sigma_{1} \approx \sigma_{2}^{\prime}, e \neq f], \text { and } \\
& \frac{\sigma_{1} \xrightarrow{e_{+}} \sigma_{1}^{\prime} \quad \sigma_{2} \xrightarrow{f} \sigma_{2}^{\prime} \sigma_{2}^{\prime}}{\sigma_{1} \cup \sigma_{2} \xrightarrow{e \cap f} \sigma_{1}^{\prime} \cup \sigma_{2}^{\prime}}[\sigma_{1} \approx \sigma_{2}, \sigma_{1}^{\prime} \approx \sigma_{2}^{\prime}, e \cap f \neq \varnothing] .
\end{aligned}
$$

Based on $\rightarrow$, the used alphabet is $\Sigma^{u}=\left\{e \in 2^{\Sigma^{\prime}} \mid \exists \sigma, \sigma^{\prime} \in R: \sigma \xrightarrow{e} \sigma^{\prime}\right\}$.
Note that $\|$-I-step covers the special case $f=\varnothing$ corresponding to $\sigma_{2} \rightarrow_{2} \cdot \|$-r-step works analogously. These step rules together resemble the step law of generalised parallel composition in CSP [Ros10, Sec. 3.4].

Algebraic properties of composition In the following, we show some desirable properties of the composition of two or more risk structures.

Lemma 8 (Idempotency of $\|$ under determinism) For any deterministic $\mathfrak{R}_{1} \in \mathcal{S}$, we have

$$
\mathfrak{R}_{1} \| \mathfrak{R}_{1}=\mathfrak{R}_{1}
$$

Proof of Lemma 8. From Definition 5, by Lemma 1, we obtain $R_{1} \otimes R_{1}=R_{1}$. Based on Sect. 4.2 and the alphabet of $\mathfrak{R}_{1}$ defined in Sect. 7.1, we can apply the rules from Definition 15 as follows.

Because of the uniqueness of $\mathfrak{R}_{1}$ and the compatibility requirement (Formula (2)), the composition takes two consistent views of $\mathfrak{R}_{1}$ offering identical source and target states $\left(\sigma_{1}=\sigma_{2}\right)$ at each step. By definition, all factors share the alphabet $\Sigma$ and $\mathfrak{R}_{1}$ is deterministic. Then, any two event sets $e, f$ in initials $\left(\mathfrak{R}_{1}\right)$ (i.e., in a state $\sigma$ ) are either disjoint or equal. Hence, there is no way for a concrete event in $P$ to be a member of more than one such event set. In line with Definition 3, $\|$-I-step and $\|$-r-step do not apply. $\|$-s-step turns into a tautology and both views exhibit an identical transition:

$$
\frac{\sigma_{1} \xrightarrow{e_{+}} \sigma_{1}^{\prime}}{\sigma_{1} \cup \sigma_{1} \xrightarrow{e} \sigma_{1}^{\prime} \cup \sigma_{1}^{\prime}}
$$

[^0]
[^0]:    ${ }^{21}$ According to the CSP notation for channel events, we have $\Sigma=\|r\|=\operatorname{events}(r)$ for the channel $r$.

For $\sigma_{1}, \sigma_{1}^{\prime} \in R_{1}$ and $e \in \Sigma_{1}^{u}$, this tautology preserves $\Sigma_{1}^{u}, \rightarrow_{1}$, and $R_{1,0}$.
The composition of a deterministic $\mathfrak{R}_{1}$ with itself turns into a synchronous (i.e., non-interleaved) composition, essentially, a sequence of external choices where both $\mathfrak{R}_{1} \mathrm{~s}$ synchronously agree with the environment.
Lemma 9 (Commutativity of $\|$ ) For any $\mathfrak{R}_{1}, \mathfrak{R}_{2} \in \mathcal{S}$, we have

$$
\mathfrak{R}_{1}\left\|\mathfrak{R}_{2}=\mathfrak{R}_{2}\right\| \mathfrak{R}_{1}
$$

Proof of Lemma 9. Lemma 1 in Sect. 4.2 makes it easy to show $R_{1} \otimes R_{2}=R\left(\operatorname{scope}\left(\mathfrak{R}_{1}\right) \cup \operatorname{scope}\left(\mathfrak{R}_{2}\right)\right)=R_{2} \otimes R_{1}$. Furthermore, the symmetric duals (i.e., $\|$-r-step is the dual of $\|$-l-step) of the rules in Definition 15 yield the same $\rightarrow$ and, hence, the same $\Sigma^{u}$.
Lemma 10 (Associativity of $\|$ ) For any $\mathfrak{R}_{1}, \mathfrak{R}_{2}, \mathfrak{R}_{3} \in \mathcal{S}$ with disjoint scopes, that is,

$$
\operatorname{scope}\left(\mathfrak{R}_{1}\right) \cap \operatorname{scope}\left(\mathfrak{R}_{2}\right) \cap \operatorname{scope}\left(\mathfrak{R}_{3}\right)=\varnothing
$$

we have

$$
\left(\mathfrak{R}_{1}\left\|\mathfrak{R}_{2}\right)\right\| \mathfrak{R}_{3}=\mathfrak{R}_{1}\left\|\left(\mathfrak{R}_{2} \| \mathfrak{R}_{3}\right)\right.
$$

Proof sketch for Lemma 10. Because of empty shared scopes, the side conditions always hold on both sides and states are merged by disjoint union. Set operations on states and events are commutative and associative. By definition, ${ }^{22}$ all factors (Definition 3) share the alphabet $\Sigma$, that is, they synchronise on all events (Sect. 4.2). Thus, interleaving is avoided, the alphabetised parallel operator takes $\Sigma$ on both sides and, this way, reduces to synchronous parallel composition for which a general associative law is available [Ros10, p. 60].
Lemma 10 allows the use of $\left\|^{f \in F} 0^{f}\right.$ as a shortcut for $\left(\left(\ldots\left(0^{f_{i}}\left\|0^{f_{i}}\right)\right\| \ldots\right)\left\|0^{f_{i}}\right)\right.$ with $f_{i} \in F$.
Lemma 11 (Associativity of $\|$ ) For any $\mathfrak{R}_{1}, \mathfrak{R}_{2}, \mathfrak{R}_{3} \in \mathcal{S}$ with equal scopes, that is,

$$
\operatorname{scope}\left(\mathfrak{R}_{1}\right)=\operatorname{scope}\left(\mathfrak{R}_{2}\right)=\operatorname{scope}\left(\mathfrak{R}_{3}\right)
$$

we have

$$
\left(\mathfrak{R}_{1}\left\|\mathfrak{R}_{2}\right)\right\| \mathfrak{R}_{3}=\mathfrak{R}_{1}\left\|\left(\mathfrak{R}_{2} \| \mathfrak{R}_{3}\right)\right.
$$

Proof sketch of Lemma 11. The proof is analogous to the proof of Lemma 10.

# 7.3. Constraints 

In Sect. 6, we specified relations over risk spaces to determine $\rightarrow$ by pruning $R \times R$. We now use constraints as a construct in the language of RISKSTRUCTURES (Definition 14). The redundancy coming with this construct can be used to identify inconsistencies between $\mathfrak{R}$ and the real world, potentially helpful in model refinement, completion, and validation [Gle14]. Particularly, these inconsistencies allow choices for their resolution. We can make such inconsistencies explicit as follows.

For factors $F \subseteq \mathcal{F}$, constraints $C \subseteq \mathcal{C}$, and a risk state $\sigma \in R(F)$, we call

$$
\mathfrak{R}_{\sigma}^{C}=\left[\left\|^{f \in F} \sigma(f)\right]_{C}\right.
$$

with $R_{0}=\{\sigma\}$ the characteristic risk structure of $\sigma$ under constraints $C$. But which definition of $\sigma \rightarrow$ is most useful? To investigate this, we split the determination of $\sigma \rightarrow$ for $\mathfrak{R}_{\sigma}^{C}$ into three fractions $\sigma \rightarrow_{\mathrm{c}, \mathrm{f}, \mathrm{p}}$ with

$$
\begin{array}{ll}
\sigma \rightarrow_{\mathrm{c}} \text { derived from } C \text {, with } & \sigma \xrightarrow{\mathrm{r}_{\mathrm{c}}} \sigma^{\prime} \in \sigma \rightarrow_{\mathrm{c}} \Longleftrightarrow\left(\sigma, \sigma^{\prime}\right) \in \llbracket C \rrbracket_{\mathrm{c}}^{R} \\
\sigma \rightarrow_{\mathrm{f}} \text { from Definitions 3 and 15, with } & \sigma \xrightarrow{\mathrm{c}} \sigma^{\prime} \in \sigma \rightarrow_{\mathrm{f}} \Longleftrightarrow \sigma \xrightarrow{\mathrm{c}} \sigma^{\prime} \text {, and } \\
\sigma \rightarrow_{\mathrm{p}} \text { from process } P \text {, with } & \sigma \xrightarrow{\mathrm{c}} \sigma^{\prime} \in \sigma \rightarrow_{\mathrm{p}} \Longleftrightarrow e \in \operatorname{initials}(P) \wedge \sigma^{\prime} \in \operatorname{reach}(\sigma, P)
\end{array}
$$

These fractions give rise to the following inconsistencies:

1. The relation $\sigma \rightarrow_{\mathrm{c}} \backslash \sigma \rightarrow_{\mathrm{f}}$ describes sensible transitions with invisible events signified by $\tau_{\mathrm{c}}$. We choose to prune transitions from $\rightarrow$ if they deviate from what is provided in $\rightarrow_{\mathrm{f}}$.
[^0]
[^0]:    ${ }^{22}$ We provide the rationale for this definition in Sect. 7.5.

![img-9.jpeg](img-9.jpeg)

Fig. 9. Semantics of $\sigma \rightarrow$ for the constrained form $[\mathfrak{R}]_{C}$ according to Definition 16
2. The relation $\sigma \rightarrow_{\mathrm{f}} \backslash \sigma \rightarrow_{\mathrm{c}}$ describes irrelevant transitions labelled with a $\tau_{\mathrm{f}}$. We choose to prune transitions from $\rightarrow$ if they violate constraints and, hence, lead to inconsistencies in $\mathfrak{R}$.
3. The relation $\sigma \rightarrow_{\mathrm{p}}\left\langle\left(\sigma \rightarrow_{\mathrm{c}} \cup \sigma \rightarrow_{\mathrm{f}}\right)\right.$ describes imperceptible transitions. In $\rightarrow$, we could label such transitions with a $\tau_{\mathrm{p}}$, making them subject of process-driven disclosure of $\mathfrak{R}$.
4. The relation $\left(\sigma \rightarrow_{\mathrm{c}} \cap \sigma \rightarrow_{\mathrm{f}}\right) \backslash \sigma \rightarrow_{\mathrm{p}}$ describes unrealised transitions. We could prune such transitions from $\rightarrow$, because they are not realised in $P$ and, hence, would only add little value to $\mathfrak{R}$.

This case analysis is visualised in Fig. 9 and suggests several possibilities to design a semantics for constraints. As indicated in the case list, one would desire the following possibility for $\rightarrow$ :

$$
\begin{aligned}
\sigma \rightarrow & =\left(\sigma \rightarrow_{\mathrm{c}} \cup \sigma \rightarrow_{\mathrm{f}} \cup \sigma \rightarrow_{\mathrm{p}}\right) \backslash\left(\underbrace{\left(\sigma \rightarrow_{\mathrm{c}} \backslash \sigma \rightarrow_{\mathrm{f}}\right)}_{1 . \text { reduce to } F} \cup \underbrace{\left(\sigma \rightarrow_{\mathrm{f}} \backslash \sigma \rightarrow_{\mathrm{c}}\right)}_{2 . \text { reduce to } C} \cup \underbrace{\left(\sigma \rightarrow_{\mathrm{c}} \cup \sigma \rightarrow_{\mathrm{f}} \backslash \sigma \rightarrow_{\mathrm{p}}\right)}_{4 . \text { reduce to } P}\right) \\
& =\sigma \rightarrow_{\mathrm{c}} \cap \sigma \rightarrow_{\mathrm{f}} \cap \sigma \rightarrow_{\mathrm{p}} .
\end{aligned}
$$

Corollary 6 For any characteristic structure $\mathfrak{R}_{\sigma}^{C}$, we have $\sigma \rightarrow_{\mathrm{c}} \backslash \sigma \rightarrow_{\mathrm{f}}=\varnothing$ because of the input-enabledness [Tre08] of factors and, thus, $\sigma \rightarrow=\sigma \rightarrow_{\mathrm{c}} \cap \sigma \rightarrow_{\mathrm{p}}$.

To weaken the dependency of $\mathfrak{R}$ on a possibly partially known process, we apply the following definition.
Definition 16 (Constraint) Let $\mathfrak{R}$ be a risk structure (Definition 14) with $\llbracket \mathfrak{R} \rrbracket_{r}=\left(R, \Sigma^{u}, \rightarrow, R_{0}\right)$ and $C$ a set of constraints well-formed for $R$ (Sect. 6, Definition 13). The constrained form $[\mathfrak{R}]_{C}$ is defined by $\llbracket[\mathfrak{R}]_{C} \rrbracket_{r}=$ $\left(R, \Sigma_{C}^{u}, \rightarrow_{C}, R_{0}\right) . \rightarrow_{C}$ is determined by the following two rules. For $\sigma, \sigma^{\prime} \in R$

$$
\begin{aligned}
& \frac{\sigma \xrightarrow{e} \sigma^{\prime}}{\sigma \xrightarrow{e}_{C} \sigma^{\prime}} \quad \text { and } \\
& \frac{\sigma \xrightarrow{e} \sigma^{\prime}}{\sigma \xrightarrow{\tau_{\mathrm{f}}} \sigma^{\prime}} \quad\left(\left[\cdot\right]_{C} \text {-step }\right) \\
& \text { Based on } \rightarrow_{C}, \Sigma_{C}^{u}=\left\{e \in 2^{\Sigma^{\prime}} \mid \exists \sigma, \sigma^{\prime} \in R: \sigma \xrightarrow{e}_{C} \sigma^{\prime}\right\} .
\end{aligned}
$$

For arbitrary structures, the $[\cdot]_{C}$-step rule implements $\rightarrow=\rightarrow_{\mathrm{c}} \cap \rightarrow_{\mathrm{f}}$ (i.e., cases 1 and 2 ). The reduction of unrealised transitions and the coverage of imperceptible transitions (i.e., cases 3 and 4 ) could be addressed by an incremental construction of $\mathfrak{R}$. $[\cdot]_{C}$-cancel produces $\tau_{\mathrm{f}}$ self-loops to preserve input-enabledness. ${ }^{23}$ Notice that $\tau_{\mathrm{f}}$-loops remain whether or not they are contained in further constraints applied to $\mathfrak{R}$, and also that Corollary 6 and Definition 16 prevent constraints such as causes from producing $\tau_{\mathrm{c}}$. Overall, the rules $\|$-l-step, $\|$-r-step, \|-s-step, $[\cdot]_{C}$-step, and $[\cdot]_{C}$-cancel determine the operational semantics of a risk structure as an LTS and, together with reach (Sect. 5.4), form a basis for automated reasoning about RISKSTRUCTURES. We demonstrate such automation with our tool prototype YAP [Gle21].
Remark 2 The meaning of f causes g, specified as a relation in Sect. 6.1, can now be investigated in the LTS semantics of $\mathfrak{R}$. On a particular path through $R$ according to $\rightarrow_{C}$ from a state in $R_{0}$, whenever f gets active, g must

[^0]
[^0]:    ${ }^{23}$ Operationally, $[\cdot]_{C}$-cancel acts like a $S K I P$, non-blocking $S T O P$, or a hiding of trace suffixes. Hence, we define $\tau_{\mathrm{f}}=\checkmark$.

get active in the same or the following state. This way, causes constraints allow immediate or weak causation and requires constraints delayed or strong causation at most one logical step apart in $\mathfrak{R}$. The weak form of causes enforces the simultaneous occurrence of $f$ and $g$, it synchronises the activation of $g$ with the prior activation of $f$. Moreover, g can stay active forever and may already be active before the activation of $f$. Consider that g might have been activated by a factor or a causal relationship not (yet) captured in $\mathfrak{R}$. Such activation is by default possible in $\mathfrak{R}$ once g is in the factor set.
Algebraic properties of constraints $\left([\cdot]_{C}\right)$. Let $C_{i} \subseteq \mathcal{C}$ for $i \in\{1,2,3\}$. We have that $[\mathfrak{R}]_{\mathcal{C}}=\mathfrak{R}$ by Definition 12. The following lemma establishes that the order in which single constraints are applied to $\mathfrak{R}$ does not matter.

# Lemma 12 (Exchange of $[\cdot]_{C}$ and $\cup$ ) 

$$
\left[[\mathfrak{R}]_{C_{1}}\right]_{C_{2}}=[\mathfrak{R}]_{C_{1} \cup C_{2}}
$$

Proof sketch. The proof is by induction over $C_{1}$, supported by an additional lemma for the induction step, and takes advantage of associativity of set intersection as used in Definition 12. The detailed proof is stated in Appendix A.

## Lemma 13 (Idempotency)

$$
\left[[\mathfrak{R}]_{C}\right]_{C}=[\mathfrak{R}]_{C}
$$

Proof sketch. This lemma follows from Lemma 12 and idempotency of set union.

## Lemma 14 (Commutativity)

$$
\left[[\mathfrak{R}]_{C_{1}}\right]_{C_{2}}=\left[[\mathfrak{R}]_{C_{2}}\right]_{C_{1}}
$$

Proof sketch. This lemma follows from Lemma 12 and commutativity of set union.

## Lemma 15 (Associativity)

$$
\left[[\mathfrak{R}]_{C_{1} \cup C_{2}}\right]_{C_{3}}=\left[[\mathfrak{R}]_{C_{1}}\right]_{C_{2} \cup C_{3}}
$$

Proof sketch. This lemma follows from Lemma 12 and associativity of set union.
For an arbitrary $C \subseteq \mathcal{C}$, we relax Definition 16 by establishing following equivalence

$$
[\mathfrak{R}]_{C}=[\mathfrak{R}]_{C}
$$

for the largest $C^{\prime} \subseteq C$ well-formed for $R$ (Definition 13). Then, $[\mathfrak{R}]_{C}$ denotes the structure resulting from applying only and exactly the constraints in $C^{\prime}$. Moreover, Definition 16 complements Definition 15 by guarding the $\|$-i-step, $\|$-r-step, and $\|$-s-step rules. In this way, the application of a constraint $c \in \mathcal{C}$ to a risk structure $\mathfrak{R}$ restricts its transition relation $\rightarrow$. Definition 16 , together with the relational pruning for three out of the four mentioned cases (cf. Fig. 9), yields the following refinement law.

## Lemma 16 (Constraints trace-refine)

$$
\mathfrak{R} \subseteq_{T}[\mathfrak{R}]_{C}
$$

Proof sketch. The proof is by showing that traces $(\mathfrak{R}) \supseteq$ traces $\left([\mathfrak{R}]_{C}\right)$. Fix $t \in$ traces $\left([\mathfrak{R}]_{C}\right)$ with $t=f^{\prime} l$ for induction over the split of $t$ into $f$ and $l$. Induction step: Assume that $f \in$ traces $(\mathfrak{R})$ as induction hypothesis (IH). With $l=\langle e\rangle^{\prime} l^{\prime}$ and $t=f^{\prime}\langle e\rangle^{\prime} l^{\prime}$, there exist $\sigma, \sigma^{\prime} \in R$ such that $\sigma \xrightarrow{e} C \sigma^{\prime}$ and, according to rule $[\cdot]_{C}$-step, such that $e \in \Sigma^{n}, \sigma \xrightarrow{e} \sigma^{\prime}$, and $\left(\sigma, \sigma^{\prime}\right) \in \llbracket C \rrbracket_{c}^{R}$. Because of IH and $\sigma \xrightarrow{e} \sigma^{\prime}$, there must be a trace $f^{\prime}\langle e\rangle^{\prime} l^{\prime \prime} \in$ traces $(\mathfrak{R})$ and, because of downward closure, a trace $f^{\prime}\langle e\rangle . e$ is part of $l$ and, therefore, $t$ such that we complete the induction step and establish the new IH $f^{\prime}\langle e\rangle$. (We do not need to prove the equivalence $l^{\prime}=l^{\prime \prime}$.) The case $f=\langle \rangle$ provides the induction start and $l=\langle e\rangle$ terminates the induction.

Following the pruning semantics described in Fig. 9, Lemma 16 establishes the desirable effect of constraints, the pruning of the transition relation of $\mathfrak{R}$ according to the relational specification of the added constraints. However, an investigation of the conditions under which constraints are compositional, that is, when they can be exchanged with, for example, $\|$, is left for future work.

Listing 2: YAP script modelling the situation manual from Table 2

```
factormodel for manual {
    // single compound consequence on a single asset: impact on
        human driver
    col desc "collision"
        accident
        detectedBy(.crashSens)
        mitigatedBy(.rA)
        requires(ncol)
        sev=[10,20);
    strA desc "airbag spurious trip"
        causes(locd)
        sev=[5,12];
    locd desc "loss of driving control"
        preventsMit(ncol,locd) // mitigation lock at loc
        requires(strA)
        sev=[2,17];
    ncol desc "near collision"
        detectedBy(.ODM)
        mitigatedBy(PREVEXT_CRASH.swBr)
        direct
        sev=[5,18];
```

![img-10.jpeg](img-10.jpeg)

Fig. 10. Risk structure $\mathfrak{R}_{\text {manual }}$ with the factor set $F=\left\{\operatorname{loc}_{\mathrm{d}}, \mathrm{ncol}, \mathrm{st}_{\mathrm{rA}}, \mathrm{col}\right\}$ generated by YAP from Listing 2

Finally, we discuss the special case that constraints are applied to a phase $p \in P h_{\mathrm{f}}$ of a factor $f$. Observe that $\operatorname{scope}(p)=\{\mathrm{f}\}$ and, by Definition 13, $C$ is well-formed for $R(\operatorname{scope}(p))$ if $C$ contains only constraints that refer to f. Moreover, if $C$ does not contain self-referential constraints (Sect. 6.1), Formula (16) entails $C^{\prime}=\varnothing$ for the largest well-formed $C^{\prime} \subseteq C$. From this observation, we obtain
by Formula (16) by Definition 13 by Definition 12
The effect of this last result is that single factors are not affected by constraints other than self-referential ones. Selfreferential constraints such as f direct can, however, restrict $p$ or convert $p$ to $S K I P$. Often, such constraints can be avoided because they do not offer much expressiveness over bespoke factor models.

# 7.4. Example: risk factors on the road (cont'd) 

We develop the example in Sect. 3 and sects. 4.3 and 6.3, modelling instances of the factor set $F=\left\{\mathrm{loc}_{\mathrm{d}}, \mathrm{ncol}, \mathrm{st}_{\mathrm{rA}}, \mathrm{col}\right\}$ with corresponding events and compose these factors into the structure

$$
\mathfrak{R}_{\text {manual }}=\left[\left(\left(0^{s t_{r A}} \| 0^{l o c_{d}}\right) \| 0^{n c o l}\right) \| 0^{c o l}\right]_{C}
$$

for the situation manual. $C$ contains dependencies such as $\mathrm{loc}_{\mathrm{d}}$ preventsMit $\left\{\mathrm{ncol}, \mathrm{loc}_{\mathrm{d}}\right\}$ and $\mathrm{st}_{\mathrm{rA}}$ causes $\mathrm{loc}_{\mathrm{d}}$. The full dependency list can be derived from Listing 2. Figure 10 shows the transition graph for $\mathfrak{R}_{\text {manual }}$ after applying composition and constraints. The edges are labelled with factor events and the nodes with active factors. Listing 2 is written in YAP script, the input language for our tool YAP [Gle21], which allows one to encode a situation/action/factor table (Table 1a) and elaborate the example in Sect. 3 in several steps.

Collision (col) is the first phenomenon we model as a factor. With the detectedBy directive, we specify that a collision is detected by a crash sensor (crashSens) that signals the release of an airbag $(r A)$. We associate an interval col. $s=[10,20)$ of 10 to 20 "negativity units" to a collision.

To illustrate scoping of a risk structure, we use the keyword accident to declare col as final. Mitigation of final factors is out of scope, so vehicle control would not take into account crashSens and $r A$ in this case. However, in practice, col is not final because of being mitigated by an airbag. Capturing a step of accident analysis-technically, backwards causal reasoning-the dependency col requires ncol specifies that a near-collision is assumed to occur before any collision.

A near-collision (ncol) is detected by an object distance measurement system (ODM). The ODM is responsible for monitoring the predicate $\operatorname{dist} T o N O o T<S B D$, which is true if the distance measured to the nearest object on the road within the planned vehicle trajectory (distToNOoT) is smaller than the safe braking distance $S B D$. We assume an interval ncol. $s=[5,18)$ with a smaller upper bound than the one for col because the indirection to the accident reduces the possibility of bad consequences. Concretely, the likelihood of consequences from col is reduced by the action $s w B r$. Based on the discussion in Sect. 4.4, we plan in future work to quantify this likelihood through probabilistic factor transitions.

The mitigatedBy(PREVENT_CRASH.swBr) directive specifies as a mitigation of ncol the swerve-and-break manoeuvre ( $s w B r$ ). The constraint direct specifies that $s w B r$ to be the event $m_{d}^{\text {ncol }}$ (cf. Fig. 2a). Shown in the controlloop block, $s w B r$ is a low-level control mode to be elaborated in an external model (e.g. in MATLAB or its free alternative GNU/Octave ${ }^{24}$ ). PREVENT_CRASH is a classifier from which generic parameters for lowlevel controllers of this kind could be inherited. The modelling of modes is akin to the specification of guarded commands (i.e., using the guard and update attributes). We demonstrate in [GC20] how YAP modes can be used for controller synthesis, and in [FGC20] how factor LTSs can be modelled as hybrid automata, simulated in GNU/Octave, and formally verified in Isabelle/UTP.

By FMEA of the airbag, we identify its spurious trip ( $\mathrm{st}_{\mathrm{rA}}$ ) and assume it to be one of possibly several sufficient causes of a loss of driving control $\left(\operatorname{loc}_{\mathrm{d}}\right)$. This finding is captured by the two dependencies $\mathrm{st}_{\mathrm{rA}}$ causes $\operatorname{loc}_{\mathrm{d}}$ and $\operatorname{loc}_{\mathrm{d}}$ requires $\mathrm{st}_{\mathrm{rA}}$. $\mathrm{st}_{\mathrm{rA}}$ gets assigned the interval $\mathrm{st}_{\mathrm{rA}} . s=[5,12) .{ }^{25}$ We specify the interval $\operatorname{loc}_{\mathrm{d}} . s=[2,17)$. Moreover, $\operatorname{loc}_{\mathrm{d}}$ preventsMit $\left\{\mathrm{ncol}, \mathrm{loc}_{\mathrm{d}}\right\}$ captures the fact that after a loss of control, manual driving mode prevents the mitigation of ncol. Additionally, $\operatorname{loc}_{\mathrm{d}}$ locks itself using a circularity so that, in $\mathfrak{R}_{\text {manual }}$, it cannot be mitigated.

From the severity intervals calculated for each risk state according to Formula (5) (see the state labels in Fig. 10), we establish

$$
\underline{\operatorname{col}}<_{\mathrm{m}} n \mathrm{col}={ }_{\mathrm{m}} \operatorname{loc}_{\mathrm{d}} s t_{r A} n \mathrm{col}<_{\mathrm{m}} \operatorname{loc}_{\mathrm{d}} s t_{r A}<_{\mathrm{m}} 0
$$

Notice that, according to $\leq_{m}$, the state ncol is equivalent to $\operatorname{loc}_{\mathrm{d}} s t_{r A} n c o l$. This equivalence results from the equality of the upper bounds of both intervals $[5,18)$ and $[2,18)$. Although one might think that the state with the smaller lower bound (i.e., $\operatorname{loc}_{\mathrm{d}} s t_{r A} n c o l$ ) is better, consider that ncol has two active factors less. This circumstance gives rise to investigate refinements of $\leq_{m}$. In fact, our tool YAP [Gle21] implements a special case of $\leq_{m}$ distinguishing pairs ( $\sigma, \sigma^{\prime}$ ) of risk states that normally are $\sigma=_{m} \sigma^{\prime}$ because they only differ in the lower bounds of their severity intervals.

The state $\mathbf{F}$ with all factors activated (cf. Definition 11) is not reachable from 0 . Moreover, only one of the five relevant states in $\mathfrak{R}_{\text {manual }}$ is covered by a mitigation $s w B r$ for ncol. In practice, one desires mitigations that cover many states or mitigate several factors at once. Although it is useful to statically assign severity intervals for analysis purposes, it is obvious that these intervals will in most applications of risk-aware machines have to be estimated online. From a particular state, online estimation allows one to trigger a mitigation based on a severity threshold that codifies an unacceptable level of risk. Moreover, a risk structure makes this estimation explicit and potentially simpler. Overall, the $\mathfrak{R}_{\text {manual }}$ is a simple risk structure, yet showing many features of RISKSTRUCTURES. Figures 11a and 11b in Appendix B show a more complex structure for a set of six factors, generated by YAP in 66 milliseconds. The use of constraints leads to a focus on 24 out of the $4096\left(4^{6}\right.$ from using four-phase factors) risk states.

# 7.5. Discussion: compositional abstraction 

Event abstraction Events in the CSP interpretation are atomic observations [Ros10, Ch. 1.5]. The initiation and termination of events representing complex enduring real-world phenomena are to be viewed as non-separable aspects of these events. Consequently, care is necessary when making assumptions about the atomicity of such

[^0]
[^0]:    ${ }^{24}$ GNU/Octave, https://octave.sourceforge.io.
    ${ }^{25}$ To keep the model simple for the sake of illustration, the upper bound 12 takes into account the possibility that the driver might be able to regain control after the airbag deflates.

events interfering with other events. Nevertheless, we consider the event sets in Fig. 2b and their embedding into compound events (Sect. 7.1) useful to model the initiation, termination, or other significant events of the corresponding sub-processes (i.e., endangerment and mitigation processes) of $P$.

Any implementation of a risk structure as a safety controller needs to make an assumption about how shared resources, such as actuators, are used. In CSP, two processes (e.g. two factors) cannot engage in two different events on the same channel at the same time. Hence, resource sharing has to be implemented outside a risk structure, creating two cases: (a) mitigation actions of two factors mapping onto the same resource simultaneously occur and (b) a mitigation action competes with an action outside the safety controller. In case (a), signal priorities or more sophisticated signal merge functions may determine the control inputs to be forwarded. Case (b) suggests the use of a safety override, that is, giving priority to the safety controller.

Shared factor alphabet for compositional abstraction The side conditions in the rules of $\|$ (Definition 15) prohibit any behaviour leading to inconsistent states. The composition constrains the behaviour of two structures with an overlapping scope. Corollary 6 summarises our decisions on defining the constraint operator in such a way that Lemma 16 confirms this operator to form a refinement of a risk structure.

Were we to use arbitrary CSP processes for factors and were we to allow different interfaces for each use of the parallel composition operator, several structures, when composed, would not have guaranteed freedom from interference, exhibit different event and state traces and, consequently, the order of their composition would have led to different risk models. Associative laws for generalised parallel composition in CSP are not universally applicable. Discussions by Oliveira et al. [OCW09] and Roscoe [Ros10, p. 60] highlight how differences in the alphabets shared between each pair in a set of risk structures would entail meaning to the order in which these pairs are composed. For example, in CSP, the equality $(P \underset{X}{\|} Q) \underset{Y}{\|} R=P \underset{X}{\|}(Q \mid R)$ holds generally only if $X=Y$. In case of $X \neq Y$, one has to compare the traces of the composed processes to prove specific guarantees to be preserved by their composition. This can be computationally complex.

Overall, we obtain two advantages in RISKSTRUCTURES when using factors with an alphabet as described in Sect. 7.1. First, all factors have to always agree on their view of the same process $P$. Second, overlapping scopes in CSP terms then mean copies of factors that will be reduced by idempotency if deterministic (see Lemma 8). The transformation of factors into CSP (Sect. 7.1) encodes all the information from the risk space $R$ into the processes $0^{I}, f$, and $\bar{f}$. This way, we restrict the use of generalised parallel composition to the use of synchronous parallel composition [Ros10, p. 45].

Risk graphs and Yap The risk graphs in Figs. 7, 8 and 10 omit the transition self-loops for nominal, endangered, and mitigated operation because these are non-essential for endangerment and mitigation. Currently, YAP explores risk by changing (i.e., activating, mitigating) one factor at a time unless constraints such as causes are used. causes enforces the synchronisation of phase changes of involved factors. Because of input-enabledness from the compound event construction (Sect. 7.1), interleaving is avoided, but non-determinism can arise from nondeterministic factors. However, composition according to Definition 15 is more flexible because it allows several factors to change their phases simultaneously. This ability is exploited for the synthesis of safety controllers from YAP models in [GC20]. Furthermore, Definition 15 does not require input-enabledness but it relies on the alphabet defined in Sect. 7.1. Anyway, the use of a risk structure as a concurrent monitor or, more actively, as a safety controller, makes input-enabledness a useful requirement.

# 7.6. Discussion: uncertainty in RISKSTRUCTURES 

Recall the notion of risk as an action with an uncertain and undesired outcome. As summarised in Fig. 1, a risk structure focuses on such outcomes. ${ }^{26}$ Consequently, we propose risk structures as one way of formalising the irreducible (or aleatory) uncertainty associated with the actions of a risk-aware machine operated in a particular domain. Table 5 highlights low-level epistemic and aleatory uncertainties about a risk structure itself as a formal model of aleatory uncertainty in that domain, and as a model of a safety controller of that machine. Table 5 classifies these low-level uncertainties based on the discussion in [BFK13] and indicates how RISKSTRUCTURES incorporate and support the handling of these uncertainties.

[^0]
[^0]:    ${ }^{26}$ Desired or certain outcomes are not typically subject of operational risk analysis of autonomous machines.

Table 5. Summary of uncertainties inherent to and controllable in RisKStructures


Legend: ${ }^{1}$ analytic imprecision, ${ }^{2}$ physical parameter variability, ${ }^{3}$ parameter measurement, - not applicable

Non-deterministic and partial risk factors With non-deterministic factors (Sect. 4.4) in $\mathfrak{R}$, from an observed phase/event, $P$ can reach several distinct phases and, thus, risk states. Without further information, $\mathfrak{R}$ ceases to know which of these states was actually reached. $\mathfrak{R}$ would be in a risk state region, ordered and bounded by $\min _{\leq_{\mathrm{m}}} / \max _{\leq_{\mathrm{m}}}$ (Sect. 5.4), suggesting to express $\mathfrak{R}$ 's uncertainty by a risk interval. If factor phases carry information about $P$ 's state in terms of disjoint state invariants, we can build state estimators into $\mathfrak{R}$, able to gradually restore lost state information, narrow the interval, and again uniquely identify $P$ 's actual risk state. Following up on Sect. 4.4, if we can show that a risk structure is an Input/Output LTS and it can be transformed to a non-deterministic finite Mealy machine, the state estimation problem can be solved, for example, by homing algorithms used for passive testing [NSV03].

Partially specified risk factors (e.g. because of partial activation or mitigation analysis according to Tables 1b and 1c) may lead to sensible transitions $\tau_{\mathrm{c}}$ (cf. Sect. 7.3). Occurrences of $\tau_{\mathrm{c}}$ could be used to incrementally learn a property enforcer guided by unrealised events from risk factors.

# 8. Related work 

Following up Sect. 2.1, we summarise research on dependability modelling for repairable systems, algebraic methods for risk assessment, run-time monitoring, and risk-aware planning and control. We discuss the role of RisKStructures in the design of safety controllers.

From dependability analysis to RisKStructures Leveson and Stolzy [LS87] investigate reachability graphs of timed Petri nets with failure places to assess fault-tolerance of safety-critical real-time systems. RisKSTRUCTURES form a projection and compositional generalisation of such graphs when risk factors are used to model faults. Based on the annotation of a component architecture with a fault model, Unanue et al. [UPM18] show the synthesises of a failure automaton, a temporal fault/repair tree, and MCSs from this tree. From the failure automaton, they construct an extended Petri net to calculate failure probabilities to identify critical MCSs. Unanue et al.'s use of graphical models is intuitive and practical. A failure automaton corresponds to a risk structure with directly reducible risk factors modelling failure and repair. The commonalities of our framework with theirs suggests that RisKSTRUCTURES can use input from state-of-the-art dependability assessments of repairable systems for the design of safety controllers. At the moment, however, RisKStructures provide no direct support for modelling probabilistic actions.

As discussed in Sect. 6, FTs (Sect. 2.1) can be translated into RisKSTRUCTURES using factor dependencies. Because of the step semantics of constraints (cf. Definition 12), such a translation is also possible for PAND and POR gates ${ }^{27}$ used in dynamic FTs. This way, RisKSTRUCTURES can include a translation of FTs generated from

[^0]
[^0]:    ${ }^{27}$ These are AND and OR gates that also express priority in a FT by taking into account the order of event occurrences.

system architectures (see, e.g. [UPM18]). The expressiveness of risk factors enables the combination of Boolean factors modelling failures internal to an autonomous robot with factors modelling hazards in physical processes in this robot's environment.

Hansen et al. [HRS98] use the Duration Calculus to derive safety requirements from system FTs for the incremental design of safety-critical real-time controllers. We have shown an integration of FTA and incremental design in [GC17], however, from a less rigorous perspective. Because FTs can be modelled by RISKSTRUCTURES, an adoption of Hansen et al.'s approach suggests a refinement of the risk factors defined in Figs. 2a and 4 for deriving safety controllers for real-time systems.

Algebraic methods for risk assessment The only algebraic approach to design-oriented risk assessment, we could find, is from Hamdi and Boudriga [HB03]. They formalise IT security risk management as an algebraic datatype specification to check the consistency of security risk analyses viewed as algebras. Probability of occurrence and severity of consequence are modelled as metrics over attack actions to select optimal countermeasures using multi-objective optimisation. While focusing on security management, their algebraic datatype is an inspiration for a further formalisation of consequences and assets in Sect. 6.3. However, our action abstraction and the use of CSP offers a design method for safety controllers as opposed to the more abstract attack model proposed in [HB03], which focuses on risk assessment.

From RISKSTRUCTURES to safety monitors and controllers As mentioned for the comparison with [UPM18], each factor $f$ (Fig. 2) can be seen as a sequential monitor automaton for a process $P$, with $f$ 's events being triggered (i.e., sensors, variable checkers) by $P$ 's actions. A risk structure $\mathfrak{R}$ then forms a concurrent monitor of $P$ 's risk space, each risk state being concurrently monitored for the detection of endangerments (i.e., safety violations) and mitigation successes (i.e., mitigation acceptances).

Guiochet et al. [GPBB08] encode a risk model into a monitor automaton with partially ordered safety modes, each with a constraint limiting the parameters of robot actions to a mode-specific risk level. Refining this idea, Mekki-Mokhtar et al. [MMBG*12] distinguish between safe, warning, and catastrophic states with safety trigger conditions. Based on this framework, Machin et al. [MGW*18] apply model checking to determine whether catastrophic states can be reached despite such triggers. The authors present an algorithm for the synthesis of a mitigation policy, that is, minimal sequences of interventions to reach the nearest safe state from any warning state fulfilling validity, permissiveness, and safety. Our framework could enhance their refined hazard model with an algebraic method and the specification of dependencies between hazards.

Based on the MOP approach to RV [MJG*11], Huang et al. [HEZ*14] present a monitoring infrastructure for (i) checking trace properties (specified in different formalisms) observable from communications between ROS modules and (ii) the property-triggered execution of mitigations. Bogdiukiewicz et al. [BBH*17] describe how monitors can be formally developed in a step-wise manner using Event-B, an abstract state machine language supporting refinement-based development. RISKSTRUCTURES provide a bridge between formal risk modelling and the design of monitors in Event-B as shown in [BBH*17], in the ROS-specific MOP framework [HEZ*14], or the ROS-based framework proposed in [SLJS16].

From RISKSTRUCTURES to risk-aware control Works in (stochastic) optimal control [PBHS13, San14, FC14, MS14, SSSS18], summarised in Sect. 2.1, incorporate risk either as a (chance) constraint not to be violated or as a minimisation criterion for determining an optimal plan. The underlying stochastic models allow the perstate estimation of expected risk. Severity intervals would allow a per-state estimation of the expected risk range. Complementary to, for example, Sanger's neuronal network-based controller [San14], RISKSTRUCTURES provide an algebraic method for structuring and composing complex risk models (i.e., state spaces, value functions, action spaces) in a verifiable manner. Once a risk model is found and validated, optimal control provides the low-level mathematical framework for detailed controller design.

# 9. Conclusion 

The certification of autonomous systems requires the rigorous verification of their safety controllers. From the application of formal methods in other domains, we know that the emerging complexity of such controllers can be tackled by compositional verification. With RISKSTRUCTURES, we proposed a novel algebraic framework for the modelling and analysis of the risk profile of an automated or autonomous machine in its multi-scenario operational environment. This framework also supports the construction of discrete-event safety controllers that,

when integrated into the machine, improve this risk profile. These controllers incorporate an explicit and, thus, verifiable structure of the risk awareness of such a machine. The presented algebraic laws support the design of and reasoning about these controllers. The proposed theory was applied in form of situation/action/factor tables used to craft risk models with the YAP tool and resulted in the generation of risk graphs useful for controller design. To the best of our knowledge, this work is the first to provide an algebraic account of risk modelling and systematic safety controller design for risk-aware machines.

Future work Our work on this framework has led to a range of new research directions we want to pursue in the near future. The further development of our framework will include its extension to more general and more refined forms of risk factors; the elaboration of probabilistic factor semantics; the investigation of more specific mitigation orders, the construction of risk lattices from risk spaces, mitigation orders, and event structures; the development of analysers for risk estimation and synthesizers for safety controllers; the derivation of RISKSTRUCTURES from dynamical models; the further discussion of factor characteristics such as compatibility; the investigation of distributivity of composition and constraints; and a mechanisation and extension of further proofs using a specialised proof assistant such as Isabelle/UTP [FBC ${ }^{+} 20$ ].

# Acknowledgements 

Mario Gleirscher was supported in part by the German Research Foundation (DFG) under the Fellowship Grant no. 381212925. Work by Radu Calinescu and Mario Gleirscher was partially supported by the Lloyd's Register Foundation under the Autonomy Assurance International Programme (AAIP) Grant CSI:Cobot. Radu Calinescu was additionally supported by the UKRI Project EP/V026747/1 "Trustworthy Autonomous Systems Node in Resilience". We would like to thank Simon Foster for inspiring discussions on the use of relational specification; Ana Cavalcanti and Cliff Jones for insightful questions about the abstraction, composition, and methodology underlying RISKSTRUCTURES; James Baxter, Alvaro Miyazawa, and Pedro Ribeiro for enlightening conversations about CSP. We are also thankful to Sam Clark for helpful feedback on an early version of the introductory and closing sections.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Author Contributions. - Mario Gleirscher: Conceptualization, Methodology, Formal analysis and investigation, Writing - original draft preparation, Writing - review and editing, Funding acquisition. - Radu Calinescu: Writing - review and editing, Funding acquisition, Resources, Supervision. - Jim Woodcock: Formal analysis and investigation, Writing - review and editing, Resources, Supervision.

## Abbreviations

AV Autonomous vehicle
CSL Continuous stochastic logic
CSP Communicating sequential processes
CTMC Continuous time Markov chain
ETA Event tree analysis
FMEA Failure mode and effects analysis
FT Fault tree


# A. Proof details 

This section provides further proof details. The symbol $\varnothing$ indicates a discharged case distinction.
Proof of Lemma 1. The proof is by mutual existence and uniqueness: For each $\sigma \in R\left(F_{1} \cup F_{2}\right)$ (i) there exists a $\sigma_{1} \cup \sigma_{2} \in R\left(F_{1}\right) \otimes R\left(F_{2}\right)$ and (ii) this pair is unique, and (iii, iv) conversely.

Below, we will need the infix binary operator scheme $\cdot|_{F^{\prime}}: R(F) \rightarrow R\left(F^{\prime}\right)$ that describes the (phase-invariant) projection from $R(F)$ to $R\left(F^{\prime}\right)$ with $F^{\prime} \subseteq F$.

We show (i): Let $\sigma \in R\left(F_{1} \cup F_{2}\right)$, then, by definition, $\sigma$ is a total injection and, hence, every restriction of $\sigma$ is a total injection, particularly, the restrictions $\sigma|_{F_{1}}$ and $\sigma|_{F_{2}}$. Obviously, we have $\sigma|_{F_{1}}(\mathrm{f})=\sigma|_{F_{2}}(\mathrm{f})$ for all $\mathrm{f} \in F_{1} \cap F_{2}$. Furthermore, by definition, $\sigma(\mathrm{f})$ is faithful to $P h_{\mathrm{f}}$ for all $\mathrm{f} \in F_{1} \cup F_{2}$ and, thus, so are both these restrictions. These two results lead to $\sigma_{1}=\sigma|_{F_{1}} \in R\left(F_{1}\right)$ and $\sigma_{2}=\sigma|_{F_{2}} \in R\left(F_{2}\right)$ and, finally, to the existence of the wanted pair.

We show (ii): Suppose there are two pairs $\left(\sigma_{1}, \sigma_{2}\right) \neq\left(\sigma_{1}^{\prime}, \sigma_{2}\right) \in R\left(F_{1}\right) \otimes R\left(F_{2}\right)$. Then there exists $\mathrm{f} \in F_{1} \backslash F_{2}$ where $\sigma_{1}(\mathrm{f}) \neq \sigma_{1}^{\prime}(\mathrm{f})$, thus, also $\sigma_{1} \cup \sigma_{2} \neq \sigma_{1}^{\prime} \cup \sigma_{2}$. However, there can be no faithful total injection $\sigma \in R\left(F_{1} \cup F_{2}\right)$ such that $\sigma=\sigma_{1} \cup \sigma_{2} \wedge \sigma=\sigma_{1}^{\prime} \cup \sigma_{2}$.

We show (iii): For each $\sigma_{1} \cup \sigma_{2} \in R\left(F_{1}\right) \otimes R\left(F_{2}\right)$ there exists a $\sigma \in R\left(F_{1} \cup F_{2}\right)=\left\{\sigma \in\left(F_{1} \cup F_{2}\right) \rightarrow\right.$ $\bigcup_{\mathrm{f} \in F_{1} \cup F_{2}} P h_{\mathrm{f}} \mid \sigma$ is a total injection $\wedge \forall \mathrm{f} \in F_{1} \cup F_{2}: \sigma(\mathrm{f}) \in P h_{\mathrm{f}}$ ]: By definition, both $\sigma_{1}$ and $\sigma_{2}$ are faithful total injections (i.e., matching results for all $\mathrm{f} \in F_{1} \cap F_{2}$ ). Then, we can construct a faithful total injection $\sigma$ by applying set union to the domains and co-domains of these two. Thus, $\sigma \in R\left(F_{1} \cup F_{2}\right)$.

We show (iv): Suppose from $\sigma_{1} \cup \sigma_{2}$ we can construct $\sigma \neq \sigma^{\prime} \in R\left(F_{1} \cup F_{2}\right)$ then there exists $\mathrm{f} \in F_{1} \cup F_{2}$ such that $\sigma(\mathrm{f}) \neq \sigma^{\prime}(\mathrm{f})$. However, then either $\sigma_{1}$ or $\sigma_{2}$ must have violated injectivity which in turn would have violated the definition of $R\left(F_{1}\right) \otimes R\left(F_{2}\right)$.
Proof of Lemma 2. $(\mathcal{F}, \cup)$ is a semi-group because $\cup$ is an associative binary operation on $\mathcal{F}$. We have that

$$
\sigma_{1} \approx\left(\sigma_{2} \cup \sigma_{3}\right) \Leftrightarrow \sigma_{1} \approx \sigma_{2} \wedge \sigma_{1} \approx \sigma_{3}
$$

(The sub-proof based on the definition of $\approx$ is omitted here.) Based on Formula (17), we show by algebraic manipulation that the binary operation $\otimes$ on $\mathcal{R}$ is associative:

$$
\begin{aligned}
& R\left(F_{1}\right) \otimes\left(R\left(F_{2}\right) \otimes R\left(F_{3}\right)\right) \\
& =\left\{\sigma_{1} \cup \sigma \mid \sigma_{1} \in R\left(F_{1}\right) \wedge \sigma \in R\left(F_{2}\right) \otimes R\left(F_{3}\right) \wedge \sigma_{1} \approx \sigma\right\} \\
& =\left\{\sigma_{1} \cup\left(\sigma_{2} \cup \sigma_{3}\right) \mid \sigma_{1} \in R\left(F_{1}\right) \wedge\left(\sigma_{2} \cup \sigma_{3}\right) \in R\left(F_{2}\right) \otimes R\left(F_{3}\right) \wedge \sigma_{1} \approx\left(\sigma_{2} \cup \sigma_{3}\right)\right\} \\
& =\left\{\sigma_{1} \cup\left(\sigma_{2} \cup \sigma_{3}\right) \mid \sigma_{1} \in R\left(F_{1}\right) \wedge\left(\sigma_{2} \in R\left(F_{2}\right) \wedge \sigma_{3} \in R\left(F_{3}\right) \wedge \sigma_{2} \approx \sigma_{3}\right) \wedge \sigma_{1} \approx\left(\sigma_{2} \cup \sigma_{3}\right)\right\} \\
& =\left\{\left(\sigma_{1} \cup \sigma_{2}\right) \cup \sigma_{3} \mid\left(\sigma_{1} \in R\left(F_{1}\right) \wedge \sigma_{2} \in R\left(F_{2}\right)\right) \wedge \sigma_{3} \in R\left(F_{3}\right) \wedge \sigma_{2} \approx \sigma_{3} \wedge \sigma_{1} \approx\left(\sigma_{2} \cup \sigma_{3}\right)\right\} \quad \text { (by Formula (17)) } \\
& =\left\{\left(\sigma_{1} \cup \sigma_{2}\right) \cup \sigma_{3} \mid\left(\sigma_{1} \in R\left(F_{1}\right) \wedge \sigma_{2} \in R\left(F_{2}\right)\right) \wedge \sigma_{3} \in R\left(F_{3}\right) \wedge \sigma_{2} \approx \sigma_{3} \wedge \sigma_{1} \approx \sigma_{2} \wedge \sigma_{1} \approx \sigma_{3}\right\} \\
& =\left\{\left(\sigma_{1} \cup \sigma_{2}\right) \cup \sigma_{3} \mid\left(\sigma_{1} \in R\left(F_{1}\right) \wedge \sigma_{2} \in R\left(F_{2}\right) \wedge \sigma_{1} \approx \sigma_{2}\right) \wedge \sigma_{3} \in R\left(F_{3}\right) \wedge\left(\sigma_{1} \cup \sigma_{2}\right) \approx \sigma_{3}\right\} \\
& =\left\{\left(\sigma_{1} \cup \sigma_{2}\right) \cup \sigma_{3} \mid\left(\sigma_{1} \cup \sigma_{2}\right) \in R\left(F_{1}\right) \otimes R\left(F_{2}\right) \wedge \sigma_{3} \in R\left(F_{3}\right) \wedge\left(\sigma_{1} \cup \sigma_{2}\right) \approx \sigma_{3}\right\} \\
& =\left(R\left(F_{1}\right) \otimes R\left(F_{2}\right)\right) \otimes R\left(F_{3}\right)
\end{aligned}
$$

Hence, $(\mathcal{R}, \otimes)$ is a semi-group, too. Lemma 1 completes the proof.
Proof of Lemma 3.
We express the basic factor template from Fig. 2a in CSP as

$$
\begin{aligned}
\mathrm{f}_{(2 a)} & =0^{f} \\
0^{f} & =? x: e^{\mathrm{f}} \rightarrow f \square ? x: o_{n}^{\mathrm{f}} \rightarrow 0^{f} \\
f & =? x: m_{d}^{\mathrm{f}} \rightarrow 0^{f} \square ? x: o_{v}^{\mathrm{f}} \rightarrow f \square ? x: m^{\mathrm{f}} \rightarrow \bar{f} \\
\bar{f} & =? x: \bar{e}^{\mathrm{f}} \rightarrow f \square ? x: o_{m}^{\mathrm{f}} \rightarrow \bar{f} \square ? x: m_{r}^{\mathrm{f}} \rightarrow 0^{f}
\end{aligned}
$$

(As indicated in the Sect. 4.1 and 4.4, we consistently omit $\underline{e}^{\mathrm{f}}$ for the sake of simplicity.) Analogously, we express the factor template with isolated non-determinism from Fig. 4 in CSP as

$$
\begin{aligned}
\mathrm{f}_{(4)} & =0^{f} \\
0^{f} & =? x: e^{\mathrm{f}} \backslash u e^{\mathrm{f}} \rightarrow f \square ? x: o_{n}^{\mathrm{f}} \backslash u e^{\mathrm{f}} \rightarrow 0^{f} \square\left(? x: u e^{\mathrm{f}} \rightarrow\left(0^{f} \cap f\right)\right) \\
f & =? x: m_{d}^{\mathrm{f}} \rightarrow 0^{f} \square ? x: o_{v}^{\mathrm{f}} \backslash u m^{\mathrm{f}} \rightarrow f \square ? x: m^{\mathrm{f}} \backslash u m^{\mathrm{f}} \rightarrow \bar{f} \square\left(? x: u m^{\mathrm{f}} \rightarrow(f \cap \bar{f})\right) \\
\bar{f} & =? x: \bar{e}^{\mathrm{f}} \rightarrow f \square ? x: o_{m}^{\mathrm{f}} \backslash u m_{r}^{\mathrm{f}} \rightarrow \bar{f} \square ? x: m_{r}^{\mathrm{f}} \backslash u m_{r}^{\mathrm{f}} \rightarrow 0^{f} \square\left(? x: u m_{v}^{\mathrm{f}} \rightarrow\left(0^{f} \cap \bar{f}\right)\right)
\end{aligned}
$$

The inherent difference of the actions $m_{d}^{\mathrm{f}}, \bar{e}^{\mathrm{f}}$, and $\underline{e}^{\mathrm{f}}$ from their phase competitors allows us to make the simplifying assumption $\bar{e}^{\mathrm{f}} \cap o_{m}^{\mathrm{f}}=\bar{e}^{\mathrm{f}} \cap m_{v}^{\mathrm{f}}=\underline{e}^{\mathrm{f}} \cap o_{v}^{\mathrm{f}}=\underline{e}^{\mathrm{f}} \cap m^{\mathrm{f}}=\underline{e}^{\mathrm{f}} \cap m_{d}^{\mathrm{f}}=m^{\mathrm{f}} \cap m_{d}^{\mathrm{f}}=\varnothing$. We further define $u e^{\mathrm{f}}=o_{n}^{\mathrm{f}} \cap e^{\mathrm{f}}$, $u m^{\mathrm{f}}=o_{v}^{\mathrm{f}} \cap m^{\mathrm{f}}, u m_{r}^{\mathrm{f}}=o_{m}^{\mathrm{f}} \cap m_{r}^{\mathrm{f}}$. For the equivalence proof, we have to distinguish whether or not the events in the three sets $\left\{e^{\mathrm{f}}, o_{n}^{\mathrm{f}}\right\},\left\{m_{d}^{\mathrm{f}}, o_{v}^{\mathrm{f}}, m^{\mathrm{f}}\right\}$, and $\left\{\bar{e}^{\mathrm{f}}, o_{m}^{\mathrm{f}}, m_{r}^{\mathrm{f}}\right\}$ are pairwise disjoint.

Case 1: Events are pairwise disjoint. Then,

1. from the emptiness of $u e^{\mathrm{f}}, u m^{\mathrm{f}}$, and $u m_{r}^{\mathrm{f}}$,
2. from applying the CSP laws $? x: \varnothing \rightarrow P={ }_{F D} S T O P$ and $P \square S T O P={ }_{F D} P$ [Sch99, p. 93] to $\mathrm{f}_{(4)}$, and
3. from the resulting structure of $\mathrm{f}_{(4)}$ being equivalent to $\mathrm{f}_{(2 a)}$,
we immediately derive $\mathrm{f}_{(4)}=_{F D} \mathrm{f}_{(2 a)}$.
Case 2: Events are not pairwise disjoint. Then,
4. from the potential non-emptiness of $u e^{\mathrm{f}}, u m^{\mathrm{f}}$, and $u m_{r}^{\mathrm{f}}$,
5. from applying the step law of external choice [Sch99, p. 93] to $\mathrm{f}_{(2 a)}$ in order to isolate, for example, $? x$ : $o_{n}^{\mathrm{f}} \cap e^{\mathrm{f}} \rightarrow\left(0^{f} \cap f\right)$, and
6. from our definitions (e.g. $u e^{\mathrm{f}}=o_{n}^{\mathrm{f}} \cap e^{\mathrm{f}}$ ),
we again immediately have that $\mathrm{f}_{(2 a)}=_{F D} \mathrm{f}_{(4)}$. The cases 1 and 2 complete the proof.
The following corollary and its proof rule out potential errors in the proof of Lemma 4.

# Corollary 7 (Converse of Lemma 4) 

$$
\begin{aligned}
\neg\left(\sigma \preceq_{m} \sigma^{\prime}\right) & \Leftarrow \neg\left(\sigma \preceq_{m} \sigma^{\prime}\right) & & \text { (by definition of } \not \preceq_{m}, \not \preceq_{m} \\
\sigma \not \preceq_{m} \sigma^{\prime} & \Leftarrow \sigma \not \preceq_{m} \sigma^{\prime} & & \text { (by negation and definition of } \preceq_{m}, \preceq_{m} \\
\sigma>_{m} \sigma^{\prime} \vee\left(\left(\sigma, \sigma^{\prime}\right) \notin \preceq_{m} \wedge\left(\sigma^{\prime}, \sigma\right) \notin \preceq_{m}\right) & \Leftarrow \sigma>_{m} \bar{\sigma}^{\prime} \vee\left(\left(\sigma, \sigma^{\prime}\right) \notin \preceq_{m} \wedge\left(\sigma^{\prime}, \sigma\right) \notin \preceq_{m}\right)
\end{aligned}
$$

Proof of Corollary 7. Case 1: If $\left(\sigma, \sigma^{\prime}\right) \notin \preceq_{m} \wedge\left(\sigma^{\prime}, \sigma\right) \notin \preceq_{m}$ then (by Definitions 8 and 9) also $\left(\sigma, \sigma^{\prime}\right) \notin \preceq_{m} \wedge$ $\left(\sigma^{\prime}, \sigma\right) \notin \preceq_{m}$ and, therefore, Formula (18).

Case 2: If $\sigma>_{m} \sigma^{\prime}=\sigma^{\prime} \precsim_{m} \sigma \wedge \sigma^{\prime} \neq_{m} \sigma$, then we have either $\left(\sigma, \sigma^{\prime}\right) \notin \preceq_{m} \wedge\left(\sigma^{\prime}, \sigma\right) \notin \preceq_{m}$ (because of some incomparable phases) which fulfils Formula (18). Alternatively, we have $\left(\sigma^{\prime}, \sigma\right) \in \preceq_{m}$ which means $\sigma$ and $\sigma^{\prime}$ are fully comparable and, because of Corollary 2, we have $\sigma>_{m} \sigma^{\prime}$.
Proof of Lemma 5. For this we only need to show that any two risk states $\sigma, \sigma^{\prime} \in R$ are (i) comparable and (ii) antisymmetric: $[\sigma]_{\neg_{1}} \leq_{m}\left[\sigma^{\prime}\right]_{\neg_{1}} \wedge\left[\sigma^{\prime}\right]_{\neg_{1}} \leq_{m}[\sigma]_{\neg_{1}} \Rightarrow[\sigma]_{\neg_{1}}={ }_{m}\left[\sigma^{\prime}\right]_{\neg_{1}}$.

We show (i) by showing that the conditions (a) and (b) guarantee the comparability of any two risk states in $R$ based on the interval order $\leq$ as defined above and use the fact that comparability can be dropped from $R / \sim_{\mathrm{s}}$ to $R$ using $[\sigma]_{\neg_{1}} \leq_{m}\left[\sigma^{\prime}\right]_{\neg_{1}} \Longleftrightarrow \forall \hat{\sigma} \in\left[\sigma\right]_{\neg_{1}}, \hat{\sigma}^{\prime} \in\left[\sigma^{\prime}\right]_{\neg_{1}}: \hat{\sigma} \leq_{m} \hat{\sigma}^{\prime}$ (Formula (6)). Recall that we equate the empty interval with the empty set, $]=\varnothing$. Now, we have to consider the following three cases to complete the sub-proof of (i):

Case "no risk factors activated": [) $\geq[$ ) $\varnothing \varnothing \varnothing$ validates (b) and lack of comparability invalidates (a), yet we have $[\sigma]_{\neg_{1}} \leq_{m}\left[\sigma^{\prime}\right]_{\neg_{1}}$.

Case "at least one risk factor activated only in $\hat{\sigma}^{\prime}$ ": Let $[a, b)=S(\hat{\sigma}) .[a, b) \geq[) \vee[a, b) \subset \varnothing$ invalidates (a) and (b). However, the observation [) $\geq[a, b) \vee \varnothing \subset[a, b)$ yields $\left[\sigma^{\prime}\right]_{\neg_{1}} \leq_{m}[\sigma]_{\neg_{1}}$. The dual of this case works analogously.

Case "at least one risk factor activated in both $\hat{\sigma}, \hat{\sigma}^{\prime}$ ": Let $[a, b)=S(\hat{\sigma})$ and $[c, d)=S\left(\hat{\sigma}^{\prime}\right)$. We need to show $[a, b) \geq[c, d) \vee[a, b) \subset[c, d)$ for all $a, b, c, d \in \mathbb{R}$ : We can assume $a \leq b \wedge c \leq d$ by definition of intervals. Then, we face the case that

- $c \leq a \wedge d \leq b$ validates (a) by definition of $\leq$ over intervals,
- $c>a \wedge d \leq b$ validates (b),
- $c \leq a \wedge d>b$ implies (b) for the dual case $\left[\sigma^{\prime}\right]_{\neg_{1}} \leq_{m}[\sigma]_{\neg_{1}}$, or
- $c>a \wedge d>b$ implies (a) for the dual case.

Hence, from each of these four cases, either $[\sigma]_{\neg_{1}} \leq_{m}\left[\sigma^{\prime}\right]_{\neg_{1}}$ or $\left[\sigma^{\prime}\right]_{\neg_{1}} \leq_{m}[\sigma]_{\neg_{1}}$ follows.
Then, we show (ii) by contradiction: Assuming $[\sigma]_{\neg_{1}} \leq_{m}\left[\sigma^{\prime}\right]_{\neg_{1}} \wedge\left[\sigma^{\prime}\right]_{\neg_{1}} \leq_{m}[\sigma]_{\neg_{1}}$, we have $\forall \hat{\sigma} \in[\sigma]_{\neg_{1}}, \hat{\sigma}^{\prime} \in$ $\left[\sigma^{\prime}\right]_{\neg_{1}}: \hat{\sigma} \leq_{m} \hat{\sigma}^{\prime} \wedge \hat{\sigma} \geq_{m} \hat{\sigma}^{\prime}$ by dropping from $R / \sim_{\mathrm{s}}$. Now, we claim that $[\sigma]_{\neg_{1}} \neq_{m}\left[\sigma^{\prime}\right]_{\neg_{1}}$. Hence, $\exists \hat{\sigma} \in[\sigma]_{\neg_{1}}, \hat{\sigma}^{\prime} \in$ $\left[\sigma^{\prime}\right]_{\neg_{1}}: \hat{\sigma} \neq_{m} \hat{\sigma}^{\prime}$ and, consequently, $\exists \hat{\sigma} \in[\sigma]_{\neg_{1}}, \hat{\sigma}^{\prime} \in\left[\sigma^{\prime}\right]_{\neg_{1}}: \hat{\sigma} \not \leq_{m} \hat{\sigma}^{\prime} \vee \hat{\sigma} \not \geq_{m} \hat{\sigma}^{\prime}$. The latter contradicts our assumption.
Proof of Lemma 7. Fix a finite $F \subseteq \mathcal{F}$ and a pair $\sigma, \sigma^{\prime} \in R(F)$. The proof is by induction over $F$ and relies on the assumption that, for any $\mathrm{f} \in F$, the phase $f$ is the unique maximal element of $\preceq_{\mathrm{f}}$ and that active only returns such elements:

Induction start $F_{0}=\varnothing: \sigma\left|{ }_{\varnothing} \leq_{m} \sigma^{\prime}\right|_{\varnothing}$ holds trivially and so does active $\left(\sigma^{\prime}\right|_{\varnothing}$ ) $\subseteq$ active $\left(\sigma \mid{ }_{\varnothing}\right)$.
Induction step (IS) $F_{n+1}=F_{n} \cup\{\mathrm{f}\}$ where $n \geq 0$ and $\mathrm{f} \in F \backslash F_{n}$ : For the IH, assume $\sigma\left|{ }_{F_{n}} \leq_{m} \sigma^{\prime}\right|{ }_{F_{n}} \Rightarrow$ active $\left(\sigma^{\prime}\right|_{F_{n}}$ ) $\subseteq$ active $\left(\sigma \mid{ }_{F_{n}}\right)$. Then, we show that $\sigma\left|{ }_{F_{n+1}} \leq_{m} \sigma^{\prime}\right|_{F_{n+1}} \Rightarrow$ active $\left(\sigma^{\prime}\right|_{F_{n+1}}$ ) $\subseteq$ active $\left(\sigma \mid{ }_{F_{n+1}}\right)$ (i.e., the IS). For this, we prove

- the case of incomparable phases $\left(\sigma(\mathrm{f}), \sigma^{\prime}(\mathrm{f})\right) \notin \preceq_{\mathrm{f}}$ : In this case, the state pair gets incomparable and the implication is trivially fulfilled,
- the inverse case $\sigma(\mathrm{f})>_{\mathrm{f}} \sigma^{\prime}(\mathrm{f})$ : In this case, the state pair gets incomparable and the implication is again trivially fulfilled, and
- the aligned case $\sigma(\mathrm{f}) \preceq_{\mathrm{f}} \sigma^{\prime}(\mathrm{f})$ : In this case, the state pair stays comparable. However, $\sigma^{\prime}(\mathrm{f})$ can either be $f$ (hence, $\sigma(\mathrm{f})=f$ and maintaining $\subseteq$ ), $\bar{f}$ (hence, $\sigma(\mathrm{f}) \in\left\{f, \bar{f}, 0^{f}\right\}$ and maintaining $\subseteq$ ), or $0^{f}$ (see former sub-case).
Having proved these cases completes the induction step by establishing the IH.
For $\precsim_{m}$, we only have to substitute case 1 of the IS: For f , the smallest $\preceq_{\mathrm{f}}$ after Definition 3 implies incomparability at most for $\left(0^{f}, \bar{f}\right)$ and $\left(\bar{f}, 0^{f}\right)$. These two phase pairs of f would not alter the active maps of both states and hence maintain $\subseteq$ as well.

Proof of Lemma 12. From associativity of set intersection in Definition 12, we know that the order in which constraints are applied to $R \times R$ does not matter. Consequently, we also have $\llbracket k \rrbracket_{\mathrm{c}}^{R} \supseteq \llbracket\left\{k, k^{\prime}\right\} \rrbracket_{\mathrm{c}}^{R}$ for any $k, k^{\prime} \in \mathcal{C}$, that is, constraints only prune $R \times R$. First, we prove the lemma

$$
\left[[\mathfrak{R}](k)]_{C}=[\mathfrak{R}]_{(k) \cup C}\right.
$$

Fix $\sigma \xrightarrow{\kappa} \sigma^{\prime}$.
$\Rightarrow$ :

1. Case $\left(\sigma, \sigma^{\prime}\right) \in \llbracket k \rrbracket_{\mathrm{c}}^{R}:[-]_{C}$-step applies to $[\mathfrak{R}]_{(k)}$.
(a) Case $\left(\sigma, \sigma^{\prime}\right) \in \llbracket C \rrbracket_{\mathrm{c}}^{R}:[-]_{C}$-step applies also to $\left[[\mathfrak{R}]_{(k)}]_{C}\right.$. Then, $\left(\sigma, \sigma^{\prime}\right)$ must be in $\llbracket k \rrbracket_{\mathrm{c}}^{R} \cap \llbracket C \rrbracket_{\mathrm{c}}^{R}$, which by Definition 12 is $\llbracket\{k\} \cup C \rrbracket_{\mathrm{c}}^{R}$. Because of $\left(\sigma, \sigma^{\prime}\right) \in \llbracket\{k\} \cup C \rrbracket_{\mathrm{c}}^{R},[-]_{C}$-step applies to $[\mathfrak{R}]_{(k) \cup C}$ in the same way as it does to $\left[[\mathfrak{R}]_{(k)}]_{C} \cdot \square^{-}\right]_{C}$-cancel does not apply. Consequently, if $\sigma \xrightarrow{\kappa} \sigma^{\prime}$ is permitted (and added) by the left-hand side (LHS) then it is permitted by the right-hand side (RHS) of Formula (19).
(b) Case $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket C \rrbracket_{\mathrm{c}}^{R}:[-]_{C}$-cancel applies to $\left[[\mathfrak{R}]_{(k)}]_{C}\right.$ instead of $[-]_{C}$-step, resulting in the production of $\sigma \xrightarrow{\kappa} C \sigma$ rather than $\sigma \xrightarrow{\kappa} C \sigma^{\prime}$ on the LHS. Because $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket C \rrbracket_{\mathrm{c}}^{R}$, we have $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket\{k\} \rrbracket_{\mathrm{c}}^{R} \cap \llbracket C \rrbracket_{\mathrm{c}}^{R}$ and, by Definition 12, $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket\{k\} \cup C \rrbracket_{\mathrm{c}}^{R}$. Hence, $[-]_{C}$-cancel applies to RHS and produces $\sigma \xrightarrow{\kappa} C \sigma$.
2. Case $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket k \rrbracket_{\mathrm{c}}^{R}:[-]_{C}$-cancel applies to $[\mathfrak{R}]_{(k)}$ instead of $[-]_{C}$-step, producing $\sigma \xrightarrow{\kappa} C \sigma$ instead of $\sigma \xrightarrow{\kappa} C \sigma^{\prime}$ on the inner LHS.
(a) Case $(\sigma, \sigma) \in \llbracket C \rrbracket_{\mathrm{c}}^{R}:[-]_{C}$-step is applicable to $\left[[\mathfrak{R}]_{(k)}]_{C}\right.$, producing $\sigma \xrightarrow{\kappa} C \sigma$ for the outer LHS.
(b) Case $(\sigma, \sigma) \notin \llbracket C \rrbracket_{\mathrm{c}}^{R}:[-]_{C}$-cancel is applicable to $\left[[\mathfrak{R}]_{(k)}]_{C}\right.$, producing $\sigma \xrightarrow{\kappa} C \sigma$ for the outer LHS.

Because of $\llbracket\{k\} \cup C \rrbracket_{\mathrm{c}}^{R}=\llbracket k \rrbracket_{\mathrm{c}}^{R} \cap \llbracket C \rrbracket_{\mathrm{c}}^{R}$, in both cases (a) and (b), the $[-]_{C}$-cancel rule applies to $[\mathfrak{R}]_{(k) \cup C}$, producing a $\sigma \xrightarrow{\kappa} C \sigma$ on the RHS of Formula (19).
$\Leftarrow$ :

1. If $\left(\sigma, \sigma^{\prime}\right) \in \llbracket\{k\} \cup C \rrbracket_{\mathrm{c}}^{R}$ then $[-]_{C}$-step is applicable to $[\mathfrak{R}]_{(k) \cup C}$ and, because of $\llbracket k \rrbracket_{\mathrm{c}}^{R} \cap \llbracket C \rrbracket_{\mathrm{c}}^{R}$, to the inner and outer constraint in $\left[[\mathfrak{R}]_{(k)}]_{C}\right.$. Thus, if $\sigma \xrightarrow{\kappa} C \sigma^{\prime}$ is produced on the RHS then so on the LHS.
2. If $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket\{k\} \cup C \rrbracket_{\mathrm{c}}^{R}$ then $[-]_{C}$-cancel applies to $[\mathfrak{R}]_{(k) \cup C}$ and produces $\sigma \xrightarrow{\kappa} C \sigma$ on the RHS. However, because of $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket k \rrbracket_{\mathrm{c}}^{R} \cap \llbracket C \rrbracket_{\mathrm{c}}^{R}$, we have at least one of the two cases for the LHS:
(a) Case $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket k \rrbracket_{\mathrm{c}}^{R}$ : This matches case (2a), that is, $[-]_{C}$-cancel and $[-]_{C}$-step produce $\sigma \xrightarrow{\kappa} C \sigma$ for $\left[[\mathfrak{R}]_{(k)}]_{C}\right.$.
(b) Case $\left(\sigma, \sigma^{\prime}\right) \notin \llbracket C \rrbracket_{\mathrm{c}}^{R}$ : This matches either case (1b) or case (2b), that is, in both cases $[-]_{C}$-cancel and $[-]_{C}$-step produce $\sigma \xrightarrow{\kappa} C \sigma$ for $\left[[\mathfrak{R}]_{(k)}]_{C}\right.$.
Second, we show by induction over $C_{1}$ that the $[-]_{C}$-step and $[-]_{C}$-cancel rules apply in the same way to both sides of Formula (15).

Induction starts with $C_{1}^{0}=\varnothing$ : In this case, we have $\left[[\mathfrak{R}]_{\varnothing}\right]_{C_{2}}=[\mathfrak{R}]_{\varnothing \cup C_{2}}$ and by applying $[-]_{C}$-step or Definition 12 on the left and $\varnothing \cup C_{2}=C_{2}$ on the right, we get the tautology $[\mathfrak{R}]_{C_{2}}=[\mathfrak{R}]_{C_{2}}$.

IS with $C_{1}^{n+1}=C_{1}^{n} \cup\{k\}$ where $n \geq 0$ and $k \in C_{1} \backslash C_{1}^{n}$ : By assuming $\left[[\mathfrak{R}]_{C_{1}^{n}}\right]_{C_{2}}=[\mathfrak{R}]_{C_{1}^{n} \cup C_{2}}(\mathrm{IH})$, we show

$$
\begin{aligned}
& {\left[[\mathfrak{R}]_{C_{1}^{n+1}}\right]_{C_{2}}} \\
& =\left[[\mathfrak{R}]_{C_{1}^{n} \cup\{k\}}\right]_{C_{2}} \\
& \text { (by U-comm and Formula (19)) } \\
& =\left[\left[[\mathfrak{R}_{(k)}]_{C_{2}^{n}}\right]_{C_{2}}\right. \\
& \text { (by IH) } \\
& =\left[[\mathfrak{R}_{(k)}]_{C_{1}^{n} \cup C_{2}}\right. \\
& \text { (by Formula (19)) } \\
& =[\mathfrak{R}]_{\left(k\right) \cup C_{1}^{n} \cup C_{2}} \\
& \text { (by def) } \\
& =[\mathfrak{R}]_{C_{1}^{n+1} \cup C_{2}}
\end{aligned}
$$

![img-11.jpeg](img-11.jpeg)

Fig. 11. Risk structure for all factors mentioned in Sects. 4.3, 7.4

# B. Supplemental material for the road vehicle example 

Figures 11a and 11b contain two parts of a larger risk structure for the road vehicle example illustrated and discussed in the Sects. 7.4, 4.3, 3.
