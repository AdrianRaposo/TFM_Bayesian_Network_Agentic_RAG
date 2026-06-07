# Modelling of an Expert System for Diagnosing the Operational Status of a Diesel Genset 

Dejan BAREŠIĆ, Željko HEDERIĆ, Miralem HADŽISELIMOVIĆ


#### Abstract

The modelling of an expert system for diagnosing the operational status of a diesel genset represents the final stage of the research undertaken so far on military gensets. The research was undertaken in several stages on a large number of gensets, and the results obtained at specific research stages were published at scientific-expert conferences. For the purpose of modelling an expert system, a knowledge base was compiled based on detailed observation of the genset operational status, interviews with experts with many years of experience in maintaining military gensets and also on a breakdown of the occurred faults archived in the overhaul documentation. The paper uses only that one segment of the knowledge base that is necessary for modelling a simplified form of the Bayesian network for fault detection in assembled condition. In addition to input probabilities, the results of diagnostic tests and simulations carried out in the Matlab Simulink program package are also entered in the Bayesian network. Fault detection represents a complex process so the application of an expert system significantly reduces the time needed for fault detection, resulting in optimized maintenance. It is especially significant in military and similar organizations which apply a large number of technical resources. The Bayesian network is processed in the GeNIe program package.


Keywords: diagnosing the operational status; expert system; fault detection;genset; maintenance optimization

## 1 INTRODUCTION

In complex systems, such as military organizations, various technical resources are used which require a high degree of reliability and availability. This implies having a well-developed maintenance system capable of establishing a working capacity of defective resources in the shortest possible time. Therefore, continuous efforts are devoted to improving methods that contribute to the maintenance optimization and the productivity of the technical repair shops [1].

When it comes to complex technical resources, such as gensets, a lot of time during the maintenance process is used to determine the technical condition, i.e. to detect a fault. In order to shorten the fault detection time, an expert system for detection is developed, with the purpose of defining the place of a hard-to-detect fault on the basis of easily detectable faults in the assembled condition.

For proper operation of the expert system, it is important to have a reliable "base of knowledge" [2]. In order to develop a knowledge base that includes the probabilities of occurrence of certain faults, a survey of specialized mechanics with years of experience in genset maintenance was carried out. In addition to the survey, an analysis of faults recorded in the last 15 years in the maintenance logbooks was also carried out. The collected data are processed in the GeNIe program package which, by applying the Bayesian method [3], calculates real values which increase or decrease the probability of certain faults.

In order to model the Bayesian network and further develop the knowledge base, it is necessary to have real indicators such as diagnostic tests. In this case, the results of genset output characteristics were used, partially gained through measurements, partially through computer simulation using the developed simulation model shown in Fig. 6. The purpose of the results of diagnostic tests that are entered into the Bayesian network, partially shown in Fig. 1, is to decide where a hard-to-detect fault had occurred.

## 2 EXPERT SYSTEM MODELING 2.1 Bayesian Method

The processing of collected information is carried out according to Bayes' method which is based on the classical probability theory. With help of the conditional probability the probability of an event $y$ is determined, if it is known that the event $x$ has occurred. Event $x$ is considered the information obtained by the sensor, whereas $y$ represents the probability of the state of the genset, i.e. the probability of a certain failure which needs to be defined. This probability is called conditional probability $p(y \mid x)$.
$p(y \mid x)=\frac{p(x \wedge y)}{p(x)}$,
If two events are independent, then

$$
\begin{aligned}
& p(x \mid y)=p(x) \\
& p(y \mid x)=p(y)
\end{aligned}
$$

According to the definition, the revolution, i.e. probability of the event x under the condition that y has occurred is:

$$
\begin{aligned}
& p(x \mid y)=\frac{p(y \wedge x)}{p(y)} \\
& \text { From (7) } \Rightarrow p(y \wedge x)=p(x \mid y) p(y)
\end{aligned}
$$

Because of the commutativity

$$
p(x \wedge y)=p(x \mid y) p(y)
$$

Including (6) in (1) we get the simplest form of Bayes' theorem.

$$
p(y \mid x)=\frac{p(x \mid y) p(y)}{p(x)}
$$

$$
\begin{aligned}
& p(x)=p(x \wedge y)=p(x \wedge(y \vee \sim \mathrm{y}))= \\
& p((x \wedge y) \vee(x \wedge \sim y))
\end{aligned}
$$

From the definition of probability

$$
\begin{aligned}
& (x \wedge y) \cap(x \wedge \sim y)=\Phi \\
& p(x)=p(x \wedge y)+(x \wedge \sim y) \\
& p(x \wedge y)=p(x \mid y) p(y) \\
& p(x \wedge \sim y)=p(x \mid \sim y) p(\sim y) \\
& p(x)=p(x \mid y) p(y)+p(x \mid \sim y) p(\sim y)
\end{aligned}
$$

By expanding the members based on the definition of the conditional probability, we get Bayes' theorem

$$
p(y \mid x)=\frac{p(x \mid y) p(y)}{p(x \mid y) p(y)+p(x \mid \sim y) p(\sim y)}
$$

From Bayes' theorem we get the Bayesian method in production systems:

IF $x$ is true, the conclusion is $Y$ with the probability $p$.
With the help of Bayes' theorem we can conclude the probability of $X$.

By interpreting this theorem with the formula (7):

- $Y$ of the theorem marks an evidence or a fact $\rightarrow E$
- $X$ of the theorem marks a hypothesis $\rightarrow H$

$$
\begin{aligned}
& p(H \mid E)=\frac{p(E \mid H) p(H)}{p(E)} \\
& p(H \mid E)=\frac{p(E \mid H) p(H)}{p(E \mid H) p(H)+p(E \mid \sim H) p(\sim H)}
\end{aligned}
$$

### 2.2 Bayesian Network

The Bayesian network represents a knowledge structure and models the relationship between possible faults, their causes, information on the genset and diagnostic tests.

Fault detection is undertaken based on principles similar to those elaborated in an example from the field of medicine regarding the diagnosis of a disease in a patient [4]. Fig. 1 shows the Bayesian network of a simplified expert system for fault detection on a genset in assembled condition, prepared in the GeNIe program package. The same principles apply to the operation of a complex expert system with a much larger number of knots developed for detecting faults on military gensets.
The knowledge about the relationships between variables is modelled by causal relationships and local distributions of conditional probabilities. The propagation algorithm processes information on the relationships between variables, resulting in unconditional or marginal distributions of the probabilities of each knot.

Unconditional or marginal knot probabilities are a probability function of that knot.

The entry of records on the genset, such as its age and location of use, changes the probability in the relevantly connected knots. The information is propagated through the network and changes the functions of probability in dependant knots.

After the known records on the resource are entered, diagnostic tests are carried out in assembled condition, such as the verification of dynamic frequency characteristics and genset output voltage. The following data were entered into the example of a network from Fig. 1 which includes predefined local conditional probabilities:

- the resource is old (more than 15 years)
- the resource has not been used in international military operations
- the resource was stored in a strategic reserves warehouse (for the last 5 years)
- during the test, the dynamic frequency characteristic did not meet the requirements
- genset output voltage met the requirements.

The results of processed data in the GeNIe program package are shown in Fig. 2. The Bayesian network, depicted in Fig. 1, was generated in the GeNIe program package. Its structure reveals the connection among variables assigned with apriori probabilities. The apriori probabilities are known from previous research. For example, it has been established that $40 \%$ of the gensets brought in for maintenance into technical repair shops are more than 15 years old and $60 \%$ of them are less than 15 years old. Faults are observed on the same principles. All the data on the apriori probabilities have been entered in the network, after which data were entered for the particular resource, and these reveal, for example, whether the resource is under or over 15 years of age. Based on the apriori probabilities and the input data, the GeNIe program package performs the calculation according to the Bayesian method and presents data as shown in Fig. 2.

The results shown lead to the conclusion that, in case of a genset older than 15 years, kept in a strategic reserves warehouse, the most probable fault occurs on the fuel supply line under the condition that the dynamic frequency characteristic had deviated. The frequency characteristic is directly connected to the rotation speed of a synchronous generator simulated for various faults in the Matlab Simulink program package and shown in the figures in the next chapter.

The Bayesian network in Fig. 1 shows that 4 different faults were considered:

- Generator stator fault
- Generator excitation system breakdown
- Short circuit on the generator excitation system
- Fuel supply line fault

The indicated faults depend on information on the genset recorded in technical documentation:

- year of production (age)
- place and manner of use (a resource stored in a strategic reserves warehouse or used in international military operations or in the Republic of Croatia)

In addition to the recorded information, the probability of a certain fault also depends on the output characteristics of the genset, such as:

- dynamic frequency characteristic
- generator output voltage.

The output characteristics are verified by measurement and compared with the characteristics obtained by simulating faults in the Matlab Simulink program package.

The above mentioned data were entered in the example from Fig. 2 for which the greatest probability (97 %) was obtained for a fault in the fuel supply line. This was also confirmed by examples from practice where, in starting gensets that had spent a significant amount of time in a warehouse, faults occurred in the fuel supply line. These were mostly blockages caused by corrosion building up in tanks that are mostly made of metal on older types of resources. In the older gensets, in addition to blockage, air also appears in the fuel supply lines due to longer periods of non-use of the resource and the deterioration of rubber pipes and seals on the fuel supply line which is also considered a fault on the fuel supply line. The indicated fault causes a disruption in fuel supply which directly affects the power of the driving diesel engine [5]. The oscillation of power under nominal load causes uneven operation which, in the diagnosis, manifests as oscillations of the generator output voltage frequency.

![img-0.jpeg](img-0.jpeg)

**Figure 1** Bayesian network for fault detection on a genset

![img-1.jpeg](img-1.jpeg)

**Figure 2** Determining fault probability based on information and diagnostic tests

## 3 DIAGNOSTIC TESTS OF GENSETS WITH THE PURPOSE OF FAULT DETECTION

In maintenance centers and technical workshops, activities are carried out following the prescribed technological process according to which first the Logbook on the receipt of resources for maintenance is made. Along with other information on the resource, malfunctions perceived by the user are also entered in the Logbook. The next step is to prepare for repairs and diagnostics in the assembled condition, which is a complex problem, especially when it comes to the complex system such as gensets. The established method so far has been to, if possible, start the engine, bring the genset in a synchronous rotation speed and record genset output characteristics. The testing is carried out according to the Product Quality Regulation (hr. Propis o kvaliteti proizvoda; PKP), if it is unavailable, according to [6]. According to the Product Quality Regulation, a genset is first tested in idle and then under load. Technical workshops are equipped with working (resistive) load, which satisfies the prescribed testing. The conducted testing can be used to detect simpler faults in the assembled condition. Nowadays, there are various software tools that can simulate different faults, which is significant for the diagnosis of more complex faults. In order to simplify fault diagnosis, the goal is to
develop an Expert System whose work is based on an as credible as possible "knowledge base". As stated earlier, a "knowledge base" including the probabilities of occurrence of certain faults has been set up. In order to detect a fault according to the Bayesian network (Fig. 1), it is also necessary to have the results of diagnostic tests which include the results of measurements and simulations performed. Therefore, within the framework of this paper, a genset simulation model has also been developed using the Matlab Simulink program package which enables simulation of genset faults and which was used to gain an overview of output characteristics. Gensets are complex resources consisting of an internal combustion engine, synchronous generator and automated control system, where a wide range of errors is possible. In order to simplify the overview of simulation results and reduce the number of diagnostic tests, this paper focuses on faults on synchronous generators. The research previously conducted on the generators of military gensets found most common faults on the excitation system, followed by the armature winding of the generator (Fig. 3). The conducted research most often focused on mobile diesel gensets with synchronous brushless generators whose excitation system is based on a three-phase synchronous exciter with a cylindrical armature on the rotor and salient poles on the stator with concentric excitation winding [7-9].
![img-2.jpeg](img-2.jpeg)

Figure 3 Schematic of the synchronous brushless generator with discussed fault

### 3.1 Identified Faults in the Generator Excitation System

The most common faults on the excitation system of a synchronous brushless generator are faults on rectifier diodes (breaks of contact and short circuiting of diodes) that have been elaborated so far [10, 11]. Apart from these faults, faults caused by break of contact and short circuits between phases of the exciter rotor have also been observed on the excitation system of military gensets [12]. Loose contact, i.e. breaks of contact appear under the screw connection that connects conductors of the exciter rotor and rotating rectifier (position A in Fig. 4). Short-circuiting occurs between two phases of the exciter rotor (position B, Fig. 4).
![img-3.jpeg](img-3.jpeg)

Figure 4 The rotating rectifier in the system of genset (1 - carrier of the rectifier, 2 - diode group output plus, 3 - diode group output minus, 4 - varistor)

One of the causes of these faults is a centrifugal force which occurs due to the rotation of the exciter rotating system, which are particularly pronounced in resources used in the field of international military operations for supplying equipment operating at the frequency of 60 Hz . In addition to the centrifugal forces, another cause of faults on the excitation system are also increased currents of the excitation winding which depend on the type of coupled load, and also increase when the rotation speed is reduced under nominal loads. A decrease in rotation speed has been observed in connection with the use of kerosene-based fuel JP-8 (F-34) which is also used to fuel diesel generators in international military operations [13].
![img-4.jpeg](img-4.jpeg)

Figure 5 Short-circuiting of armature winding (C - short circuit between armature winding and ground, D - short circuit between phases of armature winding)

### 3.2 Identified Faults on the Armature Winding of the Generator

The largest number of faults on armature windings of the previously mentioned generator construction was
identified on the connection between one phase and the ground (case C in Fig. 5), followed by the short circuit between two phases of generators (case D in Fig. 5). These faults have mostly been detected in older gensets and very rarely appear in newer gensets. This is associated with the aging of the winding insulation, which results in a reduction of insulation resistance and breakdown in the most critical places.

## 4 SIMULATION OF THE OUTPUT CHARACTERISTICS IN CASE OF FAULT

In order to make the right decisions regarding a fault, knowledge of the behavior of resources, i.e. the output characteristics in the case of a fault is necessary. For this purpose, a simulation model has been developed using the Matlab Simulink program package shown in Fig. 6, and a series of simulations have been conducted, a part of the results is shown in Fig. 7 to 12. The simulation results are to be used to supplement the "knowledge base", i.e. as diagnostic tests necessary to reach decisions in the Bayesian network displayed in Fig. 1. The results of fault simulations are compared with the results of diagnostic tests carried out in technical workshops on the resources being overhauled. The comparison is used to reach a decision on the validity of output characteristics (voltage and frequency). Based on that, the expert system defines the voltage and frequency condition (Normal, Abnormal).
![img-5.jpeg](img-5.jpeg)

Figure 6 Basic model for simulating generator faults

### 4.1 Loose contact on the rotating rectifier

In Fig. 7, the blue line shows the rotation speed of the generator obtained through simulation, which coincides with the real results obtained through measurements according to the Protocol on the Quality of Products under Nominal Load. The rotation speeds obtained through fault simulation, i.e. loose contact on a rotating rectifier, are shown in red and brown. The oscillation of speed under nominal load is shown in red, while the oscillation of speed under $25 \%$ of nominal load is shown in brown. The obtained results also confirm the expert system model, i.e. the "knowledge base" obtained through the survey of workers and the analysis of faults recorded at resource
maintenance. The obtained results confirm the link between Checking the static frequency characteristics (rotation speed) and loose contact on the voltage regulator [14], although the rotation speed is regulated with a separate regulator on the diesel engine.

Fig. 8 shows the results of simulation of generator voltage. In order to simplify the image, during the first ten seconds, work in the health condition was simulated, while after the ten seconds, a fault on the rotating rectifier (loose contact) occurs, with oscillations in the output voltage.

Fault occurrence was simulated during the operation of a genset. For the first ten seconds, the genset works properly (sound condition), after which the fault occurs on the rotating rectifier (fault condition).

![img-6.jpeg](img-6.jpeg)

Figure 7 Rotation speed of the generator in health condition and in fault condition under 100% and 25% of load

![img-7.jpeg](img-7.jpeg)

Figure 8 Generator output voltage in two different conditions (sound condition for the first ten seconds, fault condition after the first ten seconds)

![img-8.jpeg](img-8.jpeg)

Figure 9 The rotation speed in the health condition and in the state of a short circuit between two phases of the exciter

### 4.2 Short Circuit Between Phases of Exciter Rotor

Fig. 9 displays the relation between the rotation speed in the health condition under nominal load (blue curve) and the rotation speed in the event of a short circuit between two phases of exciter rotor occurring in the fifth second of the simulation, whereby the red line displays speed under nominal load, and brown line under 25% nominal load.

Fig. 10 displays generator voltage, that is, during the first 5 seconds, work in the health condition was simulated, while afterward a short circuit between phases of exciter rotor was simulated, which caused an obvious drop in generator voltage.

![img-9.jpeg](img-9.jpeg)

Figure 10 Generator output voltage at the occurrence of a short circuit between phases of exciter rotor in the fifth second

### 4.3 Short Circuit Between One Phase of Armature Winding and Ground

A short circuit between one phase and ground occurs due to the breakdown of the generator winding insulation. Fig. 11 displays simulation of the generator rotation speed in two cases. The first case (red curve) displays the rotation speed when the generator short-circuited (ground breakdown) already before the beginning of the testing. The second case (brown line) displays the rotation speed when the short circuit occurs in the fifth second of the testing (ground breakdown). This can actually happen because the contact resistance in the idle state and of unheated resource can be somewhat higher, while during testing, vibration and increase in temperature results in a reduction in contact resistance.

![img-10.jpeg](img-10.jpeg)

Figure 11 Generator rotation speed in case of a short circuit between one phase of armature winding and ground

### 4.4 Short Circuit Between Two Phases of Armature Winding

Fig. 12 shows the generator rotation speed in the event of a short circuit between two generator phases.

As in the previous example, the red curve displays the generator rotation speed when the breakdown occurred before the testing, while the brown curve shows the

generator rotation speed when breakdown occurs during testing.

![img-11.jpeg](img-11.jpeg)

Figure 12 Generator rotation speed in cases of short circuit between two phases of armature winding

## 5 CONCLUSION

The paper shows an expert system model developed for fault detection on military gensets. The advantage of this model is the possibility of fault detection in assembled condition which significantly reduces the repair time and contributes to optimized maintenance of technical resources. This model is suitable for military and similar organizations which use a large number of resources taken into consideration and for which there is updated documentation on prior faults which significantly contributes to the credibility of the "knowledge base". By applying the Bayesian network developed in the GeNle program package, the decision is made on the probability of occurrence of a particular fault. First, the known information on the genset are entered into the Bayesian network, after which the results of diagnostic tests obtained by measurement, compared with simulation results beforehand, are verified and entered. Simulations were carried out in the Matlab Simulink program package which simulates genset behaviour in case of occurrence of certain faults.

The indicated expert system model can also be adjusted for fault detection on other non-military and military systems.

## Contact information:

Dejan BAREŠIĆ, PhD student
Croatian Military Academy "Dr. Franjo Tuđman"
Ilica 256b, 10000 Zagreb, Croatia
E-mail: dejan.baresic@morth.hr
Željko HEDERIĆ, PhD, Associate Professor
J. J. Strossmayer University of Osijek, Faculty of Electrical Engineering, Computer Science and Information Technology
Ul. kneza Trpimira 2B, 31000 Osijek, Croatia
E-mail: zhederic@etfos.hr
Miralem HADŽISELIMOVIĆ, PhD, Professor
University of Maribor, Faculty of Energy Technology
Hočevarjev trg 1, 8270 Kriško, Slovenia
E-mail: miralem.h@um.si